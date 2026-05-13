---
name: Tiankii
description: Una suite di strumenti per i rivenditori e i consumatori
---

![cover](assets/cover.webp)

Nell'ecosistema Bitcoin, l'accettazione di pagamenti in tempo reale rimane una sfida importante per aziende e privati. Le soluzioni tradizionali spesso richiedono conoscenze tecniche avanzate, un'infrastruttura complessa da mantenere, o richiedono che i fondi siano detenuti da intermediari. Questa situazione frena l'adozione di massa di Bitcoin come moneta quotidiana, nonostante le promesse dei progressi tecnologici del Lightning Network.

Tiankii, un'azienda salvadoregna nata nel 2021, risponde a questo problema offrendo un'infrastruttura Bitcoin accessibile e modulare. Invece di forzare l'adozione di un ecosistema chiuso, Tiankii offre una suite di strumenti interconnessi che consentono a chiunque di integrare Bitcoin Lightning nella propria attività senza sacrificare il controllo dei propri fondi.


## Che cos'è Tiankii?

### Origine e filosofia

Tiankii - termine Nahuatl che significa "mercato all'aperto accessibile a tutti" - è la prima start-up al 100% Bitcoin di El Salvador. Fondata da Darvin Otero in seguito all'adozione di Bitcoin come moneta legale del Paese, l'azienda mira a trasformare Bitcoin da riserva di valore a moneta di scambio per gli acquisti quotidiani. A differenza delle piattaforme di custodia, Tiankii adotta un approccio non custodiale in cui gli utenti mantengono il controllo dei propri fondi e l'infrastruttura funge solo da intermediario tecnico.

### Architettura tecnica

Tiankii si posiziona come fornitore di un'infrastruttura Bitcoin-as-a-Service basata su Lightning Network. Questa tecnologia di secondo livello consente transazioni quasi istantanee con costi trascurabili, rendendo possibili micropagamenti e acquisti quotidiani.

L'architettura si basa su tre pilastri:

**Lightning-first**: favorire sistematicamente la rete Lightning per la sua velocità e i costi inferiori, mantenendo il supporto alle transazioni on-chain per importi elevati.

**Standard aperti**: uso di LNURL per automatizzare le richieste di pagamento, indirizzi Lightning per ID e-mail leggibili e Bolt Card per pagamenti NFC interoperabili.

**Modularità wallet-agnostica**: possibilità di collegare diversi wallet Lightning (LNbits, Blink, BlueWallet) o il proprio nodo, offrendo la massima flessibilità in base al livello di competenza e autonomia richiesto.


## Strumenti dell'ecosistema Tiankii

### Bitcoin POS - Terminale di pagamento in negozio

L'applicazione trasforma lo smartphone o il tablet in un terminale Lightning. L'esercente inserisce l'importo in valuta locale e l'applicazione genera un codice QR Lightning o accetta una carta Bolt. Le transazioni vengono accreditate istantaneamente senza commissioni, con conversioni automatiche in oltre 150 valute, gestione delle mance e storico delle vendite.

### Merchant Dashboard - Gestione unificata delle vendite

Interface web centralizzato per collegare i propri wallet Lightning, tracciare le transazioni in tempo reale, emettere fatture e generare report contabili. La piattaforma aggrega tutti i canali: pagamenti in negozio (POS), vendite online (plug-in di e-commerce) o integrazioni API . I pagamenti convergono sul wallet scelto.

### Carta Contactless Bitcoin (carta Bolt)

La carta NFC Bolt rappresenta la principale innovazione di Tiankii nella democratizzazione di Bitcoin per il pubblico. Funzionando come una carta bancaria contactless, consente di pagare gli acquisti Bitcoin Lightning semplicemente toccando un terminale compatibile.

A differenza delle tradizionali soluzioni di custodia, questa carta segue uno standard aperto che garantisce l'interoperabilità. Gli utenti possono collegarla al proprio wallet tramite l'applicazione IBI, mantenendo così le proprie chiavi private e il pieno controllo sui fondi associati. Il pagamento avviene in un secondo, senza bisogno di tirare fuori lo smartphone o di avere una connessione internet attiva al momento del pagamento.

Questa soluzione è particolarmente inclusiva per le persone che non hanno familiarità con gli smartphone, offrendo una porta d'accesso accessibile all'economia Bitcoin.

### App IBI - Interfaccia individuale Bitcoin

L'applicazione IBI (Individual Bitcoin Interface) è progettata per le persone che desiderano utilizzare Bitcoin Lightning su base quotidiana. Il suo principale vantaggio consiste nella generazione di un indirizzo Lightning personalizzato, un identificativo di pagamento leggibile in formato e-mail (esempio: alice@ibi.me).

