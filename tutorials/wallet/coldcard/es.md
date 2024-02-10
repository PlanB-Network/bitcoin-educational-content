---
name: Cold Card

description: Creación, copia de seguridad y uso de una clave privada de Bitcoin con un dispositivo Coldcard y Bitcoin Core.
---

![cover](assets/cover.jpeg)

Creación, copia de seguridad y uso de una clave privada Bitcoin con un dispositivo Coldcard y Bitcoin Core

## ¡Guía completa para generar una clave privada usando una Coldcard y su uso a través de la interfaz de su nodo Bitcoin Core!

En la base del uso de la red Bitcoin se encuentra el concepto de criptografía asimétrica: un par de claves -una privada y otra pública- que cifran y descifran datos, un concepto que garantiza la confidencialidad de la comunicación.

En el caso de Bitcoin, al generar ese par de claves privada y pública, podemos almacenar bitcoins (UTXO o Unspent Transaction Output) y firmar transacciones para gastarlos.

Hoy en día, existen múltiples herramientas que facilitan la generación aleatoria de una clave privada y su respaldo en forma textual utilizando BIP 39 - un estándar que determina cómo los monederos asocian una frase mnemotécnica (frase semilla) con las claves de cifrado. En la mayoría de los casos, la frase mnemotécnica consta de 12 o 24 palabras, de las que hay que hacer una copia de seguridad para poder recuperar un monedero y sus bitcoins.

En este artículo, aprenderemos a generar una clave privada usando una Coldcard Mk4, uno de los dispositivos más extendidos y seguros en el mundo de Bitcoin, usando el método de tirada de dados para asegurar la máxima entropía, ¡y cómo usarla con Bitcoin Core de forma air-gapped!

> 🧰| Consigue las siguientes herramientas para seguir la guía:
>
> - Dispositivo Coldcard (Mk3 o Mk4)
> - Tarjeta MicroSD (4GB es suficiente)
> - Cable USB magnético de sólo alimentación (mini-usb para Mk3, usb-c para Mk4)
> - Uno o varios dados de calidad

## Generar una nueva frase mnemotécnica con una Coldcard

Comenzaremos el proceso de creación de una clave privada desde cero, suponiendo una Coldcard recién desempaquetada en la que ya se ha configurado un PIN (siga los pasos indicados en la Coldcard durante la inicialización del dispositivo).

> 🚨 | Para restablecer la clave privada de una Coldcard ya configurada, siga estos pasos:
> Avanzado/Herramientas > Zona de peligro > Funciones de semilla > Destruir semilla>
>
> _Atención_: su Coldcard olvidará la clave privada después de estos pasos. Asegúrese de haber guardado correctamente su frase mnemotécnica si desea poder recuperarla más adelante.

## Pasos a seguir:

Conectar la Coldcard con el NIP > Nuevas palabras de semilla > Lanzamiento de dados de 24 palabras

Realice 100 lanzamientos de dados escribiendo el resultado obtenido del 1 al 6 en la Coldcard después de cada lanzamiento. Al practicar este método, está creando 256 bytes de entropía, lo que favorece la creación de una clave privada completamente aleatoria. Coinkite también proporciona la documentación necesaria para la verificación independiente de su sistema de generación de entropía.

![Captura de pantalla de Cold Card](assets/guide-agora/1.jpeg)

Una vez que se hayan completado los 100 lanzamientos de dados, presione ✓ y luego anote las 24 palabras obtenidas en orden. Verifique dos veces y presione ✓. ¡Finalmente, solo queda completar la prueba de verificación de las 24 palabras en la Coldcard, y ahí está, su nueva clave privada creada!

Luego elija si desea activar o no las funciones NFC (Mk4) y USB siguiendo los pasos que se muestran. Una vez en el menú principal, es hora de actualizar el microfirmware del dispositivo. Vaya a Advanced/Tools > Upgrade Firmware > Show Version y consulte el sitio web oficial para validar y descargar la última versión disponible. Se recomienda actualizar la Coldcard para obtener la máxima seguridad.

Antes de continuar, se recomienda tomar nota de la huella digital de la clave maestra (XFP) asociada a la clave privada. Este dato permite validar rápidamente si se encuentra en la billetera correcta en caso de recuperación, por ejemplo. Vaya a Advanced/Tools > View Identity > Master Key Fingerprint (XFP) y anote la serie de ocho caracteres alfanuméricos obtenidos. El XFP se puede anotar en el mismo lugar que la frase mnemotécnica, no es un dato sensible.

> 💡 Se recomienda probar su copia de seguridad de la frase mnemotécnica en un software diferente. Para hacerlo de manera segura, consulte nuestro artículo Verificar la copia de seguridad de una billetera de Bitcoin con Tails en menos de 5 minutos.

## Bonus de seguridad: la "Frase Secreta" (opcional)

'Una frase secreta (passphrase) es un elemento formidable para agregar a una configuración de billetera para agregar una capa de seguridad y proteger tus bitcoins. La frase secreta actúa de alguna manera como una palabra 25 en la frase mnemotécnica. Una vez que se agrega una, se crea una billetera completamente nueva junto con una clave privada y su frase mnemotécnica asociada. No es necesario tomar nota de la nueva frase mnemotécnica, ya que esta billetera se puede acceder combinando la frase mnemotécnica inicial con la frase secreta elegida.

El objetivo es anotar la frase secreta por separado de la frase mnemotécnica, ya que un atacante que tenga acceso a ambos elementos tendrá acceso a los fondos que se encuentren allí. Por otro lado, un atacante que solo tenga acceso a uno de estos elementos no tendrá acceso a los fondos, y es esta ventaja específica la que optimiza el nivel de seguridad de la configuración de la billetera.

![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.jpeg)

