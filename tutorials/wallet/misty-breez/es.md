---
name: Misty Breez
description: El Lightning Wallet sin proa.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez es un Wallet autoportante Lightning desarrollado por Breez basado en su Kit de Desarrollo de Software y la red **Liquid** desarrollada por BlockStream.


Viene con un enfoque completamente nuevo para operar sin un nodo Lightning: un **GAME CHANGER** potencial en las transferencias entre redes Bitcoin.


En este tutorial, describiremos cómo funciona esta cartera y le daremos una visión general completa.



## ¿Cómo funciona Misty Breez?



Misty Breez es una implementación sin nodo Lightning como backend. Se ha desarrollado sobre la base de Breez SDK y Liquid.



Liquid es una Layer paralela a la red Bitcoin, que ofrece mejoras significativas en velocidad y costes de transacción. Esta Layer permite a Misty Breez prescindir de un nodo Lightning y utilizar en su lugar servicios Exchange de terceros, como **Boltz**, para garantizar la interoperabilidad entre la Liquid Network y la Lightning Network. No te apures, volveremos sobre esto.



Por ahora, empecemos nuestra aventura con el Misty Breez Wallet.



## Primeros pasos con Misty Breez



La aplicación móvil de Misty Breez está disponible en plataformas de descarga oficiales como Google Play Store (en Android) y Apple Store (en iOS). También puede ser redirigido a la aplicación correcta desde el sitio web oficial [Misty Breez](https://breez.technology/misty/).



⚠️ Asegúrese de no confundir Misty Breez con el Breez Wallet.



⚠️ **IMPORTANTE**: Por la seguridad de tus bitcoins, es imprescindible descargar la aplicación desde plataformas oficiales para garantizar su autenticidad.



![download-misty-breez](assets/fr/01.webp)



En este tutorial, partiremos de un dispositivo Android. Sin embargo, cada uno de los pasos y características específicas detalladas en esta sección se aplican a iOS.



Tras la instalación, Misty Breez te da la opción de crear un nuevo Wallet o restaurar un antiguo Wallet Lightning para el que tengas las palabras de recuperación.


En este tutorial, elegimos crear una nueva cartera.



⚠️Misty Breez se encuentra actualmente en fase de desarrollo, por lo que le aconsejamos que empiece con cantidades razonables.



![create-wallet](assets/fr/02.webp)


### Guarda tus palabras de recuperación :


Una de las primeras cosas que debe hacer al crear una nueva cartera es hacer una copia de seguridad de sus 12 palabras de recuperación.


Aquí tienes algunos consejos sobre cómo hacer una copia de seguridad de tu frase de copia de seguridad.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Para hacer una copia de seguridad de sus frases, seleccione el menú **Preferencias > Seguridad** y, a continuación, la opción **Comprobar su frase de copia de seguridad**.



![backup](assets/fr/03.webp)


Para mayor seguridad, también puedes **crear un código PIN** para autenticar el acceso a tu Wallet.




Encuentra tu moneda local entre la multitud de monedas aceptadas por Misty Breez. Configura tu moneda en el menú **Preferencias > Monedas fiduciarias** y, a continuación, selecciona la moneda o monedas que necesites.



![devises](assets/fr/04.webp)



### Realizar las primeras transacciones


Si ya está familiarizado con la gama Breez, no se sentirá desanimado por la intuitiva Interface de Misty Breez.



En el menú **Balance** de Interface, haz clic en la opción **Receive** para crear facturas para recibir tus bitcoins en tu Wallet.



⚠️ Misty Breez te pedirá que actives las notificaciones de la aplicación en los ajustes de tu teléfono para darte derecho a un Address Lightning.



Con Misty Breez, puedes :




- Reciba bitcoins en el Lightning Network desde **100 satoshis** hasta **25.000.000 satoshis**.
- Recibe bitcoins en la red principal de Bitcoin a partir de **25.000 satoshis**.



![transactions](assets/fr/05.webp)



Aquí empieza la magia de Misty Breez.


A diferencia de Breez Wallet, que te proporciona un nodo Lightning y te pide que cubras tú mismo los costes de abrir y cerrar canales de pago, Misty Breez no te pide que hagas nada. Como ya se ha mencionado, Misty Breez ni siquiera funciona sobre la base de un nodo Lightning.



Echemos un vistazo entre bastidores.



En realidad, posees una cartera Liquid que está asociada a tu cartera Misty Breez. Lógicamente, manejará L-BTC (Liquid Bitcoin) a tipos fijos asociados a servicios de conversión de satoshis submarinos de terceros que le permitirán interoperar con la Lightning Network.



Cuando recibes un pago en tu Misty Breez Wallet, el remitente te envía satoshis que pasarán por un servicio de conversión como Boltz (actualmente utilizado por Misty Breez), para convertir los satoshis enviados en L-BTC que serán recibidos en tu Misty Breez Wallet (Liquid Wallet asociado).


He aquí un diagrama simplificado del proceso entre bastidores.



![lnswap-in](assets/fr/06.webp)



Haga clic en la Interface en el menú **Saldo**, haga clic en la opción **Enviar** para pagar una Invoice Relámpago.


Introduzca la Invoice Lightning, la Address Lightning de su destinatario o simplemente escanee el código QR de la Invoice para efectuar el pago.



![send-bitcoins](assets/fr/07.webp)



Entre bastidores, habilitas la Liquid Wallet asociada a tu Wallet Misty Breez para convertir el equivalente de L-BTC en satoshis a través de Boltz, y luego transfieres estos satoshis a la Wallet Lightning de tu destinatario (presente en la Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Esta característica de la infraestructura de Misty Breez permite a los usuarios realizar transacciones incluso cuando Misty Breez está desconectado.



Para los más experimentados, también hay un menú **Preferencias > Desarrolladores** que ofrece más detalles sobre :




- La versión del kit de desarrollo de software Breez.
- La clave pública de tu Misty Breez Wallet.
- El prestatario, el identificador único derivado de la clave pública primaria.
- El saldo de tu cartera.
- Consejo Liquid, para enviar pequeñas cantidades de L-BTC.
- La punta Bitcoin, para enviar pequeñas cantidades de Bitcoin.



También puede realizar ciertas acciones, como sincronizar con la Liquid Network, hacer una copia de seguridad de sus claves, compartir su registro de actividad y elegir volver a escanear la Liquid Network.



![dev-mode](assets/fr/09.webp)


¡Enhorabuena! Ahora ya conoce bien la cartera Misty Breez y su contribución a las transacciones entre redes Bitcoin. Si este tutorial te ha resultado útil, danos un Green pulgar. Estaremos encantados de recibir noticias suyas.



Para ir más lejos, también te recomiendo que descubras nuestro tutorial sobre el Aqua Wallet, que funciona de forma similar al Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125