---
term: OP_HASH160 (0XA9)

definition: Opcode hashující prvek na vrcholu pomocí SHA256 a poté RIPEMD160.
---
Vezme vrchní prvek ze zásobníku a nahradí jej jeho hashem, přičemž současně použije funkce `SHA256` a `RIPEMD160`. Tento dvoufázový proces vytvoří 160bitový otisk prstu.