Questo identificatore semplifica drasticamente la ricezione dei pagamenti: non c'è bisogno di generare una nuova invoice per ogni transazione, il mittente può semplicemente inserire l'indirizzo Lightning. L'interfaccia consente inoltre di gestire la carta Bolt (attivazione, disattivazione, limiti di spesa), di collegare vari wallet Lightning e di effettuare pagamenti tramite la scansione di codici QR.

### Plugin per il commercio elettronico

Integrazioni pronte all'uso per WooCommerce, Shopify e Cloudbeds. Si installa in pochi minuti per aggiungere Bitcoin Lightning al checkout. Vantaggi: zero commissioni (contro il 2-3% delle carte di credito), regolamento istantaneo, accesso in tutto il mondo, eliminazione dei chargeback. I pagamenti arrivano direttamente sul wallet collegato al commerciante.

### Bitcoin API e strumenti per gli sviluppatori

L'SDK Tiankii consente di integrare Bitcoin Lightning nelle applicazioni esistenti senza dover mantenere un proprio nodo. API gestisce la creazione di invoice, la verifica dei pagamenti e gli invii di massa tramite una solida infrastruttura ospitata su Google Cloud. Command Center completa l'offerta per le organizzazioni con indirizzi Lightning su domini personalizzati, pagamenti in blocco e gestione centralizzata di terminali e carte NFC.


## Installazione e primi passi

### Prerequisiti essenziali

L'utilizzo di Tiankii non richiede prerequisiti tecnici complessi. Le applicazioni funzionano tramite un browser web su smartphone, tablet o computer. Non è richiesta l'installazione di un'applicazione nativa: tutto ciò che serve è un accesso a Internet e un browser recente per accedere a IBI o al Merchant Dashboard.

**Per gli utenti privati (App IBI)**: Non è necessario avere già un wallet Lightning. Quando si crea un account, Tiankii configura automaticamente un indirizzo Lightning funzionante tramite [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), un'implementazione nodeless che utilizza la rete Liquid in background. È possibile ricevere e inviare immediatamente pagamenti senza alcuna configurazione tecnica. Questa soluzione semplifica drasticamente l'accesso ai principianti, pur rimanendo self-custodial.

**Per gli esercenti (Merchant Dashboard)**: La connessione di un wallet Lightning già esistente è obbligatoria per utilizzare i terminali del punto vendita e ricevere pagamenti. Tiankii supporta molte soluzioni: wallet mobili (Blink, Strike), soluzioni self-hosted (LNbits, nodo LND/CLN) o wallet web (Alby). Le guide dettagliate alla connessione sono disponibili nella sezione Risorse di questo tutorial.

### Per i clienti privati: App IBI

**Creazione di un account**

Vai su accounts.ibi.me per creare il tuo conto. In questa pagina è possibile scegliere tra due tipi di account: "Uso personale" per uso individuale o "Uso commerciale" per uso commerciale. Seleziona "Uso personale" per accedere agli strumenti per la ricezione e l'invio di pagamenti in bitcoin.

![Choix du type de compte](assets/fr/01.webp)

Dopo aver selezionato "Uso personale", sarete automaticamente reindirizzati a go.ibi.me per completare la registrazione. La registrazione può essere effettuata tramite e-mail, numero di telefono o utilizzando il proprio account Google, Microsoft o Twitter. Una volta creato, potrete accedere immediatamente alla tua interfaccia IBI, con il tuo indirizzo Lightning già operativo.

![Création du compte](assets/fr/02.webp)

**Interfaccia principale**

L'interfaccia di IBI visualizza il saldo in satoshi e in valuta locale (USD). Tre pulsanti consentono di interagire: "Ricevi" per ricevere pagamenti, "Scansiona" per scansionare un codice QR e "Invia" per inviare satoshi.

![Interface IBI](assets/fr/03.webp)

**Ricevere il pagamento**

Per ricevere i satoshi, premi "Ricevi". L'applicazione genera automaticamente un codice QR e visualizza il tuo indirizzo Lightning personalizzato (formato nome@ibi.me). Condividi questo indirizzo o il codice QR con il mittente: i fondi arriveranno immediatamente sul tuo conto IBI.

![Réception avec Lightning Address](assets/fr/04.webp)

Una volta accreditato il saldo, è possibile utilizzare questi satoshi per effettuare i pagamenti.

**Inviare un pagamento**

