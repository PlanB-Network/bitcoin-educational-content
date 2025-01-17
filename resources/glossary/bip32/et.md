---
term: BIP32

---
BIP32 võttis kasutusele hierarhilise deterministliku rahakoti (HD wallet) mõiste. See ettepanek võimaldab genereerida võtmepaaride hierarhiat ühisest "master seed'ist", kasutades ühesuunalisi tuletamisfunktsioone. Iga genereeritud võtmepaar võib ise olla teiste lapsvõtmete vanem, moodustades seega puulaadse (hierarhilise) struktuuri. BIP32 eeliseks on see, et see võimaldab hallata mitmeid erinevaid võtmepaare, kusjuures nende taastamiseks on vaja hoida ainult ühte seemet. See uuendus on eelkõige aidanud võidelda aadresside korduvkasutamise probleemiga, mis on tõsine probleem kasutaja privaatsuse seisukohast. BIP32 võimaldab ka alamharu loomist sama rahakoti sees, et hõlbustada selle haldamist.