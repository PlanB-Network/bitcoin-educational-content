---
name: 澳洲堅果 Wallet
description: Cashu 移動 wallet 用於匿名和即時 BTC 付款
---

![cover](assets/cover.webp)



Macadamia Wallet 是一款 iOS 手機 wallet，它實現了 Cashu 協定，Chaumian ecash 系統可實現完全匿名的 Bitcoin 支付。由於採用了盲簽技術，旁人無法將您的存款與消費聯繫起來，因此具有與實體現金類似的保密性。



在本教程中，我們將介紹如何安裝和配置 Macadamia、執行第一筆 Cashu 交易（鑄幣、發送、接收、融資），以及管理多個鑄幣以確保您的資金安全。



## 什麼是 Macadamia Wallet？



### 卡舒協定



Cashu 使用 David Chaum 發明的盲簽法：您將比特幣存入「鑄幣廠」伺服器，鑄幣廠會發行等值的 Satoshis 代幣。鑄幣廠會簽署這些代幣，但不會看到代幣的內容，因此無法將 token 與使用者連結。交換是 off-chain，點對點，完全不透明 - 甚至造幣廠也無法追蹤誰付錢給誰。



Macadamia 是以 Swift/SwiftUI 開發的開放原始碼 wallet iOS。它無需帳號或 KYC 即可運作，您的代幣儲存於本機，並由 seed 短語保護。代碼可在 GitHub 上進行審計，代幣可與其他 Cashu 錢包 (Minibits, Cashu.me) 進行互操作。



### 託管模式與妥協



**重要**：卡舒以託管模式運作。代幣是由鑄幣廠的 Bitcoin 儲備支持的支付承諾 (IOU)。如果鑄幣廠消失，您的代幣也會失去價值。這是最大保密性的折衷方案。



使用 Macadamia 作為實體 wallet：僅限少量。將您的資金分散在幾個薄荷糖上，以稀釋風險。



## 主要功能



Macadamia 實現了 Cashu 協定的四種基本操作。 **Mint** 透過 Lightning 發票將您的 Satoshis 轉換為代幣。 **發送**可讓您透過 QR 碼或連結免費發送代幣，完全 off-chain。 **Receive** 可讓您接收代幣或 generate Lightning 發票。 **Melt** 透過銷毀您的代幣來支付 Lightning 發票。



wallet 支援同時管理多個代幣。您可以透過 Lightning 在不同的鑄幣廠之間交換代幣。



## 支援的平台



Macadamia 僅適用於 iOS 17 或更高版本的 iPhone 和 iPad。本機 Swift/SwiftUI 應用程式提供與 Apple 生態系統的最佳整合。



Cashu 協定保證了錢包之間的互操作性。您可以在其他應用程式中還原您的 seed 短語，例如 Android 上的 Minibits 或桌面上的 Nutstash。



目前的版本透過 TestFlight 發行。此測試版僅可少量使用。



## 安裝



Macadamia 目前可透過 Apple 的測試程式 TestFlight 取得。以下是安裝方法：



### 透過 TestFlight 安裝



**步驟 1：下載 TestFlight**



如果您的裝置上還沒有 TestFlight 應用程式，請在 App Store 搜尋「TestFlight」並安裝。TestFlight 是 Apple 測試 iOS 應用程式 beta 版的官方應用程式。



**步驟 2：加入 Macadamia beta 計劃** (法語)



