---
name: VirtualBox
description: Instala VirtualBox en Windows 11 y crea tu primera máquina virtual
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian Burnel publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___




## I. Presentación



En este tutorial, aprenderemos a instalar VirtualBox en Windows 11 para crear máquinas virtuales, ya sea para ejecutar Windows 10, Windows 11, Windows Server o una distribución de Linux (Debian, Ubuntu, Kali Linux, etc.).



Este tutorial de introducción a VirtualBox te ayudará a iniciarte en esta solución de virtualización de código abierto desarrollada por Oracle, que es totalmente gratuita. Más adelante, se pondrán en línea otros tutoriales para profundizar en el tema.



Cuando se trata de virtualizar una estación de trabajo, ya sea para realizar pruebas en el marco de un proyecto o durante tus estudios de informática, VirtualBox es claramente una buena solución. También es una alternativa a otras soluciones como Hyper-V, que está integrado en Windows 10 y Windows 11 (así como en Windows Server), y VMware Workstation (de pago) / VMware Workstation Player (gratuito para uso personal).



Mi configuración: **una estación de trabajo Windows 11 donde voy a instalar VirtualBox**, pero puedes instalar VirtualBox en Windows 10 (o una versión anterior), así como en Linux. En cuanto a las máquinas virtuales, VirtualBox es compatible con una amplia gama de sistemas, incluidos Windows (por ejemplo, Windows 10, Windows 11, Windows Server 2022, etc.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, etc.), BSD (PfSense) y macOS.



## II. Descargar VirtualBox para Windows 11



