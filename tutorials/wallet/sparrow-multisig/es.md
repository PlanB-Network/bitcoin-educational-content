---
name: Sparrow Wallet - Multisig
description: Crear una billetera multifirma en Sparrow
---
![cover](assets/cover.webp)


Una billetera multifirma (a menudo llamada "*Multisig*") es una estructura de billetera Bitcoin que requiere varias firmas criptográficas, procedentes de claves diferentes, para autorizar un gasto. A diferencia de una billetera convencional ("*singlesig*"), en la que una sola clave privada basta para desbloquear un UTXO, la Multisig se basa en un modelo **m-de-n**: de las _n_ claves asociadas a la billetera, _m_ deben firmar imperativamente cada transacción.


Este mecanismo permite compartir el control de una billetera entre varias entidades o dispositivos. Por ejemplo, en una configuración 2-de-3, se generan tres conjuntos de claves independientes, pero solo se necesitan dos para liberar los fondos. Esta arquitectura reduce drásticamente los riesgos asociados al compromiso o la pérdida de una clave: un ladrón con acceso a una sola clave no puede vaciar la billetera, y un usuario que pierda una puede seguir accediendo a sus fondos con las dos restantes.


![Image](assets/fr/01.webp)


Sin embargo, esta mayor seguridad viene acompañada de una mayor complejidad. Configurar una billetera Multisig requiere guardar de forma segura varias frases mnemotécnicas (una por factor de firma) y claves públicas extendidas ("*xpub*"). En efecto, si utilizas una billetera Multisig 2-de-3, para recuperar la billetera debes tener las tres frases mnemotécnicas, o al menos dos de las tres. Pero si solo tienes dos de las tres frases, también necesitas acceso a los tres *xpubs*, sin los cuales será imposible recuperar las claves públicas necesarias para acceder a los bitcoins que protegen.


Para resumir, para recuperar una billetera Multisig, debes:


- O bien acceder a todas las frases mnemotécnicas asociadas a cada factor de firma;
- O bien disponer del número mínimo de frases mnemotécnicas exigido por el umbral para poder firmar, y también tener acceso a los xpubs de todos los factores para poder recuperar las claves públicas necesarias.


![Image](assets/fr/02.webp)


Esta gestión de las copias de seguridad de una billetera Multisig se ve facilitada por los *Descriptores de script de salida*, que agrupan todos los datos públicos necesarios para acceder a los fondos. Sin embargo, esta funcionalidad aún no está implementada en todos los programas de gestión de billeteras.


La Multisig es especialmente adecuada para los bitcoiners que buscan una seguridad reforzada o una gestión colectiva de fondos: empresas, asociaciones, familias o usuarios individuales que posean una cantidad importante de bitcoins. Puede utilizarse para crear esquemas de gobernanza descentralizada, por ejemplo, para distribuir la autoridad de firma entre varios gestores o miembros de un equipo.


En este tutorial aprenderemos a crear y usar una billetera multifirma clásica con **Sparrow Wallet**. Si deseas crear una billetera multifirma personalizada con timelocks, te recomiendo utilizar Liana en su lugar:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Requisitos previos


