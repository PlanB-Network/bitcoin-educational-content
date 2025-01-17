---
term: COINJOIN

---
Coinjoin es una técnica utilizada para romper la trazabilidad de los bitcoins. Se basa en una transacción colaborativa con una estructura específica del mismo nombre: la transacción coinjoin. Las transacciones Coinjoin ayudan a mejorar la protección de la privacidad de los usuarios de Bitcoin al dificultar el análisis de las transacciones por parte de observadores externos. Esta estructura permite mezclar varias monedas en una misma transacción, lo que dificulta determinar los vínculos entre las direcciones de entrada y salida.

El funcionamiento general de coinjoin es el siguiente: diferentes usuarios que deseen mezclar depositan una cantidad como entrada de una transacción. Estas entradas saldrán como diferentes salidas del mismo importe. Al final de la transacción, es imposible determinar qué salida pertenece a qué usuario. Técnicamente, no existe ningún vínculo entre las entradas y las salidas de la transacción coinjoin. El vínculo entre cada usuario y cada UTXO está roto, del mismo modo que lo está el historial de cada moneda.

![](../../dictionnaire/assets/4.webp)

Para permitir la coinjoin sin que ningún usuario pierda el control sobre sus fondos en ningún momento, la transacción la construye primero un coordinador y luego se transmite a cada usuario. A continuación, cada uno firma la transacción por su parte tras verificar que le conviene, y luego todas las firmas se añaden a la transacción. Si un usuario o el coordinador intentan robar los fondos de otros modificando las salidas de la transacción coinjoin, entonces las firmas no serán válidas y la transacción será rechazada por los nodos. Cuando el registro de la salida de los participantes se realiza utilizando firmas ciegas de Chaum para evitar el vínculo con la entrada, se habla de "coinjoin chaumiano".

Este mecanismo aumenta la confidencialidad de las transacciones sin necesidad de modificar el protocolo Bitcoin. Implementaciones específicas de coinjoin, como Whirlpool, JoinMarket o Wabisabi, ofrecen soluciones para facilitar el proceso de coordinación entre los participantes y mejorar la eficiencia de la transacción coinjoin. He aquí un ejemplo de transacción coinjoin:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Es difícil determinar con certeza quién introdujo por primera vez la idea de coinjoin en Bitcoin, y quién tuvo la idea de utilizar las firmas ciegas de David Chaum en este contexto. A menudo se piensa que Gregory Maxwell fue el primero en discutirlo en [un mensaje en BitcoinTalk en 2013](https://bitcointalk.org/index.php?topic=279249.0):

Utilizando firmas ciegas Chaum: Los usuarios se conectan y proporcionan entradas (y cambian de dirección), así como una versión criptográficamente enmascarada de la dirección a la que desean enviar sus monedas privadas; el servidor firma las fichas y las devuelve. Los usuarios vuelven a conectarse de forma anónima, desenmascaran sus direcciones de salida y las envían de nuevo al servidor. El servidor puede ver que todas las salidas han sido firmadas por él y que, en consecuencia, todas las salidas proceden de participantes válidos. Más tarde, las personas vuelven a conectarse y a firmar.

Maxwell, G. (2013, 22 de agosto). *CoinJoin: Privacidad Bitcoin para el mundo real*. Foro BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0

Sin embargo, hay menciones anteriores, tanto para firmas Chaum en el contexto de la mezcla, como para coinjoins. [En junio de 2011, Duncan Townsend presenta en BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) un mezclador que utiliza firmas Chaum de forma bastante similar a los modernos coinjoins chaumianos. En el mismo hilo, hay [un mensaje de hashcoin en respuesta a Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) para mejorar su mezclador. Este mensaje presenta lo que más se parece a los coinjoins. También hay una mención a un sistema similar en [un mensaje de Alex Mizrahi en 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), mientras asesoraba a los creadores de Tenebrix. El término "coinjoin" en sí no fue inventado por Greg Maxwell, sino que procede de una idea de Peter Todd.

> ► *El término "coinjoin" no tiene traducción al francés. Algunos bitcoiners utilizan también los términos "mix", "mixing" o "mixage" para referirse a la transacción coinjoin. La mezcla es más bien el proceso utilizado en el corazón de la coinjoin. Además, es importante no confundir la mezcla a través de coinjoins con la mezcla a través de un actor central que toma posesión de los bitcoins durante el proceso. Esto no tiene nada que ver con el coinjoin, en el que el usuario no pierde el control de sus bitcoins durante el proceso.*