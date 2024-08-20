---
term: ELTOO
---

ELTOO是一个针对比特币第二层的通用协议，它定义了如何共同管理UTXO的所有权。Eltoo由Christian Decker、Rusty Russell和Olaoluwa Osuntokun特别设计，旨在解决与闪电网络通道状态的协商机制相关的问题，即在开启和关闭之间的问题。Eltoo架构通过引入线性状态管理系统简化了协商过程，用一种更灵活、惩罚性更小的更新方法替代了既定的基于惩罚的方法。这一协议需要使用一种新型的SigHash，该SigHash允许在交易的签名中忽略所有输入。这种SigHash最初被称为`SIGHASH_NOINPUT`，后来改称为`SIGHASH_ANYPREVOUT`（*任何先前的输出*）。其实施计划在BIP118中。

> ► *Eltoo有时也被称为“LN-Symmetry”。*