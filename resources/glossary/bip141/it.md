---
term: BIP141

---
Ha introdotto il concetto di Segregated Witness (SegWit) che ha dato il nome al soft fork SegWit. BIP141 introduce un'importante modifica al protocollo Bitcoin per risolvere il problema della malleabilità delle transazioni. SegWit separa il testimone (dati della firma) dal resto dei dati della transazione. Questa separazione si ottiene inserendo i testimoni in una struttura di dati separata, impegnata in un nuovo albero di Merkle, che viene a sua volta referenziato nel blocco tramite la transazione coinbase, rendendo SegWit compatibile con le versioni precedenti del protocollo.