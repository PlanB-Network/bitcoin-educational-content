---
term: WTXID
---

Una extensión del TXID tradicional, incluyendo datos de testigo introducidos con SegWit. Mientras que el TXID es un hash de los datos de la transacción excluyendo el testigo, el WTXID es el `SHA256d` de todos los datos de la transacción, incluido el testigo. Los WTXIDs se almacenan en un árbol de Merkle separado cuya raíz se coloca en la transacción coinbase. Esta separación permite la eliminación de la maleabilidad de la transacción del TXID.