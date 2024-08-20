---
term: P2SH-P2WPKH
---

P2SH-P2WPKH代表*支付给脚本哈希 - 支付给见证公钥哈希*。它是一种标准的脚本模型，用于在UTXO上建立支付条件，也被称为“嵌套SegWit”。

P2SH-P2WPKH在2017年8月实施SegWit时引入。这种脚本是一个包裹在P2SH内的P2WPKH。它基于公钥的哈希锁定比特币。与经典P2WPKH的不同之处在于，脚本被包裹在经典P2SH的`redeemScript`中。

这种脚本在SegWit启动时被创建，以促进其采用。它允许使用这个新标准，即使是与SegWit尚未原生兼容的服务或钱包也是如此。它是一种向新标准过渡的脚本。因此，今天使用这种类型的包裹SegWit脚本已经不再非常相关，因为大多数钱包已经实现了原生SegWit。P2SH-P2WPKH地址使用`Base58Check`编码，并且始终以`3`开头，就像任何P2SH地址一样。

> ► *`P2SH-P2WPKH`有时也被称为`P2WPKH嵌套在P2SH中`。*