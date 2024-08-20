---
term: OP_CHECKSIG (0XAC)
---

Verifica a validade de uma assinatura contra uma chave pública dada. Ele pega os dois elementos do topo da pilha: a assinatura e a chave pública, e avalia se a assinatura é correta para o hash da transação e a chave pública especificada. Se a verificação for bem-sucedida, ele insere o valor `1` (verdadeiro) na pilha, caso contrário `0` (falso). Este opcode foi modificado em Tapscript para verificar assinaturas Schnorr.