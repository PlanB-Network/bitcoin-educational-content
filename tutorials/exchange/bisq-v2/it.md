---
name: Bisq 2
description: Guida completa all'utilizzo di Bisq 2 e allo scambio di bitcoin P2P
---
![cover](assets/cover.webp)

## Introduzione

Gli scambi peer-to-peer (P2P) senza KYC sono essenziali per preservare la riservatezza e l'autonomia finanziaria degli utenti. Permettono di effettuare transazioni dirette tra individui senza la necessità di verificare l'identità, il che è fondamentale per coloro che tengono alla privacy. Per una comprensione più approfondita dei concetti teorici, date un'occhiata al corso BTC204:

https://planb.network/courses/btc204
### Che cos'è Bisq 2?

Bisq 2 è la nuova versione del popolare exchange decentralizzato Bisq, lanciato nel 2024. A differenza del suo predecessore, Bisq 2 è stato sviluppato per supportare più protocolli di scambio, offrendo agli utenti una maggiore flessibilità.

**Nuove caratteristiche principali


- Supporto per più reti di privacy (Tor, I2P)
- Identità multiple per una maggiore riservatezza
- API REST per i bot di trading
- Supporto per più tipi di portafoglio
- Sistema di ruoli con deposito obbligatorio in BSQ

Questa guida si concentra esclusivamente su "Bisq Easy", l'unico protocollo attualmente disponibile. Bisq Easy è stato progettato specificamente per i nuovi utenti di Bitcoin. Questo protocollo consente agli utenti di acquistare e vendere Bitcoin contro valute fiat su una piattaforma decentralizzata peer-to-peer. Le transazioni sono limitate all'equivalente di 600 USD (con un minimo di 6 USD) e la sicurezza dello scambio si basa sulla reputazione dei venditori di BTC. Bisq Easy non prevede commissioni di trading né requisiti di deposito di sicurezza. Bisq Easy dovrebbe sostituire Bisq 1 per gli scambi di denaro al di sotto dei 600 USD (o equivalenti).

**Caratteristiche principali:**


- Applicazione desktop multipiattaforma
- Sono disponibili diversi protocolli di scambio
- Rete P2P decentralizzata
- Attenzione alla riservatezza (nessun KYC, uso di Tor)
- Non custodiale (il cliente mantiene il controllo dei propri fondi)
- Open source (AGPL)

### Differenze con Bisq 1

**Per gli acquirenti


- Non è richiesto alcun deposito cauzionale
- Nessuna commissione di trading
- Nessuna tassa mineraria
- Sicurezza basata sulla reputazione del fornitore
- Limiti di negoziazione inferiori (equivalenti a 600 USD)

**Per i venditori


- Non è richiesto alcun deposito cauzionale
- Costruire una reputazione
- Possibilità di bruciare BSQ o di creare legami BSQ
- Premio di vendita potenzialmente più alto (10-15% sopra il mercato)

**Nota importante:** Una volta implementato il protocollo Bisq Multisig in Bisq 2, la vecchia versione di Bisq potrà essere eliminata. Tuttavia, Bisq 1 continuerà a essere utilizzato come strumento di gestione per il CAD Bisq e per gli scambi BSQ-BTC.

### Processo di scambio


- L'ideatore dell'offerta definisce i termini dello scambio
- Una volta che gli operatori si sono accordati sui termini (metodo di pagamento e prezzo), lo scambio ha inizio
- Il venditore invia le proprie coordinate bancarie all'acquirente e l'acquirente invia il proprio indirizzo Bitcoin al venditore
- L'acquirente effettua il pagamento in contanti e lo comunica al venditore
- Una volta ricevuto il pagamento, il venditore invia i bitcoin all'indirizzo dell'acquirente
- Lo scambio è completo quando l'acquirente riceve i bitcoin

### Regole importanti


