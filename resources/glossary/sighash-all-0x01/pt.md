---
term: SIGHASH_ALL (0X01)

---
Tipo de SigHash Flag usado em assinaturas de transações Bitcoin para indicar que a assinatura se aplica a todos os componentes da transação. Ao utilizar `SIGHASH_ALL`, o signatário cobre todas as entradas e todas as saídas. Isso significa que nem as entradas nem as saídas podem ser modificadas após a assinatura sem invalidá-la. Este tipo de SigHash Flag é o mais comum em transações Bitcoin, pois garante a finalização completa e a integridade da transação.