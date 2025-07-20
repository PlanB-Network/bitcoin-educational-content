---
name: CoinJoin - 道場
description: 如何使用自己的道場執行 CoinJoin？
---
![cover](assets/cover.webp)


***警告：** Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押後，Whirlpool 工具已不再運作，即使是擁有自己的道場或正在使用 Sparrow Wallet 的個人也是如此。不過，這個工具仍有可能在未來幾週內恢復，或以不同的方式重新推出。此外，這篇文章的理論部分對於了解一般（不只是 Whirlpool）coinjoins 的原則和目標，以及了解 Whirlpool 模型的有效性，仍然具有相關性。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

在本教程中，您將學習什麼是 CoinJoin，以及如何使用 Samourai Wallet 軟體和 Whirlpool 實作，利用您自己的 Dojo 來執行一個 CoinJoin。在我看來，這種方法是目前混合比特幣的最佳方法。


## Bitcoin 上的 CoinJoin 是什麼？

**CoinJoin是一種打破比特幣在Blockchain**上的可追蹤性的技術。它依賴於具有同名特定結構的合作交易：CoinJoin 交易。


Coinjoins 會使外部觀察者的連鎖分析變得複雜，從而提高 Bitcoin 使用者的隱私。它們的結構可將不同使用者的多個硬幣合併為單一交易，從而使交易軌跡變得模糊，難以確定輸入和輸出地址之間的聯繫。


CoinJoin 的原理是基於一種協作方式：希望混合比特幣的多位使用者存入相同數額的比特幣作為同一筆交易的輸入。然後，這些金額會作為等值的輸出重新分配給每個使用者。在交易結束時，不可能將特定的輸出與輸入的已知使用者聯繫起來。輸入和輸出之間不存在直接關聯，這就打破了使用者和他們的 UTXO 之間的關聯，也打破了每個硬幣的歷史。

![coinjoin](assets/notext/1.webp)


