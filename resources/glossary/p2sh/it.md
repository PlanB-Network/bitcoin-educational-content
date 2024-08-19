---
term: P2SH
---

P2SH sta per *Pay to Script Hash*. È uno standard di script utilizzato per stabilire le condizioni di spesa su un UTXO. A differenza degli script P2PK e P2PKH, dove le condizioni di spesa sono predefinite, P2SH consente l'integrazione di condizioni di spesa arbitrarie e funzionalità aggiuntive all'interno di uno script di transazione.

Tecnicamente, in una transazione P2SH, lo `scriptPubKey` contiene l'hash crittografico di uno `script di riscatto` (`redeemScript`), piuttosto che condizioni di spesa esplicite. Questo hash è ottenuto utilizzando un hash `SHA256`. Quando si inviano bitcoin a un indirizzo P2SH, lo `script di riscatto` sottostante non viene rivelato. Solo il suo hash è incluso nella transazione. Gli indirizzi P2SH sono codificati in `Base58Check` e iniziano con il numero `3`. Quando il destinatario desidera spendere i bitcoin ricevuti, deve fornire uno `script di riscatto` che corrisponda all'hash presente nello `scriptPubKey`, insieme ai dati necessari per soddisfare le condizioni di questo `script di riscatto`. Ad esempio, in uno script multisignature P2SH, lo script potrebbe richiedere le firme di più chiavi private.

L'uso di P2SH offre maggiore flessibilità, poiché consente la costruzione di script arbitrari senza che il mittente conosca i dettagli. P2SH è stato introdotto nel 2012 con il BIP16.