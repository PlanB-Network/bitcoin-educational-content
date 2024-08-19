---
termine: BIP143
---

Introduce un nuovo metodo di hashing della transazione per la verifica della firma nei post-script SegWit. L'obiettivo è minimizzare le operazioni ridondanti durante la verifica e includere il valore degli UTXO nell'input nella firma. Questo risolve due problemi principali con l'algoritmo di hashing della transazione originale:
* La crescita quadratica dell'hashing dei dati con il numero di firme;
* L'assenza dell'inclusione del valore dell'input nella firma, che rappresentava un rischio per i portafogli hardware, specialmente per quanto riguarda la conoscenza delle commissioni di transazione sostenute.
Dall'aggiornamento SegWit, spiegato in BIP141, che introduce una nuova forma di transazioni il cui script non sarà verificato dai nodi vecchi, BIP143 coglie questa opportunità per affrontare questo problema senza richiedere un hard fork. Pertanto, BIP143 fa parte del soft fork SegWit.