Para descargar VirtualBox para instalarlo en una máquina Windows, sólo hay un buen Address: el [sitio web oficial de VirtualBox](https://www.virtualbox.org/wiki/Downloads) en la sección "**Downloads**". Basta con hacer clic en "Windows hosts" para empezar a descargar este ejecutable, que ocupa poco más de 100 MB.



![Image](assets/fr/025.webp)



## III. Instalación de VirtualBox en Windows 11



### A. Instalación de VirtualBox



La instalación de VirtualBox** es sencilla, y el proceso es el mismo para todas las versiones de Windows. Comienza ejecutando el ejecutable de VirtualBox que acabas de descargar y haz clic en "**Siguiente**".



![Image](assets/fr/026.webp)



Esta instalación es personalizable, pero le recomiendo que instale todas las características: que es el caso de la selección por defecto. En la imagen de abajo, puedes ver varios Elements, incluyendo :





- Soporte USB de VirtualBox** para que VirtualBox admita dispositivos USB
- VirtualBox Bridged Network** para integrar el soporte de red en modo "Bridge" (la máquina virtual puede conectarse directamente a su red local)
- VirtualBox Host-Only Network** para integrar soporte de red en modo "Host-Only" (la máquina virtual sólo puede comunicarse con su host físico Windows 11 y otras máquinas virtuales en este modo)



Pulse "**Siguiente**" para continuar.



![Image](assets/fr/001.webp)



Haga clic en "**Sí**", teniendo en cuenta que **la red se interrumpirá por un momento en su máquina Windows 11**, mientras VirtualBox realiza modificaciones de red para soportar diferentes tipos de red, incluyendo el modo Bridge.



![Image](assets/fr/002.webp)



Una vez que lo hayas confirmado, comenzará la instalación... Y aparecerá una notificación "**¿Desea instalar el software de este dispositivo?**". Marca la opción "**Confiar siempre en el software de Oracle Corporation**" y haz clic en "**Instalar**". En realidad, VirtualBox necesita instalar varios controladores en tu ordenador.



![Image](assets/fr/003.webp)



La instalación ha finalizado Marque la opción "**Iniciar Oracle VM VirtualBox 6.1.34 tras la instalación**" y haga clic en "**Clic**" para iniciar el software.



![Image](assets/fr/004.webp)



### B. Añadir el paquete de ampliación



Siempre en el sitio oficial de VirtualBox (ver enlace anterior), puede descargar un paquete de extensión oficial, accesible en la sección "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" haciendo clic en el enlace "**Todas las plataformas soportadas**". Este paquete te permitirá añadir funcionalidades adicionales a VirtualBox: no es obligatorio añadirlo, ¡pero puede ser útil! Por ejemplo, incluye soporte para USB 3.0 en VMs, soporte para webcam y encriptación de disco.



Abre VirtualBox, haz clic en "**Archivo**" y luego en "**Configuración**" en el menú.



![Image](assets/fr/005.webp)



Haz clic en "**Extensiones**" a la izquierda (1) y, a continuación, en el botón "**+**" a la derecha (2) para **cargar el paquete de extensiones de VirtualBox** que acabas de descargar (3).



![Image](assets/fr/006.webp)



Confirme pulsando el botón "**Instalación**".



![Image](assets/fr/007.webp)



Haga clic en "**OK**": ¡el paquete de extensión oficial ya está instalado en su instancia de VirtualBox!



![Image](assets/fr/008.webp)



Pasemos a la creación de nuestra primera máquina virtual.



## IV. Creación de la primera máquina virtual VirtualBox



Para crear una nueva máquina virtual en VirtualBox, basta con hacer clic en el botón "**Nueva**" para iniciar el asistente de creación de máquinas virtuales. Como es la primera vez que inicias VirtualBox, me gustaría darte algunos detalles más sobre Interface y los demás botones.





- Configuración**: configuración general de VirtualBox (carpeta VM por defecto, gestión de actualizaciones, idioma, redes NAT, extensiones, etc.)
- Importar**: importar un dispositivo virtual en formato OVF
- Exportar**: exportar una máquina virtual existente en formato OVF para crear un dispositivo virtual
- Añadir**: añadir una máquina virtual existente al inventario de VirtualBox, en formato estándar de VirtualBox (.vbox) o en formato XML



A la izquierda, la sección "**Herramientas**" da acceso a **funciones avanzadas, especialmente para gestionar la red virtual, pero también para gestionar el almacenamiento de las máquinas virtuales**. En la entrada "**Herramientas**" se añadirán más tarde sus máquinas virtuales.



![Image](assets/fr/009.webp)



### A. Proceso de creación de máquinas virtuales



**Como recordatorio, VirtualBox soporta multitud de sistemas operativos, incluyendo Windows, Linux y BSD. En este ejemplo, voy a crear una máquina virtual para Windows 11. Hay que rellenar varios campos:





- Nombre**: nombre de la máquina virtual (es el nombre que se mostrará en VirtualBox)
- Carpeta de la máquina**: dónde almacenar la máquina virtual, sabiendo que en esta ubicación se creará una subcarpeta con el nombre de la VM
- Tipo**: el tipo de sistema operativo, en función del SO que desee instalar
- Versión**: la versión del sistema que desea instalar, en este caso Windows 11, por lo que "**Windows11_64**"



Pulse "**Siguiente**" para continuar.



![Image](assets/fr/010.webp)



Dependiendo del sistema operativo que selecciones en el paso anterior, **VirtualBox hace recomendaciones sobre los recursos a asignar a la máquina virtual**. Aquí, estamos hablando de la memoria RAM que desea asignar a la máquina virtual. Vamos a suponer 4 GB, porque es lo que se recomienda para Windows 11, pero si tienes pocos recursos, especifica 2 GB. **Continuar



**Nota**: los recursos asignados a la máquina virtual pueden modificarse posteriormente.



![Image](assets/fr/011.webp)



En cuanto al disco virtual Hard, partimos de cero, por lo que debemos elegir "**Crear disco virtual Hard ahora**" para que la VM disponga de espacio de almacenamiento para instalar el sistema operativo y almacenar datos. Haz clic en "**Crear**".



![Image](assets/fr/012.webp)



VirtualBox admite tres formatos diferentes para los discos virtuales Hard, lo que supone una gran diferencia con respecto a otras soluciones como VMware e Hyper-V. Hay tres formatos para elegir:





- VDI**, el formato oficial de VirtualBox
- VHD**, que es el formato oficial de Hyper-V, aunque actualmente se utiliza más el nuevo formato VHDX
- VMDX** es el formato oficial de VMware tanto para VMware Workstation como para VMware ESXi



Para crear una máquina virtual que sólo se utilizará en esta instancia de VirtualBox, elija "**VDI**". Por otro lado, si el disco virtual Hard se va a conectar a un host Hyper-V más adelante, puede ser una buena idea empezar con el formato VHD para evitar tener que convertirlo. Haga clic en "**Siguiente**".



![Image](assets/fr/013.webp)



**El disco virtual puede ser dinámico o de tamaño fijo**. Cuando es dinámico, el archivo que representa **el disco virtual (aquí un archivo .vdi) crecerá a medida que se escriban datos en el disco** hasta alcanzar su tamaño máximo, pero no se reducirá si se borran datos. Por el contrario, cuando es de tamaño fijo, **el espacio total de almacenamiento se asigna inmediatamente (y, por tanto, se reserva)**, lo que permite un rendimiento ligeramente superior, pero tarda más cuando el disco virtual se crea por primera vez.



Personalmente, para las máquinas virtuales de prueba con VirtualBox, considero que el modo "**Asignado dinámicamente**" es suficiente.



![Image](assets/fr/014.webp)



**El siguiente paso es especificar el tamaño del disco virtual**, teniendo en cuenta que por defecto, el disco se almacenará en el directorio de la VM (esto se puede cambiar en esta etapa). He indicado un tamaño de 64 GB para cumplir con los requisitos de Windows 11, pero también en este caso se podría asignar un tamaño menor. Haz clic en "**Crear**" para crear la VM



![Image](assets/fr/015.webp)



En este punto, la máquina virtual está en nuestro inventario, está configurada, pero el sistema operativo no está instalado. Tenemos que finalizar la configuración de la máquina virtual antes de iniciarla.



### B. Asignación de una imagen ISO a una máquina virtual VirtualBox



Para instalar Windows 11, o cualquier otro sistema, necesitamos fuentes de instalación. En la mayoría de los casos, utilizamos una imagen de disco en formato ISO para instalar un sistema operativo. **Es necesario cargar la imagen ISO de Windows 11 en la unidad de DVD virtual de nuestra VM



Haga clic en la máquina virtual en el inventario de VirtualBox (1) y, a continuación, en el botón "**Configuración**" (2), que da acceso a la configuración general de esta máquina virtual. Este menú permite gestionar los recursos (por ejemplo, aumentar la RAM, configurar la CPU, etc.). Haga clic en "**Almacenamiento**" a la izquierda (3), en la unidad de DVD donde dice "**Vacío**" por el momento (4) luego haga clic en el icono con forma de DVD (5) y "**Elija un archivo de disco**".



![Image](assets/fr/016.webp)



Seleccione la imagen ISO del sistema operativo que desea instalar y, a continuación, haga clic en Aceptar. Esto es lo que obtengo:



![Image](assets/fr/017.webp)



Quédate en la sección "**Configuración**" de la VM, aún me quedan algunas cosas por explicar.



### C. Conexión de red VM



Vaya a la sección "**Red**" a la izquierda. Esta sección le permite gestionar la red de la máquina virtual: número de interfaces de red virtuales (hasta 4 por VM), MAC Address y modo de acceso a la red (NAT, acceso puente, red interna, etc.). **Si quieres que tu máquina virtual tenga acceso a Internet, selecciona "NAT" o "Bridge Access "**, pero este segundo modo requiere que haya un servidor DHCP activo en tu red, o tendrás que configurar una IP Address manualmente.



Nota: Volveré sobre la parte de la red con más detalle en un artículo específico.



![Image](assets/fr/018.webp)



### D. El número de procesadores virtuales



Al igual que un ordenador físico, una máquina virtual necesita RAM, un disco Hard y un procesador para funcionar. Cuando creamos la máquina virtual, te habrás dado cuenta de que el asistente no incluía la configuración del procesador. Sin embargo, esto se puede configurar en cualquier momento a través de la pestaña "**Sistema**", luego "**Procesador**", donde puedes elegir el número de procesadores virtuales.



Nota: la opción "**Habilitar VT-x/AMD-v anidado**" es necesaria para la virtualización anidada.



En mi caso, la máquina virtual tiene 2 procesadores virtuales:



![Image](assets/fr/019.webp)



**No dudes en echar un vistazo a las demás secciones del menú de configuración.



### E. Primer arranque e instalación del SO



Para iniciar una máquina virtual, basta con seleccionarla en el inventario y pulsar el botón "**Iniciar**". Se abrirá una segunda ventana que ofrecerá una visión general de la máquina virtual.



![Image](assets/fr/020.webp)



Ouch, ¡me sale un error desagradable y mi máquina virtual no arranca! El error es "Login failed for virtual machine..." con los siguientes detalles:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



¡De hecho, esto es normal porque **la función de virtualización no está activada en mi ordenador**! Para corregir este problema, necesitas reiniciar tu ordenador para acceder a la BIOS y habilitar la virtualización.



![Image](assets/fr/021.webp)



Sin esperar, reinicio mi ordenador y **presiono la tecla "SUPPR" para acceder a la BIOS** (la tecla puede variar según la máquina, y podría ser F2, por ejemplo) de mi placa base ASUS. Para activar la virtualización, en mi caso hay que activar el "Modo SVM". Aquí también, de una placa base a otra, de un fabricante a otro, el nombre puede cambiar. Busca una función que haga referencia a **AMD-V** (para una CPU AMD) o **Intel VT-x** (para una CPU Intel).



![Image](assets/fr/022.webp)



Una vez hecho esto, guarda la modificación y reinicia la máquina física.... Esta vez, **VirtualBox puede arrancar la máquina virtual** y cargar la imagen ISO de Windows para instalar el sistema operativo! 🙂 ..



![Image](assets/fr/023.webp)



En nuestro host físico de Windows 11, donde está instalado VirtualBox, podemos ver que la carpeta de la máquina virtual de Windows 11 contiene varios archivos.





- El archivo VBOX** (en formato XML) correspondiente a la configuración de la VM (RAM, CPU, etc.)
- El archivo VBOX-PREV** es una copia de seguridad de la configuración anterior
- El archivo VDI** corresponde al disco virtual Hard en modo dinámico, por lo que actualmente sólo ocupa 13 GB, mientras que su tamaño máximo es de 64 GB
- El archivo NVRAM** contiene el estado de la BIOS de la máquina virtual, que equivale a la memoria no volátil de una máquina física



![Image](assets/fr/024.webp)



## V. Conclusión



**¡VirtualBox ya está funcionando en nuestra máquina física con Windows 11! Ya volveré a hablar de la instalación de Windows 11 en una máquina virtual VirtualBox en otro artículo. Para Windows 10, Windows Server o una distribución Linux (Ubuntu, Debian, etc.), ¡simplemente déjate guiar!