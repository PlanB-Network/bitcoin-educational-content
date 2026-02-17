---
name: Maestria Mining open source di Bitaxe
goal: Padroneggiate l'intero ecosistema Bitaxe, dall'assemblaggio dell'hardware alla personalizzazione avanzata e all'ottimizzazione delle prestazioni
objectives: 

  - Comprendere la filosofia dell'hardware open source Bitcoin mining
  - Costruire da zero i dispositivi Bitaxe mining
  - Configurare e ottimizzare il software mining, compresi AxeOS e Public Pool
  - Implementare ottimizzazioni avanzate delle prestazioni, tra cui l'overclocking e il benchmarking

---

# La vostra guida Bitaxe Mining


Benvenuti al corso completo di Bitaxe, dove imparerete a padroneggiare il rivoluzionario hardware open source Bitcoin mining che sta democratizzando l'accesso alla tecnologia mining. Questo corso vi porterà dalla comprensione delle basi filosofiche del mining decentralizzato alle tecniche avanzate di personalizzazione dell'hardware e di ottimizzazione delle prestazioni.


Il progetto Bitaxe rappresenta un cambio di paradigma nel settore Bitcoin mining, rompendo il monopolio dei produttori proprietari di ASIC e fornendo progetti, firmware e software completamente open source. Attraverso questi capitoli pratici, acquisirete competenze pratiche nell'assemblaggio dell'hardware, nella configurazione del software, nella progettazione di circuiti stampati e nell'ottimizzazione delle prestazioni.


Non è richiesta alcuna esperienza precedente di mining, anche se una conoscenza di base dell'elettronica e la familiarità con GitHub saranno utili. Il corso vi trasformerà da osservatori curiosi in capaci costruttori e collaboratori di Bitaxe.


+++


# Introduzione


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Panoramica del corso


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Benvenuti al corso MIN 306 _**Bitaxe Open Source Mining Mastery**_, un viaggio completo nel mondo di Bitaxe mining. Questo corso è pensato per chi vuole capire, costruire e ottimizzare il proprio hardware Bitaxe mining, esplorando al contempo le basi filosofiche e tecniche che rendono questo progetto unico all'interno dell'ecosistema Bitcoin.


### Capire Bitaxe


La prima sezione getta le basi essenziali: scoprirete le origini del progetto Bitaxe, la sua evoluzione e i valori di decentralizzazione e trasparenza che lo definiscono. Imparerete cos'è effettivamente un Bitaxe, come si differenzia dagli ASIC proprietari e dove trovare le risorse della comunità per approfondire le vostre conoscenze. Questa sezione fornisce il contesto necessario per capire perché Bitaxe rappresenta un punto di svolta nella storia del Bitcoin mining.


### Software e operazioni


La seconda sezione si concentra sull'ambiente software, con una presentazione dettagliata di *AxeOS*: il sistema operativo open-source progettato appositamente per i dispositivi Bitaxe. Imparerete le sue caratteristiche principali e come configurare e interagire con il vostro dispositivo per avviare le prime operazioni mining.


### Comunità e collaborazione


La terza sezione evidenzia l'aspetto collaborativo del progetto. Esplorerete la filosofia open-source applicata allo sviluppo hardware e software di Bitaxe. Attraverso esercizi pratici, imparerete come contribuire direttamente al codice sorgente e scoprirete anche _Public Pool_, una piattaforma comunitaria per mettere in comune la potenza di calcolo. Imparerete anche a installarla su un nodo Umbrel per un'integrazione locale e sovrana.


### Assemblaggio dell'hardware e risoluzione dei problemi


Nella quarta sezione ci si immerge nell'hardware vero e proprio. Imparerete a identificare gli strumenti necessari per assemblare un Bitaxe, a risolvere i problemi di saldatura e a eseguire una diagnostica completa utilizzando *AxeOS* e gli strumenti USB. Questa sezione pone l'accento sulla pratica e sulla comprensione approfondita dell'interazione tra componenti hardware e software.


### Personalizzazione avanzata


La quinta sezione è dedicata alla personalizzazione. Imparerete a modificare il PCB (circuito stampato), a creare un file di fabbrica e a utilizzare il _Bitaxe Web Flasher_. Questa sezione è rivolta a coloro che vogliono andare oltre il semplice assemblaggio e progettare realmente versioni personalizzate del proprio dispositivo.


### Ottimizzazione delle prestazioni


Infine, la sesta sezione tratta le tecniche di ottimizzazione avanzate. Imparerete come effettuare il benchmark del vostro Bitaxe per valutarne le prestazioni e come overcloccarlo in modo efficiente. Queste abilità vi aiuteranno a ottenere il massimo dal vostro hardware, rispettando i suoi limiti fisici.


Come in tutti i corsi di Plan ₿ Academy, la sezione finale comprende una valutazione per rafforzare le conoscenze acquisite.


Tuffatevi in questa avventura tecnica: il futuro del Bitcoin mining è nelle vostre mani!


# Capire Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## La storia

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Il progetto Bitaxe rappresenta un cambiamento rivoluzionario nello sviluppo dell'hardware Bitcoin [mining](https://planb.academy/resources/glossary/mining), portando i principi dell'open source in un settore dominato da soluzioni proprietarie. Questa serie didattica esplora la storia completa, le innovazioni tecniche e l'evoluzione guidata dalla comunità di Bitaxe, fornendo approfondimenti su come la visione di un singolo ingegnere si sia trasformata in un fiorente ecosistema di hardware mining decentralizzato. Esaminando le origini, le sfide e i risultati del progetto, si acquisisce una preziosa comprensione delle complessità tecniche dello sviluppo del [ASIC](https://planb.academy/resources/glossary/asic) e della potenza della collaborazione open source nello spazio Bitcoin.


### La storia delle origini: Dalla scoperta della Via della Seta alla visione del Mining solare


Skot, il fondatore di Bitaxe, ha iniziato il suo viaggio nella Bitcoin durante una festa universitaria, dove è venuto a conoscenza della Bitcoin grazie all'acquisto di oggetti sulla Via della Seta. Questa esposizione iniziale al Bitcoin a circa 20 dollari per moneta ha scatenato una curiosità che si è poi evoluta in un progetto rivoluzionario di mining. Le basi tecniche per il suo lavoro futuro sono state gettate durante il periodo universitario, dove ha avuto accesso a vaste risorse FPGA in un ambiente di laboratorio. Lavorando a fianco del suo supervisore, Skot iniziò a sperimentare con i bitstream FPGA open source per il Bitcoin mining, inizialmente con il modesto obiettivo di mining abbastanza Bitcoin per acquistare una pizza per il loro ufficio.


Il passaggio dalla sperimentazione accademica allo sviluppo serio è avvenuto anni dopo, quando Skot ha lavorato su gateway a energia solare per la raccolta di dati a distanza in Africa. Questa esperienza professionale con i sistemi a energia solare ha fatto capire che gli ASIC Bitcoin mining, essendo fondamentalmente dispositivi a bassa tensione continua, si sarebbero abbinati perfettamente ai pannelli solari. Il concetto sembrava naturale ed elegante. Tuttavia, quando Skot iniziò a ricercare le soluzioni esistenti, scoprì un vuoto significativo nel mercato: a differenza dei primi tempi del Bitcoin mining, quando i progetti di FPGA erano apertamente disponibili, l'avvento degli ASIC aveva spostato il settore verso soluzioni completamente proprietarie e closed-source.


La mancanza di hardware open source per il mining è diventata una frustrazione per Skot, soprattutto in considerazione del suo background nello sviluppo di software open source e della sua convinzione che la natura open source del Bitcoin dovesse estendersi alla sua infrastruttura mining. Questo allineamento filosofico con i principi dell'open source, unito alla sfida tecnica del reverse-engineering dei progetti proprietari del ASIC, ha posto le basi per quello che sarebbe diventato il progetto Bitaxe. La visione iniziale era ambiziosa ma pratica: creare un [minatore](https://planb.academy/resources/glossary/miner) Bitcoin alimentato a energia solare che potesse funzionare in modo indipendente senza richiedere un computer separato per il controllo, rendendolo adatto all'impiego in luoghi remoti sotto i pannelli solari.


### Sfide tecniche e scoperte di ingegneria inversa


Lo sviluppo di Bitaxe ha richiesto il superamento di notevoli ostacoli tecnici, principalmente incentrati sulla completa mancanza di documentazione dei chip ASIC di Bitmain. L'approccio di Skot a questa sfida ha esemplificato la determinazione e l'ingegno necessari per un reverse engineering di successo. Senza avere accesso alle schede tecniche ufficiali o alle specifiche tecniche, ha fatto ricorso all'esame dei chip al microscopio, alla misurazione dei passi dei pin con i calibri e persino alla scansione dei chip per determinare gli esatti requisiti di ingombro. Questo processo minuzioso ha portato a diversi prototipi falliti, con le prime due iterazioni del "day miner" che non hanno funzionato correttamente a causa di calcoli errati dell'ingombro.


La svolta è arrivata con la terza iterazione nel maggio 2022, quando Skot ha creato con successo un progetto funzionante a due chip utilizzando chip BM1387 raccolti da unità Antminer S9. Questo risultato ha segnato la nascita del nome Bitaxe, ispirato al concetto di piccone per il Bitcoin mining. Il successo di questo progetto ha convalidato l'approccio di reverse engineering e ha dimostrato che gli sviluppatori indipendenti possono creare hardware mining funzionale senza il supporto del produttore. Tuttavia, le sfide tecniche non si limitavano all'interfacciamento dei chip, ma comprendevano anche una complessa progettazione dell'alimentazione, poiché gli ASIC richiedevano una precisa regolazione della tensione a correnti elevate, spesso operando a tensioni fino a 0,6 volt pur assorbendo un notevole amperaggio.


Lo sviluppo del firmware ha presentato un ulteriore livello di complessità, in quanto il progetto richiedeva la creazione di un software per il mining che potesse essere eseguito direttamente su un microcontrollore ESP32, anziché affidarsi a computer esterni che eseguono software come CGMiner. Questo approccio autonomo era essenziale per la visione di Skot di unità mining distribuibili e indipendenti. La combinazione di reverse engineering dell'hardware e sviluppo del firmware incorporato ha creato una sfida tecnica completa che ha richiesto competenze in diverse discipline, dall'ingegneria elettrica alla progettazione di PCB, dalla programmazione incorporata ai protocolli di rete.


### Formazione della comunità e collaborazione open source


La trasformazione di Bitaxe da progetto solitario a fiorente iniziativa comunitaria rappresenta uno degli aspetti più significativi del suo successo. Inizialmente, i tentativi di Skot di suscitare l'interesse di generate attraverso i forum Bitcoin e i social media hanno incontrato una risposta limitata e un occasionale scetticismo. La svolta è arrivata quando membri della comunità come SirVapesAlot hanno riconosciuto il potenziale del mining open source e hanno creato il server Discord Open Source Miners United (OSMU). Questa piattaforma ha fornito l'ambiente collaborativo necessario per la fioritura del progetto, attirando collaboratori provenienti da ambienti diversi che condividevano l'interesse comune di democratizzare la tecnologia Bitcoin mining.


