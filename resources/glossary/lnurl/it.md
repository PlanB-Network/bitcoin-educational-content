---
term: LNURL
---

Protocollo di comunicazione che specifica un insieme di funzionalità progettate per semplificare le interazioni tra i nodi Lightning e i clienti, nonché le applicazioni di terze parti. Questo protocollo è basato su HTTP e consente di creare collegamenti per varie operazioni, come una richiesta di pagamento, una richiesta di prelievo o altre funzionalità che migliorano l'esperienza dell'utente. Ogni LNURL è un URL codificato in bech32 con il prefisso `lnurl`, che, quando viene scansionato, attiva una serie di azioni automatiche sul Wallet di Lightning.


Ad esempio, LNURL-withdraw (LUD-03) consente di prelevare fondi da un servizio mediante la scansione di un codice QR, senza dover effettuare manualmente il generate di un Invoice. Oppure LNURL-auth (LUD-04) consente di connettersi ai servizi online utilizzando una chiave privata sul proprio Lightning Wallet invece di una password.