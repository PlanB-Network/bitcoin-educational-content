---
term: OP_PUSHDATA2 (0X4D)
definition: 將最多 65 KB 的數據推入堆疊的Opcode。
---

允許向堆疊推送大量資料。其後是兩個位元組（little-endian），指定要推入的資料長度（最長約 65 KB）。它可用於在腳本中插入較大的資料。