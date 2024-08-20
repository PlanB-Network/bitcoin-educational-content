---
term: MTP (MEDIAN TIME PAST)
---

Este concepto se utiliza en el protocolo de Bitcoin para determinar un margen en el timestamp de consenso de la red. MTP se define como la mediana de los timestamps de los últimos 11 bloques minados. El uso de este indicador ayuda a evitar desacuerdos entre los nodos sobre la hora exacta en caso de discrepancias. MTP se utilizó inicialmente para verificar la validez de los timestamps de los bloques contra el pasado. Desde BIP113, también se ha utilizado como referencia para el tiempo de la red para verificar la validez de las transacciones con bloqueo de tiempo (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` y `OP_CHECKSEQUENCEVERIFY`).