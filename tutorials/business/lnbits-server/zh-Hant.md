---
name: LNbits Server
description: 在 Ubuntu VPS 與 Phoenixd 或 Umbrel 上安裝與設定自行託管的 LNbits 伺服器
---

![cover](assets/cover.webp)



LNbits 是一個開放原始碼的網頁介面，可將任何 Lightning 後端（LND、Core Lightning、Phoenixd）轉換成完整的服務平台。這個自託管解決方案讓您可以單獨管理多個 Lightning 投資組合、部署銷售點、建立捐款系統或計費服務，同時保留對資金的完全控制。



本教學涵蓋兩種安裝方式： **VPS Ubuntu with Phoenixd**（無需完整 Bitcoin 節點的輕量級解決方案）和 **Umbrel**（與您現有的 LND 節點整合）。Plan ₿ Academy 的一般 LNbits 教學涵蓋概念和擴充，與此不同，本指南著重於逐步的技術安裝程序。



## 什麼是 LNbits？



LNbits 是用 Python (FastAPI) 開發的 Lightning 會計系統，可連接到現有的後端 (LND、Core Lightning、Phoenixd)。與傳統的 Lightning 節點不同，LNbits 提供了一個易於使用的介面，用自己的 API 金鑰來管理多個獨立的投資組合。您可以為家人、員工或專案建立子帳戶，但不會讓他們存取您所有的資金。



解耦架構將資訊儲存於 SQLite（預設）或 PostgreSQL（生產），而資金則仍由您的 Lightning 後端管理。這種分離保證了可移植性：您可以從 Phoenixd 遷移到 LND，而不會丟失您的用戶資料。



## 主要功能



LNbits 提供多功能的**擴充系統：TPoS (銷售點)、Paywall (內容貨幣化)、Events (票務)、LndHub (BlueWallet 的伺服器)、Bolt Cards (NFC 付款)、Split Payments (自動分發) 和 User Manager (具有驗證功能的使用者管理)。



**儀表板**顯示即時餘額、交易歷史和帳單工具。每個 wallet 都有一個包含其 API 金鑰的獨特 URL，無需傳統登入即可存取。三層 API 金鑰系統** (管理員、發票、唯讀) 為安全整合提供細緻的權限控制。



LNbits 本機實作**LNURL**（LNURL-pay、LNURL-withdraw、LNURL-auth），並支援**Lightning Address**，保證與現代 Lightning wallets 相容，方便部署專業服務。



## 支援的平台



**Ubuntu VPS**：沒有完整 Bitcoin 節點的輕量級解決方案。先決條件：1 vCPU、1-2 GB RAM、Ubuntu 22.04 LTS、Python 3.10+、Git、UV。需要 HTTPS + 網域名稱才能公開 (LNURL 服務)。



**Umbrel**：可從 App Store 輕鬆安裝。先決條件：具備同步 LND 與開放頻道的功能性 Umbrel 節點。自動設定。



以下是 Umbrel 和 Umbrel LND 教學的連結：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## 使用 Phoenixd 安裝 Ubuntu VPS



### 步驟 1：保護 VPS 伺服器



**在任何安裝**之前，您需要根據技術規則保護您的 Ubuntu VPS 伺服器。這個步驟對於保護您的基礎架構和您的 Lightning 資金來說是**關鍵的**。



