---
name: Nmap
description: Master Nmap para mapeo de redes y exploración de vulnerabilidades
---

![cover](assets/cover.webp)



*Este tutorial está basado en contenido original de Mickael Dorigny publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Se han realizado cambios en el texto original.*



___



Bienvenido a este tutorial de introducción a Nmap, diseñado para cualquiera que desee dominar esta potente herramienta de escaneo de redes. El objetivo es proporcionarle los conocimientos fundamentales que necesita para utilizar Nmap de forma efectiva en su día a día.



Nmap es una herramienta versátil, ampliamente utilizada por profesionales de TI, redes y ciberseguridad para diagnósticos, descubrimiento de redes y auditoría de seguridad. Este tutorial está dirigido a quienes se inician en estos campos y desean aprender los fundamentos de Nmap. Se recomienda tener conocimientos básicos de administración de sistemas y redes.



Aprenderá los conceptos básicos de Nmap, cómo realizar escaneos de puertos, identificar hosts activos en una red, detectar versiones de servicios y sistemas operativos, realizar escaneos de vulnerabilidades y mucho más. Cada sección incluye explicaciones detalladas y ejemplos prácticos que le ayudarán a dominar el uso de Nmap en diversos contextos.



Al final de este tutorial, tendrás una sólida comprensión de Nmap y serás capaz de utilizarlo eficazmente para mejorar la seguridad y la gestión de tus redes. Disfruta de la lectura.



## 1 - Introducción a Nmap: ¿Qué es Nmap?



### I. Presentación



En esta primera sección, echaremos un vistazo a la herramienta de escaneo de red Nmap. Veremos las claves Elements que necesitas saber sobre esta herramienta y cómo funciona en general. Esto nos ayudará a entender mejor el resto del tutorial.



### II. Presentación de la herramienta Nmap



Nmap, para _Network Mapper_, es una herramienta gratuita y de código abierto utilizada para **descubrimiento de redes, mapeo y auditoría de seguridad**. También puede utilizarse para otras tareas como **inventario, diagnóstico o supervisión de redes**.



Puede determinar si los hosts de una red objetivo están activos y accesibles, qué servicios de red están expuestos, qué versiones y tecnologías están en uso y otra información de análisis útil. Nmap puede utilizarse para escanear un único servicio en un equipo concreto o en grandes extensiones de la red, hasta Internet en su totalidad.



Los puntos fuertes de Nmap son muchos:





- Potente y flexible**: Nmap puede escanear grandes redes y utilizar técnicas de detección avanzadas. Es compatible con UDP, TCP, ICMP, IPv4 e IPv6, y puede realizar detección de versiones, análisis de vulnerabilidades o interacciones específicas con protocolos. Su arquitectura es modular, gracias en particular a los scripts NSE (Nmap Scripting Engine), que veremos más adelante en este tutorial.
- Facilidad de uso**: la documentación oficial es abundante y de la máxima calidad. También hay disponibles numerosos recursos de la comunidad para ayudarte a empezar.
- Popularidad y longevidad**: Nmap es una referencia en su campo desde 1998. La versión actual, en el momento de esta actualización, es la 7.95. Aunque existen otras herramientas para tareas específicas, Nmap sigue siendo imprescindible para el mapeo y análisis de redes.



**Nmap en el cine**



Nmap es una de las pocas herramientas de seguridad que ha adquirido cierta notoriedad entre el gran público. Aparece en la película _Matrix Reloaded_, en una escena emblemática en la que Trinity lo utiliza para piratear un sistema:



![nmap-image](assets/fr/01.webp)



matriz: Escena recargada con Nmap



También aparece en otras obras cinematográficas.



**Comentarios



Como administrador de sistemas y luego auditor de ciberseguridad y pentester, **utilizo Nmap casi a diario** y lo **recomiendo habitualmente** a los administradores de sistemas que desean reforzar su dominio de las redes y mejorar sus capacidades de diagnóstico.



### III. Funcionamiento a alto nivel



Nmap está disponible para Linux, Windows y macOS. Está escrito principalmente en C, C++ y Lua (para scripts NSE). Se utiliza principalmente en la línea de comandos, aunque también hay disponibles interfaces gráficas como Zenmap. No obstante, le recomendamos encarecidamente que empiece por la línea de comandos para comprender mejor su funcionamiento.



Un ejemplo sencillo:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Este comando se explicará en detalle más adelante. En este tutorial, usaremos Nmap en Linux, pero sus usos son similares en otros sistemas. En Windows, Nmap se basa en la biblioteca **Npcap** (que sustituye a la ya obsoleta WinPcap) para capturar e inyectar paquetes de red.



Nmap se utiliza como un binario convencional, como `ls` o `ip`. Algunas funciones avanzadas pueden requerir derechos elevados, ya que la herramienta a veces manipula paquetes de formas poco convencionales para provocar reacciones específicas en los sistemas objetivo (especialmente para la detección de servicios o vulnerabilidades).



### IV. Impactos del uso de Nmap



Antes de utilizar Nmap, es esencial ser consciente de su impacto potencial en redes y sistemas:





- Puede enviar **miles o incluso millones de paquetes** en un corto espacio de tiempo, lo que puede saturar ciertas infraestructuras de red.
- Puede generate **paquetes malformados o no estándar**, susceptibles de perturbar ciertos equipos (especialmente los sistemas industriales).
- Puede producir un **comportamiento similar al de un ataque**, que puede activar alertas en los sistemas de seguridad (cortafuegos, IDS/IPS, etc.).



En general, **Nmap es una herramienta muy habladora**, ya que genera mucho tráfico para extraer la mayor cantidad de información posible. Por lo tanto, es aconsejable entender bien cómo funciona antes de utilizarla en entornos sensibles o de producción.



### V. Conclusión



Esta sección presenta Nmap y sus principales características. Hemos visto que es una herramienta de mapeo de red esencial, potente y flexible. También hemos discutido cómo funciona y las precauciones que hay que tomar cuando se utiliza, para preparar el escenario para las siguientes partes del tutorial.



## 2 - ¿Por qué utilizar Nmap?



### I. Presentación



En esta sección, echaremos un vistazo a los principales usos de la herramienta de escaneo de redes Nmap. Veremos que es una herramienta ampliamente utilizada en muchos contextos y profesiones, y que tenerla en tu caja de herramientas y saber cómo dominarla es definitivamente una habilidad útil.



### II. Uso de Nmap para diagnóstico y supervisión



Nmap puede utilizarse para el diagnóstico de redes y, más ampliamente, para la monitorización. Del mismo modo que un ping puede utilizarse para determinar si dos hosts se están comunicando, Nmap puede utilizarse para determinar rápidamente si un host está activo, o si un servicio concreto está operativo. Gracias a [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), podemos obtener datos precisos sobre el tiempo de respuesta de un host, la ruta que siguen los paquetes, la respuesta que da un servicio concreto, etc.



El siguiente comando y su resultado se pueden utilizar, por ejemplo, para averiguar rápidamente si un servidor web en el host **192.168.1.18** está activo y responde correctamente:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Utiliza Nmap para recuperar el estado de un servicio web de un servidor remoto.*



Por tanto, el uso de Nmap va más allá de la famosa "prueba ping" durante las fases de depuración o diagnóstico. Veremos más adelante que hay varios métodos utilizados por Nmap para identificar qué servicio está escuchando en un puerto determinado, incluyendo su versión.



### III. Uso de Nmap para el mapeo de redes



Como _Mapeador de redes_, el mapeo de redes es el principal objetivo de esta herramienta. Puede usarse dentro de una red local, o a través de múltiples redes, subredes y VLANs, para listar todos los hosts y servicios alcanzables. Nmap hace esta tarea mucho más rápida y eficiente que cualquier método manual.



Por ejemplo, el siguiente comando se puede utilizar para identificar rápidamente los hosts activos en la red **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Nota: la opción `-sP` está obsoleta y ha sido sustituida por `-sn`.*



![nmap-image](assets/fr/03.webp)



*Uso de Nmap para descubrir hosts accesibles en una red*



Más adelante veremos que existen varios métodos utilizados por Nmap para determinar si un host puede considerarse "activo", aunque a priori no exponga ningún servicio.



### IV. Uso de Nmap para evaluar una política de filtrado



Nmap tiene la ventaja de ser factual: sus resultados permiten establecer conclusiones concretas, a diferencia de cualquier documento de arquitectura o política de filtrado. Es una herramienta clave para evaluar la eficacia de la compartimentación de los sistemas de información, ya que permite **verificar si la política de filtrado se aplica realmente**.



En una red corporativa, las mejores prácticas dictan que los sistemas estén segmentados según su función, criticidad o ubicación. Las reglas de filtrado (a menudo aplicadas mediante cortafuegos) deben restringir las comunicaciones entre zonas. Pero estas configuraciones suelen ser complejas y propensas a errores.



Así pues, para validar que se ha respetado la política, nada mejor que una prueba concreta. Por ejemplo, puedes comprobar que los servicios de administración sensibles (SSH, WinRM, MSSQL, MySQL, etc.) no son accesibles desde una zona de usuario.



El uso de **Nmap para comprobar la política de filtrado** debería ser sistemático antes de poner dicha política en producción. Desgraciadamente, esta comprobación se suele descuidar.



Según mi experiencia, muchos errores de configuración pasan desapercibidos en ausencia de pruebas de validación. Un simple error en un rango de IP o el descuido de una regla puede dejar vulnerable una zona supuestamente aislada.



### V. Uso de Nmap para auditoría de seguridad y pruebas de penetración



Nmap tiene **muchas características útiles para la evaluación de seguridad**, pruebas de penetración (pentests), y desafortunadamente también para atacantes.



Las funciones de descubrimiento de redes son cruciales para un atacante, que necesita comprender la topología de la red tras un compromiso inicial. Pero Nmap ofrece mucho más que esto: integra un motor de scripts, **muchos de ellos dedicados a la detección de vulnerabilidades**.



Por ejemplo, este comando se puede utilizar para comprobar si un servicio FTP permite una conexión anónima, sin tener que conectarse manualmente:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Uso de un script NSE para comprobar la autenticación FTP anónima a través de Nmap.*



La detección de vulnerabilidades con Nmap es uno de los primeros pasos en una auditoría o prueba de penetración. Permite identificar rápidamente determinados puntos débiles y optimizar los esfuerzos de análisis.



Pero cuidado: **las herramientas de exploración de vulnerabilidades tienen sus límites**. Nmap sólo cubre una fracción de las amenazas, y no garantiza que un sistema sea seguro si no se detecta ningún problema. Por tanto, es esencial **comprender cómo funcionan los scripts utilizados** y no confiar únicamente en su veredicto.



### VI. Conclusión



Hemos visto que el dominio de Nmap puede cubrir una amplia gama de casos de uso, desde el diagnóstico y la monitorización hasta el mapeo, la evaluación de políticas de seguridad y el escaneo de vulnerabilidades. En la siguiente sección, iremos al grano e instalaremos Nmap.




## 3 - Instalación y configuración de Nmap



### I. Presentación



En esta sección, aprenderemos a instalar la herramienta de exploración de redes Nmap en los sistemas operativos Linux y Windows. Al final de esta sección, tendremos todo lo que necesitamos para empezar a utilizar Nmap para futuros módulos. Por último, veremos qué privilegios puede requerir cuando se utiliza y por qué.



### II. Instalación de Nmap en Linux



