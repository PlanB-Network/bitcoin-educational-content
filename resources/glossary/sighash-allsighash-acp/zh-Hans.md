---
term: sighash_all/sighash_acp

---
比特币交易签名中使用的 SigHash 标志（`0x81`）与`SIGHASH_ANYONECANPAY`修饰符（`SIGHASH_ACP`）的组合类型。这种组合指定了签名适用于交易的所有输出和特定输入。SIGHASH_ALL | SIGHASH_ANYONECANPAY "允许其他参与者在初始签名后为交易添加额外的输入。它在众筹交易等协作场景中特别有用，不同的参与者可以添加自己的输入，同时保持初始签名者承诺的输出的完整性。