---
term: HASH160
---

在 Bitcoin 中使用的加密函數，主要用於產生 Legacy 和 SegWit v0 接收位址。它結合了兩個在輸入上相繼執行的 Hash 函式：首先是 SHA256，然後是 RIPEMD160。因此，此功能的輸出為 160 位元。


$$text{HASH160}(x) = （text{RIPEMD160}(\text{SHA256}(x)）$$