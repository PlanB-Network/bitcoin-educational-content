---
term: OP_PUSHDATA4 (0X4E)
---

Permite empurrar uma quantidade muito grande de dados para a pilha. É seguido por quatro bytes (little-endian) que indicam o comprimento dos dados a serem empurrados (até cerca de 4,3 GB). Este opcode é usado para inserir dados muito grandes em scripts, embora seu uso seja extremamente raro devido a limitações práticas no tamanho da transação.