Nmap fue diseñado originalmente para funcionar en sistemas operativos GNU/Linux. Como resultado, y gracias a su longevidad y popularidad, lo encontrarás en todos los repositorios oficiales de las principales distribuciones de Unix. En este tutorial, utilizaré un sistema operativo basado en Debian [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Pero puedes usarlo exactamente de la misma manera desde un Debian clásico, CentOS, Red Hat o ¡lo que sea!



En Debian, para comprobar que Nmap está presente en sus repositorios actuales, puede utilizar la siguiente orden:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



La respuesta aquí indica claramente que el paquete "nmap" existe en los repositorios (aquí, los de Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). A partir de ahora, puede instalar Nmap a través de los comandos de instalación habituales, nada desarma por el momento 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Para comprobar que Nmap está instalado correctamente, mostraremos su versión:



```
nmap --version
```



Este es el resultado esperado:



![nmap-image](assets/fr/05.webp)



resultado de mostrar la versión actual de Nmap._



Observa la presencia en esta pantalla de la librería "libpcap" (_Packet Capture Library_) y su versión. También utilizada por Wireshark, "libpcap" es utilizada por Nmap para crear y manipular paquetes y escuchar el tráfico de red.



### III Instalación de Nmap en Windows



Para instalarlo en un sistema operativo Windows, empieza por descargar el binario desde el sitio oficial (¡y no otro!):





- Página de descarga de Nmap en el sitio web oficial: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




A continuación, deberá descargar el binario llamado `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



página de descarga del binario de instalación de nmap para Windows



Una vez que tenga este binario en su sistema, simplemente ejecútelo para instalar Nmap. Es una instalación sencilla, y puedes dejar todas las opciones por defecto.



Mi reflejo es desmarcar la casilla "zenmap (GUI Frontend)". Este es un Interface gráfico para Nmap que no utilizo y no será cubierto en este tutorial, pero siéntase libre de probarlo una vez que haya dominado la herramienta de línea de comandos de Nmap



![nmap-image](assets/fr/07.webp)



deseleccion opcional de Zenmap al instalar Nmap en Windows



Al final de la instalación de Nmap, se propone una segunda instalación: la de la biblioteca "Npcap":



![nmap-image](assets/fr/08.webp)



instalación de la biblioteca "Npcap" al instalar Nmap en Windows



Esta es la biblioteca en la que se basa Nmap para gestionar las comunicaciones de red, es decir, construir, enviar y recibir paquetes de red. Probablemente ya te hayas topado con esta librería si usas Wireshark en Windows, ya que también la utiliza y requiere instalación.



Al igual que con Linux, puede validar que Nmap está instalado abriendo un símbolo del sistema o un terminal [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") y escribiendo el siguiente comando:



```
nmap --version
```



Este es el resultado esperado:



![nmap-image](assets/fr/09.webp)



resultado de mostrar la versión actual de Nmap._



Nmap ya está instalado en Windows. Puede utilizarlo exactamente de la misma manera que en Linux, siguiendo este tutorial.



### IV. Privilegios locales necesarios para utilizar Nmap



Pero por cierto, cuando se utiliza Nmap, **¿es necesario tener privilegios locales elevados en el sistema?** La respuesta es: **depende**.



En su forma más básica, es decir, sin ir muy lejos en el uso de sus opciones, Nmap no requiere necesariamente derechos privilegiados. Sin embargo, pronto se dará cuenta de que es mejor utilizar Nmap en un contexto privilegiado ("root" en Linux, "administrador" o equivalente en Windows) para poder utilizarlo en todo su potencial, a riesgo de recibir un mensaje de error como éste:



![nmap-image](assets/fr/10.webp)



mensaje de error en Linux cuando las opciones de Nmap requieren derechos de root._



Tanto en Linux como en Windows, hay muchos casos en los que Nmap le pedirá acceso privilegiado. Las principales razones son las siguientes (lista no exhaustiva):





- Construcción de paquetes de red "sin procesar "**: Nmap es capaz de realizar una amplia gama de métodos de sondeo, incluyendo la manipulación y construcción avanzada de paquetes. Este es el caso, por ejemplo, cuando queremos realizar sondeos TCP SYN, que no respetan el clásico _Three-way handshake_ de los intercambios TCP. Para ello, Nmap necesita utilizar funciones distintas a las nativas de los sistemas operativos, que sólo saben respetar las buenas prácticas en las comunicaciones de red (recurre a las librerías "Npcap" y "libcap" vistas anteriormente). Es gracias a que Nmap no hace las cosas de la manera "estándar" que es capaz de deducir cierta información sobre sistemas operativos, servicios y ciertas vulnerabilidades.





- Escuchar el tráfico de red**: algunas de las opciones de Nmap requieren que escuche la red para recuperar cierta información. Esta acción se considera sensible en sistemas operativos, ya que también le permite escuchar las comunicaciones de otras aplicaciones del sistema. Al igual que Wireshark, Nmap necesita privilegios específicos para hacer esto, que son más fáciles de obtener estando directamente en una sesión privilegiada.





- Escuchar en puertos privilegiados**: en los sistemas operativos se dice que los puertos del 0 al 1024 (tanto TCP como UDP) son privilegiados, es decir, que están reservados de alguna forma para usos muy específicos y por tanto protegidos. Aunque esta es una razón algo obsoleta hoy en día, sigue siendo necesario tener ciertos privilegios para escuchar en estos puertos, algo que Nmap puede tener que hacer dependiendo de cómo se vaya a utilizar.





- Envío de paquetes UDP:** Del mismo modo, escuchar una aplicación de red en los puertos UDP (un protocolo sin estado) requiere derechos privilegiados en los sistemas operativos. Por lo tanto, será necesaria una sesión privilegiada si desea realizar un sondeo UDP, para el que Nmap tendrá que escuchar una respuesta con el fin de analizar las respuestas a sus sondeos.




Para ser más precisos, es posible, al menos en Linux, ejecutar Nmap con todas sus funciones y opciones sin ser root. Esto se consigue otorgando las _capacidades_ adecuadas al binario. Sin embargo, esto requiere una manipulación avanzada y puede no ser tan práctico como ejecutar Nmap directamente con privilegios. Además, este enfoque es menos común y puede plantear problemas de seguridad si está mal configurado.



Sin embargo, esto se aleja un poco de nuestro tutorial de Nmap, así que prescindiremos de él por ahora.



Para el resto de este tutorial, asuma que Nmap siempre se ejecuta como "root" (desde un intérprete de órdenes como "root" o mediante el comando "sudo"), o en un terminal de administrador bajo Windows, incluso si esto no se indica. De lo contrario, es posible que experimente diferencias sutiles pero notables con respecto al tutorial.



### V. Conclusión



Ya está Nmap ya está instalado en nuestro sistema operativo y listo para usarse, sin necesidad de ninguna otra configuración. Con esta sección terminamos la introducción y presentación de Nmap. Espero que os haya hecho la boca agua y que estéis deseando empezar a practicar.



Hablando más en serio, ahora tenemos una mejor idea de lo que es la herramienta de mapeo Nmap y cuáles son sus usos más comunes, así como sus limitaciones. Sigamos adelante




## 4 - Escaneo de puertos TCP y UDP con Nmap



### I. Presentación



En esta sección, aprenderemos a realizar nuestros primeros escaneos de puertos utilizando la herramienta de escaneo de red Nmap. Veremos cómo utilizarla para compilar una lista de servicios de red expuestos en un host, ya sea utilizando protocolos TCP o UDP.



A partir de ahora, recuerde escanear únicamente hosts en un entorno controlado para los que disponga de autorización explícita.





- A modo de recordatorio: [Código Penal: Capítulo III: Ataques a los sistemas de tratamiento automatizado de datos](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Si no tienes uno a mano**, te recomiendo las siguientes soluciones gratuitas, ¡que son justo lo que necesitas!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Plataforma de formación en hacking, Hack The Box pone constantemente a tu disposición sistemas vulnerables para que los ataques a tu antojo. Hay varios centenares de sistemas disponibles, pero durante todo el año se ofrece gratuitamente un fondo renovado de 20 máquinas, con acceso a través de una VPN OpenVPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Esta plataforma ofrece numerosos sistemas intencionadamente vulnerables para su descarga, que pueden utilizarse a través de VirtualBox (también una solución gratuita) u otros medios. Una vez descargados, no es necesaria una VPN: todo es local.




Además, eres libre de **crear una máquina virtual** en tu sistema operativo favorito e instalar varios servicios en ella como objetivos de prueba. La ventaja aquí será que también podrás ver lo que está pasando en el lado del servidor durante un escaneo, especialmente con Wireshark, y tener una mano en el firewall local cuando hagamos pruebas más avanzadas.



Seamos prácticos



### II. Escaneando los puertos TCP de un host mediante Nmap



#### A. Primer escaneo de puertos TCP con Nmap



Ahora vamos a realizar nuestros primeros escaneos a través de Nmap. Nuestro objetivo aquí es simple: queremos averiguar qué servicios están expuestos por el servidor web que acabamos de desplegar, para ver si hay algo inesperado, como un servicio de administración que no debería ser accesible, o la exposición de un puerto de una aplicación que pensábamos que estaba decomisada.



En mi ejemplo, el host a escanear tiene la IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



He aquí un posible resultado. Vemos un retorno clásico de Nmap con mucha información:



![nmap-image](assets/fr/11.webp)



resultados de un simple escaneo TCP realizado con Nmap._



Echando un vistazo rápido a este resultado, entendemos que los puertos TCP/22 y TCP/80 son accesibles en este host.



Por defecto, y si no se lo indicas, Nmap sólo escaneará puertos TCP.



#### B. Comprender los resultados de un simple escaneo Nmap



Pero vayamos un paso más allá para entender esta salida: cada línea es importante, en primer lugar para saber qué se acaba de hacer y, en segundo lugar, para interpretar correctamente los propios resultados de la exploración.



La primera línea es esencialmente un recordatorio de la versión del escáner y la fecha (¡útil para registrar y archivar después de todo!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



La segunda línea muestra los resultados del inicio del escaneo para el host "debian.home (192.168.1.19)". Esta información será útil cuando comencemos a escanear varios hosts al mismo tiempo:



```
Nmap scan report for debian.home (192.168.1.19)
```



La tercera línea nos indica que el host en cuestión está "Up", es decir, activo:



```
Host is up (0.00022s latency).
```



Por último, Nmap nos informa de que 998 puertos TCP identificados como cerrados no se muestran en el archivo:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Esto nos ahorra casi 1.000 líneas de salida con el aspecto:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Gracias a él por evitarnos esto



¿Por qué 998 puertos "cerrados"? Sumando los 2 puertos abiertos son 1000, y ese es el número de puertos que Nmap analizará en su configuración por omisión, ¡no los 65535 puertos TCP existentes! Veremos más adelante que esto es total y fácilmente personalizable. Pero si el sistema objetivo tiene un servicio escuchando en un puerto bastante exótico, este sondeo "por defecto" no lo descubrirá.



Siguiendo esta información, encontramos lo más interesante: una tabla organizada según las tres columnas "PUERTO - ESTADO - SERVICIO":





- La primera columna "PORT" indica simplemente el puerto/protocolo de destino, y aquí es importante fijarse en si se trata de un puerto TCP (`<port>/tcp`) o UDP (`<port>/udp`).





- La columna "ESTADO" indica el estado del servicio de red descubierto en este puerto y determinado por Nmap en base a la respuesta obtenida. Puede ser "abierto", "cerrado", "filtrado" o "desconocido". Veremos más adelante cómo distingue Nmap entre estos distintos estados.





- La columna "SERVICIO" indica el servicio expuesto en el puerto en cuestión. Tenga en cuenta, sin embargo, que aquí no hemos utilizado opciones activas de descubrimiento de servicios. Nmap se basa en una referencia local entre un puerto/protocolo y el supuesto servicio asignado: el fichero "/etc/services




Si echa un vistazo al archivo "/etc/services" de un sistema Linux, encontrará un enlace "port/protocol - service" similar al que muestra Nmap:



![nmap-image](assets/fr/12.webp)



extrae el contenido del archivo "/etc/services" en Linux._



Es importante entender que, por el momento, Nmap no ha realizado ningún descubrimiento de servicio activo. Por ejemplo, habría sido incapaz de identificar el servicio SSH detrás de un puerto TCP/80 si este hubiera sido el caso. De ahí la importancia de saber utilizar las opciones correctas - ¡está al caer!



Saber cómo interpretar la salida de Nmap es una parte importante del dominio de la herramienta. La buena noticia es que esta salida será en gran medida la misma, independientemente de las opciones que utilice.



#### C. Bajo el capó: análisis de la red mediante Wireshark



Si observa detenidamente lo que ocurre en la red Interface del host que escanea el servidor, o en la del propio servidor, las acciones de Nmap serán mucho más claras. Eso es lo que vamos a hacer aquí.



Lo que puedo mostrarte aquí es sólo una parte de lo que es visible en Wireshark. Si quieres ir más allá, siéntete libre de hacer una captura de red tú mismo durante un escaneo, y luego navegar a través de lo que ha sido capturado.



En esta prueba, mi host de escaneo (192.168.1.18) y mi host de destino (192.168.1.19) están en la misma red local.



Nmap comienza averiguando si el host objetivo está activo en la red local enviando una petición ARP. Si recibe una respuesta, sabe que el host está activo y comienza su exploración de la red:



![nmap-image](assets/fr/13.webp)



solicitud ARP emitida por Nmap para determinar si un host objetivo está presente en la red local



Si el host a escanear está en una red remota, Nmap comienza enviando una petición ping e intenta alcanzar algunos de los puertos expuestos con más frecuencia (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



solicitud de ping emitida por Nmap para determinar si un host de destino es accesible en una red remota



Si obtiene respuesta a alguna de estas pruebas, considera que el objetivo está activo.



Una vez que Nmap ha determinado que su objetivo está activo, intentará resolver su nombre de dominio con el servidor DNS configurado en la tarjeta de red:



![nmap-image](assets/fr/15.webp)



resolución dNS en el objetivo de escaneo Nmap



Ahora que Nmap ha identificado su objetivo y sabe que está activo, comienza su escaneo de puertos TCP:



![nmap-image](assets/fr/16.webp)



tCP Transmisión de paquetes SYN y recepción RST/ACK durante el escaneo Nmap



Para ello, en cada puerto TCP de su rango por defecto, **enviará paquetes TCP SYN y esperará una respuesta**. En la captura de pantalla de arriba, recibe paquetes TCP RST/ACK del servidor escaneado, lo que significa "muévete, no hay nada que ver aquí" - en otras palabras, estos puertos están cerrados. Como vimos en el resultado, este será el caso para la mayoría de los puertos escaneados. Con dos excepciones:



![nmap-image](assets/fr/17.webp)



respuesta a un paquete TCP SYN enviado al puerto 22, activo en el objetivo de exploración



En la captura de pantalla anterior, vemos un paquete TCP SYN/ACK enviado por el host de destino**. El puerto está activo y expone un servicio. Nmap acusa recibo de la respuesta y luego termina la conexión (TCP RST/ACK). **Así es como supo que el puerto TCP/22 estaba activo**.



Hemos visto aquí que Nmap respeta el "Three Way Handshake" cuando sondea una red TCP. Por razones de rendimiento, es posible pedirle que no responda a la devolución del servidor, ahorrando así varios miles de paquetes al escanear una red grande. Pero veremos estas opciones y optimizaciones más adelante en el tutorial.



Ahora tenemos una mejor idea de cómo hacer un sondeo TCP y qué ocurre realmente cuando se realiza. También hemos visto que, por omisión, Nmap realiza un sondeo de puertos TCP en un número limitado de puertos.



### III. Escaneando puertos UDP con Nmap



#### A. Primer escaneo de puertos UDP con Nmap



Veamos ahora cómo analizar los puertos UDP de un sistema. Como hemos visto, por omisión Nmap siempre analizará los puertos TCP. Esto puede significar perderse mucha información si no somos conscientes de ello.



Como recordatorio, para los propósitos de esta prueba, mi host de escaneo (192.168.1.18) y mi host de destino (192.168.1.19) están en la misma red local.



```
nmap -sU 192.168.1.19
```



Aquí, el retorno obtenido tiene el mismo formato que para un escaneo TCP, pero los servicios activos mostrados están en `<port>/UDP`, ¡como se solicitó!



![nmap-image](assets/fr/18.webp)



resultado de un simple escaneo UDP realizado con Nmap._



La opción "-sU" se utiliza para decirle a Nmap que quiere trabajar en UDP, en lugar de TCP como es el valor por defecto.



Por cierto, probablemente notará que Nmap requiere derechos de "root" para los escaneos UDP, como se mencionó anteriormente en el tutorial.



nota: Desde las últimas versiones de Nmap, siempre se recomienda ejecutar escaneos UDP con privilegios de administrador para garantizar resultados fiables, ya que algunas funciones requieren acceso sin procesar a los sockets de red._



Los sondeos UDP pueden llevar mucho tiempo (1100 segundos para sondear 1000 puertos en mi ejemplo), debido a la ausencia del "Three Way Handshake" en UDP, lo que significa que Nmap esperará una respuesta por cada paquete UDP enviado, y determinará el puerto como "cerrado" sólo si no hay respuesta después de un cierto tiempo (timeout). Esta respuesta de los hosts escaneados no es sistemática y a menudo está limitada en cuanto al número de respuestas por segundo, para evitar ciertos ataques de amplificación. Esto contrasta con TCP, donde hay una respuesta inmediata del host escaneado, tanto si el puerto está abierto como cerrado. Veremos más adelante cómo optimizar esto.



Una segunda dificultad con UDP es **que los servicios no siempre responden a los paquetes entrantes**, simplemente porque no siempre es necesario y es el principio de UDP. Cuando este es el caso, y no se recibe ningún ICMP "puerto inalcanzable", el servicio es marcado como "abierto|filtrado" por Nmap, como se muestra en la captura de pantalla anterior.



#### B. Bajo el capó: análisis de la red mediante Wireshark



Al igual que con nuestro sondeo TCP, echemos un vistazo más de cerca a lo que ocurre a nivel de red durante un sondeo UDP utilizando un análisis Wireshark. El comportamiento de Nmap a la hora de determinar si un anfitrión está activo es el mismo.



La única diferencia real al escanear UDP es que Nmap no esperará un "Three Way Handshake", ya que este mecanismo no existe en UDP (protocolo sin estado):



![nmap-image](assets/fr/19.webp)



transmisión de paquetes uDP y recepción ICMP (puerto inalcanzable) durante el escaneo Nmap



Podemos ver en la captura de pantalla anterior que Nmap enviará un gran número de paquetes UDP, y recibirá para la mayoría de ellos un paquete ICMP "Destination unreachable (Port unreachable)" como respuesta. Esto es normal, ya que es la respuesta apropiada definida por [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") cuando un puerto UDP es inalcanzable:



![nmap-image](assets/fr/20.webp)



extracto de RFC 1122._



Echemos un vistazo más de cerca a esta captura de Wireshark, que muestra **los tres escenarios posibles** en UDP:



![nmap-image](assets/fr/21.webp)



captura de red durante un escaneo UDP en diferentes puertos con Nmap._



Los tres casos son los siguientes:





- El primer Exchange está formado por los paquetes nº. 3, 4 y 8, 9. Nmap envía paquetes UDP en el puerto SNMP clásico y, por lo tanto, **construye de antemano paquetes que cumplen con el protocolo**. A continuación, obtiene una respuesta del servidor (paquetes nº 8 y 9). Resultado: Nmap ha recibido una respuesta, el servicio está "abierto".





- El segundo Exchange consiste en los paquetes 6 y 7. Nmap envía un paquete UDP "vacío" (sin estructura de protocolo) al puerto UDP/165, y recibe un paquete ICMP como respuesta: "Destino inalcanzable (Puerto inalcanzable)". Resultado: Nmap ha recibido una respuesta (negativa), el host está levantado, pero el servicio que intentó alcanzar no está operativo en este puerto, que se marcará como "cerrado".





- El último Exchange consiste en el paquete nº 12: Nmap envía un paquete UDP "vacío" al puerto UDP/1235. No hay respuesta, ni siquiera un rechazo explícito del host escaneado. Resultado: Nmap marca el puerto como "abierto|filtrado", ya que es incapaz de saber si esto se debe a la presencia de un cortafuegos, configurado para no responder, o a un servicio UDP activo que no devuelve respuesta de todas formas (no es obligatorio en UDP).




Aquí está el resultado mostrado por Nmap siguiendo estos tres casos:



![nmap-image](assets/fr/22.webp)



posibles resultados de un escaneo UDP realizado a través de Nmap._



Ahora tenemos una mejor idea de cómo hacer un sondeo UDP y qué ocurre realmente cuando se realiza. Hasta ahora hemos estado utilizando Nmap de una forma muy simple, sin decidir realmente qué puertos escanear, ¡pero eso está a punto de cambiar!



### IV. Ajuste fino del escaneo de puertos con Nmap



#### A. Recordatorio del comportamiento por defecto de Nmap



Como hemos visto, el propio Nmap elige el número y los puertos a analizar si no especifica ninguna opción. Esta es la configuración "por omisión" que utiliza Nmap cuando no le dice exactamente lo que tiene que hacer. Estas opciones por omisión están diseñadas para dar una idea de los principales puertos expuestos, siendo éstos seleccionados por frecuencia de exposición (puertos más comunes o frecuentes) en lugar de por orden numérico (puerto 1, 2, 3, etc.) y también para evitar iniciar un sondeo de los 65535 puertos posibles si no especifica las opciones adecuadas, lo que sería demasiado largo y prolijo para un caso de uso "por omisión".



**¿Cómo se eligen estos puertos?



Los 1000 puertos analizados en el modo por omisión se eligen según su frecuencia de aparición. Estas estadísticas son mantenidas por Nmap y actualizadas de la misma forma que el propio binario y sus scripts (módulos). Puede ver estas estadísticas usted mismo en el archivo "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



extraído del archivo "/usr/shares/nmap/nmap-services"._



Aquí, en la tercera columna, vemos lo que parecen probabilidades (entre 0 y 1) o una distribución porcentual. Se trata de la frecuencia de aparición de cada par puerto/protocolo. Podemos ver que los puertos más conocidos (FTP, SSH, TELNET y SMTP en este extracto) tienen un valor mucho más alto que los demás.



#### B. Especificar con precisión los puertos de destino para un escaneo Nmap



Sin embargo, en el mundo real, puede que necesitemos escanear sólo un puerto específico, o varios puertos, o un rango específico de puertos. Nmap hace que sea fácil hacer precisamente eso, de forma uniforme tanto para escaneos UDP como TCP.



**Escanear un puerto específico a través de Nmap**



Si deseamos escanear un único puerto, y no 1000, podemos especificar este puerto mediante la opción "-p" o "--port" de Nmap:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Como resultado, el sondeo será naturalmente mucho más rápido y Nmap sólo emitirá los paquetes necesarios para detectar si el host está activo, y después si el puerto especificado es alcanzable. Esto ahorra tiempo si sólo quiere realizar una prueba rápida para ver si el servicio web de su sitio de escaparate sigue activo.



**Escanear múltiples puertos a través de Nmap**



Del mismo modo, podemos especificar varios puertos a Nmap, utilizando la misma opción y concatenando los puertos especificados con una coma:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Independientemente del orden, Nmap comprobará todos estos puertos, y sólo los del sistema objetivo. Observará en la salida de Nmap que **nos dice explícitamente todos los puertos y su estado**, incluso si están "cerrados". A diferencia del comportamiento por omisión, donde esta salida completa hubiera ocupado demasiado espacio:



![nmap-image](assets/fr/24.webp)



*Resultado de un escaneo Nmap TCP en los puertos indicados.*



**Escanear una serie de puertos



Si el número de puertos que desea escanear es demasiado grande, puede especificarlos por rangos, por ejemplo:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Por supuesto, puedes mezclar y combinar según te convenga, por ejemplo:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Escaneo de puertos TCP y UDP



También puede realizar escaneos UDP y TCP al mismo tiempo, en los puertos seleccionados:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Observará en este último ejemplo la presencia de "U:" para indicar un puerto UDP y "T:" para indicar un puerto TCP. He aquí una posible salida de este tipo de exploración:



![nmap-image](assets/fr/25.webp)



*Resultado de un escaneo de puertos TCP y UDP con Nmap.*



Es una forma interesante de personalizar las exploraciones



**Escanear todos los puertos



Por último, es posible especificar rangos mucho mayores o menores a Nmap. Hemos visto que la lista por omisión seleccionada por Nmap contiene 1000 puertos. También podemos pedir los 100 puertos más frecuentes, o los 200 más frecuentes, utilizando la opción "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Por último, podemos pedirle que escanee todos los puertos posibles (todos los 65535), utilizando la notación "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Esto último llevará más tiempo, especialmente con UDP, pero te asegurarás de no perder ningún puerto abierto.



*Nota: La opción "-p-" es el método recomendado para escanear todos los puertos TCP. Para los escaneos UDP, es aconsejable limitar el número de puertos por razones de rendimiento, ya que los escaneos completos de todos los puertos UDP pueden tardar mucho tiempo.*



Más adelante en el tutorial, veremos cómo optimizar la velocidad de los escaneos de Nmap para adaptarla a nuestras necesidades, lo que será especialmente útil para los escaneos en todos los puertos TCP y UDP.



### V. Conclusión



En esta sección por fin hemos practicado un poco, así que ya sabemos **cómo utilizar Nmap de forma básica para analizar los puertos TCP y UDP de un sistema**. También hemos visto en detalle lo que ocurre a nivel de red y **cómo determina Nmap si un puerto TCP o UDP está activo o no**. Finalmente, sabemos cómo seleccionar finamente los puertos que queremos analizar y **qué hacen realmente las opciones por omisión de Nmap**. En lo que sigue, reutilizaremos estos conocimientos y los aplicaremos al sondeo de una red completa, incluyendo el mapeo global y el descubrimiento de redes.




## 5 - Mapeo y descubrimiento de redes con Nmap



### I. Presentación



En esta sección, aprenderemos a utilizar la herramienta de escaneo de red Nmap para mapear tu red. Veremos lo eficaz que puede ser en esta tarea, a través de sus diversas opciones. Por último, veremos diferentes formas de especificar los objetivos de nuestros escaneos a Nmap.



En particular, usaremos lo que aprendimos en la sección anterior sobre cómo Nmap determina si un host está activo y accesible.



Como se mencionó en la introducción a Nmap, se trata de un mapeador de red. Como tal, es la herramienta perfecta para elaborar una lista de hosts accesibles en una red, ya sea local o remota.



**Retorno del autor:**



De hecho, como auditor de ciberseguridad y pentester, utilizo Nmap sistemáticamente cuando realizo pruebas de penetración internas para saber dónde estoy, quiénes son mis vecinos en la red local y qué otras redes son accesibles, así como los sistemas ubicados en ellas. Mi objetivo es simple: cartografiar la red, determinar el tamaño del sistema de información y, en particular, esbozar su superficie de ataque.



El mapeo de redes también puede ser útil en el contexto del diagnóstico de redes, la supervisión, el mapeo de activos (¿está realmente seguro de que su SI se compone únicamente de lo que está en el Directorio Activo o en su Inventario GLPI/OCS? También puede utilizarse para detectar la presencia de Shadow IT en su sistema de información.



### II. Uso de Nmap para escanear un rango de red



#### A. Descubriendo una red con un escaneo Nmap



Ahora nos gustaría subir una marcha y analizar toda nuestra red local. Nada más sencillo: todo lo que tenemos que hacer es reutilizar los comandos que vimos en la sección anterior, pero especificando un CIDR en lugar de una simple IP Address.



Un CIDR (**Classless Inter Domain Routing**) es la notación "clásica" para especificar un rango de red y su extensión (mediante la máscara). Por ejemplo, "192.168.0.0/24" es una "traducción" de la notación de máscara decimal "255.255.255.0".



Para utilizar Nmap especificando un CIDR, podemos utilizarlo de la siguiente manera:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



También es posible, como en el caso de los puertos de la sección anterior, especificar varios hosts, varias redes o un rango:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



He aquí un ejemplo de los resultados que podríamos obtener al ejecutar un escaneo en una red:



![nmap-image](assets/fr/26.webp)



resultados de un escaneo Nmap para mapear varias redes



En concreto, vemos varios hosts activos, y cada sección de host comienza con una línea como ésta:



```
Nmap scan report for <name> (<IP>)
```



Esto nos permite ver claramente a qué host se refieren los siguientes resultados. La última línea también es importante:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Sabemos que, en las redes escaneadas, Nmap descubrió 5 hosts activos.



#### B. Bajo el capó: análisis de la red mediante Wireshark



Ahora vamos a echar un vistazo más de cerca a lo que sucede a nivel de red durante un descubrimiento de red realizado a través de Nmap.



Como vimos en la sección anterior, por defecto Nmap utilizará el protocolo ARP para detectar la presencia de hosts en la red local:



![nmap-image](assets/fr/27.webp)



paquetes ARP capturados al escanear una red local utilizando Nmap y sus opciones por defecto



De este modo, es capaz de detectar prácticamente todos los hosts de la red local, ya que la respuesta a una solicitud ARP suele ser proporcionada por todos los hosts activos en la red y no parece sospechosa en modo alguno.



Para redes remotas, Nmap utiliza una combinación de técnicas:



![nmap-image](assets/fr/28.webp)



iCMP y paquetes TCP capturados al escanear una red remota utilizando Nmap y sus opciones por defecto



Para ser más precisos, Nmap utiliza un paquete eco ICMP (el caso clásico de ping) y un paquete ICMP Timestamp, normalmente utilizado para calcular los tiempos de tránsito de los paquetes. Espera obtener una respuesta de hosts en redes remotas.



Pero hay más que eso. Puedes ver en la captura de Wireshark de arriba que los paquetes **TCP SYN** se envían sistemáticamente a los puertos TCP/443 de cada host potencial de las redes que se van a escanear, así como los paquetes **TCP ACK** al puerto TCP/80.



**¿Por qué enviar paquetes TCP a los puertos como parte del descubrimiento de la red?



Enviar un paquete SYN a un puerto dado permite a Nmap **determinar si un servicio está escuchando en ese puerto**. Si un host responde a un paquete SYN con un paquete SYN/ACK, esto indica que está activo y que un servicio está escuchando en ese puerto. Por tanto, Nmap prueba suerte en este servicio, **incluso si no se ha obtenido respuesta al ping**.



El envío de un paquete ACK a un puerto dado permite a Nmap **determinar si hay un cortafuegos presente en ese sistema**. Si un sistema responde a un paquete ACK con un paquete RST (Reset), esto indica que probablemente hay un cortafuegos en ese sistema y que está bloqueando el tráfico no solicitado. El host delata así su presencia en la red, aunque no haya respondido a otras peticiones.



Sin embargo, es importante tener en cuenta que la detección de cortafuegos mediante esta técnica puede no ser perfectamente fiable en todos los casos. Algunos hosts pueden generate respuestas RST por razones distintas a la presencia de un cortafuegos, como la configuración específica del servicio o del sistema operativo. Además, los cortafuegos modernos pueden configurarse para no responder a intentos de detección de este tipo.



Ahora hemos recorrido un largo camino y podemos realizar un descubrimiento básico de la red. Ahora vamos a ver algunas opciones más que nos darán un mayor control sobre el comportamiento de Nmap.



### III. Descubrimiento de red sin escaneo de puertos con Nmap



Como habrá notado, por omisión Nmap **realiza un sondeo de puertos tras el descubrimiento de un sistema activo**, lo que añade una gran cantidad de paquetes y espera de respuestas a nuestro sondeo. Si tiene 5 máquinas en su red, Nmap intentará comprobar el estado de unos 5.000 puertos, lo que le llevará más tiempo.



Sin embargo, es posible utilizar las opciones de Nmap para realizar **sólo un descubrimiento de hosts activos** en una red, sin descubrir sus servicios.



Si sólo queremos saber qué hosts son alcanzables, sin ninguna información sobre los servicios y puertos que exponen, entonces podemos usar la opción "-sn" para realizar **sólo un escaneo usando ICMP Echo (ping) y peticiones ARP**. En otras palabras, deshabilitar completamente el escaneo de puertos:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Aquí está el resultado de un descubrimiento de red Nmap realizado sin escaneo de puertos:



![nmap-image](assets/fr/29.webp)



Resultado de un descubrimiento de red sin escaneo de puertos con Nmap.



Ya hemos mencionado las posibles limitaciones de utilizar sólo ICMP para el descubrimiento de hosts (para redes remotas). Por eso Nmap también utiliza algunos trucos que pueden delatar la presencia de un cortafuegos o un servicio específico en los sistemas. Con la ayuda de las opciones, podemos reutilizar estos trucos e incluso ampliarlos, sin tener que empezar de nuevo con un sondeo de puertos completo de cada máquina descubierta.



Para ello, utilizaremos las opciones "-PS" (TCP SYN) y "-PA" (TCP ACK), que nos permitirán especificar los puertos a los que deseamos unirnos como parte de nuestro descubrimiento de hosts, así como la opción "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Este análisis ya garantiza que el descubrimiento de hosts sea un poco más completo que con las opciones predeterminadas.



Estamos empezando a conseguir comandos bastante completos, utilizando múltiples opciones. Esto se debe a que sabemos cómo funciona Nmap y las limitaciones de sus opciones "por defecto", que a veces pueden hacernos perder tiempo o pasar por alto importantes Elements. ¡Ese es el objetivo de tomarse el tiempo para dominarlo!



Para detallar las opciones de nuestro último pedido:





- "`-sn`: desactiva el escaneo de puertos para cada host activo descubierto por Nmap.





- "`-PP`: habilita el eco ICMP (escaneo ping) para el descubrimiento de hosts.





- "`-PS <PORT>`": envía un paquete TCP SYN en el puerto o puertos indicados para detectar cualquier servicio activo que delate la presencia de un host que no haya respondido al ping.





- "`-PA <PORT>`": envía un paquete TCP ACK en el puerto o puertos indicados para detectar cualquier cortafuegos activo que delate la presencia de un host que no haya respondido al ping.




En el ejemplo anterior, especifico los puertos que considero más frecuentemente expuestos en mis contextos Nmap para la opción "-PS". Estos diferentes puertos serán entonces probados en cada host, no para ver si el servicio que albergan está realmente activo, sino para ver si esto nos permite descubrir un host que no ha respondido a nuestro ICMP Echo mientras sigue activo (a través de una respuesta del servicio o del cortafuegos del host).



Esto es lo que puede verse en una captura de red tomada en el momento de un escaneo de este tipo, en este caso un extracto en un único host objetivo:



![nmap-image](assets/fr/30.webp)



paquetes enviados por Nmap durante el descubrimiento avanzado de redes, sin escaneo de puertos



Encontramos nuestros paquetes TCP SYN, nuestro TCP ACK en el puerto TCP/80 y nuestro eco ICMP. Nmap realizará todas estas pruebas para cada host objetivo de nuestro escaneo de descubrimiento de red.



### IV. Uso de un archivo de activos como objetivo con Nmap



La especificación de objetivos puede resultar compleja rápidamente en los sistemas de información de la vida real, que a veces pueden estar formados por docenas o cientos de redes, subredes y VLAN. Por eso es más fácil utilizar un archivo como fuente para Nmap que especificarlos uno a uno en la línea de comandos.



Para empezar, cree un archivo sencillo que contenga una entrada por línea:



![nmap-image](assets/fr/31.webp)



que contiene un objetivo (host o red) por línea



A continuación, podemos utilizar todas las opciones de Nmap vistas hasta ahora y especificar la opción "-iL <ruta/archivo>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap incluirá entonces en su escaneo todos los objetivos contenidos en nuestro archivo.



Si quiere estar seguro de que se tendrán en cuenta todos sus objetivos, puede utilizar la opción "-sL -n". Nmap sólo interpretará los CIDRs y hosts del fichero y se los mostrará, sin enviar ningún paquete a través de la red:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Esto asegura que la lista de hosts a escanear es precisa.



Un último consejo importante que me gustaría compartir con ustedes se refiere a la **exclusión del host o de la red como parte de un escaneado**. Esta necesidad de excluir un host puede ser necesaria en varios casos, particularmente si queremos estar seguros de que **un componente sensible del sistema de información no es perturbado o interrumpido por nuestros escaneos**.



Ejemplos frecuentes de este tipo de necesidades se dan cuando una empresa posee equipos industriales (PLC) o sanitarios. A veces, estos equipos están mal diseñados y no están en absoluto pensados para recibir paquetes mal formateados, o demasiados. Por razones obvias de disponibilidad o de riesgo empresarial o humano, es preferible excluirlos de las pruebas.



Para excluir direcciones IP o redes de nuestro escaneo, podemos utilizar la opción "--exclude" de Nmap, por ejemplo:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



En este ejemplo, estoy analizando la red "192.168.1.0/24" pero excluyendo el sistema "192.168.1.140" que se encuentra allí. Nmap no enviará ningún paquete a este sistema. Otro ejemplo con exclusión de subred:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



De forma similar, escaneo la red grande "10.0.0.0/16", pero la red "10.0.100.0/24" no será escaneada. De nuevo, recomiendo usar la opción "-sL -n" para tener una visión muy clara de qué hosts serán escaneados y cuáles serán excluidos del escaneo, especialmente si estás operando en un contexto sensible.



### V. Descubrimiento de redes y escaneo de puertos



Ahora podemos combinar lo que hemos aprendido en esta sección con lo que aprendimos en la sección anterior sobre las opciones de sondeo de puertos. Por omisión, hemos visto que Nmap analizará los 1000 puertos más frecuentes en cada máquina activa que descubra. Hemos visto cómo evitar este comportamiento si no lo queremos, pero podemos controlarlo completamente, e incluso ampliarlo si se adapta a nuestras necesidades.



Por ejemplo, el siguiente comando comprobará la presencia de un servicio de escucha en el puerto TCP/22 en cada host escaneado:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap realizará primero un descubrimiento de red para listar los hosts activos, y para cada uno de ellos, comprobará que hay un servicio presente en el puerto TCP/22.



Del mismo modo, podemos realizar un escaneo completo de todos los puertos TCP en cada host descubierto en la red "192.168.0.0/24", excluyendo el host "192.168.0.4", por ejemplo:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Eres libre de combinar todas las opciones que hemos aprendido hasta ahora para adaptarlas a tus propias necesidades.



### VI. Conclusión



En esta sección hemos visto cómo utilizar Nmap para mapear la red utilizando varias opciones. Ahora tenemos un conocimiento más preciso de los objetivos de nuestros sondeos, así como del comportamiento del sondeo de puertos de Nmap y del método de descubrimiento de hosts. Y lo más importante, sabemos cuál es el comportamiento por omisión y las limitaciones de Nmap, y cómo utilizar sus opciones principales para ir más allá.



En la siguiente sección, veremos los mecanismos y opciones para descubrir las versiones de los servicios y sistemas operativos analizados por Nmap.




## 6 - Detección de versiones de servicios y sistemas operativos con Nmap



### I. Presentación



En esta sección, aprenderemos a utilizar Nmap para descubrir y detectar con precisión las versiones de los servicios y sistemas operativos utilizados por los hosts analizados. Veremos en detalle cómo Nmap lleva a cabo esta tarea, así como las limitaciones de la herramienta para comprender e interpretar mejor sus resultados.



Como hemos visto en secciones anteriores de este tutorial, por omisión, Nmap no mirará qué servicio está expuesto en los puertos que analiza y considera abiertos. Así que si está escuchando un servicio web en el puerto TCP/22, Nmap seguirá informando de que está abierto, pero como un servicio `SSH`. Esto se debe a que utiliza una [base de datos](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) local de su sistema para buscar una relación entre un puerto/protocolo y el nombre de un servicio (el fichero `/etc/services/`).



En la mayoría de los casos, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) le proporcionará la información correcta, ya que es raro encontrar estos casos en un entorno de producción. Sin embargo, el resto de los casos serán situaciones en las que un servicio clásico ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, etc.) esté expuesto en un puerto no clásico (por ejemplo, 2022 para un servicio SSH), en cuyo caso Nmap no encontrará una coincidencia en su base de datos local, o una que no coincida con la realidad, y se perderá información importante.



Afortunadamente, Nmap ofrece opciones y mecanismos muy precisos para descubrir qué servicio exacto puede esconderse tras un puerto abierto. Incluso dispone de una base de datos de consultas y firmas para identificar tecnologías y versiones exactas. Además de los servicios, Nmap también puede identificar la tecnología utilizada y su versión.



Eso es lo que veremos en esta sección.



### II. Cómo detectar una tecnología o versión



#### A. Recordatorio de cómo identificar una tecnología o versión



Identificar una tecnología y una versión implica recuperar el nombre del servicio, CMS, aplicación o software que escucha en el puerto objetivo. Por ejemplo, una página web está gestionada por un CMS (`WordPress`), ejecutada por un servicio web (`Apache`, IIS, Nginx) y alojada en un servidor (Linux o Windows). Pero, ¿cómo saber qué servicio web se está ejecutando?



La metodología clásica para averiguar esta información es el _banner grabbing_, que consiste simplemente en localizar dónde el servicio en cuestión muestra esta información y leer los datos. Muy a menudo, en su configuración o procesamiento por defecto, los servicios muestran su nombre e incluso su versión como primera respuesta tras una conexión.



![nmap-image](assets/fr/32.webp)



mostrar una versión en cuanto un servicio FTP establece una conexión TCP



Aquí vemos que una simple conexión TCP a este servicio a través de `telnet` resulta en un paquete TCP que contiene su tecnología y versión.



Una vez que se tiene una idea del tipo de servicio con el que se está tratando, también se pueden enviar comandos o peticiones específicas a ese servicio para extraer información de él. Estas peticiones/comandos también se pueden enviar a ciegas (sin estar seguro de que se trata del tipo de servicio correcto), con la esperanza de que alguna de ellas provoque una respuesta del servicio en cuestión.



En otros casos, más avanzados, es necesario enviar paquetes específicos para provocar una reacción, como un error, que proporcionará información detallada sobre la versión o la tecnología utilizada.



Como puedes imaginar, Nmap utilizará todas estas técnicas para intentar identificar el tipo exacto de servicio alojado en un puerto, así como el nombre de su tecnología y versión.



#### B. Entendiendo las Sondas y Coincidencias de Nmap



Para realizar todas estas comprobaciones en cada puerto escaneado, Nmap utiliza una base de datos local que se actualiza con frecuencia (al igual que el binario o sus módulos). Se trata de un fichero de texto de varios miles de líneas: `/usr/share/nmap/nmap-service-probes`.



Este fichero se compone de numerosas entradas, todas ellas organizadas en torno a dos directrices principales:





- El `Probe`: esta es la definición del paquete que Nmap enviará en un intento de provocar una reacción del servicio a identificar. Piense en ello como un intento ciego del tipo _Hola? ¿Guten Tag? Hola? Um... ¿Buenos Días quizás?_. Tan pronto como el servicio objetivo reciba una sonda que entienda (es decir, que hable el protocolo correcto), responderá a Nmap, que entonces tendrá confirmación del tipo de servicio que es.





- Match": son expresiones regulares que Nmap aplica a la respuesta obtenida. Si el envío de una petición HTTP GET ha provocado una respuesta del servicio, aplicará decenas de expresiones regulares a esta respuesta para identificar la presencia de, por ejemplo, la palabra `Apache`, `Nginx`, `Microsoft IIS`, etc.




Hay algunas directivas más para casos concretos, pero las principales para entender cómo funciona Nmap y personalizar su uso son éstas. Para hacer esta parte teórica más concreta, he aquí un ejemplo:



![nmap-image](assets/fr/33.webp)



ejemplo de una sonda en el archivo `/usr/share/nmap/nmap-service-probes` de Nmap



En la primera línea de este ejemplo, vemos una sonda fácil de entender llamada `GetRequest`. Se trata de un paquete TCP que contiene una petición HTTP GET vacía a la raíz del servicio web utilizando HTTP/1.0, seguida de un salto de línea y una línea vacía.



La línea `ports` indica a Nmap a qué puerto debe enviar esta sonda. Esto le permite priorizar las pruebas y ahorrar tiempo.



Por último, tenemos dos ejemplos de `match`. El primero, por ejemplo, categorizará el servicio web escaneado como `ajp13` si la expresión regular contenida en esta línea coincide con la respuesta de servicio recibida.



Para ayudarte a entender qué aspecto pueden tener las Sondas, aquí tienes una lista de algunas de las Sondas que encontrarás en este archivo (hay 188 en total en el momento de escribir este tutorial).



![nmap-image](assets/fr/34.webp)



ejemplo de varias Sondas utilizadas por Nmap y presentes en el fichero `/usr/share/nmap/nmap-service-probes`._



Los dos primeros (llamados `NULL` y `GenericLines`) son de particular interés aquí, ya que simplemente envían un paquete TCP vacío o uno que contiene un salto de línea. Los servicios de servidor suelen anunciarse precisamente en cuanto se recibe una conexión, sin ninguna acción, orden o petición específica por parte del cliente.



He aquí el caso de un _match_ algo más complejo:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



La expresión regular exacta está contenida aquí entre la `m|` y la `|`, que delimita cualquier expresión regular en este fichero. Por favor, tómese su tiempo para leer todo el ejemplo. Notará una selección en la expresión regular: `([\d.]+)`, usada para aislar una versión. Este ejemplo también define otros Elements como el nombre del producto `p/nginx/`, la versión recuperada `v/$1/` y el CPE con la versión `cpe:/a:igor_sysoev:nginx:$1/`.



Un CPE (Common Platform Enumeration) es un sistema de notación normalizado utilizado para identificar y describir software y hardware. Este formato permite una gestión más eficaz de las vulnerabilidades y configuraciones de seguridad y, sobre todo, una forma unificada de representarlas, sea cual sea el producto en cuestión. He aquí dos ejemplos de CPE: `cpe:/o:microsoft:windows_8.1:r1` y `cpe:/a:apache:http_server:2.4.35`



Aquí identificamos claramente sus tipos `o` para SO, `a` para aplicación, vendedor, producto y versiones.



Así, en caso de _parejar_ con una de estas expresiones regulares, obtendremos no sólo el nombre del servicio, sino también su versión y CPE exacto, facilitando la búsqueda de CVEs que afecten a esta versión. Encontrará esta información en la salida estándar de Nmap, y verá que es muy útil para otros propósitos que cubriremos en algunas secciones.



La sintaxis exacta de _matches_ y, más en general, de las directivas del fichero `/usr/share/nmap/nmap-service-probes` no se queda ahí, y puede parecer algo compleja si no está acostumbrado a manipular Nmap y sus resultados. Sin embargo, al menos debería tener presente su existencia y funcionamiento general, lo que le resultará útil más adelante cuando quiera entender o depurar un resultado, personalizar un sondeo o incluso contribuir al desarrollo de Nmap.



### III. Uso de Nmap para detectar versiones



Ahora vamos a utilizar toda esta compleja mecánica de _Probe_ y _Match_ a través de una simple opción: `-sV`. Esto simplemente le dice a Nmap: intenta averiguar exactamente qué servicios y versiones de puertos has establecido como abiertos.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



He aquí un ejemplo completo del resultado de una orden de este tipo:



![nmap-image](assets/fr/35.webp)



resultados de la detección de la versión de Nmap de las aplicaciones expuestas en la red



Aquí podemos ver que Nmap ha conseguido identificar todas las versiones de los servicios de red expuestos por este objetivo, y muestra esta información en una nueva columna `VERSION`. Es posible ver información bastante precisa, incluso hasta el sistema operativo, si esta información forma parte de la firma recuperada.



Para comprender en detalle lo que ocurre durante una exploración de vulnerabilidades, podemos utilizar la opción `--version-trace`. Esto proporcionará una vista en modo depuración, mostrando el _Probe_ que condujo a la detección:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Como resultado, tendremos mucha información que ordenar. Intenta identificar las líneas que empiezan por `Service scan Hard match`. Entonces verás líneas como estas:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Podemos ver claramente qué _Probes_ se utilizaron para detectar la tecnología y la versión (en este caso las _Probes_ `NULL` y `GetRequest`), así como la información recuperada.



### IV. Dominio de las pruebas y precisión de la detección



Ahora vamos a volver a una directiva en el archivo `/usr/share/nmap/nmap-service-probes` que no vimos antes:



![nmap-image](assets/fr/36.webp)



directiva `rarity` de sondas en el archivo `/usr/share/nmap/nmap-service-probes`._



Esta directiva se utiliza para indicar la rareza (es decir, prioridad/probabilidad) asociada a una _Probe_. Esta notación de 1 a 9 le permite controlar la exhaustividad del análisis realizado por Nmap al enviar _Probes_. En el sistema de "notación" de Nmap, una rareza de 1 proporciona información en la gran mayoría de los casos, mientras que una rareza de 8 o 9 representa un caso muy especial, específico de una configuración o servicio que raramente está presente.



Para ser más claros, en un caso por defecto, Nmap enviará a cada servicio a identificar las _Sondas_ que tengan una rareza de 1 a 7. Para darle una mejor idea de la distribución de _Probes_ por _rarity_, aquí está su recuento:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Puede parecer contraintuitivo, hay más `rarity` 8 y 9 que el resto. Esto se debe precisamente a que las Sondas de rareza 1 son genéricas y funcionan en la mayoría de los casos, independientemente del servicio (recuerde la Sonda `NULL` que simplemente envía un paquete TCP vacío). Mientras que las Sondas más complejas son casi únicas por servicio.



Si deseamos gestionar manualmente las sondas que queremos utilizar en nuestro escaneo de versiones, podemos utilizar la opción `--version-intensity`. He aquí dos ejemplos:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Para terminar con este tema, he aquí un ejemplo de _Probe_ 9 y 8:



![nmap-image](assets/fr/37.webp)



ejemplos de Sonda en rareza 8 y 9 en el archivo `/usr/share/nmap/nmap-service-probes`._



Estas dos _Sondas_ detectan servidores de Quake1 y Quake2 (el videojuego). Interesante para el lado nostálgico, pero poco probable que sea de mucha utilidad en la vida cotidiana.



Dependiendo de sus necesidades de precisión o rapidez, recuerde que este principio de "rareza" existe y puede influir en el resultado.



### V. Uso de Nmap para detectar sistemas operativos



Ahora veremos cómo Nmap puede ayudarnos a detectar los sistemas operativos de los hosts escaneados y detectados en una red. Para ello, utilice la opción `-O` (para `OS Scan`) de Nmap.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



He aquí un ejemplo de los resultados. Aquí, Nmap nos dice que probablemente se trate de un SO Linux, y nos ofrece varias estadísticas relativas a su versión exacta.



![nmap-image](assets/fr/38.webp)



detección de la probabilidad de identificación de un sistema operativo por Nmap



Para conseguirlo, Nmap utilizará multitud de técnicas que funcionan de forma muy similar a _Probes_ y _Matches_ para la detección de tecnologías y versiones. La principal diferencia es que Nmap utilizará parámetros de bastante "bajo nivel" de ICMP, TCP, UDP y otros protocolos. Aquí hay dos ejemplos de prueba para detectar un sistema operativo Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



ejemplos de pruebas realizadas por Nmap para detectar un SO Windows 11



Admitámoslo, estas pruebas son muy difíciles de interpretar, y no vamos a intentar entenderlas en profundidad en el contexto de un tutorial introductorio de Nmap. Si quiere profundizar en el tema, el fichero que contiene esta información es `/usr/share/nmap/nmap-os-db`.



Sin embargo, debe tener en cuenta que la detección del SO es más una probabilidad establecida por Nmap que una certeza.



### VI. Conclusión



En esta sección hemos aprendido a utilizar las opciones de Nmap para detectar las tecnologías, versiones y sistemas operativos de los hosts y servicios analizados. Ahora entendemos cómo Nmap obtiene esta información de forma remota. También hemos revisado las opciones para gestionar la verbosidad y la precisión de las pruebas, así como las limitaciones de la herramienta en estos temas.



En la siguiente sección aprenderemos a utilizar los scripts NSE de Nmap para realizar un análisis de seguridad de nuestro sistema de información. Tómate tu tiempo para releer las últimas secciones si lo necesitas, y no dudes en practicar y adentrarte tú mismo en las entrañas de la herramienta para dominar mejor lo que hemos aprendido hasta ahora.




## 7 - Análisis de seguridad: detección de vulnerabilidades



### I. Presentación



En esta sección, aprenderemos a utilizar la herramienta de exploración de red Nmap para detectar y analizar vulnerabilidades en los objetivos de nuestras exploraciones. En particular, veremos las distintas opciones disponibles para llevar a cabo esta tarea, y estudiaremos los límites de las capacidades de la herramienta para comprender e interpretar mejor sus resultados.



En esta primera sección, echaremos un vistazo al analizador de vulnerabilidades de Nmap, y veremos cómo utilizar las opciones básicas de detección de vulnerabilidades. En las siguientes secciones, veremos más de cerca cómo funciona esta característica, y cómo se puede personalizar.



### II. Uso de Nmap para detectar vulnerabilidades



Ahora queremos utilizar el escáner de red Nmap para detectar vulnerabilidades en los servicios y sistemas de nuestro sistema de información. Esto significa que además de descubrir hosts activos, enumerar servicios expuestos y detectar versiones y tecnologías, Nmap buscará vulnerabilidades.



Para lograrlo, Nmap se basa en scripts NSE (_Nmap Scripting Engine_), que pueden verse como módulos que permiten un enfoque granular de las pruebas.



Con las opciones adecuadas, pediremos a Nmap que utilice sus diversos scripts NSE en cada servicio descubierto, permitiéndonos descubrir:





- Fallos de configuración ;





- Descubrimientos adicionales y más avanzados de versiones y sistemas operativos ;





- Vulnerabilidades conocidas (CVE) ;





- Identificadores débiles ;





- Elements característico de una infección por malware ;





- Posibilidades de denegación de servicio ;





- Etc.




Como puede ver, los scripts de NSE amplían significativamente las capacidades de Nmap en cuanto a las operaciones de red que puede realizar. Y esto para realizar tareas mucho más avanzadas que nunca. La buena noticia es que, como es habitual, estas funciones pueden utilizarse simplemente a través de una opción y en un contexto predeterminado. Esto es lo que veremos a continuación.



### III. Ejemplo de exploración de vulnerabilidades



Los scripts de NSE se pueden utilizar cuando se usa Nmap para analizar un único puerto en un host, todos los servicios de ese host o todos los servicios detectados en varias redes. Por lo tanto, podemos utilizar las opciones que vamos a ver en todos los contextos que hemos estudiado hasta ahora.



Para habilitar el escaneo de vulnerabilidades a través de un escaneo Nmap, necesitamos usar la opción `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Recuerde que por omisión, si no especifica nada, Nmap sólo analizará los 1000 puertos más comunes. No detectará vulnerabilidades en los puertos más exóticos que sus objetivos puedan exponer.



Antes de utilizar esta funcionalidad en un sistema de información de producción, le invito a seguir leyendo el tutorial. En las siguientes secciones, veremos cómo controlar mejor el impacto y los tipos de pruebas que se ejecutarán.



Al reutilizar lo que hemos aprendido previamente, podemos, por ejemplo, ser más exhaustivos y escanear todos los puertos TCP de un objetivo:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Aquí está el resultado de un escaneo Nmap usando scripts NSE:



![nmap-image](assets/fr/40.webp)



ejemplo de los resultados de un escaneo de vulnerabilidades en un host a través de Nmap._



Aquí vemos la visualización de información adicional de interés en el contexto de un análisis de vulnerabilidad:





- Se puede acceder al servicio FTP de forma anónima, y no está protegido por autenticación. El script de NSE encargado de esta verificación nos lo indica, e incluso muestra parte de la estructura de árbol del servicio FTP. ¡Aquí vemos que tenemos acceso al directorio `C` del sistema Windows!





- El script de NSE encargado de la recuperación avanzada de servicios web muestra el título de la página, lo que nos da una mejor idea de lo que aloja el servicio web.





- También tenemos un mini análisis de la configuración del servicio SMB (scripts `smb2-time`, `smb-security-mode` y `smb2-security-mode`). La información se muestra de forma un poco diferente, después del resultado del análisis de red, para facilitar su lectura. En concreto, esta información indica la ausencia de firmas SMB Exchange. Esta debilidad de configuración permite que el objetivo sea utilizado en un ataque SMB Relay, un notable fallo de seguridad a menudo explotado en pruebas de intrusión/ataque cibernético.




Por supuesto, esto es sólo un ejemplo. Nmap tiene scripts de NSE para muchos servicios, dirigidos a una amplia gama de vulnerabilidades. Examinaremos más detenidamente estas posibilidades en la siguiente sección.



Para concluir esta introducción a la exploración de vulnerabilidades, he aquí un comando completo para el descubrimiento de redes, exploración de puertos TCP, detección de versiones y vulnerabilidades:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



¡He aquí un comando que empieza a parecerse más a los casos de uso realistas de Nmap!



### IV. Comprender las limitaciones de Nmap en la exploración de vulnerabilidades



Seamos claros: Nmap no es capaz de realizar una prueba de penetración completa de tu sistema de información, ni de simular una operación de Red Team. Tiene varias limitaciones que debes conocer para no tener una falsa sensación de seguridad:





- Cobertura limitada**: aunque los scripts de NSE de Nmap son potentes, la cobertura de sus pruebas puede ser limitada en comparación con otras herramientas especializadas en el descubrimiento de vulnerabilidades. Algunas vulnerabilidades pueden no estar cubiertas por los scripts de NSE disponibles, como las vulnerabilidades de Active Directory, la exposición de datos confidenciales o casos más avanzados de aplicaciones web vulnerables.





- Complejidad de la vulnerabilidad**: ciertos tipos de vulnerabilidad pueden ser difíciles de detectar utilizando scripts de NSE debido a su complejidad. Por ejemplo, las vulnerabilidades que requieren una interacción compleja con un servicio remoto pueden no ser detectadas eficazmente por Nmap (como en el caso de permisos excesivos en un archivo compartido o un fallo de control de permisos en una aplicación web).





- Detección pasiva**: Nmap se centra principalmente en exploraciones activas para detectar vulnerabilidades, lo que significa que puede no detectar de forma efectiva vulnerabilidades potenciales sin establecer una conexión activa con los hosts objetivo. Por lo tanto, las vulnerabilidades que no se manifiestan durante un análisis activo pueden pasar desapercibidas (como en el caso de una inyección de código en una aplicación web).





- Dependencia de las actualizaciones**: La [base de datos](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) de scripts NSE de Nmap está en constante evolución, pero puede haber un retraso entre el descubrimiento de una nueva vulnerabilidad y la adición del script correspondiente a Nmap. Como resultado, Nmap puede no estar siempre actualizado con las últimas vulnerabilidades.





- Falsos positivos y falsos negativos**: como con cualquier herramienta de seguridad, los scripts NSE de Nmap pueden producir falsos positivos (falsas alertas de vulnerabilidades) o falsos negativos (vulnerabilidades reales no detectadas). Esto es algo a tener en cuenta cuando se analizan los resultados de Nmap.




Así que es importante entender qué hace y qué no hace Nmap, y del mismo modo saber cómo interpretar sus resultados. En particular, hemos visto a lo largo de este tutorial que las opciones por defecto pueden llevarnos a pasar por alto importantes Elements que pueden ser descubiertos con un uso cuidadoso.



Tanto si eres administrador de sistemas de red, ingeniero de seguridad o incluso CISO, el uso de Nmap te ofrece una visión general del estado de seguridad de un sistema de información. Se trata de un primer paso importante para asegurar un sistema, que el equipo informático puede llevar a cabo con regularidad. Sin embargo, no debe sustituir la intervención y el asesoramiento de expertos en [ciberseguridad] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), que podrán descubrir los puntos débiles de forma mucho más exhaustiva que Nmap.



