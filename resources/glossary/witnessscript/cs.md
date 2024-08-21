---
term: WITNESSSCRIPT
---

Skript, který specifikuje podmínky, za kterých lze bitcoiny utratit z UTXO P2WSH nebo P2SH-P2WSH. Typicky `witnessScript` určuje podmínky multisignaturní peněženky podle standardu SegWit. V těchto standardech skriptů obsahuje `scriptPubKey` UTXO (výstupu) hash `witnessScriptu`. Aby mohl držitel toto UTXO použít jako vstup v nové transakci, musí odhalit původní `witnessScript`, aby prokázal jeho shodu s otiskem v `scriptPubKey`. `witnessScript` musí být poté zahrnut v `scriptWitness` transakce, který také obsahuje prvky nezbytné pro validaci skriptu, jako jsou podpisy. `witnessScript` je tedy ekvivalentem `redeemScriptu` v transakci P2SH pro SegWit, s tím rozdílem, že je umístěn v svědkovi transakce, a ne v `scriptSig`.

> ► *Pozor, `witnessScript` by neměl být zaměňován se `scriptWitness`. Zatímco `witnessScript` definuje podmínky utrácení UTXO P2WSH nebo P2SH-P2WSH a tvoří samostatný skript, `scriptWitness` obsahuje svědecká data jakéhokoli vstupu SegWit.*