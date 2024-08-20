---
termo: SIGHASH_SINGLE (0X03)
---

Tipo de bandeira SigHash usada em assinaturas de transações Bitcoin para indicar que a assinatura se aplica a todas as entradas da transação e apenas a uma saída, correspondendo ao índice da mesma entrada assinada. Assim, cada entrada assinada com `SIGHASH_SINGLE` é especificamente vinculada a uma saída particular. As outras saídas não são comprometidas pela assinatura e, portanto, podem ser modificadas posteriormente. Esse tipo de assinatura é útil em transações complexas, onde os participantes desejam vincular certas entradas a saídas específicas, enquanto deixam flexibilidade para as outras saídas da transação.