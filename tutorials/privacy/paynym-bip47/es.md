---
name: BIP47 - PayNym
description: Utilizar un código de pago reutilizable en Ashigaru
---
![cover](assets/cover.webp)



El peor error de privacidad que puedes cometer en Bitcoin es reutilizar direcciones. Cada vez que una misma dirección recibe varios pagos, estas transacciones se vinculan entre sí, proporcionando al mundo un mapa de tus transacciones. Por lo tanto, se recomienda encarecidamente que siempre generate una dirección única para cada recibo. Pero para algunas aplicaciones de Bitcoin, esto no es una cuestión sencilla.



BIP47, propuesto por Justus Ranvier en 2015, ofrece una respuesta elegante a este problema. Introduce el concepto de **código de pago reutilizable**: un identificador único que permite recibir un número prácticamente ilimitado de pagos de bitcoin onchain, sin reutilizar nunca una dirección. Gracias a un mecanismo criptográfico basado en un intercambio ECDH (*Diffie-Hellman en curvas elípticas*), cada pago al mismo código da lugar a una dirección en blanco, específica para la relación entre el remitente y el destinatario.



![Image](assets/fr/01.webp)



Este principio de BIP47 es aplicado en particular por **PayNym**, el sistema originalmente desarrollado por Samourai Wallet y ahora retomado por Ashigaru. En este tutorial, veremos cómo activar su PayNym, intercambiar códigos de pago con un corresponsal y realizar transacciones sin reutilizar una dirección.



No voy a entrar aquí en el funcionamiento detallado del BIP47. Si quieres profundizar en el tema, consulta el capítulo 6.6 de mi curso de formación BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Requisitos previos



Para seguir este tutorial, todo lo que necesitas es un wallet en la aplicación Ashigaru. Si no sabes cómo descargar, verificar, instalar la aplicación o crear un wallet, te recomiendo que primero consultes este tutorial:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Solicitar PayNym



El primer paso es reclamar su PayNym. Esta operación sólo debe realizarse una vez por cada wallet. Asocia su código de pago BIP47 derivado de su seed (`PM...`) con un identificador único específico de la aplicación PayNym. Este identificador más corto y legible puede transmitirse a sus corresponsales para facilitar los intercambios, sin tener que compartir el código BIP47 largo y completo.



Para ello, haga clic en la imagen de su PayNym en la parte superior izquierda de la interfaz y, a continuación, en su código de pago `PM...`.



![Image](assets/fr/02.webp)



A continuación, haga clic en los tres puntitos de la esquina superior derecha y seleccione "Reclamar PayNym".



![Image](assets/fr/03.webp)



Confírmelo pulsando el botón "RECLAMAR SU PAYNYM".



![Image](assets/fr/04.webp)



Actualice la página: su PayNym ID aparece ahora debajo de su imagen, justo encima de su código de pago BIP47.



![Image](assets/fr/05.webp)



Su PayNym ya está activo y listo para ser utilizado en sus primeras transacciones BIP47.



## Conectar con un contacto



Existen dos tipos de conexión entre PayNym: **follow** y **connect**. La operación `follow` es completamente gratuita. Establece un enlace entre dos PayNym a través de Soroban, un protocolo de comunicación encriptado basado en Tor desarrollado por el equipo Samourai y adoptado por Ashigaru. Este enlace permite a dos usuarios seguidos intercambiar información de forma privada, en particular para coordinar transacciones colaborativas como Stowaway o StonewallX2, que veremos en otro tutorial. Este paso es específico de PayNym y no forma parte del protocolo BIP47.



![Image](assets/fr/06.webp)



La operación de conexión (`connect`), por su parte, requiere una transacción on-chain. Consiste en realizar una transacción de notificación tal y como se define en BIP47. Esta transacción Bitcoin contiene metadatos en una salida `OP_RETURN`, que establece un canal de comunicación cifrado entre el pagador y el receptor. Desde este canal, el pagador podrá generate direcciones receptoras únicas para cada pago, y el receptor será notificado de estos pagos, y podrá generate las claves privadas asociadas a las direcciones para gastar estos fondos posteriormente.



Esta transacción de notificación tiene un coste: la tasa mining y 546 sats enviada a la dirección de notificación del destinatario para señalar la conexión. Una vez establecida la conexión, puede realizarse un número casi infinito de pagos a través de BIP47.



En pocas palabras:




- follow": gratuito, establece comunicación encriptada vía Soroban, útil para las herramientas colaborativas de Ashigaru;
- `Connect`: con cargo, realiza la transacción de notificación BIP47 para activar el canal entre pagador y receptor.



Para interactuar con un PayNym, primero hay que *seguirlo*. Este es el primer paso antes de establecer una conexión BIP47. Digamos que quieres enviar pagos recurrentes a PayNym `+instinctiveoffer10`.



Ve a tu página PayNym en Ashigaru y haz clic en el botón `+` de la parte inferior derecha de la interfaz.



![Image](assets/fr/07.webp)



A continuación, puede pegar el código de pago completo del destinatario o escanear su código QR.



![Image](assets/fr/08.webp)



Si sólo tiene su PayNym ID, vaya a [Paynym.rs](https://paynym.rs/) para encontrar el código QR asociado a su código de pago.



![Image](assets/fr/09.webp)



Una vez que hayas escaneado el código QR, haz clic en el botón `FOLLOW` para seguir el PayNym.



![Image](assets/fr/10.webp)



La acción `FOLLOW` es suficiente para las transacciones en colaboración (*cahoots*). Sin embargo, para enviar pagos BIP47, es necesario establecer una conexión: haga clic en `CONNECT` para realizar la transacción de notificación.



![Image](assets/fr/11.webp)



A continuación, la transacción notificada se difunde en la red. Espera a que tenga al menos una confirmación antes de realizar tu primer pago.



![Image](assets/fr/12.webp)



## Realizar un pago BIP47



Ahora está conectado con el destinatario y puede enviar un pago a una dirección única, generada automáticamente mediante el protocolo BIP47, sin ningún intercambio previo con el destinatario.



Desde la página principal de PayNym, haga clic en el contacto al que desea enviar un pago.



![Image](assets/fr/13.webp)



En la parte superior derecha de la interfaz, haga clic en el icono de la flecha.



![Image](assets/fr/14.webp)



Introduzca el importe que desea enviar. No es necesario introducir una dirección de recepción: se obtendrá automáticamente mediante el protocolo BIP47.



![Image](assets/fr/15.webp)



Compruebe cuidadosamente los detalles de la transacción, incluidas las comisiones, y luego arrastre la flecha verde de la parte inferior de la pantalla para firmar y emitir la transacción.



![Image](assets/fr/16.webp)



La transacción ha sido enviada.



![Image](assets/fr/17.webp)



En este ejemplo, el pago se realizó a otro de mis monederos PayNym. Por lo tanto, puedo ver que ha llegado a mi otro Ashigaru wallet, sin que se haya intercambiado ninguna dirección manualmente: sólo se ha utilizado el identificador PayNym.



![Image](assets/fr/18.webp)



Ya sabe cómo utilizar los códigos de pago reutilizables BIP47 gracias a la implementación de PayNym en la aplicación Ashigaru. Ahora puedes compartir este código de pago con cualquier persona que quiera enviarte pagos (especialmente pagos recurrentes). También puedes publicar tu PayNym ID en tu página web o redes sociales para recibir donaciones.



Para profundizar en el conocimiento de este protocolo, comprender en detalle su funcionamiento y sus implicaciones para la confidencialidad, le recomiendo encarecidamente que siga mi curso BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c