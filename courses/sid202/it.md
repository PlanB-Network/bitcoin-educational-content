---
name: Costruire con elementi e rete liquida
goal: Imparare a utilizzare e sviluppare con la piattaforma blockchain open-source Elements e le sue caratteristiche principali
objectives: 

  - Comprendere i concetti fondamentali della piattaforma blockchain Elements e delle sidechain Liquid.
  - Imparate a configurare ed eseguire i nodi Elements per le configurazioni standalone e sidechain.
  - Acquisire esperienza pratica con la firma a blocchi federata e il Federated 2-Way Peg.
  - Impostare e gestire ambienti blockchain sicuri ed efficienti per casi d'uso reali.

---
# Costruire su liquidi ed elementi

Scoprite le caratteristiche e le funzionalità avanzate di Liquid ed Elements e imparate a utilizzare efficacemente questi strumenti per migliorare i vostri progetti di sviluppo. Questa formazione fornisce una base teorica e pratica completa, consentendovi di padroneggiare funzionalità quali Transazioni riservate, Attività emesse e Firma a blocchi federata.

Liquid, basato sul framework Elements, è progettato per migliorare la privacy, la scalabilità e la funzionalità delle soluzioni finanziarie e tecniche. In questo corso, acquisirete esperienza pratica con l'emissione e la gestione di asset, il Federated 2-Way Peg e l'uso di strumenti come elementsd ed elements-cli, consentendovi di creare soluzioni innovative su misura per le vostre esigenze.

Questo corso è adatto agli sviluppatori di tutti i livelli di esperienza. I principianti e gli utenti intermedi troveranno spiegazioni accessibili ed esempi pratici, mentre gli utenti avanzati potranno approfondire i dettagli tecnici e le caratteristiche meno conosciute di Liquid ed Elements.

Unisciti a noi per elevare le tue competenze, sbloccare il pieno potenziale di Liquid ed Elements e creare strumenti d'impatto per il futuro dell'innovazione di Liquid.

+++
# Introduzione

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Introduzione ai corsi

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Lo scopo di Elements Academy è quello di introdurre e spiegare i concetti chiave di Elements, la piattaforma open-source su cui è costruito Liquid. Alla fine del corso, si dovrebbe avere una buona comprensione delle caratteristiche principali di Elements, come le Transazioni riservate e le Attività emesse, e dei processi coinvolti nella gestione di Elements Core.

Ogni sezione prevede lezioni con testo esplicativo e un video che si conclude con un quiz. Il numero di domande si riferisce alla dimensione dell'argomento precedente. La sezione 10 riassumerà il contenuto del corso e terminerà con un quiz più ampio.

Eventuali domande, richieste di ulteriori informazioni o dubbi sulle risposte ai quiz possono essere rivolte all'insegnante James Dorfman.

## Panoramica degli elementi

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements è una piattaforma blockchain open source e compatibile con la sidechain, che consente di accedere a potenti funzionalità sviluppate dai membri della comunità, come le Transazioni riservate e gli Asset emessi.

Elements è, nella sua essenza, un protocollo che consente di formare il consenso intorno alla storia delle transazioni e alle regole che governano il trasferimento e la creazione di beni memorizzati in un libro mastro distribuito della blockchain.

