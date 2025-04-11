---
term: OP_2 A OP_16 (0X52 A 0X60)

---
Los opcodes de `OP_2` a `OP_16` empujan los respectivos valores numéricos de 2 a 16 a la pila. Se utilizan para simplificar los scripts permitiendo la inserción de valores numéricos pequeños. Este tipo de opcode se utiliza sobre todo en los scripts multifirma. He aquí un ejemplo de `scriptPubKey` para un multisig 2/3:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Todos estos opcodes se denominan a veces también OP_PUSHNUM_N.*