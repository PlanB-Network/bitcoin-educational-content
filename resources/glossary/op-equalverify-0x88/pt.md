---
term: OP_EQUALVERIFY (0X88)

---
Combina as funções de `OP_EQUAL` e `OP_VERIFY`. Primeiro verifica a igualdade dos dois primeiros valores na pilha, depois exige que o resultado seja diferente de zero, caso contrário, a transação é inválida. o `OP_EQUALVERIFY` é utilizado principalmente em scripts de verificação de endereços.