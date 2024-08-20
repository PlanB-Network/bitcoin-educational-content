---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

结合了`OP_CHECKMULTISIG`和`OP_VERIFY`。它需要多个签名和公钥来验证`M`出`N`个签名是有效的，就像`OP_CHECKMULTISIG`所做的那样。然后，像`OP_VERIFY`一样，如果验证失败，脚本会立即停止并报错。如果验证成功，脚本将继续执行，而不会向栈中推送任何值。这个操作码在Tapscript中被移除了。