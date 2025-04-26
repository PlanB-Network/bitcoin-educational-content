---
term: ELTOO

---
比特币第二层的通用协议，定义了如何共同管理UTXO的所有权。Eltoo 由 Christian Decker、Rusty Russell 和 Olaoluwa Osuntokun 设计，特别是为了解决与闪电通道状态协商机制相关的问题，即打开和关闭之间的问题。Eltoo 架构通过引入线性状态管理系统简化了协商过程，用一种更灵活、惩罚性更小的更新方法取代了既有的基于惩罚的方法。该协议要求使用一种新型 SigHash，允许忽略交易签名中的所有输入。这种 SigHash 最初称为 "SIGHASH_NOINPUT"，后来又称为 "SIGHASH_ANYPREVOUT"（*任何以前的输出*）。计划在 BIP118 中实现该功能。

> ► *Eltoo有时也被称为 "LN对称"。