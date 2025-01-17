---
term: COINBASE (TRANSACCIÓN)

---
La transacción coinbase es una transacción especial y única incluida en cada bloque de la blockchain de Bitcoin. Representa la primera transacción de un bloque y es creada por el minero que ha encontrado con éxito una cabecera que valida la prueba de trabajo (*Proof-of-Work*), es decir, menor o igual que el objetivo.

La transacción coinbase sirve principalmente para dos propósitos: otorgar la recompensa del bloque al minero y añadir nuevas unidades de bitcoins a la masa monetaria en circulación. La recompensa del bloque, que es el incentivo económico para que los mineros realicen pruebas de trabajo, incluye las comisiones acumuladas por las transacciones incluidas en el bloque y una cantidad determinada de bitcoins de nueva creación ex-nihilo (subsidio del bloque). Esta cantidad, fijada inicialmente en 50 bitcoins por bloque en 2009, se reduce a la mitad cada 210.000 bloques (aproximadamente cada 4 años) durante un evento llamado "halving"

La transacción coinbase difiere de las transacciones normales en varios aspectos. En primer lugar, no tiene entrada, lo que significa que no consume ninguna salida de transacción existente (UTXO). Además, el script de firma (`scriptSig`) de la transacción coinbase suele contener un campo arbitrario que permite incorporar datos adicionales, como mensajes personalizados o información sobre la versión del software de minería. Por último, los bitcoins generados por la transacción coinbase están sujetos a un periodo de maduración de 100 bloques (101 confirmaciones) antes de que puedan gastarse, para evitar el posible gasto de bitcoins inexistentes en caso de reorganización de la cadena.

> ► *No existe traducción para "Coinbase" en francés. Por lo tanto, se acepta utilizar este término directamente.*