---
name: Introduzione a Bitcoin mining
goal: Comprendere Bitcoin mining e proof-of-work da zero
objectives: 


  - Comprendere la proof-of-work e il suo ruolo in Bitcoin.
  - Analizzare il meccanismo di regolazione della difficoltà.
  - Conoscere il significato dei termini tecnici associati al mining.
  - Descrivere le fasi di costruzione di un blocco Bitcoin e dei suoi componenti.
  - Identificare i principali sviluppi del settore mining.


---

# Scoprite i fondamenti del Bitcoin mining



Capire la proof of work vuol dire capire come funziona Bitcoin. Senza questa invenzione e il suo ingegnoso utilizzo, Bitcoin non sarebbe potuto esistere. Questo corso vi fornisce tutta la teoria del mining di cui avete bisogno per il vostro viaggio in bitcoin.



MIN 101 si rivolge principalmente ai principianti, in quanto spiega tutti i concetti partendo da zero. Tuttavia, se avete già un livello di conoscenza intermedio, questo corso vi permetterà di consolidare la vostra comprensione, correggere alcune intuizioni approssimative ed esplorare dettagli spesso mancanti nelle spiegazioni tradizionali.



Alla fine di questo corso, sarete in grado di spiegare il funzionamento della proof-of-work in modo semplice e rigoroso. MIN 101 è anche un'introduzione ideale a tutti gli altri corsi più avanzati dedicati al Bitcoin mining e al Plan ₿ Academy, sia teorici che pratici.



+++


# Introduzione


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Panoramica del corso


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Benvenuti al corso MIN 101, nel quale scoprirete i concetti teorici fondamentali del mining e della Proof-of-Work all'interno del sistema Bitcoin. Questo corso è il primo passo del vostro viaggio da bitcoiner per capire come funziona il mining. Una volta completato, potrete passare a corsi teorici più avanzati, oppure passare all'azione e diventare voi stessi miner di bitcoin!



In questo corso MIN 101 non riprenderemo i concetti di base di Bitcoin, ma andremo dritti al nocciolo della questione: IL mining. Se non avete mai sentito parlare di Bitcoin o se i suoi fondamenti non vi sono ancora chiari, vi consiglio vivamente di iniziare con il nostro corso introduttivo BTC 101. Una volta acquisiti questi fondamenti, sarete in grado di affrontare il MIN 101 con fiducia:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Parte 1 - Introduzione



Inizieremo questo corso con un primo capitolo facoltativo, in cui offrirò una spiegazione molto semplificata del mining, per darvi un quadro mentale chiaro prima di entrare nei meccanismi tecnici.



L'obiettivo non è quello di fornire tutti i dettagli tecnici (che verranno forniti più avanti nel corso), ma di fornire un filo conduttore. Una volta creato questo quadro, ogni concetto più avanzato introdotto in seguito si inserirà naturalmente in questa struttura.



### Parte 2 - Come funziona la proof of work



Dopo l'introduzione, la Parte 2 è la base tecnica del programma di formazione. Il suo scopo è spiegare, passo dopo passo, come Bitcoin produce blocchi validi. Inizieremo a scoprire la struttura di un blocco, prima di approfondire il meccanismo della proof-of-work: il ruolo del target, del nonce e della funzione di hash. Infine, vedremo come Bitcoin riesca a mantenere un tasso di produzione di blocchi stabile nonostante le variazioni della potenza di hash, grazie al meccanismo di regolazione della difficoltà. Alla fine di questa sezione, avrete una comprensione completa dei principi fondamentali di Bitcoin e della proof-of-work.



### Parte 3 - Il sistema di incentivazione Bitcoin mining



Nella terza parte esamineremo il motivo per cui i miner sono incoraggiati a partecipare onestamente al mining. Descriveremo in dettaglio il principio della ricompensa dei blocchi, la sua composizione e il metodo di calcolo, la sua evoluzione nel tempo attraverso gli halvings e il ruolo specifico della transazione coinbase.



### Parte 4 - Il settore Bitcoin mining



La quarta parte riporta il mining nella sua realtà operativa. Si ripercorre l'evoluzione delle macchine mining, dagli inizi di Bitcoin al moderno ASIC, per comprendere gli attuali vincoli hardware. Si analizzano anche le basi delle mining pool, per capire come i miner riescano a ridurre la varianza delle loro entrate.



### Parte 5 - Sezione finale



Nella parte finale del corso, potrete verificare la vostra conoscenza del mining prendendo il diploma.



L'obiettivo di questo corso MIN 101 è quindi quello di consentire una comprensione chiara, strutturata e duratura del Bitcoin mining, sia dal punto di vista tecnico che economico.



Pronti a scoprire il Bitcoin mining? Iniziamo!




