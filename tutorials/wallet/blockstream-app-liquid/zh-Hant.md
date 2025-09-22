---
name: Blockstream App - Liquid
description: 如何設定 Blockstream App 和使用 Liquid Network
---
![cover](assets/cover.webp)


## 1.簡介


### 1.1 教學目標





- 本教學說明如何使用 **Blockstream App** 行動應用程式管理 **Bitcoin Liquid** 組合，即直接記錄在 Bitcoin "Liquid" 側鏈上的交易。
- 它涵蓋安裝、初始設定、建立 Software Wallet，以及在 Liquid 上接收和傳送 bitcoins 的操作。
- 注意：附錄中的其他教程涵蓋 Onchain、Watch-Only 和桌面版本。



### 1.2 目標受眾





- 初學者：希望透過整合 Liquid Network 的直覺式行動應用程式管理比特幣的使用者。
- 中級使用者：尋求瞭解 onchain 功能和隱私權選項（如 Tor 或 SPV）的人。



### 1.3 介紹 Liquid



**Liquid** 是 Bitcoin 的 **Sidechain**，由 **[Blockstream](https://blockstream.com/Liquid/)**開發，旨在提供更快、更多 Confidential Transactions 和進階功能，同時仍與主 Blockchain Bitcoin 相連。



Sidechain 是與 Bitcoin 並行運作的獨立 Blockchain，使用稱為 **雙向掛鉤**的機制。此系統可將比特幣鎖定在主 Blockchain 上，以建立 **Liquid-比特幣 (L-BTC)** 的代幣，可在 Liquid Network 上流通，同時保留與原始比特幣的同等價值。資金可隨時返回 Blockchain Bitcoin。



![image](assets/fr/17.webp)






- (1) **Peg-in**：比特幣 (BTC) 被 Liquid 聯盟鎖定在主 Blockchain 上。作為回報，在 Blockchain Liquid 上發行等量的 Liquid 比特幣 (L-BTC)，以確保兩個鏈之間的平價，並發送給使用者。





- (2) **獨立交易**：根據使用者需求，交易可同時、獨立地在主 Blockchain (BTC) 和 Sidechain Liquid (L-BTC) 上執行。





- (3) **Peg-out**：使用者將 Liquid-Bitcoins (L-BTC) 傳回給 Liquid 聯盟。聯盟隨後會在主 Blockchain 上解鎖等額的比特幣 (BTC) 並將其轉給使用者。



Liquid 依賴**聯盟**可信賴的參與者（交易所、認可的 Bitcoin 公司）來管理區塊驗證及雙邊錨定。Blockchain Bitcoin 是分散式並依賴於礦工，Liquid 則不同，Liquid 是一個**聯邦**網路，意即其安全性和管理依賴於這些參與者。儘管這意味著在分散性上的妥協，但卻能實現最佳化的效能與先進的功能。



![image](assets/fr/18.webp)



##### 為何使用 Liquid？





- **速度**：Liquid 上的交易確認時間約為 **1分鐘**，而上鏈交易則需 10 分鐘或更長時間，這都歸功於由驗證者聯盟每分鐘產生的區塊。
- 加強保密性：Liquid 使用 **Confidential Transactions**，可隱藏轉移的資產金額和類型，使交易更加隱密（雖然地址仍然可見）。
- **低費用**：Liquid 上的交易費用通常較低，非常適合經常轉帳或小額交易。
- 多種資產：除了 L-BTC 之外，Liquid 還支援發行其他數位資產，例如穩定幣或代幣，以供特定應用程式使用。
- 使用案例：Liquid 特別適用於跨平台交換、快速付款或需要智慧型契約的應用程式，同時仍與 Bitcoin 的安全性相連。



**註：** 本教學著重於透過 Blockstream App 使用 Liquid。若要深入瞭解 Liquid Network，您可在附錄中找到相關資源。



### 1.4.Hot Wallet 提醒





- **Hot Wallet**、**Software Wallet**、**Wallet mobile**、**Software Wallet**：都是安裝在智慧型手機、電腦或任何連線至網際網路的裝置上的應用程式名稱，可讓 Bitcoin Wallet 的私人金鑰得到管理與安全保護。
- 硬體錢包**（也稱為**Cold錢包**）**會離線隔離金鑰，與此不同的是，軟體錢包是在連線環境中運作，因此更容易受到網路攻擊。





- **建議用途**：
    - 非常適合管理中等數量的 Bitcoin，尤其是日常交易。
    - 適合初學者或資產有限的使用者，對他們來說，Hardware Wallet 似乎是多餘的。





- 限制：較不適合儲存大筆資金或長期儲蓄。在這種情況下，請選擇 **Hardware Wallet**。




## 2.Blockstream 應用程式介紹





- **Blockstream App** 是一款手機（iOS、Android）和桌面應用程式，用於管理 Liquid Network 上的 Bitcoin 錢包和資產。於 2016 年被 [Blockstream](https://blockstream.com/) 收購，之前的名稱為 *Green Address*，之後改名為 *Blockstream Green*。
- **主要功能**：
- Blockchain Bitcoin 上的 **Onchain** 交易。
    - 在 **Liquid** 網路上進行交易 (Sidechain 用於快速、機密的交換)。
- **Watch-only** 投資組合，用於監控無法存取鑰匙的基金。
    - 隱私權選項：透過**Tor**連線、透過 Electrum 連線至**個人節點**，或透過**SPV**驗證以減少對第三方節點的依賴。
    - 功能 **Replace-by-fee (RBF)** 加速未確認的交易。
- **相容性**：整合硬體錢包，例如 **Blockstream Jade**。
- **Interface**：初學者可直覺操作，專家可使用進階選項。
- 注意**：本指南著重於 onchain 的使用。附錄中的其他教程涵蓋 Onchain、Watch-Only 和桌面版。




## 3.安裝和設定 Blockstream App



### 3.1. 下載





- 適用於 **Android** ：
    - 從 Google Play 商店下載 [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)。
    - 替代方案：透過 [Blockstream 官方 GitHub](https://github.com/Blockstream/green_android) 上提供的 APK 檔安裝。
- 適用於 **iOS** ：
    - 從 App Store 下載 [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590)。
- 注意**：請務必從官方來源下載，以避免詐騙性應用程式。**



### 3.2. 初始設定





- 主畫面：首次開啟時，應用程式會顯示沒有設定 Wallet 的畫面。建立或匯入的組合稍後會出現在這裡。



![image](assets/fr/02.webp)





- 自訂設定：點選「應用程式設定」，調整下列選項，點選「儲存」，重新啟動應用程式並建立您的投資組合。



![image](assets/fr/03.webp)



#### 3.2.1.強化隱私 (僅限 Android)





- **功能**：停用螢幕截圖、隱藏工作管理員中的應用程式預覽，以及在手機鎖定時鎖定存取權限。
- 為什麼？保護您的資料，防止未經授權的實體存取或螢幕擷取惡意軟體。



#### 3.2.2.透過 Tor 連線





- 功能：透過 **Tor** 路由網路流量，這是一個匿名網路，會加密您的連線。
- 為什麼？隱藏您的 IP Address 並保護您的隱私，如果您不信任您的網路 (例如公共 Wi-Fi)，這是您的理想選擇。
- 缺點：可能會因為加密而導致應用程式變慢。
- 建議：如果保密性是優先考量，請啟動 **Tor**，但請測試連線速度。



#### 3.2.3.連接至個人節點





- 功能：透過 **Electrum 伺服器**，將應用程式連接到您自己的**完整 Bitcoin 節點**。
- 為什麼？提供對 Blockchain 資料的完全控制，消除對 Blockstream 伺服器的依賴。
- **先決條件**：已設定的 Bitcoin 節點。
- 建議：希望擁有最大主權的進階使用者。



#### 3.2.4.SPV 驗證





- 功能：使用**簡化付款驗證 (SPV)**直接驗證某些 Blockchain 資料，而無需下載整個鏈。
- 為什麼？減少對 Blockstream 預設節點的依賴，同時保持行動裝置的輕量級。
- 缺點：安全性不如 Full node，因為它依賴第三方節點提供某些資訊。
- 建議：如果您無法使用個人節點，但偏好使用 Full node 以獲得最佳安全性，請啟動 **SPV**。





## 4.建立 Bitcoin onchain 組合



### 4.1.開始建立





- 注意**：在沒有攝影機或觀察者的私人環境中設定您的投資組合。
- 從主畫面，按一下「開始」 ：



![image](assets/fr/04.webp)





- 如果您想管理**Cold Wallet**（離線Wallet）：點擊**「連接翡翠 」**使用Hardware Wallet Blockstream翡翠或其他相容的Cold錢包。



![image](assets/fr/05.webp)






- 出現下一個畫面：



![image](assets/fr/06.webp)






- (1) **「設定行動版 Wallet」** ：建立新的 Hot Wallet（Hot Wallet）。
- (2) **「從備份還原」**：使用 Mnemonic 詞組 (12 或 24 個單詞) 匯入現有組合。警告：請勿從 Cold Wallet 匯入詞組，因為它會暴露在連接的裝置上，使其安全性失效。
- (3) **「僅限閱讀」**：匯入現有的唯讀投資組合，以檢視餘額（例如您的 Cold Wallet 的餘額），而不暴露 Mnemonic 的短語。請參閱附錄中的 "Watch Only "教學。



**在本教程中**：按一下 **「Setup Mobile Wallet」** 建立 Hot Wallet。


您的 Wallet 會自動建立，並顯示 Wallet 首頁，這裡稱為「我的 Wallet 5」：



![image](assets/fr/07.webp)



**重要**：Blockstream App 已經簡化了 Wallet 的創建，不再自動顯示 12 個字的 seed 短語。 *儘管投資組合現在只需一次點擊即可建立，但如果您不儲存 seed 短語*，您將冒險失去存取資金的權利。



### 4.2.儲存 seed 詞組





- 在 Wallet 主畫面上，按一下「安全性」標籤，然後按一下「備份」提示或「復原語句」功能表：



![image](assets/fr/08.webp)



seed 12 字短語將會顯示，供您儲存。





- 以最小心的方式寫下您的復原短語。將其寫在紙上或金屬上，並將其保存在安全的地方（安全的離線位置）。此短語是您在裝置遺失或應用程式刪除時存取比特幣的唯一方法。
- 還要注意的是，任何人只要有這句話，就可以偷走您所有的 bitcoins。永遠不要以數位方式儲存：
 - 沒有截圖
 - 無雲端、電子郵件或訊息備份
 - 無複製/貼上（儲存至剪貼簿的風險）



**!這一點非常重要**。如需更多關於備份 ：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3.檢查 seed 句子



在向與此 seed 短語相關的 Address 發送資金之前，您必須測試 12 個單詞的備份。


要做到這一點，我們要寫下參考，刪除 Wallet，用備份還原，然後檢查參考是否無變。





- 在 Wallet 首頁畫面，點選「設定」標籤，然後點選「Wallet 詳細資料」，複製 zPub ( [擴充公開金鑰](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f))：



![image](assets/fr/09.webp)



注意：zpub Address 可以匯入您的 Blockstream 應用程式，用於 "Watch Only "功能 (請參閱附錄)。





- 刪除應用程式，然後透過 **「從備份還原 」**，輸入 Mnemonic 的短語來還原 Wallet，並檢查 zpub 是否無變。如果是，那麼您的備份是正確的，您可以將資金傳送至 Wallet。





- 若要瞭解有關如何執行復原測試的詳細資訊，請參閱此專題教學 ：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4.確保存取應用程式的安全



使用強大的 PIN 碼鎖定應用程式的存取權：




- 從 Wallet 首頁畫面，進入 **「安全性 」**，然後按一下 **"PIN "**。
- 輸入並確認 ** 隨機的 6 位數 PIN 碼**。



**生物辨識選項**：可用於增加便利性，但安全性不如穩健的 PIN 碼 (未經授權存取的風險，例如睡眠中的指紋或臉部掃描)。



**註**：PIN 碼可確保裝置安全，但只有 seed 短語可用於取回資金。





## 5.使用 Liquid Wallet



### 5.1.接收「L-BTC」比特幣



要接收 Liquid-Bitcoins (L-BTC)，有幾種方法可供選擇。您可以透過分享 Liquid 接收 Address 的方式，請人直接寄一些給您，詳情如下。



另外，Exchange 您的 bitcoins onchain 或透過 Lightning Network 使用 [a bridge such as Boltz](https://boltz.Exchange/) 取得 L-BTC：輸入您的 Liquid 接收 Address，依您的喜好付款，並收到您的 L-BTC。





- 從投資組合首頁畫面，點選'「**交易**」，然後點選**「接收 」**。



![image](assets/fr/19.webp)





- 預設情況下，應用程式會顯示空白的 ** 收據 Address，onchain** (SegWit v0 格式，以 `bc1q...` 開頭)。按一下「Bitcoin」，選擇 **Liquid Bitcoin** ：



![image](assets/fr/20.webp)





- **選項**：
 - (1) 按一下箭頭，選擇與此 seed 句子連結的另一個新 Address。
    - (2) 您也可以按一下右上方的三個圓點，然後按一下「位址清單」，從已使用/顯示的位址中選擇一個 Address。
    - (3) 若要要求特定金額，請按一下右上方的三個圓點，選擇「要求金額」，然後輸入所需金額。QR 將會更新，Address 將被 Bitcoin 付款 URI 取代。



![image](assets/fr/21.webp)





- 點選「**分享**」、複製文字或掃描 QR code，即可分享 Address/URI。
- 驗證**：盡可能檢查與收件者共用的 Address，以避免錯誤或攻擊（例如惡意軟體修改剪貼板）。



### 5.2. 傳送比特幣





- 從投資組合首頁畫面，按一下「**交易**」，然後按**「傳送」** ：



![image](assets/fr/22.webp)





- **輸入詳細資料**：
    - (1) 貼上收件人的 **Address 或掃描 QR 代碼，輸入收件人的 **Address。
    - (2) 檢查資產和資金寄送的帳戶。
- (3) 指出要傳送的**金額**。您可以選擇單位：L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- **檢查**：
    - 檢查摘要螢幕上的 Address、金額和費用。
    - Address 錯誤可能導致不可挽回的資金損失。提防修改剪貼板的惡意軟體。



![image](assets/fr/24.webp)





- 確認：滑動「傳送」按鈕簽署並分發交易。
- 跟進：在 Wallet 「交易」標籤中，交易顯示為「未確認」，然後是「已確認」，最後是「已完成」：



![image](assets/fr/25.webp)





- 在 Liquid 上，2 個區塊之間的時間相隔 1 分鐘，因此交易很快就會被確認和完成。




## 附錄



### A1.其他 Blockstream App 教學



使用 Onchain 網路



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

在「Watch Only」模式下匯入並追蹤 Wallet



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

桌上型電腦版本



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2.最佳實踐



要安全有效地使用 **Blockstream App**，請遵循這些建議。它們將協助您在 **Bitcoin（onchain）**、**Liquid** 和 **Lightning** 網路上保護您的資金、優化您的交易，並維護您的機密性。





- **保護您的復原短語**：
 - 教學：儲存您的 Mnemonic 樂句



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 使用**安全認證**：
 - 啟動**強大 PIN**或**生物辨識驗證** (指紋或臉部辨識) 以保護對應用程式的存取。
 - 切勿分享您的 PIN 碼或生物辨識資料。





- **保護您的隱私**：
 - generate 為每個 onchain 接收提供一個新的 Address，或 Liquid 限制在 Blockchain 上追蹤。
 - 啟動「Enhanced Privacy」、「Tor」和「SPV」功能。
 - 為了獲得最大的保密性，請透過 Electrum 伺服器將您的 Wallet 連接到您自己的 Bitcoin 節點，而不要使用公共節點





- 選擇最適合您需求的**網路**：
- **Onchain**：長期託管或大額交易的首選 (費用相較於金額可忽略不计)。
- **Liquid**：用於快速、低成本的傳輸，並加強保密性。
- **閃電**：選擇即時、低成本的小額轉帳。





- 請務必檢查送貨地址：
 - 在發送資金之前，請仔細檢查 Address。發送至錯誤的 Address 的資金將永久丟失。使用複製/貼上或 QR 代碼掃描，切勿手抄/修改 Address。





- **優化成本**：
 - 對於 onchain 交易，根據緊急程度和網路擁塞情況選擇適當的費用 (慢、中、快)。
 - 少量使用 Liquid，或 Lightning。





- 隨時更新應用程式




### A3.額外資源





- 官方連結：
- [官方網站](https://blockstream.com/)
- [行動應用程式支援](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)：**文件與聊天**
- [GitHub](https://github.com/Blockstream/green_android)





- 區塊探索者 :**
 - on chain ： **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[區塊流資訊](https://blockstream.info/Liquid)**
 - 閃電： **[1ML (Lightning Network)](https://1ml.com/)**





- 學習與教程：**[Plan ₿ Network](https://planb.network/)**：
 - 保護您的復原短語



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network**：
- [詞彙](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**：
- [詞彙](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb