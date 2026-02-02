---
term: OP_2 TILL OP_16 (0X52 TILL 0X60)
definition: Opcodes som lägger numeriska värden från 2 till 16 på stacken.
---

Opkoderna från `OP_2` till `OP_16` lägger respektive numeriska värden från 2 till 16 på stacken. De används för att förenkla skript genom att göra det möjligt att infoga små numeriska värden. Den här typen av opkoder används framför allt i skript med flera signaturer. Här är ett exempel på en `scriptPubKey` för en 2/3 Multisig:


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *Alla dessa opkoder kallas ibland också OP_PUSHNUM_N.*