---
term: P2PK
---

P2PK 是 *Pay to Public Key* 的縮寫。它是 Bitcoin 上使用的標準腳本模型，用來在 UTXO 上建立支出條件。它允許直接將 bitcoins 鎖定在公開金鑰上，而不是 Address。

技術上來說，P2PK 腳本包含一個公開金鑰和一個要求對應的數位簽章來解鎖資金的指令。當擁有人想要花費比特幣時，他們必須提供用相關私密金鑰製作的簽章。此簽章使用 ECDSA（*橢圓曲線數位簽章演算法*）進行驗證。P2PK 常用於 Bitcoin 的早期版本，特別是 Satoshi Nakamoto。現在幾乎已不再使用。