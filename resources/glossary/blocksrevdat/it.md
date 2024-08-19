---
termine: BLOCKS/REV*.DAT
---

Nome dei file in Bitcoin Core che memorizzano le informazioni necessarie per potenzialmente invertire le modifiche apportate all'insieme UTXO dai blocchi precedentemente aggiunti. Ogni file è identificato da un numero unico che corrisponde al file blk*.dat a cui si riferisce. I file rev*.dat contengono i dati di inversione corrispondenti ai blocchi memorizzati nei file blk*.dat. Questi dati sono essenzialmente un elenco di tutti gli UTXO spesi come input in un blocco. Questi file di inversione permettono al nodo di ritornare a uno stato precedente in caso di una riorganizzazione della blockchain che causa lo scarto di blocchi precedentemente validati.