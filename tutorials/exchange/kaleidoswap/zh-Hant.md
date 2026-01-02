---
name: KaleidoSwap
description: 使用 KaleidoSwap 在 Lightning Network 上進行 RGB 資產交易的進階指南
---

![cover](assets/cover.webp)


KaleidoSwap 是一個複雜的開放源碼桌面應用程式，它在 RGB 協定和 Lightning Network 之間架起了一座橋樑。它是管理 RGB Lightning 節點、透過 LSPS1 規格與 RGB Lightning Service Providers (LSP) 進行互動，以及執行 RGB 資產原子交換的全面介面。


KaleidoSwap 作為一種非保管型解決方案，可讓使用者保持對其金鑰和資料的完全控制。透過利用 RGB 的客戶端驗證模式，它可以在 Bitcoin 的基礎上實現私有且可擴展的智慧契約。本教學深入探討 KaleidoSwap 的進階功能，引導您了解「有色」UTXO 管理、特定資產的通道流動性以及莊家-莊家交易模式的複雜性，確保您能充分利用這個功能強大的分散式交換協定。


## 安裝


KaleidoSwap 為主要作業系統提供預先建立的二進位檔案，但對於進階使用者而言，從原始碼建立可確保您以特定的配置執行最新的程式碼。


### 下載二進位檔


