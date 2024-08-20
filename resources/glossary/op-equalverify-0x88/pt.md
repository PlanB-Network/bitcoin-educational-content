---
term: OP_EQUALVERIFY (0X88)
---

Combina as funções de `OP_EQUAL` e `OP_VERIFY`. Primeiro, verifica a igualdade dos dois valores superiores na pilha, depois exige que o resultado seja não-zero, caso contrário, a transação é inválida. `OP_EQUALVERIFY` é notavelmente usado em scripts de verificação de endereço.