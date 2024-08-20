---
term: SIGHASH_ALL (0X01)
---

Tipo de Bandeira SigHash usada em assinaturas de transações Bitcoin para indicar que a assinatura se aplica a todos os componentes da transação. Ao usar `SIGHASH_ALL`, o assinante cobre todas as entradas e todas as saídas. Isso significa que nem as entradas nem as saídas podem ser modificadas após a assinatura sem invalidá-la. Este tipo de Bandeira SigHash é o mais comum em transações Bitcoin, pois garante a completa finalidade e integridade da transação.