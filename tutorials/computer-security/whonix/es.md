---
name: Whonix
description: Preservar su intimidad y confidencialidad.
---

![cover](assets/cover.webp)



**Whonix** es una distribución Linux basada en **Debian**, diseñada para proporcionar un entorno que combina **seguridad**, **anonimato** y **privacidad**. Fácil de aprender, y compatible con diferentes interfaces (máquinas virtuales, Qubes OS, modo Live), incluye por defecto enrutamiento de tráfico de red a través de **Tor**, **doble cortafuegos** (un cortafuegos en la puerta de enlace y otro en la estación de trabajo), **protección completa contra fugas IP/DNS** y herramientas para enmascarar eficazmente tu actividad de los observadores de la red, incluido tu ISP. Más que un sistema anónimo, **Whonix** es un completo entorno de desarrollo seguro.



## ¿Por qué elegir Whonix?





- Gratuito**: Como la mayoría de las distribuciones Linux, Whonix es un sistema de código abierto cuya licencia es totalmente gratuita. Se desarrolla en código abierto, con una comunidad activa y transparente.
- Privacidad, seguridad y anonimato**: El principal objetivo de Whonix es ofrecer un entorno ultraseguro, en el que todos tus datos estén protegidos y tus comunicaciones encriptadas a través de la red Tor.
- Fácil de usar**: Whonix ofrece un Interface gráfico intuitivo y preconfigurado, apto incluso para usuarios principiantes. No es necesario ser un experto para beneficiarse de una protección avanzada.
- Entorno ideal para un desarrollo seguro**: Whonix le permite desarrollar, probar, auditar o ejecutar programas sin revelar nunca su IP Address real ni exponer sus hábitos de navegación o comunicación en la red.
- Sesiones desechables y modo Live**: Whonix puede lanzarse en modo Live o a través de máquinas desechables (por ejemplo, a través de **Qubes OS**), lo que permite realizar tareas críticas sin dejar rastros persistentes una vez finalizada la sesión.
- Instalación relativamente sencilla**: Se suministran imágenes listas para usar que permiten una rápida instalación en máquinas virtuales (VirtualBox, KVM, Qubes). El sistema está documentado y se actualiza periódicamente.



## Instalación y configuración



Antes de pasar a la instalación de Whonix, es esencial tener en cuenta que esta distribución **todavía no está disponible oficialmente** como sistema principal que se pueda instalar directamente en el disco Hard (en modo bare metal). En otras palabras, usted **todavía no puede instalar Whonix como un sistema operativo host clásico**, como Ubuntu o Debian estándar.



No obstante, existen varias ediciones que permiten utilizar Whonix de forma **volátil** (modo Live, sesiones temporales) o **persistente** (mediante máquinas virtuales o integración en Qubes OS).



Para un uso estable a largo plazo, **la virtualización es actualmente el único método recomendado oficialmente**. Puedes ejecutar Whonix utilizando **VirtualBox** (Whonix-Gateway y Whonix-Workstation) o integrarlo en un sistema como **Qubes OS**. En este tutorial, nos centraremos en una instalación con VirtualBox.



### Requisitos previos



Antes de poder instalar Whonix en modo virtual, asegúrese de que su máquina cumple los requisitos técnicos mínimos. La virtualización requiere ciertos recursos que no todos los ordenadores pueden ofrecer. Por lo tanto, es esencial que su procesador sea compatible con la tecnología de virtualización (Intel VT-x o AMD-V), y que esta opción esté activada en la BIOS/UEFI.



Estas son las especificaciones recomendadas para disfrutar de una experiencia fluida y estable con Whonix:





- Memoria de acceso aleatorio (RAM)**: se recomienda encarecidamente un mínimo de **8 GB**. Cuanta más RAM tenga, más recursos podrá asignar a las máquinas virtuales (Gateway y Workstation), mejorando el rendimiento.
- Espacio disponible en disco**: deje al menos 30 GB de espacio libre en disco**. Esto incluye el espacio necesario para las dos máquinas virtuales, los archivos de sistema y cualquier dato o instantánea.
- Procesador**: se recomienda un procesador con al menos **4 núcleos físicos** (8 hilos lógicos), especialmente si desea ejecutar otros servicios o herramientas en paralelo.



### Descargar Whonix



