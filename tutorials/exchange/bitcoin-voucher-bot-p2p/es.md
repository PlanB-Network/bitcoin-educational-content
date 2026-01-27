---
name: BitcoinVoucherBot P2P
description: Cómo comprar y vender Bitcoin P2P con BitcoinVoucherBot
---

![image](assets/cover.webp)



Seguimos oyendo hablar de BitcoinVoucherBot, un bot de Telegram creado para comprar Bitcoin sin [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) mediante transferencia bancaria SEPA. Por desgracia, desde noviembre de 2025, el BitcoinVoucherBot en su forma centralizada ya no está disponible como servicio sin KYC.



En esta guía veremos cómo funciona la nueva implementación que permite a los usuarios comprar y vender Bitcoin directamente en el nuevo mercado P2P (Peer-To-Peer), por lo que no hay KYC. Para contrarrestar las nuevas restricciones que amenazan cada vez más la libertad digital y la privacidad, los desarrolladores crearon esta extensión, dando a los usuarios la posibilidad de comprar y vender Bitcoin con un alto grado de anonimato a través de P2P (Peer-To-Peer). Veamos juntos cómo funciona este nuevo método de intercambio.



Para utilizar el servicio tendrás que hacer transferencias a través de Lightning Network. Así que asegúrate de que tienes una wallet compatible con este protocolo y que te permite utilizar una "LNURL" o "Lightning Address" para recibir y enviar fondos.



Entre los monederos compatibles podemos encontrar:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodia)
- [Wallet De Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodia con permuta a No Custodia)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



