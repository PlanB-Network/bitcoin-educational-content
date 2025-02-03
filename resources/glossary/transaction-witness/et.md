---
term: TEHINGU TUNNISTAJA

---
Viitab Bitcoini tehingute komponendile, mis viidi üle koos SegWit pehme kahvliga, et lahendada tehingu muutlikkuse probleem. Tunnistaja sisaldab allkirju ja avalikke võtmeid, mis on vajalikud tehingus kulutatud bitcoinide avamiseks. Legacy-tehingutes kujutas tunnistaja kõigi sisendite `scriptSig` summat. SegWit-tehingutes kujutab tunnistaja iga sisendi "scriptWitnessi" summat ja see osa tehingust on nüüd viidud eraldi Merkle'i puusse ploki sees.

Enne SegWit'i võis allkirju enne tehingu kinnitamist veidi muuta, ilma et neid kehtetuks tunnistataks, mis muutis tehingu identifikaatorit. See raskendas erinevate protokollide koostamist, kuna kinnitamata tehingu identifikaator võis muutuda. Tunnistajate eraldamisega muudab SegWit tehingud mittemalleeritavaks, kuna mis tahes muutus allkirjades ei mõjuta enam tehingu identifikaatorit (TXID), vaid ainult tunnistaja identifikaatorit (WTXID). Lisaks võltsitavuse probleemi lahendamisele võimaldab selline eraldamine suurendada iga ploki mahutavust.

> ► *Inglise keeles on "témoin" tõlgitud kui "tunnistaja"