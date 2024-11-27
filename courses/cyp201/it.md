---
name: Il Funzionamento Interno dei Portafogli Bitcoin
goal: Esplorare i principi crittografici che alimentano i portafogli Bitcoin.
objectives:
  - Definire le nozioni teoriche necessarie per comprendere gli algoritmi crittografici utilizzati in Bitcoin.
  - Comprendere a fondo la costruzione di un portafoglio deterministico e gerarchico.
  - Sapere come identificare e ridurre i rischi associati alla gestione di un portafoglio.
  - Capire i principi delle funzioni hash, delle chiavi crittografiche e delle firme digitali.
---

# Un Viaggio nel Cuore dei Portafogli Bitcoin

Scopri i segreti dei portafogli Bitcoin deterministici e gerarchici con il nostro corso CYP201! Che tu sia un utente regolare o un appassionato che cerca di approfondire la tua conoscenza, questo corso offre un'immersione completa nel funzionamento di questi strumenti che tutti noi usiamo quotidianamente.

Impara i meccanismi delle funzioni hash, delle firme digitali (ECDSA e Schnorr), delle frasi mnemoniche, delle chiavi crittografiche e della creazione di indirizzi di ricezione, esplorando al contempo strategie di sicurezza avanzate.

Questo training non solo ti doterà della conoscenza per comprendere la struttura di un portafoglio Bitcoin, ma ti preparerà anche ad immergerti nel mondo affascinante della crittografia.

Con una chiara pedagogia, oltre 60 diagrammi esplicativi e esempi concreti, CYP201 ti permetterà di capire da A a Z come funziona il tuo portafoglio, così da poter navigare l'universo Bitcoin con fiducia. Prendi il controllo dei tuoi UTXO oggi, comprendendo come funzionano i portafogli HD!

+++

# Introduzione

<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Introduzione al Corso

<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

Benvenuti al corso CYP201, dove esploreremo a fondo il funzionamento dei portafogli Bitcoin HD. Questo corso è progettato per chiunque voglia comprendere le basi tecniche dell'uso di Bitcoin, sia che si tratti di utenti occasionali, appassionati illuminati o futuri esperti.

L'obiettivo di questa formazione è fornirvi le chiavi per padroneggiare gli strumenti che utilizzate quotidianamente. I portafogli Bitcoin HD, che sono al centro della vostra esperienza utente, si basano su concetti a volte complessi, che cercheremo di rendere accessibili. Insieme, li demistificheremo!

Prima di immergerci nei dettagli della costruzione e del funzionamento dei portafogli Bitcoin, inizieremo con alcuni capitoli sulle primitive crittografiche da conoscere per quanto segue. Inizieremo con le funzioni hash crittografiche, fondamentali sia per i portafogli sia per il protocollo Bitcoin stesso. Scoprirete le loro principali caratteristiche, le funzioni specifiche utilizzate in Bitcoin e, in un capitolo più tecnico, imparerete in dettaglio il funzionamento della regina delle funzioni hash: SHA256.
![CYP201](assets/fr/010.webp)

Successivamente, discuteremo il funzionamento degli algoritmi di firma digitale che utilizzate ogni giorno per proteggere i vostri UTXO. Bitcoin ne utilizza due: ECDSA e il protocollo Schnorr. Imparerete quali primitive matematiche sottostanno a questi algoritmi e come assicurano la sicurezza delle transazioni.

![CYP201](assets/fr/021.webp)

Una volta acquisita una buona comprensione di questi elementi di crittografia, passeremo finalmente al cuore della formazione: i portafogli deterministici e gerarchici! Prima, c'è una sezione dedicata alle frasi mnemoniche, queste sequenze di 12 o 24 parole che vi permettono di creare e ripristinare i vostri portafogli. Scoprirete come queste parole vengono generate da una fonte di entropia e come facilitano l'uso di Bitcoin.

![CYP201](assets/fr/040.webp)
La formazione continuerà con lo studio della passphrase BIP39, il seed (da non confondere con la frase mnemonica), il master chain code e la master key. Vedremo in dettaglio cosa sono questi elementi, i loro rispettivi ruoli e come vengono calcolati.
![CYP201](assets/fr/045.webp)

Infine, partendo dalla master key, scopriremo come le coppie di chiavi crittografiche vengono derivate in modo deterministico e gerarchico fino agli indirizzi di ricezione.

![CYP201](assets/fr/056.webp)

Questa formazione ti permetterà di utilizzare il tuo software di wallet con fiducia, migliorando al contempo le tue capacità di identificare e mitigare i rischi. Preparati a diventare un vero esperto di portafogli Bitcoin!

# Funzioni Hash

<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Introduzione alle Funzioni Hash

<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Il primo tipo di algoritmi crittografici utilizzati su Bitcoin comprende le funzioni hash. Svolgono un ruolo essenziale a diversi livelli del protocollo, ma anche all'interno dei portafogli Bitcoin. Scopriamo insieme cosa è una funzione hash e a cosa serve in Bitcoin.

### Definizione e Principio dell'Hashing

L'hashing è un processo che trasforma informazioni di lunghezza arbitraria in un'altra informazione di lunghezza fissa attraverso una funzione hash crittografica. In altre parole, una funzione hash prende un input di qualsiasi dimensione e lo converte in un'impronta digitale di dimensione fissa, chiamata "hash".
L'hash può anche essere talvolta definito come "digest", "condensato", o "hashed".

Ad esempio, la funzione hash SHA256 produce un hash di lunghezza fissa di 256 bit. Così, se usiamo l'input "_Plan ₿_", un messaggio di lunghezza arbitraria, l'hash generato sarà la seguente impronta digitale di 256 bit:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

![CYP201](assets/fr/001.webp)

### Caratteristiche delle Funzioni Hash

Queste funzioni hash crittografiche hanno diverse caratteristiche essenziali che le rendono particolarmente utili nel contesto di Bitcoin e altri sistemi informatici:

1. Irreversibilità (o resistenza alla preimmagine)
2. Resistenza alla manomissione (effetto valanga)
3. Resistenza alle collisioni
4. Resistenza alla seconda preimmagine

#### 1. Irreversibilità (resistenza alla preimmagine):

L'irreversibilità significa che è facile calcolare l'hash dalle informazioni di input, ma il calcolo inverso, cioè trovare l'input dall'hash, è praticamente impossibile. Questa proprietà rende le funzioni hash perfette per creare impronte digitali uniche senza compromettere le informazioni originali. Questa caratteristica è spesso definita come una funzione unidirezionale o una "_funzione trappola_".

Nell'esempio dato, ottenere l'hash `24f1b9…` conoscendo l'input "_Plan ₿_" è semplice e veloce. Tuttavia, trovare il messaggio "_Plan ₿_" conoscendo solo `24f1b9…` è impossibile.

![CYP201](assets/fr/002.webp)

Pertanto, è impossibile trovare una preimmagine $m$ per un hash $h$ tale che $h = \text{HASH}(m)$, dove $\text{HASH}$ è una funzione hash crittografica.

#### 2. Resistenza alla manomissione (effetto valanga)

La seconda caratteristica è la resistenza alla manomissione, nota anche come **effetto valanga**. Questa caratteristica si osserva in una funzione hash se un piccolo cambiamento nel messaggio di input comporta un radicale cambiamento nell'hash di output.

Se torniamo al nostro esempio con l'input "_Plan ₿_" e la funzione SHA256, abbiamo visto che l'hash generato è il seguente:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

Se facciamo un cambiamento molto lieve all'input usando questa volta "_Planb_", il semplice passaggio da una "B" maiuscola a una "b" minuscola altera completamente l'hash di output SHA256:

```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```

![CYP201](assets/fr/003.webp)

Questa proprietà garantisce che anche una minima alterazione del messaggio originale sia immediatamente rilevabile, poiché non cambia solo una piccola parte dell'hash, ma l'intero hash. Questo può essere di interesse in vari campi per verificare l'integrità di messaggi, software o anche transazioni Bitcoin.

#### 3. Resistenza alle Collisioni

La terza caratteristica è la resistenza alle collisioni. Una funzione hash è resistente alle collisioni se è computazionalmente impossibile trovare 2 messaggi diversi che producono lo stesso hash di output dalla funzione. Formalmente, è difficile trovare due messaggi distinti $m_1$ e $m_2$ tali che:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

![CYP201](assets/fr/004.webp)

In realtà, è matematicamente inevitabile che esistano collisioni per le funzioni hash, perché la dimensione degli input può essere maggiore della dimensione degli output. Questo è noto come il principio dei cassetti di Dirichlet: se $n$ oggetti sono distribuiti in $m$ cassetti, con $m < n$, allora almeno un cassetto conterrà necessariamente due o più oggetti. Per una funzione hash, questo principio si applica perché il numero di messaggi possibili è (quasi) infinito, mentre il numero di hash possibili è finito ($2^{256}$ nel caso di SHA256).

Quindi, questa caratteristica non significa che non ci siano collisioni per le funzioni hash, ma piuttosto che una buona funzione hash rende la probabilità di trovare una collisione trascurabile. Questa caratteristica, ad esempio, non è più verificata sugli algoritmi SHA-0 e SHA-1, predecessori di SHA-2, per i quali sono state trovate collisioni. Queste funzioni sono quindi ora sconsigliate e spesso considerate obsolete.
Per una funzione hash di $n$ bit, la resistenza alle collisioni è dell'ordine di $2^{\frac{n}{2}}$, in conformità con l'attacco del compleanno. Ad esempio, per SHA256 ($n = 256$), la complessità di trovare una collisione è dell'ordine di $2^{128}$ tentativi. In termini pratici, ciò significa che se si passano $2^{128}$ messaggi diversi attraverso la funzione, è probabile trovare una collisione.

#### 4. Resistenza alla Seconda Preimmagine

La resistenza alla seconda preimmagine è un'altra caratteristica importante delle funzioni hash. Afferma che, dato un messaggio $m_1$ e il suo hash $h$, è computazionalmente impraticabile trovare un altro messaggio $m_2 \neq m_1$ tale che:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

Pertanto, la resistenza alla seconda preimmagine è in qualche modo simile alla resistenza alle collisioni, eccetto che qui, l'attacco è più difficile perché l'attaccante non può scegliere liberamente $m_1$.

### Applicazioni delle Funzioni Hash in Bitcoin

La funzione hash più utilizzata in Bitcoin è **SHA256** ("_Secure Hash Algorithm 256 bits"_). Progettata all'inizio degli anni 2000 dalla NSA e standardizzata dal NIST, produce un output hash di 256 bit.

Questa funzione è utilizzata in molti aspetti di Bitcoin. A livello di protocollo, è coinvolta nel meccanismo di Proof-of-Work, dove viene applicata in un doppio hashing per cercare una collisione parziale tra l'intestazione di un blocco candidato, creato da un miner, e il target di difficoltà. Se questa collisione parziale viene trovata, il blocco candidato diventa valido e può essere aggiunto alla blockchain.

SHA256 è anche utilizzato nella costruzione di un albero di Merkle, che è notevolmente l'accumulatore usato per registrare le transazioni nei blocchi. Questa struttura si trova anche nel protocollo Utreexo, che permette di ridurre la dimensione del Set UTXO. Inoltre, con l'introduzione di Taproot nel 2021, SHA256 è sfruttato in MAST (_Merkelised Alternative Script Tree_), che permette di rivelare solo le condizioni di spesa effettivamente utilizzate in uno script, senza divulgare le altre opzioni possibili. È anche utilizzato nel calcolo degli identificatori di transazione, nella trasmissione di pacchetti sulla rete P2P, nelle firme elettroniche... Infine, e questo è di particolare interesse in questa formazione, SHA256 è utilizzato a livello applicativo per la costruzione di portafogli Bitcoin e la derivazione di indirizzi.

La maggior parte delle volte, quando si incontra l'uso di SHA256 su Bitcoin, si tratterà in realtà di un doppio hash SHA256, notato "**HASH256**", che consiste semplicemente nell'applicare SHA256 due volte consecutivamente:
HASH256(m) = SHA256(SHA256(m))

Questa pratica del doppio hashing aggiunge un ulteriore strato di sicurezza contro certi potenziali attacchi, anche se oggi un singolo SHA256 è considerato criptograficamente sicuro.

Un'altra funzione di hashing disponibile nel linguaggio Script e utilizzata per derivare indirizzi di ricezione è la funzione RIPEMD160. Questa funzione produce un hash di 160 bit (quindi più corto di SHA256). È generalmente combinata con SHA256 per formare la funzione HASH160:

$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$

Questa combinazione è utilizzata per generare hash più corti, in particolare nella creazione di certi indirizzi Bitcoin che rappresentano hash di chiavi o hash di script, così come per produrre impronte digitali delle chiavi.

Infine, solo a livello applicativo, talvolta viene utilizzata anche la funzione SHA512, che gioca indirettamente un ruolo nella derivazione delle chiavi per i portafogli. Questa funzione è molto simile a SHA256 nel suo funzionamento; entrambe appartengono alla stessa famiglia SHA2, ma SHA512 produce, come indica il nome, un hash di 512 bit, rispetto ai 256 bit di SHA256. Ne dettaglieremo l'uso nei capitoli seguenti.

Ora conoscete le basi essenziali sulle funzioni di hashing per ciò che segue. Nel prossimo capitolo, propongo di scoprire più in dettaglio il funzionamento della funzione che è al cuore di Bitcoin: SHA256. Lo dissezioneremo per capire come raggiunge le caratteristiche che abbiamo descritto qui. Il prossimo capitolo è piuttosto lungo e tecnico, ma non è essenziale per seguire il resto della formazione. Quindi, se avete difficoltà a comprenderlo, non preoccupatevi e passate direttamente al capitolo seguente, che sarà molto più accessibile.

## Il Funzionamento Interno di SHA256

<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>
Abbiamo precedentemente visto che le funzioni di hashing possiedono importanti caratteristiche che giustificano il loro uso su Bitcoin. Ora esaminiamo i meccanismi interni di queste funzioni di hashing che conferiscono loro queste proprietà, e per fare ciò, propongo di dissezionare il funzionamento di SHA256.
Le funzioni SHA256 e SHA512 appartengono alla stessa famiglia SHA2. Il loro meccanismo si basa su una costruzione specifica chiamata **Merkle-Damgård construction**. Anche RIPEMD160 utilizza questo stesso tipo di costruzione.

Come promemoria, abbiamo un messaggio di dimensione arbitraria come input per SHA256, e lo passeremo attraverso la funzione per ottenere un hash di 256 bit come output.

### Pre-elaborazione dell'input

Per iniziare, dobbiamo preparare il nostro messaggio di input $m$ in modo che abbia una lunghezza standard che sia un multiplo di 512 bit. Questo passaggio è cruciale per il corretto funzionamento dell'algoritmo successivamente.
Per fare ciò, iniziamo con il passaggio dei bit di padding. Aggiungiamo prima un bit separatore `1` al messaggio, seguito da un certo numero di bit `0`. Il numero di bit `0` aggiunti è calcolato in modo che la lunghezza totale del messaggio dopo questa aggiunta sia congruente a 448 modulo 512. Così, la lunghezza $L$ del messaggio con i bit di padding è uguale a:

$$
L \equiv 448 \mod 512
$$

$\text{mod}$, per modulo, è un'operazione matematica che, tra due interi, restituisce il resto della divisione euclidea del primo per il secondo. Per esempio: $16 \mod 5 = 1$. È un'operazione ampiamente utilizzata in crittografia.

Qui, il passaggio di padding assicura che, dopo aver aggiunto i 64 bit nel passaggio successivo, la lunghezza totale del messaggio equalizzato sarà un multiplo di 512 bit. Se il messaggio iniziale ha una lunghezza di $M$ bit, il numero ($N$) di bit `0` da aggiungere è quindi:

$$
N = (448 - (M + 1) \mod 512) \mod 512
$$

Per esempio, se il messaggio iniziale è di 950 bit, il calcolo sarebbe il seguente:

$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$

Così, avremmo 9 `0` in aggiunta al separatore `1`. I nostri bit di padding da aggiungere direttamente dopo il nostro messaggio $M$ sarebbero quindi:

```text
1000 0000 00
```

Dopo aver aggiunto i bit di padding al nostro messaggio $M$, aggiungiamo anche una rappresentazione di 64 bit della lunghezza originale del messaggio $M$, espressa in binario. Questo consente alla funzione hash di essere sensibile all'ordine dei bit e alla lunghezza del messaggio.
Se torniamo al nostro esempio con un messaggio iniziale di 950 bit, convertiamo il numero decimale `950` in binario, ottenendo `1110 1101 10`. Completiamo questo numero con zeri alla base per raggiungere un totale di 64 bit. Nel nostro esempio, otteniamo:

```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```

Questa dimensione di riempimento viene aggiunta seguendo il riempimento bit. Pertanto, il messaggio dopo la nostra pre-elaborazione consiste di tre parti:

1. Il messaggio originale $M$;
2. Un bit `1` seguito da diversi bit `0` per formare il riempimento bit;
3. Una rappresentazione di 64 bit della lunghezza di $M$ per formare il riempimento con la dimensione.

![CYP201](assets/fr/006.webp)

### Inizializzazione delle Variabili

SHA256 utilizza otto variabili di stato iniziali, indicate da $A$ a $H$, ognuna di 32 bit. Queste variabili sono inizializzate con costanti specifiche, che sono le parti frazionarie delle radici quadrate dei primi otto numeri primi. Utilizzeremo questi valori successivamente durante il processo di hashing:

- $A = 0x6a09e667$
- $B = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$

SHA256 utilizza anche altre 64 costanti, indicate da $K_0$ a $K_{63}$, che sono le parti frazionarie delle radici cubiche dei primi 64 numeri primi:

$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
\end{pmatrix}
$$

0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}

$$

### Divisione dell'Input

Ora che abbiamo un input equalizzato, passeremo alla fase principale di elaborazione dell'algoritmo SHA256: la funzione di compressione. Questo passaggio è molto importante, poiché è principalmente ciò che conferisce alla funzione hash le sue proprietà crittografiche che abbiamo studiato nel capitolo precedente.

Iniziamo dividendo il nostro messaggio equalizzato (risultato dei passaggi di pre-elaborazione) in diversi blocchi $P$ da 512 bit ciascuno. Se il nostro messaggio equalizzato ha una dimensione totale di $n \times 512$ bit, avremo quindi $n$ blocchi, ciascuno di 512 bit. Ogni blocco da 512 bit sarà elaborato individualmente dalla funzione di compressione, che consiste in 64 round di operazioni successive. Chiamiamo questi blocchi $P_1$, $P_2$, $P_3$...

### Operazioni Logiche

Prima di esplorare in dettaglio la funzione di compressione, è importante comprendere le operazioni logiche di base utilizzate. Queste operazioni, basate sull'algebra booleana, operano a livello di bit. Le operazioni logiche di base utilizzate sono:
- **Coniunzione (AND)**: denotata $\land$, corrisponde a un "E" logico.
- **Disgiunzione (OR)**: denotata $\lor$, corrisponde a un "O" logico.
- **Negazione (NOT)**: denotata $\lnot$, corrisponde a un "NON" logico.

Da queste operazioni di base, possiamo definire operazioni più complesse, come l'"OR esclusivo" (XOR) denotato $\oplus$, ampiamente utilizzato in crittografia.
Ogni operazione logica può essere rappresentata da una tabella di verità, che indica il risultato per tutte le possibili combinazioni di valori di input binari (due operandi $p$ e $q$).
Per XOR ($\oplus$):

| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

Per AND ($\land$):

| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           || 1   | 0   | 0           |
| 1   | 1   | 1           |

Per NOT ($\lnot p$):

| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

Prendiamo un esempio per capire il funzionamento di XOR a livello di bit. Se abbiamo due numeri binari su 6 bit:

- $a = 101100$
- $b = 001000$

Allora:


$$

a \oplus b = 101100 \oplus 001000 = 100100

$$

Applicando XOR bit per bit:

| Posizione Bit | $a$ | $b$ | $a \oplus b$ |
| ------------ | --- | --- | ------------ |
| 1            | 1   | 0   | 1            |
| 2            | 0   | 0   | 0            |
| 3            | 1   | 1   | 0            |
| 4            | 1   | 0   | 1            |
| 5            | 0   | 0   | 0            |
| 6            | 0   | 0   | 0            |

Il risultato è quindi $100100$.

Oltre alle operazioni logiche, la funzione di compressione utilizza operazioni di bit-shifting, che giocheranno un ruolo essenziale nella diffusione dei bit nell'algoritmo.

Prima di tutto, c'è l'operazione di shift logico a destra, denotata $ShR_n(x)$, che sposta tutti i bit di $x$ a destra di $n$ posizioni, riempiendo i bit vacanti a sinistra con zeri.

Per esempio, per $x = 101100001$ (su 9 bit) e $n = 4$:


$$

ShR_4(101100001) = 000010110

