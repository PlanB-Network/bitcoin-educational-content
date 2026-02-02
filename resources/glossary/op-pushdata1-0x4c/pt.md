---
term: OP_PUSHDATA1 (0X4C)

definition: Opcode que insere até 255 bytes de dados na pilha.
---
Empurra uma certa quantidade de dados para a pilha. É seguido por um byte que indica o comprimento dos dados a empurrar (até 255 bytes). Este opcode é utilizado para incluir dados de tamanho variável em scripts.