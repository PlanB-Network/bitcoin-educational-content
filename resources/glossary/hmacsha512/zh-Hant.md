---
term: HMAC-SHA512
---

`HMAC-SHA512`代表「基於 Hash 的訊息驗證碼 - 安全 Hash 演算法 512」。它是一種加密算法，用於驗證雙方交換的訊息的完整性和真實性。它結合加密 Hash 函數 `SHA512` 與共用秘鑰，為每個訊息 generate 獨特的訊息驗證碼 (MAC)。


在 Bitcoin 的情況下，`HMAC-SHA512`的自然使用略有衍生。此演算法用於 Wallet 的加密金鑰樹的確定性分層推導過程。`HMAC-SHA512` 主要用於從 seed 到主密鑰，然後再從父對到子對的每個衍生。這個演算法也出現在另一個名為 `PBKDF2` 的衍生演算法中，用來從復原詞組和 passphrase 到 seed。