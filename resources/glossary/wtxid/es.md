---
term: WTXID

---
Una extensión del TXID tradicional, que incluye datos de testigos introducidos con SegWit. Mientras que el TXID es un hash de los datos de la transacción excluyendo el testigo, el WTXID es el `SHA256d` de todos los datos de la transacción, testigo incluido. Los WTXID se almacenan en un árbol Merkle separado cuya raíz se sitúa en la transacción coinbase. Esta separación permite eliminar la maleabilidad de la transacción del TXID.