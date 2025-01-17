---
term: BIP143

---
Introduce un nuovo metodo di hashing della transazione per la verifica della firma negli script post-SegWit. L'obiettivo è ridurre al minimo le operazioni ridondanti durante la verifica e includere il valore degli UTXO nell'input della firma. Questo risolve due problemi principali dell'algoritmo originale di hashing delle transazioni:


- La crescita quadratica dell'hashing dei dati con il numero di firme;
- L'assenza di includere il valore di input nella firma, che rappresentava un rischio per i portafogli hardware, soprattutto per quanto riguarda la conoscenza delle commissioni di transazione sostenute.

Poiché l'aggiornamento SegWit, spiegato nella BIP141, introduce una nuova forma di transazioni la cui scrittura non sarà verificata dai vecchi nodi, la BIP143 coglie l'occasione per affrontare questo problema senza richiedere un hard fork. Pertanto, la BIP143 fa parte della soft fork di SegWit.