---
name: LNP2PBot
description: LNP2PBot 和 P2P Bitcoin 交易完整指南
---
![cover](assets/cover.webp)


## 簡介


免 KYC 點對點 (P2P) 交換對於維護使用者的機密性和財務自主性至關重要。它們可以讓個人之間直接進行交易，無需身份驗證，這對於重視隱私的人來說至關重要。如需更深入瞭解理論概念，請參閱 BTC204 課程：


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

買賣 Bitcoin 點對點（P2P）是獲取或處理比特幣最私密的方法之一。LNP2PBot 是一個開放原始碼的 Telegram 機器人，可促進 Lightning Network 上的 P2P 交換，實現快速、低成本、免 KYC 的交易。


### 為何使用 Lnp2pbot？




- 無需 KYC
- 在 Lightning Network 上快速交易
- 低成本
- 透過 Telegram（一個可從世界任何地方存取的熱門訊息應用程式）簡單的 Interface
- 綜合信譽系統
- 安全交易的自動託管
- 支援多種貨幣
- 活躍且不斷成長的社群


### 先決條件


若要使用 Lnp2pbot，您需要 ：


1.Lightning Network Wallet（建議使用 Breez、Phoenix 或 Blixt）


2.已安裝 Telegram 應用程式 (https://telegram.org/)


3.具有定義使用者名稱的 Telegram 帳戶


## 安裝與設定


### 1.設定您的 Lightning Wallet


首先安裝相容的 Lightning Wallet。以下是我們的詳細建議：


**推薦的錢包**




- [Breez](https://breez.technology)**：
  - 非常適合初學者
  - 直覺、現代化的 Interface
  - 非監護（您保留對資金的控制權）
  - 與 Lnp2pbot 完美相容
  - 適用於 iOS 和 Android


以下是這個 Wallet 的教學連結：


https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [Phoenix](https://phoenix.acinq.co)** ：
  - 簡單可靠
  - 自動頻道設定
  - 原生支援 BOLT11 發票
  - 非常適合日常交易
  - 適用於 iOS 和 Android


以下是這個 Wallet 的教學連結：


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [Blixt](https://blixtwallet.github.io)** ：
  - 技術性較高，但非常完整
  - 進階組態選項
  - 非常適合有經驗的使用者
  - 開放原始碼
  - 適用於 Android


以下是這個 Wallet 的教學連結：


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**其他錢包的重要注意事項**


⚠️ **重要**：在銷售 Sats 之前，請確定您的 Wallet 支援「持有」發票，此發票會被機器人用作託管系統。




- Satoshi 的 Wallet**：接收 Sats 時效果很好，但如果銷售取消，更新餘額時可能會有延遲。
- Muun**：不建議使用，因為殭屍路由費限制（最高 0.2%）可能會導致支付失敗。
- Aqua**：可接收 Sats，但在銷售取消的情況下，餘額更新可能會延遲很長時間（最長 48 小時）。


💡 **提示**：為獲得最佳體驗，請選擇推薦的錢包（Breez、Phoenix 或 Blixt）。


⚠️ **重要**：別忘了將恢復短語保存在安全的地方。


### 2.開始使用 Lnp2pbot


1.按一下此連結以存取機器人：[@lnp2pBot](https://t.me/lnp2pbot)


2.Telegram 會自動開啟


3.按一下「開始」或傳送指令「/start


4.如果您還沒有使用者名稱，機器人會要求您建立一個使用者名稱


5.機器人會引導您完成初始設定


### 3.加入社群




- 加入主頻道：[@p2plightning](https://t.me/p2plightning)
- 支援：[@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## 買賣比特幣


在 Lnp2pbot 上 Exchange 比特幣有兩種主要方式：


1.瀏覽並回應市場上的現有報價


2.建立您自己的買賣報價


在本指南中，我們將詳細介紹如何使用 .NET 技術：




- 從現有報價中購買比特幣
- 透過建立自己的報價出售比特幣


### 如何購買比特幣


**1.尋找並選擇優惠**


![Sélection d'une offre de vente](assets/fr/01.webp)


瀏覽 [@p2plightning](https://t.me/p2plightning) 中的優惠，並點擊您感興趣的廣告下的 「購買 satoshis 」按鈕。


**2.驗證報價和金額**


![Validation de l'offre](assets/fr/02.webp)


1.返回殭屍聊天


2.確認您的報價選擇


3.輸入您要購買的法定貨幣金額


4.機器人會要求您提供一個 Lightning Invoice 以 Satoshis 為單位的金額。


**3.聯絡賣家**


![Mise en relation](assets/fr/03.webp)


發送 Invoice 後，機器人會讓您與賣家聯絡。


**4.與賣家溝通**


![Chat privé](assets/fr/04.webp)


按一下賣家的暱稱，即可開啟私人聊天頻道，您可以 Exchange 法幣付款詳細資訊。


**5.付款確認


![Confirmation du paiement](assets/fr/05.webp)


進行法幣付款後，在機器人聊天中使用 `/fiatsent` 指令。交易完成後，您就可以為賣家評分，交易也會結束。


### 如何出售比特幣


**1.建立銷售要約**


![Création d'une offre de vente](assets/fr/06.webp)


若要建立銷售報價，只需使用命令 ：


`/sell`


然後，機器人會逐步引導您：


1.選擇貨幣


2.指出要出售的 Satoshis 數量


3.就價格而言，您有兩種選擇：




   - 設定固定價格的 Satoshis 數量
   - 使用市場價格，並可選擇使用溢價（正或負）。


💡 **提示**：溢價可讓您根據市場價格調整您的價格。例如，溢價為 -1%，表示您的售價比市價低 1%。


**2.確認訂單建立**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


建立訂單後，您會看到確認訊息，並可選擇使用 `/cancel` 指令取消訂單。


**3.管理銷售**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- 當買家回應您的出價時，您會收到附有 QR 代碼和 Invoice 付款方式的通知。
- 檢查買家的個人資料和聲譽。


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- 按一下買家的暱稱以開啟私人討論頻道。
- 向買家傳達法幣付款細節。
- 等待買家確認法幣付款。
- 檢查您的帳戶是否已收到付款。


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- 用 `/release` 確認交易並完成訂單。您將有機會為買家評分。


## 良好作業與安全


### 安全提示




- 從少量開始
- 經常檢查使用者的聲譽
- 僅使用建議的付款方式
- 保持所有溝通都在機器人聊天中進行
- 絕不分享敏感資訊


### 信譽系統




- 每個使用者都有一個信譽分數
- 成功交易可增加您的分數
- 選擇信譽良好的使用者
- 向版主報告任何可疑行為


### 爭議解決


1.當問題發生時，保持冷靜與專業


2.使用 `/dispute` 指令開立票狀


3.提供所有必要的證明


4.等待版主


## 與其他解決方案的比較


與 Peach、Bisq、HodlHodl 和 Robosat 等其他 P2P Exchange 解決方案相比，Lnp2pbot 有幾項優缺點：


### Lnp2pbot 的優勢




- 不需要 KYC** ：與某些平台不同，Lnp2pbot 不需要身份驗證，因此可為使用者保密。
- 快速交易**：有了 Lightning Network，交易幾乎是瞬間完成。
- 低費用** ：交易費用低於傳統交易所。
- 行動可用性**：LNP2PBot 可透過 Telegram 存取，因此可輕鬆在行動裝置上使用。
- 易於使用** ：Lnp2pbot 的直覺式 Interface 使其易於使用，即使是經驗較淺的使用者也能輕鬆上手。


### Lnp2pbot 的缺點




- Telegram 依賴性**：使用 Lnp2pbot 需要 Telegram 帳戶，這可能不適合所有使用者。
- 流動性較低**：與 Bisq 等較成熟的平台相比，流動性可能較有限。


相較之下，Bisq 等解決方案提供較高的流動性和桌面 Interface，但可能涉及較高的費用和較長的交易時間。同時，HodlHodl 和 Robosat 也提供免 KYC 交易，但收費結構和介面不同。


## 有用資源




- 官方網站：https://lnp2pbot.com/
- 文件：https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- 支援：[@lnp2pbotHelp](https://t.me/lnp2pbotHelp)