---
term: OP_CHECKSIGVERIFY (0XAD)

definition: Kombinuje OP_CHECKSIG a OP_VERIFY, přičemž zastaví skript, pokud je podpis neplatný.
---
Provede stejnou operaci jako `OP_CHECKSIG`, ale pokud ověření podpisu selže, skript se okamžitě zastaví s chybou a transakce je tak neplatná. Pokud ověření proběhne úspěšně, skript pokračuje, aniž by na zásobník vložil hodnotu `1` (true). Shrnuto, `OP_CHECKSIGVERIFY` provede operaci `OP_CHECKSIG` následovanou `OP_VERIFY`. Tento opkód byl v Tapscriptu upraven pro ověřování Schnorrových podpisů.