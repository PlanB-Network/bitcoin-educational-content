---
term: PSBT
---

Acronimo di "Partially Signed Bitcoin Transaction" (Transazione Bitcoin Parzialmente Firmata). Si tratta di una specifica introdotta con il BIP174 per standardizzare il modo in cui le transazioni non completate sono costruite nel software relativo a Bitcoin, come ad esempio i software di portafoglio. Un PSBT incapsula una transazione nella quale gli input potrebbero non essere completamente firmati. Include tutte le informazioni necessarie affinché un partecipante possa firmare la transazione senza richiedere dati aggiuntivi. Pertanto, un PSBT può assumere 3 diverse forme:
* Una transazione completamente costruita, ma non ancora firmata;
* Una transazione parzialmente firmata, dove alcuni input sono firmati mentre altri non lo sono ancora;
* O una transazione Bitcoin completamente firmata, che può essere convertita per essere pronta per la trasmissione sulla rete.

Il formato PSBT facilita l'interoperabilità tra diversi software di portafoglio e dispositivi di firma (portafoglio hardware). Attualmente, viene utilizzata la versione 0 del PSBT, come definito nel BIP174, ma la versione 2 è stata proposta tramite il BIP370.

> ► *La versione 1 del PSBT non esiste. Poiché la versione 0 era la prima versione, la seconda versione è stata informalmente chiamata versione 2. Ava Chow, che ha redatto il BIP370, ha quindi deciso di assegnare il numero 2 a questa nuova versione per evitare qualsiasi confusione.*