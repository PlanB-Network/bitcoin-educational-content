---
name: Graylog
description: Centralice y analice sus registros fácilmente
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian BURNEL publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## Implantación de Graylog en Debian 12



### I. Presentación



Graylog es una solución "log sink" de código abierto diseñada para centralizar, almacenar y analizar logs de tus máquinas y dispositivos de red en tiempo real. En este tutorial, aprenderemos a instalar la versión gratuita de Graylog en una máquina Debian 12



Dentro de un sistema de información, cada **servidor**, ya sea **Linux** o **Windows**, y cada **dispositivo de red** (switch, router, firewall, etc...) **genera sus propios logs**, almacenados localmente. Con los registros almacenados localmente en cada máquina, el análisis de eventos y la correlación es muy difícil ... Aquí es donde entra **Graylog**. Actuará como un **sumidero de logs**, lo que significa que **todas tus máquinas le enviarán sus logs** (vía syslog, por ejemplo). Graylog **almacenará e indexará estos registros**, permitiéndote realizar búsquedas globales y crear alertas.



Graylog es una herramienta de análisis y supervisión que facilita la identificación de comportamientos sospechosos y diversos problemas (estabilidad, rendimiento, etc.).




![Image](assets/fr/034.webp)



**Nota: la versión gratuita, **Graylog Open**, no es un SIEM como lo es Wazuh, especialmente porque carece de funciones reales de detección de intrusos.



### II. Requisitos previos



El **stack Graylog** se basa en **varios componentes** que tendremos que instalar y configurar. Aquí instalaremos todos los componentes en el mismo servidor, pero es posible crear clusters basados en varios nodos y distribuir los roles entre varios servidores. Para los propósitos de este tutorial, instalaremos **Graylog 6.1**, la versión más reciente hasta la fecha.





- MongoDB 7**, la versión actual recomendada para Graylog (mínimo 5.0.7, máximo 7.x)
- OpenSearch**, un Fork de código abierto de Elasticsearch creado por Amazon (mínimo 1.1.x, máximo 2.15.x)
- OpenJDK 17**



