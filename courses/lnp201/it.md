---
name: Introduzione Teorica alla Lightning Network
goal: Scoprire la Lightning Network da una prospettiva tecnica
objectives:
  - Comprendere il funzionamento dei canali della rete.
  - Familiarizzare con i termini HTLC, LNURL e UTXO.
  - Assimilare la gestione della liquidità e le commissioni della LNN.
  - Riconoscere la Lightning Network come una rete.
  - Comprendere gli usi teorici della Lightning Network.
---

# Un Viaggio nel Secondo Strato di Bitcoin

Immergiti nel cuore della Lightning Network, un sistema essenziale per il futuro delle transazioni Bitcoin. LNP201 è un corso teorico sul funzionamento tecnico della Lightning. Rivela le fondamenta e i meccanismi di questa rete di secondo livello, progettata per rendere i pagamenti Bitcoin veloci, economici e scalabili.

Grazie alla sua rete di canali di pagamento, Lightning consente transazioni rapide e sicure senza registrare ogni scambio sulla blockchain di Bitcoin. Nei vari capitoli, imparerai come funzionano l'apertura, la gestione e la chiusura dei canali, come i pagamenti vengono instradati attraverso nodi intermedi in modo sicuro minimizzando la necessità di fiducia, e come gestire la liquidità. Scoprirai cosa sono le transazioni di impegno, gli HTLC, le chiavi di revoca, i meccanismi di punizione, il routing a cipolla e le fatture.

Sia che tu sia un principiante di Bitcoin o un utente più esperto, questo corso fornirà informazioni preziose per comprendere e utilizzare la Lightning Network. Anche se copriremo alcuni fondamenti del funzionamento di Bitcoin nelle prime parti, è essenziale padroneggiare le basi dell'invenzione di Satoshi prima di immergersi in LNP201.

Buona scoperta!

+++

