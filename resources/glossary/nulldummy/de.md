---
term: NULLDUMMY

---
Mit BIP147 in der SegWit-Soft-Fork eingeführte Konsensregel, die verlangt, dass das in den Opcodes `OP_CHECKMULTISIG` und `OP_CHECKMULTISIGVERIFY` verwendete Dummy-Element ein leeres Byte-Array (`OP_0`) ist. Diese Maßnahme wurde eingeführt, um einen Vektor der Fehlbarkeit zu eliminieren, indem jeder andere Wert als `OP_0` für dieses Element verboten wird.