### V. Conclusión



En esta primera sección del Módulo 3, hemos introducido el escaneo de vulnerabilidades a través de Nmap. Ahora sabemos cómo utilizar la opción principal para realizar esta tarea, pero también conocemos los límites del ejercicio. En la siguiente sección, veremos más de cerca esta funcionalidad, utilizando scripts de NSE para multiplicar por diez la potencia de Nmap.



## 8 - Uso de los scripts NSE de Nmap



### I. Presentación



En esta sección, analizaremos en profundidad los scripts de NSE (_Nmap Scripting Engine_). En concreto, veremos por qué son uno de los grandes puntos fuertes de esta herramienta, cómo funcionan y cómo explorar y utilizar los numerosos scripts existentes.



Esta sección es la continuación del tutorial anterior, en el que aprendimos a utilizar de forma básica las funciones de exploración de vulnerabilidades de Nmap. Ahora veremos más de cerca cómo funciona [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) en este sentido, para que podamos volver a realizar escaneos más precisos y controlados.



### II. El concepto de scripts Nmap NSE



Los scripts de NSE de Nmap le permiten ampliar sus capacidades de una forma muy flexible. Están escritos en LUA, un lenguaje de scripting más fácil de manejar y acceder que el C o C# utilizado por Nmap. La ventaja de utilizar un script LUA con Nmap en lugar de una herramienta independiente es que nos permite aprovechar la velocidad de ejecución de Nmap y sus características estándar (descubrimiento de hosts, puertos y versiones, etc.).



