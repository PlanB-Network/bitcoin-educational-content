---
term: BIP141
---

Ha introdotto il concetto di Segregated Witness (SegWit) che ha dato il nome al soft fork SegWit. BIP141 introduce una modifica importante al protocollo Bitcoin con l'obiettivo di risolvere il problema della malleabilità delle transazioni. SegWit separa i dati di testimoniatura (dati della firma) dal resto dei dati della transazione. Questa separazione è ottenuta inserendo i testimoni in una struttura dati separata, impegnata in un nuovo albero di Merkle, che a sua volta è referenziato nel blocco tramite la transazione coinbase, rendendo SegWit compatibile con versioni precedenti del protocollo.