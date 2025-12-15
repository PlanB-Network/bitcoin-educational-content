---
name: Joinstr
description: 透過主權 Bitcoin 保密的 Nostr 網路進行分散式 CoinJoins
---

![cover](assets/cover.webp)



Bitcoin 區塊鏈的透明度使得追蹤交易歷史成為可能。CoinJoins 透過混合多個同時進行的交易，打破了這些連結，恢復了可媲美現金的保密性。



然而，傳統解決方案依賴中央協調器作為單點故障。在監管壓力下，Wasabi 和 Samourai 於 2024 年停止營運。



**Joinstr** 透過使用分散式 Nostr 網路進行協調，消除了這個弱點。此開放源碼應用程式可實現真正的主權 CoinJoins，任何中央機構都無法審查、監控或中斷服務。



## Joinstr 是什麼？



Joinstr 是一個開放原始碼工具，利用 Nostr 協定作為協調基礎架構，徹底改變了 CoinJoins 的方法。與需要專用伺服器的集中式解決方案不同，Joinstr 仰賴分散式的 Nostr 中繼網路，讓參與者能直接在對等者之間進行協調。



**Decentralized 架構** ：Nostr 網路取代了中央協調器。參與者透過 Nostr 中繼器張貼加密公告，建立或加入「池」。這些資訊（金額、參與者、地址）對中繼者來說仍然是不可理解的，確保沒有中央實體可以監控、審查或過濾 CoinJoins。



**SIGHASH_ALL|ANYONECANPAY 機制**：Joinstr 利用這個 Bitcoin 簽署旗號，允許每個參與者只簽署他或她的輸入，同時驗證所有輸出。每個使用者在本地產生他或她的 PSBT，然後透過 Nostr 散發。每個使用者在本地產生他的 PSBT，簽署後透過 Nostr 散發。您的 bitcoins 在最後簽章前一直由您專屬控制。



**哲學**：Joinstr 遵循 Bitcoin cypherpunk 的精神，以三個目標為目標： **抵抗審查** (任何機關都無法停止服務)、**完全不囚禁** (您可以保留您的私人密碼鑰匙)、**平等對待** (任何 UTXO 都不會受到歧視)。



### 主要功能



**Flexible pools**：與固定面額不同，任何使用者都可以依據所需的精確金額和目標參與者人數建立彩池，優化 UTXO 的使用，而無需人為分割。



**透明收費**：沒有協調費。只有 Bitcoin 交易費用由參與者均分（每人幾千 Satoshis）。



**Ephemerality**：不保留使用者資料。資訊透過加密的短暫 Nostr 訊息傳輸，交易後立即遺忘。



### 可用平台



本教學著重於**Android 應用程式**，這是目前唯一穩定且值得推薦的解決方案。Electrum 外掛程式已經存在，但因相容性問題而不穩定。網頁介面正在開發中。



## Bitcoin 核心配置



Joinstr Android 需要透過 RPC 連線至 Bitcoin 節點。您必須先在電腦上設定 Bitcoin Core 以接受來自手機的連線。



**Note**：有關 Bitcoin Core 完整設定的詳細資訊，請參閱我們的專用教學 ：



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### 網路需求



#### 找出您的本機 IP 位址



您的 Android 手機必須能夠在區域網路中連接到您的 Bitcoin 節點。找出您電腦的 IP 位址：



**在 macOS 上** ：



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



簡單的替代方案：



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**在 Linux 上** ：



```bash
hostname -I | awk '{print $1}'
```



**在 Windows 上** ：



```cmd
ipconfig
```



尋找 IPv4 位址 (格式為 `192.168.x.x` 或 `10.0.x.x`)



### RPC 配置



#### 編輯 bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



找到您的 `bitcoin.conf` 檔案：




