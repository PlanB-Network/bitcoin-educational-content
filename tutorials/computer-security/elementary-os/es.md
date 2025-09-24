---
name: Elementary OS
description: El sustituto ideal de Windows y MacOS
---

![cover](assets/cover.webp)



Elementary OS es un sistema operativo basado en Ubuntu, diseñado para ser sencillo, rápido y estable para muchos usos cotidianos. Representa una alternativa Linux equilibrada a MacOS y Windows. Su gráfica fluida, intuitiva y despejada hace que sea fácil de aprender, incluso para los principiantes. También se centra en la ergonomía, la seguridad y el rendimiento.



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Por qué elegir Elementary OS





- **Simplicidad y facilidad de uso**: El Interface gráfico de Elementary OS está a medio camino entre los de MacOs y Windows. Esta familiaridad facilita su adopción, incluso para usuarios inexpertos.





- **Seguridad**: Como la mayoría de las distribuciones Linux, Elementary OS se beneficia de un alto nivel de seguridad. Las actualizaciones periódicas, la gestión de derechos y la ausencia de virus comunes lo convierten en un sistema fiable.





- **Rapidez**: Elementary OS es una distribución ligera. Requiere pocos recursos, por lo que es rápida y adecuada para ordenadores con configuraciones modestas.





- **Gratuito**: El sistema es completamente gratuito. Sin embargo, al descargarlo, puedes hacer una donación para apoyar a los desarrolladores.





- **Comunidad activa**: La comunidad en torno a Elementary OS es diversa y receptiva. Si te encuentras con dificultades, puedes encontrar ayuda fácilmente en los foros o en las redes sociales.



## Instalación y configuración


### Requisitos de hardware



Antes de iniciar la instalación, asegúrese de que dispone del siguiente equipo:





- Una **llave USB** de al menos 12 GB
- **Memoria RAM** de al menos 4 GB
- Un disco **Hard de 20 GB** o más para un uso cómodo



## Descargar imagen ISO



Visita el sitio web oficial del sistema operativo [elementary](https://elementary.io/) y elige una cantidad para apoyar el proyecto. Este paso es opcional.


Si desea descargar gratuitamente la imagen ISO, introduzca 0 en el campo **"Otros "** e inicie la descarga de la imagen ISO del sistema.



![0_01](assets/fr/01.webp)



## Crear una llave USB de arranque



Una vez descargada la imagen ISO, tendrás que hacerla arrancar en una llave USB para proceder a la instalación.



Descargue un programa como [Balena Etcher](https://etcher.balena.io/) o una herramienta similar e inícielo.


Selecciona la imagen ISO de **Elementary OS** previamente descargada y establece tu llave USB como destino.



Haga clic en el botón **flash** para iniciar el proceso y espere a que finalice antes de retirar la llave USB.



![0_02](assets/fr/02.webp)



## Arranque con llave y acceso a la BIOS



Apague el ordenador en el que desea instalar Elementary OS y, a continuación, conecte la llave USB.


Cuando arranque el ordenador, accede a la BIOS (`ESC`, `F9` o `F11` según la marca) y selecciona la llave USB como dispositivo de arranque, después pulsa `Enter` para iniciar el proceso de arranque.



## Instalación del sistema operativo elemental



La instalación se inicia automáticamente si la llave USB está correctamente configurada.



### Selección de idioma



Seleccione el idioma en el que desea instalar el sistema. También puede elegir una variante regional.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### Disposición del teclado



Seleccione la disposición correspondiente a su teclado. Se proporciona un campo para comprobar que las teclas producen los caracteres correctos.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### Modo de prueba



El SO Elemental le permite probar el sistema antes de instalarlo. Este modo le permite explorar Interface sin modificar nada en su disco Hard.



### Iniciar la instalación





- Haga clic en **"Borrar disco e instalar "** para instalar directamente en todo el disco.
- Haga clic en **"Instalación personalizada "** si desea gestionar las particiones manualmente.



![0_07](assets/fr/07.webp)



### Selección de discos



Seleccione el disco en el que se va a instalar Elementary OS y, a continuación, haga clic en el botón Continuar.



![0_08](assets/fr/08.webp)



### Cifrado de disco



Una opción te permite encriptar el disco para **proteger tus datos**. Tendrás que establecer una contraseña segura para activar esta protección. Sin embargo, es opcional.



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### Iniciar la instalación



Antes de iniciar la instalación, puede autorizar la instalación automática de controladores de hardware adicionales, en función de la compatibilidad de su máquina.





- Haga clic en "Borrar e instalar" para iniciar la instalación.
- Espere a que finalice el proceso.



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### Reinicie



Una vez que haya terminado, haga clic en el botón **enter** para reiniciar y, a continuación, retire la llave USB en el momento oportuno para evitar que se reinicie la instalación.



![0_13](assets/fr/13.webp)



## Configuración tras la instalación



Después de reiniciar, se requieren algunos pasos adicionales.



![0_14](assets/fr/14.webp)



### Selección de idioma



Confirme o cambie el idioma del sistema en el inicio de sesión.



![0_15](assets/fr/15.webp)



### Disposición del teclado



Asegúrate de que la distribución del teclado es la que deseas.



![0_16](assets/fr/05.webp)



### Crear una cuenta de usuario



Asocie una cuenta de usuario a su sistema operativo definiendo un nombre de usuario y asegurando después el acceso a sus datos con una contraseña alfanumérica de al menos 20 caracteres y símbolos.



![0_17](assets/fr/17.webp)



### Primera conexión



Cuando te conectas por primera vez, Elementary OS te permite personalizar tu entorno con algunos ajustes básicos.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## Actualización del sistema



Antes de un uso prolongado, es importante actualizar el sistema con los últimos parches.


### Opción 1: Actualización mediante gráficos Interface



Entra en el **AppCenter** y haz clic en el icono de actualización de la esquina superior derecha. Espera a que aparezcan las actualizaciones en la lista y haz clic en **"Actualizar todo "** para iniciar la instalación.



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### Opción 2: Actualización a través del terminal



También puede realizar la actualización desde la línea de comandos a través de su terminal: una opción recomendable por su precisión.



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



Para sus primeras actualizaciones, el sistema operativo requiere su contraseña de usuario y confirmación para actualizar los paquetes de software, incluso en el núcleo elemental.



## Configuración del entorno de trabajo



Elementary OS sólo incluye las herramientas esenciales. Para adaptar tu entorno a tus necesidades, especialmente si eres desarrollador, te recomendamos instalar herramientas adicionales.





- Puede añadir dependencias útiles con el siguiente comando (que deberá adaptar a sus necesidades):



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



Este comando instala **Git**, **Python 3**, **pip**, **herramientas de compilador**, **wget**, **curl**, **zsh**, **make**, **snapd** y **vscode** para preparar un entorno de desarrollo básico.



Elementary OS ya está funcionando en tu máquina. Su filosofía de simplicidad, ligereza y elegancia lo convierte en una excelente opción tanto para uso personal como profesional. Obtendrás un sistema estable, fluido y despejado, listo para ser personalizado según tus preferencias. Ya sea para desarrollo, uso en la oficina o navegación diaria, todo está en su lugar para construir un entorno de trabajo eficiente, intuitivo y agradable. Consulta también nuestro tutorial sobre Fedora, una distribución Linux igualmente sencilla, robusta y modular.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0