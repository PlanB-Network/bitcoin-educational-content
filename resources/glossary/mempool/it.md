---
term: MEMPOOL
---

Una contrazione dei termini "memory" (memoria) e "pool" (insieme). Questo si riferisce a uno spazio virtuale in cui le transazioni Bitcoin in attesa di essere incluse in un blocco sono raggruppate insieme. Quando una transazione viene creata e trasmessa sulla rete Bitcoin, viene prima verificata dai nodi della rete. Se viene considerata valida, viene poi posizionata nel Mempool di ogni nodo, dove rimane fino a quando non viene selezionata da un miner per essere inclusa in un blocco.

È importante notare che ogni nodo nella rete Bitcoin mantiene il proprio Mempool e, quindi, può esserci una variazione nei contenuti del Mempool tra diversi nodi in qualsiasi momento. In particolare, il parametro `maxmempool` nel file `bitcoin.conf` di ogni nodo permette agli operatori di controllare la quantità di RAM (memoria ad accesso casuale) che il loro nodo utilizzerà per memorizzare le transazioni in attesa nel Mempool. Limitando la dimensione del Mempool, gli operatori dei nodi possono prevenire che esso consumi troppe risorse sul loro sistema. Questo parametro è specificato in megabyte (MB). Il valore predefinito per Bitcoin Core ad oggi è 300 MB.

Le transazioni presenti nel Mempool sono provvisorie. Non dovrebbero essere considerate immutabili fino a quando non sono incluse in un blocco e dopo un certo numero di conferme. Queste possono spesso essere sostituite o eliminate.