Whonix está disponible en varias ediciones, dependiendo del tipo de entorno en el que quieras utilizarlo. Para la mayoría de los usuarios (Windows, Linux o MacOs), la edición VirtualBox es la más fácil de configurar. Puedes descargar la imagen directamente desde [el sitio web oficial](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **no es compatible** con los MacBooks que utilizan procesadores Apple Silicon (arquitectura ARM).



## Instalación de VirtualBox



Para ejecutar Whonix, necesitarás un **hipervisor** como VirtualBox, Qubes o KVM.



Una vez descargado el archivo, instálalo como lo harías con cualquier otro programa. Acepta las opciones por defecto a menos que tengas requisitos específicos. ¿Te has perdido? Consulta nuestra guía de uso de VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importar Whonix



Una vez instalado VirtualBox, puedes importar los archivos Whonix `.ova` que descargaste anteriormente (`Whonix-Gateway-Xfce.ova` y `Whonix-Workstation-Xfce.ova`).



Abra VirtualBox y, a continuación, haga clic en **Archivo → Importar dispositivo**.


Seleccione el archivo `.ova` correspondiente (empiece por el Gateway).



![0_03](assets/fr/03.webp)



Elija la ubicación donde se almacenarán los archivos de la máquina virtual Whonix.



![0_04](assets/fr/04.webp)



Acepte las condiciones de uso, inicie la importación y espere a que finalice el proceso.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Configuración de Whonix



Antes de iniciar Whonix, es importante ajustar algunas **configuraciones del sistema** para garantizar un mejor rendimiento:



Seleccione la máquina virtual **Whonix-Workstation-Xfce** y haga clic en **Configuración**.



![0_06](assets/fr/07.webp)



Ve a la pestaña **Sistema**, donde la asignación de RAM por defecto es de 2048 MB. Le recomendamos que **la aumente a 4096 MB (4 GB)** para una mayor fluidez, especialmente si pretende abrir varias aplicaciones o trabajar en sesiones largas. El Gateway puede permanecer en 2048 MB, a menos que esté utilizando muchas conexiones Tor en paralelo.



![0_08](assets/fr/08.webp)



### Introducción a Whonix



Para que Whonix funcione correctamente y con seguridad, **debe seguir esta secuencia de inicio**:



Primero, inicia la máquina **Whonix-Gateway-Xfce**. Esta máquina es responsable de enrutar todo el tráfico a través de la red **Tor**. Sin la pasarela ejecutándose, ningún tráfico será enrutado a través de Tor y perderá el anonimato.



![0_09](assets/fr/09.webp)



Una vez que el Gateway esté completamente lanzado (verás Tor conectado), puedes iniciar **Whonix-Workstation-Xfce**, que se conectará automáticamente a través del Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Actualización del sistema



Entre en el terminal, introduzca el siguiente comando para actualizar la lista de paquetes:



```shell
sudo apt update
```



A continuación, ejecute el siguiente comando para instalar las actualizaciones disponibles:



```shell
sudo apt full-upgrade
```



## Descubra Whonix



**Whonix** es un sistema diseñado para proporcionar un entorno informático **seguro**, **anónimo** y **confidencial**, ideal para navegar por Internet sin comprometer tu identidad ni tus datos. Para conseguirlo, incluye una serie de aplicaciones útiles para el día a día, diseñadas para reforzar tu seguridad digital desde el primer momento.


### KeepassXC



**KeePassXC** es el gestor de contraseñas integrado de Whonix. Te permite **crear, almacenar y gestionar** tus contraseñas de forma segura, sin tener que recordarlas todas manualmente. Las contraseñas se almacenan en una **base de datos cifrada**, protegida por una contraseña maestra.



### Navegador Tor



**Tor Browser** es el navegador web por defecto de Whonix. Se basa en la red **Tor**, que redirige su tráfico a través de varios relés en todo el mundo, por lo que es prácticamente imposible identificar su verdadera IP Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** es un Bitcoin Wallet ligero y rápido, preinstalado en Whonix para permitirte gestionar **transacciones de criptomoneda** de forma anónima. No descarga la Blockchain completa, sino que utiliza servidores remotos para obtener la información necesaria, lo que la hace mucho más ligera que una Wallet completa.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix es más que un sistema operativo: es un auténtico **entorno seguro** diseñado para proteger tu anonimato, tu privacidad y tus actividades sensibles. Gracias a su arquitectura basada en Tor, la partición inteligente entre Gateway y Workstation, y herramientas preinstaladas como Tor Browser, KeePassXC y Electrum, ofrece una solución llave en mano para cualquiera que desee **navegar de forma anónima**, **trabajar de forma segura** o **manipular datos confidenciales**.



Para reforzar la seguridad de tu sistema Unix, echa un vistazo a nuestro tutorial sobre cómo auditar tu máquina: comprueba si hay agujeros de seguridad en tu sistema operativo y asegúrate de que tus datos no están en peligro.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af