---
name: Introduzione teorica alla rete Lightning
goal: Scoprite la rete Lightning da un punto di vista tecnico
objectives: []
  - Comprendere il funzionamento dei canali di rete.
  - Familiarizzare con i termini HTLC, LNURL e UTXO.
  - Comprendere la gestione della liquidità e le commissioni LNN.
  - Riconoscere la rete Lightning come una rete.
  - Comprendere gli usi teorici della rete Lightning.
---
# Un viaggio nel secondo strato di Bitcoin

Immergetevi nel cuore della Lightning Network, un sistema essenziale per il futuro delle transazioni Bitcoin. LNP201 è un corso teorico sul funzionamento tecnico di Lightning. Rivela i fondamenti e il funzionamento interno di questa rete di secondo livello, progettata per rendere i pagamenti in Bitcoin veloci, economici e scalabili.

Grazie alla sua rete di canali di pagamento, Lightning consente transazioni rapide e sicure senza registrare ogni scambio sulla blockchain di Bitcoin. Nel corso dei capitoli, imparerete come si aprono, si gestiscono e si chiudono i canali, come si instradano i pagamenti in modo sicuro attraverso i nodi intermedi riducendo al minimo la necessità di fiducia e come si gestisce la liquidità. Scoprirete cosa sono le transazioni di impegno, le HTLC, le chiavi di revoca, i meccanismi di punizione, il routing a cipolla e le fatture.

Che siate principianti o utenti esperti di Bitcoin, questo corso vi fornirà informazioni preziose per comprendere e utilizzare la Lightning Network. Anche se nelle prime parti verranno trattati alcuni dei fondamenti del funzionamento di Bitcoin, è essenziale padroneggiare le basi dell'invenzione di Satoshi prima di immergersi in LNP201.

Buona scoperta!

