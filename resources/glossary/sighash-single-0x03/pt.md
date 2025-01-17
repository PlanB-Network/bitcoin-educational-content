---
term: SIGHASH_SINGLE (0X03)

---
Tipo de SigHash Flag usado em assinaturas de transações Bitcoin para indicar que a assinatura se aplica a todas as entradas da transação e a apenas uma saída, correspondente ao índice da mesma entrada assinada. Assim, cada entrada assinada com `SIGHASH_SINGLE` está especificamente ligada a uma determinada saída. As outras saídas não são comprometidas pela assinatura e podem, portanto, ser modificadas posteriormente. Este tipo de assinatura é útil em transações complexas, onde os participantes desejam vincular certas entradas a saídas específicas, deixando flexibilidade para as outras saídas da transação.