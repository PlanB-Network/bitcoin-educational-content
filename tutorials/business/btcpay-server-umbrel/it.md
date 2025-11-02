---
name: BTCPAY SERVER - Ombrello
description: Installazione e utilizzo di BTCPAY SERVER su Umbrel per accettare Bitcoin e Lightning
---

![cover](assets/cover.webp)



Nell'ecosistema Bitcoin, l'accettazione dei pagamenti rappresenta una sfida importante per i commercianti e le imprese. Le soluzioni tradizionali, siano esse bancarie (carte di credito, Stripe, PayPal) o anche Bitcoin (BitPay, Coinbase Commerce), impongono intermediari che applicano commissioni sostanziali, raccolgono i vostri dati aziendali sensibili e possono BLOCK o censurare le vostre transazioni a loro piacimento. Questa dipendenza è contraria ai principi fondamentali del Bitcoin di decentralizzazione, riservatezza e sovranità finanziaria.



BTCPAY SERVER si sta affermando come la risposta open-source a questo problema. Questo processore di pagamento self-hosted trasforma il vostro nodo Bitcoin in un'infrastruttura professionale, senza intermediari, senza commissioni di elaborazione aggiuntive e senza compromessi sulla privacy. Sviluppato da una comunità globale di collaboratori dal 2017, BTCPAY SERVER consente di ricevere pagamenti Bitcoin e Lightning direttamente nei propri portafogli, mantenendo il pieno controllo dei propri fondi in ogni momento.



Tradizionalmente, l'installazione di BTCPAY SERVER richiede competenze tecniche avanzate: Configurazione del server Linux, padronanza di Docker, gestione dei certificati SSL e sicurezza della rete. Umbrel rivoluziona questo approccio grazie a un'installazione con un solo clic, direttamente integrata con i vostri Bitcoin e LIGHTNING NODE. Questa semplificazione rende accessibile a tutti ciò che prima era riservato a tecnici esperti.



**Importante da capire**: BTCPAY SERVER su Umbrel funziona per impostazione predefinita solo sulla rete locale. È possibile creare fatture, accettare pagamenti Lightning e Bitcoin e gestire la contabilità da qualsiasi dispositivo connesso alla rete domestica (computer, smartphone, tablet). Questa configurazione è ideale per la fatturazione di servizi di persona, per la gestione di pagamenti faccia a faccia o per l'utilizzo di BTCPAY SERVER dalla rete locale. D'altra parte, per integrare BTCPAY SERVER in un negozio online accessibile pubblicamente su Internet, sarà necessaria un'ulteriore configurazione con esposizione pubblica (tratteremo questo argomento alla fine del tutorial).



Questo tutorial illustra l'installazione completa di BTCPAY SERVER su Umbrel, la configurazione di Bitcoin Wallet e LIGHTNING NODE, la creazione e il pagamento delle fatture e la gestione dei rapporti contabili. Scoprirete come utilizzare efficacemente il BTCPAY SERVER sulla vostra rete locale, e poi parleremo delle soluzioni per la visualizzazione pubblica se volete integrarlo con un sito di e-commerce.



## Prerequisiti



