---
name: Il protocollo RGB, dalla teoria alla pratica
goal: Acquisire le competenze necessarie per comprendere e utilizzare l'RGB
objectives: 

  - Comprendere i concetti fondamentali del protocollo RGB
  - Padroneggiare i principi della convalida lato client e degli impegni Bitcoin
  - Imparare a creare, gestire e trasferire i contratti RGB
  - Come utilizzare un nodo Lightning compatibile con RGB

---
# Scoprire il protocollo RGB

Immergetevi nel mondo di RGB, un protocollo progettato per implementare e far rispettare i diritti digitali, sotto forma di contratti e asset, sulla base delle regole di consenso e delle operazioni della blockchain Bitcoin. Questo corso di formazione completo vi guida attraverso le basi tecniche e pratiche di RGB, dai concetti di "Client-side Validation" e "Single-use Seals", all'implementazione di smart contract avanzati.

Attraverso un programma strutturato e graduale, scoprirete i meccanismi di convalida lato client, gli impegni deterministici su Bitcoin e i modelli di interazione tra gli utenti. Imparerete a creare, gestire e trasferire i token RGB su Bitcoin o sulla rete Lightning.

Se siete sviluppatori, appassionati di Bitcoin o semplicemente curiosi di saperne di più su questa tecnologia, questo corso di formazione vi fornirà gli strumenti e le conoscenze necessarie per padroneggiare RGB e costruire soluzioni innovative su Bitcoin.

Il corso si basa su un seminario dal vivo organizzato da Fulgur'Ventures e tenuto da tre rinomati insegnanti ed esperti di RGB.

+++
# Introduzione

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Presentazione del corso

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Salve a tutti e benvenuti in questo corso di formazione dedicato a RGB, un sistema di smart contract convalidato lato client che gira su Bitcoin e sulla rete Lightning. La struttura di questo corso è pensata per consentire un'esplorazione approfondita di questo argomento complesso. Ecco come è organizzato il corso:

**Sezione 1: Teoria

La prima sezione è dedicata ai concetti teorici necessari per comprendere i fondamenti della convalida lato client e di RGB. Come scoprirete in questo corso, RGB introduce una serie di concetti tecnici che di solito non si vedono in Bitcoin. In questa sezione troverete anche un glossario che fornisce le definizioni di tutti i termini specifici del protocollo RGB.

**Sezione 2: Pratica

La seconda sezione si concentrerà sull'applicazione dei concetti teorici visti nella sezione 1. Impareremo a creare e manipolare i contratti RGB. Vedremo anche come programmare con questi strumenti. Queste prime due sezioni sono presentate da Maxim Orlovsky.

**Sezione 3: Applicazioni

La sezione finale è guidata da altri relatori che presentano applicazioni concrete basate su RGB, per evidenziare casi d'uso reali.