Estos guiones están organizados por categorías, y un mismo guión puede pertenecer a más de una categoría:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Técnicamente, las categorías a las que pertenece un script se indican directamente en su código.



![nmap-image](assets/fr/41.webp)



categorías de scripts nSE `ftp-anon`._



Este ejemplo muestra parte del código del script de NSE `ftp-anon.nse`, cuya ejecución vimos en la sección anterior.



### III. Lista de guiones NSE existentes



Por omisión, los scripts de Nmap para NSE se encuentran en el directorio `/usr/share/nmap/scripts/`, sin una estructura de árbol o jerarquía específica. A continuación se muestra un resumen del contenido de este directorio:



![nmap-image](assets/fr/42.webp)



extrae el contenido del directorio `/usr/share/nmap/scripts/` que contiene los scripts de NSE._



Este directorio contiene más de 5.000 scripts de NSE. En la mayoría de los casos, la primera parte del nombre del script contiene el protocolo o la categoría a la que pertenece. Esto nos permite ordenar la lista, por ejemplo, si deseamos listar todos los scripts dirigidos al servicio FTP:



![nmap-image](assets/fr/43.webp)



lista de scripts NSE Nmap con nombres que empiezan por `ftp-`._



Nmap no ofrece realmente una opción para navegar y listar sus scripts NSE; puede utilizar el comando `--script-help` seguido del nombre de una categoría o una palabra:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Sin embargo, la salida será el nombre de cada script y su descripción, lo que no es óptimo si la búsqueda trae varias docenas de scripts:



![nmap-image](assets/fr/44.webp)



resultado de usar el comando `--script-help` de Nmap



En mi opinión, el método más eficaz es utilizar los comandos clásicos de Linux en el directorio `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



No dude en consultar el código de los módulos que le interesen para comprender mejor cómo funciona un script de NSE.



### IV. Uso de los scripts NSE de Nmap



Ahora vamos a aprender a realizar escaneos de vulnerabilidades seleccionando cuidadosamente los scripts de NSE que nos interesan.



#### A. Seleccionar guiones por categoría



Para empezar, podemos elegir ejecutar todos los scripts que pertenezcan a una categoría específica. Tenemos que indicar esta categoría o estas categorías a Nmap con el argumento `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Esta primera orden es el equivalente a la orden `nmap -sC`. Por omisión, Nmap seleccionará los scripts de la categoría `default`, pero esto es sólo por el bien del argumento. La siguiente orden, por ejemplo, utilizará todos los scripts de la categoría `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Como hemos visto, algunas categorías nos permiten identificar rápidamente lo que hacen los scripts de NSE relacionados (`discovery`, `vuln`, `exploit`), mientras que otras definen el nivel de riesgo, detección o estabilidad de la prueba realizada. Si nos encontramos en un contexto delicado y no conocemos bien las diferentes acciones que realiza nuestra selección de scripts, podemos optar por combinar las selecciones para elegir únicamente los scripts que se encuentran en las categorías `discovery` y `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Si desea excluir de forma absoluta y explícita los scripts de las categorías `dos` e `intrusive`, puede utilizar la siguiente notación:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Tenga en cuenta que especificar condiciones de exclusión como las anteriores dará lugar al uso de todas las demás categorías que no estén explícitamente excluidas. Para ser más justos, podríamos especificar, por ejemplo:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Aquí hay algunos ejemplos de cómo manejar los scripts NSE por categoría, especialmente cuando se utiliza Nmap para el análisis de vulnerabilidades en contextos de la vida real.



#### B. Seleccionar guiones como unidad



También podemos optar por realizar una única prueba específica durante un análisis, una prueba correspondiente a un script de NSE. Para ello, es necesario especificar el nombre del script en el parámetro `-script <nombre>`. Tomando como ejemplo el script `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Entonces tenemos un resultado muy preciso:



![nmap-image](assets/fr/45.webp)



resultado de utilizar el script `ftp-anon` de NSE en un puerto FTP a través de Nmap._



Vemos el resultado de ejecutar el script `ftp-anon` en el puerto 21, y en ningún otro puerto, porque especificamos la opción `-p 21`. También podríamos haber realizado un escaneo básico de puertos, ejecutando el script de NSE `ftp-anon` sólo en los servicios FTP descubiertos:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Así, Nmap también habría ejecutado esta prueba de conexión anónima si hubiera encontrado un servicio FTP en otro puerto.



Para obtener una breve descripción de lo que hace un script de NSE, puede utilizar la opción `--script-help` mencionada anteriormente:



![nmap-image](assets/fr/46.webp)



ayuda mostrar resultado para script NSE `sshv1`._



En resumen, ¡una vez más podemos reutilizar todas las opciones, servicios, versiones y tecnologías de detección de redes que hemos utilizado hasta ahora!



#### C. Gestión de argumentos de script



Durante el uso de Nmap, se encontrará con ciertos scripts de NSE que necesitan argumentos de entrada para funcionar correctamente. A continuación veremos cómo pasar argumentos a estos scripts a través de las opciones de Nmap.



Como ejemplo, tomemos el script `ssh-brute`, que permite realizar un ataque de fuerza bruta al servicio SSH.



Un ataque clásico de fuerza bruta consiste en probar varias contraseñas (a veces millones) para intentar autenticarse en una cuenta concreta. Al intentar tantas contraseñas, el atacante apuesta por la probabilidad de que el usuario haya utilizado una contraseña débil del diccionario de contraseñas utilizado para el ataque.



Este script tiene opciones "por defecto", que podríamos personalizar para adaptarlas a nuestro contexto. En el contexto de este ataque, por ejemplo, podemos proporcionar a Nmap la lista de usuarios y el diccionario de contraseñas a utilizar. Hasta donde yo sé, no es posible listar fácilmente los argumentos necesarios para un script, así que la forma más fiable es visitar la página oficial de Nmap. Se puede obtener un enlace directo a la documentación de un script de NSE en respuesta a la opción `--script-help`:



![nmap-image](assets/fr/47.webp)



resultado de mostrar la ayuda para el script `ssh-brute` de NSE con un enlace a nmap.org._



Al hacer clic en el enlace indicado, llegamos a esta página web del sitio [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



lista de argumentos que se pueden pasar al script de NSE `ssh-brute` de Nmap



Aquí tenemos una visión clara de los argumentos que se pueden utilizar, siendo los principales en nuestro contexto `passdb` (fichero que contiene una lista de contraseñas) y `userdb` (fichero que contiene una lista de usuarios). La documentación aquí se refiere a librerías internas de Nmap, ya que estos mecanismos de fuerza bruta y opciones asociadas están mutualizados para ser usados uniformemente a través de varios scripts (`ssh-brute`, `mysql-brute`, `mssql-brute`, etc.) y por tanto tendrán más o menos los mismos argumentos:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Como puede ver en esta última orden, podemos especificar los argumentos necesarios a un script de Nmap usando la opción `--scripts-args key=value,key=value`. Aquí tenemos un posible resultado de la salida de Nmap al realizar una fuerza bruta SSH mediante el script de NSE `ssh-brute`:



![nmap-image](assets/fr/49.webp)



resultado de la ejecución de fuerza bruta SSH a través de Nmap._



Como puede ver, la información generada por los scripts de NSE lleva el prefijo `NSE: [nombre del script]` en la salida interactiva (salida del terminal), lo que facilita su localización. Dentro de la visualización habitual de los resultados de Nmap, simplemente tenemos un resumen indicando si se han descubierto o no identificadores débiles (incluyendo contraseñas, recordemos).



Para ir un paso más allá, y recordarte que todo esto se puede utilizar además de todas las opciones que ya hemos visto, aquí tienes un comando que descubrirá la red `10.10.10.0/24`, escaneará los 2000 puertos TCP más frecuentes y ejecutará una búsqueda de acceso anónimo en los servicios FTP y una campaña de fuerza bruta en los servicios SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Este es sólo un ejemplo de los muchos scripts disponibles y sus opciones. Pero ahora tenemos una mejor idea de cómo manejar los scripts de NSE, si requieren argumentos y cómo pasar estos argumentos a Nmap.



### V. Conclusión



En esta sección hemos aprendido a utilizar los scripts de NSE de Nmap para realizar diversas tareas. Le invito a que se tome su tiempo para descubrir las diferentes categorías de scripts y los propios scripts, para ver cuántas pruebas pueden automatizar.



Durante varias secciones hemos ido acumulando opciones más o menos avanzadas de descubrimiento, sondeo y enumeración. A estas alturas ya debería ser consciente de que la salida de Nmap y la visualización de resultados empieza a ser bastante extensa, a veces incluso demasiado verbosa para nuestro terminal. En la siguiente sección aprenderemos a dominar esta salida, en particular almacenándola en ficheros de varios formatos.






## 9 - Gestión de los datos de salida de Nmap




### I. Presentación



En esta sección echaremos un vistazo a la salida producida por Nmap, y en particular a las distintas opciones para formatear esta salida. Veremos que Nmap puede producir varios formatos de salida para adaptarse a diferentes necesidades, y que esto también es uno de los grandes puntos fuertes de esta herramienta.



Por defecto, Nmap ofrece una vista detallada de los resultados de los escaneos y pruebas que realiza. Esto incluye los hosts y servicios escaneados, los detectados como accesibles, los detalles de los puertos abiertos, su estado y versión. Además, los detalles de los scripts de NSE también están disponibles en la salida del terminal. Sin embargo, esta salida puede convertirse rápidamente en voluminosa, incluso con un formato claro de la información, lo que puede dificultar la búsqueda de información precisa en los resultados.



### II. Dominio de los formatos de salida de Nmap



#### A. Guardar los resultados de la exploración en un archivo de texto



Para facilitar las cosas, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) hace que sea muy fácil guardar su salida en un fichero de texto. Esto puede ser útil para archivar, comparar con otras pruebas, pero también para examinar esta salida con herramientas especializadas de procesamiento de textos o lenguajes de scripting, como Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, etc. Para almacenar la salida estándar de Nmap en un fichero de texto, podemos utilizar la opción `-oN <nombre de fichero>` (la "N" de "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



No es de extrañar, ya que Nmap mostrará su salida estándar habitual en nuestro terminal, pero también en el archivo especificado.



#### B. Salida de Nmap generate en formato condensado



También existe un segundo formato de salida en el estilo "texto" que puede ser fácilmente interpretado por un humano: el formato "greppable".



Este formato fue creado para proporcionar una vista "condensada" de la salida de Nmap, estructurada de tal forma que facilite su procesamiento por herramientas como `grep`. Veamos un ejemplo de este tipo de salida:



![nmap-image](assets/fr/50.webp)



nmap escaneo de red y salida en formato "greppable"._



Aquí, he realizado un descubrimiento de red así como un escaneo de puertos y un análisis de tecnologías y versiones en una red /24, luego he almacenado la salida en un archivo en formato "greppable". Termino con un archivo que contiene 2 líneas por host activo:





- La primera línea me dice que tal o cual host está _Up_;





- Una segunda línea me dice qué puertos se han escaneado, su estado y la información sobre tecnología y versión recuperada en un formato muy específico: `<puerto>/<estado/<protocolo>//<servicio>//<versión>/,`




