---
term: SHA512
---

*Secure Hash Algorithm 512 bits** 的縮寫。這是一個產生 512 位元摘要的加密 Hash 函數。它是由 *National Security Agency* (NSA) 在 2000 年代早期設計的。對於 Bitcoin，"SHA512 "函數不會直接在通訊協定中使用，但根據 BIP32 和 BIP39，它會在應用程式層級衍生子金鑰的情況下使用。在這些過程中，它在 `HMAC` 演算法以及 `PBKDF2` 金鑰推導函式中被多次使用。與`SHA256`一樣，`SHA512`函數也是 SHA 2 系列的一部分。其運作與後者非常相似。