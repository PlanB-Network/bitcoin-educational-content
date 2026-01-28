---
name: Bull Bitcoin Wallet
description: 瞭解如何使用 Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*BTC Sessions 的這段視訊教學將帶您了解設定和使用 Bull Bitcoin Wallet 的過程！* * BTC Sessions 的這段視訊教學將帶您了解設定和使用 Bull Bitcoin Wallet 的過程


本指南將介紹 Bull Bitcoin Wallet 的安裝、配置和使用。您將學習在 Bitcoin On-Chain、Liquid 和 Lightning 網路上傳送和接收資金，以及如何在它們之間移動 Bitcoin。wallet 豐富的功能使其成為管理 Bitcoin 的功能強大的多合一工具。讓我們開始吧


## 簡介


Bull Bitcoin Wallet 由 [Bull Bitcoin](https://www.bullbitcoin.com/)開發，是一款**自我保管**的 Bitcoin wallet，這意味著您可以完全控制您的私人金鑰，因此也可以完全控制您的資金，而無需依賴第三方。此 Wallet 採用開放原始碼並植根於 Cypherpunk 哲學，結合了簡單性、保密性和先進功能，例如跨網路交換和 PayJoin 支援。它可讓您在三個網路中管理您的比特幣： **Bitcoin onchain**、**Liquid** 和 **Lightning**，每個都是針對特定用途量身打造。在 [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) 上，您可以查看目前的主題和即將進行的開發。由於該專案是 100% 開源且「公開建置」，您也可以傳送您的建議和遇到的任何 bug。雖然有些錢包現在支援多個網路，但 Bull Bitcoin Wallet 卻透過深度整合所有網路的隱私權功能而脫穎而出，使其成為在所有主要網路管理您的 Bitcoin 的強大工具。


## 1️⃣先決條件


在您開始使用 **Bull Bitcoin Wallet** 之前，請確定您已備妥下列物品：



- 相容的智慧型手機**：iOS**（iPhone 或 iPad）或**Android**裝置
- 網際網路連線
- 安全備份媒體**：在紙張或金屬上寫下您的**恢復詞組**（12 個字），並將其存放在安全的地方。
- 基本知識**：對 Bitcoin 概念 (位址、交易、費用) 有最低限度的瞭解是有用的，不過本教程會為初學者解釋每個步驟。


## 2️⃣安裝


您可以透過下列方式安裝應用程式：



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(適用於 iOS 裝置)
- [Google Play 商店](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (適用於 Android 裝置)


Android 使用者也有其他選擇：



- 直接從 [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) 頁面下載 APK 或
- 透過與 Nostr 相容的 [Zapstore] 安裝(https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


安裝應用程式後，請跟進歡迎畫面以設定您的帳戶。


## 3️⃣初始配置


開啟時，系統會提示您下列選項：



- 建立新的 Wallet
- 回收 Wallet ` 和
- 進階選項


讓我們先點選「進階選項」。


在這裡，我們可以在建立或復原 wallet 前設定進階設定：


1.啟用 `Tor proxy` 以透過 Tor 網路路由流量。

1.啟用 [Orbot 應用程式](https://orbot.app/en/) 前需要先安裝並執行

2.Tor Proxy 僅適用於 Bitcoin（不適用於 Liquid），可能會導致連線速度較慢。

2.設定「自訂 Electrum Server」，或

3.調整 `Recover Bull` 設定。稍後我們將進一步了解 [Recover Bull](https://recoverbull.com/)。


完成所有選購的調整後，點選 `完成`。如果您想重新使用現有的 Wallet，請點選 `復原 Wallet`，然後填寫復原用語的 12 個字。


否則，請按一下「建立新的 Wallet」。


![image](assets/en/01.webp)


## 4️⃣首頁畫面


在深入了解之前，讓我們先看看「主畫面」，以瞭解其方向：



- 交易總覽」和「設定功能表」位於頂部。
- 可用餘額」有一個隱私選項，可以「開啟」或「關閉」。
- 存取「Bitcoin Bull Exchange」以進行「購買、銷售或付款」（這取決於司法管轄區，可能需要 KYC）。
- 在錢包間轉移資金
- `Secure Bitcoin` 等於 Onchain Bitcoin Wallet
- 透過 Lightning- / Liquid Network 進行「即時付款」 *(註：Bull Bitcoin Wallet 可透過 Lightning 進行付款和收款。由於透過 [*Boltz exchange](https://boltz.exchange/) 的自動交換，透過 Lightning 收到的資金會儲存在 [*Liquid network](https://liquid.net/) (Wallet Instant Payments 中)。這使您能夠與 Lightning 進行互動，而無需管理流動資金渠道，同時保持自我託管。)* *
- 資金的 「發送 」和 "接收


![image](assets/en/02.webp)


首先，讓我們進行一些重要的設定，並從 `Backup` 開始。


## 5️⃣備份


若要開始備份程序，請點選應用程式右上角的 ` 裝備圖示 (⚙)`，然後選擇 `Wallet 備份`。您會看到兩種保護 wallet 的方法：「加密儲存庫」和「實體備份」。讓我們逐一探討。


![image](assets/en/03.webp)


### 實體備份


點選「實體備份」，即可看到代表您的復原或 seed 詞組的 12 個單字清單。請考慮下列內容：



- 謹慎地寫下您的「復原詞句」。寫在紙上或金屬上，並將其保存在安全的地方（保管箱，離線位置）。這個詞組是您在裝置遺失或應用程式刪除時存取比特幣的唯一方法。
- 還要注意的是，任何人只要有這句話，就可以偷走您所有的 bitcoins。永遠不要以數位方式儲存：
- 沒有截圖
- 無雲端、電子郵件或訊息備份
- 無複製/貼上（儲存至剪貼簿的風險）


![image](assets/en/25.webp)


下一個畫面會讓您將字詞以正確的順序排列，以確保您的 seed 詞組正確無誤。測試完成且成功後，您會收到確認訊息。


! **這一點非常重要**。如需更多協助 ：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 加密保險庫


也可以選擇在雲端進行加密的匿名備份。但我們在上一段不是提到雲端備份有風險，應該避免嗎？不過，Bull Bitcoin 團隊已經開發出一種巧妙的方法，讓這個過程變得安全。以下是它的工作原理：


`Recoverbull` 是一個備份協定，透過將備份分割成兩個部分，簡化保護您的 Bitcoin wallet 的安全。首先，您的 wallet 的備份檔案會使用強大的加密金鑰在您的裝置上加密。您可以將這個加密檔案儲存到任何您想要的地方，例如 Google Drive 或您的裝置。其次，解鎖檔案所需的加密金鑰由 Recoverbull 密鑰伺服器儲存。若要復原您的 wallet，您需要同時擁有加密備份檔案和密鑰，您可以使用 PIN 或密碼存取密鑰。這樣的設計可以確保僅有您的雲端備份是無用的，而沒有您的特定備份檔案，僅有密鑰伺服器也是無用的。即使其中一部分受到損害，也能確保您的資金安全。


將它想像成保險箱。加密的備份檔案就是*保險箱*，您可以將其存放在任何地方（如 Google Drive）。您的恢復密碼就是*鑰匙*，由 Recoverbull 密鑰伺服器單獨儲存。小偷需要得到您特定的盒子和特定的鑰匙才能打開盒子。這樣的設計確保了即使有人得到了您的備份檔案，如果沒有伺服器的鑰匙，它也是無用的，而伺服器的鑰匙如果沒有您獨特的備份檔案，也是無用的。


進一步瞭解 `Recoverbull` wallet 備份通訊協定 [在此](https://recoverbull.com/)。


點選 `加密的金庫`，然後點選`繼續`，確認使用預設伺服器。連線將透過 `Tor` 網路，以確保隱私及匿名性。


**瞭解您的 PIN**



- 應用程式解鎖密碼」***:**在「設定 > 安全密碼」中設定的可選密碼，用於鎖定手機上的應用程式。
- `Recovery PIN`**:** 在 `Encrypted Vault` 備份過程中建立的強制性 PIN，用於在復原過程中解密您的備份檔案。


這是兩個不同的 PIN。請勿忘記您的復原 PIN 碼，因為它對於復原您的 wallet 非常重要。


**復原 PIN 設定：**



- 您必須建立 PIN 或密碼才能恢復 wallet 的存取權。
- PIN / 密碼必須至少有 6 位數長（例如，避免使用像 123456 這類不被接受的簡單序列）。
- 沒有這個 PIN，wallet 就無法復原。


接下來，選擇儲存庫提供者：



- Google Drive」或
- 自訂位置」（例如您的裝置）


![image](assets/en/04.webp)


現在，儲存`備份檔案`。接下來，點選`測試復原`，選擇您儲存的備份檔案或儲存庫，然後點選`解密儲存庫`。輸入您的 `PIN` 或 `Password`。如果一切正常，就會出現 `測試成功完成` 畫面。


### 進口/出口標籤


現在我們建立了備份，讓我們來看看「標籤」。  Bull Bitcoin wallet 允許用戶為收款地址和交易創建自定義標籤，從而增強隱私性和組織性。這些標籤可以幫助您將您的資金分類，因為傳送至標籤地址的交易將會繼承該標籤，您也可以為傳出的交易加上標籤以追蹤其變更。wallet 完全支援 [BIP-329](https://bip329.org/) 標準，這表示您可以將所有的標籤匯出到檔案，然後匯入另一個 wallet。此功能可確保您能無縫備份交易歷史和分類，或在不同的 wallet 實體間遷移，而不會遺失個人化的組織。


![image](assets/en/05.webp)


## 6️⃣設定


有了主要備份的安全保障，讓我們來探索設定中的其他可用功能。


### A - 確保存取安全


若要保護應用程式的安全，請導航至 `設定「，然後選擇 `安全 PIN」，以選取 PIN 碼。建立強大的 PIN 碼以鎖定 wallet 的存取權。雖然此步驟是可選的，但我們強烈建議您這樣做，以防止他人使用您的手機時產生未經授權的存取。


![image](assets/en/06.webp)


### B - 連接至個人節點 (選用)


Wallet BullBitcoin 預設連接到 Electrum 伺服器：第一台由 Bull Bitcoin 管理，第二台伺服器來自 Blockstream，這兩台伺服器都被認為不會保留日誌，降低了追蹤的風險。


為了提高保密性，您可以透過 Electrum 伺服器將應用程式連接到您自己的 Bitcoin 節點。若要這樣做，請點選 `設定 ` > `Bitcoin 設定 ` > `Electrum Server 設定 `，然後點選 `+ 新增自訂伺服器 `，輸入您的伺服器位址和憑證。


![image](assets/en/07.webp)


### C - 貨幣


可用餘額會以 `sats` 和 `USD` 顯示在主畫面上。若要變更，請導航至`設定` > `貨幣`。您可以在 `sats/BTC` 之間切換，並選擇您的 `預設法定貨幣`。


![image](assets/en/08.webp)


### D - Bitcoin 設定


Bitcoin 設定」功能表可深入存取 wallet 的核心設定和資料。在這裡，您可以檢視您的「Secure Bitcoin」和「Instant 支付錢包」的基本細節，讓您完全透明和控制。此功能表的主要功能包括



- Wallet 詳細資訊：** 導覽至您的安全 Bitcoin 或即時付款 wallet 以檢視特定資訊。
- Wallet 指紋：** 您 wallet 的唯一識別碼。
- 公開金鑰 (Pubkey)：** 用於 generate 您的 Bitcoin 接收位址的金鑰。
- Descriptor：** 您的 wallet 結構的技術摘要。
- 衍生路徑：** 用於從您的主私人密碼匙 generate 所有位址的特定路徑。
- Address 檢視：** 存取您未使用的收件地址清單，並變更地址（即將推出）。


此外，您還可以選擇



- 啟用自動轉帳」設定可設定 wallet 即時餘額上限，然後會自動轉帳至安全的 bitcoin wallet。
- 透過 `Mnemonic` 語句匯入一般錢包或匯入 `watch-only` 錢包
- 連接「硬體錢包」：目前支援的裝置有 ColdcardQ、SeedSigner、Specter、Krux、Blockstream Jade 和 Foundation Passport。


## 7️⃣ Bull Bitcoin Exchange


從 wallet 直接進入 [Bull Bitcoin 交易所](https://www.bullbitcoin.com/)，讓您無須離開應用程式即可購買、出售和支付 Bitcoin。此整合提供了一個方便的解決方案來管理您的 Bitcoin 需求。請注意，根據您的司法管轄區，存取交易所及其服務可能會受到限制，而且可能需要完成「認識您的客戶」(KYC) 驗證，以符合監管標準和使用平台的完整功能。


若要開始使用，請點選右下角的「Exchange」，然後點選「註冊」或「登入」到您的帳戶。


交易所提供以下 [功能](https://www.bullbitcoin.com/)：



- 從您的銀行帳戶購買 Bitcoin 並自行保管
- 非監護
- 個人或公司
- 即時提款
- 無隱藏費用
- Lightning Network 可用
- 無交易限制
- 重複購買選項


![image](assets/en/09.webp)


若要瞭解更多資訊，請造訪本教學：


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣接收資金


使用 **Bull Bitcoin Wallet** 收取資金既簡單又靈活，可支援三種針對不同使用情況量身打造的網路：



- Bitcoin (onchain)」網路用於安全的長期儲存。
- `Liquid` 網路可進行快速、更機密的交易。
- 提供即時、低成本付款的「Lightning」網路。


應用程式會根據您選擇的網路自動產生適當的地址或發票。以下是每個網路的操作方法。


### 透過 Onchain (Bitcoin 網路) 接收


要接收 on-chain 資金，您可以從主畫面點選 `Secure Bitcoin Wallet`，然後點選 `Receive`，或點選主畫面的 `Receive` 按鈕，然後選擇 `Bitcoin network`。


您有兩種產生接收位址的主要模式：


** 預設模式 (URI 含額外輸入參數)


預設情況下，wallet 會產生 [BIP21 URI](https://bips.dev/21/)。這是一種標準化格式，包裝了比簡單地址更多的資訊，包括金額、個人備註和 PayJoin 參數，以提高隱私性。這個全面的 URI 會編碼成 QR 碼，並可供複製。格式如下`bitcoin:<地址>?<參數1>=<value1>&<參數2>=<value2>`。



- 其他輸入參數：**
    - 金額：** 以 BTC、sats 或法定貨幣指定要求的金額。
    - 訊息：** 新增寄件者可看到的個人備註。
    - PayJoin:** 啟用此選項可結合交易中寄件人和收件人的輸入，以改善隱私。


範例 URI：


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*重要提示：請不要向本教程中的地址發送任何資金，wallet 將被刪除。


![image](assets/en/10.webp)


**僅啟用複製或掃瞄 Address 選項


啟用「僅複製或掃描 Address 選項」後，應用程式會以 SegWit (bech32) 格式產生簡單的 Bitcoin 位址。


範例：


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


即使您輸入金額或備註，它們也不會包含在 QR 碼或複製的地址中。


![image](assets/en/11.webp)


### 透過 Liquid Network 接收


您可以在 Liquid Network 上接收付款。進入「接收」畫面後，您有相同的兩個選項可產生付款請求：


**1.簡單的 Address：** 複製標準的 `Liquid 位址`。這是您的 wallet 在 Liquid 網路上的唯一識別碼，不包含任何特定金額或訊息。


範例 Address：


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2.詳細付款請求 (URI)：** 若要提出更有系統的請求，您可以指定金額和個人備註。此資訊會自動編碼為可分享的 URI 及其對應的 QR 代碼。



- 金額：** 您可以 Bitcoin (BTC)、Satoshis (Sats) 或法定貨幣設定金額。
- 註：** 加入個人訊息以識別交易。


**URI 示例：**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


要完成交易，請向寄件人提供「地址」或「URI」。您可以將它複製到剪貼簿，或讓他們直接從您的螢幕掃描 QR 代碼。


![image](assets/en/12.webp)


### 透過 Lightning 接收



Bull Bitcoin Wallet 也可讓您透過 Lightning Network 收發付款。其主要特點是透過 Lightning 收到的資金會自動交換並儲存在您的 `Instant Payments Wallet` 內的 `Liquid Network`。這項服務由 `Boltz`提供。這種設計使您能夠享受 Lightning 的速度和低成本，而無需管理流動資金渠道的複雜性，同時保持您資金的完全自我託管。雖然這種混合方法是自我託管，避免了管理渠道的複雜性，但它引入了第三方服務（Boltz），小額的交換費，並依賴Liquid Network的功能聯盟作為關鍵持有人，這與傳統的非託管Lightning wallet不同，您可以管理自己的渠道。您可以在此瞭解更多關於 Liquid 及其管理模式的資訊：


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- 限制：**
    - 最低金額：** 需要最低發票金額。請在應用程式中查看當前限額
    - 費用：** 您，即收款人，需承擔少量的交換費用。此費用會從寄件者的轉帳金額中扣除，且可能會有所變動。
- 福利：**
    - 自我監護：** 您的資金永遠在您的控制之下，並在 Liquid 網路上受到保護。
    - 避免高昂的 On-Chain 費用：** 透過使用 Lightning 並儲存於 Liquid，您可避開開啟傳統 Lightning 通道所需的 on-chain 費用。您可以選擇稍後將資金轉移到 on-chain 通道，當累積金額足以支付費用時。
    - 提示：** 若要在兩個 Bull Bitcoin 使用者之間進行最具成本效益的交易，請直接使用**Liquid 網路**，以完全避免 Lightning 交換費用。


若要收到付款，您必須 generate 領取「Lightning 發票」：


1.`Enter an Amount`**:** 指定您希望以 Bitcoin (BTC)、Satoshis (Sats) 或法定貨幣接收的金額。

2.添加備註 `**（可選）：** 包含備忘或備註。這將會內嵌在發票中，並在付款完成後顯示在您的交易記錄中，讓您更容易識別。

3.`Invoice有效期`**:**「閃電 」發票具有時效性，在**12小時**後失效。如果在這段時間內沒有付款，它就會無效，您需要 generate 新的發票。


將發票複製到剪貼簿，或讓寄件人掃描顯示在螢幕上的 QR 代碼，即可向寄件人提供發票。


![image](assets/en/13.webp)


## 9️⃣寄送資金


您可以直接從首頁或任何錢包中存取傳送畫面。Bull Bitcoin Wallet 可根據您輸入的地址或發票（無論是貼上或透過 QR 碼掃描）自動偵測目的地網路 - `Bitcoin`、`Liquid` 或 `Lightning`，從而簡化流程。


### On-Chain 透過 Bitcoin 網路傳輸


發送資金 on-chain 表示您的交易直接記錄在 Bitcoin 區塊鏈上。此方法最適合較大額的轉帳或非時間敏感的轉帳。開始時，您可以點擊右下方的「傳送按鈕」，掃描或輸入一個「標準 Bitcoin 地址」。


如果您提供的地址不包括具體金額，則會在發送螢幕上提示您填寫詳細資訊。您可以用自己喜歡的單位指定金額，例如 BTC、薩托希或等值的法幣。您還可以選擇添加個人備註，這是供您自己參考的私人備忘，有助於您日後識別交易。此備註不會與收款人分享。


相反，如果您掃描或貼上的付款請求已包含所有必要的詳細資訊，例如預先定義金額的 BIP21 URI，wallet 將會繞過資料輸入畫面，直接帶您到確認畫面授權付款。


![image](assets/en/14.webp)


在播放交易之前，您會看到一個確認畫面。請花一點時間仔細查看每項參數，密切注意收件人地址、傳送金額和網路費用，這一點非常重要。這個畫面也提供了強大的工具來自訂您的交易。


您可以用兩種主要方式控制費用。第一種方法是選擇所需的交易速度，例如低、中或高，wallet 會自動為您計算適當的費用。第二種方法可讓您更精確地控制，讓您設定特定的費用，可以是以 Satoshis 為單位的絕對總額，也可以是以每個位元組為單位的相對費率，然後提供估計的確認時間。


對於進階使用者，wallet 提供多種設定來微調交易。預設啟用了 `Replace-by-Fee` (RBF)，這是一項很有價值的功能，當交易卡在 mempool 時，可以用較高的費用重新廣播，加速交易。您也可以手動選擇要花費的「未花費交易輸出」(UTXOs)。這是 UTXO 整合的強大工具，這是一種將多個小投入合併為一個較大投入的策略。雖然這可能會增加目前交易的費用，但可以大幅降低未來交易的費用，尤其是當網路費用預期會增加時。


![image](assets/en/15.webp)


當您掃描收件人的付款請求 (BIP21 URI) 且其中包含 `pj=` 參數時，系統會自動嘗試 PayJoin。如果您只是貼上沒有額外參數的純地址，此功能將不會啟動。這種協作方法透過結合寄件者和收件者的輸入來增強隱私，打破了共同輸入擁有的啟發式，在某些情況下也能有更好的擴展性和節省費用。


### 傳送至 Liquid Network


Liquid Network`專為快速、保密的交易而設計，費用極低。當您透過 Liquid 傳送資金時，資金會從您的 `Instant Payments Wallet` 中提取。過程簡單直接：您只需輸入或掃描收件人的`Liquid 地址`。


如果地址未指定金額，則會要求您在發送螢幕上提供金額。您可以輸入 BTC、Satoshis 或法幣金額。Liquid 的一個關鍵優勢是其最低門檻很低。與 on-chain 交易一樣，您可以添加可選的個人備註，以作記錄。如果付款請求已包含金額，wallet 將直接進入確認畫面。


在 Liquid 交易的確認畫面中，您將查看詳細資訊。費用顯然很低，根據交易的複雜程度來計算。費用通常約為 0.1 Sat/vB，對於簡單的交易而言，僅需 20-40 Satoshis（例如，截至 2025 年 12 月 21 日為 26 Satoshis）。


![image](assets/en/16.webp)


### 傳送至 Lightning Network


您可以掃描 Lightning Address（例如 `runningbitcoin@rizful.com`），它可讓您設定金額和收件人的選項備註，或者掃描預先定義金額的發票，它可讓您直接進入確認畫面。


*請注意，最低金額和費用適用。


Bull Bitcoin Wallet通過從您的`Instant Payments Wallet`（Liquid上）提取資金並通過`Boltz`進行交換來發送閃電付款。這種混合方式可完全自行保管，並避免管理專用 Lightning 通道所需的高昂 on-chain 費用，但需要支付「交換費用」。若要成本最低，可直接發送至收件人的 Liquid 位址，如果他們也使用 Bull Bitcoin wallet。


## 在您的錢包間轉移資金


Bull Bitcoin 允許您在 Liquid Network 上的 `Secure Bitcoin` wallet 和 `Instant Payments Wallet` 之間轉移您的 Bitcoin，或轉移到 `外部 Wallet`。若要執行轉帳，只需導航至`轉帳`部分，選擇來源和目的地錢包，輸入您要轉帳的金額，然後確認交易。


![image](assets/en/17.webp)


## 1️⃣ 1️⃣恢復您的 Bull Bitcoin Wallet


本節說明如果您遺失裝置、卸載應用程式，或只是需要切換到一個新的裝置，如何重新取得您的 Bull Bitcoin Wallet 資金。如前所述，有兩種主要的恢復方法：使用獨特的「Recoverbull」方法和使用標準的「BIP39 seed phrase」。


### 方法 1：恢復公牛


重溫：Wallet 備份會在本機加密。加密後的檔案可儲存於雲端儲存空間，或其他裝置上。加密密鑰由 Recoverbull 密鑰伺服器儲存。兩者是分開保存的，必須結合起來才能復原 wallet。


首先，我將刪除 Wallet 及其上的所有資金，然後再重新安裝 wallet。我們會再次進入「歡迎畫面」。這次，請選擇「恢復 Wallet」選項。然後，導覽到 `加密金庫` 方法，確認使用 `預設金鑰伺服器`，並選擇您儲存備份檔案的位置或 `金庫提供者`。


![image](assets/en/18.webp)


表示儲存庫已成功匯入。點選 `Decrypt Vault` 按鈕，然後輸入 `PIN` 。下一個畫面會顯示您的`結餘`和已復原的`交易筆數`。


![image](assets/en/19.webp)


### 方法 2：種子短語


此方法使用 wallet 的主恢復詞組，這是一個標準的 12 個字清單，可作為您資金的最終備份。這是恢復 Bitcoin wallet 最通用的方法，因為它與任何特定服務或伺服器無關。只要您有這個詞組，您就可以在任何相容的裝置上復原您的 wallet，即使無法存取 Bull Bitcoin 金鑰伺服器也沒問題。


從「歡迎」畫面，選擇「復原 Wallet」。這次請選擇 ` 實體備份 ` 方法。應用程式會顯示一個單字方格。按照正確的順序仔細選擇 12 個 seed 詞組中的每個單詞。請務必仔細，因為任何一個錯誤都會造成錯誤的 wallet。


## 1️⃣ 2️⃣連接 Hardware Wallet


為了獲得最高等級的安全性，許多 Bitcoin 使用者選擇將他們的資金儲存在「冷儲存」中。這表示將控制 Bitcoin 的「私密金鑰」儲存在絕不連接網際網路的裝置上。硬體 wallet（或簽署裝置）是專門為此目的而設計的實體裝置。它就像是您金鑰的數位保險庫，可確保金鑰永遠不會受到線上電腦或智慧型手機的潛在威脅。


透過將硬體 wallet 連接到 Bull Bitcoin 應用程式，您可以獲得兩者的最佳結合：冷凍儲存為您的私人密碼匙提供絕對的安全性，並結合 Bull Bitcoin wallet 的強大功能和友善介面，方便您檢視餘額和管理交易。在最後一章，我們將教您如何連接硬體 wallet，例如 [Coldcard Q](https://coldcard.com/q)，到您的 Bull Bitcoin wallet。本教學不會深入介紹如何設定 Coldcard Q，您可以在此瞭解：


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### 匯入 Wallet


![image](assets/en/26.webp)


首先，從 Coldcard Q 的主功能表中選擇 ` 匯出 Wallet`，然後選擇 ` 公牛 Wallet`。您的 Coldcard 將會 generate 一個 QR 碼。


![image](assets/en/20.webp)


開啟 Bull Bitcoin Wallet，並導覽至「設定」>「Bitcoin 設定」>「匯入 wallet」，然後選擇手機上的「Coldcard Q」，點選「開啟相機」掃瞄此 QR 碼，即可匯入硬體 wallet 的公開金鑰。


![image](assets/en/21.webp)


### 使用 Coldcard Q 收件


若要使用已連接的 Coldcard Q 接收 Bitcoin，您不需要將裝置實際連接到您的手機。Bull Bitcoin Wallet 已經匯入必要的公開金鑰，讓它可以自行 generate 位址。


1.點選您已匯入的 Coldcard Q 簽章裝置，然後選擇 `接收`。

2.應用程式會自動從 Coldcard 的 wallet 顯示新的 Bitcoin 位址。

3.使用此地址接收資金。Bitcoin 會直接固定到硬體 wallet 的金鑰，即使在過程中裝置是離線的。


![image](assets/en/22.webp)


### 使用 Coldcard Q 傳送


使用 Coldcard Q 傳送 Bitcoin 需要您的實體確認，才能授權任何交易。雖然 Bull Wallet 應用程式可用來建立交易，但最終簽章只能在硬體 wallet 本身上建立。


首先，打開您的「Coldcard Q」wallet，點選「傳送」。然後，`打開相機`掃描接收地址的 QR 碼。掃描後，輸入您要傳送的`金額`，並視需要調整`費用優先順序`。


如需更多選項，您可以在 Advanced Settings（進階設定）下查看。在這裡您可以找到 `Replace by Fee` (RBF) 選項，預設為啟動，可讓您稍後加快卡住的交易。您也可以使用 `Coin Control` 選項，讓您手動選擇想要花費的特定 UTXO。


檢視所有詳細資料後，點選 `Show PSBT` 準備交易。


![image](assets/en/23.webp)


點選 Coldcard Q 上的「掃瞄」按鈕，使用其相機掃瞄手機上顯示的 QR 代碼。Coldcard 畫面隨即會顯示所有交易詳細資訊。仔細核實金額、收件人地址和您的變更地址。如果一切無誤，請按下 Coldcard Q 上的「Enter」鍵簽署交易。接下來，螢幕上會出現已簽署交易的 QR 代碼。


![image](assets/en/24.webp)


在 Bull wallet 上，點選`我完成了`，然後點選`相機「按鈕，從您的 Coldcard Q 掃描`已簽署交易」的 QR 代碼，Bull Wallet 現在會顯示已簽署交易的摘要畫面。最後檢視一次，然後點選 ` 廣播` 交易。這將完成交易傳送至 Bitcoin 網路的程序，您的資金就會到帳了。


## 🎯 結論


現在您已完成 Bull Bitcoin Wallet 之旅。此應用程式將強大的隱私與安全工具放在您的指尖，讓進階功能簡單易用。它可透過「PayJoin」（隱藏您在區塊鏈上的交易）和「Tor 整合」（遮掩您的網路活動，使其不被窺視）等功能幫助您保持隱私。對於想要終極控制的人，您可以連接到「自己的個人 Bitcoin 節點」，以停止依賴第三方伺服器，並使用「硬體 wallet 」來保持您的私密金鑰完全離線和安全。Bull Bitcoin Wallet 具備智慧型備份選項，並可無縫支援 Bitcoin、Liquid 和 Lightning，對於任何認真維護資金私密性、安全性，並完全由自己掌控的人而言，Bull Bitcoin Wallet 是強大的多合一選擇。


## 公牛 Wallet 資源


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)