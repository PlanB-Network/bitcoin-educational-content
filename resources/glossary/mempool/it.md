---
term: MEMPOOL

---
Contrazione dei termini "memoria" e "pool". Si riferisce a uno spazio virtuale in cui vengono raggruppate le transazioni Bitcoin in attesa di essere incluse in un blocco. Quando una transazione viene creata e trasmessa sulla rete Bitcoin, viene prima verificata dai nodi della rete. Se è ritenuta valida, viene inserita nella Mempool di ciascun nodo, dove rimane fino a quando non viene selezionata da un miner per essere inclusa in un blocco.

È importante notare che ogni nodo della rete Bitcoin mantiene il proprio Mempool e quindi il contenuto del Mempool può variare in qualsiasi momento tra i diversi nodi. In particolare, il parametro `maxmempool` nel file `bitcoin.conf` di ogni nodo consente agli operatori di controllare la quantità di RAM (memoria ad accesso casuale) che il loro nodo utilizzerà per memorizzare le transazioni in sospeso nel Mempool. Limitando la dimensione del Mempool, gli operatori dei nodi possono evitare che esso consumi troppe risorse sul loro sistema. Questo parametro è specificato in megabyte (MB). Il valore predefinito per Bitcoin Core ad oggi è di 300 MB.

Le transazioni presenti nella Mempool sono provvisorie. Non devono essere considerate immutabili finché non vengono incluse in un blocco e dopo un certo numero di conferme. Spesso possono essere sostituite o eliminate.