$$

Schematicamente, l'operazione di shift a destra potrebbe essere vista così:

![CYP201](assets/fr/007.webp)
Un'altra operazione utilizzata in SHA256 per la manipolazione dei bit è la rotazione circolare a destra, denotata $RotR_n(x)$, che sposta i bit di $x$ a destra di $n$ posizioni, reinserendo i bit spostati all'inizio della stringa.
Per esempio, per $x = 101100001$ (su 9 bit) e $n = 4$:


$$

RotR_4(101100001) = 000110110

$$

Schematicamente, l'operazione di rotazione circolare a destra potrebbe essere vista così:

![CYP201](assets/fr/008.webp)

### Funzione di Compressione

Ora che abbiamo compreso le operazioni di base, esaminiamo in dettaglio la funzione di compressione SHA256.

Nel passaggio precedente, abbiamo diviso il nostro input in diversi pezzi da 512 bit $P$. Per ogni blocco da 512 bit $P$, abbiamo:
- **Le parole del messaggio $W_i$**: per $i$ da 0 a 63.
- **Le costanti $K_i$**: per $i$ da 0 a 63, definite nel passaggio precedente.
- **Le variabili di stato $A, B, C, D, E, F, G, H$**: inizializzate con i valori dal passaggio precedente.
Le prime 16 parole, $W_0$ fino a $W_{15}$, sono estratte direttamente dal blocco elaborato di 512 bit $P$. Ogni parola $W_i$ consiste di 32 bit consecutivi del blocco. Quindi, ad esempio, prendiamo il nostro primo pezzo di input $P_1$, e lo dividiamo ulteriormente in pezzi più piccoli da 32 bit che chiamiamo parole.
Le successive 48 parole ($W_{16}$ fino a $W_{63}$) sono generate utilizzando la seguente formula:


$$

W*i = W*{i-16} + \sigma*0(W*{i-15}) + W*{i-7} + \sigma_1(W*{i-2}) \mod 2^{32}

$$

Con:
- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x)$

In questo caso, $x$ è uguale a $W_{i-15}$ per $\sigma_0(x)$ e $W_{i-2}$ per $\sigma_1(x)$.

Una volta determinate tutte le parole $W_i$ per il nostro pezzo di 512 bit, possiamo passare alla funzione di compressione, che consiste nell'eseguire 64 round.

Per ogni round $i$ da 0 a 63, abbiamo tre diversi tipi di input. Primo, il $W_i$ che abbiamo appena determinato, in parte costituito dal nostro pezzo di messaggio $P_n$. Successivamente, le 64 costanti $K_i$. Infine, usiamo le variabili di stato $A$, $B$, $C$, $D$, $E$, $F$, $G$ e $H$, che evolveranno durante il processo di hashing e saranno modificate con ogni funzione di compressione. Tuttavia, per il primo pezzo $P_1$, usiamo le costanti iniziali date in precedenza.
Eseguiamo quindi le seguenti operazioni sui nostri input:

- **Funzione $\Sigma_0$:**


$$

\Sigma*0(A) = RotR_2(A) \oplus RotR*{13}(A) \oplus RotR\_{22}(A)

$$

- **Funzione $\Sigma_1$:**


$$

\Sigma*1(E) = RotR_6(E) \oplus RotR*{11}(E) \oplus RotR\_{25}(E)

$$

- **Funzione $Ch$ ("*Scegli*"):**


$$

Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)

$$

- **Funzione $Maj$ ("*Maggioranza*"):**


$$

Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)

$$

Calcoliamo quindi 2 variabili temporanee:

- $temp1$:


$$

temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}

$$

- $temp2$:


$$

temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}

$$

Successivamente, aggiorniamo le variabili di stato come segue:


$$

\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 mod 2^{32} \\D = C \\
C = B \\
B = A \\
A = temp1 + temp2 mod 2^{32}
\end{cases}

$$

Il seguente diagramma rappresenta un round della funzione di compressione SHA256 come appena descritto:

![CYP201](assets/fr/010.webp)

- Le frecce indicano il flusso dei dati;
- I riquadri rappresentano le operazioni eseguite;
- Il simbolo $+$ circondato rappresenta l'addizione modulo $2^{32}$.

Possiamo già osservare che questo round produce nuove variabili di stato $A$, $B$, $C$, $D$, $E$, $F$, $G$ e $H$. Queste nuove variabili serviranno come input per il round successivo, che a sua volta produrrà nuove variabili $A$, $B$, $C$, $D$, $E$, $F$, $G$ e $H$, da utilizzare per il round seguente. Questo processo continua fino al 64° round.
Dopo i 64 round, aggiorniamo i valori iniziali delle variabili di stato aggiungendoli ai valori finali alla fine del round 64:
$$

\begin{cases}
A = A*{\text{iniziale}} + A mod 2^{32} \\
B = B*{\text{iniziale}} + B mod 2^{32} \\
C = C*{\text{iniziale}} + C mod 2^{32} \\
D = D*{\text{iniziale}} + D mod 2^{32} \\
E = E*{\text{iniziale}} + E mod 2^{32} \\
F = F*{\text{iniziale}} + F mod 2^{32} \\
G = G*{\text{iniziale}} + G mod 2^{32} \\
H = H*{\text{iniziale}} + H mod 2^{32}
\end{cases}

$$

Questi nuovi valori di $A$, $B$, $C$, $D$, $E$, $F$, $G$ e $H$ serviranno come valori iniziali per il blocco successivo, $P_2$. Per questo blocco $P_2$, replichiamo lo stesso processo di compressione con 64 round, poi aggiorniamo le variabili per il blocco $P_3$, e così via fino all'ultimo blocco del nostro input equalizzato.

Dopo aver processato tutti i blocchi del messaggio, concateniamo i valori finali delle variabili $A$, $B$, $C$, $D$, $E$, $F$, $G$ e $H$ per formare l'hash finale a 256 bit della nostra funzione di hashing:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H

$$

Ogni variabile è un intero a 32 bit, quindi la loro concatenazione produce sempre un risultato a 256 bit, indipendentemente dalla dimensione del nostro input al funzione di hashing.

### Giustificazione delle Proprietà Crittografiche

Ma allora, come è possibile che questa funzione sia irreversibile, resistente alle collisioni e resistente alle manomissioni?

Per la resistenza alle manomissioni, è abbastanza semplice da capire. Vengono eseguiti così tanti calcoli in cascata, che dipendono sia dall'input che dalle costanti, che la minima modifica del messaggio iniziale cambia completamente il percorso preso, e quindi cambia completamente l'hash di output. Questo è ciò che viene chiamato effetto valanga. Questa proprietà è in parte garantita dalla miscelazione degli stati intermedi con gli stati iniziali per ogni pezzo.
Successivamente, quando si discute di una funzione hash crittografica, il termine "irreversibilità" non è generalmente utilizzato. Invece, si parla di "resistenza alla pre-immagine", che specifica che per un dato $y$, è difficile trovare un $x$ tale che $h(x) = y$. Questa resistenza alla pre-immagine è garantita dalla complessità algebrica e dalla forte non-linearità delle operazioni eseguite nella funzione di compressione, così come dalla perdita di certe informazioni nel processo. Ad esempio, per un dato risultato di un'addizione modulo, ci sono diversi operandi possibili:$$
3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5
$$

In questo esempio, conoscendo solo il modulo utilizzato (10) e il risultato (5), non si può determinare con certezza quali siano gli operandi corretti utilizzati nell'addizione. Si dice che ci sono molteplici congruenze modulo 10.

Per l'operazione XOR, ci troviamo di fronte allo stesso problema. Ricordiamo la tabella di verità per questa operazione: qualsiasi output a 1 bit può essere determinato da due diverse configurazioni di input che hanno esattamente la stessa probabilità di essere i valori corretti. Pertanto, non si può determinare con certezza gli operandi di un XOR conoscendo solo il suo risultato. Se aumentiamo la dimensione degli operandi XOR, il numero di input possibili conoscendo solo il risultato aumenta esponenzialmente. Inoltre, XOR è spesso utilizzato insieme ad altre operazioni a livello di bit, come l'operazione $\text{RotR}$, che aggiungono ancora più possibili interpretazioni al risultato.

La funzione di compressione utilizza anche l'operazione $\text{ShR}$. Questa operazione rimuove una parte delle informazioni di base, che poi diventa impossibile recuperare in seguito. Ancora una volta, non esiste un mezzo algebrico per invertire questa operazione. Tutte queste operazioni unidirezionali e di perdita di informazioni sono utilizzate molto frequentemente nelle funzioni di compressione. Il numero di input possibili per un dato output è quindi quasi infinito, e ogni tentativo di calcolo inverso porterebbe a equazioni con un numero molto elevato di incognite, che aumenterebbe esponenzialmente ad ogni passo.

Infine, per la caratteristica della resistenza alle collisioni, entrano in gioco diversi parametri. La pre-elaborazione del messaggio originale gioca un ruolo essenziale. Senza questa pre-elaborazione, potrebbe essere più facile trovare collisioni sulla funzione. Anche se, teoricamente, le collisioni esistono (a causa del principio del buco della serratura), la struttura della funzione hash, combinata con le proprietà sopra menzionate, rende la probabilità di trovare una collisione estremamente bassa.
Affinché una funzione hash sia resistente alle collisioni, è essenziale che:

- L'output sia imprevedibile: Qualsiasi prevedibilità può essere sfruttata per trovare collisioni più velocemente di un attacco a forza bruta. La funzione assicura che ogni bit dell'output dipenda in modo non banale dall'input. In altre parole, la funzione è progettata in modo che ogni bit del risultato finale abbia una probabilità indipendente di essere 0 o 1, anche se questa indipendenza non è assoluta nella pratica.
- La distribuzione degli hash sia pseudo-casuale: Questo garantisce che gli hash siano uniformemente distribuiti.
- La dimensione dell'hash sia sostanziale: più grande è lo spazio possibile per i risultati, più difficile è trovare una collisione.

I crittografi progettano queste funzioni valutando i migliori attacchi possibili per trovare collisioni, poi aggiustando i parametri per rendere questi attacchi inefficaci.

### Costruzione di Merkle-Damgård

La struttura di SHA256 si basa sulla costruzione di Merkle-Damgård, che consente di trasformare una funzione di compressione in una funzione hash che può elaborare messaggi di lunghezza arbitraria. Questo è precisamente ciò che abbiamo visto in questo capitolo.
Tuttavia, alcune vecchie funzioni hash come SHA1 o MD5, che utilizzano questa specifica costruzione, sono vulnerabili agli attacchi di estensione della lunghezza. Questa è una tecnica che permette a un attaccante che conosce l'hash di un messaggio $M$ e la lunghezza di $M$ (senza conoscere il messaggio stesso) di calcolare l'hash di un messaggio $M'$ formato concatenando $M$ con contenuti aggiuntivi.
SHA256, anche se utilizza lo stesso tipo di costruzione, è teoricamente resistente a questo tipo di attacco, a differenza di SHA1 e MD5. Questo potrebbe spiegare il mistero del doppio hashing implementato in tutto il Bitcoin da Satoshi Nakamoto. Per evitare questo tipo di attacco, Satoshi potrebbe aver preferito utilizzare un doppio SHA256:

$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$

Questo migliora la sicurezza contro potenziali attacchi legati alla costruzione di Merkle-Damgård, ma non aumenta la sicurezza del processo di hashing in termini di resistenza alle collisioni. Inoltre, anche se SHA256 fosse stato vulnerabile a questo tipo di attacco, non avrebbe avuto un impatto grave, poiché tutti i casi d'uso delle funzioni hash in Bitcoin coinvolgono dati pubblici. Tuttavia, l'attacco di estensione della lunghezza potrebbe essere utile solo per un attaccante se i dati hashati sono privati e l'utente ha utilizzato la funzione hash come meccanismo di autenticazione per questi dati, simile a un MAC. Pertanto, l'implementazione del doppio hashing rimane un mistero nella progettazione di Bitcoin.
Ora che abbiamo esaminato in dettaglio il funzionamento delle funzioni hash, in particolare SHA256, che è ampiamente utilizzato in Bitcoin, ci concentreremo più specificamente sugli algoritmi di derivazione crittografica utilizzati a livello applicativo, specialmente per derivare le chiavi per il tuo portafoglio.

## Gli algoritmi utilizzati per la derivazione

<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

In Bitcoin a livello applicativo, oltre alle funzioni hash, vengono utilizzati algoritmi di derivazione crittografica per generare dati sicuri da input iniziali. Sebbene questi algoritmi si basino sulle funzioni hash, servono a scopi diversi, specialmente in termini di autenticazione e generazione di chiavi. Questi algoritmi mantengono alcune delle caratteristiche delle funzioni hash, come l'irreversibilità, la resistenza alla manomissione e la resistenza alle collisioni.

Sui portafogli Bitcoin, principalmente vengono utilizzati 2 algoritmi di derivazione:

1. **HMAC (_Hash-based Message Authentication Code_)**
2. **PBKDF2 (_Password-Based Key Derivation Function 2_)**

Esploreremo insieme il funzionamento e il ruolo di ciascuno di essi.

### HMAC-SHA512

HMAC è un algoritmo crittografico che calcola un codice di autenticazione basato su una combinazione di una funzione hash e una chiave segreta. Bitcoin utilizza HMAC-SHA512, la variante di HMAC che utilizza la funzione hash SHA512. Abbiamo già visto nel capitolo precedente che SHA512 fa parte della stessa famiglia di funzioni hash di SHA256, ma produce un output di 512 bit.

Ecco il suo schema operativo generale con $m$ che rappresenta il messaggio di input e $K$ una chiave segreta:

![CYP201](assets/fr/011.webp)

Studiamo in dettaglio cosa succede in questa black box HMAC-SHA512. La funzione HMAC-SHA512 con:

- $m$: il messaggio di dimensione arbitraria scelto dall'utente (primo input);
- $K$: la chiave segreta arbitraria scelta dall'utente (secondo input);
- $K'$: la chiave $K$ adeguata alla dimensione $B$ dei blocchi della funzione hash (1024 bit per SHA512, o 128 byte);
- $\text{SHA512}$: la funzione hash SHA512;
- $\oplus$: l'operazione XOR (o esclusivo);
- $\Vert$: l'operatore di concatenazione, che collega stringhe di bit da un'estremità all'altra;
- $\text{opad}$: costante composta dal byte $0x5c$ ripetuto 128 volte
- $\text{ipad}$: costante composta dal byte $0x36$ ripetuto 128 volte
  Prima di calcolare l'HMAC, è necessario eguagliare la chiave e le costanti secondo la dimensione del blocco $B$. Ad esempio, se la chiave $K$ è più corta di 128 byte, viene riempita con zeri fino a raggiungere la dimensione $B$. Se $K$ è più lunga di 128 byte, viene compressa usando SHA512, e poi vengono aggiunti zeri fino a raggiungere 128 byte. In questo modo, si ottiene una chiave eguagliata denominata $K'$.
  I valori di $\text{opad}$ e $\text{ipad}$ si ottengono ripetendo il loro byte base ($0x5c$ per $\text{opad}$, $0x36$ per $\text{ipad}$) fino a raggiungere la dimensione $B$. Quindi, con $B = 128$ byte, abbiamo:

$$
\text{opad} = \underbrace{0x5c5c\ldots5c}_{128 \, \text{byte}}
$$

Una volta fatto il preprocessing, l'algoritmo HMAC-SHA512 è definito dalla seguente equazione:

$$
\text {HMAC-SHA512}_K(m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)
$$

Questa equazione si scompone nei seguenti passaggi:

1. XOR della chiave aggiustata $K'$ con $\text{ipad}$ per ottenere $\text{iKpad}$;
2. XOR della chiave aggiustata $K'$ con $\text{opad}$ per ottenere $\text{oKpad}$;
3. Concatenazione di $\text{iKpad}$ con il messaggio $m$.
4. Hash di questo risultato con SHA512 per ottenere un hash intermedio $H_1$.
5. Concatenazione di $\text{oKpad}$ con $H_1$.
6. Hash di questo risultato con SHA512 per ottenere il risultato finale $H_2$.

Questi passaggi possono essere riassunti schematicamente come segue:

![CYP201](assets/fr/012.webp)

L'HMAC è utilizzato in Bitcoin in particolare per la derivazione delle chiavi nei portafogli HD (Deterministici Gerarchici) (ne parleremo più dettagliatamente nei prossimi capitoli) e come componente di PBKDF2.

### PBKDF2

PBKDF2 (_Password-Based Key Derivation Function 2_) è un algoritmo di derivazione delle chiavi progettato per aumentare la sicurezza delle password. L'algoritmo applica una funzione pseudo-casuale (in questo caso HMAC-SHA512) su una password e un sale crittografico, e poi ripete questa operazione un certo numero di volte per produrre una chiave di output.

In Bitcoin, PBKDF2 è utilizzato per generare il seme di un portafoglio HD da una frase mnemonica e una passphrase (ma ne parleremo più dettagliatamente nei prossimi capitoli).

Il processo PBKDF2 è il seguente, con:

- $m$: la frase mnemonica dell'utente;
- $s$: la passphrase opzionale per aumentare la sicurezza (campo vuoto se non c'è passphrase);
- $n$: il numero di iterazioni della funzione, nel nostro caso, è 2048.
  La funzione PBKDF2 è definita iterativamente. Ogni iterazione prende il risultato della precedente, lo passa attraverso HMAC-SHA512 e combina i risultati successivi per produrre la chiave finale:
  $$
  \text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)
  $$

Schematicamente, PBKDF2 può essere rappresentata come segue:

![CYP201](assets/fr/013.webp)

In questo capitolo, abbiamo esplorato le funzioni HMAC-SHA512 e PBKDF2, che utilizzano funzioni di hashing per garantire l'integrità e la sicurezza delle derivazioni di chiavi nel protocollo Bitcoin. Nella prossima parte, esamineremo le firme digitali, un altro metodo crittografico ampiamente utilizzato in Bitcoin.

# Firme Digitali

<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Firme Digitali e Curve Ellittiche

<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Il secondo metodo crittografico utilizzato in Bitcoin coinvolge algoritmi di firma digitale. Esploriamo cosa comporta e come funziona.

### Bitcoin, UTXO e Condizioni di Spesa

Il termine "_portafoglio_" in Bitcoin può essere piuttosto confuso per i principianti. Infatti, ciò che viene chiamato un portafoglio Bitcoin è un software che non detiene direttamente i tuoi bitcoin, a differenza di un portafoglio fisico che può contenere monete o banconote. I Bitcoin sono semplicemente unità di conto. Questa unità di conto è rappresentata da **UTXO** (_Unspent Transaction Outputs_, ovvero output di transazione non spesi), che sono output di transazione non spesi. Se questi output non sono spesi, significa che appartengono a un utente. Gli UTXO sono, in un certo senso, pezzi di bitcoin, di dimensione variabile, appartenenti a un utente.

Il protocollo Bitcoin è distribuito e opera senza un'autorità centrale. Pertanto, non è come i registri bancari tradizionali, dove gli euro che ti appartengono sono semplicemente associati alla tua identità personale. Su Bitcoin, i tuoi UTXO ti appartengono perché sono protetti da condizioni di spesa specificate nel linguaggio Script. Per semplificare, esistono due tipi di script: lo script di blocco (_scriptPubKey_), che protegge un UTXO, e lo script di sblocco (_scriptSig_), che consente di sbloccare un UTXO e quindi spendere le unità di bitcoin che rappresenta.
L'operazione iniziale di Bitcoin con gli script P2PK coinvolge l'uso di una chiave pubblica per bloccare i fondi, specificando in uno _scriptPubKey_ che la persona che desidera spendere questo UTXO deve fornire una firma valida con la chiave privata corrispondente a questa chiave pubblica. Per sbloccare questo UTXO, è quindi necessario fornire una firma valida nello _scriptSig_. Come suggeriscono i loro nomi, la chiave pubblica è nota a tutti poiché viene trasmessa sulla blockchain, mentre la chiave privata è nota solo al legittimo proprietario dei fondi.
Questa è l'operazione di base di Bitcoin, ma nel tempo, questa operazione è diventata più complessa. In primo luogo, Satoshi ha introdotto anche gli script P2PKH, che utilizzano un indirizzo di ricezione nello _scriptPubKey_, che rappresenta l'hash della chiave pubblica. Poi, il sistema è diventato ancora più complesso con l'arrivo di SegWit e poi di Taproot. Tuttavia, il principio generale rimane fondamentalmente lo stesso: una chiave pubblica o una rappresentazione di questa chiave viene utilizzata per bloccare gli UTXO, e una chiave privata corrispondente è necessaria per sbloccarli e quindi spenderli.
Un utente che desidera effettuare una transazione Bitcoin deve quindi creare una firma digitale utilizzando la propria chiave privata sulla transazione in questione. La firma può essere verificata da altri partecipanti alla rete. Se è valida, ciò significa che l'utente che inizia la transazione è effettivamente il proprietario della chiave privata e, quindi, il proprietario dei bitcoin che desidera spendere. Altri utenti possono quindi accettare e propagare la transazione.
Di conseguenza, un utente che possiede bitcoin protetti con una chiave pubblica deve trovare un modo per conservare in modo sicuro ciò che consente di sbloccare i propri fondi: la chiave privata. Un portafoglio Bitcoin è precisamente un dispositivo che ti permetterà di conservare facilmente tutte le tue chiavi senza che altre persone abbiano accesso ad esse. È quindi più simile a un portachiavi che a un portafoglio.

