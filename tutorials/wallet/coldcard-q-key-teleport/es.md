---
name: COLDCARD Q - Key Teleport
description: ¿Qué es el teletransporte de llaves y cómo se utiliza?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



¿En qué consiste la función **Key Teleport** que ofrece Coinkite con su dispositivo estrella ColdCardQ?



**Key Teleport** le permite transferir de forma segura datos confidenciales entre 2 ColdCardQs. El canal de transmisión ni siquiera necesita estar cifrado, y puede ser público.



Esto se puede utilizar para transferir:





- frases **gW-0** (el maestro seed de ColdCard Q o los secretos almacenados en la [Bóveda seed] de ColdCardQ(https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **notas confidenciales y contraseñas**: puede ser cualquier secreto o todo el directorio [Notas confidenciales y contraseñas] (https://coldcard.com/docs/secure_notes/) de su ColdCardQ.
- una copia de seguridad de toda su **ColdCardQ**: la ColdCardQ que reciba esta copia de seguridad no debe tener una seed Master para que esto funcione.
- gW-3 (**Transacciones Bitcoin parcialmente firmadas**) como parte de un esquema de firma múltiple.



Para ello es necesario haber actualizado el [firmware del dispositivo a la versión v1.3.2Q](https://coldcard.com/docs/upgrade/) o superior.



## ¿Cómo se utiliza el teletransporte de llaves?



### 1- Para transferir cualquier tipo de datos



Aquí veremos la transferencia de frases seed, notas, contraseñas o una transferencia completa de una copia de seguridad ColdCardQ. El caso de las transferencias PSBT para transacciones con varias firmas se tratará más adelante.



#### Prepara el dispositivo para recibir los secretos



En el menú **"Avanzado / Herramientas**" de tu ColdCardQ, selecciona **"Teletransporte de teclas (inicio)**".


En la pantalla siguiente, se propone una contraseña de 8 cifras, aquí "20420219". Deberá comunicar esta contraseña al remitente. Utiliza sms, por ejemplo, para enviar esta contraseña, o tu sistema de mensajería segura favorito, o incluso una llamada de voz.



A continuación, haga clic en el botón **"Intro**" de su ColdCardQ para pasar al siguiente paso.




![CCQ-key-teleport](assets/fr/01.webp)




Se genera un código QR en la pantalla. Una vez más, tendrá que comunicar este código QR al "remitente" de ColdCardQ. La forma más sencilla de hacerlo es mediante una videollamada.



**NO ENVÍE ESTE CÓDIGO QR POR EL MISMO CANAL DE TRANSMISIÓN UTILIZADO PARA ENVIAR LA CONTRASEÑA ANTERIOR DE 8 DÍGITOS**.



![CCQ-key-teleport](assets/fr/02.webp)



*Para quienes estén interesados, tratemos de entender el mecanismo subyacente que permite transferir secretos a través de canales no seguros*



*Lo que realmente estamos haciendo aquí es iniciar una transferencia de secretos a través del método Diffie-Hellman, cubierto en el curso BTC204 que he incluido a continuación*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Actualmente tenemos:*




- generado un par de claves efímeras (pública/privada respectivamente Ka y ka con Ka=G.ka, siendo G el punto generador de ECDH), y una contraseña de 8 dígitos.
- utilizó esta contraseña para cifrar la clave pública (Ka) mediante AES-256-CTR y, a continuación, transmitió esta contraseña a través de un canal de comunicación A a la ColdCardQ "emisora".
- por último, transmitimos el paquete cifrado al remitente a través del código QR anterior, utilizando un segundo canal de comunicación B distinto del 1.



#### Preparar el dispositivo que enviará los secretos



Desde el dispositivo emisor, haga clic en el botón **"QR "** para escanear el código QR que le ha enviado el dispositivo receptor y, a continuación, introduzca la contraseña de 8 dígitos que se le ha comunicado en el paso anterior a través de un canal independiente. Ya estamos listos para iniciar el envío de datos desde el dispositivo "emisor".



**Por favor, no introduzca la contraseña de 8 dígitos incorrectamente, ya que no se mostrará ningún mensaje de error y el proceso continuará. Sin embargo, la transferencia final de datos fallará y tendrás que empezar de nuevo**.



![CCQ-key-teleport](assets/fr/03.webp)



*Para los más curiosos, echemos otro vistazo a lo que nos traemos entre manos en materia de criptografía y transferencia de secretos*




- importamos los datos cifrados escaneando el código QR en el dispositivo receptor.
- luego los desciframos utilizando la contraseña de 8 dígitos que se nos ha transmitido por un canal secundario.
- por tanto, estamos en posesión de la clave pública (Ka) generada inicialmente por el receptor.
- A continuación, generate un nuevo par de claves efímeras (Kb/kb, con Kb=G.kb) en el dispositivo emisor, que utilizamos para aplicar ECDH a Ka. Por tanto, realizamos la operación kb.Ka=Ks , donde Ks se denomina **"Clave de sesión"**.




Ahora se le pide que elija la naturaleza de los secretos que se transmitirán entre las 2 ColdCardQ (notas confidenciales, contraseña, copia de seguridad completa, semillas contenidas en su cámara acorazada, maestro del dispositivo seed).



![CCQ-key-teleport](assets/fr/04.webp)



Aquí nuestro secreto será un mensaje corto eligiendo **"Mensaje de Texto Rápido "**. Escribe tu mensaje (para nosotros "PlanB Network rocks") y pulsa **"ENTER "**.


A continuación, el dispositivo genera una nueva contraseña aleatoria denominada **"Contraseña de teletransporte "** , en el ejemplo "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Pulsa **"INTRO "** y se te presentará un nuevo código QR. Haz que lo escanee el dispositivo receptor. Y en un canal de comunicación diferente, transmite la **"Contraseña de teletransporte "** al receptor.



![CCQ-key-teleport](assets/fr/06.webp)



*De nuevo, para los curiosos, durante esta etapa:*




- después de seleccionar los secretos a transmitir, generate una nueva contraseña aleatoria llamada **"Teleport Password"**.
- a continuación, ciframos los secretos mediante AES-256-CTR utilizando la **"Clave de sesión"**, "Ks", generada en el paso anterior.
- anteponemos al paquete ya cifrado con la **"Clave de sesión "** nuestra clave pública Kb, y luego añadimos otro Layer de cifrado AES-256-CTR con la **"Contraseña de teletransporte "**. A continuación, todo se codifica como un código QR




#### Finalizar la transferencia de secretos al dispositivo receptor



Pulse el botón **"QR "** para escanear el código QR presentado por el dispositivo de envío a través del canal visio. Se le pedirá que introduzca su **"Contraseña de telepuerto "** para nosotros "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





A continuación, los datos se descifran y se hacen inteligibles para el dispositivo receptor. El mensaje recibido es, en efecto, "PlanB Network rocks". Y eso es todo.



![CCQ-key-teleport](assets/fr/08.webp)



*¿Qué ocurrió realmente durante esta última etapa :*?




- hemos descifrado los datos transmitidos por el remitente utilizando el **"Teleport Password "**
- tenemos por tanto la clave pública Kb y nuestro mensaje secreto cifrado por la **"Clave de Sesión "**, "Ks". Pero, ¿cómo podemos hacer esto ya que, como receptor, no conocemos Ks, que fue creada por el emisor?
- Necesitamos aplicar nuestra clave privada "ka" del paso inicial **"Preparar el dispositivo que recibirá los datos"** a la clave pública *Kb*.
- De hecho, calculando ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, encontramos Ks. Que finalmente se utiliza para descifrar el mensaje secreto.



### 2- Para transferir PSBT a Multisig (avanzado)



Esto presupone que su Wallet Multisig ya ha sido creada y que su dispositivo ColdCardQ ya ha sido preconfigurado para poder realizar transacciones con varias firmas. Si no es el caso, encontrará explicaciones [aquí](https://coldcard.com/docs/Multisig/) en el sitio web de Coinkite.



Un rápido recordatorio de lo que es una Wallet (Multisig) multifirma.



Normalmente, para gastar sus fondos Wallet, sólo se necesita una clave privada para desbloquear los UTXO asociados a sus direcciones.


En el caso de una Wallet Multisig, pueden necesitarse hasta 15 claves privadas y, por tanto, 15 firmas para gastar los fondos. Esto se conoce como una cartera "M de N", con N entre 1 y 15 y M el número de firmas necesarias para que los fondos sean gastables. Por ejemplo, una Wallet Multisig 3 de 5 requerirá al menos 3 firmas de las 5 posibles.



El reto consiste entonces en coordinarse entre los firmantes para firmar a su vez una "PSBT" para la "Partially Signed Bitcoin Transaction". En este contexto, se puede utilizar "**Key Teleport**" para transmitir la PSBT entre los cofirmantes de forma sencilla y confidencial. Una simple videollamada entre cofirmantes bastará.



Así se hace en una Multisig 3 de 4.



**Firmante 1:**



El firmante 1 importa y firma la PSBT. Por último, hace clic en **"T "** para utilizar **"Key Teleport "** para transmitir la PSBT al firmante 2.



![CCQ-key-teleport](assets/fr/09.webp)




Tras seleccionar al firmante 2 pulsando **"INTRO "**, se proporciona una "CONTRASEÑA DE TELEPUERTO" (aquí JJ YC AB 6A), que debe transmitirse al firmante 2 a través de otro canal de comunicación. Por ejemplo, un SMS o una llamada de voz, pero **no** una videollamada.



Pulse de nuevo **"INTRO "** y aparecerá un código QR que representa el PSBT firmado por 1 y encriptado por la "CONTRASEÑA TELEPUERTO".



![CCQ-key-teleport](assets/fr/10.webp)



**Firmante 2:**



El firmante 2 escanea el código QR que le presenta el firmante 1. A continuación, introduce la "CONTRASEÑA TELEPUERTO" transmitida a través del canal de comunicación secundario para descifrar los datos transmitidos.



El firmante 2 firma la transacción y, a continuación, pulsa **"T "** para transmitir el PSBT al firmante 3 a través de "Key Teleport".


Es evidente que ya se han aplicado 2 firmas. Sólo falta la del firmante 3 para que la transacción sea válida. Seleccione el firmante 3 haciendo clic en **"INTRO "**.



![CCQ-key-teleport](assets/fr/11.webp)



Y se crea una nueva "TELEPORT PASSWORD", seguida de nuevo por un código QR que codifica el PSBT firmado por 1 y 2 y cifrado por esta nueva "TELEPORT PASSWORD" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Firmante 3:**



Repita el mismo paso anterior.


El firmante 3 escanea el código QR que le presenta el firmante 2. A continuación, introduce la "CONTRASEÑA TELEPUERTO" transmitida por el canal de comunicación secundario.



El firmante 3 firma la transacción y esta vez, dado que se han aplicado 3 de las 4 firmas, la transacción se indica como finalizada, y está lista para su distribución a través de diversos medios (tarjeta SD, NFC, QR, etc.).



![CCQ-key-teleport](assets/fr/13.webp)



Si la función "Push Tx" de su ColdCardQ está activada, sólo tiene que pegar su ColdCardQ en la parte posterior de cualquier dispositivo conectado a Internet con NFC (smartphone/tableta) para transmitir la transacción a través de la red Bitcoin.



![CCQ-key-teleport](assets/fr/14.webp)



*Para las transferencias de PSBT de un firmante a otro, se utiliza simplemente el "teletransporte de claves" mediante una "contraseña de teletransporte" en cada etapa, que encripta el PSBT a medida que se transfiere de un firmante a otro. Como los datos transmitidos no pueden utilizarse para robar fondos, no hay necesidad de un Diffie-Hellman, como ocurre cuando se envían secretos altamente confidenciales (seed, contraseña, etc...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Fuente: [Sitio web oficial de ColdCard](https://coldcard.com/)*