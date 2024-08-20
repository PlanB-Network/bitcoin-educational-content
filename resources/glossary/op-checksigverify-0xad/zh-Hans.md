---
term: OP_CHECKSIGVERIFY (0XAD)
---

执行与`OP_CHECKSIG`相同的操作，但如果签名验证失败，脚本会立即因错误而停止，因此交易无效。如果验证成功，脚本将继续执行，而不会将`1`（真）值推送到堆栈上。总之，`OP_CHECKSIGVERIFY`执行的操作是`OP_CHECKSIG`后跟`OP_VERIFY`。在Tapscript中修改了这个操作码，以验证Schnorr签名。