Il modello di sviluppo guidato dalla comunità si è rivelato straordinariamente efficace, con collaboratori chiave come johnny9 e Ben che sono emersi per affrontare sfide tecniche specifiche. L'esperienza di Johnny9 nello sviluppo del firmware ha risolto problemi critici di implementazione del software, mentre le competenze di Ben nello sviluppo front-end hanno creato l'intuitivo cruscotto AxeOS che ha semplificato la configurazione e il monitoraggio del dispositivo. Tra gli altri contributi di Ben figurano lo sviluppo di capacità produttive e la creazione di Public Pool, un [pool mining](https://planb.academy/resources/glossary/pool-mining) open source ottimizzato per i dispositivi Bitaxe. Questo approccio collaborativo ha dimostrato come i principi dell'open source possano accelerare lo sviluppo al di là dei risultati che ogni singolo collaboratore potrebbe raggiungere da solo.


La comunità OSMU ha anche favorito un ambiente inclusivo in cui i nuovi arrivati potevano imparare e contribuire indipendentemente dalle loro competenze tecniche iniziali. Il percorso di Ben, da novizio della saldatura a grande produttore, esemplifica questo approccio accogliente allo sviluppo delle competenze. L'impegno della comunità per la formazione e il sostegno reciproco ha creato un circolo virtuoso in cui i membri più esperti hanno fatto da tutor ai nuovi arrivati, che poi sono diventati essi stessi dei collaboratori. Questo modello si è rivelato essenziale per far crescere il progetto oltre la sua portata originaria e per creare un ecosistema sostenibile per un'innovazione e una crescita continue.


### Visione del Mining decentralizzato e impatto futuro


La visione a lungo termine di Skot per Bitaxe va ben oltre la creazione di un altro dispositivo mining: si tratta di una trasformazione fondamentale del panorama mining del Bitcoin. L'obiettivo ambizioso di produrre un milione di minatori one-terahash creerebbe un exahash di potenza mining distribuita, rappresentando un passo significativo verso la decentralizzazione del mining. Questa visione affronta le preoccupazioni critiche sulla centralizzazione del mining, dove i grandi bacini e le operazioni industriali potrebbero essere potenzialmente soggetti a pressioni governative o alla cattura normativa. Distribuendo l'energia del mining tra innumerevoli minatori domestici, la rete diventa più resiliente e in linea con i principi di decentralizzazione del mining.


Il modello economico a sostegno di questa visione si basa sulle caratteristiche uniche del mining domestico, dove i costi infrastrutturali sono sostanzialmente nulli e i minatori possono operare con una supervisione minima. A differenza delle operazioni industriali di mining che richiedono ingenti investimenti di capitale in strutture, infrastrutture elettriche e sistemi di raffreddamento, i minatori domestici possono semplicemente collegare i dispositivi alle prese elettriche e alle connessioni Internet esistenti. Questo approccio potrebbe teoricamente portare online un [tasso di hash](https://planb.academy/resources/glossary/hashrate) significativo senza le tradizionali barriere all'ingresso che caratterizzano le operazioni mining su larga scala.


Il successo del progetto ha già iniziato a influenzare il più ampio ecosistema Bitcoin mining, con il potenziale di ispirare altri produttori ad abbracciare modelli di sviluppo open source. La redditività finanziaria dimostrata dai produttori di Bitaxe dimostra che l'hardware open source può avere successo commerciale mantenendo la trasparenza e il coinvolgimento della comunità. Mentre il progetto continua a evolversi con nuove integrazioni di chip, design migliorati e partnership di produzione ampliate, serve come prova di concetto di come il Bitcoin mining possa tornare alle sue radici decentralizzate, abbracciando al contempo la moderna tecnologia ASIC. L'obiettivo finale va oltre la semplice distribuzione del tasso di hash e include un impatto educativo, portando un maggior numero di persone a contatto diretto con il processo fondamentale del Bitcoin mining e promuovendo una più profonda comprensione del modello di sicurezza della rete.


## Che cos'è il Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Panoramica dell'hardware e capacità


L'ecosistema Bitaxe comprende diverse iterazioni di hardware, ciascuna progettata per ottimizzare diversi aspetti dell'esperienza mining, mantenendo la filosofia di base dell'accessibilità open-source. Questi dispositivi non servono solo come hardware funzionale per il mining, ma anche come strumenti didattici che consentono agli utenti di comprendere l'intricata relazione tra i chip ASIC, i microcontrollori e il processo Bitcoin mining. La comprensione della filosofia di progettazione e dell'implementazione tecnica di Bitaxe fornisce preziose indicazioni sul funzionamento del moderno hardware mining sia a livello di componente che di sistema.



### Bitaxe Max, implementazione di prima generazione


Il Bitaxe Max rappresenta l'implementazione fondamentale del concetto di Bitaxe, utilizzando il chip BM1397 ASIC originariamente sviluppato da Bitmain per la serie S17 mining. Questa integrazione del chip dimostra come l'hardware open-source possa riutilizzare la tecnologia ASIC esistente per creare soluzioni mining accessibili. Il Bitaxe Max offre una velocità di hash stimata tra i 300 e i 400 gigahashes al secondo, posizionandosi come piattaforma mining educativa e sperimentale piuttosto che come soluzione su scala commerciale.


L'integrazione del chip BM1397 nel Bitaxe Max ha richiesto un'attenta considerazione della gestione dell'alimentazione, del controllo termico e dei protocolli di comunicazione. Il design della scheda soddisfa i requisiti specifici di questo ASIC, fornendo al contempo i circuiti di supporto necessari per un funzionamento stabile. Questa implementazione dimostra come lo sviluppo di hardware open-source possa sfruttare la tecnologia dei semiconduttori esistente per creare nuove applicazioni e opportunità di apprendimento all'interno della comunità mining.


### Bitaxe Ultra, tecnologia chip avanzata


Bitaxe Ultra rappresenta l'evoluzione della piattaforma Bitaxe e incorpora il chip BM1366 ASIC più avanzato della serie S19 di Bitmain. Questa nuova tecnologia di chip apporta alla piattaforma Bitaxe caratteristiche di efficienza e prestazioni migliori, pur mantenendo la stessa filosofia di progettazione fondamentale. L'aggiornamento al chip BM1366 dimostra l'adattabilità della piattaforma e l'impegno della comunità nell'incorporare i progressi tecnologici nelle soluzioni mining open-source.


Il passaggio dal chip BM1397 al BM1366 ha richiesto modifiche ai sistemi di alimentazione, alla gestione termica e agli algoritmi di controllo della scheda. Questi cambiamenti illustrano la natura iterativa dello sviluppo dell'hardware e l'importanza di mantenere la compatibilità pur migliorando le prestazioni. L'implementazione di Bitaxe Ultra offre agli utenti l'accesso alla più recente tecnologia ASIC, preservando al contempo la natura educativa e sperimentale della piattaforma.


### Microcontrollori e sistemi di comunicazione


Nel cuore di ogni dispositivo Bitaxe si trova un microcontrollore ESP che funge da interfaccia principale tra l'utente e il chip ASIC. Questo microcontrollore esegue un software specializzato sviluppato dalla comunità Open Source Miners United (OSMU), che consente un controllo preciso dei parametri di funzionamento del ASIC. La comunicazione tra il microcontrollore e il ASIC avviene attraverso linee di comunicazione seriali accuratamente progettate e incise direttamente sul circuito stampato come tracce visibili.


Il ruolo del microcontrollore va oltre il semplice controllo del ASIC: comprende la gestione dell'alimentazione, il monitoraggio della temperatura e le funzioni di interfaccia utente. Attraverso lo schermo integrato, gli utenti possono monitorare i parametri operativi critici come la temperatura, la velocità di hash, l'indirizzo IP e altre statistiche rilevanti del mining. Questo sistema di feedback in tempo reale fornisce preziose indicazioni sulle prestazioni del dispositivo e aiuta gli utenti a ottimizzare le operazioni del mining imparando a conoscere il comportamento dell'hardware sottostante.


### Gestione dell'alimentazione e considerazioni sulla sicurezza


La piattaforma Bitaxe funziona con un requisito di alimentazione rigoroso di 5 volt, rendendo la scelta dell'alimentazione corretta fondamentale per la longevità e la sicurezza del dispositivo. Il sistema di gestione dell'alimentazione sulle schede Bitaxe comprende circuiti sofisticati progettati per regolare la tensione di alimentazione del chip ASIC, monitorando al contempo il consumo di energia nelle diverse modalità operative. Questa capacità di gestione dell'alimentazione consente al dispositivo di funzionare in modo efficiente su una gamma di frequenze e tensioni interne, con un consumo tipico compreso tra 5 e 25 watt a seconda della configurazione.


La comprensione dei requisiti di potenza diventa cruciale se si considera che un'applicazione errata della tensione può danneggiare in modo permanente il dispositivo. La relazione tra frequenza, tensione, consumo di energia e velocità di hash dimostra i principi fondamentali del funzionamento del ASIC, che si applicano a tutto l'hardware mining. Gli utenti possono sperimentare diverse impostazioni di potenza per comprendere i compromessi di efficienza inerenti alle operazioni del mining, acquisendo esperienza pratica con concetti che si applicano alle implementazioni mining su larga scala.


### Solo Mining Focus e partecipazione alla rete


La piattaforma Bitaxe si rivolge specificamente alle applicazioni mining in solitaria, in cui i singoli minatori tentano di risolvere i [blocchi](https://planb.academy/resources/glossary/block) Bitcoin in modo indipendente anziché partecipare a grandi pool mining. Sebbene il tasso di hash dei dispositivi Bitaxe renda statisticamente improbabile la scoperta di blocchi di successo, questo approccio ha importanti finalità educative e filosofiche all'interno della comunità Bitcoin. Solo mining con dispositivi Bitaxe aiuta gli utenti a comprendere le meccaniche fondamentali del sistema [proof-of-work](https://planb.academy/resources/glossary/proof-of-work) di Bitcoin, contribuendo al contempo alla decentralizzazione della rete.


L'enfasi sul mining in solitaria riflette l'impegno della comunità OSMU a incoraggiare la partecipazione individuale al modello di sicurezza Bitcoin. Fornendo hardware accessibile che può funzionare in modo indipendente, la piattaforma Bitaxe consente agli utenti di eseguire le proprie operazioni mining senza fare affidamento sull'infrastruttura del pool. Questo approccio favorisce una comprensione più approfondita del meccanismo di [consenso](https://planb.academy/resources/glossary/consensus) del Bitcoin, sostenendo al contempo la natura decentralizzata della rete attraverso una maggiore diversità dei minatori.


### Evoluzione dell'hardware e miglioramenti della produzione


La piattaforma Bitaxe continua a evolversi grazie al feedback della comunità e all'ottimizzazione della produzione, con le nuove versioni che incorporano miglioramenti che migliorano la producibilità e l'esperienza dell'utente. Gli aggiornamenti delle versioni si concentrano in genere sull'efficienza della produzione piuttosto che su modifiche fondamentali delle prestazioni, garantendo che gli utenti esistenti non debbano affrontare la pressione dell'obsolescenza. Caratteristiche come il passaggio da connettori micro-USB a USB-C e il miglioramento dei sistemi di connessione all'alimentazione riflettono l'attenzione della comunità per i miglioramenti pratici dell'usabilità.


Questo approccio evolutivo dimostra i vantaggi dello sviluppo di hardware open-source, in cui il contributo della comunità porta a miglioramenti incrementali a vantaggio di tutti gli utenti. La filosofia del "se ha hash, ha hash" sottolinea l'attenzione della piattaforma per la funzionalità piuttosto che per gli aggiornamenti costanti, incoraggiando gli utenti a mantenere e a far funzionare i loro dispositivi piuttosto che a cercare le ultime versioni. Questo approccio supporta pratiche hardware sostenibili, mantenendo il valore educativo di Bitaxe.


## Dove posso saperne di più?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Il progetto Bitaxe rappresenta un'iniziativa open-source mining completa che va ben oltre il singolo dispositivo. Capire dove trovare informazioni affidabili, risorse tecniche e supporto della comunità è fondamentale per chiunque voglia impegnarsi in questo ecosistema. Questo capitolo fornisce una guida completa alle piattaforme e alle risorse essenziali che costituiscono la base della comunità Bitaxe e Open Source Miners United (OSMU).


### Bitaxe.org, l'hub centrale


Il sito web Bitaxe.org è il punto di accesso principale a tutte le informazioni e le risorse relative al progetto. Questa piattaforma centralizzata funge da primo punto di riferimento ogni volta che si ha bisogno di conoscere i dispositivi Bitaxe o di esplorare altri progetti all'interno della comunità OSMU. Il design del sito web privilegia l'accessibilità e l'organizzazione, presentando ai visitatori link accuratamente curati che collegano a varie risorse specializzate in tutto l'ecosistema.


L'importanza di questo hub centrale non può essere sopravvalutata, poiché elimina la confusione che spesso accompagna i progetti open-source decentralizzati. Piuttosto che cercare su più piattaforme o affidarsi a informazioni potenzialmente obsolete provenienti da fonti non ufficiali, gli utenti possono fidarsi di Bitaxe.org che fornisce collegamenti aggiornati e verificati a tutte le risorse essenziali. Questo approccio garantisce che sia i nuovi arrivati sia i membri esperti della comunità possano trovare in modo efficiente le informazioni specifiche di cui hanno bisogno per i loro progetti.


### Risorse tecniche e materiali di sviluppo


Il repository dei file di progettazione hardware su GitHub rappresenta una delle risorse più preziose per chiunque sia interessato a comprendere o costruire i dispositivi Bitaxe. Questo archivio pubblico contiene una documentazione completa che copre ogni aspetto del processo di progettazione hardware, dai concetti iniziali alle specifiche di produzione finali. Il repository include immagini dettagliate, obiettivi del progetto, descrizioni delle funzionalità e spiegazioni dei componenti integrati che forniscono sia una profondità tecnica che una guida pratica.


Per coloro che sono interessati a produrre i propri dispositivi, il repository include file di documentazione specifici come building.md, che fornisce istruzioni passo-passo per l'intero processo di produzione. Questa documentazione copre gli strumenti software necessari per la progettazione dei PCB, le procedure per l'invio dei file ai produttori e le fasi di ricezione e convalida dei PCB prodotti. Questo livello di dettaglio garantisce che i singoli o le piccole organizzazioni possano affrontare con successo il processo di produzione anche senza una precedente esperienza nella produzione di hardware.


Il repository ESP-Miner è la posizione centrale per tutto il codice e la documentazione relativi al firmware. Questo repository GitHub contiene ogni riga di codice scritta per il firmware Bitaxe, insieme a una documentazione completa che spiega i requisiti di sistema, le specifiche hardware e le opzioni di configurazione. La struttura del repository è stata progettata per soddisfare sia gli utenti che preferiscono i file binari precompilati sia gli sviluppatori che desiderano creare il firmware dal codice sorgente.


La documentazione contenuta in questo repository comprende sezioni dettagliate sui requisiti hardware, sulle opzioni di preconfigurazione e sui valori consigliati per le varie impostazioni. Queste informazioni si rivelano preziose per gli utenti che desiderano personalizzare i propri dispositivi o risolvere problemi specifici. Inoltre, il repository include informazioni sugli sviluppi più recenti, come l'integrazione di Raspberry Pi, assicurando che la documentazione rimanga aggiornata con l'evoluzione del progetto.


### Strumenti di gestione e manutenzione dei dispositivi


Il web flasher di Bitaxe rappresenta una soluzione pratica per la manutenzione e gli aggiornamenti dei dispositivi. Questo strumento basato sul web consente agli utenti di eseguire il flashing del firmware sui propri dispositivi senza dover ricorrere a software specializzati o a complesse procedure a riga di comando. Il flasher supporta diverse varianti di dispositivi, tra cui il Bitaxe Ultra con diverse versioni di porte e i vecchi modelli Bitaxe Max. Gli utenti possono scegliere tra l'aggiornamento del firmware esistente tramite l'interfaccia web e l'esecuzione di reset completi di fabbrica tramite connessioni USB.


Questo strumento affronta una delle sfide più comuni per gli appassionati di hardware: la manutenzione e l'aggiornamento del firmware dei dispositivi. Fornendo un'interfaccia web di facile utilizzo, il flasher elimina molte delle barriere tecniche che altrimenti potrebbero impedire agli utenti di mantenere i propri dispositivi aggiornati con le ultime versioni del firmware. Il design dello strumento privilegia la semplicità, pur mantenendo la flessibilità necessaria per le diverse configurazioni dei dispositivi e gli scenari di aggiornamento.


### Piattaforme comunitarie e canali di comunicazione


Il server Discord rappresenta il cuore dell'interazione e del supporto in tempo reale della comunità all'interno dell'ecosistema Bitaxe. L'organizzazione del server riflette i diversi interessi ed esigenze dei membri della comunità, con canali attentamente strutturati che facilitano discussioni mirate su argomenti specifici. I nuovi membri sono sottoposti a un processo di verifica che richiede la lettura e l'accettazione delle regole della comunità, assicurando che tutti i partecipanti comprendano le aspettative per un'interazione rispettosa e produttiva.


La struttura dei canali del server comprende aree di discussione generali che coprono argomenti quali l'integrazione dell'energia solare, le piscine mining e le discussioni relative al Bitcoin. Sezioni più specializzate si concentrano su dispositivi specifici, tra cui canali dedicati alle varianti Bitaxe Ultra, Hex e Supra. Il canale del firmware offre uno spazio mirato per le discussioni tecniche sullo sviluppo del software e la risoluzione dei problemi, mentre il canale dei comunicati ufficiali assicura che i membri della comunità ricevano notifiche tempestive sui nuovi sviluppi.


È inoltre presente un'area riservata agli abbonati che offre ulteriori vantaggi ai membri della comunità che scelgono di sostenere finanziariamente il progetto. Questo approccio a più livelli consente alla comunità di offrire servizi avanzati, pur mantenendo aperto l'accesso alle informazioni essenziali e ai canali di supporto. Il canale di assistenza è uno spazio dedicato alla risoluzione dei problemi e all'assistenza tecnica, per garantire agli utenti un supporto tempestivo in caso di difficoltà.



Il wiki di Open Source Miners United (osmu.wiki) fornisce una documentazione completa che integra le discussioni in tempo reale che si svolgono su Discord. A differenza delle piattaforme basate sulla chat, il wiki offre una documentazione strutturata e ricercabile che copre tutti gli aspetti del progetto Bitaxe e delle iniziative correlate. Il modo in cui è organizzato rispecchia la struttura del progetto, con sezioni dedicate alle diverse serie di dispositivi e guide complete alla configurazione.


La natura open-source del wiki consente ai membri della comunità di contribuire direttamente alla documentazione. Gli utenti possono modificare le pagine, inviare correzioni e aggiungere nuove informazioni attraverso l'integrazione con GitHub, garantendo che la base di conoscenze rimanga aggiornata e trasparente. Questo approccio collaborativo sfrutta l'esperienza collettiva della comunità, mantenendo al contempo un controllo di qualità attraverso un processo di revisione delle modifiche inviate.


Il wiki include risorse pratiche come le guide di configurazione in PDF che forniscono istruzioni passo-passo per la configurazione e l'uso del dispositivo. Queste guide sono un valido riferimento sia per i nuovi utenti che per i membri esperti della comunità che necessitano di un accesso rapido a procedure specifiche o a dettagli di configurazione.


### Informazioni sugli acquisti e sui fornitori


L'elenco legale di Bitaxe risponde a un'esigenza critica della comunità dell'hardware open-source: identificare i venditori affidabili ed evitare quelli fraudolenti. Questo elenco curato include rivenditori e produttori verificati che soddisfano criteri specifici per la legittimità e il supporto della comunità. Ogni elenco include link diretti ai siti web dei venditori, informazioni regionali e descrizioni delle aziende che aiutano gli utenti a prendere decisioni di acquisto informate.


È importante notare che l'elenco indica se ogni fornitore contribuisce alla comunità OSMU, sia finanziariamente che attraverso altre forme di sostegno. Questa trasparenza aiuta i membri della comunità a capire quali fornitori sostengono attivamente lo sviluppo e la sostenibilità del progetto. L'elenco serve anche come misura di protezione contro le truffe più comuni, come i pre-ordini non autorizzati di prodotti non ancora usciti, che storicamente hanno causato problemi all'interno della comunità.


L'enfasi sui link non affiliati dimostra l'impegno della comunità a fornire raccomandazioni imparziali sui fornitori. Gli utenti possono fidarsi del fatto che le raccomandazioni si basano sulla legittimità del fornitore e sul contributo della comunità piuttosto che su incentivi finanziari, assicurando che le decisioni di acquisto sostengano sia le esigenze individuali che la sostenibilità della comunità.



# Software e operazioni

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Che cos'è AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS è un firmware e un'interfaccia web per i dispositivi Bitaxe mining, che fornisce agli utenti funzionalità complete di controllo e monitoraggio attraverso un cruscotto intuitivo basato su browser. Questo sistema trasforma il complesso compito della gestione del ASIC in un'esperienza accessibile, consentendo ai minatori di monitorare le prestazioni, regolare le impostazioni e gestire più dispositivi da un'unica interfaccia. La comprensione di AxeOS è essenziale per massimizzare il potenziale del dispositivo Bitaxe e mantenere le operazioni mining ottimali.


### Panoramica del cruscotto e metriche principali


Il cruscotto di AxeOS è la finestra principale sulle prestazioni del dispositivo Bitaxe e presenta le metriche critiche del mining in un formato organizzato e in tempo reale. Quando si naviga verso l'indirizzo IP del dispositivo Bitaxe, vengono immediatamente presentati quattro indicatori di prestazioni chiave che definiscono lo stato attuale del funzionamento del mining. La visualizzazione della velocità di hash mostra l'effettiva velocità di calcolo che il chip ASIC sta producendo durante l'elaborazione del modello di blocco corrente, fornendo un feedback immediato sulla funzionalità di base del dispositivo.


Accanto al tasso di hash, il contatore delle azioni tiene traccia di ogni soluzione valida che il dispositivo Bitaxe invia al pool mining, aumentando ad ogni invio riuscito e fungendo da misura diretta del contributo del dispositivo agli sforzi del pool mining. La metrica dell'efficienza fornisce informazioni cruciali sulle prestazioni energetiche del dispositivo, calcolando il rapporto tra la velocità di hash e il consumo di energia, aiutandovi a ottimizzare la redditività dell'operazione. L'indicatore di difficoltà migliore conserva un record della quota di difficoltà più alta che il dispositivo abbia mai trovato, mantenendo questo risultato anche attraverso riavvii e aggiornamenti, resettandosi solo quando si esegue un flash completo di fabbrica.


Il sistema di menu espandibile del cruscotto, controllato da un pulsante a levetta, consente di accedere a tutte le funzionalità di AxeOS mantenendo un'interfaccia pulita. Il grafico della frequenza di hashish in tempo reale rappresenta una delle sue caratteristiche più preziose, in quanto mostra dati sulle prestazioni in tempo reale che diventano più precisi e informativi quanto più a lungo si mantiene la sessione. Le sezioni relative all'alimentazione, al calore e alle prestazioni forniscono un monitoraggio completo dello stato operativo del dispositivo, compresi gli avvisi sulla tensione d'ingresso che segnalano potenziali problemi di alimentazione, garantendo al contempo un funzionamento continuo entro parametri sicuri.


### Monitoraggio avanzato e informazioni sul sistema


Le capacità di monitoraggio di AxeOS vanno ben oltre il semplice monitoraggio del tasso di hash, fornendo informazioni dettagliate su ogni aspetto del funzionamento del dispositivo Bitaxe. La sezione dedicata all'alimentazione visualizza il consumo energetico calcolato derivato dai circuiti integrati a bordo, le misurazioni della tensione di ingresso dalla connessione dell'alimentatore e i livelli di tensione ASIC richiesti. Quando si verificano cali di tensione, AxeOS presenta immediatamente notifiche di avvertimento, anche se in genere non influiscono sulle operazioni del mining e indicano semplicemente potenziali opportunità di ottimizzazione dell'alimentazione.


Il monitoraggio della temperatura si concentra sulla gestione termica del chip ASIC, con letture effettuate da punti strategici del dispositivo per fornire dati termici accurati con offset appropriati per la precisione a livello di chip. I display di frequenza e tensione offrono un feedback in tempo reale sui parametri di regolazione del ASIC, con la tensione misurata che rappresenta la lettura più accurata disponibile, rilevata direttamente sulla posizione del chip ASIC. Questa precisione consente di regolare con precisione i parametri delle prestazioni, mantenendo condizioni operative sicure.


La sezione dello stato della connessione fornisce una visibilità immediata della configurazione del pool mining, visualizzando l'URL dello strato corrente, la porta e l'identificazione dell'utente. Per i dispositivi collegati a pool pubblici, AxeOS genera comodi collegamenti rapidi che portano direttamente all'interfaccia web del pool, dove è possibile accedere a statistiche dettagliate, elenchi di dispositivi e dati storici sulle prestazioni. Questa integrazione semplifica il processo di monitoraggio collegando le informazioni a livello di dispositivo e di pool in un flusso di lavoro continuo.


### Gestione dello sciame e controllo multidispositivo


La funzionalità Swarm rappresenta la soluzione di AxeOS alla complessità della gestione di più dispositivi Bitaxe in una rete, eliminando la necessità di ricordare e navigare verso numerosi indirizzi IP. Questo sistema di gestione centralizzato consente di aggiungere dispositivi inserendo semplicemente i loro indirizzi IP, rilevando automaticamente i minatori Bitaxe attivi e incorporandoli in un cruscotto di controllo unificato. Una volta configurato, Swarm fornisce un controllo completo dell'intero funzionamento del mining da un'unica interfaccia.


Attraverso l'interfaccia Swarm, è possibile eseguire attività di gestione critiche su più dispositivi contemporaneamente o singolarmente, tra cui modifiche alla configurazione del pool, riavvii dei dispositivi, regolazioni della frequenza e monitoraggio delle prestazioni. Questo approccio centralizzato riduce significativamente l'onere amministrativo della gestione di operazioni mining di grandi dimensioni, assicurando al contempo una configurazione coerente su tutti i dispositivi. Il sistema mantiene l'identità dei singoli dispositivi pur fornendo funzionalità di gestione collettiva, raggiungendo un equilibrio ottimale tra controllo granulare ed efficienza operativa.


Il cruscotto di Swarm presenta ogni dispositivo gestito con il suo stato attuale, le metriche delle prestazioni e i controlli di rapido accesso, consentendo una risposta rapida ai problemi di prestazioni o alle modifiche di configurazione. Questa funzionalità si rivela particolarmente preziosa per i minatori che gestiscono più dispositivi in luoghi diversi o che regolano frequentemente i parametri di mining in base alle condizioni di mercato o alle prestazioni del pool.


### Gestione della configurazione e impostazioni di sistema


La sezione Impostazioni di AxeOS offre un controllo completo su ogni aspetto configurabile del dispositivo Bitaxe, dalla connettività di rete ai parametri mining e all'ottimizzazione dell'hardware. La configurazione della rete inizia con l'impostazione del Wi-Fi, in cui si specificano il nome della rete e la password; AxeOS raccomanda nomi di rete di una sola parola senza spazi per garantire una connettività affidabile. Il sistema gestisce l'intero processo di configurazione wireless, consentendo la gestione e il monitoraggio in remoto.


La configurazione del Mining è incentrata sulle impostazioni dello strato, in cui si specifica l'URL del pool mining prescelto senza prefissi di protocollo o numeri di porta, che sono gestiti in campi separati. Il campo stratum user soddisfa i vari requisiti dei pool, supportando sia gli indirizzi Bitcoin per il solo mining che i sistemi di username per il pool mining, con la possibilità di aggiungere gli identificatori dei dispositivi per le operazioni su più dispositivi. La funzionalità stratum password, aggiunta di recente, supporta i pool che richiedono l'autenticazione, anche se la maggior parte dei pool pubblici opera senza questo requisito.


L'ottimizzazione dell'hardware attraverso la regolazione della frequenza e della tensione del core rappresenta la più potente capacità di regolazione delle prestazioni di AxeOS. A seconda della versione del dispositivo e del browser, queste impostazioni possono apparire come menu a discesa con configurazioni preimpostate o come campi aperti che consentono valori personalizzati. Le impostazioni predefinite della frequenza di 485 MHz e della tensione del core di 1200 mV garantiscono un funzionamento stabile per i test iniziali, mentre gli utenti avanzati possono ottimizzare questi parametri per ottenere le massime prestazioni o la massima efficienza in base ai loro requisiti specifici e alle condizioni operative.


### Manutenzione del sistema e funzioni avanzate


AxeOS include sofisticate funzionalità di manutenzione del sistema, progettate per mantenere il dispositivo Bitaxe al massimo delle prestazioni, fornendo al contempo informazioni diagnostiche per la risoluzione dei problemi e l'ottimizzazione. Il sistema di aggiornamento semplifica la gestione del firmware visualizzando l'ultima release disponibile direttamente nell'interfaccia e fornendo link diretti per il download dei file firmware ufficiali. Questa integrazione elimina la necessità di navigare manualmente nei repository GitHub o di gestire il download dei file, semplificando il processo di aggiornamento a pochi clic.


L'interfaccia di aggiornamento accetta i file del firmware denominati correttamente, in particolare esp-miner.bin e www.bin, garantendo la compatibilità e prevenendo gli errori di installazione. Per gli utenti che incontrano difficoltà con il processo di aggiornamento standard, AxeOS fornisce riferimenti a procedure complete di flash di fabbrica in grado di ripristinare le funzionalità originali dei dispositivi. Questo doppio approccio consente di gestire sia gli aggiornamenti di routine che gli scenari di ripristino.


Il sistema di registrazione fornisce una visione in tempo reale delle operazioni del dispositivo, visualizzando informazioni dettagliate sui modelli di chip ASIC, sul tempo di attività del sistema, sullo stato della connettività Wi-Fi, sulla memoria disponibile, sulle versioni del firmware e sulle revisioni della scheda. Questi registri si rivelano preziosi per gli sviluppatori e gli utenti avanzati che desiderano comprendere il comportamento del dispositivo, diagnosticare i problemi o ottimizzare le prestazioni. Il visualizzatore di log in tempo reale presenta dati operativi in tempo reale, tra cui l'elaborazione dei [nonce](https://planb.academy/resources/glossary/nonce), i calcoli di difficoltà e i parametri di invio del mining, offrendo una visibilità senza precedenti del processo mining stesso.


Altre caratteristiche del sistema includono il controllo dell'orientamento dello schermo per i dispositivi utilizzati in involucri personalizzati, l'inversione della polarità della ventola per configurazioni di raffreddamento particolari e il controllo automatico della ventola che regola il raffreddamento in base alla temperatura del ASIC. Il controllo manuale della velocità della ventola consente una gestione precisa del raffreddamento quando i sistemi automatici non soddisfano i requisiti specifici. Tutte le modifiche alla configurazione richiedono il salvataggio e il riavvio del dispositivo per avere effetto, garantendo un funzionamento stabile e prevenendo stati di configurazione parziali che potrebbero influire sulle prestazioni del mining.



# Comunità e collaborazione

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Panoramica dei contributi open source

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub e il suo ruolo nello sviluppo del software


GitHub rappresenta un cambiamento fondamentale nel modo in cui i progetti di sviluppo software vengono gestiti e condivisi dalla comunità globale dei programmatori. Come piattaforma basata sul cloud che ospita progetti di sviluppo software utilizzando Git, un sistema di controllo delle versioni distribuito, GitHub consente agli sviluppatori di collaborare senza problemi ai progetti, indipendentemente dalla loro posizione fisica. La piattaforma funge sia da strumento tecnico che da social network per i programmatori, consentendo loro di tenere traccia delle modifiche, unire gli aggiornamenti, mantenere diverse versioni del loro codice e contribuire a iniziative open-source come il progetto BitX di Open Source Miners United.


La potenza di GitHub risiede nella sua capacità di semplificare il complesso processo di sviluppo collaborativo. Quando più sviluppatori lavorano allo stesso progetto, GitHub fornisce l'infrastruttura per gestire i contributi, rivedere le modifiche, gestire i problemi del progetto e mantenere una documentazione completa. Questo approccio collaborativo ha reso GitHub un componente essenziale dei moderni flussi di lavoro di sviluppo del software, trasformando il modo in cui sia i singoli sviluppatori sia le grandi organizzazioni affrontano la gestione dei progetti e la condivisione del codice.


### Navigazione nella struttura GitHub Interface e del repository


La comprensione dell'interfaccia di GitHub inizia con il riconoscimento degli elementi chiave che compongono la pagina di un repository. La barra di navigazione superiore contiene diverse sezioni cruciali, tra cui Codice, Problemi, Richieste di prelievo, Discussioni, Azioni, Progetti, Sicurezza e Approfondimenti. Ogni sezione ha uno scopo specifico nell'ecosistema di gestione dei progetti, con la sezione Codice che mostra i file e le cartelle che compongono il progetto.


La struttura stessa del repository riflette l'approccio organizzativo dei manutentori del progetto. Alcuni repository contengono un solo file, magari un semplice script di shell, mentre altri, come il progetto hardware BitX, contengono numerosi file organizzati in directory e sottodirectory. Il nome del repository appare in evidenza e serve sia come identificativo che come breve descrizione dello scopo del progetto. Gli elementi interattivi essenziali includono il pulsante Watch per ricevere notifiche sugli aggiornamenti del repository, il pulsante Fork per creare copie personali del repository e il pulsante Star che funziona come un sistema di approvazione della comunità simile a una funzione "pollice in su".


La sezione About fornisce informazioni cruciali sul progetto in un formato condensato, tra cui una descrizione di una riga, informazioni sulla licenza e dettagli chiave sul progetto. Per il progetto BitX, questa sezione lo identifica come "hardware open source per minatori ASIC Bitcoin" e specifica la licenza GPL 3.0. La comprensione delle licenze è particolarmente importante perché GitHub opera come una piattaforma open-source in cui i repository pubblici sono accessibili all'intera comunità, ma i contenuti possono essere utilizzati e distribuiti solo in base alle regole di conformità di ciascuna licenza.


### Lavorare con i rami e le versioni del progetto


Il concetto di ramo rappresenta una delle caratteristiche più potenti di GitHub per la gestione di diverse versioni e tracce di sviluppo all'interno di un singolo progetto. Un ramo crea essenzialmente una copia o una versione modificata della base di codice principale, consentendo agli sviluppatori di lavorare su funzionalità specifiche, correzioni di bug o modifiche sperimentali senza influire sulla linea di sviluppo principale. Il ramo master serve in genere come versione predefinita e più stabile del progetto, mentre i rami aggiuntivi ospitano iterazioni diverse, fasi di test o varianti di prodotto completamente diverse.


Nel progetto hardware BitX esistono più rami per gestire versioni e configurazioni hardware diverse. Ad esempio, il ramo Ultra v2 contiene file specifici per quell'iterazione hardware, mentre il ramo Super 401 si concentra sulle implementazioni che utilizzano il chip S21 ASIC per una maggiore efficienza. Ogni ramo può essere più avanti o più indietro rispetto al ramo master, indicando l'entità delle modifiche e l'attività di sviluppo. Esaminando i diversi rami, gli utenti noteranno strutture di file, documentazione e persino rappresentazioni visive completamente diverse, che riflettono i requisiti e le specifiche uniche di ciascuna variante hardware.


Il sistema dei rami evita la confusione tra i collaboratori e gli utenti, separando chiaramente i diversi percorsi di sviluppo. Piuttosto che mescolare funzioni sperimentali e versioni stabili, o combinare diverse versioni hardware in un'unica posizione, i rami forniscono una separazione netta, mantenendo la possibilità di unire le modifiche apportate alla linea di sviluppo principale, quando necessario. Questo approccio organizzativo garantisce che gli utenti possano trovare facilmente la versione specifica di cui hanno bisogno, mentre gli sviluppatori possono lavorare sui miglioramenti senza interrompere il progetto principale.


### Contribuire attraverso i problemi


La sezione Problemi serve come canale di comunicazione principale tra gli utenti e i manutentori del progetto per segnalare problemi, suggerire miglioramenti e documentare bug. Tuttavia, è fondamentale capire che la sezione Problemi è pensata specificamente per problemi tecnici legittimi, piuttosto che per domande generiche o richieste di supporto. Quando gli utenti riscontrano malfunzionamenti, comportamenti inaspettati o identificano potenziali miglioramenti, la creazione di un problema ben documentato aiuta l'intera comunità, portando l'attenzione su problemi che possono interessare più utenti.


Una segnalazione efficace dei problemi richiede una documentazione dettagliata del problema, comprese le circostanze che hanno portato al problema, i passaggi per riprodurlo e tutti i dettagli tecnici rilevanti. Il progetto BitX dimostra questo principio attraverso vari problemi chiusi che mostrano il processo di risoluzione, dall'identificazione iniziale del problema alla discussione con la comunità fino alla risoluzione finale. Alcuni problemi si traducono in miglioramenti dell'hardware, come l'aggiunta di fori di montaggio per aumentare le opzioni di raffreddamento, mentre altri possono essere risolti attraverso la formazione degli utenti o gli aggiornamenti del software.


La distinzione tra Problemi e Discussioni è importante per mantenere un'interazione organizzata con la comunità. Mentre i Problemi si concentrano su problemi tecnici specifici, la sezione Discussioni offre un ambiente simile a un forum per domande, idee e impegno generale della comunità. Sebbene il server Discord sia diventato il canale di comunicazione principale per la comunità BitX, la sezione Discussioni di GitHub rimane disponibile per conversazioni più formali o ricercabili che beneficiano di una documentazione permanente e di una facile consultazione.


### Capire le richieste di pull


Le richieste di pull rappresentano il meccanismo attraverso il quale i collaboratori esterni propongono modifiche al repository di un progetto. Quando qualcuno identifica un miglioramento, una correzione di un bug o una nuova funzionalità che potrebbe essere utile al progetto, può creare una richiesta di pull per sottoporre le proprie modifiche alla revisione e alla potenziale integrazione nella base di codice principale. Questo processo garantisce che tutte le modifiche siano sottoposte a revisione prima di diventare parte del progetto ufficiale, mantenendo la qualità del codice e la coerenza del progetto e consentendo al contempo i contributi della comunità.


Il flusso di lavoro delle richieste di pull inizia tipicamente quando un collaboratore esegue un fork del repository, crea una propria copia dove può apportare modifiche e poi invia tali modifiche al progetto originale tramite una richiesta di pull. I manutentori del progetto possono quindi esaminare le modifiche proposte, discutere le modifiche con il collaboratore e infine decidere se unire le modifiche al progetto principale. Questo processo di revisione collaborativa aiuta a mantenere gli standard del progetto, incoraggiando al contempo la partecipazione e il miglioramento della comunità.


La comprensione dei tag e dei rilasci aggiunge un ulteriore livello alla gestione del progetto e al controllo delle versioni. I tag servono come marcatori nella timeline di sviluppo, identificando punti specifici che rappresentano versioni particolari o tappe fondamentali. Nei progetti hardware come BitX, i tag spesso corrispondono a numeri di modello o revisioni hardware specifici, fornendo chiari punti di riferimento per gli utenti che cercano versioni particolari. Le release, più comunemente utilizzate nei progetti software, rappresentano distribuzioni formali di funzionalità completate e correzioni di bug, spesso accompagnate da note di rilascio dettagliate e pacchetti scaricabili.


L'ecosistema GitHub crea un ambiente completo per la collaborazione open-source che va ben oltre la semplice condivisione di file. Comprendendo i vari componenti e il loro corretto utilizzo, i collaboratori possono partecipare efficacemente ai progetti, contribuire a migliorare i progetti di software e hardware e trarre vantaggio dalle conoscenze e dagli sforzi collettivi della comunità di sviluppo globale. Che si tratti di segnalare problemi, suggerire miglioramenti o contribuire al codice, GitHub fornisce gli strumenti e la struttura necessari per una collaborazione significativa nel mondo open-source.


## Contributo open-source pratico

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Partendo dalle basi della creazione di problemi e dell'esplorazione di progetti open source, questo capitolo si concentra sugli aspetti pratici della contribuzione diretta attraverso le richieste di pull e la gestione dei repository. Capire come gestire i repository fork, apportare modifiche e inviare richieste di pull rappresenta una competenza cruciale per qualsiasi sviluppatore che voglia contribuire in modo significativo ai progetti open source, sia che si tratti di sviluppo software che di progettazione hardware.


Il processo di apporto di modifiche al codice segue un flusso di lavoro standardizzato che garantisce l'integrità del progetto, consentendo al contempo lo sviluppo collaborativo. Questo flusso di lavoro prevede la creazione di una propria copia di un repository di progetto, l'esecuzione di modifiche in un ambiente controllato e la successiva proposta di tali modifiche al progetto originale attraverso un processo di revisione formale. Sebbene gli esempi di questo capitolo si concentrino principalmente sui contributi software, gli stessi principi e le stesse procedure si applicano anche ai progetti hardware che coinvolgono progetti di PCB, schemi e altra documentazione tecnica.


### Comprendere le forchette e la struttura del repository


La base per contribuire a qualsiasi progetto open source inizia con la creazione di un fork, che serve come copia personale del repository originale. Quando si naviga in un repository GitHub e si fa clic sul pulsante "fork", si crea una copia indipendente sotto il proprio account GitHub che mantiene una chiara connessione con la fonte originale. Questo repository biforcato appare nel proprio account con una chiara indicazione della sua origine, visualizzando un testo come "biforcato da [proprietario originale]/[nome del repository]" sotto il titolo del repository.


Il repository biforcato opera in modo indipendente dall'originale, consentendo di apportare modifiche senza influenzare il progetto principale. Tuttavia, mantiene la consapevolezza degli aggiornamenti del repository originale attraverso le funzioni di sincronizzazione di GitHub. Quando il repository originale riceve aggiornamenti che mancano al vostro fork, GitHub visualizza informazioni di stato come "Questo ramo è indietro di X commit" o "X commit avanti", fornendo una chiara visibilità della relazione tra il vostro fork e il repository a monte. È possibile sincronizzare il fork con il repository originale in qualsiasi momento facendo clic sul pulsante "Sync fork", che consente di inserire le ultime modifiche dalla fonte upstream.


La relazione tra il fork e il repository originale diventa particolarmente importante quando si iniziano ad apportare modifiche. Quando si implementano le modifiche e si effettua il commit sul fork, GitHub tiene traccia di queste differenze e le visualizza come commit prima del repository originale. Questo sistema di tracciamento consente il processo di richiesta di pull, in cui è possibile proporre le proprie modifiche per l'inclusione nel progetto principale, mantenendo una chiara cronologia di ciò che è stato modificato.


### Impostazione dell'ambiente di sviluppo


La creazione di un ambiente di sviluppo efficace richiede un'attenzione particolare sia agli strumenti di sviluppo generali che ai requisiti specifici del progetto. Visual Studio Code è un eccellente ambiente di sviluppo integrato (IDE) per la maggior parte dei contributi open source, in quanto fornisce funzioni essenziali per la modifica del codice, l'integrazione del controllo di versione e la gestione del progetto. Il primo componente critico è l'installazione e la configurazione dell'estensione Git, che consente una perfetta integrazione con i repository GitHub direttamente dall'ambiente di sviluppo.


Le versioni moderne di Visual Studio Code includono di solito il supporto Git per impostazione predefinita, ma è necessario autenticarsi con il proprio account GitHub per abilitare la funzionalità completa. Questo processo di autenticazione comporta l'accesso a GitHub attraverso l'IDE, che consente di clonare i repository, eseguire il commit delle modifiche e inviare gli aggiornamenti direttamente dall'ambiente di sviluppo. L'integrazione con GitHub appare come un'icona nella barra laterale sinistra, fornendo l'accesso alla clonazione dei repository, alla gestione dei rami e alle funzioni di sincronizzazione senza richiedere operazioni da riga di comando.


Per i progetti che coinvolgono sistemi embedded o piattaforme hardware specifiche, sono necessari strumenti aggiuntivi. L'estensione ESP-IDF rappresenta un componente cruciale per i progetti che si rivolgono ai microcontrollori ESP32, e richiede una compatibilità di versione specifica per garantire la corretta funzionalità. Il processo di installazione prevede la selezione della versione ESP-IDF appropriata, la configurazione dei percorsi degli strumenti e l'impostazione dell'ambiente del contenitore di sviluppo. La versione 5.1.3 rappresenta attualmente la configurazione consigliata per molti progetti basati su ESP32, anche se questi requisiti possono evolvere man mano che i progetti aggiornano le loro dipendenze e le loro catene di strumenti.


### Apportare modifiche e gestire i commit


Una volta configurato correttamente l'ambiente di sviluppo, il processo per apportare contributi significativi inizia con il download o la clonazione del repository biforcuto sul computer locale. È possibile farlo scaricando un file ZIP del contenuto del repository o utilizzando la funzionalità di clonazione integrata di Visual Studio Code, che offre un flusso di lavoro più snello per lo sviluppo continuo. Il processo di clonazione crea una copia locale del repository che rimane sincronizzata con il fork di GitHub, consentendo di lavorare offline mantenendo le funzionalità di controllo della versione.


Quando si lavora con il repository locale, si accede alla struttura completa del progetto, compresi i file di codice sorgente, i file di configurazione, la documentazione ed eventuali file di progettazione hardware. La maggior parte dei progetti firmware utilizza linguaggi di programmazione come il C per le funzionalità di base, con componenti aggiuntivi scritti in TypeScript per le interfacce utente o Java per utilità specifiche. La comprensione della struttura del progetto aiuta a identificare i file appropriati da modificare e garantisce che le modifiche siano in linea con i modelli architettonici e gli standard di codifica del progetto.


Il processo di commit rappresenta un aspetto fondamentale del controllo di versione che richiede un'attenzione particolare sia all'accuratezza tecnica che alla chiarezza della comunicazione. Prima di apportare qualsiasi modifica, è necessario comprendere a fondo il codice esistente e testare qualsiasi modifica nel proprio ambiente locale. La regola fondamentale della contribuzione open source sottolinea che non bisogna mai pubblicare codice non testato, perché questo può introdurre bug o vulnerabilità di sicurezza che si ripercuotono sull'intera comunità del progetto. Inoltre, non si devono mai inserire nei repository pubblici informazioni sensibili come password, token API o credenziali personali, poiché queste informazioni diventano permanentemente accessibili a chiunque abbia accesso al repository.


### Creare e gestire le richieste di pull


Il culmine del vostro contributo consiste nella creazione di una richiesta di pull, che serve come proposta formale per unire le vostre modifiche nel repository originale del progetto. Questo processo inizia nel vostro fork di GitHub, dove potete esaminare le differenze tra il vostro repository e la fonte a monte. L'interfaccia di GitHub mostra chiaramente il numero di commit avanti o indietro, fornendo una visibilità immediata sulla portata delle modifiche proposte. Prima di creare una richiesta di pull, è necessario assicurarsi che il proprio fork sia sincronizzato con le ultime modifiche a monte per ridurre al minimo i potenziali conflitti.


La creazione di una richiesta di pull efficace richiede qualcosa di più della semplice presentazione delle modifiche al codice. La descrizione della richiesta di pull è l'occasione per comunicare lo scopo, la portata e l'impatto delle modifiche ai manutentori del progetto e alla comunità. Una descrizione ben scritta spiega quali sono i problemi risolti dalle modifiche, come è stata implementata la soluzione e le potenziali implicazioni per altre parti del progetto. Questa documentazione diventa particolarmente importante per modifiche complesse che potrebbero non essere immediatamente evidenti dall'esame delle sole differenze di codice.


Il processo di revisione rappresenta un aspetto collaborativo dello sviluppo open source, in cui i manutentori del progetto e i collaboratori esperti valutano le modifiche proposte. È possibile richiedere revisori specifici che abbiano esperienza nelle aree su cui influiscono le modifiche, assicurando che membri della comunità competenti esaminino il vostro lavoro. Il processo di revisione può comportare più iterazioni, con i revisori che forniscono feedback, chiedono modifiche o ulteriori test. Questo processo di perfezionamento collaborativo aiuta a mantenere la qualità del codice, offrendo allo stesso tempo preziose opportunità di apprendimento per i collaboratori a tutti i livelli di esperienza.


Capire che non tutte le richieste di pull vengono accettate aiuta a stabilire aspettative appropriate per il processo di contribuzione. I manutentori del progetto possono rifiutare le richieste di pull per vari motivi, tra cui il disallineamento con gli obiettivi del progetto, i test insufficienti o l'esistenza di soluzioni alternative già in fase di sviluppo. Piuttosto che considerare il rifiuto come un fallimento, dovrebbe essere considerato come un'opportunità per imparare dal feedback, perfezionare l'approccio e potenzialmente contribuire con soluzioni alternative che soddisfino meglio le esigenze del progetto. La comunità open source vive di questo processo iterativo di proposta, revisione e perfezionamento che, in ultima analisi, fa progredire i progetti grazie allo sforzo collettivo e alla condivisione delle competenze.



## Cos'è il Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool rappresenta un approccio rivoluzionario al Bitcoin mining che risolve molti dei problemi che i minatori hanno con i pool mining tradizionali. Come pool Bitcoin mining completamente open-source, Public Pool cambia radicalmente il modello di distribuzione delle ricompense a cui i minatori sono abituati. A differenza dei pool mining tradizionali, in cui i partecipanti condividono le ricompense quando qualsiasi minatore del pool trova un blocco, Public Pool opera secondo il principio del mining in solitaria, in cui i singoli minatori conservano il 100% delle ricompense dei blocchi quando riescono a estrarre un blocco.


La caratteristica più interessante di Public Pool è la sua struttura a zero commissioni. Quando i minatori trovano con successo un blocco utilizzando Public Pool, ricevono l'intera ricompensa del blocco insieme a tutte le [commissioni di transazione](https://planb.academy/resources/glossary/transaction-fees) associate, senza alcuna deduzione per i costi di gestione del pool. Questo è in netto contrasto con i pool mining tradizionali che in genere applicano commissioni che vanno dall'1 al 3% delle ricompense mining. Il modello a zero commissioni rende Public Pool particolarmente interessante per i minatori che desiderano massimizzare i loro rendimenti potenziali mantenendo il pieno controllo sulle loro operazioni mining.


Per comprendere la posizione unica di Public Pool, è importante capire la differenza fondamentale tra mining in solitaria e mining in pool. Il vero mining in solitaria significa che si estrae in modo indipendente e si riceve l'intera ricompensa del blocco (attualmente 3,125 BTC + commissioni) se si trova un blocco, ma la probabilità è proporzionale al proprio tasso di hash rispetto all'intera rete, creando un'estrema variabilità che può durare mesi o anni tra una ricompensa e l'altra. I pool tradizionali combinano la potenza di hash per trovare blocchi più frequentemente, distribuendo le ricompense in modo proporzionale e fornendo un reddito costante e prevedibile. Per i minatori che hanno investito un capitale significativo in hardware e costi operativi, il mining puro è tipicamente impraticabile, indipendentemente dai suoi vantaggi filosofici: la varianza rende quasi impossibile coprire i costi dell'elettricità e recuperare gli investimenti. Questa realtà economica fa sì che la maggior parte dei minatori scelga il mining in pool per ragioni finanziarie pratiche. Public Pool opera come un pool di mining in solitaria, il che significa che si deve ancora affrontare la varianza del mining in solitaria (si viene ricompensati solo quando si trova personalmente un blocco), ma si beneficia dell'infrastruttura del pool e di un funzionamento trasparente e senza commissioni.


### Il vantaggio dell'Open Source e l'implementazione tecnica


L'impegno di Public Pool per lo sviluppo open-source offre ai minatori una trasparenza e un controllo senza precedenti sulle operazioni mining. L'intera base di codice è disponibile su GitHub, consentendo ai minatori di esaminare esattamente il funzionamento del software, modificarlo in base alle proprie esigenze e persino contribuire al suo sviluppo. Questa trasparenza risponde a una preoccupazione significativa della comunità mining riguardo alle configurazioni e alle pratiche sconosciute dei pool mining tradizionali.


L'architettura del software comprende sia la funzionalità principale del pool mining sia un repository separato per l'interfaccia utente, entrambi liberamente disponibili per il download e la modifica. I minatori possono eseguire Public Pool in varie configurazioni, compresi i container Docker, che lo rendono adattabile a diverse configurazioni hardware e preferenze tecniche. La documentazione completa fornita nei repository GitHub offre guide dettagliate all'installazione, opzioni di configurazione e istruzioni per la modifica, rendendolo accessibile ai minatori con diversi livelli di competenza tecnica.


La connessione a Public Pool richiede una configurazione minima rispetto alle tradizionali configurazioni mining. I minatori devono semplicemente configurare i loro dispositivi mining con i dettagli della connessione [Stratum](https://planb.academy/resources/glossary/stratum) e fornire il loro indirizzo Bitcoin come nome utente. È possibile aggiungere un nome di lavoratore opzionale dopo un separatore di punti per scopi organizzativi.


### Caratteristiche della comunità e modello di sostenibilità


Public Pool incorpora diverse caratteristiche innovative che rafforzano la comunità Bitcoin mining pur mantenendo il suo funzionamento a costo zero. La piattaforma visualizza statistiche complete, tra cui il tasso di hash totale dei minatori connessi, che era tipicamente compreso tra 1 e 2 PetaHash al secondo nel 2024 e circa 40 PH/s nel novembre 2025, e fornisce informazioni dettagliate sui dispositivi mining connessi. Particolarmente degna di nota è l'enfasi della piattaforma sull'hardware mining open-source, con i dispositivi contrassegnati da stelle che indicano progetti completamente open-source, completi di link ai rispettivi repository GitHub.


La sostenibilità dell'operazione a costo zero di Public Pool si basa su una partnership creativa del programma di affiliazione con i fornitori di hardware di mining. Quando i minatori acquistano attrezzature dalle aziende partner utilizzando il codice di sconto "SOLO", il cinquanta per cento dei guadagni degli affiliati sostiene i costi operativi di Public Pool, mentre il restante cinquanta per cento viene distribuito come ricompensa ai minatori che raggiungono le quote di difficoltà più alte ogni mese. Questo modello crea un rapporto simbiotico in cui i minatori ricevono sconti sull'acquisto di attrezzature, i venditori guadagnano clienti e Public Pool mantiene le sue operazioni senza addebitare commissioni dirette.


### Filosofia del decentramento e buone pratiche


Sebbene Public Pool offra un'eccellente alternativa ai pool mining tradizionali, è importante comprendere il suo ruolo nel contesto più ampio della decentralizzazione del Bitcoin. La piattaforma funge da trampolino di lancio verso l'obiettivo finale di singoli minatori che gestiscono le proprie pool mining. Gestire il proprio pool mining rappresenta il massimo livello di decentralizzazione, in quanto elimina la dipendenza da infrastrutture o software di terze parti, indipendentemente da quanto trasparenti o ben intenzionate possano essere.


La natura open-source di Public Pool lo rende una piattaforma di apprendimento ideale per i minatori che desiderano comprendere le operazioni del pool prima di implementare le proprie soluzioni. La disponibilità di guide all'installazione per diversi sistemi operativi e la documentazione esaustiva forniscono ai minatori le conoscenze necessarie per passare dall'utilizzo di Public Pool alla gestione della propria infrastruttura mining. Questo aspetto educativo si allinea con i principi fondamentali di auto-sovranità e decentralizzazione del Bitcoin, consentendo ai singoli minatori di assumere il controllo completo delle proprie operazioni mining, contribuendo al contempo alla sicurezza generale e alla decentralizzazione della rete Bitcoin.


L'interfaccia utente della piattaforma offre ai minatori funzionalità di monitoraggio dettagliate, tra cui lo stato dei lavoratori, le statistiche sul tasso di hash e le metriche delle prestazioni. Queste funzioni aiutano i minatori a ottimizzare le loro operazioni, imparando al contempo i principi di gestione dei pool che possono poi applicare alle proprie implementazioni di pool mining.


## Come installare Public-Pool su Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

La gestione della propria piscina Bitcoin mining a casa è diventata sempre più accessibile grazie all'hardware moderno e alle soluzioni software semplificate. Questo capitolo esplora l'implementazione pratica di una piscina pubblica a casa utilizzando hardware mini PC a prezzi accessibili e un software di gestione dei [nodi](https://planb.academy/resources/glossary/node) semplificato. Alla fine di questa guida, comprenderete i requisiti hardware, il processo di impostazione del software e la configurazione di base necessari per creare la vostra infrastruttura di pool mining.


### Requisiti hardware e configurazione


La base di qualsiasi installazione domestica di una piscina mining inizia con la scelta di un hardware appropriato che bilanci prestazioni, costi ed efficienza energetica. Un mini PC rappresenta la soluzione ideale per questa applicazione, in quanto offre una potenza di elaborazione sufficiente pur mantenendo un ingombro ridotto e un consumo energetico ragionevole. La configurazione consigliata comprende un processore Intel N100, che fornisce risorse di calcolo adeguate per le operazioni di pool, abbinato ad almeno un terabyte di storage NVMe per ospitare la [blockchain](https://planb.academy/resources/glossary/blockchain) Bitcoin e i dati associati.


Il requisito di archiviazione è particolarmente critico poiché l'esecuzione di un pool mining richiede il mantenimento di un nodo Bitcoin completamente sincronizzato. L'unità NVMe da un terabyte garantisce operazioni di lettura/scrittura veloci, essenziali per la sincronizzazione della blockchain e l'elaborazione delle [transazioni](https://planb.academy/resources/glossary/transaction-tx) in corso. Inoltre, una sufficiente allocazione di RAM supporta il funzionamento regolare del sistema operativo Linux sottostante e del software di gestione del nodo che coordinerà le attività del pool.


### Architettura software e gestione dei nodi


Lo stack software di un pool domestico mining si basa su una base Linux, che fornisce la stabilità e la sicurezza necessarie per le operazioni Bitcoin. In cima a questo sistema di base, un software specializzato nella gestione dei nodi come Umbrel crea un'interfaccia intuitiva per gestire l'infrastruttura Bitcoin. Questo approccio astrae gran parte della complessità tradizionalmente associata alla gestione dei nodi Bitcoin, rendendo il funzionamento del pool accessibile anche agli utenti che non hanno una preparazione tecnica approfondita.


Umbrel è una piattaforma di gestione dei nodi completa che gestisce l'installazione, la sincronizzazione e la manutenzione continua del [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core) attraverso un'interfaccia basata sul web. Il modello di app store della piattaforma consente una facile installazione di servizi aggiuntivi, compreso il software del pool mining, attraverso semplici operazioni point-and-click. Questa architettura garantisce che gli utenti possano concentrarsi sul funzionamento del pool piuttosto che sull'amministrazione del sistema, mantenendo comunque il pieno controllo della propria infrastruttura Bitcoin.


### Installazione e configurazione della piscina pubblica


L'installazione del software della piscina pubblica attraverso la piattaforma Umbrel dimostra la natura semplificata della moderna implementazione dell'infrastruttura Bitcoin . Il processo inizia con l'accesso all'app store di Umbrel attraverso l'interfaccia web, dove una semplice ricerca di "public pool" rivela il software per piscine mining disponibile. L'installazione richiede solo pochi clic: selezionare l'applicazione, confermare l'installazione e attendere il completamento del processo di configurazione automatica.


Il processo di installazione configura automaticamente le connessioni necessarie tra il software del pool pubblico e il nodo Bitcoin sottostante. Questa integrazione garantisce che il pool possa convalidare le transazioni, costruire modelli di blocco e distribuire il lavoro ai minatori collegati senza richiedere la configurazione manuale di complessi parametri di rete. Una volta completata l'installazione, l'interfaccia del pool diventa immediatamente accessibile attraverso la rete locale, fornendo funzionalità di monitoraggio e gestione in tempo reale.


### Collegamento dei minatori e considerazioni sulla rete


Per collegare l'hardware mining al pool appena creato è necessario configurare le impostazioni del pool del miner in modo che puntino alla propria infrastruttura locale. Ciò comporta la sostituzione dell'indirizzo predefinito del pool con l'indirizzo IP locale e il numero di porta appropriato assegnato durante l'installazione del pool pubblico. La modifica della configurazione reindirizza gli sforzi di calcolo dell'hardware mining dai pool esterni alla vostra infrastruttura domestica, consentendovi di mantenere il pieno controllo sulle operazioni mining e sui potenziali guadagni.


La configurazione della rete svolge un ruolo fondamentale per l'accessibilità e la funzionalità del pool. La configurazione della rete locale prevede in genere un indirizzamento IP standard, ma gli utenti possono incontrare variazioni nella risoluzione DNS a seconda della configurazione del router. Alcuni router forniscono servizi DNS locali che creano nomi amichevoli per i servizi locali, mentre altri richiedono l'accesso diretto all'indirizzo IP. Per un'accessibilità più ampia al di là della rete locale, può essere necessaria la configurazione del port forwarding sul router, anche se questo introduce ulteriori considerazioni sulla sicurezza che richiedono un'attenta valutazione dei rischi e dei benefici associati.


La creazione di un pool mining domestico rappresenta un passo significativo verso un'infrastruttura Bitcoin decentralizzata, in grado di fornire valore educativo e capacità pratiche mining, mantenendo il controllo completo sulle operazioni Bitcoin.


# Assemblaggio dell'hardware e risoluzione dei problemi

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Quali strumenti utilizzare?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Nel mondo della saldatura di dispositivi a montaggio superficiale (SMD), in particolare quando si lavora con progetti Bitaxe, avere gli strumenti giusti fa la differenza tra frustrazione e successo. Questa guida completa tratta l'attrezzatura essenziale necessaria per affrontare efficacemente i progetti di saldatura SMD, dagli utensili manuali di base alle attrezzature specializzate che miglioreranno le vostre capacità di saldatura.


Se volete consultare la documentazione sugli schemi, consultate questo [repo GitHub](https://github.com/skot/bitaxe-doc/tree/main).


### Utensili manuali di base e strumenti di precisione


Il fondamento di qualsiasi configurazione di saldatura SMD inizia con pinzette di qualità, che servono come strumenti principali per il posizionamento dei componenti. Due tipi di pinzette si rivelano molto utili in questo lavoro: quelle standard a punta dritta e quelle con una leggera curvatura sulla punta. La pinzetta a punta dritta è in grado di gestire la maggior parte dei componenti SMD presenti nei kit Bitaxe, mentre le pinzette a punta ricurva eccellono quando si lavora con componenti estremamente piccoli che richiedono un posizionamento preciso. Questi strumenti sono spesso inclusi nei kit di riparazione, come i set iFixit progettati per la riparazione dei telefoni, rendendoli facilmente accessibili alla maggior parte degli hobbisti.


A complemento delle pinzette, un buon paio di forbici diventa indispensabile per tagliare il nastro elettrico, che ha molteplici funzioni nei progetti di elettronica. Il nastro elettrico fornisce l'isolamento essenziale per i cavi e i componenti, e avere a disposizione nastro di qualità semplifica il processo di saldatura. Questi materiali di base possono essere reperiti presso i negozi di ferramenta o i rivenditori online, senza dover ricorrere a fornitori specializzati in elettronica.


### Applicazione e gestione della pasta saldante


L'applicazione della pasta saldante rappresenta uno degli aspetti più critici della saldatura SMD e gli strumenti giusti rendono questo processo accurato e piacevole. Le siringhe piccole e non affilate riempite di pasta saldante offrono un controllo eccezionale sul posizionamento della pasta. Questo metodo consente di applicare con precisione l'esatta quantità di pasta saldante necessaria per ogni giunzione e la maggior parte delle persone sviluppa rapidamente la tecnica corretta per controllare la pressione e la velocità del flusso attraverso la pratica.


La scelta della pasta saldante ha un impatto significativo sul successo della saldatura. ChipQuik TS391SNL50 si distingue come una pasta saldante eccezionale per i progetti Bitaxe e per i lavori SMD in generale. Questa pasta mantiene la giusta consistenza e le caratteristiche di fusione, evitando i problemi associati alle alternative più economiche che hanno punti di fusione eccessivamente bassi. Le paste saldanti di bassa qualità possono creare problemi in cui le giunzioni precedentemente saldate diventano nuovamente fluide quando si riscaldano le aree adiacenti, causando lo spostamento dei componenti e connessioni scadenti. Sebbene le paste saldanti di qualità rappresentino un investimento iniziale più elevato, i risultati migliori e la riduzione delle frustrazioni giustificano la spesa.


### Strumenti di risoluzione dei problemi e di pulizia


Anche i saldatori più esperti si imbattono in problemi che richiedono una correzione, rendendo l'attrezzatura di dissaldatura essenziale per qualsiasi kit di strumenti completo. Un impianto di dissaldatura, essenzialmente uno strumento a vuoto riscaldato, rimuove la saldatura in eccesso e corregge le connessioni a ponte tra i pin dei componenti. Questi strumenti funzionano in modo più efficace se combinati con il flussante, che migliora il flusso della saldatura e aiuta il processo di dissaldatura a funzionare in modo più efficiente.


Il flussante è disponibile in varie forme, tra cui quelle solide e liquide, e ha molteplici funzioni oltre a quella di assistenza alla dissaldatura. Quando la pasta saldante inizia a perdere la sua efficacia durante le sessioni di lavoro prolungate, l'applicazione di un flussante aggiuntivo ripristina le caratteristiche di flusso corrette e garantisce connessioni affidabili. Un piccolo strumento simile a un cucchiaio, spesso presente nei kit di riparazione di precisione, facilita l'applicazione accurata del flussante in aree specifiche senza contaminare i componenti circostanti.


La pulizia del pannello rappresenta la fase finale di un lavoro di qualità professionale e richiede l'uso di alcol isopropanolico e di una spazzola dedicata. Un vecchio spazzolino da denti funziona perfettamente a questo scopo, mentre una bottiglia da spremere contenente isopropanolo consente un'applicazione controllata della soluzione detergente. Questa combinazione rimuove i residui di flussante e i resti di pasta, lasciando le schede con un aspetto pulito e professionale che facilita anche l'ispezione dei giunti di saldatura.


### Attrezzature specializzate e strumenti avanzati


Per i progetti che coinvolgono circuiti integrati complessi, in particolare ASIC, gli stencil trasformano il processo di saldatura da un noioso posizionamento manuale a un'applicazione efficiente e accurata della pasta. Queste sagome tagliate con precisione assicurano uno spessore e un posizionamento uniformi della pasta, riducendo drasticamente il tempo necessario per i componenti complessi e migliorando l'affidabilità. L'investimento in stencil di qualità paga sia in termini di risparmio di tempo che di miglioramento dei risultati.


La gestione termica diventa cruciale quando si lavora con componenti di potenza, rendendo la pasta termica o il grasso termico forniture essenziali. Questi materiali assicurano il corretto trasferimento del calore tra i dissipatori di calore e i circuiti integrati, prevenendo i danni termici e garantendo un funzionamento affidabile. Materiali di qualità per l'interfaccia termica rappresentano un piccolo investimento che protegge componenti molto più costosi.


Il cuore di ogni impianto di saldatura SMD è la stazione di rilavorazione ad aria calda, che fornisce il calore controllato necessario per il lavoro a montaggio superficiale. Sebbene le stazioni economiche, comprese tra i 30 e i 50 dollari, siano in grado di fornire prestazioni adeguate, spesso mancano dell'affidabilità e della precisione delle apparecchiature di fascia più alta. Queste stazioni entry-level funzionano in genere efficacemente a 355°C e prevedono la riduzione automatica della temperatura quando la manopola viene rimessa nel suo supporto. Tuttavia, la loro affidabilità può essere incostante, con alcune unità che si guastano prematuramente. Per i lavori più impegnativi, investire in apparecchiature di qualità superiore, fornite da fornitori di elettronica specializzati, offre un valore migliore a lungo termine grazie a una maggiore affidabilità e a un controllo più preciso della temperatura.


La combinazione di questi strumenti crea una capacità di saldatura SMD completa che va ben oltre i progetti Bitaxe e si estende al lavoro elettronico generale. La comprensione del ruolo di ogni strumento e la scelta di un'attrezzatura di qualità adeguata al proprio livello di competenza e ai requisiti del progetto garantiscono risultati di successo e un'esperienza di saldatura piacevole.



## Risolvere i problemi di saldatura

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Il kit di ricetrasmettitori Bitaxe presenta sfide uniche durante l'assemblaggio che richiedono un'attenzione particolare all'orientamento dei componenti, alla prevenzione dei ponti di saldatura e alla corretta gestione del calore. La comprensione di questi problemi comuni e delle relative soluzioni è essenziale per il successo della costruzione del kit e per evitare costosi danni ai componenti. Questo capitolo esamina i problemi di saldatura più frequenti riscontrati durante l'assemblaggio del Bitaxe e fornisce tecniche pratiche per identificarli e risolverli.


### Orientamento e identificazione dei componenti


Il corretto orientamento dei componenti rappresenta uno degli aspetti più critici per il successo dell'assemblaggio di Bitaxe, in particolare per i MOSFET Q1 e Q2. Questi componenti sono caratterizzati da marcatori di orientamento distintivi che devono essere osservati attentamente durante l'installazione. Ogni MOSFET contiene un piccolo punto che corrisponde a specifiche disposizioni delle piazzole sulla scheda di circuito. La chiave per un corretto orientamento risiede nella comprensione della struttura fisica di questi componenti, che presentano quattro pin disposti con una piazzola grande e tre piazzole più piccole che non hanno alcun collegamento con la piazzola grande.


Quando si installano Q1 e Q2, esaminare attentamente sia il componente che la scheda. Il layout della scheda mostra chiaramente l'orientamento previsto attraverso la configurazione delle piazzole, con quattro pin posizionati in modo da corrispondere alla struttura del MOSFET. Prima di saldare qualsiasi componente di grandi dimensioni, verificare sempre l'orientamento confrontando i contrassegni fisici del componente con la disposizione delle piazzole della scheda. Questa semplice operazione di verifica evita la frustrazione di dover dissaldare e reinstallare componenti orientati in modo errato.


Le conseguenze di un orientamento errato vanno oltre i semplici problemi di funzionalità. I MOSFET orientati in modo errato possono creare malfunzionamenti del circuito che sono difficili da diagnosticare e possono richiedere la sostituzione completa dei componenti. La verifica dell'orientamento prima dell'applicazione del calore garantisce il corretto funzionamento del circuito ed evita la risoluzione di problemi non necessari durante il processo di assemblaggio.


### Gestione dei ponti di saldatura e delle saldature in eccesso


I ponti di saldatura rappresentano un'altra sfida comune nell'assemblaggio Bitaxe, in particolare per i componenti a passo fine come U10. Queste connessioni indesiderate tra pin adiacenti possono causare malfunzionamenti del circuito e richiedono tecniche di rimozione accurate. L'approccio più efficace prevede l'uso dello stoppino dissaldante, un materiale in rame intrecciato che assorbe la saldatura in eccesso quando viene riscaldato. Questa tecnica richiede pazienza e un'adeguata selezione degli strumenti per evitare di danneggiare i componenti più delicati.


Quando si affrontano i ponti di saldatura sui circuiti integrati, utilizzare un supporto per PCB o un morsetto articolato per tenere saldamente il componente durante il lavoro. Applicare un leggero calore all'area interessata e tirare con attenzione lo stoppino dissaldante sulle connessioni a ponte. La treccia di rame assorbe naturalmente la saldatura in eccesso, separando le connessioni indesiderate. Questo processo può richiedere più tentativi, ma la perseveranza consente di ottenere connessioni pulite e correttamente separate.


La prevenzione rimane l'approccio migliore alla gestione dei ponti di saldatura. L'uso di quantità adeguate di pasta saldante e il controllo costante della mano durante il posizionamento dei componenti riducono notevolmente la formazione dei ponti. Quando i ponti si formano, è bene affrontarli immediatamente piuttosto che sperare che non influiscano sul funzionamento del circuito. Anche ponti apparentemente minori possono causare problemi di funzionalità significativi, difficili da diagnosticare una volta che la scheda è completamente assemblata.


### Componenti critici e considerazioni speciali


Il convertitore buck U9 merita un'attenzione particolare per il suo ruolo critico nella conversione di 5 volt a 1,2 volt per il chip ASIC. Questo componente presenta sfide uniche a causa delle sue cinque piccole connessioni e della sua tendenza a guastarsi. Una corretta installazione richiede un'applicazione precisa della pasta saldante e un'attenta gestione del calore. Una quantità insufficiente di pasta saldante sotto U9 può causare connessioni scadenti che impediscono la corretta conversione della tensione, mentre una quantità eccessiva di pasta può creare ponti che causano il malfunzionamento del circuito.


L'U9 produce una firma audio distintiva quando si verificano problemi al ponte di saldatura, generando un rumore ad alta frequenza che differisce dal normale funzionamento del ASIC. Questa tecnica diagnostica uditiva può aiutare a identificare i problemi, anche se richiede un buon udito ad alta frequenza per essere rilevata. Quando la diagnosi audio non è possibile, diventa essenziale l'ispezione visiva. Esaminare attentamente tutti i collegamenti, alla ricerca di ponti o di una copertura insufficiente delle saldature.


Se U9 non emette gli 1,2 volt richiesti nonostante sia saldato correttamente, la causa è probabilmente una pasta saldante insufficiente. Rimuovere il componente, applicare una piccola quantità di pasta saldante aggiuntiva e reinstallarlo. Nei casi in cui i singoli pin non abbiano una copertura di saldatura adeguata, applicare con attenzione piccole quantità di pasta saldante in punti specifici utilizzando una pinzetta. La pasta saldante scorrerà naturalmente sotto il componente quando viene riscaldata, creando connessioni corrette per azione capillare.


### Gestione del calore e protezione dei componenti


Una corretta gestione del calore protegge i componenti sensibili dai danni termici, garantendo al contempo l'affidabilità delle saldature. Componenti come l'oscillatore a cristallo Y1 e U1 sono particolarmente sensibili all'esposizione prolungata al calore e richiedono un attento controllo della temperatura. Mantenere la temperatura del saldatore a 350 gradi Celsius, ma ridurre al minimo il tempo di applicazione del calore per evitare danni ai componenti. Tecniche di saldatura rapide ed efficienti proteggono questi componenti sensibili e garantiscono connessioni affidabili.


Il chip ASIC richiede tecniche di manipolazione speciali a causa della complessa struttura dei pin e della sensibilità alle sollecitazioni meccaniche. Quando si utilizzano gli stencil per l'applicazione della pasta saldante, assicurarsi che la copertura sia uniforme su tutti i pin per evitare che i componenti si posizionino in modo non uniforme. Se un'eccessiva quantità di pasta saldante causa un posizionamento non uniforme del ASIC, lasciare raffreddare completamente l'assemblaggio prima di apportare le dovute correzioni. Durante il riscaldamento, applicare una leggera pressione solo sui bordi etichettati del componente, mai sull'area centrale del die, per ottenere un corretto alloggiamento.


Il componente U8 presenta sfide uniche a causa dei suoi numerosi pin e del potenziale di piegatura dei conduttori. Quando i pin si piegano durante la manipolazione, utilizzare un supporto per PCB o una pinza articolata per fissare il componente e raddrizzare con attenzione i pin interessati. Lavorate lentamente e con pazienza per evitare di rompere i delicati conduttori. Capire che alcuni gruppi di pin dell'U8 sono collegati internamente può semplificare la risoluzione dei problemi, poiché i ponti tra questi pin specifici non influiscono sul funzionamento del circuito. Tuttavia, i ponti tra altri pin richiedono una rimozione accurata per garantire il corretto funzionamento.


## Come eseguire il debug del Bitaxe utilizzando AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Quando si lavora con i dispositivi Bitaxe mining, i guasti hardware possono manifestarsi in vari modi che possono non essere immediatamente evidenti. Capire come diagnosticare sistematicamente questi problemi utilizzando il sistema operativo AxeOS può far risparmiare molto tempo ed evitare inutili sostituzioni di componenti. Questo capitolo esplora le tecniche diagnostiche e le metodologie di risoluzione dei problemi che i tecnici esperti utilizzano per identificare problemi hardware specifici attraverso l'analisi del software.


### Comprendere gli indicatori di consumo energetico


Il primo e più critico indicatore diagnostico di AxeOS è il monitoraggio del consumo energetico. I normali dispositivi Bitaxe, compresi i modelli Bitaxe Ultra e Bitaxe Supra, consumano in genere da 10 a 17 watt durante il funzionamento standard. Questa misura di base serve come indicatore primario di salute dell'intero sistema. Quando il consumo di energia scende significativamente al di sotto di questo intervallo, in particolare al di sotto dei 3 watt, segnala un problema fondamentale del chip ASIC o dei suoi circuiti di supporto.


Gli scenari di basso consumo energetico richiedono un'attenzione immediata perché indicano che il chip mining è completamente non funzionante o funziona in uno stato gravemente degradato. Questa misura da sola può aiutare a distinguere rapidamente tra problemi di prestazioni e guasti hardware completi. La lettura dell'energia in AxeOS fornisce un feedback in tempo reale che consente di monitorare l'efficacia di qualsiasi tentativo di riparazione del dispositivo.


### Analisi delle misure di tensione del ASIC


La funzione di misurazione della tensione ASIC di AxeOS fornisce informazioni diagnostiche cruciali che aiutano a individuare la natura esatta dei problemi hardware. Quando si esaminano le letture di tensione, è necessario comprendere la relazione tra la tensione misurata e la tensione richiesta per diagnosticare correttamente i problemi. Il sistema visualizza sia la tensione erogata al chip ASIC sia la tensione richiesta dal chip al sistema di gestione dell'alimentazione.


Quando si osserva una misurazione della tensione del ASIC di esattamente 1,2 volt combinata con un consumo di energia inferiore a 3 watt, questa specifica combinazione indica un problema di saldatura con il chip ASIC o un ASIC completamente guasto. Questa lettura della tensione suggerisce che l'alimentazione raggiunge la posizione del chip, ma il chip stesso non funziona correttamente. L'ispezione fisica del die ASIC può rivelare crepe o altri danni visibili che spiegherebbero questo comportamento.


Uno scenario diagnostico diverso emerge quando si osserva un basso consumo di energia abbinato a letture di tensione richiesta molto basse, come 100 millivolt o 0,5 volt. Questo schema indica che il chip ASIC non riceve un'alimentazione di tensione adeguata, il che di solito indica problemi con il componente U9 del convertitore buck. Il convertitore buck è responsabile della regolazione precisa della tensione di cui i chip ASIC hanno bisogno per funzionare correttamente.


### Interpretazione dei dati di registro e comunicazione ASIC


Il sistema di registrazione di AxeOS fornisce informazioni preziose sulla comunicazione del chip ASIC con il sistema di controllo. Quando si accede ai registri tramite la funzione "show logs", la presenza di voci "ASIC results" conferma che il chip non solo è alimentato, ma sta anche elaborando attivamente il lavoro e restituendo i risultati. Questa comunicazione indica che il ASIC è saldato correttamente e mantiene il collegamento con il circuito di controllo.


L'assenza di risultati ASIC nei registri, soprattutto se combinata con altri sintomi, aiuta a restringere il problema a componenti specifici o a problemi di connessione. Questo approccio diagnostico consente di distinguere tra i chip che non rispondono completamente e quelli che potrebbero avere problemi di connessione intermittenti. L'analisi dei registri diventa particolarmente preziosa quando si risolvono problemi complessi in cui più sintomi possono suggerire cause diverse.


### Approccio sistematico alla risoluzione dei problemi


Quando si diagnosticano i problemi hardware di Bitaxe, seguendo un approccio sistematico si evita di trascurare i problemi critici e si garantisce un processo di riparazione efficiente. Iniziate documentando il consumo di energia e le letture di tensione, quindi mettete in relazione queste misure con i dati di registro per costruire un quadro completo del comportamento del sistema. Questo approccio metodico aiuta a identificare se i problemi derivano dal chip ASIC stesso, dal sistema di alimentazione o dai percorsi di comunicazione tra i componenti.


Nei casi in cui il problema sembra essere il convertitore buck U9, potrebbe essere necessaria un'ispezione fisica e un'eventuale risaldatura. Il componente U9 è particolarmente suscettibile a problemi di saldatura, soprattutto in situazioni di primo assemblaggio. Quando si sospettano problemi di regolazione della tensione, l'uso di un multimetro per verificare l'effettiva presenza di 1,2 volt sui pin del ASIC fornisce una conferma definitiva dei problemi di alimentazione. Se la tensione è presente sui pin ma il ASIC continua a non funzionare e l'ispezione fisica non rivela alcun danno, la sostituzione del chip ASIC diventa il passo logico successivo. Se i problemi persistono anche dopo la sostituzione del ASIC, il componente U2, che pilota il chip ASIC, potrebbe richiedere attenzione come elemento finale della sequenza di risoluzione dei problemi.


## Come eseguire il debug utilizzando l'USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Durante la risoluzione dei problemi dei dispositivi Bitaxe mining, l'accesso diretto al sistema di registrazione interno del dispositivo fornisce informazioni preziose che le interfacce basate sul Web non possono offrire. Questo capitolo spiega come stabilire una connessione seriale USB diretta al dispositivo Bitaxe utilizzando il framework ESP-IDF, consentendo il monitoraggio in tempo reale dei log di sistema, delle sequenze di avvio e dei messaggi di errore. Questo approccio di debug è particolarmente cruciale quando si ha a che fare con dispositivi che subiscono frequenti riavvii o guasti hardware, in quanto cattura tutte le informazioni diagnostiche che potrebbero andare perse durante i riavvii del sistema.


Il processo di debug richiede Visual Studio Code con l'estensione ESP-IDF, anche se è possibile utilizzare qualsiasi IDE compatibile. Questo metodo funziona con tutte le varianti di Bitaxe che includono una porta USB, compreso il Bitaxe Ultra 204 e altri modelli della serie. La connessione seriale diretta aggira le potenziali limitazioni dell'interfaccia web e fornisce un accesso non filtrato alle informazioni sullo stato interno del dispositivo.


### Impostazione della comunicazione seriale


La comunicazione con il dispositivo Bitaxe inizia con il collegamento del cavo USB e l'apertura del terminale ESP-IDF nell'ambiente di sviluppo. Il comando `idf.py monitor` avvia il processo di connessione, scansionando automaticamente le porte COM disponibili per stabilire una comunicazione UART con il chip ESP32 del dispositivo Bitaxe. In genere il sistema scorre le porte disponibili (COM3, COM4, COM16, ecc.) finché non trova la connessione corretta.


Una volta collegato, il terminale visualizza l'intera sequenza di avvio e i registri operativi in corso. Il processo di connessione iniziale può richiedere alcuni istanti, in quanto il sistema identifica la porta di comunicazione corretta. Se il rilevamento automatico della porta non riesce, è possibile specificare manualmente la porta COM attraverso l'interfaccia di selezione della porta dell'IDE. Questo canale di comunicazione diretta rimane attivo per tutto il funzionamento del dispositivo, fornendo un accesso continuo alla diagnostica del sistema e alle metriche delle prestazioni.


### Interpretare la sequenza di avvio e i registri di funzionamento normale


La sequenza di avvio fornisce informazioni fondamentali sulla configurazione hardware del dispositivo Bitaxe e sul processo di inizializzazione. I normali registri di avvio iniziano con le informazioni sulla versione dell'ESP-IDF, seguite dal caratteristico messaggio "Welcome to the Bitaxe. Hack the planet" che conferma l'avvenuto caricamento del firmware. Il sistema visualizza quindi la configurazione della frequenza ASIC, l'identificazione del modello del dispositivo e i dettagli sulla versione della scheda.


Un dispositivo correttamente funzionante mostra un'inizializzazione I2C riuscita e la regolazione della tensione ASIC impostata a 1,2 volt. I registri mostrano le informazioni sullo stato del GPIO e le sequenze di inizializzazione del Wi-Fi, seguite dalla configurazione del server DHCP e dall'assegnazione dell'indirizzo IP. Uno degli indicatori più importanti è il messaggio di rilevamento del chip ASIC, che dovrebbe riportare "detected one ASIC chip" per un dispositivo a chip singolo. Questa conferma convalida che l'hardware mining è collegato e comunica correttamente con il controllore ESP32.


I registri operativi rivelano l'esecuzione di più attività contemporanee sul dispositivo, tra cui la comunicazione API di strato, il coordinamento delle attività principali, la gestione delle attività ASIC e l'elaborazione delle attività di strato. Questi diversi identificatori di task aiutano a isolare i problemi da componenti specifici del sistema. Il funzionamento normale comprende la creazione di connessioni al pool, i messaggi di regolazione della difficoltà, l'accodamento e la rimozione dei lavori e la segnalazione della generazione di nonce. Le operazioni mining andate a buon fine visualizzano i risultati ASIC con i calcoli di difficoltà e le conferme di invio mining quando le quote raggiungono la soglia richiesta.


### Identificazione dei guasti hardware e dei modelli di errore


I guasti hardware si manifestano nei registri attraverso specifici schemi di errore che indicano quali componenti sono malfunzionanti. La modalità di guasto più comune riguarda gli errori di comunicazione I2C con specifici circuiti integrati sulla scheda Bitaxe. Ad esempio, i guasti alla comunicazione DS4432U appaiono come messaggi "ESP_ERROR_CHECK failed" con indicatori di timeout, indicando problemi di regolazione della tensione o di saldatura del componente U10 responsabile della comunicazione con il display.


Questi messaggi di errore includono informazioni di debug dettagliate, come il file sorgente specifico (main_ds4432u.c), la chiamata di funzione non riuscita e il core del processore che gestisce il task. Le informazioni di backtrace forniscono un contesto aggiuntivo per la risoluzione avanzata dei problemi. Modelli di errore simili possono verificarsi con il chip di controllo della temperatura e della ventola EMC2101, ciascuno dei quali genera firme di registro distintive che aiutano a identificare il componente guasto.


I problemi fisici dell'hardware si presentano spesso come cicli di errore ripetuti seguiti da riavvii del sistema. Se il dispositivo produce un rumore udibile durante il funzionamento, ciò indica in genere problemi di saldatura, come ponti tra i pin dei componenti o giunti di saldatura inadeguati. Sebbene questi problemi meccanici non siano sempre generate voci di registro specifiche, creano condizioni operative instabili che si manifestano con frequenti crash e cicli di riavvio nell'output di monitoraggio.


### Strategie avanzate di risoluzione dei problemi


Il monitoraggio seriale offre diversi vantaggi rispetto alle interfacce di debug basate sul Web, in particolare per i guasti intermittenti o per i dispositivi che si riavviano frequentemente. L'acquisizione continua dei registri garantisce che nessuna informazione diagnostica venga persa durante i riavvii del sistema, a differenza delle interfacce web che possono perdere i dati durante gli eventi di disconnessione. Questa capacità di registrazione completa consente di identificare gli schemi dei guasti e di correlare condizioni di errore specifiche a fattori hardware o ambientali.


Quando si analizzano i dispositivi problematici, concentrarsi sulla sequenza di eventi che portano ai guasti piuttosto che sui messaggi di errore isolati. Una comunicazione ASIC riuscita dovrebbe mostrare cicli regolari di elaborazione dei lavori, generazione di nonce e invio di azioni. La mancanza di risultati ASIC nei registri indica guasti di comunicazione tra l'ESP32 e il chip mining, spesso causati da problemi di alimentazione, tracce danneggiate o guasti dei componenti.


Per una risoluzione sistematica dei problemi, documentate gli schemi di errore e i guasti specifici dei componenti prima di richiedere il supporto della comunità. I registri dettagliati degli errori, che includono gli identificatori specifici dei chip e le modalità di guasto, consentono agli utenti esperti di fornire indicazioni mirate per la riparazione, come le procedure di sostituzione dei componenti o le correzioni di saldatura. Questo approccio metodico al debug dell'hardware migliora significativamente le percentuali di successo delle riparazioni e riduce i tempi di risoluzione dei problemi complessi.


# Personalizzazione avanzata

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Modificare il PCB

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad è uno dei più potenti strumenti open-source disponibili per la progettazione e il routing di circuiti stampati (PCB). Questo software di livello professionale consente a ingegneri e hobbisti di creare progetti elettronici complessi posizionando i componenti su schede virtuali e tracciando le intricate tracce che collegano i componenti tra loro. Ciò che rende KiCad particolarmente prezioso per scopi didattici e di sviluppo è la sua natura completamente open-source, che consente agli utenti di modificare, personalizzare e imparare dai progetti esistenti senza restrizioni di licenza.


Il progetto Bitaxe esemplifica la potenza dello sviluppo hardware open-source, fornendo un progetto completo di PCB che gli utenti possono esaminare, modificare e personalizzare in base alle loro esigenze specifiche. Questa accessibilità crea un eccellente ambiente di apprendimento in cui studenti e professionisti possono esplorare progetti di PCB reali, sviluppando al contempo la loro comprensione dei sistemi elettronici. La possibilità di personalizzare elementi visivi come i loghi offre un punto di ingresso accessibile agli utenti che potrebbero essere intimoriti dalla complessità tecnica della progettazione elettronica.


### Impostazione dell'ambiente KiCad


Prima di iniziare qualsiasi lavoro di personalizzazione, è essenziale una corretta configurazione dell'ambiente di sviluppo. Il repository Bitaxe deve essere scaricato sul computer locale, in genere tramite la funzionalità di download ZIP di GitHub. Questo repository contiene tutti i file di progetto necessari, compresi i file di progetto di KiCad, le librerie di componenti e la documentazione di progettazione necessaria per la modifica.


L'installazione di KiCad deve essere completata utilizzando la distribuzione ufficiale dal sito web di KiCad, per garantire la compatibilità con i file di progetto e l'accesso alle funzionalità più recenti. Una volta che sia il repository che KiCad sono stati installati correttamente, per aprire il progetto è necessario navigare fino al file di progetto Bitaxe Ultra KiCad all'interno della struttura del repository scaricato. Questo file di progetto funge da hub centrale che collega tutti i file di progettazione associati, le librerie di componenti e le impostazioni di configurazione.


La vista iniziale di un progetto di PCB complesso può sembrare opprimente, con numerosi componenti, tracce e livelli che creano un paesaggio visivo denso. Tuttavia, la funzionalità di visualizzazione 3D di KiCad fornisce uno strumento prezioso per comprendere il layout fisico e le relazioni spaziali all'interno del progetto. Questa prospettiva tridimensionale trasforma la rappresentazione schematica astratta in una visualizzazione realistica del prodotto finale, facilitando la comprensione del posizionamento dei componenti e dell'estetica complessiva del progetto.


### Processo di personalizzazione del logo


La personalizzazione dei loghi sui progetti di PCB rappresenta una delle modifiche più accessibili per gli utenti che non conoscono KiCad, in quanto richiede conoscenze tecniche minime e fornisce risultati visivi immediati. Il processo inizia con lo strumento di conversione delle immagini, che trasforma i file immagine standard in formati di impronta compatibili con il software di progettazione PCB. Questo processo di conversione richiede un'attenzione particolare ai parametri di dimensionamento, tipicamente misurati in millimetri per garantire una scala corretta sulla scheda finale prodotta.


Il flusso di lavoro di conversione delle immagini prevede diverse fasi critiche che determinano l'aspetto finale e il posizionamento dei loghi personalizzati. La selezione delle immagini di partenza deve privilegiare i disegni ad alto contrasto che si adattano bene al processo di serigrafia utilizzato nella produzione dei PCB. La specifica delle dimensioni diventa cruciale, in quanto i loghi devono essere sufficientemente grandi da rimanere leggibili dopo la produzione, senza interferire con il posizionamento o la funzionalità dei componenti. La scelta tra gli strati serigrafici anteriori e posteriori influisce sia sulla visibilità che sulla produzione.


La gestione delle librerie di impronte rappresenta un aspetto fondamentale della personalizzazione di KiCad e richiede agli utenti di capire come il software organizza e accede agli elementi di progetto. L'aggiunta di loghi personalizzati comporta la creazione di nuove librerie di impronte o la modifica di quelle esistenti, quindi il collegamento corretto di queste librerie all'interno della struttura del progetto. Questo processo garantisce che gli elementi personalizzati rimangano accessibili in diverse sessioni di progettazione e possano essere facilmente condivisi con altri membri del team o collaboratori.


### Esplorazione e comprensione del design avanzato


Oltre alla semplice personalizzazione del logo, KiCad offre strumenti potenti per l'esplorazione e la comprensione di progetti PCB complessi. Il sistema di gestione dei livelli consente agli utenti di visualizzare in modo selettivo diversi aspetti del progetto, dal posizionamento e instradamento dei componenti alle specifiche di produzione e alle informazioni di assemblaggio. Questo approccio a livelli consente di analizzare in dettaglio elementi specifici del progetto senza l'ingombro visivo di componenti non correlati.


L'analisi del percorso delle tracce rappresenta uno degli aspetti più istruttivi dell'esplorazione dei circuiti stampati, in quanto rivela il flusso delle connessioni elettriche tra i componenti e i sottosistemi. Seguendo singole tracce o gruppi di segnali correlati, gli utenti possono sviluppare la comprensione della funzionalità del circuito e delle decisioni di progettazione. Ad esempio, l'esame delle reti di distribuzione dell'alimentazione rivela come i componenti di regolazione e filtraggio della tensione lavorino insieme per fornire un'alimentazione pulita e stabile ai componenti elettronici sensibili.


La relazione tra la progettazione schematica e il layout fisico diventa evidente attraverso un attento esame del posizionamento dei componenti e delle decisioni di instradamento. La comprensione del motivo per cui specifici componenti sono posizionati in particolari posizioni, di come le considerazioni termiche influenzino le decisioni di layout e di come i requisiti di integrità del segnale guidino le scelte di instradamento fornisce preziose indicazioni sulle pratiche professionali di progettazione dei circuiti stampati. Queste conoscenze si rivelano preziose per gli utenti che sviluppano i propri progetti o modificano quelli esistenti per applicazioni specifiche.


Gli strumenti di verifica e controllo delle regole di progettazione di KiCad assicurano che le modifiche mantengano la compatibilità elettrica e di produzione. Questi sistemi automatizzati aiutano a prevenire gli errori di progettazione più comuni, istruendo al contempo gli utenti sugli standard e le best practice del settore. L'integrazione della visualizzazione 3D con i dati di progettazione elettrica crea un potente ambiente di apprendimento in cui i concetti teorici diventano tangibili attraverso la rappresentazione visiva e l'esplorazione interattiva.


## Come creare un file di fabbrica?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

La creazione di un firmware personalizzato per i dispositivi mining basati su ESP richiede un'attenzione particolare alla configurazione, alle dipendenze e al processo di creazione corretto. Questa guida completa illustra l'intero processo di creazione di binari del firmware standard e di file di fabbrica che includono impostazioni preconfigurate, rendendo più efficiente la distribuzione e riducendo i tempi di configurazione per gli utenti finali.


Si noti che questo capitolo è piuttosto tecnico e può essere semplicemente sfogliato se si è curiosi.


### Impostazione dell'ambiente di sviluppo


Per iniziare lo sviluppo del firmware ESP-Miner è necessario creare un ambiente di sviluppo adeguato in Visual Studio Code, idealmente su una distribuzione Linux. L'estensione ESP-IDF è la pietra miliare di questa configurazione, in quanto fornisce gli strumenti necessari e l'integrazione del framework per lo sviluppo ESP32. Quando si installa l'estensione ESP-IDF per la prima volta, gli utenti incontrano una guida all'installazione che facilita il processo di configurazione.


Una considerazione critica nel processo di configurazione riguarda la scelta della versione ESP-IDF appropriata. Sebbene in precedenza fosse consigliata la versione 5.1.3, l'esperienza pratica ha rivelato che questa versione può causare problemi di costruzione che complicano il processo di sviluppo. L'approccio consigliato prevede ora l'uso della versione 5.3 Beta 1 di ESP-IDF, che si è dimostrata in grado di risolvere queste complicazioni di costruzione e di garantire il corretto funzionamento dei dispositivi Bitaxe. Il processo di installazione richiede la selezione dell'opzione di installazione Express e la scelta specifica della versione 5.3 Beta 1 tra le opzioni disponibili.


La configurazione dell'ambiente di sviluppo va oltre l'installazione di ESP-IDF e comprende la corretta configurazione del terminale. Visual Studio Code offre diversi metodi per accedere alle funzionalità di ESP-IDF, tra cui l'opzione della palette dei comandi per aprire un terminale ESP-IDF o l'utilizzo dell'icona del terminale dedicata situata nell'interfaccia. Questo ambiente terminale specializzato garantisce il corretto funzionamento di tutti i comandi ESP-IDF e fornisce l'accesso all'intera catena di strumenti.


### Configurazione delle impostazioni di ESP-Miner


Il file di configurazione rappresenta il cuore del processo di personalizzazione dell'ESP-Miner e contiene tutti i parametri essenziali che definiscono il funzionamento del dispositivo nell'ambiente di destinazione. Questa configurazione comprende le impostazioni di rete, le connessioni al pool mining e i parametri specifici dell'hardware che devono essere adattati allo specifico scenario di implementazione.


La configurazione di rete è il componente principale del processo di configurazione e richiede la specificazione delle credenziali Wi-Fi, compresi SSID e password. Piuttosto che utilizzare valori segnaposto come "test", le configurazioni di produzione devono includere le credenziali di rete effettive che il dispositivo utilizzerà nel suo ambiente operativo. La configurazione consente inoltre di gestire diverse configurazioni di pool mining, supportando sia configurazioni di pool privati con indirizzi IP specifici sia pool pubblici come public-pool.io con le relative impostazioni di porta.


I parametri di configurazione specifici del Mining includono l'impostazione dello stratum utente, che in genere corrisponde all'indirizzo del Bitcoin dove devono essere indirizzate le ricompense del mining. Altri parametri hardware, come le impostazioni di frequenza, le configurazioni di tensione e le specifiche del tipo di ASIC devono essere in linea con la piattaforma hardware di destinazione. Il repository GitHub fornisce esempi preconfigurati per diverse varianti hardware, come la configurazione BM1368 progettata per i dispositivi Super e le impostazioni BM1366 per le varianti Ultra. Le specifiche della versione della scheda, come l'impostazione della versione della porta su 401 per le revisioni hardware più recenti, garantiscono la compatibilità con le caratteristiche specifiche del dispositivo di destinazione.


### Creazione del Web Interface e del firmware principale


Il progetto ESP-Miner incorpora una sofisticata interfaccia web che richiede una compilazione separata prima che possa iniziare il processo di creazione del firmware principale. Questa interfaccia web, denominata firmware AxeOS, fornisce agli utenti un'interfaccia di gestione completa per il monitoraggio e il controllo dei dispositivi mining.


Il processo di creazione dell'interfaccia web inizia navigando nella directory del server HTTP all'interno della struttura principale del repository, in particolare nella sottodirectory AxeOS. Questa posizione contiene l'applicazione web basata su Node.js che richiede l'installazione delle dipendenze tramite il comando npm install. Il sistema di compilazione presuppone che Node.js sia correttamente installato sul sistema di sviluppo, in quanto rappresenta un requisito fondamentale per il processo di compilazione dell'interfaccia web.


Dopo l'installazione delle dipendenze, il comando npm run build compila i componenti dell'interfaccia web, creando i file necessari che verranno incorporati nel firmware ESP32. Questo processo di compilazione genera risorse web ottimizzate che forniscono le funzionalità dell'interfaccia utente mantenendo un uso efficiente della memoria sulla piattaforma ESP32. Il completamento di questa fase di compilazione è essenziale prima di procedere alla compilazione del firmware principale, poiché il firmware ESP-Miner incorpora questi componenti dell'interfaccia web come funzionalità integrali.


### Creazione di file di fabbrica con configurazione integrata


La creazione di file di fabbrica rappresenta una strategia di distribuzione avanzata che incorpora le impostazioni di configurazione direttamente nel firmware binario, eliminando la necessità di configurazione manuale durante l'impostazione del dispositivo. Questo approccio si rivela particolarmente prezioso per le distribuzioni su larga scala o per le situazioni in cui è essenziale una configurazione coerente tra più dispositivi.


Il processo di creazione del file di fabbrica inizia con la generazione di una configurazione binaria dal file di configurazione CSV utilizzando lo strumento generatore di partizioni NVS di ESP-IDF. Questo strumento, che si trova nella directory dei componenti ESP-IDF sotto nvs-flash/nvs-partition-generator, converte la configurazione leggibile dall'uomo in un formato binario adatto alla memorizzazione diretta nella memoria flash. Lo script nvs-partition-gen.py elabora il file config.csv e genera un file config.binary che si rivolge allo spazio di memoria 0x6000.


L'assemblaggio finale dei file di fabbrica utilizza script di fusione specializzati che combinano i binari del firmware principale con i dati di configurazione. Il repository offre diverse opzioni di unione, tra cui uno script di unione standard per i file di fabbrica di base e uno script di unione comprensivo di configurazione per i file di fabbrica completi. Lo script merge-bin-with-config.sh crea file di fabbrica che includono sia la funzionalità del firmware che le impostazioni preconfigurate, ottenendo un pacchetto di distribuzione completo. Questo approccio consente di creare file di fabbrica specifici per il dispositivo, come le versioni personalizzate per i dispositivi Bitaxe Ultra con revisioni specifiche della scheda, pur mantenendo la flessibilità di creare file di fabbrica generici generate senza configurazioni incorporate per gli scenari che richiedono una flessibilità di configurazione manuale.


I file di fabbrica completati forniscono ai team di distribuzione binari pronti per l'uso che includono tutti i componenti firmware e le impostazioni di configurazione necessarie, semplificando il processo di provisioning del dispositivo e garantendo parametri operativi coerenti tra i dispositivi mining distribuiti.


## Come utilizzare Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Il Bitaxe Web Installer rappresenta un approccio semplificato alla gestione del firmware per i dispositivi Bitaxe, fornendo agli utenti molteplici opzioni di installazione attraverso un'interfaccia basata sul web. Questo strumento completo elimina la complessità tradizionalmente associata agli aggiornamenti del firmware e alle nuove installazioni, rendendo la gestione del dispositivo accessibile agli utenti indipendentemente dalle loro competenze tecniche. La comprensione dell'uso corretto di questo programma di installazione è fondamentale per mantenere le prestazioni ottimali del dispositivo e per evitare le insidie più comuni che possono rendere i dispositivi temporaneamente inutilizzabili.


### Requisiti di accesso e compatibilità del browser


Il programma di installazione web di Bitaxe è accessibile attraverso l'URL dedicato [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (quello presentato nel video è ora deprecato) e funge da hub centrale per tutte le attività di installazione del firmware. Tuttavia, il funzionamento di questo strumento basato sul web richiede la compatibilità del browser, in quanto il programma di installazione si basa su tecnologie web specifiche che non sono universalmente supportate da tutti i browser. Chrome è il browser principale consigliato per il programma di installazione, in quanto garantisce la piena compatibilità con tutte le caratteristiche e le funzioni. Sebbene altri browser basati su Chromium possano offrire funzionalità simili, alternative popolari come Brave e Firefox non dispongono del necessario supporto per il web serial API, rendendoli incompatibili con le operazioni principali del programma di installazione.


Questa limitazione del browser deriva dal fatto che l'installatore si affida alla comunicazione seriale diretta con i dispositivi Bitaxe attraverso l'interfaccia web. La seriale web API, che consente questa comunicazione, rimane uno standard web relativamente nuovo che non ha ancora raggiunto l'adozione universale dei browser. Gli utenti che tentano di accedere al programma di installazione attraverso browser non supportati incontreranno problemi di connessione e l'impossibilità di comunicare con i loro dispositivi, rendendo necessario il passaggio a un browser compatibile prima di procedere con qualsiasi attività di installazione.


### Requisiti di alimentazione e preparazione del dispositivo


I dispositivi Bitaxe presentano requisiti di alimentazione diversi a seconda del modello e della versione specifici, per cui una corretta gestione dell'alimentazione è essenziale per il successo dell'installazione del firmware. I dispositivi con versione 204 o inferiore possono funzionare esclusivamente tramite alimentazione USB, assorbendo dal computer collegato una corrente sufficiente a mantenere il funzionamento durante il processo di flashing. Questa disposizione semplificata dell'alimentazione rende queste versioni precedenti particolarmente convenienti per gli aggiornamenti del firmware, in quanto gli utenti devono solo collegare un singolo cavo USB per iniziare il processo di installazione.


Tuttavia, i dispositivi con la versione 205 e successive richiedono fonti di alimentazione esterne oltre alla connessione USB, a causa delle modifiche apportate al consumo di energia e alla progettazione dei circuiti nelle nuove revisioni hardware. Questi dispositivi non sono in grado di assorbire un'alimentazione adeguata solo tramite USB e devono essere collegati ai loro alimentatori standard durante l'installazione del firmware. Se non si fornisce un'alimentazione adeguata a questi nuovi dispositivi, l'installazione non andrà a buon fine e il processo di aggiornamento del firmware potrebbe essere danneggiato.


Il processo di connessione fisica richiede una tempistica specifica e la manipolazione dei pulsanti per garantire una comunicazione corretta tra il programma di installazione e il dispositivo. Gli utenti devono tenere premuto il pulsante di avvio del dispositivo Bitaxe prima di collegare il cavo USB-C al computer. Questa sequenza porta il dispositivo in modalità bootloader, consentendo all'installatore di comunicare direttamente con la memoria del firmware del dispositivo. Se si collega il cavo USB prima di premere il pulsante di avvio, il dispositivo funzionerà normalmente anziché in modalità bootloader, necessaria per l'installazione del firmware, impedendo all'installatore di stabilire il canale di comunicazione necessario.


### Opzioni di installazione e relative applicazioni


Il programma di installazione web di Bitaxe offre quattro opzioni di installazione distinte, ciascuna progettata per casi d'uso e configurazioni specifiche del dispositivo. La versione 4.0.1 di Bitaxe Superboard rappresenta il firmware più recente per i dispositivi del modello Super, mentre la versione 4.0.2 è prevista per il futuro. Questa opzione comprende sia le varianti di fabbrica che quelle di aggiornamento, offrendo flessibilità nell'approccio all'installazione in base alle esigenze dell'utente e allo stato del dispositivo.


Le installazioni di fabbrica rappresentano sostituzioni complete del firmware che rispecchiano il processo di produzione originale, comprese procedure complete di autotest che verificano la funzionalità del dispositivo in tutti i sistemi. Quando gli utenti scelgono un'installazione di fabbrica, l'installatore esegue una cancellazione completa del firmware e dei dati di configurazione esistenti, sostituendoli con un'installazione fresca e pulita, identica a quella applicata durante la produzione. Questo processo include un autotest automatico che convalida il corretto funzionamento dell'hardware, richiedendo agli utenti di riavviare i dispositivi al termine della procedura prima di poter riprendere il normale funzionamento. Le installazioni di fabbrica si rivelano particolarmente utili quando i dispositivi presentano problemi persistenti o quando gli utenti desiderano riportare i loro dispositivi alle specifiche originali di fabbrica.


Le installazioni di aggiornamento offrono un approccio più conservativo, preservando i dati di configurazione esistenti e aggiornando solo i componenti principali del firmware. Questa opzione è ideale per gli utenti che hanno personalizzato le impostazioni del dispositivo e che desiderano mantenere le proprie configurazioni personali pur beneficiando dei miglioramenti e delle correzioni del firmware. Il processo di aggiornamento riguarda solo i componenti del firmware che necessitano di modifiche, lasciando intatte le impostazioni specifiche dell'utente, le credenziali WiFi e gli indirizzi Bitcoin durante il processo di installazione.


### Considerazioni critiche sull'installazione e sulla protezione dei dati


La distinzione tra installazioni di fabbrica e di aggiornamento ha implicazioni significative per la configurazione del dispositivo e la conservazione dei dati dell'utente. Le installazioni di fabbrica eseguono la cancellazione completa del dispositivo, rimuovendo tutte le impostazioni configurate dall'utente, comprese le credenziali WiFi, gli indirizzi Bitcoin e tutti i parametri personalizzati del dispositivo. Dopo un'installazione di fabbrica, gli utenti devono riconnettersi alla rete WiFi predefinita del dispositivo e riconfigurare tutte le impostazioni personali da zero, trattando essenzialmente il dispositivo come se fosse nuovo di fabbrica.


Le installazioni di aggiornamento richiedono un'attenzione particolare all'opzione di cancellazione del dispositivo presentata durante il processo di installazione. Il programma di installazione chiederà agli utenti la domanda "Vuoi cancellare il dispositivo prima di installare Bitaxe Flasher?", accompagnata dall'avviso che tutti i dati presenti sul dispositivo andranno persi. Gli utenti che eseguono installazioni di aggiornamenti devono rifiutare questa opzione facendo clic su "Avanti" anziché confermare l'operazione di cancellazione. L'accettazione dell'opzione di cancellazione durante l'installazione di un aggiornamento rimuove il file di configurazione del dispositivo, rendendolo potenzialmente non funzionante fino al ripristino della configurazione corretta. Questa situazione non danneggia in modo permanente il dispositivo, ma crea inutili complicazioni e richiede ulteriori passaggi di configurazione per ripristinare il normale funzionamento.


Il processo di installazione procede automaticamente dopo che gli utenti hanno effettuato e confermato le loro scelte. Il programma di installazione gestisce tutti gli aspetti tecnici del trasferimento e della verifica del firmware, fornendo indicatori di avanzamento e aggiornamenti di stato durante l'intero processo. Questo approccio automatizzato elimina la necessità per gli utenti di comprendere le complesse procedure di installazione del firmware, garantendo al contempo risultati affidabili e coerenti tra i diversi modelli di dispositivi e le diverse versioni del firmware.


## Come creare e ordinare il PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Questo capitolo si concentra sul processo pratico di generazione di file di produzione da progetti KiCad e sull'ordinazione di PCB professionali da produttori online. Utilizzando il progetto Bitaxe come esempio, si illustra il flusso di lavoro completo, dalla generazione dei file all'ordine a un produttore di PCB.


### Comprendere il processo di produzione dei PCB


Il passaggio da un progetto KiCad completato a un PCB fisico comporta diverse fasi critiche che colmano il divario tra la progettazione digitale e la produzione fisica. Quando si lavora a progetti complessi come il Bitaxe, l'editor PCB di KiCad offre una visione completa del progetto, visualizzando tutti i componenti e le loro interconnessioni attraverso tracce colorate. Le linee rosse e blu che si vedono rappresentano le connessioni elettriche tra i diversi circuiti integrati e componenti della scheda. La funzione di visualizzazione 3D di KiCad consente di visualizzare come apparirà la scheda finale assemblata, fornendo preziose indicazioni sul posizionamento dei componenti e sui potenziali conflitti meccanici.


Il processo di produzione richiede formati di file specifici che i produttori di PCB possono interpretare e utilizzare per fabbricare le vostre schede. Questi file contengono informazioni precise sugli strati di rame, sui fori, sul posizionamento dei componenti e su altre specifiche di produzione. La comprensione di questo flusso di lavoro è essenziale sia che si lavori con il progetto standard di Bitaxe sia che si creino modifiche come l'aggiunta di loghi personalizzati, il cambiamento dei valori dei componenti o la regolazione del layout della scheda per soddisfare requisiti specifici.


### Generazione di file Gerber per la produzione


I file Gerber sono lo standard industriale per la comunicazione delle informazioni di progettazione dei PCB ai produttori. Questi file contengono tutti i dati necessari per la fabbricazione del PCB, compresi gli schemi degli strati di rame, le definizioni delle maschere di saldatura e le posizioni dei fori. Per creare questi file in KiCad, navigare nell'editor PCB e accedere alle uscite di fabbricazione attraverso il menu File. Il software configura automaticamente le impostazioni appropriate per i processi di produzione standard, compresa la struttura della directory di output, tipicamente organizzata come "manufacturing files/gerbers"


Il processo di generazione crea più file Gerber, ognuno dei quali rappresenta diversi aspetti del progetto del PCB. Questi file lavorano insieme per fornire ai produttori istruzioni complete per la fabbricazione. Una volta generati, questi file devono essere compressi in un archivio ZIP, il formato standard previsto dalla maggior parte dei produttori di PCB. Il file ZIP contiene tutti i dati di produzione necessari e garantisce che nessun file venga perso o danneggiato durante il processo di caricamento sul sito web del produttore.


Vale la pena notare che molti progetti open-source, tra cui Bitaxe, spesso includono file di produzione pre-generati nei loro repository. Tuttavia, la comprensione di come generate questi file è fondamentale quando si apportano modifiche al progetto o si lavora con versioni diverse della scheda. Questa conoscenza diventa particolarmente preziosa quando si personalizzano i progetti o si risolvono i problemi di produzione.


### Selezione dei produttori di PCB e comprensione delle opzioni


Il panorama della produzione di PCB offre diverse opzioni affidabili, con JLCPCB e PCBWay tra le scelte più popolari per hobbisti e professionisti. Entrambi i produttori offrono servizi simili con prezzi competitivi e qualità affidabile, anche se ciascuno di essi presenta vantaggi specifici a seconda dei requisiti del progetto. JLCPCB spesso attira gli utenti alle prime armi con prezzi promozionali e interfacce facili da usare, mentre PCBWay può offrire diverse opzioni di materiali o servizi specializzati.


Quando si caricano i file Gerber sul sito web di un produttore, il sistema analizza automaticamente il progetto e presenta varie opzioni di produzione. Le impostazioni predefinite fornite da queste piattaforme sono in genere adatte alla maggior parte dei progetti standard e si consiglia di mantenerle, a meno che non si abbiano esigenze specifiche. I parametri chiave includono lo spessore del PCB, il peso del rame, la finitura superficiale e le quantità minime. La maggior parte dei produttori richiede ordini minimi di cinque schede, il che funziona bene per i progetti hobbistici in cui è utile avere schede di riserva o condividerle con gli amici.


Le opzioni di colore rappresentano una delle poche scelte estetiche disponibili durante il processo di produzione. Mentre il verde rimane l'opzione tradizionale e più economica, i produttori offrono in genere alternative come il blu, il rosso, il giallo, il viola e il nero. La scelta del colore è puramente estetica e non influisce sulle prestazioni elettriche del PCB, anche se alcuni colori possono avere lievi implicazioni di costo o tempi di produzione più lunghi.


### Considerazioni sulla produzione avanzata e opzioni di assemblaggio


Oltre alla fabbricazione di base dei circuiti stampati, i produttori moderni offrono servizi aggiuntivi che possono semplificare notevolmente il completamento del progetto. Gli stencil rappresentano uno dei servizi aggiuntivi più preziosi, in particolare per i progetti con componenti a passo fine, come i chip ASIC presenti nei progetti Bitcoin e mining. Uno stencil è essenzialmente una sagoma di alluminio tagliata di precisione con aperture che corrispondono esattamente alle posizioni delle piazzole di saldatura sul PCB. Questo strumento consente un'applicazione coerente e precisa della pasta saldante, migliorando notevolmente la qualità dell'assemblaggio e riducendo la probabilità di errori di saldatura.


Le opzioni per gli stencil comprendono stencil singoli con motivi sia superiori che inferiori, oppure stencil separati per ciascun lato della tavola. Per la maggior parte dei progetti, uno stencil combinato si rivela più comodo ed economico. Lo spessore dello stencil viene calcolato attentamente per depositare la quantità di pasta saldante appropriata per i tipi di componenti e le dimensioni delle piazzole specifiche. L'uso di uno stencil trasforma quello che potrebbe essere un processo manuale noioso e soggetto a errori in una fase di assemblaggio rapida e professionale.


Sebbene alcuni produttori offrano servizi di assemblaggio parziale o completo, queste opzioni richiedono un'attenta considerazione per progetti complessi come il Bitaxe. La disponibilità dei componenti, le implicazioni di costo e il valore educativo dell'autoassemblaggio sono tutti fattori che incidono su questa decisione. Molti componenti specializzati richiesti per i progetti Bitcoin mining potrebbero non essere facilmente reperibili attraverso i servizi standard di assemblaggio di PCB, rendendo l'approvvigionamento dei componenti e l'assemblaggio manuale l'approccio più pratico. I prossimi episodi di questa serie tratteranno le strategie di approvvigionamento dei componenti e le tecniche di assemblaggio per aiutarvi a completare con successo il vostro progetto Bitaxe, dal PCB nudo al dispositivo funzionale.


Il processo di produzione e assemblaggio rappresenta un ponte cruciale tra la progettazione digitale e la realizzazione fisica. La comprensione di questi flussi di lavoro vi consente di assumere il controllo dei vostri progetti, di ridurre i costi e di acquisire una preziosa esperienza pratica con i processi di produzione professionali. Sia che stiate costruendo un singolo prototipo o pianificando una piccola produzione, la padronanza di queste competenze apre nuove possibilità per dare vita ai vostri progetti elettronici.


# Ottimizzazione delle prestazioni

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Valutazione dei parametri di Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

La ricerca di prestazioni ottimali mining richiede un approccio sistematico alla configurazione dell'hardware che bilanci hashrate, efficienza e gestione termica. I Bitaxe offrono numerosi parametri di configurazione che possono avere un impatto significativo sulle prestazioni, ma testare manualmente ogni combinazione di impostazioni sarebbe poco pratico e dispendioso in termini di tempo. Questo capitolo spiega come sfruttare gli strumenti di benchmarking automatizzati per ottimizzare scientificamente le prestazioni del Bitaxe, mantenendo condizioni operative sicure.


### Comprendere le metriche delle prestazioni di Bitaxe e la configurazione della linea di base


Prima di immergersi nelle tecniche di ottimizzazione, è essenziale comprendere gli indicatori di prestazione chiave che definiscono l'efficienza operativa del Bitaxe. Le metriche principali includono il hashrate misurato in terahash al secondo, l'efficienza energetica espressa in joule per terahash, la frequenza ASIC in megahertz e la tensione del core in volt. Un Bitaxe ben configurato potrebbe raggiungere circa 1,1 terahash con un'efficienza di circa 17 joule per terahash, operando a 550 megahertz con una tensione ASIC misurata di 1,14 volt. Questi numeri di base forniscono un punto di riferimento per comprendere i potenziali miglioramenti disponibili attraverso un'ottimizzazione sistematica.


La relazione tra queste metriche è complessa e interdipendente. Le frequenze più elevate aumentano in genere il hashrate, ma aumentano anche il consumo di energia e la generazione di calore. Allo stesso modo, la regolazione della tensione influisce sia sulle prestazioni che sulle caratteristiche termiche. La sfida consiste nel trovare l'equilibrio ottimale che massimizzi il hashrate o l'efficienza, mantenendo un funzionamento stabile entro limiti di temperatura sicuri. Questo processo di ottimizzazione richiede test metodici su più combinazioni di parametri, rendendo gli strumenti automatizzati preziosi per ottenere risultati ottimali.


### L'architettura dello strumento di benchmark Bitaxe Hashrate


Lo strumento [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) rappresenta una sofisticata soluzione basata su Python originariamente sviluppata da WhiteCookie e successivamente migliorata da mrv777. Questo strumento open-source, distribuito con licenza GPLv3, automatizza il complesso processo di verifica di molteplici combinazioni di configurazione per identificare le impostazioni ottimali per l'hardware specifico. Il punto di forza principale dello strumento è l'approccio sistematico al test dei parametri, che consente di regolare in modo incrementale le impostazioni di frequenza e tensione, monitorando continuamente le metriche delle prestazioni e le condizioni termiche.


Il processo di benchmarking richiede in genere dai 30 ai 40 minuti per essere completato, durante i quali lo strumento testa metodicamente varie combinazioni di impostazioni di frequenza e tensione del ASIC. Lo strumento inizia con impostazioni di base conservative, in genere a partire da 1,15 volt e 500 megahertz, quindi aumenta progressivamente questi parametri monitorando il hashrate, la temperatura e la stabilità. È importante notare che lo strumento dà la priorità al funzionamento sicuro rispetto alle prestazioni massime, facendo automaticamente marcia indietro rispetto alle impostazioni che causano un'eccessiva generazione di calore o instabilità. Questo approccio conservativo garantisce che il processo di ottimizzazione non comprometta la longevità o l'affidabilità dell'hardware.


### Requisiti di installazione e configurazione


L'implementazione dello strumento Bitaxe Hashrate Benchmark richiede diversi componenti software preliminari sul computer locale. I requisiti principali includono Python per l'esecuzione degli script di benchmarking, Git per la gestione del repository e, facoltativamente, Visual Studio Code per migliorare le funzionalità dell'ambiente di sviluppo. Anche se lo strumento può essere utilizzato da interfacce a riga di comando, l'uso di un ambiente di sviluppo integrato come VS Code offre una migliore visibilità del processo di benchmarking e dell'analisi dei risultati.


Il processo di installazione segue le pratiche standard di sviluppo di Python, iniziando con la clonazione del repository da GitHub al computer locale. Una volta scaricato il repository, è necessario creare un ambiente virtuale per isolare le dipendenze dello strumento dall'installazione Python del sistema. Questo isolamento previene potenziali conflitti con altre applicazioni Python e garantisce un funzionamento coerente. Dopo aver attivato l'ambiente virtuale, si installeranno le dipendenze necessarie utilizzando il file dei requisiti fornito, che configura automaticamente tutte le librerie e i moduli necessari per il corretto funzionamento dello strumento.


### Esecuzione dei benchmark e interpretazione dei risultati


L'esecuzione del benchmark richiede l'esecuzione di un singolo comando Python che include l'indirizzo IP del vostro Bitaxe come parametro. Lo strumento si collega automaticamente all'interfaccia web del vostro miner e inizia il processo di test sistematico. Durante l'esecuzione, lo strumento fornisce informazioni di registrazione dettagliate che mostrano l'iterazione corrente del test, le impostazioni di tensione e frequenza applicate, il hashrate risultante, la tensione di ingresso, le letture della temperatura e i dati termici dei componenti critici come il convertitore buck. Questo feedback in tempo reale consente di monitorare i progressi del benchmarking e di capire come le diverse impostazioni influiscono sulle prestazioni del miner.


La gestione termica intelligente dello strumento diventa evidente quando le temperature si avvicinano alla soglia di sicurezza di 66 gradi Celsius. Piuttosto che spingersi oltre i limiti operativi di sicurezza, il benchmark riduce automaticamente le impostazioni per mantenere la stabilità termica. Questo approccio conservativo garantisce che il processo di ottimizzazione dia priorità all'affidabilità dell'hardware a lungo termine rispetto ai guadagni di prestazioni a breve termine. Al termine, lo strumento genera risultati completi in formato JSON, classificando le cinque migliori configurazioni sia per il massimo hashrate che per l'efficienza ottimale. Questi risultati forniscono una guida chiara per la selezione della configurazione più adatta alle vostre priorità operative, sia che si tratti della massima produzione che dell'efficienza energetica.


Lo strumento di benchmarking offre anche opzioni di personalizzazione per gli utenti avanzati che desiderano modificare i parametri di test. Gli argomenti della riga di comando permettono di specificare tensioni e frequenze di partenza personalizzate, consentendo un'ottimizzazione più mirata per casi d'uso specifici. Ad esempio, se sapete già che il vostro hardware funziona bene a frequenze più alte, potete avviare il benchmark con impostazioni elevate invece di partire dai valori predefiniti. Questa flessibilità rende lo strumento prezioso sia per gli utenti alle prime armi che cercano un'ottimizzazione automatica, sia per i minatori esperti che vogliono regolare con precisione specifiche caratteristiche di prestazione.


## Overclock del Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

L'overclocking di un dispositivo Bitaxe richiede un'attenta considerazione dei limiti hardware e dei requisiti di raffreddamento. Sebbene molti utenti preferiscano sottoclockare i propri dispositivi per ottenere un funzionamento più silenzioso, la comprensione delle corrette tecniche di overclock è essenziale per coloro che cercano le massime prestazioni senza danneggiare l'hardware. Il processo comporta l'aumento della frequenza e la potenziale regolazione delle impostazioni di tensione al di là delle specifiche di fabbrica, con conseguente aumento della generazione di calore e dello stress sui componenti.


Il fondamento del successo dell'overclocking risiede in un'adeguata infrastruttura di raffreddamento. Prima di tentare qualsiasi modifica della frequenza, dovete assicurarvi che il vostro Bitaxe abbia una capacità di dissipazione del calore adeguata. Un Bitaxe Gamma con un dissipatore e una ventola di qualità fornisce la gestione termica necessaria per un overclocking sicuro. I dispositivi con dissipatori di piccole dimensioni e ventole inadeguate non dovrebbero essere sottoposti a overclocking, poiché le scarse prestazioni di raffreddamento causano un throttling termico e potenziali danni all'hardware. Il rapporto tra calore e longevità dei componenti è fondamentale da comprendere: un calore eccessivo crea stress che degrada i componenti elettronici nel tempo, riducendo significativamente la durata operativa del dispositivo.


### Posizionamento strategico del dissipatore


Il componente più critico che richiede un raffreddamento supplementare è il convertitore buck, un piccolo componente nero situato sul retro del Bitaxe vicino alla grande bobina. Questo dispositivo converte l'alimentazione in ingresso a 5 V nella tensione appropriata per il chip ASIC, in genere intorno a 1,2 V. Il convertitore buck, spesso chiamato TPS, genera un calore significativo durante il funzionamento e rappresenta un collo di bottiglia termico che limita il potenziale di overclocking. L'installazione di un piccolo dissipatore di calore adesivo su questo componente non solo consente di ottenere una maggiore capacità di overclocking, ma migliora anche l'efficienza complessiva riducendo le perdite termiche.


Un'ulteriore collocazione del dissipatore può essere utile per altre aree ad alta corrente della scheda. La circuiteria di regolazione della tensione subisce uno stress elettrico notevole, poiché l'alimentazione passa dalla sezione di ingresso attraverso varie tracce della scheda per alimentare il chip ASIC. Molti overclocker esperti installano dissipatori sulla parte anteriore del Bitaxe in queste aree ad alta corrente per migliorare ulteriormente la dissipazione termica. Sebbene non siano strettamente necessarie per un overclock moderato, queste misure di raffreddamento aggiuntive diventano importanti quando si spingono le frequenze a livelli estremi.


### Considerazioni e limiti del sistema di raffreddamento


Il controllore ESP32, visibile come componente argentato sulla scheda, in genere non richiede un raffreddamento aggiuntivo. Questo componente genera autonomamente un calore minimo e si riscalda solo a causa del trasferimento termico dai componenti circostanti. L'installazione di dissipatori di calore vicino all'ESP32 può potenzialmente interferire con l'antenna Wi-Fi adiacente, degradando la connettività wireless e la qualità del segnale. Concentrare gli sforzi di raffreddamento sui componenti di regolazione dell'alimentazione e sull'area ASIC piuttosto che sui circuiti di controllo.


Le configurazioni a doppia ventola presentano sia opportunità che limitazioni. Sebbene l'aggiunta di una seconda ventola per soffiare l'aria sul retro del Bitaxe possa migliorare le prestazioni di raffreddamento, il firmware del dispositivo può controllare correttamente solo una ventola. Il Bitaxe dispone di due intestazioni per le ventole ma di un solo controller, il che significa che il collegamento di due ventole confonderà il firmware in quanto riceve segnali di RPM contrastanti. Questa configurazione funziona, ma può causare un comportamento imprevedibile del controllo della ventola.


### Valutazione delle prestazioni di base


Prima di tentare qualsiasi modifica di overclocking, stabilire i parametri delle prestazioni di base facendo funzionare il Bitaxe con le impostazioni stock per diverse ore. Monitorare la temperatura del ASIC, la temperatura del regolatore di tensione e la percentuale di velocità della ventola attraverso l'interfaccia web. Le temperature operative ottimali dovrebbero mantenere il ASIC al di sotto dei 60°C e il regolatore di tensione al di sotto dei 60°C in condizioni normali. Se il dispositivo funziona già a una temperatura superiore a 65°C sul ASIC o a 70-80°C sul regolatore di tensione con le impostazioni di default, prima di procedere con l'overclocking è necessario aggiungere altro hardware di raffreddamento.


L'approccio sistematico all'aumento della frequenza prevede passi incrementali utilizzando le opzioni di frequenza predefinite nel menu delle impostazioni. Iniziate selezionando il passo di frequenza successivo rispetto a quello attuale, mantenendo la tensione del nucleo predefinita. Questo approccio conservativo consente di valutare gli impatti termici e di stabilità prima di apportare ulteriori modifiche. Lasciate che il dispositivo funzioni con ogni nuova impostazione di frequenza per almeno 30 minuti o un'ora, monitorando l'andamento della temperatura e la stabilità del tasso di hashish per tutto il periodo di valutazione.


### Configurazione personalizzata avanzata


Per accedere alle impostazioni personalizzate di frequenza e tensione è necessario abilitare l'interfaccia di overclocking avanzato aggiungendo "?OC" all'URL dell'interfaccia web del dispositivo. In questo modo si sbloccano i campi di immissione manuale per un controllo preciso della frequenza e della tensione, accompagnati da avvisi appropriati sui rischi legati al funzionamento al di fuori dei parametri progettati. L'interfaccia personalizzata consente una regolazione fine al di là delle fasi di frequenza standard, permettendo agli utenti esperti di ottimizzare le prestazioni per le loro specifiche configurazioni di raffreddamento.


Quando si utilizzano impostazioni personalizzate, mantenere incrementi prudenti di 10-15 MHz per ogni passo di regolazione. Questo approccio metodico evita picchi termici improvvisi e consente di eseguire test di stabilità adeguati a ogni livello di frequenza. Alcuni utenti avanzati raggiungono frequenze intorno ai 700 MHz con tensioni del nucleo regolate a 1,175 V o valori simili, ma queste impostazioni estreme richiedono ampie modifiche al raffreddamento e un attento monitoraggio. Il regolatore di tensione può funzionare a temperature fino a 100 °C senza subire danni immediati, ma temperature più elevate riducono l'efficienza e l'affidabilità a lungo termine. Un overclocking di successo richiede pazienza, test sistematici e un monitoraggio continuo per ottenere miglioramenti stabili delle prestazioni preservando l'integrità dell'hardware.


# Sezione finale

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Valutare questo corso

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusione

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>