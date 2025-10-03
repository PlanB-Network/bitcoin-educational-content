---
term: OP_CHECKSIGVERIFY (0xAD)

---
执行与 `OP_CHECKSIG` 相同的操作，但如果签名验证失败，脚本会立即出错停止，使交易无效。如果验证成功，脚本将继续执行，不会向堆栈推入 `1`（true）值。总之，`OP_CHECKSIGVERIFY` 执行了 `OP_CHECKSIG` 和 `OP_VERIFY` 操作。Tapscript 中修改了此操作码，以验证 Schnorr 签名。
