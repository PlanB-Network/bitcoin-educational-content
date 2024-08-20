---
term: BIP156
---

Propuesta, conocida como Dandelion, que tiene como objetivo mejorar la privacidad del enrutamiento de transacciones en la red de Bitcoin para contrarrestar la desanonimización. En la operación estándar de Bitcoin, las transacciones se transmiten inmediatamente a múltiples nodos. Si un observador puede ver cada transacción retransmitida por cada nodo en la red, podría asumir que el primer nodo en enviar una transacción es también el nodo originario de esa transacción, y por lo tanto, que proviene del operador del nodo. Este fenómeno podría permitir potencialmente a los observadores vincular transacciones, normalmente anónimas, con direcciones IP.

El objetivo de BIP156 es abordar este problema. Para hacerlo, introduce una fase adicional en la transmisión para preservar el anonimato antes de la propagación pública. Así, Dandelion primero utiliza una fase de "stem" (tallo) donde la transacción se envía a través de un camino aleatorio de nodos, antes de ser transmitida a toda la red en la fase de "fluff" (pelusa). El tallo y la pelusa son referencias al comportamiento de la propagación de la transacción a través de la red, asemejándose a la forma de un diente de león (*dandelion* en inglés).

Este método de enrutamiento oscurece el rastro que lleva de vuelta al nodo fuente, haciendo difícil rastrear una transacción a través de la red hasta su origen. Dandelion mejora así la privacidad limitando la capacidad de los adversarios para desanonimizar la red. Este método es aún más efectivo cuando la transacción cruza durante la fase de "stem" un nodo que cifra sus comunicaciones de red, como con Tor o *P2P Transport V2*. BIP156 aún no ha sido añadido a Bitcoin Core.

![](../../dictionnaire/assets/36.png)