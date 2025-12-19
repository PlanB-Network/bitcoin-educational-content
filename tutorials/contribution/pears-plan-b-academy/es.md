---
name: Plan ₿ Academy - Pears App
description: ¿Cómo instalar y utilizar la aplicación Plan ₿ Academy en Pears?
---

![cover](assets/cover.webp)


Probablemente ya sepas que Plan ₿ Academy es la mayor base de datos educativa dedicada a Bitcoin, que reúne cursos, tutoriales y miles de recursos de código abierto. Originalmente, Plan ₿ Academy era un sitio web. Pero, ¿qué pasaría si ya no pudieras acceder a ella normalmente, por ejemplo en caso de censura?


En este tutorial, aprenderemos a ejecutar la plataforma **Plan ₿ Academy** de una forma realmente resistente a la censura utilizando **Pears**, una tecnología peer-to-peer (P2P) desarrollada por **Holepunch** y apoyada por **Tether**.


Pears es el software que nos permite ejecutar la plataforma Plan ₿ Academy sin depender de un sitio web centralizado. En este tutorial, instalaremos Pears en su ordenador para poder acceder a Plan ₿ Academy a través de Pears.


El objetivo de Pears es sencillo: hacer posible la distribución y el uso de aplicaciones web sin depender de ninguna infraestructura centralizada (ni servidores, ni hosts, ni intermediarios). En otras palabras, aunque un proveedor de nube cierre o un país bloquee un dominio, la aplicación sigue viviendo entre los pares de la red. Este enfoque permite que nuestra plataforma educativa, Plan ₿ Academy, siga siendo accesible en todo el mundo, sin un solo punto de fallo.


---

**TL;DR:**



- Instala Peras;



- Ejecute el siguiente comando para iniciar la aplicación Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. ¿Qué son las peras?


Pears es a la vez un entorno de ejecución, una herramienta de desarrollo y una plataforma de despliegue para aplicaciones peer-to-peer. Esta herramienta de código abierto permite crear, compartir y ejecutar software sin servidores ni infraestructura, directamente entre usuarios. En términos prácticos, esto significa que en lugar de alojar una aplicación en un servidor central, cada usuario se convierte en un nodo de la red: comparte parte de la aplicación y los datos con otros pares. Todo el sistema forma una red distribuida en la que cada instancia coopera para mantener accesible el servicio.


![Image](assets/fr/01.webp)


Este enfoque se basa en un conjunto de componentes de software modulares desarrollados por Holepunch:



- Hypercore**: un registro distribuido que garantiza la coherencia y la seguridad de los datos sin una base de datos central.
- Hyperbee**: un índice construido sobre Hypercore que permite organizar y consultar los datos de forma eficiente.
- Hyperdrive**: un sistema de archivos distribuido utilizado para almacenar y sincronizar archivos de aplicaciones entre pares.
- Hyperswarm** y **HyperDHT**: capas de red que permiten el descubrimiento de pares y conexiones en todo el mundo sin un servidor central.
- Secretstream**: protocolo de cifrado de extremo a extremo que asegura la comunicación entre pares.


Combinando estos componentes, Pears permite crear aplicaciones autónomas, cifradas y distribuidas, en las que cada usuario participa activamente en la red. Esta arquitectura descentralizada elimina los costes de infraestructura, los riesgos de censura y los SPOF (*Single Points of Failure*).


Pears ha sido desarrollado por Holepunch, una empresa fundada por Mathias Buus y Paolo Ardoino (CEO de Tether y CTO de Bitfinex), con la misión de extender la lógica peer-to-peer más allá de Bitcoin. Su ambición es construir la "*Internet de los peers*", donde cada aplicación pueda operar sin permisos, sin servidores y sin intermediarios. Su ambición es construir la "*Internet de los pares*", donde cada aplicación pueda operar sin permiso, sin servidores y sin intermediarios. Holepunch ya está detrás de **Keet**, una aplicación de videoconferencia y mensajería totalmente P2P.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Este tutorial de instalación de Pears está dividido en varias secciones en función de su sistema operativo. Vaya directamente a la que corresponda a su entorno para seguir las instrucciones adecuadas:*



- Linux (Debian)** → Sección **2**
- Ventanas** → Sección **3**
- macOS** → Sección **4**


## 2. ¿Cómo instalar Pears en Linux (Debian)?


Instalar Pears en Debian es relativamente sencillo, pero requiere algunos requisitos previos, que detallaremos en esta sección.


### 2.1. Actualizar el sistema


Antes de nada, es importante asegurarse de que su sistema está actualizado.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Instalar dependencias


Pears depende de algunas bibliotecas del sistema, entre ellas `libatomic1`, utilizada por el motor de ejecución Bare JavaScript. Instálela con el siguiente comando:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Instalar Node.js y npm a través de NVM


Pears se distribuye a través de *npm*, el gestor de paquetes de *Node.js*. Aunque Pears no depende directamente de *Node.js* para funcionar, es necesario para su instalación. La forma recomendada de instalar *Node.js* en Linux es a través de *NVM* (*Node Version Manager*), que permite gestionar múltiples versiones de Node una al lado de la otra.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


