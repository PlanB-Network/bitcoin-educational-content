---
name: Jade Plus - Sparrow
description: Configuración avanzada de Jade Plus con Sparrow Wallet
---
![cover](assets/cover.webp)

Jade Plus es un monedero hardware exclusivo para Bitcoin diseñado por Blockstream. Es el sucesor del clásico Jade, con mejoras en el software, más opciones y una ergonomía rediseñada para un uso más intuitivo. Esta nueva versión cuenta con una magnífica pantalla LCD de 1,9 pulgadas, con una gama de colores más amplia que su predecesora. También se han optimizado los botones y la navegación por los menús.

La Jade Plus se puede utilizar de varias formas: mediante una conexión por cable USB-C, en modo "*Air-Gap*" con una tarjeta micro SD (requiere adaptador), por Bluetooth o incluso intercambiando códigos QR gracias a la cámara integrada. Este monedero físico funciona con pilas.

Está disponible desde 149,99 dólares en la versión básica de color negro, y el precio puede subir hasta 20 dólares en las versiones "*Genesis Grey*" o "*Lunar Silver*". La Jade Plus es, por tanto, una opción interesante, con funcionalidades avanzadas comparables a las de carteras hardware de gama alta como la Coldcard Q o la Passport V2, pero a un precio bastante bajo, cercano a los modelos de gama media.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

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

En este tutorial, estableceremos una configuración avanzada del Jade Plus con el software de escritorio Sparrow Wallet en modo de códigos QR. Esta configuración es ideal para usuarios intermedios o experimentados. Si buscas un enfoque más sencillo para principiantes, te recomiendo que eches un vistazo a este tutorial en el que utilizamos el Jade Plus con Green Wallet a través de una conexión Bluetooth:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## El modelo de seguridad Jade Plus

El Jade Plus utiliza un modelo de seguridad basado en un "elemento seguro virtual", materializado por un "oráculo ciego". En concreto, este mecanismo combina el PIN elegido por el usuario, un secreto alojado en el Jade y un secreto en poder del oráculo (un servidor mantenido por Blockstream), para crear una clave AES-256 distribuida entre dos entidades. Durante la iniciación, un intercambio ECDH asegura la comunicación con el oráculo y cifra la frase de recuperación en el monedero físico. En términos prácticos, cuando se quiere acceder a la semilla para firmar transacciones, se necesita acceso a :


- El propio dispositivo Jade Plus;
- Para PIN para desbloquear el dispositivo ;
- Y al secreto del oráculo.

La mayor ventaja de este enfoque es la ausencia de un único punto de fallo a nivel de hardware, ya que si un atacante consigue acceder a tu Jade, extraer las claves requiere comprometer simultáneamente el Jade y el oráculo. Este modelo también significa que Jade Plus es totalmente de código abierto, evitando las restricciones asociadas al uso de verdaderos elementos físicos seguros, como los utilizados en Ledger, por ejemplo.

La desventaja de este sistema es que el uso de Jade Plus depende del oráculo mantenido por Blockstream. Si este oráculo se vuelve inaccesible, ya no es posible utilizar el monedero físico directamente con el PIN. Sin embargo, esto no significa que sus bitcoins estén perdidos, ya que aún pueden recuperarse utilizando su frase de recuperación, que puede introducir en Jade Plus en modo "*sin estado*". Para evitar esta dependencia, también puedes configurar y gestionar tu propio servidor oracle.

Otra opción para gestionar sus semillas es simplemente no registrarlas en el Jade Plus. En este caso, el Jade se convierte únicamente en un dispositivo de firma. Durante la inicialización, además de guardar la frase de recuperación como palabras, también la guardará como un código QR generado a mano. De esta forma, cada vez que utilices tu monedero, podrás importar la semilla utilizando la cámara de tu Jade. Esta puede ser una opción interesante para usuarios avanzados, dependiendo de tu estrategia de seguridad, pero tienes que tener cuidado tanto de guardar tu semilla como de protegerla, porque incluso como código QR, permitiría a cualquiera robar tus fondos. Veremos esta opción en este tutorial, pero no es obligatoria.

