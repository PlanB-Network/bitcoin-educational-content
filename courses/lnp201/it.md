---
name: Teoria del Lightning Network
goal: Scoprire Lightning Network da una prospettiva tecnica
objectives:
- Comprendere il funzionamento dei canali di pagamento.
- Prendere confidenza con i termini HTLC, LNURL e UTXO.
- Gestire la liquidità e le fee di LN.
- Identificare Lightning Network come una rete.
- Scoprire gli usi teorici di Lightning Network.
---

# Un Viaggio nel Layer 2 di Bitcoin

Immergiti nel cuore di Lightning Network, un sistema essenziale per il futuro delle transazioni Bitcoin. LNP201 è un corso sulla teoria del funzionamento tecnico di Lightning. Rivela le fondamenta e i meccanismi di questo Layer 2 (rete di secondo livello), progettata per rendere i pagamenti Bitcoin veloci, economici e scalabili.

Grazie alla sua rete di canali di pagamento, Lightning Network consente transazioni rapide e sicure senza registrare ogni scambio sulla blockchain di Bitcoin. Nei vari capitoli imparerai come funzionano l'apertura dei canali, la loro gestione e chiusura, come i pagamenti vengono instradati attraverso nodi lungo la rete in modo sicuro, minimizzando la necessità di fiducia e come gestire la liquidità. Scoprirai cosa sono le [commitment transaction](https://planb.academy/resources/glossary/commitment-transaction), gli HTLC, le revocation keys (chiavi di revoca), i meccanismi di punizione, l'instradamento (routing) onion e le invoice (richieste di pagamento).

Che tu sia un principiante in ambito Bitcoin o un utente più esperto, questo corso ti fornirà informazioni preziose per comprendere e utilizzare Lightning Network. Nelle prime parti del corso tratteremo alcuni fondamenti del funzionamento di Bitcoin, perché è essenziale padroneggiare le basi dell'invenzione di Satoshi prima di immergersi in LNP201.

Buona scoperta!

+++

# Introduzione
<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>

## Panoramica del corso
<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>

Benvenuto al corso LNP201!

Questo corso mira a fornirti una comprensione tecnica approfondita di Lightning Network, un layer 2 progettato per facilitare transazioni Bitcoin rapide e spesso a basso costo. Scoprirai progressivamente i concetti fondamentali che regolano questo sistema, dall'apertura dei canali di pagamento fino alle tecniche di instradamento e gestione della liquidità.

**Sezione 1: Principi fondamentali**  
Inizieremo con un'introduzione generale a Lightning Network, stabilendo le basi essenziali di Bitcoin che devi sapere, i suoi indirizzi, gli UTXO e il funzionamento delle transazioni. Questo ripasso delle basi è essenziale per comprendere come Lightning Network si basi sui meccanismi della blockchain principale per funzionare in modo sicuro.

**Sezione 2: Apertura e chiusura dei canali**  
In questa sezione esploreremo il processo di apertura dei canali, che sono il pilastro di Lightning Network. Imparerai come vengono create le commitment transaction, il ruolo che le revocation keys svolgono per la sicurezza e come i canali possono essere chiusi in modo collaborativo o unilaterale. Ogni passaggio sarà spiegato in modo preciso e tecnico per aiutarti a comprendere tutte le sfumature.

**Sezione 3: Una rete basata sulla liquidità**  
Lightning Network non si limita a canali individuali; è una vera rete di pagamento. Vedremo come le transazioni possono essere instradate attraverso i nodi lungo la rete, utilizzando gli HTLC. Questa parte ti introdurrà anche alle sfide della liquidità inbound e outbound.

**Sezione 4: Strumenti Lightning Network**  
Questa sezione mostra gli strumenti pratici di Lightning Network, come *Invoice*, *LNURL* e *Keysend*. Imparerai anche a gestire la liquidità dei tuoi canali, un aspetto importante per garantire la fluidità dei pagamenti e massimizzare la loro l'efficienza sulla rete.

**Sezione 5: Andare Oltre**  
Infine concluderemo il corso ricapitolando i concetti trattati e aprendo la strada a temi più avanzati, per coloro che desiderano approfondire la loro conoscenza di Lightning Network.

Pronto a scoprire i meccanismi tecnici di Lightning Network? Andiamo!

---

*Ecco alcuni termini che incontrerai negli schemi del corso in inglese, accompagnati dalla loro traduzione per aiutarti a comprenderli meglio nella tua lingua:*

| Inglese            | Traduzione - spiegazione      |
| ------------------ | ----------------------------- |
| *timelock*         | Blocco temporale              |
| *Revocation Key*   | Chiave di revoca              |
| *invoice*          | Fattura / richiesta di pagamento|
| *sig* (signature)  | Firma                         |
| *secret*           | Segreto                       |
| *amount*           | Importo                       |
| *scan QR code*     | Scansiona il codice QR        |
| *Show QR code*     | Mostra il codice QR           |
| *Asks the invoice* | Richiede la fattura           |
| *Give the invoice* | Fornisce la fattura           |
| *Payment*          | Pagamento                     |
| *Preimage*         | Preimmagine                   |

# Le basi

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Comprendere Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>


:::video id=4315a277-12fe-4946-bb49-a807e60c09a7:::

Lightning Network è una rete di canali di pagamento costruita sopra il protocollo Bitcoin, con l'obiettivo di abilitare pagamenti veloci e a basso costo. Consente la creazione di canali di pagamento tra i partecipanti, all'interno dei quali le transazioni possono essere effettuate quasi istantaneamente e con fee minime, senza dover registrare ogni singolo movimento sulla blockchain. In questo modo Lightning Network cerca di migliorare la scalabilità di Bitcoin e renderlo utilizzabile per il pagamento di importi piccoli.

Prima di esplorare l'aspetto di "rete", è importante comprendere il concetto di **canale di pagamento**, come funziona e quali sono le sue specificità. Questo è l'argomento del primo capitolo.

### Il Concetto di Canale di Pagamento

Un canale di pagamento consente a due parti, esempio **Alice** e **Bob**, di scambiare fondi tramite Lightning Network. Ogni protagonista ha un nodo, simboleggiato da un cerchio, e il canale tra loro è rappresentato da una linea retta.

![LNP201](assets/en/001.webp)

Nel nostro esempio, Alice ha 100.000 satoshi dalla sua parte del canale, e Bob ne ha 30.000, per un totale di 130.000 satoshi, che costituiscono la **capacità del canale**.

**Ma cos'è un satoshi?**

Il **satoshi** (o "sat"), in Bitcoin è un'unità di conto. Simile a un centesimo per l'euro, un satoshi è semplicemente una frazione di Bitcoin, che equivale a **0,00000001 Bitcoin**, ovvero un cento-milionesimo. Utilizzare il satoshi diventa sempre più pratico man mano che il valore di Bitcoin aumenta.

### Assegnazione dei Fondi nel Canale

Ritorniamo al canale di pagamento. Il concetto chiave qui è il "**lato del canale**". Ogni partecipante ha fondi sul proprio lato del canale: Alice 100.000 satoshi e Bob 30.000. Come abbiamo visto la somma di questi fondi rappresenta la capacità totale del canale, una cifra stabilita al momento della sua apertura.

![LNP201](assets/en/002.webp)

Prendiamo l'esempio di una transazione Lightning. Se Alice volesse inviare 40.000 satoshi a Bob, può farlo perché lei ha fondi sufficienti (100.000 satoshi). Dopo questa transazione Alice avrà 60.000 satoshi dal suo lato, Bob 70.000.

![LNP201](assets/en/003.webp)

La **capacità del canale**, fissata a 130.000 satoshi, rimane costante. Ciò che cambia è la ripartizione dei fondi. Questo sistema non permette di inviare più fondi di quanti se ne possiedano. Se Bob volesse rispedire 80.000 satoshi ad Alice, ad esempio, non potrebbe perché ne ha solo 70.000.

Un altro modo per capire meglio l'allocazione dei fondi è immaginare un **cursore** che indichi dove si trovano i fondi nel canale. All'inizio, con 100.000 satoshi per Alice e 30.000 per Bob, il cursore è più spostato verso Bob, poiché Alice ha molti più fondi. Dopo la transazione di 40.000 satoshi, il cursore si sposterà leggermente verso Alice, che ora possiede 60.000 satoshi.

![LNP201](assets/en/004.webp)

Questa rappresentazione può essere utile per immaginare il bilanciamento dei fondi in un canale.

### Regole Fondamentali di un Canale di Pagamento

Il primo punto da ricordare è che la **capacità del canale** è fissa. È un po' come il diametro di un tubo: determina la quantità massima di fondi che possono essere inviati attraverso il canale in una sola volta.
Prendiamo un esempio: se Alice ha 130.000 satoshi dal suo lato, può inviare al massimo 130.000 satoshi a Bob in una singola transazione. Tuttavia, Bob può poi rispedire questi fondi ad Alice, in parte o interamente.

Ciò che è importante capire è che la capacità fissa del canale limita l'importo massimo di una singola transazione, ma non il numero totale di transazioni possibili, né il volume complessivo dei fondi scambiati all'interno del canale.

**Quali insegnamenti puoi trarre da questo capitolo?**

- La capacità di un canale è fissa e determina l'importo massimo che può essere inviato in una singola transazione.
- I fondi in un canale sono distribuiti tra i due partecipanti, e ciascuno può inviare all'altro solo i fondi che possiede dal suo lato.
- Lightning Network consente quindi lo scambio rapido ed efficiente di fondi, rispettando le limitazioni imposte dalla capacità dei canali.

Questa è la fine del primo capitolo, dove abbiamo gettato le basi per comprendere Lightning Network. Nei prossimi capitoli vedremo come aprire un canale e approfondiremo i concetti qui discussi.

## Bitcoin, Indirizzi, UTXO e Transazioni

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>
:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::

Questo capitolo è un po' speciale poiché non sarà dedicato espressamente a Lightning Network, ma a Bitcoin. Lightning Network è infatti un layer aggiuntivo, costruito su Bitcoin. È quindi essenziale comprendere alcuni concetti fondamentali del funzionamento di Bitcoin, per afferrare correttamente i concetti nei capitoli successivi. Di seguito esamineremo le basi degli indirizzi di ricezione Bitcoin, gli UTXO e il funzionamento delle transazioni Bitcoin.

### Indirizzi Bitcoin, Chiavi Private e Chiavi Pubbliche

Un indirizzo Bitcoin è una serie di caratteri derivati da una **chiave pubblica**, che a sua volta è calcolata da una **chiave privata**. Come sicuramente saprai, è utilizzato per bloccare i bitcoin, il che equivale a riceverli nel nostro wallet.

La chiave privata è un elemento segreto che **non dovrebbe mai essere condiviso**, mentre la chiave pubblica e l'indirizzo possono essere condivisi senza rischio per la sicurezza (la loro divulgazione rappresenta solo un rischio per la tua privacy). Ecco una rappresentazione comune che adotteremo durante questo corso:

