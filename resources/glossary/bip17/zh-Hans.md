---
term: BIP17
---

由Luke Dashjr提出的提案，与BIP12和BIP16竞争。BIP17引入了一个新的操作码`OP_CHECKHASHVERIFY`，旨在使得在解锁资金之前，能够验证`scriptSig`中的脚本与`scriptPubKey`中的哈希是否匹配。经过一段激烈的辩论后，最终选择了BIP16（P2SH）而不是BIP17（CHV）。