---
name: PureOS
description: La distribución Linux que te da el control sobre tu vida digital.
---

![cover](assets/cover.webp)



Proteger la información personal en la era digital es una prioridad absoluta para todo usuario de Internet. Empresas, organizaciones e incluso sistemas operativos son fuentes de información útiles para definir tu perfil y estilo de vida. Elegir el sistema operativo adecuado es el primer paso para reforzar tu privacidad online. En este tutorial, echaremos un vistazo a PureOS, una distribución de Linux centrada en la privacidad.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Introducción a PureOS



PureOS es un sistema operativo basado en Debian desarrollado por Purism. PureOS es adecuado tanto para profesionales de TI como para usuarios que buscan una distribución sencilla y fácil de usar. Es único por ser *Software Libre*, y se centra en la protección de los datos personales de sus usuarios estableciendo un marco basado en la privacidad, libertad, seguridad y estabilidad que ofrece Debian.



### ¿Por qué elegir PureOS?





- Interface** sencillo e intuitivo: GNOME ofrece un escritorio Interface claro, diseñado para ser fácil de usar, incluso para personas que no se sienten cómodas con la línea de comandos.





- Gratuito**: como la mayoría de las distribuciones Linux, PureOS es totalmente gratuito. Sin embargo, existe una suscripción mensual para apoyar a los desarrolladores.





- Seguridad y estabilidad**: La arquitectura y el modo operativo de PureOS la convierten en una distribución altamente segura, que garantiza la protección de los datos y la estabilidad del sistema.





- Documentación y comunidad activa**: PureOS cuenta con una documentación clara y accesible y una comunidad comprometida y receptiva, lo que facilita la resolución de problemas y el aprendizaje del sistema paso a paso.



## Instalación y configuración



La instalación y configuración de PureOS en su ordenador requerirá las siguientes características minimalistas:




- Una memoria USB de al menos 8 GB para flashear el sistema.
- 4 GB DE RAM.
- 30 GB de espacio libre en tu disco Hard.



