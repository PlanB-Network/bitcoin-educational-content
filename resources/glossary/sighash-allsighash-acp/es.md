---
term: SIGHASH_ALL/SIGHASH_ACP

---
Tipo de indicador SigHash (`0x81`) combinado con el modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilizado en las firmas de transacciones Bitcoin. Esta combinación especifica que la firma se aplica a todas las salidas y sólo a una entrada específica de la transacción. sIGHASH_ALL | SIGHASH_ANYONECANPAY` permite a otros participantes añadir entradas adicionales a la transacción después de su firma inicial. Resulta especialmente útil en situaciones de colaboración, como las transacciones de crowdfunding, en las que distintos contribuyentes pueden añadir sus propias entradas preservando la integridad de las salidas comprometidas por el firmante inicial.