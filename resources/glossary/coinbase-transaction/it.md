---
term: COINBASE (TRANSAZIONE)

---
La transazione coinbase è una transazione speciale e unica inclusa in ogni blocco della blockchain Bitcoin. Rappresenta la prima transazione di un blocco ed è creata dal miner che ha trovato con successo un'intestazione che convalida la prova di lavoro (*Proof-of-Work*), cioè inferiore o uguale all'obiettivo.

La transazione coinbase ha principalmente due scopi: assegnare la ricompensa del blocco al minatore e aggiungere nuove unità di bitcoin alla massa monetaria circolante. La ricompensa del blocco, che rappresenta l'incentivo economico per i minatori a impegnarsi nella prova del lavoro, comprende le commissioni accumulate per le transazioni incluse nel blocco e una determinata quantità di bitcoin di nuova creazione ex-nihilo (sovvenzione del blocco). Questo importo, inizialmente fissato a 50 bitcoin per blocco nel 2009, viene dimezzato ogni 210.000 blocchi (circa ogni 4 anni) durante un evento chiamato "dimezzamento"

La transazione coinbase si differenzia dalle transazioni normali per diversi aspetti. In primo luogo, non ha un ingresso, il che significa che non viene consumato l'output di una transazione esistente (UTXO). Inoltre, lo script di firma (`scriptSig`) per la transazione coinbase contiene tipicamente un campo arbitrario che consente di incorporare dati aggiuntivi, come messaggi personalizzati o informazioni sulla versione del software di mining. Infine, i bitcoin generati dalla transazione coinbase sono soggetti a un periodo di maturità di 100 blocchi (101 conferme) prima di poter essere spesi, per evitare che in caso di riorganizzazione della catena si possano spendere bitcoin inesistenti.

> *Non esiste una traduzione di "Coinbase" in francese. Pertanto, è accettato l'uso diretto di questo termine