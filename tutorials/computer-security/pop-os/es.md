---
name: Pop!_OS
description: Guía de instalación de Pop!_OS, una distribución de Linux
---

![cover](assets/cover.webp)



## Introducción



Pop!OS es un sistema operativo basado en Linux desarrollado por **System76**, un fabricante estadounidense especializado en máquinas para desarrolladores, diseñadores y usuarios avanzados.



Diseñado para ofrecer un entorno moderno, estable y de alto rendimiento, Pop!OS se distingue por una experiencia sencilla, potentes herramientas y un fuerte enfoque en la productividad.



### ¿Quién es System76?



System76 es una empresa estadounidense fundada en 2005 y con sede en Denver, especializada en la fabricación de portátiles, ordenadores de sobremesa y servidores diseñados específicamente para Linux.



A diferencia de los fabricantes tradicionales, System76 desarrolla máquinas diseñadas para ser abiertas, reparables y orientadas a la libertad del software.



System76 no sólo fabrica ordenadores.



La empresa también desarrolla :




- Pop!OS**, su propio sistema operativo basado en Linux;
- COSMIC**, el moderno entorno de escritorio de alto rendimiento utilizado por Pop!OS ;
- Open Firmware**, un firmware de código abierto basado en Coreboot ;
- herramientas para desarrolladores y diseñadores.



El objetivo es ofrecer una integración de hardware y software de alta calidad, comparable al ecosistema Apple, pero totalmente abierta y centrada en Linux.



## Un sistema moderno, estable y accesible



Pop!OS se basa en los cimientos de Ubuntu, lo que le confiere una excelente estabilidad, una amplia compatibilidad de hardware y acceso a un enorme ecosistema de software.


Ofrece una interfaz elegante, el escritorio COSMIC, diseñado para ser fluido, intuitivo y personalizable, incluso para los nuevos usuarios.



## Una opción ideal para desarrolladores, diseñadores y usuarios exigentes



Pop!OS es especialmente apreciado por :





- desarrolladores (herramientas preinstaladas, gestión avanzada de mosaicos),
- usuarios con tarjetas gráficas Nvidia o AMD,
- estudiantes y profesionales que buscan un sistema fiable,
- usuarios de windows que deseen realizar una transición sencilla.



Incluye embaldosado automático, un centro de software claro y herramientas de productividad integradas para facilitar el uso diario.



## Lo más destacado de Pop!OS





- Rendimiento optimizado** gracias a las actualizaciones periódicas.
- Dos versiones ISO disponibles**: estándar y optimizada para Nvidia.
- Seguridad mejorada** (cifrado LUKS disponible en la instalación).
- Interface COSMIC** ergonómico y moderno.
- Alta compatibilidad** con Ubuntu y el software Flatpak.



## Descargar POP!OS de forma segura



### 1. Requisitos previos



Antes de descargar e instalar POP!OS, hay algunas cosas que debe hacer para preparar correctamente el entorno de instalación.



### Equipamiento necesario





- Un ordenador compatible**: Procesador Intel o AMD, GPU Intel / AMD / Nvidia.
- Al menos 4 GB de RAM** (se recomiendan 8 GB para un uso cómodo).
- 20 GB de espacio libre como mínimo** (se recomiendan 40 GB o más).
- Una llave USB** de 4 GB como mínimo para crear el soporte de instalación.



### Conexión a Internet



Una conexión estable es útil para :





- descargar la imagen ISO,
- instalar actualizaciones después de la instalación.



Pop!OS puede funcionar sin conexión, pero la instalación es mucho más sencilla a través de Internet.



### Copia de seguridad de datos



Si Pop!OS va a sustituir o coexistir con otro sistema (Windows, Ubuntu, etc.), es aconsejable hacer una copia de seguridad de los archivos importantes antes de proceder.



### Compruebe la presencia de una GPU Nvidia (si procede)



Para los ordenadores equipados con una tarjeta gráfica Nvidia, tendrás que descargar la imagen ISO especial que incluye los controladores Nvidia.


