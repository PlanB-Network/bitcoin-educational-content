---
name: Debian
description: Una distribución Linux famosa por su estabilidad, robustez y compatibilidad.
---

![cover](assets/cover.webp)



Debian es una distribución GNU/Linux libre, famosa por su robustez y fiabilidad. Su núcleo Linux y todos sus paquetes se prueban rigurosamente para garantizar una estabilidad sólida como una roca y un alto nivel de seguridad. Adecuada tanto para servidores como para estaciones de trabajo, Debian ofrece una experiencia fácil de usar y un amplio catálogo de software. Tanto si busca un sistema seguro para el uso diario como para un entorno de producción, Debian es la elección correcta.



## ¿Por qué elegir Debian?





- Libre y abierto**: Debian es totalmente de código abierto, lo que garantiza la transparencia y la ausencia de costes de licencia.
- Estabilidad y seguridad**: cada versión pasa por un exhaustivo proceso de pruebas, haciendo de Debian una de las distribuciones más fiables y seguras del mercado.
- Comunidad activa**: una amplia comunidad y una extensa documentación están a su disposición para ayudarle siempre que lo necesite.
- Ligero y escalable**: puede instalar Debian en máquinas con recursos modestos manteniendo un buen rendimiento.
- Amplio catálogo de software**: más de 50.000 paquetes oficiales disponibles a través de los repositorios.



## Elija un gráfico Interface



Debian ofrece varios entornos de escritorio que se adaptan a sus necesidades:





- GNOME**: Interface moderno e intuitivo, ideal para principiantes. Ofrece un menú gráfico fluido y fácil de usar para acceder a las aplicaciones.
- XFCE**: ligero y rápido, perfecto para máquinas menos potentes.
- KDE Plasma**: altamente personalizable, con una apariencia similar a Windows.
- Cinnamon**: Interface sencillo y elegante, inspirado en Windows.
- LXDE / LXQt**: ultraligero, adecuado para ordenadores antiguos.
- MATE**: sencillo y clásico, cercano al antiguo GNOME.



💡 Para una experiencia cómoda y fácil de agarrar, **GNOME es muy recomendable**.



## Instalación y configuración de Debian


### Requisitos de hardware



Antes de iniciar la instalación, asegúrese de que dispone del siguiente equipo:





- Llave USB**: 8 GB como mínimo para guardar la imagen ISO de arranque.
- Memoria de acceso aleatorio (RAM)**: 4 GB para una instalación y un funcionamiento sin problemas.
- Espacio en disco**: al menos 15 GB de espacio libre para el sistema y las actualizaciones.



### Descargar



La elección de la imagen de Debian depende de la arquitectura de su procesador:





