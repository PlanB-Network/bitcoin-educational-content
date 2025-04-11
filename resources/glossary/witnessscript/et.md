---
term: WITNESSSSSCRIPT

---
Skript, mis määrab kindlaks tingimused, mille alusel saab bitcoine kulutada P2WSH või P2SH-P2WSH UTXOdest. Tavaliselt määrab `witnessScript` kindlaks SegWit-standardi kohase multisignatuuriga rahakoti tingimused. Nende skriptistandardite puhul sisaldab UTXO `scriptPubKey` (väljund) `witnessScript`i hashi. Et kasutada seda UTXO-d uues tehingus sisendina, peab omanik avaldama algse `witnessScript'i`, et tõestada selle vastavust `scriptPubKey`s sisalduvale sõrmejäljele. Seejärel tuleb `witnessScript` lisada tehingu `scriptWitness`i, mis sisaldab ka skripti valideerimiseks vajalikke elemente, näiteks allkirju. Seega on `witnessScript` SegWit'i puhul samaväärne P2SH-tehingu `redeemScript'iga, kuid selle erinevusega, et see paigutatakse tehingu tunnistajasse, mitte `scriptSig`i.

> ► *Vahe, "tunnistuseSkript" ei tohi segi ajada "tunnistuseSkripti"-ga. Kui `witnessScript` määratleb P2WSH või P2SH-P2WSH UTXO kulutustingimused ja kujutab endast iseseisvat skripti, siis `scriptWitness` sisaldab mis tahes SegWit-sisendi tunnistusandmeid.*