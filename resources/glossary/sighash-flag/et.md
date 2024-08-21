---
term: SIGHASH LIPP
---

Parameeter Bitcoin'i tehingus, mis määrab, millised tehingu komponendid (sisendid ja väljundid) on seotud allkirjaga kaetud, muutes need muutumatuks. SigHash lipp on bait, mis lisatakse iga sisendi digitaalsele allkirjale. Seega SigHash lipu valik mõjutab otseselt, millised tehingu osad on allkirja poolt külmutatud ja milliseid saab hiljem muuta. See mehhanism tagab, et allkirjad kinnitavad tehingu andmeid täpselt ja turvaliselt vastavalt allkirjastaja kavatsusele. On kolm peamist SigHash lippu:

- `SIGHASH_ALL` (`0x01`): Allkiri kehtib kõigi tehingu sisendite ja väljundite kohta, lukustades need täielikult;

- `SIGHASH_NONE` (`0x02`): Allkiri kehtib kõigi sisendite, kuid mitte ühegi väljundi kohta, võimaldades väljundeid pärast allkirjastamist muuta;

- `SIGHASH_SINGLE` (`0x03`): Allkiri hõlmab kõiki sisendeid ja ainult ühte väljundit, mis vastab allkirjastatud sisendi indeksile.

Lisaks nendele kolmele SigHash lipule saab modifikaatorit `SIGHASH_ANYONECANPAY` (`0x80`) kombineerida iga eelneva tüübiga. Kui seda modifikaatorit kasutatakse, allkirjastatakse ainult osa sisenditest, jättes ülejäänud muutmiseks avatuks. Siin on olemasolevad kombinatsioonid modifikaatoriga:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Allkiri kehtib ühele sisendile, hõlmates kõiki tehingu väljundeid;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Allkiri hõlmab ühte sisendit, ilma ühegi väljundit kinnitamata;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Allkiri kehtib ühele sisendile ja ainult sellele väljundile, mille indeks on sama kui sellel sisendil.

> ► *SigHash'i sünonüümiks on mõnikord kasutatud "Signature Hash Types".*