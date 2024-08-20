---
term: OP_PUSHDATA2 (0X4D)
---

Permite empurrar uma grande quantidade de dados para a pilha. É seguido por dois bytes (little-endian) que especificam o comprimento dos dados a serem empurrados (até cerca de 65 KB). É usado para inserir dados maiores em scripts.