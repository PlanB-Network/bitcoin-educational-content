---
term: P2SH-P2WPKH

---
P2SH-P2WPKH 代表*支付到脚本哈希-支付到见证公钥哈希*。这是一种标准脚本模式，用于在UTXO上建立消费条件，也称为 "嵌套式 SegWit"。

P2SH-P2WPKH 是随着 2017 年 8 月 SegWit 的实施而推出的。该脚本是一个包裹在 P2SH 中的 P2WPKH。它根据公钥的哈希值锁定比特币。与经典 P2WPKH 不同的是，该脚本被封装在经典 P2SH 的 "redeemScript "中。

该脚本是在 SegWit 推出时创建的，目的是促进 SegWit 的采用。它允许使用这一新标准，即使服务或钱包尚未与 SegWit 原生兼容。这是一种向新标准过渡的脚本。如今，使用这类封装的 SegWit 脚本已不再重要，因为大多数钱包都已实现了本地 SegWit。P2SH-P2WPKH 地址使用 "Base58Check "编码编写，始终以 "3 "开头，与任何 P2SH 地址一样。

> ► *`P2SH-P2WPKH`有时也称为`P2WPKH嵌套在P2SH中`。