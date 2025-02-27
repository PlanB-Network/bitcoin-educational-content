---
name: Lipa
description: Impostazione e utilizzo del portafoglio mobile Lipa lightning
---
![cover](assets/cover.webp)

Un portafoglio Bitcoin Lightning è un'applicazione mobile che consente transazioni istantanee e a basso costo sulla rete Lightning di Bitcoin. A differenza delle transazioni sulla blockchain principale (on-chain), i pagamenti Lightning sono quasi istantanei e richiedono commissioni minime, il che li rende particolarmente adatti ai piccoli pagamenti quotidiani.

I portafogli Lightning, come tutti i portafogli mobili, sono considerati portafogli "caldi" perché sono connessi a Internet. Sono quindi destinati principalmente alla gestione di piccole somme di denaro per le spese quotidiane. Per importi maggiori, è preferibile utilizzare soluzioni di archiviazione più sicure, come i portafogli hardware.

Se volete saperne di più sulla rete Lightning e capire come funziona tecnicamente, vi consiglio di seguire questo corso:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
In questo tutorial daremo un'occhiata a **Lipa**, un portafoglio Lightning semplice ed efficace sviluppato in Svizzera.

## Presentazione di Lipa

Lipa è un portafoglio Lightning non custodiale che si distingue per la semplicità d'uso e l'interfaccia ordinata. Sviluppato da un team svizzero, pone l'accento sulla riservatezza e sulla facilità d'uso per i principianti.

Le caratteristiche principali includono:


- Interfaccia utente intuitiva
- Gestione autonoma del canale Lightning
- Supporto del protocollo LNURL
- Possibilità di acquistare bitcoin direttamente nell'applicazione

## Installazione e configurazione di Lipa

Il primo passo è scaricare l'applicazione Lipa. Per il momento è disponibile solo su iOS:


