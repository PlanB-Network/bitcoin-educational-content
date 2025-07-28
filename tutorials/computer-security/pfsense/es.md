---
name: pfSense
description: Instalación de Pfsense
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian BURNEL publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Se han realizado cambios importantes en el texto original del autor para actualizar el tutorial.*



___



![Image](assets/fr/027.webp)



## I. Presentación



pfSense es un sistema operativo gratuito y de código abierto que transforma cualquier ordenador, servidor dedicado o dispositivo de hardware en un router y cortafuegos de alto rendimiento y altamente configurable. Basado en FreeBSD y reconocido por su arquitectura de red estable y robusta, pfSense lleva más de quince años estableciendo el estándar de cortafuegos de código abierto para empresas, autoridades locales y usuarios domésticos exigentes.



Sus principales funciones han evolucionado considerablemente a lo largo de los años y se han mejorado con cada nueva versión. Hasta la fecha, pfSense ofrece :





- Administración completa y centralizada a través de una Interface web moderna, intuitiva y segura.
- Cortafuegos con seguimiento de estado de alto rendimiento con compatibilidad avanzada con NAT (incluida NAT-T) y gestión granular de reglas.
- Soporte nativo multi-WAN, que permite la agregación o redundancia de conexiones a Internet.
- Servidor y relé DHCP integrados.
- Alta disponibilidad gracias al protocolo CARP para failover y a la posibilidad de configurar clusters pfSense.
- Equilibrio de carga entre varias conexiones o servidores.
- Soporte completo de VPN: IPsec, OpenVPN y WireGuard (sustituye a L2TP, ya obsoleto).
- Portal cautivo configurable para el control de acceso de invitados, especialmente en entornos públicos u hoteleros.



pfSense también cuenta con un sistema de paquetes extensible que facilita la adición de funciones avanzadas como un proxy transparente (Squid), filtrado de URL o IDS/IPS (Snort o Suricata) directamente desde la web Interface.



pfSense se distribuye únicamente para plataformas de 64 bits, en línea con las recomendaciones actuales de FreeBSD. Puede instalarse en hardware estándar (PC, servidores de bastidor) o en plataformas integradas de bajo consumo, como dispositivos Netgate o determinados equipos x86 de bajo perfil, que son mucho más potentes que los antiguos equipos Alix.



Por último, conviene recordar que pfSense requiere al menos dos interfaces de red físicas: una dedicada a la zona externa (WAN) y otra dedicada a la red interna (LAN). Dependiendo de la complejidad de su infraestructura (DMZ, VLAN, múltiples WAN), pueden ser necesarias varias interfaces adicionales para aprovechar al máximo sus capacidades.



## II. Descargar imagen



La última versión estable de pfSense, en el momento de escribir este tutorial, es la 2.8 (lanzada en junio de 2025). Puede descargar la imagen ISO o el archivo de instalación adaptado a su entorno de hardware directamente desde el sitio web oficial :





