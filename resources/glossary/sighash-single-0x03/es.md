---
term: SIGHASH_SINGLE (0X03)
---

Tipo de bandera SigHash utilizada en las firmas de transacciones de Bitcoin para indicar que la firma se aplica a todas las entradas de la transacción y solo a una salida, correspondiente al índice de la misma entrada firmada. Así, cada entrada firmada con `SIGHASH_SINGLE` está específicamente vinculada a una salida particular. Las otras salidas no están comprometidas por la firma y, por lo tanto, pueden ser modificadas más tarde. Este tipo de firma es útil en transacciones complejas, donde los participantes quieren vincular ciertas entradas a salidas específicas, mientras dejan flexibilidad para las otras salidas de la transacción.