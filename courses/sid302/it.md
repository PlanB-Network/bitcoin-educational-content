---
name: Liquid Bootcamp Essentials
goal: Acquisire una comprensione completa del progetto Liquid Network e Elements e imparare a implementare soluzioni avanzate in materia di transazioni riservate, tokenizzazione e architettura di rete decentralizzata.
objectives: 

  - Comprendere i fondamenti dell'architettura Liquid e la sua relazione con Bitcoin.
  - Imparare a configurare e gestire i nodi Liquid utilizzando il software Elements.
  - Esplorare l'uso di transazioni riservate e l'emissione di attività sul Liquid Network.
  - Cogliere gli aspetti commerciali e tecnici del Liquid per le applicazioni nei mercati dei capitali.

---

# Introduzione alla rete Liquid


Intraprendete un viaggio formativo progettato per fornire una comprensione approfondita del progetto Liquid Network e Elements. Questo bootcamp combina teoria e pratica per insegnare i fondamenti tecnici, architetturali e commerciali necessari per implementare e sfruttare le funzionalità del Liquid. Dalle transazioni riservate alla progettazione dell'ecosistema, questo corso è ideale per coloro che desiderano ampliare la propria conoscenza degli strumenti avanzati all'interno dell'ecosistema Bitcoin.


Con presentazioni di esperti del settore, il corso copre argomenti come l'architettura Liquid, le applicazioni di tokenizzazione, i concetti tecnici di Elements e casi d'uso innovativi come l'SDK Breez. Progettato per essere accessibile a principianti e utenti intermedi, il corso offre valore anche agli sviluppatori esperti che cercano di padroneggiare Liquid come piattaforma per ottimizzare i loro progetti.

+++

# Introduzione


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Panoramica del corso


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Benvenuti al Liquid Bootcamp, un corso di formazione completo progettato per fornirvi le conoscenze e le competenze necessarie per sfruttare efficacemente il progetto Liquid Network e Elements. Questo corso offre un'esplorazione completa delle caratteristiche distintive del Liquid, tra cui il Confidential Transactions, l'emissione di asset e la sua architettura di rete federata, introducendo anche i concetti fondamentali del Elements, il software che alimenta il Liquid.


Nel corso del boot camp, esplorerete le applicazioni pratiche del Liquid Network, dalla configurazione e gestione dei nodi alla comprensione del suo utilizzo nei mercati dei capitali e nella tokenizzazione del Bitcoin. Grazie alle presentazioni di esperti del settore, si approfondiranno anche argomenti avanzati come gli HTLC, l'SDK Breez e il progetto Blockstream AMP.


