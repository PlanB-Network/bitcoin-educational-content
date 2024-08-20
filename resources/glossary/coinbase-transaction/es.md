---
term: COINBASE (TRANSACTION)
---

La transacción coinbase es una transacción especial y única incluida en cada bloque de la cadena de bloques de Bitcoin. Representa la primera transacción de un bloque y es creada por el minero que ha encontrado exitosamente un encabezado que valida la prueba de trabajo (*Proof-of-Work*), es decir, que es menor o igual al objetivo.

La transacción coinbase tiene principalmente dos propósitos: otorgar la recompensa del bloque al minero y añadir nuevas unidades de bitcoins al suministro de dinero circulante. La recompensa del bloque, que es el incentivo económico para que los mineros participen en la prueba de trabajo, incluye las tarifas acumuladas por las transacciones incluidas en el bloque y una cantidad determinada de bitcoins recién creados ex-nihilo (subsidio del bloque). Esta cantidad, inicialmente establecida en 50 bitcoins por bloque en 2009, se reduce a la mitad cada 210,000 bloques (aproximadamente cada 4 años) durante un evento llamado "halving".

La transacción coinbase difiere de las transacciones regulares en varias maneras. Primero, no tiene una entrada, lo que significa que no se consume ningún output de transacción existente (UTXO) por ella. A continuación, el script de firma (`scriptSig`) para la transacción coinbase típicamente contiene un campo arbitrario que permite la incorporación de datos adicionales, como mensajes personalizados o información de la versión del software de minería. Finalmente, los bitcoins generados por la transacción coinbase están sujetos a un período de madurez de 100 bloques (101 confirmaciones) antes de que puedan ser gastados, para prevenir el gasto potencial de bitcoins no existentes en caso de una reorganización de la cadena.

> ► *No hay traducción para "Coinbase" en español. Por lo tanto, se acepta usar este término directamente.*