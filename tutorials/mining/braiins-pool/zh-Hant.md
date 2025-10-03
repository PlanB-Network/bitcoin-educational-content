---
name: Braiins Pool

description: Braiins Pool 簡介
---

![signup](assets/cover.webp)


Braiins Pool 以前稱為 Slush Pool，是第一個 Bitcoin Mining pool。成立於 2010 年 11 月，於 2010 年 12 月 16 日開採出第一個區塊，即區塊 97834。


截至 2024 年 5 月，Braiins Pool 的計算能力為 13 EH/s，約佔 Bitcoin Hashrate 總計的 1.8%。它總共開採了 1,307,188 枚比特幣，約佔最多 2,100 萬枚比特幣的 6%。


### 補償系統


自 2023 年底起，Braiins Pool 已更改其補償系統，採用 FPPS（每股全額支付）系統。這表示礦工每天都會收到前一天所有工作的報酬，即使池子沒有找到區塊也是如此。這與舊制度不同，舊制度規定礦工只有在池找到區塊時才能獲得獎勵。


**值得注意的是，[根據分析 Bitcoin TimeChain 的 Mononaut](https://x.com/mononautical/status/1777686545715089605)的推文，許多使用 FPPS 系統的 Mining pool 會將挖出的比特幣傳送到 AntPool 的 Address，這意味著 AntPool 控制了所有這些 pool 的 Hashrate，約佔全球 Bitcoin Hashrate 的 47%。這對於網路的分散性來說是個非常壞的消息。**


### 游泳池費用


Braiins Pool 的費用為 2.5%，但是，如果您在您的機器上使用 BraiinsOS，費用將為 0%。


### 提款


**Lightning Withdrawals**

閃電提款允許您每天一次通過閃電 Address 提取獎勵，無最低金額限制。

若要使用此方法，您必須擁有與 Lightning 位址相容的 Wallet。


**On-Chain提款**

On-Chain 提款設有最低金額限制，並可能需要支付手續費。

最低金額：20,000 Sats

費用：金額低於 500,000 Sats 的費用為 10,000 Sats

金額超過 500,000 Sats 免費

提款可按時間間隔或金額觸發。


## 建立帳戶


若要開始使用 Braiins Pool [前往其網站](https://braiins.com/pool)，請按右上方的「註冊



![signup](assets/3.webp)


輸入您的資訊並驗證後，您會收到一封要求確認 Address 的電子郵件。使用您收到的電子郵件中的連結進行確認，然後登入平台


![signup](assets/4.webp)



## 新增一個 「工人」

Worker 是您要連接至資料池的 Miner。若要新增 Miner，請按一下左側功能表的「Workers」。

![signup](assets/7.webp)


然後按一下紫色的「Connect Workers +」按鈕。


在此視窗中，選擇您的地理區域。


如果您要連接的 Miner 使用 BraiinsOS，請選擇「Stratum V2」協定。否則，請選擇「Stratum V1」。


![signup](assets/8.webp)


您將可以在 Miner 的網頁中輸入相關資訊 (請參閱 Miner 的說明文件，以瞭解在何處輸入這些資訊)。


這裡，**"stratum+tcp://eu.stratum.braiins.com:3333"** 是池 URL。


**JimZap.workerName** 是您的識別碼和 Miner 的名稱，其中 JimZap 是識別碼，.workerName 是 Miner 的名稱。如果您有多個礦工，您可以給他們相同的名稱，在這種情況下，他們的計算能力會在儀表板上相加，或者給他們不同的名稱，以便單獨監控他們。


而且密碼永遠都是一樣的 **"anything123"**


一旦您在 Miner 的網頁中輸入這些資訊，並且啟動 Mining，幾分鐘之後您就會看到它出現在 Braiins Pool Dashboard 上。


## 儀表板總覽


![signup](assets/9.webp)


在頂部的橫幅中，您可以看到所有礦工在 5 分鐘、1 小時和 24 小時內的平均總 Hashrate。以及線上或離線礦工數目的摘要。

以下的圖表可讓您追蹤運算能力的演進。


![signup](assets/10.webp)


在此圖表下方，有幾項關於您在 Sats 中的獎勵資訊。


**「今日 Mining 獎勵 」** 表示您今天挖到的 Sats 數量。當天結束時，此值會重設為 0，並將 Sats 送到您的帳戶。


**「昨天的總獎勵 」** 您前一天賺取的 Sats 數量


**"Est.Profitability (1 TH/s) "**是運算能力為 1 TH/s，一天內所賺取的 Sats 的估計值。例如，如果數值是 77 Sats，而您的運算能力為 10 TH/s，則理論上每天可賺 77 x 10 = 770 Sats。


**「所有時間獎勵 」**您使用 Braiins Pool 開採的 Sats 總數


**「獎勵計劃」** 獎勵池採用的收費率


**"Next Payout ETA "**預估從平台提取 Sats 所需的時間。在此，估算值什麼也沒顯示，因為 Mining 只進行了幾分鐘。


**「帳戶餘額 」** 您帳戶中可用的 Sats 數量，然後您可以提款。

## 設定提款

您可以使用 On-Chain 或 Address 透過閃電提取獎勵。


在頂部，按一下「資金」。預設情況下，您有一個「Bitcoin 帳戶」。您可以建立其他帳戶來分享獎勵。我們會在下一節再討論這一點。


現在，請按一下「設定」。


![signup](assets/17.webp)


在這個新視窗中，您可以選擇「Onchain 付款」。


命名此 Wallet，提供 BTC Address，並選擇您想要的觸發類型。「閾值 」表示當您累積了定義數量的 BTC 時就會觸發付款，使用 「時間間隔」，付款會在固定的時間間隔 (日/週/月) 觸發。


請注意，最低金額為 0.0002 BTC，低於 0.005 BTC 將收取 0.0001 BTC 的費用。


![signup](assets/18.webp)


如果您想使用 Lightning 提款，您需要一個提供 Lightning Address 的 Wallet。例如，您可以使用 getAlby。


按一下視窗上方的「Lightning payout」。


輸入您的 Lightning Address，並勾選「我了解...」方塊，然後驗證。


使用這種提款方式，您的獎金將每天發送至您的 Wallet。


![signup](assets/14.webp)


驗證您的付款設定後，您會收到一封確認電子郵件。


![signup](assets/15.webp)


## 分享獎勵


Braiins Pool 還允許您在多個錢包中分享獎勵。


若要執行此動作，請按一下上方的「Mining」，然後按一下左方的「設定」。


![signup](assets/19.webp)


在此頁面，您可以點擊 「添加其他金融賬戶 」來添加其他 「金融賬戶」，並將您的獎勵按百分比分配到這些不同的賬戶中，您必須將一個Wallet與這些賬戶聯繫起來。若要將新的 Wallet 與金融帳戶聯繫，請參閱上一節。