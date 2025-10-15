---
name: Cashu.me
description: Cashu.me ecash 使用指南
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*以下是 BTC Sessions 的視頻教程，該視頻指南將教您如何設置和使用 Cashu.me Bitcoin Wallet，它可以讓您訪問簡單、便宜和私人的 Bitcoin 交易 - 無需應用程序商店！ *


在本教程中，我們將探討 Cashu.me，一個使用 Chaumian ecash 進行私人 Bitcoin 支付的瀏覽器型 Wallet。在開始之前，讓我們先簡單介紹一下 ecash 及其運作方式。


## ecash簡介


想像一下，您口袋中的數位現金與實體鈔票運作方式一模一樣 - 私密、即時、點對點無中介可用。這就是 ecash 所能實現的功能：一種將實體現金的隱私性帶回數位世界的數位付款方式。onchain-Bitcoin會將每筆交易記錄在任何人都能看見的公開Ledger上，ecash則不同，它創造私人代幣，代表真正的Bitcoin價值，同時讓您的消費習慣保密。


將 ecash 視為儲存在您裝置上的數位不記名工具 - 如果您持有它們，您就擁有它們，就像實體現金一樣。這些代幣是由持有底層 Bitcoin 儲備的可信賴服務「Mints」所發行。當您使用 ecash 時，您不會向整個網路廣播您的交易。相反地，您是直接與他人交換私人代幣，創造出一種付款體驗，感覺上更像是將現金交給他人，而不是傳統的數位付款。


Cashu 是為 Bitcoin 建立的免費開源 Chaumian ecash 協定。該技術以 David Chaum 在 1980 年代開創的加密研究為基礎，使用「隱蔽簽署」來確保隱私。當您收到 ecash 代幣時，鑄幣廠會在不知道代幣下一步會用在哪裡的情況下簽署代幣 - 這是防止交易追蹤的重要功能。重要的是，ecash 並沒有取代 Bitcoin，而是透過解決 Bitcoin 架構需求的一些關鍵問題來補充 Bitcoin。它提供實體現金所能提供的隱私權 (Bitcoin 的透明 Ledger 所缺乏的)，並可立即進行微交易，而無需 Blockchain 費用或確認延遲。


Ecash 可與 Lightning Network 無縫整合。您可使用 Lightning 將 Bitcoin 存入造幣廠 (將您的 Bitcoin 價值轉換為 ecash 代幣)，稍後再提款 (將代幣轉換回可供消費的 Lightning 結餘)。兩者共同形成強大的組合：Bitcoin 提供安全的結算 Layer，Lightning 可實現快速交易與網路互通性，而 ecash 則增加了隱私權 Layer，讓數位付款再次感受到真正的隱私。


## Cashu.me


Cashu.me是一個 "Progressive Web App (PWA)"，它實現了Cashu協定--專為Bitcoin設計的Chaumian ecash的特定實現。作為一個 PWA，它可以直接在您的瀏覽器中運行，而不需要從應用程式商店中安裝，不過您也可以將其安裝到您的設備中以方便存取。這種以網頁為基礎的方式可確保各種作業系統之間的廣泛相容性，同時透過加密協定而非平台限制來維護安全性。


## 主要功能


讓我們深入了解其功能，探索 Cashu.me 所提供的服務：



- Lightning 上的 Chaumian ecash**：使用盲簽名，因此造幣廠無法追蹤使用者餘額或交易記錄
- 自行保管代幣**：您使用 seed 短語在本機控制 ecash 代幣
- seed 詞組備份**：用於 Wallet 恢復的 12 個字元恢復詞組
- Mint 獨立性**：可與多個獨立的造幣廠合作，您不會被鎖定在一個供應商身上
- 即時、免費交易**：在同一個造幣廠內，付款在數秒內完成，零費用
- 隱私保護架構**：鑄幣商看不到誰與誰交易
- 離線 ecash**：透過本地傳輸通訊協定 (如 NFC、QR code、藍牙等) 傳送/接收代幣，無需網際網路連線
- 透過 Nostr 發現 ecash 鑄幣商**：透過 Nostr 通訊協定尋找並驗證可信鑄幣商
- 在造幣廠之間交換ecash**：所有鑄幣廠都會說 Lightning，這表示您可以在它們之間轉移價值。
- 使用 Nostr Wallet Connect (NWC)** 遙控您的 Wallet：連線至其他應用程式，例如 Nostr Client，並透過 NWC 開始 Zapping


關鍵的權衡是 「信任」：當您控制代幣本身時，您必須信任造幣廠來保管基礎 Bitcoin 儲備。正如 Cashu 的文件所述：


