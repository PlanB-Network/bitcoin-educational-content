---
term: KONSOLIDATSIOON

---
Konkreetne tehing, mille puhul mitu väikest UTXOd liidetakse ühte sisendisse, et moodustada väljundiks üks suurem UTXO. See operatsioon on oma rahakotile tehtud tehing. Konsolideerimise eesmärk on kasutada ära perioode, mil tasud Bitcoini võrgus on madalad, et ühendada mitu väikest UTXOd üheks suuremaks väärtusega UTXOks. Seega ennetab see kohustuslikke kulutusi tasude tõusu korral, võimaldades säästa tulevaste tehingutasude pealt.

Paljude sisenditega tehingud on tõepoolest raskemad ja seega ka kallimad. Lisaks tehingutasude kokkuhoiule on konsolideerimine ka pikaajalise planeerimise vorm. Kui teie rahakott sisaldab väga väikeseid UTXOsid, võivad need muutuda kasutuskõlbmatuks, kui Bitcoini võrk satub pikema aja jooksul kõrgete tasude perioodile. Näiteks kui teil on vaja kulutada 10 000 sati suurust UTXO-d, kuid minimaalsed kaevandamistasud on 15 000 sati, ületaks see kulu UTXO enda väärtuse. Siis muutub nende väikeste UTXOde kasutamine majanduslikult ebamõistlikuks ja need jäävad kasutuskõlbmatuks nii kaua, kuni tasud ei vähene. Neid UTXOsid nimetatakse tavaliselt "tolmuks" Kui konsolideerite regulaarselt oma väikesed UTXOd, vähendate seda tasude suurenemisega seotud riski.

Siiski on oluline märkida, et konsolideerimistehingud on ahelanalüüsi käigus äratuntavad. Selline tehing viitab ühisele sisendiomandile (Common Input Ownership Heuristic, CIOH), mis tähendab, et konsolideerimistehingu sisendid kuuluvad ühele üksusele. See võib mõjutada kasutaja eraelu puutumatust.

![](../../dictionnaire/assets/7.webp)