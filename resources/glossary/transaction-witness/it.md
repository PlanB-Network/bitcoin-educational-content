---
term: TRANSACTION WITNESS
---

Si riferisce a una componente delle transazioni Bitcoin che è stata spostata con il soft fork SegWit per affrontare il problema della malleabilità delle transazioni. Il witness contiene le firme e le chiavi pubbliche necessarie per sbloccare i bitcoin spesi in una transazione. Nelle transazioni Legacy, il witness rappresentava la somma di `scriptSig` da tutti gli input. Nelle transazioni SegWit, il witness rappresenta la somma di `scriptWitness` per ogni input, e questa parte della transazione è ora spostata in un albero di Merkle separato all'interno del blocco.

Prima di SegWit, le firme potevano essere leggermente alterate senza essere invalidate prima che una transazione fosse confermata, il che cambiava l'identificatore della transazione. Questo rendeva difficile costruire vari protocolli, poiché un'identificatore di transazione non confermata poteva cambiare. Separando i witness, SegWit rende le transazioni non malleabili, poiché qualsiasi cambiamento nelle firme non influisce più sull'identificatore della transazione (TXID), ma solo sull'identificatore del witness (WTXID). Oltre a risolvere il problema della malleabilità, questa separazione consente un aumento della capacità di ogni blocco.

> ► *In inglese, "témoin" si traduce con "witness".*