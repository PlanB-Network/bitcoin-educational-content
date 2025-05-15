---
name: 海洋 Mining

description: 海洋 Mining 簡介
---

![signup](assets/cover.webp)


**2024年5月**


Ocean Mining 是有點獨特的 Mining pool。在這裡，不需要帳號、電子郵件地址、密碼。就像 Bitcoin，一切都是透明的、假名的，貢獻者可以選擇四種不同的區塊範本。


### 補償系統


Ocean 的補償系統稱為 TIDES，即「分別擴展股份的透明索引」。此系統記錄礦工提供的工作，稱為「股份」。矿池会计算每个贡献者的 「份额 」百分比，然后将他们的 Bitcoin Address 加入矿池的区块模板中，作为这个百分比的 Block reward 的受益人。


區塊範本約每 10 秒更新一次，以計入最有利可圖的新交易，並在必要時變更 Block reward 的分佈。


![signup](assets/rem.webp)


池開採新區塊時，您的機器是否連線並不重要。已提交的工作會保留給池找到的下八個區塊。


保留八個區塊的工作，而不是每挖出一個新區塊就將計數器重置為零，這意味著只有在您開始貢獻後，當池找到八個區塊時，您的補償才會是 100%。這也表示，如果您停止貢獻，您將繼續獲得八個區塊的補償。


此機制可使補償變得平順，並阻止「跳池」，即根據哪個池最有可能找到下一個區塊而定期切換池。


### 提款


Ocean Mining 的運作允許其貢獻者回收「乾淨」的比特幣，也就是由 Block reward 直接發行的比特幣。


與其他大多數池不同，Ocean 不會接收新挖出的比特幣；貢獻者的地址會直接整合到區塊模板中。


目前來說，要真正受益於淨比特幣的最低金額為 1,048,576 Sats。每挖出一個區塊，您的 「股份 」必須超過 1,048,576 Sats，才能由 Block reward 直接支付給您。

否則，您的 Sats 將由 Ocean 保管，直到您的獎勵總額超過此金額為止。


