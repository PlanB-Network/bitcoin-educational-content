---
term: OP_EQUALVERIFY (0X88)
definition: Kombinuje OP_EQUAL i OP_VERIFY, poništavajući transakciju ako se vrednosti razlikuju.
---

Kombinuje funkcije `OP_EQUAL` i `OP_VERIFY`. Prvo proverava jednakost dveju gornjih vrednosti na steku, zatim zahteva da rezultat bude različit od nule, u suprotnom, transakcija je nevažeća. `OP_EQUALVERIFY` se posebno koristi u Address verifikacionim skriptama.