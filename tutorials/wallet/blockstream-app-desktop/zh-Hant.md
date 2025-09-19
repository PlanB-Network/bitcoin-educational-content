---
name: Blockstream App - Desktop
description: 如何在電腦上使用 Hardware Wallet with Blockstream App？
---
![cover](assets/cover.webp)



## 1.簡介



### 1.1 教學目標





- 本教學說明如何在電腦上使用 **Blockstream App** 管理 Bitcoin **onchain** Wallet 與 **Hardware Wallet**，使主 Blockchain Bitcoin 上記錄的安全交易成為可能。
- 內容包括安裝、初始設定、連接 Hardware Wallet，以及接收和傳送上鏈比特幣。
- 注意：附錄中的其他教程涵蓋 Liquid、Watch-Only 和行動應用程式。



### 1.2 目標受眾





- 初學者**：希望使用安全桌面軟體和 Hardware Wallet 管理比特幣的使用者。
- 中級使用者：希望瞭解如何使用 Hardware Wallet 進行上鏈交易以及 Tor 或 SPV 等隱私選項的人。



### 1.3.硬件錢包的背景





- **Hardware Wallet**、**Cold Wallet**：一種離線儲存私人金鑰的實體裝置，提供高度的安全性以防網路攻擊，不同於**Hot 錢包** (連線裝置上的軟體錢包)。
- **建議用途**：
    - 適用於保證大額或長期儲蓄。
    - 適用於注重安全的使用者，他們希望保護自己的資金免於與連線裝置相關的風險。
- 限制：需要使用 Blockstream App 等軟體來檢視餘額、generate 位址和廣播 Hardware Wallet 簽署的交易。



## 2.Blockstream 應用程式介紹





- **Blockstream App** 是一款手機（iOS、Android）和桌面應用程式，用於管理 Bitcoin 錢包和 Liquid Network 上的資產。於2016年被Blockstream收購，原名為*GreenAddress*，後更名為*Blockstream Green*（2019年），現名為*Blockstream app*（2025年）。
- **主要功能**：
- Blockchain Bitcoin 上的 **Onchain** 交易。
    - 在 **Liquid** 網路上進行交易 (Sidechain 用於快速、機密的交換)。
- **Watch-only** 投資組合，用於監控無法存取鑰匙的基金。
    - 隱私權選項：透過**Tor**連線、透過 Electrum 連線至**個人節點**，或透過**SPV**驗證以減少對第三方節點的依賴。
    - 功能 **Replace-by-fee (RBF)** 加速未確認的交易。
- **相容性**：整合硬體錢包，例如 **Blockstream Jade**。
- **Interface**：初學者可直覺操作，專家可使用進階選項。
- 注意**：本指南著重於桌面版 Hardware Wallet 的 onchain 使用。其他教程作為附錄提供，涵蓋在行動應用程式、onchain、Liquid 和 Watch-Only 功能上的使用。



## 3.安裝和設定 Blockstream App 桌面



### 3.1. 下載