Este formato con un delimitador fijo permite un procesamiento rápido mediante herramientas de procesamiento de textos como `grep`, o lenguajes de scripting y programación. El siguiente comando, por ejemplo, me permite recuperar fácilmente información sobre el host `10.10.10.5` en el caso de un enorme escaneo realizado por Nmap cuya salida sería difícil de navegar:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



A la inversa, también puedo listar fácilmente todos los hosts que tienen el puerto 21 abierto, ya que los puertos y la IP están en la misma línea:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Para generate, necesitamos utilizar la opción `-oG <nombre de fichero>.gnmap` (la "G" de "grep"). Por costumbre, utilizo la extensión `.gnmap` para este tipo de archivo, pero siéntete libre de utilizar la que prefieras:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Este formato puede utilizarse para diversos fines y es especialmente útil para la secuenciación/clasificación rápida. Sin embargo, tiende a abandonarse en favor del formato que veremos a continuación.



nota: el formato greppable `-oG` está oficialmente obsoleto desde Nmap 7.90. Aún puede utilizarse por compatibilidad. Aún puede usarse por motivos de compatibilidad, pero se recomienda usar el formato XML o normal para cualquier desarrollo o análisis automatizado



#### C. Formato XML para la salida de Nmap



El último formato que merece la pena mencionar en este tutorial es XML. A diferencia de los dos formatos anteriores, éste no está diseñado para ser leído por humanos, sino por otras herramientas o scripts.



XML (_eXtensible Markup Language_) es un lenguaje de marcado utilizado para almacenar y transportar datos, que ofrece una estructura jerárquica mediante etiquetas personalizadas.



Dentro de Nmap, el formato XML se utiliza para generate informes detallados sobre los escaneos realizados, incluyendo información sobre hosts, puertos y vulnerabilidades detectadas, así como información adicional no mostrada en la salida estándar de Nmap.



Para generate un archivo de salida en formato XML, debemos utilizar la opción `-oX` ("O" de "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



El resultado es la salida estándar de Nmap en su terminal, así como un archivo en formato XML en su directorio actual.



Por supuesto, el formato XML no está diseñado para ser leído e interpretado por humanos. Sin embargo, si quiere hacer scripts o análisis automatizados en este formato de salida de Nmap, necesita tener una idea de las etiquetas y la estructura utilizada. Por ejemplo, aquí tiene parte del contenido del fichero XML creado por Nmap, que muestra los resultados del sondeo para 1 sistema:



![nmap-image](assets/fr/51.webp)



ejemplo de un registro XML para 1 host durante un escaneo Nmap



Hay mucha información aquí, y nos interesan especialmente los dos puertos abiertos:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Entendemos que este formato facilitará el análisis automatizado de los resultados, ya que cada dato está ordenado en una etiqueta o atributo específico. En particular, encontramos un dato que no habíamos visto antes: el CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Hemos mencionado brevemente el CPE en la sección 2 del módulo 2, y esta información se determina en las coincidencias durante la detección de versiones. Nmap utiliza sus mecanismos de detección de servicios, tecnologías y versiones para encontrar el CPE asociado.



Esto nos permite reutilizar esta información con las bases de datos y las aplicaciones que la utilizan. Estoy pensando en particular en la base de datos NVD, que hace referencia a los CVE. Para cada CVE, contiene los CPE afectados por la vulnerabilidad. He aquí un ejemplo de CVE relativo a `a:microsoft:internet_information_services:7.5` de la base de datos NVD:



![nmap-image](assets/fr/52.webp)



presencia de un CPE en los detalles de un CVE en la base de datos NVD



Ahora comprendemos mejor las ventajas de este formato, que ofrece una estructura muy clara de la información y contiene todos los datos recopilados o procesados por Nmap.



Como acto reflejo, guardo sistemáticamente mis escaneos de Nmap en los tres formatos a la vez. Esto es posible gracias a la opción `-oA <nombre>` ("A" de "Todos"), que creará un fichero `<nombre>.nmap`, un fichero `<nombre>.xml` y un fichero `<nombre>.gnmap`. De esta forma estoy seguro de que no me quedaré sin nada cuando necesite volver sobre los resultados.



Con estos tres formatos, debería tener todo lo que necesita para guardar y eventualmente procesar los resultados de Nmap de forma automatizada. Volveremos a utilizar el formato XML en la siguiente sección, cuando veamos cómo utilizar Nmap con otras herramientas de seguridad.



#### III. Generación de un informe HTML a partir de un escaneo Nmap



El formato XML ofrece muchas posibilidades, entre ellas la de servir de base para generar un informe en formato HTML, que resultará más agradable a la vista.



Para transformar un fichero Nmap en formato XML en una página web, utilizaremos la herramienta `xsltproc`, que tendremos que instalar primero:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Una vez instalada esta herramienta, basta con proporcionarle el archivo XML que se desea convertir y el nombre del informe HTML que se desea generar:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Como resultado, tendremos toda nuestra exploración bien estructurada, ¡incluso con algunos colores y enlaces clicables en el índice!



![nmap-image](assets/fr/53.webp)



extracto de un informe de escaneo Nmap en formato HTML generado por xsltproc._



A grandes rasgos, el archivo XML guardado por Nmap contiene una referencia a otro archivo en formato XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



La conversión a HTML es por tanto una función proporcionada y facilitada por Nmap, siendo `xsltproc` una herramienta común y reconocida para realizar esta tarea (que no proviene del conjunto de herramientas de Nmap).



XSLT (_Extensible Stylesheet Language Transformations_) es un subconjunto de XSL que permite mostrar datos XML en una página web y "transformarlos", en paralelo con estilos XSL, en información legible y formateada en formato HTML.



fuente: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



El nivel de información del informe es equivalente al del formato XML de Nmap y superior al de la salida estándar del terminal (_salida interactiva_).



### IV. Gestión del nivel de verbosidad de Nmap



A continuación veremos algunas opciones para Debugger Nmap o para seguir su progreso.



La primera opción que debemos mencionar es la opción `-v`, que incrementa la verbosidad de Nmap. He aquí un ejemplo:



![nmap-image](assets/fr/54.webp)



la salida detallada de nmap utilizando la opción `-v`._



En un sondeo dirigido a muchos hosts y puertos, la salida del terminal será difícil de explotar debido a la cantidad de información mostrada. Por esta razón, esta opción debería utilizarse en combinación con las opciones vistas anteriormente, que le permiten almacenar la salida estándar de Nmap en un fichero. La información relacionada con el uso de la verbosidad no se incluirá en este fichero de salida. Como puede ver en el ejemplo anterior, esta verbosidad le permite seguir las acciones y descubrimientos de Nmap de forma clara y directa. Para exploraciones más largas en las que la visualización de datos puede tardar en llegar, esto evita estar ciego a la actividad actual de Nmap y saber que cosas están progresando y a qué ritmo. Para aumentar la verbosidad un nivel más, puede utilizar la opción `-vv`.



Para seguir la actividad de Nmap durante su sondeo, puede utilizar la opción `--packet-trace`. Con la opción `-v` obtenemos un registro en tiempo real de todos los puertos abiertos descubiertos por Nmap, mientras que con esta opción obtenemos una línea de registro por cada paquete enviado a un puerto. Esto produce naturalmente una salida muy verbosa, pero permite una monitorización detallada de la actividad de Nmap, aquí tiene un ejemplo:



![nmap-image](assets/fr/55.webp)



monitorización detallada de la actividad de Nmap mediante `--packet-trace`._



De nuevo, esta información no se registrará en el fichero de salida producido por Nmap si se utilizan las opciones `-oN`, `-oG`, `-oX` o `-oA`.



Por último, Nmap también ofrece dos opciones de depuración: `-d` y `-dd`. Estas opciones se comportan de forma similar a la opción de verbosidad `-v`, pero añaden información técnica adicional, como un resumen de los parámetros técnicos al inicio del sondeo:



![nmap-image](assets/fr/56.webp)



las opciones de temporización se muestran en la vista de depuración de Nmap



En las próximas secciones, veremos cuáles son las opciones de "Temporización" y por qué merece la pena conocerlas.



Por último, si sólo quiere tener una visión básica y sintética del progreso del sondeo de Nmap, puede utilizar la opción `--stats-every 5s`. El "5s" aquí significa 5 segundos y puede ser modificado para adaptarse a sus necesidades. Esta es la frecuencia con la que recibiremos información de Nmap sobre su progreso:



![nmap-image](assets/fr/57.webp)



información mostrada por la opción `--stats-every` de Nmap



En particular, podemos obtener un porcentaje de progreso, así como una indicación de la fase en la que se encuentra: fase de descubrimiento del host mediante [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), fase de descubrimiento de los puertos TCP expuestos, etc. Esta información también puede obtenerse en la salida del terminal pulsando "Intro" durante un escaneo.



Sin embargo, Nmap no es muy bueno estimando cuánto tiempo llevará una tarea, entre otras cosas porque no sabe de antemano cuántos hosts y servicios tendrá que escanear.



### V. Conclusión



En esta sección hemos visto varias opciones para guardar los resultados de los sondeos de Nmap en diferentes formatos de fichero. Esto será muy útil, ya que en contextos realistas, ¡los resultados de los sondeos pueden ocupar cientos o incluso miles de líneas! También hemos visto cómo aumentar el nivel de verbosidad de Nmap con fines de depuración o para obtener un informe del progreso del sondeo.



El formato XML será particularmente útil en la siguiente sección, donde veremos algunas herramientas que pueden trabajar con los resultados de Nmap.




## 10 - Uso de Nmap con otras herramientas de seguridad



### I. Presentación



En esta sección echaremos un vistazo a algunos de los usos clásicos de Nmap con otras herramientas de seguridad libres y de código abierto. En particular, utilizaremos lo que hemos aprendido en las secciones anteriores para mejorar aún más la potencia y eficacia de Nmap.



La posibilidad de guardar los resultados de los análisis de Nmap en XML hace que los datos sean compatibles con una gran cantidad de otras herramientas. Como casi todos los lenguajes de programación y scripting actuales tienen bibliotecas capaces de analizar XML, esto hace que sea mucho más fácil procesar estos datos. Varias herramientas, especialmente las orientadas a la seguridad ofensiva, tienen funciones para procesar el formato XML generado por Nmap. Veámoslo más de cerca.



Voy a mencionar algunas herramientas ofensivas sin detallar realmente cómo se utilizan o cómo funcionan. Asumiré que el lector está familiarizado con su uso básico y que ya están operativas. Esta sección interesará especialmente a los profesionales [de la ciberseguridad] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), a las personas en formación o a quienes hayan decidido profundizar en el tema.



### II. Importar los resultados de Nmap a Metasploit



La primera herramienta que vamos a ver para reutilizar los datos de Nmap en la investigación ofensiva de seguridad y vulnerabilidades es Metasploit.



Metasploit es un marco de explotación y ataque. Es una solución gratuita y una herramienta reconocida que contiene un gran número de módulos escritos en Ruby o Python. Estos permiten explotar vulnerabilidades, realizar ataques, generar puertas traseras, gestionar callbacks (C&C o funciones de Comunicación y Control) y utilizar todo de manera uniforme.



En concreto, este conocido y ampliamente utilizado marco operativo puede trabajar con una [base de datos] postgreSQL (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) en la que se almacenan hosts, puertos, servicios, información de autenticación y mucho más.





- Documentación oficial de Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Aquí es donde Nmap y su salida entran en juego, ya que el formato XML de la salida de Nmap se puede importar fácilmente en la base de datos de Metasploit para poblar su base de datos de hosts y servicios, que luego pueden ser rápidamente designados como objetivos de tal o cual ataque.



Una vez en mi shell interactiva de Metasploit, empiezo por crear un espacio de trabajo, una especie de espacio específico para mi entorno del día:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Una vez creado mi espacio de trabajo, debemos validar que la comunicación con la base de datos está operativa:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Finalmente, podemos usar el comando `db_import` de Metasploit para importar nuestro escaneo Nmap en formato XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Este es el resultado de ejecutar todos estos comandos:



![nmap-image](assets/fr/58.webp)



importar un escaneo Nmap en formato XML a la base de datos de Metasploit



Aquí puedes ver que cada host es importado, junto con sus servicios. Estos datos se pueden mostrar a través del comando `services` o `services -p <port>` para un servicio específico:



![nmap-image](assets/fr/59.webp)



lista de servicios importados desde el archivo XML a la base de datos de Metasploit



Por último, podemos reutilizar rápida y fácilmente estos datos en un módulo gracias a la opción `-R`, que "convertirá" la lista de servicios obtenida como entrada para la directiva `RHOSTS`, que se utiliza para especificar los objetivos del ataque a realizar. He aquí un ejemplo con el módulo `ssh_login`, que permite realizar un ataque de fuerza bruta a los servicios [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



utilice la opción `services -R` para importar los servicios especificados como objetivo del ataque



Esto es sólo un pequeño ejemplo de lo que se puede hacer con los datos de Nmap en Metasploit, pero te da una pequeña idea de lo rápido y fácil que se puede reutilizar esta información como parte de una prueba de penetración, escaneo de vulnerabilidades o ciberataque. También vale la pena mencionar que Nmap se puede ejecutar directamente desde Metasploit para importar los resultados a la base de datos (comando `db_nmap`), ¡otro tema interesante a tratar!



### III. Uso de Nmap con el escáner web Aquatone



La segunda herramienta que me gustaría presentar en esta sección sobre la reutilización de los resultados de Nmap para la seguridad ofensiva y el análisis de vulnerabilidades es Aquatone.



Aquatone es un escáner web diseñado para explorar eficientemente aplicaciones web en una red. Ofrece funciones avanzadas para el descubrimiento de servicios web, identificación de subdominios, análisis de puertos y huellas dactilares de aplicaciones web. Todo ello presentado de forma clara y concisa en informes HTML, JSON y de texto para facilitar el análisis de la seguridad web.



Al igual que Metasploit, Aquatone puede procesar directamente el formato XML de Nmap y utilizarlo como objetivo para el escaneo. En concreto, puede extraer únicamente los hosts y servicios de interés (servicios web) de todos los datos que pueda contener un informe Nmap.





- Enlace a la herramienta: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Para utilizar la salida XML de Nmap con Aquatone, simplemente envíe el archivo XML en una tubería que será consumida por Aquatone. He aquí un ejemplo:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Mientras que Aquatone normalmente realiza el descubrimiento de puertos en los hosts para encontrar servicios web, en este contexto se basará únicamente en los resultados de Nmap, que ya ha realizado esta operación, con el consiguiente ahorro de tiempo:



![nmap-image](assets/fr/61.webp)



utilizando los resultados de Nmap en formato XML con `aquatone`._



Para su información, he aquí un extracto del informe elaborado por Aquatone:



![nmap-image](assets/fr/62.webp)



ejemplo de informe "aquatone



Personalmente, suelo utilizar Aquatone para hacerme una idea rápida de los tipos de sitios web presentes en la red, gracias sobre todo a su función de captura de pantalla.



También en este caso, disponer de un informe Nmap completo en formato XML ahorra tiempo y facilita su reutilización en otra herramienta.



### IV. Conclusión



Estos dos ejemplos muestran claramente que el formato XML de Nmap facilita a otras herramientas el uso de sus resultados, ya que se trata de un formato de datos estructurado y fácil de usar. Existen muchas otras herramientas capaces de procesar estos resultados, como herramientas de informes automatizados, representaciones gráficas o escáneres de vulnerabilidades propietarios más complejos.



Por supuesto, también puede desarrollar sus propios scripts y herramientas en Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) o cualquier otro lenguaje con una biblioteca de análisis XML para manipular y reutilizar los datos de resultados de Nmap como mejor le parezca.



Esta sección nos lleva al final del módulo tutorial sobre el uso más avanzado de Nmap, en particular para el escaneo de vulnerabilidades a través de scripts de NSE.



La siguiente sección del tutorial se centrará, entre otras cosas, en algunas buenas prácticas y consejos adicionales más técnicos sobre los sondeos específicos que puede realizar Nmap. También echaremos un vistazo a las opciones de optimización del rendimiento de los análisis, que son particularmente útiles cuando se analizan redes grandes.




## 11 - Mejorar el rendimiento de la exploración de la red



### I. Presentación



En este capítulo aprenderemos a optimizar la velocidad de los análisis de red realizados con Nmap utilizando varias opciones específicas. En particular, aprenderemos más sobre el funcionamiento interno de Nmap, desde la gestión del _timeout_ hasta las configuraciones preguardadas de la herramienta.



