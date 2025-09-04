---
name: Ntopng
description: Supervise su red con ntopng
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian Duchemin publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



**Ya sea para comprobar la fluidez de la red, para obtener una imagen clara del uso o para estadísticas de rendimiento, la supervisión del flujo de red es una parte importante de una red empresarial**. Ayuda a anticipar cambios en la infraestructura y a garantizar la calidad de uso para los usuarios (también conocida como QoE por *Quality of Experience*, en contraposición a QoS).



Para ello, hay muchas técnicas y software/protocolos disponibles. Netflow, por ejemplo, desarrollado por Cisco, puede utilizarse para recuperar estadísticas de flujo IP de una Interface, pero su uso está restringido a equipos compatibles.



Por eso en este tutorial voy a presentarte **Ntop** y mostrarte cómo usarlo en tu infraestructura para vigilar el uso de tu red.



Ntop es un software de código abierto que puede instalarse en cualquier máquina Linux. Es gratuito y puede recopilar los siguientes datos:





- Utilización del ancho de banda
- Principales clientes
- Principales destinos
- Protocolos utilizados
- Aplicaciones utilizadas
- Puertos utilizados
- Etc.



Ahora rebautizada como **Ntopng (Nueva Generación)**, ofrece numerosas funciones básicas gratuitas. También está disponible una versión comercial que permite exportar las alertas configuradas a software de tipo SIEM o filtrar el tráfico con reglas definidas directamente desde la sonda.



## II. Requisitos previos



La instalación de una sonda Ntop difiere según el equipo y el entorno. Así que no voy a darte aquí una guía paso a paso, sino que esbozaré las distintas posibilidades.



### A. Modo a bordo



Si tiene un cortafuegos pfSense, OPNSense o Endian en producción, o incluso una estación de trabajo Linux con NFTables, ¡buenas noticias! Puede instalar Ntopng directamente y empezar a monitorizar sus interfaces.



La ventaja de esta técnica es que no requiere hardware adicional. Por otro lado, aumenta la utilización de recursos, así que asegúrese de que dispone de hardware adecuado o de una máquina virtual de tamaño suficiente (mínimo 2 núcleos y 2 GB de RAM).



### B. Modo TAP / SPAN



Un **tap** es **un dispositivo de red que duplica el tráfico que pasa a través de él y lo envía a otro dispositivo.** La ventaja de este dispositivo es que no requiere ninguna modificación de la infraestructura existente, y puede colocarse en cualquier lugar para supervisar secciones específicas de la red, o entre el conmutador central y el router de borde para analizar el tráfico hacia/desde Internet.



La gran desventaja de este tipo de equipos es su coste. En las redes Gigabit actuales, una escucha pasiva no puede captar correctamente el tráfico de red, por lo que se necesita un dispositivo activo que cueste unos 200 euros (como mínimo).



El modo **SPAN**, también conocido como **port mirroring**, es utilizado por un switch para reenviar tráfico de un puerto a otro. Este es, con diferencia, mi método preferido, ya que es sencillo de configurar y, al igual que el tap, permite supervisar una parte de la red o toda la red a voluntad. Sin embargo, tiene dos inconvenientes: el conmutador debe integrar esta función y su uso puede aumentar la carga del procesador del conmutador.



### C. Modo router



Es perfectamente posible montar un router en Linux e instalar ntopng en él. El único inconveniente de este método es que modificará tu red, ya sea su direccionamiento interno, o el direccionamiento entre tu router "real" y el que estás añadiendo.



Nota: para los lectores del artículo [Crear un router Wifi con Raspberry Pi y RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) ¡es perfectamente posible instalar ntopng en tu Rpi para obtener estadísticas precisas!



### D. Modo puente



Una alternativa interesante es utilizar **una máquina Linux en modo puente.** Colocada entre dos equipos, permite captar todo el tráfico sin tener que intervenir en la configuración de la infraestructura o de sus equipos. Como una máquina vieja puede hacer el trabajo, el coste de este método también puede ser atractivo. Tenga en cuenta que para ser óptimo, el dispositivo debe tener tres tarjetas de red, dos en modo puente y una para acceder a Interface y SSH. Es posible utilizar sólo dos tarjetas, pero entonces también se capturará el tráfico de administración del dispositivo...



Así que es **este último modo el que voy a utilizar**. Por razones prácticas, voy a utilizar máquinas virtuales para la demostración, pero el método sigue siendo el mismo para su uso en máquinas físicas.



## III. Preparación de la sonda con el puente Interface



Para la sonda, elijo una máquina **Debian 11** en instalación mínima.



Primer paso, siempre el mismo, actualizar el archivo:



```
apt-get update && apt-get upgrade
```



A continuación, instala el paquete **bridge-utils**, que nos permitirá crear nuestro puente:



