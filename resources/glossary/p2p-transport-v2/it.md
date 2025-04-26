---
term: TRASPORTO P2P V2

---
Nuova versione del protocollo di trasporto P2P Bitcoin che incorpora la crittografia opportunistica per migliorare la privacy e la sicurezza delle comunicazioni tra i nodi. Questo miglioramento mira a risolvere diversi problemi della versione base del protocollo P2P, in particolare rendendo i dati scambiati indistinguibili a un osservatore passivo (come un provider di servizi Internet), riducendo così i rischi di censura e di attacchi attraverso il rilevamento di modelli specifici nei pacchetti di dati.

La crittografia implementata non include l'autenticazione per evitare di aggiungere inutili complessità e per non compromettere la natura permissionless della connessione di rete. Questo nuovo protocollo di trasporto P2P offre comunque una migliore sicurezza contro gli attacchi passivi e rende gli attacchi attivi molto più costosi e rilevabili (in particolare gli attacchi MITM). L'introduzione di un flusso di dati pseudocasuale complica il compito degli aggressori che desiderano censurare o manipolare le comunicazioni.

Il P2P Transport V2 è stato incluso come opzione (disattivata per impostazione predefinita) nella versione 26.0 di Bitcoin Core, distribuita nel dicembre 2023. Può essere attivato con l'opzione `v2transport=1` nel file di configurazione.