- [Per Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

La versione per Android è attualmente in fase di sviluppo e sarà presto disponibile.

![Installation de Lipa](assets/fr/01.webp)

Una volta avviata l'applicazione, si arriva alla schermata iniziale, che offre due opzioni:


- Creare un nuovo portafoglio
- Ripristinare un portafoglio esistente da un backup

Una volta scelta l'opzione, l'applicazione richiede di attivare le notifiche. Questo passo è importante, poiché le notifiche sono necessarie per :


- Ricevere avvisi quando vengono ricevuti i pagamenti, anche quando l'applicazione è chiusa
- Essere informati sui passi da compiere per acquistare bitcoin attraverso la loro soluzione integrata

L'applicazione presenta quindi le sue funzioni principali attraverso una serie di schermate introduttive:


- Ricezione dei pagamenti senza problemi**: Gli utenti possono ricevere pagamenti in Bitcoin anche quando l'applicazione è chiusa, garantendo affidabilità e convenienza.
- Indirizzi Lightning non custodiali**: Lipa ora supporta gli indirizzi Lightning non custodiali, migliorando la privacy e la sicurezza e dando agli utenti il pieno controllo sui loro bitcoin.
- Controllo sui dati analitici** : Con la massima trasparenza e riservatezza, gli utenti possono visualizzare i tipi di dati raccolti e scegliere le loro preferenze di condivisione.
- Invia tramite numero di telefono**: Non c'è bisogno di indirizzi complessi: basta selezionare un contatto, inserire l'importo e inviare bitcoin direttamente al suo numero di telefono.

L'applicazione beneficia inoltre di continui miglioramenti in termini di stabilità, sicurezza e affidabilità, per garantire un'esperienza utente ottimale.

## Navigazione dell'applicazione

L'interfaccia di Lipa è organizzata in 4 schede principali accessibili tramite la barra di navigazione nella parte inferiore dello schermo:

![Navigation principale](assets/fr/02.webp)


- Home**: Visualizza il saldo corrente e la cronologia delle transazioni
- Scanner**: Consente di scansionare i codici QR per effettuare pagamenti
- Mappa**: Visualizza una mappa interattiva delle aziende che accettano Bitcoin nella vostra zona
- Impostazioni**: Accesso alle impostazioni dell'applicazione, al backup e alle preferenze

È possibile accedere a un menu aggiuntivo tirando verso il basso la schermata iniziale:

![Menu supplémentaire](assets/fr/03.webp)

Questo gesto rivela funzioni aggiuntive come :


- Acquistare bitcoin
- Deposito di bitcoin sulla catena
- Creazione di fatture Lightning per ricevere bitcoin
- Pagamento fulmineo della fattura

## Salvate il vostro portafoglio

Per eseguire il backup del portafoglio, accedere alla scheda "Impostazioni" e selezionare "Frase di recupero". Lipa utilizza una frase di recupero che è essenziale scrivere accuratamente su un supporto fisico (carta, metallo). Questa frase è l'unico modo per recuperare i fondi in caso di smarrimento o furto del telefono. Per convalidare il backup, l'applicazione chiederà di confermare 3 parole a caso della frase.

![Backup](assets/fr/04.webp)

Per ulteriori informazioni su come eseguire correttamente il backup e gestire la frase di ripristino, vi consiglio di seguire quest'altra guida, soprattutto se siete principianti:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Ricevere bitcoin

Per ricevere bitcoin, sono disponibili due opzioni. Per accedere a queste opzioni, tornare alla schermata iniziale e abbassare lo schermo. A questo punto è possibile scegliere tra :


- Selezionare "Transfer BTC" per ricevere bitcoin on-chain. Quindi è sufficiente scansionare il codice QR con l'altro portafoglio e completare la transazione.
- Selezionate "Richiedi" per ricevere tramite la rete Lightning e inserite l'importo che desiderate ricevere.

In entrambi i casi, dovrete pagare una commissione pari allo 0,4% dell'importo, o circa 2.500 sats se l'applicazione deve aprire un nuovo canale di pagamento (come inevitabilmente accadrà per il primo pagamento).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Inviare bitcoin

Per inviare bitcoin, accedere alla schermata iniziale, abbassare lo schermo e selezionare "Paga". Quindi, è sufficiente inviare i bitcoin a :


- inserire un indirizzo LNURL fulminante
- scansionare un codice QR fulmineo per effettuare il pagamento.

È anche possibile accedere alla seconda scheda in fondo allo schermo per scansionare direttamente un codice QR.

![Envoi de bitcoins](assets/fr/07.webp)

## Acquistare bitcoin

Lipa offre la possibilità di acquistare bitcoin direttamente nell'applicazione con una commissione dell'1,5%. Per effettuare un acquisto, accedere alla schermata iniziale e tirare verso il basso per visualizzare il menu. Selezionare quindi "Acquista BTC". Tre schermate introduttive vi guideranno attraverso il processo di acquisto.

![Menu d'achat](assets/fr/08.webp)

Quindi è sufficiente inserire le coordinate bancarie del conto che utilizzerete per effettuare l'acquisto. Scegliete la valuta e inserite il vostro indirizzo e-mail.

Dopo la schermata di caricamento, troverete il numero di riferimento da inserire nel bonifico che state per effettuare, nonché le coordinate bancarie per il cambio.

![Sélection du montant](assets/fr/09.webp)

Tutto ciò che dovete fare è utilizzare la vostra banca per trasferire l'importo desiderato, impostare il trasferimento indicando il RIB precedentemente recuperato e indicare il riferimento al momento della transazione in modo che Lipa possa associare questo movimento bancario al vostro portafoglio Lipa.

![Confirmation d'achat](assets/fr/10.webp)

## Vantaggi e svantaggi

### Vantaggi


- Interfaccia intuitiva
- Corrispondenza corretta dei costi di servizio
- Non custodiale
- Soluzione integrata per l'acquisto di bitcoin
- Integrazione di BTCmap
- Supporto NFC

### Svantaggi


- Non è possibile inviare bitcoin sulla catena
- Pagamento leggermente più lungo della media

Lipa è una scelta eccellente per iniziare a utilizzare la rete Lightning, particolarmente adatta agli utenti che cercano una soluzione semplice per i pagamenti quotidiani. La sua facilità d'uso e l'interfaccia ordinata lo rendono un portafoglio ideale per i principianti, pur offrendo le funzioni essenziali per l'uso quotidiano di Lightning.

## Risorse


- [Sito ufficiale di Lipa](https://lipa.swiss/)
- [Supporto Lipa](https://getlipa.atlassian.net/servicedesk/customer/portal/1)