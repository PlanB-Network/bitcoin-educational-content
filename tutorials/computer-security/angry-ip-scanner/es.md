---
name: Angry IP Scanner
description: Una forma sencilla de escanear su red
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian BURNEL publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



¿Cómo escanear una red Windows en busca de máquinas conectadas de forma rápida y sencilla? La respuesta es Angry IP Scanner. Este proyecto de código abierto le permite escanear una red fácilmente, utilizando un Interface gráfico fácil de usar.



Esta herramienta puede ser utilizada por particulares para **escanear su red local**, pero también por profesionales informáticos con el mismo fin. Prueba de que **esta herramienta es muy práctica**, ya ha sido utilizada por **algunos grupos cibercriminales** para escanear redes corporativas (del mismo modo que Nmap). Un buen ejemplo es [el grupo de ransomware RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Sigue siendo un software sólido, pero como ocurre con otras herramientas orientadas a la red y la seguridad, se puede abusar de su uso.



Aquí lo usaremos en **Windows 11**, pero es perfectamente posible usarlo en otras versiones de **Windows**, así como en **Linux** y **macOS**.



Menos completo que Nmap, **Angry IP** Scanner sigue siendo interesante para un análisis rápido y básico de la red, pero también porque está al alcance de cualquiera. Podrá **detectar hosts conectados a la red** e identificar **nombres de host** y **puertos abiertos**.



Si quieres ir más allá, consulta el tutorial sobre Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Primeros pasos con Angry IP Scanner



### A. Descarga e instala Angry IP Scanner



Puedes descargar la última versión de Angry IP Scanner desde la web oficial de la aplicación o desde GitHub. Nosotros utilizaremos esta última opción. Haz clic en el siguiente enlace y descarga la versión EXE: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Ejecute el ejecutable para proceder a la instalación. No hay nada especial que hacer durante la instalación.



![Image](assets/fr/013.webp)



### B. Ejecutar una exploración inicial de la red



En el primer inicio, tómate tu tiempo para leer las instrucciones de la ventana "**Cómo empezar**" para saber más sobre el funcionamiento de la herramienta. Por cierto, hay varios términos que debes tener en cuenta:





- Alimentador**: módulo encargado de generar listas de direcciones IP a escanear, a partir de un rango de IP aleatorio o de un fichero con una lista de direcciones IP.
- Fetcher**: un conjunto de módulos para recuperar información sobre hosts en la red. Existen, por ejemplo, fetchers para detectar direcciones MAC, escanear puertos, detectar nombres de host o enviar peticiones HTTP.



![Image](assets/fr/018.webp)



Para escanear una subred IP, sólo tienes que introducir la **IP Address inicial** y la **IP Address final** en el campo "**Gama IP**" (si no, cambia el tipo a la derecha). A continuación, haz clic en el botón "**Iniciar**".



![Image](assets/fr/019.webp)



Unas decenas de segundos más tarde, el resultado será visible en el Interface del software. **Para cada IP Address en el rango analizado, verás si Angry IP Scanner ha detectado un host o no.** También aparecerá un resumen en la pantalla, indicando el número de hosts activos (en este caso 6) y el número de hosts con puertos abiertos.



![Image](assets/fr/020.webp)



Aquí, podemos ver la presencia de un host llamado "**OPNsense.local.domain**", asociado con la IP Address "**192.168.10.1**" y accesible en los **puertos 80** y **443** (HTTP y HTTPS). Haciendo clic con el botón derecho del ratón sobre el host se accede a comandos adicionales, como ping, trazar ruta y apertura del navegador a través de esta IP Address.



![Image](assets/fr/012.webp)



### C. Añadir puertos de escaneo



Por defecto, **Angry IP Scanner** escaneará 3 puertos: **80** (HTTP), **443** (HTTPS) y **8080**. Puedes añadir más puertos a escanear desde las preferencias de la aplicación. Haz clic en el menú "**Herramientas**" y luego en la pestaña "**Puertos**".



Aquí puede modificar la lista de puertos a través de la opción "**Selección de puertos**". Puede **indicar números de puerto específicos separados por una coma, o rangos de puertos**. El ejemplo siguiente añade dos puertos: **445** (SMB) y **389** (LDAP). Para escanear puertos del 1 al 1000, introduzca "**1-1000**". No se especifica si los escaneos de puertos se realizan en TCP, UDP o ambos.



![Image](assets/fr/021.webp)



Si ejecutas el escaneo de nuevo, es probable que obtengas nueva información. En el ejemplo de abajo, Angry IP Scanner me dice que los puertos 389 y 445 están abiertos en los hosts "**SRV-ADDS-01**" y "**SRV-ADDS-02**", gracias a la nueva configuración de puertos a escanear.



![Image](assets/fr/022.webp)



**Nota**: desde el menú "**Escáner**", puede exportar los resultados del escaneado a un archivo de texto.



Si desea llevar el escaneado más allá, haga clic en el menú "**Herramientas**" y, a continuación, en "**Captadores**". Esto añade "capacidades" a la exploración. Basta con seleccionar un "fetcher" y moverlo a la izquierda para activarlo. Esto añadirá una columna extra al resultado del escaneo.



![Image](assets/fr/014.webp)



El ejemplo siguiente muestra las funciones "**Información sobre NetBIOS**" y "**Detección web**". La primera proporciona información adicional como la MAC Address y el nombre de dominio de la máquina, mientras que la segunda muestra el título de la página web (que puede dar alguna indicación del tipo de servidor web o aplicación).



![Image](assets/fr/011.webp)



Por último, desde las preferencias, también puedes cambiar el método utilizado para "**ping**", es decir, para considerar si un host está activo o no. Dado que algunos hosts no responden a los pings, esto te permite probar otros métodos (paquete UDP, sonda de puerto TCP, ARP, combinación UDP + TCP, etc.).



## III. Conclusión



Simple y eficaz: Angry IP Scanner detecta hosts conectados a una red, y te permite configurar escaneos de puertos. En términos de opciones, no es tan flexible como Nmap, y no va tan lejos, pero es un buen comienzo para un escaneo rápido.



Si quieres usar **Nmap** con un Interface gráfico, puedes usar **la aplicación Zenmap** (ver descripción más abajo).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d