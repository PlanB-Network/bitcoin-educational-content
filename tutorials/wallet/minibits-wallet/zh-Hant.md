---
name: Minibits Wallet
description: Minibits Wallet 指南
---

![cover](assets/cover.webp)


在本教程中，我將引導您設定 Minibits Wallet 以使用 ecash。與 Bitcoin 同時運作的強大隱私為重點的付款技術。Minibits 是一種 ecash 與 Lightning Wallet，可實現即時、便宜且私密的價值轉移，非常適合注重隱私的日常交易。


在我們深入研究 Minibits 之前，讓我們先清楚了解何謂 ecash。很多人將 ecash 與 Bitcoin 或 Blockchain 技術混淆，但它們根本是不同的概念。


Ecash 不是 Bitcoin。它不會取代您自我監護的 Bitcoin Wallet，而是對它的補充。Ecash 不是 Blockchain，也不存在於任何公共 Ledger。有趣的是，Ecash 並不是一項新技術 - 它其實早於全球資訊網，其概念在 1980 和 1990 年代就已發展。


ecash 是什麼：令人難以置信的私密性 (交易不會留下任何可追蹤的歷史)、點對點 (直接轉帳，無需中介)，以及數位不記名工具的功能 (如果您擁有它，您就能控制它)。其主要優勢在於 ecash 可以離線使用 - 無論是寄件者或收件者，都可以在交易期間中斷網路連線。Ecash 可由單方或可信實體聯盟鑄造，是 Bitcoin 的完美補充技術，可處理小型、頻繁的交易，而 Bitcoin 則可作為結算 Layer。


請注意，此 Minibits 設定代表「託管解決方案」，這表示您信任 Mint 營運商管理您的資金。這會帶來特定風險，您必須在進行之前瞭解。


本專案顯示此重要的免責聲明：


- 本 Wallet 應僅用於研究目的。
- Wallet 是測試版，功能不完整，有已知和未知的錯誤。
- 請勿與大量的 ecash 一起使用。
- Wallet 中儲存的 ecash 由鑄幣廠發行。
- 您相信鑄幣廠會用 Bitcoin 支持它，直到您將持有的 Bitcoin 轉換成另一個 Bitcoin Lightning Wallet。
- Wallet 所執行的 Cashu 協定尚未經過廣泛的審核或測試。


將 Minibits 當作日常 Wallet，而不是儲蓄帳戶，切勿在此儲存大量價值。


## 1️⃣設定您的 Wallet