## Bitcoin mining reso semplice


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Prima di passare a una spiegazione dettagliata e più tecnica del Bitcoin [mining](https://planb.academy/resources/glossary/mining), vorrei darvi una panoramica del principio, volutamente semplice e schematica. Se avete già delle conoscenze di base, potete entrare direttamente nel vivo della questione nel prossimo capitolo, dopo aver risposto alle domande del quiz. Questo capitolo si rivolge principalmente ai principianti, per fornire loro un inizio delicato.



Immaginate Bitcoin come un grande quaderno pubblico, condiviso da tutti, in cui annotiamo chi ha inviato bitcoin a chi. Questo quaderno si chiama [blockchain](https://planb.academy/resources/glossary/blockchain). Non può essere tenuto da una sola persona, altrimenti ci si dovrebbe fidare di essa. Invece, Bitcoin funziona collettivamente: migliaia di computer verificano e mantengono la stessa versione di questo quaderno.



![Image](assets/fr/049.webp)



In Bitcoin, quando si effettua un pagamento, si crea una [transazione](https://planb.academy/resources/glossary/transaction-tx). Questa transazione non viene aggiunta immediatamente al taccuino. Viene prima inviata alla rete, poi attende di essere integrata nel pacchetto di transazioni successivo. Questo pacchetto è chiamato [blocco](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Un blocco è semplicemente un insieme di transazioni raggruppate. Quando un blocco è pronto, non basta pubblicarlo. Bisogna dimostrare alla rete che il blocco è degno di essere aggiunto al pool. È qui che entra in gioco il mining.



Il Mining è il lavoro di convalida di un blocco consumando energia. Gli attori chiamati [miner](https://planb.academy/resources/glossary/miner) utilizzano computer specializzati. Queste macchine consumano elettricità per eseguire un numero molto elevato di prove, in un ciclo, finché non trovano una prova che la rete accetta. Quando un miner trova questa prova, il suo blocco è considerato valido.



Una volta convalidato, il blocco viene trasmesso alla rete. Gli altri [nodi](https://planb.academy/resources/glossary/node) controllano rapidamente che sia conforme alle regole, quindi lo aggiungono alla sequenza di blocchi precedenti. Per questo si chiama "blockchain": ogni nuovo blocco viene dopo gli altri, in ordine sequenziale, e questa catena cresce poco a poco.



![Image](assets/fr/051.webp)



In sintesi, le transazioni vengono prima create. Poi vengono raggruppate in un blocco. Successivamente, un miner convalida il blocco consumando energia elettrica. Infine, il blocco viene aggiunto alla blockchain e le transazioni in esso contenute vengono [confermate](https://planb.academy/resources/glossary/confirmation).



Se i miner consumano elettricità, non è perché sono volontari. Lo fanno perché c'è una ricompensa. Quando un miner convalida un blocco, riceve due tipi di reddito. Da un lato, riceve i bitcoin appena creati. Dall'altro, raccoglie le [commissioni](https://planb.academy/resources/glossary/transaction-fees) pagate dagli utenti per le transazioni incluse nel blocco. In altre parole, il miner viene compensato sia attraverso l'emissione monetaria programmata, sia attraverso le commissioni di transazione determinate da un mercato.



In questa fase, viene data deliberatamente una visione molto semplice del mining. Non spiega ancora come il blocco sia costruito in dettaglio, né come funziona esattamente la prova che i miner stanno cercando, né come Bitcoin mantenga un ritmo costante, né come la ricompensa sia calcolata con precisione, né come venga richiesta. Non importa, questo è tutto ciò che vedremo nel resto di questo corso MIN 101!



Lo scopo di questo capitolo era semplicemente quello di fornire una chiara struttura mentale: transazioni → blocchi → mining → blockchain → ricompensa. Tenete a mente questa catena di idee. Nel resto del corso, ogni capitolo aggiungerà un livello di dettaglio tecnico su uno di questi elementi, finché non capirete non solo cosa sta succedendo, ma anche come e perché funziona in modo affidabile, su scala, senza un capo e senza bisogno di fiducia.



# Come funziona la proof of work


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Il percorso della transazione Bitcoin


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Per capire che cos'è il Bitcoin mining, dobbiamo innanzitutto seguire il percorso di una tipica transazione Bitcoin. Questo vi mostrerà esattamente dove entra in gioco il blocco e perché è il cuore del sistema. Questo è ciò che vorrei che scopriste in questo primo capitolo.



Nel Bitcoin, una transazione è una struttura di dati che trasferisce la proprietà dei bitcoin da un utente a un altro. In concreto, consuma gli "[output](https://planb.academy/resources/glossary/output)" delle transazioni passate (i cosiddetti [UTXO](https://planb.academy/resources/glossary/utxo)), definendoli "[input](https://planb.academy/resources/glossary/input)", e poi crea nuovi "output" che definiscono a chi appartengono ora questi bitcoin e a quali condizioni possono essere spesi in seguito.



![Image](assets/fr/001.webp)



Un punto importante dei Bitcoin è l'autorizzazione alla spesa. I Bitcoin non sono in un conto, come potrebbe essere il vostro denaro in banca, ma sono bloccati dalle condizioni di spesa. Quando un [wallet](https://planb.academy/resources/glossary/wallet) vuole utilizzare un UTXO come input, deve fornire la prova crittografica di avere il diritto di sbloccarlo. Questa prova assume spesso la forma di una [firma digitale](https://planb.academy/resources/glossary/digital-signature) generata da una [chiave privata](https://planb.academy/resources/glossary/private-key). Ecco perché i bitcoiners insistono sulla necessità di proteggere le chiavi private: sono queste che sbloccano l'accesso ai bitcoin e, di conseguenza, consentono di spenderli.



![Image](assets/fr/002.webp)



La firma digitale in Bitcoin svolge due ruoli importanti:




- Autorizzare la spesa: dimostra che l'utente possiede la chiave privata prevista dalla condizione di spesa UTXO;
- Protezione dell'integrità: collega l'autorizzazione ai dettagli precisi della transazione (destinatari, importi, commissioni, ecc.). Se qualcuno altera la transazione in seguito, la firma non sarà più valida.



Una volta che la transazione è stata costruita e firmata correttamente dal wallet dell'utente, essa deve essere trasmessa sulla rete Bitcoin.



### Il ruolo del nodo Bitcoin nella distribuzione



Bitcoin è una rete [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p): non esiste un server centrale che riceve ed elabora tutte le transazioni. Questo ruolo è svolto collettivamente dai nodi. Un nodo Bitcoin è un software (ad esempio [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) collegato ad altri nodi della rete Bitcoin, la cui missione principale è verificare, memorizzare e trasmettere transazioni e blocchi.



Quando si invia una transazione da un wallet, il wallet la inoltra a un nodo (il proprio o quello di un servizio). Questo nodo verificherà innanzitutto che la transazione sia conforme a varie regole, quali:




- le firme sono valide;
- gli input fanno riferimento a UTXO esistenti (cioè bitcoin che esistono);
- questi UTXO non siano già stati spesi altrove;
- la quantità di uscite è inferiore o uguale alla quantità di entrate (i bitcoin non vengono creati dal nulla);
- ecc.



Se la transazione supera tutti questi controlli, il nodo la propaga agli altri nodi della rete con cui è collegato. Questi la controllano a loro volta e la trasmettono, e così via. In pochi secondi, la transazione viene propagata e diventa nota all'intera rete Bitcoin, o almeno a gran parte di essa.



![Image](assets/fr/003.webp)



### Il mempool: la sala d'attesa delle transazioni



Tra il momento in cui una transazione viene trasmessa e il momento in cui viene confermata in un blocco, deve attendere. Quest'area di attesa è chiamata **[mempool](https://planb.academy/resources/glossary/mempool)** (contrazione di `memory` e `pool`). Un mempool è quindi uno spazio di memoria temporaneo per transazioni valide, ma non ancora confermate.



Punto importante: non esiste una singola mempool, ma solo mempool. Ogni nodo mantiene il proprio mempool, con i propri vincoli locali. Ciò significa che, in qualsiasi momento, due nodi possono avere contenuti di mempool leggermente diversi (a seconda di ciò che hanno ricevuto, di ciò che hanno rifiutato o di ciò che hanno eliminato).



![Image](assets/fr/004.webp)



In questa fase, la rete è a conoscenza della transazione, l'ha verificata e la tiene in memoria fino alla sua conferma. Ma la conferma di questa transazione avverrà solo quando un miner la inserirà in un blocco e questo blocco verrà accettato dalla rete.



### Blockchain: un registro pubblico di marcatura temporale



Essendo una moneta immateriale, il bitcoin deve risolvere un problema: impedire la [doppia spesa](https://planb.academy/resources/glossary/double-spending-attack) senza un'autorità centrale. Se due transazioni tentano di spendere lo stesso UTXO, tutti devono essere in grado di convergere su un unico stato coerente. Satoshi Nakamoto riassume questo problema con questa famosa frase:



> L'unico modo per confermare l'assenza di una transazione è essere a conoscenza di tutte le transazioni.

In altre parole, per sapere che un bitcoin non è già stato speso, è necessario un registro comune delle spese passate.



Questo è il ruolo della blockchain: un registro pubblico contenente la storia delle transazioni. Ma invece di scrivere ogni transazione nel momento in cui avviene, Bitcoin le raggruppa in blocchi. Ogni blocco funge da pagina di cronologia e il sistema funziona quindi come un server di datazione: ordina le transazioni nel tempo in modo verificabile.



Questo registro non può essere riscritto, grazie a un semplice principio: ogni blocco include l'impronta crittografica ([hash](https://planb.academy/resources/glossary/hash-function)) del blocco precedente. I blocchi sono quindi collegati tra loro: se si modifica un blocco del passato, il suo hash cambia, il che interrompe il legame con il blocco successivo, che interrompe il legame con il blocco successivo e così via. È questa catena di dipendenze che dà il nome alla "*blockchain*".



![Image](assets/fr/005.webp)



Una volta compresi questi principi di base di Bitcoin, possiamo descrivere l'obiettivo di un miner in termini più concreti: costruire un nuovo blocco che estenda la catena esistente, iscrivendovi le transazioni in sospeso, e poi tentare di renderlo valido (questo è il famoso "[proof of work](https://planb.academy/resources/glossary/proof-of-work)" che studieremo in un capitolo successivo). Ma prima scopriamo insieme, nel prossimo capitolo, come si costruisce un blocco candidato.



## Costruire un blocco Bitcoin


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Ora avete capito come funziona una transazione Bitcoin e il ruolo della blockchain. Tuttavia, prima di approfondire il funzionamento della proof-of-work, c'è ancora una fase essenziale che il miner deve eseguire: la costruzione di un [blocco candidato](https://planb.academy/resources/glossary/candidate-block). Scopriamo insieme cos'è un blocco candidato e come lo costruisce il miner, prima di intraprendere la ricerca di una prova valida.



### Il blocco candidato



I Miner devono costruire da soli i loro blocchi prima di cercare di estrarli. Ogni miner, a sua volta, costruisce il cosiddetto blocco candidato a partire dalle transazioni in sospeso nella sua mempool. La costruzione di un blocco candidato consiste quindi in:




- scegliere quali transazioni includere;
- organizzare queste transazioni in modo compatibile con le regole di Bitcoin;
- produrre i metadati del blocco, memorizzati nella sua [intestazione](https://planb.academy/resources/glossary/block-header).



La scelta delle transazioni segue una semplice logica economica: un blocco ha una capacità limitata dal protocollo Bitcoin, quindi il miner cerca di massimizzare il guadagno per questo spazio. Seleziona in via prioritaria le transazioni che offrono le commissioni più alte rispetto allo spazio che occupano nel blocco (questo è noto come "fee rate", espresso in sats/vB). I dettagli sulle commissioni saranno trattati in seguito; è sufficiente ricordare l'idea di ordinare in base all'efficienza dello spazio.



Un blocco Bitcoin è quindi composto da due parti principali:




- un elenco di transazioni;
- un'intestazione del blocco, che funge, in un certo senso, da carta d'identità del blocco.



![Image](assets/fr/006.webp)



L'intestazione è essenziale, in quanto viene utilizzata come base per la proof-of-work: in Bitcoin, non si estrae direttamente un intero blocco, ma solo l'intestazione di un blocco, che riassume le informazioni necessarie per collegare il blocco alla catena e impegnarne il contenuto. Per far sì che l'intestazione rappresenti tutte le transazioni, Bitcoin utilizza uno strumento crittografico: [l'albero di Merkle](https://planb.academy/resources/glossary/merkle-tree).



### L'albero di Merkle: riassumere un grande insieme di transazioni



Elencare tutte le transazioni nell'intestazione sarebbe impossibile: un blocco può contenere migliaia di transazioni, mentre l'intestazione ha una dimensione fissa (80 byte). La soluzione è quindi quella di calcolare un hash unico che dipende da tutte le transazioni del blocco: si tratta della radice di Merkle.



Il principio è il seguente:




- viene calcolata l'impronta crittografica (hash) di ogni transazione;
- questi hash vengono accoppiati, concatenati e poi sottoposti a un nuovo hash per formare un nuovo livello di hash;
- questo processo viene ripetuto fino a ottenere un unico hash finale: [la radice di Merkle](https://planb.academy/resources/glossary/merkle-root).



![Image](assets/fr/007.webp)



Quindi, se una singola transazione cambia, anche di un solo bit, il risultato è una modifica della sua impronta digitale, che si propaga alla radice Merkle. Questa radice è inclusa nell'intestazione del blocco. Quindi modificare una transazione passata significa modificare l'intestazione del blocco in cui è inclusa, e quindi l'impronta del blocco, e quindi il collegamento con i blocchi successivi.



Dal [SegWit](https://planb.academy/resources/glossary/segwit), abbiamo separato le firme dal resto. Quindi, in realtà, ci sono due alberi di Merkle annidati all'interno di ogni blocco. Questa separazione ha conseguenze sul modo in cui contiamo la dimensione di un blocco e su alcuni impegni crittografici, ma l'idea di base rimane la stessa: l'intestazione deve impegnare, in modo compatto, tutto il contenuto del blocco.



### Intestazione del blocco



L'intestazione del blocco è lunga 80 byte e contiene esattamente 6 campi. Sono questi sei elementi a essere sottoposti a hashing durante la ricerca di una proof of work (si veda il capitolo successivo):





- La versione (`version`): Indica a quali regole o segnali di aggiornamento si attiene il blocco. Serve come meccanismo per mantenere la compatibilità e l'evoluzione del protocollo.




- Hash del blocco precedente (`previousblockhash`): È l'hash dell'intestazione del blocco precedente. È ciò che collega i blocchi tra loro. Senza questo campo, avremmo blocchi indipendenti. Includendo l'hash dell'intestazione del blocco precedente, si ottiene una catena, in cui ogni nuovo blocco si basa su quello precedente.





- Radice di Merkle (`merkleroot`): È l'impronta digitale di tutte le transazioni del blocco (tramite l'albero di Merkle). Collega l'intestazione al contenuto: se il miner modifica la selezione o l'ordine delle transazioni, la radice cambia.





- [Timestamp](https://planb.academy/resources/glossary/timestamp): Si tratta di un timestamp (ora Unix) scelto dal miner (con vincoli di validità), che deve indicare quando il blocco è stato estratto. Non è necessario che sia perfettamente preciso al secondo, ma deve soddisfare determinate condizioni per rimanere accettabile per la rete.





- [Obiettivo di difficoltà](https://planb.academy/resources/glossary/difficulty-target) codificato (`nbits`): Questo campo codifica l'obiettivo di difficoltà corrente. Si approfondirà nel capitolo sulla difficoltà, ma si ricordi che questo parametro fa parte dell'intestazione.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): È un valore che il miner può modificare liberamente. Serve come variabile regolabile durante la proof-of-work. Spiegherò il suo ruolo in modo più dettagliato nel prossimo capitolo, ma è importante capire che il nonce fa parte dell'intestazione del blocco ed è progettato per consentire tentativi successivi.



Per facilitare la visualizzazione, ecco un esempio di intestazione di blocco in formato esadecimale (80 byte):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Ecco una ripartizione campo per campo:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Questa intestazione del blocco candidato, costruita dal miner, costituisce la base del suo lavoro. Quando si cerca una proof-of-work valida, non è l'intero elenco delle transazioni a essere sottoposto a hash direttamente in un ciclo, ma piuttosto questo blocco di 80 byte, che contiene tutto ciò che serve per collegare il blocco al passato e impegnarne il contenuto, includendo anche i parametri necessari per il meccanismo mining, che analizzeremo nel prossimo capitolo.



## L'hash, il target e il nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



Nei capitoli precedenti abbiamo seguito il percorso di una transazione Bitcoin: creata e firmata da un wallet, trasmessa dai nodi, memorizzata nei mempool, quindi confermata quando un miner la include in un blocco accettato dalla rete. Ma non abbiamo ancora visto come un miner possa aggiungere il suo blocco alla blockchain. Qual è il processo alla base del mining?



La comprensione del processo mining è piuttosto semplice. Si riduce a tre concetti che vanno di pari passo: una funzione hash, un valore target e una variabile che il miner può modificare. Vediamo come funziona il tutto.



### La funzione hash



Una funzione di hash è uno strumento che prende in input un messaggio e produce un output di dimensioni fisse, chiamato "*impronta*" o "*hash*".



![Image](assets/fr/010.webp)



La funzione hash è interessante nei sistemi informatici perché possiede alcune proprietà:





- Se si modifica un singolo bit dell'ingresso, l'hash di uscita risultante cambia completamente e in modo imprevedibile;



![Image](assets/fr/011.webp)





- È impossibile passare dall'uscita all'ingresso: la funzione è irreversibile;



![Image](assets/fr/012.webp)





- È impossibile trovare due messaggi diversi che diano esattamente lo stesso hash.



![Image](assets/fr/013.webp)



La funzione hash utilizzata in Bitcoin per il mining è `SHA256`, applicata due volte di seguito. Questa funzione è nota come doppio [SHA256](https://planb.academy/resources/glossary/sha256), o `SHA256d`. È questo doppio hashing che produce l'impronta digitale del blocco.



```text
hash = SHA256(SHA256(message))
```



Nel nostro caso, il `messaggio' corrisponde in effetti all'intestazione del blocco, che abbiamo visto nel capitolo precedente. Come promemoria, l'intestazione è una piccola struttura che riassume tutto ciò che è contenuto nel blocco.



![Image](assets/fr/014.webp)



### Proof-of-work: trovare un hash più piccolo del target



Proof-of-Work viene spesso descritto come la soluzione di un problema complesso. In realtà, non si tratta tanto di un problema quanto di una ricerca per tentativi: il miner deve trovare una versione dell'intestazione il cui hash (dopo essere passato attraverso la funzione di hash `SHA256d`) rispetti una semplice condizione: deve essere più piccolo di un certo obiettivo.



Questa condizione è formulata come segue:




- l'hash dell'intestazione del blocco viene calcolato con una funzione hash;
- interpretiamo questo hash come un numero;
- affinché il blocco sia valido, questo numero deve essere inferiore o uguale a un valore chiamato "*obiettivo di difficoltà*".



In altre parole, un blocco è valido se:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



L'obiettivo è un numero a 256 bit. Poiché anche l'hash prodotto da `SHA256d` è di 256 bit, possono essere confrontati come due numeri. Più basso è l'obiettivo, più difficile è la condizione, poiché ci sono meno risultati possibili al di sotto di questa soglia. Al contrario, più alto è l'obiettivo, più facile è soddisfare la condizione e più facile diventa estrarre un blocco. Nei prossimi capitoli vedremo più da vicino come viene determinato l'obiettivo.



In questo sistema, la funzione hash è interessante. Ricordiamo che è facile calcolare l'output dall'input, ma è impossibile trovare un input conoscendo solo l'output della funzione. In mining, ai miner non viene chiesto di trovare un hash preciso, ma piuttosto di trovare un hash inferiore a un valore target. L'unico modo per raggiungere questo obiettivo è quello di effettuare un numero molto elevato di tentativi, fino a quando una particolare intestazione del loro blocco candidato, una volta sottoposta a hash, produce un hash inferiore a questo obiettivo.



Quando l'obiettivo è sufficientemente basso, questo processo diventa costoso. Il miner calcola l'hash dell'intestazione del blocco candidato, controlla il risultato e, se la condizione non è soddisfatta, modifica l'intestazione e ripete il calcolo. Questo ciclo viene ripetuto finché non viene trovata un'intestazione valida. Quando l'hash dell'intestazione soddisfa la condizione, la proof of work è stabilita, il blocco è considerato valido e può essere trasmesso sulla rete Bitcoin affinché i nodi lo aggiungano alla loro blockchain. Il miner vincitore riceve quindi la ricompensa associata (ne dettaglieremo la composizione più avanti), mentre tutti i miner partono immediatamente alla ricerca di una nuova intestazione valida per il blocco successivo.



Il vantaggio fondamentale di questo meccanismo risiede nella sua asimmetria. Produrre una proof of work è costoso per i miner, poiché richiede un gran numero di calcoli di hash. D'altra parte, per i verificatori, cioè i nodi della rete, la verifica è estremamente semplice: tutto ciò che devono fare è eseguire l'hash dell'intestazione del blocco fornita dal miner e controllare che l'hash risultante sia effettivamente inferiore all'obiettivo. La ricerca di una prova richiede quindi molto lavoro e risorse, mentre la verifica della sua validità è rapida e poco costosa. È proprio questa proprietà che definisce un sistema proof-of-work efficiente.



### Il nonce



Rimane una questione pratica: se l'header del blocco candidato costruito dal miner non fornisce un hash valido, come può il miner riprovare? Deve modificare qualcosa nell'intestazione per ottenere un hash diverso. È proprio questo il ruolo del nonce.



Ricordiamo la prima proprietà di una funzione hash: basta cambiare un solo bit dell'input per produrre un hash in uscita totalmente diverso e imprevedibile. Ogni calcolo di hash è quindi simile a un'estrazione casuale.



![Image](assets/fr/016.webp)



Per ritentare la fortuna, il miner non ha bisogno di modificare l'intera intestazione del suo blocco candidato: deve solo cambiarne una piccola parte, perché anche un solo bit diverso darà luogo a un hash completamente nuovo, potenzialmente valido se è più piccolo dell'obiettivo.



È proprio per questo che l'intestazione del blocco contiene un nonce. Il nonce è un valore di 32 bit, utilizzato una volta e poi sostituito. In pratica, per lo stesso blocco candidato, un miner può testare circa 4,29 miliardi di valori possibili (da `0` a `2^32 - 1`). Ogni variazione del nonce modifica l'intestazione del blocco e, di conseguenza, cambia completamente l'hash prodotto dopo l'applicazione della funzione di hash `SHA256d`.



Il processo mining è molto semplice:




- il miner costruisce un blocco candidato (transazioni + intestazione);
- calcola quindi l'hash del `SHA256d(header)`;
- se il risultato è maggiore dell'obiettivo, cambia il nonce;
- ricomincia;
- ecc.



![Image](assets/fr/017.webp)



In effetti, il nonce non è l'unico campo che può essere modificato. Qualsiasi modifica all'interno delle transazioni di un blocco comporta una modifica alla radice dell'albero di Merkle, e quindi una modifica all'intestazione del blocco stesso. Con la moderna potenza di calcolo, l'esame dei 4,29 miliardi di valori possibili del nonce può essere effettuato in tempi relativamente brevi. Per questo motivo esiste un altro campo, generalmente chiamato "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", che moltiplica ulteriormente le possibilità di variazione dell'intestazione. Torneremo su questo meccanismo in modo più dettagliato in un capitolo successivo.



### Qual è lo scopo della proof of work?



La chiamiamo "prova" perché il risultato è immediatamente verificabile: una volta prodotto un blocco, qualsiasi nodo può verificare, in una frazione di secondo, che l'hash crittografico della sua intestazione sia effettivamente inferiore all'obiettivo richiesto. Lo chiamiamo "lavoro" perché ottenere questo hash richiede una moltitudine di tentativi, e quindi un costo reale in termini di calcolo ed energia.



Nel [White Paper](https://planb.academy/resources/glossary/white-paper) di Bitcoin, Satoshi Nakamoto presenta due vantaggi nell'utilizzo di un sistema proof-of-work in Bitcoin:





- **Sigillare la storia economica:**



Una volta esaurito il carico computazionale, il blocco è bloccato: modificarlo richiederebbe di rifare la proof of work di quel blocco. E poiché i blocchi sono concatenati, modificare un vecchio blocco significherebbe anche ricalcolare tutti i blocchi successivi, e quindi raggiungere e superare il lavoro in corso della catena onesta.



In altre parole, la proof-of-work funge da spina dorsale del sistema di marcatura temporale, rendendo sempre più costosa la falsificazione del passato man mano che i blocchi si accumulano. Quando viene estratto un nuovo blocco, la sicurezza fornita dalla proof of work viene applicata simultaneamente e uniformemente a tutti i UTXO esistenti. Ad ogni blocco aggiunto, ogni UTXO accumula quindi una quantità supplementare di sicurezza dalla Proof-of-Work.





- **Definire la regola della maggioranza ([consenso](https://planb.academy/resources/glossary/consensus)) e neutralizzare l'[attacco Sybil](https://planb.academy/resources/glossary/sybil-attack):**



La Proof-of-Work permette anche a Bitcoin di raggiungere il consenso senza affidarsi alla regola di voto "un ID = un voto", che potrebbe essere facilmente falsata dalla creazione massiccia di identità (IP, nodi, chiavi...).



In Bitcoin, la "*maggioranza*" non è il maggior numero di partecipanti, ma la **catena che accumula più lavoro**. Come dice Satoshi, si tratta del principio "una CPU = un voto", ossia un voto ponderato in base all'effettiva potenza di calcolo spesa per produrre blocchi validi. Quindi la distribuzione di migliaia di nodi non porta alcun vantaggio in sé rispetto a Bitcoin. Senza potenza di calcolo aggiuntiva, non si accumulano più prove di lavoro e l'attacco Sybil diventa inutile, mentre la regola decisionale rimane oggettiva e non richiede l'identificazione dei partecipanti.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)



I principi relativi all'utilità e ai poteri dei miner sono un argomento molto complesso, che non approfondirò in questo corso. Tuttavia, torneremo su questo argomento in modo approfondito nei prossimi corsi di formazione MIN 201.



Per il momento, è possibile riassumere il funzionamento di mining in questo modo: i miner costruiscono un blocco candidato con le transazioni in sospeso nei mempool, quindi cercano un hash della sua intestazione (tramite `SHA256d`) che sia inferiore o uguale a un obiettivo. Questo obiettivo viene raggiunto testando i nonces attraverso tentativi ed errori.



Nel prossimo capitolo, faremo una breve digressione storica sul principio della proof-of-work per comprenderne il background, per poi esaminare come il sistema determina l'obiettivo di difficoltà.



## La storia della proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



La Proof-of-work non è stata inventata per Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) ha ripreso e assemblato diverse idee precedenti, già esplorate in contesti diversi.



### Hashcash



Alla fine degli anni Novanta, il problema dello spam via e-mail è diventato significativo. Infatti, se inviare un messaggio di posta elettronica non costa quasi nulla, uno spammer può inviarne milioni. Ma se ogni messaggio richiede un piccolo sforzo computazionale, l'invio di un singolo messaggio legittimo rimane facile per un utente normale, mentre l'invio di milioni di messaggi diventa molto costoso.



Questo è l'obiettivo di [Hashcash](https://planb.academy/resources/glossary/hashcash), proposto da Adam Back nel 1997, che è considerato l'invenzione del principio proof-of-work. Il principio del Hashcash è molto simile a quello del mining: produrre un hash che rispetti una condizione (avere un certo numero di zeri all'inizio dell'hash). La prova accompagna il messaggio e può essere verificata molto rapidamente dal destinatario. Se si riceve un'e-mail che non contiene questa prova, può essere immediatamente considerata come spam e quindi filtrata. Gli spammer sono quindi costretti a spendere una notevole quantità di energia per inviare milioni di messaggi, il che riduce drasticamente (o addirittura annulla del tutto) la redditività di questo tipo di operazioni, siano esse di marketing o fraudolente.



Al giorno d'oggi, il Hashcash non viene utilizzato per la posta elettronica. Il filtraggio dello spam si basa ormai in gran parte su sistemi centralizzati. Il vantaggio di Hashcash rispetto alle soluzioni attuali sta nel fatto che non richiede un filtraggio centralizzato: chiunque può regolare i parametri secondo i propri criteri. Non richiede nemmeno l'identificazione, poiché la ricerca dell'hash può essere effettuata in modo anonimo. Soprattutto, non si basa su un sistema di reputazione, che tende a introdurre forme di filtraggio soggettivo.



Hashcash non voleva creare denaro. Cercava di imporre un costo marginale a un'azione digitale facilmente automatizzabile.



![Image](assets/fr/008.webp)



### Bit Gold



Tra la fine degli anni '90 e l'inizio del 2000, Nick Szabo ha esplorato l'idea della scarsità digitale basata sulla proof of work. Il suo progetto concettuale, chiamato Bit Gold, prevede la creazione di unità di valore risolvendo un costoso proof of work e registrando poi queste prove in un registro per stabilire una forma di proprietà.



Bit Gold non ha portato a un sistema distribuito come Bitcoin, ma contiene diverse intuizioni importanti: l'idea che la computazione possa produrre scarsità e l'idea di datare gli elementi nel tempo per creare una storia difficile da riscrivere.



### RPOW



Nel 2004, Hal Finney propose RPOW (*Reusable Proofs of Work*). L'idea era quella di produrre prove di lavoro che potessero essere scambiate, anziché semplicemente consumate. RPOW mirava a creare token digitali basati su proof of work, con un sistema per verificare e trasferire questi token senza duplicarli. Anche in questo caso, RPOW non risolse in modo soddisfacente il problema di un registro totalmente decentralizzato, come avrebbe fatto in seguito il Bitcoin, ma rimane uno dei grandi precursori del Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold e RPOW utilizzano proof-of-work per imporre un costo e creare una forma di scarsità. Il Bitcoin riprende questo meccanismo, ma gli conferisce un ruolo centrale e collettivo: proof-of-work non viene usato solo per creare qualcosa, ma anche per decidere chi ha il diritto di scrivere la pagina successiva del registro (il blocco successivo) e per rendere questo registro costoso da falsificare.



## Regolazione del target di difficoltà


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



Nei capitoli precedenti si è visto il cuore della proof-of-work: i miner eseguono l'hash dell'intestazione del loro blocco candidato con `SHA256d`, e il blocco viene considerato valido solo se l'hash risultante è numericamente inferiore o uguale a un valore di riferimento chiamato target. La domanda che rimane è: da dove viene questo target e come fa il sistema a garantire che rimanga costante nel tempo?



Bitcoin punta a una velocità media di un blocco trovato ogni 10 minuti. Ovviamente, questo ritmo non è garantito al secondo. In pratica, alcuni blocchi vengono trovati pochi secondi dopo il precedente, mentre altri vengono trovati dopo più di un'ora. Ciò che conta è la media su un periodo sufficientemente lungo.



![Image](assets/fr/019.webp)



Questa variabilità deriva dalla natura probabilistica di mining: ogni hash è un tentativo indipendente, con una probabilità costante (supponendo che l'obiettivo rimanga invariato) di produrre un risultato inferiore all'obiettivo. Si può quindi paragonare a una lotteria con estrazione continua: più hash fanno i miner al secondo, minore è il ritardo previsto prima della comparsa di un blocco valido, ma senza mai eliminare la casualità da un'estrazione all'altra.



### Perché puntare a 10 minuti tra un blocco e l'altro?



Sebbene non vi siano prove in merito, Satoshi Nakamoto ha sicuramente scelto 10 minuti come compromesso pratico tra efficienza e sicurezza. Un intervallo più breve darebbe conferme più frequenti, ma provocherebbe un maggior numero di rotture temporanee della rete. Per capire questo punto, dobbiamo tornare al modo in cui un blocco si propaga.



Quando un miner trova un blocco valido, lo distribuisce immediatamente ai suoi pari. I nodi che lo ricevono ne verificano la validità (transazioni, proof of work, regole di consenso, ecc.), quindi lo trasmettono a loro volta. Questa propagazione richiede un certo tempo, limitato dalla latenza di Internet, dalla larghezza di banda e dalla capacità di ciascun nodo di verificare il blocco.



![Image](assets/fr/020.webp)



Se, durante questo ritardo di diffusione, un altro miner scopre un blocco valido alla stessa altezza, la rete può essere temporaneamente divisa: una parte dei nodi e dei miner si affida al blocco A, mentre l'altra si affida al blocco B. Questa è una divisione temporanea della rete.



![Image](assets/fr/021.webp)



Queste divisioni non sono catastrofiche. Il consenso di Nakamoto prevede che, a lungo termine, prevarrà un solo ramo: quello che accumula più lavoro. Infatti, non appena viene estratto un nuovo blocco sopra il blocco A, ad esempio, l'intera rete si risincronizza su questo ramo e abbandona il blocco B, che diventa così un "*[blocco stantio](https://planb.academy/resources/glossary/stale-block)*", talvolta erroneamente chiamato "blocco orfano*" nel linguaggio comune.



![Image](assets/fr/022.webp)



D'altra parte, hanno un costo: per alcuni minuti, una frazione dei miner lavora su un ramo che verrà abbandonato. Questo lavoro è quindi sprecato dal punto di vista della sicurezza generale, poiché non ha contribuito alla catena finale. Quanto più veloce è l'intervallo tra un blocco e l'altro, tanto maggiore è la probabilità che si verifichino tali frazionamenti, poiché il tempo di propagazione rappresenta una parte maggiore del tempo che intercorre tra un blocco e l'altro.



L'intervallo di 10 minuti consente generalmente al blocco vincente di propagarsi ampiamente prima che venga trovato un blocco concorrente alla stessa altezza. Si tratta di un compromesso che limita le suddivisioni, riduce lo spreco di potenza di calcolo e aiuta la rete a rimanere sincronizzata su scala globale.



### Capire il hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" si riferisce alla quantità di calcoli hash prodotti al secondo, sia da un singolo miner, sia da un gruppo di miner, sia da tutti i miner di Bitcoin. È espresso in `H/s` (hash al secondo), con multipli come `TH/s` (terahashes al secondo) o `EH/s` (exahashes al secondo). Rappresenta il numero di tentativi che i miner possono fare ogni secondo per cercare di ottenere un hash inferiore all'obiettivo.



Se l'obiettivo rimane fisso, allora:




- ogni tentativo ha una probabilità fissa di successo;
- fare più tentativi al secondo aumenta la probabilità che appaia rapidamente un tentativo vincente


In altre parole, se domani la rete Bitcoin raddoppiasse la sua potenza di calcolo collegando il doppio delle macchine mining, senza un meccanismo correttivo i blocchi verrebbero trovati in media due volte più velocemente. L'obiettivo deve quindi essere regolato per compensare le variazioni del hashrate.



### Regolazione del target di difficoltà



Bitcoin risolve questo problema con un meccanismo di aggiustamento periodico dell'obiettivo, che regola [la difficoltà](https://planb.academy/resources/glossary/difficulty-adjustment) di mining. Il principio è il seguente: ogni 2016 blocchi (circa ogni 2 settimane), ogni nodo ricalcola l'obiettivo di difficoltà osservando quanto tempo è stato effettivamente necessario per produrre questi 2016 blocchi.



L'obiettivo di questo meccanismo è ridurre il tempo medio di produzione di un blocco a circa 10 minuti, mentre il hashrate complessivo della rete cambia continuamente, a causa della disconnessione di macchine o, al contrario, dell'aggiunta di nuove macchine.



![Image](assets/fr/023.webp)



Il calcolo si basa sul tempo osservato per il periodo trascorso:




- se gli ultimi blocchi del 2016 sono stati trovati troppo velocemente, significa che il hashrate è aumentato durante questo periodo; Bitcoin rende quindi la condizione più difficile abbassando l'obiettivo per il periodo successivo;
- se i blocchi 2016 sono stati trovati troppo lentamente, significa che hashrate è diminuito; Bitcoin allevia la condizione aumentando l'obiettivo.



La formula è la seguente:



```txt
Tn = To * (Ta / Tt)
```



Con:




- `tn`: nuovo obiettivo
- `to`: vecchio obiettivo
- `Ta`: tempo reale trascorso per gli ultimi 2016 blocchi
- `Tt`: tempo di destinazione (in secondi)



Con un tempo obiettivo di due settimane, cioè `Tt = 1.209.600` secondi:



```txt
Tn = To * (Ta / 1 209 600)
```



Per capire come regolare la difficoltà di Bitcoin mining, ecco un esempio con valori fittizi:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Con:



- `**To = 18.045.755.102**`: Vecchio obiettivo, ovvero il valore di riferimento prima dell'adeguamento.
- `**ta = 1.000.000 secondi**`: Tempo effettivamente impiegato per produrre gli ultimi 2016 blocchi. Poiché questo tempo è inferiore al tempo previsto, la rete ha estratto troppo velocemente.
- `**1.209.600 secondi**`: Tempo target corrispondente a 10 minuti per blocco per i blocchi 2016, utilizzato come riferimento per l'adeguamento.
- `**tn = 14.918.779.020**`: Nuovo obiettivo calcolato dopo l'aggiustamento della difficoltà.



In questo caso, il nuovo obiettivo è inferiore a quello precedente, il che significa che il mining diventa più difficile per rallentare la produzione di blocchi nel periodo successivo.


*I valori target di questo esempio sono semplificati e scalati a scopo didattico; il target effettivo utilizzato in Bitcoin è un intero a 256 bit di un ordine di grandezza completamente diverso.*



Questo calcolo viene eseguito localmente da ogni nodo, sulla base dei timestamp inseriti nei blocchi. Poiché tutti i nodi applicano le stesse regole, giungono allo stesso risultato e il nuovo obiettivo diventa il riferimento comune per i prossimi blocchi 2016.



C'è un dettaglio importante da notare su questa regolazione: **è limitato**. Il Bitcoin limita la variazione di difficoltà per periodo, per evitare cambiamenti troppo bruschi che potrebbero bloccarlo. Infatti, il tempo effettivo preso in considerazione è vincolato a rimanere in un intervallo equivalente a un fattore 4 (minimo un quarto del vecchio obiettivo, massimo quattro volte il vecchio obiettivo). Ciò impedisce un retargeting estremo se i timestamp sono altamente atipici o manipolati.



Notiamo inoltre che in realtà, l'aggiustamento della difficoltà di Bitcoin non è perfettamente esatto. In effetti, abbiamo visto che è previsto per ricalcolare la difficoltà ogni 2016 blocchi, confrontando il tempo reale trascorso con il tempo target di 14 giorni (2016 × 10 minuti). Tuttavia, il codice originale di Satoshi contiene un errore cosiddetto "*off-by-one*": invece di misurare il tempo tra gli ultimi blocchi di ogni periodo (cioè 2016 intervalli), misura il tempo tra il primo e l'ultimo blocco, ovvero solo 2015 intervalli. Concretamente, la difficoltà viene calcolata come se il periodo comprendesse solo 2015 blocchi invece di 2016. La conseguenza è che la difficoltà è sistematicamente leggermente sopravvalutata, il che fa sì che i blocchi vengano minati in media un po' meno velocemente dei 10 minuti previsti (circa lo 0,05% più lentamente). Questo bug è ben noto ma non è mai stato corretto, poiché modificarlo richiederebbe un hard fork e il suo impatto rimane trascurabile in pratica, al di fuori dell'attacco teorico denominato "*time warp*".

### Rappresentazione dell'obiettivo



Nell'intestazione del blocco, il target non appare nella sua forma completa a 256 bit, perché occuperebbe troppo spazio. Invece, il campo `nBits' a 32 bit codifica il target in un formato compatto, paragonabile alla notazione scientifica in base 256: un esponente (1 byte) e un coefficiente (3 byte). Il target completo viene quindi ricostruito a partire da questi due valori. Non entreremo nel dettaglio in questa sede, poiché l'argomento è relativamente complesso e non aggiunge nulla alla comprensione del mining. È sufficiente ricordare che il target non è memorizzato in forma grezza nell'intestazione del blocco, ma in forma compatta.



Con questo capitolo finale della Parte I, abbiamo fatto un giro su come funziona la proof-of-work nel Bitcoin: il miner costruisce un blocco candidato selezionando le transazioni dalla sua mempool, calcola l'header del blocco candidato, lo sottopone a hash, confronta l'hash risultante con l'obiettivo del periodo, quindi ricomincia modificando il nonce fino a ottenere un hash valido. Infine, ogni 2016 blocchi, la rete ricalcola un nuovo obiettivo in modo da mantenere un tempo medio di circa 10 minuti per blocco, nonostante le costanti variazioni di hashrate.




# Il sistema di incentivi Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Come potete immaginare, il Bitcoin mining non è un'attività altruistica. I Miner hanno dei costi reali: l'elettricità per far funzionare i loro computer mining, l'acquisto di attrezzature specializzate, le paghe per la manutenzione, a volte i locali e i sistemi di raffreddamento. Affinché il sistema Bitcoin funzioni, gli interessi privati dei miner devono essere allineati con gli interessi collettivi della rete. Questo è esattamente il ruolo della ricompensa mining. Incoraggia i miner a investire nella proof of work, a includere transazioni valide e a rispettare le regole del protocollo piuttosto che cercare di corromperlo.



Questa logica si basa sulla teoria dei giochi: il protocollo rende razionale l'onestà. Un miner guadagna denaro quando produce un blocco valido accettato dai nodi. Al contrario, se cerca di imbrogliare, il suo blocco verrà rifiutato dai nodi e non otterrà nulla. Poiché produrre un blocco ha un costo, un blocco rifiutato rappresenta una perdita diretta. In un ambiente competitivo in cui migliaia di giocatori sono alla ricerca simultanea di un blocco valido, la strategia più redditizia, nella maggior parte dei casi, è quindi quella di seguire rigorosamente le regole e massimizzare le entrate in modo onesto.



A tal fine, il protocollo Bitcoin stabilisce che il miner che trova un blocco valido si aggiudica il diritto di includervi una particolare transazione, che gli vale una certa somma di BTC. Questo è noto come **[compenso del blocco](https://planb.academy/resources/glossary/block-reward)**. In questo primo capitolo di questa sezione, l'obiettivo è capire da cosa è composta e come viene determinata. In seguito, vedremo come la parte di creazione del denaro si evolve nel tempo (con i dimezzamenti) e come viene effettivamente riscosso tecnicamente (tramite la transazione su coinbase).



### In cosa consiste la ricompensa in blocco?



Nei capitoli precedenti abbiamo visto come i miner riescono a trovare un blocco valido. Una volta che un miner ha trovato un'intestazione il cui hash è più piccolo dell'obiettivo, il suo blocco candidato è considerato valido. Può quindi distribuirlo a tutta la rete Bitcoin. Il blocco viene aggiunto al resto della blockchain, confermando le transazioni che contiene.



È proprio questo evento (l'aggiunta effettiva del blocco alla blockchain) che determina l'assegnazione di una ricompensa al miner vincitore. Questa ricompensa è composta da due elementi distinti che vengono sommati:




- [sovvenzione in blocco](https://planb.academy/resources/glossary/block-subsidy)**;
- spese di transazione**.



![Image](assets/fr/024.webp)



Vediamo a cosa corrispondono queste due parti della ricompensa.



### Sovvenzione in blocco



Il sussidio di blocco corrisponde alla parte di creazione monetaria della ricompensa. Quando un miner produce un blocco valido, il protocollo lo autorizza a creare un certo numero di nuovi bitcoin e ad assegnarseli come ricompensa. Questi bitcoin sono creati ex nihilo. Non esistevano prima.



Tuttavia, la quantità di nuovi bitcoin creati non è affatto arbitraria. È strettamente definita dalle regole del protocollo Bitcoin ed è identica per tutti i miner. Analizzeremo più da vicino questo meccanismo nel prossimo capitolo, poiché la sovvenzione non è un valore fisso all'infinito: viene suddivisa periodicamente secondo un preciso programma. Per ora è sufficiente ricordare che:




- il sussidio di blocco è una delle due componenti del premio di blocco;
- è limitato e determinato dal protocollo, non dal miner (anche se il miner può tecnicamente richiedere meno dell'importo massimo);
- crea bitcoin dal nulla.



Questa sovvenzione svolge due ruoli principali all'interno del protocollo Bitcoin. La prima è quella di incoraggiare i giocatori a partecipare al mining. Nei primi anni di Bitcoin (e talvolta ancora oggi), le commissioni di transazione erano molto basse. La sovvenzione ha quindi garantito un compenso sufficiente per attirare i miner e mantenere un livello di sicurezza per il sistema.



Il secondo ruolo riguarda la distribuzione della moneta. Qualsiasi nuova valuta deve affrontare il problema di come distribuire equamente le unità monetarie alla popolazione. Il sussidio di blocco fornisce una risposta a questo problema. Creando bitcoin tramite il mining, ne consente la distribuzione iniziale in modo aperto e neutrale: chiunque può ottenerli, purché partecipi al mining, senza che sia necessaria alcuna autorizzazione o identificazione preventiva.



D'altra parte, poiché questi bitcoin sono stati creati dal nulla, il loro valore non è privo di basi. Aumentando la quantità di denaro in circolazione, la sovvenzione diluisce meccanicamente il valore dei bitcoin esistenti. Introduce quindi una forma di inflazione monetaria. Tuttavia, vedremo nel prossimo capitolo che questa sovvenzione è destinata a scomparire gradualmente e che l'inflazione finirà per cessare.



![Image](assets/fr/025.webp)



### Commissioni di transazione



La seconda componente della ricompensa dei blocchi è legata all'utilizzo del sistema: quando un utente inserisce una transazione, vuole che questa venga confermata. Tuttavia, lo spazio per i blocchi è limitato e i blocchi appaiono in media solo ogni 10 minuti circa. Lo spazio per i blocchi è quindi una risorsa scarsa. Quando la domanda supera l'offerta, il prezzo aumenta: questo è il mercato delle commissioni di transazione. Ogni miner che riesce a produrre un blocco valido ottiene il diritto di riscuotere, per proprio conto, l'intera commissione di transazione associata a tutte le transazioni che ha incluso nel suo blocco.



Si può pensare a un sistema di aste: ogni transazione propone un importo, e i miner danno la priorità a quelle che massimizzano le loro entrate, nel rispetto dei vincoli di spazio. Questo meccanismo allinea naturalmente gli interessi:




- gli utenti che hanno fretta pagano di più per essere inclusi rapidamente;
- i miner sono incoraggiati a includere le transazioni che pagano le fee più alte per lo spazio dei blocchi.
- la rete evita lo spam, perché la pubblicazione di una transazione ha un costo.



#### Come vengono calcolate le commissioni di transazione?



Contrariamente a quanto si crede, le fee non sono un output in una transazione Bitcoin. In realtà, una transazione spende input e crea output. Gli input rappresentano la fonte dei bitcoin utilizzati, mentre gli output rappresentano la destinazione dei pagamenti. Le commissioni di transazione sono semplicemente **la differenza tra gli input totali e gli output totali**.



In altre parole, gli input di bitcoin dell'utente, che gli appartengono, creano output per i destinatari, ma non riproducono l'intero importo consumato dagli input. La differenza tra i due rappresenta le commissioni di transazione che il miner può riscuotere.



Facciamo un esempio. Una transazione consuma due input, uno di `100.000 sats` e l'altro di `150.000 sats`, e crea tre output di `35.000 sats`, `42.000 sats` e `170.000 sats`.



![Image](assets/fr/027.webp)



La somma degli input è quindi di `250.000 sats`, mentre la somma degli output è di `247.000 sats`. Ciò significa che `3.000 sats` sono stati consumati negli input senza essere ricreati negli output: questo importo corrisponde alle fee proposte da questa transazione.



![Image](assets/fr/028.webp)



Se un miner include questa transazione in un blocco valido, avrà diritto a recuperare questi `3.000 sats`, oltre alle commissioni di tutte le altre transazioni incluse nel blocco. Tuttavia, non esiste un legame diretto on-chain tra la transazione che paga la fee e i sats effettivamente riscossi dal miner. Tecnicamente, i `3.000 sats` di commissioni vengono distrutti e, in cambio, il miner ottiene il diritto di ricreare la stessa quantità per sé.



#### Il rapporto di remunerazione



Un blocco non è limitato dal numero di transazioni, ma dalla sua capacità totale (oggi, in pratica, dal peso del blocco). Alcune transazioni occupano più spazio di altre: una transazione con molti input e output sarà più grande di una semplice transazione con un singolo input e due output. Anche gli script utilizzati influiscono sulle dimensioni.



![Image](assets/fr/026.webp)



Due transazioni possono quindi pagare lo stesso importo di tasse in termini assoluti, ma non essere economicamente equivalenti dal punto di vista del miner. Se una di esse è due volte più grande, costa il doppio dello spazio nel blocco. Lo spazio è scarso, quindi il miner cerca di massimizzare le sue entrate per unità di spazio.



Per questo motivo, in pratica, esprimiamo la competitività di una transazione con un rapporto di commissioni, solitamente in `sats/vB` ([satoshi](https://planb.academy/resources/glossary/satoshi-sat) per byte virtuale). Il calcolo di questo rapporto è semplice:



```text
fee rate = fee / weight (in vB)
```



Ad esempio, se una transazione pesa `141 vB` e assegna `1.974 sats` in commissioni, avrà un tasso di commissione di `14 sats/vB`.



```text
1 974 / 141 ≈ 14 sats/vB
```



Questo rapporto spiega le scelte economiche dei miner: a capacità fissa, l'inclusione di transazioni ad alto tasso massimizza le fee totali del blocco e quindi il compenso del miner. Spiega anche perché le transazioni a basso costo rimangono in coda nei mempool per lunghi periodi: sono in concorrenza con altre transazioni che pagano di più per unità di spazio.



### Protezione della rete contro lo spam



Le commissioni hanno anche uno scopo di sicurezza operativa: introducono un costo alla moltiplicazione delle transazioni. Se la pubblicazione di una transazione fosse gratuita, sarebbe facile inondare la rete di transazioni inutili e saturare i mempool, aumentando il carico sui nodi.



In pratica, i nodi applicano politiche di relay locali (regole di mempool) e spesso fissano una soglia minima di fee al di sotto della quale non relayano una transazione (per impostazione predefinita, `0,1 sat/vB` in Bitcoin Core tramite `minRelayTxFee`). Una transazione può essere valida nel senso stretto delle regole di consenso, ma non trasmessa dalla maggior parte dei nodi se le sue fee sono troppo basse. Di conseguenza, non circola, non raggiunge i miner e ha poche possibilità di essere confermata.



A questo punto, avete capito il senso della ricompensa di blocco: corrisponde al compenso per il miner vincente ed è composta da due elementi distinti. Da un lato, una sovvenzione di blocco, definita dalle regole del protocollo, che crea nuovi bitcoin ex nihilo. Dall'altro, le fee delle transazioni incluse nel blocco minato.



Nel prossimo capitolo ci concentreremo più dettagliatamente sul sussidio in blocco, per capire esattamente come viene calcolato e come si evolve nel tempo secondo le regole del protocollo Bitcoin.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



Nel capitolo precedente abbiamo visto che i miner che producono un blocco valido ricevono una ricompensa costituita dalle commissioni per le transazioni incluse nel blocco, più una sovvenzione per il blocco. Tuttavia, non abbiamo ancora spiegato come viene determinato l'importo di questa sovvenzione. Il meccanismo che stabilisce ed evolve questo valore è noto come ***[halving](https://planb.academy/resources/glossary/halving)***.



### Che cos'è il dimezzamento?



Il Halving è un evento programmato nel protocollo Bitcoin che dimezza la sovvenzione del blocco, ossia la quantità massima di nuovi bitcoin che il miner vincitore può creare con ogni blocco. Non influisce sulle commissioni di transazione: le commissioni esistono indipendentemente e rimangono determinate dall'attività degli utenti e dalla competizione per lo spazio dei blocchi.



Quando Bitcoin è stato lanciato nel 2009, la sovvenzione per i blocchi è stata fissata a 50 BTC per ogni blocco estratto. Da allora, questa sovvenzione è stata dimezzata più volte per ogni dimezzamento.



![Image](assets/fr/029.webp)



Il Halving non viene attivato da una data, ma dall'altezza del blocco. Viene eseguito **ogni 210.000 blocchi**. Poiché Bitcoin punta a un intervallo medio di circa 10 minuti per blocco, 210.000 blocchi corrispondono a circa quattro anni.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Quindi, se consideriamo `n` il numero di dimezzamenti già avvenuti, il sussidio di blocco in BTC può essere calcolato come segue:



```text
subsidy(n) = 50 / 2^n
```



### Dimezzamenti passati



Ecco una tabella riassuntiva dei dimezzamenti già avvenuti, con l'altezza del blocco, la data e la nuova sovvenzione del blocco applicabile dopo l'evento:



| Evento               |   Altezza  | Data                        | Sovvenzione |
| -------------------- | ---------: | --------------------------- | ----------: |
| Halving 1            |   210 000  | 28 novembre 2012            |      25 BTC |
| Halving 2            |   420 000  | 9 luglio 2016               |    12,5 BTC |
| Halving 3            |   630 000  | 11 maggio 2020              |    6,25 BTC |
| Halving 4            |   840 000  | 20 aprile 2024              |   3,125 BTC |
| Halving 5 (prossimo) | 1 050 000  | Primavera 2028 (stima)      |  1,5625 BTC |

### Quando e come termina la sovvenzione?



Halving si ripete finché la sovvenzione può essere espressa nell'unità minima del sistema: satoshi.



```text
1 BTC = 100 000 000 sats
```



Con il dimezzamento della sovvenzione, si arriva a frazioni di bitcoin così piccole da diventare meno di 1 satoshi. A questo punto, non è più possibile creare mezza unità di satoshi. La creazione di denaro attraverso la sovvenzione dei blocchi cessa e i miner vengono compensati esclusivamente sulla base delle commissioni di transazione. Da questo momento in poi, tutti i bitcoin saranno in circolazione e non sarà più possibile produrre nuove unità.



La fine definitiva delle sovvenzioni ai blocchi avverrà al livello di blocco 6.930.000, cioè al 33° e ultimo dimezzamento. Si prevede che questo evento si verifichi intorno all'anno 2140, anche se non è possibile indicare una data esatta, poiché dipenderà dalla velocità effettiva con cui verranno trovati i blocchi da qui ad allora.



Poiché la sovvenzione dei blocchi segue una sequenza geometrica con un rapporto di 1/2 ad ogni dimezzamento, la creazione di denaro è stata estremamente elevata nei primi giorni del Bitcoin, per poi diminuire molto rapidamente. Al settimo dimezzamento, oltre il 99% dei bitcoin sarà già stato messo in circolazione. La soglia del 99% dovrebbe essere superata tra il 2032 e il 2036. Ciò significa che ci vorranno oltre 100 anni per estrarre l'ultimo 1% di bitcoin rimasto. Se al momento del lancio del Bitcoin l'inflazione monetaria era molto alta, per consentire una distribuzione capillare della moneta, ora è molto bassa e continuerà a scendere, fino a raggiungere il livello di una vera e propria moneta forte, la cui offerta in circolazione non può più aumentare.



![Image](assets/fr/030.webp)



### Perché non ci saranno mai 21 milioni di BTC?



L'offerta monetaria massima di Bitcoin viene spesso presentata come 21 milioni di BTC. Si tratta di una buona approssimazione per comprendere la sua politica monetaria, ma da un punto di vista strettamente tecnico, l'offerta totale non raggiungerà mai esattamente 21.000.000 di bitcoin.



La ragione principale è di tipo meccanico. Attraverso successivi dimezzamenti, la sovvenzione in blocchi finisce per scendere al di sotto del valore minimo di 1 sat, che termina l'emissione prima di raggiungere il totale teorico esatto. A causa di questa granularità minima e delle regole di arrotondamento, il numero totale di bitcoin creati dalla sovvenzione è leggermente inferiore a 21 milioni.



A ciò si aggiungono anche deviazioni marginali legate al protocollo. Ad esempio, in rari casi, alcuni miner potrebbero non aver richiesto l'intera sovvenzione, il che riduce definitivamente la quantità di bitcoin effettivamente emessi. Possiamo anche citare il [blocco genesis](https://planb.academy/resources/glossary/genesis-block), prodotto da Satoshi il 3 gennaio 2009, i cui bitcoin creati non fanno parte del [UTXO set](https://planb.academy/resources/glossary/utxo-set), così come alcuni eventi storici legati ai bug, come la duplicazione degli identificativi delle transazioni su coinbase.



Infine, dobbiamo tenere conto di tutti i bitcoin che sono stati distrutti o bloccati:




- bitcoin bloccati in script irrisolvibili;
- quelli deliberatamente distrutti dagli script `OP_RETURN`;
- o perdita di chiavi private a livello di applicazione.



In teoria, l'offerta di Bitcoin è quindi limitata a 21 milioni. In pratica, però, non ci saranno mai 21 milioni di bitcoin in circolazione.



## La transazione su coinbase


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



Nei capitoli precedenti abbiamo presentato due punti importanti. In primo luogo, il miner che riesce a produrre e distribuire un blocco valido riceve una ricompensa. D'altra parte, abbiamo visto che questa ricompensa è composta da due elementi distinti:




- una sovvenzione di blocco (bitcoin creati ex nihilo, il cui importo massimo è fissato dal protocollo e ridotto gradualmente tramite gli halving);
- tutte le commissioni di transazione pagate dagli utenti le cui transazioni sono state incluse nel blocco.



Rimane tuttavia una domanda: con quale meccanismo il miner raccoglie questa ricompensa in Bitcoin? È proprio questo il ruolo di una particolare transazione chiamata "coinbase".



### Come funziona la transazione su coinbase



Come abbiamo visto nella prima parte del corso, ogni blocco Bitcoin contiene un elenco di transazioni in attesa di conferma. La prima di queste è sempre la [transazione coinbase](https://planb.academy/resources/glossary/coinbase-transaction). È quella che permette al miner vincitore di ricevere la sua ricompensa.



![Image](assets/fr/031.webp)



A prima vista, sembra una classica transazione Bitcoin: ha un [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), esce ed è inclusa nell'albero Merkle del blocco. Tuttavia, si differenzia per un aspetto importante: non spende alcun UTXO esistente.



In una classica transazione Bitcoin, gli `ingressi` fanno riferimento a precedenti uscite non spese (UTXO), che forniscono il valore di ingresso. Le uscite ridistribuiscono poi questo valore a nuovi UTXO, con nuove condizioni di spesa. In altre parole, per inviare bitcoin è necessario possederli già. La transazione coinbase, invece, non consuma bitcoin in ingresso: crea bitcoin in uscita direttamente da zero.



È proprio questo meccanismo che consente l'immissione in circolazione di nuovi bitcoin attraverso la sovvenzione del blocco e che accredita al miner le commissioni associate alle transazioni incluse nel blocco. La transazione coinbase non può fare riferimento a un UTXO realmente esistente (anzi, fa riferimento a un UTXO fittizio), poiché il suo ruolo è proprio quello di creare una parte del valore (la sovvenzione) e recuperare l'altra parte (le commissioni), senza riceverle da una transazione precedente. Affinché l'intero sistema rimanga coerente, la parte corrispondente alle commissioni deve essere esattamente uguale alla somma dei bitcoin consumati in input ma non ricreati in output nelle altre transazioni del blocco.



![Image](assets/fr/032.webp)



Questa transazione non è facoltativa. Un blocco che non contiene una transazione coinbase non è valido e verrà sistematicamente rifiutato dai nodi della rete.



⚠️ Nota bene: il termine "*coinbase*" non ha alcun legame con l'omonima piattaforma di scambio. Nel Bitcoin, "*coinbase*" si riferisce storicamente alla transazione che crea la ricompensa del blocco. La società ha semplicemente adottato questo termine per il suo nome.



La transazione su coinbase svolge in realtà diversi ruoli contemporaneamente:




- Il primo è quello appena descritto: assegna al miner la ricompensa che gli spetta per aver prodotto un blocco valido.
- Il suo secondo ruolo, più tecnico, è quello di ancorare l'impegno crittografico ai testimoni (firme) delle transazioni SegWit incluse nel blocco.
- Un terzo ruolo, questa volta non direttamente legato al protocollo ma alla moderna industrializzazione del mining, è che il coinbase è ora frequentemente utilizzato per ancorare dati tecnici arbitrari. Questi dati sono generalmente legati al funzionamento delle mining pool e alla loro organizzazione interna.



Per aiutarvi a comprendere questi diversi utilizzi, daremo ora un'occhiata più da vicino alla struttura della transazione su coinbase.



### La struttura di base della transazione su coinbase



Una transazione coinbase deve contenere esattamente un ingresso. Per semplicità, a volte diciamo che non ha alcun input, perché questo input non spende alcun UTXO reale. In realtà, esiste un input con una fonte di riferimento, ma punta deliberatamente a un UTXO inesistente.



Come abbiamo già visto, ogni transazione Bitcoin deve consumare i UTXO come input per creare output validi. Nella transazione Bitcoin, questo consumo assume la forma di un riferimento a un UTXO esistente come input. Questo riferimento avviene semplicemente indicando l'identificatore della transazione precedente (quella in cui è stato creato il UTXO) e il suo indice tra gli output di questa transazione. In concreto, un UTXO è definito da un hash (il TXID precedente) e da un indice.



Ma nel caso della transazione coinbase, invece di fare riferimento a un UTXO realmente esistente, l'input deve necessariamente puntare a questo particolare UTXO falso, con un TXID pieno di zeri, che non corrisponde a nessun TXID reale:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Seguito direttamente dal falso indice:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



Nel protocollo di base Bitcoin, come descritto in Satoshi Nakamoto, questo falso ingresso è l'unico vincolo imposto alla transazione coinbase.



Come ogni UTXO a cui si fa riferimento nell'input di una transazione, è associato a un campo `scriptSig`. In una transazione convenzionale, questo campo `scriptSig` contiene gli elementi necessari per soddisfare la `scriptPubKey` e quindi sbloccare la UTXO spesa. Ma nel caso particolare di coinbase, poiché la UTXO a cui si fa riferimento è deliberatamente fittizia, il campo `scriptSig` è completamente libero. I Miner possono quindi inserire i dati che desiderano. Vedremo più avanti come viene utilizzata questa libertà.


Oltre a questo falso ingresso, ci sono una o più uscite perfettamente standard, che consentono al miner di raccogliere i bitcoin dalla ricompensa su uno dei suoi indirizzi Bitcoin . Queste uscite sono UTXO bloccate da una `scriptPubKey` (ad esempio uno script che punta a un indirizzo controllato dal miner o dal pool). L'unica particolarità sta nella regola per il calcolo del loro valore: la somma totale delle uscite della coinbase non deve mai superare la sovvenzione massima consentita, a cui si aggiungono le commissioni di blocco.



Storicamente, quindi, la transazione coinbase si riduce a questo semplice schema: un input falso che fa riferimento a un UTXO inesistente e uno o più output progettati per distribuire la ricompensa del blocco al miner vincente. Oggi, tuttavia, la coinbase non si limita più a questo ruolo di distribuzione. La sua particolare posizione nel blocco e la grande flessibilità della sua struttura hanno portato a nuovi utilizzi, sia nel protocollo stesso che nei meccanismi di gestione delle mining pool.



### Altri usi di coinbase



Nel corso del tempo, la transazione coinbase è diventata un punto di inserimento particolarmente comodo per integrare una serie di informazioni utili per il mining e per la struttura stessa del blocco. Vediamole per capire meglio l'organizzazione complessiva di coinbase.



#### Il modello BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) è un fork soft distribuito nel marzo 2013, a partire dal blocco 227.930, che ha introdotto la versione 2 dei blocchi Bitcoin. Questa nuova versione richiede che ogni blocco includa, nello `scriptSig` della transazione coinbase, l'altezza del blocco creato.



Da un lato, questa evoluzione chiarisce il modo in cui la rete accetta di evolvere la struttura dei blocchi e le regole di consenso. In secondo luogo, garantisce l'unicità di ogni blocco e di ogni transazione di coinbase.



Pertanto, il `scriptSig` di coinbase non è totalmente libero. Dall'attivazione del BIP-34, è semplicemente vincolato a iniziare con l'altezza del blocco in cui questa transazione coinbase è inclusa.



![Image](assets/fr/035.webp)



#### L'extra-nonce



Come abbiamo visto nei primi capitoli di questo corso, il miner dispone di un campo nonce a 32 bit nell'intestazione del blocco, che modifica per tentativi ed errori per trovare un hash minore o uguale all'obiettivo. Questo spazio di 32 bit consente già di esplorare un numero molto elevato di combinazioni, ma quando la difficoltà del mining è elevata, questa gamma può essere completamente esaurita in un tempo relativamente breve e quindi potrebbe non produrre alcuna combinazione che produca un hash valido. Se tutti i possibili valori di `nonce` sono stati testati senza successo, il miner deve modificare un altro elemento per cambiare l'intestazione del blocco e iniziare una nuova serie di tentativi.



Poiché la transazione coinbase offre un campo libero attraverso lo `scriptSig` del suo input, la soluzione utilizzata per estendere lo spazio del nonce è quella di sfruttare parte di questo `scriptSig`. Questo viene generalmente chiamato extra-nonce. Modificando l'extra-nonce, il miner modifica lo `scriptSig` della coinbase, cioè l'identificatore della transazione, poi la radice Merkle del blocco e infine l'intestazione del blocco stesso. In questo modo, si ottiene un nuovo spazio di ricerca di hash da esplorare, senza dover modificare gli altri componenti del blocco candidato.



![Image](assets/fr/036.webp)



#### Identificazione di pool e miner



Oggi, una parte molto consistente del hashrate mondiale è organizzata in mining pool. Queste strutture riuniscono i singoli miner per combinare il loro lavoro e ridurre la varianza del loro reddito.



Per ragioni operative, le mining pool sfruttano anche il campo libero del `scriptSig` dell'input di coinbase per inserire varie informazioni. Queste variano da pool a pool e da protocollo di rete a protocollo di rete, ma generalmente includono un identificatore unico (spesso un nonce extra strutturato in diverse sottoparti) assegnato a ciascun miner, per evitare la duplicazione del lavoro all'interno del pool. Di solito viene aggiunto un tag di identificazione del pool, utilizzato per l'attribuzione pubblica dei blocchi trovati, per le statistiche mining e per altri scopi di tracciamento.



![Image](assets/fr/037.webp)



#### L'impegno di SegWit



Dall'abilitazione del SegWit soft fork nel 2017, i dati dei testimoni (cioè generalmente le firme) sono stati separati dai dati anagrafici delle transazioni, in particolare per correggere il problema della [malleabilità delle transazioni Bitcoin](https://planb.academy/resources/glossary/malleability-transaction). Questa separazione introduce quindi un nuovo elemento da impegnare nel blocco.



Per fare ciò, i testimoni vengono raggruppati in un altro albero di Merkle dedicato, la cui radice viene poi impegnata nella transazione coinbase tramite un output `OP_RETURN`.



![Image](assets/fr/038.webp)



Non approfondirò questo meccanismo in questo corso, perché esula dallo scopo di questo articolo, ma è sufficiente ricordare che dall'introduzione del SegWit, la transazione coinbase serve come veicolo per ancorare nel blocco un'impronta digitale che riassume tutti i testimoni del SegWit. I testimoni sono inseriti in un albero di Merkle indipendente, la radice di questo albero è scritta in un output della transazione coinbase, e questa transazione coinbase è a sua volta inclusa nell'albero di Merkle principale insieme a tutte le altre transazioni, la cui radice appare nell'intestazione del blocco. In questo modo i testimoni, memorizzati separatamente dai dati della transazione principale, sono ancora impegnati nell'intestazione del blocco.



![Image](assets/fr/039.webp)



#### Messaggi arbitrari



Poiché lo `scriptSig` permette di inserire liberamente informazioni arbitrarie scelte dal miner, alcuni hanno sfruttato l'opportunità di aggiungere messaggi di natura più personale, piuttosto che tecnica. Il caso più famoso è ovviamente quello di Satoshi Nakamoto, con il suo ormai iconico messaggio:



> The Times 03/Jan/2009 Chancellor on brink of second bailout for banks

Questo messaggio, presente nel blocco Genesis (il primo blocco di Bitcoin) è in realtà codificato in esadecimale nel `scriptSig` della transazione coinbase:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Il periodo di maturità


Una volta che il blocco è stato estratto e distribuito, la transazione di coinbase appare sulla blockchain come qualsiasi altra transazione. Crea UTXO per il miner vincitore, consentendogli di riscuotere la sua ricompensa. Tuttavia, questi UTXO non sono immediatamente spendibili: sono soggetti a un [periodo di maturità](https://planb.academy/resources/glossary/maturity-period). Questa scadenza è fissata a 100 blocchi dopo il blocco contenente il coinbase. In concreto, la transazione coinbase deve quindi totalizzare 101 conferme perché i suoi output diventino spendibili dal miner vincitore.


![Image](assets/fr/040.webp)


Lo scopo di questa regola è limitare l'impatto delle riorganizzazioni della catena sull'economia. Come abbiamo visto nei capitoli precedenti, può accadere che alla stessa altezza due blocchi validi distinti vengano trovati quasi contemporaneamente da miner diversi. Per un breve momento, la rete può dividersi: alcuni nodi ricevono per primi il blocco A, mentre altri vedono per primi il blocco B. Poi, nel corso dei blocchi successivi, uno dei due rami accumula più lavoro e diventa il ramo di riferimento. L'altro ramo viene abbandonato e i suoi blocchi diventano obsoleti. Le transazioni che conteneva possono quindi, in teoria, tornare ai mempool in attesa di conferma.



In pratica, questo accade raramente, perché il mercato delle commissioni spesso fa sì che quasi le stesse transazioni appaiano in due blocchi concorrenti alla stessa altezza. Questo è uno dei motivi per cui una transazione Bitcoin è comunemente considerata immutabile dopo sei conferme: le riorganizzazioni di più di sei blocchi sono così improbabili da poter essere ragionevolmente considerate impossibili.



![Image](assets/fr/041.webp)



Il problema di queste riorganizzazioni nel caso della transazione di coinbase è che non si tratta di una transazione ordinaria. Introduce in circolazione bitcoin nuovi di zecca. Se la ricompensa del blocco potesse essere spesa immediatamente, si potrebbe creare una situazione problematica a cascata:




- un miner spende bitcoin da un coinbase,
- questi bitcoin circolano nell'economia,
- poi il blocco originale è stato definitivamente abbandonato durante una riorganizzazione.



I bitcoin in circolazione non sarebbero mai esistiti nella catena finale e una serie di transazioni valide al momento dell'emissione diventerebbero non valide a posteriori.



Il periodo di maturità impone un lasso di tempo abbastanza lungo da rendere questo scenario irrealistico. Una riorganizzazione di 101 blocchi è considerata, in pratica, impossibile (anche se rimane una probabilità infinitesimale). Non sappiamo esattamente perché Satoshi abbia scelto un valore così alto per la maturità, ma è probabile che sia stato scelto in modo che il meccanismo rimanga funzionale, anche in caso di gravi malfunzionamenti della rete.



Questa regola impedisce che la moneta di nuova creazione, che ha ricevuto una ricompensa in blocco, inizi a circolare prima che il blocco che l'ha creata sia stato sepolto in modo sicuro sotto una grande quantità di lavoro accumulato.



---

Siamo giunti alla fine della spiegazione del funzionamento del Bitcoin mining. Ora dovreste avere un quadro chiaro dei meccanismi di base coinvolti.



Nell'ultima parte del corso, torneremo ad aspetti più concreti, per mostrarvi come il Bitcoin mining si concretizza nel mondo reale: la sua industrializzazione, le macchine utilizzate, il raggruppamento dei giocatori e così via. L'obiettivo sarà quello di fornire una visione complessiva del Bitcoin mining, sia dal punto di vista teorico e protocollare che abbiamo appena visto, sia dal punto di vista pratico e operativo.



# Il settore Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## L'evoluzione delle macchine mining


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



Agli inizi di Bitcoin, il mining non era un'attività industriale. Faceva parte del software di Bitcoin, lanciato su un personal computer, spesso per curiosità, a volte per supportare la rete e, in secondo luogo, per ottenere bitcoin che all'epoca non avevano praticamente alcun valore di mercato.



Nel corso degli anni, questa attività ha subito una trasformazione: le macchine sono cambiate, la difficoltà è esplosa e il mining è diventato un'industria a sé stante. Vediamo gli aspetti operativi del Bitcoin mining.



### Per iniziare: mining con una CPU



Nel 2009 e nei primi anni, il mining veniva eseguito principalmente utilizzando la CPU di un computer convenzionale. Bitcoin era allora un semplice software che fungeva da wallet, da nodo e da miner. Il semplice lancio del software di Satoshi Nakamoto sul proprio computer era sufficiente per partecipare al processo mining e, in molti casi, per trovare blocchi.



Una CPU può fare tutto, ma non è ottimizzata per nulla. Esegue istruzioni molto generiche, con una logica complessa. Per un compito come l'hashing ripetitivo delle intestazioni dei blocchi, non è lo strumento ideale, ma all'avvio della rete, la difficoltà è così bassa che è più che sufficiente per trovare i blocchi.



Questo periodo è importante perché ci ricorda un punto fondamentale: La proof of work non dipende da una particolare categoria di apparecchiature. Ciò che conta è la capacità di calcolare gli hash più velocemente degli altri, a un determinato costo. Non appena compare un vantaggio tecnico, questo si trasforma automaticamente in un vantaggio economico. Ma in termini assoluti, oggi è ancora possibile tentare di trovare blocchi Bitcoin utilizzando una CPU convenzionale. Questo è l'approccio adottato dal progetto NerdMiner, ad esempio. Le possibilità di trovare un blocco sono praticamente nulle, ma c'è comunque una probabilità infinitesimale.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Passaggio alle GPU



Ben presto i miner si resero conto che il collo di bottiglia non era la potenza, ma la capacità di eseguire un numero enorme di operazioni simili in parallelo. Questo era esattamente ciò che potevano fare le unità di elaborazione grafica (GPU). In origine, le GPU erano state progettate per eseguire le stesse operazioni su grandi quantità di dati. Questa architettura si adattava perfettamente a un compito come l'hashing ripetuto: invece di avere pochi core altamente versatili, si disponeva di centinaia, poi migliaia di unità in grado di eseguire le stesse istruzioni simultaneamente.



A parità di consumo energetico, una GPU può produrre molti più hash al secondo di una CPU. Allo stesso tempo, il bitcoin aveva un tasso di cambio rispetto al dollaro, il suo valore stava aumentando e stavano comparendo piattaforme di scambio. Da quel momento in poi, la natura di mining iniziò a cambiare. Non si trattava più solo di partecipare, ma di fare soldi. Apparvero configurazioni dedicate: macchine costruite attorno a diverse schede grafiche, a volte senza schermo, con un sistema minimale e software specializzato, il cui unico scopo era il mining.



È stato a questo punto che la difficoltà del mining ha cominciato a esplodere. Tra la metà del 2010 e la metà del 2011 è addirittura aumentata di 1.000 volte. Meccanicamente, inizia la specializzazione, proprio come le prime forme di industrializzazione, e gli utenti comuni - che si accontentano di eseguire il software Bitcoin sui loro personal computer - hanno ora solo una piccolissima possibilità di trovare un blocco valido.



![Image](assets/fr/044.webp)



*Fonte: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Tra l'era delle GPU e quella moderna del [ASIC](https://planb.academy/resources/glossary/asic), c'è stata una fase intermedia: l'uso degli FPGA. Un FPGA è un componente riprogrammabile: può essere configurato per implementare direttamente un circuito logico dedicato a un particolare calcolo, in questo caso `SHA256d`. L'idea era quella di allontanarsi ancora di più dall'hardware general-purpose (CPU/GPU) per guadagnare in efficienza energetica. Ma presto i miglioramenti apportati virtualmente sulle FPGA sarebbero stati applicati fisicamente ai chip stessi: ecco l'arrivo del ASIC.



### L'arrivo del ASIC



La fase finale della specializzazione dell'hardware del mining fu la comparsa dei ASIC (*circuiti integrati specifici per le applicazioni*). Un ASIC è un chip progettato per un singolo compito. Nel caso del Bitcoin mining, questo compito è proprio l'esecuzione del `SHA256d` alla massima velocità e con un'efficienza energetica ottimale. A differenza di una GPU, un ASIC non viene utilizzato per eseguire giochi, rendering 3D o AI. Serve per l'hashing e basta.



![Image](assets/fr/045.webp)



*ASIC S21 XP Prodotto da Bitmain*



Questa specializzazione ha due conseguenze principali:




- Il primo è un salto di qualità in termini di prestazioni ed efficienza. Per dispositivi di pari generazione, un ASIC produce un numero di hash al secondo di gran lunga superiore a quello di una GPU, pur consumando meno energia. Il Mining con GPU è diventato rapidamente non competitivo: anche se funzionava tecnicamente, il costo dell'elettricità superava di gran lunga i ricavi previsti nella maggior parte dei contesti;
- Il secondo è un cambiamento di modello: gli investimenti si sono spostati principalmente su hardware di livello industriale. Il Mining comporta ora l'acquisto di macchine progettate per questo scopo, la loro alimentazione continua, il loro raffreddamento, la loro manutenzione e l'assorbimento della loro obsolescenza. Perché un ASIC non è economicamente eterno: quando una nuova generazione più efficiente arriva sul mercato, le vecchie macchine diventano progressivamente meno redditizie, anche se rimangono funzionanti.



Da quel momento in poi, non si tratta più di un semplice hobby. Stiamo parlando di un settore in cui la competitività dipende da un'equazione:




- costo dell'elettricità;
- costo delle attrezzature e dell'ammortamento;
- capacità di raffreddare e operare su larga scala;
- disponibilità e affidabilità della macchina;
- velocità delle comunicazioni;
- ecc.



### Mining farm



Una macchina isolata può essere utilizzata come miniera, ma raggruppando centinaia, poi migliaia di ASIC in un'unica sede, possiamo condividere i costi fissi, ottimizzare la logistica e avvicinarci a un modello di centro dati specializzato.



Una [fattoria mining](https://planb.academy/resources/glossary/mining-farm), nella sua forma più semplice, è un edificio (o un insieme di container) pieno di ASIC che funzionano 24 ore su 24, 7 giorni su 7. La sfida è ora quella di mantenere condizioni operative stabili:




- fornire grandi quantità di energia elettrica stabile e a basso costo;
- gestire il calore per evitare il throttling, poiché la densità di energia è notevole;
- filtrare la polvere, controllare l'umidità, pulire;
- monitoraggio in tempo reale delle prestazioni della macchina (temperature, errori hardware, cadute hashrate, ecc.).



![Image](assets/fr/043.webp)



*Uno dei sette edifici dedicati a Bitcoin mining presso il sito Rockdale di Riot Platforms, vicino ad Austin, Texas. Questo è specificamente dedicato all'immersione mining*



Il Mining è ora guidato da operatori industriali, alcuni dei quali quotati in borsa, che stanno costruendo e gestendo farm su larga scala. Tra questi, MARA Holdings (Nasdaq: `MARA`) e Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Anche senza entrare nei dettagli dei modelli di redditività, è importante capire perché il mining ha assunto questa forma. La Proof-of-work è un meccanismo competitivo: la probabilità di trovare un blocco, e quindi di guadagnare, è proporzionale alla quota di hashrate che si impiega. Di conseguenza, c'è una pressione costante per aumentare la potenza di calcolo, ridurre il costo per unità di calcolo e limitare le perdite. Di conseguenza, gli ambienti che offrono elettricità più economica, un clima favorevole al raffreddamento o un'infrastruttura energetica abbondante diventano naturalmente più attraenti.



Il Mining Bitcoin si è quindi evoluto da un'attività accessibile a chiunque agli inizi, a un'attività dominata da attrezzature specializzate e operazioni professionali. Questo non cambia le regole del protocollo. In teoria, chiunque può estrarre con qualsiasi macchina. Ma in pratica, il livello di difficoltà e di efficienza del ASIC ha reso il mining domestico largamente non competitivo nella maggior parte dei contesti.



Naturalmente, ci sono ancora situazioni in cui il mining domestico può essere interessante, ad esempio se si beneficia di un'elettricità molto economica o se si utilizza il calore generato dal miner per riscaldare la casa in inverno. Ma in ogni caso, dovrete comunque acquistare una macchina dotata di chip ASIC. Inoltre, poiché la vostra potenza mining rimarrà estremamente ridotta rispetto alla rete Bitcoin, dovrete trovare un modo per ridurre la varianza delle vostre entrate: è proprio questo il ruolo delle mining pool, di cui parleremo nel prossimo capitolo.



Se desiderate esplorare soluzioni domestiche mining con recupero di calore, abbiamo tutorial su vari strumenti, sia pronti all'uso che fai da te:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Raggruppamento in mining pool


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Il Bitcoin comporta costi continui e inevitabili, primo fra tutti il consumo di energia della macchina. Queste spese sono sostenute indipendentemente dai risultati, anche se i ricavi del mining sono, per loro stessa natura, rari e casuali. La scoperta di un blocco dipende esclusivamente dalla quota di hashrate del miner, il che rende i guadagni tanto più imprevedibili quanto più piccola è tale quota. È proprio questo problema pratico che ha portato rapidamente alla diffusione delle [mining pool](https://planb.academy/resources/glossary/pool-mining). In questo capitolo finale del corso MIN 101, offro un'introduzione ai principi e al funzionamento delle mining pool in Bitcoin.



### Cos'è una mining pool?



Un mining pool è un'organizzazione (spesso un servizio online) che aggrega la potenza di calcolo di molti miner indipendenti, al fine di aumentare la frequenza con cui il gruppo trova i blocchi. Quando il pool trova un blocco, la ricompensa del blocco viene ridistribuita tra i partecipanti in base alle regole interne del pool (che saranno trattate nel corso MIN 201, poiché sono troppo complesse per MIN 101).



I partecipanti a una mining pool sono spesso chiamati "[hasher](https://planb.academy/resources/glossary/hasher)", piuttosto che "miner", poiché non svolgono più tutto il lavoro mining, ma si limitano a eseguire l'hash dei dati trasmessi loro dal pool.



Attenzione a non confondere la mining pool con la farm mining. Si tratta di due concetti diversi. Come abbiamo visto nel capitolo precedente, una farm è un sito fisico in cui un'unica entità gestisce numerose macchine mining. Un pool, invece, è soprattutto un raggruppamento virtuale: migliaia di macchine, spesso geograficamente disperse, lavorano sotto un coordinamento comune. Tuttavia, una farm può, e spesso lo fa, partecipare a un pool.



![Image](assets/fr/048.webp)



### Riduzione della varianza del reddito



Allora perché unirsi a un pool? Semplicemente perché il risultato dell'attività mining è probabilistico: per ogni tentativo di hash, c'è una piccolissima possibilità di raggiungere l'obiettivo di difficoltà e quindi di produrre un blocco valido.



A lungo termine, il vostro guadagno medio dovrebbe essere proporzionale alla vostra quota del hashrate complessivo. Questo principio deriva direttamente dalle leggi della probabilità: ogni calcolo dell'hash costituisce un'estrazione casuale indipendente e, per la legge dei grandi numeri, la frequenza con cui scoprite i blocchi converge matematicamente verso la vostra frazione del hashrate totale della rete. Nel breve e medio termine, tuttavia, i guadagni effettivi possono essere estremamente irregolari. Questa discrepanza tra la media teorica e la realtà casuale è chiamata in matematica **varianza**.



Ecco un semplice esempio per illustrare il principio:




- La rete Bitcoin produce in media 144 blocchi al giorno (circa un blocco ogni 10 minuti);
- Se si dispone dello `0,0001 %` del totale di hashrate, l'aspettativa è di `144 × 0,000001`, ovvero `0,000144` blocchi/giorno;
- In altre parole, si dovrebbe trovare un blocco in media ogni `1 / 0,000144` giorni, cioè ogni 6.944 giorni, o circa 19 anni.



Ma questo valore corrisponde solo a un'aspettativa matematica: la distribuzione dei tempi di scoperta segue una legge casuale, quindi è perfettamente possibile, in pratica, non scoprire mai un singolo blocco, anche su un periodo molto lungo. Si può essere sfortunati e non trovare nulla per un periodo molto lungo, pur pagando i costi ricorrenti (elettricità, manutenzione, ammortamento delle apparecchiature...).



Il mining pool cambia la natura di questo problema: combinando i hashrate, il pool trova blocchi più spesso. Ogni partecipante accetta quindi di ricevere solo una frazione di ogni blocco trovato, ma molto più frequentemente. Si tratta di una trasformazione da un reddito altamente volatile e molto distanziato a uno più regolare, al costo di condividere le ricompense e di pagare le commissioni di servizio.



### Perché la varianza diminuisce quando si raggruppa?



Maggiore è la potenza di calcolo, maggiore è la frequenza prevista di blocchi trovati. Inoltre, più gli eventi sono frequenti, più i risultati osservati si avvicinano alla media statistica in un determinato periodo.



Da solo, un miner su piccola scala può rimanere per anni senza un singolo blocco, poi ottenere una grossa vincita un giorno, poi niente. In un pool, la stessa realtà probabilistica si applica ancora, ma è attenuata su scala collettiva: il pool trova blocchi più spesso e la ridistribuzione converte questi eventi in pagamenti più regolari per ogni partecipante. **Il mining pool vende quindi prevedibilità sull'attività mining**.



### Punti di riferimento storici



Come abbiamo visto nel capitolo precedente, all'inizio il mining poteva essere eseguito in solitaria con un computer convenzionale, poiché la difficoltà era molto bassa. Ma con l'esplosione del hashrate globale (GPU, poi ASIC), il mining in solitaria è diventato una scommessa che richiede molto tempo per la maggior parte dei partecipanti.



I primi pool sono stati creati proprio in risposta a questa nuova realtà. Braiins Pool (ex Slush Pool / Bitcoin.cz) è il primo pool Bitcoin mining: ha estratto il suo primo blocco il 16 dicembre 2010. Il successo di questo primo mining pool è stato rapido, poiché in pochi giorni ha catturato quasi il 3,5% del hashrate globale.



![Image](assets/fr/047.webp)



Dal punto di vista tecnico, i pool sono stati strutturati attorno a protocolli di comunicazione specializzati tra il pool e i miner (ad esempio [Stratum](https://planb.academy/resources/glossary/stratum), poi Stratum V2), al fine di orchestrare in modo efficiente il lavoro distribuito. Approfondiremo questi concetti nel nostro corso di formazione MIN 201.



### La situazione moderna



Al momento in cui scriviamo (inizio 2026), l'hashrate globale di Bitcoin è a un ordine di grandezza di zetta-hash al secondo (= 1.000 EH/s = 1.000.000.000.000.000 hash al secondo), e quasi tutti i blocchi trovati provengono da mining pool .



Ecco una classifica, ad oggi, dei principali mining pool e delle rispettive quote di hashrate. È probabile che questa classifica cambi nel momento in cui leggerete questo corso. Per dati aggiornati, visitare [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Fonte [mempool.space](https://mempool.space/graphs/mining/pools), dati di un mese, dal 16 dicembre 2025 al 16 gennaio 2026.*



In un corso più avanzato, approfondiremo il funzionamento interno dei pool (azioni, protocolli di rete, metodi di pagamento...), perché è qui che entrano in gioco i dettagli che determinano sia la redditività del miner che le potenziali implicazioni per Bitcoin.



---

Siamo giunti alla fine della MIN 101. Grazie per averlo seguito fino alla fine. Se volete valutare le competenze acquisite durante il corso, nella prossima sezione vi aspetta un esame finale.



Con le conoscenze di base appena acquisite, potete ora seguire corsi più avanzati sul mining sul Plan ₿ Academy, sia teorici, come questo, sia più pratici, in modo che anche voi possiate iniziare a partecipare al Bitcoin mining!



# Parte finale


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Recensioni e valutazioni


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Esame finale


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusione


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>