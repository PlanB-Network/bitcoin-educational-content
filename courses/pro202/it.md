---
name: Programmare Bitcoin
goal: Costruire una libreria Bitcoin completa da zero e comprendere le basi crittografiche di Bitcoin
objectives: 

 - Implementare l'aritmetica dei campi finiti e le operazioni sulle curve ellittiche in Python
 - Costruire e analizzare le transazioni Bitcoin in modo programmatico
 - Creare indirizzi di testnet e trasmettere le transazioni in rete
 - Padroneggiare le basi matematiche del modello di sicurezza Bitcoin

---
# Un viaggio negli script e nei programmi di Bitcoin


Questo corso intensivo di due giorni, tenuto da Jimmy Song, approfondisce le basi tecniche di Bitcoin costruendo una libreria Bitcoin completa da zero. Partendo dalla matematica essenziale dei campi finiti e delle curve ellittiche, si passerà all'analisi delle transazioni, all'esecuzione degli script e alla comunicazione di rete. Attraverso esercizi pratici di codifica in Jupyter notebook, creerete il vostro indirizzo di rete di prova, costruirete transazioni manualmente e le trasmetterete direttamente alla rete, il tutto acquisendo una profonda comprensione dei principi crittografici che rendono Bitcoin sicuro e privo di fiducia.


Godetevi il viaggio!

Nota: I video di questo corso sono disponibili solo in inglese.

+++

# Introduzione


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Panoramica del corso


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Benvenuti al corso PRO 202 _**Programmazione di Bitcoin**_, un viaggio intensivo che vi porterà dall'aritmetica dei campi finiti fino alla costruzione e alla trasmissione di transazioni reali su Bitcoin Testnet.


In questo corso si costruirà progressivamente una libreria Bitcoin in Python, acquisendo al contempo le basi crittografiche, protocollari e software necessarie per ragionare in modo preciso sulla sicurezza e sul funzionamento interno di Bitcoin. L'approccio di PRO 202 è completamente pratico: ogni concetto viene immediatamente implementato in quaderni Jupyter, assicurando che teoria e codice si rafforzino a vicenda.


### Concetti matematici essenziali per Bitcoin


Questa prima sezione stabilisce le basi matematiche indispensabili. Verranno implementate l'aritmetica dei campi finiti e le operazioni sulle curve ellittiche (legge dei gruppi, addizione, raddoppio, moltiplicazione scalare...) - i prerequisiti per ECDSA. L'obiettivo è duplice: comprendere la struttura algebrica che rende possibili le firme crittografiche e costruire strumenti Python affidabili per manipolarle.


Verranno quindi formalizzati i componenti di ECDSA: generazione della chiave, formattazione dei punti, hashing, creazione della firma e verifica. Questa sezione collega direttamente la teoria alla pratica, sottolineando i dettagli dell'implementazione e la robustezza del modello di sicurezza sottostante.


### Funzionamento interno della transazione Bitcoin


Nella seconda sezione si analizzerà la struttura di una transazione Bitcoin: UTXO, ingressi/uscite, sequenze, script, codifiche e altro ancora. Scriverete codice per costruire, firmare e verificare le transazioni, acquisendo una comprensione precisa di ciò che viene impegnato dall'hash e perché.


Successivamente, implementerete un esecutore _Script_ minimo, esaminerete gli opcode chiave e convaliderete i percorsi di spesa. L'obiettivo è quello di rendervi capaci di verificare il comportamento delle transazioni, diagnosticare i fallimenti della convalida e ragionare sulla sicurezza delle politiche di spesa.


### Funzionamento interno della rete Bitcoin


Nella terza sezione, collocherete le transazioni all'interno del sistema più ampio: la struttura dei blocchi, le intestazioni, la difficoltà e il meccanismo Proof-of-Work. Si tratteranno i messaggi di protocollo, le intestazioni dei blocchi e gli alberi di Merkle.


Infine, si studierà la comunicazione tra nodi peer-to-peer, l'ottimizzazione dei messaggi e l'introduzione di SegWit.


Come in ogni corso sul Plan ₿ Academy, la sezione finale comprende una valutazione per consolidare la comprensione. Siete pronti a scoprire i meccanismi interni di Bitcoin e a scrivere il codice che lo alimenta? Cominciamo!










# Concetti matematici essenziali per Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematica per l'implementazione di Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Fondamenti di programmazione: Strutture matematiche di base


Questo corso condensa la matematica essenziale alla base dei sistemi crittografici di Bitcoin in un flusso di lavoro estremamente pratico. I concetti vengono spiegati, dimostrati con esempi e quindi implementati in Jupyter Notebook. L'idea guida è semplice: si capisce veramente una primitiva crittografica solo dopo averla codificata. Nell'arco dei due giorni di corso, gli studenti utilizzano gli indirizzi della generate testnet, costruiscono e trasmettono [transazioni](https://planb.academy/resources/glossary/transaction-tx) e infine interagiscono con la rete senza block explorer. Tutto questo richiede una solida base di campi finiti e curve ellittiche.


### Campi finiti: Il motore aritmetico della crittografia


Un campo finito F(p) è un sistema aritmetico definito da un numero primo p, contenente gli elementi da 0 a p-1. I campi primi garantiscono che ogni elemento non nullo abbia un inverso e che tutte le operazioni rimangano all'interno del campo. L'aritmetica si basa sull'uso del modulo p per l'addizione, la sottrazione e la moltiplicazione. Python `pow(base, exp, mod)` permette un'efficiente esponenziazione modulare, cruciale per i grandi esponenti usati nelle operazioni di crittografia.


#### Comportamento moltiplicativo

La moltiplicazione di qualsiasi elemento non nullo k per tutti gli elementi di un campo primo produce una permutazione del campo. Questa proprietà garantisce l'uniformità e previene le debolezze strutturali, rendendo i campi primi ideali per la generazione sicura di chiavi e [firme digitali](https://planb.academy/resources/glossary/digital-signature).


#### Divisione e Piccolo Teorema di Fermat

La divisione è implementata tramite inversioni moltiplicative. Il Piccolo Teorema di Fermat afferma che

n^(p-1) ≡ 1 (mod p),

quindi l'inverso è n^(p-2). Python lo supporta direttamente con `pow(n, -1, p)`. Queste operazioni compaiono costantemente nelle routine crittografiche di [ECDSA](https://planb.academy/resources/glossary/ecdsa) e Bitcoin.


### Curve ellittiche: Strutture non lineari per la sicurezza delle chiavi pubbliche


Le curve ellittiche seguono l'equazione y² = x³ + ax + b. Bitcoin utilizza secp256k1, definita come y² = x³ + 7 su un campo finito. I punti di una curva ellittica formano un gruppo matematico sotto l'aggiunta di punti. Una retta tracciata attraverso due punti P e Q interseca la curva in un terzo punto R; riflettendo R sull'asse x si ottiene P + Q. Questo sistema è associativo e comprende un elemento di identità: il punto all'infinito.


Il raddoppio di un punto utilizza una retta tangente invece di una retta secante, con pendenza derivata dalla derivata della curva. Sebbene queste formule coinvolgano il calcolo sui numeri reali, diventano completamente discrete ed esatte quando la curva è definita su un campo finito, il contesto utilizzato in Bitcoin.


### Dalla matematica alla crittografia Bitcoin


I campi finiti forniscono un'aritmetica deterministica e invertibile; le curve ellittiche forniscono una struttura non lineare in cui il calcolo di k-P è facile ma l'inversione è computazionalmente impossibile. Combinando entrambi si ottengono le basi per le chiavi pubbliche/private di Bitcoin, le firme ECDSA e la sicurezza delle transazioni. La comprensione di questi fondamenti prepara gli studenti a implementare chiavi, transazioni e firme direttamente, senza astrazioni o strumenti esterni.


## Crittografia a curva ellittica

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Questo capitolo introduce le curve ellittiche definite su campi finiti e spiega perché costituiscono la spina dorsale matematica della [crittografia](https://planb.academy/resources/glossary/cryptography) di Bitcoin. Mentre le curve ellittiche sui numeri reali appaiono lisce e continue, l'applicazione delle stesse equazioni su un campo finito crea un insieme discreto e sparso di punti. Nonostante la differenza visiva, tutte le formule di addizione dei punti, le pendenze e le regole algebriche si comportano esattamente allo stesso modo, solo l'aritmetica cambia in aritmetica modulare. Bitcoin utilizza la curva y² = x³ + 7 (secp256k1), che preserva la simmetria e il comportamento non lineare essenziale per la sicurezza crittografica.


### Verifica dei punti e implementazione in campo finito


Un punto giace su una curva ellittica a campo finito se le sue coordinate soddisfano l'equazione della curva con modulo p. Per verificare un punto come (73,128) su F₁₃₇ è necessario controllare che y² mod p sia uguale a x³ + 7 mod p. L'implementazione nel codice comporta la creazione di classi per gli elementi del campo finito e i punti della curva. L'overloading degli operatori assicura che tutte le operazioni aritmetiche - addizione, moltiplicazione, esponenziazione, divisione - siano eseguite automaticamente modulo p. Una volta che queste astrazioni esistono, le operazioni crittografiche più avanzate diventano semplici da scrivere e su cui ragionare.


#### Proprietà del gruppo e aggiunta di punti

I punti delle curve ellittiche formano un gruppo matematico sotto forma di addizione. Il gruppo soddisfa le proprietà di chiusura, associatività, identità (il punto all'infinito) e inversione (riflessione sull'asse x). Le costruzioni geometriche confermano queste proprietà, rendendo ben definita la moltiplicazione scalare (P aggiunto a se stesso ripetutamente). Queste regole di gruppo consentono la crittografia a curve ellittiche e assicurano un comportamento coerente e prevedibile in caso di operazioni ripetute sui punti.


### Gruppi ciclici e problema del logaritmo discreto


La scelta di un punto generatore G su una curva ci permette di generate un gruppo ciclico: G, 2G, 3G, ..., nG = 0. I punti appaiono non lineari e imprevedibili, anche se generati in sequenza. Questa imprevedibilità crea le basi per il problema del logaritmo discreto: calcolare P = sG è facile, ma determinare s da P è computazionalmente impossibile per gruppi di grandi dimensioni. Questa funzione unidirezionale è ciò che rende sicura la crittografia a chiave pubblica. Gli scalari ([chiavi private](https://planb.academy/resources/glossary/private-key)) sono scritti in minuscolo; i punti ([chiavi pubbliche](https://planb.academy/resources/glossary/public-key)) in maiuscolo.


#### Moltiplicazione scalare efficiente

Per calcolare sG in modo efficiente, le implementazioni utilizzano l'algoritmo double-and-add: scansione della rappresentazione binaria dello scalare, raddoppio del punto a ogni passaggio e aggiunta di G solo quando il bit è 1. Questo riduce il calcolo da O(n) aggiunte a O(log n), consentendo operazioni crittografiche pratiche anche con scalari a 256 bit.


#### La curva secp256k1 nel Bitcoin


Bitcoin utilizza la curva secp256k1, definita da y² = x³ + 7 su un campo di primi dove p = 2²⁵⁶ - 2³² - 977. Il punto generatore G ha coordinate fisse scelte con una procedura deterministica NUMS ("nothing up my sleeve"). L'ordine del gruppo n è un grande primo vicino a 2²⁵⁶, che garantisce che ogni punto non nullo generi lo stesso gruppo. La dimensione di 2²⁵⁶ (~10⁷⁷) è astronomicamente grande e rende fisicamente impossibile il brute-forcing delle chiavi private. Anche un trilione di supercomputer in funzione per un trilione di anni non ridurrebbe significativamente lo spazio delle chiavi.


### Chiavi pubbliche, chiavi private e serializzazione SEC


La chiave privata è uno scalare casuale s; la chiave pubblica è P = sG. Poiché la soluzione del problema del log discreto è inaffrontabile, P può essere condivisa senza rivelare s. Le chiavi pubbliche devono essere serializzate per la trasmissione utilizzando il formato SEC. Il formato SEC non compresso utilizza 65 byte: prefisso 0x04 + coordinata x + coordinata y. Il formato compresso utilizza solo 33 byte: prefisso 0x02 o 0x03 (a seconda della parità di y) + coordinata x. Bitcoin utilizzava originariamente chiavi non compresse, ma ora preferisce quelle compresse per motivi di efficienza.


#### Bitcoin Address Creazione


Gli indirizzi Bitcoin sono hash delle chiavi pubbliche, non le chiavi grezze stesse. Per generate un indirizzo, si serializza la chiave pubblica in formato SEC, si calcola l'hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256) e poi RIPEMD-160), si aggiunge il prefisso di rete (0x00 per mainnet, 0x6F per testnet), si calcola un checksum usando un doppio SHA-256, si aggiungono i primi quattro byte del checksum e si codifica il risultato usando Base58. Questa codifica rimuove i caratteri ambigui e include la somma di controllo per evitare errori di trascrizione. La pipeline a più fasi nasconde la chiave pubblica finché non si verifica una spesa, aggiunge l'identificazione della rete e garantisce indirizzi leggibili dall'uomo e resistenti agli errori.


# Funzionamento interno della transazione Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Analisi delle transazioni e firme ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Capire ECDSA: la base della firma digitale di Bitcoin


Bitcoin si basa su ECDSA, uno schema di firma basato su curve ellittiche che offre una forte sicurezza con chiavi di dimensioni molto inferiori rispetto a RSA. La sua sicurezza deriva dal problema del logaritmo discreto della curva ellittica: dato P = eG, calcolare P è facile, ma ricavare e da P è computazionalmente impossibile. Questa asimmetria consente la crittografia a chiave pubblica e la sicurezza delle chiavi private.


#### Codifica DER delle firme ECDSA


Bitcoin codifica le firme ECDSA utilizzando il formato DER:


- 0x30 (marcatore di sequenza)
- lunghezza byte
- 0x02 + lunghezza + R byte
- 0x02 + lunghezza + S byte


Questo aggiunge overhead, espandendo una firma di 64 byte a ~71-72 byte. [Taproot](https://planb.academy/resources/glossary/taproot) elimina questa inefficienza adottando firme [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) a dimensione fissa.


### Impegni di firma e processo di firma


Le firme ECDSA si basano su un'equazione di impegno: UG + VP = KG. Il firmatario sceglie valori U e V non nulli e un [nonce](https://planb.academy/resources/glossary/nonce) casuale K, dimostrando di conoscere la chiave privata senza rivelarla. Il messaggio viene inserito in Z, viene generato un K casuale, R è la coordinata x di KG e S = (Z + RE)/K. La firma è la coppia (R, S). La sicurezza dipende in modo critico dall'utilizzo di un K unico e imprevedibile: se K viene riutilizzato o trapelato, la chiave privata è compromessa. Le moderne implementazioni utilizzano la generazione deterministica di K (RFC 6979) per evitare i fallimenti del RNG.


#### Verifica della firma

Dati Z, (R, S) e la chiave pubblica P, il verificatore calcola U = Z/S e V = R/S, quindi controlla se la coordinata x di UG + VP è uguale a R. Questo funziona perché l'algebra di verifica ricostruisce KG senza bisogno della chiave privata. La falsificazione delle firme richiederebbe la soluzione del problema del log discreto o la rottura della funzione hash.


#### Firme Schnorr e contesto storico


Le firme Schnorr sono matematicamente più pulite e supportano le funzioni di aggregazione, ma sono state brevettate al momento del lancio di Bitcoin. ECDSA offriva un'alternativa gratuita, ma con una maggiore complessità e firme più grandi. Una volta scaduti i brevetti, Bitcoin ha aggiunto le firme Schnorr tramite Taproot, fornendo firme fisse a 64 byte e migliorando la privacy. ECDSA rimane supportato per la compatibilità con il passato.



### Struttura della transazione e ingressi/uscite


Una transazione Bitcoin consiste in:


- versione (4 byte, little-endian)
- elenco degli ingressi
- elenco di output
- locktime (4 byte)


Gli ingressi fanno riferimento agli [UTXO](https://planb.academy/resources/glossary/utxo) precedenti tramite l'hash della transazione e l'indice di output, e includono uno [script](https://planb.academy/resources/glossary/script) di sblocco (scriptSig) e un numero di sequenza utilizzato per i timelock o il RBF. Le uscite specificano l'importo (8 byte) e lo script di chiusura (scriptPubKey), definendo le condizioni di spesa. Gli indirizzi Bitcoin sono rappresentazioni di questi script.


#### Il modello UTXO

Bitcoin tiene traccia delle uscite non spese piuttosto che dei saldi dei conti. Gli UTXO devono essere spesi interamente, mentre una spesa parziale è impossibile. Per spendere 1 BTC da un UTXO da 100 BTC, una transazione deve includere un output di cambio. Se si dimentica l'output di cambio, il resto diventa una commissione per il minatore.


#### Serializzazione e parsing delle transazioni


Le transazioni utilizzano un formato binario compatto. Dopo il campo della versione, una varint codifica il numero di ingressi. Gli ingressi includono:


- hash tx precedente (32 byte)
- indice di output (4 byte)
- scriptSig (varstr)
- sequenza (4 byte)


Gli output includono un importo di 8 byte e scriptPubKey (varstr). Il tempo di blocco controlla quando la transazione diventa valida. La serializzazione utilizza l'ordinamento little-endian per la maggior parte dei numeri interi. I parser consumano i byte in modo sequenziale e delegano a classi specializzate per gli input, gli output e gli script.


### Tariffe, cambiamenti e malleabilità


Le tariffe sono implicite:

quota = somma (valori di input) - somma (valori di output).

Qualsiasi valore non assegnato diventa il corrispettivo, rendendo essenziale la corretta costruzione dell'output di modifica. Prima del [SegWit](https://planb.academy/resources/glossary/segwit), le firme consentivano la malleabilità: modificando S in N-S si produceva una nuova transazione valida con un ID diverso. Bitcoin ora applica una regola di basso S e il SegWit isola le firme dal calcolo del txid, rendendo stabili gli ID e consentendo protocolli di secondo livello come [Lightning](https://planb.academy/resources/glossary/lightning-network).


## Bitcoin Convalida di script e transazioni

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script è un piccolo linguaggio per contratti intelligenti basato su stack che definisce come possono essere spese le coin. Ogni output porta con sé una scriptPubKey (script di blocco) e ogni input porta con sé una scriptSig (script di sblocco). Insieme formano un programma che deve essere valutato come "vero" affinché la spesa sia valida. Lo script non è intenzionalmente Turing-completo, in modo che tutti i percorsi di esecuzione siano prevedibili e facili da convalidare nella rete.


### Operazioni di script e modello di esecuzione


Uno script è una sequenza di elementi di dati e codici operativi. I dati (firme, chiavi pubbliche, hash) sono collocati nello stack, mentre gli opcode che iniziano con `OP_` trasformano lo stack. Dopo l'esecuzione, l'elemento superiore dello stack deve essere non nullo per avere successo. Esempi: `OP_DUP` duplica l'elemento superiore, `OP_HASH160` applica SHA256 e poi RIPEMD160, e `OP_CHECKSIG` verifica una firma rispetto al sighash della transazione e a una chiave pubblica, spingendo 1 se valida, 0 se non valida. Le regole di parsing distinguono tra dati grezzi (prefissati in base alla lunghezza) e codici operativi (cercati in base al valore del byte) e una piccola macchina virtuale li esegue in modo deterministico su ogni [nodo](https://planb.academy/resources/glossary/node).


### P2PK e P2PKH: modelli di pagamento fondamentali


Il primo schema, Pay-to-Public-Key (P2PK), aggancia le coin direttamente a una chiave pubblica completa: lo scriptPubKey è `<pubkey> OP_CHECKSIG`, e lo scriptSig è solo una firma. È semplice ma poco efficiente dal punto di vista dello spazio ed espone la chiave pubblica prima che le coin vengano spese.


#### P2PKH e indirizzi

Pay-to-Public-Key-Hash (P2PKH) migliora questo aspetto agganciandosi a un hash di 20 byte della chiave pubblica. Lo scriptPubKey è `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, e lo scriptSig fornisce `<firma> <pubkey>`. L'esecuzione verifica che la chiave pubblica fornita abbia l'hash del valore impegnato e quindi verifica la firma. Questo nasconde la chiave pubblica fino al momento della spesa, riduce le dimensioni e corrisponde al noto formato di indirizzo "1..." mainnet.


### Convalida delle transazioni e hashtag della firma


Un nodo che convalida una transazione deve garantire:

1) Ogni input fa riferimento a un'output esistente e non utilizzata.

2) Valore totale degli input ≥ valore totale degli output (la differenza è la tassa).

3) Ogni scriptSig sblocca correttamente la sua scriptPubKey di riferimento.


La verifica della firma richiede la costruzione del messaggio esatto che è stato firmato, chiamato sighash. Per ECDSA, la convalida svuota tutti gli scriptSig, sostituisce lo scriptSig dell'input corrente con la corrispondente scriptPubKey, aggiunge un tipo di hash a 4 byte (di solito `SIGHASH_ALL`) e fa un doppio hash del risultato. Il valore a 256 bit è quello utilizzato da `OP_CHECKSIG`. Tipi di hash alternativi (ad esempio, `SINGLE`, `NONE`, con o senza `ANYONECANPAY`) cambiano quali parti della transazione sono impegnate, consentendo casi d'uso di nicchia come il finanziamento collaborativo o transazioni parzialmente specificate, ma sono raramente utilizzati nella pratica.


#### Hashing quadratico e SegWit

Poiché ogni input in una transazione legacy richiede il proprio calcolo di sighash su una struttura che include tutti gli ingressi, il tempo di convalida può crescere quadraticamente con il numero di ingressi. In passato, le transazioni di grandi dimensioni con più ingressi causavano notevoli ritardi nella convalida. Il SegWit ha riprogettato il calcolo di sighash per mettere in cache le parti condivise e ridurre la complessità a un tempo lineare, migliorando la scalabilità e rendendo più difficili gli attacchi denial-of-service.


### Puzzle di script e lezioni di sicurezza


Gli script possono esprimere molto di più del semplice "una firma sblocca queste coin" I puzzle Script lo dimostrano codificando condizioni arbitrarie - problemi matematici, sfide di preimmagini hash o persino taglie di collisione - in cui chiunque fornisca i dati corretti può spendere le coin. Tuttavia, i risultati che si basano solo sui dati pubblici (senza firme) sono vulnerabili al front-running dei minatori: una volta che una soluzione valida appare nella [mempool](https://planb.academy/resources/glossary/mempool), qualsiasi [minatore](https://planb.academy/resources/glossary/miner) può copiarla e reindirizzare il pagamento a se stesso.


La lezione pratica è che i contratti del mondo reale includono quasi sempre controlli sulla firma, anche quando contengono logiche più complesse come multisig, timelock o hashlock. Le firme vincolano la soluzione a una parte specifica, preservando gli incentivi e impedendo ad altri di rubare il pagamento. La comprensione del modello di stack di Script, degli schemi standard e delle sottili insidie è essenziale per progettare smart contract Bitcoin sicuri e per ragionare sul modo in cui le transazioni vengono effettivamente convalidate sulla rete.


## Costruzione di transazioni e Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Edificio Bitcoin Transazioni e P2SH


La costruzione delle transazioni Bitcoin collega la conoscenza teorica del protocollo con l'implementazione pratica. Una transazione seleziona gli UTXO da spendere, costruisce gli output con script di blocco, crea firme per ogni input e serializza tutto nel formato esatto che i nodi si aspettano. Il processo richiede la comprensione della generazione di sighash, del comportamento degli script e della corretta gestione delle tasse e delle modifiche.


### Costruzione della transazione di base


Ogni input di transazione fa riferimento a un output precedente tramite txid e indice. Le uscite specificano gli importi in satoshi e gli script di chiusura. La differenza tra il totale degli ingressi e il totale delle uscite è la tariffa. Per firmare un input, viene serializzata una versione modificata della transazione, viene calcolato il suo sighash e la chiave privata lo firma. La firma risultante e la chiave pubblica formano lo ScriptSig. Una volta firmato ogni input, la transazione grezza può essere trasmessa alla rete.


### Transazioni con più firme


Il multisig nudo usa `OP_CHECKMULTISIG` per richiedere m-di-n firme. A causa di un bug iniziale, OP_CHECKMULTISIG consuma un elemento di stack in più, richiedendo un `OP_0` iniziale nello ScriptSig. Il multisig nudo è funzionale ma inefficiente: tutte le chiavi pubbliche appaiono on-chain, rendendo le ScriptPubKey grandi, costose e difficili da codificare come indirizzi. Queste limitazioni hanno motivato l'introduzione del pay-to-script-hash.


#### Architettura P2SH

P2SH nasconde gli script complessi dietro un HASH160 di 20 byte. La scriptPubKey è fissa: `OP_HASH160 <hash a 20 byte> OP_EQUAL`. Lo script redeem sottostante, contenente multisig, timelock o altre condizioni, viene rivelato ed eseguito solo quando viene speso. Il mittente vede solo l'hash, mentre il destinatario gestisce privatamente il redeem script. Questo design riduce le dimensioni del on-chain , migliora la privacy e consente di stipulare contratti complessi senza gravare sui mittenti.


### Spesa e attuazione del P2SH


Per spendere un output P2SH, lo ScriptSig deve includere i dati di sblocco necessari *oltre* al redeem script stesso. La convalida avviene in due fasi:

1) HASH160(redeem_script) deve corrispondere all'hash di scriptPubKey.

2) Dopo la verifica, lo script redeem viene eseguito con i dati forniti.


Quando si generano le firme per un input P2SH, il processo di sighash utilizza lo script redeem al posto dello scriptPubKey. Ciascun firmatario deve possedere lo script redeem completo per generare firme valide generate. Gli indirizzi P2SH utilizzano il byte di versione 0x05 su mainnet (indirizzi "3...") e 0xC4 su testnet (indirizzi "2...").


#### Considerazioni pratiche sulla sicurezza


Perdere uno script di riscatto significa perdere fondi: la spesa richiede sia le chiavi private che il redeem script stesso. I partecipanti a Multisig devono verificare che le loro chiavi pubbliche siano incluse correttamente prima di accettare depositi. P2SH supporta costruzioni avanzate come il multisig, il timelock e l'hashlock, ma gli errori nella logica degli script possono bloccare permanentemente i fondi, quindi è essenziale testare su testnet.


P2SH migliora la privacy nascondendo le condizioni di spesa fino alla prima spesa, ma una volta che il redeem script appare on-chain, diventa permanentemente visibile. Ciononostante, i vantaggi della riduzione delle dimensioni, della retrocompatibilità e del supporto di contratti flessibili hanno reso il P2SH una pietra miliare importante, influenzando gli aggiornamenti successivi come il SegWit e il Taproot.


# Funzionamento interno della rete Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blocchi Bitcoin e Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


I [blocchi](https://planb.academy/resources/glossary/block) Bitcoin raggruppano le transazioni e le proteggono con [proof of work](https://planb.academy/resources/glossary/proof-of-work). Ogni blocco comprende un'[intestazione](https://planb.academy/resources/glossary/block-header) di 80 byte e un elenco di transazioni. Nonostante il costo energetico elevato per la produzione di un blocco valido, la verifica di un blocco è economica: la memorizzazione di tutte le ~900k intestazioni richiede solo ~72 MB, consentendo anche ai piccoli dispositivi di verificare la catena proof of work in modo efficiente.


### Transazioni e premi in blocchi di Coinbase


Ogni blocco inizia esattamente con una [transazione Coinbase](https://planb.academy/resources/glossary/coinbase-transaction), l'unico modo in cui nuovi bitcoin entrano in circolazione. Ha un hash prev-tx azzerato e un indice di 0xffffffff, che lo identifica in modo univoco. La sovvenzione è partita da 50 BTC e si dimezza ogni 210.000 blocchi (50, 25, 12,5, 6,25, 3,125, ...). I minatori includono anche le commissioni di transazione. Poiché il nonce di 4 byte è troppo piccolo per i moderni ASIC, i minatori modificano i dati della transazione Coinbase per cambiare la radice [Merkle](https://planb.academy/resources/glossary/merkle-tree) e creare uno spazio di ricerca aggiuntivo. Il [BIP](https://planb.academy/resources/glossary/bip)34 richiede l'incorporazione dell'altezza del blocco nello scriptSig di Coinbase per garantire che ogni txid di Coinbase sia unico.


### Campi dell'intestazione del blocco e segnalazione Soft Fork


L'intestazione di 80 byte contiene:


- versione (4 byte)
- hash del blocco precedente (32 byte)
- Radice Merkle (32 byte)
- timestamp (4 byte)
- bit (obiettivo di [difficoltà](https://planb.academy/resources/glossary/difficulty), 4 byte)
- nonce (4 byte)


I numeri di versione si sono evoluti in un sistema di segnalazione a campi di bit tramite BIP9, consentendo ai minatori di coordinare la preparazione del [soft-fork](https://planb.academy/resources/glossary/soft-fork). Il timestamp è un valore temporale Unix a 32 bit e dovrà essere aggiornato intorno all'anno 2106.


#### Campo di bit e obiettivi

Il campo bit codifica l'obiettivo in forma compatta: obiettivo = coefficiente × 256^(esponente-3). Gli hash di blocco validi devono essere numericamente inferiori a questo obiettivo. Poiché gli hash sono interpretati come numeri interi little-endian, gli hash validi appaiono spesso con molti zeri di coda quando sono visualizzati in esadecimale.


### Difficoltà, convalida e aggiustamenti


La difficoltà è definita come lowest_target / current_target, che esprime quanto più difficile sia oggi mining rispetto alla difficoltà più facile possibile. La convalida richiede solo il confronto dell'hash dell'intestazione con l'obiettivo, estremamente economico rispetto a mining.


Ogni 2016 blocchi, Bitcoin regola la difficoltà per ottenere intervalli di blocco di ~10 minuti. L'aggiustamento confronta il tempo effettivo dei precedenti 2016 blocchi con le due settimane previste. I limiti limitano gli aggiustamenti a un fattore di quattro. I grandi eventi del mondo reale, come il bando del mining in Cina, hanno dimostrato la resilienza di questo meccanismo quando il tasso di hash è calato bruscamente e la difficoltà si è adattata al ribasso per compensare.


### Sovvenzione in blocco e supply totale


Il sussidio all'altezza h è calcolato come: sussidio = 5_000_000_000 >> (h // 210_000). Si ottiene così il programma di dimezzamento che converge verso un'offerta totale di ~21 milioni di BTC. La somma delle serie geometriche (50 + 25 + 12,5 + ...) × 210.000 spiega il limite massimo. I minatori possono richiedere meno della sovvenzione consentita, ma mai di più, altrimenti il blocco diventa non valido. Man mano che le sovvenzioni si riducono nel corso dei successivi dimezzamenti, le commissioni di transazione diventano una componente sempre più importante delle entrate dei minatori e della sicurezza della rete a lungo termine.


## Comunicazione di rete e alberi Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Architettura di rete Bitcoin


La rete [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) di Bitcoin funziona come un sistema di gossip decentralizzato in cui i nodi trasmettono transazioni e blocchi senza fidarsi l'uno dell'altro. I nuovi nodi si avviano contattando semi DNS codificati in modo rigido e gestiti dagli sviluppatori del nucleo. Questi semi DNS restituiscono gli IP dei peer attivi, consentendo ai nodi di scoprire la rete e di richiedere altri peer tramite getaddr. La rete non è intenzionalmente critica per il [consenso](https://planb.academy/resources/glossary/consensus), quindi le implementazioni possono essere diverse, purché le regole del consenso rimangano invariate.


### Struttura del messaggio e handshake


Tutti i messaggi Bitcoin P2P utilizzano una busta fissa: un valore magico di 4 byte (F9BEB4D9 per mainnet), un comando ASCII di 12 byte, una lunghezza del payload di 4 byte little-endian, un checksum di 4 byte (i primi 4 byte di [hash](https://planb.academy/resources/glossary/hash-function)256) e il payload. I comandi più comuni sono version, verack, inv, getdata, tx, block, getheaders, headers, ping e pong.


L'handshake inizia quando un nodo di connessione invia un messaggio di versione. Il destinatario risponde con verack e la propria versione. Una volta che entrambe le parti si sono scambiate questi due messaggi, la connessione è attiva e i nodi possono iniziare a trasmettere inventari e dati.


### Alberi e Merkle Root


Bitcoin memorizza una singola radice Merkle di 32 byte nell'intestazione di ogni blocco come impegno per tutte le transazioni del blocco. Le transazioni vengono sottoposte a hash (hash256), accoppiate, concatenate e sottoposte a hash ripetutamente finché non rimane un hash. Quando un livello ha un numero dispari, l'ultimo hash viene duplicato. Internamente, gli hash sono big-endian, mentre i dati serializzati dei blocchi sono little-endian, il che richiede l'inversione prima e dopo la costruzione dell'albero.


#### Prove di Merkle e SPV

Le prove Merkle consentono di verificare che una transazione sia inclusa in un blocco senza scaricare l'intero blocco. La prova consiste in hash fratelli lungo il percorso verso la radice. I client SPV leggeri memorizzano solo le intestazioni dei blocchi e richiedono queste prove ai [nodi completi](https://planb.academy/resources/glossary/full-node). Poiché un albero di Merkle cresce logaritmicamente, la prova dell'inclusione in un blocco con migliaia di transazioni richiede solo poche centinaia di byte.


Taproot estende questo concetto impegnando le condizioni di spesa in un albero di script Merklized (MAST), rivelando solo il ramo eseguito insieme a una prova Merkle. Questo migliora sia l'efficienza che la privacy.


### Operazioni di rete e sincronizzazione dei blocchi


I nodi utilizzano getdata per richiedere transazioni o blocchi, specificando un ID di tipo (1=tx, 2=blocco, 3=blocco filtrato, 4=blocco compatto) più un identificatore di 32 byte. Per la sincronizzazione a catena, i nodi inviano getheaders con un hash iniziale del blocco, ricevendo in risposta fino a 2000 header. Ogni intestazione restituita è di 80 byte, seguita da un conteggio di transazioni fittizie pari a zero.


La verifica completa dei blocchi ricevuti richiede due controlli:

1. L'hash del blocco deve essere inferiore all'obiettivo codificato nel campo dei bit.

2. La radice Merkle calcolata da tutte le transazioni (con una corretta gestione dell'endianness) deve corrispondere alla radice dell'intestazione.


Solo se entrambe le condizioni sono soddisfatte, un nodo accetta il blocco, riflettendo il principio di Bitcoin "non fidarti, verifica".


## Comunicazione avanzata dei nodi e testimonianza segregata

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Questa sessione unifica il networking avanzato P2P con Segregated Witness, mostrando come il moderno software Bitcoin interagisca direttamente con i nodi utilizzando strutture di transazione consapevoli del SegWit. Gli sviluppatori imparano a recuperare i blocchi, a scansionare le transazioni pertinenti e a costruire le transazioni utilizzando solo la comunicazione di rete grezza, senza bisogno di esploratori di blocchi.


### Recupero delle transazioni basato su blocchi e privacy


I [portafogli](https://planb.academy/resources/glossary/wallet) devono rilevare i pagamenti in arrivo scansionando i blocchi alla ricerca di uscite corrispondenti alla loro scriptPubKey. Il recupero di interi blocchi protegge la privacy meglio della richiesta di singole transazioni, che fa trapelare forti segnali sull'attività dell'utente. Anche le richieste di blocchi possono far trapelare informazioni su catene a basso volume, rendendo i filtri per blocchi compatti (BIP158) essenziali per i client leggeri che rispettano la privacy. I filtri possono produrre falsi positivi ma mai falsi negativi, consentendo ai clienti di scaricare solo blocchi potenzialmente rilevanti senza rivelare indirizzi specifici.


### Trustless Interazione di rete


Il flusso di lavoro `get_block` dimostra il corretto utilizzo della rete: inviare getdata, ricevere un blocco, quindi verificare in modo indipendente la sua radice Merkle e proof of work. Un blocco viene accettato solo se l'hash dell'intestazione ricevuta corrisponde all'hash richiesto e la sua radice Merkle calcolata corrisponde all'intestazione. In questo modo si può dire "non fidarsi, verificare", assicurando che anche i peer malintenzionati non possano ingannare i nodi nell'accettazione di dati alterati.


#### Recupero delle transazioni dai blocchi

Le transazioni di un blocco possono essere analizzate alla ricerca di scriptPubKey corrispondenti utilizzando una semplice iterazione. I portafogli di produzione eseguono questa operazione in continuazione all'arrivo di nuovi blocchi, dimostrando la proprietà degli output esclusivamente attraverso la convalida crittografica piuttosto che affidandosi ad API di terze parti.


### Obiettivi e progettazione di SegWit


Il testimone segregato (SegWit) ha risolto la malleabilità delle transazioni eliminando i dati della firma dal calcolo del txid. Questo ha permesso di creare catene di transazioni pre-firmate affidabili e di rendere pratico il Lightning Network. Il SegWit ha anche aumentato la capacità dei blocchi utilizzando il "peso del blocco": i vecchi nodi vedono ancora blocchi da ≤1 MB, mentre i nodi aggiornati convalidano fino a 4 MB compresi i dati del testimone. I programmi dei testimoni con versione (v0-v1 finora) creano un percorso di aggiornamento strutturato per i futuri tipi di script.


#### P2WPKH (nativo SegWit)


P2WPKH sostituisce la struttura legacy P2PKH con una scrittura a 22 byte: OP_0 + push20 + hash160(pubkey). La spesa sposta la firma e la pubkey in un campo testimone separato.


- Nodi pre-SegWit: vedere "anyone-can-spend", trattarlo come valido.
- Nodi post-SegWit: riconoscere OP_0 + hash a 20 byte e convalidare utilizzando i dati dei testimoni.


Questa separazione risolve la malleabilità e riduce le spese. Il testimone utilizza un conteggio di varint seguito dalla firma e dalla pubkey.


#### P2SH-P2WPKH (compatibile con SegWit)


Per permettere ai vecchi portafogli di inviare agli indirizzi SegWit, gli script P2WPKH possono essere avvolti in P2SH.


- scriptPubKey: standard P2SH hash160(redeemScript)
- scriptSig: il redeemScript (il programma P2WPKH)
- testimone: firma + chiave pubblica


Strati di convalida:

1. I nodi pre-BIP16 accettano il redeemScript come valido.

2. I nodi post-BIP16 lo valutano, lasciando OP_0 + hash sullo stack.

3. I nodi SegWit eseguono la convalida completa dei testimoni.


#### P2WSH per script complessi


P2WSH generalizza SegWit per script multisig e avanzati, impegnandosi a utilizzare SHA256(script) invece di hash160. Un tipico stack di 2 su 3 testimoni multisig:


- elemento vuoto (bug CHECKMULTISIG)
- sig1
- sig2
- script testimone (lo script multisig)


I nodi SegWit verificano che SHA256(witnessScript) corrisponda all'hash di scriptPubKey e quindi lo eseguono. L'uso di SHA256 e di un hash a 32 byte consente di distinguere P2WSH da P2WPKH e di rafforzare la sicurezza.


#### P2SH-P2WSH (massima compatibilità)


Anche gli script SegWit complessi possono essere confezionati in P2SH:


- scriptSig: redeemScript (OP_0 + hash a 32 byte)
- testimone: firme + testimoneScript


La convalida passa attraverso tre generazioni di regole esattamente come con P2SH-P2WPKH. Questo wrapper era essenziale per le prime implementazioni di Lightning che necessitavano di multisig senza malleabilità. Anche se oggi si preferisce il P2WSH nativo, la forma wrapper garantisce la compatibilità con i sistemi wallet più vecchi.


### L'impatto di SegWit


SegWit fornito:


- iD transazione stabile
- tariffe più basse grazie ai dati scontati dei testimoni
- maggiore produttività dei blocchi grazie al peso dei blocchi
- compatibilità con i vecchi nodi
- un percorso di aggiornamento pulito per il Taproot e le estensioni future


Insieme all'interazione di rete priva di fiducia, questi strumenti costituiscono la spina dorsale del moderno sviluppo Bitcoin.



# Sezione finale


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recensioni e valutazioni


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Esame finale


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusione



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>