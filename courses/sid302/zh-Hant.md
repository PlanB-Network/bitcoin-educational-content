---
name: Liquid Bootcamp Essentials
goal: 全面了解 Liquid Network 和 Elements 專案，並學習如何在機密交易、代幣化和分散式網路架構中實現先進的解決方案。
objectives: 

  - 瞭解 Liquid 架構的基本原理及其與 Bitcoin 的關係。
  - 學習使用 Elements 軟體設定和操作 Liquid 節點。
  - 探索在 Liquid Network 上使用保密交易和資產發行。
  - 掌握 Liquid 在資本市場應用的商業和技術層面。

---

# 介紹到 Liquid 網路


踏上旨在深入瞭解 Liquid Network 和 Elements 專案的教育之旅。本開發營結合理論與實務，教您實作與運用 Liquid 功能所需的技術、架構與商業基礎。從機密交易到生態系統設計，本課程非常適合想要擴展 Bitcoin 生態系統內進階工具知識的人。


透過業界專家的演講，課程涵蓋的主題包括 Liquid 架構、標記化應用、Elements 的技術概念，以及 Breez SDK 等創新使用案例。課程的設計適合初學者和中級使用者，同時也提供有經驗的開發人員掌握 Liquid 作為優化專案平台的價值。

+++

# 簡介


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## 課程總覽


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


歡迎來到 Liquid Bootcamp，這是一個全面的訓練，旨在讓您掌握有效利用 Liquid Network 和 Elements 專案的知識與技能。本課程全面探討 Liquid 的特色，包括 Confidential Transactions、資產發行及其聯盟網路架構，同時也介紹 Elements 的基礎概念，Elements 是為 Liquid 提供動力的軟體。


在整個訓練營中，您將探討 Liquid Network 的實際應用，從建立和操作節點，到瞭解其在 Bitcoin 資本市場和代用幣化的使用。透過業界專家的演講，您還將深入瞭解 HTLC、Breez SDK 和 Blockstream AMP 專案等進階主題。


本開發營原本是以現場活動的形式進行，遵循專為現場課程設計的結構化時間表（如圖所示）。然而，在此課程改編中，內容經過重新組織，以更適合線上形式並促進學員的理解。新的順序確保了從基礎概念到更先進和技術性主題的邏輯進程，從而最大化學習體驗。


此旅程的結構設計可滿足不同專業程度的參加者，提供理論知識與實務經驗的結合。在本訓練營結束時，您將對 Liquid 的架構、其與 Bitcoin 的整合，以及如何利用其創新功能來建立和最佳化財務解決方案有堅實的了解。


立即潛入 Liquid 側鏈的世界，發揮其全部潛力！

# 基礎


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid 架構


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network 架構與共識模型


Liquid Network 是建構在 Elements 原始碼基礎上的聯邦式側鏈，旨在擴展 Bitcoin 的功能，同時依賴其基本的安全性。與 Bitcoin 的 Proof-of-Work 不同，Liquid 以聯邦共識模式運作。該網路由一個分佈於全球的會員群體負責維護，其中包括交易所、交易台和基礎設施供應商。從這些成員中，選出十五位「功能人員」擔任區塊簽署者。


這些功能人員以確定的循環方式產生區塊，每分鐘產生一個新區塊。這種精確的時間安排與 Bitcoin 的 10 分鐘概率間隔形成對比。要使一個區塊有效，它需要 15 位功能人員中至少 11 位的簽名（三分之二加一的門檻）。此機制讓 Liquid 具備「兩區塊終局性」，意即一旦交易獲得兩次確認 (約兩分鐘)，在數學上就不可能重組區塊鏈。這種速度和確定性對於套利、自動化交易和快速的交易所間結算都是至關重要的。


聯盟是動態的。透過動態聯盟 (Dynafed) 通訊協定，網路可以輪換功能人員或更新參數，而不需要硬體 fork。這可讓系統在維持連續運作的同時，無縫地演進和更換硬體或成員。


### Confidential Transactions 與資產管理


Liquid 的決定性特徵是其原生支援 Confidential Transactions (CT) 和多重資產。在主 Bitcoin 鏈上，所有交易細節 - 發貨人、收貨人和金額 - 都是公開的。在 Liquid 中，CT 使用加密承諾來隱藏公共帳簿中的資產類型和金額，同時仍允許網路驗證交易是否有效（即沒有發生通貨膨脹）。只有持有保密鑰匙的參與者才能查看具體數值，為移動大量倉位的機構提供了必要的商業隱私級別。


