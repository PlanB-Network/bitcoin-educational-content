---
term: DER
---

Akronüüm *Distinguished Encoding Rules*. See on spetsifikatsioonis [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) määratletud ASN.1 kodeerimisreeglite range alamhulk, mida kasutatakse mis tahes tüüpi andmete kodeerimiseks binaarfaili. DERi kasutatakse peamiselt spetsiifilistes valdkondades, näiteks krüptograafias, kus andmed tuleb kodeerida standardsel, ennustataval viisil.


Bitcoin-l on ECDSA allkirjad kodeeritud DER-vormingus. Need koosnevad kahest 32baidisest kodeeritud numbrist (`r`,`s`). Allkirjaformaat koosneb järgmisest Elements (71 baiti):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Koos :




- 0x30` (1 bait): liitstruktuuri identifikaator;
- length` (1 bait): järgmiste andmete pikkus ;
- 0x02" (1 bait): andmete identifikaatori tüüp "INTEGER" (täisarv) ;
- "r-length" (1 bait): järgmise "r" väärtuse pikkus (32 baiti) ;
- r" (32 baiti): "r" väärtus big-endian täisarvuna;
- 0x02" (1 bait): andmete identifikaatori tüüp "INTEGER" (täisarv) ;
- `s-length` (1 bait): järgmise `s` väärtuse pikkus (32 baiti) ;
- "s" (32 baiti): `s` väärtus big-endian täisarvuna.


Bitcoin tehingus lisatakse DER-allkirja lõppu bait, mis näitab kasutatud SigHashi tüüpi.