---
term: MTP (MEDIANA DEL TIEMPO PASADO)

---
Este concepto se utiliza en el protocolo Bitcoin para determinar un margen sobre la marca de tiempo de consenso de la red. MTP se define como la mediana de las marcas de tiempo de los últimos 11 bloques minados. El uso de este indicador ayuda a evitar desacuerdos entre nodos sobre la hora exacta en caso de discrepancias. El MTP se utilizó inicialmente para verificar la validez de las marcas de tiempo de los bloques con respecto al pasado. Desde BIP113, también se ha utilizado como referencia de la hora de la red para verificar la validez de las transacciones de bloqueo temporal (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, y `OP_CHECKSEQUENCEVERIFY`).