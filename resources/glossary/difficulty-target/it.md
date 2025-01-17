---
term: OBIETTIVO DI DIFFICOLTÀ

---
Il fattore di difficoltà, noto anche come obiettivo di difficoltà, è un parametro utilizzato nel meccanismo di consenso per prova di lavoro (Proof of Work, PoW) su Bitcoin. Il target rappresenta un valore numerico che determina la difficoltà per i minatori di risolvere uno specifico problema crittografico, chiamato proof of work, quando si crea un nuovo blocco sulla blockchain.

Il target di difficoltà è un numero regolabile di 256 bit (64 byte) che determina un limite di accettabilità per l'hashing delle intestazioni dei blocchi. In altre parole, affinché un blocco sia valido, l'hash della sua intestazione con `SHA256d` (doppio `SHA256`) deve essere numericamente inferiore o uguale all'obiettivo di difficoltà. La prova di lavoro consiste nel modificare il campo `nonce` dell'intestazione del blocco o della transazione coinbase finché l'hash risultante non è inferiore al valore target.

Questo obiettivo viene modificato ogni 2016 blocchi (circa ogni due settimane), durante un evento chiamato "aggiustamento" Il fattore di difficoltà viene ricalcolato in base al tempo impiegato per estrarre i blocchi 2016 precedenti. Se il tempo totale è inferiore a due settimane, la difficoltà aumenta aggiustando l'obiettivo al ribasso. Se il tempo totale è superiore a due settimane, la difficoltà diminuisce regolando l'obiettivo verso l'alto. L'obiettivo è mantenere un tempo medio di estrazione di 10 minuti per blocco. Questo tempo tra un blocco e l'altro aiuta a prevenire le divisioni della rete Bitcoin, con conseguente spreco di potenza di calcolo. L'obiettivo di difficoltà si trova nell'intestazione di ogni blocco, nel campo `nBits`. Poiché questo campo è ridotto a 32 bit e l'obiettivo è in realtà di 256 bit, l'obiettivo è compattato in un formato scientifico meno preciso.

![](../../dictionnaire/assets/34.webp)

> *L'obiettivo di difficoltà è talvolta chiamato anche "fattore di difficoltà" Per estensione, può essere indicato con la sua codifica nelle intestazioni dei blocchi con il termine "nBits"