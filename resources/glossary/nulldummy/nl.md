---
term: NULLDUMMY
---

Consensusregel geïntroduceerd met BIP147 in de SegWit Soft Fork die vereist dat het dummy-element gebruikt in de `OP_CHECKMULTISIG` en `OP_CHECKMULTISIGVERIFY` opcodes een lege byte-array is (`OP_0`). Deze maatregel is geïmplementeerd om een vector van manipuleerbaarheid te elimineren door elke andere waarde dan `OP_0` voor dit element te verbieden.