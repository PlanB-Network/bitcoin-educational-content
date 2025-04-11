---
term: OP_CHECKSIGVERIFY (0XAD)

---
Executa a mesma operação que `OP_CHECKSIG`, mas se a verificação da assinatura falhar, o script pára imediatamente com um erro e a transação é, portanto, inválida. Se a verificação for bem sucedida, o script continua sem colocar um valor `1` (verdadeiro) na pilha. Em resumo, `OP_CHECKSIGVERIFY` executa a operação `OP_CHECKSIG` seguida por `OP_VERIFY`. Este opcode foi modificado no Tapscript para verificar assinaturas Schnorr.