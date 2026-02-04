---
term: OP_EVAL

definition: Opcode proposto em 2011 e abandonado, eventualmente substituído por P2SH.
---
Opcode proposto por Gavin Andresen em 2011. Ele pega o script localizado no topo da pilha, executa-o como se fosse parte do `scriptPubKey`, e coloca seu resultado na pilha. o `OP_EVAL` foi abandonado devido a preocupações relacionadas à complexidade deste opcode, que eventualmente seria substituído pelo P2SH.