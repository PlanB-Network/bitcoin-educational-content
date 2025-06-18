---
term: 施諾
---

Schnorr 協定是基於橢圓曲線加密法 (ECC) 的電子簽章演算法。它在 Bitcoin 中用於從私密金鑰推導出公開金鑰，並使用私密金鑰簽署交易。在 Bitcoin 中，就像 ECDSA 一樣，Schnorr 是基於使用橢圓曲線 `secp256k1` 的，其特徵公式為：$y^2 = x^3 + 7$。自 2021 年 11 月 Taproot 更新啟動後，Schnorr 簽署協定已在 Bitcoin 協定中實施。