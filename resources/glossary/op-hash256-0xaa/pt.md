---
term: OP_HASH256 (0XAA)
---

Retira o item do topo da pilha e o substitui pelo seu hash, utilizando a função `SHA256` duas vezes. A entrada é hasheada uma vez com `SHA256`, e então o resumo é hasheado uma segunda vez com `SHA256`. Esse processo de dois passos gera uma impressão digital de 256 bits.