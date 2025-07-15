---
name: OPNsense
description: ¿Cómo se instala y configura un cortafuegos OPNsense?
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian BURNEL publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



En este tutorial, echaremos un vistazo al cortafuegos de código abierto OPNsense. Veremos sus principales características, los requisitos previos y cómo instalar esta solución basada en FreeBSD.



Antes de empezar, debes saber que **OPNsense y pfSense son cortafuegos de código abierto** basados en FreeBSD. Podemos decir que pfSense es una especie de hermano mayor de OPNsense, ya que este último es un Fork creado en 2015. Por último, es importante señalar que desde 2017, **OPNsense ha cambiado a HardenedBSD en lugar de FreeBSD**. HardenedBSD es una versión mejorada de FreeBSD, con características de seguridad avanzadas



OPNsense destaca por su Interface de usuario más moderno y **una cadencia de actualización más frecuente**. De hecho, el calendario de actualizaciones de OPNsense incluye dos versiones principales al año, que se actualizan cada dos semanas aproximadamente (dando lugar a versiones menores). Este seguimiento es muy interesante en comparación con pfSense, si nos fijamos en las versiones comunitarias de estas soluciones.



![Image](assets/fr/050.webp)



## II. Características de OPNsense



OPNsense es un sistema operativo diseñado para actuar como cortafuegos y enrutador, aunque sus funciones son numerosas y pueden ampliarse instalando paquetes adicionales. Adecuado para su uso en producción, se utiliza principalmente para la seguridad de la red y la gestión de flujos.



### A. Características principales



Estas son algunas de las principales características de OPNsense:





- Cortafuegos y NAT**: OPNsense proporciona funciones avanzadas de cortafuegos de estado con filtrado de estado, así como funciones de traducción de red Address (NAT).





- DNS/DHCP**: OPNsense puede configurarse para gestionar servicios DNS y DHCP en la red. Puede actuar como un servidor DHCP, pero también puede ser utilizado como un resolver DNS para las máquinas en la red local. Dnsmasq también está integrado por defecto.





- VPN**: OPNsense soporta varios protocolos VPN, incluyendo IPsec, OpenVPN y WireGuard, permitiendo conexiones seguras para acceso remoto a estaciones de trabajo móviles o interconexión de sitios.





- Proxy web**: OPNsense incluye un proxy web para controlar y filtrar el acceso a Internet. También puede utilizarse para filtrar contenidos y gestionar el acceso a la red.





- Gestión del ancho de banda (QoS)**: OPNsense ofrece funciones de gestión de calidad de servicio (QoS) para priorizar el tráfico de red y gestionar mejor el ancho de banda de la red.





- Portal cautivo**: esta funcionalidad permite gestionar el acceso de los usuarios a la red a través de una página de autenticación (base local, vales, etc.). Se trata de una función muy utilizada en las redes Wi-Fi públicas.





- IDS/IPS**: OPNsense integra Suricata para ofrecer funciones de detección y prevención de intrusiones (IDS/IPS) para proteger la red contra ataques.





- Alta disponibilidad (CARP)**: OPNsense soporta CARP (*Common Address Redundancy Protocol*) para alta disponibilidad entre múltiples cortafuegos OPNsense, asegurando que el servicio permanece activo incluso en caso de fallo de hardware.





- Informes y supervisión**: OPNsense proporciona herramientas de informes y supervisión en tiempo real para realizar un seguimiento del rendimiento de la red (con NetFlow) y detectar posibles problemas, gracias a la creación de registros. Esto incluye gráficos. La herramienta Monit está integrada en OPNsense y permite supervisar el propio cortafuegos.



### B. Paquetes adicionales



Esto es sólo un resumen de las funciones que ofrece OPNsense. Además, el **catálogo de paquetes** accesible desde la administración de OPNsense Interface le permite **enriquecer el cortafuegos con funcionalidades adicionales**. Estas incluyen un cliente ACME, un agente Wazuh, el servicio NTP Chrony, y Caddy como proxy inverso.



![Image](assets/fr/051.webp)



## III. Requisitos previos de OPNsense



En primer lugar, debe decidir dónde va a instalar OPNsense. Hay varias soluciones posibles, incluyendo la instalación en :





- Un hipervisor como máquina virtual, ya sea Hyper-V, Proxmox, VMware ESXi, etc.
- Una máquina como sistema *bare-metal*. Podría ser un mini PC que actúe como cortafuegos.



También puede adquirir **un dispositivo OPNsense para montaje en bastidor** a través de nuestra tienda en línea.



