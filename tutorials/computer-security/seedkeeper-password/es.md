---
name: Seedkeeper - Gestor de contraseñas
description: ¿Cómo guardar tus contraseñas con la tarjeta inteligente Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper es una tarjeta inteligente desarrollada por Satochip, una empresa belga especializada en soluciones de hardware para la gestión y protección de secretos digitales. Conocida por su gama de tarjetas inteligentes para el ecosistema Bitcoin, Satochip concibió la Seedkeeper como alternativa a los métodos tradicionales de almacenamiento de frases mnemotécnicas y otros secretos digitales.



En concreto, el Seedkeeper adopta la forma de una tarjeta inteligente multifuncional, con certificación EAL6, dotada de un procesador seguro y una memoria a prueba de manipulaciones (el denominado "elemento seguro"). Como su nombre indica, su función es almacenar mnemónicos y contraseñas de la cartera Bitcoin de forma encriptada y protegida. Con Seedkeeper, puede generate, importar, organizar y guardar sus secretos directamente en el componente seguro de la tarjeta.



En mi opinión, Seedkeeper tiene dos usos principales, que exploraremos en 2 tutoriales separados:




- Almacenamiento de frases mnemotécnicas Bitcoin**: en lugar de escribir sus 12 o 24 palabras en papel, puede importarlas a la tarjeta inteligente y protegerlas con un código PIN.
- Gestión de contraseñas**: puedes generate contraseñas seguras a través de la aplicación Seedkeeper y almacenarlas directamente en la tarjeta inteligente, lo que te proporciona un gestor de contraseñas sin conexión cómodo y fácil de usar.



