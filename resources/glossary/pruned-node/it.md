---
term: NODO PRUNITO

---
Un nodo potato, in inglese "Pruned Node", è un nodo completo che esegue la potatura della blockchain. Questo comporta la progressiva rimozione dei blocchi più vecchi, dopo averli debitamente verificati, per conservare solo i blocchi più recenti. Il limite di conservazione è specificato nel file `bitcoin.conf` tramite il parametro `prune=n`, dove `n` è la dimensione massima assunta dai blocchi in megabyte (MB). Se dopo questo parametro viene indicato `0`, il pruning viene disabilitato e il nodo conserva la blockchain nella sua interezza.

I nodi potati sono talvolta considerati come tipi di nodi diversi dai nodi completi. L'uso di un nodo potato può essere particolarmente interessante per gli utenti che devono affrontare vincoli di capacità di archiviazione. Attualmente, un nodo completo deve disporre di quasi 600 GB solo per memorizzare la blockchain. Un nodo potato può limitare lo spazio di archiviazione richiesto a 550 MB. Sebbene utilizzi meno spazio su disco, un nodo potato mantiene un livello di verifica e validazione simile a quello di un nodo completo. I nodi pruned offrono quindi maggiore fiducia agli utenti rispetto ai nodi light (SPV).