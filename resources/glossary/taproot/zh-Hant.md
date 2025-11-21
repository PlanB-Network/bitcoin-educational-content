---
term: Taproot
---

Bitcoin 協定的重大更新，於 2021 年 11 月透過 Soft Fork 採用。此更新透過實施 BIP340、BIP341 和 BIP342，在隱私、效率和靈活性方面帶來顯著改善。此更新於 2021 年 6 月 12 日鎖定在區塊 687,284 處，當時在一段時間內產生的區塊中有 90% 發出了贊成信號，從而表明礦工已準備好啟動更新 (*Speedy Trial*)。啟動最終於 2021 年 11 月 14 日在區塊 709,632 處進行，距離 Pieter Wuille、Andrew Poelstra 和 Gregory Maxwell 就此事進行初步討論已近四年。這是自 2017 年具爭議性的 SegWit 啟用後的首次重大更新嘗試。


Taproot 也是 BIP341 的名字，在同名的 Soft Fork 中實現，它引入了一個新的腳本模型，命名為 P2TR。P2TR 脚本将比特币锁定在唯一的 Schnorr 公钥上，表示为 $K$。然而，這個鑰匙 $K$ 實際上是一個公開密鑰 $P$ 和一個公開密鑰 $M$ 的集合，後者是由 Merkle Root 的 `scriptPubKey` 清單計算出來的。用 P2TR 腳本鎖定的比特幣可以用兩種截然不同的方式花掉：一是發佈公開金鑰 $P$ 的簽章，二是滿足 Merkle Tree 中包含的其中一個腳本。第一種方式稱為 "*key path*「，第二種方式稱為 」*script path*"。