Ocean 暫時保管的所有比特幣都在這個 Address 上：[37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n，所有東西都可以在 TimeChain 上驗證。](https://Mempool.space/Address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

也可以使用 BOLT12 透過 Lightning 提取您的 Sats。我們會看看如何設定。


### 游泳池費用


根據所選的區塊範本，費用從 0% 到 2% 不等。


## 海洋的透明度


### 貢獻者資料


![signup](assets/1.webp)


池的所有資訊都是透明的，包括所有使用者資料。為了了解這一點，讓我們舉一個例子：


[在 Ocean 面板上](https://ocean.xyz/dashboard)，您有許多資訊，例如過去六個月的 Hashrate、池中的參與者數量、挖出的比特幣總數等。


我們將專注於 「貢獻者 」部分。您可以看到所有貢獻者的清單，以及他們在過去三個小時內的平均 Hashrate 以及相對於其他池的 **「股數」** 和 **「Hash」** 的百分比。


**"Shares %"**是貢獻者在最後 8 個區塊的視窗中所提供的工作，相較於池中其他區塊的百分比。


**"Hash%"**是貢獻者在過去三小時內提供的平均 Hashrate 與池中其他部分相比的百分比。


![signup](assets/2.webp)


您會注意到「貢獻者」是以 Bitcoin Address 來識別的。您可以點選其中任何一個位址，瞭解更多詳細資訊。


如果我們拿第一個，也就是 Hashrate 最高的那個 [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ) 來看，你可以看到這個使用者的所有詳細資料：Hashrate、挖出的比特幣數量、使用的區塊，甚至是他們每台機器 (ASIC) 的詳細資訊。然而，他們仍然是匿名的，就像在 Bitcoin 上一樣。


### 圖塊範本


在儀表板左上方有「下一區塊」。在此頁面中，有四種不同的區塊範本。Ocean 允許每位貢獻者選擇他們想要支援的區塊範本。這不會直接影響您的報酬。當池子挖出一個區塊時，所有貢獻者都會獲得報酬，不論他們選擇的是哪一種範本。這只是讓每個人「投票」給適合自己的區塊模板。


![signup](assets/3.webp)


**CORE:** 費用 2%，這是經典的 Bitcoin Core 模版，不含過濾器，正如其頁面上所寫 「包括交易和大部分垃圾郵件」。


**CORE+ANTISPAM:** 費用 0%，Bitcoin Core 具有針對特定交易的過濾器，例如 Ordinals 「包含交易並限制垃圾郵件」。


**OCEAN:** 費用 0%，Bitcoin 結 「僅包括交易和合理的小數據」


**DATA-FREE:** 費用 0%，Bitcoin 結 「只包含交易，不含任何任意資料」


### Bitcoin Core 與 Bitcoin Knot 的區別

Bitcoin Core 是讓全球約 99% 的 Bitcoin 節點運作的軟體。Bitcoin 是一個通訊協定，這表示就像網際網路有多種瀏覽器一樣，在同一個 TimeChain 上可以有多種不同的軟體程式共存。然而，出於對相容性的考量，也為了限制 Bug 在 TimeChain 上留下不可磨滅痕跡的風險，幾乎所有的 Bitcoin 開發人員都在 Bitcoin Core 上工作。Bitcoin Knots 是 Bitcoin Core 的 Fork，意味著它共享了他們大部分的程式碼，大大限制了 bug 的風險。這個 Fork 是由 Luke Dashjr 所創造的，他希望在不創造 Hard Fork 的情況下，套用比 Bitcoin Core 更嚴格的規則。現在，Bitcoin Core 和 Bitcoin Knots 因為中本共識而共存。


## 新增工人


若要新增 Worker，請先選擇您的區塊範本。此選擇將決定在 Miner (ASIC) 上輸入的池 URL。



- 核心**：`stratum+tcp://core.mine.ocean.xyz:3202`.
- core+antispam**：`stratum+tcp://ordis.mine.ocean.xyz:3303`。
- OCEAN**：`stratum+tcp://mine.ocean.xyz:3334`。
- DATA-FREE**：`stratum+tcp://datafree.mine.ocean.xyz:3404`。


接下來，在使用者欄位中輸入您擁有的 Bitcoin Address。以下是相容的 Address 類型清單：


- P2PKH** (原始 Address 類型。以「1」開頭)
- P2SH** (多重簽章或 P2SH-SegWit。以「3」開頭)
- Bech32** (SegWit. 以 "bc" 開頭。)
- Bech32m** (Taproot. 以 "bc" 開頭。比 Bech32 長。)


如果您有多個礦工，您可以為所有礦工輸入相同的 Address，這樣他們的 Hash 費率就會合併，顯示為單一的 Miner。您也可以為每個礦工添加一個獨特的名稱來區分它們。要做到這一點，只需在 Bitcoin Address 之後添加「.workername」即可。


最後，密碼欄位使用 `x`。


**範例：**

如果您選擇 **OCEAN** 模版，您的 Bitcoin Address 是 `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` 且您希望將 Miner 命名為 "Brrrrr"，那麼您需要在 Miner 的 Interface 中輸入下列資訊：



- URL**：`stratum+tcp://mine.ocean.xyz:3334`。
- 使用者**：`bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`。
- 密碼**：`x`


啟動 Mining 幾分鐘後，您就可以在 Ocean 網站上搜尋您的 Address，看到您的資料。


### 儀表板總覽


- 獎勵視窗中的份數**：此數據顯示分享的數量，也就是您在獎勵池挖出的最後 8 個區塊的視窗中發送給獎勵池的工作。
- 在 Windows 中的估計獎勵**：預估您以已完成的工作所賺取的 Sats 數量。這並未將交易費用計算在內，只計算 coinbase，即網路發行的新比特幣。
- 下一個區塊的估計收益**：如果現在挖出一個區塊，預估賺取的 Sats 數量。請記住，如果此值小於 1,048,576 Sats，您將不會直接收到 Sats 到您的 Address。它們會傳送到 Ocean 的 Address，直到您的收益超過此臨界值為止。


下圖顯示您 Hashrate 6 個月內的歷史記錄。


![signup](assets/4.webp)


在這裡，您可以看到您在不同時間標度（從 60s 到 24h）的平均 Hashrate，以及您已貢獻並獲得獎勵的池挖掘區塊的歷史。


![signup](assets/5.webp)


您可以選擇使用 ** 下載 CSV** 按鈕匯出此歷史記錄的 CSV 檔案。


![signup](assets/6.webp)


在下一節中，您會看到您用此 Address 連接到池中的所有礦工清單。當然，您有他們個人的 Hashrate，但也有他們個人因工作而獲得的 Sats 數量。


![signup](assets/7.webp)


您可以點選任何 Miner 的**暱稱**。接下來您就會看到我們剛才看到的所有資訊，不過是特別針對該 Miner 的資訊。


在頁面底部，還有一些額外資訊，您可以查看 Address 的付款歷史、您已開採但尚未付款的 Sats 以及您已開採的 Sats 總量。


![signup](assets/8.webp)


在這裡，您可以看到在 ** 估計距離最低償付金額的時間** 方塊中，寫著「閃電」，因為我們設定了 BOLT12 優惠。


### 設定閃電提款


正如您所瞭解的，Ocean 的目標是最大化透明度和最小化保管（代表您持有您的 Sats）。


這就是為什麼，對於閃電提款，有必要使用**BOLT12優惠**。這是 2024 年開始出現的一種在 Lightning Network 上付款的新方式，並允許以下幾種情況：


- 它是一個可重複使用的付款連結，允許自動付款，而且與 Lightning Address 不同的是，BOLT12 是非監護性的。
- 它也是一種付款方式，可提供付款證明，而 LNURL 則不然。
- 非常重要的是，它可以與 Bitcoin 簽名一起使用，以證明您同時是 BTC Address 和 BOLT12 優惠的持有人。

截至今日（2024 年 5 月），使用此方法的解決方案寥寥無幾。在本範例中，我們將使用配備 Core Lightning 的 Start9 伺服器。當其他工具（例如 Phoenix Wallet）整合了 BOLT12 報價時，本教學仍然適用。請確保您有開放的流動資金渠道，否則付款將無法運作。


首先進入 Ocean 網站的儀表板，輸入您的 BTC Address，然後按一下 ** 設定** 標籤。


![signup](assets/9.webp)


我們將在此複製 **Description** 文字：

bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv `OCEAN 付款


現在前往 Start9 伺服器上的 Core Lightning Interface（或任何能夠提供 BOLT12 報價的 Wallet）。


![signup](assets/10.webp)


按一下 **接收**。


勾選 **Offer**，然後將先前複製的文字貼到 **Description** 欄位，並將 **Amount** 欄位留空。


![signup](assets/11.webp)


按一下 **generate 優惠**。


![signup](assets/12.webp)


您已經產生一個可重複使用的永久付款連結，不需要像 Lightning 位址一樣需要中央伺服器。複製連結，然後返回 Ocean 頁面。


在 **Lightning BOLT12 Offer** 欄位中，貼上付款連結，並將 **Block Height** 欄位保留為預設值。按一下 **generate**。


![signup](assets/13.webp)


為了讓 Ocean 在不使用帳戶系統的情況下確保此付款連結確實是您的，您需要使用與您使用的 Bitcoin Address 相對應的私人金鑰簽署剛產生的訊息。使用私人金鑰簽署訊息有許多解決方案。在本教程中，我們將以 BlueWallet 為例，但該方法適用於所有錢包。


![signup](assets/14.webp)


假設您的私人密碼匙在 BlueWallet 中（使用 Hardware Wallet 也是一樣），請點選相關的 Wallet。


![signup](assets/15.webp)


然後在右上方的 **...** 上。


![signup](assets/15bis.webp)


以及 **簽署/驗證訊息**。


![signup](assets/16.webp)


在此視窗中，您有三個欄位： **Address**、**簽名**和**訊息**。


在 **Address** 欄位中，輸入您的 Bitcoin Address。如果回到我們的範例，就是 Address：`bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`。


將 ** 簽名** 欄位留空。

並將產生的訊息貼到 Ocean 頁面上的 **Message** 欄位：`{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`

按一下 ** 簽署**。


這將 generate 一個加密簽章，證明您是 Address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` 的擁有者，而這個簽章是唯一的，這要歸功於 Ocean 提供的訊息，由 BOLT12 付款連結產生。


![signup](assets/17.webp)


複製簽名並貼到 Ocean 的頁面，然後按一下 **CONFIRM**。


![signup](assets/18.webp)


您應該會看到確認訊息。


![signup](assets/19.webp)


現在進入 **My Stats** 標籤。頂部會顯示其他資訊，以及您之前在 Start9 上使用 Core Lightning 產生的 BOLT12 付款連結。


![signup](assets/20.webp)