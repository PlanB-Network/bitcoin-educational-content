---
term: op_checkmultisigverify (0xaf)

---
结合了 `OP_CHECKMULTISIG` 和 `OP_VERIFY`。与 `OP_CHECKMULTISIG` 一样，它会使用多个签名和公钥来验证 `N` 个签名中的 `M` 个签名是否有效。然后，与 `OP_VERIFY` 一样，如果验证失败，脚本会立即出错停止。如果验证成功，脚本将继续执行，不会向堆栈推送任何值。Tapscript 删除了此操作码。