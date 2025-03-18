---
name: Billetera Proton
description: Instalación y uso del monedero Proton Bitcoin
---
![cover](assets/cover.webp)

Proton es una empresa suiza especializada en privacidad digital, fundada en 2014 por científicos del CERN. Conocida por sus soluciones de código abierto, Proton ofrece un conjunto de servicios que incluyen Proton Mail, Proton VPN y Proton Drive.

Proton ha presentado recientemente Proton Wallet, un monedero Bitcoin de código abierto y autocustodia disponible como aplicación móvil o cliente web, vinculado a tu cuenta Proton. Las funcionalidades del monedero son relativamente clásicas por el momento, con las herramientas esenciales que se esperan de un buen monedero Bitcoin, como RBF (*Replace-By-Fee*), etiquetado o la posibilidad de añadir una frase de contraseña BIP39.

La característica especial de este monedero es la posibilidad de enviar bitcoins utilizando la dirección de correo electrónico del destinatario, para lo cual Proton genera automáticamente una dirección Bitcoin en blanco vinculada al monedero del usuario. Proton planea añadir nuevas funciones en el futuro, incluyendo Lightning y coinjoins (probablemente utilizando Whirlpool, como sugiere la actividad en su repositorio de GitHub).

## Crear una cuenta Proton

Para utilizar Proton Wallet, necesitas una cuenta Proton. Puedes crear una gratuitamente siguiendo los primeros pasos de este tutorial dedicado a la creación de un buzón Proton (sólo la sección "*Crear una cuenta Proton*"). Una vez configurada tu cuenta, puedes continuar con el resto de este tutorial.

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Conectarse a Proton Wallet

