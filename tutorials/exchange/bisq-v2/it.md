---
name: Bisq 2
description: Guida completa all'utilizzo di Bisq 2 e allo scambio di bitcoin P2P
---
![cover](assets/cover.webp)

## Introduzione

Gli scambi peer-to-peer (P2P) senza KYC sono essenziali per preservare la riservatezza e l'autonomia finanziaria degli utenti. Permettono di effettuare transazioni dirette tra individui senza la necessità di verificare l'identità, il che è fondamentale per coloro che tengono alla privacy. Per una comprensione più approfondita dei concetti teorici, date un'occhiata al corso BTC204:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Che cos'è Bisq 2?

Bisq 2 è la nuova versione del popolare exchange decentralizzato Bisq, lanciato nel 2024. A differenza del suo predecessore, Bisq 2 è stato sviluppato per supportare più protocolli di scambio, offrendo agli utenti una maggiore flessibilità.

**Nuove caratteristiche principali**


- Supporto per più reti di privacy (Tor, I2P)
- Identità multiple per una maggiore riservatezza
- API REST per i bot di trading
- Supporto per più tipi di wallet
- Sistema di ruoli con deposito obbligatorio in BSQ

Questa guida si concentra esclusivamente su "Bisq Easy", l'unico protocollo attualmente disponibile. Bisq Easy è stato progettato specificamente per i nuovi utenti di Bitcoin. Questo protocollo consente agli utenti di acquistare e vendere Bitcoin scambiando valute fiat su una piattaforma decentralizzata peer-to-peer. Le transazioni sono limitate all'equivalente di 600 USD (con un minimo di 6 USD) e la sicurezza dello scambio si basa sulla reputazione dei venditori di BTC. Bisq Easy non prevede commissioni di trading né richiede un deposito di sicurezza. Bisq Easy dovrebbe sostituire Bisq 1 per gli scambi di denaro al di sotto dei 600 USD (o equivalenti).

**Caratteristiche principali:**

- Applicazione desktop multipiattaforma
- Sono disponibili diversi protocolli di scambio
- Rete P2P decentralizzata
- Attenzione alla riservatezza (nessun KYC, uso di Tor)
- Non custodial (il cliente mantiene il controllo dei propri fondi)
- Open source (AGPL)

### Differenze con Bisq 1

**Per gli acquirenti**


- Non è richiesto alcun deposito cauzionale
- Nessuna commissione di trading
- Nessuna commissione di mining
- Sicurezza basata sulla reputazione del fornitore
- Limiti di trading inferiori (equivalenti a 600 USD)

**Per i venditori**

- Non è richiesto alcun deposito cauzionale
- Ci si può creare una reputazione
- Possibilità di bruciare BSQ o di creare bond in BSQ
- Premium di vendita potenzialmente più alto (10-15% sopra i tassi di mercato)

**Nota importante:** Una volta implementato il protocollo Bisq Multisig in Bisq 2, la vecchia versione di Bisq potrà essere eliminata. Tuttavia, Bisq 1 continuerà a essere utilizzato come strumento di gestione per il CAD Bisq e per gli scambi BSQ-BTC.

### Il processo di scambio

- L'ideatore dell'offerta definisce i termini dello scambio
- Una volta che gli operatori si sono accordati sui termini (metodo di pagamento e prezzo), lo scambio ha inizio
- Il venditore invia le proprie coordinate bancarie all'acquirente, e quest'ultimo invia il proprio indirizzo Bitcoin al venditore
- L'acquirente effettua il pagamento e lo comunica al venditore
- Una volta ricevuto il pagamento, il venditore invia i bitcoin all'indirizzo dell'acquirente
- Lo scambio è completo quando l'acquirente riceve i bitcoin

### Regole importanti

