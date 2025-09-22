---
name: ThunderHub
description: Interface Lightning 節點管理網站 LND
---
![cover](assets/cover.webp)



## 簡介



ThunderHub 是 Lightning 節點 (LND)** 的**開放源碼管理器，提供可從任何裝置或瀏覽器存取的直覺式 Interface。



**主要功能：**




- **監控**：結餘、通路、交易、路由統計的全球檢視
- 管理**：開啟/關閉通路、收款/付款、通路平衡

The line appears to have an unbalanced ** marker. Here's the corrected version:

- **管理**：開啟/關閉通路、收款/付款、通路平衡
- 整合：支援 LNURL、透過 Boltz 進行交換、Amboss 備份
- Interface 響應式：相容於行動裝置、平板電腦和桌上型電腦的**深色/淺色主題**



ThunderHub 可輕鬆與 **Umbrel**、**Voltage**、**RaspiBlitz** 及 **MyNode** 整合，簡化節點的日常管理。



**ThunderHub 特別適合正在尋找符合人體工學的 Interface 來管理其通道、控制流動性（再平衡）、監控交易以及整合第三方服務（如 Amboss）的業者。透過本機或 Tor 連線可確保安全性。**



如果您還沒有 Lightning 節點，建議您參考我們的 LND Umbrel 教學：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## 安裝



ThunderHub 可以根據您的 Lightning 節點主機環境，以多種不同的方式安裝。無論您使用的是交鑰匙解決方案（Umbrel、Voltage、RaspiBlitz、MyNode、Start9等）還是手動安裝，ThunderHub通常都不費吹灰之力即可使用。以下我們將介紹兩種常見的方式：透過 Umbrel App Store，以及手動安裝 (適用於伺服器或自行託管的發行版)。



### 透過 Umbrel 進行安裝



Umbrel 將 ThunderHub 整合至其 **App Store**，使安裝變得極為簡單。不需要命令列或手動設定：一切都透過 Interface Umbrel 完成。只需遵循以下步驟即可：





- 開啟 Umbrel 面板：連線到您的 Umbrel 節點的 Interface 網路 (例如：本機網路上的 `http://umbrel.local` 或透過其 `.onion` Address (如果您使用 Tor))。
- 進入 App Store：在 Umbrel 的主功能表中，點選「App Store」（或「App」）。在可用應用程式清單中搜尋 **ThunderHub**。



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- 安裝 **ThunderHub**：按一下 ThunderHub 應用程式，然後按一下安裝按鈕。必要時請確認。Umbrel 會自動下載 ThunderHub 並部署到您的節點上。





- 啟動應用程式：安裝完成後（幾十秒鐘），**ThunderHub** 會出現在您的首頁。點擊圖示開啟。**ThunderHub** 會在您的瀏覽器中啟動。



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**重要：** ThunderHub 首次開啟時，會自動顯示登入所需的**預設密碼**。不再顯示 "選項可讓您隱藏此顯示，以便日後連線。 **我們強烈建議您：**




- 立即在密碼管理器中儲存此密碼
- 複製**，以便下一步使用**
- 儲存密碼後，勾選「不再顯示此」。



![Page de connexion de ThunderHub](assets/fr/03.webp)



接著您會被帶到登入頁面，您必須輸入上一步驟中複製的密碼才能解鎖 Interface。



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel 會在後台為 ThunderHub 提供 LND 連線資訊 (TLS 證書、管理 Macaroon 等)，因此您不需要做任何額外的設定。只需幾下點擊，您就可以在 Umbrel 節點上啟用 ThunderHub。



### 手動安裝 (自行託管，不包括 Umbrel)



