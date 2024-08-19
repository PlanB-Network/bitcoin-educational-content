---
termine: OP_2 A OP_16 (0X52 A 0X60)
---

Gli opcode da `OP_2` a `OP_16` inseriscono nello stack i rispettivi valori numerici da 2 a 16. Sono utilizzati per semplificare gli script permettendo l'inserimento di piccoli valori numerici. Questo tipo di opcode è notevolmente utilizzato negli script multisignature. Ecco un esempio di `scriptPubKey` per una multisig 2/3:

```text
OP_2
<Chiave Pubblica A>
<Chiave Pubblica B>
<Chiave Pubblica C>
OP_3
OP_CHECKMULTISIG
```

> ► *Tutti questi opcode sono talvolta chiamati anche OP_PUSHNUM_N.*