- Prima di scambiare i dati di pagamento, lo scambio può essere annullato senza alcuna giustificazione
- Dopo lo scambio di informazioni, il mancato rispetto degli obblighi può comportare l'esclusione dalla piattaforma
- Per i bonifici bancari, **non utilizzare mai le parole "Bisq" o "Bitcoin"** nella causale di pagamento (ciò potrebbe comportare il blocco dei fondi o addirittura il blocco del conto bancario del destinatario o dell'ordinante)
- I trader devono collegarsi almeno una volta al giorno per seguire il processo
- In caso di problemi, i trader possono ricorrere ai servizi di un mediatore

## Installazione e configurazione

### 1. Scaricare e verificare Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)

- Vai a [bisq.network](https://bisq.network/downloads/)
- Scaricare la versione di Bisq 2 corrispondente al proprio sistema operativo (scorrere la pagina verso il basso)
- Verificare l'autenticità del file scaricato (fortemente consigliato). Per una guida dettagliata alla verifica della firma, vedi la seguente esercitazione:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. Installazione in base al proprio sistema

Seguire i passaggi di installazione adatti al proprio sistema operativo. Se si incontrano difficoltà durante l'installazione, è possibile consultare la guida dettagliata sul [portale wiki ufficiale di Bisq](https://bisq.wiki/Downloading_and_installing).

### 3. Primo avvio

- Avvia Bisq 2 e accetta le condizioni d'uso

![Conditions d'utilisation](assets/fr/01.webp)


- Crea un nuovo profilo scegliendo un nome e un avatar

![Création du profil](assets/fr/02.webp)


- Si accede quindi alla dashboard principale dell'applicazione, dove è possibile lanciare Bisq Easy per acquistare o vendere i primi bitcoin

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Impostazione dei metodi di pagamento

- Accedi alla sezione pagamenti dal menu principale

![Liste des comptes de paiement](assets/fr/04.webp)

- Aggiungi un nuovo metodo di pagamento compilando le informazioni richieste

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

La preconfigurazione dei metodi di pagamento è facoltativa, ma consigliata per risparmiare tempo durante lo scambio. È anche possibile configurare i metodi di pagamento durante una transazione, contattando la controparte dello scambio.

### 5. Sicurezza del conto

**Backup dei dati**

A differenza di Bisq 1, Bisq 2 non integra attualmente un wallet Bitcoin: le transazioni vengono quindi effettuate tramite wallet esterni. Tuttavia, si consiglia di eseguire regolarmente un backup della cartella dati di Bisq 2. Per individuare la cartella dei dati, consultare il [portale wiki ufficiale di Bisq](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Gestione delle identità**

Bisq 2 consente di creare più identità. Ogni identità può essere utilizzata per diversi tipi di transazioni. Le identità vengono memorizzate nella cartella dei dati.

## Comprare e vendere Bitcoin

### Come acquistare Bitcoin

**Opzione 1: approfittare di un'offerta esistente**

- Nella schermata principale, seleziona "Bisq Easy", la scheda "Guida introduttiva", quindi fari clic su "Avvia procedura guidata"

![Lancer trade wizard](assets/fr/06.webp)

- Scegli "Acquista Bitcoin" e seleziona la valuta

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Imposta i metodi di pagamento preferiti (SEPA, Revolut, ecc.)

![Configuration méthodes de paiement](assets/fr/09.webp)

- A questo punto, o si dispone di un elenco di offerte che corrispondono ai criteri precedenti, oppure è necessario accedere all'"Offerbook"

![Liste des offres](assets/fr/10.webp)

- Nel secondo caso, è possibile visualizzare e filtrare le offerte utilizzando i pulsanti in alto a destra dell'interfaccia

![Filtres des offres](assets/fr/11.webp)

- Una volta scelta l'offerta, non resta che scegliere il metodo di pagamento e convalidare il riepilogo dell'operazione

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Opzione 2: Creare la propria offerta**

- Seleziona "Bisq Easy" e poi "Offerbook"
- Scegli le valute dello scambio (ad es. BTC/EUR)
- Fare clic su "Crea offerta"
- Seguire la procedura guidata di creazione dell'offerta: Definire l'importo (fisso o intervallo)

![Configuration du montant](assets/fr/20.webp)

- Seleziona i metodi di pagamento accettati

![Sélection méthodes de paiement](assets/fr/21.webp)

  - Controlla il riepilogo e pubblicare l'offerta

![Récapitulatif et publication](assets/fr/22.webp)

Una volta avviato lo scambio:

- Invia al venditore il tuo indirizzo Bitcoin o la tua intece Lightning

![Ente adresse Bitcoin](assets/fr/15.webp)

- Ricevi le coordinate bancarie del venditore

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)

- Effettua il pagamento (senza citare "Bisq" o "Bitcoin")
- Comunica al venditore l'avvenuto pagamento

![Notification paiement](assets/fr/18.webp)


- Attendi l'arrivo dei bitcoin

![Attente réception](assets/fr/19.webp)

### Come vendere Bitcoin?

Il processo di vendita su Bisq 2 segue una logica simile a quella dell'acquisto, con le stesse fasi principali ma in ordine inverso. È possibile creare la propria offerta di vendita o rispondere a un'offerta di acquisto esistente. Ecco una panoramica delle varie opzioni e delle fasi del processo:

**Opzione 1: crea un'offerta di vendita**

- Seleziona "Bisq Easy" e poi "Offerbook"
- Clicca su "Crea offerta" e scegli "Vendi Bitcoin"
- Configura l'offerta:
 - Seleziona la valuta (EUR, USD, ecc.)
 - Scegli i metodi di pagamento accettati
 - Imposta l'importo (un importo equivalente all'intervallo tra 6 e 600 USD)
 - Stabilisci il tuo prezzo (fisso o in % di mercato)
- Controlla i dettagli e pubblica l'offerta

**Opzione 2: scegli un'offerta esistente**

- Sfoglia le offerte nella scheda "Offerbook"
- Filtra per valuta e metodo di pagamento
- Seleziona l'offerta che fa per te
- Controlla i dettagli e accetta l'offerta

**Processo di vendita**

Una volta avviato lo scambio:

   - Invia le tue coordinate bancarie all'acquirente
   - Attendi di ricevere l'indirizzo Bitcoin dell'acquirente
   - Verifica che l'indirizzo sia valido

Dopo la notifica di pagamento:

   - Controlla che il pagamento sia stato ricevuto sul tuo conto
   - Conferma che l'importo e i dettagli corrispondano
   - Invia bitcoin all'indirizzo fornito
   - Contrassegna la transazione come completata

Finalizzazione:

   - Attendi la conferma dell'acquirente
   - Lascia un feedback sulla transazione
   - Crea la tua reputazione per le vendite future

**Nota importante:** In qualità di venditore, è necessario essere particolarmente attenti al rischio di chargeback (una procedura per annullare il pagamento con carta di credito se ci sono problemi con l'esercente.). Date la preferenza a metodi di pagamento sicuri e controllate sempre che il pagamento sia stato ricevuto prima di inviare bitcoin.

## Buone pratiche e sicurezza

### Suggerimenti per la sicurezza

**Per gli acquirenti**

- Inizia con piccole quantità
- Controlla la reputazione dei venditori (punteggio minimo di 30.000)
- Utilizza solo i metodi di pagamento suggeriti
- Controlla che il venditore sia attivo prima di inviare il pagamento
- Utilizza solo le coordinate bancarie fornite nella chat di scambio
- Non comunicare mai al di fuori della piattaforma Bisq 2
- Conserva la prova di pagamento
- Non inviare mai informazioni sensibili

**Per i venditori**

- Fai attenzione ai nuovi account
- Evita metodi di pagamento in cui è possibile effettuare ai chargeback (PayPal, Venmo)
- Verifica che i dati del conto corrispondano a quelli dell'acquirente
- Limita la comunicazione alla chat Bisq 2
- Apri una mediazione in caso di dubbio

### Come costruire la propria reputazione (per i venditori)

Per migliorare la tua reputazione di venditore su Bisq, fai transazioni regolari e mantieni una comunicazione professionale con gli acquirenti. Rispondi rapidamente alle richieste degli acquirenti per garantire un'esperienza positiva. Puoi anche creare un BSQ bond per dimostrare il tuo impegno nella piattaforma. Queste azioni creeranno fiducia e attireranno più acquirenti.

### Risoluzione delle controversie

- Contatta la controparte via chat
- Se necessario, apri una controversia
- Fornisci tutte le prove richieste
- Segui le istruzioni del mediatore

### Informativa sulla privacy:

- Non è richiesta alcuna registrazione o verifica centralizzata dell'identità personale
- Tutte le connessioni passano attraverso la rete Tor (e presto anche I2P)
- Nessun server centrale per l'archiviazione dei dati
- I dettagli della transazione sono leggibili solo dalle parti coinvolte

### Protezione dalla censura:

- Rete P2P completamente distribuita
- Utilizzo della rete Tor (e presto anche I2P) per resistere alla censura
- Progetto open source gestito da una DAO, senza un'entità legale centralizzata

## Vantaggi e svantaggi

### Vantaggi di Bisq 2

- **Massima riservatezza**: Nessuna procedure di KYC (Know Your Customer), e utilizzo di Tor
- **Decentralizzazione**: Nessun server centrale
- **Sicurezza**: Codice open source e non custodial
- **Interfaccia intuitiva**: più semplice di Bisq 1
- **Flessibilità**: Diversi protocolli di scambio

### Bisq 2 svantaggi

- **Liquidità limitata** (per il momento):
 - **Nuovo protocollo** in fase di avvio
 - **Poche offerte** di vendita disponibili
 - **Tempi di attesa potenzialmente lunghi** per trovare un acquirente
- **Limiti di trading**: Massimo 600 USD per transazione (con Bisq easy)
- **Solo desktop**: Nessuna applicazione su mobile

## Protocolli futuri

Sebbene Bisq Easy sia attualmente l'unico protocollo disponibile, diversi altri protocolli sono in fase di sviluppo per Bisq 2:

- **Bisq Lightning**: Protocollo di scambio basato su un sistema di deposito a garanzia che utilizza la crittografia di calcolo multiparty sulla rete Lightning.
- **Bisq MuSig**: Migrazione del protocollo principale da Bisq 1 a Bisq 2, utilizzando un multisig 2 di 2 con depositi di sicurezza.
- **Scambi BSQ**: Atomic Swap istantanei tra BSQ e BTC.
- **Liquid Swaps**: Scambi sulla rete Liquid (USDT, BTC-L) tramite atomic swaps.
- **Scambi di Monero**: atomic swaps tra Bitcoin e Monero.
- **Liquid MuSig**: Versione del protocollo multisig che utilizza L-BTC per ridurre i costi e aumentare la riservatezza.
- **Submarine Swaps**: Scambi tra la rete Lightning e Bitcoin on-chain.
- **Scambi di Stablecoin**: atomic swaps tra Bitcoin e la Stablecoin USD.
- **Opzioni Multisig**: Creazione di opzioni put e call P2P con blocco di BTC in una transazione multisig on-chain.
- **Contratti aperti multisig**: Consente di creare "contratti" condizionati personalizzati utilizzando un sistema multisig 2 di 3 con arbitraggio.

Questi protocolli sono attualmente in fase di sviluppo e saranno progressivamente integrati in Bisq 2, offrendo una maggiore flessibilità agli utenti in base alle loro esigenze specifiche.

## Risorse utili

- Sito web ufficiale: [bisq.network](https://bisq.network)
- Documentazione: [Wiki Bisq](https://bisq.wiki)
- Supporto: [Forum Bisq](https://bisq.community)
- Codice sorgente: [GitHub](https://github.com/bisq-network)
