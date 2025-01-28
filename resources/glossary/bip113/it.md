---
term: BIP113

---
Introdotto un cambiamento nel calcolo di tutte le operazioni di timelock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` e `OP_CHECKSEQUENCEVERIFY`). Specifica che per valutare la validità dei timelock, ora devono essere confrontati con l'MTP (*Median Time Past*), che è la mediana dei timestamp degli ultimi 11 blocchi. In precedenza, veniva utilizzato solo il timestamp del blocco precedente. Questo metodo rende il sistema più prevedibile e impedisce la manipolazione del riferimento temporale da parte dei minatori. BIP113 è stato introdotto tramite una soft fork il 4 luglio 2016, insieme a BIP68 e BIP112, attivati per la prima volta con il metodo BIP9.