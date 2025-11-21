---
term: HMAC-SHA512

---
“Hash-based Message Authentication Code - Secure Hash Algorithm 512” 的缩写。它是一种加密算法，用于验证双方交换信息的完整性和真实性。它将加密哈希函数 `SHA512` 与共享密钥相结合，为每条信息生成独特的信息验证码（Message Authentication Code，简称 MAC）。

在比特币世界中，`HMAC-SHA512` 的自然使用略有衍生。该算法用于钱包加密密钥树的分层确定性推导过程。`HMAC-SHA512` 主要用于从种子到主密钥，然后从父密钥对到子密钥对的每次派生。这种算法也存在于另一种名为 `PBKDF2` 的派生算法中，用于从恢复短语和口令短语到种子。
