---
term: BLOOMI FILTER
---

Probabilistlik andmestruktuur, mida kasutatakse testimaks, kas element on osa mingist komplektist. Bloomi filtrid võimaldavad kiiresti kontrollida liikmelisust ilma terve andmekogumi läbitestimiseta. Need on eriti kasulikud kontekstides, kus ruumi ja kiirus on kriitilise tähtsusega, kuid madal ja kontrollitud veamäär on aktsepteeritav. Tõepoolest, Bloomi filtrid ei tekita valepositiivseid tulemusi, kuid nad genereerivad teatud hulga valepositiivseid tulemusi. Kui element lisatakse filtrile, genereerivad mitmed räsifunktsioonid positsioone bitimassiivis. Liikmelisuse kontrollimiseks kasutatakse samu räsifunktsioone. Kui kõik vastavad bitid on seadistatud, on element tõenäoliselt komplektis, kuid valepositiivsete riskiga. Bloomi filtrid on laialdaselt kasutusel andmebaaside ja võrkude valdkondades. On märkimisväärne, et Google kasutab neid oma kompresseeritud andmebaaside haldussüsteemis *BigTable*. Bitcoin'i protokollis kasutatakse neid eriti SPV rahakottide puhul vastavalt BIP37-le.

> ► *Konkreetselt rääkides Bloomi filtrite kasutamisest Bitcoin'i tehingute kontekstis kohtab mõnikord terminit "Transaction Bloom Filtering".*