這裡有一份詳細的指南，可以幫助您開始使用： **[Initial Ubuntu server configuration - Step-by-step guide](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** 作者 Daniel P. Costas。



本指南涵蓋使用者組態、安全 SSH、防火牆 (UFW)、fail2ban、自動更新和良好的系統安全實務。



### 步驟 2：安裝 Phoenixd



當您的伺服器安全後，您需要安裝和設定 Phoenixd。Plan ₿ Academy 提供全面的專門教學，涵蓋安裝、seed 生成和 systemd 服務設定：



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

一旦 Phoenixd 開啟並運作 (使用 `./phoenix-cli getinfo` 檢查)，記下 `~/.phoenix/phoenix.conf` 中的 **HTTP 密碼** - 您需要它來連接 LNbits 到 Phoenixd。



### LNbits 部署



安裝 UV 並複製 LNbits ：


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



設定 Phoenixd 後端：


```bash
cp .env.example .env && nano .env
```



新增至 `.env` ：


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



使用 `uv run lnbits --host 0.0.0.0 --port 5000` 進行測試，然後以 `Wants=phoenixd.service` 建立 systemd 服務。



## 初始設定與首次使用



### 超級使用者啟動



在 `.env` 中啟動管理員介面：


```
LNBITS_ADMIN_UI=true
```



重新啟動 LNbits (`sudo systemctl restart lnbits`) 並擷取 SuperUser ID：


```bash
cat ~/lnbits/data/.super_user
```



前往 `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` 管理面板。伺服器」功能表可讓您設定資金來源、分機和使用者帳號。



### 安全的帳戶建立



**對於公開暴露**很重要：如果您要將您的 LNbits 實例公開在可從網際網路存取的公共網域名稱上，禁止自由建立使用者帳號是**重要的**。



從 SuperUser 管理介面，進入「設定」，然後到「使用者管理」區。在那裡您可以找到「允許建立新使用者」選項。



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**For a public exhibition with domain name** ：




- 您必須停用**「允許建立新使用者」選項
- 如果沒有這種保護，網際網路上的任何人都可以在您的實例上建立帳戶。
- 攻擊者可以在您不知情的情況下創建帳戶，並使用您的 Lightning 節點的流動性
- 您需要從 SuperUser 介面手動建立使用者帳號



**For local use only** ：




- 如果您的實例只能在本機存取，則此選項較不重要 (http://localhost:5000)
- 然而，停用此選項是良好的一般安全措施



一旦配置完成，只有SuperUser管理員可以通過 "Users "介面創建新的用戶帳戶。這種方法保證了對誰可以訪問您的Lightning基礎設施和使用您的資金的完全控制。



### 開啟第一個通道



Phoenixd 透過自動流動資金自動管理通道。從 LNbits 生成一張 ~30,000 sats 的 Lightning 發票，並從另一個 wallet 支付。Phoenixd 自動為 ACINQ 打開一個通道。開戶費 (~20-23k sats) 會被扣除，餘額 (~7-10k sats) 會在 on-chain 確認後出現。



使用 `./phoenix-cli getinfo` 檢查狀態。然後考慮停用自動流動 (在 `phoenix.conf` 中 `auto-liquidity=off`) 來控制通道開啟。



### 公開顯示與 HTTPS



**重要**：公開顯示必須使用 HTTPS (API 金鑰安全性 + LNURL 相容性)。本地使用時請跳過此步驟。



**Caddy (建議)**： 自動 SSL。`sudo apt install -y caddy`, 編輯 `/etc/caddy/Caddyfile` ：


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


重新啟動：`sudo systemctl restart caddy`.



**Nginx** ：更多控制。安裝 `nginx certbot python3-certbot-nginx`，建立 `/etc/nginx/sites-available/lnbits` ：


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


啟動： `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`.



新增到 `.env`： `FORWARDED_ALLOW_IPS=*`



## 傘架安裝



### 從 App Store 部署



前往 Umbrel App Store，搜尋「LNbits」，然後按下「安裝」。



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel 會自動檢查所需的相依性。LNbits 需要 Lightning 節點 (LND) 才能運作。如果您的 Lightning 節點已開始運作，請點選「安裝 LNbits」確認。



![Dépendances LNbits](assets/fr/02.webp)



Umbrel 會下載 Docker 映像檔、自動配置與 LND 的連線，並啟動容器 (2-5 分鐘)。安裝完全在背景中進行。



### 初始超級使用者設定



首次啟動時，LNbits 會提示您建立 SuperUser 管理員帳號。輸入使用者名稱和安全密碼，以保護對管理介面的存取。



![Configuration SuperUser](assets/fr/03.webp)



**重要**：此 SuperUser 帳戶在您的 LNbits 實例上擁有完整權限。請選擇一個強大的密碼，並妥善保管。



建立帳戶後，您會自動進入主管理介面。Umbrel 已將 LND 設定為您的資金來源 - 所有 Lightning 付款將透過您現有的管道進行。



### 存取管理員介面



在左側功能表中，按一下「設定」以存取完整的管理面板。



![Interface Settings](assets/fr/04.webp)



Wallets Management（錢包管理）」會顯示有關您組態的關鍵資訊：




- 資金來源** ：LndBtcRestWallet (直接連接到您的 LND Umbrel 節點)
- 節點餘額** ：您的 Lightning 頻道中可用的流動資金總額
- LNbits 餘額**：分配給 LNbits 系統的資金（最初為 0 sats）



現在您可以直接利用您的 Umbrel 節點的流動性，來使用您所建立的所有 LNbits 錢包。不需要額外的配置 - LNbits 已經開始運行。



### 使用者管理



LNbits 最強大的功能之一是它能夠創建多個獨立的用戶，每個用戶都有密碼認證和獨立的錢包。此架構可讓您充分利用 Umbrel 節點的流動性，同時為不同用途提供完全獨立的子帳戶：企業、家庭、員工、專案等。



在側邊功能表中，按一下「使用者」以存取使用者管理。按一下「建立帳戶」以新增使用者。



![Gestion des utilisateurs](assets/fr/05.webp)



填寫使用者建立表單：




- 使用者名稱**：登入使用者名稱 (例如: "satoshi")
- 設定密碼**：啟動此選項以設定驗證密碼
- 密碼** 和 **密碼重複**：設定此使用者的密碼



![Création utilisateur satoshi](assets/fr/06.webp)



可選欄位 (Nostr Public Key、Email、First Name、Last Name) 可以留空，以進行最少的設定。按一下「建立帳戶」以確認。



![Confirmation utilisateur créé](assets/fr/07.webp)



您的新使用者現在會出現在使用者清單中，並顯示其獨特的識別碼和使用者名稱。



![Liste des utilisateurs](assets/fr/08.webp)



**重要的一點**：每個使用者都可以使用自己的密碼完全獨立地登入。SuperUser 管理員可透過管理介面保留完整的控制權。



### 使用者 wallet 管理



現在 "satoshi" 使用者已經建立，您需要為他指派一個 wallet Lightning。按一下相關使用者的 wallet 圖示 (第二個圖示)，然後按一下「CREATE NEW WALLET」。



![Gestion des wallets](assets/fr/09.webp)



對話方塊提示您為 wallet 命名。輸入描述性名稱 (例如 "Wallet Of Satoshi")，並選擇顯示貨幣 (CUC、USD、EUR 等)。



![Création wallet](assets/fr/10.webp)



點選「CREATE」。LNbits 即時為此使用者產生一個可用的 wallet Lightning。



![Confirmation wallet créé](assets/fr/11.webp)



現在您看到兩個現有的錢包：自動建立的預設 wallet "LNbits wallet「，以及新的 」Wallet Of Satoshi"。為了簡化使用者體驗，您可以按一下刪除圖示 (紅色垃圾桶) 刪除預設的 wallet。



![Wallet final unique](assets/fr/12.webp)



satoshi" 使用者現在擁有一個單一、明確識別的 wallet。每個 wallet 使用者完全自主運作，同時使用您底層 LND 節點的流動性。



**Key concept**：所有這些錢包共享您的 Umbrel 節點的全球流動資金。您不需要為每個 wallet 創建新的 Lightning 通道 - LNbits 充當智能會計層，管理您現有 Lightning 基礎設施中的資金分配。這就是 LNbits 多 wallet 系統的威力。



### 使用者登入



登出 SuperUser 帳戶（右上方的圖示）並返回 LNbits 登入頁面。現在您可以使用新使用者的憑證登入。



![Connexion utilisateur satoshi](assets/fr/13.webp)



輸入先前定義的使用者名稱 ("satoshi")和密碼，然後按一下「登入」。使用者就可以直接進入他個人的 wallet，與管理介面完全隔離。



### Interface 來自 wallet 使用者



登入後，使用者可存取完整的 wallet Lightning 介面。



![Interface wallet utilisateur](assets/fr/14.webp)



介面特色 ：




- 目前餘額**：以 sats 和選擇的貨幣（本例中為 CUC）顯示
- 主要動作**：PASTE REQUEST、CREATE INVOICE、QR 圖示 (快速掃描)
- 交易記錄** ：所有付款和收據的完整清單
- 右側面板**：設定與存取選項



### 行動存取 wallet



右側面板提供一個特別實用的功能：wallet 的行動存取。展開「行動存取」部分，即可發現可用的選項。



![Mobile Access](assets/fr/15.webp)



LNbits 提供多種方式在智慧型手機上使用此 wallet：



**選項 1：相容的行動應用程式




- 從 App Store 或 Google Play 下載 **Zeus** 或 **BlueWallet**
- 在 LNbits 中為此 wallet 啟用 **LndHub** 延伸功能
- 使用手機應用程式掃描 LndHub QR 代碼，連接 wallet



**選項 2：透過行動瀏覽器直接存取**




- 使用 QR 代碼匯出至手機」中顯示的 QR 代碼包含 wallet 的完整 URL，並已整合驗證
- 使用智慧型手機掃瞄此 QR 代碼，即可直接在手機瀏覽器中開啟 wallet
- 將頁面加入首頁畫面，以便快速存取



**重要安全**：此 URL 包含完全存取 wallet 的 API 金鑰。切勿公開分享。請像對待 Bitcoin 私密金鑰一樣對待此 QR 代碼 - 任何人掃描此 QR 代碼，即可完全存取 wallet。



這項行動功能可將您的 LNbits Umbrel 實例變成您和您朋友名副其實的 Lightning wallet 伺服器，同時由於您擁有自我託管的節點，因此可保留對您資金的完全主權。



### 使用者存取權限分享



此多使用者配置的主要用途是 ** 與您的家人或親密圈子 ** 分享錢包。一旦您建立了具有專屬 wallet 的使用者（例如我們範例中的「satoshi」），您就可以與家中值得信任的成員分享這些登入憑證。



** 在 Umbrel 上的存取安全**：在 Umbrel 上存取您的 LNbits 實例自然會受到保護，因為它只能以 .NET 方式存取：




- 在您的本地網路** ：連接至相同 WiFi/乙太網路的家庭成員可存取實例
- 透過 VPN**：如果您使用 VPN，例如在 Umbrel 伺服器上設定的 Tailscale，則授權使用者可取得安全的遠端存取。



這種雙層保護（網路存取 + 使用者驗證）讓「允許建立新使用者」選項在 Umbrel 上不那麼重要。只有已經可以存取您的網路或 VPN 的人，才能到達登入介面。



**典型情況**：您建立一個「爸爸」帳戶、一個「媽媽」帳戶、一個「企業」帳戶等。每個家庭成員都有自己獨立的 wallet Lightning，同時受益於您 Umbrel 節點的共享流動性。只要分享使用者名稱和密碼 - 使用者就可以從本機網路的任何裝置或透過 Tailscale VPN 連線。詳情請參閱我們的 Tailscale 專門教學：



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 探索可用的擴充套件



回到 SuperUser 介面，存取左側面板的「Extensions」功能表，即可發現完整的 LNbits 延伸生態系統。



![Extensions disponibles](assets/fr/16.webp)



LNbits 提供豐富的擴充功能目錄，可將您的實例轉換為名副其實的 Lightning 服務平台：





- 點唱機**：由 sats 驅動的點唱機系統 (Spotify 付款)
- 支援票**：付費支援系統（接收 satss 以回答問題）
- TPoS**：適用於零售商的安全行動銷售終端機
- 使用者管理員**：進階使用者和 wallet 管理（我們剛剛使用過）
- 活動**：活動門票的銷售和驗證
- LNURLDevices**：銷售點管理、ATM、連接交換器
- SMTP**：讓使用者可以傳送電子郵件並賺取 Satss
- Boltcards**：為 Lightning 點對點支付的 NFC 卡編程
- NostrNip5**：為您的網域建立 NIP5 位址
- Splitpayments**：在多個錢包之間自動分配付款



每個擴充套件只需在此介面上按一下即可啟用。標示「FREE」的擴充功能是免費的，有些則是「付費」版本。瀏覽產品目錄，找出符合您需求的擴充套件 - 無論是用於商務、家庭管理，或是嘗試使用 Lightning Network 的功能。



## 優點與限制



**優點**：財務主權 (完全控制資金/金鑰/資料)、架構彈性 (無損 VPS→full node 移轉)、專業擴充系統、直覺式介面。



**限制** ：測試中的軟體 (請注意金額)、安全由管理員負責、包含敏感 API 金鑰的 URL (必須使用 HTTPS)、多使用者管理意味著管理責任。



## 最佳實踐



**Backups**：Phoenixd Seed/LND 認證、LNbits 資料庫、.env 檔案。每日自動備份，不儲存在生產伺服器中，並加密。定期測試還原。



**Maintenance**：定期檢查更新（LNbits、Lightning 後端、作業系統）。在重大更新之前，請務必檢查發佈說明。





- 在 Umbrel**：App Store 會自動通知您新版本。透過「Manage Extensions」>「Update All」同步擴充套件。檢查 Umbrel 自動備份中是否包含 SQLite 資料庫。
- 在 VPS 上**：使用 `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits` 手動更新。監控系統日誌：`sudo journalctl -u lnbits -f`.



## 總結



LNbits 自助托管提供了通往 Lightning 金融主權的具體路徑。VPS+Phoenixd 提供快速服務的輕量級解決方案，Umbrel 與現有 Bitcoin 節點完全整合。可擴充的架構可從簡單的多使用者 wallet 演進至複雜的商業用例。



自我託管意味著責任：備份種子、保護存取權、從適量開始。有了這些預防措施，LNbits 就能成為「閃電」經濟的穩健解決方案，同時保留分散性與自主性。



## 資源



### 官方文件




- [LNbits 文件](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [官方安裝指南](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### 社區指南




- [Initial Ubuntu server configuration](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) by Daniel P. Costas (step-by-step VPS security)
- [LNbits + Phoenixd 安裝於 Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) by Daniel P. Costas (完整指南)
- [Clearnet 上的 LNbits 伺服器](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes