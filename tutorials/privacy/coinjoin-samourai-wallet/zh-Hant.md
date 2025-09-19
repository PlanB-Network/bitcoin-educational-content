---
name: Coinjoin - Samourai Wallet
description: 如何在 Samourai Wallet 上執行 CoinJoin？
---
![cover](assets/cover.webp)


**警告：** Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押後，Whirlpool 工具已不再運作，即使是擁有自己的道場或正在使用 Sparrow Wallet 的個人也是如此。不過，這個工具仍有可能在未來幾週內恢復，或以不同的方式重新推出。此外，這篇文章的理論部分對於了解一般（不只是 Whirlpool）coinjoins 的原則和目標，以及了解 Whirlpool 模型的有效性，仍然具有相關性。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> *街道上的 Bitcoin Wallet*

在本教程中，您將學習什麼是 CoinJoin，以及如何使用 Samourai Wallet 軟體和 Whirlpool 實作執行 CoinJoin。


## 什麼是 Bitcoin 上的 CoinJoin？

**CoinJoin是一種打破比特幣在Blockchain**上的可追蹤性的技術。它依賴於具有同名特定結構的合作交易：CoinJoin 交易。


Coinjoins 會使外部觀察者的連鎖分析變得複雜，從而提高 Bitcoin 使用者的隱私。其結構允許將來自不同使用者的多個硬幣合併為單一交易，從而掩蓋了交易軌跡，使輸入和輸出地址之間的連結難以確定。


CoinJoin 的原則是基於一種協作方式：希望混合比特幣的多位使用者存入相同數額的比特幣作為同一筆交易的輸入。然後，這些金額會作為等值的輸出重新分配給每個使用者。在交易結束時，不可能將特定的輸出與輸入中的已知使用者聯繫起來。輸入與輸出之間不存在直接關聯，打破了使用者與他們的 UTXO 之間的關聯，也打破了每個硬幣的歷史。

![coinjoin](assets/notext/1.webp)