A continuación, vuelve a cargar tu terminal para activar *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Compruebe que la *NVM* está correctamente instalada:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


A continuación, instala una versión estable de *Node.js* (por ejemplo, la versión LTS actual):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Compruebe que *Node.js* y *npm* están correctamente instalados:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Instalar Pears con npm


Una vez que *npm* está disponible, puedes instalar globalmente Pears CLI en tu sistema. Esto te permite ejecutar el comando `pear` desde cualquier directorio.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Inicializar Pears


Después de la instalación, simplemente ejecute el siguiente comando en su terminal:


```bash
pear
```


Al iniciarse, Pears se conectará a la red peer-to-peer para descargar los componentes necesarios. Este proceso no depende de ningún servidor central: los archivos se obtienen directamente de otros pares.


![Image](assets/fr/10.webp)


Una vez finalizada la descarga, vuelve a ejecutar el comando para confirmar que todo funciona:


```bash
pear
```


![Image](assets/fr/11.webp)


Si todo está correctamente instalado, aparecerá el menú de ayuda de Pears con una lista de comandos disponibles.


### 2.6. Peras de prueba con Keet


Para comprobar que Pears está plenamente operativo, puede iniciar una aplicación P2P existente disponible en la red, como Keet, el software de mensajería y videoconferencia de código abierto desarrollado por Holepunch.


```bash
pear run pear://keet
```


Este comando carga la aplicación Keet directamente desde la red Pears, sin utilizar un servidor central. Si Keet se inicia correctamente, significa que su instalación de Pears es totalmente funcional.


![Image](assets/fr/12.webp)


Tu sistema Linux ya está listo para ejecutar y alojar aplicaciones peer-to-peer con Pears.


## 3. Cómo instalar Pears en Windows


La instalación de Pears en Windows es tan sencilla como en Linux, pero requiere algunas herramientas específicas.


*Si utilizas Linux y ya has instalado Pears, puedes pasar directamente al **Paso 5**.*


### 3.1. Abra PowerShell como administrador


En primer lugar, inicie PowerShell con privilegios de administrador:



- Haz clic en el menú Inicio;
- Escribe "PowerShell";
- Haga clic con el botón derecho del ratón en "*Windows PowerShell*";
- Seleccione "*Ejecutar como administrador*".


![Image](assets/fr/15.webp)


### 3.2. Descargar NVS


Pears se instala mediante *npm*, el gestor de paquetes de *Node.js*. En Windows, el método recomendado por Holepunch es usar *NVS* (*Node Version Switcher*), que es más estable que *NVM* en este sistema.


En PowerShell, ejecute el siguiente comando para instalar la última versión de *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Instalar Node.js


Tras la instalación, reinicie PowerShell e introduzca el siguiente comando:


```powershell
nvs
```


Deberías ver una lista de versiones disponibles de *Node.js*. Selecciona la primera pulsando la tecla `a` de tu teclado.


![Image](assets/fr/17.webp)


*Node.js* ya está instalado.


![Image](assets/fr/18.webp)


### 3.4. Verificar las instalaciones


Asegúrate de que *Node.js* y *npm* están accesibles:


```powershell
node -v
npm -v
```


Ambos comandos deberían devolver un número de versión.


![Image](assets/fr/19.webp)


### 3.5. Instalar Pears con npm


Una vez que *Node.js* y *npm* estén disponibles, instala **Pears CLI** globalmente en tu sistema:


```powershell
npm install -g pear
```


Esto instala el binario `pear` en tu directorio global *npm*.


![Image](assets/fr/20.webp)


### 3.6. Verificar e inicializar las peras


Una vez finalizada la instalación, ejecútela:


```powershell
pear
```


Al iniciarse por primera vez, Pears descargará automáticamente los componentes necesarios de la red peer-to-peer. Este proceso puede tardar unos instantes.


![Image](assets/fr/21.webp)


Si todo ha ido bien, debería ver el menú de ayuda de Pears CLI con la lista de subcomandos disponibles (run, seed, info...).


### 3.7. Peras de prueba con Keet


Para comprobar que Pears está plenamente operativo, puede iniciar una aplicación P2P existente disponible en la red, como Keet, el software de mensajería y videoconferencia de código abierto desarrollado por Holepunch.


```bash
pear run pear://keet
```


Este comando carga la aplicación Keet directamente desde la red Pears, sin utilizar ningún servidor central. Si Keet se inicia correctamente, significa que su instalación de Pears es totalmente funcional.


![Image](assets/fr/22.webp)


Su sistema Windows ya está listo para ejecutar y alojar aplicaciones peer-to-peer con Pears.


## 4. Cómo instalar Pears en macOS


La instalación de Pears en macOS es similar a la de Linux, pero requiere algunos ajustes específicos para el entorno de Apple. Repasemos juntos estos pasos.


