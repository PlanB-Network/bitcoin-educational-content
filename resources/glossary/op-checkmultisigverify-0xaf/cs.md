---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Kombinuje `OP_CHECKMULTISIG` a `OP_VERIFY`. Vyžaduje více podpisů a veřejných klíčů k ověření, že `M` z `N` podpisů jsou platné, stejně jako to dělá `OP_CHECKMULTISIG`. Poté, podobně jako `OP_VERIFY`, pokud ověření selže, skript okamžitě skončí s chybou. Pokud je ověření úspěšné, skript pokračuje bez toho, aby na zásobník vložil jakoukoliv hodnotu. Tento operační kód byl odstraněn v Tapscript.