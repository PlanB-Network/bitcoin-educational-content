---
term: TXID (IDENTIFICADOR DE TRANSACCIÓN)
---

Un identificador único asociado con cada transacción de Bitcoin. Se genera calculando el hash `SHA256d` de los datos de la transacción. El TXID sirve como referencia para encontrar una transacción específica dentro de la blockchain. También se utiliza para referirse a un UTXO, que es esencialmente la concatenación del TXID de una transacción anterior y el índice de la salida designada (también llamado "vout"). Para las transacciones post-SegWit, el TXID ya no toma en cuenta el testigo de la transacción, lo que elimina la maleabilidad.