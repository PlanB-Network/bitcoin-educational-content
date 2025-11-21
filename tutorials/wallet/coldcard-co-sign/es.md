---
name: COLDCARD - Firma conjunta
description: Descubra la función Co-Firma y utilícela en su COLDCARD
---

![cover](assets/cover.webp)


*Nota: Este tutorial está dirigido a personas que ya tienen cierta experiencia con monederos multifirma, dispositivos Coinkite y software como Sparrow wallet o Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**¿Por qué ColdCard Co-Sign?



Esta función le permite añadir **condiciones de gasto** a su dispositivo ColdCard (Q o Mk4) a modo de módulo de seguridad de hardware (HSM), para proteger sus fondos al tiempo que conserva una flexibilidad y un control considerables sobre ellos.



Las condiciones de gasto pueden ser, por ejemplo:





- Límites de magnitud**: limita la cantidad de bitcoins que puedes gastar en una sola transacción.
- Límites de velocidad:** decide cuántas transacciones puedes realizar por unidad de tiempo (por hora, día, semana, etc.), requiriendo un número mínimo de bloques entre ellas.
- Direcciones pre-aprobadas:** Sólo permite el envío de bitcoins a direcciones pre-aprobadas.
- Autenticación de dos factores:** Requiere confirmación desde una aplicación móvil 2FA de terceros (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) en un smartphone/tableta con NFC y acceso a Internet.



**Cómo funciona



Añadiendo una segunda seed a su dispositivo ColdCard Mk4 o Q, denominada "Clave de política de gasto", a la que nos referiremos a lo largo de este tutorial como "Clave C".


Además de esta seed adicional, se le pedirá Supply al menos una clave adicional (XPUB), que llamaremos "Clave de reserva", para crear una Wallet Multisig 2-en-N.



En resumen, vamos a crear una Wallet Multisig, y su dispositivo ColdCard contendrá 2 de las claves privadas necesarias para gastar los fondos, la seed maestra del dispositivo y la "Clave de Política de Gasto".



Cada vez que se pida a la "Clave C" que firme, se aplicarán las condiciones de gasto especificadas, y la ColdCard sólo firmará si la transacción las cumple.



Si desea prescindir de estas condiciones de gasto, puede hacerlo:




- firmando con una de las llaves de reserva y la mano seed, o 2 llaves de reserva según el tamaño de su Multisig.
- introduciendo la "Clave de política de gasto" o la "Clave C" en el menú "Cofirmar". **Esta última no puede consultarse directamente en el dispositivo, ya que de lo contrario cualquiera podría anular las condiciones de gasto configuradas.**




## Configuración de ColdCard Co-Sign