+++
# I fondamenti

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Capire la rete Lightning

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Comprendre le lightning Network](https://youtu.be/PszWk046x-I)

Benvenuti a LNP201, un corso di formazione che spiega il funzionamento tecnico della rete Lightning.

La Lightning Network è una rete di canali di pagamento costruita sulla base del protocollo Bitcoin, con l'obiettivo di consentire transazioni veloci e a basso costo. Consente la creazione di canali di pagamento tra i partecipanti, all'interno dei quali le transazioni possono essere effettuate quasi istantaneamente e a costi minimi, senza dover registrare ogni singola transazione sulla blockchain. La Lightning Network mira quindi a migliorare la scalabilità di Bitcoin e a renderne possibile l'utilizzo per pagamenti di basso valore.

Prima di esplorare l'aspetto "rete", è importante comprendere il concetto di **canale di pagamento** su Lightning, il suo funzionamento e le sue caratteristiche specifiche. Questo è l'argomento di questo primo capitolo.

### Il concetto di canale di pagamento

Un canale di pagamento consente a due parti, in questo caso **Alice** e **Bob**, di scambiarsi fondi sulla rete Lightning. Ogni protagonista ha un nodo, simboleggiato da un cerchio, e il canale tra loro è rappresentato da un segmento.

![LNP201](assets/fr/01.webp)

Nel nostro esempio, Alice ha 100.000 satoshis sul suo lato del canale e Bob ne ha 30.000, per un totale di 130.000 satoshis, che è la **capacità del canale**.

**Ma cos'è un satoshi?

Il **satoshi** (o "sat") è un'unità di conto in Bitcoin. Come un centesimo per l'euro, un satoshi è semplicemente una frazione di un Bitcoin. Un satoshi equivale a **0,00000001 Bitcoin**, o a un centomilionesimo di Bitcoin. L'uso dei satoshi diventa sempre più pratico con l'aumento del valore del Bitcoin.

### Allocazione dei fondi nel canale

Torniamo al canale di pagamento. La nozione chiave è "lato canale". Ogni partecipante dispone di fondi sul proprio lato del canale: Alice 100.000 satoshi e Bob 30.000. Come abbiamo visto, la somma di questi fondi rappresenta la capacità totale del canale, un elemento fissato al momento dell'apertura.

![LNP201](assets/fr/02.webp)

Facciamo un esempio di transazione Lightning. Se Alice desidera inviare 40.000 satoshis a Bob, ciò è possibile, poiché dispone di fondi sufficienti (100.000 satoshis). Dopo questa transazione, Alice avrà 60.000 satoshis e Bob 70.000.

![LNP201](assets/fr/03.webp)

La **capacità del canale** di 130.000 satoshi rimane costante. Ciò che cambia è l'allocazione dei fondi. Questo sistema non permette di inviare più fondi di quelli che si hanno. Ad esempio, se Bob volesse inviare 80.000 satoshi ad Alice, non potrebbe farlo, perché ne ha solo 70.000.

Un altro modo per immaginare l'allocazione dei fondi è quello di immaginare un **cursore** che indichi dove si trovano i fondi nel canale. Inizialmente, con 100.000 satoshi per Alice e 30.000 per Bob, il cursore è logicamente dalla parte di Alice. Dopo la transazione di 40.000 satoshi, il cursore si sposta leggermente dalla parte di Bob, che ora ha 70.000 satoshi.

![LNP201](assets/fr/04.webp)

Questa rappresentazione può essere utile per immaginare l'equilibrio dei fondi in un canale.

### Le regole fondamentali di un canale di pagamento

Il primo punto da ricordare è che la **capacità del canale** è fissa. È un po' come il diametro di un tubo: determina la quantità massima di fondi che possono essere inviati attraverso il canale in una sola volta.

Ad esempio, se Alice dispone di 130.000 satoshis, può inviare a Bob un massimo di 130.000 satoshis in una singola transazione. Tuttavia, Bob può rispedire questi fondi ad Alice, in parte o per intero.

È importante capire che la capacità fissa del canale limita l'importo massimo di una transazione, ma non il numero totale di transazioni possibili, né il volume complessivo dei fondi scambiati all'interno del canale.

**Che cosa dovreste imparare da questo capitolo?

- La capacità di un canale è fissa e determina l'importo massimo che può essere inviato in una singola transazione.
- I fondi di un canale sono divisi tra i due partecipanti e ciascuno può inviare all'altro solo i fondi che ha dalla sua parte.
- La rete Lightning consente di scambiare fondi in modo rapido ed efficiente, rispettando i limiti imposti dalla capacità del canale.
Questo è il termine di questo primo capitolo, in cui abbiamo gettato le basi della rete Lightning. Nei prossimi capitoli vedremo come aprire un canale e come approfondire i concetti che abbiamo trattato qui.

## Bitcoin, indirizzi, UTXO e transazioni

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, adresses, utxo et transactions](https://youtu.be/cadCJ2V7zTg)

Questo capitolo è un po' speciale perché non è direttamente dedicato a Lightning, ma a Bitcoin. Infatti, la rete Lightning è un overlay di Bitcoin. È quindi essenziale avere una buona comprensione di alcuni concetti fondamentali di Bitcoin per poter comprendere correttamente il funzionamento di Lightning nei capitoli successivi. In questo capitolo rivedremo le basi degli indirizzi di ricezione Bitcoin, degli UTXO e del funzionamento delle transazioni Bitcoin.

### Indirizzi Bitcoin, chiavi private e pubbliche

Un indirizzo Bitcoin è una sequenza di caratteri derivati da una **chiave pubblica**, a sua volta calcolata da una **chiave privata**. Come probabilmente sapete, lo usiamo per bloccare i bitcoin, il che equivale a riceverli nel nostro portafoglio.

La chiave privata è un elemento segreto che non deve mai essere condiviso**, mentre la chiave pubblica e l'indirizzo possono essere condivisi senza alcun rischio per la sicurezza (la loro divulgazione rappresenta solo un rischio per la vostra riservatezza). Ecco una rappresentazione comune che adotteremo in questo corso di formazione:

- Le chiavi private** saranno rappresentate **verticalmente**.
- Le **chiavi pubbliche** saranno rappresentate **orizzontalmente**.
- Il loro colore indica chi li possiede (Alice in arancione e Bob in nero...).
### Transazioni Bitcoin: invio di fondi e script

In Bitcoin, una transazione consiste nell'invio di fondi da un indirizzo a un altro. Ad esempio, Alice invia 0,002 Bitcoin a Bob. Alice utilizza la chiave privata associata al suo indirizzo per **firmare** la transazione, dimostrando di essere effettivamente in grado di spendere questi fondi. Ma cosa succede esattamente dietro questa transazione? I fondi di un indirizzo Bitcoin sono bloccati da un **script**, una sorta di mini-programma che impone determinate condizioni sulla spesa dei fondi.

Lo script più comune richiede una firma con la chiave privata associata all'indirizzo. Quando Alice firma una transazione con la sua chiave privata, **sblocca lo script** che blocca i fondi, che possono quindi essere trasferiti. Il trasferimento dei fondi comporta l'aggiunta di un nuovo script ai fondi, stabilendo che per spenderli, questa volta è necessaria una firma con la chiave privata di **Bob**.

![LNP201](assets/fr/05.webp)

### UTXO: uscite di transazione non utilizzate

In Bitcoin, ciò che si scambia non sono direttamente i bitcoin, ma gli **UTXO** (_Unspent Transaction Outputs_).

Un UTXO è un pezzo di bitcoin che può avere qualsiasi valore, ad esempio **2.000 bitcoin**, **8 bitcoin** o **8.000 sats**. Ogni UTXO è bloccato da uno script e per spenderlo è necessario soddisfare le condizioni dello script, spesso una firma con la chiave privata corrispondente a un determinato indirizzo di ricezione.

Gli UTXO non possono essere divisi. Ogni volta che vengono utilizzati per spendere l'importo di bitcoin che rappresentano, deve essere fatto per intero. È un po' come una banconota: se avete una banconota da 10 euro e dovete al panettiere 5 euro, non potete semplicemente tagliarla a metà. Dovete dargli la banconota da 10 euro e lui vi darà 5 euro di resto. È esattamente lo stesso principio per UTXO su Bitcoin! Ad esempio, quando Alice sblocca uno script con la sua chiave privata, sblocca l'intero UTXO. Se desidera inviare a Bob solo una parte dei fondi rappresentati da questo UTXO, può "frammentarlo" in diversi altri più piccoli. Invierà quindi 0,0015 BTC a Bob e rimanderà il resto, 0,0005 BTC, a se stessa tramite un **indirizzo di scambio**.

Ecco un esempio di transazione con 2 uscite:

- Un UTXO di 0,0015 BTC per Bob, bloccato da uno script che richiede una firma con la chiave privata di Bob.
- Un UTXO di 0,0005 BTC per Alice, bloccato da uno script che richiede la propria firma.
![LNP201](assets/fr/06.webp)

### Indirizzi a più firme

Oltre agli indirizzi semplici generati da una singola chiave pubblica, è possibile creare **indirizzi a firma multipla** da più chiavi pubbliche. Un caso particolare di interesse per la Lightning Network è l'indirizzo **2/2 multisignature**, generato da due chiavi pubbliche:

![LNP201](assets/fr/07.webp)

Per spendere i fondi bloccati con questo indirizzo a firma multipla 2/2, è necessario firmare con le due chiavi private associate alle chiavi pubbliche.

![LNP201](assets/fr/08.webp)

Questo tipo di indirizzo è proprio la rappresentazione sulla blockchain di Bitcoin dei canali di pagamento della Lightning Network.

**Che cosa dovreste imparare da questo capitolo?

- Un indirizzo di **Bitcoin** deriva da una chiave pubblica, a sua volta derivata da una chiave privata.
- I fondi su Bitcoin sono bloccati da **scritture** e per spenderli è necessario soddisfare la scrittura, che di solito consiste nel fornire una firma con la chiave privata corrispondente.
- Gli **UTXO** sono pezzi di bitcoin bloccati da script e ogni transazione su Bitcoin consiste nello sbloccare un UTXO per poi crearne uno o più nuovi in cambio.
- gli indirizzi multi-firma 2/2** richiedono la firma di due chiavi private per spendere i fondi. Sono questi indirizzi specifici che Lightning utilizza per creare canali di pagamento.
Questo capitolo su Bitcoin ci ha dato l'opportunità di rivedere alcuni concetti essenziali per il futuro. Nel prossimo capitolo scopriremo come funziona l'apertura dei canali sulla Lightning Network.

# Apertura e chiusura dei canali

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Apertura del canale

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![ouvrir un canal](https://youtu.be/B2caBC0Rxko)

In questo capitolo vedremo da vicino come aprire un canale di pagamento sulla Lightning Network e capiremo il legame tra questa operazione e il sistema Bitcoin sottostante.

### Canali di illuminazione

Come abbiamo visto nel primo capitolo, un **canale di pagamento** su Lightning può essere paragonato a un "tubo" per lo scambio di fondi tra due partecipanti (**Alice** e **Bob** nei nostri esempi). La capacità di questo canale corrisponde alla somma dei fondi disponibili da ciascuna parte. Nel nostro esempio, Alice dispone di **100.000 satoshis** e Bob di **30.000 satoshis**, per una **capacità totale** di **130.000 satoshis**.

![LNP201](assets/fr/09.webp)

### Livelli di scambio di informazioni

È importante distinguere tra i diversi livelli di scambio di fulmini:

- Comunicazioni peer-to-peer (protocollo Lightning)**: sono i messaggi che i nodi Lightning si inviano a vicenda per comunicare. Questi messaggi sono rappresentati come linee nere tratteggiate nei nostri diagrammi.
- Canali di pagamento (protocollo Lightning)**: sono i percorsi per lo scambio di fondi su Lightning, che rappresenteremo come linee nere.
- Transazioni Bitcoin (protocollo Bitcoin)** : si tratta di transazioni effettuate onchain, che rappresenteremo con linee arancioni.
![LNP201](assets/fr/10.webp)

Si noti che un nodo Lightning può comunicare tramite il protocollo P2P senza aprire un canale, ma per lo scambio di fondi è necessario un canale.

### Procedura per aprire un canale Lightning

1. **Scambio di messaggi**: Alice vuole aprire un canale con Bob. Gli invia un messaggio contenente l'importo che vuole depositare nel canale (130.000 sats) e la sua chiave pubblica. Bob risponde condividendo la propria chiave pubblica.

![LNP201](assets/fr/11.webp)

2. **Creazione di un indirizzo a firma multipla**: Con queste due chiavi pubbliche, Alice crea un indirizzo **2/2 a firma multipla**, il che significa che i fondi depositati successivamente a questo indirizzo richiederanno entrambe le firme (Alice e Bob) per essere spesi.

![LNP201](assets/fr/12.webp)

3. **Transazione di deposito**: Alice prepara una transazione Bitcoin per depositare fondi su questo indirizzo a firma multipla. Ad esempio, può decidere di inviare **130.000 satoshis** a questo indirizzo a firma multipla. Questa transazione è **costruita ma non ancora pubblicata** sulla blockchain.

![LNP201](assets/fr/13.webp)

4. **Transazione di prelievo**: Prima di pubblicare la transazione di deposito, Alice costruisce una transazione di prelievo in modo da poter recuperare i propri fondi in caso di problemi con Bob. Infatti, quando Alice pubblica la transazione di deposito, i suoi satelliti saranno bloccati su un indirizzo 2/2 a firma multipla che richiede sia la sua firma che quella di Bob per essere rilasciata. Alice si assicura contro questo rischio di perdita costruendo la transazione di prelievo che le permette di recuperare i suoi fondi.

![LNP201](assets/fr/14.webp)

5. **Firma di Bob**: Alice invia a Bob la transazione di deposito come prova e gli chiede di firmare la transazione di prelievo. Una volta ottenuta la firma di Bob sulla transazione di prelievo, Alice ha la certezza di poter recuperare i suoi fondi in qualsiasi momento, poiché manca solo la sua firma per sbloccare la multi-firma.

![LNP201](assets/fr/15.webp)

6. **Pubblicazione della transazione di deposito**: Una volta ottenuta la firma di Bob, Alice può pubblicare la transazione di deposito sulla blockchain Bitcoin, aprendo così ufficialmente il canale Lightning tra i due utenti.

![LNP201](assets/fr/16.webp)

### Quando è aperto il canale?

Il canale è considerato aperto quando la transazione di deposito è inclusa in un blocco Bitcoin e ha raggiunto una certa profondità di conferma (numero di blocchi successivi).

**Che cosa dovreste imparare da questo capitolo?

- L'apertura di un canale inizia con lo scambio di **messaggi** tra le due parti (scambio di importi e chiavi pubbliche).
- Un canale si forma creando un indirizzo **2/2 a firma multipla** e depositandovi fondi tramite una transazione Bitcoin.
- La persona che apre il canale garantisce di poter **recuperare i propri fondi** attraverso un'operazione di prelievo firmata dall'altra parte prima di pubblicare l'operazione di deposito.
Nel prossimo capitolo analizzeremo il funzionamento tecnico di una transazione Lightning in un canale.

## Operazione di impegno

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![trasanction lightning & transaction d'engagement](https://youtu.be/aPqI34tpypM)

In questo capitolo vedremo il funzionamento tecnico di una transazione all'interno di un canale della rete Lightning, cioè quando i fondi vengono spostati da un lato all'altro del canale.

### Richiamo del ciclo di vita di un canale

Come si è visto, un canale Lightning inizia con la sua **apertura** tramite una transazione Bitcoin. Il canale può essere **chiuso** in qualsiasi momento, sempre tramite una transazione Bitcoin. Tra questi due momenti, un numero quasi infinito di transazioni può essere effettuato all'interno del canale, senza passare per la blockchain Bitcoin. Vediamo cosa succede durante una transazione all'interno del canale.

![LNP201](assets/fr/17.webp)

### Stato iniziale del canale

Quando il canale viene aperto, Alice ha depositato **130.000 satoshis** sull'indirizzo multi-firma del canale. Pertanto, nello stato iniziale, tutti i fondi sono dalla parte di Alice. Prima di aprire il canale, Alice ha anche fatto firmare a Bob una **transazione di prelievo**, che le avrebbe permesso di recuperare i suoi fondi se avesse voluto chiudere il canale.

![LNP201](assets/fr/18.webp)

### Operazioni non pubblicate: operazioni di impegno

Quando Alice effettua una transazione nel canale per inviare fondi a Bob, viene creata una nuova transazione Bitcoin per riflettere questo cambiamento nella distribuzione dei fondi. Questa transazione, chiamata **transazione di impegno**, non viene pubblicata sulla blockchain, ma rappresenta il nuovo stato del canale dopo la transazione Lightning.

Ad esempio, Alice invia 30.000 satoshis a Bob:

- Inizialmente**: Alice possiede 130.000 satoshi.
- Dopo la transazione**: Alice possiede 100.000 satoshis e Bob 30.000 satoshis.
Per convalidare questo trasferimento, Alice e Bob creano una nuova **transazione Bitcoin non pubblicata** che invia **100.000 satoshis ad Alice** e **30.000 satoshis a Bob** dall'indirizzo con firma multipla. Entrambe le parti costruiscono questa transazione in modo indipendente, ma con gli stessi dati (importi e indirizzi). Una volta costruita, ciascuna parte firma la transazione e scambia le firme con l'altra. Ciò consente a ciascuna parte di pubblicare la transazione in qualsiasi momento, se necessario, per recuperare la propria quota del canale sulla blockchain principale di Bitcoin.

![LNP201](assets/fr/19.webp)

### Processo di trasferimento: la fattura

Quando Bob desidera ricevere fondi, invia ad Alice una **fattura_** di 30.000 satoshi. Alice procede quindi al pagamento di questa fattura avviando il trasferimento all'interno del canale. Come abbiamo visto, questo processo si basa sulla creazione e sulla firma di una nuova **transazione di impegno**.

Ogni transazione di impegno rappresenta la nuova distribuzione dei fondi nel canale dopo il trasferimento. In questo esempio, dopo la transazione, Bob dispone di 30.000 satoshis e Alice di 100.000 satoshis. Se uno dei due partecipanti decidesse di pubblicare questa transazione di impegno sulla blockchain, il canale verrebbe chiuso e i fondi verrebbero distribuiti in base all'ultima ripartizione.

![LNP201](assets/fr/20.webp)

### Nuovo stato dopo una seconda transazione

Facciamo un altro esempio: dopo la prima transazione in cui Alice ha inviato 30.000 satoshis a Bob, Bob decide di inviare **10.000 satoshis ad Alice**. Questo crea un nuovo stato di canale. La nuova **transazione di impegno** rappresenterà questa distribuzione aggiornata:

- Alice** ora possiede **110.000 satoshi**.
- Bob** possiede **20.000 satoshi**.
![LNP201](assets/fr/21.webp)

Ancora una volta, questa transazione non viene pubblicata sulla blockchain, ma può esserlo in qualsiasi momento se il canale viene chiuso.

In breve, quando i fondi vengono trasferiti all'interno di un Lightning :

- Alice e Bob creano una nuova **transazione di impegno**, che riflette la nuova distribuzione dei fondi.
- Questa transazione Bitcoin è **firmata** da entrambe le parti, ma **non pubblicata** sulla blockchain Bitcoin finché il canale rimane aperto.
- Le transazioni di impegno garantiscono che ogni partecipante possa recuperare i propri fondi in qualsiasi momento sulla blockchain Bitcoin pubblicando l'ultima transazione firmata.
Tuttavia, c'è un potenziale difetto in questo sistema, che affronteremo nel prossimo capitolo. In quell'occasione, vedremo come ogni partecipante può proteggersi da un tentativo di imbroglio da parte dell'altra parte.

## Chiave di revoca

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

![transactions partie 2](https://youtu.be/RRvoVTLRJ84)

In questo capitolo vedremo più da vicino come funzionano le transazioni su Lightning Network e i meccanismi di protezione contro gli imbrogli, per garantire che ogni parte rispetti le regole all'interno di un canale.

### Promemoria: operazioni di impegno

Come già menzionato, le transazioni Lightning si basano su **transazioni di impegno** non pubblicate. Queste transazioni riflettono l'attuale distribuzione dei fondi nel canale. Quando viene effettuata una nuova transazione Lightning, viene creata una nuova transazione di impegno, firmata da entrambe le parti per riflettere il nuovo stato del canale.

Facciamo un semplice esempio:

- Stato iniziale**: Alice possiede **100.000 satoshis**, Bob **30.000 satoshis**.
- Dopo una transazione in cui Alice invia **40.000 satoshis** a Bob, la nuova transazione di impegno distribuisce i fondi come segue:
  - Alice : **60.000 satoshis**
  - Bob: **70.000 satoshis**
![LNP201](assets/fr/22.webp)

Entrambe le parti possono, in qualsiasi momento, pubblicare l'**ultima transazione di impegno firmata** per chiudere il canale e recuperare i propri fondi.

### La falla: imbrogliare pubblicando una vecchia transazione

Un potenziale problema sorge se una delle parti decide di **truffare** pubblicando una transazione di impegno più vecchia. Ad esempio, Alice potrebbe pubblicare una transazione di impegno più vecchia in cui possiede **100.000 satoshis**, anche se in realtà ne possiede solo **60.000**. Questo le permetterebbe di rubare **40.000 satoshis** a Bob.

![LNP201](assets/fr/23.webp)

Peggio ancora, Alice potrebbe pubblicare la primissima transazione di prelievo, quella precedente all'apertura del canale, in cui possedeva **130.000 satoshi**, e quindi rubare gli interi fondi del canale.

![LNP201](assets/fr/24.webp)

### Soluzione: la chiave di revoca e il timelock

Per evitare questo imbroglio da parte di Alice, su Lightning Network aggiungiamo **meccanismi di sicurezza** alle transazioni di impegno:

1. **Timelock**: Ogni transazione di impegno include un timelock per i fondi di Alice. Il timelock è una primitiva dello smart contract che definisce una condizione temporale da soddisfare prima che una transazione possa essere aggiunta a un blocco. Ciò significa che Alice non potrà riavere i suoi fondi fino a un certo numero di blocchi dopo, se pubblica una delle transazioni di impegno. Questo timelock inizia ad essere applicato non appena la transazione di impegno viene confermata. La sua durata è generalmente proporzionale alla dimensione del canale, ma può anche essere configurata manualmente.

2. **chiave di revoca**: I fondi di Alice possono essere spesi immediatamente anche da Bob se questi possiede la **chiave di revoca**. Questa chiave consiste in un segreto detenuto da Alice e in un segreto detenuto da Bob. Si noti che questo segreto è diverso per ogni transazione di impegno.

Grazie a questi due meccanismi combinati, Bob ha il tempo di rilevare il tentativo di imbroglio di Alice e di punirla recuperando il suo output grazie alla chiave di revoca, il che per Bob significa recuperare tutti i fondi nel canale. La nostra nuova transazione di impegno avrà ora il seguente aspetto:

![LNP201](assets/fr/25.webp)

Vediamo più da vicino come funziona questo meccanismo.

### Processo di aggiornamento delle transazioni

Quando Alice e Bob aggiornano lo stato del canale con una nuova transazione Lightning, si scambiano a monte i rispettivi **segreti** per la precedente transazione di impegno (quella che sta per diventare obsoleta e che potrebbe permettere a uno dei due di barare). Ciò significa che, nel nuovo stato del canale :

- Alice e Bob hanno una nuova transazione di impegno che rappresenta l'attuale distribuzione dei fondi dopo la transazione Lightning.
- Ciascuno dei due possiede il segreto dell'altro per la transazione precedente, il che consente di utilizzare la chiave di revoca solo se uno dei due tenta di imbrogliare pubblicando una transazione con uno stato vecchio nei mempool dei nodi Bitcoin. Infatti, per punire la controparte, è necessario detenere entrambi i segreti e la transazione di impegno dell'altro, che include l'input firmato. Senza questa transazione, la sola chiave di revoca è inutile. L'unico modo per ottenere questa transazione è recuperarla dai mempool (nelle transazioni in attesa di conferma) o dalle transazioni confermate sulla blockchain durante il timelock, il che dimostra che la controparte sta cercando di imbrogliare, volontariamente o meno.
Facciamo un esempio per capire questo processo:

1. **Stato iniziale**: Alice possiede **100.000 satoshis**, Bob **30.000 satoshis**.

![LNP201](assets/fr/26.webp)

2. Bob vuole ricevere 40.000 satoshis da Alice attraverso il loro canale Lightning. Per fare questo :

   - Gli invia una fattura e il suo segreto per la chiave di revoca della sua precedente transazione di impegno.
   - In risposta, Alice fornisce la sua firma per la nuova transazione di impegno di Bob e il suo segreto per la chiave di revoca della transazione precedente.
   - Infine, Bob invia la sua firma per la nuova transazione di impegno di Alice.
   - Questi scambi consentono ad Alice di inviare **40.000 satoshi** a Bob su Lightning attraverso il loro canale, e le nuove transazioni di impegno riflettono ora questa nuova distribuzione dei fondi.
![LNP201](assets/fr/27.webp)

3. Se Alice tenta di pubblicare la vecchia transazione di impegno in cui possedeva ancora **100.000 satoshi**, Bob, avendo ottenuto la chiave di revoca, può recuperare immediatamente i fondi grazie a questa chiave, mentre Alice è bloccata dal timelock.

![LNP201](assets/fr/28.webp)

Anche se in questo caso Bob non ha alcun interesse economico a cercare di imbrogliare, se imbroglia, anche Alice beneficia di una protezione simmetrica che offre le stesse garanzie.

**Che cosa dovreste imparare da questo capitolo?

Le transazioni di impegno** su Lightning Network includono meccanismi di sicurezza che riducono sia il rischio di imbroglio che l'incentivo a farlo. Prima di firmare una nuova transazione di impegno, Alice e Bob si scambiano le rispettive **segrete** per le transazioni di impegno precedenti. Se Alice tenta di pubblicare una vecchia transazione di impegno, Bob può utilizzare la **chiave di revoca** per recuperare l'intero importo prima che Alice possa farlo (poiché è bloccata dal timelock), punendola così per aver tentato di imbrogliare.

Questo sistema di sicurezza garantisce che i partecipanti rispettino le regole della Lightning Network e che non possano trarre profitto dalla pubblicazione di vecchie transazioni di impegno.

A questo punto del corso, saprete come vengono aperti i canali Lightning e come funzionano le transazioni in questi canali. Nel prossimo capitolo vedremo come chiudere un canale e riportare i bitcoin sulla blockchain principale.

## Chiusura del canale

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![fermer un canal](https://youtu.be/FVmQvNpVW8Y)

In questo capitolo esamineremo la **chiusura di un canale** sulla Lightning Network, che si ottiene tramite una transazione Bitcoin, proprio come l'apertura di un canale. Dopo aver visto come funzionano le transazioni all'interno di un canale, è ora il momento di vedere come chiudere un canale e recuperare i fondi sulla blockchain Bitcoin.

### Richiamo del ciclo di vita di un canale

Il **ciclo di vita di un canale** inizia con la sua **apertura**, tramite una transazione Bitcoin, quindi vengono effettuate transazioni Lightning al suo interno e infine, quando le parti desiderano recuperare i propri fondi, il canale viene **chiuso** tramite una seconda transazione Bitcoin. Le transazioni intermedie effettuate su Lightning sono rappresentate da **transazioni di impegno** non pubblicate.

![LNP201](assets/fr/29.webp)

### I tre tipi di chiusura del canale

Esistono tre modi principali per chiudere questo canale, che possono essere definiti **il buono, il cattivo e il brutto** (ispirato da Andreas Antonopoulos in _Mastering the Lightning Network_):

1. **La buona**: la **chiusura cooperativa**, in cui Alice e Bob si accordano per chiudere il canale.

2. **Il bruto**: la **chiusura forzata**, in cui una delle parti decide di chiudere il canale in modo onesto, ma senza l'accordo dell'altra.

3. **L'ingannatore**: la **chiusura con imbroglio**, in cui una delle parti cerca di rubare i fondi pubblicando una vecchia transazione di impegno (una qualsiasi, ma non l'ultima, che riflette la reale ed equa distribuzione dei fondi).

Facciamo un esempio:

- Alice possiede **100.000 satoshis** e Bob **30.000 satoshis**.
- Questa distribuzione si riflette in **2 transazioni di impegno** (una per utente) che non vengono pubblicate, ma potrebbero esserlo in caso di chiusura del canale.
![LNP201](assets/fr/30.webp)

### Il giusto: la chiusura cooperativa

In una **chiusura cooperativa**, Alice e Bob si accordano per chiudere il canale. Ecco come funziona:

1. Alice invia un messaggio a Bob tramite il protocollo di comunicazione Lightning per proporre la chiusura del canale.

2. Bob accetta e le due parti non effettuano altre transazioni nel canale.

![LNP201](assets/fr/31.webp)

3. Alice e Bob negoziano insieme la **commissione di chiusura della transazione**. Queste commissioni sono generalmente calcolate in base al mercato delle commissioni Bitcoin al momento della chiusura. È importante notare che **è sempre la persona che ha aperto il canale** (Alice nel nostro esempio) a pagare la commissione di chiusura.

4. Costruiscono una nuova **transazione di chiusura**. Questa transazione assomiglia a una transazione di impegno, ma senza meccanismi di timelock o di revoca, poiché entrambe le parti stanno cooperando e non c'è il rischio di barare. Questa transazione di chiusura cooperativa è quindi diversa da una transazione di impegno.

Ad esempio, se Alice possiede **100.000 satoshis** e Bob **30.000 satoshis**, la transazione di chiusura invierà **100.000 satoshis** all'indirizzo di Alice e **30.000 satoshis** all'indirizzo di Bob, senza vincoli di tempo. Una volta firmata da entrambe le parti, la transazione viene pubblicata da Alice. Una volta che la transazione è stata confermata sulla blockchain Bitcoin, il canale Lightning è ufficialmente chiuso.

![LNP201](assets/fr/32.webp)

La chiusura cooperativa** è il metodo di chiusura preferito, perché è veloce (senza timelock) e le commissioni di transazione sono regolate in base alle attuali condizioni del mercato Bitcoin. In questo modo si evita di pagare troppo poco, con il rischio di bloccare la transazione nei mempool, o di pagare troppo inutilmente, con conseguenti perdite finanziarie per i partecipanti.

### Il bruto: chiusura forzata

Quando il nodo di Alice invia un messaggio al nodo di Bob per richiedere una chiusura cooperativa, se Bob non risponde (ad esempio a causa di un'interruzione di Internet o di un problema tecnico), Alice può eseguire una **chiusura forzata** pubblicando l'ultima transazione di impegno firmata**.

In questo caso, Alice pubblicherà semplicemente l'ultima transazione di impegno, che riflette lo stato del canale nel momento in cui ha avuto luogo l'ultima transazione Lightning con la corretta allocazione dei fondi.

![LNP201](assets/fr/33.webp)

Questa transazione include un **blocco temporale** per i fondi di Alice, che rende la chiusura più lenta.

![LNP201](assets/fr/34.webp)

Inoltre, le commissioni per le transazioni di impegno possono essere inadeguate al momento della chiusura, poiché sono state fissate al momento della creazione della transazione, a volte diversi mesi prima. In generale, i clienti Lightning sovrastimano le commissioni per evitare problemi futuri, ma questo può portare a commissioni eccessive o al contrario troppo basse.

In breve, la **chiusura forzata** è un'opzione di ultima istanza quando l'interlocutore non risponde più. È più lenta e meno economica della chiusura cooperativa. Pertanto, dovrebbe essere evitata ogni volta che è possibile.

### Il truffatore: imbrogliare

Infine, una chiusura con **truffa** si verifica quando una delle parti tenta di pubblicare una vecchia transazione di impegno, spesso in cui deteneva più fondi del dovuto. Ad esempio, Alice potrebbe pubblicare una vecchia transazione in cui possiede **120.000 satoshi**, mentre in realtà ne possiede solo **100.000**.

![LNP201](assets/fr/35.webp)

Per prevenire l'imbroglio, Bob monitora la blockchain Bitcoin e il suo mempool per assicurarsi che Alice non pubblichi una vecchia transazione. Se Bob rileva un tentativo di imbroglio, può usare la **chiave di revoca** per recuperare i fondi di Alice e punirla prendendo i fondi dell'intero canale. Poiché Alice è bloccata dal timelock sulla sua uscita, Bob ha il tempo di spenderlo senza un proprio timelock per recuperare l'intera somma su un indirizzo che gli appartiene.

![LNP201](assets/fr/36.webp)

Naturalmente, l'imbroglio può potenzialmente avere successo se Bob non si presenta entro il limite di tempo imposto dal timelock sull'uscita di Alice. In questo caso, l'uscita di Alice viene sbloccata, consentendole di utilizzarla per creare una nuova uscita a un indirizzo da lei controllato.

**Che cosa dovreste imparare da questo capitolo?

Esistono tre modi per chiudere un canale:

1. **Chiusura cooperativa**: rapida e meno costosa, in cui entrambe le parti concordano di chiudere il canale e pubblicano una transazione di chiusura adeguata.

2. **Chiusura forzata**: meno auspicabile, in quanto si basa sulla pubblicazione di una transazione di impegno, con commissioni potenzialmente inappropriate e un timelock, che rallenta la chiusura.

3. **Truffa**: se una parte cerca di rubare fondi pubblicando una vecchia transazione, l'altra può usare la chiave di revoca per punire questa truffa.

Nei prossimi capitoli daremo uno sguardo più ampio alla rete Lightning e al suo funzionamento.

# Una rete di liquidità

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Fulmine le Réseau

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![lightning le réseau](https://youtu.be/RAZAa3v41DM)

In questo capitolo analizzeremo come i pagamenti sulla rete Lightning possono raggiungere un destinatario anche se quest'ultimo non è direttamente collegato tramite un canale di pagamento. Lightning è, in effetti, una **rete di canali di pagamento**, il che significa che i fondi possono essere inviati a un nodo remoto attraverso i canali di altri partecipanti. Scopriremo come vengono instradati i pagamenti sulla rete, come si muove la liquidità tra i canali e come vengono calcolate le commissioni sulle transazioni.

### La rete dei canali di pagamento

Nella rete Lightning, una transazione corrisponde a un trasferimento di fondi tra due nodi. Come visto nei capitoli precedenti, per effettuare transazioni Lightning è necessario aprire un canale con una persona. Questo canale permette di effettuare un numero quasi infinito di transazioni fuori dalla catena prima di chiuderlo nuovamente per recuperare il saldo sulla catena. Tuttavia, questo metodo ha lo svantaggio di richiedere un canale diretto con l'altra persona per ricevere o inviare fondi, il che implica una transazione di apertura e una di chiusura per ogni canale. Se ho intenzione di effettuare un gran numero di pagamenti con questa persona, aprire e chiudere un canale diventa redditizio. D'altra parte, se ho bisogno di effettuare solo poche transazioni lampo, l'apertura di un canale diretto non è vantaggiosa, poiché mi costerebbe 2 transazioni on-chain per un numero limitato di transazioni off-chain. Questo potrebbe essere il caso, ad esempio, di chi vuole pagare con Lightning presso un commerciante senza prevedere un ritorno.

Per risolvere questo problema, la rete Lightning consente di instradare un pagamento attraverso diversi canali e nodi intermedi, permettendo di effettuare una transazione senza un canale diretto con l'altra persona.

Ad esempio, supponiamo che :

- Alice** (in arancione) ha un canale con **Suzie** (in grigio) con **100.000 satoshis** dalla sua parte e **30.000 satoshis** dalla parte di Suzie.
- Suzie** ha un canale con **Bob** in cui lei ha **250.000 satoshi** e Bob non ha satoshi.
![LNP201](assets/fr/37.webp)

Se Alice desidera inviare fondi a Bob senza aprire un canale diretto con lui, dovrà passare attraverso Suzie, e ogni canale dovrà regolare la liquidità da ogni lato. **I satoshi inviati rimangono nei rispettivi canali**; in realtà non "attraversano" i canali, ma il trasferimento avviene tramite una regolazione della liquidità interna a ciascun canale.

Supponiamo che Alice voglia inviare **50.000 satoshis** a Bob :

1. **Alice** invia 50.000 satoshi a **Suzie** nel loro canale comune.

2. **Suzie** contrasta questo trasferimento inviando 50.000 satoshis a Bob** nel loro canale.

![LNP201](assets/fr/38.webp)

Il pagamento viene indirizzato a Bob attraverso uno spostamento di liquidità in ogni canale. Al termine dell'operazione, Alice si ritrova con 50.000 sats. Ha trasferito 50.000 sats, dato che originariamente ne aveva 100.000. Bob, dal canto suo, si ritrova con altri 50.000 sats. Per Suzie (il nodo intermedio), questa operazione è neutra: inizialmente aveva 30.000 sats nel suo canale con Alice e 250.000 sats nel suo canale con Bob, per un totale di 280.000 sats. Dopo l'operazione, ha 80.000 saturazioni nel suo canale con Alice e 200.000 saturazioni nel suo canale con Bob, cioè la stessa quantità che aveva all'inizio.

Questo trasferimento è quindi limitato dalla **liquidità disponibile** nella direzione del trasferimento.

### Calcolo dei limiti di rotta e di liquidità

Facciamo un esempio teorico di un'altra rete con :

- 130.000 satoshis** dalla parte di Alice (arancione) nel suo canale con **Suzie** (grigio).
- 90.000 satoshis** sul lato **Suzie** e **200.000 satoshis** sul lato **Carol** (in rosa).
- 150.000 satoshi** per **Carol** e **100.000 satoshi** per **Bob**.
![LNP201](assets/fr/39.webp)

Il massimo che Alice può inviare a Bob in questa configurazione è di **90.000 satoshi**, poiché è limitata dalla minore liquidità disponibile nel canale da **Suzie** a Carol**. Nella direzione opposta (da Bob ad Alice), non è possibile alcun pagamento perché il lato di **Suzie** del canale con **Alice** non contiene satoshi. Non c'è quindi **nessun percorso** che possa essere utilizzato per un trasferimento in questa direzione.

Alice invia **40.000 satoshi** a Bob attraverso i canali :

1. Alice trasferisce 40.000 satoshi nel suo canale con Suzie.

2. Suzie trasferisce 40.000 satoshi a Carol nel loro canale condiviso.

3. Carol trasferisce infine 40.000 satoshi a Bob.

![LNP201](assets/fr/40.webp)

I **satoshi inviati** in ciascun canale **rimangono nel canale**, quindi i satoshi inviati da Carol a Bob non sono gli stessi inviati da Alice a Suzie. Il trasferimento avviene esclusivamente regolando la liquidità all'interno di ciascun canale. La capacità totale dei canali rimane invariata.

![LNP201](assets/fr/41.webp)

Come nell'esempio precedente, dopo la transazione il nodo sorgente (Alice) ha 40.000 satoshis in meno. I nodi intermedi (Suzie e Carol) conservano lo stesso importo totale, rendendo la transazione neutrale per loro. Infine, il nodo di destinazione (Bob) riceve altri 40.000 satoshis.

I nodi intermediari svolgono quindi un ruolo importante nel funzionamento della rete Lightning. Essi rendono i trasferimenti più fluidi offrendo diversi percorsi di pagamento. Per incoraggiare questi nodi a fornire la loro liquidità e a partecipare all'instradamento dei pagamenti, viene loro corrisposta una **commissione di instradamento**.

### Costi di instradamento

I nodi intermediari applicano commissioni per consentire il passaggio dei pagamenti attraverso i loro canali. Queste commissioni sono definite da **ogni nodo per ogni canale**. Le commissioni hanno 2 componenti:

1. "**Canone base**": un importo fisso per canale, spesso **1 sat** di default, ma personalizzabile.

2. "**Variabile della tassa**": una percentuale della quantità trasferita, calcolata in **parti per milione (ppm)**. Per impostazione predefinita, è **1 ppm** (1 sat per milione di satoshi trasferiti), ma può anche essere regolata.

Le commissioni variano anche a seconda della direzione del trasferimento. Ad esempio, per un trasferimento da Alice a Suzie, si applicano le spese di Alice. Viceversa, da Suzie ad Alice, si applicano le tariffe di Suzie.

Ad esempio, per un canale tra Alice e Suzie, si potrebbe avere :

- Alice**: quota base di 1 sat e 1 ppm per i costi variabili.
- Suzie**: 0.5 sat di base e 10 ppm di quota variabile.
![LNP201](assets/fr/42.webp)

Per capire come funzionano le commissioni, studiamo la stessa rete Lightning di prima, ma ora con le seguenti commissioni di instradamento:

- Canale **Alice - Suzie**: tariffa base di 1 satoshi e 1 ppm per Alice.
- Canale **Suzie - Carol**: tariffa base di 0 satoshi e 200 ppm per Suzie 1.
- Canale **Carol - Bob**: quota base di 1 satoshi e 1 ppm per Suzie 2.
![LNP201](assets/fr/43.webp)

Per lo stesso pagamento di **40.000 satoshis** a Bob, Alice dovrà inviare un po' di più, poiché ogni nodo intermediario applicherà le proprie tariffe:

- Carol** prende 1,04 satoshi dal canale con Bob :
$$ f*{{testo{Carol-Bob}} = \testo{tassa} + ´sinistra(´frac{{testo{ppm}} ´mille volte ´testo{ammontare}}{10^6}}destra) $$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0,04 = 1,04 \text{ sats} $$

- Suzie** fa pagare 8 satoshi sul canale con Carol :
$$ f*{{testo{Suzie-Carol}} = \testo{tassa base} + ´sinistra(´frac{testo{ppm} ´mille volte ´testo{importo}}{10^6}}destra) $$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 ´times 40001.04}{10^6} = 0 + 8.0002 ´circa 8 ´sats} $$

La spesa totale per questo pagamento su questo percorso è quindi di **9,04 satoshis**. Pertanto, Alice deve inviare **40.009,04 satoshis** affinché Bob riceva esattamente **40.000 satoshis**.

![LNP201](assets/fr/44.webp)

La liquidità viene quindi aggiornata:

![LNP201](assets/fr/45.webp)

### Instradamento a cipolla

Per instradare un pagamento dal mittente al destinatario, la Lightning Network utilizza un metodo chiamato "onion routing". A differenza dell'instradamento convenzionale dei dati, in cui ogni router decide dove i dati devono andare in base alla loro destinazione, l'instradamento a cipolla funziona in modo diverso:

- Il nodo mittente calcola l'intero percorso**: Alice, ad esempio, determina che il suo pagamento deve passare attraverso Suzie e Carol prima di raggiungere Bob.
- Ogni nodo intermedio conosce solo il suo vicino immediato** : Suzie sa solo di aver ricevuto dei fondi da Alice e di doverli trasferire a Carol. Tuttavia, Suzie non sa se Alice è il nodo sorgente o un nodo intermedio, né sa se Carol è il nodo destinatario o solo un altro nodo intermedio. Questo principio si applica anche a Carol e a tutti gli altri nodi del percorso. L'instradamento a cipolla preserva quindi la riservatezza delle transazioni nascondendo l'identità del mittente e del destinatario finale.
Per calcolare un percorso completo verso il destinatario nel routing a cipolla, il nodo mittente deve mantenere un **grafo di rete** per conoscere la sua topologia e determinare i possibili percorsi.

**Che cosa dovreste imparare da questo capitolo?

1. Su Lightning, i pagamenti possono essere instradati tra nodi collegati indirettamente tramite canali intermedi. Ciascuno di questi nodi intermedi funge da relay di liquidità.

2. I nodi intermediari ricevono una commissione per il loro servizio, composta da costi fissi e variabili.

3. L'instradamento a cipolla consente al nodo mittente di calcolare il percorso completo senza che i nodi intermedi conoscano la sorgente o la destinazione finale.

In questo capitolo abbiamo imparato a conoscere l'instradamento dei pagamenti sulla rete Lightning. Ma la domanda sorge spontanea: cosa impedisce ai nodi intermedi di accettare un pagamento in entrata senza inoltrarlo alla destinazione successiva, con l'obiettivo di intercettare la transazione? È proprio questo il ruolo di HTLC, che esamineremo nel prossimo capitolo.

## HTLC - Contratto a tempo bloccato con hash

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

In questo capitolo scopriremo come Lightning permette ai pagamenti di passare attraverso i nodi intermediari senza bisogno di fidarsi di loro, grazie agli **HTLC** (_Hashed Time-Locked Contracts_). Questi contratti intelligenti garantiscono che ogni nodo intermediario riceverà fondi dal suo canale solo se invia il pagamento al destinatario finale, altrimenti il pagamento non sarà convalidato.

Il problema che si pone quando si instrada un pagamento è quindi la fiducia necessaria nei nodi intermediari e tra i nodi intermediari stessi. Per illustrare questo aspetto, prendiamo l'esempio di una rete Lightning semplificata con 3 nodi e 2 canali:

- Alice ha un canale con Suzie.
- Suzie ha un canale con Bob.
Alice vuole inviare 40.000 satelliti a Bob, ma non ha un canale diretto con lui e non vuole aprirne uno. Cerca un percorso e sceglie di passare attraverso il nodo di Suzie.

![LNP201](assets/fr/46.webp)

Se Alice invia ingenuamente a Suzie 40.000 satoshis nella speranza che Suzie trasferisca questa somma a Bob, Suzie potrebbe tenere i fondi per sé e non trasmettere nulla a Bob.

![LNP201](assets/fr/47.webp)

Per evitare questa situazione, Lightning utilizza HTLC, che condiziona il pagamento al nodo intermediario, ovvero Suzie deve soddisfare determinate condizioni per accedere ai fondi di Alice e passarli a Bob.

### Come funzionano i contratti HTLC (_Hashed Time-Locked Contracts_)

Un contratto HTLC è un contratto speciale basato su due principi:

- Condizione di accesso** : Il destinatario deve rivelare un segreto per sbloccare il pagamento dovuto.
- Scadenza**: Se il pagamento non viene completato entro un determinato periodo, viene annullato e i fondi vengono restituiti al mittente.
Ecco come funziona il processo nel nostro esempio con Alice, Suzie e Bob:

![LNP201](assets/fr/48.webp)

**Creazione del segreto**: Bob genera un segreto casuale noto _s_ (la pre-immagine) e ne calcola l'hash noto _r_ con la funzione hash nota _h_. Il risultato è :

$$
r = h(s)
$$

L'uso di una funzione hash rende impossibile trovare _s_ con _h(s)_ da solo, ma se _s_ viene fornito, è facile verificare che corrisponda a _h(s)_.

![LNP201](assets/fr/49.webp)

**Invio di una richiesta di pagamento**: Bob invia una **fattura** ad Alice per richiedere il pagamento. Questa fattura include l'hash _r_.

![LNP201](assets/fr/50.webp)

**Pagamento condizionato**: Alice invia un HTLC di 40.000 satoshis a Suzie. La condizione perché Suzie riceva questi fondi è che fornisca ad Alice un _s'_ segreto che verifichi la seguente equazione:

$$
h(s') = r
$$

![LNP201](assets/fr/51.webp)

**Trasmissione di HTLC al destinatario finale**: Suzie, per ottenere i 40.000 satoshis da Alice, deve trasferire un analogo HTLC di 40.000 satoshis a Bob, che ha la stessa condizione, cioè deve fornire a Suzie un segreto _s'_ che verifichi l'equazione :

$$
h(s') = r
$$

![LNP201](assets/fr/52.webp)

**Validazione tramite _s_ segreto**: Bob fornisce a Suzie _s_ per ricevere i 40.000 satoshis promessi nell'HTLC. Con questo segreto, Suzie può sbloccare l'HTLC di Alice e ottenere i 40.000 satoshis da Alice. Il pagamento viene quindi correttamente indirizzato a Bob.

![LNP201](assets/fr/53.webp)

Questo processo rende impossibile per Suzie trattenere i fondi di Alice senza completare il trasferimento a Bob, poiché deve inviare il pagamento a Bob per ottenere il segreto _s_ e quindi sbloccare l'HTLC di Alice. L'operazione rimane la stessa anche se il percorso comprende diversi nodi intermedi: basta ripetere i passaggi di Suzie per ogni nodo intermedio. Ogni nodo è protetto dalle condizioni HTLC, poiché lo sblocco dell'ultimo HTLC da parte del destinatario innesca automaticamente lo sblocco di tutti gli altri HTLC della cascata.

### Scadenza e gestione dell'HTLC in caso di problemi

Se durante il processo di pagamento uno dei nodi intermediari, o il nodo di destinazione, non risponde, ad esempio in caso di interruzione di Internet o di energia elettrica, il pagamento non può andare a buon fine, in quanto non viene trasmesso il segreto che consente di sbloccare l'HTLC. Se torniamo al nostro esempio con Alice, Suzie e Bob, questo problema si presenta, ad esempio, se Bob non trasmette il segreto _s_ a Suzie. In questo caso, tutti gli HTLC a monte del percorso sono bloccati, così come i fondi che essi proteggono.

![LNP201](assets/fr/54.webp)

Per evitare questo inconveniente, le HTLC su Lightning sono dotate di una scadenza che consente di eliminare la HTLC se non viene completata entro un certo tempo. La scadenza segue un ordine specifico, iniziando dalla HTLC più vicina al destinatario e procedendo progressivamente a ritroso fino al mittente della transazione. Nel nostro esempio, se Bob non fornisce mai il segreto _s_ a Suzie, l'HTLC da Suzie a Bob scadrà per primo.

![LNP201](assets/fr/55.webp)

Poi l'HTLC di Alice a Suzie.

![LNP201](assets/fr/56.webp)

Se l'ordine di scadenza fosse invertito, Alice potrebbe recuperare il suo pagamento prima che Suzie possa proteggersi da un potenziale imbroglio. Infatti, se Bob tornasse a reclamare il suo HTLC quando Alice ha già cancellato il suo, Suzie si troverebbe danneggiata. Questo ordine di scadenza delle HTLC a cascata garantisce che nessun nodo intermedio subisca perdite ingiuste.

### Rappresentazione HTLC nelle transazioni di impegno

Le transazioni di impegno rappresentano le HTLC in modo che le condizioni che impongono a Lightning siano trasferibili a Bitcoin in caso di chiusura forzata del canale durante la vita di una HTLC. Come promemoria, le transazioni di impegno rappresentano lo stato attuale del canale tra i due utenti e consentono la chiusura forzata unilaterale in caso di problemi. Per ogni nuovo stato del canale, vengono create 2 transazioni di impegno: una per ogni parte. Torniamo al nostro esempio con Alice, Suzie e Bob, ma osserviamo più da vicino cosa succede nel canale tra Alice e Suzie quando viene creato l'HTLC.

![LNP201](assets/fr/57.webp)

Prima dell'inizio del pagamento di 40.000 sats tra Alice e Bob, Alice ha 100.000 sats nel suo canale con Suzie, mentre Suzie ne ha 30.000. Le loro transazioni di impegno sono quindi le seguenti:

![LNP201](assets/fr/58.webp)

Alice ha appena ricevuto la fattura di Bob, che contiene _r_, l'hash del segreto. Può quindi costruire un HTLC di 40.000 satoshis con Suzie. Questo HTLC è rappresentato nelle ultime transazioni di impegno come un output chiamato "**_HTLC Out_**" dal lato di Alice, poiché i fondi sono in uscita, e "**_HTLC In_**" dal lato di Suzie, poiché i fondi sono in entrata.

![LNP201](assets/fr/59.webp)

Queste uscite associate all'HTLC condividono esattamente le stesse condizioni, ovvero :

- Se Suzie è in grado di fornire le _s_ segrete, può sbloccare immediatamente questa uscita e trasferirla a un indirizzo da lei controllato.
- Se Suzie non ha il segreto _s_, non può sbloccare questa uscita, e Alice può sbloccarla dopo un blocco temporale per inviarla a un indirizzo da lei controllato. Il blocco temporale dà quindi a Suzie il tempo di reagire se ottiene _s_.
Queste condizioni si applicano solo se il canale viene chiuso (una transazione di impegno viene pubblicata sulla catena) mentre l'HTLC è ancora attivo su Lightning, cioè il pagamento tra Alice e Bob non è ancora stato finalizzato e gli HTLC non sono ancora scaduti. Grazie a queste condizioni, Suzie può recuperare i 40.000 satoshis di HTLC che le sono dovuti fornendo _s_. In caso contrario, Alice recupera i fondi dopo che il timelock è scaduto, perché se Suzie non conosce _s_, significa che non ha trasmesso i 40.000 satoshis a Bob e quindi i fondi di Alice non gli sono dovuti.

D'altra parte, se il canale viene chiuso mentre diversi HTLC sono in attesa, ci saranno tante uscite quanti sono gli HTLC in corso.

Se il canale non è chiuso, dopo che il pagamento lampo è scaduto o è andato a buon fine, vengono create nuove transazioni di impegno per riflettere il nuovo stato stabile del canale, cioè senza HTLC in sospeso. Le uscite relative agli HTLC possono quindi essere rimosse dalle transazioni di impegno.

![LNP201](assets/fr/60.webp)

Infine, in caso di chiusura di un canale cooperativo mentre è attivo un HTLC, Alice e Suzie smettono di accettare nuovi pagamenti e attendono la risoluzione o la scadenza dell'HTLC corrente. Questo permette loro di pubblicare una transazione di chiusura più leggera, senza le uscite legate agli HTLC, riducendo così i costi ed evitando di attendere un eventuale timelock.

**Che cosa dovreste imparare da questo capitolo?

HTLC consente di instradare i pagamenti Lightning attraverso più nodi senza doverli fidare. Ecco i punti chiave da ricordare:

1. HTLC garantisce la sicurezza del pagamento attraverso un segreto (pre-immagine) e una data di scadenza.

2. La risoluzione o la scadenza dell'HTLC segue un ordine specifico: dalla destinazione alla sorgente, per proteggere ogni nodo.

3. Finché un HTLC non viene risolto o scaduto, viene mantenuto come output nelle transazioni di impegno più recenti.

Nel prossimo capitolo scopriremo come il nodo mittente di una transazione Lightning trova e seleziona i percorsi per far sì che il pagamento raggiunga il nodo destinatario.

## Trovare la strada

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![trouver sa voie](https://youtu.be/wnUGJjOxd9Q)

Nei capitoli precedenti abbiamo visto come utilizzare i canali di altri nodi per instradare i pagamenti e raggiungere un nodo senza essere direttamente collegati ad esso tramite un canale. Abbiamo anche discusso come garantire la sicurezza del trasferimento senza affidarsi a nodi intermediari. In questo capitolo vedremo come trovare il miglior percorso possibile per raggiungere un nodo di destinazione.

### Instradamento in Lightning

Come abbiamo visto, su Lightning è il nodo mittente del pagamento a dover calcolare il percorso completo verso il destinatario, poiché utilizziamo un sistema di routing a cipolla. I nodi intermedi non conoscono né il punto di origine né la destinazione finale. Sanno solo da dove proviene il pagamento e a quale nodo devono trasferirlo successivamente. Ciò significa che il nodo mittente deve mantenere una topologia di rete locale dinamica, con i nodi Lightning esistenti e i canali tra di essi, tenendo conto delle aperture, delle chiusure e degli aggiornamenti di stato.

![LNP201](assets/fr/61.webp)

Anche con questa topologia di rete Lightning, c'è un'informazione essenziale sull'instradamento che rimane inaccessibile al nodo trasmittente: l'esatta distribuzione della liquidità nei canali in qualsiasi momento. Infatti, ogni canale mostra solo la sua **capacità totale**, ma la distribuzione interna dei fondi è nota solo ai due nodi partecipanti. Questo pone delle sfide per un instradamento efficiente, poiché il successo del pagamento dipende in particolare dal fatto che il suo importo sia inferiore alla liquidità più bassa sul percorso scelto. Tuttavia, non tutta la liquidità è visibile al nodo mittente.

![LNP201](assets/fr/62.webp)

### Aggiornamento della mappa di rete

Per mantenere aggiornata la mappa della rete, i nodi si scambiano regolarmente messaggi utilizzando un algoritmo noto come "**_gossip_**". Si tratta di un algoritmo distribuito utilizzato per diffondere informazioni in modo epidemico a tutti i nodi della rete, consentendo di scambiare e sincronizzare lo stato globale dei canali in pochi cicli di comunicazione. Ogni nodo propaga le informazioni a uno o più vicini selezionati in modo casuale o non casuale, che a loro volta propagano le informazioni ad altri vicini, e così via, fino a raggiungere uno stato sincronizzato a livello globale.

I due messaggi principali scambiati tra i nodi Lightning sono i seguenti:

- "**Channel Announcements**": messaggi che annunciano l'apertura di un nuovo canale.
- "**Aggiornamenti canale**": messaggi di aggiornamento sullo stato di un canale, in particolare sull'evoluzione delle spese (ma non sulla distribuzione di liquidità).
I nodi Lightning monitorano anche la blockchain Bitcoin per le transazioni di chiusura del canale. Il canale chiuso viene quindi rimosso dalla carta, poiché non può più essere utilizzato per instradare i pagamenti.

### Instradamento di un pagamento

Facciamo un esempio di una piccola rete Lightning con 7 nodi: Alice, Bob, 1, 2, 3, 4 e 5. Immaginiamo che Alice voglia inviare un pagamento a Bob, ma che debba passare attraverso nodi intermedi.

![LNP201](assets/fr/63.webp)

Ecco la distribuzione effettiva dei fondi in questi canali:

- Canale tra Alice e 1**: 250.000 satelliti sul lato Alice, 80.000 sul lato 1 (capacità totale di 330.000 satelliti).
- Canale tra 1 e 2**: 300.000 satelliti sul lato 1, 200.000 sul lato 2 (capacità totale di 500.000 satelliti).
- Canale tra 2 e 3**: 50.000 satelliti sul lato 2, 60.000 sul lato 3 (capacità totale di 110.000 satelliti).
- Canale tra 2 e 5**: 90.000 satelliti sul lato 2, 160.000 sul lato 5 (capacità totale di 250.000 satelliti).
- Canale tra 2 e 4**: 180.000 satelliti sul lato 2, 110.000 sul lato 4 (capacità totale 290.000 satelliti).
- Canale tra 4 e 5**: 200.000 satelliti sul lato 4, 10.000 sul lato 5 (capacità totale di 210.000 satelliti).
- Canale tra 3 e Bob**: 50.000 satelliti sul lato 3, 250.000 sul lato Bob (capacità totale di 300.000 satelliti).
- Canale tra 5 e Bob**: 260.000 satelliti sul lato 5, 100.000 sul lato Bob (capacità totale di 360.000 satelliti).
![LNP201](assets/fr/64.webp)

Per effettuare un pagamento di 100.000 satelliti da Alice a Bob, le opzioni di instradamento sono limitate dalla liquidità disponibile in ogni canale. Il percorso ottimale per Alice, basato sulle distribuzioni di liquidità note, potrebbe essere la sequenza `Alice → 1 → 2 → 4 → 5 → Bob` :

![LNP201](assets/fr/65.webp)

Ma poiché Alice non conosce l'esatta distribuzione dei fondi in ogni canale, deve stimare il percorso ottimale in modo probabilistico, tenendo conto dei seguenti criteri:

- Probabilità di successo**: un canale con una capacità totale più elevata ha maggiori probabilità di contenere liquidità sufficiente. Ad esempio, il canale tra il nodo 2 e il nodo 3 ha una capacità totale di 110.000 satelliti, quindi è improbabile che ci siano 100.000 satelliti o più sul lato del nodo 2, anche se è possibile.
- Costi di transazione**: quando sceglie il percorso migliore, il nodo mittente tiene conto anche dei costi applicati da ciascun nodo intermediario e cerca di minimizzare il costo totale dell'instradamento.
- Scadenza HTLC**: per evitare il blocco dei pagamenti, anche il tempo di scadenza HTLC è un parametro da tenere in considerazione.
- Numero di nodi intermedi**: infine, in senso più globale, il nodo mittente cercherà di trovare un percorso con il minor numero possibile di nodi, per ridurre il rischio di fallimento e limitare i costi di transazione di Lightning.
Analizzando questi criteri, il nodo trasmittente può verificare i percorsi più probabili e cercare di ottimizzarli. Nel nostro esempio, Alice potrebbe classificare i percorsi migliori come segue:

1. `Alice → 1 → 2 → 5 → Bob`, perché è il percorso più breve con la massima capacità.

2. `Alice → 1 → 2 → 4 → 5 → Bob`, poiché questo percorso offre buone possibilità, anche se è più lungo del primo.

3. `Alice → 1 → 2 → 3 → Bob`, perché questo percorso include il canale `2 → 3`, che ha una capacità molto limitata, ma è ancora potenzialmente utilizzabile.

### Esecuzione del pagamento

Alice decide di testare il suo primo percorso (`Alice → 1 → 2 → 5 → Bob`). Invia un HTLC di 100.000 satelliti al nodo 1, che verifica di avere sufficiente liquidità con il nodo 2 e continua la trasmissione. Il nodo 2 riceve l'HTLC dal nodo 1, ma si rende conto di non avere abbastanza liquidità nel suo canale con il nodo 5 per inviare un pagamento di 100.000 sats. Invia quindi un messaggio di errore al nodo 1, che lo inoltra ad Alice. Questo percorso è fallito.

![LNP201](assets/fr/66.webp)

Alice cerca quindi di instradare il pagamento utilizzando il suo secondo percorso (`Alice → 1 → 2 → 4 → 5 → Bob`). Invia un HTLC di 100.000 satelliti al nodo 1, che lo inoltra al nodo 2, poi al nodo 4, al nodo 5 e infine a Bob. Questa volta c'è abbastanza denaro e il percorso è attivo. Ogni nodo rilascia il proprio HTLC in cascata, utilizzando la pre-immagine fornita da Bob (il _s_ segreto), finalizzando così con successo il pagamento da Alice a Bob.

![LNP201](assets/fr/67.webp)

La ricerca del percorso si svolge come segue: il nodo mittente identifica innanzitutto i migliori percorsi possibili, quindi tenta pagamenti successivi fino a trovare un percorso funzionale.

Si noti che Bob può fornire ad Alice informazioni nella **fattura** per facilitare l'instradamento. Ad esempio, può indicare i canali vicini con sufficiente liquidità o rivelare l'esistenza di canali privati. Queste indicazioni consentono ad Alice di evitare i percorsi con scarse possibilità di successo e di provare prima i percorsi raccomandati da Bob.

**Che cosa dovreste imparare da questo capitolo?

1. I nodi mantengono una mappa della topologia della rete attraverso annunci e monitorando le chiusure dei canali sulla blockchain Bitcoin.

2. La ricerca di un percorso ottimale per un pagamento rimane probabilistica e dipende da molti criteri.

3. Bob può fornire suggerimenti nella **fattura** per guidare l'itinerario di Alice ed evitarle di provare percorsi improbabili.

Nel prossimo capitolo vedremo più da vicino come funzionano le fatture e alcuni degli altri strumenti utilizzati su Lightning Network.

# Strumenti della rete Lightning

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Fattura, LNURL e Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

![invoice, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

In questo capitolo vedremo più da vicino come funzionano le **fatture** di Lightning, ovvero le richieste di pagamento inviate dal nodo destinatario al nodo mittente. L'obiettivo è capire come pagare e ricevere pagamenti con Lightning. Verranno inoltre analizzate due alternative alle fatture tradizionali: LNURL e Keysend.

![LNP201](assets/fr/68.webp)

### La struttura della fattura Lightning

Come spiegato nel capitolo sull'HTLC, ogni pagamento inizia con la generazione di una **fattura** da parte del destinatario. Questa fattura viene poi trasmessa al pagatore (tramite codice QR o copia-incolla) per avviare il pagamento. Una fattura è composta da due parti principali:

1. **Parte leggibile dall'uomo: questa sezione contiene metadati ben visibili per migliorare l'esperienza dell'utente.

2. **Carico di pagamento**: questa sezione contiene informazioni destinate alle macchine per l'elaborazione dei pagamenti.

La struttura tipica della fattura inizia con un identificatore `ln` per "Lightning", seguito da `bc` per Bitcoin, quindi dall'importo della fattura. Un separatore `1` distingue la parte leggibile dall'uomo dalla parte dei dati (payload).

Prendiamo ad esempio la seguente fattura:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Possiamo già dividerlo in due parti. Innanzitutto, c'è la parte che può essere letta dagli esseri umani:

```invoice
lnbc100u
```

Poi la sezione del carico utile:

```invoice
p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Le due parti sono separate da un `1`. Questo separatore è stato scelto al posto di un carattere speciale per facilitare il copia e incolla dell'intera fattura con un doppio clic.

Nella prima parte, possiamo vedere che :

- `ln` indica che si tratta di una transazione Lightning.
- bc` indica che la rete Lighnting è sulla blockchain di Bitcoin (e non su testnet o Litecoin).
- `100u` indica l'importo della fattura, espresso in **microsatoshi** (`u` significa "micro"), che qui equivale a 10.000 saturazioni.
L'importo del pagamento è espresso in unità secondarie di bitcoin. Ecco le unità utilizzate:

- Millibitcoin (indicato con `m`):** Rappresenta un millesimo di un bitcoin.
$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$

- Microbitcoin (indicato con `u`):** Talvolta chiamato anche "bit", rappresenta un milionesimo di un bitcoin.
$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$

- Nanobitcoin (indicato con `n`):** Rappresenta un miliardesimo di un bitcoin.
$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$

- Picobitcoin (indicato con `p`):** Rappresenta un trilionesimo di bitcoin.
$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$

### Carico utile della fattura

Il payload di una fattura include diverse informazioni per l'elaborazione del pagamento:

- Timestamp** : L'ora di creazione della fattura, espressa in Unix Timestamp (il numero di secondi trascorsi dal 1° gennaio 1970).
- L'hash segreto**: Come abbiamo visto nella sezione su HTLC, il nodo ricevente deve fornire al nodo mittente l'hash della pre-immagine. Questo verrà utilizzato in HTLC per proteggere la transazione. Lo abbiamo chiamato "_r_".
- Segreto di pagamento**: Un altro segreto viene generato dal destinatario, ma questa volta trasmesso al nodo di invio. Viene utilizzato nel routing a cipolla per impedire ai nodi intermedi di indovinare se il nodo successivo è il destinatario finale o meno. In questo modo si mantiene una forma di riservatezza per il destinatario nei confronti dell'ultimo nodo intermedio del percorso.
- Chiave pubblica del destinatario**: Indica al pagatore l'identificativo della persona da pagare.
- Tempo di scadenza**: Tempo massimo per il pagamento della fattura (default: 1 ora).
- Informazioni sul percorso**: Informazioni aggiuntive fornite dal destinatario per aiutare il mittente a ottimizzare il percorso di pagamento.
- Firma**: Garantisce l'integrità della fattura autenticando tutte le informazioni.
Le fatture sono poi codificate in **bech32**, lo stesso formato degli indirizzi Bitcoin SegWit (formato che inizia con `bc1`).

### Ritiro LNURL

In una transazione convenzionale, come un acquisto in negozio, la fattura viene generata per l'importo totale da pagare. Una volta presentata la fattura (come codice QR o stringa di caratteri), il cliente può scansionarla e concludere la transazione. Il pagamento segue quindi il processo classico studiato nella sezione precedente. Tuttavia, questo processo può talvolta risultare molto fastidioso per l'esperienza dell'utente, in quanto richiede che il destinatario invii informazioni al mittente tramite la fattura.

Per alcune situazioni, come il prelievo di bitcoin da un servizio online, la procedura tradizionale è troppo restrittiva. La soluzione di prelievo **LNURL** semplifica questo processo mostrando un codice QR che il portafoglio del destinatario scansiona per creare automaticamente la fattura. Il servizio paga quindi la fattura e l'utente vede semplicemente un prelievo istantaneo.

![LNP201](assets/fr/69.webp)

LNURL è un protocollo di comunicazione che specifica una serie di funzionalità progettate per semplificare le interazioni tra i nodi e i client di Lightning e le applicazioni di terze parti. Il ritiro di LNURL, come abbiamo appena visto, è solo un esempio di questa funzionalità.

Questo protocollo si basa su HTTP e consente di creare link per varie operazioni, come una richiesta di pagamento, una richiesta di prelievo o altre funzionalità che migliorano l'esperienza dell'utente. Ogni LNURL è un URL codificato in bech32 con il prefisso lnurl che, una volta scansionato, attiva una serie di azioni automatiche sul portafoglio Lightning.

Ad esempio, LNURL-withdraw (LUD-03) consente di prelevare fondi da un servizio scansionando un codice QR, senza dover generare manualmente una fattura. Oppure LNURL-auth (LUD-04) consente di connettersi ai servizi online utilizzando una chiave privata del proprio portafoglio Lightning invece di una password.

### Invio di un pagamento Lightning senza fattura: Keysend

Un altro caso interessante è il trasferimento di fondi senza ricevere prima una fattura, noto come "**Keysend**". Questo protocollo consente di inviare fondi aggiungendo ai dati di pagamento crittografati un pre-tag accessibile solo dal destinatario. Questo pre-tag permette al destinatario di sbloccare l'HTLC e quindi di recuperare i fondi senza aver prima generato una fattura.

In parole povere, in questo protocollo è il mittente a generare il segreto utilizzato in HTLC, e non il destinatario. In pratica, ciò consente al mittente di inviare un pagamento senza dover interagire preventivamente con il destinatario.

![LNP201](assets/fr/70.webp)

**Che cosa dovreste imparare da questo capitolo?

1. Una **fattura** Lightning è una richiesta di pagamento composta da una parte leggibile dall'uomo e da una parte di dati leggibile dalla macchina.

2. La fattura è codificata in **bech32**, con un separatore `1` per facilitare la copia e una sezione dati contenente tutte le informazioni necessarie per elaborare il pagamento.

3. Su Lightning esistono altri processi di pagamento, tra cui **LNURL-Withdraw** per prelievi semplici e **Keysend** per trasferimenti diretti senza fattura.

Nel prossimo capitolo vedremo come l'operatore di un nodo può gestire la liquidità nei suoi canali, in modo da non essere mai bloccato e poter sempre inviare e ricevere pagamenti sulla Rete Lightning.

## Gestione della liquidità

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![gerer sa liquidité](https://youtu.be/YuPrbhEJXbg)

In questo capitolo esamineremo le strategie per gestire efficacemente la liquidità sulla rete Lightning. La gestione della liquidità varia a seconda del tipo di utente e del contesto. Verranno illustrati i principi fondamentali e le tecniche esistenti per aiutarvi a capire come ottimizzare la gestione della liquidità.

### Requisiti di liquidità

Su Lightning esistono tre profili principali di utenti, ciascuno con specifiche esigenze di cassa:

1. **Il pagatore**: È la persona che effettua i pagamenti. Ha bisogno di liquidità in uscita per poter trasferire fondi ad altri utenti. Ad esempio, potrebbe essere un consumatore.

2. **Il venditore (o beneficiario) **: È la persona che riceve i pagamenti. Ha bisogno di liquidità in entrata per poter accettare i pagamenti al suo nodo. Ad esempio, potrebbe essere un'azienda o un negozio online.

3. **Il router**: Un nodo intermediario, spesso specializzato nell'instradamento dei pagamenti, che deve ottimizzare la propria liquidità in ogni canale per instradare un numero massimo di pagamenti e guadagnare commissioni.

Naturalmente, questi profili non sono fissi: un utente può alternarsi tra pagatore e beneficiario a seconda della transazione. Ad esempio, Bob potrebbe ricevere il suo stipendio su Lightning dal suo datore di lavoro, il che lo pone nella posizione di "venditore" che richiede liquidità in entrata. In seguito, se desidera utilizzare il suo stipendio per comprare cibo, diventa "pagatore", richiedendo liquidità in uscita.

Per capire meglio, facciamo l'esempio di una semplice rete con tre nodi: l'acquirente (Alice), il router (Suzie) e il venditore (Bob).

![LNP201](assets/fr/71.webp)

Immaginiamo che l'acquirente voglia inviare 30.000 sats al venditore e che il pagamento passi attraverso il nodo router. Ogni parte deve quindi disporre di una quantità minima di liquidità nella direzione del pagamento:

- Il pagatore deve avere almeno 30.000 satoshis sul suo lato del canale con il router.
- Il venditore deve avere un canale in cui 30.000 satoshi si trovano sul lato opposto per poterli ricevere.
- Per poter instradare il pagamento, il router deve disporre di 30.000 satoshis dal lato del pagatore nel proprio canale e di 30.000 satoshis dal lato del venditore.
![LNP201](assets/fr/72.webp)

### Strategie di gestione della liquidità

I pagatori devono mantenere una liquidità sufficiente sul proprio lato dei canali per garantire la liquidità in uscita. Questo è relativamente semplice, in quanto è sufficiente aprire nuovi canali Lightning per fornire questa liquidità. Infatti, i fondi iniziali bloccati nel multisig on-chain sono interamente sul lato del pagatore del canale Lightning all'inizio. La capacità di pagamento è quindi garantita finché i canali sono aperti con fondi sufficienti. Quando la liquidità in uscita si esaurisce, è sufficiente aprire nuovi canali.

Per il venditore, invece, il compito è più complesso. Per poter ricevere i pagamenti, deve disporre di liquidità sul lato opposto dei suoi canali. Aprire un canale non è sufficiente: deve anche effettuare un pagamento in quel canale per spostare la liquidità dall'altra parte prima di poter ricevere i pagamenti. Per alcuni profili di utenti Lightning, come i commercianti, esiste una chiara sproporzione tra ciò che il loro nodo invia e ciò che riceve, poiché l'obiettivo di un'attività commerciale è soprattutto quello di incassare più di quanto spende, al fine di ottenere un profitto. Fortunatamente, per gli utenti con esigenze specifiche in termini di liquidità in entrata, esistono diverse soluzioni:

- Canali di attrazione**: L'esercente gode di un vantaggio dovuto al volume di pagamenti in entrata previsti sul suo nodo. Tenendo conto di ciò, può cercare di attirare i nodi router che sono alla ricerca di entrate da commissioni di transazione e che potrebbero aprirgli dei canali, nella speranza di instradare i suoi pagamenti e raccogliere le commissioni associate.
- Spostamento della liquidità** : Il venditore può anche aprire un canale e trasferire parte dei fondi al lato opposto, effettuando pagamenti fittizi a un altro nodo, che restituirà il denaro in un altro modo. Vedremo come fare nella prossima sezione.
- Apertura del triangolo**: Esistono piattaforme di connessione per i nodi che desiderano aprire canali in modo collaborativo, consentendo a tutti di beneficiare immediatamente della liquidità in entrata e in uscita. Ad esempio, [LightningNetwork+](https://lightningnetwork.plus/) offre questo servizio. Se Alice, Bob e Suzie desiderano aprire un canale di 100.000 satelliti, possono concordare su questa piattaforma che Alice apra un canale verso Bob, Bob verso Suzie e Suzie verso Alice. In questo modo, ciascuno dispone di 100.000 sats di liquidità in uscita e di 100.000 sats di liquidità in entrata, pur avendo vincolato solo 100.000 sats.
![LNP201](assets/fr/73.webp)

- Acquisto di canali**: Esistono anche servizi di noleggio di canali Lightning per ottenere liquidità in entrata, come [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) o [Pool de Lightning Labs](https://lightning.engineering/pool/). Ad esempio, Alice può acquistare un canale di un milione di satoshis per il suo nodo al fine di ricevere pagamenti.
![LNP201](assets/fr/74.webp)

Infine, per i router, il cui obiettivo è massimizzare il numero di pagamenti elaborati e le commissioni riscosse, devono :

- Aprire canali ben forniti con nodi strategici.
- Adattare regolarmente l'assegnazione dei fondi ai canali in base alle esigenze della rete.
### Il servizio Loop Out

Il servizio [Loop Out](https://lightning.engineering/loop/), offerto da Lightning Labs, consente di spostare la liquidità sul lato opposto del canale mentre i fondi vengono recuperati dalla blockchain Bitcoin. Ad esempio, Alice invia 1 milione di satoshi tramite Lightning a un nodo loop, che restituisce i fondi in Bitcoin della catena. Questo bilancia il suo canale con 1 milione di satoshis su ciascun lato, ottimizzando la sua capacità di ricevere pagamenti.

![LNP201](assets/fr/75.webp)

Questo servizio consente di avere liquidità in entrata e di recuperare i bitcoin sulla catena, limitando così la quantità di denaro legata all'accettazione dei pagamenti con Lightning.

**Che cosa dovreste imparare da questo capitolo?

- Per inviare pagamenti su Lightning, è necessario disporre di una liquidità sufficiente nei propri canali. Per aumentare questa capacità di invio, è sufficiente aprire nuovi canali.
- Per ricevere pagamenti, è necessario disporre di liquidità sul lato opposto nei propri canali. Aumentare questa capacità di ricezione è più complesso, in quanto richiede che altri aprano canali verso di voi o che effettuino pagamenti (fittizi o di altro tipo) per spostare la liquidità dall'altra parte.
- Mantenere la liquidità dove si vuole può essere ancora più difficile, a seconda dell'utilizzo dei canali. Per questo motivo esistono strumenti e servizi che aiutano a bilanciare i canali come desiderato.
Nel prossimo capitolo rivedrò i concetti più importanti di questa formazione.

# Vai avanti

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Conclusione della formazione

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![conclusion](https://youtu.be/MaWpD0rbkVo)

In questo capitolo finale, che segna la fine del corso di formazione LNP201, vorrei ripercorrere i concetti importanti che abbiamo visto insieme.

L'obiettivo di questo corso è stato quello di fornire una comprensione tecnica e completa della Lightning Network. Abbiamo scoperto come la Lightning Network si basi sulla blockchain di Bitcoin per effettuare transazioni fuori catena, pur mantenendo le caratteristiche fondamentali di Bitcoin, in particolare l'assenza della necessità di fidarsi di altri nodi.

### Canali di pagamento

Nei primi capitoli abbiamo visto come due parti, aprendo un canale di pagamento, possano effettuare transazioni al di fuori della blockchain Bitcoin. Ecco i passaggi trattati:

1. **Apertura del canale**: Il canale viene creato tramite una transazione Bitcoin che blocca i fondi su un indirizzo 2/2 a firma multipla. Questo deposito è la rappresentazione del canale Lightning sulla blockchain.

![LNP201](assets/fr/76.webp)

2. **Transazioni nel canale**: In questo canale è possibile effettuare numerose transazioni senza doverle pubblicare sulla blockchain. Ogni transazione Lightning crea un nuovo stato del canale che si riflette in una transazione di impegno.

![LNP201](assets/fr/77.webp)

3. **Sicurezza e chiusura**: I partecipanti si impegnano a rispettare il nuovo stato del canale scambiandosi le chiavi di revoca per proteggere i fondi e prevenire gli imbrogli. Entrambe le parti possono chiudere il canale in modo cooperativo effettuando una nuova transazione sulla blockchain Bitcoin, o come ultima risorsa con una chiusura forzata. Sebbene quest'ultima opzione sia meno efficace, in quanto richiede più tempo ed è talvolta poco conveniente in termini di costi, consente comunque di recuperare i fondi. In caso di truffa, la vittima può punire l'imbroglione recuperando tutti i fondi del canale dalla blockchain.

![LNP201](assets/fr/78.webp)

### La rete di canali

Dopo aver studiato i canali isolati, abbiamo esteso la nostra analisi alla rete di canali:

- Instradamento** : Quando due parti non sono direttamente collegate da un canale, la rete consente loro di passare attraverso nodi intermedi. I pagamenti vengono quindi instradati da un nodo all'altro.
![LNP201](assets/fr/79.webp)

- HTLC** : I pagamenti che passano attraverso i nodi intermediari sono protetti da "_Hash Time-Locked Contracts_" (HTLC), che consentono di bloccare i fondi fino al completamento del pagamento da un capo all'altro.
![LNP201](assets/fr/80.webp)

- Instradamento a cipolla**: Per garantire la riservatezza del pagamento, l'onion routing nasconde la destinazione finale ai nodi intermedi. Il nodo mittente deve quindi calcolare l'intero percorso, ma in assenza di informazioni complete sulla liquidità del canale, procede per tentativi successivi di instradare il pagamento.
![LNP201](assets/fr/81.webp)

### Gestione della liquidità

Abbiamo visto che la gestione della liquidità è una sfida per Lightning per garantire il flusso regolare dei pagamenti. Inviare pagamenti è relativamente semplice: basta aprire un canale. Tuttavia, la ricezione dei pagamenti richiede liquidità sul lato opposto dei canali. Ecco alcune delle strategie che abbiamo discusso:

- Attirare canali**: Incoraggiando altri nodi ad aprire canali verso di voi, un utente ottiene liquidità in entrata.
- Spostamento della liquidità**: Inviando i pagamenti ad altri canali, la liquidità si sposta sul lato opposto.
![LNP201](assets/fr/82.webp)

- Utilizzo di servizi come Loop e Pool**: Questi servizi consentono di riequilibrare o acquistare canali con liquidità sul lato opposto.
![LNP201](assets/fr/83.webp)

- Aperture collaborative**: Esistono anche piattaforme per mettere in contatto le persone tra loro per realizzare aperture triangolari e accedere alla liquidità in entrata.
![LNP201](assets/fr/84.webp)

### Grazie

Vorrei ringraziare tutti voi per l'interesse, il sostegno e le domande che mi avete rivolto nel corso di questa serie. In origine, la mia idea era di creare contenuti in lingua francese sugli aspetti tecnici di Lightning, data la mancanza di risorse disponibili. È stata una sfida personale che ho voluto raccogliere combinando rigore tecnico e accessibilità. Se questo corso di formazione gratuito vi è piaciuto, valutatelo nella sezione "Vota questo corso" e condividetelo con i vostri amici e sui vostri social network.

Grazie, a presto!

### Bonus: Intervista a Fanis

![interview de Fanis](https://youtu.be/VeJ4oJIXo9k)

### Bonus: Intervista a Fanis

![interview de Fanis](https://youtu.be/VeJ4oJIXo9k)

# Conclusione

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Valuta questo corso

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>

## Esame finale

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>vero</isCourseExam>

## Conclusione

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

Congratulazioni! 🎉

Avete completato LNP 201 - Introduzione alla rete Lightning! Potete essere orgogliosi di voi stessi, perché questa non è una materia facile. Pochi si spingono così in profondità nella tana del coniglio di Bitcoin.

Grazie a **Fanis Michalakis** per averci offerto questo grande corso gratuito sul funzionamento tecnico della Lightning Network. Sentitevi liberi di seguirlo su [Twitter](https://x.com/FanisMichalakis), sul [suo blog](https://fanismichalakis.fr/) o tramite il suo lavoro presso [LN Markets](https://lnmarkets.com/).

Ora che avete imparato a conoscere la Lightning Network, vi invito a esplorare gli altri corsi gratuiti sul Piano ₿ Network per approfondire altri aspetti dell'invenzione di Satoshi Nakamoto:

#### Comprendere il funzionamento di un portafoglio Bitcoin con

https://planb.network/courses/cyp201
#### Scoprite la storia delle origini di Bitcoin con

https://planb.network/courses/his201
#### Impostare un server di pagamento BTC con

https://planb.network/courses/btc305
#### Padroneggiare i principi della privacy in Bitcoin

https://planb.network/courses/btc204
#### Imparate le basi dell'attività mineraria con

https://planb.network/courses/min201
#### Scoprite come creare la vostra comunità Bitcoin con

https://planb.network/courses/btc302