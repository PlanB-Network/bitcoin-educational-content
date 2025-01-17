---
term: BLOCKS/REV*.DAT

---
Nome dei file in Bitcoin Core che memorizzano le informazioni necessarie per invertire potenzialmente le modifiche apportate all'insieme UTXO dai blocchi precedentemente aggiunti. Ogni file è identificato da un numero unico che è lo stesso del file blk*.dat a cui corrisponde. I file rev*.dat contengono i dati di inversione corrispondenti ai blocchi memorizzati nei file blk*.dat. Questi dati sono essenzialmente un elenco di tutti gli UTXO spesi come ingressi in un blocco. Questi file di inversione consentono al nodo di tornare a uno stato precedente in caso di riorganizzazione della blockchain che causa lo scarto dei blocchi precedentemente convalidati.