## Pasos a seguir para agregar una frase secreta con Coldcard:

Passphrase > Add Words (recomendado) > Apply. El dispositivo mostrará el XFP de la billetera recién generada con la frase secreta, que se recomienda anotar junto con la frase secreta por las mismas razones mencionadas anteriormente.

> 💡 Recursos adicionales relacionados con la frase secreta:

> https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af > https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/ > https://armantheparman.com/passphrase/

## Exportación de la billetera a Bitcoin Core

La billetera ahora está lista para ser exportada a un software para interactuar con la red de Bitcoin. En esta guía, utilizaremos Bitcoin Core (v24.1).

Consulte nuestras guías de instalación y configuración de Bitcoin Core:

> Faire tourner son propre noeud avec Bitcoin Core - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Configuration de Tor pour un nœud Bitcoin Core - https://agora256.com/configuration-tor-bitcoin-core/

Primero, inserta una tarjeta micro SD en Coldcard y luego exporta la billetera a Bitcoin Core siguiendo estos pasos: Advanced/Tools > Export Wallet > Bitcoin Core. Dos archivos se registrarán en la tarjeta micro SD: bitcoin-core.sig y bitcoin-core.txt. Inserta la tarjeta micro SD en la computadora en la que está instalado Bitcoin Core y abre el archivo .txt. Verás la línea "For wallet with master key fingerprint". Verifica que el XFP de ocho caracteres coincida con el que anotaste al crear tu clave privada.'

Antes de seguir las instrucciones del archivo, comencemos por preparar la billetera en la interfaz de Bitcoin Core siguiendo estos pasos: ve a la pestaña Archivo > Crear una billetera. Elije un nombre para tu billetera (término intercambiable con "porte-monnaie" en Core) y marca las opciones Desactivar las claves privadas, Crear una billetera vacía y Billetera de descriptores como se muestra en la imagen a continuación. Luego, presiona el botón Crear.

![crée un portefeuille](assets/guide-agora/3.jpeg)

Una vez creada la billetera en Bitcoin Core, ve a la pestaña Ventana > Consola y asegúrate de que la billetera seleccionada en la parte superior de la página muestre correctamente el nombre de la que creaste.

Ahora, en el archivo .txt generado previamente por la Coldcard, copia la línea que comienza con "importdescriptors" y pégala en la consola de Bitcoin Core. Debería devolver una respuesta que incluya la línea "success": true.

![ fenetre des noeuds ](assets/guide-agora/4.jpeg)

Si la respuesta contiene "message": "Ranged descriptors should not have a label", borra la entrada "label": "Coldcard xxxx0000" en la línea copiada del archivo .txt y luego pega la línea completa nuevamente en la consola de Bitcoin Core.

Ayuda: [https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## Validación de la importación de la billetera en Bitcoin Core

Para asegurarse de que la operación se haya realizado correctamente, es necesario validar que se haya importado la billetera deseada en Bitcoin Core. Una forma sencilla de confirmarlo es verificar que las direcciones generadas en la Coldcard coincidan con las direcciones generadas en Bitcoin Core.

Bitcoin Core: Recibir > Crear una nueva dirección de recepción
Coldcard: Address Explorer > Elegir la dirección que comienza con bc1q. La dirección Coldcard 'bc1q' debe coincidir con la dirección mostrada en Bitcoin Core.
Recibir y enviar transacciones en modo 'air-gapped'

Recibir una transacción es extremadamente sencillo; simplemente presiona Recibir, etiqueta la transacción (opcional pero recomendado) y crea una nueva dirección de recepción. Luego, solo queda compartir la dirección con el remitente.

Ahora, el elemento clave de esta configuración Coldcard + Bitcoin Core es enviar transacciones sin que la Coldcard y su clave privada estén conectadas a Internet, utilizando un método llamado "air-gapped" que utiliza la función TBSP (PSBT - Partially Signed Bitcoin Transactions) de Bitcoin.
Essentially, we use the Bitcoin Core interface to build a transaction, which we will then export via the micro SD card to the Coldcard to sign, and then return the signed transaction file to Bitcoin Core and broadcast the transaction to the network. We have to do it this way because the wallet imported into Bitcoin Core does not have a private key, only the public key (which allows us to generate our receiving addresses), so it is impossible for us to sign a transaction within the software to spend our bitcoins.

Before proceeding, make sure the following options are enabled in Settings > Wallet:

> - Enable coin control features
> - Spend unconfirmed coins (Optional)
> - Enable TBPS checks

![option ](assets/guide-agora/5.jpeg)

### Steps to send in air-gapped mode:

Send > Inputs > choose the desired utxo, then enter the recipient's address in Pay to. Transaction fee: Choose... > Custom > Enter the transaction fee (Bitcoin Core calculates in sats/kilobyte rather than sat/byte like most alternative wallet solutions. So 4000 sats/kilobyte = 4 sats/byte). Create an unsigned transaction > save the file to your micro SD card and insert it into the Coldcard.

In the Coldcard, press Ready to sign, check the transaction details, then press ✓ and insert the micro SD card back into the computer once the signed files are generated.

Back in Bitcoin Core, go to the File tab > Load TBSP from file, and enter the signed transaction file .psbt. The PSBT Operations box will appear on the screen, confirming that the transaction is fully signed and ready to be broadcasted. Just press Broadcast transaction.

![PSBT operations](assets/guide-agora/6.jpeg)

### Conclusion

The combination of the Coldcard device with Bitcoin Core, on which you run your own node, is powerful. Add to that a private key generated with 100 dice rolls and a secret phrase, and your wallet configuration becomes a sophisticated and robust fortress.

Feel free to contact us to share all your comments and questions! Our goal is to share our knowledge and increase our understanding day by day.
