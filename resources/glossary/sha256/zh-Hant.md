---
term: SHA256
---

*Secure Hash Algorithm 256 bits* 的縮寫。這是一個產生 256 位元摘要的加密 Hash 函數。由 *National Security Agency* (NSA) 於 2000 年代初設計，目前已成為處理敏感資料的聯邦標準。在 Bitcoin 協定中，`SHA256` 功能無處不在。它用於 Hash 區塊標頭，是 Proof of Work 的一部分。SHA256」也用於從公開金鑰導出接收 Address 的過程中。此外，它還用於 Merkle 樹中的交易和見證人在區塊中的聚合。`SHA256` 也用於計算金鑰指紋、計算某些校驗和，以及圍繞 Bitcoin 的許多其他過程。當連續應用兩次時，稱為 `HASH256`。Bitcoin 上主要使用這種雙重應用。當 `SHA256` 與 `RIPEMD160` 函式一起使用時，稱為 `HASH160`。這種雙雜湊方式用於鑰匙指紋和公共鑰匙的雜湊。SHA256`函數是 SHA 2 系列的一部分。