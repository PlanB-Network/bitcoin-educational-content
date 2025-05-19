---
name: 加入機器人
description: 了解並使用 JoinBot
---

![DALL·E – samurai robot in a red forest, 3D render](assets/cover.webp)


***警告:** 在 Samourai Wallet 的創辦人於 4 月 24 日被逮捕及其伺服器被扣押之後，**JoinBot 服務已不再可用**。從現在開始，已經無法使用此工具。然而，您仍然可以執行石牆 X2，但您需要找到合作者並手動 Exchange PSBT。此服務可能會在未來幾個月內重新啟動，視案件進度而定*。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

JoinBot 是著名的 Bitcoin Wallet 軟體最新更新 0.99.98f 時加入 Samourai Wallet 套件的新工具。它可以讓您輕鬆地進行協作交易，優化您的隱私，而無需尋找合作夥伴。


*感謝優秀的 Fanis Michalakis 提供使用 DALL-E 做為縮圖的點子！ *


## 什麼是 Bitcoin 上的合作交易？


Bitcoin 以分佈式透明帳戶 Ledger 為基礎。任何人都能追蹤此電子現金系統使用者的交易。為了確保一定程度的隱私，Bitcoin 使用者可以用特定的結構進行交易，以增加其解釋的可信推诿性。


其目的不是直接隱藏資訊，而是在其他人中混淆資訊。這個目標用在 Coinjoins 中，這些交易會破壞 Bitcoin 上的硬幣歷史，使其追蹤變得複雜。為了達到這個效果，必須在交易中建立多個相同金額的輸入和輸出。


Inputs 是 Bitcoin 交易的輸入，而 Outputs 代表輸出。交易消耗其輸入，透過改變比特幣的消費條件來創造新的輸出。這個機制允許比特幣在使用者之間移動。

我將在這篇文章中詳細討論：Bitcoin 交易機制：UTXO、輸入和輸出。


在 Bitcoin 交易中，模糊軌跡的一種方法是進行協作交易。顧名思義，它涉及多個使用者之間的協議，每個使用者在同一筆交易中存入一筆比特幣作為輸入，並收到一筆比特幣作為輸出。


如前所述，最著名的協作交易結構是 CoinJoin。例如，在 CoinJoin Whirlpool 協定上，交易涉及 5 個參與者作為輸入和輸出，每個參與者擁有相同數量的比特幣。


![Diagram of a Coinjoin transaction on Whirlpool](assets/1.webp)


此交易的外部觀察者將無法知道哪個輸出是屬於哪個使用者的輸入。如果我們以 4 號使用者 (紫色) 為例，我們可以認出他們的輸入 UTXO，但我們將無法知道 5 個輸出中哪一個實際上是他們的。初始資訊不是隱藏的，而是在群組中混淆的。

使用者可以否認擁有某個 UTXO 作為輸出。這種現象稱為「似是而非的否認」，它允許在透明的 Bitcoin 交易中保密。


要瞭解更多關於 CoinJoin 的資訊，我在這篇長文章中解釋了一切：了解並在 Bitcoin 上使用 CoinJoin。


雖然 CoinJoin 在破解 UTXO 的追蹤方面非常有效，但不適合直接花費。事實上，它的結構意味著必須使用預先定義的金額輸入和相同價值的輸出（模擬 Mining 費用）。然而，Bitcoin 上的消費交易是隱私權的關鍵時刻，因為它通常會在使用者與其 On-Chain 活動之間建立實體連結。因此，在消費時使用隱私權工具似乎是必要的。還有其他專為實際付款交易設計的協作交易結構。


## StonewallX2 交易


在 Samourai Wallet 提供的無數消費工具中，有協同交易的 StonewallX2。它是兩個使用者之間的迷你 CoinJoin，專為付款而設計。從外部來看，這種交易可以導致幾種可能的解釋。因此，它提供了似是而非的隱蔽性，從而為用戶保密。


