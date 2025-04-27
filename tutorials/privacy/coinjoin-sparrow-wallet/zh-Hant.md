---
name: CoinJoin - 麻雀 Wallet
description: 如何在 Sparrow Wallet 上執行 CoinJoin？
---
![cover](assets/cover.webp)


***警告：** Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押後，Whirlpool 工具已不再運作，即使是擁有自己的道場或正在使用 Sparrow Wallet 的個人也是如此。不過，這個工具仍有可能在未來幾週內恢復，或以不同的方式重新推出。此外，這篇文章的理論部分對於了解一般（不只是 Whirlpool）coinjoins 的原則和目標，以及了解 Whirlpool 模型的有效性，仍然具有相關性。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

在本教程中，您將學習什麼是 CoinJoin，以及如何使用 Sparrow Wallet 軟體和 Whirlpool 實作執行 CoinJoin。


## 什麼是 Bitcoin 上的 CoinJoin？

**CoinJoin是一種打破比特幣在Blockchain**上的可追蹤性的技術。它依賴於具有同名特定結構的合作交易：CoinJoin 交易。


Coinjoins 會使外部觀察者的連鎖分析變得複雜，從而提高 Bitcoin 使用者的隱私。它們的結構允許將不同使用者的多個硬幣合併為單一交易，從而使交易軌跡變得模糊，難以確定輸入和輸出地址之間的聯繫。


CoinJoin 的原理是基於一種協作方式：希望混合比特幣的多位使用者存入相同數額的比特幣作為同一筆交易的輸入。然後，這些金額會作為等值的輸出重新分配給每個使用者。在交易結束時，不可能將特定的輸出與輸入的已知使用者聯繫起來。輸入與輸出之間不存在直接關聯，這就打破了使用者與其 UTXO 之間的關聯，也打破了每個硬幣的歷史。

![coinjoin](assets/notext/1.webp)


