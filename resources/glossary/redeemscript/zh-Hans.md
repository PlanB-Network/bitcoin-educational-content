---
term: REDEEMSCRIPT

---
定义输入必须满足的特定条件才能解锁 P2SH 输出相关资金的脚本。在 P2SH UTXO 中，`scriptPubKey`包含`redeemScript`的哈希值。当交易希望将此 UTXO 作为输入使用时，必须提供与 `scriptPubKey` 中的哈希值相匹配的清晰 `redeemScript` 。因此，"redeemScript "与满足脚本条件所需的其他元素（如签名或公钥）一起在输入的 "scriptSig "中给出。这种封装结构可确保在比特币实际花费之前，花费条件的细节保持隐蔽。它主要用于传统的 P2SH 多重签名钱包。