---
term: OP_SUCCESS

---
O `OP_SUCCESS` representa uma série de opcodes que foram desativados no passado e agora estão reservados para uso futuro no Tapscript. O seu objetivo final é facilitar actualizações e extensões da linguagem de script, permitindo a introdução de novas funcionalidades através de soft forks. Quando um destes opcodes é encontrado num script, indica um sucesso automático dessa parte do script, independentemente dos dados ou condições presentes. Isto significa que o script continua a sua execução sem falhas, independentemente das operações anteriores.

Assim, quando um novo opcode é adicionado a um `OP_SUCCESS`, ele representa necessariamente a adição de uma regra mais restritiva que a anterior. Os nós actualizados podem então verificar o cumprimento desta regra, e os nós não actualizados não recusarão as transacções associadas e os blocos que as incluem, porque o `OP_SUCCESS` valida essa parte do script. Portanto, não há hard fork.

Em comparação, os `OP_NOP` (*No Operation*) também servem como espaços reservados no script, mas não têm qualquer efeito na execução do script. Quando um `OP_NOP` é encontrado, o script simplesmente continua sem alterar o estado da pilha ou a progressão do script. A diferença chave, portanto, está no seu impacto na execução: `OP_SUCCESS` garante uma passagem bem sucedida através daquela parte do script, enquanto `OP_NOP` é neutro, e não afeta nem a pilha nem o fluxo do script. Estes opcodes são designados por `OP_SUCCESSN` onde `N` é um número utilizado para diferenciar o `OP_SUCCESS`.