CoinJoin 交易範例 (非本人所為)：[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


為了執行 CoinJoin，同時確保每位使用者都能隨時控制自己的資金，流程一開始是由協調員建立交易，然後將交易傳送給參與者。之後，每位使用者在確認交易適合自己之後，在交易上簽名。所有收集到的簽名最後都會整合到交易中。如果使用者或協調者試圖透過修改 CoinJoin 交易的輸出來轉移資金，簽名將被證明無效，導致節點拒絕交易。


CoinJoin 有幾種實作，例如 Whirlpool、JoinMarket 或 Wabisabi，每種實作的目標都是管理參與者之間的協調，並提高 CoinJoin 交易的效率。

在本教程中，我們將探討**Whirlpool**的實現，我認為這是在Bitcoin上執行coinjoins最有效的解決方案。雖然**Whirlpool**可在多個錢包上使用，但在本教程中，我們將只探討其在 Samourai Wallet 移動應用程式中的使用，而不使用 Dojo。


## 為什麼要在 Bitcoin 上執行共同接合？

任何點對點支付系統的初始問題之一都是雙重消費：如何防止惡意個人多次使用相同的貨幣單位，而無需訴諸中央機構來仲裁？


Satoshi Nakamoto 透過 Bitcoin 協定提供了一個解決這個困境的方案，這是一個獨立於任何中央機關運作的點對點電子支付系統。他在白皮書中強調，證明沒有雙重花費的唯一方法，就是確保支付系統內所有交易的可視性。


為了保證每個參與者都知道交易，這些交易必須公開披露。因此，Bitcoin 的運作依賴於透明且分散式的基礎架構，允許任何節點操作員驗證電子簽章鏈的全部內容，以及每個硬幣從 Miner 製造開始的歷史。


Bitcoin 的 Blockchain 的透明性和分散性意味著任何網路使用者都可以跟蹤和分析所有其他參與者的交易。因此，交易層級的匿名性是不可能的。但是，在個人識別層面上，匿名性得以保留。在傳統銀行系統中，每個帳戶都與個人身份相關聯，而在 Bitcoin 上則不同，資金與成對的加密鑰匙相關聯，因此在加密識別符後為使用者提供了一種假名形式。


因此，當外部觀察者成功將特定的 UTXO 與已識別的使用者聯繫起來時，Bitcoin 的機密性就會受到威脅。一旦建立這種關聯，就有可能追蹤他們的交易並分析他們的比特幣歷史。CoinJoin 正是為了破解 UTXOs 的可追蹤性而開發的技術，從而在交易層面為 Bitcoin 用戶提供一定的 Layer 保密性。


## Whirlpool 如何運作？

Whirlpool 有別於其他 CoinJoin 方法，它使用「_ZeroLink_」交易，確保所有輸入和所有輸出之間完全沒有可能的技術連結。這種完美的混合是透過一種結構來實現的，在這種結構中，每個參與者都提供相同數額的投入（Mining 費用除外），從而產生數額完全相等的輸出。

這種對輸入的限制性方法使 Whirlpool CoinJoin 交易具有一個獨特的特點：輸入和輸出之間完全沒有確定的聯繫。換句話說，與交易中的所有其他輸出相比，每項輸出歸屬於任何參與者的機率相同。

最初，每個 Whirlpool CoinJoin 的參與者人數限制為 5 人，其中有 2 位新加入者和 3 位混音者（我們將進一步解釋這些概念）。然而，在 2023 年觀察到的 On-Chain 交易費用增加，促使 Samourai 團隊重新思考其模式，以提高隱私性，同時降低成本。因此，考慮到費用和參與者數量的市場情況，協調員現在可以組織包括 6、7 或 8 個參與者的 Coinjoins。這些增強的會話被稱為"_Surge Cycles_"。重要的是要注意，無論配置如何，在 Whirlpool 幣會中總是只有 2 個新參與者。


因此，Whirlpool 交易的特點是輸入和輸出的數量相同，可以是：


- 5 組輸入和 5 組輸出；

![coinjoin](assets/notext/2.webp)


- 6 組輸入和 6 組輸出；

![coinjoin](assets/notext/3.webp)


- 7 組輸入和 7 組輸出；

![coinjoin](assets/notext/4.webp)


- 8 組輸入和 8 組輸出。

![coinjoin](assets/notext/5.webp)

因此，Whirlpool 提出的模式是基於 CoinJoin 的小型交易。與 Wasabi 和 JoinMarket 不同，Wasabi 和 JoinMarket 的 anonsets 的穩健性依賴於單一循環中參與者的數量，而 Whirlpool 則賭注於數個小規模循環的連鎖性。


在此模式中，使用者只需在初次進入池中時支付費用，即可參與眾多混音，無需支付額外費用。由新加入者支付混音者的 Mining 費用。


隨著每一個額外的 CoinJoin 幣參與，加上過去遇到的同業，anonsets 將以指數方式成長。因此，我們的目標是利用這些免費的混音，每次出現都有助於強化與每個混合硬幣相關的 anonsets 密度。


Whirlpool 的設計考慮到兩個重要的要求：


- 由於 Samourai Wallet 主要是智慧型手機應用程式，因此可在行動裝置上輕鬆實作；
- 重新混合循環的速度，以促進安寧集的顯著增加。

這些必要因素引導 Samourai Wallet 的開發人員設計 Whirlpool，導致他們限制每個週期的參與者人數。參與人數太少會影響 CoinJoin 的效率，大幅減少每個週期所產生的 anonsets，而參與人數太多則會對行動應用程式造成管理問題，並會妨礙週期的流程。

**終究，Whirlpool 上的每個 CoinJoin 不需要有大量參與者，因為 ONSET 是透過累積數個 CoinJoin 週期來達成的。**


-> 進一步了解 Whirlpool anonsets。


### 水池和 CoinJoin 費用

為了讓這些多重循環能有效地增加混合硬幣的anonsets，必須建立一定的框架來限制UTXO的使用量。因此，Whirlpool 定義了不同的池。


一個池代表一群希望混合在一起的使用者，他們同意使用 UTXO 的數量來優化 CoinJoin 流程。每個池指定固定的 UTXO 數量，使用者必須遵守此數量才能參與。因此，要使用 Whirlpool 執行硬幣接合，您需要選擇一個池。目前可用的池如下：


- 0.5 比特幣
- 0.05 Bitcoin；
- 0.01 Bitcoin；
- 0.001 Bitcoin (= 100,000 Sats)。


用您的比特幣加入一個池後，您的比特幣將會被分到與池中其他參與者完全一致的 generate UTXOs 中。每個池都有最高限額；因此，如果金額超過此限額，您將被迫在同一池中分兩次加入，或者選擇另一個金額更高的池：


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

如前所述，當 UTXO 可整合至 CoinJoin 時，即視為屬於一個池。然而，這並不表示使用者失去對它的擁有權。**這是 CoinJoin 技術與其他集中式混合技術的不同之處。**


要進入 CoinJoin 遊戲池，必須支付服務費以及 Mining 費用。服務費對每個池都是固定的，目的是補償負責開發和維護 Whirlpool 的團隊。

使用 Whirlpool 的服務費僅需在進入池時支付一次。完成這一步之後，您就有機會無限次參與混音，而無需支付任何額外費用。以下是目前每個池的固定費用：


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


這些費用基本上就像是所選池的入場券，無論您投入多少 CoinJoin。因此，無論您是以 0.01 BTC 加入 0.01 遊戲池，還是以 0.5 BTC 加入，費用的絕對值都是一樣的。


因此，在進行共同接合之前，使用者可以在兩種策略之間進行選擇：


- 選擇較小的基金池，以盡量減少服務費，因為他們知道會收到數個小的 UTXO 作為回報；
- 或者喜歡更大的池子，同意支付更高的費用，最終獲得數量減少但價值更高的 UTXO。


一般建議不要在 CoinJoin 循環之後合併數個混合的 UTXO，因為這可能會破壞取得的機密性，尤其是由於共用輸入-Ownership 啟發式 (CIOH) 所造成的。因此，明智的做法可能是選擇較大的資料池，即使這意味著要付出較高的代價，以避免有太多小價值的 UTXO 輸出。使用者必須權衡這些折衷方案，才能選擇自己喜歡的池。


除了服務費，還必須考慮任何 Bitcoin 交易固有的 Mining 費用。身為 Whirlpool 的使用者，您必須支付準備交易 (`Tx0`)的 Mining 費用，以及第一次 CoinJoin 的費用。由於 Whirlpool 的模式是依賴新加入者付費，因此之後所有的混音都是免費的。


事實上，在每個 Whirlpool CoinJoin 中，輸入的使用者中有兩個是新加入者。其他投入來自混音者。因此，交易中所有參與者的 Mining 費用都由這兩個新參與者支付，他們也會從免費的混音中獲益：

![coinjoin](assets/en/6.webp)

得益於這種收費系統，Whirlpool 真正區別於其他 CoinJoin 服務，因為 UTXO 的匿名性與用戶支付的價格不成正比。因此，只需支付入池費和兩筆交易（"Tx0 "和初始組合）的 Mining 費用，就可以實現相當高的匿名級別。

需要注意的是，用戶在完成多個 Coinjoins 後，還需要支付 Mining 費用，才能從池中提取他們的 UTXO，除非他們選擇了 "mix to "選項，我們將在下面的教程中討論。


### Whirlpool 使用的 HD Wallet 帳號

若要透過 Whirlpool 執行 CoinJoin，Wallet 必須 generate 多個不同的帳戶。在 HD (*Hierarchical Deterministic*) Wallet 的情況下，一個帳號構成一個與其他帳號完全隔離的區段，這種隔離發生在 Wallet 層級結構的第三個深度層級，也就是「xpub」層級。


理論上，一個 HD Wallet 最多可衍生出 `2^(32/2)` 不同的帳戶。所有 Bitcoin 錢包預設使用的初始帳戶對應索引 `0'`。


對於適應 Whirlpool 的錢包，如 Samourai 或 Sparrow，使用 4 個帳戶來滿足 CoinJoin 流程的需求：


- 以索引 `0'` 識別的**存款**帳戶；
- **壞銀行** (或哆啦A夢) 帳戶，以索引 `2 147 483 644'` 識別；
- **premix** 帳戶，以索引`2 147 483 645'` 識別；
- **postmix** 帳戶，以索引 `2 147 483 646'` 識別。


這些帳戶在 CoinJoin 流程中各司其職。


所有這些帳戶都連結到單一的 seed，讓使用者可以使用他們的復原短語以及（如適用）他們的 passphrase 來復原存取他們所有的 bitcoins。但是，在此復原作業中，有必要向軟體指定所使用的不同帳戶索引。


現在讓我們看看這些帳戶中 Whirlpool CoinJoin 的不同階段。


### Whirlpool 上不同階段的共同接合

**第 1 階段：Tx0**

任何 Whirlpool CoinJoin 的起始點都是**存款**帳戶。當您建立一個新的 Bitcoin Wallet 時，您會自動使用這個帳戶。這個帳戶必須存入想要混合的比特幣。

Tx0 代表 Whirlpool 混合過程的第一步。其目的是為 CoinJoin 準備和均化 UTXO，將其劃分為與所選池量相對應的單位，以確保混合的均勻性。均化後的 UTXO 會被送至 **premix** 帳戶。至於無法進入混合池的差額，則會被分到一個特定的帳戶：**不良庫**（或稱為「毒性變化」）。

此初始交易 `Tx0` 也用來結清應付給混合協調器的服務費用。與下面的步驟不同，此交易不是協作式的；因此使用者必須承擔所有的 Mining 費用：

![coinjoin](assets/en/7.webp)


在這個 `Tx0` 交易的範例中，來自我們 ** 存款** 帳戶的 `372,000 Sats` 輸入被分成數個輸出 UTXO，其分佈如下：


- 5,000Sats 「的款項擬用於協調員的服務費，相應於進入 」100,000Sats "的池；
- 三個準備混合的 UTXO，轉到我們的 **premix** 帳戶，並向協調員註冊。這些 UTXO 的均勻價各為 `108,000 Sats`，以支付其未來初始混合的 Mining 費用；
- 不能進入池中的盈餘，因為太小，被視為有毒變更。它會被送到特定的帳戶。在此，此變化為「40,000 Sats」；
- 最後，有`3,000 Sats`不構成輸出，而是確認`Tx0`所需的 Mining 費用。


例如，這裡有一個真實的 Whirlpool Tx0 (不是我提供的)：[edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**第 2 步：毒性變化**

無法併入池中的盈餘（在此相當於`40,000 Sats`）會被轉至**壞銀行**帳戶，也稱為 "doxxic change"，以確保與 Wallet 中的其他 UTXO 嚴格分離。


這個 UTXO 對使用者的隱私而言是很危險的，因為它不僅仍依附於它的過去，因此也可能依附於它擁有者的身分，此外，它也被記下來是屬於執行過 CoinJoin 的使用者。

如果將 UTXO 與混合輸出合併，則會失去在 CoinJoin 循環過程中獲得的所有機密性，特別是因為共用輸入-Ownership-驅動程式 (CIOH)。如果與其他毒性變更合併，使用者會冒失去機密性的風險，因為這會連結 CoinJoin 循環的不同輸入。因此，必須謹慎處理。管理這種毒性 UTXO 的方法將在本文最後一部分詳述，未來的教學將更深入地介紹 PlanB Network 上的這些方法。


**第 3 步：初步混合**

在 `Tx0` 完成後，均衡後的 UTXO 將傳送至 Wallet 的 **premix** 帳戶，準備導入其第一個 CoinJoin 循環，也稱為「初始混合」。如果在我們的範例中，`Tx0`產生多個UTXO進行混合，則每個UTXO都會被整合到單獨的初始CoinJoin中。


在這些第一次混合結束時，**premix** 帳戶將為空，而我們的硬幣在支付了第一個 CoinJoin 的 Mining 費用後，將完全調整為所選池所定義的金額。在我們的例子中，我們最初的 `108 000 Sats` 的 UTXOs 將減少到正好 `100 000 Sats`。

![coinjoin](assets/en/8.webp)

**第四步：混音**

初始混音之後，UTXOs 會被轉移到 **postmix** 帳戶。此帳戶收集已混合的 UTXO 和等待重新混合的 UTXO。當 Whirlpool 用戶端啟動時，**postmix** 帳戶中的 UTXO 會自動可供重新混合，並會隨機選擇參與這些新週期。


需要提醒的是，混音是 100% 免費的：不需要額外的服務費或 Mining 費用。因此，將 UTXOs 保留在 ** 後混合 ** 帳戶中，可保持其價值不變，並同時提高其匿名性。這就是為什麼允許這些錢幣參與多次 CoinJoin 循環的重要性。嚴格來說，您不需要花費任何金錢，而且還能提高它們的匿名性。


當您決定使用混合的 UTXO 時，您可以直接從這個 **postmix** 帳戶使用。建議您將混合 UTXO 保留在此帳戶中，以享受免費混音，並避免其離開 Whirlpool 電路，從而降低其保密性。


正如我們將在下面的教學中看到的，還有 "mix to "選項，它提供了自動將您的混合硬幣傳送到另一個 Wallet 的可能性，例如在定義的硬幣接合次數之後的 Cold Wallet。

在介紹完理論之後，讓我們透過 Samourai Wallet Android 應用程式使用 Whirlpool 的教學來深入實作！


## 教學：CoinJoin Whirlpool on Samourai Wallet

使用 Whirlpool 有許多選項。我在此要介紹的是 Samourai Wallet 選項 (不含 Dojo)，這是 Android 上的開放原始碼 Bitcoin Wallet 管理應用程式。


在 Samourai 上混音而不使用 Dojo 的優點是相當容易操作、設定快速，而且除了 Android 手機和網際網路連線之外，不需要其他裝置。


但是，這種方法有兩個明顯的缺點：


- Coinjoins 只會在 Samourai 於背景執行且連線時發生。這意味著如果您想全天候混合比特幣，您必須持續開啟 Samourai；
- 如果您使用 Whirlpool 與 Samourai Wallet 而沒有注意連接您自己的 Dojo，那麼您的應用程式將必須連線到由 Samourai 團隊維護的伺服器，而您將會透露您 Wallet 的 `xpub` 給他們。這些匿名資訊對於您的應用程式找到您的交易是必要的。


克服這些限制的理想解決方案是在您個人的 Bitcoin 節點上，操作與 Whirlpool CLI 實例相關的您自己的 Dojo。這樣，您就可以避免任何資訊洩漏，並達到完全獨立。雖然下面介紹的教學對某些目標或初學者很有用，但要真正優化您的 CoinJoin 會話，建議使用您自己的 Dojo。PlanB Network 即將提供設定此組態的詳細指南。


### 安裝 Samourai Wallet

要開始使用，您顯然需要 Samourai Wallet 應用程式。您可以使用 APK 直接從官方網站、GitLab 或 Google Play 商店下載。


### 建立 Software Wallet

安裝軟體後，您需要在 Samourai 上建立 Bitcoin Wallet。如果您已經有一個，可以直接跳到下一步。


開啟應用程式後，按下藍色的「開始」按鈕。接著會要求您在手機檔案中選擇儲存新 Wallet 加密備份的位置。


![samourai](assets/notext/9.webp)

按一下相應的缺口即可啟動 Tor。在此階段，您也可以選擇特定的 Dojo。但是，在本教程中，我們將繼續使用預設的 Dojo；所以您可以不啟用該選項。Tor 連線後，按下「建立新的 Wallet」按鈕。

![samourai](assets/notext/10.webp)


Samourai Wallet 會提示您設定 BIP39 passphrase。這個額外的密碼非常重要，因為它直接作用於您的私密金鑰的推導。如果遺失了這個 passphrase，將導致您無法存取您的比特幣，使其無法復原。要恢復您的 Samourai Wallet，必須同時擁有您的 12 字恢復短語和 passphrase。


因此，選擇一個堅固的 passphrase，並在紙張或金屬介質上做一個或多個實體副本，以確保您比特幣的安全是非常重要的。完成這些任務後，勾選 `我知道如果遺失...'，然後按下 `NEXT` 按鈕。


![samourai](assets/notext/11.webp)


然後，您必須定義一個由 5 到 8 位數組成的 PIN 碼。此密碼將確保您在手機上存取 Wallet。每次您要開啟 Samourai 應用程式時，系統都會要求您輸入此密碼。請選擇一個可靠的 PIN 碼，並確保保留一份備份。之後，您可以按下`NEXT`按鈕。


![samourai](assets/notext/12.webp)


Samourai會請您再次輸入PIN碼進行確認。輸入後按下 `FINALIZE`。


![samourai](assets/notext/13.webp)


接下來您將存取由 12 個單字組成的復原短語。這個短語允許您用之前輸入的 passphrase 復原您的 Wallet。強烈建議將此短語複製一份或多份在實體媒體上，例如紙張或金屬材料，以確保您的比特幣在發生問題時的安全性。


進行這些備份之後，您將會被導引至您新的 Samourai Wallet 的 Interface。


![samourai](assets/notext/14.webp)


您可獲取您的 PayNym Bot。如果您願意，您可以要求它，儘管它對我們的教學並非必要。


![samourai](assets/notext/15.webp)

在繼續在這個新的Wallet上接收比特幣之前，強烈建議重新檢查您的Wallet備份（passphrase和恢復短語）的有效性。要驗證 passphrase，您可以選擇位於螢幕左上方的 PayNym Bot 圖示，然後沿著路徑走：

```plaintext
Settings > Troubleshooting > Passphrase/backup test
```


輸入您的 passphrase 執行驗證。


![samourai](assets/notext/16.webp)


Samourai 將確認其是否有效。


![samourai](assets/notext/17.webp)


要驗證您的恢復短語備份，請訪問您的 PayNym Bot 的圖標，位於屏幕左上方，並按照此路徑：

```plaintext
Settings > Wallet > Show 12-word recovery phrase
```


Samourai 將顯示一個視窗，其中包含您的復原短語。確保它與您的實體備份完全匹配。


若要進一步執行完整的復原測試，請記下 Wallet 的見證元素，例如其中一個 `xpubs`，然後繼續刪除您的 Wallet（前提是它仍然是空的）。目標是嘗試只使用您的實體備份還原這個空的 Wallet。如果還原成功，這表示您的備份是有效且可靠的。


### 接收比特幣

建立您的 Wallet 之後，您會從單一帳戶開始，以索引 `0'`來識別。這就是我們在前面談到的**存款**帳戶。您需要將用於 Coinjoins 的 bitcoins 轉移到這個帳戶。


若要執行此操作，請按一下螢幕右下方的藍色 `+` 符號。


![samourai](assets/notext/18.webp)


然後按一下 Green `Receive` 按鈕。


![samourai](assets/notext/19.webp)


Samourai 會自動 generate 一個新的空白 Address 來接收 bitcoins。


![samourai](assets/notext/20.webp)


您可以將比特幣寄到那裡混合。


![samourai](assets/notext/21.webp)


### 製作 Tx0

當交易確認後，我們就可以開始 Coinjoins 程序。要做到這一點，請點擊螢幕右下方的藍色 `+` 按鈕。


![samourai](assets/notext/22.webp)


然後按一下藍色的「Whirlpool」。


![samourai](assets/notext/23.webp)


等待 Whirlpool 初始化和 Samourai 建立必要的帳戶。


![samourai](assets/notext/24.webp)


然後您就會到達 Whirlpool 首頁。按一下「開始」。

![samourai](assets/notext/25.webp)

從 ** 存款** 帳戶中選擇您希望以 CoinJoin 循環傳送的 UTXO，然後按一下`下一步'。


![samourai](assets/notext/26.webp)


在下一步中，您需要選擇分配給 `Tx0` 以及您的首次混合的費用等級。此設定將決定您的 `Tx0` 與您的初始 CoinJoin（或初始合幣）的確認速度。請記住，`Tx0`和初始混音的 Mining 費用由您負責，但後續的重新混音則無需支付 Mining 費用。您可以選擇 `Low`、`Normal` 或 `High`。


![samourai](assets/notext/27.webp)


在同一個視窗中，您可以選擇要輸入的池。鑒於我最初選擇的 UTXO 是 `454,258 Sats`，我唯一可能的選擇是 `100,000 Sats` 池。除了 Mining 的費用之外，此頁面也會為您呈現水池的服務費用，讓您知道這個 CoinJoin 週期的總費用。如果一切都適合您，請選擇合適的池，然後點擊藍色的 `VERIFY CYCLE DETAILS` 按鈕繼續。


![samourai](assets/notext/28.webp)


然後您就可以看到 CoinJoin 循環的所有詳細資訊：


- 將進入池中的 UTXO 數量；
- 所產生的各種費用；
- 毒性變化的量...


確認資訊，然後按一下 Green `START CYCLE` 按鈕。


![samourai](assets/notext/29.webp)


一個視窗將會出現，提供您標記您進入CoinJoin循環所產生的毒性變化為 「不可花費」。選擇 「是」，這個UTXO將不會在您的Wallet中顯示，也不能在未來的交易中被選擇。但是，它仍然可以在 Wallet 的 UTXOs 清單中被訪問，您可以手動改變它的狀態。建議您選擇此選項，以避免日後出現處理錯誤，影響您的隱私。如果您選擇 "NO"，毒性變更仍可在您的 Wallet 中使用。如果您想瞭解更多關於管理和使用有毒變更的資訊，我建議您閱讀本教程的最後一部分。


![samourai](assets/notext/30.webp)


Samourai 接著會廣播您的 Tx0。


![samourai](assets/notext/31.webp)


### 製作共同接合

一旦 Tx0 被廣播，您就可以在 Whirlpool 功能表的「交易」索引標籤中找到它。


![samourai](assets/notext/32.webp)

您準備好混合的 UTXO 在「混合中...」標籤中，該標籤對應於 **Premix** 帳戶。

![samourai](assets/notext/33.webp)


一旦 `Tx0` 確認，您的 UTXO 將自動向協調器註冊，初始混音將以自動方式相繼啟動。


![samourai](assets/notext/34.webp)


通過檢查與 **Postmix** 帳戶相對應的 "Remixing "標籤，您可以觀察到初始混合產生的 UTXO。這些錢幣將繼續為後續的混幣做好準備，混幣不會產生任何額外費用。我建議參考這篇其他文章，以瞭解更多關於重新混合過程和 CoinJoin 循環的效率：[REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


![samourai](assets/notext/35.webp)


按下 UTXO 右側的暫停按鈕，即可暫停 UTXO 的混音。若要再次進行混音，只要再按一次相同的按鈕即可。請注意，每個使用者和每個池只能同時執行一個 CoinJoin。因此，如果您有 6 個 `100 000 Sats` 的 UTXO 已準備好進行 CoinJoin，則只能混合其中一個。在混合一個 UTXO 之後，Samourai Wallet 會從您的可用性中隨機選擇一個新的 UTXO，以分散和平衡每個硬幣的再混合。


![samourai](assets/notext/36.webp)


為了確保您的 UTXO 能持續可用於混音，有必要讓 Samourai 應用程式在背景中維持運作。您應該會在手機上看到確認 Whirlpool 正在執行的通知。關閉應用程式或關閉手機將會暫停幣兌。


### 完成共同接合

要使用您混合的 bitcoins，請前往 Whirlpool 功能表選項卡中註明 `Remixing` 的 **Postmix** 帳戶。


![samourai](assets/notext/37.webp)


按一下位於右下方的藍色 Whirlpool 標誌。


![samourai](assets/notext/38.webp)


然後按一下 `Spend Mixed UTXOs`。


![samourai](assets/notext/39.webp)


然後，您可以輸入收款人的 Address 和要傳送的金額，方式與其他使用 Samourai Wallet 進行的交易相同。藍色背景表示資金是從 Whirlpool 帳戶支出，而不是從**存款**帳戶支出。


![samourai](assets/notext/40.webp)


按一下右上方的 3 個小圓點，您就可以選擇特定的 UTXO。

![samourai](assets/notext/41.webp)

按一下視窗右上方的白色方塊，即可使用相機掃描接收 Address 的 QR 代碼。


![samourai](assets/notext/42.webp)


輸入消費交易的必要資訊，然後按一下藍色的「驗證交易」按鈕。


![samourai](assets/notext/43.webp)


在下一步中，您可以選擇修改與交易相關的費率。您也可以通過勾選相應的方塊來啟用 「石牆 」選項。如果 「石牆 」選項無法選擇，則表示您的 **Postmix** 帳戶中沒有足夠大小的 UTXO 來支援此特定交易結構。


[-> 進一步瞭解石牆交易](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


如果一切都令您滿意，請按 Green `SEND ... BTC` 按鈕。


![samourai](assets/notext/44.webp)


Samourai 會在您的交易在網路中廣播之前進行簽署。您只需等待 Miner 將交易加入區塊即可。


![samourai](assets/notext/45.webp)


### 使用 SCODE

Samourai Wallet 球隊有時會提供「SCODE」。SCODE 是一種促銷代碼，可為游泳池的服務費提供折扣。Samourai Wallet 偶爾會在特別活動期間提供這樣的代碼給使用者。我建議您 [在社交媒體上追蹤 Samourai Wallet](https://twitter.com/SamouraiWallet)，以免錯過未來的 SCODE。


若要在 Samourai 上套用 SCODE，在開始新的 CoinJoin 循環之前，請前往 Whirlpool 功能表，並選擇位於螢幕右上方的三個小圓點。


![samourai](assets/notext/46.webp)


按一下「SCODE (促銷代碼) Whirlpool」。


![samourai](assets/notext/47.webp)


在開啟的視窗中輸入 SCODE，然後按一下`OK`進行驗證。


![samourai](assets/notext/48.webp)


Whirlpool 會自動關閉。等待 Samourai 載入完成後，再次開啟 Whirlpool 功能表。


![samourai](assets/notext/49.webp)


再次點擊三個小圓點，然後選擇「SCODE (促銷代碼) Whirlpool」，確定您的 SCODE 已正確註冊。如果一切正常，您就可以開始一個新的 Whirlpool 循環，並享受服務費折扣。需要注意的是，這些 SCODE 是臨時的：在過期前的幾天內仍然有效。


## 如何瞭解我們 CoinJoin 循環設備的品質？

要使 CoinJoin 真正有效，它必須顯示出輸入和輸出金額之間的一致性。這種均勻性擴大了外部觀察者眼中可能的詮釋數量，從而增加了交易的不確定性。為了量化 CoinJoin 所產生的不確定性，我們可以計算交易的熵。


若要深入探討這些指標（Whirlpool 模型被公認為能為共同接合帶來最大同质性的模型），請參考教學：[boltzmann calculator](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)


接下來，我們會根據硬幣被隱藏的群組程度來評估幾個 CoinJoin 循環的效能。這些群組的大小定義了所謂的 anonsets。有兩種類型的 anonsets：第一種是針對回溯分析（從現在到過去）來評估所獲得的隱藏性，第二種是針對前瞻分析（從過去到現在）來評估所獲得的隱藏性。如需這兩個指標的詳細說明，請參閱教學：Whirlpool STATS TOOLS - ANONSETS


## 如何管理後混合？

執行 CoinJoin 循環之後，最好的策略是將您的 UTXO 保留在 **postmix** 帳戶中，等待將來使用。甚至建議您無限期地讓它們重新混合，直到您需要使用它們為止。


有些用戶可能會考慮將其混合的比特幣轉移到由 Hardware Wallet 保護的 Wallet。這是有可能的，但重要的是要仔細遵循 Samourai Wallet 的建議，以免影響獲取的機密性。


合併 UTXOs 是最常犯的錯誤。為了避免 CIOH（*Commun-Input-Ownership-Heuristic*），必須避免在同一個交易中將混合的 UTXO 與未混合的 UTXO 合併。這需要在 Wallet 內小心管理您的 UTXO，特別是在標籤方面。除了 CoinJoin 之外，合併 UTXOs 通常是一種不好的做法，如果管理不當，往往會導致失密。

您還應該警惕混合 UTXOs 之間的相互鞏固。如果您的混合 UTXOs 有顯著的匿名性，則可以進行適度的合併，但這將不可避免地降低您的錢幣的隱私性。請確保合併既不會太大，也不會在重新混合次數不足後進行，因為這有可能在 CoinJoin 循環之前和之後，在您的 UTXOs 之間建立可推斷的連結。如果對這些作業有疑問，最好的做法是不要合併混合後的 UTXO，而是將它們逐一轉移到您的 Hardware Wallet，每次都產生新的空白 Address。再次提醒您，請記得正確標示每個接收到的 UTXO。


此外，也建議您不要使用不常用的腳本將您的postmix UTXOs轉移到Wallet。例如，如果您使用 `P2WSH` 腳本從 Multisig Wallet 進入 Whirlpool，您幾乎不可能與其他原本擁有相同類型 Wallet 的使用者混在一起。如果您退出您的後混合到這個相同的 Multisig Wallet，您的混合比特幣的隱私級別將大大降低。除了腳本之外，還有許多其他的 Wallet 指紋可以騙你。


與任何 Bitcoin 交易一樣，也不宜重複使用收件地址。每筆新交易都必須使用新的空白 Address 收件。


最簡單和安全的解決方案是讓您混合的 UTXO 在其 **postmix** 帳戶中休息，讓它們重新混合，並只在花費時才碰觸它們。Samourai 和 Sparrow 錢包有額外的保護措施，可避免所有這些與鍊分析相關的風險。這些保護措施可以幫助您避免犯錯。


## 如何管理毒性變化？

接下來，您必須小心管理有毒的變更，也就是無法進入 CoinJoin 池的變更。這些因使用 Whirlpool 而產生的毒性 UTXOs 會對您的隱私構成風險，因為它們會在您與 CoinJoin 的使用之間建立連結。因此，必須謹慎處理，不要將它們與其他 UTXOs（特別是混合 UTXOs）結合在一起。以下是使用它們時要考慮的不同策略：


- 在較小的水池中混合使用：**如果您的毒性 UTXO 大到足以單獨進入較小的水池，請考慮混合使用。這通常是最好的選擇。但是，關鍵是不要將幾個有毒的 UTXO 合併進入一個池中，因為這可能會將您的不同入口連結起來。**
- 將它們標記為「不可花費」：**另一種方法是停止使用，在專用帳戶中將它們標記為「不可花費」，並直接使用 HODL。這樣可以確保您不會不小心花掉它們。如果 Bitcoin 的價值增加，可能會出現更適合您的有毒 UTXOs 的新池；**
- 捐款：請考慮捐款，即使是微不足道的捐款，也要捐給研究 Bitcoin 及其相關軟體的開發人員。您也可以捐款給接受 BTC 的組織。如果管理您的有毒 UTXOs 看起來太複雜，您可以直接透過捐款來擺脫它們；
- 購買禮品卡：**[Bitrefill](https://www.bitrefill.com/)** 等平台允許您用 Exchange 比特幣購買禮品卡，這些禮品卡可以在各種商家使用。這可以在不損失相關價值的情況下，將有毒的 UTXOs 處理掉；
- 在 Monero 上整合它們：**Samourai Wallet 現在提供 BTC 和 XMR 之間的原子交換服務。這是管理有毒 UTXOs 的理想選擇，您可以將它們整合到 Monero 上，而不會透過 KYC 洩露您的隱私，然後再將它們送回 Bitcoin。但是，由於流動性的限制，這個選擇在 Mining 費用和溢價方面可能會很昂貴**；
- 將它們傳送至 Lightning Network：將這些 UTXO 傳送至 Lightning Network 以享受交易費用的降低，是一個很有趣的選擇。但是，此方法可能會透露某些資訊，這取決於您對 Lightning 的使用，因此應謹慎實行。


PlanB Network 即將提供實施這些不同技術的詳細教學。


**其他資源：**

[Samourai Wallet video tutorial]()


- [Samourai Wallet Documentation - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts)；
- [Twitter thread on coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739)；
- [Blog post on coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).
