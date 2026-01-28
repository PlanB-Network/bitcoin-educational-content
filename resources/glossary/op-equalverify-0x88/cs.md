---
term: OP_EQUALVERIFY (0X88)

definition: Kombinuje OP_EQUAL a OP_VERIFY, čímž zneplatní transakci, pokud se hodnoty liší.
---
Kombinuje funkce `OP_EQUAL` a `OP_VERIFY`. Nejprve zkontroluje rovnost dvou horních hodnot na zásobníku a poté vyžaduje, aby výsledek byl nenulový, jinak je transakce neplatná. funkce `OP_EQUALVERIFY` se používá zejména ve skriptech pro ověřování adres.