- [Descargar pfSense](https://www.pfsense.org/download/)



El portal de descargas le permite seleccionar :





- Arquitectura (generalmente **AMD64** para todo el hardware moderno).
- Tipo de imagen (**Installer USB Memstick** para la instalación a través de una memoria USB, **ISO Installer** para la grabación o edición virtual).
- La réplica de descarga más cercana, para optimizar la velocidad de transferencia.



Para aquellos que deseen desplegar pfSense en un entorno virtualizado (Proxmox, VMware ESXi, VirtualBox...), también está disponible una imagen **OVA**. Esta máquina virtual lista para usar simplifica enormemente la instalación y la configuración inicial. Sólo tiene que asegurarse de ajustar los recursos asignados (CPU, RAM, interfaces de red) en función de la carga prevista y de su topología de red.



Antes de la instalación, recomendamos comprobar la integridad del archivo descargado verificando el **SHA256** proporcionado en la página oficial de descargas. Esto garantiza que la imagen no ha sido alterada ni corrompida.



## III. Instalación



En este ejemplo, la instalación se realiza en una máquina virtual que ejecuta VirtualBox. El procedimiento sigue siendo estrictamente idéntico en una máquina física o en cualquier otro hipervisor, a excepción de la gestión de dispositivos virtuales.



### 1. Requisitos mínimos de hardware



Para una implantación estándar, recomendamos :





- 1 GB de RAM** como mínimo (se recomiendan 2 GB o más para habilitar paquetes adicionales o compatibilidad con ZFS).
- 8 GB de espacio en disco** (20 GB o más es preferible para configuraciones más avanzadas, especialmente si instalas una caché proxy, IDS/IPS o registros detallados).
- Al menos dos interfaces de red virtuales** (una para la WAN, otra para la LAN). En VirtualBox, añádalas a la configuración de la máquina virtual antes de iniciarla.



### 2. Inicio del instalador



Monta la imagen ISO descargada como unidad óptica virtual en VirtualBox, o inserta la llave USB si vas a instalar en una máquina física. Al arrancar, aparecerá un menú de arranque:



Si no selecciona ninguna opción, pfSense se iniciará automáticamente con las opciones por defecto después de unos segundos. Pulse la tecla "**Enter**" para iniciar el arranque normal.



![Image](assets/fr/027.webp)



Cuando aparezca el menú principal, pulse rápidamente el botón "**I**" para iniciar la instalación.



![Image](assets/fr/001.webp)



### 3. Configuración inicial del instalador



La primera pantalla permite configurar algunos parámetros regionales, como la fuente de visualización y la codificación de caracteres. Estos ajustes son útiles en casos concretos (teclados no estándar, pantallas en serie, idiomas orientales). Para la mayoría de las instalaciones, mantenga los valores por defecto y seleccione "**Aceptar esta configuración**".



![Image](assets/fr/002.webp)



### 4. Elección del modo de instalación



Seleccione "**Instalación rápida/fácil**" para ejecutar una instalación automatizada con las opciones recomendadas. Este método borra el disco seleccionado y configura pfSense con el particionado por defecto.



![Image](assets/fr/003.webp)



Aparece una advertencia indicando que se borrarán todos los datos del disco. Confirme con "**OK**".



A continuación, el instalador copia los archivos necesarios en el disco. Dependiendo de tu hardware, esto puede tardar desde unos segundos hasta unos minutos.



### 5. Selección del núcleo



Cuando el instalador le pida que elija el tipo de kernel, deje seleccionado "**Kernel estándar**". Este kernel genérico se adapta perfectamente a las implantaciones estándar, ya sea en un PC, un servidor o una máquina virtual.



### 6. Fin de la instalación y reinicio



Una vez completada la instalación, seleccione "**Reboot**" para reiniciar su máquina en su nueva instancia de pfSense.



**Nota importante**: retire la imagen ISO o desconecte la llave USB de instalación antes de reiniciar, para evitar reiniciar el programa de instalación la próxima vez que arranque.



## IV. Iniciar pfSense por primera vez



En la primera puesta en marcha, pfSense debe ser configurado para reconocer y asignar correctamente sus interfaces de red (WAN, LAN, DMZ, VLANs, etc.). La identificación cuidadosa de sus tarjetas de red es esencial para evitar cualquier error de configuración que podría privarle de acceso a Interface web o hacer que su firewall inoperativo.



Al iniciarse, pfSense detecta y enumera automáticamente todas las interfaces de red disponibles, indicando la MAC Address de cada una. Esto hace que sea fácil distinguir entre ellos.



### 1. VLAN



La primera pregunta se refiere a la configuración de las VLAN. En esta fase, para una configuración básica, no activaremos ninguna VLAN. Así que pulsa la tecla "**N**" para saltarte este paso.



![Image](assets/fr/004.webp)



### 2. WAN y LAN Interface Assignment



a continuación, pfSense le pedirá que defina qué Interface se utilizará para la WAN (acceso a Internet). Puede elegir entre :





- Introduzca el nombre de Interface manualmente (recomendado para entornos virtuales).
- Utiliza la detección automática pulsando "**A**". Esta opción es útil en un host físico, siempre que los cables de red estén conectados y los enlaces activos.



![Image](assets/fr/005.webp)



En este ejemplo, configuramos manualmente la WAN. Introduzca el nombre exacto de la Interface. Para una tarjeta Intel, el nombre será a menudo "**em0**" bajo FreeBSD, pero puede variar dependiendo del hardware. Por ejemplo, una tarjeta Realtek se mostrará a menudo como "**re0**".



![Image](assets/fr/006.webp)



Repita la misma operación para definir la LAN Interface. Aquí utilizamos "**em1**".



pfSense confirma que la LAN Interface activa tanto el cortafuegos como NAT para proteger su red interna y gestionar la traducción Address.



Si dispone de otras interfaces físicas, puede configurar interfaces adicionales (DMZ, Wi-Fi, VLAN específicas) en esta fase. Cada Interface lógica requiere una tarjeta de red o Interface virtual correspondiente. Para la configuración inicial, nos limitaremos a WAN y LAN.



Una vez completadas las asignaciones, pfSense muestra un resumen claro de las correspondencias entre las interfaces físicas y los roles asignados. Confirme con "**Y**".



### 3. Consola PfSense



Una vez completado este paso, aparece el menú principal de la consola pfSense. Ofrece varias opciones útiles para la administración directa, como restablecer la contraseña web, reiniciar, recargar la configuración o reasignar interfaces.



![Image](assets/fr/007.webp)



También verá un resumen de la configuración de red actual, incluyendo la IP Address por defecto de la LAN Interface, normalmente **192.168.1.1**. Esta es la Address que tendrá que introducir en su navegador para acceder a la web de administración de Interface.



**Nota**: Si su red interna utiliza un rango Address diferente, seleccione "**2)** Set Interface(s) IP Address" en el menú para asignar una IP Address adecuada a su entorno.



Por defecto, si su Interface WAN está conectada a una caja o modem configurado con DHCP, pfSense recuperará automáticamente una IP pública Address. Por lo tanto, debería beneficiarse de un acceso inmediato a Internet conectando un cliente a la LAN de pfSense Interface.



## V. Primer acceso a la web Interface



Una vez completada la puesta en marcha inicial y configuradas las interfaces de red, puede acceder a la web Interface de pfSense para finalizar y afinar su configuración.



### 1. Conexión inicial



Conecte un ordenador al puerto LAN (o a la Interface LAN virtual en su hipervisor) y asígnele una Address IP en el mismo rango si es necesario (por defecto, pfSense distribuye automáticamente una Address vía DHCP en la LAN).



En su navegador, vaya al Address indicado por la consola (por defecto `https://192.168.1.1`). Ten en cuenta que pfSense requiere HTTPS incluso para la primera conexión - así que espera un aviso de certificado autofirmado, que puedes ignorar añadiendo una excepción.



Aparece la pantalla de inicio de sesión. Las credenciales por defecto son :




- Nombre de usuario:** `admin`
- Contraseña:** `pfsense`



Estos identificadores se modificarán durante el asistente de configuración inicial.



## VI. Asistente de configuración



En la primera conexión, pfSense le pide que siga su **Asistente de configuración**. Le recomendamos encarecidamente que lo utilice para asegurarse de que todos los parámetros esenciales están correctamente definidos.



### 1. Parámetros generales



Puede :




- Especifique un nombre de host y un dominio local (ejemplo: `pfsense` y `lan.local`).
- Define los servidores DNS y elige si pfSense debe usar los DNS de tu ISP o un servicio externo (Cloudflare, OpenDNS, Quad9...).



### 2. Huso horario



Indique la zona horaria de su sitio para que los registros y los horarios sean coherentes (por ejemplo, `Europa/París`).



### 3. Configuración WAN



Configurar la conexión WAN :




- Por defecto es **DHCP** (suficiente si estás detrás de una caja).
- Si tiene una IP fija, introduzca los parámetros (IP estática, máscara, pasarela, DNS) manualmente.
- Si es necesario, defina una VLAN o una autenticación PPPoE (común con algunos ISP).



### 4. Configuración LAN



El asistente sugiere cambiar la subred LAN por defecto. Si tienes un plan de direccionamiento específico, ahora es el momento de adaptarlo.



### 5. Cambiar la contraseña del administrador



Asegure su pfSense estableciendo inmediatamente una contraseña segura para el usuario `admin`.



## VII. Verificación y actualizaciones



Antes de instalar el cortafuegos, asegúrese de que dispone de la última versión de :





- Vaya a **Sistema > Actualizar**.
- Seleccione el canal de actualización (normalmente **Estable**).
- Compruebe si hay actualizaciones y aplíquelas.



Es una buena idea activar las notificaciones de actualizaciones para mantenerte informado de los parches de seguridad.



## VIII. Guardar la configuración



Antes de realizar cambios importantes, aplica una política de copias de seguridad:





- Vaya a **Diagnóstico > Copia de seguridad y restauración**.
- Descargue una copia de la configuración actual (`config.xml`).
- Guárdalo en un lugar seguro (soporte externo encriptado).



Para entornos de misión crítica, considere la posibilidad de realizar copias de seguridad automáticas de la configuración en un servidor externo o mediante un script programado.



## IX. Buenas prácticas tras la instalación



Para terminar su despliegue con tranquilidad :





- Modificar las reglas del cortafuegos**: por defecto, pfSense permite todo el tráfico saliente en la LAN y bloquea el tráfico entrante en la WAN. Ajuste estas reglas según sea necesario.
- Configure el acceso remoto seguro**: si es necesario, habilite el acceso a Interface web desde la WAN sólo a través de VPN o con restricciones de IP.
- Activar notificaciones**: configurar un servidor SMTP para recibir alertas (fallos, actualizaciones, errores).
- Instale extensiones útiles**: por ejemplo, IDS/IPS (Snort, Suricata), proxy (Squid), filtrado DNS (pfBlockerNG).



Su cortafuegos pfSense ya está en funcionamiento, listo para proteger su red. Gracias a su flexibilidad y a su comunidad activa, dispone de una herramienta potente y escalable que puede adaptarse a sus necesidades futuras (multi-WAN, VLAN, VPN sitio a sitio, portal cautivo, etc.).



Consulte regularmente la documentación oficial ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) para descubrir nuevas funciones y asegurarse de que su configuración está actualizada y es segura.