---
term: ERLAY
---

Protocolo de red propuesto para mejorar la eficacia de la retransmisión de transacciones no confirmadas entre nodos Bitcoin.


Actualmente, cada transacción se propaga mediante un sistema en el que cada nodo difunde la transacción de la que tiene conocimiento a todos sus pares. El problema es que esto genera mucha redundancia y uso de ancho de banda por duplicado. Muchas transmisiones de transacciones son innecesarias, ya que el destinatario ya conoce estas transacciones, y cada nodo sólo necesita conocer cada transacción una vez. Erlay propone limitar por defecto a 8 el número de pares a los que un nodo envía directamente transacciones de las que tiene conocimiento, y luego utilizar un proceso de reconciliación basado en la biblioteca minisketch para compartir las transacciones que faltan de forma más eficiente.


Erlay reduciría el consumo de ancho de banda en torno a un 40%, lo que haría más accesible el funcionamiento de Full node a usuarios con conexiones limitadas a Internet y fomentaría así una mejor descentralización de la red. Este protocolo también mantendría casi constante el consumo de ancho de banda a medida que aumenta el número de conexiones. Esto significa que sería mucho más sencillo para los operadores de nodos aceptar un número muy elevado de conexiones de sus pares, lo que aumentaría la seguridad de la red Bitcoin al reducir el riesgo de partición, ya sea intencionada o accidental. Además, Erlay haría más difícil determinar el nodo de origen de una transacción, aumentando así la confidencialidad para los usuarios de nodos que no operan bajo Tor.


Erlay se propone en BIP330.