對於 Umbrel 以外的使用者 (例如在個人伺服器上、使用 RaspiBlitz 的 Raspberry Pi 或*單機*安裝)，ThunderHub 的安裝需要一些額外的步驟。以下我們將根據 [ThunderHub 官方文件](https://docs.thunderhub.io) 描述如何從原始碼安裝與配置。



#### 安裝



**Prerequisites:** 請根據 [documentation setup](https://docs.thunderhub.io/setup) 確認您的系統符合最低需求：




- **Node.js** 版本 18 或更高
- 已安裝 **npm**
- 存取 LND 驗證檔案 ：
  - LND TLS 憑證 (`tls.cert`)
  - LND 管理 Macaroon (`admin.macaroon`)
  - LND gRPC 服務 Address (hostname:port) (本機預設為 `127.0.0.1:10009`)



**1.取回 ThunderHub 程式碼：** 按照 [安裝說明文件](https://docs.thunderhub.io/installation) 所述，克隆專案的 GitHub 儲存庫：



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. 安裝相依性並建立應用程式：**



```bash
npm install
npm run build
```



這些指令會安裝所有需要的模組，然後編譯應用程式（ThunderHub 是以 TypeScript/React 寫成）。



**3.稍後更新:** ThunderHub 提供多種日後更新的方法：



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### 組態 (設定)



**1.主要設定檔:** 在 ThunderHub 資料夾的根目錄建立一個`.env.local`檔來自訂設定 (這樣可以防止您的設定在更新時被覆蓋)。主要變數依照 [setup documentation](https://docs.thunderhub.io/setup)：



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2.伺服器帳號設定：** 建立在 `ACCOUNT_CONFIG_PATH` 中指定的 YAML 檔案：



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3.遠端存取：** 若要連線到遠端的 LND 節點，請在 `LND.conf` 中加入 ：



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4.安全性：** 首次啟動時，ThunderHub 會自動隱藏 YAML 檔案中的「masterPassword」和所有帳號密碼，以避免在伺服器上出現明碼密碼。



**5.啟動 ThunderHub：**



```bash
npm start
```



預設情況下，伺服器會在連接埠 3000 上監聽。存取 `http://localhost:3000` (或從本機網路存取 `http://ip-serveur:3000`)。



**6.Docker 替代方案：** ThunderHub 提供官方 Docker 映像：



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



出現 ThunderHub 登入頁面。選擇已設定的帳號，並輸入密碼以存取儀表板。



**在其他發行版上安裝：** 預先套件的節點發行版（RaspiBlitz、MyNode、Start9 等）通常會透過各自的管理介面提供原生 ThunderHub 支援。



**如需詳細資訊：** 請參閱完整的官方文件：




- 安裝：**[docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)**
- 設定：**[docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)**



這些資源詳細說明了 SSO 帳戶、加密 macaroons、TOR 設定等進階選項。



一旦 ThunderHub 安裝完成並可存取，您就可以使用其所有功能了。在下一節中，我們將介紹 Interface ThunderHub 及其各種選項卡，引導您使用。



## Interface 簡報



Interface ThunderHub 的結構圍繞一個主選單（通常顯示在左側欄中），由幾個關鍵部分組成。每個部分對應於管理您的 Lightning 節點的一個方面。讓我們逐一介紹：





- **Home** - 具有一般儀表板的 Home 標籤 (您節點的總覽和快速動作)。
- **儀表板** - 具備小工具和進階衡量指標的客製化儀表板。
- **Peers** - Lightning 對等管理 (與其他節點的連線)。
- **頻道** - 詳細管理 Lightning 頻道。
- **Rebalance** - 通路平衡工具 (循環付款)。
- **交易** - Lightning 付款記錄 (LN 交易)。
- **Forwards** - 路由統計 (由您的節點轉接的付款)。
- **Chain** - Node 的 On-Chain 投資組合 (On-Chain BTC: UTXOs, 交易)。
- **Amboss** - 與 Amboss 整合 (節點監控、備份等)。
- **Tools** - 雜項工具 (備份、簽署訊息、金剛圈、報告等)。
- **交換** - 透過 Boltz 進行 On-Chain/Lightning 交換功能。
- **Stats** - 進階統計資料和節點效能指標。



*(註：視 ThunderHub 版本而定，某些部分的標題或附加功能可能略有不同，但一般原則維持不變)*。



### 首頁 (一般控制面板)



ThunderHub 的 **Home** 標籤是您登入後出現的首頁。它包含**一般儀表板**，提供您 Lightning 節點狀態的**全局概觀**，並建議日常操作的**快速動作**。以下是您通常會發現的內容：



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- 餘額和容量：在頁面頂部，ThunderHub 會顯示您的可用餘額。在這裡，您通常會看到 On-Chain 結餘 (節點的 Wallet 中的 Bitcoin On-Chain，以 Anchor ⚓ 表示) 和 Lightning 結餘 (您的頻道容量，以閃電 Bolt ⚡ 表示)。這可讓您立即瞭解您在 On-Chain 和 Lightning 中的資金。如果您有多個帳號或頻道，請確定您的帳號或頻道是正確的 (例如 Mainnet vs Testnet)。





- 關鍵統計資料：**該儀表板可以顯示節點的一些全局指標 - 例如，開放通道的數量、連線對等體的數量、賺取的路由費（如果適用）等。這是節點最近活動和健康狀況的摘要。**





- 快速動作：**面板上的按鈕可快速執行最常見的工作，而無需透過功能表來瀏覽。這些快速動作包括：**





- **鬼**：透過 Amboss 設定自訂 Lightning Address。
- 捐款：透過 Lightning 捐款。
- 登入/前往**Amboss**：連線至您的 Amboss 帳戶 (Quick Connect) 並直接前往 Amboss.space 檢視您的節點資訊。
- **Address**：輸入 Lightning Address 進行付款。
- 開啟：開啟一個新的 Lightning 通道。點擊會開啟一個表單，輸入要開啟通道的遠端節點 URI、金額以及（如適用）要使用的最高 On-Chain 費用。
- 解碼：解碼 Lightning Invoice 或 LNURL，以便在付款前檢視詳細資訊。
- **LNURL**：處理 Lightning 付款或提款的 LNURL。
- 登入 **LnMarkets**：登入 LnMarkets 進行交易。



這些快速動作可讓您直接從首頁執行最常見的操作，而無需瀏覽 Interface 的各個選項卡。



簡而言之，ThunderHub 面板可讓您快速檢視您的節點，並可讓您執行最常見的操作 (傳送/接收、開啟頻道)，只要按一下即可。這是日常管理的理想起點。



### 儀表板



儀表板」區段與「主選項卡」分開，提供更進階、可自訂的儀表板。此區段允許您根據節點操作員的需求，使用特定小工具建立自訂檢視。





- 可自訂 Widget：**與有固定版面的首頁不同，儀表板可讓您精確選擇要顯示的 Elements 以及組織方式。**



![Dashboard sans widgets activés](assets/fr/06.webp)



如果沒有啟用任何 Widget，您會看到「沒有啟用 Widget！」訊息，並附有「設定」按鈕以存取自訂參數。



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



在設定中，您可以選擇各種分類的 widget："Lightning - Info」、「Lightning - Table」、「Lightning - Graph」等。每個 Widget 都可以用「顯示/隱藏」按鈕個別啟動或關閉。



![Bas de la page des paramètres](assets/fr/08.webp)



在設定的底部，您會發現「至儀表板」按鈕可返回儀表板，而「重設小工具」按鈕則可重設預設顯示。



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



配置完成後，您的儀表板可以顯示各種圖表和指標：閃電付款圖表、發出的發票數量、前進統計、明細餘額等。





- 進階指標：**使用圖表和即時資料，取得節點效能的更詳細統計資料。**





- 可設定的總覽：**無論您是隨意使用的使用者，或是管理多個路由通道的專業操作員，都可以調整顯示內容。**





- 模組化 Interface：**根據需要新增或移除小工具：前進圖表、流動性指標、節點健康警示等。**



此部分對於希望監控特定指標或獲得其Lightning節點的更多技術概述的高級用戶特別有用。它與 「主頁 」部分相輔相成，為資訊的顯示方式提供了更大的靈活性和控制權。



### 同儕



Peers** 區段列出目前與您連線的所有 Lightning 節點，並將其視為 Peers。一個 ** 對等體是 Lightning Network 上直接的節點對節點連線。即使沒有開放的通道，您的節點也可以與對等節點連線（例如，只是連線到 Exchange 網路上的八卦資訊），當然每個開放的通道都會自動暗示連線的對等節點。



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



在 Peers 標籤中，您會看到 ：





- 資訊列：**Interface 會顯示有用的詳細資訊，例如同步狀態、連線類型 (clearnet 或 Tor)、ping、接收/傳送的 Satoshis 和交換的資料量。**
- 新增對等點：**ThunderHub 讓你透過右上角的「新增」按鈕，手動連線到一個新的對等點。你需要輸入節點的 URI (格式為 `<public_key>@<socket>`)。一經驗證，ThunderHub 就會傳送相對應的 `lncli connect` 指令。如果節點是線上且可存取的，它就會被加入您的對等者清單。**



### 頻道



**渠道**標籤是Lightning渠道管理的核心。它可能是您最常使用的部分。它展示了**您所有的Lightning通道**及其詳細資訊，並允許您對這些通道執行管理動作。



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



以下是頻道頁面的內容：





- 頻道清單檢視：每個開放 (或開啟/關閉) 的頻道都會列出來，通常有遠端節點的別名、頻道總容量，以及說明本地與遠端流動性分佈的彩色條。ThunderHub 使用顏色代碼（通常是藍色/Green）或百分比來表示通道平衡：例如，藍色代表您的本地份額，Green 代表遠端份額。如果通道完全平衡 (50/50)，顏色條會是每種顏色的一半。這可讓您一眼就看出哪些頻道不平衡 (全部藍色 = 幾乎全部近端，全部 Green = 幾乎全部遠端)。





- 資訊欄位：**Interface 顯示詳細欄位，包括狀態、可用動作、對等資訊、頻道 ID、容量、活動、費用和餘額，並以圖形顯示流動性。**





- 顯示設定：**右上角的齒輪可讓您自訂頻道顯示，以符合您的喜好。**





- 狀態：**您也會看到狀態指示器** - 例如：`Active` (頻道已開啟並可正常運作)、`Offline` (對等體已斷線，因此頻道暫時無法使用)、`Pending` (開啟或關閉等待 On-Chain 確認)。





- 頻道上的動作：**ThunderHub 為每個頻道提供動作按鈕 (通常是圖示形式)**：



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- 編輯費用：**Interface 「更新頻道政策」可讓您調整所有頻道參數：基本費用、費率 (以 ppm 為單位)、CLTV Delta、最大 HTLC 和最小 HTLC。這可讓您針對每個通道個別調整收費政策，以達到吸引（或抑制）路由流量的目的。** *(注意：ThunderHub 不能替代自動費用管理工具，但對於手動調整非常有效)*。
- 關閉通道 (*Close*)：Interface "Close Channel"（關閉通道）讓您透過定義費用（Sats/vByte），選擇**合作關閉**（默認）或**強制關閉**（*Force Close*）。**重要：**在可能的情況下，總是選擇合作關閉，以避免 On-Chain 結算延遲和更高的費用。ThunderHub 會告訴您對等方是否在線上（合作可能）。在強制平倉的情況下，請務必確認，因為這是不可逆轉的，並會觸發具有時間鎖（在 Bitcoin Mainnet 上一般為 144 個區塊或 ~1 天）的掃描交易。
- 開啟新頻道：**若要開啟新頻道，請按一下頻道頁面右上的齒輪，然後選擇「開啟」。然後您就可以啟動一個頻道到新的或現有的對等人。使用此頁面的好處是您可以看到現有頻道的清單，這可以幫助您決定在哪裡開啟新頻道。**



簡而言之，「頻道」部分可讓您**精細控制每個頻道**。在這裡您可以推動流動性分配、決定保留或關閉哪些頻道，以及設定每個頻道的路由參數。ThunderHub 為這些關鍵的節點管理操作提供了一個清晰的 Interface。



### 重新平衡



重新平衡**頁籤專門用於通道平衡**。平衡 (或 *rebalancing*) 是指重新調整您的流出和流入通道之間的資金分佈，方法是透過 Lightning Network 從您的一個通道向另一個通道進行**循環付款**。這可讓您在不引入新資金的情況下，將流動資金從太滿的頻道轉移到太空的頻道，使您的頻道更有用（一個平衡的頻道可以同時發送和接收付款）。



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub 為這項操作提供了極大的便利，否則在命令列上執行這項操作會很繁瑣。以下是如何使用 Rebalance 部分：





- 初始頻道檢視：在進入 Rebalance 時，ThunderHub 會顯示您的頻道清單，每個頻道都有一個平衡指標（類似於頻道頁面的指標）。你可以馬上看到哪些頻道失去平衡。ThunderHub 可以將頻道依平衡度增加的順序排序，因此最不平衡的頻道會排在清單的最上方 (0.0 表示完全在本機或遠端)。





- 對等體選擇：**Interface 可輕鬆選擇出站和入站對等體進行再平衡。**





- 參數設定：**您可以設定**：
  - 您願意支付的**最高費用**（以 Sats 和 ppm 為單位
  - 使用「固定」或「目標」選項重新平衡**的**金額
- 路由時應避免的節點
- 尋找路線的最長試驗時間





- 選擇**來源通道**：首先選擇**出站（來源）**通道，即您有太多本地流動資金需要移動的通道。實際上，這是一個您的本地佔有率很高 (> 50%) 的渠道。讓我們想像一個有 1,000,000 個 Sats 的 A 頻道，其中 900,000 個是當地的，這是一個將 Sats 傳送到其他地方的好選擇。點選這個 A 頻道為 「外送」，ThunderHub 就會將它標示為來源。





- 選擇**目標通道**：接下來，選擇需要接收流動資金的**進入（目標）**通道。通常，這將是一個反其道而行的渠道 - 大部分資金都在遠方（例如，100萬中只有10萬本地Satss）。ThunderHub 在選定來源頻道後，會將其他頻道以相反順序排序 (餘額遞減)，以協助找出最具互補性的頻道。選擇一個本端有空位的 B 頻道。ThunderHub 接著會清楚顯示哪兩個頻道已被選中 (來源 A 與目標 B)。





- 設定費用金額和公差：**表格可讓您輸入**：





- 要重新平衡的**數量（以 Sats 為單位）**。通常，我們會選擇一個相等於在 \~50/50 時平衡兩個通道的數量。例如，ThunderHub 可以預先填滿來源通道一半的過剩容量。
  - 您願意付給此操作的**最高費用**（選項）。此費用以 Sats 表示（循環路由的總費用）。如果留空，ThunderHub 將會不計成本地尋找路徑，這通常是不可取的（設定一個限制會比較好，例如 10 Sats 來做一個小的再平衡，或是設定一個最大的 ppm）。





- 尋找路由：點擊按鈕尋找路由。ThunderHub 會查詢 LND，計算從您的來源頻道經由網路到您自己的目標頻道的路徑。如果它找到符合您的費用標準的可能路徑，它會顯示該路徑的跳數和費用的詳細資訊。例如，它可能會顯示它找到了一個 3 跳的路徑，總共需要 2 個 Sats 的費用。





- 開始重新平衡：如果您滿意建議的路徑，請點選**平衡通道**。ThunderHub 將透過 LND 啟動循環付款。如果付款成功，您會看到成功通知，通道 A 和通道 B 的餘額會即時修改。ThunderHub 會更新這些頻道的餘額指示器 (理想情況下，它們會比之前更綠色，表示餘額更好)。





- 調整和迭代：**如果第一次嘗試沒有找到路由（或路由太貴），您可以調整參數**：





  - 嘗試較小的金額（有時部分重新平衡會成功，而大量重新平衡則會失敗）。
  - 逐步增加最高費用，但要小心不要支付超過價值的費用。
  - 使用 **Get Another Route** 按鈕（如果有）嘗試其他路徑。
  - 如果事情真的很棘手，可以試試另一對通道。



ThunderHub 讓這個過程變得非常**直觀和形象**。只需 4 個步驟（選擇傳出通道、選擇傳入通道、金額、驗證），您就可以完成以往需要複雜手動指令才能完成的工作。此工具對於維持一個平衡的節點、改善您的路由效能和體驗 (更容易在您所有的管道上傳送和接收付款) 是非常有價值的。



最後，請注意重新平衡會消耗路由成本 (付費給中間節點)，因此這是讓您的節點更具流動性的**投資。明智地使用它，例如支持您經常使用的服務通道（入站流動性）或平衡大型路由通道。ThunderHub 可讓您**簡單、有效率地做到這一點。



### 交易



ThunderHub 中的**Transactions**部分對應您節點的**Lightning**交易歷史，即透過通道支付或收到的付款和發票。這是您 LN 作業的一種帳目報表。



![Historique des transactions Lightning](assets/fr/14.webp)



在此標籤中，您可以找到 ：





- Invoice 圖表：**在右上角，圖表顯示收到的發票隨時間的演變，讓您直觀了解節點的活動。**





- 按時間順序列出所有來自*或*至*您節點的 Lightning 交易。每個項目可以顯示 ：





  - 操作類型： **sent payment** (outgoing payment) 或 **received payment** (inbound, via a paid Invoice)。
  - Sats 中的金額。
  - 日期/時間。
  - 付款 ID (Hash 或 RHash 預設影像) 或註解 (如果您在 Invoice 中加入備註)。
  - 狀態： **已完成**，或可能是**進行中**/*失敗*（例如，等待解決的付款，但一般 LND 會快速處理，因此與 On-Chain 交易相比，這裡很少有「待決」）。



簡而言之，交易部分是您的**LN 活動日誌**。它對於檢查付款是否已經完成、費用是多少，或者追蹤您的 Lightning 交換歷史非常有用。結合 Forwards 區段 (接下來會說明)，您就可以完整地檢視通過您節點的資金。



### 前鋒



**Forwards**選項卡專門顯示您節點的**路由**活動，即透過您的通道（當您作為 Lightning Network 上的中介節點時）**轉移**的付款。如果您將您的節點當成路由節點來運作，這是追蹤您績效的重要部分。



![Statistiques de routage Lightning](assets/fr/15.webp)



在 Forwards 中，ThunderHub 呈現 ：





- 篩選器和顯示選項：**在右上方，篩選器可讓您依日/週/月/年對資料排序，並選擇圖形或表格顯示。**





- 活動訊息：**如果在選取的期間內沒有執行路由，Interface 會顯示「No forwards for this period（此期間沒有轉寄）」，如本範例所示。**





- 最近轉寄的**表：每個條目對應已經透過您的節點**轉寄**的付款。對於每筆轉帳，我們通常會看到 ：





  - Timestamp、
  - 路由的數量（以 Sats 為單位）、
- 在這次轉寄中所賺取的**費用**（在 Sats 中，這是您在傳入頻道中收到的費用和在傳出頻道中發送的費用之間的差額）、
  - 使用的傳入和傳出頻道 (通常以對等別名或頻道 ID 來識別)。
  - 狀態 (通常為 * 已完成*，若轉送途中失敗則為失敗)。





- 綜合統計：ThunderHub 會計算並在頁面頂端顯示特定時段（例如過去 24 小時或 7 天等，有時可設定）內的總計和統計資料。



簡而言之，Forwards部分提供了Lightning節點路由活動的**即時概覽**。加上通道和再平衡部分，這就形成了優化節點的完整套件：Channels/Rebalance 用於流動性，Forwards 用於觀察結果（流量和利潤）。



### 鏈條



** Chain** 區段對應您 LND 節點的 Bitcoin On-Chain 投資組合管理。此 Interface 可讓您檢視並管理 Bitcoin 資金，這些資金用於開啟通道或從關閉的通道接收資金。



![Gestion du portefeuille on-chain](assets/fr/16.webp)



在 Chain 中，您會發現 ：





- **Balance On-Chain:** 顯示 Wallet LND 中可用的 BTC 總餘額。





- UTXO 列表：**檢視所有未使用的輸出 (UTXO)，包括每項輸出的金額、確認、Address 和格式。**





- 交易記錄：**所有 Bitcoin 交易的詳細表格，包含類型 (輸入/輸出)、日期、金額、費用、確認、包含區塊、地址和 txid。**



### Amboss



ThunderHub 與 **Amboss** 平台 (amboss.space) 整合，提供 Lightning 節點的詳細資訊、流通量市場，以及加密通道備份和可用性監控等實用功能。



![Intégration Amboss avec ses options](assets/fr/17.webp)



在 ThunderHub 中，Amboss 區塊允許您將您的節點**連結到您的 Amboss 帳戶**：





- Ghost Address：**為您的節點設定一個個人化的 Lightning Address**，方便接收付款。





- 自動頻道備份：** Amboss 上加密頻道備份** (SCB 檔案) 的旗艦功能。在設定中啟動 **Amboss Auto Backup = Yes**，在您每次變更頻道時自動傳送加密備份更新。當發生故障時，有了這個外部備份，您就可以恢復您的資金。





- 健康檢查：**啟動 Amboss Healthcheck = Yes** 來讓您的節點定期傳送 pings 到 Amboss。如果您的節點似乎離線，您會收到警示。





- 其他功能：**自動推送餘額、Magma/Hydro 整合 (流通量市場)，以及存取詳細的效能統計。**



Amboss 整合增加了一個重要的**安全 Layer**，具有自動外部備份和可用性監控功能，可直接從 ThunderHub 存取。



### 工具



**Tools** 區段匯集了各種用於管理節點的進階工具。以下是主要的 Elements：



![Interface des outils disponibles](assets/fr/18.webp)





- 備份：**手動管理頻道備份 (SCB)。ThunderHub 讓您下載您頻道的完整備份檔案** (選項 「備份所有頻道 -> 下載」)。將這個 `channel-all.bak` 檔案保存在安全的地方 - 它對於在當機時恢復您的資金非常重要。您也可以在重新部署節點時**匯入**備份檔案。





- 會計：**財務報告的匯出工具，包括特定期間內所賺取/支付的費用和傳送的數量。**
- 簽名訊息：**與您的節點簽名或驗證訊息**，以透過加密簽名證明您的 Lightning 節點的 Ownership。
- 馬卡龍（麵包坊部分）：**管理 LND 馬卡龍，建立自訂存取權限**。Interface 「麵包坊」可讓您精確選擇每項權限：「新增或移除 Peers」、「建立連鎖地址」、「建立發票」、「建立 Macaroons」、「衍生金鑰」、「取得存取金鑰」、「取得連鎖交易」、「取得發票」、「取得 Wallet 資訊」、「取得付款」、「取得對等人」、「支付發票」、「撤銷存取碼」、「傳送至連鎖位址」、「簽署位元組」、「簽署訊息」、「停止 daemon」、「驗證位元組簽章」、「驗證訊息 」等。每個權限都可以用「是/否」按鈕個別啟動，以建立量身打造的金剛圈。
- 系統資訊：**顯示 Wallet 版本和啟用的 RPC。**



簡而言之，「工具」區塊將進階管理功能 - 備份、會計、安全性和存取管理 - 整合在統一的 Interface 中。



### 交換



ThunderHub 的 **Swap** 標籤可讓您透過 Boltz 服務將 Lightning Satoshis 交換至 Bitcoin On-Chain。此功能對於在不關閉頻道的情況下「傾倒」過剩的 Lightning 流動資金到頻道非常有用。



![Interface de swap via Boltz](assets/fr/19.webp)



過程很簡單：





- 金額：定義要交換的金額
- **Address** ：輸入 Bitcoin 接收 Address
- 執行：ThunderHub 與 Boltz 通訊，自動處理 Exchange



**福利：**




- 非保管服務（無現金保管）
- 保留您現有的通路
- 易於使用的整合式 Interface



Boltz 會收取少量佣金，您則支付標準的 Bitcoin 交易費用。ThunderHub 會在確認前顯示所有費用。



### 統計資料



ThunderHub的**Stats**部分提供Lightning節點的**進階統計**，以分析效能並最佳化路由。



![Statistiques du nœud via Amboss](assets/fr/20.webp)



本節對於優化您的成本、識別成功的通路以及規劃擴展您的節點是非常重要的。



## 總結



**ThunderHub** 已經成為簡易管理 Lightning **LND** 節點的基本工具。這款現代化的 Interface 提供所有基本功能：通道管理、付款、監控，以及自動再平衡和 Amboss 整合等進階功能。



**主要福利：**




- Interface 時尚直覺
- 強大的工具（重新平衡、Boltz 交換、自動備份）
- 相容於 Umbrel、Voltage、RaspiBlitz 及其他發行版本



ThunderHub 將先進的 Lightning 節點管理平民化，讓以往需要複雜技術指令的操作變得容易上手。無論您是新手還是經驗豐富的操作員，ThunderHub 都能讓您透過現代化、全面的 Interface 高效管理您的 Lightning 節點。



## 資源



** 官方連結：**




- 官方網站：**[thunderhub.io](https://thunderhub.io)**
- 說明文件：**[docs.thunderhub.io](https://docs.thunderhub.io)**
- GitHub 原始碼：**[github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)**