Liquid 將所有資產視為區塊鏈的「原生」公民。這包括 Liquid Bitcoin (LBTC)、穩定幣（如 USDT）和安全代幣。發行資產不需要複雜的智慧契約；這是協定的基本功能。


#### 受規管資產與 AMP

對於需要合規的資產，例如安全代幣，Liquid 採用 Blockstream 資產管理平台 (AMP)。這引入了一個許可層，交易需要授權伺服器的第二個簽章。這可讓發行商在細微層面上強制執行規則，例如白名單或 KYC 要求，將區塊鏈的效率與傳統金融的監管控制相結合。


### 雙向 Peg 與安全基礎架構


Liquid 和 Bitcoin 之間的連線透過雙向掛接保持。若要「掛入」，使用者會將 Bitcoin 傳送至 mainchain 上所產生的位址。這些資金會鎖定 102 次確認（約 17 小時），以消除重組風險。一旦確認，就會在 Liquid 側鏈上鑄造等量的 LBTC。


Peg-out" 程序可讓使用者將 LBTC 兌換成 Bitcoin。這需要燃燒 LBTC 和聯盟的加密授權。為了防止盜竊，peg-out 由聯盟成員持有的 Peg-out 授權密鑰 (PAK) 嚴格控制。此外，資金可透過第三方供應商（如 SideSwap）即時交換，繞過結算延遲，以加快流動性。


#### 硬體安全模組 (HSM)

安全性透過硬體嚴格執行。功能人員不會在標準伺服器上保留私人金鑰；相反地，他們會操作硬體安全模組 (HSM)。這些裝置與主伺服器的邏輯隔離，並依據嚴格的規則編程。例如，如果區塊的高度不比前一個大，HSM 會拒絕簽署該區塊，以防止歷史重寫。這種「對抗式」安全模型假設主伺服器可能會被攻破，以確保金鑰即使在實體位置被攻破時仍能保持安全。


## Elements 的基本原理


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements：Liquid 的基礎


Elements 是一個開放源碼的區塊鏈平台，源自 Bitcoin 核心程式碼庫。Elements 擴展了 Bitcoin 的功能，使獨立於側鏈的區塊鏈能夠將資產轉移到 Bitcoin 或從 Bitcoin 轉移資產。Bitcoin Core 為 Bitcoin 網路提供動力，而 Elements 則是 Liquid Network 和其他自訂側鏈背後的軟體引擎。


關係很直接：Liquid 是 Elements 側鏈的特定「實例」，配置為聯邦共識模型的生產用途。熟悉 Bitcoin 的開發者會發現 Elements 很直覺，因為它保留了相同的 RPC (Remote Procedure Call) 介面和命令列結構 (`elements-cli`、`elements-d`、`elements-qt`)。關鍵的差異在於設定：設定 `chain=liquidv1` 會將節點連線到主 Liquid 網路，而 `chain=elementsregtest` 則會啟動一個本機的回歸測試環境，開發人員可以在這個環境中即時 generate 區塊並進行測試，而不需要外部的依賴。


#### 資產發行

Elements 的一個突出特點是原生資產發行。與代幣是複雜的智慧契約的 Ethereum 不同，Elements 的資產是透過簡單的 RPC 指令 (`issueasset`)所建立的一等公民。


- 唯一識別碼：** 每項資產都有一個唯一的 64 位元十六進位 ID。
- 再發行代幣：** 發行者可選擇建立再發行代幣，賦予持有人日後鑄造更多資產的權利（對於穩定幣或安全代幣非常有用）。
- 資產註冊處：** 由於十六進位 ID 並非人類可讀，Blockstream 資產註冊處會將這些 ID 映射到名稱和股票代號 (例如「USDT」)，類似於資產的 DNS。


### 透過 Confidential Transactions 隱私權


Elements 解決了公共區塊鏈的主要限制之一：缺乏商業隱私。在 Bitcoin 上，每筆交易金額都是全世界可見的。Elements 引入了 **Confidential Transactions (CT)**，它以加密方式隱藏了金額和資產類型，同時仍允許網路驗證交易的有效性。


