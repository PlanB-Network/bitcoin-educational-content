---
name: Zorin OS
description: Guía completa para instalar y utilizar Zorin OS como alternativa moderna a Windows
---

![cover](assets/cover.webp)



## Introducción



Un sistema operativo (SO) es el software fundamental que permite el funcionamiento de un ordenador: gestiona el hardware, el software, la seguridad y la interfaz de usuario.


Zorin OS es una distribución Linux diseñada específicamente para facilitar la transición desde Windows, al tiempo que ofrece las ventajas del software de código abierto: seguridad, estabilidad, privacidad y rendimiento.



Basado en Ubuntu LTS, Zorin OS combina una alta compatibilidad de software con una interfaz familiar y personalizable, lo que lo convierte en una alternativa creíble y accesible a Windows.



## ¿Por qué Zorin OS?





- Interface familiar**: Aspecto similar a Windows (menú de inicio, barra de tareas)
- Fácil transición**: diseñado para usuarios procedentes de Windows
- Mayor seguridad**: Arquitectura Linux, menos expuesta a los virus
- Respeto de la intimidad**: no se recopilan datos intrusivos
- Rendimiento optimizado**: funciona bien en máquinas modestas
- Ubuntu LTS** base: estabilidad, actualizaciones periódicas y amplia compatibilidad
- Personalización avanzada**: mediante la herramienta Zorin Appearance.



## Instalación y configuración



### 1. Requisitos previos



**Equipo necesario:**





- Una llave USB de al menos **8 GB** (se recomiendan 12 GB);
- Un ordenador con al menos **25 GB de espacio libre en disco**
- Conexión a Internet (recomendada).



### 2. Descargar Zorin OS





- Visite el sitio web oficial: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Elija **Zorin OS Core** (se recomienda la versión gratuita)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Descargar imagen ISO



Zorin OS también ofrece :





- Zorin OS Lite** (ordenadores antiguos)
- Zorin OS Pro** (de pago, con funciones avanzadas y asistencia)



## Crear una llave USB de arranque



Puede utilizar varias herramientas, como Balena Etcher :





