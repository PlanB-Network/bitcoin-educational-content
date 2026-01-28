---
term: OP_NUMEQUALVERIFY (0X9D)

definition: Kombineerib OP_NUMEQUAL ja OP_VERIFY, ebaõnnestudes, kui arvulised väärtused erinevad.
---
Kombineerib operatsioonid `OP_NUMEQUAL` ja `OP_VERIFY`. Võrreldakse numbriliselt korstnas olevaid kahte kõige ülemist elementi. Kui väärtused on võrdsed, eemaldab `OP_NUMEQUALVERIFY` tõelise tulemuse virnast ja jätkab skripti täitmist. Kui väärtused ei ole võrdsed, on tulemus vale ja skript kohe ebaõnnestub.