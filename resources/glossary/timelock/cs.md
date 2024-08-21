---
term: TIMELOCK
---

Jedná se o primitivní funkci chytrého kontraktu, která umožňuje nastavit časovou podmínku, která musí být splněna, aby byla transakce přidána do bloku. Na Bitcoinu existují dva typy timelocků:
* Absolutní timelock, který určuje přesný okamžik, před kterým nemůže být transakce zařazena do bloku;
* Relativní timelock, který nastavuje zpoždění od přijetí předchozí transakce.
Timelock může být definován buď jako datum vyjádřené v Unixovém čase, nebo jako číslo bloku. Nakonec může být timelock aplikován na výstup transakce použitím specifického operačního kódu ve skriptu pro uzamčení (`OP_CHECKLOCKTIMEVERIFY` nebo `OP_CHECKSEQUENCEVERIFY`), nebo na celou transakci použitím specifických polí transakce (`nLockTime` nebo `nSequence`).