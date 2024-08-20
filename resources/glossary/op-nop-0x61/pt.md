---
termo: OP_NOP (0X61)
---

Não produz efeito na pilha ou no estado do script. Não realiza movimentos, verificações ou modificações. Simplesmente não faz nada, a menos que decidido de outra forma via um soft fork. De fato, desde a sua modificação por Satoshi Nakamoto em 2010, os comandos `OP_NOP` (`OP_NOP1` (`0XB0`) até `OP_NOP10` (`0XB9`)) são usados para adicionar novos opcodes na forma de um soft fork.

Assim, `OP_NOP2` (`0XB1`) e `OP_NOP3` (`0XB2`) já foram usados para implementar `OP_CHECKLOCKTIMEVERIFY` e `OP_CHECKSEQUENCEVERIFY`, respectivamente. Eles são usados em combinação com `OP_DROP` para remover os valores temporais associados da pilha, permitindo assim que a execução do script continue, seja o nó atualizado ou não. Os comandos `OP_NOP`, portanto, permitem a inserção de um ponto de interrupção em um script para verificar condições adicionais que já existem ou podem ser adicionadas com futuros soft forks. Desde o Tapscript, o uso de `OP_NOP` foi substituído pelo mais eficiente `OP_SUCCESS`.