---
name: Pasaporte - Fundación
description: Configuración y uso del monedero electrónico Passport en modo manual
---
![cover](assets/cover.webp)

El Passport es un monedero de hardware solo para Bitcoin, diseñado por Foundation Devices, una empresa estadounidense fundada en abril de 2020 en Boston.

El Passport "*Batch 2*" que presentamos en este tutorial es el sucesor de la edición "*Founder's Edition*". Se distingue por su diseño premium, una pantalla a color de alta definición y un teclado físico ergonómico. Funciona en modo "*Air-Gap*", lo que garantiza que las claves privadas de su monedero permanezcan completamente aisladas, con intercambios posibles a través de una tarjeta MicroSD o códigos QR. El dispositivo está equipado con una batería recargable extraíble Nokia BL-5C de 1200 mAh. Esta batería no propietaria se puede reemplazar fácilmente, ya que el modelo BL-5C es de fácil acceso en el mercado.

En cuanto a la conectividad, el Passport está equipado con un puerto MicroSD, un puerto USB-C para la carga y una cámara trasera para escanear códigos QR.

En términos de seguridad, el Passport incorpora un elemento seguro, y el código fuente del dispositivo es totalmente de código abierto. Ofrece todas las características que se esperan de un buen monedero hardware de Bitcoin. Tenga en cuenta que el Passport aún no es compatible con miniscript, pero esta característica está prevista para el segundo trimestre de 2025.

Con un precio de 199 dólares, el Passport se posiciona como un monedero hardware de gama alta, compitiendo con la Coldcard Q, Jade Plus, Tezor Safe 5 y los modelos de gama alta de Ledger.

![Image](assets/fr/01.webp)

Para gestionar tu monedero seguro en un Passport, tienes varias opciones. Este monedero hardware es compatible con la mayoría de software de gestión de monederos del mercado, incluyendo Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, entre otros. En este tutorial, aprenderemos a usarlo con Sparrow Wallet.

Si eres principiante, la opción más sencilla es utilizar tu Passport con la aplicación nativa Envoy, desarrollada por Foundation. Para saber cómo utilizar Envoy con tu Passport, consulta este otro tutorial :

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

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

En el dispositivo encontrará :


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

## Pasaporte inicial

Pulse el botón de encendido/apagado situado en el lateral del aparato para ponerlo en marcha.

![Image](assets/fr/04.webp)

Pulse el botón de confirmación para acceder al siguiente menú.

![Image](assets/fr/05.webp)

En este tutorial, utilizaremos Sparrow Wallet para gestionar el monedero protegido por pasaporte. Selecciona "*Configuración manual*".

![Image](assets/fr/06.webp)

A continuación, acepta las condiciones de uso.

![Image](assets/fr/07.webp)

El siguiente paso es comprobar su dispositivo. Esto confirma la autenticidad de su pasaporte y garantiza que no ha sido manipulado durante el transporte. Se le pedirá que escanee un código QR.

![Image](assets/fr/08.webp)

