---
term: WITNESSSCRIPT
---

Skript, mis määratleb tingimused, millal bitcoine saab kulutada P2WSH või P2SH-P2WSH UTXO-dest. Tavaliselt määrab `witnessScript` tingimused multisignatuuriga rahakoti jaoks SegWit standardi alusel. Nendes skripti standardites sisaldab UTXO (väljund) `scriptPubKey` `witnessScript`i hashi. Selle UTXO kasutamiseks sisendina uues tehingus peab hoidja paljastama algse `witnessScript`i, et tõestada selle vastavust `scriptPubKey`s olevale sõrmejäljele. `witnessScript` tuleb seejärel lisada tehingu `scriptWitness`i, mis sisaldab ka elemente skripti valideerimiseks, nagu allkirjad. Seega on `witnessScript` SegWiti jaoks samaväärne `redeemScript`iga P2SH tehingus, erinevusega, et see asetatakse tehingu tunnistaja osasse, mitte `scriptSig`i.

> ► *Ettevaatust, `witnessScript`i ei tohiks segi ajada `scriptWitness`iga. Kuigi `witnessScript` määratleb P2WSH või P2SH-P2WSH UTXO kulutamise tingimused ja on iseseisev skript, sisaldab `scriptWitness` kõiki SegWit sisendi tunnistaja andmeid.*