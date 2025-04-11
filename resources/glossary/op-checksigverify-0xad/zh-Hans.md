---
term: op_checksigverify (0xad)

---
执行与 `OP_CHECKSIG` 相同的操作，但如果签名验证失败，脚本会立即出错停止，交易因此无效。如果验证成功，脚本将继续执行，不会向堆栈推送 `1`（true）值。总之，"OP_CHECKSIGVERIFY "执行了 "OP_CHECKSIG "和 "OP_VERIFY "操作。Tapscript 中修改了此操作码，以验证 Schnorr 签名。