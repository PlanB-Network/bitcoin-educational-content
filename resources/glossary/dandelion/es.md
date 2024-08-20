---
term: DANDELION
---

Una propuesta destinada a mejorar la privacidad del enrutamiento de transacciones en la red de Bitcoin para contrarrestar la desanonimización. En la operación estándar de Bitcoin, las transacciones se transmiten inmediatamente a múltiples nodos. Este fenómeno puede permitir potencialmente que los observadores vinculen transacciones, normalmente anónimas, con direcciones IP. El objetivo de BIP156 es abordar este problema. Para hacerlo, introduce una fase adicional en el proceso de difusión para preservar el anonimato antes de la propagación pública. Así, Dandelion primero utiliza una fase de "tallo" donde la transacción se envía a través de un camino aleatorio de nodos, antes de ser transmitida a toda la red en la fase de "pelusa". El tallo y la pelusa son referencias al comportamiento de la propagación de la transacción a través de la red, asemejándose a la forma de un diente de león. Este método de enrutamiento oscurece el rastro que lleva de vuelta al nodo de origen, dificultando rastrear una transacción a través de la red hasta su origen.

![](../../dictionnaire/assets/36.png)