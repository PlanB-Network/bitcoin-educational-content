---
termine: SEED
---

Nel contesto specifico di un portafoglio Bitcoin deterministico gerarchico, un seed è un pezzo di informazione da 512 bit derivato dalla casualità. Viene utilizzato per generare in modo deterministico e gerarchico un insieme di chiavi private e le loro corrispondenti chiavi pubbliche, per un portafoglio Bitcoin. Il seed è spesso confuso con la frase di recupero stessa. Tuttavia, si tratta di informazioni diverse. Il seed si ottiene applicando la funzione `PBKDF2` alla frase mnemonica e a qualsiasi eventuale passphrase.

Il seed è stato inventato con l'introduzione di BIP32, che definisce le fondamenta del portafoglio deterministico gerarchico. In questo standard, il seed era di 128 bit. Questo permette la derivazione di tutte le chiavi in un portafoglio da un unico pezzo di informazione, a differenza dei portafogli JBOK (*Just a Bunch Of Keys*), che richiedono nuovi backup per ogni chiave generata. BIP39 ha successivamente introdotto una codifica di questo seed per semplificarne la leggibilità umana. Questa codifica è realizzata sotto forma di frase, comunemente riferita come frase mnemonica o frase di recupero. Questo standard aiuta a evitare errori nel backup del seed, notevolmente attraverso l'uso di un checksum.

Più in generale, in crittografia, un seed è un pezzo di dati casuali utilizzato come punto di partenza per generare chiavi crittografiche, cifrature o sequenze pseudo-casuali. La qualità e la sicurezza di molti processi crittografici dipendono dalla casualità e dalla confidenzialità del seed.

> ► *La traduzione in inglese di "graine" è "seed". In francese, molti usano direttamente la parola inglese per riferirsi al seed.*