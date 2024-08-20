---
term: P2WPKH
---

P2WPKH代表*向见证公钥哈希支付（Pay to Witness Public Key Hash）*。它是一种标准的脚本模型，用于建立UTXO上的支出条件。P2WPKH在2017年8月实施SegWit时引入。

这种脚本类似于P2PKH（*向公钥哈希支付（Pay to Public Key Hash）*），因为它也基于公钥的哈希锁定比特币，即接收地址。不同之处在于签名和脚本如何包含在交易中。在P2WPKH的情况下，签名脚本信息（`scriptSig`）从传统的交易结构移动到一个称为`Witness`的单独部分。这种移动是SegWit（*隔离见证（Segregated Witness）*）更新的一个特点，有助于防止签名可变性。与传统交易相比，P2WPKH交易在费用上通常更便宜，因为见证部分的成本较低。

P2WPKH地址使用带有BCH代码校验和的`Bech32`编码编写。这些地址始终以`bc1q`开头。P2WPKH是版本0的SegWit输出。