---
name: Costruire con Elements e Liquid Network
goal: Imparare a utilizzare e sviluppare con la piattaforma blockchain open-source Elements e le sue caratteristiche principali
objectives: 

  - Comprendere i concetti fondamentali della piattaforma blockchain Elements e della sidechain Liquid.
  - Imparate a configurare ed eseguire i nodi Elements per le configurazioni standalone e sidechain.
  - Acquisire esperienza pratica con la firma a blocchi federata e il Federated 2-Way Peg (Ancoraggio Federato bidirezionale).
  - Impostare e gestire ambienti blockchain sicuri ed efficienti per casi d'uso reali.

---
# Costruire su Liquid Network ed Elements

Scoprirete le caratteristiche e le funzionalità avanzate di Liquid Network ed Elements e imparerete a utilizzare efficacemente questi strumenti per migliorare i vostri progetti di sviluppo. Questa formazione fornisce una base teorica e pratica completa, consentendovi di padroneggiare funzionalità quali "Confidential Transaction", "Issued Asset" e "Federated Block Signing" (Firma federata dei blocchi).

Liquid, basato sul framework Elements, è progettato per migliorare la privacy, la scalabilità e la funzionalità delle soluzioni finanziarie e tecniche. In questo corso, acquisirai esperienza pratica riguardo alla l'emissione e la gestione di asset, il "Federated 2-Way Peg" (Ancoraggio Federato bidirezionale) e l'uso di strumenti come `elementsd` ed `elements-cli`, consentendovi di creare soluzioni innovative su misura per le vostre esigenze.

Questo corso è adatto agli sviluppatori di tutti i livelli di esperienza. I principianti e gli utenti intermedi troveranno spiegazioni accessibili ed esempi pratici, mentre gli utenti avanzati potranno approfondire i dettagli tecnici e le caratteristiche meno conosciute di Liquid ed Elements.

Unisciti a noi per elevare le tue competenze, sbloccare il pieno potenziale di Liquid ed Elements e creare strumenti d'impatto per il futuro dell'innovazione di Liquid.
+++

# Introduzione

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Panoramica del Corso

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::

Benvenuto al corso SID202!

L'obiettivo di *Elements Academy* è di presentare e spiegare i concetti chiave di *Elements*, la piattaforma open-source su cui è costruita la sidechain Liquid. Al termine di questo corso, dovresti possedere una solida comprensione delle principali funzionalità di Elements, come le confidential transactions e gli issued assets, nonché dei processi coinvolti nel funzionamento di Elements Core. Ogni sezione del corso comprende lezioni con testi esplicativi e video, che si concludono con un quiz.

Questo corso mira a insegnarti come utilizzare e sviluppare con la piattaforma open-source Elements, con focus sulla rete Liquid. Scoprirai come queste tecnologie possano migliorare la privacy, la scalabilità e le funzionalità dei tuoi progetti di sviluppo. Che tu sia un principiante o uno sviluppatore esperto, questo corso ti fornirà una solida base per padroneggiare i concetti fondamentali di Elements e Liquid e le loro applicazioni pratiche.

**Sezione 1: Introduzione**  
Inizieremo con una panoramica completa dei concetti di Elements. Imparerai come questa piattaforma è stata progettata per fornire una base modulare e flessibile per la creazione di sidechain come Liquid. L'obiettivo è comprendere la struttura di Elements prima di passare alle applicazioni pratiche.

**Sezione 2: Elements**  
Questa sezione si concentrerà sul funzionamento di Elements. Imparerai come configurare un nodo Elements, gestirlo in modalità autonoma o utilizzarlo come sidechain.

**Sezione 3: Utilizzo di Elements – Casi di Utilizzo Pratici**  
Dopo aver appreso le basi teoriche, ci concentreremo sulle applicazioni pratiche di Elements. Imparerai a eseguire transazioni confidenziali, emettere asset e gestire la riemissione degli asset.

**Sezione 4: Federazione Elements**  
Qui esploreremo i meccanismi avanzati, inclusa la firma federata dei blocchi, l'utilizzo di Elements come sidechain e la creazione di blockchain indipendenti. Questa sezione ti aiuterà a comprendere come garantire la sicurezza, l'integrità e l'interoperabilità delle blockchain basate su Elements.

Pronto a scoprire il potenziale di Elements e della sidechain Liquid? Iniziamo!

## Panoramica su Elements

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::

