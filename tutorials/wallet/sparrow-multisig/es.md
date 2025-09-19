---
name: Sparrow Wallet - Multisig
description: Crear una cartera multifirma en Sparrow
---
![cover](assets/cover.webp)



Una Wallet multifirma (a menudo denominada "*Multisig*") es una estructura Bitcoin Wallet que requiere varias firmas criptográficas, de claves diferentes, para autorizar un gasto. A diferencia de una Wallet convencional ("*singlesig*"), en la que una sola clave privada basta para desbloquear una UTXO, la Multisig se basa en un modelo **m-de-n**: de las _n_ claves asociadas a la Wallet, _m_ deben imperativamente cofirmar cada transacción.



Este mecanismo permite compartir el control de una cartera entre varias entidades o dispositivos. Por ejemplo, en una configuración 2-de-3, se generan tres conjuntos independientes de claves, pero sólo se necesitan dos para liberar fondos. Esta arquitectura reduce drásticamente los riesgos asociados al compromiso o pérdida de una clave: un ladrón con acceso a una sola clave no puede vaciar la Wallet, y un usuario que pierda una puede seguir accediendo a sus fondos con las dos restantes.



![Image](assets/fr/01.webp)



Sin embargo, esta mayor seguridad conlleva una mayor complejidad. Configurar una Multisig Wallet requiere asegurar varias frases Mnemonic (una por factor de firma) y claves públicas extendidas ("*xpub*"). De hecho, si está utilizando una Multisig 2-de-3 Wallet, para recuperar la Wallet debe tener las tres frases Mnemonic, o al menos dos de las tres frases. Pero si sólo tienes dos de las tres frases, también necesitas acceder a los tres *xpubs*, sin los cuales será imposible recuperar las claves públicas necesarias para acceder a los bitcoins que protegen.



En resumen, para recuperar una cartera Multisig, debe :




- O acceda a todas las frases de Mnemonic asociadas a cada factor de firma;
- O bien tener el número mínimo de frases Mnemonic requeridas por el umbral para poder firmar, y también tener acceso a los xpubs de todos los factores para poder recuperar las claves públicas necesarias.



![Image](assets/fr/02.webp)



Esta gestión de las copias de seguridad de la cartera Multisig se ve facilitada por los *Descriptores de Scriptores de Salida*, que agrupan todos los datos públicos necesarios para acceder a los fondos. Sin embargo, esta funcionalidad aún no está implementada en todos los programas informáticos de gestión de carteras.



Multisig está especialmente indicado para bitcoiners que buscan una mayor seguridad o una gestión colectiva de fondos: empresas, asociaciones, familias o usuarios individuales que posean una cantidad significativa de bitcoins. Puede utilizarse para crear esquemas de gobierno descentralizados, por ejemplo, para distribuir la autoridad de firma entre varios gestores o miembros de un equipo.



En este tutorial, aprenderemos a crear y utilizar una Wallet multifirma clásica con **Sparrow Wallet**. Si desea crear una cartera multifirma personalizada con timelocks, le recomiendo utilizar Liana en su lugar:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Requisitos previos



