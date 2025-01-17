---
term: SIGHASH_SINGLE/SIGHASH_ACP

---
Tipo de indicador SigHash (`0x83`) combinado con el modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilizado en firmas de transacciones Bitcoin. Esta combinación especifica que la firma sólo se aplica a una única entrada específica y sólo a la salida que tenga el mismo índice que esta entrada. Otras entradas y salidas pueden ser añadidas o modificadas por otras partes. Esta configuración es útil para transacciones colaborativas en las que los participantes pueden añadir sus propias entradas para financiar una salida específica.