這是使用 **Pedersen Commitments** 和 **Range Proofs** 來實現的。


- Pedersen Commitments** 以加密承諾取代可見金額。由於同態加密的關係，驗證者可以檢查 *輸入承諾 = 輸出承諾 + 費用*，而無需看到實際數值。
- 範圍證明**透過數學證明隱藏值是有效範圍內的正整數，防止使用者憑空創造金錢（例如使用負數）。


對於外部觀察者而言，保密交易顯示有效的輸入和輸出，但卻隱藏了傳送的*內容*和*數量*。只有寄件者和收件者（擁有保密鑰匙）可以檢視明文資料。


### 開發與 RPC 工作流程


與 Elements 節點互動主要是透過其 JSON-RPC 介面完成。這允許使用 Python、JavaScript 或 Go 寫成的應用程式與區塊鏈進行通訊。



- 設定:** 開發人員通常以 `regtest` 模式啟動。這允許即時產生區塊 (`generateblock`)，以立即確認交易，繞過即時網路 1 分鐘的區塊時間。
- 指令：** `getblockchaininfo` 等標準 Bitcoin 指令，以及 `dumpblindingkey` (用於稽核 CT) 或 `pegin` (將 BTC 移入側鏈) 等 Elements 特定指令。
- 別名：** 為了管理多個節點 (例如，用於測試的 「寄件者」 和 「收件者」)，開發人員通常會使用 shell 別名，例如 `e1-cli` 和 `e2-cli` 指向不同的資料目錄，在單一機器上模擬對等網路。


此架構可讓開發人員利用 Bitcoin 生態系統強大且熟悉的工具，建立複雜的金融應用程式，例如證券平台或私人付款閘道。


## 連接 Bitcoin 層


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cross-Layer 基礎架構和 HTLC


Bitcoin 生態系統已演進為多層架構，其中主鏈提供結算，閃電提供速度，而 Liquid 則可實現先進的資產功能。在這些層級之間移動價值而無需集中式中介，需要一種無信任的加密基元：Hash 時間鎖定 Contract (HTLC)。


HTLC 會建立一個有條件的付款通道，以原子方式連結獨立系統。它透過兩個主要的限制條件來運作：**雜湊鎖定**和**時間鎖定**。


- Hash 鎖：** 如果接收者透露出符合特定加密雜湊值的秘密「前影像」，資金就可以立即使用。
- 時間鎖定：** 如果接收方未能在設定的時間範圍內（區塊高度）揭露秘密，原發送方就可以收回資金。


這種雙路徑結構可確保安全性。在跨層交換中，兩個網路使用相同的哈希鎖。當接收方在其中一層（例如 Liquid）揭露秘密以索取資金時，寄件方便可看到該秘密，然後寄件方可使用該秘密在另一層（例如 Lightning）索取對等資金。這種加密約束保證了交換對雙方都能成功完成或失敗，消除了一方失去資金而另一方獲得資金的風險。


### Taproot 和 MuSig2 升級


傳統 HTLC (SegWit v0) 功能良好，但存在隱私和效率方面的缺點。它們需要發布整個腳本邏輯 on-chain，使得區塊鏈分析師很容易識別掉期交易，而且由於其數據量較大，因此成本較高。Taproot (SegWit v1) 和 MuSig2 協定的推出徹底改變了這種架構。


Taproot 允許透過 MuSig2 進行**金鑰聚合**。MuSig2 可讓交換參與者將其密鑰合併為單一匯總的公開密鑰，而不是揭示包含多個公開密鑰的複雜腳本。


- 合作「關鍵路徑」：** 如果雙方都同意交換（「快樂路徑」），他們會共同簽署交易。對於網路來說，這與標準的單一簽章付款完全相同。它消耗最小的區塊空間，並且完全不透露任何關於交換條件的資訊。
- 逆向「腳本路徑」：** 如果一方變得不回應或惡意，底層腳本 (包含哈希/時間鎖定) 才會被揭露。這會以 Merkle 樹的方式組織，讓誠實的一方只揭露回收資金所需的特定分支，而隱藏契約邏輯的其他部分。


### 實際執行：Liquid-閃電交換


