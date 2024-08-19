---
termine: ASSUME UTXO
---

Un parametro di configurazione nel principale client Bitcoin Core che permette a un nodo appena inizializzato (ma che non ha ancora completato l'IBD) di posticipare la verifica delle transazioni e del set UTXO fino a uno snapshot dato. Il concetto si basa sull'uso di un set UTXO (un elenco di tutti gli UTXO esistenti in un dato momento) fornito da Core e presunto accurato, che permette al nodo di sincronizzarsi molto rapidamente con la catena con il maggior lavoro accumulato. Poiché il nodo salta il lungo passaggio dell'IBD, diventa operativo per il suo utente molto velocemente. Assume UTXO divide la sincronizzazione (IBD) in due parti:
* Prima, il nodo esegue la sincronizzazione Header First (verifica solo degli header) e considera il set UTXO fornito da Core come valido;
* Poi, una volta che è operativo, il nodo verificherà la completa storia dei blocchi in background, aggiornando un nuovo set UTXO che ha verificato da sé. Se questo nuovo set UTXO non corrisponde a quello fornito da Core, produrrà un messaggio di errore.

Pertanto, Assume UTXO accelera la preparazione di un nuovo nodo Bitcoin posticipando il processo di verifica delle transazioni e del set UTXO attraverso uno snapshot aggiornato fornito in Core.