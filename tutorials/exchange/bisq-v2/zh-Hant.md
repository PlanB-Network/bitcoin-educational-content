---
name: Bisq 2
description: 使用 Bisq 2 和交換比特幣的完整指南 P2P
---
![cover](assets/cover.webp)


## 簡介


免 KYC 點對點 (P2P) 交換對於維護使用者的機密性和財務自主性至關重要。它們可以讓個人之間直接進行交易，而無需身份驗證，這對於重視隱私的人來說至關重要。如需更深入瞭解理論概念，請參閱 BTC204 課程：


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 什麼是 Bisq 2？


Bisq 2 是 2024 年推出的流行去中心化 Bisq Exchange 的新版本。與其前身不同的是，Bisq 2 的開發支援多種 Exchange 協定，為使用者提供更大的靈活性。


**主要新功能：**




- 支援多種隱私權網路 (Tor、I2P)
- 多重身分可提高機密性
- 適用於交易機器人的 REST API
- 支援多種 Wallet 類型
- BSQ 中強制性存款的角色系統


本指南專門針對目前唯一可用的通訊協定「Bisq Easy」。Bisq Easy 是專為 Bitcoin 新用戶設計的。此協定可讓使用者在分散式點對點平台上，以法定貨幣買賣比特幣。交易額度限制為等值 600 美元（最低 6 美元），Exchange 的安全性依賴於 BTC 賣家的信譽。Bisq Easy 沒有交易費用或保證金要求。Bisq Easy 預計將取代 Bisq 1，用於低於 600 美元（或等值）的現金交換。


**主要功能：**




- 跨平台桌面應用程式
- 多種 Exchange 通訊協定可用
- 分散式 P2P 網路
- 專注於保密性（無 KYC、使用 Tor）
- 非監護（您保留對資金的控制權）
- 開放原始碼 (AGPL)


### 與 Bisq 1 的差異


**適合買家：**




- 無需保證金
- 無交易費用
- 無 Mining 費用
- 以供應商信譽為基礎的安全性
- 較低的交易限額（相當於 600 美元）


**針對賣家：**




- 無需保證金
- 建立聲譽
- 燃燒 BSQ 或建立 BSQ 鍵的可能性
- 潛在的較高銷售溢價（高於市場 10-15）


**Iportant note:** 一旦 Bisq Multisig 協定在 Bisq 2 中實施，舊版的 Bisq 就可以逐步淘汰。但是，Bisq 1 將繼續用作 Bisq CAD 和 BSQ-BTC 交換的管理工具。


### Exchange 製程




- 要約的創造者定義 Exchange 的條款
- 一旦交易者就條款（付款方式和價格）達成一致，Exchange 就開始了
- 賣方將其銀行資料寄給買方，買方將其 Bitcoin Address 寄給賣方
- 買家以現金付款並通知賣家
- 收到付款後，賣方會將位元幣傳送至買方的 Address
- 當買方收到比特幣時，Exchange 就完成了。


### 重要規則




- 在交換付款細節之前，Exchange 可以無理由取消
- 交換詳細資料後，若未履行義務，可能會被放逐
- 對於銀行轉帳，**切勿在付款原因中使用「Bisq」或「Bitcoin」等字眼**（這可能導致資金被凍結，甚至導致收款人或付款人的銀行帳戶被凍結）
- 交易員必須每天至少登入一次，以遵循流程
- 如果發生問題，交易商可以請求調解員提供服務


## 安裝與設定


### 1.下載並驗證 Bisq 2


![Téléchargement de Bisq 2](assets/fr/01.webp)