您可以從 [官方網站](https://kaleidoswap.com/) 或 [GitHub 發佈頁面](https://github.com/kaleidoswap/desktop-app/releases) 下載適用於您作業系統的最新版本。


### 安裝方法


1.  **Windows**：下載 `.exe` 安裝程式並執行。

2.  **macOS**：下載`.dmg`檔案，開啟後拖曳 KaleidoSwap 到您的 Applications 資料夾。

3.  **Linux**：下載 `.AppImage` 或 `.deb` 檔案並安裝/執行。



## 節點設定選項


當您第一次啟動 KaleidoSwap，您會看到**連接畫面**。這是設定環境的第一步。


![Node Selection Screen](assets/en/01.webp)


您必須選擇與 RGB Lightning Network 連線的方式。此選擇會影響您的控制層級和隱私權。


### 選項 1：本端節點 (建議用於自我保管)


**For complete control and privacy**, run a node directly on your machine, see the advantages below：


- 自我監護**：您持有鑰匙。沒有第三方可以凍結您的資金或審查您的交易。
- 隱私**：您的資料會保留在您的裝置上。
- 獨立性**：不依賴外部服務供應商。


如果您選擇 **本機節點**，就會進入設定畫面，您可以在此建立新的 wallet 或還原現有的 wallet。


![Local Node Setup Screen](assets/en/02.webp)


### 選項 2：遠端節點


連接至遠端 RGB Lightning Node（自行託管於 VPS 或託管供應商）。


- 優點**：無須使用本機資源，全天候可用。
- 取捨**：需要信任主機或管理遠端伺服器。


![Remote Node Setup Screen](assets/en/03.webp)


*** 我們強烈建議您運行您自己的節點 - 在本機運行 (選項 1) 或自我託管一個遠端節點 - 以充分發揮 Bitcoin 和 RGB 的抗審查特性。


## 建立 Wallet


KaleidoSwap 管理 Bitcoin 和 RGB 資產。wallet 的建立過程會初始化一個 keystore，以保護您的 on-chain 資金和 Lightning 通道狀態。


以下是詳細流程：

1.開啟 KaleidoSwap 並選擇 ** 本地節點**。

2.按一下 **Create New Wallet**。

3. **帳號設定**：輸入 ** 帳戶名稱**，並選擇 ** 網路** (例如：Bitcoin、Mainnet、Testnet、Signet)。

4. **進階設定**（可選）：如果您是高階使用者，可以在「進階設定」下設定自訂 RPC 端點、Indexer URL 或 Proxy 設定。

5.按一下 **繼續**。

6. **密碼**：設定強大的密碼，在本機加密您的 wallet 檔案。

7. **Recovery Phrase**：寫下您的 seed 詞組並妥善保存。


    - 關鍵**：要恢復您的 on-chain 資金和節點身分，必須使用此短語。
    - 警告**： **Lightning 通道狀態無法單獨從 seed 完全復原**。您必須同時維護靜態通道備份 (SCB)，才能恢復鎖定在通道中的資金。


![Wallet Creation Screen](assets/en/04.webp)



## 儀表板總覽


一旦您的 wallet 建立後，您會被導向到主 **儀表板**。


![KaleidoSwap Dashboard](assets/en/05.webp)


注意：上面的截圖顯示的 wallet 已經注資並擁有活動頻道。新的 wallet 在您注資之前會顯示零餘額和無活動頻道。


## 資助您的 Wallet


要使用 RGB 資產進行操作，您需要為您的 wallet 存入資金。KaleidoSwap 支援透過 on-chain 交易或 Lightning Network 存入 Bitcoin 和 RGB 資產。


### 存入 Bitcoin


1.在 Quick Actions（快速操作）功能表中按一下 **Deposit（存款）**。

2.從資產清單中選擇 **BTC**。


![Select BTC Asset](assets/en/06.webp)


3.選擇您的存款方式： **On-chain** 或 **Lightning**。


![BTC Deposit Options](assets/en/07.webp)



- 鏈上**：掃描 QR 碼或複製地址，從另一個 wallet 傳送 Bitcoin。
- 閃電**：產生所需金額的發票。


![BTC On-chain Deposit](assets/en/08.webp)


### 存入 RGB 資產和彩色 UTXOs


若要接收 RGB 資產 (如 USDT)，您需要特定的 UTXO 可用來「上色」（指定資產）。


1.按一下 **存款**，然後選擇 RGB 資產 (例如 USDT)。 **重要**：如果這是**第一次**您的節點接收此特定資產，請**將資產 ID 欄位留空**。輸入未知資產的 ID 會導致節點回傳錯誤，因為它尚未識別該資產。

2.選擇**鏈上**或**閃電**。


![USDT Deposit Options](assets/en/09.webp)


#### 鏈上接收模式：見證與盲目


接收 RGB 資產 on-chain 時，您有兩種隱私模式：



- Blinded Receive (建議用來保護隱私)**：您提供「blinded」UTXO 給發送者。您要求寄件者將資產傳送至您擁有的現有 UTXO，但您混淆了實際的 UTXO 識別碼。這提供了更好的隱私性。
- 見證接收**：您提供一個標準的 Bitcoin 位址。您要求寄件者將資產傳送至該地址，以為您建立*新的 UTXO。這可讓 RGB 資產直接附加到交易建立的新 UTXO。


#### 閃電存款


對於 Lightning 存款，只需 generate 發票即可。RGB 資產將通過您的開放渠道傳送給您。


![USDT Lightning Invoice](assets/en/10.webp)



## 使用 RGB 資產開啟通道


要在 Lightning Network 上路由 RGB 資產，您需要一個具有足夠流動性和資產配置的通道。最簡單的入門方法是向 LSP（閃電服務供應商）**購買通道**。


### 向 Kaleido LSP 購買頻道


1.移至 **Channels** 標籤。您會看到「開啟頻道」（手動）或「購買頻道」（LSP）的選項。

2.按一下 ** 購買頻道**。


![Channels Dashboard](assets/en/11.webp)


3. **Connect to LSP**：應用程式將連接到預設的 Kaleido LSP。此提供商提供入站流動性，並支援 RGB 資產路由。


![Connect to LSP](assets/en/12.webp)


4. **設定通道**：


    - 容量**：選取頻道的 Bitcoin 總容量。
    - RGB 分配**：選擇您希望能夠接收或傳送的 RGB 資產 (例如 USDT)。LSP 將確保通道已設定為支援此資產。


![Configure Channel](assets/en/13.webp)



    - RGB 分配**：選擇您希望能夠接收或傳送的 RGB 資產 (例如 USDT)。LSP 會確保頻道已設定為支援此資產。


![RGB Allocation](assets/en/14.webp)


5.  **付款**：您必須向 LSP 支付費用，以打開通道並提供流動性。您可以使用**Lightning**或**On-chain** Bitcoin支付。付款可以從您的內部 KaleidoSwap wallet 或外部 wallet 進行。


![Complete Payment](assets/en/15.webp)


6.一旦確認付款，LSP 將啟動通道開啟交易。您會看到**訂單完成**畫面。


![Order Completed](assets/en/16.webp)


7.在區塊鏈上確認之後，您的通道就會啟動，並準備好進行 RGB 轉帳。



## 交易：接受者-製造者模式


KaleidoSwap 的交易引擎以**做市商模式**運作。您可以手動與同行進行資產交換，也可以使用做市商 (LSP)。


### 與做市商 (LSP) 進行交換


這是最常見的交易方式。您作為**接受者**，根據 LSP（**製造者**）提供的可用流動性執行訂單。


1.導覽到 **Trade** 標籤，然後選擇 **Market Maker**。

2. **Enter Amount**（輸入金額**）：輸入您要傳送的 Bitcoin 金額 (或您要接收的資產)。介面會顯示估計匯率和費用。


![Market Maker Swap](assets/en/17.webp)


3. **確認交換**：檢視詳細資訊，包括匯率和您將收到的確切金額。按一下 **確認交換**。


![Confirm Swap](assets/en/18.webp)


4. **處理**：交換在 Lightning Network 上以原子方式執行。您會看到一個狀態畫面，顯示交換正在等待中。


![Swap Pending](assets/en/19.webp)


5. **成功**：HTLC 一經結算，交換即告完成，資產即進入您的通道。


![Swap Success](assets/en/20.webp)



## 開發人員 API


對於在 KaleidoSwap 之上建置的開發人員，應用程式會暴露一個支援的 API：



- RGB LSPS1**：用於自動化流動性服務。
- 交換 API**：用於程式化交易和做市商。
- WebSocket**：用於即時市場資料訂閱。


有關完整的端點和規格，請參閱 [API 文件](https://docs.kaleidoswap.com/api/introduction)。


## 總結


KaleidoSwap 讓您能夠在 Lightning Network 上充分利用 RGB 資產的隱私性和可擴展性。透過瞭解 Colored UTXOs 和通道資產分配，您可以充分利用這個強大的分散式交換協定。