此 StonewallX2 協同交易設定可在 Samourai Wallet 和 Sparrow Wallet 上使用。此工具可在兩種軟體之間互通。


其機制非常簡單易懂。以下是其實際運作方式：



- 使用者想要以 bitcoins 付款 (例如在商家)。
- 他們會擷取實際付款收款人 (商家) 的收款 Address。
- 他們以多個輸入來建構特定的交易：至少有一個屬於他們，另一個則屬於外部合作者。
- 交易將有 4 個輸出，包括 2 個相同金額的輸出：一個輸出到商家的 Address 進行付款，一個作為零錢返回使用者，一個與付款相同價值的輸出到合作者，另一個輸出也返回合作者。


例如，這裡是一個典型的 StonewallX2 交易，我在其中支付了 50,125 Sats。第一次輸入的 102,588 Sats 來自我的 Samourai Wallet。第二次輸入的 104,255 Sats 來自我合作者的 Wallet：


![StonewallX2 transaction diagram](assets/2.webp)


我們可以觀察到 4 筆輸出，包括 2 筆相同數額的輸出，以混淆軌跡：



- `50,125 Sats`，這些款項會付給我的實際收款人。
- 代表我的變更的 `52,306 Sats`，因此回到我的 Wallet 中的 Address。
- 50,125Sats`歸還給我的合作者。
- `53,973 Sats` 交還給我的合作者。


操作結束時，合作者將恢復其初始餘額（扣除 Mining 費用），而使用者則已向商家付款。這會為交易增加大量的熵，並斷絕付款寄件者和收件者之間不可抹煞的聯繫。


StonewallX2 交易的優勢在於它完全反駁了連鎖分析師所使用的經驗規則之一：多投入交易中投入的共同 Ownership。換句話說，在大多數情況下，如果我們觀察到一個有多個輸入的 Bitcoin 交易，我們可以假設所有這些輸入都屬於同一個人。Satoshi 中本在他的白皮書中已經指出了這個使用者隱私的問題：


> 作為額外的防火牆，每個交易都可以使用新的金鑰對，以防止它們連結到共同的擁有者。然而，多輸入交易的連結是無法避免的，因為多輸入交易必然會揭露其輸入是由相同的擁有者所擁有。

這是 On-Chain 分析中用來建構 Address 聚類的許多經驗規則之一。若要進一步瞭解這些啟發式方法，我建議您閱讀 Samourai 這一系列的四篇文章，其中精彩地介紹了這個主題。


StonewallX2 交易的優勢在於，外部觀察者會認為交易的不同輸入屬於一個共同的所有者。實際上，它們是兩個不同的使用者在合作。因此，對付款的分析會被引導至一個誘餌，而使用者的隱私則得以保留。


從外觀上看，StonewallX2 交易與 Stonewall 交易無法區分。它們之間唯一有效的區別是 Stonewall 不是協作式的。它只使用單一用戶的 UTXO。然而，在帳戶 Ledger 的結構上，Stonewall 和 StonewallX2 完全相同。這使得這個交易結構有了更多可能的解釋，因為外部觀察者將無法分辨輸入是來自同一個人還是兩個合作者。


此外，StonewallX2 相較於 Stowaway 型 PayJoin 的優勢在於它可以在任何情況下使用。付款的實際收款人不會為交易提供任何輸入。因此，StonewallX2 可用於在任何接受 Bitcoin 的商家付款，即使該商家不使用 Samourai 或 Sparrow。

另一方面，這種交易結構的主要缺點是需要合作者願意使用他們的比特幣參與您的支付。如果您有願意在任何情況下幫助您的 Bitcoin 朋友，這並不是問題。但是，如果您不認識其他 Samourai Wallet 使用者，或是沒有人願意合作，那麼您就會陷入困境。


為了解決這個問題，Samourai 團隊最近在他們的應用程式中加入了一項新功能：JoinBot.


## JoinBot 是什麼？


JoinBot 的原則很簡單。如果您找不到人合作進行石牆 X2 交易，您可以與 JoinBot 合作。實際上，您會直接與 Samourai Wallet 進行協作交易。


這項服務非常方便，特別是對於新手用戶來說，因為它是全天候可用的。如果您需要緊急付款並想做石牆X2，您不再需要聯絡朋友或尋找線上合作者。JoinBot 會協助您。


JoinBot 的另一個優點是，它所提供作為輸入的 UTXOs 完全來自於後混合 Whirlpool，這提高了您付款的隱私性。此外，由於 JoinBot 永遠在線上，您應該與擁有大量潛在 Anonsets 的 UTXOs 合作。


很明顯的，JoinBot 有一些需要注意的妥協：



- 就像經典的 StonewallX2，你的合作者必然知道所使用的 UTXOs 及其目的地。在 JoinBot 的情況中，Samourai 知道這個交易的細節。這不一定是壞事，但應該要記住。
- 為了避免垃圾郵件，Samourai 按實際交易金額收取 3.5% 的服務費，最高上限為 0.01 BTC。舉例來說，如果我用 JoinBot 寄出 100 千歐元的實際付款，服務費金額為 3,500 Sats。
- 要使用 JoinBot，您的 Wallet 中必須至少有兩個無關連且可用的 UTXO。
- 在經典的 StonewallX2 中，Mining 的費用是由兩個合作者平分。有了 JoinBot，您顯然必須支付全部的 Mining 費用。
- 為了讓 JoinBot 交易與經典的 StonewallX2 或 Stonewall 交易完全相同，服務費的支付是在完全獨立的交易中進行。Samourai 最初支付的一半 Mining 費用的退款將在這第二筆交易中完成。為了將您的隱私優化到底，費用的結算採用Stowaway (PayJoin)結構化交易。


## 如何使用 JoinBot？


要執行 JoinBot 交易，您必須擁有 Samourai Wallet。您可以在此下載，或從 Google Playstore 下載。


與大部分 Samourai 所開發的工具不同，Sparrow Wallet 尚未宣佈 JoinBot 的實作。因此這個工具只能在 Samourai 上使用。


在這段影片中，您將逐步了解如何使用 JoinBot 執行 StonewallX2 交易：


![How to use Joinbot](https://youtu.be/80MoMz2Ne5g)


以下是我們剛剛在影片中執行的交易圖：


![Diagram of my StonewallX2 transaction with JoinBot.](assets/3.webp)


我們可以看到 5 個輸入：



- 3 筆 100 公斤的輸入來自 Samourai (JoinBot)。
- 2 個輸入來自我個人的 Wallet、3,524 Sats 和 1.8 megasat。


交易的 4 個輸出如下：



- 212,452 個 Sats 中的 1 個給我付款的實際收款人。
- 另一個相同數量的，可以追溯到 Samourai Address。
- 1 的變更，也會回到 Samourai，金額為 87,302 Sats。這代表他們的投入總額 (300,000 Sats) 與混淆輸出 (212,452 Sats) 減去 Mining 費用的差額。
- 1 變更，回到我的 Wallet 中的另一個 Address。它代表我的輸入總額與實際付款之間的差額，再減去 Mining 的費用。


提醒一下，Mining 費用不代表交易輸出。它們只代表總投入與總輸出之間的差額。


## 總結


JoinBot 是一個額外的工具，為 Samourai 使用者增加更多的選擇和自由。它允許直接以 Samourai 作為合作夥伴進行石牆 X2 合作交易。這種交易方式有助於提高用戶隱私。


如果您可以和朋友一起進行經典的 StonewallX2，我還是建議您使用這個工具。然而，如果您被卡住，找不到任何合作者來付款，您知道 JoinBot 會全天候與您合作。


**外部資源：**


- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin