---
name: Programmazione Bitcoin
goal: Costruire una libreria Bitcoin completa da zero e comprendere le basi crittografiche di Bitcoin
objectives: 

 - Implementare l'aritmetica dei campi finiti e le operazioni sulle curve ellittiche in Python
 - Costruire e analizzare le transazioni Bitcoin in modo programmatico
 - Creare indirizzi Testnet e trasmettere le transazioni in rete
 - Padroneggiare le basi matematiche del modello di sicurezza di Bitcoin

---
# Un viaggio nei copioni e nei programmi di Bitcoin


Questo corso intensivo di due giorni, tenuto da Jimmy Song, vi porta in profondità nelle basi tecniche di Bitcoin costruendo una libreria Bitcoin completa da zero. Partendo dalla matematica essenziale dei campi finiti e delle curve ellittiche, si passerà all'analisi delle transazioni, all'esecuzione degli script e alla comunicazione di rete. Attraverso esercizi pratici di codifica in Jupyter notebook, creerete il vostro Testnet Address, costruirete transazioni manualmente e le trasmetterete direttamente alla rete, il tutto acquisendo una profonda comprensione dei principi crittografici che rendono Bitcoin sicuro e Trustless.


Buona scoperta!


+++

# Introduzione

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Panoramica del corso

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Benvenuto al corso PRO 202 _**Programming Bitcoin**_, un viaggio intensivo che ti porta dall'aritmetica dei campi finiti fino alla creazione e trasmissione di transazioni reali sulla rete di test di Bitcoin.

In questo corso, costruirai progressivamente una libreria Bitcoin in Python acquisendo al contempo le basi crittografiche, di protocollo e di software necessarie per comprendere con precisione la sicurezza e il funzionamento interno di Bitcoin. L’approccio PRO 202 è completamente pratico: ogni concetto viene immediatamente implementato nei notebook Jupyter, garantendo che teoria e codice si rafforzino a vicenda.

### Concetti matematici essenziali per Bitcoin

Questa prima sezione pone le indispensabili basi matematiche. Implementerai l'aritmetica dei campi finiti e le operazioni sulle curve ellittiche (legge di gruppo, addizione, raddoppio, moltiplicazione scalare...) — i prerequisiti per ECDSA. L'obiettivo è duplice: comprendere la struttura algebrica che rende possibili le firme crittografiche e costruire strumenti affidabili in Python per manipolarle.

Successivamente formalizzerai i componenti di ECDSA: generazione delle chiavi, formattazione dei punti, hashing, creazione e verifica delle firme. Questa sezione collega direttamente la teoria alla pratica, enfatizzando i dettagli di implementazione e la robustezza del modello di sicurezza sottostante.

### Funzionamento interno di una transazione Bitcoin

Nella seconda sezione analizzerai la struttura di una transazione Bitcoin: UTXO, input/output, sequenze, script, codifiche e altro ancora. Scriverai codice per costruire, firmare e verificare transazioni, ottenendo una comprensione precisa di ciò che viene impegnato dall’hash e del perché.

Successivamente implementerai un esecutore _Script_ minimale, esaminerai gli opcodes principali e validerai i percorsi di spesa. L’obiettivo è renderti capace di verificare il comportamento delle transazioni, diagnosticare errori di validazione e valutare la sicurezza delle politiche di spesa.

### Funzionamento interno della rete Bitcoin

Nella terza sezione, collocherai la transazione all’interno del sistema più ampio: struttura del blocco, intestazioni, difficoltà e meccanismo di Proof-of-Work. Gestirai i messaggi di protocollo, le intestazioni dei blocchi e gli alberi di Merkle.

Infine, studierai la comunicazione tra nodi peer-to-peer, l’ottimizzazione dei messaggi e l’introduzione di SegWit.

Come in ogni corso della Plan ₿ Academy, la sezione finale include una valutazione progettata per consolidare la tua comprensione. Pronto a scoprire il funzionamento interno di Bitcoin e a scrivere il codice che lo alimenta? Iniziamo!

# Concetti matematici essenziali per Bitcoin

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matematica per l'implementazione del Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Crittografia a curva ellittica

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Operazioni interne al Bitcoin

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Parsing delle transazioni e firme ECDSA

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Convalida di script e transazioni

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Costruzione di transazioni e Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Rete Bitcoin: struttura interna della rete

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Blocchi Bitcoin e Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Comunicazione di rete e alberi Merkle

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Comunicazione avanzata dei nodi e testimonianza segregata

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sezione finale


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Recensioni e valutazioni


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusione


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
