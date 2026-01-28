---
name: Qubes
description: Un sistema operativo razonablemente seguro.
---

![cover](assets/cover.webp)



Qubes OS es un sistema operativo gratuito y de código abierto diseñado para usuarios que sitúan la seguridad entre sus principales prioridades. Su particularidad se basa en una idea sencilla pero radical: en lugar de considerar el ordenador como un todo, divide su uso en compartimentos independientes llamados **_qubes_**.



Cada qube funciona como un **entorno virtual aislado**, con un nivel de confianza y una función específicos. Así, aunque una aplicación se vea comprometida, el ataque queda confinado a su qube sin afectar al resto del sistema.



> Si te tomas en serio la seguridad, Qubes OS es el mejor sistema operativo disponible hoy en día. - **Edward Snowden**.

Sin embargo, instalar Qubes OS requiere más preparación que instalar un sistema operativo convencional. Implica comprobar ciertos requisitos previos de hardware, comprender los fundamentos de la virtualización y aceptar una experiencia diferente, en la que cada tarea cotidiana se plantea en términos de separación. Pero una vez instalado, Qubes OS ofrece un marco robusto que redefine la forma en que interactúas con tu ordenador a diario. En este tutorial, te explicaremos cómo funciona Qubes OS y cómo instalarlo fácilmente en tu sistema.



## ¿Cómo funciona Qubes OS?



Qubes OS se basa en el principio de compartimentación. En lugar de utilizar un único sistema, se basa en el hipervisor **Xen** para crear máquinas virtuales aisladas, llamadas qubes. Cada qube se dedica a una tarea específica o a un nivel de confianza (trabajo, navegación personal, banca, etc.). Esta separación garantiza que cualquier compromiso en una qube no pueda propagarse a las demás, actuando como varios ordenadores independientes dentro de una única máquina.



El usuario Interface es gestionado por un dominio central y seguro llamado **dom0**. Este dominio está totalmente aislado de Internet, lo que lo convierte en el corazón del sistema. Aunque las ventanas y menús son mostrados por dom0, la ejecución real de las aplicaciones tiene lugar en sus respectivos qubes.



## Los distintos tipos de qubes



En torno a dom0 giran distintos tipos de qubes, cada uno con un papel muy específico.





- Las **AppVM** se utilizan para ejecutar aplicaciones cotidianas: el usuario puede así separar sus correos electrónicos profesionales de su navegación por Internet o sus actividades bancarias, permaneciendo cada entorno totalmente independiente de los demás.





- Estas AppVMs se basan a su vez en **TemplateVMs**, que sirven como plantillas centralizadas para instalar y actualizar software, eliminando la necesidad de gestionar cada qube por separado.



Qubes OS también integra máquinas virtuales especializadas en **servicios del sistema**.





- Las **NetVM** gestionan directamente los **dispositivos de red** y garantizan la conexión a Internet. A menudo están asociadas a **FirewallVM**, que intervienen para **filtrar el tráfico** y limitar la exposición de otros qubes.





- Las ServiceVM desempeñan un papel similar, por ejemplo en la gestión de dispositivos USB, siempre con la misma lógica: aislar los componentes más arriesgados para reducir la superficie de ataque.



Por último, para tareas ocasionales o arriesgadas, Qubes OS ofrece **VM desechables**. Estos qubes efímeros se crean sobre la marcha para **abrir un documento sospechoso** o **visitar un sitio dudoso**, y luego desaparecen por completo al cerrarse, borrando todos los rastros y evitando cualquier ataque persistente.



### El mecanismo de copia segura (qrexec)



Los intercambios entre qubes se basan en **qrexec**, un sistema de comunicación inter-VM diseñado para la seguridad. En lugar de dejar que las qubes se comuniquen libremente, qrexec impone **políticas específicas**: un archivo copiado de una AppVM a otra, o un texto transferido a través del portapapeles, pasa siempre por un canal supervisado y validado por el sistema. De este modo, incluso el simple acto de copiar y pegar se controla para evitar la propagación de malware.



### Gestión de discos



Qubes OS utiliza un ingenioso sistema para la gestión del almacenamiento. Las TemplateVM contienen la base de software común, mientras que las AppVM añaden sólo sus datos personales y archivos específicos. Esto reduce el uso de espacio en disco y facilita las actualizaciones globales. Las DisposableVMs, por su parte, utilizan volúmenes temporales que desaparecen por completo al cerrarse. Este modelo no sólo garantiza una mayor seguridad, sino también una gestión eficaz de los recursos.



## ¿Por qué elegir Qubes OS?



