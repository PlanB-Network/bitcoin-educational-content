---
term: OP_IF (0X63)

---
Executa a seguinte parte do script se o valor no topo da pilha for diferente de zero (verdadeiro). Se o valor for zero (falso), estas operações são ignoradas, passando diretamente para as que se seguem a `OP_ELSE`, se esta estiver presente. `OP_IF` permite o lançamento de uma estrutura de controle condicional dentro de um script. Ela determina o fluxo de controle em um script com base em uma condição fornecida no momento da execução da transação. `OP_IF` é utilizado com `OP_ELSE` e `OP_ENDIF` da seguinte forma:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```