```
apt-get install bridge-utils
```



Una vez instalado, lo primero que hay que tener en cuenta es el nombre actual de nuestras tarjetas de red. En Debian, este nombre puede tomar varias formas, y lo necesitaremos para la configuración.



Un simple comando **ip add** devolverá una salida con esta información:



![Image](assets/fr/016.webp)



Aquí, veo 3 interfaces:





- Lo**: es la Interface de loopback; es una Interface virtual que "hace bucle" sobre el equipo. Básicamente, esta Interface, cuya Address es 127.0.0.1 (aunque cualquier Address en 127.0.0.0/8 servirá, ya que este rango está reservado para este propósito) se utiliza para contactar con el propio equipo. Si has instalado un sitio web en tu estación de trabajo (usando WAMPP, por ejemplo), probablemente hayas usado el "*localhost*" Address en algún momento para mostrar el sitio alojado en tu propia máquina. Este nombre de host está asociado con el 127.0.0.1 de Address y por lo tanto con el loopback de Interface.
- ens33**: este es mi primer Interface, que recibió un Address aquí desde mi DHCP
- ens36**: mi segundo Interface



Ahora que tengo toda la información, puedo modificar el archivo */etc/network/interfaces* para crear mi puente. Esto es lo que parece actualmente (puede variar):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



La primera parte se refiere a mi Interface loopback, que no voy a tocar, seguido por el Interface ens33. Las modificaciones implican añadir mi segundo Interface (ens36) y configurar el bridge con estas dos interfaces:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



He aquí algunas explicaciones sobre estos primeros cambios:





- auto *Interface***: "iniciará" automáticamente Interface al arrancar el sistema
- iface *Interface* inet manual**: para utilizar la Interface sin ninguna IP Address. Como la palabra clave "static" para definir una IP estática Address o "dhcp" para usar direccionamiento dinámico



Las modificaciones continúan:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Una vez más, algunas explicaciones:





- iface br0 inet static**: aquí he definido mi puente Interface (*br0*) con un Address estático.
- Address, máscara de red, pasarela**: información de direccionamiento de la placa
- bridge_ports**: interfaces que se incluirán en el puente
- bridge_stp**: el protocolo Spanning Tree se utiliza al interconectar conmutadores para detectar enlaces redundantes y evitar bucles. Dado que un puente puede insertarse entre dos rutas de red, puede ser el origen de un bucle, de ahí la posibilidad de habilitar este protocolo. Aquí no lo necesito, así que lo desactivo.



Guarde los cambios y reinicie la red:



```
systemctl restart networking
```



Para comprobar los cambios, visualice de nuevo el resultado del comando **ip** add:



![Image](assets/fr/021.webp)


Puedes ver claramente **mi nueva Interface "*br0*" con la IP Address que le he asignado.** Por cierto, también puedes ver que mis dos interfaces físicas están efectivamente "UP", pero no tienen IP Address.



## IV. Instalación de NtopNG



Ahora que nuestra sonda es capaz de olfatear el tráfico entre mi red y el router, todo lo que queda por hacer es instalar ntopng. Para ello, primero modifica el archivo */etc/apt/sources.list* y añade **contrib** al final de cada línea que empiece por **deb** o **deb-src**.



Por defecto, las fuentes de los paquetes sólo contienen paquetes compatibles con DFSG (*Debian Free Sotftware Guidelines*), identificados por la palabra clave **main**. También puede añadir estas fuentes:





- contrib**: paquetes que contienen software compatible con DFSG, pero que utilizan dependencias que no forman parte de la rama **main**
- non-free**: contiene paquetes que no son compatibles con DFSG



Ejemplo de línea en /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Así que añadiré la palabra **contrib** a líneas como estas.



