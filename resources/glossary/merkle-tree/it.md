---
term: Albero di Merkle

definition: Struttura dati gerarchica che consente una rapida verifica dell'inclusione di una transazione in un blocco.
---
Un albero di Merkle è un accumulatore crittografico. È un metodo per dimostrare l'appartenenza di una data informazione a un insieme più ampio. È una struttura di dati che facilita la verifica delle informazioni in un formato compatto. Nel sistema Bitcoin, gli alberi di Merkle sono utilizzati per raggruppare e condensare le transazioni di un blocco in un unico hash, chiamato Radice di Merkle (o "*Root Hash*"). Ogni transazione viene sottoposta a hash, quindi gli hash adiacenti vengono sottoposti a un hash gerarchico fino a ottenere la Merkle Root.



Questa struttura consente di verificare rapidamente se una specifica transazione è inclusa in un determinato blocco senza dover analizzare tutte le transazioni. Ad esempio, se ho solo la radice di Merkle e voglio verificare che `TX 7` fa effettivamente parte dell'albero, mi basteranno le seguenti prove:


- `TX 7`;
- `HASH 8`;
- `HASH 5-6`;
- `HASH 1-2-3-4`.

Con queste informazioni, sono in grado di calcolare i nodi intermedi fino alla radice di Merkle.



Le Merkle Trees sono utilizzate in particolare per i nodi leggeri (noti come "SPV") che conservano solo le intestazioni dei blocchi, ma non le transazioni. Questa struttura si trova anche nel protocollo UTREEXO, un protocollo che permette di condensare l'insieme dei nodi UTXO, e nel MAST Taproot.

