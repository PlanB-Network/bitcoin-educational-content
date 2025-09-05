---
name: Fedora
description: La distribución Linux que te proporciona un espacio de trabajo libre, completo y seguro.
---


![cover](assets/cover.webp)





Fedora es un sistema operativo gratuito y de código abierto basado en Linux lanzado en 2003, desarrollado por la comunidad del **Proyecto Fedora** y respaldado por **Red Hat Linux**. Es famoso por su estabilidad, buen rendimiento y facilidad de uso, lo que lo convierte en una opción excelente tanto para principiantes como para usuarios avanzados. El sistema funciona en la mayoría de las arquitecturas de procesador modernas, lo que facilita su instalación en prácticamente cualquier ordenador. Fedora también está disponible en varias ediciones preconfiguradas, llamadas "Fedora Spins" o "Fedora Editions", diseñadas para necesidades específicas (videojuegos, astronomía, desarrollo...).



## Arquitectura de Fedora Linux



Como has leído antes, Fedora es un sistema operativo libre basado en el núcleo Linux. El núcleo Linux es la parte del sistema operativo que se comunica con el hardware del ordenador y gestiona los recursos del sistema, como la memoria y la capacidad de procesamiento.



Fedora Linux incluye una variedad de herramientas de software y aplicaciones que son necesarias para ejecutar el sistema operativo sobre el núcleo Linux. La arquitectura modular de Fedora significa que consiste principalmente en una colección de componentes individuales que pueden ser fácilmente agregados, removidos o reemplazados según se requiera. Esto le permite dar forma al sistema operativo utilizando sólo los recursos que necesita.



Fedora también incluye un entorno de escritorio, que es el Interface a través del cual los usuarios realizan las tareas y acceden a las aplicaciones. El entorno de escritorio predeterminado de Fedora es GNOME, un entorno de escritorio amigable, fácil de usar y altamente personalizable.



## ¿Por qué elegir Fedora?



Entre la multitud de distribuciones Linux disponibles, Fedora destaca especialmente por:





- Modularidad**: Compatible con diferentes arquitecturas de procesador, Fedora puede instalarse en la mayoría de ordenadores, incluso los de baja potencia, adaptándose perfectamente a sus necesidades.





- Un Interface sencillo e intuitivo**: Fedora combina un moderno Interface gráfico con un potente Interface de línea de comandos, lo que facilita su uso para todos los perfiles.





- Estabilidad del kernel**: Basado en Red Hat, Fedora es famoso por la fiabilidad de sus actualizaciones, especialmente las del kernel, que se llevan a cabo sin grandes fallos gracias a las contribuciones gratuitas de una gran comunidad.





- Instalación rápida y sencilla**: con un tamaño de imagen de sólo 3 GB, la instalación es rápida y sencilla, incluso en máquinas con recursos limitados.



## Ediciones Fedora



En función de su perfil y uso, Fedora ofrece ediciones que se adaptan a sus necesidades. Principalmente encontrarás ediciones:





- Estación de trabajo Fedora**: Ideal para uso personal y/o profesional en sus ordenadores, esta edición lleva instaladas utilidades genéricas como navegadores, una suite ofimática (editores de texto) y software de reproducción multimedia.





- Servidor Fedora**: Esta edición está dedicada a la gestión de servidores. Fedora Server incluye diversas herramientas que le ayudarán a desplegar y gestionar servidores a su propia escala.





- Fedora CoreOS**: ¿Desea ejecutar y desplegar fácilmente aplicaciones en la nube? Fedora CoreOS es la edición que le ofrece las herramientas para crear y gestionar imágenes con Docker y Kubernets, por ejemplo.



En este tutorial, nos haremos cargo de la edición Fedora Workstation. Sin embargo, los procesos detallados a continuación son similares para las otras ediciones.



## Instalación y configuración de Fedora Workstation



La instalación de Fedora Workstation requiere la siguiente configuración de hardware:




- Una memoria USB de al menos **8 GB** para arrancar el sistema operativo.
- Al menos **40 GB de espacio libre** en el disco Hard de tu ordenador.
- 4 GB de RAM** para una experiencia fluida.



### Descargar Fedora Workstation



Puede descargar la edición [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) desde el sitio web oficial del proyecto Fedora. A continuación, seleccione la versión correspondiente a la arquitectura de su procesador (32 bits - 64 bits) y haga clic en el icono **Descargar**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Crear una llave USB de arranque



