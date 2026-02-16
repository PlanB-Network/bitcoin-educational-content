---
term: Chiave pubblica

definition: Elemento crittografico derivato da una chiave privata, utilizzato per creare indirizzi Bitcoin.
---
La chiave pubblica è un elemento utilizzato nella crittografia asimmetrica. Viene generata da una chiave privata utilizzando una funzione matematica irreversibile. Su Bitcoin, le chiavi pubbliche sono derivate dalla chiave privata associata attraverso gli algoritmi di firma digitale a curva ellittica ECDSA o Schnorr. A differenza della chiave privata, la chiave pubblica può essere condivisa liberamente senza compromettere la sicurezza dei fondi. All'interno del protocollo Bitcoin, la chiave pubblica serve come base per creare un indirizzo Bitcoin, che viene poi utilizzato per creare condizioni di spesa su un UTXO utilizzando una `scriptPubKey`. Le chiavi pubbliche vengono spesso confuse con la chiave master o con le chiavi estese (xpub...). Tuttavia, questi elementi sono molto diversi.