- 前往 [官方網站](https://blockstream.com/app/)，點選「_Download Now_」。下載與您的作業系統（Windows、macOS、Linux）相對應的版本。
- 注意**：請務必從官方來源下載，以避免使用詐騙軟體。**



### 3.2. 初始設定





- 主畫面：首次開啟時，應用程式會顯示沒有設定 Wallet 的畫面。建立或匯入的組合稍後會出現在這裡。



![image](assets/fr/02.webp)





- 自訂設定：按一下左下方的設定圖示，調整下列選項，然後離開 Interface 繼續。



![image](assets/fr/03.webp)



#### 3.2.1.一般參數





- 在「設定」功能表中，按一下「**一般**」。
- **功能**：變更軟體語言，必要時啟動實驗功能。



![image](assets/fr/04.webp)



#### 3.2.2.透過 Tor 連線





- 在「設定」功能表中，按一下「**網路**」。
- 功能：透過 **Tor** 路由網路流量，這是一個匿名網路，會加密您的連線。
- 為什麼？隱藏您的 IP Address 並保護您的隱私，如果您不信任您的網路 (例如公共 Wi-Fi)，這是您的理想選擇。
- 缺點：可能會因為加密而導致應用程式變慢。
- 建議：如果保密性是優先考量，請啟動 **Tor**，但請測試連線速度。



![image](assets/fr/05.webp)



#### 3.2.3.連接至個人節點





- 在「設定」功能表中，按一下「**自訂伺服器與驗證**」。
- 功能：透過 **Electrum 伺服器**，將應用程式連接到您自己的**完整 Bitcoin 節點**。
- 為什麼？提供對 Blockchain 資料的完全控制，消除對 Blockstream 伺服器的依賴。
- **先決條件**：已設定的 Bitcoin 節點。
- 建議：希望擁有最大主權的進階使用者。



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4.SPV 驗證





- 在「設定」功能表中，按一下「**自訂伺服器與驗證**」。
- 功能：使用**簡化付款驗證 (SPV)**，可下載區塊標頭，並透過包含證明 (Merkle) 來驗證您的交易，而無需儲存完整的 Blockchain。
- 為什麼？減少對 Blockstream 預設節點的依賴，同時保持裝置的輕量級。
- 缺點：安全性不如 Full node，因為它依賴第三方節點提供某些資訊。
- 建議：如果您無法使用個人節點，但偏好使用 Full node 以獲得最佳安全性，請啟動 **SPV**。



![image](assets/fr/07.webp)



## 4.將 Hardware Wallet 連接到 Blockstream App



### 4.1.初步考慮



#### 4.1.1.適用於 Ledger 使用者





- Blockstream Green 僅支援 Ledger 裝置 (Nano S、Nano X) 上的 **Bitcoin Legacy** 應用程式。
- 連接您的裝置前，在 **Ledger Live** 中應遵循的步驟 ：


1.移至 **「設定 」** → **「實驗性功能 」**，並啟用 ** 開發者模式**。


2.前往 **「我的 Ledger」** → **「應用程式目錄」**，然後安裝 **Bitcoin Legacy** 應用程式


3.在啟動 Blockstream Green 建立連線之前，請在 Ledger 上開啟 **Bitcoin Legacy** 應用程式。




- 注意**：請確認您的 Ledger 已經使用 PIN 碼解除鎖定，且 Bitcoin Legacy 應用程式在您連線時處於啟動狀態。



#### 4.1.2 初始化 Hardware Wallet





- 如果您的 Hardware Wallet（Ledger、Trezor 或 Blockstream Jade）從未使用過（無論是與 Blockstream Green 搭配使用，或是與 Ledger Live 等其他軟體搭配使用），您首先需要對其進行初始化。這個步驟需要在安全的環境中進行，不能有攝影機或觀察員：


1. **seed 短語生成 / Mnemonic 短語**（12、18 或 24 個單詞）：仔細寫在紙上。


2. **seed 詞組驗證**：測試 Wallet 從所記載的詞彙匯入，例如驗證擴充的公開金鑰。在傳送資金到 Wallet 和永久保護 seed 短語之前執行。


3. **Securing the seed phrase**：將短句儲存在實體媒體（紙張或金屬）上，並存放在安全的地方。切勿以數位方式儲存（不可使用螢幕截圖、雲端或電子郵件）。




- **重要**：如果裝置遺失或發生故障，seed 短語是您恢復資金的唯一方法。任何有存取權限的人都可以盜取您的 bitcoins。
- 用於備份和檢查 seed 句子的資源：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3.本教程的配置 ：





- 我們假設 Hardware Wallet 已經用 seed 詞組和鎖定 PIN 碼初始化。
- 我們假設 Hardware Wallet 從未與 Blockstream App 連線，因此需要建立新帳戶。如果 Hardware Wallet 已經使用 Blockstream App，開啟應用程式時會自動出現帳號。



### 4.2.開始連接





- 從主畫面按一下「**設定新的 Wallet**」，然後驗證條款與條件，再按一下「**開始**」：



![image](assets/fr/08.webp)





- 選擇「**在 Hardware Wallet**」選項：



![image](assets/fr/09.webp)





- 如果您使用的是 **Blockstream Jade**，請按一下對應的按鈕。否則，請選擇「**連接不同的硬體裝置**」：



![image](assets/fr/10.webp)





- 透過 USB 將 Hardware Wallet 連接到電腦，並在 Blockstream App 中選擇它：



![image](assets/fr/22.webp)





- Blockstream App 匯入您的投資組合資訊時，請稍候：



![image](assets/fr/23.webp)



### 4.3.建立帳號





- 如果您的 Hardware Wallet 已經使用 Blockstream App，您的帳號會在匯入後自動出現在 Interface 中。否則，請點擊 「**創建帳戶**」來創建帳戶：



![image](assets/fr/24.webp)





- 選擇「**標準**」來設定經典的 Bitcoin 產品組合：



![image](assets/fr/25.webp)





- 建立帳戶後，您可以存取您的 Interface 主要組合：



![image](assets/fr/26.webp)





## 5.與 Hardware Wallet 搭配使用 onchain Wallet



### 5.1.接收比特幣





- 從主投資組合畫面，按一下「**接收**」：



![image](assets/fr/27.webp)





- 應用程式會顯示**空白的接待 Address**。每次接收都使用新的 Address，可提高您的保密性。按一下「**複製 Address**」以複製 Address，或讓寄件者掃描顯示的 QR 代碼：



![image](assets/fr/12.webp)



** 選項** ：




- (1) 按一下箭頭，即可 generate 新增一個 Address 連接到您的投資組合。
- (2) 若要要求特定金額，請點選「**更多選項**」，然後點選「**要求金額**」。QR 將會更新，Address 將被 Bitcoin 付款 URI 取代，例如`Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) 若要重新使用先前的 Address，請按一下「**更多選項**」，然後按一下「**位址清單**」：



![image](assets/fr/14.webp)





- 驗證：仔細檢查共用的 Address 以避免錯誤或攻擊 (例如惡意軟體修改剪貼板)。
- 一旦交易在網路中廣播，它就會出現在您的 Wallet 中。等待 1 到 6 次確認，即可視為交易不可更改。



![image](assets/fr/28.webp)



### 5.2. 傳送比特幣





- 在主投資組合畫面中，按一下「**傳送**」。



![image](assets/fr/29.webp)





- **輸入詳細資料**：
    - (1) 檢查所選擇的資產是否為 **Bitcoin**（onchain）。
    - (2) 貼上收件人的 **Address 或使用網路攝影機掃描 QR 代碼，輸入收件人的 **Address。
- (3) 指出要發送的**金額（BTC、Satoshis 或其他單位）**。




![image](assets/fr/16.webp)





- 選擇 **交易費用**（選擇性） ：
 - 根據緊急程度從建議的選項（快速、中速、慢速）中選擇，並預計確認時間。
 - 若要自訂收費，請手動調整每 vbyte 的 Satoshis 數量。這些都會顯示在首頁畫面。另請參閱 [Mempool.space](https://Mempool.space/)。



![image](assets/fr/17.webp)





- 手動選擇 UTXO（選擇性）：按一下「**手動選擇 Coin**」，選擇交易中要使用的特定 UTXO。



![image](assets/fr/18.webp)





- 初步確認：檢查摘要畫面上的 Address、金額和費用，然後按一下「**確認交易**」。實際上，在您使用 Hardware Wallet 簽署之前，交易不會被釋放到網路中，只有 Hardware Wallet 擁有與將從中扣除 UTXOs (satoshis) 的地址相關聯的密匙。



![image](assets/fr/19.webp)





- 最後檢查和簽名**：在 Hardware Wallet** 畫面上確認所有交易參數正確無誤，然後用它簽署交易。Address 錯誤可能會導致不可挽回的資金損失。





- 廣播：簽署後，Blockstream App 會自動在 Bitcoin 網路上廣播交易。



![image](assets/fr/20.webp)





- **跟進**：
 - 交易在 Wallet 首頁畫面中顯示為「待決」，直到確認為止。
 - 只要交易尚未確認，就可以使用 **Replace-by-fee (RBF)** 功能，透過增加費用來加快確認速度 (請參閱附錄)。



![image](assets/fr/21.webp)



## 附錄



### A1.其他 Blockstream 教學





- 使用 Liquid Network ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- 匯入並追蹤「僅供觀看」的投資組合：



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- 在手機上使用 Blockstream App (Hot Wallet) ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2.Replace-by-fee (RBF) 的說明





- 定義：Replace-by-fee (RBF) 是 Bitcoin 網路的一項功能，允許寄件者透過增加費用來加速確認**鏈上**交易。
- **限制**：
    - RBF 不適用於 Liquid 或 Lightning 交易。
    - 初始交易必須標示為 RBF 相容，Blockstream App 會自動執行。
- 如需詳細資訊，請參閱 [我們的詞彙](https://planb.network/resources/glossary/rbf-replacebyfee)。



### A3.最佳實踐





- **保護您的復原短語**：
    - 將您的 Hardware Wallet 的 Mnemonic 詞組保存在實體媒體（紙張、金屬）上，放在安全的地方。
    - 切勿以數位方式儲存（雲端、電子郵件、截圖）。
    - 教學：儲存您的 Mnemonic 詞組：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **保護您的隱私**：





    - generate 每一個 onchain 接收一個新的 Address。
    - 啟動 **Tor** 或 **SPV** 以限制追蹤。
    - 透過 Electrum 連接到您自己的 Bitcoin 節點，以獲得最大的主權。
- 請務必檢查送貨地址：





    - 簽署前請檢查 Hardware Wallet 螢幕上的 Address。
    - 使用複製/貼上或 QR 代碼，避免手動出錯。
- **優化成本**：





    - 根據緊急程度和網路壅塞情況調整收費 (請參閱 [Mempool.space](https://Mempool.space/))。
    - 使用 Liquid 或 Lightning 進行快速、低成本的交易，不需要 onchain 安全性。
- **更新軟體**：





    - 讓您的 Blockstream App 和 Hardware Wallet 韌體保持更新，提供最新功能和安全修補程式。



### A4.額外資源





- **官方連結**：
    - [官方網站](https://blockstream.com/)
    - [支援 Blockstream App](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)：文件與聊天
    - [GitHub](https://github.com/Blockstream/green_qt)





- **區塊探索者**：
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - 閃電：[1ML (Lightning Network)](https://1ml.com/)





- 保護您的復原短語：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network**：



[詞彙](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**：



[詞彙](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb