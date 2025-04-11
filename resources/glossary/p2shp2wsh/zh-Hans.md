---
term: P2SH-P2WSH

---
P2SH-P2WSH 代表*支付脚本散列--支付见证脚本散列*。它是一种标准脚本模型，用于建立UTXO 的消费条件，也称为 "嵌套 SegWit"。

P2SH-P2WSH 是随着 2017 年 8 月 SegWit 的实施而引入的。该脚本描述了一个包裹在 P2SH 中的 P2WSH。它根据脚本的哈希值锁定比特币。与经典 P2WSH 不同的是，脚本被包裹在经典 P2SH 的 "redeemScript "中。

该脚本是在 SegWit 推出时创建的，目的是促进 SegWit 的采用。它允许使用这一新标准，即使服务或钱包尚未与 SegWit 原生兼容。如今，使用这类封装的 SegWit 脚本已不再重要，因为大多数钱包都已实现了本地 SegWit。P2SH-P2WSH 地址使用 "Base58Check "编码书写，始终以 "3 "开头，与任何 P2SH 地址一样。