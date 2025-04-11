---
term: WITNESSSCRIPT

---
Um script que especifica as condições sob as quais bitcoins podem ser gastos a partir de UTXOs P2WSH ou P2SH-P2WSH. Tipicamente, o `witnessScript` determina as condições de uma carteira multisignature sob o padrão SegWit. Nestes padrões de script, o `scriptPubKey` do UTXO (a saída) contém um hash do `witnessScript`. Para utilizar este UTXO como entrada numa nova transação, o detentor deve revelar o `witnessScript` original, de forma a provar a sua correspondência com a impressão digital na `scriptPubKey`. O `witnessScript` deve então ser incluído no `scriptWitness` da transação, que também contém os elementos necessários para validar o script, tais como as assinaturas. Portanto, o `witnessScript` é o equivalente para o SegWit do `redeemScript` em uma transação P2SH, com a diferença de que ele é colocado no witness da transação, e não no `scriptSig`.

> ► *Cuidado, o `witnessScript` não deve ser confundido com o `scriptWitness`. Enquanto o `witnessScript` define as condições de gasto de um UTXO P2WSH ou P2SH-P2WSH e constitui um script por direito próprio, o `scriptWitness` contém os dados de testemunho de qualquer entrada SegWit