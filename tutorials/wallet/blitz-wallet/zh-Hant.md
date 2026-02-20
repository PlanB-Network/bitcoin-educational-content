---
name: Blitz Wallet
description: 最簡單的比特幣錢包。
---

![cover](assets/cover.webp)

使用者體驗是選擇比特幣錢包時的關鍵因素之一。在本教學中，我們將向您介紹 Blitz Wallet——一款以簡潔為核心理念的錢包：得益於 **Spark** 協議的整合，Blitz 為您提供了市場上最簡單、最全面的比特幣錢包之一，支援即時支付且無需任何技術管理。

## 什麼是 Blitz Wallet？

Blitz Wallet 是一款 **self-custodial** 且 **open source** 的比特幣錢包，專注於您的主權掌控以及流暢直覺的使用者體驗。

[Blitz Wallet](https://blitz-wallet.com/) 是一款行動應用程式，可在 Android（Play Store）和 iOS（App Store）上下載。

與需要管理支付通道和入站流動性的傳統 Lightning 錢包不同，Blitz Wallet 依託 **Spark 協議**來消除這些技術複雜性。結果是：從收到第一個聰開始即可即時支付，無需任何預先配置。Blitz 的目標是讓比特幣支付像普通支付應用程式一樣簡單，同時絕不犧牲您對資金的 self-custody。

Blitz Wallet 還支援格式為 `使用者名稱@網域.com` 的**可讀地址**（透過 LNURL），讓傳送比特幣像寄電子郵件一樣簡單，無需每次交易都處理冗長的 invoice 或 QR code。

## 理解 Spark 協議

在進入實際操作之前，了解 Blitz Wallet 底層運作的技術是很有幫助的：**Spark 協議**。

### 什麼是 Spark？

Spark 是一個建構在比特幣之上的 open source 二層協議，由 Lightspark 團隊開發。它能夠實現即時且低成本的交易，同時保持您對比特幣的 self-custody。

與依賴兩方之間**支付通道**的 Lightning Network 不同，Spark 使用了一種名為 **statechain**（狀態鏈）的技術。其基本原理如下：Spark 不是在每次交易時在區塊鏈上移動比特幣，而是將一個使用者的**支出權**轉移給另一個使用者，無需 on-chain 操作。

### 它是如何運作的？

為了直覺地理解 Spark，我們可以想像在 Spark 上花費比特幣需要完成一個由兩塊拼圖組成的拼圖：
- 一塊由使用者持有（例如 Alice）。
- 另一塊由一組被稱為 **Spark Entity (SE)** 的營運商持有。

只有兩塊相匹配的拼圖組合在一起，才能花費比特幣。

當 Alice 想將比特幣傳送給 Bob 時，會發生以下情況：Bob 和 SE 之間共同建立一個新的拼圖。拼圖保持相同的形狀，但組成它的拼圖塊發生了變化。現在是 Bob 的拼圖塊與 SE 的拼圖塊相匹配。Alice 的舊拼圖塊變得不可用，因為 SE 已經銷毀了與之對應的拼圖塊。比特幣的所有權已經易手，**且沒有在區塊鏈上發生任何交易**。

Bob 隨後可以重複相同的過程將這些比特幣傳送給 Carol，以此類推。每次轉帳都是透過替換拼圖塊來完成的，而非透過 on-chain 資金轉移。

### 為什麼是安全的？

一個合理的問題是：如果 SE 沒有真正銷毀其舊拼圖塊會怎樣？

Spark Entity 不是一個單一實體：它是一組獨立的營運商。SE 的拼圖塊從不由單個營運商持有。拼圖的替換需要多個營運商的協作。在一次轉帳中，只要有**一個營運商是誠實的**，就足以阻止舊拼圖被重新啟用。沒有任何單個營運商能夠秘密地保留一個舊的活躍拼圖或在事後重新建立它。

此外，Spark 整合了單方面退出機制：您始終可以在不需要 SE 協作的情況下將比特幣取回 on-chain。這一備用機制是 Spark 架構的核心組成部分，確保您永遠不會依賴網路來存取您的資金。

### Spark 與 Lightning Network 的比較

Spark 和 Lightning 並非競爭關係：它們是**互補的**。Blitz Wallet 整合了兩者，讓您能夠享受各自的優勢。

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **技術**                      | Statechains（狀態鏈）         | 支付通道              |
| **通道管理**                  | 不需要                        | 需要                  |
| **入站流動性**                | 不需要                        | 需要                  |
| **即時交易**                  | 是                            | 是                    |
| **Self-custody**              | 是                            | 是                    |
| **Lightning 相容性**          | 是（透過 atomic swaps）       | 原生                  |

Lightning Network 仍然是即時支付的優秀協議，但它帶來了技術限制（通道管理、入站流動性、節點需上線等），這可能會讓新手望而卻步。Spark 消除了這些限制，同時仍然與 Lightning 相容。

## 安裝與設定

在本教學中，我們以 Blitz Wallet 的 Android 版本為基礎，但以下所有流程同樣適用於 iOS。

![installation](assets/fr/01.webp)

由於 Blitz Wallet 是 self-custody 錢包，您可以選擇**建立新錢包**或**匯入恢復助記詞**（12 或 24 個單字）來恢復已有錢包。

在這裡，我們選擇建立新錢包。以下是我們關於備份恢復助記詞的建議：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **重要提示**：這 12 或 24 個恢復詞是**存取您比特幣的唯一金鑰**。Blitz 是 self-custodial 錢包：Blitz 和 Spark 都無法存取您的恢復助記詞或資金。如果您遺失了這些詞，您將永久失去對比特幣的存取權。不要與任何人分享：任何擁有這些詞的人都可以花費您的比特幣。

然後建立一個 **PIN 碼**來保護錢包的存取安全。

![setup-wallet](assets/fr/02.webp)

## 開始使用 Blitz

使用 Blitz 進行交易比大多數其他比特幣錢包更加直覺。介面極簡，圍繞三個主要操作：傳送、掃描和接收。

### 接收比特幣

要在您的 Blitz 錢包上接收比特幣，請點擊**「向下箭頭」**圖示（↓），輸入您希望接收的聰數金額，新增可選描述，錢包將產生一張帳單（invoice），您可以分享給付款人。

⚠️ **注意**：聰（satoshi，簡稱「sat」）是比特幣的最小單位：**1 比特幣 = 100,000,000 聰**。

Blitz Wallet 的特色之一是它支援比特幣生態系統中的多個網路和協議：

- **Lightning Network**：比特幣的二層網路之一，能夠以極低的手續費即時完成小額支付。非常適合日常小額消費。

- **Bitcoin (on-chain)**：比特幣協議的主鏈，適用於金額較大、需要最高安全性和最終確認性的交易。

- **Liquid Network**：由 Blockstream 開發的比特幣 sidechain（側鏈），可使用 Liquid Bitcoin (L-BTC) 進行快速且保密的交易。

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

預設情況下，Blitz 會產生一張 Lightning 帳單，但您可以透過點擊 **「Choose format」**（選擇格式）按鈕來選擇希望在哪個網路上接收聰。

![receive-sats](assets/fr/03.webp)

### 建立聯絡人

Blitz Wallet 透過聯絡人系統簡化了比特幣的定期傳送。

在**聯絡人**選單中，您可以儲存經常互動的 Blitz 使用者名稱或 Lightning 地址（LNURL）。

這樣，您只需幾次點擊即可向這些地址傳送聰，無需每次都掃描 QR code 或手動輸入地址。

### 傳送比特幣

除了經典的比特幣傳送方式（掃描 QR code、手動輸入地址），Blitz 還提供了幾種便捷選項：

- **從圖片傳送**（*From Image*）：從相簿匯入 QR code。
- **從剪貼簿傳送**（*From Clipboard*）：貼上之前複製的地址或帳單。
- **手動輸入**（*Manual Input*）：直接輸入比特幣地址、Lightning invoice 或可讀地址（例如 `使用者名稱@walletofsatoshi.com`）。
- **從聯絡人傳送**：選擇一個預先儲存的收款人，幾次點擊即可傳送。

在 **Wallet** 選單中，點擊**「向上箭頭」**按鈕（↑），選擇傳送方式，輸入傳送金額，新增描述並確認交易。

當前最低傳送金額為 **1,000 聰**。

![send-bitcoin](assets/fr/05.webp)

## Blitz 商店

除了比特幣轉帳操作，Blitz Wallet 還整合了一個商店，您可以在其中使用比特幣直接在應用程式內購買數位服務。

從主選單中，點擊 **Store** 分頁進入商店。在這裡您還可以存取 **Bitrefill** 平台，直接用比特幣從全球數千家商戶購買禮品卡。

- **人工智慧**：存取最新的生成式 AI 模型（Claude 3.5 Sonnet、GPT-4o、GPT-4o-mini、Gemini Flash 1.5），直接用聰支付積分。根據您的需求提供多種方案（Casual、Pro、Power）。

![ia-credits](assets/fr/06.webp)

- **匿名簡訊**：在全球範圍內傳送和接收簡訊，無需透露您的個人手機號碼。每則傳送的訊息以聰計費。

![sms-credit](assets/fr/07.webp)

- **WireGuard VPN**：透過訂閱 WireGuard VPN（按週、按月或按季）來保護您的線上隱私，可直接在 Blitz 商店中用比特幣支付。您只需在裝置上下載 WireGuard 用戶端應用程式即可使用。

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet 的幕後：深入了解

在 Blitz Wallet 簡潔易用的背後，隱藏著一個精心設計的技術架構，結合了比特幣生態系統的多個層級。

### 餘額分配

Blitz Wallet 以透明的方式管理您的餘額，根據需求將資金分配到不同的協議上。當您的餘額低於 500,000 聰時，Blitz 使用 **Liquid Network** 和 atomic swaps（原子交換）來為您提供流暢的體驗，即使是小額也能在 Lightning Network 上進行交易。

這種方式確保新使用者無需了解底層機制即可輕鬆上手。您可以在**設定 > Balance Info** 選單中查看餘額在各層級之間的分配情況。

![balance](assets/fr/09.webp)

### Lightning 模式（可選）

預設情況下，Blitz Wallet 使用 Liquid Network 和 Spark 協議為您提供無需技術設定的流暢體驗。不過，Blitz 允許您啟用 **Lightning 模式**，當餘額達到 **500,000 聰**（0.005 BTC）時將自動開啟一個支付通道。

要啟用 Lightning 模式，請進入**設定**，然後在**技術設定**部分，點擊 **Node Info** 選項。

![enable-lightning](assets/fr/10.webp)

得益於 Spark 協議，此啟用是**可選的**：Spark 已經能夠進行相容 Lightning 的支付，無需開啟通道或管理入站流動性。原生 Lightning 模式對於希望在應用程式內擁有自己的 Lightning 節點的進階使用者仍然有用。

### 銷售終端（PoS）

Blitz Wallet 整合了**銷售終端**功能，允許商戶直接透過應用程式接受比特幣支付。

在**設定 > Point-of-sale** 選單中，您可以設定：

- 您商店的唯一識別碼
- 用於顯示價格的當地法定貨幣
- 給員工的操作說明
- 客戶的小費選項

您的客戶只需掃描產生的 QR code 即可即時完成比特幣支付。

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

編寫本教學時使用的資源：
- [Breez](https://breez.technology/) Technology 部落格：[*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0)。
