---
term: SIGHASH_SINGLE (0X03)

---
Tipo de SigHash Bandera utilizada en las firmas de transacciones Bitcoin para indicar que la firma se aplica a todas las entradas de la transacción y a una sola salida, correspondiente al índice de la misma entrada firmada. Así, cada entrada firmada con `SIGHASH_SINGLE` está específicamente vinculada a una salida concreta. Las demás salidas no están comprometidas por la firma y, por tanto, pueden modificarse posteriormente. Este tipo de firma es útil en transacciones complejas, en las que los participantes desean vincular determinadas entradas a salidas específicas, dejando flexibilidad para las demás salidas de la transacción.