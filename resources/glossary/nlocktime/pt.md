---
term: NLOCKTIME

---
Um campo incorporado nas transacções que define uma condição baseada no tempo antes da qual a transação não pode ser adicionada a um bloco válido. Este parâmetro permite especificar uma hora exacta (Unix timestamp) ou um número específico de blocos como condição para que a transação seja considerada válida. Portanto, é um timelock absoluto (não relativo). O `nLockTime` afeta toda a transação e efetivamente permite a verificação do tempo, enquanto o opcode `OP_CHECKLOCKTIMEVERIFY` permite apenas comparar o valor do topo da pilha com o valor do `nLockTime`.