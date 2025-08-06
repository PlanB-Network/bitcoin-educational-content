---
name: Jade Plus - Verde
description: Configura fácilmente Jade Plus con Green
---
![cover](assets/cover.webp)

Jade Plus es un monedero hardware exclusivo para Bitcoin diseñado por Blockstream. Es el sucesor del clásico Jade, con mejoras en el software, más opciones y una ergonomía rediseñada para un uso más intuitivo. Esta nueva versión cuenta con una magnífica pantalla LCD de 1,9 pulgadas, con una gama de colores más amplia que su predecesora. También se han optimizado los botones y la navegación por los menús.

La Jade Plus se puede utilizar de varias formas: mediante una conexión por cable USB-C, en modo "*Air-Gap*" con una tarjeta micro SD (requiere adaptador), por Bluetooth o incluso intercambiando códigos QR gracias a la cámara integrada. Este monedero físico funciona con pilas.

Está disponible desde 149,99 dólares en la versión básica de color negro, y el precio puede aumentar hasta 20 dólares en las versiones "*Genesis Grey*" o "*Lunar Silver*". La Jade Plus es, por tanto, una opción interesante, con funcionalidades avanzadas comparables a las de carteras hardware de gama alta como la Coldcard Q o la Passport V2, pero a un precio bastante bajo, cercano a los modelos de gama media.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus es compatible con la mayoría de los programas de gestión de carteras. He aquí un resumen de la compatibilidad en el momento de redactar este documento (enero de 2025):

| Escritorio | Móvil | USB | Bluetooth | QR | JadeLink | Software de gestión

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Verde | 🟢 | 🟢 | 🟢 (Móvil) | 🟢 | 🔴 | 🔴

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴

| Gorrión | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢

| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

| Custodio | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢

En este tutorial, vamos a configurar y utilizar el Jade Plus con la aplicación móvil Green Wallet de Blockstream a través de una conexión Bluetooth. Esta configuración es ideal para principiantes. Si buscas un enfoque más avanzado, te recomiendo que eches un vistazo a este tutorial en el que utilizamos el Jade Plus con Sparrow Wallet en modo códigos QR:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## El modelo de seguridad Jade Plus

El Jade Plus utiliza un modelo de seguridad basado en un "elemento seguro virtual", materializado por un "oráculo ciego". En concreto, este mecanismo combina el PIN elegido por el usuario, un secreto alojado en el Jade y un secreto en poder del oráculo (un servidor mantenido por Blockstream), para crear una clave AES-256 distribuida entre dos entidades. Durante la iniciación, un intercambio ECDH asegura la comunicación con el oráculo y cifra la frase de recuperación en el monedero físico. En términos prácticos, cuando se quiere acceder a la semilla para firmar transacciones, se necesita acceso a :


- Al propio dispositivo Jade Plus;
- Para PIN para desbloquear el dispositivo ;
- Y al secreto del oráculo.

La mayor ventaja de este enfoque es la ausencia de un único punto de fallo a nivel de hardware, ya que si un atacante consigue acceder a tu Jade, extraer las claves requiere comprometer simultáneamente el Jade y el oráculo. Este modelo también significa que Jade Plus es totalmente de código abierto, evitando las restricciones asociadas al uso de verdaderos elementos físicos seguros, como los utilizados en Ledger, por ejemplo.

La desventaja de este sistema es que el uso de Jade Plus depende del oráculo mantenido por Blockstream. Si este oráculo se vuelve inaccesible, ya no es posible utilizar el monedero físico directamente con el PIN. Sin embargo, esto no significa que sus bitcoins estén perdidos, ya que aún pueden recuperarse utilizando su frase de recuperación, que puede introducir en Jade Plus en modo "*sin estado*". Para evitar esta dependencia, también puedes configurar y gestionar tu propio servidor oracle.

## Unboxing del Jade Plus

Cuando recibas tu Jade Plus, comprueba que la caja y el precinto están en buen estado para asegurarte de que el paquete no ha sido abierto.

![JADE-PLUS-GREEN](assets/fr/02.webp)

En la caja encontrará :


- Le Jade Plus;
- Cable USB-C;
- Tarjetas para grabar su frase mnemotécnica como palabras o como "*CompactSeedQR*";
- Algunas instrucciones de uso ;
- Un cordón;
- Algunas pegatinas.

![JADE-PLUS-GREEN](assets/fr/03.webp)

El dispositivo tiene 4 botones de navegación:


- El botón de la parte inferior derecha enciende el Jade;
- El botón grande de la parte frontal del aparato sirve para seleccionar un elemento;
- Los dos pequeños botones de la parte superior permiten navegar a izquierda y derecha;
- También puede seleccionar un elemento pulsando simultáneamente los dos botones situados en la parte superior del dispositivo.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Crear un nuevo monedero Bitcoin

Pulsa el botón de inicio.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Haz clic en "*Configurar Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Elija "Iniciar configuración". La opción "*Configuración avanzada*" hace lo mismo, pero con acceso a la configuración avanzada.

![JADE-PLUS-GREEN](assets/fr/07.webp)

A continuación, haga clic en "*Crear un nuevo monedero*" para generar una nueva semilla.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Haz clic en el botón "*Continuar*" para mostrar tu nueva frase de recuperación.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Tu Jade Plus muestra tu frase mnemotécnica de 12 palabras. **Esta frase mnemotécnica te da acceso total y sin restricciones a todos tus bitcoins. Cualquiera que posea esta frase puede robar tus fondos, incluso sin tener acceso físico a tu Jade Plus. La frase de 12 palabras restablece el acceso a tus bitcoins en caso de pérdida, robo o rotura de tu Jade. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.

Puede escribirlo en el cartón suministrado en la caja o, para mayor seguridad, le recomiendo grabarlo en una base de acero inoxidable para protegerlo de incendios, inundaciones o derrumbes.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Para más información sobre la forma correcta de guardar y gestionar tu frase mnemotécnica, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Obviamente, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Esta cartera de muestra sólo se utilizará en Testnet y se borrará al final del tutorial

Haz clic en la flecha de la derecha de la pantalla para que aparezcan las siguientes palabras.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Una vez que hayas guardado tu frase, Jade Plus te pedirá que la confirmes. Selecciona la palabra correcta según el orden utilizando los botones de la parte superior del dispositivo y pulsa el botón central para pasar a la siguiente palabra.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Conexión de Jade Plus a Green Wallet

En este tutorial, utilizaremos la aplicación Green Wallet para gestionar el monedero alojado en el Jade Plus. Este método es especialmente adecuado para principiantes. Si quieres gestionar tu monedero Bitcoin con más detalle, también puedes utilizar Sparrow Wallet, que trataremos en otro tutorial:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Para obtener instrucciones sobre la instalación y configuración de la aplicación Blockstream Green, consulte la primera parte de este otro tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Una vez en la aplicación Blockstream Green, haz clic en el botón "*Configurar una nueva cartera*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Seleccione "*On Hardware Wallet*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Activa el Bluetooth en tu smartphone y haz clic en el botón "*Conecta tu Jade*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Autoriza a la aplicación Verde a acceder a las conexiones Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

La aplicación busca tu Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

En el Jade Plus, haz clic en el menú "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Selecciona tu dispositivo en la aplicación Verde.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Confirma el código de emparejamiento en tu Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green te ofrece una prueba para asegurarte de que tu Jade es auténtico. Haga clic en el botón para hacerlo.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Confirmar en el Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

El color verde confirma que el dispositivo es auténtico.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Configurar el código PIN

Haz clic en el botón "*Continuar*" para elegir el código PIN de tu Jade.

![JADE-PLUS-GREEN](assets/fr/24.webp)

El código PIN desbloquea tu Jade. Es, por tanto, una protección contra el acceso físico no autorizado. Este código PIN no interviene en la derivación de las claves criptográficas de su monedero. Por lo tanto, incluso sin acceso a este código PIN, la posesión de su frase mnemotécnica de 12 palabras le permitirá recuperar el acceso a sus bitcoins. Te recomendamos que elijas un código PIN lo más aleatorio posible. Y asegúrate de guardar este código en un lugar distinto de donde esté almacenado tu Jade (por ejemplo, en un gestor de contraseñas).

Elija el código PIN de 6 dígitos de su Jade, utilizando los botones derecho e izquierdo para desplazarse por los dígitos y el botón central para confirmar la introducción de un dígito.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Confirme su PIN por segunda vez.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Tu monedero bitcoin ha sido creado.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Crear una cuenta Bitcoin

Ahora debe crear una cuenta dentro de su cartera. Haga clic en el botón "*Crear una cuenta*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Elija "*Estándar*" si desea crear una cartera clásica de una sola firma.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Para más información sobre la opción "*2FA*", puedes seguir este otro tutorial:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Su cuenta ha sido creada.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Si desea personalizar su Cartera Verde, haga clic en los tres puntitos de la parte superior derecha.

![JADE-PLUS-GREEN](assets/fr/31.webp)