Ulteriori informazioni di base su Elements sono disponibili sul sito web del progetto Elements (https://elementsproject.org/), sul blog ufficiale di Liquid (https://blog.liquid.net/) e sul portale degli sviluppatori (https://liquid.net/devs).

### Elementi

Lanciato nel 2015, Elements riduce i costi interni di sviluppo e ricerca e sfrutta la più recente tecnologia blockchain, aprendo molti nuovi casi d'uso per l'implementazione. Una blockchain basata su Elements può funzionare come blockchain indipendente o essere collegata a un'altra e funzionare come sidechain. L'esecuzione di Elements come Sidechain consente di trasferire in modo verificabile gli asset tra blockchain diverse.

Costruito sulla base del codice di Bitcoin e da esso esteso, consente agli sviluppatori che hanno familiarità con l'API di Bitcoin di creare rapidamente e a costi contenuti blockchain funzionanti e di testare progetti proof-of-concept. Essendo costruito sulla base di codice di Bitcoin, Elements può anche funzionare come banco di prova per le modifiche al protocollo Bitcoin stesso.

Di seguito sono elencate alcune delle caratteristiche principali di Elements.

#### Transazioni riservate

Per impostazione predefinita, tutti gli indirizzi in Elements sono blindati utilizzando le Transazioni riservate. L'accecamento è il processo mediante il quale l'importo e il tipo di attività trasferita vengono nascosti crittograficamente a tutti, tranne che ai partecipanti e a coloro che scelgono di rivelare la chiave di accecamento.

#### Attività emesse

Gli Issued Assets su Elements consentono di emettere e trasferire più tipi di asset tra i partecipanti alla rete. Un Asset emesso beneficia anche delle Transazioni riservate e può essere riemesso o distrutto da chiunque possieda il relativo token di riemissione.

#### Piolo Federato a 2 vie

Elements è una piattaforma blockchain di uso generale che può anche essere "agganciata" a una blockchain esistente (come Bitcoin) per consentire il trasferimento bidirezionale di asset da una catena all'altra. L'implementazione di Elements come sidechain consente di aggirare alcune delle proprietà intrinseche della catena principale, pur mantenendo un buon grado di sicurezza fornito dagli asset protetti sulla catena principale.

#### Blocchi firmati

Elements utilizza una Strong Federation di firmatari, chiamati Block Signers, che firmano e creano blocchi in modo affidabile e tempestivo. In questo modo si elimina la latenza delle transazioni del processo di estrazione PoW, che è soggetto a una grande varianza dei tempi dei blocchi a causa della sua distribuzione casuale di tipo poisson. Il processo di Federated Block Signing consente di ottenere una creazione affidabile dei blocchi senza introdurre la necessità di una fiducia da parte di terzi o di un mining basato su algoritmi computazionali.

Elements aggiunge tutte queste funzionalità alla base di codice di Bitcoin Core, estendendo le capacità del protocollo mainchain e consentendo nuovi casi d'uso commerciali quando viene distribuito come sidechain o come soluzione blockchain indipendente.

# Elemento

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Come funziona Elements

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements fornisce una soluzione tecnica ai problemi che gli utenti della blockchain devono affrontare quotidianamente: latenza delle transazioni, mancanza di privacy e rischio di fungibilità.

Elements supera questi problemi grazie all'uso della firma a blocchi federata e delle transazioni riservate.

A differenza della rete Bitcoin, il processo di firma dei blocchi all'interno di Elements non si basa su Dynamic Membership Multiparty Signatures (DMMS) e Proof of Work (PoW). Elements utilizza invece una Strong Federation di firmatari, chiamati Block Signers, che possono firmare e creare blocchi in modo affidabile e tempestivo. In questo modo si elimina la latenza delle transazioni del processo di estrazione PoW, che è soggetto a grandi variazioni di tempo dei blocchi a causa della sua distribuzione casuale di tipo poisson. Il processo di Federated Block Signing consente di ottenere una creazione affidabile dei blocchi senza introdurre la necessità di una fiducia da parte di terzi.

Elements può funzionare come sidechain di un'altra blockchain, come Bitcoin, o come blockchain autonoma senza dipendere da altre reti.

Quando viene utilizzata come sidechain, la Strong Federation contiene anche membri che consentono il trasferimento sicuro e controllato di asset tra una catena principale e una sidechain Elements. Il trasferimento controllato di beni è chiamato Federated 2-Way Peg e i membri che svolgono il ruolo di trasferimento dei beni sono chiamati Watchmen.

I processi coinvolti nella gestione di una rete Elements e i ruoli dei partecipanti alla rete sono importanti per comprendere il funzionamento di Elements.

Sia che venga implementata come sidechain o come blockchain indipendente, Elements si avvale di Federazioni forti di firmatari di blocchi per produrre blocchi.

### Federazioni forti

Elements utilizza un modello di consenso proposto per la prima volta da Blockstream, chiamato Strong Federations. Una Strong Federation non ha bisogno di Proof of Work (PoW) e si affida invece alle azioni collettive di un gruppo di partecipanti reciprocamente diffidenti, chiamati Funzionari.

I ruoli che un Funzionario può ricoprire all'interno di una Federazione forte sono: Firmatari di blocchi e Guardiani. I Block Signers sono necessari se si esegue Elements in modalità sidechain o standalone blockchain, mentre i Watchmen sono necessari solo in una configurazione sidechain.

Le azioni che un membro di una Strong Federation può eseguire sono suddivise tra due ruoli distinti per migliorare la sicurezza e limitare i danni che un attaccante può causare.

Se combinati, i ruoli di questi partecipanti consentono a Elements di fornire sia una rapida creazione di blocchi (una conferma più rapida e definitiva delle transazioni) sia asset sicuri e trasferibili (asset pegged direttamente collegabili a un'altra blockchain).

È possibile leggere il whitepaper Strong Federations qui: https://blockstream.com/strong-federations.pdf

### Blocco dei firmatari

Una blockchain come quella di Bitcoin viene estesa quando chiunque faccia parte di un gruppo dinamico di firmatari di blocchi estende la catena dimostrando la prova del lavoro svolto. La natura dinamica dell'insieme introduce i problemi di latenza propri di questi sistemi.

Utilizzando un insieme fisso di firmatari, il modello federato sostituisce l'insieme dinamico con un insieme noto e uno schema a più firme. La riduzione del numero di partecipanti necessari per estendere la blockchain aumenta la velocità e la scalabilità del sistema, mentre la convalida da parte di tutte le parti garantisce l'integrità della cronologia delle transazioni.

La firma a blocchi federata consiste in diverse fasi:


- Fase 1 - I firmatari dei blocchi propongono i blocchi candidati in modo circolare a tutti gli altri firmatari dei blocchi partecipanti.
- Fase 2 - Ogni firmatario del blocco segnala la propria intenzione impegnandosi a firmare il blocco candidato.
- Fase 3 - Se la soglia data per il preimpegno è soddisfatta, ogni firmatario del blocco firma il blocco.
- Fase 4 - Se la soglia di firma (che può essere diversa da quella della fase 3) è soddisfatta, il blocco viene accettato e inviato alla rete. La Strong Federation ha raggiunto il consenso sull'ultimo blocco di transazioni.
- Fase 5 - Il blocco successivo viene proposto dal successivo firmatario del blocco nel round-robin e il processo si ripete.

Poiché la generazione dei blocchi di una Strong Federation non è probabilistica e si basa su un insieme fisso di firmatari, non sarà mai soggetta a riorganizzazioni multi-blocco. Ciò consente una significativa riduzione dei tempi di attesa associati alla conferma delle transazioni. Inoltre, elimina l'incentivo a estrarre per profitto (cioè le ricompense dei blocchi) e lo sostituisce con un incentivo a partecipare in modo produttivo a una rete in cui tutti i partecipanti hanno lo stesso obiettivo condiviso: garantire che la rete continui a funzionare in modo vantaggioso per tutti. Ciò avviene senza introdurre un singolo punto di fallimento o requisiti di fiducia più elevati.

### Elementi come catena laterale - Watchmen e il Peg a 2 vie federato

Se gestita come sidechain, alcuni membri della Strong Federation hanno un ruolo aggiuntivo da svolgere, quello dei Watchmen. I guardiani sono responsabili del trasferimento di beni in entrata e in uscita da una sidechain Elements, processi noti come `Peg-In` e `Peg-Out`.

Affinché una sidechain operi in modo affidabile, deve consentire ai partecipanti di verificare che la fornitura di asset sia controllata e verificabile. Una sidechain di Elements utilizza un 2-Way Federated Peg per consentire il trasferimento bidirezionale di asset all'interno e all'esterno di una blockchain di Elements. Questo soddisfa i requisiti di emissione e trasferimento intercatena dimostrabili.

La funzione Federated 2-way Peg consente a un asset di essere interoperabile con altre blockchain e rappresentativo dell'asset nativo di un'altra blockchain. Agganciando la propria blockchain a un'altra, è possibile estendere le capacità della mainchain e superare alcune delle sue limitazioni intrinseche.

Ad alto livello, i trasferimenti nella sidechain avvengono quando qualcuno invia beni della mainchain a un indirizzo controllato da un portafoglio Watchmen a firma multipla. Questo blocca di fatto gli asset sulla mainchain. Watchmen convalida quindi la transazione e rilascia la stessa quantità di asset associati all'interno della sidechain. Gli asset rilasciati vengono inviati a un portafoglio della sidechain che può dimostrare di avere diritto agli asset originali della mainchain. Questo processo sposta effettivamente gli asset dalla catena principale alla sidechain.

Per trasferire gli asset alla mainchain, un utente effettua una speciale transazione di peg-out sulla sidechain. Questa transazione viene controllata dai Watchmen, che poi firmano una transazione di spesa dal portafoglio multi-firma che controllano sulla mainchain. Un numero limite di partecipanti alla federazione deve firmare prima che la transazione sulla mainchain diventi valida. Quando i Watchmen rimandano un asset alla mainchain, distruggono anche l'importo corrispondente sulla sidechain, trasferendo di fatto gli asset tra le blockchain.

## Impostazione ed esecuzione degli elementi

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Poiché Elements si basa sulla base di codice di Bitcoin, i componenti che costituiscono una rete funzionante sono molto simili.

Il software del nodo Elements si chiama `elementsd` e viene eseguito come demone sul computer dell'utente. Un demone (o servizio in Windows) è un programma che viene eseguito come servizio in background senza richiedere il controllo diretto di un utente connesso.

Nota: in questo documento ci riferiremo sempre a elementsd come versione del demone, ma tutto può essere fatto con elements-qt, a condizione che l'opzione server sia abilitata.

Il demone Elements si connette agli altri nodi della rete per scambiare i dati delle transazioni e dei blocchi, convalidando ed estendendo la propria copia locale della blockchain della rete.

Il software Elements comprende anche un programma client chiamato `elements-cli` che consente di inviare comandi RPC (Remote Procedure Call) a elementsd dalla riga di comando. Questo può essere usato, ad esempio, per interrogare il saldo di un portafoglio, visualizzare i dati delle transazioni o dei blocchi o trasmettere una transazione. Questa configurazione dovrebbe essere familiare a chiunque abbia usato gli equivalenti di Bitcoin: bitcoind e bitcoin-cli.

Poiché un nodo Elements può essere configurato passando i parametri all'avvio o tramite un file di configurazione, è possibile avere più di un'istanza in esecuzione sulla stessa macchina. Ciò è utile per scopi di test e sviluppo, in quanto è possibile configurare la propria rete locale su una singola macchina, con ciascun nodo Elements che dispone della propria copia dei dati della blockchain, gestisce il proprio pool di transazioni valide non confermate e ascolta le richieste RPC su porte diverse.

### L'archivio e la comunità del codice Elements

Elements è un progetto open-source e il suo codice sorgente può essere trovato nel repository GitHub di Elements, all'indirizzo https://github.com/ElementsProject/elements. Il repository contiene i sorgenti dei programmi elementsd ed elements-cli, oltre a strumenti di installazione e compilazione di supporto, una suite di test e una certa documentazione didattica.

A complemento del repository di codice, c'è anche il sito web https://elementsproject.org, una risorsa incentrata sulla comunità che contiene spiegazioni su cos'è Elements, come funziona e una sezione di tutorial completa. L'esercitazione si concentra sull'apprendimento di Elements seguendo esempi da riga di comando e mostra come costruire semplici applicazioni desktop e web su di esso. Il sito elenca anche i forum di discussione della comunità di Elements ed è ospitato su GitHub, consentendo alla comunità di contribuire ai contenuti del sito.

Per eseguire Elements sul proprio computer è necessario innanzitutto clonare (scaricare una copia) del codice sorgente, installare tutte le dipendenze presenti nel codice e infine creare gli eseguibili del demone e del client. Il software Elements è quindi pronto per essere configurato ed eseguito.

## Configurazione dei nodi e della rete

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Le impostazioni di configurazione possono essere passate a un nodo Elements all'avvio per modificare il modo in cui funziona, convalida i dati, si connette ad altri nodi e inizializza i suoi dati blockchain.

Le impostazioni vengono caricate dal file `elements.conf' designato o passate come parametri tramite la riga di comando.

Alcuni elementi possono essere modificati utilizzando questi parametri:


- Il nome dell'asset predefinito utilizzato nelle implementazioni di blockchain standalone.
- Il numero della risorsa iniziale creata.
- L'asset da utilizzare per il pagamento delle commissioni di transazione sulla rete.
- La posizione di archiviazione dei file di dati della blockchain.
- Le credenziali RPC utilizzate per connettersi a un nodo Bitcoin.
- La soglia `n di m` da rispettare e le chiavi pubbliche valide che possono firmare i blocchi.
- Lo script che deve essere soddisfatto per trasferire le attività all'interno e all'esterno di una sidechain.
- Se connettersi o meno a un nodo Bitcoin come sidechain.

Molti di questi fanno parte delle regole di consenso della rete, quindi è importante che siano applicati a tutti i nodi all'avvio. Alcune possono essere modificate dopo l'inizializzazione di una catena, mentre altre devono essere corrette dopo che sono state usate per inizializzare una catena.

L'uso dei parametri sarà trattato più avanti nel corso del corso, in relazione a ciascuna sezione.

### Operazioni di base con la riga di comando

Questo corso mostra esempi che utilizzano il programma `elements-cli` per effettuare chiamate RPC a uno o più nodi Elements. Questo viene fatto da una sessione di terminale e per rendere i comandi più brevi verrà usato un `alias`. In base a questa convenzione, quando si vede qualcosa come i seguenti comandi:

```bash
e1-dae
e1-cli getnewaddress
```

I caratteri `e1-dae` e `e1-cli` sono in realtà una scorciatoia tipografica che sfrutta la funzione `alias` del terminale. I caratteri `e1-dae` e `e1-cli` verranno effettivamente sostituiti quando il comando verrà eseguito e il comando che verrà eseguito sarà simile a:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Quello che vediamo sopra è una chiamata per avviare il demone Elements e una chiamata ai programmi elements-cli che si trovano nella directory `$HOME/elements/src` e un valore per il parametro `datadir`. Il parametro `datadir` ci permette di dire alle istanze del demone e del client dove localizzare i loro file di configurazione e, nel caso del demone, dove memorizzare la sua copia della blockchain. Poiché condividono un file di configurazione, il client sarà in grado di effettuare chiamate RPC al demone.

Eseguendo nuovamente il comando precedente, ma con un valore diverso di `datadir`, possiamo avviare più di un'istanza di Elements, ognuna con la propria copia separata della blockchain e delle impostazioni di configurazione. Per questa convenzione, nel corso useremo gli alias `e2-dae` e `e2-cli` per riferirci a una directory datadir diversa da quella di e1. Quindi l'esempio precedente per la nostra seconda istanza `e2` sarebbe:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Questo ci consentirà di eseguire ogni sorta di operazione, come la transazione di beni tra nodi, l'emissione di beni e la verifica dell'uso del blinding nelle transazioni riservate tra nodi diversi della stessa rete.

# Utilizzo dell'elemento Caso d'uso pratico

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Transazioni riservate

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

In questa sezione si spiega come utilizzare la funzione Transazioni riservate di Elements.

Tutti gli indirizzi in Elements sono, per impostazione predefinita, blindati utilizzando le Transazioni confidenziali, che mantengono l'importo e il tipo di attività trasferite visibili solo ai partecipanti alla transazione (e a coloro che scelgono di rivelare la chiave di blindatura), garantendo comunque crittograficamente che non si possano spendere più monete di quelle disponibili.

### Indirizzi riservati e transazioni riservate

Per impostazione predefinita, quando si crea un nuovo indirizzo in Elements con il comando `getnewaddress`, viene creato come indirizzo riservato.

Per dimostrare le transazioni confidenziali, faremo in modo che e2 invii a se stesso dei fondi e poi cerchi di visualizzare la transazione da e1. Questo dimostrerà la natura confidenziale delle transazioni in Elements.

Ogni nuovo indirizzo generato da un nodo Elements è riservato per impostazione predefinita. Possiamo dimostrarlo facendo generare a e2 un nuovo indirizzo.

```
e2-cli getnewaddress
```

Si noti che l'indirizzo inizia con e1. Questo lo identifica come un indirizzo confidenziale. Esaminando l'indirizzo in modo più dettagliato con il comando getaddressinfo si ottengono ulteriori dettagli sull'indirizzo.

```
e2-cli getaddressinfo <address>
```

Si può notare che c'è una proprietà confidential_key che indica che si tratta di un indirizzo confidenziale.

La confidential_key è la chiave pubblica di cecità, che viene aggiunta all'indirizzo confidenziale stesso. Questo è il motivo per cui un indirizzo confidenziale è così lungo.

Ha anche un indirizzo non riservato associato. Se si desidera utilizzare transazioni regolari, non riservate, all'interno di Elements, le attività devono essere inviate a questo indirizzo invece che a quello con il prefisso lq1.

Ora possiamo fare in modo che e2 invii dei fondi all'indirizzo che ha generato. In seguito si dimostrerà che e1, non essendo una delle parti coinvolte nella transazione, non sarà in grado di visualizzare i dettagli della transazione.

```
e2-cli sendtoaddress <address>
```

Annotare l'ID della transazione. Confermare la transazione.

```
e2-cli -generate 101
```

Osservando la transazione in cui e2 ha inviato alcuni fondi a se stesso dal punto di vista di e2 stesso.

```
e2-cli gettransaction <txid>
```

Scorrendo i dettagli della transazione, si può notare che e2 è in grado di visualizzare gli importi inviati e ricevuti e l'asset transato. Si possono anche vedere le proprietà amountblinder e assetblinder, utilizzate per nascondere i dettagli da altri nodi non coinvolti nella transazione.

Per controllare i dettagli della stessa transazione da e1, dobbiamo prima ottenere i dettagli della transazione grezza.

```
e1-cli getrawtransaction <txid>
```

Questo restituisce i dettagli grezzi della transazione. Se si guarda alla sezione vout, si può notare che ci sono tre istanze. Le prime due istanze sono gli importi di ricezione e di modifica, mentre la terza è la commissione della transazione. Di questi tre importi, quello della commissione è l'unico in cui è possibile vedere un valore, poiché la commissione stessa è sempre non evidenziata all'interno di Elements.

### Chiavi accecanti

Le prime due sezioni di vout mostrano "intervalli ciechi" di importi di valore e dati di impegno che fungono da prova dell'importo effettivo e del tipo di attività transata.

Anche se importassimo la chiave privata di e2 nel portafoglio di e1, quest'ultimo non sarebbe comunque in grado di vedere gli importi e il tipo di attività transate, perché non è ancora a conoscenza della chiave di blocco utilizzata da e2. Lo dimostreremo importando la chiave privata utilizzata dal portafoglio di e2 in quello di e1. Per prima cosa dobbiamo esportare la chiave da e2

```
e2-cli dumpprivkey <address>
```

Quindi importarlo in e1.

```
e1-cli importprivkey <privkey>
```

Ora possiamo dimostrare che e1 non può ancora vedere i valori.

```
e1-cli gettransaction <txid>
```

In effetti, mostra 0 come quantità di tx, mentre in realtà era 1.

Per poter vedere il valore effettivo, non abbattuto, abbiamo bisogno della chiave di abbattimento. Per farlo, esportiamo prima la chiave di accecamento da e2.

```
e2-cli dumpblindingkey <address>
```

Quindi importarlo in e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Ora, quando otteniamo i dettagli della transazione da e1.

```
e1-cli gettransaction <txid>
```

Si vede che con l'importazione della chiave di cecità è possibile visualizzare il valore effettivo di 1 all'interno della transazione.

In questa sezione abbiamo visto che l'uso di una chiave di vincolo nasconde l'importo e il tipo di attività di una transazione e che, importando la giusta chiave di vincolo, è possibile rivelare tali valori. Nell'uso pratico, una chiave di vincolo può essere fornita, ad esempio, a un revisore dei conti, nel caso in cui sia necessario verificare l'importo e il tipo di attività detenute da una parte. La funzione Transazioni riservate di Elements consente anche di eseguire "prove di intervallo". Le prove di intervallo possono dimostrare che la quantità di un'attività è detenuta all'interno di un determinato intervallo, senza la necessità di esporre l'importo effettivo.

Abbiamo anche visto che le Transazioni riservate sono facoltative, ma vengono attivate di default quando viene generato un nuovo indirizzo.

Per questa lezione è tutto; in bocca al lupo per il quiz e arrivederci alla prossima!

## Attività emesse

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

In questa sezione si spiega come utilizzare la funzione Attività emesse di Elements.

Gli asset emessi consentono di emettere e trasferire diversi tipi di asset tra i partecipanti alla rete Elements. Ogni nodo della rete può emettere i propri asset. Le emissioni possono rappresentare la proprietà fungibile di qualsiasi asset, compresi buoni, coupon, valute, depositi, obbligazioni, azioni, ecc. Gli asset emessi aprono la strada alla creazione di scambi, opzioni e altri contratti intelligenti avanzati senza fiducia che coinvolgono asset auto-emessi.

Un'attività emessa beneficia anche di transazioni riservate e può essere riemessa da chiunque detenga il token associato.

Il primo passo è l'accesso a due nodi Elements, che chiameremo e1 ed e2. I nodi sono stati sottoposti a un reset della blockchain e la risorsa predefinita è stata divisa tra loro.

I due nodi si trovano sulla stessa rete locale e sono collegati tra loro, quindi condividono le stesse transazioni nel loro mempool di transazioni e blockchain identiche. Sebbene siano in esecuzione sulla stessa macchina, vale la pena notare che non condividono gli stessi file blockchain effettivi. Ogni nodo gestisce la propria copia locale della blockchain, che contiene la stessa cronologia delle transazioni, perché sono in consenso e rispettano le stesse regole del protocollo.

Iniziamo controllando la visione di ciascun nodo sulle emissioni di asset esistenti nella rete.

Per farlo, si utilizza il comando listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Come si può vedere, entrambi i nodi mostrano la stessa cronologia di emissione. Entrambi mostrano un asset, l'emissione iniziale di 21 milioni di Bitcoin creati all'inizializzazione della catena. È possibile vedere l'id esadecimale dell'asset nei risultati dell'esecuzione del comando precedente e anche l'etichetta assegnata all'asset, che è "bitcoin".

Vale la pena notare che all'asset predefinito viene sempre assegnata un'etichetta quando la catena viene inizializzata. Quando si rilasciano le proprie risorse, è possibile impostare le etichette per esse, cosa che faremo a breve. Prima di poterlo fare, dobbiamo emettere la nostra risorsa.

Chiederemo a e1 di emettere la nuova risorsa. Per farlo, si utilizza il comando issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` accetta 3 parametri.

L'ammontare del nuovo asset da emettere, noi abbiamo usato 100. La quantità di token da creare (i token sono utilizzati per riemettere quantità di un asset), di cui abbiamo scelto 1. Il parametro finale indica a Elements di creare l'emissione dell'asset come blinded o unblinded. Utilizzeremo unblinded perché vogliamo visualizzare gli importi dell'emissione da e2 tra un minuto, quindi inseriremo false.

L'esecuzione del comando restituisce i dati relativi all'emissione. Questi includono l'id della transazione, di cui si può fare una copia per un uso successivo, il valore esadecimale unico della risorsa e il valore esadecimale unico del token della risorsa.

Generare un blocco per confermare la transazione di emissione.

```
e1-cli -generate 1
```

Eseguire nuovamente il comando `listissuances` su e1.

```
e1-cli listissuances
```

Questo ci mostra che e1 è ora a conoscenza di due emissioni, l'emissione iniziale di Bitcoin e la nostra nuova attività emessa, di cui possiamo vedere 100 esemplari. Si noti il valore esadecimale del nuovo asset e che non c'è un'etichetta di asset associata, come per l'emissione di bitcoin.

Controllate di nuovo l'elenco delle emissioni note di e2.

```
e2-cli listissuances
```

Ciò dimostra che e2 non è a conoscenza dell'emissione di asset effettuata da e1. Può solo vedere l'emissione iniziale di bitcoin che già vedeva.

Questo perché e2 non è a conoscenza e non sta guardando l'indirizzo a cui è stata inviata la nuova risorsa quando è stata emessa da e1.

Vale la pena notare che, anche se e2 non può vedere l'emissione stessa, e1 potrebbe comunque inviare a e2 una parte dell'asset. La nuova attività verrebbe quindi visualizzata come saldo disponibile nel portafoglio di e2, anche se quest'ultimo non è a conoscenza dell'emissione originale.

Per consentire a e2 di vedere l'emissione effettiva (e quindi l'importo emesso), dobbiamo aggiungere l'indirizzo a e2 come indirizzo guardato.

Per farlo, dobbiamo scoprire l'indirizzo a cui è stata inviata la risorsa. A tale scopo, utilizzeremo l'id della transazione copiato in precedenza e chiederemo a e1 di recuperare i dettagli della transazione, in modo da individuare l'indirizzo corretto da aggiungere all'elenco dei portafogli di e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Scorrendo verso l'alto, oltre l'esadecimale dei dati della transazione, si vedrà l'indirizzo che ha ricevuto 100 esemplari del nostro nuovo bene, identificato dal suo valore esadecimale.

Prendete l'indirizzo e copiatelo per poterlo importare in e2.

Ora importiamo l'indirizzo in e2. Per farlo, si usa il comando importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Se ora controlliamo l'elenco delle emissioni di e2.

```
e2-cli listissuances
```

Si può notare che il nostro asset appena emesso è ora incluso nell'elenco. Il nodo e2 è anche in grado di determinare l'importo dell'asset emesso, insieme all'importo del token associato, poiché l'emissione è stata un'emissione non bloccata. Per abilitare l'uso dell'ID dell'asset alla mappatura dei nomi all'interno di Elements, occorre innanzitutto arrestare Elements.

```
e1-cli stop
```

Poi lo si riavvia con un parametro aggiuntivo che mappa l'esagono di una risorsa con l'etichetta fornita. Questo permette al nodo di visualizzare i dati sulla risorsa in un formato più leggibile. Se si preferisce, si può aggiungere questo parametro alla fine di elements.conf, in modo da non dover aggiungere l'argomento al demone ogni volta che lo si avvia. Per esempio:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Ma in questo caso utilizzeremo il metodo degli argomenti.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Interrogare nuovamente il nodo per ottenere un elenco di emissioni.

```
e1-cli listissuances
```

Questo dimostra che la mappatura del valore esadecimale dell'asset con la sua etichetta funziona. Controlliamo di nuovo l'elenco delle emissioni del nodo e2.

```
e2-cli listissuances
```

Si può notare che il nodo e2 non ha accesso a questa etichetta, perché le etichette sono disponibili solo per il nodo che le ha impostate. In effetti, è possibile assegnare un'etichetta diversa allo stesso asset hex su e2 rispetto a quella assegnata su e1. Per prima cosa fermiamo il nodo e2.

```
e2-cli stop
```

Riavviare con un'etichetta diversa assegnata all'esagono della nostra nuova risorsa.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Emissioni di elenchi da e2.

```
e2-cli listissuances
```

Le etichette degli asset sono locali a ciascun nodo, solo l'esagono dell'asset viene riconosciuto dagli altri nodi della rete.

La mappatura dell'etichetta con l'esagono dell'asset è utile quando si eseguono azioni come le transazioni e le interrogazioni sul saldo del portafoglio, in quanto consente di fare riferimento a un asset in modo abbreviato. Ad esempio, se volessimo inviare una parte della nostra nuova attività (una quantità di 10) da e1 a e2 senza usare l'etichetta.

Per prima cosa dobbiamo ottenere un indirizzo a cui inviare la risorsa.

```
e2-cli getnewaddress
```

Quindi utilizzare il comando sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Confermare la transazione generando un blocco.

```
generate 1
```

Verifica della ricezione del bene su e2.

```
e2-cli getwalletinfo
```

Possiamo vedere che la risorsa è stata effettivamente ricevuta.

Si noti che e2 mappa l'esagono dell'asset ricevuto e lo visualizza utilizzando la propria etichetta. Un modo più semplice per fare la stessa cosa sarebbe quello di utilizzare l'etichetta della risorsa di e1 durante l'invio.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Dietro le quinte, Elements mappa le etichette locali in valori esadecimali per semplificare l'uso delle risorse emesse.

In questa sezione abbiamo visto come emettere ed etichettare le attività. Nella prossima sezione vedremo come riemettere e distruggere le quantità di un'attività emessa.

## Riemissione di attività

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

In questa sezione imparerete come emettere una quantità maggiore di un'attività già emessa e come distruggere una determinata quantità di un'attività emessa.

La necessità di riemettere (creare di più) un'attività o di distruggerne una quantità è probabile che si verifichi quando l'attività rappresenta qualcosa che non ha una fornitura fissa. Questo potrebbe valere, ad esempio, per le attività che rappresentano l'oro custodito in un caveau; man mano che le unità d'oro entrano ed escono dal caveau, l'attività che rappresenta la fornitura del caveau deve essere regolata di conseguenza.

La riemissione di un importo di un'attività richiede la proprietà del token associato che è stato creato insieme all'attività quando è stata inizialmente emessa.

Quando si creano altre attività, non importa quale nodo abbia emesso l'attività in primo luogo, purché il nodo che sta riemettendo una quantità di attività sia in possesso di quello che viene comunemente chiamato token di riemissione dell'attività. Vedremo come creare inizialmente il token di riemissione, come usarlo per riemettere una quantità di asset e come trasferire il token di riemissione ad altri nodi, in modo che anch'essi abbiano il permesso di riemettere l'asset.

Avremo bisogno di accedere a due nodi Elements, che chiameremo e1 ed e2. I nodi sono stati resettati e la risorsa predefinita è stata divisa tra loro.

Faremo in modo che e1 emetta una quantità di 100 di una nuova attività e crei 1 token di riemissione per quella stessa attività. Per semplificare l'esempio, creeremo l'emissione come non bloccata. Procediamo quindi con l'emissione dell'attività e del relativo token di riemissione.

```
e1-cli issueasset 100 1 false
```

Si noti l'ID dell'asset e anche quello del token (di riemissione).

Poiché in seguito emetteremo altre attività da e2, dovremo prendere nota dell'ID della transazione in cui è stata emessa l'attività e utilizzarlo per importare l'indirizzo a cui è stata inviata l'attività.

Confermare la transazione.

```
e1-cli -generate 1
```

Ora controlleremo i dettagli della transazione utilizzando il comando gettransaction:

```
e1-cli gettransaction <txid>
```

Scorrendo l'esagono dei dati della transazione, si vedrà che nella transazione e1 ha ricevuto 1 token di riemissione e 100 dell'asset associato.

Fate una copia dell'indirizzo per poterlo importare in e2.

E ora importa l'indirizzo nel portafoglio di e2.

```
e2-cli importaddress <address>
```

Ora possiamo vedere che sia e1 che e2 sono a conoscenza dell'emissione di attività.

```
e1-cli listissuances
e2-cli listissuances
```

Attualmente e1 detiene una quantità di asset e 1 token di riemissione, mentre e2 non ne possiede.

```
e1-cli getwalletinfo
```

Si noti inoltre che e1 possiede una quantità minore di attività predefinita rispetto a prima, perché ha pagato un piccolo importo per coprire le commissioni di transazione. Questo importo deve essere riscosso da e1 quando il blocco creato viene maturato con una profondità di oltre 100 blocchi.

```
e2-cli getwalletinfo
```

Poiché e1 detiene il token di riemissione, può riemetterne altri. Ciò avviene utilizzando il comando reissueasset. Facciamo in modo che e1 riemetta altri 100 asset.

```
e1-cli reissueasset <asset-id> 100
```

La verifica della riemissione ha funzionato.

```
e1-cli getwalletinfo
```

Si può notare che e1 ora detiene 200 dell'asset, come previsto.

Poiché e2 non detiene una quantità di token di riemissione, riceveranno un errore se proveranno a riemettere l'attività.

```
e2-cli reissueasset <asset-id> 100
```

Notare il messaggio di errore.

È possibile visualizzare i dettagli della riemissione da e1 utilizzando il comando listissuances.

```
e1-cli listissuances
```

Si noti il flag `is_reissuance`.

Se ora inviamo a e2 una quantità di token di riemissione, essi saranno in grado di riemettere essi stessi una quantità di asset. Per prima cosa abbiamo bisogno di un indirizzo a cui inviarlo. Vale la pena notare che il token di riemissione viene trattato come qualsiasi altro asset all'interno di elements quando si inviano e si visualizzano i saldi e che può anche essere suddiviso in tagli più piccoli come qualsiasi altro asset, quindi non è necessario inviare 1 token di riemissione a e2 perché possa riemettere l'asset. Qualsiasi taglio sarà sufficiente. Generare un indirizzo per e2 per ricevere il token di riemissione.

```
e2-cli getnewaddress
```

Quindi inviare una frazione del RIT da e1 a e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confermare la transazione.

```
e1-cli -generate 1
```

Ora possiamo vedere che e2 mantiene lo 0,1 che gli è stato inviato.

```
e2-cli getwalletinfo
```

Ciò significa che e2 può ora riemettere una quantità maggiore dell'asset associato alla RIT che detiene nel suo portafoglio. Faremo in modo che e2 riemetta 500 esemplari dell'asset.

```
e2-cli reissueasset <asset-id> 500
```

Controllare il risultato della riemissione.

```
e2-cli getwalletinfo
```

Si può notare che e2 ora detiene l'importo riemesso nel suo portafoglio e che la RIT stessa non viene consumata nel processo di riemissione delle attività.

Distruggere una quantità di un'attività è qualcosa che può fare chiunque detenga almeno la quantità che viene distrutta, non è governato dal token di riemissione.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

In questa sezione abbiamo visto come emettere un asset e come utilizzare il token di riemissione che viene creato opzionalmente come parte dell'emissione dell'asset. Abbiamo anche visto che trasferire un token di riemissione è semplice come trasferire qualsiasi altro asset e che detenere una qualsiasi quantità di token di riemissione conferisce al titolare il diritto di emettere altri asset. È quindi molto importante controllare chi ha accesso ai token di riemissione nella vostra rete. Abbiamo anche visto come distruggere una quantità di un asset e che questo processo non è controllato dal possesso del token di riemissione.

# Federazione degli elementi

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Blocco della firma

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements supporta un modello di firma federata che consente di specificare il numero di membri della Strong Federation che devono firmare un blocco proposto per produrre un blocco valido.

In precedenza, e per facilità di esempio, abbiamo creato i blocchi utilizzando il comando `generate`, che non ha dovuto soddisfare un requisito di firma multipla affinché i blocchi creati fossero accettati dalla rete come validi.

Impostiamo i nostri nodi in modo che richiedano la creazione di blocchi multisig 2-of-2. Questo verrà impostato usando il parametro signblockscript, che può essere aggiunto al file di configurazione o passato al nodo all'avvio. Per inizializzare una catena con questo parametro, dobbiamo prima costruire lo script che la compone.

Lo faremo usando alcuni nodi esistenti, salveremo i dati che producono e poi cancelleremo la catena in modo da poterla riavviare usando il nostro parametro signblockscript. Questo è necessario perché lo script fa parte delle regole di consenso della rete e deve essere impostato all'inizializzazione della catena. Non può essere aggiunto in un secondo momento a una catena già esistente.

Avremo bisogno di accedere a due nodi Elements, che chiameremo e1 ed e2. I nodi sono stati resettati e la risorsa predefinita è stata divisa tra loro.

Assicurarsi che il parametro con_max_block_sig_size sia impostato a un valore elevato nel file elements.conf, altrimenti la firma a blocchi fallirà più avanti in questa sezione. Per questa esercitazione abbiamo impostato con_max_block_sig_size=2000.

Poiché resetteremo la blockchain e cancelleremo i portafogli associati a e1 ed e2, dovremo fare una copia degli indirizzi, delle chiavi pubbliche e delle chiavi private utilizzate per generare lo script di firma dei blocchi, in modo da poterli utilizzare in seguito.

Per prima cosa, è necessario che ciascuno di quelli che saranno i nodi di firma dei blocchi generi un nuovo indirizzo, di cui è necessario fare una copia.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Poi dobbiamo estrarre le chiavi pubbliche dagli indirizzi e annotarle per un uso successivo.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Quindi estraiamo le chiavi private, che reimporteremo in seguito in modo che i nodi possano firmare i blocchi dopo aver reinizializzato la blockchain e i dati del portafoglio.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Ora dobbiamo generare uno script redeem con i requisiti di multi-firma 2 su 2. Lo facciamo utilizzando il comando createmultisig e passando il primo parametro come 2 e fornendo poi due chiavi pubbliche. Per farlo, si utilizza il comando createmultisig, passando il primo parametro a 2 e fornendo due chiavi pubbliche. Sono queste chiavi che la proprietà deve essere dimostrata in seguito, quando il blocco viene creato.

Entrambi i nodi, e1 o e2, possono generare il multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

In questo modo si ottiene il nostro riscritto, che può essere copiato per essere utilizzato in seguito.

Ora dobbiamo cancellare i dati della blockchain e del portafoglio esistenti per poter ricominciare con il nuovo signblockscript come parte delle regole di consenso della catena. Per questo motivo è stato necessario fare una copia di alcuni dati, come le chiavi private che verranno utilizzate nella nuova catena per firmare i blocchi. È necessario farlo prima di procedere.

Con i dati del portafoglio e della catena esistenti cancellati, possiamo ora avviare i nostri nodi e far loro inizializzare una nuova catena usando il parametro signblockscript. Inseriamo -evbparams=dynafed:0::: per disabilitare l'attivazione di dynafed, perché in questo esempio non abbiamo bisogno di questa funzione avanzata.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Ora dobbiamo importare le chiavi private che abbiamo salvato in precedenza, in modo che i nostri nodi possano firmare e contribuire a completare i blocchi proposti.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

L'uso del comando generate dovrebbe ora dare un errore, poiché non soddisfa le regole di firma dei blocchi ora applicate dai nostri nodi.

```
e1-cli -generate 1
```

Per proporre un nuovo blocco, un nodo può chiamare il comando getnewblockhex. Questo comando restituisce l'esagono di un nuovo blocco che dovrà essere firmato prima di essere accettato da tutti i nodi della rete.

```
e1-cli getnewblockhex
```

Ricordate che il comando crea solo un blocco proposto, non ne genera uno.

A conferma di ciò, possiamo vedere che attualmente non ci sono blocchi nella nostra blockchain.

```
e1-cli getblockcount
```

Se proviamo a inviare il blocco esagonale senza prima firmarlo.

```
e1-cli submitblock <block-hex>
```

Riceviamo un messaggio che ci informa che la prova di blocco non è valida. Questo perché non è ancora stata firmata da due delle due parti richieste.

Facciamo in modo che e1 firmi il blocco proposto.

```
e1-cli signblock <block-hex>
```

Chiedere a e2 di firmare l'esagono.

```
e2-cli signblock <block-hex>
```

Si noti che e2 non firma l'output creato da e1 che firma il blocco proposto. Entrambi firmano l'esagono del blocco proposto indipendentemente dai risultati dell'altro.

Ora dobbiamo combinare le firme dei blocchi e1 ed e2. Entrambi i nodi possono farlo, tutto ciò di cui hanno bisogno è l'esagono del blocco firmato dall'altro nodo.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Si può notare che il comando combineblocksigs fornisce l'esagono del blocco firmato e lo stato di complete, che indica che l'esagono del blocco è pronto per essere inviato.

Ora entrambi i nodi possono inviare il blocco hex completato. Lo faremo fare a e1.

```
e1-cli submitblock <combined-signed-hex>
```

Verifica della validità dell'invio.

```
e1-cli getblockcount
e2-cli getblockcount
```

Si può notare che sia e1 che e2 hanno accettato il blocco come valido e lo hanno aggiunto alla punta delle loro copie locali della blockchain.

Per riassumere il processo. In questa sezione abbiamo:


- Proposta di un blocco.
- Lo abbiamo fatto firmare a ciascun nodo.
- Unire le firme.
- Verifica che le firme siano valide e che soddisfino la soglia di riscrittura della catena.
- Presentato il blocco.

Ogni nodo della rete convalida il blocco e lo aggiunge alla propria copia locale della blockchain.

### Blocco di posizionamento

Sebbene il processo appaia inizialmente complesso, la sequenza di firma dei blocchi in Elements è sempre la stessa e la configurazione iniziale deve essere eseguita una sola volta:

1. Impostazione iniziale (eseguita una volta)

2. Viene creato un indirizzo multi-firma chiamato `signblockscript` utilizzando le chiavi pubbliche dei firmatari di blocchi federati.

3. Lo script di riscatto viene utilizzato per avviare una nuova blockchain.

4. Produzione in blocco (in corso)

5. I blocchi proposti vengono generati e scambiati per la firma.

Una volta che un numero soglia di firmatari ha firmato il blocco proposto, questo viene combinato e sottoposto alla rete. Se soddisfa i criteri del `signblockscript' della catena, i nodi lo accettano come blocco valido.

## Elemento come catena laterale

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements è una piattaforma blockchain open-source di uso generale che può anche essere "agganciata" a una blockchain esistente, come Bitcoin. Quando è collegato a un'altra blockchain, si dice che Elements opera come una `sidechain`. Le sidechain consentono il trasferimento bidirezionale di beni da una catena all'altra. L'implementazione di Elements come sidechain consente di aggirare alcune delle limitazioni intrinseche della mainchain, pur mantenendo un buon grado di sicurezza fornito dagli asset protetti sulla mainchain.

Mentre una sidechain è a conoscenza della mainchain e della sua cronologia delle transazioni, la mainchain non è a conoscenza della sidechain e non è necessaria per il suo funzionamento. Ciò consente alle sidechain di innovare senza restrizioni o ritardi associati alle proposte di miglioramento del protocollo della mainchain. Piuttosto che cercare di modificarlo direttamente, l'estensione del protocollo principale permette alla mainchain stessa di rimanere sicura e specializzata, sostenendo il buon funzionamento della sidechain.

Estendendo le funzionalità di Bitcoin e sfruttando la sua sicurezza sottostante, una sidechain basata su Elements è in grado di fornire nuove funzionalità che in precedenza non erano disponibili per gli utenti della mainchain. Un esempio di sidechain basata su Elements in produzione è Liquid Network.

Per inizializzare una blockchain Elements come sidechain, è necessario utilizzare il parametro di script federated peg. Questo parametro può essere impostato nel file di configurazione di un nodo o passato all'avvio.

Lo script peg federato definisce quali membri della federazione forte possono svolgere funzioni di peg-in e peg-out. Questi funzionari sono chiamati `Watchmen`, in quanto controllano la mainchain e la sidechain alla ricerca di transazioni peg-in e peg-out valide e le eseguono se sono valide. Peg-out" significa spostare gli asset pegged dalla sidechain alla mainchain e "peg-in" significa spostare gli asset pegged dalla mainchain alla sidechain. Quando diciamo "spostare nella sidechain", in realtà intendiamo dire che i fondi vengono bloccati in un indirizzo multi-firma sulla mainchain e una quantità corrispondente dell'asset viene creata sulla sidechain Elements. Quando si dice "uscire dalla sidechain", si intende che gli asset vengono distrutti sulla sidechain di Elements e l'importo corrispondente viene rilasciato dai fondi bloccati sulla mainchain. Il permesso di eseguire le funzioni di peg-in e peg-out richiede che i funzionari dimostrino la proprietà delle chiavi pubbliche utilizzate nello script di peg federato. Ciò avviene con l'uso delle chiavi private corrispondenti.

Per creare uno script peg federato, quindi, è necessario che ogni nodo generi una chiave pubblica. Dobbiamo anche memorizzare le chiavi private associate per un uso successivo, poiché dovremo cancellare tutti i dati della catena esistente e inizializzare una nuova catena usando lo script peg federato. Questo perché lo script peg federato fa parte delle regole di consenso di una sidechain e non può essere applicato a una blockchain esistente, non peg, in un secondo momento.

Generiamo quindi un indirizzo per ciascuno dei nostri nodi, memorizziamo i dati rilevanti per un uso successivo e generiamo lo script del peg federato che useremo per inizializzare la nostra sidechain in seguito.

Per prima cosa è necessario che ciascuno dei nostri nodi, che fungeranno da sentinelle della nostra rete, generi un nuovo indirizzo.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Quindi convalidiamo l'indirizzo per ottenere le chiavi pubbliche.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

E poi recuperare le chiavi private associate a ciascun indirizzo.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Memorizzare le chiavi private e pubbliche per un uso successivo.

Ora dobbiamo cancellare i dati della blockchain e del portafoglio esistenti, poiché inizializzeremo una nuova catena utilizzando uno script peg federato. Potete farlo ora. Non dimenticate di avviare il demone Bitcoin, che ci servirà per il peg-in.

Ora possiamo inizializzare una nuova catena con uno script di peg federato creato utilizzando le chiavi pubbliche che abbiamo memorizzato in precedenza. I numeri che inseriamo e che circondano le nostre chiavi pubbliche definiscono e delimitano il numero di chiavi utilizzate e la proprietà delle chiavi che deve essere dimostrata per effettuare il peg-in e il peg-out della nostra sidechain.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Ora importeremo le chiavi private che abbiamo salvato in precedenza, in modo che i nostri nodi possano successivamente firmare e completare il trasferimento delle risorse tra le catene e soddisfare i requisiti dello script del peg federato.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Ora dobbiamo far maturare alcuni blocchi su entrambe le catene. La maturazione dei blocchi è un requisito del processo di peg, in quanto protegge dalle riorganizzazioni dei blocchi sulla mainchain che portano a un'inflazione dell'offerta di asset pegati all'interno della sidechain.

Per mantenere questa sezione focalizzata sul peg federato, genereremo i blocchi senza usare il modello di firma dei blocchi visto nell'ultima sezione e torneremo a usare il comando "generate" per creare nuovi blocchi.

```
b-cli generate 101
e1-cli generate 1
```

Non abbiamo necessariamente bisogno di generare blocchi per gli elementi. Ma generiamone comunque uno. È una buona pratica per evitare potenziali incoerenze.

Ora la nostra catena è pronta per il peg-in. Per effettuare il peg-in è necessario generare un tipo speciale di indirizzo utilizzando il comando getpeginaddress. Si noti che il tempo che intercorre tra la generazione di un indirizzo peg-in con getpeginaddress e la sua rivendicazione con claimpegin deve essere ridotto al minimo. Gli indirizzi peg-in non sono durevoli a lungo termine e non devono essere riutilizzati.

```
e1-cli getpeginaddress
```

Si può notare che il comando crea un nuovo indirizzo mainchain e un nuovo script che dovrà essere soddisfatto per richiedere i fondi peg-in. L'indirizzo della mainchain è un indirizzo "pay to script hash" che sarà utilizzato dai funzionari che svolgono il ruolo di Watchmen all'interno della rete Elements.

Come getnewaddress, getpeginaddress aggiunge un nuovo segreto al portafoglio del nodo chiamante, quindi è importante tenere conto del backup del file del portafoglio nel processo di gestione del nodo.

Ora invieremo alcuni bitcoin dalla mainchain alla sidechain. Il nostro portafoglio di test di regressione della mainchain contiene già alcuni fondi.

```
b-cli getwalletinfo
```

Possiamo vedere che il portafoglio contiene 50 bitcoin. Invieremo un bitcoin dalla mainchain alla sidechain. Dobbiamo inviare i fondi all'indirizzo della mainchain che il nostro nodo ha generato in precedenza.

```
b-cli sendtoaddress <e1-pegin-address>
```

Dobbiamo conservare l'ID di questa transazione perché ci servirà come prova di finanziamento in seguito.

Ora possiamo vedere che il saldo del portafoglio della mainchain è diminuito dell'importo che abbiamo inviato, più un ulteriore piccolo importo per coprire le spese di transazione.

```
b-cli getwalletinfo
```

Dobbiamo far maturare nuovamente la transazione.

```
b-cli generate 101
```

Per far sì che il nostro nodo Elements rivendichi i fondi peg-in, dobbiamo ottenere la "prova" che la transazione peg-in è stata effettuata. La prova crittografica utilizza l'ID della transazione di finanziamento per calcolare il percorso di Merkel e dimostra che la transazione è presente in un blocco confermato.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Abbiamo bisogno anche dei dati grezzi delle transazioni.

```
b-cli getrawtransaction <tx-id>
```

Con la prova e i dati grezzi della transazione peg-in, il nostro nodo elemento può ora rivendicare il peg-in utilizzando la transazione grezza e la prova della transazione.

```
e1-cli claimpegin <raw> <proof>
```

Si noti che c'è un terzo parametro opzionale che avremmo potuto fornire a claimpegin. Questo terzo parametro può essere usato per specificare l'indirizzo della catena laterale a cui inviare i fondi rivendicati. Nel nostro esempio non è stato necessario, poiché il comando è stato chiamato dallo stesso nodo che possiede l'indirizzo a cui sono destinati i fondi rivendicati.

Controllo del saldo di e1.

```
e1-cli getwalletinfo
```

Generare un blocco per confermare la richiesta.

```
e1-cli generate 1
```

Controllo del saldo di e1.

```
e1-cli getwalletinfo
```

Si può notare che il peg-in è stato rivendicato con successo.

Per il peg-out, il processo è simile. Viene generato un indirizzo, vi si inviano i fondi e questi vengono rilasciati se la transazione è valida. Non tratteremo l'intero processo di peg-out perché comporta un lavoro sulla mainchain che esula dagli scopi di questo corso. I passaggi in termini di eventi Elements sono: un indirizzo viene generato sulla mainchain.

```
b-cli getnewaddress
```

I fondi vengono inviati all'indirizzo della mainchain da un nodo Elements utilizzando il comando sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Generazione di un blocco per confermare la transazione.

```
e1-cli generate 1
```

Controllare il saldo del portafoglio del nodo.

```
e1-cli getwalletinfo
```

E vedere che il saldo è diminuito.

In questa sezione abbiamo visto come:


- Generare uno script peg federato.
- Inizializza una nuova catena che utilizza lo script come regola di parametro del consenso di rete.
- Invia fondi dalla mainchain alla sidechain.
- Rivendicare i fondi all'interno della sidechain di Elements.
- Capire come si avvia l'invio di fondi alla mainchain.

### FederatedPegScript

Per consentire a Elements di funzionare come sidechain, il blocco genesis nella sua blockchain deve essere creato con un `fedpegscript` al suo posto. Ciò avviene passando il parametro `fedpegscript` all'avvio del nodo. Lo script farà quindi parte delle regole di consenso della blockchain Elements e consentirà la convalida e l'esecuzione delle richieste di peg-in e peg-out.

Il `fedpegscript` è composto da chiavi pubbliche controllate da coloro che sono autorizzati a eseguire le azioni peg. Di seguito viene mostrato un esempio di formato di un fedpegscript a 2 firme su 2:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Nota: I caratteri al di fuori delle chiavi pubbliche sono delimitatori che indicano i requisiti della chiave pubblica e di `n di m`. Ad esempio, il modello per un fedpegscript 1-of-1 sarebbe "5121<chiave pubblica 1>51ae".

### Piolo-in

Prima che un peg-in possa essere accettato da una sidechain di Elements, deve avere sufficienti conferme sulla mainchain. Ciò è necessario per evitare l'inflazione dell'offerta dell'asset pegged sulla sidechain di Elements che potrebbe essere causata da una riorganizzazione della mainchain.

Brevi riorganizzazioni della punta della blockchain Bitcoin sono previste come parte del normale funzionamento del meccanismo di consenso Proof of Work (PoW). Per questo motivo, Elements accetta che un peg-in sia valido solo quando ha una profondità sufficiente all'interno della blockchain Bitcoin. Questo serve a evitare che Elements accetti lo stesso peg-in più di una volta.

### Uscita a pioli

Un peg-out si verifica quando un nodo Elements chiama il comando `sendtomainchain`, che prende in input un indirizzo della mainchain (la destinazione del peg-out) e l'ammontare dell'asset pegged da `ritirare`. In questo modo si crea una transazione di peg-out sulla sidechain. Una volta che i Funzionari che agiscono come Watchmen rilevano che la transazione di peg-out è stata confermata sulla sidechain, si occupano di rilasciare effettivamente l'asset sulla mainchain alla destinazione di peg-out, come abbiamo imparato nelle sezioni precedenti del corso.

## Elementi come Blockchain indipendente

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Finora abbiamo visto come far funzionare Elements come sidechain. Tuttavia, può anche funzionare come soluzione blockchain autonoma con un proprio asset nativo predefinito. In questa configurazione, una blockchain Elements mantiene tutte le caratteristiche di un'implementazione sidechain, come le transazioni riservate e gli asset emessi, ma non ha bisogno di peg-in o peg-out per aggiungere o rimuovere dalla circolazione gli asset predefiniti.

In questa sezione ci occuperemo di:

Inizializza una nuova blockchain Elements con un asset predefinito chiamato `newasset`.

Specificare 1.000.000 di `newasset` da creare insieme a 2 gettoni di riemissione per esso.

Reclama tutte le monete `newasset` spendibili da chiunque.

Rivendica tutti i gettoni di riemissione che chiunque può spendere per "newasset".

Inviare la risorsa e il relativo token di riemissione al portafoglio di un altro nodo.

Ripubblicare altri 'newasset' da entrambi i nodi.

Per inizializzare una rete Elements e farla funzionare come una blockchain indipendente, ogni nodo deve essere avviato con alcuni parametri di base. Vengono utilizzati per indicare al nodo di non cercare di convalidare i peg-in da un'altra blockchain, il nome dell'asset predefinito della rete e la quantità di asset predefinito e di token di riemissione associato da creare.

Avvieremo ora una nuova catena utilizzando questi parametri sui nostri due nodi Elements collegati. Chiameremo l'asset predefinito `newasset` e ne emetteremo un milione e due gettoni di riemissione `newasset`.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Si noti che gli importi qui utilizzati sono nel taglio più piccolo che la rete può accettare, quindi i duecento milioni di gettoni di riemissione equivalgono in realtà a due gettoni interi. Lo stesso vale per il taglio delle monete gratuite iniziali.

Controllare i saldi attuali del portafoglio del nostro nodo.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Si può notare che l'inizializzazione ha funzionato correttamente.

Poiché l'emissione iniziale di beni viene creata come "chiunque può spendere", faremo in modo che e1 li rivendichi tutti, in modo da rimuovere l'accesso di e2 ad essi.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Non è necessario specificare 'newasset' come asset da inviare, poiché è già l'asset predefinito e quindi anche l'asset predefinito utilizzato per pagare le tariffe di rete.

All'interno di Elements, è possibile inviare più tipi di asset allo stesso indirizzo, quindi possiamo riutilizzare l'indirizzo appena generato per ricevere l'asset predefinito e usarlo come indirizzo di destinazione per i token di riemissione.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confermare le transazioni.

```
e1-cli generate 101
```

Verificheremo che e1 sia l'unico possessore dell'asset e del suo token di riemissione.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

E come possiamo vedere è proprio così.

Ora invieremo una parte del 'newasset' a e2, che attualmente ha un saldo pari a zero.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Si noti che non è stato necessario specificare il tipo di risorsa da inviare, poiché `newasset` è stato creato come risorsa predefinita della rete

Inviamo anche alcuni dei token di riemissione per `newasset` a e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confermare le transazioni.

```
e1-cli generate 101
```

Possiamo verificare che i portafogli siano stati aggiornati di conseguenza.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Ora riemetteremo alcune delle risorse predefinite da e1. Si noti che la possibilità di farlo è abilitata dal parametro di avvio initialreissuancetokens. Se omesso o impostato a zero, si otterrà una risorsa predefinita che non potrà essere riemessa in un secondo momento.

```
e1-cli reissueasset newasset 100
```

Abbiamo potuto usare l'etichetta di `newasset` invece di dover fornire il valore esadecimale dell'id, perché una catena di elementi etichetta sempre la sua risorsa predefinita.

Verifica che la riemissione dell'asset predefinito abbia funzionato:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Dimostreremo ora che, poiché e2 possiede alcuni token di riemissione di `newasset`, può anche riemettere l'asset predefinito.

```
e2-cli reissueasset newasset 100
```

Verifica del funzionamento della riemissione dell'asset predefinito da parte di e2.

```
e2-cli generate 101
e2-cli getwalletinfo
```

In questa sezione abbiamo configurato Elements come blockchain indipendente e abbiamo verificato che le funzionalità di base funzionino come ci aspetteremmo.

Abbiamo utilizzato i parametri di avvio per:

Inizializza una nuova blockchain Elements con un asset predefinito chiamato "newasset".

Specificare la quantità di risorsa predefinita da creare all'inizializzazione della catena.

Creare alcuni gettoni di riemissione per l'asset predefinito e riemettere altri asset predefiniti da entrambi i nodi.

Sulla nostra rete blockchain Elements indipendente, tutte le altre operazioni transazionali opereranno nello stesso modo degli esempi trattati nelle sezioni principali del corso, ma utilizzeranno "newasset" invece di "bitcoin" come asset predefinito e a pagamento.

### Parametri di avvio del nodo e di inizializzazione della catena

Per dire a un nodo Elements di operare come una blockchain indipendente è necessario utilizzare alcuni parametri. Vediamo ora ciascuno di essi e scopriamo a cosa serve.

#### `validatepegin=0`

Poiché una blockchain indipendente non ha bisogno di convalidare le transazioni peg-in o peg-out, è necessario disabilitare tali controlli. Con questa impostazione, non è necessario eseguire il software client Bitcoin o memorizzare una copia della blockchain Bitcoin, poiché la rete Elements funzionerà in modo indipendente.

#### `defaultpeggedassetname`

Consente di specificare il nome dell'asset predefinito creato all'inizializzazione della blockchain.

#### `inizialialfreecoins`

Il numero (nell'equivalente dell'unità Satoshi di Bitcoin) dell'asset predefinito da creare.

#### `token iniziali di riemissione`

Il numero (nell'equivalente dell'unità Satoshi di Bitcoin) dei token di riemissione per l'asset predefinito da creare. Senza questo valore sarebbe impossibile creare altri asset di default. Se non si vuole che sia possibile creare altri asset predefiniti, questo valore può essere impostato a zero o omesso.

Utilizzando questi parametri, la procedura comune per avviare un nodo sarà simile a questa:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Operazioni di base

Il parametro `defaultpeggedassetname` applica un'etichetta all'attività predefinita. Senza questa impostazione, la risorsa predefinita sarà automaticamente chiamata `bitcoin`. Nelle sezioni precedenti, quando abbiamo inviato risorse emesse da noi stessi a un altro nodo, abbiamo dovuto specificare l'esagono della risorsa o l'etichetta della risorsa applicata localmente per indicare a Elements quale risorsa stavamo inviando. Poiché `defaultpeggedassetname` si applica a tutti i nodi, non abbiamo bisogno di nominarlo quando lo inviamo, anche se il suo nome non è `bitcoin`. Ogni funzione che prima avrebbe inviato `bitcoin` per impostazione predefinita, ora invierà qualsiasi cosa si sia scelto di etichettare come risorsa predefinita.

Per questo motivo, l'invio di 10 esemplari del nuovo asset predefinito a un indirizzo è semplice come:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Se avete fornito al nodo anche un valore di `initialreissuancetokens` maggiore di zero, sarete anche in grado di riemettere altri asset di default, cosa che non è possibile se eseguite Elements come sidechain.

A tal fine, qualsiasi nodo che detenga una quantità di token associata all'asset predefinito deve solo emettere un comando nella forma:

```
e1-cli reissueasset <default asset name> <amount>
```

Utilizzando i parametri di cui sopra è possibile far funzionare Elements come una blockchain autonoma con un proprio asset predefinito, disaccoppiato da Bitcoin e da altre blockchain.

## Conclusione

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

In questo corso abbiamo imparato che Elements è un protocollo di rete open-source che può essere implementato come sidechain di un'altra blockchain o come soluzione blockchain autonoma.

Abbiamo visto che il codice sorgente e il sito web di Elements (https://github.com/ElementsProject/elements) sono ospitati su GitHub e che esistono forum di discussione della comunità, come Build On L2 (https://community.liquid.net/c/developers/) o Liquid Developers Telegram (https://t.me/liquid_devel), che possono essere utilizzati per saperne di più sulla distribuzione e lo sviluppo di applicazioni su Elements e Liquid. Sono state illustrate caratteristiche chiave come le Transazioni riservate e gli Asset emessi, oltre a come i membri di una Strong Federation consentono la firma federata dei blocchi e il meccanismo 2-Way Peg.

Il passo successivo è quello di sfidare se stessi con un quiz cumulativo che copre tutte le sezioni precedenti, per poi iniziare il viaggio di Elements... buona fortuna!

# Conclusione

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Recensioni e valutazioni

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusione

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Congratulazioni per aver completato questo corso!

Siamo entusiasti che abbiate raggiunto con successo questa pietra miliare nel vostro percorso di apprendimento. Grazie alla vostra dedizione e al vostro impegno, avete acquisito conoscenze e competenze preziose che vi saranno utili nel vostro sviluppo professionale.