---
term: WTXID

definition: Identificativo di transazione che include i dati witness, un'estensione del TXID introdotta con SegWit.
---
Un'estensione del TXID tradizionale, che include i dati del testimone introdotti con SegWit. Mentre il TXID è un hash dei dati della transazione escluso il testimone, il WTXID è lo `SHA256d` dell'intera transazione, testimone incluso. I WTXID sono memorizzati in un albero Merkle separato la cui radice è collocata nella transazione coinbase. Questa separazione consente di eliminare la malleabilità della transazione TXID.