實際上，這些通訊協定可讓 Bitcoin 的各層之間進行無縫交換。典型的 Liquid 到 Lightning 的交換開始於客戶向服務提供商提出交換請求。用戶端提供 Lightning 發票，服務提供商將等價的 Liquid Bitcoin (L-BTC) 鎖定到啟用 Taproot 的 HTLC 位址中。


原子性會在付款結算時強制執行。要領取 L-BTC，服務提供商必須擁有預設影像。只有在成功支付客戶的 Lightning 發票時，服務提供商才能獲得此預設影像。當 Lightning 付款完成時，預設影像就會顯示出來，讓服務提供者可以解鎖 Liquid 資金。


#### Wallet 抽取與 UTXO 管理

對於終端使用者來說，這種複雜性是完全抽象化的。Aqua 等現代錢包在後台處理密鑰生成、發票創建和簽署過程。用戶只需使用他們的 Liquid 結餘 「支付 」一張 Lightning 發票。在幕後，服務會管理 UTXO 的整合，定期清理小額、無人認領或退款的輸出，以維持 wallet 的效率，並在高流量期間將費用影響降至最低。


## Liquid Network 概觀


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network 架構與共識


Liquid Network 以聯盟側鏈的形式運作，建構於 **Elements** 程式碼庫之上。Elements - Bitcoin Core 的 fork - 提供軟體基礎，而 Liquid 則是生產網路的實作。Liquid 與 Bitcoin 的 Proof-of-Work 不同，Proof-of-Work 依賴具有競爭力的 mining，而 Liquid 則使用 **Federated Consensus** 模型。


該網路由十五個分佈在全球各地的「功能人員」維護。這些實體操作專門的伺服器，執行兩個關鍵的角色：

1.  **區塊製作：** 功能人員以確定的輪循排程輪流建立區塊，準確地每分鐘產生一個新區塊。

2.  **區塊簽署：** 要使一個區塊有效，必須由 15 位功能人員中的至少 11 位簽署。


此 11-15 的臨界值可確保網路最多可容忍四個節點故障而不會停止。這種取捨的主要優點在於**決定性的最終**。Bitcoin 處理的是概率，而 Liquid 則是在兩個區塊 (約兩分鐘) 之後達到結算確定性。一旦一個區塊上面有一個確認，該區塊鏈就無法重新組織，因此對於套利和快速結算非常有效。


### Confidential Transactions 與本土資產


Liquid 的界定特徵是預設使用 **Confidential Transactions (CT)**。在 Bitcoin mainchain 上，寄件人、收件人和金額都是公開的。Liquid 改善了這一點，將金額和資產類型以加密方式隱藏，同時保留寄件者和收件者的位址以供驗證。


為了確保使用者無法印錢 (例如傳送負數)，Liquid 採用了 **Pedersen Commitments** 和 **Range Proofs**。這些加密原始碼允許網路驗證 *Inputs = Outputs + Fees*，以及所有值都是正整數，而不會向公共帳簿透露具體數字。只有持有保密金鑰的參與者才能檢視解密後的資料。


#### 資產發行

Liquid 將所有資產視為 「原生」。無論是 Liquid Bitcoin (L-BTC)、穩定幣（如 USDT），還是證券 token，它們都擁有相同的架構。發行資產不需要智慧契約，只需要簡單的 RPC 呼叫。


- 不受管制的資產：** 任何人都可以不經許可而發行。
- 受監管資產：** 利用 Blockstream 資產管理平台 (AMP)，發行商可透過要求授權伺服器在移動資產前進行第二次簽章，以強制執行合規規則（如 KYC/AML）。


### 雙向 Peg 和動態聯盟


Bitcoin 和 Liquid 之間的橋梁是 **雙向 Peg**。它允許使用者將 BTC 移動到側鏈（Peg-in）並返回到 mainchain（Peg-out）。


**鎖入程序：**

這是無允許的。使用者發送 BTC 到聯邦控制的地址。為了防止 Bitcoin 區塊鏈重組，這些資金必須等待 **102 確認**（約 17 小時），才會在側鏈上鑄造等值的 L-BTC。


**汰換過程：**

要返回 Bitcoin，需要燒掉 L-BTC。然而，為了防止基礎 Bitcoin 儲備被盜，掛鉤退出並非完全自動化。它們需要持有 ** Peg-Out Authorization Key (PAK)** 的會員授權。Bitcoin 資金本身是由 11-15 個多重簽章的 wallet 所保護，金鑰存放在硬體安全模組 (HSM) 中，與功能人員的主伺服器隔離。


