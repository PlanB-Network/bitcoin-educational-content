---
termine: WALLET FOOTPRINT
---

Un insieme di caratteristiche distintive osservabili nelle transazioni effettuate dallo stesso portafoglio Bitcoin. Queste caratteristiche possono includere somiglianze nell'uso dei tipi di script, il riutilizzo degli indirizzi, l'ordine degli UTXO, il posizionamento degli output di resto, la segnalazione di RBF (*Replace-by-Fee*), il numero di versione, il campo `nSequence` e il campo `nLockTime`.

Le impronte dei portafogli sono utilizzate dagli analisti per tracciare le attività di una particolare entità sulla blockchain identificando schemi ricorrenti nelle sue transazioni. Ad esempio, un utente che sistematicamente invia il suo resto agli indirizzi P2TR (`bc1p…`) crea un'impronta distintiva che può essere utilizzata per tracciare le sue future transazioni.

Come spiega LaurentMT in Space Kek #19 (un podcast in lingua francese), l'utilità delle impronte dei portafogli nell'analisi della catena aumenta significativamente nel tempo. Infatti, il crescente numero di tipi di script e il dispiegamento sempre più graduale di queste nuove funzionalità da parte del software del portafoglio accentuano le differenze. È addirittura possibile identificare con precisione il software utilizzato dall'entità tracciata. Pertanto, è importante comprendere che studiare l'impronta di un portafoglio è particolarmente rilevante per le transazioni recenti, più che per quelle avviate nei primi anni 2010.