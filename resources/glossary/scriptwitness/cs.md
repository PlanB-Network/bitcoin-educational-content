---
term: SCRIPTWITNESS
---

Prvek v záznamech transakcí SegWit, který obsahuje podpisy a veřejné klíče potřebné k odemčení bitcoinů poslaných v transakci. Podobně jako `scriptSig` u tradičních transakcí, `scriptWitness` není umístěn na stejném místě. Skutečně, je to tato část, označovaná jako "svědek" (`*witness*` v angličtině), která je přesunuta do samostatné databáze za účelem vyřešení problému s mutovatelností transakcí. Každý vstup SegWit má svůj vlastní `scriptWitness`, a všechny prvky `scriptWitness` dohromady tvoří pole `Witness` transakce.

> ► *Buďte opatrní, abyste nespletli `scriptWitness` s `witnessScript`. Zatímco `scriptWitness` obsahuje data svědka pro jakýkoli vstup SegWit, `witnessScript` definuje podmínky výdaje pro UTXO P2WSH nebo P2SH-P2WSH a tvoří skript samotný, podobně jako `redeemScript` pro výstup P2SH.*