**Dynamic Federation (Dynafed):**

為了確保長期使用，Liquid 採用了 Dynafed 協定，此協定可讓網路在沒有硬體 fork 的情況下輪換功能人員或更新參數。如果需要更換功能人員，網路會廣播轉換交易。經過兩週的重疊期後，新的組態就會接手，讓聯盟能夠無縫演進，同時維持連續的正常運作時間。


## 生態系統與資本市場


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network：商業策略與生態系統


Liquid 不只是技術上的側鏈；它是以業務為重點的基礎架構層，旨在處理 Bitcoin mainchain 無法有效支援的資本市場的複雜需求。Lightning Network 優化了高頻、低價值支付，而 Liquid 則針對高價值轉移、資產發行和交易所間結算。


此生態系統由 **Liquid 聯盟** 所推動，該聯盟由 ~73 家公司組成，包括交易所、交易平台和基礎設施供應商。此合作模式與傳統的金融交換中心相同，但運作透明度更高，交割時間大幅縮短 (2 分鐘對 T+2 天)。


### 真實世界資產 (RWA) 的代幣化


Liquid 的核心商業案例是「代幣化」--將真實世界的價值（股票、債券、mining 合約）表示為區塊鏈上的數位代幣。這提供了三個主要優勢：

1.  **24/7 全球市場：** 取消銀行服務時間和地域限制。

2.  **Operational Efficiency:** 透過共用、不可變更的分類帳消除對帳錯誤。

3.  **原子結算：** 透過確保交付與付款同時進行，降低交易對手風險。


#### 受規管資產與 AMP

由於法律規定，大多數機構資產都無法進行無允許交易。** 資產管理平台 (AMP)** 是執行這些規則的技術標準。


- 白名單：** 發行人可以限制 KYC 驗證過的地址才能持有和交易。
- Multisig 控制：** 透過多重簽名授權管理合規行動 (例如凍結竊取的資金或重新簽發遺失的代幣)，確保沒有任何一位員工可以單方面採取行動。


此基礎設施已於今日啟用。像**Stalker**這樣的平台在歐洲提供端對端的代幣化服務，而**Sideswap**則扮演分散式交易所和非保管wallet的角色，讓**Blockstream Mining Note (BMN)**和代幣化 MicroStrategy 股票 (CMSTR)等資產的點對點交易成為可能。


### 真實世界的成功：Mayfell 個案研究


墨西哥**Mayfell**最能證明 Liquid 的效用。在傳統融資依賴紙本期票的市場中，期票容易遺失、詐騙、處理速度緩慢，Mayfell 將整個基礎架構轉移到 Liquid。



- 規模：** 發行超過 25,000 張期票，代表**15 億美元以上**的價值。
- 隱私權：** 使用 Liquid 的 Confidential Transactions，貸款金額只有出借人和借款人可以看到，在保護商業隱私的同時，也允許稽核人員驗證帳簿的完整性。
- 影響：** 透過區塊鏈將非銀行貸款機構與全球資本市場連接起來，Mayfell 降低了成本，並擴大了墨西哥中小企業獲得信貸的機會，證明 Liquid 的價值主張遠遠超出了投機交易的範圍。


### 與其他連鎖店的策略定位


Liquid 在眾多代幣化平台（Ethereum、Solana 等）的市場中競爭，但它擁有明顯的策略優勢：


- 監管明確：** Liquid 使用 Bitcoin (L-BTC) 作為其原生資產。它沒有預挖 token 或 ICO，避免了其他 L1 區塊鏈所面臨的「未登記證券」風險。
- 穩定性：** 不同於以太坊的帳戶模型，交易失敗仍會燒掉瓦斯費，Liquid 的 UTXO 模型對於關鍵任務的財務資料而言，是確定且可靠的。
- 隱私權：** 預設保密性是大多數金融機構的要求，Liquid 原生提供此項功能，而公有鏈若不使用複雜的附加元件，則很難實現此項功能。


對開發人員而言，這個生態系統提供了一個明顯的機會：建立工具 (儀表板、錢包、合規整合)，橋樑傳統金融與 Bitcoin 的安全結算層。


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP：Liquid上的許可資產控制