Para este tutorial, te voy a mostrar cómo crear una Multisig con el [software de gestión de billeteras Sparrow Wallet](https://sparrowwallet.com/download/). Si aún no has instalado este software, hazlo ahora. Si necesitas ayuda, también tenemos un tutorial detallado sobre la configuración de Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Para configurar una billetera multifirma, necesitarás varias Hardware Wallet distintas. Para una Multisig 2-de-3, por ejemplo, podrías usar:


- Una Trezor Model One;
- Ledger Flex;
- Una Passport Core.


![Image](assets/fr/03.webp)


Es buena idea usar diferentes marcas de Hardware Wallet en tu configuración Multisig. Esto garantiza que, si un modelo concreto presenta un problema grave, no afecte a la seguridad global de tu Multisig. Además, te permite beneficiarte de las ventajas específicas de cada dispositivo. Por ejemplo, en mi configuración:



- La Trezor Model One es completamente de código abierto, lo que permite verificar la generación de la semilla. Sin embargo, al no contar con un Secure Element, sigue siendo vulnerable a ataques físicos;



- La Ledger Flex, por su parte, se beneficia de un firmware propietario no verificable, pero incorpora un Secure Element que ofrece una excelente protección física;



- La Passport Core combina un firmware totalmente de código abierto, un Secure Element e intercambios air-gapped mediante código QR. Es un tercer firmante independiente capaz de verificar direcciones y firmar PSBT sin conexión de datos USB.


Antes de configurar tu billetera Multisig, asegúrate de que cada Hardware Wallet está correctamente configurada (generación y guardado de la frase mnemotécnica, definición del PIN). Para instrucciones detalladas, puedes consultar nuestros tutoriales de cada Hardware Wallet, por ejemplo:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Como veremos más adelante en este tutorial, también es posible integrar en tu configuración Multisig un factor que no esté asociado a una Hardware Wallet, sino cuyas claves privadas se guarden en tu ordenador. Este método es, evidentemente, menos seguro que el uso exclusivo de billeteras de hardware, pero puede ser pertinente en ciertos casos. Por ejemplo, para una Multisig 2-de-3, podrías optar por dos billeteras de hardware y una Software Wallet.

> ⚠️ **Aviso de seguridad para Coldcard MK3:** no crees una nueva semilla en una MK3 con un firmware anterior a la versión 4.2.0. Las semillas generadas con firmwares anteriores deben reemplazarse y los fondos deben trasladarse. Por ello, este tutorial usa Passport Core como firmante de referencia air-gapped.


## Crear una billetera Multisig


Abre Sparrow Wallet, haz clic en la pestaña "*File*" y selecciona "*New Wallet*".


![Image](assets/fr/04.webp)


Asigna un nombre a tu billetera multifirma y haz clic en "*Create Wallet*" para confirmar.


![Image](assets/fr/05.webp)


En el menú desplegable "*Policy Type*", selecciona la opción "*Multi Signature*".


![Image](assets/fr/06.webp)


En la esquina superior derecha, ahora puedes definir el número total de claves de tu Multisig, así como el número de cofirmantes necesarios para autorizar un gasto. En mi ejemplo, se trata de un esquema 2-de-3.


![Image](assets/fr/07.webp)


En la parte inferior de la ventana, Sparrow Wallet muestra tres "*Keystore*". Cada uno representa un conjunto de claves. Aquí uso tres billeteras de hardware, por lo que cada "*Keystore*" corresponde a una de ellas. Ahora las configuraremos.


Empiezo por la Passport Core. En la pestaña "*Keystore 1*", elijo la opción "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


En la Passport, abre la cuenta que quieras usar y selecciona "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". La Passport muestra un código QR animado que contiene su información de clave pública.

En Sparrow, selecciona "*Scan...*" junto a "*Passport*" y escanea ese código QR animado con la webcam de tu ordenador. Comprueba que la huella digital de la clave maestra mostrada por Sparrow coincide con la que muestra la Passport, y a continuación importa el keystore.

Tu xpub de la Passport ya se ha importado. Repite el procedimiento correspondiente para la Ledger Flex y la Trezor Model One.


Para la Ledger Flex, selecciono "*Keystore 2*" y luego hago clic en "*Connected Hardware Wallet*". Asegúrate de que la Ledger está conectada al ordenador, desbloqueada y de que la aplicación Bitcoin está abierta.


![Image](assets/fr/15.webp)


A continuación, haz clic en el botón "*Scan...*".


![Image](assets/fr/16.webp)


Junto al nombre de tu billetera de hardware, haz clic en "*Import Keystore*".


![Image](assets/fr/17.webp)


El segundo firmante ya está correctamente registrado en Sparrow Wallet.


![Image](assets/fr/18.webp)


Repito exactamente el mismo procedimiento con la Trezor One para finalizar la configuración de la Multisig.


![Image](assets/fr/19.webp)


En mi configuración no cubrimos este caso, pero si quieres incluir una firma mediante una billetera de software en Sparrow (hot wallet) dentro de tu Multisig, simplemente haz clic en el botón "*New or Imported Software Wallet*".


Ahora que todos tus dispositivos de firma están importados en Sparrow Wallet, puedes finalizar la creación de la Multisig haciendo clic en "*Apply*".


![Image](assets/fr/20.webp)


Elige una contraseña fuerte para proteger el acceso a tu billetera Sparrow Wallet. Esta contraseña protege tus claves públicas, direcciones, etiquetas e historial de transacciones frente a accesos no autorizados.


Recuerda guardar esta contraseña en un lugar seguro, como un gestor de contraseñas, para evitar perderla.


![Image](assets/fr/21.webp)


## Hacer una copia de seguridad de una billetera Multisig


Ahora vamos a guardar el *Descriptor de script de salida* en un soporte independiente y a conservar varias copias del mismo.


El *Descriptor* contiene todos los xpubs de tu billetera Multisig, así como las rutas de derivación utilizadas para generar las claves. Recuerda lo que vimos en la primera parte: para restaurar una billetera Multisig, debes tener **todas** las frases mnemotécnicas, o solo el número mínimo necesario para alcanzar el umbral de firma. Sin embargo, en este último caso, también es imprescindible disponer de **los xpubs** de los firmantes que falten. El *Descriptor* contiene todos los xpubs de tu Multisig.


Si esto no queda claro, recuerda simplemente esto: para recuperar una Multisig, necesitas el número mínimo de frases mnemotécnicas de cada billetera de hardware utilizada, según el umbral (en mi caso: 2 frases), además del *Descriptor*.


Este *Descriptor* no contiene claves privadas, solo públicas. Esto significa que no da acceso a los fondos. Por lo tanto, no es tan crítico como las frases mnemotécnicas, que dan acceso completo a tus bitcoins. El riesgo del *Descriptor* está relacionado únicamente con la confidencialidad: en caso de compromiso, un tercero podría observar todas tus transacciones, pero no podría gastar tus fondos.


Te recomiendo encarecidamente crear varias copias de este *Descriptor* y guardarlas junto a cada dispositivo de firma de tu Multisig. Por ejemplo, en mi caso, imprimo el *Descriptor* en papel y guardo una copia con la Passport, otra con la Trezor y otra con la Ledger. También guardo este *Descriptor* como archivo PDF en tres memorias USB, cada una almacenada junto a una de las billeteras de hardware. De este modo, maximizo mis posibilidades de no perder nunca este *Descriptor*, y me aseguro de tener dos copias (una física y otra digital) junto a cada dispositivo.


Una vez creada tu billetera Multisig, Sparrow te proporciona automáticamente este *Descriptor*. Haz clic en el botón "*Save PDF...*" para guardarlo tanto en texto como en código QR.


![Image](assets/fr/22.webp)


Después puedes imprimir este PDF y copiarlo en tus memorias USB.


![Image](assets/fr/23.webp)


La Passport usa la configuración multisig importada por Sparrow para mostrar y verificar la información de clave pertinente durante el proceso de emparejamiento y firma por QR. Guarda el *Descriptor* de forma independiente: sigue siendo esencial para recuperar la billetera si uno de los firmantes no está disponible.


Además de guardar el *Descriptor*, no olvides prestar especial atención a guardar las frases mnemotécnicas de cada uno de tus dispositivos de firma. Si estás empezando, te recomiendo encarecidamente consultar este otro tutorial para aprender a guardarlas y gestionarlas correctamente:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Antes de recibir tus primeros bitcoins en tu Multisig, **te recomiendo encarecidamente realizar una prueba de recuperación en vacío**. Anota alguna información de referencia, como la primera dirección de recepción, y luego restablece tus billeteras de hardware mientras la billetera aún está vacía. A continuación, intenta restaurar tu billetera Multisig en las billeteras de hardware usando tus copias en papel de las frases mnemotécnicas, y luego en Sparrow usando el *Descriptor*. Comprueba que la primera dirección generada tras la restauración coincide con la que anotaste originalmente. Si es así, puedes estar tranquilo de que tus copias en papel son fiables.


Para saber más sobre cómo realizar una prueba de recuperación, te sugiero consultar este otro tutorial:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Recibir bitcoins en tu Multisig


Tu billetera ya está lista para recibir bitcoins. En Sparrow, haz clic en la pestaña "*Receive*".


![Image](assets/fr/30.webp)


Antes de usar la dirección generada por Sparrow Wallet, tómate el tiempo de comprobarla directamente en la pantalla de tus billeteras de hardware. Esto garantizará que la dirección no ha sido alterada y que tus dispositivos poseen las claves privadas necesarias para gastar los fondos asociados. Esto te ayuda a protegerte frente a varios vectores de ataque.


Para ello, haz clic en "*Display Address*" para mostrar la dirección en tu Trezor o Ledger, cuando estén conectados por cable.


![Image](assets/fr/31.webp)


Con la Passport, selecciona la cuenta multisig y elige "*Verify Address*". Escanea el código QR de la dirección de recepción mostrada por Sparrow. La Passport confirma en su pantalla si la dirección pertenece a la billetera multisig.


Comprueba que la dirección mostrada en cada billetera de hardware coincide exactamente con la de Sparrow Wallet. Es recomendable hacer esto justo antes de compartir la dirección con quien vaya a pagar, para asegurarte de su integridad.


A continuación puedes asignar una "*Label*" a esta dirección, para indicar el origen de los bitcoins recibidos. Es una buena forma de organizar la gestión de tus UTXO.


![Image](assets/fr/34.webp)


Una vez verificado esto, puedes usar la dirección para recibir bitcoins.


![Image](assets/fr/35.webp)


## Enviar bitcoins con tu Multisig


Ahora que has recibido tus primeros satoshis en tu billetera Multisig, ¡también puedes gastarlos! En Sparrow, ve a la pestaña "*Send*" para crear una nueva transacción.


![Image](assets/fr/36.webp)


Si deseas usar *Coin Control*, es decir, seleccionar manualmente los UTXO que quieres gastar, ve a la pestaña "*UTXOs*". Elige los UTXO que quieras gastar y haz clic en "*Send Selected*". Se te redirigirá automáticamente a la pestaña "*Send*", con los UTXO ya rellenados.


![Image](assets/fr/37.webp)


Introduce la dirección de destino. Se pueden añadir varias direcciones haciendo clic en "*+ Add*".


![Image](assets/fr/38.webp)


Añade una "*Label*" para describir el propósito de este gasto, para facilitar el seguimiento de tus transacciones.


![Image](assets/fr/39.webp)


Introduce la cantidad que se enviará a la dirección seleccionada.


![Image](assets/fr/40.webp)


Ajusta la tarifa según las condiciones actuales de la red. Por ejemplo, consulta [Mempool.space](https://Mempool.space/) para elegir un nivel de tarifa adecuado.


Después de comprobar todos los parámetros de la transacción, haz clic en "*Create Transaction*".


![Image](assets/fr/41.webp)


Si todo te parece correcto, haz clic en "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


En la parte inferior de la pantalla verás que Sparrow está esperando 2 firmas. Esto es normal: la billetera usada aquí es una Multisig 2-de-3.


![Image](assets/fr/43.webp)


Empiezo firmando con mi Passport. En Sparrow, haz clic en "*Show QR*" para mostrar la PSBT (*Partially Signed Bitcoin Transaction*) como códigos QR animados. En la Passport, selecciona la cuenta multisig y elige "*Sign with QR Code*", y luego escanea el código QR mostrado por Sparrow.


En la pantalla de tu billetera de hardware, comprueba cuidadosamente los parámetros de la transacción: la dirección del destinatario, el importe enviado y las tarifas. Una vez confirmada la transacción, valida para proceder a la firma.


Después de aprobar la transacción, la Passport muestra la PSBT firmada como códigos QR animados. En Sparrow, haz clic en "*Scan QR*" y escanea esos códigos con tu webcam. La firma de la Passport se añade entonces. Ahora uso la Ledger para la segunda firma requerida: la conecto y desbloqueo, y luego hago clic en "*Sign*" en Sparrow.


![Image](assets/fr/48.webp)


Haz clic en "*Sign*" junto al nombre de tu billetera de hardware.


![Image](assets/fr/49.webp)


La primera vez que uses tu Ledger con esta Multisig, Sparrow te pedirá que verifiques las claves públicas extendidas (xpubs) de los cofirmantes. Al igual que con la Passport, este paso evita que firmes a ciegas más adelante. Para validar esta información, compara el xpub mostrado en la pantalla de la Ledger con los proporcionados directamente por tus otras billeteras de hardware.


![Image](assets/fr/50.webp)


Comprueba la dirección del destinatario, el importe transferido y la tarifa de la transacción, y a continuación firma la transacción.


![Image](assets/fr/51.webp)


Pulsa la pantalla para firmar.


![Image](assets/fr/52.webp)


Sparrow ya tiene las dos firmas necesarias para liberar los fondos de la billetera Multisig. Comprueba la transacción una última vez y, si todo está correcto, haz clic en "*Broadcast Transaction*" para transmitirla a la red.


![Image](assets/fr/53.webp)


Encontrarás esta transacción en la pestaña "*Transactions*" de Sparrow Wallet.


![Image](assets/fr/54.webp)


Enhorabuena, ahora ya sabes cómo configurar y usar una billetera multifirma en Sparrow. Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde abajo. No dudes en compartir este artículo en tus redes sociales. ¡Gracias por compartir!


Para ir más allá, te recomiendo consultar este tutorial sobre otro método para aumentar la seguridad de tu billetera Bitcoin, la passphrase BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
