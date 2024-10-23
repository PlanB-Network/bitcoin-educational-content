---
name: Introduzione agli algoritmi crittografici di Bitcoin
goal: Comprendere la creazione di un portafoglio Bitcoin da una prospettiva crittografica
objectives:
  - Demistificare la terminologia crittografica legata a Bitcoin.
  - Padroneggiare la creazione di un portafoglio Bitcoin.
  - Comprendere la struttura di un portafoglio Bitcoin.
  - Comprendere gli indirizzi e i percorsi di derivazione.
---

# Un viaggio nella crittografia

Sei affascinato da Bitcoin? Ti chiedi come funziona un portafoglio Bitcoin? Preparati per intraprendere un affascinante viaggio nella crittografia! Loïc, il nostro esperto, ti guiderà attraverso le complessità della creazione di un portafoglio Bitcoin, svelando i misteri dietro termini tecnici intimidatori come hash, derivazione delle chiavi e curve ellittiche.

Questo corso non solo ti fornirà le conoscenze per comprendere la struttura di un portafoglio Bitcoin, ma ti preparerà anche a approfondire il mondo affascinante della crittografia. Quindi, sei pronto per intraprendere questo viaggio? Unisciti a noi e trasforma la tua curiosità in competenza!

+++

# Introduzione
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Introduzione alla crittografia
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Questo corso è adatto a te? SÌ!


Siamo lieti di darti il benvenuto al nuovo corso di formazione dal titolo "Crypto 301: Introduzione alla crittografia e ai portafogli HD ", guidato dall'esperto del settore, Loïc Morel. Questo corso ti immergerà nel mondo affascinante della crittografia, la disciplina fondamentale della matematica che garantisce la crittografia e la sicurezza dei tuoi dati.

Nella nostra vita quotidiana, e in particolare nel campo di Bitcoin, la crittografia svolge un ruolo cruciale. Concetti legati alla crittografia, come chiavi private, chiavi pubbliche, indirizzi, percorsi di derivazione, seed ed entropia, sono al centro dell'uso e della creazione di un portafoglio Bitcoin. Durante questo corso, Loïc spiegherà in dettaglio come vengono generate le chiavi private e come sono collegate agli indirizzi. Loïc dedicherà anche un'ora a spiegare i dettagli matematici delle curve ellittiche. Inoltre, comprenderai perché l'uso di HMAC SHA512 è importante per la sicurezza del tuo portafoglio e qual è la differenza tra un seed e una frase mnemonica.

L'obiettivo finale di questa formazione è consentirti di comprendere i processi tecnici coinvolti nella creazione di un portafoglio HD e i metodi crittografici utilizzati. Nel corso degli anni, i portafogli Bitcoin sono evoluti per diventare più facili da usare, più sicuri e standardizzati grazie a specifici BIP. Loïc ti aiuterà a comprendere questi BIP per cogliere le scelte fatte dagli sviluppatori di Bitcoin e dai crittografi. Come tutti i corsi offerti dalla nostra università ache questo è completamente gratuito ed open source. Ci auguriamo di ricevere i tuoi feedback alla fine di questo entusiasmante corso.

### La parola passa a te, professore!

Ciao a tutti, sono Loïc Morel, la vostra guida in questa esplorazione tecnica sulla crittografia utilizzata nei portafogli Bitcoin.

Il nostro viaggio inizia dalle funzioni di hash crittografiche. Insieme, analizzeremo il funzionamento interno dell'essenziale SHA256 ed esploreremo vari algoritmi dedicati alla derivazione.

Continueremo la nostra avventura decifrando il misterioso mondo delle firme digitali. Scoprirai come la magia delle curve ellittiche si applica a queste firme e faremo luce su come calcolare la chiave pubblica dalla chiave privata. E naturalmente, approfondiremo il processo di firma digitale.
Successivamente, faremo un salto indietro nel tempo per vedere l'evoluzione dei portafogli Bitcoin e ci addentreremo nei concetti di entropia e numeri casuali. Esamineremo la celebre frase mnemonica e l'utilizzo di una passphrase. Avrai persino l'opportunità di vivere qualcosa di unico creando un seed da 128 lanci di dadi!

Con queste solide basi, saremo pronti per la parte cruciale: creare un portafoglio Bitcoin. Dalla nascita del seed e della chiave principale, allo studio delle chiavi estese e alla derivazione delle coppie di chiavi figlie, ogni passo sarà analizzato nel dettaglio. Discuteremo anche la struttura del portafoglio e i percorsi di derivazione.

Per concludere, esamineremo gli indirizzi Bitcoin. Spiegheremo come vengono creati e come svolgono un ruolo essenziale nel funzionamento dei portafogli Bitcoin.

Unisciti a me in questo affascinante viaggio e preparati ad esplorare il mondo della crittografia come mai prima d'ora. Lascia i preconcetti alla porta e apri la tua mente a un nuovo modo di comprendere Bitcoin e la sua struttura fondamentale.

# Funzioni di Hash
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Introduzione alle funzioni di hash crittografiche correlate a Bitcoin
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Benvenuti alla sessione odierna dedicata a un'immersione approfondita nel mondo crittografico delle funzioni di hash, una pietra angolare cruciale della sicurezza del protocollo Bitcoin. Immaginate una funzione di hash come un efficientissimo robot crittografico che trasforma informazioni di qualsiasi dimensione in un'impronta digitale unica e di dimensioni fisse, chiamata "hash", "digest" o "checksum".
In sintesi, una funzione di hash prende un messaggio di input di dimensione arbitraria e lo converte in un'impronta digitale di dimensioni fisse.

Descrivere il profilo delle funzioni di hash crittografiche richiede la comprensione di due qualità essenziali: la loro irreversibilità e la loro resistenza alla falsificazione.

L'irreversibilità, o resistenza alla preimmagine, significa che calcolare l'output dato l'input è facile, ma calcolare l'input dato l'output è impossibile.
È una funzione unidirezionale.

![immagine](assets/image/section1/0.webp)

La resistenza alla falsificazione deriva dal fatto che anche la più piccola modifica dell'input produrrà un output profondamente diverso.
Queste funzioni consentono di verificare l'integrità del software scaricato.

![immagine](assets/image/section1/1.webp)

Un'altra caratteristica cruciale che possiedono è la resistenza alle collisioni e alla seconda preimmagine. Una collisione si verifica quando due input distinti producono lo stesso output.

Certamente, nell'universo dell'hashing, le collisioni sono inevitabili, ma una buona funzione di hash crittografica le riduce significativamente. Il rischio deve essere così basso da poter essere considerato trascurabile. È come se ogni hash fosse una casa in una vasta città; nonostante il grande numero di case, una buona funzione di hash assicura che ogni casa abbia un indirizzo unico.

La resistenza alla seconda preimmagine dipende dalla resistenza alle collisioni; se c'è resistenza alle collisioni, allora c'è resistenza alla seconda preimmagine.
Data un'informazione di input che ci viene imposta, dobbiamo trovare un secondo input, diverso dal primo, che produca una collisione nell'hash di output della funzione. La resistenza alla seconda preimmagine è simile alla resistenza alle collisioni, tranne che l'input ci viene imposto.

Ora navigheremo le acque tumultuose delle funzioni di hash obsolete. SHA0, SHA1 e MD5 sono ora considerate gusci arrugginiti nell'oceano dell'hashing crittografico. Spesso vengono sconsigliate poiché hanno perso la loro resistenza alle collisioni. Il principio dei cassetti spiega perché, nonostante i nostri migliori sforzi, l'evitare le collisioni è impossibile a causa della limitazione della dimensione dell'output. Per essere considerata veramente sicura, una funzione di hash deve resistere alle collisioni, alle seconde preimmagini e alle preimmagini.

Un elemento chiave nel protocollo Bitcoin, la funzione di hash SHA-256 è il capitano della nave. Altre funzioni, come SHA-512, vengono utilizzate per la derivazione con HMAC e PBKDF. Inoltre, RIPMD160 viene utilizzato per ridurre una impronta a 160 bit. Quando ci riferiamo a HASH256 e HASH160, ci riferiamo all'uso del doppio hashing con SHA-256 e RIPMD.
Per HASH256, si intende un doppio hash del messaggio utilizzando la funzione SHA256.
$$
SHA256(SHA256(messaggio))
$$
Per HASH160, si intende un doppio hash del messaggio utilizzando prima SHA256, poi RIPMD160.
$$
RIPMD160(SHA256(messaggio))
$$
L'uso di HASH160 è particolarmente vantaggioso in quanto garantisce la sicurezza di SHA-256 riducendo al contempo la dimensione dell'impronta.

In sintesi, l'obiettivo finale di una funzione di hash crittografica è trasformare informazioni di dimensioni arbitrarie in un'impronta di dimensioni fisse. Per essere riconosciuta come sicura, deve avere diverse caratteristiche: irreversibilità, resistenza alle manipolazioni, resistenza alle collisioni e resistenza alle seconde preimmagini.