- AMD64**: descargue la edición "live hybrid" de la lista [download] (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: obtenga la imagen de DVD del sitio web oficial de [Debian] (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Otras arquitecturas**: busque la ISO correspondiente a su arquitectura [aquí](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Crear una llave USB de arranque



Una vez descargada la imagen ISO adecuada, proceda a crear el soporte de instalación:




- Descarga Balena Etcher** desde el [sitio web oficial](https://etcher.balena.io/), luego obtén el binario para tu sistema e instálalo.



![etcher](assets/fr/02.webp)





- Inicie Etcher**: abra el software y seleccione la imagen ISO de Debian previamente descargada.
- Elige la llave USB**: especifica tu llave (8 GB+) como destino.
- Iniciar flash**: pulsa sobre **¡Flash!** y espera a que se complete el proceso.



![flash](assets/fr/03.webp)



Su llave USB ya está lista para empezar a instalar Debian.



## Instalación de Debian en su sistema



### Arranque desde llave USB



Para iniciar la instalación desde la llave USB:




- Apague** completamente el ordenador.
- Reinicie** y acceda a BIOS/UEFI pulsando inmediatamente `ESC`, `F2`, `F11` (o la tecla dedicada dependiendo de su marca).
- En el menú de arranque, **selecciona tu llave USB** como dispositivo de arranque.
- Confirme** con la tecla Intro para iniciar la imagen de Debian: esto le llevará a la pantalla de bienvenida del instalador.



### Iniciar la instalación



Pantalla de inicio:



![starting](assets/fr/04.webp)



Al arrancar desde la memoria USB, la pantalla de bienvenida de Debian ofrece varias opciones:




- Live System**: lanza Debian sin instalarlo, ideal para probar el entorno.
- Start Installer**: inicia la instalación directamente en el disco Hard.
- Opciones de instalación avanzadas**: le da acceso a modos de instalación personalizados.



Para explorar Debian en modo vivo, seleccione **Sistema vivo** y confirme con **Intro**. A continuación, puede iniciar la instalación pulsando **Instalar Debian** en el entorno en vivo.



![system](assets/fr/05.webp)





- Selección de idioma** (opcional)



Seleccione el idioma principal de su sistema Debian de la lista y pulse Aceptar.



![language](assets/fr/06.webp)





- Zona horaria** (GMT)



Elige tu zona geográfica para ajustar automáticamente la fecha y la hora.



![timezone](assets/fr/07.webp)





- Disposición del teclado



Selecciona el idioma y la distribución del teclado. Utilice el campo de prueba integrado para comprobar que cada tecla produce el carácter esperado.



![keyboard](assets/fr/08.webp)



### Partición de discos





- Borrar disco**: si tienes una partición dedicada, esta opción borrará todo su contenido.
- Particionado manual**: elija esta opción para crear, redimensionar o eliminar particiones según sus necesidades.



![disk](assets/fr/09.webp)





- Crear una cuenta de usuario



Introduzca su nombre completo, el nombre de su cuenta y una contraseña segura para garantizar la seguridad de su sesión.



![user](assets/fr/10.webp)





- Resumen de parámetros**



Aparecerá un resumen de sus opciones: compruebe cada elemento y vuelva a modificarlo si es necesario.



![settings](assets/fr/11.webp)





- Iniciar la instalación



Haga clic en **Instalar** para empezar a copiar archivos y configurar el sistema, y espere a que finalice el proceso.



![install](assets/fr/12.webp)





- Reiniciar**



Una vez completada la instalación, reinicie el ordenador para aplicar todas las configuraciones y acceder a su nuevo sistema Debian.



![restart](assets/fr/13.webp)



Al iniciarse, introduzca el nombre de usuario y la contraseña para acceder al sistema.



![login](assets/fr/14.webp)



## Actualización del sistema



Antes de empezar a utilizar tu sistema, es esencial actualizarlo. Esto le permitirá beneficiarse de los últimos parches de software, repositorios actualizados y, en algunos casos, parches de seguridad para el propio sistema operativo.



### Opción 1: Actualización mediante Interface gráfico (GNOME)



Si ha instalado Debian con el entorno de escritorio GNOME, puede realizar las actualizaciones gráficamente. Para ello, abra la aplicación **Software** y vaya a la pestaña **Actualizaciones**. A continuación, pulse sobre **Reiniciar y actualizar** para iniciar el proceso.



### Opción 2: Actualización a través del terminal (recomendada)



Este método ofrece un control más completo. Permite actualizar repositorios, paquetes de software y, si es necesario, el kernel.




- Abra el terminal utilizando el atajo de teclado `Ctrl + Alt + T`.
- Actualice la lista de paquetes disponibles con el siguiente comando:



```shell
sudo apt update
```



Introduzca su contraseña cuando se le solicite (tenga en cuenta que no aparecerá ningún carácter mientras teclea, es normal).





- Para instalar las actualizaciones disponibles:



```shell
sudo apt full-upgrade
```



## Descubra las tareas básicas



### Navegar por Internet



El navegador web por defecto en Debian es **Firefox**. Si prefiere otro navegador, puede instalar otro, siempre que esté disponible en los repositorios de Debian (como Chromium, Brave...).



### Tratamiento de textos



El paquete **LibreOffice** está instalado por defecto en Debian.





- Para escribir documentos, utiliza **LibreOffice Writer**, el equivalente a Microsoft Word.
- Para las hojas de cálculo, **LibreOffice Calc** actúa como alternativa a Excel.
- Por último, **LibreOffice Impress** te permite crear presentaciones, igual que PowerPoint.



## Instalación de aplicaciones



Hay dos formas de instalar aplicaciones en Debian:



### Método gráfico:



Puedes utilizar el **gestor de software** (accesible a través del Interface gráfico) para buscar e instalar aplicaciones fácilmente.



### Método de línea de comandos:



Si la aplicación que buscas no aparece en el Interface gráfico, o si prefieres el terminal, utiliza el siguiente comando:



```shell
sudo apt install <name>
```



Sustituya `<nombre>` por el nombre del paquete. Por ejemplo, para instalar `curl`:



```shell
sudo apt install curl
```



### Instalación de un paquete descargado manualmente:



Si ha descargado un archivo `.deb` (paquete Debian), puede instalarlo con el siguiente comando:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Su sistema Debian está ahora instalado y listo para usar en sus tareas diarias.


Gracias al entorno de escritorio **GNOME**, puedes acceder a una amplia gama de aplicaciones a través de un Interface gráfico fácil de usar, ideal tanto para principiantes como para usuarios avanzados.



También es posible cambiar de entorno de escritorio (por ejemplo, a XFCE, KDE, etc.) sin tener que reinstalar Debian. Para ello, simplemente use el terminal e instale el nuevo entorno de su elección.



Para saber más sobre Debian, y más en general sobre las distribuciones GNU/Linux, le recomiendo que consulte este curso:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1