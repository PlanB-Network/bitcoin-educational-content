---
name: Mapa ₿ Academia - Pears App
description: Cómo instalo y uso la aplicación Plan ₿ Academy en Pears?
---

![cover](assets/cover.webp)



Como probablemente sepas, Plan ₿ Academy es la mayor base de datos educativa dedicada a Bitcoin, que reúne cursos, tutoriales y miles de recursos publicados bajo licencia abierta. Originalmente, Plan ₿ Academy era un sitio web. Pero, ¿qué pasaría si ya no pudieras acceder a ella con normalidad, por ejemplo en caso de censura?



En este tutorial, aprenderemos a ejecutar la plataforma **Plan ₿ Academy** de forma realmente incensurable gracias a **Pears**, una tecnología peer-to-peer (P2P) desarrollada por **Holepunch** y respaldada por **Tether**.



Pears es el software que nos permitirá ejecutar la plataforma Plan ₿ Academy sin depender de un sitio web centralizado. En este tutorial, instalaremos Pears en tu ordenador para acceder a Plan ₿ Academy a través de Pears.



El objetivo de Pears es sencillo: hacer posible la distribución y el uso de aplicaciones web sin depender de ninguna infraestructura centralizada (ni servidores, ni hosts, ni intermediarios). En otras palabras, aunque un proveedor de nube cierre o un país bloquee un dominio, la aplicación sigue viva entre los pares de la red. Este enfoque es el que permite que nuestra plataforma educativa Plan ₿ Academy siga siendo accesible en cualquier parte del mundo, sin un solo punto de fallo.



---

**TL;DR :**





- Instalar Peras ;





- Ejecute el siguiente comando para iniciar la aplicación Plan ₿ Academy:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Instalar Peras



### 1.1 ¿Qué son las peras?



Pears es un entorno de ejecución, una herramienta de desarrollo y una plataforma de despliegue para aplicaciones peer-to-peer. Esta herramienta de código abierto permite crear, compartir y ejecutar software sin servidor ni infraestructura, directamente entre usuarios. En concreto, esto significa que en lugar de alojar una aplicación en un servidor central, cada usuario se convierte en un nodo de la red, compartiendo parte de la aplicación y los datos con otros pares. Todo el sistema forma una red distribuida, en la que cada instancia coopera para mantener accesible el servicio.



![Image](assets/fr/01.webp)



Este enfoque se basa en un conjunto de ladrillos de software modulares desarrollados por Holepunch:




- Hypercore**: un registro distribuido que garantiza la coherencia y la seguridad de los datos sin una base de datos central.
- Hyperbee**: un indexador sobre Hypercore, para una organización y navegación eficientes de los datos.
- Hyperdrive**: un sistema de archivos distribuido utilizado para almacenar y sincronizar archivos de aplicaciones entre pares.
- Hyperswarm** y **HyperDHT**: capas de red que permiten el descubrimiento y la conexión entre pares de todo el mundo, sin un servidor central.
- Secretstream**: protocolo de cifrado E2E para proteger los intercambios entre dos pares.



Combinando estos componentes, Pears permite crear aplicaciones autónomas, cifradas y distribuidas, en las que cada usuario participa activamente en la red. Esta arquitectura descentralizada elimina los costes de infraestructura, los riesgos de censura y los SPOF (*Single Point of Failure*).



Pears está siendo desarrollado por Holepunch, una empresa fundada por Mathias Buus y Paolo Ardoino (CEO de Tether y CTO de Bitfinex), con la misión de extender la lógica peer-to-peer más allá de Bitcoin. Su ambición es construir la "Internet peer-to-peer", donde cada aplicación pueda ejecutarse sin autorización, sin servidores y sin intermediarios. Su ambición es construir la "Internet entre iguales", donde todas las aplicaciones puedan ejecutarse sin autorización, sin servidores y sin intermediarios. Holepunch ya está detrás de **Keet**, una aplicación de videoconferencia y mensajería totalmente P2P.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Este tutorial de instalación de Pears está dividido en varias secciones en función de su sistema operativo. Vaya directamente a la sección correspondiente a su entorno para seguir las instrucciones apropiadas :*




- Linux (Debian)** → Parte **1.2.**
- Windows** → Parte **1.3.**
- macOS** → Parte **1.4.**




### 1.2 - ¿Cómo se instala Pears en Linux (Debian)?



Instalar Pears en un sistema Debian es relativamente sencillo, pero requiere algunos requisitos previos, que explicaremos en detalle en esta sección.



#### 1.2.1. Actualización del sistema