Para este tutorial, voy a mostrarle cómo hacer un Multisig con [Sparrow Wallet software de gestión de cartera](https://sparrowwallet.com/download/). Si aún no ha instalado este software, por favor hágalo ahora. Si necesita ayuda, también tenemos un tutorial detallado sobre la configuración de Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Para configurar una Wallet multifirma, necesitará diferentes monederos de hardware. Para una Multisig 2-de-3, por ejemplo, podrías utilizar :




- Un Trezor Modelo Uno;
- Ledger Flex;
- Una Coldcard MK3.



![Image](assets/fr/03.webp)



Es una buena idea utilizar diferentes marcas de Hardware Wallet en la configuración de su Multisig. Esto garantiza que si un modelo específico tiene un problema grave, no afectará a la seguridad general de su Multisig. Además, le permite beneficiarse de las ventajas específicas de cada dispositivo. Además, le permite beneficiarse de las ventajas específicas de cada aparato. Por ejemplo, en mi configuración :





- El Trezor Model One es completamente de código abierto, lo que permite verificar la generación seed. Sin embargo, al no estar equipado con un elemento seguro, sigue siendo vulnerable a los ataques físicos;





- La Ledger Flex, por su parte, se beneficia de un firmware propietario no verificable, pero incorpora un Elemento Seguro que ofrece una excelente protección física;





- La Coldcard está equipada con un elemento seguro y su código se puede buscar. Es una opción interesante para nuestra configuración, ya que ofrece funciones de verificación no disponibles en otros modelos.



Antes de configurar su Multisig Wallet, asegúrese de que cada Hardware Wallet está correctamente configurada (generación y guardado de Mnemonic, definición de PIN). Para obtener instrucciones detalladas, puede consultar nuestros tutoriales para cada Hardware Wallet, por ejemplo :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Como veremos más adelante en este tutorial, también es posible integrar en la configuración de su Multisig un factor que no esté asociado a una Hardware Wallet, pero cuyas claves privadas estén almacenadas en su PC. Este método es obviamente menos seguro que el uso exclusivo de monederos hardware, pero puede ser pertinente en ciertos casos. Por ejemplo, para un Multisig 2-de-3, podría optar por dos monederos hardware y un Software Wallet.



## Crear una cartera Multisig



Abra Sparrow Wallet, haga clic en la pestaña "*Archivo*" y seleccione "*Nuevo Wallet*".



![Image](assets/fr/04.webp)



Asigne un nombre a su cartera multifirma y haga clic en "*Crear Wallet*" para confirmar.



![Image](assets/fr/05.webp)



En el menú desplegable "*Tipo de política*", seleccione la opción "*Firma múltiple*".



![Image](assets/fr/06.webp)



En la esquina superior derecha, ahora puede definir el número total de claves de su Multisig, así como el número de cofirmantes necesarios para autorizar un gasto. En mi ejemplo, se trata de un esquema 2 de 3.



![Image](assets/fr/07.webp)



En la parte inferior de la ventana, Sparrow Wallet muestra tres "*Keystore*". Cada uno representa un juego de llaves. Aquí, estoy usando tres portafolios de hardware, por lo que cada "*Keystore*" corresponde a uno de ellos. Ahora vamos a configurarlos.



Empiezo con la Coldcard. En la pestaña "*Keystore 1*", elijo la opción "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



En la Coldcard, una vez desbloqueado el dispositivo, voy al menú "*Configuración*" y luego a "*Billeteras Multisig*".



![Image](assets/fr/09.webp)



Este menú permite gestionar las carteras Multisig en las que participa el Coldcard. Quiero crear una nueva, así que selecciono "*Exportar XPUB*".



![Image](assets/fr/10.webp)



Para el campo "*Número de cuenta*", si sólo gestiona una cuenta, puede dejarlo en blanco y validar directamente pulsando el botón de confirmación.



![Image](assets/fr/11.webp)



A continuación, la Coldcard generate creará un archivo con tu xpub, guardado en la tarjeta Micro SD.



![Image](assets/fr/12.webp)



Inserte esta Micro SD en su ordenador. En Sparrow Wallet, haga clic en el botón "*Import File...*" junto a "*Coldcard Multisig*", a continuación seleccione el archivo creado por la Coldcard en la tarjeta.



![Image](assets/fr/13.webp)



Su xpub ha sido importado con éxito. Ahora vamos a repetir el procedimiento con las otras dos carteras de hardware.



![Image](assets/fr/14.webp)



Para el Ledger Flex, selecciono "*Keystore 2*", luego hago clic en "*Connected Hardware Wallet*". Asegúrese de que el Ledger está conectado al ordenador, desbloqueado, y que la aplicación Bitcoin está abierta.



![Image](assets/fr/15.webp)



A continuación, haz clic en el botón "*Escanear...*".



![Image](assets/fr/16.webp)



Junto al nombre de su cartera de hardware, haga clic en "*Importar almacén de claves*".



![Image](assets/fr/17.webp)



El segundo firmante está ahora correctamente registrado en Sparrow Wallet.



![Image](assets/fr/18.webp)



Repito exactamente el mismo procedimiento con el Trezor One para finalizar la configuración del Multisig.



![Image](assets/fr/19.webp)



En mi configuración no contemplamos este caso, pero si desea incluir una firma a través de una Software Wallet en Sparrow (Hot Wallet) dentro de su Multisig, simplemente haga clic en el botón "*Nueva o Importada Software Wallet*".



Ahora que todos sus dispositivos de firma están importados en Sparrow Wallet, puede finalizar la creación de Multisig haciendo clic en "*Aplicar*".



![Image](assets/fr/20.webp)



Elija una contraseña fuerte para asegurar el acceso a su Sparrow Wallet Wallet. Esta contraseña protege tus claves públicas, direcciones, etiquetas e historial de transacciones de accesos no autorizados.



Recuerda guardar esta contraseña en un lugar seguro, como un gestor de contraseñas, para evitar perderla.



![Image](assets/fr/21.webp)



## Copia de seguridad de una cartera Multisig



Ahora vamos a guardar nuestro *Descriptor de Script de Salida* en la Coldcard (esto sólo es aplicable a usuarios con Coldcard en su Multisig), y sobre todo, vamos a guardar una copia de seguridad del mismo en un soporte independiente.



El *Descriptor* contiene todos los xpubs de su cartera Multisig, así como las rutas de derivación utilizadas para generate las claves. Recuerde lo que vimos en la Parte 1: para restaurar una cartera Multisig, debe tener **todas** las frases Mnemonic, o sólo el número mínimo necesario para alcanzar el umbral de firma. Sin embargo, en este último caso, también es esencial tener **los xpubs** de los firmantes que faltan. El *Descriptor* contiene todos los xpubs de tu Multisig.



Si esto no está claro, recuerde lo siguiente: para recuperar una Multisig, necesita el número mínimo de frases Mnemonic por cada Hardware Wallet utilizada, dependiendo del umbral (en mi caso: 2 frases), así como el *Descriptor*.



Este *Descriptor* no contiene claves privadas, sólo públicas. Esto significa que no da acceso a los fondos. Por lo tanto, no es tan crítico como las frases Mnemonic, que dan acceso completo a tus bitcoins. El riesgo con el *Descriptor* está únicamente relacionado con la confidencialidad: en caso de compromiso, un tercero podría observar todas tus transacciones, pero no podría gastar tus fondos.



Le recomiendo encarecidamente que cree varias copias de este *Descriptor*, y las guarde con cada dispositivo de firma de su Multisig. Por ejemplo, en mi caso, imprimo el *Descriptor* en papel y guardo una copia con la Coldcard, otra con el Trezor, y otra con la Ledger. También guardo este *Descriptor* como archivo PDF en tres memorias USB, cada una de ellas con una de las carteras de hardware. De este modo, maximizo mis posibilidades de no perder nunca este *Descriptor*, y me aseguro de tener dos copias (una física y otra digital) con cada dispositivo.



Una vez creada su cartera Multisig, Sparrow le proporciona automáticamente este *Descriptor*. Haga clic en el botón "*Guardar PDF...*" para guardarlo como texto y como código QR.



![Image](assets/fr/22.webp)



A continuación, puede imprimir este PDF y copiarlo en sus memorias USB.



![Image](assets/fr/23.webp)



También registraremos este *Descriptor* en la Coldcard (si utiliza una en su configuración). Esto permitirá al Coldcard verificar que cada transacción firmada posteriormente corresponde a la Wallet original: xpubs correctos, formato Address correcto, ruta de derivación correcta... Sin este *Descriptor* importado, Coldcard no puede confirmar que las direcciones Exchange no han sido secuestradas o que la PSBT no ha sido manipulada.



Esto es lo que hace que la Coldcard sea tan interesante en una Multisig: ofrece comprobaciones adicionales contra ciertos ataques sofisticados, que otras carteras de hardware no permiten (siempre que, por supuesto, la utilices para firmar).



En Sparrow, accede al menú "*Configuración*" y haz clic en "*Exportar...*".



![Image](assets/fr/24.webp)



Junto a la opción "*Coldcard Multisig*", haz clic en "*Exportar archivo...*" y guarda el archivo de texto en la tarjeta Micro SD.



![Image](assets/fr/25.webp)



A continuación, inserta la tarjeta en la Coldcard. Ve al menú "*Configuración*", luego a "*Carteras Multisig*" y selecciona "*Importar desde SD*".



![Image](assets/fr/26.webp)



Seleccione el archivo apropiado y confirme la importación.



![Image](assets/fr/27.webp)



Haz clic en el nombre de tu Multisig recién importado.



![Image](assets/fr/28.webp)



Compruebe los parámetros de configuración de Multisig y confirme el registro.



![Image](assets/fr/29.webp)



Su Multisig está ahora correctamente guardado en su Coldcard. Si tiene varias Coldcards en el mismo Multisig, repita este procedimiento para cada una de ellas.



Además de guardar el *Descriptor*, no olvides prestar especial atención a guardar las frases Mnemonic para cada uno de tus dispositivos de firma. Si estás empezando, te recomiendo encarecidamente que consultes este otro tutorial para aprender a guardarlas y gestionarlas correctamente:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Antes de recibir sus primeros bitcoins en su Multisig, **le aconsejo encarecidamente que realice una prueba de recuperación en vacío**. Tome nota de alguna información de referencia, como la primera Address de recepción, a continuación, restablecer sus carteras de hardware, mientras que el Wallet está todavía vacío. A continuación, intente restaurar su Multisig Wallet en los monederos hardware utilizando sus copias de seguridad en papel de la frase Mnemonic, luego en Sparrow utilizando el *Descriptor*. Comprueba que la primera Address generada tras la restauración coincide con la que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables.



Para saber más sobre cómo realizar una prueba de recuperación, te sugiero que consultes este otro tutorial:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Recibe bitcoins en tu Multisig



Tu Wallet ya está lista para recibir bitcoins. En Sparrow, haz clic en la pestaña "*Recibir*".



![Image](assets/fr/30.webp)



Antes de utilizar la Address generada por Sparrow Wallet, tómate tu tiempo para comprobarlo directamente en la pantalla de tus monederos hardware. Esto asegurará que el Address no ha sido alterado, y que tus dispositivos contienen las claves privadas necesarias para gastar los fondos asociados. Esto le ayudará a protegerse contra una serie de vectores de ataque.



Para ello, haz clic en "*Visualizar Address*" para visualizar Address en tu Trezor o Ledger, cuando esté conectado por cable.



![Image](assets/fr/31.webp)



Con Coldcard, esta verificación puede llevarse a cabo sin ninguna interacción con Sparrow. Basta con abrir el menú "*Address Explorer*" y seleccionar su Multisig en la parte inferior.



![Image](assets/fr/32.webp)



A continuación, verá las direcciones de recepción generadas por la Multisig.



![Image](assets/fr/33.webp)



Compruebe que el Address que aparece en cada Hardware Wallet se corresponde exactamente con el que aparece en el Wallet de Sparrow. Es aconsejable hacerlo justo antes de compartir la Address con el pagador, para estar seguros de su integridad.



A continuación, puedes asignar una "*Etiqueta*" a este Address, para indicar el origen de los bitcoins recibidos. Esta es una buena forma de organizar la gestión de tus UTXOs.



![Image](assets/fr/34.webp)



Una vez verificado esto, puedes utilizar el Address para recibir bitcoins.



![Image](assets/fr/35.webp)



## Envía bitcoins con tu Multisig



Ahora que has recibido tus primeros Satss en tu Multisig Wallet, ¡también puedes gastarlos! En Sparrow, ve a la pestaña "*Enviar*" para crear una nueva transacción.



![Image](assets/fr/36.webp)



Si desea utilizar *Coin Control*, es decir, seleccionar manualmente los UTXOs que desea gastar, vaya a la pestaña "*UTXOs*". Elija los UTXOs que desea gastar y haga clic en "*Enviar seleccionados*". Se le redirigirá automáticamente a la pestaña "*Enviar*", con los UTXOs ya rellenados.



![Image](assets/fr/37.webp)



Introduzca el Address de destino. Se pueden añadir varias direcciones haciendo clic en "*+ Añadir*".



![Image](assets/fr/38.webp)



Añada una "*Etiqueta*" para describir el propósito de este gasto, para facilitar el seguimiento de sus transacciones.



![Image](assets/fr/39.webp)



Introduzca el importe que debe enviarse a la Address seleccionada.



![Image](assets/fr/40.webp)



Ajuste el nivel de carga en función de las condiciones actuales de la red. Por ejemplo, consulte [Mempool.space](https://Mempool.space/) para seleccionar un nivel de carga adecuado.



Después de comprobar todos los parámetros de la transacción, haga clic en "*Crear transacción*".



![Image](assets/fr/41.webp)



Si está conforme con todo, haga clic en "*Finalizar transacción para firmar*".



![Image](assets/fr/42.webp)



En la parte inferior de la pantalla, verás que Sparrow está esperando 2 firmas. Esto es normal: la Wallet utilizada aquí es una Multisig 2-de-3.



![Image](assets/fr/43.webp)



Empiezo a firmar con mi tarjeta Coldcard. Para ello, inserto una tarjeta Micro SD en el ordenador y, a continuación, hago clic en "*Guardar transacción*".



![Image](assets/fr/44.webp)



Hay 3 formas de transmitir la transacción a firmar a tu Hardware Wallet, y luego recuperarla desde Sparrow. La primera es utilizar una tarjeta Micro SD, como haremos aquí para la Coldcard. La segunda es mediante una conexión por cable, que utilizaremos para la segunda firma (Ledger y Trezor). Por último, es posible utilizar la comunicación por código QR, para los dispositivos equipados con cámara, como la Coldcard Q, la Jade Plus o la Passport V2.



Una vez guardada la PSBT (*Partially Signed Bitcoin Transaction*) en la Micro SD, la inserto en la Coldcard MK3 y selecciono el menú "*Listo para firmar*".



![Image](assets/fr/45.webp)



En la pantalla de su Hardware Wallet, compruebe cuidadosamente los parámetros de la transacción: la Address del destinatario, el importe enviado y los gastos. Una vez confirmada la transacción, valide para proceder a la firma.



![Image](assets/fr/46.webp)



A continuación, devuelve la Micro SD a tu ordenador y haz clic en "*Load Transaction*" en Sparrow. Selecciona la PSBT firmada por Coldcard de tus archivos.



![Image](assets/fr/47.webp)



Puedes ver que la firma Coldcard ha sido añadida. Ahora voy a utilizar un segundo dispositivo, en este caso el Ledger, para realizar la segunda firma requerida. Lo conecto, lo desbloqueo y pulso "*Firmar*" en Sparrow.



![Image](assets/fr/48.webp)



Haga clic en "*Firmar*" junto al nombre de su Hardware Wallet.



![Image](assets/fr/49.webp)



La primera vez que uses tu Ledger con esta Multisig, Sparrow te pedirá que verifiques las claves públicas extendidas (xpubs) de los cofirmantes. Al igual que con la Coldcard, este paso evita que firmes a ciegas más adelante. Para validar esta información, compara las xpub mostradas en la pantalla de la Ledger con las proporcionadas directamente por tus otros monederos hardware.



![Image](assets/fr/50.webp)



Compruebe el Address del beneficiario, el importe transferido y la comisión de la transacción, y firme la transacción.



![Image](assets/fr/51.webp)



Pulse la pantalla para firmar.



![Image](assets/fr/52.webp)



Sparrow tiene ahora las dos firmas necesarias para liberar los fondos de la cartera Multisig. Comprueba la transacción una última vez y, si todo va bien, haz clic en "*emitir transacción*" para emitirla por la red.



![Image](assets/fr/53.webp)



Encontrarás esta transacción en la pestaña "*Transacciones*" de Sparrow Wallet.



![Image](assets/fr/54.webp)



Enhorabuena, ya sabes cómo configurar y utilizar una Wallet multifirma en Sparrow. Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Gracias por compartir!



Para ir más allá, te recomiendo que consultes este tutorial sobre otro método para aumentar la seguridad de tu Bitcoin Wallet, el passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7