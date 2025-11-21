---
term: op_checksigadd (0xba)
---

從堆疊中抽取前三個值：`public key`、`CScriptNum``n`和`signature`。如果簽章不是空向量且無效，腳本會以錯誤結束。如果簽章有效或為空向量 (`OP_0`)，則會出現兩種情況：


- 如果簽章是空向量：則會將值為 `n` 的 `CScriptNum` 推入堆疊，並繼續執行；
- 如果簽章不是空向量且仍然有效：則會將值為 `n + 1` 的 `CScriptNum` 推入堆疊，並繼續執行。

為了簡化，`OP_CHECKSIGADD` 執行類似於 `OP_CHECKSIG` 的操作，但它不是將真或假推入堆疊，而是在簽章有效時，在堆疊頂端的第二個值加上 `1`，或在簽章代表空向量時，讓這個值維持不變。`OP_CHECKSIGADD`允許在 Tapscript 中建立與`OP_CHECKMULTISIG`和`OP_CHECKMULTISIGVERIFY`相同的多重簽章政策，但以可批次驗證的方式，也就是去除了傳統 Multisig 驗證中的查詢過程，因此可以加快驗證速度，同時降低節點 CPU 的作業負載。此作業碼是完全為了 Taproot 的需求而在 Tapscript 中加入的。