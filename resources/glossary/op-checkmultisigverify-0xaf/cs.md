---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Kombinuje `OP_CHECKMULTISIG` a `OP_VERIFY`. K ověření platnosti `M` z `N` podpisů se použije více podpisů a veřejných klíčů, stejně jako to dělá `OP_CHECKMULTISIG`. Pak, stejně jako `OP_VERIFY`, pokud ověření selže, skript se okamžitě zastaví s chybou. Pokud je ověření úspěšné, skript pokračuje, aniž by na zásobník vložil nějakou hodnotu. Tento opkód byl v Tapscriptu odstraněn.