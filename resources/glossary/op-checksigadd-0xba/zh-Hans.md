---
term: op_checksigadd (0xba)

---
从堆栈中提取前三个值："公钥"、"CScript 数""n "和 "签名"。如果签名不是空向量且无效，脚本将错误终止。如果签名有效或为空向量（`OP_0`），则会出现两种情况：


- 如果签名是空向量：一个值为 `n` 的 `CScriptNum` 被推入堆栈，然后继续执行；
- 如果签名不是空向量，并且仍然有效：一个值为 `n + 1` 的 `CScriptNum` 将被推入堆栈，并继续执行。

为了简化，`OP_CHECKSIGADD` 执行的操作类似于 `OP_CHECKSIG`，但它不是将 true 或 false 推入堆栈，而是在签名有效时将 `1` 添加到堆栈顶端的第二个值，或者在签名代表空向量时保持该值不变。OP_CHECKSIGADD "允许在 Tapscript 中创建与 "OP_CHECKMULTISIG "和 "OP_CHECKMULTISIGVERIFY "相同的多签名策略，但采用的是可批量验证的方式，这意味着它取消了传统多签名验证中的查找过程，从而加快了验证速度，同时减少了节点 CPU 的运行负荷。在 Tapscript 中添加此操作码完全是为了满足 Taproot 的需要。