Vaya al [sitio web oficial de PureOS](https://pureos.net/) y descargue la imagen ISO del sistema operativo según la arquitectura de su máquina.



Para iniciar la instalación de PureOS, es necesario crear una llave USB de arranque utilizando un software flash como [Balena Etcher](https://www.balena.io/etcher).



En tres sencillos pasos, tendrás una memoria USB arrancada con el sistema operativo PureOS.





- Conecta la llave USB y ejecuta el software Balena descargado.
- A continuación, seleccione la imagen ISO de PureOS
- Elige la llave USB como dispositivo de salida, haz clic en el botón **Flash** y espera a que termine el proceso.



![0_01](assets/fr/01.webp)



Una vez arrancada la llave USB, reinicie el ordenador en el que desea instalar PureOS.



Al arrancar, acceda a la BIOS pulsando la tecla `ESC`, `F9` o `F11`, dependiendo de su máquina. Seleccione la memoria USB como dispositivo de arranque y pulse `ENTER` para confirmar.



### Pantalla de inicio



PureOS ofrece varias opciones para iniciar su sistema operativo. Elija la opción **Probar o instalar PureOS** para iniciar la instalación del sistema operativo.



![0_02](assets/fr/02.webp)



Configure el idioma y la distribución del teclado que desea utilizar en su ordenador.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Permite o deniega el acceso a tu **localización geográfica** a las aplicaciones para obtener recomendaciones personalizadas basadas en tu zona.



![0_05](assets/fr/05.webp)



Puedes conectarte a tu cuenta existente de **NextCloud** para recuperar datos vinculados a la suite ofimática que estés utilizando en otro sistema.



![0_06](assets/fr/06.webp)



Se ofrece un tutorial, pero puede cerrar la ventana si desea saltarse este paso.



![0_08](assets/fr/08.webp)



### Iniciar la instalación



Haga clic en el menú **Actividades** y explore las aplicaciones y herramientas preinstaladas en el sistema. Haga clic en **Instalar PureOS** para iniciar la instalación



![0_09](assets/fr/09.webp)



Configure el idioma del sistema y la distribución del teclado según sea necesario y, a continuación, configure el modo de partición del disco Hard.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Tiene dos opciones para particionar su disco Hard:




- Borrar disco**: Para una instalación completa de PureOS, borrando todos los datos preexistentes en su disco Hard.



![0_14](assets/fr/14.webp)





- Partición manual** para crear sus propias partituras



⚠️ Cuando cree particiones manualmente para su sistema operativo, asegúrese de asignar una partición de al menos 2 GB para el funcionamiento de PureOS y otra partición para los datos.



![0_15](assets/fr/15.webp)



Activa el **cifrado de disco** si quieres proteger tus datos. Introduce una contraseña fuerte y compleja.



Asocie un usuario a su sistema operativo definiendo un nombre de usuario y una contraseña alfanumérica de al menos 20 caracteres para reforzar la seguridad de sus datos.



![0_16](assets/fr/16.webp)



Revisa los ajustes que has realizado y modifícalos si es necesario.



![0_17](assets/fr/17.webp)



Haga clic en **Instalar** y luego en **Instalar ahora** para confirmar que PureOS se ha instalado en su ordenador.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Una vez finalizada la instalación, marque la casilla **Reiniciar ahora** para reiniciar el ordenador y, a continuación, confirme:




- El idioma.
- Disposición del teclado.
- Tu cuenta NextCloud (opcional).



![0_25](assets/fr/25.webp)



## Actualizaciones



Antes de empezar a utilizar PureOS, es esencial que actualices tu sistema. Así podrás beneficiarte de las últimas funciones y parches de seguridad, además de garantizar una mayor estabilidad.





- Actualización a través del gráfico Interface**:


Abra la aplicación **Software** y vaya a la pestaña **Actualizaciones**. Aparecerán automáticamente las actualizaciones disponibles. Haga clic en **Descargar** y, a continuación, en **Instalar** una vez finalizada la descarga.





- Actualización a través del terminal**:


Abra el terminal e introduzca el siguiente comando para actualizar la lista de paquetes disponibles:



```shell
sudo apt update
```



Introduce tu contraseña y confírmala. A continuación, instale las actualizaciones con:



```shell
sudo apt full-upgrade
```



## PureOS para el desarrollo



Por defecto, PureOS no incluye todas las herramientas necesarias para el desarrollo.


Puede instalarlos rápidamente con el siguiente comando:



```shell
sudo apt install build-essential git curl
```



Esto instalará las herramientas de compilación **Git** y **Curl**, útiles en la mayoría de los entornos de desarrollo.



## Entorno PureOS



PureOS destaca por su innovador enfoque de la convergencia real: un único sistema operativo garantiza un funcionamiento fluido y sin problemas en una gran variedad de dispositivos, como portátiles, tabletas, mini PC y smartphones.



Las aplicaciones PureOS están diseñadas para ser adaptativas: se ajustan automáticamente al tamaño de la pantalla y al modo de entrada (táctil o teclado/ratón). Por ejemplo, el navegador web GNOME adapta dinámicamente su Interface para ofrecer una experiencia óptima tanto en dispositivos móviles como de sobremesa.



PureOS también incluye la suite ofimática **LibreOffice**, que incluye:





- Writer**: un completo procesador de textos para crear y editar documentos.
- Calc**: un potente programa de hoja de cálculo para gestionar tus datos y cálculos.
- Impress**: una herramienta para crear presentaciones profesionales.



Esta suite gratuita te permite trabajar con eficacia sin tener que depender de software propietario.



PureOS ofrece un entorno unificado, seguro y flexible, basado en una distribución 100% de código abierto que garantiza un control total y un estricto respeto de la privacidad. Su auténtica convergencia facilita la creación de aplicaciones compatibles con distintos tipos de dispositivos, como ordenadores, tabletas y smartphones, sin necesidad de complejas adaptaciones.



Con acceso nativo a herramientas esenciales, robustos gestores de paquetes y un rico ecosistema de código abierto, PureOS simplifica el desarrollo, las pruebas y la implantación de aplicaciones en un entorno seguro. Su arquitectura estable y Commitment a la confidencialidad la convierten en una plataforma fiable para una gran variedad de usos, incluidos el desarrollo Blockchain, la creación rápida de prototipos o los entornos de producción.



Descubra nuestro curso para reforzar su seguridad y proteger su privacidad digital.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1