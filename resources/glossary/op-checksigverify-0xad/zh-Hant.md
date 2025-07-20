---
term: op_checksigverify (0xad)
---

執行與 `OP_CHECKSIG` 相同的操作，但如果簽章驗證失敗，腳本會立即停止並顯示錯誤，交易因此無效。如果驗證成功，腳本會繼續，不會推送一個 `1` (true) 值到堆疊。總而言之，`OP_CHECKSIGVERIFY` 執行操作 `OP_CHECKSIG` 之後的 `OP_VERIFY`。這個 opcode 在 Tapscript 中被修改以驗證 Schnorr 簽名。