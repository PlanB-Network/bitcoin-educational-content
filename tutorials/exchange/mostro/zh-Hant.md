---
name: Mostro
description: 透過 Lightning 和 Nostr 的免 KYC Bitcoin P2P 交換平台
---

![cover](assets/cover.webp)



如何在不損害您的金融主權的情況下獲取或出售比特幣？集中式平台會強加侵入性的 KYC 程序，暴露您的個人資料，並有可能任意凍結帳戶或進行國家監控。



**Mostro P2P** 提供了一個去中心化的替代方案，結合了 Lightning Network、Nostr 協定和持有發票。它的主要創新：一個自動化的託管系統，您的比特幣在整個交易過程中都在您的控制之下，消除了盜竊、交易所破產或任意沒收的風險。



## 什麼是 Mostro P2P？



Mostro P2P 是一種開放原始碼的 Bitcoin 交換通訊協定，由 2021 年推出的熱門 Telegram 機器人 **lnp2pbot** 的開發者 **grunch** 所創造。雖然 lnp2pbot 已經透過 Lightning 啟用免 KYC 的 P2P 交換，但它卻出現了一個重大的漏洞： **Telegram 構成集中式故障點**，容易受到政府的審查。



Mostro 代表此概念的**去中心化演進**：透過以**Nostr**通訊協定 (分散式中繼的不可感應網路) 取代 Telegram，Mostro 可消除此系統性風險。該通訊協定結合了即時交易的 Lightning Network、可抗審查通訊的 Nostr，以及**持有發票**，以建立真正非監管式的自動託管。



### 技術架構



Mostro 透過三個元件運作：




- Daemon Mostrod**：協調使用者與 Lightning Network 之間的交流
- Lightning** 節點：建立保留發票 (~24 小時加密託管)
- Mostro** 客戶：使用者介面 (CLI、行動裝置、Web)



訂單在 Nostr 上公佈為公開事件 (類型 38383)，而私人交易則透過端對端加密訊息 (NIP-59、NIP-44) 傳送。每個 Mostro 實例都定義了自己的費用（一般在 0.3% 到 1% 之間）和交易限額（從幾千到幾十萬 sats，視實例而定）。



### 決定性優勢



**抗檢查**：只要 Nostr 中繼存在於世界某處，任何政府都無法關閉 Mostro。與透過 Telegram 的易受攻擊的 lnp2pbot 不同，Mostro 允許進行**防檢查**的交換。



**Escrow 非保管**：Lightning 持有發票鎖定您的比特幣，而不會永久轉移。您的資金仍由您控制，並在發生問題時 (~24h) 自動歸還給您。



**保密設計**：提供兩種模式以滿足您的需求。聲譽模式** 將您的聲譽與您的 Nostr 金鑰連結，以建立持久的信任。完全隱私模式**傾向於使用單次使用的短暫金鑰來實現絕對匿名。



## 主要功能



**分散式通訊**：所有訂單都透過加密簽署的事件在 Nostr 上公佈。私人協商透過端對端加密訊息傳輸，保證絕對保密。



**Reputation system**：5 星評級與迭代計算永久保存在 Nostr 上。讓您逐漸建立可靠交易者的聲譽。



**分散仲裁**：發生爭議時，公正的仲裁人會審查證據，並根據透明的標準做出決定。每項爭議都會產生唯一的 token，以便追蹤。



**付款彈性**：透過 yadio.io 匯率服務支援多種法定貨幣。接受 SEPA 轉帳、PayPal、Revolut、現金以及雙方同意的任何方式。



## 可用的 Mostro 客戶



Mostro 為您的 P2P 交換器提供兩種主要的操作用戶端。



### Mostro CLI - 指令行用戶端



**Mostro CLI** 是最成熟、功能最齊全的用戶端。以 Rust 寫成，透過命令列介面提供完整的 Mostro 功能。相容於 macOS、Linux 和 Windows。



**主要控制** ：




