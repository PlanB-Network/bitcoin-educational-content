---
name: 混音 - Whirlpool
description: Whirlpool 應該做多少混音？
---
![cover remix- wp](assets/cover.webp)


*** 警告：** 在 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押之後，Whirlpool Stats Tool 已不再提供下載，因為它寄存在 Samourai 的 Gitlab 上。即使您先前已將此工具下載至您的本機，或已安裝在您的 RoninDojo 節點上，WST 目前仍無法運作。它依賴 OXT.me 提供的資料來運作，而這個網站已無法再存取。目前，WST 並不是特別有用，因為 Whirlpool 通訊協定已停止運作。不過，這些軟體仍有可能在未來幾週內恢復運作。此外，這篇文章的理論部分對於了解一般（不只是 Whirlpool）的共連原理和目標，以及了解 Whirlpool 模型的有效性，仍然具有相關性。您也可以學習如何量化 CoinJoin 循環所提供的隱私*。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> *打破硬幣留下的連結*

這是我經常被問到的問題。 **當使用 Whirlpool 進行共同接合時，應該進行多少次重混才能達到令人滿意的效果？


CoinJoin 的目的是將您的硬幣與一群無法區分的硬幣混在一起，以提供似是而非的隱匿性。這個動作的目的是要打破從過去到現在、從現在到過去的追蹤連結。換句話說，知道您在 CoinJoin 週期進入時的初始交易的分析師，應該無法確切辨識您在混幣週期退出時的 UTXO (從進入週期到退出週期的分析)。

![past-present links diagram](assets/en/1.webp)


相反地，如果分析師知道您在 CoinJoin 週期出口時的 UTXO，就應該無法判斷在進入週期時的原始交易（從出口週期到進入週期的分析）。

![present-past links diagram](assets/en/2.webp)

然而，混音的數量並不是評估分析師在建立過去與現在之間的聯繫時會遇到的困難的可靠標準，反之亦然。更相關的指標是您的硬幣所隱藏的群組大小。這些指標被稱為 "anonsets"。就 Whirlpool 而言，有兩種類型的 anonsets。


首先，我們可以確定您的 UTXO 在 CoinJoin 循環的出口處所隱藏的那一組的大小，也就是在這組中存在的不可區分硬幣的數量。

![probable UTXOs at exit](assets/en/3.webp)

這個指標，法文稱為 "prospective anonset「，英文稱為 」forward anonset「，或 」前瞻性指標"，讓我們可以評估您的錢幣對於追溯其從 CoinJoin 週期的進入到退出路徑的分析的抵抗力。這個指標可以估算出您的 UTXO 受保護的程度，以防有人試圖重建它在 CoinJoin 過程中從進入點到退出點的歷史。例如，如果您的交易參與了第一個 CoinJoin 週期，並進行了兩個額外的下游週期，您的硬幣的預期取消時間將為 `13`：

![forward anonset](assets/en/4.webp)

其次，可以計算出另一個指標來評估您的作品對從現在到過去的分析的阻力。藉由知道您在週期結束時的 UTXO，這個指標可以決定在 CoinJoin 週期（從週期結束到開始的分析）中可能構成您的輸入的潛在 Tx0 交易數量。這個指標測量分析師在您的作品經過coinjoins後，追蹤其來源的難度！[輸入時的可能來源](assets/en/5.webp)

這個指標的名稱是 "backward anonset「 或 」backward-looking metrics"。在法語中，我喜歡稱之為 "anonset rétrospectif"。在下圖中，這與所有橙色的 Tx0 氣泡相對應：

![backward anonset](assets/en/6.webp)

若要進一步瞭解這些指標的計算方法，我建議您閱讀 [我的 Twitter 線程](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) 中關於此主題的內容。我們也正在準備一篇關於 PlanB Network 的更全面的文章。


我知道所提供的答案可能看起來並不令人滿意，因為您希望得到特定的混音次數，而我正引導您參閱文件。原因是混音次數是評估 CoinJoin 循環中所獲得的匿名性的不可靠指標。因此，不可能將固定的混音數量定義為絕對和普遍的安全臨界值。


您的作品每增加一次混音，都會增加其匿名集。然而，重要的是要瞭解，主要是您的同儕所執行的混音才會增加您的潛在匿名集。在 Whirlpool 模型中，您的交易只需兩到三次 CoinJoin 循環，就可以達到相當高的潛在匿名集水平，這完全是透過參與過之前幣合的同業的活動來實現的。


另一方面，在我們的案例中，回溯性的anonset 並不是一個問題。事實上，從您最初的 CoinJoin 開始，您就可以從先前的池交易繼承中獲益，立即讓您的作品有很高的回溯性 anonset，在隨後的每個週期中都會有微弱的增加。

同樣重要的是要了解，似是而非的推諉性的建立永遠不會是完整的。它依賴於追查您的硬幣的概率。這個概率會隨著隱匿群體規模的增加而降低。因此，您應該根據個人的期望調整您在隱匿方面的目標。問問自己導致您使用硬幣組合的原因，以及實現這些目標所需的匿名程度。例如，如果使用 coinjoins 的目的仅仅是在向您的教子发送一些 Sats 作为生日礼物时保护您的 Wallet 的隐私，则不需要非常高的匿名级别。您的教子可能無法進行深入的鍊分析，即使他們可以，也不會對您的生活造成災難性的影響。但是，如果您是專制政權的目標，而在這種政權下，一丁點的資訊都可能導致您入獄，那麼您的行動就需要遵循嚴格得多的標準。


要確定這些著名的 anonset 指示器，您可以使用 Python 工具，稱為 **WST**（Whirlpool Stats Tool）。


然而，並非總是有必要計算您的每個硬幣連接硬幣的 anonsets。Whirlpool 的設計本身已經為您提供了保證。如前所述，追溯自動贖回很少會引起關注。從您的初始組合中，您已經獲得了特別高的回溯分數。至於前瞻性失效，您只需將您的硬幣在混合後帳戶中保留足夠長的時間即可。例如，以下是我的一枚`100,000 Sats` 硬幣在 CoinJoin 池中存放兩個月後的 anonset 分數：

![WST anonsets](assets/en/7.webp)

它顯示的回溯分數為 `34,593`，前瞻分數為 `45,202`。具體來說，這意味著兩件事：


- 如果分析師知道我的硬幣在循環結束時，並嘗試追溯其來源，他們會遇到 `34,593` 個潛在來源，每個來源都有相同的可能性是我的。
- 如果分析師在週期開始時知道我的硬幣，並嘗試在週期結束時確定其對應關係，他們將面臨 `45,202` 個可能的 UTXO，每個都有相同的概率是我的。

這就是為什麼我認為Whirlpool的使用在`HODL -> Mix -> Spend -> Replace`策略中特別相關。在我看來，最符合邏輯的做法是將大部分的比特幣儲蓄放在 Cold Wallet 中，同時在 Samourai 上持續維持一定數量的 CoinJoin 硬幣以支付日常開支。一旦兌換幣中的比特幣用完，就會換成新的比特幣，以回到混合幣的定義門檻。這個方法讓我們不用擔心UTXOs的ONSET，同時也讓coinjoins生效所需的時間更短。


我希望這個答案能讓您對 Whirlpool 機型有所了解。如果您想進一步瞭解 Bitcoin 上的硬幣接合如何運作，我建議您閱讀我關於此主題的綜合文章：


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**外部資源：**


- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-Whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7。