---
term: EMPILHAR

---
No contexto da linguagem de script utilizada para aplicar condições de despesa em Bitcoin UTXOs, a pilha é uma estrutura de dados "LIFO" (*Last In, First Out*) que serve para armazenar elementos temporários durante a execução de um script. Cada operação no script manipula estas pilhas, onde os elementos podem ser adicionados (*push*) ou removidos (*pop*). Os scripts utilizam pilhas para avaliar expressões, armazenar variáveis temporárias e gerir condições.

Durante a execução de um script Bitcoin, 2 pilhas podem ser usadas: a pilha principal e a pilha alt (alternativa). A pilha principal é usada para a maioria das operações de um script. É nesta pilha que as operações do script adicionam, removem ou manipulam dados. A pilha alternativa, por outro lado, serve para armazenar dados temporariamente durante a execução do script. Códigos de operação específicos, como `OP_TOALTSTACK` e `OP_FROMALTSTACK`, permitem a transferência de elementos da pilha principal para a pilha alternativa e vice-versa.

Por exemplo, durante a validação de uma transação, as assinaturas e as chaves públicas são colocadas na pilha principal e processadas por opcodes sucessivos para verificar se as assinaturas correspondem às chaves e aos dados da transação.

> ► *Em inglês, a tradução de "pile" é "pilha". O termo inglês é geralmente utilizado, mesmo em francês, durante as discussões técnicas