---
term: SIGHASH_NONE (0X02)
---

Tipo de bandera SigHash utilizada en las firmas de transacciones de Bitcoin para indicar que la firma se aplica a todas las entradas de la transacción, pero a ninguna de sus salidas. El uso de `SIGHASH_NONE` implica que el firmante se compromete solo con las entradas, permitiendo que las salidas permanezcan indeterminadas o modificables después de firmar. Este tipo de firma es útil en casos donde el firmante desea autorizar a otras partes a decidir cómo se distribuirán los bitcoins en la transacción.