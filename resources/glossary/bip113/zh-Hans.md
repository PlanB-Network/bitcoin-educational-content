---
term: BIP113

---
修改了所有时间锁操作（`nLockTime`、`OP_CHECKLOCKTIMEVERIFY`、`nSequence` 和 `OP_CHECKSEQUENCEVERIFY`）的计算方法。它规定，要评估时间锁的有效性，现在必须将其与 MTP（*过去中位时间*）进行比较，后者是最近 11 个块的时间戳的中位数。以前，只使用前一个区块的时间戳。这种方法提高了系统的可预测性，防止矿工操纵时间参考。BIP113 于 2016 年 7 月 4 日通过软分叉引入，同时引入的还有 BIP68 和 BIP112，首次使用 BIP9 方法激活。