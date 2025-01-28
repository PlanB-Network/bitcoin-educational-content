---
term: SEME (BITCOIN)

---
Nel contesto di Bitcoin, un seme è un valore di 512 bit utilizzato per ricavare tutte le chiavi private e pubbliche associate a un portafoglio HD (Hierarchical Deterministic). Tecnicamente, il seme è un valore diverso dalla frase di recupero (o mnemonica). La frase, tipicamente composta da 12 o 24 parole, è generata in modo pseudocasuale da una fonte di entropia e completata da un checksum. Questa frase facilita il backup umano fornendo una rappresentazione testuale del valore alla base del portafoglio.

Per ottenere il seme vero e proprio, la frase di recupero, eventualmente accompagnata da una passphrase opzionale, viene elaborata attraverso l'algoritmo PBKDF2 (*Password-Based Key Derivation Function 2*). Il risultato di questo calcolo è un seme di 512 bit. È questo seme che viene utilizzato per generare in modo deterministico la chiave master e poi l'intera serie di chiavi per il portafoglio HD, in conformità con BIP32.

![](../../dictionnaire/assets/31.webp)

> tuttavia, nel linguaggio comune, la maggior parte dei bitcoiners si riferisce alla frase mnemonica quando parla del "seme", e non allo stato intermedio di derivazione che si trova tra la frase mnemonica e la chiave master