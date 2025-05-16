---
name: Ricochet
description: 瞭解並使用 Ricochet 交易
---
![cover ricochet](assets/cover.webp)


***警告：** Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被查封之後，Ricochet 工具已不再可用。然而，此工具有可能在未來幾週內恢復。在此期間，您只能手動執行 Ricochet。本文的理論部分仍適用於瞭解其運作，並學習如何手動執行。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> 為您的交易增加額外歷史記錄的高級工具。攔截黑名單，並協助防止不公正的第三方帳戶關閉。

## 什麼是 Ricochet？


Ricochet 是一種對自己進行多次虛構交易以模擬 Bitcoin Ownership 轉移的技術。此工具不同於其他 Samourai 交易，因為它不提供前瞻性匿名，而是一種回溯性匿名。Ricochet 有助於模糊可能損害 Bitcoin 硬幣可替代性的特殊性。


例如，如果您執行 CoinJoin，您從混合中輸出的硬幣就會被識別為 CoinJoin。連鎖分析工具能夠偵測到 CoinJoin 交易的模式，並標示從中產生的硬幣。事實上，CoinJoin 的目的是打破硬幣的歷史連結，但其通過硬幣接合的過程仍可被偵測到。打个比方，这种现象类似于对文本进行加密：尽管我们无法访问原始明文，但很容易识别出已经应用了加密技术。


準確來說，「CoinJoin 輸出幣」這個標籤會影響 UTXO 的可替代性。受監管的實體，如 Exchange 平台，可能會拒絕接受經過 CoinJoin 的 UTXO，甚至要求其擁有者作出解釋，其帳戶可能會被封鎖或資金被凍結。在某些情況下，平台甚至可能將您的行為上報至國家機關。


這就是 Ricochet 方法發揮作用的地方。為了模糊 CoinJoin 所留下的足跡，Ricochet 會執行四次連續交易，讓使用者在不同的位址將資金轉移給自己。在這一連串的交易之後，Ricochet 工具最後會將比特幣傳送到最終目的地，例如 Exchange 平台。目的是在原始 CoinJoin 交易和最終消費行為之間建立距離。這樣一來，連鎖分析工具就會認為在 CoinJoin 之後很可能已經有 Ownership 的轉移，因此不必對寄送者採取行動。


![ricochet diagram](assets/en/1.webp)


面對 Ricochet 方法，我們可以想像，連鎖分析軟體會在四次反彈之後深化其檢查。然而，這些平台在最佳化偵測臨界值時面臨兩難的局面。它們必須建立跳躍次數的限制，在此限制之後，它們才會承認有可能發生了屬性變更，並應該忽略與先前 CoinJoin 的連結。然而，決定這個臨界值是有風險的：每延長一個觀測到的跳躍數量，就會以指數方式增加假陽性的數量，也就是被錯誤標示為 CoinJoin 參與者的個體，而實際上該操作是由其他人執行的。這種情況會對這些公司構成重大風險，因為誤判會導致不滿，進而使受影響的客戶轉向競爭對手。長期而言，過高的門檻會導致平台失去比競爭對手更多的客戶，這可能會威脅到平台的生存空間。因此，對這些平台而言，增加觀察到的跳票數量是很複雜的，而 4 通常是足以反駁其分析的數量。


因此，**Ricochet 最常見的使用情況出現在有必要在屬於您的 UTXO 上隱藏之前參與 CoinJoin 的情況**。理想情況下，最好避免將經過 CoinJoin 的比特幣轉移至受監管的實體。然而，在沒有其他選擇的情況下，尤其是在急需將比特幣變現成法定貨幣的時候，Ricochet 提供了一個有效的解決方案。


## Ricochet 在 Samourai Wallet 上如何運作？

Ricochet 只是一種將 bitcoins 寄給自己的方法。因此，完全可以手動模擬 Ricochet，而無需使用專門的工具。然而，對於那些希望自動化過程，同時受益於更精細的結果的人來說，Samourai Wallet 應用程式提供的 Ricochet 工具是一個很好的解決方案。


由於該服務是以 Samourai 支付，因此除了 Mining 費用外，Ricochet 還會產生 `100,000 Sats` 的服務費。因此，如果轉帳金額龐大，則建議使用 Ricochet。


Samourai 應用程式提供兩種 Ricochet 變體：


- Reinforced Ricochet，或稱「交錯交割」，具有將 Samourai 服務費分散到連續五筆交易的優點。此選項還可確保每筆交易都在不同的時間廣播，並記錄在不同的區塊中，這與 Ownership 的變更行為非常接近。儘管速度較慢，但對於不急於用錢的人來說，此方法較為可取，因為它可藉由增強 Ricochet 對於連鎖分析的抵抗力，將 Ricochet 的效率發揮到最大。
- 經典 Ricochet，其目的是在縮短的時間間隔內廣播所有交易，以快速執行作業。因此，與強化方法相比，此方法的隱私性較低，抗分析能力也較低。只有在緊急傳輸時，才應選用此方法。


## 如何在 Samourai Wallet 上執行 Ricochet？

要從 Samourai Wallet 應用程式執行 Ricochet 交易，請參照我們的視訊教學：

![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)


如果您想研究本教學中執行的 Ricochet 交易，請看這裡：


- 第一筆 Ricochet 交易：[8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://Mempool.space/fr/Testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- 最後一筆 Ricochet 交易：[27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://Mempool.space/fr/Testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)


**外部資源：**


- https://docs.samourai.io/en/Wallet/features/ricochet