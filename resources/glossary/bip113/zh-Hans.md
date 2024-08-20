---
term: BIP113
---

引入了对所有时间锁操作（`nLockTime`、`OP_CHECKLOCKTIMEVERIFY`、`nSequence` 和 `OP_CHECKSEQUENCEVERIFY`）计算方式的更改。它规定，为了评估时间锁的有效性，现在必须将它们与 MTP（*过去的中位数时间*），即最后 11 个区块的时间戳的中位数进行比较。以前，只使用前一个区块的时间戳。这种方法使系统更加可预测，并防止矿工操纵时间参考。BIP113 通过一个软分叉在 2016 年 7 月 4 日引入，与 BIP68 和 BIP112 一起激活，首次使用 BIP9 方法激活。