Elements è una piattaforma blockchain, che può essere utilizzata come una ["sidechain"](https://planb.academy/resources/glossary/sidechain), e consente di accedere a potenti funzionalità sviluppate dai membri della community, come le ["Confidential Transaction"](https://elementsproject.org/features/confidential-transactions) e le ["Issued Assets"](https://elementsproject.org/features#issuedassets).

Elements, nella sua essenza, è un protocollo che consente di ottenere consenso riguardo alla storia delle transazioni e alle regole che governano il trasferimento e la creazione di asset memorizzati in un libro mastro distribuito della blockchain.

Ulteriori informazioni di base su Elements sono disponibili sul sito web del progetto Elements (https://elementsproject.org/), sul blog ufficiale di Liquid (https://blog.liquid.net/) e sul portale degli sviluppatori (https://liquid.net/devs).

### Elements

Lanciato nel 2015, Elements riduce i costi interni di sviluppo e ricerca e sfrutta la più recente tecnologia blockchain, aprendo molti nuovi casi d'uso per la sua implementazione. Una blockchain basata su Elements può funzionare come blockchain indipendente o essere collegata a un'altra e funzionare come sidechain. L'esecuzione di Elements come Sidechain consente di trasferire in modo verificabile gli asset tra blockchain diverse.

Elements è stato sviluppato sulle basi del codice di Bitcoin, che è stato poi implementato, e consente agli sviluppatori di familiarizzare con l'_API bitcoind_ in modo rapido e a costi contenuti, per creare blockchain funzionanti e anche di testare progetti "proof-of-concept" (la proof-of-concept è una prova ottenuta da un progetto pilota, che viene eseguito per dimostrare che un prodotto, o un progetto, è realizzabile). Essendo costruito sulla base del codice di Bitcoin, Elements può anche funzionare come banco di prova per le modifiche al protocollo Bitcoin stesso.

Di seguito sono elencate alcune delle caratteristiche principali di Elements.

#### Confidential Transactions

Per impostazione predefinita, tutti gli indirizzi di Elements sono resi confidenziali utilizzando le Confidential Transactions. Il Blinding è il processo mediante il quale l'importo e il tipo di asset trasferito vengono nascosti crittograficamente a tutti, tranne che ai partecipanti e a coloro che scelgono di rivelare la blinding key. Con Confidential Transaction si intende dire che le transazioni di Elements sono offuscate, nascondendo sia l'ammontare sia il tipo di asset trasferito.

#### Issued Assets

Gli "Issued Assets" su Elements consentono di emettere e trasferire più tipi di asset tra i partecipanti alla rete. Un Issued Asset beneficia anche delle Confidential Transactions e può essere riemesso o distrutto da chiunque possieda il relativo token.

#### Federated 2-Way Peg (Ancoraggio Federato bidirezionale)

Elements è una piattaforma blockchain di uso generale che può anche essere "ancorata" a una blockchain esistente (come Bitcoin) per consentire il trasferimento bidirezionale di asset da una chain all'altra. L'implementazione di Elements come sidechain consente di aggirare alcune delle proprietà intrinseche della chain principale, pur mantenendo un buon grado di sicurezza fornito dagli asset protetti sulla chain principale.

#### Signed Blocks (Blocchi firmati)

Elements utilizza una "Strong Federation" di firmatari, chiamati ["Block Signers"](https://planb.academy/resources/glossary/blocksigners), che firmano e creano blocchi in modo affidabile e tempestivo. In questo modo si elimina la latenza delle transazioni derivata dal processo di mining basato sulla "PoW" (Proof-of-work, prova di lavoro), che è soggetta alla varianza nei tempi di emissione dei blocchi, a causa della loro distribuzione casuale (questa caratteristica si può mostrare creando una _curva di Poisson_). Il processo di "Federated Block Signing" (Firma federata dei blocchi) consente di creare i blocchi in maniera affidabile senza la necessità di fiducia in terze parti o l'utilizzo del mining basato su `algoritmi` computazionali.

Elements aggiunge tutte queste funzionalità al codice di Bitcoin Core, estendendo gli utilizzi del protocollo mainchain e consentendo nuovi casi d'uso commerciali quando viene usato come sidechain o come soluzione blockchain indipendente.

# Elements

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Come funziona Elements

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::

Elements fornisce una soluzione tecnica ai problemi che gli utenti della blockchain devono affrontare quotidianamente: latenza delle transazioni, mancanza di privacy e rischio di fungibilità.

Elements supera questi problemi grazie all'uso della "Federated Block Signing" (Firma federata dei blocchi) e delle "Confidential Transaction" (Transazioni riservate).

A differenza della rete Bitcoin, il processo di firma dei blocchi all'interno di Elements non si basa su Dynamic Membership Multiparty Signatures (DMMS) e Proof of Work (PoW). Elements utilizza invece una "Strong Federation" di firmatari, chiamati "Block Signers" (Firmatari dei Blocchi), che possono firmare e creare blocchi in modo affidabile e tempestivo. In questo modo si elimina la latenza delle transazioni del processo di mining _PoW_, che è soggetto a grandi variazioni di tempo dei blocchi a causa della sua [distribuzione casuale di tipo Poisson](https://it.wikipedia.org/wiki/Distribuzione_di_Poisson). Il processo di "Federated Block Signing" consente di ottenere una creazione affidabile dei blocchi senza introdurre la necessità di una fiducia da parte di terzi.

Elements può funzionare come sidechain di un'altra blockchain, come Bitcoin, o come blockchain autonoma senza dipendere da altre reti.

Quando viene utilizzata come sidechain, la Federazione contiene anche membri che consentono il trasferimento sicuro e controllato di asset tra una chain principale e una sidechain Elements. Il trasferimento controllato di asset è chiamato "Federated 2-Way Peg" (Ancoraggio Federato Bidirezionale) e i membri che svolgono il ruolo di trasferimento degli asset sono chiamati ["Watchmen" (Guardiani)](https://planb.academy/resources/glossary/watchmen).

I processi coinvolti nella gestione di una rete Elements e i ruoli dei partecipanti alla rete sono importanti per comprendere il funzionamento di Elements.

Sia che venga implementata come sidechain o come blockchain indipendente, Elements si avvale di "Strong Federations" di "Block Signers" (Firmatari dei Blocchi) per emettere i blocchi.

### Strong Federations

Elements utilizza un modello di consenso proposto per la prima volta da Blockstream, chiamato "Strong Federations". Questo tipo di Federazione non ha bisogno di Proof-of-Work (PoW) e si affida invece alle azioni collettive di un gruppo di partecipanti che diffidano l'uno dell'altro, chiamati "Functionaries" (Funzionari).

I ruoli che un Funzionario può ricoprire all'interno di una "Strong Federations" sono: "Block Signer" (Firmatario del Blocco) e "Watchman" (Guardiano). I Firmatari sono necessari se si esegue Elements in modalità sidechain o standalone blockchain, mentre i Watchmen sono necessari solo in una configurazione sidechain.

Le azioni che un membro di una Federazione può eseguire sono suddivise tra due ruoli distinti per migliorare la sicurezza e limitare i danni che un attaccante può causare.

Se combinati, i ruoli di questi partecipanti consentono a Elements di fornire sia una rapida creazione di blocchi (una conferma più rapida e definitiva delle transazioni) sia asset sicuri e trasferibili (asset ancorati direttamente collegabili a un'altra blockchain).

È possibile leggere il whitepaper delle Strong Federations qui: https://blockstream.com/strong-federations.pdf

### I Block Signers

Una blockchain come quella di Bitcoin viene estesa quando chiunque faccia parte di un gruppo dinamico di firmatari di blocchi allunga la chain dando prova del lavoro svolto. La natura dinamica dell'insieme introduce i problemi di latenza propri di questi sistemi.

Utilizzando un insieme fisso di firmatari, il modello federato sostituisce l'insieme dinamico con un gruppo noto, e uno schema a più firme. La riduzione del numero di partecipanti necessari per estendere la blockchain aumenta la velocità e la scalabilità del sistema, mentre la convalida da parte di tutte le parti garantisce l'integrità della cronologia delle transazioni.

La firma a blocchi federata consiste in diverse fasi:

- Fase 1 - I "Block Signers" (Firmatari del Blocco) propongono a turno i blocchi candidati a tutti gli altri Firmatari partecipanti.
- Fase 2 - Ogni Firmatario segnala la propria intenzione impegnandosi a firmare il blocco candidato.
- Fase 3 - Se la soglia data per un pre-impegno è soddisfatta, ogni Firmatario firma il blocco.
- Fase 4 - Se la soglia di firma (che può essere diversa da quella della fase 3) è soddisfatta, il blocco viene accettato e inviato alla rete. La Federazione  ha raggiunto il consenso sull'ultimo blocco di transazioni.
- Fase 5 - Il blocco successivo viene proposto dal successivo Firmatario in modo circolare, e il processo si ripete.

Poiché la generazione dei blocchi di una Federazione non è probabilistica e si basa su un insieme fisso di firmatari, non sarà mai soggetta a riorganizzazioni di molteplici blocchi. Ciò consente una significativa riduzione dei tempi di attesa associati alla conferma delle transazioni. Inoltre, elimina l'incentivo a fare mining per profitto (per esempio, per ottenere il reward dei blocchi) e lo sostituisce con un incentivo a partecipare in modo produttivo a una rete in cui tutti i partecipanti hanno lo stesso obiettivo condiviso: garantire che la rete continui a funzionare in modo vantaggioso per tutti. Ciò avviene senza introdurre un singolo punto di fallimento o requisiti di fiducia più elevati.

### Elements come sidechain - Watchmen e il Federated 2-Way Peg

Se gestita come sidechain, alcuni membri della Strong Federation hanno un ruolo aggiuntivo da svolgere, quello dei "Watchmen" (Guardiani). I Guardiani sono responsabili del trasferimento degli asset in entrata e in uscita da una sidechain Elements, processi noti come `Peg-In` (Ancoraggio in Ingresso) e `Peg-Out` (Ancoraggio in Uscita).

Affinché una sidechain operi in modo affidabile, deve consentire ai partecipanti di verificare che il numero di asset sia controllato e verificabile. Una sidechain di Elements utilizza un _"Federated 2-Way Peg"_ (Ancoraggio Federato bidirezionale) per consentire il trasferimento bidirezionale di asset all'interno e all'esterno della blockchain di Elements. Questo soddisfa i requisiti di emissione dimostrabile e trasferimento tra chain diverse.

La funzione "Federated 2-Way Peg" (Ancoraggio Federato a due Vie) consente a un asset di essere interoperabile con altre blockchain e rappresentativo dell'asset nativo di un'altra blockchain. Agganciando la propria blockchain a un'altra, è possibile estendere le capacità della mainchain (chain principale) e superare alcune delle sue limitazioni intrinseche.

Ad alto livello, i trasferimenti nella sidechain avvengono quando qualcuno invia asset della mainchain a un indirizzo controllato da un "Watchmen multi-signature wallet" (il wallet multi-firma dei guardiani). Questo blocca di fatto gli asset sulla mainchain. Il Guardiano convalida quindi la transazione e rilascia all'interno della sidechain la stessa quantità di asset. Gli asset rilasciati vengono inviati a un wallet della sidechain che può dimostrare di avere dei diritti di proprietà sugli asset originali della mainchain. Questo processo sposta effettivamente gli asset dalla mainchain alla sidechain.

Per trasferire gli asset alla mainchain, un utente effettua una speciale transazione di peg-out sulla sidechain. Questa transazione viene controllata dai Guardiani, che poi firmano una transazione di spesa dal wallet multi-firma che controllano sulla mainchain. Un numero minimo di partecipanti alla federazione deve firmare la transazione prima che diventi valida sulla mainchain. Quando i Guardiani rimandano un asset alla mainchain, distruggono anche l'importo corrispondente sulla sidechain, trasferendo di fatto gli asset tra le blockchain.

## Impostazione ed esecuzione di Elements

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::

Poiché Elements si fonda sul codice di base di Bitcoin, i componenti che costituiscono una rete funzionante sono molto simili.

Il software Element nel nodo si chiama `elementsd` e viene eseguito come daemon (demone) sul computer dell'utente. Un daemon (o servizio, in Windows) è un programma che viene eseguito come servizio in background senza richiedere il controllo diretto di un utente connesso.

Nota: in questo documento ci riferiremo sempre a elementsd come versione del daemon, ma tutto può essere fatto con elements-qt, a condizione che l'opzione server sia abilitata.

Il daemon di Elements si connette agli altri nodi della rete per scambiare i dati delle transazioni e dei blocchi, convalidando ed estendendo la propria copia locale della blockchain della rete.

Il software Elements comprende anche un programma client chiamato `elements-cli` che consente di inviare comandi [RPC - Remote Procedure Call](https://planb.academy/resources/glossary/rpc-remote-procedure-call) a elementsd dalla riga di comando. Ciò può essere usato, ad esempio, per interrogare il wallet e vederne il saldo, per visualizzare i dati delle transazioni o dei blocchi o per trasmettere una transazione. Questa configurazione dovrebbe essere familiare a chiunque abbia usato gli equivalenti in Bitcoin: bitcoind e bitcoin-cli.

Poiché un nodo Elements può essere configurato passando i parametri all'avvio o tramite un file di configurazione, è possibile avere più di un'istanza in esecuzione sulla stessa macchina. Ciò è utile per scopi di test e sviluppo, in quanto è possibile configurare la propria rete locale su una singola macchina, con ciascun nodo Elements che dispone della propria copia dei dati della blockchain, gestisce la propria pool di transazioni valide non confermate e ascolta le richieste RPC su porte diverse.

### L'archivio e la community del codice Elements

Elements è un progetto open-source e il suo codice sorgente lo puoi trovare nel repository GitHub di Elements, all'indirizzo https://github.com/ElementsProject/elements. Il repository contiene i sorgenti dei programmi elementsd ed elements-cli, oltre agli strumenti di installazione e compilazione di supporto, una suite di test e una vasta documentazione didattica.

A complemento del repository del codice, c'è anche il sito web https://elementsproject.org, una risorsa incentrata sulla community che contiene spiegazioni su cos'è Elements, come funziona, oltre a una sezione di tutorial completa. Il tutorial si concentra sull'apprendimento di Elements seguendo esempi da riga di comando, e mostra come costruire semplici applicazioni desktop e web su di esso. Il sito elenca anche i forum di discussione della community di Elements ed è ospitato su GitHub, consentendo alla community stessa di contribuire ai contenuti del sito.

Per eseguire Elements sul proprio computer è necessario innanzitutto clonare (scaricare una copia) il codice sorgente, installare tutte le dipendenze presenti nel codice e infine creare gli eseguibili del daemon e del client. Il software Elements è quindi pronto per essere configurato ed eseguito.

## Configurazione dei nodi e della rete

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Le impostazioni di configurazione possono essere passate a un nodo Elements all'avvio per modificare il modo in cui funziona, convalida i dati, si connette ad altri nodi e inizializza i suoi dati blockchain.

Le impostazioni vengono caricate dal file `elements.conf` designato o passate come parametri tramite la riga di comando.

Alcuni elementi possono essere modificati utilizzando questi parametri:

- Il nome dell'asset predefinito utilizzato nelle implementazioni di blockchain standalone.
- Il numero di asset inizialmente creati.
- L'asset da utilizzare per il pagamento delle commissioni di transazione sulla rete.
- La posizione di archiviazione di file con i dati della blockchain.
- Le credenziali RPC utilizzate per connettersi a un nodo Bitcoin.
- La soglia `n di m` da rispettare e le chiavi pubbliche valide che possono firmare i blocchi.
- Lo script che deve essere soddisfatto per trasferire gli asset all'interno e all'esterno di una sidechain.
- Se connettersi o meno a un nodo Bitcoin come sidechain.

Molti di questi parametri fanno parte delle regole di consenso della rete, quindi è importante che siano applicati a tutti i nodi all'avvio. Alcuni possono essere modificati dopo l'inizializzazione di una chain, mentre altri devono essere corretti dopo che sono stati usati per inizializzare una chain.

L'uso dei parametri sarà trattato più avanti nello svolgimento del corso, in relazione a ciascuna sezione.

### Operazioni di base con la riga di comando

Questo corso mostra esempi che utilizzano il programma `elements-cli` per effettuare chiamate RPC a uno o più nodi Elements. Ciò viene fatto dal terminale, e viene usato un `alias` per rendere i comandi più brevi. In base a questa convenzione, quando si vede qualcosa di simile ai seguenti comandi:

```bash
e1-dae
e1-cli getnewaddress
```

I caratteri `e1-dae` e `e1-cli` sono in realtà una scorciatoia tipografica che sfrutta la funzione `alias` del terminale. I caratteri `e1-dae` e `e1-cli` verranno effettivamente sostituiti quando il comando verrà eseguito. Quest'ultimo sarà simile a:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Sopra possiamo vedere tre cose: una chiamata per avviare il daemon di Elements; e una chiamata ai programmi elements-cli che si trovano nella directory `$HOME/elements/src`; e un valore per il parametro `datadir`. Il parametro `datadir` ci permette di dire alle istanze del daemon e del client dove localizzare i loro file di configurazione e, nel caso del daemon, dove memorizzare la sua copia della blockchain. Poiché condividono un file di configurazione, il client sarà in grado di effettuare chiamate RPC al daemon.

Eseguendo nuovamente il comando precedente, ma con un valore diverso di `datadir`, possiamo avviare più di un'istanza di Elements, ognuna con la propria copia separata della blockchain e delle impostazioni di configurazione. Per questa convenzione, nel corso useremo gli alias `e2-dae` e `e2-cli` per riferirci a una directory datadir diversa da quella di e1. Quindi l'esempio precedente per la nostra seconda istanza `e2` sarebbe:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

In questo modo, potremo eseguire ogni sorta di operazione, come l'invio di asset tra nodi, l'emissione di asset e la verifica dell'uso del blinding nelle Confidential Transactions tra nodi diversi della stessa rete.

# Utilizzo di Elements - Caso d'uso pratico

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Confidential Transactions

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::

In questa sezione si spiega come utilizzare la funzione Confidential Transactions di Elements.

Tutti gli indirizzi in Elements sono, per impostazione predefinita, offuscati utilizzando le Confidential Transactions, che mantengono l'importo e il tipo di asset visibili solo ai partecipanti alla transazione (e a coloro che scelgono di rivelare la blinding key), garantendo comunque crittograficamente che non si possano spendere più coin di quelle disponibili.

### Confidential Addresses e Confidential Transactions

Per impostazione predefinita, quando si crea un nuovo indirizzo in Elements con il comando `getnewaddress`, viene creato un "Confidential Address".

Per dimostrare come funzionano le Confidential Transactions, faremo in modo che e2 invii a se stesso dei fondi e poi cerchi di visualizzare la transazione da e1. Questo dimostrerà la natura confidenziale delle transazioni in Elements.

Ogni nuovo indirizzo generato da un nodo Elements è riservato per impostazione predefinita. Possiamo dimostrarlo facendo generare a e2 un nuovo indirizzo.

```
e2-cli getnewaddress
```

Si noti che l'indirizzo inizia con e1, in modo che venga identificato come un "Confidential Address" (un tipo di indirizzo dove le informazioni rimangono confidenziali). Esaminando l'indirizzo in modo più dettagliato con il comando getaddressinfo si ottengono ulteriori dettagli sull'indirizzo.

```
e2-cli getaddressinfo <address>
```

Si può notare che c'è una proprietà `confidential_key` che indica che si tratta di un  "Confidential Address".

La confidential_key è la blinding key pubblica, che viene aggiunta al Confidential Address stesso. Questo è il motivo per cui un Confidential Address è così lungo.

Ha anche un "unconfidential address" associato. Se si desidera utilizzare transazioni regolari, non riservate, all'interno di Elements, gli asset devono essere inviati a questo indirizzo invece che a quello con il prefisso lq1.

Ora possiamo fare in modo che e2 invii dei fondi all'indirizzo che ha generato. In seguito si dimostrerà che e1, non essendo una delle parti coinvolte nella transazione, non sarà in grado di visualizzare i dettagli della transazione.

```
e2-cli sendtoaddress <address>
```

Annota l'ID della transazione. Conferma la transazione.

```
e2-cli -generate 101
```

Osservando la transazione in cui e2 ha inviato alcuni fondi a se stesso dal punto di vista di e2 stesso.

```
e2-cli gettransaction <txid>
```

Scorrendo i dettagli della transazione, si può notare che e2 è in grado di visualizzare gli importi inviati e ricevuti, e l'asset transato. Si possono anche vedere le proprietà `amountblinder` e `assetblinder`, utilizzate per nascondere i dettagli ad altri nodi non coinvolti nella transazione.

Per controllare i dettagli della stessa transazione da e1, dobbiamo prima ottenere i dettagli della transazione in formato raw (grezzo).

```
e1-cli getrawtransaction <txid>
```

Questo restituisce i dettagli della transazione. Se si guarda alla sezione vout, si può notare che ci sono tre istanze. Le prime due istanze sono gli importi di ricezione e di modifica, mentre la terza sono le fee della transazione. Di questi tre importi, quello delle fee è l'unico in cui è possibile vedere un valore, poiché le fee sono sempre mostrate all'interno di Elements.

### Blinding Keys

Le prime due sezioni di vout mostrano dei "blinded ranges" (intervalli nascosti) di valori e di commitment data, i quali fungono da prova dell'importo effettivo e del tipo di asset transato.

Anche se importassimo la chiave privata di e2 nel wallet di e1, quest'ultimo non sarebbe comunque in grado di vedere gli importi e il tipo di asset transato, perché non è ancora a conoscenza della blinding key utilizzata da e2. Tutto questo lo dimostriamo importando la chiave privata utilizzata dal wallet di e2 in quello di e1. Per prima cosa dobbiamo esportare la chiave da e2.

```
e2-cli dumpprivkey <address>
```

Quindi lo importiamo in e1.

```
e1-cli importprivkey <privkey>
```

Ora possiamo dimostrare che e1 non può ancora vedere i valori.

```
e1-cli gettransaction <txid>
```

In effetti, mostra 0 come quantità di tx, mentre in realtà era 1.

Per poter vedere il valore effettivo, non offuscato, abbiamo bisogno della blinding key. Per farlo, esportiamo prima la blinding key da e2.

```
e2-cli dumpblindingkey <address>
```

Quindi importarlo in `e1`.

```
e1-cli importblindingkey <address> <blinding key>
```

Ora, quando otteniamo i dettagli della transazione da e1.

```
e1-cli gettransaction <txid>
```

Si vede che, con l'importazione della blinding key, è possibile visualizzare il valore effettivo di 1 all'interno della transazione.

In questa sezione abbiamo visto che l'uso di una blinding key nasconde l'importo e il tipo di asset di una transazione, e che, importando la giusta blinding key, è possibile rivelare tali valori. Nell'uso pratico, una blinding key può essere fornita, ad esempio, a un contabile, nel caso in cui sia necessario verificare l'importo e il tipo di asset detenuto da una delle parti. La funzione Confidential Transactions di Elements consente anche di eseguire delle "range proofs", ovvero delle operazioni che possono dimostrare che l'ammontare di un'asset si trova all'interno di un determinato intervallo, senza la necessità di esporre l'importo effettivo.

Abbiamo anche visto che le Confidential Transactions sono facoltative, ma vengono attivate di default quando viene generato un nuovo indirizzo.

Per questa lezione è tutto, in bocca al lupo per il quiz e arrivederci alla prossima!

## Issued Assets

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::

In questa sezione verrà insegnato come utilizzare la funzione "Issued Assets" di Elements.

Gli Issued Assets consentono di emettere e scambiare diversi tipi di asset tra i partecipanti alla rete Elements. Ogni nodo della rete può emettere i propri asset. Le emissioni possono rappresentare la proprietà fungibile di qualsiasi asset, compresi voucher, coupon, valute, depositi, obbligazioni, azioni, ecc. Gli asset emessi aprono la strada a scambi "trustless" (non basati sulla fiducia in terze parti), options e altri smart contract avanzati che coinvolgono asset auto-generati.

Un "Issued Asset" beneficia anche di Confidential Transactions e può essere riemesso da chiunque detenga il token associato.

Il primo passo è l'accesso a due nodi Elements, che chiameremo e1 ed e2. I nodi hanno resettato la blockchain, e l'asset iniziale è stato diviso tra loro.

I due nodi si trovano sulla stessa rete locale e sono collegati tra loro, quindi condividono sia le stesse transazioni nella loro _mempool_, sia blockchain identiche. Sebbene siano in esecuzione sulla stessa macchina, vale la pena notare che non condividono gli stessi file blockchain. Ogni nodo gestisce la propria copia locale della blockchain, che contiene la stessa cronologia delle transazioni, perché sono in consenso e rispettano le stesse regole del protocollo.

Iniziamo controllando cosa vede ciascun nodo riguardo alle emissioni di asset esistenti nella rete.

Per farlo, si utilizza il comando `listissuances`.

```
e1-cli listissuances

e2-cli listissuances
```

Come si può vedere, entrambi i nodi mostrano la stessa cronologia di emissione. Entrambi mostrano un asset, l'emissione iniziale di 21 milioni di Bitcoin creati all'inizializzazione della chain. È possibile vedere l'hex id dell'asset nei risultati dell'esecuzione del comando precedente e anche l'etichetta assegnata all'asset, che è 'bitcoin'.

Vale la pena notare che all'asset predefinito viene sempre assegnata un'etichetta quando la chain viene inizializzata. Quando si rilasciano i propri asset, è possibile impostare le relative etichette, cosa che faremo a breve. Prima di poterlo fare, dobbiamo emettere i nostri asset.

Chiederemo a e1 di emettere nuovi asset, utilizzando il comando `issueasset`.

```
e1-cli issueasset 100 1 false
```

`issueasset` accetta 3 parametri.

- L'ammontare del nuovo asset da emettere (noi abbiamo usato 100).
- La quantità di token da creare (i token sono utilizzati per riemettere delle quantità di un asset), e noi abbiamo scelto 1.
- Il parametro finale indica a Elements di emettere l'asset come "blinded" (offuscato) o "unblinded" (non offuscato). Utilizzeremo un asset unblinded perché vogliamo visualizzare gli importi dell'emissione da e2, quindi inseriremo `false`.

L'esecuzione del comando restituisce i dati relativi all'emissione. Questi includono l'ID della transazione, di cui si può fare una copia per un uso successivo, il valore hex unico dell'asset e il valore hex unico del token dell'asset.

Generiamo un blocco per confermare la transazione di emissione.

```
e1-cli -generate 1
```

Eseguiamo nuovamente il comando `listissuances` su e1.

```
e1-cli listissuances
```

Questo ci mostra che e1 è ora a conoscenza di due emissioni: l'emissione iniziale di bitcoin e i nostri nuovi asset emessi, di cui possiamo vedere 100 elementi. Si noti a quanto ammonta il valore hex del nuovo asset, e che non c'è un'etichetta associata all'asset, come per l'emissione iniziale di bitcoin.

Controllate di nuovo l'elenco delle emissioni note di e2.

```
e2-cli listissuances
```

Ciò dimostra che e2 non è a conoscenza dell'emissione di asset effettuata da e1. Può solo vedere l'emissione iniziale di bitcoin (che già poteva vedere).

Ciò perché e2 non conosce, e non sta guardando, l'indirizzo a cui sono stati inviati i nuovi asset quando sono stati emessi da e1.

Vale la pena notare che, anche se e2 non può vedere l'emissione stessa, e1 potrebbe comunque inviare a e2 una parte dell'asset. Il nuovo asset verrebbe quindi visualizzato come saldo disponibile nel wallet di e2, anche se quest'ultimo non è a conoscenza dell'emissione originale.

Per consentire a e2 di vedere l'emissione effettiva (e quindi l'importo emesso), dobbiamo aggiungere l'indirizzo a e2 come watched address.

Per farlo, dobbiamo scoprire l'indirizzo a cui è stato inviato l'asset. A tale scopo, utilizzeremo l'_id della transazione_ copiato in precedenza, e chiederemo a e1 di recuperare i dettagli della transazione, in modo da individuare l'indirizzo corretto da aggiungere all'elenco dei wallet di e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Scorrendo verso l'alto, oltre l'hex dei dati della transazione, si vedrà l'indirizzo che ha ricevuto 100 dei nostri nuovi asset, identificato dal suo valore hex.

Prendi l'indirizzo e copialo per poterlo importare in e2.

Ora importiamo l'indirizzo in e2. Per farlo, si usa il comando `importaddress`.

```
e2-cli importaddress <the-issued-to-address>
```

Ora controlliamo l'elenco delle emissioni di e2.

```
e2-cli listissuances
```

Si può notare che l'asset appena emesso è ora incluso nell'elenco. Il nodo e2 è anche in grado di determinare l'importo dell'asset emesso, insieme all'importo del token associato, poiché l'emissione non è stata "blinded". Per abilitare l'uso dell'ID dell'asset alla mappatura dei nomi all'interno di Elements, occorre innanzitutto arrestare Elements.

```
e1-cli stop
```

Poi lo si riavvia con un parametro aggiuntivo che mappa l'hex dell'asset con l'etichetta fornita. Questo permette al nodo di visualizzare i dati sull'asset in un formato più leggibile. Se preferisci, puoi aggiungere questo parametro alla fine di `elements.conf`, in modo da non dover aggiungere l'argomento al daemon ogni volta che lo si avvia. Per esempio:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Ma in questo caso utilizzeremo il metodo degli argomenti.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Interroga nuovamente il nodo per ottenere un elenco di emissioni.

```
e1-cli listissuances
```

Ciò dimostra che la mappatura del valore esadecimale dell'asset con la sua etichetta funziona. Controlliamo di nuovo l'elenco delle emissioni del nodo e2.

```
e2-cli listissuances
```

Si può notare che il nodo e2 non ha accesso a questa etichetta, perché le etichette sono disponibili solo per il nodo che le ha impostate. In effetti, è possibile assegnare un'etichetta diversa allo stesso esadecimale dell'asset su e2 rispetto a quella assegnata su e1. Per prima cosa fermiamo il nodo e2.

```
e2-cli stop
```

Riavviamo con un'etichetta diversa assegnata all'hex della nostra nuovo asset.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Elenchiamo le emissioni da e2.

```
e2-cli listissuances
```

Le etichette degli asset sono native rispetto a ciascun nodo, solo l'hex dell'asset viene riconosciuto dagli altri nodi della rete.

La mappatura dell'etichette con l'hex dell'asset è utile quando si eseguono azioni come le transazioni e le interrogazioni sul saldo del wallet, in quanto consente di fare riferimento a un asset in modo abbreviato. Ad esempio, se volessimo inviare una parte del nostro nuovo asset (una quantità di 10) da e1 a e2 senza usare l'etichetta.

Per prima cosa dobbiamo ottenere un indirizzo a cui inviare l'asset.

```
e2-cli getnewaddress
```

Quindi utilizzamo il comando sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Confermiamo la transazione generando un blocco.

```
generate 1
```

Verifichiamo la ricezione dell'asset su e2.

```
e2-cli getwalletinfo
```

Possiamo vedere che l'asset è stato effettivamente ricevuto.

Si noti che e2 mappa l'hex dell'asset ricevuto e lo visualizza utilizzando la propria etichetta. Un modo più semplice per fare la stessa cosa sarebbe quello di utilizzare l'etichetta della risorsa di e1 durante l'invio.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Dietro le quinte, Elements mappa le etichette native in valori hex per semplificare l'uso degli asset emessi.

In questa sezione abbiamo visto come emettere ed etichettare gli asset. Nella prossima sezione vedremo come riemettere e distruggere delle quantità di un'asset emesso.

## Riemissione di Asset

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::

In questa sezione imparerai come emettere una quantità superiore di un'asset già emesso, e come distruggerne una determinata quantità.

Riemettere un'asset (crearne di più) o distruggerne una quantità può essere necessario quando l'asset rappresenta qualcosa che non ha una fornitura fissa. Ciò potrebbe valere, ad esempio, per gli asset che rappresentano l'oro custodito in un caveau; man mano che le unità d'oro entrano ed escono dal caveau, l'asset che rappresenta la quantità totale nel caveau deve essere regolato di conseguenza.

La riemissione dell'importo di un'asset richiede la proprietà del token associato, che è stato creato insieme all'asset quando è stato inizialmente emesso.

Quando si creano altri asset, non importa quale nodo lo abbia emesso in primo luogo, purché il nodo che sta riemettendo una quantità di asset sia in possesso di ciò che viene chiamato "asset's reissuance token" (token di riemissione dell'asset). Vedremo a breve come creare inizialmente l'asset's reissuance token, come usarlo per riemettere una quantità di asset, e come trasferire l'asset's reissuance token ad altri nodi, in modo che anch'essi abbiano il permesso di riemettere l'asset.

Per cui, avremo bisogno di accedere a due nodi Elements, che chiameremo e1 ed e2. I nodi sono stati resettati e l'asset predefinito è stato diviso tra loro.

Faremo in modo che e1 emetta una quantità pari a 100 nuovi asset e crei 1 token di riemissione per uno stesso asset. Per semplificare l'esempio, l'emissione sarà non-blinded. Procediamo quindi con l'emissione dell'asset e del relativo token di riemissione.

```
e1-cli issueasset 100 1 false
```

Si noti l'ID dell'asset e anche quello del token (di riemissione).

Poiché in seguito emetteremo altri asset da e2, dovremo prendere nota dell'ID della transazione in cui è stato emesso l'asset e utilizzarlo per importare l'indirizzo a cui è stato inviato l'asset.

Confermiamo la transazione.

```
e1-cli -generate 1
```

Ora controlleremo i dettagli della transazione utilizzando il comando `gettransaction`:

```
e1-cli gettransaction <txid>
```

Scorrendo l'hex dei dati della transazione, si vedrà che e1 ha ricevuto 1 token di riemissione e 100 unità dell'asset associato.

Fai una copia dell'indirizzo per poterlo importare in e2.

E ora importa l'indirizzo nel wallet di e2.

```
e2-cli importaddress <address>
```

Ora possiamo vedere che sia e1 che e2 sono a conoscenza dell'emissione dell'asset.

```
e1-cli listissuances

e2-cli listissuances
```

Attualmente e1 detiene una quantità di asset e 1 token di riemissione, mentre e2 non ne possiede.

```
e1-cli getwalletinfo
```

Si noti inoltre che e1 possiede una quantità minore di asset predefinita rispetto a prima, perché ha pagato un piccolo importo per coprire le fee di transazione. Questo importo deve essere riscosso da e1 quando sul blocco creato vengono minati oltre 100 blocchi in più.

```
e2-cli getwalletinfo
```

Poiché e1 detiene il token di riemissione, può riemetterne altri. Ciò avviene utilizzando il comando 'reissueasset'. Facciamo in modo che e1 riemetta altri 100 asset.

```
e1-cli reissueasset <asset-id> 100
```

La verifica della riemissione ha funzionato.

```
e1-cli getwalletinfo
```

Si può notare che e1 ora detiene 200 unità dell'asset, come previsto.

Poiché e2 non detiene una quantità di token di riemissione, riceveremo un errore se proviamo a riemettere l'asset.

```
e2-cli reissueasset <asset-id> 100
```

Leggi il messaggio di errore.

È possibile visualizzare i dettagli della riemissione da e1 utilizzando il comando `listissuances`.

```
e1-cli listissuances
```

Si noti il flag `is_reissuance`.

Se ora inviamo a e2 una quantità di token di riemissione, saremo in grado di riemettere da soli una quantità di asset. Per prima cosa abbiamo bisogno di un indirizzo a cui inviarli. Vale la pena notare che il token di riemissione viene trattato come qualsiasi altro asset all'interno di Elements quando si inviano e si visualizzano i saldi, e che può anche essere suddiviso in pezzi più piccoli come qualsiasi altro asset: quindi non è necessario inviare 1 token di riemissione a e2 perché possa riemettere l'asset. Qualsiasi pezzo sarà sufficiente. Genera un indirizzo per e2 al fine di ricevere il token di riemissione.

```
e2-cli getnewaddress
```

Quindi inviamo una frazione del RIT (reissuance token) da e1 a e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confermiamo la transazione.

```
e1-cli -generate 1
```

Ora possiamo vedere che e2 detiene lo 0,1 che gli è stato inviato.

```
e2-cli getwalletinfo
```

Ciò significa che e2 può ora riemettere una quantità maggiore dell'asset associato al RIT che detiene nel suo wallet. Faremo in modo che e2 riemetta 500 unità dell'asset.

```
e2-cli reissueasset <asset-id> 500
```

Controlla il risultato della riemissione.

```
e2-cli getwalletinfo
```

Si può notare che e2 ora detiene l'importo riemesso nel suo wallet e che il RIT stesso non viene consumato nel processo di riemissione degli asset.

Distruggere una quantità di un'asset è qualcosa che può fare chiunque detenga almeno la quantità che viene distrutta: questa azione non è gestita dal token di riemissione.

```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```

In questa sezione abbiamo visto come emettere un asset e come utilizzare il token di riemissione che viene creato opzionalmente come parte dell'emissione dell'asset. Abbiamo anche visto che trasferire un token di riemissione è semplice come trasferire qualsiasi altro asset, e che detenere una qualsiasi quantità di token di riemissione conferisce al titolare il diritto di emettere altri asset. È quindi molto importante controllare chi ha accesso ai token di riemissione nella vostra rete. Abbiamo anche visto come si fa a distruggere una quantità di un asset, e che questo processo non è soggetto al possesso del token di riemissione.

# Element Federation

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Block Signing

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::

Elements supporta un modello di [firma federata](https://planb.academy/resources/glossary/blocksigners) che consente di specificare il numero di membri della _"Strong Federation"_ che devono firmare un blocco proposto per validarlo.

In precedenza, e per facilità di esempio, abbiamo creato i blocchi utilizzando il comando `generate`, che non ha dovuto soddisfare un requisito di firma multipla affinché i blocchi creati fossero accettati dalla rete come validi.

Impostiamo i nostri nodi in modo che richiedano la creazione di blocchi multisig 2-of-2. Ciò avverrà usando il parametro `signblockscript`, che può essere aggiunto al file di configurazione o passato al nodo all'avvio. Per inizializzare una chain con questo parametro, dobbiamo prima costruire lo script che la compone.

Lo faremo usando alcuni nodi esistenti, di cui salveremo i dati emessi, e poi cancelleremo la chain in modo da poterla riavviare usando il nostro parametro `signblockscript`. Ciò è necessario perché lo script fa parte delle regole di consenso della rete e deve essere impostato all'inizializzazione della chain. Non può essere aggiunto in un secondo momento a una chain già esistente.

Avremo bisogno di accedere a due nodi Elements, che chiameremo e1 ed e2. I nodi sono stati resettati e l'asset predefinito è stato diviso tra loro.

Assicurati che il parametro `con_max_block_sig_size` sia impostato a un valore elevato nel file `elements.conf`, altrimenti la firma dei blocchi fallirà più avanti in questa sezione. Per questa esercitazione, abbiamo impostato con_max_block_sig_size=2000.

Poiché resetteremo la blockchain e cancelleremo i wallet associati a e1 ed e2, dovremo fare una copia degli indirizzi, delle chiavi pubbliche e delle chiavi private utilizzate per generare lo script di firma dei blocchi, in modo da poterli utilizzare in seguito.

Per prima cosa, è necessario che ciascun nodo firmatario dei blocchi generi un nuovo indirizzo, di cui è necessario fare una copia.

```
e1-cli getnewaddress

e2-cli getnewaddress
```

Poi dobbiamo estrarre le chiavi pubbliche dagli indirizzi e annotarle per un uso successivo.

```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```

Quindi estraiamo le chiavi private, che reimporteremo in seguito in modo che i nodi possano firmare i blocchi dopo aver reinizializzato la blockchain e i dati del wallet.

```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```

Ora dobbiamo generare uno [_script redeem_](https://planb.academy/resources/glossary/redeemscript) con i requisiti di multi-firma 2 su 2. Per farlo, utilizziamo il comando `createmultisig`, passando il primo parametro a 2 e fornendo due chiavi pubbliche. Sono queste chiavi, la cui proprietà deve essere dimostrata in seguito, quando il blocco viene creato.

Entrambi i nodi, e1 o e2, possono generare il multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

In questo modo si ottiene il nostro script reedem, che può essere copiato per essere utilizzato in seguito.

Ora dobbiamo cancellare i dati della blockchain e del wallet esistenti per poter ricominciare con il nuovo `signblockscript` come parte delle regole di consenso della chain. Per questo motivo, è stato necessario fare una copia di alcuni dati, come le chiavi private che verranno utilizzate nella nuova chain per firmare i blocchi, tutto ciò è stato necessario prepararlo prima di procedere.

Con i dati del wallet e della chain cancellati, possiamo ora avviare i nostri nodi e far loro inizializzare una nuova chain usando il parametro `signblockscript`. Inseriamo -evbparams=dynafed:0::: per disabilitare l'attivazione di dynafed, perché in questo esempio non abbiamo bisogno di questa funzione avanzata.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Ora dobbiamo importare le chiavi private che abbiamo salvato in precedenza, in modo che i nostri nodi possano firmare e contribuire a completare i blocchi proposti.

```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```

L'uso del comando `generate` dovrebbe ora dare un errore, poiché non soddisfa le regole di firma dei blocchi ora applicate dai nostri nodi.

```
e1-cli -generate 1
```

Per proporre un nuovo blocco, un nodo può usare il comando `getnewblockhex`, il quale restituisce l'hex di un nuovo blocco che dovrà essere firmato prima di essere accettato da tutti i nodi della rete.

```
e1-cli getnewblockhex
```

Ricorda che il comando crea solo un blocco da proporre, ma non ne genera uno.

A conferma di ciò, possiamo vedere che attualmente non ci sono blocchi nella nostra blockchain.

```
e1-cli getblockcount
```

Se proviamo a inviare il blocco hex senza prima firmarlo.

```
e1-cli submitblock <block-hex>
```

Riceviamo un messaggio che ci informa che la prova di blocco non è valida. Questo perché non è ancora stata firmata da entrambe le parti richieste.

Facciamo in modo che e1 firmi il blocco proposto.

```
e1-cli signblock <block-hex>
```

Chiedere a e2 di firmare l'hex.

```
e2-cli signblock <block-hex>
```

Si noti che e2 non firma l'output creato da e1, il quale firma il blocco proposto. Entrambi firmano l'hex del blocco proposto indipendentemente dai risultati dell'altro.

Ora dobbiamo combinare le firme dei blocchi e1 ed e2. Entrambi i nodi possono farlo, tutto ciò di cui hanno bisogno è l'hex del blocco firmato dall'altro nodo.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Si può notare che il comando `combineblocksigs` fornisce l'hex del blocco firmato e lo stato di `complete`, che indica che l'hex del blocco è pronto per essere inviato.

Ora entrambi i nodi possono inviare il blocco hex completato. Lo faremo fare a e1.

```
e1-cli submitblock <combined-signed-hex>
```

Verifichiamo la validità dell'invio.

```
e1-cli getblockcount

e2-cli getblockcount
```

Si può notare che sia e1 che e2 hanno accettato il blocco come valido e lo hanno aggiunto alla fine delle loro copie locali della blockchain.

Per riassumere il processo. In questa sezione abbiamo:

- Proposto un nuovo blocco.
- Ottenuto la firma del blocco da ciascun nodo.
- Unito le firme.
- Verificato che le firme fossero valide e che soddisfassero la soglia di riscrittura della chain.
- Presentato il blocco.

Ogni nodo della rete convalida il blocco e lo aggiunge alla propria copia locale della blockchain.

### Block Signing

Sebbene il processo appaia inizialmente complesso, la sequenza di firma dei blocchi in Elements è sempre la stessa, e la configurazione iniziale deve essere eseguita una sola volta:

1. Impostazione iniziale (eseguita una volta)

2. Creazione di un indirizzo multi-firma chiamato `signblockscript` utilizzando le chiavi pubbliche dei Block Signers della Federazione.

3. Uso del reedem script che viene utilizzato per avviare una nuova blockchain.

5. Produzione dei blocchi (in corso)

6. Generazione dei blocchi proposti, che vengono scambiati per la firma.

Una volta che un numero di firmatari che rappresenta la soglia ha firmato il blocco proposto, quest'ultimo viene combinato e sottoposto alla rete. Se soddisfa i criteri del `signblockscript` della chain, i nodi lo accettano come blocco valido.

## Elements come sidechain 

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::

Elements è una piattaforma blockchain open-source di uso generico che può anche essere `pegged` (ancorata) a una blockchain esistente, come Bitcoin. Quando è collegata a un'altra blockchain, si dice che Elements opera come una `sidechain`. Le [sidechain](https://planb.academy/resources/glossary/sidechain) consentono il trasferimento bidirezionale di asset da una chain all'altra. L'implementazione di Elements come sidechain consente di aggirare alcune delle limitazioni intrinseche della mainchain, pur mantenendo un buon grado di sicurezza fornito dagli asset protetti sulla mainchain.

Mentre una sidechain conosce la mainchain e la sua cronologia delle transazioni, la mainchain non è a conoscenza dell'esistenza della sidechain, che non è necessaria per il suo funzionamento. Ciò consente alle sidechain di innovare senza restrizioni o ritardi associati alle proposte di miglioramento del protocollo della mainchain. Piuttosto che cercare di modificare il protocollo principale direttamente, lo si estende, consentendo alla chain principale di rimanere sicura e specializzata, sostenendo il buon funzionamento della sidechain.

Estendendo le funzionalità di Bitcoin e sfruttando la sua sicurezza sottostante, una sidechain basata su Elements è in grado di fornire nuove funzionalità che in precedenza non erano disponibili per gli utenti della mainchain. Un esempio di sidechain basata su Elements in produzione è Liquid Network.

Per inizializzare una blockchain Elements come sidechain, è necessario utilizzare il parametro di script federated peg. Questo parametro può essere impostato nel file di configurazione di un nodo o utilizzato all'avvio.

Lo script federated peg definisce quali membri della Federazione possono svolgere funzioni di peg-in e peg-out. Questi funzionari sono chiamati `Watchmen`, in quanto controllano la mainchain e la sidechain alla ricerca di transazioni peg-in e peg-out valide e le eseguono (se lo sono). `Peg-out` significa spostare gli asset pegged dalla sidechain alla mainchain e `peg-in` significa spostare gli asset pegged dalla mainchain alla sidechain. 

Quando diciamo `move into the sidechain` (spostare nella sidechain), in realtà intendiamo dire che i fondi vengono bloccati in un indirizzo multi-firma sulla mainchain e una quantità corrispondente dell'asset viene creata sulla sidechain Elements. Quando si dice `move out of the sidechain` (uscire dalla sidechain), si intende che gli asset vengono distrutti sulla sidechain di Elements e l'importo corrispondente viene liberato dai fondi bloccati sulla mainchain. Il permesso di eseguire le funzioni di peg-in e peg-out richiede che i funzionari dimostrino la proprietà delle chiavi pubbliche utilizzate nello script federated peg. Ciò avviene con l'uso delle chiavi private corrispondenti.

Per creare uno script federated peg, quindi, è necessario che ogni nodo generi una chiave pubblica. Dobbiamo anche memorizzare le chiavi private associate per un uso successivo, poiché dovremo cancellare tutti i dati della chain esistente e inizializzare una nuova chain usando lo script federated peg. Questo perché lo script federated peg fa parte delle regole di consenso di una sidechain e non può essere applicato a una blockchain esistente, non ancorata, in un secondo momento.

Generiamo quindi un indirizzo per ciascuno dei nostri nodi, memorizziamo i dati rilevanti per un uso successivo e generiamo lo script federated peg che useremo per inizializzare la nostra sidechain in seguito.

Per prima cosa è necessario che ciascuno dei nostri nodi, che fungeranno da Watchmen della nostra rete, generino un nuovo indirizzo.

```
e1-cli getnewaddress

e2-cli getnewaddress
```

Quindi convalidiamo l'indirizzo per ottenere le chiavi pubbliche.

```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```

E poi recuperiamo le chiavi private associate a ciascun indirizzo.

```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```

Memorizziamo le chiavi private e pubbliche per un uso successivo.

Ora dobbiamo cancellare i dati della blockchain e dei wallet esistenti, poiché inizializzeremo una nuova chain utilizzando uno script federated peg. Puoi farlo ora. Non dimenticare di avviare il daemon di Bitcoin, che ci servirà per il peg-in.

Ora possiamo inizializzare una nuova chain con uno script federated peg creato utilizzando le chiavi pubbliche che abbiamo memorizzato in precedenza. I numeri che inseriamo e che circoscrivono le nostre chiavi pubbliche definiscono e delimitano il numero di chiavi utilizzate e la proprietà delle chiavi, che deve essere dimostrata per effettuare il peg-in e il peg-out della nostra sidechain.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Ora importeremo le chiavi private che abbiamo salvato in precedenza, in modo che i nostri nodi possano successivamente firmare e completare il trasferimento delle risorse tra le chain e soddisfare i requisiti dello script federated peg.

```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```

Ora dobbiamo aspettare la generazione di alcuni blocchi su entrambe le chain: si tratta di un requisito del processo di ancoraggio, in quanto protegge dalle riorganizzazioni dei blocchi sulla mainchain, che portano a un'inflazione dell'offerta di asset ancorati all'interno della sidechain.

Per mantenere questa sezione focalizzata sul federated peg, genereremo i blocchi senza usare il modello di firma dei blocchi visto nell'ultima sezione, e torneremo invece a usare il comando `generate` per creare nuovi blocchi.

```
b-cli generate 101

e1-cli generate 1
```

Non abbiamo necessariamente bisogno di generare blocchi per Elements. Ma generiamone comunque uno: è una buona pratica per evitare potenziali incoerenze.

Ora la nostra chain è pronta per il peg-in. Per effettuare il peg-in è necessario generare un tipo speciale di indirizzo utilizzando il comando `getpeginaddress`. Si noti che il tempo che intercorre tra la generazione di un indirizzo peg-in con getpeginaddress e la sua rivendicazione con `claimpegin` deve essere ridotto al minimo. Gli indirizzi peg-in non durano a lungo termine e non devono essere riutilizzati.

```
e1-cli getpeginaddress
```

Si può notare che il comando crea un nuovo indirizzo mainchain e un nuovo script che dovrà essere soddisfatto per richiedere i fondi peg-in. L'indirizzo della mainchain è un indirizzo `pay to script hash` che sarà utilizzato dai "Functionaries" (Funzionari) che svolgono il ruolo di "Watchmen" all'interno di Elements Network.

Come `getnewaddress`, `getpeginaddress` aggiunge un nuovo segreto al wallet del nodo chiamante, quindi è importante tenere conto del backup del file del wallet nel processo di gestione del nodo.

Ora invieremo alcuni bitcoin dalla mainchain alla sidechain. Il nostro wallet di test, che ci servirà per tornare sulla mainchain, contiene già alcuni fondi.

```
b-cli getwalletinfo
```

Possiamo vedere che il wallet contiene 50 bitcoin. Invieremo un bitcoin dalla mainchain alla sidechain. Dobbiamo inviare i fondi all'indirizzo della mainchain che il nostro nodo ha generato in precedenza.

```
b-cli sendtoaddress <e1-pegin-address>
```

Dobbiamo conservare l'ID di questa transazione perché ci servirà come prova di finanziamento in seguito.

Ora possiamo vedere che il saldo del wallet della mainchain è diminuito dell'importo che abbiamo inviato, più un ulteriore piccolo importo per coprire le fee di transazione.

```
b-cli getwalletinfo
```

Dobbiamo far maturare nuovamente la transazione.

```
b-cli generate 101
```

Per far sì che il nostro nodo Elements rivendichi i fondi peg-in, dobbiamo ottenere la `prova` che la transazione peg-in è stata effettuata. La prova crittografica utilizza l'ID della transazione di finanziamento per calcolare il _Merkel path_ e dimostra che la transazione è presente in un blocco confermato.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Abbiamo bisogno anche dei dati raw (grezzi) delle transazioni.

```
b-cli getrawtransaction <tx-id>
```

Con la prova e i dati raw della transazione peg-in, il nostro nodo Elements può ora rivendicare il peg-in utilizzando la transazione raw e la prova della transazione stessa.

```
e1-cli claimpegin <raw> <proof>
```

Si noti che c'è un terzo parametro opzionale che avremmo potuto fornire a `claimpegin`. Questo terzo parametro può essere usato per specificare l'indirizzo della sidechain a cui inviare i fondi rivendicati. Nel nostro esempio non è stato necessario, poiché il comando è partito dallo stesso nodo che possiede l'indirizzo a cui sono destinati i fondi rivendicati.

Contriamo il saldo di e1.

```
e1-cli getwalletinfo
```

Generiamo un blocco per confermare la richiesta.

```
e1-cli generate 1
```

Contriamo il saldo di e1.

```
e1-cli getwalletinfo
```

Si può notare che il peg-in è stato rivendicato con successo.

Per il peg-out, il processo è simile. Viene generato un indirizzo, vi si inviano i fondi e questi vengono rilasciati se la transazione è valida. Non tratteremo l'intero processo di peg-out perché comporta un lavoro sulla mainchain che esula dagli scopi di questo corso. I passaggi in termini di eventi Elements sono: un indirizzo viene generato sulla mainchain.

```
b-cli getnewaddress
```

I fondi vengono inviati all'indirizzo della mainchain da un nodo Elements utilizzando il comando `sendtomainchain`.

```
e1-cli sendtomainchain <new-address> 1
```

Generiamo un blocco per confermare la transazione.

```
e1-cli generate 1
```

Controlliamo il saldo del wallet del nodo.

```
e1-cli getwalletinfo
```

Vediamo che il saldo è diminuito.

In questa sezione abbiamo visto come:

- Generare uno script federated peg.
- Inizializzare una nuova chain che utilizza lo script come parametro delle regole di consenso della rete.
- Inviare fondi dalla mainchain alla sidechain.
- Rivendicare i fondi all'interno della sidechain di Elements.
- Capire come si avvia l'invio di fondi alla mainchain.

### FederatedPegScript

Per consentire a Elements di funzionare come sidechain, il blocco genesi nella sua blockchain deve essere creato con un `fedpegscript` attivato. Ciò avviene passando il parametro `fedpegscript` all'avvio del nodo. Lo script farà quindi parte delle regole di consenso della blockchain Elements e consentirà la convalida e l'esecuzione delle richieste di peg-in e peg-out.

Il `fedpegscript` è composto da chiavi pubbliche controllate da coloro che sono autorizzati a eseguire le azioni di peg (ancoraggio). Di seguito viene mostrato un esempio di formato di un fedpegscript a 2 firme su 2:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Nota: i caratteri al di fuori delle chiavi pubbliche sono delimitatori che indicano i requisiti della chiave pubblica e di `n di m`. Ad esempio, il modello per un fedpegscript 1-of-1 sarebbe "5121<chiave pubblica 1>51ae".

### Peg-in

Prima che un peg-in (ancoraggio in ingresso) possa essere accettato da una sidechain di Elements, deve avere sufficienti conferme sulla mainchain. Ciò è necessario per evitare l'inflazione dell'offerta dell'asset peggato sulla sidechain di Elements che potrebbe essere causata da una riorganizzazione della mainchain.

Brevi riorganizzazioni della parte finale della blockchain Bitcoin sono previste come parte del normale funzionamento del meccanismo di consenso Proof-of-Work (PoW). Per questo motivo, Elements accetta che un peg-in sia valido solo quando vengono minati una quantità di blocchi sufficiente all'interno della blockchain Bitcoin. Questo serve a evitare che Elements accetti lo stesso peg-in più di una volta.

### Peg-out (ancoraggio in uscita)

Un peg-out si verifica quando un nodo Elements chiama il comando `sendtomainchain`, che prende in input un indirizzo della mainchain (la destinazione del peg-out) e l'ammontare dell'asset pegged da `prelevare`. In questo modo si crea una transazione di peg-out sulla sidechain. Una volta che i Funzionari (che agiscono come guardiani) rilevano che la transazione di peg-out è stata confermata sulla sidechain, si occupano di rilasciare effettivamente l'asset sulla mainchain alla destinazione di peg-out, come abbiamo imparato nelle sezioni precedenti del corso.

## Elements come Blockchain indipendente

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::

Fin ora abbiamo visto come far funzionare Elements come sidechain. Tuttavia, può anche funzionare come soluzione blockchain autonoma con un proprio asset nativo predefinito. In questa configurazione, una blockchain Elements mantiene tutte le caratteristiche di un'implementazione sidechain, come le Confidential Transactions e gli Issued Assets, ma non ha bisogno di peg-in o peg-out per aggiungere o rimuovere dalla circolazione gli asset predefiniti.

In questa sezione ci occuperemo di:

- Inizializzare una nuova blockchain Elements con un asset predefinito chiamato `newasset`.
- Specificare 1.000.000 di `newasset` da creare insieme a 2 token di riemissione per questi asset.
- Reclamare tutte le coin anyone-can-spend (chiunque può spendere) `newasset`.
- Rivendicare tutti i token di riemissione anyone-can-spend (chiunque può spendere) per `newasset`.
- Inviare la risorsa e il relativo token di riemissione al wallet di un altro nodo.
- Ripubblicare altri `newasset` da entrambi i nodi.

Per inizializzare una rete Elements e farla funzionare come una blockchain indipendente, ogni nodo deve essere avviato con alcuni parametri di base. Vengono utilizzati per indicare al nodo di non cercare di convalidare i peg-in da un'altra blockchain, il nome dell'asset predefinito della rete e la quantità di asset predefinito e di token di riemissione associato da creare.

Avvieremo ora una nuova chain utilizzando questi parametri sui nostri due nodi Elements collegati. Chiameremo l'asset predefinito `newasset` e ne emetteremo un milione, oltre a due token di riemissione `newasset`.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Si noti che gli importi qui utilizzati sono nella quantità più piccola che la rete può accettare, quindi i duecento milioni di token di riemissione equivalgono in realtà a due gettoni interi. Lo stesso vale per le quantità delle "initial free coins".

Controlliamo i saldi attuali del wallet del nostro nodo.

```
e1-cli getwalletinfo

e2-cli getwalletinfo
```

Si può notare che l'inizializzazione ha funzionato correttamente.

Poiché l'emissione iniziale di asset viene creata come `anyone-can-spend` (chiunque può spendere), faremo in modo che e1 li rivendichi tutti, in modo da rimuovere l'accesso di e2 ad essi.

```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Non è necessario specificare `newasset` come asset da inviare, poiché è già l'asset predefinito e quindi anche l'asset predefinito utilizzato per pagare le fee di rete.

All'interno di Elements, è possibile inviare più tipi di asset allo stesso indirizzo, quindi possiamo riutilizzare l'indirizzo appena generato per ricevere l'asset predefinito e usarlo come indirizzo di destinazione per i token di riemissione.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confermiamo le transazioni.

```
e1-cli generate 101
```

Verificheremo che e1 sia l'unico possessore dell'asset e del suo token di riemissione.

```
e1-cli getwalletinfo

e2-cli getwalletinfo
```

E come possiamo vedere che è proprio così.

Ora invieremo una parte del `newasset` a e2, che attualmente ha un saldo pari a zero.

```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Si noti che non è stato necessario specificare il tipo di risorsa da inviare, poiché `newasset` è stato creato come risorsa predefinita della rete

Inviamo anche alcuni dei token di riemissione per `newasset` a e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confermiamo le transazioni.

```
e1-cli generate 101
```

Possiamo verificare che i wallet siano stati aggiornati di conseguenza.

```
e1-cli getwalletinfo

e2-cli getwalletinfo
```

Ora riemetteremo alcune delle risorse predefinite da e1. Si noti che la possibilità di farlo è abilitata dal parametro di avvio `initialreissuancetokens`. Se omesso o impostato a zero, si otterrà una risorsa predefinita che non potrà essere riemessa in un secondo momento.

```
e1-cli reissueasset newasset 100
```

Abbiamo potuto usare l'etichetta di `newasset` invece di dover fornire il valore _hex dell'id_, perché una chain di Elements etichetta sempre il suo asset predefinito.

Verifichiamo che la riemissione dell'asset predefinito abbia funzionato:

```
e1-cli generate 101

e1-cli getwalletinfo
```

Dimostreremo ora che, poiché e2 possiede alcuni token di riemissione di `newasset`, può anche riemettere l'asset predefinito.

```
e2-cli reissueasset newasset 100
```

Verifichiamo il funzionamento della riemissione dell'asset predefinito da parte di e2.

```
e2-cli generate 101

e2-cli getwalletinfo
```

In questa sezione, abbiamo configurato Elements come blockchain indipendente e abbiamo verificato che le funzionalità di base funzionino come ci aspetteremo.

Abbiamo utilizzato i parametri di avvio per:

- Inizializzare una nuova blockchain Elements con un asset predefinito chiamato `newasset`.
- Specificare la quantità di asset predefinito da creare all'inizializzazione della chain.
- Creare alcuni token di riemissione per l'asset predefinito e riemettere altri asset predefiniti da entrambi i nodi.

Sulla nostra rete blockchain Elements indipendente, tutte le altre operazioni transazionali opereranno nello stesso modo degli esempi trattati nelle sezioni principali del corso, ma utilizzeranno `newasset` invece di `bitcoin` come asset predefinito e come fee.

### Parametri di avvio del nodo e di inizializzazione della chain

Per dire a un nodo Elements di operare come una blockchain indipendente è necessario utilizzare alcuni parametri. Vediamo ora ciascuno di essi e scopriamo a cosa servono.

#### `validatepegin=0`

Poiché una blockchain indipendente non ha bisogno di convalidare le transazioni peg-in o peg-out, è necessario disabilitare tali controlli. Con questa impostazione, non è necessario eseguire il software client Bitcoin o memorizzare una copia della blockchain Bitcoin, poiché la rete Elements funzionerà in modo indipendente.

#### `defaultpeggedassetname`

Consente di specificare il nome dell'asset predefinito creato all'inizializzazione della blockchain.

#### `initialfreecoins`

Il numero (nell'equivalente dell'unità satoshi di Bitcoin) dell'asset predefinito da creare.

#### `initialreissuancetokens`

Il numero (nell'equivalente dell'unità satoshi di Bitcoin) dei token di riemissione per l'asset predefinito da creare. Senza questo valore sarebbe impossibile creare altri asset di default. Se non si vuole che sia possibile creare altri asset predefiniti, questo valore può essere impostato a zero o omesso.

Utilizzando questi parametri, la procedura comune per avviare un nodo sarà simile a questa:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Operazioni di base

Il parametro `defaultpeggedassetname` applica un'etichetta all'asset predefinito. Senza questa impostazione, la risorsa predefinita sarà automaticamente chiamata `bitcoin`. Nelle sezioni precedenti, quando abbiamo inviato asset emessi da noi stessi a un altro nodo, abbiamo dovuto specificare l'hex dell'asset o l'etichetta dell'asset applicato nativamente per indicare a Elements quale risorsa stavamo inviando. Poiché `defaultpeggedassetname` si applica a tutti i nodi, non abbiamo bisogno di nominarlo quando lo inviamo, anche se il suo nome non è `bitcoin`. Ogni funzione che prima avrebbe inviato `bitcoin` per impostazione predefinita, ora invierà qualsiasi cosa si sia scelto di etichettare come asset predefinito.

Per questo motivo, l'invio di 10 unità del nuovo asset predefinito a un indirizzo è semplice come:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Se hai fornito al nodo anche un valore di `initialreissuancetokens` maggiore di zero, sarai anche in grado di riemettere altri asset di default, cosa che non è possibile se eseguite Elements come sidechain.

A tal fine, qualsiasi nodo che detenga una quantità di token associata all'asset predefinito deve solo emettere un comando nella forma:

```
e1-cli reissueasset <default asset name> <amount>
```

Utilizzando i parametri di cui sopra è possibile far funzionare Elements come una blockchain autonoma con un proprio asset predefinito, disaccoppiato da Bitcoin e da altre blockchain.

## Conclusione

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::

In questo corso abbiamo imparato che Elements è un protocollo di rete open-source che può essere implementato come [sidechain](https://planb.academy/resources/glossary/sidechain) di un'altra blockchain o come soluzione blockchain autonoma.

Abbiamo visto che il codice sorgente e il sito web di Elements (https://github.com/ElementsProject/elements) sono ospitati su GitHub e che esistono forum di discussione della community, come Build On L2 (https://community.liquid.net/c/developers/) o Liquid Developers Telegram (https://t.me/liquid_devel), che possono essere utilizzati per saperne di più sulla distribuzione e lo sviluppo di applicazioni su Elements e Liquid. Sono state illustrate caratteristiche chiave come le "Confidential Transactions" e gli "Issued Assets", oltre a come i membri di una "Strong Federation" consentono la firma federata dei blocchi e il meccanismo 2-Way Peg (Ancoraggio Bilaterale). 

Il passo successivo è quello di sfidare se stessi con un quiz che copre tutte le sezioni precedenti, per poi iniziare il viaggio sulla rete Elements... buona fortuna!

# Sezione finale

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Recensioni e valutazioni

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusione

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>
<isCourseConclusion>true</isCourseConclusion>
