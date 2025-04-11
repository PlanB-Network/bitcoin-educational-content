---
term: SIGHASH_NONE (0X02)

---
Tipo de indicador SigHash utilizado en las firmas de transacciones Bitcoin para indicar que la firma se aplica a todas las entradas de la transacción, pero a ninguna de sus salidas. El uso de `SIGHASH_NONE` implica que el firmante se compromete sólo a las entradas, permitiendo que las salidas permanezcan indeterminadas o modificables tras la firma. Este tipo de firma es útil en casos en los que el firmante desea autorizar a otras partes a decidir cómo se distribuirán los bitcoins en la transacción.