## Unboxing del Jade Plus

Cuando recibas tu Jade Plus, comprueba que la caja y el precinto están en buen estado para asegurarte de que el paquete no ha sido abierto.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

En la caja encontrará :


- Le Jade Plus;
- Cable USB-C;
- Tarjetas para grabar su frase mnemotécnica como palabras o como "*CompactSeedQR*";
- Algunas instrucciones de uso ;
- Un cordón;
- Algunas pegatinas.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

El dispositivo tiene 4 botones de navegación:


- El botón de la parte inferior derecha enciende el Jade;
- El botón grande de la parte frontal del aparato sirve para seleccionar un elemento;
- Los dos pequeños botones de la parte superior permiten navegar a izquierda y derecha;
- También puede seleccionar un elemento pulsando simultáneamente los dos botones situados en la parte superior del dispositivo.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Crear un nuevo monedero Bitcoin

Pulsa el botón de inicio.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Haz clic en "*Configurar Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Seleccione "Configuración avanzada".

![Image](assets/fr/07.webp)

A continuación, haga clic en "*Crear un nuevo monedero*" para generar una nueva semilla. Puede elegir entre una frase mnemotécnica de 12 o 24 palabras. La seguridad de tu monedero sigue siendo equivalente con ambas opciones, por lo que puede ser más conveniente elegir la opción más sencilla de guardar, es decir, 12 palabras.

![Image](assets/fr/08.webp)

Haz clic en el botón "*Continuar*" para mostrar tu nueva frase de recuperación.

![Image](assets/fr/09.webp)

Tu Jade Plus muestra tu frase mnemotécnica de 12 palabras. **Esta frase mnemotécnica te da acceso total y sin restricciones a todos tus bitcoins. Cualquiera que posea esta frase puede robar tus fondos, incluso sin tener acceso físico a tu Jade Plus. La frase de 12 palabras restablece el acceso a tus bitcoins en caso de pérdida, robo o rotura de tu Jade. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.**

Puede escribirlo en el cartón suministrado en la caja o, para mayor seguridad, le recomiendo grabarlo en una base de acero inoxidable para protegerlo de incendios, inundaciones o derrumbes.

![Image](assets/fr/10.webp)

Para más información sobre la forma correcta de guardar y gestionar tu frase mnemotécnica, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

por supuesto, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Esta cartera de muestra sólo se utilizará en Testnet y se eliminará al final del tutorial.

Haz clic en la flecha de la derecha de la pantalla para que aparezcan las siguientes palabras.

![Image](assets/fr/11.webp)

Una vez que hayas guardado tu frase, Jade Plus te pedirá que la confirmes. Selecciona la palabra correcta según el orden utilizando los botones de la parte superior del dispositivo y pulsa el botón central para pasar a la siguiente palabra.

![Image](assets/fr/12.webp)

A continuación, tienes 2 opciones. Como se explica en la introducción, puedes elegir guardar tu semilla directamente en el dispositivo y utilizar el sistema de protección "*Elemento Virtual Seguro*" de Blockstream para acceder a tu monedero (Opción 1), o guardar tu semilla como un código QR y escanearlo cada vez que lo utilices (Opción 2).

Para la opción 1, seleccione "*No*", y para la opción 2, seleccione "*Sí*".

![Image](assets/fr/13.webp)

### Opción 1: Desbloqueo QR PIN

Si ha elegido la opción 1 (CompactSeedQR: "*No*"), pasará directamente a la selección del método de conexión. En este tutorial, queremos utilizar el dispositivo en modo Air-Gap mediante intercambios de códigos QR, así que selecciona "*QR*".

![Image](assets/fr/27.webp)

Haga clic en "*Continuar*".

![Image](assets/fr/28.webp)

