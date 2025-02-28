---
term: OP_NOP (0X61)

---
Não produz qualquer efeito na pilha ou no estado do script. Ele não executa nenhum movimento, verificação ou modificação. Ele simplesmente não faz nada, a menos que seja decidido de outra forma através de um soft fork. De fato, desde sua modificação por Satoshi Nakamoto em 2010, os comandos `OP_NOP` (`OP_NOP1` (`0XB0`) a `OP_NOP10` (`0XB9`)) são usados para adicionar novos opcodes na forma de um soft fork.

Assim, `OP_NOP2` (`0XB1`) e `OP_NOP3` (`0XB2`) já foram utilizados para implementar `OP_CHECKLOCKTIMEVERIFY` e `OP_CHECKSEQUENCEVERIFY`, respetivamente. São utilizados em combinação com `OP_DROP` para remover os valores temporais associados da pilha, permitindo assim que a execução do script continue, quer o nó esteja atualizado ou não. Os comandos `OP_NOP`, portanto, permitem a inserção de um ponto de interrupção em um script para verificar condições adicionais que já existem ou podem ser adicionadas com futuros soft forks. Desde o Tapscript, o uso do `OP_NOP` foi substituído pelo mais eficiente `OP_SUCCESS`.