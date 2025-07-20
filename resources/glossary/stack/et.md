---
term: BATTERI
---

Skriptikeele kontekstis, mida kasutatakse kulutustingimuste kinnitamiseks Bitcoin UTXOdele, on virna LIFO (*Last In, First Out*) andmestruktuur, mida kasutatakse ajutise Elements salvestamiseks skripti täitmise ajal. Iga skripti toiminguga manipuleeritakse neid virnasid, kus Elements saab lisada (*push*) või eemaldada (*pop*). Skriptid kasutavad stäkke väljendite hindamiseks, ajutiste muutujate salvestamiseks ja tingimuste haldamiseks.


Bitcoin skripti käivitamisel saab kasutada 2 virna: põhi- ja alternatiivset virna. Peamist virna kasutatakse enamiku skriptioperatsioonide jaoks. Selles virnas toimuvad skriptioperatsioonid andmete lisamiseks, eemaldamiseks või manipuleerimiseks. Alternatiivset virna kasutatakse seevastu andmete ajutiseks säilitamiseks skripti täitmise ajal. Spetsiifilised opkoodid, nagu `OP_TOALTSTACK` ja `OP_FROMALTSTACK`, võimaldavad Elements üle kanda peast virna alternatiivsesse virna ja vastupidi.


Näiteks tehingu valideerimisel lükatakse allkirjad ja avalikud võtmed põhihunnikusse ja neid töödeldakse järjestikuste opkoodidega, et kontrollida allkirjade vastavust tehingu võtmetele ja andmetele.