CoinJoin 交易範例 (非本人所為)：[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


為了執行 CoinJoin，同時確保每位使用者都能隨時控制自己的資金，流程一開始是由協調員建立交易，然後將交易傳送給參與者。之後，每個使用者在確認交易適合自己之後，在交易上簽名。所有收集到的簽名最後都會整合到交易中。如果使用者或協調人試圖透過修改 CoinJoin 交易的輸出來轉移資金，簽名將被證明無效，導致節點拒絕交易。


CoinJoin 有多種實作，例如 Whirlpool、JoinMarket 或 Wabisabi，每種實作的目標都是管理參與者之間的協調，並提高 CoinJoin 交易的效率。

在本教程中，我們將探討 **Whirlpool**的實現，我認為這是在 Bitcoin 上執行硬幣接合的最有效解決方案。雖然**Whirlpool**可在多種錢包上使用，但在本教程中，我們將只探討其在 Samourai Wallet 移動應用程式中的使用，而不使用 Dojo。


## 為什麼要在 Bitcoin 上執行共同接合？

任何點對點支付系統的初始問題之一都是雙重消費：如何防止惡意個人多次使用相同的貨幣單位，而無需訴諸中央機構來仲裁？


Satoshi Nakamoto 透過 Bitcoin 協定提供了一個解決這個困境的方案，Bitcoin 協定是一個獨立於任何中央機關運作的點對點電子支付系統。他在白皮書中強調，證明沒有雙重花費的唯一方法，就是確保支付系統內所有交易的可視性。


為了確保每個參與者都知道交易，這些交易必須公開披露。因此，Bitcoin 的運作依賴於透明且分散式的基礎架構，允許任何節點操作者驗證電子簽章鏈的全部內容，以及每個硬幣從 Miner 製造開始的歷史。


Bitcoin 的 Blockchain 的透明性和分散性意味著網路的任何使用者都可以跟蹤和分析所有其他參與者的交易。因此，交易層級的匿名性是不可能的。但是，匿名性在個人識別層面上卻得以保留。在傳統銀行系統中，每個帳戶都與個人身份相關聯，而在 Bitcoin 上則不同，資金與成對的加密鑰匙相關聯，因此在加密識別符後為使用者提供了一種假名形式。


因此，當外部觀察者成功將特定的 UTXO 與已識別的使用者聯繫起來時，Bitcoin 的機密性就會受到威脅。一旦建立這種關聯，就有可能追蹤他們的交易並分析他們的比特幣歷史。CoinJoin 正是為了破解 UTXOs 的可追蹤性而開發的技術，從而在交易層面上為 Bitcoin 用戶提供一定的 Layer 保密性。


## Whirlpool 如何運作？

Whirlpool 有別於其他 CoinJoin 方法，它使用「_ZeroLink_」交易，確保所有輸入和所有輸出之間完全沒有可能的技術連結。這種完美的混合是透過一種結構來實現的，在這種結構中，每個參與者都提供相同數額的投入（Mining 費用除外），從而產生數額完全相等的輸出。

這種對輸入的限制性方法使 Whirlpool CoinJoin 交易具有一個獨特的特點：輸入和輸出之間完全沒有確定的聯繫。換句話說，與交易中的所有其他輸出相比，每項輸出歸屬於任何參與者的機率相同。

最初，每個 Whirlpool CoinJoin 的參與者人數限制為 5 人，其中有 2 位新加入者和 3 位混音者（我們將進一步解釋這些概念）。然而，在 2023 年觀察到 On-Chain 交易費用的增加，促使 Samourai 團隊重新思考其模式，以提高隱私性，同時降低成本。因此，考慮到費用和參與者數量的市場情況，協調員現在可以組織包括 6、7 或 8 個參與者的 Coinjoins。這些增強的會話被稱為"_Surge Cycles_"。重要的是要注意，無論設置如何，在 Whirlpool 幣會中總是只有 2 個新參與者。


因此，Whirlpool 交易的特點是輸入和輸出的數量相同，可以是：


- 5 組輸入和 5 組輸出；

![coinjoin](assets/notext/2.webp)


- 6 組輸入和 6 組輸出；

![coinjoin](assets/notext/3.webp)


- 7 組輸入和 7 組輸出；

![coinjoin](assets/notext/4.webp)


- 8 組輸入和 8 組輸出。

![coinjoin](assets/notext/5.webp)

因此，Whirlpool 提出的模式是基於 CoinJoin 的小型交易。與 Wasabi 和 JoinMarket 不同的是，Anonsets 的穩健性依賴於單一循環中參與者的數量，而 Whirlpool 則賭注於多個小規模循環的連鎖性。


在這種模式下，使用者只需在初次進入音源池時支付費用，即可參與眾多混音，無需支付額外費用。由新加入者支付混音者的 Mining 費用。


隨著每一個額外的 CoinJoin 幣參與，加上其過去遇到的同業，anonsets 將以指數方式成長。因此，我們的目標是利用這些免費的混音，每次混音都有助於提高與每個混合硬幣相關的 anonsets 密度。


Whirlpool 的設計考慮到兩個重要的需求：


- 由於 Samourai Wallet 主要是智慧型手機應用程式，因此可在行動裝置上輕鬆實作；
- 重新混合循環的速度，以促進安裝的顯著增加。

這些必要因素引導 Samourai Wallet 的開發人員在設計 Whirlpool 時做出選擇，導致他們限制每個週期的參與者人數。參與人數太少會影響 CoinJoin 的效率，大幅減少每個週期所產生的 anonsets，而參與人數太多則會造成行動應用程式的管理問題，並會妨礙週期的流程。

**最終，Whirlpool 上的每個 CoinJoin 不需要有大量參與者，因為ONSET 是透過數個 CoinJoin 循環的累積來實現的。


[-> 進一步了解 Whirlpool anonsets。](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### 游泳池和 CoinJoin 費用

為了讓這些多重循環能有效地增加混合硬幣的anonsets，必須建立一定的框架來限制UTXO的使用量。因此，Whirlpool 定義了不同的池。


UTXO 池代表一群希望混合在一起的使用者，他們同意使用 UTXO 的數量來優化 CoinJoin 流程。每個 UTXO 池指定一個固定數量，使用者必須遵守該數量才能參與。因此，要使用 Whirlpool 執行硬幣接合，您需要選擇一個池。目前可用的池如下：


- 0.5 比特幣
- 0.05 Bitcoin；
- 0.01 Bitcoin；
- 0.001 Bitcoin (= 100,000 Sats)。


當您加入一個比特幣池時，您的比特幣將被分為 generate UTXOs，這些比特幣與池中其他參與者的比特幣完全一致。每個池都有最高限額；因此，若金額超過此限額，您將被迫在同一池中分兩次加入，或轉入另一個金額更高的池：


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

如前所述，當 UTXO 可整合至 CoinJoin 時，即視為屬於一個池。然而，這並不表示使用者失去對它的擁有權。 ***這是 CoinJoin 技術與其他集中式混合技術的區別。


要進入 CoinJoin 遊戲池，必須支付服務費以及 Mining 費用。服務費對每個池都是固定的，目的是補償負責開發和維護 Whirlpool 的團隊。

使用 Whirlpool 的服務費只需在進入池時支付一次。完成這一步之後，您就有機會無限次參與混音，而無需支付任何額外費用。以下是目前每個池的固定費用：


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


無論您在 CoinJoin 中投入多少資金，這些費用基本上都是所選池的入場券。因此，無論您是以 0.01 BTC 加入 0.01 遊戲池，還是以 0.5 BTC 加入，費用的絕對值都是一樣的。


因此，在進行共同接合之前，使用者可以在兩種策略之間進行選擇：


- 選擇較小的基金池，以盡量減少服務費，因為他們知道會收到數個小的 UTXO 作為回報；
- 或偏好較大的池子，同意支付較高的費用，以減少價值較高的 UTXO 的數量。


一般建議不要在 CoinJoin 循環之後合併數個混合的 UTXO，因為這可能會損害獲取的機密性，特別是由於共用輸入-Ownership 啟發式 (CIOH)。因此，明智的做法可能是選擇較大的資料池，即使這意味著要付出較高的代價，以避免在輸出端有太多的小值 UTXO。使用者必須權衡這些利弊，才能選擇自己喜歡的池。


除了服務費之外，還必須考慮任何 Bitcoin 交易固有的 Mining 費用。身為 Whirlpool 的使用者，您必須支付準備交易 (`Tx0`)的 Mining 費用，以及第一次 CoinJoin 的費用。由於 Whirlpool 的模式依賴於新加入者的付款，所有後續的混音都將免費。


事實上，在每個 Whirlpool CoinJoin 中，輸入的使用者中有兩個是新加入者。其他的輸入則來自混音者。因此，交易中所有參與者的 Mining 費用都由這兩個新參與者支付，他們也會從免費的混音中獲益：

![coinjoin](assets/en/6.webp)

得益於此費用系統，Whirlpool 真正區別於其他 CoinJoin 服務，因為 UTXOs 的匿名性與用戶支付的價格不成正比。因此，只需為兩筆交易（"Tx0 "和初始組合）支付入池費和 Mining 費用，即可實現相當高水平的匿名性。

需要注意的是，用戶在完成多個 Coinjoins 後，還需要支付 Mining 費用，才能從池中提取他們的 UTXO，除非他們選擇了 "mix to "選項，我們將在下面的教程中討論。


### Whirlpool 使用的 HD Wallet 帳戶

要透過 Whirlpool 執行 CoinJoin，Wallet 必須 generate 多個不同的帳戶。在 HD (*Hierarchical Deterministic*) Wallet 的情況下，一個帳號構成一個與其他帳號完全隔離的區段，這種隔離發生在 Wallet 階層結構的第三個深度層級，也就是「xpub」層級。


理論上，一個 HD Wallet 最多可衍生出 `2^(32/2)` 不同的帳戶。所有 Bitcoin 錢包默認使用的初始帳戶對應於索引 `0'`。


對於適應 Whirlpool 的錢包，如 Samourai 或 Sparrow，使用 4 個帳戶來滿足 CoinJoin 流程的需求：


- 以索引 `0'` 識別的**存款**帳戶；
- **壞銀行** (或哆啦A夢) 帳戶，以索引 `2 147 483 644'` 識別；
- **premix** 帳戶，以索引`2 147 483 645'` 識別；
- **postmix** 帳戶，以索引 `2 147 483 646'` 識別。


每個帳戶都在 CoinJoin 內履行特定的功能。


所有這些帳號都連結到單一的 seed，允許使用者使用他們的復原短語以及必要時使用他們的 passphrase，來復原存取他們所有的 bitcoins。但是，在此復原操作中，有必要向軟體指定所使用的不同帳戶索引。


現在讓我們看看這些帳戶中 Whirlpool CoinJoin 的不同階段。


### Whirlpool 上不同階段的共同接合

**第 1 階段：Tx0**

任何 Whirlpool CoinJoin 的起始點都是**存款**帳戶。當您建立新的 Bitcoin Wallet 時，您會自動使用這個帳戶。這個帳戶必須存入想要混合的比特幣。

Tx0 代表 Whirlpool 混合過程的第一步。其目的是為 CoinJoin 準備和均衡 UTXO，將其劃分為與所選池量相對應的單位，以確保混合的均勻性。均分後的 UTXO 會被送至 **premix** 帳戶。至於無法進入池中的差額，則會被分到一個特定的帳戶：**不良庫**（或稱為「毒性變化」）。

此初始交易 `Tx0` 也用來結清應付給混合協調器的服務費用。與以下步驟不同的是，此交易不是協作式的；因此使用者必須負擔所有的 Mining 費用：

![coinjoin](assets/en/7.webp)


在這個 `Tx0` 交易的範例中，來自我們 ** 存款** 帳戶的 `372,000 Sats` 輸入被分成數個 UTXO 輸出，其分佈如下：


- 5,000Sats 「的金額，擬用於協調員的服務費，相對應於進入匯集的 」100,000Sats"；
- 三個準備混合的 UTXO，轉到我們的 **premix** 帳戶，並向協調員註冊。這些 UTXO 的均價各為 `108,000 Sats`，以支付其未來初始混合的 Mining 費用；
- 不能進入池中的盈餘，因為太小，被視為有毒變更。它會被送到特定的帳戶。在此，此變化為「40,000 Sats」；
- 最後，有`3,000 Sats`不構成輸出，而是確認`Tx0`所需的 Mining 費用。


舉例來說，這裡有一個真實的 Whirlpool Tx0 (不是我提供的)：[edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**第 2 步：毒性變化**

無法併入池中的盈餘（在此相當於`40,000 Sats`）會被轉至**壞銀行**帳戶，也稱為 "doxxic change"，以確保與 Wallet 中的其他 UTXO 嚴格分離。


這個 UTXO 對使用者的隱私而言是很危險的，因為它不僅仍附著在過去，因此可能附著在其擁有者的身分上，此外，它也被記下來是屬於執行過 CoinJoin 的使用者。

如果將 UTXO 與混合輸出合併，他們將喪失在 CoinJoin 循環過程中獲得的所有機密性，特別是因為共用輸入-Ownership-驅動程式 (CIOH)。如果與其他毒性變更合併，使用者會冒失去機密性的風險，因為這會連結 CoinJoin 循環的不同輸入。因此，必須謹慎處理。管理這種毒性 UTXO 的方法將在本文最後一部分詳述，未來的教學將更深入地介紹 PlanB Network 上的這些方法。


**第 3 步：初步混合**

在 `Tx0` 完成後，均衡後的 UTXO 將傳送至 Wallet 的 **premix** 帳戶，準備導入其第一個 CoinJoin 循環，也稱為 「初始混合」。如果在我們的範例中，`Tx0`產生多個要混合的 UTXO，則每個 UTXO 都會整合到單獨的初始 CoinJoin 中。


在這些第一次混合結束時，**premix** 帳戶將為空，而我們的硬幣在支付了第一次 CoinJoin 的 Mining 費用後，將完全調整為所選池所定義的金額。在我們的例子中，我們的初始 UTXOs `108 000 Sats` 將減少到正好 `100 000 Sats`。

![coinjoin](assets/en/8.webp)

**第四步：混音**

初始混音之後，UTXOs 會被轉移到 **postmix** 帳戶。此帳戶收集已混合的 UTXO 和等待重新混合的 UTXO。當 Whirlpool 用戶端啟動時，位於 **postmix** 帳戶中的 UTXO 會自動可供重新混音，並會隨機選擇參與這些新的週期。


需要提醒的是，混音是 100% 免費的：不需要額外的服務費或 Mining 費用。因此，將 UTXOs 保留在 ** 後混合 ** 帳戶中，可保持其價值不變，並同時提高其匿名性。這就是為什麼允許這些錢幣參與多次 CoinJoin 循環的重要性。嚴格來說，您不需要花費任何金錢，而且還能提高它們的匿名性。


當您決定使用混合的 UTXO 時，您可以直接從這個 **postmix** 帳戶使用。建議您將混合 UTXO 保留在此帳戶中，以享受免費混音，並避免其離開 Whirlpool 電路，從而降低其保密性。


正如我們將在下面的教學中看到的，還有 "mix to "選項，它提供了自動將您的混合硬幣傳送到另一個 Wallet 的可能性，例如，在定義的硬幣接合數量後的 Cold Wallet。

在涵蓋了理論之後，讓我們深入實踐，透過 Samourai Wallet Android 應用程式使用 Whirlpool，在自己的 Dojo 上同步 Whirlpool CLI 和 GUI 的教學！

## 教學：CoinJoin Whirlpool 與您自己的道場

使用 Whirlpool 有許多選項。我想在此介紹的是 Samourai Wallet 選項，這是 Android 上的開放原始碼 Bitcoin Wallet 管理應用程式，但這次是 ** 搭配您自己的 Dojo**。


使用您自己的Dojo通過Samourai Wallet進行coinjoins，在我看來，是迄今為止在Bitcoin上進行coinjoins最有效的策略。這種方法需要一定的初始投資，但一旦到位，它提供了可能性，每天24小時，每周7天不斷地混合和重新混合您的比特幣，而無需保持您的Samourai應用程序在任何時候都處於激活狀態。事實上，由於 Whirlpool CLI 在 Bitcoin 節點上運行，您可以隨時準備參與 Coinjoins。Samourai 應用程式讓您有機會在任何時間、任何地點，直接從您的智慧型手機使用您的混合資金。此外，這種方法的優點是不會將您與 Samourai 團隊管理的伺服器相連，從而保護您的 `xpub` 免於任何外部暴露。


因此，這項技術非常適合那些追求最大隱私和最高品質 CoinJoin 循環的人。不過，它需要有一個 Bitcoin 節點供您使用，而且我們稍後還會看到，它需要一些設定。因此，它更適合中級到高級使用者。對於初學者，我建議透過另外兩個教學來熟悉 CoinJoin，這兩個教學展示了如何從 Sparrow Wallet 或 Samourai Wallet (不使用 Dojo)：


- [Sparrow Wallet CoinJoin tutorial](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- [Samourai Wallet CoinJoin tutorial (without Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.


### 瞭解設定

首先，您需要一個 Dojo！Dojo 是基於 Bitcoin Core 的 Bitcoin 節點實作，由 Samourai 團隊開發。


若要執行您自己的 Dojo，您可以選擇獨立安裝 Dojo 節點，或是利用 Dojo 在另一個「節點中的節點」Bitcoin 節點解決方案之上的優勢。目前，可用的選項有


- [RoninDojo](https://ronindojo.io/)，它是一個增強了附加工具的 Dojo，包括安裝助手和管理助手。我在這份教學中詳細說明了設定和使用 RoninDojo 的步驟：[RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- [Umbrel](https://umbrel.com/) 與 "Samourai Server" 應用程式；
- [MyNode](https://mynodebtc.com/) 與 "Dojo" 應用程式；
- [Nodl](https://www.nodl.eu/)與「Dojo」應用程式；
- [Citadel](https://runcitadel.space/) 與 "Samourai" 應用程式。

![coinjoin](assets/notext/9.webp)

在我們的設定中，我們將與三個不同的介面互動：


- Samourai Wallet**，它將主持我們的Bitcoin Wallet專用於coinjoins。這個 FOSS 應用程式可在 Android 免費下載，讓您可以控制您的混音 Wallet，特別是從智慧型手機中花費您的後混音；
- Whirlpool CLI** (_Command Line Interface_)，它將在主控 Dojo 的節點上運作。此軟體可存取 Samourai Wallet 的鑰匙。它負責與協調器溝通，並持續管理 Coinjoins。它在您的節點上扮演您的 Samourai Wallet 的複本，隨時準備參與 Coinjoins；
- Whirlpool GUI** (_Graphical User Interface_圖形使用者介面)，是我們用來監控 Whirlpool CLI 的活動和遠端啟動混合的圖形使用者 Interface。Whirlpool GUI 可視化顯示 Whirlpool CLI 所進行的作業。此軟體必須安裝在與 Dojo 分離的電腦上。對於 Umbrel、MyNode、Nodl 和 Citadel 的使用者而言，Whirlpool GUI 是必須安裝的。不過，使用 RoninDojo 時，Whirlpool GUI Interface 已經透過 `Whirlpool` 應用程式整合到您節點的網頁 Interface 中。因此，您不需要將其安裝在單獨的 PC 上。


在我看來，使用 RoninDojo 是用 Dojo 執行 coinjoins 的最佳解決方案。由於這個 node-in-box 軟體是與 Samourai 團隊直接合作，RoninDojo 對於執行這項工作更為優化。此外，Whirlpool GUI 與網頁 Interface 的整合也大幅簡化了設定流程。在本教程中，我仍將介紹如何使用其他整合 Dojo 的解決方案 (Umbrel、Nodl、MyNode 和 Citadel)。


### 準備您的道場

首先，您需要安裝 Dojo 並取得 QR 代碼或連結，以便遠端連線。此連結是以 `.onion` 結尾的 Tor Address。如果您使用的是 RoninDojo，只需導航到 `Pairing` 功能表即可存取此資訊。

![coinjoin](assets/notext/10.webp)


在 `Samourai Dojo` 下方，按一下 `Pair now` 按鈕。


![coinjoin](assets/notext/11.webp)


您的連線 QR 代碼和對應的連結將會顯示。


![coinjoin](assets/notext/12.webp)


如果您使用 Umbrel，請到 App Store 搜尋 `Samourai Server` 應用程式。它位於`Bitcoin`標籤中。


![coinjoin](assets/notext/13.webp)


安裝應用程式。


![coinjoin](assets/notext/14.webp)


開啟應用程式後，您就可以取得 QR 代碼，連接到您的 Dojo。


![coinjoin](assets/notext/15.webp)


如果您使用的是 MyNode、Citadel 或 Nodl 等其他 node-in-box 軟體，流程與 Umbrel 相似。您需要安裝 Samourai 或 Dojo 應用程式，以取得連線到 Dojo 的必要資訊。


![coinjoin](assets/notext/16.webp)


### 準備您的 Samourai Wallet

擷取道場的連線資訊後，現在就該設定您的 Wallet 以進行硬幣兌換。有兩種情況：如果您的智慧型手機上還沒有 Samourai Wallet，過程很簡單，只要建立一個新的即可。


另一方面，如果您已經擁有 Samourai Wallet，則需要重新安裝應用程式以將其與新的 Dojo 相關聯。這個步驟是必要的，因為只有在第一次啟動應用程式時才能建立與 Dojo 的連接。不過，由於您的手機上有 Samourai 自動產生的加密備份檔案，因此這個步驟非常簡單快速。


*如果您從未使用過 Samourai，您可以跳過這些初步步驟，直接進行應用程式的安裝。


首先，請確認您的Samourai Wallet應用程式為最新版本。要做到這一點，請檢查Google Play商店或比較您的應用程序在 「設置>其他 」與Samourai網站提供的版本。


![coinjoin](assets/notext/17.webp)


確保您的 Samourai Wallet 復原短語清晰可辨。然後，透過導覽到 `設定 > 疑難排解 > passphrase/Backup test` 對您的 BIP39 passphrase 進行測試，以確認其準確性。


![coinjoin](assets/notext/18.webp)

輸入您的 passphrase，然後驗證 Samourai 確認其有效性。

![coinjoin](assets/notext/19.webp)


如果您的passphrase無效，或者您沒有您的恢復短語，必須立即停止程序！ **在這種情況下，建議您將資金轉移到另一個Wallet，然後從一個新的空白Samourai Wallet開始。只有當您確定您擁有所有必要的備份資訊，並且您的passphrase是有效的，才能執行以下步驟。


然後繼續建立 Wallet 的加密備份，並將其複製到剪貼簿。若要執行此操作，請按一下螢幕右上方的三個小圓點，然後選擇「匯出 Wallet 備份」。


![coinjoin](assets/notext/20.webp)


**從這一步開始，請勿複製任何其他內容到剪貼板！** 保留您複製的備份是絕對必要的。


如果您已正確執行之前的步驟，現在您可以安全地刪除您的 Samourai Wallet。要執行此動作，請前往設定 > Wallet > 安全刪除 Wallet。


![coinjoin](assets/notext/21.webp)


![coinjoin](assets/notext/22.webp)


*如果您從未使用過 Samourai，並且是從頭開始安裝應用程式，您可以從這一步繼續教程。


您的 Samourai 應用程式已重新設定。開啟應用程式，然後像第一次使用一樣進行設定步驟。


![coinjoin](assets/notext/23.webp)


下一步，您將存取專門設定 Dojo 的頁面。選擇 `Dojo` 選項，然後輸入您的 Dojo 登入資訊。要做到這一點，您可以選擇按 `Scan QR` 來掃描信息。


![coinjoin](assets/notext/24.webp)


*對於Samourai的新使用者來說，就必須從頭建立一個Wallet。如果您需要協助，您可以參考建立新的 Samourai Wallet 的說明 [在本教程中，特別是在 「建立 Software Wallet」](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*。


如果您要繼續還原已存在的 Samourai Wallet，請選擇`還原現有的 Wallet`，然後選擇`我有 Samourai 備份檔案`。


![coinjoin](assets/notext/25.webp)

通常情況下，您的剪貼簿中應總是有您的復原檔案。然後點擊 `PASTE` 將檔案插入指定位置。為了解密，您還必須在下方對應的欄位中輸入 Wallet 的 BIP39 passphrase。完成時，按一下 `FINISH`。

![coinjoin](assets/notext/26.webp)


然後，您會被重新導向到您的 Samourai Wallet，這次，它會連接到您自己的道場。


![coinjoin](assets/notext/27.webp)


### 安裝 Whirlpool GUI

現在是安裝 Whirlpool GUI 的時候了，圖形化使用者 Interface 將允許您從平常的電腦管理您的 CoinJoin 週期。對於 RoninDojo 使用者來說，這一步是不需要的，因為可以直接在 `Apps > Whirlpool` 中透過網頁 Interface 來管理 coinjoins。但是，如果您正在使用其他 Bitcoin "node-in-box "解決方案，則必須進行此安裝。

![coinjoin](assets/notext/28.webp)

前往您的個人電腦，從 Samourai Wallet 官方網站下載 Whirlpool 軟體，選擇與您作業系統相對應的版本。


![coinjoin](assets/notext/29.webp)


在啟動 Whirlpool GUI 之前，必須在您的機器上安裝 JAVA 8 或更高版本。為此，[您可以安裝 OpenJDK](https://adoptium.net/)。

![coinjoin](assets/notext/30.webp)

Tor daemon 或 Tor 瀏覽器也必須在您電腦的背景運作。確保在每次使用 Whirlpool GUI 前啟動 Tor。如果 Tor 尚未安裝在您的電腦上，[您可以從官方專案網站下載並安裝](https://www.torproject.org/download/)，那麼請務必在背景啟動 Tor。


![coinjoin](assets/notext/31.webp)


一旦 JDK 安裝在您的系統上且 Tor 在背景啟動，您就可以啟動 Whirlpool GUI。


![coinjoin](assets/notext/32.webp)


從 Whirlpool GUI，點選 `進階：Remote CLI ` 連線您 Dojo 上的 Whirlpool CLI。您將需要 Whirlpool CLI 的 Tor Address。


![coinjoin](assets/notext/33.webp)


若要在 Umbrel 和其他「節點在盒內」解決方案上找到 Tor Address，只需啟動 Samourai Server 或 Dojo 應用程式（名稱可能因使用的軟體而異）。Tor Address 會直接出現在應用程式的頁面上。

![coinjoin](assets/notext/34.webp)

在 Whirlpool GUI 中，在 `CLI Address` 欄位中輸入之前取得的 Tor Address。保留 `http://` 前綴，但不要在最後加入 `:8899` 連接埠。只貼上提供給您的 Address。

![coinjoin](assets/notext/35.webp)


在 Tor Proxy 欄位，如果您使用的是 Tor daemon，請輸入 `socks5://127.0.0.1:9050`；如果是 Tor Browser，請輸入 `socks5://127.0.0.1:9150`。當您第一次透過 Whirlpool CLI GUI 連線時，可以將 API key 欄位留空。如果這不是您第一次連線，請在專用空格中輸入您的 API 金鑰。此密鑰可在 Tor Address 的相同頁面上找到。


![coinjoin](assets/notext/36.webp)


填好所有資料後，按一下「連線」按鈕。請稍候，連線可能需要幾分鐘。


![coinjoin](assets/notext/37.webp)


### 將 Samourai Wallet 與 Whirlpool GUI 配對

*對於 RoninDojo 使用者，您可以在這裡繼續教學。


現在我們將先前設定好的 Samourai Wallet 與 Whirlpool GUI 軟體配對，或直接與 RoninDojo 配對。無論您是使用 Whirlpool GUI 或 RoninDojo，都會要求您貼上或掃描 Samourai Wallet 的配對資訊。


![coinjoin](assets/notext/38.webp)


若要尋找此資訊，請進入 Wallet 的設定。


![coinjoin](assets/notext/39.webp)


按一下「交易」，然後按一下「與 Whirlpool GUI 配對」。


![coinjoin](assets/notext/40.webp)


之後，Samourai 會提供您必要的資訊以建立連線。請小心，這些資料很敏感！您可以直接複製或點選 QR 代碼符號後使用電腦的網路攝影機掃描顯示的 QR 代碼，將資料傳輸至您的電腦。


![coinjoin](assets/notext/41.webp)


執行此操作後，在 Whirlpool GUI 中選擇「Initialize GUI」。請稍候，因為此步驟可能需要一些時間。


![coinjoin](assets/notext/42.webp)


無論您使用的是 Whirlpool GUI 或 RoninDojo，都會要求您輸入 Samourai Wallet 的 passphrase。將其插入專用欄位，然後按下`登入`按鈕繼續。


![coinjoin](assets/notext/43.webp)


然後您就會到達 Whirlpool CLI 的首頁。


![coinjoin](assets/notext/44.webp)


### 從 Whirlpool GUI 啟動共同接合

*對 RoninDojo 使用者而言，遵循的流程完全相同。整合至 RoninDojo 的 Whirlpool 應用程式 Interface 提供與桌面 Whirlpool GUI 軟體相同的選項和功能。因此，您可以以相同的方式遵循這些說明。

現在一切都準備好了，您可以開始混合您的比特幣了。首先，將您想要混合的比特幣轉入您的Samourai Wallet的**Deposit**帳戶。此操作可直接透過 Samourai Wallet 應用程式或 Whirlpool 圖形使用者介面進行。在主頁面，點擊左上方的 「+存款 」按鈕。


![coinjoin](assets/notext/45.webp)


Whirlpool GUI 將 generate 接收 Address。它還會顯示參與每個 CoinJoin 池所需的最低金額。此金額因收費市場而異。建議您存入比最低要求略高的金額，因為如果 Mining 費用不降低，您的 UTXO 可能不被所需池接受。因此，請將您的比特幣發送到所提供的 Address。要獲得新的 Address，只需點擊 「更新 Address 」按鈕。


![coinjoin](assets/notext/46.webp)


確認存款後，您將可以在 Whirlpool GUI 的 ** 存款** 帳戶中看到存款。


![coinjoin](assets/notext/47.webp)


要啟動 CoinJoin 循環，請選擇要混合的 UTXO，然後按下 `Premix`按鈕。請小心：如果您同時選擇多個不同的 UTXO，它們會在 `TX0` 準備交易時合併。由於通用輸入 Ownership 啟發式 (CIOH)，這種合併可能會導致隱私性降低，尤其是當 UTXO 來自不同來源時。


![coinjoin](assets/notext/48.webp)


Whirlpool 配置頁面會開啟。您可以選擇要進入的錢池。同時選擇 Mining 專用於 `TX0` 和第一次合幣的費用。在此頁面的底部，會有一個摘要向您顯示哆啦A夢的變更金額，以及將被均衡並包含在 CoinJoin 循環中的 UTXOs 的金額和數量。如果您對此配置感到滿意，請按下 `Premix` 按鈕以啟動 CoinJoin 循環。

![coinjoin](assets/notext/49.webp)


一旦 `TX0` 建立，您就可以在 **Premix** 帳戶中看到您的均分 UTXOs，等待確認。為了讓您的錢幣可以一週 7 天、每天 24 小時自動混幣，我建議您啟動 `自動混合預混和後混 '選項。您可以在 Whirlpool GUI 視窗左側的 「配置 」標籤中找到此功能。

![coinjoin](assets/notext/50.webp)

在開始合幣之後，您可以退出 Whirlpool GUI 以及 Samourai Wallet。只有您的節點需要保持連線，才能參加連續的合幣。然而，建議您定期檢查 CoinJoin 循環的進度。如果您發現您的 UTXOs 在一段時間內不再被選中參加 CoinJoin，這可能表示有 bug。在這種情況下，請前往 Whirlpool CLI 並選擇 `Start`，以重新啟動您的可用性進行硬幣接合。


![coinjoin](assets/notext/51.webp)


您可以從 Whirlpool GUI 的 **Postmix** 帳戶看到您的混合 UTXO。此外，您也可以選擇直接透過 Samourai Wallet 上的 Whirlpool Interface 來檢視和花費它們。若要存取此選單，請按螢幕下方的藍色 `+`，然後選擇 `Whirlpool`。


![coinjoin](assets/notext/52.webp)


在 Samourai Wallet 上，Whirlpool 帳戶的藍色很容易辨認。這可讓您隨時隨地直接使用智慧型手機花費混合 UTXO。


![coinjoin](assets/notext/53.webp)


為了追蹤您的自動接幣情況，我也建議您透過 Sentinel 應用程式設定 Watch-only wallet。添加您的**Postmix**帳戶的ZPUB，並即時監控您的CoinJoin週期的進度。如果您想瞭解如何使用 Sentinel，我建議您參考 PlanB Network 上的其他教學：[**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)