*Si utilizas Linux o Windows y ya has instalado Pears, puedes pasar directamente al **Paso 5**.*


### 4.1. Compruebe los requisitos previos del sistema


Antes de la instalación, asegúrate de que *Xcode Command Line Tools* está instalado en tu sistema. Este paquete proporciona las herramientas de compilación necesarias para *Node.js* y sus dependencias.


Para ello, abre un terminal con el atajo `Cmd + Barra espaciadora`, escribe `Terminal` y pulsa `Enter`. A continuación, ejecuta el siguiente comando en el terminal para instalarlo:


```bash
xcode-select --install
```


Si las herramientas ya están instaladas en tu sistema, macOS te lo notificará.


### 4.2. Instalar NVM


Pears se distribuye a través de *npm*, el gestor de paquetes de *Node.js*. Aunque Pears no depende directamente de *Node.js* para funcionar, es necesario para la instalación. El método recomendado para instalar *Node.js* en macOS es *NVM* (*Node Version Manager*), que permite gestionar múltiples versiones de Node simultáneamente.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Luego recarga tu terminal para activar *NVM*:


```bash
source ~/.zshrc
```


Si utiliza *bash* en lugar de *zsh*, ejecute:


```bash
source ~/.bashrc
```


A continuación, compruebe que *NVM* está instalado correctamente:


```bash
nvm --version
```


Su terminal debería mostrar la versión *NVM* instalada.


### 4.3. Instalar Node.js y npm


A continuación, instala una versión estable de *Node.js* (por ejemplo, la versión LTS actual):


```bash
nvm install --lts
```


Una vez finalizada la instalación, verifique las versiones instaladas:


```bash
node -v
npm -v
```


Ambos comandos deberían devolver un número de versión.


### 4.4. Instalar Pears con npm


Una vez que *npm* esté disponible, puedes instalar globalmente Pears CLI en tu sistema. Esto te permitirá ejecutar el comando `pear` desde cualquier directorio.


```bash
npm install -g pear
```


### 4.5. Inicializar Pears


Después de la instalación, simplemente ejecute el siguiente comando en su terminal:


```bash
pear
```


Al iniciarse, Pears se conecta a la red peer-to-peer para descargar los componentes necesarios. Este proceso no requiere ningún servidor central: los archivos se recuperan directamente de otros pares.


Una vez finalizada la descarga, vuelva a ejecutar el comando para comprobar que todo funciona:


```bash
pear
```


Si todo está correctamente instalado, aparecerá el menú de ayuda de Pears con la lista de comandos disponibles.


### 4.6. Peras de prueba con Keet


Para comprobar que Pears está plenamente operativo, puede iniciar una aplicación P2P ya disponible en la red, como Keet, el software de mensajería y videoconferencia de código abierto de Holepunch.


```bash
pear run pear://keet
```


Este comando carga la aplicación Keet directamente desde la red Pears, sin utilizar un servidor central. Si Keet se inicia correctamente, significa que tu instalación de Pears es totalmente funcional.


Tu sistema macOS ya está listo para ejecutar y alojar aplicaciones peer-to-peer con Pears.


## 5. Cómo utilizar la Academia Plan ₿ en las peras


Una vez que Pears esté instalado y en funcionamiento, podrá iniciar directamente la plataforma **Plan ₿ Academy** a través de la red P2P. Simplemente ejecute el siguiente comando en su terminal (el mismo comando funciona en Linux, Windows y macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Una vez finalizada la carga, Plan ₿ Academy se abrirá en su entorno Pears, listo para ser utilizado igual que el sitio web original, pero sin depender de un servidor central.


![Image](assets/fr/14.webp)


## 6. Cómo sembrar plan ₿ Academia sobre las peras


En la red Pears, *seed* una aplicación significa redistribuirla a otros pares desde su propia máquina. En la práctica, cuando usted seed Plan ₿ Academy, su ordenador se convierte en una fuente de datos que permite a otros usuarios descargar la aplicación sin depender de un servidor central.


Este mecanismo refuerza la resiliencia y la resistencia a la censura de nuestra aplicación en la red Pears. Cuantos más pares seed tenga una aplicación, más disponible y descentralizada estará, incluso si algunos nodos originales se desconectan.


Para ayudar a distribuir el Plan ₿ Academia, basta con ejecutar el siguiente comando:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Mientras este comando permanezca activo, tu dispositivo participará en la distribución de los archivos de la aplicación. Si cierras el terminal, el proceso de compartición se detiene.


Para continuar la siembra después de un reinicio, puede ejecutar el comando en segundo plano o crear un servicio del sistema, por ejemplo, un servicio systemd en Linux, un LaunchAgent en macOS o una tarea programada en Windows. Estos métodos garantizan que la aplicación Plan ₿ Academy reanude automáticamente la siembra al iniciar el sistema.


¡Gracias por contribuir a la distribución descentralizada del Plan ₿ Academia en Peras y ayudar a que la educación de Bitcoin sea realmente resistente a la censura!