Il legame matematico tra una chiave pubblica e una chiave privata, così come la capacità di eseguire una firma per provare il possesso di una chiave privata senza rivelarla, sono resi possibili da un algoritmo di firma digitale. Nel protocollo Bitcoin, vengono utilizzati 2 algoritmi di firma: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) e lo **schema di firma Schnorr**. ECDSA è il protocollo di firma digitale utilizzato in Bitcoin fin dai suoi inizi. Schnorr è più recente in Bitcoin, poiché è stato introdotto nel novembre 2021 con l'aggiornamento Taproot.
Questi due algoritmi sono abbastanza simili nei loro meccanismi. Entrambi si basano sulla crittografia a curve ellittiche. La principale differenza tra questi due protocolli risiede nella struttura della firma e in alcune proprietà matematiche specifiche. Studieremo quindi il funzionamento di questi algoritmi, partendo dal più vecchio: ECDSA.

### Crittografia a Curve Ellittiche

La Crittografia a Curve Ellittiche (ECC) è un insieme di algoritmi che utilizzano una curva ellittica per le sue varie proprietà matematiche e geometriche a scopi crittografici. La sicurezza di questi algoritmi si basa sulla difficoltà del problema del logaritmo discreto sulle curve ellittiche. Le curve ellittiche sono notevolmente utilizzate per gli scambi di chiavi, la crittografia asimmetrica o per la creazione di firme digitali.

Una proprietà importante di queste curve è che sono simmetriche rispetto all'asse x. Così, ogni linea non verticale che taglia la curva in due punti distinti intersecherà sempre la curva in un terzo punto. Inoltre, ogni tangente alla curva in un punto non singolare intersecherà la curva in un altro punto. Queste proprietà saranno utili per definire operazioni sulla curva.

Ecco una rappresentazione di una curva ellittica sul campo dei numeri reali:

![CYP201](assets/fr/014.webp)

Ogni curva ellittica è definita da un'equazione della forma:

$$
y^2 = x^3 + ax + b
$$

### secp256k1

Per utilizzare ECDSA o Schnorr, è necessario scegliere i parametri della curva ellittica, ovvero i valori di $a$ e $b$ nell'equazione della curva. Esistono diversi standard di curve ellittiche che sono reputati essere sicuri dal punto di vista crittografico. Il più noto è la curva _secp256r1_, definita e raccomandata dal NIST (_National Institute of Standards and Technology_).

Nonostante ciò, Satoshi Nakamoto, l'inventore di Bitcoin, ha scelto di non utilizzare questa curva. La ragione di questa scelta è sconosciuta, ma alcuni credono che abbia preferito trovare un'alternativa perché i parametri di questa curva potrebbero potenzialmente contenere un backdoor. Invece, il protocollo Bitcoin utilizza lo standard **_secp256k1_**. Questa curva è definita dai parametri $a = 0$ e $b = 7$. La sua equazione è quindi:

$$
y^2 = x^3 + 7
$$

La sua rappresentazione grafica sul campo dei numeri reali appare così:
Tuttavia, in crittografia, lavoriamo con insiemi finiti di numeri. Più specificamente, lavoriamo sul campo finito $\mathbb{F}_p$, che è il campo degli interi modulo un numero primo $p$.
**Definizione**: Un numero primo è un intero naturale maggiore o uguale a 2 che ha solo due distinti divisori interi positivi: 1 e se stesso. Per esempio, il numero 7 è un numero primo poiché può essere diviso solo per 1 e 7. D'altra parte, il numero 8 non è primo perché può essere diviso per 1, 2, 4 e 8.
In Bitcoin, il numero primo $p$ utilizzato per definire il campo finito è molto grande. È scelto in modo tale che l'ordine del campo (cioè, il numero di elementi in $\mathbb{F}_p$) sia sufficientemente grande da garantire la sicurezza crittografica.

Il numero primo $p$ utilizzato è:

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

In notazione decimale, questo corrisponde a:

$$
p = 2^{256} - 2^{32} - 977
$$

Quindi, l'equazione della nostra curva ellittica è in realtà:

$$
y^2 \equiv x^3 + 7 \mod p
$$

Dato che questa curva è definita sul campo finito $\mathbb{F}_p$, non assomiglia più a una curva continua ma piuttosto a un insieme discreto di punti. Per esempio, ecco come appare la curva utilizzata in Bitcoin per un $p$ molto piccolo, $p = 17$:

![CYP201](assets/fr/016.webp)

In questo esempio, ho intenzionalmente limitato il campo finito a $p = 17$ per motivi didattici, ma bisogna immaginare che quello utilizzato in Bitcoin sia immensamente più grande, quasi $2^{256}$.

Utilizziamo un campo finito di interi modulo $p$ per garantire l'accuratezza delle operazioni sulla curva. Infatti, le curve ellittiche sul campo dei numeri reali sono soggette a imprecisioni a causa degli errori di arrotondamento durante i calcoli computazionali. Se vengono eseguite numerose operazioni sulla curva, questi errori si accumulano e il risultato finale può essere incorretto o difficile da riprodurre. L'uso esclusivo di interi positivi garantisce una perfetta accuratezza dei calcoli e quindi la riproducibilità del risultato.

La matematica delle curve ellittiche sui campi finiti è analoga a quella sui campi dei numeri reali, con l'adattamento che tutte le operazioni sono eseguite modulo $p$. Per semplificare le spiegazioni, continueremo nei capitoli seguenti a illustrare i concetti utilizzando una curva definita sui numeri reali, tenendo presente che, in pratica, la curva è definita su un campo finito.

Se desideri approfondire le basi matematiche della crittografia moderna, ti consiglio anche di consultare questo altro corso su Plan ₿ Network:

https://planb.network/courses/cyp302

## Calcolare la Chiave Pubblica dalla Chiave Privata

<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>
Come visto in precedenza, gli algoritmi di firma digitale su Bitcoin si basano su una coppia di chiavi private e pubbliche che sono matematicamente collegate. Esploriamo insieme quale sia questo legame matematico e come vengono generate.

### La Chiave Privata

La chiave privata è semplicemente un numero casuale o pseudo-casuale. Nel caso di Bitcoin, questo numero è di 256 bit. Il numero di possibilità per una chiave privata Bitcoin è quindi teoricamente $2^{256}$.
**Nota**: Un "numero pseudo-casuale" è un numero che possiede proprietà vicine a quelle di un numero veramente casuale ma è generato da un algoritmo deterministico.
Tuttavia, nella pratica, ci sono solo $n$ punti distinti sulla nostra curva ellittica secp256k1, dove $n$ è l'ordine del punto generatore $G$ della curva. Vedremo più avanti a cosa corrisponde questo numero, ma ricorda semplicemente che una chiave privata valida è un intero tra $1$ e $n-1$, sapendo che $n$ è un numero vicino ma leggermente inferiore a $2^{256}$. Pertanto, ci sono alcuni numeri a 256 bit che non sono validi per diventare una chiave privata in Bitcoin, specificamente, tutti i numeri tra $n$ e $2^{256}$. Se la generazione del numero casuale (la chiave privata) produce un valore $k$ tale che $k \geq n$, è considerato non valido, e deve essere generato un nuovo valore casuale.

Il numero di possibilità per una chiave privata Bitcoin è quindi circa $n$, che è un numero vicino a $1.158 \times 10^{77}$. Questo numero è così grande che se scegli una chiave privata a caso, è statisticamente quasi impossibile capitare sulla chiave privata di un altro utente. Per darti un'idea della scala, il numero di possibili chiavi private su Bitcoin è di un ordine di grandezza vicino a quello degli atomi stimati nell'universo osservabile.

Come vedremo nei prossimi capitoli, oggi, la maggior parte delle chiavi private utilizzate su Bitcoin non sono generate casualmente ma sono il risultato della derivazione deterministica da una frase mnemonica, essa stessa pseudo-casuale (questa è la famosa frase di 12 o 24 parole). Questa informazione non cambia nulla per l'uso di algoritmi di firma come ECDSA, ma aiuta a riconcentrare la nostra divulgazione su Bitcoin.

Per il proseguimento della spiegazione, la chiave privata sarà denotata dalla lettera minuscola $k$.

### La Chiave Pubblica

La chiave pubblica è un punto sulla curva ellittica, denotato dalla lettera maiuscola $K$, e viene calcolata dalla chiave privata $k$. Questo punto $K$ è rappresentato da una coppia di coordinate $(x, y)$ sulla curva ellittica, ogni coordinata essendo un intero modulo $p$, il numero primo che definisce il campo finito $\mathbb{F}_p$.
Nella pratica, una chiave pubblica non compressa è rappresentata da 512 bit (o 64 byte), corrispondenti a due numeri a 256 bit ($x$ e $y$) posti uno di seguito all'altro. Questi numeri sono l'ascissa ($x$) e l'ordinata ($y$) del nostro punto su secp256k1. Se aggiungiamo il prefisso, la chiave pubblica totalizza 520 bit.

Tuttavia, è anche possibile rappresentare la chiave pubblica in una forma compressa utilizzando solo 33 byte (264 bit) mantenendo solo l'ascissa $x$ del nostro punto sulla curva e un byte che indica la parità di $y$. Questo è ciò che è noto come chiave pubblica compressa. Parlerò di più di questo negli ultimi capitoli di questa formazione. Ma ciò che devi ricordare è che una chiave pubblica $K$ è un punto descritto da $x$ e $y$.

Per calcolare il punto $K$ che corrisponde alla nostra chiave pubblica, utilizziamo l'operazione di moltiplicazione scalare sulle curve ellittiche, definita come un'addizione ripetuta ($k$ volte) del punto generatore $G$:

$$
K = k \cdot G
$$

dove:

- $k$ è la chiave privata (un intero casuale tra $1$ e $n-1$);
- $G$ è il punto generatore della curva ellittica utilizzato da tutti i partecipanti della rete Bitcoin;
- $\cdot$ rappresenta la moltiplicazione scalare sulla curva ellittica, che equivale ad aggiungere il punto $G$ a se stesso $k$ volte.

Il fatto che questo punto $G$ sia comune a tutte le chiavi pubbliche su Bitcoin ci permette di essere sicuri che la stessa chiave privata $k$ ci darà sempre la stessa chiave pubblica $K$:

![CYP201](assets/fr/017.webp)

La caratteristica principale di questa operazione è che si tratta di una funzione unidirezionale. È facile calcolare la chiave pubblica $K$ conoscendo la chiave privata $k$ e il punto generatore $G$, ma è praticamente impossibile calcolare la chiave privata $k$ conoscendo solo la chiave pubblica $K$ e il punto generatore $G$. Trovare $k$ a partire da $K$ e $G$ equivale a risolvere il problema del logaritmo discreto sulle curve ellittiche, un problema matematicamente difficile per il quale non è noto alcun algoritmo efficiente. Anche i calcolatori più potenti attuali non sono in grado di risolvere questo problema in un tempo ragionevole.

### Addizione e Raddoppio dei Punti sulle Curve Ellittiche

Il concetto di addizione sulle curve ellittiche è definito geometricamente. Se abbiamo due punti $P$ e $Q$ sulla curva, l'operazione $P + Q$ viene calcolata tracciando una linea che passa per $P$ e $Q$. Questa linea intersecherà necessariamente la curva in un terzo punto $R'$. Prendiamo poi l'immagine speculare di questo punto rispetto all'asse x per ottenere il punto $R$, che è il risultato dell'addizione:

$$
P + Q = R
$$

Graficamente, ciò può essere rappresentato come segue:

![CYP201](assets/fr/019.webp)

Per il raddoppio di un punto, ovvero l'operazione $P + P$, tracciamo la tangente alla curva nel punto $P$. Questa tangente interseca la curva in un altro punto $S'$. Prendiamo poi l'immagine speculare di questo punto rispetto all'asse x per ottenere il punto $S$, che è il risultato del raddoppio:

$$
2P = S
$$

Graficamente, ciò è mostrato come:

![CYP201](assets/fr/020.webp)

Utilizzando queste operazioni di addizione e raddoppio, possiamo eseguire la moltiplicazione scalare di un punto per un intero $k$, denotata $kP$, eseguendo ripetuti raddoppi e addizioni.

Per esempio, supponiamo di aver scelto una chiave privata $k = 4$. Per calcolare la chiave pubblica associata, eseguiamo:

$$
K = k \cdot G = 4G
$$

Graficamente, ciò corrisponde a eseguire una serie di addizioni e raddoppi:

- Calcolare $2G$ raddoppiando $G$.
- Calcolare $4G$ raddoppiando $2G$.

![CYP201](assets/fr/021.webp)

Se vogliamo, per esempio, calcolare il punto $3G$, dobbiamo prima calcolare il punto $2G$ raddoppiando il punto $G$, poi aggiungere $G$ e $2G$. Per aggiungere $G$ e $2G$, basta tracciare la linea che collega questi due punti, recuperare l'unico punto $-3G$ all'intersezione tra questa linea e la curva ellittica, e poi determinare $3G$ come l'opposto di $-3G$.

Avremo:

$$
G + G = 2G
$$

$$
2G + G = 3G
$$

Graficamente, ciò sarebbe rappresentato come segue:

### Funzione Unidirezionale

Grazie a queste operazioni, possiamo capire perché è facile derivare una chiave pubblica da una chiave privata, ma il contrario è praticamente impossibile.

Ritorniamo al nostro esempio semplificato. Con una chiave privata $k = 4$. Per calcolare la chiave pubblica associata, eseguiamo:
K = k \cdot G = 4G$$

Siamo quindi stati in grado di calcolare facilmente la chiave pubblica $K$ conoscendo $k$ e $G$.

Ora, se qualcuno conosce solo la chiave pubblica $K$, si trova di fronte al problema del logaritmo discreto: trovare $k$ tale che $K = k \cdot G$. Questo problema è considerato difficile perché non esiste un algoritmo efficiente per risolverlo sulle curve ellittiche. Questo garantisce la sicurezza degli algoritmi ECDSA e Schnorr.

Naturalmente, in questo esempio semplificato con $k = 4$, sarebbe possibile trovare $k$ tramite tentativi ed errori, poiché il numero di possibilità è basso. Tuttavia, nella pratica su Bitcoin, $k$ è un intero a 256 bit, rendendo il numero di possibilità astronomicamente grande (circa $1.158 \times 10^{77}$). Pertanto, è impraticabile trovare $k$ con la forza bruta.

## Firma con la Chiave Privata

<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Ora che sai come derivare una chiave pubblica da una chiave privata, puoi già ricevere bitcoin utilizzando questa coppia di chiavi come condizione di spesa. Ma come spenderli? Per spendere bitcoin, dovrai sbloccare lo _scriptPubKey_ allegato al tuo UTXO per dimostrare che sei effettivamente il legittimo proprietario. Per fare ciò, devi produrre una firma $s$ che corrisponda alla chiave pubblica $K$ presente nello _scriptPubKey_ utilizzando la chiave privata $k$ che è stata inizialmente utilizzata per calcolare $K$. La firma digitale è quindi la prova irrefutabile che sei in possesso della chiave privata associata alla chiave pubblica che affermi.

### Parametri della Curva Ellittica

Per eseguire una firma digitale, tutti i partecipanti devono prima concordare sui parametri della curva ellittica utilizzata. Nel caso di Bitcoin, i parametri di **secp256k1** sono i seguenti:

Il campo finito $\mathbb{Z}_p$ definito da:

$$
p = 2^{256} - 2^{32} - 977
$$

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

$p$ è un numero primo molto grande leggermente inferiore a $2^{256}$.

La curva ellittica $y^2 = x^3 + ax + b$ su $\mathbb{Z}_p$ definita da:

$$
a = 0, \quad b = 7
$$

Il punto generatore o punto di origine $G$:

```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```

Questo numero è la forma compressa che fornisce solo l'ascissa del punto $G$. Il prefisso `02` all'inizio determina quale dei due valori aventi questa ascissa $x$ deve essere utilizzato come punto generatore.
L'ordine $n$ di $G$ (il numero di punti esistenti) e il cofattore $h$:

```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```

$n$ è un numero molto grande leggermente inferiore a $p$.

$$
h=1
$$

$h$ è il cofattore o il numero di sottogruppi. Non approfondirò cosa rappresenta qui, poiché è abbastanza complesso, e nel caso di Bitcoin, non dobbiamo prenderlo in considerazione poiché è uguale a $1$.

Tutte queste informazioni sono pubbliche e note a tutti i partecipanti. Grazie a loro, gli utenti sono in grado di effettuare una firma digitale e verificarla.

### Firma con ECDSA

L'algoritmo ECDSA consente a un utente di firmare un messaggio utilizzando la propria chiave privata, in modo tale che chiunque conosca la corrispondente chiave pubblica possa verificare la validità della firma, senza che la chiave privata venga mai rivelata. Nel contesto di Bitcoin, il messaggio da firmare dipende dal _sighash_ scelto dall'utente. È questo _sighash_ che determinerà quali parti della transazione sono coperte dalla firma. Parlerò di più di questo nel prossimo capitolo.

Ecco i passaggi per generare una firma ECDSA:

Primo, calcoliamo l'hash ($e$) del messaggio che deve essere firmato. Il messaggio $m$ viene quindi passato attraverso una funzione hash crittografica, generalmente SHA256 o doppio SHA256 nel caso di Bitcoin:

$$
e = \text{HASH}(m)
$$

Successivamente, calcoliamo un nonce. In crittografia, un nonce è semplicemente un numero generato in modo casuale o pseudo-casuale che viene utilizzato una sola volta. Ciò significa che ogni volta che viene effettuata una nuova firma digitale con questa coppia di chiavi, sarà molto importante utilizzare un nonce diverso, altrimenti, comprometterà la sicurezza della chiave privata. È quindi sufficiente determinare un intero casuale e unico $r$ tale che $1 \leq r \leq n-1$, dove $n$ è l'ordine del punto generatore $G$ della curva ellittica.

Poi, calcoleremo il punto $R$ sulla curva ellittica con le coordinate $(x_R, y_R)$ tale che:

$$
R = r \cdot G
$$

Estraiamo il valore dell'ascissa del punto $R$ ($x_R$). Questo valore rappresenta la prima parte della firma. E infine, calcoliamo la seconda parte della firma $s$ in questo modo:

$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$

dove:

- $r^{-1}$ è l'inverso modulare di $r$ modulo $n$, cioè un intero tale che $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ è la chiave privata dell'utente;
- $e$ è l'hash del messaggio;
- $n$ è l'ordine del punto generatore $G$ della curva ellittica.

La firma è quindi semplicemente la concatenazione di $x_R$ e $s$:

$$
\text{SIG} = x_R \Vert s
$$

### Verifica della Firma ECDSA

Per verificare una firma $(x_R, s)$, chiunque conosca la chiave pubblica $K$ e i parametri della curva ellittica può procedere in questo modo:
Prima, verifica che $x_R$ e $s$ siano nell'intervallo $[1, n-1]$. Questo assicura che la firma rispetti i vincoli matematici del gruppo ellittico. Se ciò non avviene, il verificatore rifiuta immediatamente la firma come non valida.
Poi, calcola l'hash del messaggio:

$$
e = \text{HASH}(m)
$$

Calcola l'inverso modulare di $s$ modulo $n$:

$$
s^{-1} \mod n
$$

Calcola due valori scalari $u_1$ e $u_2$ in questo modo:

$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$

E infine, calcola il punto $V$ sulla curva ellittica tale che:

$$
V = u_1 \cdot G + u_2 \cdot K
$$

La firma è valida solo se $x_V \equiv x_R \mod n$, dove $x_V$ è la coordinata $x$ del punto $V$. Infatti, combinando $u_1 \cdot G$ e $u_2 \cdot K$, si ottiene un punto $V$ che, se la firma è valida, deve corrispondere al punto $R$ utilizzato durante la firma (modulo $n$).

### Firma con il Protocollo Schnorr