首先，請造訪 [Minibits 網站](https://www.minibits.cash/)，您可以找到所有主要平台的下載選項。iOS 使用者可以從 [App Store](https://testflight.apple.com/join/defJQgTD) 下載，而 EU iOS 使用者則可以額外選擇從 [Freedom Store](https://freedomstore.io/) 安裝。Android 使用者可從 [Google Play 商店](https://play.google.com/store/apps/details?id=com.minibits_wallet) 下載應用程式，或直接從 [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases) 頁面下載 APK 檔案。


安裝 Minibits 時，您會看到解釋基本概念的介紹畫面，您可以閱讀這些畫面，如果您已經熟悉這項技術，也可以跳過這些畫面。完成這些初始步驟後，系統會提示您在以下兩者中選擇：


- 新使用者可使用`Got it, take me to the Wallet` 或`Got it, take me to the Wallet`。
- 復原遺失的 Wallet`，如果您要從備份還原。


![image](assets/en/01.webp)

完成初始設定後，您會進入主畫面，其中有幾個重要的 Elements 需要注意。① 上角的個人資料圖示會帶您進入個人資料頁面，您可以在此存取您的 Minibits Wallet Address 並選擇「批次接收」選項。② 在螢幕中間，您會看到可以使用的薄荷糖，預設選取 Minibits 薄荷糖。下面的動作行提供了發送 ecash 或閃電付款、掃描 QR 代碼和接收付款的選項。最後，底部導覽列包含通往主畫面、交易記錄、聯絡人和設定的捷徑。


![image](assets/en/02.webp)


## 2️⃣管理薄荷糖


根據預設，當您啟動應用程式時，會啟用 Minibits 造幣。然而，ecash 的強項之一是可以使用多個鑄幣以增加分散性和安全性。若要新增另一個鑄幣，請導航至「設定」，然後選擇「管理鑄幣」，最後點選「新增鑄幣」。


[Bitcoinmints.com](Bitcoinmints.com)提供了一個全面的可用鑄幣廠列表，並附有用戶評級，幫助您選擇有信譽的選項。使用多個鑄幣廠可以降低您的風險。如果一個鑄幣廠出現問題，您在其他鑄幣廠的資金仍然可以使用。


![image](assets/en/04.webp)


## 3️⃣建立備份


備份可以說是整個設定過程中最關鍵的步驟。若要存取備份選項，請導航至 `設定 `-> `備份 ` 在這裡您會找到兩個重要選項：

1.您的 seed 詞組」包含「12 個單字」，可讓您在裝置遺失時恢復您的 ecash 結餘。這個 seed 詞組是您在所有已加入的鑄幣廠存取所有 ecash 的主密碼。請將它寫在實體媒體 (紙張或金屬) 上，並將它安全地儲存在多個位置。切勿以數位方式儲存您的 seed 短語，因為它可能會外洩。請考慮瀏覽此 [教學](https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) 以獲得保護您的 Wallet 的最佳做法。

2.包含長備份字串的 `Wallet backup`。


**注意**：使用此備份來復原 Wallet 時，您仍需要 seed 的短語。


![image](assets/en/05.webp)


## 4️⃣ 創建 Minibits Wallet Address


接下來瀏覽底部的`聯絡人`，然後點選`變更`->`變更 Wallet Address`，自訂您專屬的`Minibits Wallet Address`。輸入您偏好的 Address 並檢查可用性。


![image](assets/en/07.webp)


設定您的 Address 之後，系統會提示您支付一小筆「捐款」以支持專案。雖然這是可選的，但我強烈建議如果您打算經常使用這項服務的話，可以考慮捐獻。像 Minibits 這樣的開放原始碼專案仰賴社群的支持來繼續開發和維護。即使是很小的貢獻也有助於確保專案的持久性。


![image](assets/en/08.webp)


## 5️⃣ Nostr 設定


如果您想給您在 Nostr 上追蹤的人小費，您可以藉由選擇「連絡人」，然後選擇「公開」，來「加入您的 npub 金鑰」。這可將您的 Minibits Wallet 連接到 Nostr 社交網路，實現無縫小費。


您也可以選擇 「使用您自己的設定檔」，進入 「設定」，然後選擇 「隱私」，匯入您自己的 Nostr Address 和金鑰。但是，請注意這樣做會阻止您的 Wallet 與 minibits.cash Nostr 和 LNURL Address 伺服器通訊，這會停用接收 Zaps 和付款的閃電 Address 功能。


![image](assets/en/09.webp)


## 6️⃣接收資金


要初始接收資金，您需要通過閃電 Invoice 為您的 Wallet 充值。這個過程很簡單：點擊 `充值` ，輸入要充值的`金額` ，選擇性地添加一個`備忘` ，然後點擊 `創建 Invoice`。然後您需要使用另一個閃電 Wallet 來支付這個 Invoice，這會在您的 Minibits Wallet 中將 Bitcoin 閃電付款轉換為 ecash 代幣。


![image](assets/en/10.webp)


## 7️⃣寄送資金


現在您已為 Wallet 注資，您可以透過兩種不同的方式寄送資金。


### 發送電子現金


第一個選項是直接傳送 ecash。點選「傳送」，然後選擇「傳送 ecash」，輸入「金額」，然後點選「建立 token.」，這將會 generate 一個 QR 代碼，您可以分享給收件人或讓他們直接用裝置掃描。收件人幾乎會立即看到代幣出現在他們的 Wallet 中，沒有 Blockchain 費用或確認延遲。


![image](assets/en/11.webp)


### 使用閃電付款


第二個選項是透過 Lightning 付款。點選 `發送` ，然後選擇 `使用 Lightning 付款`。您可以從您的 Nostr `contacts` 中選擇 (如果您已連接您的 npub)，或使用 `Paste` 或 `scan` 選項輸入/貼上一個 Lightning Address、Invoice 或 LNURL 付款代碼。確認收款人後，系統會提示您輸入 「付款金額」，可選擇添加備忘錄，然後點擊 「確認」，再點擊 「立即付款 」完成 Lightning 交易。


![image](assets/en/12.webp)


## 8️⃣建立 NWC 連線


Minibits 的另一項強大功能是建立「Nostr Wallet Connect (NWC)` 連線」的能力，可讓其他應用程式向您的 Wallet 要求付款，而無需暴露您的私密金鑰。


若要設定，請移至「設定」，然後選取「Nostr Wallet Connect」，然後點選「新增連線」。將連線命名為具有描述性的名稱，以識別應用程式和相關的使用者帳戶。設定合理的每日最大限額，以控制可透過此連線花費的金額，然後點選`儲存`完成設定。


此功能對於像 Nostr Clients 這樣的服務特別有用，在這種服務中，您想要啟用自動小費，而不需要手動核准每筆交易。


![image](assets/en/12.webp)


## 🎯 結論


Minibits 提供進入 ecash 世界的切入點，提供注重隱私的付款方式，與您持有的 Bitcoin 相輔相成。請記住永遠保持適當的備份，考慮使用多個鑄幣廠來進行備援，並且只在此保管解決方案中儲存適當的金額。


如需其他資源，請參閱 Minibits GitHub 儲存庫、官方網站，以及他們的 Telegram 頻道，社群會在該頻道中積極討論開發並排除故障。


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Website](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


ecash 的生態系統仍在演進中，但 Minibits 等工具讓日常使用者越來越容易取得這項強大的隱私技術。