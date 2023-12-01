---
name: Introduzione alla crittografia
goal: Comprendere la creazione di un portafoglio Bitcoin dal punto di vista crittografico
objectives:
  - Svelare la terminologia crittografica legata ai Bitcoin.
  - Padroneggiare la creazione di un portafoglio Bitcoin.
  - Comprendere la struttura di un portafoglio Bitcoin.
  - Comprendere gli indirizzi e il percorso di derivazione.
---

# Un viaggio nel cuore della crittografia

Sei affascinato da Bitcoin? Ti chiedi come funziona un portafoglio Bitcoin? Preparati a intraprendere un viaggio avvincente nel cuore della crittografia! Loïc, il nostro esperto, ti guiderà attraverso i meandri della creazione di un portafoglio Bitcoin, svelando i misteri dietro i termini tecnici intimidatori come hash, derivazione delle chiavi e curve ellittiche.

Questo corso ti fornirà non solo le conoscenze per comprendere la struttura di un portafoglio Bitcoin, ma ti preparerà anche ad approfondire l'affascinante mondo della crittografia. Quindi, sei pronto per intraprendere questo viaggio? Unisciti a noi e trasforma la tua curiosità in competenza!

+++

# Introduzione

## Introduzione alla crittografia

### Questo corso è adatto a te? SÌ!

