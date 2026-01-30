---
term: SIGHASH_NONE/SIGHASH_ACP

definition: Combinação de SigHash assinando um único input específico sem se comprometer com nenhum output.
---
Tipo de SigHash Flag (`0x82`) combinado com o modificador `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) usado em assinaturas de transações Bitcoin. Esta combinação indica que a assinatura se aplica apenas a uma entrada específica, sem comprometer-se com qualquer saída. Isso permite que outros participantes adicionem livremente entradas adicionais e modifiquem todas as saídas da transação.