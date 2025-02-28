---
term: OP_2 AŽ OP_16 (0X52 AŽ 0X60)

---
Opkódy od `OP_2` do `OP_16` přenesou na zásobník příslušné číselné hodnoty 2 až 16. Používají se pro zjednodušení skriptů tím, že umožňují vkládání malých číselných hodnot. Tento typ opkódů se používá zejména ve víceznakových skriptech. Zde je příklad `scriptPubKey` pro multisignály 2/3:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Všechny tyto opkódy se někdy nazývají také OP_PUSHNUM_N.*