---
term: WITNESSSCRIPT

---
Skript, který určuje podmínky, za kterých lze utratit bitcoiny z P2WSH nebo P2SH-P2WSH UTXO. Typicky `witnessScript` určuje podmínky peněženky s více podpisy podle standardu SegWit. V těchto standardech skriptů obsahuje `scriptPubKey` UTXO (výstup) hash `witnessScript`. Pokud chce držitel použít tento UTXO jako vstup v nové transakci, musí odhalit původní `witnessScript`, aby prokázal jeho shodu s otiskem v `scriptPubKey`. Pak musí být `witnessScript` zahrnut do `scriptWitness` transakce, která obsahuje také prvky nezbytné k ověření skriptu, jako jsou podpisy. Proto je `witnessScript` pro SegWit ekvivalentem `redeemScript` v transakci P2SH s tím rozdílem, že je umístěn ve svědkovi transakce, a nikoli ve `scriptSig`.

> ► *Upozornění, `svědekScript` by neměl být zaměňován s `skriptemSvědek`. Zatímco `witnessScript` definuje podmínky výdajů P2WSH nebo P2SH-P2WSH UTXO a představuje samostatný skript, `scriptWitness` obsahuje svědecké údaje jakéhokoli vstupu SegWit.*