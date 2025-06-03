---
term: BIP0113
---

Uvedena je promena u izračunavanju svih operacija vremenskog zaključavanja (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` i `OP_CHECKSEQUENCEVERIFY`). Ona specificira da se za procenu validnosti vremenskih zaključavanja sada moraju porediti sa MTP (*Median Time Past*), što je medijana vremenskih oznaka poslednjih 11 blokova. Prethodno je korišćen samo Timestamp prethodnog bloka. Ovaj metod čini sistem predvidljivijim i sprečava manipulaciju vremenskom referencom od strane rudara. BIP113 je uveden putem Soft Fork 4. jula 2016. godine, zajedno sa BIP68 i BIP112, prvi put aktiviran korišćenjem BIP9 metode.