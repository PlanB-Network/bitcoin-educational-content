---
term: NULLDUMMY
---

Pravidlo konsensu zavedené s BIP147 v soft forku SegWit, které vyžaduje, aby dummy prvek používaný v opcode `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` byl prázdné pole bajtů (`OP_0`). Toto opatření bylo implementováno za účelem eliminace vektoru proměnlivosti tím, že zakazuje jakoukoli hodnotu jinou než `OP_0` pro tento prvek.