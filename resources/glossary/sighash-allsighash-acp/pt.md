---
term: SIGHASH_ALL/SIGHASH_ACP

definition: Combinação de SigHash que permite adicionar inputs após a assinatura inicial.
---
Tipo de SigHash Flag (`0x81`) combinado com o modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) usado em assinaturas de transações Bitcoin. Esta combinação especifica que a assinatura se aplica a todas as saídas e apenas a uma entrada específica da transação. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` permite que outros participantes adicionem entradas adicionais à transação após sua assinatura inicial. É particularmente útil em cenários colaborativos, como as transacções de crowdfunding, em que diferentes contribuintes podem adicionar os seus próprios inputs, preservando a integridade dos outputs atribuídos pelo signatário inicial.