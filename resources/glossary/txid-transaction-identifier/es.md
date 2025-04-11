---
term: TXID (IDENTIFICADOR DE TRANSACCIÓN)

---
Un identificador único asociado a cada transacción Bitcoin. Se genera calculando el hash `SHA256d` de los datos de la transacción. El TXID sirve como referencia para encontrar una transacción específica dentro de la cadena de bloques. También se utiliza para referirse a un UTXO, que es esencialmente la concatenación del TXID de una transacción anterior y el índice de la salida designada (también llamada "vout"). Para las transacciones posteriores a SegWit, el TXID ya no tiene en cuenta el testigo de la transacción, lo que elimina la maleabilidad.