- Linux**：`~/.bitcoin/bitcoin.conf
- macOS**：`~/Library/Application Support/Bitcoin/bitcoin.conf
- 視窗**：`%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



使用您喜愛的文字編輯器開啟檔案，並加入此設定以啟用 RPC 伺服器。



**入門建議設定 (書籤)** ：



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet** 配置（生產使用） ：



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Important** ：




- 強烈建議**使用 Signet 進行首次測試：應用程式仍在開發中 (測試版)，可能仍存在錯誤。Signet 可讓您免費測試，無需冒實際資金的風險。
- 將 `192.168.1.0/24` 改為您的網路子網路 (例如，如果您的 IP 是 `192.168.68.57`，請使用 `192.168.68.0/24`)。



**Security**：產生強大的密碼 ：



```bash
openssl rand -base64 32
```



### 初始化



#### 重新啟動並檢查



1.完全關閉 Bitcoin Core


2.重新啟動以套用組態




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



當 Bitcoin Core 首次啟動時，它會下載並同時處理書籤區塊鏈。此操作比 mainnet 快得多（只需幾分鐘）。請等待同步化完成後再繼續。



![CRÉATION DE WALLET](assets/fr/04.webp)



同步化後，按一下「建立新的 wallet」，建立新的投資組合。給它一個明確的名稱，如 `tuto_joinstr_signet`。



![WALLET CRÉÉ](assets/fr/05.webp)



您的 wallet 現已建立，並已準備好接收書籤比特幣進行測試。



#### 取得書籤上的 bitcoins (測試)



要在書籤上測試 Joinstr，您需要免費測試 bitcoins ：



![SIGNET FAUCET](assets/fr/06.webp)



使用公共書籤，例如 ：




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



在 Bitcoin Core 中，generate 新建一個接收地址（「接收 」標籤），複製它並貼到龍頭表單中。如有必要，請解決驗證碼。您會在幾秒鐘內收到免費的書籤比特幣。



## Android 應用程式



### 安裝



![APPLICATION ANDROID](assets/fr/07.webp)



前往 [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) 下載最新的 APK 版本。在您的 Android 瀏覽器上，下載檔案，然後開啟檔案啟動安裝。如有必要，您需要在手機的安全設置中允許來自未知來源的安裝。



### 應用程式配置



![PERMISSIONS VPN](assets/fr/08.webp)



在第一次啟動時，Joinstr 應用程式會要求控制內建 VPN 的權限。接受這兩個權限要求：OpenVPN 控制和 VPN 連線。這些權限是 VPN 整合所必需的，可以保護您的網路隱私。



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr 應用程式分為三個主要標籤：




- 首頁**：主畫面
- Pools**：建立和管理 CoinJoin 池
- 設定**：應用程式設定



![CONFIGURATION SETTINGS](assets/fr/13.webp)



在「設定」標籤中設定：



**1.Nostr Relay**：池協調的 Nostr 中繼位址




- 範例： `wss://relay.damus.io`
- 其他推薦的中繼站： `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **重要**：所有參與者必須使用 ** 相同的 Nostr 中繼**，才能看到並加入相同的池。如果您使用不同的中繼，您將無法看到在其他中繼上建立的資料池。



**2.節點 URL**：您的 Bitcoin 節點的 IP 位址（不含連接埠）




- 格式：`http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3.RPC 使用者名稱** ：在 bitcoin.conf 上的 `rpcuser=` 中設定的使用者名稱




