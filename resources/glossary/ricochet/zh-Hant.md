---
term: RICOCHET
---

一種涉及向自己進行多筆虛假交易以模擬比特幣 Ownership 轉移的技術。Ricochet 用來模糊可能影響 Bitcoin 硬幣可替代性的細節。例如，如果您執行 CoinJoin，您的輸出硬幣會被識別為 CoinJoin。這個「_coin from a coinjoin_」的標籤會影響 UTXO 的可替代性。受監管的實體，如 Exchange 平台，可能會拒絕接受經過 CoinJoin 的 UTXO，甚至要求其擁有人作出解釋，其帳戶可能會被封鎖或資金被凍結。在某些情況下，平台甚至會將您的行為上報至國家機關。這就是 Ricochet 方法發揮作用的地方。為了隱藏 CoinJoin 留下的痕跡，Ricochet 會連續執行四次交易，讓使用者在不同的地址將資金轉移給自己。在這一連串的交易之後，Ricochet 工具最後會將比特幣傳送到最終目的地，例如 Exchange 平台。目標是在原始 CoinJoin 交易和最終消費行為之間建立距離。如此一來，連鎖分析工具很可能會假設在 CoinJoin 之後，已經有 Ownership 的轉移，因此不需要啟動針對發行者的行動。Ricochet 最常見的使用案例發生在有必要隱瞞 UTXO 先前參與 CoinJoin 的情況，尤其是為了避免成為受監管平台或黑名單的 AML/CTF 政策的目標。Ricochet 工具可在 Samourai Wallet 上使用。