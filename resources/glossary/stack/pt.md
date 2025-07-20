---
term: BATERIA
---

No contexto da linguagem de scripting utilizada para associar condições de despesa a UTXOs Bitcoin, a pilha é uma estrutura de dados LIFO (*Last In, First Out*) utilizada para armazenar Elements temporários durante a execução do script. Cada operação no script manipula estas pilhas, onde o Elements pode ser adicionado (*push*) ou removido (*pop*). Os scripts utilizam pilhas para avaliar expressões, armazenar variáveis temporárias e gerir condições.


Ao executar um script Bitcoin, 2 pilhas podem ser usadas: a pilha principal e a pilha alt (alternativa). A pilha principal é utilizada para a maioria das operações de script. É nesta pilha que as operações de script adicionam, removem ou manipulam dados. A pilha alternativa, por outro lado, é usada para armazenar temporariamente dados durante a execução do script. Códigos de operação específicos, como `OP_TOALTSTACK` e `OP_FROMALTSTACK`, permitem transferir Elements da pilha principal para a pilha alternativa e vice-versa.


Por exemplo, quando uma transação é validada, as assinaturas e as chaves públicas são colocadas na pilha principal e processadas por opcodes sucessivos para verificar se as assinaturas correspondem às chaves e aos dados da transação.