El código PIN se utiliza para desbloquear su Jade y ofrece protección contra el acceso físico no autorizado. Este código PIN no interviene en la derivación de las claves criptográficas de tu monedero. Por lo tanto, incluso sin acceso a este código PIN, la posesión de su frase mnemotécnica de 12 palabras le permitirá recuperar el acceso a sus bitcoins. Te recomendamos que elijas un código PIN lo más aleatorio posible. Además, asegúrate de guardar este código en un lugar distinto de donde esté almacenado tu Jade, como por ejemplo en un gestor de contraseñas.

Elija un código PIN de 6 dígitos en su Jade, utilizando los botones izquierdo y derecho para desplazarse por los dígitos, y el botón central para confirmar cada dígito.

![Image](assets/fr/29.webp)

Confirme su PIN por segunda vez.

![Image](assets/fr/30.webp)

Como se explica en la introducción, tu semilla se almacena encriptada en el Jade Plus. Para descifrarla, debes proporcionar :


- El código PIN válido (que acabamos de configurar) ;
- El secreto del oráculo mantenido por Blockstream.

En este tutorial avanzado, utilizaremos Sparrow Wallet para gestionar nuestro monedero Bitcoin. Sin embargo, a diferencia del software Green Wallet de Blockstream, Sparrow no tiene acceso al oráculo en los servidores de Blockstream. Por lo tanto, utilizaremos el sitio web de Blockstream para recuperar el secreto del oráculo cada vez que desbloqueemos Jade Plus.

Visite https://jadefw.blockstream.com/pinqr/index.html

Haga clic en "*Iniciar desbloqueo QR*".

![Image](assets/fr/31.webp)

Haz clic en "*Hecho*", puesto que ya has elegido tu PIN en el Jade Plus.

![Image](assets/fr/32.webp)

Utiliza la cámara de tu ordenador para escanear los códigos QR que aparecen en la pantalla de tu Jade.

![Image](assets/fr/33.webp)

Confirma en tu Jade para acceder a la siguiente pantalla.

![Image](assets/fr/34.webp)

Escanea el código QR ahora visible en el sitio web para recuperar el secreto del oráculo.

![Image](assets/fr/35.webp)

Ahora que su cartera ha sido creada, puede proceder a los siguientes pasos y saltarse la subsección "*Opción 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Cada vez que arranques, haz clic en "*QR Mode*".

![Image](assets/fr/37.webp)

Seleccione "*QR PIN Unlock*".

![Image](assets/fr/38.webp)

Introduzca su código PIN.

![Image](assets/fr/39.webp)

