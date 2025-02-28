---
term: SEME

---
Nel contesto specifico di un portafoglio Bitcoin deterministico gerarchico, un seme è un'informazione di 512 bit derivata dalla casualità. Viene utilizzato per generare in modo deterministico e gerarchico un insieme di chiavi private e le corrispondenti chiavi pubbliche per un portafoglio Bitcoin. Il seme viene spesso confuso con la frase di recupero stessa. Tuttavia, si tratta di informazioni diverse. Il seme si ottiene applicando la funzione `PBKDF2` alla frase mnemonica e a qualsiasi potenziale passphrase.

Il seme è stato inventato con l'introduzione del BIP32, che definisce le basi del portafoglio deterministico gerarchico. In questo standard, il seme era di 128 bit. Ciò consente di derivare tutte le chiavi di un portafoglio da un'unica informazione, a differenza dei portafogli JBOK (*Just a Bunch Of Keys*), che richiedono nuovi backup per ogni chiave generata. Il BIP39 ha poi introdotto una codifica di questo seme per semplificarne la leggibilità da parte dell'uomo. La codifica avviene sotto forma di frase, comunemente chiamata frase mnemonica o frase di recupero. Questo standard aiuta a evitare errori nel backup del seme, in particolare attraverso l'uso di una somma di controllo.

Più in generale, in crittografia, un seme è un dato casuale utilizzato come punto di partenza per generare chiavi crittografiche, crittografie o sequenze pseudocasuali. La qualità e la sicurezza di molti processi crittografici dipendono dalla casualità e dalla riservatezza del seme.

> *La traduzione inglese di "graine" è "seme". In francese, molti usano direttamente la parola inglese per riferirsi al seme.*