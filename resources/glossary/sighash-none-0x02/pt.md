---
term: SIGHASH_NONE (0X02)

---
Tipo de SigHash Flag usado em assinaturas de transações Bitcoin para indicar que a assinatura se aplica a todas as entradas da transação, mas a nenhuma de suas saídas. O uso de `SIGHASH_NONE` implica que o signatário se compromete apenas com as entradas, permitindo que as saídas permaneçam indeterminadas ou modificáveis após a assinatura. Esse tipo de assinatura é útil nos casos em que o signatário deseja autorizar outras partes a decidir como os bitcoins serão distribuídos na transação.