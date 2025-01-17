---
term: MEMPOOL

---
Contracción de los términos "memoria" y "pool". Se refiere a un espacio virtual en el que se agrupan las transacciones de Bitcoin que esperan ser incluidas en un bloque. Cuando se crea una transacción y se difunde en la red Bitcoin, primero es verificada por los nodos de la red. Si se considera válida, se coloca en el Mempool de cada nodo, donde permanece hasta que es seleccionada por un minero para ser incluida en un bloque.

Es importante señalar que cada nodo de la red Bitcoin mantiene su propia Mempool, y por lo tanto, puede haber variaciones en el contenido de la Mempool entre diferentes nodos en un momento dado. En particular, el parámetro `maxmempool` en el archivo `bitcoin.conf` de cada nodo permite a los operadores controlar la cantidad de RAM (memoria de acceso aleatorio) que su nodo utilizará para almacenar transacciones pendientes en el Mempool. Limitando el tamaño del Mempool, los operadores del nodo pueden evitar que consuma demasiados recursos de su sistema. Este parámetro se especifica en megabytes (MB). El valor por defecto para Bitcoin Core hasta la fecha es de 300 MB.

Las transacciones presentes en el Mempool son provisionales. No deben considerarse inmutables hasta que se incluyan en un bloque, y después de un cierto número de confirmaciones. A menudo pueden sustituirse o purgarse.