Vaya a [el sitio oficial de verificación](https://validate.foundationdevices.com/) y seleccione "*Pasaporte*".

![Image](assets/fr/09.webp)

Utilice la cámara de su pasaporte para escanear el código QR que aparece en el sitio.

![Image](assets/fr/10.webp)

Su dispositivo mostrará entonces 4 palabras.

![Image](assets/fr/11.webp)

Introduzca estas palabras en el sitio web para confirmar la autenticidad de su pasaporte y haga clic en "*Validar*".

![Image](assets/fr/12.webp)

Si aparece el mensaje "*Passed*", su monedero hardware es auténtico. Ahora puede utilizarlo para proteger un monedero Bitcoin.

![Image](assets/fr/13.webp)

Confirme el resultado de la prueba en su pasaporte.

![Image](assets/fr/14.webp)

## Configurar el código PIN

A continuación viene el paso del código PIN. El código PIN desbloquea su pasaporte. Por lo tanto, proporciona protección contra el acceso físico no autorizado. El código PIN no interviene en la derivación de las claves criptográficas de su monedero. Por tanto, incluso sin acceso al código PIN, la posesión de su frase mnemotécnica de 12 o 24 palabras le permitirá recuperar el acceso a sus bitcoins.

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

Para ello, utiliza la tarjeta MicroSD incluida en la caja de tu Passport (u otra) e insértala en tu ordenador. Descarga la última versión del firmware desde [el sitio de documentación de la Fundación](https://docs.foundation.xyz/firmware-updates/passport/) o [su repositorio de GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Antes de instalarlo en tu dispositivo, te aconsejamos encarecidamente que compruebes la autenticidad e integridad del firmware descargado. Si necesitas ayuda para ello, consulta este tutorial :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Después de comprobar el archivo `.bin`, colócalo en tu MicroSD e insértalo en el Passport. Se abrirá el explorador de archivos del Passport. Selecciona el archivo `vN.N.N-passport.bin`.

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

por supuesto, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Esta cartera de muestra sólo se utilizará en Testnet y se borrará al final del tutorial.**_

Haga una copia de seguridad física de esta frase.

![Image](assets/fr/35.webp)

Su Pasaporte se ha configurado correctamente. Haga clic en el botón de confirmación para continuar.

![Image](assets/fr/36.webp)

## Descubrir el menú

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

También puede introducir una frase de contraseña BIP39 (véase la sección siguiente) o utilizar una semilla temporal.

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

## Añadir una frase de contraseña BIP39

Antes de continuar, si lo desea, puede añadir una frase de contraseña BIP39. Una frase de contraseña BIP39 es una contraseña opcional que puedes elegir libremente, y que se añade a tu frase mnemotécnica para reforzar la seguridad del monedero. Con esta función activada, el acceso a su monedero Bitcoin requerirá tanto la frase mnemotécnica como la frase de contraseña. Sin ninguno de los dos, sería imposible recuperar el monedero.

Antes de configurar esta opción en tu Passport, te recomendamos encarecidamente que leas este artículo para comprender perfectamente el funcionamiento teórico de la frase de contraseña y evitar errores que podrían provocar la pérdida de tus bitcoins:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Para activarla, ve al menú "*Más*" y haz clic en "*Introducir frase de contraseña*".

![Image](assets/fr/50.webp)

Introduce tu frase de contraseña utilizando el teclado aA1, y asegúrate de guardarla una o más veces en un soporte físico (papel o metal). Para el ejemplo, estoy utilizando una frase de contraseña muy débil, pero deberías elegir una frase de contraseña fuerte y aleatoria, que incluya todos los tipos de caracteres y que sea suficientemente larga (como una contraseña fuerte).

![Image](assets/fr/51.webp)

Tenga en cuenta que las frases de contraseña BIP39 distinguen entre mayúsculas y minúsculas y entre errores tipográficos. Si introduce una frase de contraseña ligeramente diferente de la configurada inicialmente, Passport no informará de un error, sino que obtendrá otro conjunto de claves criptográficas que no serán las de su monedero inicial.

Por eso es importante que, al configurar, anotes en algún sitio la huella de la clave maestra que te darán en el siguiente paso. Por ejemplo, con mi frase de contraseña "Red Plan B", mi huella de clave maestra es "745D526B".

![Image](assets/fr/52.webp)

Cada vez que desbloquee su Passport, tendrá que volver a este menú para introducir su frase de contraseña y aplicarla a su monedero. Passport no guarda la frase de contraseña.

Cada vez que desbloquee, después de escribir la contraseña, compruebe en esta pantalla de confirmación que la huella dactilar es la misma que escribió durante la configuración. Si lo es, tu frase de contraseña es correcta y estás accediendo al monedero Bitcoin correcto. Si no lo es, estás en el monedero equivocado y necesitas intentarlo de nuevo, teniendo cuidado de no cometer ningún error de entrada.

Antes de recibir tus primeros bitcoins en tu monedero, **te aconsejo encarecidamente que realices una prueba de recuperación en vacío**. Tome nota de alguna información de referencia, como su xpub o la primera dirección de recepción, luego borre su monedero en el Passport mientras esté vacío (`Configuración -> Avanzado -> Borrar Passport`). A continuación, intente restaurar su monedero utilizando sus copias de seguridad en papel de la frase mnemotécnica y cualquier frase de contraseña. Comprueba que la información de la cookie generada tras la restauración coincide con la que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables. Para saber más sobre cómo realizar una recuperación de prueba, consulta este otro tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)

## Configuración del monedero en Sparrow Wallet

En este tutorial, te mostraré un uso avanzado de Passport con Sparrow Wallet. Sin embargo, esta billetera de hardware también es compatible con Envoy (la aplicación de la Fundación), Keeper, BlueWallet, Nunchuk, Specter, y muchos otros....

Empieza descargando e instalando Sparrow Wallet [desde el sitio web oficial](https://sparrowwallet.com/) en tu ordenador, si aún no lo has hecho.

![Image](assets/fr/54.webp)

Asegúrese de comprobar la autenticidad e integridad del software antes de instalarlo. Si no sabes cómo hacerlo, consulta este tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Una vez abierta la Cartera Sparrow, haz clic en la pestaña "*Archivo*" y luego en "*Nueva Cartera*".

![Image](assets/fr/55.webp)

Dale un nombre a tu monedero y haz clic en "*Crear monedero*".

![Image](assets/fr/56.webp)

Seleccione "*Airgapped Hardware Wallet*".

![Image](assets/fr/57.webp)

Haz clic en "*Escanear...*" junto a la opción "*Pasaporte*". Esto abrirá tu webcam.

![Image](assets/fr/58.webp)

En su monedero físico, vaya al menú "*Cuenta*", seleccione el submenú "*Gestionar cuenta*" y haga clic en "*Conectar monedero*".

![Image](assets/fr/59.webp)

En la lista desplegable que aparece, elija "*Sparrow*".

![Image](assets/fr/60.webp)

A continuación, seleccione "*Single-sig*" para una configuración normal, sin multisig.

![Image](assets/fr/61.webp)

Seleccione la opción "*Código QR*".

![Image](assets/fr/62.webp)

Tu Pasaporte generará entonces códigos QR dinámicos. Utiliza la cámara web de tu ordenador para escanearlos en el software Sparrow.

![Image](assets/fr/63.webp)

Ahora deberías ver tu xpub y la huella digital de tu llave maestra, que debería coincidir con la que aparece en tu Pasaporte cuando introduces tu frase de contraseña. Haz clic en el botón "*Aplicar*".

![Image](assets/fr/64.webp)

Establece una contraseña fuerte para asegurar el acceso a tu Billetera Sparrow. Esta contraseña protegerá tus claves públicas, direcciones, etiquetas e historial de transacciones de accesos no autorizados. Es una buena idea guardar esta contraseña en un gestor de contraseñas, para no olvidarla.

![Image](assets/fr/65.webp)

A continuación, su pasaporte le pedirá que escanee la primera dirección de recepción para confirmar que la importación se ha realizado correctamente.

![Image](assets/fr/66.webp)

En Sparrow, ve a la pestaña "*Recibir*" y escanea el código QR de la primera dirección.

![Image](assets/fr/67.webp)

Si la operación se realiza correctamente, su Pasaporte mostrará "*Verificado*".

![Image](assets/fr/68.webp)

Esto confirma que la importación se ha realizado correctamente.

![Image](assets/fr/69.webp)

## Recibir bitcoins

Ahora que tu Pasaporte está configurado, estás listo para recibir tus primeros sats en tu nuevo monedero Bitcoin. Para ello, en Sparrow, haz clic en el menú "*Recibir*".

![Image](assets/fr/70.webp)

Sparrow mostrará la primera dirección de recibo en blanco de su cartera. Puedes añadir una etiqueta.

![Image](assets/fr/71.webp)

Antes de usarla, comprobaremos la dirección en la pantalla de Passport para asegurarnos de que pertenece a nuestro monedero Bitcoin. En Sparrow, puedes ampliar el código QR de la dirección haciendo clic sobre él si es necesario. En el menú "*Account*" de tu Passport, selecciona "*Account Tools*".

![Image](assets/fr/72.webp)

Haga clic en "*Verificar dirección*" y, a continuación, escanee el código QR que aparece en Sparrow Wallet.

![Image](assets/fr/73.webp)

Asegúrate de que la dirección que aparece en el Pasaporte se corresponde exactamente con la que aparece en Sparrow, y de que aparece "*Verificado*".

![Image](assets/fr/74.webp)

Ahora puedes usarlo para recibir bitcoins. Cuando la transacción se emita en la red, aparecerá en Sparrow. Espera a recibir suficientes confirmaciones para considerar la transacción definitiva.

![Image](assets/fr/75.webp)

## Enviar bitcoins

Ahora que ya tienes unos cuantos sats en tu cartera, también puedes enviar algunos. Para ello, haz clic en el menú "*UTXOs*".

![Image](assets/fr/76.webp)

Seleccione los UTXO que desea utilizar como entradas para esta transacción y, a continuación, haga clic en "*Enviar seleccionados*".

![Image](assets/fr/77.webp)

Introduzca la dirección del destinatario, una etiqueta que le recuerde el objetivo de la transacción y el importe que desea enviar a esta dirección.

![Image](assets/fr/78.webp)

Ajuste la tasa de comisión en función de las condiciones actuales del mercado y, a continuación, haga clic en "*Crear transacción*".

![Image](assets/fr/79.webp)

Compruebe que todos los parámetros de la transacción son correctos y, a continuación, haga clic en "*Finalizar transacción para firmar*".

![Image](assets/fr/80.webp)

Haz clic en "*Show QR*" para mostrar la PSBT (*Partially Signed Bitcoin Transaction*). Sparrow ha construido la transacción, pero aún le faltan las firmas para desbloquear los bitcoins utilizados en la entrada. Estas firmas sólo pueden ser realizadas por el Pasaporte, que aloja su semilla dando acceso a las claves privadas necesarias para firmar la transacción.

![Image](assets/fr/81.webp)

En su Pasaporte, acceda al menú "*Cuenta*" y haga clic en "*Firmar con código QR*".

![Image](assets/fr/82.webp)

Escanee el PSBT (*Partially Signed Bitcoin Transaction*) que aparece en Sparrow Wallet.

![Image](assets/fr/83.webp)

Confirme que la dirección de recepción y el importe enviado son correctos y, a continuación, pulse el botón de confirmación.

![Image](assets/fr/84.webp)

Compruebe la dirección de intercambio. En mi ejemplo, no hay ninguna, ya que la transacción incluye una única salida.

![Image](assets/fr/85.webp)

Asegúrese de que la tarifa es la que usted ha elegido.

![Image](assets/fr/86.webp)

Si toda la información es correcta, haga clic en el botón de confirmación para firmar la transacción.

![Image](assets/fr/87.webp)

En Sparrow Wallet, haz clic en "*Escanear QR*" y escanea el código QR que aparece en tu Pasaporte.

![Image](assets/fr/88.webp)

Su transacción firmada está ahora lista para ser difundida en la red Bitcoin e incluida en un bloque por un minero. Si todo es correcto, haga clic en "*Broadcast Transaction*".

![Image](assets/fr/89.webp)

Su transacción ha sido emitida y está a la espera de confirmación.

![Image](assets/fr/90.webp)

Enhorabuena, ya sabes cómo configurar y utilizar Passport. Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Gracias por compartir!

Para más información, consulte nuestro tutorial sobre el software Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