Alla fine di questa esplorazione, abbiamo svelato i misteri delle funzioni di hash crittografiche, evidenziato il loro utilizzo nel protocollo Bitcoin e analizzato i loro obiettivi specifici. Abbiamo appreso che per considerare sicure le funzioni di hash devono essere resistenti alle preimmagini, alle seconde preimmagini, alle collisioni e alle manipolazioni. Abbiamo anche esaminato la gamma delle funzioni di hash utilizzate nel protocollo Bitcoin. Nella prossima sessione, approfondiremo il nucleo della funzione di hash SHA256 e scopriremo gli affascinanti principi matematici che le conferiscono le sue caratteristiche uniche.

## Il funzionamento interno di SHA256
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>


Benvenuti al proseguimento del nostro affascinante viaggio attraverso i labirinti crittografici della funzione di hash. Oggi sveliamo i misteri di SHA256, un processo complesso ma ingegnoso che abbiamo introdotto in precedenza.
-> 950 + 1 + P + 64 = 1024-> P = 1024 - 1 - 64 - 950
-> P = 9

Pertanto, sono necessari 9 bit di padding per ottenere un messaggio che sia un multiplo di 512.

E ora?
Subito dopo il messaggio iniziale, è necessario aggiungere il separatore 1 seguito da P, che nel nostro esempio sono nove 0.

```
messaggio + 1 000 000 000
```

#### Padding della dimensione

Passiamo ora alla seconda fase di pre-elaborazione, che prevede l'aggiunta della rappresentazione binaria della dimensione del messaggio iniziale in bit.

Riprendiamo l'esempio con un input di 950 bit:


La rappresentazione binaria del numero 950 è: 11 1011 0110

Utilizziamo i nostri 64 bit riservati dal passaggio precedente. Aggiungiamo zeri per arrotondare i nostri 64 bit all'input equalizzato. Quindi, uniamo il messaggio iniziale, i bit di padding e il padding della dimensione per ottenere il nostro input equalizzato.

Ecco il risultato:

![image](assets/image/section1/4.webp)

### Elaborazione

#### Comprensione dei prerequisiti

##### Costanti e vettori di inizializzazione

Ora ci stiamo preparando per i primi passi dell'elaborazione della funzione SHA-256. Proprio come in una buona ricetta, abbiamo bisogno di alcuni ingredienti di base, che chiamiamo costanti e vettori di inizializzazione.

I vettori di inizializzazione, da A a H, sono i primi 32 bit delle parti decimali delle radici quadrate dei primi 8 numeri primi. Serviranno come valori di base nei primi passaggi di elaborazione. I loro valori sono in formato esadecimale.

Le costanti K, da 0 a 63, rappresentano i primi 32 bit delle parti decimali delle radici cubiche dei primi 64 numeri primi. Vengono utilizzate in ogni iterazione della funzione di compressione. Anche i loro valori sono in formato esadecimale.

![image](assets/image/section1/5.webp)

##### Operazioni utilizzate

All'interno della funzione di compressione, utilizziamo operatori specifici come XOR, AND e NOT. Elaboriamo i bit uno per uno in base alla loro posizione, utilizzando l'operatore XOR e una tabella di verità. L'operatore AND viene utilizzato per restituire 1 solo se entrambi gli operandi sono uguali a 1, e l'operatore NOT viene utilizzato per restituire il valore opposto di un operando. Utilizziamo anche l'operazione SHR per spostare i bit verso destra di un numero scelto.

La tabella di verità:

![image](assets/image/section1/6.webp)

Operazioni di spostamento dei bit:

![image](assets/image/section1/7.webp)

#### La funzione di compressione

Prima di applicare la funzione di compressione, dividiamo l'input in blocchi di 512 bit. Ogni blocco verrà elaborato indipendentemente dagli altri.

Ogni blocco di 512 bit viene poi ulteriormente diviso in pezzi di 32 bit chiamati W. In questo modo, W(0) rappresenta i primi 32 bit del blocco di 512 bit. W(1) rappresenta i successivi 32 bit, e così via, fino a raggiungere i 512 bit del blocco.

Una volta definiti tutte le costanti K e i pezzi W, possiamo procedere con i seguenti calcoli per ogni pezzo W in ogni round.

Eseguiamo 64 round di calcoli nella funzione di compressione. Nell'ultimo round, al livello "Output della funzione", avremo uno stato intermedio che verrà aggiunto allo stato iniziale della funzione di compressione.

Quindi, ripetiamo tutti questi passaggi della funzione di compressione sul prossimo blocco di 512 bit, fino all'ultimo blocco.
Tutte le aggiunte nella funzione di compressione sono somme modulo 2^32 per mantenere sempre una somma di 32 bit.

![immagine](assets/image/section1/9.webp)

![immagine](assets/image/section1/8.webp)

##### Un round della funzione di compressione

![immagine](assets/image/section1/11.webp)

![immagine](assets/image/section1/10.webp)

La funzione di compressione verrà eseguita 64 volte. Abbiamo i nostri pezzi W e le nostre costanti K precedentemente definite come input.
I quadrati/croci rossi corrispondono a una somma modulo 2^32 di 32 bit.

Gli input A, B, C, D, E, F, G, H saranno associati a un valore di 32 bit per ottenere un totale di 32 * 8 = 256 bit.
Abbiamo anche una nuova sequenza A, B, C, D, E, F, G, H come output. Questo output verrà quindi utilizzato come input per il round successivo e così via fino alla fine del 64° round.

I valori della sequenza di input per il primo round della funzione di compressione corrispondono ai vettori di inizializzazione predefiniti menzionati in precedenza.
Come promemoria, i vettori di inizializzazione rappresentano i primi 32 bit delle parti decimali delle radici quadrate dei primi 8 numeri primi.

Ecco un esempio di round:

![immagine](assets/image/section1/12.1.webp)

##### Stato intermedio

Come promemoria, il messaggio è diviso in blocchi di 512 bit, che vengono poi divisi in pezzi da 32 bit. Per ogni blocco di 512 bit, applichiamo i 64 round della funzione di compressione.
Lo stato intermedio corrisponde alla fine dei 64 round di un blocco. I valori della sequenza di output di questo 64° round vengono utilizzati come valori iniziali per la sequenza di input del primo round del blocco successivo.

![immagine](assets/image/section1/12.2.webp)

#### Panoramica della funzione di hash

![immagine](assets/image/section1/13.webp)

Possiamo notare che l'output del primo pezzo di messaggio di 512 bit corrisponde ai nostri vettori di inizializzazione come input per il secondo pezzo di messaggio di 512 bit, e così via.

L'output dell'ultimo round, dell'ultimo pezzo, corrisponde al risultato finale della funzione SHA256.

In conclusione, vorremmo sottolineare il ruolo cruciale dei calcoli eseguiti nelle caselle CH, MAJ, σ0 e σ1. Queste operazioni, tra le altre, sono le guardie che garantiscono la robustezza della funzione di hash SHA256 contro gli attacchi, rendendola una scelta preferita per la sicurezza di molti sistemi digitali, specialmente all'interno del protocollo Bitcoin. È evidente che, sebbene complessa, la bellezza di SHA256 risiede nella sua capacità di trovare l'input dall'hash, mentre verificare l'hash per un dato input è un'azione meccanicamente semplice.

## Gli algoritmi utilizzati per la derivazione
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

Gli algoritmi di derivazione HMAC e PBKDF2 sono componenti chiave nel meccanismo di sicurezza del protocollo Bitcoin. Prevengono una varietà di potenziali attacchi e garantiscono l'integrità dei portafogli Bitcoin.

HMAC e PBKDF2 sono strumenti crittografici utilizzati per varie operazioni in Bitcoin. HMAC viene utilizzato principalmente per contrastare gli attacchi di estensione della lunghezza durante la derivazione di portafogli deterministici gerarchici (HD), mentre PBKDF2 viene utilizzato per convertire una frase mnemonica in un seed.

#### HMAC-SHA512

La coppia HMAC-SHA512 ha due input: un messaggio m (Input 1) e una chiave K scelta arbitrariamente dall'utente (Input 2). Ha anche un output di dimensione fissa: 512 bit.


Notiamo:
- m: messaggio di dimensione arbitraria scelto dall'utente (input 1)
- K: chiave arbitraria scelta dall'utente (input 2)
- K': chiave K equalizzata. È stata adattata alla dimensione B dei blocchi.
- ||: operazione di concatenazione.
- opad: costante definita dal byte 0x5c ripetuto B volte.
- ipad: costante definita dal byte 0x36 ripetuto B volte.
- B: dimensione dei blocchi della funzione hash utilizzata.

HMAC-SHA512, che prende un messaggio e una chiave come input, genera un output di dimensione fissa. Per garantire l'uniformità, la chiave viene adattata in base alla dimensione dei blocchi utilizzati nella funzione di hash. Nel contesto della derivazione del portafoglio HD, viene utilizzato HMAC-SHA-512. Opera con blocchi di 1024 bit (128 byte) e adatta di conseguenza la chiave. Utilizza le costanti OPAD (0x5c) e IPAD (0x36), ripetute se necessario per migliorare la sicurezza.

