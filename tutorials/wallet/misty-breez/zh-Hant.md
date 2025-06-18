---
name: Misty Breez
description: 無弓的 Lightning Wallet。
---

![misty-breez-cover](assets/cover.webp)



Misty Breez 是 Breez 基於其軟體開發套件和 BlockStream 所開發的 **Liquid** 網路所開發的 Lightning 自持 Wallet。


它配備全新的無 Lightning 節點作業方式：Bitcoin 網路間傳輸的潛在**遊戲改變者**。


在本教程中，我們將介紹此組合的運作方式，並為您提供完整的概述。



## Misty Breez 如何運作？



Misty Breez 是一個沒有使用 Lightning 節點作為後端的實作。它是在 Breez SDK 和 Liquid 的基礎上開發的。



Liquid 是與 Bitcoin 網路平行的 Layer，在速度和交易成本上有顯著的改善。此 Layer 可讓 Misty Breez 免去 Lightning 節點，改用第三方 Exchange 服務，例如 **Boltz** 以確保 Liquid Network 與 Lightning Network 之間的互通性。別著急，我們會再來討論這個問題。



現在，讓我們從 Misty Breez Wallet 開始冒險。



## 開始使用 Misty Breez



Misty Breez 手機應用程式可於 Google Play Store (Android) 及 Apple Store (iOS) 等官方下載平台下載。您也可以從 [Misty Breez] 官方網站(https://breez.technology/misty/) 轉到正確的應用程式。



⚠️ 請確保不要將 Misty Breez 與 Breez Wallet 混淆。



⚠️ **重要**：為了您比特幣的安全，必須從官方平台下載應用程式，以確保其真實性。



![download-misty-breez](assets/fr/01.webp)



在本教程中，我們將從 Android 裝置開始。然而，本節中詳述的每個步驟和特定功能都適用於 iOS。



安裝時，Misty Breez 會讓您選擇建立新的 Wallet 或還原您有復原碼的舊 Lightning Wallet。


在本教程中，我們選擇建立一個新的投資組合。



⚠️Misty Breez 目前正處於開發階段，因此我們建議您從合理的金額開始。



![create-wallet](assets/fr/02.webp)


### 保存您的恢復單詞 ：


在建立新的投資組合時，您應該做的第一件事就是備份您的 12 個恢復字詞。


以下是如何備份您的備份短語的一些提示。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

若要備份您的短語，請選取 ** 喜好設定 > 安全** 功能表，然後選取 ** 檢查您的備份短語** 選項。



![backup](assets/fr/03.webp)


為了增加安全性，您也可以**建立 PIN 碼**，以驗證 Wallet 的存取權限。




在 Misty Breez 接受的多種貨幣中找到您的當地貨幣。從 ** 偏好設定 > 法定貨幣** 功能表設定您的貨幣，然後選擇您需要的一種或多種貨幣。



![devises](assets/fr/04.webp)



### 進行首次交易


如果您已經熟悉 Breez 產品系列，就完全不會對 Misty Breez 的直覺式 Interface 感到陌生。



在 Interface 的 **Balance** 功能表上，點選 **Receive** 選項，即可建立發票，在您的 Wallet 上接收您的 bitcoins。



⚠️ Misty Breez 會要求您在手機設定中啟動應用程式的通知，讓您有權獲得 Lightning Address。



使用 Misty Breez，您可以 ：




- 在 Lightning Network 上接收比特幣，從 **100 Satoshis** 到 **25,000,000 Satoshis**。
- 在 Bitcoin 主網路上接收比特幣，**25,000 薩托希起**。



![transactions](assets/fr/05.webp)



Misty Breez 的魔力就從這裡開始。


Breez Wallet 為您提供一個 Lightning 節點，並要求您自行承擔開啟和關閉支付通道的費用，而 Misty Breez 則不同，它不要求您做任何事情。如前所述，Misty Breez 甚至不是在 Lightning 節點的基礎上運作。



讓我們仔細看看幕後的故事。



在現實中，您擁有與您的 Misty Breez 投資組合相關的 Liquid 投資組合。邏輯上，您將以固定費率處理 L-BTC (Liquid Bitcoin) 與第三方海底衛星轉換服務相關聯，這將使您能夠與 Lightning Network 互通。



當您在您的 Misty Breez Wallet 上收到付款時，您的寄件者會寄給您薩托希，薩托希會經過像 Boltz（目前由 Misty Breez 使用）這樣的轉換服務，將寄來的薩托希轉換成 L-BTC，然後在您的 Misty Breez Wallet 上收到（相關的 Liquid Wallet）。


以下是幕後流程的簡化圖表。



![lnswap-in](assets/fr/06.webp)



按一下 **Balance** 功能表中的 Interface，按一下 **Send** 選項來支付 Lightning Invoice。


插入 Lightning Invoice、收件人的 Lightning Address 或直接掃描 Invoice 上的 QR 代碼進行付款。



![send-bitcoins](assets/fr/07.webp)



在幕後，您啟動與您的 Misty Breez Wallet 相關聯的 Liquid Wallet，透過 Boltz 將等值的 L-BTC 轉換為 Satoshis，然後將這些 Satoshis 轉移到收件人的 Lightning Wallet（存在於 Lightning Network 上）。



![send-bitcoin-bts](assets/fr/08.webp)



Misty Breez 基礎架構的這項功能讓使用者即使在 Misty Breez 離線時也能進行交易。



對於較有經驗的使用者，還有一個選單 ** 偏好設定 > 開發者**，可讓您瞭解更多關於 .NET 的詳細資訊：




- Breez 軟體開發套件的版本。
- 您的 Misty Breez Wallet 的公開金鑰。
- 借款人，從主要公開金鑰衍生出來的唯一識別碼。
- 您的投資組合餘額。
- 提示 Liquid，用於發送少量的 L-BTC。
- Bitcoin Tip，用於傳送少量的 Bitcoin。



您也可以執行某些動作，例如與 Liquid Network 同步、備份您的鑰匙、分享您的活動記錄以及選擇重新掃描 Liquid Network。



![dev-mode](assets/fr/09.webp)


恭喜您現在您已充分瞭解 Misty Breez 產品組合及其對 Bitcoin 網際交易的貢獻。如果您覺得本教程有用，請對我們豎起 Green 大拇指。我們很高興收到您的來信。



若要更進一步，我也建議您探索我們關於 Aqua Wallet 的教學，其運作方式與 Misty Breez 相似 ：



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125