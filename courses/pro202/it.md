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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematica per l'implementazione del Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Crittografia a curva ellittica

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Operazioni interne al Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Parsing delle transazioni e firme ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Convalida di script e transazioni

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Costruzione di transazioni e Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Rete Bitcoin: struttura interna della rete

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blocchi Bitcoin e Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Comunicazione di rete e alberi Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Comunicazione avanzata dei nodi e testimonianza segregata

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sezione finale


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recensioni e valutazioni


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusione


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
