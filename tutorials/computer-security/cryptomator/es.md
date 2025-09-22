---
name: Cryptomator
description: Cifra tus archivos en la nube
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian BURNEL publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



En este tutorial, utilizaremos la aplicación Cryptomator para cifrar datos almacenados en la Nube, ya sea en Microsoft OneDrive, Google Drive, Dropbox, Box o incluso iCloud.



Cifrar los datos que almacenas en soluciones de almacenamiento en línea como Drive es la mejor manera de proteger tus archivos y tu privacidad. Gracias al cifrado, tú eres el único que puede descifrar y leer tus datos, aunque estén almacenados en un servidor de Estados Unidos o de otro país del mundo.



En esta demostración, se utilizará un equipo Windows 11 22H2 con OneDrive, pero el procedimiento es idéntico en otras versiones de Windows y otros servicios de almacenamiento. Todo lo que necesita hacer es instalar el cliente de sincronización y añadir su cuenta. Esto permitirá a Cryptomator almacenar sus datos en la bóveda.



![Image](assets/fr/020.webp)



Cryptomator es una alternativa a otras aplicaciones, notablemente Picocrypt presentada en otro artículo, que parece diferente, pero es igualmente simple de usar. Cryptomator es también **de código abierto**, compatible con RGPD, y **cifrará los datos con el algoritmo de cifrado AES-256 bits**. En cambio, Picocrypt se basa en el algoritmo más rápido XChaCha20 (también de 256 bits).



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

La aplicación Cryptomator está disponible en **Windows** (exe / msi), **Linux**, **macOS,** pero también **Android** e **iOS**. Por cierto, todas las aplicaciones son gratuitas, excepto la de Android, por la que hay que pagar (14,99 euros).



En tu máquina, **Cryptomator creará una carpeta dentro de la cual creará una caja fuerte**. Dentro de la caja fuerte, que puede estar almacenada en tu OneDrive, Google Drive o similar, se cifrarán tus datos. Así, si almacenas todos tus datos en la caja fuerte alojada en tu espacio de almacenamiento de Drive, estarán protegidos (porque están cifrados).



**Nota**: en este artículo, los servicios de almacenamiento en línea se utilizan como ejemplo, pero Cryptomator puede utilizarse para cifrar datos en un disco local, un disco externo o incluso un NAS. De hecho, no hay restricciones.



## II. Instalación de Cryptomator



Para empezar, necesitas **descargar** e **instalar** **Cryptomator**. Una vez completada la descarga, basta con unos pocos clics para completar la instalación. Al igual que [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator se basará en WinFsp para **montar una unidad virtual en su máquina Windows**.





- [Descargar Cryptomator desde el sitio web oficial](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Uso de Cryptomator en Windows



### A. Crear una nueva caja fuerte



Para crear una nueva caja fuerte, haga clic en el botón "**Añadir**" y seleccione "**Nueva caja fuerte...**". Las cajas fuertes existentes y conocidas en esta máquina aparecerán entonces en Interface, a la izquierda. **Una caja fuerte creada en la máquina A puede abrirse y modificarse en la máquina B**, siempre que esté equipada con Cryptomator (y se conozca la clave de cifrado).



![Image](assets/fr/015.webp)



Empiece dando un nombre al almacén, por ejemplo "**IT-Connect**". Esto creará un directorio llamado "**IT-Connect**" en mi OneDrive.



![Image](assets/fr/011.webp)



En el siguiente paso, es probable que Cryptomator **detecte el "Drive "** presente en tu máquina: Google Drive, OneDrive, Dropbox, etc.... Para que puedas seleccionar directamente el proveedor. Probé esto en dos máquinas diferentes con Windows 11, con varios Drives, y no fue detectado. No hay problema, simplemente define una "**Ubicación personalizada**" y selecciona la raíz de tu espacio de almacenamiento. Por ejemplo: **C:\Users\<NombreDeUsuario>\OneDrive**.



![Image](assets/fr/018.webp)



A continuación, puedes ajustar una opción en la configuración de experto.



![Image](assets/fr/021.webp)



A continuación, deberá definir **una contraseña correspondiente a la clave de cifrado**. Esta contraseña le permitirá **desbloquear su caja fuerte Cryptomator** y acceder a sus datos. **Si la pierde, perderá el acceso a sus datos**. Por último, aún tiene la opción de **crear una clave de seguridad** marcando la opción "**Sí, más vale prevenir que curar**", muy similar a la clave de recuperación [BitLocker] (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Esto es recomendable, ¡pero no guardes esta clave de seguridad en la raíz de tu OneDrive!



Haz clic en "**Crear una caja fuerte**".



![Image](assets/fr/019.webp)



Copie la clave de recuperación y guárdela en su gestor de contraseñas favorito. Haz clic en "**Siguiente**".



![Image](assets/fr/013.webp)



Eso es todo, ¡tu nuevo baúl está creado y listo para usar!



![Image](assets/fr/014.webp)



### B. Cifras de acceso



Para acceder a una caja fuerte y a sus datos, ya sea para **leer los datos existentes o añadir nuevos datos**, es necesario **desbloquearla**. Cryptomator enumera las cajas fuertes conocidas: la caja fuerte IT-Connect aparece, así que basta con seleccionarla y hacer clic en "**Desbloquear**".



![Image](assets/fr/016.webp)



Debe introducir su contraseña para desbloquear la caja fuerte. A continuación, haga clic en "**Liberar unidad**".



![Image](assets/fr/022.webp)



**Tu caja fuerte se monta en la máquina Windows como una unidad virtual.** Esta unidad, que aquí hereda la letra E, te da acceso a tus datos (en texto plano, ya que la caja fuerte está desbloqueada).



![Image](assets/fr/017.webp)



En el lado de OneDrive, no podemos navegar por la bóveda de Cryptomator directamente. No podemos ver los datos (ni los nombres de los archivos ni su contenido). Esto significa que no necesitas añadir datos a tu bóveda Cryptomator a través del acceso directo habitual de OneDrive. **Debes añadir tus datos utilizando la unidad virtual de Cryptomator.**



![Image](assets/fr/012.webp)



### C. Opciones de tronco



A la configuración de la caja fuerte se accede a través del botón "**Opciones de volumen cifrado**" (cuando está bloqueado) y habilitará el bloqueo automático en caso de inactividad, igual que puedes hacer con tu caja fuerte de contraseñas. La opción "**Desbloquear volumen cifrado al iniciar**", como su nombre indica, desbloquea la unidad sin ninguna intervención por tu parte y monta la unidad virtual. Por razones de seguridad, es mejor evitar activar esta opción.



A través de la pestaña "**Montaje**" también puedes decidir montarlo en sólo lectura o asignarle una letra específica.



![Image](assets/fr/024.webp)



Además, en la configuración de Cryptomator, puede **activar el inicio automático de la aplicación**.



## IV. Conclusión



Con **Cryptomator**, puedes **crear una caja fuerte cifrada** en pocos minutos para proteger los datos que desees almacenar en OneDrive y consortes. Es muy fácil de usar a la hora de "emparejarlo" con un Drive: para ello, tiene mi preferencia sobre Picocrypt.