El resto de los pasos están listados en el sitio [NtopNG] (https://packages.ntop.org/apt/) donde, para Debian 11, necesita añadir las fuentes de Ntop para una futura instalación. Esta adición se automatiza usando un archivo:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Luego viene la fase de instalación propiamente dicha:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



El primer comando borra la caché del gestor de paquetes apt. El segundo actualizará la lista de paquetes y el tercero instalará NtopNG.



Tras la instalación, el software **NtopNG está disponible directamente en el puerto 3000 de la máquina Debian**. Para mí es `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Página principal de NtopNG



Se muestran el nombre de usuario y la contraseña por defecto, ¡así que todo lo que tienes que hacer es introducirlos!



## V. Uso de NtopNG



Cuando te conectas por primera vez, lo primero que se te pide es que cambies la contraseña de administrador y el idioma por defecto. Por desgracia, el francés no es uno de ellos.



A continuación, llega al salpicadero:



![Image](assets/fr/023.webp)



Cuadro de mandos NtopNG



¡No te acostumbres a ésta! Si te fijas en el recuadro amarillo de la parte superior de la pantalla, verás la frase: "*La licencia caduca a las 04:57*". Por defecto, la instalación lanza una versión de prueba de la versión completa de NtopNG, pero por un tiempo (muy) limitado. Una vez alcanzada esta "cuenta atrás", se activa la versión *community* y el panel de control cambia:



![Image](assets/fr/024.webp)



Nuevo panel de control de la comunidad NtopNG



Lo primero que hay que hacer es **comprobar que está escuchando la Interface correcta**. En la esquina superior izquierda, una lista desplegable de interfaces disponibles te permite seleccionar la Interface que nos interesa aquí: br0



![Image](assets/fr/025.webp)



Selección Interface



La nueva ventana muestra los "Top Flaw Talkers", es decir, los aparatos que más se comunican. Aquí sólo me aparecen dos emisoras:



![Image](assets/fr/026.webp)



**Los hosts de origen aparecen a la izquierda, los de destino a la derecha ** Esto permite visualizar el uso del ancho de banda total por cada host, y obtener una visión global del tráfico de red. No está mal, pero podemos ir más allá...



Si hago clic en "*Hosts*", por ejemplo, obtengo un gráfico que muestra el consumo de energía de envío y recepción de cada host de mi red. Aquí, por ejemplo, puedo ver que sólo 192.168.1.37 representa el 80% de mi tráfico:



![Image](assets/fr/027.webp)



Si hago clic en la IP Address del host en cuestión, se me redirige a una página de resumen:



![Image](assets/fr/028.webp)



Puedo ver, por ejemplo, que es una máquina VMWare (al reconocer el SÍ de mi MAC Address), que se llama DESKTOP-GHEBGV1 (así que seguramente es un host Windows) Y tengo **estadísticas de paquetes recibidos y enviados, así como de la cantidad de datos**.



También observará un nuevo menú en la parte superior de este resumen. Te sugiero que hagas clic en "**Aplicaciones**" para ver qué está generando tanto tráfico:



![Image](assets/fr/017.webp)


Ja, ¡parece que tenemos una respuesta! En el gráfico de la izquierda, **vemos que el 76,6% de su tráfico proviene de ... Windows Update**, ¡así que este host está descargando actualizaciones!



NtopNG utiliza una tecnología llamada DPI para *Inspección Profunda de Paquetes*, que le permite categorizar cada flujo de red y definir la aplicación (o familia de aplicaciones) que hay detrás.



Para demostrarlo, lanzo un vídeo de YouTube en mi host:



![Image](assets/fr/018.webp)



**¡El tráfico fue inmediatamente reconocido y categorizado!



Nota: por razones obvias, este tipo de software puede plantear problemas de privacidad, así que tenga cuidado de utilizarlo en las condiciones adecuadas. Ten en cuenta también que es posible **anonimizar los resultados**, la opción se encuentra en **Configuración > Preferencias > Misc** y se llama "**Mask Host IP Address**".



## VI. Detecciones y alertas



NtopNG también es capaz de emitir alertas de seguridad en determinados feeds. Éstas se encuentran en el menú **Alertas**, en el banner de la izquierda. Aquí, por ejemplo, tengo un total de 2851 alertas, divididas en diferentes severidades: Aviso, Advertencia y Error.



![Image](assets/fr/019.webp)



Echemos un vistazo a las alertas de alta criticidad, ¡tengo 17!



Al hacer clic en esta figura aparecen los detalles de las alertas. No hay nada alarmante aquí, se trata de un falso positivo, la descarga de actualizaciones que se categoriza como una transferencia de archivos binarios en un flujo HTTP, lo que sí podría significar un ataque.



![Image](assets/fr/020.webp)



Sin embargo, como estoy utilizando la versión gratuita, no puedo excluir dominios o hosts que sean fuente de alertas, por lo que tendrás que estar pendiente de ellos para no perderte algo mucho más preocupante. NtopNG se generate alertas en caso de:





- Descarga de archivos binarios a través de HTTP
- Tráfico DNS sospechoso
- Utilizar un puerto no estándar
- Detección de inyecciones SQL
- Secuencias de comandos en sitios cruzados (XSS)
- Etc.



## VII. Conclusión



En este tutorial, hemos visto **cómo configurar una sonda con NtopNG** permitiéndonos **analizar nuestro tráfico de red** para visualizar el uso de protocolos y la ocupación de cada host, pero también detectar tráfico sospechoso.



Por desgracia, no puedo abarcar todas las funciones y posibilidades en este artículo, pero ¡no dudes en explorarlas!



Esta solución puede implantarse de forma permanente en una infraestructura empresarial. NtopNG también puede exportar los resultados a una base de datos InfluxDB, lo que le permite crear sus propios cuadros de mando con una herramienta de terceros como Graphana.