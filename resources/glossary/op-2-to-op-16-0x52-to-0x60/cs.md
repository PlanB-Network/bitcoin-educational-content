---
term: OP_2 DO OP_16 (0X52 DO 0X60)
---

Opcodes od `OP_2` do `OP_16` vkládají na zásobník odpovídající číselné hodnoty od 2 do 16. Používají se pro zjednodušení skriptů tím, že umožňují vložení malých číselných hodnot. Tento typ opcode je významně používán v multisignaturních skriptech. Zde je příklad `scriptPubKey` pro 2/3 multisig:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Všechny tyto opcodes jsou někdy také nazývány OP_PUSHNUM_N.*