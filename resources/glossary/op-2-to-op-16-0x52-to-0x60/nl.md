---
term: OP_2 TOT OP_16 (0X52 TOT 0X60)
definition: Opcodes die numerieke waarden van 2 tot 16 op de stack plaatsen.
---

De opcodes van `OP_2` tot `OP_16` duwen de respectievelijke numerieke waarden van 2 tot 16 op de stack. Ze worden gebruikt om scripts te vereenvoudigen door het invoegen van kleine numerieke waarden toe te staan. Dit type opcode wordt vooral gebruikt in scripts met meerdere handtekeningen. Hier is een voorbeeld van een `scriptPubKey` voor een 2/3 Multisig:


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *Al deze opcodes worden soms ook OP_PUSHNUM_N.* genoemd