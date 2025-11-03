---
name: Ride The Lightning (RTL)
description: 使用 Ride The Lightning (RTL) 管理您的 Lightning 節點
---
![cover](assets/cover.webp)


## 1.簡介



**Ride The Lightning (RTL)** 是一個完整的 Interface 網路應用程式，用於管理 Lightning Network 節點。這個自託管的 Web 應用程式提供一個可從瀏覽器存取的 Lightning 「駕駛艙」。RTL 可與所有主要的 Lightning 實作 (LND、Core Lightning/CLN 和 Eclair) 搭配使用，並讓您完全控制您的節點和頻道。RTL 是開放原始碼（MIT 授權）且免費的，預設已整合在許多交鑰匙節點解決方案（RaspiBlitz、MyNode、Umbrel 等）中。



**如果沒有圖形化的 Interface，Lightning 節點只能透過人性化的 CLI 指令來管理。RTL 使用符合人體工學的 Interface 簡化了這些操作。以下是主要的應用**：





- **檢視您的頻道和節點** - 面板顯示 On-Chain 結餘、Lightning 流動性 (本地/遠端)、同步狀態、節點別名等。您可以檢視您的頻道清單、容量、本地/遠端分佈和狀態。RTL 提供上下文相關的儀表板，可從不同角度分析活動。





- **Lightning 頻道管理** - 只需幾下點擊即可開啟/關閉頻道。RTL 讓您無需指令即可連線至對等人並開啟通道。您可以調整路由費、檢視結餘分數，或啟動循環再平衡以重新平衡通道間的資金。





- **追蹤與付款** - RTL 管理 Lightning 交易：透過發票傳送付款、generate 發票接收、追蹤交易（付款、路由）與詳細歷史。Interface 還會分析路由，查看哪些付款經過您的節點。





- **Wallet On-Chain 管理與備份** - On-Chain 標籤可讓您 generate 位址與傳送交易。RTL 可透過匯出 LND 的 SCB 檔案輕鬆儲存頻道，每次修改頻道都會自動更新。



簡而言之，RTL 是 Lightning Network 的**強大儀表板**，提供教育性的 Interface 供您每天試用節點。本教學將引導您完成其安裝與使用，以管理您的通路與付款。



## 2.RTL 的技術操作



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



在進入細節之前，先簡單瞭解一下 ** RTL 與您的 Lightning 節點 ** 在技術層級上的互動方式是非常有用的。



**一般架構：** RTL 是使用 Node.js (後端) 和 Angular (前端) 建立的 Web 應用程式。具體而言，RTL 以小型本機 Web 伺服器（預設埠為 3000）的方式執行，透過其 API 與您的 Lightning 實作進行對話。取決於.NET的類型：





- 透過 **LND**，RTL 使用 LND 的 REST API (port 8080) 來執行 Lightning 指令。連線以 TLS 加密，並需要 LND 的 **admin macaroon** 檔案進行驗證。





- 使用 **Core Lightning (CLN)**，RTL 使用 *c-lightning-REST* 提供的 REST API，或透過 `commando` 外掛程式使用 **access rune**。Umbrel 等解決方案會自動配置這些 Elements。





- 使用 **Eclair** 時，RTL 會使用設定的驗證密碼連線至 Eclair REST API。



** 配置與安全性：** RTL 透過 JSON 檔案 (`RTL-Config.json`)進行配置，您可在其中定義 Web 連接埠、存取密碼以及與節點的連線資訊。Interface Web 受登入/密碼保護 (預設 `password` 可變更)，並支援 2FA。預設情況下，RTL 以本機 HTTP (`http://localhost:3000`)方式執行，但若要遠端存取，請務必使用安全連線 (透過反向代理、Tor 或 VPN 的 HTTPS)。



簡而言之，RTL 是一個額外的元件，可透過安全 API 連接到您的節點，需要適當的存取代碼，並提供其本身的安全性 Layer。這種模組化的架構甚至允許您使用一個 RTL 實例來管理**多個 Lightning 節點**。



## 3.RTL 安裝



由於 RTL 是以開放原始碼軟體的形式散佈，因此有多種方法可以將它安裝到您的系統上。在本節中，我們將介紹兩種主要方法：手動安裝和透過 Umbrel 安裝。



### 手動方法



如果您想保持細緻的控制，或是將 RTL 整合到自訂組態中，則適合手動安裝。以下步驟適用於執行 Linux 的 LND 節點 (例如 Raspberry Pi 或執行 Ubuntu/Debian 的 VPS)，但對於 CLN/Eclair 也類似。



