---
name: Enviado
description: Configuración y uso de un pasaporte con la aplicación Envoy
---
![cover](assets/cover.webp)

Envoy es una aplicación de gestión de monederos Bitcoin desarrollada por Foundation. Está especialmente diseñada para su uso con el monedero físico Passport.

El Passport "*Lote 2*" que presentamos en este tutorial con la aplicación Envoy es el sucesor del "*Founder's Edition*". Presenta un diseño de primera calidad, pantalla en color de alta definición y teclado físico ergonómico. Funciona en modo "*Air-Gap*", lo que garantiza que las claves privadas de tu monedero permanezcan totalmente aisladas, siendo posibles los intercambios a través de una tarjeta MicroSD o códigos QR. El dispositivo incluye una batería extraíble de 1200 mAh.

En cuanto a la conectividad, el Passport está equipado con un puerto MicroSD, un puerto USB-C para la carga y una cámara trasera para escanear códigos QR.

En términos de seguridad, el Passport incorpora un elemento seguro, y el código fuente del dispositivo es totalmente de código abierto. Ofrece todas las características que se esperan de un buen monedero hardware de Bitcoin. Tenga en cuenta que el Passport aún no es compatible con miniscript, pero esta característica está prevista para el segundo trimestre de 2025.

Con un precio de 199 dólares, el Passport se posiciona como un monedero hardware de gama alta, compitiendo con la Coldcard Q, Jade Plus, Tezor Safe 5 y los modelos de gama alta de Ledger.

![Image](assets/fr/01.webp)

Para gestionar tu monedero seguro en un Passport, tienes varias opciones. Este monedero hardware es compatible con la mayoría de software de gestión de monederos del mercado, incluidos Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, entre otros.

En este tutorial, dirigido a usuarios principiantes e intermedios, vamos a descubrir cómo utilizar la aplicación Envoy con su Passport. Es la forma más sencilla de sacar el máximo partido a tu monedero físico.

Si eres un usuario avanzado y quieres explorar funciones más complejas, te recomiendo que eches un vistazo a este otro tutorial en el que configuramos Passport con Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236
## Unboxing del Passport

Cuando reciba su Passport, asegúrese de que la caja y el precinto del cartón están intactos para confirmar que el paquete no ha sido abierto. También se llevará a cabo una verificación informática de la autenticidad e integridad del dispositivo en el momento de su instalación.

![Image](assets/fr/02.webp)

El contenido de la caja incluye :


- Pasaporte;
- Un trozo de cartulina para escribir tu frase mnemotécnica;
- Un cable USB-C para cargar ;
- Tarjeta MicroSD ;
- Dos adaptadores de MicroSD a Lightning o USB-C ;
- Pegatinas.

En el dispositivo, encontrará :


- Un teclado (1) ;
- Puerto USB-C (2);
- Un botón de borrado (3);
- Un botón de retorno (4) ;
- Un botón de confirmación (5);
- Almohadilla direccional (6);
- Botón de encendido/apagado (7);
- Un indicador de estado (8);
- Puerto MicroSD (9) ;
- Un botón para cambiar de modo aA1 (10) ;
- Una cámara trasera.

![Image](assets/fr/03.webp)

## Descargar la aplicación Envoy

Vaya a su tienda de aplicaciones para descargar Envoy :


