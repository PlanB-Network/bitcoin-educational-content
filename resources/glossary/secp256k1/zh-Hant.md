---
term: SECP256K1
---

Bitcoin 協定中用來實作 ECDSA (*Elliptic Curve Digital Signature Algorithm*) 和 Schnorr 數位簽章演算法的特定橢圓曲線的名稱。secp256k1」曲線是由 Bitcoin 的發明者 Satoshi Nakamoto 選擇的。它有一些有趣的特性，尤其是性能優勢。


在 Bitcoin 中使用 `secp256k1` 表示每個私人密碼鑰匙 (隨機 256 位元的數字) 都是透過私人密碼鑰匙的點與 `secp256k1` 曲線的產生點相加再加倍的方式映射到相對應的公開密碼匙。這個操作在單向上很容易執行，但實際上不可能逆轉，這也是 Bitcoin 上數位簽章安全性的基礎。


`secp256k1` 曲線是由橢圓曲線公式 $y^2 = x^3 + 7$ 指定的，也就是說它的係數 $a$ 等於 $0$，$b$ 等於 $7$，是橢圓曲線公式 $y^2 = x^3 + ax + b$ 的一般形式。 - 2^{32} - 977$.曲線也有一個群階，也就是曲線上不同點的數目，一個預先定義的產生點 (或點 $G$)，用於加密作業中的 generate 金鑰對，以及一個等於 $1$ 的輔因。


> ► *"SEC 「代表 」Standards for Efficient Cryptography"(高效加密標準)。"P256 "表示曲線定義在一個 $\mathbb{Z}_p$ 的欄位上，其中 $p$ 是一個 256 位元的素數。"K "是指其發明者 Neal Koblitz 的名字。最後，"1" 表示這是此曲線的第一個版本。