Il schema di firma Schnorr è un'alternativa a ECDSA che offre molti vantaggi. È stato possibile utilizzarlo su Bitcoin dal 2021 e l'introduzione di Taproot, con i modelli di script P2TR. Come ECDSA, lo schema Schnorr consente di firmare un messaggio utilizzando una chiave privata, in modo tale che la firma possa essere verificata da chiunque conosca la corrispondente chiave pubblica.
Nel caso di Schnorr, si utilizza esattamente la stessa curva di ECDSA con gli stessi parametri. Tuttavia, le chiavi pubbliche sono rappresentate leggermente in modo diverso rispetto a ECDSA. Infatti, sono designate solo dalla coordinata $x$ del punto sulla curva ellittica. A differenza di ECDSA, dove le chiavi pubbliche compresse sono rappresentate da 33 byte (con il byte prefisso che indica la parità di $y$), Schnorr utilizza chiavi pubbliche di 32 byte, corrispondenti solo alla coordinata $x$ del punto $K$, ed è assunto che $y$ sia pari per default. Questa rappresentazione semplificata riduce la dimensione delle firme e facilita certe ottimizzazioni negli algoritmi di verifica.
La chiave pubblica è quindi la coordinata $x$ del punto $K$:

$$
\text{pk} = K_x
$$

Il primo passo per generare una firma è l'hash del messaggio. Ma a differenza di ECDSA, viene fatto con altri valori e si utilizza una funzione di hash etichettata per evitare collisioni in contesti diversi. Una funzione di hash etichettata implica semplicemente l'aggiunta di un'etichetta arbitraria agli input della funzione di hash insieme ai dati del messaggio.

![CYP201](assets/fr/023.webp)

Oltre al messaggio, vengono passati nella funzione etichettata anche la coordinata $x$ della chiave pubblica $K_x$, così come un punto $R$ calcolato dal nonce $r$ ($R=r \cdot G$) che è a sua volta un intero unico per ogni firma, calcolato deterministicamente dalla chiave privata e dal messaggio per evitare vulnerabilità legate al riutilizzo del nonce. Proprio come per la chiave pubblica, viene trattenuta solo la coordinata $x$ del punto nonce $R_x$ per descrivere il punto.

Il risultato di questo hashing notato $e$ è chiamato "sfida":
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n$$

Qui, $\text{HASH}$ è la funzione di hash SHA256, e $\text{``BIP0340/challenge''}$ è il tag specifico per l'hashing.

Infine, il parametro $s$ viene calcolato in questo modo dalla chiave privata $k$, dal nonce $r$ e dalla sfida $e$:

$$
s = (r + e \cdot k) \mod n
$$

La firma è quindi semplicemente la coppia $Rx$ e $s$.

$$
\text{SIG} = R_x \Vert s
$$

### Verifica della Firma Schnorr

La verifica di una firma Schnorr è più semplice di quella di una firma ECDSA. Ecco i passaggi per verificare la firma $(R_x, s)$ con la chiave pubblica $K_x$ e il messaggio $m$:
Prima, verifichiamo che $K_x$ sia un intero valido e minore di $p$. Se è così, recuperiamo il corrispondente punto sulla curva con $K_y$ pari. Estraiamo anche $R_x$ e $s$ separando la firma $\text{SIG}$. Poi, controlliamo che $R_x < p$ e $s < n$ (l'ordine della curva).
Successivamente, calcoliamo la sfida $e$ nello stesso modo in cui l'ha fatto l'emittente della firma:

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Poi, calcoliamo un punto di riferimento sulla curva in questo modo:

$$
R' = s \cdot G - e \cdot K
$$

Infine, verifichiamo che $R'_x = R_x$. Se le due coordinate x corrispondono, allora la firma $(R_x, s)$ è effettivamente valida con la chiave pubblica $K_x$.

### Perché funziona?

Il firmatario ha calcolato $s = r + e \cdot k \mod n$, quindi $R' = s \cdot G - e \cdot K$ dovrebbe essere uguale al punto originale $R$, perché:

$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$

Poiché $K = k \cdot G$, abbiamo $e \cdot k \cdot G = e \cdot K$. Quindi:

$$
R' = r \cdot G = R
$$

Pertanto, abbiamo:

$$
R'_x = R_x
$$

### I vantaggi delle firme Schnorr

Il sistema di firma Schnorr offre diversi vantaggi per Bitcoin rispetto all'algoritmo ECDSA originale. Prima di tutto, Schnorr consente l'aggregazione di chiavi e firme. Ciò significa che più chiavi pubbliche possono essere combinate in una singola chiave.

![CYP201](assets/fr/024.webp)

E allo stesso modo, più firme possono essere aggregate in una singola firma valida. Quindi, nel caso di una transazione multisignature, un insieme di partecipanti può firmare con una singola firma e una singola chiave pubblica aggregata. Ciò riduce significativamente i costi di archiviazione e di calcolo per la rete, poiché ogni nodo deve verificare una sola firma.

![CYP201](assets/fr/025.webp)

Inoltre, l'aggregazione delle firme migliora la privacy. Con Schnorr, diventa impossibile distinguere una transazione multisignature da una transazione standard a singola firma. Questa omogeneità rende l'analisi della catena più difficile, limitando la capacità di identificare le impronte dei portafogli.
Infine, Schnorr offre anche la possibilità di verifica in batch. Verificando simultaneamente più firme, i nodi possono guadagnare in efficienza, specialmente per i blocchi che contengono molte transazioni. Questa ottimizzazione riduce il tempo e le risorse necessarie per validare un blocco. Inoltre, le firme Schnorr non sono malleabili, a differenza delle firme prodotte con ECDSA. Ciò significa che un attaccante non può modificare una firma valida per crearne un'altra valida per lo stesso messaggio e la stessa chiave pubblica. Questa vulnerabilità era precedentemente presente su Bitcoin e ha impedito notevolmente l'implementazione sicura della Lightning Network. È stata risolta per ECDSA con il softfork SegWit nel 2017, che prevede lo spostamento delle firme in un database separato dalle transazioni per prevenirne la malleabilità.

### Perché Satoshi ha scelto ECDSA?

Come abbiamo visto, Satoshi ha inizialmente scelto di implementare ECDSA per le firme digitali su Bitcoin. Tuttavia, abbiamo anche visto che Schnorr è superiore a ECDSA sotto molti aspetti, e questo protocollo è stato creato da Claus-Peter Schnorr nel 1989, 20 anni prima dell'invenzione di Bitcoin.

Beh, non sappiamo realmente perché Satoshi non lo abbia scelto, ma un'ipotesi probabile è che questo protocollo fosse sotto brevetto fino al 2008. Anche se Bitcoin è stato creato un anno dopo, nel gennaio 2009, in quel momento non era disponibile alcuna standardizzazione open-source per le firme Schnorr. Forse Satoshi ha ritenuto più sicuro utilizzare ECDSA, che era già ampiamente utilizzato e testato nel software open-source e aveva diverse implementazioni riconosciute (in particolare la libreria OpenSSL utilizzata fino al 2015 su Bitcoin Core, poi sostituita da libsecp256k1 nella versione 0.10.0). O forse semplicemente non era a conoscenza che questo brevetto sarebbe scaduto nel 2008. In ogni caso, l'ipotesi più probabile sembra essere legata a questo brevetto e al fatto che ECDSA aveva una storia comprovata ed era più facile da implementare.

## I flag sighash

<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>

Come abbiamo visto nei capitoli precedenti, le firme digitali sono spesso utilizzate per sbloccare lo script di un input. Nel processo di firma, è necessario includere i dati firmati nel calcolo, designati nei nostri esempi dal messaggio $m$. Questi dati, una volta firmati, non possono essere modificati senza rendere la firma invalida. Infatti, sia per ECDSA che per Schnorr, il verificatore della firma deve includere nel suo calcolo lo stesso messaggio $m$. Se differisce dal messaggio $m$ inizialmente utilizzato dal firmatario, il risultato sarà errato e la firma sarà considerata invalida. Si dice quindi che una firma copre determinati dati e li protegge, in un certo senso, da modifiche non autorizzate.

### Cos'è un flag sighash?

Nel caso specifico di Bitcoin, abbiamo visto che il messaggio $m$ corrisponde alla transazione. Tuttavia, in realtà, è un po' più complesso. Infatti, grazie ai flag sighash, è possibile selezionare dati specifici all'interno della transazione che saranno coperti o meno dalla firma.
Il "flag sighash" è quindi un parametro aggiunto a ciascun input, che consente di determinare i componenti di una transazione che sono coperti dalla firma associata. Questi componenti sono gli input e gli output. La scelta del flag sighash determina quindi quali input e quali output della transazione sono fissati dalla firma e quali possono ancora essere modificati senza invalidarla. Questo meccanismo consente alle firme di impegnare i dati della transazione secondo le intenzioni del firmatario.
Ovviamente, una volta che la transazione è confermata sulla blockchain, diventa immutabile, indipendentemente dai flag sighash utilizzati. La possibilità di modifica tramite i flag sighash è limitata al periodo tra la firma e la conferma.
Generalmente, il software del portafoglio non offre l'opzione di modificare manualmente il flag sighash dei tuoi input quando costruisci una transazione. Per impostazione predefinita, è impostato `SIGHASH_ALL`. Personalmente, conosco solo Sparrow Wallet che permette questa modifica dall'interfaccia utente.

### Quali sono i flag sighash esistenti su Bitcoin?

Su Bitcoin, ci sono innanzitutto 3 flag sighash di base:

- `SIGHASH_ALL` (`0x01`): La firma si applica a tutti gli input e tutti gli output della transazione. La transazione è quindi interamente coperta dalla firma e non può più essere modificata. `SIGHASH_ALL` è il sighash più comunemente usato nelle transazioni quotidiane quando si vuole semplicemente effettuare una transazione senza che possa essere modificata.

![CYP201](assets/fr/026.webp)

In tutti i diagrammi di questo capitolo, il colore arancione rappresenta gli elementi coperti dalla firma, mentre il colore nero indica quelli che non lo sono.

- `SIGHASH_NONE` (`0x02`): La firma copre tutti gli input ma nessuno degli output, consentendo così la modifica degli output dopo la firma. Concretamente, è paragonabile a un assegno in bianco. Il firmatario sblocca gli UTXO negli input ma lascia il campo degli output completamente modificabile. Chiunque conosca questa transazione può quindi aggiungere l'output di sua scelta, ad esempio specificando un indirizzo di ricezione per raccogliere i fondi consumati dagli input, e poi trasmettere la transazione per recuperare i bitcoin. La firma del proprietario degli input non sarà invalidata, poiché copre solo gli input.

![CYP201](assets/fr/027.webp)

- `SIGHASH_SINGLE` (`0x03`): La firma copre tutti gli input così come un singolo output, corrispondente all'indice dell'input firmato. Ad esempio, se la firma sblocca lo _scriptPubKey_ dell'input #0, allora copre anche l'output #0. La firma protegge anche tutti gli altri input, che non possono più essere modificati. Tuttavia, chiunque può aggiungere un output aggiuntivo senza invalidare la firma, a condizione che l'output #0, che è l'unico coperto da essa, non venga modificato.
  ![CYP201](assets/fr/028.webp)

Oltre a questi tre flag sighash, esiste anche il modificatore `SIGHASH_ANYONECANPAY` (`0x80`). Questo modificatore può essere combinato con un flag sighash di base per creare tre nuovi flag sighash:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): La firma copre un singolo input includendo tutti gli output della transazione. Questo flag sighash combinato permette, ad esempio, la creazione di una transazione di crowdfunding. L'organizzatore prepara l'output con il proprio indirizzo e l'importo target, e ogni investitore può poi aggiungere input per finanziare questo output. Una volta raccolti fondi sufficienti negli input per soddisfare l'output, la transazione può essere trasmessa.

![CYP201](assets/fr/029.webp)

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): La firma copre un singolo input, senza impegnarsi su alcun output;

![CYP201](assets/fr/030.webp)

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): La firma copre un singolo input così come l'output che ha lo stesso indice di questo input. Ad esempio, se la firma sblocca lo _scriptPubKey_ dell'input #3, coprirà anche l'output #3. Il resto della transazione rimane modificabile, sia in termini di altri input che di altri output.
  ![CYP201](assets/fr/031.webp)

### Progetti per Aggiungere Nuove Flag Sighash

Attualmente (2024), solo le flag sighash presentate nella sezione precedente sono utilizzabili su Bitcoin. Tuttavia, alcuni progetti stanno considerando l'aggiunta di nuove flag sighash. Ad esempio, il BIP118, proposto da Christian Decker e Anthony Towns, introduce due nuove flag sighash: `SIGHASH_ANYPREVOUT` e `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Qualsiasi Output Precedente"_).

Queste due flag sighash offrirebbero una possibilità aggiuntiva su Bitcoin: creare firme che non coprono nessun input specifico della transazione.

![CYP201](assets/fr/032.webp)

Questa idea è stata inizialmente formulata da Joseph Poon e Thaddeus Dryja nel Lightning White Paper. Prima della sua rinominazione, questa flag sighash era denominata `SIGHASH_NOINPUT`.
Se questa flag sighash viene integrata in Bitcoin, consentirà l'uso di covenants, ma è anche un prerequisito obbligatorio per implementare Eltoo, un protocollo generale per i second layer che definisce come gestire congiuntamente la proprietà di un UTXO. Eltoo è stato specificamente progettato per risolvere i problemi associati ai meccanismi di negoziazione dello stato dei canali Lightning, ovvero tra l'apertura e la chiusura.

Per approfondire la tua conoscenza della Lightning Network, dopo il corso CYP201, ti consiglio vivamente il corso LNP201 di Fanis Michalakis, che copre l'argomento in dettaglio:

https://planb.network/courses/lnp201

Nella prossima parte, propongo di scoprire come funziona la frase mnemonica alla base del tuo portafoglio Bitcoin.

# La frase mnemonica

<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Evoluzione dei portafogli Bitcoin

<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Ora che abbiamo esplorato il funzionamento delle funzioni hash e delle firme digitali, possiamo studiare come funzionano i portafogli Bitcoin. L'obiettivo sarà immaginare come è costruito un portafoglio su Bitcoin, come è decomposto e quali sono le diverse informazioni che lo costituiscono utilizzate. Questa comprensione dei meccanismi del portafoglio ti permetterà di migliorare il tuo uso di Bitcoin in termini di sicurezza e privacy.

Prima di immergerci nei dettagli tecnici, è essenziale chiarire cosa si intende per "portafoglio Bitcoin" e comprendere la sua utilità.

### Cos'è un portafoglio Bitcoin?

A differenza dei portafogli tradizionali, che ti permettono di conservare banconote e monete fisiche, un portafoglio Bitcoin non "contiene" di per sé i bitcoin. Infatti, i bitcoin non esistono in una forma fisica o digitale che può essere conservata, ma sono rappresentati da unità di conto raffigurate nel sistema sotto forma di **UTXOs** (_Unspent Transaction Output_).
Gli UTXO rappresentano quindi frammenti di bitcoin, di dimensioni variabili, che possono essere spesi a condizione che il loro _scriptPubKey_ sia soddisfatto. Per spendere i suoi bitcoin, un utente deve fornire uno _scriptSig_ che sblocca lo _scriptPubKey_ associato al suo UTXO. Questa prova è generalmente fornita attraverso una firma digitale, generata dalla chiave privata corrispondente alla chiave pubblica presente nello _scriptPubKey_. Quindi, l'elemento cruciale che l'utente deve proteggere è la chiave privata. Il ruolo di un portafoglio Bitcoin è proprio quello di gestire queste chiavi private in modo sicuro. In realtà, il suo ruolo è più simile a quello di un portachiavi che non a un portafoglio nel senso tradizionale.

### Portafogli JBOK (_Just a Bunch Of Keys_)

I primi portafogli utilizzati su Bitcoin erano i portafogli JBOK (_Just a Bunch Of Keys_), che raggruppavano chiavi private generate indipendentemente e senza alcun collegamento tra loro. Questi portafogli operavano su un modello semplice dove ogni chiave privata poteva sbloccare un unico indirizzo Bitcoin di ricezione.

![CYP201](assets/fr/033.webp)

Se si desiderava utilizzare più chiavi private, era quindi necessario effettuare altrettanti backup per garantire l'accesso ai fondi in caso di problemi con il dispositivo che ospita il portafoglio. Se si utilizza una singola chiave privata, questa struttura del portafoglio può essere sufficiente, poiché un singolo backup è abbastanza. Tuttavia, questo pone un problema: su Bitcoin, è fortemente sconsigliato utilizzare sempre la stessa chiave privata. Infatti, una chiave privata è associata a un indirizzo unico, e gli indirizzi Bitcoin di ricezione sono normalmente progettati per un uso singolo. Ogni volta che ricevi fondi, dovresti generare un nuovo indirizzo vuoto.

Questo vincolo deriva dal modello di privacy di Bitcoin. Riutilizzando lo stesso indirizzo, si facilita per gli osservatori esterni la tracciabilità di tutte le mie transazioni Bitcoin. Ecco perché è fortemente sconsigliato riutilizzare un indirizzo di ricezione. Tuttavia, per avere più indirizzi e separare pubblicamente le nostre transazioni, è necessario gestire più chiavi private. Nel caso dei portafogli JBOK, ciò implica la creazione di altrettanti backup quanti sono le nuove coppie di chiavi, un compito che può rapidamente diventare complesso e difficile da mantenere per gli utenti.

Per saperne di più sul modello di privacy di Bitcoin e scoprire metodi per proteggere la tua privacy, ti consiglio anche di seguire il mio corso BTC204 su Plan ₿ Network:

https://planb.network/courses/btc204

### Portafogli HD (_Hierarchical Deterministic_)

Per affrontare il limite dei portafogli JBOK, è stata successivamente utilizzata una nuova struttura di portafoglio. Nel 2012, Pieter Wuille ha introdotto un miglioramento con BIP32, che introduce i portafogli gerarchici deterministici. Il principio di un portafoglio HD è quello di derivare tutte le chiavi private da una singola fonte di informazione, chiamata seed, in modo deterministico e gerarchico. Questo seed viene generato casualmente alla creazione del portafoglio e costituisce un backup unico che consente di ricreare tutte le chiavi private del portafoglio. Così, l'utente può generare un numero molto elevato di chiavi private per evitare il riutilizzo degli indirizzi e preservare la propria privacy, avendo bisogno di effettuare un solo backup del proprio portafoglio tramite il seed.
![CYP201](assets/fr/034.webp)

Nei portafogli HD, la derivazione delle chiavi è eseguita secondo una struttura gerarchica che consente di organizzare le chiavi in sottospazi di derivazione, ciascuno ulteriormente suddivisibile, per facilitare la gestione dei fondi e l'interoperabilità tra diversi software di portafoglio. Oggi, questo standard è adottato dalla stragrande maggioranza degli utenti Bitcoin. Per questo motivo, lo esamineremo in dettaglio nei capitoli seguenti.

### Lo Standard BIP39: La Frase Mnemonica

Oltre a BIP32, BIP39 standardizza il formato del seed come frase mnemonica, per facilitare il backup e la leggibilità da parte degli utenti. La frase mnemonica, chiamata anche frase di recupero o frase di 24 parole, è una sequenza di parole tratte da un elenco predefinito che codifica in modo sicuro il seed del portafoglio.

La frase mnemonica semplifica notevolmente il backup per l'utente. In caso di perdita, danneggiamento o furto del dispositivo che ospita il portafoglio, conoscere semplicemente questa frase mnemonica consente la ricreazione del portafoglio e il recupero dell'accesso a tutti i fondi da esso protetti.

Nei capitoli successivi, esploreremo il funzionamento interno dei portafogli HD, inclusi i meccanismi di derivazione delle chiavi e le diverse possibili strutture gerarchiche. Questo ti permetterà di comprendere meglio le fondamenta crittografiche su cui si basa la sicurezza dei fondi su Bitcoin. E per iniziare, nel prossimo capitolo, propongo di scoprire il ruolo dell'entropia alla base del tuo portafoglio.

## Entropia e Numero Casuale

<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>
I moderni portafogli HD (deterministici e gerarchici) si affidano a un unico pezzo iniziale di informazione chiamato "entropia" per generare in modo deterministico l'intero set di chiavi del portafoglio. Questa entropia è un numero pseudo-casuale il cui livello di caos determina in parte la sicurezza del portafoglio.

### Definizione di Entropia

L'entropia, nel contesto della crittografia e dell'informazione, è una misura quantitativa dell'incertezza o imprevedibilità associata a una fonte di dati o a un processo casuale. Gioca un ruolo importante nella sicurezza dei sistemi crittografici, specialmente nella generazione di chiavi e numeri casuali. Un'alta entropia assicura che le chiavi generate siano sufficientemente imprevedibili e resistenti agli attacchi di forza bruta, dove un attaccante prova tutte le combinazioni possibili per indovinare la chiave.

Nel contesto di Bitcoin, l'entropia è utilizzata per generare il seed. Quando si crea un portafoglio deterministico e gerarchico, la costruzione della frase mnemonica avviene a partire da un numero casuale, a sua volta derivato da una fonte di entropia. La frase viene poi utilizzata per generare più chiavi private, in modo deterministico e gerarchico, per creare condizioni di spesa su UTXO.