Il processo HMAC-SHA-512 prevede la concatenazione del risultato di SHA-512 applicato alla chiave XOR OPAD e la chiave XOR IPAD con il messaggio. Quando viene utilizzato con blocchi di 1024 bit (128 byte), la chiave di input viene riempita con zeri se necessario, quindi XORata con IPAD e OPAD. La chiave modificata viene quindi concatenata con il messaggio.

L'inclusione di un salt nel codice stringa aumenta la sicurezza delle chiavi derivate. Senza di esso, un attacco potrebbe compromettere l'intero portafoglio e rubare tutti i bitcoin.

PBKDF2 viene utilizzato per convertire una frase mnemonica in un seed. Questo algoritmo esegue 2048 round utilizzando HMAC SHA512. Attraverso questi algoritmi di derivazione, input diversi possono produrre un output unico e fisso, che mitiga il problema di possibili attacchi di estensione della lunghezza sulle funzioni della famiglia SHA-2.
Un attacco di estensione della lunghezza sfrutta una proprietà specifica di alcune funzioni hash crittografiche. In un simile attacco, un attaccante che possiede già l'hash di un messaggio sconosciuto può utilizzarlo per calcolare l'hash di un messaggio più lungo, che è un'estensione del messaggio originale. Questo è spesso possibile senza conoscere il contenuto del messaggio originale, il che può portare a significative vulnerabilità di sicurezza se questo tipo di funzione hash viene utilizzato per compiti come la verifica dell'integrità.

In conclusione, gli algoritmi HMAC e PBKDF2 svolgono un ruolo essenziale nella sicurezza della derivazione del portafoglio HD nel protocollo Bitcoin. HMAC-SHA-512 viene utilizzato per proteggersi dagli attacchi di estensione della lunghezza, mentre PBKDF2 consente la conversione della frase mnemonica in un seed. Il codice stringa aggiunge una fonte aggiuntiva di entropia nella derivazione delle chiavi, garantendo la robustezza del sistema.

# Firme digitali
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Firme digitali e curve ellittiche
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Dove vengono conservati questi famosi bitcoin? Non in un portafoglio Bitcoin, come si potrebbe pensare. In realtà, un portafoglio Bitcoin conserva le chiavi private necessarie per dimostrare la proprietà dei bitcoin. I bitcoin stessi sono registrati sulla blockchain, un database decentralizzato che archivia tutte le transazioni.
Nel sistema Bitcoin, l'unità di conto è il bitcoin (nota la "b" minuscola). È divisibile fino a otto decimali, con la più piccola unità chiamata satoshi. UTXO, o "Unspent Transaction Outputs" (output di transazione non spesi), rappresentano gli output di transazione non spesi appartenenti a una chiave pubblica che è collegata matematicamente ad una chiave privata. Per spendere questi bitcoin, è necessario soddisfare la condizione di spesa della transazione. Una tipica condizione di spesa consiste nel dimostrare al resto della rete che l'utente è il legittimo proprietario della chiave pubblica associata all'UTXO. Per fare ciò, l'utente deve dimostrare di possedere la chiave privata corrispondente alla chiave pubblica collegata a ciascun UTXO senza rivelare la chiave privata.

È qui che entra in gioco la firma digitale. Serve come prova matematica del possesso di una chiave privata associata ad una specifica chiave pubblica. Questa tecnica di protezione dei dati si basa principalmente su un affascinante campo della crittografia chiamato crittografia a curva ellittica (ECC).

La firma può essere verificata matematicamente da altri partecipanti nella rete Bitcoin.

Per garantire la sicurezza delle transazioni, Bitcoin si basa su due protocolli di firma digitale: ECDSA (Elliptic Curve Digital Signature Algorithm) e Schnorr. ECDSA è stato un protocollo di firma integrato in Bitcoin fin dal suo lancio nel 2009, mentre le firme Schnorr sono state aggiunte più di recente nel novembre 2021. Sebbene entrambi i protocolli si basino sulla crittografia a curva ellittica ed utilizzino meccanismi matematici simili, differiscono principalmente per la struttura della firma.

In questo corso, presenteremo l'algoritmo ECDSA.

### Cosa è una curva ellittica?

La crittografia a curva ellittica è un insieme di algoritmi che utilizzano una curva ellittica per le sue varie proprietà geometriche e matematiche in un contesto crittografico, con la sicurezza basata sulla difficoltà di calcolare il logaritmo discreto.

Le curve ellittiche sono utili in una varietà di applicazioni crittografiche nel protocollo Bitcoin, che vanno dagli scambi di chiavi alla crittografia asimmetrica e alle firme digitali.

Le curve ellittiche hanno proprietà interessanti:

- Simmetria: Qualsiasi linea non verticale che interseca due punti sulla curva ellittica intersecherà la curva in un terzo punto.
- Qualsiasi linea non verticale tangente alla curva in un punto intersecherà sempre la curva in un secondo punto unico.

Il protocollo Bitcoin utilizza una specifica curva ellittica chiamata Secp256k1 per le sue operazioni crittografiche.

Prima di approfondire questi meccanismi di firma, è importante capire cosa sia una curva ellittica. Una curva ellittica è definita dall'equazione y² = x³ + ax + b. Ogni punto su questa curva ha una simmetria distintiva che è fondamentale per la sua utilità in crittografia.

Infine, varie curve ellittiche sono riconosciute come sicure per l'uso crittografico. La più conosciuta potrebbe essere la curva secp256r1. Tuttavia, per Bitcoin, Satoshi Nakamoto ha optato per una curva diversa: secp256k1.

Questa curva è definita dai parametri a=0 e b=7, e la sua equazione è y² = x³ + 7 modulo n, dove n rappresenta il numero primo che determina l'ordine della curva.

La prima immagine rappresenta la curva secp256k1 sul campo reale e la sua equazione.
La seconda immagine è una rappresentazione della curva secp256k1 sul campo ZP, il campo dei numeri naturali positivi, modulo p dove p è un numero primo. Assomiglia a una nuvola di punti. Utilizziamo questo campo di numeri naturali positivi per evitare approssimazioni.
p è un numero primo ed è l'ordine della curva che viene utilizzato.
Infine, l'equazione utilizzata nel protocollo Bitcoin è: $$y^2 = (x^3 + 7) mod(p)$$
L'equazione della curva ellittica in Bitcoin corrisponde all'ultima equazione nell'immagine precedente.

Nella prossima sezione di questo corso, utilizzeremo curve che sono nel campo reale semplicemente per facilitare la comprensione.

## Calcolo della chiave pubblica dalla chiave privata
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>


Per iniziare, immergiamoci nel mondo dell'Elliptic Curve Digital Signature Algorithm (ECDSA). Bitcoin utilizza questo algoritmo di firma digitale per collegare chiavi private e pubbliche. In questo sistema, la chiave privata è un numero casuale o pseudo-casuale di 256 bit. Il numero totale di possibilità per una chiave privata è teoricamente 2^256, ma in realtà è leggermente inferiore a questo valore. Per essere precisi, alcune chiavi private di 256 bit non sono valide per Bitcoin.

Per essere compatibile con Bitcoin, una chiave privata deve essere compresa tra 1 e n-1, dove n rappresenta l'ordine della curva ellittica. Ciò significa che il numero totale di possibilità per una chiave privata di Bitcoin è quasi uguale a 1,158 x 10^77. Per mettere le cose in prospettiva, è approssimativamente lo stesso numero di atomi presenti nell'universo osservabile.

![immagine](assets/image/section2/3.webp)

La chiave privata unica, indicata come k, viene quindi utilizzata per determinare una chiave pubblica.

La chiave pubblica, indicata come K, è un punto sulla curva ellittica che deriva dalla chiave privata utilizzando algoritmi irreversibili come ECDSA. Quando abbiamo conoscenza della chiave privata, è molto facile recuperare la chiave pubblica, ma quando abbiamo solo la chiave pubblica, è impossibile recuperare la chiave privata. Questa irreversibilità è la base della sicurezza del portafoglio Bitcoin.

La chiave pubblica è lunga 512 bit in quanto corrisponde a un punto sulla curva con una coordinata x di 256 bit e una coordinata y di 256 bit. Tuttavia, può essere compressa in un numero di 264 bit.

![immagine](assets/image/section2/4.webp)

Il punto generatore (G) è il punto sulla curva da cui vengono generate tutte le chiavi pubbliche nel protocollo Bitcoin. Ha coordinate x e y specifiche, di solito rappresentate in esadecimale. Per secp256k1, le coordinate di G sono, in esadecimale:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Questo punto è utile per derivare tutte le chiavi pubbliche. Per calcolare la chiave pubblica K, basta moltiplicare il punto G per la chiave privata k, in modo che: K = k.G

Studieremo ora come aggiungere e moltiplicare punti sulle curve ellittiche.