Vaya a [la página web de Proton Wallet](https://proton.me/wallet) y haga clic en el botón "*Obtener Proton Wallet*".

![Image](assets/fr/01.webp)

Elija la opción de suscripción "*Gratis*" y, a continuación, haga clic en "*Iniciar sesión*".

![Image](assets/fr/02.webp)

Introduzca el correo electrónico y la contraseña asociados a su cuenta Proton para iniciar sesión.

![Image](assets/fr/03.webp)

Ahora debería aparecer tu cuenta. Haga clic en "*Iniciar el uso de Proton Wallet ahora*".

![Image](assets/fr/04.webp)

## Crear un monedero Bitcoin

Seleccione la moneda fiduciaria predeterminada para su cuenta y, a continuación, haga clic en "*Crear nuevo monedero*".

![Image](assets/fr/05.webp)

Su monedero Bitcoin ha sido creado. En teoría, puede empezar a utilizarlo inmediatamente, pero es muy importante que primero guarde su mnemónico. Para ello, haz clic en "*Guarda tu monedero*" en la esquina superior derecha de la interfaz.

![Image](assets/fr/06.webp)

Si aún no lo has hecho en Proton, se te pedirá que configures una copia de seguridad de tu cuenta y que la asegures mediante un método 2FA. Estas medidas de seguridad, aunque aplicables a toda su cuenta Proton, son tanto más relevantes cuanto que su monedero Bitcoin está integrado en ella. Te recomiendo encarecidamente que las pongas en práctica.

![Image](assets/fr/07.webp)

Para guardar su frase mnemotécnica, haga clic en "*Hacer una copia de seguridad de la frase semilla de este monedero*".

![Image](assets/fr/08.webp)

Introduce tu contraseña de Proton.

![Image](assets/fr/09.webp)

A continuación, haga clic en "*Ver frase mnemotécnica del monedero*" para visualizar la frase mnemotécnica de su monedero.

![Image](assets/fr/10.webp)

Proton Wallet muestra su frase mnemotécnica de 12 palabras. **Esta frase mnemotécnica te da acceso completo y sin restricciones a todos tus bitcoins**. Cualquiera en posesión de esta frase puede robar tus fondos, incluso sin acceso a tu cuenta Proton. La frase de 12 palabras puede utilizarse para restaurar el acceso a tus bitcoins si pierdes el acceso a tu cuenta. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.

Puedes escribirlo en un papel o, para mayor seguridad, te recomiendo grabarlo en una base de acero inoxidable para protegerlo de incendios, inundaciones o derrumbes.

![Image](assets/fr/11.webp)

Para más información sobre la forma correcta de guardar y gestionar tu frase mnemotécnica, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

por supuesto, nunca se debe tomar una foto de estas palabras, a diferencia de lo que hago en este tutorial

Haz clic en el botón "*Hecho*" cuando hayas guardado tu frase.

![Image](assets/fr/12.webp)

## Descubra la interfaz

La interfaz de Proton Wallet es muy intuitiva. A la izquierda, encontrarás tus diferentes monederos y sus cuentas asociadas. La cuenta "*Primaria*" es tu cuenta principal. Por razones de confidencialidad, los bitcoins recibidos a través de la dirección de correo electrónico de Proton se colocan en una cuenta separada, llamada "*Bitcoin via Email*".

![Image](assets/fr/13.webp)

Para añadir una nueva cuenta, haga clic en "*Añadir cuenta*".

![Image](assets/fr/14.webp)

Para crear una nueva cartera, haga clic en el símbolo "*+*" situado junto a "*Carteras*".

![Image](assets/fr/15.webp)

Aquí es donde puedes añadir una frase de contraseña BIP39 a un nuevo monedero.

![Image](assets/fr/16.webp)

Para profundizar en el conocimiento de la frase de contraseña, te recomiendo este tutorial:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Recibir bitcoins

Para recibir bitcoins en su monedero, seleccione la cuenta deseada a la izquierda de la interfaz y, a continuación, haga clic en el botón "*Recibir*".

![Image](assets/fr/17.webp)

A continuación, Proton Wallet genera automáticamente una nueva dirección en blanco.

![Image](assets/fr/18.webp)

Una vez completada la transacción, la encontrará en la sección "*Transacciones*". Haz clic en "*+Añadir*" para asignar una etiqueta a la transacción.

![Image](assets/fr/19.webp)

## Enviar bitcoins

Ahora que tienes bitcoins en tu monedero, puedes enviarlos. Selecciona la cuenta que quieras en la parte izquierda de la interfaz y haz clic en "*Enviar*".

![Image](assets/fr/20.webp)

Introduzca la dirección Bitcoin del destinatario. Puede escanear un código QR haciendo clic en el pequeño logotipo. Para enviar a una dirección de correo electrónico, introdúzcala directamente en este campo. Una vez introducida la dirección Bitcoin, haga clic en la flechita y luego en "*Confirmar*".

![Image](assets/fr/21.webp)

Introduzca el importe que desea enviar, ya sea en moneda fiduciaria o en bitcoins, y haga clic en "*Revisar*".

![Image](assets/fr/22.webp)

Seleccione la tasa de transacción en función de la situación actual del mercado.

![Image](assets/fr/23.webp)

Añada una etiqueta a su transacción y vuelva a comprobar todos los detalles. Si todo es correcto, haga clic en "*Confirmar y enviar*" para firmar y enviar la transacción.

![Image](assets/fr/24.webp)

Su transacción aparecerá ahora a la espera de confirmación en la sección "*Transacciones*" de su cuenta.

![Image](assets/fr/25.webp)

## Iniciar sesión en la aplicación

Además del cliente web, Proton Wallet también es accesible a través de una aplicación móvil. Al vincular el monedero a su cuenta Proton, puede sincronizar su monedero entre el cliente web y la aplicación móvil.

Descarga Proton Wallet desde tu tienda de aplicaciones:


- [En la App Store](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [En Google Play Store](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Tras la instalación, haz clic en "*Iniciar sesión*" e introduce tu dirección de correo electrónico y la contraseña de Proton.

![Image](assets/fr/27.webp)

A continuación, tendrá acceso a su monedero Bitcoin, con las mismas funciones que en el cliente web.

![Image](assets/fr/28.webp)

Enhorabuena, ya sabes cómo configurar y utilizar Proton Wallet. Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Gracias por compartir!

Para ir más allá, recomiendo este tutorial sobre Jade Plus, el último monedero de hardware de Blockstream:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
