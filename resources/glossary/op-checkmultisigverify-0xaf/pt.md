---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Combina um `OP_CHECKMULTISIG` e um `OP_VERIFY`. Utiliza múltiplas assinaturas e chaves públicas para verificar se `M` das `N` assinaturas são válidas, assim como faz o `OP_CHECKMULTISIG`. Então, como `OP_VERIFY`, se a verificação falhar, o script pára imediatamente com um erro. Se a verificação for bem sucedida, o script continua sem colocar nenhum valor na pilha. Este opcode foi removido no Tapscript.