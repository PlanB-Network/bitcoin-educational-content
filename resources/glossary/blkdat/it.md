---
term: BLK*.DAT

---
Nome dei file in Bitcoin Core che memorizzano i dati grezzi dei blocchi della blockchain. Ogni file è identificato da un numero unico nel suo nome. Pertanto, i blocchi vengono registrati in ordine cronologico, a partire dal file blk00000.dat. Quando questo file raggiunge la sua capacità massima, i blocchi successivi vengono registrati in blk00001.dat, poi blk00002.dat e così via. Ogni file blk ha una capacità massima di 128 mebibyte (MiB), che equivale a poco più di 134 megabyte (MB). Dalla versione 0.8.0 questi file sono stati spostati nella cartella `/blocks`.