O cualquier wallet que tenga un "Lightning Address" y genere una factura Bolt11. Los monederos que generate una factura Bolt12 no están soportados actualmente. Para más información, véase la definición de [Bolt](https://planb.academy/resources/glossary/bolt).



Para este tutorial, dada su facilidad de uso inmediato, utilizaremos Wallet of Satoshi.



**Precaución**: Wallet of Satoshi, aunque popular entre los principiantes, es custodio, con control limitado sobre los fondos; úsala solo de forma transitoria, transfiriendo inmediatamente a una no custodio para tener plena soberanía. A partir de octubre de 2025, incluye un modo de autocustodia estable en todo el mundo en iOS/Android (actualiza la aplicación), con claves privadas autónomas, cambio entre modos, direcciones Lightning personalizadas y copia de seguridad de 12 palabras seed. Sin embargo, sigue siendo una solución provisional hasta la consolidación, prefiriendo wallet sin custodia madura para la gestión a largo plazo.



Muy bien Ahora podemos comenzar nuestro viaje, que le guiará paso a paso en la creación de su cuenta, la gestión de los partidos de compra y venta, y el uso de su área restringida.



## Wallet y matriculación



En primer lugar, si aún no lo tienes instalado en tu smartphone, descarga Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Si nunca has usado Wallet of Satoshi y quieres entender cómo funciona, te sugiero que sigas este tutorial para que puedas activarlo correctamente y hacer copias de seguridad de forma segura.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Ahora que tu wallet está lista, puedes empezar a enviar una pequeña cantidad de sats. Tenga en cuenta que, para completar su inscripción en la plataforma P2P (Peer-To-Peer), se le pedirá que envíe 1000 sats como medida de control: esto es para crear una barrera contra cualquier ataque de tipo phantom match (estafa), evitando que alguien se inscriba sin ningún filtro de spam.



![image](assets/it/02.webp)



Ya podemos abrir la plataforma P2P (Peer-To-Peer) para proceder a la inscripción. Puede iniciar sesión desde ordenadores de sobremesa o navegadores en smartphones, a través del Telegram BitcoinVoucherBot o mediante enlaces .onion para proporcionar un nivel de privacidad aún mayor.



si decides usar el enlace Tor .onion también te recomiendo "Tor Browser". Si aún no lo conoces puedes aprender más sobre él en este enlace:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Ahora elige cómo quieres llegar a la plataforma.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Escritorio / Navegador Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Será redirigido a la página principal.



pulse "Get Starter" para empezar de inmediato



![image](assets/it/03.webp)



En la siguiente pantalla tienes que elegir una contraseña e introducirla (casilla A), y luego repetirla (casilla B). Te recomiendo que guardes inmediatamente esta contraseña en un soporte de seguridad, que puede ser en un dispositivo digital seguro como el "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

o guarda tu contraseña en un soporte de papel (**advertencia**: esta no es una buena solución, aunque está bien si se trata de una solución temporal).



Marque la casilla de verificación en la que declara que no es un robot (casilla C). Tenga en cuenta No active el cifrado RSA a menos que sepa exactamente qué es y cómo funciona. No es necesario que hagas nada en esta fase. Haz clic en "Generar Avatar" ("Generate Avatar") (casilla D).



![image](assets/it/04.webp)



Ahora tienes que pagar los 1000 sats para completar la inscripción.



1. Empezando por arriba, primero ve tu "Avatar ID" generado aleatoriamente y extremadamente importante Guárdalo con cuidado, tal y como te aconsejé que hicieras con la contraseña.


2. A continuación, debe introducir su "Rayo Address" en el campo de abajo. Esto le permitirá recibir pagos si compra Bitcoin, u obtener reembolsos. Si utiliza Wallet Of Satoshi podrá copiar su Address haciendo clic en recibir.


3. Marque la casilla de verificación en la que declara que no es un robot.


4. Realiza el pago de 1000 sats para acceder a tu área restringida. Si no puedes encuadrarlo, haz clic sobre él con el ratón (en PC) o toca con el dedo (en Navegador/Telegram smartphones) para copiar la dirección que debes pegar en Wallet of Satoshi y completar el pago de la factura.



![image](assets/it/05.webp)



Este es su LNURL Address.



![image](assets/it/06.webp)



¡¡¡Enhorabuena!!! Has creado tu Avatar de forma permanente y puedes ver el resumen aquí. Una vez más, te recomiendo que guardes cuidadosamente tanto tu Avatar como tu contraseña, como ya te he sugerido antes.



Haga clic en "He guardado mis credenciales, continuar"



![image](assets/it/07.webp)



Ahora se encuentra en el corazón de la plataforma, donde puede ver todas las coincidencias comerciales con sus detalles. Para una visión más clara, a continuación verá las imágenes inherentes a la página web desde ordenadores de sobremesa.





- "Tipo" ("Type") define si se trata de una venta ("sell") o de una compra ("buy")
- "Cantidad" ("Amount"): indica cuántos sats está vendiendo el usuario si la coincidencia es de tipo "Vender", o cuántos Bitcoin está dispuesto a comprar si la coincidencia es de tipo "Comprar".
- "Precio BTC con margen" ("BTC Price with Margin"): muestra el precio teniendo en cuenta el margen aplicado por encima del valor marcado.
- "Margen" ("Margin") es el porcentaje que se aplica al precio de mercado, Con un signo menos (-) se obtiene un descuento sobre el precio de mercado, Con un signo más (+) se aplica una prima sobre el precio de mercado.
- "Método" ("Method") indica por qué motodo prefiere ser pagado el usuario.
- "Creador" es el avatar único utilizado por el usuario en la plataforma.
- "Rep" (Reputación) El nivel de reputación del usuario oscila entre -5 poco fiable y +5 extremadamente fiable.
- "Estado" ("Status"): indica el estado del partido. En la captura de pantalla de ejemplo, todos los partidos aparecen como "Abiertos" ("Open").
- "Expiración" ("Expiration"): muestra cuánto tiempo queda antes de que el partido expire y se cancele si no ha sido elegido por nadie.



![image](assets/it/08.webp)



Arriba a la derecha, haz clic en tu avatar para acceder a tu perfil.



![image](assets/it/09.webp)



Aquí puedes ver tu nombre de avatar, ID de usuario, fecha de creación y reputación, que reflejará positiva o negativamente tu comportamiento en las negociaciones.



![image](assets/it/10.webp)



En la sección Configuración puedes ver tu "Lightning Address", introducido durante el registro, y cambiarlo si es necesario. También tienes la opción de crear una Clave Pública, que como ya se ha mencionado sólo debes configurar si tienes los conocimientos adecuados. Se utiliza para cifrar los mensajes que intercambiará con su homólogo directamente desde su ordenador.



La función Notificación de Telegram es muy recomendable. Al activarla, aparecerá un código QR para que lo encuadres con la app Telegram: así recibirás notificaciones en tiempo real sobre todas las acciones relacionadas con tus partidos, directamente en el chat bot de Telegram.



![image](assets/it/11.webp)



Por último, encontrarás tu sección de referidos, con las ganancias generadas por los usuarios que has invitado. Desde aquí puedes utilizar el botón para compartir tu enlace o código QR y, un poco más abajo, ver una lista de coincidencias para hacer un seguimiento de tu reputación junto con la puntuación correspondiente.



![image](assets/it/12.webp)



## Crear un pedido para Comprar Bitcoin



Entrar en el Mercado: desde la barra de navegación principal, pulse sobre el símbolo del carrito "Mercado" ("Marketplace") para abrir el libro de pedidos. a continuación, iniciar un nuevo pedido: pulse el botón "Nuevo pedido" ("New Order") para iniciar el proceso.



![image](assets/it/13.webp)





- Establezca los detalles del pedido:
- Seleccione la opción "Comprar Bitcoin" ("Comprar Bitcoin").
- Introduzca la cantidad de sats que desee.
- Definir el margen de precios (entre -20% y +20% del valor de mercado).
- Elija el método de pago (Instant SEPA, etc.).
- Indica la moneda preferida.
- Confirmar pedido: haga clic en "Crear pedido" ("Confirmar pedido") para pasar a la fase de presentación.



![image](assets/it/14.webp)



Depósito requerido: se requiere un depósito equivalente al 10% del importe total, más una tasa de servicio, para activar el pedido.




- Pago del depósito: cuando se crea el pedido, el sistema genera automáticamente una factura relámpago. El depósito es solo temporal y se reembolsa cuando se completa el pedido.
- Características principales:
- Depósito de garantía: 10% del valor del pedido.
- Cuota de servicio: coste de utilización de la plataforma.
- Límite de tiempo: Tienes 5 minutos para realizar el pago, de lo contrario la transacción caduca.



![image](assets/it/15.webp)



Una vez efectuado el pago, la orden aparecerá en el libro y será visible para todos los usuarios, que podrán elegirla y aceptarla. Para crear una orden de venta, sólo tiene que hacer clic en "Vender Bitcoin" ("Sell Bitcoin"), introducir la cantidad de satoshi que desea vender, fijar el margen, seleccionar el método de pago y la divisa y, a continuación, proceder al ingreso del 10% como depósito de seguridad. Una vez completado, su partido será visible en la lista.



![image](assets/it/16.webp)



## Cómo aceptar un pedido



1. Los vendedores pueden ver una lista de todos los pedidos disponibles en el libro.


2. Compruebe los detalles: cada pedido muestra información como:




  - Cantidad de Bitcoin,
  - Margen sobre el precio,
  - Forma de pago,
  - Reputación de los usuarios.



![image](assets/it/17.webp)



3. Haga clic en el pedido para abrir la ficha completa con toda la información.


4. Pulse en "Vender Bitcoin" ("Sell Bitcoin") para aceptar la propuesta.



![image](assets/it/18.webp)



## Depósito exigido por el vendedor



Cuando se acepta el pedido, el sistema genera una factura para el pago. El depósito incluye:



- El importe total del pedido,



- la comisión de servicio.



El pago del depósito debe efectuarse dentro del plazo estipulado; de lo contrario, no se confirmará la transacción.



![image](assets/it/19.webp)



## Envío de instrucciones de pago



Una vez realizado el ingreso, la transacción aparecerá en el panel personal del vendedor, que deberá facilitar los datos al comprador para completar el pago en moneda fiduciaria.



1. El vendedor muestra la transacción activa en su panel.


2. Haga clic en "Enviar instrucciones de pago"


3. Introduzca toda la información necesaria para el pago en fiat (IBAN, beneficiario, dirección, motivo del pago, etc.).


4. Haga clic en "Enviar mensaje" ("Send Message") para transmitir los datos al comprador.



![image](assets/it/20.webp)



## Procedimiento de pago



El comprador recibe, dentro del chat de la plataforma, un mensaje con todos los datos necesarios para realizar el pago en moneda fiat:




- Datos bancarios: IBAN con nombre y dirección del titular de la cuenta del vendedor.
- Importe exacto: importe exacto en fiat que debe transferirse.
- Causal/descripción: texto que debe incluirse en la operación.
- Plazo: fecha límite para efectuar el pago.



La transferencia tiene lugar fuera del sistema P2P y debe realizarse a través de la propia entidad bancaria.



⚠️ **Nota importante:** la confirmación en la plataforma debe hacerse sólo después de haber organizado la transferencia o el pago en fiat a través de su banco.



![image](assets/it/21.webp)



## Confirmación de pago fiat



Este paso es crucial para el comprador y debe realizarse sólo después de verificar que el pago se ha enviado realmente.



1. Recepción de datos: el comprador ha recibido instrucciones de pago del vendedor.


2. Ejecución del pago: se organiza una transferencia fiat desde la propia cuenta bancaria.


3. Verificación: comprobar que la operación se ha procesado correctamente.


4. Confirme en la plataforma: haga clic en "Confirmar pago en fiat" ("Confirm fiat payment") en la página de operaciones.


El botón "Confirmar pago fiat" aparece en la sección de transacciones y sólo debe utilizarse después de verificar que el pago ha sido efectivamente enviado.



![image](assets/it/22.webp)



El último paso del proceso es que el vendedor confirme la recepción del pago en fiat, tras lo cual se liberan los satss al comprador.



![image](assets/it/23.webp)



## Conclusión



Con la esperanza de que este tutorial le ayude a utilizar un nuevo método para intercambiar Bitcoins o incluso simplemente comprarlos, ya sea para su propio depósito de valor o para empezar a dar vida a los pagos diarios. Aún así, sigue siendo una puerta a explorar para hacer frente a lo que está a punto de suceder en nuestro mundo digital.



La soga de los organismos que nos controlan se está tensando, para dar lugar a una Internet cada vez más controlada. Al comprar P2P, mantendrá sus compras en el anonimato total, sin dejar rastro ni repercusiones de seguimiento por parte de terceros.