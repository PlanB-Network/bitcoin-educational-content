---
name: 公牛 Bitcoin Wallet
description: 瞭解如何使用 Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



本指南將介紹 Bull Bitcoin Mobile 的安裝、配置和使用。您將學習如何在三個網路（onchain、Liquid 和 Lightning）上接收和發送資金，以及如何將您的 Bitcoin 從一個網路轉移到另一個網路。附錄提供資源與聯絡方式、背景資訊以及技術概念的簡要說明。



## 簡介



**Bull Bitcoin Mobile**，由 **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([create account](https://app.bullbitcoin.com/registration/orangepeel)) 所開發，是一款**自我保管**的 Bitcoin Wallet，這表示您可以完全控制您的私密金鑰，因此也可以完全控制您的資金，而不需要仰賴第三方。此 Wallet 採用開放原始碼並植根於 Cypherpunk 哲學，結合了簡易性、保密性和進階功能，例如跨網路交換和 PayJoin 支援。它可讓您在三個網路中管理您的比特幣： **Bitcoin onchain**、**Liquid** 和 **Lightning**，每個都是針對特定用途量身打造。



### 發展背景



Wallet 回應了一項重大挑戰：Bitcoin 網路收費不適合小額支付，或開設小型自管 Lightning 通路。Wallet Bull Bitcoin Mobile 在依賴 3 個主要 Bitcoin 網路的同時，提供了自保管解決方案：





- Bitcoin 網路 (onchain)**：中長期儲存 UTXO 和大額交易的理想選擇，費用在比例上可以忽略不计。
- Liquid Network**：專為快速（約 2 分鐘）、更保密（隱藏金額）、低成本的交易而設計，非常適合累積小額金額或保護您的隱私。
- Lightning** 網路：針對即時、低成本付款進行最佳化，適用於中小價值的日常交易。



以 Bull Bitcoin Mobile 為例，您可以在 **Liquid** 或 **Lightning** 組合中累積小額資金，當您累積的資金達到相當可觀的數額時，您就可以 ：





- 轉移到 onchain 網路進行安全的中期或長期儲存，與上游的 Liquid 和/或 Lightning 一起提高了機密性，並且單筆交易可收取 onchain 費用



### 持續演進



Wallet 在不斷演進，因此如果您發現本教學與您最新的應用程式之間有差異，請不要感到驚訝。




- 例如，自 2025 年 7 月 19 日起，**「買入/賣出/支付 」** 按鈕在應用程式中是可見的，但呈灰色，因為這些選項可在 Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel) 上使用，不久將整合為統一的體驗。它們的使用仍然是完全可選的。許多其他開發正在進行或計劃中：多 Wallet 管理、passphrase、與硬體錢包的相容性...
- 在 [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)，您可以查看當前主題和即將進行的開發。由於本專案是 100% 開放原始碼且「公開建置」，您也可以將您的建議和遇到的任何 bug 寄給我們。




## 1.先決條件



在您開始使用 **Bull Bitcoin Mobile** 之前，請確定您已備妥下列物品：





- 相容的智慧型手機**：iOS**（iPhone 或 iPad）或**Android**裝置
- 網際網路連線
- 安全備份媒體**：在紙張或金屬上寫下您的**恢復詞組**（12 個字），並將其存放在安全的地方。
- 基本知識**：對 Bitcoin 概念 (位址、交易、費用) 有最低限度的瞭解是有用的，不過本教程會為初學者解釋每個步驟。



## 2.安裝





- 下載申請表** ：
 - [Google Play 商店](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)**從 Android 裝置的應用程式商店下載
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) 直接下載 Android 裝置的 APK**。
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** 透過 TestFlight 為 Apple 裝置下載
 - 檢查開發者的名稱 (Bull Bitcoin)，以避免詐騙性的應用程式。
 - 確保下載的版本與 GitHub 上顯示的最新穩定版本相符。
 - Bull Bitcoin Mobile 是**開放原始碼**。查看程式碼：[BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- 安裝應用程式




## 3.初始設定



### 3.1 啟動應用程式 ：



該應用程式對兩個組合都使用了獨特的 12 個字的復原短語：




 - 安全 Bitcoin' Wallet**：用於 Bitcoin 網路 (onchain) 上的交易
 - instant Payments' Wallet**：用於 Liquid 和 Lightning 網路上的即時交易



開啟時，系統會提示您匯入現有的復原短語，或建立新的 Wallet ：



![image](assets/fr/02.webp)



### 3.2 恢復詞組 ：



如果您希望重新使用現有的 Wallet，請按一下「**復原 Wallet**」，然後填寫復原用語的 12 個字。



否則，請按一下「**建立新 Wallet**」：




- 謹慎寫下您的復原用語。寫在紙上或金屬上，並將其保存在安全的地方（保管箱、離線位置）。此短語是您在裝置遺失或應用程式刪除時存取比特幣的唯一方法。
- 還要注意的是，任何人只要有這句話，就可以偷走您所有的 bitcoins。永遠不要以數位方式儲存：
 - 沒有截圖
 - 無雲端、電子郵件或訊息備份
 - 無複製/貼上（儲存至剪貼簿的風險）



**!這一點非常重要**。如需更多協助 ：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 安全存取 ：





- 前往設定，然後按一下 **PIN 碼**。
- 設定強大的 **PIN 碼**，以保護對應用程式的存取。
- 此步驟為可選步驟，但強烈建議您進行此步驟，以防止任何可存取您手機的人取得 Wallet 的存取權。



![image](assets/fr/03.webp)



### 3.4 連接到個人節點 (選用)：



Wallet BullBitcoin 預設連線至 Electrum 伺服器：第一台由 Bull Bitcoin 管理，第二台伺服器來自 Blockstream，這兩台伺服器都被認為不會保留任何日誌，降低了追蹤的風險。



為了更高的保密性，您可以透過 Electrum 伺服器將應用程式連接到您自己的 Bitcoin 節點 (說明請參考 [BullBitcoin's GitHub](https://github.com/orgs/SatoshiPortal/projects/49) )。




## 4.接收資金



使用 **Bull Bitcoin Mobile ** 收取資金非常簡單，而且是針對您的需求量身打造，無論您使用的是 ：




  - **Bitcoin（onchain）** 網絡進行長期保護、
  - **Liquid**網路，以獲得快速、更多的 Confidential Transactions、
  - **Lightning**網路進行即時、低價值付款。



應用程式會自動產生 Lightning 接收或 Invoice 位址，視所選擇的網路而定。以下是每個網路的操作方法。



### 4.1. onchain (Bitcoin 網路)



在主畫面上，您可以 ：




- 或選擇 **Secure Bitcoin Wallet**，然後按一下「**接收」** ：



![image](assets/fr/04.webp)





- 或按一下「**接收」**，然後選擇 **Bitcoin** 網路：



![image](assets/fr/05.webp)



#### 4.1.1.僅複製或掃描 Address」選項已停用（預設值）



![image](assets/fr/06.webp)





- 這可讓您存取可選的進階參數。您可以指定 ：
 - 以 BTC、Sats 或法定貨幣計算的**金額。
 - 要包含在 URI / QR Code 副本中的**個人說明。
 - 啟動 **PayJoin**（詳情請參閱附錄 3），可透過結合寄件者和收件者項目提高機密性。





- 自動產生 URI 的範例** ：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- 使用方式**：複製 URI 與寄件者分享，或讓寄件者掃描 QR 代碼。



#### 4.1.2.僅複製或掃瞄 Address」選項已啟用



![image](assets/fr/07.webp)





- 啟用 **「僅複製或掃描 Address」** 選項後，應用程式會以 SegWit (bech32) 格式產生簡單的 Bitcoin Address。





- 範例：



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



即使您輸入金額或備註，它們也不會包含在 QR 代碼或 Address 的複本中。





- 使用方式**：複製 Address 與寄件者分享，或讓他掃描 QR 代碼。



#### 4.1.3.產生新的 Address





- 為什麼每次交易都要使用新的 Address？此舉可**保護您的隱私**，防止多筆付款連結到同一個 Address，並限制在 Blockchain 上追蹤的可能性。
 - 預設情況下，Bull Bitcoin 會自動產生一個未使用的 Address.**。
 - 您可以點選畫面下方的 **「New Address」**，強制建立新的 Address。
 - 您所有的地址都會連結到您的 seed 短語：無論您使用多少個地址，您的投資組合都會顯示單一餘額，並可在出貨時自動整合資金。





- 提示：除非您有特殊需求 (例如：使用公共 Address 接受捐款)，否則請務必使用 Bull Bitcoin 提供的新 Address**。



### 4.2.Liquid



在主畫面上，您可以 ：




- 或選擇 ** 即時付款 Wallet**，然後按一下 **「接收」**，再按一下 **「Liquid」**：



![image](assets/fr/08.webp)





- 或按一下「**接收」**，然後選擇 **Liquid** 網路：



![image](assets/fr/09.webp)



進入 **「接收 」** 畫面後，複製一個 Liquid Address：





- 無金額或備註。範例：



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- 或指定**金額**（BTC、Sats 或法幣）和/或**個人備註**，以包含在 URI / QR Code 的副本中。範例：



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**使用**：複製 Address/URI 與寄件者分享，或讓他掃描 QR 代碼。



### 4.3.閃電



在主畫面上，您可以 ：




- 或選擇 ** 即時付款 Wallet**，然後按一下「**接收」** ：



![image](assets/fr/10.webp)





- 或按一下「**接收」**，然後選擇 **Lightning** 網路：



![image](assets/fr/11.webp)



#### 4.3.1.操作、限制和效益





- 機制**：Bull Bitcoin Wallet 是一個可以透過 Lightning 付款和收款的 Wallet。由於透過**Boltz**進行自動交換，透過 Lightning 收到的資金會儲存在**Liquid**網路（Wallet Instant Payments 中）。這讓您能夠與 Lightning 互動，而無需管理流動資金管道，同時保持自我保管。





- 限制：**
 - 當您 generate Invoice 時，最低金額**為 100 Satoshis（截至 07/19/2025）。
 - 您支付的費用**，將從寄件者寄出的金額中扣除，這與使用 Wallet Lightning native 收件不同，在 Wallet Lightning native 收件中，除了寄出的金額之外，只有寄件者支付轉帳費用。截至 2025 年 7 月 19 日，47 Sats 會從寄出的金額中扣除。





- 福利** ：
 - 自行保管**：您的資金仍由您控制，儲存在 Liquid Network 上。
 - 沒有高昂的上鏈費用**：儲存在 Liquid 上可避免開啟您的 Lightning 通道或增加流動性所需的昂貴上鏈存款。當 Liquid 上累積的金額足以支付費用時，這些操作可以稍後再進行。





- 提示：** 如果寄件者有 Wallet Bull Bitcoin，請直接使用 Liquid Network 以避免交換費用



#### 4.3.2.generate Invoice





- 輸入**金額**（BTC、Sats 或法定貨幣）





- 加入**個人備註**，此備註將整合至 Invoice。如果寄件者支付 Invoice，您的 Wallet 也會將其納入交易詳細資料中。





- Invoice 有效期：** Lightning Invoice 的有效期為 **12 小時**。此時間過後即失效，無法再支付。必須產生新的 Invoice。





- 使用方法**：複製 Invoice 與寄件者分享，或讓他掃描 QR 代碼。




## 5.寄送資金



### 5.1.基本原則



從首頁或從錢包 ：



![image](assets/fr/12.webp)



進入傳送畫面：



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** 可根據輸入的 Address 或 Invoice（複製或透過 QR 碼掃描）自動偵測網路（Bitcoin、Liquid 或 Lightning），讓您輕鬆匯款。



### 5.2. 鏈上傳輸 (Bitcoin 網路)



#### 5.2.1.傳送畫面



**Action**：輸入或掃描 Bitcoin onchain Address





- 如果尚未定義金額，例如 ：



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- 然後您可以在傳送畫面中選擇 ：
 - 金額以 BTC、sat 或法幣計算。最低金額：546薩托希斯，2025 年 7 月 22 日。
 - 識別交易的可選備註。只有您可以在交易詳細資料中看到。



![image](assets/fr/14.webp)





- 如果已經定義了金額，例如 ：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



接著您會直接進入以下的確認畫面。



#### 5.2.2 確認畫面



花時間檢查所有參數，尤其是金額、目的地 Address 和費用。


然後您可以調整參數：



![image](assets/fr/15.webp)




- 費用**：您可以選擇：
  - 無論是您交易的執行速度**，還是相關費用都會估算出來。
  - 無論是絕對費用** (以 Satoshis 為單位的總費用) 或相對費用 (每位元組的費用) 模式，都會估算您的交易速度。





- 進階設定** ：





 - Replace-by-fee (RBF)** ：預設已啟動，此功能可透過支付較高費用加快交易速度 (詳情請參閱附錄 4)。





 - 手動選擇 UTXO**：如果您的資金存放在數個不同的 Wallet 位址，您可以選擇從哪些位址寄送資金。為什麼要這樣做？隨著 Bitcoin 的採用越來越多，轉帳費用也在不斷上升。從數個地址發送小額資金比從單個 Address 發送資金更昂貴，但現在這樣做可避免日後需要這樣做，屆時費用會更高。這稱為 UTXO 的**整合。



![image](assets/fr/16.webp)





- 使用 PayJoin** 發送：如果提供 URI 的收件者已啟動該功能，例如 ：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



然後 Bull Bitcoin Mobile 將結合您的 UTXO 與收件者的 UTXO 作為輸入來設定傳送，以提高機密性 (詳情請參閱附錄 3)。



### 5.3.傳送至 Liquid



#### 5.3.1 傳送畫面



**Liquid**網路可實現快速交易（由於每分鐘一個區塊，因此約 2 分鐘即可完成交易），與 onchain 網路相比，更加保密（遮蔽金額），而且費用非常低。資金從 **Instant Payments Wallet** 提取。



**動作**：輸入或掃描 Liquid Address





- 如果尚未定義金額，例如 ：



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



然後您可以在傳送畫面中選擇 ：




- 金額以 BTC、sat 或法幣計算。無最低金額，1 Satoshi 可能；
- 識別交易的可選備註。只有您可以在交易詳細資料中看到。



![image](assets/fr/17.webp)





- 如果已經定義了金額，例如 ：



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



接著您會直接進入以下的確認畫面。



#### 5.3.2 確認畫面



花時間檢查所有參數，特別是金額和目的地 Address。



![image](assets/fr/18.webp)





- 費用**：與交易的複雜性成正比，一般以 0.1 Sat/vB 為基礎，即簡單交易為 20-40 Satoshis (07/22/2025 時為 33 Sats)。



### 5.4.傳送至閃電



#### 5.4.1 傳送畫面



**Lightning**網路可實現即時、低成本的小額支付，是日常小額交易的理想選擇。



**動作**：輸入或掃描「閃電」Invoice





- 如果您掃描 LN-URL Address，可讓您設定金額


例如： `orangepeel@walletofsatoshi.com`。


然後您可以在傳送畫面中選擇 ：




 - 金額為 BTC、sat 或法幣。23/07/2025 最低金額為 1000 Satoshis
 - 用於識別交易的可選備註。它會寄給收件人。



![image](assets/fr/19.webp)





- 如果您掃描的 Lightning Invoice 包含定義的數量


範例：



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



接著您會直接進入以下的確認畫面。



註：金額必須大於 21 Sats on 07/23/2025



#### 5.4.2 運作、限制與效益





- 機制**：資金來自 **Instant Payments Wallet** (Liquid)，並透過 **Liquid → Lightning** 與 **Boltz** 的交換進行轉換。





- 限制：**
 - 最低金額**高於 Wallet Lightning 本機 (見上文)
 - 支出**加上 Liquid → 透過 Boltz 進行閃電交換





- 福利** ：
 - 自行保管**：您的資金仍由您控制，儲存在 Liquid Network 上，如有需要，可透過 Lightning 轉帳
 - 沒有高昂的上鏈費用**：儲存在 Liquid 上為您省下了高昂的上鏈存款費用，以打開您的 Lightning 通道或增加流動性。當 Liquid 上累積的金額足以支付費用時，這些操作可以稍後再進行。





- 提示：** 如果收件人有 Wallet Bull Bitcoin，請直接使用 Liquid Network，以避免交換成本



#### 5.3.3 確認畫面



花時間檢查所有參數，尤其是金額和目的地 Address。



![image](assets/fr/20.webp)




## 6.檢視歷史



**Bull Bitcoin Mobile** 可讓您輕鬆追蹤您在**Bitcoin（onchain）**、**Liquid**和**Lightning**網路的交易。歷史記錄可以兩種方式存取，並顯示每種交易的詳細資訊。您也可以使用外部區塊瀏覽器檢查您的交易。



### 6.1.存取歷史





- 透過主畫面** ：
 - 按一下 **Secure Bitcoin Wallet** 檢視 **onchain** 交易，或按一下 **Instant Payments Wallet** 檢視 **Liquid** 和 **Lightning** 交易。
 - 歷史記錄會顯示在投資組合總計的正下方，並根據所選的 Wallet 類型進行篩選。



![image](assets/fr/21.webp)





- 透過專屬頁面** ：
 - 在主畫面上，按一下 ** 歷史符號** (時鐘圖示或類似圖示)。
 - 存取列出所有交易的頁面，並可依行動類型篩選： **Send**, **Receive**, **Swap**, **PayJoin**, **Sell**, **Buy** (註：Sell 和 Buy 正在開發中，目前尚未提供，2025 年 7 月 20 日)。



![image](assets/fr/22.webp)



### 6.2.交易詳細資訊



每筆交易都會根據網路和動作類型（發送或接收）顯示特定資訊。以下是 ** 鏈上交易的可用詳細資訊 *** ：



![image](assets/fr/23.webp)



### 6.3.透過 Block explorer 進行檢查



**Bitcoinonchain**、**Liquid**和**Lightning**網路的探測者名單列於附錄 4。



對於**Lightning**，公共瀏覽器上看不到交易。請在應用程式中檢查詳細資訊 (包括 Boltz 的交換 ID)。




## 7.設定



可直接從 Bull Bitcoin 應用程式首頁存取「設定」頁面，該頁面可用於設定和管理組合的各個方面以及使用者體驗。



![image](assets/fr/24.webp)





- Wallet 備份**：顯示安全備份組合的復原短語。有關管理和儲存復原片語的最佳作法，請參閱第 3.節的組合建立。





- Wallet 詳細資訊** ：
 - Pubkey**：與 Wallet 相關的公開金鑰，用於 generate Bitcoin 接收位址。
 - 衍生路徑**：用來從私人金鑰 generate Wallet 位址的衍生路徑。





- Electrum 伺服器 (Bitcoin 節點)**：建立與客製化 Bitcoin 節點的連線，以進行鏈上交易。





- PIN 碼**：啟動和/或修改安全碼，以保護對應用程式和 Wallet 功能的存取。





- 貨幣**：選擇是否以 BTC 或 Sats 顯示金額，以及預設法定貨幣（美元、歐元等）。





- 自動交換設定**：自動交換_功能允許您自動將您的 BTC 從 **Instant Payments Wallet (Liquid)** 轉移到您的 **Bitcoin On-Chain** Wallet，只要金額達到您認為高到足以證明交易費用合理的臨界值。





- 日誌**：可檢視的活動日誌，可與技術支援人員分享，以便排除故障。





- Telegram 支援訪問** ：直接連結至官方 Telegram 頻道，以提供使用者協助。





- Github 存取** ：連結至 [Bull Bitcoin Github 套件庫](https://github.com/SatoshiPortal) 以檢視開放原始碼或報告問題。




## 附錄



### A1.PayJoin (P2EP) 說明



![image](assets/fr/25.webp)



** 定義** ：




- PayJoin 或 **Pay-to-EndPoint (P2EP)** 是一種 Bitcoin 交易技術，可增強 **onchain** 網路的機密性。它在單一交易中結合了寄件者和收件者項目，使金額和地址更難被追蹤。



**操作：**




- 在 PayJoin 交易中，寄件者和收件者透過相容的 PayJoin 伺服器共同合作，以 generate 進行聯合交易。
- 接收方不再只提供寄件方的項目 (UTXO)，而是也提供自己的一個 UTXO。這使得 Blockchain 上可見的資訊變得模糊：現在並非只有一個項目對應實際金額，而是有兩個項目，而且輸出並不直接反映交換的金額。
- 最後的交易類似於標準的 Bitcoin 交易 (多輸入/多輸出)，但由於採用了隱藏結構，因此隱藏了實際發送的金額和地址之間的連結。



**適用於公牛 Bitcoin 移動**




- 接收** (Address Supply)：預設啟用 PayJoin。
- 發送** ：Wallet 會自動偵測 PayJoin URI 並據此設定交易，例如



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**福利**




- 加強保密性**：PayJoin 使交易中的所有項目均屬於單一實體的假設失效。有了 PayJoin，輸入會同時來自發送者和接收者，打破這個假設。
- 金額遮蔽** ：實際交換金額不會直接出現在輸出中。它是以接收方的 UTXO 入站和出站之間的差額來計算的，使得分析具有誤導性。



**限制**




- PayJoin 要求寄件者和收件者使用相容的錢包，否則會使用標準的 onchain 交易。
- 交易略為複雜（更多的輸入和輸出），導致成本略高。
- 雖然設計上與標準交易類似，但先進的啟發式（例如：模稜兩可的輸出、已知的 PayJoin 伺服器）可能會讓人懷疑其用途，儘管沒有絕對的確定性。



**更多資訊：**




- [詞彙](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2.Replace-by-fee（RBF）的解釋



**定義**：Replace-by-fee (RBF) 是 Bitcoin 網路的一項功能，允許寄件者透過同意支付較高的費用，加速**鏈上**交易的確認。



**Limits** ：




- RBF 不適用於 Liquid 或 Lightning 交易。
- 初始交易在建立時必須標記為 RBF 相容，除非禁用，否則 Bull Bitcoin Mobile 會自動這樣做。



**更多資訊：**




- [詞彙](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3.最佳實踐



要安全有效地使用 **Bull Bitcoin Mobile**，請遵循這些建議。它們將幫助您在**Bitcoin (onchain)**、**Liquid**和**Lightning**網絡上保護您的資金、優化您的交易並維護您的機密性。





- 保護您的復原短語** ：
 - 教學：[Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- 使用安全認證** ：
 - 啟動**強大 PIN**或**生物辨識驗證** (指紋或臉部辨識) 以保護對應用程式的存取。
 - 切勿分享您的 PIN 碼或生物辨識資料。





- 保護您的隱私** ：
 - generate 為每個 onchain 或 Liquid 接收一個新的 Address，以限制在 Blockchain 上進行追蹤。
 - 在可用的情況下使用 PayJoin，以提高鏈上傳送數量的保密性。
 - 為了獲得最大的保密性，請透過 Electrum 伺服器將您的 Wallet 連接到您自己的 Bitcoin 節點，而不要使用公共節點





- 選擇最適合您需求的網路** ：
 - Onchain**：長期託管或大額交易的首選 (費用相較於金額可忽略不计)。
 - Liquid**：用於快速、低成本的傳輸，並加強保密性。
 - 閃電**：選擇即時、低成本的小額轉帳。如果您是兩位 Wallet Bull Bitcoin 使用者，請選擇 Liquid 以避免透過 Boltz 的 Lightning <> Liquid 掉期費用。





- 請務必檢查送貨地址** ：
 - 發送資金之前，請仔細檢查 Address。發送至錯誤的 Address 的資金將永久丟失。使用複製/貼上或 QR 代碼掃描，切勿手抄/修改 Address。





- 優化成本** ：
 - 對於 onchain 交易，根據緊急程度和網路擁塞情況選擇適當的費用 (慢、中、快)。
 - 少量使用 Liquid，或 Lightning。
 - 如果您預期需要加快確認速度，請啟動 Replace-by-fee (RBF)（請參閱附錄 4）以進行串聯出貨。





- 隨時更新應用程式




### A4.額外資源





- 官方連結與支援：**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : 支援電子郵件
 - [Bull Bitcoin 官方網站](https://bullbitcoin.com/) :** 有關 Bull Bitcoin 服務、建立帳號、存取應用程式的資訊
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** 檢視程式碼、演進與路線圖，為開發貢獻心力...
 - [Account X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Wallet Mobile 的 Telegram** 群組：與支援人員群組聊天，請參閱「設定」頁面。





- 區塊探索者 :**
 - on chain ： **[Mempool.space](https://Mempool.space/)**
 - Liquid ： **[Blockstream Info](https://blockstream.info/Liquid)**
 - 閃電： **[1ML (Lightning Network)](https://1ml.com/)**





- 學習與教學：** ** [Plan ₿ Network](https://planb.network/)** ：
 - 保護您的復原短語



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** ：
 - [詞彙](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** ：
 - [詞彙](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5.公牛 Bitcoin



#### 公司概覽



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**，是專門針對 Bitcoin 的歷史最悠久的非存款 Exchange 平台，於 2013 年在加拿大蒙特婁的 Bitcoin 大使館成立。該公司由 Bitcoin 生態系統中公認的先驅 Francis Pouliot 領導，將自身定位為促進金融主權和用戶自主的關鍵角色。其使命是讓個人透過使用 Bitcoin 作為自由和付款的工具，重新掌控自己的金錢，同時拒絕使用 Bitcoin 以外的法定貨幣和加密貨幣。



![image](assets/fr/26.webp)



[建立您的帳號](https://app.bullbitcoin.com/registration/orangepeel) Bitcoin 買賣可享有 0.25% 折扣。



#### 價值與理念



公牛 Bitcoin 以其 Commitment 到 Cypherpunk 的原則和 Bitcoin 的道德觀脫穎而出：





- 獨家專訪 Bitcoin** ：該平台忠於去中心化、抗審查貨幣的願景。





- 非保管人** ：使用者可將資金傳送至自己的投資組合，保留對比特幣的完全控制權。





- 保密性**：盡量減少個人資料的收集，999 美元以下的交易提供免 KYC 購買選項。資料依照法規受到保護 (加拿大的 FINTRAC、法國的 AMF)。





- 透明度**：沒有隱藏費用，成本包含在差價（買入價和賣出價之間的差額）中。





- 金融主權**：Bull Bitcoin 提倡獨立於傳統的銀行系統和中央機構。



#### 主要服務





- 法幣存款** ：使用者可在指定的加拿大郵局，透過銀行轉帳或現金/借記卡，以法定貨幣（加元、歐元等）為 Bull Bitcoin 帳戶存入資金。





- 購買 Bitcoin** ：使用者可購買 Bitcoin，Bitcoin 會直接傳送到他們的非存管投資組合，保證完全掌控他們的資金。





- 定期購買 Bitcoin**：Bull Bitcoin 提供定期自動循環購買服務 (DCA - Dollar Cost Averaging)，動用您的可用餘額，直接將比特幣轉移至使用者控制的 Wallet，減少價格波動的影響。



請注意，一個名為「自動購買」的選項可讓您在法幣觸及您的 Bull Bitcoin 結餘時立即進行轉換，並將您的比特幣傳送到您自己的 Wallet。此選項也可以與您的銀行預定的定期銀行轉帳結合，進行 DCA。此選項可自動累積您的 Bitcoin，而無需打開應用程式。






- 以固定價格買入 Bitcoin「限價訂單」**：允許您以使用者事先指定的價格買入 Bitcoin，當 Bull Bitcoin 指數價格達到或低於設定的限價時，該指令會自動執行。





- 出售 Bitcoin**：使用者可以出售他們的比特幣，並透過銀行或 SEPA 轉帳直接將款項以法定貨幣存入他們的銀行帳戶。





- 第三方支付**：Bull Bitcoin 可讓使用者用比特幣向銀行帳戶傳送法幣，對收款人完全透明。





- Bull Bitcoin Prime**：Bull Bitcoin Prime 是專為高淨值和企業客戶提供的尊貴服務，可提供客製化解決方案和尊貴支援。這包括享有較低的費用、專屬的帳戶經理以及量身打造的企業服務。這項服務主要針對尋求深入專業知識和優先待遇的機構、專業交易員和企業客戶。





- 行動版 Wallet**：公牛 Bitcoin 提供開放原始碼、自我保管的行動版 Wallet，可在 Android 和 iOS 上使用，支援 onchain、Liquid 和 Lightning Network 交易。





- 教育支援**：免費指南與個人化輔導，協助使用者建立、保全及管理 Bitcoin 投資組合，強化財務自主性。



#### 合規與安全





- 監管**：在加拿大 FINTRAC 和法國 AMF 註冊，Bull Bitcoin 符合 KYC/AML 要求。





- 安全性**：使用安全的投資組合和離線儲存建議。個人資料託管於 Bull 的 Bitcoin 基礎架構，此基礎架構為 100% 自行託管，不依賴任何第三方。