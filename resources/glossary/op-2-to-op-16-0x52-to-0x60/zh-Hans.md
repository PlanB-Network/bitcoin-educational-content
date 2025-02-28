---
term: OP_2 至 OP_16 (0x52 至 0x60)

---
OP_2 "至 "OP_16 "操作码分别将 2 至 16 的数值推入堆栈。这些操作码允许插入较小的数值，用于简化脚本。这类操作码主要用于多签名脚本。下面是一个 2/3 多重签名的 `scriptPubKey` 实例：

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *所有这些操作码有时也称为 OP_PUSHNUM_N。