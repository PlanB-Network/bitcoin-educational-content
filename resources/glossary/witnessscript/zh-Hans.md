---
term: WITNESSSCRIPT

---
一种脚本，用于指定可以从 P2WSH 或 P2SH-P2WSH UTXO 支出比特币的条件。通常，`witnessScript` 决定了 SegWit 标准下多重签名钱包的条件。在这些脚本标准中，UTXO（输出）的`scriptPubKey`包含 `witnessScript` 的哈希值。要将该 UTXO 作为新交易的输入，持有者必须披露原始 `witnessScript`，以证明其与 `scriptPubKey` 中的指纹匹配。然后，`witnessScript` 必须包含在交易的 `witnessScript` 中，其中还包含验证脚本所需的元素，如签名。因此，对于 SegWit 来说，`witnessScript` 等同于 P2SH 交易中的 `redeemScript`，不同之处在于它被放在交易见证中，而不是放在 `scriptSig`中。

> ► *请注意，`witnessScript` 不应与 `scriptWitness` 混淆。虽然 `witnessScript` 定义了 P2WSH 或 P2SH-P2WSH UTXO 的支出条件，其本身就构成了一个脚本，但 `scriptWitness` 包含了任何 SegWit 输入的见证数据*。
