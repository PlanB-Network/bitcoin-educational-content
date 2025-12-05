---
name: Windows 11
description: Instalación automática de Microsoft Windows 11 mediante archivo de configuración
---
![cover](assets/cover.webp)


En este tutorial, aprenderemos a instalar Windows 11 automáticamente utilizando un método distinto al proceso de instalación estándar de Windows.


## Descargar


Lo primero que necesitarás es un archivo de instalación. El lugar más seguro y fiable para descargarlo es directamente desde el sitio web oficial de Microsoft.


Sólo tiene que visitar el enlace que se proporciona a continuación y seguir las instrucciones para descargar el [archivo ISO de Windows 11](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Una vez en la página de descargas, desplázate hasta la sección para descargar el archivo ISO.


![Image](assets/en/01.webp)


َY elija la versión adecuada.


![Image](assets/en/03.webp)


Después de seleccionar Windows 11, haga clic en el botón Confirmar.


En este paso, puede tardar unos segundos en procesar la solicitud y, a continuación, verá la siguiente página:


![Image](assets/en/04.webp)


Tras confirmar la solicitud, debe elegir el idioma que prefiera.


![Image](assets/en/05.webp)


Tras seleccionar el idioma y hacer clic en el botón Confirmar, se procesará la solicitud. Este paso puede tardar unos segundos.


Una vez que la solicitud se haya procesado correctamente, verás una página con el enlace de descarga del archivo .iso. Haga clic en el botón de descarga de 64 bits para iniciar la descarga.


El tamaño del archivo es de unos 5,5 GB, y el enlace generado será válido durante 24 horas.


## ¡Automatización!


En esta etapa, tenemos que hacer cambios en la instalación estándar de Windows. En esta etapa, utilizando la instalación desatendida, determinamos qué elementos se van a instalar, sin la intervención posterior del usuario. De hecho, en este método, se utiliza un archivo XML para configurar los pasos de instalación y los servicios instalados en Windows. En otras palabras, el uso del archivo Unattended.xml crea un proceso de automatización durante la instalación, evitando la necesidad de seleccionar múltiples opciones y evitando los tediosos pasos que normalmente se requieren durante la instalación. Se trata de un método inusual pero estándar que ha sido introducido por Microsoft. Encontrará más información en [el sitio web oficial de Microsoft](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Hay varias herramientas disponibles en Internet para generar archivos desatendidos. Algunas de ellas están en línea, mientras que otras no lo están. Una de las herramientas en línea para crear este archivo es [este sitio web](https://schneegans.de/windows/unattend-generator). Tras abrirla, se nos presenta la siguiente página:


![Image](assets/en/06.webp)


Como se menciona en la parte superior de la página, este método se puede utilizar para instalar Windows 10 y 11. En el primer paso, seleccionamos el idioma de Windows. Si necesitamos añadir un segundo o incluso un tercer idioma a la lista de idiomas de pantalla y teclado de Windows, podemos utilizar el cuadro de abajo:


![Image](assets/en/07.webp)


En el siguiente paso, seleccionamos la ubicación deseada.


![Image](assets/en/08.webp)


En esta fase, también podemos especificar la arquitectura del procesador del ordenador. En este paso, podemos:

1. Decida si ignora las funciones de seguridad de Windows, como TPM y Secure Boot. La función de arranque seguro garantiza que si se manipula algún archivo principal de Windows durante el proceso de arranque, se detecta el problema y se impide su ejecución. Esta función también ayuda a proteger el sistema frente a la instalación de actualizaciones maliciosas en Windows. Activar la opción para evitar estas características es a veces inevitable en algunos ordenadores, especialmente en los modelos más antiguos. Sin embargo, en general se recomienda mantener activadas características como Secure Boot.

2. Ignora el requisito de conexión a Internet para completar el proceso. Esto es útil en situaciones en las que no se dispone de una conexión LAN por cable, ya que en la mayoría de los casos, la tarjeta inalámbrica aún no se reconoce durante la instalación de Windows, y se requiere acceso a Internet por cable. Activando esta opción se resuelven los problemas relacionados con este paso.


En el siguiente paso, podemos elegir un nombre para el ordenador.


![Image](assets/en/09.webp)


También podemos permitir que Windows elija un nombre para el sistema. En este paso, podemos seleccionar el tipo de Windows, si comprimido o sin comprimir, o dejar que Windows determine la versión adecuada en función de las especificaciones del ordenador. En este paso también se puede establecer la zona horaria.


El siguiente paso consiste en configurar la partición:


![Image](assets/en/10.webp)


En esta fase, podemos especificar el tipo de partición para instalar Windows, así como la configuración necesaria para instalar el Entorno de recuperación de Windows. Al seleccionar la primera opción, la selección de la partición y el particionamiento se posponen hasta el momento de la instalación de Windows, y durante la instalación, estas preguntas se harán igual que en el método de instalación normal.


En este paso, seleccionamos la versión de Windows a instalar:


![Image](assets/en/11.webp)


Si dispone de una clave de producto, también puede introducirla en esta fase.


El siguiente paso consiste en configurar la cuenta de inicio de sesión de Windows:


![Image](assets/en/12.webp)


## Reuniones contables


En esta etapa:


1. Podemos definir un nombre y una contraseña para la cuenta de administrador. También es posible crear varias cuentas de usuario o de administrador.

2. Aquí se especifica con qué cuenta se debe iniciar sesión la primera vez tras la instalación de Windows. Las diferentes opciones para esta sección se muestran en la imagen.

3. Si no desea que se cree ninguna cuenta, limpie todas las cuentas y seleccione esta opción. En este caso, tras la instalación de Windows, iniciará sesión automáticamente en la cuenta de administrador de Windows.


El siguiente paso consiste en configurar la contraseña y el archivo host:


![Image](assets/en/13.webp)


En esta etapa, determinamos si las contraseñas deben tener un período de caducidad. Además, esta sección incluye ajustes de seguridad relacionados con los intentos fallidos de inicio de sesión, que pueden activarse o desactivarse en función de sus necesidades.


Al final de esta sección, hay opciones para la visualización de archivos. Ninguna de estas opciones está disponible durante una instalación estándar de Windows y deben configurarse después de la instalación. En cambio, con el método de instalación desatendida, estos ajustes son fácilmente accesibles.


El siguiente paso consiste en configurar los parámetros de seguridad de Windows:


![Image](assets/en/14.webp)


## Ajustes de seguridad


En esta etapa:


1. Windows Defender puede activarse o desactivarse. Esta característica actúa como un software de seguridad en Windows y ayuda a prevenir la ejecución de archivos maliciosos, ciertos ataques de red y más.

2. Es posible desactivar las actualizaciones automáticas de Windows. Este es uno de los problemas más comunes a los que se enfrentan los usuarios de Windows

3. Esta sección permite activar o desactivar UAC (Control de Cuentas de Usuario). Esta función impide que se ejecuten aplicaciones sospechosas con permisos elevados de lectura y escritura.

4. Windows utiliza esta función para detectar software potencialmente dañino.

5. Active o desactive la compatibilidad con rutas largas en aplicaciones de Windows, como PowerShell y otras.

6. Activa o desactiva Escritorio Remoto para acceder al sistema de forma remota.


Dependiendo de la versión de Windows que se utilice, algunas de estas funciones pueden ser compatibles o no.


El siguiente paso consiste en configurar los iconos:


![Image](assets/en/15.webp)


En esta sección:


1. Se enumeran los iconos del escritorio, que pueden añadirse o eliminarse según sea necesario.

2. Se enumeran los iconos del menú Inicio, que también pueden añadirse o eliminarse en función de las necesidades.

3. Esta sección permite configurar si se instalan o no herramientas relacionadas con la virtualización. Esta opción es específica de Windows 11 y no se aplica a Windows 10.


El siguiente paso consiste en configurar los ajustes Wi-Fi:


![Image](assets/en/16.webp)


En esta sección se pueden configurar los ajustes de la red Wi-Fi. Como se ha mencionado anteriormente, en la mayoría de los casos, la tarjeta Wi-Fi no se reconoce durante la instalación de Windows, por lo que la conexión durante la configuración no suele ser posible. Sin embargo, configurando esta sección, si se detecta la tarjeta inalámbrica, el sistema puede conectarse a Internet.


El siguiente paso implica un ajuste importante:


![Image](assets/en/17.webp)


En esta sección, especificamos si la información sobre problemas del sistema debe enviarse a Microsoft o no.


El siguiente paso consiste en configurar las aplicaciones por defecto:


![Image](assets/en/18.webp)


## Activación/desactivación del software por defecto


En esta sección, podemos elegir cualquier aplicación que no queramos que se instale por defecto. Por ejemplo, podemos optar por no instalar Cortana o Copilot.


El siguiente paso implica la configuración de seguridad relacionada con la ejecución de la aplicación:


![Image](assets/en/19.webp)


Aplicando la configuración WDAC, se puede impedir la ejecución de determinadas aplicaciones.


Por último, tras aplicar los ajustes deseados, puede descargarse el archivo XML generado:


![Image](assets/en/20.webp)


Al hacer clic en Descargar archivo XML, se descarga el archivo autounattend.xml. Para utilizar este archivo, basta con montar la ISO descargada en una unidad USB, colocar el archivo autounattend.xml en el directorio raíz y proceder a la instalación de Windows.


Una de las herramientas disponibles para crear una unidad USB de arranque es Rufus. Rufus puede hacer una unidad flash de arranque de instalación de Windows, con un determinado archivo ISO de instalación de Windows. Es rápido y sencillo, puedes descargarlo [aquí](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


En este software, tras seleccionar la unidad USB deseada y el archivo ISO adecuado, hacemos clic en Inicio.


![Image](assets/en/22.webp)


En esta fase, desactivamos todas las opciones, ya que tenerlas activadas puede causar conflictos al utilizar el archivo Unattend generado. Una vez copiados los archivos en la unidad USB, colocamos el archivo autounattend.xml en el directorio raíz:


![Image](assets/en/23.webp)


En este punto, la unidad USB está lista para su uso para instalar Windows automáticamente, y la instalación se puede iniciar utilizando esta unidad.


## Edición ISO


Si necesita instalar Windows en una máquina virtual, puede utilizar software para crear y editar archivos ISO. Uno de estos programas es AnyBurn. Después de extraer el contenido del archivo ISO descargado del sitio web de Microsoft, coloque el archivo autounattend.xml en el directorio raíz. A continuación, utilizando AnyBurn, crea una nueva ISO con los contenidos actualizados.


AnyBurn es un software multifuncional para trabajar con archivos ISO. Ofrece varias funciones para manejar archivos ISO, una de las cuales es la creación de imágenes ISO de arranque; [aquí](https://www.anyburn.com/download.php) es el sitio web original.


En la página principal del software, seleccione "Crear imagen a partir de archivo/carpeta":


![Image](assets/en/24.webp)


En la página siguiente, seleccione todos los archivos extraídos de la ISO junto con el archivo autounattend.xml.


![Image](assets/en/25.webp)


En este paso, configuramos los ajustes para que el archivo ISO sea arrancable:


![Image](assets/en/26.webp)


En esta fase, debe establecerse la ruta del archivo bootfix.bin para que la ISO sea arrancable. Este archivo se encuentra en la raíz de la ISO, dentro de la carpeta de arranque. También se recomienda activar las opciones ISO9660 y UDF en la sección Propiedades.


![Image](assets/en/27.webp)


Después de este paso, al hacer clic en Siguiente se creará el archivo ISO. Este archivo se puede utilizar en software de virtualización como Oracle VirtualBox. A continuación encontrará un tutorial sobre VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65