---
term: PRUNED NODE
---

Un pruned node, in italiano "Nodo Potato", è un nodo completo che esegue la potatura della blockchain. Questo comporta la rimozione progressiva dei blocchi più vecchi, dopo averli debitamente verificati, per mantenere solo i blocchi più recenti. Il limite di conservazione è specificato nel file `bitcoin.conf` tramite il parametro `prune=n`, dove `n` è la dimensione massima occupata dai blocchi in megabyte (MB). Se dopo questo parametro è indicato `0`, allora la potatura è disabilitata e il nodo mantiene la blockchain nella sua interezza.

I nodi potati sono talvolta considerati come tipi di nodi diversi dai nodi completi. L'uso di un nodo potato può essere particolarmente interessante per gli utenti che affrontano vincoli di capacità di archiviazione. Attualmente, un nodo completo deve avere quasi 600 GB solo per memorizzare la blockchain. Un nodo potato può limitare lo spazio di archiviazione richiesto fino a 550 MB. Sebbene utilizzi meno spazio su disco, un nodo potato mantiene un livello di verifica e validazione simile a quello di un nodo completo. I nodi potati offrono quindi maggiore fiducia ai loro utenti in confronto ai nodi leggeri (SPV).