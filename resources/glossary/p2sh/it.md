---
term: P2SH

---
P2SH sta per *Pay to Script Hash*. È un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO. A differenza degli script P2PK e P2PKH, in cui le condizioni di spesa sono predefinite, P2SH consente di integrare condizioni di spesa arbitrarie e funzionalità aggiuntive in uno script di transazione.

Tecnicamente, in una transazione P2SH, la `scriptPubKey` contiene l'hash crittografico di un `redeemScript`, piuttosto che condizioni di spesa esplicite. Questo hash è ottenuto utilizzando un hash `SHA256`. Quando si inviano bitcoin a un indirizzo P2SH, il `redeemScript` sottostante non viene rivelato. Solo il suo hash è incluso nella transazione. Gli indirizzi P2SH sono codificati in `Base58Check` e iniziano con il numero `3`. Quando il destinatario desidera spendere i bitcoin ricevuti, deve fornire un `redeemScript` che corrisponde all'hash presente nella `scriptPubKey`, insieme ai dati necessari per soddisfare le condizioni di questo `redeemScript`. Ad esempio, in uno script P2SH con più firme, lo script potrebbe richiedere le firme di più chiavi private.

L'uso di P2SH offre una maggiore flessibilità, in quanto consente la costruzione di script arbitrari senza che il mittente ne conosca i dettagli. P2SH è stato introdotto nel 2012 con BIP16.