---
term: EXTRA-Nonce
---

Campo utilizado en el `scriptSig` del Coinbase Transaction de un bloque, que permite probar un mayor número de posibilidades para tener un Hash inferior al objetivo de dificultad, además del clásico Nonce, que se encuentra directamente en la cabecera de cada bloque.


La modificación del Nonce extra en el Coinbase Transaction cambia el identificador de esta transacción, y por tanto el Merkle Root de todas las transacciones del bloque, lo que también modifica la cabecera del bloque. Esto permite a la Miner seguir buscando hashes cuando el rango de la Nonce clásica ya se ha agotado, sin cambiar la estructura de su bloque candidato.


En los pools Mining, el extra-Nonce suele dividirse en dos partes: una generada por el pool para identificar a cada chopper, y otra modificada por el chopper en busca de una parte válida. Esto permite a los distintos choppers del pool trabajar simultáneamente en el mismo bloque candidato con todo el rango de nonces, sin duplicar el mismo trabajo a nivel de pool.