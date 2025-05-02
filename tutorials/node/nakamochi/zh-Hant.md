---
name: Nakamochi
description: Node Running Made Easy - 如何設定和使用 Nakamochi Bitcoin 和 Lightning 節點。
---

運行您自己的 Bitcoin 和 Lightning Full node 不再是技術專家才能完成的複雜任務。傳統上，建立和管理節點需要深入的密碼學、網路和軟體開發知識。Nakamochi 不論技術背景，讓每個人都能使用節點，改變了這種情況。


有了 Nakamochi，任何人都可以在家建立並運作一個節點，實現完全隱私和財務獨立。運行 Full node 不僅能保障您自己交易的安全，還能為 Bitcoin 網路的強大做出貢獻。分散且有彈性的 Bitcoin 網路仰賴廣泛的節點分佈，以確保其安全性和獨立性。


### 目錄



- 什麼是 Nakamochi，它如何運作？
- 設定 Nakamochi
- 關於 Lightning Network
- 在 Lightning Network 中開啟通道並進行交易



## 什麼是 Nakamochi，它如何運作？


Nakamochi 是 Bitcoin 專用的 Full node，同時支援 Bitcoin 和 Lightning 網路。它包含整合式 Bitcoin 和 Lightning Wallet，讓使用者可以執行安全、自主控的 Bitcoin 節點，同時受惠於 Lightning Network 的速度和低交易成本。


您的 Nakamochi 節點可透過行動應用程式 [BitBanana (Android)](https://bitbanana.app) 和 [Zeus (iOS)](https://bitbanana.app) 進行管理，讓您隨時隨地都能方便地控制節點。這些應用程式就像是您節點的遙控器，讓您可以直接使用 Bitcoin 或 Lightning 付款、管理交易、開啟或關閉通道、檢查餘額，以及監控您節點的效能，一切都輕鬆簡單。



## 設定 Nakamochi 只需 5 分鐘


### 步驟 1：插上電源並開始使用


1.將 Nakamochi 連接到電源和 Wi-Fi。

2.按一下 **「設定新的 Wallet」**，並安全地儲存您的 24 字復原短語。

3.使用節點管理應用程式 (Zeus 或 BitBanana) 連接到您的 Nakamochi：

4.開啟應用程式並掃描 Nakamochi 上顯示的 QR 代碼。

5.為了增加安全性，請在裝置上設定 PIN 碼。


![image](assets/en/01.webp)

_連接電源並寫下您的 24 字 seed 詞組_


![image](assets/en/02.webp)

_Wait until the Blockchain has caught up_


![image](assets/en/03.webp)

_在 Lightning Tab 中設定新的 Wallet_


![image](assets/en/04.webp)

使用節點管理應用程式掃描 QR 碼_


![image](assets/en/05.webp)

_為了更安全，請設定 PIN 碼_________________________。


**注意：** _讓您的 Nakamochi 節點與 Blockchain 同步。這個過程可能需要一些時間，視您的網際網路連線而定。



## 關於 Lightning Network


Bitcoin Lightning Network 徹底改變了 Bitcoin 的交易方式，讓交易更快、更便宜、更有效率。它非常適合日常使用，能以最低的費用實現近乎即時的支付，非常適合買咖啡或處理頻繁的小額消費等微型交易。

通過運行 off-chain，Lightning 被設計成可擴展的，每秒支援數以千計的交易，而不會使主要的 Bitcoin Blockchain 負荷過重。這使其成為 Bitcoin 演變為實用的全球支付系統的關鍵角色。

隱私是另一個優勢，因為 Lightning 上的交易是透過私人支付渠道進行，而不是直接記錄在 Blockchain 上。這可確保以更隱密的方式進行交易，同時維持 Bitcoin 的穩健安全性。



#### 付款管道說明


Lightning Network 透過支付通道進行操作，這是雙方之間的連接，允許進行多筆交易，而無需直接與 Blockchain 進行互動。當通道打開時，雙方之間的餘額會在第二個 Layer Lightning 解決方案上更新，以進行每筆交易，確保快速、低成本的付款。只有通道的開啟和關閉才會被 On-Chain 記錄下來，從而減少 Bitcoin Blockchain 上的擁擠情況。這種設計確保了可擴展性和隱私性，因為個別交易在公共 Ledger 上不會被記錄下來。


**Example:** Alice 和 Bob 通過提交 Bitcoin 來打開一個通道。Alice 發送比特幣給 Bob，他們的 off-chain 結餘立即更新，沒有 On-Chain 記錄。如果 Alice 繼而付款給 Charlie，而 Alice 沒有直接通往 Charlie 的通道，則付款可以透過 Bob 的通道路由到 Charlie。即使沒有直接連線，透過中介節點的路由也能確保付款，使網路變得非常有效率。



## 在 Lightning Network 中開通渠道並進行交易


一旦您的 Nakamochi 設定好並連接到節點管理應用程式，您就可以開始使用 Lightning Network，開啟通道並進行交易。


### 在 Zeus (iOS) 上開啟頻道：


1.移至 **「頻道」** 標籤（底部功能表）。

2.按一下 **"+"** 開啟新頻道。

3.掃描或輸入您要連線的節點的 pubkey。

4.輸入鎖定的金額（與您的同儕一起選擇，或使用知名節點的最低固定金額）。

5.按一下 **「開啟頻道」**。


![image](assets/en/06.webp)

_ZEUS 螢幕截圖_


如需詳細資訊：[Channels | Zeus Documentation](https://docs.zeusln.app/)


### 在 BitBanana (Android) 上開啟頻道：


1.開啟漢堡包功能表（左）。

2.移至 **「頻道 」**。

3.按一下 **"+"** 以新增/開啟新頻道。

4.掃描或貼上公開金鑰。

5.輸入鎖定的金額（與您的同儕一起選擇，或使用知名節點的最低固定金額）。


![image](assets/en/07.webp)

_Bitbanana 螢幕截圖_


如需更多資訊：[BitBanana](https://bitbanana.com)


一旦您的通道打開，就可以透過它向網路中的其他參與者付款。餘額會以 off-chain 調整，確保交易幾乎是即時的，並產生最少的費用。

如果您不再需要某個頻道，您可以關閉它。這個動作會結算您和對等方之間的最終餘額，並記錄在 On-Chain 中。理想的情況是雙方都同意並在線進行「合作關閉」（相對於沒有回應/離線的對等「強制關閉」更快、費用更少）。

一般而言，我們建議保持通道開放，以降低成本並提高網路可靠性和效率。透過保持通道開放，您可以將 On-Chain 交易費用降至最低，避免因通道重新連線而造成的停機時間，並維持穩定的路由能力，以進行無縫支付處理。此方法可建立強大且具彈性的網路，同時提升整體使用者體驗並減少營運開銷。



### 有用連結



- [關於 Nakamochi](https://nakamochi.io/)
- [訂閱 Nakamochi 電子報](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)