Ahora que hemos echado un buen vistazo a las características de Nmap, vamos a familiarizarnos con la bestia y su potencia. Si alguna vez has utilizado la herramienta en redes grandes, probablemente te habrás dado cuenta de que algunos escaneos pueden llevar mucho tiempo, a pesar de la potencia de la herramienta. Y con razón: un simple comando `nmap` con unas pocas opciones puede generate millones de paquetes dirigidos a cientos de miles de sistemas y servicios potenciales.



Es más, algunas configuraciones de equipos de red pueden imponer intencionadamente una velocidad más lenta (número de paquetes por segundo), a riesgo de rechazar sus paquetes o prohibir su IP Address por motivos de seguridad.



Dependiendo del contexto, puede merecer la pena intentar optimizar todo esto, como veremos en este capítulo.



En cualquier caso, puedes comprobar los valores por defecto de los parámetros que vamos a ver, así como si se han tenido en cuenta correctamente las opciones que vas a utilizar, a través de la depuración de Nmap (opción `-d` vista en un capítulo anterior):



![nmap-image](assets/fr/63.webp)



ver las opciones de Temporización a través de la opción `-d` de Nmap._



### II. Gestión de la velocidad de los escaneos de Nmap



#### A. Gestión de la paralelización



Por omisión, Nmap utiliza la paralelización en sus exploraciones para optimizarlas, y todos los parámetros que utiliza pueden modificarse a través de varias opciones. Sin embargo, los casos en los que realmente es necesario modificar estos parámetros son bastante raros, por lo que no entraremos en detalle en este tutorial:





- `--min-hostgroup/max-hostgroup <size>`: tamaño de los grupos de escaneo de hosts paralelos.





- `--min-parallelism/max-parallelism <numprobes>`: paralelización de Sondas.





- `--scan-delay/--max-scan-delay <time>`: ajusta el retardo entre Sondas.




Sólo hay que saber que existen y que se pueden utilizar.



#### B. Gestión del número de paquetes por segundo



Por omisión, el propio Nmap ajusta el número de paquetes por segundo que envía según la respuesta de la red. Pero es posible forzar este ajuste definiendo el valor máximo y/o mínimo a seguir en cuanto a número de paquetes por segundo. Este ajuste se realiza utilizando las opciones `--min-rate <number>` y `--max-rate <number>` donde `number` representa un número de paquetes por segundo. Ejemplo:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Estas opciones le permiten ajustar la velocidad de los escaneos según sus necesidades específicas, ya sea para acelerar el proceso o para limitar el ancho de banda utilizado. El último caso (limitar la velocidad de los escaneos) es el que más probablemente le lleve a estas opciones, especialmente si experimenta latencia de red al utilizar Nmap (lo cual es bastante raro).



### III. Gestión de fallos de conexión y tiempos de espera



Otro parámetro con el que podemos jugar para optimizar la velocidad de los escaneos de Nmap (o garantizar una mayor precisión) tiene que ver con _timeout_ y _retry_.



Para _timeouts_, este es el **tiempo de espera sin respuesta** tras el cual Nmap dejará de esperar una respuesta y considerará el servicio o máquina inalcanzable. Para _retry_, este es el **número de intentos sucesivos de una operación** que Nmap realizará antes de continuar.



Al igual que con la paralelización, la gestión de _timeout_ y _retry_ puede aplicarse a las fases de descubrimiento de hosts o servicios:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: especifica el tiempo de ida y vuelta de un Exchange. De nuevo, este parámetro se calcula y adapta sobre la marcha durante la exploración. Es poco probable que necesite utilizarlo, ya que Nmap calcula este tiempo sobre la marcha según la reacción de la red.





- `--max-retries <number>`: limita el número de retransmisiones de un paquete durante el sondeo de puertos. Por omisión, Nmap puede llegar hasta 10 reintentos para un mismo servicio, especialmente si encuentra latencias o pérdidas a nivel de red, pero en la mayoría de los casos sólo se realiza uno.





- `--host-timeout <time>`: especifica el tiempo máximo que Nmap pasará en un sistema para todas sus operaciones, incluyendo el sondeo de puertos, detección de servicios y cualquier otra operación relacionada con ese sistema. Si se supera este intervalo de tiempo sin ninguna respuesta o **finalización de las operaciones**, Nmap abandonará este sistema sin mostrar ningún resultado sobre él, y pasará al siguiente de su lista. Esto le permite controlar el tiempo máximo que Nmap pasa en un sistema determinado, evitando quedarse atascado en sistemas recalcitrantes y optimizando el tiempo total de sondeo.




En mi trabajo diario, utilizo las opciones `--max-retries` y `--host-timeout` para optimizar mis escaneos:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Estos parámetros ofrecen flexibilidad adicional para ajustar el comportamiento del escaneo a las necesidades específicas y a las condiciones de la red. Sin embargo, debe ser consciente de sus implicaciones en términos de carga en los hosts escaneados y la posible pérdida de precisión.



### IV. Utilización de configuraciones preparadas



Las distintas opciones que hemos visto en este capítulo se pueden utilizar individualmente o como parte de las configuraciones ya hechas que ofrece Nmap. La opción que permite utilizar estas _plantillas_ (plantillas de configuración) es `-T <número>` o `-T <nombre>`. Hay 5 niveles de _plantillas_ utilizables:



```
-T<0-5>: Set timing template (higher is faster)
```



Por defecto, Nmap utiliza _template_ 3 (_normal_), que suele ser suficiente.



Por mi parte, suelo actuar en contextos en los que necesito ser bastante rápido (sin dejar de ser lo más completo posible) y utilizo con frecuencia la opción `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Esto es lo que nos muestra la información de depuración de esta exploración:



![nmap-image](assets/fr/64.webp)



uso de la configuración `-T4` durante un escaneo Nmap



### V. Conclusión



En este capítulo hemos visto varias técnicas y opciones que puede utilizar para gestionar la potencia, agresividad y rendimiento de Nmap. Estas opciones son particularmente útiles cuando se analizan redes grandes, y más raramente para propósitos de ocultación.



En el próximo capítulo, veremos algunas de las mejores prácticas para usar Nmap y garantizar su seguridad.




## 12 - Seguridad y confidencialidad de los datos al utilizar Nmap



### I. Presentación



En este capítulo veremos una serie de buenas prácticas a adoptar en relación con la seguridad y, sobre todo, la confidencialidad de los datos producidos, procesados y almacenados por Nmap.



El uso de Nmap dentro de un sistema de información puede clasificarse rápidamente como una acción ofensiva. En consecuencia, es necesario tomar una serie de precauciones para actuar dentro de un marco legal, garantizando al mismo tiempo la seguridad de los objetivos previstos, los datos recopilados y el sistema utilizado para el escaneado.



### II. Obtención de las autorizaciones pertinentes



Antes de escanear una red o un sistema, asegúrese de haber obtenido las autorizaciones pertinentes. Escanear sistemas en busca de vulnerabilidades (`NSE scripts`) sin autorización puede ser ilegal y tener consecuencias legales, especialmente si la seguridad de los sistemas de información no forma parte de sus competencias oficiales.





- A modo de recordatorio: [Código Penal: Capítulo III: Ataques a los sistemas de tratamiento automatizado de datos](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Protección de datos sensibles



Los resultados producidos por Nmap pueden considerarse sensibles, sobre todo cuando contienen información sobre puntos débiles del sistema de información que podrían ser explotados por un atacante. Pero también cuando se refieren a sistemas que no son accesibles a todo el mundo (por ejemplo, sistemas de información sensibles, industriales, sanitarios o [de copia de seguridad] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



También hemos visto que, dependiendo de los scripts NSE utilizados, los resultados del escaneo NSE de [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) también pueden contener identificadores.



Así, un individuo malintencionado que consiga acceder a los resultados de estos escaneos tendrá a mano un mapa del sistema de información y abundante información técnica, sin haber realizado él mismo estas acciones, a riesgo de ser detectado.



Por lo tanto, es importante tener cuidado de no recopilar o almacenar de forma inapropiada información sensible cuando se utiliza Nmap, incluyendo, pero no limitado a, lo siguiente:





- Cifrar los datos de salida: si necesita almacenar o transmitir los resultados de sus sondeos Nmap, asegúrese de cifrarlos para proteger la confidencialidad de los datos. Esto evitará la interceptación no autorizada de información sensible. Lo ideal sería cifrar los datos tan pronto como salgan del sistema utilizado para realizar el sondeo (un archivo ZIP cifrado con una contraseña segura es un buen comienzo).





- Establezca controles de acceso: asegúrese de que sólo las personas autorizadas tienen acceso a los resultados de sus escaneos Nmap donde se almacenarán. Establezca controles de acceso adecuados para proteger la información sensible de accesos no autorizados.





- Vigilancia en la manipulación de datos: cuando transites, copies o proceses datos de escaneado, asegúrate de mantener la seguridad de los datos bajo estricto control. Esto significa: no dejarlos en el directorio "Download" de una estación de trabajo conectada a Internet, no dejarlos transitar por su aplicación interna HTTP file Exchange, no dejar el bloc de notas abierto sin bloquear la estación de trabajo durante la pausa para comer, etc.




### IV. Gestión de las exploraciones agresivas



Como hemos visto a lo largo de este tutorial, Nmap puede ser muy verboso a nivel de red. También puede enviar paquetes que no estén correctamente formateados, y que no respeten estrictamente la estructura del protocolo en las tramas y paquetes de red que genera. Todas estas acciones pueden repercutir en determinados sistemas y servicios, a veces hasta el punto de provocar un mal funcionamiento o la saturación de los recursos del sistema y de la red.



Para evitar cualquier incidente, es necesario dominar el comportamiento de Nmap y saber adaptarlo al contexto en el que se utiliza, mediante las distintas opciones que se comentan en este tutorial. No necesariamente utilizaremos Nmap de la misma forma en un sistema de información que contenga [hardware] industrial (https://www.it-connect.fr/actualites/actu-materiel/) que en una red de usuario formada por sistemas Windows protegidos por un cortafuegos local o en un núcleo de red.



Esperamos que las distintas lecciones de este tutorial le hayan enseñado a dominar y analizar el comportamiento de Nmap, pero la mejor forma de aprender es haciendo. Así que asegúrese de que está familiarizado con las opciones de Nmap que va a utilizar.



### V. Protección del sistema de escaneado



En el primer capítulo vimos que en la mayoría de los casos, Nmap necesita ejecutarse como `root` o administrador local. Esto se debe a que realiza operaciones de red, a veces a un nivel bastante bajo, a través de bibliotecas de red, que requieren permisos altos y arriesgados desde el punto de vista de la estabilidad del sistema o la confidencialidad de otras aplicaciones.



Como resultado, Nmap puede ser visto como un componente sensible del sistema en el que está instalado. Asegúrese de utilizar la última versión de Nmap, ya que las versiones anteriores pueden contener vulnerabilidades de seguridad conocidas. Utilizando una versión actualizada, puede minimizar los riesgos asociados al uso de la herramienta.



Si ha optado por utilizar Nmap no a través de una sesión como `root`, sino otorgando privilegios específicos a un usuario privilegiado para que tenga todo lo que necesita para utilizar Nmap (`sudo` o _capabilities_), tenga en cuenta que Nmap puede utilizarse como parte de una elevación completa de privilegios:



![nmap-image](assets/fr/65.webp)



elevación de privilegios de Nmap a través de `sudo`._



Aquí, estoy usando el comando Nmap a través de `sudo`, pero esto me permite obtener una shell interactiva como `root` en el sistema, que no era el objetivo original.



También es muy desaconsejable instalar Nmap en sistemas que no están diseñados para realizar escaneos de red. Estoy pensando en particular en servidores o estaciones de trabajo. Por un lado, esto añadiría un vector potencial para la elevación de privilegios, pero sobre todo daría al atacante acceso sin esfuerzo a una herramienta ofensiva.



Por último, la seguridad del sistema utilizado para la exploración debe garantizarse de forma más general, para que no se convierta él mismo en un vector de intrusión o de fuga de información. Como administrador del sistema, es mejor utilizar un sistema dedicado, idealmente con una vida útil limitada, en lugar de su propia estación de trabajo.



### VI. Conclusión



En conclusión, asegúrate de dominar correctamente Nmap antes de utilizarlo en condiciones reales o de producción, y mantente alerta a la hora de procesar y gestionar sus resultados. Sería una lástima causar daños, filtrar datos o facilitar un compromiso, cuando el planteamiento inicial tiene como objetivo mejorar la seguridad de tu empresa.



## 13 - Escaneo de puertos vía TCP: SYN, Connect y FIN



### I. Presentación



En este capítulo y en el siguiente veremos más de cerca los distintos tipos de sondeos TCP disponibles en Nmap, empezando por los más utilizados: SYN, Connect y FIN.



Como habrá notado, Nmap ofrece varias opciones para escaneos TCP:



![nmap-image](assets/fr/66.webp)



técnicas de escaneo disponibles en Nmap._



La idea aquí es explicar algunos de estos métodos, para ayudarte a entender sus diferencias, sus ventajas y sus limitaciones. Verás que, según el contexto o lo que quieras saber, es mejor optar por una opción u otra.



### II. TCP SYN scan o "Half Open scan



El primer tipo de sondeo TCP que vamos a ver es el `Scan SYN TCP`, también conocido como `Scan Half Open`. Si recuerda los escaneos de red que hicimos después de nuestros primeros escaneos de puertos, este es el tipo de escaneo utilizado por defecto por [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) cuando se ejecuta con derechos de root.



La traducción le ayudará a entender cómo funciona este escaneo. De hecho, un escaneo TCP SYN enviará un paquete TCP SYN a cada puerto objetivo, que es el primer paquete enviado por un cliente (el que solicita establecer una conexión) como parte del famoso _Three way handshake_ TCP. Normalmente, si el puerto está abierto en el servidor de destino, con un servicio ejecutándose detrás, el servidor enviará de vuelta un paquete TCP SYN/ACK para validar el SYN del cliente e inicializar la conexión TCP. Esta respuesta toma la forma de un paquete TCP con las banderas SYN y ACK establecidas a 1, lo que nos permite confirmar que el puerto está abierto y conduce a un servicio.



Por otro lado, si el puerto está cerrado, el servidor nos enviará un paquete `TCP` con las banderas RST y ACK a 1 para terminar la petición de conexión, por lo que sabremos que no parece haber ningún servicio activo detrás de este puerto:



![nmap-image](assets/fr/67.webp)



diagrama de comportamiento de tCP SYN Scan para puertos abiertos y cerrados



Para tener una visión más concreta del `TCP SYN Scan`, realicé un escaneo del puerto TCP/80 a un host que tenía un servidor web activo en este puerto. Ejecutando un escaneo de red con Wireshark, podemos ver el siguiente flujo (fuente del escaneo: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



captura de red durante un escaneo TCP SYN para un puerto abierto



En la primera línea, vemos que el origen del escaneo está enviando un paquete TCP al host `10.10.10.203` en el puerto TCP/80. En este paquete TCP, la bandera SYN se pone a 1 para indicar que se trata de una petición de inicialización de conexión TCP. En este paquete TCP, la bandera SYN se establece en 1 para indicar que se trata de una solicitud de inicialización de conexión TCP.



Luego, en la segunda línea, vemos que el objetivo responde con un `TCP SYN/ACK`, lo que significa que acepta inicializar una conexión y, por tanto, recibir flujos en el puerto TCP/80. Por lo tanto, podemos deducir que el puerto TCP/80 está abierto y que hay un servidor web presente en el servidor escaneado.



Nuestro host devuelve entonces un paquete RST para cerrar la conexión, permitiendo al host escaneado no mantener una conexión TCP abierta esperando respuesta. En el caso de un escaneo en muchos puertos, no cerrar las conexiones TCP podría llevar a una denegación de servicio, saturando el número de conexiones esperando respuesta que el servidor puede mantener (ver [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



En Wireshark, podrás ver el estado de las banderas TCP para cada prueba que realicemos. Esto mostrará si el paquete es un paquete SYN, SYN/ACK, ACK, etc:



![nmap-image](assets/fr/69.webp)



ver las banderas TCP de un paquete en Wireshark (TCP SYN aquí)



A la inversa, ejecuté la misma prueba entre las dos máquinas, pero esta vez escaneando un puerto TCP/81 en el que no hay ningún servicio activo (origen del escaneo: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



captura de red durante un escaneo TCP SYN para un puerto cerrado



El host escaneado devuelve un `TCP RST/ACK` en respuesta a mi `TCP SYN` cuando el puerto no está abierto.



Como se ha mencionado, cuando se ejecuta Nmap desde un terminal privilegiado, TCP SYN Scan es el modo por defecto, y puede forzarse mediante la opción `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




