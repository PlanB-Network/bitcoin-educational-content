---
term: NULLDUMMY
---

Konsensregel, die mit BIP147 im SegWit-Soft-Fork eingeführt wurde und verlangt, dass das Dummy-Element, das in den Opcodes `OP_CHECKMULTISIG` und `OP_CHECKMULTISIGVERIFY` verwendet wird, ein leeres Byte-Array (`OP_0`) sein muss. Diese Maßnahme wurde implementiert, um einen Veränderbarkeitsvektor zu eliminieren, indem jeglicher Wert außer `OP_0` für dieses Element verboten wird.