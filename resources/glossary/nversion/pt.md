---
termo: NVERSION
---

O campo `nVersion` em uma transação Bitcoin é usado para indicar a versão do formato da transação que está sendo usada. Ele permite que a rede distinga entre diferentes evoluções do formato da transação ao longo do tempo e aplique as regras correspondentes. Este campo não tem impacto nas regras de consenso. Isso significa que qualquer valor atribuído a este campo não resulta na invalidação da transação. No entanto, o campo `nVersion` tem regras de padronização que atualmente só aceitam os valores de `1` e `2`. Por enquanto, este campo é útil apenas para a ativação do campo `nSequence`.