La opción "*Renombrar*" le permite personalizar el nombre de su cartera, lo que resulta especialmente útil si gestiona varias carteras en la misma aplicación. El menú "*Unidad*" le permite cambiar la unidad básica de su cartera. Por ejemplo, puede elegir mostrarla en satoshis en lugar de bitcoins. Por último, el menú "*Parámetros*" le da acceso a otras opciones. Aquí, por ejemplo, encontrarás tu clave pública extendida y su descriptor, útil si estás planeando configurar un monedero sólo para relojes desde tu Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Para volver a conectarte a tu Jade después de apagarlo, pulsa el botón de encendido/apagado situado en la parte inferior del dispositivo. En la aplicación Verde, selecciona tu dispositivo en la página de inicio:

![JADE-PLUS-GREEN](assets/fr/33.webp)

A continuación, introduce el código PIN de tu Jade y volverás a estar conectado.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Tu Jade se desbloquea a través del "elemento seguro virtual" de Blockstream (consulta la primera sección de este tutorial). Esto requiere una conexión Bluetooth con la aplicación Green. Si tienes problemas con la conexión Bluetooth durante el desbloqueo, intenta disociar y volver a asociar los dos dispositivos. Si el problema persiste, aún puedes desbloquear tu Jade seleccionando la opción "*QR Scan*" y siguiendo las instrucciones disponibles [en el sitio web de Blockstream](https://jadefw.blockstream.com/pinqr/index.html).

Antes de recibir tus primeros bitcoins en tu monedero, **te aconsejo encarecidamente que realices una prueba de recuperación en vacío**. Toma nota de alguna información de referencia, como tu xpub o la primera dirección de recepción, luego borra tu monedero en la aplicación Green y en el Jade Plus mientras esté vacío (`Opciones -> Dispositivo -> Reinicio de fábrica`). A continuación, intenta restaurar tu monedero utilizando tus copias de seguridad en papel de la frase mnemotécnica. Comprueba que la información de la cookie generada tras la restauración coincide con la que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables. Para saber más sobre cómo realizar una recuperación de prueba, consulta este otro tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Recibir bitcoins

Ahora que su monedero Bitcoin está configurado, ¡está listo para recibir sus primeros sats! Solo tienes que hacer clic en el botón "*Recibir*" de la aplicación Green.

![JADE-PLUS-GREEN](assets/fr/35.webp)

El verde muestra una dirección de recepción, pero antes de utilizarla es imprescindible comprobarla en el Jade para confirmar que realmente pertenece a nuestra cartera. Para ello, haz clic en el botón "*Verificar en el dispositivo*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Compruebe en el Jade que la dirección es la misma que en Verde y pulse el botón para confirmar.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Ahora puedes compartir la dirección con el pagador para recibir bitcoins en tu monedero. Cuando la transacción se difunda en la red, aparecerá en tu monedero. Espera a recibir suficientes confirmaciones para considerar la transacción definitiva.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Enviar bitcoins

Con bitcoins en tu monedero, ahora también puedes enviar bitcoins. Haz clic en "*Enviar*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

En la página siguiente, introduce la dirección del destinatario. Puedes introducirla manualmente o escanear un código QR.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Elija el importe del pago.

![JADE-PLUS-GREEN](assets/fr/41.webp)

En la parte inferior de la pantalla, puede seleccionar el tipo de comisión para esta transacción. Puede elegir entre seguir las recomendaciones de la aplicación o personalizar sus tarifas. Cuanto más alta sea la tarifa en relación con otras transacciones pendientes, más rápido se procesará su transacción. Para obtener información sobre el mercado de comisiones, visite [Mempool.space](https://mempool.space/) en la sección "*Cargos por transacción*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Pulse "*Siguiente*" para acceder a la pantalla de resumen de la transacción. Compruebe que la dirección, el importe y los cargos son correctos.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Si todo va bien, deslice el botón verde de la parte inferior de la pantalla hacia la derecha para firmar y difundir la transacción en la red Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Ahora se le pide que confirme la transacción en el Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Asegúrese de que la dirección del destinatario es correcta. Haga clic en la marca de verificación para confirmar.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Compruebe que el importe del cargo es correcto y, a continuación, valídelo.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Su transacción ha sido firmada y emitida desde Verde.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Enhorabuena, ahora ya sabes cómo configurar y utilizar el Jade Plus con la aplicación móvil Blockstream Green, mediante conexión Bluetooth. Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Gracias por compartir!

Para ir un paso más allá, te recomiendo este tutorial sobre el Jade Plus, donde lo configuramos con el software Sparrow Wallet en modo QR. También aprenderás a utilizar la configuración avanzada de tu hardware wallet:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

