---
termine: COINBASE (TRANSAZIONE)
---

La transazione coinbase è una transazione speciale e unica inclusa in ogni blocco della blockchain di Bitcoin. Rappresenta la prima transazione di un blocco ed è creata dal minatore che ha trovato con successo un'intestazione che valida la prova di lavoro (*Proof-of-Work*), ovvero, inferiore o uguale al target.

La transazione coinbase ha principalmente due scopi: premiare il minatore con il block reward e aggiungere nuove unità di bitcoin alla fornitura di moneta circolante. Il block reward, che è l'incentivo economico per i minatori a impegnarsi nella prova di lavoro, include le commissioni accumulate per le transazioni incluse nel blocco e una determinata quantità di bitcoin appena creati ex-nihilo (sussidio di blocco). Questa quantità, inizialmente fissata a 50 bitcoin per blocco nel 2009, viene dimezzata ogni 210.000 blocchi (circa ogni 4 anni) durante un evento chiamato "halving".

La transazione coinbase si differenzia dalle transazioni regolari in diversi modi. Primo, non ha un input, il che significa che nessun output di transazione esistente (UTXO) viene consumato da essa. Successivamente, lo script di firma (`scriptSig`) per la transazione coinbase contiene tipicamente un campo arbitrario che permette l'incorporazione di dati aggiuntivi, come messaggi personalizzati o informazioni sulla versione del software di mining. Infine, i bitcoin generati dalla transazione coinbase sono soggetti a un periodo di maturità di 100 blocchi (101 conferme) prima che possano essere spesi, per prevenire la potenziale spesa di bitcoin non esistenti in caso di una riorganizzazione della catena.

> ► *Non esiste una traduzione per "Coinbase" in francese. Pertanto, è accettato utilizzare direttamente questo termine.*