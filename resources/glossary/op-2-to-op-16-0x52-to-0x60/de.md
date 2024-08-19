---
term: OP_2 BIS OP_16 (0X52 BIS 0X60)
---

Die Opcodes von `OP_2` bis `OP_16` legen die jeweiligen numerischen Werte von 2 bis 16 auf den Stack. Sie werden verwendet, um Skripte zu vereinfachen, indem sie das Einfügen kleiner numerischer Werte ermöglichen. Diese Art von Opcode wird insbesondere in Multisignatur-Skripten verwendet. Hier ist ein Beispiel für ein `scriptPubKey` für ein 2/3 Multisig:

```text
OP_2
<Öffentlicher Schlüssel A>
<Öffentlicher Schlüssel B>
<Öffentlicher Schlüssel C>
OP_3
OP_CHECKMULTISIG
```

> ► *All diese Opcodes werden manchmal auch OP_PUSHNUM_N genannt.*