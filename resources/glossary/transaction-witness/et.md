---
term: TEHINGU TUNNISTAJA
---

Viitab Bitcoin'i tehingute komponendile, mis SegWiti pehme tarkvarauuendusega liigutati, et lahendada tehingute muudetavuse probleemi. Tunnistaja sisaldab allkirju ja avalikke võtmeid, mis on vajalikud tehingus kulutatud bitcoinide vabastamiseks. Pärandtehingutes esindas tunnistaja kõikide sisendite `scriptSig` summat. SegWiti tehingutes esindab tunnistaja iga sisendi `scriptWitness` summat ning see osa tehingust on nüüd liigutatud eraldi Merkle puusse blokis.

Enne SegWiti sai allkirju enne tehingu kinnitamist veidi muuta ilma, et need kehtetuks muutuksid, mis muutis tehingu identifikaatori. See tegi erinevate protokollide loomise keeruliseks, kuna kinnitamata tehingu identifikaator võis muutuda. Tunnistajate eraldamisega muudab SegWit tehingud muudetamatuks, kuna allkirjade muutmine ei mõjuta enam tehingu identifikaatorit (TXID), vaid ainult tunnistaja identifikaatorit (WTXID). Lisaks muudetavuse probleemi lahendamisele võimaldab see eraldamine suurendada iga bloki mahutavust.

> ► *Inglise keeles tõlgitakse "témoin" kui "witness".*