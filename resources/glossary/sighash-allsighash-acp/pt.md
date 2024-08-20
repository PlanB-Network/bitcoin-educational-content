---
termo: SIGHASH_ALL/SIGHASH_ACP
---

Tipo de bandeira SigHash (`0x81`) combinada com o modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) usado em assinaturas de transações Bitcoin. Esta combinação especifica que a assinatura se aplica a todas as saídas e apenas a uma entrada específica da transação. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` permite que outros participantes adicionem entradas adicionais à transação após sua assinatura inicial. É particularmente útil em cenários colaborativos, como transações de financiamento coletivo, onde diferentes contribuidores podem adicionar suas próprias entradas enquanto preservam a integridade das saídas comprometidas pelo signatário inicial.