---
term: REDEEMSCRIPT

---
Um script que define as condições específicas que as entradas devem cumprir para desbloquear os fundos associados a uma saída P2SH. Num UTXO P2SH, o `scriptPubKey` contém o hash do `redeemScript`. Quando uma transação deseja gastar este UTXO como um input, deve fornecer o `redeemScript` que corresponde ao hash contido na `scriptPubKey`. O `redeemScript` é assim fornecido no `scriptSig` do input, juntamente com outros elementos necessários para satisfazer as condições do script, tais como assinaturas ou chaves públicas. Essa estrutura encapsulada garante que os detalhes das condições de gasto permaneçam ocultos até que os bitcoins sejam realmente gastos. É usada nomeadamente para carteiras Legacy P2SH com várias assinaturas.