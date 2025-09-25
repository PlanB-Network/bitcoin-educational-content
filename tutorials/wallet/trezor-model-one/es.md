---
name: Trezor Model One
description: Configuración y uso de la Hardware Wallet Modelo Uno
---
![cover](assets/cover.webp)



*Crédito de la imagen: [Trezor.io](https://trezor.io/)*



El Trezor Model One es el primer Hardware Wallet que salió al mercado, lanzado en 2014 por SatoshiLabs. Después de más de diez años de existencia, sigue siendo una opción interesante, especialmente para los usuarios que buscan un Hardware Wallet accesible tanto técnicamente como en términos de presupuesto. De hecho, tiene un precio de 49 € en la web oficial de Trezor. Es uno de los únicos monederos hardware en este rango de precios. Se sitúa a medio camino entre los dispositivos básicos de unos 20 euros, como el Tapsigner, que a menudo carecen de pantalla, y los dispositivos de gama media de unos 80 euros, como el Ledger Nano S Plus o el Trezor Safe 3.



El Model One cuenta con una pantalla OLED monocroma de 0,96 pulgadas y dos botones físicos. Funciona sin batería, utilizando únicamente una conexión micro USB para alimentación y datos Exchange.



![Image](assets/fr/01.webp)



El principal inconveniente del Modelo Uno es su falta de Elemento Seguro, que lo hace vulnerable a diversos ataques físicos, algunos de los cuales son relativamente sencillos de ejecutar. Estos ataques pueden incluir el análisis de canales auxiliares para determinar el PIN del dispositivo, o técnicas más avanzadas para extraer el seed cifrado con el fin de forzarlo posteriormente. Tenga en cuenta que estos ataques requieren acceso físico al dispositivo. Sin embargo, esta vulnerabilidad puede reducirse considerablemente utilizando una passphrase BIP39 sólida. Si optas por esta Hardware Wallet, te aconsejo encarecidamente que configures una passphrase.



El Modelo Uno ofrece dos ventajas importantes:




- Se basa en una arquitectura completamente de código abierto. A diferencia de los modelos más recientes con Secure Element, todos los componentes de hardware y software del Model One son auditables;
- Está equipado con una pantalla. Que yo sepa, es el único Hardware Wallet del mercado en este rango de precios con pantalla. Se trata de una característica muy importante, ya que permite verificar la información firmada y las direcciones de recepción, evitando así muchos ataques digitales.



Por lo tanto, el Trezor Model One puede representar una elección acertada para usuarios principiantes e intermedios con un presupuesto limitado. Sin embargo, es importante ser consciente de sus limitaciones en términos de protección física, debido a la ausencia de Secure Element. Si su presupuesto es limitado, es una buena opción, pero si puede permitirse optar por un modelo superior, como el Trezor Safe 3 a 79 euros, es preferible, ya que incluye un Elemento Seguro.



## Unboxing del Trezor Model One



Cuando reciba su Model One, asegúrese de que la caja y el Seal están intactos para confirmar que el paquete no ha sido abierto. También se llevará a cabo una verificación por software de la autenticidad e integridad del dispositivo cuando se configure posteriormente.



El contenido de la caja incluye :




- El Trezor Modelo Uno;
- Cartulina para grabar tu frase Mnemonic, pegatinas e instrucciones;
- Cable USB-A a micro-USB.



![Image](assets/fr/02.webp)



Navegar por el dispositivo es muy sencillo:




- Haga clic con el botón derecho del ratón para confirmar y continuar con los pasos siguientes;
- Utilice el botón izquierdo para volver atrás.



## Requisitos previos



En este tutorial, voy a mostrarle cómo utilizar el Trezor Model One con el [software de gestión de carteras Sparrow Wallet](https://sparrowwallet.com/download/). Si aún no ha instalado este software, hágalo ahora. Si necesita ayuda, también tenemos un tutorial detallado sobre la configuración de Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

También necesitarás el software Trezor Suite para configurar el Model One, comprobar su autenticidad e instalar el firmware. Sólo utilizaremos este software para eso, y después sólo será necesario para las actualizaciones del firmware. Para la gestión diaria de la Wallet, usaremos exclusivamente Sparrow Wallet, ya que está optimizado para Bitcoin y es fácil de usar, incluso para principiantes (Sparrow sólo soporta Bitcoin, no altcoins).



[Descargar Trezor Suite desde el sitio web oficial](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Para estos dos programas, te recomiendo encarecidamente que compruebes tanto su autenticidad (con GnuPG) como su integridad (mediante Hash) antes de instalarlos en tu máquina. Si no sabes cómo hacerlo, puedes seguir este otro tutorial :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Arrancar el Trezor Model One



Conecte su Model One a su ordenador donde ya están instalados Trezor Suite y Sparrow Wallet.



![Image](assets/fr/04.webp)



Abra Trezor Suite y haga clic en "*Configurar mi Trezor*".



![Image](assets/fr/05.webp)



Seleccione "*Bitcoin-only firmware*" y, a continuación, haga clic en "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite instalará el firmware en su Model One. Por favor, espere durante la instalación.



![Image](assets/fr/07.webp)



Haga clic en "*Continuar*".



![Image](assets/fr/08.webp)



## Crear una cartera Bitcoin



En Trezor Suite, haga clic en el botón "*Crear nuevo Wallet*".



![Image](assets/fr/09.webp)



Acepta las condiciones de uso de Hardware Wallet.



![Image](assets/fr/10.webp)



En Trezor Suite, haga clic en "*Continuar con la copia de seguridad*".



![Image](assets/fr/11.webp)



El software proporciona instrucciones sobre cómo gestionar su frase Mnemonic.



Este Mnemonic te da acceso completo y sin restricciones a todos tus bitcoins. Cualquiera en posesión de esta frase puede robar sus fondos, incluso sin acceso físico a su Trezor Modelo Uno.



La frase de 24 palabras restablece el acceso a tus bitcoins en caso de pérdida, robo o rotura de tu Hardware Wallet. Por lo tanto, es muy importante guardarla con cuidado y almacenarla en un lugar seguro.



Puede escribirlo en el cartón suministrado en la caja o, para mayor seguridad, le recomiendo grabarlo en una base de acero inoxidable para protegerlo de incendios, inundaciones o derrumbes.



Confirma las instrucciones y haz clic en el botón "*Crear copia de seguridad de Wallet*".



![Image](assets/fr/12.webp)



El Model One creará su frase Mnemonic utilizando su generador de números aleatorios. Asegúrese de que no le están observando durante esta operación. Escriba las palabras proporcionadas en la pantalla en el soporte físico de su elección. Dependiendo de su estrategia de seguridad, puede considerar hacer varias copias físicas completas de la frase (pero sobre todo, no la divida). Es importante mantener las palabras numeradas y en orden secuencial.



**Obviamente, nunca debes compartir estas palabras en Internet, como hago yo en este tutorial. Este ejemplo Wallet se utilizará sólo en el Testnet y se borrará al final del tutorial**



Para más información sobre la forma correcta de guardar y gestionar tu frase Mnemonic, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Para pasar a las palabras siguientes, haz clic con el botón derecho. Cuando hayas escrito todas las palabras, vuelve a hacer clic con el botón derecho para pasar al siguiente paso.



![Image](assets/fr/13.webp)



Tu Hardware Wallet te muestra de nuevo todas tus palabras. Comprueba que las has escrito todas.



![Image](assets/fr/14.webp)



## Configurar el código PIN



A continuación viene el paso del código PIN. El código PIN desbloquea su Trezor. Por lo tanto, proporciona protección contra el acceso físico no autorizado. Este código PIN no interviene en la derivación de las claves criptográficas de su Wallet. Así que incluso sin acceso al código PIN, la posesión de su frase Mnemonic de 12 palabras le permitirá recuperar el acceso a sus bitcoins.



En Trezor Suite, haga clic en "*Continuar con PIN*" y, a continuación, en el botón "*Configurar PIN*".



![Image](assets/fr/15.webp)



Confirmar en el Modelo Uno.



![Image](assets/fr/16.webp)



Le recomendamos que elija un código PIN lo más aleatorio posible. Asegúrese de guardar este código en un lugar distinto de donde esté almacenado su Trezor (por ejemplo, en un gestor de contraseñas). Puede definir un código PIN de entre 8 y 50 dígitos. Le recomiendo que elija un código PIN lo más largo posible para aumentar la seguridad.



El código PIN debe introducirse en Trezor Suite en su ordenador haciendo clic en los puntos correspondientes a los dígitos, según la configuración del teclado que aparece en el Trezor Modelo Uno.



Este método específico de introducción del PIN es necesario cada vez que desbloquee su Trezor Modelo Uno, ya sea a través de Trezor Suite o Sparrow Wallet.



![Image](assets/fr/17.webp)



Una vez que haya terminado, pulse el botón "*Introducir PIN*".



![Image](assets/fr/18.webp)



Escriba de nuevo su PIN para confirmar.



![Image](assets/fr/19.webp)



En Trezor Suite, haga clic en el botón "*Completar configuración*".



![Image](assets/fr/20.webp)



La configuración de su Modelo Uno ha finalizado. Si lo desea, puede cambiar el nombre y la página de inicio de su Hardware Wallet.



![Image](assets/fr/21.webp)



Ya no necesitaremos el software Trezor Suite, excepto para realizar actualizaciones periódicas de firmware en su Hardware Wallet, o si desea realizar una prueba de recuperación. Ahora vamos a utilizar Sparrow para gestionar la cartera, ya que este software se adapta perfectamente al uso exclusivo de Bitcoin.



## Configuración de la cartera en Sparrow Wallet



Empieza descargando e instalando Sparrow Wallet [desde el sitio web oficial](https://sparrowwallet.com/) en tu ordenador, si aún no lo has hecho.



Una vez que hayas abierto Sparrow Wallet, asegúrate de que el software está conectado a un nodo Bitcoin, lo que se indica con la marca en la esquina inferior derecha de Interface. Si tienes problemas para conectar Sparrow, te recomiendo que consultes el principio de este tutorial:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Haga clic en la pestaña "*Archivo*" y, a continuación, en "*Nuevo Wallet*".



![Image](assets/fr/22.webp)



Asigne un nombre a su cartera y haga clic en "*Crear Wallet*".



![Image](assets/fr/23.webp)



En el menú desplegable "*Tipo de script*", selecciona el tipo de script que se utilizará para asegurar tus bitcoins. Yo recomiendo "*Taproot*", o en su defecto, "*Native SegWit*".



![Image](assets/fr/24.webp)



Haga clic en el botón "*Hardware Wallet conectado*". Por supuesto, su Model One debe estar conectado al ordenador.



![Image](assets/fr/25.webp)



Haga clic en el botón "*Escanear*". Debería aparecer su Modelo Uno.



Cuando conecte su Modelo Uno a un ordenador con Sparrow Wallet abierto, se le pedirá que introduzca un passphrase BIP39 en Sparrow. Esta opción avanzada será cubierta en un futuro tutorial. Por ahora, puede simplemente seleccionar "*Desactivar passphrase*" para evitar que su Trezor le pida que introduzca un passphrase cada vez que se inicie.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Haga clic en "*Importar almacén de claves*".



![Image](assets/fr/27.webp)



Ahora puede ver los detalles de su Wallet, incluida la clave pública extendida de su primera cuenta. Haga clic en el botón "*Aplicar*" para finalizar la creación de la Wallet.



![Image](assets/fr/28.webp)



Elija una contraseña fuerte para asegurar el acceso a Sparrow Wallet. Esta contraseña garantizará un acceso seguro a sus datos de Sparrow Wallet, protegiendo sus claves públicas, direcciones, etiquetas e historial de transacciones de accesos no autorizados.



Te aconsejo que guardes esta contraseña en un gestor de contraseñas para que no la olvides.



![Image](assets/fr/29.webp)



¡Y ahora su cartera ha sido importada a Sparrow Wallet!



![Image](assets/fr/30.webp)



Antes de recibir sus primeros bitcoins en su Wallet, **le aconsejo encarecidamente que realice una prueba de recuperación en vacío**. Anota alguna información de referencia, como tu xpub, luego reinicia tu Trezor Modelo Uno mientras la Wallet está todavía vacía. A continuación, intente restaurar su Wallet en el Trezor utilizando sus copias de seguridad en papel. Comprueba que el xpub generado tras la restauración coincide con el que anotaste originalmente. Si es así, puede estar seguro de que sus copias de seguridad en papel son fiables.



Para saber más sobre cómo realizar una prueba de recuperación, te sugiero que consultes este otro tutorial:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## ¿Cómo recibir bitcoins con el Trezor Model One?



En Sparrow, haz clic en la pestaña "*Recibir*".



![Image](assets/fr/31.webp)



Antes de utilizar la Address propuesta por Sparrow Wallet, compruébala en la pantalla de tu Trezor. Esta práctica le permite confirmar que la Address mostrada en Sparrow no es fraudulenta, y que la Hardware Wallet posee efectivamente la clave privada necesaria para gastar posteriormente los bitcoins asegurados con esta Address. Esto te ayuda a evitar varios tipos de ataques.



Para realizar esta comprobación, pulse el botón "*Visualizar Address*".



![Image](assets/fr/32.webp)



Comprueba que el Address que aparece en tu Trezor coincide con el del Sparrow Wallet. También es aconsejable realizar esta comprobación justo antes de comunicar tu Address al remitente, para estar seguro de su validez. Puedes pulsar el botón derecho para confirmar.



![Image](assets/fr/33.webp)



También puedes añadir una "*Etiqueta*" para describir la fuente de bitcoins que se asegurará con este Address. Esta es una buena práctica que te permite gestionar mejor tus UTXOs.



![Image](assets/fr/34.webp)



A continuación, puede utilizar esta Address para recibir bitcoins.



![Image](assets/fr/35.webp)



## ¿Cómo enviar bitcoins con el Trezor Model One?



Ahora que has recibido tus primeros Satss en tu Wallet asegurada por Modelo Uno, ¡también puedes gastarlos! Conecta tu Trezor a tu ordenador, inicia Sparrow Wallet y ve a la pestaña "*Enviar*" para crear una nueva transacción.



![Image](assets/fr/36.webp)



Si desea *Coin Control*, es decir, elegir específicamente qué UTXOs consumir en la transacción, vaya a la pestaña "*UTXOs*". Seleccione los UTXOs que desea gastar y, a continuación, haga clic en "*Enviar seleccionados*". Será redirigido a la misma pantalla de la pestaña "*Enviar*", pero con sus UTXOs ya seleccionados para la transacción.



![Image](assets/fr/37.webp)



Introduzca la Address de destino. También puede introducir varias direcciones haciendo clic en el botón "*+ Añadir*".



![Image](assets/fr/38.webp)



Escriba una "*etiqueta*" para recordar la finalidad de este gasto.



![Image](assets/fr/39.webp)



Seleccione el importe que se enviará a este Address.



![Image](assets/fr/40.webp)



Ajuste la tarifa de su transacción en función del mercado actual. Por ejemplo, puede utilizar [Mempool.space](https://Mempool.space/) para elegir una tasa de comisión adecuada.



Asegúrese de que todos los parámetros de la transacción son correctos y, a continuación, haga clic en "*Crear transacción*".



![Image](assets/fr/41.webp)



Si todo está a su satisfacción, haga clic en "*Finalizar transacción para firmar*".



![Image](assets/fr/42.webp)



Haga clic en "*Firmar*".



![Image](assets/fr/43.webp)



Haga clic en "*Firmar*" junto a su Trezor Modelo Uno.



![Image](assets/fr/44.webp)



Compruebe los parámetros de la transacción en la pantalla de su Hardware Wallet, incluidos el Address receptor del destinatario, el importe enviado y la comisión. Una vez verificada la transacción en el Trezor, haz clic con el botón derecho del ratón para firmarla.



![Image](assets/fr/45.webp)



Su transacción ya está firmada. Compruebe por última vez que todo está correcto y haga clic en "Transmitir transacción" para transmitirla a la red Bitcoin.



![Image](assets/fr/46.webp)



Puedes encontrarlo en la pestaña "*Transacciones*" de Sparrow Wallet.



![Image](assets/fr/47.webp)



¡Enhorabuena, ya estás al día en el uso básico del Trezor Modelo Uno con Sparrow Wallet! Para ir un paso más allá, te recomiendo este completo tutorial sobre el uso de un Trezor Hardware Wallet con un BIP39 passphrase para reforzar tu seguridad :



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este artículo en tus redes sociales. Muchas gracias