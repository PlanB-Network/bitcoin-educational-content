---
termine: P2P TRANSPORT V2
---

Nuova versione del protocollo di trasporto P2P di Bitcoin che incorpora la crittografia opportunistica per migliorare la privacy e la sicurezza delle comunicazioni tra nodi. Questo miglioramento mira a risolvere diversi problemi con la versione base del protocollo P2P, in particolare rendendo i dati scambiati indistinguibili per un osservatore passivo (come un fornitore di servizi internet), riducendo così i rischi di censura e attacchi tramite il rilevamento di schemi specifici nei pacchetti di dati.

La crittografia implementata non include l'autenticazione al fine di evitare di aggiungere complessità non necessaria e per non compromettere la natura senza permessi della connessione di rete. Questo nuovo protocollo di trasporto P2P offre comunque una migliore sicurezza contro attacchi passivi e rende gli attacchi attivi significativamente più costosi e rilevabili (in particolare gli attacchi MITM). L'introduzione di un flusso di dati pseudo-casuale complica il compito per gli attaccanti che desiderano censurare o manipolare le comunicazioni.

Il P2P Transport V2 è stato incluso come opzione (disabilitata per impostazione predefinita) nella versione 26.0 di Bitcoin Core, distribuita nel dicembre 2023. Può essere attivato con l'opzione `v2transport=1` nel file di configurazione.