Blockstream AMP (資產管理平台) 作為 Liquid Network 上的重要基礎架構層級，專為受監管的數位證券和穩定幣發行者所設計。雖然 Liquid 提供無權限的基礎層與原生資產發行，但受監管的實體通常需要嚴格的監督與合規能力。AMP 在不犧牲 Liquid 的 Confidential Transactions 隱私權優勢的情況下，透過在特定資產上引入許可控制層，彌補了這一差距。


該平台的核心價值主張基於兩項主要功能：發行人的全面可見性和交易授權。標準的 Liquid 資產除了參與者之外，所有人都不知道其金額和類型，而 AMP 資產則不同，它允許發行人維持完全的 unblinded 稽核追蹤。這種透明度對於監管報告和內部審計非常重要。此外，AMP 透過共同簽署機制執行嚴格的授權模式。AMP 資產的每次轉移都需要 AMP 伺服器的簽章。這可讓發行商執行複雜的 off-chain 規則，例如凍結帳戶、將經認證的投資者列入白名單，或施加轉讓限制，在分散式網路中有效地扮演集中式看門人的角色。


#### 操作權衡

此架構引入了特定的權衡。系統依賴於 AMP 伺服器的可用性；如果伺服器作為共同簽署人而離線，資產的流動性就會暫停。此外，雖然使用者與使用者之間的隱私得以維護，但投資人必須接受發行人對其持有的資產有完全的可見性。這種模式非常適合符合規定的安全代幣，但不適合抗審查的加密貨幣。


### 架構演進與整合路徑


AMP 生態系統目前正從第一次迭代過渡到更靈活、更具互操作性的「第 2 版」架構。舊系統要求發行商維護完全同步的 Elements 節點，並迫使開發人員嚴重依賴單一的 Green SDK。雖然功能強大，但卻造成了很高的技術障礙，並限制了 wallet 的選擇。


下一代架構將複雜性轉移到伺服器，從根本上簡化了這些需求。在這個新模式中，AMP 伺服器處理交易建立、UTXO 選擇和費用計算等繁重的工作。它向發行者展示只需要簽名的部分簽名 Elements 交易 (PSET)。這種「智慧型伺服器，啞巴 wallet」的方式讓發行商無需執行完整的節點，並可使用硬體錢包和標準的多重簽章設定來進行金庫管理。


對開發人員而言，這種演進意味著從專屬 SDK 轉向標準描述符和 PSET 工作流程。錢包現在可以向 AMP 伺服器註冊多重簽章描述符，以建立授權權利。這讓 AMP 開發符合更廣泛的 Bitcoin wallet 標準，讓任何能夠處理 PSBT/PSET 格式的應用程式都能進行整合。我們鼓勵開發人員利用 Liquid Wallet Kit (LWK) 等工具來進行目前的建置，這些工具支援這些以描述符為基礎的現代架構，可確保他們的應用程式未來能符合新的 AMP 標準。


### Liquid Wallet 生態系統與機密性


由於原生資產和 Confidential Transactions 等功能，在 Liquid 上建立應用程式需要瀏覽比標準 Bitcoin 開發更複雜的堆疊。生態系統由分層架構支援：低階函式庫（如 `secp256k1-zkp` ）處理加密基元，而較高階的工具套件則管理 wallet 邏輯。


過去，Green 開發套件 (GDK) 提供了全面但僵化的解決方案。現代的替代方案是 Liquid Wallet 套件 (LWK)，它提供了模組化的方法。LWK 將關注點分隔成不同的板塊，獨立處理描述符、簽章和硬體通訊，讓開發人員可以靈活地建立客製解決方案，而不需要單一程式庫的開銷。


#### 處理 Confidential Transactions

在這個生態系統中，最明顯的挑戰是管理盲點生命週期。在 Liquid 中，交易輸出使用橢圓曲線 Diffie-Hellman (ECDH) 金鑰交換加密。寄件者使用收件者的保密公開金鑰來加密資產金額和類型，產生範圍證明，在不透露數值的情況下驗證交易的有效性。


要讓 wallet 運作，它必須成功逆轉這個過程。當 wallet 偵測到進入的交易時，它會嘗試使用私人保密金鑰解除輸出的保密。如果共用密碼相符，wallet 就可以解密數值，並將其加入使用者的餘額。此過程屬於計算密集型，需要精確管理致盲因子，以確保交易在數學上達到平衡，而 LWK 之類的工具就是要為開發者抽象出這種複雜性。


