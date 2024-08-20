---
term: WITNESSSCRIPT
---

Um script que especifica as condições sob as quais bitcoins podem ser gastos de UTXOs P2WSH ou P2SH-P2WSH. Tipicamente, `witnessScript` determina as condições de uma carteira multisignature sob o padrão SegWit. Nestes padrões de script, o `scriptPubKey` do UTXO (a saída) contém um hash do `witnessScript`. Para usar este UTXO como uma entrada em uma nova transação, o detentor deve revelar o `witnessScript` original, a fim de provar sua correspondência com a impressão digital no `scriptPubKey`. O `witnessScript` deve então ser incluído no `scriptWitness` da transação, que também contém os elementos necessários para validar o script, como assinaturas. Portanto, o `witnessScript` é o equivalente para SegWit do `redeemScript` em uma transação P2SH, com a diferença de que ele é colocado na testemunha da transação, e não no `scriptSig`.

> ► *Atenção, o `witnessScript` não deve ser confundido com o `scriptWitness`. Enquanto o `witnessScript` define as condições de gasto de um UTXO P2WSH ou P2SH-P2WSH e constitui um script por direito próprio, o `scriptWitness` contém os dados de testemunha de qualquer entrada SegWit.*