![introduzione di Rogzy](https://youtu.be/ul8zU5QWIXg)

È con grande piacere che ti diamo il benvenuto al nuovo corso intitolato "Crypto 301: Introduzione alla crittografia e al portafoglio HD", condotto dall'esperto in materia, Loïc Morel. Questo corso ti immergerà nell'affascinante mondo della crittografia, una disciplina fondamentale della matematica che assicura la crittografia e la sicurezza dei tuoi dati.

Nella nostra vita quotidiana e soprattutto nel campo dei Bitcoin, la crittografia svolge un ruolo primario. I concetti ad essa legati, come le chiavi private, pubbliche, gli indirizzi, i percorsi di derivazione, il seed e l'entropia, sono al centro dell'uso e della creazione di un portafoglio Bitcoin. Attraverso questo corso, Loïc ti spiegherà nel dettaglio come vengono create le chiavi private e come sono collegate agli indirizzi. Loïc dedicherà anche un'ora per spiegarti i dettagli matematici della curva ellittica, questa complessa curva matematica. Inoltre, capirai perché l'uso di HMAC SHA512 è importante per proteggere il tuo portafoglio e qual è la differenza tra il seed e la frase mnemonica.

L'obiettivo finale di questa formazione è permetterti di comprendere tecnicamente i processi di creazione di un portafoglio HD e i metodi crittografici utilizzati. Nel corso degli anni, i portafogli Bitcoin sono evoluti per diventare più facili da usare, più sicuri e standardizzati grazie a specifici BIP. Loïc ti aiuterà a comprendere questi BIP per capire le scelte dei sviluppatori di Bitcoin e dei crittografi. Come tutti i corsi offerti dalla nostra università, questo è completamente gratuito e open source. Ci auguriamo di ricevere i vostri feedback alla fine di questo emozionante corso.

### La parola è al professore!

![intro di Loïc](https://youtu.be/mwuxXLk4Kws)

Buongiorno a tutti, sono Loïc Morel, la vostra guida in questa esplorazione tecnica della crittografia utilizzata nei portafogli Bitcoin.

Il nostro viaggio inizia con una discesa negli abissi delle funzioni di hash crittografiche. Smontiamo insieme i meccanismi dell'indispensabile SHA256 ed esploriamo vari algoritmi dedicati alla derivazione.

Continueremo la nostra avventura svelando il misterioso mondo delle firme digitali. Scoprirete come la magia delle curve ellittiche si applica a queste firme e faremo luce su come calcolare la chiave pubblica dalla chiave privata. E naturalmente, affronteremo l'atto di firmare con la chiave privata.

Successivamente, faremo un salto indietro nel tempo per vedere l'evoluzione dei portafogli Bitcoin e ci addentreremo nei concetti di entropia e numeri casuali. Esamineremo la famosa frase mnemonica, aprendo anche una parentesi sulla passphrase. Avrete persino l'opportunità di vivere un'esperienza unica creando un seed da 128 lanci di dadi!

Con queste solide basi, saremo pronti per la parte cruciale: la creazione di un portafoglio Bitcoin. Dalla generazione del seed e della chiave master, passando allo studio delle chiavi estese, fino alla derivazione delle coppie di chiavi figlie, ogni passaggio sarà analizzato nel dettaglio. Discuteremo anche della struttura del portafoglio e dei percorsi di derivazione.

Per coronare il tutto, concluderemo il nostro percorso esaminando gli indirizzi Bitcoin. Spiegheremo come vengono creati e come svolgono un ruolo essenziale nel funzionamento dei portafogli Bitcoin.

Imbarcati con me in questo affascinante viaggio e preparati ad esplorare l'universo della crittografia come mai prima d'ora. Lascia i tuoi preconcetti alla porta e apri la tua mente a un nuovo modo di comprendere Bitcoin e la sua struttura fondamentale.

# Le funzioni di hash

## Introduzione alle funzioni di hash crittografiche relative a Bitcoin

![2.1 - les fonctions de hachage cryptographiques](https://youtu.be/dvnGArYvVr8)

Benvenuti alla nostra sessione odierna dedicata a un'immersione approfondita nel mondo crittografico delle funzioni di hash, una pietra angolare essenziale per la sicurezza del protocollo Bitcoin. Immaginate una funzione di hash come un robot crittografico ultra efficiente che trasforma informazioni di qualsiasi dimensione in un'impronta digitale unica e di dimensioni fisse, chiamata "hash". Nel corso della nostra esplorazione, dipingeremo il profilo delle funzioni di hash crittografiche, mettendo in luce il loro utilizzo nel protocollo Bitcoin e definendo gli obiettivi specifici che queste funzioni crittografiche devono raggiungere.

![image](assets/image/section1/0.JPG)

Dipingere il profilo delle funzioni di hash crittografiche richiede la comprensione di due qualità essenziali: la loro irreversibilità e la loro resistenza alla falsificazione. Ogni funzione di hash crittografica è come un artista unico, che produce un "hash" distintivo per ogni input. Anche un pennello che si devia leggermente altera notevolmente il quadro finale, cioè l'hash. Queste funzioni agiscono come sentinelle digitali, verificando l'integrità del software scaricato. Un'altra caratteristica cruciale che possiedono è la loro resistenza alle collisioni. Certamente, nell'universo dell'hashing, le collisioni sono inevitabili, ma una eccellente funzione di hash crittografica le riduce notevolmente. È come se ogni hash fosse una casa in una città immensa; nonostante il grande numero di case, una buona funzione di hash assicura che ogni casa abbia un indirizzo unico.

![image](assets/image/section1/1.JPG)

Navighiamo ora sulle acque tumultuose delle funzioni di hash obsolete. SHA0, SHA1 e MD5 sono oggi considerate come gusci arrugginiti nell'oceano dell'hashing crittografico. Sono spesso sconsigliate perché hanno perso la loro resistenza alle collisioni. Il principio delle cassettiere spiega perché, nonostante i nostri migliori sforzi, evitare le collisioni è impossibile a causa della limitazione della dimensione di output. È anche importante notare che la resistenza alla seconda preimmagine dipende dalla resistenza alle collisioni. Per essere considerata veramente sicura, una funzione di hash deve resistere alle collisioni, alla seconda preimmagine e alla preimmagine.

Elemento chiave nel protocollo Bitcoin, la funzione di hash SHA-256 è il capitano della nave. Altre funzioni, come SHA-512, vengono utilizzate per la derivazione con HMAC e PBKDF. Inoltre, RIPMD160 viene utilizzata per ridurre un'impronta a 160 bit. Quando parliamo di HASH256 e HASH160, ci riferiamo all'uso di un doppio hash con SHA-256 e RIPMD. L'uso di HASH160 è particolarmente vantaggioso perché consente di beneficiare della sicurezza di SHA-256 riducendo al contempo la dimensione dell'impronta.

In sintesi, l'obiettivo finale di una funzione di hash crittografica è trasformare un'informazione di dimensioni arbitrarie in un'impronta di dimensioni fisse. Per essere considerata sicura, deve avere diverse caratteristiche: irreversibilità, resistenza alla falsificazione, resistenza alle collisioni e resistenza alla seconda preimmagine.

![image](assets/image/section1/2.JPG)

Alla fine di questa esplorazione, abbiamo svelato i segreti delle funzioni di hash crittografiche, evidenziato il loro utilizzo nel protocollo Bitcoin e analizzato i loro obiettivi specifici. Abbiamo appreso che per essere considerate sicure, le funzioni di hash devono essere resistenti alla preimmagine, alla seconda preimmagine, alle collisioni e alla falsificazione. Abbiamo anche esaminato le diverse funzioni di hash utilizzate nel protocollo Bitcoin. Nella nostra prossima sessione, ci immergeremo nel cuore della funzione di hash SHA256 e scopriremo le affascinanti nozioni matematiche che le conferiscono le sue caratteristiche uniche.

## I meccanismi di SHA256

![I meccanismi di SHA256](https://youtu.be/74SWg_ZbUj4)

Benvenuti al seguito del nostro affascinante viaggio attraverso i labirinti crittografici della funzione di hash. Oggi sveliamo i misteri di SHA256, un processo complesso, ma ingegnoso che abbiamo introdotto nella nostra precedente discussione sulle funzioni di hash. Facciamo un passo avanti in questo labirinto, iniziando con il pre-processing di SHA256. Immaginate il pre-processing come la preparazione di un piatto gustoso, in cui aggiungiamo "bit di riempimento" per far sì che la dimensione del nostro ingrediente principale, l'input, raggiunga un multiplo perfetto di 512 bit. Tutto questo con l'obiettivo finale di generare un hash succulento di 256 bit da un ingrediente di dimensioni variabili.

![image](assets/image/section1/3.JPG)
![image](assets/image/section1/4.JPG)

Nella presente ricetta crittografica, giochiamo con i bit, avendo una dimensione di messaggio iniziale che chiameremo M. Un bit è riservato per il separatore, mentre P bit sono utilizzati per il padding. Inoltre, mettiamo da parte 64 bit per la seconda fase di pre-elaborazione. Il totale deve essere un multiplo di 512 bit. Un po' come assicurarsi che tutti gli ingredienti si armonizzino perfettamente nel nostro piatto.

![image](assets/image/section1/5.JPG)

Passiamo ora alla seconda fase di pre-elaborazione, che coinvolge l'aggiunta della rappresentazione binaria della dimensione del messaggio iniziale, in bit. Per fare ciò, utilizziamo i nostri 64 bit riservati durante il passaggio precedente. Aggiungiamo zeri per arrotondare i nostri 64 bit alla nostra input bilanciata. Successivamente, uniamo il messaggio iniziale, il padding dei bit e il padding della dimensione, come ingredienti in un frullatore, per ottenere il nostro input bilanciato.

![image](assets/image/section1/6.JPG)

Ora ci prepariamo per i primi passaggi del processo di hashing SHA-256. Come in ogni buona ricetta, abbiamo bisogno di alcuni ingredienti di base, che chiamiamo costanti e vettori di inizializzazione. I vettori di inizializzazione, da A a H, sono i primi 32 bit delle parti decimali delle radici quadrate dei primi 8 numeri primi. Le costanti K, da 0 a 63, rappresentano invece i primi 32 bit delle parti decimali delle radici cubiche dei primi 64 numeri primi.

![image](assets/image/section1/7.JPG)

All'interno della funzione di compressione, utilizziamo operatori specifici come XOR, AND e NOT. Elaboriamo i bit uno per uno in base alla loro posizione, utilizzando l'operatore XOR e una tabella di verità. L'operatore AND viene utilizzato per restituire 1 solo se entrambi gli operandi sono uguali a 1, e l'operatore NOT per restituire il valore opposto di un operando. Utilizziamo anche l'operazione SHR per spostare i bit verso destra secondo un numero scelto.

![image](assets/image/section1/8.JPG)
![image](assets/image/section1/9.JPG)

Infine, dopo aver separato l'input bilanciato in diversi blocchi di messaggi di 512 bit, eseguiamo 64 cicli di calcolo nella funzione di compressione. Come in una corsa ciclistica, ogni giro di pista migliora la nostra posizione. Aggiungiamo modulo 2^32 lo stato intermedio allo stato iniziale della funzione di compressione. Le addizioni nella funzione di compressione sono addizioni modulo 2^32 per contenere la dimensione delle somme a 32 bit.

![image](assets/image/section1/10.JPG)
![image](assets/image/section1/11.JPG)
![image](assets/image/section1/12.JPG)
![image](assets/image/section1/13.JPG)

Per concludere, vorremmo sottolineare il ruolo cruciale dei calcoli eseguiti nelle scatole CH, MAJ, σ0 e σ1. Queste operazioni, tra le altre, sono i guardiani che garantiscono la robustezza della funzione di hash SHA256 contro gli attacchi, rendendola una scelta preferita per la sicurezza di molti sistemi digitali, in particolare nel protocollo Bitcoin. È quindi evidente che, sebbene complessa, la bellezza di SHA256 risiede nella sua robustezza nel trovare l'input a partire dall'hash, mentre la verifica dell'hash per un determinato input è un'azione meccanicamente semplice.

## Gli algoritmi utilizzati per la derivazione

![Gli algoritmi utilizzati per la derivazione](https://youtu.be/ZF1_BMsOJXc)

Gli algoritmi di derivazione HMAC e PBKDF2 sono componenti chiave nella sicurezza del protocollo Bitcoin. Prevengono una varietà di potenziali attacchi e garantiscono l'integrità dei portafogli Bitcoin.

HMAC e PBKDF2 sono strumenti crittografici utilizzati per diverse operazioni in Bitcoin. HMAC è principalmente utilizzato per contrastare gli attacchi di estensione di lunghezza durante la derivazione dei portafogli deterministici gerarchicamente (HD), mentre PBKDF2 viene utilizzato per convertire una frase mnemonica in un seme.

![image](assets/image/section1/14.JPG)

HMAC, che prende un messaggio e una chiave come input, genera un output di dimensione fissa. Per garantire l'uniformità, la chiave viene adattata in base alle dimensioni dei blocchi utilizzati nella funzione di hash. Nella derivazione dei portafogli HD, viene utilizzato HMAC-SHA-512. Quest'ultimo funziona con blocchi di 1024 bit (128 byte) e adatta di conseguenza la chiave. Utilizza le costanti OPAD (0x5c) e IPAD (0x36), ripetute quante volte necessario per rafforzare la sicurezza.

Il processo di HMAC-SHA-512 implica la concatenazione del risultato di SHA-512 applicato alla chiave XOR OPAD e alla chiave XOR IPAD con il messaggio. Quando viene utilizzato con blocchi di 1024 bit (128 byte), la chiave di input viene completata con zeri se necessario, quindi XORata con IPAD e OPAD. La chiave così modificata viene quindi concatenata con il messaggio.

![image](assets/image/section1/15.JPG)

Il codice di concatenazione, integrando una fonte aggiuntiva di entropia, aumenta la sicurezza delle chiavi derivate. Senza di esso, un attacco potrebbe compromettere l'intero portafoglio e rubare tutti i bitcoin.

PBKDF2 viene utilizzato per convertire una frase mnemonica in un seme. Questo algoritmo esegue 2048 iterazioni utilizzando HMAC SHA512. Grazie a questi algoritmi di derivazione, due input diversi possono produrre un output unico e fisso, risolvendo il problema degli attacchi di estensione di lunghezza possibili sulle funzioni della famiglia SHA-2. Un attacco di estensione di lunghezza sfrutta una proprietà specifica di alcune funzioni di hash crittografiche. In un tale attacco, un attaccante che già possiede l'hash di un messaggio sconosciuto può utilizzarlo per calcolare l'hash di un messaggio più lungo, che è un'estensione del messaggio originale. Questo è spesso possibile senza conoscere il contenuto del messaggio originale, il che può portare a gravi vulnerabilità di sicurezza se questo tipo di funzione di hash viene utilizzato per compiti come la verifica dell'integrità.

![image](assets/image/section1/16.JPG)

In conclusione, gli algoritmi HMAC e PBKDF2 svolgono un ruolo essenziale nella sicurezza della derivazione dei portafogli HD nel protocollo Bitcoin. HMAC-SHA-512 viene utilizzato per proteggersi dagli attacchi di estensione di lunghezza, mentre PBKDF2 consente la conversione della frase mnemonica in un seme. Il codice di stringa aggiunge una fonte di entropia aggiuntiva nella derivazione delle chiavi, garantendo così la robustezza del sistema.

# Le firme digitali

## Firme digitali e curve ellittiche

![Firme digitali e curve ellittiche](https://youtu.be/gOjYiPkx4z8)

Nel mondo delle criptovalute, la sicurezza delle transazioni è fondamentale. Al centro del protocollo Bitcoin, troviamo l'uso di firme digitali che fungono da prove matematiche della proprietà di una chiave privata associata a una specifica chiave pubblica. Questa tecnica di protezione dei dati si basa essenzialmente su un affascinante campo della crittografia chiamato crittografia a curve ellittiche (ECC).

![image](assets/image/section2/0.JPG)

La crittografia a curve ellittiche è il fondamento della sicurezza delle transazioni Bitcoin. Queste curve ellittiche, che ricordano le curve matematiche studiate a scuola, sono utili in una varietà di applicazioni crittografiche, dalla scambio di chiavi alla crittografia asimmetrica alla creazione di firme digitali. Un dettaglio interessante che distingue le curve ellittiche è la loro simmetria: qualsiasi linea non verticale che taglia due punti della curva intersecherà un terzo punto.
Ora, approfondiamo un po': il protocollo Bitcoin utilizza una particolare curva ellittica chiamata SecP256K1 per eseguire le sue operazioni crittografiche. Questa curva, definita su un insieme finito di interi positivi modulo un numero primo di 256 bit, può essere visualizzata come un insieme di punti anziché come una curva tradizionale. È questa particolare progettazione che consente a Bitcoin di garantire in modo efficace le sue transazioni.

![image](assets/image/section2/1.JPG)

Per quanto riguarda la scelta della curva secp256k1 per Bitcoin, è interessante notare che è stata preferita alla curva secp256r1. Questa curva è definita dai parametri a=0 e b=7, e la sua equazione è y² = x³ + 7 modulo n, con n che rappresenta il numero primo che determina l'ordine della curva.

Quando si parla delle costanti utilizzate nel sistema Bitcoin, si fa generalmente riferimento ai parametri specifici dell'algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA) e del sistema di curve ellittiche utilizzato da Bitcoin, che è la curva secp256k1. Ecco questi parametri:

- campo primario (p): Bitcoin utilizza una curva su un campo primario, quindi p è il primo numero utilizzato per definire questo campo. Per la curva secp256k1, p è uguale a `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` in esadecimale o p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 in decimale.
- ordine della curva (n): Questo è il numero di punti sulla curva, incluso il punto all'infinito. Per secp256k1, n è uguale a `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` in esadecimale o n = 2^256 - 432420386565659656852420866394968145599 in decimale.
- punto generatore (G): Il punto base, o generatore, è il punto sulla curva da cui vengono generate tutte le altre chiavi pubbliche. Ha coordinate x e y specifiche, generalmente rappresentate in esadecimale. Per secp256k1, le coordinate G sono, in esadecimale:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

![image](assets/image/section2/2.JPG)

Nota che tutti i valori esadecimali sono generalmente rappresentati in base 16, mentre i valori decimali sono in base 10. Inoltre, tutte le operazioni su queste costanti vengono eseguite modulo p per le coordinate dei punti sulla curva e modulo n per le operazioni di chiave e firma.
Quindi, dove vengono conservati questi famosi bitcoin? Non in un portafoglio Bitcoin, come si potrebbe pensare. In realtà, un portafoglio Bitcoin conserva le chiavi private necessarie per dimostrare la proprietà dei bitcoin. I bitcoin stessi sono registrati sulla blockchain, un database decentralizzato che archivia tutte le transazioni.

Nel sistema Bitcoin, l'unità di conto è il bitcoin (nota la "b" minuscola). Quest'ultimo è divisibile fino a otto decimali, con la più piccola unità chiamata satoshi. Gli UTXO, o "Unspent Transaction Output", rappresentano le uscite di transazioni non spese appartenenti a un utente. Per spendere questi bitcoin, è necessario dimostrare la proprietà della chiave privata corrispondente alla chiave pubblica associata a ciascun UTXO.

Per garantire la sicurezza delle transazioni, Bitcoin utilizza due protocolli di firma digitale: ECDSA (Elliptic Curve Digital Signature Algorithm) e Schnorr. ECDSA è un protocollo di firma integrato in Bitcoin fin dal suo lancio nel 2009, mentre le firme di Schnorr sono state aggiunte più di recente, nel novembre 2021. Sebbene entrambi i protocolli si basino sulla crittografia a curve ellittiche e utilizzino meccanismi matematici simili, differiscono principalmente in termini di struttura della firma.

Prima di approfondire questi meccanismi di firma, è importante capire cosa sia una curva ellittica. Una curva ellittica è definita dall'equazione y² = x³ + ax + b. Ogni punto su questa curva ha una distintiva simmetria che è la chiave della sua utilità in crittografia.

Alla fine, diverse curve ellittiche sono riconosciute come sicure per l'uso crittografico. La più conosciuta è forse la curva secp256r1. Tuttavia, per Bitcoin, Satoshi Nakamoto ha optato per un'altra curva: la secp256k1.

Nella prossima sezione di questo corso, esamineremo più da vicino la chiave pubblica e la chiave privata per una comprensione approfondita della crittografia su curve ellittiche e dell'algoritmo di firma digitale. Sarà il momento di consolidare le tue conoscenze e capire come tutte queste informazioni si integrano per garantire la sicurezza del protocollo Bitcoin.

## Calcolare la chiave pubblica dalla chiave privata

![Calcolare la chiave pubblica dalla chiave privata](https://youtu.be/NJENwFU889Y)

Nella continuazione di questo corso, esamineremo i meccanismi delle chiavi pubbliche e private, due elementi cruciali del protocollo Bitcoin. Queste chiavi sono intrinsecamente legate dall'algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA). Comprenderle ci darà una profonda comprensione di come Bitcoin protegge le transazioni sulla sua piattaforma.

![image](assets/image/section2/3.JPG)
![image](assets/image/section2/4.JPG)

Per iniziare, immergiamoci nell'universo dell'algoritmo ECDSA. Bitcoin utilizza questo algoritmo di firma digitale per collegare le chiavi private e pubbliche. In questo sistema, la chiave privata è un numero casuale o pseudo-casuale di 256 bit. Il numero totale di possibilità per una chiave privata è teoricamente 2^256, ma nella realtà è leggermente inferiore. Per essere precisi, alcune chiavi private di 256 bit non sono valide per Bitcoin.

![image](assets/image/section2/5.JPG)

Per essere compatibile con Bitcoin, una chiave privata deve essere compresa tra 1 e n-1, dove n rappresenta l'ordine della curva ellittica. Ciò significa che il numero totale di possibilità per una chiave privata Bitcoin è quasi pari a 1,158 x 10^77. Per mettere le cose in prospettiva, è approssimativamente lo stesso numero di atomi presenti nell'universo osservabile. La chiave privata unica viene quindi utilizzata per determinare una chiave pubblica di 512 bit.

![image](assets/image/section2/6.JPG)

La chiave pubblica, indicata con K, è un punto sulla curva ellittica che deriva dalla chiave privata utilizzando operazioni di punti sulla curva. È importante notare che la funzione ECDSA è irreversibile, ovvero è impossibile recuperare la chiave privata dalla chiave pubblica. Questa irreversibilità è la pietra angolare della sicurezza del portafoglio Bitcoin.

La chiave pubblica è composta da due punti di 256 bit ciascuno, per un totale di 512 bit. Tuttavia, può essere compressa in un numero di 264 bit. Il punto G è il punto di partenza per calcolare tutte le chiavi pubbliche degli utenti del sistema.

![image](assets/image/section2/7.JPG)

Una delle proprietà notevoli delle curve ellittiche è che una linea che interseca la curva in due punti intersecherà anche un terzo punto, chiamato punto O. Questa proprietà viene utilizzata per determinare il punto U, che è l'opposto del punto O. L'aggiunta di un punto a se stesso viene fatta tracciando una tangente alla curva in quel punto, ottenendo così un nuovo punto unico chiamato j. Il prodotto scalare di un punto per n equivale ad aggiungere quel punto a se stesso n volte.

![image](assets/image/section2/8.JPG)

Queste operazioni sui punti di una curva ellittica sono alla base del calcolo delle chiavi pubbliche. Conoscendo la chiave privata, è facile calcolare la chiave pubblica. Tuttavia, conoscere la chiave pubblica non permette di calcolare la chiave privata, garantendo così la sicurezza del sistema Bitcoin. Infatti, la sicurezza delle chiavi pubbliche e private si basa sul problema del logaritmo discreto, una questione matematica complessa.

![image](assets/image/section2/9.JPG)

Nella nostra prossima lezione, esploreremo come viene realizzata una firma digitale utilizzando l'algoritmo ECDSA con una chiave privata per sbloccare i bitcoin. Restate sintonizzati per questa emozionante esplorazione del mondo delle criptovalute e della crittografia.

## Firmare con la chiave privata

![Firmare con la chiave privata](https://youtu.be/h2hIyGgPqkM)

Il processo di firma digitale è un metodo chiave per dimostrare di essere il detentore di una chiave privata senza doverla rivelare. Questo viene realizzato utilizzando l'algoritmo ECDSA, che comprende la determinazione di un nonce univoco, il calcolo di un numero specifico, V, e la creazione di una firma digitale composta da due parti, S1 e S2. È fondamentale utilizzare sempre un nonce univoco per evitare attacchi di sicurezza. Un esempio noto di ciò che può accadere quando questa regola non viene rispettata è il caso dell'hacking della PlayStation 3, che è stato compromesso a causa del riutilizzo del nonce.

In modo preciso, per validare una firma digitale utilizzando l'algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm), di solito sono coinvolte le seguenti fasi:

1. Verificare che i valori della firma, S1 e S2, siano nell'intervallo [1, n-1]. Se non è così, la firma è invalida.
2. Calcolare l'inverso di S2 mod n. Lo chiameremo u. Spesso viene calcolato come segue: u = (S2)^-1 mod n.
3. Calcolare H, che è il valore di hash del messaggio firmato.
4. Calcolare u1 = H _ u mod n e u2 = S1 _ u mod n.
5. Calcolare il punto P sulla curva ellittica utilizzando u1, u2 e la chiave pubblica K: P = u1*G + u2*K, dove G è il punto di generazione della curva.
6. Se P è il punto all'infinito, la firma è invalida.
7. Calcolare I = coordinata x di P mod n.
8. La firma è valida se I è uguale a S1.

![image](assets/image/section2/10.JPG)
![image](assets/image/section2/11.JPG)

È importante notare che ogni software può utilizzare diverse notazioni e alcune fasi possono essere combinate o riarrangiate, ma la logica di base è la stessa. Si noti inoltre che tutte le operazioni aritmetiche vengono eseguite nel campo finito definito dalla curva ellittica (mod n, dove n è l'ordine della curva). Come promemoria, la curva secp256k1 (utilizzata in Bitcoin) ha n = 2^256 - 432420386565659656852420866394968145599.
Per quanto riguarda la generazione di chiavi pubbliche e private, è essenziale familiarizzare con la curva ellittica e il punto generatore. Per ottenere una chiave pubblica, è necessario scegliere un numero casuale come chiave privata, spesso chiamato "nonce", e utilizzarlo nell'equazione della curva ellittica.

La curva ellittica è uno strumento potente per generare chiavi pubbliche e private sicure. Ad esempio, per ottenere la chiave pubblica 3G, si traccia una tangente al punto G, si calcola l'opposto di -G per ottenere 2G, quindi si somma G e 2G. Per effettuare una transazione, è necessario dimostrare di conoscere il numero 3 sbloccando i bitcoin associati alla chiave pubblica 3G.

Per creare una firma digitale e dimostrare di conoscere la chiave privata associata alla chiave pubblica 3G, si calcola prima un nonce, quindi il punto V associato a questo nonce (nell'esempio dato, è 4G). Successivamente, si calcola il punto T sommando la chiave pubblica 3G e il punto V, ottenendo così 7G.

![image](assets/image/section2/12.JPG)

La verifica di una firma digitale è un passaggio cruciale nell'utilizzo dell'algoritmo ECDSA, che consente di confermare l'autenticità di un messaggio firmato senza la necessità della chiave privata del mittente. Ecco come avviene in dettaglio:

Nel nostro esempio, abbiamo due valori importanti: T e V. T è un valore numerico (7 in questo esempio), e V è un punto sulla curva ellittica (rappresentato qui come 4G). Questi valori vengono prodotti durante la creazione della firma digitale e vengono successivamente inviati insieme al messaggio per consentire la verifica.

Quando il verificatore riceve il messaggio, riceverà anche questi due valori, T e V.

Ecco i passaggi che il verificatore seguirà per validare la firma:

1. Prima di tutto, calcolerà l'hash del messaggio, che chiameremo H.
2. Successivamente, calcolerà u1 e u2. Per farlo, utilizzerà le seguenti formule:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n'
     Dove S2 è la seconda parte della firma digitale, n è l'ordine della curva ellittica e (S2)^-1 è l'inverso di S2 mod n.3. Il verificatore calcolerà quindi un punto P' sulla curva ellittica utilizzando la formula: P' = u1 _ G + u2 _ K
   - G è il punto in cui è stata generata la curva
   - K è la chiave pubblica del mittente
3. Il verificatore calcolerà quindi I', che è semplicemente la coordinata x del punto P' modulo n.
4. Infine, il verificatore confermerà che I' è uguale a T. Se lo è, la firma è considerata valida. In caso contrario, la firma non è valida.

Questa procedura garantisce che solo il mittente con la chiave privata corrispondente possa aver prodotto una firma che superi questo processo di verifica.

In conclusione, la verifica di una firma digitale ECDSA è una procedura essenziale nelle transazioni Bitcoin. Essa garantisce che il messaggio firmato non sia stato alterato durante la trasmissione e che il mittente sia effettivamente il titolare della chiave privata. Questa tecnica di autenticazione digitale si basa su principi matematici complessi, in particolare sull'aritmetica a curva ellittica, mantenendo la riservatezza della chiave privata. Fornisce una solida base di sicurezza per le transazioni crittografiche.

Detto questo, la gestione di queste chiavi, così come la loro creazione, è un'altra questione chiave in Bitcoin. Come si genera una nuova coppia di chiavi? Come si organizza una moltitudine di chiavi in modo sicuro ed efficiente? Come recuperarle se necessario?

Per rispondere a queste domande ed approfondire la comprensione della sicurezza crittografica, il prossimo corso si concentrerà sul concetto di portafogli deterministici gerarchici (portafogli HD) e sull'uso di frasi mnemoniche. Questi meccanismi offrono modi eleganti per gestire in modo efficiente le chiavi delle criptovalute, migliorando al contempo la sicurezza e la recuperabilità.

# Il mnemonico

## Evoluzione dei portafogli Bitcoin

![Évolution des portefeuilles Bitcoin](https://youtu.be/6tmu1R9cXyk)

Il **Portafoglio Deterministico Gerarchico**, comunemente chiamato portafoglio HD, svolge un ruolo fondamentale nell'ecosistema delle criptovalute. Il termine "portafoglio" può sembrare fuorviante per coloro che sono nuovi in questo campo, poiché non implica la detenzione di denaro o valute. Si riferisce piuttosto a una collezione di chiavi crittografiche private derivate da una singola chiave madre, attraverso un ingegnoso processo di aritmetica algoritmica. Queste chiavi private, che hanno una lunghezza fissa di 256 bit, sono l'essenza stessa del possesso di criptovalute e sono talvolta indicate con il termine un po' più grezzo di "Just a Bunch Of Keys" (JBOC).

![image](assets/image/section3/0.JPG)

Tuttavia, la complessità della gestione di queste chiavi è compensata da un insieme di protocolli, chiamati Bitcoin Improvement Proposals (BIP). Queste proposte di miglioramento sono al centro della funzionalità e della sicurezza dei portafogli HD. Ad esempio, il [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lanciato nel 2012, ha rivoluzionato il modo in cui queste chiavi vengono generate e memorizzate, introducendo il concetto di chiavi derivate in modo deterministico e gerarchico. In questo modo, il processo di backup di queste chiavi è notevolmente semplificato, pur mantenendo il loro livello di sicurezza.

![image](assets/image/section3/1.JPG)

Successivamente, il [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) ha introdotto un'innovazione significativa: la frase mnemonica di 24 parole. Questo sistema ha permesso di trasformare una sequenza complessa di numeri, difficile da ricordare, in una serie di parole comuni, molto più facili da memorizzare e conservare. Inoltre, il [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) ha proposto di aggiungere una frase aggiuntiva - passphrase, per rafforzare la sicurezza delle singole chiavi. Questi miglioramenti successivi hanno portato agli standard BIP43 e BIP44, che hanno standardizzato la struttura e la gerarchia dei portafogli HD, rendendo questi portafogli più accessibili e facili da usare per il pubblico.

Nelle sezioni seguenti, approfondiremo il funzionamento dei portafogli HD. Esamineremo i principi di derivazione delle chiavi e esamineremo i concetti fondamentali di entropia e generazione di numeri casuali, che sono essenziali per garantire la sicurezza del tuo portafoglio HD.
In sintesi, è essenziale sottolineare il ruolo centrale di BIP32 e BIP39 nella progettazione e sicurezza dei portafogli HD. Questi protocolli consentono di generare una moltitudine di chiavi da un unico seed, che dovrebbe essere un numero casuale o pseudo-casuale. Oggi, queste norme sono adottate dalla maggior parte dei portafogli di criptovalute, che siano dedicati a una singola criptovaluta o supportino diversi tipi di valute.

Spero che questa introduzione vi abbia aiutato a comprendere meglio le basi del portafoglio HD e le sue diverse caratteristiche. Il nostro obiettivo è aiutarvi a padroneggiare questi concetti essenziali e a navigare in modo più efficiente nel complesso mondo delle criptovalute. Quindi, rimanete con noi mentre continuiamo ad esplorare le sottigliezze e le sfumature di questo affascinante mondo nelle prossime lezioni.

## Entropia e numero casuale

![Entropia e numero casuale](https://youtu.be/k18yH18w2TE)

L'importanza della sicurezza delle chiavi private nell'ecosistema del Bitcoin è indiscutibile. Sono infatti la base che garantisce la sicurezza delle transazioni Bitcoin. Per evitare qualsiasi vulnerabilità legata alla prevedibilità, queste chiavi devono essere generate in modo veramente casuale, il che può rapidamente rivelarsi un compito laborioso per l'utente. Una soluzione a questo enigma è il Portafoglio Deterministico Gerarchico, o portafoglio HD. Questo metodo consente di generare in modo deterministico e gerarchico coppie di chiavi figlie da un'unica informazione alla base del portafoglio. È qui che il casuale si rivela indispensabile per garantire la sicurezza delle chiavi derivate.

![image](assets/image/section3/2.JPG)

La generazione di numeri casuali è infatti un elemento cruciale in crittografia, per garantire l'integrità delle chiavi private. Per prevenire qualsiasi vulnerabilità legata alla prevedibilità, una chiave privata deve essere prodotta in modo casuale. L'uso di una nuova coppia di chiavi per ogni transazione contribuisce ulteriormente a rafforzare la sicurezza, anche se ciò complica il loro backup e preserva solo parzialmente la riservatezza. In sintesi, la sicurezza delle chiavi private è una priorità assoluta, che richiede una generazione rigorosa e casuale. I portafogli HD offrono una soluzione per facilitare la generazione e la gestione delle chiavi mantenendo un alto livello di sicurezza.
Tuttavia, la generazione di numeri casuali sui computer rappresenta una sfida, poiché i risultati ottenuti non sono veramente casuali. Pertanto, è essenziale utilizzare un Generatore di Numeri Casuali (RNG). I tipi di RNG variano, dai Generatori di Numeri Pseudo-Casuali (PRNG) ai Generatori di Numeri Veramente Casuali (TRNG), così come i PRNG che integrano una sorgente di entropia.
![image](assets/image/section3/3.JPG)

Nel caso del Bitcoin, le chiavi private vengono generate da un'unica informazione alla base del portafoglio. Questa informazione consente una derivazione deterministica e gerarchica delle coppie di chiavi figlie. L'entropia è la base di ogni portafoglio HD, anche se non esiste uno standard per la generazione di questo numero casuale. Pertanto, la generazione di numeri casuali è una questione di grande importanza per garantire la sicurezza delle transazioni Bitcoin.

La fase di verifica della generazione delle chiavi è cruciale per garantire la sicurezza e l'autenticità della generazione di numeri casuali, un passaggio fondamentale per prevenire qualsiasi vulnerabilità associata alla prevedibilità. Pertanto, è fortemente consigliabile utilizzare portafogli open source per consentire questa verifica.

Tuttavia, è importante notare che alcuni hardware wallet possono essere "closed source", rendendo impossibile la verifica della generazione del numero casuale. Un possibile workaround sarebbe generare la propria frase mnemonica utilizzando dei dadi, anche se questo approccio potrebbe comportare alcuni rischi.

![image](assets/image/section3/4.JPG)

L'utilizzo di una passphrase generata casualmente può contribuire ad attenuare questi rischi.

Un esempio di applicazione di questo metodo è l'opzione "dice roll" offerta da CoinKit per generare frasi mnemoniche. Un'altra possibilità sarebbe utilizzare un'informazione iniziale molto ampia e ridurre questa informazione a 256 bit con la funzione di hash SHA-256, in grado di generare un buon numero casuale. È importante menzionare che la funzione di hash SHA-256 è resistente alle collisioni, alla falsificazione e agli attacchi di pre-immagine e seconda pre-immagine.

In definitiva, il casuale occupa un posto centrale nella crittografia e nell'informatica, e la capacità di generare casualità in modo sicuro è cruciale per garantire la sicurezza delle chiavi private e delle transazioni Bitcoin. L'entropia, che è al centro del portafoglio HD di Bitcoin, è essenziale per la sua sicurezza. Nella nostra prossima lezione, continueremo ad esplorare questo argomento, approfondendo ulteriormente il modo in cui l'entropia contribuisce alla sicurezza dei portafogli HD.

## La frase mnemonica

![La frase mnemonica](https://youtu.be/uJERqH9Xp7I)

La sicurezza di un portafoglio Bitcoin è una preoccupazione principale per tutti i suoi utenti. Un modo essenziale per garantire il backup del portafoglio è generare una frase mnemonica basata sull'entropia e sul checksum.

![image](assets/image/section3/5.JPG)

L'entropia è il fondamento della sicurezza del portafoglio HD. Ci sono diversi metodi per generare questa entropia, tra cui generatori di numeri pseudo-casuali (PRNG), generatori di numeri casuali veri (TRNG) o manualmente. È cruciale che questa entropia sia casuale o pseudo-casuale per garantire la sicurezza del portafoglio.

![image](assets/image/section3/6.JPG)

La checksum, d'altra parte, garantisce la verifica dell'esattezza della frase di recupero. Senza questa checksum, un errore nella frase potrebbe portare alla creazione di un portafoglio diverso e quindi alla perdita dei fondi. La checksum viene ottenuta passando l'entropia attraverso la funzione SHA256 e recuperando i primi 8 bit dell'hash.

Esistono diversi standard per la frase mnemonica in base alla dimensione dell'entropia. Lo standard più comunemente utilizzato per una frase di recupero di 24 parole è un'entropia di 256 bit. La dimensione della checksum è determinata dividendo la dimensione dell'entropia per 32.

Ad esempio, un'entropia di 256 bit genera una checksum di 8 bit. La concatenazione dell'entropia e della checksum porta quindi a dimensioni rispettive di 128 bit, 160 bit, ecc. In base alla dimensione dell'entropia, la frase di recupero avrà 12 parole per 128 bit, 15 parole per 160 bit e 24 parole per 256 bit.

![image](assets/image/section3/7.JPG)

Per trasformare i bit in frasi, ogni segmento è associato a una parola da una lista di 2048 parole. È importante precisare che nessuna parola presenta le prime quattro lettere nello stesso ordine.

È essenziale salvare la frase di recupero di 24 parole per preservare l'integrità del portafoglio Bitcoin. I due standard più comunemente utilizzati si basano su un'entropia di 128 o 256 bit e una concatenazione di 12 o 24 parole. L'aggiunta di una passphrase costituisce un'opzione aggiuntiva per rafforzare la sicurezza del portafoglio.

In conclusione, la generazione di una frase mnemonica per proteggere un portafoglio Bitcoin è un processo cruciale. È importante rispettare gli standard della frase mnemonica in base alla dimensione dell'entropia. Il backup della frase di recupero di 24 parole è essenziale per prevenire qualsiasi perdita di fondi. Vi ringraziamo per l'attenzione e vi diamo appuntamento per il nostro prossimo corso sulla criptovaluta.

## La passphrase

![La passphrase](https://youtu.be/dZkOYO7MXwc)

La passphrase è una parola ( o un insieme di parole) aggiuntiva che può essere integrata in un portafoglio Bitcoin per aumentarne la sicurezza. Il suo utilizzo è opzionale e dipende dalla discrezione dell'utente. Aggiungendo informazioni arbitrarie che, insieme alla frase mnemonica, consentono di calcolare il seed del portafoglio, la passphrase rafforza la sua sicurezza.

![image](assets/image/section3/8.JPG)

Per derivare le chiavi di un portafoglio HD, sono necessarie la frase mnemonica e la passphrase. La passphrase è libera e può raggiungere una dimensione quasi infinita. Non è inclusa nella frase mnemonica, che è standardizzata e deve seguire determinati vincoli di dimensione, checksum e codifica. Un attaccante non può accedere ai bitcoin di un utente senza conoscere la passphrase. Quest'ultima svolge un ruolo nella costruzione e nel calcolo di tutte le chiavi del portafoglio.

La funzione pbkdf2 viene utilizzata per generare il seed dalla passphrase. Questo seed consente di derivare tutte le coppie di chiavi figlie del portafoglio. Se la passphrase viene modificata, il portafoglio Bitcoin diventa completamente diverso.

La passphrase è uno strumento essenziale per rafforzare la sicurezza dei portafogli Bitcoin. Può consentire l'applicazione di diverse strategie di sicurezza. Ad esempio, può essere utilizzata per creare duplicati e facilitare il backup della frase mnemonica. Può inoltre migliorare la sicurezza del portafoglio attenuando i rischi associati alla generazione casuale della frase mnemonica.

Una passphrase efficace dovrebbe essere lunga (da 20 a 40 caratteri) e diversificata (utilizzando maiuscole, minuscole, numeri e simboli). Non dovrebbe essere direttamente legata all'utente o al suo ambiente. È più sicuro utilizzare una sequenza casuale di caratteri piuttosto che una semplice parola come passphrase.

![image](assets/image/section3/9.JPG)

Una passphrase è più sicura di una semplice password. La passphrase ideale è lunga, variegata e casuale. Può rafforzare la sicurezza di un portafoglio o di un hot wallet. Può anche essere utilizzata per creare backup ridondanti e sicuri.

È fondamentale prendersi cura dei backup della passphrase per evitare di perdere l'accesso al portafoglio. Una passphrase è un'opzione per un portafoglio HD. Può essere generata casualmente con dadi o un altro generatore di numeri pseudo-casuali. Non è consigliabile memorizzare una passphrase o una frase mnemonica.

Nel nostro prossimo corso, esamineremo in dettaglio il funzionamento del seed e la prima coppia di chiavi generate da esso. Non esitate a seguire questo corso per continuare il vostro apprendimento. Non vediamo l'ora di rivedervi molto presto.

# Creazione dei portafogli Bitcoin

## Creazione del seed e della chiave master

![Création de la graine et de la clé maîtresse](https://youtu.be/56yAt_JDWhY)

In questa parte del corso, esploreremo i passaggi per la derivazione di un portafoglio HD (Hierarchical Deterministic Wallet), che consente di creare e gestire chiavi private e pubbliche in modo gerarchico.

![image](assets/image/section4/0.JPG)

La base del portafoglio HD si basa su due elementi essenziali: la frase mnemonica e la passphrase. Insieme, costituiscono il seed, una sequenza alfanumerica di 512 bit che serve come base per derivare le chiavi del portafoglio. Da questo seed, è possibile derivare tutte le coppie di chiavi figlie del portafoglio Bitcoin. Il seed è la chiave per accedere a tutti i bitcoin associati al portafoglio, che tu utilizzi o meno una passphrase.

Per ottenere il seed, viene utilizzata la funzione pbkdf2 (Password-Based Key Derivation Function 2) con la frase mnemonica e la passphrase. L'output di pbkdf2 è un seed di 512 bit. La chiave privata maestra e il codice di catena maestra vengono determinati utilizzando l'algoritmo HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Questo algoritmo richiede un messaggio e una chiave per generare un risultato. La chiave privata maestra viene calcolata a partire dal seed e dalla frase "Bitcoin SEED". Questa frase è identica per tutte le derivazioni del portafoglio HD, garantendo così coerenza tra i portafogli.

![image](assets/image/section4/1.JPG)

Inizialmente, la funzione SHA-512 non era implementata nel protocollo Bitcoin, motivo per cui viene utilizzato HMAC SHA-512. L'utilizzo di HMAC SHA-512 con la frase "Bitcoin SEED" vincola l'utente a generare un portafoglio specifico per Bitcoin. Il risultato di HMAC SHA-512 è un numero di 512 bit, diviso in due parti: i 256 bit a sinistra rappresentano la chiave privata maestra, mentre i 256 bit a destra rappresentano il codice di catena maestra.

La chiave privata maestra è la chiave genitore di tutte le future chiavi del portafoglio, mentre il codice di catena maestra è coinvolto nella derivazione delle chiavi figlie. È importante notare che è impossibile derivare una coppia di chiavi figlie senza conoscere il codice di catena corrispondente della coppia genitore. Il codice di catena aggiunge una fonte di entropia nel processo di derivazione.

Una coppia di chiavi nel portafoglio comprende una chiave privata, una chiave pubblica e un codice di catena. Il codice di catena consente di introdurre una fonte di casualità nella derivazione delle chiavi figlie e di isolare ogni coppia di chiavi per evitare eventuali falle di informazioni.

![image](assets/image/section4/2.JPG)

È importante sottolineare che la chiave privata master è la prima chiave privata derivata dal seed e non ha alcun collegamento con le chiavi estese del portafoglio. Il seed è quindi l'elemento fondamentale per derivare tutte le chiavi del portafoglio. Se avete aggiunto una o più passphrase, anche queste saranno fondamentali per la derivazione delle chiavi del portafolio.
Nella prossima lezione, esploreremo in dettaglio le chiavi estese, come xPub, xPRV, zPub, e capiremo perché vengono utilizzate e come vengono costruite.

## Le chiavi estese

![Le chiavi estese](https://youtu.be/TRz760E_zUY)

In questa parte del corso, studieremo le chiavi estese (xPub, zPub, yPub) e i loro prefissi, che svolgono un ruolo importante nella derivazione delle chiavi figlie in un portafoglio HD (Hierarchical Deterministic Wallet).

![image](assets/image/section4/3.JPG)

Le chiavi estese si distinguono dalle chiavi master. Un portafoglio HD genera una frase mnemonica e un seed per ottenere la chiave master e il codice di catena master. Le chiavi estese vengono utilizzate per derivare le chiavi figlie e richiedono sia la chiave genitore che il corrispondente codice di catena. Una chiave estesa combina queste due informazioni per semplificare il processo di derivazione.

Le chiavi estese sono identificate da prefissi specifici (XPRV, XPUB, YPUB, ZPUB) che indicano se si tratta di una chiave estesa privata o pubblica, nonché il suo scopo specifico. I metadati associati a una chiave estesa includono la versione (prefisso), la profondità, l'impronta digitale della chiave pubblica, l'indice e il payload (codice di catena e chiave genitore).

![image](assets/image/section4/4.JPG)

Il payload è composto dal codice di catena (32 byte) e dalla chiave genitore (33 byte). Questi elementi sono essenziali per la derivazione delle chiavi figlie. Una chiave privata viene generata da un numero casuale o pseudo-casuale, mentre una chiave pubblica viene generata utilizzando l'algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm).

Ogni coppia di chiavi estese è associata a un codice di catena univoco, che consente di effettuare derivazioni specifiche. Concatenando la chiave genitore con il codice di catena, si ottiene una chiave estesa privata o pubblica.

![image](assets/image/section4/5.JPG)

Le chiavi pubbliche estese possono essere derivate solo dalle normali chiavi pubbliche figlie, mentre le chiavi private estese possono essere derivate dalle chiavi pubbliche e private figlie, sia in una derivazione normale che indurita - hardened. L'uso delle chiavi estese con il prefisso XPUB consente di derivare nuovi indirizzi senza risalire alle corrispondenti chiavi private, offrendo una maggiore sicurezza. I metadati associati alle chiavi estese forniscono informazioni importanti sul loro ruolo e sulla loro posizione nella gerarchia delle chiavi.

Le chiavi pubbliche compressate hanno una dimensione di 33 byte, mentre le chiavi pubbliche non elaborate sono di 512 bit. Le chiavi pubbliche compressate conservano le stesse informazioni delle chiavi non elaborate, ma con una dimensione ridotta. Le chiavi estese hanno una dimensione di 82 byte e il loro prefisso è rappresentato in base 58 tramite una conversione in esadecimale. Il checksum viene calcolato utilizzando la funzione di hash HASH256.

![image](assets/image/section4/6.JPG)

Le derivazioni rafforzate iniziano dagli indici che sono potenze di 2 (2^31). Le chiavi pubbliche estese consentono solo la derivazione di chiavi pubbliche figlie normali, mentre le chiavi private estese consentono di derivare qualsiasi chiave figlia. È interessante notare che i prefissi più comunemente utilizzati sono xpub e zpub, che corrispondono rispettivamente agli standard legacy e segwit v1 e segwit v0.

Nella nostra prossima lezione, esamineremo la derivazione delle coppie di chiavi figlie utilizzando le conoscenze acquisite sulle chiavi estese e la chiave master del portafoglio.

In conclusione, le chiavi estese svolgono un ruolo essenziale nella crittografia e nel funzionamento dei portafogli HD. Comprendere il loro utilizzo e il loro calcolo è cruciale per garantire la sicurezza delle transazioni e la protezione degli asset digitali. I prefissi e i metadati associati alle chiavi estese consentono un utilizzo efficiente e una derivazione precisa delle chiavi figlie necessarie.

## Derivazione delle coppie di chiavi figlie

![Derivazione delle coppie di chiavi figlie](https://youtu.be/FXhI-GmE9Aw)

Ora affronteremo il calcolo del seed e della chiave master, che sono i primi elementi essenziali per la gerarchizzazione e la derivazione del portafoglio HD (Hierarchical Deterministic Wallet). Il seed, di lunghezza compresa tra 128 e 256 bit, viene generato in modo casuale o da una frase segreta. Gioca un ruolo deterministico nella derivazione di tutte le altre chiavi. La chiave master è la prima chiave derivata dal seed e consente di derivare tutte le altre coppie di chiavi figlie.

Il codice della catena principale svolge un ruolo importante nel recupero del portafoglio dalla seed. È importante notare che tutte le chiavi derivate dalla stessa seed avranno lo stesso codice della catena principale.

![image](assets/image/section4/7.JPG)

La gerarchizzazione e la derivazione del portafoglio HD offrono una gestione più efficiente delle chiavi e delle strutture del portafoglio. Le chiavi estese consentono la derivazione di una coppia di chiavi figlie da una coppia genitore utilizzando calcoli matematici e algoritmi specifici.

Esistono diversi tipi di coppie di chiavi figlie, tra cui chiavi rinforzate e chiavi normali. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, sia in modalità normale che rinforzata. Ogni coppia di chiavi ha un indice che consente di differenziarle l'una dall'altra.

![image](assets/image/section4/8.JPG)

La derivazione delle chiavi figlie utilizza la funzione HMAC-SHA512 utilizzando la chiave genitore concatenata all'indice e al codice della catena associato alla coppia di chiavi. Le chiavi figlie normali hanno un indice compreso tra 0 e 2 alla potenza 31 meno 1, mentre le chiavi figlie rinforzate hanno un indice compreso tra 2 alla potenza 31 e 2 alla potenza 32 meno 1.

![image](assets/image/section4/9.JPG)
![image](assets/image/section4/10.JPG)

Esistono due tipi di coppie di chiavi figlie: coppie rinforzate e coppie normali. Il processo di derivazione delle chiavi figlie utilizza le chiavi pubbliche per generare le condizioni di spesa, mentre le chiavi private vengono utilizzate per la firma. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, in modalità normale o rinforzata.

![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)

La derivazione rinforzata utilizza la chiave privata genitore, mentre la derivazione normale utilizza la chiave pubblica genitore. La funzione HMAC-SHA512 viene utilizzata per la derivazione rinforzata, mentre la derivazione normale utilizza un condensato di 512 bit. La chiave pubblica figlia viene ottenuta moltiplicando la chiave privata figlia per il generatore della curva ellittica.

![image](assets/image/section4/13.JPG)
![image](assets/image/section4/14.JPG)

## Struttura del portafoglio e percorsi di derivazione

![Struttura del portafoglio e percorsi di derivazione](https://youtu.be/etO9UxwyE2I)

In questo capitolo, studieremo la struttura dell'albero di derivazione in un portafoglio HD (Hierarchical Deterministic Wallet). Abbiamo già esplorato il calcolo del seed, la chiave master e la derivazione delle coppie di chiavi figlie. Ora ci concentreremo sull'organizzazione delle chiavi all'interno del portafoglio.

Il portafoglio HD utilizza livelli di profondità per organizzare le chiavi. Ogni derivazione da una coppia genitore a una coppia figlia corrisponde a un livello di profondità. Il livello di profondità 0 corrisponde alla chiave master e al codice di catena master.

![immagine](assets/image/section4/15.JPG)

- Il livello di profondità 1 viene utilizzato per derivare chiavi figlie secondo un obiettivo specifico, determinato dall'indice. Gli obiettivi sono conformi agli standard BIP 84 e Segwit v0/v1.

- Il livello di profondità 2 consente di distinguere i conti di diverse criptovalute o reti. Ciò consente di organizzare il portafoglio in base alle diverse fonti di fondi.

- Il livello di profondità 3 viene utilizzato per organizzare il portafoglio in diversi account, offrendo una struttura più chiara e organizzata.

- Il livello di profondità 4 corrisponde alle catene interne ed esterne, utilizzate per gli indirizzi destinati a essere comunicati pubblicamente. L'indice 0 è associato alla catena esterna, mentre l'indice 1 è associato alla catena interna. Ogni account ha due catene: la catena esterna (0) e la catena interna (1). Il livello di profondità 4 viene anche utilizzato per gestire i tipi di script nel caso dei portafogli multi firma.

- Il livello di profondità 5 viene utilizzato per gli indirizzi di ricezione su un portafoglio classico. Nella prossima sezione, esamineremo più nel dettaglio la derivazione delle coppie di chiavi figlie.

![immagine](assets/image/section4/16.JPG)

Per ogni livello di profondità, utilizziamo indici per distinguere le coppie di chiavi figlie. Gli indici potenziati vengono utilizzati con un apostrofo per alcune derivazioni. La chiave pubblica per anno viene utilizzata come input per la funzione HMAC. L'indice in un percorso di derivazione indica il valore utilizzato nella funzione HMAC.

L'indice senza apostrofo corrisponde all'indice reale utilizzato, mentre l'indice con apostrofo corrisponde all'indice reale + 2^31. Le derivazioni migliorate utilizzano indici da 2^31 a 2^32-1. Ad esempio, l'indice 44' corrisponde all'indice reale 2^31 + 44.

Per generare un indirizzo di ricezione specifico, si ricava una coppia di chiavi figlio dalla chiave master e dal codice stringa master. L'indice viene quindi utilizzato per distinguere tra diverse coppie di chiavi figlio della stessa profondità.

Le chiavi estese, come XPUB, consentono di condividere il portafoglio con più persone. La catena di derivazione viene utilizzata per distinguere tra la catena esterna (indirizzi destinati alla comunicazione) e la catena interna (indirizzi di scambio).

È importante notare che in un portafoglio HD vengono utilizzate profondità diverse a seconda dei diversi standard. La derivazione delle chiavi padre da chiavi figlio consente all'utente di passare da una profondità all'altra. L'uso di diversi rami nel portafoglio HD indica i diversi standard seguiti.

Nel prossimo capitolo vedremo gli indirizzi di ricezione, i vantaggi del loro utilizzo e le fasi della loro costruzione.

# Cos'è un indirizzo Bitcoin?

## Indirizzi Bitcoin

Indirizzi Bitcoin (https://youtu.be/nqGBMjPtFNI)

In questo capitolo esploreremo gli indirizzi di ricezione, che svolgono un ruolo cruciale nel sistema Bitcoin. Essi consentono di ricevere fondi su una moneta e sono generati da coppie di chiavi private e pubbliche. Sebbene esista un tipo di script chiamato Pay2PublicKey che può essere utilizzato per bloccare i bitcoin su una chiave pubblica, gli utenti preferiscono generalmente utilizzare gli indirizzi di ricezione piuttosto che questo script.

![immagine](assets/image/section5/0.JPG)

Quando un destinatario desidera ricevere bitcoin, fornisce al mittente un indirizzo di ricezione anziché la propria chiave pubblica. Un indirizzo è in realtà un hash di una chiave pubblica, con un formato specifico. La chiave pubblica è derivata dalla chiave privata del bambino utilizzando operazioni matematiche come l'aggiunta e il raddoppio di punti su curve ellittiche.

![immagine](assets/image/section5/1.JPG)

È importante notare che non è possibile risalire dall'indirizzo alla chiave pubblica o dalla chiave pubblica alla chiave privata. L'uso di un indirizzo riduce la dimensione delle informazioni della chiave pubblica, che inizialmente è di 512 bit. È possibile comprimere una chiave pubblica mantenendo solo il valore di x e aggiungendo un prefisso, ma questa tecnica non era nota al momento della creazione di Bitcoin. L'utilizzo di un indirizzo non consente quindi di risparmiare spazio nei blocchi.

Gli indirizzi Bitcoin sono stati ridotti in dimensione per facilitarne l'uso. Hanno un checksum, che consente di rilevare errori di battitura e ridurre i rischi di perdita di bitcoin. Al contrario, le chiavi pubbliche non hanno un checksum, il che significa che gli errori di battitura possono portare alla perdita dei fondi corrispondenti.

Gli indirizzi offrono anche un secondo livello di sicurezza tra le informazioni pubbliche e private, rendendo più difficile il controllo della chiave privata. Le funzioni di hash utilizzate consentono alle coppie di chiavi di resistere ad eventuali attacchi da parte di computer quantistici. Infatti, questi computer possono potenzialmente rompere l'ECDSA (Elliptic Curve Digital Signature Algorithm), ma non possono rompere una funzione di hash.

È essenziale sottolineare che ogni indirizzo è a uso unico, il che contribuisce alla sicurezza e alla privacy. Il riutilizzo dello stesso indirizzo comporta gravi problemi di privacy e deve essere evitato. Inoltre, ogni indirizzo è un hash di una chiave pubblica, accompagnato da un checksum per ridurre il rischio di perdita di bitcoin.

Diversi prefissi vengono utilizzati per gli indirizzi Bitcoin. Ad esempio, BC1Q corrisponde a un indirizzo Segwit V0, BC1P a un indirizzo Taproot/Segwit V1, e i prefissi 1 e 3 sono associati agli indirizzi Pay2PublicKeyH/Pay2ScriptH (legacy). Nel prossimo corso, spiegheremo passo dopo passo la derivazione di un indirizzo da una chiave pubblica.

In sintesi, gli indirizzi di ricezione sono un elemento essenziale del sistema Bitcoin. Sono generati da coppie di chiavi private e pubbliche e servono per ricevere fondi su una transazione. Gli indirizzi includono una checksum per ridurre i rischi di perdita di bitcoin e sono progettati per essere utilizzati in modo univoco, garantendo così sicurezza e privacy. Vengono utilizzati diversi tipi di indirizzi nel sistema Bitcoin, offrendo una maggiore privacy e sicurezza.

## Come creare un indirizzo Bitcoin?

![Come creare un indirizzo Bitcoin?](https://youtu.be/ewMGTN8dKjI)

In questo capitolo, affronteremo la creazione di un indirizzo di ricezione per le transazioni Bitcoin. Un indirizzo di ricezione è una rappresentazione in forma di caratteri alfanumerici di una chiave pubblica compressa. La conversione di una chiave pubblica in un indirizzo di ricezione passa attraverso diverse fasi.

![immagine](assets/image/section5/3.JPG)

Una delle caratteristiche vantaggiose degli indirizzi di ricezione è la presenza di una checksum, che consente la rilevazione degli errori. A tal scopo, utilizziamo la tecnologia di checksum BCH (Bose-Chaudhuri-Hocquenghem) che garantisce una precisa rilevazione degli errori. Questa tecnologia contribuisce anche a ridurre il numero di caratteri necessari per rappresentare un indirizzo, facilitandone così l'uso.

Per iniziare la costruzione di un indirizzo, dobbiamo comprimere la corrispondente chiave pubblica. Una chiave pubblica grezza occupa 520 bit, ma grazie alla simmetria della curva ellittica utilizzata, una curva ellittica può avere un'ascissa x associata a due possibili valori per y: positivo o negativo. Nella rete Bitcoin, lavoriamo con un campo di interi positivi finiti anziché con il campo dei reali. Per rappresentare una chiave pubblica a partire da x, aggiungiamo un prefisso che indica il valore di y (pari o dispari). La compressione di una chiave pubblica consente di ridurne la dimensione da 520 a 264 bit. La parità di y in un campo di interi positivi finiti corrisponde alla parità di y nel campo dei reali.

![image](assets/image/section5/4.JPG)
![image](assets/image/section5/5.JPG)

Prendiamo ad esempio la chiave pubblica appartenente a Satoshi Nakamoto, con un prefisso 0,3 che indica un valore dispari di y. Possiamo quindi passare alla seconda fase della costruzione di un indirizzo a partire da chiavi pubbliche compressate. È possibile calcolare due indirizzi per ogni chiave pubblica. Per farlo, utilizziamo la funzione SHA256 per ottenere il condensato (hash) della chiave pubblica. Successivamente, applichiamo la funzione ripemd160 al risultato di SHA256 per ottenere una sequenza di caratteri. Questa sequenza viene quindi codificata in formato binario per gruppi di 5 bit, a cui vengono aggiunti metadati per il calcolo della checksum utilizzando il programma BCH.

![image](assets/image/section5/6.JPG)

Nel caso degli indirizzi legacy, utilizziamo il doppio hash SHA256 per generare la somma di controllo dell'indirizzo. Tuttavia, per gli indirizzi Segwit V0 e V1, facciamo affidamento sulla tecnologia di checksum BCH per garantire la rilevazione degli errori. Il programma BCH è in grado di suggerire e correggere gli errori con una probabilità di errore estremamente bassa. Attualmente, il programma BCH viene utilizzato per rilevare e suggerire modifiche da apportare, ma non le esegue automaticamente al posto dell'utente. Il calcolo della checksum con il codice BCH si basa sull'aritmetica polinomiale di Chien-Chauffage.

![image](assets/image/section5/7.JPG)

Il programma BCH richiede diverse informazioni in input, tra cui l'HRP (Human Readable Part) che deve essere esteso. L'estensione dell'HRP consiste nel codificare ogni lettera in base 2, prendendo i primi tre bit di ogni carattere inserendo un separatore 0 e concatenando gli ultimi cinque bit di ogni carattere. I caratteri blu convertiti in base 10 corrispondono a 3 e 3 in decimale, mentre gli altri cinque caratteri arancioni corrispondono a 2 e 3 in base 10. L'estensione del HRP in base 10 consente di isolare gli ultimi cinque bit di ogni carattere, rafforzando così il checksum.

![image](assets/image/section5/8.JPG)

La versione Segwit V0 è rappresentata dal codice 00 e il "payload" è in nero, in base 10. Segue poi sei caratteri riservati per il checksum. L'input contenente i metadati viene quindi sottoposto al programma BCH per ottenere il checksum in base 10. La concatenazione della versione, del payload e della checksum consente di costruire l'indirizzo. I caratteri in base 10 vengono poi convertiti in caratteri bech32 utilizzando una tabella di corrispondenza. L'alfabeto bech32 comprende tutti i caratteri alfanumerici, ad eccezione di 1, b, i e o, per evitare confusione.

![image](assets/image/section5/9.JPG)
![image](assets/image/section5/10.JPG)

Per costruire un indirizzo che inizia con bc1q, è necessario applicare una funzione di hash (H160) a una chiave pubblica compressa, quindi aggiungere la checksum, la versione (q), l'HRP (bc) e il separatore (1). Gli indirizzi Taproot, invece, iniziano con bc1p perché la loro versione (Segwit V1) corrisponde a 0+1=1, da cui l'uso del carattere p. Tutti questi elementi vengono poi convertiti in BCH32, una variante della base 32 specifica per Bitcoin.

Pertanto, abbiamo esaminato i passaggi per la costruzione di un indirizzo di ricezione, l'uso della tecnologia di checksum BCH e la costruzione di un indirizzo che inizia con bc1q o bc1p utilizzando la variante BCH32 della base 32 specifica per Bitcoin.

## Riepilogo della crittografia per i portafogli Bitcoin

![sintesi della formazione](https://youtu.be/NkAYoVUMvOs)

Durante questa formazione, abbiamo approfondito il portafoglio deterministico gerarchico (HD) con il BIP32. L'entropia svolge un ruolo centrale in questo tipo di portafoglio, poiché viene utilizzata per generare una frase mnemonica da un numero casuale. Grazie alla lista di 2048 parole fornite nel BIP39, questa frase mnemonica può essere codificata in una serie di parole facili da ricordare. La frase mnemonica, insieme a una eventuale passphrase, sono necessarie per generare il seed del portafoglio. La passphrase agisce come un sale crittografico che aggiunge un ulteriore livello di protezione al portafoglio.

![image](assets/image/section5/11.JPG)

La funzione pbkdf2 viene utilizzata per generare il seed dalla frase mnemonica e dalla passphrase, utilizzando un hmacha512 e 2048 iterazioni. La chiave master e il codice di catena master vengono quindi derivati da questo seed utilizzando nuovamente la funzione hmacha512 con la frase "bitcoin seed". La chiave privata master e il codice di catena master sono gli elementi più alti nella gerarchia del portafoglio HD.

![image](assets/image/section5/12.JPG)

La derivazione di una chiave figlia dipende da diversi fattori, tra cui la chiave genitore e il corrispondente codice di catena. Una chiave estesa viene ottenuta concatenando una chiave genitore con il suo codice di catena, mentre una chiave master è una chiave separata. Per derivare un indirizzo, la chiave pubblica compressa viene prima hashata utilizzando SHA256 e RIPMD160, quindi viene calcolato una checksum. L'hash doppio SHA256 viene utilizzato per calcolare la checksum nel caso di uno standard legacy, mentre il programma BCH (Bose-Chaudhuri-Hocquenghem) viene utilizzato per calcolare la checksum nel caso di uno standard segwit. Successivamente, viene utilizzata una rappresentazione in formato base 58 per uno standard legacy, mentre il formato bech32 viene utilizzato per uno standard segwit, al fine di ottenere l'indirizzo del portafoglio HD.

![image](assets/image/section5/13.JPG)

In sintesi, abbiamo esplorato in dettaglio le funzioni di hash e le loro caratteristiche, così come le firme digitali e le curve ellittiche. Successivamente, ci siamo immersi nell'universo del portafoglio deterministico gerarchico (HD) con il BIP32, utilizzando l'entropia e la passphrase per generare il seed del portafoglio. Abbiamo anche imparato come derivare le chiavi figlie e ottenere l'indirizzo del portafoglio HD. Spero che queste informazioni ti siano state utili e ti incoraggio ora a procedere con la valutazione per testare le tue conoscenze acquisite durante il corso Crypto 301. Grazie per l'attenzione.

# Vai oltre

## Creazione di un seed da 128 lanci di dadi!

![Creazione di un seed da 128 lanci di dadi!](https://youtu.be/lUw-1kk75Ok)

La creazione di una frase mnemonica è un passaggio cruciale per la sicurezza del tuo portafoglio di criptovalute. Ci sono diversi metodi per generare una frase mnemonica, tuttavia, ci concentreremo sul metodo di generazione manuale utilizzando dei dadi. È importante sottolineare che questo metodo non è adatto per un portafoglio di grande valore. Si consiglia di utilizzare un software open source o un portafoglio hardware per generare la frase mnemonica. Per creare una frase mnemonica, useremo dei dadi per generare un'informazione binaria. L'obiettivo è capire il processo di creazione della frase mnemonica.

**Passaggio 1 - Preparazione:**
Assicurati di avere una distribuzione Linux amnesica, come Tails OS, installata su una chiavetta USB per maggiore sicurezza. Nota che questo tutorial non dovrebbe essere utilizzato per creare un portafoglio principale.

**Passaggio 2 - Generazione di un numero binario casuale:**
Useremo dei dadi per generare un'informazione binaria. Lancia un dado 128 volte e annota ogni risultato (1 per dispari, 0 per pari).

**Passaggio 3 - Organizzazione dei numeri binari:**
Organizza i numeri binari ottenuti in righe di 11 cifre per facilitare i calcoli successivi. La dodicesima riga dovrebbe avere solo 7 cifre.

**Passaggio 4 - Calcolo del checksum:**
Le ultime 4 cifre per la dodicesima riga corrispondono al checksum. Per calcolare questa checksum, è necessario utilizzare un terminale di una distribuzione Linux. Si consiglia di utilizzare [TailOs](https://tails.boum.org/index.fr.html) che è una distribuzione senza memoria (al riavvio dimentica tutto quello che è stato fatto in precedenza) avviabile da una chiavetta USB. Una volta sul tuo terminale, inserisci il comando `echo <numero binario> | shasum -a 254 -0`. Sostituisci `<numero binario>` con la tua lista di 128 zeri e uni. L'output sarà un hash in esadecimale. Prendi il primo carattere di questo hash e convertilo in binario. Puoi aiutarti con questa [tabella](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table). Aggiungi il checksum in binario (4 cifre) alla dodicesima riga del tuo foglio.

**Passaggio 5 - Conversione in decimale:**
Per trovare le parole associate a ciascuna delle tue righe, devi prima convertire in decimale ogni serie di 11 bit. Qui non puoi utilizzare un convertitore online perché questi bit rappresentano la tua frase mnemonica. Quindi dovrai convertire utilizzando una calcolatrice e un trucco che ti spiegherò: ogni bit è associato a una potenza di 2, quindi da sinistra a destra abbiamo 11 posizioni che corrispondono rispettivamente a 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Per convertire la tua serie di 11 bit in decimale, devi semplicemente sommare le posizioni che contengono un 1. Ad esempio, per la serie 00110111011, corrisponde alla seguente somma: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Ora puoi convertire ogni riga in decimale. E prima di passare alla codifica in parole, devi aggiungere +1 a tutte le righe perché l'indice della lista delle parole BIP39 parte da 1 e non da 0.

**Passaggio 8 - Generazione della frase mnemonica:**
Inizia stampando la [lista delle 2048 parole](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) per convertire i tuoi numeri decimali nelle parole del BIP39. La particolarità di questa lista è che nessuna parola ha le prime 4 lettere in comune con tutte le altre parole di questo dizionario. Quindi cerca per ciascuna delle tue righe la parola associata al numero decimale.
**Passaggio 9 - Test della frase mnemonica:**
Testa immediatamente la tua frase mnemonica su Sparrow Wallet creando un portafoglio da essa. Se ottieni un errore di checksum non valido, è probabile che tu abbia commesso un errore di calcolo. Correggi questo errore ripartendo dal passaggio 4 e testa nuovamente su Sparrow Wallet. Ecco! Hai appena creato un nuovo portafoglio Bitcoin lanciando 128 dadi.

Generare una frase mnemonica è un processo importante per proteggere il tuo portafoglio di criptovaluta. Si consiglia di utilizzare metodi più sicuri, come l'uso di software open source o di un hardware wallet, per generare la frase mnemonica. Tuttavia, completando questo workshop, si comprende meglio come a partire da un numero casuale si possa creare un portafoglio Bitcoin.

## BONUS: Intervista con Théo Pantamis

![Intervista con Théo Pantamis](https://youtu.be/c9MvtGJsEvY)

## Conclusioni e fine

### Ringraziamenti e continua a scavare la tana del coniglio

Noi desideriamo ringraziarvi sinceramente per aver seguito il corso Crypto 301. Speriamo che questa esperienza sia stata arricchente e formativa per voi. Abbiamo affrontato molti argomenti interessanti, dalla matematica alla crittografia fino al funzionamento del protocollo Bitcoin.

Se desiderate approfondire ulteriormente l'argomento, abbiamo una risorsa aggiuntiva da offrirvi. Abbiamo realizzato un'intervista esclusiva con Théo Pantamis e Loïc Morel, due esperti rinomati nel campo della crittografia. Questa intervista esplora in profondità vari aspetti dell'argomento e offre prospettive interessanti.

Non esitate a guardare questa intervista per continuare ad esplorare l'affascinante campo della crittografia. Speriamo che vi sia utile e fonte di ispirante nel vostro percorso. Ancora una volta, grazie per la vostra partecipazione e impegno durante tutto il corso.

### Sostienici

Questo corso, così come l'intero contenuto presente su questa università, vi è stato offerto gratuitamente dalla nostra comunità. Per sostenerci, potete condividerlo con gli altri, diventare membri dell'università e persino contribuire al suo sviluppo tramite GitHub. A nome di tutto il team, grazie!

### Valuta il corso

Un sistema di valutazione per il corso sarà presto integrato in questa nuova piattaforma di E-learning! Nel frattempo, grazie mille per aver seguito il corso e se l'avete apprezzato, pensate di condividerlo con gli altri.
