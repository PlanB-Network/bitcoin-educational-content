---
name: Robosats

description: 如何使用 Robosats
---

![cover](assets/cover.webp)


RoboSats (https://learn.robosats.com/) 是私人 Exchange Bitcoin 國家貨幣的簡易方式 它簡化了點對點體驗，並利用閃電持有發票，將保管和信任要求降至最低。


![video](https://youtu.be/XW_wzRz_BDI)


## 指南


**Note:** 本指南來自 Bitocin Q&A (https://bitcoiner.guide/robosats/)。所有功勞都歸於他，您可以支持他 [這裡](https://bitcoiner.guide/contribute); BitcoinQ&A 也是 Bitcoin 的指導者。請聯繫他接受指導！


![image](assets/0.webp)


RoboSats - 基於 Lightning 的簡單私有 P2P Exchange


## 開始之前


### 您需要知道的事情


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## 您需要準備的東西


### A Lightning Wallet


RoboSats 是 Lightning 原生，因此您需要 Lightning Wallet 來為債券提供資金，並以買方身份接收所購買的 Sats。您在選擇 Wallet 時應小心，由於 RoboSats 功能所使用的技術，並非所有 Wallet 都能相容。


如果您是節點運行員，Zeus 是目前最好的選擇。如果您沒有自己的節點，我會強烈推薦 Phoenix，這是一個跨平台的行動 Wallet，設定簡單且可存取 Lightning。製作本指南時使用了 Phoenix。


### 一些 Bitcoin


買方和賣方需要在進行任何交易前提供保證金。這通常是非常小的金額 (~ 交易金額的 3%)，但仍是一個先決條件。


使用 RoboSats 購買您的第一台 Sats？為什麼不找朋友借給您入門所需的一小筆錢呢？如果您是單獨飛行，這裡有一些其他很棒的選擇，可以獲得一些 noKYC Sats 來讓您開始。


### 存取 RoboSats


顯然您需要存取 RoboSats！您可以透過四種主要方式來進行存取：


1.透過 Tor 瀏覽器 (建議使用!)

2.透過一般網頁瀏覽器 (不建議使用!)

3.透過 Android APK

4.您自己的客戶


如果您是第一次使用 Tor 瀏覽器，請瞭解更多資訊並下載 [在此](https://www.torproject.org/download/)。


希望透過 Tor 從手機存取 RoboSats 的 iOS 使用者請注意。洋蔥瀏覽器」並非 Tor 瀏覽器。請使用 Orbot + Safari 和 Orbot + DuckDuckGo。


## 購買 Bitcoin


以下步驟於 2023 年 5 月使用版本 0.5.0 進行，透過 Tor 瀏覽器存取。對於透過 Android APK 存取 RoboSats 的使用者，步驟應該相同。


在撰寫本文時，RoboSats 仍在積極開發中，因此 Interface 未來可能會有些變化，但完成交易所需的基本步驟應大致維持不變。


**註：** 當您第一次載入 RoboSats 時，您會看到這個登陸頁面。按一下開始。


![image](assets/2.webp)


generate 您的令牌，並將其存放在安全的地方，如加密的筆記應用程序或密碼管理器。如果您的瀏覽器或應用程式在交易過程中途關閉，此代碼可用於恢復您的臨時 Robot ID。


![image](assets/3.webp)


會見您的新 Robot 身分，然後按一下 Continue（繼續）。


![image](assets/4.webp)


按一下「提供」瀏覽訂單簿。在頁面頂部，您可以根據自己的喜好進行篩選。請務必注意債券百分比和 Exchange 平均利率的溢價。



- 選擇「購買」標籤
- 選擇貨幣
- 選擇您的付款方式


![image](assets/5.webp)


**注意：** 點擊您想接受的報價。輸入您想向賣家購買的金額（以您選擇的法定貨幣計算），然後對細節進行最後檢查，並點擊 「接受訂單」。


如果賣家不在線上（在其個人資料圖片上以紅點表示），您會看到交易可能需要比平常更長時間的警告。如果您繼續交易，但賣家未及時進行交易，您將獲得其保證金的 50%，以補償您浪費的時間。


![image](assets/6.webp)


接下來，您需要支付螢幕上的 Invoice 來鎖定您的交易保證金。這是一個凍結在您的 Wallet 中的 Invoice。只有當您未能完成交易時，才會被收取。


![image](assets/7.webp)


在您的 Lightning Wallet 中，掃描 QR 碼並支付 Invoice。


![image](assets/8.webp)


接下來，在您的 Lightning Wallet generate 和 Invoice 中輸入所顯示的金額，並貼到所提供的空格中。


![image](assets/9.webp)


等待賣家鎖定交易金額。完成後，RoboSats 會自動進入下一步，開啟聊天視窗。向賣家問好並詢問其法幣付款資訊。一旦提供，通過選擇的方式發送付款，然後在RoboSats中確認。在RoboSats中的所有聊天都是經過PGP加密的，這意味著只有您和您的交易對手可以讀取信息。


![image](assets/10.webp)


一旦賣家確認收到付款，RoboSats 會使用之前提供的 Invoice 自動放款。


![image](assets/11.webp)


當支付 Invoice 時，交易完成，您的債券解鎖。然後您會看到交易摘要。


![image](assets/12.webp)


檢查您的 Lightning Wallet 確認 Sats 已經到達。


![image](assets/13.webp)


## 附加功能


除了明顯的 Bitcoin 買賣功能外，RoboSats 還有一些您應該知道的其他功能。

機器人車庫


想要同時進行多個交易，但又不想在這些交易中共用相同的身份？沒問題！點擊「機器人」標籤，generate 一個額外的機器人，然後創建或接受您的下一個訂單。


![image](assets/14.webp)


### 建立訂單


除了接受別人的出價之外，您也可以創造自己的出價，等待其他 Robot 來找您。



- 開啟「建立」頁面。
- 定義您的訂單是買入或賣出 Bitcoin。
- 輸入要買入/賣出的金額和貨幣。
- 輸入您願意使用的付款方式。
- 輸入您願意接受的「市場溢價」百分比。請注意，此數值可以是負數，表示出價較目前市價有折扣。
- 按一下建立訂單。
- 支付「閃電」Invoice 鎖定您的製造者債券。
- 您的訂單現已生效。請坐好等待有人接受您的訂單。


![image](assets/15.webp)


### On-Chain 付費


RoboSats 以「閃電」為主，但買家可選擇將其 Sats 接收至 On-Chain Bitcoin Address。買家可在鎖定保證金後，選擇此選項。選擇 On-Chain 之後，買家會看到費用概覽。這項服務的額外收費包括



- RoboSats 收取的交換費 - 此費用是動態的，會依據 Bitcoin 網路的忙碌程度而變動。
- 支付交易的 Mining 費用 - 買家可自行設定。


![image](assets/16.webp)


### P2P 交換


RoboSats 允許使用者將 Sats 與他們的 Lightning Wallet 互換。只需點擊優惠頁面頂端的交換按鈕，即可查看當前的交換優惠。


作為 「換入 」要約的買方，您發送On-Chain Bitcoin給同行，並收到Sats的回復，減去廣告費用和/或溢價，到您的Lightning Wallet。作為 「換出 」要約的買方，您通過 Lightning 發送 Sats 並接收 Bitcoin，減去任何費用和/或溢價，到您的 On-Chain Address。Samourai 或 Sparrow Wallet 使用者也可以利用 Stowaway 功能來完成交換。


RoboSats 的交換優惠也可以包含 Bitcoin 的掛鉤替代品，包括 RBTC、LBTC 和 WBTC。與這些代幣互動時，您應該格外小心，因為它們都有不同的取捨。掛鉤 Bitcoin 並非 Bitcoin！


![image](assets/17.webp)


### 執行您自己的 RoboSats 用戶端


Umbrel、Citadel 和 Start9 節點的運行員可以直接在他們的節點上安裝自己的 RoboSats 用戶端。這樣做的好處如下



- 大幅加快載入時間。
- 更安全：您可控制執行的 RoboSats 客戶端應用程式。
- 從任何瀏覽器/裝置安全存取 RoboSats。如果您在本地網路或使用 VPN，則無需使用 TOR：您的節點後端會處理匿名化所需的 torification。
- 允許控制您連線的 P2P 市場協調器 (預設為 robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## 常見問題


### 我會被騙嗎？


身為買方，如果您已寄出您交易一方所需的法定貨幣，但賣方卻沒有將 Sats 釋放給您，那麼您可以提出爭議。如果在爭議過程中，您能向 RoboSats 仲裁員證明您確實寄送了法幣，賣方的託管資金和交易保證金就會發放給您。

如何取消交易？


您可以單擊交易菜單中的 「合作取消 」按鈕，在提交保證金後取消交易。如果您的交易對手同意取消，您將不會產生任何費用。但如果您的交易夥伴想完成交易，而您還是取消了，您就會失去您的交易保證金。


### RoboSats 是否支援 'X' 付款方式？


RoboSats 對付款方式沒有限制。如果您沒有看到任何您想要的付款方式，請使用它創建您自己的付款方式！


![image](assets/19.webp)


### 當我使用 RoboSats 時，它會瞭解我什麼？


如果您透過 Tor 或 Android 應用程式使用 RoboSats，則完全不需要！在此瞭解更多資訊。



- Tor 可保護您的網路隱私。
- PGP 加密可保持您的交易聊天私密性。
- 沒有帳戶意味著每筆交易只有一個 Robot。這表示 RoboSats 無法將多筆交易與單一實體相關聯。


但是，也有一些注意事項！作為發送方，Lightning 是相當隱私的，但作為接收方則不然。如果您接收到自己的Lightning節點，您的節點ID會在您的發票中共享。這個節點ID會給任何知道它的人一個起點，嘗試將您的On-Chain活動聯繫起來。如果用戶選擇通過 On-Chain 付費接收交易，情況也是如此。


為了緩解這個問題，使用者可以選擇使用解決方案，例如 Lightning 的 Proxy Wallet 或 On-Chain 的 CoinJoin。


### 聯盟


目前有一個由 RoboSats 開發團隊運作的單一 RoboSats 協調器。在 Bitcoin 中，任何形式的集中化都會讓政府或監管機構更容易成為目標，因為他們可能不喜歡某項特定服務。


由於 RoboSats 是開放原始碼專案，任何人都可以取得程式碼並開始執行自己的協調器。儘管這在某種程度上分散了單一目標的風險，但也削弱了本已稀薄的流動性市場。


RoboSats 團隊意識到這一點，並已開始聯盟模型的工作。身為終端使用者，這應該不會對上述展示的交易流程有太大的改變，但會有額外的檢視或螢幕，讓您可以新增或移除不同的協調者。


指南結束

https://bitcoiner.guide/robosats/