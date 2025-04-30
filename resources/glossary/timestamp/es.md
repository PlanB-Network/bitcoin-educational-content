---
term: HORODATAJE
---

El sellado de tiempo, o "Timestamp" en inglés, es un mecanismo para asociar una marca temporal precisa a un evento, dato o mensaje. En el contexto general de los sistemas informáticos, el sellado de tiempo se utiliza para determinar el orden cronológico de las operaciones y verificar la integridad de los datos a lo largo del tiempo.


En el caso concreto de Bitcoin, las marcas de tiempo se utilizan para establecer la cronología de las transacciones y los bloques. Cada bloque en Blockchain contiene una Timestamp que indica la hora aproximada de su creación. Satoshi Nakamoto habla incluso de un "servidor Timestamp", en su Libro Blanco, para describir lo que hoy llamaríamos "Blockchain". La función del sellado de tiempo en Bitcoin es determinar la cronología de las transacciones, de modo que, sin la intervención de una autoridad central, se pueda determinar qué transacción llegó primero. Este mecanismo permite a cada usuario verificar la inexistencia de una transacción en el pasado, y evitar así que un usuario malintencionado realice un doble gasto. Este mecanismo lo justifica Satoshi Nakamoto en su Libro Blanco con la famosa frase "*Esta norma se basa en el tiempo Unix, que representa el número total de segundos transcurridos desde el 1 de enero de 1970.


> ► *Las marcas de tiempo de los bloques son relativamente flexibles en Bitcoin, ya que para que un Timestamp se considere válido basta con que sea mayor que la mediana del tiempo de los 11 bloques que le preceden (MTP) y menor que la mediana de los tiempos devueltos por los nodos (tiempo ajustado a la red) más 2 horas.*