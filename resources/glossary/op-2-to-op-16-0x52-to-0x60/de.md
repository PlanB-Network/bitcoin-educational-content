---
term: OP_2 BIS OP_16 (0X52 BIS 0X60)

---
Die Opcodes von `OP_2` bis `OP_16` schieben die jeweiligen Zahlenwerte von 2 bis 16 auf den Stack. Sie werden verwendet, um Skripte zu vereinfachen, indem sie das Einfügen kleiner numerischer Werte ermöglichen. Diese Art von Opcode wird vor allem in Skripten mit mehreren Unterschriften verwendet. Hier ist ein Beispiel für einen `scriptPubKey` für eine 2/3-Multisig:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Alle diese Opcodes werden manchmal auch als OP_PUSHNUM_N bezeichnet