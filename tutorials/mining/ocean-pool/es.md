---
name: Ocean Mining

description: Introducción a la Minería Oceánica
---

![signup](assets/cover.webp)

**Mayo 2024**

Ocean Mining es un pool de minería algo único. Aquí, no se requieren cuentas, direcciones de correo electrónico, ni contraseñas. Al igual que Bitcoin, todo es transparente, pseudónimo, y los contribuyentes pueden elegir entre cuatro diferentes plantillas de bloque.

### Sistema de Compensación

El sistema de compensación de Ocean se llama TIDES, "Índice Transparente de Shares Extendidos Distintos". Este sistema registra el trabajo proporcionado por los mineros, conocido como "shares". El pool calcula el porcentaje de "shares" para cada contribuyente, luego agrega su dirección de Bitcoin en la plantilla del bloque del pool como el beneficiario de este porcentaje de la recompensa del bloque.

La plantilla del bloque se actualiza aproximadamente cada 10 segundos para tener en cuenta las nuevas transacciones más lucrativas y para cambiar la distribución de la recompensa del bloque si es necesario.

![signup](assets/rem.webp)

No importa si tus máquinas están conectadas o no en el momento en que el pool mina un nuevo bloque. El trabajo ya enviado se guarda para los próximos ocho bloques encontrados por el pool.

Mantener el trabajo para ocho bloques en lugar de restablecer los contadores a cero con cada nuevo bloque minado significa que tu compensación solo será del 100% una vez que el pool haya encontrado ocho bloques después de que comenzaste a contribuir. Esto también significa que continuarás siendo compensado por ocho bloques si dejas de contribuir al pool.

Este mecanismo suaviza la compensación y desalienta el "pool hopping", que implica cambiar de pools regularmente dependiendo de cuál es más probable que encuentre el próximo bloque.

### Retiros

La operación de Ocean Mining permite a sus contribuyentes recuperar bitcoins "limpios", es decir, bitcoins que son emitidos directamente por la recompensa del bloque.

A diferencia de la mayoría de los otros pools, Ocean no recibe los bitcoins recién minados; las direcciones de los contribuyentes se integran directamente en la plantilla del bloque.

Por ahora, la cantidad mínima para beneficiarse verdaderamente de los bitcoins limpios es de 1,048,576 sats. Con cada bloque minado por el pool, tu parte de "shares" debe otorgarte más de 1,048,576 sats para que sean pagados directamente a ti por la recompensa del bloque.
De lo contrario, tus sats serán guardados por Ocean hasta que tus recompensas totales excedan esta cantidad.

Todos los bitcoins temporalmente guardados por Ocean están en esta dirección: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, todo es verificable en la TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
También es posible retirar tus sats a través de Lightning usando BOLT12. Veremos cómo configurar esto.

### Tarifas del Pool

Las tarifas varían del 0% al 2% dependiendo de la plantilla de bloque elegida.

## La Transparencia de Ocean

### Datos de los Contribuyentes

![signup](assets/1.webp)

Toda la información sobre el pool es transparente, incluyendo todos los datos de los usuarios. Para entender este punto, tomemos un ejemplo:

