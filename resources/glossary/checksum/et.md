---
term: CHECKSUM

---
Kontrollsumma on andmekogumi arvutatud väärtus, mida kasutatakse andmete terviklikkuse ja kehtivuse kontrollimiseks nende edastamise või salvestamise ajal. Kontrollsumma algoritmid on mõeldud andmete juhuslike vigade või tahtmatute muutuste, näiteks edastusvigade või failide vigade avastamiseks. On olemas mitmesuguseid kontrollsummaalgoritme, näiteks pariteedikontrollid, modulaarsed kontrollsummad, krüptograafilised hash-funktsioonid või BCH-koodid (*Bose, Ray-Chaudhuri ja Hocquenghem*).

Bitcoinis kasutatakse rakenduse tasandil kontrollsummasid, et tagada vastuvõtvate aadresside terviklikkus. Kontrollsumma arvutatakse kasutaja aadressi kasuliku koormuse põhjal ja lisatakse sellele aadressile, et tuvastada võimalikke vigu selle sisestamisel. Kontrollsumma on olemas ka taastamislausetes (mnemooniline).

> ► *Somme de contrôle'i ingliskeelne tõlge on "checksum". Prantsuse keeles on üldtunnustatud kasutada otse mõistet "checksum".*