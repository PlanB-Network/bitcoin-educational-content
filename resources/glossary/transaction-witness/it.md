---
term: TESTIMONE DI TRANSAZIONE

---
Si riferisce a un componente delle transazioni Bitcoin che è stato spostato con il soft fork SegWit per risolvere il problema della malleabilità delle transazioni. Il testimone contiene le firme e le chiavi pubbliche necessarie per sbloccare i bitcoin spesi in una transazione. Nelle transazioni Legacy, il testimone rappresentava la somma di `scriptSig` di tutti gli input. Nelle transazioni SegWit, il testimone rappresenta la somma di `scriptWitness` per ogni input, e questa parte della transazione è ora spostata in un Merkle tree separato all'interno del blocco.

Prima di SegWit, le firme potevano essere leggermente alterate senza essere invalidate prima che una transazione fosse confermata, modificando così l'identificativo della transazione. Ciò rendeva difficile la creazione di vari protocolli, poiché una transazione non confermata poteva veder cambiare il proprio identificatore. Separando i testimoni, SegWit rende le transazioni non malleabili, in quanto qualsiasi modifica delle firme non influisce più sull'identificatore della transazione (TXID), ma solo sull'identificatore del testimone (WTXID). Oltre a risolvere il problema della malleabilità, questa separazione consente di aumentare la capacità di ciascun blocco.

> *In inglese, "témoin" è tradotto come "testimone "*