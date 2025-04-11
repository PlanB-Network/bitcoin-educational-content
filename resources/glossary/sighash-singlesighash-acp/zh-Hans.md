---
term: sighash_single/sighash_acp

---
比特币交易签名中使用的 SigHash 标志（`0x83`）与`SIGHASH_ANYONECANPAY`修饰符（`SIGHASH_ACP`）的组合类型。这种组合指定签名只适用于特定的单个输入，并且只适用于与该输入具有相同索引的输出。其他各方可以添加或修改其他输入和输出。这种配置适用于合作交易，参与者可以添加自己的输入，为特定输出提供资金。