- `listorders`：顯示所有可用的訂單
- neworder`：建立新的買入或賣出指令
- `takesell` / `takebuy`：接受買盤或賣盤
- `fiatsent`：確認傳送法幣付款
- `解除`：解除託管並完成交換
- `getdm`：檢視直接訊息
- `rate` : 在交換後評估您的交易對手



適合技術使用者、自動化和需要最高安全性的環境。



### Mostro Mobile - 智慧型手機應用程式



Alpha 版本中的**手機應用程式**可直接從您的智慧型手機進行 P2P 交易。直觀的圖形 Interface 具有標籤式導覽、訂單檢視、進階篩選器和整合式聊天功能，可與您的交易對手溝通。



適用於**Android**（透過 GitHub 上的 APK），是偏好簡單和偶爾進行行動交易的使用者的最佳選擇。



### Mostro-web - Interface web (開發中)



Interface 進階 JavaScript Web 應用程式正在積極開發中。旨在提供完整的用戶體驗，具有廣泛的交易和投資組合管理功能。透過瀏覽器存取，無需安裝。



## 安裝與設定



本教學將引導您安裝和使用兩個主要的 Mostro 用戶端：CLI 和行動應用程式。



### 必要的先決條件



在開始之前，您需要 ：





- 具備足夠流動性的可用 Lightning Network** wallet (或 Lightning 相容型)
 - 推薦使用：Phoenix, Breez, Wallet of Satoshi...
 - 最低 1000 Satoshis 的流動資金進行測試



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Nostr** 私密金鑰 (格式為 `nsec1...`)
 - 在 [nostrkeygen.com](https://nostrkeygen.com/) 上建立專用交易金鑰
 - 重要**：切勿使用您的主要個人 Nostr 金鑰
 - 將私人密碼匙存放在安全的地方（密碼管理器）





- 可選擇但建議**：VPN 或 Tor 連線以遮蔽您的 IP 位址



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI 安裝



#### 在 macOS 上



**第 1 步：Rust 檢查**



檢查是否已安裝 Rust（需要 1.64 以上版本）：



```bash
rustc --version
```



如果未安裝 Rust ：



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**步驟 2：複製儲存庫**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**第 3 步：配置**



複製並編輯 ：



```bash
cp .env-sample .env
```



開啟 `.env` 並設定您的設定：



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**對於 CLI/Mobile** 同步化很重要：若要在 CLI 和行動應用程式上存取相同的訂單，您必須在兩個用戶端中使用 ** 相同的 Mostro Pubkey** 和 ** 相同的 Nostr 中繼器**。請在手機應用程式的 Settings（設定）中檢查這些設定。



![Configuration .env](assets/fr/02.webp)



**步驟 4：安裝**



編譯並安裝 CLI ：



```bash
cargo install --path .
```



編譯需要 1-2 分鐘。`mostro-cli` 可執行檔會安裝在 `~/.cargo/bin/` 中。



![Installation du CLI](assets/fr/03.webp)



**第 5 步：檢查**



檢查一切正常：



```bash
mostro-cli --help
```



您應該可以看到完整的訂單清單。



![Vérification avec --help](assets/fr/04.webp)



#### 在 Linux (Ubuntu/Debian) 上



安裝方式與 macOS 相同，但增加了 .NET Framework：



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



然後按照 macOS 章節中的步驟 3 和 4 進行操作。



#### 在視窗上



首先透過 [rustup.rs](https://rustup.rs/) 安裝 Rust，然後使用 PowerShell ：



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



相同的設定：複製 `.env-sample` 到 `.env` 並填入您的參數。



### 安裝 Mostro Mobile



#### 在 Android 上



**Step 1**：前往 [GitHub 發佈頁面](https://github.com/MostroP2P/mobile/releases) 下載 **app-release.apk** 檔案 (約 65 MB)。



![Page GitHub Releases](assets/fr/10.webp)



**步驟 2：下載完成後，從您的下載區開啟 APK 檔案。Android 會要求您授權從此來源安裝。



![Téléchargement et installation APK](assets/fr/11.webp)



**步驟 3**：遵循介紹功能的上線畫面：




- 自由交易 Bitcoin - 無需 KYC** ：透過 Nostr，交易無需身份驗證
- 預設隱私**：在「聲譽」模式和「完全隱私」模式之間進行選擇
- 每個步驟的安全性**：使用非保管式保留發票提供保護



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Step 4**：繼續上線探索：




- 完全加密的聊天**：端對端加密通訊
- 接受報價**：瀏覽訂購簿並選擇報價
- 找不到您需要的產品嗎？建立您自己的客製化訂單



![Suite onboarding](assets/fr/13.webp)



**步驟5：上線完成後，應用程式會自動生成一對Nostr密鑰。进入菜单（☰）然后**账户**保存你的**密语**（恢复短语）。也是在這個畫面，你可以選擇改變之前提到的隱私模式。



![Menu et sauvegarde des clés](assets/fr/15.webp)



**重要**：將您的復原短語寫在安全的地方 (密碼管理員、紙張保險箱)。



### 初始安全設定



無論您使用何種平台 ：





- 專用金鑰**：使用獨立的 Nostr 身分進行交易
- 小額**：從少於 sats 10,000 開始入門
- 多重中繼**：配置 3-5 個不同地理位置的繼電器
- 網路保護**：啟動 VPN 或 Tor 隱藏您的 IP 位址
- Wallet 安全**：啟動 wallet Lightning 的自動鎖定功能



## 與 CLI 搭配使用



本節依照真實使用案例，示範透過 Mostro CLI 購買比特幣。



### 步驟 1：列出可用訂單



listorders` 指令會顯示所有作用中的訂單：



