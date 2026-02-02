---
term: OP_VER (0X62)

definition: 曾推入客户端版本的已禁用Opcode，已转换为 OP_SUCCESS。
---
将客户端版本推入堆栈。这个操作码后来被禁用，因为如果继续使用它，每次更新都会导致硬分叉。BIP342 将此操作码改成 `OP_SUCCESS`。
