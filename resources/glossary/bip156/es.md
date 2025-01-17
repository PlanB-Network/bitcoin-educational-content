---
term: BIP156

---
Propuesta, conocida como Dandelion, que pretende mejorar la privacidad del enrutamiento de transacciones en la red Bitcoin para contrarrestar la desanonimización. En el funcionamiento estándar de Bitcoin, las transacciones se transmiten inmediatamente a múltiples nodos. Si un observador es capaz de ver cada transacción retransmitida por cada nodo de la red, podría asumir que el primer nodo en enviar una transacción es también el nodo de origen de esa transacción, y por tanto que proviene del operador del nodo. Este fenómeno podría permitir a los observadores vincular transacciones, normalmente anónimas, con direcciones IP.

El objetivo de BIP156 es resolver este problema. Para ello, introduce una fase adicional en la difusión para preservar el anonimato antes de la propagación pública. Así, Dandelion utiliza primero una fase "stem" en la que la transacción se envía a través de una ruta aleatoria de nodos, antes de ser difundida a toda la red en la fase "fluff". El tallo y la pelusa son referencias al comportamiento de la propagación de la transacción a través de la red, asemejándose a la forma de un diente de león (*a dandelion* en inglés).

Este método de enrutamiento oculta el rastro que conduce al nodo de origen, lo que dificulta el seguimiento de una transacción a través de la red hasta su origen. Dandelion mejora así la privacidad al limitar la capacidad de los adversarios para desanonimizar la red. Este método es aún más eficaz cuando la transacción atraviesa durante la fase "tallo" un nodo que encripta sus comunicaciones de red, como con Tor o *P2P Transport V2*. BIP156 aún no ha sido añadido a Bitcoin Core.

![](../../dictionnaire/assets/36.webp)