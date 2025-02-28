---
term: SCRIPTWITNESS

---
Prvek v záznamech transakcí SegWit, který obsahuje podpisy a veřejné klíče potřebné k odemčení bitcoinů odeslaných v transakci. Podobně jako `scriptSig` u transakcí Legacy se však `scriptWitness` nenachází na stejném místě. Ve skutečnosti je právě tato část, označovaná jako "svědek" (anglicky `*witness*`), přesunuta do samostatné databáze, aby se vyřešil problém s falšovatelností transakcí. Každý vstup SegWit má svůj vlastní `scriptWitness` a všechny prvky `scriptWitness` dohromady tvoří pole `Witness` transakce.

> ► *Dejte pozor, abyste nezaměnili `scriptWitness` s `witnessScript`. Zatímco `scriptWitness` obsahuje svědecká data pro jakýkoli vstup SegWit, `witnessScript` definuje podmínky výdejů P2WSH nebo P2SH-P2WSH UTXO a představuje samostatný skript, podobně jako `redeemScript` pro výstup P2SH.*