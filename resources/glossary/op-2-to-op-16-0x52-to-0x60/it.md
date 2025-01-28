---
term: DA OP_2 A OP_16 (DA 0X52 A 0X60)

---
Gli opcode da `OP_2` a `OP_16` inseriscono i rispettivi valori numerici da 2 a 16 nello stack. Vengono utilizzati per semplificare gli script consentendo l'inserimento di piccoli valori numerici. Questo tipo di opcode è particolarmente utilizzato negli script a più firme. Ecco un esempio di `scriptPubKey` per una multi-firma 2/3:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Tutti questi codici operazionali sono talvolta chiamati anche OP_PUSHNUM_N