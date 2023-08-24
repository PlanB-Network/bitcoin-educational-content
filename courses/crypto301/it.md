---
name: Introduzione alla crittografia
goal: Comprendere la creazione di un portafoglio Bitcoin dal punto di vista crittografico
objectives:
  - Svelare la terminologia crittografica legata a Bitcoin.
  - Padroneggiare la creazione di un portafoglio Bitcoin.
  - Comprendere la struttura di un portafoglio Bitcoin.
  - Comprendere gli indirizzi e il percorso di derivazione.
---

# Un viaggio nel cuore della crittografia

**Attenzione: questo corso è stato completamente tradotto dall'IA e non è ancora stato revisionato. Se si desidera farlo, si prega di contribuire a [github](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/main/courses/crypto301).**

Sei affascinato da Bitcoin? Ti chiedi come funziona un portafoglio Bitcoin? Preparati per un viaggio avvincente nel cuore della crittografia! Loïc, il nostro esperto, ti guiderà attraverso i meandri della creazione di un portafoglio Bitcoin, svelando i misteri dietro i termini tecnici intimidatori come hash, derivazione delle chiavi e curve ellittiche.

Questo corso ti fornirà non solo le conoscenze per comprendere la struttura di un portafoglio Bitcoin, ma ti preparerà anche ad approfondire l'affascinante universo della crittografia. Quindi, sei pronto per intraprendere questo viaggio? Unisciti a noi e trasforma la tua curiosità in competenza!

+++

# Introduzione alla crittografia