![video](https://youtu.be/MjMPDUWWegw)



### 1- Activar la funcionalidad



En primer lugar, asegúrate de que tu dispositivo tiene al menos la última versión de firmware:




- Mk4: v5.4.2
- Q: v1.3.2Q




En su Mk4 o ColdCardQ, vaya a *Herramientas avanzadas > Cofirmación de la ColdCard*.



![Co-Sign](assets/fr/01.webp)



*En el siguiente tutorial, las capturas de pantalla se tomarán en un ColdCardQ por comodidad, pero los pasos y menús son idénticos entre el Mk4 y el Q.*



Se muestra un resumen de la funcionalidad.


La terminología utilizada para designar las claves, que volveremos a utilizar en el Wallet multifirma 2 contra 3 que estamos a punto de crear, es:



Tecla A = Coldcard master seed


Clave B = Clave de reserva


Clave C = Clave de política de gasto



Pulse **"INTRO "**.



![Co-Sign](assets/fr/02.webp)



El siguiente paso es decidir qué clave privada actuará como "Clave de política de gasto" o "Clave C".



Vemos que tenemos varias opciones:





- O pulse **"ENTER "** para generate una nueva frase seed de 12 palabras.





- Haga clic en **"(1) "** para importar una seed de 12 palabras existente, o elija **"(2) "** para importar una seed de 24 palabras existente.





- O pulsa **"(6) "** para importar un seed desde el almacén de tu dispositivo.



Para los propósitos de este tutorial, hemos decidido importar un seed de 12 palabras existente pulsando **"(1) "**. Esto puede ser cualquier seed BIP39 que ya posee, y para el que, obviamente, tiene una copia de seguridad.



Utilice su teclado para introducir las 12 palabras de su seed. Para este ejemplo, elegiremos la frase valida seed beef x 12. Luego presione **"ENTER "**.


*Nota: si no dispone de una copia de seguridad de este seed, ya no podrá modificar los ajustes de "Co-firma" en su dispositivo, con el fin de cambiar sus condiciones de gasto*



La función "Co-firma" ya está activada en el dispositivo. A continuación tendremos que elegir nuestras condiciones de gasto, y después completar la creación del Wallet multifirma.



![Co-Sign](assets/fr/03.webp)



### 2- Elija las condiciones de gasto o "*políticas de gasto*"



Aquí especificamos las condiciones de gasto que deben cumplirse cuando la **"Clave C "** o **"Clave de Política de Gasto**" firma una transacción.



En el menú **"Cofirmación "**, haga clic en **"Política de gastos**".



A continuación, puede elegir la magnitud máxima, es decir, el número máximo de satoshis que pueden gastarse en una sola transacción.



Para este ejemplo, elegiremos una magnitud máxima de **21212** satoshis. Pulsa **"ENTER "** para confirmar.




![Co-Sign](assets/fr/04.webp)



A continuación, elegimos establecer la velocidad máxima, es decir, el número de transacciones que el dispositivo podrá firmar por unidad de tiempo. Para este tutorial, elegiremos velocidad ilimitada, es decir, sin límite en el número de transacciones.




![Co-Sign](assets/fr/05.webp)



### 3- Crear Wallet Multisig 2-en-N



Todavía tenemos que elegir la tercera clave para nuestra Wallet Multisig, es decir, la **"Clave de reserva "** (Clave B), además de la **seed** maestra del dispositivo (Clave A) y la **"Clave de política de gastos "** (Clave C).



Nuestra "Clave B" tendrá que ser importada a través de una tarjeta SD, o a través de un código QR en el caso de ColdCardQ.


Para ello, necesitaremos un segundo dispositivo ColdCard Mk4 o Q, en el que se utilizará nuestra "Clave B".



En este segundo dispositivo que contiene su **"Backup Key "**, digamos una ColdCard Mk4 para este ejemplo, vaya desde el menú principal a **"Settings "**, luego, **"Multisig Wallet"**, y finalmente **"Export Xpub "**.


(Si tu segundo dispositivo es un ColdCardQ, tendrás la opción de exportar tu Xpub mediante código QR, por supuesto).





![Co-Sign](assets/fr/06.webp)





En la siguiente pantalla, inserta una tarjeta SD y haz clic en el botón **"validar "** de la parte inferior derecha. A continuación, haz clic en **"(1) "** para guardar el archivo en la tarjeta SD.



El archivo contendrá la huella digital de la clave pública (*fingerprint*) en su nombre, y tendrá la forma `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



A continuación, inserta la tarjeta SD en la ColdCardQ "inicial" para importar nuestra "Backup Key" (clave B).


En el menú "ColdCard Co-Signing", elige "Build 2-of-N", luego en la siguiente pantalla pulsa **"ENTER "**, luego otra vez **"ENTER "** para importar la "Backup Key" de la tarjeta SD.



![Co-Sign](assets/fr/08.webp)



En la siguiente pantalla, deje en blanco "Número de cuenta" (a menos que sepa exactamente lo que está haciendo) y vuelva a pulsar **"INTRO "**.



![Co-Sign](assets/fr/09.webp)



Por fin, estamos listos para utilizar nuestro nuevo Wallet Multisig 2-sur-3, compuesto de la siguiente manera:



Tecla A= Coldcard Q master seed


Clave B= Clave de seguridad (recién importada de un segundo dispositivo Coldcard)


Clave C= Clave de política de gasto (si se utiliza para firmar, impone condiciones de gasto predefinidas)



## Firma conjunta con Sparrow wallet



Si es necesario, consulte los siguientes tutoriales para familiarizarse con el software Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Exportación Wallet Multisig 2-sur-3 a Sparrow wallet



Ahora tenemos que exportar nuestra Wallet Multisig a Sparrow para poder colocar allí nuestros primeros satoshis.



En el menú principal de tu ColdCardQ, selecciona **"Configuración "**, y luego **"Multisig Carteras "**.


Ahora se muestra el conjunto de monederos Multisig conocidos por su ColdCard, con el número de claves implicadas aquí "2/3" (2-sur3). Elija la Multisig **"ColdCard Co-Sign "** que acabamos de crear y, a continuación, haga clic en **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Por último, elige el método que te permitirá exportar Wallet a Sparrow. En nuestro caso, elegiremos tarjeta SD, por lo que haremos clic en **"(1) "** después de insertar una tarjeta SD en la ranura A del dispositivo.



![Co-Sign](assets/fr/11.webp)



A continuación, en Sparrow wallet, seleccione "Importar Wallet".



![Co-Sign](assets/fr/12.webp)



A continuación, haz clic en **"Importar archivo "**. A continuación, elija el archivo **"export-Coldcard_Co-sign.txt "** de su tarjeta SD.



![Co-Sign](assets/fr/13.webp)



Dale a tu Wallet un nombre tal y como aparecerá en Sparrow, y elige una contraseña para encriptar tu Wallet (o no).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Ya estamos listos para recibir nuestros primeros satoshis y probar las condiciones de gasto que hemos aplicado a nuestro Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Comprobación de las políticas de gasto predefinidas



Como recordatorio, habíamos decidido una magnitud máxima de 21212 satoshis para nuestra Wallet Multisig. Esto significaba que cada vez que la Clave de Política de Gasto (Clave C) firmara una transacción, ésta sólo sería válida si la cantidad gastada era menor o igual a 21212 satoshis.



Vamos a probarlo.


En primer lugar, vamos a hacer clic en la pestaña "Recibir" de Sparrow y soltar unos cuantos Satss en Wallet, que utilizaremos a lo largo de este tutorial.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



A continuación, intentemos gastar más de los 21212 satoshis permitidos simulando una transacción de 50.000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Tras escanear el código QR que representa la transacción *sin firmar* con nuestro ColdCardQ para importar la transacción, esto es lo que se nos muestra en pantalla. Un mensaje de advertencia nos indica que no se cumplen las condiciones de gasto. Si firmamos la transacción de todas formas, sólo firmará una de las 2 claves (la seed maestra del dispositivo, pero no la "Clave C").




![Co-Sign](assets/fr/23.webp)



Aquí, después de importar nuestra transacción a Sparrow, podemos ver que sólo una de las firmas se ha aplicado a la transacción.



![Co-Sign](assets/fr/24.webp)




Ahora repitamos el experimento, pero para una operación de 21.000 satoshis, es decir, inferior a la magnitud máxima (21212 Sats) que fijamos para este Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Intentemos firmar esta transacción con nuestra ColdCardQ.



Esta vez no hay problema, no aparece ningún mensaje de advertencia, y cuando importamos la transacción firmada en Sparrow wallet, esta vez se han aplicado las 2 firmas, con lo que la transacción es válida y está lista para su distribución.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Co-firmar con el Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA y direcciones en lista blanca



En este apartado, usaremos nuestro Wallet Multisig Co-Sign con Nunchuk, y aprovecharemos para aplicar nuevas condiciones de gasto a ver qué tal.



Vaya a *Herramientas avanzadas > Cofirmación de ColdCard*.


Se nos pide que introduzcamos nuestra "Clave de Política de Gasto", para acceder al menú que nos permite cambiar las condiciones de gasto. En nuestro caso, introducimos 12 x "ternera".



Hemos decidido mantener una magnitud de 21212 Sats, y una "Velocidad límite" máxima por razones prácticas relacionadas con este tutorial. Por otra parte, vamos a utilizar el menú **"Lista blanca de direcciones "** para imponer las direcciones en las que se pueden gastar nuestros fondos.




![Co-Sign](assets/fr/31.webp)




Escanee los códigos QR asociados a las direcciones (elegiremos 2) que desea añadir a su lista blanca y, a continuación, pulse **"INTRO "**. Tras validar tus direcciones pulsando sucesivamente **"INTRO "**, vemos que se han aplicado límites a las direcciones de Magnitud y beneficiarias.



![Co-Sign](assets/fr/32.webp)



Por último, para tener una visión completa de las posibilidades que ofrece "Co-Firma", activemos la opción "Web 2FA".


Esta función te permite utilizar una aplicación compatible con TOTP RFC-6238 como Google Authenticator / Ente Authenticator / Proton Authenticator / Authy 2FA / o Aegis Authenticator, para añadir un Layer extra de seguridad.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

En concreto, antes de firmar una transacción, tendrá que acercar su dispositivo con NFC y conexión a Internet a su Coldcard. Esto le llevará automáticamente a una página web coldcard.com, donde se le pedirá que introduzca el código de 6 dígitos de su solicitud. Si introduces el código correcto, la página web te mostrará un código QR que deberás escanear para obtener la ColdCardQ, o un código de 8 dígitos que deberás introducir en tu Mk4, para autorizar a tu dispositivo a firmar.





![Co-Sign](assets/fr/33.webp)



Tras escanear el código QR que aparece en su aplicación de doble autenticación y añadir su cuenta ColdCard Co-Sign (CCC), se le pedirá que verifique que todo está en orden introduciendo su código 2FA.



Introduzca su ColdCard en la parte posterior de su dispositivo NFC.



![Co-Sign](assets/fr/34.webp)



En la página web que se abre, introduce el código 2FA de tu aplicación favorita. A continuación, escanea el código QR que aparece con tu ColdCardQ (o introduce el código de 8 dígitos que aparece en tu Mk4).



![Co-Sign](assets/fr/35.webp)




Ahora hemos impuesto un límite de magnitud (21212 Sats), direcciones de destino y doble autenticación.



![Co-Sign](assets/fr/36.webp)



### 2- Exportar Wallet Multisig 2 contra 3 a Nunchuk



Exportemos Wallet Multisig 2 contra 3 a Nunchuk esta vez, como hicimos con Sparrow anteriormente.


Vaya a *Configuración > Carteras Multisig > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Esta vez elija la opción NFC para la exportación haciendo clic en el botón ColdcardQ del mismo nombre **"NFC "**.



![Co-Sign](assets/fr/37.webp)



En el Nunchuk, si es la primera vez que abres la aplicación, haz clic en **"Recuperar Wallet existente "**.



![Co-Sign](assets/fr/38.webp)



Si ya tienes una Wallet en la aplicación, haz clic en el **"+"** de la parte superior derecha y, a continuación, en **"Recuperar Wallet existente "**.



![Co-Sign](assets/fr/39.webp)




A continuación, elija **"Recuperar Wallet de COLDCARD "** y luego **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Por último, acerca la parte posterior de tu smartphone a la pantalla de tu ColdCardQ para importar la Wallet a través de NFC.



![Co-Sign](assets/fr/41.webp)



Nuestra cuenta y los satoshis depositados anteriormente a través de Sparrow wallet están de vuelta.



![Co-Sign](assets/fr/42.webp)



### 3- Probar las políticas de gasto predefinidas



Intentemos ahora hacer una transacción que viole las 2 condiciones de gasto que hemos establecido. **Intentaremos gastar más de 21212 Sats a una Address que no ha sido aprobada.** Intentemos enviar 22 222 Sats a una Address aleatoria.



![Co-Sign](assets/fr/43.webp)



Una vez creada la transacción, haga clic en los 3 puntitos de la esquina superior derecha para exportarla a su ColdCard.



![Co-Sign](assets/fr/44.webp)



A continuación, elige **"Exportar vía BBQR "**, y escanea el código QR que aparece con tu ColdCardQ.



![Co-Sign](assets/fr/45.webp)



Su ColdcardQ muestra entonces una advertencia que, al desplazarse hasta la parte inferior de la pantalla, aclara que la transacción infringe las condiciones de gasto, como era de esperar.



**Nótese que el dispositivo no nos dice de qué condiciones de gasto se trata, para evitar que un posible atacante intente burlar las restricciones.**




![Co-Sign](assets/fr/46.webp)



Si sigues validando pulsando **"INTRO "**, aparece el código QR que representa la transacción firmada. Si lo importas en el Nunchuk, podrás ver que sólo se ha aplicado una firma.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Realicemos exactamente la misma operación, pero esta vez con una transacción que respete el límite de magnitud (21212 Sats), y gaste los satoshis a una de las 2 direcciones que hemos preconfigurado.



Enviamos el Nunchuk 12121 Sats a una de nuestras 2 direcciones. Luego exportamos la transacción a nuestra ColdCard como se hizo anteriormente.



![Co-Sign](assets/fr/49.webp)




Después de importar la transacción sin firmar a nuestro ColdCardQ, veamos lo que se nos muestra esta vez.



Siempre aparece una advertencia, pero esta vez, desplazándonos hasta la parte inferior de la pantalla, vemos que se trata de validar la transacción mediante 2FA. El dispositivo nos pide que acerquemos nuestra ColdcardQ a nuestro terminal NFC conectado a Internet (smartphone o tableta), cosa que hacemos.



![Co-Sign](assets/fr/50.webp)



Se abre una página web en nuestro smartphone, pidiéndonos que introduzcamos nuestro código 2FA, lo que hacemos gracias a Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





A continuación, escanee el código QR que aparece en la página web, para autorizar a su ColdCard a firmar la transacción.


La transacción está ahora firmada por las 2 claves y, por tanto, es válida.



Si la función "Push Tx" está activada en su ColdCardQ, podrá transmitir la transacción directamente a la red con un simple toque en la parte posterior de su smartphone.



![Co-Sign](assets/fr/52.webp)




Si no tienes "Push tx" activado, pulsa el botón "QR" de tu ColdCardQ para mostrar la transacción firmada como un código QR, e impórtalo en el Nunchuk, de la misma forma que en el ejemplo anterior.



![Co-Sign](assets/fr/53.webp)



Esta vez observamos que se han aplicado 2 firmas, por lo que la transacción está lista para ser difundida en la red Bitcoin.



![Co-Sign](assets/fr/54.webp)




Hemos llegado al final de este tutorial, que te dará una visión general de las posibilidades que ofrece la funcionalidad Co-Sign integrada en los dispositivos ColdCardQ y Mk4 de Coinkite, así como su uso a través de monederos como Sparrow y Nunchuk.