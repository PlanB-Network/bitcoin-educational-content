---
term: OP_2 A OP_16 (0X52 A 0X60)
---

Los opcodes de `OP_2` a `OP_16` empujan los respectivos valores numéricos de 2 a 16 en la pila. Se utilizan para simplificar scripts permitiendo la inserción de pequeños valores numéricos. Este tipo de opcode se utiliza notablemente en scripts de multisignatura. Aquí hay un ejemplo de un `scriptPubKey` para una multisig 2/3:

```text
OP_2
<Clave Pública A>
<Clave Pública B>
<Clave Pública C>
OP_3
OP_CHECKMULTISIG
```

> ► *Todos estos opcodes a veces también se llaman OP_PUSHNUM_N.*