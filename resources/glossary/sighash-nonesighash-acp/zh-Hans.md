---
term: sighash_none/sighash_acp

---
比特币交易签名中使用的 SigHash 标志（`0x82`）与`SIGHASH_ANYONECANPAY`修饰符（`SIGHASH_ACP`）的组合类型。这种组合表示签名只适用于特定的输入，而不承诺任何输出。这就允许其他参与者自由添加额外的输入，并修改交易的所有输出。