Per seguire questo tutorial, è necessario che Umbrel sia installato e configurato correttamente. Se non l'avete ancora fatto, consultate il nostro tutorial sull'installazione di Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Il nodo Bitcoin core deve essere completamente sincronizzato con Blockchain (100% nell'applicazione Bitcoin di Umbrel). Questa sincronizzazione iniziale richiede solitamente da 3 giorni a 2 settimane, a seconda dell'hardware e della connessione a Internet.



Per accettare pagamenti istantanei Lightning, è necessario installare LND (Lightning Network Daemon) su Umbrel. Se volete abilitare questa funzione, consultate il nostro tutorial sull'installazione e la configurazione di LND su Umbrel.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Prevedere almeno 50 GB di spazio libero su disco per BTCPAY SERVER, i suoi database e i dati di Lightning. Si raccomanda vivamente di disporre di una connessione Internet stabile tramite cavo Ethernet per evitare disconnessioni.



## Installazione del BTCPAY SERVER su Umbrel



Da Umbrel Interface (`umbrel.local`), accedere all'App Store e cercare "BTCPAY SERVER" nella categoria Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Fare clic su Installa. Umbrel controlla automaticamente che Bitcoin core e LND siano installati, quindi avvia la distribuzione (2-5 minuti).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Una volta installata, aprire l'applicazione. È necessario creare un account amministratore con credenziali forti.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Una volta creato il vostro account, BTCPAY SERVER vi chiederà immediatamente di creare il vostro primo negozio. Scegliete un nome professionale e selezionate una valuta di riferimento (EUR, USD o BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Accesso al BTCPAY SERVER sulla rete locale



Il BTCPAY SERVER è accessibile da qualsiasi dispositivo della rete locale (WiFi o Ethernet). Accesso dal browser a :



```url
http://umbrel.local
```



O direttamente a :



```url
http://umbrel.local:3003
```



**Accesso remoto con Tailscale**: Per accedere al BTCPAY SERVER da qualsiasi parte del mondo, utilizzate Tailscale. Questa VPN sicura vi permette di connettervi al vostro Umbrel come se foste sulla vostra rete locale. Consultate il nostro tutorial dedicato a Tailscale su Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Configurazione della cartella Bitcoin



Per accettare i pagamenti, è necessario configurare un Bitcoin Wallet. Il BTCPAY SERVER visualizza le opzioni di configurazione nella dashboard.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Per configurare il Wallet Bitcoin, andare a "Portafogli" > "Bitcoin".



Avete due opzioni: creare un nuovo portafoglio direttamente in BTCPay o importare un portafoglio esistente. Per l'importazione sono disponibili diversi metodi:




- Collegare Hardware Wallet** (consigliato): Importare le chiavi pubbliche tramite l'applicazione Vault
- Importazione del file Wallet** (consigliato): Caricare un file esportato dal proprio portfolio
- Inserire la chiave pubblica estesa**: Inserire manualmente la propria XPub/YPub/ZPub
- Scansione del codice QR Wallet** : Scansione di un codice QR da BlueWallet, Cobo Vault, Passport o Specter DIY
- Inserire Wallet seed** (non consigliato) : Inserire la frase di recupero di 12 o 24 parole



![Options de création de portefeuille](assets/fr/06.webp)



Per questo tutorial, creeremo un nuovo Hot Wallet: la chiave privata sarà quindi memorizzata sul nostro server Umbrel. In questo caso, consigliamo vivamente di spostare regolarmente i fondi su un Cold Wallet per evitare di immagazzinare grandi quantità sul server.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Una volta configurato, il BTCPAY SERVER conferma che il Wallet è pronto ad accettare i pagamenti del On-Chain .



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Attivare il Lightning Network



Per accettare pagamenti istantanei con Lightning, andare su Portafogli > Lightning. Quindi, dato che il vostro nodo LND è già presente su Umbrel, è sufficiente fare clic sul pulsante "Salva" per convalidare la connessione tra il vostro BTCPAY SERVER e il vostro LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Creare e pagare le fatture



In Interface BTCPAY SERVER, passare a Fatture > Crea Invoice. Immettere l'importo, aggiungere una descrizione opzionale e fare clic su Crea.



![Création d'une nouvelle facture](assets/fr/10.webp)



È quindi possibile fare clic sul pulsante "Checkout" per visualizzare il Invoice. BTCPay genera quindi un Invoice con un codice QR unificato (BIP21) contenente il Bitcoin Address e il Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Il cliente può scansionare il codice QR con qualsiasi Wallet compatibile.



![Page de paiement avec QR code](assets/fr/12.webp)



Una volta pagato, il Invoice diventa "Settled" in pochi secondi per Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Gestione e tracciamento dei pagamenti



Nella sezione "Reporting", scheda "Fatture", troverete uno storico completo delle vostre fatture, con data, importo, stato e metodo di pagamento. Se necessario, è possibile esportarlo.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Configurazione del negozio



BTCPAY SERVER consente di gestire più negozi con parametri distinti. Ogni negozio rappresenta un'entità aziendale separata: negozio di e-commerce, punto vendita fisico o fatturazione di servizi.



Nelle impostazioni del negozio sono presenti diverse sezioni importanti:



![Paramètres du magasin](assets/fr/15.webp)





- Impostazioni generali**: Nome del negozio, valuta di riferimento (BTC, EUR, USD), tempo di scadenza Invoice (predefinito 15 minuti), numero di conferme Blockchain richieste
- Tassi**: Configurazione delle fonti dei tassi Exchange e delle conversioni fiat/Bitcoin
- Aspetto della cassa**: Personalizzare l'aspetto delle pagine di pagamento (logo, colori, messaggi personalizzati)
- Impostazioni e-mail**: Configurazione delle notifiche via e-mail per i pagamenti ricevuti
- Token di accesso**: Gestione API token per le integrazioni di e-commerce (WooCommerce, Shopify, ecc.)
- Utenti**: Gestire l'accesso degli utenti al negozio con diversi livelli di autorizzazione (Proprietario, Ospite)
- Webhook**: Configurazione di webhook per la sincronizzazione in tempo reale con il sistema di contabilità o ERP



BTCPAY SERVER offre anche una sezione Plugin per estendere le funzionalità con integrazioni di e-commerce, sistemi di punti vendita e strumenti aggiuntivi.



![Gestion des plugins](assets/fr/16.webp)



## Vantaggi e limiti dell'uso locale



**Benefici del BTCPAY SERVER su Umbrel** :




- Sovranità totale: controllo esclusivo delle chiavi private e dei fondi, nessuna terza parte può bloccare o censurare i vostri pagamenti
- Risparmio sostanziale: solo costi di rete Bitcoin (pochi centesimi su Lightning) contro il 2-3% dei processori tradizionali
- Massima riservatezza: nessuna registrazione, verifica dell'identità o condivisione dei dati con società terze
- L'architettura open-source garantisce trasparenza, verificabilità e sostenibilità attraverso un'ampia comunità di sviluppatori
- Installazione semplice tramite Umbrel, senza necessità di competenze tecniche avanzate



**Limitazioni importanti** :




- Solo rete locale**: BTCPAY SERVER su Umbrel è accessibile solo dalla rete domestica. Perfetto per la fatturazione faccia a faccia, per i servizi dei freelance o per le piccole imprese fisiche, ma non adatto ai negozi online accessibili pubblicamente su Internet.
- Piena responsabilità tecnica: manutenzione dei nodi, backup regolari, monitoraggio della connettività
- Gestione della liquidità fulminea: apertura e gestione di canali con sufficiente capacità in entrata
- L'assistenza si limita alla documentazione e ai forum della comunità, richiedendo maggiore autonomia rispetto a un servizio clienti commerciale



Questa limitazione della LAN è il principale ostacolo all'integrazione del BTCPAY SERVER in un negozio di e-commerce, dove i clienti devono poter accedere alle pagine di pagamento da qualsiasi punto di Internet.



## Migliori pratiche e sicurezza



Attivare i backup automatici di Umbrel e conservarne una copia su un supporto esterno (chiavetta USB, disco Hard, cloud crittografato). Conservare i semi del Bitcoin (frasi di ripristino) in un luogo sicuro e fisicamente separato. Salvare il file channel.backup del LND per il recupero di Lightning.



Monitorare regolarmente la sincronizzazione del Bitcoin core, i canali Lightning e la risposta del BTCPAY SERVER. Un semplice test settimanale: generate e pagare un conto di qualche satoshis. Mantenere Umbrel aggiornato (patch di sicurezza, miglioramenti). Eseguire un backup prima degli aggiornamenti più importanti. Per un uso professionale, considerare un monitoraggio esterno (UptimeRobot) con avvisi via e-mail/SMS.



## Mostra BTCPAY SERVER pubblicamente per un negozio online



Per integrare BTCPAY SERVER in un negozio di e-commerce basato sul web (WooCommerce, Shopify, ecc.), i clienti devono poter accedere alle pagine di pagamento da qualsiasi luogo, non solo dalla rete locale.



**Soluzione: Nginx Proxy Manager**



È possibile esporre pubblicamente BTCPAY SERVER utilizzando Nginx Proxy Manager (disponibile nell'App Store di Umbrel). Questa soluzione richiede :




- Un nome di dominio (classico o gratuito tramite DuckDNS, No-IP, Afraid.org)
- Configurazione del port forwarding (porte 80 e 443) sul router
- Installazione di Nginx Proxy Manager, che gestisce automaticamente i certificati SSL



Questa configurazione espone il server a Internet e richiede una maggiore vigilanza (password forti, 2FA, aggiornamenti regolari). Prepareremo un tutorial dedicato che illustrerà nel dettaglio questa procedura completa.



## Conclusione



BTCPAY SERVER su Umbrel combina la potenza del nodo Bitcoin con la semplicità di Umbrel per creare un'infrastruttura di pagamento professionale self-hosted accessibile a tutti. Questa sovranità finanziaria comporta una responsabilità di manutenzione, ma Umbrel semplifica notevolmente l'onere operativo rispetto ai vantaggi: eliminazione delle commissioni di elaborazione, protezione della privacy, resistenza alla censura e controllo totale dei fondi.



L'uso della rete locale copre già un'ampia gamma di applicazioni: fatturazione di servizi freelance, pagamenti faccia a faccia, piccoli negozi fisici o semplicemente l'apprendimento e la sperimentazione di Bitcoin e Lightning in un ambiente controllato. Per le esigenze di e-commerce che richiedono un'esposizione pubblica, esiste la soluzione Nginx Proxy Manager, ma richiede una configurazione tecnica aggiuntiva, che illustreremo in dettaglio in un tutorial dedicato.



Che si tratti di un'attività commerciale, di un progetto nascente o semplicemente di un esperimento, BTCPAY SERVER su Umbrel offre una completa autonomia finanziaria. Il percorso inizia con un primo negozio, un primo Invoice, un primo pagamento ricevuto direttamente nella vostra infrastruttura sovrana.



## Risorse



### Documentazione ufficiale




- [Sito ufficiale BTCPAY SERVER](https://btcpayserver.org)
- [Documentazione completa BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Documentazione Tailscale](https://tailscale.com/kb)


### Comunità e supporto




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)