- Le **chiavi private** saranno rappresentate **verticalmente**.
- Le **chiavi pubbliche** saranno rappresentate **orizzontalmente**.
- Il loro colore indica chi le possiede (Alice in arancione e Bob in nero...).

### Transazioni Bitcoin: Invio di Fondi e Script

Una transazione Bitcoin comporta l'invio di fondi da un indirizzo ad un altro. Prendiamo l'esempio di Alice che invia 0,002 bitcoin a Bob. Alice utilizza la chiave privata associata al suo indirizzo per **firmare** la transazione, dimostrando così di essere effettivamente in grado di spendere questi fondi. Ma cosa succede esattamente dietro questa transazione? I fondi su un indirizzo Bitcoin sono bloccati da uno **script**, una sorta di mini-programma che impone certe condizioni per spendere i fondi.

Lo script più comune richiede una firma digitale, effettuata con la chiave privata associata all'indirizzo. Quando Alice firma una transazione con la sua chiave privata, **sblocca lo script** che vincola i fondi, i quali possono essere trasferiti. Il trasferimento di fondi comporta l'aggiunta di un nuovo script, stabilendo che per spenderli in seguito, sarà richiesta la firma della chiave privata di **Bob**.

![LNP201](assets/en/005.webp)


### UTXO: Unspent Transaction Output (Output di una Transazione Non Spesa)

