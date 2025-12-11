---
name: BIP47 - PayNym
description: 在 Ashigaru 上使用可重複使用的付款代碼
---
![cover](assets/cover.webp)



您在 Bitcoin 上最容易犯的隱私錯誤就是重複使用地址。每次同一地址收到數筆付款時，這些交易都會連結在一起，為全世界提供您的交易地圖。因此，強烈建議您每次收款都使用唯一的 generate 位址。但對於某些 Bitcoin 應用程式而言，這並不是一件簡單的事。



Justus Ranvier 在 2015 年提出的 BIP47 為這個問題提供了一個優雅的答案。它引入了**可重複使用支付代碼**的概念：一個獨特的識別符，幾乎可以接收無限數量的鏈上比特幣支付，而無需重複使用地址。拜 ECDH (*Diffie-Hellman on elliptic curves*) 交換加密機制所賜，每次向相同代碼付款都會產生一個空白地址，特定於寄件人和收件人之間的關係。



![Image](assets/fr/01.webp)



**PayNym**特別實現了BIP47原則，該系統最初由Samourai Wallet開發，現在由Ashigaru接管。在本教程中，我們將探討如何啟動您的 PayNym、與對應方交換付款代碼以及在不重複使用地址的情況下進行交易。



我不會在此詳述 BIP47 的詳細操作。如果您想深入了解，請參閱我的 BTC 204 訓練課程第 6.6 章。



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 先決條件



要遵循本教學，您只需要在 Ashigaru 應用程式上建立 wallet。如果您不知道如何下載、驗證、安裝應用程式或建立 wallet，我建議您先參考本教學：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## 申請 PayNym



第一步是申請您的 PayNym。每個 wallet 只需執行一次此操作。它將來自您的 seed (`PM...`)的 BIP47 支付代碼與 PayNym 實施的唯一識別符相結合。這個更短、更易於閱讀的識別碼就可以傳送給您的通信員，以方便交換，而無需分享冗長、完整的 BIP47 代碼。



要這樣做，請點擊介面左上方的 PayNym 圖片，然後點擊您的付款代碼 "PM..."。



![Image](assets/fr/02.webp)



然後按一下右上角的三個小圓點，並選擇 `Claim PayNym`。



![Image](assets/fr/03.webp)



按一下「申請您的 PAYNYM」按鈕以確認。



![Image](assets/fr/04.webp)



刷新頁面：您的 PayNym ID 現在會顯示在您的圖像下方，就在您的 BIP47 付款代碼上方。



![Image](assets/fr/05.webp)



您的 PayNym 現在已啟動，並準備用於您的第一筆 BIP47 交易。



## 連絡人



PayNym 之間有兩種連接方式： **follow**和**connect**。follow "操作完全免費。它通過 Soroban 在兩個 PayNym 之間建立連接，Soroban 是由 Samourai 團隊開發、Ashigaru 採用的基於 Tor 的加密通信協定。此連結可讓彼此關注的兩個使用者私下交換資訊，特別是協調協作交易，例如 Stowaway 或 StonewallX2，我們會在另一個教學中介紹。此步驟為 PayNym 所特有，並非 BIP47 協定的一部分。



![Image](assets/fr/06.webp)



另一方面，連接操作 (`connect`)需要 on-chain 交易。它包括執行 BIP47 定義的通知交易。此 Bitcoin 交易包含 `OP_RETURN` 輸出中的元資料，它在付款方和收款方之間建立了加密通信通道。從這個通道，付款人將能夠為每筆付款提供 generate 獨特的收款地址，而收款人將獲得這些付款的通知，並能夠 generate 與地址相關的私人金鑰，以便稍後花費這些資金。



此通知交易是有成本的：mining 費用和 546 sats 傳送至收件者的通知位址以示連線。一旦建立連線，幾乎可以透過 BIP47 進行無限次的付款。



一言以蔽之：




- follow」：免費，透過 Soroban 建立加密通訊，對 Ashigaru 的協作工具很有用；
- Connect`：收費，執行 BIP47 通知交易，以啟動付款人和收款人之間的通道。



要與 PayNym 進行互動，您必須先*follow*它。這是建立 BIP47 連接之前的第一步。假設您想向 PayNym `+instinctiveoffer10`發送定期付款。



前往您在 Ashigaru 上的 PayNym 頁面，然後按一下介面右下方的 `+` 按鈕。



![Image](assets/fr/07.webp)



然後，您可以貼入收件人的完整付款代碼，或掃描他們的 QR 代碼。



![Image](assets/fr/08.webp)



如果您只有他的 PayNym ID，請到 [Paynym.rs](https://paynym.rs/) 找到與他的付款代碼相關的 QR 代碼。



![Image](assets/fr/09.webp)



掃描 QR 代碼後，點擊 `FOLLOW` 按鈕跟隨 PayNym。



![Image](assets/fr/10.webp)



對於協同交易 (*cahoots*) 而言，`FOLLOW`動作已經足夠。但是，要發送 BIP47 付款，您需要建立連線：點擊 `CONNECT` 執行通知交易。



![Image](assets/fr/11.webp)



然後通知交易會在網路中廣播。請等待至少有一次確認後，再進行第一次付款。



![Image](assets/fr/12.webp)



## 進行 BIP47 付款



現在您已與收款人連線，並可將付款傳送至使用 BIP47 通訊協定自動產生的唯一地址，而無需事先與收款人進行任何交換。



從您的 PayNym 主頁面，點擊您希望向其發送付款的聯絡人。



![Image](assets/fr/13.webp)



在介面右上方，按一下箭頭圖示。



![Image](assets/fr/14.webp)



輸入要發送的金額。您不需要輸入收件地址：它會使用 BIP47 通訊協定自動產生。



![Image](assets/fr/15.webp)



仔細檢查交易細節，包括費用，然後拖動螢幕底部的綠色箭頭，簽署並廣播交易。



![Image](assets/fr/16.webp)



交易已傳送。



![Image](assets/fr/17.webp)



在這個例子中，付款是支付到我的另一個 PayNym 錢包。因此，我可以看到它已經到達我的另一個 Ashigaru wallet，沒有手動交換任何地址：只使用了 PayNym 識別碼。



![Image](assets/fr/18.webp)



由於 Ashigaru 應用程式上的 PayNym 實作，您現在知道如何使用 BIP47 可重複使用的付款代碼。現在，您可以與任何希望向您發送付款（特別是循環付款）的人分享此付款代碼。您也可以在您的網站上或社交網路中公佈您的 PayNym ID，以接受捐款。



若要加深您對此協定的認識，詳細瞭解其運作方式及其對保密性的影響，我強烈建議您參加我的 BTC 204 課程：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c