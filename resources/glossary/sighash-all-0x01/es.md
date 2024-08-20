---
term: SIGHASH_ALL (0X01)
---

Tipo de bandera SigHash utilizada en las firmas de transacciones de Bitcoin para indicar que la firma se aplica a todos los componentes de la transacción. Al usar `SIGHASH_ALL`, el firmante cubre todas las entradas y todas las salidas. Esto significa que ni las entradas ni las salidas pueden ser modificadas después de la firma sin invalidarla. Este tipo de bandera SigHash es el más común en las transacciones de Bitcoin, ya que asegura la finalidad completa y la integridad de la transacción.