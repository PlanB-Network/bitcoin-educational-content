---
term: OP_IF (0X63)
---

Executa a porção seguinte do script se o valor no topo da pilha for não-zero (verdadeiro). Se o valor for zero (falso), essas operações são puladas, movendo diretamente para aquelas após `OP_ELSE`, se estiver presente. `OP_IF` possibilita o lançamento de uma estrutura de controle condicional dentro de um script. Ele determina o fluxo de controle em um script baseado em uma condição fornecida no momento da execução da transação. `OP_IF` é usado com `OP_ELSE` e `OP_ENDIF` da seguinte maneira:

```text
<condição>
OP_IF
<operações se a condição for verdadeira>
OP_ELSE
<operações se a condição for falsa>
OP_ENDIF
```