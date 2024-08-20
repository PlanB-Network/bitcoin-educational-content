---
term: REDEEMSCRIPT
---

Um script que define as condições específicas que as entradas devem cumprir para desbloquear os fundos associados a uma saída P2SH. Em um UTXO P2SH, o `scriptPubKey` contém o hash do `redeemScript`. Quando uma transação deseja gastar este UTXO como uma entrada, ela deve fornecer o `redeemScript` claro que corresponde ao hash contido no `scriptPubKey`. O `redeemScript` é, portanto, fornecido no `scriptSig` da entrada, juntamente com outros elementos necessários para satisfazer as condições do script, como assinaturas ou chaves públicas. Esta estrutura encapsulada garante que os detalhes das condições de gasto permaneçam ocultos até que os bitcoins sejam de fato gastos. É notavelmente usado para carteiras multisignature P2SH Legacy.