Para instalar Fedora, es necesario crear una llave USB de arranque utilizando software como [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Una vez que hayas terminado de instalar Balena Etcher, abre la aplicación y selecciona la imagen ISO de Fedora Workspace descargada. Selecciona tu llave USB como medio de destino y haz clic en el botón **Flash** para empezar a crear la llave de arranque.



![boot](assets/fr/05.webp)


### Instalación de Fedora



Cuando hayas terminado de arrancar la llave USB, apaga el ordenador.


Encienda su ordenador y acceda a la BIOS durante el arranque pulsando la tecla `F2`, `F12` o `ESC`, dependiendo de su ordenador.



En las opciones de arranque, seleccione su llave USB como dispositivo de arranque primario. Al confirmar esta elección, su ordenador se reiniciará e iniciará automáticamente el instalador de Fedora** presente en la llave USB.



Una vez que el ordenador haya arrancado desde la memoria USB, aparecerá la pantalla **GRUB**.



En esta fase, tiene las siguientes opciones:




- Medios de prueba**: Esta opción te permite comprobar la integridad de la memoria USB y asegurarte de que todas las dependencias necesarias para una correcta instalación están presentes. Se trata de un paso opcional, pero recomendable si tiene dudas sobre la memoria USB.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Iniciar Fedora**: Inicia Fedora en modo "vivo", sin instalación.



En el escritorio de Fedora (modo en vivo), haga clic en **Instalar Fedora** (o Instalar en disco Hard) para iniciar el proceso de instalación. Puede elegir instalar más tarde y probar Fedora sin tener que instalarlo.



![install-live](assets/fr/08.webp)



El primer paso es seleccionar el **idioma de instalación** de Fedora y la **disposición del teclado**



![language](assets/fr/10.webp)





- Selección del disco de instalación:



Elija el disco Hard en el que desea instalar Fedora.



Si el disco está vacío, Fedora utilizará automáticamente todo el espacio disponible. De lo contrario, puede personalizar el particionamiento (manual o automático).



![disk](assets/fr/11.webp)





- Cifrado:



En esta etapa, Fedora sugiere encriptar su disco para agregar un Layer extra de seguridad. Esto asegura que sus datos sólo puedan ser leídos por su sistema Fedora.



![chiffrement](assets/fr/12.webp)



Antes de iniciar la instalación, Fedora muestra un resumen de sus opciones. Confirme y haga clic en el botón instalar para iniciar la instalación de Fedora.



![resume](assets/fr/13.webp)



Durante la instalación, Fedora copia archivos y configura el sistema. Cuando termina, el ordenador se reinicia automáticamente.



![installation](assets/fr/14.webp)



### Configuración básica


La primera vez que lo uses, tendrás que finalizar algunos ajustes:




- Cambie el idioma del sistema si es necesario.



![language](assets/fr/15.webp)





- Selecciona una distribución de teclado que se adapte a tus preferencias.



![keyboard](assets/fr/16.webp)





- Elige tu zona horaria escribiendo el nombre de tu ciudad en la barra de búsqueda y, a continuación, haz clic en la sugerencia correspondiente.



![timezone](assets/fr/17.webp)





 - Habilite o deshabilite el acceso a su posición para las aplicaciones que lo necesiten, así como el envío automático de informes de errores.



![location](assets/fr/18.webp)





- Decida si desea habilitar repositorios de software de terceros.



![logs](assets/fr/19.webp)





- Introduzca su nombre completo y defina un nombre de usuario para su cuenta.



![name](assets/fr/20.webp)





- Crea una contraseña segura para tu sesión: lo más larga posible (mínimo 20 caracteres), lo más aleatoria posible y con variedad de caracteres (minúsculas, mayúsculas, números y símbolos). Recuerda guardar tu contraseña.



![mdp](assets/fr/21.webp)



Una vez completados todos estos pasos, inicie Fedora y comience a utilizarlo inmediatamente, sin necesidad de reiniciar.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Una vez completada la instalación, puedes consultar tu Interface doméstica con algunas utilidades preinstaladas.



![install-now](assets/fr/09.webp)



## Descubra las tareas básicas



### Navegar por Internet


El navegador por defecto de Fedora es **Firefox**. Es fácil de usar y adecuado para la mayoría de las necesidades.


Si prefieres otro navegador, puedes instalarlo desde el **gestor de software** o a través del **terminal**.


### Tratamiento de textos


Fedora incluye por defecto la suite ofimática **LibreOffice**, que ofrece varias herramientas útiles:




- Writer** para el tratamiento de textos.
- Calc** para hojas de cálculo.
- Impress** para crear presentaciones.


## Instalación de aplicaciones


Para instalar nuevas aplicaciones, puede utilizar el **gestor de software** de Fedora (llamado _Software_), que hace que la instalación sea fácil y visual.  Sin embargo, usar el **terminal** suele ser más rápido y preciso.



Antes de instalar cualquier software, recuerda siempre actualizar los **repositorios** para asegurarte de que tienes acceso a las últimas versiones disponibles.



A continuación, utilice el siguiente comando para iniciar la instalación de la aplicación deseada:


sudo dnf install nombre_del_software`


## Actualizar el sistema operativo


Tras la instalación, es importante actualizar Fedora para aprovechar los últimos parches de seguridad y actualizaciones de software.


### Opción 1: A través del gráfico Interface




- Abra Fedora **Configuración**, luego vaya a la sección **Sistema**.
- Haga clic en **Actualización del software**.
- Inicie la descarga de actualizaciones y espere a que finalice el proceso.



Puede ser necesario un **reinicio** una vez instaladas las actualizaciones.


### Opción 2: A través del terminal




- Abre un terminal y empieza por actualizar los **repositorios** para asegurarte de que tienes las últimas versiones de:



```shell
sudo dnf check-update
```





- A continuación, actualice todo el software instalado con el siguiente comando:



```shell
sudo dnf upgrade
```



Ahora tu sistema Fedora está actualizado y listo para usar en todas tus tareas cotidianas. Descubre nuestro tutorial sobre Linux Mint, otra distribución de Linux, y cómo configurar un entorno sano y seguro para tus transacciones Bitcoin.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5