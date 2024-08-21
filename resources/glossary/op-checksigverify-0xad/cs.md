---
term: OP_CHECKSIGVERIFY (0XAD)
---

Provádí stejnou operaci jako `OP_CHECKSIG`, ale pokud ověření podpisu selže, skript okamžitě skončí s chybou a transakce je tím pádem neplatná. Pokud ověření uspěje, skript pokračuje bez toho, aby na zásobník vložil hodnotu `1` (pravda). Shrnutí, `OP_CHECKSIGVERIFY` provádí operaci `OP_CHECKSIG` následovanou `OP_VERIFY`. Tento operační kód byl v Tapscriptu modifikován pro ověření Schnorrůvých podpisů.