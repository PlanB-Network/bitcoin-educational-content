---
name: Blockstream 應用程式 - 僅供觀看
description: 如何在 Blockstream App 上設定 Watch-only wallet？
---

![cover](assets/cover.webp)


## 1.簡介


### 1.1 教學目的





- 本教學說明如何設定並使用 **Blockstream App** 行動應用程式的 **Watch-Only** 功能，在不存取 Bitcoin Wallet 私密金鑰的情況下監控 Bitcoin。
- 內容包括安裝、初始設定、匯入擴充公開金鑰，以及使用它追蹤餘額和 generate 接收位址。
- 注意：附錄中提供的其他教程涵蓋 Onchain、Liquid 和桌面版。



### 1.2.目標受眾





- 初學者**：希望透過直覺式行動應用程式監控 Bitcoin 組合（通常與 Hardware Wallet 相關聯）的使用者。
- 中級使用者**：希望在使用 Tor 或 SPV 等隱私選項時管理唯讀投資組合的人。
- Hardware Wallet 擁有者**：無須連接裝置即可檢查其餘額和 generate 位址。
- 企業和商店** ：
 - 為了會計目的追蹤您的交易，而不會暴露您的私人金鑰。
 - 驗證線上付款系統中未輸入私密金鑰而收到的交易。
 - 讓員工可以 generate 新接收位址，而無需存取私人金鑰。
- 組織與集資**：向捐贈者透明顯示餘額，但不允許存取資金。



### 1.3.介紹專用觀看



僅需監控**的 Wallet 允許您監控 Bitcoin Wallet 的交易和餘額，而無需存取私人金鑰。與傳統的 Wallet 不同，它只儲存公開資料，例如**擴充的**公開金鑰** (衍生出 "**xpub**「，然後是 」zpub"、"ypub "等)，這使它能夠取得接收地址並追蹤 Blockchain Bitcoin 上的交易記錄。由於沒有私密金鑰，因此無法從應用程式中支出資金，保證了更高的安全性。



![image](assets/fr/10.webp)



**為何使用 Watch-only wallet？





- 安全性**：是監控由 **Hardware Wallet** 保護的組合的理想選擇，而不會暴露連接裝置上的私人金鑰。
- 方便**：讓您無需連接 Hardware Wallet，即可檢查餘額及 generate 新收件人地址。
- 保密性**：與 **Tor** 或 **SPV** 等選項相容，可限制對第三方伺服器的依賴。
- 使用個案**：追蹤移動中的資金、產生地址以接收付款，或驗證交易而無需冒私密金鑰的風險。



![image](assets/fr/01.webp)



### 1.4.擴充公開金鑰



擴充公開金鑰** (xpub, ypub, zpub, 等等) 是由 Bitcoin Wallet 產生所有子公開金鑰及其相關接收位址的資料，但不給予存取私密金鑰的權限。





- 如何運作** ：擴充公開金鑰是經由確定程序 (BIP-32) 由 seed 詞組產生。它會建立子公開金鑰的階層樹狀結構，每個子公開金鑰都可以轉換成接收 Address。使用與被監視 Wallet 相同的衍生路徑 (例如 `m/44'/0'/0'`)，Watch-only wallet 會產生相同的位址，因此可以追蹤資金並建立新的接收位址。



![image](assets/fr/11.webp)





- 擴充的公開金鑰類型
 - xpub**：用於傳統組合（位址以「1」開頭，BIP-44）和 Taproot 組合（位址以「bc1p」開頭，BIP-86）。
 - ypub**：專為相容的 SegWit 錢包 (地址以「3」開頭，BIP-49) 設計。
 - zpub**：與原生 SegWit 組合相關（位址以「bc1q」開頭，BIP-84）。
 - Others (tpub, upub, vpub, etc.)**：用於替代網路（如 Testnet）或特定標準。例如，tpub 用於 Testnet 網路。





- 區別** ：xpub、ypub或zpub之間的選擇取決於Address類型（傳統、SegWit、Taproot或嵌套SegWit）和Wallet使用的BIP標準。請檢查您的來源組合所需的格式，以確保與 Blockstream App 相容。





- 安全性與機密性** ：擴充的公開金鑰在安全性方面並不敏感，因為它不允許資金被花費（無法存取私人金鑰）。然而，就機密性而言，它是敏感的，因為它會揭露所有公共位址和相關的交易歷史。



**建議**：將您的擴充公開金鑰視為敏感資訊加以保護。



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5.Hot Wallet 提醒





- Hot Wallet**、**Software Wallet**、**Wallet mobile**、**Software Wallet**：都是安裝在智慧型手機、電腦或任何連線到網際網路的裝置上的應用程式名稱，可讓 Bitcoin Wallet 的私人金鑰得到管理和安全保護。
- 硬體錢包**（也稱為 **Cold錢包**）會離線隔離金鑰，與此不同的是，軟體錢包是在連線環境中運作，因此更容易受到網路攻擊。