> ......造幣廠正在執行 Lightning 基礎架構，並為造幣廠的 ecash 使用者保管 Satoshis。用戶必須信任鑄幣廠，當他們想要轉換到 Lightning 時，鑄幣廠才會 Redeem 他們的 ecash。

- 卡舒文件，[一般安全與隱私權問題](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


這使得 ecash 成為 Bitcoin 本身的託管解決方案，雖然您仍保留代幣的完全控制權。


## 1️⃣初始設定


① 首先在瀏覽器中訪問 [Wallet.cashu.me](https://Wallet.cashu.me)。由於Cashu.me是一個`PWA`，您不需要從應用程式商店下載，只需直接在瀏覽器中打開網站即可。為了更方便訪問，您可以選擇將其安裝到您設備的主屏幕上。


要安裝 PWA，請點擊瀏覽器中的⋮菜單按鈕，然後選擇 「添加到主屏幕」。安裝完成後，關閉瀏覽器標籤，然後從裝置的主螢幕啟動 Cashu.me。在歡迎畫面中，點擊`下一步`繼續。


③ 安全是關鍵。將您的 seed 詞組安全地儲存在密碼管理器中，或者最好寫在紙上。如果您無法存取本裝置，這 12 個字的恢復短語是您恢復資金的唯一方法。點選 👁️ 圖示以顯示您的 seed 詞組，依序仔細寫下所有 12 個字，然後勾選標示「我已寫下」的方塊。點選「下一步」繼續，並勾選方格確認您接受以下畫面的「條款」。


![image](assets/en/01.webp)


完成設定後，您需要連線到`Mint`。點擊 `ADD MINT` 後面的 `DISCOVER MINTS` 查看 Nostr 社群推薦的鑄幣。為了額外的驗證，您可以在 [bitcoinmints.com](bitcoinmints.com) 檢視造幣廠的評級。


接下來點選「點選瀏覽薄荷糖」以查看完整清單。複製薄荷糖的 URL，將其貼入 URL 欄位，並為其命名。在這個範例中，我們將使用


URL：`https://mint.minibits.cash/Bitcoin`

名稱：Minibits


![image](assets/en/02.webp)


點選 `ADD MINT` 完成程序。在確認畫面中，確認您信任此薄荷糖的操作者，然後再點選 `ADD MINT`。Minibits 鑄幣現在就會出現在您的主螢幕上。一旦您的 Wallet 設定完成，您需要在進行交易前為其注資。


![image](assets/en/03.webp)


## 2️⃣資助您的 Wallet


Cashu.me提供兩種不同的方法來為您的Wallet注資。當您點擊主畫面的 「接收」，您會看到通過 "ECASH 「或 」LIGHTNING "接收資金的選項。


![image](assets/en/04.webp)


### 透過 LIGHTNING 融資


第一個選項是透過 Lightning Invoice 撥款給 Wallet。如果您添加了不同的鑄幣廠，請選擇鑄幣廠，並定義您想要收到的 「金額 (Sats)」。然後點擊 「創建Invoice. 」現在你會得到一個QR碼，你可以用另一個閃電Wallet掃描，或者你可以簡單地 「複製 」Invoice並粘貼到另一個Wallet來支付和注資你的cashu.me Wallet。


![image](assets/en/05.webp)


### 接收電子現金


ecash 方法可讓您直接從另一個 ecash Wallet 接收代幣。首先點選`接收`按鈕，然後選擇`ecash`選項。您將能夠`貼上`或`掃描`或使用`NFC`從另一個 Wallet 提交 Cashu token。如果您選擇貼上，輸入您從其他 Wallet 複製的 token 字串，`Amount`和`Mint`會自動顯示。點選 `RECEIVE` 完成交易，Sats 將出現在您的 Wallet 中。請注意，您的餘額現在分佈在多個鑄幣上。例如，您的 Minibits `Mint`中可能有 1,000 Sats，而 Coinos `Mint`中可能有另外 1,000 Sats。這種在不同造幣廠之間的分離是 Cashu 架構的一個重要方面。


![image](assets/en/06.webp)


### 交換薄荷糖


如果您不再信任您添加的某個造幣廠，cashu.me 提供了一個功能，可以將您的資金從一個造幣廠 「交換 」到另一個造幣廠。導航到造幣廠標籤，向下滾動，直到您看到 "Multimint Swaps"。從下拉式功能表中選擇 "FROM 「和 」TO"，並輸入您要轉移的金額。點選 `SWAP`，在造幣廠之間轉移代幣。這將透過 Lightning 交易執行，因此您需要預留空間以支付潛在的 Lightning 費用。在我的範例中，1 sat 已經足夠。


![image](assets/en/07.webp)


## 3️⃣寄送資金


要發送 Sats，Cashu.me 提供了兩個選項。通過 "ecash 「或 」lightning "發送。讓我們來看看這兩個選項。


### 透過 Lightning 傳送


若要透過 Lightning 傳送，請遵循下列步驟：


1.點選主畫面上的 `SEND` 並選擇 `Lightning

2.應用程式會提示您輸入 `Lightning Invoice` 或 `Address`。您可以直接貼上 Invoice/Address，或使用掃描 QR 碼選項以目視方式擷取，然後以 `ENTER` 確認。

3.使用下拉式欄位選擇您要付款的 Mint，然後點選 `PAY` 確認。 **註**： 在 `設置 ` -> `實驗 `下也有使用 `Multinut`的選項，可讓您一次支付來自多個 Mints 的發票。

4.成功完成後，您會看到付款確認以及從餘額中扣除的金額。


![image](assets/en/08.webp)


### 透過 ecash 傳送


傳送 ecash 也同樣簡單直接。


1.點選「傳送」，這次選擇「ECASH」選項。

2.選擇一個薄荷糖，然後在 Sats 中輸入您要發送的 「金額」，然後點觸 「發送 」確認。

3.這會建立一個您可以調整速度和大小參數來自訂的「動畫 QR Code」。任何人都可以掃瞄此 QR 碼立即 Redeem Sats，或者您也可以點選 COPY，透過藍牙、NFC 或標準訊息等其他管道將 token 字串傳送給其他人。

4.開啟另一個 Wallet。從剪貼簿貼上，然後在另一個 Wallet 中選擇`Receive ecash`。


![image](assets/en/09.webp)


## 4️⃣附加功能


除了核心的傳送和接收功能外，Cashu.me 還提供強大的附加功能，可提升您在 Nostr 生態系統中的 Bitcoin 體驗。


### Nostr Wallet 連線


Nostr Wallet Connect (`NWC`)透過在您的 Wallet 與社交應用程式之間建立無縫連接，改變您與 Nostr 應用程式的互動方式。此協定可讓 [Damus](https://damus.io/) 或 [Primal](https://primal.net/home) 等應用程式直接透過 Nostr 中繼要求付款，而無需您離開應用程式。


在 Cashu.me 中設定 `NWC`：


1.移至左上方漢堡選單中的 ` 設定

2.捲動至「NOSTR Wallet CONNECT」部分，然後點選「啟用」按鈕

3.然後，您會設定一個零用錢，以建立應用程式可以從 Wallet 花費的最高金額。

4.設定完成後，您可以複製連線字串並貼到任何支援「NWC」的 Nostr 用戶端，以啟用即時斬件和小費功能。


![image](assets/en/10.webp)


### Lightning Address via npub.cash


Cashu.me與[npub.cash](https://npub.cash/)整合，為您提供與Nostr協議無縫配合的Lightning Address。在這裡，您可以註冊並通過提供您的 Nostr `nsec` 領取您的用戶名，費用為 5,000 Sats 並支持 npub.cash 項目，您也可以使用任何 Nostr 公鑰 (`npub`)，無需註冊。


首先，進入 `設定` 並點選 `啟用`使用 npub.cash 的 Lightning Address。這將 generate 一個 npub.cash Address，預設使用從您的 Wallet seed 詞組衍生的 `npub` 字串。


或者，請造訪 [此網頁](https://npub.cash/username)，使用您自己的 Nostr `nsec` 領取自訂使用者名稱，讓您擁有個人化的 Lightning Address，就像 username@npub.cash。


![image](assets/en/11.webp)


## 🎯 結論


Cashu.me 提供私人 Bitcoin 付款，其功能就像實體現金一樣 - 即時、點對點，不會暴露您的交易歷史。我個人很欣賞它的 PWA 架構，因為它的運作不受應用程式商店的限制。透過結合 Bitcoin 的安全性、Lightning 的速度以及 ecash 的隱私性，Wallet 提供的使用案例可提升日常 Bitcoin 的採用率。


當您透過自我保管完全控制您的 ecash 代幣時，請記住鑄幣廠是可信賴的第三方，持有底層的 Bitcoin 儲備。使用多個鑄幣廠並在它們之間交換的能力，在保持隱私的同時提供了靈活性。


由於具有 NWC 和 npub.cash 位址等功能，Cashu.me 對於重視隱私和主權而非大型科技政策限制的社群客戶而言，是一個吸引人的 Wallet 選項。


## 資源


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)