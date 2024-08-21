---
term: VIN
---

Specifický prvek Bitcoinové transakce, který specifikuje zdroj finančních prostředků použitých k pokrytí výstupů. Každý `vin` odkazuje na nespotřebovaný výstup (UTXO) z předchozí transakce. Transakce může obsahovat více vstupů, každý identifikovaný kombinací `txid` (identifikátor původní transakce) a `vout` (index výstupu v této transakci).

Každý `vin` obsahuje následující informace:
* `txid`: identifikátor předchozí transakce obsahující výstup použitý zde jako vstup;
* `vout`: index výstupu v předchozí transakci;
* `scriptSig` nebo `scriptWitness`: odemykací skript, který poskytuje nezbytná data k splnění podmínek stanovených `scriptPubKey` předchozí transakce, jejíž prostředky jsou vynakládány, obvykle poskytnutím kryptografického podpisu;
* `nSequence`: specifické pole používané k indikaci, jak je tento vstup časově uzamčen, stejně jako další možnosti, jako je RBF.