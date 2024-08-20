---
term: SIGHASH FLAG
---

Un parámetro en una transacción de Bitcoin que determina qué componentes de una transacción (entradas y salidas) están cubiertos por la firma asociada, volviéndolos inmutables. El SIGHASH FLAG es un byte añadido a la firma digital de cada entrada. Por lo tanto, la elección del SIGHASH FLAG afecta directamente qué partes de la transacción son congeladas por la firma y cuáles pueden ser modificadas posteriormente. Este mecanismo asegura que las firmas comprometan los datos de la transacción de manera precisa y segura según la intención del firmante. Hay tres principales SIGHASH FLAGS:

- `SIGHASH_ALL` (`0x01`): La firma se aplica a todas las entradas y salidas de la transacción, bloqueándolas completamente;

- `SIGHASH_NONE` (`0x02`): La firma se aplica a todas las entradas pero a ninguna de las salidas, permitiendo que las salidas sean modificadas después de la firma;

- `SIGHASH_SINGLE` (`0x03`): La firma cubre todas las entradas y solo una salida correspondiente al índice de la entrada firmada.

Además de estos tres SIGHASH FLAGS, el modificador `SIGHASH_ANYONECANPAY` (`0x80`) puede combinarse con cada uno de los tipos anteriores. Cuando se usa este modificador, solo se firma una porción de las entradas, dejando las otras abiertas a modificación. Aquí están las combinaciones existentes con el modificador:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): La firma se aplica a una sola entrada mientras cubre todas las salidas de la transacción;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): La firma cubre una sola entrada, sin comprometerse con ninguna salida;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): La firma se aplica a una sola entrada y solo a la salida que tiene el mismo índice que esta entrada.

> ► *Un sinónimo que a veces se usa para "SigHash" es "Tipos de Hash de Firma".*