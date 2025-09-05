---
name: Boltz
description: 在不同的 Bitcoin 層間切換，同時保持控制。
---


![cover](assets/cover.webp)



自 2009 年部署以來，Bitcoin 的點對點電子現金系統已成倍成長，賦予解決方案生命力，使其今天成為我們在日常行動中可立即使用的系統，特別是透過 Lightning Network。



然而，Bitcoin 通訊協定各層之間仍存在一個主要問題：流體互通性。為了充分發揮 Bitcoin 的潛力，當務之急是找到一個解決方案，讓協定的不同層之間能夠進行交易。這個需求在 2019 年催生了 Boltz，一個連結數個 Bitcoin 層的橋接器。



## 什麼是 Boltz？



[Boltz](https://boltz.Exchange)是一個非監護平台，是任何希望在 Bitcoin 通訊協定不同層級之間進行交易的人的理想選擇：




- on chain**：Bitcoin 的主鏈，交易平均每 10 分鐘確認一次，交易費用通常很高，不一定能滿足使用者的需求；
- Lightning Network**：覆蓋 Bitcoin 即時付款，費用低廉，可讓 Bitcoin 用於日常付款；
- Liquid Network**：由 Blockstream 創建的 Bitcoin 的覆蓋層，可實現快速、Confidential Transactions 以及使用其他基於 Bitcoin 的金融工具；
- RootStock**：以 Bitcoin 通訊協定為基礎開發智慧型契約的解決方案。



![layers](assets/fr/01.webp)



這些不同層級之間的互操作性非常重要，因為它提供使用者充分利用 Bitcoin 生態系統所提供的一切所需的靈活性。



Boltz 使用原子交換技術。此技術可讓比特幣在 2 層之間直接進行交換 (例如 Exchange 鏈上的 BTC 交換 Lightning 鏈上的 BTC)，不需要信任，也不需要中介。這些交換被稱為 「原子」，因為它們只能產生兩個結果：




- 要麼 Exchange 成功，兩個參與者有效地交換了他們的 BTC ；
- 要麼 Exchange 失敗，要麼兩位參與者都帶著自己原有的 BTC 離開。



如此一來，您就能永久保有比特幣的自我保管權，而且 Exchange 並不基於對交易對手的任何信任：Exchange 不是成功就是失敗，但任何一方都無法竊取對方的資金。



原子式 Exchange 可與智慧契約 [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*) 搭配使用。在這一類 Contract 中，金額被 「鎖定 」在雙向通道中，並引入時間限制，如果交易未在一定時間內完成，餘額就會歸還給存款人。這是 Boltz 平台使用的機制。



## 您與 Boltz 的首次交流



Boltz 是一個不需要您提供任何個人資訊的非存管式網路平台。Boltz 擁有簡約流暢的 Interface，可讓您在一分鐘內開始交易。



![boltz](assets/fr/02.webp)



進入平台後，您可以在 Bitcoin 生態系統的不同層級之間建立原子交換。



![home](assets/fr/03.webp)



您會看到您可以透過 Boltz 進行交易的最小和最大薩托希數量（Bitcoin 的最小單位），包括網路費用和 Boltz 徵收的 0.1% 到 0.5% 之間的百分比。



![fees](assets/fr/04.webp)



然後，選擇您希望製作原子 Exchange 的 Layer，並選擇您希望接收比特幣的 Layer。



![couches](assets/fr/05.webp)



在本教程中，我們將專注於原子 Exchange 從主 Layer 到 Lightning Network。



您可以在下列選項中進行選擇，以設定交換機的基本裝置 ：




- BTC ；
- Sats.



![unités](assets/fr/06.webp)



完成基本配置後，請插入原子 Exchange 的金額，然後為相等的金額建立 Lightning Invoice，或直接插入您的 LNURL。



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



為了安全起見，請檢查您的原子 Exchange 的參數，以輸出與您的 Exchange 相連的備份金鑰。



在 ** 設定** 圖示上，下載備份金鑰，並適當地儲存檔案。



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



此檔案包含與原子交換相關的 12 個投資組合關鍵字。



然後按一下 ** 建立原子 Exchange** 按鈕，並繼續支付指定金額。



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

一旦您完成付款並確認，您的 Lightning Wallet 將自動收到等值金額。



在 **Refund** 功能表中，找到您的原子 Exchange 歷史，以識別您希望退款的 Exchange。您也可以匯入您在其他裝置上的交換記錄，例如使用與這些交換相關的備份金鑰檔案。



![refund](assets/fr/11.webp)



在**歷史**功能表中，您可以按一下**備份**按鈕，下載與救援金鑰相關的更詳細的交換歷史記錄。



![backup](assets/fr/12.webp)



⚠️ 請也不要洩露此檔案，因為它包含與您的交易相關的所有資訊，以及與這些交易連結的備份金鑰。



Boltz 透過 Tor 網路上的 `.onion` 連結，為您提供高度的保密性。在您的瀏覽器中啟動 Tor 瀏覽功能後，選擇**洋蔥**選單，即可讓原子交換完全匿名。



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

現在您已經熟悉 Boltz 了，它是一個獨特的 Exchange 平台，能夠實現 Bitcoin 生態系統不同層級之間的互操作性。