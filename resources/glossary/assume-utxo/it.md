---
term: Assume utxo

definition: Un parametro Bitcoin Core che consente la sincronizzazione rapida di un nuovo nodo utilizzando uno snapshot del set UTXO presumibilmente valido, prima di verificare la cronologia in background.
---
Parametro di configurazione nel client di maggioranza Bitcoin Core che consente a un nodo appena inizializzato (ma che non ha ancora eseguito l'IBD) di posticipare la verifica delle transazioni e dell'UTXO set prima di un determinato snapshot. Il concetto si basa sull'uso di un UTXO set (elenco di tutti gli UTXO esistenti in un dato momento) fornito da Core e presunto accurato, che consente al nodo di sincronizzarsi molto rapidamente sulla catena con il maggior lavoro accumulato. Poiché il nodo salta la lunga fase di IBD, diventa operativo per l'utente in tempi brevissimi.

Assume UTXO divide la sincronizzazione (IBD) in due parti: in primo luogo, il nodo esegue l'Header First Sync (solo verifica delle intestazioni) e considera valido l'UTXO set fornitogli da Core; quindi, una volta funzionante, il nodo verificherà la cronologia completa dei blocchi in background, aggiornando un nuovo UTXO set che avrà verificato esso stesso. Se quest'ultimo non corrisponde all'UTXO set fornito da Core, fornirà un messaggio di errore.

Assume UTXO consente quindi di accelerare la preparazione di un nuovo nodo Bitcoin posticipando il processo di verifica delle transazioni e dell'UTXO set grazie a uno snapshot aggiornato fornito in Core.





