---
term: overt asicboost
---

AsicBoost 的開放透明版本。AsicBoost 是用於 Bitcoin Mining 的演算法最佳化技術。使用公開透明版本的礦工會操作候選區塊的 `nVersion` 欄位，並使用此修改作為額外的 Nonce。此方法可在每次散列嘗試中保持區塊的實際 `Nonce` 欄位不變，藉由在每次嘗試之間保持某些資料相同，從而減少每次 SHA256 所需的計算。此版本與 AsicBoost 的隱蔽版本不同，它是公開可偵測的，並且不會對網路的其他部分隱藏其修改。