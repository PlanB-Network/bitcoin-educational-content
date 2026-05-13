---
name: BTCPay Server
description: Accettare pagamenti in BTC senza intermediari
---

![cover](assets/cover.webp)

![video](https://youtu.be/KqsM-n-e4aY)

BTCPay Server è un pacchetto software gratuito e open-source creato da Nicolas Dorier che consente di accettare pagamenti in bitcoin senza intermediari. Progettato per offrire autonomia e sovranità finanziaria, si installa sul proprio server e fornisce una gestione completa delle transazioni, dalla emissione di invoice alla convalida dei pagamenti on-chain o Lightning Network, fino alla contabilità. Si integra facilmente con i siti di e-commerce (WooComerce, Shopify, ecc.) o può essere utilizzato come terminale di pagamento per i negozi fisici (_POS_).

BTCPay Server è senza dubbio la soluzione più avanzata per gli esercenti che desiderano accettare bitcoin. È il software più completo e robusto in termini di sicurezza, sovranità e riservatezza. D'altro canto, è anche il più complesso da installare e mantenere. Esistono anche alternative più semplici: alcune sono interamente custodial, come OpenNode, mentre altre offrono un interessante compromesso tra facilità d'uso e sovranità, come Swiss Bitcoin Pay:

https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

L'obiettivo di questo tutorial è quello di guidarti passo dopo passo nell'installazione, nella configurazione e nell'utilizzo di BTCPay Server, in modo che tu possa implementare un'infrastruttura di pagamento sicura e indipendente, in linea con l'etica di Bitcoin.


## Caratteristiche del server BTCPay

Le soluzioni centralizzate per i punti vendita Bitcoin, come ad esempio _OpenNode_, offrono facilità d'uso, ma si affidano a una società terza poiché non possono essere self-hosted e sono, nella maggior parte dei casi, proprietarie. Se da un lato facilitano l'impostazione dei pagamenti, dall'altro comportano costi di commissione ed espongono gli utenti a maggiori rischi rispetto a soluzioni come BTCPay Server, sia in termini di custodia dei fondi che di riservatezza.

BTCPay Server si rivolge a commercianti online o fisici, associazioni e organizzazioni no-profit che desiderano ricevere donazioni in bitcoin. È anche una soluzione ideale per i proprietari di progetti e gli sviluppatori che cercano un sostegno diretto dalla loro comunità.

Le caratteristiche speciali di BTCPay Server includono:
- la sua **completa autonomia**;
- l'assenza di una procedura **KYC**;
- **pieno controllo dei fondi**;
- l'**eliminazione delle commissioni di piattaforma**.

Diventando il tuo processore di pagamenti, elimini la dipendenza da una terza parte centralizzata tra te e i tuoi clienti. Potrai accettare pagamenti direttamente in bitcoin e generare invoice di pagamento. Questo garantisce che né tu né la tua azienda possa essere bandita da altri. Svolgi il ruolo di banca e di elaboratore di pagamenti, senza dover pagare commissioni a un intermediario per ogni transazione.

Le commissioni di transazione per transazioni **on-chain** rimangono, ma possono essere ridotte utilizzando la rete **Lightning** o **Liquid**.

Inoltre:
- interfaccia e invoice completamente personalizzabili;
- supporto nativo **Tor** per una maggiore riservatezza;
- supporto per **crowdfunding**, **POS** e **pulsanti di pagamento**;
- compatibile con molte valute;
- pagamenti diretti in bitcoin e peer-to-peer;
- controllo completo delle chiavi private;
- maggiore privacy;
- maggiore sicurezza;
- software self-hosted;
- supporto per **SegWit** e **Lightning Network**;
- wallet interno, basato sui nodi, con integrazione degli hardware wallet.


## Installazione e configurazione del server BTCPay

### Scegliere la modalità di hosting

Il server BTCPay può essere installato in diversi modi. A seconda delle tue esigenze e risorse, esistono tre opzioni principali:
- **Server BTCPay ospitato da terzi**: utilizza una piattaforma che ospita il servizio per te. È semplice, ma di solito non è gratuito.
- **Server BTCPay self-hosted su un server cloud** (ad esempio tramite [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) o qualsiasi altro provider). Questa è la soluzione consigliata per la maggior parte dei commercianti alle prime armi.
- **Server BTCPay installato sul proprio hardware (localmente)**: su un computer, mini-PC o Umbrel. Questo metodo è più tecnico, ma offre una totale indipendenza.

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Per un commerciante in fase di avviamento, la **distribuzione su un server cloud** è il miglior compromesso tra autonomia, semplicità e sicurezza, senza dover gestire l'intera infrastruttura tecnica.

Il server BTCPay può essere distribuito rapidamente da diversi provider di hosting. Tra questi, **Voltage** si distingue come soluzione di riferimento per gli utenti che richiedono un'infrastruttura **affidabile**, **professionale** e **sovranazionale**.

### Creare un'istanza del server BTCPay su Voltage

**Voltage** è una piattaforma di hosting Bitcoin e Lightning chiavi in mano che ti permette di implementare immediatamente il tuo server BTCPay, senza complesse configurazioni o manutenzione del server.

Visita il [sito ufficiale di Voltage](https://voltage.cloud).

![capture](assets/fr/03.webp)

Crea un **account utente** con un indirizzo e-mail valido e una password forte.

![capture](assets/fr/04.webp)

Voltage offre una **prova gratuita di 7 giorni**. Si prega di notare che dopo i 7 giorni di prova gratuita, sarai invitato a sottoscrivere un abbonamento fisso di **25 dollari al mese** per continuare a **mantenere attivi i tuoi nodi**.

Dopo aver creato il tuo account Voltage e aver effettuato il primo accesso, verrai reindirizzato alla pagina iniziale, che presenta due sezioni principali:
- Una sezione **Infrastruttura** per gestire i nodi Lightning, Bitcoin Core, BTCPay Server e altri servizi Bitcoin nel cloud;
- e una sezione **Pagamenti** che consente di accedere alle API Lightning di Voltage per integrare i pagamenti Bitcoin in applicazioni personalizzate.

Per distribuire l'istanza di **BTCPay Server**, fai clic su **Infrastruttura di accesso**. Qui è possibile creare, gestire e monitorare tutti i servizi, compresi il nodo Bitcoin e il server BTCPay.

#### Creare un gruppo

Prima di distribuire un servizio, la piattaforma richiede di **creare un gruppo**. Un **gruppo** (spazio di lavoro) è un'area di lavoro che raggruppa tutti i servizi Bitcoin e Lightning (ad esempio un nodo, un server BTCPay, un explorer e così via). È un po' come una cartella che contiene i vari progetti.

![capture](assets/fr/05.webp)

Ai fini di questa esercitazione, il gruppo che abbiamo creato si chiamerà **Genesis**. Se lo desideri, puoi aggiungere un'immagine del profilo. Una volta fatto questo, clicca sul pulsante **Crea**. È possibile invitare altri utenti a unirsi al gruppo e anche cambiare il nome del gruppo, se lo desideri.

Nella pagina iniziale del gruppo appaiono diverse opzioni:
- **Nodi Lightning** : per distribuire un nodo Lightning completo (LND);
- **Nodi Bitcoin Core** : per lanciare un nodo Bitcoin completo;
- **Server BTCPay** : per ospitare un'istanza BTCPay pronta all'uso;
- **Nostr Accounts**: per gestire le identità Nostr.

Attiva la **doppia autenticazione (2FA)** per proteggere il tuo account e i tuoi servizi (il pulsante è visibile in rosso se è disattivato).

![capture](assets/fr/06.webp)

Fai clic su **BTCPay Server** tra le opzioni, quindi su **Lancia un negozio BTCPay**.

![capture](assets/fr/07.webp)

Voltage ti chiederà quindi di **creare e configurare la tua istanza del server BTCPay** scegliendo un **nome del servizio** (1) e abilitando i pagamenti Lightning (2).

Avrai bisogno di un nodo Lightning se decidi di accettare pagamenti Lightning.

Se non hai già un nodo Bitcoin o Lightning, Voltage ti suggerirà di crearne uno automaticamente.

Clicca su **Crea un nodo Lightning** (3) .

![capture](assets/fr/08.webp)

Una volta entrato nell'interfaccia di creazione dei nodi, ti verrà chiesto di scegliere tra i layout **standard** e **professional**.

È possibile creare un nodo effettivo (**Mainnet**) o un nodo di prova (**Testnet**). Fai quindi clic sul pulsante **Continua**.

![capture](assets/fr/09.webp)

Per questa esercitazione, utilizziamo il piano standard. Inserisci il **nome del nodo**, una **password** e premi il pulsante **Crea**.

![capture](assets/fr/10.webp)

Dopo pochi istanti, il tuo nodo sarà operativo e potrai aprire un canale libero con una capacità di ricezione di 500.000 sats.

![capture](assets/fr/11.webp)

Un po' più in basso sulla destra, troverai tutte le informazioni necessarie sul tuo nodo!

![capture](assets/fr/12.webp)

Ora che il nostro nodo Lightning è attivo e funzionante, torniamo a installare il nostro server BTCPay. Ora è possibile fare clic sul pulsante **Crea BTCPay**.

![capture](assets/fr/13.webp)

Si aprirà una pagina con i dati di accesso predefiniti e un messaggio che invita a modificare la password iniziale. Una volta effettuata questa operazione, fai clic sul pulsante **Login Now** per accedere all'interfaccia.

![capture](assets/fr/14.webp)

Ecco fatto! Il tuo server BTCPay è pronto all'uso. Sarai reindirizzato direttamente alla pagina di accesso del tuo server BTCPay.

![capture](assets/fr/15.webp)

Una volta effettuato l'accesso, configurare il primo **store**:
- Dagli un **nome**.
- Scegli la **valuta predefinita** (EUR, USD, CFA, ecc.).
- Seleziona un **fornitore di tassi di cambio** (ad esempio CoinGecko).

![capture](assets/fr/16.webp)

Verrai quindi reindirizzato alla dashboard del tuo negozio. Nell'interfaccia della dashboard, noterai che il pulsante **Crea il tuo negozio** è contrassegnato in verde, poiché questa fase è già stata completata.

![capture](assets/fr/17.webp)

Poco più in basso si trovano i pulsanti **Configura wallet** e **Configura nodo Lightning**. Nel nostro caso, ci siamo già collegati a un nodo Lightning su Voltage. Quindi non dovremo farlo qui.

Passiamo alla configurazione di un wallet. Fai clic sul pulsante **Configura un portafoglio**.

Dato che abbiamo appena iniziato con il server BTCPay, colleghiamo un wallet esistente. Premi quindi **Collega un portafoglio esistente**.

![capture](assets/fr/18.webp)

È quindi necessario scegliere il **metodo di importazione**. Tra le opzioni disponibili, seleziona **Inserisci chiave pubblica estesa**.

![capture](assets/fr/19.webp)

Collegando un wallet esistente, è possibile ricevere i pagamenti **direttamente su questo wallet esterno**, senza che il server BTCPay abbia accesso alla chiave privata. Quindi, anche se il server venisse violato o la chiave pubblica (`xpub`) compromessa, un aggressore potrebbe visualizzare la cronologia delle transazioni, ma sarebbe **impossibile accedere ai fondi**.

Una volta fatto clic sul pulsante **Inserisci chiave pubblica estesa**, verrai **indirizzato** alla pagina in cui è necessario fornire questa chiave.

Ora recuperiamo la **chiave pubblica estesa**.

### Collegamento di un Bitcoin wallet

Per ricevere i pagamenti, è necessario collegare un Bitcoin wallet al proprio negozio. A tal fine, sono disponibili diverse opzioni:
- **hardware wallet** (Coldcard, Ledger, Trezor,...);
- **software wallet** (Electrum, Sparrow, Blockstream App, Ashigaru...)
- **Server BTCPay** wallet interno (sconsigliato, perché è meno sicuro ed espone maggiormente i tuoi fondi in caso di violazione del server).

In questa esercitazione, utilizzeremo un **software wallet**, più accessibile per la configurazione iniziale. È possibile scegliere tra una serie di applicazioni compatibili: **Electrum**, **Phoenix**, **Zeus**, **Muun**, ecc...

Per la dimostrazione, utilizzeremo **Electrum**. Apri **Electrum**, fai clic su **Wallet**, quindi su **Informazioni**:

![capture](assets/fr/20.webp)

Successivamente, copia la **chiave pubblica principale (xpub)**.

![capture](assets/fr/21.webp)

Una volta copiata la chiave pubblica principale, incollala nell'apposito campo della pagina del server BTCPay.

![capture](assets/fr/22.webp)

Dopo la verifica, sarai reindirizzato alla dashboard del tuo negozio.

![capture](assets/fr/23.webp)

### Generare un punto vendita (PoS)

Dopo aver configurato il tuo negozio e il tuo portafoglio, puoi ora impostare un **Punto vendita (PoS)** per iniziare a ricevere i pagamenti Bitcoin direttamente dai tuoi clienti.

Questa funzione integrata di **BTCPay Server** è ideale per **commercianti, artigiani, ristoratori o fornitori di servizi** che desiderano accettare Bitcoin **senza un sito web** o particolari competenze tecniche.

### Qual è il punto vendita (PoS)?

Il **PoS** è un'**interfaccia POS semplificata** che agisce come un **terminale di pagamento Bitcoin**.

Consente di:
- Creare un **menu di prodotti o servizi** con prezzi fissi.
- Generare un'**invoice istantanea con codice QR** da scansionare.
- Condividere un **URL di pagamento** accessibile tramite smartphone, tablet o computer.

In altre parole, il PoS trasforma il tuo server BTCPay in un'**interfaccia di vendita diretta**, dove ogni pagamento viene ricevuto **nel tuo Bitcoin wallet**, senza intermediari.

### Configurazione del PoS

Nella dashboard di BTCPay, fai clic su **PLUGINS**, quindi su **Point of sale**.

Quindi fai clic su **Crea una nuova applicazione PoS**. Questa azione aggiunge una **nuova applicazione** al tuo negozio BTCPay, come se tu stessi installando un mini sito di vendita interno.

Si apre una pagina per creare l'applicazione. Definisci un **nome dell'applicazione**: si tratta di un nome interno, visibile solo dalla tua dashboard (ad esempio _Shoe Shop_).

Fai clic su **Crea** per convalidare.

![capture](assets/fr/24.webp)

Una volta creato, verrai reindirizzato alla **pagina di configurazione dettagliata** del punto vendita.

### Personalizzare l'interfaccia di vendita

In questa pagina è possibile definire gli elementi essenziali del proprio PoS:
- **Nome dell'applicazione** (nome di gestione interno, modificabile in qualsiasi momento).
- **Titolo del display** (ciò che i clienti vedranno in cima alla pagina).
- **Stile del punto vendita** (la modalità **Descrizione** è adatta a servizi come il taglio dei capelli o i pasti, mentre la modalità **Catalogo prodotti** è ideale per i negozi che offrono diversi articoli).
- **Visualizza valuta** (scegli **XOF**, **EUR** o **USD** in base ai prezzi abituali).
- **Elenco dei prodotti** (aggiungi qui i prodotti, le descrizioni e i prezzi).

![capture](assets/fr/25.webp)

![capture](assets/fr/26.webp)

### Salvate e testate il vostro PoS

Una volta terminata la configurazione, fai clic su **Save** per salvare le impostazioni, quindi su **View** per visualizzare l'anteprima del PoS.

Verrà visualizzata una pagina di presentazione dei prodotti, con ogni pulsante corrispondente a un articolo o servizio.

Non appena un cliente sceglie un prodotto:
1. BTCPay genera automaticamente un'**invoice Bitcoin o Lightning**.
2. Sullo schermo appare un **codice QR**.
3. I clienti possono **scansionare e pagare direttamente** con il loro Bitcoin wallet.

![capture](assets/fr/27.webp)

### Risultato finale

Ora hai un **Punto vendita Bitcoin** completo che puoi:
- aprire da uno smartphone o tablet nel tuo negozio;
- visualizzare su uno schermo per la scansione da parte del cliente;
- condividere eventualmente tramite un **URL** pubblico, come una pagina d'ordine semplificata.

Ad ogni pagamento, l'importo viene accreditato automaticamente sul **tuo wallet** di BTCPay, senza intermediari o commissioni di terzi.

Questo trasforma il tuo PoS in un **terminale di pagamento Bitcoin autonomo**.


## Uso quotidiano

Prima di incassare i pagamenti reali, si consiglia di effettuare **un test** per verificare che tutto funzioni correttamente.

### Testare un pagamento

- **Crea un'invoice** dall'interfaccia PoS (ad esempio, un prodotto da 1 satoshi o un piccolo importo).
- **Esegui la scansione del codice QR** sullo schermo utilizzando un Bitcoin o un Lightning wallet (come **Phoenix**, **Muun** o **Wallet di Satoshi**).

![capture](assets/fr/28.webp)

- **Convalida il pagamento** nel tuo wallet: la transazione viene inviata immediatamente.
- **Ritorna al server BTCPay**: l'invoice apparirà come **Pagata** nell'elenco.

![capture](assets/fr/29.webp)

Congratulazioni! Il tuo punto vendita è ora **funzionante**. Puoi iniziare a ricevere i pagamenti Bitcoin dai tuoi clienti, in modo semplice, rapido e senza intermediari.

### Creare un'invoice per un cliente

Nel menu **Invoice**, fai clic su **Nuova invoice**.

![capture](assets/fr/30.webp)

Inserisci l'**importo** e la **valuta locale** (BTCPay calcola automaticamente l'equivalente in BTC), nonché altre informazioni sul prodotto.

![capture](assets/fr/31.webp)

Condividi il **codice QR** o l'**URL** con il cliente.

![capture](assets/fr/32.webp)

### Tracciare i pagamenti ricevuti

Sempre nel menu **Invoice**, viene visualizzato un elenco di tutte le transazioni.

Gli stati possibili sono:
- **In attesa**: pagamento non ancora confermato.
- **Pagato**: pagamento confermato.
- **Scaduta**: invoice non pagata entro la data di scadenza.

### Rimborso di un cliente

Nel menu **Invoice**, seleziona l'invoice da rimborsare.

![capture](assets/fr/33.webp)

Fai clic su **Rimborso** e inserisci l'indirizzo Bitcoin fornito dal cliente.

![capture](assets/fr/34.webp)

![capture](assets/fr/35.webp)

### Rapporti ed esportazione dei dati

BTCPay Server consente di **esportare le transazioni** (in formato CSV o Excel). Si tratta di un'opzione molto pratica per la contabilità e il registro di cassa.

![capture](assets/fr/36.webp)

Nel menu **Report**, clicca su **Export**: tutte le transazioni verranno salvate in un file CSV, che potrà essere consultato localmente.


## Sicurezza e best practices (buone pratiche)

L'autonomia conferita dal server BTCPay (piena sovranità sui tuoi fondi) è un vero punto di forza. Ma questa libertà comporta una maggiore responsabilità in termini di sicurezza. Gestendo i tuoi pagamenti, assumi il ruolo di banca personale. Ecco perché è indispensabile adottare le migliori pratiche per proteggere i tuoi fondi, i tuoi dati e la tua infrastruttura. Ecco i punti principali da considerare.

### Accesso sicuro al tuo server

- Utilizza una password forte: combina lettere maiuscole e minuscole, numeri e caratteri speciali. Evita di riutilizzare una password esistente.
- Attiva l'autenticazione a due fattori (2FA) per accedere alla tua interfaccia BTCPay.
- Aggiorna regolarmente il sistema operativo, l'istanza del server BTCPay e le dipendenze (Docker, nodo Bitcoin, nodo Lightning...). Gli aggiornamenti spesso correggono le vulnerabilità di sicurezza.

### Gestione e backup delle chiavi private

- Salva le chiavi private e le seedphrases offline, su supporti fisici (carta o metallo).
- Utilizza preferibilmente un hardware wallet.
- Conserva diverse copie dei tuoi backup, in luoghi fisici separati e protetti.

### Pagamenti sicuri e riservatezza

- Utilizza la rete Tor o una VPN per nascondere l'indirizzo IP del tuo server e proteggere la tua privacy.
- Disattiva le porte non necessarie sul tuo server e limitate le connessioni SSH solo agli indirizzi affidabili.
- Attiva HTTPS (certificato SSL) per tutte le connessioni all'interfaccia web di BTCPay.
- Non condividere mai la tua interfaccia di amministrazione con personale non addestrato alla gestione del wallet Bitcoin.

### Implementazione delle migliori pratiche per la rete Lightning

Il tuo negozio è collegato a un **nodo Lightning ospitato su Voltage**, che semplifica notevolmente la gestione tecnica della rete. Resta comunque importante adottare **best practices (buone pratiche) di monitoraggio e sicurezza**:
- **Salva il login e le chiavi di accesso API** del nodo di Voltage (che consentono la connessione a BTCPay).
- **Proteggi il tuo account Voltage** con l'autenticazione a due fattori e una password forte.
- **Monitora lo stato dei nodi e dei canali** dalla dashboard di Voltage: ciò consente di individuare eventuali anomalie o desincronizzazioni.
- **Evita di condividere le credenziali API** o di esporle pubblicamente (ad esempio nel codice del sito).
- In caso di migrazione, è sufficiente **riconfigurare il collegamento tra BTCPay e Voltage**: non è necessario chiudere manualmente alcun canale.

Con Voltage, benefici di un'infrastruttura **sicura, altamente disponibile** e con **back-up automatico**, mantenendo la **piena sovranità sui tuoi pagamenti Lightning**.

### Organizzare e strutturare le procedure interne

- Definisci una chiara politica di gestione degli accessi: chi può creare un'invoice, visualizzare i pagamenti, accedere al nodo, ecc.
- Documenta le procedure di backup e ripristino per poter reagire rapidamente in caso di incidente.
- Verifica regolarmente il ripristino dei tuoi backup per assicurarti che funzionino correttamente.
- Forma il personale o i collaboratori sulla sicurezza operativa di base: vigilanza contro il phishing, uso di password sicure, rispetto della riservatezza.

### Supervisionare e stabilire la manutenzione continua

- Monitora costantemente l'attività del server utilizzando strumenti di registrazione o di monitoraggio.
- Programma una revisione periodica della sicurezza: controllare gli aggiornamenti, gli accessi, i backup e la coerenza delle transazioni.

Congratulazioni! Sei arrivato alla fine di questo tutorial. Ora è possibile utilizzare il server BTCPay da solo, rendendo più facile la gestione del tuo negozio.

Per saperne di più, ti consiglio di seguire il nostro corso di formazione completo sull'integrazione del Bitcoin nella tua azienda:

https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a
