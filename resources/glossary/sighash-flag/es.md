---
term: BANDERA SIGHASH

---
Un parámetro en una transacción Bitcoin que determina qué componentes de una transacción (entradas y salidas) están cubiertos por la firma asociada, convirtiéndose así en inmutables. El SigHash Flag es un byte que se añade a la firma digital de cada entrada. Por lo tanto, la elección del SigHash Flag afecta directamente a qué partes de la transacción quedan congeladas por la firma y cuáles pueden seguir siendo modificadas posteriormente. Este mecanismo garantiza que las firmas comprometen de forma precisa y segura los datos de la transacción de acuerdo con la intención del firmante. Existen tres banderas SigHash principales:


- `SIGHASH_ALL` (`0x01`): La firma se aplica a todas las entradas y salidas de la transacción, bloqueándolas por completo;
- `SIGHASH_NONE` (`0x02`): La firma se aplica a todas las entradas pero a ninguna de las salidas, permitiendo que las salidas se modifiquen después de la firma;
- `SIGHASH_SINGLE` (`0x03`): La firma cubre todas las entradas y sólo una salida correspondiente al índice de la entrada firmada.

Además de estas tres banderas SigHash, el modificador `SIGHASH_ANYONECANPAY` (`0x80`) puede combinarse con cada uno de los tipos anteriores. Cuando se utiliza este modificador, sólo se firma una parte de las entradas, dejando las demás abiertas a modificaciones. Estas son las combinaciones existentes con el modificador:


- sIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): La firma se aplica a una sola entrada mientras que cubre todas las salidas de la transacción;
- sIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): La firma cubre una única entrada, sin comprometer ninguna salida;
- sIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): La firma se aplica a una sola entrada y sólo a la salida que tiene el mismo índice que esta entrada.

> ► *Un sinónimo utilizado a veces para "SigHash" es "Signature Hash Types".*