Debe tener en cuenta los recursos de hardware necesarios para ejecutar OPNsense. Esto se detalla en [esta página de documentación](https://docs.opnsense.org/manual/hardware.html).



**Recursos mínimos y recomendados para la producción:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Por último, **sus necesidades de recursos dependen sobre todo del número de conexiones a gestionar**, y por tanto de **sus necesidades de ancho de banda**. Además, hay que **tener en cuenta los servicios que se van a activar y utilizar** (proxy, detección de intrusos, etc.), ya que pueden consumir mucha CPU y/o RAM.



También necesitará la imagen ISO de instalación de OPNsense, que puede descargar desde [el sitio web oficial](https://opnsense.org/download/). Para la instalación en una máquina virtual, seleccione "**dvd**" como tipo de imagen para obtener una imagen ISO (y haga lo que quiera con ella...). Para la instalación a través de una llave USB de arranque, selecciona la opción "**vga**" para obtener un archivo "**.img**".



![Image](assets/fr/048.webp)



También necesitará un ordenador para la administración y las pruebas de OPNsense.



## IV. Configuración del objetivo



Nuestro objetivo es





- Cree una red virtual interna (192.168.10.0/24 - LAN)**, que pueda acceder a Internet a través del cortafuegos de OPNsense. Para uso en producción, esta podría ser su red local, por cable y/o Wi-Fi.
- Activar y configurar NAT** para que las máquinas virtuales de la red virtual interna puedan acceder a Internet
- Activar y configurar el servidor DHCP en OPNsense** para distribuir una configuración IP a las futuras máquinas conectadas a la red virtual interna
- Configure el cortafuegos** para permitir sólo los flujos salientes de LAN a WAN en HTTP (80) y HTTPS (443).
- Configure el cortafuegos** para permitir que la LAN virtual utilice OPNsense como servidor DNS (53).



Si utiliza la plataforma Hyper-V, obtendrá la siguiente representación:



![Image](assets/fr/033.webp)



## V. Instalación del cortafuegos OPNsense



### A. Preparación de la llave USB de arranque



El primer paso es preparar el medio de instalación: **la llave USB de arranque con OPNsense**. Por supuesto, esto es opcional si está trabajando en un entorno virtual, pero en cualquier caso necesita descargar la imagen ISO de instalación de OPNsense.



Tras la descarga, obtendrás **un archivo que contiene una imagen en formato ".img "**. Puedes **crear una memoria USB de arranque** con varias aplicaciones, entre ellas **balenaEtcher**: ultrasencilla de usar. Además, la aplicación reconocerá la imagen en el archivo, por lo que no tendrás que descomprimirla previamente.





- [Descargar balenaEtcher](https://etcher.balena.io/)



Una vez instalada la aplicación, selecciona tu imagen, tu llave USB y pulsa el botón "¡Flash! Espere un momento.



![Image](assets/fr/049.webp)



Ahora estás listo para instalar.



### B. Instalación del sistema OPNsense



Inicie la máquina que aloja OPNsense. Debería ver una página de bienvenida similar a la siguiente. Durante unos segundos, la pantalla mostrada será visible en la ventana. Deje que el proceso siga su curso...



![Image](assets/fr/019.webp)



La imagen OPNsense se carga en la máquina, de modo que se puede acceder al sistema en modo "**vivo**", es decir, almacenado temporalmente en la memoria.



![Image](assets/fr/025.webp)



Entonces llegarás a un Interface similar al de abajo. Entra con el login "**installer**" y la contraseña "**opnsense**". Tenga en cuenta que el teclado es **QWERTY** por el momento. En este punto, vamos a **iniciar el proceso de instalación de OPNsense**.



![Image](assets/fr/026.webp)



Aparece un nuevo asistente en la pantalla. El primer paso consiste en seleccionar la distribución de teclado correspondiente a su configuración. Para un teclado AZERTY, seleccione la opción "**Francés (teclas acentuadas)**" de la lista y, a continuación, haga doble clic**.



![Image](assets/fr/027.webp)



El segundo paso es seleccionar la tarea a realizar. En este caso, vamos a realizar una instalación utilizando el **sistema de archivos ZFS**. Sitúate en la línea "**Instalar (ZFS)**" y confirma con **Intro**.



![Image](assets/fr/028.webp)



En el tercer paso, seleccione "**stripe**", ya que nuestra máquina está equipada con **un solo disco**: no hay redundancia posible para asegurar el almacenamiento del cortafuegos y sus datos. Esto es particularmente relevante cuando se instala en una máquina física para proteger contra fallos de hardware de un disco, a través del principio RAID.



![Image](assets/fr/029.webp)



En el cuarto paso, sólo tiene que pulsar **Intro** para confirmar.



![Image](assets/fr/030.webp)



Por último, confirme seleccionando "**SÍ**" y pulsando la tecla **Intro**.



![Image](assets/fr/031.webp)



Ahora tendrá que esperar mientras se instala OPNsense... Este proceso dura unos 5 minutos.



![Image](assets/fr/032.webp)



Una vez finalizada la instalación, podemos cambiar la contraseña "**root**" antes de reiniciar. Selecciona "**Contraseña de root**", pulsa **Intro** e introduce la contraseña "**root**" dos veces.



![Image](assets/fr/020.webp)



Por último, selecciona "**Completar instalación**" y pulsa **Intro**. Aprovecha para **expulsar el disco de la unidad de DVD de la VM**. En la configuración de la VM, también puedes establecer el primer arranque en disco.



![Image](assets/fr/021.webp)



La máquina virtual se reiniciará y cargará el sistema OPNsense desde el disco, ya que acabamos de instalarlo. Inicie sesión con la cuenta "root" en la consola, y su nueva contraseña (de lo contrario, la contraseña por defecto es "**opnsense**").



### D. Enlace de interfaces de red



Aparecerá la pantalla que se muestra a continuación. Seleccione "**1**" y pulse **Intro** para asociar las tarjetas de red de la máquina con las interfaces OPNsense.



![Image](assets/fr/022.webp)



En primer lugar, el asistente le pide que configure la agregación de enlaces y las VLAN. Especifique "**n**" para negarse, y cada vez, valide su respuesta con **Enter**. A continuación, debe asignar las dos interfaces "**hn0**" y "**hn1**" a la **WAN** y a la **LAN**. En principio, "**hn0**" corresponde a la WAN y la otra Interface a la LAN.



Funciona así:



![Image](assets/fr/023.webp)



Ahora tenemos :





- La **LAN** Interface asociada con la tarjeta de red "**hn1**" y con la IP por defecto Address de OPNsense, es decir **192.168.1.1/24**.
- La Interface **WAN** asociada a la tarjeta de red "**hn0**" y con una IP Address recuperada vía **DHCP** en la red local (gracias a nuestro switch virtual externo).



Por defecto, la administración de OPNsense Interface sólo es accesible desde la LAN Interface, por razones obvias de seguridad. Por lo tanto, debe conectarse a la LAN Interface del cortafuegos para realizar la administración. Si esto no es posible, puede administrar temporalmente OPNsense desde la WAN. Esto implica desactivar la función de cortafuegos.



Para ello, cambie al modo shell mediante la opción "**8**" y ejecute el siguiente comando:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Acceso al sistema de gestión OPNsense Interface



Se puede acceder a la Administración de OPNsense Interface a través de HTTPS, utilizando la IP Address de la LAN** Interface (o la WAN). Su navegador le llevará a una página de inicio de sesión. Inicie sesión con la cuenta "root" y la contraseña que seleccionó anteriormente.



![Image](assets/fr/034.webp)



Espere unos segundos... Se le pedirá que siga un asistente para realizar la configuración básica. Haga clic en "**Siguiente**" para continuar.



![Image](assets/fr/036.webp)



El primer paso es definir el nombre de host, el nombre de dominio, elegir el idioma y definir el servidor o servidores DNS que se utilizarán para la resolución de nombres. Mantener la opción "**Habilitar Resolver**" permitirá que el cortafuegos se utilice como un resolvedor DNS, lo que será útil para las máquinas de nuestra LAN virtual.



![Image](assets/fr/037.webp)



Continúe con el siguiente paso. El asistente le da la opción de **definir un servidor NTP para la sincronización de fecha y hora**, aunque ya existen servidores configurados por defecto. Además, es imprescindible elegir la zona horaria correspondiente a su ubicación geográfica (salvo que tenga requisitos especiales).



![Image](assets/fr/038.webp)



Luego viene un paso importante: **configurar la WAN Interface**. Actualmente, está configurado en DHCP y permanecerá en este modo de configuración, a menos que desee establecer una IP estática Address.



![Image](assets/fr/039.webp)



Todavía en la página de configuración de la WAN de Interface, tienes que desmarcar la opción "**Bloquear el acceso a redes privadas a través de la WAN**" si la red en el lado WAN utiliza direccionamiento privado. Este será probablemente el caso si estás ejecutando un Laboratorio, y por lo tanto puede impedirte el acceso a Internet.



![Image](assets/fr/040.webp)



A continuación, puedes **definir una contraseña "root "**, pero esto es opcional porque ya lo hemos hecho.



![Image](assets/fr/041.webp)



Continúe hasta el final para iniciar la recarga de la configuración. Si necesita seguir tomando el control a través de la WAN, reinicie el comando anterior una vez finalizado este proceso.



![Image](assets/fr/042.webp)



¡Eso es todo!



![Image](assets/fr/035.webp)



### E. Configuración DHCP



Nuestro objetivo es utilizar el servidor DHCP de OPNsense para distribuir direcciones IP en la LAN virtual. Para ello, necesitamos acceder a esta ubicación del menú:



```
Services > ISC DHCPv4 > [LAN]
```



**Como puedes ver, DHCP ya está habilitado por defecto en la LAN ** Si no te interesa este servicio, deberías deshabilitarlo. Aunque ya esté habilitado y queramos utilizarlo, es importante revisar su configuración.



Si es necesario, puede cambiar el rango de direcciones IP a distribuir: **192.168.10.10** a **192.168.10.245**, según la configuración actual.



![Image](assets/fr/046.webp)



También podemos ver que los campos "**Servidores DNS**", "**Pasarela**", "**Nombre de dominio**", etc., están vacíos por defecto. De hecho, existe una herencia automática de ciertas opciones y valores por defecto para estos distintos campos. Por ejemplo, para el servidor DNS, se distribuirá la IP Address de la LAN Interface, lo que permitirá utilizar el cortafuegos OPNsense como un resolver DNS.



Guarde la configuración después de realizar cualquier cambio, si es necesario.



![Image](assets/fr/047.webp)



Para probar el servidor DHCP, necesita conectar una máquina a la red LAN de su cortafuegos.



Esta máquina debe obtener una IP Address del servidor DHCP de OPNsense, y nuestra máquina debe tener acceso a la red. El acceso a Internet debe funcionar. Tenga en cuenta que si ha desactivado la función de cortafuegos para acceder a OPNsense desde la WAN, esto desactivará NAT, impidiéndole acceder a la Web.



**Nota**: los arrendamientos DHCP emitidos actualmente son visibles desde la administración de OPNsense Interface. Para ello, vaya a la siguiente ubicación: **Servicios > ISC DHCPv4 > Arrendamientos**.



![Image](assets/fr/045.webp)



### F. Configuración de NAT y reglas de cortafuegos



La buena noticia es que ahora podemos acceder a la administración de OPNsense Interface desde la LAN.



```
https://192.168.1.10
```



Después de iniciar sesión en OPNsense, vamos a descubrir la configuración NAT. Vaya a esta ubicación: **Firewall > NAT > Outbound**. Aquí puede elegir entre la creación automática (por defecto) y manual de reglas NAT salientes.



Elija el modo automático a través de la opción "**Generación automática de reglas NAT salientes**" y pulse "**Guardar**" (en principio, esta configuración ya es la activa). En modo automático, OPNsense crea por sí mismo una regla NAT para cada una de sus redes.



![Image](assets/fr/043.webp)



Por el momento, todos los ordenadores conectados a la LAN virtual "**192.168.10.0/24**" pueden acceder a Internet sin restricciones. Sin embargo, nuestro objetivo es restringir el acceso a la WAN a los protocolos HTTP y HTTPS, así como a DNS en la LAN Interface del cortafuegos.



Así que tenemos que crear reglas de firewall... Navega por el menú de la siguiente manera: **Firewall > Reglas > LAN**.



**Por defecto, hay dos reglas para autorizar todo el tráfico LAN saliente, en IPv4 e IPv6**. Desactive estas dos reglas haciendo clic en la flecha Green del extremo izquierdo, al principio de cada línea.



A continuación, cree tres nuevas reglas para autorizar la **redLAN** a :





- acceder a todos los destinos utilizando **HTTP**.
- acceder a todos los destinos con **HTTPS**.
- solicitar **OPNsense** en su **LAN Interface** (es decir, "**LAN Address**"), a través del **protocolo DNS** (esto implica utilizar el cortafuegos como DNS), o bien autorizar su DNS resolver a través de su IP Address.



El resultado es el siguiente:



![Image](assets/fr/044.webp)



Sólo queda hacer clic en "**Aplicar cambios**" para pasar las nuevas reglas del cortafuegos a producción. **Tenga en cuenta que todos los flujos que no estén explícitamente autorizados se bloquearán por defecto



La máquina LAN puede acceder a Internet, utilizando HTTP y HTTPS. Todos los demás protocolos serán bloqueados.



![Image](assets/fr/018.webp)



## IV. Conclusión



Siguiendo esta guía, podrá instalar OPNsense y empezar de inmediato. OPNsense ofrece una amplia gama de funciones para proteger y gestionar eficazmente el tráfico de su red, y es adecuado para su uso en entornos profesionales.



Esta instalación es sólo el principio: no dude en explorar los menús y configurar otras funciones para adaptar OPNsense a sus necesidades.