### Metodi di Generazione dell'Entropia

L'entropia iniziale utilizzata per un portafoglio HD è generalmente di 128 bit o 256 bit, dove:

- **128 bit di entropia** corrispondono a una frase mnemonica di **12 parole**;
- **256 bit di entropia** corrispondono a una frase mnemonica di **24 parole**.

Nella maggior parte dei casi, questo numero casuale è generato automaticamente dal software del portafoglio utilizzando un PRNG (_Pseudo-Random Number Generator_). I PRNG sono una categoria di algoritmi utilizzati per generare sequenze di numeri da uno stato iniziale, che hanno caratteristiche che si avvicinano a quelle di un numero casuale, senza però esserlo. Un buon PRNG deve avere proprietà come uniformità dell'output, imprevedibilità e resistenza agli attacchi predittivi. A differenza dei generatori di numeri casuali veri (TRNG), i PRNG sono deterministici e riproducibili.

![CYP201](assets/fr/035.webp)

Un'alternativa è generare manualmente l'entropia, che offre un controllo migliore ma è anche molto più rischioso. Sconsiglio vivamente di generare da soli l'entropia per il vostro portafoglio HD.

Nel prossimo capitolo, vedremo come si passa da un numero casuale a una frase mnemonica di 12 o 24 parole.

## La Frase Mnemonica

<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>
La frase mnemonica, chiamata anche "frase seme", "frase di recupero", "frase segreta" o "frase di 24 parole", è una sequenza solitamente composta da 12 o 24 parole, generata a partire dall'entropia. Viene utilizzata per derivare deterministicamente tutte le chiavi di un portafoglio HD. Questo significa che da questa frase è possibile generare e ricreare deterministicamente tutte le chiavi private e pubbliche del portafoglio Bitcoin, e di conseguenza accedere ai fondi che sono protetti con essa. Lo scopo della frase mnemonica è fornire un mezzo di backup e recupero dei bitcoin che sia sia sicuro che facile da usare. È stata introdotta negli standard nel 2013 con il BIP39.
Scopriamo insieme come passare dall'entropia a una frase mnemonica.

### Il Checksum

Per trasformare l'entropia in una frase mnemonica, si deve prima aggiungere un checksum (o "somma di controllo") alla fine dell'entropia. Questo checksum è una breve sequenza di bit che garantisce l'integrità dei dati verificando che non siano state introdotte modifiche accidentali.

Per calcolare il checksum, si applica la funzione hash SHA256 all'entropia (solo una volta; questo è uno dei rari casi in Bitcoin in cui si usa un singolo hash SHA256 invece di un doppio hash). Questa operazione produce un hash di 256 bit. Il checksum consiste nei primi bit di questo hash, e la sua lunghezza dipende da quella dell'entropia, secondo la seguente formula:

$$
\text{CS} = \frac{\text{ENT}}{32}
$$

dove $\text{ENT}$ rappresenta la lunghezza dell'entropia in bit, e $\text{CS}$ la lunghezza del checksum in bit.

Per esempio, per un'entropia di 256 bit, si prendono i primi 8 bit dell'hash per formare il checksum:

$$
\text{CS} = \frac{256}{32} = 8 \text{ bit}
$$

Una volta calcolato il checksum, viene concatenato con l'entropia per ottenere una sequenza di bit estesa indicata con $\text{ENT} \Vert \text{CS}$ ("concatenare" significa mettere in fila).

![CYP201](assets/fr/036.webp)

### Corrispondenza tra l'Entropia e la Frase Mnemonica

Il numero di parole nella frase mnemonica dipende dalla dimensione dell'entropia iniziale, come illustrato nella seguente tabella con:

- $\text{ENT}$: la dimensione in bit dell'entropia;
- $\text{CS}$: la dimensione in bit del checksum;
- $w$: il numero di parole nella frase mnemonica finale.

$$
\begin{array}{|c|c|c|c|}
\hline
Per esempio, per un'entropia di 256 bit, il risultato $\text{ENT} \Vert \text{CS}$ è di 264 bit e produce una frase mnemonica di 24 parole.

### Conversione della Sequenza Binaria in una Frase Mnemonica

La sequenza di bit $\text{ENT} \Vert \text{CS}$ viene quindi divisa in segmenti di 11 bit. Ogni segmento di 11 bit, una volta convertito in decimale, corrisponde a un numero tra 0 e 2047, che designa la posizione di una parola [in una lista di 2048 parole standardizzata dal BIP39](https://github.com/Plan ₿-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).

![CYP201](assets/fr/037.webp)
Per esempio, per un'entropia di 128 bit, il checksum è di 4 bit, e quindi la sequenza totale misura 132 bit. È divisa in 12 segmenti di 11 bit (i bit arancioni designano il checksum):

![CYP201](assets/fr/038.webp)

Ogni segmento è poi convertito in un numero decimale che rappresenta una parola nella lista. Per esempio, il segmento binario `01011010001` è equivalente in decimale a `721`. Aggiungendo 1 per allinearsi con l'indicizzazione della lista (che inizia da 1 e non da 0), si ottiene il rango della parola `722`, che è "*focus*" nella lista.

![CYP201](assets/fr/039.webp)

Questa corrispondenza è ripetuta per ciascuno dei 12 segmenti, al fine di ottenere una frase di 12 parole.

![CYP201](assets/fr/040.webp)

### Caratteristiche della Lista di Parole BIP39

Una particolarità della lista di parole BIP39 è che nessuna parola condivide le stesse prime quattro lettere nello stesso ordine con un'altra parola. Questo significa che annotare solo le prime quattro lettere di ogni parola è sufficiente per salvare la frase mnemonica. Questo può essere interessante per risparmiare spazio, specialmente per coloro che desiderano inciderla su un supporto metallico.

Questa lista di 2048 parole esiste in diverse lingue. Queste non sono semplici traduzioni, ma parole distinte per ogni lingua. Tuttavia, è fortemente consigliato attenersi alla versione inglese, poiché le versioni in altre lingue generalmente non sono supportate dal software del portafoglio.

### Quale Lunghezza Scegliere per la Tua Frase Mnemonica?
Per determinare la lunghezza ottimale della tua frase mnemonica, si deve considerare la reale sicurezza che essa fornisce. Una frase di 12 parole assicura 128 bit di sicurezza, mentre una frase di 24 parole offre 256 bit.

Tuttavia, questa differenza nella sicurezza a livello di frase non migliora la sicurezza complessiva di un portafoglio Bitcoin, poiché le chiavi private derivate da questa frase beneficiano solo di 128 bit di sicurezza. Infatti, come abbiamo visto in precedenza, le chiavi private Bitcoin sono generate da numeri casuali (o derivate da una fonte casuale) compresi tra $1$ e $n-1$, dove $n$ rappresenta l'ordine del punto generatore $G$ della curva secp256k1, un numero leggermente inferiore a $2^{256}$. Si potrebbe quindi pensare che queste chiavi private offrano 256 bit di sicurezza. Tuttavia, la loro sicurezza risiede nella difficoltà di trovare una chiave privata a partire dalla sua chiave pubblica associata, una difficoltà stabilita dal problema matematico del logaritmo discreto sulle curve ellittiche (*ECDLP*). Ad oggi, l'algoritmo più noto per risolvere questo problema è l'algoritmo rho di Pollard, che riduce il numero di operazioni necessarie per violare una chiave alla radice quadrata della sua dimensione.

Per le chiavi a 256 bit, come quelle utilizzate su Bitcoin, l'algoritmo rho di Pollard riduce quindi la complessità a $2^{128}$ operazioni:


$$

O(\sqrt{2^{256}}) = O(2^{128})

$$

Pertanto, si considera che una chiave privata utilizzata su Bitcoin offra 128 bit di sicurezza.

Di conseguenza, scegliere una frase di 24 parole non fornisce una protezione aggiuntiva per il portafoglio, poiché 256 bit di sicurezza sulla frase sono inutili se le chiavi derivate offrono solo 128 bit di sicurezza. Per illustrare questo principio, è come avere una casa con due porte: una porta di legno vecchia e una porta blindata. In caso di effrazione, la porta blindata non sarebbe di alcuna utilità, poiché l'intruso passerebbe attraverso la porta di legno. Questa è una situazione analoga qui.
Una frase di 12 parole, che offre quindi 128 bit di sicurezza, è attualmente sufficiente per proteggere i tuoi bitcoin da qualsiasi tentativo di furto. Finché l'algoritmo di firma digitale non cambia per utilizzare chiavi più grandi o per affidarsi a un problema matematico diverso dall'ECDLP, una frase di 24 parole rimane superflua. Inoltre, una frase più lunga aumenta il rischio di perdita durante il backup: un backup che è due volte più corto è sempre più facile da gestire.
Per approfondire e imparare concretamente come generare manualmente una frase mnemonica di prova, ti consiglio di scoprire questo tutorial:

https://planb.network/tutorials/wallet/generate-mnemonic-phrase
Prima di continuare con la derivazione del portafoglio da questa frase mnemonica, ti presenterò, nel capitolo seguente, la passphrase BIP39, poiché gioca un ruolo nel processo di derivazione, ed è allo stesso livello della frase mnemonica.
## La passphrase
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

Come abbiamo appena visto, i portafogli HD sono generati da una frase mnemonica che tipicamente consiste di 12 o 24 parole. Questa frase è molto importante perché permette il ripristino di tutte le chiavi di un portafoglio in caso il suo dispositivo fisico (come un portafoglio hardware, ad esempio) venga perso. Tuttavia, costituisce un unico punto di fallimento, perché se viene compromessa, un attaccante potrebbe rubare tutti i bitcoin. Qui entra in gioco la passphrase BIP39.

### Cos'è una passphrase BIP39?

La passphrase è una password opzionale, che puoi scegliere liberamente, che viene aggiunta alla frase mnemonica nel processo di derivazione della chiave per migliorare la sicurezza del portafoglio.

Attenzione, la passphrase non deve essere confusa con il codice PIN del tuo portafoglio hardware o la password usata per sbloccare l'accesso al tuo portafoglio sul tuo computer. A differenza di tutti questi elementi, la passphrase gioca un ruolo nella derivazione delle chiavi del tuo portafoglio. **Questo significa che senza di essa, non sarai mai in grado di recuperare i tuoi bitcoin.**

La passphrase lavora in tandem con la frase mnemonica, modificando il seme da cui vengono generate le chiavi. Così, anche se qualcuno ottiene la tua frase di 12 o 24 parole, senza la passphrase, non possono accedere ai tuoi fondi. Usare una passphrase crea essenzialmente un nuovo portafoglio con chiavi distinte. Modificare (anche leggermente) la passphrase genererà un portafoglio diverso.

![CYP201](assets/fr/041.webp)

### Perché dovresti usare una passphrase?

La passphrase è arbitraria e può essere qualsiasi combinazione di caratteri scelta dall'utente. Usare una passphrase offre quindi diversi vantaggi. Prima di tutto, riduce tutti i rischi associati al compromesso della frase mnemonica richiedendo un secondo fattore per accedere ai fondi (effrazione, accesso alla tua casa, ecc.).

In seguito, può essere usata strategicamente per creare un portafoglio esca, per affrontare vincoli fisici per rubare i tuoi fondi come il famigerato "_attacco con chiave inglese da 5 dollari_". In questo scenario, l'idea è di avere un portafoglio senza passphrase contenente solo una piccola quantità di bitcoin, abbastanza per soddisfare un potenziale aggressore, mentre si ha un portafoglio nascosto. Quest'ultimo utilizza la stessa frase mnemonica ma è protetto con una passphrase aggiuntiva.
Infine, l'uso di una passphrase è interessante quando si desidera controllare la casualità della generazione del seme del portafoglio HD.
### Come scegliere una buona passphrase?

Affinché la passphrase sia efficace, deve essere sufficientemente lunga e casuale. Come per una password forte, raccomando di scegliere una passphrase il più lunga e casuale possibile, con una diversità di lettere, numeri e simboli per rendere impossibile qualsiasi attacco di forza bruta.
È inoltre importante salvare correttamente questa passphrase, allo stesso modo della frase mnemonica. **Perderla significa perdere l'accesso ai propri bitcoin**. Sconsiglio vivamente di ricordarla soltanto a memoria, poiché ciò aumenta in modo irragionevole il rischio di perdita. L'ideale è scriverla su un supporto fisico (carta o metallo) separato dalla frase mnemonica. Questo backup deve ovviamente essere conservato in un luogo diverso da dove si conserva la frase mnemonica per prevenire che entrambi vengano compromessi simultaneamente.
![CYP201](assets/fr/042.webp)

Nella sezione seguente, scopriremo come questi due elementi alla base del tuo portafoglio — la frase mnemonica e la passphrase — vengono utilizzati per derivare le coppie di chiavi usate nello *scriptPubKey* che blocca i tuoi UTXO.

# Creazione di Portafogli Bitcoin
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Creazione del Seed e della Chiave Master
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Una volta generati la frase mnemonica e la passphrase opzionale, può iniziare il processo di derivazione di un portafoglio HD Bitcoin. La frase mnemonica viene prima convertita in un seed che costituisce la base di tutte le chiavi del portafoglio.

![CYP201](assets/fr/043.webp)

### Il Seed di un Portafoglio HD

Lo standard BIP39 definisce il seed come una sequenza di 512 bit, che serve come punto di partenza per la derivazione di tutte le chiavi di un portafoglio HD. Il seed è derivato dalla frase mnemonica e dalla possibile passphrase utilizzando l'algoritmo **PBKDF2** (*Password-Based Key Derivation Function 2*) di cui abbiamo già discusso nel capitolo 3.3. In questa funzione di derivazione, utilizzeremo i seguenti parametri:

- $m$ : la frase mnemonica;
- $p$ : una passphrase opzionale scelta dall'utente per aumentare la sicurezza del seed. Se non c'è una passphrase, questo campo viene lasciato vuoto;
- $\text{PBKDF2}$ : la funzione di derivazione con $\text{HMAC-SHA512}$ e $2048$ iterazioni;
- $s$: il seed del portafoglio di 512 bit.
Indipendentemente dalla lunghezza della frase mnemonica scelta (132 bit o 264 bit), la funzione PBKDF2 produrrà sempre un output di 512 bit, e il seed sarà quindi sempre di questa dimensione.

### Schema di Derivazione del Seed con PBKDF2

La seguente equazione illustra la derivazione del seed dalla frase mnemonica e dalla passphrase:


$$

s = \text{PBKDF2}\_{\text{HMAC-SHA512}}(m, p, 2048)

$$

![CYP201](assets/fr/044.webp)

Il valore del seed è quindi influenzato dal valore della frase mnemonica e della passphrase. Cambiando la passphrase, si ottiene un seed diverso. Tuttavia, con la stessa frase mnemonica e passphrase, viene sempre generato lo stesso seed, poiché PBKDF2 è una funzione deterministica. Questo garantisce che le stesse coppie di chiavi possano essere recuperate attraverso i nostri backup.

**Nota:** Nel linguaggio comune, il termine "seed" si riferisce spesso, per abuso di linguaggio, alla frase mnemonica. Infatti, in assenza di una passphrase, uno è semplicemente la codifica dell'altro. Tuttavia, come abbiamo visto, nella realtà tecnica dei portafogli, il seed e la frase mnemonica sono effettivamente due elementi distinti.

Ora che abbiamo il nostro seed, possiamo continuare con la derivazione del nostro portafoglio Bitcoin.
### La Chiave Maestra e il Codice Catena Maestro
Una volta ottenuto il seed, il passo successivo nella derivazione di un portafoglio HD coinvolge il calcolo della chiave privata maestra e del codice catena maestro, che rappresenteranno il livello 0 del nostro portafoglio.

Per ottenere la chiave privata maestra e il codice catena maestro, la funzione HMAC-SHA512 viene applicata al seed, utilizzando una chiave fissa "*Bitcoin Seed*" identica per tutti gli utenti Bitcoin. Questa costante è scelta per garantire che le derivazioni delle chiavi siano specifiche per Bitcoin. Ecco gli elementi:
- $\text{HMAC-SHA512}$: la funzione di derivazione;
- $s$: il seed del portafoglio da 512 bit;
- $\text{"Bitcoin Seed"}$: la costante di derivazione comune per tutti i portafogli Bitcoin.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)

$$

L'output di questa funzione è quindi di 512 bit. Viene poi diviso in 2 parti:
- I 256 bit a sinistra formano la **chiave privata maestra**;
- I 256 bit a destra formano il **codice catena maestro**.
Matematicamente, questi due valori possono essere notati come segue con $k_M$ che rappresenta la chiave privata maestra e $C_M$ il codice catena maestro:
$$

k*M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)*{[:256]}

$$


$$

C*M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)*{[256:]}

$$

![CYP201](assets/fr/045.webp)

### Ruolo della Chiave Maestra e del Codice Catena

La chiave privata maestra è considerata la chiave genitore, da cui tutte le chiavi private derivate — figli, nipoti, pronipoti, ecc. — saranno generate. Rappresenta il livello zero nella gerarchia di derivazione.

Il codice catena maestro, d'altra parte, introduce una fonte aggiuntiva di entropia nel processo di derivazione delle chiavi per i figli, al fine di contrastare certi potenziali attacchi. Inoltre, nel portafoglio HD, ogni coppia di chiavi ha un codice catena unico associato ad essa, che viene anche utilizzato per derivare chiavi figlie da questa coppia, ma discuteremo di questo più dettagliatamente nei prossimi capitoli.

Prima di continuare con la derivazione del portafoglio HD con i seguenti elementi, desidero, nel prossimo capitolo, introdurvi alle chiavi estese, che sono spesso confuse con la chiave maestra. Vedremo come sono costruite e quale ruolo giocano nel portafoglio Bitcoin.

## Chiavi Estese
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Una chiave estesa è semplicemente la concatenazione di una chiave (sia privata che pubblica) e il suo codice catena associato. Questo codice catena è essenziale per la derivazione delle chiavi figlie perché, senza di esso, è impossibile derivare chiavi figlie da una chiave genitore, ma scopriremo questo processo più precisamente nel prossimo capitolo. Queste chiavi estese permettono quindi di aggregare tutte le informazioni necessarie per derivare chiavi figlie, semplificando così la gestione degli account all'interno di un portafoglio HD.

![CYP201](assets/fr/046.webp)

La chiave estesa consiste di due parti:
- Il payload, che contiene la chiave privata o pubblica così come il codice catena associato;
- I metadati, che sono varie informazioni per facilitare l'interoperabilità tra software e migliorare la comprensione per l'utente.

### Come Funzionano le Chiavi Estese
Quando la chiave estesa contiene una chiave privata, viene definita come chiave privata estesa. È riconosciuta dal suo prefisso che contiene la menzione `prv`. Oltre alla chiave privata, la chiave privata estesa contiene anche il codice catena associato. Con questo tipo di chiave estesa, è possibile derivare tutti i tipi di chiavi private figlie e, quindi, mediante l'addizione e il raddoppio dei punti sulle curve ellittiche, permette anche la derivazione dell'intero insieme di chiavi pubbliche figlie.
Quando la chiave estesa non contiene una chiave privata, ma invece una chiave pubblica, viene definita come chiave pubblica estesa. È riconosciuta dal suo prefisso che contiene la menzione `pub`. Ovviamente, oltre alla chiave, contiene anche il codice catena associato. A differenza della chiave privata estesa, la chiave pubblica estesa permette la derivazione solo di chiavi pubbliche figlie "normali" (cioè non può derivare chiavi figlie "rinforzate"). Vedremo nel capitolo seguente cosa significano questi qualificatori "normali" e "rinforzati".

In ogni caso, la chiave pubblica estesa non permette la derivazione di chiavi private figlie. Pertanto, anche se qualcuno ha accesso a un `xpub`, non sarà in grado di spendere i fondi associati, poiché non avrà accesso alle corrispondenti chiavi private. Possono solo derivare chiavi pubbliche figlie per osservare le transazioni associate.

Per il seguito, adotteremo la seguente notazione:
- $K_{\text{PAR}}$: una chiave pubblica genitore;
- $k_{\text{PAR}}$: una chiave privata genitore;
- $C_{\text{PAR}}$: un codice catena genitore;
- $C_{\text{CHD}}$: un codice catena figlio;
- $K_{\text{CHD}}^n$: una chiave pubblica figlio normale;
- $k_{\text{CHD}}^n$: una chiave privata figlio normale;
- $K_{\text{CHD}}^h$: una chiave pubblica figlio rinforzata;
- $k_{\text{CHD}}^h$: una chiave privata figlio rinforzata.

![CYP201](assets/fr/047.webp)

### Costruzione di una Chiave Estesa

