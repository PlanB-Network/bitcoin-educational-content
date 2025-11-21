---
name: Dojo
description: Un nodo Bitcoin de código abierto para la privacidad y la autonomía
---

![cover](assets/cover.webp)



*Este tutorial está basado en [la documentación oficial de Ashigaru](https://ashigaru.rs/docs/), que he retomado y ampliado. He reescrito todas las secciones para mejorar la claridad, he añadido explicaciones más detalladas, así como ilustraciones para principiantes, para que la instalación y el uso sean más fáciles de entender.*



---

Dojo es un programa de código abierto diseñado para actuar como servidor backend para ciertos monederos Bitcoin orientados a la privacidad, basados en un nodo Bitcoin core. Históricamente, fue desarrollado para trabajar con Samourai Wallet, una Wallet móvil que ofrecía características avanzadas de privacidad como Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet se ha cerrado tras la detención de sus desarrolladores, pero su sucesor en la comunidad, **Ashigaru Wallet**, ha tomado el relevo y sigue apoyándose en Dojo para ofrecer una experiencia completa a los usuarios que deseen mantener el control de sus datos cuando utilicen Bitcoin.



![Image](assets/fr/01.webp)



En la práctica, Dojo actúa como pasarela entre tu Wallet y la red Bitcoin. Sin Dojo, una Wallet móvil ligera tendría que consultar servidores de terceros para obtener el estado de sus UTXO y su historial, o para difundir sus transacciones. Esto implica dependencia y filtración de datos sensibles a un servidor de terceros (direcciones utilizadas, importes, frecuencia de pago, etc.). Con Dojo, usted mismo aloja este servidor, directamente conectado a su propio nodo Bitcoin. De este modo, todas sus solicitudes de cartera pasan por una infraestructura que usted controla, sin intermediarios, reforzando su confidencialidad y soberanía.



## Requisitos para crear un Dojo



Configurar un servidor Dojo no requiere una máquina ultrapotente. Cualquiera con un ordenador básico, una conexión a Internet estable y la capacidad de dejarlo encendido continuamente (24/7) puede montar un Dojo que funcione.



### Elija su tipo de máquina



Puede utilizar :




- un ordenador portátil ;
- un ordenador de sobremesa ;
- un mini-PC (por ejemplo, Intel NUC, Lenovo Thincentre Tiny...).



Cada opción tiene sus ventajas e inconvenientes:




- Precio: un mini PC o sobremesa reacondicionado suele ser más barato que un portátil nuevo.
- Ocupa menos espacio: un mini PC ocupa menos espacio.
- Power Supply: un portátil tiene la ventaja de contar con una batería, lo que significa que no se apagará en caso de corte del suministro eléctrico, a diferencia de un mini PC.
- Capacidad de actualización: por lo general, los barbones permiten añadir memoria o sustituir fácilmente un disco Hard.



Para más información sobre cómo elegir tu equipo, te recomiendo que sigas este curso:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Equipamiento recomendado



No es necesario comprar una máquina nueva. Un ordenador reacondicionado con las especificaciones que se indican a continuación ofrecerá un rendimiento muy superior al de la electrónica de placa única (como la Raspberry Pi).



**Especificaciones mínimas:**




- Arquitectura X86-64 (procesador de 64 bits).
- procesador de doble núcleo a 2 GHz o superior.
- 8 GB de RAM como mínimo.
- sSD NVMe de 2 TB o más (para almacenar Blockchain de Bitcoin y los índices necesarios).



**Sistema operativo recomendado: **




- Una distribución basada en Debian, como Ubuntu 24.04 LTS.



**Equipo recomendado:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- etc.



Es perfectamente posible ejecutar un servidor Dojo en otras configuraciones de hardware. Sin embargo, para obtener el mejor rendimiento y limitar los problemas, te aconsejamos que sigas las recomendaciones anteriores.



En este tutorial, utilizaré un viejo ThinkCentre Tiny con un procesador Intel Pentium Dual-Core G4400T, 8 GB de RAM y una unidad SSD de 2 TB.



## 1 - Instalación de Ubuntu



*Si desea instalar Dojo en un dispositivo que ya está configurado, puede omitir este paso y proceder directamente al paso 2.*



Una vez preparado el hardware elegido, es hora de instalar un sistema operativo. Puedes utilizar prácticamente cualquier distribución Debian, pero te recomiendo que optes por una versión LTS de Ubuntu, ya que se adapta perfectamente a nuestros propósitos. Estos son los pasos a seguir:



### 1.1. crear una memoria USB de arranque



Desde un ordenador que ya funcione (su máquina habitual), descargue la imagen ISO de Ubuntu LTS [desde el sitio oficial](https://ubuntu.com/download/desktop) (`24.04` en el momento de escribir estas líneas, pero tome la más reciente si hay otra disponible).



![Image](assets/fr/02.webp)



Inserta una llave USB de al menos 8 GB en este ordenador y, a continuación, crea una llave de arranque utilizando un software como [Balena Etcher](https://etcher.balena.io/). Selecciona la imagen ISO de Ubuntu que acabas de descargar, elige la llave USB como dispositivo de destino e inicia el proceso de creación (ten paciencia, puede tardar varios minutos).



![Image](assets/fr/03.webp)



Inserte la llave USB de arranque en el ordenador apagado (aquel en el que desea ejecutar Dojo). Arranque el ordenador e inmediatamente pulse **F12** o **F10** en su teclado (dependiendo del modelo) para acceder al menú de arranque. A continuación, elige tu llave USB como dispositivo prioritario en el orden de arranque del ordenador.



![Image](assets/fr/04.webp)



### 1.2. instalar el sistema operativo



Aparecerá la pantalla de inicio de Ubuntu. Seleccione "Probar o instalar Ubuntu*".



![Image](assets/fr/05.webp)



A continuación, sigue el proceso clásico de instalación de Ubuntu:




- Selecciona el idioma.
- Selecciona el tipo de teclado.
- Si estás conectado mediante un cable RJ45, no es necesario configurar el Wi-Fi.
- Haz clic en "*Instalar Ubuntu*" y marca la opción para instalar software de terceros (controladores Wi-Fi, códecs multimedia, etc.).
- Cuando el asistente pregunte por el tipo de instalación, seleccione "*Borrar disco e instalar Ubuntu*". **Atención**: esta operación borrará completamente el contenido del disco. Compruebe cuidadosamente que el disco que ha elegido corresponde al SSD NVMe destinado a Dojo.
- Crea un nombre de usuario sencillo (por ejemplo, "*loic*").
- Asigne un nombre a la máquina (por ejemplo, "*dojo-node*").
- Establezca una contraseña segura y guárdela.
- Active la opción "*Solicitar mi contraseña para iniciar sesión*" para reforzar la seguridad.
- Indique su zona horaria y haga clic en "*Instalar*".
- Espere a que finalice la instalación. Una vez completada, el sistema se reiniciará automáticamente.
- Retire la llave de instalación USB al reiniciar el ordenador.



Para más detalles sobre el proceso de instalación de Ubuntu, consulte nuestro tutorial dedicado :



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. actualización del sistema



Tras el primer arranque, abra un terminal utilizando la combinación de teclas ***Ctrl + Alt + T*** y ejecute los siguientes comandos para actualizar el sistema:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Instalación de edificios anexos



Para que Dojo funcione correctamente, ciertos bricks de software deben estar presentes en tu sistema. Estos se utilizan para gestionar los repositorios de software, la comunicación, la descompresión de archivos y la ejecución de Dojo dentro de contenedores Docker. Todas estas operaciones se realizan en el terminal.



### 2.1. Preparación



El siguiente comando le devuelve a su carpeta personal. Esta es una buena práctica antes de ejecutar una serie de instalaciones.



```bash
cd ~/
```



Antes de instalar cualquier software, asegúrate de que la base de datos de software disponible en tu máquina está actualizada. Así evitarás instalar versiones obsoletas.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. instalar utilidades



Hay que añadir varias herramientas al sistema:




- `apt-transport-https`: permite descargar paquetes de forma segura a través de HTTPS
- `ca-certificates`: gestiona los certificados necesarios para las conexiones cifradas
- `curl`: para recuperar archivos de Internet
- `gnupg-agent`: para la gestión de claves GPG
- software-properties-common`: proporciona utilidades para manipular repositorios APT
- `unzip`: descomprime archivos en formato ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Durante la instalación, el sistema puede pedirle confirmación. Pulse la tecla "*y*" y, a continuación, pulse "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. instalar Torsocks



Torsocks permite ejecutar ciertos comandos a través de la red Tor, mejorando la confidencialidad de las comunicaciones.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. instalar Docker y Docker Compose



Dojo se ejecuta dentro de contenedores Docker. Esto significa que cada servicio está aislado en un entorno independiente, lo que simplifica el mantenimiento y la seguridad. Para ello, es necesario instalar Docker y la herramienta Docker Compose, que permite gestionar varios contenedores al mismo tiempo.



#### Añadir clave de firma Docker



Docker proporciona su propia clave de firma digital. Al añadirla se verifica la autenticidad de los paquetes descargados.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Repositorio Docker oficial añadido



A continuación, debes indicar al sistema dónde encontrar los paquetes oficiales de Docker. Este comando añade un nuevo repositorio a la configuración del gestor de paquetes.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Instalación de Docker y Docker Compose



Ahora se pueden instalar los principales componentes de Docker.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Autorización del usuario



Por defecto, sólo los comandos ejecutados con derechos de administrador pueden lanzar Docker. Para mayor comodidad, le recomiendo que añada su usuario actual al grupo "*docker*". Esto le permite utilizar Docker sin tener que escribir `sudo` cada vez.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Creación de un usuario único (opcional)



Si quieres mejorar la seguridad de tu sistema, te recomiendo que crees un usuario separado exclusivamente para ejecutar Dojo. Esta separación limita los riesgos: si ocurre un problema de seguridad en Dojo, no comprometerá directamente tu cuenta principal.



### 3.1. creación de cuentas de usuario



El siguiente comando crea un nuevo usuario llamado "*dojo*". Este usuario tendrá un directorio home `/home/dojo` y acceso a la terminal bash. También será añadido al grupo sudo para permitir la ejecución de comandos de administrador.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Establecer una contraseña



Es importante asignar una contraseña fuerte a esta cuenta. Lo ideal es utilizar un gestor de contraseñas como Bitwarden para generate una combinación larga y Hard de adivinar.



```bash
sudo passwd dojo
```



El sistema le pedirá que introduzca la contraseña elegida y que la confirme una segunda vez.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autorizar al usuario a utilizar Docker



Para permitir al usuario "*dojo*" lanzar los contenedores necesarios para ejecutar Dojo, debe ser añadido al grupo Docker. Esto evita tener que preceder cada comando con `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Reinicio del sistema



Para que los cambios de grupo surtan efecto, es necesario reiniciar la máquina.



```bash
sudo reboot
```



### 3.5. Iniciar sesión con el nuevo usuario



Cuando el sistema se reinicie, inicie sesión con el nombre de usuario ***dojo*** y la contraseña que definió anteriormente. Todos los pasos posteriores deberán realizarse desde esta cuenta dedicada.



## 4. Descargar y comprobar Dojo



Antes de instalar Dojo, es esencial asegurarse de que los archivos proceden del desarrollador oficial y que no han sido modificados. Este paso se basa en el uso de PGP y hashes para verificar la autenticidad e integridad de los archivos.



### 4.1. importar la clave PGP del desarrollador



Descargue la clave pública del desarrollador a través de Tor e impórtela en su llavero local. Esta clave se utilizará para verificar las firmas asociadas a los archivos Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. descargar la última versión de Dojo



Recupera el archivo comprimido que contiene el código fuente de Dojo. En este ejemplo, la versión más reciente es `1.27.0`: modifica el comando según [la última versión aquí en el repositorio oficial de GitHub](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Descargar huellas dactilares y firma



Los desarrolladores publican un archivo con las huellas digitales de los archivos, así como un archivo firmado con su clave PGP. Descárgalos para comparar tus archivos localmente.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Comprobar firma PGP



Compruebe que el archivo de huellas dactilares ha sido firmado por la clave importada.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Un resultado correcto muestra una firma válida con la clave `E53AD419B242822F19E23C6D3033D463D6E544F6` y el Address asociado `dojocoder@pm.me`. Puede aparecer una advertencia indicando que la clave no está certificada: puede ignorarla.



Si, por el contrario, la firma no es válida, detenga inmediatamente el proceso de instalación y vuelva a empezar desde el principio.



![Image](assets/fr/17.webp)



### 4.5. Comprobar la integridad del archivo



Calcule la huella digital SHA256 del archivo descargado y, a continuación, abra el archivo de huellas digitales para comparar los dos valores.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Si las dos huellas son idénticas, puede estar seguro de que el archivo no ha sido modificado. Si son diferentes, no sigas adelante y elimina los archivos.



![Image](assets/fr/18.webp)



### 4.6. Extraer y organizar archivos



Una vez completada con éxito la verificación, puede descomprimir el archivo y preparar una carpeta dedicada a la instalación de Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Limpiar archivos innecesarios



Elimine los archivos temporales y los archivos que ya no necesite para mantener limpio su entorno.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Configuración del Dojo



Dojo es un servidor backend que reúne varios servicios para interactuar con tu cartera y gestionar tu nodo Bitcoin. Su configuración puede ser compleja, pero el proyecto ofrece un método simplificado que instala y configura automáticamente los siguientes componentes:




- Dojo (API principal)
- Bitcoin core (nodo Bitcoin completo)
- Explorador BTC-RPC (web Block explorer)
- Fulcrum Indexer (indexación rápida de bloques y transacciones)
- Servidor Fulcrum Electrum disponible en la red Tor
- Servidor Fulcrum Electrum disponible en la red local
- Credenciales de la Administración



### 5.1. credenciales de administración



Para garantizar el acceso a los distintos servicios, es necesario generate varios identificadores únicos:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USUARIO
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `CLAVE_ADMIN_NODO`
- `NODE_JWT_SECRET`



Estos identificadores **deben ser únicos** (esto es muy importante: no debes utilizar la misma contraseña para varios servicios), estar compuestos únicamente por números, letras mayúsculas y minúsculas (alfanuméricos), y tener unos 40 caracteres para garantizar un alto nivel de seguridad. Una vez más, recomiendo encarecidamente el uso de un gestor de contraseñas.



### 5.2. Acceder a los archivos de configuración



Los archivos de configuración de Dojo se encuentran en la carpeta `conf/`. Mover a este directorio:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Configuración de Bitcoin core



Abra el archivo de configuración de Bitcoin core con el editor de texto nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



En este archivo, introduzca los identificadores generados:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Sustituye `tu-ID-aquí` y `tu-contraseña-aquí` por tus propios datos de acceso (con una contraseña segura).***



También puedes ajustar el tamaño de la memoria caché utilizada por Bitcoin core para mejorar el rendimiento (incluso puedes utilizar más si tienes mucha RAM disponible):



```
BITCOIND_DB_CACHE=2048
```



Para guardar los cambios y cerrar el editor :




- pulse `Ctrl + X
- tipo `y`
- y pulse "*Enter*"



### 5.4. Configuración de MySQL



A continuación, abra la configuración de la base de datos MySQL:



```bash
nano docker-mysql.conf.tpl
```



Por favor, introduzca sus datos de acceso:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ *** Sustituye `tu-id-aquí` y `tu-contraseña-aquí` por tus propios nombres de usuario (con contraseñas fuertes y únicas).***



Guardar de la misma manera (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Configuración del indexador Fulcrum



Abra el siguiente archivo:



```bash
nano docker-indexer.conf.tpl
```



Añade los parámetros para activar Fulcrum e integrarlo correctamente en Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



A continuación, hay 2 posibilidades, dependiendo de su configuración. Si Dojo está instalado en una máquina separada de tu ordenador cotidiano (en una máquina dedicada, un servidor...), introduce su IP Address en tu red local, por ejemplo :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Para averiguar la IP local Address de su máquina, abra otro terminal e introduzca el siguiente comando:



```bash
hostname -I
```



Segunda posibilidad: si Dojo se ejecuta directamente en su ordenador personal de todos los días, mantenga el valor por defecto ya presente en el archivo de configuración :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Guarda y sal del editor (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Configuración del servicio de nodos



Por último, abra la configuración del servicio principal de Dojo:



```bash
nano docker-node.conf.tpl
```



Por favor, introduzca sus datos de acceso:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Sustituye `tu-contraseña-aquí` por tus propias credenciales (con contraseñas fuertes y únicas).***



![Image](assets/fr/26.webp)



A continuación, active el indexador local:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Guarda y sal del editor (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Gestión del inicio de sesión



Una vez finalizada la configuración, no es necesario guardar todos los identificadores generados. El único que es absolutamente necesario guardar es :



```
NODE_ADMIN_KEY
```



Este inicio de sesión le permitirá acceder más tarde a la herramienta de mantenimiento Dojo. Todos los demás inicios de sesión pueden ser eliminados de su gestor de contraseñas o de sus notas manuscritas. Permanecerán accesibles desde los archivos de configuración de Dojo en caso de que necesites recuperarlos en el futuro.



## 6. Instalación del Dojo



En esta fase, Dojo se instalará e iniciará en su máquina. La operación pondrá en marcha varios servicios (Bitcoin core, el indexador Fulcrum, el backend de Dojo, etc.) e iniciará la sincronización completa de Blockchain Bitcoin. Esto puede tardar varios días, dependiendo de su hardware y de su conexión a Internet.



### 6.1. Compruebe que Docker funciona correctamente



Antes de comenzar la instalación, asegúrese de que Docker está operativo. Ejecute el siguiente comando:



```bash
docker run hello-world
```



Este comando descarga y lanza un pequeño contenedor de prueba. Si todo funciona correctamente, debería ver un mensaje similar a :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Si no aparece este mensaje, reinicie el equipo con :



```bash
sudo reboot
```



A continuación, vuelva a iniciar sesión en su cuenta **dojo** y ejecute de nuevo el comando de prueba. Si el error persiste, Docker no se ha instalado correctamente. En este caso, vuelve al paso `2.4.` sobre la instalación de Docker y comprueba cada comando cuidadosamente.



### 6.2. Ir al directorio de instalación de Dojo



Los scripts necesarios para la instalación se encuentran en la carpeta `my-dojo`. Desplácese a este directorio:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Usa el comando `ls` para comprobar que el archivo `dojo.sh` está presente. Este es el script principal que automatiza la instalación de Dojo y el lanzamiento de todos sus servicios.



![Image](assets/fr/29.webp)



### 6.3. Iniciar la instalación



Inicie la instalación ejecutando el archivo :



```bash
./dojo.sh install
```



Confirme la instalación pulsando `y` y luego "*Enter*".



![Image](assets/fr/30.webp)



Este script :




- descargar e iniciar los contenedores Docker necesarios,
- inicializar Bitcoin core y empezar a sincronizar Blockchain,
- iniciar el indexador Fulcrum para rastrear transacciones y direcciones,
- activar el backend Dojo y sus APIs.



Verás un flujo constante de registros desplazándose, con coloridas referencias como `bitcoind`, `soroban`, `nodejs` o `fulcrum`. Este desplazamiento indica que Dojo está funcionando y empezando a ejecutar los distintos servicios.



![Image](assets/fr/31.webp)



### 6.4. Salir de la pantalla de registro



Los registros aparecen en tiempo real en su terminal. Para volver al símbolo del sistema mientras Dojo se ejecuta en segundo plano, escriba :



```
Ctrl + C
```



No te preocupes: detener la visualización del registro no detiene los servicios. Docker continúa ejecutando Dojo en segundo plano (obviamente no necesitas detener el equipo si quieres que IBD continúe).



### 6.5. Comprender la *Descarga Inicial de Bloques* (IBD)



Al arrancar, Bitcoin core debe descargar y verificar todo el Blockchain desde 2009. Este paso se denomina ***Descarga Inicial de Bloques* (IBD)**. Es esencial, ya que permite a su nodo Dojo verificar cada bloque y transacción de Bitcoin de forma independiente.



La duración de esta sincronización depende de varios factores:




- la potencia de tu procesador y la cantidad de memoria RAM disponible,
- la velocidad de tu disco,
- el número y la calidad de los pares a los que se conecta su nodo,
- la velocidad de tu conexión a Internet.



En la práctica, esta operación suele durar entre **2 y 7 días**. Durante este periodo, puede dejar la máquina funcionando continuamente. Cuanto más tiempo esté encendida la máquina, más rápido se completará la sincronización. Le aconsejo que compruebe regularmente el estado de la sincronización consultando los registros de Bitcoin core, o utilizando la herramienta de mantenimiento de Dojo una vez instalada (véase la sección siguiente).



Para profundizar en sus conocimientos sobre la EII y, más en general, sobre el funcionamiento y la función de su nódulo Bitcoin, le recomiendo que eche un vistazo a este curso:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Supervisión de la sincronización



Cuando instale Dojo por primera vez, deberá esperar a que se completen dos operaciones principales: la descarga completa del Blockchain Bitcoin (*IBD*) y la indexación de este Blockchain por Fulcrum. Dependiendo de su conexión y de la potencia de la máquina, esto puede tardar varios días. Durante este tiempo, puedes monitorizar el progreso del proceso para asegurarte de que todo va bien.



Hay dos formas de controlar el estado de la sincronización:




- uso de la Herramienta de Mantenimiento Dojo (o DMT), que es sencilla pero proporciona pocos detalles durante el IBD;
- consulta directa de los registros de Dojo en su máquina, más técnica pero mucho más precisa.



### 7.1. Comprobación a través de la Herramienta de Mantenimiento Dojo (DMT)



La herramienta de mantenimiento Dojo es un Interface seguro y basado en la web que le permite supervisar el estado de su planta y realizar determinadas operaciones. Es la forma más fácil y accesible de supervisar el progreso del IBD. Durante la fase inicial de sincronización, la información mostrada puede ser limitada. Por ejemplo, el DMT no muestra el progreso detallado de la indexación de Fulcrum. En cambio, una vez completada la sincronización, el DMT mostrará claramente :




- todas las luces en Green;
- el último bloque validado para cada servicio (Nodo, Indexador, Dojo DB).



Para acceder a él, necesitas conocer la URL de tu DMT y conectarte a él [a través del navegador Tor](https://www.torproject.org/download/). Para ello, abra un terminal y vaya al directorio `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



A continuación, ejecute el siguiente comando:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Entonces tendrás acceso a toda la información relativa a las conexiones a tu Dojo a través de Tor. La que nos interesa aquí es la siguiente URL:



```
Dojo API and Maintenance Tool =
```



Para acceder al DMT desde cualquier máquina en cualquier red (incluso remotamente), abra el Navegador Tor e introduzca esta URL seguida de `/admin`. Por ejemplo, si tu URL es `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, tendrás que introducirla en la barra del [Navegador Tor](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Por favor, mantenga esta Address estrictamente confidencial



A continuación, se le redirigirá a una página de autenticación. El DMT inicia sesión utilizando la contraseña `NODE_ADMIN_KEY` que generó anteriormente.



![Image](assets/fr/33.webp)



Una vez iniciada la sesión, podrás acceder a la *Herramienta de mantenimiento Dojo* Durante el IBD, puedes ver la información "*Latest Block*" en el menú "*Full node*", que te permite conocer el estado actual de tu nodo Bitcoin.



![Image](assets/fr/34.webp)



Recuerde marcar este Address en el Navegador Tor para recuperarlo más tarde.



Una vez que tu Dojo esté totalmente sincronizado, deberías ver Green check ✅ en todos los indicadores de la página de inicio de DMT.



### 7.2. Verificación a través de los registros de Dojo



La segunda forma de seguir la evolución de su IBD es consultar directamente los registros de su máquina. Este enfoque ofrece un seguimiento mucho más preciso y en tiempo real. Puedes ver cómo Bitcoin core está progresando en la descarga de bloques, y cómo Fulcrum los está indexando.



Conéctate a la máquina que aloja tu Dojo y abre un terminal. Todos los comandos deben ejecutarse desde el directorio `my-dojo`. Sitúate en esta carpeta:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Registros Bitcoin core



Consulte los registros de Bitcoin core para seguir la evolución de la EII:



```bash
./dojo.sh logs bitcoind
```



Al principio, verá una fase de presincronización de las cabeceras de bloque:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Cuando esta cifra alcance el 100%, Bitcoin core iniciará la descarga completa de Blockchain. Verás el progreso del IBD. Para conocer la altura actual del bloque, fíjese en el valor indicado por `height=`. También puede seguir la clave `progress=`, que indica el porcentaje de progreso del IBD.



![Image](assets/fr/36.webp)



Como siempre, para cerrar los registros y volver al símbolo del sistema, utilice la combinación `Ctrl + C`.



#### Registros Fulcrum



Una vez que Bitcoin core ha completado la presincronización de cabeceras, Fulcrum comienza a indexar Blockchain sobre la marcha. Vea sus registros con :



```bash
./dojo.sh logs fulcrum
```



A continuación, verá la altura del último bloque indexado, indicada tras `height:`, así como el porcentaje de progreso de la indexación.



![Image](assets/fr/37.webp)



### 7.3. Corrupción de la base de datos Fulcrum



Fulcrum es un indexador especialmente potente, pero su instalación puede resultar compleja, entre otras cosas por la delicada gestión de su base de datos. En caso de corte de corriente o de apagado repentino de la máquina durante la sincronización inicial, la base de datos del indexador puede corromperse. Esto se puede comprobar, por ejemplo, con los siguientes registros:



```bash
fulcrum | The database has been corrupted etc...
```



**Nota:** Este tipo de error debería corregirse con la próxima versión de Fulcrum 2.0.



Si esto te ocurre, no hay ningún impacto en bitcoind (tu nodo Bitcoin): su IBD seguirá progresando independientemente de Fulcrum. Sin embargo, no podrás utilizar Fulcrum hasta que hayas borrado sus datos corruptos y hayas reiniciado su sincronización desde el principio. Así es como funciona:



Stop Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Borra sólo el contenedor y el volumen Fulcrum:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normalmente el nombre es `my-dojo_data-fulcrum`, si este no es tu caso, adapta el nombre devuelto por el comando anterior.



Entonces relanza Dojo y reconstruye Fulcrum desde cero:



```bash
./dojo.sh upgrade
```



A continuación, puedes comprobar que Fulcrum funciona correctamente consultando los logs:



```bash
docker logs -f fulcrum
```




## 8. Uso de la herramienta de mantenimiento Dojo



Una vez que su nudo Bitcoin está sincronizado al cabezal de urdimbre con el más Proof of Work, y el Blockchain está 100% indexado por Fulcrum, puede empezar a utilizar su Dojo.



Su Dojo ofrece una amplia gama de características, mejoradas regularmente con cada nueva versión. En mi opinión, las 2 más importantes son :




- la posibilidad de conectar su Ashigaru Wallet para utilizar su propio nodo para consultar los datos de Blockchain y transmitir sus transacciones,
- y la Block explorer, que le da acceso a información sobre la Blockchain Bitcoin sin exponer sus datos a una instancia externa que no controla.



Averigüemos cómo utilizarlos.


### 8.1. Conecta Ashigaru a tu Dojo



Conectar tu Ashigaru Wallet a tu Dojo es muy sencillo: una vez en tu DMT, abre el menú "*Pairing*". Aparecerá un código QR que podrás escanear directamente con la aplicación Ashigaru.



![Image](assets/fr/38.webp)



En la aplicación Ashigaru, la primera vez que la inicies después de crear o restaurar tu Wallet, serás redirigido a la página "*Configura tu servidor Dojo*". Pulse "*Escanear QR*", luego escanee el código QR mostrado en su DMT.



![Image](assets/fr/39.webp)



A continuación, haga clic en el botón "*Continuar*".



![Image](assets/fr/40.webp)



Ya estás conectado a tu Dojo.



![Image](assets/fr/41.webp)



### 8.2. Utilización de la Block explorer



Dojo instala automáticamente una Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), que se nutre directamente de los datos de tu propio nodo Bitcoin. El explorador te permite acceder a la información en bruto de Blockchain y tu Mempool a través de una web Interface fácil de entender. Así puedes, por ejemplo, comprobar el estado de una transacción pendiente, ver el saldo de una Address o examinar la composición de un bloque con facilidad.



Para acceder a él, simplemente recupere el Tor Address desde su navegador. Para ello, ejecute el mismo comando que utilizó para obtener el Address de su DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Tendrás acceso a toda la información de tu conexión a Dojo a través de Tor. La que nos interesa aquí es la siguiente URL:



```
Block Explorer =
```



Si ya estás conectado a tu DMT, también puedes encontrar esta Address en el menú "*Pairing*", dentro del JSON de conexión:



![Image](assets/fr/43.webp)



Para acceder a su navegador desde cualquier máquina en cualquier red (incluso remotamente), abra [Navegador Tor](https://www.torproject.org/download/) e introduzca la URL que acaba de recuperar.



⚠️ **Por favor, mantenga este Address estrictamente confidencial



Entonces tendrás acceso a tu propia Block explorer.



![Image](assets/fr/44.webp)



*Crédito de la imagen: https://ashigaru.rs/.*



Para rastrear una transacción, basta con introducir su txid en la barra de búsqueda de la parte superior derecha.



![Image](assets/fr/45.webp)



*Crédito de la imagen: https://ashigaru.rs/.*



Para comprobar los movimientos asociados a un Address, proceda del mismo modo introduciendo el Address en la barra de búsqueda.



![Image](assets/fr/46.webp)



*Crédito de la imagen: https://ashigaru.rs/.*



También puede introducir la Hash o la altura de un bloque en la barra de búsqueda para ver los detalles.



![Image](assets/fr/47.webp)



*Crédito de la imagen: https://ashigaru.rs/.*



## 9. Mantenimiento del dojo



### 9.1 Detenga su Dojo



Nunca corte bruscamente la alimentación de su Dojo, ya que podría corromper ciertas bases de datos, en particular el indexador Fulcrum. Si tienes que apagarlo, realiza siempre un apagado limpio de Dojo y, una vez completados todos los procedimientos, apaga también la máquina:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Actualice su Dojo



Dojo evoluciona regularmente y se publican nuevas versiones para corregir errores, mejorar la estabilidad y añadir funciones. Por lo tanto, es importante [comprobar regularmente si hay actualizaciones](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) y actualizar tu Dojo. El proceso es similar a la instalación inicial, pero requiere que reemplaces ciertos archivos con la última versión disponible, manteniendo tu configuración. A continuación se detallan los pasos a seguir para una actualización limpia y segura:



Para conocer la versión actual de tu Dojo, ejecuta el comando :



```bash
./dojo.sh version
```



Aunque este paso es opcional, te recomiendo que empieces por actualizar tu sistema operativo. Esto reduce el riesgo de incompatibilidades y asegura que las dependencias utilizadas por Dojo están actualizadas:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Vaya al directorio Dojo y detenga los servicios actuales:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



A continuación, reinicie el sistema para hacer borrón y cuenta nueva:



```bash
sudo reboot
```



Dojo viene con archivos firmados digitalmente. Estas firmas PGP aseguran que los archivos provienen del desarrollador y no han sido alterados de ninguna manera. Es importante comprobarlas cada vez que actualice Dojo, al igual que hizo cuando lo instaló por primera vez. Empiece descargando la clave pública del desarrollador vía Tor, luego impórtela :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Vuelve a tu directorio personal:



```bash
cd ~/
```



Descarga la última versión de Dojo desde GitHub vía Tor. En este ejemplo, es la versión `1.28.0` (que todavía no existe en el momento de escribir esto: es sólo para dar un ejemplo). Recuerde reemplazar el archivo y el enlace [con la versión que desea instalar](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Descargue también el archivo que contiene las huellas y la firma PGP (una vez más, recuerde ajustar la versión en el comando):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Compruebe que el archivo de huellas dactilares descargado ha sido firmado por la clave del desarrollador:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Un resultado correcto debería mostrar :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Puede aparecer un aviso de que la clave no está certificada, pero no tiene importancia. En cambio, si la firma no es válida o corresponde a otra clave, no siga adelante y comience de nuevo, comprobando los enlaces.



A continuación, calcule la huella digital SHA256 del archivo y compárela con el archivo oficial de huellas digitales :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Si las dos huellas coinciden perfectamente, el archivo es auténtico y está intacto. Si difieren, elimine los archivos inmediatamente y no continúe.



Descomprime el archivo en tu directorio personal:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



A continuación, copie el contenido en el directorio Dojo, sobrescribiendo el antiguo archivo :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Esta operación mantiene tus archivos de configuración ubicados en `~/dojo-app/docker/my-dojo/conf`, pero reemplaza todos los demás archivos con las versiones actualizadas.



Para mantener limpio tu entorno, elimina los archivos innecesarios :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Vuelva al directorio de scripts de Dojo y ejecute el comando de actualización:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Este comando ordena a Docker que reconstruya las imágenes con los nuevos archivos y, a continuación, reinicie automáticamente todos los servicios. Al final del proceso, comprueba los registros para asegurarte de que Bitcoin core, Fulcrum y Dojo funcionan correctamente:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Si los servicios se inician sin errores y los registros muestran bloques siendo procesados, su Dojo está ahora actualizado y operativo.