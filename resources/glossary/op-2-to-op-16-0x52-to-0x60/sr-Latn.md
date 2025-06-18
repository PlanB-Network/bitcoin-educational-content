---
term: OP_2 DO OP_16 (0X52 DO 0X60)
---

Opcodi od `OP_2` do `OP_16` postavljaju odgovarajuće numeričke vrednosti od 2 do 16 na stek. Koriste se za pojednostavljenje skripti omogućavajući umetanje malih numeričkih vrednosti. Ovaj tip opkoda se naročito koristi u skriptama sa višestrukim potpisima. Evo primera `scriptPubKey` za 2/3 Multisig:


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *Svi ovi opkodi se ponekad nazivaju i OP_PUSHNUM_N.*