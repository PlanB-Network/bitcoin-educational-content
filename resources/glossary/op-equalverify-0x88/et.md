---
term: OP_EQUALVERIFY (0X88)

definition: Kombineerib OP_EQUAL ja OP_VERIFY, tühistades tehingu, kui väärtused erinevad.
---
Ühendab funktsioonid `OP_EQUAL` ja `OP_VERIFY`. Esmalt kontrollitakse virna kahe ülemise väärtuse võrdsust, seejärel nõutakse, et tulemus ei oleks null, vastasel juhul on tehing kehtetu. `OP_EQUALVERIFY` kasutatakse eelkõige aadressi kontrollimise skriptides.