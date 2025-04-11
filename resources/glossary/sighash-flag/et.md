---
term: SIGHASH FLAG

---
Bitcoini tehingu parameeter, mis määrab, millised tehingu komponendid (sisendid ja väljundid) on hõlmatud seotud allkirjaga, muutmata seeläbi muutumatuks. SigHash Flag on bait, mis lisatakse iga sisendi digitaalallkirjale. Seega mõjutab SigHash Flagi valik otseselt seda, millised tehingu osad on allkirjaga külmutatud ja milliseid saab hiljem veel muuta. See mehhanism tagab, et allkirjad kinnitavad tehingu andmed täpselt ja turvaliselt vastavalt allkirjastaja kavatsusele. On kolm peamist SigHash Flagi:


- `SIGHASH_ALL` (`0x01`): Allkiri kehtib kõigile tehingu sisenditele ja väljunditele, lukustades need seega täielikult;
- `SIGHASH_NONE` (`0x02`): Allkiri kehtib kõigile sisenditele, kuid mitte ühelegi väljundile, võimaldades väljundite muutmist pärast allkirja andmist;
- `SIGHASH_SINGLE` (`0x03`): Allkiri hõlmab kõiki sisendeid ja ainult ühte väljundit, mis vastab allkirjastatud sisendi indeksile.

Lisaks nendele kolmele SigHashi lippudele saab modifikaatorit `SIGHASH_ANYONECANPAY` (`0x80`) kombineerida kõigi eelnevate tüüpidega. Kui seda modifikaatorit kasutatakse, allkirjastatakse ainult osa sisenditest, jättes ülejäänud muutmisele avatuks. Siin on esitatud olemasolevad kombinatsioonid koos modifitseerijaga:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Allkiri kehtib ühe sisendi suhtes, kuid hõlmab kõiki tehingu väljundeid;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Allkiri katab ühe sisendi, ilma et see kohustuks mingit väljundit andma;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Allkiri kehtib ühe sisendi ja ainult selle sisendiga sama indeksiga väljundi suhtes.

> ► *Signature Hash'i sünonüümiks on mõnikord "Signature Hash Types"