[En el tablero de Ocean](https://ocean.xyz/dashboard), tienes numerosas piezas de información como el hashrate de los últimos seis meses, el número de participantes en el pool, el número total de bitcoins minados, etc.

Nos centraremos en la sección "Contribuyentes". Puedes ver la lista de todos los contribuyentes con su hashrate promedio de las últimas tres horas, así como el porcentaje de **"shares"** y **"hash"** relativo al resto del pool.
**"Porcentaje de Acciones"** es el porcentaje de trabajo proporcionado por el colaborador en la ventana de los últimos ocho bloques comparado con el resto del pool.
**"Porcentaje de Hash"** es el porcentaje del hashrate promedio proporcionado por el colaborador durante las últimas tres horas comparado con el resto del pool.

![signup](assets/2.webp)

Notarás que los "Colaboradores" son identificados por una dirección de Bitcoin. Puedes hacer clic en cualquiera de estas direcciones para más detalles.

Si tomamos la primera, la que tiene el hashrate más alto [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), puedes ver todos los detalles sobre este usuario: hashrate, número de bitcoins minados, con qué bloque, e incluso los detalles de cada una de sus máquinas (ASICs). Sin embargo, permanecen anónimos, como en Bitcoin.

### Plantilla de Bloque

En la parte superior izquierda del tablero, tienes "Siguiente bloque". En esta página, hay cuatro diferentes plantillas de bloque. Ocean permite a cada colaborador elegir la plantilla de bloque que deseen apoyar. Esto no tiene un impacto directo en tu compensación. Cuando el pool mina un bloque, todos los colaboradores son compensados independientemente de la plantilla que hayan elegido. Esto simplemente permite a todos "votar" por la plantilla de bloque que les convenga.

![signup](assets/3.webp)

**CORE:** Tarifa 2%, esta es la plantilla clásica de Bitcoin Core sin filtro, como se indica en su página "Incluye transacciones y la mayoría del spam"

**CORE+ANTISPAM:** Tarifa 0%, Bitcoin Core con un filtro contra ciertas transacciones como Ordinals "Incluye transacciones y limita el spam"

**OCEAN:** Tarifa 0%, Bitcoin Knot "Incluye solo transacciones y datos razonablemente pequeños"

**DATA-FREE:** Tarifa 0%, Bitcoin Knot "Incluye solo transacciones sin ningún dato arbitrario"

### Distinción entre Bitcoin Core y Bitcoin Knot
Bitcoin Core es el software que permite operar a aproximadamente el 99% de los nodos de Bitcoin alrededor del mundo. Bitcoin es un protocolo, lo que significa que, al igual que Internet, donde hay múltiples navegadores, pueden coexistir varios programas de software diferentes en la misma TimeChain. Sin embargo, por preocupaciones de compatibilidad y para limitar el riesgo de bugs que dejarían huellas indelebles en la TimeChain, casi todos los desarrolladores de Bitcoin trabajan en Bitcoin Core. Bitcoin Knots es un fork de Bitcoin Core, lo que significa que comparte la mayoría de su código, limitando enormemente el riesgo de bugs. Este fork fue creado por Luke Dashjr, quien quería aplicar reglas más restrictivas que Bitcoin Core sin crear un hard fork. Ahora, Bitcoin Core y Bitcoin Knots coexisten gracias al consenso de Nakamoto.

## Agregando un Trabajador

Para agregar un trabajador, comienza eligiendo tu plantilla de bloque. Esta elección determinará la URL del pool para ingresar en tu minero (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

A continuación, para el campo de usuario, ingresa una dirección de Bitcoin que poseas. Aquí está la lista de tipos de direcciones compatibles:
- **P2PKH** (Tipo de dirección original. Comienza con “1”)
- **P2SH** (Multisignatura o P2SH-Segwit. Comienza con “3”)
- **Bech32** (Segwit. Comienza con “bc”.)
- **Bech32m** (Taproot. Comienza con “bc”. Más largo que Bech32.)

Si tienes varios mineros, puedes ingresar la misma dirección para todos ellos para que sus tasas de hash se combinen y aparezcan como un solo minero. También puedes distinguirlos agregando un nombre distinto a cada uno. Para hacer esto, simplemente agrega “.nombreDelTrabajador” después de la dirección de Bitcoin.

Finalmente, para el campo de contraseña, usa `x`.

**Ejemplo:**
Si eliges la plantilla **OCEAN**, tu dirección de Bitcoin es `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` y deseas nombrar a tu minero “Brrrr”, entonces necesitarás ingresar la siguiente información en la interfaz de tu minero:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **USUARIO**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **CONTRASEÑA**: `x`

Unos minutos después de comenzar a minar, podrás ver tus datos en el sitio de Ocean buscando por tu dirección.

### Visión General del Tablero
- **Participaciones en la Ventana de Recompensa**: Estos datos indican el número de participaciones, el trabajo que has enviado al pool en la ventana de los últimos 8 bloques minados por el pool.
- **Recompensas Estimadas en Ventanas**: Estimación del número de sats que ganarás con el trabajo ya realizado. Esto no tiene en cuenta las tarifas de transacción, sino solo el coinbase, los nuevos bitcoins emitidos por la red.
- **Ganancias Estimadas Próximo Bloque**: Estimación del número de sats ganados si un bloque se mina ahora. Recuerda, si este valor es menor a 1,048,576 sats, no recibirás directamente los sats a tu dirección. Serán enviados a la dirección de Ocean hasta que tus ganancias superen este umbral.

A continuación, tienes un gráfico que muestra tu historial de tasa de hash hasta 6 meses.

![signup](assets/4.webp)

Aquí, tienes tu tasa de hash promedio en diferentes escalas de tiempo, desde 60s hasta 24h, así como la historia de bloques minados por el pool para los cuales has contribuido y sido recompensado.

![signup](assets/5.webp)

Tienes la opción de exportar un archivo CSV de este historial con el botón **Descargar CSV**.

![signup](assets/6.webp)

En la siguiente sección, tienes una lista de todos los mineros que has conectado al pool con esta dirección. Tienes, por supuesto, su tasa de hash individual, pero también el número de sats que han recibido individualmente por su trabajo.

![signup](assets/7.webp)

Puedes hacer clic en el **Apodo** de cualquier minero. Entonces tendrás toda la información que acabamos de ver, pero específicamente para ese minero.

Y al final de la página, alguna información adicional donde puedes ver el historial de pagos en tu dirección, los sats que has minado pero aún no se han pagado, y el total de sats que has minado.

![signup](assets/8.webp)

Aquí, puedes ver que en el cuadro **Tiempo Estimado Hasta el Pago Mínimo**, está escrito Lightning porque hemos configurado una oferta BOLT12.

### Configurando Retiros Lightning
Como has entendido, Ocean tiene como objetivo maximizar la transparencia y minimizar la custodia (mantener tus sats en tu nombre). Por eso, para los retiros Lightning, es necesario utilizar **ofertas BOLT12**. Esta es una nueva forma de realizar un pago en la red Lightning que está empezando a surgir en 2024 y permite varias cosas:
- Es un enlace de pago reutilizable, que permite pagos automáticos y, a diferencia de una dirección Lightning, el BOLT12 no es custodial.
- También es un método de pago que proporciona prueba de que el pago se realizó, lo cual no ocurre con los LNURLs.
- Muy importante, se puede usar junto con una firma de Bitcoin para probar que eres tanto el titular de la dirección BTC como de la oferta BOLT12.
A partir de hoy (mayo de 2024), existen pocas soluciones para usar este método. En este ejemplo, utilizaremos un servidor Start9 con Core Lightning. Cuando otras herramientas, como Phoenix Wallet por ejemplo, hayan integrado ofertas BOLT12, este tutorial seguirá siendo aplicable. Asegúrate de tener canales abiertos con liquidez entrante, de lo contrario, los pagos no funcionarán.

Comienza yendo a tu panel de control en el sitio de Ocean ingresando tu dirección BTC, luego haz clic en la pestaña **Configuration**.

![signup](assets/9.webp)

Copiaremos el texto de **Description**, aquí:
`OCEAN Payouts for bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Ahora ve a tu interfaz de Core Lightning en tu servidor Start9 (o cualquier billetera capaz de proporcionar una oferta BOLT12).

![signup](assets/10.webp)

Haz clic en **Receive**.

Marca **Offer**, luego pega el texto copiado anteriormente en el campo **Description** y deja el campo **Amount** vacío.

![signup](assets/11.webp)

Haz clic en **Generate Offer**.

![signup](assets/12.webp)

Has generado un enlace de pago reutilizable y permanente que no requiere un servidor central como es el caso con las direcciones Lightning. Copia el enlace y luego regresa a la página de Ocean.

En el campo **Lightning BOLT12 Offer**, pega el enlace de pago y deja el campo **Block Height** en su valor predeterminado. Haz clic en **GENERATE**.

![signup](assets/13.webp)

Para que Ocean asegure que este enlace de pago es realmente tuyo sin usar un sistema de cuentas, necesitarás firmar el mensaje que acaba de generarse con tu clave privada correspondiente a la dirección de Bitcoin que estás utilizando. Existen muchas soluciones para firmar un mensaje con tu clave privada. En este tutorial, tomaremos el ejemplo de BlueWallet, pero el método es el mismo para todas las billeteras.

![signup](assets/14.webp)

Suponiendo que tu clave privada esté en BlueWallet (puedes hacer lo mismo con una billetera de hardware), haz clic en la billetera concernida.

![signup](assets/15.webp)

Luego en el **…** en la parte superior derecha.

![signup](assets/15bis.webp)

Y **Sign/Verify Message**.

![signup](assets/16.webp)

En esta ventana, tienes tres campos: **Address**, **Signature** y **Message**.

En el campo **Address**, ingresa tu dirección de Bitcoin. Si volvemos a nuestro ejemplo, es la dirección: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Deja el campo **Signature** vacío.
Y pega el mensaje generado en el campo **Mensaje** en la página de Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Haz clic en **Sign**.

Esto generará una firma criptográfica que demuestra que eres el propietario de la dirección `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, y esta firma es única gracias al mensaje proporcionado por Ocean, generado a partir del enlace de pago BOLT12.

![signup](assets/17.webp)

Copia la firma y pégala en la página de Ocean, luego haz clic en **CONFIRM**.

![signup](assets/18.webp)

Deberías ver un mensaje de confirmación.

![signup](assets/19.webp)

Ahora ve a la pestaña **My Stats**. Se muestra información adicional en la parte superior con el enlace de pago BOLT12 que previamente generaste con Core Lightning en Start9.

![signup](assets/20.webp)