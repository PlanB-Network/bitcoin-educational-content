---
term: SIGHASH_ANYPREVOUT
---

Ettepanek uue SigHash lipu modifikaatori rakendamiseks Bitcoinis, mis tutvustati BIP118-ga. `SIGHASH_ANYPREVOUT` võimaldab suuremat paindlikkust tehingute haldamisel, eriti edasijõudnud rakenduste puhul nagu maksekanalid Lightning Network'il ja Eltoo uuendus. `SIGHASH_ANYPREVOUT` võimaldab allkirjal mitte olla seotud ühegi kindla eelneva UTXO-ga (*Any Previous Output*). Kasutades koos `SIGHASH_ALL`-iga, võimaldaks see allkirjastada kõik tehingu väljundid, kuid mitte ühtegi sisendit. See võimaldaks allkirja taaskasutamist erinevate tehingute jaoks, tingimusel, et on täidetud teatud määratud tingimused.

> ► *See SigHash modifikaator SIGHASH_ANYPREVOUT on tuletatud ideest SIGHASH_NOINPUT, mille esitas algselt Joseph Poon 2016. aastal, et täiustada tema kontseptsiooni Lightning Network'ist.*