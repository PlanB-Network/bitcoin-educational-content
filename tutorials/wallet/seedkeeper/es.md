---
name: Seedkeeper
description: ¿Cómo hago una copia de seguridad de mi wallet Bitcoin con la tarjeta inteligente Seedkeeper?
---

![cover](assets/cover.webp)



El Seedkeeper es una tarjeta inteligente desarrollada por Satochip, una empresa belga especializada en soluciones de hardware para la gestión y protección de secretos digitales. Conocida por su gama de tarjetas inteligentes para el ecosistema Bitcoin, Satochip diseñó la Seedkeeper como alternativa a los métodos tradicionales de almacenamiento de frases mnemotécnicas.



En concreto, el Seedkeeper adopta la forma de una tarjeta inteligente multifuncional, con certificación EAL6, dotada de un procesador seguro y una memoria a prueba de manipulaciones (lo que se conoce como "elemento seguro"). Como su nombre indica, su función es almacenar mnemónicos y contraseñas de Bitcoin wallet de forma encriptada y protegida. Con Seedkeeper, puedes generate, importar, organizar y guardar tus secretos directamente en el componente seguro de la tarjeta.



En mi opinión, Seedkeeper tiene dos usos principales, que exploraremos en 2 tutoriales separados:




- Almacenamiento de frases mnemotécnicas Bitcoin**: en lugar de escribir sus 12 o 24 palabras en papel, puede importarlas a la tarjeta inteligente y protegerlas con un código PIN.
- Gestión de contraseñas**: puedes generate contraseñas seguras a través de la aplicación Seedkeeper y almacenarlas directamente en la tarjeta inteligente, lo que te proporciona un gestor de contraseñas sin conexión cómodo y fácil de usar.