Las ventajas de Qubes OS residen sobre todo en su modelo de seguridad único. En el corazón de este enfoque está la compartimentación, que protege al usuario aislando cada tarea en máquinas virtuales separadas. En la práctica, un correo electrónico infectado o un sitio web malicioso sólo pueden comprometer un único qube, dejando el resto del sistema y sus datos personales totalmente protegidos. Esta arquitectura limita considerablemente los ataques complejos que, en un sistema convencional, podrían propagarse libremente.



Qubes OS también ofrece total transparencia y control sobre tu entorno digital. Sabes exactamente qué software tiene acceso a qué recurso, ya sea la red, un dispositivo USB u otros componentes sensibles. El sistema integra por defecto funciones de seguridad avanzadas, como el cifrado completo del disco, y facilita el uso de servicios de anonimización como el sistema operativo Whonix.



https://planb.academy/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

En lugar de tratar de crear un sistema impenetrable, Qubes OS se centra en la resiliencia: encapsula los daños en caso de compromiso, reduciendo el riesgo para el resto del sistema. Este enfoque pragmático convierte a Qubes OS en la opción preferida de los usuarios con grandes necesidades de seguridad o que desean mantener el máximo control sobre su vida digital.



## Instalación de Qubes OS



Antes de instalar Qubes OS, es esencial que te asegures de que tu hardware cumple los requisitos mínimos, ya que el sistema se basa en la virtualización para aislar los qubes. Los principales componentes a comprobar son :




- El **Procesador**: Un procesador de 64 bits compatible con la virtualización por hardware (Intel VT-x o AMD-V).
- RAM: se requiere un mínimo de 8 GB, pero recomendamos una RAM de 16 GB o más para ejecutar varios qubes simultáneamente.
- **Espacio de almacenamiento**: un mínimo de 36 GB, idealmente 128 GB en un SSD para un rendimiento óptimo.



