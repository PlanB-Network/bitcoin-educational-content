---
term: OP_2 TIL OP_16 (0X52 TIL 0X60)

---
Opkodene fra `OP_2` til `OP_16` skyver de respektive tallverdiene fra 2 til 16 opp på stakken. De brukes til å forenkle skript ved å tillate innsetting av små numeriske verdier. Denne typen opkoder brukes særlig i skript med flere signaturer. Her er et eksempel på en `scriptPubKey` for en 2/3 multisignatur:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Alle disse opkodene kalles noen ganger også OP_PUSHNUM_N