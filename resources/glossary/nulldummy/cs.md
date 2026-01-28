---
term: Nulldummy

definition: Pravidlo vyžadující, aby fiktivní prvek v OP_CHECKMULTISIG byl prázdným polem bajtů.
---
Pravidlo konsensu zavedené s BIP147 v soft forku SegWit, které vyžaduje, aby fiktivní prvek použitý v opkódech `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` byl prázdné pole bajtů (`OP_0`). Toto opatření bylo zavedeno za účelem eliminace vektoru ovlivnitelnosti tím, že pro tento prvek zakazuje jakoukoli jinou hodnotu než `OP_0`.