- En [Google Play Store](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- En la [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- En [F-Cold](https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

También puede descargar el archivo APK directamente [desde el repositorio GitHub de la Fundación](https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Una vez abierta la aplicación, seleccione "*Gestionar pasaporte*".

![Image](assets/fr/52.webp)

Elija si desea activar la conexión Tor para reforzar la confidencialidad y, a continuación, pulse "*Continuar*".

![Image](assets/fr/53.webp)

Elija "*Conectar un Passport existente*" si su Passport ya está configurado, o "*Configurar un nuevo Passport*" si está inicializando su monedero físico por primera vez.

![Image](assets/fr/54.webp)

Acepta las condiciones de uso.

![Image](assets/fr/55.webp)

A continuación se le pedirá que verifique la autenticidad del pasaporte. Haga clic en "*Siguiente*".

![Image](assets/fr/56.webp)

## Pasaporte inicial

Pulse el botón de encendido/apagado situado en el lateral del aparato para ponerlo en marcha.

![Image](assets/fr/04.webp)

Pulse el botón de confirmación para acceder al siguiente menú.

![Image](assets/fr/05.webp)

En este tutorial, utilizaremos Envoy para gestionar el monedero seguro Passport. Seleccione "*Envoy App*".

![Image](assets/fr/57.webp)

Haz clic en "*Continuar en Envoy*".

![Image](assets/fr/58.webp)

El siguiente paso es comprobar su dispositivo. Esto confirma la autenticidad de su pasaporte y garantiza que no ha sido manipulado durante el transporte. Se le pedirá que escanee un código QR.

![Image](assets/fr/08.webp)

Escanee con su pasaporte los códigos QR dinámicos que aparecen en la aplicación. Una vez finalizado el escaneado, haga clic en "*Siguiente*".

![Image](assets/fr/59.webp)

A continuación, utilice su teléfono para escanear el código QR que aparece en su pasaporte.

![Image](assets/fr/60.webp)

Si aparece el mensaje "*Your Passport is secure*", esto confirma que su monedero físico es auténtico. Ahora puede utilizarlo para proteger un monedero Bitcoin.

![Image](assets/fr/61.webp)

Confirme el resultado de la prueba en su pasaporte.

![Image](assets/fr/14.webp)

## Configurar el código PIN

A continuación viene el paso del código PIN. El código PIN desbloquea su pasaporte. Por lo tanto, proporciona protección contra el acceso físico no autorizado. El código PIN no interviene en la obtención de las claves criptográficas de su monedero. Por tanto, incluso sin acceso al código PIN, la posesión de su frase mnemotécnica de 12 o 24 palabras le permitirá recuperar el acceso a sus bitcoins.

![Image](assets/fr/15.webp)

Le recomendamos que elija un código PIN lo más aleatorio posible. Además, asegúrate de guardar este código en un lugar distinto de donde esté almacenado tu Pasaporte (por ejemplo, en un gestor de contraseñas).

Puedes elegir un código PIN de entre 6 y 12 dígitos. Te aconsejo que sea lo más largo posible.

Utilice el teclado para introducir sus números PIN. Cuando hayas terminado, pulsa el botón de confirmación.

![Image](assets/fr/16.webp)

Confirme su PIN por segunda vez.

![Image](assets/fr/17.webp)

Su código PIN ha sido registrado.

![Image](assets/fr/18.webp)

## Actualizar el firmware del Passport

Tu cartera de hardware te sugiere que actualices su firmware. Le recomiendo que actualice inmediatamente para beneficiarse de las mejoras y correcciones que aportan las últimas versiones. Para continuar, haz clic en el botón de confirmación de la derecha.

![Image](assets/fr/19.webp)

Tu Passport está listo para recibir el nuevo firmware a través de una tarjeta MicroSD.

![Image](assets/fr/20.webp)

### Sin aplicación Envoy

Para ello, utiliza la tarjeta MicroSD incluida en la caja de tu Passport (u otra) e insértala en tu ordenador. Descarga la última versión del firmware desde [el sitio de documentación de la Fundación](https://docs.foundation.xyz/firmware-updates/passport/) o [su repositorio de GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Antes de instalarlo en tu dispositivo, te aconsejamos encarecidamente que compruebes la autenticidad e integridad del firmware descargado. Si necesitas ayuda para ello, consulta este tutorial :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### Con la aplicación Envoy

La otra opción, más sencilla, es utilizar directamente la aplicación Envoy. Pulse en "*Descargar Firmware*".

![Image](assets/fr/62.webp)

Utiliza el adaptador suministrado con el Passport para conectar la tarjeta MicroSD al teléfono.

![Image](assets/fr/63.webp)

Selecciona la tarjeta MicroSD en tu explorador de archivos para guardar el firmware.

![Image](assets/fr/64.webp)

El firmware ya está guardado. Retira la MicroSD de tu smartphone e insértala en el Passport.

![Image](assets/fr/65.webp)

Se abrirá el explorador de archivos de Passport. Seleccione el archivo `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Haga clic en "*Seleccionar*".

![Image](assets/fr/23.webp)

A continuación, confirme la instalación del firmware.

![Image](assets/fr/24.webp)

Espere a que se complete la actualización.

![Image](assets/fr/25.webp)

Una vez finalizada la actualización, introduce tu código PIN para desbloquear el dispositivo y continuar con la configuración.

![Image](assets/fr/26.webp)

## Crear un nuevo monedero Bitcoin

Ahora es el momento de crear un nuevo monedero Bitcoin. Haga clic en el botón de confirmación.

![Image](assets/fr/27.webp)

Para crear una nueva cartera, haga clic en "*Crear nueva semilla*".

![Image](assets/fr/28.webp)

Puedes elegir entre una frase mnemotécnica de 12 o 24 palabras. La seguridad que ofrecen ambas opciones es similar, así que puedes optar por la más fácil de guardar, es decir, 12 palabras.

![Image](assets/fr/29.webp)

Haga clic en "*Continuar*".

![Image](assets/fr/30.webp)

Su Pasaporte generará ahora su "*Código de copia de seguridad*". Se trata de una serie de números que pueden utilizarse para descifrar una copia de seguridad de su monedero almacenada en una MicroSD. Este sistema de copia de seguridad, específico de los dispositivos Foundation, constituye una copia de seguridad adicional a su frase mnemotécnica, pero no es compatible con otro software Bitcoin.

Si decide utilizar este "*Código de copia de seguridad*", asegúrese de guardarlo en un lugar distinto de la MicroSD que contiene la copia de seguridad cifrada de su monedero. No obstante, puede optar por no utilizar este sistema si considera que una buena copia de seguridad de su frase mnemotécnica es suficiente.

![Image](assets/fr/31.webp)

Introduzca su "*Código de copia de seguridad*" para confirmar que lo ha guardado correctamente.

![Image](assets/fr/32.webp)

Si se ha insertado una MicroSD, la copia de seguridad encriptada de su cartera se ha guardado allí.

![Image](assets/fr/33.webp)

Tu Pasaporte mostrará tu frase mnemotécnica de 12 palabras. Esta frase mnemotécnica te da acceso total y sin restricciones a todos tus bitcoins. Cualquiera que posea esta frase puede robar tus fondos, incluso sin tener acceso físico a tu Pasaporte.

La frase de 12 palabras restablece el acceso a sus bitcoins en caso de pérdida, robo o rotura de su Pasaporte. Por lo tanto, es muy importante guardarlo con cuidado y almacenarlo en un lugar seguro.

Puede escribirlo en el cartón suministrado en la caja o, para mayor seguridad, le recomiendo grabarlo en una base de acero inoxidable para protegerlo de incendios, inundaciones o derrumbes.

Haga clic en el botón de confirmación para ver su frase mnemotécnica.

![Image](assets/fr/34.webp)

Para más información sobre la forma correcta de guardar y gestionar tu frase mnemotécnica, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
por supuesto, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Esta cartera de muestra sólo se utilizará en Testnet y se eliminará al final del tutorial.**_

Haga una copia de seguridad física de esta frase.

![Image](assets/fr/35.webp)

Su Pasaporte se ha configurado correctamente. Haga clic en el botón de confirmación para continuar.

![Image](assets/fr/36.webp)

## Configuración de la cartera en Envoy

En este tutorial, le mostraré cómo utilizar el Passport con la aplicación Envoy. Sin embargo, esta billetera de hardware también es compatible con Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter, y muchos otros....

![Image](assets/fr/66.webp)

Utilice la aplicación Envoy para escanear el código QR que aparece en su pasaporte.

![Image](assets/fr/67.webp)

Tus claves públicas ya están importadas en la aplicación. Haga clic en "*Validar dirección de recepción*".

![Image](assets/fr/68.webp)

Utilice su pasaporte para escanear la dirección que aparece en Envoy.

![Image](assets/fr/69.webp)

Su pasaporte confirmará si la cartera importada en Envoy es válida. Confírmelo en la aplicación.

![Image](assets/fr/70.webp)

Ahora puedes acceder a la información pública de tu monedero en Envoy, pero para gastar bitcoins, tendrás que utilizar tu Pasaporte.

![Image](assets/fr/71.webp)

## Descubra los menús del Pasaporte

La interfaz de tu Passport tiene tres menús principales:


- "*Cuenta*";
- "*Más*";
- "*Configuración*".

Para navegar entre estos menús, utilice las flechas izquierda y derecha del pad direccional.

### *Menú "Cuenta

En el menú "*Cuenta*" encontrarás las principales funciones de tu monedero Bitcoin. Puedes firmar una transacción a través de la cámara o del puerto MicroSD.

![Image](assets/fr/37.webp)

El submenú "*Herramientas de la cuenta*" ofrece opciones como verificar una dirección, firmar un mensaje o consultar las direcciones de su cartera.

![Image](assets/fr/38.webp)

En el submenú "*Gestionar cuenta*", puedes conectar tu monedero Bitcoin a un software de gestión de monederos (que veremos en los siguientes pasos de este tutorial), o ver y renombrar tu cuenta.

![Image](assets/fr/39.webp)

### Menú "Más

En el menú "*Más*", puede crear una nueva cuenta en su cartera, vinculada a la misma frase mnemotécnica.

![Image](assets/fr/40.webp)

También puede introducir una frase de contraseña BIP39 o utilizar una semilla temporal.

![Image](assets/fr/41.webp)

### Menú "Ajustes

En el menú "*Configuración*" encontrarás todos los ajustes de tu monedero y dispositivo.

![Image](assets/fr/42.webp)

El submenú "*Dispositivo*" te ofrece opciones para personalizar el brillo de la pantalla, establecer el retardo antes del bloqueo automático, cambiar el código PIN o renombrar el dispositivo.

![Image](assets/fr/43.webp)

El submenú "*Copia de seguridad*" le permite exportar la copia de seguridad cifrada de su cartera, comprobar la validez de una copia de seguridad existente o volver a buscar su "*Código de copia de seguridad*".

![Image](assets/fr/44.webp)

El submenú "*Firmware*" sirve para actualizar el firmware de tu Passport. Te recomendamos que realices estas actualizaciones con regularidad para beneficiarte de las últimas correcciones y funciones.

![Image](assets/fr/45.webp)

El submenú "*Bitcoin*" permite cambiar la unidad mostrada (BTC o satoshis), gestionar un posible monedero Multisig o pasar al modo "*Testnet*".

![Image](assets/fr/46.webp)

En "*Avanzado*", puede ver las palabras de su frase mnemotécnica, realizar acciones en la MicroSD insertada, restablecer la configuración de fábrica de su Passport o realizar una comprobación de autenticidad, como se hizo anteriormente.

![Image](assets/fr/47.webp)

Puede activar "*Palabras de seguridad*", una función que añade una capa de seguridad mostrando dos palabras específicas al desbloquear el dispositivo tras introducir los cuatro primeros dígitos del código PIN. Estas palabras, que se guardan durante la configuración, garantizan que el Passport no ha sido sustituido ni manipulado. En caso de discrepancia posterior, le aconsejamos que no utilice el dispositivo. Le aconsejo que active esta opción para prevenir la mayoría de los riesgos de compromiso físico del dispositivo.

![Image](assets/fr/48.webp)

Por último, el submenú "*Extensiones*" permite activar funciones específicas para determinados usos del aparato, como el protocolo coinjoin de Whirlpool.

![Image](assets/fr/49.webp)

## Recibir bitcoins

Ahora que su Pasaporte está configurado, está listo para recibir sus primeros sats en su nuevo monedero Bitcoin. Para ello, en Envoy, haga clic en su cuenta "*Primary 0*".

![Image](assets/fr/72.webp)

Haga clic en el botón "*Recibir*".

![Image](assets/fr/73.webp)

Su aplicación Envoy muestra la primera dirección en blanco disponible en su monedero. Antes de utilizarla, vamos a comprobar la dirección en la pantalla de Passport para asegurarnos de que realmente pertenece a nuestra cartera Bitcoin. En el menú "*Account*" de su Passport, seleccione "*Account Tools*".

![Image](assets/fr/74.webp)

Haga clic en "*Verificar dirección*" y, a continuación, escanee el código QR que aparece en Envoy.

![Image](assets/fr/75.webp)

Asegúrate de que la dirección que aparece en el Pasaporte se corresponde exactamente con la que aparece en Sparrow, y de que aparece "*Verificado*".

![Image](assets/fr/76.webp)

Ahora puede utilizarlo para recibir bitcoins. Cuando la transacción se difunda en la red, aparecerá en Envoy. Espere a recibir suficientes confirmaciones para considerar la transacción definitiva.

![Image](assets/fr/77.webp)

## Enviar bitcoins

Ahora que ya tienes unos cuantos sats en tu cartera, también puedes enviar algunos. Para ello, haz clic en el botón "*Enviar*".

![Image](assets/fr/78.webp)

Introduce la dirección del destinatario, pegándola directamente o escaneando el código QR con la cámara de tu smartphone.

![Image](assets/fr/79.webp)

Determine el importe que desea enviar y haga clic en "*Confirmar*".

![Image](assets/fr/80.webp)

Seleccione la tarifa de transacción de acuerdo con la situación actual del mercado y, a continuación, compruebe la información de la transacción. Si todo es correcto, haga clic en "*Firmar con pasaporte*".

![Image](assets/fr/81.webp)

Añada una etiqueta a su transacción para mantener un registro claro de su propósito.

![Image](assets/fr/82.webp)

Envoy muestra entonces una PSBT (*Transacción Bitcoin Parcialmente Firmada*). La aplicación ha creado la transacción, pero aún le faltan la(s) firma(s) para desbloquear los bitcoins utilizados en la entrada. Estas firmas sólo pueden ser realizadas por el Pasaporte, que aloja su semilla dando acceso a las claves privadas necesarias para firmar la transacción.

![Image](assets/fr/83.webp)

En su Pasaporte, acceda al menú "*Cuenta*" y haga clic en "*Firmar con código QR*".

![Image](assets/fr/84.webp)

Escanee la PSBT (*Transacción Bitcoin parcialmente firmada*) que aparece en Envoy.

![Image](assets/fr/85.webp)

Confirme que la dirección de recepción y el importe enviado son correctos y, a continuación, pulse el botón de confirmación.

![Image](assets/fr/86.webp)

Compruebe la dirección de intercambio. En mi ejemplo, no hay ninguna, ya que la transacción incluye una única salida.

![Image](assets/fr/87.webp)

Asegúrese de que la tarifa es la que usted ha elegido.

![Image](assets/fr/88.webp)

Si toda la información es correcta, haga clic en el botón de confirmación para firmar la transacción.

![Image](assets/fr/89.webp)

Su Pasaporte le muestra su transacción firmada en forma de código QR.

![Image](assets/fr/90.webp)

En la aplicación Envoy, haga clic en el icono del código QR y, a continuación, escanee el PSBT que aparece en la pantalla de su pasaporte.

![Image](assets/fr/91.webp)

Compruebe los detalles de su transacción una última vez. Si todo es correcto, pulse "*Enviar transacción*" para difundirla en la red Bitcoin.

![Image](assets/fr/92.webp)

Su transacción está pendiente de confirmación. Puede seguir su estado directamente desde su cuenta.

![Image](assets/fr/93.webp)

Enhorabuena, ahora ya sabe cómo configurar y utilizar Passport con la aplicación Envoy. Si este tutorial le ha resultado útil, le agradecería que dejara un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Gracias por compartirlo!

Para más información, consulte nuestro tutorial sobre el software Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04