# 技術


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeless


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Breez Liquid SDK 簡介


Breez Liquid SDK 是一個自我監護的開放原始碼工具包，旨在彌補 Liquid Network 與更廣泛的 Bitcoin 生態系統之間的差距。其主要任務是抽象 Lightning Network 節點管理和原子交換的複雜性，讓開發人員建立無摩擦的金融應用程式。


以「行動為先」的理念打造，核心邏輯以 Rust 撰寫，以確保效能與安全性，但它利用 UniFFI (Unified Foreign Function Interface)，提供 Kotlin、Swift、Python、C#、Dart 和 Flutter 的原生綁定。這可確保開發人員可將 Bitcoin 功能整合至其偏好的環境，而無需管理低階加密作業。


**支援的交易類型：**

SDK 以 Liquid 為「大本營」。它擅長三種特定操作：

1.  **Liquid 至 Liquid：** 直接 on-chain 轉移。

2.  **Liquid 至 Lightning：** 使用 Liquid 資金支付 Lightning 發票。

3.  **Liquid-to-Bitcoin:** 直接將資金交換至 Bitcoin mainchain。


*注意：SDK 不支援直接的 Lightning-to-Lightning 或 Bitcoin-to-Bitcoin 交易。它絕對是以 Liquid 為中心的工具。


### 付款架構：海底掉期


為了在沒有集中保管人的情況下實現 Liquid、Lightning 和 Bitcoin 之間的互操作性，Breez 依賴 **Submarine Swaps**。這些都是原子操作，交易不是在兩個網路都成功完成，就是在兩個網路都失敗，以確保資金不會在傳輸過程中遺失。


#### 閃電發送 (潛艇交換)

當用戶支付 Lightning 發票時，SDK 會在 Liquid Network 上廣播 「鎖定 」交易。這會有效地將資金託管。掉期提供者 (Boltz) 會偵測到這一情況，支付 Lightning 發票，然後用支付前影像（加密收據）來索取鎖定的 Liquid 資金。


#### 閃電接收 (反向潛艇交換)

接收 Lightning 是一個相反的過程。用戶生成發票，交換提供商將資金鎖定在 Lightning Network 上。SDK 透過 WebSockets 監控這個過程。一旦確認鎖定，SDK 會自動執行索償交易，將等額資金轉入用戶的 Liquid wallet。


#### 交叉鏈 Bitcoin

對於 Liquid 到 Bitcoin 的傳輸，架構使用「雙交換」機制。鎖定交易同時在兩條鏈上發生。寄件者在 Bitcoin 上申領資金，而收件者在 Liquid 上申領資金。這樣就可以實現無信任橋接，而無需依賴 federated peg 出口或集中式交換。


### 開發人員 Interface 和自動化管理


Breez SDK 將複雜的財務流程濃縮為標準的三個步驟，簡化了開發人員的經驗： **連接、準備和執行**。


1.  **Connect:** 初始化 wallet，使用 Liquid Wallet 套件 (LWK) 與區塊鏈同步，並建立 WebSocket 連線以進行即時監控。

2.  **Prepare:** 在投入資金之前，此步驟會計算並回傳所有相關的網路費用和交換成本，讓使用者介面可以向使用者呈現清楚的總計。

3.  **Execute:** 此步驟會建構交易、廣播交易並啟動交換。


#### 自動化安全機制

SDK 最重要的功能之一是 **自動退款管理**。在網路故障或交易對手不合作的情況下，理論上資金可能會卡在時間鎖定的合約中。SDK 將恢復邏輯完全抽象化。它會監控每個交換的狀態；如果交換失敗或超時，SDK 會自動建立並廣播退款交易，將資金退回到用戶的 wallet 中。


此外，SDK 還會處理 **Metadata Resolution**。它將 off-chain 交換資料（由 Boltz 交換器提供）與 on-chain 交易歷史合併。這可確保使用者的交易歷史是人類可讀的、顯示發票詳細資料和付款內容，而不只是原始的十六進位交易哈希值。


# 最後部分


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## 評論與評分


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## 期末考試


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## 總結


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>