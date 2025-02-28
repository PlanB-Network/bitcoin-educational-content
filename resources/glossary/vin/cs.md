---
term: VIN

---
Specifický prvek bitcoinové transakce, který určuje zdroj finančních prostředků použitých k uspokojení výstupů. Každý `vin` odkazuje na nespotřebovaný výstup (UTXO) z předchozí transakce. Transakce může obsahovat více vstupů, z nichž každý je identifikován kombinací `txid` (identifikátor původní transakce) a `vout` (index výstupu v dané transakci).

Každý `vin` obsahuje následující informace:


- `txid`: identifikátor předchozí transakce obsahující výstup, který je zde použit jako vstup;
- `vout`: index výstupu v předchozí transakci;
- `scriptSig` nebo `scriptWitness`: odemykací skript, který poskytuje údaje nezbytné ke splnění podmínek zadaných v `scriptPubKey` předchozí transakce, jejíž prostředky se vynakládají, obvykle poskytnutím kryptografického podpisu;
- `nSequence`: specifické pole, které slouží k určení způsobu, jakým je tento vstup časově uzamčen, a dalších možností, jako je RBF.