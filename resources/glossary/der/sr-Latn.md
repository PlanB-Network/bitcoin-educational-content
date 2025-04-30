---
term: DER
---

Akronim za *Distinguished Encoding Rules*. To je strogi podskup ASN.1 pravila kodiranja definisanih u specifikaciji [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) i koristi se za kodiranje bilo koje vrste podataka u binarnom nizu. DER se uglavnom koristi u specifičnim oblastima, kao što je kriptografija, gde podaci moraju biti kodirani na standardan, predvidljiv način.


Na Bitcoin, ECDSA potpisi su kodirani u DER formatu. Sastoje se od dva 32-bajtna kodirana broja (`r`,`s`). Format potpisa se sastoji od sledećeg Elements (71 bajt):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Sa :




- 0x30` (1 bajt): identifikator složene strukture;
- dužina` (1 bajt): dužina sledećih podataka ;
- 0x02` (1 byte): tip identifikatora podataka `INTEGER` (integer) ;
- `r-length` (1 bajt): dužina sledeće `r` vrednosti (32 bajta) ;
- r` (32 bajta): vrednost `r` kao big-endian ceo broj;
- 0x02` (1 byte): tip identifikatora podataka `INTEGER` (integer) ;
- `s-length` (1 bajt): dužina sledeće `s` vrednosti (32 bajta) ;
- `s` (32 bajta): `s` vrednost kao big-endian ceo broj.


U Bitcoin transakciji, bajt se dodaje na kraju DER potpisa kako bi se označila vrsta korišćenog SigHash-a.