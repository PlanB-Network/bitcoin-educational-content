---
term: BIP32
---

BIP32 tutvustas hierarhilise deterministliku rahakoti (HD rahakott) kontseptsiooni. See ettepanek võimaldab ühisest `master seed`'ist lähtuvalt genereerida võtmepaaride hierarhiat, kasutades ühesuunalisi tuletusfunktsioone. Iga genereeritud võtmepaar võib omakorda olla teiste alamvõtmete vanem, moodustades nii puulaadse (hierarhilise) struktuuri. BIP32 eeliseks on see, et see võimaldab hallata mitmeid erinevaid võtmepaare, vajades selleks vaid ühte algset seemet nende taasgenereerimiseks. See uuendus on märkimisväärselt aidanud võidelda aadresside korduvkasutuse probleemiga, mis on kasutajate privaatsuse seisukohast tõsine. BIP32 võimaldab samuti luua samas rahakotis alamharusid, et hõlbustada selle haldamist.