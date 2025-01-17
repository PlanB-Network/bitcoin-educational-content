---
term: SIGHASH_SINGLE/SIGHASH_ACP

---
Tipo de SigHash Flag (`0x83`) combinado com o modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilizado em assinaturas de transações Bitcoin. Esta combinação especifica que a assinatura se aplica apenas a uma única entrada específica e apenas à saída com o mesmo índice que esta entrada. Outras entradas e saídas podem ser adicionadas ou modificadas por outras partes. Esta configuração é útil para transacções colaborativas em que os participantes podem adicionar as suas próprias entradas para financiar uma saída específica.