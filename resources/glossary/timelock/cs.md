---
term: TIMELOCK

---
Primitivum chytré smlouvy, které umožňuje nastavit časovou podmínku, která musí být splněna, aby byla transakce přidána do bloku. V Bitcoinu existují dva typy časových zámků:


- Absolutní časový zámek, který určuje přesný okamžik, před kterým nemůže být transakce zařazena do bloku;
- Relativní časový zámek, který nastavuje zpoždění od přijetí předchozí transakce.

Časový zámek lze definovat buď jako datum vyjádřené v čase systému Unix, nebo jako číslo bloku. Časový zámek se může vztahovat na výstup transakce pomocí specifického opkódu v zamykacím skriptu (`OP_CHECKLOCKTIMEVERIFY` nebo `OP_CHECKSEQUENCEVERIFY`) nebo na celou transakci pomocí specifických polí transakce (`nLockTime` nebo `nSequence`).