CoinJoin 交易範例 (非本人所為)：[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


為了在執行 CoinJoin 的同時，確保每位使用者都能隨時控制自己的資金，流程一開始是由協調員建立交易，然後將交易傳送給每位參與者。之後，每位使用者在確認交易適合自己之後，在交易上簽名。所有收集到的簽名最後都會整合到交易中。如果使用者或協調人試圖透過修改 CoinJoin 交易的輸出來轉移資金，簽名將被證明無效，導致交易被節點拒絕。


CoinJoin 有多種實作，例如 Whirlpool、JoinMarket 或 Wabisabi，每種實作都旨在管理參與者之間的協調，並提高 CoinJoin 交易的效率。


在本教程中，我們將專注於**Whirlpool**實現，我認為這是在 Bitcoin 上執行硬幣接合的最有效解決方案。儘管它可在多個錢包上使用，但本教程僅探討其與 Sparrow Wallet Desktop 軟體的搭配使用。

## 為什麼要在 Bitcoin 上執行 CoinJoins？


任何點對點支付系統的初始問題之一是 Double-spending：如何防止惡意個人多次使用相同的貨幣單位，而不訴諸一個中央機構進行仲裁？


Satoshi Nakamoto 透過 Bitcoin 協定提供了一個解決這個困境的方案，Bitcoin 協定是一個獨立於任何中央機關運作的點對點電子支付系統。他在白皮書中強調，證明 Double-spending 不存在的唯一方法，就是確保支付系統內所有交易的可見性。


為了確保每個參與者都知道交易，這些交易必須公開披露。因此，Bitcoin 的運作有賴於透明且分散式的基礎架構，允許任何節點操作者驗證電子簽章鏈的全部內容，以及每個硬幣從 Miner 製造開始的歷史。


Bitcoin 的 Blockchain 的透明性和分散性意味著任何網路使用者都可以跟蹤和分析所有其他參與者的交易。因此，交易層級的匿名性是不可能的。但是，在個人識別層面上，匿名性得以保留。在傳統銀行系統中，每個帳戶都與個人身份相關聯，而在 Bitcoin 上則不同，資金與成對的加密鑰匙相關聯，因此在加密識別符後為使用者提供了一種假名形式。


因此，當外部觀察者成功將特定的 UTXO 與已識別的使用者聯繫起來時，Bitcoin 的機密性就會受到威脅。一旦建立了這種關聯，就有可能追蹤他們的交易並分析他們的比特幣歷史。CoinJoin 正是為了破解 UTXOs 的可追蹤性而開發的技術，從而在交易層面上為 Bitcoin 用戶提供一定的 Layer 保密性。


## Whirlpool 如何運作？


Whirlpool 有別於其他 CoinJoin 方法，它使用「_ZeroLink_」交易，確保所有輸入和所有輸出之間完全沒有可能的技術連結。這種完美的混合是透過一種結構來實現的，在這種結構中，每個參與者都提供相同數額的投入（Mining 費用除外），從而產生數額完全相等的輸出。


Whirlpool CoinJoin 交易在輸入方面的這種限制性方法賦予了它一個獨特的特點：輸入和輸出之間完全沒有確定的聯繫。換句話說，與交易的所有其他輸出相比，每項輸出歸屬於任何參與者的機率相同。

最初，每個 Whirlpool CoinJoin 的參與者人數限制為 5 人，其中有 2 位新加入者和 3 位混音者（我們將進一步解釋這些概念）。然而，在 2023 年觀察到的 On-Chain 交易費用增加，促使 Samourai 團隊重新思考其模式，以提高隱私性，同時降低成本。因此，考慮到費用和參與者數量的市場情況，協調員現在可以組織包括 6、7 或 8 個參與者的 Coinjoins。這些增強的會話被稱為"_Surge Cycles_"。重要的是要注意，無論設置如何，在 Whirlpool 幣會中總是只有 2 個新參與者。


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


在這種模式下，使用者僅在初次進入池時產生費用，讓他們可以參與眾多的混音，而無需額外收費。是新加入者為混音者承擔 Mining 費用。


隨著每一個額外的 CoinJoin 幣參與，加上其過去遇到的同伴，anonsets 將以指數方式成長。因此，我們的目標是利用這些免費的混音，每次出現都有助於強化與每個混合硬幣相關的 anonsets 密度。


Whirlpool 的設計考慮到兩個重要的要求：


- 由於 Samourai Wallet 主要是智慧型手機應用程式，因此可在行動裝置上輕鬆實作；
- 重新混合循環的速度，以促進安寧集的顯著增加。


這些必要因素引導 Samourai Wallet 的開發人員在設計 Whirlpool 時做出選擇，導致他們限制每個週期的參與者人數。參與人數太少會影響 CoinJoin 的效能，大幅減少每個週期所產生的 anonsets，而參與人數太多則會對行動應用程式造成管理問題，並會阻礙週期的流程。


**最終，Whirlpool 上每個 CoinJoin 的參與者人數不需要太多，因為取消設定是在幾個 CoinJoin 週期的累積下完成的。

[-> 進一步了解 Whirlpool anonsets。](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### CoinJoin 游泳池和費用

為了確保多重循環能有效地增加混合硬幣的anonsets，必須建立一定的框架來限制所使用的UTXOs數量。Whirlpool 為此定義了不同的池。


一個池代表一群希望混合在一起的使用者，他們同意使用多少 UTXO 來優化 CoinJoin 流程。每個池指定 UTXO 的固定金額，使用者必須遵守才能參與。因此，要使用 Whirlpool 執行合幣，您需要選擇一個池。目前可用的池如下：


- 0.5 比特幣
- 0.05 Bitcoin；
- 0.01 Bitcoin；
- 0.001 Bitcoin (= 100,000 Sats)。


用您的比特幣加入一個池後，您的比特幣將被分到與池中其他參與者完全一致的 generate UTXOs 中。每個池都有最高限額；因此，如果金額超過此限額，您將被迫在同一池中分兩次加入，或轉入另一個金額更高的池：


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

如前所述，當 UTXO 可整合至 CoinJoin 時，即視為屬於一個池。然而，這並不表示使用者失去對它的擁有權。 *** 這就是 CoinJoin 技術與其他集中式混合技術的差異。


要進入 CoinJoin 遊戲池，必須支付服務費以及 Mining 費用。服務費對每個池都是固定的，目的是補償負責開發和維護 Whirlpool 的團隊。對於 Sparrow Wallet 使用者，這些費用由 Samourai 團隊轉嫁給 Sparrow 的開發人員。


使用 Whirlpool 的服務費需在進入池時支付一次。完成這一步驟後，您就有機會不限次數參與混音，無需支付額外費用。以下是目前每個池的固定費用：


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


無論您投入多少 CoinJoin，這些費用基本上都是所選池的入場券。因此，無論您是以 0.01 BTC 恰好加入 0.01 池，還是以 0.5 BTC 加入，費用的絕對值都是一樣的。


因此，在進行共同接合之前，使用者可以在兩種策略之間進行選擇：


- 選擇較小的基金池，以盡量減少服務費，因為他們知道會收到數個小的 UTXO 作為回報；
- 或偏好較大的池子，同意支付較高的費用，以減少價值較高的 UTXO 的數量。


一般建議不要在 CoinJoin 循環之後合併數個混合的 UTXO，因為這可能會破壞取得的機密性，尤其是由於共用輸入-Ownership 啟發式 (CIOH) 所造成的。因此，明智的做法可能是選擇較大的資料池，即使這意味著要付出較高的代價，以避免有太多小價值的 UTXO 輸出。使用者必須權衡這些利弊得失，才能選擇自己喜歡的池。


除了服務費之外，還必須考慮任何 Bitcoin 交易固有的 Mining 費用。身為 Whirlpool 的使用者，您必須支付準備交易 (`Tx0`)的 Mining 費用，以及第一次 CoinJoin 的費用。由於 Whirlpool 的模式是依賴新加入者付費，因此之後所有的混音都是免費的。


事實上，在每個 Whirlpool CoinJoin 中，輸入的使用者中有兩個是新加入者。其他投入來自混音者。因此，交易中所有參與者的 Mining 費用都由這兩個新參與者支付，他們也會從免費的混音中獲益：

![coinjoin](assets/en/6.webp)

得益於此費用系統，Whirlpool 真正區別於其他 CoinJoin 服務，因為 UTXOs 的匿名性與用戶支付的價格不成正比。因此，只需為兩筆交易（"Tx0 "和初始組合）支付池的入池費和 Mining 費用，就有可能實現相當高的匿名級別。


需要注意的是，用戶在完成多個 Coinjoins 後，還需要支付 Mining 費用，才能從池中提取他們的 UTXO，除非他們選擇了 "mix to "選項，我們將在下面的教程中討論。


### Whirlpool 使用的 HD Wallet 帳號

要透過 Whirlpool 執行 CoinJoin，Wallet 必須 generate 多個不同的帳戶。在 HD (Hierarchical Deterministic) Wallet 的情況下，一個帳號構成一個與其他帳號完全隔離的區段，這種隔離發生在 Wallet 層級結構的第三個深度層級，也就是「xpub」層級。

理論上，一個 HD Wallet 最多可衍生出 `2^(32/2)` 不同的帳戶。所有 Bitcoin 錢包預設使用的初始帳戶對應索引 `0'`。


對於適應 Whirlpool 的錢包，如 Samourai 或 Sparrow，使用 4 個帳戶來滿足 CoinJoin 流程的需求：


- 以索引 `0'` 識別的**存款**帳戶；
- **壞銀行** (或哆啦A夢) 帳戶，以索引 `2 147 483 644'` 識別；
- **premix** 帳戶，以索引`2 147 483 645'` 識別；
- **postmix** 帳戶，以索引 `2 147 483 646'` 識別。


每個帳戶都在 CoinJoin 內履行特定的功能。


所有這些帳號都連結到單一的 seed，使用者可以使用他們的復原用語及（如適用）他們的 passphrase 來復原存取他們所有的 bitcoins。但是，在此復原作業中，有必要向軟體指定所使用的不同帳戶索引。


現在讓我們看看這些帳戶中 Whirlpool CoinJoin 的不同階段。


### Whirlpool 上不同階段的共同接合

**第 1 階段：Tx0**

任何 Whirlpool CoinJoin 的起始點都是**存款**帳戶。當您建立一個新的 Bitcoin Wallet 時，您會自動使用這個帳戶。這個帳戶必須存入您想要混合的比特幣。


Tx0代表Whirlpool混合過程的第一階段。其目的是為 CoinJoin 準備和均衡UTXOs，將其劃分為與所選池量相對應的單位，以確保混合的均勻性。均分後的 UTXOs 會被送至 **premix** 帳戶。至於無法進入池中的差額，則會被分到一個特定的帳戶：**不良庫**（或稱為 「毒性變化」）。


此初始交易 `Tx0` 也用來結清應付給混合協調器的服務費用。與以下階段不同的是，此交易不是協作式的；因此使用者必須承擔全部的 Mining 費用：

![coinjoin](assets/en/7.webp)

在這個交易`Tx0`的範例中，從我們的**存款**帳戶輸入的`372,000 Sats`分為數個輸出的 UTXO，其分佈如下：


- 5,000Sats 「的金額，擬用於協調員的服務費，相對應於進入池的 」100,000Sats"；
- 三個準備混合的 UTXO，轉到我們的 **premix** 帳戶，並向協調員註冊。這些 UTXO 每顆均等為 `108,000 Sats`，以支付其未來初始混合的 Mining 費用；
- 盈餘因為太小而無法進入池中，被視為有毒變化。它被送到其特定帳戶。在此，此變化量為`40,000 Sats`；
- 最後，有`3,000 Sats`不構成輸出，而是確認`Tx0`所需的 Mining 費用。


例如，這裡有一個真實的 Tx0 Whirlpool（並非來自我）：[edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


*第 2 步：毒性改變***

未能融入池中的盈餘（在此相當於`40,000 Sats`）會被轉至**壞銀行**帳戶，也稱為 「有毒變化」，以確保與 Wallet 中的其他 UTXO 嚴格分離。


這個 UTXO 對使用者的隱私是很危險的，因為它不只總是附著在它的過去，因此也可能附著在它的擁有者的身分上，此外，它也被記下來是屬於執行過 CoinJoin 的使用者。


如果此 UTXO 與混合輸出合併，後者將喪失在 CoinJoin 循環過程中獲得的所有隱私，特別是因為 CIOH（*Commun-Input-Ownership-Heuristic*）。如果與其他毒性變更合併，使用者就有可能失去隱私，因為這會連結 CoinJoin 循環的不同項目。因此必須謹慎處理。管理此有毒 UTXO 的方法將在本文最後一部分詳述，未來的教學將深入探討 PlanB 網路上的這些方法。


**第 3 步：初步混合**

在完成 `Tx0` 之後，均衡的 UTXO 會傳送到 Wallet 的 **premix** 帳戶，準備導入 CoinJoin 的第一週期，也稱為「初始混合」。如果在我們的範例中，`Tx0`產生多個要混合的 UTXO，每個都會整合到單獨的初始 CoinJoin 中。

在這些初始混合結束時，**premix** 帳戶將為空，而我們的硬幣在支付了第一個 CoinJoin 的 Mining 費用後，將完全調整為所選池所定義的金額。在我們的例子中，我們的初始 UTXOs `108 000 Sats` 將減少到正好 `100 000 Sats`。

![coinjoin](assets/en/8.webp)

**第四步：混音**

初始混音之後，UTXOs 會被轉移到 **postmix** 帳戶。此帳戶收集已混合的 UTXO 和等待重新混合的 UTXO。當 Whirlpool 用戶端啟動時，位於 **postmix** 帳戶中的 UTXO 會自動可供重新混音，並會隨機選擇參與這些新的週期。


需要提醒的是，混音是 100% 免費的：不需要額外的服務費或 Mining 費用。因此，將 UTXOs 保留在 ** 後混合 ** 帳戶中可保持其價值不變，同時提高其匿名性。這就是為什麼允許這些錢幣參與多次 CoinJoin 循環的重要性。這完全不花您一分錢，而且還提高了它們的匿名性。


當您決定花費混合的 UTXOs 時，您可以直接從這個 **postmix** 帳戶花費。建議您將混合 UTXO 保留在此帳戶中，以享受免費混音，並防止其離開 Whirlpool 電路，以免降低其隱私性。


正如我們將在下面的教學中看到的，還有 "mix to "選項，它提供了自動將您的混合硬幣傳送到另一個 Wallet 的可能性，例如，在定義的硬幣接合數量後的 Cold Wallet。


討論完理論之後，讓我們透過 Sparrow Wallet 桌面軟體使用 Whirlpool 的教學深入實作！


## 教學：CoinJoin Whirlpool on Sparrow Wallet

使用 Whirlpool 有許多選項。我想向您介紹的第一個是 Sparrow Wallet 選項，這是一個開放原始碼的 Bitcoin Wallet 管理軟體，適用於 PC。

使用 Sparrow 的優點是相當容易上手、設定快速，而且除了電腦和網際網路連線之外，不需要其他設備。但是，有一個明顯的缺點：只有在 Sparrow 啟動並連線時，才會發生幣兌。這意味著，如果您想全天候混合比特幣，您需要經常開啟電腦。


### 安裝麻雀 Wallet

首先，您顯然需要 Sparrow Wallet 軟體。您可以直接從 [官方網站](https://sparrowwallet.com/download/) 或 [他們的 GitHub](https://github.com/sparrowwallet/sparrow/releases) 下載。


在安裝軟體之前，必須先驗證您剛下載的可執行檔的簽章和完整性。如果您想瞭解更多關於 Sparrow 軟體安裝過程和驗證的詳細資訊，我建議您閱讀這篇其他教程： *[The Sparrow Wallet Guides](https://planb.network/tutorials/Wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)*


### 建立 Software Wallet

安裝軟體後，您需要繼續建立 Bitcoin Wallet。需要注意的是，要參與硬幣接合，必須使用 Software Wallet（也稱為 "Hot Wallet"）。因此，**使用由 Hardware Wallet 擔保的 Wallet 將無法執行共同接合**。


儘管並非必要，但若您打算大量混合，強烈建議選擇使用強效 BIP39 passphrase 來混合此 Wallet。


若要建立新的 Wallet，請開啟 Sparrow，然後按一下「檔案」標籤和「新建 Wallet」。


![sparrow](assets/notext/9.webp)


選擇此 Wallet 的名稱，例如"CoinJoin Wallet"。按一下「建立 Wallet」按鈕。


![sparrow](assets/notext/10.webp)


保留預設設定，然後按一下 `New or Imported Software Wallet` 按鈕。


![sparrow](assets/notext/11.webp)


當您存取 Wallet 建立視窗時，我建議您選擇 12 個字的序列，因為這已經足夠了。選擇 `generate New` 來 generate 一個新的恢復詞組，如果您想要新增 BIP39 passphrase，請按一下 `Use passphrase`。為了確保您比特幣的安全，對您的復原信息進行實體備份是非常重要的，無論是在紙張上還是在金屬支撐物上。


![sparrow](assets/notext/12.webp)

在點擊 「確認備份... 」之前，請確認您備份的復原短語的有效性。然後 Sparrow 會要求您再次輸入您的短語，以確認您已記下該短語。這一步驟完成後，請繼續點選 `建立鑰匙庫(Create Keystore)`。

![sparrow](assets/notext/13.webp)


將建議的衍生路徑保留為預設值，然後按下 `Import Keystore`。在我的範例中，衍生路徑略有不同，因為我在本教程中使用的是 Testnet。為您顯示的衍生路徑如下：

```plaintext
m/84'/0'/0'
```


![sparrow](assets/notext/14.webp)


之後，Sparrow 會顯示您新 Wallet 的衍生詳細資訊。如果您已經設定了 passphrase，強烈建議您記下您的`主密碼指紋`。雖然此主密鑰指紋並非敏感資料，但對於您稍後驗證是否存取正確的 Wallet，以及確認在輸入 passphrase 時沒有出錯是很有用的。


按一下「應用」按鈕。


![sparrow](assets/notext/15.webp)


Sparrow 邀請您為 Wallet 建立一個密碼。透過 Sparrow Wallet 軟體存取時將需要此密碼。選擇一個強大的密碼，並將其備份，然後點擊 "Set Password"（設定密碼）。


![sparrow](assets/notext/16.webp)


### 接收比特幣

建立 Wallet 之後，一開始您會有一個索引為 `0'`的帳戶。這就是我們在前面談到的**存款**帳戶。您需要將比特幣發送到這個帳戶來進行混合。


要做到這一點，請選擇視窗左側的`接收`標籤。Sparrow 會自動 generate 一個新的空白 Address 來接收 bitcoins。


![sparrow](assets/notext/17.webp)


您可以為這個 Address 輸入一個標籤，然後將要混合的 bitcoins 傳送給它。


![sparrow](assets/notext/18.webp)


### 製作 Tx0

交易確認後，您就可以前往 `UTXOs` 標籤。


![sparrow](assets/notext/19.webp)


接下來，選擇您希望提交至 CoinJoin 循環的 UTXO。若要同時選擇多個 UTXOs，請按住 `Ctrl` 鍵，同時點選您所選擇的 UTXOs。


![sparrow](assets/notext/20.webp)


然後按一下視窗底部的 `Mix Selected` 按鈕。如果這個按鈕沒有在您的 Interface 上出現，那是因為您的 Wallet 與 Hardware Wallet 相連。您需要使用 Software Wallet 來與 Sparrow 執行共同接合。

![sparrow](assets/notext/21.webp)

開啟視窗說明 Whirlpool 如何運作。這是我在前面部分所解釋的簡化。按一下 `Next` 繼續。


![sparrow](assets/notext/22.webp)


在下一頁，您可以輸入「SCODE」（如果您有）。SCODE 是提供游泳池服務費折扣的促銷代碼。Samourai Wallet 偶爾會在特別活動時提供這種代碼給使用者。我建議您在社交媒體上 [關注 Samourai Wallet](https://twitter.com/SamouraiWallet)，以免錯過日後的 SCODE。


在同一頁，您也需要設定 `Tx0` 的費率和您的初始組合。此選擇將影響您的準備交易和第一次 CoinJoin 的確認速度。請記住，您要負責`Tx0`和初始混音的Mining費用，但您不需為後續的混音支付Mining費用。根據您的喜好調整「Premix Priority」滑桿，然後按一下「Next」。


![sparrow](assets/notext/23.webp)


在這個新視窗中，您可以選擇使用下拉清單來選擇要輸入的資料庫。在我的案例中，最初選擇了 `456 214 Sats` 的 UTXO，我唯一可能的選擇是 `100 000 Sats` 的池。此 Interface 也會告知您所需支付的服務費，以及將納入池中的 UTXO 數量。如果您對這些條件感到滿意，請繼續點擊 `預覽預混料`。


![sparrow](assets/notext/24.webp)


完成此步後，Sparrow 會要求您輸入 Wallet 的密碼，也就是您在軟體上建立 Wallet 時所設定的密碼。輸入密碼後，您就可以預覽您的 `Tx0`。在視窗的左側，您會看到 Sparrow 已經生成了使用 Whirlpool 所需的不同帳戶（`Deposit`、`Premix`、`Postmix` 和`Badbank`）。您也有機會檢視不同輸出的 `Tx0` 結構：


- 服務費；
- 均衡的 UTXOs 擬進入池；
- 毒性變化（Doxxic Change）。


![sparrow](assets/notext/25.webp)


如果交易符合您的喜好，點擊 `播送交易` 來播送您的 `Tx0`。否則，您可以選擇 `Clear` 來調整此 `Tx0` 的參數，刪除輸入的資料，並從頭開始建立程序。


### 執行 Coinjoins

一旦 Tx0 廣播完成，您會發現您的 UTXO 已準備好在 `Premix` 帳戶中進行混合。

![sparrow](assets/notext/26.webp)


一旦 `Tx0` 確認，您的 UTXO 就會在協調器註冊，初始混音會自動依序開始。


![sparrow](assets/notext/27.webp)


透過檢查 `Postmix` 帳戶，您可以觀察到初始混合所產生的 UTXO。這些硬幣將隨時準備進行後續混幣，而後續混幣不會產生任何額外費用。


![sparrow](assets/notext/28.webp)


在 "Mixes "列中，可以看到您的每個硬幣所執行的硬幣接合（coinjoins）數量。正如我們在接下來的章節中所看到的，真正重要的不是混拼本身的數量，而是相關的 anonsets，儘管這兩個指標有部分關聯。


![sparrow](assets/notext/29.webp)


若要暫時停止硬幣接合，只需按一下「停止混合」。您可以隨時選擇 `Start Mixing` 來恢復操作。


![sparrow](assets/notext/30.webp)


為了確保您的UTXOs能持續可用於remixing，Sparrow軟體必須保持啟動狀態。關閉軟體或關閉電腦會暫停硬幣拼接。迴避這個問題的解決方案是透過作業系統的設定來停用休眠功能。此外，Sparrow 提供了一個防止電腦自動休眠的選項，您可以在 「工具 」標籤下找到，標題為 「防止電腦休眠」。


![sparrow](assets/notext/31.webp)


### 完成共同接合

要使用您的混合比特幣，您有幾個選擇。最直接的方法是進入 `Postmix` 帳戶，然後選擇 `Send` 標籤。


![sparrow](assets/notext/32.webp)


在這部分，您可以選擇輸入目的地 Address、要發送的金額以及交易費用，方式與使用 Sparrow Wallet 進行的任何其他交易相同。如果您願意的話，您也可以利用進階的隱私功能，例如石牆，點擊`隱私`按鈕。


![sparrow](assets/notext/33.webp)


[-> 進一步瞭解石牆交易](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


如果您想更精確地選擇要消耗的硬幣，請前往 `UTXOs` 標籤。選取您特別想要消耗的 UTXOs，然後按下 `送出所選 ` 按鈕以啟動交易。


![sparrow](assets/notext/34.webp)

最後，Sparrow上的 "Mix to... "選項允許從CoinJoin週期中自動移除所選的UTXO，而不會產生額外的費用。這個功能可以確定一個混轉的數量，在這個數量之後，UTXO 將不會重新整合到您的 `Postmix` 帳戶中，而是直接轉到另一個 Wallet 中。此選項通常用於自動發送混合比特幣到 Cold Wallet。

若要使用此選項，請先在 Sparrow 軟體中開啟 Wallet 與 CoinJoin Wallet。


![sparrow](assets/notext/35.webp)


然後，移至 `UTXOs` 索引標籤，然後按一下視窗底部的 `Mix to...` 按鈕。


![sparrow](assets/notext/36.webp)


開啟視窗，首先從下拉清單中選擇目的地 Wallet。


![sparrow](assets/notext/37.webp)


選擇 CoinJoin 門檻，超過此門檻將自動提款。我無法提供您執行混音的確切次數，因為這會因您的個人狀況和隱私權目標而異，但請避免選擇太低的臨界值。我建議參考這篇其他文章，以瞭解更多關於 remix 的過程：[REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-Whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


您可以保留 `Index range` 選項的預設值，即 `Full`。此功能允許從不同的用戶端同時進行混音，但這不是我們在本教程中要做的。要完成並啟動 `Mix to...`選項，請按下 `Restart Whirlpool`。


![sparrow](assets/notext/38.webp)


但是，在使用 `Mix to` 選項時請務必謹慎，因為從您的 `Postmix` 帳戶中移除混合硬幣可能會顯著增加隱私外洩的風險。以下各節將詳細介紹造成這種潛在風險的原因。


## 如何瞭解我們 CoinJoin 循環的品質？

要使 CoinJoin 真正有效，必須在輸入和輸出數量之間呈現良好的均勻性。這種一致性會擴大外部觀察者眼中可能的詮釋數量，從而增加交易的不確定性。為了量化 CoinJoin 所產生的不確定性，我們可以計算交易的熵。若要深入探討這些指標，請參考教學：[boltzmann calculator](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)。Whirlpool 模型被公認為能帶來最多同源接合的模型。

接下來，我們會根據隱藏硬幣的群組大小來評估幾個 CoinJoin 循環的效能。這些群組的大小定義了所謂的 anonsets。有兩種類型的 anonsets：第一種是評估針對回溯分析 (從現在到過去) 所獲得的隱私權，第二種是針對前瞻分析 (從過去到現在) 所獲得的隱私權。如需這兩種指標的詳細說明，請參閱教學：[Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## 如何管理後混合？

執行 CoinJoin 循環後，最好的策略是將您的 UTXO 保留在 **postmix** 帳戶中，等待將來使用。甚至建議您無限期地讓它們重新混合，直到您需要使用它們為止。


有些使用者可能會考慮將混合的 bitcoins 轉移到以 Hardware Wallet 作保護的 Wallet。這是可能的，但必須仔細遵循 Samourai Wallet 的建議，以免損害取得的機密性。


合併 UTXO 是最常犯的錯誤。為了避免 CIOH（*Commun-Input-Ownership-Heuristic*），必須避免在同一個交易中將混合的 UTXO 與未混合的 UTXO 合併。這需要在 Wallet 內小心管理您的 UTXO，特別是在標籤方面。除了 CoinJoin 之外，合併 UTXOs 通常是不好的做法，如果管理不當，往往會導致隱私權的流失。


將混合的 UTXOs 合併也必須謹慎。如果您的混合 UTXOs 有顯著的非集結性，則可以進行適度的合併，但這將不可避免地降低硬幣的保密性。確保合併既不會太大，也不會在重新混合的次數不足後進行，因為這有可能在 CoinJoin 循環之前和之後，在您的 UTXOs 之間建立可推斷的連結。如果對這些操作有疑問，最好的做法是不要合併混合後的 UTXO，而是將它們逐一轉移到您的 Hardware Wallet，每次都產生一個新的空白 Address。同樣地，請記得正確標示每個接收到的 UTXO。

此外，建議您不要使用不常用的腳本將您的後混合 UTXOs 轉移到 Wallet。例如，如果您使用 `P2WSH` 腳本從 Multisig Wallet 輸入 Whirlpool，您與其他原本擁有相同類型 Wallet 的使用者混合的機會不大。如果您撤回您的postmix到這個相同的Multisig Wallet，您的混合比特幣的隱私級別將大大降低。除了腳本之外，還有許多其他的 Wallet 指紋可以騙你。

與任何 Bitcoin 交易一樣，同樣重要的是不要重複使用收件地址。每筆新交易都應使用新的空白 Address 收件。


最簡單、最安全的解決方案是讓您的混合 UTXO 在其 **postmix** 帳戶中休息，讓它們重新混合，並只在花費時才碰觸它們。Samourai 和 Sparrow 錢包有額外的保護措施來防止所有這些鏈分析相關的風險。這些保護措施可以幫助您避免犯錯。


## 如何管理毒性變化？

接下來，您需要小心管理有毒的變更，也就是無法進入 CoinJoin 池的變更。這些因使用 Whirlpool 而產生的毒性 UTXO 會對您的隱私造成風險，因為它們會在您與 CoinJoin 的使用之間建立連結。因此，必須小心處理，不要將它們與其他 UTXOs 結合，尤其是混合 UTXOs。以下是使用它們時要考慮的不同策略：


- 在較小的水池中混合使用：** 如果您的 UTXO 毒性很強，足以單獨進入一個較小的水池，請考慮混合使用。這通常是最好的選擇。但是，關鍵是不要將幾個有毒的 UTXO 合併進入一個池中，因為這可能會將您的不同入口連結起來；
- 將它們標示為「不可花費」：** 另一種方法是不再使用它們，在其專用帳戶中將它們標示為「不可花費」，並僅使用 HODL。這樣可以確保您不會不小心花掉它們。如果 Bitcoin 的價值增加，可能會出現更適合您的有毒 UTXOs 的新池；
- 捐款：** 請考慮捐款，即使是微不足道的捐款，也要捐給研究 Bitcoin 及其相關軟體的開發人員。您也可以捐款給接受 BTC 的組織。如果管理您的有毒 UTXOs 看起來太複雜，您可以直接透過捐款來擺脫它們；
- 購買禮物卡：** [Bitrefill](https://www.bitrefill.com/) 等平台允許您用 Exchange 比特幣換取可在不同商家使用的禮物卡。這可以是一種處理有毒 UTXOs 的方式，而不會失去相關的價值。
- 在 Monero 上整合它們：** Samourai Wallet 現在提供 BTC 和 XMR 之間的原子交換服務。這是管理有毒 UTXOs 的理想選擇，可將它們整合到 Monero 上，而不會透過 CIOH 洩露您的隱私，然後再將它們送回 Bitcoin。但是，由於流動性的限制，這個選擇在 Mining 費用和溢價方面可能會很昂貴。
- 將它們傳送至 Lightning Network：** 將這些 UTXO 傳送至 Lightning Network，以享受交易費用的降低，這可能是一個有趣的選擇。但是，此方法可能會透露某些資訊，這取決於您對 Lightning 的使用，因此應謹慎實行。


PlanB Network 即將提供實施這些不同技術的詳細教學。


**其他資源：**

[Sparrow Wallet 影片教學](https://planb.network/tutorials/Wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

[Samourai Wallet Video Tutorial](https://planb.network/tutorials/Wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Documentation - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts)；
- [Twitter Thread on CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739)；
- [CoinJoins 上的部落格文章](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin)。