![introduzione di Rogzy](https://youtu.be/ul8zU5QWIXg)

È con grande piacere che ti diamo il benvenuto al nuovo corso intitolato "Crypto 301: Introduzione alla crittografia e al portafoglio HD", organizzato dall'esperto in materia, Loïc Morel. Questo corso ti immergerà nell'affascinante mondo della crittografia, una disciplina fondamentale della matematica che garantisce la crittografia e la sicurezza dei tuoi dati.

Nella nostra vita quotidiana e soprattutto nel campo dei Bitcoin, la crittografia svolge un ruolo primario. I concetti ad essa legati, come le chiavi private, pubbliche, gli indirizzi, i percorsi di derivazione, il seed e l'entropia, sono al centro dell'uso e della creazione di un portafoglio Bitcoin. Attraverso questo corso, Loïc ti spiegherà nel dettaglio come vengono create le chiavi private e come sono collegate agli indirizzi. Loïc dedicherà anche un'ora per spiegarti i dettagli matematici della curva ellittica. Inoltre, capirai perché l'uso di HMAC SHA512 è importante per proteggere il tuo portafoglio e qual è la differenza tra seed e frase mnemonica.
I but ultimi di questa formazione sono di permetterti di comprendere tecnicamente i processi di creazione di un portafoglio HD e i metodi crittografici utilizzati. Nel corso degli anni, i portafogli Bitcoin sono evoluti per diventare più facili da usare, più sicuri e standardizzati grazie a specifici BIP. Loïc ti aiuterà a comprendere questi BIP per capire le scelte dei sviluppatori di Bitcoin e dei crittografi. Come tutti i corsi offerti dalla nostra università, questo è completamente gratuito e open source. Ci auguriamo di ricevere i vostri feedback alla fine di questo corso appassionante.
![intro par loïc](https://youtu.be/mwuxXLk4Kws)

Buongiorno a tutti, sono Loïc Morel, la vostra guida in questa esplorazione tecnica della crittografia utilizzata nei portafogli Bitcoin.

Il nostro viaggio inizia con una discesa nelle profondità delle funzioni di hash crittografiche. Smontiamo insieme i meccanismi dell'indispensabile SHA256 ed esploriamo vari algoritmi dedicati alla derivazione.

Continueremo la nostra avventura svelando il misterioso mondo delle firme digitali. Scoprirete come la magia delle curve ellittiche si applica a queste firme e faremo luce su come calcolare la chiave pubblica dalla chiave privata. E naturalmente, affronteremo il processo di firma digitale.

Successivamente, faremo un salto indietro nel tempo per vedere l'evoluzione dei portafogli Bitcoin e ci addentreremo nei concetti di entropia e numeri casuali. Faremo una panoramica sulla famosa frase mnemonica, aprendo anche una parentesi sulla passphrase. Avrete persino l'opportunità di vivere un'esperienza unica creando un seed da 128 lanci di dadi!

Con queste solide basi, saremo pronti per la parte cruciale: la creazione di un portafoglio Bitcoin. Dalla generazione del seed e della chiave master, passando allo studio delle chiavi estese, fino alla derivazione delle coppie di chiavi figlie, ogni passo sarà analizzato nel dettaglio. Discuteremo anche della struttura del portafoglio e dei percorsi di derivazione.

Per coronare il tutto, concluderemo il nostro percorso esaminando gli indirizzi Bitcoin. Spiegheremo come vengono creati e come svolgono un ruolo essenziale nel funzionamento dei portafogli Bitcoin.

Imbarcati con me in questo viaggio avvincente e preparati ad esplorare l'universo della crittografia come mai prima d'ora. Lascia le tue preconcetti alla porta e apri la tua mente a un nuovo modo di comprendere Bitcoin e la sua struttura fondamentale.

# Le funzioni di hash

## Introduzione alle funzioni di hash crittografiche relative a Bitcoin

![2.1 - le funzioni di hash crittografiche](https://youtu.be/dvnGArYvVr8)
Benvenuti alla nostra sessione odierna dedicata a un'immersione approfondita nel mondo crittografico delle funzioni di hash, una pietra angolare essenziale per la sicurezza del protocollo Bitcoin. Immaginate una funzione di hash come un robot crittografico ultra efficiente che trasforma informazioni di qualsiasi dimensione in un'impronta digitale unica e di dimensione fissa, chiamata "hash", "impronta" o "condensato".
In sintesi, una funzione di hash prende in input un messaggio di dimensione arbitraria e lo converte in un'impronta di dimensione fissa in output.

Descrivere il profilo delle funzioni di hash crittografiche richiede la comprensione di due qualità essenziali: la loro irreversibilità e la loro resistenza alla falsificazione.

L'irreversibilità o la resistenza alla preimmagine significa che il calcolo dell'output conoscendo l'input può essere facilmente eseguito, ma il calcolo a partire dall'output per recuperare l'input è impossibile.
È una funzione unidirezionale.

![image](assets/image/section1/0.JPG)

La resistenza alla falsificazione deriva dal fatto che anche la più piccola modifica dell'input produrrà un output profondamente diverso.
Queste funzioni consentono di verificare l'integrità dei software scaricati.

![image](assets/image/section1/1.JPG)

Un'altra caratteristica cruciale che possiedono è la loro resistenza alle collisioni e alla seconda preimmagine. Una collisione si verifica quando due input distinti producono lo stesso output.
Certamente, nell'universo dell'hashing, le collisioni sono inevitabili, ma una eccellente funzione di hash crittografica le riduce considerevolmente. Il rischio deve essere così basso da poter essere considerato nullo. È come se ogni hash fosse una casa in una città immensa; nonostante il numero enorme di case, una buona funzione di hash garantisce che ogni casa abbia un indirizzo unico.
La resistenza alla seconda preimmagine dipende dalla resistenza alle collisioni; se c'è resistenza alle collisioni, allora c'è resistenza alla seconda preimmagine.
Dato un input imposto, è necessario trovare un secondo input, diverso dal primo, che produca una collisione sull'hash in output della funzione. La resistenza alla seconda preimmagine è simile alla resistenza alle collisioni, tranne per il fatto che l'input è imposto.
Navighiamo tra le onde tumultuose delle funzioni hash obsolete. SHA0, SHA1 e MD5 sono ormai considerati scafi arrugginiti nell'oceano dell'hashing crittografico. Spesso sono sconsigliate perché hanno perso la loro resistenza alle collisioni. Il principio del cassetto spiega perché, nonostante i nostri sforzi, evitare le collisioni è impossibile a causa della dimensione limitata dell'output. Per essere veramente considerata sicura, una funzione hash deve essere resistente alle collisioni, alla seconda preimmagine e alla preimmagine.

Elemento chiave del protocollo Bitcoin, la funzione hash SHA-256 è il capitano della nave. Altre funzioni, come SHA-512, sono utilizzate per la derivazione con HMAC e PBKDF. Inoltre, RIPMD160 viene utilizzata per ridurre un'impronta digitale a 160 bit. Quando parliamo di HASH256 e HASH160, ci riferiamo all'uso di un doppio hash con SHA-256 e RIPMD.

Per HASH256, si parla di un doppio hash del messaggio utilizzando la funzione SHA256.

$$
SHA256(SHA256(messaggio))
$$

Per HASH160, il messaggio viene sottoposto a un doppio hash utilizzando la funzione SHA256 e poi RIPMD160.

$$
RIPMD160(SHA256(messaggio))
$$

L'uso di HASH160 è particolarmente vantaggioso perché consente di beneficiare della sicurezza di SHA-256 riducendo al contempo le dimensioni dell'impronta digitale.

In sintesi, l'obiettivo finale di una funzione hash crittografica è quello di trasmettere informazioni di dimensioni arbitrarie in un'impronta digitale di dimensioni fisse. Per essere riconosciuta come sicura, deve avere diverse corde al suo arco: irreversibilità, resistenza alla falsificazione, resistenza alle collisioni e resistenza alla seconda pre-immagine.

![immagine](assets/image/section1/2.JPG)

Alla fine di questa esplorazione, abbiamo demistificato le funzioni hash crittografiche, evidenziato il loro utilizzo nel protocollo Bitcoin e analizzato i loro obiettivi specifici. Abbiamo imparato che per essere considerate sicure, le funzioni hash devono essere resistenti alla preimmagine, alla seconda preimmagine, alla collisione e alla falsificazione. Abbiamo anche analizzato la gamma di funzioni hash utilizzate nel protocollo Bitcoin. Nella prossima sessione ci immergeremo nel cuore della funzione hash SHA256 e scopriremo l'affascinante matematica che le conferisce caratteristiche uniche.

## Il funzionamento di SHA256

Il funzionamento di SHA256](https://youtu.be/74SWg_ZbUj4)

Benvenuti alla continuazione del nostro affascinante viaggio nei labirinti crittografici della funzione hash. Oggi sveliamo i misteri di SHA256, un processo complesso ma ingegnoso che abbiamo introdotto in precedenza.
Per ricordare, lo scopo della funzione di hash SHA256 è prendere un messaggio in input di qualsiasi dimensione e generare in output un hash di 256 bit.

### Pre-elaborazione

Facciamo un passo avanti in questo labirinto, iniziando con la pre-elaborazione di SHA256.

#### Bit di riempimento

L'obiettivo di questo primo passaggio è avere un messaggio allineato su un multiplo di 512 bit. Per farlo, aggiungeremo dei bit di riempimento al messaggio.

Sia M la dimensione del messaggio iniziale.
Sia 1 un bit riservato per il separatore.
Sia P il numero di bit utilizzati per il riempimento e 64 il numero di bit messi da parte per la seconda fase di pre-elaborazione.
Il totale deve essere un multiplo di 512 bit, che rappresenta n.

![image](assets/image/section1/3.JPG)

Esempio con un messaggio in input di 950 bit:

```
Passo 1: Determinare la dimensione; il numero finale di bit ideale.
Il primo multiplo di 512 > (M + 64 + 1) (con M = 950) è 1024.
1024 = 2 * 512
Quindi n = 2.

Passo 2: Determinare P, il numero di bit di riempimento necessari per raggiungere il numero finale di bit ideale.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 940 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Quindi sarà necessario aggiungere 9 bit di riempimento per avere un messaggio allineato su un multiplo di 512.
```

E adesso?
Subito dopo il messaggio iniziale, è necessario aggiungere il separatore 1 seguito da P che nel nostro esempio è uguale a nove 0.

```
messaggio + 1 000 000 000
```

#### Riempimento della dimensione

Passiamo ora alla seconda fase della pre-elaborazione, che coinvolge l'aggiunta della rappresentazione binaria della dimensione del messaggio iniziale, in bit.

Riprendiamo l'esempio con un input di 950 bit:

```
La rappresentazione binaria del numero 950 è: 11 1011 0110

Utilizziamo i nostri 64 bit riservati durante il passaggio precedente. Aggiungiamo zeri per arrotondare i nostri 64 bit alla nostra input bilanciato. Poi uniamo il messaggio iniziale, il riempimento dei bit e il riempimento della dimensione, per ottenere il nostro input bilanciato.
```

Ecco il risultato:

![image](assets/image/section1/4.JPG)

### Elaborazione

#### Prerequisiti di comprensione

##### Le costanti e i vettori di inizializzazione

À present, ci stiamo preparando per i primi passaggi del trattamento della funzione SHA-256. Come in ogni buona ricetta, abbiamo bisogno di alcuni ingredienti di base, che chiamiamo costanti e vettori di inizializzazione.
I vettori di inizializzazione, da A a H, sono i primi 32 bit delle parti decimali delle radici quadrate dei primi 8 numeri primi. Saranno utilizzati come valori di base nei primi passaggi del trattamento. I loro valori sono in formato esadecimale.

Le costanti K, da 0 a 63, rappresentano invece i primi 32 bit delle parti decimali delle radici cubiche dei primi 64 numeri primi. Vengono utilizzate in ogni ciclo della funzione di compressione. Anche i loro valori sono in formato esadecimale.

![image](assets/image/section1/5.JPG)

##### Le operazioni utilizzate

All'interno della funzione di compressione, utilizziamo operatori specifici come XOR, AND e NOT. I bit vengono elaborati uno per uno in base alla loro posizione, utilizzando l'operatore XOR e una tabella di verità. L'operatore AND viene utilizzato per restituire 1 solo se entrambi gli operandi sono uguali a 1, mentre l'operatore NOT restituisce il valore opposto di un operando. Utilizziamo anche l'operazione SHR per spostare i bit verso destra di un numero scelto.

La tabella di verità:

![image](assets/image/section1/6.JPG)

Le operazioni di spostamento dei bit:

![image](assets/image/section1/7.JPG)

#### La funzione di compressione

Prima di applicare la funzione di compressione, dividiamo l'input in blocchi di 512 bit. Ogni blocco viene trattato indipendentemente dagli altri.

Ogni blocco di 512 bit viene quindi suddiviso in pezzi W di 32 bit. In questo modo, W(0) rappresenta i primi 32 bit del blocco di 512 bit. W(1) rappresenta i successivi 32 bit e così via fino ad arrivare ai 512 bit del blocco.

Una volta definiti tutte le costanti K e i pezzi W, possiamo elaborare i seguenti calcoli per ogni pezzo W in ogni ciclo.

Effettuiamo 64 cicli di calcolo nella funzione di compressione. All'ultimo ciclo, avremo uno stato intermedio che verrà sommato allo stato iniziale della funzione di compressione al livello dell'"Output della funzione".

Successivamente, ripetiamo tutti questi passaggi della funzione di compressione sul successivo blocco di 512 bit, fino all'ultimo blocco.

Tutte le somme nella funzione di compressione sono somme modulo 2^32 per mantenere sempre una somma a 32 bit.

![image](assets/image/section1/9.JPG)

![image](assets/image/section1/8.JPG)

##### Un ciclo della funzione di compressione

![image](assets/image/section1/11.JPG)

![image](assets/image/section1/10.JPG)
Il tour della funzione di compressione verrà eseguito 64 volte. In input troviamo i nostri pezzi W e le nostre costanti K definite in precedenza.
I quadrati/croci rossi corrispondono a un'addizione modulo 2^32 bit.

Gli input A, B, C, D, E, F, G, H saranno associati a un valore di 32 bit per un totale di 32 \* 8 = 256 bit.
In output troviamo anche una nuova sequenza A, B, C, D, E, F, G, H. Questo output verrà poi utilizzato in input nel tour successivo e così via fino alla fine del 64° tour.

I valori della sequenza in input per il primo tour della funzione di compressione corrispondono ai vettori di inizializzazione definiti in precedenza.
Come promemoria, i vettori di inizializzazione rappresentano i primi 32 bit decimali delle radici quadrate dei primi 8 numeri primi.

Ecco un esempio di tour:

![image](assets/image/section1/12.1.png)

##### Stato intermedio

Come promemoria, il messaggio viene diviso in blocchi di 512 bit che vengono poi divisi in pezzi da 32 bit. Per ogni blocco di 512 bit, applichiamo i 64 tour della funzione di compressione.
Lo stato intermedio corrisponde alla fine dei 64 tour di un blocco. I valori della sequenza in output di questo 64° tour vengono utilizzati come valori iniziali della sequenza in input per il primo tour del blocco successivo.

![image](assets/image/section1/12.2.png)

#### Visione generale della funzione di hash

![image](assets/image/section1/13.JPG)

Noteremo che l'output del primo pezzo di messaggio di 512 bit corrisponde ai nostri vettori di inizializzazione in input del secondo pezzo di messaggio, e così via.

L'output dell'ultimo tour, dell'ultimo pezzo, corrisponde al risultato finale della funzione SHA256.

In conclusione, vorremmo sottolineare il ruolo cruciale dei calcoli effettuati nelle scatole CH, MAJ, σ0 e σ1. Queste operazioni, tra le altre, sono i guardiani che garantiscono la robustezza della funzione di hash SHA256 contro gli attacchi, rendendola una scelta preferita per la sicurezza di numerosi sistemi digitali, in particolare nel protocollo Bitcoin. È quindi evidente che, sebbene complessa, la bellezza di SHA256 risiede nella sua robustezza nel trovare l'input a partire dall'hash, mentre la verifica dell'hash per un determinato input è un'azione meccanicamente semplice.

## Gli algoritmi utilizzati per la derivazione

![Gli algoritmi utilizzati per la derivazione](https://youtu.be/ZF1_BMsOJXc)

Gli algoritmi di derivazione HMAC e PBKDF2 sono componenti chiave nella sicurezza del protocollo Bitcoin. Prevengono una varietà di potenziali attacchi e garantiscono l'integrità dei portafogli Bitcoin.
HMAC e PBKDF2 sono strumenti crittografici utilizzati per diverse operazioni in Bitcoin. HMAC è principalmente utilizzato per contrastare attacchi di estensione di lunghezza durante la derivazione dei portafogli deterministici gerarchicamente (HD), mentre PBKDF2 è utilizzato per convertire una frase mnemonica in un seme.

#### HMAC-SHA512

La coppia HMAC-SHA512 ha due input: un messaggio m (Input 1) e una chiave K scelta arbitrariamente dall'utente (Input 2).
Ha anche un output di dimensione fissa: 512 bit

```
Nota:
- m: messaggio di dimensione arbitraria scelto dall'utente (input 1)
- K: chiave arbitraria scelta dall'utente (input 2)
- K': la chiave K allineata. È stata adattata alla dimensione B dei blocchi.
- ||: operazione di concatenazione.
- opad: costante definita dall'ottetto 0x5c ripetuto B volte.
- ipad: costante definita dall'ottetto 0x36 ripetuto B volte.
- B: dimensione dei blocchi della funzione di hash utilizzata.
```

![image](assets/image/section1/14.JPG)

HMAC-SHA512, che prende un messaggio e una chiave come input, genera un output di dimensione fissa. Per garantire l'uniformità, la chiave viene adattata in base alla dimensione dei blocchi utilizzati nella funzione di hash. Nell'ambito della derivazione dei portafogli HD, viene utilizzato HMAC-SHA-512. Quest'ultimo funziona con blocchi di 1024 bit (128 byte) e adatta di conseguenza la chiave. Utilizza le costanti OPAD (0x5c) e IPAD (0x36), ripetute quante volte necessario per rafforzare la sicurezza.

Il processo di HMAC-SHA-512 implica la concatenazione del risultato di SHA-512 applicato alla chiave XOR OPAD e alla chiave XOR IPAD con il messaggio. Quando viene utilizzato con blocchi di 1024 bit (128 byte), la chiave di input viene completata con zeri se necessario, quindi XORata con IPAD e OPAD. La chiave così modificata viene quindi concatenata con il messaggio.

![image](assets/image/section1/15.JPG)

Il codice di stringa, integrando una fonte aggiuntiva di entropia, aumenta la sicurezza delle chiavi derivate. Senza di esso, un attacco potrebbe compromettere l'intero portafoglio e rubare tutti i bitcoin.

#### PBKDF2

PBKDF2 viene utilizzato per convertire una frase mnemonica in un seme. In questo caso, nell'input 1 possiamo trovare la frase mnemonica e nell'input 2 la passphrase.
Questo algoritmo esegue 2048 iterazioni utilizzando HMAC SHA512. Grazie a questi algoritmi di derivazione, due input diversi possono produrre un output unico e fisso, risolvendo così il problema degli attacchi di estensione di lunghezza possibili sulle funzioni della famiglia SHA-2. Un attacco di estensione di lunghezza sfrutta una proprietà specifica di alcune funzioni di hash crittografiche. In un tale attacco, un attaccante che già possiede l'hash di un messaggio sconosciuto può utilizzarlo per calcolare l'hash di un messaggio più lungo, che è un'estensione del messaggio originale. Questo è spesso possibile senza conoscere il contenuto del messaggio originale, il che può portare a gravi vulnerabilità di sicurezza se questo tipo di funzione di hash viene utilizzato per compiti come la verifica dell'integrità.

![image](assets/image/section1/16.JPG)

In conclusione, gli algoritmi HMAC e PBKDF2 svolgono un ruolo essenziale nella sicurezza della derivazione dei portafogli HD nel protocollo Bitcoin. L'HMAC-SHA-512 viene utilizzato per proteggersi dagli attacchi di estensione di lunghezza, mentre PBKDF2 consente la conversione della frase mnemonica in un seme. Il codice di concatenazione aggiunge una fonte di entropia aggiuntiva nella derivazione delle chiavi, garantendo così la robustezza del sistema.

# Le firme digitali

## Firme digitali e curve ellittiche

![Firme digitali e curve ellittiche](https://youtu.be/gOjYiPkx4z8)

Dove sono conservati questi famosi bitcoin? Non in un portafoglio Bitcoin, come si potrebbe pensare. In realtà, un portafoglio Bitcoin conserva le chiavi private necessarie per dimostrare la proprietà dei bitcoin. I bitcoin stessi sono registrati sulla blockchain, un database decentralizzato che archivia tutte le transazioni.

Nel sistema Bitcoin, l'unità di conto è il bitcoin (nota la "b" minuscola). Questo è divisibile fino a otto decimali, con la più piccola unità chiamata satoshi. Le UTXO, o "Unspent Transaction Output", rappresentano le uscite delle transazioni non spese appartenenti a una chiave pubblica che è a sua volta legata matematicamente a una chiave privata. Per spendere questi bitcoin, è necessario soddisfare la condizione di spesa della transazione. Una tipica condizione di spesa consiste nel dimostrare al resto della rete che l'utente è il legittimo proprietario della chiave pubblica associata alle UTXO. Per fare ciò, dovrà dimostrare di essere in possesso della chiave privata corrispondente alla chiave pubblica legata a ciascuna UTXO senza però rivelare la chiave privata.
Ecco cosa consente la firma digitale. Serve come prova matematica che dimostra il possesso di una chiave privata associata a una specifica chiave pubblica. Questa tecnica di protezione dei dati si basa essenzialmente su un affascinante campo della crittografia chiamato crittografia a curve ellittiche (ECC).
La firma può essere verificata matematicamente dalle altre parti coinvolte nella rete Bitcoin.

![image](assets/image/section2/0.JPG)

Per garantire la sicurezza delle transazioni, Bitcoin utilizza due protocolli di firma digitale: ECDSA (Elliptic Curve Digital Signature Algorithm) e Schnorr. ECDSA è un protocollo di firma integrato in Bitcoin fin dal suo lancio nel 2009, mentre le firme di Schnorr sono state aggiunte più di recente, nel novembre 2021. Sebbene entrambi i protocolli si basino sulla crittografia a curve ellittiche e utilizzino meccanismi matematici simili, differiscono principalmente in termini di struttura della firma.

In questo corso, presenteremo l'algoritmo ECDSA.

### Cosa sono le curve ellittiche?

La crittografia a curve ellittiche è un insieme di algoritmi che utilizzano una curva ellittica per le sue diverse proprietà geometriche e matematiche a scopo crittografico e la cui sicurezza si basa sulla difficoltà di calcolo del logaritmo discreto.

Le curve ellittiche sono utili in una varietà di applicazioni crittografiche nel protocollo Bitcoin, dalle chiavi di scambio alla crittografia asimmetrica alle firme digitali.

Le curve ellittiche hanno proprietà interessanti:

- simmetria: ogni retta non verticale che taglia due punti sulla curva ellittica, taglierà la curva in un terzo punto.
- ogni retta non verticale e tangente alla curva in un punto, taglierà sempre la curva in un secondo punto unico.

Il protocollo Bitcoin utilizza una particolare curva ellittica chiamata Secp256k1 per eseguire le sue operazioni crittografiche.

Prima di approfondire questi meccanismi di firma, è importante capire cosa sia una curva ellittica. Una curva ellittica è definita dall'equazione y² = x³ + ax + b. Ogni punto su questa curva ha una distintiva simmetria che è la chiave della sua utilità in crittografia.

![image](assets/image/section2/1.JPG)

Alla fine, diverse curve ellittiche sono riconosciute come sicure per l'uso crittografico. La più conosciuta è forse la curva secp256r1. Tuttavia, per Bitcoin, Satoshi Nakamoto ha optato per un'altra curva: la secp256k1.

Questa curva è definita dai parametri a=0 e b=7, e la sua equazione è y² = x³ + 7 modulo n, con n che rappresenta il numero primo che determina l'ordine della curva.

![image](assets/image/section2/2.JPG)
La prima immagine rappresenta la curva secp256k1 sul campo dei numeri reali e la sua equazione. La seconda immagine è una rappresentazione della curva secp256k1 sul campo ZP, il campo dei numeri naturali e positivi, modulo p dove p è un numero primo. Assomiglia a una nuvola di punti. Utilizziamo questo campo dei numeri naturali e positivi per evitare approssimazioni.
p è un numero primo, è l'ordine della curva che viene utilizzato.
Infine, l'equazione utilizzata nel protocollo Bitcoin è:

$$
y^2 = (x^3 + 7) mod(p)
$$

L'equazione della curva ellittica su Bitcoin corrisponde all'ultima equazione nell'immagine precedente.

Nella prossima sezione di questo corso, utilizzeremo curve che sono sul campo dei numeri reali semplicemente per facilitare la comprensione.

### Calcolare la chiave pubblica dalla chiave privata

![Calcolare la chiave pubblica dalla chiave privata](https://youtu.be/NJENwFU889Y)

Per iniziare, immergiamoci nell'universo dell'algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA). Bitcoin sfrutta questo algoritmo di firma digitale per collegare le chiavi private e pubbliche. In questo sistema, la chiave privata è un numero casuale o pseudo-casuale di 256 bit. Il numero totale di possibilità per una chiave privata è teoricamente 2^256, ma nella realtà è leggermente inferiore a questo. Per essere precisi, alcune chiavi private di 256 bit non sono valide per Bitcoin.

Per essere compatibile con Bitcoin, una chiave privata deve essere compresa tra 1 e n-1, dove n rappresenta l'ordine della curva ellittica. Ciò significa che il numero totale di possibilità per una chiave privata Bitcoin è quasi pari a 1,158 x 10^77. Per mettere le cose in prospettiva, è approssimativamente lo stesso numero di atomi presenti nell'universo osservabile.

![image](assets/image/section2/3.JPG)

La chiave privata unica, indicata con k, viene quindi utilizzata per determinare una chiave pubblica.

La chiave pubblica, indicata con K, è un punto sulla curva ellittica che è derivato dalla chiave privata utilizzando algoritmi irreversibili come ECDSA. Quando abbiamo conoscenza della chiave privata, è molto facile trovare la chiave pubblica, ma quando abbiamo solo la chiave pubblica, è impossibile trovare la chiave privata. Questa irreversibilità è la base della sicurezza del portafoglio Bitcoin.

La chiave pubblica è di 512 bit perché corrisponde a un punto sulla curva con una coordinata x di 256 bit e una coordinata y di 256 bit. Tuttavia, può essere compressa in un numero di 264 bit.

![image](assets/image/section2/4.JPG)
Il punto generatore (G) è il punto sulla curva da cui vengono generate tutte le chiavi pubbliche nel protocollo Bitcoin. Ha coordinate x e y specifiche, generalmente rappresentate in esadecimale. Per secp256k1, le coordinate di G sono, in esadecimale:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Questo punto è utile per derivare tutte le chiavi pubbliche. Per calcolare la chiave pubblica K, è sufficiente moltiplicare il punto G per la chiave privata k, come segue: K = k.G

Ora studieremo come sommare e moltiplicare punti sulle curve ellittiche.

#### Somma e raddoppio di punti sulle curve ellittiche

##### Somma di due punti M + L

Una delle proprietà notevoli delle curve ellittiche è che una retta non verticale che interseca la curva in due punti intersecherà anche un terzo punto, chiamato punto O nel nostro esempio. Questa proprietà viene utilizzata per determinare il punto U, che è l'opposto del punto O.

M + L = U

![image](assets/image/section2/5.JPG)

##### Raddoppio di un punto

L'aggiunta di un punto G a se stesso viene effettuata tracciando una tangente alla curva nel punto G. Questa tangente, secondo le proprietà delle curve ellittiche, intersecherà inevitabilmente la curva in un secondo punto unico -J. L'opposto di questo punto, J, è il risultato dell'aggiunta del punto G a se stesso.
G + G = J

Inoltre, il punto G è il punto di partenza per calcolare tutte le chiavi pubbliche degli utenti del sistema Bitcoin.

![image](assets/image/section2/6.JPG)

#### Prodotto scalare su curve ellittiche

Il prodotto scalare di un punto per n equivale ad aggiungere quel punto a se stesso n volte.

Come nel caso del raddoppio di un punto, il prodotto scalare del punto G per un punto n viene effettuato tracciando una tangente alla curva nel punto G. Questa tangente, secondo le proprietà delle curve ellittiche, intersecherà inevitabilmente la curva in un secondo punto unico -2G. L'opposto di questo punto, 2G, è il risultato dell'aggiunta del punto G a se stesso.

Se n = 4, l'operazione viene ripetuta fino a raggiungere 4G.

![image](assets/image/section2/7.JPG)

Ecco un esempio di calcolo per 3G:

![image](assets/image/section2/8.JPG)
Queste operazioni sui punti di una curva ellittica sono alla base del calcolo delle chiavi pubbliche. La derivazione di una chiave pubblica conoscendo la chiave privata è molto facile. Una chiave pubblica è un punto sulla curva ellittica, è il risultato della nostra aggiunta e raddoppio del punto G k volte. Con k = chiave privata.

In questo esempio:

- La chiave privata k = 4
- La chiave pubblica K = kG = 4G

![image](assets/image/section2/9.JPG)

Conoscendo la chiave privata k, è facile calcolare la chiave pubblica K. Impossibile invece recuperare la chiave privata in base alla chiave pubblica. È il risultato di un'aggiunta o di un raddoppio del punto?

Nella nostra prossima lezione, esploreremo come viene realizzata una firma digitale utilizzando l'algoritmo ECDSA con una chiave privata per spendere bitcoin.

## Firmare con la chiave privata

![Firmare con la chiave privata](https://youtu.be/h2hIyGgPqkM)

Il processo di firma digitale è un metodo chiave per dimostrare di essere il detentore di una chiave privata senza doverla rivelare. Questo viene realizzato utilizzando l'algoritmo ECDSA, che comprende la determinazione di un nonce unico, il calcolo di un numero specifico, V, e la creazione di una firma digitale composta da due parti, S1 e S2.
È fondamentale utilizzare sempre un nonce unico per evitare attacchi di sicurezza. Un esempio noto di ciò che può accadere quando questa regola non viene rispettata è il caso dell'hacking della PlayStation 3, che è stato compromesso a causa del riutilizzo del nonce.

![](assets/image/section2/10.JPG)

Passaggi:

- Determinare un nonce v, cioè un numero unico e casuale.
  Nonce = Number Only Use Once.
  Viene determinato da chi effettua la firma.
- Calcolare per aggiunta e raddoppio del punto sulla curva ellittica a partire dal punto G, la posizione di V sulla curva ellittica.
  Come V = v.G
  x e y sono le coordinate di V sul piano.
- Calcolare S1.
  S1 = x mod n con n = l'ordine della curva e x una coordinata di V sul piano.
  NB: Il numero di possibilità della chiave pubblica è maggiore del numero di punti sulla curva ellittica nel campo finito dei numeri interi positivi utilizzato in Bitcoin.
  L'ordine della curva corrisponde solo alle possibilità che la chiave pubblica può assumere sulla curva.
- Calcolare S2.
  H(Tx) = Hash della transazione
  k = la chiave privata
- Calcolare la firma: la concatenazione di S1 + S2.
- Calcolare P, il calcolo della verifica della firma.
  K = la chiave pubblica
  'Par exemple, per ottenere la chiave pubblica 3G, si disegna una tangente al punto G, si calcola l'opposto di -G per ottenere 2G, quindi si somma G e 2G. Per effettuare una transazione, è necessario dimostrare di conoscere il numero 3 sbloccando i bitcoin associati alla chiave pubblica 3G.
  Per creare una firma digitale e dimostrare di conoscere la chiave privata associata alla chiave pubblica 3G, si calcola prima un nonce, quindi il punto V associato a questo nonce (nell'esempio dato, è 4G). Successivamente, si calcola il punto T sommando la chiave pubblica 3G e il punto V, ottenendo così 7G.

![image](assets/image/section2/11.JPG)

Semplifichiamo il processo di firma digitale.
Nell'immagine precedente, la chiave privata k = 3.
Possiamo facilmente calcolare la chiave pubblica K associata a questa chiave privata: K = 3G.
Successivamente, generiamo pseudo casualmente un nonce: v = 4.
A partire da questo nonce, è possibile calcolare V come: V = v.G = 4G.

A partire da questo punto V, calcoliamo il punto T come:
T = t.G = 7G (con t = 7).

È ora il momento di procedere alla verifica della firma digitale.

La verifica di una firma digitale è un passaggio cruciale nell'utilizzo dell'algoritmo ECDSA, che consente di confermare l'autenticità di un messaggio firmato senza la necessità della chiave privata del mittente. Ecco come avviene in dettaglio:

Nel nostro esempio, abbiamo due valori importanti: t e V.
t è un valore numerico (7 in questo esempio), e V è un punto sulla curva ellittica (rappresentato qui come 4G). Questi valori vengono generati durante la creazione della firma digitale e successivamente inviati con il messaggio per consentire la verifica.

Quando il verificatore riceve il messaggio, riceverà anche questi due valori, t e V.

Ecco i passaggi che il verificatore seguirà per validare la firma:

1. Prima di tutto, calcolerà l'hash del messaggio, che chiameremo H.
2. Successivamente, calcolerà u1 e u2. Per fare ciò, utilizzerà le seguenti formule:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Dove S2 è la seconda parte della firma digitale, n è l'ordine della curva ellittica e (S2)^-1 è l'inverso di S2 mod n.
3. Il verificatore calcolerà quindi un punto P' sulla curva ellittica utilizzando la formula: P' = u1 _ G + u2 _ K
   - G è il punto di generazione della curva
   - K è la chiave pubblica del mittente'
4. Il verificatore calcolerà quindi I', che è semplicemente la coordinata x del punto P' modulo n. 5. Infine, il verificatore confermerà che I' sia uguale a t. Se è così, la firma è considerata valida. Se non è così, la firma è invalida.

Questa procedura garantisce che solo il mittente che possiede la corrispondente chiave privata potrebbe aver prodotto una firma che supera questo processo di verifica.

![image](assets/image/section2/12.JPG)

Semplifichiamo:
Colui che produce la firma fornirà a colui che verifica il numero t (nel nostro esempio, t = 7) e il punto V.

È impossibile determinare la chiave pubblica o la chiave privata a partire dal numero 7 e dal numero V.

I passaggi per la verifica della firma digitale sono i seguenti:

- Sulla curva, si aggiunge il punto della chiave pubblica al punto V per ottenere il punto T'.
- Si calcola il numero t.G
- Si verifica che il risultato di t.G sia effettivamente uguale al numero T'

In conclusione, la verifica di una firma digitale è una procedura essenziale nelle transazioni Bitcoin. Garantisce che il messaggio firmato non sia stato alterato durante la trasmissione e che il mittente sia effettivamente il detentore della chiave privata. Questa tecnica di autenticazione digitale si basa su principi matematici complessi, come l'aritmetica delle curve ellittiche, mantenendo al contempo la riservatezza della chiave privata. Offre una solida base di sicurezza per le transazioni crittografiche.

Detto ciò, la gestione di queste chiavi, così come la loro creazione, è un'altra questione essenziale in Bitcoin. Come generare una nuova coppia di chiavi? Come organizzare in modo sicuro ed efficiente una moltitudine di chiavi? Come recuperarle se necessario?

Per rispondere a queste domande e approfondire la comprensione della sicurezza crittografica, il nostro prossimo corso si concentrerà sul concetto di Portafoglio Deterministico Gerarchico (HD wallets) e sull'uso di frasi mnemoniche. Questi meccanismi offrono modi eleganti per gestire in modo efficiente le tue chiavi di criptovaluta, rafforzando al contempo la sicurezza.

# La frase mnemonica

## Evoluzione dei portafogli Bitcoin

![Evoluzione dei portafogli Bitcoin](https://youtu.be/6tmu1R9cXyk)

Il Portafoglio Deterministico Gerarchico, o più comunemente chiamato portafoglio HD, svolge un ruolo fondamentale nell'ecosistema delle criptovalute. Il termine "portafoglio" può sembrare fuorviante per coloro che sono nuovi in questo campo, poiché non implica il possesso di denaro o valute. Si riferisce piuttosto a una collezione di chiavi crittografiche private.
I primi portafogli erano software che raggruppavano chiavi private generate in modo pseudo-casuale ma che non avevano alcun collegamento tra di loro. Questi portafogli sono chiamati "Just a Bunch Of Keys" (JBOK).
Poiché le chiavi non hanno alcun collegamento tra di loro, l'utente è obbligato a fare un nuovo backup per ogni nuova coppia di chiavi generate.
L'utente può utilizzare sempre la stessa coppia di chiavi e perdere in termini di riservatezza, oppure può generare una nuova coppia di chiavi in modo casuale e quindi deve fare un nuovo backup di queste chiavi.

![image](assets/image/section3/0.JPG)

Tuttavia, la complessità della gestione di queste chiavi è compensata da un insieme di protocolli chiamati Bitcoin Improvement Proposals (BIP). Queste proposte di aggiornamento sono al centro della funzionalità e della sicurezza dei portafogli HD. Ad esempio, il [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lanciato nel 2012, ha rivoluzionato il modo in cui queste chiavi vengono generate e memorizzate, introducendo il concetto di chiavi derivate in modo deterministico e gerarchico. L'idea è quella di derivare tutte le chiavi in modo deterministico e gerarchico da un'unica informazione: il seed. In questo modo, il processo di backup di queste chiavi è notevolmente semplificato, mantenendo comunque il loro livello di sicurezza.

![image](assets/image/section3/1.JPG)

Successivamente, il [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) ha introdotto un'innovazione significativa: la frase mnemonica di 24 parole. Questo sistema ha permesso di trasformare una sequenza di numeri complessa e difficile da ricordare in una serie di parole comuni, molto più facili da memorizzare e conservare. Inoltre, il [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) ha proposto di aggiungere una passphrase aggiuntiva per aumentare la sicurezza delle singole chiavi. Questi miglioramenti successivi hanno portato agli standard BIP43 e BIP44, che hanno standardizzato la struttura e la gerarchia dei portafogli HD, rendendo questi portafogli più accessibili e facili da usare per il grande pubblico.

Nelle sezioni seguenti, approfondiremo il funzionamento dei portafogli HD. Esamineremo i principi di derivazione delle chiavi e esamineremo i concetti fondamentali di entropia e generazione di numeri casuali, che sono essenziali per garantire la sicurezza del tuo portafoglio HD.
A titolo di sintesi, è essenziale sottolineare il ruolo centrale di BIP32 e BIP39 nella progettazione e sicurezza dei portafogli HD. Questi protocolli consentono di generare una moltitudine di chiavi da un unico seed, che dovrebbe essere un numero casuale o pseudo-casuale. Oggi, queste norme sono adottate dalla maggior parte dei portafogli di criptovalute, che siano dedicati a una singola criptovaluta o supportino diversi tipi di valute.

## Entropia e numero casuale

![Entropia e numero casuale](https://youtu.be/k18yH18w2TE)

L'importanza della sicurezza delle chiavi private nell'ecosistema Bitcoin è innegabile. Infatti, sono la base che garantisce la sicurezza delle transazioni Bitcoin. Per evitare vulnerabilità legate alla prevedibilità, queste chiavi devono essere generate in modo veramente casuale, il che può rapidamente rivelarsi un compito laborioso. Il problema è che in informatica è impossibile generare un numero veramente casuale poiché deriva necessariamente da un processo deterministico; un codice.
Ecco perché è essenziale informarsi sui diversi Generatori di Numeri Casuali (RNG). I tipi di RNG variano, dai Pseudo-Random Number Generators (PRNG) ai True Random Number Generators (TRNG), così come i PRNG che integrano una fonte di entropia.

L'entropia si riferisce allo "stato di disordine" di un sistema. Utilizzando un'entropia esterna, cioè una fonte di informazione esterna, è possibile utilizzare un generatore di numeri casuali per ottenere un numero casuale.

![image](assets/image/section3/2.JPG)

Vediamo insieme il funzionamento di un Pseudo-Random Number Generator (PRNG).

Prende in input un seed, cioè un'informazione che corrisponde allo stato interno 0.
Su questo stato interno viene applicata una funzione di trasformazione e il risultato, che è un numero pseudo-casuale, corrisponde allo stato interno 1.
Su questo stato interno 1, di nuovo, viene applicata una funzione di trasformazione che porta a un nuovo numero casuale = stato interno 2.
E così via.

Il principale inconveniente è che lo stesso seed produrrà sempre lo stesso risultato in output. Inoltre, se conosciamo i risultati delle funzioni di trasformazione dall'inizio, saremo in grado di recuperare il numero casuale in output dal processo.

Un esempio di funzione di trasformazione è la funzione PBKDF2.

**In sintesi, un PRNG criptograficamente sicuro deve:**

- essere statisticamente casuale
- essere imprevedibile
- essere resistente anche se i risultati sono rivelati
- avere un periodo sufficientemente lungo

![image](assets/image/section3/3.JPG)
Nel caso del Bitcoin, le chiavi private vengono generate da un'unica informazione alla base del portafoglio. Questa informazione consente una derivazione deterministica e gerarchica delle coppie di chiavi figlie. L'entropia è la base di ogni portafoglio HD, anche se non esiste uno standard per la generazione di questo numero casuale. Pertanto, la generazione di numeri casuali è una sfida importante per garantire la sicurezza delle transazioni Bitcoin.
![image](assets/image/section3/4.JPG)

La fase di verifica della generazione delle chiavi è cruciale per garantire la sicurezza e l'autenticità della generazione di numeri casuali, un passaggio fondamentale per prevenire qualsiasi vulnerabilità legata alla prevedibilità. È quindi fortemente consigliato utilizzare portafogli open source per consentire questa verifica.

Tuttavia, è importante notare che alcuni portafogli hardware possono essere "closed source", rendendo impossibile la verifica della generazione del numero casuale. Un possibile workaround sarebbe generare la propria frase mnemonica utilizzando dei dadi, anche se questo approccio potrebbe comportare alcuni rischi.

L'utilizzo di una passphrase generata casualmente può contribuire ad attenuare questi rischi.

In definitiva, il casuale occupa un ruolo centrale nella crittografia e nell'informatica, e la capacità di generare casualità in modo sicuro è cruciale per garantire la sicurezza delle chiavi private e delle transazioni Bitcoin. L'entropia, che è al centro del portafoglio HD di Bitcoin, è essenziale per la sua sicurezza. Nella nostra prossima lezione, continueremo ad esplorare questo argomento, approfondendo ulteriormente il modo in cui l'entropia contribuisce alla sicurezza dei portafogli HD.

## La frase mnemonica

![La frase mnemonica](https://youtu.be/uJERqH9Xp7I)

La sicurezza di un portafoglio Bitcoin è una preoccupazione principale per tutti i suoi utenti. Un modo essenziale per garantire il backup del portafoglio è generare una frase mnemonica basata sull'entropia e sul checksum.

![image](assets/image/section3/5.JPG)

Per passare dall'entropia a una frase mnemonica, è sufficiente calcolare il checksum dell'entropia e concatenare entropia e checksum.

Una volta generata l'entropia, si utilizza la funzione SHA256 sull'entropia per crearne un hash.
Si recuperano i primi 8 bit dell'hash, che costituiscono il checksum.
La frase mnemonica è il risultato dell'entropia aggiunta al checksum.

Il checksum garantisce la verifica dell'esattezza della frase di recupero. Senza questo checksum, un errore nella frase potrebbe portare alla creazione di un portafoglio diverso e quindi alla perdita dei fondi. Si ottiene il checksum passando l'entropia attraverso la funzione SHA256 e recuperando i primi 8 bit dell'hash.
![image](assets/image/section3/6.JPG)
Diversi standard esistono per la frase mnemonica in base alla dimensione dell'entropia. Lo standard più comunemente utilizzato per una frase di recupero di 24 parole è un'entropia di 256 bit. La dimensione del checksum è determinata dividendo la dimensione dell'entropia per 32.

Ad esempio, un'entropia di 256 bit genera un checksum di 8 bit. La concatenazione dell'entropia e del checksum porta quindi a dimensioni rispettive di 128 bit, 160 bit, ecc. In base alla dimensione dell'entropia, la frase di recupero avrà 12 parole per 128 bit, 15 parole per 160 bit e 24 parole per 256 bit.

**Codifica della frase mnemonica:**

![image](assets/image/section3/7.JPG)

Gli ultimi 8 bit corrispondono al checksum.
Ogni segmento di 11 bit viene convertito in decimale.
Ogni decimale corrisponde a una parola proveniente da un elenco di 2048 parole sul BIP39. È importante precisare che nessuna parola presenta le prime quattro lettere nello stesso ordine.

È essenziale salvare la frase di recupero di 24 parole per preservare l'integrità del portafoglio Bitcoin. I due standard più comunemente utilizzati si basano su un'entropia di 128 o 256 bit e una concatenazione di 12 o 24 parole. L'aggiunta di una passphrase costituisce un'opzione aggiuntiva per rafforzare la sicurezza del portafoglio.

In conclusione, la generazione di una frase mnemonica per proteggere un portafoglio Bitcoin è un processo cruciale. È importante rispettare gli standard della frase mnemonica in base alla dimensione dell'entropia. Il salvataggio della frase di recupero di 24 parole è essenziale per prevenire la perdita di fondi.

## La passphrase

![La passphrase](https://youtu.be/dZkOYO7MXwc)

La passphrase è una password aggiuntiva che può essere integrata in un portafoglio Bitcoin per aumentarne la sicurezza. Il suo utilizzo è opzionale e dipende dall'apprezzamento dell'utente. Aggiungendo informazioni arbitrarie che, insieme alla frase mnemonica, consentono di calcolare il seed del portafoglio, la passphrase rafforza la sicurezza dello stesso.

![image](assets/image/section3/8.JPG)

Una volta stabilito quando viene creato un portafoglio, è necessario per la derivazione di tutte le chiavi del portafoglio. La funzione pbkdf2 viene utilizzata per generare il seme dalla passphrase. Questo seme viene utilizzato per derivare tutte le coppie di chiavi figlio del portafoglio. Se la passphrase viene modificata, il portafoglio Bitcoin diventa completamente diverso.

La passphrase è uno strumento essenziale per rafforzare la sicurezza dei portafogli Bitcoin. Può essere utilizzata per applicare diverse strategie di sicurezza. Ad esempio, può essere utilizzata per creare duplicati e facilitare il backup della passphrase. Può anche migliorare la sicurezza del portafoglio mitigando i rischi associati alla generazione casuale della passphrase.

Una passphrase efficace dovrebbe essere lunga (da 20 a 40 caratteri) e diversificata (utilizzando lettere maiuscole e minuscole, numeri e simboli). Non deve essere direttamente collegata all'utente o al suo ambiente. È più sicuro utilizzare una sequenza casuale di caratteri piuttosto che una semplice parola come passphrase.

![immagine](assets/image/section3/9.JPG)

Una passphrase è più sicura di una semplice password. La passphrase ideale è lunga, varia e casuale. Può rafforzare la sicurezza di un portafoglio o di un software a caldo. Può anche essere utilizzata per creare backup ridondanti e sicuri.

È fondamentale curare i backup della passphrase per evitare di perdere l'accesso al portafoglio. Una passphrase è un'opzione per un portafoglio HD. Può essere generata casualmente utilizzando i dadi o un altro generatore di numeri pseudocasuali.

# Creazione di un portafoglio Bitcoin

## Creazione del seme e della chiave master

![Creazione del seme e della chiave master](https://youtu.be/56yAt_JDWhY)

In questa parte del corso, esploreremo le fasi di creazione di un HD (Hierarchical Deterministic Wallet), che consente di creare e gestire le chiavi private e pubbliche in modo gerarchico e deterministico.

![immagine](assets/image/section4/0.JPG)

Le fondamenta del portafoglio HD si basano su due elementi essenziali: la frase mnemonica e la passphrase (password aggiuntiva opzionale). Insieme formano il seme, una sequenza alfanumerica di 512 bit che serve come base per ricavare le chiavi del portafoglio. Da questo seme è possibile ricavare tutte le coppie di chiavi figlio del portafoglio Bitcoin. Il seme è la chiave per accedere a tutti i bitcoin associati al portafoglio, sia che si utilizzi una passphrase o meno.

![image](assets/image/section4/1.JPG)
Per ottenere il seed, si utilizza la funzione pbkdf2 (Password-Based Key Derivation Function 2) con la frase mnemonica e la passphrase. L'output di pbkdf2 è un seed di 512 bit.
A partire dal seed, è possibile determinare la chiave privata principale e il codice di catena utilizzando l'algoritmo HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Questo algoritmo richiede un messaggio e una chiave in input per generare un risultato. La chiave privata principale viene calcolata a partire dal seed e dalla frase "Bitcoin SEED". Questa frase è identica per tutte le derivazioni di tutti i portafogli HD, garantendo così coerenza tra i portafogli.

Inizialmente, la funzione SHA-512 non era implementata nel protocollo Bitcoin, quindi si utilizza HMAC SHA-512. L'utilizzo di HMAC SHA-512 con la frase "Bitcoin SEED" vincola l'utente a generare un portafoglio specifico per Bitcoin. Il risultato di HMAC SHA-512 è un numero di 512 bit, diviso in due parti: i 256 bit a sinistra rappresentano la chiave privata principale, mentre i 256 bit a destra rappresentano il codice di catena principale.

![image](assets/image/section4/2.JPG)

La chiave privata principale è la chiave genitore di tutte le future chiavi del portafoglio, mentre il codice di catena principale interviene nella derivazione delle chiavi figlie. È importante notare che è impossibile derivare una coppia di chiavi figlie senza conoscere il codice di catena corrispondente della coppia genitore.

Una coppia di chiavi nel portafoglio comprende una chiave privata, una chiave pubblica e un codice di catena. Il codice di catena consente di introdurre una fonte di casualità nella derivazione delle chiavi figlie e di isolare ogni coppia di chiavi per evitare eventuali falle di informazioni.

È importante sottolineare che la chiave privata principale è la prima chiave privata derivata dal seed e non ha alcun collegamento con le chiavi estese del portafoglio.

Nel prossimo corso, esploreremo in dettaglio le chiavi estese, come xPub, xPRV, zPub, e comprenderemo perché vengono utilizzate e come vengono costruite.

## Le chiavi estese

![Le chiavi estese](https://youtu.be/TRz760E_zUY)

In questa parte del corso, studieremo le chiavi estese (xPub, zPub, yPub) e i loro prefissi, che svolgono un ruolo importante nella derivazione delle chiavi figlie in un portafoglio HD (Hierarchical Deterministic Wallet).

![image](assets/image/section4/3.JPG)
Le chiavi estese si distinguono dalle chiavi principali. Un portafoglio HD genera una frase mnemonica e un seme per ottenere la chiave principale e il codice di catena principale. Le chiavi estese vengono utilizzate per derivare le chiavi figlie e richiedono sia la chiave genitore che il corrispondente codice di catena. Una chiave estesa combina queste due informazioni per semplificare il processo di derivazione.
![image](assets/image/section4/4.JPG)

Le chiavi pubbliche estese possono derivare solo da normali chiavi pubbliche figlie, mentre le chiavi private estese consentono di derivare sia chiavi pubbliche che private figlie, sia in una derivazione normale che indurita.
La derivazione indurita è la derivazione dalla chiave genitore privata. La derivazione normale corrisponde alla derivazione dalla chiave genitore pubblica.

L'uso di chiavi estese con il prefisso XPUB consente di derivare nuovi indirizzi senza risalire alle corrispondenti chiavi private, offrendo una maggiore sicurezza. I metadati associati alle chiavi estese forniscono informazioni importanti sul loro ruolo e sulla loro posizione nella gerarchia delle chiavi.

Le chiavi estese sono identificate da specifici prefissi (XPRV, XPUB, YPUB, ZPUB) che indicano se si tratta di una chiave estesa privata o pubblica, nonché il suo scopo specifico. I metadati associati a una chiave estesa includono la versione (prefisso), la profondità, l'impronta digitale della chiave pubblica, l'indice e il payload (codice di catena e chiave genitore).

![image](assets/image/section4/5.JPG)

La versione corrisponde al tipo di chiave: xpub, xprv, ...

La profondità corrisponde al numero di derivazioni tra genitore e figlio che sono state effettuate dalla chiave principale.

L'impronta genitore sono i primi 4 byte dell'hash 160 della chiave genitore.

L'indice è il numero della coppia che viene utilizzata per generare la chiave estesa tra le sue sorelle. (sorelle = chiavi della stessa profondità)
esempio: se vogliamo derivare l'xpub del nostro terzo account, il suo indice sarà 2 (perché l'indice inizia da 0).

Il payload è composto dal codice di catena (32 byte) e dalla chiave genitore (33 byte).

Le chiavi pubbliche compressate hanno una dimensione di 33 byte, mentre le chiavi pubbliche non compressate sono di 512 bit. Le chiavi pubbliche compressate conservano le stesse informazioni delle chiavi non compressate, ma con una dimensione ridotta. Le chiavi estese hanno una dimensione di 82 byte e il loro prefisso è rappresentato in base 58 tramite una conversione in esadecimale. Il checksum viene calcolato utilizzando la funzione di hash HASH256.

![image](assets/image/section4/6.JPG)
Le derivate rinforzate iniziano dagli indici che sono potenze di 2 (2^31). È interessante notare che i prefissi più comunemente utilizzati sono xpub e zpub, che corrispondono rispettivamente agli standard legacy e segwit v1 e segwit v0.
Nella nostra prossima lezione, esamineremo la derivazione delle coppie di chiavi figlie utilizzando le conoscenze acquisite sulle chiavi estese e la chiave principale del portafoglio.

## Derivazione delle coppie di chiavi figlie

![Derivazione delle coppie di chiavi figlie](https://youtu.be/FXhI-GmE9Aw)

Come promemoria, abbiamo affrontato il calcolo del seed e della chiave principale, che costituiscono i primi elementi essenziali per la gerarchizzazione e la derivazione del portafoglio HD (Hierarchical Deterministic Wallet). Il seed, di lunghezza compresa tra 128 e 256 bit, viene generato in modo casuale o da una frase segreta. Gioca un ruolo deterministico nella derivazione di tutte le altre chiavi. La chiave principale è la prima chiave derivata dal seed e consente di derivare tutte le altre coppie di chiavi figlie.

Il codice di catena principale svolge un ruolo importante nel ripristino del portafoglio dal seed. È importante notare che tutte le chiavi derivate dallo stesso seed avranno lo stesso codice di catena principale.

![immagine](assets/image/section4/7.JPG)

La gerarchizzazione e la derivazione del portafoglio HD offrono una gestione più efficiente delle chiavi e delle strutture del portafoglio. Le chiavi estese consentono la derivazione di una coppia di chiavi figlie da una coppia genitore utilizzando calcoli matematici e algoritmi specifici.

Esistono diversi tipi di coppie di chiavi figlie, tra cui chiavi rinforzate e chiavi normali. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, sia in modalità normale che rinforzata. Ogni coppia di chiavi ha un indice che consente di differenziarle l'una dall'altra.

![immagine](assets/image/section4/8.JPG)

La derivazione delle chiavi figlie utilizza la funzione HMAC-SHA512 utilizzando la chiave genitore concatenata all'indice e al codice di catena associato alla coppia di chiavi. Le chiavi figlie normali hanno un indice compreso tra 0 e 2 elevato alla 31 meno 1, mentre le chiavi figlie rinforzate hanno un indice compreso tra 2 elevato alla 31 e 2 elevato alla 32 meno 1.

![immagine](assets/image/section4/9.JPG)

![immagine](assets/image/section4/10.JPG)
Esistono due tipi di coppie di chiavi figlie: coppie rinforzate e coppie normali. Il processo di derivazione delle chiavi figlie utilizza le chiavi pubbliche per generare le condizioni di spesa, mentre le chiavi private vengono utilizzate per la firma. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, in modalità normale o rinforzata.
![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)
La derivazione rinforzata utilizza la chiave privata genitore, mentre la derivazione normale utilizza la chiave pubblica genitore. La funzione HMAC-SHA512 viene utilizzata per la derivazione rinforzata, mentre la derivazione normale utilizza un hash di 512 bit. La chiave pubblica figlia viene ottenuta moltiplicando la chiave privata figlia per il generatore della curva ellittica.

![image](assets/image/section4/13.JPG)
![image](assets/image/section4/14.JPG)

La gerarchizzazione e la derivazione di molte coppie di chiavi in modo deterministico consentono di creare uno schema ad albero per la derivazione gerarchica. Nel prossimo corso di questa formazione, studieremo la struttura del portafoglio HD e i percorsi di derivazione, concentrandoci in particolare sulla notazione dei percorsi di derivazione.

## Struttura del portafoglio e percorsi di derivazione

![Struttura del portafoglio e percorsi di derivazione](https://youtu.be/etO9UxwyE2I)

In questo capitolo, studieremo la struttura dell'albero di derivazione in un portafoglio HD (Hierarchical Deterministic Wallet). Abbiamo già esplorato il calcolo del seed, la chiave master e la derivazione delle coppie di chiavi figlie. Ora ci concentreremo sull'organizzazione delle chiavi all'interno del portafoglio.

Il portafoglio HD utilizza livelli di profondità per organizzare le chiavi. Ogni derivazione da una coppia genitore a una coppia figlia corrisponde a un livello di profondità.

![image](assets/image/section4/15.JPG)

- La profondità 0 corrisponde alla chiave master e al codice di catena master.

- La profondità 1 viene utilizzata per derivare chiavi figlie secondo un obiettivo specifico, determinato dall'indice. Gli obiettivi sono conformi agli standard BIP 84 e Segwit v0/v1.

- La profondità 2 consente di distinguere i conti di diverse criptovalute o reti. Ciò consente di organizzare il portafoglio in base alle diverse fonti di fondi. Per bitcoin, l'indice sarà 0.

- La profondità 3 viene utilizzata per organizzare il portafoglio in diversi account, offrendo così una struttura più chiara e organizzata.
- La profondità 4 corrisponde alle catene esterne e interne, che vengono utilizzate per gli indirizzi destinati a essere comunicati pubblicamente. L'indice 0 è associato alla catena esterna, mentre l'indice 1 è associato alla catena interna. Ogni account ha due catene: la catena esterna (0) e la catena interna (1). La profondità 4 viene anche utilizzata per gestire i tipi di script nel caso dei portafogli multi firma.
- La profondità 5 viene utilizzata per gli indirizzi di ricezione su un portafoglio classico. Nella prossima sezione, esamineremo più in dettaglio la derivazione delle coppie di chiavi figlie.

![image](assets/image/section4/16.JPG)

Per ogni livello di profondità, utilizziamo gli indici per differenziare le coppie di chiavi figlie.

L'indice senza apostrofo corrisponde all'indice effettivamente utilizzato, mentre l'indice con apostrofo corrisponde all'indice effettivo + 2^31. Le derivazioni rinforzate utilizzano indici da 2^31 a 2^32-1. Ad esempio, l'indice 44' corrisponde all'indice effettivo 2^31 + 44.

Per generare un indirizzo di ricezione specifico, deriviamo una coppia di chiavi figlie dalla chiave principale e dal codice della catena principale. Successivamente, utilizziamo l'indice per differenziare le diverse coppie di chiavi figlie dello stesso livello di profondità.

Le chiavi estese, come XPUB, consentono di condividere il tuo portafoglio con più persone. La catena di derivazione viene utilizzata per differenziare la catena esterna (indirizzi destinati a essere comunicati) e la catena interna (indirizzi di cambio).

Nel prossimo capitolo, studieremo gli indirizzi di ricezione, i loro vantaggi di utilizzo e i passaggi per la loro costruzione.

# Cos'è un indirizzo Bitcoin?

## Gli indirizzi Bitcoin

![Gli indirizzi Bitcoin](https://youtu.be/nqGBMjPtFNI)

![image](assets/image/section5/0.JPG)

In questo capitolo, esploreremo gli indirizzi di ricezione, che svolgono un ruolo cruciale nel sistema Bitcoin. Consentono di ricevere fondi e vengono generati a partire da coppie di chiavi private e pubbliche. Sebbene esista un tipo di script chiamato Pay2PublicKey che consente di bloccare bitcoin su una chiave pubblica, gli utenti preferiscono generalmente utilizzare gli indirizzi di ricezione anziché questo script.

Quando un destinatario desidera ricevere bitcoin, fornisce un indirizzo di ricezione all'emittente anziché la sua chiave pubblica. Un indirizzo è in realtà un hash di una chiave pubblica, con un formato specifico.

![image](assets/image/section5/1.JPG)
È importante notare che non è possibile risalire dall'indirizzo alla chiave pubblica, né dalla chiave pubblica alla chiave privata. L'uso di un indirizzo permette di ridurre le dimensioni dell'informazione della chiave pubblica, che inizialmente è di 512 bit.
Gli indirizzi Bitcoin sono stati ridotti in dimensione per facilitarne l'uso. Hanno un checksum, che permette di rilevare gli errori di battitura e ridurre i rischi di perdita di bitcoin. Al contrario, le chiavi pubbliche non hanno un checksum, il che significa che gli errori di battitura possono comportare la perdita dei fondi corrispondenti.

Gli indirizzi offrono anche un secondo livello di sicurezza tra l'informazione pubblica e privata, rendendo più difficile il controllo della chiave privata.

È essenziale sottolineare che ogni indirizzo dovrebbe essere a uso unico. Il riutilizzo dello stesso indirizzo comporta problemi di privacy e dovrebbe essere evitato.

Sono utilizzati diversi prefissi per gli indirizzi Bitcoin. Ad esempio, BC1Q corrisponde a un indirizzo Segwit V0, BC1P a un indirizzo Taproot/Segwit V1, e i prefissi 1 e 3 sono associati agli indirizzi Pay2PublicKeyH/Pay2ScriptH (legacy). Nel prossimo corso, spiegheremo passo dopo passo la derivazione di un indirizzo da una chiave pubblica.

## Come creare un indirizzo Bitcoin?

![Come creare un indirizzo Bitcoin?](https://youtu.be/ewMGTN8dKjI)

In questo capitolo, affronteremo la costruzione di un indirizzo di ricezione per le transazioni Bitcoin. Un indirizzo di ricezione è una rappresentazione in forma di caratteri alfanumerici di una chiave pubblica compressa. La conversione di una chiave pubblica in un indirizzo di ricezione passa attraverso diverse fasi.

### Fase 1: Compressione della chiave pubblica

![immagine](assets/image/section5/14.png)

Un indirizzo è derivato da una chiave pubblica figlia.

Una chiave pubblica è un punto sulla curva ellittica. Grazie alla simmetria della curva ellittica, un punto sulla curva ellittica avrà una coordinata x associata solo a due possibili valori per y: positivo o negativo.
Tuttavia, nel protocollo Bitcoin, lavoriamo con un campo di interi positivi finiti anziché con il campo dei reali. Per distinguere tra i due possibili valori di y, è sufficiente indicare se y è pari o dispari.

La compressione di una chiave pubblica consente di ridurne la dimensione da 520 bit a 264 bit.

Utilizziamo il prefisso 0x02 per un y pari e 0x03 per un y dispari. Questa è la forma compressa della chiave pubblica.

### Fase 2: Hash della chiave pubblica compressa

![immagine](assets/image/section5/3.JPG)
Il **hash** della chiave pubblica compressa viene eseguito utilizzando la funzione SHA256. Successivamente, viene applicata la funzione RIPEMD160 al risultato.

### Step 3: Il payload = Carico utile dell'indirizzo

![image](assets/image/section5/4.JPG)

Il risultato binario di RIPEMD160(SHA256(K)) viene suddiviso in gruppi di 5 bit. Ogni gruppo viene poi convertito in base16 (Esadecimale) e/o in base 10.

### Step 4: Aggiunta dei metadati per il calcolo del checksum con il programma BCH

![image](assets/image/section5/5.JPG)

Nel caso degli indirizzi legacy, utilizziamo il doppio hash SHA256 per generare il checksum dell'indirizzo. Tuttavia, per gli indirizzi Segwit V0 e V1, facciamo uso della tecnologia di checksum BCH per garantire la rilevazione degli errori. Il programma BCH è in grado di suggerire e correggere gli errori con una probabilità di errore estremamente bassa. Attualmente, il programma BCH viene utilizzato per rilevare e suggerire le modifiche da apportare, ma non le esegue automaticamente al posto dell'utente.

Il programma BCH richiede diverse informazioni in input, tra cui l'HRP (Human Readable Part) che deve essere esteso. L'estensione dell'HRP consiste nel codificare ogni lettera in base 2 secondo il loro codice ASCII. Quindi, prendendo i primi 3 bit del risultato per ogni lettera e convertendoli in base 10 (in blu nell'immagine). Inserire un separatore 0. Poi concatenare i 5 bit finali di ogni lettera precedentemente convertiti in base 10 (in giallo nell'immagine).

L'estensione dell'HRP in base 10 consente di isolare gli ultimi cinque bit di ogni carattere, rafforzando così il checksum.

La versione Segwit V0 è rappresentata dal codice 00 e il "payload" è in nero, in base 10. Seguito da sei caratteri riservati per il checksum.

### Step 5: Calcolo del checksum con il programma BCH

![image](assets/image/section5/6.JPG)

L'input contenente i metadati viene quindi sottoposto al programma BCH per ottenere il checksum in base 10.

Qui abbiamo il checksum.

### Step 6: Costruzione dell'indirizzo e conversione in Bech32

![image](assets/image/section5/7.JPG)

La concatenazione della versione, del payload e del checksum consente di costruire l'indirizzo. I caratteri in base 10 vengono quindi convertiti in caratteri bech32 utilizzando una tabella di corrispondenza. L'alfabeto bech32 include tutti i caratteri alfanumerici, ad eccezione di 1, b, i e o, per evitare confusione.

### Step 7: Aggiunta dell'HRP e del separatore

![image](assets/image/section5/8.JPG)

In rosa il checksum.
In nero, il payload = l'hash della chiave pubblica.
In blu, la versione.
Il tutto viene convertito in Bech32, poi viene aggiunto 'bc' per bitcoin e '1' come separatore e qui c'è l'indirizzo.
Così, abbiamo attraversato i passaggi per la costruzione di un indirizzo di ricezione, l'utilizzo della tecnologia di checksum BCH e la costruzione di un indirizzo che inizia con bc1q o bc1p utilizzando la variante BCH32 della base 32 specifica per Bitcoin.

## Riepilogo della crittografia per i portafogli Bitcoin

![sintesi della formazione](https://youtu.be/NkAYoVUMvOs)

Le funzioni di hash utilizzate nel protocollo Bitcoin hanno caratteristiche necessarie per la sicurezza del protocollo. Devono essere irreversibili (= resistenza alla preimmagine), resistenti alla falsificazione, resistenti alla collisione e alla seconda preimmagine.

![immagine](assets/image/section5/11.JPG)

Un altro metodo crittografico ampiamente utilizzato nel protocollo Bitcoin è il metodo delle firme digitali.

![immagine](assets/image/section5/12.JPG)

Durante tutto questo corso, abbiamo approfondito il portafoglio deterministico gerarchico (HD) con il BIP32. L'entropia svolge un ruolo centrale in questo tipo di portafoglio, poiché viene utilizzata per generare una frase mnemonica da un numero casuale.

Questo numero casuale viene quindi formattato in un formato di 256 bit utilizzando la funzione di hash SHA256. Il checksum corrisponde agli 8 bit iniziali di questo risultato.
La frase mnemonica corrisponde alla concatenazione del numero casuale con il checksum. Grazie alla lista di 2048 parole fornite nel BIP39, questa frase mnemonica può essere codificata in una serie di parole facili da ricordare. La frase mnemonica, insieme a una eventuale passphrase, sono necessarie per generare il seed del portafoglio. La passphrase agisce come un sale crittografico che aggiunge un ulteriore livello di protezione al portafoglio.

La funzione pbkdf2 viene utilizzata per generare il seed dalla frase mnemonica e dalla passphrase, utilizzando un HMAC-SHA512 e 2048 iterazioni. La chiave master e il codice di catena master vengono quindi derivati da questo seed utilizzando nuovamente la funzione HMAC-SHA512 con la frase "bitcoin seed". La chiave privata master e il codice di catena master sono gli elementi più alti nella gerarchia del portafoglio HD.

La derivazione di una chiave figlia dipende da diversi fattori, tra cui la chiave genitore e il corrispondente codice di catena. Una chiave estesa viene ottenuta concatenando una chiave genitore con il suo codice di catena, mentre una chiave master è una chiave separata.
Per derivare un indirizzo, la chiave pubblica compressa viene prima hashata utilizzando SHA256 e RIPMD160, quindi viene calcolato un checksum. L'hash doppio SHA256 viene utilizzato per calcolare il checksum nel caso di uno standard legacy, mentre il programma BCH (Bose-Chaudhuri-Hocquenghem) viene utilizzato per calcolare il checksum nel caso di uno standard segwit. Successivamente, viene utilizzata una rappresentazione in formato base 58 per uno standard legacy, mentre il formato bech32 viene utilizzato per uno standard segwit, al fine di ottenere l'indirizzo del portafoglio HD.
![image](assets/image/section5/13.JPG)

In sintesi, abbiamo esplorato in dettaglio le funzioni di hash e le loro caratteristiche, così come le firme digitali e le curve ellittiche. Successivamente, ci siamo immerse nell'universo del portafoglio deterministico gerarchico (HD) con il BIP32, utilizzando l'entropia e la passphrase per generare il seed del portafoglio. Abbiamo anche imparato come derivare le chiavi figlie e ottenere l'indirizzo del portafoglio HD. Spero che queste informazioni ti siano state utili e ti incoraggio ora a procedere con la valutazione per testare le tue conoscenze acquisite durante il corso Crypto 301. Grazie per la tua attenzione.