Per inviare i satoshi, premi "Invia". È possibile scansionare un codice QR Lightning o inserire direttamente una destinazione come un indirizzo Lightning.

![Solde et boutons IBI](assets/fr/05.webp)

![Interface d'envoi](assets/fr/06.webp)

Inserisci l'importo desiderato in satoshi, verifica l'importo equivalente in valuta locale e conferma il pagamento.

![Confirmation du montant](assets/fr/07.webp)

Una notifica di successo conferma la spedizione con i dettagli: importo inviato, costo della transazione e destinatario.

![Paiement réussi](assets/fr/08.webp)

**Gestione dei conti**

In Impostazioni è possibile gestire le carte NFC Bitcoin (carte Bolt). L'interfaccia consente di attivare, disattivare o impostare limiti di spesa per le carte.

![Historique des transactions](assets/fr/09.webp)

![Paramètres IBI](assets/fr/10.webp)

### Per gli esercenti: Cruscotto commercianti e POS

**Creazione di un account aziendale**

Vai su accounts.ibi.me per creare il tuo conto. Seleziona "Uso commerciale" per accedere agli strumenti del commerciante. Questo tipo di conto sblocca l'accesso alla Merchant Dashboard e ai terminali dei punti vendita.

Dopo aver selezionato "Uso commerciale", si verrà automaticamente reindirizzati alla Merchant Dashboard (pay.tiankii.com). In questo modo si accede all'interfaccia di gestione dell'attività con il monitoraggio delle entrate, le transazioni e gli strumenti di pagamento. Per iniziare ad accettare pagamenti, è necessario collegare il proprio wallet Lightning cliccando sul link in cima alla pagina (vedi freccia nell'immagine).

![Dashboard marchand](assets/fr/11.webp)

*Connessione* **wallet Lightning**

Passo fondamentale per l'attivazione del punto vendita: collega il wallet Lightning per ricevere i pagamenti. L'interfaccia offre diverse opzioni di connessione. Si noti che alcune opzioni (Bitcoin Onchain e Lightning Network) sono ancora in fase di sviluppo e appaiono in grigio sull'interfaccia.

![Options de connexion wallet](assets/fr/12.webp)

Per questa esercitazione, utilizzeremo la connessione degli indirizzi Lightning, compatibile con Chivo, Blink Wallet e Strike. Inserisci il tuo indirizzo Lightning (formato nome@domaine.com), ad esempio da LN Markets, Alby o qualsiasi altro fornitore compatibile.

![Saisie de la Lightning Address](assets/fr/13.webp)

Una volta effettuato l'accesso, l'account è operativo. È ora possibile accedere al POS o tornare alla dashboard per configurare altre impostazioni.

![Connexion réussie](assets/fr/14.webp)

**Link di pagamento**

Il menu "Strumenti di pagamento" dà accesso a "Richiesta di pagamento", che consente di creare e gestire i link di pagamento. Questa funzione è utile per generare link di pagamento personalizzati da inviare via e-mail o messaggio: donazioni, pagamenti singoli, pagamenti multipli o anche paywall per proteggere i contenuti. È possibile creare diversi tipi di link in base alle proprie esigenze aziendali.

![Liens de paiement](assets/fr/15.webp)

**Configurazione del terminale di vendita**

Per accettare pagamenti in negozio, accedi al menu "Terminale di vendita" da "Strumenti di pagamento". Questa sezione ti permette di creare e gestire i tuoi terminali POS (il numero di terminali dipende dal tuo piano, vedi i piani Freemium e Business). Fai clic su "Apri" per aprire l'interfaccia POS nel browser.

![Gestion des terminaux](assets/fr/16.webp)

**Generare una vendita**

Il terminale POS visualizza un tastierino numerico per l'inserimento dell'importo della vendita. Inserisci l'importo nella valuta locale (ad esempio, 500 sats corrispondono a 630,74 ARS), quindi premere "OK" per confermare.

![Saisie du montant](assets/fr/17.webp)

L'applicazione genera istantaneamente un codice QR Lightning e un'indirizzo Lightning per il pagamento. I clienti possono scansionare il codice QR con il loro wallet o utilizzare la carta Bolt su un terminale NFC.

![QR code de paiement](assets/fr/18.webp)

Non appena il pagamento viene ricevuto, appare una schermata di conferma che mostra l'importo ricevuto in valuta locale e in satoshi. È possibile inviare una ricevuta via e-mail, stampare il biglietto o avviare immediatamente una nuova vendita.

![Paiement encaissé](assets/fr/19.webp)

**Monitoraggio e gestione**

Tutte le transazioni sono registrate nel tuo Merchant Dashboard. È possibile tenere traccia completa dei ricavi per periodo, del numero totale di vendite e dello storico dettagliato per la contabilità.

L'interfaccia delle impostazioni offre diverse schede di configurazione. La scheda "Impostazioni generali" consente di gestire il profilo del commerciante e le notifiche. La scheda "Utenti" consente di aggiungere e gestire l'accesso alla Merchant Dashboard per il tuo team (gestione multiutente in base al tuo piano). La scheda "Spazio di lavoro per lo sviluppo" dà accesso alle chiavi API per le integrazioni avanzate, mentre "Abbonamento" consente di gestire l'abbonamento.

![Paramètres du compte marchand](assets/fr/20.webp)

**Piani gratuiti e piani business**

Tiankii offre due pacchetti per il Merchant Dashboard. Il piano **Freemium** (gratuito) è adatto alle start-up con limitazioni: un solo punto vendita, un solo utente, volume mensile limitato a 1.000 USD e nessun accesso ai connettori di e-commerce. Il piano **Business** (0,5% di commissione per transazione) offre terminali illimitati, utenti illimitati, volume illimitato, accesso ai plugin WooCommerce/Shopify/Cloudbeds ed esclusive notifiche WhatsApp.

![Comparaison plans Freemium et Business](assets/fr/21.webp)


## Vantaggi e vincoli

### Punti salienti

**Autotutela**: mantieni le tue chiavi private e il pieno controllo dei tuoi fondi. Nessun rischio di blocco del conto o di fallimento della piattaforma di terzi.

**Semplicità**: indirizzo Lightning come indirizzo e-mail, pagamenti NFC con un semplice tocco, interfaccia intuitiva senza necessità di competenze tecniche.

**Ecosistema completo**: strumenti per tutti i profili (privati, rivenditori, sviluppatori) con integrazioni modulari per soddisfare le tue esigenze.

**Conformità professionale**: cloud hosting sicuro, conformità PCI-DSS, conformità normativa salvadoregna.

### Limitazioni

**Limiti di sicurezza**: richiede una connessione wallet permanente, gestione della liquidità per grandi volumi, rischio di fallimento se il destinatario è offline. Tiankii mitiga questi aspetti con gli LSP integrati.

**Dipendenza da SaaS**: se Tiankii non è disponibile, la generazione di invoice è temporaneamente impossibile (i tuoi fondi rimangono al sicuro).

**Privacy**: Tiankii può osservare i metadati delle transazioni (importi, date). Meno privato di una soluzione self-hosted come BTCPay Server.


## Conclusione

Tiankii illustra come un'infrastruttura ben progettata possa rimuovere le barriere tecniche che impediscono l'adozione di massa di Bitcoin come valuta quotidiana. Combinando la potenza del Lightning Network con un approccio non custodial e strumenti accessibili, l'ecosistema offre un percorso equilibrato tra sovranità finanziaria e facilità d'uso.

Per gli esercenti, Tiankii rappresenta un'opportunità per ridurre drasticamente i costi delle transazioni e accedere a una nuova base di clienti. Per i consumatori, indirizzi Lightning e le carte NFC trasformano Bitcoin in una moneta pratica, senza complessità tecniche.

Sebbene l'adozione diffusa di Bitcoin rimanga una sfida che richiede formazione e tempo, infrastrutture come Tiankii dimostrano che gli strumenti tecnici esistono già. La missione di semplificare i pagamenti bitcoin non è più una visione lontana, ma una realtà accessibile a chiunque sia disposto a fare il grande passo.


## Risorse

### Documentazione ufficiale

- [Sito ufficiale di Tiankii](https://tiankii.com)
- [Centro assistenza Tiankii](https://help.tiankii.com)
- [Applicazione IBI](https://go.ibi.me)
- [Dashboard commercianti](https://pay.tiankii.com)
- [Centro di comando](https://cc.ibi.me)

### Guide di collegamento Wallet

- [Collegare LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Collegare BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Collegare Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)

### Comunità

- [Lightning Network Plus](https://lightningnetwork.plus) - Risorsa educativa Lightning.
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Iniziativa salvadoregna di economia circolare Bitcoin.

### Strumenti correlati

- [Blink Wallet](https://blink.sv) - Raccomandata la compatibilità con il Wallet Lightning.
- [LNbits](https://lnbits.com) - Soluzione wallet autogestita.
- [Scheda Bolt standard](https://github.com/boltcard) - Specifiche tecniche per le schede NFC.
