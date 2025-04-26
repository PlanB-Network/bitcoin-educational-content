---
term: ASSUNZIONE UTXO

---
Parametro di configurazione del client principale di Bitcoin Core che consente a un nodo appena inizializzato (ma non ancora sottoposto all'IBD) di rinviare la verifica delle transazioni e del set UTXO fino a una determinata istantanea. Il concetto si basa sull'uso di un set UTXO (un elenco di tutti gli UTXO esistenti in un determinato momento) fornito dal Core e presumibilmente accurato, che consente al nodo di sincronizzarsi molto rapidamente con la catena con il maggior numero di lavori accumulati. Poiché il nodo salta la lunga fase di IBD, diventa operativo per il suo utente molto rapidamente. Si supponga che UTXO divida la sincronizzazione (IBD) in due parti:


- In primo luogo, il nodo esegue l'Header First Sync (verifica solo delle intestazioni) e considera valido il set UTXO fornito dal Core;
- Quindi, una volta operativo, il nodo verificherà la cronologia completa dei blocchi in background, aggiornando un nuovo set UTXO che ha verificato da solo. Se questo nuovo set UTXO non corrisponde a quello fornito dal Core, viene visualizzato un messaggio di errore.

Pertanto, supponiamo che UTXO acceleri la preparazione di un nuovo nodo Bitcoin posticipando il processo di verifica delle transazioni e il set UTXO attraverso un'istantanea aggiornata fornita nel Core.