---
term: OP_2 A OP_16 (0X52 A 0X60)
---

Os opcodes de `OP_2` a `OP_16` empurram os respectivos valores numéricos de 2 a 16 para a pilha. Eles são usados para simplificar scripts permitindo a inserção de pequenos valores numéricos. Este tipo de opcode é notavelmente usado em scripts de multisignatura. Aqui está um exemplo de um `scriptPubKey` para uma multisig 2/3:

```text
OP_2
<Chave Pública A>
<Chave Pública B>
<Chave Pública C>
OP_3
OP_CHECKMULTISIG
```

> ► *Todos esses opcodes são às vezes também chamados de OP_PUSHNUM_N.*