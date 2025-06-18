---
term: PBKDF2
---

`PBKDF2` 代表 *Password-Based Key Derivation Function 2*。這是一種使用衍生函數從密碼建立密碼鑰匙的方法。它將一個密碼、一個加密鹽作為輸入，然後將一個預先設定的函數 (通常是 Hash 函數，如 `SHA256` 或 `HMAC`)反覆套用在這些資料上。這個過程會重覆多次，以獲得 generate 密鑰。


在 Bitcoin 的情況下，`PBKDF2`與`HMAC-SHA512`函數結合使用，從 12 或 24 個字的恢復詞組建立確定且分層的 Wallet (seed)。本例中使用的加密鹽為 BIP39 passphrase，迭代次數為 `2048`。