---
term: OP_2 A OP_16 (0X52 A 0X60)

---
Os códigos de operação de `OP_2` a `OP_16` empurram os respectivos valores numéricos de 2 a 16 para a pilha. São utilizados para simplificar os scripts, permitindo a inserção de pequenos valores numéricos. Este tipo de opcode é utilizado nomeadamente em scripts com várias assinaturas. Aqui está um exemplo de um `scriptPubKey` para um multisig 2/3:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Todos estes opcodes são por vezes também designados por OP_PUSHNUM_N.*