En primer lugar, es importante asegurarse de que el sistema está actualizado.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Instalación de dependencias



Pears depende de una serie de bibliotecas del sistema, incluida `libatomic1`, utilizada por el tiempo de ejecución de Bare JavaScript. Instálala con el siguiente comando:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Instalación de Node.js y npm a través de NVM



Pears se distribuye a través de *npm*, el gestor de paquetes de *Node.js*. Aunque Pears no depende directamente de *Node.js* para funcionar, es necesario para la instalación. El método recomendado para instalar *Node.js* en Linux es *NVM* (*Node Version Manager*), que permite gestionar varias versiones de Node en paralelo.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



A continuación, vuelva a cargar su terminal para activar *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Compruebe que *NVM* está instalado:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



A continuación, instala una versión estable de *Node.js* (por ejemplo, la LTS actual):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Comprueba las instalaciones de *Node.js* y *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 Instalación de Pears con npm



Una vez que *npm* esté disponible, puedes instalar Pears CLI globalmente en tu sistema. Esto te permitirá ejecutar el comando `pear` desde cualquier directorio.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Inicializar Pears



Después de la instalación, simplemente ejecute el siguiente comando en su terminal:



```bash
pear
```



En la primera puesta en marcha, Pears se conectará a la red peer-to-peer para descargar los componentes necesarios. Este proceso no requiere ningún servidor central: los archivos se obtienen directamente de otros peers.



![Image](assets/fr/10.webp)



Una vez finalizada la descarga, vuelve a ejecutar el comando para comprobar que todo funciona:



```bash
pear
```



![Image](assets/fr/11.webp)



Si todo está correctamente instalado, aparecerá la Ayuda de Pears con una lista de los comandos disponibles.



#### 1.2.6. Pruebas de peras con Keet



Para comprobar que Pears está plenamente operativo, puedes lanzar una aplicación P2P ya disponible en la red, como Keet, el software de mensajería y videoconferencia de código abierto de Holepunch.



```bash
pear run pear://keet
```



Este comando carga la aplicación Keet directamente desde la red Pears, sin pasar por un servidor central. Si Keet se inicia correctamente, su instalación de Pears es totalmente funcional.



![Image](assets/fr/12.webp)



Tu sistema Linux ya está listo para ejecutar y alojar aplicaciones peer-to-peer con Pears.



### 1.3 - ¿Cómo se instala Pears en Windows?



Instalar Pears en Windows es tan fácil como en Linux, pero requiere algunas herramientas especiales.



*Si utiliza Linux y ya ha instalado Pears, puede ir directamente al paso 2



#### 1.3.1. Abrir PowerShell en modo administrador



En primer lugar, ejecute PowerShell con derechos de administrador :




- Haz clic en el menú Inicio;
- Escriba PowerShell ;
- Haga clic con el botón derecho del ratón en "*Windows PowerShell*" ;
- Seleccione "*Ejecutar como administrador*".



![Image](assets/fr/15.webp)



#### 1.3.2. Descargar NVS



Pears se instala mediante *npm*, el gestor de paquetes de *Node.js*. En Windows, el método recomendado por Holepunch es usar *NVS* (*Node Version Switcher*), que es más estable que *NVM* en este sistema.



En PowerShell, ejecute el siguiente comando para instalar la última versión de *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Instalación de Node.js



Tras la instalación, reinicie PowerShell e introduzca el siguiente comando:



```powershell
nvs
```



Deberías ver una lista de versiones disponibles de *Node.js*. Selecciona la primera pulsando la tecla `a` de tu teclado.



![Image](assets/fr/17.webp)



*Node.js* está instalado.



![Image](assets/fr/18.webp)



#### 1.3.4. Comprobar las instalaciones



Asegúrate de que *Node.js* y *npm* están accesibles:



```powershell
node -v
npm -v
```



Ambos comandos deben devolver un número de versión.



![Image](assets/fr/19.webp)



#### 1.3.5. Instalación de Pears con npm



Una vez que *Node.js* y *npm* estén disponibles, instala **Pears CLI** globalmente en tu sistema:



```powershell
npm install -g pear
```



Esto instalará el binario `pear` en tu directorio global *npm*.



![Image](assets/fr/20.webp)



#### 1.3.6. Comprobar e inicializar Pears



Una vez finalizada la instalación, ejecute :



```powershell
pear
```



Al iniciarse por primera vez, Pears descargará automáticamente los componentes necesarios de la red peer-to-peer. Este proceso puede tardar unos instantes.



![Image](assets/fr/21.webp)



Si todo ha ido bien, debería ver la pantalla de ayuda de CLI Pears con una lista de los subcomandos disponibles (run, seed, info...).



