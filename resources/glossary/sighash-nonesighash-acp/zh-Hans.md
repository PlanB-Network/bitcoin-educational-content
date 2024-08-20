---
term: SIGHASH_NONE/SIGHASH_ACP
---

SigHash标志（`0x82`）的一种类型，与`SIGHASH_ANYONECANPAY`修饰符（`SIGHASH_ACP`）结合使用，在比特币交易签名中使用。这种组合表明签名仅适用于特定输入，而不承诺任何输出。这允许其他参与者自由添加额外的输入并修改交易的所有输出。