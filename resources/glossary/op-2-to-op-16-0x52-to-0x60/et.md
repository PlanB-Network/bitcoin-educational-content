---
term: OP_2 KUNI OP_16 (0X52 KUNI 0X60)

---
Operatsioonikoodid `OP_2` kuni `OP_16` lükkavad virna vastavad arvväärtused 2 kuni 16. Neid kasutatakse skriptide lihtsustamiseks, võimaldades väikeste arvväärtuste sisestamist. Seda tüüpi opkoode kasutatakse eelkõige mitme allkirjaga skriptides. Siin on näide `scriptPubKey`st 2/3 multisignatuuri jaoks:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Kõiki neid opkoode nimetatakse mõnikord ka OP_PUSHNUM_N.*