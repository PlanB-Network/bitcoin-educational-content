---
term: op_checkmultisigverify (0xaf)
---

結合了 `OP_CHECKMULTISIG` 和 `OP_VERIFY`。它會使用多個簽章和公開金鑰來驗證 `N` 個簽章中的 `M` 個簽章是否有效，就像 `OP_CHECKMULTISIG` 所做的一樣。然後，就像 `OP_VERIFY` 一樣，如果驗證失敗，腳本會立即以錯誤訊息停止。如果驗證成功，腳本會繼續，不會推任何值到堆疊。這個 opcode 在 Tapscript 中被移除。