---
term: OP_NOP (0X61)
---

Ne proizvodi nikakav efekat na stek ili stanje skripta. Ne vrši nikakvo pomeranje, provere ili izmene. Jednostavno ne radi ništa osim ako nije drugačije odlučeno putem Soft Fork. Zaista, od njihove izmene od strane Satoshi Nakamoto 2010. godine, `OP_NOP` komande (`OP_NOP1` (`0XB0`) do `OP_NOP10` (`0XB9`)) se koriste za dodavanje novih opkodova u obliku Soft Fork.


Dakle, `OP_NOP2` (`0XB1`) i `OP_NOP3` (`0XB2`) su već korišćeni za implementaciju `OP_CHECKLOCKTIMEVERIFY` i `OP_CHECKSEQUENCEVERIFY`, respektivno. Oni se koriste u kombinaciji sa `OP_DROP` kako bi uklonili povezane vremenske vrednosti sa steka, čime se omogućava nastavak izvršavanja skripta, bez obzira na to da li je čvor ažuriran ili ne. `OP_NOP` komande, dakle, omogućavaju umetanje tačke prekida u skriptu kako bi se proverili dodatni uslovi koji već postoje ili mogu biti dodati sa budućim Soft forkovima. Od Tapscript-a, korišćenje `OP_NOP` je zamenjeno efikasnijim `OP_SUCCESS`.