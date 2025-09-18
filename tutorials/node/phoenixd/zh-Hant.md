---
name: Phoenixd
description: 使用 Phoenixd 部署您自己的極簡 Lightning 節點
---

![cover](assets/cover.webp)



財務自主還意味著控制您的 Lightning 基礎設施。對於希望將 Bitcoin Lightning 整合到其應用程式中的開發人員和公司而言，**Phoenixd** 代表了理想的解決方案：一個簡約、專門的 Lightning 節點，具有自動流動性管理功能。



Phoenixd是ACINQ開發的Lightning服務器，專為通過HTTP API發送和接收Lightning付款而設計。與LND或Core Lightning等全功能實現不同，Phoenixd抽象了渠道管理的所有複雜性，同時保留了您資金的自我保護。



在本教程中，我們將探討如何安裝、配置和使用 Phoenixd，以便利用自託管的基礎結構和易用的 API 開發 Lightning 應用程式。



## 什麼是 Phoenixd？



Phoenixd是ACINQ開發的最小化、專門的Lightning節點。它是專為希望將 Lightning 整合到應用程式中的開發人員和企業設計的解決方案，而無需 Full node 的複雜管理。



### 操作原理



**Phoenixd是一個最小的Lightning節點，它使用ACINQ作為其LSP（Lightning服務提供商），以實現自動流動性。當您收到 Lightning 付款時，它會自動打開與 ACINQ 節點的通道，以分配必要的流入容量。這種 「即時 」的流動性是即時的，但收費恰好是所收到金額的**1% + Mining 費用**。



**自動化管理：** 系統管理三個關鍵 Elements：




- Lightning** 通道：根據需要自動開啟、關閉和管理
- 流入/流出的流動性**：透過拼接和通道開放自動提供
- 費用信用** ：小額付款不足以證明通道的合理性，會儲存為未來收費的準備金



### Phoenixd 福利



**您可以控制您的私人金鑰（12 個字的 seed）和資金。Phoenixd 會在本地產生您的 Wallet，而不會分享您的金鑰。



**個人基礎架構：** Phoenixd 在您的伺服器上執行，讓您可以存取詳細的日誌、配置和 API 控制。您不再依賴第三方服務來存取您的資金。



**整合式 API：** Phoenixd 具有 HTTP API，可與其他服務、本機 LNURL 支援和客製化應用程式開發整合。



** 易於整合：** 由於其簡單的 REST API，Phoenixd 可以整合到任何需要 Lightning 付款的應用程式或服務中。



**重要提示：** 自動流動資金仍然來自作為 LSP (Lightning Service Provider) 的 ACINQ。Phoenixd 使用與 Phoenix mobile 相同的機制進行自動通道管理。



## 安裝 Phoenixd



### 先決條件



Phoenixd 需要 Linux 環境 (建議使用 Ubuntu/Debian)，並具備一些基本的指令列技能。為了達到最佳效能，您需要 .NET Framework 2.0：





- Linux 伺服器**：VPS 或連線穩定的本機
- OpenJDK 21** ：Java 運行環境
- 穩定的網際網路連線**：用於與 Lightning Network 同步
- 網域名稱**（可選） ：用於安全 HTTPS 存取 API



### 下載與安裝



**1.下載 Phoenixd**



