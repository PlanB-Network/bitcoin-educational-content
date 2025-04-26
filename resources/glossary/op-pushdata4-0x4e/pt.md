---
term: OP_PUSHDATA4 (0X4E)

---
Permite colocar uma quantidade muito grande de dados na pilha. É seguido por quatro bytes (little-endian) que indicam o comprimento dos dados a empurrar (até cerca de 4,3 GB). Este opcode é usado para inserir dados muito grandes em scripts, embora seu uso seja extremamente raro devido a limitações práticas no tamanho da transação.