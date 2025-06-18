---
term: CHECKSUM
---

Kontrollsumma on andmekogumi põhjal arvutatud väärtus, mida kasutatakse andmete terviklikkuse ja kehtivuse kontrollimiseks edastamise või salvestamise ajal. Kontrollsumma algoritmid on mõeldud andmete juhuslike vigade või tahtmatute muutuste, näiteks edastusvigade või faili kahjustamise avastamiseks. On olemas eri tüüpi kontrollsummaalgoritme, näiteks pariteedikontrollid, modulaarsed kontrollsummad, krüptograafilised Hash-funktsioonid või BCH (*Bose, Ray-Chaudhuri ja Hocquenghem*) koodid.


Bitcoin-s kasutatakse rakendustasandil kontrollsummasid, et tagada vastuvõtvate aadresside terviklikkus. Kontrollsumma arvutatakse kasutaja Address kasuliku koormuse põhjal ja lisatakse seejärel sellele Address-le, et tuvastada kõik vead selle sisendis. Kontrollsumma on olemas ka taastamislausetes (mnemonites).


> ► *Üldiselt on aktsepteeritud kasutada inglise keele terminit "checksum" otse prantsuse keeles