Una chiave estesa è strutturata come segue:
- **Versione**: Codice versione per identificare la natura della chiave (`xprv`, `xpub`, `yprv`, `ypub`...). Vedremo alla fine di questo capitolo a cosa corrispondono le lettere `x`, `y` e `z`.
- **Profondità**: Livello gerarchico nel portafoglio HD relativo alla chiave maestra (0 per la chiave maestra).
- **Impronta Genitore**: I primi 4 byte dell'hash HASH160 della chiave pubblica genitore utilizzata per derivare la chiave presente nel payload.
- **Numero Indice**: Identificatore del figlio tra le chiavi fratelli, ovvero tra tutte le chiavi allo stesso livello di derivazione che hanno gli stessi genitori.
- **Codice Catena**: Un codice unico di 32 byte per derivare le chiavi figlie.
- **Chiave**: La chiave privata (prefissata da 1 byte per la dimensione) o la chiave pubblica.
- **Checksum**: Un checksum calcolato con la funzione HASH256 (doppio SHA256) viene anche aggiunto, il che permette la verifica dell'integrità della chiave estesa durante la sua trasmissione o memorizzazione.

Il formato completo di una chiave estesa è quindi di 78 byte senza il checksum, e di 82 byte con il checksum. Viene poi convertito in Base58 per produrre una rappresentazione facilmente leggibile dagli utenti. Il formato Base58 è lo stesso utilizzato per gli indirizzi di ricezione *Legacy* (prima di *SegWit*).

| Elemento          | Descrizione                                                                                                        | Dimensione |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Versione          | Indica se la chiave è pubblica (`xpub`, `ypub`) o privata (`xprv`, `zprv`), così come la versione della chiave estesa | 4 byte    |
| Profondità        | Livello nella gerarchia rispetto alla chiave principale                                                             | 1 byte    |
| Impronta Genitore | I primi 4 byte di HASH160 della chiave pubblica genitore                                                            | 4 byte    |
| Numero Indice     | Posizione della chiave nell'ordine dei figli                                                                        | 4 byte    |
| Codice Catena     | Utilizzato per derivare le chiavi figlie                                                                            | 32 byte   |
| Chiave            | La chiave privata (con un prefisso di 1 byte) o la chiave pubblica                                                  | 33 byte   |
| Checksum          | Checksum per verificare l'integrità                                                                                 | 4 byte    |

Se viene aggiunto un byte solo alla chiave privata, è perché la chiave pubblica compressa è più lunga della chiave privata di un byte. Questo byte aggiuntivo, inserito all'inizio della chiave privata come `0x00`, eguaglia le loro dimensioni, assicurando che il payload della chiave estesa sia della stessa lunghezza, sia che si tratti di una chiave pubblica o privata.

### Prefissi delle Chiavi Estese
Come abbiamo appena visto, le chiavi estese includono un prefisso che indica sia la versione della chiave estesa sia la sua natura. La notazione `pub` indica che si riferisce a una chiave pubblica estesa, e la notazione `prv` indica una chiave privata estesa. La lettera aggiuntiva alla base della chiave estesa aiuta ad indicare se lo standard seguito è Legacy, SegWit v0, SegWit v1, ecc.
Ecco un riassunto dei prefissi utilizzati e dei loro significati:

| Prefisso Base 58 | Prefisso Base 16 | Rete     | Scopo                | Script Associati         | Derivazione                | Tipo di Chiave |
|------------------|------------------|----------|----------------------|--------------------------|----------------------------|----------------|
| `xpub`           | `0488b21e`       | Mainnet  | Legacy e SegWit V1   | P2PK / P2PKH / P2TR      | `m/44'/0'`, `m/86'/0'`     | pubblica       |
| `xprv`           | `0488ade4`       | Mainnet  | Legacy e SegWit V1   | P2PK / P2PKH / P2TR      | `m/44'/0'`, `m/86'/0'`     | privata        |
| `tpub`           | `043587cf`       | Testnet  | Legacy e SegWit V1   | P2PK / P2PKH / P2TR      | `m/44'/1'`, `m/86'/1'`     | pubblica       |
| `tprv`           | `04358394`       | Testnet  | Legacy e SegWit V1   | P2PK / P2PKH / P2TR      | `m/44'/1'`, `m/86'/1'`     | privata        |
| `ypub`           | `049d7cb2`       | Mainnet  | Nested SegWit        | P2WPKH in P2SH           | `m/49'/0'`                 | pubblica       |
Questa tabella fornisce una panoramica completa dei prefissi utilizzati nelle chiavi estese, dettagliando i loro prefissi in base 58 e base 16, la rete a cui sono associati (Mainnet o Testnet), il loro scopo, gli script a cui sono associati, il loro percorso di derivazione e se sono chiavi pubbliche o private.
| `yprv`         | `049d7878`         | Mainnet  | Nested SegWit        | P2WPKH in P2SH           | `m/49'/0'`                 | privata     |
| `upub`         | `049d7cb2`         | Testnet  | Nested SegWit        | P2WPKH in P2SH           | `m/49'/1'`                 | pubblica    |
| `uprv`         | `044a4e28`         | Testnet  | Nested SegWit        | P2WPKH in P2SH           | `m/49'/1'`                 | privata     |
| `zpub`         | `04b24746`         | Mainnet  | SegWit V0            | P2WPKH                   | `m/84'/0'`                 | pubblica    |
| `zprv`          | `04b2430c`          | Mainnet  | SegWit V0            | P2WPKH                    | `m/84'/0'`                  | privata     |
| `vpub`          | `045f1cf6`          | Testnet  | SegWit V0            | P2WPKH                    | `m/84'/1'`                  | pubblica    |
| `vprv`          | `045f18bc`          | Testnet  | SegWit V0            | P2WPKH                    | `m/84'/1'`                  | privata     |

### Dettagli degli Elementi di una Chiave Estesa

Per comprendere meglio la struttura interna di una chiave estesa, prendiamo una come esempio e analizziamola. Ecco una chiave estesa:

- **In Base58**:

```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```

- **In esadecimale**:

```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```

Questa chiave estesa si suddivide in diversi elementi distinti:

1. **Versione**: `0488B21E`

I primi 4 byte sono la versione. Qui, corrisponde a una chiave pubblica estesa sul Mainnet con uno scopo di derivazione *Legacy* o *SegWit v1*.

2. **Profondità**: `03`

Questo campo indica il livello gerarchico della chiave all'interno del portafoglio HD. In questo caso, una profondità di `03` significa che questa chiave è tre livelli di derivazione sotto la chiave principale.

3. **Impronta del genitore**: `6D5601AD`
Questi sono i primi 4 byte dell'hash HASH160 della chiave pubblica genitore che è stata utilizzata per derivare questo `xpub`.
4. **Numero di indice**: `80000000`

Questo indice indica la posizione della chiave tra i figli del suo genitore. Il prefisso `0x80` indica che la chiave è derivata in modo protetto (hardened), e poiché il resto è riempito con zeri, indica che questa chiave è la prima tra i suoi possibili fratelli.

5. **Codice catena**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`
6. **Chiave Pubblica**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`
7. **Checksum**: `1F067C3A`

Il checksum corrisponde ai primi 4 byte dell'hash (doppio SHA256) di tutto il resto.

In questo capitolo, abbiamo scoperto che esistono due tipi differenti di chiavi figlie. Abbiamo anche appreso che la derivazione di queste chiavi figlie richiede una chiave (sia privata che pubblica) e il suo codice catena. Nel prossimo capitolo, esamineremo in dettaglio la natura di questi diversi tipi di chiavi e come derivarle dalla chiave genitore e dal codice catena.

## Derivazione delle Coppie di Chiavi Figlie
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

La derivazione delle coppie di chiavi figlie nei portafogli Bitcoin HD si basa su una struttura gerarchica che consente di generare un grande numero di chiavi, organizzando queste coppie in diversi gruppi attraverso i rami. Ogni coppia figlia derivata da una coppia genitore può essere utilizzata direttamente in uno *scriptPubKey* per bloccare i bitcoin, o come punto di partenza per generare ulteriori chiavi figlie, e così via, per creare un albero di chiavi.

Tutte queste derivazioni iniziano con la chiave maestra e il codice catena maestro, che sono i primi genitori al livello di profondità 0. Sono, in un certo senso, l'Adamo e l'Eva delle chiavi del tuo portafoglio, antenati comuni di tutte le chiavi derivate.

![CYP201](assets/fr/048.webp)

Esploriamo come funziona questa derivazione deterministica.

### I Diversi Tipi di Derivazioni di Chiavi Figlie

Come abbiamo brevemente accennato nel capitolo precedente: le chiavi figlie sono divise in due tipi principali:
1. **Chiavi figlie normali** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Queste sono derivate dalla chiave pubblica estesa ($K_{\text{PAR}}$), o dalla chiave privata estesa ($k_{\text{PAR}}$), derivando prima la chiave pubblica.
2. **Chiavi figlie protette** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Queste possono essere derivate solo dalla chiave privata estesa ($k_{\text{PAR}}$) e sono quindi invisibili agli osservatori che hanno solo la chiave pubblica estesa.
Ogni coppia di chiavi figlio è identificata da un **indice** a 32 bit (denominato $i$ nei nostri calcoli). Gli indici per le chiavi normali variano da $0$ a $2^{31}-1$, mentre quelli per le chiavi potenziate (hardened) variano da $2^{31}$ a $2^{32}-1$. Questi numeri sono utilizzati per distinguere le coppie di chiavi fratello durante la derivazione. Infatti, ogni coppia di chiavi genitore deve essere in grado di derivare più coppie di chiavi figlio. Se applicassimo lo stesso calcolo sistematicamente dalle chiavi genitore, tutte le chiavi fratello ottenute sarebbero identiche, il che non è desiderabile. L'indice introduce quindi una variabile che modifica il calcolo di derivazione, permettendo di differenziare ogni coppia di chiavi fratello. Eccetto per l'uso specifico in certi protocolli e standard di derivazione, generalmente iniziamo derivando la prima chiave figlio con l'indice `0`, la seconda con l'indice `1`, e così via.
### Processo di Derivazione con HMAC-SHA512

La derivazione di ogni chiave figlio si basa sulla funzione HMAC-SHA512, di cui abbiamo discusso nella Sezione 2 sulle funzioni hash. Prende due input: il codice catena genitore $C_{\text{PAR}}$ e la concatenazione della chiave genitore (sia la chiave pubblica $K_{\text{PAR}}$ che la chiave privata $k_{\text{PAR}}$, a seconda del tipo di chiave figlio desiderata) e l'indice. L'output dell'HMAC-SHA512 è una sequenza di 512 bit, divisa in due parti:
- **I primi 32 byte** (o $h_1$) sono utilizzati per calcolare la nuova coppia di chiavi figlio.
- **Gli ultimi 32 byte** (o $h_2$) servono come nuovo codice catena $C_{\text{CHD}}$ per la coppia di chiavi figlio.

In tutti i nostri calcoli, denoterò $\text{hash}$ l'output della funzione HMAC-SHA512.

![CYP201](assets/fr/049.webp)

#### Derivazione di una Chiave Privata Figlio da una Chiave Privata Genitore

Per derivare una chiave privata figlio $k_{\text{CHD}}$ da una chiave privata genitore $k_{\text{PAR}}$, sono possibili due scenari a seconda che si desideri una chiave normale o potenziata.

Per una **chiave figlio normale** ($i < 2^{31}$), il calcolo di $\text{hash}$ è il seguente:


$$

\text{hash} = \text{HMAC-SHA512}(C*{\text{PAR}}, G \cdot k*{\text{PAR}} \Vert i)

$$
In questo calcolo, osserviamo che la nostra funzione HMAC prende due input: prima, il codice catena genitore, e poi la concatenazione dell'indice con la chiave pubblica associata alla chiave privata genitore. La chiave pubblica genitore è utilizzata qui perché stiamo cercando di derivare una chiave figlio normale, non una potenziata.
Ora abbiamo un $\text{hash}$ di 64 byte che divideremo in 2 parti da 32 byte ciascuna: $h_1$ e $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h*1 = \text{hash}*{[:32]} \quad, \quad h*2 = \text{hash}*{[32:]}

$$

La chiave privata figlio $k_{\text{CHD}}^n$ è quindi calcolata come segue:


$$

k*{\text{CHD}}^n = \text{parse256}(h_1) + k*{\text{PAR}} \mod n

$$
In questa calcolazione, l'operazione $\text{parse256}(h_1)$ consiste nell'interpretare i primi 32 byte dell'$\text{hash}$ come un intero a 256 bit. Questo numero viene poi sommato alla chiave privata genitore, il tutto preso modulo $n$ per rimanere nell'ordine della curva ellittica, come abbiamo visto nella sezione 3 sulle firme digitali. Pertanto, per derivare una chiave privata figlio normale, sebbene la chiave pubblica genitore sia utilizzata come base per il calcolo negli input della funzione HMAC-SHA512, è sempre necessario avere la chiave privata genitore per finalizzare il calcolo.
Da questa chiave privata figlio, è possibile derivare la corrispondente chiave pubblica applicando ECDSA o Schnorr. In questo modo, otteniamo una coppia completa di chiavi.

Quindi, la seconda parte dell'$\text{hash}$ è semplicemente interpretata come il codice catena per la coppia di chiavi figlio che abbiamo appena derivato:


$$

C\_{\text{CHD}} = h_2

$$

Ecco una rappresentazione schematica della derivazione complessiva:

![CYP201](assets/fr/050.webp)

Per una **chiave figlio rinforzata** ($i \geq 2^{31}$), il calcolo dell'$\text{hash}$ è il seguente:


$$

hash = \text{HMAC-SHA512}(C*{\text{PAR}}, 0x00 \Vert k*{\text{PAR}} \Vert i)

$$

In questa calcolazione, osserviamo che la nostra funzione HMAC prende due input: primo, il codice catena genitore, e poi la concatenazione dell'indice con la chiave privata genitore. La chiave privata genitore è utilizzata qui perché stiamo cercando di derivare una chiave figlio rinforzata. Inoltre, un byte pari a `0x00` viene aggiunto all'inizio della chiave. Questa operazione ne eguaglia la lunghezza per farla corrispondere a quella di una chiave pubblica compressa.
Quindi, ora abbiamo un $\text{hash}$ di 64 byte che divideremo in 2 parti da 32 byte ciascuna: $h_1$ e $h_2$:
$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

La chiave privata figlio $k_{\text{CHD}}^h$ viene quindi calcolata come segue:


$$

k*{\text{CHD}}^h = \text{parse256}(h_1) + k*{\text{PAR}} \mod n

$$

Successivamente, interpretiamo semplicemente la seconda parte dell'$\text{hash}$ come il codice catena per la coppia di chiavi figlio che abbiamo appena derivato:


$$

C\_{\text{CHD}} = h_2

$$

Ecco una rappresentazione schematica della derivazione complessiva:

![CYP201](assets/fr/051.webp)

Possiamo vedere che la derivazione normale e quella rinforzata funzionano allo stesso modo, con questa differenza: la derivazione normale utilizza la chiave pubblica genitore come input alla funzione HMAC, mentre la derivazione rinforzata utilizza la chiave privata genitore.

#### Derivare una chiave pubblica figlio da una chiave pubblica genitore
Se conosciamo solo la chiave pubblica genitore $K_{\text{PAR}}$ e il codice catena associato $C_{\text{PAR}}$, ovvero una chiave pubblica estesa, è possibile derivare le chiavi pubbliche figlio $K_{\text{CHD}}^n$, ma solo per le chiavi figlio normali (non rinforzate). Questo principio permette notevolmente di monitorare i movimenti di un account in un portafoglio Bitcoin dall'`xpub` (*solo visualizzazione*).
Per eseguire questo calcolo, calcoleremo l'$\text{hash}$ con un indice $i < 2^{31}$ (derivazione normale):


$$

\text{hash} = \text{HMAC-SHA512}(C*{\text{PAR}}, K*{\text{PAR}} \Vert i)

$$

In questo calcolo, osserviamo che la nostra funzione HMAC prende due input: prima il codice catena genitore, poi la concatenazione dell'indice con la chiave pubblica genitore.

Quindi, ora abbiamo un $hash$ di 64 byte che divideremo in 2 parti da 32 byte ciascuna: $h_1$ e $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

La chiave pubblica figlio $K_{\text{CHD}}^n$ viene quindi calcolata come segue:


$$

K*{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K*{\text{PAR}}

$$
Se $\text{parse256}(h_1) \geq n$ (ordine della curva ellittica) o se $K_{\text{CHD}}^n$ è il punto all'infinito, la derivazione è invalida e deve essere scelto un altro indice.
In questo calcolo, l'operazione $\text{parse256}(h_1)$ implica l'interpretazione dei primi 32 byte dell'$\text{hash}$ come un intero a 256 bit. Questo numero è utilizzato per calcolare un punto sulla curva ellittica attraverso l'addizione e il raddoppio dal punto generatore $G$. Questo punto viene poi aggiunto alla chiave pubblica genitore per ottenere la chiave pubblica figlio normale. Quindi, per derivare una chiave pubblica figlio normale, sono necessari solo la chiave pubblica genitore e il codice catena genitore; la chiave privata genitore non entra mai in questo processo, a differenza del calcolo della chiave privata figlio che abbiamo visto in precedenza.

Successivamente, il codice catena figlio è semplicemente:


$$

C\_{\text{CHD}} = h_2

$$

Ecco una rappresentazione schematica della derivazione complessiva:

![CYP201](assets/fr/052.webp)

### Corrispondenza tra chiavi pubbliche e private figlio

Una domanda che può sorgere è come una chiave pubblica figlio normale derivata da una chiave pubblica genitore possa corrispondere a una chiave privata figlio normale derivata dalla corrispondente chiave privata genitore. Questo collegamento è precisamente garantito dalle proprietà delle curve ellittiche. Infatti, per derivare una chiave pubblica figlio normale, l'HMAC-SHA512 viene applicato nello stesso modo, ma il suo output viene utilizzato diversamente:
   - **Chiave privata figlio normale**: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
   - **Chiave pubblica figlio normale**: $K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}$
Grazie alle operazioni di addizione e raddoppio sulla curva ellittica, entrambi i metodi producono risultati consistenti: la chiave pubblica derivata dalla chiave privata figlia è identica alla chiave pubblica figlia derivata direttamente dalla chiave pubblica genitore.

### Riassunto dei tipi di derivazione

Per riassumere, ecco i diversi possibili tipi di derivazioni:


$$

\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k*{\text{PAR}} \rightarrow k*{\text{CHD}} & k*{\text{PAR}} & \{ k*{\text{CHD}}^n, k\_{\text{CHD}}^h \} & \{ n, h \} \\
\end{array}

$$
$$

k*{\text{PAR}} \rightarrow K*{\text{CHD}} & k*{\text{PAR}} & \{ K*{\text{CHD}}^n, K*{\text{CHD}}^h \} & \{ n, h \} \\
K*{\text{PAR}} \rightarrow k*{\text{CHD}} & K*{\text{PAR}} & \times & \times \\
K*{\text{PAR}} \rightarrow K*{\text{CHD}} & K*{\text{PAR}} & K*{\text{CHD}}^n & n \\
\hline
\end{array}

$$

Per riassumere, finora hai imparato a creare gli elementi base del portafoglio HD: la frase mnemonica, il seme e poi la chiave principale e il codice catena principale. Hai anche scoperto come derivare coppie di chiavi figlie in questo capitolo. Nel prossimo capitolo, esploreremo come queste derivazioni sono organizzate nei portafogli Bitcoin e quale struttura seguire per ottenere concretamente gli indirizzi di ricezione così come le coppie di chiavi utilizzate nello *scriptPubKey* e nello *scriptSig*.

## Struttura del Portafoglio e Percorsi di Derivazione
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

La struttura gerarchica dei portafogli HD su Bitcoin consente l'organizzazione delle coppie di chiavi in vari modi. L'idea è derivare, dalla chiave privata principale e dal codice catena principale, diversi livelli di profondità. Ogni livello aggiunto corrisponde alla derivazione di una coppia di chiavi figlia da una coppia di chiavi genitore.

Nel tempo, diversi BIP hanno introdotto standard per questi percorsi di derivazione, con l'obiettivo di standardizzare il loro uso attraverso diversi software. Quindi, in questo capitolo, scopriremo il significato di ogni livello di derivazione nei portafogli HD, secondo questi standard.

### I Livelli di Derivazione di un Portafoglio HD

I percorsi di derivazione sono organizzati in strati di profondità, che vanno dalla profondità 0, che rappresenta la chiave principale e il codice catena principale, a strati di sottolivelli per derivare gli indirizzi utilizzati per bloccare gli UTXO. I BIP (*Proposte di Miglioramento di Bitcoin*) definiscono gli standard per ogni strato, il che aiuta ad armonizzare le pratiche attraverso diversi software di gestione dei portafogli.

Un percorso di derivazione, quindi, si riferisce alla sequenza di indici utilizzati per derivare le chiavi figlie da una chiave principale.

**Profondità 0: Chiave Principale (BIP32)**

