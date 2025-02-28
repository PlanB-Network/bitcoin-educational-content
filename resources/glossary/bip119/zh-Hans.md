---
term: BIP119

---
引入名为 "OP_CHECKTEMPLATEVERIFY"（CTV）的新操作码。CTV 允许在交易中创建非递归契约，以便对特定硬币的使用（包括在未来的交易中）施加特定条件。更具体地说，它可以根据作为输入的UTXO的 "scriptPubKey "定义交易输出的 "scriptPubKey "条件。CheckTemplateVerify 设计简单，没有动态状态。它的实现旨在扩展比特币的脚本功能，以促进各种应用，如交易拥堵控制、创建非交互式支付通道、DLC、支付池......这个新的操作码将作为 `OP_NOP4` 的替代品被引入。这一变化意味着软分叉。