---
term: BIP0330
---

Uma proposta conhecida como "*Erlay*", que visa otimizar a propagação de transacções não confirmadas na rede Bitcoin. Atualmente, as transacções são transmitidas a todos os pares de um nó, resultando em redundância e utilização excessiva de largura de banda. O BIP330 propõe limitar esta difusão a 8 pares por defeito, utilizando depois um mecanismo de reconciliação para partilhar eficientemente as transacções em falta. O Erlay reduz o consumo de largura de banda em cerca de 40%. Também evita um aumento linear do consumo de largura de banda com o número de pares ligados ao nó.