---
term: SIGHASH_ALL/SIGHASH_ACP
---

SigHash标志（`0x81`）的类型，结合了`SIGHASH_ANYONECANPAY`修饰符（`SIGHASH_ACP`）在比特币交易签名中使用。这种组合指定签名适用于交易的所有输出，并且只适用于特定的输入。`SIGHASH_ALL | SIGHASH_ANYONECANPAY`允许其他参与者在初始签名后向交易添加额外的输入。这在合作场景中特别有用，例如众筹交易，不同的贡献者可以添加他们自己的输入，同时保持初始签名者承诺的输出的完整性。