#### Aggiunta e raddoppio di punti sulle curve ellittiche

##### Aggiunta di due punti M + L

Una delle proprietà notevoli delle curve ellittiche è che una linea non verticale che interseca la curva in due punti intersecherà anche un terzo punto, chiamato punto O nel nostro esempio. Questa proprietà viene utilizzata per determinare il punto U, che è l'opposto del punto O.

M + L = U

![immagine](assets/image/section2/5.webp)

##### Aggiunta di un punto a se stesso = Raddoppio del punto
Aggiungere un punto G a se stesso viene fatto disegnando una tangente alla curva in quel punto. Questa tangente, secondo le proprietà delle curve ellittiche, intersecherà la curva in un secondo punto unico -J. L'opposto di questo punto, J, è il risultato dell'aggiunta del punto G a se stesso.
G + G = J

In effetti, il punto G è il punto di partenza per il calcolo di tutte le chiavi pubbliche degli utenti del sistema Bitcoin.

![immagine](assets/image/section2/6.webp)

#### Moltiplicazione scalare su curve ellittiche

La moltiplicazione scalare di un punto per n è equivalente all'aggiunta di quel punto a se stesso n volte.

Similmente al raddoppio del punto, la moltiplicazione scalare del punto G per un punto n viene fatta disegnando una tangente alla curva nel punto G. Questa tangente, secondo le proprietà delle curve ellittiche, intersecherà la curva in un secondo punto unico -2G. L'opposto di questo punto, 2G, è il risultato dell'aggiunta del punto G a se stesso.

Se n = 4, l'operazione viene ripetuta fino a raggiungere 4G.

![immagine](assets/image/section2/7.webp)

Ecco un esempio di calcolo per 3G:

![immagine](assets/image/section2/8.webp)

Queste operazioni su punti di una curva ellittica sono alla base del calcolo delle chiavi pubbliche. Derivare una chiave pubblica conoscendo la chiave privata è molto facile.
Una chiave pubblica è un punto sulla curva ellittica; è il risultato della nostra aggiunta e raddoppio del punto G k volte. Con k = chiave privata.

In questo esempio:

- La chiave privata k = 4
- La chiave pubblica K = kG = 4G

![immagine](assets/image/section2/9.webp)

Conoscendo la chiave privata k, è facile calcolare la chiave pubblica K. Tuttavia, è impossibile recuperare la chiave privata basandosi sulla chiave pubblica. Questo è il risultato di un'aggiunta o di un raddoppio di punti?

Nella nostra prossima lezione, esploreremo come viene creata una firma digitale utilizzando l'algoritmo ECDSA con una chiave privata per spendere bitcoin.

## Firma con la chiave privata
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Il processo di firma digitale è un metodo chiave per dimostrare di essere il detentore di una chiave privata senza rivelarla. Questo viene realizzato utilizzando l'algoritmo ECDSA, che prevede la determinazione di un nonce unico, il calcolo di un numero specifico V e la creazione di una firma digitale composta da due parti, S1 e S2.
È fondamentale utilizzare sempre un nonce unico per evitare attacchi di sicurezza. Un esempio notorio di ciò che può accadere quando questa regola non viene seguita è l'hacking della PlayStation 3, compromessa a causa del riutilizzo del nonce.

![](assets/image/section2/10.webp)

Passaggi:

- Determinare un nonce v, che è un numero casuale unico.
  Nonce = Numero Utilizzato Solo Una Volta.
  Viene determinato da chi esegue la firma.
- Calcolare aggiungendo e raddoppiando punti su una curva ellittica dal punto G, la posizione di V sulla curva ellittica.
  In modo tale che V = v.G
  x e y sono le coordinate di V sul piano.
- Calcolare S1.
  S1 = x mod n con n = l'ordine della curva e x una coordinata di V sul piano.
  Nota: Il numero di possibili chiavi pubbliche è maggiore del numero di punti sulla curva ellittica nel campo finito di numeri interi positivi utilizzato in Bitcoin.
  L'ordine della curva corrisponde solo alle possibilità che la chiave pubblica può assumere sulla curva.
- Calcolare S2.
  H(Tx) = Hash della transazione
k = la chiave privata- Calcola la firma: la concatenazione di S1 + S2.
- Calcola P, il calcolo della verifica della firma.
  K = la chiave pubblica

Ad esempio, per ottenere la chiave pubblica 3G, tracci una tangente al punto G, calcola l'opposto di -G per ottenere 2G, e poi aggiungi G e 2G. Per effettuare una transazione, devi dimostrare di conoscere il numero 3 sbloccando i bitcoin associati alla chiave pubblica 3G.
Per creare una firma digitale e dimostrare di conoscere la chiave privata associata alla chiave pubblica 3G, calcoli prima un nonce, quindi il punto V associato a questo nonce (nell'esempio dato, è 4G). Quindi, calcoli il punto T aggiungendo la chiave pubblica 3G e il punto V, che dà 7G.

![image](assets/image/section2/11.webp)

Semplifichiamo il processo di firma digitale.
Nell'immagine precedente, la chiave privata k = 3.
Possiamo facilmente calcolare la chiave pubblica K associata a questa chiave privata: K = 3G.
Quindi, generiamo un nonce in modo pseudo-casuale: v = 4.
Da questo nonce, è possibile calcolare V in modo tale che: V = v.G = 4G.

Da questo punto V, calcoliamo il punto T in modo tale che:
T = t.G = 7G (con t = 7).

Ora è il momento di procedere con la verifica della firma digitale.

Verificare una firma digitale è un passaggio cruciale nell'utilizzo dell'algoritmo ECDSA, che consente di confermare l'autenticità di un messaggio firmato senza avere bisogno della chiave privata del mittente. Ecco come funziona nel dettaglio:

Nel nostro esempio, abbiamo due valori importanti: t e V.
t è un valore numerico (7 in questo esempio), e V è un punto sulla curva ellittica (rappresentato qui da 4G). Questi valori vengono generati durante la creazione della firma digitale e vengono quindi inviati insieme al messaggio per consentire la verifica.

Quando il verificatore riceve il messaggio, riceverà anche questi due valori, t e V.

Ecco i passaggi che il verificatore seguirà per convalidare la firma:

1. Prima di tutto, calcolerà l'hash del messaggio, che chiameremo H.
2. Quindi, calcolerà u1 e u2. Per fare ciò, utilizzerà le seguenti formule:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Dove S2 è la seconda parte della firma digitale, n è l'ordine della curva ellittica e (S2)^-1 è l'inverso di S2 mod n.
3. Il verificatore calcolerà quindi un punto P' sulla curva ellittica utilizzando la formula: P' = u1 _ G + u2 _ K
   - G è il punto generatore della curva
   - K è la chiave pubblica del mittente
4. Il verificatore calcolerà quindi I', che è semplicemente la coordinata x del punto P' modulo n.
5. Infine, il verificatore confermerà che I' è uguale a t. Se questo è il caso, la firma viene considerata valida. Se non lo è, la firma è invalida.
Questo procedimento garantisce che solo il mittente che possiede la corrispondente chiave privata potrebbe aver prodotto una firma che supera questo processo di verifica.

![image](assets/image/section2/12.webp)

In termini più semplici:
La persona che produce la firma fornirà il numero t (nel nostro esempio, t = 7) e il punto V alla persona che la verifica.
È impossibile determinare la chiave pubblica o privata dal numero 7 e dal numero V.

I passaggi per verificare la firma digitale sono i seguenti:

- Sulla curva, il verificatore aggiunge il punto della chiave pubblica al punto V per recuperare il punto T'.
- Il verificatore calcola il numero t.G.
- Il verificatore verifica che il risultato di t.G sia effettivamente uguale al numero T'.

In conclusione, verificare una firma digitale è una procedura essenziale nelle transazioni Bitcoin. Garantisce che il messaggio firmato non sia stato alterato durante la trasmissione e che il mittente sia effettivamente il detentore della chiave privata. Questa tecnica di autenticazione digitale si basa su principi matematici complessi, inclusa l'aritmetica delle curve ellittiche, mantenendo nel contempo la riservatezza della chiave privata. Fornisce una solida base di sicurezza per le transazioni crittografiche.

Detto ciò, la gestione di queste chiavi, così come la loro creazione, è un'altra questione essenziale in Bitcoin. Come generare una nuova coppia di chiavi? Come organizzare in modo sicuro ed efficiente una moltitudine di chiavi? Come recuperarle se necessario?

Per rispondere a queste domande e approfondire la comprensione della sicurezza crittografica, il nostro prossimo corso si concentrerà sul concetto di portafogli deterministici gerarchici (HD wallets) e sull'uso di frasi mnemoniche. Questi meccanismi offrono modi eleganti per gestire in modo efficace le chiavi associate alle criptovalute, migliorando la sicurezza.

# La frase mnemonica
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Evoluzione dei portafogli Bitcoin
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Il portafoglio deterministico gerarchico, comunemente noto come HD wallet, svolge un ruolo di primo piano nell'ecosistema delle criptovalute. Il termine "portafoglio" può sembrare fuorviante per coloro che sono nuovi in questo campo, poiché non implica il possesso di denaro o valute. Invece, si riferisce ad una collezione di chiavi private crittografiche.

I primi portafogli erano software che raggruppavano chiavi determinate privatamente in modo pseudo-casuale ma non avevano alcuna connessione tra di loro. Questi portafogli sono chiamati "Just a Bunch Of Keys" (JBOK).

Poiché le chiavi non hanno alcuna connessione tra di loro, all'utente viene richiesto di effettuare un nuovo backup per ogni nuova coppia di chiavi generata. L'utente può utilizzare sempre la stessa coppia di chiavi compromettendo la riservatezza, o generare casualmente una nuova coppia di chiavi con l'onere di avere un backup per ciascuna di queste chiavi. 

Tuttavia, la complessità della gestione di queste chiavi è compensata da un insieme di protocolli chiamati Bitcoin Improvement Proposals (BIP). Queste proposte di aggiornamento sono al centro della funzionalità e della sicurezza degli HD wallet. Ad esempio, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lanciato nel 2012, ha rivoluzionato il modo in cui queste chiavi vengono generate e archiviate introducendo il concetto di chiavi derivate in modo deterministico e gerarchico. L'idea è derivare tutte le chiavi in modo deterministico e gerarchico da un'unica informazione: il seed. Questo semplifica notevolmente il processo di backup di queste chiavi mantenendo al contempo il loro livello di sicurezza.

Successivamente, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) ha introdotto una significativa innovazione: la frase mnemonica di 24 parole. Questo sistema ha trasformato una sequenza complessa e difficile da ricordare di numeri in una serie di parole comuni, rendendola molto più facile da memorizzare e conservare. Inoltre, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) ha proposto l'aggiunta di una passphrase aggiuntiva per migliorare la sicurezza delle chiavi individuali. Questi miglioramenti successivi hanno portato agli standard BIP43 e BIP44, che hanno standardizzato la struttura e la gerarchizzazione dei portafogli HD, rendendoli più accessibili ed user-friendly per il pubblico generale.

