---
term: DIFFIE-HELLMAN
---

加密方法，可讓雙方透過不安全的通訊通道 generate 共享秘密。此秘密可用於加密雙方之間的通訊。Diffie-Hellman 使用模組演算法，因此，即使攻擊者可以觀察到交換，他們也無法在不解決困難的數學問題（即離散對數）的情況下推算出共用的秘密。在 Bitcoin 中，有時候會使用稱為 ECDH 的 DH 變體，它使用橢圓曲線，尤其是靜態 Address 協定，例如 Silent Payments 或 BIP47。