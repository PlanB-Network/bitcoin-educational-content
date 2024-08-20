---
term: MEMPOOL
---

Una contracción de los términos "memory" (memoria) y "pool" (conjunto). Esto se refiere a un espacio virtual en el cual las transacciones de Bitcoin que esperan ser incluidas en un bloque se agrupan. Cuando una transacción es creada y transmitida en la red de Bitcoin, primero es verificada por los nodos de la red. Si se considera válida, entonces se coloca en el Mempool de cada nodo, donde permanece hasta que es seleccionada por un minero para ser incluida en un bloque.

Es importante notar que cada nodo en la red de Bitcoin mantiene su propio Mempool, y por lo tanto, puede haber variaciones en el contenido del Mempool entre diferentes nodos en cualquier momento dado. Notablemente, el parámetro `maxmempool` en el archivo `bitcoin.conf` de cada nodo permite a los operadores controlar la cantidad de RAM (memoria de acceso aleatorio) que su nodo utilizará para almacenar transacciones pendientes en el Mempool. Al limitar el tamaño del Mempool, los operadores de nodos pueden prevenir que consuma demasiados recursos en su sistema. Este parámetro se especifica en megabytes (MB). El valor predeterminado para Bitcoin Core hasta la fecha es 300 MB.

Las transacciones presentes en el Mempool son provisionales. No deben considerarse inmutables hasta que sean incluidas en un bloque, y después de un cierto número de confirmaciones. Estas a menudo pueden ser reemplazadas o purgadas.