Questa profondità corrisponde alla chiave privata principale del portafoglio e al codice catena principale. È rappresentata dalla notazione $m/$.

**Profondità 1: Scopo (BIP43)**
L'obiettivo determina la struttura logica di derivazione. Ad esempio, un indirizzo P2WPKH avrà $/84'/$ a profondità 1 (secondo BIP84), mentre un indirizzo P2TR avrà $/86'/$ (secondo BIP86). Questo strato facilita la compatibilità tra portafogli indicando numeri di indice corrispondenti ai numeri BIP.

In altre parole, una volta che si ha la chiave maestra e il codice catena maestro, questi servono come coppia di chiavi genitore per derivare una coppia di chiavi figlio. L'indice usato in questa derivazione può essere, ad esempio, $/84'/$ se il portafoglio è inteso per usare script di tipo SegWit v0. Questa coppia di chiavi è quindi a profondità 1. Il suo ruolo non è bloccare bitcoin, ma semplicemente servire come punto di passaggio nella gerarchia di derivazione.

**Profondità 2: Tipo di Valuta (BIP44)**

Dalla coppia di chiavi a profondità 1, viene eseguita una nuova derivazione per ottenere la coppia di chiavi a profondità 2. Questa profondità permette di differenziare i conti Bitcoin da altre criptovalute all'interno dello stesso portafoglio.

Ogni valuta ha un indice unico per garantire la compatibilità tra portafogli multi-valuta. Ad esempio, per Bitcoin, l'indice è $/0'/$ (o `0x80000000` in notazione esadecimale). Gli indici delle valute sono scelti nell'intervallo da $2^{31}$ a $2^{32}-1$ per garantire una derivazione rinforzata.

Per darvi altri esempi, ecco gli indici di alcune valute:
- $1'$ (`0x80000001`) per i bitcoin di testnet;
- $2'$ (`0x80000002`) per Litecoin;
- $60'$ (`0x8000003c`) per Ethereum...

**Profondità 3: Account (BIP32)**

Ogni portafoglio può essere diviso in diversi account, numerati da $2^{31}$, e rappresentati a profondità 3 da $/0'/$ per il primo account, $/1'/$ per il secondo, e così via. Generalmente, quando si fa riferimento a una chiave estesa `xpub`, si riferisce a chiavi a questa profondità di derivazione.

Questa separazione in diversi account è opzionale. Ha lo scopo di semplificare l'organizzazione del portafoglio per gli utenti. In pratica, spesso si usa solo un account, di solito il primo per impostazione predefinita. Tuttavia, in alcuni casi, se si desidera distinguere chiaramente coppie di chiavi per usi diversi, ciò può essere utile. Ad esempio, è possibile creare un account personale e un account professionale dallo stesso seme, con gruppi di chiavi completamente distinti da questa profondità di derivazione.

**Profondità 4: Catena (BIP32)**
Ogni account definito a profondità 3 è poi strutturato in due catene:
- **La catena esterna**: In questa catena, vengono derivate quelle che sono note come indirizzi "pubblici". Questi indirizzi di ricezione sono destinati a bloccare UTXO provenienti da transazioni esterne (cioè, originati dal consumo di UTXO che non appartengono a te). Per dirla semplicemente, questa catena esterna viene utilizzata ogni volta che si desidera ricevere bitcoin. Quando si clicca su "*ricevi*" nel software del portafoglio, è sempre un indirizzo della catena esterna che viene offerto.
- **La catena interna (resto)**: Questa catena è riservata per gli indirizzi di ricezione che bloccano bitcoin provenienti dal consumo di UTXO che ti appartengono, in altre parole, indirizzi di resto. È identificata dall'indice $/1/$.

**Profondità 5: Indice degli Indirizzi (BIP32)**
Infine, il livello 5 rappresenta l'ultimo passo della derivazione nel portafoglio. Sebbene tecnicamente sia possibile continuare all'infinito, gli standard attuali si fermano qui. A questa profondità finale, vengono derivati le coppie di chiavi che saranno effettivamente utilizzate per bloccare e sbloccare gli UTXO. Ogni indice permette di distinguere tra coppie di chiavi fratelli: quindi, il primo indirizzo di ricezione utilizzerà l'indice $/0/$, il secondo l'indice $/1/$, e così via.
![CYP201](assets/fr/053.webp)

### Notazione dei Percorsi di Derivazione

Il percorso di derivazione è scritto separando ogni livello con una barra ($/$). Ogni barra indica quindi una derivazione di una coppia di chiavi genitore ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) in una coppia di chiavi figlio ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$). Il numero indicato ad ogni profondità corrisponde all'indice utilizzato per derivare questa chiave dai suoi genitori. L'apostrofo ($'$) talvolta posto alla destra dell'indice indica una derivazione rinforzata ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Talvolta, questo apostrofo è sostituito da una $h$. In assenza di un apostrofo o di una $h$, si tratta quindi di una derivazione normale ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).
Come abbiamo visto nei capitoli precedenti, gli indici delle chiavi rinforzate partono da $2^{31}$, o `0x80000000` in esadecimale. Pertanto, quando un indice è seguito da un apostrofo in un percorso di derivazione, a $2^{31}$ deve essere aggiunto il numero indicato per ottenere il valore effettivo utilizzato nella funzione HMAC-SHA512. Ad esempio, se il percorso di derivazione specifica $/44'/$, l'indice effettivo sarà:
$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$

In esadecimale, questo è `0x8000002C`.

Ora che abbiamo compreso i principi principali dei percorsi di derivazione, prendiamo un esempio! Ecco il percorso di derivazione per un indirizzo Bitcoin di ricezione:


$$

m / 84' / 0' / 1' / 0 / 7

$$

In questo esempio:
- $84'$ indica lo standard P2WPKH (SegWit v0);
- $0'$ indica la valuta Bitcoin sulla rete principale;
- $1'$ corrisponde al secondo account nel portafoglio;
- $0$ indica che l'indirizzo si trova sulla catena esterna;
- $7$ indica l'8° indirizzo esterno di questo account.

### Riassunto della struttura di derivazione

| Profondità | Descrizione        | Esempio Standard                  |
| ---------- | ------------------ | --------------------------------- |
| 0          | Chiave Maestra     | $m/$                              |
| 1          | Scopo              | $/86'/$ (P2TR)                    |
| 2          | Valuta             | $/0'/$ (Bitcoin)                  |
| 3          | Account            | $/0'/$ (Primo account)            |
| 4          | Catena             | $/0/$ (esterna) o $/1/$ (di cambio)|
| 5          | Indice Indirizzo   | $/0/$ (primo indirizzo)           |
Nel prossimo capitolo, scopriremo cosa sono i "*descrittori degli script di output*", una novità recentemente introdotta in Bitcoin Core che semplifica il backup di un portafoglio Bitcoin.
## Descrittori degli script di output
<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>
Spesso ci viene detto che la frase mnemonica da sola è sufficiente per recuperare l'accesso a un portafoglio. In realtà, le cose sono un po' più complesse. Nel capitolo precedente, abbiamo esaminato la struttura di derivazione del portafoglio HD, e potreste aver notato che questo processo è piuttosto complesso. I percorsi di derivazione indicano al software quale direzione seguire per derivare le chiavi dell'utente. Tuttavia, quando si recupera un portafoglio Bitcoin, se non si conoscono questi percorsi, la frase mnemonica da sola non è sufficiente. Permette di ottenere la chiave principale e il codice catena principale, ma è poi necessario conoscere gli indici usati per raggiungere le chiavi figlie.

Teoricamente, sarebbe necessario salvare non solo la frase mnemonica del nostro portafoglio, ma anche i percorsi agli account che usiamo. In pratica, spesso è possibile riguadagnare l'accesso alle chiavi figlie senza queste informazioni, a patto che siano stati seguiti gli standard. Testando ogni standard uno per uno, generalmente è possibile riguadagnare l'accesso ai bitcoin. Tuttavia, ciò non è garantito ed è particolarmente complicato per i principianti. Inoltre, con la diversificazione dei tipi di script e l'emergere di configurazioni più complesse, queste informazioni potrebbero diventare difficili da estrapolare, trasformando così questi dati in informazioni private e difficili da recuperare con la forza bruta. Ecco perché è stata recentemente introdotta un'innovazione e sta iniziando ad essere integrata nel vostro software di portafoglio preferito: i *descrittori degli script di output*.

### Cos'è un "descrittore"?

I "*descrittori degli script di output*", o semplicemente "*descrittori*", sono espressioni strutturate che descrivono completamente uno script di output (*scriptPubKey*) e forniscono tutte le informazioni necessarie per seguire le transazioni associate a uno script particolare. Facilitano la gestione delle chiavi nei portafogli HD offrendo una descrizione standardizzata e completa della struttura del portafoglio e dei tipi di indirizzi utilizzati.

Il principale vantaggio dei descrittori risiede nella loro capacità di incapsulare tutte le informazioni essenziali per ripristinare un portafoglio in una singola stringa (in aggiunta alla frase di recupero). Salvando un descrittore con le frasi mnemoniche associate, diventa possibile ripristinare le chiavi private conoscendo esattamente la loro posizione nella gerarchia. Per i portafogli multisig, il cui backup era inizialmente più complesso, il descrittore include l'`xpub` di ogni fattore, garantendo così la possibilità di rigenerare gli indirizzi in caso di problema.

### Costruzione di un descrittore

