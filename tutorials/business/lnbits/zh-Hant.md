---
name: LNbits

description: 商家會計平台
---

![presentation](assets/lnbits-intro.webp)

# 會計系統


LNbits 內含許多工具，可控制和疏導您的進出資金、連結您的網路商店，甚至是您自己建立的 Hardware Wallet 或 ATM 等裝置。使用者類型包括


- Wallet 擁有者希望將 LNbits 當作 Interface 使用，以管理其資金及其額外功能。
- 想要接受 Bitcoin onchain 和 Lightning Network 付款的線上和離線商家或服務供應商。
- 想要建立 Lightning Network 應用程式的開發人員。
- 希望將其節點與 LNbits 系統整合以進行會計的節點操作員。
- 所有這些都有不同的需求。我們以模組化的方式建立 LNbits，讓每位使用者都能以最適合您的方式使用我們的功能。


# Wallet 管理員


LNbits 是一個免費且開放原始碼的會計系統 - 不是節點管理器。通道管理是連接至 LNbits 作為資金來源的 Lightning 節點（如 LND 或 c-lightning）的領域。LNbits 系統中的 Superuser 或 Admin 用戶負責管理會計功能和內部擴展功能的整體可訪問性和配置。


LNbits 充當用戶與 Lightning 節點之間的 Interface，提供簡單易用的方式來管理支付網路並與之互動。


將 LNbits 想像成您的節點的「wordpress 模組化框架」。一個容易管理的平台，基於您可以結合許多使用個案的擴充套件。


將 LNbits 視為您自己的銀行財務管理軟體。您的節點提供付款管道，而 LNbits 擴展您的節點，讓您可以運行節點自帶的多個閃電 Wallet。這些錢包不一定要屬於您自己。假設您作為 LN 節點的運行者，已經有足夠的通道流動性和資金，現在您想為您的朋友、家人、自己的商店或其他普通商家提供一些 Bitcoin 銀行服務。


您將提供一個簡單的方法，讓他們在您的節點上開設一個 「銀行帳戶」，而無權存取您節點上的其他錢包和您節點上的所有流動資金，只能存取他們的部分。您的節點（銀行）僅作為他們付款（進/出）的傳輸提供者。


注意：您的 「客戶 」存入他們在您節點上的 LNbits 銀行帳戶的所有資金，將直接進入您節點的 LN 通道。這意味著您才是這些資金的真正擁有者。您對他們的資金有很大的責任。不要做惡，帶著資金逃跑，不要做惡，收取高昂的費用。我們要操那些法國銀行家，而不是操其他人（Bitcoin 使用者）。


# 示範平台


