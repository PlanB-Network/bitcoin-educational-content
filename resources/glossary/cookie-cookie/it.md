---
term: COOKIE (.COOKIE)

---
File utilizzato per l'autenticazione RPC (*Remote Procedure Call*) in Bitcoin Core. Quando bitcoind si avvia, genera un cookie di autenticazione unico e lo memorizza in questo file. I client o gli script che desiderano interagire con bitcoind tramite l'interfaccia RPC possono utilizzare questo cookie per autenticarsi in modo sicuro. Questo meccanismo consente una comunicazione sicura tra bitcoind e le applicazioni esterne (come ad esempio i software di portafoglio), senza richiedere la gestione manuale di nomi utente e password. Il file `.cookie' viene rigenerato a ogni riavvio di bitcoind e cancellato allo spegnimento.