#### 1.3.7. Prueba de las peras con Keet



Para comprobar que Pears está plenamente operativo, puedes lanzar una aplicación P2P ya disponible en la red, como Keet, el software de mensajería y videoconferencia de código abierto de Holepunch.



```bash
pear run pear://keet
```



Este comando carga la aplicación Keet directamente desde la red Pears, sin pasar por un servidor central. Si Keet se inicia correctamente, su instalación de Pears es totalmente funcional.



![Image](assets/fr/22.webp)



Su sistema Windows ya está listo para ejecutar y alojar aplicaciones peer-to-peer con Pears.



### 1.4. ¿Cómo instalar Pears en macOS?



La instalación de Pears en macOS es similar a la de Linux, pero requiere algunos ajustes específicos del entorno Apple. Descubramos juntos estos pasos.



*Si utiliza Linux o Windows y ya ha instalado Pears, puede ir directamente al paso 2



#### 1.4.1. Comprobar los requisitos del sistema



Antes de instalar, por favor asegúrese de que *Xcode Command Line Tools* está presente en su sistema. Este paquete proporciona las herramientas de compilación necesarias para _Node.js_ y sus dependencias.



Para ello, abre un terminal con el atajo de teclado `Cmd + Barra espaciadora`, escribe `Terminal` y pulsa la tecla `Enter`. A continuación, introduzca este comando en el terminal para iniciar la instalación:



```bash
xcode-select --install
```



Si las herramientas ya están instaladas en tu sistema, macOS te informará.



#### 1.4.2. Instalación de la NVM



Pears se distribuye a través de *npm*, el gestor de paquetes de *Node.js*. Aunque Pears no depende directamente de *Node.js* para funcionar, es necesario para la instalación. El método recomendado para instalar *Node.js* en macOS es *NVM* (*Node Version Manager*), que permite gestionar varias versiones de Node en paralelo.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



A continuación, vuelva a cargar su terminal para activar *NVM* :



```bash
source ~/.zshrc
```



Si utiliza *bash* en lugar de *zsh*, ejecute :



```bash
source ~/.bashrc
```



A continuación, compruebe que *NVM* está instalado:



```bash
nvm --version
```



El terminal debería devolver la versión de *NVM* instalada en su sistema.



#### 1.4.3 Instalación de Node.js y npm



A continuación, instala una versión estable de *Node.js* (por ejemplo, la LTS actual):



```bash
nvm install --lts
```



Una vez finalizada la instalación, compruebe las versiones instaladas:



```bash
node -v
npm -v
```



Ambos comandos deben devolver un número de versión.



#### 1.4.4 Instalación de Pears con npm



Una vez que *npm* esté disponible, puedes instalar Pears CLI globalmente en tu sistema. Esto le permitirá ejecutar el comando `pear` desde cualquier directorio.



```bash
npm install -g pear
```



#### 1.4.5. Inicializar Pears



Después de la instalación, simplemente ejecute el siguiente comando en su terminal:



```bash
pear
```



En la primera puesta en marcha, Pears se conectará a la red peer-to-peer para descargar los componentes necesarios. Este proceso no requiere ningún servidor central: los archivos se obtienen directamente de otros peers.



Una vez finalizada la descarga, vuelve a ejecutar el comando para comprobar que todo funciona:



```bash
pear
```



Si todo está correctamente instalado, aparecerá la Ayuda de Pears con una lista de los comandos disponibles.



#### 1.4.6. Prueba de las peras con Keet



Para comprobar que Pears está plenamente operativo, puedes lanzar una aplicación P2P ya disponible en la red, como Keet, el software de mensajería y videoconferencia de código abierto de Holepunch.



```bash
pear run pear://keet
```



Este comando carga la aplicación Keet directamente desde la red Pears, sin pasar por un servidor central. Si Keet se inicia correctamente, su instalación de Pears es totalmente funcional.



Tu sistema macOS ya está listo para ejecutar y alojar aplicaciones peer-to-peer con Pears.



## 2. ¿Cómo se utiliza el Plan ₿ Academia en Peras?



Una vez que Pears esté instalado y en funcionamiento, podrá ejecutar directamente la plataforma **Plan ₿ Academy** a través de la red P2P. Simplemente ejecute el siguiente comando en su terminal (es el mismo comando para Linux, Windows y macOS):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



Una vez cargado, Plan ₿ Academy se abrirá en su entorno Pears, listo para ser utilizado como en el sitio web original, pero sin dependencia de un servidor central.



![Image](assets/fr/14.webp)