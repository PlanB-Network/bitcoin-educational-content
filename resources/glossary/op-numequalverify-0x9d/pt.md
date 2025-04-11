---
term: OP_NUMEQUALVERIFY (0X9D)

---
Combina as operações `OP_NUMEQUAL` e `OP_VERIFY`. Compara numericamente os dois elementos mais altos da pilha. Se os valores forem iguais, `OP_NUMEQUALVERIFY` remove o resultado verdadeiro da pilha e continua a execução do script. Se os valores não forem iguais, o resultado é falso, e o script falha imediatamente.