---
name: Blitz Wallet
description: Il portafoglio Bitcoin più semplice.
---

![cover](assets/cover.webp)

L'esperienza utente è uno dei fattori decisivi nella scelta di un portafoglio Bitcoin. In questo tutorial vi presentiamo Blitz Wallet, un portafoglio che pone la semplicità al centro del suo approccio: grazie all'integrazione del protocollo **Spark**, Blitz vi offre uno dei portafogli Bitcoin più semplici e completi sul mercato, con pagamenti istantanei e senza gestione tecnica.

## Cos'è Blitz Wallet?

Blitz Wallet è un portafoglio Bitcoin **self-custodial** e **open source**, che punta sulla vostra sovranità e su un'esperienza utente fluida e intuitiva.

[Blitz Wallet](https://blitz-wallet.com/) è un'applicazione mobile disponibile su Android (Play Store) e iOS (App Store).

A differenza dei portafogli Lightning tradizionali che richiedono la gestione di canali di pagamento e della liquidità in entrata, Blitz Wallet si basa sul **protocollo Spark** per eliminare queste complessità tecniche. Risultato: pagamenti istantanei fin dal primo satoshi ricevuto, senza alcuna configurazione preliminare. L'obiettivo di Blitz è rendere i pagamenti in bitcoin semplici come un'applicazione di pagamento classica, senza mai compromettere la self-custody dei vostri fondi.

Blitz Wallet supporta anche gli **indirizzi leggibili** nel formato `utente@dominio.com` (tramite LNURL), permettendo di inviare bitcoin con la stessa facilità di un'e-mail, senza dover manipolare lunghe invoice o QR code ad ogni transazione.

## Comprendere il protocollo Spark

Prima di passare alla pratica, è utile comprendere la tecnologia che fa funzionare Blitz Wallet sotto il cofano: il **protocollo Spark**.

### Cos'è Spark?

Spark è un protocollo di secondo livello open source costruito su Bitcoin, sviluppato dal team di Lightspark. Permette di effettuare transazioni istantanee e a basso costo, preservando al contempo la self-custody dei vostri bitcoin.

A differenza del Lightning Network che si basa su **canali di pagamento** tra due parti, Spark utilizza una tecnologia chiamata **statechain** (catena di stato). Il principio fondamentale è il seguente: invece di spostare i bitcoin sulla blockchain ad ogni transazione, Spark trasferisce il **diritto di spesa** da un utente all'altro, senza movimenti on-chain.

### Come funziona?

Per comprendere Spark in modo intuitivo, immaginiamo che spendere un bitcoin su Spark richieda di completare un puzzle a due pezzi:
- Un pezzo è detenuto dall'utente (ad esempio, Alice).
- L'altro pezzo è detenuto da un gruppo di operatori chiamato **Spark Entity (SE)**.

Solo la combinazione dei due pezzi corrispondenti permette di spendere i bitcoin.

Quando Alice vuole inviare i suoi bitcoin a Bob, ecco cosa succede: viene creato un nuovo puzzle congiuntamente tra Bob e il SE. Il puzzle mantiene la stessa forma, ma i pezzi che lo compongono cambiano. D'ora in poi, è il pezzo di Bob che corrisponde a quello del SE. Il vecchio pezzo di Alice diventa inutilizzabile, poiché il SE ha distrutto il suo pezzo corrispondente. La proprietà dei bitcoin è passata di mano, **senza alcuna transazione sulla blockchain**.

Bob può poi ripetere lo stesso processo per inviare questi bitcoin a Carol, e così via. Ogni trasferimento funziona per sostituzione dei pezzi del puzzle, non per un movimento di fondi on-chain.

### Perché è sicuro?

Una domanda legittima si pone: cosa succede se il SE non distrugge realmente il suo vecchio pezzo?

La Spark Entity non è un'entità unica: è un gruppo di operatori indipendenti. Il pezzo del SE non è mai detenuto da un singolo operatore. La sostituzione del puzzle richiede la cooperazione di più operatori. È sufficiente che **un solo operatore sia onesto** durante un trasferimento per impedire la riattivazione di un vecchio puzzle. Nessun operatore isolato può segretamente conservare un vecchio puzzle attivo o ricrearlo successivamente.

Inoltre, Spark integra un meccanismo di uscita unilaterale: potete sempre recuperare i vostri bitcoin on-chain senza la cooperazione del SE. Questo meccanismo di sicurezza è parte integrante dell'architettura di Spark e garantisce che non siate mai dipendenti dalla rete per accedere ai vostri fondi.

### Spark vs Lightning Network

Spark e Lightning non sono in concorrenza: sono **complementari**. Blitz Wallet integra entrambi, permettendovi di beneficiare dei vantaggi di ciascuno.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Tecnologia**                | Statechains (catene di stato)| Canali di pagamento   |
| **Gestione dei canali**       | Non richiesta                | Richiesta             |
| **Liquidità in entrata**      | Non richiesta                | Richiesta             |
| **Transazioni istantanee**    | Sì                           | Sì                    |
| **Self-custody**              | Sì                           | Sì                    |
| **Compatibilità Lightning**   | Sì (tramite atomic swaps)    | Nativo                |

Il Lightning Network resta un eccellente protocollo per i pagamenti istantanei, ma impone vincoli tecnici (gestione dei canali, liquidità in entrata, nodo online...) che possono scoraggiare i principianti. Spark elimina questi vincoli rimanendo compatibile con Lightning.

## Installazione e configurazione

In questo tutorial ci basiamo sulla versione Android di Blitz Wallet, ma tutti i processi presentati di seguito sono ugualmente validi su iOS.

![installation](assets/fr/01.webp)

Essendo Blitz Wallet un portafoglio in self-custody, avete la scelta tra **creare un nuovo portafoglio** o **importare una frase di recupero** (12 o 24 parole) da un portafoglio esistente.

Qui partiamo dalla creazione di un nuovo portafoglio. Trovate di seguito le nostre raccomandazioni sul backup della vostra frase di recupero:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **IMPORTANTE**: Queste 12 o 24 parole di recupero sono **l'unica chiave di accesso ai vostri bitcoin**. Blitz è un portafoglio self-custodial: né Blitz né Spark hanno accesso alla vostra frase di recupero né ai vostri fondi. Se perdete queste parole, perderete definitivamente l'accesso ai vostri bitcoin. Non condividetele con nessuno: chiunque le possieda può spendere i vostri bitcoin.

Create poi un **codice PIN** per proteggere l'accesso al vostro portafoglio.

![setup-wallet](assets/fr/02.webp)

## Iniziare con Blitz

Effettuare transazioni con Blitz è più intuitivo che nella maggior parte degli altri portafogli Bitcoin. L'interfaccia è minimalista e incentrata su tre azioni principali: inviare, scansionare e ricevere.

### Ricevere bitcoin

Per ricevere bitcoin sul vostro portafoglio Blitz, cliccate sull'icona **"Freccia giù"** (↓), inserite l'importo in satoshi che desiderate ricevere, aggiungete una descrizione opzionale, e il portafoglio genererà una fattura (invoice) che potrete condividere con il vostro mittente.

⚠️ **NOTA**: Il satoshi (o "sat") è la più piccola unità di bitcoin: **1 bitcoin = 100 000 000 satoshi**.

Una delle particolarità di Blitz Wallet è che supporta diverse reti e protocolli dell'ecosistema Bitcoin:

- **Lightning Network**: Uno dei livelli superiori di Bitcoin che permette di effettuare micropagamenti istantaneamente con commissioni molto basse. Ideale per i piccoli importi quotidiani.

- **Bitcoin (on-chain)**: La blockchain principale del protocollo Bitcoin, adatta per transazioni di importi più elevati dove la massima sicurezza e la finalità sono prioritarie.

- **Liquid Network**: Una sidechain (catena parallela) di Bitcoin sviluppata da Blockstream, che permette transazioni rapide e confidenziali utilizzando Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Per impostazione predefinita, Blitz genera una fattura Lightning, ma potete scegliere la rete sulla quale desiderate ricevere i vostri satoshi cliccando sul pulsante **"Choose format"** (Scegli il formato).

![receive-sats](assets/fr/03.webp)

### Creare contatti

Blitz Wallet semplifica l'invio ricorrente di bitcoin grazie al suo sistema di contatti.

Nel menu **Contacts**, potete registrare nomi utente Blitz o indirizzi Lightning (LNURL) con i quali interagite frequentemente.

Potrete così inviare satoshi a questi indirizzi in pochi clic, senza dover scansionare un QR code o inserire manualmente un indirizzo ogni volta.

### Inviare bitcoin

Oltre ai metodi classici di invio di bitcoin (scansione di QR code, inserimento manuale dell'indirizzo), Blitz propone diverse opzioni pratiche:

- **Da un'immagine** (*From Image*): Importate un QR code dalla vostra galleria foto.
- **Dagli appunti** (*From Clipboard*): Incollate un indirizzo o una fattura copiata in precedenza.
- **Inserimento manuale** (*Manual Input*): Inserite direttamente un indirizzo Bitcoin, una fattura Lightning o un indirizzo leggibile (ad esempio `utente@walletofsatoshi.com`).
- **Dai vostri contatti**: Selezionate un destinatario pre-registrato per inviare in pochi clic.

Nel menu **Wallet**, cliccate sul pulsante **"Freccia su"** (↑), scegliete il vostro metodo di invio, inserite l'importo da inviare, aggiungete una descrizione e confermate la transazione.

L'importo minimo per effettuare un invio è attualmente di **1 000 satoshi**.

![send-bitcoin](assets/fr/05.webp)

## Il negozio Blitz

Oltre alle operazioni di trasferimento di bitcoin, Blitz Wallet integra un negozio nel quale potete spendere i vostri bitcoin per acquistare servizi digitali direttamente dall'applicazione.

Dal menu principale, cliccate sulla scheda **Store** per accedere al negozio. Vi troverete anche un accesso alla piattaforma **Bitrefill** che permette di acquistare carte regalo presso migliaia di commercianti in tutto il mondo, direttamente in bitcoin.

- **Intelligenza artificiale**: Accedete agli ultimi modelli di IA generativa (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) e pagate i vostri crediti direttamente in satoshi. Diversi piani sono disponibili in base alle vostre esigenze (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS anonimi**: Inviate e ricevete SMS in tutto il mondo senza rivelare il vostro numero di telefono personale. Il servizio è fatturato in satoshi per ogni messaggio inviato.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Proteggete la vostra privacy online sottoscrivendo un abbonamento VPN WireGuard (settimanale, mensile o trimestrale), pagabile in bitcoin direttamente dal negozio Blitz. Vi basterà scaricare l'applicazione client WireGuard sul vostro dispositivo per utilizzarlo.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet dietro le quinte: approfondimento

Dietro la semplicità d'uso di Blitz Wallet si nasconde un'architettura tecnica ben progettata che combina diversi livelli dell'ecosistema Bitcoin.

### La ripartizione del vostro saldo

Blitz Wallet gestisce il vostro saldo in modo trasparente distribuendo i vostri fondi tra i diversi protocolli in base alle necessità. Quando il vostro saldo è inferiore a 500 000 satoshi, Blitz utilizza il **Liquid Network** e gli scambi atomici (*atomic swaps*) per offrirvi un'esperienza fluida e permettere transazioni sul Lightning Network anche con piccoli importi.

Questo approccio garantisce un avvio semplice per i nuovi utenti, senza che debbano comprendere i meccanismi sottostanti. Potete consultare la ripartizione del vostro saldo tra i diversi livelli nel menu **Impostazioni > Balance Info**.

![balance](assets/fr/09.webp)

### La modalità Lightning (opzionale)

Per impostazione predefinita, Blitz Wallet utilizza il Liquid Network e il protocollo Spark per offrirvi un'esperienza fluida senza configurazione tecnica. Tuttavia, Blitz vi dà la possibilità di attivare la **modalità Lightning** che aprirà automaticamente un canale di pagamento quando raggiungerete un saldo di **500 000 satoshi** (0,005 BTC).

Per attivare la modalità Lightning, andate nelle **Impostazioni**, poi nella sezione **Impostazioni Tecniche**, cliccate sull'opzione **Node Info**.

![enable-lightning](assets/fr/10.webp)

Grazie al protocollo Spark, questa attivazione è **opzionale**: Spark permette già di effettuare pagamenti compatibili con Lightning senza dover aprire canali né gestire liquidità in entrata. La modalità Lightning nativa resta utile per gli utenti avanzati che desiderano disporre del proprio nodo Lightning integrato all'interno dell'applicazione.

### Punto vendita (PoS)

Blitz Wallet integra una funzionalità di **punto vendita** che permette ai commercianti di accettare pagamenti in bitcoin direttamente dall'applicazione.

Nel menu **Impostazioni > Point-of-sale**, potete configurare:

- L'identificativo unico del vostro negozio
- La valuta fiat locale nella quale visualizzare i prezzi
- Le istruzioni per i vostri dipendenti
- L'opzione mancia per i vostri clienti

I vostri clienti dovranno semplicemente scansionare il QR code generato per effettuare il pagamento in bitcoin, in modo istantaneo.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Risorse utilizzate per la redazione di questo tutorial:
- Blog di [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
