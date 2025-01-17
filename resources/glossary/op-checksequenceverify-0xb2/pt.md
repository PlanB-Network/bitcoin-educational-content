---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Torna a transação inválida se for observada qualquer uma destas caraterísticas:


- A pilha está vazia;
- O valor no topo da pilha é menor que `0`;
- A flag de desativação do valor no topo da pilha é indefinida e; A versão da transação é inferior a `2` ou; A flag de desativação do campo `nSequence` da entrada é definida ou; O tipo de timelock não é o mesmo entre o campo `nSequence` e o valor no topo da pilha (tempo real ou número de blocos) ou; O valor no topo da pilha é superior ao valor do campo `nSequence` da entrada.

Se uma ou mais destas caraterísticas for observada, o script que contém o `OP_CHECKSEQUENCEVERIFY` não pode ser satisfeito. Se todas as condições forem válidas, então `OP_CHECKSEQUENCEVERIFY` actua como um `OP_NOP`, o que significa que não executa qualquer ação no script. É como se ele desaparecesse. o `OP_CHECKSEQUENCEVERIFY` impõe assim uma restrição de tempo relativa ao gasto do UTXO protegido com o script que o contém. Pode fazê-lo quer sob a forma de tempo real, quer sob a forma de um número de blocos. Para tal, restringe os valores possíveis para o campo `nSequence` da entrada que o gasta, e este campo `nSequence` restringe ele próprio quando a transação que inclui esta entrada pode ser incluída num bloco.

> ► *Este opcode é um substituto do `OP_NOP`. Foi colocado no `OP_NOP3`. É frequentemente referido pelo seu acrónimo "CSV". Nota, `OP_CSV` não deve ser confundido com o campo `nSequence` de uma transação. O primeiro utiliza o segundo, mas as suas naturezas e acções são diferentes.*