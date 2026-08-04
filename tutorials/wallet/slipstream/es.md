---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normalmente, cuando firmas una transacción, esta se retransmite automáticamente a todos los nodos de la red Bitcoin. Luego espera a ser minada.

Sin embargo, mientras no esté incluida en un bloque, un atacante que haya obtenido tu clave privada podría reemplazarla y robar los fondos. Este es típicamente el caso si utilizas una cartera hardware ColdCard.

La herramienta Slipstream, de la empresa minera MARA, te permite evitar la retransmisión de la transacción a la red: se envía directamente (y únicamente) a un minero, lo que la mantiene privada y evita exponerla en la red. Es probable que la transacción tarde más en ser minada, pero estará protegida contra un ataque de reemplazo.

A continuación, ofrecemos un tutorial que permite a los usuarios de [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), así como a los usuarios de la cartera [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), utilizar la herramienta Slipstream del minero MARA a través de la página [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Advertencia**: esta herramienta está pensada únicamente para ciertos perfiles, principalmente carteras Liana, carteras miniscript y algunos tipos de multisig. Wizardsardine **desaconseja explícitamente** su uso para carteras cuyos fondos ya estén en riesgo crítico de robo, por ejemplo aquellas cuya frase de recuperación fue generada en un dispositivo ColdCard afectado por la vulnerabilidad del generador de números aleatorios. En esa situación, la carrera contra el atacante se juega en cuestión de segundos, y una transacción enviada a un único minero tarda mucho más en confirmarse que una retransmitida normalmente. Si esto te preocupa, lee primero nuestro tutorial dedicado:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Para usuarios de Liana

Liana está mantenida por Wizardsardine, editor de la página [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), por lo que el camino es directo: simplemente exportas el archivo PSBT firmado en lugar de retransmitirlo.

*Requisito previo: tener fondos en tu cartera Liana.*

### Paso 1: Crea tu transacción con Liana

Como de costumbre, construye tu transacción añadiendo la dirección de destino, la descripción y el importe (aquí, el máximo disponible en la cartera).

Para configurar la tasa de comisión:

- selecciona las monedas que quieres gastar haciendo clic en la pequeña casilla de la parte inferior izquierda, debajo de "Coins selection";
- luego introduce la tasa de comisión. Recuerda establecer comisiones mucho más altas que la tasa sugerida, tal como se describe en esta página: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Finalmente, haz clic en "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Paso 2: Verifica los detalles de tu transacción

Antes de hacer clic en "Sign", verifica los detalles de tu transacción; en particular:

- el importe enviado;
- el número de satoshis destinado a las comisiones de la transacción;
- pero sobre todo, la dirección a la que estás enviando los fondos (recuerda comprobar los primeros 5/6 caracteres, los últimos 5/6, y 5/6 caracteres en el medio de la dirección para evitar ataques de "envenenamiento de direcciones" o "address poisoning").

![Checking the transaction details](assets/fr/02.webp)

### Paso 3: Selecciona las carteras firmantes

A continuación, selecciona las carteras de software y/o hardware con las que necesitas firmar tu transacción. Un recordatorio rápido: en el caso de una cartera multisig 2 de 2, necesitas 2 firmas de 2.

### Paso 4: Exporta el archivo PSBT de tu transacción

La transacción de Bitcoin ya está firmada por las claves correspondientes. No hagas clic en "Broadcast", ya que de lo contrario se compartirá con toda la red y, si usas una cartera hardware ColdCard, tu transacción quedará expuesta públicamente y tus fondos estarán en riesgo.

Ahora puedes hacer clic en "Export" y luego guardar el archivo PSBT localmente en tu ordenador.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Paso 5: Envía la transacción al minero a través de outofband.wizardsardine.com

Ahora vienen los últimos pasos. Para enviar la transacción al minero, solo tienes que tomar el archivo PSBT y arrastrarlo y soltarlo en el área designada.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

La transacción se muestra entonces como se indica a continuación.

![Transaction in the queue](assets/fr/05.webp)

### Paso 6: Envía la transacción mediante Slipstream

Finalmente, solo tienes que hacer clic en "Send" para que la transacción se envíe a MARA a través de Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

En cuestión de segundos, la transacción pasa de "Sending" a "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Solo queda copiar el identificador de la transacción (TXID) y pegarlo en [mempool.space](https://mempool.space/) para ver cómo se mina:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Ten en cuenta: la transacción aparecerá como "Transaction not found" hasta que el minero, MARA, mine un bloque e incluya tu transacción en él. Esto puede tardar varias decenas de minutos, o incluso horas, ya que MARA solo posee alrededor del 4,5 % del hash rate de la red Bitcoin. A fecha de 4 de agosto de 2026, esto corresponde aproximadamente a un bloque minado cada 3 horas y 45 minutos.

## Para usuarios de otras carteras

Si no utilizas [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) pero aun así quieres usar la herramienta, aquí tienes un tutorial que utiliza una cartera multisig 2 de 2. Para ello, usaremos la cartera de software [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Requisito previo: tener fondos en tu cartera Sparrow.*

### Paso 1: Crea tu transacción

Con [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), crea la transacción en tu cartera multisig. Recuerda establecer comisiones mucho más altas que la tasa sugerida, tal como se describe en esta página: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Una vez creada, haz clic en "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Paso 2: Finaliza tu transacción

Para finalizar tu transacción, ahora necesitas firmarla. Para ello, haz clic en "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Paso 3: Firma tu transacción con tus distintas claves

Ahora llega el momento de firmar la transacción. Para ello, simplemente fírmala con la(s) cartera(s) de software o hardware que uses.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Paso 4: Descarga la transacción firmada y no la retransmitas a la red

La transacción de Bitcoin ya está firmada por ambas claves de nuestro multisig 2 de 2. No hagas clic en "Broadcast Transaction", ya que de lo contrario se compartirá con toda la red y, si usas una cartera hardware ColdCard, tu transacción quedará expuesta públicamente y tus fondos estarán en riesgo.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Paso 5: Muestra el script de la transacción firmada, o descarga el archivo PSBT

Para mostrar la transacción de Bitcoin firmada, haz clic ahora en "View Final Transaction". Después puedes copiar el script de la transacción de Bitcoin firmada:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Si quieres descargar el archivo de la transacción, puedes:

- hacer clic en "File" y luego en "Save transaction…";
- o hacer clic en el botón de conexión de red en la parte inferior derecha (botón amarillo) y luego en "Save Final Transaction".

La transacción se guardará entonces localmente en tu ordenador.

![Saving the final transaction locally](assets/fr/14.webp)

### Paso 6: Envía la transacción al minero a través de outofband.wizardsardine.com

Ahora vienen los últimos pasos. Para enviar la transacción al minero, solo tienes que:

- ir a [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- pegar el script de la transacción firmada copiado en el paso anterior, y luego hacer clic en "ADD TO QUEUE" debajo;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- o tomar el archivo y arrastrarlo y soltarlo en el área designada.

![Dropping the transaction file on the tool](assets/fr/16.webp)

La transacción se muestra entonces como se indica a continuación.

![Transaction in the queue](assets/fr/17.webp)

Si un mensaje te indica que se desconoce el importe total de entrada en satoshis de tu transacción (y que, en consecuencia, no se puede calcular el número de satoshis destinado a las comisiones), simplemente debes introducir manualmente el importe total de entrada en satoshis. Para encontrarlo, solo tienes que hacer clic en la visualización de tu transacción en Sparrow, en el centro del diagrama:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Luego introduce ese importe (15.904 sats en nuestro ejemplo) en la herramienta [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

Finalmente, comprueba que la tasa de comisión sea correcta.

### Paso 7: Envía la transacción mediante Slipstream

Finalmente, solo tienes que hacer clic en "Send" para que la transacción se envíe a MARA a través de Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

En cuestión de segundos, la transacción pasa de "Sending" a "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Solo queda copiar el identificador de la transacción (TXID) y pegarlo en [mempool.space](https://mempool.space/) para ver cómo se mina:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Ten en cuenta: la transacción aparecerá como "Transaction not found" hasta que el minero, MARA, mine un bloque e incluya tu transacción en él. Esto puede tardar varias decenas de minutos, o incluso horas, ya que MARA solo posee alrededor del 4,5 % del hash rate de la red Bitcoin. A fecha de 4 de agosto de 2026, esto corresponde aproximadamente a un bloque minado cada 3 horas y 45 minutos.
</content>
<parameter name="i">Write Spanish translation of Slipstream tutorial