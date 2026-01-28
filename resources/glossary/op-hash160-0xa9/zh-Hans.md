---
term: OP_HASH160 (0XA9)

definition: 先用 SHA256 再用 RIPEMD160 对顶部元素进行哈希处理的Opcode。
---
同时使用 `SHA256` 和 `RIPEMD160` 函数，从堆栈中提取顶层元素，并将其哈希值替换。这两步过程会生成一个 160 位的哈希指纹。
