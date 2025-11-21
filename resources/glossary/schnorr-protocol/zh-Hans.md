---
term: SCHNORR PROTOCOL

---
Schnorr 协议是一种基于椭圆曲线加密法（ECC）的电子签名算法。在比特币系统中，它用于从私钥导出公钥，并用私钥签署交易。在比特币系统中，就像 ECDSA 一样，Schnorr 也是基于椭圆曲线 `secp256k1` 的使用，其等式为：$y^2 = x^3 + 7$。随着 Taproot 更新的激活，Schnorr 签名协议自 2021 年 11 月起在比特币协议中实施。
