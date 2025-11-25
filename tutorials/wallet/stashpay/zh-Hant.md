---
name: StashPay
description: 適合所有人的簡約型 Bitcoin Wallet
---

![cover](assets/cover.webp)



用戶體驗是全球採用 Bitcoin 解決方案的關鍵因素。提供流暢、簡單且不受技術限制的體驗是許多錢包和 Exchange 平台的優先考量。在這方面，StashPay 以其簡約的方式脫穎而出，同時也展示了 Lightning Network 的強大功能。



在本教程中，我們將介紹此投資組合，瞭解其運作方式，以及它如何成為小型企業或個人創業者的理想選擇。



## 開始使用 StashPay



StashPay 是一款 Lightning 自保管 Wallet，主要因其簡約、以使用者為中心的使用者體驗而獲得肯定。  有了這個 Wallet，您不需要任何技術知識就可以接收和傳送您的第一個梭子錢。



StashPay 是一個以 React Native 開發的開放源碼專案，旨在解決即使在 Bitcoin 協定的主鏈上進行交易，也需要支付高昂交易費用的問題。它是 Android 和 iOS 平台上的行動應用程式，可透過 [網站](https://stashpay.me/) 上的下載連結下載。



![introduce](assets/fr/01.webp)



請務必從網站下載 Android 應用程式，因為 Google Play 商店無法下載。


下載完成後，請授予必要的權限，以便在 Android 手機上安裝應用程式。



一旦應用程式安裝完成，StashPay 會在您第一次開啟時為您建立一個初始 Bitcoin Wallet。在進行任何交易之前，我們建議您備份這個 Wallet。在下面，您可以找到我們所有的指南，以確保您的恢復短語得到適當的備份。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

點選「設定」圖示進入 StashPay 設定，然後點選 **建立備份**選項。然後授權顯示恢復短語。請勿將您的恢復短語複製到手機的剪貼簿，因為它們可能會被安裝在手機上的其他詐騙應用程式存取。



![backup](assets/fr/02.webp)



您也可以按一下 ** 復原 Wallet** 選項，並插入 12 或 24 個復原字元，以復原您已在使用的 Bitcoin Wallet。



### 在 StashPay 上收到您的第一筆沙托希



在首頁畫面中，按一下 **Receive** 按鈕，並設定一個大於紅色指定金額的數額。在我們的案例中，使用 StashPay Wallet 收取的金額不能少於 0.11 美元。



![receive](assets/fr/03.webp)



定義好金額後，您可以按一下 ** 建立 Invoice** 按鈕，然後掃描或複製 Invoice 將其傳送至您的 Satoshis 寄件者。



![receive_sats](assets/fr/04.webp)



按一下首頁的「時鐘」圖示，即可檢視您的交易記錄。



![network_fee](assets/fr/05.webp)



您會注意到，要收到 Satoshis，您必須支付網絡費。這些費用將會從您即將收到的 Satoshis 中扣除。這是因為 StashPay 是基於 Breez 開發套件的 Wallet。若要使用該套件的 Lightning 節點免費實作來收取 Satoshis，Breez 將會向客戶 (StashPay 在我們的案例中) 徵收 `0.25% + 40 satoshis` 的費用。更多資訊請參考我們的 Misty Breez 教學。



https://planb.academy/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### 使用 StashPay 傳送比特幣



使用 StashPay 傳送比特幣是相當直覺的，這要歸功於簡約的 Interface。在主畫面點選 **Send** 按鈕。掃描 QR 代碼或貼上您想要寄送 Satoshis 的 Address。StashPay 會自動偵測您要寄送比特幣的 Bitcoin 協定鏈。



![send](assets/fr/06.webp)



由於 StashPay 是基於 Breez 開發套件的 Wallet，因此它受益於一個有趣的優勢：以低成本在主鏈上發送比特幣。Breez 使用 Boltz 服務在 Bitcoin 協定的不同鏈之間進行交易，使實作開發套件的客戶能夠直接在其應用程式中受益於此服務。



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

但是，Breez SDK 設定了一個最低金額，您可以將比特幣發送到主鏈上的 Address。



![onchain](assets/fr/07.webp)



您也可以使用收件人的 Lightning Address 傳送比特幣。查看您的交易詳情，然後點擊 **Send** 按鈕進行確認。



![confirm](assets/fr/08.webp)



## 更多配置



在 StashPay 設定中，您可以調整配置以個人化使用 Wallet。



StashPay 可讓您根據您選擇的當地貨幣 Exchange 薩托希。按一下 ** 貨幣** 選項，然後在 StashPay 提供的 +113 種貨幣清單中搜尋您的貨幣。



![currencies](assets/fr/09.webp)



在**接收選項**選單中，您可以找到使用 StashPay 接收比特幣的所有設定。例如，選擇 ** 選擇 Lightning 或 Onchain**，啟用您的 Wallet 從主鏈接收比特幣。



![receive-onchain](assets/fr/10.webp)



透過 **Scan OnChain addresses** 選項，您可以檢查連結到不同位址的所有 UTXOs（您尚未花費的比特幣），以刷新 Wallet 的餘額。



![rescan](assets/fr/11.webp)



** 匯出記錄** 功能表會列出所有 Breez 和 Boltz 基礎架構的動作，這些動作與您在各個 Bitcoin 通訊協定鏈之間的交易和原子交換有關。



![export](assets/fr/12.webp)



您剛剛掌握了StashPay的極簡Bitcoin Wallet。如果您覺得本教程有用，我們向您推薦我們的教程：如何開始使用 Bitcoin 並賺取您的第一個比特幣。



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f