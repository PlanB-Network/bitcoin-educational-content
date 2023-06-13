---
name: Introduzione alla crittografia
goal: Comprendere la creazione di un portafoglio Bitcoin dal punto di vista crittografico
objectives:
  - Demistificare la terminologia della crittografia legata ai Bitcoin.
  - Padroneggiare la creazione di un portafoglio Bitcoin.
  - Comprendere la struttura di un portafoglio Bitcoin.
---

# Un viaggio nel cuore della crittografia

Sei affascinato da Bitcoin? Ti chiedi come funziona un portafoglio Bitcoin? Preparati a intraprendere un viaggio affascinante nel cuore della crittografia! Loïc, il nostro esperto, ti guiderà attraverso i meandri della creazione di un portafoglio Bitcoin, svelando i misteri dietro i termini tecnici intimidatori come hash, derivazione delle chiavi e curve ellittiche. 

Questa formazione ti doterà non solo delle conoscenze per comprendere la struttura di un portafoglio Bitcoin, ma ti preparerà anche ad approfondire ulteriormente il mondo appassionante della crittografia. Quindi, sei pronto per intraprendere questo viaggio? Unisciti a noi e trasforma la tua curiosità in competenza!

+++

# Introduzione alla crittografia

![introduzione di Rogzy](https://youtu.be/ul8zU5QWIXg)

È con grande piacere che vi diamo il benvenuto al nuovo corso intitolato "Crypto 301: Introduzione alla crittografia e al portafoglio HD", orchestrato dall'esperto in materia, Loïc Morel. Questo corso ti farà immergere nel mondo affascinante della crittografia, questa disciplina fondamentale della matematica che garantisce la crittografia e la sicurezza dei tuoi dati. Nella nostra vita quotidiana e soprattutto nel campo dei Bitcoin, la crittografia svolge un ruolo fondamentale. I concetti ad essa legati, come le chiavi private, pubbliche, gli indirizzi, i percorsi di derivazione, il seme e l'entropia, sono al centro dell'uso e della creazione di un portafoglio Bitcoin. Attraverso questo corso, Loïc ti spiegherà in dettaglio come vengono create le chiavi private e come sono collegate agli indirizzi. Loïc dedicherà anche un'ora per spiegarti i dettagli matematici della curva ellittica, questa complessa curva matematica. Inoltre, capirai perché l'uso di HMAC SHA512 è importante per proteggere il tuo portafoglio e qual è la differenza tra il seme e la frase mnemonica.

L'obiettivo finale di questa formazione è quello di permettervi di comprendere tecnicamente i processi di creazione di un portafoglio HD e i metodi crittografici impiegati. Nel corso degli anni, i portafogli Bitcoin sono evoluti diventando più facili da usare, più sicuri e standardizzati grazie a specifici BIP. Loïc vi aiuterà a comprendere questi BIP per capire le scelte dei developer di Bitcoin e dei crittografi. Come tutti i corsi offerti dalla nostra università, questo è completamente gratuito e open source. Ci auguriamo di ricevere i vostri feedback alla fine di questo entusiasmante corso.

![intro par loïc](https://youtu.be/mwuxXLk4Kws)

Buongiorno a tutti, sono Loïc Morel, la vostra guida in questa esplorazione tecnica della crittografia utilizzata nei portafogli Bitcoin.

Il nostro viaggio inizia con una discesa negli abissi delle funzioni di hash crittografiche. Smontiamo insieme i meccanismi dell'indispensabile SHA256 ed esploriamo vari algoritmi dedicati alla derivazione.

Continueremo la nostra avventura decifrando il misterioso mondo delle firme digitali. Scoprirete come la magia delle curve ellittiche si applica a queste firme e faremo luce su come calcolare la chiave pubblica a partire dalla chiave privata. E naturalmente, affronteremo l'atto di firmare con la chiave privata.

Poi, risaliremo nel tempo per vedere l'evoluzione dei portafogli Bitcoin e ci avventureremo nei concetti di entropia e numeri casuali. Esamineremo la famosa frase mnemonica, aprendo una parentesi sulla passphrase. Avrete persino l'opportunità di vivere un'esperienza unica creando un seme da 128 lanci di dadi!

Con queste solide basi, saremo pronti per la parte cruciale: la creazione di un portafoglio Bitcoin. Dalla nascita del seme e della chiave master, passando allo studio delle chiavi estese, fino alla derivazione delle coppie di chiavi figlie, ogni passaggio sarà analizzato. Discuteremo anche la struttura del portafoglio e i percorsi di derivazione.

Per coronare il tutto, concluderemo il nostro percorso esaminando gli indirizzi Bitcoin. Spiegheremo come vengono creati e come svolgono un ruolo essenziale nel funzionamento dei portafogli Bitcoin.

Imbarcatevi con me in questo viaggio avvincente e preparatevi ad esplorare l'universo della crittografia come mai prima d'ora. Lasciate le vostre preconcetti alla porta e aprite la vostra mente a un nuovo modo di comprendere Bitcoin e la sua struttura fondamentale.

# Le funzioni di hash

## Introduzione alle funzioni di hash crittografiche relative a Bitcoin

![le funzioni di hash crittografiche](https://youtu.be/dvnGArYvVr8)
Benvenuti alla nostra sessione odierna dedicata all'immersione approfondita nel mondo crittografico delle funzioni di hash, una pietra angolare essenziale per la sicurezza del protocollo Bitcoin. Immaginate una funzione di hash come un robot decrittatore crittografico ultra efficiente che trasforma informazioni di qualsiasi dimensione in un'impronta digitale unica e di dimensioni fisse, chiamata "hash". Nel corso della nostra esplorazione, dipingeremo il profilo delle funzioni di hash crittografiche, mettendo in luce il loro utilizzo nel protocollo Bitcoin e definendo gli obiettivi specifici che queste funzioni crittografiche devono raggiungere.

Dipingere il profilo delle funzioni di hash crittografiche richiede la comprensione di due qualità essenziali: la loro irreversibilità e la loro resistenza alla falsificazione. Ogni funzione di hash crittografica è come un artista unico, che produce un "hash" distintivo per ogni input. Anche un pennello che devia leggermente altera considerevolmente il quadro finale, ovvero l'hash. Queste funzioni agiscono come sentinelle digitali, verificando l'integrità del software scaricato. Un'altra caratteristica cruciale che possiedono è la loro resistenza alle collisioni. Certamente, nell'universo dell'hash, le collisioni sono inevitabili, ma una eccellente funzione di hash crittografica le minimizza considerevolmente. È come se ogni hash fosse una casa in una città immensa; nonostante il numero enorme di case, una buona funzione di hash si assicura che ogni casa abbia un indirizzo unico.

Navighiamo ora sulle onde tumultuose delle funzioni di hash obsolete. SHA0, SHA1 e MD5 sono oggi considerate come gusci arrugginiti nell'oceano dell'hash crittografico. Sono spesso sconsigliate perché hanno perso la loro resistenza alle collisioni. Il principio delle caselle spiega perché, nonostante i nostri migliori sforzi, l'evitamento delle collisioni è impossibile a causa della limitazione della dimensione di output. È anche importante notare che la resistenza alla seconda preimmagine dipende dalla resistenza alle collisioni. Per essere veramente considerata sicura, una funzione di hash deve resistere alle collisioni, alla seconda preimmagine e alla preimmagine.
Elemento chiave nel protocollo Bitcoin, la funzione di hash SHA-256 è il capitano della nave. Altre funzioni, come SHA-512, sono utilizzate per la derivazione con HMAC e PBKDF. Inoltre, RIPMD160 è utilizzata per ridurre un'impronta a 160 bit. Quando parliamo di HASH256 e HASH160, ci riferiamo all'uso di un doppio hash con SHA-256 e RIPMD. L'uso di HASH160 è particolarmente vantaggioso perché consente di beneficiare della sicurezza di SHA-256 riducendo contemporaneamente la dimensione dell'impronta.

In sintesi, l'obiettivo finale di una funzione di hash crittografica è quello di trasformare un'informazione di dimensioni arbitrarie in un'impronta di dimensioni fisse. Per essere considerata sicura, deve avere diverse corde al suo arco: irreversibilità, resistenza alla falsificazione, resistenza alle collisioni e resistenza alla seconda preimmagine.

Alla fine di questa esplorazione, abbiamo svelato i segreti delle funzioni di hash crittografiche, evidenziato il loro utilizzo nel protocollo Bitcoin e analizzato i loro obiettivi specifici. Abbiamo imparato che per essere considerate sicure, le funzioni di hash devono essere resistenti alla preimmagine, alla seconda preimmagine, alle collisioni e alla falsificazione. Abbiamo anche esaminato la gamma di diverse funzioni di hash utilizzate nel protocollo Bitcoin. Nella nostra prossima sessione, ci immergeremo nel cuore della funzione di hash SHA256 e scopriremo le affascinanti matematiche che le conferiscono le sue caratteristiche uniche.

## I meccanismi di SHA256

![I meccanismi di SHA256](https://youtu.be/74SWg_ZbUj4)

Benvenuti alla continuazione del nostro affascinante viaggio attraverso i labirinti crittografici della funzione di hash. Oggi sveliamo i misteri di SHA256, un processo complesso ma ingegnoso che abbiamo introdotto nella nostra precedente discussione sulle funzioni di hash. Facciamo un passo avanti in questo labirinto, iniziando con il pre-trattamento di SHA256. Immaginate il pre-trattamento come la preparazione di un piatto gustoso, dove aggiungiamo "bit di riempimento" per far sì che la dimensione del nostro ingrediente principale, l'input, raggiunga un multiplo perfetto di 512 bit. Tutto questo con l'obiettivo finale di generare un hash succulento di 256 bit da un ingrediente di dimensioni variabili.

In questa ricetta crittografica, giochiamo con i bit, avendo una dimensione di messaggio iniziale che chiameremo M. Un bit è riservato per il separatore, mentre P bit sono utilizzati per il riempimento. Inoltre, mettiamo da parte 64 bit per la seconda fase di pre-trattamento. Il totale deve essere un multiplo di 512 bit. Un po' come assicurarsi che tutti gli ingredienti si armonizzino perfettamente nel nostro piatto.
Passiamo ora alla seconda fase del pre-trattamento, che implica l'aggiunta della rappresentazione binaria della dimensione del messaggio iniziale, in bit. Per questo, utilizziamo i nostri 64 bit riservati durante la fase precedente. Aggiungiamo zeri per arrotondare i nostri 64 bit all'input bilanciato. Successivamente, uniamo il messaggio iniziale, il riempimento dei bit e il riempimento della dimensione, come ingredienti in un frullatore, per ottenere il nostro input bilanciato.

Ora ci prepariamo per i primi passi del trattamento della funzione SHA-256. Come in ogni buona ricetta, abbiamo bisogno di alcuni ingredienti di base, che chiamiamo costanti e vettori di inizializzazione. I vettori di inizializzazione, da A a H, sono i primi 32 bit delle parti decimali delle radici quadrate dei primi 8 numeri primi. Le costanti K, da 0 a 63, rappresentano invece i primi 32 bit delle parti decimali delle radici cubiche dei primi 64 numeri primi.

All'interno della funzione di compressione, utilizziamo operatori specifici come XOR, AND e NOT. Elaboriamo i bit uno per uno in base alla loro posizione, utilizzando l'operatore XOR e una tabella di verità. L'operatore AND viene utilizzato per restituire 1 solo se entrambi gli operandi sono uguali a 1, e l'operatore NOT per restituire il valore opposto di un operando. Utilizziamo anche l'operazione SHR per spostare i bit verso destra di un numero scelto.

Infine, dopo aver separato l'input bilanciato in diversi blocchi di messaggi di 512 bit, effettuiamo 64 cicli di calcolo nella funzione di compressione. Come in una gara ciclistica, ogni giro di pista migliora la nostra posizione. Aggiungiamo modulo 2^32 lo stato intermedio allo stato iniziale della funzione di compressione. Le addizioni nella funzione di compressione sono addizioni modulo 2^32 per contenere la dimensione delle somme a 32 bit.

In conclusione, vorremmo sottolineare il ruolo cruciale dei calcoli effettuati nelle scatole CH, MAJ, σ0 e σ1. Queste operazioni, tra le altre, sono i guardiani che assicurano la robustezza della funzione di hash SHA256 contro gli attacchi, rendendola una scelta privilegiata per la sicurezza di molti sistemi digitali, in particolare nel protocollo Bitcoin. È quindi evidente che, sebbene complessa, la bellezza di SHA256 risiede nella sua robustezza nel trovare l'input a partire dall'hash, mentre la verifica dell'hash per un input dato è un'azione meccanicamente semplice.

## Gli algoritmi utilizzati per la derivazione

![Gli algoritmi utilizzati per la derivazione](https://youtu.be/ZF1_BMsOJXc)
Gli algoritmi di derivazione HMAC e PBKDF2 sono componenti chiave nella meccanica di sicurezza del protocollo Bitcoin. Prevengono una varietà di attacchi potenziali e garantiscono l'integrità dei portafogli Bitcoin.

HMAC e PBKDF2 sono strumenti crittografici utilizzati per diverse attività in Bitcoin. HMAC è principalmente utilizzato per contrastare gli attacchi di estensione di lunghezza durante la derivazione dei portafogli deterministici gerarchicamente (HD), mentre PBKDF2 è utilizzato per convertire una frase mnemonica in un seme.

HMAC, che prende un messaggio e una chiave come input, genera un output di dimensione fissa. Per garantire l'uniformità, la chiave viene adattata in base alla dimensione dei blocchi utilizzati nella funzione di hash. Nel contesto della derivazione dei portafogli HD, viene utilizzato HMAC-SHA-512. Quest'ultimo funziona con blocchi di 1024 bit (128 byte) e adatta la chiave di conseguenza. Utilizza le costanti OPAD (0x5c) e IPAD (0x36), ripetute quante volte necessario per rafforzare la sicurezza.

Il processo di HMAC-SHA-512 implica la concatenazione del risultato di SHA-512 applicato alla chiave XOR OPAD e alla chiave XOR IPAD con il messaggio. Quando viene utilizzato con blocchi di 1024 bit (128 byte), la chiave di input viene completata con zeri se necessario, quindi XORata con IPAD e OPAD. La chiave così modificata viene quindi concatenata con il messaggio.

Il codice di catena, integrando una fonte aggiuntiva di entropia, aumenta la sicurezza delle chiavi derivate. Senza di esso, un attacco potrebbe compromettere l'intero portafoglio e rubare tutti i bitcoin.

PBKDF2 viene utilizzato per convertire una frase mnemonica in un seme. Questo algoritmo esegue 2048 cicli utilizzando HMAC SHA512. Grazie a questi algoritmi di derivazione, due input diversi possono dare un output unico e fisso, che risolve il problema degli attacchi di estensione di lunghezza possibili sulle funzioni della famiglia SHA-2.

Un attacco di estensione di lunghezza sfrutta una proprietà specifica di alcune funzioni di hash crittografiche. In un tale attacco, un attaccante che già possiede l'hash di un messaggio sconosciuto può utilizzarlo per calcolare l'hash di un messaggio più lungo, che è un'estensione del messaggio originale. Ciò è spesso possibile senza conoscere il contenuto del messaggio originale, il che può portare a importanti falle di sicurezza se questo tipo di funzione di hash viene utilizzato per attività come la verifica dell'integrità.
In conclusione, gli algoritmi HMAC e PBKDF2 svolgono un ruolo essenziale nella sicurezza della derivazione dei portafogli HD nel protocollo Bitcoin. HMAC-SHA-512 viene utilizzato per proteggersi dagli attacchi di estensione di lunghezza, mentre PBKDF2 consente la conversione della frase mnemonica in un seme. Il codice di catena aggiunge una fonte di entropia aggiuntiva nella derivazione delle chiavi, garantendo così la robustezza del sistema.

# Le firme digitali

## Firme digitali e curve ellittiche

![Firme digitali e curve ellittiche](https://youtu.be/gOjYiPkx4z8)

Nel mondo delle criptovalute, la sicurezza delle transazioni è fondamentale. Al centro del protocollo Bitcoin si trova l'uso di firme digitali che fungono da prove matematiche della proprietà di una chiave privata associata a una chiave pubblica specifica. Questa tecnica di protezione dei dati si basa essenzialmente su un campo affascinante della crittografia chiamato crittografia a curve ellittiche (ECC).

La crittografia a curve ellittiche è la colonna vertebrale della sicurezza delle transazioni Bitcoin. Queste curve ellittiche, che ricordano le curve matematiche che abbiamo studiato a scuola, sono utili in una varietà di applicazioni crittografiche, dalla scambio di chiavi alla crittografia asimmetrica alla creazione di firme digitali. Un dettaglio interessante che distingue le curve ellittiche è la loro simmetria: qualsiasi linea non verticale che taglia due punti della curva intersecherà un terzo punto.

Ora, approfondiamo un po': il protocollo Bitcoin utilizza una particolare curva ellittica chiamata SecP256K1 per eseguire le sue operazioni crittografiche. Questa curva, definita su un insieme finito di interi positivi modulo un numero primo di 256 bit, può essere visualizzata come una nuvola di punti piuttosto che come una curva tradizionale. È questa progettazione unica che consente a Bitcoin di proteggere efficacemente le sue transazioni.

Per quanto riguarda la scelta della curva secp256k1 per Bitcoin, è interessante notare che è stata preferita alla curva secp256r1. Questa curva è definita dai parametri a=0 e b=7, e la sua equazione è y² = x³ + 7 modulo n, con n che rappresenta il numero primo che determina l'ordine della curva.

Quando si parla delle costanti utilizzate nel sistema Bitcoin, si fa generalmente riferimento ai parametri specifici dell'algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA) e del sistema di curve ellittiche utilizzato da Bitcoin, che è la curva secp256k1. Ecco questi parametri:

- Champ primaire (p) : Bitcoin utilizza una curva su un campo primario, quindi p è il primo numero utilizzato per definire questo campo. Per la curva secp256k1, p è uguale a `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` in esadecimale o p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 in decimale.
- Ordine della curva (n) : Si tratta del numero di punti sulla curva, compreso il punto all'infinito. Per secp256k1, n è uguale a `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` in esadecimale o n = 2^256 - 432420386565659656852420866394968145599 in decimale.
- Punto generatore (G) : Il punto di base, o generatore, è il punto sulla curva da cui vengono generate tutte le altre chiavi pubbliche. Ha coordinate x e y specifiche, generalmente rappresentate in esadecimale. Per secp256k1, le coordinate G sono, in esadecimale:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Si noti che tutti i valori esadecimali sono generalmente rappresentati in base 16, mentre i valori decimali sono in base 10. Inoltre, tutte le operazioni su queste costanti vengono eseguite modulo p per le coordinate dei punti sulla curva e modulo n per le operazioni di chiave e firma.

Quindi, dove vengono conservati questi famosi bitcoin? Non in un portafoglio Bitcoin, come si potrebbe pensare. In realtà, un portafoglio Bitcoin conserva le chiavi private necessarie per dimostrare la proprietà dei bitcoin. I bitcoin stessi sono registrati sulla blockchain, un database decentralizzato che archivia tutte le transazioni.

Nel sistema Bitcoin, l'unità di conto è il bitcoin (si noti la "b" minuscola). Quest'ultimo è divisibile fino a otto decimali, l'unità più piccola è il satoshi. Gli UTXO, o "Unspent Transaction Output", rappresentano le uscite di transazioni non spese appartenenti a un utente. Per spendere questi bitcoin, è necessario dimostrare la proprietà della chiave privata corrispondente alla chiave pubblica associata a ciascun UTXO.
Per garantire la sicurezza delle transazioni, Bitcoin utilizza due protocolli di firma digitale: l'ECDSA (Elliptic Curve Digital Signature Algorithm) e Schnorr. ECDSA è un protocollo di firma integrato in Bitcoin fin dal suo lancio nel 2009, mentre le firme di Schnorr sono state aggiunte più recentemente, nel novembre 2021. Sebbene entrambi i protocolli si basino sulla crittografia a curve ellittiche e utilizzino meccanismi matematici simili, differiscono principalmente in termini di struttura di firma.

Prima di approfondire questi meccanismi di firma, è importante capire cosa sia una curva ellittica. Una curva ellittica è definita dall'equazione y² = x³ + ax + b. Ogni punto su questa curva ha una distintiva simmetria che è la chiave della sua utilità in crittografia.

In definitiva, diverse curve ellittiche sono riconosciute come sicure per l'uso crittografico. La più conosciuta è forse la curva secp256r1. Tuttavia, per Bitcoin, Satoshi Nakamoto ha optato per un'altra curva: la secp256k1.

Nella prossima sezione di questo corso, esamineremo più da vicino la chiave pubblica e la chiave privata per una comprensione approfondita della crittografia sulle curve ellittiche e dell'algoritmo di firma digitale. Sarà il momento di consolidare le tue conoscenze e capire come tutte queste informazioni si articolano per garantire la sicurezza del protocollo Bitcoin.

## Calcolo della chiave pubblica dalla chiave privata

![Calcolo della chiave pubblica dalla chiave privata](https://youtu.be/NJENwFU889Y)

Nella continuazione di questo corso, esamineremo i meccanismi delle chiavi pubbliche e private, due elementi cruciali del protocollo Bitcoin. Queste chiavi sono intrinsecamente legate dall'algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA). Comprendere queste chiavi ci darà una profonda comprensione di come Bitcoin protegge le transazioni sulla sua piattaforma.

Per iniziare, immergiamoci nell'universo dell'algoritmo ECDSA. Bitcoin utilizza questo algoritmo di firma digitale per collegare le chiavi private e pubbliche. In questo sistema, la chiave privata è un numero casuale o pseudo-casuale di 256 bit. Il numero totale di possibilità per una chiave privata è teoricamente di 2^256, ma è leggermente inferiore a questo nella realtà. Per essere precisi, alcune chiavi private di 256 bit non sono valide per Bitcoin.
Per essere compatibile con Bitcoin, una chiave privata deve essere compresa tra 1 e n-1, dove n rappresenta l'ordine della curva ellittica. Ciò significa che il numero totale di possibilità per una chiave privata Bitcoin è quasi uguale a 1,158 x 10^77. Per mettere questo in prospettiva, è circa lo stesso numero di atomi presenti nell'universo osservabile. La chiave privata unica viene quindi utilizzata per determinare una chiave pubblica di 512 bit.

La chiave pubblica, indicata con K, è un punto sulla curva ellittica che deriva dalla chiave privata utilizzando operazioni di punti sulla curva. È importante notare che la funzione ECDSA è irreversibile, ovvero è impossibile recuperare la chiave privata dalla chiave pubblica. Questa irreversibilità è la pietra angolare della sicurezza del portafoglio Bitcoin.

La chiave pubblica è composta da due punti di 256 bit ciascuno, per un totale di 512 bit. Tuttavia, può essere compressa in un numero di 264 bit. Il punto G è il punto di partenza per calcolare tutte le chiavi pubbliche degli utenti del sistema.

Una delle proprietà notevoli delle curve ellittiche è che una linea che interseca la curva in due punti intersecherà anche un terzo punto, chiamato punto O. Questa proprietà viene utilizzata per determinare il punto U, che è l'opposto del punto O. L'aggiunta di un punto a se stesso viene effettuata tracciando una tangente alla curva a quel punto, che dà un nuovo punto unico chiamato j. Il prodotto scalare di un punto per n equivale ad aggiungere quel punto a se stesso n volte.

Queste operazioni sui punti di una curva ellittica sono alla base del calcolo delle chiavi pubbliche. Conoscendo la chiave privata, è facile calcolare la chiave pubblica. Tuttavia, conoscere la chiave pubblica non consente di calcolare la chiave privata, garantendo così la sicurezza del sistema Bitcoin. Infatti, la sicurezza delle chiavi pubbliche e private si basa sul problema del logaritmo discreto, una questione matematica complessa.

Nella nostra prossima lezione, esploreremo come una firma digitale viene realizzata utilizzando l'algoritmo ECDSA con una chiave privata per sbloccare i bitcoin. Restate sintonizzati per questa emozionante esplorazione del mondo delle criptovalute e della crittografia.

## Firmare con la chiave privata

![Firmare con la chiave privata](https://youtu.be/h2hIyGgPqkM)
Il processo di firma digitale è un metodo chiave per dimostrare di essere il detentore di una chiave privata senza doverla rivelare. Ciò viene realizzato utilizzando l'algoritmo ECDSA, che prevede la determinazione di un nonce univoco, il calcolo di un numero specifico, V, e la creazione di una firma digitale composta da due parti, S1 e S2. È cruciale utilizzare sempre un nonce univoco per evitare attacchi di sicurezza. Un esempio noto di ciò che può accadere quando questa regola non viene rispettata è il caso dell'hacking della PlayStation 3, che è stato compromesso a causa del riutilizzo del nonce.

In modo preciso, per validare una firma digitale utilizzando l'algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm), di solito sono coinvolti i seguenti passaggi:

1. Verificare che i valori della firma, S1 e S2, siano nell'intervallo [1, n-1]. Se non è così, la firma è invalida.
2. Calcolare l'inverso di S2 mod n. Lo chiameremo u. Spesso viene calcolato come segue: u = (S2)^-1 mod n.
3. Calcolare H, che è il valore di hash del messaggio firmato.
4. Calcolare u1 = H _ u mod n e u2 = S1 _ u mod n.
5. Calcolare il punto P sulla curva ellittica utilizzando u1, u2 e la chiave pubblica K: P = u1*G + u2*K, dove G è il punto di generazione della curva.
6. Se P è il punto all'infinito, la firma è invalida.
7. Calcolare I = coordinata x di P mod n.
8. La firma è valida se I è uguale a S1.

È importante notare che ogni software può utilizzare diverse notazioni e alcune fasi possono essere combinate o riarrangiate, ma la logica di base è la stessa. Si noti inoltre che tutte le operazioni aritmetiche vengono eseguite nel campo finito definito dalla curva ellittica (mod n, dove n è l'ordine della curva). Per ricordare, la curva secp256k1 (utilizzata in Bitcoin) n = 2^256 - 432420386565659656852420866394968145599.

Per quanto riguarda la generazione di chiavi pubbliche e private, è essenziale familiarizzarsi con la curva ellittica e il punto generatore. Per ottenere una chiave pubblica, deve essere scelto un numero casuale come chiave privata, spesso chiamato `nonce`, e utilizzato nell'equazione della curva ellittica.
La curva ellittica è uno strumento potente per generare chiavi pubbliche e private sicure. Ad esempio, per ottenere la chiave pubblica 3G, si disegna una tangente al punto G, si calcola l'opposto di -G per ottenere 2G, quindi si aggiunge G e 2G. Per effettuare una transazione, è necessario dimostrare di conoscere il numero 3 sbloccando i bitcoin associati alla chiave pubblica 3G.

Per creare una firma digitale e dimostrare di conoscere la chiave privata associata alla chiave pubblica 3G, si calcola prima un nonce, quindi il punto V associato a questo nonce (nell'esempio dato, è 4G). Successivamente, si calcola il punto T aggiungendo la chiave pubblica 3G e il punto V, ottenendo 7G.

La verifica di una firma digitale è un passaggio cruciale nell'utilizzo dell'algoritmo ECDSA, che consente di confermare l'autenticità di un messaggio firmato senza la necessità della chiave privata del mittente. Ecco come funziona in dettaglio:

Nel nostro esempio, abbiamo due valori importanti: T e V. T è un valore numerico (7 in questo esempio), e V è un punto sulla curva ellittica (rappresentato qui da 4G). Questi valori vengono prodotti durante la creazione della firma digitale e vengono quindi inviati con il messaggio per consentire la verifica.

Quando il verificatore riceve il messaggio, riceverà anche questi due valori, T e V.

Ecco i passaggi che il verificatore seguirà per validare la firma:

1. Calcolerà prima l'hash del messaggio, che chiameremo H.
2. Quindi calcolerà u1 e u2. Per farlo, utilizzerà le seguenti formule:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n
     Dove S2 è la seconda parte della firma digitale, n è l'ordine della curva ellittica e (S2)^-1 è l'inverso di S2 mod n.
3. Il verificatore calcolerà quindi un punto P' sulla curva ellittica utilizzando la formula: P' = u1 _ G + u2 _ K
   - G è il punto di generazione della curva
   - K è la chiave pubblica del mittente
4. Il verificatore calcolerà quindi I', che è semplicemente la coordinata x del punto P' modulo n.
5. Infine, il verificatore confermerà che I' è uguale a T. Se è così, la firma è considerata valida. Se non è così, la firma è invalida.

Questa procedura garantisce che solo il mittente che possiede la corrispondente chiave privata potrebbe aver prodotto una firma che supera questo processo di verifica.
In conclusione, la verifica di una firma digitale ECDSA è una procedura essenziale nelle transazioni Bitcoin. Ciò garantisce che il messaggio firmato non sia stato alterato durante la trasmissione e che il mittente sia il detentore della chiave privata. Questa tecnica di autenticazione digitale si basa su principi matematici complessi, tra cui l'aritmetica delle curve ellittiche, mantenendo la riservatezza della chiave privata. Offre una solida base di sicurezza per le transazioni crittografiche.

Detto ciò, la gestione di queste chiavi, così come la loro creazione, è un'altra questione essenziale in Bitcoin. Come generare una nuova coppia di chiavi? Come organizzare una moltitudine di chiavi in modo sicuro ed efficiente? Come recuperarle se necessario?

Per rispondere a queste domande e approfondire la comprensione della sicurezza della crittografia, il nostro prossimo corso si concentrerà sul concetto di Portafoglio Deterministico Gerarchico (HD wallets) e sull'uso di frasi mnemoniche. Questi meccanismi offrono modi eleganti per gestire efficacemente le tue chiavi di criptovaluta, rafforzando la sicurezza e la recuperabilità.

# La frase mnemonica

## Evoluzione dei portafogli Bitcoin

![Evoluzione dei portafogli Bitcoin](https://youtu.be/6tmu1R9cXyk)

Il Portafoglio Deterministico Gerarchico, o più comunemente chiamato portafoglio HD, gioca un ruolo predominante nell'ecosistema delle criptovalute. Il termine "portafoglio" può sembrare fuorviante per coloro che sono alle prime armi in questo campo, poiché non implica il possesso di denaro o valute. Si riferisce invece a una collezione di chiavi crittografiche private derivate da una singola chiave madre, grazie a un ingegnoso processo di aritmetica algoritmica. Queste chiavi private, che hanno una lunghezza fissa di 256 bit, sono l'essenza stessa del possesso di criptovalute e a volte sono indicate con il nome un po' più grezzo di "Just a Bunch Of Keys" (JBOC).

Tuttavia, la complessità della gestione di queste chiavi è compensata da un insieme di protocolli, chiamati Bitcoin Improvement Proposals (BIP). Queste proposte di aggiornamento sono al centro della funzionalità e della sicurezza dei portafogli HD. Ad esempio, il [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lanciato nel 2012, ha rivoluzionato il modo in cui queste chiavi vengono generate e archiviate, introducendo il concetto di chiavi derivate in modo deterministico e gerarchico. In questo modo, il processo di backup di queste chiavi è notevolmente semplificato, mantenendo comunque il loro livello di sicurezza.
In seguito, il [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) ha introdotto un'innovazione significativa: la frase mnemonica di 24 parole. Questo sistema ha permesso di trasformare una sequenza di numeri complessa e difficile da ricordare in una serie di parole comuni, molto più facili da memorizzare e conservare. Inoltre, il [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) ha proposto di aggiungere una password aggiuntiva per rafforzare la sicurezza delle chiavi individuali. Questi miglioramenti successivi hanno portato agli standard BIP43 e BIP44, che hanno standardizzato la struttura e la gerarchia dei portafogli HD, rendendo questi portafogli più accessibili e facili da usare per il grande pubblico.

Nelle sezioni seguenti, approfondiremo il funzionamento dei portafogli HD. Affronteremo i principi di derivazione delle chiavi e esamineremo i concetti fondamentali di entropia e generazione di numeri casuali, che sono essenziali per garantire la sicurezza del tuo portafoglio HD.

In sintesi, è essenziale sottolineare il ruolo centrale di BIP32 e BIP39 nella progettazione e sicurezza dei portafogli HD. Questi protocolli consentono di generare molte chiavi da un'unica seme, che dovrebbe essere un numero casuale o pseudo-casuale. Oggi, questi standard sono adottati dalla maggior parte dei portafogli di criptovalute, sia che siano dedicati a una singola criptovaluta o che supportino diversi tipi di valute.

Speriamo che questa introduzione ti abbia aiutato a comprendere meglio i fondamenti del portafoglio HD e le sue diverse caratteristiche. Il nostro obiettivo è aiutarti a padroneggiare questi concetti essenziali e a navigare più efficacemente nell'universo complesso delle criptovalute. Quindi, rimani con noi mentre continuiamo a esplorare le sfumature e le sottigliezze di questo mondo affascinante nelle prossime lezioni.

## Entropia e numeri casuali

![Entropia e numeri casuali](https://youtu.be/k18yH18w2TE)
L'importanza della sicurezza delle chiavi private nell'ecosistema di Bitcoin è indiscutibile. Infatti, sono la pietra angolare che garantisce la sicurezza delle transazioni Bitcoin. Per evitare qualsiasi vulnerabilità associata alla prevedibilità, queste chiavi devono essere generate in modo veramente casuale, il che può rapidamente diventare un esercizio laborioso per l'utente. Una soluzione a questo enigma è il Portafoglio Deterministico Gerarchico, o portafoglio HD. Questo metodo consente di generare in modo deterministico e gerarchico coppie di chiavi figlie da un'unica informazione alla base del portafoglio. Qui l'aleatorietà si rivela indispensabile per garantire la sicurezza delle chiavi derivate.

La generazione di numeri casuali è infatti un elemento cruciale in crittografia, per garantire l'integrità delle chiavi private. Per prevenire qualsiasi vulnerabilità legata alla prevedibilità, una chiave privata deve essere prodotta in modo casuale. L'uso di una nuova coppia di chiavi per ogni transazione consente di rafforzare ulteriormente la sicurezza, anche se ciò complica il loro backup e preserva solo parzialmente la riservatezza. In sintesi, la sicurezza delle chiavi private è una priorità assoluta, che richiede una generazione rigorosa e casuale. I portafogli HD offrono una soluzione per facilitare la generazione e la gestione delle chiavi, mantenendo un alto livello di sicurezza.

Tuttavia, la generazione di numeri casuali sui computer rappresenta una sfida importante, poiché i risultati ottenuti non sono veramente casuali. Ecco perché è essenziale utilizzare un Generatore di Numeri Casuali (RNG). I tipi di RNG variano, dalle Pseudo-Random Number Generators (PRNG) ai True Random Number Generators (TRNG), così come ai PRNG che integrano una fonte di entropia.

Nel caso di Bitcoin, le chiavi private sono generate da un'unica informazione alla base del portafoglio. Questa informazione consente una derivazione deterministica e gerarchica delle coppie di chiavi figlie. L'entropia è la base di ogni portafoglio HD, anche se non esiste uno standard per la generazione di questo numero casuale. Pertanto, la generazione di numeri casuali è una questione cruciale per garantire la sicurezza delle transazioni Bitcoin.

La fase di verifica della generazione delle chiavi è cruciale per garantire la sicurezza e l'autenticità della generazione di numeri casuali, una fase fondamentale per prevenire qualsiasi vulnerabilità associata alla prevedibilità. È quindi fortemente consigliato utilizzare portafogli open source per consentire questa verifica.
Tuttavia, è importante notare che alcuni portafogli hardware possono essere "closed source", rendendo impossibile la verifica della generazione del numero casuale. Una possibile soluzione sarebbe quella di generare la propria frase mnemonica utilizzando dei dadi, anche se questo approccio potrebbe presentare alcuni rischi. L'utilizzo di una passphrase generata casualmente può aiutare ad attenuare questi rischi.

Un esempio di applicazione di questo metodo è l'opzione "dice roll" offerta da CoinKit per generare frasi mnemoniche. Un'altra possibilità sarebbe quella di utilizzare un'informazione iniziale molto ampia e ridurre questa informazione a 256 bit con la funzione di hash SHA-256, in grado di generare un buon numero casuale. È importante menzionare che la funzione di hash SHA-256 resiste alle collisioni, alla falsificazione e agli attacchi di pre-immagine e di seconda pre-immagine.

In definitiva, il casuale occupa un posto centrale nella crittografia e nell'informatica, e la capacità di generare casualità in modo sicuro è cruciale per garantire la sicurezza delle chiavi private e delle transazioni Bitcoin. L'entropia, che è al centro del portafoglio HD di Bitcoin, è essenziale per la sua sicurezza. Nella nostra prossima lezione, continueremo ad esplorare questo argomento, approfondendo ulteriormente il modo in cui l'entropia contribuisce alla sicurezza dei portafogli HD.

### Sostienici

Questo corso, così come l'intero contenuto presente su questa università, ti è stato offerto gratuitamente dalla nostra comunità. Per sostenerci, puoi condividerlo con chi ti sta intorno, diventare membro dell'università e persino contribuire al suo sviluppo tramite GitHub. A nome di tutto il team, grazie!

### Valuta il corso

Un sistema di valutazione per il corso sarà presto integrato in questa nuova piattaforma di E-learning! Nel frattempo, grazie mille per aver seguito il corso e se ti è piaciuto, pensa di condividerlo con chi ti sta intorno.

## La frase mnemonica

![La frase mnemonica](https://youtu.be/uJERqH9Xp7I)

La sicurezza di un portafoglio Bitcoin è una preoccupazione principale per tutti i suoi utenti. Un modo essenziale per garantire il backup del portafoglio consiste nella generazione di una frase mnemonica basata sull'entropia e sul checksum.

L'entropia è il pilastro della sicurezza del portafoglio HD. Esistono diverse metodologie per generare questa entropia, tra cui i generatori di numeri pseudo-casuali (PRNG), i generatori di numeri casuali veri (TRNG) o manualmente. È cruciale che questa entropia sia casuale o pseudo-casuale per garantire la sicurezza del portafoglio.
D'altra parte, il checksum garantisce la verifica dell'esattezza della frase di recupero. Senza questo checksum, un errore nella frase potrebbe portare alla creazione di un portafoglio diverso e quindi alla perdita dei fondi. Si ottiene il checksum passando l'entropia attraverso la funzione SHA256 e recuperando i primi 8 bit dell'hash.

Esistono diversi standard per la frase mnemonica in base alla dimensione dell'entropia. Lo standard più comunemente utilizzato per una frase di recupero di 24 parole è un'entropia di 256 bit. La dimensione del checksum è determinata dividendo la dimensione dell'entropia per 32.

Ad esempio, un'entropia di 256 bit genera un checksum di 8 bit. La concatenazione dell'entropia e del checksum porta quindi a dimensioni rispettivamente di 128 bit, 160 bit, ecc. In base alla dimensione dell'entropia, la frase di recupero avrà 12 parole per 128 bit, 15 parole per 160 bit e 24 parole per 256 bit.

Per trasformare i bit in parole, ogni segmento è associato a una parola proveniente da un elenco di 2048 parole. È importante precisare che nessuna parola presenta le prime quattro lettere nello stesso ordine.

È essenziale salvare la frase di recupero di 24 parole per preservare l'integrità del portafoglio Bitcoin. I due standard più comunemente utilizzati si basano su un'entropia di 128 o 256 bit e una concatenazione di 12 o 24 parole. L'aggiunta di una passphrase costituisce un'opzione aggiuntiva per rafforzare la sicurezza del portafoglio.

In conclusione, la generazione di una frase mnemonica per proteggere un portafoglio Bitcoin è un processo cruciale. È importante rispettare gli standard della frase mnemonica in base alla dimensione dell'entropia. Il salvataggio della frase di recupero di 24 parole è essenziale per prevenire qualsiasi perdita di fondi. Vi ringraziamo per la vostra attenzione e vi diamo appuntamento per il nostro prossimo corso sulla criptovaluta.

## La passphrase

![La passphrase](https://youtu.be/dZkOYO7MXwc)

La passphrase è una password aggiuntiva che può essere integrata in un portafoglio Bitcoin per aumentarne la sicurezza. Il suo utilizzo è opzionale e dipende dall'apprezzamento dell'utente. Aggiungendo informazioni arbitrarie che, insieme alla frase mnemonica, consentono di calcolare il seme del portafoglio, la passphrase rafforza la sicurezza dello stesso.
Per derivare le chiavi di un portafoglio HD, è necessaria la frase mnemonica e la passphrase. La passphrase è libera e può raggiungere una dimensione quasi infinita. Non è inclusa nella frase mnemonica, che è standardizzata e deve seguire alcune restrizioni di dimensione, checksum e codifica. Un attaccante non può accedere ai bitcoin di un utente senza conoscere la passphrase. Quest'ultima gioca un ruolo nella costruzione e nel calcolo di tutte le chiavi del portafoglio.
La funzione pbkdf2 viene utilizzata per generare il seme dalla passphrase. Questo seme consente di derivare tutte le coppie di chiavi figlie del portafoglio. Se la passphrase viene modificata, il portafoglio Bitcoin diventa completamente diverso.

La passphrase è uno strumento essenziale per rafforzare la sicurezza dei portafogli Bitcoin. Può consentire l'applicazione di diverse strategie di sicurezza. Ad esempio, può essere utilizzata per creare duplicati e facilitare il backup della frase mnemonica. Può anche migliorare la sicurezza del portafoglio attenuando i rischi associati alla generazione casuale della frase mnemonica.

Una passphrase efficace dovrebbe essere lunga (20-40 caratteri) e diversificata (utilizzando maiuscole, minuscole, numeri e simboli). Non dovrebbe essere direttamente legata all'utente o al suo ambiente. È più sicuro utilizzare una sequenza casuale di caratteri anziché una parola semplice come passphrase.

Una passphrase è più sicura di una semplice password. La passphrase ideale è lunga, variegata e casuale. Può rafforzare la sicurezza di un portafoglio o di un software caldo. Può anche essere utilizzata per creare backup ridondanti e sicuri.

È fondamentale prendersi cura dei backup della passphrase per evitare di perdere l'accesso al portafoglio. Una passphrase è un'opzione per un portafoglio HD. Può essere generata casualmente con dadi o un altro generatore di numeri pseudo-casuali. Non è consigliabile memorizzare una passphrase o una frase mnemonica.

Nel nostro prossimo corso, esamineremo in dettaglio il funzionamento del seme e la prima coppia di chiavi generata da esso. Non esitate a seguire questo corso per continuare il vostro apprendimento. Non vediamo l'ora di rivedervi presto.

## Creazione di un seme da 128 lanci di dadi!

![Creazione di un seme da 128 lanci di dadi!](https://youtu.be/lUw-1kk75Ok)
La creazione di una frase mnemonica è un passaggio cruciale per la sicurezza del tuo portafoglio di criptovalute. Ci sono diverse metodologie per generare una frase mnemonica, ma ci concentreremo sulla generazione manuale utilizzando dei dadi. È importante sottolineare che questa metodologia non è adatta per un portafoglio di grande valore. Si consiglia di utilizzare un software open source o un portafoglio hardware per generare la frase mnemonica. Per creare una frase mnemonica, utilizzeremo dei dadi per generare un'informazione binaria. L'obiettivo è comprendere il processo di creazione della frase mnemonica.

**Passaggio 1 - Preparazione:**
Assicurati di avere una distribuzione Linux amnesica, come Tails OS, installata su una chiavetta USB per maggiore sicurezza. Si noti che questo tutorial non dovrebbe essere utilizzato per creare un portafoglio principale.

**Passaggio 2 - Generazione di un numero binario casuale:**
Utilizzeremo dei dadi per generare un'informazione binaria. Lancia un dado 128 volte e annota ogni risultato (1 per dispari, 0 per pari).

**Passaggio 3 - Organizzazione dei numeri binari:**
Organizza i numeri binari ottenuti in righe di 11 cifre per facilitare i calcoli successivi. La dodicesima riga dovrebbe avere solo 7 cifre.

**Passaggio 4 - Calcolo del checksum:**
Le ultime 4 cifre per la dodicesima riga corrispondono al checksum. Per calcolare questo checksum, dobbiamo utilizzare un terminale di una distribuzione Linux. Si consiglia di utilizzare [TailOs](https://tails.boum.org/index.fr.html) che è una distribuzione senza memoria avviabile da una chiavetta USB. Una volta sul tuo terminale, inserisci il comando `echo <numero binario> | shasum -a 254 -0`. Sostituisci `<numero binario>` con la tua lista di 128 zeri e uno. L'output è un hash in esadecimale. Prendi il primo carattere di questo hash e convertilo in binario. Puoi aiutarti con questa [tabella](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table). Aggiungi il checksum in binario (4 cifre) alla dodicesima riga del tuo foglio.

**Passaggio 5 - Conversione in decimale:**
Per trovare le parole associate ad ogni riga, è necessario prima convertire in decimale ogni serie di 11 bit. Qui non è possibile utilizzare un convertitore online poiché questi bit rappresentano la tua frase mnemonica. Quindi sarà necessario convertire utilizzando una calcolatrice e un trucco che segue: ogni bit è associato ad una potenza di 2, quindi da sinistra a destra abbiamo 11 posizioni che corrispondono rispettivamente a 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Per convertire la tua serie di 11 bit in decimale, è sufficiente aggiungere solo le posizioni che contengono un 1. Ad esempio, per la serie 00110111011, ciò corrisponde all'aggiunta seguente: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Ora puoi convertire ogni riga in decimale. E prima di passare alla codifica in parole, è necessario aggiungere +1 a tutte le righe poiché l'indice della lista delle parole BIP39 inizia da 1 e non da 0.

**Passaggio 8 - Generazione della frase mnemonica:**
Inizia stampando la [lista dei 2048 parole](https://seedxor.com/files/wordlist.pdf) per convertire i tuoi numeri decimali nelle parole BIP39. La particolarità di questa lista è che nessuna parola ha le prime 4 lettere in comune con tutte le altre parole di questo dizionario. Quindi cerca per ogni riga la parola associata al numero decimale.

**Passaggio 9 - Test della frase mnemonica:**
Testa immediatamente la tua frase mnemonica su Sparrow Wallet creando un portafoglio da essa. Se ottieni un errore di checksum non valido, è probabile che tu abbia commesso un errore di calcolo. Correggi questo errore ripartendo dal passaggio 4 e testa nuovamente su Sparrow Wallet. Ecco fatto! Hai appena creato un nuovo portafoglio Bitcoin da 128 lanci di dadi.

Generare una frase mnemonica è un processo importante per proteggere il tuo portafoglio di criptovaluta. Si consiglia di utilizzare metodi più sicuri, come l'uso di software open source o di hardware wallet, per generare la frase mnemonica. Tuttavia, realizzare questo workshop consente di comprendere meglio come a partire da un numero casuale possiamo creare un portafoglio Bitcoin.

# Creazione di un portafoglio Bitcoin

## Creazione del seed e della chiave master

![Creazione del seed e della chiave master](https://youtu.be/56yAt_JDWhY)

In questa parte del corso, esploreremo i passaggi per la derivazione di un portafoglio HD (Hierarchical Deterministic Wallet), che consente di creare e gestire chiavi private e pubbliche in modo gerarchico.
Il fondamento del portafoglio HD si basa su due elementi essenziali: la frase mnemonica e la passphrase (password aggiuntiva opzionale). Insieme, costituiscono il seed, una sequenza alfanumerica di 512 bit che serve come base per derivare le chiavi del portafoglio. A partire da questo seed, è possibile derivare tutte le coppie di chiavi figlie del portafoglio Bitcoin. Il seed è la chiave per accedere a tutti i bitcoin associati al portafoglio, che si utilizzi o meno una passphrase.

Per ottenere il seed, si utilizza la funzione pbkdf2 (Password-Based Key Derivation Function 2) con la frase mnemonica e la passphrase. L'output di pbkdf2 è un seed di 512 bit. La chiave privata principale e il codice di catena principale sono determinati utilizzando l'algoritmo HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Questo algoritmo richiede un messaggio e una chiave per generare un risultato. La chiave privata principale è calcolata a partire dal seed e dalla frase "Bitcoin SEED". Questa frase è identica per tutte le derivazioni di portafoglio HD, garantendo così una coerenza tra i portafogli.

Inizialmente, la funzione SHA-512 non era implementata nel protocollo Bitcoin, motivo per cui si utilizza HMAC SHA-512. L'utilizzo di HMAC SHA-512 con la frase "Bitcoin SEED" vincola l'utente a generare un portafoglio specifico per Bitcoin. Il risultato di HMAC SHA-512 è un numero di 512 bit, diviso in due parti: i 256 bit a sinistra rappresentano la chiave privata principale, mentre i 256 bit a destra rappresentano il codice di catena principale.

La chiave privata principale è la chiave genitore di tutte le future chiavi del portafoglio, mentre il codice di catena principale interviene nella derivazione delle chiavi figlie. È importante notare che non è possibile derivare una coppia di chiavi figlie senza conoscere il codice di catena corrispondente della coppia genitore. Il codice di catena aggiunge una fonte di entropia nel processo di derivazione.

Una coppia di chiavi nel portafoglio comprende una chiave privata, una chiave pubblica e un codice di catena. Il codice di catena consente di introdurre una fonte di casualità nella derivazione delle chiavi figlie e di isolare ogni coppia di chiavi per evitare eventuali fughe di informazioni.

È importante sottolineare che la chiave privata principale è la prima chiave privata derivata a partire dal seed e non ha alcun legame con le chiavi estese del portafoglio. Il seed è quindi l'elemento fondamentale per derivare tutte le chiavi del portafoglio. Esso differisce dalla frase mnemonica e dalla passphrase, che vengono utilizzate per la creazione del seed.
Nel prossimo corso, esploreremo in dettaglio le chiavi estese, come xPub, xPRV, zPub, e capiremo perché vengono utilizzate e come vengono costruite.

## Le chiavi estese

![Le chiavi estese](https://youtu.be/TRz760E_zUY)

In questa parte del corso, studieremo le chiavi estese (xPub, zPub, yPub) e i loro prefissi, che svolgono un ruolo importante nella derivazione delle chiavi figlie in un portafoglio HD (Hierarchical Deterministic Wallet).

Le chiavi estese si distinguono dalle chiavi maestre. Un portafoglio HD genera una frase mnemonica e un seme per ottenere la chiave maestra e il codice di catena maestro. Le chiavi estese vengono utilizzate per derivare le chiavi figlie e richiedono sia la chiave genitore che il corrispondente codice di catena. Una chiave estesa combina queste due informazioni per semplificare il processo di derivazione.

Le chiavi estese sono identificate da prefissi specifici (XPRV, XPUB, YPUB, ZPUB) che indicano se si tratta di una chiave estesa privata o pubblica, nonché il suo scopo specifico. I metadati associati a una chiave estesa includono la versione (prefisso), la profondità, l'impronta della chiave pubblica, l'indice e il payload (codice di catena e chiave genitore).

Il payload è composto dal codice di catena (32 byte) e dalla chiave genitore (33 byte). Questi elementi sono essenziali per la derivazione delle chiavi figlie. Una chiave privata viene generata da un numero casuale o pseudo-casuale, mentre una chiave pubblica viene generata utilizzando l'algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm).

Ogni coppia di chiavi estese è associata a un codice di catena unico, che consente di effettuare derivazioni specifiche. Concatenando la chiave genitore con il codice di catena, si ottiene una chiave estesa privata o pubblica.

Le chiavi pubbliche estese possono derivare solo da chiavi pubbliche figlie normali, mentre le chiavi private estese possono derivare da chiavi figlie pubbliche e private, sia su una derivazione normale che indurita. L'uso di chiavi estese con il prefisso XPUB consente di derivare nuovi indirizzi senza risalire alle corrispondenti chiavi private, offrendo una maggiore sicurezza. I metadati associati alle chiavi estese forniscono informazioni importanti sul loro ruolo e sulla loro posizione nella gerarchia delle chiavi.
Le chiavi pubbliche compressate hanno una dimensione di 33 byte, mentre le chiavi pubbliche non elaborate sono di 512 bit. Le chiavi pubbliche compressate conservano le stesse informazioni delle chiavi non elaborate, ma con una dimensione ridotta. Le chiavi estese hanno una dimensione di 82 byte e il loro prefisso è rappresentato in base 58 grazie ad una conversione in esadecimale. Il checksum è calcolato utilizzando la funzione di hash HASH256.
Le derivazioni rafforzate iniziano a partire dagli indici che sono potenze di 2 (2^31). Le chiavi pubbliche estese consentono solo di derivare chiavi pubbliche figlie normali, mentre le chiavi private estese consentono di derivare qualsiasi chiave figlia. È interessante notare che i prefissi più comunemente utilizzati sono xpub e zpub, che corrispondono rispettivamente agli standard legacy e segwit v1 e segwit v0.

Nel nostro prossimo corso, ci concentreremo sulla derivazione delle coppie di chiavi figlie utilizzando le conoscenze acquisite sulle chiavi estese e la chiave maestra del portafoglio.

In conclusione, le chiavi estese svolgono un ruolo essenziale nella crittografia e nel funzionamento dei portafogli HD. Comprendere il loro utilizzo e il loro calcolo è cruciale per garantire la sicurezza delle transazioni e la protezione degli asset digitali. I prefissi e i metadati associati alle chiavi estese consentono un utilizzo efficiente e una derivazione precisa delle chiavi figlie necessarie.

## Derivazione delle coppie di chiavi figlie

![Derivazione delle coppie di chiavi figlie](https://youtu.be/FXhI-GmE9Aw)

Adesso, affronteremo il calcolo del seed e della chiave maestra, che costituiscono i primi elementi essenziali per la gerarchizzazione e la derivazione del portafoglio HD (Hierarchical Deterministic Wallet). Il seed, di lunghezza compresa tra 128 e 256 bit, viene generato in modo casuale o a partire da una frase segreta. Gioca un ruolo deterministico nella derivazione di tutte le altre chiavi. La chiave maestra è la prima chiave derivata dal seed e consente di derivare tutte le altre coppie di chiavi figlie.

Il codice di catena maestra svolge un ruolo importante nel recupero del portafoglio a partire dal seed. È importante notare che tutte le chiavi derivate dallo stesso seed avranno lo stesso codice di catena maestra.

La gerarchizzazione e la derivazione del portafoglio HD offrono una gestione più efficiente delle chiavi e delle strutture del portafoglio. Le chiavi estese consentono la derivazione di una coppia di chiavi figlie a partire da una coppia genitore utilizzando calcoli matematici e algoritmi specifici.
Ci sono diversi tipi di coppie di chiavi figlie, tra cui le chiavi rinforzate e le chiavi normali. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, sia in modalità normale che rinforzata. Ogni coppia di chiavi ha un indice che consente di differenziarle l'una dall'altra.
La derivazione delle chiavi figlie utilizza la funzione HMAC-SHA512 utilizzando la chiave genitore concatenata all'indice e al codice di stringa associato alla coppia di chiavi. Le chiavi figlie normali hanno un indice compreso tra 0 e 2 alla potenza 31 meno 1, mentre le chiavi figlie rinforzate hanno un indice compreso tra 2 alla potenza 31 e 2 alla potenza 32 meno 1.

Ci sono due tipi di coppie di chiavi figlie: le coppie rinforzate e le coppie normali. Il processo di derivazione delle chiavi figlie utilizza le chiavi pubbliche per generare le condizioni di spesa, mentre le chiavi private vengono utilizzate per la firma. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, in modalità normale o rinforzata.

La derivazione rinforzata utilizza la chiave privata genitore, mentre la derivazione normale utilizza la chiave pubblica genitore. La funzione HMAC-SHA512 viene utilizzata per la derivazione rinforzata, mentre la derivazione normale utilizza un condensato di 512 bit. La chiave pubblica figlia viene ottenuta moltiplicando la chiave privata figlia per il generatore della curva ellittica.

La gerarchizzazione e la derivazione di numerose coppie di chiavi in modo deterministico consentono di creare uno schema ad albero genealogico per la derivazione gerarchica. Nel prossimo corso di questa formazione, esamineremo la struttura del portafoglio HD e i percorsi di derivazione, concentrandoci in particolare sulla notazione dei percorsi di derivazione.

## Struttura del portafoglio e percorsi di derivazione

![Struttura del portafoglio e percorsi di derivazione](https://youtu.be/etO9UxwyE2I)

In questo capitolo, esamineremo la struttura dell'albero di derivazione in un portafoglio HD (Hierarchical Deterministic Wallet). Abbiamo già esplorato il calcolo del seme, la chiave principale e la derivazione delle coppie di chiavi figlie. Ora ci concentreremo sull'organizzazione delle chiavi all'interno del portafoglio.
Il portafoglio HD utilizza strati di profondità per organizzare le chiavi. Ogni derivazione da una coppia genitore a una coppia figlio corrisponde a uno strato di profondità. La profondità 0 corrisponde alla chiave principale e al codice di catena principale.
La profondità 1 viene utilizzata per derivare le chiavi figlie secondo uno specifico obiettivo, che è determinato dall'indice. Gli obiettivi sono conformi agli standard BIP 84 e Segwit v0/v1.

La profondità 2 consente di distinguere i conti di diverse criptovalute o reti. Ciò consente di organizzare il portafoglio in base alle diverse fonti di fondi.

La profondità 3 viene utilizzata per organizzare il portafoglio in diversi conti, offrendo così una struttura più chiara e organizzata.

La profondità 4 corrisponde alle catene interne ed esterne, che vengono utilizzate per gli indirizzi destinati a essere comunicati pubblicamente. L'indice 0 è associato alla catena esterna, mentre l'indice 1 è associato alla catena interna. Ogni conto ha due catene: la catena esterna (0) e la catena interna (1). La profondità 4 viene anche utilizzata per gestire i tipi di script nel caso dei portafogli multi firma.

La profondità 5 viene utilizzata per gli indirizzi di ricezione su un portafoglio classico. Nella prossima sezione, esamineremo più in dettaglio la derivazione delle coppie di chiavi figlie.

Per ogni strato di profondità, utilizziamo gli indici per distinguere le coppie di chiavi figlie. Gli indici rinforzati vengono utilizzati con un apostrofo per alcune derivazioni. La chiave pubblica per anno viene utilizzata come input per la funzione HMAC. L'indice in un percorso di derivazione indica il valore utilizzato nella funzione HMAC.

L'indice senza apostrofo corrisponde all'indice effettivamente utilizzato, mentre l'indice con apostrofo corrisponde all'indice effettivo + 2^31. Le derivazioni rinforzate utilizzano indici da 2^31 a 2^32-1. Ad esempio, l'indice 44' corrisponde all'indice effettivo 2^31 + 44.

Per generare un indirizzo di ricezione specifico, deriviamo una coppia di chiavi figlie dalla chiave principale e dal codice di catena principale. Quindi utilizziamo l'indice per distinguere le diverse coppie di chiavi figlie della stessa profondità.

Le chiavi estese, come XPUB, consentono di condividere il tuo portafoglio con più persone. La catena di derivazione viene utilizzata per distinguere la catena esterna (indirizzi destinati a essere comunicati) e la catena interna (indirizzi di cambio).
È importante notare che diverse profondità vengono utilizzate in un portafoglio HD in base a diversi standard. La derivazione delle chiavi genitore alle chiavi figlie consente di passare da una profondità all'altra. L'uso di diversi rami nel portafoglio HD indica i diversi standard seguiti.
Nel prossimo capitolo, esamineremo gli indirizzi di ricezione, i loro vantaggi di utilizzo e i passaggi per la loro costruzione.

# Cos'è un indirizzo Bitcoin?

## Gli indirizzi Bitcoin

![Gli indirizzi Bitcoin](https://youtu.be/nqGBMjPtFNI)

In questo capitolo, esploreremo gli indirizzi di ricezione, che svolgono un ruolo cruciale nel sistema Bitcoin. Consentono di ricevere fondi su una moneta e vengono generati a partire da coppie di chiavi private e pubbliche. Sebbene esista un tipo di script chiamato Pay2PublicKey che consente di bloccare bitcoin su una chiave pubblica, gli utenti preferiscono generalmente utilizzare gli indirizzi di ricezione anziché questo script.

Quando un destinatario desidera ricevere bitcoin, fornisce un indirizzo di ricezione all'emittente anziché la sua chiave pubblica. Un indirizzo è in realtà un hash di una chiave pubblica, con un formato specifico. La chiave pubblica è derivata dalla chiave privata figlia utilizzando operazioni matematiche come l'addizione e il raddoppio dei punti sulle curve ellittiche.

È importante notare che non è possibile risalire dall'indirizzo alla chiave pubblica, né dalla chiave pubblica alla chiave privata. L'uso di un indirizzo consente di ridurre le dimensioni dell'informazione della chiave pubblica, che inizialmente è di 512 bit. È possibile comprimere una chiave pubblica mantenendo solo il valore di x e aggiungendo un prefisso, ma questa tecnica non era nota al momento della creazione di Bitcoin. L'uso di un indirizzo non consente quindi di risparmiare spazio nei blocchi.

Gli indirizzi Bitcoin sono stati ridotti in dimensioni per facilitarne l'uso. Hanno un checksum, il che consente di rilevare gli errori di battitura e ridurre i rischi di perdita di bitcoin. Al contrario, le chiavi pubbliche non hanno un checksum, il che significa che gli errori di battitura possono comportare la perdita dei fondi corrispondenti.

Gli indirizzi offrono anche un secondo livello di sicurezza tra le informazioni pubbliche e private, rendendo più difficile il controllo della chiave privata. Le funzioni di hash utilizzate consentono alle coppie di chiavi di essere resistenti a eventuali attacchi condotti da calcolatori quantistici. Infatti, questi calcolatori possono potenzialmente rompere ECDSA (Elliptic Curve Digital Signature Algorithm), ma non possono rompere una funzione di hash.
È essenziale sottolineare che ogni indirizzo è a uso unico, il che contribuisce alla sicurezza e alla riservatezza. La riutilizzazione di uno stesso indirizzo comporta gravi problemi di riservatezza e deve essere evitata. Inoltre, ogni indirizzo è un hash di una chiave pubblica, accompagnato da una checksum per ridurre il rischio di perdita di bitcoin.

Diversi prefissi vengono utilizzati per gli indirizzi Bitcoin. Ad esempio, BC1Q corrisponde a un indirizzo Segwit V0, BC1P a un indirizzo Taproot/Segwit V1, e i prefissi 1 e 3 sono associati agli indirizzi Pay2PublicKeyH/Pay2ScriptH (legacy). Nel prossimo corso, spiegheremo passo dopo passo la derivazione di un indirizzo da una chiave pubblica.

In sintesi, gli indirizzi di ricezione sono un elemento essenziale del sistema Bitcoin. Sono generati a partire da coppie di chiavi private e pubbliche, e servono per ricevere fondi su una moneta. Gli indirizzi integrano una checksum per ridurre i rischi di perdita di bitcoin e sono progettati per essere utilizzati in modo univoco, garantendo così la sicurezza e la riservatezza. Diversi tipi di indirizzi sono utilizzati nel sistema Bitcoin, offrendo una maggiore riservatezza e sicurezza.

## Come creare un indirizzo Bitcoin?

![Come creare un indirizzo Bitcoin?](https://youtu.be/ewMGTN8dKjI)

In questo capitolo, affronteremo la costruzione di un indirizzo di ricezione per le transazioni Bitcoin. Un indirizzo di ricezione è una rappresentazione sotto forma di caratteri alfanumerici di una chiave pubblica compressa. La conversione di una chiave pubblica in un indirizzo di ricezione passa attraverso diverse fasi.

Una delle caratteristiche vantaggiose degli indirizzi di ricezione è la presenza di una checksum, che consente la rilevazione degli errori. Per questo, utilizziamo la tecnologia di checksum BCH (Bose-Chaudhuri-Hocquenghem) che assicura una precisa rilevazione degli errori. Questa tecnologia contribuisce anche alla riduzione del numero di caratteri necessari per rappresentare un indirizzo, facilitandone così l'utilizzo.

Per iniziare la costruzione di un indirizzo, dobbiamo comprimere la corrispondente chiave pubblica. Una chiave pubblica grezza occupa 520 bit, ma grazie alla simmetria della curva ellittica utilizzata, una curva ellittica può avere un'ascissa x associata a due possibili valori per y: positivo o negativo. Sulla rete Bitcoin, lavoriamo con un campo di interi positivi finiti invece che con il campo dei reali. Per rappresentare una chiave pubblica a partire da x, aggiungiamo un prefisso che indica il valore di y (pari o dispari). La compressione di una chiave pubblica consente di ridurre la sua dimensione da 520 a 264 bit. La parità di y in un campo di interi positivi finiti corrisponde alla parità di y nel campo dei reali.
Prendiamo ad esempio la chiave pubblica di Satoshi Nakamoto, con un prefisso 0,3 che indica un valore dispari di y. Possiamo quindi passare alla seconda fase della costruzione di un indirizzo a partire da chiavi pubbliche compressi. È possibile calcolare due indirizzi per ogni chiave pubblica. Per fare ciò, utilizziamo la funzione SHA256 per ottenere il condensato (hash) della chiave pubblica. Successivamente, applichiamo la funzione ripemd160 al risultato di SHA256 per ottenere una sequenza di caratteri. Questa sequenza viene quindi codificata in formato binario per gruppi di 5 bit, ai quali vengono aggiunte le metadati per il calcolo della checksum utilizzando il programma BCH.

Nel caso degli indirizzi legacy, utilizziamo il doppio hash SHA256 per generare il checksum dell'indirizzo. Tuttavia, per gli indirizzi Segwit V0 e V1, utilizziamo la tecnologia di checksum BCH per garantire la rilevazione degli errori. Il programma BCH è in grado di suggerire e correggere gli errori con una probabilità di errore estremamente bassa. Attualmente, il programma BCH viene utilizzato per rilevare e suggerire le modifiche da apportare, ma non le effettua automaticamente al posto dell'utente. Il calcolo della checksum con il codice BCH si basa sull'aritmetica polinomiale di Chien-Chauffage.

Il programma BCH richiede diverse informazioni in input, tra cui l'HRP (Human Readable Part) che deve essere esteso. L'estensione dell'HRP consiste nel codificare ogni lettera in base 2, prendendo i primi tre bit di ogni carattere, inserendo un separatore 0 e concatenando gli ultimi cinque bit di ogni carattere. I caratteri blu convertiti in base 10 corrispondono a 3 e 3 in decimale, mentre gli altri cinque caratteri arancioni corrispondono a 2 e 3 in base 10. L'estensione dell'HRP in base 10 consente di isolare gli ultimi cinque bit di ogni carattere, rafforzando così la checksum.

La versione Segwit V0 è rappresentata dal codice 00 e il "payload" è in nero, in base 10. Ciò è seguito da sei caratteri riservati per la checksum. L'input contenente le metadati viene quindi sottoposto al programma BCH per ottenere la checksum in base 10. La concatenazione della versione, del payload e della checksum consente di costruire l'indirizzo. I caratteri in base 10 vengono quindi convertiti in caratteri bech32 utilizzando una tabella di corrispondenza. L'alfabeto bech32 comprende tutti i caratteri alfanumerici, ad eccezione di 1, b, i e o, per evitare confusione.
Per costruire un indirizzo che inizia con bc1q, dobbiamo applicare una funzione di hash (H160) a una chiave pubblica compressa, quindi aggiungere la checksum, la versione (q), l'HRP (bc) e il separatore (1). Gli indirizzi Taproot, invece, iniziano con bc1p perché la loro versione (Segwit V1) corrisponde a 0+1=1, da qui l'uso del carattere p. Tutti questi elementi vengono quindi convertiti in BCH32, una variante della base 32 specifica per Bitcoin.

Così abbiamo esaminato i passaggi per la costruzione di un indirizzo di ricezione, l'uso della tecnologia di checksum BCH e la costruzione di un indirizzo che inizia con bc1q o bc1p utilizzando la variante BCH32 della base 32 specifica per Bitcoin.

## Riepilogo della crittografia per i portafogli Bitcoin

![sintesi della formazione](https://youtu.be/NkAYoVUMvOs)

Durante questa formazione, abbiamo approfondito il portafoglio deterministico gerarchico (HD) con il BIP32. L'entropia gioca un ruolo centrale in questo tipo di portafoglio, poiché viene utilizzata per generare una frase mnemonica da un numero casuale. Grazie alla lista di 2048 parole fornita nel BIP39, questa frase mnemonica può essere codificata in una serie di parole facili da ricordare. La frase mnemonica, insieme a una eventuale passphrase, sono necessarie per generare il seed del portafoglio. La passphrase agisce come un sale crittografico che aggiunge un ulteriore livello di protezione al portafoglio.

La funzione pbkdf2 viene utilizzata per generare il seed dalla frase mnemonica e dalla passphrase, utilizzando un hmacha512 e 2048 iterazioni. La chiave master e il codice di catena master sono quindi derivati da questo seed utilizzando nuovamente la funzione hmacha512 con la frase "bitcoin seed". La chiave privata master e il codice di catena master sono gli elementi più alti nella gerarchia del portafoglio HD.
La derivazione di una chiave figlia dipende da diversi fattori, tra cui la chiave genitore e il corrispondente codice di catena. Una chiave estesa viene ottenuta concatenando una chiave genitore con il suo codice di catena, mentre una chiave principale è una chiave separata. Per derivare un indirizzo, la chiave pubblica compressa viene prima hashata utilizzando SHA256 e RIPMD160, quindi viene calcolato un checksum. Il doppio hash SHA256 viene utilizzato per calcolare il checksum nel caso di uno standard legacy, mentre il programma BCH (Bose-Chaudhuri-Hocquenghem) viene utilizzato per calcolare il checksum nel caso di uno standard segwit. Successivamente, viene utilizzata una rappresentazione in formato base 58 per uno standard legacy, mentre il formato bech32 viene utilizzato per uno standard segwit, al fine di ottenere l'indirizzo del portafoglio HD.

In sintesi, abbiamo esplorato in dettaglio le funzioni di hash e le loro caratteristiche, così come le firme digitali e le curve ellittiche. Successivamente, ci siamo immersi nell'universo del portafoglio deterministico gerarchico (HD) con il BIP32, utilizzando l'entropia e la passphrase per generare il seed del portafoglio. Abbiamo anche imparato come derivare le chiavi figlie e ottenere l'indirizzo del portafoglio HD. Speriamo che queste informazioni ti siano state utili e ti incoraggiamo ora a passare alla valutazione per testare le tue conoscenze acquisite durante la formazione Crypto 301. Grazie per la tua attenzione.

# Ringraziamenti e continua a scavare la tana del coniglio

Desideriamo ringraziarti sinceramente per aver seguito la formazione Crypto 301. Speriamo che questa esperienza sia stata arricchente e formativa per te. Abbiamo affrontato molti argomenti appassionanti, dalla matematica alla crittografia fino al funzionamento del protocollo Bitcoin.

Se desideri approfondire ulteriormente l'argomento, abbiamo una risorsa aggiuntiva da offrirti. Abbiamo realizzato un'intervista esclusiva con Théo Pantamis e Loïc Morel, due esperti rinomati nel campo della crittografia. Questa intervista esplora in profondità vari aspetti dell'argomento e offre prospettive interessanti.

Non esitare a guardare questa intervista per continuare a esplorare il fascinante campo della crittografia. Speriamo che ti sia utile e ispirante nel tuo percorso. Ancora una volta, grazie per la tua partecipazione e il tuo impegno durante tutta la formazione.

## Intervista con Théo Pantamis

![Intervista con Théo Pantamis](https://youtu.be/c9MvtGJsEvY)

Ecco un riassunto dell'intervista:

In questa intervista, Théo Pantamys, specializzato in matematica e appassionato di Bitcoin, Lightning Network e protocolli, condivide il suo percorso e le sue riflessioni su vari argomenti.
Théo ha scoperto Bitcoin nel 2009, ma il suo interesse si è sviluppato ulteriormente nel 2015-2016 grazie a divulgatori scientifici su YouTube. Si è concentrato sulla matematica e sulla crittografia di Bitcoin, nonché sul confronto con altri protocolli.

Sottolinea l'importanza della decentralizzazione in Bitcoin e come ciò vada contro l'autorità dello Stato, offrendo un'apertura del registro. Bitcoin risolve anche il problema della regolamentazione in modo efficace.

Théo affronta anche il tema della privacy in Bitcoin. Spiega l'importanza di CoinJoin per preservare la privacy degli utenti ed evitare la divulgazione di informazioni personali. Raccomanda l'uso di Wasabi e Whirlpool per migliorare l'anonimato delle transazioni.

Successivamente, Théo discute di RGB, un protocollo complesso che risolve i problemi tecnici di Bitcoin. Spiega come RGB utilizzi contratti discreti per creare token e prodotti finanziari mantenendo la validazione dello stato del contratto sulla blockchain Bitcoin.

La discussione continua sulla minaccia dell'informatica quantistica su Bitcoin. Théo menziona che sarebbero necessari circa cento qubit per rompere la maggior parte degli algoritmi e, al momento, i computer quantistici non hanno ancora raggiunto questo livello di potenza.

Per quanto riguarda il checksum degli indirizzi Bitcoin, Théo spiega come i codici BCH vengano utilizzati per rilevare e potenzialmente correggere gli errori di battitura. Sottolinea l'importanza del checksum per evitare la perdita di bitcoin e ottimizzare le dimensioni degli indirizzi.

In conclusione, Théo condivide risorse per approfondire la comprensione di Bitcoin, tra cui canali YouTube di divulgazione matematica, libri consigliati e spazi Twitter in cui gli sviluppatori discutono dei loro lavori.