- 建議用途** ：
    - 非常適合管理中等金額的 Bitcoin，尤其是日常交易。
    - 適合初學者或資產有限的使用者，對他們來說，Hardware Wallet 似乎是多餘的。





- 限制**：較不適合儲存大筆資金或長期儲蓄。在這種情況下，請選擇 Hardware Wallet。




## 2.Blockstream 應用程式介紹





- Blockstream App** 是一款手機（iOS、Android）和桌面應用程式，用於管理 Bitcoin 投資組合和 Liquid Network 上的資產。於2016年被[Blockstream](https://blockstream.com/)收購，之前的名稱為*Green Address*，之後為*Blockstream Green*。
- 主要功能** ：
    - Blockchain Bitcoin 上的 Onchain** 交易。
    - 在 **Liquid** 網路上進行交易 (Sidechain 用於快速、機密的交換)。
    - Watch-only** 投資組合，用於監控無法存取鑰匙的基金。
    - 隱私權選項：透過**Tor**連線、透過 Electrum 連線至**個人節點**，或透過**SPV**驗證以減少對第三方節點的依賴。
    - 功能 **Replace-by-fee (RBF)** 加速未確認的交易。
- 相容性**：整合硬體錢包，例如 **Blockstream Jade**。
- Interface**：初學者可直覺操作，專家可使用進階選項。
- 注意**：本指南著重於 onchain 的使用。附錄中的其他教程涵蓋 Onchain、Watch-Only 和桌面版。




## 3.安裝和設定 Blockstream App



### 3.1. 下載





- 適用於 Android** ：
    - 從 Google Play 商店下載 [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)。
    - 替代方案：透過 [Blockstream 官方 GitHub](https://github.com/Blockstream/green_android) 上提供的 APK 檔安裝。
- 適用於 iOS** ：
    - 從 App Store 下載 [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590)。
- 注意**：請務必從官方來源下載，以避免詐騙性應用程式。



### 3.2. 初始設定





- 主畫面**：首次開啟時，應用程式會顯示沒有設定 Wallet 的畫面。建立或匯入的組合稍後會出現在這裡。



![image](assets/fr/02.webp)





- 自訂設定**：點選「應用程式設定」，調整下列選項，點選「儲存」，重新啟動應用程式並建立您的投資組合。



![image](assets/fr/03.webp)



#### 3.2.1.強化隱私 (僅限 Android)





- 功能**：停用螢幕截圖、隱藏工作管理員中的應用程式預覽，以及在手機鎖定時鎖定存取權限。
- 為什麼？保護您的資料，防止未經授權的實體存取或螢幕擷取惡意軟體。



#### 3.2.2.透過 Tor 連線





- 功能**：透過 **Tor** 路由網路流量，這是一個匿名網路，會加密您的連線。
- 為什麼？隱藏您的 IP Address 並保護您的隱私，如果您不信任您的網路 (例如公共 Wi-Fi)，這是您的理想選擇。
- 缺點**：可能會因為加密而導致應用程式變慢。
- 建議**：如果保密性是優先考量，請啟動 Tor，但請測試連線速度。



#### 3.2.3.連接至個人節點





- 功能**：透過 **Electrum 伺服器**，將應用程式連接到您自己的 ** 完整 Bitcoin 節點**。
- 為什麼？提供對 Blockchain 資料的完全控制，消除對 Blockstream 伺服器的依賴。
- 先決條件**：已設定的 Bitcoin 節點。
- 建議**：希望擁有最大主權的進階使用者。



#### 3.2.4.SPV 驗證





- 功能**：使用 ** 簡化付款驗證 (SPV)** 直接驗證某些 Blockchain 資料，而無需下載整個鏈。
- 為什麼？減少對 Blockstream 預設節點的依賴，同時保持行動裝置的輕量級。
- 缺點**：安全性不如 Full node，因為它依賴第三方節點提供某些資訊。
- 建議**：如果您無法使用個人節點，但偏好使用 Full node 以獲得最佳安全性，請啟動 SPV。





## 4.建立 Bitcoin 「僅看盤」投資組合



### 4.1.恢復已擴充的公開金鑰



要設定 Watch-only wallet，您必須先取得要監控的 Wallet 的擴充公開金鑰 (xpub、ypub、zpub 等)。此資訊一般可在您的軟體或 Hardware Wallet 的設定或 「Wallet 資訊」 區段中取得。





- 使用 Blockstream App 的範例：從 Wallet 首頁畫面，移至「設定」，然後移至「Wallet 詳細資訊」，複製 zpub ：



![image](assets/fr/09.webp)





- 替代方案 1：generate 包含擴充公開金鑰的 QR 碼，供下一步掃描。
- 替代方案 2：如果您的 Wallet 提供 output descriptor，請使用 output descriptor。



### 4.2. 匯入 Wallet 僅供觀看





- 注意**：在沒有攝影機或觀察者的私人環境中設定您的投資組合。
- 從主畫面按一下「設定新的投資組合」，然後按一下「開始」：



![image](assets/fr/04.webp)





- 出現下一個畫面：



![image](assets/fr/06.webp)






- (1) **「設定行動版 Wallet」** ：建立新的 Hot Wallet。請參閱附錄中的 "Blockstream App - Onchain "教學。
- (2) **「從備份還原」**：使用 Mnemonic 詞組 (12 或 24 個單詞) 匯入現有組合。注意：請勿從 Cold Wallet 匯入詞組，因為它會暴露在連接的裝置上，使其安全性失效。
- (3) **「僅限觀看」**：本教程中我們感興趣的選項。





- 然後選擇「**單一簽章**」和「**Bitcoin**」網路：



![image](assets/fr/12.webp)





- 貼上擴充的公開金鑰 (xpub、ypub、zpub 等)，掃瞄對應的 QR 碼，或輸入 output descriptor。即使應用程式指定 "xpub"，鑰匙 ypub、zpub 等也會被授權。然後按一下「連線」：



![image](assets/fr/13.webp)




### 4.3.使用 Wallet 僅需觀察



匯入後，Watch-only wallet 會顯示從延伸公開金鑰衍生出來的地址的總餘額和交易歷史。只有 onchain 交易是可見的（Liquid 交易會被忽略）。若要監控 Liquid Wallet，請在上一步選擇「Liquid」重複匯入。





- 檢視餘額與歷史記錄**：從首頁畫面檢視總餘額與鏈上交易歷史記錄：



![image](assets/fr/14.webp)





- generate 一個接收 Address**：點選「交易」，然後點選「接收」，建立一個新的 onchain Address。透過 QR code 或複製分享，即可接收資金：



![image](assets/fr/15.webp)





- 發送資金**：按一下 **「交易」**，然後按一下 **「寄送」**。您可以輸入 ：
 - 收件人的 Address。
 - 交易金額。
 - 交易費用。



不過，由於 Watch-only wallet 並未持有私密金鑰，因此無法直接傳送資金。若要簽署交易，請透過掃描 QR 碼 (例如 Coldcard Q 上的選項) 連接您的 Hardware Wallet 或 Exchange PSBT。



![image](assets/fr/16.webp)





- 注意**：請務必檢查收款的 Address 和交易詳細資料，以免出錯。發送至錯誤 Address 的資金將無法收回。




## 附錄



### A1.其他 Blockstream App 教學





- 使用 Onchain 網路 ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- 使用 Liquid Network ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- 桌面版本 ：



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2.擴充的公開金鑰





- 詞彙 ：
 - [擴充公開金鑰](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- 課程 ：
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3.最佳實踐



要安全有效地使用 **Blockstream App**，請遵循這些建議。它們將協助您在 **Bitcoin（onchain）**、**Liquid** 和 **Lightning** 網路上保護您的資金、優化您的交易，並維護您的機密性。





- 保護您的復原短語** ：
 - 教學：儲存您的 Mnemonic 詞組



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 使用安全認證** ：
 - 啟動**強大 PIN**或**生物辨識驗證** (指紋或臉部辨識) 以保護對應用程式的存取。
 - 切勿分享您的 PIN 碼或生物辨識資料。





- 保護您的隱私** ：
 - generate 為每個 onchain 或 Liquid 接收提供新的 Address，以限制 Blockchain 上的追蹤。
 - 啟動「Enhanced Privacy」、「Tor」和「SPV」功能。
 - 為了達到最高的保密性，請透過 Electrum 伺服器將您的 Wallet 連接到您自己的 Bitcoin 節點，而不要使用公共節點





- 選擇最適合您需求的網路** ：
 - Onchain**：長期託管或大額交易的首選 (費用相較於金額可忽略不计)。
 - Liquid**：用於快速、低成本的傳輸，並加強保密性。
 - 閃電**：選擇即時、低成本的小額轉帳。





- 請務必檢查送貨地址** ：
 - 在發送資金之前，請仔細檢查 Address。發送至錯誤的 Address 的資金將永久丟失。使用複製/貼上或 QR 代碼掃描，切勿手抄/修改 Address。





- 優化成本** ：
 - 對於 onchain 交易，根據緊急程度和網路擁塞情況選擇適當的費用 (慢、中、快)。
 - 少量使用 Liquid，或 Lightning。





- 隨時更新應用程式




### A4.額外資源





- 官方 Blockstream 連結：**
 - [官方網站](https://blockstream.com/)**
 - [行動應用程式支援](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)**：文件與聊天
 - [GitHub](https://github.com/Blockstream/green_android)**





- 區塊探索者 :**
 - Onchain： **[Mempool.space](https://Mempool.space/)**
 - Liquid ： **[Blockstream Info](https://blockstream.info/Liquid)**
 - 閃電： **[1ML (Lightning Network)](https://1ml.com/)**





 - 學習與教程：** ** [Plan ₿ Network](https://planb.network/)** ：
  - 保護您的復原短語



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** ：
 - [詞彙](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** ：
 - [詞彙](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