Questo bootcamp è stato originariamente condotto come evento di persona, seguendo un programma strutturato (come mostrato nell'immagine) progettato per le sessioni dal vivo. Tuttavia, per questo adattamento del corso, i contenuti sono stati riorganizzati per adattarsi meglio al formato online e facilitare la comprensione da parte degli studenti. Il nuovo ordine assicura una progressione logica dai concetti fondamentali agli argomenti più avanzati e tecnici, massimizzando così l'esperienza di apprendimento.


Questo percorso è strutturato in modo da accogliere partecipanti con diversi livelli di competenza, offrendo un mix di conoscenze teoriche ed esperienza pratica. Alla fine di questo boot camp, avrete una solida comprensione dell'architettura di Liquid, della sua integrazione con Bitcoin e di come utilizzare le sue caratteristiche innovative per costruire e ottimizzare soluzioni finanziarie.


Immergetevi nel mondo della sidechain Liquid e liberate subito tutto il suo potenziale!

# Fondamenti


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Architettura Liquid


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Architettura Liquid Network e modello di consenso


Il Liquid Network è una sidechain federata costruita sulla base di codice del Elements, progettata per estendere le capacità del Bitcoin pur basandosi sulla sua sicurezza fondamentale. A differenza del [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work) del Bitcoin, il Liquid opera su un modello di [consenso](https://planb.academy/resources/glossary/consensus) federato. La rete è gestita da un gruppo di membri distribuiti a livello globale, tra cui borse, trading desk e fornitori di infrastrutture. Da questi membri vengono selezionati quindici "funzionari" che agiscono come firmatari dei [blocchi](https://planb.academy/resources/glossary/block).


Questi funzionari producono blocchi in modo deterministico, con un nuovo blocco generato ogni minuto. Questa precisa tempistica è in contrasto con gli intervalli probabilistici di dieci minuti del Bitcoin. Per essere valido, un blocco deve essere firmato da almeno 11 dei 15 funzionari (una soglia di due terzi più uno). Questo meccanismo conferisce al Liquid la "finzionalità di due blocchi", ovvero una volta che una [transazione](https://planb.academy/resources/glossary/transaction-tx) ha due conferme (circa due minuti), è matematicamente impossibile riorganizzare la catena. Questa velocità e certezza sono fondamentali per l'arbitraggio, il trading automatizzato e il regolamento rapido tra le borse.


La federazione è dinamica. Grazie al protocollo Dynamic Federation (Dynafed), la rete può ruotare i funzionari o aggiornare i parametri senza richiedere un [fork](https://planb.academy/resources/glossary/fork). Ciò consente al sistema di evolversi e di sostituire l'hardware o i membri senza problemi, mantenendo il funzionamento continuo. Ciò consente al sistema di evolversi e di sostituire l'hardware o i membri senza soluzione di continuità, mantenendo il funzionamento continuo.


### Confidential Transactions e gestione delle risorse


Una caratteristica distintiva del Liquid è il suo supporto nativo per il Confidential Transactions (CT) e per le attività multiple. Nella catena principale Bitcoin, tutti i dettagli delle transazioni - mittente, destinatario e importo - sono pubblici. Nel Liquid, il CT utilizza impegni crittografici per nascondere il tipo di asset e l'importo dal libro mastro pubblico, consentendo comunque alla rete di verificare che la transazione sia valida (cioè che non si sia verificata un'[inflazione](https://planb.academy/resources/glossary/inflation)). Solo i partecipanti in possesso delle chiavi di criptazione possono visualizzare i valori specifici, offrendo un livello di privacy commerciale essenziale per le istituzioni che movimentano grandi posizioni.


Liquid tratta tutti gli asset come cittadini "nativi" della [blockchain](https://planb.academy/resources/glossary/blockchain). Ciò include Liquid Bitcoin (LBTC), monete stabili come USDT e token di sicurezza. L'emissione di un asset non richiede complessi contratti intelligenti; è una funzione di base del protocollo.


#### Attività regolamentate e AMP

Per gli asset che richiedono conformità, come i token di sicurezza, Liquid impiega la Blockstream Asset Management Platform (AMP). Questa introduce un livello autorizzato in cui le transazioni richiedono una seconda firma da parte di un server di autorizzazione. Ciò consente agli emittenti di applicare regole, come Whitelisting o requisiti KYC, a livello granulare, combinando l'efficienza di una blockchain con i controlli normativi della finanza tradizionale.


### L'infrastruttura bidirezionale di Peg e sicurezza


La connessione tra il Liquid e il Bitcoin è mantenuta attraverso un peg bidirezionale. Per effettuare il "peg-in", l'utente invia il Bitcoin a un indirizzo generato sul mainchain. Questi fondi sono bloccati per 102 conferme (circa 17 ore) per eliminare i rischi di riorganizzazione. Una volta confermati, una quantità equivalente di LBTC viene coniata sulla sidechain Liquid.


Il processo di "peg-out" permette agli utenti di riscattare LBTC per Bitcoin. Ciò richiede la combustione di LBTC e un'autorizzazione crittografica da parte della federazione. Per prevenire i furti, i peg-out sono strettamente controllati dalle Peg-out Authorization Keys (PAK) detenute dai membri della federazione. Inoltre, i fondi possono essere scambiati istantaneamente tramite fornitori di terze parti come SideSwap, aggirando il ritardo del regolamento per una liquidità più rapida.


#### Moduli di sicurezza hardware (HSM)

La sicurezza viene applicata rigorosamente attraverso l'hardware. I funzionari non conservano le [chiavi private](https://planb.academy/resources/glossary/private-key) sui server standard, ma utilizzano i moduli di sicurezza hardware (HSM). Questi dispositivi sono separati dalla logica del server host e sono programmati con regole rigorose. Ad esempio, un HSM si rifiuta di firmare un blocco se la sua altezza non è superiore a quella del blocco precedente, impedendo la riscrittura della cronologia. Questo modello di sicurezza "adversariale" presuppone che il server host possa essere compromesso, garantendo che le chiavi rimangano sicure anche in caso di violazione del luogo fisico.


## Fondamenti del Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Le fondamenta del Liquid


Elements è una piattaforma blockchain open-source derivata dalla base di codice Bitcoin Core. Estende le funzionalità di Bitcoin consentendo alle blockchain indipendenti dalle sidechain di trasferire beni da e verso Bitcoin. Mentre Bitcoin Core alimenta la rete Bitcoin, Elements è il motore software dietro Liquid Network e altre sidechain personalizzate.


La relazione è semplice: Liquid è una specifica "istanza" di una sidechain Elements, configurata per l'uso in produzione con un modello di consenso federato. Gli sviluppatori che hanno familiarità con Bitcoin troveranno Elements intuitivo, poiché mantiene la stessa interfaccia RPC (Remote Procedure Call) e la stessa struttura della riga di comando (`elements-cli`, `elements-d`, `elements-qt`). La differenza fondamentale sta nella configurazione: impostando `chain=liquidv1` si connette un [nodo](https://planb.academy/resources/glossary/node) alla rete principale Liquid , mentre `chain=elementsregtest` crea un ambiente locale di test di regressione in cui gli sviluppatori possono eseguire blocchi generate istantaneamente e testare senza dipendenze esterne.


#### Emissione di attività

Una caratteristica distintiva di Elements è l'emissione nativa di asset. A differenza di Ethereum, dove i token sono complessi contratti intelligenti, gli asset in Elements sono cittadini di prima classe creati tramite un semplice comando RPC (`issueasset`).


- Identificatori univoci:** Ogni risorsa riceve un ID esadecimale unico di 64 caratteri.
- Gettoni di riemissione:** Gli emittenti possono creare facoltativamente gettoni di riemissione, che garantiscono al possessore il diritto di coniarne altri in un secondo momento (utili per le stablecoin o i gettoni di sicurezza).
- Registro degli asset:** Poiché gli ID esadecimali non sono leggibili dall'uomo, il registro degli asset di Blockstream mappa questi ID in nomi e ticker (ad esempio, "USDT"), in modo simile a un DNS per gli asset.


### Privacy via Confidential Transactions


Il Elements affronta uno dei limiti principali delle blockchain pubbliche: la mancanza di privacy commerciale. Su Bitcoin, l'importo di ogni transazione è visibile al mondo. Il Elements introduce il **Confidential Transactions (CT)**, che criptografa l'importo e il tipo di attività, consentendo comunque alla rete di verificare la validità della transazione.


Ciò si ottiene utilizzando gli **impegni di Pedersen** e le **prove di intervallo**.


- Gli impegni Pedersen** sostituiscono l'importo visibile con un impegno crittografico. Grazie alla crittografia omomorfa, i validatori possono verificare che *Impegni di ingresso = Impegni di uscita + Commissioni* senza mai vedere i valori reali.
- Le prove di intervallo** impediscono all'utente di creare denaro dal nulla (ad esempio, utilizzando numeri negativi) dimostrando matematicamente che il valore nascosto è un numero intero positivo all'interno di un intervallo valido.


Per un osservatore esterno, una transazione confidenziale mostra input e output validi, ma nasconde *cosa* viene inviato e *quanto*. Solo il mittente e il destinatario (che possiedono le chiavi di cecità) possono vedere i dati in chiaro.


### Sviluppo e flusso di lavoro RPC


L'interazione con un nodo Elements avviene principalmente attraverso la sua interfaccia JSON-RPC. Ciò consente alle applicazioni scritte in Python, JavaScript o Go di comunicare con la blockchain.



- Configurazione:** Uno sviluppatore inizia in genere in modalità `regtest`. Ciò consente la generazione istantanea di blocchi (`generateblock`) per confermare immediatamente le transazioni, aggirando il tempo di blocco di 1 minuto della rete live.
- Comandi:** Sono disponibili comandi standard del Bitcoin come `getblockchaininfo`, oltre a comandi specifici del Elements come `dumpblindingkey` (per verificare i CT) o `pegin` (per spostare BTC nella sidechain).
- Alias:** Per gestire più nodi (ad esempio, un "mittente" e un "ricevitore" per i test), gli sviluppatori spesso usano alias di shell come `e1-cli` e `e2-cli` che puntano a diverse directory di dati, simulando una rete [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) su una singola macchina.


Questa architettura consente agli sviluppatori di creare applicazioni finanziarie sofisticate, come piattaforme di titoli o gateway di pagamento privati, utilizzando gli strumenti solidi e familiari dell'ecosistema Bitcoin.


## Collegamento degli strati del Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infrastruttura Cross-Layer e HTLC


L'ecosistema Bitcoin si è evoluto in un'architettura a più livelli, con la Mainchain che fornisce il regolamento, Lightning che offre velocità e Liquid che abilita funzionalità avanzate per gli asset. Lo spostamento del valore tra questi livelli senza intermediari centralizzati richiede una primitiva crittografica senza fiducia: il [Hash](https://planb.academy/resources/glossary/hash-function) Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


Un HTLC crea un [canale di pagamento](https://planb.academy/resources/glossary/payment-channel) condizionato che collega atomicamente sistemi indipendenti. Funziona attraverso due vincoli primari: un **hash lock** e un **time lock**.


- Il Hash Lock:** I fondi possono essere spesi immediatamente se il destinatario rivela una "preimmagine" segreta che corrisponde a uno specifico hash crittografico.
- Il blocco temporale:** Se il destinatario non rivela il segreto entro un determinato lasso di tempo (altezza del blocco), il mittente originale può reclamare i fondi.


Questa struttura a doppio percorso garantisce la sicurezza. In un cross-layer swap, lo stesso blocco hash viene utilizzato su entrambe le reti. Quando il destinatario rivela il segreto per richiedere fondi su un livello (ad esempio, Liquid), quel segreto diventa visibile al mittente, che può quindi usarlo per richiedere i fondi reciproci sull'altro livello (ad esempio, Lightning). Questo vincolo crittografico garantisce che lo scambio si concluda con successo per entrambe le parti o che fallisca per entrambe, eliminando il rischio che una parte perda fondi mentre l'altra ne guadagna.


### Aggiornamento del Taproot e del MuSig2


Le HTLC tradizionali ([SegWit](https://planb.academy/resources/glossary/segwit) v0) funzionavano bene, ma soffrivano di inconvenienti legati alla privacy e all'efficienza. Richiedevano la pubblicazione dell'intera logica di [script](https://planb.academy/resources/glossary/script) on-chain, rendendo le transazioni di swap facilmente identificabili dagli analisti della blockchain e più costose a causa delle dimensioni dei dati. L'introduzione di [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) e del protocollo MuSig2 ha rivoluzionato questa architettura.


Taproot consente l'aggregazione delle chiavi tramite MuSig2. Invece di rivelare uno script complesso con più [chiavi pubbliche](https://planb.academy/resources/glossary/public-key), MuSig2 consente ai partecipanti allo swap di combinare le proprie chiavi in un'unica chiave pubblica aggregata.


- Percorso cooperativo: ** Se entrambe le parti sono d'accordo con lo scambio (il "percorso felice"), co-firmano la transazione. Per la rete, questa transazione è identica a un pagamento standard a firma singola. Il consumo di spazio è minimo e non rivela alcuna informazione sulle condizioni dello scambio.
- Se una delle parti non risponde o è malintenzionata, lo script sottostante (contenente i blocchi hash/tempo) viene rivelato solo in quel momento. Questo è organizzato in un albero di [Merkle](https://planb.academy/resources/glossary/merkle-tree), che consente alla parte onesta di rivelare solo il ramo specifico necessario per recuperare i fondi, tenendo nascosto il resto della logica del contratto.


### Attuazione pratica: Scambi Liquid-Lightning


In pratica, questi protocolli consentono un interscambio senza soluzione di continuità tra i livelli del Bitcoin. Un tipico scambio da Liquid a Lightning inizia con una richiesta di scambio da parte di un cliente a un fornitore di servizi. Il cliente fornisce una [fattura Lightning](https://planb.academy/resources/glossary/invoice-lightning) e il fornitore blocca l'equivalente Liquid Bitcoin (L-BTC) in un indirizzo HTLC abilitato per Taproot.


L'atomicità viene applicata quando il pagamento viene regolato. Per richiedere il L-BTC, il fornitore di servizi deve avere la preimmagine. Ottiene questa preimmagine solo quando paga con successo la fattura Lightning del cliente. Nel momento in cui il pagamento Lightning viene finalizzato, la preimmagine viene rivelata, consentendo al fornitore di sbloccare i fondi Liquid.


#### Astrazione Wallet e gestione UTXO

Per gli utenti finali, questa complessità è completamente astratta. I portafogli moderni come Aqua gestiscono in background i processi di generazione delle chiavi, creazione delle fatture e firma. L'utente deve semplicemente "pagare" una fattura Lightning utilizzando il proprio saldo Liquid. Dietro le quinte, il servizio gestisce il consolidamento di [UTXO](https://planb.academy/resources/glossary/utxo), spazzando periodicamente le uscite piccole, non reclamate o rimborsate per mantenere l'efficienza di [wallet](https://planb.academy/resources/glossary/wallet) e ridurre al minimo l'impatto delle commissioni nei periodi di traffico elevato.


## Panoramica del Liquid Network


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Architettura e consenso


Il Liquid Network opera come una sidechain federata costruita sulla base di codice del **Elements**. Mentre il Elements - un fork del Bitcoin Core - fornisce la base software, il Liquid è l'implementazione della rete di produzione. A differenza del Bitcoin, che si basa sul [mining](https://planb.academy/resources/glossary/mining), il Liquid utilizza un modello di **consenso federato**.


La rete è gestita da quindici "funzionari" distribuiti a livello globale Queste entità gestiscono server specializzati che svolgono due ruoli fondamentali:

1.  **Produzione di blocchi:** I funzionari creano a turno i blocchi in un programma deterministico di round-robin, generando un nuovo blocco esattamente ogni minuto.

2.  **Firma dei blocchi:** Perché un blocco sia valido, deve essere firmato da almeno 11 dei 15 funzionari.


Questa soglia di 11 su 15 garantisce che la rete possa tollerare il guasto di un massimo di quattro nodi senza arrestarsi. Il vantaggio principale di questo compromesso è la **finalità deterministica**. Mentre Bitcoin si basa sulle probabilità, Liquid raggiunge la certezza del regolamento dopo due blocchi (circa due minuti). Una volta che un blocco ha una singola conferma sopra di esso, la catena non può essere riorganizzata, rendendola altamente efficace per l'arbitraggio e la liquidazione rapida.


### Confidential Transactions e risorse native


La caratteristica distintiva del Liquid è l'uso predefinito del **Confidential Transactions (CT)**. Nel Bitcoin mainchain, il mittente, il destinatario e l'importo sono pubblici. Il Liquid migliora questo aspetto, oscurando crittograficamente l'importo e il tipo di attività, mentre lascia gli indirizzi del mittente e del destinatario visibili per la verifica.


Per garantire che un utente non possa stampare denaro (ad esempio, inviando importi negativi), Liquid impiega i **Pedersen Commitments** e le **Range Proofs**. Queste primitive crittografiche consentono alla rete di verificare che *Inputs = Outputs + Fees* e che tutti i valori sono numeri interi positivi, senza mai rivelare i numeri specifici al libro mastro pubblico. Solo i partecipanti in possesso delle chiavi di criptazione possono vedere i dati decriptati.


#### Emissione di attività

Liquid tratta tutti gli asset come "nativi" Che si tratti di Liquid Bitcoin (L-BTC), di una stablecoin come USDT o di un titolo token, tutti condividono la stessa architettura. L'emissione di un asset non richiede contratti intelligenti, ma solo una semplice chiamata RPC.


- Attività non regolamentate:** Possono essere emesse senza autorizzazione da chiunque.
- Attività regolamentate:** Utilizzando la Blockstream Asset Management Platform (AMP), gli emittenti possono applicare le regole di conformità (come KYC/AML) richiedendo una seconda firma da un server di autorizzazione prima che un'attività possa essere spostata.


### Il piolo bidirezionale e la Federazione dinamica


Il ponte tra Bitcoin e Liquid è il **Peg a due vie**. Consente agli utenti di spostare BTC sulla catena laterale (Peg-in) e di tornare al mainchain (Peg-out).


**Il processo Peg-in

Si tratta di un sistema senza permessi. Un utente invia BTC a un indirizzo controllato dalla federazione. Per proteggersi dalle riorganizzazioni della blockchain Bitcoin, questi fondi devono attendere **102 conferme** (circa 17 ore) prima che l'equivalente L-BTC venga coniato sulla sidechain.


**Il processo di uscita del piolo:**

Per tornare al Bitcoin, si bruciano L-BTC. Tuttavia, per evitare il furto delle riserve Bitcoin sottostanti, le uscite dal peg non sono completamente automatizzate. Richiedono l'autorizzazione di un membro in possesso di una **Peg-Out Authorization Key (PAK)**. I fondi Bitcoin stessi sono protetti in un wallet a 11 di 15 firme multiple, con chiavi conservate in moduli di sicurezza hardware (HSM) che sono collegati in air-gapping ai server principali dei funzionari.


**Federazione Dinamica (Dynafed):**

Per garantire la longevità, il Liquid impiega Dynafed, un protocollo che consente alla rete di ruotare i funzionari o aggiornare i parametri senza che il fork sia costretto a farlo. Se un funzionario deve essere sostituito, la rete trasmette una transazione di transizione. Dopo un periodo di sovrapposizione di due settimane, la nuova configurazione prende il sopravvento, consentendo alla federazione di evolversi senza soluzione di continuità, mantenendo un uptime continuo.


## Ecosistema e mercati dei capitali


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Strategia aziendale ed ecosistema


Liquid è più di una sidechain tecnica; è un livello infrastrutturale focalizzato sul business, progettato per gestire i complessi requisiti dei mercati dei capitali che Bitcoin mainchain non possono supportare in modo efficiente. Mentre la [Lightning Network](https://planb.academy/resources/glossary/lightning-network) è ottimizzata per i pagamenti ad alta frequenza e di basso valore, la Liquid si rivolge ai trasferimenti di alto valore, all'emissione di asset e al regolamento interscambio.


L'ecosistema è guidato dalla **Federazione Liquid**, un consorzio di circa 73 aziende tra cui borse, trading desk e fornitori di infrastrutture. Questo modello collaborativo rispecchia le tradizionali stanze di compensazione finanziaria, ma opera con una maggiore trasparenza e tempi di regolamento significativamente ridotti (2 minuti contro T+2 giorni).


### La gettonizzazione delle attività del mondo reale (RWA)


Il core business case di Liquid è la "Tokenization", ovvero la rappresentazione del valore del mondo reale (azioni, obbligazioni, contratti mining) come token digitali sulla blockchain. Questo offre tre vantaggi principali:

1.  **Mercati globali 24/7:** Eliminazione degli orari bancari e delle restrizioni geografiche.

2.  **Efficienza operativa: ** Eliminazione degli errori di riconciliazione grazie a un libro mastro condiviso e immutabile.

3.  **Regolamento atomico:** Ridurre il rischio di controparte garantendo che la consegna avvenga contemporaneamente al pagamento.


#### Attività regolamentate e AMP

La maggior parte delle attività istituzionali non può essere scambiata senza permesso a causa di requisiti legali. La **Piattaforma di gestione degli asset (AMP)** è lo standard tecnico che fa rispettare queste regole.


- Whitelisting:** Gli emittenti possono limitare la detenzione e la negoziazione agli indirizzi verificati da KYC.
- Controllo Multisig:** Le azioni di conformità (come il congelamento dei fondi rubati o la riemissione dei token persi) sono gestite tramite autorizzazione a più firme, garantendo che nessun singolo dipendente possa agire unilateralmente.


Questa infrastruttura è attiva oggi. Piattaforme come **Stalker** forniscono servizi di tokenizzazione end-to-end in Europa, mentre **Sideswap** funge da borsa decentralizzata e non custodiale wallet, consentendo la negoziazione peer-to-peer di attività come la **Blockstream Mining Note (BMN)** e le azioni MicroStrategy tokenizzate (CMSTR).


### Successo nel mondo reale: Lo studio del caso Mayfell


La prova più convincente dell'utilità del Liquid viene da **Mayfell** in Messico. In un mercato in cui il finanziamento tradizionale si basa su cambiali cartacee, soggette a perdite, frodi e lentezza di elaborazione, Mayfell ha trasferito l'intera infrastruttura al Liquid.



- Scala:** Più di 25.000 cambiali emesse, per un valore di **1,5 miliardi di dollari+**.
- Privacy:** Utilizzando il Liquid del Confidential Transactions, gli importi dei prestiti sono visibili solo al prestatore e al mutuatario, preservando la privacy commerciale e consentendo ai revisori di verificare l'integrità del libro mastro.
- Impatto:** Collegando i prestatori non bancari ai mercati globali dei capitali tramite blockchain, Mayfell ha ridotto i costi e ampliato l'accesso al credito per le PMI messicane, dimostrando che la proposta di valore di Liquid va ben oltre il trading speculativo.


### Posizionamento strategico rispetto ad altre catene


Liquid compete in un mercato affollato di piattaforme di tokenizzazione (Ethereum, Solana, ecc.), ma possiede vantaggi strategici distinti:


- Chiarezza normativa:** Liquid utilizza Bitcoin (L-BTC) come asset nativo. Non ha un token pre-minato o una ICO, evitando i rischi di "titolo non registrato" che affliggono altre blockchain L1.
- Stabilità:** A differenza del modello di conto di Ethereum, in cui le transazioni non andate a buon fine bruciano comunque le tariffe del gas, il modello Liquid di UTXO è deterministico e affidabile per i dati finanziari mission-critical.
- Privacy:** La riservatezza di default è un requisito per la maggior parte delle istituzioni finanziarie, una caratteristica che Liquid offre in modo nativo e che le catene pubbliche faticano a implementare senza complessi componenti aggiuntivi.


Per gli sviluppatori, questo ecosistema offre una chiara opportunità: costruire gli strumenti (dashboard, portafogli, integrazioni per la conformità) che collegano la finanza tradizionale con il livello di regolamento sicuro di Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Controllo delle attività autorizzate su Liquid


Blockstream AMP (Asset Management Platform) funge da strato infrastrutturale critico del Liquid Network, progettato specificamente per gli emittenti di titoli digitali regolamentati e di stablecoin. Mentre il Liquid fornisce un livello di base senza permessi con l'emissione di asset nativi, le entità regolamentate spesso richiedono una rigorosa supervisione e capacità di conformità. AMP colma questa lacuna introducendo un livello di controllo permissioned su asset specifici senza sacrificare i vantaggi di privacy del Liquid.


La proposta di valore principale della piattaforma si basa su due funzionalità principali: la visibilità completa dell'emittente e l'autorizzazione delle transazioni. A differenza degli asset Liquid standard, in cui gli importi e i tipi sono blinded noti a tutti tranne che ai partecipanti, gli asset AMP consentono all'emittente di mantenere una traccia di audit completamente unblinded. Questa trasparenza è essenziale per le relazioni normative e gli audit interni. Inoltre, AMP applica un modello di autorizzazione rigoroso attraverso un meccanismo di co-firma. Ogni trasferimento di un asset AMP richiede una firma da parte del server AMP. Ciò consente agli emittenti di applicare regole complesse, come il congelamento dei conti, la whitelist degli investitori accreditati o l'imposizione di limiti di trasferimento, agendo di fatto come un gatekeeper centralizzato all'interno di una rete decentralizzata.


#### Scambi operativi

Questa architettura introduce specifici compromessi. Il sistema si basa sulla disponibilità del server AMP; se il server funge da cofirmatario e va offline, la liquidità degli asset si blocca. Inoltre, pur mantenendo la privacy da utente a utente, gli investitori devono accettare che l'emittente abbia piena visibilità sulle loro partecipazioni. Questo modello è ideale per i token di sicurezza conformi, ma non è adatto alle [criptovalute](https://planb.academy/resources/glossary/cryptocurrency) resistenti alla censura.


### Evoluzione dell'architettura e percorsi di integrazione


L'ecosistema AMP sta attualmente passando dalla sua prima iterazione a un'architettura "Versione 2" più flessibile e interoperabile. Il sistema preesistente richiedeva agli emittenti di mantenere nodi Elements completamente sincronizzati e costringeva gli sviluppatori a fare grande affidamento sull'SDK monolitico Green . Pur essendo funzionale, ciò creava elevate barriere tecniche all'ingresso e limitava le possibilità di scelta del wallet.


L'architettura di nuova generazione semplifica radicalmente questi requisiti spostando la complessità sul server. In questo nuovo modello, il server AMP gestisce il lavoro pesante della costruzione della transazione, della selezione del UTXO e del calcolo delle commissioni. Presenta all'emittente una transazione Elements parzialmente firmata (PSET) che richiede semplicemente una firma. Questo approccio "smart server, dumb wallet" elimina la necessità per gli emittenti di gestire nodi completi e consente l'uso di portafogli hardware e di configurazioni standard a firma multipla per la gestione della tesoreria.


Per gli sviluppatori, questa evoluzione significa abbandonare gli SDK proprietari per passare ai descrittori standard e ai flussi di lavoro PSET. I portafogli possono ora registrare descrittori multi-firma con il server AMP per stabilire i diritti di autorizzazione. Questo allinea lo sviluppo di AMP agli standard Bitcoin e wallet, rendendo l'integrazione accessibile a qualsiasi applicazione in grado di gestire i formati PSBT/PSET. Gli sviluppatori che stanno costruendo oggi sono incoraggiati a utilizzare strumenti come il Liquid Wallet Kit (LWK), che supporta queste moderne architetture basate sui descrittori, assicurando che le loro applicazioni siano a prova di futuro per i nuovi standard AMP.


### L'ecosistema Liquid Wallet e la riservatezza


La costruzione di applicazioni su Liquid richiede la navigazione in uno stack più complesso rispetto allo sviluppo standard di Bitcoin, grazie a caratteristiche come le risorse native e Confidential Transactions. L'ecosistema è supportato da un'architettura a strati: librerie di basso livello come `secp256k1-zkp` gestiscono le primitive crittografiche, mentre toolkit di livello superiore gestiscono la logica wallet .


Storicamente, il Green Development Kit (GDK) forniva una soluzione completa ma rigida. L'alternativa moderna è il Liquid Wallet Kit (LWK), che offre un approccio modulare. LWK separa i problemi in crate distinte che gestiscono i descrittori, la firma e la comunicazione hardware in modo indipendente, offrendo agli sviluppatori la flessibilità di costruire soluzioni personalizzate senza l'overhead di una libreria monolitica.


#### Manipolazione Confidential Transactions

La sfida più importante in questo ecosistema è la gestione del ciclo di vita della crittografia. Nel Liquid, i risultati delle transazioni sono crittografati utilizzando lo scambio di chiavi Elliptic Curve Diffie-Hellman (ECDH). Il mittente utilizza la chiave pubblica del destinatario per criptare gli importi e i tipi di beni, generando una prova di portata che verifica la validità della transazione senza rivelare i valori.


Per funzionare, un wallet deve riuscire a invertire questo processo. Quando un wallet rileva una transazione in entrata, tenta di sbloccare l'uscita utilizzando la sua chiave di blocco privata. Se il segreto condiviso corrisponde, il wallet può decifrare il valore e aggiungerlo al saldo dell'utente. Questo processo è computazionalmente intenso e richiede una gestione precisa dei fattori di blocco per garantire che le transazioni siano matematicamente bilanciate, una complessità che strumenti come LWK mirano ad astrarre per lo sviluppatore.


# Tecnica


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## SDK Breez - Senza nodo


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Introduzione al Breez Liquid SDK


L'SDK Breez Liquid è un kit di strumenti open-source autocostruito progettato per colmare il divario tra il Liquid Network e l'ecosistema Bitcoin. La sua missione principale è quella di astrarre le complessità della gestione dei nodi Lightning Network e degli swap atomici, consentendo agli sviluppatori di creare applicazioni finanziarie senza attriti.


Costruita con una filosofia "mobile-first", la logica di base è scritta in Rust per garantire prestazioni e sicurezza, ma utilizza UniFFI (Unified Foreign Function Interface) per fornire binding nativi per Kotlin, Swift, Python, C#, Dart e Flutter. In questo modo gli sviluppatori possono integrare le funzionalità di Bitcoin nel loro ambiente preferito senza dover gestire operazioni crittografiche di basso livello.


**Tipi di transazione supportati:**

L'SDK opera con Liquid come "base" Eccelle in tre operazioni specifiche:

1.  **Da Liquid a Liquid:** Trasferimenti diretti on-chain.

2.  **Liquid-to-Lightning:** Pagamento delle fatture Lightning con fondi Liquid.

3.  **Da Liquid a Bitcoin:** scambio di fondi direttamente con il Bitcoin mainchain.


*Nota: l'SDK non supporta le transazioni dirette da Lightning a Lightning o da Bitcoin a Bitcoin. Si tratta di uno strumento strettamente incentrato su Liquid


### Architetture di pagamento: Swap sottomarini


Per ottenere l'interoperabilità tra Liquid, Lightning e Bitcoin senza custodi centralizzati, Breez si basa su **Submarine Swaps**. Si tratta di operazioni atomiche in cui una transazione viene completata con successo su entrambe le reti o fallisce su entrambe, garantendo che i fondi non vengano mai persi durante il transito.


#### Invio di fulmini (Scambio di sottomarini)

Quando un utente paga una fattura Lightning, l'SDK trasmette al Liquid Network una transazione di "blocco". In questo modo i fondi vengono effettivamente messi in deposito. Il fornitore di swap (Boltz) lo rileva, paga la fattura Lightning e poi utilizza la preimmagine del pagamento (la ricevuta crittografica) per richiedere i fondi bloccati al Liquid.


#### Ricezione del fulmine (scambio di sottomarini inverso)

La ricezione di Lightning è il processo inverso. L'utente genera una fattura e il fornitore di swap blocca i fondi su Lightning Network. L'SDK monitora questo processo tramite WebSocket. Una volta confermato il blocco, l'SDK esegue automaticamente una transazione di richiesta per spostare i fondi equivalenti nel Liquid wallet dell'utente.


#### Catena incrociata Bitcoin

Per i trasferimenti da Liquid a Bitcoin, l'architettura utilizza un meccanismo "dual-swap". Le transazioni di blocco avvengono contemporaneamente su entrambe le catene. Il mittente richiede i fondi sul Bitcoin, mentre il destinatario li richiede sul Liquid. Ciò consente un bridging senza fiducia, senza dover ricorrere a federated peg-out o a scambi centralizzati.


### Sviluppatore Interface e gestione automatizzata


L'SDK Breez semplifica l'esperienza degli sviluppatori condensando i complessi flussi finanziari in un processo standardizzato in tre fasi: **Connetti, prepara ed esegui**.


1.  **Connect:** Inizializza il wallet, si sincronizza con la blockchain utilizzando il Liquid Wallet Kit (LWK) e stabilisce connessioni WebSocket per il monitoraggio in tempo reale.

2.  **Preparazione:** Prima di impegnare i fondi, questa fase calcola e restituisce tutte le commissioni di rete e i costi di swap associati, consentendo all'interfaccia utente di presentare un totale chiaro all'utente.

3.  **Eseguire:** Questa fase costruisce la transazione, la trasmette e avvia lo swap.


#### Meccanismi di sicurezza automatizzati

Una delle caratteristiche più importanti dell'SDK è la **Gestione automatizzata dei rimborsi**. In caso di guasto della rete o di una controparte non collaborativa, i fondi potrebbero teoricamente rimanere bloccati in un contratto a tempo. L'SDK astrae completamente la logica di recupero. Monitora lo stato di ogni swap; se uno swap fallisce o va in time out, l'SDK costruisce e trasmette automaticamente la transazione di rimborso per restituire i fondi al wallet dell'utente.


Inoltre, l'SDK gestisce la **Risoluzione dei metadati**. Unisce i dati di swap off-chain (forniti dallo swapper Boltz) con la storia delle transazioni on-chain. In questo modo si garantisce che la cronologia delle transazioni dell'utente sia leggibile, mostrando i dettagli della fattura e il contesto del pagamento piuttosto che i semplici hash esadecimali delle transazioni.


# Sezione finale


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Recensioni e valutazioni


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Esame finale


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusione


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>