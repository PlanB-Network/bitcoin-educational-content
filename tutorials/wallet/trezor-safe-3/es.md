---
name: Trezor Safe 3
description: Configuración y uso de Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Crédito de la imagen: [Trezor.io](https://trezor.io/)*



El Trezor Safe 3 es un Hardware Wallet diseñado por SatoshiLabs y creado en 2023. Es un modelo muy compacto y ligero (14 gramos) diseñado tanto para principiantes como para usuarios intermedios. Es el sucesor del famoso Model One, con importantes añadidos, pero conservando el enfoque de código abierto de la marca que lo diferencia de su principal competidor, el Ledger. La Safe 3 tiene un precio de 79 euros. Se sitúa así en el segmento medio de Hardware Wallet, en competencia directa con la Ledger Nano S Plus.



La Safe 3 no tiene batería y funciona exclusivamente a través de una conexión USB-C, utilizada tanto para la alimentación como para la comunicación. Cuenta con una pequeña pantalla OLED monocroma de 0,96 pulgadas y dos botones físicos.



![Image](assets/fr/01.webp)



La Safe 3 ofrece todas las características esenciales que se esperan de una buena Hardware Wallet, incluida una excelente integración de la passphrase BIP39. Sin embargo, aún no es compatible con Miniscript.



Este modelo es especialmente adecuado para principiantes, e incluso podría ser la Hardware Wallet que recomendaría a un nuevo usuario. También es adecuado para usuarios intermedios. Por otro lado, puede que no cumpla todas las expectativas de los usuarios avanzados que buscan funciones más específicas, disponibles en dispositivos como la Coldcard. No obstante, si no necesita estas opciones avanzadas, el Trezor Safe 3 puede ser una excelente elección.



## El modelo de seguridad Trezor Safe 3



La Trezor Safe 3 está ahora equipada con un **Elemento Seguro** con certificación EAL6+, un avance significativo respecto a modelos anteriores como el Model One y el Model T. Se trata del chip OPTIGA Trust M V3, que no almacena directamente el seed, sino que actúa como componente criptográfico para asegurar el acceso al mismo. El elemento seguro conserva un secreto al que sólo se puede acceder una vez que el usuario ha introducido correctamente el PIN. Este secreto se utiliza entonces para descifrar la seed, que se almacena cifrada en la memoria principal del dispositivo.



Este sistema de seguridad híbrido ofrece una protección física mejorada, especialmente contra los ataques de extracción o los análisis invasivos, problemas a los que era propenso el Modelo Uno, sobre todo en la gestión de PIN. Estas vulnerabilidades ahora se sortean gracias al uso del Elemento Seguro. Este modelo también mantiene una arquitectura de software de código abierto: el código que gestiona la generación y el uso de las claves privadas sigue siendo totalmente accesible y verificable. El chip OPTIGA sólo gestiona el código PIN, un elemento externo a la gestión de claves Bitcoin Wallet. Sólo libera un secreto que puede utilizarse para descifrar la seed. Además, el chip OPTIGA Trust M V3 se beneficia de una licencia relativamente libre, que autoriza a SatoshiLabs a publicar libremente las posibles vulnerabilidades.



Este modelo de seguridad representa, en mi opinión, uno de los mejores compromisos disponibles actualmente en el mercado. Combina las ventajas de un elemento seguro con la gestión de software de código abierto. Antes, los usuarios tenían que elegir entre la seguridad física mejorada con un chip y la transparencia con el código abierto; con Trezor Safe 3, es posible beneficiarse de ambas.



En este tutorial, le mostraremos cómo configurar y utilizar su Trezor Safe 3 de forma segura.



## Unboxing de la Trezor Safe 3



Cuando reciba su Safe 3, asegúrese de que la caja y el Seal están intactos para confirmar que el paquete no ha sido abierto. También se llevará a cabo una verificación por software de la autenticidad e integridad del dispositivo cuando se configure posteriormente.



El contenido de la caja incluye :




- Trezor Safe 3;
- Una bolsa que contiene cartulinas para grabar su frase Mnemonic, pegatinas e instrucciones;
- Cable USB-C a USB-C.



![Image](assets/fr/02.webp)



Al abrirlo, tu Trezor Safe 3 debería estar protegido por un plástico protector y el puerto USB-C debería estar asegurado por un Seal holográfico. Asegúrate de que está ahí.



![Image](assets/fr/03.webp)



La navegación por el dispositivo es sencilla: utilice el botón derecho para desplazarse hacia la derecha y el botón izquierdo para desplazarse hacia la izquierda. Pulsa ambos botones simultáneamente para confirmar una acción.



![Image](assets/fr/04.webp)



## Requisitos previos



En este tutorial, voy a mostrarle cómo utilizar el Trezor Safe 3 con el [software de gestión de carteras Sparrow Wallet](https://sparrowwallet.com/download/). Si aún no ha instalado este software, hágalo ahora. Si necesita ayuda, también tenemos un tutorial detallado sobre la configuración de Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

También necesitará el software Trezor Suite para configurar la Safe 3, comprobar su autenticidad e instalar el firmware. Sólo utilizaremos este software para eso, y después sólo será necesario para las actualizaciones del firmware. Para la gestión diaria de la Wallet, utilizaremos exclusivamente Sparrow Wallet, ya que está optimizado para Bitcoin y es fácil de usar, incluso para principiantes (Sparrow sólo soporta Bitcoin, no altcoins).



[Descargar Trezor Suite desde el sitio web oficial](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Para estos dos programas, te recomiendo encarecidamente que compruebes tanto su autenticidad (con GnuPG) como su integridad (mediante Hash) antes de instalarlos en tu máquina. Si no sabes cómo hacerlo, puedes seguir este otro tutorial :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Inicio de Trezor Safe 3



Conecte su Safe 3 a su ordenador donde ya están instalados Trezor Suite y Sparrow Wallet.



![Image](assets/fr/06.webp)



Abra Trezor Suite y haga clic en "*Configurar mi Trezor*".



![Image](assets/fr/07.webp)



Seleccione "*Bitcoin-only firmware*" y, a continuación, haga clic en "*Install Bitcoin-only*".



![Image](assets/fr/08.webp)



A continuación, Trezor Suite instalará el firmware en su Safe 3. Espere durante la instalación.



![Image](assets/fr/09.webp)



Haga clic en "*Continuar*".



![Image](assets/fr/10.webp)



A continuación, proceda a la prueba de autenticidad para asegurarse de que su Hardware Wallet no es falso ni está comprometido.



![Image](assets/fr/11.webp)



En tu Safe 3, pulsa el botón derecho para confirmar.



![Image](assets/fr/12.webp)



Si su Trezor es auténtico, aparecerá un mensaje de confirmación en Trezor Suite.



![Image](assets/fr/13.webp)



A continuación, puede omitir las ventanas con las instrucciones de funcionamiento básicas.



![Image](assets/fr/14.webp)



## Crear una cartera Bitcoin



En Trezor Suite, haga clic en el botón "*Crear nuevo Wallet*".



![Image](assets/fr/15.webp)



Para una cartera estándar, puede optar por el tipo de copia de seguridad por defecto. Esto crea una cartera clásica de una sola firma con una frase Mnemonic de 12 palabras. Haga clic en "*Crear Wallet*".



Si desea obtener más información sobre las demás opciones de copia de seguridad disponibles en Trezor, incluida *Multi-share Backup*, le recomiendo que consulte también este tutorial :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Acepta las condiciones de uso de Hardware Wallet.



![Image](assets/fr/17.webp)



Pulse de nuevo el botón derecho para crear una nueva cartera.



![Image](assets/fr/18.webp)



En Trezor Suite, haga clic en "*Continuar con la copia de seguridad*".



![Image](assets/fr/19.webp)



El software proporciona instrucciones sobre cómo gestionar su frase Mnemonic.



Este Mnemonic le da acceso completo y sin restricciones a todos sus bitcoins. Cualquier persona en posesión de esta frase puede robar sus fondos, incluso sin acceso físico a su Trezor Safe 3.



La frase de 12 palabras restablece el acceso a tus bitcoins en caso de pérdida, robo o rotura de tu Hardware Wallet. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.



Puede escribirlo en el cartón suministrado en la caja o, para mayor seguridad, le recomiendo grabarlo en una base de acero inoxidable para protegerlo de incendios, inundaciones o derrumbes.



Confirme las instrucciones y haga clic en el botón "*Crear copia de seguridad de Wallet*".



![Image](assets/fr/20.webp)



Safe 3 creará tu frase Mnemonic utilizando su generador de números aleatorios. Asegúrese de que no le están observando durante esta operación. Escriba las palabras que aparecen en la pantalla en el soporte físico de su elección. Dependiendo de su estrategia de seguridad, puede considerar hacer varias copias físicas completas de la frase (pero sobre todo, no la divida). Es importante mantener las palabras numeradas y en orden secuencial.



***Obviamente, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Este ejemplo Wallet sólo se utilizará en el Testnet y se borrará al final del tutorial



Para más información sobre la forma correcta de guardar y gestionar tu frase Mnemonic, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Para pasar a las palabras siguientes, haz clic con el botón derecho. Puedes retroceder pulsando el botón izquierdo. Cuando hayas escrito todas las palabras, mantén pulsado el botón derecho para pasar al siguiente paso.



![Image](assets/fr/22.webp)



Seleccione las palabras de su frase Mnemonic según su orden para confirmar que las ha escrito correctamente. Utilice los botones izquierdo y derecho para navegar entre las propuestas y, a continuación, seleccione la palabra correcta pulsando simultáneamente los 2 botones.



![Image](assets/fr/23.webp)



Una vez finalizado este procedimiento de verificación, haga clic en el botón de la derecha.



![Image](assets/fr/24.webp)



## Configurar el código PIN



A continuación viene el paso del código PIN. El código PIN desbloquea su Trezor. Por lo tanto, proporciona protección contra el acceso físico no autorizado. Este código PIN no interviene en la derivación de las claves criptográficas de su Wallet. Así que incluso sin acceso al código PIN, la posesión de su frase Mnemonic de 12 palabras le permitirá recuperar el acceso a sus bitcoins.



En Trezor Suite, haga clic en "*Continuar con PIN*" y, a continuación, en el botón "*Configurar PIN*".



![Image](assets/fr/25.webp)



Confirmar con Safe 3.



![Image](assets/fr/26.webp)



Le recomendamos que elija un código PIN lo más aleatorio posible. Asegúrese de guardar este código en un lugar distinto de donde esté almacenado su Trezor (por ejemplo, en un gestor de contraseñas). Puede definir un código PIN de entre 8 y 50 dígitos. Le recomiendo que elija un código PIN lo más largo posible para aumentar la seguridad.



Utilice los botones izquierdo y derecho para seleccionar cada dígito. Para confirmar la selección y pasar a la cifra siguiente, pulse simultáneamente los dos botones.



![Image](assets/fr/27.webp)



Cuando haya terminado, haga clic en la marca de verificación "*ENTER*" que aparece al principio de los dígitos y, a continuación, confirme su PIN por segunda vez.



![Image](assets/fr/28.webp)



Su código PIN ha sido registrado.



![Image](assets/fr/29.webp)



En Trezor Suite, haga clic en el botón "*Completar configuración*".



![Image](assets/fr/30.webp)



La configuración de su Safe 3 ha finalizado. Si lo desea, puede cambiar el nombre y la página de inicio de su Hardware Wallet.



![Image](assets/fr/31.webp)



Ya no necesitaremos el software Trezor Suite, excepto para realizar actualizaciones periódicas de firmware en su Hardware Wallet, o si desea ejecutar una prueba de recuperación. Ahora vamos a utilizar Sparrow para gestionar la cartera, ya que este software se adapta perfectamente al uso exclusivo de Bitcoin.



## Configuración de la cartera en Sparrow Wallet



Empieza descargando e instalando Sparrow Wallet [desde el sitio web oficial](https://sparrowwallet.com/) en tu ordenador, si aún no lo has hecho.



Una vez que hayas abierto Sparrow Wallet, asegúrate de que el software está conectado a un nodo Bitcoin, lo que se indica con la marca en la esquina inferior derecha de la Interface. Si tienes problemas para conectar Sparrow, te recomiendo que leas el principio de este tutorial:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Haga clic en la pestaña "*Archivo*" y, a continuación, en "*Nuevo Wallet*".



![Image](assets/fr/32.webp)



Asigne un nombre a su cartera y haga clic en "*Crear Wallet*".



![Image](assets/fr/33.webp)



En el menú desplegable "*Tipo de script*", selecciona el tipo de script que se utilizará para asegurar tus bitcoins. Yo recomiendo "*Taproot*", o en su defecto, "*Native SegWit*".



![Image](assets/fr/34.webp)



Haga clic en el botón "*Hardware Wallet conectada*". Por supuesto, su Safe 3 debe estar conectada al ordenador y desbloqueada.



![Image](assets/fr/35.webp)



Haga clic en el botón "*Escanear*". Debería aparecer tu Safe 3. Haga clic en "*Importar almacén de claves*".



![Image](assets/fr/36.webp)



Ahora puede ver los detalles de su Wallet, incluida la clave pública ampliada de su primera cuenta. Haz clic en el botón "*Aplicar*" para finalizar la creación de la Wallet.



![Image](assets/fr/37.webp)



Elija una contraseña fuerte para asegurar el acceso a Sparrow Wallet. Esta contraseña garantizará un acceso seguro a sus datos de Sparrow Wallet, protegiendo sus claves públicas, direcciones, etiquetas e historial de transacciones de accesos no autorizados.



Te aconsejo que guardes esta contraseña en un gestor de contraseñas para que no la olvides.



![Image](assets/fr/38.webp)



¡Y ahora su cartera ha sido importada a Sparrow Wallet!



![Image](assets/fr/39.webp)



Antes de recibir tus primeros bitcoins en tu Wallet, **te aconsejo encarecidamente que realices una prueba de recuperación en vacío**. Anota alguna información de referencia, como tu xpub, luego reinicia tu Trezor Safe 3 mientras la Wallet está todavía vacía. A continuación, intente restaurar su Wallet en el Trezor utilizando sus copias de seguridad en papel. Comprueba que el xpub generado tras la restauración coincide con el que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables.



Para saber más sobre cómo realizar una prueba de recuperación, te sugiero que consultes este otro tutorial:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## ¿Cómo puedo recibir bitcoins con Trezor Safe 3?



En Sparrow, haz clic en la pestaña "*Recibir*".



![Image](assets/fr/40.webp)



Antes de utilizar la Address propuesta por Sparrow Wallet, compruébala en la pantalla de tu Trezor. Esta práctica le permite confirmar que la Address mostrada en Sparrow no es fraudulenta, y que la Hardware Wallet posee efectivamente la clave privada necesaria para gastar posteriormente los bitcoins asegurados con esta Address. Esto te ayuda a evitar varios tipos de ataques.



Para realizar esta comprobación, haga clic en el botón "*Visualizar Address*".



![Image](assets/fr/41.webp)



Comprueba que el Address que aparece en tu Trezor coincide con el del Sparrow Wallet. También es aconsejable realizar esta comprobación justo antes de comunicar tu Address al remitente, para estar seguro de su validez. Puedes utilizar los botones para confirmar.



![Image](assets/fr/42.webp)



A continuación, puedes añadir una "*Etiqueta*" para describir la fuente de bitcoins que se asegurará con esta Address. Esta es una buena práctica que te permite gestionar mejor tus UTXOs.



![Image](assets/fr/43.webp)



A continuación, puede utilizar este Address para recibir bitcoins.



![Image](assets/fr/44.webp)



## ¿Cómo envío bitcoins con Trezor Safe 3?



Ahora que has recibido tus primeros Satss en tu Safe 3-secured Wallet, ¡también puedes gastarlos! Conecta tu Trezor a tu ordenador, desbloquéalo con el código PIN, inicia Sparrow Wallet y ve a la pestaña "*Enviar*" para crear una nueva transacción.



![Image](assets/fr/45.webp)



Si desea *Coin Control*, es decir, elegir específicamente qué UTXOs consumir en la transacción, vaya a la pestaña "*UTXOs*". Seleccione los UTXOs que desea gastar y, a continuación, haga clic en "*Enviar seleccionados*". Será redirigido a la misma pantalla de la pestaña "*Enviar*", pero con sus UTXOs ya seleccionados para la transacción.



![Image](assets/fr/46.webp)



Introduzca la Address de destino. También puede introducir varias direcciones haciendo clic en el botón "*+ Añadir*".



![Image](assets/fr/47.webp)



Escriba una "*etiqueta*" para recordar la finalidad de este gasto.



![Image](assets/fr/48.webp)



Seleccione el importe que se enviará a esta Address.



![Image](assets/fr/49.webp)



Ajuste el tipo de comisión de su operación en función del mercado actual. Por ejemplo, puede utilizar [Mempool.space](https://Mempool.space/) para elegir una tasa de comisión adecuada.



Asegúrese de que todos los parámetros de la transacción son correctos y, a continuación, haga clic en "*Crear transacción*".



![Image](assets/fr/50.webp)



Si todo está a su satisfacción, haga clic en "*Finalizar transacción para firmar*".



![Image](assets/fr/51.webp)



Haga clic en "*Firmar*".



![Image](assets/fr/52.webp)



Haga clic en "*Firmar*" junto a su Trezor Safe 3.



![Image](assets/fr/53.webp)



Compruebe los parámetros de la transacción en la pantalla de su Hardware Wallet, incluyendo la Address receptora del destinatario, el importe enviado y el cargo. Una vez verificada la transacción en el Trezor, pulsa simultáneamente los dos botones para firmarla.



![Image](assets/fr/54.webp)



Su transacción ya está firmada. Compruebe por última vez que todo está correcto y, a continuación, haga clic en "*Emisión de transacción*" para emitirla en la red Bitcoin.



![Image](assets/fr/55.webp)



Puedes encontrarlo en la pestaña "*Transacciones*" de Sparrow Wallet.



![Image](assets/fr/56.webp)



¡Enhorabuena, ya estás al día en el uso básico del Trezor Safe 3 con Sparrow Wallet! Para ir un paso más allá, te recomiendo este completo tutorial sobre el uso de un Trezor Hardware Wallet con un BIP39 passphrase para mejorar tu seguridad:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!