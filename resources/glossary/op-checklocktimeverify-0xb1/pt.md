---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Torna a transação inválida, a menos que todas estas condições sejam cumpridas:


- A pilha não está vazia;
- O valor no topo da pilha é maior ou igual a `0`;
- O tipo de timelock é o mesmo entre o campo `nLockTime` e o valor no topo da pilha (tempo real ou número de bloco);
- O campo `nSequence` da entrada não é igual a `0xffffffff`;
- O valor no topo da pilha é maior ou igual ao valor do campo `nLockTime` da transação.

Se qualquer uma destas condições não for satisfeita, o script que contém o `OP_CHECKLOCKTIMEVERIFY` não pode ser satisfeito. Se todas estas condições forem válidas, então `OP_CHECKLOCKTIMEVERIFY` actua como um `OP_NOP`, o que significa que não executa qualquer ação no script. É como se ele desaparecesse. o `OP_CHECKLOCKTIMEVERIFY` impõe, portanto, uma restrição de tempo sobre o gasto do UTXO protegido com o script que o contém. Ele pode fazer isso tanto na forma de uma data de tempo Unix ou como um número de bloco. Para isso, restringe os valores possíveis para o campo `nLockTime` da transação que o gasta, e esse próprio campo `nLockTime` restringe quando a transação pode ser incluída em um bloco.

> ► *Este opcode é um substituto do `OP_NOP`. Foi colocado no `OP_NOP2`. É frequentemente referido pelo seu acrónimo "CLTV". Nota, `OP_CLTV` não deve ser confundido com o campo `nLockTime` de uma transação. O primeiro utiliza o segundo, mas a sua natureza e ação são diferentes.*