- Prima di scambiare i dati di pagamento, lo scambio può essere annullato senza alcuna giustificazione
- Dopo lo scambio di informazioni, il mancato rispetto degli obblighi può comportare l'esilio
- Per i bonifici bancari, **non utilizzare mai i termini "Bisq" o "Bitcoin "** nella causale di pagamento (ciò potrebbe comportare il blocco dei fondi o addirittura il blocco del conto bancario del destinatario o dell'ordinante)
- I trader devono collegarsi almeno una volta al giorno per seguire il processo
- In caso di problemi, i commercianti possono ricorrere ai servizi di un mediatore

## Installazione e configurazione

### 1. Scaricare e verificare Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Vai a [bisq.network](https://bisq.network/downloads/)
- Scaricare la versione di Bisq 2 corrispondente al proprio sistema operativo (scorrere la pagina verso il basso)
- Verificare l'autenticità del file scaricato (fortemente consigliato). Per una guida dettagliata alla verifica della firma, vedere la seguente esercitazione:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Installazione in base al proprio sistema

Seguire i passaggi di installazione appropriati per il proprio sistema operativo. Se si incontrano difficoltà durante l'installazione, è possibile consultare la guida dettagliata sul [wiki ufficiale di Bisq](https://bisq.wiki/Downloading_and_installing).

### 3. Primo avvio


- Avviare Bisq 2 e accettare le condizioni d'uso

![Conditions d'utilisation](assets/fr/01.webp)


- Creare un nuovo profilo scegliendo un nome e un avatar

![Création du profil](assets/fr/02.webp)


- Si accede quindi alla dashboard principale dell'applicazione, dove è possibile lanciare Bisq Easy per acquistare o vendere i primi bitcoin

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Impostazione dei metodi di pagamento


- Accedere alla sezione conti di pagamento dal menu principale

![Liste des comptes de paiement](assets/fr/04.webp)


- Aggiungete un nuovo metodo di pagamento compilando le informazioni richieste

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

La preconfigurazione dei metodi di pagamento è facoltativa, ma consigliata per risparmiare tempo durante la negoziazione. È anche possibile configurare i metodi di pagamento direttamente durante una transazione, contattando il partner di scambio.

### 5. Sicurezza del conto

**Backup dei dati

A differenza di Bisq 1, Bisq 2 non integra attualmente un portafoglio Bitcoin: le transazioni vengono quindi effettuate tramite portafogli esterni. Tuttavia, si consiglia di eseguire regolarmente un backup della cartella dati di Bisq 2. Per individuare la cartella dati, consultare il [wiki ufficiale di Bisq](). Per individuare la cartella dei dati, consultare il [wiki ufficiale di Bisq](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Gestione dell'identità

Bisq 2 consente di creare più identità. Ogni identità può essere utilizzata per diversi tipi di transazioni. Le identità vengono memorizzate nella cartella dei dati.

## Comprare e vendere Bitcoin

### Come acquistare i Bitcoin

**Opzione 1: approfittare di un'offerta esistente**


- Nella schermata principale, selezionare "Bisq Easy", la scheda "Guida introduttiva", quindi fare clic su "Avvia procedura guidata"

![Lancer trade wizard](assets/fr/06.webp)


- Scegliete "Acquista Bitcoin" e selezionate la vostra valuta

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Impostare i metodi di pagamento preferiti (SEPA, Revolut, ecc.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- A questo punto, o si dispone di un elenco di offerte che corrispondono ai criteri precedenti, oppure è necessario accedere al "Libro delle offerte"

![Liste des offres](assets/fr/10.webp)


- Nel secondo caso, è possibile visualizzare e filtrare le offerte utilizzando i pulsanti in alto a destra dell'interfaccia

![Filtres des offres](assets/fr/11.webp)


- Una volta scelta l'offerta, non resta che scegliere il metodo di pagamento e convalidare il riepilogo dell'operazione

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Opzione 2: Creare la propria offerta**


- Selezionare "Bisq Easy" e poi "Offerbook"
- Scegliere la coppia di trading (ad es. BTC/EUR)
- Fare clic su "Crea offerta
- Seguire la procedura guidata di creazione dell'offerta: Definire l'importo (fisso o intervallo)

![Configuration du montant](assets/fr/20.webp)


- Selezionare i metodi di pagamento accettati

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Controllare il riepilogo e pubblicare l'offerta

![Récapitulatif et publication](assets/fr/22.webp)

Una volta avviato lo scambio :


- Inviate al venditore il vostro indirizzo Bitcoin o la vostra fattura Lightning

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Ricevere le coordinate bancarie del venditore

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Effettuare il pagamento (senza menzionare "Bisq" o "Bitcoin")
- Comunicare al venditore l'avvenuto pagamento

![Notification paiement](assets/fr/18.webp)


- Attendere l'arrivo dei bitcoin

![Attente réception](assets/fr/19.webp)

### Come vendere i Bitcoin?

Il processo di vendita su Bisq 2 segue una logica simile a quella dell'acquisto, con le stesse fasi principali ma in ordine inverso. È possibile creare la propria offerta di vendita o rispondere a un'offerta di acquisto esistente. Ecco una panoramica delle varie opzioni e delle fasi del processo:

**Opzione 1: creare un'offerta di vendita**


- Selezionare "Bisq Easy" e poi "Offerbook"
- Cliccate su "Crea offerta" e scegliete "Vendi Bitcoin"
- Configurare l'offerta :
 - Selezionare la valuta (EUR, USD, ecc.)
 - Scegliere i metodi di pagamento accettati
 - Impostare l'importo (tra 6 e 600 USD equivalenti)
 - Stabilite il vostro prezzo (fisso o in % del mercato)
- Controllare i dettagli e pubblicare l'offerta

**Opzione 2: aderire ad un'offerta esistente**


- Sfogliare le offerte nella scheda "Libro delle offerte"
- Filtro per valuta e metodo di pagamento
- Selezionate l'offerta che fa per voi
- Controllare i dettagli e accettare l'offerta

**Processo di vendita

Una volta avviato lo scambio :


   - Inviate le vostre coordinate bancarie all'acquirente
   - Attendere l'indirizzo Bitcoin dell'acquirente
   - Verificare che l'indirizzo sia valido

Dopo la notifica del pagamento :


   - Controllare che il pagamento sia stato ricevuto sul vostro conto
   - Confermare che l'importo e i dettagli corrispondono
   - Inviare bitcoin all'indirizzo fornito
   - Contrassegnare la transazione come completata

Finalizzazione :


   - Attendere la conferma dell'acquirente
   - Lasciate un feedback sulla transazione
   - Costruite la vostra reputazione per le vendite future

**Nota importante:** In qualità di venditore, è necessario essere particolarmente attenti al rischio di chargeback. Date la preferenza a metodi di pagamento sicuri e controllate sempre che il pagamento sia stato ricevuto prima di inviare bitcoin.

## Buone pratiche e sicurezza

### Suggerimenti per la sicurezza

**Per gli acquirenti


- Iniziare con piccole quantità
- Controllare la reputazione dei venditori (punteggio minimo di 30.000)
- Utilizzate solo i metodi di pagamento suggeriti
- Controllare che il venditore sia attivo prima di inviare il pagamento
- Utilizzate solo le coordinate bancarie fornite nella chat di scambio
- Non comunicare mai al di fuori della piattaforma Bisq 2
- Conservare la prova di pagamento
- Non inviare mai informazioni sensibili

**Per i venditori


- Attenzione ai nuovi conti
- Evitare i metodi di pagamento sensibili ai chargeback (PayPal, Venmo)
- Verificare che i dati del conto corrispondano a quelli dell'acquirente
- Limitare la comunicazione alla chat Bisq 2
- Aprire una mediazione in caso di dubbio

### Costruzione della reputazione (per i venditori)

Per migliorare la vostra reputazione di venditore su Bisq, conducete transazioni regolari e mantenete una comunicazione professionale con gli acquirenti. Rispondete rapidamente alle richieste degli acquirenti per garantire un'esperienza positiva. Potete anche creare un BSQ bond per dimostrare il vostro impegno nella piattaforma. Queste azioni creeranno fiducia e attireranno più acquirenti.

### Risoluzione delle controversie


- Contattare la controparte via chat
- Se necessario, aprire una controversia
- Fornire tutte le prove richieste
- Seguire le istruzioni del mediatore

### Informativa sulla privacy :


- Non è richiesta alcuna registrazione o verifica centralizzata dell'identità
- Tutte le connessioni passano attraverso la rete Tor (e presto anche I2P)
- Nessun server centrale per l'archiviazione dei dati
- I dettagli della transazione sono leggibili solo dalle parti coinvolte

### Protezione dalla censura :


- Rete P2P completamente distribuita
- Usare la rete Tor (e presto anche I2P) per resistere alla censura
- Progetto open source gestito da una DAO, senza un'entità legale centralizzata

## Vantaggi e svantaggi

### Vantaggi di Bisq 2


- Massima riservatezza**: Nessun KYC, uso di Tor
- Decentralizzazione**: Nessun server centrale
- Sicurezza**: Codice open source e non custodiale
- Interfaccia intuitiva**: più semplice di Bisq 1
- Flessibilità**: Protocolli di scambio multipli

### Bisq 2 svantaggi


- Liquidità limitata** (per il momento) :
 - Nuovo protocollo in fase di avvio
 - Poche offerte di vendita disponibili
 - Tempi di attesa potenzialmente lunghi per trovare un acquirente
- Limiti di trading**: Massimo 600 USD per transazione (con Bisq easy)
- Solo desktop**: Nessuna applicazione mobile

## Protocolli futuri

Sebbene Bisq Easy sia attualmente l'unico protocollo disponibile, diversi altri protocolli sono in fase di sviluppo per Bisq 2 :


- Bisq Lightning**: Protocollo di scambio basato su un sistema di deposito a garanzia che utilizza la crittografia di calcolo multiparty sulla rete Lightning.
- Bisq MuSig**: Migrazione del protocollo principale da Bisq 1 a Bisq 2, utilizzando un multisig 2 contro 2 con depositi di sicurezza.
- Scambi BSQ**: Scambi atomici istantanei tra BSQ e BTC.
- Liquid Swaps**: Scambio di attività sulla rete Liquid (USDT, BTC-L) tramite swap atomici.
- Scambi di Monero**: Scambi atomici tra Bitcoin e Monero.
- Liquid MuSig**: Versione del protocollo multisig che utilizza L-BTC per ridurre i costi e aumentare la riservatezza.
- Scambi sottomarini**: Scambi tra Bitcoin sulla rete Lightning e Bitcoin on-chain.
- Scambi di Stablecoin**: Scambi atomici tra Bitcoin e Stablecoin USD.
- Opzioni Multisig**: Creazione di opzioni put e call P2P con blocco di BTC in una transazione multisig on-chain.
- Contratti aperti multisig**: Consente di creare contratti condizionati personalizzati utilizzando un sistema multisig 2 contro 3 con arbitraggio.

Questi protocolli sono attualmente in fase di sviluppo e saranno progressivamente integrati in Bisq 2, offrendo una maggiore flessibilità agli utenti in base alle loro esigenze specifiche.

## Risorse utili


- Sito web ufficiale: [bisq.network](https://bisq.network)
- Documentazione: [Wiki Bisq](https://bisq.wiki)
- Supporto: [Forum Bisq](https://bisq.community)
- Codice sorgente : [GitHub](https://github.com/bisq-network)