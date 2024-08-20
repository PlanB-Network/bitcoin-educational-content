---
term: OP_SUCCESS
---

O `OP_SUCCESS` representa uma série de opcodes que foram desativados no passado e agora estão reservados para uso futuro no Tapscript. Seu objetivo final é facilitar atualizações e extensões da linguagem de script, permitindo a introdução de novas funcionalidades via soft forks. Quando um desses opcodes é encontrado em um script, indica um sucesso automático dessa parte do script, independentemente dos dados ou condições presentes. Isso significa que o script continua sua execução sem falhas, independente das operações anteriores.

Assim, quando um novo opcode é adicionado em um `OP_SUCCESS`, ele necessariamente representa a adição de uma regra mais restritiva do que a anterior. Nós atualizados podem então verificar a conformidade com esta regra, e nós não atualizados não recusarão as transações associadas e os blocos que as incluem, porque o `OP_SUCCESS` valida aquela parte do script. Portanto, não há hard fork.

Em comparação, o `OP_NOP` (*No Operation*) também serve como placeholders no script, mas eles não têm efeito sobre a execução do script. Quando um `OP_NOP` é encontrado, o script simplesmente continua sem alterar o estado da pilha ou a progressão do script. A diferença chave, portanto, está no impacto sobre a execução: `OP_SUCCESS` garante uma passagem bem-sucedida por aquela porção do script, enquanto `OP_NOP` é neutro e não afeta nem a pilha nem o fluxo do script. Esses opcodes são designados por `OP_SUCCESSN` onde `N` é um número usado para diferenciar o `OP_SUCCESS`.