- 範例： `satoshi



**4.RPC 密碼** ：在 bitcoin.conf 上的 `rpcpassword=` 中設定的密碼



**5.RPC 連接埠** ：RPC 連接埠，視網路而定




- Mainnet** ：`8332`
- 書籤**：`38332`



**6.Wallet**：選擇包含要混合的 UTXO 的 Bitcoin 核心組合




- 範例: `tutoo_joinstr_signet`



**7.VPN Gateway**：選擇 Riseup VPN 伺服器




- 範例： `(Paris) vpn07-par.riseup.net`
- 其他可用：阿姆斯特丹、西雅圖等。
- ⚠️ **重要**：同組的所有參加者必須使用 ** 相同的 VPN 閘道** 參加 CoinJoin。在混合回合中，所有參加者必須以相同的出口 IP 位址出現，以防止網路分析將參加者關聯起來。



Joinstr 應用程式**整合 Riseup VPN，簡化參與者之間的協調。



**Important** ：




- 確保您的手機和電腦位於相同的本機 WiFi 網路上
- 參與匯集時，VPN 連線會自動啟動
- 設定所有參數後，按一下 **「儲存」**。



## 實際使用



### 建立或加入資料庫



![CRÉATION POOL ANDROID](assets/fr/10.webp)



參加 CoinJoin 有兩種選擇：



**選項 1：建立新池**



點擊 "Pools 「標籤中的 」Create New Pool"。指定 BTC 的面額（例如 0.002 BTC）和所需的參與者人數（最少 2 人，建議 3-5 人以提高匿名性）。然後，應用程式會等待其他使用者加入您的池。一旦達到所需數量，輸出註冊過程將自動開始，您需要選擇您的 UTXO 進行混合，然後點擊 「註冊」。



**⏱️ Important**：池在**10 分鐘**無活動後失效。如果未達到所需的參加人數，資源池將自動關閉。



**選項二：加入現有的游泳池**



在「檢視其他匯集」標籤中，瀏覽其他使用者建立的可用匯集。選擇與您的金額相對應的資料池並加入。確保您已設定與其他參與者相同的 Nostr relay 和 VPN Gateway（請參閱「設定」一節）。



**UTXO 選擇規則**：您的 UTXO 必須略高於彩池面額（sats 盈餘在 +500 到 +5000 之間）。



**範例**：對於 0.002 BTC (200,000 sats) 的池，使用介於 200,500 和 205,000 sats 之間的 UTXO。



![PROCESSUS COINJOIN](assets/fr/11.webp)



此過程會自動**：您的輸入一經註冊，應用程式就會等待所有參與者註冊他們的輸入。一旦所有輸入都完成註冊，PSBT 即會建立，並自動以您的金鑰簽名，然後與其他參與者的簽名結合。最後，完整的交易會在 Bitcoin 網路上廣播。廣播完成後，您會收到 TXID (交易識別碼)。在 Android 上不需要手動操作 PSBT。



### on-chain 驗證



![TRANSACTION MEMPOOL](assets/fr/12.webp)



一旦交易被廣播，您將收到 TXID (交易識別碼)。在 [mempool.space](https://mempool.space) 或您喜愛的瀏覽器上檢視。若要在書籤上測試，請使用 [mempool.space/signet](https://mempool.space/signet)。



您可以觀察：





- N 個參賽**：每位參賽者一份（在我們的例子中，2 份參賽作品）
- N 個相同的輸出**：面額的確實金額（在此，2 個輸出，每個 0.00199800 BTC）
- 流程圖**：mempool.space 可視化顯示輸入和輸出的組合
- 特點** ：交易可識別為 SegWit、Taproot、RBF 等。



由於所有主要輸出的數量相同，因此**不可能判斷出哪一個屬於誰。這就是 CoinJoin 的基本原則：輸出的無區別性。



**Exemple de transaction signet** ：[404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**請注意**：如果您的 UTXO 大於匯池面額，您將有外匯輸出（盈餘）。這些外匯 UTXO 仍可追蹤，且必須與您的匿名輸出分開管理。切勿將其與您的混合輸出結合。



## CoinJoin 品質與匿名套件



CoinJoin 的效率以其 **anonset** 來衡量：交易產生的相同價值的輸出數量。這個數字越高，就越難確定哪個輸入對應哪個輸出。



Joinstr 目前平均產生 2 到 5 個**參與者。這些數字低於傳統的集中式協調者，例如 Wasabi (50-100 參與者) 或 Whirlpool (5-10 參與者)，但這就是分散化的代價。



💡 **要詳細瞭解匿名集及其計算**，請參閱我們的完整課程：[匿名集](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431)。



### Joinstr vs. 其他 CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **其他活性 CoinJoin 溶液** ：




- Ashigaru**：Whirlpool 通訊協定的開放原始碼實作，具有中央協調器，但可以分散方式部署。在 2024 年奪取 Samourai Wallet 後繼續運作。
- JoinMarket**：分散式 P2P 解決方案，無中央協調員，以製造商/承購商商業模式為基礎，由「製造商」提供流動性，並由「承購商」支付報酬。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**基本的權衡**：Joinstr 與 JoinMarket 是唯一兩個沒有中央協調者的解決方案。JoinMarket 使用 P2P 的商業模式與財務獎勵，而 Joinstr 則使用 Nostr 進行無成本的協調。Joinstr 犧牲了立即的大規模匿名性，以換取簡單性 (沒有製造者/接受者管理) 及完全沒有協調費用。



**實用建議**：為了補償較小的池，請使用不同的參賽者連續進行幾輪 CoinJoin。拉開每輪比賽的距離，並在每輪比賽之間更換 Nostr 接力，以盡量提高保密性。



請隨時參考我們完整的 bitcoin 隱私權課程，以獲得更多關於此主題的資訊：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 優點與限制



### 重點介紹



**加強隱私**：結合 Nostr 通訊加密、與會者之間共用 VPN，以及建議使用 Tor，可建立難以繞過的多層保護。



**透明、成本最低**：沒有協調成本，只有 mining 成本由參與者公平分擔。任何營運商都不徵收百分比。



### 需要考慮的限制條件





- 可變的流動性**：較小的池，可以等待參與者聚集在一起
- 專案進行中**：應用程式處於測試階段，可能會有錯誤。先在書籤上少量測試
- Sybil 攻擊**：一個對手控制多個池參與者的可能性



## 最佳實踐



**UTXO 隔離**：切勿將混合的 UTXO 與未混合的 UTXO 合併。為您的匿名輸出使用獨立的組合。



** 多輪比賽必不可少**：與不同的參加者至少連續進行 3 輪。改變數量和時間以避免模式化。每輪相隔數小時。



**網路保護**：除了內建的 VPN 外，有系統地使用 Tor。為每個重要會話產生短暫的 Nostr 金鑰。



**謹慎進度**：從少量開始加入書籤。



## 總結



Joinstr 代表真正分散式的 Bitcoin 隱私權解決方案。透過使用 Nostr 進行協調，它消除了對中央協調員的依賴，同時保留使用者的主權。



** 適用於重視抵抗審查，並準備執行數輪 CoinJoin 以補償較小池的使用者。



在金融審查日益嚴格的背景下，保護隱私權的分散式工具變得非常重要。



## 資源



### 官方文件




- [Joinstr官方網站](https://joinstr.xyz)
- [使用者文件](https://docs.joinstr.xyz/users/using-joinstr)
- [技術文件](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab 原始碼](https://gitlab.com/invincible-privacy/joinstr)
- [Android 應用程式](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### 教學




- [Electrum 外掛程式教學](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - 完整指南 by Uncensored Tech



### 社群與支援




- [Telegram Joinstr Group](https://t.me/joinstr) - 社區支援與書籤角
- [DelvingBitcoin的技術討論](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### 其他工具




- [Bookmark Faucet](https://signetfaucet.com) - 免費測試比特幣
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet 替代品
- [Mempool.space](https://mempool.space) - 含隱私分析的 Block explorer
