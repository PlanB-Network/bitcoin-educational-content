---
name: Impostazione del primo nodo Lightning
goal: Comprensione, installazione, configurazione e utilizzo di un nodo Lightning
objectives: 


  - Comprendere il ruolo e lo scopo di un nodo Lightning.
  - Identificare le diverse soluzioni software disponibili.
  - Installare e configurare un nodo Lightning (LND).
  - Collegare un conto spese.
  - Conoscere i rischi dell'utilizzo di un nodo Lightning.


---

# Il tuo primo passo verso l'autonomia su Lightning



Avete già acquisito il tuo primo sats, vi siete assicurati i fondi per l'autocustodia e avete implementato un nodo Bitcoin per essere sovrani nell'uso del on-chain. Il passo successivo è ottenere la stessa autonomia su Lightning: è proprio questo l'obiettivo di questo corso.



LNP202 è rivolto agli utenti intermedi e vi guida passo dopo passo nell'implementazione del tuo primo nodo Lightning, senza competenze tecniche avanzate.



Imparerete a installare il LND sul Umbrel, ad aprire e gestire i tuoi canali, a supervisionare il tuo nodo e a collegare un wallet mobile, in modo da poter godere di un'esperienza paragonabile a quella di un wallet custodiale, mantenendo il controllo totale sui tuoi fondi.



+++


# Introduzione


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Panoramica del corso


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 è un corso pratico progettato per rendervi autonomi su Lightning gestendo il tuo nodo. L'obiettivo è semplice: iniziare con un nodo Bitcoin già esistente, implementare il LND sul Umbrel, proteggerlo correttamente, aprire e gestire i primi canali, quindi utilizzare il nodo quotidianamente da un wallet mobile. Questo corso presuppone che abbiate già seguito il corso BTC 202, in quanto presumo che il tuo nodo Bitcoin su Umbrel sia già operativo e sincronizzato. Non torneremo su come impostare un nodo Bitcoin in questa sede.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Per una migliore comprensione della meccanica interna di Lightning, si consiglia anche il corso LNP 201, anche se non è un prerequisito per questo corso:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Nella prima parte di questo corso LNP202, vedremo cos'è realmente un nodo Lightning, come si differenzia da un semplice wallet e perché la gestione di un nodo personale è l'unico modo per utilizzare Lightning senza delegare il proprio sats a una terza parte fidata. Questa sezione si conclude con una scelta strategica: quale soluzione fa al caso tuo, dagli approcci più semplici al classico nodo Lightning, quello che implementeremo in questo corso.



Nella seconda parte del corso, installerete il LND sul Umbrel, quindi metterete in atto gli elementi che prevengono gli errori più costosi: una strategia di backup realistica e la protezione contro gli imbrogli tramite una watchtower. Una volta che questi elementi di base sono stati messi a punto, aprirete il tuo primo canale, in modo da poter iniziare a pagare su Lightning con la tua infrastruttura.



Quindi, in questo corso LNP202, configureremo un nodo Lightning in modalità plug-and-play tramite Umbrel, anziché con il classico approccio da riga di comando, per renderlo adatto agli utenti intermedi. Se preferite un'installazione da riga di comando, vi consiglio di seguire il tutorial qui sotto. Sono in preparazione anche altri corsi su Lightning più avanzati e orientati alla riga di comando.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

La Parte 3 vi porterà da un nodo che funziona a uno che sapete come controllare. Inizierete a determinare il profilo dell'operatore del tuo nodo Lightning (consumatore, commerciante o router), per poi passare all'utilizzo di un pacchetto software di gestione completo, al fine di tracciare i tuoi canali e agire in modo pulito sulla tua topologia. Infine, affronterete un punto molto importante di Lightning: come ottenere liquidità in entrata, sia attraverso soluzioni a pagamento che cooperative.



La quarta parte si concentra sull'uso quotidiano. Verrà creata una connessione tra il proprio nodo e un cliente mobile, in modo da poter pagare e riscuotere semplicemente dal proprio smartphone, senza rinunciare alla custodia autonoma. Verrà esaminato prima un approccio di rete tramite *Tailscale*, poi un approccio di protocollo tramite *Nostr Wallet Connect*, con i rispettivi vantaggi e compromessi. Il corso si concluderà con un capitolo finale che vi darà le giuste abitudini per sostenere la tua autocustodia, sia dal punto di vista operativo che pedagogico.



Se seguite questo corso LNP202 nel giusto ordine, alla fine avrete una configurazione completa per il tuo nodo Lightning, funzionale per l'uso quotidiano e, soprattutto, sotto controllo.