# I Fondamenti

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Comprendere la Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Comprendere la Lightning Network](https://youtu.be/PszWk046x-I)

Benvenuto al corso LNP201, che mira a spiegare il funzionamento tecnico della Lightning Network.

La Lightning Network è una rete di canali di pagamento costruita sopra il protocollo Bitcoin, con l'obiettivo di abilitare transazioni veloci e a basso costo. Consente la creazione di canali di pagamento tra i partecipanti, all'interno dei quali le transazioni possono essere effettuate quasi istantaneamente e con commissioni minime, senza dover registrare ogni transazione individualmente sulla blockchain. Così, la Lightning Network cerca di migliorare la scalabilità di Bitcoin e renderlo utilizzabile per pagamenti di basso valore.

Prima di esplorare l'aspetto "rete", è importante comprendere il concetto di **canale di pagamento** su Lightning, come funziona e le sue specificità. Questo è l'argomento di questo primo capitolo.

### Il Concetto di Canale di Pagamento

Un canale di pagamento consente a due parti, qui **Alice** e **Bob**, di scambiare fondi sulla Lightning Network. Ogni protagonista ha un nodo, simboleggiato da un cerchio, e il canale tra loro è rappresentato da un segmento di linea.

![LNP201](assets/en/01.webp)

Nel nostro esempio, Alice ha 100.000 satoshi dalla sua parte del canale, e Bob ne ha 30.000, per un totale di 130.000 satoshi, che costituisce la **capacità del canale**.

**Ma cos'è un satoshi?**

Il **satoshi** (o "sat") è un'unità di conto su Bitcoin. Simile a un centesimo per l'euro, un satoshi è semplicemente una frazione di Bitcoin. Un satoshi equivale a **0,00000001 Bitcoin**, ovvero un centomilionesimo di Bitcoin. Utilizzare il satoshi diventa sempre più pratico man mano che il valore di Bitcoin aumenta.

### L'Assegnazione dei Fondi nel Canale

Ritorniamo al canale di pagamento. Il concetto chiave qui è il "**lato del canale**". Ogni partecipante ha fondi sul proprio lato del canale: Alice 100.000 satoshi e Bob 30.000. Come abbiamo visto, la somma di questi fondi rappresenta la capacità totale del canale, una cifra stabilita al momento della sua apertura.

![LNP201](assets/en/02.webp)

Prendiamo l'esempio di una transazione Lightning. Se Alice vuole inviare 40.000 satoshi a Bob, ciò è possibile perché lei ha fondi sufficienti (100.000 satoshi). Dopo questa transazione, Alice avrà 60.000 satoshi dal suo lato e Bob 70.000.

![LNP201](assets/en/03.webp)

La **capacità del canale**, fissata a 130.000 satoshi, rimane costante. Ciò che cambia è l'allocazione dei fondi. Questo sistema non permette di inviare più fondi di quanti se ne possiedano. Ad esempio, se Bob volesse rispedire 80.000 satoshi ad Alice, non potrebbe, perché ha solo 70.000.

Un altro modo per immaginare l'allocazione dei fondi è pensare a uno **scorrimento** che indica dove si trovano i fondi nel canale. Inizialmente, con 100.000 satoshi per Alice e 30.000 per Bob, lo scorrimento è logicamente dal lato di Alice. Dopo la transazione di 40.000 satoshi, lo scorrimento si muoverà leggermente verso il lato di Bob, che ora ha 70.000 satoshi.

![LNP201](assets/en/04.webp)

Questa rappresentazione può essere utile per immaginare il bilancio dei fondi in un canale.

### Le Regole Fondamentali di un Canale di Pagamento

Il primo punto da ricordare è che la **capacità del canale** è fissa. È un po' come il diametro di un tubo: determina la quantità massima di fondi che possono essere inviati attraverso il canale in una sola volta.
Prendiamo un esempio: se Alice ha 130.000 satoshi dal suo lato, può inviare al massimo 130.000 satoshi a Bob in una singola transazione. Tuttavia, Bob può poi rispedire questi fondi ad Alice, in parte o interamente.

Ciò che è importante capire è che la capacità fissa del canale limita l'importo massimo di una singola transazione, ma non il numero totale di transazioni possibili, né il volume complessivo dei fondi scambiati all'interno del canale.

**Cosa dovresti ricavare da questo capitolo?**

- La capacità di un canale è fissa e determina l'importo massimo che può essere inviato in una singola transazione.
- I fondi in un canale sono distribuiti tra i due partecipanti, e ciascuno può inviare all'altro solo i fondi che possiede dal suo lato.
- La Lightning Network consente quindi lo scambio rapido ed efficiente di fondi, rispettando le limitazioni imposte dalla capacità dei canali.

Questo è la fine di questo primo capitolo, dove abbiamo gettato le basi per la Lightning Network. Nei prossimi capitoli, vedremo come aprire un canale e approfondiremo i concetti qui discussi.

## Bitcoin, Indirizzi, UTXO e Transazioni

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, indirizzi, utxo e transazioni](https://youtu.be/cadCJ2V7zTg)
Questo capitolo è un po' speciale poiché non sarà dedicato direttamente a Lightning, ma a Bitcoin. Infatti, la Lightning Network è uno strato aggiuntivo su Bitcoin. È quindi essenziale comprendere alcuni concetti fondamentali di Bitcoin per afferrare correttamente il funzionamento di Lightning nei capitoli successivi. In questo capitolo, esamineremo le basi degli indirizzi di ricezione di Bitcoin, gli UTXO, così come il funzionamento delle transazioni Bitcoin.

### Indirizzi Bitcoin, Chiavi Private e Chiavi Pubbliche

Un indirizzo Bitcoin è una serie di caratteri derivata da una **chiave pubblica**, che a sua volta è calcolata da una **chiave privata**. Come sicuramente saprai, è utilizzato per bloccare i bitcoin, il che equivale a riceverli nel nostro portafoglio.

La chiave privata è un elemento segreto che **non dovrebbe mai essere condiviso**, mentre la chiave pubblica e l'indirizzo possono essere condivisi senza rischio per la sicurezza (la loro divulgazione rappresenta solo un rischio per la tua privacy). Ecco una rappresentazione comune che adotteremo durante questo corso:

- Le **chiavi private** saranno rappresentate **verticalmente**.
- Le **chiavi pubbliche** saranno rappresentate **orizzontalmente**.
- Il loro colore indica chi le possiede (Alice in arancione e Bob in nero...).

### Transazioni Bitcoin: Invio di Fondi e Script

Su Bitcoin, una transazione comporta l'invio di fondi da un indirizzo all'altro. Prendiamo l'esempio di Alice che invia 0,002 Bitcoin a Bob. Alice utilizza la chiave privata associata al suo indirizzo per **firmare** la transazione, dimostrando così di essere effettivamente in grado di spendere questi fondi. Ma cosa succede esattamente dietro questa transazione? I fondi su un indirizzo Bitcoin sono bloccati da uno **script**, una sorta di mini-programma che impone certe condizioni per spendere i fondi.

Lo script più comune richiede una firma con la chiave privata associata all'indirizzo. Quando Alice firma una transazione con la sua chiave privata, lei **sblocca lo script** che blocca i fondi, e questi possono quindi essere trasferiti. Il trasferimento di fondi comporta l'aggiunta di un nuovo script a questi fondi, stabilendo che per spenderli questa volta, sarà richiesta la firma della chiave privata di **Bob**.

![LNP201](assets/en/05.webp)

### UTXO: Output di Transazione Non Spesi

Su Bitcoin, ciò che effettivamente scambiamo non sono direttamente bitcoin, ma **UTXO** (_Unspent Transaction Outputs_), ovvero "output di transazione non spesi".

Un UTXO è una porzione di bitcoin che può avere qualsiasi valore, ad esempio, **2.000 bitcoin**, **8 bitcoin**, o anche **8.000 satoshi**. Ogni UTXO è bloccato da uno script, e per spenderlo, si devono soddisfare le condizioni dello script, spesso una firma con la chiave privata corrispondente a un dato indirizzo di ricezione.

Gli UTXO non possono essere divisi. Ogni volta che vengono utilizzati per spendere l'importo in bitcoin che rappresentano, deve essere fatto nella sua interezza. È un po' come una banconota: se hai una banconota da 10€ e devi al panettiere 5€, non puoi semplicemente tagliare la banconota a metà. Devi dargli la banconota da 10€, e lui ti darà 5€ di resto. Questo è esattamente lo stesso principio per gli UTXO su Bitcoin! Ad esempio, quando Alice sblocca uno script con la sua chiave privata, sblocca l'intero UTXO. Se desidera inviare solo una parte dei fondi rappresentati da questo UTXO a Bob, può "frammentarlo" in più piccoli. Invierà quindi 0,0015 BTC a Bob e invierà il resto, 0,0005 BTC, a un **indirizzo di resto**.

Ecco un esempio di una transazione con 2 output:

- Un UTXO di 0,0015 BTC per Bob, bloccato da uno script che richiede la firma della chiave privata di Bob.
- Un UTXO di 0,0005 BTC per Alice, bloccato da uno script che richiede la sua firma.

![LNP201](assets/en/06.webp)

### Indirizzi Multi-firma

Oltre agli indirizzi semplici generati da una singola chiave pubblica, è possibile creare **indirizzi multi-firma** da più chiavi pubbliche. Un caso particolarmente interessante per la Lightning Network è l'**indirizzo multi-firma 2/2**, generato da due chiavi pubbliche:

![LNP201](assets/en/07.webp)

Per spendere i fondi bloccati con questo indirizzo multi-firma 2/2, è necessario firmare con le due chiavi private associate alle chiavi pubbliche.

![LNP201](assets/en/08.webp)

Questo tipo di indirizzo rappresenta precisamente sulla blockchain di Bitcoin i canali di pagamento sulla Lightning Network.

**Cosa dovresti ricordare da questo capitolo?**

- Un **indirizzo Bitcoin** deriva da una chiave pubblica, che a sua volta deriva da una chiave privata.
- I fondi su Bitcoin sono bloccati da **script**, e per spendere questi fondi, è necessario soddisfare lo script, che generalmente comporta la fornitura di una firma con la corrispondente chiave privata.
- Gli **UTXO** sono porzioni di bitcoin bloccate da script, e ogni transazione su Bitcoin consiste nello sbloccare un UTXO e poi crearne uno o più nuovi in cambio.
- Gli **indirizzi multi-firma 2/2** richiedono la firma di due chiavi private per spendere i fondi. Questi indirizzi specifici sono utilizzati nel contesto della Lightning per creare canali di pagamento.

Questo capitolo su Bitcoin ci ha permesso di rivedere alcune nozioni essenziali per quanto segue. Nel prossimo capitolo, scopriremo specificamente come funziona l'apertura dei canali sulla Lightning Network.

# Apertura e Chiusura dei Canali

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Apertura del Canale

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![apri un canale](https://youtu.be/B2caBC0Rxko)

In questo capitolo, vedremo più precisamente come aprire un canale di pagamento sulla Lightning Network e capire il collegamento tra questa operazione e il sistema Bitcoin sottostante.

### Canali Lightning

Come abbiamo visto nel primo capitolo, un **canale di pagamento** su Lightning può essere paragonato a un "tubo" per lo scambio di fondi tra due partecipanti (**Alice** e **Bob** nei nostri esempi). La capacità di questo canale corrisponde alla somma dei fondi disponibili su ciascun lato. Nel nostro esempio, Alice ha **100.000 satoshi** e Bob ha **30.000 satoshi**, dando una **capacità totale** di **130.000 satoshi**.

![LNP201](assets/en/09.webp)

### Livelli di Scambio di Informazioni

È cruciale distinguere chiaramente i diversi livelli di scambio sulla Lightning Network:

- **Comunicazioni peer-to-peer (protocollo Lightning)**: Questi sono i messaggi che i nodi Lightning inviano l'uno all'altro per comunicare. Rappresenteremo questi messaggi con linee tratteggiate nere nei nostri diagrammi.
- **Canali di pagamento (protocollo Lightning)**: Questi sono i percorsi per lo scambio di fondi su Lightning, che rappresenteremo con linee nere continue.
- **Transazioni Bitcoin (protocollo Bitcoin)**: Queste sono le transazioni effettuate onchain, che rappresenteremo con linee arancioni.

![LNP201](assets/en/10.webp)
È importante notare che un nodo Lightning può comunicare tramite il protocollo P2P senza aprire un canale, ma per scambiare fondi, è necessario un canale.

### Passaggi per Aprire un Canale Lightning

1. **Scambio di messaggi**: Alice vuole aprire un canale con Bob. Lei gli invia un messaggio contenente l'importo che vuole depositare nel canale (130.000 satoshi) e la sua chiave pubblica. Bob risponde condividendo la propria chiave pubblica.

![LNP201](assets/en/11.webp)

2. **Creazione dell'indirizzo multisignature**: Con queste due chiavi pubbliche, Alice crea un **indirizzo multisignature 2/2**, il che significa che i fondi che verranno successivamente depositati su questo indirizzo richiederanno entrambe le firme (di Alice e di Bob) per essere spesi.

![LNP201](assets/en/12.webp)

3. **Transazione di deposito**: Alice prepara una transazione Bitcoin per depositare fondi su questo indirizzo multisignature. Ad esempio, potrebbe decidere di inviare **130.000 satoshi** a questo indirizzo multisignature. Questa transazione è **costruita ma non ancora pubblicata** sulla blockchain.

![LNP201](assets/en/13.webp)

4. **Transazione di prelievo**: Prima di pubblicare la transazione di deposito, Alice costruisce una transazione di prelievo in modo da poter recuperare i suoi fondi in caso di problemi con Bob. Infatti, una volta che Alice pubblica la transazione di deposito, i suoi satoshi saranno bloccati su un indirizzo multisignature 2/2 che richiede entrambe le sue firme e quella di Bob per essere sbloccato. Alice si protegge da questo rischio di perdita costruendo la transazione di prelievo che le permette di recuperare i suoi fondi.

![LNP201](assets/en/14.webp)

5. **Firma di Bob**: Alice invia la transazione di deposito a Bob come prova e gli chiede di firmare la transazione di prelievo. Una volta ottenuta la firma di Bob sulla transazione di prelievo, Alice ha la certezza di poter recuperare i suoi fondi in qualsiasi momento, poiché ora è necessaria solo la sua firma per sbloccare il multisignature.

![LNP201](assets/en/15.webp)

6. **Pubblicazione della transazione di deposito**: Una volta ottenuta la firma di Bob, Alice può pubblicare la transazione di deposito sulla blockchain di Bitcoin, aprendo ufficialmente il canale Lightning tra i due utenti.

![LNP201](assets/en/16.webp)

### Quando si considera il canale aperto?

Il canale si considera aperto una volta che la transazione di deposito è inclusa in un blocco Bitcoin e ha raggiunto una certa profondità di conferme (numero di blocchi successivi).

**Cosa dovresti ricordare da questo capitolo?**

- L'apertura di un canale inizia con lo scambio di **messaggi** tra le due parti (scambio di importi e chiavi pubbliche).
- Un canale si forma creando un **indirizzo multisignature 2/2** e depositando fondi su di esso tramite una transazione Bitcoin.
- La persona che apre il canale si assicura di poter **recuperare i suoi fondi** attraverso una transazione di prelievo firmata dall'altra parte prima di pubblicare la transazione di deposito.

Nel prossimo capitolo, esploreremo il funzionamento tecnico di una transazione all'interno di un canale sulla rete Lightning.

## Transazione di Impegno

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![Transazione Lightning & transazione di impegno](https://youtu.be/aPqI34tpypM)

In questo capitolo, scopriremo il funzionamento tecnico di una transazione all'interno di un canale sulla rete Lightning, ovvero quando i fondi vengono spostati da un lato all'altro del canale.

### Promemoria del ciclo di vita del canale

Come visto in precedenza, un canale Lightning inizia con un'**apertura** tramite una transazione Bitcoin. Il canale può essere **chiuso** in qualsiasi momento, anch'esso tramite una transazione Bitcoin. Tra questi due momenti, un numero quasi infinito di transazioni può essere eseguito all'interno del canale, senza passare attraverso la blockchain di Bitcoin. Vediamo cosa succede durante una transazione nel canale.

### Lo stato iniziale del canale

Al momento dell'apertura del canale, Alice ha depositato **130.000 satoshi** sull'indirizzo multisignature del canale. Pertanto, nello stato iniziale, tutti i fondi sono dalla parte di Alice. Prima di aprire il canale, Alice ha anche fatto firmare a Bob una **transazione di prelievo**, che le avrebbe permesso di recuperare i suoi fondi se avesse desiderato chiudere il canale.

### Transazioni non pubblicate: Le Transazioni di Impegno

Quando Alice effettua una transazione nel canale per inviare fondi a Bob, viene creata una nuova transazione Bitcoin per riflettere questo cambiamento nella distribuzione dei fondi. Questa transazione, chiamata **transazione di impegno**, non viene pubblicata sulla blockchain ma rappresenta il nuovo stato del canale a seguito della transazione Lightning.

Prendiamo un esempio con Alice che invia 30.000 satoshi a Bob:

- **Inizialmente**: Alice ha 130.000 satoshi.
- **Dopo la transazione**: Alice ha 100.000 satoshi, e Bob 30.000 satoshi.
  Per convalidare questo trasferimento, Alice e Bob creano una nuova **transazione Bitcoin non pubblicata** che invierebbe **100.000 satoshi ad Alice** e **30.000 satoshi a Bob** dall'indirizzo multisignature. Entrambe le parti costruiscono questa transazione indipendentemente, ma con gli stessi dati (importi e indirizzi). Una volta costruita, ciascuno firma la transazione e scambia la propria firma con l'altro. Questo permette a entrambe le parti di pubblicare la transazione in qualsiasi momento, se necessario, per recuperare la propria quota del canale sulla blockchain principale di Bitcoin.

### Processo di Trasferimento: La Fattura

Quando Bob desidera ricevere fondi, invia ad Alice una **_fattura_** per 30.000 satoshi. Alice procede quindi a pagare questa fattura avviando il trasferimento all'interno del canale. Come abbiamo visto, questo processo si basa sulla creazione e firma di una nuova **transazione di impegno**.

Ogni transazione di impegno rappresenta la nuova distribuzione dei fondi nel canale dopo il trasferimento. In questo esempio, dopo la transazione, Bob ha 30.000 satoshi e Alice ha 100.000 satoshi. Se uno dei due partecipanti decidesse di pubblicare questa transazione di impegno sulla blockchain, ciò risulterebbe nella chiusura del canale e i fondi sarebbero distribuiti secondo questa ultima distribuzione.

### Nuovo Stato Dopo una Seconda Transazione

Prendiamo un altro esempio: dopo la prima transazione in cui Alice ha inviato 30.000 satoshi a Bob, Bob decide di inviare **10.000 satoshi indietro ad Alice**. Questo crea un nuovo stato del canale. La nuova **transazione di impegno** rappresenterà questa distribuzione aggiornata:

- **Alice** ora ha **110.000 satoshi**.
- **Bob** ha **20.000 satoshi**.

Ancora una volta, questa transazione non viene pubblicata sulla blockchain ma può essere pubblicata in qualsiasi momento nel caso in cui il canale venga chiuso.

In sintesi, quando i fondi vengono trasferiti all'interno di un canale Lightning:

- Alice e Bob creano una nuova **transazione di impegno**, che riflette la nuova distribuzione dei fondi. - Questa transazione Bitcoin è **firmata** da entrambe le parti, ma **non pubblicata** sulla blockchain di Bitcoin finché il canale rimane aperto.
- Le transazioni di impegno assicurano che ciascun partecipante possa recuperare i propri fondi in qualsiasi momento sulla blockchain di Bitcoin pubblicando l'ultima transazione firmata.

Tuttavia, questo sistema presenta una potenziale falla, che affronteremo nel prossimo capitolo. Vedremo come ciascun partecipante può proteggersi contro un tentativo di truffa da parte dell'altra parte.

## Chiave di Revoca

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transazioni parte 2](https://youtu.be/RRvoVTLRJ84)
In questo capitolo, approfondiremo il funzionamento delle transazioni sulla Lightning Network discutendo i meccanismi in atto per proteggersi dalle truffe, assicurando che ciascuna parte rispetti le regole all'interno di un canale.

### Promemoria: Transazioni di Impegno

Come visto in precedenza, le transazioni su Lightning si basano su **transazioni di impegno** non pubblicate. Queste transazioni riflettono l'attuale distribuzione dei fondi nel canale. Quando viene effettuata una nuova transazione Lightning, viene creata e firmata da entrambe le parti una nuova transazione di impegno per riflettere il nuovo stato del canale.

Prendiamo un esempio semplice:

- **Stato iniziale**: Alice ha **100.000 satoshi**, Bob **30.000 satoshi**.
- Dopo una transazione in cui Alice invia **40.000 satoshi** a Bob, la nuova transazione di impegno distribuisce i fondi come segue:
  - Alice: **60.000 satoshi**
  - Bob: **70.000 satoshi**

![LNP201](assets/en/22.webp)

In qualsiasi momento, entrambe le parti possono pubblicare la **più recente transazione di impegno** firmata per chiudere il canale e recuperare i propri fondi.

### Il Problema: Truffare Pubblicando una Vecchia Transazione

Un potenziale problema sorge se una delle parti decide di **truffare** pubblicando una vecchia transazione di impegno. Ad esempio, Alice potrebbe pubblicare una vecchia transazione di impegno in cui aveva **100.000 satoshi**, anche se ora ne ha solo **60.000** in realtà. Ciò le permetterebbe di rubare **40.000 satoshi** a Bob.

![LNP201](assets/en/23.webp)

Ancora peggio, Alice potrebbe pubblicare la primissima transazione di prelievo, quella prima che il canale fosse aperto, dove aveva **130.000 satoshi**, e così rubare tutti i fondi del canale.

![LNP201](assets/en/24.webp)

### Soluzione: Chiave di Revoca e Timelock

Per prevenire questo tipo di truffa da parte di Alice, sulla Lightning Network, vengono aggiunti **meccanismi di sicurezza** alle transazioni di impegno:

1. **Il timelock**: Ogni transazione di impegno include un timelock per i fondi di Alice. Il timelock è una primitiva di smart contract che stabilisce una condizione temporale che deve essere soddisfatta affinché una transazione possa essere aggiunta a un blocco. Ciò significa che Alice non può recuperare i suoi fondi fino a quando non sia passato un certo numero di blocchi, se pubblica una delle transazioni di impegno. Questo timelock inizia ad applicarsi dalla conferma della transazione di impegno. La sua durata è generalmente proporzionale alla dimensione del canale, ma può anche essere configurata manualmente.
2. **Chiave di Revoca**: I fondi di Alice possono anche essere spesi immediatamente da Bob se possiede la **chiave di revoca**. Questa chiave consiste in un segreto detenuto da Alice e un segreto detenuto da Bob. Nota che questo segreto è diverso per ogni transazione di impegno.
   Grazie a questi 2 meccanismi combinati, Bob ha il tempo di rilevare il tentativo di Alice di barare, e di punirla recuperando il suo output con la chiave di revoca, il che per Bob significa recuperare tutti i fondi del canale. La nostra nuova transazione di impegno ora apparirà così:
   ![LNP201](assets/en/25.webp)

Analizziamo insieme il funzionamento di questo meccanismo.

### Processo di Aggiornamento della Transazione

Quando Alice e Bob aggiornano lo stato del canale con una nuova transazione Lightning, scambiano in anticipo i rispettivi **segreti** per la precedente transazione di impegno (quella che diventerà obsoleta e potrebbe permettere a uno di loro di barare). Questo significa che, nel nuovo stato del canale:

- Alice e Bob hanno una nuova transazione di impegno che rappresenta l'attuale distribuzione dei fondi dopo la transazione Lightning.
- Ognuno ha il segreto dell'altro per la transazione precedente, il che permette loro di usare la chiave di revoca solo se uno di loro prova a barare pubblicando una transazione con uno stato vecchio nei mempool dei nodi Bitcoin. Infatti, per punire l'altra parte, è necessario detenere entrambi i segreti e l'altra transazione di impegno, che include l'input firmato. Senza questa transazione, la chiave di revoca da sola è inutile. L'unico modo per ottenere questa transazione è recuperarla dai mempool (nelle transazioni in attesa di conferma) o nelle transazioni confermate sulla blockchain durante il timelock, il che dimostra che l'altra parte sta cercando di barare, intenzionalmente o meno.

Prendiamo un esempio per capire bene questo processo:

1. **Stato Iniziale**: Alice ha **100.000 satoshi**, Bob **30.000 satoshi**.

![LNP201](assets/en/26.webp)

2. Bob vuole ricevere 40.000 satoshi da Alice tramite il loro canale Lightning. Per fare ciò:
   - Lui le invia una fattura insieme al suo segreto per la chiave di revoca della sua precedente transazione di impegno.
   - In risposta, Alice fornisce la sua firma per la nuova transazione di impegno di Bob, così come il suo segreto per la chiave di revoca della sua precedente transazione.
   - Infine, Bob invia la sua firma per la nuova transazione di impegno di Alice.
   - Questi scambi permettono ad Alice di inviare **40.000 satoshi** a Bob su Lightning tramite il loro canale, e le nuove transazioni di impegno ora riflettono questa nuova distribuzione dei fondi.

![LNP201](assets/en/27.webp)

3. Se Alice tenta di pubblicare la vecchia transazione di impegno dove possedeva ancora **100.000 satoshi**, Bob, avendo ottenuto la chiave di revoca, può immediatamente recuperare i fondi usando questa chiave, mentre Alice è bloccata dal timelock.

![LNP201](assets/en/28.webp)

Anche se, in questo caso, Bob non ha interesse economico a cercare di barare, se lo fa comunque, Alice beneficia anche della protezione simmetrica che le offre le stesse garanzie.

**Cosa dovresti ricavare da questo capitolo?**

Le **transazioni di impegno** sulla Lightning Network includono meccanismi di sicurezza che riducono sia il rischio di barare sia gli incentivi a farlo. Prima di firmare una nuova transazione di impegno, Alice e Bob scambiano i rispettivi **segreti** per le precedenti transazioni di impegno. Se Alice prova a pubblicare una vecchia transazione di impegno, Bob può usare la **chiave di revoca** per recuperare tutti i fondi prima che Alice possa (perché è bloccata dal timelock), il che la punisce per aver tentato di barare.

Questo sistema di sicurezza garantisce che i partecipanti aderiscano alle regole della Lightning Network, e non possano trarre profitto dalla pubblicazione di vecchie transazioni di impegno.
A questo punto della formazione, ora sai come vengono aperti i canali Lightning e come funzionano le transazioni all'interno di questi canali. Nel prossimo capitolo, scopriremo i diversi modi per chiudere un canale e recuperare i tuoi bitcoin sulla blockchain principale.

## Chiusura del Canale

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![chiudi un canale](https://youtu.be/FVmQvNpVW8Y)

In questo capitolo, discuteremo della **chiusura di un canale** sulla Lightning Network, che viene effettuata tramite una transazione Bitcoin, proprio come l'apertura di un canale. Dopo aver visto come funzionano le transazioni all'interno di un canale, è ora il momento di vedere come chiudere un canale e recuperare i fondi sulla blockchain di Bitcoin.

### Promemoria del ciclo di vita del canale

Il **ciclo di vita di un canale** inizia con la sua **apertura**, tramite una transazione Bitcoin, poi vengono effettuate transazioni Lightning al suo interno, e infine, quando le parti desiderano recuperare i loro fondi, il canale viene **chiuso** tramite una seconda transazione Bitcoin. Le transazioni intermedie effettuate su Lightning sono rappresentate da **transazioni di impegno** non pubblicate.

![LNP201](assets/en/29.webp)

### I tre tipi di chiusura del canale

Ci sono tre modi principali per chiudere questo canale, che possono essere chiamati **il buono, il brutto e il truffatore** (ispirati da Andreas Antonopoulos in _Mastering the Lightning Network_):

1. **Il Buono**: la **chiusura cooperativa**, dove Alice e Bob concordano di chiudere il canale.
2. **Il Brutto**: la **chiusura forzata**, dove una delle parti decide di chiudere il canale onestamente, ma senza l'accordo dell'altra.
3. **Il Truffatore**: la **chiusura con imbroglio**, dove una delle parti tenta di rubare fondi pubblicando una vecchia transazione di impegno (qualsiasi tranne l'ultima, che riflette la distribuzione effettiva e giusta dei fondi).

Prendiamo un esempio:

- Alice possiede **100.000 satoshi** e Bob **30.000 satoshi**.
- Questa distribuzione è riflessa in **2 transazioni di impegno** (una per utente) che non sono pubblicate, ma potrebbero esserlo in caso di chiusura del canale.

![LNP201](assets/en/30.webp)

### Il Buono: la chiusura cooperativa

In una **chiusura cooperativa**, Alice e Bob concordano di chiudere il canale. Ecco come procede:

1. Alice invia un messaggio a Bob tramite il protocollo di comunicazione Lightning per proporre la chiusura del canale.
2. Bob accetta, e le due parti non effettuano ulteriori transazioni nel canale.

![LNP201](assets/en/31.webp)

3. Alice e Bob negoziano insieme le commissioni della **transazione di chiusura**. Queste commissioni sono generalmente calcolate in base al mercato delle commissioni Bitcoin al momento della chiusura. È importante notare che **è sempre la persona che ha aperto il canale** (Alice nel nostro esempio) a pagare le commissioni di chiusura.
4. Costruiscono una nuova **transazione di chiusura**. Questa transazione assomiglia a una transazione di impegno, ma senza timelock o meccanismi di revoca, poiché entrambe le parti stanno cooperando e non c'è rischio di imbroglio. Questa transazione di chiusura cooperativa è quindi diversa dalle transazioni di impegno.
   Per esempio, se Alice possiede **100.000 satoshi** e Bob **30.000 satoshi**, la transazione di chiusura invierà **100.000 satoshi** all'indirizzo di Alice e **30.000 satoshi** all'indirizzo di Bob, senza vincoli di timelock. Una volta che questa transazione è firmata da entrambe le parti, viene pubblicata da Alice. Una volta che la transazione è confermata sulla blockchain di Bitcoin, il canale Lightning viene ufficialmente chiuso.
   ![LNP201](assets/en/32.webp)

La **chiusura cooperativa** è il metodo preferito di chiusura perché è veloce (nessun timelock) e le commissioni di transazione sono regolate in base alle attuali condizioni di mercato di Bitcoin. Questo evita di pagare troppo poco, il che potrebbe rischiare di bloccare la transazione nei mempool, o di pagare inutilmente troppo, portando a una perdita finanziaria non necessaria per i partecipanti.

### Il Lato Negativo: la chiusura forzata

Quando il nodo di Alice invia un messaggio a quello di Bob chiedendo una chiusura cooperativa, se lui non risponde (per esempio, a causa di un'interruzione di internet o di un problema tecnico), Alice può procedere con una **chiusura forzata** pubblicando **l'ultima transazione di impegno firmata**.
In questo caso, Alice pubblicherà semplicemente l'ultima transazione di impegno, che riflette lo stato del canale al momento dell'ultima transazione Lightning avvenuta con la corretta distribuzione dei fondi.

![LNP201](assets/en/33.webp)

Questa transazione include un **timelock** per i fondi di Alice, rendendo la chiusura più lenta.

![LNP201](assets/en/34.webp)

Inoltre, le commissioni della transazione di impegno possono essere inadeguate al momento della chiusura, poiché sono state impostate quando la transazione è stata creata, talvolta diversi mesi prima. Generalmente, i clienti Lightning sovrastimano le commissioni per evitare problemi futuri, ma questo può portare a commissioni eccessive, o al contrario troppo basse.

In sintesi, la **chiusura forzata** è un'opzione dell'ultimo minuto quando il peer non risponde più. È più lenta e meno economica della chiusura cooperativa. Pertanto, dovrebbe essere evitata il più possibile.

### Il Trucco: barare

Infine, una chiusura con **barare** si verifica quando una delle parti cerca di pubblicare una vecchia transazione di impegno, spesso dove detenevano più fondi di quanto dovrebbero. Per esempio, Alice potrebbe pubblicare una vecchia transazione dove possedeva **120.000 satoshi**, mentre ora ne possiede effettivamente solo **100.000**.

![LNP201](assets/en/35.webp)

Bob, per prevenire questo imbroglio, monitora la blockchain di Bitcoin e il suo mempool per assicurarsi che Alice non pubblichi una vecchia transazione. Se Bob rileva un tentativo di barare, può usare la **chiave di revoca** per recuperare i fondi di Alice e punirla prendendo l'intera somma del canale. Poiché Alice è bloccata dal timelock sul suo output, Bob ha il tempo di spenderlo senza un timelock dalla sua parte per recuperare l'intera somma su un indirizzo di sua proprietà.

![LNP201](assets/en/36.webp)

Ovviamente, barare può potenzialmente avere successo se Bob non agisce entro il tempo imposto dal timelock sull'output di Alice. In questo caso, l'output di Alice viene sbloccato, permettendole di consumarlo per creare un nuovo output verso un indirizzo che controlla.

**Cosa dovresti ricavare da questo capitolo?**

Ci sono tre modi per chiudere un canale:

1. **Chiusura Cooperativa**: Veloce e meno costosa, dove entrambe le parti concordano di chiudere il canale e pubblicano una transazione di chiusura su misura.
2. **Chiusura Forzata**: Meno desiderabile, poiché si basa sulla pubblicazione di una transazione di impegno, con commissioni potenzialmente inadeguate e un timelock, che rallenta la chiusura.
3. **Imbroglio**: Se una delle parti tenta di rubare fondi pubblicando una transazione vecchia, l'altra può utilizzare la chiave di revoca per punire questo imbroglio.
   Nei prossimi capitoli, esploreremo la Lightning Network da una prospettiva più ampia, concentrandoci su come funziona la sua rete.

# Una Rete di Liquidità

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![lightning network](https://youtu.be/RAZAa3v41DM)

In questo capitolo, esploreremo come i pagamenti sulla Lightning Network possono raggiungere un destinatario anche se non sono direttamente connessi tramite un canale di pagamento. Lightning è, infatti, una **rete di canali di pagamento**, che consente di inviare fondi a un nodo distante attraverso i canali di altri partecipanti. Scopriremo come vengono instradati i pagamenti attraverso la rete, come si muove la liquidità tra i canali e come vengono calcolate le commissioni sulle transazioni.

### La Rete dei Canali di Pagamento

Sulla Lightning Network, una transazione corrisponde a un trasferimento di fondi tra due nodi. Come visto nei capitoli precedenti, è necessario aprire un canale con qualcuno per eseguire transazioni Lightning. Questo canale consente un numero quasi infinito di transazioni off-chain prima di chiuderlo per recuperare il saldo on-chain. Tuttavia, questo metodo ha lo svantaggio di richiedere un canale diretto con l'altra persona per ricevere o inviare fondi, il che implica una transazione di apertura e una di chiusura per ogni canale. Se prevedo di effettuare un gran numero di pagamenti con questa persona, aprire e chiudere un canale diventa conveniente. Al contrario, se ho bisogno di eseguire solo poche transazioni Lightning, aprire un canale diretto non è vantaggioso, poiché mi costerebbe 2 transazioni on-chain per un numero limitato di transazioni off-chain. Questo caso potrebbe verificarsi, ad esempio, quando si desidera pagare con Lightning presso un commerciante senza pianificare di tornare.

Per risolvere questo problema, la Lightning Network consente di instradare un pagamento attraverso diversi canali e nodi intermedi, consentendo così una transazione senza un canale diretto con l'altra persona.

Per esempio, immagina che:

- **Alice** (in arancione) abbia un canale con **Suzie** (in grigio) con **100.000 satoshi** dalla sua parte e **30.000 satoshi** dalla parte di Suzie.
- **Suzie** ha un canale con **Bob** in cui possiede **250.000 satoshi** e dove Bob non ha satoshi.

![LNP201](assets/en/37.webp)

Se Alice vuole inviare fondi a Bob senza aprire un canale diretto con lui, dovrà passare attraverso Suzie, e ogni canale dovrà adeguare la liquidità da ciascun lato. **I satoshi inviati rimangono all'interno dei rispettivi canali**; non "attraversano" effettivamente i canali, ma il trasferimento avviene tramite un adeguamento della liquidità interna in ogni canale.

Supponiamo che Alice voglia inviare **50.000 satoshi** a Bob:

1. **Alice** invia 50.000 satoshi a **Suzie** nel loro canale comune.
2. **Suzie** replica questo trasferimento inviando 50.000 satoshi a **Bob** nel loro canale.

![LNP201](assets/en/38.webp)
Così, il pagamento viene instradato a Bob attraverso un movimento di liquidità in ogni canale. Al termine dell'operazione, Alice finisce con 50.000 satoshi. Ha effettivamente trasferito 50.000 satoshi poiché inizialmente ne aveva 100.000. Bob, dal canto suo, finisce con un ulteriore 50.000 satoshi. Per Suzie (il nodo intermedio), questa operazione è neutra: inizialmente, aveva 30.000 satoshi nel suo canale con Alice e 250.000 satoshi nel suo canale con Bob, per un totale di 280.000 satoshi. Dopo l'operazione, detiene 80.000 satoshi nel suo canale con Alice e 200.000 satoshi nel suo canale con Bob, che è la stessa somma di partenza.
Questo trasferimento è quindi limitato dalla **liquidità disponibile** nella direzione del trasferimento.

### Calcolo del Percorso e Limiti di Liquidità

Prendiamo un esempio teorico di un altro network con:

- **130.000 satoshi** dal lato di Alice (in arancione) nel suo canale con **Suzie** (in grigio).
- **90.000 satoshi** dal lato di **Suzie** e **200.000 satoshi** dal lato di **Carol** (in rosa).
- **150.000 satoshi** dal lato di **Carol** e **100.000 satoshi** dal lato di **Bob**.

![LNP201](assets/en/39.webp)

Il massimo che Alice può inviare a Bob in questa configurazione è **90.000 satoshi**, poiché è limitata dalla più piccola liquidità disponibile nel canale da **Suzie a Carol**. Nella direzione opposta (da Bob ad Alice), nessun pagamento è possibile perché il lato di **Suzie** nel canale con **Alice** non contiene satoshi. Pertanto, non c'è **nessun percorso** utilizzabile per un trasferimento in questa direzione.
Alice invia **40.000 satoshi** a Bob attraverso i canali:

1. Alice trasferisce 40.000 satoshi nel suo canale con Suzie.
2. Suzie trasferisce 40.000 satoshi a Carol nel loro canale condiviso.
3. Carol infine trasferisce 40.000 satoshi a Bob.

![LNP201](assets/en/40.webp)

I **satoshi inviati** in ogni canale **rimangono nel canale**, quindi i satoshi inviati da Carol a Bob non sono gli stessi di quelli inviati da Alice a Suzie. Il trasferimento avviene solo regolando la liquidità all'interno di ogni canale. Inoltre, la capacità totale dei canali rimane invariata.

![LNP201](assets/en/41.webp)

Come nell'esempio precedente, dopo la transazione, il nodo sorgente (Alice) ha 40.000 satoshi in meno. I nodi intermedi (Suzie e Carol) mantengono lo stesso importo totale, rendendo l'operazione neutra per loro. Infine, il nodo di destinazione (Bob) riceve un ulteriore 40.000 satoshi.

Il ruolo dei nodi intermedi è quindi molto importante nel funzionamento della Lightning Network. Essi facilitano i trasferimenti offrendo molteplici percorsi per i pagamenti. Per incoraggiare questi nodi a fornire la loro liquidità e partecipare all'instradamento dei pagamenti, vengono pagate loro delle **commissioni di routing**.

### Commissioni di Routing

I nodi intermedi applicano delle commissioni per permettere ai pagamenti di passare attraverso i loro canali. Queste commissioni sono stabilite da **ogni nodo per ogni canale**. Le commissioni consistono di 2 elementi:

1. "**Commissione base**": un importo fisso per canale, spesso **1 sat** per default, ma personalizzabile.
2. "**Commissione variabile**": una percentuale dell'importo trasferito, calcolata in **parti per milione (ppm)**. Per impostazione predefinita, è **1 ppm** (1 sat per milione di satoshi trasferiti), ma può anche essere regolata.
   Le commissioni variano anche a seconda della direzione del trasferimento. Ad esempio, per un trasferimento da Alice a Suzie, si applicano le commissioni di Alice. Al contrario, da Suzie ad Alice, si utilizzano le commissioni di Suzie.

Per esempio, per un canale tra Alice e Suzie, potremmo avere:

- **Alice**: commissione base di 1 sat e 1 ppm per le commissioni variabili.
- **Suzie**: commissione base di 0,5 sat e 10 ppm per le commissioni variabili.

![LNP201](assets/en/42.webp)

Per comprendere meglio come funzionano le commissioni, studiamo la stessa rete Lightning di prima, ma ora con le seguenti commissioni di routing:

- Canale **Alice - Suzie**: commissione base di 1 satoshi e 1 ppm per Alice.
- Canale **Suzie - Carol**: commissione base di 0 satoshi e 200 ppm per Suzie.
- Canale **Carol - Bob**: commissione base di 1 satoshi e 1 ppm per Suzie 2.
  ![LNP201](assets/en/43.webp)

Per lo stesso pagamento di **40.000 satoshi** a Bob, Alice dovrà inviare un po' di più, poiché ogni nodo intermediario dedurrà le proprie commissioni:

- **Carol** deduce 1,04 satoshi sul canale con Bob:
  $$ f*{\text{Carol-Bob}} = \text{commissione base} + \left(\frac{\text{ppm} \times \text{importo}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0,04 = 1,04 \text{ sats} $$

- **Suzie** deduce 8 satoshi in commissioni sul canale con Carol:
  $$ f*{\text{Suzie-Carol}} = \text{commissione base} + \left(\frac{\text{ppm} \times \text{importo}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001,04}{10^6} = 0 + 8,0002 \approx 8 \text{ sats} $$

Le commissioni totali per questo pagamento su questo percorso sono quindi **9,04 satoshi**. Così, Alice deve inviare **40.009,04 satoshi** affinché Bob riceva esattamente **40.000 satoshi**.

![LNP201](assets/en/44.webp)

La liquidità viene quindi aggiornata:

![LNP201](assets/en/45.webp)

### Onion Routing

Per instradare un pagamento dal mittente al destinatario, la rete Lightning utilizza un metodo chiamato "**onion routing**". A differenza dell'instradamento dei dati classici, dove ogni router decide la direzione dei dati in base alla loro destinazione, l'onion routing funziona diversamente:

- **Il nodo mittente calcola l'intero percorso**: Alice, ad esempio, determina che il suo pagamento deve passare attraverso Suzie e Carol prima di raggiungere Bob.
- **Ogni nodo intermedio conosce solo il suo vicino immediato**: Suzie sa solo che ha ricevuto fondi da Alice e che deve trasferirli a Carol. Tuttavia, Suzie non sa se Alice è il nodo sorgente o un nodo intermedio, e non sa nemmeno se Carol è il nodo destinatario o solo un altro nodo intermedio. Questo principio si applica anche a Carol e a tutti gli altri nodi sul percorso. Il routing Onion preserva così la confidenzialità delle transazioni mascherando l'identità del mittente e del destinatario finale. Per garantire che il nodo trasmittente possa calcolare un percorso completo verso il destinatario nel routing Onion, deve mantenere un **grafico della rete** per conoscere la sua topologia e determinare i percorsi possibili.
  **Cosa dovresti ricavare da questo capitolo?**

1. Su Lightning, i pagamenti possono essere instradati tra nodi indirettamente connessi attraverso canali intermedi. Ciascuno di questi nodi intermedi facilita il rilancio della liquidità.
2. I nodi intermedi ricevono una commissione per il loro servizio, consistente in tariffe fisse e variabili.
3. Il routing Onion consente al nodo trasmittente di calcolare il percorso completo senza che i nodi intermedi conoscano la sorgente o la destinazione finale.

In questo capitolo, abbiamo esplorato l'instradamento dei pagamenti sulla Lightning Network. Ma sorge una domanda: cosa impedisce ai nodi intermedi di accettare un pagamento in entrata senza inoltrarlo alla destinazione successiva, con l'obiettivo di intercettare la transazione? Questo è precisamente il ruolo degli HTLC che studieremo nel capitolo seguente.

## HTLC – Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

In questo capitolo, scopriremo come Lightning consente ai pagamenti di transitare attraverso nodi intermedi senza la necessità di fidarsi di loro, grazie agli **HTLC** (_Hashed Time-Locked Contracts_). Questi contratti intelligenti assicurano che ciascun nodo intermedio riceverà i fondi dal suo canale solo se inoltra il pagamento al destinatario finale, altrimenti, il pagamento non verrà convalidato.

Il problema che sorge per l'instradamento dei pagamenti è quindi la necessaria fiducia nei nodi intermedi, e tra i nodi intermedi stessi. Per illustrare questo, rivediamo il nostro esempio semplificato di rete Lightning con 3 nodi e 2 canali:

- Alice ha un canale con Suzie.
- Suzie ha un canale con Bob.

Alice vuole inviare 40.000 satoshi a Bob ma non ha un canale diretto con lui e non desidera aprirne uno. Cerca quindi una rotta e decide di passare attraverso il nodo di Suzie.

![LNP201](assets/en/46.webp)

Se Alice invia ingenuamente 40.000 satoshi a Suzie sperando che Suzie trasferisca questa somma a Bob, Suzie potrebbe tenere i fondi per sé e non trasmettere nulla a Bob.

![LNP201](assets/en/47.webp)
Per evitare questa situazione, su Lightning, utilizziamo gli HTLC (Hashed Time-Locked Contracts), che rendono il pagamento al nodo intermedio condizionale, nel senso che Suzie deve soddisfare determinate condizioni per accedere ai fondi di Alice e trasferirli a Bob.

### Come Funzionano gli HTLC

Un HTLC è un contratto speciale basato su due principi:

- **Condizione di accesso**: Il destinatario deve rivelare un segreto per sbloccare il pagamento a loro dovuto.
- **Scadenza**: Se il pagamento non viene completato integralmente entro un periodo definito, viene annullato e i fondi ritornano al mittente.

Ecco come funziona questo processo nel nostro esempio con Alice, Suzie e Bob:

![LNP201](assets/en/48.webp)
**Creazione del segreto**: Bob genera un segreto casuale noto come _s_ (la preimmagine) e calcola il suo hash noto come _r_ con la funzione hash indicata come _h_. Abbiamo:

$$
r = h(s)
$$

L'uso di una funzione hash rende impossibile trovare _s_ avendo solo _h(s)_, ma se _s_ è fornito, è facile verificare che corrisponde a _h(s)_.

![LNP201](assets/en/49.webp)

**Invio della richiesta di pagamento**: Bob invia una **fattura** ad Alice chiedendo un pagamento. Questa fattura include in particolare l'hash _r_.

![LNP201](assets/en/50.webp)

**Invio del pagamento condizionale**: Alice invia un HTLC di 40.000 satoshi a Suzie. La condizione affinché Suzie riceva questi fondi è che fornisca ad Alice un segreto _s'_ che soddisfa la seguente equazione:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Trasferimento dell'HTLC al destinatario finale**: Suzie, per ottenere i 40.000 satoshi da Alice, deve trasferire un HTLC simile di 40.000 satoshi a Bob, che ha la stessa condizione, ovvero che deve fornire a Suzie un segreto _s'_ che soddisfa l'equazione:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Validazione tramite il segreto _s_**: Bob fornisce _s_ a Suzie per ricevere i 40.000 satoshi promessi nell'HTLC. Con questo segreto, Suzie può quindi sbloccare l'HTLC di Alice e ottenere i 40.000 satoshi da Alice. Il pagamento viene quindi correttamente instradato a Bob.

![LNP201](assets/en/53.webp)
Questo processo impedisce a Suzie di trattenere i fondi di Alice senza completare il trasferimento a Bob, poiché deve inviare il pagamento a Bob per ottenere il segreto _s_ e quindi sbloccare l'HTLC di Alice. L'operazione rimane la stessa anche se il percorso include diversi nodi intermedi: si tratta semplicemente di ripetere i passaggi di Suzie per ogni nodo intermedio. Ogni nodo è protetto dalle condizioni degli HTLC, perché lo sblocco dell'ultimo HTLC da parte del destinatario attiva automaticamente lo sblocco di tutti gli altri HTLC in cascata.

### Scadenza e gestione degli HTLC in caso di problemi

Se durante il processo di pagamento, uno dei nodi intermedi, o il nodo destinatario, smette di rispondere, specialmente in caso di interruzione di internet o di corrente, allora il pagamento non può essere completato, perché il segreto necessario per sbloccare gli HTLC non viene trasmesso. Prendendo il nostro esempio con Alice, Suzie e Bob, questo problema si verifica, ad esempio, se Bob non trasmette il segreto _s_ a Suzie. In questo caso, tutti gli HTLC a monte del percorso sono bloccati, e anche i fondi che assicurano.

![LNP201](assets/en/54.webp)

Per evitare ciò, gli HTLC su Lightning hanno una scadenza che consente di rimuovere l'HTLC se non viene completato dopo un certo tempo. La scadenza segue un ordine specifico poiché inizia prima con l'HTLC più vicino al destinatario, e poi si sposta progressivamente fino all'emittente della transazione. Nel nostro esempio, se Bob non dà mai il segreto _s_ a Suzie, ciò farebbe scadere prima l'HTLC di Suzie verso Bob.

![LNP201](assets/en/55.webp)

Poi l'HTLC da Alice a Suzie.
Se l'ordine di scadenza fosse invertito, Alice potrebbe recuperare il suo pagamento prima che Suzie possa proteggersi da potenziali truffe. Infatti, se Bob tornasse a reclamare il suo HTLC mentre Alice ha già rimosso il suo, Suzie sarebbe in svantaggio. Questo ordine cascata di scadenza degli HTLC assicura quindi che nessun nodo intermediario subisca perdite ingiuste.

### Rappresentazione degli HTLC nelle transazioni di impegno

Le transazioni di impegno rappresentano gli HTLC in modo tale che le condizioni che impongono su Lightning possano essere trasferite a Bitcoin in caso di chiusura forzata del canale durante la durata di un HTLC. Come promemoria, le transazioni di impegno rappresentano lo stato attuale del canale tra i due utenti e consentono una chiusura forzata unilaterale in caso di problemi. Con ogni nuovo stato del canale, vengono create 2 transazioni di impegno: una per ciascuna parte. Rivisitiamo il nostro esempio con Alice, Suzie e Bob, ma guardiamo più da vicino cosa succede a livello di canale tra Alice e Suzie quando viene creato l'HTLC.

Prima dell'inizio del pagamento di 40.000 satoshi tra Alice e Bob, Alice ha 100.000 satoshi nel suo canale con Suzie, mentre Suzie ne detiene 30.000. Le loro transazioni di impegno sono le seguenti:

Alice ha appena ricevuto la fattura di Bob, che contiene in modo notevole _r_, l'hash del segreto. Può quindi costruire un HTLC di 40.000 satoshi con Suzie. Questo HTLC è rappresentato nelle ultime transazioni di impegno come un output chiamato "**_HTLC Out_**" dal lato di Alice, poiché i fondi sono in uscita, e "**_HTLC In_**" dal lato di Suzie, poiché i fondi sono in entrata.

Questi output associati all'HTLC condividono esattamente le stesse condizioni, ovvero:

- Se Suzie è in grado di fornire il segreto _s_, può sbloccare immediatamente questo output e trasferirlo a un indirizzo che controlla.
- Se Suzie non possiede il segreto _s_, non può sbloccare questo output, e Alice sarà in grado di sbloccarlo dopo un timelock per inviarlo a un indirizzo che controlla. Il timelock concede quindi a Suzie un periodo per reagire se ottiene _s_.

Queste condizioni si applicano solo se il canale viene chiuso (cioè, una transazione di impegno viene pubblicata sulla blockchain) mentre l'HTLC è ancora attivo su Lightning, il che significa che il pagamento tra Alice e Bob non è ancora stato finalizzato e gli HTLC non sono ancora scaduti. Grazie a queste condizioni, Suzie può recuperare i 40.000 satoshi dell'HTLC che le sono dovuti fornendo _s_. Altrimenti, Alice recupera i fondi dopo la scadenza del timelock, perché se Suzie non conosce _s_, significa che non ha trasferito i 40.000 satoshi a Bob e, quindi, i fondi di Alice non le sono dovuti.

Inoltre, se il canale viene chiuso mentre sono in sospeso diversi HTLC, ci saranno tanti output aggiuntivi quanti sono gli HTLC in corso.
Se il canale non viene chiuso, allora dopo la scadenza o il successo del pagamento Lightning, vengono create nuove transazioni di impegno per riflettere il nuovo stato stabile del canale, cioè senza HTLC in sospeso. Gli output relativi agli HTLC possono quindi essere rimossi dalle transazioni di impegno.
Infine, nel caso di una chiusura cooperativa del canale mentre un HTLC è attivo, Alice e Suzie smettono di accettare nuovi pagamenti e attendono la risoluzione o la scadenza degli HTLC in corso. Ciò consente loro di pubblicare una transazione di chiusura più leggera, senza gli output relativi agli HTLC, riducendo così le commissioni ed evitando l'attesa per un possibile timelock.
**Cosa dovresti ricavare da questo capitolo?**

Gli HTLC consentono il routing dei pagamenti Lightning attraverso più nodi senza doverli fidare. Ecco i punti chiave da ricordare:

1. Gli HTLC garantiscono la sicurezza dei pagamenti attraverso un segreto (preimage) e un tempo di scadenza.
2. La risoluzione o la scadenza degli HTLC segue un ordine specifico: poi dalla destinazione verso la fonte, al fine di proteggere ogni nodo.
3. Finché un HTLC non è né risolto né scaduto, viene mantenuto come output nelle transazioni di impegno più recenti.

Nel prossimo capitolo, scopriremo come un nodo che emette una transazione Lightning trova e seleziona le rotte per il suo pagamento per raggiungere il nodo destinatario.

## Trovare la Tua Strada

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![trovare la tua strada](https://youtu.be/wnUGJjOxd9Q)

Nei capitoli precedenti, abbiamo visto come utilizzare i canali di altri nodi per instradare i pagamenti e raggiungere un nodo senza essere direttamente connessi ad esso tramite un canale. Abbiamo anche discusso su come garantire la sicurezza del trasferimento senza fidarsi dei nodi intermedi. In questo capitolo, ci concentreremo sul trovare la migliore rotta possibile per raggiungere un nodo target.

### Il Problema del Routing in Lightning

Come abbiamo visto, in Lightning, è il nodo che invia il pagamento che deve calcolare l'intera rotta verso il destinatario, perché utilizziamo un sistema di routing a cipolla. I nodi intermedi non conoscono né il punto di origine né la destinazione finale. Sanno solo da dove proviene il pagamento e a quale nodo devono trasferirlo successivamente. Ciò significa che il nodo mittente deve mantenere una topologia locale dinamica della rete, con i nodi Lightning esistenti e i canali tra ciascuno, tenendo conto delle aperture, delle chiusure e degli aggiornamenti di stato.

![LNP201](assets/en/61.webp)
Anche con questa topologia della rete Lightning, ci sono informazioni essenziali per il routing che rimangono inaccessibili al nodo mittente, ovvero la distribuzione esatta della liquidità nei canali in un dato momento. Infatti, ogni canale mostra solo la sua **capacità totale**, ma la distribuzione interna dei fondi è nota solo ai due nodi partecipanti. Questo pone sfide per un routing efficiente, poiché il successo del pagamento dipende notevolmente dal fatto che il suo importo sia inferiore alla liquidità più bassa sulla rotta scelta. Tuttavia, le liquidità non sono tutte visibili al nodo mittente.
![LNP201](assets/en/62.webp)

### Aggiornamento della Mappa della Rete

Per mantenere aggiornata la loro mappa della rete, i nodi scambiano regolarmente messaggi attraverso un algoritmo chiamato "**_gossip_**". Si tratta di un algoritmo distribuito utilizzato per diffondere informazioni in modo epidemico a tutti i nodi della rete, che consente lo scambio e la sincronizzazione dello stato globale dei canali in pochi cicli di comunicazione. Ogni nodo propaga le informazioni a uno o più vicini scelti a caso o meno, questi, a loro volta, propagano le informazioni ad altri vicini e così via fino a raggiungere uno stato sincronizzato a livello globale.

I 2 messaggi principali scambiati tra i nodi Lightning sono i seguenti:

- "**Annunci di Canale**": messaggi che segnalano l'apertura di un nuovo canale.
- "**Aggiornamenti Canale**": messaggi di aggiornamento sullo stato di un canale, in particolare sull'evoluzione delle commissioni (ma non sulla distribuzione della liquidità).
  I nodi Lightning monitorano anche la blockchain di Bitcoin per rilevare le transazioni di chiusura del canale. Il canale chiuso viene quindi rimosso dalla mappa poiché non può più essere utilizzato per instradare i nostri pagamenti.

### Instradamento di un Pagamento

Prendiamo l'esempio di una piccola Rete Lightning con 7 nodi: Alice, Bob, 1, 2, 3, 4 e 5. Immaginiamo che Alice voglia inviare un pagamento a Bob ma debba passare attraverso nodi intermedi.

![LNP201](assets/en/63.webp)

Ecco la distribuzione attuale dei fondi in questi canali:

- **Canale tra Alice e 1**: 250.000 sats dal lato di Alice, 80.000 dal lato di 1 (capacità totale di 330.000 sats).
- **Canale tra 1 e 2**: 300.000 sats dal lato di 1, 200.000 dal lato di 2 (capacità totale di 500.000 sats).
- **Canale tra 2 e 3**: 50.000 sats dal lato di 2, 60.000 dal lato di 3 (capacità totale di 110.000 sats).
- **Canale tra 2 e 5**: 90.000 sats dal lato di 2, 160.000 dal lato di 5 (capacità totale di 250.000 sats).
- **Canale tra 2 e 4**: 180.000 sats dal lato di 2, 110.000 dal lato di 4 (capacità totale di 290.000 sats).
- **Canale tra 4 e 5**: 200.000 sats dal lato di 4, 10.000 dal lato di 5 (capacità totale di 210.000 sats).
- **Canale tra 3 e Bob**: 50.000 sats dal lato di 3, 250.000 dal lato di Bob (capacità totale di 300.000 sats).
- **Canale tra 5 e Bob**: 260.000 sats dal lato di 5, 100.000 dal lato di Bob (capacità totale di 360.000 sats).

![LNP201](assets/en/64.webp)

Per effettuare un pagamento di 100.000 sats da Alice a Bob, le opzioni di instradamento sono limitate dalla liquidità disponibile in ciascun canale. Il percorso ottimale per Alice, basato sulla distribuzione di liquidità conosciuta, potrebbe essere la sequenza `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Ma poiché Alice non conosce la distribuzione esatta dei fondi in ciascun canale, deve stimare il percorso ottimale probabilisticamente, tenendo conto dei seguenti criteri:

- **Probabilità di successo**: un canale con una capacità totale maggiore ha maggiori probabilità di contenere sufficiente liquidità. Ad esempio, il canale tra il nodo 2 e il nodo 3 ha una capacità totale di 110.000 sats, quindi è improbabile trovare 100.000 sats o più dal lato del nodo 2, anche se rimane possibile.
- **Commissioni di transazione**: nella scelta del percorso migliore, il nodo mittente considera anche le commissioni applicate da ciascun nodo intermedio e cerca di minimizzare il costo totale di instradamento.
- **Scadenza degli HTLC**: per evitare pagamenti bloccati, anche il tempo di scadenza degli HTLC è un parametro da considerare.
- **Numero di nodi intermedi**: infine, più in generale, il nodo mittente cercherà di trovare una rotta con il minor numero possibile di nodi per ridurre il rischio di fallimento e limitare le commissioni delle transazioni Lightning.
  Analizzando questi criteri, il nodo mittente può testare le rotte più probabili e tentare di ottimizzarle. Nel nostro esempio, Alice potrebbe classificare le migliori rotte come segue:

1. `Alice → 1 → 2 → 5 → Bob`, perché è la rotta più breve con la capacità più alta.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, perché questa rotta offre buone capacità, anche se è più lunga della prima.
3. `Alice → 1 → 2 → 3 → Bob`, perché questa rotta include il canale `2 → 3`, che ha una capacità molto limitata, ma rimane potenzialmente utilizzabile.

### Esecuzione del Pagamento

Alice decide di testare la sua prima rotta (`Alice → 1 → 2 → 5 → Bob`). Invia quindi un HTLC di 100.000 sats al nodo 1. Questo nodo verifica di avere sufficiente liquidità con il nodo 2 e continua la trasmissione. Il nodo 2 riceve l'HTLC dal nodo 1, ma si rende conto di non avere abbastanza liquidità nel suo canale con il nodo 5 per instradare un pagamento di 100.000 sats. Invia quindi un messaggio di errore al nodo 1, che lo trasmette ad Alice. Questa rotta è fallita.

![LNP201](assets/en/66.webp)

Alice tenta quindi di instradare il suo pagamento utilizzando la sua seconda rotta (`Alice → 1 → 2 → 4 → 5 → Bob`). Invia un HTLC di 100.000 sats al nodo 1, che lo trasmette al nodo 2, poi al nodo 4, al nodo 5 e infine a Bob. Questa volta, la liquidità è sufficiente e la rotta è funzionale. Ogni nodo sblocca il suo HTLC in cascata utilizzando il preimage fornito da Bob (il segreto _s_), che consente di finalizzare con successo il pagamento di Alice a Bob.

![LNP201](assets/en/67.webp)

La ricerca di una rotta viene condotta come segue: il nodo mittente inizia identificando le rotte migliori possibili, poi tenta i pagamenti successivamente fino a trovare una rotta funzionale.

È importante notare che Bob può fornire ad Alice informazioni nella **fattura** per facilitare l'instradamento. Ad esempio, può indicare canali vicini con sufficiente liquidità o rivelare l'esistenza di canali privati. Queste indicazioni permettono ad Alice di evitare rotte con poche possibilità di successo e di tentare per prime i percorsi raccomandati da Bob.

**Cosa dovresti ricavare da questo capitolo?**

1. I nodi mantengono una mappa della topologia della rete attraverso annunci e monitorando le chiusure dei canali sulla blockchain di Bitcoin.
2. La ricerca di una rotta ottimale per un pagamento rimane probabilistica e dipende da molti criteri.
3. Bob può fornire indicazioni nella **fattura** per guidare l'instradamento di Alice e salvarla dal testare rotte improbabili.

Nel capitolo seguente, studieremo specificamente il funzionamento delle fatture, oltre ad alcuni altri strumenti utilizzati sulla Lightning Network.

# Gli Strumenti della Lightning Network

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Fattura, LNURL e Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![fattura, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
In questo capitolo, esamineremo più da vicino il funzionamento delle **fatture** Lightning, ovvero le richieste di pagamento inviate dal nodo destinatario al nodo mittente. L'obiettivo è capire come pagare e ricevere pagamenti su Lightning. Discuteremo anche di 2 alternative alle fatture classiche: LNURL e Keysend.
![LNP201](assets/en/68.webp)

### La Struttura delle Fatture Lightning

Come spiegato nel capitolo sugli HTLCs, ogni pagamento inizia con la generazione di una **fattura** da parte del destinatario. Questa fattura viene poi trasmessa al pagatore (tramite un codice QR o copiando e incollando) per avviare il pagamento. Una fattura consiste di due parti principali:

1. **La Parte Leggibile dall'Uomo**: questa sezione contiene metadati chiaramente visibili per migliorare l'esperienza utente.
2. **Il Payload**: questa sezione include informazioni destinate alle macchine per elaborare il pagamento.

La struttura tipica di una fattura inizia con un identificatore `ln` per "Lightning", seguito da `bc` per Bitcoin, poi l'importo della fattura. Un separatore `1` distingue la parte leggibile dall'uomo dalla parte dei dati (payload).

Prendiamo come esempio la seguente fattura:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Possiamo già dividerla in 2 parti. Prima, c'è la Parte Leggibile dall'Uomo:

```invoice
lnbc100u
```

Poi la parte destinata al payload:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Le due parti sono separate da un `1`. Questo separatore è stato scelto invece di un carattere speciale per permettere un facile copia-incolla dell'intera fattura con un doppio clic.
Nella prima parte, possiamo vedere che:

- `ln` indica che si tratta di una transazione Lightning.
- `bc` indica che la rete Lightning è sulla blockchain di Bitcoin (e non sulla testnet o su Litecoin).
- `100u` indica l'importo della fattura, espresso in **microsatoshis** (`u` che significa "micro"), che qui equivale a 10.000 sats.

Per designare l'importo del pagamento, questo è espresso in sottounità di bitcoin. Ecco le unità utilizzate:

- **Millibitcoin (denotato `m`):** Rappresenta un millesimo di bitcoin.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
  $$

- **Microbitcoin (denotato `u`):** Chiamato anche talvolta "bit", rappresenta un milionesimo di bitcoin.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
  $$

- **Nanobitcoin (denotato `n`):** Rappresenta un miliardesimo di bitcoin.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
  $$

- **Picobitcoin (denotato `p`):** Rappresenta un trilionesimo di bitcoin.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
  $$

### Il Payload di una Fattura

Il payload di una fattura include diverse informazioni necessarie per l'elaborazione del pagamento:

- **Il timestamp:** Il momento della creazione della fattura, espresso in Unix Timestamp (il numero di secondi trascorsi dal 1 gennaio 1970).
- **Hashing del Segreto**: Come abbiamo visto nella sezione sugli HTLC, il nodo ricevente deve fornire al nodo mittente l'hash del preimage. Questo viene utilizzato negli HTLC per garantire la transazione. Lo abbiamo definito "_r_".
- **Il Segreto del Pagamento**: Un altro segreto viene generato dal destinatario, ma questa volta viene trasmesso al nodo mittente. Viene utilizzato nel routing a cipolla per impedire ai nodi intermedi di indovinare se il nodo successivo sia il destinatario finale o meno. Questo mantiene quindi una forma di riservatezza per il destinatario rispetto all'ultimo nodo intermedio sul percorso.
- **La Chiave Pubblica del Destinatario**: Indica al pagatore l'identificatore della persona da pagare.
- **La Durata di Scadenza**: Il tempo massimo affinché la fattura venga pagata (1 ora per impostazione predefinita).
- **Suggerimenti di Routing**: Informazioni aggiuntive fornite dal destinatario per aiutare il mittente a ottimizzare il percorso di pagamento.
- **La Firma**: Garantisce l'integrità della fattura autenticando tutte le informazioni.

Le fatture vengono poi codificate in **bech32**, lo stesso formato utilizzato per gli indirizzi Bitcoin SegWit (formato che inizia con `bc1`).

### LNURL Prelievo

In una transazione tradizionale, come un acquisto in negozio, viene generata una fattura per l'importo totale da pagare. Una volta presentata la fattura (sotto forma di codice QR o stringa di caratteri), il cliente può scansionarla e finalizzare la transazione. Il pagamento segue quindi il processo tradizionale che abbiamo studiato nella sezione precedente. Tuttavia, questo processo può talvolta essere molto ingombrante per l'esperienza utente, poiché richiede al destinatario di inviare informazioni al mittente tramite la fattura.
Per certe situazioni, come il prelievo di bitcoin da un servizio online, il processo tradizionale è troppo ingombrante. In tali casi, la soluzione di prelievo **LNURL** semplifica questo processo visualizzando un codice QR che il portafoglio del destinatario scansiona per creare automaticamente la fattura. Il servizio paga quindi la fattura e l'utente vede semplicemente un prelievo istantaneo.

LNURL è un protocollo di comunicazione che specifica un insieme di funzionalità progettate per semplificare le interazioni tra nodi Lightning e clienti, così come applicazioni di terze parti. Il prelievo LNURL, come abbiamo appena visto, è quindi solo un esempio tra altre funzionalità.
Questo protocollo si basa su HTTP e consente la creazione di link per varie operazioni, come una richiesta di pagamento, una richiesta di prelievo o altre funzionalità che migliorano l'esperienza utente. Ogni LNURL è un URL codificato in bech32 con il prefisso lnurl, che, una volta scansionato, innesca una serie di azioni automatiche sul portafoglio Lightning.
Ad esempio, la funzionalità LNURL-withdraw (LUD-03) consente di prelevare fondi da un servizio scansionando un codice QR, senza la necessità di generare manualmente una fattura. Allo stesso modo, LNURL-auth (LUD-04) consente l'accesso ai servizi online utilizzando una chiave privata sul proprio portafoglio Lightning invece di una password.

### Inviare un pagamento Lightning senza fattura: Keysend

Un altro caso interessante è il trasferimento di fondi senza aver ricevuto una fattura in precedenza, noto come "**Keysend**". Questo protocollo consente di inviare fondi aggiungendo un preimmagine nei dati di pagamento crittografati, accessibile solo dal destinatario. Questo preimmagine consente al destinatario di sbloccare l'HTLC, recuperando così i fondi senza aver generato una fattura in precedenza.

Per semplificare, in questo protocollo, è il mittente a generare il segreto utilizzato negli HTLC, piuttosto che il destinatario. Praticamente, ciò consente al mittente di effettuare un pagamento senza aver dovuto interagire con il destinatario in precedenza.

**Cosa dovresti ricavare da questo capitolo?**

1. Una **Fattura Lightning** è una richiesta di pagamento composta da una parte leggibile dall'uomo e una parte di dati macchina.
2. La fattura è codificata in **bech32**, con un separatore `1` per facilitare la copia e una parte dati contenente tutte le informazioni necessarie per elaborare il pagamento.
3. Esistono altri processi di pagamento su Lightning, in particolare **LNURL-Withdraw** per facilitare i prelievi, e **Keysend** per trasferimenti diretti senza fattura.

Nel capitolo seguente, vedremo come un operatore di nodo può gestire la liquidità nei propri canali, per non essere mai bloccato e essere sempre in grado di inviare e ricevere pagamenti sulla rete Lightning.

## Gestire la Tua Liquidità

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

In questo capitolo, esploreremo strategie per gestire efficacemente la liquidità sulla rete Lightning. La gestione della liquidità varia a seconda del tipo di utente e del contesto. Esamineremo i principi principali e le tecniche esistenti per capire meglio come ottimizzare questa gestione.

### Esigenze di Liquidità

Ci sono tre principali profili di utenti su Lightning, ognuno con specifiche esigenze di liquidità:

1. **Il Pagatore**: Questo è colui che effettua pagamenti. Hanno bisogno di liquidità in uscita per poter trasferire fondi ad altri utenti. Ad esempio, potrebbe trattarsi di un consumatore.
2. **Il Venditore (o Beneficiario)**: Questo è colui che riceve pagamenti. Hanno bisogno di liquidità in entrata per poter accettare pagamenti al loro nodo. Ad esempio, potrebbe trattarsi di un'attività commerciale o di un negozio online.
3. **Il Router**: Un nodo intermediario, spesso specializzato nel routing dei pagamenti, che deve ottimizzare la sua liquidità in ogni canale per instradare quanti più pagamenti possibile e guadagnare commissioni.

Questi profili ovviamente non sono fissi; un utente può passare da pagatore a beneficiario a seconda delle transazioni. Ad esempio, Bob potrebbe ricevere il suo stipendio su Lightning dal suo datore di lavoro, ponendosi nella posizione di un "venditore" che richiede liquidità in entrata. Successivamente, se vuole usare il suo stipendio per comprare cibo, diventa un "pagatore" e deve quindi avere liquidità in uscita.

Per capire meglio, prendiamo l'esempio di una semplice rete composta da tre nodi: l'acquirente (Alice), il router (Suzie) e il venditore (Bob).

![LNP201](assets/en/71.webp)

Immagina che l'acquirente voglia inviare 30.000 satoshi al venditore e che il pagamento passi attraverso il nodo del router. Ogni parte deve quindi avere una quantità minima di liquidità nella direzione del pagamento:

- Il pagatore deve avere almeno 30.000 satoshi dalla sua parte del canale con il router.
- Il venditore deve avere un canale dove 30.000 satoshi sono dalla parte opposta per poterli ricevere.
- Il router deve avere 30.000 satoshi dalla parte del pagatore nel loro canale, e anche 30.000 satoshi dalla loro parte nel canale con il venditore, per poter instradare il pagamento.

![LNP201](assets/en/72.webp)

### Strategie di Gestione della Liquidità

I pagatori devono assicurarsi di mantenere sufficiente liquidità dalla loro parte dei canali per garantire la liquidità in uscita. Questo si rivela relativamente semplice, poiché è sufficiente aprire nuovi canali Lightning per avere questa liquidità. Infatti, i fondi iniziali bloccati nel multisig on-chain sono interamente dalla parte del pagatore nel canale Lightning all'inizio. La capacità di pagamento è quindi assicurata finché vengono aperti canali con fondi sufficienti. Quando la liquidità in uscita è esaurita, è sufficiente aprire nuovi canali.
D'altra parte, per il venditore, il compito è più complesso. Per poter ricevere pagamenti, devono avere liquidità dalla parte opposta dei loro canali. Pertanto, aprire un canale non è sufficiente: devono anche effettuare un pagamento in questo canale per spostare la liquidità dall'altra parte prima di poter ricevere pagamenti. Per certi profili di utenti Lightning, come i commercianti, esiste una chiara sproporzione tra ciò che il loro nodo invia e ciò che riceve, poiché l'obiettivo di un'attività commerciale è principalmente quello di incassare più di quanto spende, al fine di generare un profitto. Fortunatamente, per questi utenti con specifiche esigenze di liquidità in entrata, esistono diverse soluzioni:

- **Attrarre canali**: Il commerciante beneficia di un vantaggio dovuto al volume di pagamenti in entrata previsti sul loro nodo. Tenendo conto di ciò, possono cercare di attrarre nodi router che sono alla ricerca di entrate dalle commissioni di transazione e che potrebbero aprire canali verso di loro, sperando di instradare i loro pagamenti e riscuotere le commissioni associate.
- **Movimento di liquidità**: Il venditore può anche aprire un canale e trasferire parte dei fondi verso il lato opposto effettuando pagamenti fittizi verso un altro nodo, che restituirà il denaro in un altro modo. Vedremo nella prossima parte come effettuare questa operazione.
- **Apertura triangolare**: Esistono piattaforme per i nodi che desiderano aprire canali in modo collaborativo, consentendo a ciascuno di beneficiare immediatamente di liquidità in entrata e in uscita. Ad esempio, [LightningNetwork+](https://lightningnetwork.plus/) offre questo servizio. Se Alice, Bob e Suzie vogliono aprire un canale con 100.000 sats, possono accordarsi su questa piattaforma perché Alice apra un canale verso Bob, Bob verso Suzie e Suzie verso Alice. In questo modo, ciascuno ha 100.000 sats di liquidità in uscita e 100.000 sats di liquidità in entrata, avendo bloccato solo 100.000 sats.

![LNP201](assets/en/73.webp)

- **Acquisto di canali**: Esistono anche servizi per affittare canali Lightning per ottenere liquidità in entrata, come [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) o [Lightning Labs Pool](https://lightning.engineering/pool/). Ad esempio, Alice può acquistare un canale di un milione di satoshi verso il suo nodo per poter ricevere pagamenti.

![LNP201](assets/en/74.webp)

Infine, per i router, il cui obiettivo è massimizzare il numero di pagamenti elaborati e le commissioni raccolte, devono:

- Aprire canali ben finanziati con nodi strategici.
- Regolare regolarmente la distribuzione dei fondi nei canali secondo le necessità della rete.

### Il servizio Loop Out

Il servizio [Loop Out](https://lightning.engineering/loop/), offerto da Lightning Labs, consente di spostare la liquidità verso il lato opposto del canale recuperando i fondi sulla blockchain di Bitcoin. Ad esempio, Alice invia 1 milione di satoshi tramite Lightning a un nodo loop, che poi restituisce quei fondi a lei in bitcoin on-chain. Questo bilancia il suo canale con 1 milione di satoshi su ciascun lato, ottimizzando la sua capacità di ricevere pagamenti.

![LNP201](assets/en/75.webp)

Pertanto, questo servizio consente di ottenere liquidità in entrata recuperando i propri bitcoin on-chain, il che aiuta a limitare l'immobilizzazione di contanti necessaria per accettare pagamenti con Lightning.

**Cosa dovresti ricavare da questo capitolo?**

- Per inviare pagamenti su Lightning, devi avere abbastanza liquidità dal tuo lato nei tuoi canali. Per aumentare questa capacità di invio, basta aprire nuovi canali.
- Per ricevere pagamenti, è necessario avere liquidità sul lato opposto nei tuoi canali. Aumentare questa capacità di ricezione è più complesso, poiché richiede che altri aprano canali verso di te, o che effettuino pagamenti (fittizi o reali) per spostare la liquidità dall'altro lato.
- Mantenere la liquidità desiderata può essere ancora più sfidante a seconda dell'uso dei canali. Ecco perché esistono strumenti e servizi per aiutare a bilanciare i canali come desiderato.

Nel prossimo capitolo, propongo di rivedere i concetti più importanti di questa formazione.

# Vai oltre

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Conclusione della formazione

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![conclusione](https://youtu.be/MaWpD0rbkVo)
In questo capitolo finale che segna la conclusione del corso LNP201, propongo di rivedere insieme i concetti importanti che abbiamo coperto.

L'obiettivo di questo corso era fornirvi una comprensione completa e tecnica della Lightning Network. Abbiamo scoperto come la Lightning Network si basi sulla blockchain di Bitcoin per eseguire transazioni off-chain, mantenendo al contempo le caratteristiche fondamentali di Bitcoin, in particolare l'assenza della necessità di fidarsi degli altri nodi.

### Canali di Pagamento

Nei capitoli iniziali, abbiamo esplorato come due parti, aprendo un canale di pagamento, possano effettuare transazioni al di fuori della blockchain di Bitcoin. Ecco i passaggi trattati:

1. **Apertura del Canale**: La creazione del canale avviene tramite una transazione Bitcoin che blocca i fondi in un indirizzo multisignature 2/2. Questo deposito rappresenta il canale Lightning sulla blockchain.

![LNP201](assets/en/76.webp) 2. **Transazioni nel Canale**: In questo canale, è quindi possibile effettuare numerose transazioni senza doverle pubblicare sulla blockchain. Ogni transazione Lightning crea un nuovo stato del canale riflesso in una transazione di impegno.
![LNP201](assets/en/77.webp)

3. **Sicurezza e Chiusura**: I partecipanti si impegnano nel nuovo stato del canale scambiandosi chiavi di revoca per assicurare i fondi e prevenire eventuali frodi. Entrambe le parti possono chiudere il canale cooperativamente effettuando una nuova transazione sulla blockchain di Bitcoin, o come ultima risorsa attraverso una chiusura forzata. Quest'ultima opzione, sebbene meno efficiente perché più lunga e talvolta mal valutata in termini di commissioni, consente comunque il recupero dei fondi. In caso di frode, la vittima può punire il truffatore recuperando tutti i fondi del canale sulla blockchain.

![LNP201](assets/en/78.webp)

### La Rete dei Canali

Dopo aver studiato i canali isolati, abbiamo esteso la nostra analisi alla rete dei canali:

- **Routing**: Quando due parti non sono direttamente collegate da un canale, la rete consente il routing attraverso nodi intermediari. I pagamenti transitano quindi da un nodo all'altro.

![LNP201](assets/en/79.webp)

- **HTLCs**: I pagamenti che transitano attraverso nodi intermediari sono assicurati da "_Hash Time-Locked Contracts_" (HTLC), che consentono di bloccare i fondi fino al completamento del pagamento da un capo all'altro.

![LNP201](assets/en/80.webp)

- **Onion Routing**: Per garantire la riservatezza del pagamento, l'onion routing maschera la destinazione finale ai nodi intermediari. Il nodo mittente deve quindi calcolare l'intero percorso, ma in assenza di informazioni complete sulla liquidità dei canali, procede attraverso tentativi successivi per instradare il pagamento.

![LNP201](assets/en/81.webp)

### Gestione della Liquidità

Abbiamo visto che la gestione della liquidità è una sfida su Lightning per garantire il flusso regolare dei pagamenti. Inviare pagamenti è relativamente semplice: basta aprire un canale. Tuttavia, ricevere pagamenti richiede di avere liquidità sul lato opposto dei propri canali. Ecco alcune strategie discusse:

- **Attrarre Canali**: Incoraggiando altri nodi ad aprire canali verso di sé, un utente ottiene liquidità in entrata.

- **Spostare la Liquidità**: Inviando pagamenti ad altri canali, la liquidità si sposta sul lato opposto.

![LNP201](assets/en/82.webp)

- **Utilizzare Servizi come Loop e Pool**: Questi servizi consentono di riequilibrare o acquistare canali con liquidità sul lato opposto.
  ![LNP201](assets/en/83.webp)
- **Aperture Collaborative**: Esistono anche piattaforme disponibili per connettersi al fine di eseguire aperture triangolari e avere liquidità in entrata.

![LNP201](assets/en/84.webp)

# Conclusione

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Valuta questo corso

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Esame finale

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusione

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
Congratulazioni! 🎉

Hai completato il corso LNP 201 - Introduzione al Lightning Network!

Puoi essere orgoglioso di te stesso, perché non è un argomento facile.

Poche persone si addentrano così profondamente nella tana del coniglio di Bitcoin.

Un grande ringraziamento a **Fanis Michalakis** per averci offerto questo eccellente corso gratuito sul funzionamento tecnico del Lightning Network.

Non esitare a seguirlo su [Twitter](https://x.com/FanisMichalakis), sul [suo blog](https://fanismichalakis.fr/) o attraverso il suo lavoro su [LN Markets](https://lnmarkets.com/).

Ora che padroneggi il Lightning Network, ti invito a esplorare i nostri altri corsi gratuiti su Plan ₿ Network per approfondire gli altri aspetti dell'invenzione di Satoshi Nakamoto:

#### Comprendi il funzionamento di un portafoglio Bitcoin con

https://planb.network/courses/cyp201

#### Scopri la storia delle origini di Bitcoin con

https://planb.network/courses/his201

#### Configura un server di pagamento BTC con

https://planb.network/courses/btc305

#### Padroneggia i principi della privacy in Bitcoin

https://planb.network/courses/btc204

#### Scopri le basi del mining con

https://planb.network/courses/min201

#### Impara a creare la tua comunità Bitcoin con

https://planb.network/courses/btc302