**先決條件：** 確保您的機器上有一個**同步**的 Bitcoin 節點和一個正常運作的 Lightning 節點 (LND、CLN 或 Eclair)。RTL 本身不包含 Lightning 節點，它連接到現有的節點。您也需要安裝 **Node.js**（建議版本 14 以上）。您可以使用 `node -v` 檢查，或從官方網站 (https://nodejs.org/en/download/) 或您的套件管理員安裝 Node。



主要安裝階段為 ：



**下載 RTL 程式碼**：克隆官方的 RTL GitHub 套件庫到您選擇的目錄。例如



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**安裝相依性**：RTL 是一個 Node.js 應用程式，因此您需要安裝其所需的模組。在 RTL 資料夾中，執行 ：



```bash
npm install --omit=dev --legacy-peer-deps
```



此指令會安裝必要的 NPM 套件 (忽略開發上的相依性)。建議使用 `--legacy-peer-deps` 選項，以避免可能的 Node 相依性衝突。



**RTL-Config**：相依性就位後，準備組態檔案。複製/重命名專案根目錄中的「Sample-RTL-Config.json」檔案為「RTL-Config.json」。在您的 .NET Framework 中開啟它：





- UI 密碼：選擇一個安全的密碼，並在 `multiPass` 中輸入 (取代預設的 `"password"`)。
- 連接埠：預設為 `3000`。如果您的機器已使用此連接埠，您可以變更它。
- 節點：在 `nodes[0]` 區段中，調整節點的參數：
     - `lnNode`：節點的描述性名稱 (例如：`"LND Node Maison"`)。
     - lnImplementation`：`"LND「`（或`」CLN"`/`"ECL"`視情況而定）。
     - 在「驗證」下：
       - macaroonPath`：指定包含 LND 的 macaroon 管理員資料夾的完整路徑。
       - `configPath`: 節點設定檔案的路徑 (對於 LND，為 `LND.conf`)。
     - 在「設定」下：
       - `fiatConversion`: 如果要轉換法定貨幣，請設定為 `true`。
       - `unannouncedChannels `：設為 `true`，可以看到未通知的頻道。
       - themeColor` 和 `themeMode`：Interface 自訂。
       - channelBackupPath`：LND 通道備份的路徑。
       - `lnServerUrl`：您的 Lightning 節點的 URL (例如 `https://127.0.0.1:8080`)。



**啟動 RTL 伺服器**：在 RTL 資料夾中，執行 ：



```bash
node rtl
```



應用程式啟動後，可從 `http://localhost:3000` 存取。



**(可選) 以服務方式執行 RTL**：若要自動啟動，請建立 systemd ：



要做到這一點：




- 在您的電腦上開啟終端機。
- 使用下列指令建立新的服務檔案 (將 `nano` 改為您喜愛的編輯器)：


```bash
sudo nano /etc/systemd/system/RTL.service
```




- 將以下內容複製並貼到此檔案中：



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- 將 `/path/to/RTL/rtl` 改為您電腦上 `rtl` 檔案的實際路徑，並將 `<your_user>` 改為您的 Linux 使用者名稱。
- 儲存並關閉檔案。
- 重新載入 systemd 設定：


```bash
sudo systemctl daemon-reload
```




- 啟動並啟動 RTL 服務：


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



現在每次重新開機時，RTL 都會自動啟動。您可以使用 ：


```bash
sudo systemctl status RTL
```



### 透過 Umbrel 進行安裝



如果使用 [Umbrel](https://getumbrel.com)，RTL 安裝就簡單多了：





- 存取 Interface Umbrel (通常透過 `http://umbrel.local`)
- 前往 ** 應用程式商店**
- 搜尋 "Ride The Lightning"



**重要提示：Umbrel App Store 中有兩個獨立的 RTL 應用程式：**




- **Ride The Lightning** (for LND)：與 Umbrel 的預設 Lightning 節點 (LND) 搭配使用。
- Ride The Lightning (Core Lightning)**：僅當您已在 Umbrel 上安裝 *Core Lightning* 應用程式，並希望使用 RTL 管理此節點時才使用。



*每個 RTL 版本都預先設定好與相對應的實作（LND 或 Core Lightning）對話。如果您沒有變更您的 Lightning 節點，只需選擇經典的 LND 版本*。



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- 按一下 ** 安裝**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**重要事項：** 安裝完成後，RTL 會顯示預設密碼的畫面。 **複製並儲存這個密碼** - 您需要它來登入 Interface RTL。每次 RTL 啟動時都會顯示此密碼，直到您勾選「不再顯示」選項。



Umbrel 會自動處理 ：




- 下載並設定 RTL
- 設定 Lightning 節點的存取權限
- 管理更新
- 確保存取 Interface



安裝後，應用程式會出現在 Umbrel 的 *Apps* 功能表中。按一下 ** Ride The Lightning** 以啟動它。



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



在登入畫面中，輸入之前複製的密碼。登入後，就可以直接從 Umbrel 面板存取 Interface web RTL，不需要額外的設定！



## 4.Interface RTL 的介紹與使用



現在 RTL 已經開始運作，讓我們來探索它的 Interface 網頁及其主要功能。我們將透過應用程式的不同部分，為您提供完整的概觀。



### 主控制面板



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



當您登入後，您就可以存取**主控制面板**，它會提供您 Lightning 節點的總覽。此頁面集中了基本資訊：




- 您的 Lightning 結餘總額
- On-Chain 結餘可用
- 您的流動資金明細（流入/流出）
- 透過您的 Lightning 節點快速存取傳送與接收 Satss



### 基金管理 On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



**On-Chain** 標籤可讓您直接在主鏈上管理您的比特幣：




- 以不同單位顯示餘額 (Sats、BTC、美元)
- 完整的交易清單
- Address 代 Taproot (P2TR)、P2SH (NP2WKH) 或 Bech32 (P2WKH)
- UTXO 管理、接收和發送比特幣



### 閃電：子功能表的詳細介紹



Interface RTL 擁有 Lightning Network 專用的側邊功能表，匯集了管理節點的所有基本功能。以下是每個子功能表的詳細資訊，依畫面截圖的順序排列：



#### 1.同儕/管道



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



此子功能表可讓您 ：




- 檢視您已連線的同伴清單，以及開啟或等待中的 Lightning 頻道。
- 新增一個對等點 (連接到另一個 Lightning 節點)。
- 開啟、關閉或管理現有的通路。
- 檢視每個通道的詳細資訊：容量、本地/遠端餘額、狀態、交易歷史、餘額分數等。



#### 2.交易



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



在此子功能表中，您可以 ：




- 發送 Lightning 付款（透過 Invoice）。
- generate 並管理發票以收取付款。
- 查看發送和接收付款的完整歷史記錄，包括詳細資訊（金額、日期、狀態、費用、跳過次數等）。



#### 3.路由



此子功能表顯示 ：




- 您的節點為其他 Lightning Network 使用者路由的付款。
- 路由統計資料：中繼的交易筆數、賺取的費用、遇到的錯誤。
- 可輸出歷史記錄以進行進階分析。



#### 4.遞延



此子功能表提供 ：




- 有關您的 Lightning 節點活動的詳細報告。
- 有關渠道、付款、費用、容量等的圖表。
- 可讓您更了解節點效能的工具。



#### 5.圖形查詢



此子功能表可讓您 ：




- 探索 Lightning Network 的拓樸結構。
- 搜尋特定節點或頻道。
- 取得有關連線性和整體網路容量的資訊。



#### 6.簽署/驗證



此子功能表提供 ：




- 用您節點的金鑰簽署訊息的能力（Ownership 的證明）。
- 簽章驗證來驗證其他節點的訊息。



#### 7.備份



此子功能表專門用於備份：




- 匯出通道備份檔案 (SCB for LND)。
- 必要時還原設定或通道。
- 保護您的備份的提示。



#### 8.節點/網路



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



在此子功能表中，您可以找到 ：




- Lightning 節點狀態的完整摘要：別名、版本、顏色、同步狀態。
- 頻道統計資料 (使用中、等待中、關閉)、總容量、連線性。
- 有關全局 Lightning Network 的資訊，以及您的節點在其中的位置。



### 服務：Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz 是一種隱私友好的非監禁 Exchange 服務，可在 Lightning Network 和 Blockchain Bitcoin (On-Chain) 之間轉換比特幣。它提供兩種操作方式：反向海底交換 (**Swap Out**) 和海底交換 (**Swap In**)。



#### 掉換（反向潛水艇掉換）



Swap Out 可將 Lightning Network 上可用的 Satss 兌換成 On-Chain 比特幣。當一個節點的輸入容量耗盡時，或當您想從 On-Chain Address 收回資金時，這個機制就很有用。過程如下




- 使用者選擇要兌換的金額
- 節點發送一個 Lightning 付款給 Boltz
- 在 Exchange 中，Boltz 用 On-Chain 封鎖了等額的比特幣
- 交易確認後，使用者可透過揭露交換時使用的秘密來領取資金。



這個過程是非監護性的，Boltz 從不持有使用者的資金。


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### 交換 (潛艇交換)



另一方面，Swap In 允許 On-Chain 資金重新注入 Lightning Network。這對於恢復通道的輸出容量特別有用。步驟如下：




- 使用者將 bitcoins 傳送至 Boltz 所產生的特定 Address
- Boltz 必須支付使用者節點所產生的 Lightning Invoice 才能釋放這些資金。
- 一旦支付了 Invoice，「閃電 」通道上就有了資金，增加了節點的輸出能力



![Configuration d'un swap-in](assets/fr/12.webp)



這兩種機制使 Lightning 渠道的流動性得到有效管理，同時保持用戶對其資金的主權。



### 配置與客製化



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



**Node Config** 標籤可讓您自訂您的體驗：




- 啟動未經通知的頻道
- 自訂銷售顯示
- Block explorer 配置
- 調整 Interface



### 文件和幫助



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



最後，**Help** 部分提供 .NET Framework 的全面說明文件：




- 初始設定
- 同儕與通路管理
- 付款與交易
- 備份與還原
- 報告與統計
- 簽名與驗證
- 節點與應用程式參數



這套全面的 Interface 可讓您有效率地管理您的 Lightning 節點，從基本操作到進階功能，全都在直覺式、井然有序的 Interface 中完成。



## 5.進階使用個案與安全性



在本節中，以下是您需要知道的事項，以進一步使用 RTL 並確保您的 Lightning 節點安全：



### 監控和故障排除



若要監控您的節點，您可以匯出 RTL 資料 (日誌、CSV) 並在 Grafana 等工具中檢視。若發生問題 (付款受阻、頻道不活躍)，可查詢 LND/CLN 日誌，並使用診斷指令 (`lncli listchannels`、`lncli pendingchannels`等)。RTL 也提供 Interface 日誌來監控路由事件。



### 安全遠端存取



切勿在網際網路上直接暴露 RTL。優先使用.NET：




- **VPN** (例如 Tailscale) 用於私人加密存取
- **Tor** 提供安全的匿名存取
- 反向代理 **HTTPS** (Nginx/Caddy)，前提是您知道如何設定它



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 良好的安全措施





- **保護您的存取權限**：切勿共用 admin.macaroon 或您的 RTL 密碼。限制敏感檔案的權限。
- 定期備份：每次修改後匯出通道備份檔案 (SCB)，並儲存在節點之外。
- 更新：讓 **RTL、您的節點和 Umbrel** 保持在最新的安全修復狀態。
- **保密性**：在分享日誌和螢幕截圖之前先將其匿名。絕不公開分享您的餘額或同儕清單。
- 單一存取**：RTL 並非多使用者。請勿共用管理存取權。如需唯讀存取，必要時請使用專用的 Macaroon。



通過應用這些原則，您可以大大限制風險，並保持對您的 Lightning 節點的控制。



## 7.總結



**Ride The Lightning** 是有效管理 Bitcoin/Lightning 節點的必要工具，不論您是初學者或進階使用者。它提供清晰的 Interface 來控制您的通道、付款和節點健康，同時加深您對 Lightning Network 的了解。



RTL 因其多執行相容性、進階功能 (重新平衡、交換、報告) 及其教學方式而脫穎而出。對於簡單的需求，Interface Umbrel 或 Wallet mobile 就已經足夠，但 RTL 對於主動、最佳化的節點管理來說，是非常合理的。



要瞭解更多資訊 ：




- RTL 官方網站：https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- Reddit r/lightningnetwork：[r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - 技術討論、專案公告、回饋和教育資源
- Umbrel 社區論壇：[community.getumbrel.com](https://community.getumbrel.com) - 官方論壇，設有 Bitcoin/Lightning 專區、指南及常見問題解決方案
- Lightning Network 開發人員：[github.com/lightning](https://github.com/lightning) - 官方 GitHub 套件庫，用於跟進開發並提供原始碼
- 堆疊 Exchange **Bitcoin** ：[Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - 開發人員與進階使用者的技術問與答



簡而言之，RTL 讓您在現代化、功能齊全的 Interface 中，完全控制您的 Lightning 節點。



**Sources :** RTL 官方網站；RTL GitHub；Umbrel App Store；Umbrel 社群；Plan ₿ Academy 資源。



為了加深您對 Lightning Network 工作原理的瞭解，我也建議您參加這個免費課程：



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb