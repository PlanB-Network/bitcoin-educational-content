---
term: OP_CHECKSIGADD (0XBA)
---

Extrai os três valores do topo da pilha: uma `chave pública`, um `CScriptNum` `n`, e uma `assinatura`. Se a assinatura não for o vetor vazio e não for válida, o script termina com um erro. Se a assinatura for válida ou for o vetor vazio (`OP_0`), dois cenários são apresentados:
* Se a assinatura for o vetor vazio: um `CScriptNum` com o valor de `n` é empurrado para a pilha, e a execução continua;
* Se a assinatura não for o vetor vazio e permanecer válida: um `CScriptNum` com o valor de `n + 1` é empurrado para a pilha, e a execução continua.
Para simplificar, `OP_CHECKSIGADD` realiza uma operação similar a `OP_CHECKSIG`, mas em vez de empurrar verdadeiro ou falso para a pilha, ele adiciona `1` ao segundo valor no topo da pilha se a assinatura for válida, ou deixa este valor inalterado se a assinatura representar o vetor vazio. `OP_CHECKSIGADD` permite a criação das mesmas políticas de multisignatura em Tapscript como com `OP_CHECKMULTISIG` e `OP_CHECKMULTISIGVERIFY` mas de uma maneira verificável em lote, o que significa que remove o processo de busca na verificação de um multisig tradicional e, assim, acelera a verificação enquanto reduz a carga operacional nos CPUs dos nós. Este opcode foi adicionado em Tapscript exclusivamente para as necessidades do Taproot.