```bash
mostro-cli listorders
```



您會看到一個表格，裡面有每個訂單的詳細資料：ID、類型（買入/賣出）、金額、貨幣、付款方式。



![Liste des ordres disponibles](assets/fr/05.webp)



在此示例中，透過 Revolut 賣出 5 歐元的訂單可見 (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`)。



### 步驟 2：接受訂單



若要購買這些 bitcoins，請使用 `takesell` 接受訂單：



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro 會要求您提供 **Lightning 發票**，以收取 BTC。以 Satoshis 為單位的確切金額會顯示出來 (這裡：4715 sats)。



![Prise d'ordre de vente](assets/fr/06.webp)



### 步驟 3：提供您的 Lightning 發票



從您的 wallet（Phoenix、Breez 等）產生一張準確數額的 Lightning 發票，然後將它 ：



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



系統會確認出貨，並告訴您在啟動託管之前要等待賣家支付保留發票。



![Envoi de la Lightning invoice](assets/fr/07.webp)



### 步驟 4：聯絡賣家



啟動託管後，使用 `dmtouser` 向賣家索取付款詳細資料：



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### 步驟 5：擷取答案



檢查直接訊息以查看賣家的回應：



```bash
mostro-cli getdm
```



賣家會給您他的付款 ID (這裡是他的 Revtag: `@satoshi`)。



![Réception de la réponse](assets/fr/09.webp)



### 步驟 6：支付法定貨幣



透過協定的付款方式（本例中為 Revolut）將款項發送至所提供的詳細聯絡資訊。 **保留所有證明文件**（截圖、交易參考）。



### 步驟 7：確認付款寄送



付款完成後，請通知 Mostro ：



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### 步驟 8：收到 bitcoins



只要賣方確認收到法幣，並使用 `release` 指令解除託管，您就會立即在您提供的 Lightning 發票上收到您的 bitcoins。



### 步驟 9：評估



為賣家評分，為分散的聲譽做出貢獻：



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### 有用的指令



**取消訂單** (在訂單被接受之前) ：


```bash
mostro-cli cancel -o <order-id>
```



**Create a new sales order** ：


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Open a dispute** ：


```bash
mostro-cli dispute -o <order-id>
```



## 與行動應用程式搭配使用



本節依照真實使用案例，示範透過 Mostro Mobile 銷售 bitcoins。



### Interface 主



本應用程式有 3 個主要索引標籤：





- 訂單簿**：瀏覽可用的買入 (BUY BTC) 和賣出 (SELL BTC) 訂單
- 我的交易**：查看您的有效訂單和歷史訂單
- 聊天**：使用數字與您的交易對手溝通



![Interface principale](assets/fr/14.webp)



### 建議配置



交易前，通過菜單（☰） > **設定**配置一些設定：





- Lightning Address**（可選）：直接接收付款
- 中繼**：新增數個 Nostr 繼電器以提供彈性 (例如 `wss://nos.lol`、`wss://relay.damus.io`)
- Mostro 公鑰**：檢查您使用的 Mostro 實例的公開金鑰



![Paramètres de l'application](assets/fr/16.webp)



**對於 CLI/Mobile 同步化**很重要：如果您同時使用 CLI 和行動應用程式，請在兩個用戶端設定 ** 完全相同的 Nostr 中繼器和 Mostro Pubkey**。如果沒有相同的設定，您將無法在兩個介面上看到相同的訂單。Settings (上述截圖) 中可見的中繼器和 Mostro Pubkey 必須與您 CLI `.env' 檔案中的相符。



### 步驟 1：建立賣出訂單



按下右下方的綠色 **"+"** 按鈕，然後選擇 **SELL**（紅色按鈕）。



![Boutons de création d'ordre](assets/fr/17.webp)



填寫建立表格 ：



1. **貨幣**：選擇您希望接收的貨幣（歐元、美元等）


2. **Amount** ：輸入法幣金額（例如 1 至 3 歐元）


3. ** 付款方式** ：選擇方法 (例如 "Revolut")


4. **價格類型**：選擇 「市場價格」


5. **Premium**：調整溢價（滑桿從 -10% 到 +10%，建議：0% 以快速出售）



按 ** 提交** 發佈您的訂單。



### 步驟 2：出版確認



您的訂單現已公佈！該訂單可使用 24 小時。您可以隨時執行 `cancel` 指令，在買家購買之前取消訂單。



![Ordre publié](assets/fr/18.webp)



訂單會出現在**我的交易**標籤中，狀態為 "Pending「，徽章為 」Created by you"。



### 步驟 3：買家接受您的訂單



當買家接下您的訂單時，您會收到通知。詳情請參閱 **我的交易**。



![Ordre pris par un acheteur](assets/fr/19.webp)



**重要指示**：您現在必須**支付所顯示的保留發票**，以將您的比特幣（4674 sats 代表 1-5 歐元）鎖定在託管中。您最多有**15 分鐘的時間**，否則交換將被取消。



複製保留的發票，並從您的 wallet Lightning (Phoenix、Breez 等) 支付。



### 步驟 4：與買家溝通



啟動託管後，按 **CONTACT** 開啟與買家的加密聊天。



買方（此處為 "anonymous-gloriaZhao"）將聯繫您，要求您提供付款詳情。請回覆您的詳細資料（Revtag、IBAN 等）。



![Chat avec l'acheteur](assets/fr/20.webp)



### 步驟 5：收到法幣付款



等到您的 Revolut 帳戶（或其他協定方式）收到法幣付款。 **仔細檢查**：




- 精確金額
- 寄件者
- 參考資料（如有要求



買家會透過聊天通知您他已經發送款項。Mostro 也會顯示一則訊息，確認法幣已經寄給您。



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### 步驟 6：解除託管



當您確認收到您帳戶上的法幣付款後，請按下綠色的**RELEASE**按鈕，並確認將 Satss 寄給買家。



![Libération de l'escrow](assets/fr/20.webp)



比特幣會透過買方的 Lightning 發票即時轉移給買方。



### 步驟 7：評估考量



放行後，按 **RATE** 為買家評分。選擇 1 到 5 顆星 (這裡是 5/5)，然後按 **Submit Rating**。



![Évaluation de la contrepartie](assets/fr/21.webp)



交換結束！



### 使用手機應用程式購買比特幣



**購買**比特幣的過程與此類似，但相反：



1.瀏覽 ** 訂單簿** > ** 購買 BTC** 標籤，檢視賣出訂單


2.按一下有趣的訂單，以檢視詳細資料


3.按 ** 接受訂單**


4.提供您的 Lightning 發票 (由您的 wallet 產生)


5.等待賣家啟動託管


6.請透過**CONTACT**與賣家聯絡付款細節


7.發送法幣付款（保留憑證）


8.經核實後，賣方解除託管


9.在您的 Lightning 發票上即時接收比特幣


10.為賣家評分 (1-5 顆星)



### 問題管理



**取消訂單**：在**我的交易**中，按下您的訂單，然後按下**取消**按鈕（僅在訂單被接受前可用）。



**開啟爭議**：如果發生爭議，請按下訂單詳細資料中的 **DISPUTE** 。附上所有證據（聊天截圖、銀行交易參考）。



## 優點與限制



### 優點



**財務主權**：由於持有發票機制，您的 bitcoins 永遠不會離開您的直接控制，消除了交易所破產或盜版的風險。



**抗檢查**：任何機關都無法關閉網路或審查您的指令。只要 Nostr 繼電器能運作，系統就能運作。



**預設匿名**：只有假名的 Nostr 金鑰可以識別您的身份，不需要 KYC 或個人資料。端對端加密通訊。



** 付款方式靈活**：可以使用任何雙方都接受的付款方式（轉帳、行動應用程式、現金、易貨）。



### 限制條件



**早期開發**：需要基本的介面和技術學習曲線。



**流動性有限**：訂單數量有限，尤其是大額或稀有貨幣。



**技術要求**：需要基本瞭解 Lightning 和 Nostr。



**個人負責**：遇到問題不需要集中支援，需要小心謹慎。



## 總結



Mostro P2P 結合了 Lightning Network、Nostr 和自動化託管，是真正去中心化交易的選擇。儘管其發展尚早且流動性有限，但該平台已提供金融主權、抗審查性和默認匿名性。



對於偏好自主性與保密性的比特幣使用者而言，Mostro 是值得逐步探索的可行選擇。其分散式架構保證了社群而非商業演進，為未來真正自由的 Bitcoin 交易所鋪路。



## 資源



### 官方文件




- [Mostro 官方網站](https://mostro.network)
- [技術文件](https://mostro.network/docs-english/index.html)
- [Mostro 基金會](https://mostro.foundation)



### 原始碼與開發




- [主 GitHub 儲存庫](https://github.com/MostroP2P/mostro)
- [Web 客戶端](https://github.com/MostroP2P/mostro-web)
- [Customer CLI](https://github.com/MostroP2P/mostro-cli)



### 社區




- [Nostr Protocol](https://nostr.com)
- [Lightning Network 指南](https://lightning.network)