Técnicamente hablando, Seedkeeper tiene una capacidad de 8192 bytes, lo que le permite almacenar un mínimo de 50 secretos distintos (el número exacto dependerá de su tamaño y de los metadatos asociados a cada uno). Se puede acceder a Seedkeeper [a través de un lector de tarjetas inteligentes conectado](https://satochip.io/accessories/) a un ordenador, o a través de la aplicación móvil con conexión NFC. Todo el sistema funciona en modo offline, sin conexión a Internet, lo que garantiza una superficie de ataque limitada.



![Image](assets/fr/001.webp)



Una función especialmente interesante es la posibilidad de duplicar el contenido de un Seedkeeper en otro para crear una copia de seguridad. En este tutorial, te mostraremos cómo hacerlo.



Seedkeeper también es muy interesante cuando se combina con hardware sin estado wallet, como SeedSigner o Specter DIY. En este caso, no es necesario utilizar el cliente de Satochip en el ordenador o el teléfono móvil. El Seedkeeper mantiene el seed en su secure element y puede ser utilizado directamente con el dispositivo de firma, eliminando la necesidad de un código QR en papel. No voy a desarrollar este caso de uso particular en este tutorial, ya que es el tema de otro tutorial dedicado :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. ¿Qué caso de uso tiene Seedkeeper?



En este tutorial, sólo trataré los casos de uso relacionados con Bitcoin, ya que de eso trata este tutorial. No entraremos en la funcionalidad de gestión de contraseñas, que será objeto de otro tutorial.



En comparación con una simple copia de seguridad en papel de la frase mnemotécnica, utilizar un Seedkeeper tiene varias ventajas:





- Resistente al robo:** La seed de tu wallet no es accesible en texto claro. Para extraerla, es necesario conocer el PIN Seedkeeper. Un ladrón que se haga con el dispositivo no podrá hacer nada con él sin este código.





- Repartir el riesgo en dos factores:** puedes dividir la seguridad entre un factor digital y un factor físico. Por ejemplo, si almacenas el PIN Seedkeeper en tu gestor de contraseñas, necesitarás tanto el acceso a este gestor como la posesión física de la tarjeta inteligente para obtener el seed (una probabilidad de ataque significativamente reducida).





- Gestión centralizada:** Seedkeeper facilita la gestión de múltiples semillas de diferentes carteras.





- Copias de seguridad sencillas:** simplemente duplica las copias de seguridad cifradas en otros SeedKeepers.



Sin embargo, hay una serie de desventajas en comparación con una simple copia de seguridad en papel de tu seed:





- El precio:** aunque modesto (unos 25 euros), sigue siendo superior al de una hoja de papel.





- Dependencia de un dispositivo informático de propósito general:** la introducción y gestión de seed requiere un ordenador o un smartphone, lo que significa que su mnemónica pasa por una máquina con una superficie de ataque mucho más amplia que el hardware de wallet. Esto puede representar un riesgo si la máquina se ve comprometida. Esta es la razón por la que no recomiendo usar Seedkeeper para almacenar la seed de un hardware wallet (excepto en uso sin estado y sin ordenador, como con SeedSigner). El papel del hardware wallet es precisamente almacenar la seed en un entorno minimalista y altamente seguro. Al introducir manualmente su seed en su ordenador habitual, ya no queda confinada al hardware wallet: también acaba en una máquina de uso general, expuesta a múltiples vectores de ataque. Así que es mejor usar Seedkeeper para una wallet caliente que para una fría (excepto SeedSigner / hardware wallet sin estado).





- El riesgo de pérdida vinculado al PIN:** la inaccesibilidad directa del seed, a diferencia de una copia de seguridad en papel, ofrece efectivamente una protección contra el robo físico. Pero como siempre, la seguridad es un acto de equilibrio entre el riesgo de robo y el riesgo de pérdida. Si tu copia de seguridad requiere un PIN, la pérdida de este código hará imposible recuperar tu frase mnemotécnica, y por tanto acceder a tus bitcoins.



Teniendo en cuenta estas ventajas y desventajas, considero que los mejores usos de Seedkeeper (aparte de su función de gestor de contraseñas) son, por un lado, almacenar semillas de tus **carteras de software**, puesto que ya residen en tu teléfono u ordenador, o de tu hardware wallet sin pantalla como el Satochip, y por otro lado, usarlo en combinación con hardware wallet sin estado como el SeedSigner, donde realmente destaca.



Otro caso de uso especialmente interesante para Seedkeeper es la posibilidad de realizar copias de seguridad seguras y fiables de los *Descriptores* de sus carteras.



## 2. ¿Cómo consigo un Seedkeeper?



Hay dos formas principales de conseguir tu Seedkeeper. Puedes [comprarlo directamente en la tienda oficial de Satochip](https://satochip.io/product/seedkeeper/) o en un distribuidor autorizado. Pero como [el applet Seedkeeper es de código abierto](https://github.com/Toporin/Seedkeeper-Applet), también tienes la opción de instalarlo tú mismo en [una tarjeta inteligente en blanco](https://satochip.io/product/blank-javacard-for-diy-project/).



Si deseas utilizar la función de copia de seguridad de Seedkeeper, obviamente tendrás que adquirir dos tarjetas inteligentes.



## 3. Instalación del cliente Seedkeeper



En este tutorial, haremos una copia de seguridad de nuestra cartera seed en nuestro Seedkeeper. El primer paso es instalar el software en tu ordenador o smartphone. En un PC, tendrás que [descargar la última versión de Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). En móvil, la aplicación Seedkeeper está disponible en [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) así como en [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inicialización del Seedkeeper



Inicie la aplicación y haga clic en el botón "*Click & Scan*".



![Image](assets/fr/003.webp)



Se le pedirá un código PIN para su Seedkeeper. Como se trata de una tarjeta nueva, aún no se ha definido ningún PIN. Introduzca cualquier código para saltarse este paso y haga clic en "*Siguiente*".



![Image](assets/fr/004.webp)



A continuación, coloca la tarjeta en la parte posterior de tu smartphone. La aplicación detectará que Seedkeeper aún no se ha inicializado y te pedirá que configures el código PIN de tu tarjeta inteligente, de entre 4 y 16 caracteres. Para una seguridad óptima, elige una contraseña segura, lo más larga posible, aleatoria y compuesta por una gran variedad de caracteres. Este código PIN es la única barrera contra el acceso físico a su frase de recuperación.



**Recuerda también guardar este PIN ahora**, por ejemplo en un gestor de contraseñas, o en un soporte físico aparte. En este último caso, nunca guardes el soporte que contiene el PIN en el mismo lugar que tu Seedkeeper, de lo contrario esta seguridad se volverá inútil. Es importante tener una copia de seguridad fiable: sin el PIN, no podrás recuperar los secretos almacenados en tu Seedkeeper.



![Image](assets/fr/005.webp)



Confirme su código PIN por segunda vez.



![Image](assets/fr/006.webp)



Tu Seedkeeper ya está inicializado. Puedes desbloquearlo introduciendo el código PIN que acabas de configurar.



![Image](assets/fr/007.webp)



Ahora accederá a la página de gestión de su tarjeta inteligente.



![Image](assets/fr/008.webp)



## 5. Registre una seed en Seedkeeper



Una vez desbloqueado tu Seedkeeper, haz clic en el botón "*+*".



![Image](assets/fr/009.webp)



Seleccione "Importar secreto*". La opción "*Generar secreto*" te permite crear una nueva frase mnemotécnica directamente desde la aplicación.



![Image](assets/fr/010.webp)



En nuestro caso, queremos guardar el seed en nuestra cartera. Haz clic en "*Mnemonic*".



![Image](assets/fr/011.webp)



Asigna una "*Etiqueta*" a este secreto para poder identificarlo fácilmente si almacenas varios datos en tu Seedkeeper.



![Image](assets/fr/012.webp)



A continuación, introduzca su frase de recuperación en el campo correspondiente. Si lo desea, también puede añadir un passphrase BIP39 o sus *Descriptores*. A continuación, haga clic en "Importar*".



![Image](assets/fr/013.webp)



*La mnemotecnia que aparece en esta imagen es ficticia y no pertenece a nadie. Es sólo un ejemplo. Nunca reveles tu propia mnemotecnia a nadie, o te robarán tus bitcoins



Coloca tu Seedkeeper en la parte posterior de tu smartphone.



![Image](assets/fr/014.webp)



Su seed ha sido registrado.



![Image](assets/fr/015.webp)



## 6. Acceda a su seed en Seedkeeper



Si desea comprobar su frase mnemotécnica, coja su Seedkeeper y haga clic en el botón "*Click & Scan*".



![Image](assets/fr/016.webp)



Introduzca su código PIN y pulse "*Siguiente*".



![Image](assets/fr/017.webp)



Coloca tu Seedkeeper en la parte posterior de tu smartphone.



![Image](assets/fr/018.webp)



Esto te lleva a una lista de todos tus secretos registrados. En este ejemplo, quiero mostrar el seed de mi cartera "*Blockstream App*", así que hago clic en él.



![Image](assets/fr/019.webp)



Pulsa el botón "*Revelar*".



![Image](assets/fr/020.webp)



Vuelve a escanear tu Seedkeeper.



![Image](assets/fr/021.webp)



Su frase mnemotécnica previamente grabada aparece ahora en la pantalla.



![Image](assets/fr/022.webp)



## 7. Copia de seguridad de Seedkeeper



Ahora vamos a hacer una copia de seguridad de mi Seedkeeper en un segundo Seedkeeper para tener dos copias. Esta redundancia puede formar parte de una estrategia para asegurar tus bitcoins: por ejemplo, almacenar tu frase en dos lugares distintos para limitar los riesgos físicos, o confiar una copia a un familiar de confianza como parte de un plan de herencia.



Para ello, llévate tu segundo Seedkeeper (recuerda identificar uno de los dos con una marca para evitar confusiones). Empieza por inicializarlo, como se describe en el paso 4 de este tutorial. Elige de nuevo una contraseña segura. Dependiendo de tu estrategia, puedes optar por una contraseña diferente o mantener la misma.



![Image](assets/fr/023.webp)



Abre la aplicación, haz clic en "*Click & Scan*", introduce la contraseña de tu Seedkeeper n°1 (fuente) y escanéalo.



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



¡Eso es todo! Ahora ya sabes cómo utilizar Seedkeeper para guardar la frase mnemotécnica de una Bitcoin wallet. En un próximo tutorial, veremos cómo utilizar Seedkeeper para guardar tus contraseñas. También te invito a descubrir su uso combinado con SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

En este tutorial, hemos mencionado varias veces los ***Descriptores*** de su cartera Bitcoin. ¿No sabe lo que son? En ese caso, le recomiendo que realice nuestro curso de formación gratuito CYP 201, que profundiza en todos los mecanismos que intervienen en el funcionamiento de las carteras HD



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f