## Comprendere i nodi Lightning


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Prima di lanciare il proprio nodo, questo capitolo passa in rassegna brevemente la teoria di base che sta alla base del [Lightning Network](https://planb.academy/resources/glossary/lightning-network). È infatti importante capire i meccanismi coinvolti, perché questo vi permetterà di identificare i rischi e di adottare buone pratiche per limitarli. Tuttavia, non entrerò nei dettagli, perché non è l'obiettivo principale di questo corso. Se volete approfondire l'argomento, vi consiglio di consultare il corso LNP 201 di Fanis Michalakis, che è un punto di riferimento nel settore:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Cos'è un nodo Lightning?



Torniamo alle basi: prima di definire cos'è un nodo, dobbiamo capire cos'è il Lightning Network. È un protocollo di livello superiore, costruito sopra il Bitcoin, progettato per consentire transazioni [offchain](https://planb.academy/resources/glossary/offchain) BTC veloci (con finalità quasi istantanee) e generalmente economiche. Si tratta di un protocollo di livello superiore, costruito sopra il Bitcoin, progettato per consentire transazioni offchain BTC che sono veloci (con finalità quasi istantanee) e generalmente poco costose. "Offchain" significa che le transazioni eseguite su Lightning non sono destinate a comparire sulla [blockchain](https://planb.academy/resources/glossary/blockchain) principale del Bitcoin. Lightning è anche una risposta parziale al crescente utilizzo di Bitcoin e alla congestione della catena, che sta sollevando preoccupazioni sulla [scalabilità](https://planb.academy/resources/glossary/scalability) del sistema.



Per funzionare, Lightning si basa sull'apertura di [canali di pagamento](https://planb.academy/resources/glossary/payment-channel) tra i partecipanti, all'interno dei quali le transazioni possono essere eseguite quasi istantaneamente, spesso con commissioni minime, senza la necessità di registrarle una per una sulla blockchain Bitcoin. Questi canali possono rimanere aperti per un tempo molto lungo, richiedendo transazioni [onchain](https://planb.academy/resources/glossary/onchain) solo al momento della loro apertura e chiusura.



Un [nodo Lightning](https://planb.academy/resources/glossary/lightning-node) è un partecipante alla rete Lightning, che apre canali ed effettua pagamenti con altri nodi. In concreto, un nodo Lightning è un software che gira su un computer e che implementa il protocollo Lightning Network. Alcuni esempi sono LND, Core Lightning o Eclair. Il ruolo principale di questo software è quello di:




- connettersi a un [nodo Bitcoin](https://planb.academy/resources/glossary/full-node) per ottenere informazioni dalla blockchain principale;
- creare e gestire canali di pagamento bidirezionali con altri nodi;
- scambiare messaggi con l'intera rete Lightning.



![Image](assets/fr/001.webp)



### Nodo vs. Lightning Wallet: una distinzione importante



Nel Bitcoin (onchain), "*[wallet](https://planb.academy/resources/glossary/wallet)*" si riferisce al software che gestisce le [chiavi private](https://planb.academy/resources/glossary/private-key), calcola il saldo dai [UTXO](https://planb.academy/resources/glossary/utxo) e crea le transazioni. Questo wallet può essere basato sul tuo nodo Bitcoin o su quello di qualcun altro, ma oggi il ruolo del nodo e quello del wallet onchain sono chiaramente distinti.



Su Lightning è più difficile riutilizzare questo tipo di vocabolario senza creare confusione. Il termine "*Lightning wallet*" è piuttosto vago, perché in realtà non esiste un vero e proprio Lightning wallet autocustodito, a meno che non sia basato su un nodo. Sono quindi possibili solo due situazioni:



- Per avere un vero nodo Lightning (cioè non custodiale): il software che si sta utilizzando (ad esempio un'applicazione mobile come Phoenix o un'istanza di LND su Umbrel) sta effettivamente gestendo un nodo, e l'utente possiede effettivamente le chiavi per recuperare i bitcoin. In questo caso, il tuo "*Lightning wallet*" è in realtà solo un'interfaccia utente sopra un nodo Lightning, sia esso incorporato o remoto.



- Per utilizzare un servizio custodial: si utilizza un'applicazione che mostra un saldo in [sats](https://planb.academy/resources/glossary/satoshi-sat) su Lightning, ma in background i fondi sono sul nodo di un fornitore (ad esempio Wallet of Satoshi). Non avete né le chiavi né il controllo dei canali. Il tuo saldo è solo una voce contabile nel database dell'azienda. È paragonabile a lasciare i tuoi bitcoin su una piattaforma di scambio, con tutti i rischi associati. In questo caso, il tuo "*Lightning wallet*" è solo un accesso a un conto gestito da un operatore che, a sua volta, gestisce un vero nodo Lightning.



Per Lightning non ci sono vie di mezzo: o si ha un nodo (anche incorporato) e quindi si è in autocustodia, o non lo si ha, quindi un'azienda possiede il sats. Ma come vedremo nei capitoli successivi, questi due usi possono essere talvolta difficili da distinguere. Ad esempio, il Phoenix è un'applicazione mobile che incorpora un vero e proprio nodo Lightning, ma l'utente non ne è necessariamente consapevole, poiché l'intera complessità del suo funzionamento è quasi del tutto nascosta.



### Un promemoria su come funziona il Lightning Network



In questa sezione, vi fornirò un rapido promemoria di come funziona Lightning. Ancora una volta, se desiderate una presentazione più approfondita dei concetti teorici, vi invito a dare un'occhiata al corso LNP 201 dedicato.



#### Canali di pagamento: apertura, aggiornamento e chiusura



Il cuore della rete Lightning si basa su canali di pagamento bidirezionali. Un canale può essere aperto (cioè creato), aggiornato man mano che avvengono le transazioni Lightning e infine chiuso. Dal punto di vista di onchain, un canale non è altro che l’[output](https://planb.academy/resources/glossary/output) di una transazione [multisig](https://planb.academy/resources/glossary/multisig) 2/2.



![Image](assets/fr/002.webp)



Dal punto di vista di Lightning, si tratta di un canale di pagamento con [liquidità](https://planb.academy/resources/glossary/liquidity-lightning) divisa tra i due partecipanti.



![Image](assets/fr/003.webp)





- Apertura di un canale:**



Due nodi decidono di aprire un canale. Uno di loro impegna i bitcoin in una transazione onchain chiamata *transazione di finanziamento*. Questa transazione crea un output basata su uno [script](https://planb.academy/resources/glossary/script) a [firma](https://planb.academy/resources/glossary/digital-signature) multipla 2 su 2, il che significa che per spendere questi fondi su Bitcoin è necessaria la firma di entrambi i nodi del canale. Prima di emettere questa transazione, la parte che fornisce i fondi chiede all'altra di firmare una *transazione di prelievo*, che non viene emessa onchain, ma che consente di recuperare i propri fondi in caso di problemi.



![Image](assets/fr/004.webp)





- Transazioni Commitment:**



Lo stato del canale (cioè la distribuzione del sats tra A e B) è rappresentato da un *[commitment transaction](https://planb.academy/resources/glossary/commitment-transaction)*, noto a entrambi i nodi ma non immediatamente trasmesso sulla blockchain. Questa transazione descrive come ridistribuire i fondi del canale sulla blockchain in base ai pagamenti effettuati su Lightning.



Ad ogni pagamento Lightning, i due nodi firmano un nuovo stato che sostituisce quello precedente. Il vecchio stato viene revocato grazie a un meccanismo di chiavi di revoca: se uno dei partecipanti tenta di trasmettere un vecchio stato, l'altro può recuperare l'intero importo dei fondi come sanzione.



L'idea importante è che esiste sempre una transazione Bitcoin firmata, non trasmessa sulla catena, conservata dai nodi e che consente la ridistribuzione del sats di ciascuno in base ai pagamenti effettuati sul Lightning Network.



![Image](assets/fr/005.webp)





- Chiusura del canale:**



Un canale può essere chiuso in modo pulito attraverso una chiusura cooperativa, quando entrambe le parti concordano sullo stato finale del canale, o unilateralmente (una chiusura forzata) se uno dei partecipanti cessa di cooperare o diventa irraggiungibile. In tutti i casi, la chiusura assume la forma di una transazione onchain che spende l'output 2/2 e distribuisce i fondi tra i partecipanti in base all'ultimo stato valido del canale.



![Image](assets/fr/006.webp)



Lightning funziona quindi come un livello secondario ancorato al Bitcoin: solo alcuni eventi (l'apertura e la chiusura di canali) appaiono sulla blockchain principale. I pagamenti intermedi rimangono fuori dalla blockchain.



Prima di proseguire, ecco due concetti essenziali per capire come gestire un canale Lightning:




- *Liquidity*: la quantità di sats disponibile su un lato del canale;
- La *[capacità](https://planb.academy/resources/glossary/lightning-channel-capacity)*: è l'importo totale bloccato nell'output 2/2 multisig, cioè la somma della liquidità su entrambi i lati del canale.



#### Una rete di canali e liquidità



Un canale non serve solo per i pagamenti tra due nodi: fa parte di una rete globale di canali interconnessi. Il tuo nodo può instradare i pagamenti per altri utenti attraverso i propri canali, e potete inviare sats a un nodo Lightning con cui non avete un canale diretto, purché si trovi un percorso valido tra i tuoi due nodi.



Ogni nodo conosce, tramite il [protocollo di gossip](https://planb.academy/resources/glossary/gossip), una mappa di questa rete: quali canali esistono, quali nodi sono collegati da un canale bidirezionale e quali capacità sono pubblicate. Per inviare un pagamento a un destinatario senza un canale diretto, il proprio nodo calcola un percorso composto da diversi hop: il proprio nodo → nodo X → nodo Y → nodo destinatario. A ogni passaggio, il pagamento transita su un canale che deve avere sufficiente liquidità nella direzione del pagamento.



![Image](assets/fr/007.webp)



La liquidità di un canale non è quindi simmetrica: un lato può essere molto carico, mentre l'altro è quasi vuoto. La gestione di questa liquidità, cioè sapere dove si trovano i sats e in quale direzione possono fluire, è uno degli aspetti più importanti della gestione di un nodo Lightning. Lo vedremo in dettaglio nei prossimi capitoli pratici.



#### HTLC: trasportare i pagamenti senza essere derubati



Per consentire ai pagamenti di passare attraverso nodi intermedi senza bisogno di fiducia, Lightning utilizza [contratti intelligenti](https://planb.academy/resources/glossary/smart-contract) chiamati *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). In termini semplici, un HTLC condiziona il trasferimento di fondi alla rivelazione di un segreto e incorpora un vincolo temporale per proteggere il mittente in caso di fallimento della transazione. Ogni pagamento è quindi subordinato alla presentazione di una pre-immagine (un segreto il cui [hash](https://planb.academy/resources/glossary/hash-function) corrisponde a un valore concordato). Se il destinatario finale fornisce questa pre-immagine, può rivendicare i fondi, il che a sua volta consente a ogni nodo intermediario di recuperare i propri fondi.



![Image](assets/fr/008.webp)



Vi risparmio i dettagli tecnici sul funzionamento dei HTLC, perché non sono essenziali ai fini di questo corso. Troverete una spiegazione approfondita nel corso teorico LNP 201. Ricordate solo che i HTLC consentono di effettuare scambi atomici: o il trasferimento viene completato e non c'è alcun problema. Ricordate solo che i HTLC consentono scambi atomici: o il trasferimento viene completato e nessuno viene danneggiato nel percorso, o fallisce e ogni partecipante recupera i propri fondi iniziali. Non ci sono vie di mezzo.



### Le principali implementazioni del nodo Lightning



Come per il Bitcoin, esistono diverse implementazioni del protocollo Lightning. Diversi team indipendenti stanno sviluppando le proprie versioni, tutte interoperabili in quanto aderiscono alle stesse specifiche (le [BOLT](https://planb.academy/resources/glossary/bolt)). Ecco le principali implementazioni in uso oggi.



#### LND (*Lightning Network Daemon*)



LND è un'implementazione completa del protocollo Lightning, scritta in Go e sviluppata da Lightning Labs.



![Image](assets/fr/009.webp)



#### Lightning centrale (*CLN*)



Core Lightning (precedentemente *C-Lightning*) è l'implementazione sviluppata da Blockstream. È scritta in C, con alcuni componenti in Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair è un'implementazione scritta in Scala e sviluppata dall'azienda francese ACINQ. ACINQ gestisce con Eclair uno dei nodi di routing più importanti della rete Lightning e utilizza questa implementazione come base software per i propri prodotti, come ad esempio l'applicazione Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) è un kit di sviluppo Rust, gestito da Spiral (Block, ex-Square). Non si tratta di un daemon pronto all'uso come il LND o il CLN, ma di una libreria per gli sviluppatori che desiderano integrare Lightning direttamente nelle loro applicazioni.



![Image](assets/fr/012.webp)



In questo corso LNP202 ci concentreremo principalmente sul LND: l'implementazione più comunemente utilizzata nelle soluzioni "chiavi in mano" per i clienti privati, come il Umbrel.



Questo è quanto per questo breve promemoria sul funzionamento di Lightning. Ancora una volta, se c'è qualche concetto che non vi è chiaro o se volete approfondire un po' prima di metterlo in pratica, il corso di Fanis Michalakis è il riferimento essenziale sull'argomento:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Perché gestire il proprio nodo Lightning?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Rispondere a questa domanda è piuttosto semplice, poiché è retorica: senza il proprio nodo, non si utilizza più realmente Lightning, ma solo l'illusione di Lightning attraverso l'infrastruttura di un'azienda.



L'utilizzo di un wallet custodial Lightning significa che i bitcoin appartengono tecnicamente alla società che gestisce il nodo. Non si detengono le chiavi private e non si controllano i canali. Il tuo saldo wallet è solo una riga nel database di un fornitore di servizi. Questa situazione è certamente molto comoda per i principianti e l'esperienza dell'utente è spesso fluida, ma la domanda fondamentale è: qual è il vantaggio di usare Bitcoin e Lightning se si finisce per rinunciare proprio agli aspetti che li distinguono dalle valute e dalle banche tradizionali?



Le due principali proposte di valore di Bitcoin sono la sovranità monetaria (non dipendere più da un'autorità centrale per l'emissione e la custodia) e la resistenza alla censura (impossibilità per una terza parte di impedire o filtrare i pagamenti). Un sistema custodial su Lightning si scontra con entrambi gli obiettivi: non è possibile controllare la massa monetaria interna della piattaforma e, per definizione, un operatore che detiene tutti i fondi e tutti i canali può censurare, ritardare, dare priorità o bloccare i pagamenti. In queste condizioni, possiamo legittimamente chiederci: "Che senso ha utilizzare bitcoin tramite Lightning se poi si riprodurranno gli stessi schemi di fiducia e dipendenza dei sistemi valutari statali tradizionali?



> È necessario un sistema di pagamento elettronico basato sulla prova crittografica anziché sulla fiducia, che consenta a due parti intenzionate di effettuare transazioni direttamente l'una con l'altra senza bisogno di una terza parte fidata.
*Libro bianco Satoshi Nakamoto, Bitcoin


A parte la filosofia, gli svantaggi più concreti sono i seguenti. In primo luogo, non avete modo di verificare che la società detenga effettivamente i bitcoin corrispondenti ai saldi visualizzati. Potrebbe operare con una riserva frazionaria, essere hackerata, andare in bancarotta o semplicemente scomparire. In questo caso, siete solo un altro creditore, senza alcuna garanzia di riavere il tuo denaro.



In secondo luogo, l'azienda è soggetta a rischi normativi: ingiunzioni, congelamento di fondi, richieste di blocco di utenti o transazioni, sorveglianza rafforzata o addirittura divieto assoluto di attività in determinate giurisdizioni. Ogni vincolo che grava sul fornitore di servizi si riflette meccanicamente su di te.



In termini di riservatezza, la situazione non è migliore. Un operatore di deposito vede tutti i tuoi flussi: importi, frequenze, destinatari, saldi, abitudini di spesa. Combinate con le informazioni fornite dall'applicazione ed eventualmente dall'analisi della catena sottostante a Bitcoin, queste informazioni possono fornire un profilo molto preciso della tua attività finanziaria. Anche in questo caso, l'obiettivo di Bitcoin è quello di ridurre il monitoraggio finanziario.



La buona notizia è che oggi la gestione del proprio nodo Lightning non è più appannaggio di tecnici esperti, come poteva essere alla fine degli anni 2010. Per gli utenti privati sono disponibili soluzioni relativamente semplici, che spiegheremo in dettaglio nel prossimo capitolo.




## Scegliere la soluzione giusta per il lavoro


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Oggi è possibile avere un'esperienza d'uso molto vicina a quella di un wallet custodial Lightning, pur rimanendo in autocustodia. Lo scopo di questo capitolo è quello di aiutarti a scegliere il percorso più adatto al tuo profilo.



### Opzione 1: Non utilizzare direttamente Lightning



La prima soluzione è semplicemente quella di non utilizzare Lightning in modo nativo, ma di utilizzare un Bitcoin o [Liquid](https://planb.academy/resources/glossary/liquid-network) wallet che incorpora gli [swap atomici](https://planb.academy/resources/glossary/atomic-swap). Ad esempio, le applicazioni Aqua o BULL Wallet utilizzano questo metodo, consentendo di pagare le [intece Lightning](https://planb.academy/resources/glossary/invoice-lightning) senza gestire un nodo Lightning, pur rimanendo in autocustodia.



Il principio è semplice: i fondi rimangono nel Bitcoin, o nel on-chain o nel Liquid, e vi si accede tramite un wallet di cui si detengono le chiavi in modo tradizionale. Quando si scansiona una intece Lightning, il wallet avvia una transazione (on-chain o Liquid) verso un servizio di swap atomico. Questo servizio gestisce quindi il pagamento Lightning attraverso il proprio nodo, utilizzando i bitcoin forniti dal on-chain o dal Liquid. In questo modo, non dovrete gestire personalmente alcun canale Lightning, ma potrete comunque saldare le intece Lightning senza problemi.



![Image](assets/fr/013.webp)



Il vantaggio principale di questo approccio, rispetto a un tradizionale Lightning custodial wallet, è che si rimane sempre in possesso al 100% dei propri fondi. I bitcoin sono nella tua onchain o Liquid wallet, con la tua [frase mnemonica](https://planb.academy/resources/glossary/seed). Anche durante lo scambio, si rimane in possesso dei propri fondi, perché lo scambio è atomico. Si basa su un meccanismo crittografico che garantisce due soli risultati possibili: o lo scambio riesce completamente, o fallisce e il servizio non può appropriarsi dei tuoi fondi.



La maggior parte dei wallet che offrono questo tipo di funzionalità si affidano a [Boltz](https://boltz.exchange/) per la parte tecnica dello scambio.



Questa soluzione offre anche interessanti vantaggi in termini di riservatezza, soprattutto se abbinata al Liquid. Per un principiante, è anche molto facile da configurare e salvare: una classica frase mnemonica, nessun canale, nessuna liquidità da bilanciare...



D'altra parte, questo approccio ha i suoi limiti. In primo luogo, non è incensurabile: dipendete dalla disponibilità e dalla buona volontà del servizio di swap. Se non vuole più gestire il tuo conto o cessa l'attività, non potrete più pagare le intece Lightning attraverso di esso. Ci sono poi le non trascurabili commissioni: si pagano sia le [commissioni per le transazioni](https://planb.academy/resources/glossary/transaction-fees) onchain o Liquid, sia la commissione del servizio di swap. Inoltre, se le commissioni onchain aumentano drasticamente, l'utilizzo di Lightning può diventare molto costoso.



Quindi, per un uso occasionale, è ancora accettabile, ma per un utente molto attivo di Lightning, è meglio fare le cose per bene con un vero nodo Lightning.



### Opzione 2: Nodi Lightning on-board



La seconda categoria di soluzioni si basa su nodi Lightning integrati direttamente in un'applicazione mobile. Phoenix Wallet è stato il pioniere di questo modello e rimane un punto di riferimento. Oggi altri progetti offrono approcci analoghi, come Zeus (in modalità embedded) o BitKit.



L'idea è semplice: l'applicazione esegue effettivamente un nodo Lightning, ma tutte le operazioni complesse sono gestite automaticamente in background. Si ha un'interfaccia "*Lightning wallet*" con una frase mnemonica per il backup, si vede il saldo e si pagano le intece, ma non si gestiscono i canali, la liquidità o la maggior parte dei parametri.



![Image](assets/fr/014.webp)



Queste soluzioni sono sempre autocustodite. Le chiavi che controllano i fondi sono generated e memorizzate sul telefono, mentre il backup avviene tramite un seed o un meccanismo equivalente. Non si detiene semplicemente un conto presso un fornitore di servizi, ma si possiedono effettivamente bitcoin bloccati in canali che appartengono all'utente e che non possono essere rubati.



I vantaggi dei nodi LN on-board sono numerosi:




- estremamente facile da installare e utilizzare;
- esperienza d'uso simile a quella di un Lightning wallet custodial, ma con autocustodia;
- nessuna gestione manuale dei canali o della liquidità;
- backup relativamente semplice.



Ma questi wallet incorporati presentano anche limitazioni significative. In primo luogo, in termini di riservatezza, l'operatore del servizio (ad esempio ACINQ nel caso del Phoenix) ha una visione abbastanza dettagliata dei flussi che passano attraverso il tuo nodo: quantità, frequenze, destinatari, anche se questo è destinato a migliorare, in particolare con la graduale adozione dei *Nodi Trampolino*. In secondo luogo, dipendete fortemente da questo operatore come principale peer di Lightning. Se il nodo ACINQ diventa indisponibile (nel caso di Phoenix), se l'azienda subisce pressioni normative o cambia il suo modello di business, la tua esperienza utente potrebbe essere gravemente degradata o addirittura compromessa.



Infine, questa semplicità ha un prezzo. I servizi del nodo LN incorporato generalmente applicano commissioni specifiche su depositi, prelievi o su alcune operazioni di gestione del canale. A mio avviso, questo modello ha senso in termini di servizio offerto, ma per un uso intensivo può essere molto più costoso di un nodo Lightning convenzionale ben gestito.



### Opzione 3: il classico nodo Lightning



La terza soluzione, quella che approfondiremo in questo corso LNP202, consiste nel gestire un nodo Lightning convenzionale su un server o un dispositivo dedicato.



Per "classico" intendo che si installa e si configura un'implementazione di Lightning (ad esempio, LND) in cima al proprio nodo Bitcoin. Si scelgono i peer, si aprono i canali, si gestisce la [liquidità in entrata](https://planb.academy/resources/glossary/inbound-capacity) e in uscita e si impostano le politiche di routing.



In termini di sovranità, è la soluzione migliore. Non dipendete più da una società specifica per i tuoi canali o pagamenti: se un peer vi censura o chiude un canale, potete aprirne un altro con un nodo diverso. Se un servizio scompare, i tuoi sats rimangono nei canali che controllate e potete rimpatriarli onchain. Potete anche ottimizzare i costi a lungo termine: una volta che i tuoi canali sono correttamente dimensionati e gestiti, il costo complessivo dei pagamenti può diventare molto basso.



In termini di riservatezza, siete ovviamente soggetti alle limitazioni del modello di Lightning, ma non state consegnando la tua intera attività a un singolo operatore.



Al contrario, la configurazione di un nodo Lightning classico è ovviamente più complessa: bisogna installare, configurare, mantenere, monitorare gli aggiornamenti, comprendere la logica dei canali e delle politiche di addebito, gestire i canali e il flusso di cassa e così via. Una configurazione errata, un backup approssimativo o una gestione poco attenta possono portare più facilmente alla perdita del sats. Il nodo deve inoltre funzionare in modo continuo.



È proprio questo il percorso che vi propongo in questo corso, accompagnandovi in ogni passo per limitare i rischi e strutturare il tuo approccio.



### Quale soluzione per quale profilo utente?



Per scegliere la soluzione giusta per il tuo profilo di utente Lightning, devi considerare due fattori: la frequenza di utilizzo di Lightning e la tua propensione alla gestione tecnica.



Se non si effettuano molti pagamenti Lightning su base occasionale, ma si vuole comunque essere in grado di saldare le intece LN dal proprio telefono di tanto in tanto, senza rinunciare all'autodeposito: un Bitcoin o Liquid wallet con funzionalità di swap è probabilmente l'opzione migliore. Si mantiene la proprietà dei propri fondi, non si gestiscono nodi e si accettano commissioni leggermente più alte in cambio della semplicità.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Se utilizzate Lightning con una certa regolarità e desiderate i vantaggi di un vero e proprio nodo, ma non volete perdere tempo a gestire canali, commissioni o infrastrutture, un nodo Lightning mobile incorporato è una buona soluzione. Si mantiene la custodia dei propri fondi, l'interfaccia utente rimane molto accessibile e tutta la complessità è nascosta, al prezzo di una marcata dipendenza da un operatore.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Se siete utenti intermedi o avanzati, disposti a investire tempo nella comprensione e nella gestione della tua infrastruttura e desiderate il massimo controllo sui tuoi canali, sulla liquidità e sui costi: un nodo Lightning classico basato su server è la strada da percorrere. È la soluzione più impegnativa, ma anche la più coerente con l'idea di sovranità di Bitcoin.




# Creare il primo nodo Lightning


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Installazione di LND con Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Dopo aver esaminato le basi di Lightning e le soluzioni disponibili, è ora di passare all'azione. Per seguire questo corso, è necessario disporre di un nodo Bitcoin sincronizzato con Umbrel. Questo corso di formazione LNP202 è la continuazione del BTC 202; se non avete ancora un nodo Bitcoin, vi invito a seguire quest'altro corso di formazione prima di tornare qui una volta sincronizzato il tuo nodo. Vi consiglio vivamente di consultarlo, perché non entrerò nei dettagli del suo funzionamento, della sua configurazione e delle sue misure di sicurezza.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

In questo primo capitolo vedremo come installare il LND sul Umbrel. Il funzionamento del Umbrel rende questa fase molto semplice, poiché è sufficiente installare un'applicazione.



Dalla pagina iniziale, aprire l'"App Store" nella parte inferiore dell'interfaccia.



![Image](assets/fr/015.webp)



Nella barra di ricerca, inserite `Lightning Node`, quindi fate clic sull'applicazione.



![Image](assets/fr/016.webp)



Fare quindi clic sul pulsante `Install` per avviare l'installazione.



![Image](assets/fr/017.webp)



Dalla pagina iniziale, fare clic sull'applicazione per aprirla, quindi selezionare "Imposta un nuovo nodo".



![Image](assets/fr/018.webp)



Vi viene data una frase mnemonica di 24 parole. Conservatela in un luogo sicuro. Nel prossimo capitolo vedremo più dettagliatamente come riottenere l'accesso al nodo Lightning (si tratta di un processo molto più complesso rispetto a un semplice Bitcoin wallet), ma per ora ricordate che questa frase ha un ruolo cruciale e deve essere conservata con la massima cura.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Salvate questa frase come una frase mnemonica convenzionale: su un supporto fisico (carta o metallo) conservato in un luogo sicuro, quindi fate clic sul pulsante `NEXT`.



![Image](assets/fr/019.webp)



Inserite quindi le parole della frase per verificare che siano state scritte correttamente.



![Image](assets/fr/020.webp)



Un messaggio di avviso vi ricorderà che l'applicazione è in versione beta e che Lightning Network rimane una tecnologia sperimentale. Ovviamente, non impegnate mai nel tuo nodo Lightning somme che non siete disposti a perdere.



Si arriva quindi all'interfaccia principale del nodo Lightning. A sinistra, troverete la catena Bitcoin onchain wallet ospitata sul tuo nodo. Si tratta del generated della frase di 24 parole appena salvata.



Al centro, si trova il proprio Lightning wallet. Rappresenta i [fondi in uscita](https://planb.academy/resources/glossary/outbound-capacity), ovvero i bitcoin che si possiedono all'interno dei canali Lightning.



A destra, vengono visualizzate diverse informazioni importanti sul nodo:




- Il numero di connessioni e di canali aperti;
- Il tuo flusso di cassa totale in uscita, cioè quello che potete teoricamente spendere per Lightning;
- La tua liquidità totale in entrata, ovvero quanto potete teoricamente ricevere su Lightning.



![Image](assets/fr/021.webp)



Cominciamo a personalizzare il nostro nodo. Fare clic sui tre puntini in alto a destra dell'interfaccia, quindi su "Impostazioni avanzate". Nel sottomenu `Personalizzazione` è possibile definire un nome pubblico per il nodo (evitando di usare il proprio nome reale) e sceglierne il colore.



![Image](assets/fr/046.webp)



Fare quindi clic sul pulsante verde "Salva e riavvia" per riavviare il nodo e applicare le modifiche.



Il tuo nodo Lightning è ora pronto ad aprire i primi canali per effettuare pagamenti. Ma prima, diamo un'occhiata a come proteggere il tuo sats!



## Salvataggio del nodo Lightning


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Prima di inviare il primo sats al proprio nodo, è importante capire come funziona il backup e quali sono i rischi associati. A differenza di un semplice wallet onchain Bitcoin, il backup di un nodo Lightning è piuttosto complesso: una strategia sbagliata può portare alla perdita permanente dei fondi. In questo capitolo vedremo cosa è necessario fare per il backup e come il Umbrel gestisce questo processo con il LND.



In questo corso utilizzeremo l'implementazione LND (*Lightning Network Daemon*). Sebbene i principi siano simili a quelli delle altre implementazioni, i file di recupero e le procedure di cui parlerò sono specifici del LND.



### Che cosa devo salvare su un nodo Lightning?



Su un nodo Lightning non basta salvare il seed e sperare che tutto torni alla normalità. Diversi elementi svolgono ruoli diversi, quindi è importante distinguerli.



#### Il seed (*aezeed*)



Quando si inizializza il LND, si riceve un seed di 24 parole. Si tratta di un formato specifico del LND chiamato "*aezeed*". Non si tratta di un classico seed BIP39, anche se gli assomiglia molto. Da questo seed, il LND ricava le chiavi private del tuo wallet onchain associato al nodo Lightning, ossia gli indirizzi in cui potete ricevere o a cui potete rimpatriare bitcoin in seguito alla chiusura del canale.



![Image](assets/fr/019.webp)



Questo seed può quindi essere utilizzato per ricreare il wallet onchain associato al tuo nodo e per recuperare i fondi che sono già stati rimpatriati onchain (ad esempio dopo la chiusura di un canale). D'altra parte, il seed da solo non è sufficiente per ripristinare i canali Lightning ancora aperti, poiché non contiene le informazioni necessarie sullo stato dei canali.



#### Il database del canale (`channel.db`)



Il LND memorizza lo stato dettagliato dei canali in un database denominato `channel.db`. Questo database contiene:




- l'elenco dei canali aperti;
- i propri peer e i loro identificatori;
- gli ultimi commitment transaction per ogni canale (gli stati successivi che definiscono chi possiede cosa nel canale e permettono di recuperare i fondi onchain in caso di problemi);
- le informazioni necessarie per punire un peer che tenta di trasmettere un vecchio rapporto.



Il problema di questo database è che cambia continuamente: ogni pagamento, ogni routing, ogni apertura o chiusura di un canale ne modifica il contenuto. Questo è il motivo per cui un backup convenzionale (ad esempio una copia periodica di `channel.db`) è pericoloso. Se si ripristina una versione troppo vecchia di `channel.db` e si riassembla il nodo con questo stato obsoleto, i peer potrebbero ritenere che si stia trasmettendo un vecchio stato del canale. In questo caso, il protocollo prevede una penalità: il tuo pari può recuperare l'intero ammontare dei fondi del canale, come se aveste cercato di imbrogliare.



In pratica, quindi, `channel.db` non è un supporto di backup in quanto tale. È lo stato vivente del tuo nodo. L'unica situazione in cui ha senso usarlo per ripristinare il nodo è quando si recupera questo database direttamente da una macchina che si è appena guastata (ad esempio un disco ancora leggibile). In questo caso, si recupera lo stato più recente e si può riavviare LND su un'altra macchina basata su questo database, sapendo che lo stato è il più aggiornato possibile, dato che la vecchia macchina non è più in funzione. Un'altra situazione in cui questo metodo può servire come backup rilevante è in una configurazione a due dischi, con una copia dinamica e permanente da uno all'altro. Tuttavia, questo tipo di configurazione è più complesso da implementare.



Ma fare copie periodiche di `channel.db` e conservarle come backup da ripristinare in seguito è una pessima idea: il giorno in cui le si usa, si corre il rischio di penalizzarsi e di perdere tutto il sats.



#### Canale statico di backup (SCB)



Per rendere possibile il ripristino di emergenza, LND ha introdotto il meccanismo *Static Channel Backup* (SCB). Si tratta di un file speciale, spesso chiamato `channel.backup`, che contiene informazioni statiche sui tuoi canali: chi sono i tuoi pari, come contattarli e quali sono i tuoi canali.



Questo file non contiene lo stato dettagliato del canale o la cronologia degli aggiornamenti. Non consente di riaprire i canali nello stato esatto in cui si trovavano, né di continuare a gestire questo nodo Lightning. Il suo ruolo è piuttosto quello di fungere da punto di ancoraggio per chiedere ai tuoi pari di aiutarti a chiudere in modo pulito tutti i tuoi canali, ricevendo così il tuo sats onchain, su chiavi che potrete recuperare grazie al seed. Quindi, a differenza del file `channel.db`, che viene modificato a ogni pagamento o routing, il file SCB viene aggiornato solo quando un canale viene aperto o chiuso.



Per il recupero tramite SCB, la procedura è la seguente:




- Si ripristina il seed (*aezeed*), che ricrea il wallet onchain associato al nodo Lightning;
- Il cliente fornisce al LND la sua più recente SCB;
- Il LND utilizza l'SCB per trovare l'elenco dei tuoi pari e i canali che avete con loro;
- Contatta ogni peer, comunica loro che si è verificata una perdita di dati e chiede loro di "chiudere forzatamente" il canale con loro, in modo da poter recuperare la propria quota onchain.



L'idea è che i tuoi pari, notando che state segnalando una perdita di dati, trasmetteranno il loro ultimo commitment transaction e chiuderanno il canale di forza. Una volta confermate le transazioni, i fondi riappaiono nel tuo wallet onchain (collegato al seed).



Questo meccanismo di recupero, tuttavia, non è perfetto. In primo luogo, non ripristina il nodo Lightning, poiché tutti i canali vengono chiusi. Dovrete quindi costruire un nuovo nodo Lightning da zero. In secondo luogo, non garantisce il 100% di recupero, anche se aumenta notevolmente le possibilità di recuperare i saldi onchain in caso di problemi. Infatti, questo protocollo di recupero dipende dalla collaborazione e dalla disponibilità dei tuoi peer: se uno di essi è offline, ha perso i propri dati o si rifiuta di collaborare, i tuoi fondi potrebbero rimanere bloccati o addirittura andare definitivamente persi. Per questo motivo è importante non tenere canali aperti sul proprio nodo Lightning con peer non raggiungibili per lunghi periodi di tempo. Se a quel punto si verifica una perdita di dati e il peer rimane irraggiungibile, il recupero tramite SCB sarà impossibile e i fondi resteranno persi finché il peer non tornerà online (forse per sempre).



In sintesi, una buona strategia di backup Lightning su LND si basa su tre pilastri:




- Il tuo seed (*aezeed*), per lo strato onchain;
- Backup automatico affidabile del sistema SCB;
- Una buona gestione del canale, scegliendo i peer affidabili e chiudendo preventivamente quelli spesso irraggiungibili.



### In che modo il Umbrel gestisce il backup del nodo LND?



Umbrel offre un meccanismo di backup semplificato per il nodo LND, basato proprio sull'SCB. L'idea è quella di risparmiarvi la fatica di manipolare questo file da soli, di farne un backup e di automatizzare il più possibile il processo.



Quando si crea il nodo su Umbrel, si riceve un seed che svolge un doppio ruolo:




- deriva il tuo Bitcoin sul wallet on-chain associata al tuo nodo Lightning;
- viene utilizzato per ricavare un identificatore di backup e una chiave di crittografia utilizzata per i backup SCB remoti.



Grazie a questo meccanismo, Umbrel esegue automaticamente un backup criptato della tua SCB e lo archivia sui suoi server tramite Tor. La SCB viene memorizzata in modo criptato, grazie a una chiave derivata dal seed. Quindi, in caso di perdita di dati, basta ricreare un nodo Bitcoin e un nodo Lightning su Umbrel, sulla stessa macchina o su un'altra, quindi inserire il proprio seed. Sarà quindi possibile recuperare l'ultimo stato dell'SCB dai server del Umbrel, decriptarlo e avviare il processo di recupero dei fondi.



Questi backup vengono crittografati localmente dal nodo prima di essere inviati, il che garantisce la riservatezza dei dati: Il Umbrel non può leggere il contenuto dell'SCB. La trasmissione avviene tramite Tor, che impedisce la diffusione del tuo indirizzo IP. Inoltre, il Umbrel aggiunge rumore al traffico (padding casuale e falsi backup inviati a intervalli irregolari) per impedire al server di dedurre con precisione quando si apre o si chiude un canale.



Il vantaggio principale di questo metodo è che semplifica notevolmente il backup del nodo Lightning: è sufficiente eseguire il backup del seed una sola volta durante l'inizializzazione del nodo. Ciò comporta qualche rischio, poiché si tratta solo di un backup dell'SCB, ma per importi ragionevoli è un compromesso accettabile.



### Le migliori pratiche per limitare il rischio di perdita



Anche con il backup del Umbrel, alcune semplici buone pratiche possono ridurre notevolmente il rischio di perdere il sats:





- Monitorate la disponibilità dei tuoi colleghi:



Se un canale importante è spesso associato a un peer irraggiungibile o instabile, è più sicuro chiuderlo in modo pulito mentre il nodo è ancora funzionante. Una chiusura cooperativa preventiva o forzata elimina una potenziale fonte di problemi in caso di ripristino dell'SCB.





- Evitate di concentrare troppa liquidità su pari sconosciuti:



Più grande è il canale che un peer ha con te, più è importante che sia affidabile. Scegliete nodi seri, ben collegati e attivi, in modo che ogni futuro recupero tramite SCB possa avvenire senza problemi.





- Integrate il Umbrel con i backup locali:



Oltre al backup automatico del Umbrel, è possibile conservare una copia criptata del file SCB (`channel.backup`) su un supporto esterno e aggiornarla periodicamente. L'ideale sarebbe rinnovarlo ogni volta che si apre o si chiude un canale. In questo modo si ottiene una soluzione di backup se, per qualsiasi motivo, il servizio di backup automatico del Umbrel non è disponibile.





- Gestire il seed nel modo giusto



Il tuo seed Umbrel non solo ripristina il tuo wallet onchain, ma ricava anche la chiave di crittografia per i backup. Un aggressore che vi abbia accesso potrebbe quindi lanciare un recupero e trasferire i tuoi fondi al proprio wallet, senza nemmeno avere accesso fisico al tuo nodo.



Pertanto, se è necessario ripristinare il nodo ma non si dispone più del seed, non sarà possibile recuperare nulla: tutto il sats andrà perso. È quindi molto importante salvare il seed con la massima cura, solo su supporti fisici (carta o metallo), e conservarlo in un luogo sicuro. Per ulteriori informazioni sulla gestione di un seed, consultare questo tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Come si salva il nodo Lightning su Umbrel?



Ora che avete capito come funziona la teoria, passiamo alla pratica. Dall'applicazione Lightning Node (che in realtà è LND), fate clic sui tre puntini in alto a destra.



![Image](assets/fr/022.webp)



Ci sono tre elementi di interesse per il backup:




- Verificare che l'opzione "Backup automatico" sia attivata. Questo invierà automaticamente il tuo SCB crittografato ai server di Umbrel.
- Si può quindi scegliere se inviare tramite Tor o Clearnet, utilizzando l'opzione `Backup over Tor`. Come spiegato nelle sezioni precedenti, vi consiglio vivamente di usare Tor per preservare la tua riservatezza.
- Infine, c'è un pulsante "Scarica il file di backup del canale", che consente di scaricare sul proprio computer un file "channel.backup", cioè un'istantanea criptata del proprio SCB. In questo modo è possibile effettuare di tanto in tanto ulteriori backup locali, oltre a quelli inviati automaticamente ai server Umbrel.



Ora sapete come proteggere il sats del tuo nodo Lightning dalla perdita di dati. Nel prossimo capitolo vedremo come proteggere il nodo da tentativi di truffa.




## Watchtower: ruolo e impostazione


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



In Lightning, ogni canale si basa su una sequenza di stati successivi, rappresentati da commitment transaction non pubblicati. A ogni pagamento o routing Lightning, i 2 partecipanti al canale costruiscono una nuova coppia di commitment transaction, che riflette l'attuale distribuzione dei fondi nel canale. I vecchi commitment transaction diventano obsoleti.



Se una delle parti pubblica uno stato non aggiornato, l'altra ha il diritto di sanzionarla e di recuperare l'intero ammontare dei fondi del canale. In questo capitolo daremo una breve occhiata al funzionamento di questo meccanismo e spiegheremo come impostare una ***watchtower***: un sistema per proteggere il nodo Lightning da eventuali tentativi di truffa.



### Capire come funzionano le watchtower


In qualsiasi momento, ogni parte del canale ha un commitment transaction che, se pubblicato, gli permetterebbe di chiudere il canale e di recuperare la propria quota di fondi. Questo processo è noto come *chiusura forzata*. Ma se tentassero di pubblicare un commitment transaction più vecchio, corrispondente a uno stato precedente del canale in cui deteneva più sats, allora questa transazione sarebbe considerata un tentativo di truffa. In questo caso, la controparte può usare la chiave di revoca associata a questo stato più vecchio per recuperare l'intero ammontare dei fondi nel canale, mentre l'imbroglione è temporaneamente bloccato dal timelock.


Questo sistema significa che pubblicare un vecchio stato, cioè tentare di imbrogliare, è molto rischioso: se l'altra parte vede questa transazione sul mempool o sulla blockchain prima della scadenza del timelock, può usare la chiave di revoca e recuperare tutti i fondi. **Pertanto, la sicurezza del tuo canale Lightning dipende dalla tua capacità di rilevare un tentativo di imbroglio entro la finestra temporale imposta dal timelock**.



#### Perché le watchtower sono necessarie?



Il meccanismo sanzionatorio funziona solo se la parte lesa è in grado di farlo:




- monitorare ogni nuovo blocco Bitcoin per vedere se è stato pubblicato un canale commitment transaction;
- determinare se questa transazione corrisponde all'ultimo stato valido o a uno stato revocato;
- in caso di revoca, trasmettere la transazione legale in tempo utile, utilizzando la chiave di revoca per recuperare tutti i fondi prima della scadenza del timelock.



![Image](assets/fr/023.webp)



In uno scenario ideale, il nodo Lightning è online 24 ore su 24, 7 giorni su 7, è sincronizzato e monitora continuamente la blockchain. Per questo motivo, può rilevare da solo un tentativo di truffa e reagire. In pratica, però, un nodo Lightning personale può spegnersi, soprattutto in caso di interruzione prolungata della corrente o di interruzione della connessione a Internet.



È proprio durante questi periodi di inattività che il rischio diventa reale: se un peer disonesto pubblica un vecchio status mentre il tuo nodo è offline e il timelock si esaurisce senza alcuna reazione da parte tua, l'imbroglio diventa effettivo. Si perdono alcuni o tutti i fondi del canale.



Le Watchtower sono state introdotte per ridurre questo rischio. Una watchtower è un servizio esterno che monitora la blockchain per conto dell'utente, analizzando l'eventuale pubblicazione di un vecchio stato su uno dei suoi canali e, se necessario, trasmette automaticamente la transazione sanzionata per suo conto. Quindi, anche se il tuo nodo Lightning rimane offline per un periodo prolungato, finché la watchtower che state utilizzando è operativa, sarà in grado di proteggere i tuoi fondi monitorando eventuali tentativi di truffa e applicando la penalità corrispondente, non appena ne rileva uno.



#### Come funziona una watchtower



Una watchtower è progettata per ridurre al minimo le informazioni che apprende sui tuoi canali, fornendole al contempo i mezzi per agire in caso di problemi:




- Per ogni nuovo stato di canale con un peer, il nodo prepara in anticipo una potenziale transazione di penalizzazione. Nel caso in cui il peer barasse, questa transazione permetterebbe di recuperare tutti i fondi del canale;
- Il nodo cripta quindi questa transazione di penalizzazione utilizzando il TXID del commitment transaction corrispondente (quello che verrebbe utilizzato se l'imbroglione tentasse una frode). Finché non avviene la chiusura, la watchtower non può decrittare questa transazione, poiché non conosce il TXID della transazione truffaldina;
- Il nodo invia alla watchtower un pacchetto contenente la transazione di penalità criptata e metà del TXID della transazione potenzialmente truffaldina.



Poiché il TXID trasmesso alla watchtower è incompleto, essa non può decriptare la transazione di giustizia. Tuttavia, può monitorare la blockchain alla ricerca di un TXID che corrisponda alla parte di sua proprietà. Se rileva una transazione di questo tipo, tenta di utilizzare il TXID completo di quella transazione per decriptare la transazione di giustizia. Se la decrittazione ha successo, sa che si tratta di un tentativo di truffa e pubblica immediatamente la transazione di penalità per l'utente.



![Image](assets/fr/024.webp)



La watchtower non ha quindi visibilità sui dettagli dei tuoi canali: né l'identità dei tuoi pari, né i saldi, né la struttura delle transazioni. Vede solo i pacchetti criptati. L'unica informazione che può dedurre è la velocità di aggiornamento dei tuoi canali, poiché riceve un pacchetto per ogni nuovo stato, ma non è in grado di conoscerne il contenuto. In caso di imbroglio, scoprirà sicuramente le informazioni sul canale decriptando la transazione di penalità, ma almeno il tuo sats sarà salvo.



Questo meccanismo si basa su un compromesso: si delega alla watchtower la capacità di pubblicare una transazione penale pre-firmata, ma questa transazione rimane totalmente opaca per la watchtower fino a quando non avviene un imbroglio. La watchtower non può né modificare i destinatari né deviare i fondi, poiché dispone solo di una transazione già firmata, con gli output congelati a tuo favore. Non può nemmeno conoscere i dettagli di un canale in una legittima chiusura forzata o cooperativa, poiché i TXID non corrispondono. D'altra parte, watchtower rimane una terza parte minimamente fidata: devi fare affidamento sul fatto che sia online e che trasmetta correttamente la tua transazione di giustizia quando ne avete bisogno.



#### Diventare una watchtower



In teoria, qualsiasi nodo Lightning può fungere da watchtower per altri nodi (se utilizzano la stessa implementazione, ad esempio LND), mentre è protetto da altri nodi che svolgono questo ruolo per lui. Nelle sezioni pratiche che seguono, vi mostrerò come impostare questo semplice meccanismo sul tuo LND sotto Umbrel.


Di conseguenza, una strategia interessante potrebbe essere quella di concordare con amici bitcoiner fidati di fungere da watchtower reciproca. Voi monitorate i loro canali e loro monitorano i tuoi.



### Trovare una watchtower altruista



Se non conoscete nessuno che possa fornire un servizio di watchtower, ci sono diverse watchtower pubbliche altruiste a cui potete collegarvi. Per esempio, in questo corso LNP202, vi suggerisco di collegarvi al servizio di watchtower offerto congiuntamente da LN+ e Voltage, che è una watchtower per LND.


Qui sono disponibili i dati di accesso:



- Via Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Via clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Per ringraziarli di fornire questo servizio gratuito della Torre di Guardia, [è possibile fare una donazione tramite Lightning](https://lightningnetwork.plus/donation).


Ora che utilizziamo un servizio di watchtower altruista, vediamo come configurarlo sul nostro nodo LND sotto Umbrel.


### Installazione di una watchtower


Dall'applicazione `Lightning Node`, fare clic sui tre punti in alto a destra dell'interfaccia, quindi selezionare `Impostazioni avanzate`.


![Image](assets/fr/025.webp)


Andare quindi al menu `Watchtower`.


![Image](assets/fr/026.webp)



Attivare l'opzione "Client Watchtower", quindi fare clic sul pulsante "Salva e riavvia il nodo". Attendere il riavvio del LND.


![Image](assets/fr/027.webp)


Una volta completato il riavvio, tornate allo stesso menu e inserite l'ID della watchtower altruista di tua scelta nell'apposito campo. Fare quindi clic sul pulsante `ADD` per confermare. È inoltre possibile regolare il parametro `Watchtower Client Sweep Fee Rate`: si tratta della tariffa che si è disposti a pagare per un'eventuale transazione di giustizia trasmessa dalla watchtower. Non è necessario scegliere una tariffa eccessivamente alta, ma bisogna anche evitare una tariffa troppo bassa, altrimenti la transazione legale non sarà confermata in tempo.


Riavviare il nodo utilizzando il pulsante `SAVE AND RESTART NODE` per applicare le modifiche.


![Image](assets/fr/028.webp)



Se tornate a questo stesso menu, vedrete che il tuo nodo Lightning è ora protetto dalla watchtower appena aggiunta.



![Image](assets/fr/029.webp)



Una watchtower altruista è generalmente sufficiente, soprattutto se non si depositano grandi quantità di denaro sul nodo Lightning e se si gestisce bene il nodo (non lasciarlo spento per troppo tempo). Per una sicurezza ancora maggiore, potete anche aggiungerne diverse ripetendo lo stesso procedimento.



## Aprite il tuo primo canale Lightning


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Se siete arrivati fin qui, sapete già che un nodo Lightning senza canale è un po' come un wallet vuoto: esiste, ma è inutile. Per poter inviare o ricevere pagamenti, il tuo nodo deve essere collegato ad almeno un altro nodo della rete Lightning tramite un canale. In futuro, consigliamo vivamente di aprire più canali, per ragioni di resilienza e di efficienza di routing. Nei capitoli successivi, vedremo anche come gestire le attività liquide, ottimizzare la topologia dei canali e utilizzare strumenti più avanzati rispetto all'interfaccia di base del LND sul Umbrel.



Ma in questo capitolo introduttivo, l'obiettivo è semplicemente quello di capire come scegliere un buon peer Lightning, dove trovare le informazioni necessarie per selezionare i peer e infine come aprire il primo canale attraverso l'interfaccia di base del LND.



### Come scegliere un buon Lightning peer?



Quando si apre un canale, è necessario scegliere un peer: un altro nodo Lightning a cui il proprio nodo sarà direttamente collegato, tramite un canale. La scelta del peer è importante, poiché avrà un impatto diretto su:




- la facilità con cui i tuoi pagamenti trovano la loro strada;
- l'affidabilità dei tuoi canali nel tempo;
- i costi di routing.



Non esiste una corrispondenza perfetta per tutti, ma esistono alcuni criteri affidabili per identificare i candidati validi.



#### 1. Connettività dei nodi



Un buon peer è un nodo ben connesso alla rete Lightning. Ciò significa non solo avere un gran numero di canali (anche se questo può essere un indicatore), ma soprattutto essere connesso ad altri nodi affidabili e occupare una posizione sufficientemente centrale nel grafo della rete.



Un nodo ben collegato aumenta le possibilità di trovare un percorso efficiente verso la maggior parte delle destinazioni di pagamento. Inoltre, riduce il numero di nodi intermediari necessari, con conseguente riduzione dei costi.



Al contrario, aprire il primo canale a un nodo isolato o debolmente connesso può limitare le tue possibilità: sarete in grado di pagare questo peer, ma sarà molto più difficile pagare il resto della rete.



#### 2. Capitalizzazione e capacità del canale



Un buon peer è anche un nodo sufficientemente capitalizzato. Ciò è dimostrato dalla sua capacità totale di canale (la somma dei sats impegnati in tutti i suoi canali) e dalla sua capacità media di canale (spesso è meglio avere pochi canali ben capitalizzati che molti piccoli).



Un nodo con una capacità ridicola, o i cui canali sono tutti minuscoli, non sarà in grado di instradare pagamenti di importo elevato, con conseguenti errori di routing.



#### 3. Politiche di spesa



Ogni nodo stabilisce le proprie tariffe di routing (`base fee` e `fee rate`). Un buon peer non applicherà tariffe esorbitanti per i canali strategici. Per un primo canale, è meglio scegliere un nodo con tariffe piuttosto moderate, in modo da non penalizzare i propri pagamenti.



Ricordate che le tue tariffe di routing influenzano anche la percezione che gli altri hanno di te come peer: un nodo che cambia costantemente le sue tariffe o impone costi assurdi è raramente apprezzato.



#### 4. Stabilità e anzianità



La stabilità dei peer è un criterio molto importante. Un buon nodo ha un tempo di attività elevato (è molto raramente offline), mantiene i suoi canali aperti per molto tempo e non apre/chiude costantemente i canali senza motivo.



I canali vecchi e ancora attivi sono un buon segnale: suggeriscono che la relazione è redditizia per il peer, che il nodo sa come gestire il suo capitale e che non chiude in qualsiasi momento, in modo da non dover continuare a pagare le commissioni onchain per la chiusura e la riapertura.



Al contrario, un peer che è spesso offline o che chiude rapidamente i canali può essere fonte di problemi per te e di costi aggiuntivi per l'apertura di nuovi canali.



Anche con questi criteri, non riuscirete a fare una scelta perfetta al primo colpo. È normale: la vera qualità di un peer si rivela con il suo utilizzo. È quindi importante:




- monitorare l'attività del canale (volumi instradati, disponibilità, ecc.);
- chiudere i canali che non servono a nulla o i cui pari sono troppo spesso offline;
- riallocare il proprio capitale su peers migliori nel corso del tempo.



L'idea non è quella di aprire e chiudere canali ogni giorno (il che sarebbe costoso in termini di costi onchain), ma di far evolvere gradualmente la topologia per convergere su un insieme di peer affidabili e ben connessi, compatibili con le proprie esigenze.



### Come si fa a trovare un coetaneo?



Per applicare questi criteri, è necessario disporre di strumenti che forniscano visibilità alla rete Lightning. A questo scopo sono disponibili diversi esploratori e servizi. Tra i più noti esploratori di Lightning ci sono [1ML](https://1ml.com/) e [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

In questo caso, tuttavia, vi suggerisco di utilizzare [lo strumento Lightning Terminal di Lightning Labs](https://terminal.lightning.engineering/), che fornisce una classifica (basata in parte su criteri soggettivi) dei nodi Lightning ritenuti più rilevanti per l'apertura di un canale.



![Image](assets/fr/030.webp)



Il problema con i nodi Lightning molto grandi in cima a questa classifica è che la maggior parte non accetta aperture di canali al di sotto di importi molto elevati. Molti applicano anche rigide politiche di gestione dei peer, che possono portare alla chiusura del canale. D'altra parte, questi nodi non hanno generalmente bisogno di liquidità in entrata, dato il loro numero di connessioni.



Vi consiglio quindi di scendere nella classifica per trovare un nodo ben connesso, affidabile e sufficientemente centrale nel grafo della rete, senza essere eccessivamente grande. Ad esempio, qui ho identificato il nodo Lightning di stacker.news, che è molto ben connesso, ha una capacità elevata e occupa una posizione centrale nel grafo della rete.



![Image](assets/fr/031.webp)



Un altro approccio interessante è quello di aprire un canale verso un nodo che ha bisogno di liquidità in entrata, come un commerciante conosciuto, un'associazione o una comunità. Questa strategia presenta tre vantaggi:




- Poiché l'entità scelta ha bisogno di liquidità in entrata, avrà logicamente meno incentivi a chiudere il tuo canale senza motivo;
- La sua attività economica aumenta le possibilità di routing su questo canale, e quindi di riscuotere alcune tariffe;
- State facendo un favore all'ecosistema e state dando un contributo prezioso agli altri bitcoiners.



Una volta identificato un nodo rilevante, è possibile recuperare il suo ID nodo. Si tratta semplicemente di una concatenazione della chiave pubblica del nodo, un separatore `@`, il suo indirizzo IP o Tor e la porta utilizzata. Questo ID è facilmente accessibile dal profilo del nodo in qualsiasi Lightning explorer.



### Aprire il primo canale tramite LND



Ora che abbiamo identificato il nodo con cui aprire il nostro primo canale, abbiamo bisogno che il sats si agganci ad esso. Per farlo, è necessario alimentare il Bitcoin sul wallet on-chain associata al LND.



Dall'interfaccia principale del LND, individuare il proprio `Bitcoin Wallet`, quindi fare clic sul pulsante `Deposit`. Un indirizzo di ricezione onchain è quindi il generated: inviategli il sats. L'importo da trasferire dipende dalla capacità che si desidera assegnare al primo canale, ma bisogna tenere presente che è necessario inviare una quantità leggermente superiore alla capacità desiderata. Ad esempio, se volete aprire un canale da 500.000 sats, non inviate esattamente 500.000 sats, ma una quantità superiore.



![Image](assets/fr/032.webp)



Una volta trasmessa, la transazione appare nell'interfaccia. Attendere la conferma prima di aprire il canale. Quando la transazione è confermata, viene visualizzata una freccia verde accanto ad essa.



![Image](assets/fr/033.webp)



Scorrere fino all'interfaccia principale, quindi fare clic su `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Inserite il `Node ID` del nodo con cui desiderate aprire un canale, indicate l'importo che desiderate bloccare e quindi regolate la commissione di apertura della transazione in base allo stato del mercato delle commissioni onchain. Naturalmente, assicuratevi di disporre di fondi sufficienti nel tuo wallet onchain LND prima di procedere.



Una volta impostati tutti i parametri, fare clic sul pulsante "APRI CANALE".



![Image](assets/fr/035.webp)



Attendete la conferma della transazione di apertura sulla catena. Il tuo primo canale è ora ufficialmente operativo: congratulazioni!



Si può notare che, per il momento, il 100% della liquidità del canale è dalla mia parte: è normale, visto che sono io ad aver aperto il canale. Con l'evoluzione dei pagamenti e del routing, questa distribuzione cambierà, ma la capacità totale del canale rimarrà sempre la stessa.



![Image](assets/fr/036.webp)



Ora che si dispone di un canale, è possibile effettuare i primi pagamenti con Lightning, a condizione che il nodo scelto sia correttamente connesso alla rete. Naturalmente, nei capitoli successivi vedremo come impostare un metodo più comodo per pagare le intece Lightning dal cellulare. Ma per ora proviamo a effettuare un primo pagamento direttamente da LND a Umbrel.



A tal fine, nella sezione `Lightning Wallet`, fare clic sul pulsante `Invia`, quindi incollare la intece da impostare.



![Image](assets/fr/037.webp)



Viene visualizzato l'importo della intece. Confermare il pagamento facendo clic sul pulsante "Invia".



![Image](assets/fr/038.webp)



Se viene trovato un percorso valido, il primo pagamento Lightning dovrebbe andare a buon fine.



![Image](assets/fr/039.webp)



Se poi osserviamo la distribuzione della liquidità nel canale, vediamo che il mio pari ha ora 5.002 sats dalla sua parte. Questo corrisponde ai 5.000 sats del pagamento che ho appena effettuato, che ha instradato verso il nodo del destinatario. I 2 sats aggiuntivi rappresentano le commissioni di routing che ho pagato, poiché il destinatario ha ricevuto esattamente 5.000 sats.



![Image](assets/fr/040.webp)



Per migliorare l'affidabilità dei nostri pagamenti, sarà ovviamente necessario aprire altri canali. A seconda dei nostri obiettivi, dovremo anche trovare un modo per rendere disponibile la liquidità in entrata in modo da poter ricevere i pagamenti su Lightning. Questo sarà l'argomento della prossima sezione.



# Gestione del nodo Lightning


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Definire il profilo dell'operatore del nodo


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Ora che il tuo nodo Lightning è attivo e funzionante, il passo successivo è quello di definire il tuo profilo di trader. Si tratta di una scelta importante, poiché determina la strategia di apertura del canale, il tipo di peer che preferite e il modo in cui gestite la liquidità.



Su Lightning, perché questo funzioni, è necessaria la liquidità nella giusta direzione. La liquidità in uscita corrisponde alla tua capacità di pagare (sats disponibile sul tuo lato dei canali). La liquidità in entrata corrisponde alla tua capacità di ricevere (sats disponibile sul lato dei tuoi pari). In altre parole, il tuo profilo si riduce a una semplice domanda: per la maggior parte del tempo, le tue sats escono dal tuo nodo o vi entrano?



### Il consumatore



Questo è il profilo della stragrande maggioranza degli utenti. Utilizzate il tuo nodo per effettuare pagamenti con Lightning: per acquistare beni e servizi, pagare bollette, inviare mance - in breve, per utilizzare Lightning come mezzo di pagamento rapido. D'altro canto, si riceve poco da Lightning, o solo marginalmente, ad esempio qualche donazione, rimborsi tra amici o qualche micropagamento.



Questo profilo è il più facile da gestire, perché la tua esigenza principale è quella di poter pagare. In termini pratici, ciò significa che avete bisogno di liquidità in uscita. Una volta aperti uno o più canali di dimensioni corrette verso nodi stabili e ben collegati, i pagamenti in uscita sposteranno meccanicamente la liquidità dall'altra parte dei canali. È proprio questo movimento che crea naturalmente una quantità ragionevole di liquidità in entrata. Di conseguenza, anche se non desiderate ricevere regolarmente, sarete comunque in grado di ricevere di tanto in tanto senza dover attuare una strategia complessa. Non devi quindi preoccuparvi della tua liquidità in entrata.



In questo corso LNP202 ci concentreremo su questo profilo di operatore di nodo "consumer", poiché è quello che corrisponde a quasi tutti gli utenti di Bitcoin su Lightning.



### Il rivenditore



Il commerciante è, in un certo senso, l'opposto del consumatore. In questo caso, l'obiettivo principale non è il pagamento, ma l'incasso. Un'azienda, un fornitore di servizi, un negozio online o un punto vendita che accetta Lightning riceverà molti pagamenti in entrata ed effettuerà relativamente pochi pagamenti in uscita da questo nodo.



Questo profilo è più esigente, poiché un pagamento rifiutato su Lightning rappresenta potenzialmente una vendita persa. La priorità diventa quindi la liquidità in entrata. Se il tuo nodo non ha abbastanza liquidità in entrata, i tuoi clienti vedranno i loro pagamenti fallire, anche se hanno i fondi, semplicemente perché non c'è un percorso per farvi arrivare la liquidità nella giusta direzione.



La sfida principale per il commerciante deriva anche dalla naturale evoluzione dei canali. Se non fate altro che ricevere, i tuoi canali si riempiranno gradualmente. È quindi necessario disporre di meccanismi per mantenere e rinnovare la liquidità in entrata.



Esiste tuttavia un caso più semplice: il profilo misto consumatore/commerciante. Se si incassa su Lightning, ma si spende anche su Lightning (spese aziendali, pagamenti ai fornitori o anche spese personali), i pagamenti in uscita ricreano naturalmente quelli in entrata. La gestione diventa più fluida, poiché i flussi si compensano a vicenda, e si ha meno bisogno di ricorrere a meccanismi artificiali progettati esclusivamente per recuperare la liquidità in entrata.



### Il router



Il router è un profilo specifico. Non utilizza il proprio nodo Lightning per pagare o riscuotere, ma per instradare i pagamenti degli altri e riscuotere le commissioni. L'obiettivo è quello di essere un percorso utile, affidabile ed economicamente competitivo all'interno del grafo di Lightning.



In tutta onestà, essere un router su Lightning è un'attività più complessa di quanto sembri e la redditività è difficile da raggiungere. Innanzitutto, aprire e chiudere canali è costoso in termini di costi onchain. Per instradare in modo efficiente, è spesso necessario modificare la topologia, effettuare test, chiudere i canali poco performanti, aprirne di nuovi e riequilibrare regolarmente la liquidità. In secondo luogo, la concorrenza è agguerrita: i nodi grandi e consolidati si accaparrano naturalmente un'ampia fetta di traffico, ed è difficile prendere piede senza impegnare un capitale significativo in canali di buone dimensioni.



Vi è anche un elevato requisito operativo. Un nodo di routing deve essere estremamente stabile, monitorato, con un backup adeguato e gestito in modo rigoroso. È necessario monitorare le prestazioni del canale, adattare la politica delle commissioni, mantenere una liquidità equilibrata, gestire i peer e risolvere rapidamente i problemi tecnici. Questo livello di coinvolgimento può essere interessante come hobby tecnico o come contributo all'infrastruttura, ma se il tuo obiettivo è semplicemente quello di utilizzare Lightning in modo sovrano, entrare nel routing per fare soldi è raramente rilevante. Ecco perché questo corso LNP202 non tratta questo profilo in modo approfondito.



### Posizionarsi chiaramente prima di andare avanti



Se rientrate nel profilo del consumatore, la tua priorità sarà quella di poter pagare in modo affidabile con una gestione semplice. Se siete un commerciante, la tua priorità sarà quella di incassare senza fallire, il che implica una strategia di acquisizione di liquidità in entrata. Se state considerando il routing, devi affrontarlo come un'attività impegnativa, economicamente incerta e che richiede tempo.



La definizione di questo profilo vi aiuterà a evitare un classico trabocchetto: applicare una strategia di canale pensata per un commerciante o un router, quando te siete semplicemente un utente che vuole pagare.



## Utilizzo di un gestore di nodi Lightning


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Nella parte precedente di questo corso di formazione sul LNP202, abbiamo utilizzato l'interfaccia di base dell'applicazione `Lightning Node` del Umbrel. Questa interfaccia è sufficiente per le operazioni essenziali (controllo dei saldi, visualizzazione della distribuzione del contante, apertura e chiusura dei canali), ma è volutamente molto semplificata. Questa semplicità limita le opzioni disponibili e non permette di accedere a molte delle funzioni avanzate del nodo LND. Per questo motivo, ora utilizzeremo un altro software di gestione del nodo Lightning, più completo.



Questo software aggiuntivo sarà semplicemente un'interfaccia di gestione complementare per il tuo nodo. Ciò significa che si può continuare a usare l'interfaccia `Lightning Node` in parallelo, e anche usarne diverse se lo si desidera. Si tratta semplicemente di modi diversi di interagire con lo stesso nodo Lightning.



Tra i programmi software più noti vi sono:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Tutte e tre le soluzioni sono valide. Se lo desiderate, potete provarle tutte e tre con il tuo nodo prima di scegliere quella più adatta a te. Personalmente, uso ThunderHub per abitudine e perché mi sembra più completo degli altri. È lo strumento che presenterò in questo corso di formazione, ma potete anche scegliere una delle altre due alternative. Per ognuno di questi programmi abbiamo un tutorial dedicato su Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Installare ThunderHub



Tutti questi programmi possono essere installati molto facilmente dall'App Store Umbrel . Come ho detto, qui useremo il ThunderHub, ma se volete testarne un altro in seguito, la procedura sarà simile.



![Image](assets/fr/041.webp)



Il Umbrel fornisce una password predefinita per accedere al ThunderHub. Copiatela: vi servirà subito. Ricordatevi anche di salvarla nel tuo gestore di password, perché vi verrà richiesta ogni volta che aprirete il software.



![Image](assets/fr/042.webp)



Fare clic su `Login`, quindi incollare la password fornita da Umbrel per accedere.



![Image](assets/fr/043.webp)



Si accede quindi alla pagina iniziale del ThunderHub, che visualizza le informazioni principali sul nodo Lightning.



![Image](assets/fr/044.webp)



Per cominciare, vi consiglio di attivare l'autenticazione a due fattori (2FA). Nelle impostazioni, è sufficiente fare clic su `Attiva` accanto a `Attiva 2FA`, quindi seguire la procedura abituale.



![Image](assets/fr/045.webp)



### Utilizzare ThunderHub



ThunderHub è relativamente facile da imparare. Tutti i menu sono accessibili dalla colonna sinistra dell'interfaccia. In sintesi, ecco cosa fa ciascuno di essi:




- home: panoramica dei nodi, bilanci e azioni rapide;
- dashboard: dashboard personalizzabile con widget e metriche;
- peer: visualizza e gestisce le connessioni ad altri nodi Lightning;
- channels: gestione completa dei canali (liquidità, commissioni, chiusura, ecc.);
- rebalance: uno strumento per riequilibrare i canali tramite pagamenti circolari;
- translactions: cronologia dei pagamenti Lightning inviati e ricevuti;
- forwards: statistiche di routing e costi generated del nodo;
- chain: wallet onchain Bitcoin (UTXO e transazioni);
- integrazione di gW-201 per il monitoraggio e il backup;
- tools: strumenti avanzati (backup, report, macaron, firme, ecc.);
- swap: swap lightning/on-chain tramite Boltz;
- stats: statistiche generali e prestazioni del nodo Lightning.



Con questo insieme di funzioni, si dispone di tutti gli strumenti necessari per gestire in modo efficiente il nodo Lightning. Non è indispensabile padroneggiare subito ogni opzione in dettaglio: le esploreremo progressivamente nel corso di questo corso. Tuttavia, se desiderate approfondire la conoscenza del software, date un'occhiata alla nostra guida ThunderHub:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Il menu che ci interessa di più è "Canali". Offre una visione dettagliata di tutti i canali del nodo, con la loro distribuzione della liquidità. In particolare, è possibile vedere quali canali sono aperti in `Open`, quali sono in attesa di essere aperti o chiusi in `Pending` e quali sono già chiusi in `Closed`.



![Image](assets/fr/047.webp)



Per un determinato canale, è possibile fare clic sul nome del peer o sull'ID del canale per aprire la sua pagina Amboss e ottenere ulteriori informazioni. È anche possibile fare clic sull'icona della matita per modificare i parametri del canale, compresa la politica delle tariffe applicata a quel canale se il proprio nodo instrada i pagamenti al nodo del peer.



![Image](assets/fr/048.webp)



Se si utilizza il nodo Lightning principalmente come "consumatore", non è necessario modificare questi costi: si possono mantenere i valori predefiniti. D'altra parte, se volete capire meglio come funzionano i costi di routing su Lightning, vi consiglio di seguire il corso LNP 201, in particolare il capitolo 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Facendo clic sulla piccola croce accanto a un peer, è possibile avviare la chiusura di un canale. Se notate, ad esempio, che un peer è regolarmente inattivo, può essere opportuno chiudere questo canale per riallocare il tuo capitale su un peer più affidabile.



A questo punto avete due opzioni. La prima, sempre preferibile, è la chiusura cooperativa. Confermando questa azione, il nodo chiede al suo pari di chiudere il canale congiuntamente. Se accetta, potete trasmettere la transazione di chiusura onchain e recuperare la tua parte di fondi. I vantaggi di questo metodo sono che si scelgono le tariffe onchain per la transazione, evitando così costi inutili, e che i fondi vengono recuperati più rapidamente, senza alcun timelock.



![Image](assets/fr/049.webp)



La seconda opzione è la chiusura forzata. In questo caso, non si chiede il consenso del peer e si trasmette direttamente l'ultimo commitment transaction in proprio possesso. Non consiglio questo metodo se non come ultima risorsa, ad esempio se il peer rifiuta sistematicamente le chiusure cooperative o non risponde più. La chiusura forzata ha due svantaggi principali: le tariffe sono spesso molto alte, poiché sono state fissate in anticipo per anticipare un aumento delle tariffe onchain, e c'è un ritardo nel recupero dei fondi, poiché sono bloccati da un timelock. Questo timelock dà al peer il tempo di reagire in caso di tentativo di truffa (ovviamente non è questo il caso, ma bisogna comunque aspettare).



![Image](assets/fr/050.webp)



Infine, per aprire un nuovo canale, andare al menu `Home` e cliccare su `Aprire un canale` nella sezione `Liquidity`. Sarà quindi possibile inserire l'ID del nodo scelto, la capacità del canale, la tariffa di routing Lightning desiderata e la tariffa onchain per la transazione di apertura.



![Image](assets/fr/051.webp)



Queste sono le azioni principali da eseguire su ThunderHub. Scopriremo altre funzioni nel corso di questo corso LNP202.



## Ottenere liquidità in entrata


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Come si vede, disporre di liquidità in uscita per effettuare pagamenti su Lightning non è particolarmente complesso. Basta aprire di propria iniziativa dei canali verso altri nodi e iniziare a inviare sats. D'altro canto, disporre di liquidità in entrata per ricevere pagamenti su Lightning è più complicato, in quanto è necessario che altri nodi aprano canali verso di te, oppure devi spostare te stessi la liquidità effettuando pagamenti.



Se si adotta un profilo "consumatore", in genere non è necessario preoccuparsi della liquidità in entrata. L'utilizzo del nodo Lightning sarà prevalentemente orientato al pagamento, piuttosto che all'incasso. Effettuando semplicemente alcuni pagamenti Lightning, si creerà naturalmente liquidità in entrata nel corso del tempo.



D'altra parte, se avete un profilo "commerciante", la situazione è invertita: raccoglierete principalmente pagamenti e ne farete pochi. Non si può quindi contare solo sui propri pagamenti per la liquidità in entrata. Diventa quindi necessario che altri nodi Lightning aprano dei canali verso il tuo. Ma come si può ottenere questo risultato? Come convincere altri operatori a vincolare il capitale per te? È proprio questo l'aspetto che analizzeremo in questo capitolo.



### Acquisto di liquidità in entrata



Come ci si aspetterebbe, il modo più efficace per convincere qualcuno ad agire è quello di pagarlo. Per la liquidità in entrata nel tuo nodo Lightning, il principio è esattamente lo stesso. Il modo più semplice per far arrivare i canali al tuo nodo è quello di pagare il servizio e il capitale necessario.



Se siete un'azienda o un rivenditore, questo approccio vi permette di ottenere rapidamente canali affidabili per raccogliere i pagamenti dai tuoi clienti senza attriti.



Esistono molti modi per acquistare liquidità in entrata. Quello che personalmente uso e raccomando è la piattaforma [Magma](https://magma.amboss.tech/) di Amboss. È molto facile da usare, l'apertura di un canale è rapida e i tassi sono generalmente ragionevoli. Magma funziona come un mercato con acquirenti e venditori, ma la versione 2 ha semplificato notevolmente l'esperienza: basta creare una richiesta, pagare il prezzo tramite Lightning e Magma la abbina automaticamente alla migliore offerta disponibile. Dopo sei conferme onchain, il canale con la liquidità in entrata è attivo e funzionante. Ecco come funziona:



Andate su [il sito web di Magma](https://magma.amboss.tech/buy), nella sezione `Acquista canali`.



![Image](assets/fr/052.webp)



Se lo desiderate, potete creare un account per tenere traccia dei tuoi acquisti, ma non è obbligatorio. Se non create un account, Magma vi fornirà semplicemente un ID di sessione, che vi permetterà di recuperare i tuoi acquisti in un secondo momento.



Una volta sul sito, compilate le informazioni richieste per acquistare liquidità. Selezionare "Una volta" per un acquisto una tantum, quindi inserire l'importo che si è disposti a pagare per la liquidità in entrata. Più alto è l'importo pagato, maggiore sarà la capacità del canale aperto al tuo nodo. Di seguito è riportata una stima della capacità del canale: si tratta di un'approssimazione, poiché l'importo finale dipenderà dalla migliore offerta trovata da Magma, che a volte è più alta, a volte più bassa.



![Image](assets/fr/053.webp)



Inserire quindi l'ID del nodo. Lo si può trovare, ad esempio, nel menu `Node ID` dell'applicazione `Lightning Node` su Umbrel.



![Image](assets/fr/054.webp)



Una volta completate tutte le informazioni, fare clic sul pulsante "Rivedi e apri ordine".



![Image](assets/fr/055.webp)



Se non avete creato un account, Magma vi fornirà una chiave di sessione e un file di backup. Conservate questi due elementi in un luogo sicuro, perché vi consentiranno di recuperare l'ordine in un secondo momento o di seguirne lo stato in caso di problemi. Una volta salvato il file, cliccate sul pulsante "Paga con Lightning".



![Image](assets/fr/056.webp)



Magma emette quindi una intece Lightning per l'importo scelto. L'utente deve pagarla. Se si dispone già di canali sul proprio nodo Lightning, è possibile pagare direttamente da esso, oppure utilizzare un altro wallet Lightning esterno.



![Image](assets/fr/057.webp)



Una volta effettuato il pagamento, la transazione appare come in fase di elaborazione nell'interfaccia di Magma.



![Image](assets/fr/058.webp)



Dopo qualche minuto, la richiesta viene elaborata: viene aperto un canale con sats verso il tuo nodo Lightning. Una volta che la transazione di apertura è stata confermata onchain, avrete accesso alla liquidità in entrata corrispondente.



![Image](assets/fr/059.webp)



Magma è anche integrato direttamente in ThunderHub. Nella scheda `Home`, scorrere fino alla sezione `Liquidity` e fare clic su `Acquista Liquidity in entrata`. È sufficiente inserire l'importo desiderato e confermare. Non è necessario pagare manualmente le intece, poiché ThunderHub si occupa automaticamente del pagamento dal tuo nodo.



![Image](assets/fr/060.webp)



Se siete commercianti, questo tipo di servizio è particolarmente adatto, in quanto vi consente di ottenere rapidamente una grande quantità di liquidità in entrata da nodi affidabili, garantendo ai tuoi clienti di potervi pagare senza difficoltà. D'altra parte, se siete un privato o se non volete pagare per la liquidità in entrata, esistono anche soluzioni gratuite. Diamo un'occhiata.



### Liquidità cooperativa in entrata



Se non siete trader, ma avete comunque bisogno di liquidità in entrata (ad esempio, per alimentare il tuo nodo all'avvio, mentre aspettate che vengano effettuati alcuni pagamenti) non devi necessariamente pagarla. Una delle soluzioni che preferisco è quella di collaborare con altri operatori di nodi che hanno bisogno di liquidità in entrata, per aprire reciprocamente dei canali Lightning. In questo modo, l'apertura di un canale vi porta liquidità in uscita e allo stesso tempo vi fornisce liquidità in entrata, gratuitamente (a prescindere dalle commissioni onchain per l'apertura).



Naturalmente è possibile organizzarsi direttamente con i colleghi bitcoiners. Tuttavia, esiste una piattaforma dedicata a questo tipo di apertura circolare: [Lightning Network +](https://lightningnetwork.plus/). Il principio è quello di non aprire due canali tra le stesse persone, ma di creare aperture circolari che coinvolgano un minimo di tre partecipanti, o anche di più.



Facciamo un esempio per capire come funziona il Lightning Network +:




- Un operatore di nodo, chiamato `A`, pubblica un annuncio in cui dichiara di voler aprire un canale sats da 1 milione con altre due persone;
- L'annuncio rimane attivo finché non si aggiungono altri partecipanti;
- Successivamente, due operatori, `B` e `C`, si uniscono all'annuncio del nodo `A`. Il triangolo è ora completo e la fase di apertura può iniziare.
- Il nodo `A` apre un canale verso il nodo `B`;
- Il nodo `B` apre un canale verso il nodo `C`;
- Il nodo `C` apre un canale verso il nodo `A`.



Al termine dell'operazione, ogni nodo dispone di 1 milione di sats di liquidità in uscita e 1 milione di sats di liquidità in entrata. Questo schema può essere esteso a quattro o cinque partecipanti.



Naturalmente, non esiste un meccanismo tecnico che garantisca che un partecipante apra effettivamente il canale che si è impegnato a creare. Per questo motivo la piattaforma ha creato un sistema di reputazione, basato su recensioni positive quando gli operatori rispettano gli impegni presi. E nel peggiore dei casi, se vi imbattete in qualcuno che non collabora, non avrete perso denaro: avrete semplicemente perso un'opportunità di liquidità in entrata.



Questa soluzione è particolarmente adatta a un profilo "consumer", in quanto consente di ottenere gratuitamente la liquidità in entrata, collegando il proprio nodo ad altri piccoli operatori. D'altra parte, se siete un trader, questo approccio non è generalmente pertinente: ogni sat di liquidità in entrata richiede il blocco di un sat di liquidità in uscita, e il tuo grande fabbisogno di liquidità in entrata comporterebbe quindi un eccessivo vincolo di capitale.



Per utilizzare Lightning Network +, avete due possibilità: utilizzare l'applicazione integrata in Umbrel, oppure utilizzare il sito web classico e creare un account accedendo dal tuo nodo. Consiglio quest'ultima opzione, poiché l'applicazione integrata non offre l'intera gamma di funzioni disponibili.



Accedere al sito web [Lightning Network +](https://lightningnetwork.plus/) e fare clic sul pulsante `Login` in alto a destra dell'interfaccia.



![Image](assets/fr/061.webp)



Per autenticarsi, è necessario firmare il messaggio fornito utilizzando la chiave privata del proprio nodo Lightning. Con ThunderHub, questa operazione è molto semplice. Iniziare copiando il messaggio visualizzato da LN+.



![Image](assets/fr/062.webp)



In ThunderHub, andare alla scheda `Strumenti`, quindi fare clic sul pulsante `Firma` nella sezione `Messaggi`.



![Image](assets/fr/063.webp)



Incollare il messaggio di autenticazione fornito da LN+, quindi fare clic su "Firma".



![Image](assets/fr/064.webp)



ThunderHub firma quindi il messaggio utilizzando la chiave privata del nodo. Copiare la firma di generated.



![Image](assets/fr/065.webp)



Incollare questa firma nel campo corrispondente del sito LN+, quindi fare clic su "Accedi".



![Image](assets/fr/066.webp)



Ora siete connessi a LN+ con il tuo nodo Lightning. Questo processo consente a LN+ di verificare che siate i legittimi proprietari del nodo che state rivendicando sulla loro piattaforma.



![Image](assets/fr/067.webp)



Se lo desiderate, potete personalizzare il tuo profilo LN+, ad esempio aggiungendo una breve biografia.



Per partecipare alla prima apertura di un canale circolare, accedere al menu `Swaps` nella parte superiore dell'interfaccia. Qui troverete tutti gli swap attualmente disponibili, a seconda delle caratteristiche del tuo nodo.



![Image](assets/fr/068.webp)



Per aderire a un'offerta di scambio esistente, è sufficiente cliccare su di essa e registrarsi. Tuttavia, su LN+, il creatore di uno scambio può imporre alcune condizioni ai partecipanti, come un numero minimo di canali o una capacità totale minima del nodo. È quindi possibile, soprattutto nei primi giorni, che poche offerte siano disponibili per il tuo nodo. Nel mio caso, nonostante alcuni canali già aperti, nessuna offerta era disponibile per il mio nodo. Ho quindi creato il mio swap, e te potete fare lo stesso se vi trovate nella stessa situazione.



Fare clic su "Avvia Liquidity Swap", quindi inserire i parametri dell'offerta:




- Scegliere il numero totale di partecipanti (3, 4 o 5);
- Indicare la quantità di canali da aprire (assicurarsi di avere almeno questa quantità nelil wallet on-chain);
- Definire il tempo di apertura del canale. È il periodo durante il quale i partecipanti concordano di non chiuderli;
- A destra, è possibile impostare le restrizioni per i partecipanti: numero minimo di canali, capacità totale minima e tipo di connessione accettata.



Una volta impostati tutti i parametri, fare clic sul pulsante `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



La tua offerta di scambio è stata creata. Ora non resta che aspettare che altri operatori di nodi si iscrivano. Se le condizioni non sono troppo restrittive, non dovrebbe volerci molto. Ricordate di monitorare lo stato del tuo scambio nelle ore o nei giorni successivi.



![Image](assets/fr/070.webp)



Tutti i posti di scambio sono stati occupati: ora si passa alla fase di apertura del canale. Ogni partecipante può vedere, dalla sua interfaccia LN+, verso quale nodo deve aprire un canale Lightning.



![Image](assets/fr/084.webp)



Da parte tua, aprite il canale utilizzando l'ID del nodo fornito da LN+ e rispettando la quantità indicata. Come abbiamo visto nei capitoli precedenti, è possibile farlo tramite ThunderHub, con un altro gestore di nodi Lightning o direttamente dall'interfaccia di base dell'applicazione Lightning Node.



![Image](assets/fr/085.webp)



Una volta lanciata l'apertura, la si può vedere apparire nella sezione dei canali in attesa. Nel mio caso, si tratta del canale con il nodo `Plebian_fr`.



![Image](assets/fr/086.webp)



È quindi possibile tornare al LN+ per confermare l'apertura del canale. È sufficiente fare clic sul pulsante "Apertura canale avviata".



![Image](assets/fr/087.webp)



Quando anche tutti gli altri partecipanti avranno aperto il canale su cui si sono impegnati, ricordatevi di lasciare loro una recensione positiva.



![Image](assets/fr/088.webp)



In caso di difficoltà o ritardi, potete contattare direttamente i tuoi colleghi tramite la sezione commenti in fondo alla pagina.



![Image](assets/fr/089.webp)



Alcuni partecipanti potrebbero voler riequilibrare i canali circolari fin dall'inizio, effettuando un pagamento a se stessi. In questo modo si garantisce una distribuzione equilibrata del contante in ogni canale. Se siete in un profilo "consumatore", questo non è essenziale, ma potete fare te stessi questo riequilibrio, se lo desiderate, oppure azzerare temporaneamente le tue spese per i canali, per facilitare il compito a chi vuole farlo. A volte nessuno vuole farlo.



![Image](assets/fr/090.webp)




# Liberare il potenziale del nodo Lightning


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Collegare un wallet mobile tramite il Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Ecco fatto: ora avete un nodo Lightning ben collegato, con liquidità in entrata e in uscita. Siete quindi pronti a utilizzare il tuo nodo Lightning nella vita reale. Finora abbiamo sempre utilizzato le interfacce direttamente su Umbrel, sia l'applicazione `Lightning Node` che l'interfaccia `ThunderHub`. Questi strumenti funzionano per inviare e ricevere pagamenti, ma non sono chiaramente ottimizzati per i pagamenti Lightning di tutti i giorni. L'interfaccia è progettata per l'uso su un computer, impraticabile su uno smartphone, e inoltre richiede una connessione alla stessa rete per funzionare correttamente (anche se è tecnicamente possibile connettersi da remoto tramite Tor).



In pratica, quello che cerchiamo come bitcoiners è una classica interfaccia Lightning wallet su smartphone: la possibilità di scansionare le intece tramite codice QR e un'interfaccia semplice per pagare e incassare sats . Questo è esattamente ciò che implementeremo in questo capitolo e nel prossimo. L'idea generale è quella di avere un'applicazione mobile Lightning wallet sullo smartphone, che può essere utilizzata da qualsiasi luogo (non solo dalla rete locale) ma che, in background, si appoggia al proprio nodo Lightning per inviare e ricevere pagamenti.



### Quali sono le soluzioni per connettere un cliente mobile?



Oggi esistono diversi modi per farlo, sia per quanto riguarda l'applicazione mobile sia per quanto riguarda il tipo di connessione tra il nodo e questa applicazione. Le tre modalità di connessione principali sono:




- via ***Tor***;
- via VPN ***Tailscale***;
- tramite ***Nostr Wallet Connect***.



Qualche anno fa, mi connettevo tramite ***Tor***, ma ho smesso rapidamente: il numero di fallimenti e i ritardi di comunicazione erano troppo elevati. In teoria funziona, ma in pratica l'esperienza dell'utente era catastrofica. Sconsiglio quindi questo approccio.



L'alternativa che ho adottato è stata quella di utilizzare una VPN ***Tailscale*** per garantire la comunicazione tra l'applicazione mobile e il nodo. Questa soluzione funziona molto bene: anche su reti mobili con basso throughput, i miei pagamenti passano sempre senza difficoltà. Questo è il metodo che presenterò per primo in questo capitolo, con l'applicazione Zeus.



Nel prossimo capitolo, esamineremo un'altra soluzione più recente, anch'essa molto efficace: ***Nostr Wallet Connect***. Questa volta utilizzeremo l'applicazione Alby Go per presentarvi un'alternativa, sebbene Zeus sia compatibile anche con NWC, se lo desiderate.



### Installazione e configurazione del Tailscale



Per questo primo metodo, avremo bisogno di Tailscale. Si tratta di una soluzione VPN basata su WireGuard, che consente di collegare in modo sicuro i dispositivi sparsi su Internet, gestendo automaticamente la crittografia, l'autenticazione e il NAT traversal. In parole povere, è come se tutti i dispositivi fossero collegati alla stessa LAN del router, anche se potrebbero trovarsi ovunque in Internet.



Per utilizzarlo, occorre innanzitutto creare un account. Accedere al sito Web di Tailscale, quindi fare clic sul pulsante "Inizia".



![Image](assets/fr/071.webp)



Scegliere quindi un fornitore di identità per l'account Tailscale. Personalmente, ho usato uno dei miei account GitHub per accedere.



![Image](assets/fr/072.webp)



Una volta effettuato l'accesso, vi verranno poste alcune domande sul tuo utilizzo. Rispondete brevemente per continuare.



![Image](assets/fr/073.webp)



Tailscale propone quindi di installare un client sul computer. Per il momento non ci interessa: andate direttamente a Umbrel e installate l'applicazione Tailscale dall'App Store.



![Image](assets/fr/074.webp)



Quando si apre l'applicazione, fare clic su `Log In`, quindi seguire il processo di autenticazione, utilizzando lo stesso metodo utilizzato per la creazione dell'account.



![Image](assets/fr/075.webp)



Fare clic su `Connect` per confermare. Il Umbrel è ora connesso alla rete VPN.



![Image](assets/fr/076.webp)



Scaricate quindi l'applicazione Tailscale sul tuo smartphone e accedete utilizzando lo stesso account. Nota bene: su Android non è possibile utilizzare due VPN contemporaneamente. Affinché il Tailscale funzioni, è necessario disattivare qualsiasi altra VPN attiva. Inoltre, ogni volta che vorrete utilizzare il tuo nodo Lightning tramite Zeus, dovrete attivare la VPN Tailscale, altrimenti la connessione non verrà stabilita.



![Image](assets/fr/077.webp)



Sul sito del Tailscale, ora che almeno due client sono collegati, è possibile accedere alla console di amministrazione con un elenco di tutti i dispositivi collegati alla rete e dei relativi indirizzi IP del Tailscale.



![Image](assets/fr/078.webp)



### Collegare Zeus



Installare l'applicazione Zeus sul telefono. Quando si apre, selezionare `Impostazione avanzata`, quindi `Creare o collegare un wallet`.



![Image](assets/fr/079.webp)



Nella sezione "Interfaccia Wallet", scegliere "LND (REST)". Inserire quindi l'indirizzo Tailscale del Umbrel, che si può trovare nella dashboard del Tailscale o direttamente nell'applicazione Tailscale sul Umbrel. Per la porta, inserire `8080`.



![Image](assets/fr/080.webp)



Zeus chiede quindi di fornire un `Macaroon`. Si tratta di un'autorizzazione token che consente di definire con precisione i diritti concessi a un'applicazione (in questo caso Zeus) per interagire con il nodo Lightning. È possibile generate creare un macaron da ThunderHub, nel menu `Strumenti`, sottomenu `Panetteria`, ma per questo scopo, il modo più semplice è recuperarlo direttamente dall'applicazione `Lightning Node`.



Fare clic sui tre puntini in alto a destra dell'interfaccia, quindi su `Connetti Wallet`. Scegliere `REST (Rete locale)`. Sarà quindi possibile copiare un macaron con i diritti appropriati.



![Image](assets/fr/081.webp)



Incollarlo nel campo corrispondente in Zeus, quindi fare clic sul pulsante `Salva la configurazione del wallet`.



![Image](assets/fr/082.webp)



È ora possibile accedere al proprio nodo Lightning dall'app Zeus. Ciò significa che potete ricevere le intece generate direttamente sul tuo nodo Lightning dal tuo smartphone e pagare le intece Lightning ovunque vi troviate.



![Image](assets/fr/083.webp)



Suggerimento: Tailscale non si limita a utilizzare il nodo Lightning in remoto. Consente di accedere a tutti gli strumenti del Umbrel da altri software, anche in remoto. Ad esempio, è possibile utilizzare l'indirizzo IP Tailscale del Umbrel per connettere il nodo Bitcoin (tramite Electrs o Fulcrum) al Sparrow Wallet, senza passare per Tor. Anche in questo caso, si evita la lentezza insita in Tor. È sufficiente installare il client Tailscale sul computer e collegarlo alla rete.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Nel prossimo capitolo vedremo un altro modo, altrettanto efficace, di collegare un client mobile al nodo Lightning: Nostr Wallet Connect. Utilizzeremo un'applicazione diversa da Zeus (sebbene Zeus sia compatibile anche con NWC), ovvero Alby Go.



## Collegare un wallet mobile tramite NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Se la connessione Tailscale non vi convince o se la gestione di una doppia VPN vi sembra troppo fastidiosa, questo capitolo suggerisce un altro modo di utilizzare un client mobile remoto per pagare e ricevere il sats tramite il tuo nodo Lightning: ***Nostr Wallet Connect***.



Per questo esempio, utilizzeremo l'applicazione mobile Alby Go, che è molto ben progettata e particolarmente facile da imparare. Tuttavia, è possibile utilizzare anche Zeus o qualsiasi altra applicazione mobile compatibile con NWC. Troverete un elenco di applicazioni compatibili su [il repository `awesome-nwc` di GitHub](https://github.com/getAlby/awesome-nwc).



### Come funziona il Nostr Wallet Connect?



Nostr Wallet Connect è un protocollo standardizzato che consente a un'applicazione o a un sito web di attivare azioni su un nodo Lightning remoto, senza stabilire una connessione di rete diretta a tale nodo (nessun API LND esposto, nessuna VPN, nessun servizio `.onion`...). NWC definisce il modo in cui un'applicazione formula un intento (ad esempio, `pagare_intece`) e riceve il risultato.



Il funzionamento è molto semplice. Si inizializza una sessione scansionando un codice QR o tramite un collegamento profondo `nostr+walletconnect:`. Questa stringa contiene i parametri della sessione e un segreto di autorizzazione. Quindi, quando l'applicazione vuole pagare, serializza la richiesta, la cripta e la pubblica come evento su un relay Nostr . Il nodo legge l'evento sul relay, lo decifra, verifica che l'autore sia autorizzato per questa sessione, esegue il pagamento e restituisce una risposta criptata (successo con preimmagine o errore). Il relay agisce solo come intermediario di trasporto: non può leggere il contenuto, ma può osservare i tempi e la frequenza delle richieste.



Rispetto a una connessione tramite Tailscale o Tor, il vantaggio principale di NWC è che il tuo nodo non è direttamente raggiungibile dall'esterno. Questo semplifica notevolmente l'uso mobile: il tuo nodo non ha bisogno di accettare connessioni in entrata, deve solo essere in grado di comunicare con un relay. D'altra parte, si introduce una dipendenza funzionale dai relay Nostr: se non sono disponibili, l'esperienza degrada. Inoltre, anche se i messaggi sono criptati, il relay può osservare un certo livello di metadati sull'attività.



Anche la differenza nei modelli di sicurezza è importante. Con Tailscale o Tor, si espone l'accesso diretto al proprio nodo (tramite API o LND) protetto da segreti altamente sensibili. Questo è potente, perché si può amministrare tutto, ma è anche una superficie di attacco di livello inferiore. Con NWC, l'accesso è più applicativo: si delega una sessione token che autorizza solo determinate azioni.



### Installare Alby Hub sul nodo Lightning



In precedenza, nell'App Store Umbrel era presente un'applicazione specificamente dedicata alle connessioni NWC, ma purtroppo non è più disponibile. Ora è necessario utilizzare Alby Hub per stabilire questo tipo di connessione. A tal fine, è necessario installare l'applicazione Alby Hub direttamente dal negozio.



![Image](assets/fr/091.webp)



All'apertura, saltare le schermate introduttive, quindi fare clic sul pulsante `Get Started (LND)`. È importante controllare che tra parentesi ci sia scritto `LND` e non `LDK`. Se appare `LND`, significa che Alby Hub ha rilevato correttamente il nodo Lightning esistente e si configurerà come interfaccia per esso. Se invece appare `LDK`, significa che Alby Hub non ha rilevato il tuo nodo e sta per crearne uno nuovo, che non è il nostro scopo.



![Image](assets/fr/092.webp)



Verrà quindi richiesto di creare un account Alby. Per l'uso limitato a NWC, questo non è necessario, ma potreste volerlo fare se desiderate usufruire dei servizi specifici di Alby. In caso contrario, fare clic su "Forse più tardi" per continuare.



![Image](assets/fr/093.webp)



Scegliere quindi una password forte e unica. Questa proteggerà l'accesso a Alby Hub sul tuo nodo. Ricordatevi di salvarla nel tuo gestore di password.



![Image](assets/fr/094.webp)



Si accede così all'interfaccia di Alby Hub. Non è necessario eseguire l'intero processo di configurazione, a meno che non lo si voglia usare come gestore principale del nodo Lightning. Come abbiamo visto in precedenza, Alby Hub può infatti sostituire l'uso di ThunderHub per l'amministrazione del nodo. Se volete saperne di più sulle opzioni di Alby Hub, date un'occhiata al nostro tutorial dedicato:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Andare al menu "Collegamenti".



![Image](assets/fr/095.webp)



Qui si possono vedere tutte le applicazioni che possono connettersi al nodo Lightning tramite NWC. Tra queste c'è Zeus, già menzionato nel capitolo precedente. Qui useremo Alby Go. Fare clic su Alby Go, quindi sul pulsante `Connetti a Alby Go` per avviare il processo di connessione.



![Image](assets/fr/096.webp)



### Installazione e collegamento del Alby Go



Sullo smartphone, installare l'applicazione Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



In Alby Hub, configurare i diritti che si desidera concedere all'applicazione Alby Go sul nodo Lightning. È possibile, ad esempio, impostare limiti di spesa per periodo, una data di scadenza per il collegamento NWC o lasciare il controllo totale. Una volta impostati i parametri, fare clic sul pulsante "Avanti".



![Image](assets/fr/097.webp)



Il Alby Hub invia un codice QR per stabilire la connessione NWC tra il tuo nodo Lightning e il Alby Go.



![Image](assets/fr/098.webp)



All'apertura dell'applicazione Alby Go, fare clic su "Connetti Wallet", quindi eseguire la scansione del codice QR fornito dal Alby Hub.



![Image](assets/fr/099.webp)



Scegliere un nome per identificare questo wallet. Ora si dispone di un accesso remoto al proprio nodo Lightning tramite Alby Go. È possibile ricevere le intece generate sul nodo sats o impostare le intece Lightning direttamente con esso.



![Image](assets/fr/100.webp)



Ad esempio, ho inviato 1543 sats dall'interfaccia Alby Go.



![Image](assets/fr/101.webp)



Se vado all'interfaccia di base del mio nodo Lightning su Umbrel, posso vedere che questo pagamento è stato effettivamente effettuato dal mio nodo.



![Image](assets/fr/102.webp)



Ora sapete come utilizzare facilmente il tuo nodo Lightning da qualsiasi luogo.



## Autonomia di lunga durata su Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Siamo giunti alla fine di questo corso pratico su LNP202. Ora avete le basi necessarie per utilizzare Lightning Network in modo sovrano: avete capito il vero ruolo di un nodo, i compromessi tra i diversi approcci e avete configurato un'istanza LND su Umbrel con una strategia di backup e protezione coerente. Avete anche aperto i tuoi primi canali, imparato a gestire la liquidità e a rendere affidabili i tuoi pagamenti su base giornaliera.



Da un punto di vista operativo, il tuo nodo dovrebbe ora entrare in un ritmo di manutenzione. La cosa principale è monitorarlo (uptime, sincronizzazione, stato dei canali, fallimenti dei pagamenti, ecc.), applicare gli aggiornamenti offerti da Umbrel quando sono disponibili versioni stabili e controllare periodicamente che i backup e la configurazione della watchtower siano ancora attivi.



Per quanto riguarda i canali, adottate un approccio pragmatico: mantenete quelli che vi sono utili, chiudete quelli che sono permanentemente inattivi o associati a peer instabili e riallocate gradualmente il tuo capitale verso una topologia più robusta.



**Una delle insidie più comuni in questa fase è quella di destinare troppo capitale al tuo nodo Lightning. Tenete presente che il tuo nodo Lightning è molto meno sicuro di un wallet hardware e che la disponibilità dei fondi impegnati nei tuoi canali si basa su meccanismi di backup che rimangono imperfetti. È quindi molto importante mantenere importi ragionevoli, che potete permettervi di perdere in caso di problemi, e mantenere sempre la maggior parte del tuo sats su un wallet hardware onchain.



Per quanto riguarda gli strumenti, vi consiglio di rimanere curiosi e attenti ai nuovi sviluppi. In questa sessione di formazione ne abbiamo scoperti diversi, sia per la gestione del nodo, sia per la sua connettività o per l'utilizzo in remoto per effettuare pagamenti. Tuttavia, Lightning è un campo particolarmente dinamico. Ogni anno emergono nuovi e importanti strumenti e molte nuove applicazioni appaiono anche su Umbrel. Tenersi aggiornati su questi nuovi sviluppi può consentire di scoprire soluzioni più potenti o più pratiche di quelle presentate in questo corso.



Sul fronte della formazione, se non l'avete ancora fatto, vi consiglio vivamente di seguire il corso teorico LNP 201 di Fanis Michalakis, dedicato al funzionamento del Lightning Network. Vi aiuterà a comprendere meglio le manipolazioni eseguite in questo corso LNP202 e vi darà maggiore sicurezza nella gestione quotidiana del tuo nodo.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

In un'ottica diversa, ma altrettanto essenziale per il tuo viaggio in bitcoin, vi consiglio anche l'eccellente corso di Ludovic Lars sulla storia della creazione del Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Ma prima di andare avanti, potete scrivere una recensione di questo corso LNP202 e, naturalmente, prendere il diploma per confermare che avete compreso tutti i suoi contenuti.



# Parte finale


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Recensioni e valutazioni


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Esame finale


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusione


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>
