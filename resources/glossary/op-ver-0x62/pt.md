---
term: OP_VER (0X62)

definition: Opcode desativado que inseria a versão do cliente, convertido em OP_SUCCESS.
---
Permitia colocar a versão do cliente na pilha. Este opcode foi desabilitado porque se tivesse sido usado, cada atualização teria levado a um hard fork. BIP342 modificou este opcode para `OP_SUCCESS`.