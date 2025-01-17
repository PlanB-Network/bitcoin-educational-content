---
term: SIGHASH_ALL (0X01)

---
Tipo de SigHash Bandera utilizada en las firmas de transacciones Bitcoin para indicar que la firma se aplica a todos los componentes de la transacción. Usando `SIGHASH_ALL`, el firmante cubre todas las entradas y todas las salidas. Esto significa que ni las entradas ni las salidas pueden ser modificadas después de la firma sin invalidarla. Este tipo de SigHash Flag es el más común en las transacciones Bitcoin, ya que asegura la completa finalidad e integridad de la transacción.