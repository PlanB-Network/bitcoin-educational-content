---
name: Lynis
description: Realizar una auditoría de seguridad de una máquina Linux con Lynis
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en el contenido original de Fares CHELLOUG publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



**En este tutorial, vamos a aprender cómo realizar una auditoría de seguridad en una máquina Linux usando Lynis Para aquellos que no conozcan **Lynis,** es una pequeña utilidad de línea de comandos que analizará la configuración de tu servidor y hará recomendaciones para **mejorar la seguridad de tu máquina.**



Lynis es una herramienta de código abierto de CISOFY, una empresa especializada en **auditoría y endurecimiento de sistemas**. Si quieres progresar en el hardening de Linux y servicios populares (SSH, Apache2, etc.), ¡Lynis es tu aliado! Lynis no sólo te dice lo que va mal, sino que también te ofrece recomendaciones para indicarte la dirección correcta (y ahorrarte tiempo).



**Lynis** funciona con la mayoría de las distribuciones de Linux, incluyendo: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis está dirigido a usuarios de Linux / UNIX, pero también es compatible con **macOS**. Muy rápido de instalar, no hay gestión de dependencias a nivel de paquete.



Se utiliza para diversos fines:





- Auditorías de seguridad
- Pruebas de conformidad (PCI, HIPAA y SOX)
- Configuraciones de sistema más resistentes
- Detección de vulnerabilidades



La herramienta es ampliamente utilizada por un amplio abanico de usuarios, incluidos administradores de sistemas, auditores informáticos y pentesters. Para los análisis, la herramienta se basa en estándares como **CIS Benchmark, NIST, NSA, OpenSCAP** y en recomendaciones oficiales de **Debian, Gentoo, Red Hat**.



