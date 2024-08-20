---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Torna a transação inválida se qualquer uma destas características for observada:
* A pilha está vazia;
* O valor no topo da pilha é menor que `0`;
* A bandeira de desativação para o valor no topo da pilha é indefinida e; A versão da transação é menor que `2` ou; A bandeira de desativação para o campo `nSequence` da entrada está definida ou; O tipo de bloqueio temporal não é o mesmo entre o campo `nSequence` e o valor no topo da pilha (tempo real ou número de blocos) ou; O valor no topo da pilha é maior que o valor do campo `nSequence` da entrada.

Se uma ou mais destas características for observada, o script contendo o `OP_CHECKSEQUENCEVERIFY` não pode ser satisfeito. Se todas as condições forem válidas, então `OP_CHECKSEQUENCEVERIFY` age como um `OP_NOP`, significando que não realiza nenhuma ação no script. É como se ele desaparecesse. `OP_CHECKSEQUENCEVERIFY` impõe assim uma restrição de tempo relativo ao gasto do UTXO segurado com o script que o contém. Isso pode ser feito tanto na forma de tempo real quanto como um número de blocos. Para fazer isso, restringe os valores possíveis para o campo `nSequence` da entrada que o gasta, e este campo `nSequence` por si só restringe quando a transação que inclui esta entrada pode ser incluída em um bloco.

> ► *Este opcode é um substituto para `OP_NOP`. Foi colocado em `OP_NOP3`. É frequentemente referido pela sua sigla "CSV". Note, `OP_CSV` não deve ser confundido com o campo `nSequence` de uma transação. O primeiro utiliza o último, mas suas naturezas e ações são diferentes.*