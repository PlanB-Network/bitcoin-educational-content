---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Torna a transação inválida a menos que todas estas condições sejam atendidas:
* A pilha não está vazia;
* O valor no topo da pilha é maior ou igual a `0`;
* O tipo de bloqueio temporal é o mesmo entre o campo `nLockTime` e o valor no topo da pilha (tempo real ou número do bloco);
* O campo `nSequence` da entrada não é igual a `0xffffffff`;
* O valor no topo da pilha é maior ou igual ao valor do campo `nLockTime` da transação.

Se qualquer uma dessas condições não for atendida, o script contendo o `OP_CHECKLOCKTIMEVERIFY` não pode ser satisfeito. Se todas essas condições forem válidas, então `OP_CHECKLOCKTIMEVERIFY` age como um `OP_NOP`, significando que não realiza nenhuma ação no script. É como se ele desaparecesse. `OP_CHECKLOCKTIMEVERIFY` impõe assim uma restrição temporal no gasto do UTXO assegurado com o script que o contém. Isso pode ser feito tanto na forma de uma data de tempo Unix quanto como um número de bloco. Para fazer isso, restringe os valores possíveis para o campo `nLockTime` da transação que o gasta, e este campo `nLockTime` por si só restringe quando a transação pode ser incluída em um bloco.

> ► *Este opcode é um substituto para `OP_NOP`. Foi colocado em `OP_NOP2`. É frequentemente referido pela sua sigla "CLTV". Note, `OP_CLTV` não deve ser confundido com o campo `nLockTime` de uma transação. O primeiro utiliza o último, mas suas naturezas e ações são diferentes.*