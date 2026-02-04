---
term: OP_HASH160 (0XA9)
definition: 先用 SHA256 再用 RIPEMD160 對頂部元素進行雜湊處理的Opcode。
---

同時使用 `SHA256` 和 `RIPEMD160` 函式，從堆疊中取出最上層的元素，並以其 Hash 取代。這兩個步驟會產生 160 位元的指紋。