A continuación, visita [el sitio web de Blockstream](https://jadefw.blockstream.com/pinqr/qrpin.html) para intercambiar códigos QR con el oráculo.

![Image](assets/fr/40.webp)

Tu Jade ya está desbloqueada.

![Image](assets/fr/41.webp)

### Opción 2: CompactSeedQR

Si ha elegido la opción 2 (CompactSeedQR: "*Sí*"), haga clic de nuevo en "*Sí*".

![Image](assets/fr/14.webp)

Haga clic en "*Iniciar*".

![Image](assets/fr/15.webp)

Puede utilizar la base de códigos QR suministrada en la caja Jade Plus. Selecciona la casilla adecuada en función de si has optado por una frase de 12 o 24 palabras. También puedes [imprimir la plantilla desde el sitio web de Blockstream](https://help.blockstream.com/hc/article_attachments/41928319071769).

Tu Jade Plus mostrará cada zona de tu código QR.

![Image](assets/fr/16.webp)

Utiliza un bolígrafo para colorear los cuadrados y reproduce tu semilla como un código QR. Sé preciso para asegurarte de que la cámara del Jade Plus pueda escanearlo después. Utiliza la flecha para pasar a la siguiente zona.

![Image](assets/fr/17.webp)

Cuando haya terminado, haga clic en "*Hecho*".

![Image](assets/fr/18.webp)

Escanea tu código QR hecho a mano con el Jade Plus para comprobar su validez.

![Image](assets/fr/19.webp)

Si la copia de seguridad del papel es correcta, haga clic en "*Continuar*".

![Image](assets/fr/20.webp)

En este tutorial, utilizaremos un modo de conexión basado exclusivamente en el escaneado de códigos QR, así que selecciona "*QR*".

![Image](assets/fr/21.webp)

También puede optar por añadir un PIN además de su copia de seguridad CompactSeedQR, como en la opción 1. Esto ofrece dos formas de acceder a su monedero: a través del PIN y el sistema "Virtual Secure Element" de Blockstream, o a través del CompactSeedQR.

Si opta por la opción de doble PIN, seleccione "*PIN*" y siga los mismos pasos que en la opción 1 para configurar su código PIN.

Si prefiere continuar sólo con CompactSeedQR, seleccione "*SeedQR*".

![Image](assets/fr/22.webp)

Ahora que ya ha creado su cartera, puede pasar a los siguientes pasos.

![Image](assets/fr/23.webp)

Cada vez que se inicie, haga clic en el botón "*QR Mode*" y, a continuación, en "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Utiliza la cámara del dispositivo para escanear tus semillas guardadas como un código QR.

![Image](assets/fr/25.webp)

Tu Jade ya está desbloqueada.

![Image](assets/fr/26.webp)

## Añadir una frase de contraseña BIP39

Una frase de contraseña BIP39 es una contraseña opcional que puede elegir libremente, y que se añade a su frase mnemotécnica para reforzar la seguridad del monedero. Con esta función activada, el acceso a su monedero Bitcoin requerirá tanto la frase mnemotécnica como la frase de contraseña. Sin ninguno de los dos, sería imposible recuperar el monedero.

Antes de configurar esta opción en tu Jade Plus, es muy recomendable que leas este artículo para comprender perfectamente el funcionamiento teórico de la frase de contraseña y evitar errores que podrían provocar la pérdida de tus bitcoins :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Con tu Jade aún bloqueado (la frase de contraseña sólo puede introducirse cuando el dispositivo no está desbloqueado), accede al menú "*Opciones*".

![Image](assets/fr/42.webp)

Seleccione "*BIP39 Passphrase*".

![Image](assets/fr/43.webp)

En la opción "*Frecuencia*", puedes elegir si Jade Plus te pedirá que introduzcas tu frase de contraseña cada vez que se inicie:


- "*Desactivado*" desactiva el uso de una frase de contraseña;
- "*Sólo en el próximo inicio de sesión*" le obligará a volver a este menú para activar la solicitud de su frase de contraseña en el próximo inicio de sesión. Esta opción le permite no revelar su uso;
- "*Siempre preguntar*" hace que Jade te pida sistemáticamente tu frase de contraseña cada vez que se inicia, revelando así que tu monedero está protegido por una frase de contraseña.

Elige la opción según tu estrategia de seguridad. Personalmente, selecciono "*Siempre preguntar*" para el ejemplo.

![Image](assets/fr/44.webp)

A continuación, puede elegir entre dos métodos para introducir su frase de contraseña:


- "*Manual*: Un teclado virtual le permite introducir letras (mayúsculas y minúsculas), números y símbolos, carácter por carácter. Es el método estándar de todos los monederos físicos;
- "*WordList*": Método específico diseñado por Blockstream para Jade, que acelera la introducción de la frase de contraseña y aumenta su entropía. Durante la introducción, el sistema sugiere palabras de la lista BIP39, lo que facilita el desbloqueo. Este método genera automáticamente una frase concatenando las palabras elegidas, separadas por espacios (ejemplo: `abandon ability able`).

Personalmente, le aconsejo que utilice el primer método, ya que es el estándar que encontrará en todos los demás soportes de cartera.

![Image](assets/fr/45.webp)

A continuación, puede volver a la pantalla de inicio y desbloquear su monedero con normalidad, ya sea utilizando su código PIN o su CompactSeedQR (como se ve arriba). A continuación, se le pedirá que introduzca su frase de contraseña.

![Image](assets/fr/46.webp)

Introdúcela en el teclado de Jade, y asegúrate de hacer una o más copias de seguridad en soporte físico (papel o metal). Para el ejemplo, estoy usando una frase de contraseña muy débil, pero necesitas elegir una frase de contraseña fuerte y aleatoria que incluya todo tipo de caracteres y sea lo suficientemente larga (como una contraseña fuerte).

![Image](assets/fr/47.webp)

Si tu contraseña es válida, confírmala.

![Image](assets/fr/48.webp)

Tenga en cuenta que las frases de contraseña BIP39 distinguen entre mayúsculas y minúsculas y errores tipográficos. Si introduce una frase de contraseña ligeramente diferente de la configurada inicialmente, Jade no informará de un error, sino que derivará otro conjunto de claves criptográficas que no serán las de su cartera inicial.

Por eso es importante que, al configurarlo, anotes la huella de tu clave maestra, que se encuentra en la esquina inferior derecha de la pantalla. Por ejemplo, con mi frase de contraseña "PBN", mi clave maestra es "3AD1AE65".

![Image](assets/fr/49.webp)

Cada vez que desbloquees tu Jade con tu frase de contraseña, comprueba que la huella digital es la misma que la que introdujiste durante la configuración. Si lo es, tu frase de contraseña es correcta y estás accediendo al monedero Bitcoin correcto. Si no lo es, estás en el monedero equivocado y necesitas intentarlo de nuevo, teniendo cuidado de no cometer ningún error de entrada.

Antes de recibir tus primeros bitcoins en tu monedero, **te aconsejo encarecidamente que realices una prueba de recuperación en vacío**. Tome nota de alguna información de referencia, como su xpub o primera dirección de recepción, a continuación, elimine su cartera en el Jade Plus, mientras que todavía está vacío (`Opciones -> Dispositivo -> Factory Reset`). A continuación, intente restaurar su monedero utilizando sus copias de seguridad en papel de la frase mnemotécnica y cualquier frase de contraseña. Comprueba que la información de la cookie generada tras la restauración coincide con la que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables. Para saber más sobre cómo realizar una recuperación de prueba, echa un vistazo a este otro tutorial:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Configuración del monedero en Sparrow Wallet

En este tutorial, presento un uso avanzado de Jade Plus utilizando Sparrow Wallet. Sin embargo, esta billetera de hardware es compatible con muchos otros programas, como Liana, Nunchuk, Specter, Green y Keeper. Estas compatibilidades varían en términos de conexiones: USB, Bluetooth o código QR (ver tabla en la introducción para más detalles).

Empieza descargando e instalando Sparrow Wallet [desde el sitio web oficial](https://sparrowwallet.com/) en tu ordenador, si aún no lo has hecho.

![Image](assets/fr/50.webp)

Asegúrese de comprobar la autenticidad e integridad del software antes de instalarlo. Si no sabes cómo hacerlo, consulta este tutorial:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Una vez abierta la Cartera Sparrow, haz clic en la pestaña "*Archivo*" y luego en "*Nueva Cartera*".

![Image](assets/fr/51.webp)

Dale un nombre a tu monedero y haz clic en "*Crear monedero*".

![Image](assets/fr/52.webp)

Seleccione "*Airgapped Hardware Wallet*".

![Image](assets/fr/53.webp)

Haz clic en "*Escanear...*" junto a la opción "*Jade*".

![Image](assets/fr/54.webp)

Desbloquea tu Jade Plus y, si utilizas uno, introduce tu frase de contraseña. A continuación, ve al menú "*Opciones*", selecciona "*Billetera*" y haz clic en "*Exportar Xpub*".

![Image](assets/fr/55.webp)

Tu Jade mostrará tu Keystore a través de varios códigos QR. Escanéalos en tu máquina utilizando Sparrow.

![Image](assets/fr/56.webp)

Ahora deberías ver tu xpub y la huella de tu llave maestra, que debería coincidir con la de tu Jade Plus. Haz clic en "*Aplicar*".

![Image](assets/fr/57.webp)

Establece una contraseña fuerte para asegurar el acceso a tu Billetera Sparrow. Esta contraseña protegerá tus claves públicas, direcciones, etiquetas e historial de transacciones de accesos no autorizados. Es una buena idea guardar esta contraseña en un gestor de contraseñas, para no olvidarla.

![Image](assets/fr/58.webp)

Su cartera está ahora correctamente configurada en Sparrow.

![Image](assets/fr/59.webp)

## Recibir bitcoins

Ahora que tu Jade Plus está configurado, estás listo para recibir tus primeros sats en tu nuevo monedero Bitcoin. Para ello, en Sparrow, haz clic en el menú "*Recibir*".

![Image](assets/fr/60.webp)

Sparrow mostrará la primera dirección de recepción en blanco de su cartera.

![Image](assets/fr/61.webp)

Antes de usarla, vamos a comprobarla en la pantalla del Jade Plus para asegurarnos de que pertenece a nuestro monedero Bitcoin. En el Jade, haz clic en "*Escanear QR*" y, a continuación, escanea el código QR de la dirección que aparece en Sparrow.

![Image](assets/fr/62.webp)

Comprueba que la dirección que aparece en la pantalla de tu Jade se corresponde con la que aparece en Sparrow Wallet. Si es así, haz clic en la marca de verificación para continuar.

![Image](assets/fr/63.webp)

Su monedero físico confirmará entonces que esta dirección forma parte de su monedero y que posee la clave privada asociada.

![Image](assets/fr/64.webp)

Si la dirección es validada por tu Jade, ya puedes utilizarla para recibir bitcoins. Cuando la transacción se difunda en la red, aparecerá en Sparrow. Espera a recibir suficientes confirmaciones para considerar la transacción como definitiva.

![Image](assets/fr/65.webp)

## Enviar bitcoins

Ahora que ya tienes unos cuantos sats en tu cartera, también puedes enviar algunos. Para ello, haz clic en el menú "*UTXOs*".

![Image](assets/fr/66.webp)

Seleccione los UTXO que desea utilizar como entradas para esta transacción y, a continuación, haga clic en "*Enviar seleccionados*".

![Image](assets/fr/67.webp)

Introduzca la dirección del destinatario, una etiqueta que le recuerde el objetivo de la transacción y el importe que desea enviar a esta dirección.

![Image](assets/fr/68.webp)

Ajuste el tipo de comisión en función de las condiciones actuales del mercado y, a continuación, haga clic en "*Crear transacción*".

![Image](assets/fr/69.webp)

Compruebe que todos los parámetros de la transacción son correctos y, a continuación, haga clic en "*Finalizar transacción para firmar*".

![Image](assets/fr/70.webp)

Haz clic en "*Show QR*" para mostrar la PSBT (*Partially Signed Bitcoin Transaction*). Sparrow ha construido la transacción, pero aún le faltan las firmas para desbloquear los bitcoins utilizados en la entrada. Estas firmas sólo pueden ser realizadas por Jade Plus, que aloja su semilla dando acceso a las claves privadas necesarias para firmar la transacción.

![Image](assets/fr/71.webp)

En tu Jade Plus, haz clic en "*Escanear QR*" para escanear el PSBT que aparece en Sparrow.

![Image](assets/fr/72.webp)

Confirme que la dirección de entrega y el importe enviado son correctos y, a continuación, haga clic en la flecha para validar.

![Image](assets/fr/73.webp)

Asegúrese de que el importe de la tasa es el que ha elegido y, a continuación, haga clic en el icono de la marca de verificación situado en la esquina superior izquierda de la interfaz para firmar la transacción.

![Image](assets/fr/74.webp)

En Sparrow Wallet, haz clic en "*Escanear QR*" y escanea el código QR que aparece en tu Jade.

![Image](assets/fr/75.webp)

Su transacción firmada está ahora lista para ser difundida en la red Bitcoin e incluida en un bloque por un minero. Si todo es correcto, haga clic en "*Broadcast Transaction*".

![Image](assets/fr/76.webp)

Su transacción ha sido emitida y está a la espera de confirmación.

![Image](assets/fr/77.webp)

Enhorabuena, ya sabes cómo configurar y utilizar el Jade Plus en modo QR. Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Gracias por compartir!

Para ir más allá, te recomiendo este otro tutorial sobre el Jade Plus, donde lo configuramos vía Bluetooth con la app móvil Green:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0