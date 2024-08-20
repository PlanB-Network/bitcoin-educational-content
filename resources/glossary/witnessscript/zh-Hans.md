---
术语：WITNESSSCRIPT
---

`witnessScript` 是一个脚本，指定了从 P2WSH 或 P2SH-P2WSH UTXO 中花费比特币的条件。通常，`witnessScript` 确定了在 SegWit 标准下多签名钱包的条件。在这些脚本标准中，UTXO（输出）的 `scriptPubKey` 包含了 `witnessScript` 的哈希值。要在新交易中将此 UTXO 作为输入使用，持有者必须揭示原始的 `witnessScript`，以证明其与 `scriptPubKey` 中的指纹匹配。然后，`witnessScript` 必须包含在交易的 `scriptWitness` 中，`scriptWitness` 还包含验证脚本所需的元素，如签名。因此，对于 SegWit 来说，`witnessScript` 相当于 P2SH 交易中的 `redeemScript`，不同之处在于它放置在交易的见证人部分，而不是 `scriptSig` 中。

> ► *注意，`witnessScript` 不应与 `scriptWitness` 混淆。虽然 `witnessScript` 定义了 P2WSH 或 P2SH-P2WSH UTXO 的花费条件，并构成了一个独立的脚本，`scriptWitness` 包含了任何 SegWit 输入的见证数据。*