Nelle sezioni seguenti, approfondiremo il funzionamento dei portafogli HD. Discuteremo i principi di derivazione delle chiavi e esamineremo i concetti fondamentali di entropia e generazione di numeri casuali, che sono essenziali per garantire la sicurezza del tuo portafoglio HD.

In sintesi, è essenziale sottolineare il ruolo centrale di BIP32 e BIP39 nella progettazione e sicurezza dei portafogli HD. Questi protocolli consentono la generazione di molteplici chiavi da un singolo seed, che dovrebbe essere un numero casuale o pseudo-casuale. Oggi, questi standard sono adottati dalla maggior parte dei portafogli di criptovalute, che siano dedicati a una singola criptovaluta o supportino diversi tipi di valute.

## Entropia e Numero Casuale
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

L'importanza della sicurezza delle chiavi private nell'ecosistema Bitcoin è innegabile. Sono infatti il fondamento che garantisce la sicurezza delle transazioni Bitcoin. Per evitare qualsiasi vulnerabilità associata alla prevedibilità, queste chiavi devono essere generate in modo veramente casuale, il che può rapidamente diventare un esercizio laborioso. Il problema è che nell'informatica è impossibile generare un numero veramente casuale poiché deriva necessariamente da un processo deterministico; un codice. Ecco perché è essenziale conoscere i diversi Generatori di Numeri Casuali (RNG). I tipi di RNG variano, spaziando dai Generatori di Numeri Pseudo-Casuali (PRNG) ai Generatori di Numeri Veramente Casuali (TRNG), nonché PRNG che incorporano una fonte di entropia.

L'entropia si riferisce allo stato di "disordine" di un sistema. Da un'entropia esterna, cioè una fonte esterna di informazioni, è possibile utilizzare un generatore di numeri casuali per ottenere un numero casuale.

![immagine](assets/image/section3/2.webp)

Diamo un'occhiata a come funziona un Generatore di Numeri Pseudo-Casuali (PRNG).

Prende in input un seed, che corrisponde allo stato interno 0.
Su questo stato interno viene applicata una funzione di trasformazione e il risultato, che è un numero pseudo-casuale, corrisponde allo stato interno 1.
Su questo stato interno 1, ancora una volta, viene applicata una funzione di trasformazione, ottenendo un nuovo numero casuale = stato interno 2.
E così via.

Il principale svantaggio è che qualsiasi seed identico produrrà sempre lo stesso output. Inoltre, se conosciamo il risultato delle funzioni di trasformazione iniziali, saremo in grado di recuperare il numero casuale in uscita dal processo.

Un esempio di funzione di trasformazione è la funzione PBKDF2.

**In sintesi, un PRNG crittograficamente sicuro deve:**

- essere statisticamente casuale
- essere imprevedibile
- essere resistente anche se i risultati sono rivelati
- avere un periodo sufficientemente lungo

![immagine](assets/image/section3/3.webp)

Nel caso di Bitcoin, le chiavi private vengono generate da un'unica informazione alla base del portafoglio. Questa informazione consente la derivazione deterministica e gerarchica di coppie di chiavi figlie. L'entropia è alla base di ogni portafoglio HD, anche se non esiste uno standard per generare questo numero casuale. Pertanto, la generazione di numeri casuali rappresenta una sfida importante per la sicurezza delle transazioni Bitcoin.

## La frase mnemonica
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

La sicurezza di un portafoglio Bitcoin è una preoccupazione principale per tutti i suoi utenti. Un modo essenziale per garantire il backup del portafoglio è generare una frase mnemonica basata sull'entropia e sul checksum.

![immagine](assets/image/section3/5.webp)

Per convertire l'entropia in una frase mnemonica, basta calcolare il checksum dell'entropia e concatenare l'entropia e il checksum.

Una volta generata l'entropia, la funzione SHA256 viene utilizzata sull'entropia per creare un hash.
Vengono recuperati i primi 8 bit dell'hash, che costituiscono il checksum.
La frase mnemonica è il risultato dell'entropia aggiunta al checksum.

Il checksum garantisce la verifica dell'accuratezza della frase di recupero. Senza questo checksum, un errore nella frase potrebbe comportare la creazione di un portafoglio diverso e quindi la perdita di fondi. Il checksum viene ottenuto passando l'entropia attraverso la funzione SHA256 e recuperando i primi 8 bit dell'hash.

![immagine](assets/image/section3/6.webp)

Esistono diversi standard per la frase mnemonica a seconda delle dimensioni dell'entropia. Lo standard più comunemente utilizzato per una frase di recupero di 24 parole è un'entropia di 256 bit. La dimensione del checksum è determinata dividendo la dimensione dell'entropia per 32.

Ad esempio, un'entropia di 256 bit genera un checksum di 8 bit. La concatenazione dell'entropia e del checksum porta quindi a dimensioni rispettive di 128 bit, 160 bit, ecc. A seconda delle dimensioni dell'entropia, la frase di recupero sarà composta da 12 parole per 128 bit, 15 parole per 160 bit e 24 parole per 256 bit.

**Codifica della frase mnemonica:**

![immagine](assets/image/section3/7.webp)

Gli ultimi 8 bit corrispondono al checksum.
Ogni segmento di 11 bit viene convertito in decimale.
Ogni decimale corrisponde a una parola di una lista di 2048 parole su BIP39. È importante notare che nessuna parola ha lo stesso ordine delle prime quattro lettere.

È essenziale fare il backup della frase di recupero di 24 parole per preservare l'integrità del portafoglio Bitcoin. Gli standard più comunemente utilizzati si basano su un'entropia di 128 o 256 bit e una concatenazione di 12 o 24 parole. L'aggiunta di una passphrase è un'opzione aggiuntiva per migliorare la sicurezza del portafoglio.

In conclusione, generare una frase mnemonica per proteggere un portafoglio Bitcoin è un processo cruciale. È importante attenersi agli standard della frase mnemonica in base alle dimensioni dell'entropia. Eseguire il backup della frase di recupero di 24 parole è essenziale per evitare la perdita di fondi.

## La passphrase
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

La passphrase è una password aggiuntiva che può essere integrata in un portafoglio Bitcoin per aumentarne la sicurezza. Il suo utilizzo è facoltativo ed è a discrezione dell'utente. Aggiungendo informazioni arbitrarie che, insieme alla frase mnemonica, consentono il calcolo del seed del portafoglio, la passphrase ne migliora la sicurezza.

![immagine](assets/image/section3/8.webp)

La passphrase è un sale crittografico opzionale di dimensioni scelte dall'utente. Migliora la sicurezza di un portafoglio HD aggiungendo informazioni arbitrarie che, combinati con la frase mnemonica, consentiranno il calcolo del seed.
Una volta stabilita durante la creazione di un portafoglio, è necessaria per la derivazione di tutte le chiavi del portafoglio. La funzione pbkdf2 viene utilizzata per generare il seed dalla passphrase. Questo seed consente la derivazione di tutte le coppie di chiavi figlie del portafoglio. Se la passphrase viene modificata, il portafoglio Bitcoin diventa completamente diverso.

