---
termine: SEED (BITCOIN)
---

Nel contesto di Bitcoin, un seed è un valore di 512 bit utilizzato per derivare tutte le chiavi private e pubbliche associate a un portafoglio HD (Hierarchical Deterministic). Tecnicamente, il seed è un valore diverso dalla frase di recupero (o mnemonica). La frase, che è tipicamente composta da 12 o 24 parole, viene generata in modo pseudo-casuale da una fonte di entropia e completata da un checksum. Questa frase facilita il backup umano fornendo una rappresentazione testuale del valore alla base del portafoglio.

Per ottenere il seed effettivo, la frase di recupero, eventualmente accompagnata da una passphrase opzionale, viene elaborata attraverso l'algoritmo PBKDF2 (*Password-Based Key Derivation Function 2*). Il risultato di questo calcolo è un seed di 512 bit. È questo seed che viene utilizzato per generare deterministicamente la chiave maestra, e poi l'intero set di chiavi per il portafoglio HD, in conformità con BIP32.

![](../../dictionnaire/assets/31.png)

> ► *Tuttavia, nel linguaggio comune, la maggior parte dei bitcoiner si riferisce alla frase mnemonica quando parlano di "seed", e non allo stato intermedio di derivazione che si trova tra la frase mnemonica e la chiave maestra.*