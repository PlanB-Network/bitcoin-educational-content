---
term: RIPEMD160
---

歐洲先進通訊技術研發中心 (Research and Development in Advanced Communications technologies in Europe) 的縮寫 完整性原始碼評估訊息摘要 160* (Integrity Primitives Evaluation Message Digest 160)。它是一個加密 Hash 函數，可從任意輸入產生 160 位元摘要。它用於 Bitcoin 將公開金鑰轉換為接收 Address 的 Legacy 和 SegWit v0 標準（對於 SegWit v1，公開金鑰不進行散列）。此過程會先對公開金鑰套用 `SHA256` Hash 函式，然後再對結果套用 `RIPEMD160` 函式。這兩個不同的 Hash 函數的組合在 Bitcoin 中被稱為「HASH160」。`RIPEMD160` 也用於確定性和分層式錢包，以計算金鑰指紋。具體來說，`HASH160` 用來計算父鑰匙的指紋，然後包含在擴展鑰匙 (xpub、xprv...) 的元資料中。