La passphrase è uno strumento essenziale per migliorare la sicurezza dei portafogli Bitcoin. Può consentire l'implementazione di varie strategie di sicurezza. Ad esempio, può essere utilizzata per creare duplicati e facilitare il backup della frase mnemonica. Può anche migliorare la sicurezza del portafoglio mitigando i rischi associati alla generazione casuale della frase mnemonica.

Una passphrase efficace dovrebbe essere lunga (da 20 a 40 caratteri) e diversificata (utilizzando lettere maiuscole, lettere minuscole, numeri e simboli). Non dovrebbe essere direttamente correlata all'utente o al suo ambiente. È più sicuro utilizzare una sequenza casuale di caratteri piuttosto che una semplice parola come passphrase.

![image](assets/image/section3/9.webp)

Una passphrase è più sicura di una semplice password. La passphrase ideale è lunga, varia e casuale. Può migliorare la sicurezza di un portafoglio o di un portafoglio hot. Può anche essere utilizzata per creare backup ridondanti e sicuri.

È fondamentale prendersi cura dei backup della passphrase per evitare di perdere l'accesso al portafoglio. Una passphrase è un'opzione per un portafoglio HD. Può essere generata casualmente con dadi o un altro generatore di numeri pseudo-casuali. Non è consigliabile memorizzare una passphrase o una frase mnemonica.

Nella nostra prossima lezione, esamineremo in dettaglio il funzionamento del seed e la prima coppia di chiavi generata da esso. Sentiti libero di seguire questo corso per continuare il tuo apprendimento. Non vediamo l'ora di rivederti molto presto.

# Creazione dei portafogli Bitcoin
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Creazione del Seed e della Chiave Master
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

In questa parte del corso, esploreremo i passaggi per la derivazione di un portafoglio deterministico gerarchico (HD Wallet), che consente la creazione e la gestione gerarchica e deterministica di chiavi private e pubbliche.

![image](assets/image/section4/0.webp)

La base dell'HD Wallet si basa su due elementi essenziali: la frase mnemonica e la passphrase (password aggiuntiva opzionale). Insieme, costituiscono il seed, una sequenza alfanumerica di 512 bit che serve come base per la derivazione delle chiavi del portafoglio. Da questo seed, è possibile derivare tutte le coppie di chiavi figlie del portafoglio Bitcoin. Il seed è la chiave che garantisce l'accesso a tutti i bitcoin associati al portafoglio, che tu utilizzi una passphrase o meno.

![image](assets/image/section4/1.webp)

Per ottenere il seed, viene utilizzata la funzione pbkdf2 (Password-Based Key Derivation Function 2) con la frase mnemonica e la passphrase. L'output di pbkdf2 è un seed di 512 bit.

Dal seed, è possibile determinare la chiave privata master e il codice di catena utilizzando l'algoritmo HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Questo algoritmo richiede un messaggio e una chiave come input per generare un risultato. La chiave privata master viene calcolata dal seed e dalla frase "Bitcoin SEED". Questa frase è identica per tutte le derivazioni di tutti i portafogli HD, garantendo coerenza tra i portafogli.

Inizialmente, la funzione SHA-512 non era implementata nel protocollo Bitcoin, motivo per cui viene utilizzato HMAC SHA-512. L'uso di HMAC SHA-512 con la frase "Bitcoin SEED" vincola l'utente a generare un portafoglio specifico per Bitcoin. Il risultato di HMAC SHA-512 è un numero di 512 bit, diviso in due parti: i 256 bit più a sinistra rappresentano la chiave privata principale, mentre i 256 bit più a destra rappresentano il codice di catena principale.

![image](assets/image/section4/2.webp)

La chiave privata principale è la chiave genitore di tutte le chiavi future nel portafoglio, mentre il codice di catena principale è coinvolto nella derivazione delle chiavi figlie. È importante notare che è impossibile derivare una coppia di chiavi figlie senza conoscere il codice di catena corrispondente della coppia genitore.

Una coppia di chiavi nel portafoglio è composta da una chiave privata, una chiave pubblica e un codice di catena. Il codice di catena introduce una fonte di casualità nella derivazione delle chiavi figlie e isola ogni coppia di chiavi per prevenire eventuali perdite di informazioni.
È importante notare che la chiave privata principale è la prima chiave privata derivata dal seed e non ha alcuna connessione con le chiavi estese del portafoglio.

Nella prossima lezione, esploreremo in dettaglio le chiavi estese, come xPub, xPRV, zPub, e capiremo perché vengono utilizzate e come vengono costruite.

## Chiavi estese
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

In questa parte della lezione, studieremo le chiavi estese (xPub, zPub, yPub) e i loro prefissi, che svolgono un ruolo importante nella derivazione delle chiavi figlie in un portafoglio deterministico gerarchico (HD Wallet).

![image](assets/image/section4/3.webp)

Le chiavi estese sono diverse dalle chiavi principali. Un portafoglio HD genera una frase mnemonica e un seed per ottenere la chiave principale e il codice di catena principale. Le chiavi estese vengono utilizzate per derivare le chiavi figlie e richiedono sia la chiave genitore che il codice di catena corrispondente. Una chiave estesa combina queste due informazioni per semplificare il processo di derivazione.

![image](assets/image/section4/4.webp)

Le chiavi pubbliche estese possono derivare solo chiavi pubbliche normali, mentre le chiavi private estese possono derivare sia chiavi pubbliche che private figlie, sia attraverso una derivazione normale che indurita. La derivazione indurita è la derivazione dalla chiave privata genitore, mentre la derivazione normale corrisponde alla derivazione dalla chiave pubblica genitore.

L'utilizzo di chiavi estese con il prefisso XPUB consente la derivazione di nuovi indirizzi senza dover tornare alle chiavi private corrispondenti, garantendo così una maggiore sicurezza. I metadati associati alle chiavi estese forniscono informazioni importanti sul loro ruolo e posizione nella gerarchia delle chiavi.

Le chiavi estese sono identificate da prefissi specifici (XPRV, XPUB, YPUB, ZPUB) che indicano se si tratta di una chiave privata o pubblica estesa, nonché il suo scopo specifico. I metadati associati a una chiave estesa includono la versione (prefisso), la profondità, l'impronta digitale della chiave genitore, l'indice e il payload (codice di catena e chiave genitore).

![image](assets/image/section4/5.webp)

La versione corrisponde al tipo di chiave: xpub, xprv, ...

La profondità corrisponde al numero di derivazioni tra le chiavi genitore e figlie dalla chiave principale.

