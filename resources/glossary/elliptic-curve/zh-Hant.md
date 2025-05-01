---
term: 橢圓弧度
---

在密碼學的範疇中，橢圓曲線是由等式 $y^2 = x^3 + ax + b$ 定義的代數曲線。這些曲線用於橢圓曲線加密法 (ECC)，ECC 是公開密碼匙加密法的一種方法，可建立加密演算法、數位簽署和密碼匙 Exchange 機制。在 Bitcoin 的情況下，ECDSA (*Elliptic Curve Digital Signature Algorithm*) 或 Schnorr 通訊協定會使用 `secp256k1` 曲線。選擇此曲線是基於其效能與安全特性。這些演算法用來從私密金鑰取得 generate 公開金鑰，以及簽署交易，從而解鎖比特幣。