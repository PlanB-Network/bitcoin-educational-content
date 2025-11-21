---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Kombinuje `OP_CHECKMULTISIG` i `OP_VERIFY`. Uzima više potpisa i javnih ključeva kako bi proverio da li je `M` od `N` potpisa validno, baš kao što to radi `OP_CHECKMULTISIG`. Zatim, kao `OP_VERIFY`, ako provera ne uspe, skripta se odmah zaustavlja sa greškom. Ako je provera uspešna, skripta se nastavlja bez dodavanja bilo kakve vrednosti na stek. Ovaj opcode je uklonjen u Tapscript-u.