Esta comprobación es muy sencilla:





- consultando las especificaciones del PC,
- o buscando el modelo de tarjeta gráfica en la configuración del sistema.



### Descargar de la web oficial



La imagen ISO de Pop!OS debe descargarse directamente de la página oficial de System76: [system76.com/pop](https://system76.com/pop/).



Esta página ofrece siempre la versión más reciente, adaptada a su hardware.



![capture](assets/fr/03.webp)



### Elige versión: Estándar o Nvidia, o Raspberry Pi (ARM64)



Pop!OS está disponible en tres variantes:



### Versión estándar



Recomendado para ordenadores que utilicen :





- procesador intel o AMD;
- una GPU Intel o AMD integrada;
- una tarjeta gráfica AMD Radeon.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Versión Nvidia



Recomendado para ordenadores equipados con tarjetas gráficas Nvidia.


Esta imagen ya incluye los controladores de Nvidia, lo que facilita la instalación y reduce los problemas gráficos.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Versión Raspberry Pi (ARM64)



Para Raspberry Pi 4 y 400 (procesador ARM).


Adaptada a la arquitectura ARM, se trata de una versión específica para estos miniordenadores.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Crear una llave USB de arranque



Puede utilizar varias herramientas, como Balena Etcher :





- Descargue e instale [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Abra Balena Etcher y seleccione la imagen Pop!OS ISO.
- Selecciona la llave USB como soporte de destino.
- Haga clic en Flash y espere a que finalice el proceso.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Instalación y seguridad de Pop!OS



### Arranque desde llave USB





- Apaga el ordenador.
- Conecte la llave USB (que contiene el Pop!OS).
- Encienda el ordenador. En los PC recientes, el sistema debería reconocer automáticamente la llave de arranque USB. Si no es así, reinicia manteniendo pulsada la tecla de acceso a la BIOS/UEFI (normalmente F2, F12 o Supr, según la marca).
  - En el menú BIOS/UEFI, selecciona tu llave USB como dispositivo de arranque.
  - Guardar y reiniciar.



### Iniciar la instalación



Una vez que haya seleccionado su llave USB de arranque como dispositivo de inicio, su ordenador arrancará en un entorno Pop!OS Live.



Seleccione su idioma.



![Capture](assets/fr/10.webp)



Seleccione una ubicación.



![Capture](assets/fr/11.webp)



Seleccione un idioma para la entrada de teclado.



![Capture](assets/fr/12.webp)



Selecciona una distribución de teclado.



![Capture](assets/fr/13.webp)



Elija la opción `Instalación limpia` para una instalación estándar. Esta es la mejor opción para los nuevos usuarios de Linux, pero tenga en cuenta que borrará todo el contenido de la unidad de destino. Alternativamente, puede seleccionar `Probar Modo Demo` para continuar probando Pop!OS en un entorno real.



![Capture](assets/fr/14.webp)



Selecciona `Personalizado (Avanzado)` para acceder a GParted. Esta herramienta le permite configurar funciones avanzadas como el arranque dual, la creación de una partición `/home` independiente o la colocación de la partición `/tmp` en una unidad diferente.



Haga clic en `Borrar e instalar` para instalar Pop!OS en la unidad seleccionada.



![Capture](assets/fr/15.webp)



### Configuración de la cuenta de usuario



La siguiente sección del programa de instalación le guiará a través de la creación de una cuenta de usuario para que pueda iniciar sesión en su nuevo sistema operativo.



Proporcione un nombre completo (puede incluir cualquier texto de su elección, en mayúsculas o minúsculas), así como un nombre de usuario (que debe estar en minúsculas) :



![Capture](assets/fr/16.webp)



Una vez creada la cuenta, se le pedirá que establezca una nueva contraseña.



![Capture](assets/fr/17.webp)



### Cifrado de disco completo



El cifrado del disco del sistema no es necesario, pero garantiza la seguridad de los datos del usuario en caso de que alguien acceda físicamente al dispositivo sin autorización.



La unidad puede cifrarse utilizando su contraseña de inicio de sesión marcando `La contraseña de cifrado es la misma que la contraseña de la cuenta de usuario`. También puede desmarcar esta casilla y seleccionar "Establecer contraseña" en la parte inferior. Seleccione `No cifrar` para ignorar el proceso de cifrado del disco.



![Capture](assets/fr/18.webp)



Si has elegido el botón "Establecer contraseña", verás un mensaje adicional para establecer tu contraseña de cifrado.



Continúe con el siguiente paso del programa de instalación. Pop!OS comenzará ahora la instalación en el disco.



![Capture](assets/fr/19.webp)



Una vez finalizada la instalación, reinicie el ordenador e inicie sesión para completar el proceso de configuración de la cuenta de usuario.



Si ha cambiado el orden de arranque para dar prioridad a su llave USB Live en el arranque, apague completamente el ordenador y retire la llave USB de instalación. Si está en modo de arranque dual, pulse las teclas adecuadas para acceder a la configuración y seleccione la unidad que contiene la instalación del Pop!OS.



![Capture](assets/fr/20.webp)



### Gráficos NVIDIA



Si has instalado desde la ISO de Intel/AMD y tu sistema tiene una tarjeta gráfica discreta NVIDIA, o si has añadido una posteriormente, tendrás que instalar manualmente los controladores de tu tarjeta para conseguir un rendimiento óptimo. Ejecute el siguiente comando en un terminal de comandos para instalar el controlador:



```bash
sudo apt install system76-driver-nvidia
```



También puedes instalar los controladores gráficos de NVIDIA desde la Pop!_Shop.



![Capture](assets/fr/20.webp)



## Instalación de herramientas esenciales



Pop!OS ofrece una amplia gama de software a través de su Pop!Shop, pero muchas herramientas esenciales también se pueden instalar a través del terminal con `apt` o `flatpak`. A continuación se explica cómo instalar las herramientas clave para un entorno de trabajo completo.



### Instalación de terminales




| Herramienta | Descripción | Comando de instalación |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox | Navegador web libre y popular | `sudo apt install firefox` |
| Brave | Navegador web enfocado en la privacidad | Instalación vía Pop!_Shop o sitio oficial |
| Visual Studio Code (VS Code) | Editor de código potente para desarrolladores | `flatpak install flathub com.visualstudio.code` |
| Git | Gestor de versiones | `sudo apt install git` |
| Flatpak | Gestor de paquetes alternativo | `sudo apt install flatpak` |
| VLC | Reproductor multimedia versátil | `sudo apt install vlc` |
| GNOME Terminal | Terminal por defecto | Preinstalado en Pop!OS |
| Curl | Herramienta de transferencia de datos en línea | `sudo apt install curl` |
| Wget | Descarga de archivos vía HTTP/FTP | `sudo apt install wget` |
| Docker | Contenedorización de aplicaciones | Instalación vía script oficial o `apt` |
| Node.js | Entorno JavaScript del lado del servidor | Instalación vía `apt` o NodeSource |
| Python3 | Lenguaje de programación | `sudo apt install python3 python3-pip` |
| GIMP | Editor de imágenes avanzado | `sudo apt install gimp` |
| Thunderbird | Cliente de correo | `sudo apt install thunderbird` |
| Transmission | Cliente BitTorrent ligero | `sudo apt install transmission-gtk` |
| Htop | Monitor de sistema interactivo | `sudo apt install htop` |

### ¡Instalación a través de Pop! Shop (interfaz gráfica)





- Abra **Pop!_Shop** desde el menú principal.
- Utiliza la barra de búsqueda para encontrar las aplicaciones que desees (por ejemplo, "Brave").
- Haga clic en **Instalar** para cada aplicación.
- Pop!_Shop gestiona automáticamente las dependencias y actualizaciones.



## Actualización del sistema



### Opción 1: a través de la interfaz gráfica de usuario (GUI)



Pop!OS cuenta con un sencillo e intuitivo gestor gráfico de actualizaciones.



1. Haga clic en el **menú principal** (icono inferior izquierdo).


2. Abrir **"Pop!_Shop "**.


3. En la tienda Pop!_Shop, haga clic en la pestaña **"Actualizaciones "**.


4. El sistema comprobará automáticamente si hay actualizaciones disponibles.


5. Haga clic en **"Actualizar todo "** para iniciar la instalación de las actualizaciones.


6. Introduzca su contraseña si se le solicita.


7. Deje que finalice el proceso y, si es necesario, reinícielo.



### Opción 2: A través del terminal



Abra un terminal y escriba :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Gestión de usuarios



Recomendamos utilizar una cuenta de usuario estándar con derechos sudo para las operaciones cotidianas.



Para crear un nuevo usuario :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Cierre la sesión y vuelva a iniciarla con este nuevo usuario.



### Gestión de controladores gráficos





- En el caso de las tarjetas Nvidia, comprueba que están instalados los controladores propietarios:



```bash
sudo apt install system76-driver-nvidia
```





- En el caso de AMD/Intel, los controladores suelen venir incluidos por defecto.



### Activar cortafuegos (UFW)



Pop!OS no bloquea el tráfico de red por defecto. Active UFW para mejorar la seguridad:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Configurar las actualizaciones automáticas



Mantener el sistema actualizado sin intervención manual:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Personalizar la apariencia y el comportamiento





- Abre **Configuración del sistema** → **Apariencia** para elegir un tema claro u oscuro.
- Configure las esquinas activas, las animaciones y las extensiones mediante el gestor COSMIC.
- Ajusta la distribución del escritorio para optimizar tu flujo de trabajo.



### Configurar la copia de seguridad automática



Pop!OS integra herramientas como Deja Dup para realizar copias de seguridad:





- Inicie **Backup** desde el menú.
- Elige una unidad externa o una ubicación de red.
- Programe copias de seguridad periódicas.



### Instalación de extensiones útiles de GNOME/COSMIC



He aquí algunas extensiones recomendadas para mejorar la experiencia del usuario:





- Dash to Dock**: barra de aplicaciones siempre visible.
- GSConnect**: sincronización con Android.
- Indicador del portapapeles**: gestión avanzada del portapapeles.



Instálelos a través de :



```bash
sudo apt install gnome-shell-extensions
```



A continuación, actívalos en los ajustes.



### Optimización de la gestión de memoria y swap



Comprueba el estado de tu intercambio:



```bash
swapon --show
```



Si es necesario, aumente el tamaño de la swap o configure un archivo swap :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Añádalo al archivo `/etc/fstab` para el montaje automático.



## Gestión de paquetes y repositorios



### Comprender las fuentes de los paquetes



Pop!OS, basado en Ubuntu, utiliza principalmente :





- Repositorios oficiales de Ubuntu**: para la mayoría del software estable.
- Repositorios System76**: para controladores, firmware y herramientas específicas.
- Flatpak**: acceda a una amplia gama de aplicaciones sandboxed.
- Snap** (opcional): otro formato de paquete universal.



---

### Añadir y gestionar repositorios PPA



Para instalar software actualizado con frecuencia, se pueden añadir determinados PPA (Archivos de Paquetes Personales):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Conclusión



Pop!OS es una distribución Linux moderna y estable, adecuada tanto para principiantes como para usuarios avanzados.



Gracias a su intuitiva interfaz COSMIC y a sus herramientas integradas, ofrece una experiencia fluida y productiva, ya sea para el desarrollo, la creación o el uso cotidiano.



Este tutorial cubre las etapas clave: preparación, descarga, instalación, ajustes iniciales y herramientas esenciales.



No dudes en explorar Pop!OS más a fondo y personalizar tu entorno para sacarle el máximo partido.