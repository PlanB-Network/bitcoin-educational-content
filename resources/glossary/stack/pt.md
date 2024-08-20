---
termo: STACK
---

No contexto da linguagem de script usada para aplicar condições de gasto em UTXOs do Bitcoin, a pilha é uma estrutura de dados "LIFO" (*Last In, First Out* ou *Último a Entrar, Primeiro a Sair*) que serve para armazenar elementos temporários durante a execução de um script. Cada operação no script manipula essas pilhas, onde elementos podem ser adicionados (*push*) ou removidos (*pop*). Scripts usam pilhas para avaliar expressões, armazenar variáveis temporárias e gerenciar condições.

Durante a execução de um script Bitcoin, 2 pilhas podem ser usadas: a pilha principal e a pilha alt (alternativa). A pilha principal é usada para a maioria das operações de um script. É nesta pilha que as operações do script adicionam, removem ou manipulam dados. A pilha alternativa, por outro lado, serve para armazenar temporariamente dados durante a execução do script. Opcodes específicos, como `OP_TOALTSTACK` e `OP_FROMALTSTACK`, permitem a transferência de elementos da pilha principal para a pilha alternativa e vice-versa.

Por exemplo, durante a validação de uma transação, assinaturas e chaves públicas são adicionadas à pilha principal e processadas por opcodes sucessivos para verificar se as assinaturas correspondem às chaves e aos dados da transação.

> ► *Em inglês, a tradução de « pile » é « stack ». O termo em inglês é geralmente usado mesmo em francês durante discussões técnicas.*