Para instalar Qubes OS, descarga la imagen ISO oficial desde Qubes OS [sitio oficial](https://www.qubes-os.org/downloads/). Es esencial comprobar la integridad de la ISO utilizando las firmas GPG proporcionadas, para garantizar que el archivo no ha sido manipulado y que la descarga es segura.



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Una vez verificada la ISO, tienes que crear un medio de instalación de arranque, normalmente una memoria USB. Para ello, descarga e instala software como **Rufus** en Windows o **Etcher** en Windows, Linux o macOS. Estas herramientas te permiten copiar la ISO en la memoria USB para que sea arrancable.



Antes de comenzar la instalación, es necesario configurar la **BIOS o UEFI** de su ordenador para **habilitar la virtualización** y permitir el arranque desde USB. Dependiendo del modelo de tu máquina, puede ser necesario **desactivar Secure Boot**, ya que Qubes OS puede no arrancar con esta opción activada.



![0_02](assets/fr/02.webp)



Una vez cumplidas estas condiciones, reinicia tu ordenador y accede a la BIOS/UEFI pulsando inmediatamente **Esc**, **Del**, **F9**, **F10**, **F11** o **F12** (según el fabricante). En el menú de arranque, selecciona la llave USB como dispositivo de arranque para iniciar la instalación de Qubes OS.



**Pantalla de inicio**


Al arrancar desde la memoria USB, accederás directamente al menú **GRUB**, donde podrás elegir la acción a realizar. Usando las flechas de tu teclado, selecciona "Instalar Qubes OS" y pulsa "Enter".



![0_03](assets/fr/03.webp)



**Elección de lengua** :



Cuando se inicia la instalación, el primer paso es **elegir el idioma** y la **variante regional** adecuados para su configuración. Esto garantiza que el sistema y las opciones de instalación se muestren correctamente en su idioma preferido.



![0_04](assets/fr/04.webp)



**Configuración de parámetros** :



En esta fase, tendrás que configurar una serie de Elements antes de iniciar la instalación en tu máquina.



![0_05](assets/fr/05.webp)



**Disposición del teclado** :



Haz clic en la opción **Teclado** y, a continuación, selecciona la **disposición adecuada** para tu ordenador. Una vez que hayas hecho tu elección, haz clic en **Terminado** para pasar al siguiente paso.



**Elección de destino** :



Selecciona la opción "Destino de la instalación" para elegir el disco en el que deseas instalar Qubes OS. Por defecto, el particionado se realiza automáticamente, permitiéndole eliminar todos los datos del disco e instalar el sistema en él. Sin embargo, puedes elegir **Personalizado** o **Personalización avanzada** para realizar un particionado personalizado. A continuación, haga clic en "Hecho". El sistema te pedirá que establezcas una **contraseña**, que actúa como Layer de seguridad para encriptar tus datos. Asegúrese de elegir una contraseña compleja y única.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Seleccionar formato de fecha y hora** :


Haga clic en la opción Fecha y hora y seleccione su zona geográfica. También puede elegir el formato de hora que prefiera: 24h o 12h.



![0_08](assets/fr/08.webp)



**Creación de cuenta de usuario** :


Haz clic en **Crear usuario** para crear tu **primera cuenta**, que te permitirá iniciar sesión en Qubes OS.



![0_09](assets/fr/09.webp)



**Activar cuenta root** :


También puede **habilitar la cuenta root** estableciendo una contraseña independiente para la administración.



![0_10](assets/fr/10.webp)



Una vez realizados estos ajustes, haga clic en **Iniciar instalación** para iniciar el proceso.



![0_11](assets/fr/11.webp)



Espera a que aparezca el **fin de la instalación**, después pulsa en **restart system** para finalizar la instalación e iniciar Qubes OS.



![0_12](assets/fr/12.webp)



**Configuración adicional** :


Después de reiniciar, Qubes OS te pide que finalices las **plantillas por defecto y la configuración de qubes**. Introduzca la contraseña definida para cifrar el disco.



![0_13](assets/fr/13.webp)



A continuación, empieza seleccionando el **TemplateVM** que deseas instalar. Las opciones comunes incluyen **Debian 12 Xfce**, **Fedora 41 Xfce** y **Whonix 17**, siendo esta última recomendada para usos que requieran **anonimato y seguridad de red**. También puedes definir la **plantilla por defecto**, que servirá como base para la creación de nuevas **AppVMs**.



![0_14](assets/fr/14.webp)



En la sección **Configuración principal**, puedes elegir crear automáticamente qubes esenciales del sistema como **sys-net**, **sys-firewall** y **default DisposableVM**. Es aconsejable activar la opción de hacer **sys-firewall y sys-usb desechables**, para limitar la exposición del dispositivo y la red en caso de compromiso. También puedes crear **AppVMs** predeterminadas, como **personal**, **trabajo**, **no de confianza** y **bóveda**, para organizar tus actividades según su nivel de confianza.



![0_15](assets/fr/15.webp)



Qubes OS también te permite crear un **qube dedicado a dispositivos USB** (sys-usb) y configurar **Whonix Gateway y Workstation qubes** para asegurar tus comunicaciones a través de la red Tor. Para usuarios avanzados, la sección **Configuración avanzada** te permite crear un **LVM thin pool** para gestionar eficientemente el espacio de disco entre qubes.



Una vez configuradas todas estas opciones, haga clic en **Completar** y, a continuación, en **Finalizar configuración**. Espera mientras el sistema aplica esta configuración. A continuación, se le pedirá que **entre en su cuenta de usuario**, y su entorno Qubes OS estará listo para su uso, seguro y debidamente aislado para sus diversas actividades.



![0_17](assets/fr/17.webp)



Su sistema operativo ya está instalado y listo para funcionar.



![0_18](assets/fr/18.webp)



## Crea un qube en tu sistema



Para crear un qube, el proceso se gestiona mediante la herramienta **Qube Manager**, accesible desde el menú Inicio. En la ventana de la herramienta, basta con hacer clic en el icono **Crear qube** para abrir una nueva ventana de configuración. En primer lugar, introduzca un nombre para su qube, como "perso-web" o "work", para identificar su uso.



A continuación, seleccionarás su **Tipo**, normalmente **AppVM** para tareas rutinarias, o **DisposableVM** para uso temporal. Es crucial elegir el **Template** en el que se basará tu qube, como "fedora-39" o "debian-12", ya que éste proporcionará el sistema operativo y el software. También designará la **NetVM**, que es el qube responsable del acceso a Internet, por defecto **sys-firewall**.



Finalmente, tras ajustar el tamaño de almacenamiento y la RAM si es necesario, un simple clic en **OK** iniciará el proceso de creación. Una vez completado el proceso, tu nuevo qube será visible en la lista y estará listo para su uso.



En conclusión, Qubes OS no es un sistema operativo cualquiera, sino una solución de seguridad de vanguardia que replantea la arquitectura del ordenador personal. Su enfoque, basado en la compartimentación y el aislamiento mediante virtualización, ofrece una protección inigualable contra las amenazas más sofisticadas. Al segmentar el entorno de trabajo en qubes especializados para cada tarea, garantiza que el malware no pueda propagarse y poner en peligro todo el sistema.



Tanto si necesitas navegar por Internet de forma segura, proteger información sensible o trabajar con distintos niveles de confianza, Qubes OS te proporciona un marco resistente y transparente. Adoptando buenas prácticas y aprovechando al máximo sus características, tendrás una **fortaleza digital** adaptada a las amenazas modernas. Más información sobre cómo proteger tus datos y tu privacidad.



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1