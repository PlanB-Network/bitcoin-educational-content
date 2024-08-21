---
term: STACK
---

Skriptimiskeele kontekstis, mida kasutatakse Bitcoin'i UTXO-de kulutamistingimuste rakendamiseks, on stack "LIFO" (*Last In, First Out*) andmestruktuur, mis teenib ajutiste elementide salvestamise eesmärki skripti täitmise ajal. Iga toiming skriptis manipuleerib neid stäkke, kus elemente saab lisada (*push*) või eemaldada (*pop*). Skriptid kasutavad stäkke avaldiste hindamiseks, ajutiste muutujate salvestamiseks ja tingimuste haldamiseks.

Bitcoin'i skripti täitmisel võib kasutada 2 stäkki: peamine stäkk ja alt (alternatiivne) stäkk. Peamist stäkki kasutatakse skripti enamiku toimingute jaoks. Just selles stäkis lisavad, eemaldavad või manipuleerivad skripti toimingud andmeid. Alternatiivne stäkk seevastu teenib andmete ajutist salvestamist skripti täitmise ajal. Spetsiifilised operaatorid, nagu `OP_TOALTSTACK` ja `OP_FROMALTSTACK`, võimaldavad elementide ülekandmist peamisest stäkist alternatiivsesse stäkki ja vastupidi.

Näiteks tehingu valideerimise ajal lükatakse allkirjad ja avalikud võtmed peamisele stäkile ja töödeldakse järjestikuste operaatoritega, et kontrollida, kas allkirjad vastavad võtmetele ja tehingu andmetele.

> ► *Inglise keeles tõlgitakse « pile » kui « stack ». Tehnilistes aruteludes kasutatakse üldiselt inglisekeelset terminit isegi prantsuse keeles.*