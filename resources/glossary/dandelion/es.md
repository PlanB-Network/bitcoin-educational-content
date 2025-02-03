---
term: DANDELION

---
Una propuesta destinada a mejorar la privacidad del enrutamiento de transacciones en la red Bitcoin para contrarrestar la desanonimización. En el funcionamiento estándar de Bitcoin, las transacciones se difunden inmediatamente a múltiples nodos. Este fenómeno puede potencialmente permitir a los observadores vincular transacciones, normalmente anónimas, con direcciones IP. El objetivo de BIP156 es resolver este problema. Para ello, introduce una fase adicional en el proceso de difusión para preservar el anonimato antes de la propagación pública. Así, Dandelion utiliza primero una fase "stem" en la que la transacción se envía a través de una ruta aleatoria de nodos, antes de ser difundida a toda la red en la fase "fluff". El tallo y la pelusa son referencias al comportamiento de la propagación de la transacción a través de la red, asemejándose a la forma de un diente de león. Este método de enrutamiento oculta el rastro que conduce al nodo de origen, lo que dificulta el seguimiento de una transacción a través de la red hasta su origen.

![](../../dictionnaire/assets/36.webp)