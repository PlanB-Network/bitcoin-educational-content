---
term: ATAQUE DE REPETICIÓN
---

En el contexto de Bitcoin, se produce un ataque de repetición cuando una transacción válida en un Blockchain se reproduce maliciosamente en otro Blockchain que tiene el mismo historial de transacciones. En otras palabras, una transacción difundida en un canal puede reproducirse en otro sin el consentimiento del remitente de la primera transacción.


Tomemos el ejemplo de una hipotética Hard Fork de Bitcoin, llamada "*BitcoinBis*". Si realizas un pago en bitcoins para comprar una baguette a un panadero en la Blockchain Bitcoin real, ese mismo panadero podría reproducir esa transacción legítima en *BitcoinBis* para obtener la misma cantidad en criptomonedas en esta Fork, sin ninguna acción por tu parte.


Este tipo de ataque sólo puede producirse en el caso de ramificación Blockchain con 2 cadenas independientes que persistan en el tiempo. Típicamente, este sería el caso de Hard Fork. Para que un ataque de repetición sea posible, las 2 blockchains deben tener una historia común, y la transacción duplicada debe consumir como entradas UTXOs creados a partir de transacciones anteriores que tuvieron lugar antes de que las dos cadenas se dividieran, o a partir de transacciones anteriores que a su vez ya han sido reproducidas en un ataque de repetición anterior.


En general, en informática, un ataque de repetición consiste en interceptar y reutilizar datos válidos para engañar a un sistema repitiendo la transmisión original. Esto puede conducir a veces a una usurpación de identidad en una red.


> ► *En el caso de un ataque de repetición contra una transacción Bitcoin, a veces se denomina simplemente "transacción de repetición. "*