---
term: OP_CHECKSIGADD (0XBA)

---
Extrai os três primeiros valores da pilha: uma `chave pública`, um `CScriptNum` `n`, e uma `assinatura`. Se a assinatura não for o vetor vazio e não for válida, o script termina com um erro. Se a assinatura for válida ou for o vetor vazio (`OP_0`), dois cenários são apresentados:


- Se a assinatura for o vetor vazio: um `CScriptNum` com o valor de `n` é colocado na pilha e a execução continua;
- Se a assinatura não for o vetor vazio e permanecer válida: um `CScriptNum` com o valor de `n + 1` é colocado na pilha e a execução continua.

Para simplificar, `OP_CHECKSIGADD` executa uma operação similar a `OP_CHECKSIG`, mas ao invés de colocar true ou false na pilha, ele adiciona `1` ao segundo valor no topo da pilha se a assinatura for válida, ou deixa este valor inalterado se a assinatura representar o vetor vazio. o `OP_CHECKSIGADD` permite a criação das mesmas políticas de multisignature no Tapscript que o `OP_CHECKMULTISIG` e o `OP_CHECKMULTISIGVERIFY`, mas de uma maneira verificável em lote, o que significa que ele remove o processo de pesquisa na verificação de um multisig tradicional e, portanto, acelera a verificação enquanto reduz a carga operacional nas CPUs dos nós. Este opcode foi adicionado no Tapscript apenas para as necessidades do Taproot.