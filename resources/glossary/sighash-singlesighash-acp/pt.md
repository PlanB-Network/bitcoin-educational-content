---
termo: SIGHASH_SINGLE/SIGHASH_ACP
---

Tipo de bandeira SigHash (`0x83`) combinada com o modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) usado em assinaturas de transações Bitcoin. Esta combinação especifica que a assinatura se aplica apenas a uma entrada específica e somente à saída que tem o mesmo índice que esta entrada. Outras entradas e saídas podem ser adicionadas ou modificadas por outras partes. Esta configuração é útil para transações colaborativas onde os participantes podem adicionar suas próprias entradas para financiar uma saída específica.