安裝 TestFlight 後，請從 iPhone 或 iPad 遵循此邀請連結：[https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



連結會自動開啟 TestFlight 並提供您安裝 Macadamia Wallet。點選「接受」，然後點選「安裝」開始下載。此應用程式重約 10 MB，安裝只需幾秒鐘。



![Installation TestFlight](assets/fr/01.webp)



### 關於測試版的重要資訊



Macadamia 仍處於積極開發的階段。TestFlight 版本會經常更新，並可能推出新功能或修正錯誤。然而，與任何測試版一樣，可能會發生故障。 **我們強烈建議您只使用少量**，您接受在發生技術問題時可能會遺失。



根據顯示的隱私權政策，Macadamia 不會收集任何使用者資料。安裝時請務必檢查開發者是否為 cypherbase UG。



## 初始設定



第一次啟動時，Macadamia 會產生一個包含 12 個字的 BIP-39 句子。請將它們寫在安全的地方 - 絕對不要截圖。這些字詞可讓您重新建立 wallet，並花費您的代幣。



![Configuration initiale](assets/fr/02.webp)



遵循四個步驟：歡迎、接受條款、儲存 seed 句子和最後確認。



![Interface principale](assets/fr/03.webp)



設定完成後，Macadamia 會顯示三個主要標籤。 **Wallet** 顯示您的餘額和交易歷史。 **Mints** 可讓您管理您的 Cashu 伺服器。 **Settings** 可以存取設定和您的 seed 詞組。



![Ajout d'un mint](assets/fr/04.webp)



現在您需要配置一個mint，也就是將發行代用幣的Cashu服務器。進入 "Mints 「標籤，點擊 」Add new Mint URL"，然後輸入您選擇的鑄幣廠地址（例如：mint.cubabitcoin.org）。查看 bitcoinmints.com 或 cashu.space，了解聲譽良好的公共鑄幣廠。僅驗證您已檢查其聲譽的鑄幣廠，因為他們將負責保管您的 Satoshis。



## 每日使用



### 建立新代用幣 (Mint)



若要以 ecash 養活您的 wallet Macadamia，您需要執行「Mint」作業 (建立代幣)。點選「Receive」，然後選擇「Lightning」選項。輸入所需金額 (例如 1000 sats)，選擇要使用的鑄幣，然後點選 generate Lightning 發票。



![Opération Mint](assets/fr/05.webp)



使用您常用的 wallet (Phoenix、Zeus、BlueWallet) 支付生成的 Lightning 發票。



![Confirmation Mint](assets/fr/06.webp)



付款後，Cashu 代幣會立即出現在您的餘額中。



### 傳送代幣



若要傳送 Cashu 代幣給其他使用者，請點選主畫面上的「傳送」按鈕，然後選擇「Ecash」。輸入要傳送的金額 (例如：50 sats)，並視需要加入描述性備註。



![Envoi Ecash](assets/fr/07.webp)



透過 iMessage、Signal 或 Telegram 分享 QR 代碼或產生的文字。收款人可立即免費領取資金。



### 接收代幣



若要接收其他使用者傳送的 Cashu 代幣，請點選「接收」，然後選擇「Ecash」。掃描 token QR 代碼或貼上您收到的 token 連結。



![Réception Ecash](assets/fr/08.webp)



點選「Redeem」可申請 token。



### 閃電（融化）付款



要使用您的 Cashu 代幣支付 Lightning 發票，請點選 「發送」，然後選擇 "Lightning"。貼上您要支付的 BOLT11 發票。



![Paiement Lightning](assets/fr/11.webp)



鑄幣廠會銷毀您的代幣，並執行 Lightning 付款。因此，您可以支付任何 Lightning 服務，同時保留您的匿名性。



### 交換薄荷糖



當您從未設定的鑄幣廠收到代幣時，Macadamia 會提供您幾個選項來管理這些代幣。



![Swap inter-mints](assets/fr/09.webp)



添加新的鑄幣廠或將代幣交換到現有的鑄幣廠。交換使用 Lightning 作為橋樑，以匿名方式轉移您的資金。



### 先進的多重薄荷管理



Macadamia 提供精密的工具，可同時管理多個薄荷糖，並策略性地分配您的資金。



![Gestion multi-mints](assets/fr/10.webp)



「分配資金 」根據百分比自動分配您的餘額（例如 50/50）。「轉帳 」允許在鑄幣廠之間手動轉帳，以分散您的風險。



## 優點與限制



**Highlights** ：





- 最高保密性**：無法追蹤的交易，甚至造幣廠也無法追蹤。無區塊鏈元資料、無軌跡的點對點交換。
- 快速、免費**：薄荷糖內免費即時轉帳，是微額付款的理想選擇。
- 互操作性**：標準化的 Cashu 代幣，可與其他相容的錢包 (Minibits, Nutstash) 搭配使用。
- 簡單**：Interface iOS 本機適合初學者使用，同時保持可稽核性 (開放原始碼)。



**Constraints** ：





- 託管模式**：需要信任鑄幣廠。如果鑄幣廠消失，您的代幣就會失去價值。
- 僅限 iOS**：沒有 Android/桌面版本。Cashu 互操作性允許透過其他錢包存取，但最佳體驗仍是 iOS。
- Mint 依賴性**：Mint 離線 = 無法執行需要其介入的交易 (Mint、Melt)。
- 新興技術** ：積極開發、可能的錯誤、不斷演進的標準。



## 最佳實踐





- 分散您的鑄幣廠**：將您的籌碼分散到幾家信譽良好的造幣廠，以降低風險。
- 限制金額**：使用 Macadamia 作為日常付款的實體 wallet，而非保險箱。
- 保護您的 seed**：將 12 字短語寫在紙上，放在安全的地方。偶爾測試還原。
- 檢查薄荷**：在新增一個mint之前，請諮詢cashu.space和社區論壇。選擇正常運行時間長且聲譽良好的廠商。
- VPN 或 Tor**：使用 VPN/Tor 隱藏您的 IP，最大化網路隱私。
- 加入社群**：Telegram/Discord Cashu 群組了解最新資訊、薄荷糖建議和最佳實務。



## 總結



Macadamia Wallet 將實體現金的特性帶入數位 Bitcoin。透過結合 Chaum 和 Lightning 盲簽名，它為交易保密性提供了優雅的解決方案。它的原生 iOS 介面讓複雜的加密技術成為可能，同時保持開放原始碼，並與 Cashu 生態系統互通。



託管模式需要警覺性和良好的安全措施。如果使用得當，Macadamia 會成為需要匿名的日常付款的寶貴工具，並補充非保管式錢包的儲蓄功能。



## 資源



### 官方文件




- 官方網站：[macadamia.cash](https://macadamia.cash)
- 澳洲堅果常見問題：[macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub 原始碼：[github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### 卡舒文件




- 技術文件：[docs.cashu.space](https://docs.cashu.space)
- 公共造幣廠列表：[bitcoinmints.com](https://bitcoinmints.com)
- 官方協定網站：[cashu.space](https://cashu.space)



### 社區




- Telegram Cashu 群組：[t.me/cashu_ecash](https://t.me/cashu_ecash)