Un descrittore è composto da diversi elementi:
* Funzioni di script come `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Multifirma*), e `sortedmulti` (*Multifirma con chiavi ordinate*);
* Percorsi di derivazione, ad esempio, `[d34db33f/44h/0h/0h]` che indica un percorso di account derivato e un'impronta digitale della chiave principale specifica;
* Chiavi in vari formati come chiavi pubbliche esadecimali o chiavi pubbliche estese (`xpub`);
* Un checksum, preceduto da un segno di cancelletto, per verificare l'integrità del descrittore.
Ad esempio, un descrittore per un portafoglio P2WPKH (SegWit v0) potrebbe apparire così:
```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```

In questo descrittore, la funzione di derivazione `wpkh` indica un tipo di script *Pay-to-Witness-Public-Key-Hash*. È seguito dal percorso di derivazione che contiene:
* `cdeab12f`: l'impronta della chiave principale;
* `84h`: che indica l'uso di uno scopo BIP84, destinato agli indirizzi SegWit v0;
* `0h`: che indica che si tratta di una valuta BTC sulla rete principale;
* `0h`: che si riferisce al numero di conto specifico utilizzato nel portafoglio.

Il descrittore include anche la chiave pubblica estesa utilizzata in questo portafoglio:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Successivamente, la notazione `/<0;1>/*` specifica che il descrittore può generare indirizzi dalla catena esterna (`0`) e dalla catena interna (`1`), con un carattere jolly (`*`) che consente la derivazione sequenziale di più indirizzi in modo configurabile, simile alla gestione di un "limite di gap" sui software di portafoglio tradizionali.
Infine, `#jy0l7nr4` rappresenta il checksum per verificare l'integrità del descrittore.
Ora conosci tutto sul funzionamento del portafoglio HD su Bitcoin e il processo di derivazione delle coppie di chiavi. Tuttavia, negli ultimi capitoli, ci siamo limitati alla generazione di chiavi private e pubbliche, senza affrontare la costruzione degli indirizzi di ricezione. Questo sarà precisamente l'argomento del prossimo capitolo!

## Indirizzi di Ricezione
<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>

Gli indirizzi di ricezione sono informazioni incorporate in *scriptPubKey* per bloccare gli UTXO appena creati. Semplicemente, un indirizzo serve a ricevere bitcoin. Esploriamo il loro funzionamento in connessione con quanto abbiamo studiato nei capitoli precedenti.

### Il Ruolo degli Indirizzi Bitcoin negli Script

Come spiegato in precedenza, il ruolo di una transazione è trasferire la proprietà dei bitcoin dagli input agli output. Questo processo coinvolge il consumo di UTXO come input mentre crea nuovi UTXO come output. Questi UTXO sono protetti da script, che definiscono le condizioni necessarie per sbloccare i fondi.
Quando un utente riceve bitcoin, il mittente crea un output UTXO e lo blocca con uno *scriptPubKey*. Questo script contiene le regole che specificano tipicamente le firme e le chiavi pubbliche richieste per sbloccare questo UTXO. Per spendere questo UTXO in una nuova transazione, l'utente deve fornire le informazioni richieste tramite uno *scriptSig*. L'esecuzione di *scriptSig* in combinazione con *scriptPubKey* deve restituire "vero" o `1`. Se questa condizione è soddisfatta, l'UTXO può essere speso per creare un nuovo UTXO, a sua volta bloccato da un nuovo *scriptPubKey*, e così via.
![CYP201](assets/fr/054.webp)

È precisamente nello *scriptPubKey* che si trovano gli indirizzi di ricezione. Tuttavia, il loro utilizzo varia a seconda dello standard di script adottato. Ecco una tabella riassuntiva delle informazioni contenute nello *scriptPubKey* secondo lo standard utilizzato, così come le informazioni attese nello *scriptSig* per sbloccare lo *scriptPubKey*.

| Standard           | *scriptPubKey*                                              | *scriptSig*                     | *script di riscatto* | *testimone*                              |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | -------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<firma>`                       |                      |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<firma> <chiave pubblica>`     |                      |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<spinte di dati> <script di riscatto>` | Dati arbitrari     |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                      | `<firma> <chiave pubblica>`              |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                      | `<spinte di dati> <script testimone>`    |
| P2SH-P2WPKH        | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<script di riscatto>`          | `0 <pubKeyHash>`    | `<firma> <chiave pubblica>`              |
| P2SH-P2WSH         | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<script di riscatto>`          | `0 <scriptHash>`    | `<spinte di dati> <script testimone>`    |
| P2TR (percorso chiave)    | `1 <chiave pubblica>`                                    |                                 |                      | `<firma>`                                |
| P2TR (percorso script) | `1 <chiave pubblica>`                                    |                                 |                      | `<spinte di dati> <script> <blocco di controllo>` |

*Fonte: Bitcoin Core PR review club, 7 luglio 2021 - Gloria Zhao*

Gli opcode utilizzati in uno script sono progettati per manipolare le informazioni e, se necessario, per confrontarle o testarle. Prendiamo l'esempio di uno script P2PKH, che è il seguente:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Come vedremo in questo capitolo, `<pubKeyHash>` rappresenta effettivamente il payload dell'indirizzo di ricezione utilizzato per bloccare l'UTXO. Per sbloccare questo *scriptPubKey*, è necessario fornire uno *scriptSig* contenente:

```text
<firma> <chiave pubblica>
```
Nel linguaggio degli script, lo "stack" è una struttura dati "*LIFO*" ("*Last In, First Out*") utilizzata per memorizzare temporaneamente elementi durante l'esecuzione di uno script. Ogni operazione dello script manipola questo stack, dove gli elementi possono essere aggiunti (*push*) o rimossi (*pop*). Gli script utilizzano questi stack per valutare espressioni, memorizzare variabili temporanee e gestire condizioni.
L'esecuzione dello script che ho appena fornito come esempio segue questo processo:

- Abbiamo lo *scriptSig*, lo *ScriptPubKey* e lo stack:

![CYP201](assets/fr/055.webp)

- Lo *scriptSig* viene inserito nello stack:

![CYP201](assets/fr/056.webp)

- `OP_DUP` duplica la chiave pubblica fornita nello *scriptSig* sullo stack:

![CYP201](assets/fr/057.webp)

- `OP_HASH160` restituisce l'hash della chiave pubblica appena duplicata:

![CYP201](assets/fr/058.webp)

- `OP_PUSHBYTES_20 <pubKeyHash>` inserisce l'indirizzo Bitcoin contenuto nello *scriptPubKey* sullo stack:

![CYP201](assets/fr/059.webp)

- `OP_EQUALVERIFY` verifica che la chiave pubblica hashata corrisponda all'indirizzo di ricezione fornito:

![CYP201](assets/fr/060.webp)
`OP_CHECKSIG` controlla la firma contenuta nello *scriptSig* utilizzando la chiave pubblica. Questo opcode esegue essenzialmente una verifica della firma come descritto nella parte 3 di questa formazione:
![CYP201](assets/fr/061.webp)

- Se `1` rimane sullo stack, allora lo script è valido:

![CYP201](assets/fr/062.webp)

Pertanto, per riassumere, questo script consente di verificare, con l'aiuto della firma digitale, che l'utente che rivendica la proprietà di questo UTXO e desidera spenderlo possiede effettivamente la chiave privata associata all'indirizzo di ricezione utilizzato durante la creazione di questo UTXO.

### I diversi tipi di indirizzi Bitcoin

Nell'evoluzione di Bitcoin, sono stati aggiunti diversi modelli di script standard. Ognuno di essi utilizza un tipo distinto di indirizzo di ricezione. Ecco una panoramica dei principali modelli di script disponibili fino ad oggi:

**P2PK (*Pay-to-PubKey*)**:

Questo modello di script è stato introdotto nella prima versione di Bitcoin da Satoshi Nakamoto. Lo script P2PK blocca i bitcoin direttamente utilizzando una chiave pubblica grezza (quindi, nessun indirizzo di ricezione viene utilizzato con questo modello). La sua struttura è semplice: contiene una chiave pubblica e richiede una firma digitale corrispondente per sbloccare i fondi. Questo script fa parte dello standard "*Legacy*".

**P2PKH (*Pay-to-PubKey-Hash*)**:

Come il P2PK, lo script P2PKH è stato introdotto al lancio di Bitcoin. A differenza del suo predecessore, blocca i bitcoin utilizzando l'hash della chiave pubblica, piuttosto che utilizzare direttamente la chiave pubblica grezza. Lo *scriptSig* deve quindi fornire la chiave pubblica associata all'indirizzo di ricezione, così come una firma valida. Gli indirizzi corrispondenti a questo modello iniziano con `1` e sono codificati in *base58check*. Anche questo script appartiene allo standard "*Legacy*".

**P2SH (*Pay-to-Script-Hash*)**:
Introdotta nel 2012 con il BIP16, il modello P2SH permette l'uso dell'hash di uno script arbitrario nel *scriptPubKey*. Questo script hashato, chiamato "*redeemScript*", contiene le condizioni per sbloccare i fondi. Per spendere un UTXO bloccato con P2SH, è necessario fornire uno *scriptSig* contenente l'originale *redeemScript* così come i dati necessari per validarla. Questo modello è notevolmente utilizzato per vecchi multisig. Gli indirizzi associati a P2SH iniziano con `3` e sono codificati in *base58check*. Questo script appartiene anche allo standard "*Legacy*".
**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:
Questo script è simile al P2PKH, poiché anch'esso blocca i bitcoin utilizzando l'hash di una chiave pubblica. Tuttavia, a differenza del P2PKH, lo *scriptSig* è spostato in una sezione separata chiamata "*Witness*". Questo è talvolta riferito come "*scriptWitness*" per denotare l'insieme comprendente la firma e la chiave pubblica. Ogni input SegWit ha il proprio *scriptWitness*, e la collezione di *scriptWitnesses* costituisce il campo *Witness* della transazione. Questo spostamento dei dati della firma è un'innovazione introdotta dall'aggiornamento SegWit, mirata particolarmente a prevenire la malleabilità delle transazioni a causa delle firme ECDSA.
Gli indirizzi P2WPKH usano la codifica *bech32* e iniziano sempre con `bc1q`. Questo tipo di script corrisponde agli output SegWit versione 0.

**P2WSH (*Pay-to-Witness-Script-Hash*)**:

Il modello P2WSH è stato introdotto anch'esso con l'aggiornamento SegWit nell'agosto 2017. Simile al modello P2SH, blocca i bitcoin utilizzando l'hash di uno script. La principale differenza risiede in come firme e script sono incorporati nella transazione. Per spendere bitcoin bloccati con questo tipo di script, il destinatario deve fornire lo script originale, chiamato *witnessScript* (equivalente a *redeemScript* in P2SH), insieme ai dati necessari per validare questo *witnessScript*. Questo meccanismo permette l'implementazione di condizioni di spesa più complesse, come i multisig.

Gli indirizzi P2WSH usano la codifica *bech32* e iniziano sempre con `bc1q`. Questo script corrisponde anche agli output SegWit versione 0.

**P2TR (*Pay-to-Taproot*)**:

Il modello P2TR è stato introdotto con l'implementazione di Taproot nel novembre 2021. Si basa sul protocollo Schnorr per l'aggregazione delle chiavi crittografiche, così come su un albero di Merkle per script alternativi, chiamato MAST (*Merkelized Alternative Script Tree*). A differenza di altri tipi di script, dove le condizioni di spesa sono esposte pubblicamente (sia alla ricezione che alla spesa), P2TR permette di nascondere script complessi dietro a una singola, apparente chiave pubblica.

Tecnicamente, uno script P2TR blocca i bitcoin su una unica chiave pubblica Schnorr, denotata come $Q$. Questa chiave $Q$ è in realtà un aggregato di una chiave pubblica $P$ e una chiave pubblica $M$, quest'ultima calcolata dalla radice di Merkle di una lista di *scriptPubKey*. I bitcoin bloccati con questo tipo di script possono essere spesi in due modi:
- Pubblicando una firma per la chiave pubblica $P$ (*key path*).
- Soddisfacendo uno degli script contenuti nell'albero di Merkle (*script path*).
P2TR offre quindi grande flessibilità, poiché consente di bloccare bitcoin sia con una chiave pubblica unica, sia con diversi script a scelta, o entrambi simultaneamente. Il vantaggio di questa struttura ad albero di Merkle è che solo lo script di spesa utilizzato viene rivelato durante la transazione, ma tutti gli altri script alternativi rimangono segreti.

P2TR corrisponde agli output di versione 1 di SegWit, il che significa che le firme per gli input P2TR sono memorizzate nella sezione *Witness* della transazione, e non nello *scriptSig*. Gli indirizzi P2TR utilizzano la codifica *bech32m* e iniziano con `bc1p`, ma sono piuttosto unici perché non utilizzano una funzione hash per la loro costruzione. Infatti, rappresentano direttamente la chiave pubblica $Q$ che è semplicemente formattata con metadati. È, quindi, un modello di script vicino a P2PK.

Ora che abbiamo coperto la teoria, passiamo alla pratica! Nel capitolo seguente, propongo di derivare sia un indirizzo SegWit v0 che un indirizzo SegWit v1 da una coppia di chiavi.

## Derivazione dell'Indirizzo
<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>

Esploriamo insieme come generare un indirizzo di ricezione da una coppia di chiavi situate, ad esempio, alla profondità 5 di un portafoglio HD. Questo indirizzo può poi essere utilizzato in un software di portafoglio per bloccare un UTXO.

Poiché il processo di generazione di un indirizzo dipende dal modello di script adottato, concentriamoci su due casi specifici: generare un indirizzo SegWit v0 in P2WPKH e un indirizzo SegWit v1 in P2TR. Questi due tipi di indirizzi coprono la stragrande maggioranza degli usi oggi.

### Compressione della Chiave Pubblica

Dopo aver eseguito tutti i passaggi di derivazione dalla chiave maestra alla profondità 5 utilizzando gli indici appropriati, otteniamo una coppia di chiavi ($k$, $K$) con $K = k \cdot G$. Anche se è possibile utilizzare questa chiave pubblica così com'è per bloccare fondi con lo standard P2PK, questo non è il nostro obiettivo qui. Invece, miriamo a creare un indirizzo in P2WPKH in prima istanza, e poi in P2TR per un altro esempio.

Il primo passo è comprimere la chiave pubblica $K$. Per comprendere bene questo processo, ricordiamo prima alcuni fondamenti trattati nella parte 3.
Una chiave pubblica su Bitcoin è un punto $K$ situato su una curva ellittica. È rappresentata nella forma $(x, y)$, dove $x$ e $y$ sono le coordinate del punto. Nella sua forma non compressa, questa chiave pubblica misura 520 bit: 8 bit per un prefisso (valore iniziale di `0x04`), 256 bit per la coordinata $x$ e 256 bit per la coordinata $y$.
Tuttavia, le curve ellittiche hanno una proprietà di simmetria rispetto all'asse x: per una data coordinata $x$, ci sono solo due valori possibili per $y$: $y$ e $-y$. Questi due punti si trovano su entrambi i lati dell'asse x. In altre parole, se conosciamo $x$, è sufficiente specificare se $y$ è pari o dispari per identificare il punto esatto sulla curva.
Per comprimere una chiave pubblica, viene codificato solo $x$, che occupa 256 bit, e viene aggiunto un prefisso per specificare la parità di $y$. Questo metodo riduce la dimensione della chiave pubblica a 264 bit invece dei 520 iniziali. Il prefisso `0x02` indica che $y$ è pari, e il prefisso `0x03` indica che $y$ è dispari.
Prendiamo un esempio per capire bene, con una chiave pubblica grezza in rappresentazione non compressa:

```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Se decomponiamo questa chiave, abbiamo:
   - Il prefisso: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`

L'ultimo carattere esadecimale di $y$ è `f`. In base 10, `f = 15`, che corrisponde a un numero dispari. Pertanto, $y$ è dispari, e il prefisso sarà `0x03` per indicarlo.

La chiave pubblica compressa diventa:

```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```
Questa operazione si applica a tutti i modelli di script basati su ECDSA, cioè tutti tranne P2TR che utilizza Schnorr. Nel caso di Schnorr, come spiegato nella parte 3, si conserva solo il valore di $x$, senza aggiungere un prefisso per indicare la parità di $y$, a differenza di ECDSA. Questo è reso possibile dal fatto che una parità unica è arbitrariamente scelta per tutte le chiavi. Ciò consente una leggera riduzione dello spazio di archiviazione richiesto per le chiavi pubbliche.
### Derivazione di un indirizzo SegWit v0 (bech32)

Ora che abbiamo ottenuto la nostra chiave pubblica compressa, possiamo derivare da essa un indirizzo di ricezione SegWit v0.

Il primo passo è applicare la funzione hash HASH160 alla chiave pubblica compressa. HASH160 è una composizione di due funzioni hash successive: SHA256, seguita da RIPEMD160:


$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$

Prima, passiamo la chiave attraverso SHA256:

```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```

Poi passiamo il risultato attraverso RIPEMD160:

```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```
Abbiamo ottenuto un hash a 160 bit della chiave pubblica, che costituisce quello che viene chiamato il payload dell'indirizzo. Questo payload rappresenta la parte centrale e più importante dell'indirizzo. È utilizzato anche nello *scriptPubKey* per bloccare gli UTXO.
Tuttavia, per rendere questo payload più facilmente utilizzabile dagli esseri umani, ad esso vengono aggiunti dei metadati. Il passo successivo prevede la codifica di questo hash in gruppi di 5 bit in decimale. Questa trasformazione decimale sarà utile per la conversione in *bech32*, utilizzato dagli indirizzi post-SegWit. L'hash binario a 160 bit è quindi diviso in 32 gruppi di 5 bit:


$$

\begin{array}{|c|c|}
\hline
\text{Gruppi di 5 bit} & \text{Valore Decimale} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
\end{array}

$$
Quindi, abbiamo:

```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```

Una volta che l'hash è codificato in gruppi di 5 bit, viene aggiunto un checksum all'indirizzo. Questo checksum è utilizzato per verificare che il payload dell'indirizzo non sia stato alterato durante la sua memorizzazione o trasmissione. Ad esempio, permette a un software di portafoglio di assicurarsi che non sia stato commesso un errore di battitura quando si inserisce un indirizzo di ricezione. Senza questa verifica, si potrebbe accidentalmente inviare bitcoin a un indirizzo errato, risultando in una perdita permanente di fondi, poiché non si possiede la chiave pubblica o privata associata. Pertanto, il checksum è una protezione contro gli errori umani.

Per i vecchi indirizzi Bitcoin *Legacy*, il checksum veniva semplicemente calcolato dall'inizio dell'hash dell'indirizzo con la funzione HASH256. Con l'introduzione di SegWit e del formato *bech32*, ora vengono utilizzati i codici BCH (*Bose, Ray-Chaudhuri e Hocquenghem*). Questi codici correttori di errore sono utilizzati per rilevare e correggere errori nelle sequenze di dati. Assicurano che le informazioni trasmesse arrivino intatte a destinazione, anche in caso di alterazioni minori. I codici BCH sono utilizzati in molti campi, come SSD, DVD e codici QR. Ad esempio, grazie a questi codici BCH, un codice QR parzialmente oscurato può comunque essere letto e decodificato.

Nel contesto di Bitcoin, i codici BCH offrono un miglior compromesso tra dimensione e capacità di rilevamento degli errori rispetto alle semplici funzioni hash utilizzate per gli indirizzi *Legacy*. Tuttavia, su Bitcoin, i codici BCH sono utilizzati solo per il rilevamento degli errori, non per la correzione. Pertanto, il software del portafoglio segnalerà un indirizzo di ricezione errato ma non lo correggerà automaticamente. Questa limitazione è deliberata: consentire la correzione automatica ridurrebbe la capacità di rilevamento degli errori.

Per calcolare il checksum con i codici BCH, dobbiamo preparare diversi elementi:
- **La Parte Leggibile dall'Uomo (HRP)**: Per il mainnet di Bitcoin, l'HRP è `bc`;
L'HRP deve essere espanso separando ogni carattere in due parti:
- Prendendo i caratteri dell'HRP in ASCII:
	- `b`: `01100010`
- `c`: `01100011`
- Estraendo i 3 bit più significativi e i 5 bit meno significativi:
  - 3 bit più significativi: `011` (3 in decimale)
  - 3 bit più significativi: `011` (3 in decimale)
  - 5 bit meno significativi: `00010` (2 in decimale)
  - 5 bit meno significativi: `00011` (3 in decimale)

Con il separatore `0` tra i due caratteri, l'estensione dell'HRP è quindi:

```text
03 03 00 02 03
```

- **La versione witness**: Per la versione SegWit 0, è `00`;

- **Il payload**: I valori decimali dell'hash della chiave pubblica;

- **La riserva per il checksum**: Aggiungiamo 6 zeri `[0, 0, 0, 0, 0, 0]` alla fine della sequenza.

Tutti i dati combinati da inserire nel programma per calcolare il checksum sono i seguenti:

```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```

Il calcolo del checksum è piuttosto complesso. Coinvolge l'aritmetica dei campi finiti polinomiali. Non dettaglieremo questo calcolo qui e passeremo direttamente al risultato. Nel nostro esempio, il checksum ottenuto in decimale è:

```text
10 16 11 04 13 18
```

Ora possiamo costruire l'indirizzo di ricezione concatenando in ordine i seguenti elementi:
- **La versione SegWit**: `00`
- **Il payload**: L'hash della chiave pubblica
- **Il checksum**: I valori ottenuti nel passaggio precedente (`10 16 11 04 13 18`)

Questo ci dà in decimale:

```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```

Quindi, ogni valore decimale deve essere mappato al suo carattere *bech32* utilizzando la seguente tabella di conversione:


$$

Per convertire un valore in un carattere _bech32_ utilizzando questa tabella, è sufficiente localizzare i valori nella prima colonna e nella prima riga che, sommati insieme, danno il risultato desiderato. Quindi, recuperare il carattere corrispondente. Ad esempio, il numero decimale `19` verrà convertito nella lettera `n`, perché $19 = 16 + 3$.
Mappando tutti i nostri valori, otteniamo il seguente indirizzo:

```
qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

Tutto ciò che rimane da fare è aggiungere l'HRP `bc`, che indica che si tratta di un indirizzo per il mainnet di Bitcoin, così come il separatore `1`, per ottenere l'indirizzo completo di ricezione:

```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

La particolarità di questo alfabeto _bech32_ è che include tutti i caratteri alfanumerici tranne `1`, `b`, `i` e `o` per evitare confusione visiva tra caratteri simili, specialmente durante la loro digitazione o lettura da parte degli umani.

Per riassumere, ecco il processo di derivazione:

![CYP201](assets/fr/065.webp)

Questo è il modo per derivare un indirizzo di ricezione P2WPKH (SegWit v0) da una coppia di chiavi. Passiamo ora agli indirizzi P2TR (SegWit v1 / Taproot) e scopriamo il loro processo di generazione.

### Derivazione di un Indirizzo SegWit v1 (bech32m)

Per gli indirizzi Taproot, il processo di generazione differisce leggermente. Vediamolo insieme!

Dal passo della compressione della chiave pubblica, appare una prima distinzione rispetto a ECDSA: le chiavi pubbliche utilizzate per Schnorr su Bitcoin sono rappresentate solo dalla loro ascissa ($x$). Pertanto, non c'è prefisso, e la chiave compressa misura esattamente 256 bit.
Come abbiamo visto nel capitolo precedente, uno script P2TR blocca i bitcoin su una unica chiave pubblica Schnorr, designata da $Q$. Questa chiave $Q$ è un aggregato di due chiavi pubbliche: $P$, una principale chiave pubblica interna, e $M$, una chiave pubblica derivata dalla radice di Merkle di un elenco di _scriptPubKey_. I bitcoin bloccati con questo tipo di script possono essere spesi in due modi:

- Pubblicando una firma per la chiave pubblica $P$ (_key path_);
- Soddisfacendo uno degli script inclusi nell'albero di Merkle (_script path_).

In realtà, queste due chiavi non sono veramente "aggregate". La chiave $P$ è invece modificata dalla chiave $M$. In crittografia, "modificare" una chiave pubblica significa modificare questa chiave applicando un valore additivo chiamato "tweak". Questa operazione permette alla chiave modificata di rimanere compatibile con la chiave privata originale e il tweak. Tecnicamente, un tweak è un valore scalare $t$ che viene aggiunto alla chiave pubblica iniziale. Se $P$ è la chiave pubblica originale, la chiave modificata diventa:

$$
P' = P + tG
$$

Dove $G$ è il generatore della curva ellittica utilizzata. Questa operazione produce una nuova chiave pubblica derivata dalla chiave originale, mantenendo al contempo proprietà crittografiche che ne consentono l'uso.
Se non hai bisogno di aggiungere script alternativi (spendendo esclusivamente tramite il _key path_), puoi generare un indirizzo Taproot basato unicamente sulla chiave pubblica presente al livello 5 del tuo portafoglio. In questo caso, è necessario creare uno script non spendibile per il _script path_, al fine di soddisfare i requisiti della struttura. Il tweak $t$ viene poi calcolato applicando una funzione di hash etichettata, **`TapTweak`**, sulla chiave pubblica interna $P$:

$$
t = \text{H}_{\text{TapTweak}}(P)
$$

dove:

- **$\text{H}_{\text{TapTweak}}$** è una funzione di hash SHA256 etichettata con il tag `TapTweak`. Se non sei familiare con cosa sia una funzione di hash etichettata, ti invito a consultare il capitolo 3.3;
- $P$ è la chiave pubblica interna, rappresentata nel suo formato compresso di 256 bit, utilizzando solo la coordinata $x$.

La chiave pubblica Taproot $Q$ viene poi calcolata aggiungendo il tweak $t$, moltiplicato per il generatore della curva ellittica $G$, alla chiave pubblica interna $P$:

$$
Q = P + t \cdot G
$$

Una volta ottenuta la chiave pubblica Taproot $Q$, possiamo generare l'indirizzo di ricezione corrispondente. A differenza di altri formati, gli indirizzi Taproot non sono stabiliti su un hash della chiave pubblica. Pertanto, la chiave $Q$ viene inserita direttamente nell'indirizzo, in modo grezzo.

Per iniziare, estraiamo la coordinata $x$ del punto $Q$ per ottenere una chiave pubblica compressa. Su questo payload, viene calcolato un checksum utilizzando i codici BCH, come con gli indirizzi SegWit v0. Tuttavia, il programma utilizzato per gli indirizzi Taproot differisce leggermente. Infatti, dopo l'introduzione del formato _bech32_ con SegWit, è stato scoperto un bug: quando l'ultimo carattere di un indirizzo è una `p`, inserire o rimuovere `q` proprio prima di questa `p` non rende il checksum invalido. Sebbene questo bug non abbia conseguenze su SegWit v0 (grazie a un vincolo di dimensione), potrebbe rappresentare un problema in futuro. Questo bug è stato quindi corretto per gli indirizzi Taproot, e il nuovo formato corretto è chiamato "_bech32m_".

L'indirizzo Taproot viene generato codificando la coordinata $x$ di $Q$ nel formato _bech32m_, con i seguenti elementi:

- **L'HRP (_Human Readable Part_)**: `bc`, per indicare la rete Bitcoin principale;
- **La versione**: `1` per indicare Taproot / SegWit v1;
- **Il checksum**.

L'indirizzo finale avrà quindi il formato:

```
bc1p[Qx][checksum]
```

D'altra parte, se desideri aggiungere script alternativi in aggiunta alla spesa con la chiave pubblica interna (_script path_), il calcolo dell'indirizzo di ricezione sarà leggermente diverso. Dovrai includere l'hash degli script alternativi nel calcolo del tweak. In Taproot, ogni script alternativo, situato alla fine dell'albero di Merkle, è chiamato "foglia".

Una volta scritti i diversi script alternativi, devi passarli individualmente attraverso una funzione di hash etichettata `TapLeaf`, accompagnata da alcuni metadati:

$$
\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)
$$

Con:

- $v$: il numero di versione dello script (default `0xC0` per Taproot);
- $sz$: la dimensione dello script codificato in formato _CompactSize_; - $S$: lo script.

I diversi hash dello script ($\text{h}_{\text{leaf}}$) vengono prima ordinati in ordine lessicografico. Poi, vengono concatenati a coppie e passati attraverso una funzione hash etichettata `TapBranch`. Questo processo viene ripetuto iterativamente per costruire, passo dopo passo, l'albero di Merkle:
L'hash del ramo \(\text{h}_{\text{branch}}\) viene calcolato come la funzione hash etichettata `TapBranch` applicata alla concatenazione degli hash delle foglie \(\text{h}_{\text{leaf1}} \Vert \text{h}\_{\text{leaf2}}\):

Proseguiamo quindi concatenando i risultati due a due, passandoli ad ogni passo attraverso la funzione hash etichettata `TapBranch`, fino ad ottenere la radice dell'albero di Merkle:

![CYP201](assets/fr/066.webp)

Una volta calcolata la radice di Merkle \(h*{\text{root}}\), possiamo calcolare il tweak. Per questo, concateniamo la chiave pubblica interna del portafoglio \(P\) con la radice \(h*{\text{root}}\), e poi passiamo il tutto attraverso la funzione hash etichettata `TapTweak`:

\[
t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})
\]

Infine, come prima, la chiave pubblica Taproot \(Q\) si ottiene aggiungendo la chiave pubblica interna \(P\) al prodotto del tweak \(t\) per il punto generatore \(G\):

\[
Q = P + t \cdot G
\]

Quindi, la generazione dell'indirizzo segue lo stesso processo, utilizzando la chiave pubblica grezza \(Q\) come payload, accompagnata da alcuni metadati aggiuntivi.

Ed eccoci! Abbiamo raggiunto la fine di questo corso CYP201. Se hai trovato questo corso utile, ti sarei molto grato se potessi dedicare qualche momento per dare una buona valutazione nel capitolo di valutazione seguente. Sentiti libero di condividerlo anche con i tuoi cari o sui tuoi social network. Infine, se desideri ottenere il tuo diploma per questo corso, puoi sostenere l'esame finale subito dopo il capitolo di valutazione.

# Conclusione

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Valuta questo corso

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Esame finale

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusione

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

Siamo giunti alla fine della formazione CYP201. Spero che sia stata utile nel vostro percorso di apprendimento di Bitcoin e vi abbia aiutato a comprendere meglio il funzionamento dei portafogli HD che utilizzate quotidianamente. Grazie per aver seguito questo corso fino alla fine!

A mio parere, questa conoscenza sui portafogli è fondamentale, poiché collega un aspetto teorico di Bitcoin al suo uso pratico. Infatti, se utilizzate Bitcoin, gestite necessariamente software di portafoglio. Comprendere il loro funzionamento interno vi permette di implementare strategie di sicurezza efficaci padroneggiando al contempo i meccanismi sottostanti, i rischi e le potenziali debolezze. Così, potete utilizzare Bitcoin in modo più sicuro e con fiducia.

Se non l'avete ancora fatto, vi invito a valutare e commentare questa formazione. Mi aiuterebbe enormemente. Potete anche condividere questa formazione sui vostri social network per diffondere questa conoscenza al maggior numero possibile di persone.

Per continuare il vostro viaggio nella tana del coniglio, vi raccomando vivamente la formazione **BTC204**, che ho anche prodotto su Plan ₿ Network. È dedicata alla privacy di Bitcoin ed esplora temi chiave: Qual è il modello di privacy? Come funziona l'analisi della catena? Come utilizzare Bitcoin in modo ottimale per massimizzare la vostra privacy? Un logico passo successivo per approfondire le vostre competenze!

https://planb.network/courses/btc204

Inoltre, per continuare ad approfondire le vostre conoscenze nell'universo Bitcoin, vi invitiamo a esplorare altri corsi disponibili su Plan ₿ Network come:

#### Impara a creare la tua comunità Bitcoin con

https://planb.network/courses/btc302

#### Scopri il Lightning Network con

https://planb.network/courses/lnp201

#### Scopri il pensiero economico della Scuola Austriaca con

https://planb.network/courses/eco201

#### Scopri la storia delle origini di Bitcoin con

https://planb.network/courses/his201

#### Scopri l'evoluzione della libertà attraverso le epoche con

https://planb.network/courses/phi201
