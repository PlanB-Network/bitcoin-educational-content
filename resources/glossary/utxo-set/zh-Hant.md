---
term: UTXO SET
---

指在任何特定時刻所有現有 UTXO 的集合。換句話說，它是所有等待被花費的不同比特幣的大清單。如果將 UTXO 中所有 UTXOs 的金額加起來，就可以得到流通中的比特幣總金額。Bitcoin 網絡中的每個節點都會即時維護自己的 UTXO 集。當新的有效區塊被確認時，它會更新該區塊，其中包含的交易會消耗 UTXO 中的一些 UTXOs，並產生新的 UTXOs。


每個節點都會保留這套 UTXO，以快速驗證在交易中所花的 UTXO 是否真的合法。這可讓他們偵測並拒絕 Double-spending 試圖。UTXO 集通常是 Bitcoin 去中心化的核心問題，因為它的大小自然會快速增加。由於其中一部分必須保留在 RAM 中，才能在合理的時間內驗證交易，因此 UTXO 集會逐漸使 Full node 的運作成本過高。UTXO 集對 IBD（*初始區塊下載*）也有重大影響。可以放置在 RAM 中的 UTXO 集數越多，IBD 的速度就越快。在 Bitcoin Core 上，UTXO 集儲存在名為 `/chainstate`的資料夾中。


> ► *在英文中，「UTXO set」可譯為「UTXO set」。