El servidor **Graylog** se ejecuta en **Debian 12**, pero la instalación es posible en otras distribuciones, incluso a través de Docker. La máquina virtual está equipada con **8 GB de RAM** y **256 GB de espacio en disco**, con el fin de tener suficientes recursos para todos los componentes (de lo contrario esto puede tener un impacto significativo en el rendimiento). No obstante, esto es orientativo, ya que **el dimensionamiento de la arquitectura Graylog depende de la cantidad de información a procesar**. Graylog puede procesar 30 MB o 300 MB de datos al día, así como 300 GB de datos al día... Se trata de una solución **escalable** capaz de gestionar **terabytes de registros** (véase [esta página](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Fuente: Graylog



Antes de iniciar la configuración, asigna una IP estática Address a la máquina Graylog e instala las últimas actualizaciones. Asegúrese de establecer la zona horaria de la máquina local y definir un servidor NTP para la sincronización de fecha y hora. Aquí está el comando a ejecutar:



```
sudo timedatectl set-timezone Europe/Paris
```



**Nota: **La instalación de OpenSearch es opcional** si utiliza **Graylog Data Node** en su lugar.



### III Instalación paso a paso de Graylog



Empecemos por actualizar la caché de paquetes e instalar las herramientas que necesitamos para lo que está por venir.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Instalación de MongoDB



Una vez hecho esto, empezaremos a instalar MongoDB. Descarga la clave GPG correspondiente al repositorio de MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



A continuación, añada el repositorio de MongoDB 6 a la máquina Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



A continuación, actualizaremos la caché de paquetes e intentaremos instalar MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB no se puede instalar porque falta una dependencia: **libssl1.1**. Tendremos que instalar este paquete manualmente antes de poder continuar, porque Debian 12 no lo tiene en sus repositorios.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Vamos a descargar el paquete DEB llamado "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (última versión) con el comando **wget**, y luego instalarlo con el comando **dpkg**. Esto produce los siguientes dos comandos:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Reinicie la instalación de MongoDB:



```
sudo apt-get install -y mongodb-org
```



A continuación, reinicie el servicio MongoDB y habilítelo para que se inicie automáticamente cuando se inicie el servidor Debian.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Con MongoDB instalado, podemos pasar a instalar el siguiente componente.



#### B. Instalación de OpenSearch



Pasemos a instalar OpenSearch en el servidor. El siguiente comando añade la clave de firma para los paquetes OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



A continuación, añade el repositorio OpenSearch para que podamos descargar el paquete con **apt** después:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Actualice su caché de paquetes:



```
sudo apt-get update
```



Luego **instale OpenSearch**, teniendo cuidado de **definir la contraseña por defecto para la cuenta Admin** de su instancia. Aquí, la contraseña es "**IT-Connect2024!**", pero sustituya este valor por una contraseña segura. **Evite contraseñas débiles** como "**P@ssword123**" y utilice al menos **8 caracteres** con al menos un carácter de cada tipo (minúscula, mayúscula, número y carácter especial), de lo contrario se producirá un error al final de la instalación. **Esto es un prerrequisito desde OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Tenga paciencia durante la instalación...



Cuando hayas terminado, tómate un momento para realizar la configuración mínima. Abra el archivo de configuración en formato YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Cuando el archivo esté abierto, configure las siguientes opciones:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Esta configuración de OpenSearch está diseñada para configurar un único nodo. Aquí hay algunas explicaciones de los diferentes parámetros que utilizamos:





- cluster.name: graylog**: este parámetro nombra el cluster OpenSearch con el nombre "**graylog**".
- node.name: ${HOSTNAME}**: el nombre del nodo se establece dinámicamente para que coincida con el de la máquina Linux local. Aunque sólo tengamos un nodo, es importante nombrarlo correctamente.
- ruta.datos: /var/lib/opensearch**: esta ruta especifica dónde almacena OpenSearch sus datos en la máquina local, en este caso en "**/var/lib/opensearch**".
- ruta.logs: /var/log/opensearch**: esta ruta define dónde se almacenan los archivos de registro de OpenSearch, aquí en "**/var/log/opensearch**".
- discovery.type: single-node**: este parámetro configura OpenSearch para trabajar con un único nodo, de ahí la elección de la opción "**single-node**".
- network.host: 127.0.0.1**: esta configuración asegura que OpenSearch sólo escucha en su bucle local Interface, lo cual es suficiente ya que está en el mismo servidor que Graylog.
- action.auto_create_index: false**: al desactivar la creación automática de índices, OpenSearch no creará automáticamente un índice cuando se envíe un documento sin un índice existente.
- plugins.security.disabled: true**: esta opción desactiva el plugin de seguridad OpenSearch, lo que significa que no habrá autenticación, gestión de acceso o encriptación de comunicaciones. Esta configuración ahorra tiempo al configurar Graylog, pero debe evitarse en producción (véase [esta página](https://opensearch.org/docs/1.0/security-plugin/index/)).



Algunas opciones ya están presentes, por lo que sólo tiene que eliminar el "#" para activarlas y, a continuación, indicar su valor. Si no encuentra una opción, puede declararla directamente al final del archivo.



![Image](assets/fr/023.webp)



Guarde y cierre este archivo.



#### C. Configurar Java (JVM)



Es necesario configurar la máquina virtual Java utilizada por OpenSearch para ajustar la cantidad de memoria que puede utilizar este servicio. Edite el siguiente archivo de configuración:



```
sudo nano /etc/opensearch/jvm.options
```



Con la configuración desplegada aquí, **OpenSearch comenzará con 4 GB de memoria asignada y podrá crecer hasta 4 GB**, por lo que no habrá variación de memoria durante el funcionamiento. Aquí, la configuración tiene en cuenta que la máquina virtual tiene un total de **8 GB de RAM**. Ambos parámetros deben tener el mismo valor. Esto significa sustituir las líneas:



```
-Xms1g
-Xmx1g
```



Con estas líneas:



```
-Xms4g
-Xmx4g
```



He aquí una imagen de la modificación a realizar:



![Image](assets/fr/022.webp)



Cierre este archivo después de guardarlo.



Además, tenemos que comprobar la configuración del parámetro "**max_map_count**" en el kernel de Linux. Define el límite de áreas de memoria mapeadas por proceso, con el fin de satisfacer las necesidades de nuestra aplicación. **OpenSearch**, al igual que Elasticsearch**, recomienda establecer este valor en "262144" para evitar errores de gestión de memoria.



En principio, en una máquina Debian 12 recién instalada, el valor ya es correcto. Pero vamos a comprobarlo. Ejecute este comando:



```
cat /proc/sys/vm/max_map_count
```



Si obtiene un valor distinto de "**262144**", ejecute el siguiente comando; de lo contrario, no es necesario.



```
sudo sysctl -w vm.max_map_count=262144
```



Por último, active el inicio automático de OpenSearch y ejecute el servicio asociado.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Si muestra el estado de su sistema, debería ver un proceso Java con 4 GB de RAM.



```
top
```



![Image](assets/fr/029.webp)



Siguiente paso: ¡la tan esperada instalación de Graylog!



#### D. Instalación de Graylog



Para **instalar Graylog 6.1** en su última versión, ejecuta los 4 comandos siguientes para **descargar e instalar Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Una vez hecho esto, tenemos que hacer algunos cambios en la configuración de Graylog antes de intentar lanzarlo.



Empecemos por configurar estas dos opciones:





- password_secret**: este parámetro se utiliza para definir una clave utilizada por Graylog para asegurar el almacenamiento de las contraseñas de los usuarios (en el espíritu de una clave de salting). Esta clave debe ser **única** y **aleatoria**.
- root_password_sha2**: este parámetro corresponde a la contraseña de administrador por defecto en Graylog. Se almacena como Hash SHA-256.



Empezaremos generando una clave de 96 caracteres para el parámetro **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Copie el valor devuelto y abra el archivo de configuración de Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Pega la clave en el parámetro **password_secret**, así:



![Image](assets/fr/027.webp)



Guarde y cierre el archivo.



A continuación, debe establecer la contraseña de la cuenta "**admin**" creada por defecto. En el archivo de configuración debe almacenarse el Hash de la contraseña, lo que significa que debe calcularse. El ejemplo siguiente da el Hash de la contraseña "**LogsWells@**": adapte el valor a su contraseña.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Copie el valor obtenido como salida (sin el guión al final de la línea).



Vuelva a abrir el archivo de configuración de Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Pega el valor en la opción **root_password_sha2** así:



![Image](assets/fr/026.webp)



Mientras estás en el archivo de configuración, establece la opción "**http_bind_address**". Especifica "**0.0.0.0:9000**" para que se pueda acceder a la web Interface de Graylog en el puerto **9000**, a través de cualquier servidor IP Address.



![Image](assets/fr/024.webp)



A continuación, establece la opción "**elasticsearch_hosts**" en `http://127.0.0.1:9200` para declarar nuestra instancia local de OpenSearch. Esto es necesario, ya que no estamos utilizando un **Graylog Data Node**. Y sin esta opción, no será posible ir más allá...



![Image](assets/fr/025.webp)



Guarde y cierre el archivo.



Este comando activa Graylog para que se inicie automáticamente en el siguiente arranque, y lanza inmediatamente el servidor Graylog.



```
sudo systemctl enable --now graylog-server
```



Una vez hecho esto, intenta conectarte a Graylog desde un navegador. Introduzca la IP Address (o nombre) del servidor y el puerto 9000.



**Para su información:**



No hace mucho tiempo, cuando te conectabas por primera vez a Graylog, aparecía una ventana de autenticación similar a la siguiente. Tenías que introducir tu nombre de usuario "**admin**" y tu contraseña. Y entonces te llevabas la desagradable sorpresa de que la conexión no funcionaba.



![Image](assets/fr/031.webp)



Fue necesario volver a la línea de comandos del servidor Graylog y consultar los registros. Entonces pudimos ver que **para la primera conexión**, es necesario **utilizar una contraseña temporal**, especificada en los logs.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



A continuación, había que volver a intentar una conexión con el usuario "**admin**" y la contraseña temporal, ¡y esto permitía iniciar la sesión!



**Este ya no es el caso. Todo lo que tienes que hacer es iniciar sesión con tu cuenta de administrador y la contraseña configurada en la línea de comandos



![Image](assets/fr/033.webp)



**¡Bienvenidos al Interface de Graylog!



![Image](assets/fr/019.webp)



#### E. Graylog: crear una nueva cuenta de administrador



En lugar de utilizar la cuenta de administrador creada de forma nativa por Graylog, puedes crear tu propia cuenta de administrador personal. Haz clic en el menú "**Sistema**", luego en "**Usuarios y equipos**" para hacer clic en el botón "**Crear usuario**". A continuación, rellena el formulario y asigna el rol de administrador a tu cuenta.



![Image](assets/fr/020.webp)



Una cuenta personalizada puede contener información adicional, como nombre y apellidos y correo electrónico Address, a diferencia de una cuenta de administrador nativa. Además, esto garantiza una mejor trazabilidad cuando cada persona trabaja con una cuenta personalizada.



## Enviar logs a Graylog con rsyslog



### I. Presentación



En esta segunda parte, aprenderemos a configurar una máquina Linux para que envíe sus registros a un servidor Graylog. Para ello, instalaremos y configuraremos Rsyslog en el sistema.



### II. Configuración de Graylog para recibir logs de Linux



Empezaremos por configurar Graylog. Hay que seguir tres pasos:





- La creación de un **Input** para crear un punto de entrada que permita a las máquinas Linux **enviar logs Syslog vía UDP**.
- La creación de un nuevo **índice** para almacenar e **indexar todos los registros de Linux**.
- Creación de un **Stream** para **enrutar** los logs recibidos por Graylog al nuevo Índice Linux.



#### A. Crear una entrada para Syslog



Conéctese a Graylog Interface, haga clic en "**Sistema**" en el menú y luego en "**Entradas**". En la lista desplegable, seleccione "**Syslog UDP**" y haga clic en el botón "**Lanzar nueva entrada**". También es posible crear una entrada Syslog TCP, pero esto requiere el uso de un certificado TLS: una ventaja para la seguridad, pero no se trata en este artículo.



![Image](assets/fr/001.webp)



Aparecerá un asistente en la pantalla. Empieza dando un nombre a esta Entrada, por ejemplo "**Graylog_UDP_Rsyslog_Linux**" y elige un puerto. Por defecto, el puerto es "**514**", pero puedes personalizarlo. Aquí, el puerto "**12514**" está seleccionado.



![Image](assets/fr/016.webp)



También puede marcar la opción "**Almacenar mensaje completo**" para almacenar el mensaje de registro completo en Graylog. Haz clic en "**Lanzar entrada**".



![Image](assets/fr/017.webp)



La nueva Entrada ha sido creada y ya está activa. Graylog ya puede recibir registros Syslog en el puerto 12514/UDP, pero aún no hemos terminado de configurar la aplicación.



![Image](assets/fr/018.webp)


**Nota: una sola Entrada puede utilizarse para almacenar registros de varias máquinas Linux.



#### B. Crear un nuevo índice Linux



Necesitamos crear un Índice en Graylog para almacenar los logs de las máquinas Linux. Un **índice** en Graylog es una estructura de almacenamiento que contiene los registros recibidos, es decir, los mensajes recibidos. Graylog utiliza OpenSearch como motor de almacenamiento, y los mensajes se indexan para permitir búsquedas rápidas y eficientes.



Desde Graylog, haz clic en "**Sistema**" en el menú, y luego en "**Índices**". En la nueva página que aparece, haz clic en "**Crear conjunto de índices**".



![Image](assets/fr/005.webp)



Nombra este índice, por ejemplo "**Índice Linux**", añade una descripción y un prefijo, antes de confirmar. Aquí, vamos a **almacenar todos los logs de Linux en este índice**. También es posible crear índices específicos para almacenar sólo determinados registros (sólo registros [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), registros de servicios web, etc.).



![Image](assets/fr/006.webp)



Ahora tenemos que crear un nuevo flujo para dirigir los mensajes a este índice.



#### C. Crear una corriente



Para crear un nuevo stream, haz clic en "**Streams**" en el menú principal de Graylog. A continuación, haz clic en el botón "**Crear flujo**" de la derecha. En la ventana que aparece, asigne un nombre al flujo, por ejemplo "**Corriente Linux**" y elija el índice "**Índice Linux**" para el campo "**Conjunto de índices**". Confirme su elección.



**Nota: los mensajes correspondientes a este flujo también se incluirán en el "**Corriente por defecto**", a menos que marque la opción "**Eliminar coincidencias de 'Corriente por defecto'**".



![Image](assets/fr/002.webp)



A continuación, en la configuración de Steam, haga clic en el botón "**Añadir regla de flujo**" para añadir una nueva regla de enrutamiento de mensajes. Si no encuentra esta ventana, haga clic en "**Streams**" en el menú, luego en la línea correspondiente a su stream, haga clic en "**More**" y luego en "**Manage Rules**".



Elija el tipo "**match input**" y seleccione la entrada **Rsyslog en UDP** creada anteriormente. Confirme con el botón "**Crear regla**". Todos los mensajes a nuestra nueva Entrada serán ahora enviados al Índice para Linux.



![Image](assets/fr/003.webp)



Su nuevo Stream debería aparecer en la lista y debería estar en estado "**Running**". El mensaje de ancho de banda muestra "**0 msg/s**", ya que actualmente no estamos enviando ningún registro a la entrada Rsyslog UDP. Para ver los registros de un flujo, simplemente haga clic en su nombre.



![Image](assets/fr/004.webp)



**Todo está listo en el lado Graylog**. El siguiente paso es configurar la máquina Linux.



### III. Instalación y configuración de Rsyslog en Linux



Inicie sesión en la máquina Linux, ya sea de forma local o remota, y utilice una cuenta de usuario con permisos para elevar sus privilegios (a través de sudo). De lo contrario, utilice directamente la cuenta "root".



#### A. Instalación del paquete Rsyslog



Empiece actualizando la caché de paquetes e instalando el paquete llamado "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



A continuación, compruebe el estado del servicio. En la mayoría de los casos, ya está en marcha.



```
sudo systemctl status rsyslog
```



#### B. Configuración de Rsyslog



Rsyslog tiene un archivo de configuración principal ubicado aquí:



```
/etc/rsyslog.conf
```



Además, el directorio "**/etc/rsyslog.d/**" se utiliza para almacenar archivos de configuración adicionales para Rsyslog. En el archivo de configuración principal, hay una directiva Include para importar todos los archivos "**.conf**" ubicados en este directorio. Esto permite disponer de ficheros adicionales para configurar Rsyslog sin modificar el fichero principal.



En este directorio, debe utilizar números para definir el orden de carga, ya que los ficheros se cargan por orden alfabético. Añadir un prefijo numérico permite gestionar la prioridad entre varios ficheros de configuración. Aquí, sólo tenemos un archivo adicional, por lo que no es un problema.



En este directorio, crearemos un archivo llamado "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



En este archivo, inserte esta línea:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



He aquí cómo interpretar esta línea:





- `*.*`: significa enviar todos los registros Syslog de la máquina Linux a Graylog.
- `@`: indica que el transporte se realiza en UDP. Debe especificar "**@@**" para cambiar a TCP.
- `192.168.10.220:12514`: indica el Address del servidor Graylog, y el puerto por el que se envían los logs (correspondiente a la Entrada).
- `RSYSLOG_SyslogProtocol23Format`: corresponde al formato de los mensajes a enviar a Graylog.



Cuando haya terminado, guarde el archivo y reinicie Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Tras esta acción, los primeros mensajes deberían llegar a tu servidor Graylog



### IV. Visualización de los registros de Linux en Graylog



Desde Graylog, puedes hacer clic en "**Streams**" y seleccionar tu nuevo stream para ver los mensajes relacionados. También puedes hacer clic en "**Buscar**", seleccionar tu Steam e iniciar una búsqueda.



Estas son algunas de las principales características de la Interface:



**1** - Seleccione el periodo durante el cual se mostrarán los mensajes. Por defecto, se muestran los mensajes de los últimos 5 minutos.



**2** - Seleccione la(s) secuencia(s) que desea visualizar.



**3** - Activa la actualización automática de la lista de mensajes (cada 5 segundos, por ejemplo). De lo contrario, será estática y tendrás que actualizarla manualmente.



**4** - Haga clic en la lupa para lanzar la búsqueda después de modificar el periodo, el flujo o el filtro.



**5** - Barra de entrada para especificar los filtros de búsqueda. Aquí, especifico "**source:srv\-docker**" para mostrar sólo los registros de la nueva máquina en la que acabo de configurar Rsyslog.



Los logs son enviados por la máquina Linux:



![Image](assets/fr/015.webp)



### V. Identificación de un fallo de conexión SSH



La fuerza de Graylog reside en su capacidad para indexar logs y permitir realizar búsquedas según diversos criterios: máquina de origen, Timestamp, contenido de los mensajes, etc... Podríamos estar buscando identificar conexiones SSH fallidas.



Desde una máquina remota (el servidor Graylog, por ejemplo), intente conectarse a su servidor Linux en el que acaba de configurar Rsyslog. Por ejemplo:



```
ssh [email protected]
```



A continuación, introduzca deliberadamente un **nombre de usuario** y **contraseña** incorrectos, con el fin de **generate errores de conexión**. En el archivo "**/var/log/auth.log**", esto generate mensajes de registro similares a los siguientes:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Deberías encontrar estos mensajes en Graylog.



En Graylog, utilice el siguiente filtro de búsqueda para mostrar sólo los mensajes coincidentes:



```
message:Failed password AND application_name:sshd
```



Si dispone de varios servidores y desea analizar los registros de un servidor concreto, especifique su nombre además de:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



He aquí un resumen del resultado en una máquina en la que generé varios errores de conexión, a diferentes horas del día:



![Image](assets/fr/009.webp)



Los intentos de conexión fallidos se realizan desde la máquina con IP Address "**192.168.10.199**". Si quieres saber más sobre la actividad de este host, puedes **buscar esta IP Address**. Graylog mostrará todos los logs donde se haga referencia a esta IP Address, en todos los hosts (para los que esté configurado el envío de logs).



En este caso, el filtro a utilizar puede ser:



```
message:"192.168.10.199"
```



Obtenemos resultados adicionales (no es sorprendente, ya que no filtramos en la aplicación SSH):



![Image](assets/fr/008.webp)



### VI. Conclusión



Siguiendo este tutorial, deberías ser capaz de configurar una máquina Linux para que envíe sus logs a un servidor Graylog. De esta forma, ¡podrás centralizar los logs de tus máquinas Linux en tu sumidero de logs!



Para ir aún más lejos, considere la posibilidad de crear cuadros de mando y alertas para recibir notificaciones cuando se detecte una anomalía.



![Image](assets/fr/007.webp)