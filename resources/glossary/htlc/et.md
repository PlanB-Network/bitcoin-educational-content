---
term: HTLC
---

Tähendab "*Hashed Timelock Contract*". See on Smart contract mehhanism, mida kasutatakse peamiselt Lightningi puhul. Seda leidub mõnikord ka aatomivahetustes. Põhimõtteliselt seab HTLC rahaülekande tingimuseks saladuse avalikustamise ja sisaldab ka ajalist tingimust, et kaitsta saatja raha ebaõnnestunud tehingu korral.


Lightningi puhul võimaldab HTLC saata bitcoine sõlme, millega teil ei ole otsekanalit, läbides mitu kanalit, ilma et teekonnal oleks vaja usaldust. Iga sõlme vaheline makse sõltub eelpildi (saladus, mis vastab hashimise korral kokkulepitud väärtusele) esitamisest. Kui lõppsaaja esitab selle eelkujutise, saab ta raha nõuda ja võimaldab tingimata igal vahesõlmel raha kaskaadina nõuda.


Näiteks kui Alice soovib saata 1 BTC Davidile, kuid tal ei ole temaga otsekanalit, peab ta minema läbi Bobi ja Caroli, kellel on omavahelised maksekanalid. Tehing toimib järgmiselt:




- David kingib Alice'ile Invoice Lightning'i. See sisaldab Hash $h$ salajast $s$ (eelpilt), mida teab ainult David. Seega on meil: $h = \text{Hash}(s)$ ;
- Alice loob HTLC koos Bobiga, kes pakub talle 1 BTC tingimusel, et Bob annab talle salajase $s$ (eelpildi), mis vastab Hash $h$ ;
- Bob loob HTLC koos Caroliga, kes pakub talle 1 BTC tingimusel, et ta annab sama salajase $s$ ;
- Carol loob HTLC koos Davidiga, kes pakub veel 1 BTC, kui ta paljastab $s$ eelpildi;
- David avaldab Carolile $s$ (mida ainult tema teadis), et saada 1 BTC. Carol saab nüüd kasutada $s$, et saada Bobilt BTC. Ja Bob, kes nüüd teab $s$, teeb sama Alice'iga.


Lõpuks saatis Alice 1 BTC Davidile Bobi ja Caroli kaudu (viimase jaoks neutraalne tegevus), ilma et keegi peaks üksteist usaldama, sest kõik on tagatud HTLC-de tingimustega.


HTLC-d võimaldavad seega niinimetatud "aatomilisi" vahetusi: kas ülekanne õnnestub täielikult või ebaõnnestub ja raha tagastatakse. See tagab tehingute turvalisuse isegi mitme osaleja vahel, ilma et oleks vaja usaldust.