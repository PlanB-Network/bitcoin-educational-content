---
termine: DIFFICULTY TARGET
---

Il fattore di difficoltà, noto anche come difficulty target, è un parametro utilizzato nel meccanismo di consenso tramite proof of work (Prova di Lavoro, PoW) su Bitcoin. Il target rappresenta un valore numerico che determina la difficoltà per i minatori di risolvere uno specifico problema crittografico, chiamato proof of work, nella creazione di un nuovo blocco sulla blockchain.

Il difficulty target è un numero regolabile di 256 bit (64 byte) che determina un limite di accettabilità per l'hashing degli header dei blocchi. In altre parole, affinché un blocco sia valido, l'hash del suo header con `SHA256d` (doppio `SHA256`) deve essere numericamente inferiore o uguale al difficulty target. La prova di lavoro consiste nel modificare il campo `nonce` dell'header del blocco o della transazione coinbase fino a quando l'hash risultante non è inferiore al valore target.

Questo target viene aggiustato ogni 2016 blocchi (circa ogni due settimane), durante un evento chiamato "aggiustamento". Il fattore di difficoltà viene ricalcolato basandosi sul tempo impiegato per minare i precedenti 2016 blocchi. Se il tempo totale è inferiore a due settimane, la difficoltà aumenta aggiustando il target verso il basso. Se il tempo totale è superiore a due settimane, la difficoltà diminuisce aggiustando il target verso l'alto. L'obiettivo è mantenere un tempo medio di mining di 10 minuti per blocco. Questo intervallo di tempo tra ogni blocco aiuta a prevenire divisioni della rete Bitcoin, risultando in uno spreco di potenza computazionale. Il difficulty target si trova in ogni header di blocco, all'interno del campo `nBits`. Poiché questo campo è ridotto a 32 bit e il target è effettivamente di 256 bit, il target viene compattato in un formato scientifico meno preciso.

![](../../dictionnaire/assets/34.png)

> ► *Il difficulty target è talvolta chiamato anche "fattore di difficoltà". Per estensione, può essere riferito con la sua codifica negli header dei blocchi con il termine "nBits".*