- Descargue e instale [Balena Etcher](https://etcher.balena.io/).
- Abra Balena Etcher y seleccione la imagen ISO de Zorin.
- Selecciona la llave USB como soporte de destino.
- Haga clic en Flash y espere a que finalice el proceso.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Arranque con llave y acceso a la BIOS



Apague el ordenador en el que desea instalar Zorin OS y, a continuación, conecte la llave USB.


Cuando arranque el ordenador, accede a la BIOS (`ESC`, `F9` o `F11` según la marca) y selecciona la llave USB como dispositivo de arranque, después pulsa `Enter` para iniciar el proceso de arranque.





- Al iniciarse, seleccione **Probar o Instalar Zorin OS**.



![capture](assets/fr/08.webp)





- Si tienes una tarjeta gráfica NVIDIA, selecciona **Probar o Instalar Zorin OS (controladores NVIDIA modernos)**.
- Espere mientras se comprueban los archivos.



![capture](assets/fr/09.webp)





- En el instalador de Zorin OS, seleccione el idioma **Francés** y haga clic en Instalar **Zorin OS**.



![capture](assets/fr/10.webp)





- Selecciona la distribución del teclado.



![capture](assets/fr/11.webp)





- Marca las casillas **Descargar actualizaciones durante la instalación de Zorin OS** e **Instalar software de terceros para hardware gráfico y Wi-Fi y formatos multimedia adicionales**.



![capture](assets/fr/12.webp)





- Para instalar Zorin OS en todo el disco: seleccione **Borrar disco e instalar Zorin OS**.



![capture](assets/fr/14.webp)



Para instalar Zorin OS junto con Windows (arranque dual) :





- Seleccione **Instalar Zorin OS junto al Gestor de arranque de Windows**.



![capture](assets/fr/15.webp)





- Si no has particionado tu disco, selecciona el espacio de disco que deseas asignar a Zorin OS y haz clic en **Instalar ahora**.



![capture](assets/fr/16.webp)





- Confirme los cambios en el disco dos veces.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Seleccione la zona geográfica **París**.



![capture](assets/fr/18.webp)





- Crea tu cuenta de usuario y dale un nombre a tu ordenador.



![capture](assets/fr/19.webp)





- Espere mientras se instala Zorin OS.



![capture](assets/fr/20.webp)





- Una vez finalizada la instalación, haga clic en **Reiniciar ahora**.



![capture](assets/fr/21.webp)





- Retire la llave de instalación USB y pulse Intro.



![capture](assets/fr/22.webp)



## Descubrir y utilizar Zorin OS



### Primera puesta en marcha



Cuando encienda su ordenador, accederá a GRUB, el gestor de arranque de Linux. Por defecto, **Zorin OS** está seleccionado; después de 30 segundos, se inicia automáticamente.



![capture](assets/fr/23.webp)



Si has instalado Zorin OS como arranque dual con Windows, puedes arrancar Windows seleccionando **Administrador de arranque de Windows**.



Inicie sesión con su cuenta de usuario :



![capture](assets/fr/24.webp)



En el primer arranque, la aplicación **Welcome to Zorin OS** se lanza para ayudarte a descubrir tu nuevo sistema operativo.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Actualizar el sistema



En breve se abrirá el Gestor de Actualizaciones para informarle de que hay actualizaciones disponibles. Instálelas haciendo clic en el botón **Instalar ahora**.



![capture](assets/fr/33.webp)



Puede comprobar manualmente si hay actualizaciones en la aplicación **Software** > Actualizaciones:



![capture](assets/fr/34.webp)



### Personalización



Lo primero que hay que hacer en Zorin OS es elegir el **dispositivo de escritorio** con el que te sientas más cómodo. Encontrarás diseños similares a los encontrados en Windows (e incluso más con la versión Pro).



Para ello, abre **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



A continuación, abre **Configuración** para personalizar tu sistema:


**Sonido - Ajustes - Zorin OS



![capture](assets/fr/36.webp)



**Cuentas online - Configuración - Zorin OS



![capture](assets/fr/37.webp)



### Aplicaciones



Hay varias formas de instalar aplicaciones:





- Software**, la tienda de aplicaciones de Zorin OS. Las aplicaciones provienen de varias fuentes: apt, Flatpak y Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (línea de comandos) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Para obtener más información sobre la instalación de aplicaciones en Zorin OS, consulte esta página: [Instalar aplicaciones (zorin.com)](https://zorin.com/help/install-apps/).



### Aplicaciones Windows



Para instalar aplicaciones Windows, comience por instalar el paquete **zorin-windows-app-support** a través de Terminal :



```bash
sudo apt install zorin-windows-app-support
```



Para obtener una lista de aplicaciones Windows compatibles y sus niveles de compatibilidad, consulte la página [Base de datos de aplicaciones Wine] (https://appdb.winehq.org/). Allí encontrará las siguientes insignias, correspondientes al nivel de compatibilidad (de mejor a peor): Platino, Oro, Plata, Bronce y Basura.



Para instalar una aplicación .exe o .msi de Windows, tiene dos opciones:





- Abre **PlayOnLinux** y haz clic en el botón **Install** para buscar aplicaciones y juegos compatibles.



![capture](assets/fr/41.webp)





- Haga doble clic en el archivo **.exe o .msi** de la aplicación y déjese guiar por el programa de instalación.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Conclusión y recursos adicionales



Zorin OS es una alternativa sólida y asequible a Windows, que combina sencillez, seguridad y privacidad.



Permite una transición suave a Linux, sin sacrificar la comodidad ni la productividad.



Para proteger aún más tu vida digital, te recomendamos que utilices servicios respetuosos con la privacidad, especialmente para la comunicación encriptada:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2