前往 [GitHub 發行版本] 頁面 (https://github.com/ACINQ/phoenixd/releases) 並下載適用於您架構的最新版本：



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2.首次啟動



啟動 Phoenixd 進行初始化：



```bash
./phoenixd
```



首次啟動時，您會被要求輸入「我了解」來確認兩個重要步驟：



**訊息 1 - 備份：**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**保存這 12 個字** - 這是您復原的唯一保證。



**訊息 2 - 自動清償：**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



每次確認時，請輸入`I understand`。



![Premier démarrage](assets/fr/01.webp)



*Phoenixd 首次啟動：備份確認和自動清算*



**3.在役配置** (僅法文)



若要連續運作，請建立 systemd .NET 檔案：



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Phoenixd 服務透過 systemd 和 2m sat* 的「自動流動」已啟動並可運作



## 設定與安全性



### 設定檔案



Phoenixd 會自動建立包含基本參數的 `~/.phoenix/phoenix.conf`：



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**主要參數：**




- `auto-liquidity `：自動開啟通道的大小 (預設: 2M Sats)
- http-password`：API 的管理密碼 (Invoice 建立與付款派送)
- http-password-limited-access`：限制密碼 (僅限 Invoice 建立)



### 使用 HTTPS 進行安全存取



預設情況下，Phoenixd API 只能透過本機 HTTP (`http://127.0.0.1:9740`)存取。若要從外部使用您的節點 (行動應用程式、其他伺服器、Web 整合)，您需要設定安全的 HTTPS 存取。



**反向代理原則：**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** 充當**反向代理**：它在埠 443 監聽來自網際網路的 HTTPS 請求，將其重定向到本機的 Phoenixd (埠 9740)，然後將加密的回應傳回給用戶端。



**SSL/TLS**證書是一個數位檔案，.SSL/TLS**證書是一個數位檔案：




- 證明您伺服器的身分** (防止中間人攻擊)
- 啟用 HTTPS** 加密：所有資料 (包括您的 API 密碼) 都會在傳輸過程中加密
- 由 Let's Encrypt 透過 certbot 工具免費發行**



此設定可讓您 ：




- 從網際網路安全存取 API**
- 在傳輸過程中加密您的 API** 密碼 (防止它們以明碼傳輸)
- 將 Phoenixd** 整合至需要 HTTPS 的外部應用程式中
- 符合金融 API 的安全標準**



使用 nginx 設定 HTTPS 反向代理：



**1.Nginx** 配置



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2.SSL** 憑證



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### 功能測試



檢查 Phoenixd 是否正常運作：



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



這些指令應該會回傳關於節點狀態和餘額的 JSON 資訊 (最初為空)。



![Commandes CLI](assets/fr/03.webp)



*Getinfo 和 getbalance 指令可檢查節點狀態*



## 使用 API



### 首次接收測試



**1.建立「閃電」** Invoice



使用 API 建立您的第一個 Invoice：



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### 瞭解自動流動資金機制



**基本原則：** 當您收到 Lightning 付款時，Phoenixd 有時必須開啟一個新的通道才能接收。此通道的開啟需要花費一定的費用，該費用**自動從收到的金額中扣除。



**具體範例：100,000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*第一次驗收測試：收到 Sats 100k，扣除流動資金成本後，Sats 最終餘額為 75.561*。



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**費用計算：**




- 服務費**：頻道容量的 1% (2,115,000 Sats) = 21,150 Sats
- Mining 費用**：~3,289 Sats (On-Chain 交易)
- 總計**：24,439 Sats 自動扣除



**使用 CLI 指令進行驗證：**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*付款寄出後的最終餘額：閃電出貨後剩餘 257 Sats*



**小額付款的費用抵用額：** 如果您收到的付款太少，不足以開通頻道 (< 大約 25k Sats)，這些付款會儲存在一個不可退還的 「費用抵用額 」中。當您收到足夠的金額時，此信用額將用來支付未來的頻道費用。



**2.遵循通道開啟**



觀看 Phoenixd 日誌：



```bash
journalctl -u phoenixd -f
```



您會看到通道打開，並自動扣除流動性費用。費用根據 Mempool Bitcoin 條件而有所不同，但總是包括 1% 的服務費加上當前的 Mining 費用。



**3.檢查通道**



```bash
./phoenix-cli listchannels
```



此指令會顯示您的活動頻道及其狀態和餘額。



### 完成 API 作業



Phoenixd 在連接埠 9740 上開放了 REST API，使 .NET Framework 能夠使用 Phoenixd：



**基本操作：**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**重要的成本：**




- 收款**：1% + Mining 自動資金週轉手續費
- 運費**： 0.Lightning Network 的 4% 路由費



**Webhooks:** Webhooks 可讓 Phoenixd 在事件發生時自動通知**您的應用程式（收到付款、支付 Invoice、頻道開啟等）。您的應用程式會收到即時的 HTTP 通知，而無需不斷要求 Phoenixd 更新。



**當顧客付款時，您的線上商店會自動收到通知，以便即時確認交易。



配置在 `phoenix.conf` 中：


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## 進階應用



### LNURL 整合



Phoenixd 原生支援 LNURL 通訊協定，以進行進階整合：



**LNURL-Pay:** 為 LNURL 相容的服務付款


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** 從 LNURL 服務擷取資金


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** 透過 Lightning 進行驗證，以存取服務


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### 與 LNbits 整合



根據其 [官方文件](https://docs.lnbits.org/guide/wallets.html)，LNbits 可以使用 Phoenixd 作為資金來源：



**LNbits 配置：**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



此整合可讓您建立由 Phoenixd 節點驅動的 LNbits 子帳戶，提供網頁式 Interface 以管理多個 Lightning 錢包。



### 自訂應用程式



由於其全面的 REST API，您可以開發.NET Framework：



**電子商務：** 直接將 Lightning 付款整合到您的商店中


**捐款服務：** 附有發票和自動網路掛鉤的捐款系統


**社交網路機器人：** 具備提示功能的 Telegram/Discord 機器人


**Paywall Lightning:** 只需支付 Lightning 費用即可獲得高級內容



## 安全與最佳實務



### 存取保護



**API 密碼：** 自動產生的密碼是您的 Lightning 寶庫的鑰匙。切勿共用密碼，如有疑問，請更改密碼。



**防火牆：** 切勿將 9740 連接埠直接開啟至網際網路。永遠使用 HTTPS 的 nginx。



**強化驗證：** 考慮使用 VPN 或 Tailscale 來限制只有授權裝置才能存取您的伺服器。



### 重要備份



**seed 復原：** 將您的 12 個字保存在伺服器以外的安全位置。這是您復原的唯一保證。



*~/.phoenix 目錄：** 定期備份此資料夾 (Phoenixd 關閉後)，以保留通道狀態，並加快還原速度。



**服務恢復代碼：** 也請保留您與 Phoenix 啟用 2FA 的所有服務的備份代碼。



### 監控與維護



**監控日誌：**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Updates:** 請注意 [GitHub releases](https://github.com/ACINQ/phoenixd/releases) 以取得新版本。更新就像更換二進位檔和重新啟動服務一樣簡單。



## 與替代品比較



### Phoenixd vs Phoenix 標準



**Phoenix 標準 (行動) :**




- 立即安裝、零組態
- ✅ Interface 行動直覺
- ✅ 與 Phoenixd 相同的自動儲存功能
- ❌ 沒有提供給開發人員的 API
- ❌ 無法存取詳細記錄



**Phoenixd (伺服器) :**




- ✅ 用於整合的 HTTP API
- ✅ 完全存取日誌
- 個人基礎設施
- 需要技術技能
- 需要伺服器維護



**兩者均使用 ACINQ 作為自動流動性的 LSP。



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ 全面控制，完整 Lightning 通訊協定
- ✅ 大型社區、成熟的生態系統
- 複雜的手動流動性管理
- 學習曲線較長



**Phoenixd :**




- ✅ 自動流動資金管理（如 Phoenix mobile）
- ✅ 開發人員的 API
- ✅ 簡化配置
- 使用 ACINQ 作為 LSP (無獨立路由)
- ❌ 靈活性比完整節點低



## 解決常見問題



### API 存取問題



**驗證失敗」錯誤：**


1.檢查檔案`~/.phoenix/phoenix.conf`中的密碼


2.檢查驗證格式 `-u:password`


3.確定 Phoenixd 正在執行 (`./phoenix-CLI getinfo`)



**連線超時：**




- 檢查 Phoenixd 是否在正確的連接埠（9740）上偵聽
- 在設定 HTTPS 前測試本機存取
- 檢查日誌：`journalctl -u phoenixd -f`



### 流動資金問題



** 付款未到 :**


1.檢查金額是否超過最低臨界值 (~30k Sats)


2.檢視日誌以找出通道錯誤


3.必要時重新啟動 Phoenixd



**「支出贷记 」中的余额：**


小額付款會儲存為備用金。收到較大的金額時會啟動通道開啟，並釋放這些資金。



## 總結



Phoenixd 在易用性和技術主權之間為開發人員提供了極佳的折衷方案。它提供簡單但功能強大的 Lightning API，具有自動流動性管理功能，消除了傳統 Lightning 節點的複雜性。



此解決方案特別適合希望.NET 平台的開發人員和公司：




- 將 Bitcoin Lightning 整合到您的應用程式中
- 避免 Lightning 通路管理的複雜性
- 受益於自行託管的基礎架構
- 簡單可靠的 API



有了Phoenixd，您可以利用現代化的REST API和自動化的技術管理，建立自己專屬的Lightning基礎架構。這是在您的專案中實現 Lightning 整合民主化的理想解決方案。



## 有用資源



### 官方文件




- GitHub Phoenixd** ：[github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - 原始碼與發行版
- Phoenix 伺服器**網站：[phoenix.acinq.co/server](https://phoenix.acinq.co/server) - 完整說明文件
- 常見問題集 Phoenixd** ：[phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - 常見問題



### 社區支援




- GitHub Issues** ：[github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - 技術支援
- Twitter ACINQ** ：[@ACINQ_co](https://twitter.com/ACINQ_co) - 新聞和公告