---
term: NLOCKTIME
---

Um campo embutido em transações que estabelece uma condição baseada em tempo antes da qual a transação não pode ser adicionada a um bloco válido. Este parâmetro permite especificar um tempo exato (timestamp Unix) ou um número específico de blocos como condição para que a transação seja considerada válida. Assim, é um bloqueio de tempo absoluto (não relativo). O `nLockTime` afeta toda a transação e efetivamente habilita a verificação de tempo, enquanto o opcode `OP_CHECKLOCKTIMEVERIFY` apenas permite comparar o valor do topo da pilha com o valor de `nLockTime`.