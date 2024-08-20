---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Combina um `OP_CHECKMULTISIG` e um `OP_VERIFY`. Ele requer múltiplas assinaturas e chaves públicas para verificar que `M` de `N` assinaturas são válidas, assim como o `OP_CHECKMULTISIG` faz. Então, como o `OP_VERIFY`, se a verificação falhar, o script para imediatamente com um erro. Se a verificação for bem-sucedida, o script continua sem adicionar nenhum valor à pilha. Este opcode foi removido no Tapscript.