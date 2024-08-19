---
term: P2PKH
---

P2PKH sta per *Pay to Public Key Hash* (Pagare all'Hash della Chiave Pubblica). È un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO. Permette di bloccare bitcoin su un hash di una chiave pubblica, ovvero su un indirizzo di ricezione. Questo script è associato allo standard Legacy ed è stato introdotto nelle prime versioni di Bitcoin da Satoshi Nakamoto.

A differenza di P2PK, dove la chiave pubblica è inclusa esplicitamente nello script, P2PKH utilizza un'impronta crittografica della chiave pubblica. Questo script include l'hash `RIPEMD160` dell'`SHA256` della chiave pubblica e stabilisce che, per accedere ai fondi, il destinatario deve fornire una chiave pubblica che corrisponda a questo hash, oltre a una firma digitale valida generata dalla chiave privata associata. Gli indirizzi P2PKH sono codificati utilizzando il formato `Base58Check`, che li rende robusti contro errori di battitura attraverso l'uso di un checksum. Questi indirizzi iniziano sempre con il numero `1`.