El proyecto está disponible en este Address en **Github** :





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Descargar Lynis de CISOFY](https://cisofy.com/lynis/#download)



En este tutorial paso a paso, voy a **utilizar un VPS ejecutando Debian 12** y me voy a centrar en la parte de SSH, ya que me gustaría comprobar su configuración y mejorarla.



## II. Descarga e instalación



Hay varias formas de descargar e instalar Lynis. Elige la que prefieras de la siguiente lista.



### A. Instalación desde los repositorios de Debian



Este modo de instalación le permite utilizar el comando **lynis** desde cualquier lugar del sistema, a diferencia de la instalación desde el código fuente, en la que necesita estar ubicado en el directorio.



Conéctese a su servidor a través de SSH e introduzca los siguientes comandos para instalar Lynis :



```
sudo apt-get update
sudo apt-get install lynis -y
```



Esto es lo que obtienes:



![Image](assets/fr/024.webp)



### B. Descargar desde el sitio web oficial



También puede descargarlo del sitio web de Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Esto es lo que obtienes:



![Image](assets/fr/032.webp)



A continuación, descomprimiremos el archivo utilizando el siguiente comando:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Esto es lo que obtienes:



![Image](assets/fr/020.webp)



Vamos a la carpeta **lynis**:



```
cd lynis
```



Podemos comprobar si hay actualizaciones con el siguiente comando:



```
./lynis update info
```



Esto es lo que obtienes:



![Image](assets/fr/023.webp)



### C. Descargar desde GitHub



Descargaremos **Lynis** desde el repositorio oficial de GitHub, utilizando el siguiente comando (*git* debe estar presente en tu máquina):



```
git clone https://github.com/CISOfy/lynis.git
```



Esto es lo que obtienes:



![Image](assets/fr/060.webp)



## III. Utilización de Lynis



Lynis está presente en nuestra máquina, ¡así que aprendamos a utilizarlo!



### A. Principales controles y opciones



Para visualizar los comandos disponibles, basta con introducir el siguiente comando:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```



Esto es lo que obtienes:



![Image](assets/fr/039.webp)



Y también tienes las siguientes opciones:



![Image](assets/fr/040.webp)



Para visualizar todos los comandos disponibles, introduzca el siguiente comando:



```
sudo lynis show
```



Esto es lo que obtienes:



![Image](assets/fr/022.webp)



Si desea visualizar todas las opciones, debe introducir :



```
sudo lynis show options
```



Esto es lo que obtienes:



![Image](assets/fr/021.webp)



En el resto de este artículo, aprenderemos a utilizar determinadas opciones.



### B. Realización de la auditoría del sistema



Vamos a pedir a **Lynis** que audite nuestro sistema, destacando lo que está correctamente configurado y lo que podría mejorarse. Para ello, introduzca el siguiente comando:



```
sudo lynis audit system
# ou
./lynis audit system
```



Por defecto, si no está conectado como root cuando ejecute este comando, la herramienta se ejecutará con los privilegios del usuario conectado en ese momento. Algunas pruebas no se ejecutarán en este contexto:



![Image](assets/fr/052.webp)



Estas son las pruebas que no se realizarán en este modo:



![Image](assets/fr/051.webp)



Una vez ejecutado el comando, se inicia el análisis. Espere un momento.



Al final de la auditoría, se obtiene esto (podemos ver que **Lynis** ha identificado correctamente el sistema **Debian 12** y utilizará el plugin **Debian** para el análisis):



![Image](assets/fr/017.webp)



A continuación, Lynis enumerará un conjunto de puntos correspondientes a todo lo que ha comprobado en nuestro sistema. Esto se organiza por categorías, como veremos. También vale la pena señalar que se utiliza un código de colores para resaltar las recomendaciones:





- Rojo** para Elements crítico o buenas prácticas no respetadas (falta un paquete, por ejemplo), es decir, su servidor no respeta este punto
- Amarillo** para sugerencias o cumplimiento parcial de la recomendación (digamos que es una ventaja cumplir un punto resaltado con este color (no prioritario))
- Green** para los puntos en los que la configuración de su servidor es conforme
- Blanco**, cuando es neutro



Aquí podemos ver que Lynis recomienda instalar **fail2ban**:



![Image](assets/fr/057.webp)



En la sección "**Boot y servicios**", vemos que la protección de servicios a través de *systemd* podría mejorarse. En el lado positivo, Grub2 está presente y no hay problemas con los permisos en :



![Image](assets/fr/029.webp)



Luego tienes las secciones "**Núcleo**" y "**Memoria y Procesos**":



![Image](assets/fr/037.webp)



A continuación, la sección "**Usuarios, grupos y autenticación**". La herramienta nos informa de una advertencia sobre los permisos del directorio "**/etc/sudoers.d**". De momento, no sabemos más, pero podremos ver cuál es la recomendación al final del análisis.



![Image](assets/fr/049.webp)



Esto es lo que puedes encontrar en las secciones "**Shells", "Files Systems" y "USB Devices "**. Entre otras cosas, podemos ver que hay sugerencias sobre puntos de montaje y que los dispositivos USB están actualmente permitidos en esta máquina.



![Image](assets/fr/048.webp)



A continuación, las secciones: "**Nombre de los servicios", "Puertos y paquetes", "Redes".** Aquí se indica que los paquetes que ya no se utilizan podrían ser purgados y que no existe ninguna utilidad capaz de gestionar las actualizaciones automáticas.



![Image](assets/fr/058.webp)



Podemos ver que hay un cortafuegos activado (y sí, ¡hay iptables!). Además, podemos ver que ha encontrado reglas no utilizadas y que hay instalado un servidor web Apache.



![Image](assets/fr/055.webp)



A continuación se analiza el propio servidor web, una vez identificado el servicio.



Podemos ver que ha encontrado ficheros de configuración de **Nginx**, y que para la parte SSL/TLS, los **cifradores** están configurados con el uso de un protocolo que sería inseguro. Por otro lado, según Lynis, la gestión de logs es correcta.



![Image](assets/fr/038.webp)



El servicio SSH está presente en mi servidor VPS. Su configuración es analizada por Lynis. Hay que decir que la seguridad SSH puede mejorarse fácilmente Volveremos sobre este tema en detalle una vez que hayamos obtenido las recomendaciones.



![Image](assets/fr/026.webp)



Aquí están las secciones **"Soporte SNMP", "Bases de datos", "PHP", "Soporte Squid", "Servicios LDAP", "Logging y ficheros "**.



Hay una sugerencia muy importante sobre la gestión de registros: se recomienda encarecidamente no almacenar los registros localmente en la máquina. Si la máquina fuera corrompida por un atacante, es probable que intentara borrar sus rastros... Así que hay que externalizar los logs.



![Image](assets/fr/050.webp)



Aquí, tenemos la auditoría de servicios vulnerables, gestión de cuentas, tareas programadas y sincronización NTP.Se indica que el nivel es bajo en el banner y la parte de identificación: esto es comprensible, si muestra la versión del sistema, da una indicación a un atacante potencial. Esta es la configuración por defecto.



Sería interesante activar **auditd** para tener logs en caso de **análisis forense**. También se comprueba el **NTP**, porque para buscar logs eficientemente, es preferible tener los sistemas a tiempo, lo que simplifica la búsqueda.



![Image](assets/fr/036.webp)



A continuación, Lynis examina el Elements criptográfico, la virtualización, los contenedores y los marcos de seguridad. Algunas secciones están vacías porque no hay correspondencia con la máquina analizada. Sin embargo, podemos ver que tengo dos certificados SSL caducados y que no he activado **SELinux**.



![Image](assets/fr/027.webp)



Aquí también hay margen de mejora: no hay antivirus ni antimalware, y tenemos sugerencias sobre los permisos de los archivos.



![Image](assets/fr/028.webp)



A continuación, Lynis se centra en hacer más estricta la configuración del kernel de Linux (incluidas las reglas para la pila IPv4), así como la gestión de los directorios "Home" de la máquina Linux.



![Image](assets/fr/035.webp)



Hemos llegado al final del análisis... Este último punto demuestra que tendríamos todas las de ganar si tuviéramos ClamaV en esta máquina.



![Image](assets/fr/030.webp)



## IV. Recomendaciones



Tras la auditoría, llega el momento de leer y analizar las recomendaciones. Aquí es donde obtenemos las recomendaciones y explicaciones de cada una de las pruebas realizadas por Lynis.



Por ejemplo, las recomendaciones SSH. **Para cada sugerencia, encontrarás el parámetro recomendado y un enlace que te explicará el punto de seguridad **Tú decides, dependiendo de tu contexto y uso.



Veamos algunos ejemplos de recomendaciones que se hacen eco directamente de los puntos destacados a lo largo de la auditoría...



### A. Ejemplos de recomendaciones





- Como hemos visto antes, NTP es importante para los registros de marcas de tiempo:



![Image](assets/fr/043.webp)





- Lynis también sugiere instalar el paquete **apt-listbugs** para obtener información sobre errores críticos durante la instalación de paquetes a través de **apt.**



![Image](assets/fr/041.webp)





- La herramienta sugiere que instalemos **needrestart para poder** ver qué procesos están utilizando una versión antigua de la librería y necesitan ser reiniciados.



![Image](assets/fr/054.webp)





- Esta sugerencia sugiere instalar **fail2ban** para bloquear automáticamente los hosts que no se autentiquen (especialmente por fuerza bruta).



![Image](assets/fr/044.webp)





- Para endurecer los servicios del sistema, recomienda que ejecutemos el comando blue para cada servicio de nuestra máquina.



![Image](assets/fr/056.webp)





- Sugiere fijar fechas de caducidad para todas las contraseñas de cuentas protegidas.



![Image](assets/fr/031.webp)





- Esta sugerencia sugiere establecer valores mínimos y máximos para la antigüedad de una contraseña. Entre otras cosas, esto garantizará que las contraseñas se cambien con regularidad.



![Image](assets/fr/042.webp)





- Recomendamos utilizar particiones separadas, para limitar el impacto de los problemas de espacio en disco en una partición.



![Image](assets/fr/047.webp)





- Esta recomendación sugiere desactivar el almacenamiento USB y firewire para evitar la fuga de datos



![Image](assets/fr/033.webp)





- Para cumplir esta recomendación, basta con instalar y configurar **unnatended-upgrade**, por ejemplo.



![Image](assets/fr/053.webp)



### B. Instalación de los paquetes recomendados



Para mejorar la configuración del sistema, vamos a instalar algunos paquetes en la máquina: algunos recomendados por Lynis, otros que yo personalmente recomiendo.



Tendrás una buena base sobre la que trabajar, siempre que dediques un poco de tiempo a configurarlos. Para ello, consulta el sitio de IT-Connect, otros artículos de la web y la documentación de las herramientas.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Información sobre los paquetes instalados :





- Clamav** es un antivirus.
- unattend-upgrades** le permitirá gestionar sus actualizaciones automáticamente e incluso reiniciar la máquina o purgar automáticamente paquetes antiguos, es totalmente configurable.
- rkhunter** es un anti-rootkit que escanea tu sistema de archivos.
- Fail2ban** se basará en tus archivos de registro según lo que le des a leer y funcionará con **iptables**, por ejemplo para banear direcciones IP que intenten "forzar" tu servidor en SSH.



### C. Recomendaciones para SSH



Echemos un vistazo a las recomendaciones SSH. Se enumeran a continuación. No te preocupes, vamos a explicar de inmediato cómo mejorar la configuración.



![Image](assets/fr/034.webp)



Echemos un vistazo a mi configuración actual de **SSH** en :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



La configuración sugerida a continuación aún puede optimizarse, pero le ofrece una buena base. *Ten en cuenta que he eliminado algunos comentarios para facilitar la lectura*.



Vamos a :





- Cambiar el puerto de conexión SSH (olvidar el 22 por defecto)
- Aumentar el nivel de verbosidad de los registros, de **INFO a VERBOSE**
- Establecer **LoginGraceTime** a **2 minutos**



Si no se introduce ninguna información de conexión en dos minutos, la conexión se desconecta.





- Activar **ModosEstrictos**



Especifica si "sshd" debe comprobar los modos y el propietario de los archivos del usuario, así como el directorio personal del usuario antes de validar una conexión. Esto es normalmente deseable, porque a veces los novatos accidentalmente dejan su directorio o archivos totalmente accesibles a todo el mundo. El valor por defecto es "sí".





- Establecer **MaxAuthtries** a 3



Representa el número de intentos de autenticación fallidos antes de que se cierre la comunicación.





- Establecer **MaxSessions** a 2



Representa el número máximo de sesiones simultáneas.





- Activar la autenticación de clave pública



```
PubkeyAuthentication yes
```





- Mantener la autenticación de contraseña :



```
PasswordAuthentication yes
```



Prohibir las contraseñas vacías y la autenticación **Kerberos**, así como la **autenticación root directa**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Asegúrese de que tiene "**PermitRootLogin no", si es igual a "sí", es "mal absoluto "**.





- Prohibir la redirección de conexiones TCP



```
AllowTcpForwarding no
```



Indica si se permiten las redirecciones TCP, con "sí" como valor predeterminado. Nota: desactivar las redirecciones TCP no mejora la seguridad si los usuarios tienen acceso a una shell, ya que pueden seguir configurando sus propias herramientas de redirección.





- Prohibir la redirección X11



```
X11Forwarding no
```



Indica si se aceptan las redirecciones X11, con "no" como configuración por defecto. Nota: aunque se deshabiliten las redirecciones X11, esto no aumenta la seguridad, ya que los usuarios pueden configurar sus propias redirecciones. La redirección X11 se desactiva automáticamente si se selecciona **UseLogin**.





- Establecer el tiempo de espera de comunicación entre el cliente y sshd



```
ClientAliveInterval  300
```



Define un tiempo de espera en segundos, tras el cual, si no se reciben datos del cliente, el servicio sshd envía un mensaje solicitando una respuesta del cliente. Por defecto, esta opción se establece en "0", lo que significa que estos mensajes no se envían al cliente. Sólo la versión 2 del protocolo SSH soporta esta opción.



```
ClientAliveCountMax 0
```



Según la [documentación (*página man*) para sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), esto es lo que significa esta opción: "Establece el número de mensajes hold (ver arriba) a ser enviados sin respuesta del cliente para **sshd**. Si este umbral es alcanzado mientras los mensajes de espera han sido enviados, **sshd** desconecta al cliente y termina la sesión. Es importante notar que estos mensajes de retención son muy diferentes de la opción **KeepAlive** (abajo). Los mensajes de retención de conexión son enviados a través del túnel encriptado, y por lo tanto no son falsificables. La retención de conexión a nivel TCP activada por **KeepAlive** es falsificable. El mecanismo de retención de conexión es interesante cuando el cliente o el servidor necesitan saber si la conexión está inactiva."





- Evite la divulgación de información desactivando **motd, banner, lastlog**



```
PrintMotd no
```



Especifica si sshd debe mostrar el contenido del fichero "/etc/motd" cuando un usuario se conecta en modo interactivo. En algunos sistemas, este contenido también puede ser mostrado por el shell, a través de /etc/profile o un archivo similar. El valor por defecto es "yes".



```
Banner none
```



Cabe señalar que, en algunas jurisdicciones, el envío de un mensaje antes de la autenticación puede ser un requisito previo para la protección legal. El contenido del archivo especificado se transmite al usuario remoto antes de que se autorice la conexión. Esta opción debe configurarse, ya que por defecto no se mostrará ningún mensaje.



En imágenes, esto da :



![Image](assets/fr/019.webp)



### D. Puntuación de auditoría



Por último, ¡no olvidemos comprobar la **puntuación de auditoría de Lynis**! Vemos que **mi puntuación de Hardening es 63** y que el archivo de informe se puede ver en "**/var/log/lynis-report.dat**". También está el archivo "**/var/log/lynis.log**".



**En otras palabras, ¡cuanto más alta sea la puntuación, mejor! Por tanto, debes trabajar en tu configuración para conseguir la máxima puntuación posible, permitiendo al mismo tiempo que tu máquina y los servicios alojados funcionen con normalidad (lo que significa realizar pruebas funcionales).



![Image](assets/fr/046.webp)



Echemos un vistazo a los resultados en mi segundo servidor, ¡donde pasé un poco más de tiempo endureciendo! Así que es normal que la puntuación sea más alta (**76**).



![Image](assets/fr/045.webp)



## V. Planificación automatizada Lynis



**Lynis** también ofrece la opción de ejecutar sus comprobaciones mediante una tarea programada. De hecho, existe la opción **"--cronjob "**, que ejecutará todas las pruebas de Lynis sin necesidad de validación o acción del usuario. A continuación, puede crear de forma muy sencilla un script que ejecutará **Lynis** y pondrá la salida en un archivo con fecha y hora con el nombre del servidor en cuestión. Aquí tienes un fichero de este tipo que puedes poner en la carpeta */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



La variable **"AUDITOR_NAME "** es simplemente una variable que estableceremos en la opción **"--auditor "** de **Lynis** para que este nombre aparezca en el informe:



![Image](assets/fr/059.webp)



También vamos a crear algunas variables contextuales que nos ayudarán a organizarnos mejor, como el nombre del host y la fecha para nombrar el informe y ponerle la marca de tiempo, y la ruta a la carpeta en la que queremos poner nuestros informes.



## VI. Conclusión



Lynis es una herramienta muy práctica que te ayudará a ahorrar tiempo y ser más eficiente cuando quieras saber más sobre el estado de la configuración de un servidor Linux, particularmente en términos de seguridad. Sin embargo, no olvides que cada modificación debe probarse antes de aplicarse en producción, teniendo en cuenta tu propio uso y contexto.



Probablemente no vas a aplicar la misma configuración para un VPS expuesto a la Red, donde sólo necesitas una conexión SSH (porque eres la única persona que se conecta), a diferencia de un **bastion** o **scheduler** que necesitarán multiplicar las conexiones **SSH.**



Una vez que tengas una configuración que te convenga en términos de hardening, es aconsejable adoptar una herramienta de automatización para no tener que rehacer las tareas manualmente, ya que esto llevaría mucho tiempo y daría lugar a errores. Por ejemplo, puede utilizar Puppet, Chef, Ansible, etc...**



No olvides comunicarte con tus equipos antes de la implantación: tienes que hacerles entender por qué haces estos cambios, no sólo decirles que los haces. Al final, el objetivo será transmitir buenas prácticas, y así aumentarán tus posibilidades de éxito.



Por último, también puedes comparar **Lynis** con otras herramientas, de las que hay varias. Si quieres pasar a una gestión centralizada sin dejar de ser de código abierto, te recomiendo la herramienta [Wazuh] (https://wazuh.com/).



**Este tutorial ha terminado, ¡diviértete con Lynis!