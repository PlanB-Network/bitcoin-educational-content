---
term: SIGHASH_ALL/SIGHASH_ACP
---

Tipo de bandera SigHash (`0x81`) combinada con el modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilizado en firmas de transacciones de Bitcoin. Esta combinación especifica que la firma se aplica a todos los outputs y solo a un input específico de la transacción. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` permite a otros participantes agregar inputs adicionales a la transacción después de su firma inicial. Es particularmente útil en escenarios colaborativos, como transacciones de crowdfunding, donde diferentes contribuyentes pueden agregar sus propios inputs mientras se preserva la integridad de los outputs comprometidos por el firmante inicial.