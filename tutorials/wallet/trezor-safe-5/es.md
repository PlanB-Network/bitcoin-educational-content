---
name: Trezor Safe 5
description: Configuración y uso de Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Crédito de la imagen: [Trezor.io](https://trezor.io/)*



La Trezor Safe 5 es una Hardware Wallet de última generación diseñada por SatoshiLabs y lanzada en 2024. Se posiciona como una versión de gama alta de la Safe 3, centrada en la ergonomía y la durabilidad. Se beneficia de los mismos avances en seguridad que su predecesora, la Safe 3, en comparación con la Model One y la Model T.



Con un precio de 169 euros, la Safe 5 se sitúa en la categoría Hardware Wallet de gama alta, compitiendo con modelos como Coldcard, Ledger Nano X y Flex, Jade Plus, Passport y Bitbox.



El Safe 5 se distingue por su pantalla táctil en color de 1,54 pulgadas, protegida por *Gorilla Glass 3*, que resiste golpes y arañazos. También está equipada con un motor háptico *Trezor Touch* que emite pequeñas vibraciones al tocarla. Al igual que el Safe 3, incorpora un Secure Element y funciona a través de una conexión USB-C, con el añadido de un puerto Micro SD.



La principal diferencia entre la Safe 3 y la Safe 5 radica en la calidad del dispositivo, aparte de los aspectos de seguridad. Mejora notablemente la experiencia del usuario, con un funcionamiento más fluido y una pantalla más cómoda. En términos de seguridad, es equivalente.



![Image](assets/fr/01.webp)



Safe 5 tiene todas las características esenciales que cabría esperar de un buen Hardware Wallet, incluida una excelente integración de passphrase BIP39. Sin embargo, aún no es compatible con Miniscript.



Este modelo está especialmente indicado para usuarios principiantes e intermedios. Por otro lado, puede que no cumpla todas las expectativas de los usuarios avanzados que buscan funciones más específicas disponibles en dispositivos como la Coldcard. No obstante, si no necesita estas opciones avanzadas, el Trezor Safe 5 puede ser una excelente elección.



## El modelo de seguridad Trezor Safe 5



Al igual que la Safe 3, la Trezor Safe 5 está equipada con un **Elemento Seguro** con certificación EAL6+, un avance significativo respecto a modelos anteriores como el Model One y el Model T. Se trata del chip OPTIGA Trust M V3, que no almacena el seed directamente, sino que actúa como componente criptográfico para asegurar el acceso al mismo. El elemento seguro conserva un secreto al que sólo se puede acceder una vez que el usuario ha introducido correctamente el PIN. Este secreto se utiliza entonces para descifrar la seed, que se almacena cifrada en la memoria principal del dispositivo.



Este sistema de seguridad híbrido ofrece una protección física mejorada, especialmente contra los ataques de extracción o los análisis invasivos, problemas a los que era propenso el Modelo Uno, sobre todo en la gestión de PIN. Estas vulnerabilidades ahora se sortean gracias al uso del Elemento Seguro. Este modelo también mantiene una arquitectura de software de código abierto: el código que gestiona la generación y el uso de las claves privadas sigue siendo totalmente accesible y verificable. El chip OPTIGA sólo gestiona el código PIN, un elemento externo a la gestión de claves Bitcoin Wallet. Se limita a liberar un secreto que puede utilizarse para descifrar la seed. Además, el chip OPTIGA Trust M V3 se beneficia de una licencia relativamente libre, que autoriza a SatoshiLabs a publicar libremente posibles vulnerabilidades (NDA-Free).



Este modelo de seguridad representa, en mi opinión, uno de los mejores compromisos disponibles actualmente en el mercado. Combina las ventajas de un elemento seguro con la gestión de software de código abierto. Antes, los usuarios tenían que elegir entre la seguridad física mejorada con un chip y la transparencia con el código abierto; con Trezor Safe, es posible beneficiarse de ambas.



En este tutorial, aprenderá a configurar y utilizar su Trezor Safe 5 de forma segura.



## Unboxing de la Trezor Safe 5



Cuando reciba su Safe 5, asegúrese de que la caja y el Seal están intactos para confirmar que el paquete no ha sido abierto. También se realizará una comprobación por software de la autenticidad e integridad del dispositivo cuando se configure posteriormente.



El contenido de la caja incluye :




- Trezor Safe 5;
- Una bolsa que contiene cartulinas para grabar su frase Mnemonic, pegatinas e instrucciones;
- Cable USB-C a USB-C.



Al abrirlo, tu Trezor Safe 5 debería estar protegido por un plástico protector y el puerto USB-C debería estar asegurado por un Seal holográfico. Asegúrate de que está ahí.



![Image](assets/fr/02.webp)



La navegación por el dispositivo es bastante intuitiva:




- Toca la mitad inferior de la pantalla para avanzar;
- Deslice hacia abajo para volver ;
- Mantenga pulsada la pantalla para confirmar una operación.



## Requisitos previos



En este tutorial voy a mostrarle cómo utilizar el Trezor Safe 5 con el [software de gestión de carteras Sparrow Wallet](https://sparrowwallet.com/download/). Si aún no ha instalado este software, hágalo ahora. Si necesita ayuda, también tenemos un tutorial detallado sobre la configuración de Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

También necesitará el software Trezor Suite para configurar el Safe 5, comprobar su autenticidad e instalar el firmware. Sólo utilizaremos este software para eso, y después sólo será necesario para las actualizaciones del firmware. Para la gestión diaria de la Wallet, utilizaremos exclusivamente Sparrow Wallet, ya que está optimizado para Bitcoin y es fácil de usar, incluso para principiantes (Sparrow sólo soporta Bitcoin, no altcoins).



[Descargar Trezor Suite desde el sitio web oficial](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Para estos dos programas, te recomiendo encarecidamente que compruebes tanto su autenticidad (con GnuPG) como su integridad (mediante Hash) antes de instalarlos en tu máquina. Si no sabes cómo hacerlo, puedes seguir este otro tutorial :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Puesta en marcha de Trezor Safe 5



Conecte su Safe 5 a su ordenador donde ya están instalados Trezor Suite y Sparrow Wallet.



![Image](assets/fr/04.webp)



Abra Trezor Suite y haga clic en "*Configurar mi Trezor*".



![Image](assets/fr/05.webp)



Seleccione "*Bitcoin-only firmware*" y, a continuación, haga clic en "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite instalará el firmware en su Safe 5. Por favor, espere durante la instalación.



![Image](assets/fr/07.webp)



Haga clic en "*Continuar*".



![Image](assets/fr/08.webp)



A continuación, proceda a la prueba de autenticidad para asegurarse de que su Hardware Wallet no es falso ni está comprometido.



![Image](assets/fr/09.webp)



En tu Safe 5, pulsa la pantalla para confirmar.



![Image](assets/fr/10.webp)



Si su Trezor es auténtico, aparecerá un mensaje de confirmación en Trezor Suite.



![Image](assets/fr/11.webp)



A continuación, puede omitir las ventanas con las instrucciones de funcionamiento básicas.



![Image](assets/fr/12.webp)



## Crear una cartera Bitcoin



En Trezor Suite, haga clic en el botón "*Crear nuevo Wallet*".



![Image](assets/fr/13.webp)



Para crear una BIP39 Wallet estándar, comience seleccionando "*Tipos de copia de seguridad de Legacy Wallet*" en el menú desplegable y, a continuación, elija entre una frase Mnemonic de 12 o 24 palabras (actualmente se recomiendan 12 palabras). Esto le permitirá crear una cartera clásica de una sola clave. Le aconsejo que opte aquí por parámetros conformes a BIP39, para facilitar la recuperación y evitar estar restringido a un entorno específico. Para finalizar, haga clic en "*Crear Wallet*".



Si desea obtener más información sobre las demás opciones de copia de seguridad disponibles en Trezor, incluida *Multi-share Backup*, le recomiendo que consulte también este tutorial :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Acepta las condiciones de uso de Hardware Wallet.



![Image](assets/fr/15.webp)



Mantenga pulsada la pantalla para crear una nueva cartera.



![Image](assets/fr/16.webp)



En Trezor Suite, haga clic en "*Continuar con la copia de seguridad*".



![Image](assets/fr/17.webp)



El software proporciona instrucciones sobre cómo gestionar su frase Mnemonic.



Este Mnemonic le da acceso completo y sin restricciones a todos sus bitcoins. Cualquier persona en posesión de esta frase puede robar sus fondos, incluso sin acceso físico a su Trezor Safe 5.



La frase de 12 palabras restablece el acceso a tus bitcoins en caso de pérdida, robo o rotura de tu Hardware Wallet. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.



Puede escribirlo en el cartón suministrado en la caja o, para mayor seguridad, le recomiendo grabarlo en una base de acero inoxidable para protegerlo de incendios, inundaciones o derrumbes.



Confirme las instrucciones y haga clic en el botón "*Crear copia de seguridad de Wallet*".



![Image](assets/fr/18.webp)



Safe 5 creará tu frase Mnemonic utilizando su generador de números aleatorios. Asegúrese de que no le están observando durante esta operación. Escriba las palabras que aparecen en la pantalla en el soporte físico de su elección. Dependiendo de su estrategia de seguridad, puede considerar hacer varias copias físicas completas de la frase (pero sobre todo, no la divida). Es importante mantener las palabras numeradas y en orden secuencial.



***Obviamente, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Este ejemplo Wallet sólo se utilizará en el Testnet y se borrará al final del tutorial



Para más información sobre la forma correcta de guardar y gestionar tu frase Mnemonic, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Para pasar a las palabras siguientes, pulsa en la parte inferior de la pantalla. Puedes retroceder deslizándote hacia abajo. Cuando hayas escrito todas las palabras, mantén el dedo en la pantalla para pasar al siguiente paso.



![Image](assets/fr/20.webp)



Selecciona las palabras de tu frase Mnemonic según su orden para confirmar que las has escrito correctamente.



![Image](assets/fr/21.webp)



Una vez completado este procedimiento de verificación, haga clic en la pantalla para continuar.



![Image](assets/fr/22.webp)



## Configurar el código PIN



A continuación viene el paso del código PIN. El código PIN desbloquea su Trezor. Por lo tanto, proporciona protección contra el acceso físico no autorizado. Este código PIN no interviene en la derivación de las claves criptográficas de su Wallet. Así que incluso sin acceso al código PIN, la posesión de su frase Mnemonic de 12 palabras le permitirá recuperar el acceso a sus bitcoins.



En Trezor Suite, haga clic en "*Continuar con PIN*" y, a continuación, en el botón "*Configurar PIN*".



![Image](assets/fr/23.webp)



Confirmar con Safe 5.



![Image](assets/fr/24.webp)



Le recomendamos que elija un código PIN lo más aleatorio posible. Asegúrese de guardar este código en un lugar distinto de donde esté almacenado su Trezor (por ejemplo, en un gestor de contraseñas). Puede definir un código PIN de entre 8 y 50 dígitos. Le recomiendo que elija un código PIN lo más largo posible para aumentar la seguridad.



Utilice el teclado táctil para introducir su PIN.



![Image](assets/fr/25.webp)



Cuando haya terminado, haga clic en la marca Green de la parte inferior derecha y confirme su PIN por segunda vez.



![Image](assets/fr/26.webp)



Su código PIN ha sido registrado.



![Image](assets/fr/27.webp)



En Trezor Suite, haga clic en el botón "*Completar configuración*".



![Image](assets/fr/28.webp)



La configuración de su Safe 5 ha finalizado. Si lo desea, puede cambiar el nombre y la página de inicio de su Hardware Wallet.



![Image](assets/fr/29.webp)



Ya no necesitaremos el software Trezor Suite, excepto para realizar actualizaciones periódicas de firmware en su Hardware Wallet, o si desea ejecutar una prueba de recuperación. Ahora vamos a utilizar Sparrow para gestionar la cartera, ya que este software se adapta perfectamente al uso exclusivo de Bitcoin.



## Configuración de la cartera en Sparrow Wallet



Empieza descargando e instalando Sparrow Wallet [desde el sitio web oficial](https://sparrowwallet.com/) en tu ordenador, si aún no lo has hecho.



Una vez que hayas abierto Sparrow Wallet, asegúrate de que el software está conectado a un nodo Bitcoin, lo que se indica con la marca en la esquina inferior derecha de Interface. Si tienes problemas para conectar Sparrow, te recomiendo que consultes el principio de este tutorial:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Haga clic en la pestaña "*Archivo*" y, a continuación, en "*Nuevo Wallet*".



![Image](assets/fr/30.webp)



Asigne un nombre a su cartera y haga clic en "*Crear Wallet*".



![Image](assets/fr/31.webp)



En el menú desplegable "*Tipo de script*", selecciona el tipo de script que se utilizará para asegurar tus bitcoins. Yo recomiendo "*Taproot*", o en su defecto, "*Native SegWit*".



![Image](assets/fr/32.webp)



Haga clic en el botón "*Hardware Wallet conectada*". Por supuesto, su Safe 5 debe estar conectada al ordenador y desbloqueada.



Cuando conecte su Safe 5 a un ordenador con Sparrow Wallet abierto, se le pedirá que introduzca un BIP39 de passphrase en la pantalla de Hardware Wallet. Esta opción avanzada será tratada en un futuro tutorial. Por ahora, puede simplemente hacer clic en la marca Green en la esquina superior derecha para confirmar que desea utilizar una passphrase vacía (es decir, sin passphrase). Para evitar que su Trezor le pida que introduzca una passphrase cada vez que se inicie, vaya a Trezor Suite, acceda a la configuración y cambie la opción en "*Dispositivo*" > "*Wallet por defecto*" a "*Estándar*" en lugar de "*passphrase*".



![Image](assets/fr/33.webp)



Haga clic en el botón "*Escanear*". Debería aparecer tu Safe 5. Haga clic en "*Importar almacén de claves*".



![Image](assets/fr/34.webp)



Ahora puede ver los detalles de su Wallet, incluida la clave pública extendida de su primera cuenta. Haz clic en el botón "*Aplicar*" para finalizar la creación de la Wallet.



![Image](assets/fr/35.webp)



Elija una contraseña fuerte para asegurar el acceso a Sparrow Wallet. Esta contraseña garantizará un acceso seguro a sus datos de Sparrow Wallet, protegiendo sus claves públicas, direcciones, etiquetas e historial de transacciones de accesos no autorizados.



Te aconsejo que guardes esta contraseña en un gestor de contraseñas para que no la olvides.



![Image](assets/fr/36.webp)



¡Y ahora su cartera ha sido importada a Sparrow Wallet!



![Image](assets/fr/37.webp)



Antes de recibir sus primeros bitcoins en su Wallet, **le aconsejo encarecidamente que realice una prueba de recuperación en vacío**. Anota alguna información de referencia, como tu xpub, luego reinicia tu Trezor Safe 5 mientras la Wallet está todavía vacía. A continuación, intente restaurar su Wallet en el Trezor utilizando sus copias de seguridad en papel. Comprueba que el xpub generado tras la restauración coincide con el que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables.



Para saber más sobre cómo realizar una prueba de recuperación, te sugiero que consultes este otro tutorial:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## ¿Cómo puedo recibir bitcoins con Trezor Safe 5?



En Sparrow, haz clic en la pestaña "*Recibir*".



![Image](assets/fr/38.webp)



Antes de utilizar el Address propuesto por Sparrow Wallet, compruébalo en la pantalla de tu Trezor. Esta práctica le permite confirmar que el Address mostrado en Sparrow no es fraudulento, y que Hardware Wallet posee efectivamente la clave privada necesaria para gastar posteriormente los bitcoins asegurados con este Address. Esto te ayuda a evitar varios tipos de ataques.



Para realizar esta comprobación, pulse el botón "*Visualizar Address*".



![Image](assets/fr/39.webp)



Comprueba que la Address que aparece en tu Trezor coincide con la de la Wallet de Sparrow. También es aconsejable realizar esta comprobación justo antes de comunicar tu Address al remitente, para estar seguro de su validez. Puedes pulsar la pantalla para confirmar.



![Image](assets/fr/40.webp)



A continuación, puedes añadir una "*Etiqueta*" para describir la fuente de bitcoins que se asegurará con este Address. Esta es una buena práctica que te permite gestionar mejor tus UTXOs.



![Image](assets/fr/41.webp)



A continuación, puedes utilizar este Address para recibir bitcoins.



![Image](assets/fr/42.webp)



## ¿Cómo envío bitcoins con Trezor Safe 5?



Ahora que has recibido tus primeros Satss en tu Safe 5-secured Wallet, ¡también puedes gastarlos! Conecta tu Trezor al ordenador, desbloquéalo con el código PIN, inicia Sparrow Wallet y ve a la pestaña "*Enviar*" para crear una nueva transacción.



![Image](assets/fr/43.webp)



Si desea *Coin Control*, es decir, elegir específicamente qué UTXOs consumir en la transacción, vaya a la pestaña "*UTXOs*". Seleccione los UTXOs que desea gastar y, a continuación, haga clic en "*Enviar seleccionados*". Será redirigido a la misma pantalla de la pestaña "*Enviar*", pero con sus UTXOs ya seleccionados para la transacción.



![Image](assets/fr/44.webp)



Introduzca la Address de destino. También puede introducir varias direcciones haciendo clic en el botón "*+ Añadir*".



![Image](assets/fr/45.webp)



Escriba una "*etiqueta*" para recordar la finalidad de este gasto.



![Image](assets/fr/46.webp)



Seleccione el importe que se enviará a esta Address.



![Image](assets/fr/47.webp)



Ajusta la tarifa de tu transacción en función del mercado actual. Por ejemplo, puede utilizar [Mempool.space](https://Mempool.space/) para elegir una tasa de comisión adecuada.



Asegúrese de que todos los parámetros de la transacción son correctos y, a continuación, haga clic en "*Crear transacción*".



![Image](assets/fr/48.webp)



Si todo está a su satisfacción, haga clic en "*Finalizar transacción para firmar*".



![Image](assets/fr/49.webp)



Haga clic en "*Firmar*".



![Image](assets/fr/50.webp)



Haga clic en "*Firmar*" junto a su Trezor Safe 5.



![Image](assets/fr/51.webp)



Compruebe los parámetros de la transacción en la pantalla de su Hardware Wallet, incluidos el Address de recepción del destinatario, el importe enviado y el cargo. Una vez verificada la transacción en el Trezor, mantenga pulsada la pantalla para firmarla.



![Image](assets/fr/52.webp)



Su transacción ya está firmada. Compruebe una última vez que todo está correcto y, a continuación, haga clic en "*Emisión de transacción*" para emitirla en la red Bitcoin.



![Image](assets/fr/53.webp)



Puedes encontrarlo en la pestaña "*Transacciones*" de Sparrow Wallet.



![Image](assets/fr/54.webp)



Enhorabuena, ya conoces el uso básico del Trezor Safe 5 con Sparrow Wallet Para ir un paso más allá, te recomiendo este completo tutorial sobre el uso de una Trezor Hardware Wallet con una passphrase BIP39 para mejorar tu seguridad:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!