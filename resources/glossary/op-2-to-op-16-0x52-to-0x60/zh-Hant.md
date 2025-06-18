---
term: op_2 至 op_16 (0x52 至 0x60)
---

從 `OP_2` 到 `OP_16` 的操作碼會將 2 到 16 的數值分別推入堆疊。它們用來簡化腳本，允許插入小數值。這種類型的 opcode 主要用於多簽名腳本。以下是 2/3 Multisig `scriptPubKey` 的範例：


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *所有這些操作碼有時也稱為 OP_PUSHNUM_N.*