- 前往 [bisq.network](https://bisq.network/downloads/)
- 下載與您的作業系統相對應的 Bisq 2 版本（向下捲動頁面）
- 驗證下載檔案的真實性（強烈建議）。如需簽名驗證的詳細指南，請參閱以下教程：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2.根據您的系統進行安裝


請依照適合您作業系統的安裝步驟進行安裝。如果您在安裝過程中遇到任何困難，可以參考 [Bisq 官方 wiki](https://bisq.wiki/Downloading_and_installing) 上的詳細指南。


### 3.首次啟動




- 啟動 Bisq 2 並接受使用條款


![Conditions d'utilisation](assets/fr/01.webp)




- 選擇名稱和頭像以建立新個人資料


![Création du profil](assets/fr/02.webp)




- 然後，您會被帶到應用程式的主控制面板，您可以啟動 Bisq Easy 買入或賣出您的第一枚比特幣


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4.設定付款方式




- 從主功能表存取付款帳戶部分


![Liste des comptes de paiement](assets/fr/04.webp)




- 填寫必要資訊，新增付款方式


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


預先設定付款方式是可選的，但建議在交易時節省時間。您也可以在交易時直接與 Exchange 合作夥伴聯絡，設定您的付款方式。


### 5.帳戶安全


**資料備份：**


與 Bisq 1 不同，Bisq 2 目前並未整合 Bitcoin Wallet：因此交易是透過您自己的外部錢包來進行。然而，我們建議您定期備份您的 Bisq 2 資料夾。若要找到您的資料夾，請參閱 [Bisq wiki 官方網站](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory)。


**身份管理：**


Bisq 2 可讓您建立多重身分。每個身份可以用於不同類型的交易。您的身分會儲存在資料夾中。


## 買賣比特幣


### 如何購買比特幣


**選項 1：利用現有優惠**




- 在主畫面上，選擇 "Bisq Easy"，「開始 」標籤，然後點擊 「開始交易精靈」。


![Lancer trade wizard](assets/fr/06.webp)




- 選擇「購買 Bitcoin」並選擇您的貨幣


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- 設定您偏好的付款方式 (SEPA、Revolut 等)


![Configuration méthodes de paiement](assets/fr/09.webp)




- 此時，要麼您已獲得與之前條件對應的要約清單，要麼您需要前往 "Offerbook" (要約簿)


![Liste des offres](assets/fr/10.webp)




- 在第二種情況下，您可以使用 Interface 右上方的按鈕顯示和篩選報價。


![Filtres des offres](assets/fr/11.webp)




- 一旦您選擇了您的報價，您所要做的就是選擇您的付款方式，然後驗證交易摘要


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**選項二：建立您自己的報價**




- 選擇 "Bisq Easy「，然後選擇 」Offerbook"。
- 選擇您的交易對（例如：BTC/EUR）
- 按一下「建立報價
- 遵循要約建立精靈：定義金額（固定或範圍）


![Configuration du montant](assets/fr/20.webp)




- 選擇可接受的付款方式


![Sélection méthodes de paiement](assets/fr/21.webp)




  - 檢查摘要並發佈要約


![Récapitulatif et publication](assets/fr/22.webp)


一旦 Exchange 啟動 ：




- 將您的 Bitcoin Address 或 Lightning Invoice 寄給賣家


![Envoi adresse Bitcoin](assets/fr/15.webp)




- 接收賣家的銀行詳細資料


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- 付款（請勿提及「Bisq」或「Bitcoin」）。
- 通知賣家您的付款


![Notification paiement](assets/fr/18.webp)




- 等待比特幣到達


![Attente réception](assets/fr/19.webp)


### 如何出售比特幣？


Bisq 2 上的出售過程與購買過程的邏輯相似，主要步驟相同，但順序相反。您可以創建自己的銷售要約，也可以回應現有的購買要約。以下是流程中各種選項和階段的細分：


**選項 1：建立銷售要約**




- 選擇 "Bisq Easy「，然後選擇 」Offerbook"。
- 按一下「建立要約」，然後選擇「銷售 Bitcoin」。
- 配置您的報價 ：
 - 選擇貨幣（歐元、美元等）
 - 選擇接受的付款方式
 - 設定金額（相當於 6 到 600 美元之間）
 - 設定您的價格（固定或市場百分比）
- 檢查細節並發佈優惠


**選項二：接受現有報價**




- 在「Offerbook」標籤中瀏覽報價
- 依貨幣和付款方式篩選
- 選擇適合您的優惠
- 檢查詳細資訊並接受要約


**銷售流程：**


一旦啟動 Exchange ：




   - 將您的銀行資料寄給買家
   - 等待買家的 Bitcoin Address
   - 檢查 Address 是否有效


付款通知後 ：




   - 檢查您的帳戶是否已收到付款
   - 確認金額與詳細資料相符
   - 將 bitcoins 傳送至所提供的 Address
   - 標記交易完成


定稿 ：




   - 等待買家確認
   - 留下交易回饋
   - 為未來的銷售建立您的聲譽


**重要提示：** 作為賣家，您需要特別警惕扣款的風險。請優先使用安全的付款方式，並在發送比特幣之前，務必檢查是否已收到付款。


## 良好作業與安全


### 安全提示


**適合買家：**




- 從少量開始
- 檢查賣家的聲譽 (最低分數為 30,000)
- 僅使用建議的付款方式
- 發送付款前，請檢查賣家是否處於活動狀態
- 僅使用 Exchange 聊天中提供的銀行詳細資訊
- 切勿在 Bisq 2 平台之外進行通訊
- 保留付款憑證
- 切勿傳送敏感資訊


**針對賣家：**




- 小心使用新帳戶
- 避免使用對扣款敏感的付款方式 (PayPal, Venmo)
- 檢查帳戶詳細資料是否與買家相符
- 限制溝通至聊天 Bisq 2
- 如有疑問，請開啟調解


### 建立信譽（銷售人員）


為了提高您在 Bisq 上作為賣家的聲譽，請定期進行交易並與買家保持專業溝通。快速回應買家的要求，以確保良好的體驗。您也可以建立 BSQ 繫結，以顯示您對平台的 Commitment。這些行動將建立信任，吸引更多的買家。


### 爭議解決




- 透過聊天聯絡您的對應人員
- 如有必要，請開啟爭議
- 提供所有要求的證明
- 遵循調解員的指示


### 隱私權政策 ：




- 無需註冊或集中身份驗證
- 所有連線都會透過 Tor 網路 (很快也會透過 I2P)
- 無中央伺服器儲存資料
- 交易詳細資料僅可由相關各方讀取


### 防止審查：




- 完全分散式 P2P 網路
- 使用 Tor 網路 (以及即將推出的 I2P) 來抵抗審查制度
- 由 DAO 管理的開放原始碼專案，沒有中央法律實體


## 優點與缺點


### Bisq 2 的優點




- 最大保密性**：無需 KYC，使用 Tor
- 分散化**：無中央伺服器
- 安全性**：開放原始碼、非監管程式碼
- 直觀的 Interface**：比 Bisq 1 更簡單
- 彈性**：多種 Exchange 通訊協定


### Bisq 2 的缺點




- 有限的流動性**（目前） ：
 - 處於啟動階段的新通訊協定
 - 少量銷售優惠
 - 找到買家的等待時間可能很長
- 交易限額**：每筆交易最高 600 美元 (使用 Bisq easy)
- 僅限桌上型電腦**：無行動應用程式


## 未來議定書


雖然 Bisq Easy 是目前唯一可用的通訊協定，但 Bisq 2 還有其他幾個通訊協定正在開發中：




- Bisq Lightning**：Exchange 通訊協定，以在 Lightning Network 上使用多方計算密碼技術的代管系統為基礎。
- Bisq MuSig**：將主要通訊協定從 Bisq 1 遷移到 Bisq 2，使用有保證金的 2 對 2 Multisig。
- BSQ Swaps**：BSQ 與 BTC 之間的即時原子交換。
- Liquid 掉期**：Exchange 的資產在 Liquid Network (USDT, BTC-L) 上透過原子交換。
- Monero 交換**：Bitcoin 和 Monero 之間的原子交換。
- Liquid MuSig**：使用 L-BTC 的 Multisig 通訊協定版本，可降低成本並提高機密性。
- 海底交換**：Lightning Network 上的 Bitcoin 與 Bitcoin On-Chain 之間的交換。
- 穩定幣交換**：Bitcoin 和美元穩定幣之間的原子交換。
- Multisig 期權**：在 On-Chain Multisig 交易中建立 BTC 封鎖的 P2P 看跌和看漲期權。
- Multisig 開放式合約**：可使用套利的 2 對 3 Multisig 系統建立自訂條件合約。


這些通訊協定目前正在開發中，並將逐步整合到 Bisq 2 中，根據使用者的特定需求提供更大的靈活性。


## 有用資源




- 官方網站：[bisq.network](https://bisq.network)
- 文件：[Bisq Wiki](https://bisq.wiki)
- 支援：[Forum Bisq](https://bisq.community)
- 原始碼 ：[GitHub](https://github.com/bisq-network)