El `TCP SYN Scan` es el más utilizado por razones de velocidad. Por otro lado, el hecho de que un cliente no finalice el _Three Way Handshake_ (es decir, que no envíe el ACK tras el SYN/ACK del servidor) puede parecer sospechoso si se observa demasiadas veces en un servidor o desde la misma fuente en la red. De hecho, el comportamiento normal de un cliente tras recibir un paquete TCP SYN/ACK en respuesta a un TCP SYN es enviar un `acknowledgement` (ACK) y a continuación iniciar el Exchange.



No obstante, proporciona un escaneo ligeramente más rápido, ya que no se molesta en enviar un ACK por cada respuesta positiva. La ventaja de SYN Scan es su velocidad, ya que sólo se envía un paquete por puerto a escanear, a costa de una mayor probabilidad de detección.



Además, la exploración TCP SYN es capaz de detectar si un puerto está filtrado (protegido) por un cortafuegos. De hecho, se puede detectar un cortafuegos delante del host objetivo por la forma en que se comporta cuando recibe un paquete TCP SYN en un puerto que se supone que protege. Simplemente no responderá. Sin embargo, como hemos visto, en ambos casos (puerto abierto o cerrado), hay una respuesta del host. Este tercer comportamiento revelará la presencia de un cortafuegos entre el host analizado y la máquina que ejecuta el análisis. Este es el resultado que puede devolver Nmap cuando un puerto escaneado está filtrado por un cortafuegos:



![nmap-image](assets/fr/71.webp)



visualización de nmap al escanear un puerto filtrado



Cuando realizamos una captura de red en el momento del escaneo, podemos ver que no se da ninguna respuesta:



![nmap-image](assets/fr/72.webp)



captura de red durante una exploración TCP SYN de un puerto filtrado por un cortafuegos



La diferencia entre un puerto cerrado y un puerto filtrado es la siguiente: un puerto filtrado es un puerto protegido por un cortafuegos, mientras que un puerto cerrado es un puerto en el que no se está ejecutando ningún servicio y que, por tanto, no puede procesar nuestros paquetes TCP. Algunos tipos de análisis TCP, como el análisis TCP SYN, son capaces de detectar si un puerto está filtrado, mientras que otros tipos de análisis no pueden hacerlo.



### III. Escaneo TCP Connect o Escaneo Full Open



El segundo tipo de escaneo TCP es el `TCP Connect scan`, también conocido como _Full Open Scan_. Funciona de la misma manera que el escaneo TCP SYN, pero esta vez devuelve un `TCP ACK` después de una respuesta positiva del servidor (un SYN/ACK). Por eso se llama `Full Open`, ya que la conexión se abre completamente y se inicia en cada puerto abierto durante el escaneo, respetando así el TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



diagrama de comportamiento de tCP Connect Scan para puertos abiertos y cerrados



Esto es lo que se puede ver transitando por la red durante un `TCP Connect scan` apuntando a un puerto abierto:



![nmap-image](assets/fr/74.webp)



sniffing de red durante una exploración de TCP Connect en busca de un puerto abierto



Podemos ver que el primer paquete TCP enviado es un `TCP SYN` enviado por el cliente, y el servidor responderá con un `TCP SYN/ACK`, indicando que el puerto está abierto y albergando un servicio activo. Para simular un cliente legítimo, Nmap enviará un `TCP ACK` de vuelta al servidor. Por el contrario, al escanear un puerto cerrado:



![nmap-image](assets/fr/75.webp)



captura de red durante una exploración TCP Connect para un puerto cerrado



Observa que la respuesta del servidor a nuestro paquete `SYN` es una vez más un paquete `TCP RST/ACK`, por lo que podemos deducir que el puerto está cerrado y no hay ningún servicio ejecutándose en él.



Cuando se utiliza Nmap, la opción `-sT` (`scan Connect`) se utiliza para realizar un sondeo de conexión TCP. Tenga en cuenta que cuando se utiliza Nmap desde una sesión sin privilegios, este es el modo de sondeo TCP por omisión:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



El `TCP Connect Scan` simula una solicitud de conexión más legítima, con un comportamiento que se asemeja más al de un cliente lambda, por lo que es más difícil detectar un escaneo en un número reducido de puertos. Sin embargo, es más lento, ya que inicializa completamente cada conexión TCP en los puertos abiertos de la máquina escaneada.



Un escaneo Nmap de 10.000 puertos seguirá siendo fácilmente detectable si se instalan servicios de detección y protección de intrusiones en la red (IDS, IPS, EDR). Cuando un atacante quiere pasar desapercibido, tiende a centrarse en un pequeño número de puertos elegidos estratégicamente, como el 445 (SMB) o el 80 (HTTP), que suelen estar abiertos en los servidores y presentan vulnerabilidades comunes.



Dado que TCP Connect Scan espera una respuesta en ambos casos, también puede detectar la presencia de un cortafuegos que pueda estar filtrando puertos en el host de destino.



### IV. Escaneo TCP FIN o "Stealth Scan



El `TCP FIN Scan`, también conocido como _Stealth Scan_, utiliza el comportamiento de un cliente que finaliza una conexión TCP para detectar un puerto abierto.



En TCP, fin de sesión significa el envío de un paquete TCP con la bandera FIN a 1. En un Exchange normal, el servidor cesa toda comunicación con el cliente (sin respuesta). Si el servidor no tiene ninguna conexión TCP activa con el cliente, enviará un `RST/ACK`. Por lo tanto, podemos diferenciar entre puertos abiertos y cerrados enviando paquetes `TCP FIN` a un conjunto de puertos:



![nmap-image](assets/fr/76.webp)



diagrama de comportamiento del escáner tCP FIN para puertos abiertos y cerrados



He capturado de nuevo la red durante un _Stealth scan_ y esto es lo que se ve cuando el puerto escaneado está abierto:



![nmap-image](assets/fr/77.webp)



captura de red durante un escaneo TCP FIN para un puerto abierto



Podemos ver que el cliente envía uno o dos paquetes para terminar una conexión TCP y que el servidor no responde. Simplemente acepta el fin de la conexión y deja de comunicarse.



Esto es lo que vemos ahora cuando escaneamos un puerto cerrado:



![nmap-image](assets/fr/78.webp)



captura de red durante un escaneo TCP FIN para un puerto cerrado



Vemos que el servidor devuelve un paquete `TCP RST/ACK`, por lo que hay una diferencia de comportamiento entre un puerto abierto y uno cerrado, y podemos listar los puertos abiertos en un servidor enviando un paquete TCP FIN. Usando Nmap, la opción `-sF` (`scan FIN`) se usa para realizar un escaneo TCP FIN:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan no funciona en hosts Windows, porque el sistema operativo tiende a ignorar los paquetes TCP FIN cuando se envían a puertos que no están abiertos. Por lo tanto, si ejecuta un TCP FIN Scan en un host Windows, tendrá la impresión de que todos los puertos están cerrados.



Por eso es importante conocer varios métodos de escaneado y entender la diferencia entre ellos.



Dado que en ambos casos el TCP FIN no esperará una respuesta, será incapaz de detectar la presencia de un cortafuegos entre el host de destino y el origen del escaneo.



Este es un ejemplo del resultado del escaneo TCP FIN de Nmap:



![nmap-image](assets/fr/79.webp)



resultados de un escaneo TCP FIN por Nmap._



De hecho, la falta de respuesta del host en un puerto determinado puede significar que el puerto está filtrado, pero también que está abierto y activo.



Este escaneo se conoce como "sigiloso", ya que no generate mucho tráfico y generalmente no causa registro en los sistemas objetivo. Puede utilizarse para descubrir discretamente puertos en una red sin hacer saltar ninguna alarma. Sin embargo, como ya se ha mencionado, su eficacia puede variar en función del sistema objetivo, al igual que su discreción en función de la configuración de los equipos de seguridad.



### V. Conclusión



Hasta aquí el primero de los dos capítulos sobre los distintos tipos de sondeos TCP que ofrece Nmap En el siguiente capítulo veremos los tipos de sondeo TCP XMAS, Null y ACK, que funcionan de distintas formas para detectar puertos abiertos en un sistema.





## 14 - Escaneado de puertos vía TCP: XMAS, Null y ACK



### I. Presentación



En esta sección continuaremos explorando los distintos métodos de sondeo TCP que ofrece Nmap. Aquí veremos los métodos `XMAS`, `Null` y `ACK`, que utilizan características específicas de TCP para recuperar información sobre los puertos y servicios abiertos en un objetivo dado.



### II. Exploración TCP XMAS



XMAS Scan TCP es un poco inusual, ya que no simula en absoluto el comportamiento normal de un usuario o máquina en una red. De hecho, XMAS Scan enviará paquetes TCP con las banderas `URG` (Urgente), `PSH` (Push), y `FIN` (Fin) a 1, para evitar ciertos cortafuegos o mecanismos de filtrado.



El nombre XMAS viene del hecho de que ver estas banderas encendidas es inusual. Cuando las tres banderas se activan simultáneamente en un paquete TCP, parece un árbol de Navidad iluminado:



![nmap-image](assets/fr/80.webp)



indicadores tCP utilizados en la exploración XMAS



Sin entrar en detalles sobre el papel de estas banderas aquí, es importante saber que al enviar un paquete con estas tres banderas activadas, un servicio activo detrás del puerto de destino no devolverá ningún paquete. Por otro lado, si el puerto está cerrado, recibiremos un paquete TCP RST/ACK. Ahora seremos capaces de diferenciar entre el comportamiento de un puerto abierto y uno cerrado cuando listamos puertos en una máquina:



![nmap-image](assets/fr/81.webp)



diagrama de comportamiento de tCP XMAS Scan para puertos abiertos y cerrados



Siguiendo la misma lógica, un escaneo de red en el puerto TCP/80 de un host con un servidor web activo muestra el siguiente comportamiento al detectar un puerto abierto (fuente de escaneo `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



captura de red durante un escaneo TCP XMAS para un puerto abierto



Podemos ver que el origen del escaneo envía dos paquetes TCP XMAS (con las banderas `FIN`, `PSH` y `URG` a 1) al host `10.10.10.203` y que no hay retorno del objetivo, indicando que el puerto está abierto. Por el contrario, al realizar un `TCP XMAS Scan` en un puerto cerrado, se observa el siguiente resultado:



![nmap-image](assets/fr/83.webp)



captura de red durante un escaneo TCP XMAS para un puerto cerrado



La respuesta a nuestro paquete TCP es entonces un `TCP RST/ACK`, indicando que el puerto está cerrado. Para utilizar esta técnica con Nmap, la opción `-sX` (`scan XMAS`) le permite realizar un escaneo TCP XMAS:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Es importante tener en cuenta que el escaneo TCP XMAS no es capaz de detectar cortafuegos que puedan estar entre el objetivo y la máquina de escaneo, a diferencia de otros tipos de escaneo como TCP SYN o Connect. De hecho, un cortafuegos activo entre los dos hosts garantizará que no se produzca ninguna devolución TCP si el puerto objetivo está filtrado (es decir, protegido por el cortafuegos). En caso de no respuesta, es imposible saber si el puerto está protegido por el cortafuegos o si está abierto y activo. También hay que tener en cuenta que, al igual que el escaneo TCP FIN, ciertas aplicaciones o sistemas operativos como Windows pueden distorsionar los resultados de este tipo de escaneo.



nota: el soporte para escaneos XMAS/FIN/NULL en versiones recientes de Windows sigue siendo limitado, y los resultados pueden ser inconsistentes en este tipo de objetivos. (Actualización 2025)_



### III. Escaneo nulo TCP



En contraste con el escaneo TCP XMAS, el escaneo TCP Null enviará paquetes de escaneo TCP con todas las banderas a 0. Este también es un comportamiento que nunca se encontrará en un Exchange normal entre máquinas, ya que enviar un paquete TCP sin una bandera no está especificado en el RFC que describe el protocolo TCP. Por eso se puede detectar más fácilmente.



Al igual que el escaneo TCP XMAS, este escaneo puede interferir con ciertos cortafuegos o módulos de filtrado, permitiendo el paso de paquetes:



![nmap-image](assets/fr/84.webp)



diagrama de comportamiento de tCP Null Scan para puertos abiertos y cerrados



Esto es lo que puede verse en la red durante un escaneo TCP Null en un puerto abierto:



![nmap-image](assets/fr/85.webp)



captura de red durante una exploración TCP Null en busca de un puerto abierto



La máquina de exploración envía un paquete sin bandera (`[<None>]` en Wireshark) sin ninguna respuesta del servidor. Por el contrario, cuando el puerto de destino está cerrado:



![nmap-image](assets/fr/86.webp)



captura de red durante un escaneo TCP Null para un puerto cerrado



Para realizar un escaneo TCP Null con Nmap, simplemente utilice la opción `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Dado que la respuesta cuando un puerto está abierto y cuando un cortafuegos está activo (sin respuesta del servidor en ambos casos) es idéntica, el escaneo TCP Null es incapaz de detectar la presencia de un cortafuegos. Es más, el cortafuegos puede incluso falsear el resultado sugiriendo que un puerto está abierto, ya que no responde a paquetes TCP sin banderas, aunque el puerto esté filtrado. Esta es una información importante a tener en cuenta cuando se utilizan escáneres que no son capaces de diferenciar entre un puerto abierto y uno filtrado (protegido por cortafuegos), como los escáneres `TCP Null`, `XMAS` o `FIN`, con el fin de mantener la coherencia en la interpretación de los resultados obtenidos.



### IV. Exploración TCP ACK



El escaneo TCP ACK se utiliza para detectar la presencia de un cortafuegos en el host de destino o entre el destino y el origen del escaneo.



A diferencia de otros escaneos, el escaneo TCP ACK no intenta identificar qué puertos están abiertos en el host, sino si hay un sistema de filtrado activo, respondiendo para cada puerto con `filtered` o `unfiltered`. Algunos escaneos TCP, como `TCP SYN` o `TCP Connect`, pueden hacer ambas cosas a la vez, mientras que otros, como `TCP FIN` o `TCP XMAS`, no pueden determinar la presencia de filtrado en absoluto. Esta es la razón por la que el escaneo TCP ACK puede ser útil:



![nmap-image](assets/fr/87.webp)



diagrama de comportamiento de tCP ACK Scan para puertos filtrados y no filtrados



Utilizaremos la opción `-sA` de Nmap para realizar este tipo de sondeo. Este es el resultado de un sondeo TCP ACK si el puerto está filtrado, es decir, bloqueado y protegido por un cortafuegos:



![nmap-image](assets/fr/88.webp)



nmap pantalla durante TCP ACK Scan._



Ejemplo de resultado para un host con cortafuegos y otro sin él. Nmap devuelve `filtered` en los puertos TCP/80 y TCP/81 del host `10.10.10.203`. En un análisis de red mediante Wireshark, el comportamiento es el siguiente:



![nmap-image](assets/fr/89.webp)



captura de red durante una exploración TCP ACK para un puerto no filtrado por un cortafuegos



La máquina de destino no devuelve nada si hay un cortafuegos.



Para lanzar este escaneo con Nmap, utilice la opción `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Conclusión



Hemos examinado tres métodos diferentes de escaneo a través de TCP, además de los ya presentados. Estos métodos diferentes deben utilizarse en condiciones y contextos muy específicos, especialmente en el marco de pruebas de penetración u operaciones de Red Team, durante las cuales están presentes nociones de discreción.



## 15 - Nmap CheatSheet - Resumen de comandos del tutorial



### I. Presentación



Aquí tienes un breve resumen de los muchos comandos y casos de uso de Nmap, para que puedas encontrarlos rápidamente y reutilizarlos en el uso diario.



### II. Nmap: CheatSheet IT-Connect



Aquí hay una hoja de trucos de los comandos presentados. Esta página facilita la búsqueda de los usos más comunes de Nmap.





- Escaneado de puertos




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Descubrir hosts activos




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



nota: La opción `-sP` está obsoleta desde hace varios años y debería sustituirse por `-sn`. (Actualización 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Detección de versiones




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Scripts NSE: en busca de vulnerabilidades




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Gestión de la salida de Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optimización del rendimiento




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Tipos de exploración TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Espero que estos comandos te resulten útiles. No olvides adaptar el objetivo de tus exploraciones a tu contexto y consultar la documentación oficial para dominar completamente las pruebas realizadas.



### III. Conclusión



El tutorial de Nmap ha finalizado. Ahora tiene lo básico que necesita para utilizar esta completa y potente herramienta. Le recomendamos encarecidamente que practique en entornos controlados (Hack The Box, VulnHub, máquinas virtuales) antes de utilizarlo en producción.



Queda mucho por explorar sobre el funcionamiento interno y las funciones avanzadas de la herramienta. Sin embargo, el dominio de los comandos y conceptos presentados aquí le permitirá utilizar Nmap con confianza y relevancia.