L'impronta digitale del genitore è i primi 4 byte dell'hash 160 della chiave genitore.
L'indice è il numero della coppia che viene utilizzata per generare la chiave estesa tra i suoi fratelli. (fratelli = chiavi della stessa profondità) Ad esempio, se vogliamo derivare l'xpub del nostro terzo account, il suo indice sarà 2 (perché l'indice parte da 0).
Il payload è composto dal codice della catena (32 byte) e dalla chiave genitore (33 byte).
Le chiavi pubbliche compressate hanno una dimensione di 33 byte, mentre le chiavi pubbliche non elaborate sono di 512 bit. Le chiavi pubbliche compressate mantengono le stesse informazioni delle chiavi non elaborate, ma con una dimensione ridotta. Le chiavi estese hanno una dimensione di 82 byte e il loro prefisso è rappresentato in base 58 attraverso una conversione in esadecimale. Il checksum viene calcolato utilizzando la funzione di hash HASH256.

![Immagine](assets/image/section4/6.webp)

Le derivazioni migliorate partono da indici che sono potenze di 2 (2^31). È interessante notare che i prefissi più comunemente utilizzati sono xpub e zpub, che corrispondono rispettivamente agli standard legacy e segwit v1 e segwit v0.

Nella nostra prossima lezione, ci concentreremo sulla derivazione delle coppie di chiavi figlie utilizzando le conoscenze acquisite sulle chiavi estese e la chiave principale del portafoglio.

## Derivazione delle coppie di chiavi figlie
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Come promemoria, abbiamo discusso del calcolo del seed e della chiave principale, che sono i primi elementi essenziali per l'organizzazione gerarchica e la derivazione del portafoglio HD (Hierarchical Deterministic). Il seed, con una lunghezza di 128 a 256 bit, viene generato casualmente o da una frase segreta. Gioca un ruolo deterministico nella derivazione di tutte le altre chiavi. La chiave principale è la prima chiave derivata dal seed e consente la derivazione di tutte le altre coppie di chiavi figlie.

Il codice della catena principale svolge un ruolo importante nel recupero del portafoglio dal seed. Va notato che tutte le chiavi derivate dallo stesso seed avranno lo stesso codice della catena principale.

![Immagine](assets/image/section4/7.webp)

L'organizzazione gerarchica e la derivazione del portafoglio HD offrono una gestione più efficiente delle chiavi e delle strutture del portafoglio. Le chiavi estese consentono la derivazione di una coppia di chiavi figlie da una coppia di chiavi genitore utilizzando calcoli matematici e algoritmi specifici.
Ci sono diversi tipi di coppie di chiavi figlie, tra cui chiavi rinforzate e chiavi normali. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, che siano in modalità normale o rinforzata. Ogni coppia di chiavi ha un indice che consente di differenziarle l'una dall'altra.

![Immagine](assets/image/section4/8.webp)

La derivazione delle chiavi figlie utilizza la funzione HMAC-SHA512 utilizzando la chiave genitore concatenata con l'indice e il codice della catena associato alla coppia di chiavi. Le chiavi figlie normali hanno un indice che va da 0 a 2 alla potenza di 31 meno 1, mentre le chiavi figlie rinforzate hanno un indice che va da 2 alla potenza di 31 a 2 alla potenza di 32 meno 1.

![Immagine](assets/image/section4/9.webp)

![Immagine](assets/image/section4/10.webp)

Ci sono due tipi di coppie di chiavi figlie: coppie rinforzate e coppie normali. Il processo di derivazione delle chiavi figlie utilizza le chiavi pubbliche per generare condizioni di spesa, mentre le chiavi private vengono utilizzate per la firma. La chiave pubblica estesa consente solo la derivazione di chiavi pubbliche figlie normali, mentre la chiave privata estesa consente la derivazione di tutte le chiavi figlie, sia pubbliche che private, in modalità normale o rinforzata.

![Immagine](assets/image/section4/11.webp)
![Immagine](assets/image/section4/12.webp)

La derivazione rinforzata utilizza la chiave privata genitore, mentre la derivazione normale utilizza la chiave pubblica genitore. La funzione HMAC-SHA512 viene utilizzata per la derivazione rinforzata, mentre la derivazione normale utilizza un digest a 512 bit. La chiave pubblica figlio viene ottenuta moltiplicando la chiave privata figlio per il generatore della curva ellittica.

![immagine](assets/image/section4/13.webp)
![immagine](assets/image/section4/14.webp)

La derivazione gerarchica e la derivazione di molte coppie di chiavi in modo deterministico consentono la creazione di una struttura ad albero per la derivazione gerarchica. Nella prossima lezione di questo corso, studieremo la struttura del portafoglio HD e i percorsi di derivazione, con particolare attenzione alle notazioni dei percorsi di derivazione.

## Struttura del portafoglio e percorsi di derivazione
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

In questo capitolo, studieremo la struttura dell'albero di derivazione in un portafoglio deterministico gerarchico (HD Wallet). Abbiamo già esplorato il calcolo del seed, la chiave principale e la derivazione delle coppie di chiavi figlio. Ora, ci concentreremo sull'organizzazione delle chiavi all'interno del portafoglio.

L'HD Wallet utilizza livelli di profondità per organizzare le chiavi. Ogni derivazione da una coppia genitore a una coppia figlio corrisponde a un livello di profondità.

![immagine](assets/image/section4/15.webp)

- La profondità 0 corrisponde alla chiave principale e al codice catena principale.

- La profondità 1 viene utilizzata per derivare chiavi figlio per uno scopo specifico, determinato dall'indice. Gli scopi sono conformi agli standard BIP 84 e Segwit v0/v1.

- La profondità 2 consente la differenziazione dei conti per diverse criptovalute o reti. Ciò consente di organizzare il portafoglio in base a diverse fonti. Per Bitcoin, l'indice sarà 0.

- La profondità 3 viene utilizzata per organizzare il portafoglio in diversi account, fornendo una struttura più chiara e organizzata.

- La profondità 4 corrisponde alle catene esterne e interne, che vengono utilizzate per gli indirizzi destinati a essere comunicati pubblicamente. L'indice 0 è associato alla catena esterna, mentre l'indice 1 è associato alla catena interna. Ogni account ha due catene: la catena esterna (0) e la catena interna (1). La profondità 4 viene utilizzata anche per gestire tipi di script nel caso di portafogli multi-firma.

- La profondità 5 viene utilizzata per gli indirizzi di ricezione in un portafoglio standard. Nella prossima sezione, esamineremo in dettaglio la derivazione delle coppie di chiavi figlio.

![immagine](assets/image/section4/16.webp)

Per ogni livello di profondità, utilizziamo gli indici per differenziare le coppie di chiavi figlio.

L'indice senza apostrofo corrisponde all'indice effettivamente utilizzato, mentre l'indice con apostrofo corrisponde all'indice effettivo + 2^31. Le derivazioni rinforzate utilizzano indici da 2^31 a 2^32-1. Ad esempio, l'indice 44' corrisponde all'indice effettivo 2^31 + 44.

Per generare un indirizzo di ricezione specifico, deriviamo una coppia di chiavi figlio dalla chiave principale e dal codice catena principale. Quindi, utilizziamo l'indice per differenziare tra diverse coppie di chiavi figlio alla stessa profondità.
Le chiavi estese, come XPUB, ti consentono di condividere il tuo portafoglio con più persone. Il percorso di derivazione viene utilizzato per differenziare tra la catena esterna (indirizzi destinati a essere condivisi) e la catena interna (indirizzi di cambio).

Nel prossimo capitolo, studieremo gli indirizzi di ricezione, i loro vantaggi di utilizzo e i passaggi coinvolti nella loro costruzione.

# Cos'è un indirizzo Bitcoin?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Indirizzi Bitcoin
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

In questo capitolo, esploreremo gli indirizzi di ricezione, che svolgono un ruolo cruciale nel sistema Bitcoin. Consentono di ricevere fondi in una transazione e vengono generati da coppie di chiavi private e pubbliche. Sebbene esista un tipo di script chiamato Pay2PublicKey che consente di bloccare i bitcoin su una chiave pubblica, gli utenti preferiscono generalmente utilizzare gli indirizzi di ricezione invece di questo script.

![image](assets/image/section5/0.webp)

Quando un destinatario desidera ricevere bitcoin, fornisce un indirizzo di ricezione al mittente anziché la sua chiave pubblica. Un indirizzo è in realtà un hash di una chiave pubblica, con un formato specifico. La chiave pubblica è derivata dalla chiave privata figlia utilizzando operazioni matematiche come l'addizione e il raddoppio dei punti sulle curve ellittiche.

![image](assets/image/section5/1.webp)

È importante notare che non è possibile risalire da un indirizzo alla chiave pubblica, né dalla chiave pubblica alla chiave privata. Utilizzare un indirizzo riduce le dimensioni delle informazioni sulla chiave pubblica, che inizialmente è di 512 bit.

Gli indirizzi Bitcoin sono stati ridotti in dimensioni per agevolarne l'uso. Hanno un checksum, che consente di rilevare errori di battitura e ridurre il rischio di perdita di bitcoin. D'altra parte, le chiavi pubbliche non hanno un checksum, il che significa che gli errori di battitura possono comportare la perdita dei fondi corrispondenti.

Gli indirizzi forniscono anche un secondo livello di sicurezza tra informazioni pubbliche e private, rendendo più difficile prendere il controllo della chiave privata.

È essenziale sottolineare che ogni indirizzo dovrebbe essere utilizzato solo una volta. Riutilizzare lo stesso indirizzo comporta problemi di privacy e dovrebbe essere evitato.

Vengono utilizzati diversi prefissi per gli indirizzi Bitcoin. Ad esempio, BC1Q corrisponde a un indirizzo Segwit V0, BC1P a un indirizzo Taproot/Segwit V1 e i prefissi 1 e 3 sono associati agli indirizzi Pay2PublicKeyH/Pay2ScriptH (legacy). Nella prossima lezione, spiegheremo passo dopo passo come derivare un indirizzo da una chiave pubblica.

## Come creare un indirizzo Bitcoin?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

In questo capitolo, discuteremo della costruzione di un indirizzo di ricezione per le transazioni Bitcoin. Un indirizzo di ricezione è una rappresentazione alfanumerica di una chiave pubblica compressa. La conversione di una chiave pubblica in un indirizzo di ricezione comporta diversi passaggi.

### Passaggio 1: Compressione della chiave pubblica

![image](assets/image/section5/14.webp)

Un indirizzo deriva da una chiave pubblica figlia.

Una chiave pubblica è un punto sulla curva ellittica. Grazie alla simmetria della curva ellittica, un punto sulla curva ellittica avrà una coordinata x associata solo a due possibili valori per y: positivo o negativo. 
Tuttavia, nel protocollo Bitcoin, lavoriamo con un insieme finito di numeri interi positivi anziché con l'insieme dei numeri reali. Per distinguere tra i due possibili valori di y, è sufficiente indicare se y è pari o dispari.

La compressione di una chiave pubblica riduce le sue dimensioni da 520 bit a 264 bit.

Utilizziamo il prefisso 0x02 per un y pari e 0x03 per un y dispari. Questa è la forma compressa della chiave pubblica.

### Passaggio 2: Hashing della chiave pubblica compressa

![image](assets/image/section5/3.webp)

L'hashing della chiave pubblica compressa viene eseguito utilizzando la funzione SHA256. Viene quindi applicata la funzione RIPEMD160 al digest.

### Passaggio 3: Il payload = Payload dell'indirizzo

![image](assets/image/section5/4.webp)

Il digest binario di RIPEMD160(SHA256(K)) viene utilizzato per formare gruppi di 5 bit. Ogni gruppo viene poi trasformato in base16 (esadecimale) e/o base 10.

### Passaggio 4: Aggiunta di metadati per il calcolo del checksum con il programma BCH

![immagine](assets/image/section5/5.webp)

Nel caso degli indirizzi legacy, utilizziamo l'hashing doppio SHA256 per generare il checksum dell'indirizzo. Tuttavia, per gli indirizzi Segwit V0 e V1, ci affidiamo alla tecnologia di checksum BCH per garantire la rilevazione degli errori. Il programma BCH è in grado di suggerire e correggere errori con una probabilità di errore estremamente bassa. Attualmente, il programma BCH viene utilizzato per rilevare e suggerire modifiche da apportare, ma non le esegue automaticamente per conto dell'utente.
Il programma BCH richiede diverse informazioni come input, tra cui l'HRP (Parte Leggibile dall'Uomo) che deve essere estesa. L'estensione dell'HRP comporta la codifica di ogni lettera in base 2 secondo il loro codice ASCII. Quindi, prendendo i primi 3 bit del risultato per ogni lettera e convertendoli in base 10 (in blu nell'immagine). Inserire un separatore 0. Quindi concatenare i successivi 5 bit di ogni lettera precedentemente convertiti in base 10 (in giallo nell'immagine).

