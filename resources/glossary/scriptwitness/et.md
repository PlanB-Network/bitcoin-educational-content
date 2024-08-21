---
term: SCRIPTWITNESS
---

SegWiti tehingukirjetes olev element, mis sisaldab allkirju ja avalikke võtmeid, mis on vajalikud tehingus saadetud bitcoinide vabastamiseks. Sarnaselt Legacy tehingute `scriptSig`-iga ei aseta `scriptWitness` siiski samasse asukohta. Tegelikult on see osa, mida nimetatakse "tunnistajaks" (`*witness*` inglise keeles), viidud eraldi andmebaasi, et lahendada tehingute muudetavuse probleem. Igal SegWiti sisendil on oma `scriptWitness`, ja kõik `scriptWitness` elemendid kokku moodustavad tehingu `Witness` välja.

> ► *Olge ettevaatlik, et mitte segi ajada `scriptWitness`-i `witnessScript`-iga. Kuigi `scriptWitness` sisaldab tunnistaja andmeid mis tahes SegWiti sisendi jaoks, määratleb `witnessScript` P2WSH või P2SH-P2WSH UTXO kulutamise tingimused ja on omaette skript, sarnaselt P2SH väljundi `redeemScript`-iga.*