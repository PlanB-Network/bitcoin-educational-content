---
term: STACK

---
Bitcoini UTXOde kulutamistingimuste kohaldamiseks kasutatava skriptikeele kontekstis on virn "LIFO" (*Last In, First Out*) andmestruktuur, mis on mõeldud ajutiste elementide salvestamiseks skripti täitmise ajal. Iga skripti toiminguga manipuleeritakse neid virna, kuhu saab elemente lisada (*push*) või kustutada (*pop*). Skriptid kasutavad stäkke väljendite hindamiseks, ajutiste muutujate salvestamiseks ja tingimuste haldamiseks.

Bitcoini skripti täitmise ajal saab kasutada 2 virna: põhihunnikut ja alt (alternatiivset) virna. Peamist virna kasutatakse enamiku skripti toimingute jaoks. Selles virnas toimuvad skripti operatsioonid, millega lisatakse, eemaldatakse või manipuleeritakse andmeid. Alternatiivne virn seevastu on mõeldud andmete ajutiseks säilitamiseks skripti täitmise ajal. Spetsiifilised opkoodid, nagu `OP_TOALTSTACK` ja `OP_FROMALTSTACK`, võimaldavad elementide ülekandmist põhihunnikust alternatiivsesse hunnikusse ja vastupidi.

Näiteks tehingu valideerimise ajal lükatakse allkirjad ja avalikud võtmed põhihunnikusse ja neid töödeldakse järjestikuste opkoodidega, et kontrollida allkirjade vastavust võtmetele ja tehingu andmetele.

> ► *Inglise keeles on sõna "pile" tõlge "virn". Ingliskeelset terminit kasutatakse üldiselt ka prantsuse keeles tehniliste arutelude käigus.*