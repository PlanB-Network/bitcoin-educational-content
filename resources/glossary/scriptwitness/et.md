---
term: SCRIPTWITNESS

---
Element SegWit-tehingute kirjetes, mis sisaldab allkirju ja avalikke võtmeid, mis on vajalikud tehingus saadetud bitcoinide avamiseks. Sarnaselt Legacy-tehingute `scriptSig`iga ei ole `scriptWitness` siiski samas kohas. See osa, mida nimetatakse "tunnistajaks" (inglise keeles `*witness*`), on tõepoolest viidud eraldi andmebaasi, et lahendada tehingu võltsitavuse probleem. Igal SegWiti sisendil on oma `scriptWitness` ja kõik `scriptWitness` elemendid koos moodustavad tehingu `Witness` välja.

> ► *Ole ettevaatlik, et mitte segi ajada `scriptWitness` ja `witnessScript`. Kui `scriptWitness` sisaldab mis tahes SegWit-sisendi tunnistusandmeid, siis `witnessScript` määratleb P2WSH või P2SH-P2WSH UTXO kulutustingimused ja kujutab endast iseseisvat skripti, sarnaselt P2SH-väljundi `redeemScript`iga.*