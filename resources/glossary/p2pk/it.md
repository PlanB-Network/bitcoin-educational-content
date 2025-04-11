---
term: P2PK

---
P2PK sta per *Pay to Public Key*. È un modello di script standard utilizzato su Bitcoin per stabilire le condizioni di spesa su un UTXO. Consente di bloccare i bitcoin direttamente su una chiave pubblica, anziché su un indirizzo.

Tecnicamente, lo script P2PK contiene una chiave pubblica e un'istruzione che richiede una firma digitale corrispondente per sbloccare i fondi. Quando il proprietario desidera spendere i bitcoin, deve fornire una firma prodotta con la chiave privata associata. Questa firma viene verificata utilizzando l'ECDSA (*algoritmo di firma digitale a curva ellittica*). Il P2PK è stato spesso utilizzato nelle prime versioni di Bitcoin, in particolare da Satoshi Nakamoto. Oggi non è quasi più utilizzato.