您可以在 [https://legend.lnbits.com](https://legend.lnbits.com)找到示範。其功能完整，可用來了解 LNbits 和 LNURL 的 Lightning Network 和一般功能。雖然我們無法阻止您使用它，但請您不要將它用於您的生產設定。我們不僅經常在伺服器上測試新功能，也鼓勵您以主權的方式運行自己的節點和 LNbits。如果您認為運行一個節點是太多的要求，你可以在雲端連接 LNbits 到保管人資金服務，如 Opennode、Luna 或 Votage，或到 Telegram 上的 Lightning Tipbot，僅舉幾個例子。


# LNbits 傳單


想要將一些基本資訊交給商戶或您的建築朋友嗎？我們很高興地宣布，我們的第一份傳單可供大家使用。傳單的大小是全球典型的傳單格式，共有 6 頁（2 摺），寬度為 3508，高度為 2480px。


商戶的 LNbits：[EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits for builders：[EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# 一些基本知識


LNbits 基於 LNURL 通訊協定運作，這表示請求有兩種形式：https:// clearnet 連結（不允許自簽證書）或 http:// v2/v3 onion 連結。若要提供 LNbits 服務，例如 LNURLp/w QR 碼或 NFC 卡，並可在野外使用，您需要將 LNbits 開放至 clearnet (https)。


在您安裝 LNbits 之前，請務必先閱讀並瞭解下列關於 LNbits 的一般指南，以及它為您帶來的可能性。



- [LND 指南](https://docs.lightning.engineering/) | 安裝 LND
- [LND 組態範例](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | LND 設定
- [CLN 指南](https://docs.corelightning.org/docs/installation) | 安裝 CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Run a Watchtower](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | 非常重要！


更多在特定使用情況下使用 LNbits 的詳細指南，請參閱此處：



- [Getting Started with LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack guide
- [ToDos for your safety with LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Lightning Network上的私人銀行](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | 分包指南
- [為您的親朋好友運行保管錢包](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [LNbits for a small restaurant / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [Using LNbits Streamer copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack guide
- [使用 LNbits 開啟您的 NOSTR 市場](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack 指南
- [將 LNbits 用於學校專案或節慶活動](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substack 指南



# 安裝 LNbits


## 基本安裝指南


LNbits 可以安裝在任何 Linux 作業系統的機器上。它不需要強大的機器或伺服器，只要有足夠的 RAM 記憶體和資料庫所需的磁碟空間即可。它可以與 BTC/LN 節點 (本機 PC 或遠端 VPS) 分開執行，也可以與節點一起安裝在同一台機器上，或已經安裝在 bundle 節點軟體機器上。


您可以選擇最常見的套件管理員，例如 poetry 和 nix。預設情況下，LNbits 會使用 SQLite 作為資料庫。您也可以使用 PostgreSQL，建議用於高負載的應用程式。[Here is a guide for basic installation using poetry or nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


對於新手，您可以找到更詳細的分步指南，讓您的 LNbits 在特定環境中運行：


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [LNbits on a VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) by Leo


您也可以在 [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) 找到影片。


[更多安裝方案在此](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server)。


對於 bundle 軟體節點，請參閱其有關 LNbits 的特定說明文件：[Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


當您對技術性的東西不感興趣，也不想自己主持您的資金來源或您的 lnbits 時，您可以使用 [LNbits SaaS 版本](https://saas.lnbits.com) (軟體即服務)。它基本上就像雲端中的 LNbits，但您可以自行定義資金來源 (例如您的節點、LNbits Wallet、LNtipbot、fakewallet 等) 和環境變數 - 其他雲端解決方案大多不具備這些功能。


[Here is a detailed guide how to use LNbits SaaS for specific use cases](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## 資金來源


LNbits 並非節點管理軟體，而是在 LND 或 CLN 資金來源之上，以 LN 為重點的會計系統。首次安裝之後，您可以到 http://localhost:5000/ 瀏覽您的 LNbits。


若要修改資金來源，請前往您的超級使用者URL，然後在「管理伺服器」中選擇資金來源，或編輯 .env 檔案，將 `LNBITS_BACKEND_WALLET_CLASS` 修改為您需要的來源，如果您在 `.env` 中設定了 `adminUI=TRUE`。


您可以在您的 lnbits/ 或 lnbits/apps/data 資料夾中找到 .env 檔案，方法是透過 `ls -a` 延伸指令，列出您目錄中的檔案。


您可能還需要安裝其他套件或執行其他設定步驟，選擇所需的資金來源。重新啟動後，您的新設定將會生效。


LNbits 可以使用哪些資金來源？


LNbits 可以運行在許多雷射網路資金來源之上。目前已支援 CoreLightning、LND、LNbits、LNPay、OpenNode，並會定期增加更多支援。

重要的是要選擇一個具有良好流動性和良好對等連接的來源。如果您將 LNbits 用於公共服務，您的用戶支付才能雙向暢通。


後端 Wallet（資金來源）可以使用下列 LNbits 環境變數在 `.env` 檔案中或在您的超級使用者帳號中的 Manage-Server 區段下進行設定。

如果您想使用 .env 版本，可以在這裡找到參數：



### CoreLightning


- CLN
  - lnbits_backend_wallet_class`： **CoreLightningWallet**
  - corelightning_rpc`：/file/path/lightning-RPC
- 火花 (c-lightning)
  - lnbits_backend_wallet_class`： **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - lnbits_backend_wallet_class`： **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `lnd_rest_cert`：/file/path/tls.cert
  - lnd_rest_macaroon`：/file/path/admin.macaroon 或 Bech64/Hex
  - LND_REST_MACAROON_ENCRYPTED`： eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - lnbits_backend_wallet_class`： **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - LND_GRPC_PORT`: 連接埠
  - `lnd_grpc_cert`：/file/path/tls.cert
  - lnd_grpc_macaroon`：/file/path/admin.macaroon 或 Bech64/Hex

您也可以使用 AES 加密的 macaroon (更多資訊) 來取代，方法是使用


  - LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

若要加密您的 macaroon，請執行 `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`。


### LNbits (另一個 LNbits 實例)



- 在雲端伺服器或您自己的家用伺服器上託管的 LNbits 實例
  - lnbits_backend_wallet_class`： **LNbitsWallet**
  - `lnbits_endpoint`: https://lnbits.mydomain.com
  - LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend 示範伺服器 (!! 請勿將此伺服器用於生產/商業用途，僅用於測試 !!!)
  - lnbits_backend_wallet_class`： **LNbitsWallet**
  - `lnbits_endpoint`: https://legend.lnbits.com
  - LNBITS_KEY: legend-lnbits-AdminKey

### 閃電提示機器人


要從 Telegram 連接您的 [Lightning Tipbot](https://t.me/LightningTipBot)，您需要設定以下參數：


  - lnbits_backend_wallet_class`： **LnTipsWallet**
  - `lnbits_endpoint`: https://LN.tips
  - LNBITS_KEY`：要取得 Key，您需要在 Telegram 上與 LightningTipbot 私聊一次，執行 /api。


也請參閱本教學如何安裝 [LNbits with LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### IBEX HUB


註冊 [這裡](https://ibexpay.ibexmercado.com/onboard)，然後從那裡取得您的金鑰/代號，端點是 https://ibexpay-api.ibexmercado.com。

更多資訊請參閱 [IBEX API-說明文件](https://ibexpay-api.readme.io/reference/getting-started-with-your-api)。


### LNPay

為了讓 Invoice 監聽器運作，您必須在您的 LNbits 設定一個公開存取的 URL，並設定一個 [LNPay webhook](https://dashboard.lnpay.co/webhook/)，指向 `<您的 LNbits 主機>/Wallet/webhook`，並設定 "Wallet Receive" 事件，且不給予任何秘密。設定 `https://mylnbits/Wallet/webhook` 將會是收到任何付款通知的端點 url。


  - lnbits_backend_wallet_class`： **LNPayWallet**
  - `lnpay_api_endpoint`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - LNPAY_WALLET_KEY`: waka_apiKey


### 開放式節點

要讓 Invoice 正常運作，您需要在 LNbits 中擁有可公開存取的 URL。webhook 設定是可選的。


  - lnbits_backend_wallet_class`： **OpenNodeWallet**
  - `opennode_api_endpoint`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby 是一個瀏覽器擴充套件，具有 LN Wallet 功能和 LNDHUB 帳戶，可作為 LNbits 的資金來源。[更多詳情請見此處](https://getalby.com/)。


您必須在 LNbits 中擁有可公開存取的 URL，才能使用 Invoice。不需要手動設定 webhook。您可以在這裡取得 generate Alby 存取代碼： https://getalby.com/developer/access_tokens/new



- `lnbits_backend_wallet_class`：AlbyWallet
- `alby_api_endpoint`: https://api.getalby.com/
- Alby_access_token`：AlbyAccessToken


## 其他 / 疑難排解指南


以下是一些額外的說明，以備不時之需。按一下箭頭以展開說明。


### Killswitch 🚨


最近不僅在整個領域，在 LNbits 中也出現了許多危險的 bug，因此我們決定採取一些措施。現在，當可能導致資金損失的漏洞或 bug 再次出现時，您可以選擇接收警告和/或直接採取行動。


![killswitchn](assets/lnbits-killswitch.webp)


如果切換到 void-Wallet，實例上的所有用戶類型都會看到一個黃色的橫幅，通常您會在主題/語言區域右側發現 "LNbits is in Beta "的通知 - 這是最明顯的提示，說明發生了什麼。看看您的新伺服器標籤，在視窗左邊以 Green 標示。


如何運作？啟用 killswitch 後，LNbits 核心團隊會每隔 X 分鐘（可指定）檢查一個秘密的 github 倉庫。如果有漏洞的 bug 發佈在這個儲存庫中，它就會成為一個信號，觸發所有訂閱的安裝程式的 killswitch，並將您的 lnbits 實例轉換為使用 void Wallet。如果烏雲已經散去，而且您已經安裝了安全更新，您就可以將資金來源設定為您的節點、Wallet 或任何您正在使用的東西，同樣也可以透過管理伺服器區段來設定。如果您不知道該如何設定，這個 wiki 有一個關於切換資金來源的章節。



### 管理員與超級使用者的差異


LNbits 管理 UI 可以讓您透過 LNbits 前端更改 LNbits 設定。預設是關閉的，當您第一次在 `.env` 檔案中設定環境變數 `LNBITS_ADMIN_UI=true` 時，設定會被初始化並使用。自此之後，將會使用資料庫中的相關設定，而非 .env 檔案中的設定。


### 超級使用者


透過管理介面，我們引進了超級使用者，超級使用者擁有伺服器的存取權，因此可以透過前端和 api 變更可能導致伺服器當機或無法回應的設定，例如變更資金來源。超級使用者只儲存在資料庫的設定表中。當設定「重設為預設值」並重新啟動後，新的超級使用者就會被建立。我們也為 API 路由新增了一個裝飾程式，以檢查超級使用者是否存在。它的 ID 不會透過 api 和前端傳送，只會接收一個 bool (是/否) 來判斷您是否是超級使用者。


只有超級使用者才可以透過「充值」區段將 Satoshis 儲存在不同的錢包中。


您也可以在建立超級使用者時，透過 webhook 將其發佈到另一個服務。更多資訊請參考 https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`.


在前端，您也可以開啟「管理伺服器」部分，選擇「主題」->「自訂標誌」，以變更顯示在「建立 Wallet」頁面上的商店圖片。


### 管理員使用者


環境變數：LNBITS_ADMIN_USERS」，以逗號隔開的使用者 ID 清單。管理員使用者可以變更管理介面中的設定 - 但資金來源設定除外，因為這將需要重新啟動伺服器，並可能導致伺服器無法存取。此外，他們也可以存取 `LNBITS_ADMIN_EXTENSIONS` 中專屬於他們的所有擴充套件。


### 允許使用者


環境變數：LNBITS_ALLOWED_USERS`，以逗號隔開的使用者 ID 清單。定義這些使用者後，LNbits 將不再對公眾開放。只有已定義的使用者和管理員才能存取 LNbits 前端。




#### 更新 LNbits

更新 LNbits 本機實例的一般方式是複製貼上下列 CLI 指令：


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


如果您執行 Raspiblitz 或 MyNode，可能還需要一個

```
sudo systemctl restart lnbits
```

在最後，因為它將 LNbits 作為服務來執行。


在 Umbrel/Citadel 上，指令為

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### SQLite 遷移到 PostgreSQL


如果您已經安裝 LNbits 並在 SQLite 資料庫上執行，我們強烈建議您遷移到 postgres，如果您打算大規模執行 LNbits。


附帶的腳本可以輕鬆完成遷移。您需要已經安裝了 Postgres，而且應該有使用者密碼（請參閱上面的 Postgres 安裝指南）。此外，您的 LNbits 實例需要在 postgres 上執行一次，以執行資料庫 Schema，然後才可以進行遷移：


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

希望現在所有東西都能正常運作並遷移...再次啟動 LNbits 並檢查是否一切運作正常。



#### 資料庫的備份和還原


請參考 [這份非常詳細的備份與還原程序指南](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore)。



#### 從我的節點為我的 LNbits Wallet 注資不起作用


如果您要從 LNbits 資金來源的相同節點傳送 Sats，您需要編輯 LND.conf 檔案。


要包含的參數有`allow-circular-route=1`


請在 LND.conf 的 Application options（應用程式選項）一節中這樣做。否則在某些 bundle 節點上，LND 的啟動可能會失敗。


注意：建議改用新的 adminUI 擴充套件與「TopUp」選項來為 LNbits 帳戶充值。


#### 錯誤 426

我收到錯誤："lnurl 需要透過公開存取的 https 網域或 tor 傳送。需要 426 升級"</summary>。


這個錯誤通常是因為您在 ngnix tunnel 後面的 LNbits 未正確轉送 LNURL Address。停止您的 LNbits 並編輯 .env 檔案，加入這一行：

`forwarded_allow_ips=*`


此外，如果您使用 ngnix 設定，請確定 ngnix 配置中有這些標頭：


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### 網路錯誤

掃描 QR 時，我收到「https 錯誤」、「網路錯誤」或其他錯誤</summary>。


壞消息，這是一個路由錯誤，可能有很多原因。首先用 [Lightning Decoder](https://lightningdecoder.com/) 檢查 QR 的 LNURL，看看是否有什麼奇怪的地方。讓我們試試幾個最可能的問題及其解決方法。


LNbits 僅透過 Tor 執行，您無法在公共網域上開啟，例如 lnbits.yourdomain.com



- 如果您希望您的設定保持如此，請使用 .onion URI 開啟您的 LNbits Wallet 並再次建立。以這種方式產生的 QR 可透過此 .onion URI 存取，因此只能透過 tor 存取。請勿從 .local URI 開啟 generate QR，因為它無法透過網際網路存取 - 只能從您的家庭區域網路存取。
- 開啟您用來掃描 QR 的 LN Wallet 應用程式，這次請使用 tor（請參閱 Wallet 應用程式設定）。如果應用程式不提供 tor，您可以使用 Orbot (Android) 代替。有關如何開啟 LNbits 的 clearnet/https 詳細說明，請參閱安裝部分。



#### 防止他人在我的 LNbits 上產生錢包


當您在 clearnet 中執行 LNbits 時，基本上每個人都可以在上面使用 generate 和 Wallet。由於您節點的資金與這些錢包綁定在一起，您可能想要防止這種情況發生。有兩種方法可以做到這一點：


在 `.env` 檔案中設定允許的使用者和擴充套件 ([請參閱此處的 env範例](https://github.com/lnbits/lnbits/blob/main/.env.example))。只有在 .env 中使用 `adminUI=FALSE` 設定時才會生效，否則需要在管理伺服器部分 -> 使用者 -> 允許的使用者中執行。之後其他人都不會被允許。




#### 自訂 Invoice 到期時間範圍


現在您可以使用自訂到期日的 generate 發票。與後端相容：LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet 到目前為止！


您可以在 .env 檔案中設定 `LIGHTNING_INVOICE_EXPIRY` 或使用 AdminUI 來變更所有發票的預設值。在 /api/v1/payments 端點中也有一個新欄位，您可以在 JSON 資料中設定到期日。




## Wallet-URL 已刪除


### 示範伺服器 legend.lnbits 上的 Wallet


請務必將您的 Wallet-URL、Export2phone-QR 或 LNDhub 的副本保存在安全的地方，以備您自己的錢包使用。遺失時，LNbits 無法幫助您找回。


### 自己的資金來源/節點上的 Wallet

請務必將您的 Wallet-URL、Export2phone-QR 或 LNDhub 的副本保存在安全的地方，以備您自己的錢包使用。您可以在您的 LNbits 用戶管理器擴展或 sqlite 資料庫中找到所有 LNbits 用戶和 Wallet-ID 。要編輯或讀取 LNbits 資料庫，請前往 LNbits /data 資料夾，並尋找名為 sqlite.db 的檔案。您可以使用 excel 或專用的 SQL 編輯器（如 [SQLite browser](https://sqlitebrowser.org/)）來開啟和編輯它。


您也可以透過 CLI 轉存錢包，並檢視資料庫內的每個 Wallet。


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


輸出結果如下


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

您想要將這些值放入一個 url，就像這樣


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


其中，將 f8a43fc363ea428db5c53b3559935f1f 替換為名稱前的值 (在我們的範例中為 f8a43fc363ea428db5c53b3559935f1f)，而 1280ff5910a9c485a782a2376f338b6c 為您的使用者，並應該成為名稱後的值。要退出 sqlite3，請在


```
.quit
```

#### LNURL 適用於閃電-Address 反之亦然


試試 fiatjaf 的 [encoder](https://lnurl-codec.netlify.app/) 或 [this one](https://lightningdecoder.com/).若要支付或檢查 LNURLp，您也可以使用 [LNurlpay](https://wwww.lnurlpay.com/)。它應該說明 HTTPS 而不是 HTTP。



#### 設定人們向我的 LNURLp QR 付費時看到的註解

當您建立 LNURL-p 時，預設不填寫註解方塊。這表示不允許在付款上附加註解。


為了允許註解，請加入方塊的字元長度，從 1 到 250。一旦您在此加上數字，註解方塊就會顯示在付款過程中。您也可以編輯已建立的 LNURL-p 並加入該數字。


![lnbits comments](assets/lnbits-comments.webp)


#### 存入 onchain BTC 到 LNbits

有兩種方式可以將 Exchange Sats 從 onchain BTC 轉換成 LN BTC (resp. to LNbits)。


##### 透過外部交換服務。


其他無法存取您的 LNb 的使用者可以使用交換服務，例如 [Boltz](https://boltz.Exchange/)、[FixedFloat](https://fixedfloat.com/)、[DiamondHands](https://swap.diamondhands.technology/) 或 [ZigZag](https://zigzag.io/)。如果您在 LNbits 實例中只提供 LNURL/LN 發票，但付款人只有 onchain Sats，因此他們必須先在自己這邊交換這些 Sats，這就很有用了。程序很簡單：用戶發送 onchain btc 到交換服務，並提供來自 LNbits 的 LNURL / LN Invoice 作為交換的目的地。


##### 使用 Onchain 和 Boltz LNbits 延伸。


請記住，這是一個獨立的 Wallet，而不是 LNbits 在您的 LN 資金來源上表示為 「您的 Wallet 」的 LN btc。這個鏈上的 Wallet 也可以使用 LNbits Boltz 或 Deezy 擴展來交換 LN btc 到（例如您的 hardwarewallet）。如果您運行一個與您的 LNbits 相連的網路商店來進行 LN 付款，定期將 LN 中的所有 Sats 放到 onchain 中是非常方便的。這將使您的 LN 通道有更多空間來接收新的 Sats。


沒有 Bitcoin Hardware Wallet 的程序：



- 使用 Electrum 或 Sparrow Wallet 建立新的 onchain Wallet，並將備份 seed 保存在安全的地方。
- 前往 Wallet 資訊，複製 xpub。
- 前往 LNbits - Onchain 延伸，使用該 xpub 建立新的 Watch-only wallet。
- 前往 LNbits - Tipjar 延伸並建立新的 Tipjar。除了 LN Wallet 之外，也選擇 onchain 選項。
- 選項 - 到 LNbits - SatsPay 延伸，為 onchain btc 建立一個新的收費。您可以選擇 onchain 和 LN 或兩者皆有。然後，它將創建一個可以共享的 Invoice。
- 選項 - 如果您使用您的 LNbits 連結到 Wordpress + Woocommerce 頁面，一旦您建立/連結 Watch-only wallet 到您的 LN btc 商店 Wallet，客戶就可以在同一個螢幕上同時選擇付款。


當您在 LNbits 收到付款時，交易記錄只會顯示交易的恢復類型。


![lnbits payment details](assets/lnbits-payment-details.webp)


在交易總覽中，您會發現一個 Green 的小箭頭代表已收到，紅色箭頭則代表已送出的資金。


如果您按一下這些箭頭，就會彈出詳細資料視窗，顯示附加的訊息以及寄件者的姓名 (如果有)。


要設定在付款中出現的名稱，在 LNbits 中目前無法做到 - 但可以接收。這只有在寄件者的 LN Wallet 支援 [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) 如 [OBW、Blixt、Alby、ZBD、BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents) 的情況下才有可能。


然後，您會在 LNbits 交易的詳細資料中看到一個別名/假名（點擊箭頭）。請注意，您可以在這裡提供任何名字，如果您收到的是真實的寄件人名字，它可能與真實的寄件人名字無關。


![lnbits namedesc](assets/lnbits-namedesc.webp)


要在 Wallet 應用程式中匯入您的 LNbits 帳號，請使用您要使用的帳號/Wallet 開啟您的 LNbits，進入「管理擴充套件」並啟動 LNDHUB 擴充套件。開啟 LNDHUB 擴充套件，選擇您想要使用的 Wallet，掃描 "admin「 或 」Invoice only" QR，視您想要該 Wallet 的安全層級而定。


您可以使用 [Zeus](https://zeusln.app/) 或 [Bluewallet](https://bluewallet.io/) 作為 lndhub 帳戶的 Wallet 應用程式，其中 BW 支援一個以上的 Wallet。


我們建議您也將 LN 網路 URI 設定為您自己節點的 URI。如果您的 LNbits 實例僅限於 Tor，您也必須在啟用 Tor 的情況下使用這些應用程式。在這種情況下，您也需要透過 Tor .onion Address 來開啟 LNbits 頁面。


如果您在使用 On-Chain 擴充套件中的 ypub 時出現 Error "unsupported Hash type"，請檢查您的 LNbits 實例是否使用 python 3.10，它可能受到 [this issue](https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python) 的影響。按照 stackoverflow 答案中的描述編輯 openssl.cnf，並重新啟動您的 LNbits。



## 使用 LNbits 製作工具與建置


LNbits 擁有各式各樣的 [開放 API](https://legend.lnbits.com/docs)和工具，可針對數千萬種不同的使用情況，編寫程式並連接至許多不同的裝置。


如果你是個新手，可以從 Ben Arc 提供的 [MakerBits 簡報](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) 開始，了解如何根據 LNbits 製作小工具。


### 重要事項：


- LNbits 以 LNURL 協定為基礎，其請求有兩種有效形式：https:// clearnet 連結（不允許自簽證書）或 http:// v2/v3 onion 連結。若要提供 LNbits 服務，例如可在野外使用的 LNURLp/w QR 碼或 NFC 卡，您需要將 LNbits 開啟至 clearnet (https)。
- 只能使用 DATA 纜線為您的 esp32 供電。不是所有的纜線除了為 esp 供電外，還支援資料。 如果 esp 隨附的纜線是僅供電的纜線，您就不是第一個使用這種纜線的人了。
- 請確定不要使用連接其他裝置的 USB-Hub。這可能會導致 Hard 要除錯的怪異效果 (例如無法啟動或停止)。
- 要在 MacOS 上實現 esp 專案，您需要 UART Bridge 驅動程式。如果您在 Mac 或 Linux 系統上遇到驅動程式的問題，您可以在這裡找到這些驅動程式；如果涉及 TTGO 顯示器，則可以在這裡找到這些驅動程式。如果您在 Windows 系統上遇到連接問題，請確定下載舊版的 11.1.0，因為較新的版本無法運作！您也可以在這裡找到串列終端機來檢查您的連線 - 設定為波特率 115200。
- 雖然使用 Platform.io 會比較舒適 (例如，會自動安裝相依性)，但我們建議初學者使用 Arduino。
- TT-Go Display S3：螢幕保護膜的標籤顏色會告訴您是使用哪個控制器 (ST7735_redtab、ST7735_blacktag、ST7735_greetab、greentab128...) 製作的。保留它是為了在您自己編程時，螢幕無法正確顯示圖形，例如顏色錯誤、鏡像或邊緣的雜散像素時，能夠進行除錯。如果您需要這樣做，有一份史詩級的指南可以幫助您針對不同的顯示器進行調整。
- 請務必使用小寫的 lnurl239xx，而非 LNURLl239xx
- 加入 lightning:lnurl1234xyz 會建立 QR，要求在掃描時開啟使用者 Wallet 的此 Invoice（在 iOS 上最後安裝的 lightning 應用程式，在 Android 中設定）
- 如果您透過 Web 更新 esp32，則只能使用這些瀏覽器 (TL:DR Chrome、Edge 和 Opera)。
- 請注意此 PIN-OUT 參考值為 esp
- 當您使用 FOSSoftware 或 FOSGuides 時，請務必連結作者。每個人都喜歡看著自己的寶貝成長，而且這也會啟動一個令人讚嘆的建築鏈:)


如果您在專案上需要協助，請來 [Makerbits Telegram 群組](https://t.me/makerbits) - 我們會幫您！


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


以下是您可以使用 LNbits 建立的一些專案類別：



- [Nostr簽署裝置](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN atm](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [自動販賣機](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora and Mesh Networking](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [幫手與資源](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [更多 "Powered by LNbits" 的專案範例請見此](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits)。
- [LNbits 用例](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)