Técnicamente hablando, Seedkeeper tiene una capacidad de 8192 bytes, lo que le permite almacenar un mínimo de 50 secretos distintos (el número exacto dependerá de su tamaño y de los metadatos asociados a cada uno). Se puede acceder a Seedkeeper [a través de un lector de tarjetas inteligentes conectado](https://satochip.io/accessories/) a un ordenador, o a través de la aplicación móvil con conexión NFC. Todo el sistema funciona en modo offline, sin conexión a Internet, lo que garantiza una superficie de ataque limitada.



![Image](assets/fr/001.webp)



Una función especialmente interesante es la posibilidad de duplicar el contenido de un Seedkeeper en otro para crear una copia de seguridad. En este tutorial, te mostraremos cómo hacerlo.



En este tutorial, sólo cubriremos el uso de SeedKeeper para contraseñas tradicionales, a la manera de un gestor de contraseñas. Si quieres usar SeedKeeper para guardar frases mnemotécnicas Bitcoin wallet, consulta este otro tutorial:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. ¿Cómo consigo un Seedkeeper?



Hay dos formas principales de conseguir tu Seedkeeper. Puedes [comprarlo directamente en la tienda oficial de Satochip](https://satochip.io/product/seedkeeper/) o en un distribuidor autorizado. Pero como [el applet Seedkeeper es de código abierto](https://github.com/Toporin/Seedkeeper-Applet), también tienes la opción de instalarlo tú mismo en [una tarjeta inteligente en blanco](https://satochip.io/product/blank-javacard-for-diy-project/).



Si deseas utilizar la función de copia de seguridad de Seedkeeper, obviamente tendrás que adquirir dos tarjetas inteligentes.



## 2. Instalación del cliente Seedkeeper



El primer paso es instalar el software en tu ordenador o smartphone. En un PC, tendrás que [descargar la última versión de Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). En los móviles, la aplicación Seedkeeper está disponible en [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) y en [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Inicialización del Seedkeeper



Inicie la aplicación y haga clic en el botón "*Click & Scan*".



![Image](assets/fr/003.webp)



Se le pedirá un código PIN para su Seedkeeper. Como se trata de una tarjeta nueva, aún no se ha definido ningún PIN. Introduzca cualquier código para saltarse este paso y haga clic en "*Siguiente*".



![Image](assets/fr/004.webp)



A continuación, coloca la tarjeta en la parte posterior de tu smartphone. La aplicación detectará que Seedkeeper aún no se ha inicializado y te pedirá que configures el código PIN de tu tarjeta inteligente, de entre 4 y 16 caracteres. Para una seguridad óptima, elige un código PIN robusto, lo más largo posible, aleatorio y compuesto por una gran variedad de caracteres. Este PIN es la única barrera contra el acceso físico a sus contraseñas.



**Recuerda también guardar este PIN ahora**, por ejemplo en un gestor de contraseñas, o en un soporte físico aparte. En este último caso, nunca guardes el soporte que contiene el PIN en el mismo lugar que tu Seedkeeper, de lo contrario esta seguridad se volverá inútil. Es importante tener una copia de seguridad fiable: sin el PIN, no podrás recuperar los secretos almacenados en tu Seedkeeper.



![Image](assets/fr/005.webp)



Confirme su código PIN por segunda vez.



![Image](assets/fr/006.webp)



Tu Seedkeeper ya está inicializado. Puedes desbloquearlo introduciendo el código PIN que acabas de configurar.



![Image](assets/fr/007.webp)



Ahora accederá a la página de gestión de su tarjeta inteligente.



![Image](assets/fr/008.webp)



## 4. Guardar contraseñas en Seedkeeper



Una vez desbloqueado tu Seedkeeper, haz clic en el botón "*+*".



![Image](assets/fr/009.webp)



Seleccione "Generar secreto*". La opción "*Importar un secreto*" te permite guardar un secreto existente (por ejemplo, una contraseña que hayas creado en el pasado).



![Image](assets/fr/010.webp)



En nuestro caso, queremos guardar una contraseña. Haz clic en "*Contraseña*".



![Image](assets/fr/011.webp)



Asigna una "*Etiqueta*" a este secreto para poder identificarlo fácilmente si almacenas varios datos en tu Seedkeeper. También puedes añadir un identificador asociado a la contraseña y la URL del sitio.



![Image](assets/fr/012.webp)



Elija la longitud y los parámetros de su contraseña, luego haga clic en "*Generar*" y, a continuación, en "*Importar*".



![Image](assets/fr/013.webp)



Coloca tu Seedkeeper en la parte posterior de tu smartphone.



![Image](assets/fr/014.webp)



Su contraseña ha sido registrada.



![Image](assets/fr/015.webp)



## 5. Accede a tu contraseña Seedkeeper



Si quieres comprobar tu contraseña, coge tu Seedkeeper y haz clic en el botón "*Click & Scan*".



![Image](assets/fr/016.webp)



Introduzca su código PIN y pulse "*Siguiente*".



![Image](assets/fr/017.webp)



Coloca tu Seedkeeper en la parte posterior de tu smartphone.



![Image](assets/fr/018.webp)



Esto te lleva a una lista de todos tus secretos registrados. En este ejemplo, quiero mostrar la contraseña de mi cuenta de la Academia Plan ₿, así que hago clic en ella.



![Image](assets/fr/019.webp)



Pulsa el botón "*Revelar*".



![Image](assets/fr/020.webp)



Vuelve a escanear tu Seedkeeper.



![Image](assets/fr/021.webp)



Ahora aparecerá en pantalla la contraseña que ha guardado anteriormente. Puede copiarla y utilizarla en el sitio web correspondiente.



![Image](assets/fr/022.webp)



## 6. Copia de seguridad de Seedkeeper



Ahora vamos a hacer una copia de seguridad de mi Seedkeeper en un segundo Seedkeeper para tener dos copias. Esta redundancia puede formar parte de una estrategia para asegurar tus contraseñas más importantes: por ejemplo, almacenando tus Seedkeepers en 2 lugares distintos para limitar los riesgos físicos, o confiando una copia a un familiar de confianza.



Para ello, llévate tu segundo Seedkeeper (recuerda identificar uno de los dos con una marca para evitar confusiones). Empieza por inicializarlo, como se describe en el paso 3 de este tutorial. Una vez más, elige un código PIN fuerte. Dependiendo de tu estrategia, puedes optar por un PIN diferente o mantener el mismo.



![Image](assets/fr/023.webp)



Abre la aplicación, haz clic en "*Click & Scan*", introduce el PIN de tu Seedkeeper n°1 (fuente) y escanéalo.



![Image](assets/fr/024.webp)



Esto te lleva a la página de inicio, con una lista de tus secretos. Haz clic en los tres puntitos de la parte superior derecha de la interfaz.



![Image](assets/fr/025.webp)



Selecciona "*Hacer una copia de seguridad*" y pulsa "*Iniciar*".



![Image](assets/fr/026.webp)



Introduzca el código PIN de su tarjeta de reserva (Seedkeeper n°2).



![Image](assets/fr/027.webp)



A continuación, escanea la tarjeta.



![Image](assets/fr/028.webp)



Haga lo mismo con la tarjeta principal (Seedkeeper n°1) y, a continuación, haga clic en "*Hacer una copia de seguridad*".



![Image](assets/fr/029.webp)



Tu Seedkeeper n°2 contiene ahora todos los secretos almacenados en el Seedkeeper n°1.



![Image](assets/fr/030.webp)



Puedes escanear tu Seedkeeper n°2 para comprobar que se han copiado los secretos.



![Image](assets/fr/031.webp)



¡Eso es todo! Ahora ya sabes cómo utilizar Seedkeeper para almacenar tus contraseñas. En un próximo tutorial, veremos cómo utilizar Seedkeeper para hacer copias de seguridad de un Bitcoin wallet. También te invito a descubrir su uso combinado con SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356