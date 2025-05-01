---
term: op_equalverify (0x88)
---

結合了 `OP_EQUAL` 和 `OP_VERIFY` 的功能。它首先檢查堆疊上前兩個值是否相等，然後要求結果為非零，否則，交易無效。`OP_EQUALVERIFY` 主要用於 Address 驗證腳本。