---
term: LIBSECP256K1
---

Suure jõudlusega ja kõrge turvalisusega C-keelkirjade ja muude krüptograafiliste primitiivide jaoks `secp256k1` elliptilisel kõveral. Kuna seda kõverat ei ole kunagi laialdaselt kasutatud väljaspool Bitcoin (erinevalt sageli eelistatud `secp256r1` kõverast), on selle raamatukogu eesmärk olla kõige põhjalikum viide selle kasutamiseks. Libsecp256k1 arendus oli peamiselt suunatud Bitcoin vajadustele ning teiste rakenduste jaoks mõeldud funktsioone võib olla vähem testitud või kontrollitud. Selle raamatukogu asjakohane kasutamine nõuab hoolikat tähelepanu, et tagada selle sobivus muude rakenduste kui Bitcoin spetsiifilisteks eesmärkideks.


Libsecp256k1 raamatukogu pakub mitmesuguseid funktsioone, sealhulgas:




- ECDSA-secp256k1 allkiri ja kontroll ning krüptograafilise võtme genereerimine ;
- Additiivsed ja multiplikatiivsed operatsioonid salajaste ja avalike võtmetega ;
- Salajaste võtmete, avalike võtmete ja allkirjade järjestamine ja analüüs ;
- Konstantse ajaga avaliku võtme allkirjastamine ja genereerimine pideva mäluühendusega;
- Ja hulk muid krüptograafilisi primitiive.