In Bitcoin ciò che effettivamente scambiamo non sono direttamente i bitcoin, ma **[UTXO](https://planb.academy/resources/glossary/utxo)** (_Unspent Transaction Outputs_), ovvero "gli output di transazione non spesi".

Un UTXO è una porzione di bitcoin che può avere qualsiasi valore, ad esempio, **2.000 bitcoin**, **8 bitcoin**, o anche **8.000 satoshi**. Ogni UTXO è bloccato da uno script e, per spenderlo, si devono soddisfare le condizioni dello script, spesso una firma effettuata con la chiave privata corrispondente a un dato indirizzo di ricezione.

Gli UTXO non possono essere divisi. Ogni volta che vengono utilizzati per spendere l'importo che rappresentano, devono essere usati nella loro totalità. È un po' come una banconota: se hai una banconota da 10€ e devi al panettiere 5€, non puoi semplicemente tagliare la banconota a metà. Devi dargli la banconota da 10€ e lui ti darà 5€ di resto. Questo è esattamente lo stesso principio per gli UTXO! Quando Alice sblocca ad esempio uno script con la sua chiave privata, sblocca l'intero UTXO. Se desidera inviare a Bob solo una parte dei fondi rappresentati da questo UTXO, può "frammentarlo" in parti più piccole. Invierà quindi 0,0015 BTC a Bob e invierà il resto, 0,0005 BTC, a un proprio **indirizzo di resto**.

Ecco un esempio di una transazione con 2 output:

- Un UTXO di 0,0015 BTC per Bob, bloccato da uno script che richiede la firma della chiave privata di Bob.
- Un UTXO di 0,0005 BTC per Alice, bloccato da uno script che richiede la sua firma.

![LNP201](assets/en/006.webp)

### Indirizzi multi-firma

Oltre agli indirizzi semplici generati da una singola chiave pubblica, è possibile usare **indirizzi multi-firma** creati da più chiavi pubbliche. Un caso particolarmente interessante per Lightning Network è l'**indirizzo multi-firma 2/2** (multifirma due-di-due), generato da due chiavi pubbliche:

![LNP201](assets/en/007.webp)

Per spendere i fondi bloccati con questo indirizzo multi-firma 2/2, è necessario firmare con entrambe le chiavi private associate alle chiavi pubbliche.

![LNP201](assets/en/008.webp)

Questo tipo di indirizzo rappresenta per l'appunto i canali di pagamento Lightning Network sulla blockchain di Bitcoin.

**Quali insegnamenti puoi trarre da questo capitolo?**

- Un **indirizzo Bitcoin** deriva da una chiave pubblica, che a sua volta è calcolata a partire da una chiave privata.
- Nel protocollo Bitcoin i fondi sono bloccati da **script**; per spendere questi fondi è necessario soddisfare lo script, che generalmente comporta la fornitura di una firma effettuata con la corrispondente chiave privata.
- Gli **UTXO** sono porzioni di bitcoin bloccate da script e ogni transazione Bitcoin consiste nello sblocco di un UTXO che ne crea uno o più nuovi al suo posto.
- Gli **indirizzi multi-firma 2/2** richiedono la firma di due chiavi private per spendere i fondi. Questi indirizzi specifici sono utilizzati nel contesto di Lightning Network per la creazione dei canali di pagamento.

Questo capitolo su Bitcoin ci ha permesso di rivedere alcune nozioni essenziali per proseguire. Nel prossimo scopriremo specificamente come funziona l'apertura dei canali Lightning Network.

# Apertura e Chiusura dei Canali

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Apertura del Canale

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::

In questo capitolo vedremo, in maniera accurata, come aprire un canale di pagamento Lightning Network, per poi capire il collegamento tra questa operazione e il sistema Bitcoin sottostante.

### Canali Lightning

Come abbiamo visto nel primo capitolo, un **canale di pagamento** Lightning può essere paragonato a un "tubo" per lo scambio di fondi tra due partecipanti (**Alice** e **Bob** nei nostri esempi). La capacità di questo canale corrisponde alla somma dei fondi disponibili su ciascun lato. Nel nostro esempio Alice ha **100.000 satoshi** e Bob ne ha **30.000**, dando al canale una **capacità totale** di **130.000 satoshi**.

![LNP201](assets/en/009.webp)

### Livelli di Scambio di Informazioni

È cruciale distinguere chiaramente i diversi livelli di scambio su Lightning Network:

- **Comunicazioni peer-to-peer (protocollo Lightning)**: questi sono i messaggi che i nodi Lightning inviano l'uno all'altro per comunicare. Rappresenteremo questi messaggi con linee tratteggiate nere nei prossimi diagrammi.

- **Canali di pagamento (protocollo Lightning)**: questi sono i percorsi per lo scambio di fondi su Lightning, che rappresenteremo con linee nere continue.

- **Transazioni Bitcoin (protocollo Bitcoin)**: queste sono le transazioni effettuate onchain, che rappresenteremo con linee arancioni.

![LNP201](assets/en/010.webp)

Vale la pena sottolineare che un nodo Lightning può comunicare tramite il protocollo P2P senza aprire un canale ma, per scambiare fondi, il canale è necessario.

### Step di apertura di un Canale Lightning

- **Scambio di messaggi**: Alice vuole aprire un canale con Bob. Lei gli invia un messaggio contenente l'importo che vuole depositare nel canale (130.000 satoshi) e la sua chiave pubblica. Bob risponde condividendo la propria chiave pubblica.

![LNP201](assets/en/011.webp)

- **Creazione dell'indirizzo multi-firma**: con le due chiavi pubbliche, Alice crea un **indirizzo multi-firma 2/2**, il che significa che i fondi che verranno successivamente depositati su questo indirizzo richiederanno entrambe le firme (di Alice e di Bob) per essere spesi.

![LNP201](assets/en/012.webp)

- **Transazione di deposito**: Alice prepara una transazione Bitcoin per depositare fondi su questo indirizzo multi-firma. Ad esempio, potrebbe decidere di inviare **130.000 satoshi** a questo indirizzo. La transazione è **costruita ma non ancora pubblicata** sulla blockchain.

![LNP201](assets/en/013.webp)

- **Transazione di prelievo**: prima di pubblicare la transazione di deposito, Alice costruisce una transazione di prelievo, in modo da poter recuperare i suoi fondi in caso di problemi con Bob. Infatti, una volta che Alice pubblica la transazione di deposito, i suoi satoshi saranno bloccati su un indirizzo multi-firma 2/2 che richiede entrambe le firme per essere sbloccato, la sua e quella di Bob. Alice si protegge da questo rischio costruendo la transazione di prelievo, che le permetterà di recuperare i suoi fondi.

![LNP201](assets/en/014.webp)

- **Firma di Bob**: Alice invia la transazione di deposito a Bob come prova e gli chiede di firmare la transazione di prelievo. Una volta ottenuta la firma di Bob sulla transazione di prelievo, Alice ha la certezza di poter recuperare i suoi fondi in qualsiasi momento, poiché ora è necessaria solo la sua firma per sbloccare il multi-firma.

![LNP201](assets/en/015.webp)

- **Pubblicazione della transazione di deposito**: una volta ottenuta la firma di Bob, Alice può pubblicare la transazione di deposito sulla blockchain di Bitcoin, aprendo ufficialmente il canale tra i due utenti.

![LNP201](assets/en/016.webp)

### Quando il canale si può considerare aperto?

Il canale si considera aperto una volta che la transazione di deposito è inclusa in un blocco e ha raggiunto una certa profondità di conferme (numero di blocchi successivi).

**Quali insegnamenti puoi trarre da questo capitolo?**

- L'apertura di un canale inizia con lo scambio di **messaggi** tra le due parti (scambio di importi e chiavi pubbliche).
- Un canale si forma creando un **indirizzo multi-firma 2/2** e depositando fondi su di esso tramite una transazione onchain.
- La persona che apre il canale si assicura di poter **recuperare i suoi fondi** attraverso una transazione di prelievo firmata dall'altra parte, prima di pubblicare la transazione di deposito.

Nel prossimo capitolo, esploreremo il funzionamento tecnico di una transazione all'interno di un canale sulla rete Lightning.

## Commitment transaction

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::

In questo capitolo scopriremo il funzionamento tecnico di una transazione all'interno di un canale sulla rete Lightning, ovvero quando i fondi vengono spostati da un lato all'altro del canale.

### Promemoria del ciclo di vita del canale

Come visto in precedenza, un canale Lightning inizia con un'**apertura** tramite una transazione onchain. Il canale può essere **chiuso** in qualsiasi momento, anch'esso tramite una transazione Bitcoin. Tra questi due momenti, un numero quasi infinito di transazioni può essere eseguito all'interno del canale, senza passare attraverso la blockchain. Vediamo cosa succede durante una transazione nel canale.

![LNP201](assets/en/017.webp)

### Lo stato iniziale del canale

Al momento dell'apertura del canale, Alice ha depositato **130.000 satoshi** sull'indirizzo multi-firma del canale. Pertanto, nello stato iniziale, tutti i fondi sono dalla parte di Alice. Prima di aprire il canale Alice ha anche fatto firmare a Bob una **transazione di prelievo**, per permetterle di recuperare i suoi fondi qualora decidesse di chiudere il canale.

![LNP201](assets/en/018.webp)

### Transazioni non pubblicate: Commitment Transactions

Quando Alice effettua un pagamento nel canale per inviare fondi a Bob, viene creata una nuova transazione Bitcoin che riflette il cambiamento nella distribuzione dei fondi. Questa transazione, chiamata **commitment transaction**, non viene pubblicata sulla blockchain ma rappresenta il nuovo stato del canale a seguito del pagamento Lightning.

Prendiamo un esempio con Alice che invia 30.000 satoshi a Bob:

- **Inizialmente**: Alice ha 130.000 satoshi.
- **Dopo il pagamento**: Alice ha 100.000 satoshi e Bob 30.000 satoshi.
  Per convalidare questo trasferimento, Alice e Bob creano una nuova **transazione onchain non pubblicata** che invierebbe **100.000 satoshi ad Alice** e **30.000 satoshi a Bob** dall'indirizzo multi-firma. Entrambe le parti costruiscono questa transazione indipendentemente, ma con gli stessi dati (importi e indirizzi). Una volta costruita, ciascuno firma la transazione e scambia la propria firma con l'altro. Questo permette a entrambe le parti di pubblicare la transazione in qualsiasi momento, se necessario, per recuperare onchain la propria quota di fondi sul canale.  

![LNP201](assets/en/019.webp)

### Processo di Trasferimento: Invoice

Quando Bob desidera ricevere fondi, invia ad Alice un'**_[invoice](https://planb.academy/resources/glossary/invoice-lightning)_** per 30.000 satoshi. Alice procede quindi a pagare avviando il trasferimento all'interno del canale. Come abbiamo visto, questo processo si basa sulla creazione e firma di una nuova **commitment transaction**.

Ogni commitment transaction rappresenta la nuova distribuzione dei fondi nel canale dopo ogni trasferimento. In questo esempio, dopo la transazione, Bob ha 30.000 satoshi e Alice ha 100.000 satoshi. Se uno dei due partecipanti decidesse di pubblicare questa commitment transaction sulla blockchain, ciò provocherebbe la chiusura del canale con i fondi ripartiti secondo quest'ultima distribuzione.

![LNP201](assets/en/020.webp)

### Nuovo Stato Dopo una Seconda Transazione

Prendiamo un altro esempio: dopo la prima transazione in cui Alice ha inviato 30.000 satoshi a Bob, Bob decide di inviare **10.000 satoshi indietro ad Alice**. Questo crea un nuovo stato del canale. La nuova **commitment transaction** rappresenterà questa distribuzione aggiornata:

- **Alice** ora ha **110.000 satoshi**.
- **Bob** ha **20.000 satoshi**.

![LNP201](assets/en/021.webp)

Ancora una volta questa transazione non viene propagata alla blockchain, ma può essere pubblicata in qualsiasi momento nel caso in cui il canale debba essere chiuso.

In sintesi, quando i fondi vengono trasferiti all'interno di un canale Lightning:

- Alice e Bob creano una nuova **commitment transaction**, che riflette la nuova distribuzione dei fondi.
- Questa transazione è **firmata** da entrambe le parti, ma **non pubblicata** sulla blockchain di Bitcoin finché il canale rimane aperto.
- Le commitment transaction assicurano che ciascun partecipante possa recuperare onchain i propri fondi in qualsiasi momento, pubblicando l'ultima transazione firmata.

Questo sistema presenta tuttavia una potenziale falla, che affronteremo nel prossimo capitolo. Vedremo come ciascun partecipante può proteggersi contro un tentativo di truffa da parte dell'altra parte.

## Revocation key

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

In questo capitolo approfondiremo il funzionamento delle transazioni sulla rete Lightning, discutendo i meccanismi in atto per proteggersi dalle truffe, assicurando che ciascuna parte rispetti le regole all'interno di un canale.

### Promemoria: commitment transaction

Come visto in precedenza, le transazioni su Lightning si basano su **commitment transaction** non pubblicate. Queste transazioni riflettono la distribuzione aggiornata dei fondi all'interno del canale. Quando viene effettuato un nuovo pagamento Lightning, viene creata e firmata da entrambe le parti una nuova commitment transaction che rispecchia lo stato aggiornato del canale.

Prendiamo un esempio semplice:

- **Stato iniziale**: Alice ha **100.000 satoshi**, Bob **30.000 satoshi**.
- Dopo una transazione in cui Alice invia **40.000 satoshi** a Bob, la nuova commitment transaction distribuisce i fondi come segue:
  - Alice: **60.000 satoshi**
  - Bob: **70.000 satoshi**

![LNP201](assets/en/022.webp)

Entrambe le parti possono pubblicare la **commitment transaction firmata più recente** in qualsiasi momento, chiudere il canale e recuperare i propri fondi.

### La falla: Truffare Pubblicando una Vecchia Commitment Transaction

Un potenziale problema sorge se una delle parti decide di **truffare** l'altra, pubblicando una commitment transaction non aggiornata. Ad esempio, Alice potrebbe pubblicare una vecchia commitment transaction in cui aveva **100.000 satoshi**, anche se ora ne ha solo **60.000**. Ciò le permetterebbe di rubare **40.000 satoshi** a Bob.

![LNP201](assets/en/023.webp)

Ancora peggio, Alice potrebbe pubblicare la primissima transazione di prelievo, quella creata prima che il canale fosse aperto, dove aveva **130.000 satoshi**, per rubare così tutti i fondi del canale.

![LNP201](assets/en/024.webp)

### Soluzione: Revocation Key e Timelock

Per prevenire questo tipo di truffa da parte di Alice, su Lightning Network vengono aggiunti **meccanismi di sicurezza** alle commitment transaction:

- **Il timelock**: ogni commitment transaction include un timelock per i fondi di Alice. Il timelock è una primitiva di smart contract che stabilisce una condizione temporale che deve essere soddisfatta affinché una transazione possa essere aggiunta a un blocco. Ciò significa che Alice non può recuperare i suoi fondi fino a quando non sia passato un certo numero di blocchi, se pubblica una delle commitment transaction. Il timelock inizia si applica dalla conferma della commitment transaction. La sua durata è generalmente proporzionale alla dimensione del canale, ma può anche essere configurata manualmente.

- **Revocation Key**: i fondi di Alice possono anche essere spesi immediatamente da Bob se possiede la **revocation key**. Questa chiave consiste in un segreto detenuto da Alice e un segreto detenuto da Bob. Nota che questo segreto è diverso per ogni commitment transaction. Grazie a questi 2 meccanismi combinati, Bob ha il tempo di rilevare il tentativo di Alice di barare e di punirla, recuperando il suo output con la revocation key, il che per Bob significa ricevere tutti i fondi del canale. La nostra nuova commitment transaction ora apparirà così:

![LNP201](assets/en/025.webp)

Analizziamo insieme il funzionamento di questo meccanismo.


### Processo di Aggiornamento della Transazione

Quando Alice e Bob aggiornano lo stato del canale con un nuovo pagamento Lightning, si scambiano in anticipo i rispettivi **segreti** relativi alla precedente commitment transaction (quella che diventerà obsoleta e potrebbe permettere a uno di loro di barare). Significa che, nel nuovo stato del canale:

- Alice e Bob hanno una nuova commitment transaction che rispecchia l'attuale distribuzione dei fondi dopo il pagamento Lightning.
- Ognuno ha il segreto dell'altro per la transazione precedente, il che permette loro di usare la revocation key solo se uno di loro prova a barare pubblicando una transazione con uno stato vecchio nella mempool di Bitcoin. Per punire l'altra parte, è infatti necessario detenere entrambi i segreti e la commitment transaction della controparte, che include l'input firmato. Senza questa transazione, la revocation key da sola è priva di utilità. L'unico modo per ottenere questa transazione è recuperarla dalla mempool (nelle transazioni in attesa di conferma) o tra le transazioni confermate sulla blockchain durante il timelock, il che dimostra che l'altra parte sta cercando di barare, intenzionalmente o meno.

Facciamo un esempio per capire bene questo processo:

- **Stato Iniziale**: Alice ha **100.000 satoshi**, Bob **30.000 satoshi**.

![LNP201](assets/en/026.webp)

- Bob vuole ricevere 40.000 satoshi da Alice tramite il loro canale Lightning. Per fare ciò:
   - Lui le invia un'invoice insieme al suo segreto per la revocation key della precedente commitment transaction.
   - In risposta, Alice fornisce la sua firma per la nuova commitment transaction di Bob, così come il proprio segreto per la revocation key della precedente transazione.
   - Infine, Bob invia la sua firma per la nuova commitment transaction di Alice.
   - Questi scambi permettono ad Alice di inviare **40.000 satoshi** a Bob su Lightning tramite il loro canale, mentre le nuove commitment transaction riflettono la nuova distribuzione dei fondi.

![LNP201](assets/en/027.webp)

- Se Alice tenta di pubblicare la vecchia commitment transaction dove possedeva ancora **100.000 satoshi**, Bob, avendo ottenuto la revocation key, può immediatamente recuperare i fondi usandola, mentre Alice è bloccata dal timelock.

![LNP201](assets/en/028.webp)

Anche se, in questo caso, Bob non ha interesse economico a cercare di barare, se lo fa comunque, anche Alice beneficia della protezione simmetrica che le offre le stesse garanzie.

**Quali insegnamenti puoi trarre da questo capitolo?**

Le **commitment transaction** di Lightning Network includono meccanismi di sicurezza che riducono il rischio di venire imbrogliati e disincentivano gli utenti malevoli a farlo. Prima di firmare una nuova commitment transaction, Alice e Bob scambiano i rispettivi **segreti** per le precedenti commitment transaction. Se Alice prova a pubblicare una vecchia commitment transaction, Bob può usare la **revocation key** per recuperare tutti i fondi prima che Alice possa ricevere i fondi (perché è bloccata dal timelock), il che la punisce per aver tentato di barare.

Questo sistema di sicurezza garantisce che i partecipanti aderiscano alle regole di Lightning Network, e non possano trarre profitto dalla pubblicazione di vecchie commitment transaction.

A questo punto della formazione, sai come vengono aperti i canali Lightning e come funzionano le transazioni al loro interno. Nel prossimo capitolo scopriremo i diversi modi per chiudere un canale e recuperare i tuoi bitcoin sulla blockchain.

## Chiusura del Canale

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::

In questo capitolo, discuteremo della **chiusura di un canale** Lightning Network, che viene effettuata tramite una transazione onchain, proprio come l'apertura di un canale. Dopo aver visto come funzionano le transazioni all'interno di un canale, è ora il momento di vedere come chiudere il canale e recuperare i fondi sulla blockchain di Bitcoin.

### Promemoria del ciclo di vita del canale

Il **ciclo di vita di un canale** inizia con la sua **apertura**, tramite una transazione onchain, poi vengono effettuate transazioni Lightning al suo interno e, infine, quando le parti desiderano recuperare i loro fondi, il canale viene **chiuso** tramite una seconda transazione onchain. Le transazioni intermedie effettuate sul canale sono rappresentate da **commitment transaction** e non sono pubblicate.

![LNP201](assets/en/029.webp)

### I tre tipi di chiusura del canale

Ci sono tre modi principali per chiudere questo canale, che possono essere chiamati **il buono, il brutto e il truffatore** (ispirato da Andreas Antonopoulos in _Mastering the Lightning Network_):

- **Il Buono**: la **chiusura cooperativa**, dove Alice e Bob concordano di chiudere il canale.
- **Il Brutto**: la **chiusura forzata**, dove una delle parti decide di chiudere il canale onestamente, ma senza l'accordo dell'altra.
- **Il Cattivo**: la **chiusura con imbroglio**, dove una delle parti tenta di rubare fondi pubblicando una vecchia commitment transaction (qualsiasi tranne l'ultima, che riflette la distribuzione effettiva e giusta dei fondi).

Facciamo un esempio:

- Alice possiede **100.000 satoshi** e Bob **30.000 satoshi**.
- Questa distribuzione si riflette in **2 commitment transaction** (una per utente) che non sono pubblicate, ma potrebbero esserlo in caso di chiusura del canale.

![LNP201](assets/en/030.webp)

### Il Buono: la chiusura cooperativa

In una **chiusura cooperativa**, Alice e Bob concordano di chiudere il canale. Ecco come accade:

- Alice invia un messaggio a Bob tramite il protocollo di comunicazione Lightning per proporre la chiusura del canale.
- Bob accetta e le due parti non effettuano ulteriori transazioni nel canale.

![LNP201](assets/en/031.webp)

- Alice e Bob negoziano insieme le fee della **transazione di chiusura**. Queste fee sono generalmente calcolate in base allo stato della rete al momento della chiusura. È importante notare che **è sempre la persona che ha aperto il canale** (Alice nel nostro esempio) a pagare le fee per la chiusura.
- Costruiscono una nuova **transazione di chiusura**, che assomiglia a una commitment transaction, ma senza timelock o meccanismi di revoca, poiché entrambe le parti stanno cooperando e non c'è rischio di imbroglio. Questa transazione di chiusura cooperativa è quindi diversa dalle commitment transaction.

Per esempio, se Alice possiede **100.000 satoshi** e Bob **30.000 satoshi**, la transazione di chiusura invierà **100.000 satoshi** all'indirizzo di Alice e **30.000 satoshi** all'indirizzo di Bob, senza vincoli di timelock. Una volta che questa transazione è firmata da entrambe le parti, viene pubblicata da Alice. Non appena la transazione è confermata sulla blockchain di Bitcoin, il canale Lightning è ufficialmente chiuso.

![LNP201](assets/en/032.webp)

La **chiusura cooperativa** è il metodo migliore per chiudere un canale, perché è veloce (non c'è timelock) e le fee di transazione sono commisurate alle attuali condizioni di mercato. Questo evita di pagare troppo poco, il che potrebbe rischiare di bloccare la transazione nella mempool, o di pagare inutilmente troppo, portando a una perdita finanziaria non necessaria per i partecipanti.

### Il Brutto: la chiusura forzata

Quando il nodo di Alice invia un messaggio a quello di Bob chiedendo una chiusura cooperativa, se lui non risponde (per esempio, a causa di un'interruzione di internet o di un problema tecnico), Alice può procedere alla **chiusura forzata**, pubblicando **l'ultima commitment transaction firmata**.
In questo caso, Alice pubblicherà semplicemente l'ultima commitment transaction, che riflette lo stato del canale al momento dell'ultimo pagamento Lightning avvenuto e con la corretta distribuzione dei fondi.

![LNP201](assets/en/033.webp)

La transazione legata alla chiusura forzata include un **timelock** per i fondi di Alice, rendendo la chiusura più lenta.

![LNP201](assets/en/034.webp)

Inoltre, le fee della commitment transaction possono essere inadeguate al momento della chiusura, poiché sono state impostate quando la commitment transaction è stata creata, talvolta diversi mesi prima. I client Lightning generalmente sovrastimano le fee per evitare problemi futuri, ma questo può portare stimare fee eccessive o, al contrario, troppo basse.

In sintesi, la **chiusura forzata** è un'opzione di ultima ratio, quando la controparte non risponde più. È più lenta e meno economica della chiusura cooperativa, pertanto dovrebbe essere evitata il più possibile.

### Il Cattivo: l'imbroglio

Infine una chiusura con **imbroglio** si verifica quando una delle parti cerca di pubblicare una vecchia commitment transaction, spesso nel momento in cui detiene più fondi di quanto dovrebbe. Per esempio, Alice potrebbe pubblicare una vecchia transazione dove possedeva **120.000 satoshi**, mentre ora ne possiede effettivamente solo **100.000**.

![LNP201](assets/en/035.webp)

Per prevenire questo imbroglio, Bob monitora la blockchain di Bitcoin e la sua mempool per assicurarsi che Alice non pubblichi una vecchia transazione. Se Bob rileva un tentativo di imbroglio, può usare la **revocation key** per recuperare i fondi di Alice e punirla, prendendo l'intera somma nel canale. Poiché Alice è bloccata dal timelock sul suo output, Bob ha il tempo di spenderlo senza un timelock dalla sua parte per recuperare l'intera somma su un indirizzo di sua proprietà.

![LNP201](assets/en/036.webp)

Ovviamente, barare può potenzialmente avere successo se Bob non agisce entro il tempo imposto dal timelock sull'output di Alice. In questo caso l'output di Alice viene sbloccato, permettendole di consumarlo per creare un nuovo output verso un proprio indirizzo.

**Quali insegnamenti puoi trarre da questo capitolo?**

Ci sono tre modi per chiudere un canale:

- **Chiusura Cooperativa**: veloce e meno costosa, dove entrambe le parti concordano di chiudere il canale e pubblicano una transazione di chiusura su misura.
- **Chiusura Forzata**: meno desiderabile, poiché si basa sulla pubblicazione di una commitment transaction, con fee potenzialmente inadeguate e un timelock che rallenta la chiusura.
- **Imbroglio**: se una delle parti tenta di rubare fondi pubblicando uno stato del canale non aggiornato, l'altra può utilizzare la revocation key per punire questo imbroglio.

Nei prossimi capitoli, esploreremo Lightning Network da una prospettiva più ampia, concentrandoci su come funziona la sua rete.

# Una rete basata sulla liquidità

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::

In questo capitolo esploreremo come i pagamenti Lightning Network possono raggiungere un destinatario anche se le parti non sono direttamente connesse tra loro con un canale di pagamento. Lightning è, infatti, una **rete di canali di pagamento**, che consente di inviare fondi a un nodo distante attraverso i canali di altri partecipanti. Scopriremo come vengono instradati i pagamenti attraverso la rete, come si muove la liquidità tra i canali e come vengono calcolate le fee sulle transazioni.

### Rete dei Canali di Pagamento

Su Lightning Network una transazione corrisponde a un trasferimento di fondi tra due nodi. Come visto nei capitoli precedenti, è necessario aprire un canale con qualcuno per eseguire pagamenti Lightning. Il canale consente un numero quasi infinito di transazioni off-chain prima di chiuderlo per recuperare il saldo on-chain. Tale metodo ha lo svantaggio di richiedere un canale diretto con l'altra persona per ricevere o inviare fondi, il che implica una transazione di apertura e una di chiusura per ogni canale. Se prevedo di effettuare un gran numero di pagamenti con questa persona, aprire e chiudere un canale diventa conveniente. Al contrario, se ho bisogno di eseguire solo pochi pagamenti Lightning, aprire un canale diretto non è vantaggioso, poiché mi costerebbe 2 transazioni on-chain per un numero limitato di trasferimenti off-chain. È il caso potrebbe verificarsi, ad esempio, quando si desidera pagare con Lightning un commerciante senza pianificare di tornare.

Per risolvere questo problema, Lightning Network consente di instradare un pagamento attraverso diversi canali e nodi intermedi, consentendo così una transazione senza un canale diretto con l'altra persona.

Per esempio, immagina che:

- **Alice** (in arancione) abbia un canale con **Suzie** (in grigio) con **100.000 satoshi** dal suo lato e **30.000 satoshi** dal lato di Suzie.
- **Suzie** ha un canale con **Bob** in cui possiede **250.000 satoshi** e dove Bob non ha satoshi.

![LNP201](assets/en/037.webp)

Se Alice vuole inviare fondi a Bob senza aprire un canale diretto con lui, dovrà passare attraverso Suzie, e ogni canale dovrà adeguare la liquidità da ciascun lato. **I satoshi inviati rimangono all'interno dei rispettivi canali**; non "attraversano" effettivamente i canali, ma il trasferimento avviene tramite un adeguamento della liquidità interna in ogni canale.

Supponiamo che Alice voglia inviare **50.000 satoshi** a Bob:

- **Alice** invia 50.000 satoshi a **Suzie** nel loro canale comune.
- **Suzie** replica questo trasferimento inviando 50.000 satoshi a **Bob** nel loro canale.

![LNP201](assets/en/038.webp)

Il pagamento viene instradato a Bob attraverso uno spostamento di liquidità in ogni canale. Al termine dell'operazione, Alice finisce con 50.000 satoshi. Ha effettivamente trasferito 50.000 satoshi poiché inizialmente ne aveva 100.000. Bob, dal canto suo, finisce con un incremento di 50.000 satoshi. Per Suzie (il nodo intermedio), questa operazione è neutra: inizialmente, aveva 30.000 satoshi nel suo canale con Alice e 250.000 satoshi nel suo canale con Bob, per un totale di 280.000 satoshi. Dopo l'operazione detiene 80.000 satoshi nel suo canale con Alice e 200.000 satoshi nel suo canale con Bob, che da come totale la stessa somma di partenza.

L'instradamento è quindi limitato dalla **liquidità disponibile** nella direzione del trasferimento.

### Calcolo del Percorso e Limiti di Liquidità

Prendiamo un esempio teorico di un'altra rete con:

- **130.000 satoshi** dal lato di Alice (in arancione) nel suo canale con **Suzie** (in grigio).
- **90.000 satoshi** dal lato di **Suzie** e **200.000 satoshi** dal lato di **Carol** (in rosa).
- **150.000 satoshi** dal lato di **Carol** e **100.000 satoshi** dal lato di **Bob**.

![LNP201](assets/en/039.webp)

Il massimo che Alice può inviare a Bob in questa configurazione è **90.000 satoshi**, poiché è limitata dalla minore liquidità disponibile nel canale da **Suzie a Carol**. Nella direzione opposta (da Bob ad Alice), nessun pagamento è possibile perché il lato di **Suzie** nel canale con **Alice** non contiene satoshi. Pertanto, non c'è **nessun instradamento** utilizzabile per un trasferimento in questa direzione.
Alice invia **40.000 satoshi** a Bob attraverso i canali:

- Alice trasferisce 40.000 satoshi nel suo canale con Suzie.
- Suzie trasferisce 40.000 satoshi a Carol nel loro canale condiviso.
- Carol infine trasferisce 40.000 satoshi a Bob.

![LNP201](assets/en/040.webp)

I **satoshi inviati** in ogni canale **rimangono nel canale**, quindi i satoshi inviati da Carol a Bob non sono gli stessi di quelli inviati da Alice a Suzie. Il trasferimento avviene solo regolando la liquidità all'interno di ogni canale. Inoltre, la capacità totale dei canali rimane invariata.

![LNP201](assets/en/041.webp)

Come nell'esempio precedente, dopo la transazione, il nodo di partenza (Alice) ha 40.000 satoshi in meno. I nodi intermedi (Suzie e Carol) mantengono lo stesso importo totale, rendendo l'operazione neutra per loro. Infine, il nodo di destinazione (Bob) incrementa il saldo di 40.000 satoshi.

Il ruolo dei nodi intermedi è quindi molto importante nel funzionamento di Lightning Network. Essi facilitano i trasferimenti offrendo molteplici percorsi per i pagamenti. Per incoraggiare questi nodi a fornire la loro liquidità e partecipare all'instradamento dei pagamenti, vengono pagate loro delle **fee di routing**.

### Fee di Routing

I nodi intermedi applicano delle fee per permettere ai pagamenti di passare attraverso i loro canali. Queste sono stabilite da **ogni nodo per ogni canale**. Le fee consistono di 2 elementi:

- "**Fee base**": un importo fisso per canale, spesso **1 sat** per default, ma personalizzabile.
- "**Fee variabile**": una percentuale dell'importo trasferito, calcolata in **parti per milione (ppm)**. Per impostazione predefinita, è **1 ppm** (1 sat per milione di satoshi trasferiti), ma può anche essere variata.

Le fee variano anche a seconda della direzione del trasferimento. Ad esempio, per un pagamento da Alice a Suzie, si applicano le fee decise da Alice. Al contrario, da Suzie ad Alice, si applicano quelle impostate di Suzie.

Per esempio, per un canale tra Alice e Suzie, potremmo avere:

- **Alice**: fee base di 1 sat e 1 ppm per quelle variabili.
- **Suzie**: fee base di 0,5 sat e 10 ppm per quelle variabili.

![LNP201](assets/en/042.webp)

Per comprendere meglio come funzionano le fee, studiamo la stessa rete di canali di prima, ma ora con le seguenti fee di routing:

- Canale **Alice - Suzie**: fee base di 1 satoshi e 1 ppm per Alice.
- Canale **Suzie - Carol**: fee base di 0 satoshi e 200 ppm per Suzie.
- Canale **Carol - Bob**: fee base di 1 satoshi e 1 ppm per Suzie 2.
  
![LNP201](assets/en/043.webp)
Per lo stesso pagamento di **40.000 satoshi** a Bob, Alice dovrà inviare un po' di più, poiché ogni nodo intermedio tratterrà le proprie fee:

- **Carol** trattiene 1,04 satoshi sul canale con Bob:
$$ f_{\text{Carol-Bob}} = \text{base fee} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$
$$ f_{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- **Suzie** trattiene 8 satoshi sul canale con Carol:
$$ f_{\text{Suzie-Carol}} = \text{base fee} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$
$$ f_{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

Le fee totali per questo pagamento, con questo percorso, sono quindi **9,04 satoshi**. Così, Alice deve inviare **40.009,04 satoshi** affinché Bob ne riceva esattamente **40.000**.

![LNP201](assets/en/044.webp)

La liquidità viene quindi aggiornata:

![LNP201](assets/en/045.webp)

### Onion Routing (Instradamento su rete Onion)

Per instradare un pagamento dal mittente al destinatario, la rete Lightning utilizza un metodo chiamato "**onion routing**". A differenza dell'instradamento dei dati classici, dove ogni nodo intermedio decide la direzione dei dati in base alla loro destinazione, l'onion routing funziona diversamente:

- **Il nodo mittente calcola l'intero percorso**: Alice, ad esempio, determina che il suo pagamento deve passare attraverso Suzie e Carol prima di raggiungere Bob.
- **Ogni nodo intermedio conosce solo il suo vicino più prossimo**: Suzie sa solo che ha ricevuto fondi da Alice e che deve trasferirli a Carol. Tuttavia, Suzie non sa se Alice è il nodo sorgente o un nodo intermedio, così come non sa nemmeno se Carol è il nodo destinatario o solo un altro nodo di passaggio. Questo vale sia per Carol che per tutti gli altri nodi sul percorso. L'Onion Routing preserva così la confidenzialità delle transazioni mascherando l'identità del mittente e del destinatario finale. Per garantire che il nodo trasmittente possa calcolare un percorso completo verso il destinatario nell'Onion Routing, deve mantenere un **grafico della rete** per conoscere la sua topologia e determinare i percorsi possibili.
  
**Quali insegnamenti puoi trarre da questo capitolo?**

- I pagamenti Lightning possono essere instradati tra nodi indirettamente connessi attraverso canali intermedi. Ciascuno di questi nodi di passaggio facilita la trasmissione della liquidità.
- I nodi della rete ricevono una commissione per il loro servizio, costituita da fee fisse e variabili.
- L'Onion Routing consente al nodo di partenza di calcolare il percorso completo senza che i nodi intermedi conoscano l'origine o la destinazione finale.

In questo capitolo, abbiamo esplorato l'instradamento dei pagamenti su Lightning Network. Ma sorge una domanda: cosa impedisce ai nodi intermedi di ricevere un pagamento in entrata senza inoltrarlo alla destinazione successiva, con lo scopo di intercettare la transazione? Questo è precisamente il ruolo degli HTLC che studieremo di seguito.

## HTLC – Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::

Ora scopriremo come il protocollo Lightning Network permette ai pagamenti di transitare attraverso nodi intermedi, senza la necessità di fidarsi di loro, grazie agli **[HTLC](https://planb.academy/resources/glossary/htlc)** (_Hashed Time-Locked Contracts_). Questi smart contract assicurano che ciascun nodo intermedio riceverà i fondi dal suo canale solo se inoltra il pagamento al destinatario finale; in caso contrario, il pagamento non verrà convalidato.

Il problema che sorge per l'instradamento dei pagamenti è quindi la necessaria fiducia nei nodi intermedi e tra gli stessi. Per illustrare meglio, rivediamo il nostro esempio semplificato di una rete composta da 3 nodi e 2 canali:

- Alice ha un canale con Suzie.
- Suzie ha un canale con Bob.

Alice vuole inviare 40.000 satoshi a Bob ma non ha un canale diretto con lui e non desidera aprirne uno. Cerca quindi un percorso e decide di passare attraverso il nodo di Suzie.

![LNP201](assets/en/046.webp)

Se Alice invia ingenuamente 40.000 satoshi a Suzie, sperando che trasferisca la somma a Bob, potrebbe capitare che Suzie tenga i fondi per sé, senza trasmetterli a Bob.

![LNP201](assets/en/047.webp)

Per evitare questa situazione, il protocollo Lightning prevede l'uso di HTLC (Hashed Time-Locked Contracts), che impone delle condizioni di pagamento al nodo intermedio, nel senso che Suzie deve soddisfare determinati vincoli per accedere ai fondi di Alice e trasferirli a Bob.

### Come Funzionano gli HTLC

Un HTLC è un contratto speciale basato su due principi:

- **Condizione di accesso**: il destinatario deve rivelare un segreto per sbloccare il pagamento a lui destinato.
- **Scadenza**: se il pagamento non viene completato integralmente entro un periodo definito, viene annullato e i fondi ritornano al mittente.

Ecco come funziona questo processo nel nostro esempio con Alice, Suzie e Bob:

![LNP201](assets/en/048.webp)

**Creazione del segreto**: Bob genera un segreto casuale che viene denotato con la _s_ (la preimmagine) e calcola il suo hash _r_ con la funzione hash indicata come _h_. Abbiamo:

$$
r = h(s)
$$

L'uso di una funzione hash rende impossibile trovare _s_ avendo solo _h(s)_, ma se viene mostrato _s_, è facile verificare la corrispondenza con _h(s)_.

![LNP201](assets/en/049.webp)

**Invio della richiesta di pagamento**: Bob invia un'**invoice** (richiesta di pagamento) ad Alice. Questa invoice deve includere l'hash _r_.

![LNP201](assets/en/050.webp)

**Invio del pagamento condizionato**: Alice invia un HTLC di 40.000 satoshi a Suzie. La condizione affinché Suzie riceva questi fondi è che fornisca ad Alice un segreto _s'_ che soddisfa la seguente equazione:

$$
h(s') = r
$$

![LNP201](assets/en/051.webp)

**Trasferimento dell'HTLC al destinatario finale**: Suzie, per ottenere i 40.000 satoshi da Alice, deve trasferire a Bob un HTLC simile di 40.000 satoshi e che abbia la medesima condizione, ovvero che deve fornire a Suzie un segreto _s'_ che soddisfi l'equazione:

$$
h(s') = r
$$

![LNP201](assets/en/052.webp)

**Convalida con l'esibizione di _s_**: Bob esibisce _s_ a Suzie per ricevere i 40.000 satoshi promessi nell'HTLC. Con questo segreto Suzie può quindi sbloccare l'HTLC di Alice e ottenere i 40.000 satoshi da Alice. Il pagamento viene quindi correttamente instradato a Bob.

![LNP201](assets/en/053.webp)

Questo processo impedisce a Suzie di trattenere i fondi di Alice senza completare il trasferimento a Bob, poiché deve inviare il pagamento a Bob per ottenere il segreto _s_ e quindi sbloccare l'HTLC di Alice. L'operazione rimane la stessa anche se il percorso include diversi altri nodi intermedi: si ripetono semplicemente i passaggi di Suzie per ognuno di essi. Ogni nodo è protetto dalle condizioni dell'HTLC, perché lo sblocco dell'ultimo HTLC da parte del destinatario attiva automaticamente lo sblocco di tutti gli altri HTLC in cascata.

### Scadenza e gestione degli HTLC in caso di problemi

Se durante il processo di pagamento uno dei nodi intermedi o il nodo destinatario smette di rispondere, per esempio in caso di interruzione di internet o di corrente, allora il pagamento non può essere completato, perché il segreto necessario per sbloccare gli HTLC non viene rivelato. Prendendo il nostro modello con Alice, Suzie e Bob, questo problema si verifica, ad esempio, se Bob non trasmette il segreto _s_ a Suzie. In questo caso, tutti gli HTLC a monte del percorso sono bloccati e, con essi, anche i fondi.

![LNP201](assets/en/054.webp)

Per evitare ciò gli HTLC hanno una scadenza, che consente di rimuovere il timelock se non viene completato entro un certo tempo. La scadenza segue un ordine specifico poiché inizia prima con l'HTLC più vicino al destinatario, per poi risalire progressivamente fino a chi ha emesso il pagamento. Nel nostro esempio, se Bob non dà mai il segreto _s_ a Suzie, ciò farebbe scadere prima l'HTLC di Suzie verso Bob.

![LNP201](assets/en/055.webp)

Poi l'HTLC da Alice a Suzie.

![LNP201](assets/en/056.webp)

Se l'ordine di scadenza fosse invertito, Alice potrebbe recuperare il suo pagamento prima che Suzie possa proteggersi da potenziali truffe. Se infatti Bob tornasse (online) a reclamare il suo HTLC mentre Alice ha già rimosso il proprio, Suzie sarebbe in condizione di svantaggio. L'ordine di scadenza degli HTLC in cascata, assicura quindi che nessun nodo intermedio subisca perdite ingiuste.

### Come le commitment transaction integrano le condizioni degli HTLC

Le commitment transaction integrano gli HTLC in modo tale che, le condizioni che l'HTLC impone su Lightning possano essere trasferite onchain in caso di chiusura forzata del canale, quando l'HTLC è ancora attivo. Ricordiamo che le commitment transaction riflettono lo stato attuale del canale tra i due utenti e consentono la chiusura forzata unilaterale in caso di problemi. Con ogni nuovo stato del canale vengono create 2 commitment transaction: una per ciascuna parte. Utilizziamo di nuovo l'esempio con Alice, Suzie e Bob, ma guardiamo più da vicino cosa succede a livello di canale tra Alice e Suzie quando viene creato l'HTLC.

![LNP201](assets/en/057.webp)

Prima che Alice invii 40.000 satoshi a Bob, Alice ha 100.000 satoshi nel suo canale con Suzie, mentre Suzie ne detiene 30.000. Le loro commitment transaction sono le seguenti:

![LNP201](assets/en/058.webp)

Quando Alice riceve l'invoice da Bob, quest'ultima contiene anche _r_, l'hash del segreto. Alice può quindi generare un HTLC di 40.000 satoshi con Suzie. Nelle ultime commitment transaction, questo HTLC viene indicato come output, chiamato "**_HTLC Out_**" dal lato di Alice poiché i fondi sono in uscita. Lo stesso è invece chiamato "**_HTLC In_**" dal lato di Suzie, poiché i fondi sono in entrata.

![LNP201](assets/en/059.webp)

Questi output associati all'HTLC condividono esattamente le stesse condizioni, ovvero:

- Se Suzie è in grado di fornire il segreto _s_, può sbloccare immediatamente questo output e trasferirlo a un indirizzo sotto il suo controllo.
- Se Suzie non possiede il segreto _s_, non può sbloccare questo output. Alice sarà in grado di sbloccarlo dopo la scadenza del timelock, per inviarlo a un proprio indirizzo. Il timelock, quindi, concede a Suzie un periodo di tempo per tornare su Lightning e mostrare che in effetti possiede il segreto _s_.

Le condizioni appena spiegate si applicano solo se il canale viene chiuso mentre l'HTLC Lightning è ancora attivo (cioè, la commitment transaction viene pubblicata sulla blockchain). Ciò significa che il pagamento tra Alice e Bob non è ancora stato finalizzato, ma gli HTLC non sono ancora scaduti. Grazie a queste condizioni, Suzie può fornire _s_ e recuperare i 40.000 satoshi dell'HTLC. In caso contrario Alice recupera i fondi dopo la scadenza del timelock perché, se Suzie non conosce _s_, significa che non ha trasferito i 40.000 satoshi a Bob e quindi non può trattenere i fondi di Alice.

Inoltre, se il canale viene chiuso mentre diversi HTLC sono ancora in sospeso, ci saranno tanti output aggiuntivi quanti sono gli HTLC in corso. Se il canale non viene chiuso allora, dopo la scadenza del timelock o la riuscita del pagamento Lightning, vengono create nuove commitment transaction per riflettere il nuovo stato del canale (ora stabile), cioè senza HTLC in sospeso. Gli output relativi agli HTLC possono quindi essere rimossi dalle commitment transaction.

![LNP201](assets/en/060.webp)

Infine, nel caso di una chiusura cooperativa del canale mentre un HTLC è attivo, Alice e Suzie smettono di accettare nuovi pagamenti e attendono la risoluzione o la scadenza degli HTLC in corso. Ciò consente loro di pubblicare una transazione di chiusura più leggera, senza gli output relativi agli HTLC, riducendo così le fee ed evitando l'attesa per un possibile timelock.

**Quali insegnamenti puoi trarre da questo capitolo?**

Gli HTLC consentono il routing dei pagamenti Lightning attraverso più nodi senza dover porre fiducia in loro. Ecco i punti chiave da ricordare:

- Gli HTLC garantiscono la sicurezza dei pagamenti attraverso un segreto (preimage) e una durata massima fissata nel tempo.
- La risoluzione o la scadenza degli HTLC segue un ordine specifico: inizia dalla destinazione per risalire alla fonte del pagamento, al fine di proteggere ogni nodo intermedio.
- Finché un HTLC non è risolto o scaduto, viene mantenuto come output nelle commitment transaction più recenti.

Nel prossimo capitolo, scopriremo come un nodo che deve trasmettere un pagamento Lightning, trova e seleziona il percorso affinché il suo pagamento possa raggiungere il nodo destinatario.

## Trovare il percorso

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::

Nei capitoli precedenti abbiamo visto come utilizzare i canali di altri nodi per instradare i pagamenti e raggiungere un nodo senza essere direttamente connessi ad esso. Abbiamo anche discusso su come è garantita la sicurezza del trasferimento senza bisogno di porre fiducia nei nodi intermedi. Nel nuovo capitolo ci concentreremo su come trovare il routing migliore possibile per raggiungere il nodo di destinazione.

### Il Problema del Routing su Lightning

Come abbiamo visto, nel protocollo Lightning è il nodo che invia il pagamento a dover calcolare l'intero percorso verso il destinatario, perché utilizziamo un sistema di routing onion. I nodi intermedi non conoscono né il punto di origine né la destinazione finale, sanno solo da dove proviene il pagamento e verso quale nodo devono trasferirlo. Ciò significa che il nodo mittente deve mantenere in locale una topologia dinamica della rete, che comprenda tutti i nodi esistenti e i canali tra ciascuno, che tenga conto delle aperture, delle chiusure e degli aggiornamenti di stato.

![LNP201](assets/en/061.webp)

Anche conoscendo la topologia della rete, ci sono informazioni essenziali per il routing che rimangono inaccessibili al nodo mittente, come la distribuzione esatta della liquidità nei canali in un dato momento. Ogni canale mostra infatti solo la sua **capacità totale**, ma la distribuzione interna dei fondi è nota solo ai due nodi partecipanti. Questo pone sfide per un routing efficiente, poiché il successo del pagamento dipende principalmente dal fatto che l'importo sia inferiore alla liquidità più bassa presente sul percorso scelto. Tuttavia queste informazioni non sono tutte disponibili per il nodo mittente.

![LNP201](assets/en/062.webp)

### Aggiornamento della Mappa della Rete

Per mantenere aggiornata la loro mappa della rete, i nodi scambiano regolarmente messaggi attraverso un algoritmo chiamato "**_gossip_**". Si tratta di un algoritmo distribuito, utilizzato per diffondere informazioni che i nodi propagano l'uno all'altro e che consente lo scambio e la sincronizzazione dello stato globale dei canali in pochi cicli di comunicazione. Ogni nodo propaga le informazioni a uno o più nodi vicini, scelti a caso o meno; questi ultimi, a loro volta, propagano le informazioni ad altri vicini e così via fino a raggiungere uno stato globale di sincronizzazione.

I due messaggi principali scambiati tra i nodi Lightning sono i seguenti:

- "**Annuncio del Canale**": messaggi che segnalano l'apertura di un nuovo canale.
- "**Aggiornamenti del Canale**": messaggi di aggiornamento sullo stato di un canale, in particolare sull'evoluzione delle fee (ma non sulla distribuzione della liquidità).

I nodi Lightning monitorano anche la blockchain di Bitcoin per rilevare le transazioni di chiusura di un determinato canale. Il canale chiuso viene quindi rimosso dalla mappa, poiché non può più essere utilizzato per instradare pagamenti.

### Instradare un Pagamento

Prendiamo l'esempio di una piccola Rete Lightning con 7 nodi: Alice, Bob, 1, 2, 3, 4 e 5, immaginando che Alice voglia inviare un pagamento a Bob ma debba passare attraverso nodi intermedi.

![LNP201](assets/en/063.webp)

Ecco la distribuzione attuale dei fondi in questi canali:

- **Canale tra Alice e 1**: 250.000 sats dal lato di Alice, 80.000 dal lato di 1 (capacità totale di 330.000 sats).
- **Canale tra 1 e 2**: 300.000 sats dal lato di 1, 200.000 dal lato di 2 (capacità totale di 500.000 sats).
- **Canale tra 2 e 3**: 50.000 sats dal lato di 2, 60.000 dal lato di 3 (capacità totale di 110.000 sats).
- **Canale tra 2 e 5**: 90.000 sats dal lato di 2, 160.000 dal lato di 5 (capacità totale di 250.000 sats).
- **Canale tra 2 e 4**: 180.000 sats dal lato di 2, 110.000 dal lato di 4 (capacità totale di 290.000 sats).
- **Canale tra 4 e 5**: 200.000 sats dal lato di 4, 10.000 dal lato di 5 (capacità totale di 210.000 sats).
- **Canale tra 3 e Bob**: 50.000 sats dal lato di 3, 250.000 dal lato di Bob (capacità totale di 300.000 sats).
- **Canale tra 5 e Bob**: 260.000 sats dal lato di 5, 100.000 dal lato di Bob (capacità totale di 360.000 sats).

![LNP201](assets/en/064.webp)

Per instradare un pagamento di 100.000 sats da Alice a Bob, le opzioni di routing sono limitate dalla liquidità disponibile in ciascun canale. Il percorso ottimale per Alice, basato sulla distribuzione conosciuta della liquidità, potrebbe essere la sequenza `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/065.webp)

Poiché Alice non conosce la distribuzione esatta dei fondi in ciascun canale, deve stimare il percorso ottimale basandosi sulle possibilità, tenendo conto dei seguenti criteri:

- **Probabilità di successo**: un canale con una capacità totale superiore all'importo da instradare, ha maggiori probabilità di contenere sufficiente liquidità. Ad esempio, il canale tra il nodo 2 e il nodo 3 ha una capacità totale di 110.000 sats; è quindi improbabile trovare 100.000 sats o più dal lato del nodo 2, anche se rimane possibile.
- **Fee di transazione**: nella scelta del percorso migliore, il nodo mittente considera anche le fee applicate da ciascun nodo intermedio e cerca di minimizzare il costo totale per l'instradamento.
- **Scadenza degli HTLC**: il tempo di scadenza degli HTLC è un parametro da considerare, per evitare che i pagamenti restino bloccati.
- **Numero di nodi intermedi**: infine e più in generale, il nodo mittente cercherà di trovare un percorso con il minor numero possibile di nodi intermedi, per ridurre il rischio di fallimento e limitare le fee.
  
Analizzando questi criteri, il nodo mittente può testare i percorsi più probabili e tentare di ottimizzarli. Nel nostro esempio, Alice potrebbe classificare le migliori rotte come segue:

- `Alice → 1 → 2 → 5 → Bob`, perché è la rotta più breve con la capacità più alta.
- `Alice → 1 → 2 → 4 → 5 → Bob`, perché questa rotta offre buone capacità, anche se è più lunga della prima.
- `Alice → 1 → 2 → 3 → Bob`, perché questa rotta include il canale `2 → 3`, che ha una capacità molto limitata, ma rimane potenzialmente utilizzabile.

### Esecuzione del Pagamento

Alice decide di testare la sua prima rotta (`Alice → 1 → 2 → 5 → Bob`). Invia quindi un HTLC di 100.000 sats al nodo 1. Questo nodo verifica di avere sufficiente liquidità con il nodo 2 e inoltra la trasmissione. Il nodo 2 riceve l'HTLC dal nodo 1, ma si rende conto di non avere abbastanza liquidità nel suo canale con il nodo 5 per instradare un pagamento di 100.000 sats. Invia quindi un messaggio di errore al nodo 1, che lo trasmette ad Alice. Questo routing fallisce.

![LNP201](assets/en/066.webp)

Alice tenta quindi di instradare il suo pagamento utilizzando la sua seconda opzione (`Alice → 1 → 2 → 4 → 5 → Bob`). Invia un HTLC di 100.000 sats al nodo 1, che lo trasmette al nodo 2, poi al nodo 4, al nodo 5 e infine a Bob. Questa volta la liquidità è sufficiente e il routing è funzionale. Ogni nodo sblocca il suo HTLC in cascata utilizzando la preimage fornita da Bob (il segreto _s_), che consente di finalizzare con successo il pagamento da Alice a Bob.

![LNP201](assets/en/067.webp)

La ricerca di un instradamento viene condotta come segue: il nodo mittente inizia identificando i percorsi migliori possibili, poi tenta i pagamenti in successione tra questi percorsi, fino a trovare il routing che funziona.

È importante notare che Bob può fornire ad Alice informazioni nell'**invoice** per facilitare l'instradamento. Ad esempio indicando i canali vicini con sufficiente liquidità o rivelare l'esistenza di canali privati. Queste indicazioni permettono ad Alice di evitare percorsi con poche possibilità di successo e di tentare per primi quelli raccomandati da Bob.

**Quali insegnamenti puoi trarre da questo capitolo?**

- I nodi mantengono una mappa della topologia della rete attraverso annunci e monitorando le chiusure dei canali sulla blockchain di Bitcoin.
- La ricerca di un instradamento ottimale per un pagamento è basata sulle probabilità e dipende da molti criteri.
- Con la sua invoice, Bob può fornire informazioni per guidare l'instradamento di Alice, evitandole di testare percorsi improbabili.

Nel capitolo seguente studieremo nello specifico il funzionamento delle invoice, oltre ad alcuni altri strumenti utilizzati sul Lightning Network.

# Strumenti Lightning Network

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Invoice, LNURL e Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::

In questo capitolo esamineremo più da vicino il funzionamento delle **invoice** Lightning Network, ovvero le richieste di pagamento inviate dal nodo che riceve al nodo che paga. L'obiettivo è capire come inviare e ricevere pagamenti tramite Lightning Network. Discuteremo anche di 2 alternative alle classiche invoice: LNURL e Keysend.

![LNP201](assets/en/068.webp)

### La Struttura delle Invoice Lightning

Come spiegato nel capitolo sugli HTLC, ogni pagamento inizia con la generazione di un'**invoice** da parte del destinatario. Questa viene poi trasmessa a chi deve pagarla (tramite un codice QR o copiando e incollando) per avviare il processo. Un'invoice consiste di due parti principali:

- **Una Parte Leggibile dall'uomo**: sezione che contiene metadati chiaramente distinguibili e che migliorano l'esperienza utente.
- **Payload**: che include informazioni destinate alle macchine per elaborare il pagamento.

La struttura tipica di un'invoice inizia con un identificatore `ln` che sta per "Lightning", seguito da `bc` per Bitcoin, poi l'importo dell'invoice. Un separatore `1` distingue la parte leggibile dall'uomo dalla parte dei dati destinati alle macchine (payload).

Prendiamo come esempio la seguente invoice:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Possiamo già dividerla in 2 parti. Prima, c'è la parte leggibile:

```invoice
lnbc100u
```

Poi la parte destinata al payload:

```invoice
p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Le due parti sono separate da un `1`. Questo separatore è stato scelto invece di un carattere speciale per permettere un facile copia-incolla dell'intera invoice con un doppio clic.
Nella prima parte, possiamo vedere che:

- `ln` indica che si tratta di una richiesta di pagamento Lightning.
- `bc` indica che la rete Lightning è sulla blockchain di Bitcoin (e non sulla testnet o su Litecoin).
- `100u` indica l'importo dell'invoice, espresso in **microbitcoin** (`u` che significa "micro"), che qui equivale a 10.000 sats.

Per designare l'importo del pagamento, questo è espresso in sotto-unità di bitcoin. Ecco quelle utilizzate:

- **Millibitcoin (denotato `m`):** Rappresenta un millesimo di bitcoin.

$$
1 \text{ mBTC} = 10^{-3} \text{ BTC} = 10^5 \text{ satoshi}
$$

- **Microbitcoin (denotato `u`):** talvolta chiamato "bit", rappresenta un milionesimo di bitcoin.

$$
1 \ \mu\text{BTC} = 10^{-6} \text{ BTC} = 100 \text{ satoshi}
$$

- **Nanobitcoin (denotato `n`):** Rappresenta un miliardesimo di bitcoin.

$$
1 \text{ nBTC} = 10^{-9} \text{ BTC} = 0.1 \text{ satoshi}
$$

- **Picobitcoin (denotato `p`):** Rappresenta un trilionesimo di bitcoin.

$$
1 \text{ pBTC} = 10^{-12} \text{ BTC} = 0.0001 \text{ satoshi}
$$

### Il Payload di un'invoice

Il payload di un'invoice include diverse informazioni necessarie per l'elaborazione del pagamento:

- **Il timestamp:** il momento della creazione dell'invoice espresso in Unix Timestamp (il numero di secondi trascorsi dal 1 gennaio 1970).
- **Hash del Segreto**: come abbiamo visto nella sezione sugli HTLC, il nodo che richiede il pagamento deve fornire al nodo mittente l'hash della preimage. Questo viene utilizzato negli HTLC per garantire il pagamento. Lo abbiamo definito "_r_".
- **Il Segreto del Pagamento**: un altro segreto generato dal destinatario, trasmesso solo al nodo mittente. Viene utilizzato nel routing onion per impedire ai nodi intermedi di indovinare se il nodo successivo sia il destinatario finale o meno. Questo segreto mantiene quindi una forma di confidenzialità per il destinatario, rispetto all'ultimo nodo intermedio sul percorso.
- **La Chiave Pubblica del Destinatario**: indica a chi paga come identificare la persona da pagare.
- **La Durata prima della Scadenza**: il tempo massimo affinché l'invoice venga pagata (1 ora per impostazione predefinita).
- **Suggerimenti di Routing**: informazioni aggiuntive fornite dal destinatario per aiutare il mittente a ottimizzare il percorso di pagamento.
- **La Firma**: garantisce l'integrità dell'invoice autenticando tutte le informazioni.

Le richieste di pagamento vengono poi codificate in **bech32**, lo stesso formato utilizzato per gli indirizzi Bitcoin SegWit (formato che inizia con `bc1`).

### LNURL Withdrawal

In un pagamento tradizionale, come un acquisto in negozio, viene generata un'invoice per l'importo totale da pagare. Una volta presentata l'invoice (sotto forma di codice QR o stringa di caratteri), il cliente può scansionarla e finalizzare la transazione. Il pagamento segue quindi il consueto processo che abbiamo studiato nella sezione precedente. Questo processo può talvolta essere molto ingombrante sotto il profilo dell'esperienza utente, poiché richiede al destinatario di inviare informazioni al mittente tramite invoice.

Per certe situazioni, come il prelievo di bitcoin da un servizio online, il processo tradizionale è troppo scomodo. In tali casi la soluzione offerta da **LNURL Whithdrawal** (una sorta di prelievo automatico) semplifica questo processo, visualizzando un codice QR che il wallet del destinatario scansiona per creare automaticamente l'invoice. Il servizio paga quindi l'invoice e l'utente vede semplicemente un prelievo istantaneo.

![LNP201](assets/en/069.webp)

LNURL è un protocollo di comunicazione che specifica un insieme di funzionalità, progettate per semplificare le interazioni tra nodi Lightning e client, così come applicazioni di terze parti. LNURL Withdrawal, come abbiamo appena visto, è solo un esempio tra altre funzionalità.
Questo protocollo si basa su HTTP e consente la creazione di link per varie operazioni, come una richiesta di pagamento, una richiesta di prelievo o altre funzionalità che migliorano l'esperienza utente. Ogni LNURL è un URL codificato in bech32 con il prefisso `lnurl` che, una volta scansionato, innesca una serie di azioni automatiche sul wallet Lightning.
Ad esempio, la funzionalità LNURL-withdraw (LUD-03) consente di prelevare fondi da un servizio scansionando un codice QR, senza la necessità di generare manualmente un'invoice. Allo stesso modo, LNURL-auth (LUD-04) consente l'accesso a servizi online utilizzando una chiave privata del proprio wallet Lightning invece di una password.

### Inviare un pagamento Lightning senza invoice: Keysend

Un altro caso interessante è il trasferimento di fondi senza aver ricevuto un'invoice in precedenza, noto come "**Keysend**". Questo protocollo consente di inviare fondi aggiungendo un preimage nei dati di pagamento crittografati, accessibile solo dal destinatario. Questa preimage consente al destinatario di sbloccare l'HTLC, recuperando così i fondi senza aver generato un'invoice in precedenza.

Per semplificare: in questo protocollo è il mittente a generare il segreto utilizzato negli HTLC, anziché il destinatario. Il Keysend consente al mittente di effettuare un pagamento senza aver dovuto interagire con il destinatario in precedenza.

![LNP201](assets/en/070.webp)

**Quali insegnamenti puoi trarre da questo capitolo?**

- Un'**invoice Lightning** è una richiesta di pagamento composta da una parte leggibile dall'uomo e una parte di dati riservati alla macchina.
- L'invoice è codificata in **bech32**, con un separatore `1` per facilitarne la copia, nonché una parte dati contenente tutte le informazioni necessarie per elaborare il pagamento.
- Esistono altri processi di pagamento Lightning, in particolare **LNURL-Withdraw** per facilitare i prelievi, e **Keysend** per trasferimenti diretti senza invoice.

Nel capitolo seguente, vedremo come l'operatore di nodo può gestire la liquidità nei propri canali, per non rimanere mai bloccato e essere sempre in grado di inviare e ricevere pagamenti sulla rete Lightning.

## Gestire la Tua Liquidità

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>
:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::

In questo capitolo esploreremo strategie per gestire efficacemente la liquidità di un canale Lightning Network. La gestione della liquidità varia a seconda del tipo di utente e del contesto. Esamineremo i principi essenziali e le tecniche esistenti per capire meglio come ottimizzare questa gestione.

### Esigenze di Liquidità

Ci sono tre profili principali di utenti Lightning, ognuno con specifiche esigenze di liquidità:

- **Chi paga**: colui che effettua pagamenti. Ha bisogno di liquidità in uscita per poter trasferire fondi ad altri utenti. Potrebbe trattarsi, ad esempio, di un consumatore.
- **Chi vende (o Beneficiario)**: colui che riceve pagamenti. Ha bisogno di liquidità in entrata per poter accettare pagamenti al suo nodo. Potrebbe trattarsi di un'attività commerciale o di un negozio online.
- **Il nodo intermedio**: spesso specializzato nel routing dei pagamenti, che deve ottimizzare la sua liquidità in ogni canale per instradare quanti più pagamenti possibile e guadagnare fee.

Questi profili ovviamente non sono fissi; un utente può passare da pagante a beneficiario a seconda delle situazioni. Bob potrebbe ad esempio ricevere il suo stipendio dal suo datore di lavoro via Lightning Network, ponendosi nella posizione di un "venditore" che ha bisogno di liquidità in entrata. Successivamente, se vuole usare il suo stipendio per comprare cibo, diventa "chi paga" e deve quindi avere liquidità in uscita.

Per capire meglio prendiamo l'esempio di una semplice rete composta da tre nodi: l'acquirente (Alice), il nodo intermedio (Suzie) e il venditore (Bob).

![LNP201](assets/en/071.webp)

Immagina che l'acquirente voglia inviare 30.000 satoshi al venditore e che il pagamento passi attraverso il nodo di routing. Ogni parte deve quindi avere una quantità minima di liquidità nella direzione del pagamento:

- Chi paga deve avere almeno 30.000 satoshi dalla sua parte del canale con il nodo intermedio di routing.
- Il venditore deve avere un canale in cui 30.000 satoshi sono dalla parte opposta, per poterli ricevere.
- Il nodo di routing deve avere 30.000 satoshi dalla parte di chi paga, ma anche 30.000 satoshi dalla sua parte nel canale con il venditore, per poter instradare il pagamento.

![LNP201](assets/en/072.webp)

### Strategie di Gestione della Liquidità

Chi paga assicurarsi di mantenere sufficiente liquidità dalla sua parte dei canali, per garantire i fondi in uscita. Questo si rivela relativamente semplice, poiché è sufficiente aprire nuovi canali per avere tale liquidità: i fondi bloccati nel multisig on-chain sono, all'inizio, interamente dalla parte del canale di chi svolge la funzione di pagante. La capacità di pagamento è quindi assicurata finché vengono aperti canali con fondi sufficienti. Quando la liquidità in uscita è esaurita, è sufficiente aprire nuovi canali.
Per il venditore, invece, il compito è più complesso. Per poter ricevere pagamenti deve avere liquidità dalla parte opposta dei suoi canali. Pertanto, aprire un canale non è sufficiente: deve anche effettuare un pagamento in questo canale per spostare la liquidità dall'altra parte prima di poter ricevere pagamenti. Per certi profili di utenti Lightning, come i commercianti, esiste un netto squilibrio tra ciò che il loro nodo invia e ciò che riceve, poiché l'obiettivo di un'attività commerciale è principalmente quello di incassare più di quanto spende, al fine di generare un profitto. Fortunatamente esistono diverse soluzioni per questi utenti con specifiche esigenze di liquidità in entrata:

- **Attirare canali**: il commerciante beneficia di un vantaggio dovuto al volume di pagamenti in entrata previsti sul suo nodo. Tenendo conto di ciò, può cercare di attirare nodi interessati al routing che sono alla ricerca di entrate dalle fee associate e che potrebbero aprire canali verso di loro, sperando così che instradino i loro pagamenti e riscuotere le fee associate.

- **Spostare liquidità**: il venditore può anche aprire un canale e trasferire parte dei fondi verso il lato opposto, effettuando pagamenti fittizi verso un altro nodo, che restituirà il denaro in un altro modo. Vedremo nella prossima parte come effettuare queste operazioni.

- **Triangolazione di canali**: esistono piattaforme per i nodi che desiderano aprire canali in modo collaborativo, consentendo a ciascuno di beneficiare subito di liquidità in entrata e in uscita. [LightningNetwork+](https://lightningnetwork.plus/), ad esempio, offre questo servizio. Se Alice, Bob e Suzie vogliono aprire un canale con 100.000 sats, possono accordarsi su questa piattaforma affinché Alice apra un canale verso Bob, Bob verso Suzie e Suzie verso Alice. In questo modo ciascuno ha 100.000 sats di liquidità in uscita e 100.000 sats di liquidità in entrata, bloccando solo 100.000 sats a testa.

![LNP201](assets/en/073.webp)

- **Acquisto di canali**: esistono anche servizi che affittano canali Lightning per ottenere liquidità in entrata, come [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) o [Lightning Labs Pool](https://lightning.engineering/pool/). Alice può acquistare un canale di un milione di satoshi verso il suo nodo per poter ricevere pagamenti.

![LNP201](assets/en/074.webp)

Infine, per i nodi di routing che hanno come obiettivo quello di massimizzare il numero di pagamenti elaborati e le fee raccolte, è necessario:

- Aprire canali ben finanziati con nodi strategici.
- Bilanciare regolarmente la distribuzione dei fondi nei canali, secondo le necessità della rete.

### Il servizio Loop Out

Il servizio [Loop Out](https://lightning.engineering/loop/), offerto da Lightning Labs, consente di spostare la liquidità verso il lato opposto del canale recuperando i fondi onchain. Alice invia per esempio 1 milione di satoshi tramite Lightning a un nodo loop, che poi le restituisce quei fondi come bitcoin on-chain. Questo bilancia il suo canale con 1 milione di satoshi su ciascun lato, ottimizzando la sua capacità di ricevere pagamenti.

![LNP201](assets/en/075.webp)

Un servizio come Loop Out consente pertanto di ottenere liquidità in entrata recuperando i propri bitcoin on-chain, il che aiuta a limitare l'immobilizzazione di fondi necessaria per accettare pagamenti Lightning.


**Quali insegnamenti puoi trarre da questo capitolo?**

- Per inviare pagamenti Lightning, devi avere abbastanza liquidità dal tuo lato dei canali. Per aumentare questa capacità di invio basta aprire nuovi canali.
- Per ricevere pagamenti, è necessario avere liquidità sul lato opposto nei tuoi canali. Aumentare questa capacità di ricezione è più complesso, poiché richiede che altri aprano canali verso di te o che effettuino pagamenti (fittizi o reali) per spostare la liquidità dall'altro lato.
- Mantenere la liquidità desiderata può rivelarsi una sfida ancor più difficile, a seconda dell'uso dei canali. Ecco perché esistono strumenti e servizi per aiutare a bilanciare i canali come desiderato.

Nel prossimo capitolo propongo di rivedere i concetti più importanti di questa formazione.

# Vai oltre

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Riassunto del corso


<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>
:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::

In questo capitolo finale che segna la conclusione del corso LNP201, propongo di rivedere insieme i concetti importanti che abbiamo trattato.

L'obiettivo di questo corso era fornirti una comprensione chiara e tecnica di Lightning Network. Abbiamo scoperto come Lightning Network si basi sulla blockchain di Bitcoin per eseguire transazioni off-chain, mantenendo al contempo le caratteristiche fondamentali di Bitcoin, in particolare l'assenza della necessità di fiducia negli altri nodi.

### Canali di Pagamento

Nei capitoli iniziali abbiamo esplorato come due parti, aprendo un canale di pagamento, possano effettuare transazioni al di fuori della blockchain. Ecco i passaggi trattati:

- **Apertura del Canale**: la creazione del canale avviene tramite una transazione onchain che blocca i fondi in un indirizzo multi-firma 2/2. Questo deposito rappresenta il canale Lightning sulla blockchain.

![LNP201](assets/en/076.webp)

- **Transazioni nel Canale**: nel canale Lightning Network è quindi possibile effettuare numerose transazioni, senza doverle pubblicare sulla blockchain. Ogni transazione Lightning crea un nuovo stato del canale che è espresso in una commitment transaction.

![LNP201](assets/en/077.webp)

- **Sicurezza e Chiusura**: i partecipanti si affidano al nuovo stato del canale e si scambiano le revocation keys, per assicurare i fondi e prevenire eventuali frodi. Entrambe le parti possono chiudere il canale in maniera cooperativa, effettuando una nuova transazione sulla blockchain di Bitcoin oppure, come ultima risorsa, attraverso una chiusura forzata. Quest'ultima opzione, sebbene meno efficiente perché più lunga e talvolta non ottimizzata in termini di fee, consente comunque il recupero dei fondi. In caso di frode la vittima può punire il truffatore recuperando tutti i fondi del canale, direttamente onchain.

![LNP201](assets/en/078.webp)

### Una Rete di Canali

Dopo aver studiato i canali isolati, abbiamo esteso l'analisi alla rete di canali:

- **Routing**: quando due parti non sono direttamente collegate da un canale, la rete consente il routing attraverso nodi intermediari. I pagamenti transitano quindi da un nodo all'altro.

![LNP201](assets/en/079.webp)

- **HTLCs**: i pagamenti instradati attraverso nodi di routing sono assicurati da "_Hash Time-Locked Contracts_" (HTLC), che consentono di bloccare i fondi fino a che il pagamento non si completa da mittente a beneficiario.

![LNP201](assets/en/080.webp)

- **Onion Routing**: Per garantire confidenzialità nel pagamento, l'onion routing maschera la destinazione finale ai nodi intermediari. Il nodo mittente deve quindi calcolare l'intero percorso ma, in assenza di informazioni complete sulla liquidità dei canali, procede attraverso tentativi successivi per instradare il pagamento.

![LNP201](assets/en/081.webp)

### Gestione della Liquidità

Abbiamo visto che la gestione della liquidità su Lightning Network, è una sfida per garantire il regolare flusso dei pagamenti. Inviare pagamenti è relativamente semplice: basta aprire un canale. Tuttavia, ricevere pagamenti richiede di avere liquidità sul lato opposto dei propri canali. Ecco alcune strategie discusse:

- **Attirare Canali**: incoraggiando altri nodi ad aprire canali verso di sé, un utente ottiene liquidità in entrata.

- **Spostare Liquidità**: inviando pagamenti ad altri canali, la liquidità si sposta sul lato opposto.

![LNP201](assets/en/082.webp)

- **Utilizzare Servizi come Loop e Pool**: questi servizi consentono di riequilibrare o acquistare canali con liquidità sul lato opposto.

  ![LNP201](assets/en/083.webp)
  
- **Aperture Collaborative**: esistono poi piattaforme accessibili per connettersi con altri nodi, al fine di eseguire triangolazioni (aperture collaborative tra più nodi) e avere liquidità in entrata.

![LNP201](assets/en/084.webp)

# Sezione finale

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Recensioni & Valutazioni

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Esame finale

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusione

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
<isCourseConclusion>true</isCourseConclusion>