L'estensione dell'HRP in base 10 consente di isolare gli ultimi cinque bit di ogni carattere, rafforzando così il checksum.

La versione Segwit V0 è rappresentata dal codice 00 e il "payload" è in nero, in base 10. Seguono sei caratteri riservati per il checksum.

### Passaggio 5: Calcolo del checksum con il programma BCH

![immagine](assets/image/section5/6.webp)

L'input contenente i metadati viene quindi inviato al programma BCH per ottenere il checksum in base 10.

Qui abbiamo il checksum.

### Passaggio 6: Costruzione dell'indirizzo e conversione in Bech32

![immagine](assets/image/section5/7.webp)

La concatenazione della versione, del payload e del checksum consente di costruire l'indirizzo. I caratteri in base 10 vengono quindi convertiti in caratteri Bech32 utilizzando una tabella di corrispondenza. L'alfabeto Bech32 include tutti i caratteri alfanumerici, ad eccezione di 1, b, i e o, per evitare confusione.

### Passaggio 7: Aggiunta dell'HRP e del separatore

![immagine](assets/image/section5/8.webp)

In rosa, il checksum.
In nero, il payload = l'hash della chiave pubblica.
In blu, la versione.

Tutto viene convertito in Bech32, quindi viene aggiunto 'bc' per bitcoin e '1' come separatore, ed ecco l'indirizzo.

# Approfondimenti
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Creazione di un seed da 128 lanci di dadi!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Creare una frase mnemonica è un passaggio cruciale per proteggere il portafoglio di ciascuna criptovaluta. Ci sono diversi metodi per generare una frase mnemonica, tuttavia, ci concentreremo sul metodo di generazione manuale utilizzando i dadi. È importante notare che questo metodo non è adatto per un portafoglio di alto valore. Si consiglia di utilizzare software open-source o un portafoglio hardware per generare la frase mnemonica. Per creare una frase mnemonica, utilizzeremo i dadi per generare informazioni binarie. L'obiettivo è comprendere il processo di creazione della frase mnemonica.

**Passaggio 1 - Preparazione:**
Assicurati di avere una distribuzione Linux amnesica, come Tails OS, installata su una chiavetta USB per una maggiore sicurezza. Si noti che questo tutorial non deve essere utilizzato per creare un portafoglio principale.
**Passaggio 2 - Generazione di un numero binario casuale:**
Useremo dei dadi per generare informazioni binarie. Lancia un dado 128 volte e registra ogni risultato (1 per dispari, 0 per pari).
**Passaggio 3 - Organizzazione dei numeri binari:**
Organizza i numeri binari ottenuti in righe di 11 cifre per facilitare ulteriori calcoli. La dodicesima riga dovrebbe avere solo 7 cifre.

**Passaggio 4 - Calcolo del checksum:**
Le ultime 4 cifre della dodicesima riga corrispondono al checksum. Per calcolare questo checksum, è necessario utilizzare il terminale da una distribuzione Linux. Si consiglia di utilizzare [TailOs](https://tails.boum.org/index.fr.html), che è una distribuzione senza memoria avviabile da una chiave USB. Una volta sul tuo terminale, inserisci il comando `echo <numero binario> | shasum -a 254 -0`. Sostituisci `<numero binario>` con la tua lista di 128 zeri e uno. L'output è un hash esadecimale. Prendi nota del primo carattere di questo hash e convertilo in binario. Puoi utilizzare questa [tabella](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) per assistenza. Aggiungi il checksum binario (4 cifre) alla dodicesima riga del tuo foglio.

**Passaggio 5 - Conversione in decimale:**
Per trovare le parole associate a ciascuna delle tue righe, devi prima convertire ogni serie di 11 bit in decimale. Qui, non puoi utilizzare un convertitore online perché questi bit rappresentano la tua frase mnemonica. Pertanto, dovrai convertire utilizzando una calcolatrice e un trucco come segue: ogni bit è associato a una potenza di 2, quindi da sinistra a destra, abbiamo 11 posizioni corrispondenti a 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Per convertire la tua serie di 11 bit in decimale, basta sommare solo le posizioni che contengono un 1. Ad esempio, per la serie 00110111011, ciò corrisponde alla seguente somma: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Ora puoi convertire ogni riga in decimale. E prima di passare alla codifica in parole, aggiungi +1 a tutte le righe perché l'indice della lista di parole BIP39 parte da 1, non da 0.

**Passaggio 8 - Generazione della frase mnemonica:**
Inizia stampando l'[elenco di 2048 parole](https://seedxor.com/files/wordlist.pdf) per convertire tra i tuoi numeri decimali e le parole BIP39. La particolarità di questa lista è che nessuna parola condivide le prime 4 lettere con un'altra parola in questo dizionario. Quindi, cerca la parola associata a ciascun numero decimale delle tue righe.
**Passaggio 9 - Test della frase mnemonica:**
Testa immediatamente la tua frase mnemonica su Sparrow Wallet creando un portafoglio da essa. Se ricevi un errore di checksum non valido, è probabile che tu abbia commesso un errore di calcolo. Correggi questo errore tornando al passaggio 4 e riprova su Sparrow Wallet. Voilà! Hai appena creato un nuovo portafoglio Bitcoin da 128 lanci di dadi.

Generare una frase mnemonica è un processo importante per proteggere il tuo portafoglio di criptovalute. Si consiglia di utilizzare metodi più sicuri, come l'uso di software open source o un portafoglio hardware, per generare la frase mnemonica. Tuttavia, completando questo workshop hai compreso meglio come è possibile creare un portafoglio Bitcoin da un numero casuale.

## BONUS: Intervista con Théo Pantamis
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Un altro metodo crittografico ampiamente utilizzato nel protocollo Bitcoin è il metodo delle firme digitali.


![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Valuta il corso
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Esame Finale
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Conclusioni e fine
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Grazie e continua a scavare nella tana del coniglio

Desideriamo ringraziarti sinceramente per aver completato il corso Crypto 301. Speriamo che questa esperienza sia stata arricchente ed educativa per te. Abbiamo affrontato molti argomenti interessanti, che vanno dalla matematica alla crittografia al funzionamento del protocollo Bitcoin.

Se desideri approfondire ulteriormente l'argomento, abbiamo una risorsa aggiuntiva da offrirti. Abbiamo condotto un'intervista esclusiva con Théo Pantamis e Loïc Morel, due rinomati esperti nel campo della crittografia. Questa intervista esplora vari aspetti dell'argomento in profondità e fornisce interessanti prospettive.

Sentiti libero di guardare questa intervista per continuare a esplorare il fascinante campo della crittografia. Speriamo che sia utile e fonte di ispirazione nel tuo percorso. Ancora una volta, grazie per la tua partecipazione e impegno durante tutto il corso.

### Sostienici

Questo corso, insieme a tutti i contenuti di questa università, ti è stato fornito gratuitamente dalla nostra comunità. Per sostenerci, puoi condividerlo con gli altri, diventare membro dell'università e persino contribuire al suo sviluppo tramite GitHub. A nome di tutto il team, grazie!

### Valuta il corso
Un sistema di valutazione per la formazione sarà presto integrato in questa nuova piattaforma di e-learning! Nel frattempo, ti ringraziamo molto per aver seguito il corso e, se ti è piaciuto, ti preghiamo di considerare la possibilità di condividerlo con gli altri.
