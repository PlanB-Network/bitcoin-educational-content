---
term: NVERSÃO

---
O campo `nVersion` em uma transação Bitcoin é usado para indicar a versão do formato de transação que está sendo usado. Ele permite que a rede distinga entre diferentes evoluções do formato da transação ao longo do tempo e aplique as regras correspondentes. Este campo não tem impacto nas regras de consenso. Isto significa que qualquer valor atribuído a este campo não resulta na invalidação da transação. No entanto, o campo `nVersion` tem regras de normalização que atualmente só aceitam os valores `1` e `2`. Por enquanto, este campo só é útil para a ativação do campo `nSequence`.