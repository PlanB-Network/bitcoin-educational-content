---
term: OP_CHECKSIG (0XAC)

---
Verifica a validade de uma assinatura em relação a uma determinada chave pública. Pega os dois primeiros elementos da pilha: a assinatura e a chave pública, e avalia se a assinatura está correta para o hash da transação e a chave pública especificada. Se a verificação for bem sucedida, ele coloca o valor `1` (verdadeiro) na pilha, caso contrário `0` (falso). Este opcode foi modificado no Tapscript para verificar assinaturas Schnorr.