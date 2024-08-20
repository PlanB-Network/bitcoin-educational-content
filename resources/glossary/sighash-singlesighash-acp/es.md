---
term: SIGHASH_SINGLE/SIGHASH_ACP
---

Tipo de bandera SigHash (`0x83`) combinada con el modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilizado en firmas de transacciones de Bitcoin. Esta combinación especifica que la firma se aplica solo a una entrada específica y solo al output que tiene el mismo índice que esta entrada. Otras entradas y outputs pueden ser añadidos o modificados por otras partes. Esta configuración es útil para transacciones colaborativas donde los participantes pueden añadir sus propias entradas para financiar un output específico.