---
Questo corso di formazione è nato da un bootcamp di sviluppo avanzato di due settimane a Viareggio, in Toscana, organizzato da [Fulgur'Ventures](https://fulgur.ventures/). La prima settimana, incentrata su Rust e sugli SDK, si trova in quest'altro corso:

https://planb.network/courses/lnp402
In questo corso ci concentriamo sulla seconda settimana del bootcamp, incentrata su RGB.

**Settimana 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**Settimana 2 - Formazione in corso CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Grazie agli organizzatori di questi corsi dal vivo e ai 3 insegnanti che vi hanno partecipato:


- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotica, transumanesimo. Creatore di RGB, Prime, Radiant e lnp_bp, mycitadel_io e cyphernet_io* ;
- Hunter Trujilo: *Sviluppatore, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Sto facendo la mia parte per trasformare il mondo in una distopia cypherpunk. Attualmente lavoro su RGB presso Bitfinex*.

La versione scritta di questo corso di formazione è stata redatta utilizzando due risorse principali:


- Video del seminario di Maxim Orlovsky, Hunter Trujilo e Frederico Tenga al Lightning Bootcamp ;
- La documentazione RGB, la cui produzione è stata sponsorizzata da [Bitfinex](https://www.bitfinex.com/).

# RGB in teoria

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Introduzione ai concetti di calcolo distribuito

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB è un protocollo progettato per applicare e far rispettare i diritti digitali (sotto forma di contratti e beni) in modo scalabile e riservato, basandosi sulle regole di consenso e sulle operazioni della blockchain Bitcoin. L'obiettivo di questo primo capitolo è quello di presentare i concetti e la terminologia di base del protocollo RGB, evidenziando in particolare i suoi stretti legami con i concetti di base dell'informatica distribuita, come la convalida lato client e i sigilli monouso.

In questo capitolo esploriamo i fondamenti dei **sistemi di consenso distribuito** e vediamo come RGB si inserisce in questa famiglia di tecnologie. Introdurremo anche i principi principali che ci aiutano a capire perché RGB mira a essere estensibile e indipendente dal meccanismo di consenso di Bitcoin, pur affidandosi a esso quando necessario.

### Introduzione

L'informatica distribuita, una branca specifica dell'informatica, studia i protocolli utilizzati per far circolare ed elaborare le informazioni su una rete di nodi. Insieme, questi nodi e le regole del protocollo costituiscono il cosiddetto sistema distribuito. Tra le proprietà essenziali che caratterizzano un sistema di questo tipo ci sono :


- La **capacità di verifica e convalida indipendente** di alcuni dati da parte di ciascun nodo;
- La possibilità per i nodi di costruire (a seconda del protocollo) una visione completa o parziale delle informazioni. Queste viste sono gli **stati** del sistema distribuito;
- L'ordine **cronologico** delle operazioni, in modo che i dati siano registrati in modo affidabile e che ci sia un consenso sulla sequenza degli eventi (sequenza di stati).

In particolare, la nozione di **consenso** in un sistema distribuito copre due aspetti:


- Riconoscimento della validità** dei cambiamenti di stato (secondo le regole del protocollo);
- L'**accordo sull'ordine** di questi cambiamenti di stato, che rende impossibile riscrivere o invertire le operazioni convalidate a posteriori (questo è anche noto in Bitcoin come "double-spend protection").

La prima implementazione funzionale e senza permessi di un meccanismo di consenso distribuito è stata introdotta da Satoshi Nakamoto con Bitcoin, grazie all'uso combinato di una struttura di dati blockchain e di un algoritmo Proof-of-Work (PoW). In questo sistema, la credibilità della storia del blocco dipende dalla potenza di calcolo ad esso dedicata dai nodi (minatori). Bitcoin è quindi un importante e storico esempio di sistema di consenso distribuito aperto a tutti (*permissionless*).

Nel mondo della blockchain e dell'informatica distribuita, possiamo distinguere due paradigmi fondamentali: ***blockchain*** in senso tradizionale e ***canali di stato***, il cui miglior esempio in produzione è Lightning Network. La blockchain è definita come un registro di eventi ordinati cronologicamente, replicati per consenso all'interno di una rete aperta e senza permessi. I canali di stato, invece, sono canali peer-to-peer che consentono a due (o più) partecipanti di mantenere uno stato aggiornato fuori dalla catena, utilizzando la blockchain solo al momento dell'apertura e della chiusura di questi canali.

Nel contesto di Bitcoin, conoscete senza dubbio i principi di mining, decentralizzazione e finalità delle transazioni sulla blockchain, nonché il funzionamento dei canali di pagamento. Con RGB, stiamo introducendo un nuovo paradigma chiamato **Client-side Validation** che, a differenza della blockchain o di Lightning, consiste nel memorizzare e validare localmente (lato client) le transizioni di stato di uno smart contract. Questo si differenzia anche da altre tecniche "DeFi" (_rollup_, _plasma_, _ARK_, ecc.), in quanto la Client-side Validation si affida alla blockchain per prevenire i doppi pagamenti e per avere un sistema di time-stamping, mantenendo il registro degli stati e delle transizioni fuori dalla catena, solo con i partecipanti interessati.

![RGB-Bitcoin](assets/fr/003.webp)

In seguito, introdurremo anche un termine importante: la nozione di "**stash**", che si riferisce all'insieme dei dati lato client necessari per preservare lo stato di un contratto, dato che questi dati non sono replicati globalmente nella rete. Infine, esamineremo la logica alla base di RGB, un protocollo che sfrutta la convalida lato client, e il motivo per cui integra gli approcci esistenti (blockchain e canali di stato).

### Trilemmi nell'informatica distribuita

Per capire come la convalida lato client e l'RGB affrontino i problemi non risolti da blockchain e Lightning, scopriamo i 3 principali "trilemmi" dell'informatica distribuita:


- Scalabilità, decentralizzazione, privacy** ;
- Teorema CAP** (consistenza, disponibilità, tolleranza partizione) ;
- Trilemma CIA** (Riservatezza, Integrità, Disponibilità).

#### 1. Scalabilità, decentralizzazione e riservatezza


- Blockchain (Bitcoin)**

La blockchain è altamente decentralizzata, ma non è molto scalabile. Inoltre, poiché tutto è in un registro pubblico globale, la riservatezza è limitata. Possiamo cercare di migliorare la riservatezza con tecnologie a conoscenza zero (transazioni riservate, schemi mimblewimble, ecc.), ma la catena pubblica non può nascondere il grafico delle transazioni.


- Fulmini/canali di stato**

I canali statali (come la Lightning Network) sono più scalabili e più privati della blockchain, poiché le transazioni avvengono fuori dalla catena. Tuttavia, l'obbligo di annunciare pubblicamente alcuni elementi (transazioni di finanziamento, topologia della rete) e il monitoraggio del traffico di rete possono in parte compromettere la riservatezza. Anche la decentralizzazione ne risente: il routing richiede molto denaro e i nodi principali possono diventare punti di centralizzazione. Questo è proprio il fenomeno che stiamo iniziando a vedere su Lightning.


- Convalida lato client (RGB)**

Questo nuovo paradigma è ancora più scalabile e più confidenziale, perché non solo possiamo integrare tecniche di proof-of-knowledge a zero rivelazioni, ma non esiste un grafo globale delle transazioni, poiché nessuno possiede l'intero registro. D'altra parte, implica anche un certo compromesso sulla decentralizzazione: l'emittente di uno smart contract può avere un ruolo centrale (come un "contract deployer" in Ethereum). Tuttavia, a differenza della blockchain, con la Client-side Validation si memorizzano e si convalidano solo i contratti a cui si è interessati, il che migliora la scalabilità evitando di dover scaricare e verificare tutti gli stati esistenti.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Teorema CAP (Consistenza, disponibilità, tolleranza alle partizioni)

Il teorema CAP sottolinea che è impossibile per un sistema distribuito soddisfare simultaneamente la coerenza (*Consistenza*), la disponibilità (*Disponibilità*) e la tolleranza alle partizioni (*Tolleranza alle partizioni*).


- Blockchain**

La blockchain favorisce la coerenza e la disponibilità, ma non si adatta bene alla suddivisione della rete: se non si può vedere un blocco, non si può agire e avere la stessa visione dell'intera rete.


- Fulmine** (in francese)

Un sistema di canali di stato ha una tolleranza alla disponibilità e al partizionamento (poiché due nodi possono rimanere connessi tra loro anche se la rete è frammentata), ma la coerenza complessiva dipende dall'apertura e dalla chiusura dei canali sulla blockchain.


- Convalida lato client (RGB)**

Un sistema come RGB offre coerenza (ogni partecipante convalida i propri dati a livello locale, senza ambiguità) e tolleranza al partizionamento (si conservano i dati in modo autonomo), ma non garantisce la disponibilità globale (ognuno deve assicurarsi di avere i pezzi di storia rilevanti, e alcuni partecipanti potrebbero non pubblicare nulla o smettere di condividere certe informazioni).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. Trilemma CIA (Riservatezza, Integrità, Disponibilità)

Questo trilemma ci ricorda che riservatezza, integrità e disponibilità non possono essere ottimizzate allo stesso tempo. Blockchain, Lightning e Client-side Validation rientrano in questo equilibrio in modo diverso. L'idea è che nessun singolo sistema può fornire tutto; è necessario combinare diversi approcci (il time-stamping della blockchain, l'approccio sincrono di Lightning e la validazione locale con RGB) per ottenere un pacchetto coerente che offra buone garanzie in ogni dimensione.

![RGB-Bitcoin](assets/fr/006.webp)

### Il ruolo della blockchain e la nozione di sharding

La blockchain (in questo caso, Bitcoin) serve principalmente come meccanismo di _stampaggio_ e protezione contro le doppie spese. Invece di inserire i dati completi di uno smart contract o di un sistema decentralizzato, ci limitiamo a includere **impegni crittografici** (_commitments_) alle transazioni (nel senso di Client-side Validation, che chiameremo "transizioni di stato"). Quindi :


- Liberiamo la blockchain da una grande quantità di dati e di logica;
- Ogni utente memorizza solo la cronologia necessaria per la propria porzione di contratto (il suo "*shard*"), invece di replicare lo stato globale.

Lo sharding è un concetto nato nei database distribuiti (ad esempio MySQL per i social network come Facebook o Twitter). Per risolvere il problema del volume dei dati e delle latenze di sincronizzazione, il database viene segmentato in _shard_ (USA, Europa, Asia, ecc.). Ogni segmento è coerente a livello locale e solo parzialmente sincronizzato con gli altri.

Per gli smart contract di tipo RGB, gli shard vengono suddivisi in base ai contratti stessi. Ogni contratto è uno _shard_ indipendente. Ad esempio, se si possiedono solo token USDT, non è necessario memorizzare o convalidare l'intera storia di un altro token come USDC. Su Bitcoin, la blockchain non fa _sharding_: si ha un insieme globale di UTXO. Con la convalida lato client, ogni partecipante conserva solo i dati del contratto che detiene o utilizza.

Possiamo quindi immaginare l'ecosistema come segue:


- La blockchain (Bitcoin)** come base che assicura la replica completa di un registro minimo e serve come livello di marcatura temporale;
- Lightning Network** per transazioni rapide e riservate, sempre basate sulla sicurezza e sul regolamento finale della blockchain Bitcoin;
- RGB e Client-side Validation** per aggiungere una logica smart contract più complessa, senza ingombrare la blockchain o perdere la riservatezza.

![RGB-Bitcoin](assets/fr/007.webp)

Questi tre elementi formano un insieme triangolare, piuttosto che una pila lineare di "strato 2", "strato 3" e così via. Lightning può collegarsi direttamente a Bitcoin o essere associato a transazioni Bitcoin che incorporano dati RGB. Allo stesso modo, un utilizzo "BiFi" (finanza su Bitcoin) può comporsi con la blockchain, con Lightning e con RGB a seconda delle esigenze di riservatezza, scalabilità o logica contrattuale.

![RGB-Bitcoin](assets/fr/008.webp)

### La nozione di transizioni di stato

In qualsiasi sistema distribuito, l'obiettivo del meccanismo di convalida è quello di essere in grado di **determinare la validità e l'ordine cronologico dei cambiamenti di stato**. L'obiettivo è verificare che le regole del protocollo siano state rispettate e dimostrare che questi cambiamenti di stato si susseguono in un ordine definitivo e inattaccabile.

Per capire come funziona questa convalida nel contesto di **Bitcoin** e, più in generale, per comprendere la filosofia che sta alla base della Client-side Validation, diamo prima uno sguardo ai meccanismi della blockchain di Bitcoin, prima di vedere come la Client-side Validation si differenzia da essi e quali ottimizzazioni rende possibili.

![RGB-Bitcoin](assets/fr/009.webp)

Nel caso della blockchain Bitcoin, la convalida delle transazioni si basa su una semplice regola:


- Tutti i nodi della rete scaricano ogni blocco e transazione;
- Convalidano queste transazioni per verificare la corretta evoluzione dell'insieme UTXO (tutte le uscite non spese);
- Memorizzano questi dati (sotto forma di blocchi) in modo che la storia possa essere riprodotta se necessario.

![RGB-Bitcoin](assets/fr/010.webp)

Tuttavia, questo modello presenta due svantaggi principali:


- Scalabilità**: poiché ogni nodo deve elaborare, verificare e archiviare le transazioni di tutti, esiste un ovvio limite alla capacità di transazione, legato in particolare alla dimensione massima del blocco (1 MB in media su 10 minuti per Bitcoin, esclusi i cookie);
- Privacy**: tutto viene trasmesso e memorizzato pubblicamente (importi, indirizzi di destinazione, ecc.), il che limita la riservatezza degli scambi.

![RGB-Bitcoin](assets/fr/012.webp)

In pratica, questo modello funziona per Bitcoin come livello di base (Layer 1), ma può diventare insufficiente per usi più complessi che richiedono contemporaneamente un'elevata velocità di transazione e un certo grado di riservatezza.

La convalida lato client si basa sull'idea opposta: invece di richiedere all'intera rete di convalidare e memorizzare tutte le transazioni, ogni partecipante (client) convaliderà solo la parte della cronologia che lo riguarda:


- Quando una persona riceve un bene (o qualsiasi altra proprietà digitale), deve solo conoscere e verificare la catena di operazioni (transizioni di stato) che portano a quel bene e provarne la legittimità;
- Questa sequenza di operazioni, dalla ***Genesi*** (emissione iniziale) alla transazione più recente, forma un grafo diretto aciclico (DAG) o shard, cioè una frazione della storia complessiva.

![RGB-Bitcoin](assets/fr/013.webp)

Allo stesso tempo, affinché il resto della rete (o più precisamente il livello sottostante, come Bitcoin) possa bloccare lo stato finale senza vedere i dettagli di questi dati, la convalida lato client si basa sulla nozione di ***impegno***.

Un *impegno* è un impegno crittografico, tipicamente un _hash_ (SHA-256 per esempio) inserito in una transazione Bitcoin, che dimostra che sono stati inseriti dati privati, senza rivelarli.

Grazie a questi _impegni_, possiamo dimostrare:


- L'esistenza dell'informazione (poiché è impegnata in un hash) ;
- L'anteriorità di queste informazioni (perché ancorate e marcate temporalmente nella blockchain, con una data e un ordine di blocco).

Il contenuto esatto, tuttavia, non viene rivelato, preservando così la sua riservatezza.

In concreto, ecco come funziona una transizione di stato RGB:


- Si prepara una nuova transizione di stato (ad esempio il trasferimento di un token RGB);
- Si genera un impegno crittografico per questa transizione e lo si inserisce in una transazione Bitcoin (questi impegni sono chiamati "*ancore*" nel protocollo RGB);
- La controparte (il destinatario) recupera la storia lato cliente associata a questo asset e ne convalida la coerenza end-to-end, dalla genesi dello smart contract alla transizione che gli trasmettete.

![RGB-Bitcoin](assets/fr/014.webp)

La convalida lato client offre due vantaggi principali:


- Scalabilità:**

Gli impegni (*commitments*) inclusi nella blockchain sono piccoli (dell'ordine di qualche decina di byte). Ciò garantisce che lo spazio dei blocchi non sia saturo, poiché è necessario includere solo l'hash. Inoltre, consente al protocollo off-chain di evolversi, poiché ogni utente deve memorizzare solo il proprio frammento di storia (il proprio _stash_).


- Privacy :**

Le transazioni stesse (cioè il loro contenuto dettagliato) non sono pubblicate sulla catena. Lo sono solo le loro impronte digitali (*hash*). Pertanto, gli importi, gli indirizzi e la logica del contratto rimangono privati e il destinatario può verificare, localmente, la validità del suo shard ispezionando tutte le transizioni precedenti. Non c'è motivo per il ricevente di rendere pubblici questi dati, se non in caso di controversia o quando è necessaria una prova.

In un sistema come RGB, più transizioni di stato provenienti da contratti diversi (o da asset diversi) possono essere aggregate in un'unica transazione Bitcoin tramite un singolo _commitment_. Questo meccanismo stabilisce un collegamento deterministico, con data e ora, tra la transazione on-chain e i dati off-chain (le transizioni convalidate dal lato client) e consente a più frammenti di essere registrati simultaneamente in un singolo punto di ancoraggio, riducendo ulteriormente il costo e l'ingombro on-chain.

In pratica, quando questa transazione Bitcoin viene convalidata, "blocca" definitivamente lo stato dei contratti sottostanti, poiché diventa impossibile modificare l'hash già iscritto nella blockchain.

![RGB-Bitcoin](assets/fr/015.webp)

### Il concetto di scorta

Lo **stash** è l'insieme dei dati lato client che un partecipante deve assolutamente conservare per mantenere l'integrità e la storia di uno smart contract RGB. A differenza di un canale Lightning, dove alcuni stati possono essere ricostruiti localmente da informazioni condivise, lo stash di un contratto RGB non è replicato altrove: se lo perdete, nessuno sarà in grado di ripristinarlo, poiché siete responsabili della vostra parte di storia. Per questo motivo è necessario adottare un sistema con procedure di backup affidabili in RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Sigillo monouso: origini e funzionamento

Quando si accetta un bene come una valuta, sono essenziali due garanzie:


- L'autenticità dell'articolo ricevuto;
- L'unicità dell'articolo ricevuto, per evitare doppie spese.

Per i beni fisici, come una banconota, la presenza fisica è sufficiente a dimostrare che non è stata duplicata. Tuttavia, nel mondo digitale, dove gli asset sono puramente informativi, questa verifica è più complessa, poiché le informazioni possono facilmente moltiplicarsi ed essere duplicate.

Come abbiamo visto in precedenza, la rivelazione da parte del mittente della storia delle transizioni di stato ci permette di garantire l'autenticità di un token RGB. Avendo accesso a tutte le transazioni successive alla transazione genetica, possiamo confermare l'autenticità del token. Questo principio è simile a quello di Bitcoin, dove la storia delle monete può essere rintracciata fino alla transazione originale su coinbase per verificarne la validità. Tuttavia, a differenza di Bitcoin, la storia delle transizioni di stato in RGB è privata e conservata dal lato del cliente.

Per evitare il doppio utilizzo dei gettoni RGB, utilizziamo un meccanismo chiamato "**Single-use Seal**". Questo sistema garantisce che ogni gettone, una volta utilizzato, non possa essere riutilizzato in modo fraudolento una seconda volta.

I sigilli monouso sono primitive crittografiche, proposte nel 2016 da Peter Todd, simili al concetto di sigillo fisico: una volta che un sigillo è stato posto su un contenitore, diventa impossibile aprirlo o modificarlo senza rompere irreversibilmente il sigillo.

![RGB-Bitcoin](assets/fr/018.webp)

Questo approccio, trasposto al mondo digitale, permette di dimostrare che una sequenza di eventi è effettivamente avvenuta e che non può più essere alterata a posteriori. I sigilli monouso vanno quindi oltre la semplice logica di "hash + timestamp", aggiungendo la nozione di sigillo che può essere chiuso "una sola volta".

![RGB-Bitcoin](assets/fr/017.webp)

Affinché i sigilli monouso funzionino, è necessario un mezzo di prova della pubblicazione in grado di dimostrare l'esistenza o l'assenza di una pubblicazione e difficile (se non impossibile) da falsificare una volta che l'informazione è stata diffusa. Una **blockchain** (come Bitcoin) può svolgere questo ruolo, così come, ad esempio, un giornale cartaceo a diffusione pubblica. L'idea è la seguente:


- Si vuole dimostrare che un certo impegno su un messaggio `h(m)` è stato pubblicato ad un pubblico senza rivelare il contenuto del messaggio `m` ;
- Si vuole dimostrare che nessun altro messaggio di impegno concorrente `h(m')` è stato pubblicato al posto di `h(m)` ;
- Vogliamo anche essere in grado di controllare che il messaggio `m` esista prima di una certa data.

Una blockchain si presta in modo ideale a questo ruolo: non appena una transazione viene inserita in un blocco, l'intera rete ha la stessa prova non falsificabile della sua esistenza e del suo contenuto (almeno in parte, dato che l'_impegno_ può nascondere i dettagli, pur dimostrando l'autenticità del messaggio).

Un sigillo monouso può quindi essere visto come una promessa formale di pubblicare un messaggio (ancora sconosciuto in questa fase) una e una sola volta, in un modo che può essere verificato da tutte le parti interessate.

A differenza dei semplici _impegni_ (hash) o dei timestamp, che attestano una data di esistenza, un sigillo monouso offre l'ulteriore garanzia che **nessun impegno alternativo** può coesistere: non è possibile chiudere due volte lo stesso sigillo, né tentare di sostituire il messaggio sigillato.

Il seguente confronto aiuta a comprendere questo principio:


- Impegno crittografico (hash)**: Con una funzione hash, è possibile impegnarsi su un dato (un numero) pubblicando il suo hash. I dati rimangono segreti finché non si rivela la pre-immagine, ma si può dimostrare di conoscerli in anticipo;
- Timestamp (blockchain)**: Inserendo questo hash nella blockchain, dimostriamo anche di conoscerlo in un momento preciso (quello dell'inclusione in un blocco);
- Sigillo monouso**: Con i sigilli monouso, facciamo un passo avanti rendendo unico l'impegno. Con un singolo hash, è possibile creare diversi impegni contraddittori in parallelo (il problema del medico che annuncia "*È un maschio*" alla famiglia e "*È una femmina*" nel suo diario personale). Il sigillo monouso elimina questa possibilità collegando l'impegno a un mezzo di prova della pubblicazione, come la blockchain di Bitcoin, in modo che una spesa di UTXO suggelli definitivamente l'impegno. Una volta speso, lo stesso UTXO non può essere speso nuovamente per sostituire l'impegno.

| Sigilli monouso | Timestamps | Impegno semplice (digest/hash) | Sigilli monouso

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

la pubblicazione dell'impegno non rivela il messaggio | Si | Si | Si | Si | Si

prova della data dell'impegno/esistenza del messaggio prima di una certa data | Impossibile | Possibile | Possibile | Possibile | Possibile

| Prova che non può esistere nessun altro impegno alternativo | Impossibile | Possibile |

I sigilli monouso funzionano in tre fasi principali:

**Definizione di guarnizione :**


- Alice definisce in anticipo le regole per la pubblicazione del sigillo (quando, dove e come verrà pubblicato il messaggio);
- Bob accetta o riconosce queste condizioni.

![RGB-Bitcoin](assets/fr/021.webp)

**Chiusura ermetica :**


- In fase di esecuzione, Alice chiude il sigillo pubblicando il messaggio effettivo (di solito sotto forma di un _commitment_, ad esempio un hash);
- Fornisce inoltre un **testimone** (prova crittografica) che dimostra che il sigillo è chiuso e irrevocabile.

![RGB-Bitcoin](assets/fr/019.webp)

**Verifica della tenuta :**


- Una volta chiuso il sigillo, Bob non può più aprirlo: può solo verificare che sia stato chiuso;
- Bob raccoglie il sigillo, il **testimone** e il messaggio (o il suo impegno) per assicurarsi che tutto corrisponda e che non ci siano sigilli concorrenti o versioni diverse.

Il processo può essere riassunto come segue:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

La convalida lato client, tuttavia, fa un ulteriore passo avanti: se la definizione stessa di un sigillo rimane al di fuori della blockchain, è possibile (in teoria) che qualcuno contesti l'esistenza o la legittimità del sigillo in questione. Per superare questo problema, viene utilizzata una catena di sigilli monouso interconnessi:


- Ogni sigillo chiuso contiene la definizione del sigillo successivo;
- Registriamo queste chiusure (con i loro _impegni_) all'interno della blockchain (in una transazione Bitcoin);
- Pertanto, qualsiasi tentativo di modificare un sigillo precedente sarebbe in contraddizione con la storia incorporata in Bitcoin.

Questo è esattamente ciò che fa il sistema RGB:


- I messaggi pubblicati sono _impegni_ a dati convalidati dal lato client;
- La definizione di sigillo è associata a un Bitcoin UTXO ;
- Il sigillo si chiude quando questo UTXO viene speso o quando una nuova uscita viene accreditata allo stesso impegno;
- La catena di transazioni che spende questi UTXO corrisponde alla prova di pubblicazione: ogni transizione o cambiamento di stato su RGB è quindi ancorato in Bitcoin.

Per riassumere:


- La _definizione di sigillo_ è l'UTXO che si intende sigillare per un impegno futuro;
- La _chiusura del sigillo_ avviene quando si spende questo UTXO, creando una transazione che contiene l'impegno;
- Il _testimone_ è la transazione stessa, che prova che avete chiuso il sigillo con questo contenuto;
- Non si può provare che un sigillo non sia stato chiuso (non si può essere assolutamente certi che un UTXO non sia già stato speso o non sarà speso in un blocco che non si è ancora visto), ma si può provare che è stato effettivamente chiuso.

Questa unicità è importante per la convalida lato client: quando si convalida una transizione di stato, si controlla che corrisponda a un UTXO unico, non speso in precedenza in un impegno concorrente. Questo è ciò che garantisce l'assenza di doppie spese negli smart contract off-chain.

### Molteplici impegni e radici

Uno smart contract RGB può avere bisogno di spendere diversi Single-use Seals (diversi UTXO) contemporaneamente. Inoltre, una singola transazione Bitcoin può fare riferimento a diversi contratti distinti, ognuno dei quali sigilla la propria transizione di stato. Ciò richiede un meccanismo di **multi-commitment** per dimostrare, in modo deterministico e univoco, che nessuno degli impegni esiste in duplice copia. È qui che entra in gioco la nozione di **ancora** in RGB: una struttura speciale che collega una transazione Bitcoin e uno o più impegni lato client (transizioni di stato), ciascuno potenzialmente appartenente a un contratto diverso. Analizzeremo più da vicino questo concetto nel prossimo capitolo.

![RGB-Bitcoin](assets/fr/023.webp)

Due dei principali repository GitHub del progetto (sotto l'organizzazione LNPBP) raggruppano le implementazioni di base di questi concetti studiati nel primo capitolo:


- client_side_validation** : Contiene primitive Rust per la validazione locale ;
- sigilli_di_uso**: Implementa la logica per definire e chiudere questi sigilli in modo sicuro.

![RGB-Bitcoin](assets/fr/020.webp)

Si noti che questi mattoni software sono agnostici rispetto a Bitcoin; in teoria, potrebbero essere applicati a qualsiasi altro mezzo di prova della pubblicazione (un altro registro, una rivista, ecc.). In pratica, RGB si affida a Bitcoin per la sua robustezza e l'ampio consenso.

![RGB-Bitcoin](assets/fr/021.webp)

### Domande del pubblico

#### Verso un uso più ampio delle guarnizioni monouso

Peter Todd ha anche creato il protocollo _Open Timestamps_ e il concetto di Single-use Seal è una naturale estensione di queste idee. Oltre a RGB, si possono prevedere altri casi d'uso, come la costruzione di _sidechain_ senza ricorrere al _merge mining_ o proposte legate alle drivechain come BIP300. In linea di principio, qualsiasi sistema che richieda un singolo impegno può sfruttare questa primitiva crittografica. Oggi RGB è la prima grande implementazione su scala reale.

#### Problemi di disponibilità dei dati

Poiché nella Validazione lato client ogni utente memorizza la propria parte di cronologia, la disponibilità dei dati non è garantita a livello globale. Se l'emittente di un contratto nasconde o revoca alcune informazioni, l'utente potrebbe non essere a conoscenza dell'effettiva evoluzione dell'offerta. In alcuni casi (come le stablecoin), l'emittente è tenuto a mantenere dati pubblici per dimostrare il volume in circolazione, ma non vi è alcun obbligo tecnico in tal senso. È quindi possibile progettare contratti deliberatamente opachi con un'offerta illimitata, il che solleva questioni di fiducia.

#### Sharding e isolamento dei contratti

Ogni contratto rappresenta uno _shard_ isolato: USDT e USDC, ad esempio, non devono condividere le loro cronologie. Gli scambi atomici sono ancora possibili, ma non comportano la fusione dei loro registri. Tutto avviene tramite impegno crittografico, senza rivelare l'intero grafico della storia a ciascun partecipante.

### Conclusione

Abbiamo visto come il concetto di Client-side Validation si inserisca nella blockchain e nei _canali di stato_, come risponda ai trilemmi dell'informatica distribuita e come sfrutti la blockchain Bitcoin in modo unico per evitare la doppia spesa e per il *time-stamping*. L'idea si basa sulla nozione di **Single-use Seal**, che consente di creare impegni unici che non possono essere riutilizzati a piacimento. In questo modo, ogni partecipante carica solo la cronologia strettamente necessaria, aumentando la scalabilità e la riservatezza dei contratti intelligenti e mantenendo la sicurezza di Bitcoin come sfondo.

Il prossimo passo sarà quello di spiegare in modo più dettagliato come questo meccanismo di Single-use Seal viene applicato in Bitcoin (tramite gli UTXO), come vengono create e convalidate le ancore e quindi come vengono costruiti gli smart contract completi in RGB. In particolare, esamineremo la questione degli impegni multipli, la sfida tecnica di dimostrare che una transazione Bitcoin sigilla simultaneamente più transizioni di stato in contratti diversi, senza introdurre vulnerabilità o doppi impegni.

Prima di immergerci nei dettagli tecnici del secondo capitolo, rileggiamo le definizioni chiave (Client-side Validation, Single-use Seal, ancore, ecc.) e teniamo a mente la logica generale: stiamo cercando di conciliare i punti di forza della blockchain Bitcoin (sicurezza, decentralizzazione, time-stamping) con quelli delle soluzioni off-chain (velocità, riservatezza, scalabilità), ed è proprio questo che RGB e Client-side Validation cercano di ottenere.

## Il livello di impegno

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

In questo capitolo esamineremo l'implementazione della convalida lato client e dei sigilli monouso nella blockchain Bitcoin. Presenteremo i principi principali del **commitment layer** di RGB (layer 1), con particolare attenzione allo schema **TxO2**, che RGB utilizza per definire e chiudere un sigillo in una transazione Bitcoin. Successivamente, discuteremo due punti importanti che non sono ancora stati trattati in dettaglio:


- Gli _impegni deterministici di Bitcoin_;
- Impegni multiprotocollo.

È la combinazione di questi concetti che ci permette di sovrapporre diversi sistemi o contratti a un unico UTXO e quindi a un'unica blockchain.

Va ricordato che le operazioni crittografiche descritte possono essere applicate, in termini assoluti, ad altre blockchain o supporti editoriali, ma le caratteristiche di Bitcoin (in termini di decentralizzazione, resistenza alla censura e apertura a tutti) lo rendono la base ideale per sviluppare una programmabilità avanzata come quella richiesta da **RGB**.

### Schemi di impegno in Bitcoin e loro utilizzo da parte di RGB

Come abbiamo visto nel primo capitolo del corso, i sigilli monouso sono un concetto generale: facciamo una promessa di includere un impegno (_commitment_) in una posizione specifica di una transazione, e questa posizione agisce come un sigillo che chiudiamo su un messaggio. Tuttavia, sulla blockchain Bitcoin, ci sono diverse opzioni per scegliere dove collocare questo _impegno_.

Per capire la logica, ricordiamo il principio di base: per chiudere un _sigillo a uso singolo_, spendiamo l'area sigillata inserendo il _commitment_ su un determinato messaggio. In Bitcoin, questo può essere fatto in diversi modi:


- Utilizzare una chiave pubblica o un indirizzo**

Possiamo decidere che una chiave o un indirizzo pubblico specifico sia il _single-use seal_. Non appena questa chiave o indirizzo appare sulla catena in una transazione, significa che il sigillo è stato chiuso con un certo messaggio.


- Utilizzare un output di transazione Bitcoin**

Ciò significa che un _sigillo monouso_ è definito come un preciso _outpoint_ (una coppia TXID + numero di uscita). Non appena questo _outpoint_ viene esaurito, il sigillo viene chiuso.

Mentre lavoravamo su RGB, abbiamo identificato almeno 4 modi diversi per implementare questi sigilli su Bitcoin:


- Definire il sigillo tramite una chiave pubblica e chiuderlo in un _output_ ;
- Definire il sigillo con un _outpoint_ e chiuderlo con un _output_ ;
- Definire il sigillo tramite il valore di una chiave pubblica e chiuderlo in un _input_ ;
- Definire il sigillo tramite un _outpoint_ e chiuderlo in un _input_.

| Definizione del sigillo | Chiusura del sigillo | Requisiti aggiuntivi | Applicazione principale | Possibili schemi d'impegno

| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |

| P2(W)PKH | Nessuno al momento | Keytweak, taptweak, opret |

| TxO2 | Transaction output | Transaction output | Richiede impegni deterministici su Bitcoin | RGBv1 (universale) | Keytweak, tapret, opret |

| PkI | Valore della chiave pubblica | Voce di transazione | Solo Taproot e non compatibile con i portafogli Legacy | Identità basate su Bitcoin | Sigtweak, witweak |

| TxO1 | Uscita transazione | Ingresso transazione | Solo Taproot e non compatibile con i portafogli Legacy | Al momento nessuno | Sigtweak, witweak |

Non entreremo nel dettaglio di ciascuna di queste configurazioni, poiché in RGB abbiamo scelto di utilizzare **un _outpoint_ come definizione del sigillo**, e di collocare il _commitment_ nell'output della transazione che spende questo _outpoint_. Possiamo quindi introdurre i seguenti concetti per il seguito:


- "Definizione del sigillo "** : Un dato _outpoint_ (identificato da TXID + n. uscita) ;
- "Chiusura del sigillo "**: La transazione che spende questo _outpoint_, in cui viene aggiunto un _commitment_ a un messaggio.

Questo schema è stato scelto per la sua compatibilità con l'architettura RGB, ma altre configurazioni potrebbero essere utili per usi diversi.

La "O2" di "TxO2" ci ricorda che sia la definizione che la chiusura si basano sulla spesa (o sulla creazione) di un output di transazione.

### Esempio di diagramma TxO2

Come promemoria, la definizione di un _single-use seal_ non richiede necessariamente la pubblicazione di una transazione sulla catena. È sufficiente che Alice, ad esempio, abbia già un UTXO non speso. Può decidere: "Questo _outpoint_ (già esistente) è ora il mio sigillo". Lo annota localmente (lato cliente) e finché questo UTXO non viene speso, il sigillo è considerato aperto.

![RGB-Bitcoin](assets/fr/024.webp)

Il giorno in cui vuole chiudere il sigillo (per segnalare un evento o per ancorare un particolare messaggio), spende questo UTXO in una nuova transazione (questa transazione è spesso chiamata "transazione di testimonianza" (non correlata a _segwit_, è solo il termine che gli diamo). Questa nuova transazione conterrà il _commitment_ al messaggio.

![RGB-Bitcoin](assets/fr/025.webp)

Si noti che in questo esempio :


- Nessuno tranne Bob (o le persone a cui Alice sceglie di rivelare la prova completa) saprà che un certo messaggio è nascosto in questa transazione;
- Tutti possono vedere che il _punto di uscita_ è stato speso, ma solo Bob possiede la prova che il messaggio è effettivamente ancorato alla transazione.

Per illustrare questo schema TxO2, possiamo utilizzare un _single-use seal_ come meccanismo di revoca di una chiave PGP. Invece di pubblicare un certificato di revoca sui server, Alice può dire: "Questa uscita di Bitcoin, se spesa, significa che la mia chiave PGP è revocata".

Alice dispone quindi di uno specifico UTXO, al quale è associato localmente (sul lato client) un determinato stato o dato (noto solo a lei).

Alice informa Bob che se questo UTXO viene speso, si riterrà che si sia verificato un particolare evento. Dall'esterno, tutto ciò che vediamo è una transazione Bitcoin; ma Bob sa che questa spesa ha un significato nascosto.

![RGB-Bitcoin](assets/fr/026.webp)

Quando Alice spende questo UTXO, chiude il sigillo su un messaggio che indica la sua nuova chiave, o semplicemente la revoca di quella vecchia. In questo modo, chiunque controlli la catena vedrà che l'UTXO è stato speso, ma solo chi ha la prova completa saprà che si tratta proprio della revoca della chiave PGP.

![RGB-Bitcoin](assets/fr/027.webp)

Affinché Bob o chiunque altro possa verificare il messaggio nascosto, Alice deve fornirgli informazioni fuori dalla catena.

![RGB-Bitcoin](assets/fr/028.webp)

Alice deve quindi fornire a Bob :


- Il messaggio stesso (ad esempio, la nuova chiave PGP) ;
- Prova crittografica che il messaggio è stato coinvolto nella transazione (nota come _extra transaction proof_ o _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Le terze parti non dispongono di queste informazioni. Vedono solo che è stato speso un UTXO. La riservatezza è quindi garantita.

Per chiarire la struttura, riassumiamo il processo in due operazioni:


- Transazione 1**: Contiene la _definizione del sigillo_, cioè il _punto di uscita_ che servirà da sigillo.

![RGB-Bitcoin](assets/fr/031.webp)


- Operazione 2**: Spende questo _outpoint_. Chiude il sigillo e, nella stessa transazione, inserisce il _commitment_ sul messaggio.

![RGB-Bitcoin](assets/fr/033.webp)

Per questo motivo chiamiamo la seconda transazione "transazione del testimone".

Per illustrare questo aspetto da un altro punto di vista, possiamo rappresentare due strati:


- Il livello superiore (blockchain, pubblico)**: tutti vedono la transazione e sanno che è stato speso un _outpoint_;
- Il livello inferiore (lato client, privato)** : solo Alice (o la persona interessata) sa che questa spesa corrisponde a tale e tal altro messaggio, tramite la prova crittografica e il messaggio che conserva localmente.

![RGB-Bitcoin](assets/fr/034.webp)

Ma al momento di chiudere il sigillo, si pone il problema di dove inserire l'impegno

Nella sezione precedente, abbiamo brevemente accennato a come il modello di validazione lato client possa essere applicato a RGB e ad altri sistemi. Qui affrontiamo la parte relativa agli **impegni deterministici di Bitcoin** e a come integrarli in una transazione. L'idea è quella di capire perché stiamo cercando di inserire un singolo impegno nella _transazione testimone_, e soprattutto come garantire che non ci possano essere altri impegni concorrenti non rivelati.

### Luoghi di impegno in una transazione

Quando si fornisce a qualcuno la prova che un certo messaggio è incorporato in una transazione, bisogna essere in grado di garantire che non ci sia un'altra forma di impegno (un secondo messaggio nascosto) nella stessa transazione che non è stata rivelata. Affinché la validazione lato client rimanga robusta, è necessario un meccanismo **deterministico** per inserire un singolo _impegno_ nella transazione che chiuda il _single-use seal_.

La _transazione testimone_ spende il famoso UTXO (o _definizione del sigillo_) e questa spesa corrisponde alla chiusura del sigillo. Tecnicamente parlando, sappiamo che ogni outpoint può essere speso una sola volta. È proprio questo che sta alla base della resistenza di Bitcoin alla doppia spesa. Ma la transazione di spesa può avere diversi _ingressi_, diverse _uscite_, o essere composta in modo complesso (coinjoin, canali Lightning, ecc.). Occorre quindi definire chiaramente dove inserire il _commitment_ in questa struttura, in modo univoco e uniforme.

Qualunque sia il metodo (PkO, TxO2, ecc.), il _commitment_ può essere inserito:


- In un ingresso** tramite :
    - Sigtweak** (modifica la componente `r` della firma ECDSA, simile al principio "Sign-to-contract") ;
    - Witweak** (i dati del testimone _segregato_ della transazione vengono modificati).
- In un Output** via :
    - Keytweak** (la chiave pubblica del destinatario viene "modificata" con il messaggio) ;
    - Opret** (il messaggio viene inserito in un output non spendibile `OP_RETURN`) ;
    - Tapret** (o _Taptweak_), che si basa su taproot per inserire l'impegno nella parte di script di una chiave taproot, modificando così la chiave pubblica in modo deterministico.

![RGB-Bitcoin](assets/fr/035.webp)

Ecco i dettagli di ciascun metodo:

![RGB-Bitcoin](assets/fr/038.webp)

***Tipo di firma (sign-to-contract) :***

Uno schema precedente prevedeva lo sfruttamento della parte casuale di una firma (ECDSA o Schnorr) per incorporare il _commitment_: questa è la tecnica nota come "**Sign-to-contract**". Si sostituisce il nonce generato casualmente con un hash contenente i dati. In questo modo, la firma rivela implicitamente il vostro impegno, senza alcuno spazio aggiuntivo nella transazione. Questo approccio presenta una serie di vantaggi:


- Nessun sovraccarico sulla catena (si usa lo stesso posto del nonce di base);
- In teoria, questo può essere abbastanza discreto, poiché il nonce è inizialmente un dato casuale.

Tuttavia, sono emersi due inconvenienti principali:


- Multisig prima di Taproot: quando si hanno più firmatari, è necessario decidere quale firma porterà l'_impegno_. Le firme possono essere ordinate in modo diverso e se un firmatario si rifiuta, si perde il controllo sull'esito dell'_impegno_;
- MuSig e il nonce condiviso: con Schnorr multisig (*MuSig*), la generazione del nonce è un algoritmo multiparty e diventa praticamente impossibile modificare il nonce individualmente.

In pratica, **sig tweak** non è molto compatibile con l'hardware (portafogli hardware) e i formati esistenti (Lightning, ecc.). Quindi questa grande idea è difficile da mettere in pratica.

***Modifica chiave (pay-to-contract) :***

Il **tweak della chiave** riprende il concetto storico di _pay-to-contract_. Prendiamo la chiave pubblica `X' e la modifichiamo aggiungendo il valore `H(messaggio)`. In particolare, se `X = x * G` e `h = H(messaggio)`, la nuova chiave sarà `X' = X + h * G`. Questa chiave modificata nasconde l'impegno nei confronti del `messaggio'. Il detentore della chiave privata originale può, aggiungendo `h' alla sua chiave privata `x', dimostrare di avere la chiave per spendere l'output. In teoria, questo è elegante, perché :


- L'_impegno_ viene inserito senza aggiungere altri campi;
- Non si memorizza alcun dato aggiuntivo sulla catena.

In pratica, però, ci si scontra con le seguenti difficoltà:


- I portafogli non riconoscono più la chiave pubblica standard, poiché è stata "modificata", quindi non possono facilmente associare UTXO alla vostra chiave abituale;
- I portafogli hardware non sono progettati per firmare con una chiave che non sia derivata dalla loro derivazione standard;
- È necessario adattare gli script, i descrittori, ecc.

Nel contesto di RGB, questo percorso era previsto fino al 2021, ma si è rivelato troppo complicato da far funzionare con gli standard e le infrastrutture attuali.

***Modifica del testimone :***

Un'altra idea, che alcuni protocolli come _inscrizioni ordinali_ hanno messo in pratica, è quella di inserire i dati direttamente nella sezione "testimone" della transazione (da qui l'espressione "witness tweak"). Tuttavia, questo metodo :


- Rende l'impegno immediatamente visibile (si incollano letteralmente i dati grezzi nel testimone);
- Può essere soggetto a censura (i minatori o i nodi possono rifiutarsi di trasmetterlo se è troppo grande o per qualsiasi altra caratteristica arbitraria);
- Consuma spazio nei blocchi, contrariamente all'obiettivo di discrezione e leggerezza di RGB.

Inoltre, il testimone è stato progettato per essere potatile in determinati contesti, il che può rendere più complicato avere prove robuste.

***Apertura-ritorno (opret) :***

Molto semplice nel suo funzionamento, un `OP_RETURN' permette di memorizzare un hash o un messaggio in un campo speciale della transazione. Ma è immediatamente rilevabile: tutti vedono che c'è un _commitment_ nella transazione, e può essere censurato o scartato, oltre ad aggiungere output extra. Poiché questo aumenta la trasparenza e le dimensioni, è considerato meno soddisfacente dal punto di vista di una soluzione di validazione lato client.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

L'ultima opzione è l'uso di **Taproot** (introdotto con BIP341) con lo schema *Tapret*. *Tapret* è una forma più complessa di impegno deterministico, che apporta miglioramenti in termini di ingombro sulla blockchain e di riservatezza per le operazioni contrattuali. L'idea principale è quella di nascondere l'impegno nella parte `Script Path Spend` di una [taproot transaction] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Prima di descrivere come l'impegno viene inserito in una transazione taproot, vediamo la **forma esatta** dell'impegno, che deve **imperativamente** corrispondere a una stringa di 64 byte [costruita](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) come segue:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- I 29 byte `OP_RESERVED`, seguiti da `OP_RETURN`, quindi da `OP_PUSHBYTE_33`, formano la parte _prefisso_ di 31 byte;
- Segue un _commitment_ di 32 byte (di solito la radice Merkle di **MPC**), a cui si aggiunge 1 byte di **Nonce** (per un totale di 33 byte per questa seconda parte).

Quindi il metodo `Tapret` a 64 byte assomiglia a una `Opret` a cui abbiamo anteposto 29 byte di `OP_RESERVED` e aggiunto un byte extra come Nonce.

Per mantenere la flessibilità in termini di implementazione, riservatezza e scalabilità, lo schema Tapret tiene conto di diversi casi d'uso, a seconda dei requisiti:


- Incorporazione unica di un impegno Tapret in una transazione Taproot senza una struttura Script Path preesistente;
- Integrazione di un impegno Tapret in una transazione Taproot già dotata di Script Path.

Analizziamo più da vicino ciascuno di questi due scenari.

#### Incorporazione di Tapret senza percorso di scrittura esistente

In questo primo caso, si parte da una chiave di uscita taproot (*Taproot Output Key*) `Q` che contiene solo la chiave pubblica interna `P` *(Internal Key*), senza alcun percorso di script associato (*Script Path*):

![RGB-Bitcoin](assets/fr/047.webp)


- `P`: la chiave pubblica interna del _Key Path Spend_.
- `G`: il punto di generazione della curva ellittica [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` è il fattore di tweak, calcolato tramite un _tagged hash_ (ad esempio `SHA-256(SHA-256(TapTweak) || P)`), in accordo con [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). Questo dimostra che non esiste uno script nascosto.

Per includere un impegno **Tapret**, aggiungere un **Script Path Spend** con uno **scritto unico**, come segue:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` diventa quindi il nuovo fattore di modifica, compresa la **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` rappresenta la radice di questo **script**, che è semplicemente un hash di tipo `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

La prova dell'inclusione e dell'unicità nell'albero della radice si riduce alla singola chiave pubblica interna `P`.

#### Integrazione di Tapret in un percorso di script preesistente

Il secondo scenario riguarda un output `Q` taproot** più complesso, che contiene già diversi script. Ad esempio, abbiamo un albero di 3 script:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` designa la funzione hash normalizzata di uno script foglia.
- a, B, C` rappresentano gli script già inclusi nella struttura del fittone.

Per aggiungere l'impegno di Tapret, dobbiamo inserire uno *scritto non spendibile* al primo livello dell'albero, spostando gli script esistenti un livello più in basso. Visivamente, l'albero diventa :

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` rappresenta il tag hash del raggruppamento di primo livello `A, B, C`.
- tHT` rappresenta l'hash dello script corrispondente al `Tapret` a 64 byte.

Secondo le regole del taproot, ogni ramo/foglia deve essere combinato secondo un ordine lessicografico di hash. Ci sono due casi possibili:


- `tHT` > `tHABC`: l'impegno di Tapret si sposta a destra dell'albero. La prova di unicità richiede solo `tHABC` e `P` ;
- tHT` < `tHABC`**: l'impegno Tapret è posto a sinistra. Per dimostrare che non esiste un altro impegno Tapret a destra, occorre rivelare `tHAB` e `tHC` per dimostrare l'assenza di un'altra scrittura di questo tipo.

Esempio visivo per il primo caso (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Esempio per il secondo caso (`tHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Ottimizzazione con il nonce

Per migliorare la riservatezza, possiamo "estrarre" (un termine più preciso sarebbe "bruteforcing") il valore della `<Nonce>` (l'ultimo byte del `Tapret` a 64 byte) nel tentativo di ottenere un hash `tHT` tale che `tHABC < tHT`. In questo caso, l'impegno è posto a destra, evitando all'utente di dover divulgare l'intero contenuto di script esistenti per dimostrare l'unicità del Tapret.

In sintesi, il `Tapret` offre un modo discreto e deterministico di incorporare un impegno in una transazione taproot, rispettando al contempo i requisiti di unicità e univocità essenziali per la logica di convalida lato cliente e di sigillo monouso di RGB.

#### Uscite valide

Per le transazioni con impegno RGB, il requisito principale per uno schema di impegno Bitcoin valido è il seguente: La transazione (*transazione testimone*) deve contenere un unico impegno. Questo requisito rende impossibile costruire una cronologia alternativa per i dati convalidati dal lato client all'interno della stessa transazione. Ciò significa che il messaggio attorno al quale si chiude il _single-use seal_ è unico.

Per soddisfare questo principio, e indipendentemente dal numero di uscite in una transazione, si richiede che **una e una sola uscita** possa contenere un impegno (*impegno*). Per ciascuno degli schemi utilizzati (*Opret* o *Tapret*), le uniche uscite valide che possono contenere un _impegno_ RGB sono :


- Il primo output `OP_RETURN` (se presente) per lo schema *Opret*;
- Il primo output taproot (se presente) per lo schema *Tapret*.

Si noti che è possibile che una transazione contenga un singolo impegno `Opret` e un singolo impegno `Tapret` in due output separati. Grazie alla natura deterministica della Seal Definition, questi due impegni corrispondono a due dati distinti convalidati sul lato client.

### Analisi e scelte pratiche in RGB

Quando abbiamo avviato RGB, abbiamo esaminato tutti questi metodi per determinare dove e come inserire un _impegno_ in una transazione in modo deterministico. Abbiamo definito alcuni criteri:


- Compatibilità con diversi scenari (ad es. multisig, Lightning, portafogli hardware, ecc.);
- Impatto sullo spazio della catena ;
- Difficoltà di implementazione e manutenzione ;
- Riservatezza e resistenza alla censura.

| Trace e dimensionamento on-chain | Dimensionamento lato client | Integrazione del portafoglio | Compatibilità hardware | Compatibilità Lightning | Compatibilità Taproot |

| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |

| Keytweak (P2C deterministico) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig |

| Sigtweak (S2C deterministico) | 🟢 | 🟠 | 🔴 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 BOLT, 🟠 Bifrost | - |

| Algoritmo Tapret: nodo in alto a sinistra | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Algoritmo Tapret #4: qualsiasi nodo + prova | 🟢 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Schema di impegno deterministico | Standard | Costo a catena | Dimensione dell'evidenza lato cliente

| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |

| Keytweak (deterministico P2C) | LNPBP-1, 2 | 0 byte | 33 byte (chiave non modificata) |

| Sigtweak (S2C deterministico) | WIP (LNPBP-39) | 0 byte | 0 byte |

| Opret (OP_RETURN) | - | 36 (v)byte (TxOut aggiuntivo) | 0 byte |

| Algoritmo Tapret: nodo in alto a sinistra | LNPBP-6 | 32 byte nel testimone (8 vbyte) su qualsiasi n-di-m multisig e spesa per percorso di script | 0 byte su script taproot senza script ~270 byte in un caso di script singolo, ~128 byte se più di uno script |

| Algoritmo Tapret #4: qualsiasi nodo + prova di unicità | LNPBP-6 | 32 byte nel testimone (8 vbyte) per i casi di script singolo, 0 byte nel testimone nella maggior parte degli altri casi | 0 byte su script senza taproot, 65 byte finché il Taptree non ha una dozzina di script |

| Layer | Costo della catena (byte/vbyte) | Costo della catena (byte/vbyte) | Costo della catena (byte/vbyte) | Costo della catena (byte/vbyte) | Costo della catena (byte/vbyte) | Costo lato cliente (byte) | Costo lato cliente (byte) | Costo lato cliente (byte) | Costo lato cliente (byte) | Costo lato cliente (byte) | Costo lato cliente (byte) | Costo lato cliente (byte) | Costo lato cliente (byte) | Costo lato cliente (byte)

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

**Tipo** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** |

| Single-sig | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | 0? | 0 | 0 |

| MuSig (n-di-n) | 0 | 0 | 0 | 32 | 0 | 0 | 32 | ? > 0 | 0 |

| Multi-sig 2-of-3 | 32/8 | 32/8 o 0 | 0 n/a | 32 | ~270 | 65 | 32 | n/a | 0 |

| Multi-sig 3-of-5 | 32/8 | 32/8 o 0 | 0 n/a | 32 | ~340 | 65 | 32 | n/a | 0 |

| Multi-sig 2-of-3 con timeout | 32/8 | 0 | 0 n/a | 32 | 64 | 65 | 32 | n/a | 0 | 0

| Layer | Costo su catena (vbyte) | Costo su catena (vbyte) | Costo su catena (vbyte) | Costo sul lato client (byte) | Costo sul lato client (byte) |

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Type** | **Base** | **Tapret #2** | **Tapret #4** | **Tapret #2** | **Tapret #4** |

muSig (n-di-n) | 16,5 | 0 | 0 | 0 | 0 | 0 | 0

| FROST (n-of-m) | ? | 0 | 0 | 0 | 0 |

| Multi_a (n-di-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 |

| MuSig branch / Multi_a (n-di-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 | 65

| Con timeout (n-di-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Metodo | Riservatezza e scalabilità | Interoperabilità | Compatibilità | Portabilità | Complessità

| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |

keytweak (P2C deterministico) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 | 🟡 |

sigtweak (S2C deterministico) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 |

opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 | 🟢 |

| Algo Tapret: nodo in alto a sinistra | 🟠 | 🟢 | 🔴 | 🟠 |

| Algo Tapret #4: Qualsiasi nodo + prova | 🟢 | 🟢 | 🟠 | 🔴 |

Nel corso dello studio è emerso chiaramente che nessuno degli schemi di impegno era pienamente compatibile con l'attuale standard Lightning (che non utilizza Taproot, _muSig2_ o un supporto aggiuntivo per gli impegni). Sono in corso sforzi per modificare la costruzione dei canali di Lightning (*BiFrost*) per consentire l'inserimento di impegni RGB. Questa è un'altra area in cui è necessario rivedere la struttura delle transazioni, le chiavi e il modo in cui gli aggiornamenti dei canali vengono firmati.

L'analisi ha mostrato che, in realtà, altri metodi (key tweak, sig tweak, witness tweak, ecc.) presentavano altre forme di complicazione:


- O abbiamo un grande volume sulla catena;
- O c'è un'incompatibilità radicale con il codice del portafoglio esistente;
- O la soluzione non è praticabile in multisig non cooperativo.

Per l'RGB, si distinguono due metodi in particolare: ***Opret*** e ***Tapret***, entrambi classificati come "Transaction Output" e compatibili con la modalità TxO2 utilizzata dal protocollo.

### Impegni multiprotocollo - MPC

In questa sezione, vediamo come **RGB** gestisce l'aggregazione di più contratti (o, più precisamente, dei loro _transition bundles_) all'interno di un singolo impegno (*commitment*) registrato in una transazione Bitcoin attraverso uno schema deterministico (secondo `Opret` o `Tapret`). Per ottenere questo risultato, l'ordine di Merkelizzazione dei vari contratti avviene in una struttura chiamata **albero MPC** (_Multi Protocol Commitment Tree_). In questa sezione vedremo la costruzione di questo albero MPC, come ottenere la sua radice e come più contratti possono condividere la stessa transazione in modo confidenziale e non ambiguo.

L'impegno multiprotocollo (MPC) è stato progettato per soddisfare due esigenze:


- La costruzione dell'hash `mpc::Commitment`: sarà incluso nella blockchain Bitcoin secondo uno schema `Opret` o `Tapret` e deve riflettere tutti i cambiamenti di stato da convalidare;
- Memorizzazione simultanea di più contratti in un unico _commitment_, che consente di gestire aggiornamenti separati su più asset o contratti RGB in un'unica transazione Bitcoin.

In concreto, ogni _fascio di transizione_ appartiene a un particolare contratto. Tutte queste informazioni vengono inserite in un **albero MPC**, la cui radice (`mpc::Root`) viene poi sottoposta a un nuovo hash per ottenere il `mpc::Commitment`. È quest'ultimo hash che viene inserito nella transazione Bitcoin (_transazione testimone_), secondo il metodo deterministico scelto.

![RGB-Bitcoin](assets/fr/042.webp)

#### Hash radice MPC

Il valore effettivamente scritto sulla catena (in `Opret` o `Tapret`) è chiamato `mpc::Commitment`. Viene calcolato nella forma [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), secondo la formula :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

dove :


- `mpc_tag` è un tag: `urn:ubideco:mpc:commitment#2024-01-31`, scelto in base alle [convenzioni di etichettatura RGB] (https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) indica la profondità dell'albero *MPC* ;
- cofactor` (16 bit, in Little Endian) è un parametro utilizzato per promuovere l'unicità delle posizioni assegnate a ciascun contratto nell'albero;
- `mpc::Root` è la radice di *MPC Tree*, calcolata secondo il processo descritto nella prossima sezione.

![RGB-Bitcoin](assets/fr/044.webp)

#### Costruzione di alberi MPC

Per costruire questo albero MPC, dobbiamo assicurarci che ogni contratto corrisponda a un'unica posizione della foglia. Supponiamo di avere :


- c` contratti da includere, indicizzati da `i` in `i = {0,1,...,C-1}` ;
- Per ogni contratto `c_i`, abbiamo un identificatore `ContractId(i) = c_i`.

Si costruisce quindi un albero di larghezza `w` e profondità `d` tale che `2^d = w`, con `w > C`, in modo che ogni contratto possa essere collocato in una _foglia_ separata. La posizione `pos(c_i)` di ogni contratto nell'albero è determinata da :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

dove `cofattore' è un numero intero che aumenta la probabilità di ottenere posizioni distinte per ogni contratto. In pratica, la costruzione segue un processo iterativo:


- Si parte da una profondità minima (`d=3` per convenzione, per nascondere il numero esatto di contratti);
- Proviamo diversi `cofattori` (fino a `w/2`, o un massimo di 500 per motivi di prestazioni);
- Se non riusciamo a posizionare tutti i contratti senza collisioni, incrementiamo `d` e ricominciamo.

L'obiettivo è evitare gli alberi troppo alti, mantenendo il rischio di collisione al minimo. Si noti che il fenomeno della collisione segue una logica di distribuzione casuale, legata al [Paradosso degli Anniversari](https://en.wikipedia.org/wiki/Birthday_problem).

#### Foglie abitate

Una volta ottenute `C` posizioni distinte `pos(c_i)` per i contratti `i = {0,1,...,C-1}`, ogni foglio viene riempito con una funzione hash (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

dove :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, è sempre scelto in base alle convenzioni Merkle di RGB ;
- `0x10` identifica una _foglia di contratto_ ;
- `c_i` è l'identificatore del contratto a 32 byte (derivato dall'hash di Genesis);
- bundleId(c_i)` è un hash di 32 byte che descrive l'insieme delle `Transizioni di stato` relative a `c_i` (raccolte in un *Bundle di transizione*).

#### Foglie disabitate

Le foglie rimanenti, non assegnate a un contratto (cioè le foglie `w - C`), sono riempite con un valore "fittizio" (_foglia di entropia_) :

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

dove :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, è sempre scelto in base alle convenzioni Merkle di RGB ;
- `0x11` denota una _foglia di entropia_ ;
- l'entropia è un valore casuale di 64 byte, scelto dalla persona che costruisce l'albero;
- `j' è la posizione (in 32 bit Little Endian) di questa foglia nell'albero.

#### Nodi MPC

Dopo aver generato le `w` foglie (abitate o meno), si procede alla merkelizzazione. Tutti i nodi interni vengono sottoposti a hash come segue:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

dove :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, è sempre scelto in base alle convenzioni Merkle di RGB ;
- b` è il _fattore di ramificazione_ (8 bit). Molto spesso, `b=0x02` perché l'albero è binario e completo;
- d'è la profondità del nodo nell'albero;
- `w` è la larghezza dell'albero (in formato binario Little Endian a 256 bit);
- tH1` e `tH2` sono gli hash dei nodi figli (o foglie), già calcolati come mostrato sopra.

Procedendo in questo modo, si ottiene la radice `mpc::Root`. Possiamo quindi calcolare `mpc::Commitment` (come spiegato sopra) e inserirlo nella catena.

Per illustrarlo, immaginiamo un esempio in cui `C=3` (tre contratti). Le loro posizioni sono assunte come `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Le altre foglie (posizioni 0, 1, 3, 5, 6) sono _foglie di entropia_. Il diagramma seguente mostra la sequenza di hash fino alla radice con :


- `BUNDLE_i` che rappresenta `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` e così via, che rappresentano foglie (alcune per i contratti, altre per l'entropia) ;
- Ogni ramo `tH_MPC_BRANCH(...)` combina gli hash dei suoi due figli.

Il risultato finale è **mpc::Root**, quindi `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### Controllo dell'albero MPC

Quando un verificatore vuole assicurarsi che un contratto `c_i` (e il suo `BundleId`) sia incluso nel contratto finale `mpc::Commitment`, riceve semplicemente una prova Merkle. Questa prova indica i nodi necessari per risalire dalle foglie (in questo caso, la _foglia di contratto_ di `c_i`) alla radice. Non è necessario rivelare l'intero *albero MPC*: questo protegge la riservatezza degli altri contratti.

Nell'esempio, un verificatore `c_2` ha bisogno solo di un hash intermedio (`tH_MPC_LEAF(D)`), di due `tH_MPC_BRANCH(...)`, della prova di posizione `pos(c_2)` e del valore `cofattore`. Può quindi ricostruire localmente la radice, ricalcolare il `mpc::Commitment` e confrontarlo con quello scritto nella transazione Bitcoin (all'interno di `Opret` o `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Questo meccanismo garantisce che :


- Lo stato relativo a `c_2` è effettivamente incluso nel blocco di informazioni aggregate (lato client);
- Nessuno può costruire una storia alternativa con la stessa transazione, perché il _commitment_ sulla catena punta a un'unica radice MPC.

#### Sintesi della struttura dell'MPC

Il Multi Protocol Commitment* (MPC) è il principio che consente a RGB di aggregare più contratti in un'unica transazione Bitcoin, mantenendo l'unicità degli impegni e la riservatezza nei confronti degli altri partecipanti. Grazie alla costruzione deterministica dell'albero, a ogni contratto viene assegnata una posizione unica e la presenza di foglie "fittizie" (*foglie di entropia*) maschera parzialmente il numero totale di contratti che partecipano alla transazione.

L'intero albero di Merkle non viene mai memorizzato sul client. Viene semplicemente generato un _percorso Merkle_ per ogni contratto interessato, da trasmettere al destinatario (che può quindi convalidare l'impegno). In alcuni casi, si possono avere diverse attività che sono passate attraverso lo stesso UTXO. È quindi possibile unire diversi _tracciati Merkle_ in un cosiddetto _blocco di impegno multiprotocollo_, per evitare di duplicare troppi dati.

Ogni _prova di Merkle_ è quindi leggera, soprattutto perché la profondità dell'albero non supera i 32 in RGB. Esiste anche una nozione di "blocco Merkle", che conserva più informazioni (sezione trasversale, entropia, ecc.), utile per combinare o separare diversi rami.

Ecco perché ci è voluto così tanto tempo per finalizzare RGB. Avevamo la visione generale dal 2019: mettere tutto sul lato client e far circolare i token fuori dalla catena. Ma per dettagli come lo sharding per contratti multipli, la struttura dell'albero di Merkle, la gestione delle collisioni e delle prove di fusione... tutto questo ha richiesto iterazioni.

### Ancore: un'assemblea globale

Dopo aver costruito i nostri impegni (`Opret` o `Tapret`) e il nostro MPC (*Multi Protocol Commitment*), dobbiamo affrontare la nozione di **Anchor** nel protocollo RGB. Un Anchor è una struttura convalidata dal lato client che riunisce gli elementi necessari per verificare che un impegno Bitcoin contenga effettivamente informazioni contrattuali specifiche. In altre parole, un Anchor riassume tutti i dati necessari per convalidare gli _impegni_ descritti sopra.

Un'ancora è composta da tre campi ordinati:


- `Txid`
- prova MPC
- prova di transazione extra - ETP

Ognuno di questi campi svolge un ruolo nel processo di convalida, sia che si tratti di ricostruire la transazione Bitcoin sottostante, sia che si tratti di provare l'esistenza di un impegno nascosto (in particolare nel caso di `Tapret`).

#### TxId

Il campo `Txid` corrisponde all'identificatore a 32 byte della transazione Bitcoin contenente l'impegno `Opret` o `Tapret`.

In teoria, sarebbe possibile trovare questo `Txid` tracciando la catena di transizioni di stato che a loro volta puntano a ogni transazione testimone, seguendo la logica dei sigilli monouso. Tuttavia, per facilitare e accelerare la verifica, questo `Txid` è semplicemente incluso nell'Anchor, evitando così al validatore di dover ripercorrere l'intera storia fuori catena.

#### Prova MPC

Il secondo campo, `MPC Proof`, si riferisce alla prova che questo particolare contratto (ad esempio `c_i`) è incluso nel _Multi Protocol Commitment_. È una combinazione di :


- `pos_i', la posizione di questo contratto nell'albero MPC;
- cofattore`, il valore definito per risolvere le collisioni di posizione;
- la `Merkle Proof', cioè l'insieme dei nodi e degli hash utilizzati per ricostruire la radice dell'MPC e verificare che l'identificatore del contratto e il suo `Transition Bundle' siano impegnati nella radice.

Questo meccanismo è stato descritto nella sezione precedente sulla costruzione dell'albero *MPC*, dove ogni contratto ottiene una foglia unica grazie alla funzione :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Quindi, viene utilizzato uno schema di merkelizzazione deterministico per aggregare tutte le foglie (contratti + entropia). Alla fine, la `MPC Proof` permette di ricostruire localmente la radice e di confrontarla con la `mpc::Commitment` inclusa nella catena.

#### Prova di transazione extra - ETP

Il terzo campo, il **ETP**, dipende dal tipo di impegno utilizzato. Se l'impegno è di tipo `Opret`, non è richiesta alcuna prova aggiuntiva. Il validatore ispeziona il primo output `OP_RETURN` della transazione e trova il `mpc::Commitment` direttamente lì.

**Se l'impegno è di tipo `Tapret`**, deve essere fornita una prova aggiuntiva chiamata *Extra Transaction Proof - ETP*. Essa contiene :


- La chiave pubblica interna (`P`) dell'output taproot in cui è incorporato il *commitment*;
- I nodi partner dello `Script Path Spend` (quando il Tapret *commitment* è inserito in uno script), per dimostrare l'esatta posizione di questo script nell'albero delle radici:
 - Se il `Tapret` *impegno* è sul ramo destro, riveliamo il nodo sinistro (ad esempio `tHABC`),
 - Se l'*impegno* di `Tapret` è a sinistra, è necessario rivelare 2 nodi (ad esempio `tHAB` e `tHC`) per dimostrare che nessun altro *impegno* è presente sul lato destro.
- Il `nonce' può essere usato per "estrarre" la configurazione migliore, consentendo al *impegno* di essere collocato a destra dell'albero (ottimizzazione della prova).

Questa prova aggiuntiva è essenziale perché, a differenza di `Opret`, l'impegno di `Tapret` è integrato nella struttura di uno script taproot, che richiede la rivelazione di parte dell'albero taproot per validare correttamente la posizione dell'*impegno*.

![RGB-Bitcoin](assets/fr/045.webp)

Gli **Anchors** incapsulano quindi tutte le informazioni necessarie per convalidare un impegno Bitcoin nel contesto di RGB. Indicano sia la transazione pertinente (`Txid`) che la prova del posizionamento del contratto (`MPC Proof`), mentre gestiscono la prova aggiuntiva (`ETP`) nel caso di `Tapret`. In questo modo, un Anchor protegge l'integrità e l'unicità dello stato fuori catena, garantendo che la stessa transazione non possa essere reinterpretata per altri dati contrattuali.

### Conclusione

In questo capitolo vengono trattati i temi :


- Come applicare il concetto di Single-use Seals in Bitcoin (in particolare tramite un _outpoint_);
- I vari metodi per inserire deterministicamente un _commitment_ in una transazione (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- I motivi per cui RGB si concentra sugli impegni di Tapret ;
- Gestione di più contratti tramite _impegni multiprotocollo_, essenziale se non si vuole esporre un intero stato o altri contratti quando si vuole dimostrare un punto specifico;
- Abbiamo anche visto il ruolo degli _Anchors_, che riuniscono tutto (TXID della transazione, prova dell'albero di Merkle e prova di Taproot) in un unico pacchetto.

In pratica, l'implementazione tecnica è divisa tra diverse _crate_ Rust dedicate (in _client_side_validation_, _commit-verify_, _bp_core_, ecc.) Le nozioni fondamentali ci sono:

![RGB-Bitcoin](assets/fr/046.webp)

Nel prossimo capitolo, esamineremo la componente puramente off-chain di RGB, ovvero la logica dei contratti. Vedremo come i contratti RGB, organizzati come _macchine a stati finiti_ parzialmente replicate, raggiungano un'espressività molto più elevata rispetto agli script Bitcoin, preservando al contempo la riservatezza dei loro dati.

## Introduzione ai contratti intelligenti e ai loro stati

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

In questo e nel prossimo capitolo, esamineremo la nozione di **contratto intelligente** all'interno dell'ambiente RGB ed esploreremo i diversi modi in cui questi contratti possono definire ed evolvere il loro *stato*. Vedremo perché l'architettura RGB, utilizzando la sequenza ordinata di Single-use Seals, rende possibile l'esecuzione di vari tipi di ***operazioni contrattuali*** in modo scalabile e senza passare attraverso un registro centralizzato. Vedremo anche il ruolo fondamentale della ***Logica di business*** nell'inquadrare l'evoluzione dello stato del contratto.

### Contratti intelligenti e diritti digitali al portatore

L'obiettivo di RGB è fornire un'infrastruttura per l'implementazione di contratti intelligenti su Bitcoin. Per "contratto intelligente" si intende un accordo tra più parti che viene applicato automaticamente e computazionalmente, senza l'intervento umano per far rispettare le clausole. In altre parole, la legge del contratto è applicata dal software, non da una terza parte fidata.

Questa automazione solleva la questione della decentralizzazione: come possiamo liberarci da un registro centralizzato (ad esempio una piattaforma o un database centrale) per gestire la proprietà e l'esecuzione dei contratti? L'idea originale, ripresa da RGB, è quella di tornare a una modalità di proprietà nota come "strumenti al portatore". Storicamente, alcuni titoli (obbligazioni, azioni, ecc.) venivano emessi al portatore, consentendo a chiunque possedesse fisicamente il documento di far valere i propri diritti.

![RGB-Bitcoin](assets/fr/055.webp)

RGB applica questo concetto al mondo digitale: i diritti (e gli obblighi) sono incapsulati in dati che vengono manipolati fuori dalla catena, e lo stato di questi dati è convalidato dagli stessi partecipanti. Ciò consente, a priori, un grado di riservatezza e di indipendenza molto maggiore di quello offerto da altri approcci basati su registri pubblici.

### Introduzione al contratto intelligente Stato RGB

Uno smart contract in RGB può essere visto come una macchina a stati, definita da :


- Uno **Stato**, cioè l'insieme delle informazioni che riflettono la configurazione attuale del contratto;
- Una **Business Logic** (insieme di regole), che descrive in quali condizioni e da chi può essere modificato lo stato.

![RGB-Bitcoin](assets/fr/056.webp)

È importante capire che questi contratti non si limitano al semplice trasferimento di token. Essi possono incorporare un'ampia varietà di applicazioni: dai beni tradizionali (token, azioni, obbligazioni) a meccaniche più complesse (diritti d'uso, termini commerciali, ecc.). A differenza di altre blockchain, dove il codice del contratto è accessibile ed eseguibile da tutti, l'approccio di RGB compartimenta l'accesso e la conoscenza del contratto ai partecipanti ("***partecipanti al contratto***"). Esistono diversi ruoli:


- L'emittente** o creatore del contratto, che definisce la Genesi del contratto e le sue variabili iniziali;
- Parti con diritti** (*proprietà*) o altre capacità di esecuzione ;
- Osservatori**, potenzialmente limitati a vedere determinate informazioni, ma che non possono attivare modifiche.

Questa separazione dei ruoli contribuisce alla resistenza alla censura, garantendo che solo le persone autorizzate possano interagire con lo stato contrattuale. Inoltre, dà a RGB la capacità di scalare orizzontalmente: la maggior parte delle convalide avviene al di fuori della blockchain e solo le ancore crittografiche (gli *impegni*) sono iscritte su Bitcoin.

### Stato e logica aziendale in RGB

Da un punto di vista pratico, la **Business Logic** del contratto assume la forma di regole e script, definiti in quello che RGB chiama uno **Schema**. Lo Schema codifica :


- Struttura dello Stato (quali campi sono pubblici? Quali campi sono di proprietà di quali parti?
- Condizioni di validità (cosa deve essere controllato prima di autorizzare un aggiornamento di stato?) ;
- Autorizzazioni (chi può avviare una *Transizione di Stato*? Chi può solo osservare?).

Allo stesso tempo, lo **Stato contrattuale** spesso si scompone in due componenti:


- Uno **Stato globale**: parte pubblica, potenzialmente osservabile da tutti (a seconda della configurazione);
- Stati di proprietà**: parti private, assegnate specificamente ai proprietari tramite gli UTXO a cui si fa riferimento nella logica del contratto.

Come vedremo nei capitoli successivi, ogni aggiornamento di stato (*Operazione di contratto*) deve agganciarsi a un _commitment_ di Bitcoin (tramite `Opret` o `Tapret`) e rispettare gli script di *Business Logic* per essere considerato valido.

### Operazioni contrattuali: creazione ed evoluzione dello Stato

Nell'universo RGB, una ***Operazione di contratto*** è un qualsiasi evento che cambia il contratto da un **vecchio stato** a un **nuovo stato**. Queste operazioni seguono la seguente logica:


- Prendiamo atto dello stato attuale del contratto;
- Applichiamo la regola o l'operazione (una ***Transizione di stato***, una ***Genesi*** se è il primo stato, o una ***Estensione di stato*** se c'è una *valenza* pubblica da riattivare);
- Ancoriamo la modifica tramite un nuovo _commitment_ sulla blockchain, chiudendo un _single-use seal_ e creandone un altro;
- I titolari dei diritti interessati convalidano localmente (*lato cliente*) che la transizione è conforme allo *Schema* e che la transazione Bitcoin associata è registrata sulla catena.

![RGB-Bitcoin](assets/fr/057.webp)

Il risultato finale è un contratto aggiornato, ora con uno stato diverso. Questa transizione non richiede che l'intera rete Bitcoin si occupi dei dettagli, poiché solo una piccola impronta crittografica (il _commitment_) viene registrata nella blockchain. La sequenza di sigilli monouso impedisce qualsiasi doppio utilizzo dello Stato.

### Catena operativa: dalla Genesi allo Stato terminale

Per mettere le cose in prospettiva, uno smart contract RGB inizia con una **Genesi**, il primo stato. Successivamente, si susseguono varie operazioni contrattuali, formando un DAG (*grafo aciclico diretto*) di operazioni:


- Ogni transizione si basa su uno stato precedente (o più stati, nel caso di transizioni convergenti);
- L'ordine cronologico è garantito dall'inclusione di ogni transizione in un'ancora Bitcoin, marcata temporalmente e inalterabile grazie al consenso tramite Proof-of-Work;
- Quando non ci sono più operazioni in corso, si raggiunge lo **Stato finale**: lo stato più recente e completo del contratto.

![RGB-Bitcoin](assets/fr/012.webp)

Questa topologia DAG (invece di una semplice catena lineare) riflette la possibilità che diverse parti del contratto si evolvano in parallelo, purché non si contraddicano a vicenda. RGB si occupa quindi di evitare qualsiasi incoerenza attraverso la verifica *sul lato cliente* di ogni partecipante coinvolto.

### Sintesi

I contratti intelligenti in RGB introducono un modello di strumenti digitali al portatore, decentralizzati ma ancorati a Bitcoin per la marcatura temporale e la garanzia dell'ordine delle transazioni. L'esecuzione automatica di questi contratti si basa su :


- Uno **Stato del contratto*, che indica la configurazione attuale del contratto (diritti, saldi, variabili, ecc.);
- Una **Business Logic** (*Schema*), che definisce quali transizioni sono consentite e come devono essere convalidate;
- Contract Operations**, che aggiornano questo stato passo dopo passo, grazie agli impegni ancorati alle transazioni Bitcoin.

Nel prossimo capitolo approfondiremo la rappresentazione concreta di questi ***stati*** e ***transizioni di stato*** a livello off-chain e il loro rapporto con gli UTXO e i Single-use Seals incorporati in Bitcoin. Sarà l'occasione per vedere come la meccanica interna di RGB, basata sulla convalida lato client, riesca a mantenere la coerenza dei contratti intelligenti preservando la riservatezza dei dati.

## Operazioni di contratto RGB

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

In questo capitolo vedremo come funzionano le operazioni negli smart contract e le transizioni di stato, sempre nell'ambito del protocollo RGB. Lo scopo sarà anche quello di capire come più partecipanti cooperano per trasferire la proprietà di un bene.

### Transizioni di stato e loro meccanica

Il principio generale è ancora quello della convalida lato client, in cui i dati di stato sono detenuti dal proprietario e convalidati dal destinatario. Tuttavia, la specificità di RGB sta nel fatto che Bob, in qualità di destinatario, chiede ad Alice di incorporare alcune informazioni nei dati del contratto per avere un controllo reale sul bene ricevuto, tramite un riferimento nascosto a uno dei suoi UTXO.

Per illustrare il processo di una *Transizione di stato* (che è una delle ***Operazioni contrattuali*** fondamentali in RGB), facciamo un esempio passo passo di un trasferimento di beni tra Alice e Bob:

**Situazione iniziale:**

Alice ha uno ***stash RGB*** di dati convalidati localmente (*lato cliente*). Questo stash si riferisce a uno dei suoi UTXO su Bitcoin. Ciò significa che una _definizione di sigillo_ in questi dati punta a un UTXO appartenente ad Alice. L'idea è di consentirle di trasferire a Bob alcuni diritti digitali legati a un bene (ad esempio, i token RGB).

![RGB-Bitcoin](assets/fr/058.webp)

**Bob ha anche gli UTXO :**

Bob, invece, ha almeno un proprio UTXO, senza alcun legame diretto con quello di Alice. Nel caso in cui Bob non abbia un UTXO, è comunque possibile effettuare il trasferimento a lui utilizzando la stessa *transazione di testimonianza*: l'output di questa transazione includerà quindi l'impegno (_commitment_) e assocerà implicitamente la proprietà del nuovo contratto a Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Costruzione della nuova proprietà (*Nuovo Stato*) :**

Bob invia ad Alice informazioni codificate sotto forma di ***fattura*** (approfondiremo la costruzione delle fatture nei capitoli successivi), chiedendole di creare un nuovo stato conforme alle regole del contratto. Questo stato includerà una nuova *definizione di sigillo* che punta a uno degli UTXO di Bob. In questo modo, Bob ottiene la proprietà delle attività definite in questo nuovo stato, ad esempio una certa quantità di gettoni RGB.

![RGB-Bitcoin](assets/fr/060.webp)

**Preparazione della transazione campione:**

Alice crea quindi una transazione Bitcoin spendendo l'UTXO a cui si è fatto riferimento nel sigillo precedente (quello che l'ha legittimata come titolare). Nell'output di questa transazione, viene inserito un *impegno* (tramite `Opret` o `Tapret`) per ancorare il nuovo stato RGB. Gli impegni `Opret` o `Tapret` sono derivati da un *albero MPC* (come visto nei capitoli precedenti), che può aggregare diverse transizioni da contratti diversi.

**Trasmissione di *Consegna* a Bob:**

Prima di trasmettere la transazione, Alice invia a Bob un ***Consignment*** contenente tutti i dati necessari *sul lato cliente* (il suo *stash*) e le nuove informazioni sullo stato a favore di Bob. A questo punto, Bob applica le regole di consenso RGB:


- Convalida tutti i dati RGB contenuti nella *Consegna*, compreso il nuovo stato che gli conferisce la proprietà del bene;
- Basandosi sugli *Anchors* inclusi nella *Consegna*, verifica la cronologia delle transazioni dei testimoni (dalla Genesi alla transizione più recente) e convalida gli impegni corrispondenti nella blockchain.

**Completamento della transizione:**

Se Bob è soddisfatto, può dare la sua approvazione (ad esempio, firmando l'*incarico*). Alice può quindi trasmettere la transazione campione preparata. Una volta confermata, questa chiude il sigillo precedentemente detenuto da Alice e formalizza la proprietà da parte di Bob. La sicurezza anti-doppio spreco si basa sullo stesso meccanismo di Bitcoin: l'UTXO viene speso, dimostrando che Alice non può più riutilizzarlo.

![RGB-Bitcoin](assets/fr/061.webp)

Il nuovo stato fa ora riferimento all'UTXO di Bob, conferendo a Bob la proprietà precedentemente detenuta da Alice. L'uscita Bitcoin in cui sono ancorati i dati RGB diventa la prova irrevocabile del trasferimento di proprietà.

Un esempio di DAG (*grafo aciclico diretto*) minimo che comprende due operazioni contrattuali (una **Genesi** e una ***Transizione di stato***) può illustrare come lo stato RGB (strato *lato cliente*, in rosso) si connette alla blockchain Bitcoin (strato *Commitment*, in arancione).

![RGB-Bitcoin](assets/fr/062.webp)

Mostra che una Genesi definisce un sigillo (*definizione del sigillo*), quindi una *Transizione di stato* chiude questo sigillo per crearne uno nuovo in un altro UTXO.

In questo contesto, ecco alcuni richiami alla terminologia:


- Un ***Assignment*** combina :
    - Una ***Definizione di tenuta*** (che punta a un UTXO);
    - Stati di proprietà**, ovvero i dati legati alla proprietà (ad esempio, la quantità di gettoni trasferiti).
- Uno **Stato globale** riunisce le proprietà generali del contratto, visibili a tutti, e garantisce la coerenza globale delle evoluzioni.

Le transizioni di stato**, descritte nel capitolo precedente, sono la forma principale di operazione contrattuale. Fanno riferimento a uno o più stati precedenti (da Genesis o da un'altra transizione di stato) e li aggiornano a un nuovo stato.

![RGB-Bitcoin](assets/fr/063.webp)

Questo diagramma mostra come, in un *Bundle di transizione di stato*, diversi sigilli possano essere chiusi in una singola transazione campione, aprendo contemporaneamente nuovi sigilli. In effetti, una caratteristica interessante del protocollo RGB è la sua capacità di scalare: diverse transizioni possono essere aggregate in un Transition Bundle, ogni aggregazione è associata a una foglia distinta dell'albero *MPC* (un identificatore unico del bundle). Grazie al meccanismo *Deterministic Bitcoin Commitment* (DBC), l'intero messaggio viene inserito in un'uscita `Tapret` o `Opret`, chiudendo i sigilli precedenti ed eventualmente definendone di nuovi. L'`Anchor* funge da collegamento diretto tra l'impegno memorizzato nella blockchain e la struttura di validazione lato client (*client-side*).

Nei capitoli seguenti verranno esaminati tutti i componenti e i processi coinvolti nella costruzione e nella convalida di una transizione di stato. La maggior parte di questi elementi fa parte del consenso RGB, implementato nella **RGB Core Library**.

### Pacchetto di transizione

Su RGB è possibile raggruppare diverse transizioni di stato appartenenti allo stesso contratto (cioè che condividono lo stesso **ContractId**, derivato dal **OpId** di Genesis). Nel caso più semplice, come quello tra Alice e Bob nell'esempio precedente, un **Bundle di transizioni** contiene una sola transizione. Ma il supporto per le operazioni multi-pagatore (come coinjoin, aperture di canali Lightning, ecc.) significa che più utenti possono combinare le loro transizioni di stato in un unico bundle.

Una volta raccolte, queste transizioni sono ancorate (dal meccanismo MPC + DBC) in una singola transazione Bitcoin:


- Ogni transizione di stato viene sottoposta a hash e raggruppata in un fascio di transizioni;
- Il bundle di transizione è a sua volta sottoposto a hashing e inserito nella foglia dell'albero MPC corrispondente a questo contratto (un BundleId);
- L'albero MPC viene infine impegnato tramite `Opret` o `Tapret` nella transazione testimone, che chiude i sigilli consumati e definisce i nuovi sigilli.

Tecnicamente, il **BundleId** inserito nel foglio MPC è ottenuto da un hash taggato applicato alla serializzazione rigorosa del campo *InputMap* del bundle:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

In cui `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` per esempio.

La *InputMap* è una struttura dati che elenca, per ogni ingresso `i` della transazione campione, il riferimento all'*OpId* della transizione di stato corrispondente. Ad esempio:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` è il numero totale di voci della transazione che fanno riferimento a un `OpId`;
- opId(input_j)` è l'identificatore di operazione di una delle transizioni di stato presenti nel pacchetto.

Facendo riferimento a ogni voce una sola volta e in modo ordinato, si evita che lo stesso sigillo venga speso due volte in due transizioni di stato simultanee.

### Generazione dello stato e stato attivo

Le transizioni di stato possono quindi essere utilizzate per trasferire la proprietà di un bene da una persona a un'altra. Tuttavia, non sono le uniche operazioni possibili nel protocollo RGB. Il protocollo definisce tre **operazioni di contratto** :


- Transizione di stato** ;
- Genesi** ;
- Estensione statale**.

Tra queste, **Genesis** e **State Extension** sono talvolta chiamate "operazioni di generazione di stati*", perché creano nuovi stati senza chiuderne immediatamente alcuno. Questo è un punto molto importante: **Genesi** e **Estensione dello stato** non comportano la chiusura di un sigillo. Piuttosto, definiscono un nuovo sigillo, che deve poi essere speso da una successiva **Transizione di Stato** per essere veramente convalidato nella storia della blockchain.

![RGB-Bitcoin](assets/fr/064.webp)

Lo **Stato attivo** di un contratto è spesso definito come l'insieme degli ultimi stati risultanti dalla storia (il DAG) delle transazioni, a partire dalla Genesi e seguendo tutte le ancore nella blockchain Bitcoin. I vecchi stati che sono già obsoleti (cioè legati a UTXO esauriti) non sono più considerati attivi, ma rimangono essenziali per controllare la coerenza della storia.

### Genesi

La Genesi è il punto di partenza di ogni contratto RGB. Viene creata dall'emittente del contratto e definisce i parametri iniziali, in conformità con lo **Schema**. Nel caso di un token RGB, la Genesi può specificare, ad esempio :


- Il numero di gettoni creati originariamente e i loro proprietari;
- Massimale di emissione totale possibile ;
- Eventuali regole per la riemissione e i partecipanti ammissibili.

Essendo la prima transazione del contratto, la Genesis non fa riferimento a nessuno stato precedente, né chiude alcun sigillo. Tuttavia, per apparire nella cronologia ed essere convalidata, la Genesis deve essere **consumata** (chiusa) da una prima transizione di stato (spesso una transazione di scansione/autospesa verso l'emittente stesso, o la distribuzione iniziale agli utenti).

### Estensione dello Stato

Le Estensioni di Stato** offrono una funzionalità originale per gli smart contract. Esse consentono di riscattare alcuni diritti digitali (*Valenze*) previsti nella definizione del contratto, senza chiudere immediatamente il sigillo. Il più delle volte si tratta di :


- Problemi di token distribuiti;
- Meccanismi di asset swap ;
- Riedizioni condizionate (che possono includere la distruzione di altri beni, ecc.).

Tecnicamente, un'Estensione di Stato fa riferimento a una *Redenzione* (un particolare tipo di input RGB) che corrisponde a una *Valenza* definita in precedenza (ad esempio, in Genesi o in un'altra Transizione di Stato). Definisce un nuovo sigillo, disponibile per la persona o la condizione che ne beneficia. Perché questo sigillo diventi effettivo, deve essere speso da una successiva Transizione di Stato.

![RGB-Bitcoin](assets/fr/065.webp)

Ad esempio: la Genesi crea un diritto di emissione (*Valenza*). Questo può essere esercitato da un attore autorizzato, che poi costruisce un'Estensione di Stato:


- Si riferisce alla Valenza (riscatto);
- Crea una nuova *assegnazione* (nuovi dati di *Stato di proprietà*) che punta a un UTXO ;
- Una futura transizione di Stato, emessa dal proprietario di questo nuovo UTXO, trasferirà o distribuirà effettivamente i gettoni appena emessi.

### Componenti di un'operazione contrattuale

Vorrei ora dare un'occhiata dettagliata a ciascuno degli elementi costitutivi di una **Operazione contrattuale** in RGB. Una Contract Operation è l'azione che modifica lo stato di un contratto e che viene convalidata sul lato client, in modo deterministico, dal legittimo destinatario. In particolare, vedremo come la Contract Operation tenga conto, da un lato, del **vecchio stato** (*Old State*) del contratto e, dall'altro, della definizione di un **nuovo stato** (*New State*).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Se osserviamo il diagramma precedente, possiamo notare che un'operazione di contratto include elementi che si riferiscono al **nuovo stato** e altri che si riferiscono al **vecchio stato** aggiornato.

Gli elementi del **Nuovo Stato** sono :


- Assegnazioni**, in cui sono definiti :
 - La **definizione della guarnizione**;
 - Lo **Stato di proprietà**.
- Lo **Stato globale**, che può essere modificato o arricchito ;
- Valenze**, eventualmente definite in una transizione di stato o in una genesi.

Il **vecchio Stato** è referenziato tramite :


- Ingressi**, che puntano a *assegnazioni* di transizioni di stato precedenti (non presenti in Genesis);
- Riscatti**, che si riferiscono a valenze definite in precedenza (solo nelle estensioni di Stato).

Inoltre, un'Operazione a contratto include campi più generali specifici per l'operazione:


- ffv` (*Versione di avanzamento rapido*): numero intero a 2 byte che indica la versione del contratto;
- transitionType` o ExtensionType`: numero intero a 16 bit che specifica il tipo di transizione o di estensione, in base alla logica aziendale;
- `ContractId`: numero a 32 byte che si riferisce all'*OpId* del contratto Genesis. Incluso in Transizioni ed Estensioni, ma non in Genesis ;
- schemaId: presente solo in Genesis, è un hash di 32 byte che rappresenta la struttura (*Schema*) del contratto;
- testnet`: Booleano che indica se si è sulla rete Testnet o Mainnet. Solo Genesis;
- altlayers1`: variabile che identifica il livello alternativo (sidechain o altro) usato per ancorare i dati oltre a Bitcoin. Presente solo in Genesis ;
- metadata": campo che può memorizzare informazioni temporanee, utili per convalidare un contratto complesso, ma che non devono essere registrate nella cronologia dello stato finale.

Infine, tutti questi campi sono condensati da un processo di hashing personalizzato, per produrre un'impronta digitale unica, l'`OpId`. Questo `OpId` viene quindi integrato nel bundle di transizione, consentendone l'autenticazione e la convalida all'interno del protocollo.

Ogni *operazione contrattuale* è quindi identificata da un hash di 32 byte denominato `OpId`. Questo hash è calcolato mediante un hash SHA256 di tutti gli elementi che compongono l'operazione. In altre parole, ogni *Operazione contrattuale* ha un proprio impegno crittografico, che include tutti i dati necessari per verificare l'autenticità e la coerenza dell'operazione.

Un contratto RGB è quindi identificato da un `ContractId`, derivato dall'`OpId` di Genesis (poiché non esiste un'operazione precedente a Genesis). In concreto, prendiamo l'`OpId` di Genesis, invertiamo l'ordine dei byte e applichiamo una codifica Base58. Questa codifica rende il `ContractId` più facile da gestire e riconoscere.

### Metodi e regole di aggiornamento dello stato

Lo **Stato del contratto** rappresenta l'insieme di informazioni che il protocollo RGB deve tracciare per un determinato contratto. È composto da :


- Un singolo Stato globale**: è la parte pubblica e globale del contratto, visibile a tutti;
- Uno o più Stati di proprietà**: ogni Stato di proprietà è associato a un sigillo unico (e quindi a un UTXO su Bitcoin). Si distingue tra :
    - Gli Stati **pubblici**,
    - Gli Stati **privati**.

![RGB-Bitcoin](assets/fr/066.webp)

Lo *Stato globale* è direttamente incluso nell'*Operazione contratto* come blocco singolo. Gli *Stati proprietari* sono definiti in ogni *Assegnazione*, insieme alla *Definizione di tenuta*.

Una caratteristica importante di RGB è il modo in cui vengono modificati lo Stato globale e gli Stati posseduti. Esistono generalmente due tipi di comportamento:


- Mutevole**: quando un elemento di stato è descritto come mutabile, ogni nuova operazione sostituisce lo stato precedente con un nuovo stato. I vecchi dati vengono quindi considerati obsoleti;
- Accumulante**: quando un elemento di stato è definito come accumulante, ogni nuova operazione aggiunge nuove informazioni allo stato precedente, senza sovrascriverle. Il risultato è una sorta di storia accumulata.

Se nel contratto un elemento di stato non è definito come mutabile o cumulativo, questo elemento rimarrà vuoto per le operazioni successive (in altre parole, non ci saranno nuove versioni per questo campo). È lo Schema del contratto (cioè la logica aziendale codificata) a determinare se uno stato (Globale o di proprietà) è mutabile, cumulativo o fisso. Una volta definita la Genesi, queste proprietà possono essere modificate solo se il contratto stesso lo consente, ad esempio tramite una specifica Estensione di Stato.

La tabella seguente illustra come ogni tipo di operazione contrattuale può manipolare (o meno) lo Stato globale e lo Stato proprietario:

| Genesi | Estensione dello stato | Transizione dello stato

| ---------------------------- | :-----: | :-------------: | :--------------: |

| Aggiungere lo stato globale**

| n/a | - | + | **Mutazione dello Stato Globale** | - | + |

| **Aggiungi uno Stato di proprietà** | + | - | + |

**Mutazione dello stato di proprietà** | n/a | No | + |

**Aggiungi valenze** | + | + | + | + | +

**`+`** : azione possibile se lo Schema del contratto lo consente.

**`-`**: l'operazione deve essere confermata da una successiva transizione di stato (la sola estensione di stato non chiude il sigillo monouso).

Inoltre, l'ambito temporale e i diritti di aggiornamento di ciascun tipo di dati possono essere distinti nella tabella seguente:

| Metadati | Stato globale | Stato di proprietà

| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |

| Definito per una singola Operazione di contratto | Definito globalmente per il contratto | Definito per ogni sigillo (*Assegnazione*) | Definito per una singola Operazione di contratto | Definito globalmente per il contratto | Definito per ogni sigillo (*Assegnazione*) | Definito per ogni sigillo (*Assegnazione*) | Definito per ogni contratto

| Non realizzabile (dati effimeri) | Transazione emessa da attori (emittente, ecc.) | Dipende dal legittimo titolare del sigillo (colui che può spenderlo in una transazione successiva) |

| Lo stato è definito prima dell'operazione (dalla *Seal Definition* dell'operazione precedente) | Lo stato è stabilito al termine dell'operazione | Lo stato è stabilito al termine dell'operazione | Lo stato è definito prima dell'operazione (dalla *Seal Definition* dell'operazione precedente) | Lo stato è stabilito al termine dell'operazione | Lo stato è definito prima dell'operazione (dalla *Seal Definition* dell'operazione precedente)

### Stato globale

Lo Stato globale è spesso descritto come "nessuno possiede, tutti sanno". Contiene informazioni generali sul contratto, che sono pubblicamente visibili. Ad esempio, in un contratto di emissione di token, contiene potenzialmente :


- Il ticker (abbreviazione simbolica del token): `ticker` ;
- Il nome completo del token: `nome` ;
- Precisione (numero di cifre decimali): `precisione` ;
- Offerta iniziale (e/o limite massimo di token): `emessoSupporto` ;
- Data di emissione: `creato` ;
- Dati legali o altre informazioni pubbliche: `data`.

Questo Stato globale può essere collocato su risorse pubbliche (siti web, IPFS, Nostr, Torrent, ecc.) e distribuito alla comunità. Inoltre, l'incentivo economico (la necessità di detenere e trasferire questi token, ecc.) spinge naturalmente gli utenti del contratto a mantenere e propagare questi dati da soli.

### Incarichi

L'*Assegnazione* è la struttura di base per la definizione di :


- Il sigillo (*Definizione di sigillo*), che punta a un UTXO specifico;
- Lo *Stato di proprietà*, cioè la proprietà o i dati associati a questo sigillo.

Un *Assignment* può essere visto come l'analogo di un output di una transazione Bitcoin, ma con maggiore flessibilità. Qui sta la logica del trasferimento di proprietà: l'*Assegnazione* associa un particolare tipo di bene o diritto (`AssignmentType`) a un sigillo. Chiunque possieda la chiave privata dell'UTXO collegato a questo sigillo (o chiunque possa spendere questo UTXO) è considerato proprietario di questo *Stato posseduto*.

Uno dei grandi punti di forza di RGB è la possibilità di rivelare (*rivelare*) o nascondere (*nascondere*) i campi *Definizione del sigillo* e *Stato di proprietà* a piacimento. Ciò offre una potente combinazione di riservatezza e selettività. Ad esempio, è possibile dimostrare che una transizione è valida senza rivelare tutti i dati, fornendo la versione rivelata alla persona che deve convalidarla, mentre i terzi vedono solo la versione nascosta (un hash). In pratica, l'`OpId' di una transizione è sempre calcolato a partire dai dati *nascosti*.

![RGB-Bitcoin](assets/fr/067.webp)

#### Definizione di sigillo

La *Definizione di Sigillo*, nella sua forma rivelata, ha quattro campi di base: `txptr`, `vout`, `blinding` e `method` :


- txptr**: è un riferimento a un UTXO su Bitcoin :
    - Nel caso di un **sigillo Genesis**, punta direttamente a un UTXO esistente (quello associato al Genesis);
    - Nel caso di un **Graph seal**, si può avere :
        - Un semplice `txid`, se punta a un UTXO specifico,
        - Oppure un `WitnessTx`, che designa un autoreferente: il sigillo punta alla transazione stessa. Questo è particolarmente utile quando non è disponibile un UTXO esterno, ad esempio nelle transazioni di apertura del canale Lightning, o se il destinatario non ha un UTXO.
- vout** : il numero di uscita della transazione indicata da `txptr`. Presente solo per un sigillo grafico standard (non per `WitnessTx`);
- blinding**: un numero casuale di 8 byte, per rafforzare la riservatezza e prevenire tentativi di forza bruta sull'identità dell'UTXO;
- metodo** : indica il metodo di ancoraggio utilizzato (`Tapret` o `Opret`).

La forma *concelta* della Seal Definition è un hash SHA256 (taggato) della concatenazione di questi 4 campi, con un tag specifico per RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Stati di proprietà

Il secondo componente di *Assegnazione* è lo Stato di proprietà. A differenza dello Stato globale, può esistere in forma pubblica o privata:


- Stato di proprietà pubblica**: tutti conoscono i dati associati al sigillo. Ad esempio, un'immagine pubblica;
- Stato privato**: i dati sono nascosti, noti solo al proprietario (e potenzialmente al validatore, se necessario). Ad esempio, il numero di token posseduti.

RGB definisce quattro possibili tipi di stato (*StateTypes*) per uno Stato di proprietà:


- Dichiarativo**: non contiene dati numerici, ma solo un diritto dichiarativo (ad esempio, il diritto di voto). Le forme nascoste e rivelate sono identiche;
- Fungibile**: rappresenta una quantità fungibile (come i gettoni). In forma rivelata, abbiamo `importo' e `marginatura'. In forma nascosta, abbiamo un singolo *impegno di Pedersen* che nasconde l'importo e l'accecamento;
- Strutturato**: memorizza dati strutturati (fino a 64 kB). In forma rivelata, è il blob di dati. In forma nascosta, è un hash etichettato di questo blob:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Con, ad esempio :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Allegati**: collega un file (audio, immagine, binario, ecc.) allo Stato posseduto, memorizzando l'hash del file `file_hash`, il tipo MIME `media type` e un sale crittografico `salt`. Il file stesso è ospitato altrove. In forma nascosta, è un hash etichettato con i tre dati precedenti:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Con, ad esempio :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Per riassumere, ecco i 4 possibili tipi di stato nella forma pubblica e nascosta:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

**Dichiarativo** | **Fungibile** | **Strutturato** | **Attaccati** |

| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |

| Nessuno | Numero intero a 64 bit firmato o non firmato | Qualsiasi tipo di dati rigorosi | Qualsiasi file |

| Tipo di informazione** | Nessuno | Firmato o non firmato | Tipi rigorosi | Tipo MIME |

| Pedersen commitment | Hashing con accecamento | Hashed file ID

| Limiti di dimensione** | N/A | 256 byte | Fino a 64 KB | Fino a ~ 500 Gb |

### Ingressi

Gli ingressi di una *Operazione contratto* si riferiscono agli *Assegnamenti* che vengono spesi in questa nuova operazione. Un ingresso indica :


- prevOpId` : l'identificatore (`OpId`) dell'operazione precedente in cui si trovava l'*assegnazione*;
- assignmentType` : il tipo di *Assignment* (ad esempio, `assetOwner` per un token) ;
- `Index`: l'indice dell'*assegnazione* nell'elenco associato al precedente `OpId`, determinato dopo un ordinamento lessicografico dei sigilli nascosti.

Gli ingressi non compaiono mai nella Genesi, poiché non esistono assegnazioni precedenti. Non compaiono nemmeno nelle Estensioni di stato (perché le Estensioni di stato non chiudono i sigilli, ma ridefiniscono nuovi sigilli in base alle Valenze).

Quando abbiamo Stati posseduti di tipo `Fungibile`, la logica di validazione (tramite lo script AluVM fornito nello Schema) controlla la consistenza delle somme: la somma dei token in entrata (*Ingressi*) deve essere uguale alla somma dei token in uscita (nei nuovi *Assegnamenti*).

### Metadati

Il campo **Metadata** può avere una dimensione massima di 64 KiB ed è utilizzato per includere dati temporanei utili per la convalida, ma non integrati nello stato permanente del contratto. Ad esempio, le variabili di calcolo intermedie per gli script complessi possono essere memorizzate qui. Questo spazio non è destinato a essere memorizzato nella cronologia globale, motivo per cui non rientra nell'ambito degli Stati posseduti o dello Stato globale.

### Valenze

Le valenze** sono un meccanismo originale del protocollo RGB. Si possono trovare in Genesi, Transizioni di Stato o Estensioni di Stato. Rappresentano diritti numerici che possono essere attivati da un'Estensione di Stato (tramite *Redenzioni*), quindi finalizzati da una successiva Transizione. Ogni Valenza è identificata da un `ValencyType` (16 bit). La sua semantica (diritto di riemissione, scambio di token, diritto di masterizzazione, ecc.) è definita nello Schema.

In concreto, potremmo immaginare una Genesi che definisca una valenza "diritto di riemissione". Un'Estensione di Stato la consumerà (*Redimissione*) se sono soddisfatte determinate condizioni, per introdurre una nuova quantità di gettoni. Poi, una Transizione di Stato emanata dal titolare del sigillo così creato può trasferire questi nuovi gettoni.

### Riscatta

I riscatti sono l'equivalente delle valenze per le assegnazioni. Compaiono solo nelle Estensioni di stato, poiché è qui che viene attivata una Valenza definita in precedenza. Un Riscatto è composto da due campi:


- `PrevOpId` : l'`OpId` dell'operazione in cui è stata specificata la Valenza;
- `ValencyType`: il tipo di Valenza che si desidera attivare (ogni `ValencyType` può essere utilizzato una sola volta dall'Estensione di Stato).

Esempio: un Riscatto può corrispondere a un'esecuzione di CoinSwap, a seconda di quanto è stato codificato nella Valenza.

### Caratteristiche di stato RGB

Ora analizzeremo alcune caratteristiche fondamentali dello stato in RGB. In particolare, esamineremo :


- Lo **Strict Type System**, che impone un'organizzazione precisa e tipizzata dei dati;
- L'importanza di separare la **validazione** dalla **proprietà** ;
- Il sistema di **evoluzione del consenso** in RGB, che include le nozioni di *fast-forward* e *push-back*.

Come sempre, si tenga presente che tutto ciò che ha a che fare con lo stato del contratto viene convalidato dal lato del cliente secondo le regole di consenso stabilite nel protocollo, il cui riferimento crittografico ultimo è ancorato alle transazioni Bitcoin.

#### Sistema di tipi rigoroso

RGB utilizza uno *Strict Type System* e una modalità di serializzazione deterministica (*Strict Encoding*). Questa organizzazione è pensata per garantire una perfetta riproducibilità e precisione nella definizione, nel trattamento e nella convalida dei dati contrattuali.

In molti ambienti di programmazione (JSON, YAML...), la struttura dei dati può essere flessibile, persino troppo permissiva. In RGB, invece, la struttura e i tipi di ogni campo sono definiti con vincoli espliciti. Ad esempio :


- Ogni variabile ha un tipo specifico (per esempio, un intero senza segno a 8 bit `u8`, o un intero firmato a 16 bit, ecc;)
- I tipi possono essere composti (tipi annidati). Ciò significa che è possibile definire un tipo basato su altri tipi (ad esempio, un tipo aggregato contenente un campo `u8`, un campo `bool`, ecc;)
- È possibile specificare anche le collezioni: liste (*list*), insiemi (*set*) o dizionari (*map*), con un ordine di progressione deterministico;
- Ogni campo è delimitato (*limite inferiore* / *limite superiore*). Imponiamo anche dei limiti al numero di elementi nelle collezioni (contenimento);
- I dati sono allineati ai byte e la serializzazione è rigorosamente definita e non ambigua.

Grazie a questo rigido protocollo di codifica :


- L'ordine dei campi è sempre lo stesso, indipendentemente dall'implementazione o dal linguaggio di programmazione utilizzato;
- Gli hash calcolati sullo stesso set di dati sono quindi riproducibili e identici (*impegni* strettamente deterministici);
- I limiti impediscono una crescita incontrollata delle dimensioni dei dati (ad esempio, un numero eccessivo di campi);
- Questa forma di codifica facilita la verifica crittografica, in quanto ogni partecipante sa esattamente come serializzare e fare l'hash dei dati.

In pratica, la struttura (*Schema*) e il codice risultante (*Interfaccia* e logica associata) vengono compilati. Si utilizza un linguaggio descrittivo per definire il contratto (tipi, campi, regole) e generare un formato binario rigoroso. Una volta compilato, il risultato è :


- Un *dispositivo di memoria* per ogni campo;
- Identificatori semantici (che indicano se la modifica del nome di una variabile ha un impatto sulla logica, anche se la struttura della memoria rimane la stessa).

Il sistema di tipi rigoroso consente anche un monitoraggio preciso delle modifiche: qualsiasi modifica alla struttura (anche un cambio di nome di campo) è rilevabile e può portare a una variazione dell'impronta complessiva.

Infine, ogni compilazione produce un'impronta digitale, un identificatore crittografico che attesta l'esatta versione del codice (dati, regole, validazione). Ad esempio, un identificatore della forma :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

In questo modo è possibile gestire il consenso o gli aggiornamenti delle implementazioni, garantendo al contempo una tracciabilità dettagliata delle versioni utilizzate nella rete.

Per evitare che lo stato di un contratto RGB diventi troppo complicato da convalidare sul lato client, una regola di consenso impone una dimensione massima di `2^16` byte (64 Kio) per qualsiasi dato coinvolto nei calcoli di convalida. Questo vale per ogni variabile o struttura: non più di 65536 byte, o l'equivalente in numeri (32768 interi a 16 bit, ecc.). Questo vale anche per le collezioni (liste, insiemi, mappe), che non possono superare i `2^16` elementi.

Questo limite garantisce :


- Controlla la dimensione massima dei dati da manipolare durante una transizione di stato;
- Compatibilità con la macchina virtuale (*AluVM*) utilizzata per eseguire gli script di convalida.

#### Il paradigma Convalida = Proprietà

Una delle principali innovazioni di RGB è la rigida separazione tra due concetti:


- Convalida**: verifica che una transizione di stato rispetti le regole del contratto (logica aziendale, storia, ecc.);
- La **proprietà** (proprietà, o controllo): il fatto di possedere il Bitcoin UTXO che consente di spendere (o chiudere) il sigillo monouso e quindi di effettuare la transizione di stato.

La convalida** avviene a livello dello stack software RGB (librerie, protocollo *impegni*, ecc.). Il suo ruolo è quello di garantire che le regole interne del contratto (importi, autorizzazioni, ecc.) siano rispettate. Anche gli osservatori o altri partecipanti possono convalidare la cronologia dei dati.

La proprietà**, invece, si basa interamente sulla sicurezza di Bitcoin. Possedere la chiave privata di un UTXO significa controllare la capacità di avviare una nuova transizione (chiusura del sigillo monouso). Quindi, anche se qualcuno può vedere o convalidare i dati, non può cambiare lo stato se non possiede l'UTXO in questione.

![RGB-Bitcoin](assets/fr/069.webp)

Questo approccio limita le classiche vulnerabilità riscontrate nelle blockchain più complesse (dove tutto il codice di uno smart contract è pubblico e modificabile da chiunque, cosa che a volte ha portato ad hackeraggi). Su RGB, un attaccante non può semplicemente interagire con lo stato della catena, poiché il diritto di agire sullo stato (*proprietà*) è protetto dal livello Bitcoin.

Inoltre, questo disaccoppiamento consente a RGB di integrarsi naturalmente con la rete Lightning. I canali Lightning possono essere utilizzati per coinvolgere e spostare le risorse RGB senza dover impegnare ogni volta gli *impegni* della catena. Nei capitoli successivi del corso esamineremo più da vicino l'integrazione di RGB con Lightning.

#### Sviluppi del consenso in RGB

Oltre al versioning semantico del codice, RGB include un sistema di evoluzione o aggiornamento delle regole di consenso di un contratto nel tempo. Esistono due forme principali di evoluzione:


- Avanti veloce**
- Push-back** (in francese)

Un avanzamento rapido si verifica quando una regola precedentemente non valida diventa valida. Ad esempio, se il contratto si evolve per consentire un nuovo tipo di `AssignmentType` o un nuovo campo :


- Questo non può essere paragonato a un classico hardfork della blockchain, in quanto RGB opera nella validazione lato client e non influisce sulla compatibilità complessiva della blockchain;
- In pratica, questo tipo di modifica è indicato dal campo `Ffv` (*versione veloce*) nell'operazione di contratto;
- Gli attuali titolari non subiscono alcun danno: il loro status rimane valido;
- I nuovi beneficiari (o nuovi utenti), invece, devono aggiornare il loro software (il loro portafoglio) per riconoscere le nuove regole.

Un push-back significa che una regola precedentemente valida diventa non valida. Si tratta quindi di un "indurimento" delle regole, ma non di un softfork in senso stretto:


- I titolari esistenti potrebbero subire un impatto (potrebbero ritrovarsi con beni resi obsoleti o non validi nella nuova versione);
- Possiamo considerare che stiamo creando un nuovo protocollo: chi adotta la nuova regola si allontana dalla vecchia;
- L'emittente potrebbe decidere di riemettere asset in questo nuovo protocollo, costringendo gli utenti a mantenere due portafogli separati (uno per il vecchio protocollo, l'altro per il nuovo), se vogliono gestire entrambe le versioni.

In questo capitolo sulle operazioni di contratto RGB, abbiamo esplorato i principi fondamentali alla base di questo protocollo. Come avrete notato, la complessità intrinseca del protocollo RGB richiede l'uso di molti termini tecnici. Nel prossimo capitolo, quindi, vi fornirò un glossario che riassumerà tutti i concetti trattati in questa prima parte teorica, con le definizioni di tutti i termini tecnici relativi a RGB. Poi, nella prossima sezione, daremo uno sguardo pratico alla definizione e all'implementazione dei contratti RGB.

## Glossario RGB

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Se avete bisogno di tornare a questo breve glossario di termini tecnici importanti utilizzati nel mondo RGB (elencati in ordine alfabetico), lo troverete utile. Questo capitolo non è essenziale se avete già compreso tutto ciò che abbiamo trattato nella prima sezione.

#### AluVM

L'abbreviazione AluVM sta per "_Algorithmic logic unit Virtual Machine_", una macchina virtuale basata su registri progettata per la convalida di contratti smart e per il calcolo distribuito. È utilizzata (ma non esclusivamente riservata) per la convalida dei contratti RGB. Gli script o le operazioni incluse in un contratto RGB possono quindi essere eseguiti nell'ambiente AluVM.

Per ulteriori informazioni: [Sito ufficiale di AluVM](https://www.aluvm.org/)

#### Ancora

Un Anchor rappresenta un insieme di dati lato client utilizzati per dimostrare l'inclusione di un unico _commitment_ in una transazione. Nel protocollo RGB, un Anchor è composto dai seguenti elementi:


- L'identificativo della transazione Bitcoin (TXID) della **transazione testimone** ;
- Il **Multi Protocol Commitment (MPC)** ;
- Il **Deterministic Bitcoin Commitment (DBC)**;
- La **Extra Transaction Proof (ETP)** se si utilizza il meccanismo di impegno **Tapret** (si veda la sezione dedicata a questo modello).

Un Anchor serve quindi a stabilire un legame verificabile tra una specifica transazione Bitcoin e i dati privati convalidati dal protocollo RGB. Garantisce che questi dati siano effettivamente inclusi nella blockchain, senza che il loro contenuto esatto sia esposto pubblicamente.

#### Assegnazione

Nella logica di RGB, un Assignment è l'equivalente di un output di transazione che modifica, aggiorna o crea determinate proprietà all'interno dello stato di un contratto. Un Assignment comprende due elementi:


- A **Definizione di tenuta** (riferimento a un UTXO specifico) ;
- Uno **Stato di proprietà** (dati che descrivono lo stato associato a questo nuovo proprietario).

Un'assegnazione indica quindi che una parte dello stato (ad esempio, un bene) è ora assegnata a un particolare titolare, identificato tramite un sigillo monouso collegato a un UTXO.

#### Logica aziendale

La Business Logic raggruppa tutte le regole e le operazioni interne di un contratto, descritte dal suo **schema** (cioè la struttura del contratto stesso). Stabilisce come può evolvere lo stato del contratto e in quali condizioni.

#### Convalida lato client

La convalida lato client si riferisce al processo con cui ogni parte (client) verifica un insieme di dati scambiati privatamente, secondo le regole di un protocollo. Nel caso di RGB, questi dati scambiati sono raggruppati in quelli che sono noti come **conferimenti**. A differenza del protocollo Bitcoin, che richiede la pubblicazione di tutte le transazioni sulla catena, RGB consente di memorizzare pubblicamente solo gli _impegni_ (ancorati in Bitcoin), mentre le informazioni essenziali del contratto (transizioni, attestazioni, prove) rimangono fuori dalla catena, condivise solo tra gli utenti interessati.

#### Impegno

Un impegno (in senso crittografico) è un oggetto matematico, indicato con `C`, derivato deterministicamente da un'operazione su dati strutturati `m` (il messaggio) e un valore casuale `r`. Scriviamo :

$$
C = \text{commit}(m, r)
$$

Questo meccanismo comprende due operazioni principali:


- Commit**: una funzione crittografica viene applicata a un messaggio `m` e a un numero casuale `r` per produrre `C` ;
- Verify**: si utilizza `C`, il messaggio `m` e il valore `r` per verificare che questo impegno sia corretto. La funzione restituisce `Vero` o `Falso`.

Un impegno deve rispettare due proprietà:


- Binding**: deve essere impossibile trovare due messaggi diversi che producano la stessa `C` :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Come ad esempio :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Nascondere**: la conoscenza di `C` non deve rivelare il contenuto di `m`.

Nel protocollo RGB, un impegno è incluso in una transazione Bitcoin per dimostrare l'esistenza di una certa informazione in un determinato momento, senza rivelare l'informazione stessa.

#### In conto vendita

Una **Consegna** raggruppa i dati scambiati tra le parti, soggetti a convalida lato cliente in RGB. Esistono due categorie principali di spedizioni:


- Contract Consignment**: fornito dall'*emittente* (contract issuer), include informazioni di inizializzazione quali Schema, Genesi, Interfaccia e Implementazione dell'interfaccia.
- Trasferimento di partita**: fornito dalla parte pagante (*pagatore*). Contiene l'intera cronologia delle transizioni di stato che portano alla consegna finale (cioè lo stato finale ricevuto dal pagatore).

Questi invii non vengono registrati pubblicamente sulla blockchain, ma vengono scambiati direttamente tra le parti interessate attraverso il canale di comunicazione di loro scelta.

#### Contratto

Un Contratto è un insieme di diritti eseguiti digitalmente tra diversi attori tramite il protocollo RGB. Ha uno stato attivo e una logica di business, definita da uno Schema, che specifica quali operazioni sono autorizzate (trasferimenti, estensioni, ecc.). Lo stato di un contratto, così come le sue regole di validità, sono espressi nello Schema. In qualsiasi momento, il contratto si evolve solo in base a quanto consentito da questo Schema e dagli script di validazione (eseguiti, ad esempio, in AluVM).

#### Operazione a contratto

Una Contract Operation è un aggiornamento dello stato del contratto eseguito secondo le regole di Schema. In RGB esistono le seguenti operazioni:


- Transizione di stato** ;
- Genesi** ;
- Estensione statale**.

Ogni operazione modifica lo stato aggiungendo o sostituendo alcuni dati (Stato globale, Stato di proprietà...).

#### Partecipante al contratto

Un partecipante al contratto è un attore che prende parte alle operazioni relative al contratto. In RGB si distingue tra :


- L'emittente del contratto, che crea la Genesi (l'origine del contratto);
- Le parti del contratto, cioè i titolari dei diritti sullo stato del contratto;
- Soggetti pubblici, che possono costruire estensioni statali se il contratto offre valenze accessibili al pubblico.

#### Diritti contrattuali

I diritti contrattuali si riferiscono ai vari diritti che possono essere esercitati dai soggetti coinvolti in un contratto RGB. Essi si dividono in diverse categorie:


- Diritti di proprietà**, associati alla proprietà di un particolare UTXO (tramite una _Seal Definition_);
- Diritti esecutivi**, cioè la capacità di costruire una o più transizioni (transizioni di stato) in conformità con lo Schema ;
- Diritti pubblici**, quando lo schema autorizza determinati usi pubblici, ad esempio la creazione di un'estensione dello Stato tramite il riscatto di una valenza.

#### Stato del contratto

Lo Stato del contratto corrisponde allo stato attuale di un contratto in un determinato momento. Può essere composto da dati pubblici e privati, che riflettono lo stato del contratto. RGB distingue tra :


- Lo **Stato globale**, che include le proprietà pubbliche del contratto (impostate in Genesis o aggiunte tramite aggiornamenti autorizzati);
- Stati di proprietà**, che appartengono a proprietari specifici, identificati dai loro UTXO.

#### Impegno deterministico di Bitcoin - DBC

Il Deterministic Bitcoin Commitment (DBC) è l'insieme di regole utilizzate per registrare in modo certo e univoco un _impegno_ in una transazione Bitcoin. Nel protocollo RGB, esistono due forme principali di DBC:


- Opret**
- Tapret**

Questi meccanismi definiscono con precisione il modo in cui l'impegno viene codificato nell'output o nella struttura di una transazione Bitcoin, per garantire che tale impegno sia deterministicamente tracciabile e verificabile.

#### Grafico aciclico diretto - DAG

Un DAG (o *grafo guidato aciclico*) è un grafo privo di cicli, che consente una programmazione topologica. Le blockchain, come gli _shard_ dei contratti RGB, possono essere rappresentate da DAG.

Per ulteriori informazioni: [Grafico Aciclico Diretto](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Incisione

L'incisione è una stringa di dati opzionale che i proprietari successivi di un contratto possono inserire nella cronologia del contratto. Questa funzione esiste, ad esempio, nell'interfaccia **RGB21** e consente di aggiungere informazioni commemorative o descrittive alla cronologia dei contratti.

#### Prova di transazione extra - ETP

L'ETP (*Extra Transaction Proof*) è la parte dell'Anchor che contiene i dati aggiuntivi necessari per convalidare un *impegno* di un **Tapret** (nel contesto di _taproot_). Include, tra l'altro, la chiave pubblica interna dello script taproot (_internal PubKey_) e informazioni specifiche del _Script Path Spend_.

#### Genesi

Genesis si riferisce all'insieme di dati, governati da uno Schema, che costituisce lo stato iniziale di qualsiasi contratto in RGB. Può essere paragonato al concetto di _Blocco Genesi_ di Bitcoin, o al concetto di transazione di Coinbase, ma qui a livello di _client-side_ e di token RGB.

#### Stato globale

Lo Stato globale è l'insieme delle proprietà pubbliche contenute nello Stato del contratto. È definito in Genesis e, a seconda delle regole del contratto, può essere aggiornato da transizioni autorizzate. A differenza degli Stati di proprietà, lo Stato globale non appartiene a un'entità particolare; è più vicino a un registro pubblico all'interno del contratto.

#### Interfaccia

L'interfaccia è l'insieme delle istruzioni utilizzate per decodificare i dati binari compilati in uno schema o nelle operazioni contrattuali e i loro stati, al fine di renderli leggibili per l'utente o il suo portafoglio. Agisce come un livello di interpretazione.

#### Implementazione dell'interfaccia

L'implementazione dell'interfaccia è l'insieme delle dichiarazioni che collegano una **interfaccia** a uno **schema**. Consente la traduzione semantica effettuata dall'Interfaccia stessa, in modo che i dati grezzi di un contratto possano essere compresi dall'utente o dal software coinvolto (i portafogli).

#### Fattura

Una fattura assume la forma di un URL codificato in [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), che incorpora i dati necessari per la costruzione di una **Transizione di Stato** (da parte del pagatore). In altre parole, è una fattura che consente alla controparte (*pagatore*) di creare la transizione corrispondente per trasferire il bene o aggiornare lo stato del contratto.

#### Rete di fulmini

La Lightning Network è una rete decentralizzata di canali di pagamento (o _state channels_) su Bitcoin, composta da 2/2 portafogli multi-firma. Consente transazioni _off-chain_ veloci e a basso costo, affidandosi al livello 1 di Bitcoin per l'arbitrato (o la chiusura) quando necessario.

Per maggiori informazioni sul funzionamento di Lightning, vi consiglio di seguire quest'altro corso:

https://planb.network/courses/lnp201
#### Impegno multiprotocollo - MPC

Multi Protocol Commitment (MPC) si riferisce alla struttura ad albero di Merkle utilizzata in RGB per includere, all'interno di una singola transazione Bitcoin, diversi **Transition Bundles** provenienti da contratti diversi. L'idea è quella di raggruppare diversi impegni (potenzialmente corrispondenti a diversi contratti o a diverse attività) in un unico punto di ancoraggio per ottimizzare l'occupazione dello spazio dei blocchi.

#### Stato di proprietà

Uno Stato di proprietà è la parte di uno Stato contrattuale racchiusa in un'assegnazione e associata a un particolare titolare (tramite un sigillo monouso che punta a un UTXO). Rappresenta, ad esempio, un bene digitale o uno specifico diritto contrattuale assegnato a quella persona.

#### Proprietà

La proprietà si riferisce alla capacità di controllare e spendere un UTXO a cui fa riferimento una Seal Definition. Quando uno Stato di proprietà è collegato a un UTXO, il proprietario di questo UTXO ha il diritto, potenzialmente, di trasferire o far evolvere lo Stato associato, secondo le regole del contratto.

#### Transazione Bitcoin parzialmente firmata - PSBT

Una PSBT (_Partially Signed Bitcoin Transaction_) è una transazione Bitcoin non ancora completamente firmata. Può essere condivisa tra diverse entità, ognuna delle quali può aggiungere o verificare alcuni elementi (firme, script...), finché la transazione non viene considerata pronta per la distribuzione sulla catena.

Per ulteriori informazioni: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Impegno di Pedersen

Un impegno Pedersen è un tipo di impegno crittografico con la proprietà di essere **omorfo** rispetto all'operazione di addizione. Ciò significa che è possibile convalidare la somma di due impegni senza rivelare i singoli valori.

Formalmente, se :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

allora :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Questa proprietà è utile, ad esempio, per nascondere le quantità di gettoni scambiati, pur potendo verificare i totali.

Ulteriori informazioni: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Riscatto

In un'Estensione di Stato, il Riscatto si riferisce all'azione di rivendicare (o sfruttare) una **Valenza** precedentemente dichiarata. Poiché una Valenza è un diritto pubblico, il Riscatto consente a un partecipante autorizzato di rivendicare una specifica estensione di stato del contratto.

#### Schema

Uno Schema in RGB è un pezzo di codice dichiarativo che descrive l'insieme di variabili, regole e logica aziendale (*Business Logic*) che regolano il funzionamento di un contratto. Lo schema definisce la struttura degli stati, i tipi di transizioni consentite e le condizioni di convalida.

#### Definizione di sigillo

La Definizione del sigillo è la parte di un'assegnazione che associa l'_impegno_ a un UTXO di proprietà del nuovo titolare. In altre parole, indica dove si trova la condizione (in quale UTXO) e stabilisce la proprietà di un bene o di un diritto.

#### Frammento

Uno Shard rappresenta un ramo nel DAG della storia delle transizioni di stato di un contratto RGB. In altre parole, è un sottoinsieme coerente della storia complessiva del contratto, corrispondente, ad esempio, alla sequenza di transizioni necessarie per dimostrare la validità di un determinato bene fin dalla _Genesi_.

#### Sigillo monouso

Un sigillo monouso è una promessa crittografica di impegno per un messaggio ancora sconosciuto, che sarà rivelato solo una volta in futuro e deve essere conosciuto da tutti i membri di un pubblico specifico. Lo scopo è quello di impedire la creazione di più impegni concorrenti per lo stesso sigillo.

#### Stash

Lo Stash è l'insieme dei dati lato client che un utente memorizza per uno o più contratti RGB, ai fini della convalida (*convalida lato client*). Comprende la cronologia delle transizioni, gli invii, le prove di validità, ecc. Ogni titolare conserva solo le parti dello storico di cui ha bisogno (*shard*).

#### Estensione dello Stato

Un'Estensione di Stato è un'operazione contrattuale utilizzata per riattivare gli aggiornamenti di stato riscattando le **Valenze** precedentemente dichiarate. Per essere efficace, una State Extension deve essere chiusa da una State Transition (che aggiorna lo stato finale del contratto).

#### Transizione di stato

La transizione di stato è l'operazione che cambia lo stato di un contratto RGB in un nuovo stato. Può modificare i dati dello Stato globale e/o dello Stato di proprietà. In pratica, ogni transizione è verificata dalle regole dello Schema e ancorata alla blockchain Bitcoin tramite un _commitment_.

#### Radice di fittone

Si riferisce al formato di transazione Segwit v1 di Bitcoin, introdotto da [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) e [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot migliora la riservatezza e la flessibilità degli script, in particolare rendendo le transazioni più compatte e più difficili da distinguere l'una dall'altra.

#### Spedizione terminale - Punto finale di spedizione

Il Terminal Consignment (o _Consignment Endpoint_) è un *trasferimento consignment* contenente lo stato finale del contratto, inclusa la State Transition creata dalla Fattura del destinatario (*pagatore*). È quindi il punto finale di un trasferimento, con i dati necessari a dimostrare che la proprietà o lo stato sono stati trasferiti.

#### Pacchetto di transizione

Un pacchetto di transizioni è un insieme di transizioni di stato RGB (appartenenti allo stesso contratto) che sono tutte impegnate nella stessa ***transazione di testimonianza*** Bitcoin. Ciò consente di raggruppare diversi aggiornamenti o trasferimenti in un'unica ancora sulla catena.

#### UTXO

Un Bitcoin UTXO (*Unspent Transaction Output*) è definito dall'hash di una transazione e dall'indice di uscita (*vout*). A volte viene anche chiamato _outpoint_. Nel protocollo RGB, il riferimento a un UTXO (tramite una **Seal Definition**) consente di individuare lo **Owned State**, ossia la proprietà detenuta sulla blockchain.

#### Valenza

Una Valenza è un diritto pubblico che non richiede la conservazione dello Stato in quanto tale, ma che può essere riscattato tramite una **Estensione di Stato**. Si tratta quindi di una forma di possibilità aperta a tutti (o a determinati giocatori), dichiarata nella logica del contratto, al fine di effettuare una particolare estensione in una data successiva.

#### Testimonianza di transazione

La transazione del testimone è la transazione Bitcoin che chiude il sigillo monouso attorno a un messaggio contenente un impegno multiprotocollo (MPC). Questa transazione spende un UTXO o ne crea uno, in modo da sigillare l'impegno legato al protocollo RGB. Agisce come prova sulla catena che lo stato è stato impostato in un momento specifico.

# Programmazione su RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Implementazione dei contratti RGB

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

In questo capitolo vedremo da vicino come viene definito e implementato un contratto RGB. Vedremo quali sono i componenti di un contratto RGB, quali sono i loro ruoli e come vengono costruiti.

### I componenti di un contratto RGB

Finora abbiamo già parlato della **Genesi**, che rappresenta il punto di partenza di un contratto, e abbiamo visto come si inserisce nella logica di una *Operazione di contratto* e nello stato del protocollo. La definizione completa di un contratto RGB, tuttavia, non si limita alla sola Genesi: coinvolge tre componenti complementari che, insieme, costituiscono il cuore dell'implementazione.

Il primo componente è chiamato **Schema**. Si tratta di un file che descrive la struttura fondamentale e la logica aziendale (*business logic*) del contratto. Specifica i tipi di dati utilizzati, le regole di convalida, le operazioni consentite (ad esempio, l'emissione iniziale di token, i trasferimenti, le condizioni speciali e così via) - in breve, il quadro generale che detta il funzionamento del contratto.

Il secondo componente è l'**interfaccia**. Si concentra sul modo in cui gli utenti (e, per estensione, il software del portafoglio) interagiranno con questo contratto. Descrive la semantica, cioè la rappresentazione leggibile dei vari campi e delle azioni. Quindi, mentre lo Schema definisce come funziona tecnicamente il contratto, l'Interfaccia definisce come presentare ed esporre queste funzionalità: nomi dei metodi, visualizzazione dei dati, ecc.

Il terzo componente è l'**Interface Implementation**, che completa i due precedenti agendo come una sorta di ponte tra lo Schema e l'Interfaccia. In altre parole, associa la semantica espressa dall'Interfaccia alle regole sottostanti definite nello Schema. È questa implementazione che gestirà, ad esempio, la conversione tra un parametro inserito nel portafoglio e la struttura binaria imposta dal protocollo, o la compilazione delle regole di validazione in linguaggio macchina.

Questa modularità è una caratteristica interessante di RGB, in quanto consente a diversi gruppi di sviluppatori di lavorare separatamente su questi aspetti (*Schema*, *Interfaccia*, *Implementazione*), purché seguano le regole di consenso del protocollo.

In sintesi, ogni contratto è composto da :


- Genesis**, che rappresenta lo stato iniziale del contratto (e può essere paragonato a una transazione speciale che definisce la prima proprietà di un bene, di un diritto o di qualsiasi altro dato parametrizzabile);
- Schema**, che descrive la logica di business del contratto (tipi di dati, regole di validazione, ecc.);
- Interfaccia**, che fornisce un livello semantico sia per i portafogli che per gli utenti umani, chiarendo la lettura e l'esecuzione delle transazioni;
- Interfaccia di implementazione**, che colma il divario tra la logica aziendale e la presentazione, per garantire che la definizione del contratto sia coerente con l'esperienza dell'utente.

![RGB-Bitcoin](assets/fr/070.webp)

È importante notare che affinché un portafoglio possa gestire un asset RGB (sia esso un token fungibile o un diritto di qualsiasi tipo), deve avere tutti questi elementi compilati: *Schema*, *Interfaccia*, *Implementazione dell'interfaccia* e *Genesi*. Il tutto viene trasmesso tramite un ***invio di contratto***, ovvero un pacchetto di dati contenente tutto ciò che serve per convalidare il contratto lato cliente.

Per chiarire queste nozioni, ecco una tabella riassuntiva che confronta i componenti di un contratto RGB con concetti già noti nella programmazione orientata agli oggetti (OOP) o nell'ecosistema Ethereum:

| Componente del Contratto RGB | Significato | Equivalente OOP | Equivalente Ethereum |

| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |

| Costruttore di classe | Costruttore di contratto | Stato iniziale del contratto

| Classe | Logica aziendale del contratto

| Semantica del contratto | Interfaccia (Java) / tratto (Rust) / protocollo (Swift) | Standard ERC |

| Application Binary Interface (ABI) | Impl (Rust) / Implements (Java) | Mappatura di semantica e logica

La colonna di sinistra mostra gli elementi specifici del protocollo RGB. La colonna centrale mostra la funzione concreta di ciascun componente. Poi, nella colonna "equivalente OOP", troviamo il termine equivalente nella programmazione orientata agli oggetti:


- La **Genesi** svolge un ruolo simile a quello di un *costruttore di classe*: è qui che viene inizializzato lo stato del contratto;
- Lo **Schema** è la descrizione di una classe, cioè la definizione delle sue proprietà, dei suoi metodi e della logica sottostante;
- L'**interfaccia** corrisponde alle *interfacce* (Java), ai *tratti* (Rust) o ai *protocolli* (Swift): si tratta delle definizioni pubbliche di funzioni, eventi, campi... ;
- L'**Interface Implementation** corrisponde a *Impl* in Rust o a *Implements* in Java, dove si specifica come il codice eseguirà effettivamente i metodi annunciati nell'interfaccia.

Nel contesto di Ethereum, la Genesi è più vicina al *costruttore del contratto*, lo Schema alla definizione del contratto, l'Interfaccia a uno standard come ERC-20 o ERC-721 e l'Implementazione dell'Interfaccia all'ABI (*Application Binary Interface*), che specifica il formato delle interazioni con il contratto.

Il vantaggio della modularità di RGB risiede anche nel fatto che diverse parti interessate possono scrivere, ad esempio, la propria implementazione dell'interfaccia, purché rispettino la logica dello *Schema* e la semantica dell'*Interfaccia*. In questo modo, un emittente potrebbe sviluppare un nuovo front-end (interfaccia) più facile da usare, senza modificare la logica del contratto, o viceversa, si potrebbe estendere lo Schema per aggiungere funzionalità e fornire una nuova versione dell'implementazione dell'interfaccia adattata, mentre le vecchie implementazioni rimarrebbero valide per le funzionalità di base.

Quando compiliamo un nuovo contratto, generiamo una Genesi (il primo passo per l'emissione o la distribuzione dell'asset), nonché i suoi componenti (Schema, Interfaccia, Implementazione dell'interfaccia). Dopodiché, il contratto è pienamente operativo e può essere propagato ai portafogli e agli utenti. Questo metodo, in cui Genesis è combinato con questi tre componenti, garantisce un alto grado di personalizzazione (ogni contratto può avere una propria logica), decentralizzazione (tutti possono contribuire a un determinato componente) e sicurezza (la convalida rimane rigorosamente definita dal protocollo, senza dipendere da codice arbitrario sulla catena, come spesso accade su altre blockchain).

Vorrei ora dare un'occhiata più da vicino a ciascuno di questi componenti: lo **Schema**, l'**Interfaccia** e l'**Implementazione dell'interfaccia**.

### Schema

Nella sezione precedente abbiamo visto che nell'ecosistema RGB un contratto è composto da diversi elementi: la Genesi, che stabilisce lo stato iniziale, e diversi altri componenti complementari. Lo scopo dello Schema è quello di descrivere in modo dichiarativo tutta la logica di business del contratto, ovvero la struttura dei dati, i tipi utilizzati, le operazioni consentite e le loro condizioni. È quindi un elemento molto importante per rendere operativo un contratto sul lato client, poiché ogni partecipante (un portafoglio, ad esempio) deve verificare che le transizioni di stato che riceve siano conformi alla logica definita nello Schema.

Uno schema può essere paragonato a una "classe" nella programmazione orientata agli oggetti (OOP). In generale, serve come modello che definisce i componenti di un contratto, come ad esempio :


- I diversi tipi di Stati di proprietà e di incarichi ;
- Valenze, ovvero diritti speciali che possono essere attivati (*riscattati*) per determinate operazioni;
- Campi Global State, che descrivono le proprietà globali, pubbliche e condivise del contratto;
- La struttura Genesis (la prima operazione che attiva il contratto) ;
- Le forme consentite di transizioni di stato e di estensioni di stato e il modo in cui queste operazioni possono modificare il ;
- Metadati associati a ciascuna operazione, per memorizzare informazioni temporanee o aggiuntive;
- Regole che determinano il modo in cui i dati del contratto interno possono evolvere (ad esempio, se un campo è mutabile o cumulativo);
- Sequenze di operazioni considerate valide: ad esempio, un ordine di transizioni da rispettare o un insieme di condizioni logiche da soddisfare.

![RGB-Bitcoin](assets/fr/071.webp)

Quando l'*emittente* di un asset su RGB pubblica un contratto, fornisce la Genesi e lo Schema ad esso associato. Gli utenti o i portafogli che desiderano interagire con l'asset recuperano questo Schema per comprendere la logica alla base del contratto e per poter verificare in seguito che le transizioni a cui parteciperanno siano legittime.

Il primo passo, per chiunque riceva informazioni su un asset RGB (ad esempio un trasferimento di token), è quello di convalidare queste informazioni rispetto allo Schema. Ciò comporta l'utilizzo della compilazione dello Schema per :


- Verificare che gli Stati posseduti, le assegnazioni e gli altri elementi siano definiti correttamente e che rispettino i tipi imposti (il cosiddetto *sistema di tipi severo*);
- Verificare che le regole di transizione (script di convalida) siano soddisfatte. Questi script possono essere eseguiti tramite AluVM, che è presente sul lato client ed è responsabile della convalida della coerenza della logica aziendale (importo del trasferimento, condizioni speciali, ecc.).

In pratica, Schema non è codice eseguibile, come si può vedere nelle blockchain che memorizzano codice on-chain (EVM su Ethereum). Al contrario, RGB separa la logica aziendale (dichiarativa) dal codice eseguibile sulla blockchain (che è limitato alle ancore crittografiche). In questo modo, lo Schema determina le regole, ma l'applicazione di queste regole avviene al di fuori della blockchain, sul sito di ciascun partecipante, secondo il principio della Convalida lato client.

Uno schema deve essere compilato prima di poter essere utilizzato dalle applicazioni RGB. Questa compilazione produce un file binario (ad esempio `.rgb`) o un file binario criptato (`.rgba`). Quando il portafoglio importa questo file, sa che :


- Come si presenta ogni tipo di dato (interi, strutture, array...) grazie al rigido sistema di tipi;
- Come dovrebbe essere strutturato Genesis (per comprendere l'inizializzazione delle risorse);
- I diversi tipi di operazioni (transizioni di stato, estensioni di stato) e come possono modificare lo stato ;
- Le regole di scripting (introdotte nello Schema) che il motore di AluVM applicherà per verificare la validità delle operazioni.

Come spiegato nei capitoli precedenti, il *sistema di tipi severi* ci fornisce un formato di codifica stabile e deterministico: tutte le variabili, siano esse Stati posseduti, Stati globali o Valenze, sono descritte con precisione (dimensione, limiti inferiori e superiori se necessario, tipo firmato o non firmato, ecc.) È anche possibile definire strutture annidate, ad esempio per supportare casi d'uso complessi.

Facoltativamente, lo schema può fare riferimento a uno `SchemaId` principale, che facilita il riutilizzo di una struttura di base esistente (un modello). In questo modo, è possibile evolvere un contratto o creare variazioni (ad esempio un nuovo tipo di token) da un modello già collaudato. Questa modularità evita la necessità di ricreare interi contratti e incoraggia la standardizzazione delle migliori pratiche.

Un altro punto importante è che la logica dell'evoluzione dello stato (trasferimenti, aggiornamenti, ecc.) è descritta nello Schema sotto forma di script, regole e condizioni. Quindi, se il progettista del contratto desidera autorizzare una riemissione o imporre un meccanismo di bruciatura (distruzione dei token), può specificare gli script corrispondenti per AluVM nella parte di validazione dello Schema.

#### Differenza rispetto alle blockchain on-chain programmabili

A differenza di sistemi come Ethereum, dove il codice dello smart contract (eseguibile) è scritto nella blockchain stessa, RGB memorizza il contratto (la sua logica) fuori dalla catena, sotto forma di documento dichiarativo compilato. Ciò implica che :


- Non esiste una macchina virtuale Turing-completa in esecuzione in ogni nodo della rete Bitcoin. Le regole di un contratto RGB non vengono eseguite sulla blockchain, ma in ogni utente che desidera convalidare uno stato;
- I dati dei contratti non inquinano la blockchain: solo le prove crittografiche (*impegni*) sono incorporate nelle transazioni Bitcoin (tramite `Tapret` o `Opret`);
- Lo Schema può essere aggiornato o rifiutato (*fast-forward*, *push-back*, ecc.), senza richiedere un fork della blockchain Bitcoin. I portafogli devono semplicemente importare il nuovo Schema e adattarsi alle modifiche del consenso.

#### Utilizzo da parte dell'emittente e degli utenti

Quando un *emittente* crea un'attività (ad esempio, un gettone fungibile non inflazionistico), prepara :


- Uno schema che descrive le regole di emissione, trasferimento, ecc;
- Una Genesi adattata a questo Schema (con il numero totale di gettoni emessi, l'identità del proprietario iniziale, eventuali Valenze speciali per la riemissione, ecc.)

Mette quindi a disposizione degli utenti lo Schema compilato (un file `.rgb`), in modo che chiunque riceva un trasferimento di questo token possa verificare localmente la coerenza dell'operazione. Senza questo Schema, un utente non sarebbe in grado di interpretare i dati di stato o di verificare la conformità alle regole del contratto.

Quindi, quando un nuovo portafoglio vuole supportare un asset, deve semplicemente integrare il relativo Schema. Questo meccanismo consente di aggiungere la compatibilità a nuovi tipi di asset RGB, senza modificare in modo invasivo il software di base del portafoglio: è sufficiente importare il binario dello Schema e comprenderne la struttura.

Lo Schema definisce la logica di business in RGB. Elenca le regole di evoluzione di un contratto, la struttura dei suoi dati (Stati di proprietà, Stato globale, Valenze) e gli script di validazione associati (eseguibili da AluVM). Grazie a questo documento dichiarativo, la definizione di un contratto (file compilato) è chiaramente separata dall'effettiva esecuzione delle regole (lato client). Questo disaccoppiamento conferisce a RGB una grande flessibilità, consentendo un'ampia gamma di casi d'uso (token fungibili, NFT, contratti più sofisticati) ed evitando al contempo la complessità e i difetti tipici delle blockchain programmabili on-chain.

#### Esempio di schema

Vediamo un esempio concreto di Schema per un contratto RGB. Si tratta di un estratto in Rust del file `nia.rs` (iniziali di "*Non-Inflatable Assets*"), che definisce un modello per i token fungibili che non possono essere riemessi oltre la loro fornitura iniziale (un asset non inflazionistico). Questo tipo di token può essere visto come l'equivalente, nell'universo RGB, dell'ERC20 di Ethereum, cioè token fungibili che rispettano alcune regole di base (ad esempio sui trasferimenti, sull'inizializzazione della fornitura, ecc.)

Prima di immergersi nel codice, vale la pena ricordare la struttura generale di uno schema RGB. C'è una serie di dichiarazioni che incorniciano :


- Un possibile `SchemaId` che indica l'uso di un altro schema di base come modello;
- Gli **Stati globali** e gli **Stati posseduti** (con i loro tipi rigorosi) ;
- Valenze** (se presenti);
- Le **Operazioni** (Genesi, Transizioni di stato, Estensioni di stato) che possono fare riferimento a questi stati e valenze;
- Il **Sistema di tipi rigorosi** utilizzato per descrivere e convalidare i dati;
- Script di convalida** (eseguiti tramite AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

Il codice sottostante mostra la definizione completa dello schema di Rust. Lo commenteremo parte per parte, seguendo le annotazioni da (1) a (9):

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Intestazione della funzione e sotto-schema**

La funzione `nia_schema()` restituisce un `SubSchema`, indicando che questo Schema può parzialmente ereditare da uno schema più generico. Nell'ecosistema RGB, questa flessibilità consente di riutilizzare alcuni elementi standard di uno schema principale, per poi definire regole specifiche per il contratto in questione. In questo caso, si sceglie di non abilitare l'ereditarietà, poiché `subset_of` sarà `None`.


- (2) - Proprietà generali: ffv, subset_of, type_system**

La proprietà `ffv` corrisponde alla versione *veloce* del contratto. Un valore di `zero!()` indica che siamo alla versione 0 o alla versione iniziale di questo schema. Se in seguito si desidera aggiungere nuove funzionalità (nuovi tipi di operazioni, ecc.), si può incrementare questa versione per indicare una modifica del consenso.

La proprietà `subset_of: None` conferma l'assenza di ereditarietà. Il campo `type_system` si riferisce al sistema di tipi rigorosi già definito nella libreria `types`. Questa riga indica che tutti i dati utilizzati dal contratto utilizzano l'implementazione della serializzazione rigorosa fornita dalla libreria in questione.


- (3) - Stati globali

Nel blocco `global_types`, si dichiarano quattro elementi. Utilizziamo la chiave, come `GS_NOMINAL` o `GS_ISSUED_SUPPLY`, per farvi riferimento in seguito:


- `GS_NOMINAL` si riferisce a un tipo `DivisibleAssetSpec`, che descrive vari campi del token creato (nome completo, ticker, precisione...);
- `GS_DATA` rappresenta dati generali, come una dichiarazione di non responsabilità, metadati o altro testo;
- `GS_TIMESTAMP` si riferisce a una data di emissione;
- `GS_ISSUED_SUPPLY` imposta l'offerta totale, cioè il numero massimo di gettoni che possono essere creati.

La parola chiave `once(...)` significa che ognuno di questi campi può comparire una sola volta.


- (4) - Tipi di proprietà

In `owned_types`, dichiariamo `OS_ASSET`, che descrive uno stato fungibile. Utilizziamo `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, indicando che la quantità di asset (token) è memorizzata come un intero a 64 bit senza segno. Pertanto, ogni transazione invierà una certa quantità di unità di questo token, che sarà convalidata in base a questa struttura numerica strettamente tipizzata.


- (5) - Valenze**

Indichiamo `tipi_di_valenza: nessuno!()`, il che significa che non ci sono valenze in questo schema, in altre parole non ci sono diritti speciali o extra (come la riedizione, la masterizzazione condizionale, ecc.). Se uno schema ne includesse, sarebbero dichiarate in questa sezione.


- (6) - Genesi: prime operazioni

Qui entriamo nella parte che dichiara le Operazioni contrattuali. La Genesi è descritta da :


- L'assenza di `metadati` (campo `metadati: Ty::<SemId>::UNIT.id(None)`) ;
- Stati globali che devono essere presenti una volta ciascuno (`Once`);
- Un elenco di Assegnazioni in cui `OS_ASSET` deve apparire `Una volta o più`. Ciò significa che Genesis richiede almeno un'assegnazione di `OS_ASSET` (un titolare iniziale);
- Nessuna valenza : `valenze: nessuna!()`.

In questo modo limitiamo la definizione dell'emissione iniziale del token: dobbiamo dichiarare l'offerta emessa (`GS_ISSUED_SUPPLY`), più almeno un possessore (un Owned State di tipo `OS_ASSET`).


- (7) - Estensioni

Il campo `estensioni: nessuna!()` indica che in questo contratto non è prevista alcuna estensione di stato. Ciò significa che non esiste alcuna operazione per riscattare un diritto digitale (Valency) o per eseguire un'estensione di stato prima di una transizione. Tutto avviene tramite Genesi o Transizioni di Stato.


- (8) - Transizioni: TS_TRANSFER

In `transizioni', definiamo il tipo di operazione `TS_TRANSFER'. Spieghiamo che :


- Non ha metadati;
- Non modifica lo Stato globale (che è già definito in Genesis);
- Prende come input uno o più `OS_ASSET`. Ciò significa che deve spendere gli Stati posseduti esistenti;
- Crea (`assegna`) almeno un nuovo `OS_ASSET` (in altre parole, il destinatario o i destinatari ricevono i token) ;
- Non genera nuova Valenza.

Questo modella il comportamento di un trasferimento di base, che consuma gettoni su un UTXO, quindi crea nuovi Stati Propri a favore dei destinatari, e quindi preserva l'uguaglianza dell'importo totale tra entrate e uscite.


- (9) - Script AluVM e punti di ingresso** (in francese)

Infine, si dichiara uno script AluVM (`Script::AluVM(AluScript { ... })`). Questo script contiene :


- Una o più librerie esterne (`libs`) da utilizzare durante la validazione;
- Punti di ingresso che puntano a offset di funzioni nel codice di AluVM, corrispondenti alla convalida della Genesi (`ValidateGenesis`) e di ogni Transizione dichiarata (`ValidateTransition(TS_TRANSFER)`).

Questo codice di validazione è responsabile dell'applicazione della logica di business. Ad esempio, controllerà :


- Che il valore `GS_ISSUED_SUPPLY` non venga superato durante Genesis ;
- Che la somma degli `ingressi` (gettoni spesi) sia uguale alla somma delle `assegnazioni` (gettoni ricevuti) per `TS_TRANSFER`.

Se queste regole non vengono rispettate, la transizione sarà considerata non valida.

Questo esempio di schema "*Asset fungibile non gonfiabile*" ci permette di comprendere meglio la struttura di un semplice contratto di token fungibile RGB. Possiamo vedere chiaramente la separazione tra la descrizione dei dati (Stati globali e di proprietà), la dichiarazione delle operazioni (Genesi, Transizioni, Estensioni) e l'implementazione della validazione (script AluVM). Grazie a questo modello, un token si comporta come un classico token fungibile, ma rimane validato sul lato client e non dipende dall'infrastruttura on-chain per eseguire il suo codice. Solo gli impegni crittografici sono ancorati alla blockchain di Bitcoin.

### Interfaccia

L'interfaccia è lo strato destinato a rendere un contratto leggibile e manipolabile, sia dagli utenti (lettura umana) che dai portafogli (lettura software). L'interfaccia svolge quindi un ruolo paragonabile a quello di un'interfaccia in un linguaggio di programmazione orientato agli oggetti (Java, Rust trait, ecc.), in quanto espone e chiarisce la struttura funzionale di un contratto, senza necessariamente rivelare i dettagli interni della logica aziendale.

A differenza di Schema, che è puramente dichiarativo e compilato in un file binario difficile da usare così com'è, Interface fornisce le chiavi di lettura necessarie per :


- Elencare e descrivere gli Stati globali e gli Stati di proprietà inclusi nel contratto;
- Accedere ai nomi e ai valori di ciascun campo, in modo da poterli visualizzare (ad esempio, per un token, scoprire il suo ticker, l'importo massimo, ecc;)
- Interpretare e costruire le operazioni contrattuali (genesi, transizione di stato o estensione di stato) associando i dati a nomi comprensibili (ad esempio, eseguire un trasferimento specificando chiaramente "importo" piuttosto che un identificatore binario).

![RGB-Bitcoin](assets/fr/073.webp)

Grazie all'interfaccia, è possibile, ad esempio, scrivere codice in un portafoglio che, invece di manipolare i campi, manipola direttamente le etichette come "numero di token", "nome dell'asset", ecc. In questo modo, la gestione di un contratto diventa più intuitiva. In questo modo, la gestione dei contratti diventa più intuitiva.

#### Funzionamento generale

Questo metodo presenta molti vantaggi:


- Standardizzazione:**

Lo stesso tipo di contratto può essere supportato da un'interfaccia standard, condivisa da diverse implementazioni di portafogli. Questo facilita la compatibilità e il riutilizzo del codice.


- Chiara separazione tra Schema e Interfaccia:**

Nella progettazione RGB, Schema (logica di business) e Interfaccia (presentazione e manipolazione) sono due entità indipendenti. Gli sviluppatori che scrivono la logica del contratto possono concentrarsi sullo Schema, senza preoccuparsi dell'ergonomia o della rappresentazione dei dati, mentre un altro team (o lo stesso team, ma con una tempistica diversa) può sviluppare l'Interfaccia.


- Evoluzione flessibile:**

L'interfaccia può essere modificata o aggiunta dopo l'emissione dell'asset, senza dover modificare il contratto stesso. Questa è una differenza sostanziale rispetto ad alcuni sistemi di smart contract on-chain, in cui l'interfaccia (spesso mescolata al codice di esecuzione) è congelata nella blockchain.


- Capacità multi-interfaccia

Lo stesso contratto potrebbe essere esposto attraverso diverse interfacce adatte a esigenze diverse: un'interfaccia semplice per l'utente finale, un'altra più avanzata per l'emittente che deve gestire operazioni di configurazione complesse. Il portafoglio può quindi scegliere quale Interfaccia importare, a seconda del suo utilizzo.

![RGB-Bitcoin](assets/fr/074.webp)

In pratica, quando il portafoglio recupera un contratto RGB (tramite un file `.rgb` o `.rgba`), importa anche l'interfaccia associata, che viene anch'essa compilata. In fase di esecuzione, il portafoglio può, ad esempio :


- Sfogliare l'elenco degli Stati e leggere i loro nomi, per visualizzare Ticker, Importo iniziale, Data di emissione, ecc. sull'interfaccia utente, anziché un identificativo numerico illeggibile;
- Costruire un'operazione (come un trasferimento) usando nomi di parametri espliciti: invece di scrivere `assegnazioni { OS_ASSET => 1 }`, si può offrire all'utente un campo "Importo" in un modulo, e tradurre questa informazione nei campi strettamente tipizzati previsti dal contratto.

#### Differenza con Ethereum e altri sistemi

Su Ethereum, l'interfaccia (descritta tramite l'ABI, *Application Binary Interface*) è generalmente derivata dal codice memorizzato sulla catena (lo smart contract). Può essere costoso o complicato modificare una parte specifica dell'interfaccia senza toccare il contratto stesso. Tuttavia, RGB si basa su una logica interamente fuori dalla catena, con dati ancorati in *impegni* su Bitcoin. Questo design consente di modificare l'interfaccia (o la sua implementazione) senza influire sulla sicurezza fondamentale del contratto, poiché la convalida delle regole commerciali rimane nello schema e nel codice AluVM di riferimento.

#### Compilazione dell'interfaccia

Come per gli schemi, l'interfaccia è definita nel codice sorgente (spesso in Rust) e compilata in un file `.rgb` o `.rgba`. Questo file binario contiene tutte le informazioni necessarie al portafoglio per :


- Identificare i campi per nome ;
- Collegare ogni campo (e il suo valore) al tipo di sistema rigoroso definito nel contratto;
- Conoscere le diverse operazioni consentite e come costruirle.

Una volta importata l'interfaccia, il portafoglio può visualizzare correttamente il contratto e proporre interazioni all'utente.

### Interfacce standardizzate dall'associazione LNP/BP

Nell'ecosistema RGB, un'Interfaccia viene utilizzata per dare un significato leggibile e manipolabile ai dati e alle operazioni di un contratto. L'Interfaccia integra quindi lo Schema, che descrive internamente la logica di business (tipi rigorosi, script di validazione, ecc.). In questa sezione, daremo un'occhiata alle Interfacce standard sviluppate dall'associazione LNP/BP per i tipi di contratto più comuni (token fungibili, NFT, ecc.).

Come promemoria, l'idea è che ogni Interfaccia descriva come visualizzare e manipolare un contratto dal lato del portafoglio, nominando chiaramente i campi (come `spec`, `ticker`, `issuedSupply`...) e definendo le possibili operazioni (come `Transfer`, `Burn`, `Rename`...). Diverse interfacce sono già operative, ma ce ne saranno altre in futuro.

#### Alcune interfacce pronte all'uso

**RGB20** è l'interfaccia per gli asset fungibili, che può essere paragonata allo standard ERC20 di Ethereum. Tuttavia, si spinge oltre, offrendo funzionalità più ampie:


- Ad esempio, la possibilità di rinominare l'attività (modifica del *ticker* o del nome completo) dopo che è stata emessa, o di aggiustarne la precisione (*scissioni azionarie*);
- Può anche descrivere meccanismi per la riemissione secondaria (limitata o illimitata) e per la bruciatura e la successiva sostituzione, al fine di autorizzare l'emittente a distruggere e poi ricreare le attività in determinate condizioni;

Ad esempio, l'interfaccia RGB20 può essere collegata allo schema **Non-Inflatable Asset (NIA)**, che impone una fornitura iniziale non inflazionabile, o ad altri schemi più avanzati, a seconda delle esigenze.

**RGB21** riguarda i contratti di tipo NFT o, più in generale, qualsiasi contenuto digitale unico, come la rappresentazione di media digitali (immagini, musica, ecc.). Oltre a descrivere l'emissione e il trasferimento di un singolo bene, include caratteristiche quali :


- Supporto integrato per l'inclusione diretta di un file (fino a 16 MB) nel contratto (per il recupero lato client);
- La possibilità per il proprietario di inserire una "*incisione*" nella cronologia per dimostrare la passata proprietà di un NFT.

**RGB25** è uno standard ibrido che combina aspetti fungibili e non fungibili. È stato progettato per asset parzialmente fungibili, come la tokenizzazione di immobili, in cui si desidera suddividere una proprietà mantenendo un collegamento a un singolo asset principale (in altre parole, si hanno pezzi fungibili di una casa, collegati a una casa non fungibile). Tecnicamente, questa interfaccia può essere collegata allo schema **Collectible Fungible Asset* (CFA)**, che tiene conto della nozione di suddivisione, pur tracciando il bene originale.

#### Interfacce in fase di sviluppo

Altre interfacce sono previste per usi più specialistici, ma non sono ancora disponibili:


- RGB22**, dedicato alle identità digitali, per gestire gli identificatori e i profili on-chain nell'ecosistema RGB;
- RGB23**, per la marcatura temporale avanzata, utilizzando alcune idee di *Opentimestamps*, ma con funzioni di tracciabilità;
- RGB24**, che mira all'equivalente di un sistema di nomi di dominio (DNS) decentralizzato simile all'*Ethereum Name Service* ;
- RGB26**, progettato per gestire le DAO (*Decentralized Autonomous Organization*) in un formato più complesso (governance, votazione, ecc.);
- RGB30**, molto simile a RGB20 ma con la particolarità di tenere conto dell'emissione iniziale decentralizzata e di utilizzare le estensioni statali. Questo sarebbe utilizzato per le attività la cui riemissione è gestita da diverse entità, o soggetta a condizioni più sottili.

Naturalmente, a seconda della data di consultazione del corso, queste interfacce potrebbero essere già operative e accessibili.

#### Esempio di interfaccia

Questo frammento di codice di Rust mostra un'interfaccia [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) (risorsa fungibile). Questo codice è tratto dal file `rgb20.rs` della libreria standard RGB. Vediamolo per capire la struttura di un'interfaccia e come essa costituisca un ponte tra, da un lato, la logica aziendale (definita nello schema) e, dall'altro, le funzionalità esposte ai portafogli e agli utenti.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

In questa interfaccia, notiamo delle somiglianze con la struttura dello Schema: troviamo una dichiarazione dello Stato globale, degli Stati posseduti, delle Operazioni contrattuali (Genesi e Transizioni), nonché la gestione degli errori. Ma l'Interfaccia si concentra sulla presentazione e sulla manipolazione di questi elementi per un portafoglio o per qualsiasi altra applicazione.

La differenza con Schema sta nella natura dei tipi. Schema utilizza tipi rigidi (come `FungibleType::Unsigned64Bit`) e identificatori più tecnici. L'interfaccia utilizza nomi di campi, macro (`fname!()`, `tn!()`) e riferimenti a classi di argomenti (`ArgSpec`, `OwnedIface::Rights`...). L'obiettivo è quello di facilitare la comprensione funzionale e l'organizzazione degli elementi per il portafoglio.

Inoltre, l'Interfaccia può introdurre funzionalità aggiuntive allo Schema di base (ad esempio, la gestione di un diritto `burnEpoch`), purché rimanga coerente con la logica finale convalidata sul lato client. La sezione "script" di AluVM nello Schema garantirà la validità crittografica, mentre l'Interfaccia descrive come l'utente (o il portafoglio) interagisce con questi stati e transizioni.

#### Stato globale e incarichi

Nella sezione `global_state`, troviamo campi come `spec` (descrizione dell'asset), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Si tratta di campi che il portafoglio può leggere e presentare. Ad esempio:


- `spec` mostrerà la configurazione del token;
- `issuedSupply` o `burnedSupply` ci danno il numero totale di gettoni emessi o bruciati, ecc.

Nella sezione `assegnazioni' si definiscono vari ruoli o diritti. Ad esempio:


- `assetOwner` corrisponde alla detenzione di gettoni (è lo stato fungibile *Owned State*) ;
- `burnRight` corrisponde alla capacità di bruciare le pedine ;
- updateRight` corrisponde al diritto di rinominare la risorsa.

La parola chiave `public` o `private` (ad esempio `AssignIface::public(...)`) indica se questi stati sono visibili (`public`) o riservati (`private`). Per quanto riguarda `Req::NoneOrMore`, `Req::Optional`, indicano l'occorrenza prevista.

#### Genesi e transizioni

La parte `genesi` descrive come viene inizializzata la risorsa:


- I campi `spec`, `data`, `created`, `issuedSupply` sono obbligatori (`ArgSpec::required()`) ;
- Assegnazioni come `assetOwner` possono essere presenti in più copie (`ArgSpec::many()`), consentendo di distribuire i token a più titolari iniziali;
- Campi come `inflationAllowance` o `burnEpoch` possono essere (o meno) inclusi in Genesis.

Poi, per ogni transizione (`Transfer`, `Issue`, `Burn`...), l'interfaccia definisce quali campi l'operazione si aspetta come input, quali campi l'operazione produrrà come output e gli eventuali errori che possono verificarsi. Per esempio:

**Transizione :**


- Ingressi : `precedente` → deve essere un `assetOwner` ;
- Assegnazioni: il `beneficiario` → sarà un nuovo `assetOwner` ;
- Errore: `NON_EQUAL_AMOUNTS` (il portafoglio sarà quindi in grado di gestire i casi in cui la somma di ingresso non corrisponde alla somma di uscita).

**Transizione `Issue` :**


- Opzionale (`optional: true`), in quanto l'emissione aggiuntiva non viene necessariamente attivata;
- Ingressi: `used` → una `inflationAllowance`, cioè il permesso di aggiungere altri token ;
- Assegnazioni: `beneficiario` (nuovi gettoni ricevuti) e `futuro` (rimanenza di `inflationAllowance`) ;
- Possibili errori: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, ecc.

**Transizione di fuoco :**


- Ingressi : `usato` → a `burnRight` ;
- Globali : `burnedSupply` richiesto ;
- Incarichi: `futuro` → una possibile continuazione del `burnRight` se non abbiamo bruciato tutto ;
- Errori: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Ogni operazione è quindi descritta in modo leggibile per un portafoglio. Ciò consente di visualizzare un'interfaccia grafica in cui l'utente può vedere chiaramente: "Hai il diritto di bruciare. Vuoi bruciare una certa quantità? Il codice sa che deve compilare un campo `burnedSupply` e verificare che il `burnRight` sia valido.

Per riassumere, è importante tenere presente che un'interfaccia, per quanto completa, non definisce da sola la logica interna del contratto. Il cuore del lavoro è svolto dallo **Schema**, che include tipi rigorosi, struttura di Genesis, transizioni e così via. L'interfaccia espone semplicemente questi elementi in modo più intuitivo e con un nome, per poterli utilizzare in un'applicazione.

Grazie alla modularità di RGB, l'interfaccia può essere aggiornata (ad esempio, aggiungendo una transizione `Rename`, correggendo la visualizzazione di un campo e così via) senza dover riscrivere l'intero contratto. Gli utenti di questa interfaccia possono quindi beneficiare immediatamente di questi miglioramenti, non appena aggiornano il file `.rgb` o `.rgba`.

Ma una volta dichiarata un'interfaccia, è necessario collegarla allo schema corrispondente. Ciò avviene tramite l'***Interface Implementation***, che specifica come mappare ogni campo denominato (come `fname!("assetOwner")`) all'ID rigoroso (come `OS_ASSET`) definito nello schema. Questo assicura, ad esempio, che quando un portafoglio manipola un campo `burnRight`, questo sia lo stato che, nello Schema, descrive la capacità di bruciare token.

### Implementazione dell'interfaccia

Nell'architettura RGB, abbiamo visto che ogni componente (Schema, Interfaccia, ecc.) può essere sviluppato e compilato indipendentemente. Tuttavia, c'è ancora un elemento indispensabile che collega tra loro questi diversi blocchi costruttivi: l'***Interface Implementation***. È questa che mappa esplicitamente gli identificatori o i campi definiti nello Schema (dal lato della logica aziendale) ai nomi dichiarati nell'Interfaccia (dal lato della presentazione e dell'interazione con l'utente). In questo modo, quando un portafoglio carica un contratto, può capire esattamente a quale campo corrisponde cosa, e come un'operazione denominata nell'Interfaccia si riferisce alla logica dello Schema.

Un punto importante è che l'implementazione dell'interfaccia non è necessariamente destinata a esporre tutte le funzionalità dello schema, né tutti i campi dell'interfaccia: può essere limitata a un sottoinsieme. In pratica, ciò consente di limitare o filtrare alcuni aspetti dello schema. Ad esempio, si potrebbe avere uno Schema con quattro tipi di operazioni, ma un'Interfaccia di implementazione che ne mappa solo due in un determinato contesto. Al contrario, se un'interfaccia propone endpoint aggiuntivi, si può scegliere di non implementarli qui.

Ecco un classico esempio di implementazione dell'interfaccia, in cui associamo uno schema *Non-Inflatable Asset* (NIA) all'interfaccia RGB20:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

In questa interfaccia di implementazione :


- Si fa riferimento esplicito allo Schema, tramite `nia_schema()`, e all'Interfaccia, tramite `Rgb20::iface()`. Le chiamate `schema.schema_id()` e `iface.iface_id()` sono usate per ancorare l'implementazione dell'interfaccia dal lato della compilazione (questo associa gli identificatori crittografici di questi due componenti);
- Viene stabilita una mappatura tra gli elementi dello Schema e quelli dell'Interfaccia. Ad esempio, il campo `GS_NOMINAL` nello Schema è collegato alla stringa `"spec"` nell'Interfaccia (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Si fa lo stesso per le operazioni, come `TS_TRANSFER`, che si collega a `"Transfer"` nell'interfaccia... ;
- Si può notare che non ci sono valenze (`valencies: none!()`) o estensioni (`extensions: none!()`), il che riflette il fatto che questo contratto NIA non usa queste caratteristiche.

Il risultato dopo la compilazione è un file `.rgb` o `.rgba` separato, da importare nel portafoglio in aggiunta allo Schema e all'Interfaccia. In questo modo, il software sa come collegare concretamente questo contratto NIA (la cui logica è descritta dal suo Schema) all'Interfaccia "RGB20" (che fornisce nomi umani e una modalità di interazione per i gettoni fungibili), applicando questa Implementazione dell'Interfaccia come gateway tra i due.

#### Perché separare l'implementazione dell'interfaccia?

La separazione aumenta la flessibilità. Un singolo schema può avere diverse implementazioni di interfacce distinte, ognuna delle quali mapperà un diverso insieme di funzionalità. Inoltre, la stessa implementazione dell'interfaccia può evolversi o essere riscritta senza richiedere una modifica dello schema o dell'interfaccia. In questo modo si mantiene il principio di modularità di RGB: ogni componente (Schema, Interfaccia, Implementazione dell'Interfaccia) può essere modificato e aggiornato in modo indipendente, purché vengano rispettate le regole di compatibilità imposte dal protocollo (stessi identificatori, coerenza dei tipi, ecc.).

Nell'uso concreto, quando il portafoglio carica un contratto, deve :


- Caricare lo **Schema** compilato (per conoscere la struttura della logica di business) ;
- Caricare **interfaccia** compilata (per capire i nomi e le operazioni lato utente) ;
- Caricare la **Interface Implementation** compilata (per collegare la logica dello schema ai nomi delle interfacce, operazione per operazione, campo per campo).

Questa architettura modulare rende possibili scenari di utilizzo come :


- Limitare alcune operazioni per determinati utenti: offrire un'interfaccia di implementazione parziale che dia accesso solo ai trasferimenti di base, senza offrire funzioni di masterizzazione o aggiornamento, ad esempio;
- Presentazione delle modifiche: progettare un'implementazione dell'interfaccia che rinomini un campo dell'interfaccia o lo mappi in modo diverso, senza alterare la base del contratto;
- Supporto di più schemi: un portafoglio può caricare più implementazioni di interfaccia per lo stesso tipo di interfaccia, per gestire schemi diversi (logiche di token diverse), purché la loro struttura sia compatibile.

Nel prossimo capitolo vedremo come funziona il trasferimento di un contratto e come vengono generate le fatture RGB.

## Trasferimenti di contratti

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

In questo capitolo analizzeremo il processo di trasferimento di un contratto nell'ecosistema RGB. Per illustrarlo, prenderemo in considerazione Alice e Bob, i nostri soliti protagonisti, che desiderano scambiare un asset RGB. Mostreremo anche alcuni estratti di comandi dello strumento a riga di comando `rgb`, per vedere come funziona in pratica.

### Comprendere il trasferimento del contratto RGB

Facciamo un esempio di trasferimento tra Alice e Bob. In questo esempio, ipotizziamo che Bob abbia appena iniziato a utilizzare RGB, mentre Alice possiede già asset RGB nel suo portafoglio. Vedremo come Bob configura il suo ambiente, importa il relativo contratto, richiede un trasferimento ad Alice e infine come Alice esegue la transazione effettiva sulla blockchain Bitcoin.

#### 1) Installazione del portafoglio RGB

Prima di tutto, Bob deve installare un portafoglio RGB, cioè un software compatibile con il protocollo. All'inizio non contiene alcun contratto. Bob avrà anche bisogno di :


- Un portafoglio Bitcoin per gestire gli UTXO;
- Una connessione a un nodo Bitcoin (o a un server Electrum), in modo da poter identificare gli UTXO e propagare le transazioni sulla rete.

Come promemoria, gli **Stati posseduti** in RGB si riferiscono agli UTXO di Bitcoin. Dobbiamo quindi essere sempre in grado di gestire e spendere gli UTXO in una transazione Bitcoin che incorpora impegni crittografici (`Tapret` o `Opret`) che puntano ai dati RGB.

#### 2) Acquisizione di informazioni sul contratto

Bob deve quindi recuperare i dati del contratto che gli interessano. Questi dati possono circolare attraverso qualsiasi canale: sito web, e-mail, applicazione di messaggistica... In pratica, vengono raggruppati in un ***incarico***, cioè un piccolo pacchetto di dati contenente :


- La **Genesi**, che definisce lo stato iniziale del contratto;
- Lo **Schema**, che descrive la logica aziendale (tipi rigorosi, script di validazione, ecc.);
- L'**interfaccia**, che definisce il livello di presentazione (nomi dei campi, operazioni accessibili);
- L'**implementazione dell'interfaccia**, che collega concretamente lo schema all'interfaccia.

![RGB-Bitcoin](assets/fr/075.webp)

La dimensione totale è spesso dell'ordine di pochi kilobyte, poiché ogni componente pesa generalmente meno di 200 byte. Può anche essere possibile trasmettere questo invio in Base58, tramite canali resistenti alla censura (come Nostr o la rete Lightning, ad esempio), o come codice QR.

#### 3) Importazione e convalida del contratto

Una volta ricevuta la partita, Bob la importa nel suo portafoglio RGB. Questo poi :


- Verificare che Genesis e Schema siano validi;
- Interfaccia di carico e implementazione dell'interfaccia ;
- Aggiornare la scorta di dati sul lato client.

Bob può ora vedere l'asset nel suo portafoglio (anche se non lo possiede ancora) e capire quali campi sono disponibili, quali operazioni sono possibili... A questo punto deve contattare la persona che possiede effettivamente l'asset da trasferire. Nel nostro esempio, si tratta di Alice.

Il processo di scoperta di chi detiene un determinato asset RGB è simile alla ricerca di un pagatore di Bitcoin. I dettagli di questa connessione dipendono dall'uso (marketplace, canali di chat privati, fatturazione, vendita di beni e servizi, stipendio...).

#### 4) Emissione di una fattura

Per avviare il trasferimento di un bene RGB, Bob deve prima emettere una fattura. Questa fattura viene utilizzata per :


- Indicare ad Alice il tipo di operazione da eseguire (ad esempio, un `Trasferimento` da un'interfaccia RGB20);
- Fornire ad Alice la *definizione del sigillo* di Bob (cioè l'UTXO in cui desidera ricevere il bene);
- Specificare la quantità di principio attivo richiesta (ad es. 100 unità).

Bob utilizza lo strumento `rgb` alla riga di comando. Supponiamo che voglia 100 unità di un token il cui `ContractId` è noto, che voglia affidarsi a `Tapret` e che specifichi il suo UTXO (`456e3..dfe1:0`):

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Alla fine di questo capitolo esamineremo più da vicino la struttura delle fatture RGB.

#### 5) Trasmissione della fattura

La fattura generata (ad esempio come URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) contiene tutte le informazioni necessarie ad Alice per preparare il trasferimento. Come per la spedizione, può essere codificata in modo compatto (Base58 o un altro formato) e inviata tramite un'applicazione di messaggistica, e-mail, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Preparazione della transazione sul lato Alice

Alice riceve la fattura di Bob. Nel suo portafoglio RGB ha uno stash contenente il bene da trasferire. Per spendere l'UTXO contenente il bene, deve prima generare una PSBT (*Partially Signed Bitcoin Transaction*), cioè una transazione Bitcoin incompleta, utilizzando l'UTXO in suo possesso:

```bash
alice$ wallet construct tx.psbt
```

Questa transazione di base (per il momento non firmata) sarà utilizzata per ancorare l'impegno crittografico legato al trasferimento a Bob. L'UTXO di Alice verrà quindi speso e, in uscita, verrà inserito l'impegno `Tapret` o `Opret` per Bob.

#### 7) Generazione di partite di trasferimento

Successivamente, Alice costruisce il ***terminal consignment*** (talvolta chiamato "transfer consignment") tramite il comando :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Questo nuovo file `consignment.rgb` contiene :


- La storia completa delle transizioni di Stato necessarie per convalidare l'asset fino al momento attuale (dalla Genesi);
- La nuova transizione di stato che trasferisce le attività da Alice a Bob, in base alla fattura emessa da Bob;
- La transazione Bitcoin incompleta (*transazione testimone*) (`tx.psbt`), che spende il sigillo monouso di Alice, modificato per includere l'impegno crittografico verso Bob.

In questa fase, la transazione non è ancora trasmessa sulla rete Bitcoin. La partita è più grande di una partita di base, poiché include l'intera storia (*catena di prova*) per dimostrare la legittimità del bene.

#### 8) Bob controlla e accetta la spedizione

Alice trasmette questo **invio terminale** a Bob. Bob quindi :


- Verificare la validità della transizione di stato (assicurarsi che la storia sia coerente, che le regole del contratto siano rispettate, ecc;)
- Aggiungetelo alla vostra scorta locale;
- Eventualmente generare una firma (`sig:...`) sulla spedizione, per dimostrare che è stata esaminata e approvata (a volte chiamata "busta paga*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Opzione: Bob invia la conferma ad Alice (*borsa di pagamento*)

Se Bob lo desidera, può inviare questa firma ad Alice. Questo indica che:


- Che riconosce la transizione come valida;
- Che accetti la trasmissione della transazione Bitcoin.

Questo non è obbligatorio, ma può dare ad Alice la certezza che non ci saranno controversie successive sul trasferimento.

#### 10) Alice firma e pubblica la transazione

Alice può quindi :


- Controllare la firma di Bob (`rgb check <sig>`) ;
- Firmare la *transazione di testimonianza* che è ancora un PSBT (`segno del portafoglio`) ;
- Pubblicare la transazione del testimone sulla rete Bitcoin (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Una volta confermata, questa transazione segna la conclusione del trasferimento. Bob diventa il nuovo proprietario del bene: ora ha uno Stato di proprietà che punta all'UTXO che controlla, dimostrato dalla presenza dell'impegno nella transazione.

In sintesi, ecco il processo di trasferimento completo:

![RGB-Bitcoin](assets/fr/079.webp)

### Vantaggi dei trasferimenti RGB


- Riservatezza** :

Solo Alice e Bob hanno accesso a tutti i dati sulla transizione di stato. Essi si scambiano queste informazioni al di fuori della blockchain, attraverso le spedizioni. Gli impegni crittografici nella transazione Bitcoin non rivelano il tipo di bene o l'importo, il che garantisce una riservatezza molto maggiore rispetto ad altri sistemi di token on-chain.


- Convalida lato cliente** :

Bob può verificare la coerenza del trasferimento confrontando il *consignment* con gli *anchor* della blockchain Bitcoin. Non ha bisogno di una convalida da parte di terzi. Alice non deve pubblicare l'intera cronologia sulla blockchain, il che riduce il carico del protocollo di base e migliora la riservatezza.


- Atomicità semplificata** :

Scambi complessi (scambi atomici tra BTC e un asset RGB, ad esempio) possono essere effettuati all'interno di una singola transazione, evitando la necessità di script HTLC o PTLC. Se l'accordo non viene trasmesso, ognuno può riutilizzare i propri UTXO in altri modi.

### Schema riassuntivo del trasferimento

Prima di esaminare le fatture in dettaglio, ecco un diagramma riassuntivo del flusso complessivo di un trasferimento RGB:


- Bob installa un portafoglio RGB e ottiene la consegna del contratto iniziale;
- Bob emette una fattura indicando all'UTXO dove ricevere il bene;
- Alice riceve la fattura, costruisce il PSBT e genera la spedizione del terminale;
- Bob lo accetta, controlla, aggiunge i dati alla sua scorta e, se necessario, firma (*bolletta*);
- Alice pubblica la transazione sulla rete Bitcoin;
- La conferma della transazione rende ufficiale il trasferimento.

![RGB-Bitcoin](assets/fr/080.webp)

Il trasferimento illustra tutta la potenza e la flessibilità del protocollo RGB: uno scambio privato, convalidato dal lato del cliente, ancorato in modo minimo e discreto alla blockchain Bitcoin e che conserva il meglio della sicurezza del protocollo (nessun rischio di doppia spesa). Ciò rende RGB un ecosistema promettente per trasferimenti di valore più riservati e scalabili rispetto alle blockchain programmabili on-chain.

### Fatture RGB

In questa sezione spiegheremo in dettaglio come funzionano le **fatture** nell'ecosistema RGB e come consentono di effettuare operazioni (in particolare trasferimenti) con un contratto. In primo luogo, esamineremo gli identificatori utilizzati, poi il modo in cui sono codificati e infine la struttura di una fattura espressa come URL (un formato abbastanza pratico per l'uso nei portafogli).

#### Identificatori e codifica

Per ciascuno dei seguenti elementi viene definito un identificatore unico:


- Un contratto RGB;
- Il suo schema (logica aziendale) ;
- La sua interfaccia e l'implementazione dell'interfaccia ;
- I suoi asset (token, NFT, ecc.),

L'unicità è molto importante, poiché ogni componente del sistema deve essere distinguibile. Ad esempio, un contratto X non deve essere confuso con un altro contratto Y, e due interfacce diverse (RGB20 vs. RGB21, ad esempio) devono avere identificatori distinti.

Per rendere questi identificatori efficienti (dimensioni ridotte) e leggibili, utilizziamo il formato :


- Codifica Base58, che evita l'uso di caratteri confusi (ad esempio, `0` e la lettera `O`) e fornisce stringhe relativamente brevi;
- Un prefisso che indica la natura dell'identificatore, di solito sotto forma di `rgb:` o di un URN simile.

Per esempio, un `ContractId` potrebbe essere rappresentato da qualcosa come :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Il prefisso `rgb:` conferma che si tratta di un identificatore RGB e non di un link HTTP o di un altro protocollo. Grazie a questo prefisso, i portafogli sono in grado di interpretare correttamente la stringa.

#### Segmentazione degli identificatori

Gli identificatori RGB sono spesso molto lunghi, poiché la sicurezza (crittografica) sottostante può richiedere campi di 256 bit o più. Per agevolare la lettura e la verifica da parte dell'uomo, si suddividono queste stringhe in diversi blocchi separati da un trattino (`-`). Quindi, invece di avere una lunga stringa ininterrotta di caratteri, la dividiamo in blocchi più corti. Questa pratica è comune per i numeri di carta di credito o di telefono e si applica anche in questo caso per facilitare la verifica. Così, ad esempio, si può dire a un utente o a un partner: "*Per favore, controlla che il terzo blocco sia `9GEgnyMj7`*", invece di doverlo confrontare tutto in una volta. L'ultimo blocco è spesso usato come **checksum**, per avere un sistema di rilevamento degli errori o dei refusi.

Ad esempio, un `ContractId` in base58 codificato e segmentato potrebbe essere :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Ognuno dei trattini spezza la stringa in sezioni. Questo non influisce sulla semantica del codice, ma solo sulla sua presentazione.

#### Utilizzo di URL per le fatture

Una fattura RGB viene presentata come un URL. Ciò significa che può essere cliccata o scansionata (come un codice QR) e un portafoglio può interpretarla direttamente per effettuare una transazione. Questa semplicità di interazione è diversa da quella di altri sistemi in cui è necessario copiare e incollare vari dati nei diversi campi del software.

Una fattura per un token fungibile (ad esempio un token RGB20) potrebbe avere il seguente aspetto:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Analizziamo questo URL:


- `rgb:`** (prefisso): indica un collegamento che invoca il protocollo RGB (analogo a `http:` o `bitcoin:` in altri contesti);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: rappresenta il `ContractId` del token che si vuole manipolare;
- `/RGB20/100`**: indica che viene utilizzata l'interfaccia `RGB20` e che vengono richieste 100 unità dell'asset. La sintassi è: `/Interface/amount` ;
- `+utxob:`**: specifica che vengono aggiunte informazioni sull'UTXO ricevente (o, più precisamente, sulla definizione del sigillo monouso);
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: questo è l'UTXO *blindato* (o definizione di sigillo). In altre parole, Bob ha mascherato il suo UTXO esatto, quindi il mittente (Alice) non sa quale sia l'indirizzo esatto. Sa solo che esiste un sigillo valido che si riferisce a un UTXO controllato da Bob.

Il fatto che tutto rientri in un unico URL semplifica la vita dell'utente: un semplice clic o una scansione nel portafoglio e l'operazione è pronta per essere eseguita.

Si potrebbero immaginare sistemi in cui al posto del `ContractId` si utilizzi un semplice ticker (ad esempio `USDT`). Tuttavia, questo solleverebbe grossi problemi di fiducia e sicurezza: un ticker non è un riferimento univoco (diversi contratti potrebbero affermare di chiamarsi `USDT`). Con RGB, vogliamo un identificatore crittografico unico e non ambiguo. Da qui l'adozione della stringa a 256 bit, codificata in base58 e segmentata. L'utente sa che sta manipolando proprio il contratto il cui ID è `2WBcas9-yjz...` e non un altro.

#### Parametri URL aggiuntivi

È inoltre possibile aggiungere ulteriori parametri all'URL, come nel caso di HTTP, ad esempio :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: rappresenta, ad esempio, una firma associata alla fattura, che alcuni portafogli possono verificare;
- Se un portafoglio non gestisce questa firma, ignora semplicemente questo parametro.

Prendiamo il caso di un NFT tramite l'interfaccia RGB21. Ad esempio, potremmo avere :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Qui vediamo :


- `rgb:`**: Prefisso URL ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: ID contratto (NFT) ;
- rGB21**: interfaccia per beni non fungibili (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: un riferimento esplicito alla parte unica dell'NFT, ad esempio un hash del blob di dati (media, metadati...) ;
- `+utxob:egXsFnw-...`**: la definizione del sigillo.

L'idea è la stessa: trasmettere un link unico che il portafoglio possa interpretare, identificando chiaramente l'asset unico da trasferire.

#### Altre operazioni tramite URL

Gli URL RGB non sono utilizzati solo per richiedere un trasferimento. Possono anche codificare operazioni più avanzate, come l'emissione di nuovi token (*emissione*). Ad esempio:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Qui troviamo :


- `rgb:` : protocollo ;
- `2WBcas9-...`: ID contratto ;
- `/RGB20/issue/100000`: indica che si vuole invocare la transizione "*Issue*" per creare altri 100.000 gettoni;
- `+utxob:`: la definizione del sigillo.

Ad esempio, il portafoglio potrebbe recitare: "Mi è stato chiesto di effettuare un'operazione di `emissione` dall'interfaccia `RGB20`, su tale e tale contratto, per 100.000 unità, a beneficio di tale e tale Sigillo monouso.*"

Dopo aver esaminato gli elementi principali della programmazione RGB, nel prossimo capitolo vi illustrerò come redigere un contratto RGB.

## Redazione di contratti intelligenti

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

In questo capitolo, affronteremo passo dopo passo la scrittura di un contratto, utilizzando lo strumento a riga di comando `rgb`. L'obiettivo è mostrare come installare e manipolare la CLI, compilare uno **Schema**, importare l'**Interfaccia** e l'**Implementazione dell'interfaccia**, quindi emettere (*emettere*) una risorsa. Verrà esaminata anche la logica sottostante, compresa la compilazione e la convalida dello stato. Alla fine di questo capitolo, dovreste essere in grado di riprodurre il processo e creare i vostri contratti RGB.

Come promemoria, la logica interna di RGB è basata su librerie Rust che voi, come sviluppatori, potete importare nei vostri progetti per gestire la parte di validazione lato client. Inoltre, il team dell'associazione LNP/BP sta lavorando a legami per altre lingue, ma non sono ancora stati finalizzati. Inoltre, altre entità come Bitfinex stanno sviluppando i propri stack di integrazione (ne parleremo negli ultimi due capitoli del corso). Per il momento, quindi, la CLI `rgb` è il riferimento ufficiale, anche se rimane relativamente poco rifinita.

### Installazione e presentazione dello strumento rgb

Il comando principale si chiama semplicemente `rgb`. È stato progettato per ricordare `git`, con una serie di sottocomandi per manipolare i contratti, invocarli, emettere beni e così via. Bitcoin Wallet non è attualmente integrato, ma lo sarà in una prossima versione (0.11). Questa prossima versione consentirà agli utenti di creare e gestire i loro portafogli (tramite descrittori) direttamente da `rgb`, compresa la generazione di PSBT, la compatibilità con l'hardware esterno (ad esempio un portafoglio hardware) per la firma e l'interoperabilità con software come Sparrow. Questo semplificherà l'intero scenario di emissione e trasferimento degli asset.

#### Installazione tramite Cargo

Installiamo lo strumento in Rust con :

```bash
cargo install rgb-contracts --all-features
```

(Nota: il crate si chiama `rgb-contracts` e il comando installato si chiamerà `rgb`. Se esisteva già un crate chiamato `rgb`, potrebbe esserci stata una collisione, da cui il nome)

L'installazione compila un gran numero di dipendenze (ad esempio, parsing dei comandi, integrazione di Electrum, gestione delle prove a conoscenza zero, ecc.)

Una volta completata l'installazione, il file :

```bash
rgb
```

L'esecuzione di `rgb` (senza argomenti) visualizza un elenco di sottocomandi disponibili, come `interfacce`, `schema`, `importazione`, `esportazione`, `emissione`, `fattura`, `trasferimento`, ecc. È possibile modificare la directory di archiviazione locale (una riserva che contiene tutti i log, gli schemi e le implementazioni), scegliere la rete (testnet, mainnet) o configurare il server Electrum.

![RGB-Bitcoin](assets/fr/081.webp)

#### Prima panoramica dei controlli

Eseguendo il seguente comando, si noterà che un'interfaccia `RGB20` è già integrata per impostazione predefinita:

```bash
rgb interfaces
```

Se questa interfaccia non è integrata, clonare il file :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compilare:

```bash
cargo run
```

Importare quindi l'interfaccia scelta:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

D'altra parte, ci viene detto che nessuno schema è stato ancora importato nel software. Non c'è nemmeno un contratto nella scorta. Per vederlo, eseguire il comando :

```bash
rgb schemata
```

È quindi possibile clonare il repository per recuperare determinati schemi:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

Questo repository contiene, nella sua directory `src/`, diversi file Rust (per esempio `nia.rs`) che definiscono gli schemi (NIA per "*Non Inflatable Asset*", UDA per "*Unique Digital Asset*", ecc.) Per la compilazione, è possibile eseguire :

```bash
cd rgb-schemata
cargo run
```

Questo genera diversi file `.rgb` e `.rgba` corrispondenti agli schemi compilati. Ad esempio, si trova `NonInflatableAsset.rgb`.

#### Importazione dello schema e dell'implementazione dell'interfaccia

Ora è possibile importare lo schema in `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Questo lo aggiunge allo stash locale. Se si esegue il comando seguente, si vede che ora lo schema appare:

```bash
rgb schemata
```

### Creazione del contratto (emissione)

Esistono due approcci per creare una nuova risorsa:


- Si utilizza uno script o del codice in Rust che costruisce un Contratto popolando i campi dello schema (stato globale, stati posseduti, ecc.) e produce un file `.rgb` o `.rgba`;
- Oppure si può usare direttamente il sottocomando `issue`, con un file YAML (o TOML) che descrive le proprietà del token.

Nella cartella `examples` si possono trovare degli esempi in Rust, che illustrano come costruire un `ContractBuilder`, compilare lo `stato globale` (nome dell'asset, ticker, fornitura, data, ecc.), definire lo Stato di proprietà (a quale UTXO è assegnato), quindi compilare il tutto in una *partita di contratto* che si può esportare, convalidare e importare in uno stash.

L'altro modo è quello di modificare manualmente un file YAML per personalizzare il `ticker`, il `nome`, la `fornitura` e così via. Supponiamo che il file si chiami `RGB20-demo.yaml`. È possibile specificare :


- `spec`: ticker, nome, precisione ;
- `terms`: un campo per le note legali ;
- `issuedSupply` : la quantità di token emessi;
- `assegnazioni`: indica il sigillo monouso (*definizione del sigillo*) e la quantità sbloccata.

Ecco un esempio di file YAML da creare:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Quindi è sufficiente eseguire il comando :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

Nel mio caso, l'identificatore unico dello schema (da racchiudere tra virgolette singole) è `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` e non ho inserito alcun emittente. Quindi il mio ordine è :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Se non si conosce l'ID dello schema, eseguire il comando :

```bash
rgb schemata
```

La CLI risponde che un nuovo contratto è stato emesso e aggiunto allo stash. Se digitiamo il comando seguente, vediamo che ora c'è un contratto aggiuntivo, corrispondente a quello appena emesso:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Quindi, il comando successivo visualizza gli stati globali (nome, ticker, fornitura...) e l'elenco degli Stati posseduti, cioè le allocazioni (ad esempio, 1 milione di gettoni `PBN` definiti in UTXO `b449fea3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Esportazione, importazione e convalida

Per condividere questo contratto con altri utenti, è possibile esportarlo dallo stash in un file :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

Il file `myContractPBN.rgb` può essere passato a un altro utente, che può aggiungerlo alla sua scorta con il comando :

```bash
rgb import myContractPBN.rgb
```

Al momento dell'importazione, se si tratta di una semplice *partita di contratto*, si otterrà un messaggio "Importazione della partita rgb". Se si tratta di una partita *di transizione di stato* più grande, il comando sarà diverso (`rgb accept`).

Per garantire la validità, si può anche utilizzare la funzione di validazione locale. Ad esempio, si può eseguire :

```bash
rgb validate myContract.rgb
```

#### Utilizzo, verifica e visualizzazione dello Stash

Come promemoria, lo stash è un inventario locale di schemi, interfacce, implementazioni e contratti (Genesis + transizioni). Ogni volta che si esegue "import", si aggiunge un elemento allo stash. Questo stash può essere visualizzato in dettaglio con il comando :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Questo genererà una cartella con i dettagli dell'intera scorta.

### Trasferimento e PSBT

Per effettuare un trasferimento, è necessario manipolare un portafoglio Bitcoin locale per gestire gli impegni `Tapret` o `Opret`.

#### Generare una fattura

Nella maggior parte dei casi, l'interazione tra i partecipanti a un contratto (ad esempio, Alice e Bob) avviene attraverso la generazione di una fattura. Se Alice vuole che Bob esegua qualcosa (un trasferimento di token, una riemissione, un'azione in un DAO, ecc.), Alice crea una fattura che dettaglia le sue istruzioni a Bob. Quindi abbiamo :


- Alice** (l'emittente della fattura) ;
- Bob** (che riceve ed esegue la fattura).

A differenza di altri ecosistemi, una fattura RGB non si limita alla nozione di pagamento. Può incorporare qualsiasi richiesta legata al contratto: revocare una chiave, votare, creare un'incisione (*incisione*) su un NFT, ecc. L'operazione corrispondente può essere descritta nell'interfaccia del contratto. L'operazione corrispondente può essere descritta nell'interfaccia del contratto.

Il comando seguente genera una fattura RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Con :


- `$CONTRATTO`: Identificatore contratto (*ContractId*) ;
- `$INTERFACE`: l'interfaccia da utilizzare (ad es. `RGB20`) ;
- `$ACTION`: il nome dell'operazione specificata nell'interfaccia (per un semplice trasferimento di token fungibili, potrebbe essere "Transfer"). Se l'interfaccia fornisce già un'azione predefinita, non è necessario inserirla di nuovo qui;
- `$STATE`: i dati di stato da trasferire (ad esempio, una quantità di gettoni se viene trasferito un gettone fungibile);
- `$SEAL`: il sigillo monouso del beneficiario (Alice), cioè un riferimento esplicito a un UTXO. Bob utilizzerà queste informazioni per costruire la transazione testimone e l'output corrispondente apparterrà ad Alice (in forma *blindata UTXO* o non criptata).

Ad esempio, con i seguenti comandi

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

La CLI genererà una fattura come :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Può essere trasmesso a Bob tramite qualsiasi canale (testo, codice QR, ecc.).

#### Effettuare un trasferimento

Per trasferire da questa fattura :


- Bob (che detiene i token nella sua scorta) ha un portafoglio Bitcoin. Deve preparare una transazione Bitcoin (sotto forma di PSBT, ad esempio `tx.psbt`) che spende gli UTXO in cui si trovano i token RGB richiesti, più un UTXO per la valuta (scambio);
- Bob esegue il seguente comando:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Questo genera un file `consignment.rgb` che contiene :
 - La storia della transizione dimostra ad Alice che i gettoni sono autentici;
 - La nuova transizione che trasferisce i gettoni al Sigillo monouso di Alice ;
 - Una transazione testimone (non firmata).
- Bob invia questo file `consignment.rgb` ad Alice (tramite e-mail, un server di condivisione o un protocollo RGB-RPC, Storm, ecc;)
- Alice riceve `consignment.rgb` e lo accetta nel proprio stash :

```bash
alice$ rgb accept consignment.rgb
```


- La CLI controlla la validità della transizione e la aggiunge allo stash di Alice. Se non è valido, il comando fallisce con messaggi di errore dettagliati. Altrimenti, ha successo e segnala che la transazione campione non è ancora stata trasmessa sulla rete Bitcoin (Bob sta aspettando il via libera di Alice);
- A titolo di conferma, il comando `accept` restituisce una firma (*pagina*) che Alice può inviare a Bob per dimostrargli di aver convalidato l'*incarico* ;
- Bob può quindi firmare e pubblicare (`-publish`) la sua transazione Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Non appena la transazione viene confermata sulla catena, la proprietà dell'asset viene considerata trasferita ad Alice. Il portafoglio di Alice, che sta monitorando il mining della transazione, vede apparire il nuovo Stato di proprietà nella sua scorta.

Nel prossimo capitolo vedremo da vicino l'integrazione di RGB nella rete Lightning.

## RGB sulla rete Lightning

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

In questo capitolo propongo di esaminare come RGB possa essere utilizzato all'interno della Lightning Network, per integrare e muovere asset RGB (token, NFT, ecc.) attraverso canali di pagamento fuori dalla catena.

L'idea di base è che la transizione di stato RGB (*Transizione di stato*) può essere impegnata in una transazione Bitcoin che, a sua volta, può rimanere fuori dalla catena fino alla chiusura del canale Lightning. Quindi, ogni volta che il canale viene aggiornato, una nuova transizione di stato RGB può essere incorporata nella nuova transazione impegnata, che invalida la vecchia transizione. In questo modo, i canali Lightning possono essere utilizzati per trasferire beni RGB e possono essere instradati nello stesso modo dei pagamenti Lightning convenzionali.

### Creazione di canali e finanziamenti

Per creare un canale Lightning che trasporta risorse RGB, abbiamo bisogno di due elementi:


- Finanziamento Bitcoin per creare il multisig del canale 2/2 (l'UTXO di base per il canale);
- Finanziamento RGB, che invia le risorse allo stesso multisig.

In termini di Bitcoin, la transazione di finanziamento deve esistere per definire l'UTXO di riferimento, anche se contiene solo una piccola quantità di sats (si tratta solo di far sì che ogni uscita nelle future transazioni di impegno rimanga comunque al di sopra del limite di polvere). Ad esempio, Alice potrebbe decidere di fornire 10k sats e 500 USDT (emessi come asset RGB). Nella transazione di finanziamento, aggiungiamo un impegno (`Opret` o `Tapret`) che fissa la transizione di stato di RGB.

![RGB-Bitcoin](assets/fr/091.webp)

Una volta che la transazione di finanziamento è stata preparata (ma non ancora trasmessa), vengono create transazioni di impegno in modo che una delle parti possa chiudere il canale unilateralmente in qualsiasi momento. Queste transazioni assomigliano alle transazioni di impegno classiche di Lightning, tranne per il fatto che aggiungiamo un'uscita supplementare contenente l'ancora RGB (OP_RETURN o Taproot) legata alla nuova transizione di stato.

La transizione di stato RGB sposta quindi le attività dal multisigma 2/2 del finanziamento agli output della transazione di impegno. Il vantaggio di questo processo è che la sicurezza dello stato RGB corrisponde esattamente alla meccanica punitiva di Lightning: se Bob trasmette uno stato di canale vecchio, Alice può punirlo e spendere l'output, per recuperare sia la saturazione che i gettoni RGB. L'incentivo è quindi ancora più forte che in un canale Lightning senza risorse RGB, poiché un attaccante può perdere non solo la saturazione, ma anche le risorse RGB del canale.

Una transazione di impegno firmata da Alice e inviata a Bob avrebbe quindi il seguente aspetto:

![RGB-Bitcoin](assets/fr/092.webp)

La transazione di impegno che la accompagna, firmata da Bob e inviata ad Alice, avrà il seguente aspetto:

![RGB-Bitcoin](assets/fr/093.webp)

### Aggiornamento del canale

Quando si verifica un pagamento tra due partecipanti al canale (o questi desiderano modificare l'allocazione delle attività), essi creano una nuova coppia di transazioni di impegno. L'importo in sats di ciascuna uscita può rimanere invariato o meno, a seconda dell'implementazione, poiché il suo ruolo principale è quello di consentire la costruzione di UTXO validi. D'altra parte, l'uscita OP_RETURN (o Taproot) deve essere modificata per contenere la nuova ancora RGB, che rappresenta la nuova distribuzione degli asset nel canale.

Ad esempio, se Alice trasferisce 30 USDT a Bob nel canale, la nuova transizione di stato rifletterà un saldo di 400 USDT per Alice e 100 USDT per Bob. La transazione di commit viene aggiunta (o modificata) all'ancora OP_RETURN/Taproot per includere questa transizione. Si noti che, dal punto di vista di RGB, l'input della transizione rimane il multisig iniziale (dove le attività sulla catena sono effettivamente allocate fino alla chiusura del canale). Solo le uscite di RGB (allocazioni) cambiano, a seconda della ridistribuzione decisa.

La transazione di impegno firmata da Alice, pronta per essere distribuita da Bob :

![RGB-Bitcoin](assets/fr/094.webp)

La transazione di impegno firmata da Bob, pronta per essere distribuita da Alice :

![RGB-Bitcoin](assets/fr/095.webp)

### Gestione HTLC

In realtà, la rete Lightning consente di instradare i pagamenti attraverso più canali, utilizzando gli HTLC (*Hashed Time-Locked Contracts*). È la stessa cosa con RGB: per ogni pagamento in transito attraverso il canale, viene aggiunto un output HTLC alla transazione che lo impegna e un'allocazione RGB collegata a questo HTLC. In questo modo, chi spende l'uscita HTLC (grazie al segreto o dopo la scadenza del timelock) recupera sia la saturazione che gli asset RGB associati. D'altra parte, è ovviamente necessario avere abbastanza denaro in circolazione sia in termini di sats che di asset RGB.

![RGB-Bitcoin](assets/fr/096.webp)

Il funzionamento di RGB su Lightning deve quindi essere considerato in parallelo a quello della rete Lightning stessa. Se volete approfondire questo argomento, vi consiglio di dare un'occhiata a questo altro corso di formazione completo:

https://planb.network/courses/lnp201
### Mappa del codice RGB

Infine, prima di passare alla sezione successiva, vorrei fornire una panoramica del codice utilizzato in RGB. Il protocollo si basa su un insieme di librerie Rust e di specifiche open source. Ecco una panoramica dei principali repository e crate:

![RGB-Bitcoin](assets/fr/097.webp)

#### Convalida lato client


- Repository**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Casse** : [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Gestione della convalida fuori catena e della logica dei sigilli monouso.

#### Impegni deterministici di Bitcoin (DBC)


- Repository**: [bp-core](https://github.com/BP-WG/bp-core)
- Cassa**: [bp-dbc](https://crates.io/crates/bp-dbc)

Gestione dell'ancoraggio deterministico nelle transazioni Bitcoin (Tapret, OP_RETURN, ecc.).

#### Impegno multiprotocollo (MPC)


- Repository**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Cassa** : [commit_verify](https://crates.io/crates/commit_verify)

Combinazioni di ingaggio multiple e integrazione con diversi protocolli.

#### Tipi rigorosi e codifica rigorosa


- Specifiche**: [sito web strict-types.org](https://www.strict-types.org/)
- Repository**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Casse** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Il sistema di tipizzazione rigoroso e la serializzazione deterministica utilizzati per la validazione lato client.

#### Nucleo RGB


- Repository**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Cassa**: [rgb-core](https://crates.io/crates/rgb-core)

Il cuore del protocollo, che racchiude la logica principale della convalida RGB.

#### Libreria e portafoglio standard RGB


- Repository**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Cassa** : [rgb-std](https://crates.io/crates/rgb-std)

Implementazioni standard, gestione di stash e portafogli.

#### RGB CLI


- Repository**: [rgb](https://github.com/RGB-WG/rgb)
- Casse**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

La CLI `rgb` e il crate wallet, per la manipolazione dei contratti a riga di comando.

#### Schema RGB


- Repository**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Contiene esempi di schemi (NIA, UDA, ecc.) e delle loro implementazioni.

#### ALuVM


- Info** : [aluvm.org](https://www.aluvm.org/)
- Repository**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Casse**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Macchina virtuale basata sul registro utilizzata per eseguire gli script di convalida.

#### Protocollo Bitcoin - BP


- Repository** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Componenti aggiuntivi per il supporto del protocollo Bitcoin (transazioni, bypass, ecc.).

#### Calcolo deterministico ubiquo - UBIDECO


- Repository**: [UBIDECO](https://github.com/UBIDECO)

Ecosistema legato agli sviluppi deterministici open-source.

# Costruire su RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA e il progetto Bitmask

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

Questa sezione finale del corso si basa sulle presentazioni fatte da vari relatori al bootcamp RGB. Include testimonianze e riflessioni su RGB e sul suo ecosistema, nonché presentazioni di strumenti e progetti basati sul protocollo. Questo primo capitolo è moderato da Hunter Beast e i due successivi da Frederico Tenga.

### Da JavaScript a Rust e all'ecosistema Bitcoin

All'inizio, Hunter Beast lavorava principalmente in JavaScript. Poi ha scoperto **Rust**, la cui sintassi all'inizio sembrava poco attraente e frustrante. Tuttavia, ha imparato ad apprezzare la potenza del linguaggio, il controllo sulla memoria (*heap* e *stack*), la sicurezza e le prestazioni che ne derivano. Sottolinea che Rust è un'eccellente palestra per comprendere a fondo il funzionamento di un computer.

Hunter Beast racconta il suo passato in vari progetti dell'ecosistema *altcoin*, come Ethereum (con Solidity, TypeScript, ecc.) e successivamente Filecoin. Spiega di essere stato inizialmente colpito da alcuni protocolli, ma di aver finito per sentirsi disilluso dalla maggior parte di essi, non da ultimo a causa della loro tokenomica. Denuncia i dubbi incentivi finanziari, la creazione inflazionistica di token che diluisce gli investitori e l'aspetto potenzialmente di sfruttamento di questi progetti. Ha quindi finito per adottare una posizione **Bitcoin massimalista**, anche perché alcune persone gli hanno aperto gli occhi sui meccanismi economici più solidi del Bitcoin e sulla solidità di questo sistema.

### Il fascino dell'RGB e della costruzione su livelli

Ciò che lo ha definitivamente convinto della rilevanza di Bitcoin, secondo le sue parole, è stata la scoperta di RGB e del concetto di livelli. Ritiene che le funzionalità esistenti su altre blockchain possano essere riprodotte su livelli superiori, al di sopra del Bitcoin, senza alterare il protocollo di base.

Nel febbraio 2022, si è unito a **DIBA** per lavorare specificamente su RGB, e in particolare sul portafoglio **Bitmask**. All'epoca, Bitmask era ancora alla versione 0.01 e RGB girava alla versione 0.4, solo per la gestione di singoli token. Egli osserva che questo sistema era meno orientato all'autocustodia rispetto a quello attuale, in quanto la logica era in parte basata su server. Da allora, l'architettura si è evoluta verso questo modello, molto apprezzato dai bitcoiners.

### Le basi del protocollo RGB

Il protocollo **RGB** è l'incarnazione più recente e più avanzata del concetto di _monete colorate_, già esplorato intorno al 2012-2013. All'epoca, diversi team stavano cercando di associare diversi valori di bitcoin agli UTXO, il che ha portato a molteplici implementazioni sparse. Questa mancanza di standardizzazione e la scarsa domanda dell'epoca hanno impedito a queste soluzioni di prendere piede in modo duraturo.

Oggi, RGB si distingue per la sua solidità concettuale e per le specifiche unificate tramite l'associazione LNP/BP. Il principio si basa sulla validazione lato client. La blockchain Bitcoin memorizza solo gli impegni crittografici (_commitments_, tramite Taproot o OP_RETURN), mentre la maggior parte dei dati (definizioni dei contratti, cronologia dei trasferimenti, ecc.) viene memorizzata dagli utenti interessati. In questo modo, il carico di archiviazione è distribuito e la riservatezza degli scambi è rafforzata, senza appesantire la blockchain. Questo approccio consente di creare asset fungibili (standard **RGB20**) o unici (standard **RGB21**), in un quadro modulare e scalabile.

### La funzione token (RGB20) e gli asset unici (RGB21)

Con **RGB20**, definiamo un token fungibile su Bitcoin. L'emittente sceglie una _fornitura_, una _precisione_ e crea un _contratto_ in cui può poi effettuare trasferimenti. Ogni trasferimento è riferito a un Bitcoin UTXO, che funge da *sigillo monouso*. Questa logica garantisce che l'utente non possa spendere due volte lo stesso bene, poiché solo la persona in grado di spendere l'UTXO possiede la chiave per aggiornare lo stato del contratto lato client.

**RGB21** si rivolge ad asset unici (o "NFT"). L'asset ha una fornitura pari a 1 e può essere associato a metadati (file immagine, audio, ecc.) descritti tramite un campo specifico. A differenza degli NFT sulle blockchain pubbliche, i dati e i loro identificatori MIME possono rimanere privati, distribuiti peer-to-peer a discrezione del proprietario.

### La soluzione Bitmask: un portafoglio per RGB

Per sfruttare le capacità di RGB nella pratica, il progetto **DIBA** ha progettato un portafoglio chiamato [Bitmask](https://bitmask.app/). L'idea è quella di fornire uno strumento non custodiale, basato su Taproot, accessibile come applicazione web o estensione del browser. Bitmask gestisce beni sia RGB20 che RGB21 e integra diversi meccanismi di sicurezza:


- Il codice principale è scritto in Rust, quindi compilato in WebAssembly per essere eseguito in un ambiente JavaScript (React);
- Le chiavi vengono generate localmente e poi conservate crittografate localmente;
- I dati di stato (stash) sono conservati in memoria, serializzati e crittografati tramite la libreria **Carbonado**, che esegue la compressione, la correzione degli errori, la crittografia e la verifica del flusso utilizzando Blake3.

Grazie a questa architettura, tutte le transazioni di asset avvengono sul lato client. Dall'esterno, la transazione Bitcoin non è altro che una classica transazione di spesa Taproot, che nessuno sospetterebbe essere anche un trasferimento di token fungibili o NFT. L'assenza di sovraccarico sulla catena (nessun metadato memorizzato pubblicamente) garantisce un certo grado di discrezione e rende più facile resistere a eventuali tentativi di censura.

### Sicurezza e architettura distribuita

Poiché il protocollo RGB richiede che ogni partecipante conservi la cronologia delle transazioni (per dimostrare la validità dei trasferimenti ricevuti), si pone la questione dell'archiviazione. Bitmask propone di serializzare questa scorta a livello locale, per poi inviarla a diversi server o cloud (facoltativi). I dati rimangono criptati dall'utente tramite **Carbonado**, quindi un server non può leggerli. In caso di corruzione parziale, il livello di correzione degli errori può ricostituire il contenuto.

L'uso di CRDT (_Conflict-free replicated data type_) consente di unire diverse versioni dello stash, qualora dovessero divergere. Ognuno è libero di ospitare questi dati dove vuole, poiché nessun singolo nodo completo contiene tutte le informazioni legate alla risorsa. Questo riflette esattamente la filosofia della *convalida lato cliente*, in cui ogni proprietario è responsabile della conservazione delle prove della validità della propria risorsa RGB.

### Verso un ecosistema più ampio: mercato, interoperabilità e nuove funzioni

L'azienda che sta dietro a Bitmask non si limita al semplice sviluppo di un portafoglio. DIBA intende sviluppare :


- Un **mercato** per lo scambio di gettoni, in particolare in forma **RGB21**;
- Compatibilità con altri portafogli (come *Iris Wallet*);
- Tecniche di batching** dei trasferimenti, ovvero la possibilità di includere diversi trasferimenti RGB successivi in un'unica transazione.

Allo stesso tempo, stiamo lavorando a **WebBTC** o **WebLN** (standard che consentono ai siti web di chiedere al portafoglio di firmare le transazioni Bitcoin o Lightning), nonché alla possibilità di "teleburnare" le voci Ordinals (se vogliamo rimpatriare gli Ordinals in un formato RGB più discreto e flessibile).

### Conclusione

L'intero processo mostra come l'ecosistema RGB possa essere implementato e reso accessibile agli utenti finali attraverso solide soluzioni tecniche. Il passaggio da una prospettiva altcoin a una visione più Bitcoin-centrica, insieme alla scoperta della *Client-side Validation*, illustra un percorso abbastanza logico: abbiamo capito che è possibile implementare varie funzionalità (token fungibili, NFT, smart contract...) senza biforcare la blockchain, semplicemente sfruttando gli impegni crittografici sulle transazioni Taproot o OP_RETURN.

Il portafoglio **Bitmask** fa parte di questo approccio: dal lato della blockchain, tutto ciò che si vede è una normale transazione Bitcoin; dal lato dell'utente, si manipola un'interfaccia web in cui si creano, si scambiano e si memorizzano tutti i tipi di asset fuori dalla catena. Questo modello dissocia chiaramente l'infrastruttura monetaria (Bitcoin) dalla logica di emissione e trasferimento (RGB), garantendo al contempo un elevato livello di riservatezza e una migliore scalabilità.

## Il lavoro di Bitfinex su RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

In questo capitolo, basato su una presentazione di Frederico Tenga, esaminiamo una serie di strumenti e progetti creati dal team di Bitfinex dedicati a RGB, con l'obiettivo di favorire la nascita di un ecosistema ricco e diversificato intorno a questo protocollo. L'obiettivo iniziale del team non è quello di rilasciare un prodotto commerciale specifico, ma piuttosto di fornire blocchi software, contribuire al protocollo RGB stesso e proporre riferimenti concreti di implementazione come un portafoglio mobile (*Iris Wallet*) o un nodo Lightning compatibile con RGB.

### Contesto e obiettivi

Dal 2022 circa, il team Bitfinex RGB si è concentrato sullo sviluppo dello stack tecnologico che consente di sfruttare e testare RGB in modo efficiente. Sono stati apportati diversi contributi:


- Partecipazione alle specifiche del codice sorgente e del protocollo, compresa la scrittura di proposte di miglioramento, la correzione di bug, ecc;
- Strumenti per gli sviluppatori per semplificare l'integrazione di RGB nelle loro applicazioni;
- Progettazione di un portafoglio mobile chiamato [Iris](https://iriswallet.com/) per sperimentare e illustrare le migliori pratiche per l'utilizzo di RGB ;
- Creazione di un nodo Lightning personalizzato, in grado di gestire canali con asset RGB;
- Sostenere altri team che costruiscono soluzioni su RGB, per incoraggiare la diversità e un forte ecosistema.

Questo approccio mira a coprire l'intera catena di esigenze: dalla libreria di basso livello (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), che consente l'implementazione di un portafoglio, all'aspetto produttivo (un nodo Lightning, un portafoglio per Android, ecc.).

### La libreria RGBlib: semplificazione dello sviluppo di applicazioni RGB

Un punto importante per democratizzare la creazione di portafogli e applicazioni RGB è quello di rendere disponibile un'astrazione abbastanza semplice in modo che gli sviluppatori non debbano imparare tutto sulla logica interna del protocollo. Questo è proprio l'obiettivo di **RGBlib**, scritto in Rust.

RGBlib funge da ponte tra i requisiti altamente flessibili (ma talvolta complessi) di RGB che abbiamo avuto modo di studiare nei capitoli precedenti e le esigenze concrete di uno sviluppatore di applicazioni. In altre parole, un portafoglio (o un servizio) che voglia gestire trasferimenti di token, emissione di asset, verifica, ecc. può affidarsi a RGBlib senza conoscere ogni dettaglio crittografico o ogni parametro RGB personalizzabile.

La libreria offre :


- Funzioni chiavi in mano per l'emissione (_emissione_) di beni (fungibili o meno);
- La capacità di trasferire (inviare/ricevere) attività manipolando semplici oggetti (indirizzi, importi, UTXO, ecc.);
- Un meccanismo per memorizzare e caricare le informazioni di stato (*conferme*) necessarie per la convalida lato client.

RGBlib si basa quindi su nozioni complesse specifiche di RGB (Client-side Validation, ancore Tapret/Opret), ma le incapsula in modo che l'applicazione finale non debba riprogrammare tutto o prendere decisioni rischiose. Inoltre, RGBlib è già legato a diversi linguaggi (Kotlin e Python), aprendo la porta a usi che vanno oltre il semplice universo di Rust.

### Iris Wallet: un esempio di portafoglio RGB su Android

Per dimostrare l'efficacia di RGBlib, il team di Bitfinex ha sviluppato **Iris Wallet**, per ora esclusivamente su Android. Si tratta di un portafoglio mobile che illustra un'esperienza d'uso simile a quella di un normale portafoglio Bitcoin: è possibile emettere un asset, inviarlo, riceverlo e visualizzarne la cronologia, rimanendo su un modello di autodeposito.

Iris presenta una serie di caratteristiche interessanti:

**Utilizzando un server Electrum:**

Come ogni portafoglio, Iris ha bisogno di conoscere le conferme delle transazioni sulla blockchain. Piuttosto che incorporare un nodo completo, Iris utilizza per default un server Electrum gestito dal team di Bitfinex. Gli utenti possono tuttavia configurare il proprio server o un altro servizio di terze parti. In questo modo, le transazioni Bitcoin possono essere convalidate e le informazioni recuperate (indicizzazione) in modo modulare.

**Il server proxy RGB:**

A differenza di Bitcoin, RGB richiede lo scambio di metadati fuori catena (*conferimenti*) tra mittente e destinatario. Per semplificare questo processo, Iris offre una soluzione in cui la comunicazione avviene tramite un server proxy. Il portafoglio ricevente genera una *fattura* che indica dove il mittente deve inviare i dati *sul lato cliente*. Per impostazione predefinita, l'URL punta a un proxy ospitato dal team Bitfinex, ma è possibile cambiare questo proxy (o ospitarne uno proprio). L'idea è quella di tornare a un'esperienza utente familiare in cui il destinatario visualizza un codice QR e il mittente lo scansiona per effettuare la transazione, senza complesse manipolazioni aggiuntive.

**Backup continuo

In un contesto strettamente Bitcoin, il backup del seme è generalmente sufficiente (anche se al giorno d'oggi si consiglia di eseguire il backup del seme e dei descrittori). Con RGB, questo non è sufficiente: è necessario conservare anche la storia locale (i *conferimenti*) che dimostra che si possiede davvero un asset RGB. Ogni volta che si riceve una ricevuta, il dispositivo memorizza nuovi dati, essenziali per le spese successive. Iris gestisce automaticamente un backup criptato nel Google Drive dell'utente. Questo non richiede una particolare fiducia in Google, poiché il backup è criptato, e per il futuro sono previste opzioni più robuste (come un server personale) per evitare qualsiasi rischio di censura o cancellazione da parte di un operatore terzo.

**Altre caratteristiche:**


- Create un rubinetto per testare o distribuire rapidamente i gettoni per la sperimentazione o la promozione;
- Un sistema di certificazione (attualmente centralizzato) per distinguere un token legittimo da uno falso che copia un famoso ticker. In futuro, questa certificazione potrebbe diventare più decentralizzata (tramite DNS o altri meccanismi).

Nel complesso, Iris offre un'esperienza d'uso vicina a quella di un portafoglio Bitcoin classico, mascherando la complessità aggiuntiva (gestione delle scorte, cronologia degli *incarichi*, ecc.) grazie a RGBlib e all'uso di un server proxy.

### Server proxy ed esperienza utente

Il server proxy introdotto in precedenza merita di essere illustrato in dettaglio, poiché è la chiave per un'esperienza utente senza problemi. Invece che il mittente debba trasmettere manualmente i *conferimenti* al destinatario, la transazione RGB avviene in background tramite un file :


- Il destinatario genera una *fattura* (contenente, tra l'altro, l'indirizzo del proxy);
- Il mittente invia (tramite una richiesta HTTP) un progetto di transizione (il *consignment*) al proxy ;
- Il destinatario recupera questo progetto, esegue la convalida *lato cliente* localmente;
- Il destinatario pubblica quindi, tramite il proxy, l'accettazione (o eventualmente il rifiuto) della transizione di stato;
- Il mittente può visualizzare lo stato di convalida e, se accettato, trasmettere la transazione Bitcoin finalizzando il trasferimento.

In questo modo, il portafoglio si comporta quasi come un normale portafoglio. L'utente non è a conoscenza di tutti i passaggi intermedi. Certo, il proxy attuale non è né crittografato né autenticato (il che lascia dubbi sulla riservatezza e l'integrità), ma questi miglioramenti sono possibili nelle versioni successive. Il concetto di proxy rimane estremamente utile per ricreare l'esperienza "io invio un codice QR, tu lo scansioni per pagare".

### Integrazione RGB sulla rete Lightning

Un altro punto chiave del lavoro del team di Bitfinex è quello di rendere la rete Lightning compatibile con gli asset RGB. L'obiettivo è quello di abilitare i canali Lightning in USDT (o qualsiasi altro token) e di beneficiare degli stessi vantaggi di bitcoin su Lightning (transazioni quasi istantanee, routing, ecc.). In concreto, si tratta di creare un nodo Lightning modificato in :


- Aprire un canale inserendo non solo i satoshi, ma anche uno o più asset RGB nel multisigma UTXO di finanziamento;
- Generare transazioni di impegno Lightning (lato Bitcoin) accompagnate dalle corrispondenti transizioni di stato RGB. Ogni volta che il canale viene aggiornato, una transizione RGB ridefinisce la distribuzione delle attività nelle uscite di Lightning;
- Abilitare la chiusura unilaterale, in cui il bene viene recuperato in un UTXO esclusivo, in conformità con le regole della rete Lightning (HTLC, timelock, punizione, ecc.).

Questa soluzione, denominata "**RGB Lightning Node**", utilizza LDK (*Lightning Dev Kit*) come base e aggiunge i meccanismi necessari per iniettare token RGB nei canali. Gli impegni di Lightning mantengono la struttura classica (uscite perforabili, timelock...), e in aggiunta ancorano una transizione di stato RGB (tramite `Opret` o `Tapret`). Per l'utente, questo apre la strada ai canali Lightning in stablecoin o in qualsiasi altro asset emesso via RGB.

### Potenziale di DEX e impatto su Bitcoin

Una volta che diversi asset sono gestiti tramite Lightning, diventa possibile immaginare uno **scambio atomico** su un singolo percorso di routing Lightning, utilizzando la stessa logica di segreti e timelock. Ad esempio, l'utente A possiede bitcoin su un canale Lightning e l'utente B possiede USDT RGB su un altro canale Lightning. Possono creare un percorso che colleghi i loro due canali e scambiare simultaneamente BTC con USDT, senza bisogno di fiducia. Questo non è altro che uno **scambio atomico** che si svolge in diversi hops, rendendo i partecipanti esterni quasi ignari del fatto che stanno effettuando uno scambio, non solo un instradamento. Questo approccio offre :


- Latenza molto bassa, in quanto tutto rimane fuori dalla catena su Lightning.
- Una **privacy** superiore: nessuno sa che si tratta di uno scambio e non di un normale routing;
- Evitare il frontrunning, un problema ricorrente per i DEX on-chain ;
- Costi ridotti (non si paga il blockspace, ma solo le tariffe di Lightning routing).

Possiamo quindi immaginare un ecosistema in cui i nodi Lightning offrono prezzi di scambio (fornendo liquidità). Ogni nodo, se lo desidera, può svolgere il ruolo di _market maker_, comprando e vendendo vari asset su Lightning. Questa prospettiva di un DEX _layer-2_ rafforza l'idea che non sia necessario effettuare fork o utilizzare blockchain di terze parti per ottenere scambi di asset decentralizzati.

L'impatto su Bitcoin potrebbe essere positivo: L'infrastruttura di Lightning (nodi, canali e servizi) sarebbe più utilizzata grazie ai volumi generati da queste *stablecoin*, derivati e altri token. I commercianti interessati ai pagamenti in USDT su Lightning scoprirebbero meccanicamente i pagamenti in BTC su Lightning (gestiti dallo stesso stack). Anche la manutenzione e il finanziamento dell'infrastruttura della rete Lightning potrebbero beneficiare della moltiplicazione di questi flussi non in BTC, a vantaggio indiretto degli utenti di Bitcoin.

### Conclusioni e risorse

Il team di Bitfinex dedicato a RGB illustra, attraverso il suo lavoro, la diversità di ciò che si può fare con il protocollo. Da un lato, c'è RGBlib, una libreria che facilita la progettazione di portafogli e applicazioni. Dall'altro, c'è Iris Wallet, una dimostrazione pratica su Android di un'ottima interfaccia per l'utente finale. Infine, l'integrazione di RGB con Lightning dimostra che i canali stablecoin sono possibili e apre la strada a un potenziale DEX decentralizzato su Lightning.

Questo approccio rimane in gran parte sperimentale e continua ad evolversi: la libreria RGBlib viene perfezionata man mano, Iris Wallet riceve miglioramenti regolari e il nodo Lightning dedicato non è ancora un client Lightning mainstream.

Per coloro che desiderano saperne di più o contribuire, sono disponibili diverse risorse, tra cui :


- [Repository GitHub RGB Tools](https://github.com/RGB-Tools);
- [Un sito informativo dedicato a Iris Wallet](https://iriswallet.com/) per testare il portafoglio su Android.

Nel prossimo capitolo vedremo più da vicino come lanciare un nodo RGB Lightning.

## RLN - Nodo fulmine RGB

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

In questo capitolo finale, Frederico Tenga vi guida passo dopo passo nella configurazione di un nodo Lightning RGB in un ambiente Regtest e vi mostra come creare token RGB su di esso. Avviando due nodi separati, scoprirete anche come aprire un canale Lightning tra di essi e scambiare asset RGB.

Questo video funge da esercitazione, simile a quella che abbiamo trattato in un capitolo precedente, ma questa volta è incentrato specificamente su Lightning!

La risorsa principale per questo video è il repository Github [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), che consente di lanciare facilmente questa configurazione in Regtest.

### Distribuzione di un nodo Lightning compatibile con RGB

Il processo riprende e mette in pratica tutti i concetti trattati nei capitoli precedenti:


- L'idea che **UTXO** bloccato su un multisig 2/2 di un canale Lightning possa ricevere non solo bitcoin, ma anche essere un sigillo monouso di asset RGB (fungibili o meno);
- L'aggiunta, in ogni operazione di Lightning engagement, di un'uscita (`Tapret` o `Opret`) dedicata all'ancoraggio della transizione di stato RGB;
- L'infrastruttura associata (bitcoind/indexer/proxy) per convalidare le transazioni Bitcoin e scambiare dati *sul lato cliente*.

### Introduzione del nodo rgb-lightning

Il progetto **`rgb-lightning-node`** è un demone Rust basato su un fork di `rust-lightning` (LDK) modificato per tenere conto dell'esistenza di asset RGB in un canale. Quando si apre un canale, è possibile specificare la presenza di asset e ogni volta che lo stato del canale viene aggiornato, viene creata una transizione RGB che riflette la distribuzione dell'asset nelle uscite di Lightning. Questo permette di :


- Aprire canali Lightning in USDT, ad esempio;
- Instradare questi gettoni attraverso la rete, a condizione che i percorsi di instradamento abbiano una liquidità sufficiente;
- Sfruttare la logica di punizione e di timelock di Lightning senza modifiche: basta ancorare la transizione RGB in un'uscita aggiuntiva della transazione di impegno.

Il codice è ancora in fase alfa: si consiglia di utilizzarlo solo in **regtest** o su **testnet**.

### Installazione dei nodi

Per compilare e installare il binario `rgb-lightning-node', si inizia clonando il repository e i suoi sottomoduli, quindi si esegue il comando :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- L'opzione `--recurse-submodules` clona anche i sottodispositivi necessari (compresa la versione modificata di `rust-lightning`);
- L'opzione `--shallow-submodules` limita la profondità del clone per accelerare il download, fornendo comunque l'accesso ai commit essenziali.

Dalla root del progetto, eseguire il seguente comando per compilare e installare il binario :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` assicura che la versione delle dipendenze sia rigorosamente rispettata;
- `--debug` non è obbligatorio, ma può aiutare a concentrarsi (si può usare `--release` se si preferisce);
- `-percorso .` indica a `cargo install` di installare dalla directory corrente.

Al termine di questo comando, un eseguibile `rgb-lightning-node' sarà disponibile nella cartella `$CARGO_HOME/bin/`. Assicurarsi che questo percorso sia presente in `$PATH`, in modo da poter invocare il comando da qualsiasi directory.

### Requisiti di prestazione

Per funzionare, il demone `rgb-lightning-node` richiede la presenza e la configurazione di :


- Un nodo `bitcoind`**

Ogni istanza RLN dovrà comunicare con `bitcoind` per trasmettere e monitorare le proprie transazioni sulla catena. Al demone dovranno essere forniti l'autenticazione (login/password) e l'URL (host/porta).


- Un indicizzatore** (Electrum o Esplora)

Il demone deve essere in grado di elencare ed esplorare le transazioni sulla catena, in particolare di trovare l'UTXO su cui è stata ancorata una risorsa. È necessario specificare l'URL del server Electrum o di Esplora.


- Un proxy RGB**

Come visto nei capitoli precedenti, il **proxy server** è un componente (opzionale, ma altamente consigliato) per semplificare lo scambio di *incarichi* tra i peer di Lightning. Anche in questo caso, è necessario specificare un URL.

Gli ID e gli URL vengono inseriti quando il demone viene _sbloccato_ tramite l'API. Per saperne di più, si veda più avanti.

### Lancio di Regtest

Per un uso semplice, c'è uno script `regtest.sh` che avvia automaticamente, tramite Docker, un insieme di servizi: `bitcoind`, `electrs` (indicizzatore), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

Consente di avviare un ambiente locale, isolato e preconfigurato. Crea e distrugge i contenitori e le directory di dati a ogni riavvio. Inizieremo avviando il file :

```bash
./regtest.sh start
```

Questo script :


- Creare una cartella `docker/` per memorizzare i file ;
- Eseguire `bitcoind` in regtest, così come l'indicizzatore `electrs` e il `rgb-proxy-server`;
- Aspettare che tutto sia pronto per l'uso.

![RGB-Bitcoin](assets/fr/101.webp)

Successivamente, lanceremo diversi nodi RLN. In shell separate, eseguire ad esempio (per lanciare 3 nodi RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- Il parametro `--rete regtest` indica l'uso della configurazione regtest;
- `--daemon-listening-port` indica su quale porta REST il nodo Lightning ascolterà le chiamate API (JSON);
- `--ldk-peer-listening-port` specifica su quale porta Lightning p2p ascoltare;
- `dataldk0/`, `dataldk1/` sono i percorsi delle directory di archiviazione (ogni nodo memorizza le proprie informazioni separatamente).

È inoltre possibile eseguire comandi sui nodi RLN dal browser:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Perché un nodo possa aprire un canale, deve prima disporre di bitcoin su un indirizzo generato con il seguente comando (per il nodo n°1, ad esempio):

```bash
curl -X POST http://localhost:3001/address
```

La risposta vi fornirà un indirizzo.

![RGB-Bitcoin](assets/fr/103.webp)

Nel Regtest `bitcoind`, stiamo per estrarre alcuni bitcoin. Eseguire :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Inviare i fondi all'indirizzo del nodo generato sopra:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Quindi, estrarre un blocco per confermare la transazione:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Lancio di Testnet (senza Docker)

Se si vuole testare uno scenario più realistico, si possono lanciare 3 nodi RLN sulla Testnet piuttosto che in Regtest, puntando a servizi pubblici:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Per impostazione predefinita, se non viene trovata alcuna configurazione, il demone cercherà di utilizzare il file :


- `bitcoind_rpc_host`: `electrum.iriswallet.com
- `bitcoind_rpc_port`: `18332
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Con il login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

È possibile personalizzare questi elementi anche tramite l'API `init`/`unlock`.

### Emissione di un token RGB

Per emettere un token, inizieremo creando degli UTXO "colorabili":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Naturalmente è possibile adattare l'ordine. Per confermare la transazione, viene emesso un :

```bash
./regtest.sh mine 1
```

Ora possiamo creare una risorsa RGB. Il comando dipende dal tipo di risorsa che si desidera creare e dai suoi parametri. Qui sto creando un token NIA (*Non Inflatable Asset*) chiamato "PBN" con una dotazione di 1000 unità. La `precisione` consente di definire la divisibilità delle unità.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

La risposta include l'ID della risorsa appena creata. Ricordarsi di annotare questo identificatore. Nel mio caso, è :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

È quindi possibile trasferirlo sulla catena o allocarlo in un canale Lightning. Questo è esattamente ciò che faremo nella prossima sezione.

### Apertura di un canale e trasferimento di un asset RGB

È necessario prima collegare il proprio nodo a un peer sulla rete Lightning utilizzando il comando `/connectpeer`. Nel mio esempio, controllo entrambi i nodi. Quindi recupererò la chiave pubblica del mio secondo nodo Lightning con questo comando:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Il comando restituisce la chiave pubblica del mio nodo n°2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Successivamente, apriremo il canale specificando la risorsa pertinente (`PBN`). Il comando `/openchannel` consente di definire la dimensione del canale in satoshi e di scegliere di includere l'asset RGB. Dipende da cosa si vuole creare, ma nel mio caso il comando è :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Per saperne di più, cliccate qui:


- `peer_pubkey_e_opt_addr`: Identificatore del peer a cui ci si vuole connettere (la chiave pubblica trovata in precedenza);
- `capacità_sat`: Capacità totale del canale in satoshi ;
- `push_msat`: Importo in millisatoshi inizialmente trasferito al peer quando il canale viene aperto (qui trasferisco immediatamente 10.000 sats in modo che possa fare un trasferimento RGB più tardi) ;
- `asset_amount`: Quantità di risorse RGB da impegnare nel canale ;
- `asset_id` : identificatore univoco dell'asset RGB impegnato nel canale;
- `pubblico`: Indica se il canale deve essere reso pubblico per l'instradamento sulla rete.

![RGB-Bitcoin](assets/fr/111.webp)

Per confermare la transazione, vengono estratti 6 blocchi:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Il canale Lightning è ora aperto e contiene anche 500 gettoni `PBN` dal lato del nodo n°1. Se il nodo n°2 desidera ricevere i token `PBN`, deve generare una fattura. Ecco come fare:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Con :


- `amt_msat`: Importo della fattura in millisatoshi (minimo 3000 sats) ;
- `scadenza_sec` : tempo di scadenza della fattura in secondi ;
- `asset_id` : identificativo dell'asset RGB associato alla fattura ;
- importo_patrimonio": Importo del bene RGB da trasferire con questa fattura.

In risposta, si otterrà una fattura RGB (come descritto nei capitoli precedenti):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Ora pagheremo questa fattura dal primo nodo, che detiene il denaro necessario con il token `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Il pagamento è stato effettuato. Questo può essere verificato eseguendo il comando :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Ecco come distribuire un nodo Lightning modificato per trasportare risorse RGB. Questa dimostrazione si basa su :


- Un ambiente regtest (tramite `./regtest.sh`) o testnet ;
- Un nodo Lightning (`rgb-lightning-node`) basato su un `bitcoind`, un indicizzatore e un `rgb-proxy-server`;
- Una serie di API REST JSON per l'apertura/chiusura di canali, l'emissione di token, il trasferimento di attività tramite Lightning, ecc.

Grazie a questo processo :


- Le transazioni con impegno lightning includono un'uscita aggiuntiva (OP_RETURN o Taproot) con l'ancoraggio di una transizione RGB;
- I trasferimenti vengono effettuati esattamente come i tradizionali pagamenti Lightning, ma con l'aggiunta di un token RGB;
- Più nodi RLN possono essere collegati per instradare e sperimentare pagamenti attraverso più nodi, a condizione che ci sia sufficiente liquidità sia in bitcoin che in asset RGB sul percorso.

Il progetto rimane in fase alfa. Si raccomanda pertanto di limitarsi agli ambienti di prova (regtest, testnet).

Le opportunità aperte da questa compatibilità LN-RGB sono notevoli: monete stabili su Lightning, DEX layer-2, trasferimento di gettoni fungibili o NFT a costi molto bassi... I capitoli precedenti hanno delineato l'architettura concettuale e la logica di validazione. Ora avete una visione pratica di come ottenere un nodo di questo tipo e farlo funzionare, per i vostri futuri sviluppi o test.

# Conclusione

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Recensioni e valutazioni

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusione

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>
