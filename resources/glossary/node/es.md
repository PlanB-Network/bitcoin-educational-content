---
term: NODO

---
En la red Bitcoin, un nodo (o "node" en inglés) es un ordenador que ejecuta un cliente del protocolo Bitcoin (como Bitcoin Core, por ejemplo). Participa en la red manteniendo una copia de la cadena de bloques, retransmitiendo y verificando transacciones y nuevos bloques y, opcionalmente, participando en el proceso de minería. La suma de todos los nodos Bitcoin representa la propia red Bitcoin.

Existen varios tipos de nodos en Bitcoin, incluidos los nodos completos y los nodos ligeros. Los nodos completos guardan una copia completa de la cadena de bloques, verifican todas las transacciones y bloques de acuerdo con las reglas de consenso, y participan activamente en la difusión de transacciones y bloques por la red. Por otro lado, los nodos ligeros, o nodos SPV (*Simple Payment Verification*), sólo guardan las cabeceras de los bloques y dependen de los nodos completos para obtener información sobre las transacciones.

> ► *Algunos también diferencian entre los llamados "nodos podados" ("pruned node" en inglés). Se trata de nodos completos, que descargan y verifican todos los bloques desde el bloque Génesis, pero solo mantienen en memoria los bloques más recientes.*