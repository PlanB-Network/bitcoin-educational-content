---
term: OP_2 KUNI OP_16 (0X52 KUNI 0X60)
---

Opcodes alates `OP_2` kuni `OP_16` lükkavad vastavad numbrilised väärtused 2 kuni 16 virna (stack) peale. Neid kasutatakse skriptide lihtsustamiseks, võimaldades väikeste numbriliste väärtuste sisestamist. Sellist tüüpi opcode'i kasutatakse märkimisväärselt multisignatuuri skriptides. Siin on näide `scriptPubKey`st 2/3 multisig jaoks:

```text
OP_2
<Avalik Võti A>
<Avalik Võti B>
<Avalik Võti C>
OP_3
OP_CHECKMULTISIG
```

> ► *Kõiki neid opkoode nimetatakse mõnikord ka OP_PUSHNUM_N.*