---
term: ECDH
---

密碼金鑰 Exchange 的方法，以 Diffie-Hellman 金鑰 Exchange 的原理為基礎，但使用橢圓曲線，以較小的金鑰大小提供高度的安全性。此協定允許雙方使用其公開金鑰和私人金鑰對 generate 共用秘密，而無需自己 Exchange 私人金鑰。共用秘密可用於加密後續通訊。這種演算法有時也會出現在改進 Bitcoin 的提案中，特別是 BIP47 或 BIP352，用來從靜態識別碼推導出新的接收位址。