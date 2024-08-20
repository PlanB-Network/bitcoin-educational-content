---
term: OP_CHECKSIGVERIFY (0XAD)
---

Realiza a mesma operação que `OP_CHECKSIG`, mas se a verificação da assinatura falhar, o script é imediatamente interrompido com um erro e a transação se torna inválida. Se a verificação for bem-sucedida, o script continua sem empurrar um valor `1` (verdadeiro) para a pilha. Em resumo, `OP_CHECKSIGVERIFY` executa a operação `OP_CHECKSIG` seguida por `OP_VERIFY`. Este opcode foi modificado em Tapscript para verificar assinaturas Schnorr.