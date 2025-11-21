---
term: BIP0112
---

Uvodi opcode `OP_CHECKSEQUENCEVERIFY` (CSV) u Bitcoin Script jezik. Ova operacija omogućava kreiranje transakcija čija validnost postaje efektivna tek nakon određenog kašnjenja u odnosu na prethodnu transakciju, definisano ili brojem blokova ili vremenskim trajanjem. `OP_CHECKSEQUENCEVERIFY` poredi vrednost na vrhu steka sa vrednošću `nSequence` polja ulaza. Ako je veća i svi ostali uslovi su ispunjeni, skript je validan. Tako, `OP_CHECKSEQUENCEVERIFY` ograničava moguće vrednosti za `nSequence` polje ulaza koji ga troši, a samo to `nSequence` polje ograničava kada transakcija koja uključuje taj ulaz može biti uključena u blok. BIP112 je uveden putem Soft Fork 4. jula 2016, zajedno sa BIP68 i BIP113, prvi put aktiviran korišćenjem BIP9 metode.