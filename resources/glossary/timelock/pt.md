---
term: TIMELOCK
---

Um primitivo de contrato inteligente que permite definir uma condição baseada em tempo que deve ser cumprida para que uma transação seja adicionada a um bloco. Existem dois tipos de timelocks no Bitcoin:
* O timelock absoluto, que especifica um momento exato antes do qual a transação não pode ser incluída em um bloco;
* O timelock relativo, que estabelece um atraso a partir da aceitação de uma transação anterior.
O timelock pode ser definido tanto como uma data expressa em tempo Unix quanto como um número de bloco. Finalmente, o timelock pode ser aplicado a uma saída de transação usando um opcode específico no script de bloqueio (`OP_CHECKLOCKTIMEVERIFY` ou `OP_CHECKSEQUENCEVERIFY`), ou a uma transação inteira usando campos específicos da transação (`nLockTime` ou `nSequence`).