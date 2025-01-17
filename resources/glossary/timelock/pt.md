---
term: TIMELOCK

---
Uma primitiva de contrato inteligente que permite definir uma condição baseada no tempo que deve ser cumprida para que uma transação seja adicionada a um bloco. Existem dois tipos de timelocks no Bitcoin:


- O timelock absoluto, que especifica um momento exato antes do qual a transação não pode ser incluída num bloco;
- O timelock relativo, que define um atraso a partir da aceitação de uma transação anterior.

O timelock pode ser definido como uma data expressa em tempo Unix ou como um número de bloco. Finalmente, o timelock pode ser aplicado a uma saída de transação utilizando um opcode específico no script de bloqueio (`OP_CHECKLOCKTIMEVERIFY` ou `OP_CHECKSEQUENCEVERIFY`), ou a uma transação inteira utilizando campos de transação específicos (`nLockTime` ou `nSequence`).