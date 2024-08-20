---
term: REDEEMSCRIPT
---

`REDEEMSCRIPT`是一个脚本，定义了输入必须满足的具体条件，以解锁与P2SH输出相关联的资金。在P2SH UTXO中，`scriptPubKey`包含了`redeemScript`的哈希值。当一个交易希望将此UTXO作为输入花费时，它必须提供与`scriptPubKey`中包含的哈希值匹配的明文`redeemScript`。因此，`redeemScript`在输入的`scriptSig`中给出，连同满足脚本条件所需的其他元素，如签名或公钥。这种封装结构确保了花费条件的细节在比特币实际被花费之前保持隐藏。它特别用于传统的P2SH多签名钱包。