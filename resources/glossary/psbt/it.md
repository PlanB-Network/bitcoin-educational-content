---
term: PSBT

---
Acronimo di "Partially Signed Bitcoin Transaction". È una specifica introdotta con BIP174 per standardizzare il modo in cui le transazioni non finite vengono costruite nel software relativo a Bitcoin, come il software del portafoglio. Una PSBT incapsula una transazione in cui gli input potrebbero non essere completamente firmati. Include tutte le informazioni necessarie affinché un partecipante possa firmare la transazione senza richiedere dati aggiuntivi. Pertanto, un PSBT può assumere 3 forme diverse:


- Una transazione completamente costruita, ma non ancora firmata;
- Una transazione parzialmente firmata, in cui alcuni input sono firmati mentre altri non lo sono ancora;
- Oppure una transazione Bitcoin completamente firmata, che può essere convertita per essere pronta per la trasmissione sulla rete.

Il formato PSBT facilita l'interoperabilità tra diversi software e dispositivi di firma (hardware wallet). Attualmente viene utilizzata la versione 0 del PSBT, definita nel BIP174, ma la versione 2 è stata proposta tramite il BIP370.

> la versione 1 del PSBT non esiste. Dato che la versione 0 era la prima, la seconda versione è stata informalmente chiamata versione 2. Ava Chow, autrice del BIP370, ha quindi deciso di assegnare il numero 2 a questa nuova versione per evitare qualsiasi confusione.*