---
term: SIGHASH_ANYPREVOUT

---
Ettepanek uue SigHash Flag modifikaatori rakendamiseks Bitcoinis, mis on kasutusele võetud koos BIP118-ga. `SIGHASH_ANYPREVOUT` võimaldab suuremat paindlikkust tehingute haldamisel, eriti selliste täiustatud rakenduste puhul nagu maksekanalid Lightning Networkis ja Eltoo uuendamine. `SIGHASH_ANYPREVOUT` võimaldab allkirja mitte siduda ühegi konkreetse eelneva UTXO-ga (*Any Previous Output*). Kasutades seda koos `SIGHASH_ALL`, võimaldab see allkirjastada kõik tehingu väljundid, kuid mitte ühtegi sisendit. See võimaldaks allkirja taaskasutamist erinevate tehingute puhul, kui teatavad kindlaksmääratud tingimused on täidetud.

> ► *See SigHashi modifikaator SIGHASH_ANYPREVOUT on tuletatud ideest SIGHASH_NOINPUT, mille algselt pakkus välja Joseph Poon 2016. aastal, et täiustada oma Lightning Network'i kontseptsiooni