---
term: MTP（过去时间中位数）

---
比特币协议中使用这一概念来确定网络共识时间戳的差值。MTP 被定义为最近 11 个开采区块时间戳的中位数。使用这一指标有助于避免节点之间在出现差异时对确切时间产生分歧。MTP 最初用于验证区块时间戳是否与过去一致。自 BIP113 以来，它还被用作网络时间的参考，以验证时间锁定交易（"nLockTime"、"OP_CHECKLOCKTIMEVERIFY"、"nSequence "和 "OP_CHECKSEQUENCEVERIFY"）的有效性。