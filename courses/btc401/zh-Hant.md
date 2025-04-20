---
name: Bitcoin 開發加速器
goal: 取得在 Bitcoin 上開始開發的所有基礎
objectives: 

  - 瞭解 Bitcoin 的核心概念和技術基礎。
  - 獲得 Bitcoin 安全、軟體開發和網路治理的實務技能。
  - 掌握 Lightning Network 及其相關協議。

---
歡迎來到 Bitcoin 的 Cubo+ 開發課程！

在接下來的 20 個小時中，您將深入了解 BTC 和 LN 協定。本課程專為想要開始在 BTC 生態系統中工作，並尋求紮實了解 BTC 和 LN 不同技術堆疊的程式設計師所設計。

這些影片是在薩爾瓦多舉行的 CUBO+ 2023 新兵訓練營中現場錄制的，成功地將世界知名的老師們聚集在一起。由於 Fulgure Venture 的慷慨解囊，以及教師、Bitcoin 辦公室、DecouvreBitcoin 和許多其他參與者的通力合作，本課程得以免費提供。

請盡情享用！

+++
# 簡介和預備課程

<partId>43a835de-c4e7-542b-9d1a-c92f049e88e6</partId>

## CUBO+ 課程簡介

<chapterId>dcf2d37e-b32a-5eb8-aaa3-41ac92475ba9</chapterId>

:::video id=9b6aa5cf-245e-4a66-b3b8-c4860ab51e90:::

Filippo 和 Mario 提供了 CUBO+ 2023 的介紹性講座，為等待中的全面學習旅程奠定基礎。他們討論了課程的結構、學習成果，以及這些成果將如何增強學生在 Bitcoin 開發領域的能力。

### 目標

本課程旨在讓學員深入瞭解 Bitcoin 的基本原理、實用開發技巧，以及有效導航和貢獻 Bitcoin 生態系統的能力。透過理論知識與實務練習的結合，學員將掌握 Bitcoin 安全性的要點、其軟體堆疊的複雜性，以及其治理機制。

### 先決條件

參加者應具備強烈的好奇心、專業水平的學習熱情，以及一定的開發基礎知識。雖然不需要具備 Bitcoin 的詳細背景，但對編碼原則的基本瞭解，以及對複雜技術概念的開放態度，對充分利用加速器是非常重要的。

#### 工具

在整個課程中，學員將利用關鍵工具來幫助理解並提升學習體驗。使用 Linux、命令列 Interface、GitHub 和 Docker 將是提供 Bitcoin 開發實作方法不可或缺的一環。這些工具將有助於使用 Bitcoin 軟體堆疊、管理開發環境，以及在實際環境中進行專案協作。

## 為何選擇 Bitcoin

<chapterId>89a0aa8b-90bd-58b2-82b3-bc5e1f82eaeb</chapterId>

### 為何薩爾瓦多需要 Bitcoin

:::video id=ff820fb2-83d4-450f-bda0-17cc5044a902:::

歡迎來到**Cubo Plus**教育計畫的第一講。今天，我們將在**Bitcoin Italia Podcast**創辦人 Ricky 的帶領下，深入了解 Bitcoin 的世界。Ricky 是一位熱心的人權活動家，他使用 Bitcoin 作為保護和促進人權的工具。Ricky 擁有超過六年的經驗，他走遍各地，記錄薩爾瓦多、危地馬拉等新興市場採用 Bitcoin 的情況。他的工作不僅限於播客；他也活躍於 YouTube (**Bitcoin Explorers**) 和 Twitter (**BTC Explorer**, **Ricky6**)。Ricky 之所以選擇 Commitment 到 Bitcoin，是因為他相信 Bitcoin 能提供財務自由和隱私，挑戰傳統的中央銀行系統。

![Unbanked Population](assets/en/1/1.webp)

_全球無銀行戶籍人口_

### Bitcoin：金融自由及其對薩爾瓦多的影響

本演講**「為什麼薩爾瓦多需要 Bitcoin」**概述了**Bitcoin 協定**、其在**Cypherpunk 運動中的根源**，以及其作為促進自由的**不加密貨幣**、**金融包容性**等工具的作用。

> **定義：**
>

> - 比特幣協定：_規範 Bitcoin 作為分散式數位貨幣如何運作的規則和結構。
> - _Cypherpunk movement:_一個提倡使用密碼學來確保數位空間隱私與自由的團體。
> - _金融包容性：_為被排除在傳統銀行體系之外的人提供金融服務，這些人通常被稱為 「沒有銀行服務的人」。
> - 不受政府或金融機構控制或限制的貨幣。
#### Ricky 的背景和 Bitcoin 倡議

Ricky 的 Bitcoin 之旅源於他身為人權倡導者的工作。他相信 Bitcoin 可以讓個人控制自己的財務，讓他們保護自己的隱私，避免中央銀行的限制。他對 Bitcoin 在薩爾瓦多等地採用的探索，突顯了這項技術如何能讓新興市場的人們獲得財務獨立。

### Bitcoin 的全球意義與挑戰

Bitcoin 不只是一種數位貨幣。它是保護隱私和確保財務自由的工具。透過使用像主密碼一樣的**私人金鑰**，使用者可以安全地管理他們的 Bitcoin，並完全控制他們的資金。

在專制政權下，金融鎮壓很常見，Bitcoin 的**不可感知性**可讓人們進行交易，而不必擔心資金會被凍結或沒收。Bitcoin 的**開放源碼**性質鼓勵全球參與，促進社群持續改善網路。

![Image](assets/en/1/4.webp)

儘管 Bitcoin 具備潛力，但仍面臨著重大的挑戰。在非洲和印度等地區，往往缺乏電力和網際網路等基本基礎設施，限制了技術的採用。此外，**數位包容** - 確保所有年齡層和教育程度的人都能使用技術 - 仍是一大障礙。

> **定義：**
>

> - _Private keys:_可以存取使用者 Bitcoin 的密碼。
> - _Open-source:_ 任何人都可以檢查、修改和改進的軟體。
### 薩爾瓦多案例

薩爾瓦多決定採用 Bitcoin 作為法定貨幣，顯示了其轉型潛力。透過使用 Bitcoin，該國力求吸引外國投資並促進金融穩定。像**Bitcoin 海灘**這樣的專案，展現了當地經濟如何透過採用 Bitcoin 作為 Exchange 的方式來成長。

然而，全球 Bitcoin 的採用仍面臨無知、對新技術的抗拒以及基礎建設的挑戰等障礙。邁向更具包容性的金融體系 - Bitcoin 可協助提升發展中國家的地位 - 的道路雖然漫長，但卻充滿希望。Bitcoin 的分散性和開放源碼特性，為人人都能享有金融公平的未來帶來了希望。

#### 總結

總而言之，Bitcoin 對於金融授權和包容性具有無限的希望，但前方仍有重大的挑戰。與 Bitcoin 社群保持聯繫、學習並提出問題，將是實現分散式金融未來的關鍵。透過合作與宣導，為所有人打造更公平金融體系的願景將可成為現實。

### Cypherpunk 運動與奧地利經濟學

![video](https://youtube.com/live/KIaC31YQLBA)

#### Cypherpunk 機芯

**Cypherpunk 運動**興起於 20 世紀末期，提倡透過加密來保護隱私與自由。像 **Eric Hughes** 和 **Tim May** 之類的先驅認為，強大的加密功能對於保護數位世界中的個人自由至關重要。他們的想法在很大程度上影響了 Bitcoin 的創建。

> **定義：**
>

> - _Cypherpunk:_運用密碼學促進隱私與自由的運動。
#### 奧地利經濟學

同時，**奧地利經濟學**為 Bitcoin 的貨幣原則奠定了基礎。路德維希‧馮‧米塞斯（**Ludwig von Mises**）和弗里德里希‧哈耶克（**Friedrich Hayek**）等經濟學家認為，健全的貨幣應該是稀缺的、持久的，並且是良好的價值儲存工具，這些核心原則塑造了 Bitcoin 的設計。

> **定義：**
>

> - _Scarcity:_ 有限的可用性，透過謹慎分配的需求來創造價值。
### Bitcoin 的創作

**Satoshi Nakamoto** 結合這些想法，於 2008 年創造 Bitcoin 作為一種分散式、可抵抗審查的數位貨幣。Bitcoin 將 Cypherpunk 的隱私權理想與奧地利的健全貨幣原則相結合，提供了一個挑戰傳統銀行和政府控制的金融體系。

> **定義：**
>

> - _Censorship-resistant:_ 不受外力控制或阻擋的金錢。
#### 主要經濟原則


- 稀有性：** Bitcoin 的固定 Supply 可確保其價值長久不變。
- 時間偏好：** 鼓勵為未來儲蓄，而非立即花費。
- 儲存：** 儲存價值以備未來之需，進而進行投資與創新。

> **定義：**
>

> - 時間偏好：_ 重現在的物品而非未來的物品。
> - 儲存：_ 儲存價值以供未來使用。
### 薩爾瓦多的 Bitcoin

薩爾瓦多採用 Bitcoin 反映出其作為金融自由工具的潛力，透過促進自願採用和分散化，與**奧地利經濟學**一致。此舉挑戰了傳統的金融體系，解決了關鍵問題：競爭、壟斷和沒收。

![Image](assets/en/1/5.webp)


- 競爭**：Bitcoin 提供傳統銀行業務以外的選擇，讓薩爾瓦多人可以繞過金融守門人，選擇更符合其需求的服務，從而為金融市場引入競爭。
- 壟斷**：Bitcoin 透過分散金融存取，打破銀行和政府發行貨幣的壟斷，減少對中央機構的依賴，促進金融包容性。
- 沒收**：Bitcoin 對沒收的抗拒，讓薩爾瓦多人能夠控制自己的資產，保護他們的財富不被外來攫取，並提升金融主權。

薩爾瓦多採用 Bitcoin 可促進一個更具包容性、競爭力和安全性的金融體系，挑戰傳統金融的限制。

#### 總結

Bitcoin在**Cypherpunk運動**和**奧地利經濟學**的基礎上，使其成為一種獨特且革命性的貨幣形式。了解這些原則有助於掌握 Bitcoin 的創立原因及其今日的運作方式。如需進一步閱讀，請考慮**Saifedean Ammous**所著的**Bitcoin Standard**。

感謝您參與這份材料！

## Bitcoin 如何

<chapterId>d800970a-0d8e-5557-810a-7aef845d4a34</chapterId>

### Bitcoin 的技術堆疊

:::video id=2c008198-7f4e-4e60-87a0-0af17528ad2f:::

在「如何使用 Bitcoin」課程的第一講中，我們開始探索 Bitcoin 網路的技術堆疊。我們涵蓋的主題包括**Hashcash**、**transactions**、**Blockchain**、**Lightning Network**，以及 Bitcoin 通訊協定的其他關鍵元件。

### Bitcoin 的技術堆疊第二部分

:::video id=752343b8-aa78-4bd3-9320-efe2a7e9d88f:::

在「How Bitcoin」的第二場講座中，我們對 Bitcoin 的技術堆疊進行了更深入的檢視。

### Bitcoin 結構

Bitcoin 的起源是基於幾項重要的創新，首先是**Adam Back 的 Hashcash**，這是一個 Proof-of-Work (PoW) 系統，目的是透過要求寄件者完成計算任務來防止垃圾郵件和拒絕服務攻擊。這個 PoW 概念成為 Bitcoin 安全性的基石。

Bitcoin 依賴**數位簽章**，使用**橢圓曲線加密**來保護和驗證交易。橢圓曲線數位簽章演算法 (ECDSA)** 可確保只有 Bitcoin 的合法擁有者才能授權交易，而不會洩露其私人金鑰。

*Bitcoin 的化名創造者 *Satoshi Nakamoto** 將 PoW 模式轉換為分散式的 **Blockchain**，從而擴展了這些想法。這使得分散式節點網路可以在沒有中央機關的情況下驗證和記錄交易，標誌著之前數位貨幣嘗試的重大演進。

> **定義：**
>

> - _Proof-of-Work (PoW)：_ 參與者必須解決計算謎題以驗證交易並確保網路安全的系統。
> - _Elliptic Curve Cryptography:_一種可實現安全、高效數位簽章的加密方法。
### Blockchain 機制與交易驗證

Bitcoin 交易由 **miners** 驗證並加到區塊中，這些 miners** 競爭使用 Proof-of-Work 演算法解決加密謎題。這包括透過調整 **Nonce** 值，找出具有特定前導零數目的 Hash，直到找到正確的 Hash。

Blockchain 中的每個**區塊**都由一個**標頭**（包含類似前一個區塊 Hash 的資料）和一個交易清單組成。第一個區塊稱為 **Genesis 區塊**，由於沒有前一個區塊，因此是獨一無二的。

![Image](assets/en/1/6.webp)

在交易納入區塊之前，它們會存放在 **Mempool**，等待驗證。一經驗證，這些交易就會加入新挖出的區塊，然後再加入 Blockchain。

> **定義：**
>

> - 挖礦：_ 解開加密謎題，將新區塊加入 Blockchain 的過程。
> - _Nonce:_ 在 Mining 期間用來尋找正確 Hash 的值。
> - _Mempool:_ 在未確認的交易加入區塊前的等待區。
### Bitcoin 中的可擴展性、隱私和開發

Bitcoin 面臨與擴充性和隱私權相關的挑戰。Blockchain 的交易容量有限，難以處理大量交易。類似 **Lightning Network** Address 的解決方案可透過付款管道進行 off-chain 交易，提高速度和隱私性，從而克服這些挑戰。

運行**Full node**對於確保分散性和安全性至關重要，但**簡化支付驗證 (SPV) 節點**允許以犧牲部分安全性為代價的輕度參與。

Bitcoin 的開發已演進至提升效能與安全性。主要升級包括**分離見證 (SegWit)**，可解決交易可篡改性問題，並增加有效區塊大小；以及**Taproot**，可改善隱私性，並允許使用**抽象語法樹 (MAST)** 來簽訂更複雜的合約。

> **定義：**
>

> - _SegWit:_ Bitcoin 升級，可將簽章資料與交易資料分離，提高效率。
> - _Taproot:_一項升級，可透過啟用更複雜的智慧型契約，增強 Bitcoin 的隱私權和可擴充性。
> - _Lightning Network:_ 第二個 Layer 解決方案，可使用付款管道進行更快速、更便宜的 Bitcoin 交易。
#### 總結

Bitcoin 的結構和持續演進展示了其技術的創新性和適應性。從 **Hashcash** 到去中心化的 Blockchain，從 **SegWit** 到 **Taproot**，Bitcoin 繼續 Address 在可擴展性、隱私和安全性方面的挑戰。社群的持續努力確保 Bitcoin 保持彈性和分散性，同時不斷演進以滿足未來的需求。

## 揭穿 Bitcoin

<chapterId>171ec71d-3028-5820-9b4f-36682113fc81</chapterId>

### 揭穿 Bitcoin

:::video id=c5e2e575-fa9d-4430-805f-205c2cf6f2a5:::

在本講座中，我們將揭開圍繞**Bitcoin**、**區塊鏈**和**加密貨幣**的常見迷思。讓我們來 Address 關於 Bitcoin 能源消耗、犯罪用途的錯誤觀念，以及對這項技術散播的廣泛「FUD」（恐懼、不確定、懷疑）。

### Bitcoin vs. Blockchain

一個常見的誤解是**Bitcoin**和**Blockchain**是相同的。Bitcoin 是一種數位貨幣，而 **Blockchain** 則是為其提供動力的技術。區塊鏈可提供經驗證的交易記錄，但也有速度較慢、成本較高的缺點，而**Lightning Network** Address 等解決方案則可提供這些優點。

> **定義：**
>

> - 區塊鏈：_ 用於在分散、不可變的 Ledger 中記錄交易的底層技術。
> - _Lightning Network:_ 第二個 Layer 解決方案，可透過啟用 off-chain 交易來提高 Bitcoin 的交易效率。
### Bitcoin 對 Crypto

另一個關鍵區別是，**Bitcoin** 創建的唯一目的是提供一種去中心化、抗審查的貨幣形式，不受任何公司或政府的控制。相比之下，加密貨幣 **shitcoins** 的設計通常都是集中式控制，主要是為了讓背後的公司透過掠奪式行為、抽水拋售計劃或徹頭徹尾的詐騙賺錢而存在。這些代幣除了讓其創造者快速獲利之外，通常都沒有真正的目的，而是犧牲不明真相的投資者。然而，Bitcoin 是唯一真正去中心化的數位貨幣，其安全性和復原能力已獲得證實。

> **定義：**
>

> - 糞幣：_糞幣是指缺乏實際效用的低價值或品質有問題的加密貨幣。它們通常具有高度投機性，有時是為了欺詐目的或在沒有明確目的的情況下，利用加密貨幣市場的蓬勃發展而創造出來的。
![Image](assets/en/1/2.webp)

### 能源消耗與環境影響

對 Bitcoin 最常見的批評之一是其**能源消耗。雖然 Bitcoin Mining 確實會使用能源，但它只佔全球耗電量不到 1%，而且浪費的能源也不到 3%。此外，**Bitcoin Mining** 常常利用未使用或可再生的能源，使其比通常所描述的更環保。

> **定義：**
>

> - _Bitcoin Mining:_通過解決加密字謎來驗證交易和保障網路安全的過程，這需要計算能力。
### 關於犯罪用途的誤解

Bitcoin 常被批評為用於犯罪活動。然而，Blockchain 分析顯示，只有一小部分的 Bitcoin 交易與犯罪有關。實際上，傳統金融系統中的犯罪用途遠超過 Bitcoin。

### 隱私權與可攜性

**隱私性**和可替代性**是 Bitcoin 的基本特征。隱私性可保護在壓迫制度下的使用者，而可替代性則可確保每個 Bitcoin 都是平等的，不論其歷史如何。這使得 Bitcoin 成為一種可靠且公平的貨幣形式。

> **定義：**
>

> - 可流通性：_ 貨幣的特性，其中每個單位都可以與另一個單位互換，以確保價值相等。
### 處理 FUD 和市場動態

圍繞 Bitcoin 的 FUD 常常誇大對其環境影響、犯罪用途和安全性的疑慮。儘管市場會出現波動，但 Bitcoin 分散且健全的技術為長期穩定與財務自由奠定了堅實的基礎，尤其是在委內瑞拉等限制性環境中。

#### 總結

了解 Bitcoin 的能源消耗、隱私特性以及在犯罪預防方面的作用等現實，有助於消除圍繞它的迷思。藉由撇開 FUD，我們可以欣賞 Bitcoin 作為一種革命性的健全貨幣形式，促進隱私、安全和分散化的潛力。

## 運行 Bitcoin

<chapterId>5f638ec9-a6c1-5716-b27f-d837ab896eb1</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

### 安裝 Bitcoin 核心

:::video id=4a5253cf-b863-466a-8506-0506b28a28de:::

在第四模組的第一講中，我們探討了 Bitcoin 的架構和 Bitcoin 核心節點的安裝。

### 執行 Bitcoin 節點

**1.簡介重溫**

歡迎回來！在上一節中，我們介紹了 Bitcoin 架構背後的基本概念，包括其加密基礎和對等網路結構。今天，我們將透過示範如何安裝和設定 Bitcoin 節點，從理論走向實務。

**2.實務會議概述**

在這一課中，Alekos 將教我們如何使用虛擬機器設定 Bitcoin 節點。本教學旨在讓您熟悉設定節點參與 Bitcoin 網路的步驟。

運行 Bitcoin 節點包括驗證交易和區塊、執行共識規則，以及支援網路的去中心化。建立節點可確保您與 Bitcoin 網路直接連線，讓您為其安全性和完整性做出貢獻。

在這個講座中，您會找到安裝和執行自己的 Bitcoin Core 的指南，學習如何修剪 Blockchain 以節省空間，並開始實驗使用軟體。Alekos 將逐步引導您完成這個令人興奮的過程。

### Bitcoin Core 的功能與優點

透過執行 Bitcoin Core，您可以獲得以下能力：


- 驗證您自己的交易和區塊**：確保遵循 Bitcoin 網路的規則，而無需依賴第三方。
- 強化網路**：藉由參與網路，您可以協助保持網路的分散性，讓 Bitcoin 更能抵擋攻擊。
- 修剪 Blockchain**：只保留最近的交易，減少儲存需求，如果您的磁碟空間有限，這是最理想的選擇。
- 使用先進的 Wallet 功能**：隱私且安全地管理您的 Bitcoin、離線使用 generate 私密金鑰，以及安全地簽署交易。
- 直接與 Bitcoin 網路互動**：使用 Bitcoin Core，您可以直接與網路連線，無須經過中介，確保獲得最精確的資料。
- 受益於增加的隱私**：身為 Full node 業者，您不必信任外部服務，可保護您的交易隱私不受外部監控。

運行 Bitcoin 節點的好處對任何專注的比特幣玩家來說都是巨大的。您不僅可以幫助保護網路安全並加強其分散性，還可以提高您的隱私權，確保您自己交易的完整性，並在 Bitcoin 生態系統中扮演積極主動的角色。運行一個節點是實現金融主權和完全接受 Bitcoin 去中心化特性的關鍵一步。

### 基本指令

這些是設定節點時的一些基本指令：


- 檢查 Bitcoin daemon** 的狀態：

```bash
sudo systemctl status bitcoind
```


- 啟動 Bitcoin daemon：**：

```bash
systemctl start bitcoind
```


- 停止 Bitcoin daemon：**：

```bash
sudo systemctl stop bitcoind
```


  - 取得詳細資訊**：

```bash
bitcoin-cli getblockchaininfo
```


- 剪枝 Blockchain 只保留最近的區塊，以節省磁碟空間：**：

```bash
prune=550
```


- 啟用 Bitcoin 核心伺服器並設定 RPC 設定：**：

```bash
server=1
rpcuser=yourusername
rpcpassword=yourpassword
```


- 檢查 Bitcoin daemon** 的狀態：

```bash
sudo systemctl status bitcoind
```


- 檢查 Bitcoin Wallet 的餘額：**：

```bash
sudo systemctl status bitcoind
```

### 安裝 C-lightning

:::video id=e13a1407-46e3-4b03-9a7a-b0f4a338c3c7:::

#### 1. **Bitcoin 核心重溫**

讓我們先簡單回顧一下在雲端虛擬機器上安裝 Bitcoin Core 的步驟，因為這對我們之後的 C-Lightning 設定非常重要。

**在雲端虛擬機器上重新安裝 Bitcoin Core**

首先，您要在虛擬機器上重新安裝 Bitcoin Core。在此環節中，我們將跳過二進位檔的驗證，以節省時間，但請記住，在生產環境中，驗證二進位檔是確保安全性的關鍵步驟。

**下載並驗證檔案哈希值**

首先，下載最新的 Bitcoin Core 版本，並驗證檔案哈希值，以確保沒有發生篡改。

```sh
wget https://bitcoin.org/bin/bitcoin-core-22.0/bitcoin-22.0-x86_64-linux-gnu.tar.gz
sha256sum bitcoin-22.0-x86_64-linux-gnu.tar.gz
# Compare the output hash with the official hash
```

**安裝二進位檔，並使用 systemd 設定自動啟動**

接下來安裝二進位檔，並使用 systemd 設定為自動啟動。

```sh
tar -xzf bitcoin-22.0-x86_64-linux-gnu.tar.gz
sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-22.0/bin/*
```

**建立 systemd 服務檔案：**

```sh
sudo nano /etc/systemd/system/bitcoind.service
```

**新增以下設定：**

```ini
[Unit]
Description=Bitcoin daemon
After=network.target
[Service]
ExecStart=/usr/local/bin/bitcoind -daemon
User=bitcoin
Group=bitcoin
Type=forking
PIDFile=/var/lib/bitcoind/bitcoind.pid
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

**建立和設定 Bitcoin 使用者和目錄**

為 Bitcoin Core 建立專屬使用者並設定目錄。

```sh
sudo adduser --disabled-login --gecos "" bitcoin
sudo mkdir -p /var/lib/bitcoind
sudo chown bitcoin:bitcoin /var/lib/bitcoind
```

**透過修剪 Blockchain** 使用最少的磁碟空間

若要節省磁碟空間，請在組態檔案中啟用修剪功能。

```sh
sudo nano /var/lib/bitcoind/bitcoin.conf
```

新增下列各行：

```ini
prune=550
```

完成這些步驟後，Bitcoin Core 就能以最少的磁碟使用量運作，並與 C-Lightning 進行互動。

#### 2. **C-Lightning 概觀與安裝**

**C-Lightning 概觀**

C-Lightning 也稱為 Core-Lightning，是一種 Layer 2 協定，可使用 off-chain 通道促進更快速、更便宜的交易。它的突出之處在於其模組化和開發人員友好的架構，可透過外掛進行廣泛的客製化。

**模組化和外掛擴充的重要性**

C-Lightning 的模組化設計意味著您可以根據需要增加或移除功能，使您能夠根據特定的使用案例來定制系統。使用範例包括


- 付款處理**：自訂外掛程式可處理特定付款條件。
- 路由費**：根據網路條件動態調整路由費。
- 自動化**：自動化任務，例如頻道管理和流動資金供應。

### C-Lightning 安裝

讓我們繼續安裝 C-Lightning。

**使用最新的穩定版本**

在本講座中，我們會使用最新的穩定版，例如 22.11.1。

```sh
wget https://github.com/ElementsProject/lightning/releases/download/v22.11.1/clightning-v22.11.1.tar.gz
sha256sum clightning-v22.11.1.tar.gz
# Verify the hash against the provided hash
```

**使用 GPG 金鑰驗證完整性**

務必使用 GPG 金鑰驗證下載檔案的完整性。

```sh
gpg --recv-keys <developer-key-id>
gpg --verify clightning-v22.11.1.tar.gz.asc clightning-v22.11.1.tar.gz
```

**安裝相依性並從原始碼編譯**

安裝必要的相依性，並從原始碼編譯 C-Lightning。

```sh
sudo apt-get update
sudo apt-get install -y autoconf automake build-essential git libtool libgmp-dev \
libsqlite3-dev python3 python3-mako net-tools zlib1g-dev
tar -xzf clightning-v22.11.1.tar.gz
cd clightning-v22.11.1
./configure
make
sudo make install
```

**設定 systemd 服務自動啟動**

為 C-Lightning 建立 systemd 服務檔案：

```sh
sudo nano /etc/systemd/system/lightningd.service
```

新增下列設定：

```ini
[Unit]
Description=C-Lightning daemon
After=network.target bitcoind.service
[Service]
ExecStart=/usr/local/bin/lightningd
User=bitcoin
Group=bitcoin
Type=simple
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

#### 3. ** 設定與設定**

**建立必要的目錄和設定檔案**

建立 C-Lightning 所需的目錄和設定檔。

```sh
sudo mkdir -p /var/lib/lightning
sudo chown bitcoin:bitcoin /var/lib/lightning
sudo -u bitcoin nano /var/lib/lightning/config
```

在設定檔中加入以下幾行：

```ini
network=testnet
log-level=debug
plugin=/usr/local/libexec/c-lightning/plugins
```

*設定 C-Lightning 與 Testnet 上的 Bitcoin 核心連線***

加入下列行數，以確保 C-Lightning 可以與 Bitcoin Core 連線：

```ini
bitcoin-datadir=/var/lib/bitcoind
bitcoin-rpcuser=<rpcusername>
bitcoin-rpcpassword=<rpcpassword>
```

**確保相容性與同步性**

啟動服務，並確保它們是相容和同步的。

```sh
sudo systemctl start bitcoind
sudo systemctl start lightningd
sudo systemctl enable bitcoind
sudo systemctl enable lightningd
```

**Address 檔案路徑與權限，特別是 Tor 整合**

設定檔案路徑和權限，以確保順利運作，尤其是使用 Tor 來保護隱私時。

```sh
sudo apt-get install tor
sudo -u bitcoin nano /var/lib/lightning/config
```

新增下列內容以整合 Tor：

```ini
proxy=127.0.0.1:9050
```

** 備份 HSM 用於基金恢復的秘密**

備份 HSM 秘密以進行資金復原。

```sh
sudo cp /var/lib/lightning/hsm_secret /path/to/secure/location
```

**測試連線和驗證節點的運作狀態**

最後，透過測試連線來驗證您節點的運作狀態，並確保一切運作符合預期。

```sh
lightning-cli getinfo
```

按照這些步驟，您就可以將功能完整的 C-Lightning 設定連接到 Bitcoin 核心節點，準備進行 Testnet 交易。

#### 結論與問題

總括而言，今天我們介紹了重新安裝 Bitcoin Core 的基本步驟，接下來是安裝和設定 C-Lightning 的詳細步驟。如果您有任何問題，歡迎現在提出，或準備在下一節再進一步說明。請記住，實際上機經驗非常重要，因此請使用我們討論過的 Testnet 設定，以獲得更多心得。

### 安全與硬體裝置

:::video id=8b4baf24-1350-46b8-a87b-18678ed219ed:::

### Specter 和 Ledger 裝置

#### 簡介

歡迎來到 Bitcoin 的安全與裝置設定講座。今天的重點是了解安全工具的運用，特別是 Specter 桌面 Wallet 和 Ledger Hardware Wallet，以及如何有效配置它們以增強 Bitcoin 的安全性。

**工具：Specter Desktop Wallet 和 Ledger 模擬器**

Specter 是一個桌面 Wallet 設計，方便建立和管理 Bitcoin 錢包，尤其是使用硬體設備的錢包。在示範中，我們將採用 Ledger 模擬器，模仿 Ledger Hardware Wallet 的功能。

**Ledger裝置與公司爭議的差異**

廣受歡迎的 Hardware Wallet 裝置 Ledger 因其強大的安全性而備受稱頌。然而，Ledger 背後的公司卻因為各種關於使用者資料隱私的爭議而備受審查。了解實體裝置的安全性與該公司的作法之間的差異，對於知情使用而言至關重要。

**安全模型：multi-sig 錢包和多樣化硬體的重要性**

Bitcoin 安全性的一個關鍵方面是利用多重簽章 (multi-sig) 錢包。multi-sig 錢包需要多個私人金鑰來授權交易，可大幅提升安全性。此外，使用不同類型的硬體錢包可分散風險並加強安全模式。

### 設定與組態

**下載和設定 Specter**

安裝過程的第一步是從官方資源庫下載 Specter。驗證下載的完整性以避免軟體受損是非常重要的。下載完成後，在桌面上安裝 Specter 並啟動應用程式。

**設定 Specter 與 Bitcoin Core 或 Electrum 伺服器連線**

要設定 Specter，您需要將其連接到 Bitcoin Core 或 Electrum 伺服器。這些伺服器提供 Wallet 作業所需的 Blockchain 資料。配置包括在 Specter 的設定中設定伺服器 Address，並確保連線穩定。

**解釋衍生路徑與公開金鑰擷取**

瞭解衍生路徑對 Wallet 管理非常重要。衍生路徑定義密鑰如何從主密鑰產生。在 Specter 中，您可以透過連接 Hardware Wallet（或模擬器）並瀏覽 Wallet Interface 來擷取公開金鑰。確保您記錄這些路徑，以供日後參考。

**Practical Demonstration：使用 Ledger 模擬器**

現在我們要使用 Ledger 模擬器來取得金鑰。這包括將模擬器連接到 Specter，導覽到金鑰管理部分，並選擇適當的金鑰來建立 Wallet。

**在 Specter 中建立和管理錢包**

在 Specter 中建立 Wallet 非常簡單。存取 Wallet 建立 Interface，輸入必要的詳細資訊，並包含您擷取的公開金鑰。建立後，您就可以管理 Wallet、監控交易，並確保穩健的安全實務。

**接收和監控交易**

設定 Wallet 之後，接收交易就像分享您的 Wallet Address 一樣簡單。Specter 可即時監控收到的交易，確保您隨時掌握 Wallet 的最新狀態。

### 進階組態

**設定遠端 Specter daemon**

對於進階使用者而言，設定遠端 Specter daemon 可提升存取性與安全性。這包括設定遠端伺服器以執行 Specter 的後端，允許從不同裝置進行安全存取。

**啟用 Tor 來保護隱私**

為了保護隱私，強烈建議設定 Specter 使用 Tor。Tor 會將您的網路流量匿名化，保護您的 IP Address 免遭潛在監控。這對關心隱私和安全的使用者尤其重要。

**安全連接遠端節點**

連接遠端節點時，請確保連線安全。這包括使用 SSL/TLS 證書和驗證節點的真實性。安全連線可防止中間人攻擊，並確保資料完整性。

**Debugging Issues：實用技術**

遇到問題是不可避免的。實際的除錯工作包括檢查使用者權限、驗證資料目錄存取權限，以及檢視日誌是否有錯誤。例如，確保 Specter 具有存取 Bitcoin Core 資料目錄的必要權限，以避免作業中斷。

** 問題範例：資料目錄存取**

常見的問題是資料目錄存取不正確。請確認 Specter 設定中 Bitcoin 核心資料目錄的路徑是否正確。這可確保 Specter 能存取 Wallet 作業所需的 Blockchain 資料。

**下一步與整合**

正如我們所總結的，接下來的步驟包括將 Specter 與 Lightning Network 整合。這樣就可以從 Specter 向 Lightning 節點發送資金，促進更快更便宜的交易。未來的課程將詳細介紹這一整合，以增強您的 Bitcoin 交易能力。

**Block Timing Variability**

瞭解區塊時序的變化至關重要。Bitcoin 區塊可能會以不同的間隔進行挖掘，從而影響交易確認時間。在所有配置和 Wallet 作業中，都必須考慮到這種可變性。

**學習資源**

如需額外學習，請考慮 "Mastering the Lightning Network "和 Rusty Russell 的教學等資源。這些資料提供有關 Lightning 節點和進階 Bitcoin 配置的深入知識。

**節點安裝與 Tor 安全**

安裝節點，不論是本機或遠端安裝，都能從使用 Tor 強化安全性中獲益。運行自己的節點可以確保個人交易驗證，提高安全性和隱私性。

**理念：自給自足的學習**

擁抱自給自足的哲學。實用技能和自學是最重要的，往往超越正規教育的效益。參與實務練習，加深您對 Bitcoin 安全性的了解。

**隱私權考量**

避免使用會追蹤或記錄交易的服務，以維護隱私。匿名性對於安全的 Bitcoin 作業至關重要，謹慎選擇服務有助於保護您的身份和交易記錄。

使用 Specter 和 Ledger 設定 Bitcoin 的安全性和裝置設定講座到此為止。歡迎提出任何問題或要求澄清討論的任何觀點。

## 改善 Bitcoin

<chapterId>4fdd032f-2b05-5f24-a094-297d64f939de</chapterId>

### Bitcoin 生態系統中尚未解決的問題

:::video id=6d771eca-3f53-493d-8937-db6ddb2cf172:::

十多年來，Bitcoin 已經證明是金融界的轉型創新，在全球範圍內成功運作，並為數位經濟開啟了新的可能性。然而，它仍面臨著需要創新與合作解決方案的挑戰。Bitcoin 的持續演進為有興趣塑造分散式金融未來的人提供了獨特的機會。

![Image](assets/en/1/8.webp)

#### Bitcoin 可用性中尚未解決的問題

儘管 Bitcoin 已經存在超過十年，但仍然面臨重大的可用性挑戰。使用者可使用的工具和介面往往缺乏較傳統金融系統的成熟度和易用性。這一點在薩爾瓦多等地區尤為明顯，在這些地區，Bitcoin 的採用已經得到了政府的認可。這方面的主要問題是需要更好的抽象，以簡化使用者體驗，讓即使只有極少技術知識的個人也能使用 Bitcoin。

#### 可擴充性的未解決問題

可擴展性一直是 Bitcoin 發展過程中的老大難問題。該網路處理大量交易的能力仍然有限，經常導致 On-Chain 費用高昂，使某些使用者無法參與。雖然 Lightning Network 等解決方案透過啟用 off-chain 交易提供了一些緩解措施，但卻無法完全 Address 解決可擴展性的問題。顯而易見，我們需要更全面的解決方案，既能處理不斷增加的交易量，又不影響網路的完整性。

#### 安全方面的未解決問題

保護 Bitcoin 資產安全是一項複雜的任務，充滿挑戰。通常用於日常交易的 Hot 錢包，會構成重大的安全風險，尤其是對那些操作 Lightning 節點的人而言。此外，繼承 Bitcoin 資產的規劃仍是一個迂迴曲折且經常不安全的過程。這些安全措施的複雜性會讓潛在使用者卻步，並使廣泛採用變得複雜。

#### 隱私權的公開問題

隱私權是 Bitcoin 生態系統中的另一個關鍵問題。雖然隱私權對於安全性而言至關重要，但 Bitcoin 目前的架構所提供的隱私權功能有限。On-Chain 交易很容易被追蹤，對使用者的匿名性構成風險。雖然 Lightning Network 具備提升隱私權的潛力，但仍需大幅改善。透明度與隱私權之間的平衡十分微妙，需要創新的解決方案來確保使用者的安全性與隱私權。

#### 彈性的未解決問題

Bitcoin 通訊協定的彈性對於改善隱私、安全性和擴充性是必要的。然而，過高的彈性也可能成為漏洞，可能成為攻擊媒介，並威脅到網路的分散性。取得適當的平衡對於維持 Bitcoin 通訊協定的完整性和彈性至關重要。

### 強化 Bitcoin 的權衡取捨

#### 可用性與安全性與隱私權

![Image](assets/en/1/7.webp)

提高 Bitcoin 可用性的努力往往是以犧牲安全性和隱私為代價的。例如，用戶友好型保管錢包（如 Satoshi 的 Wallet）提供了可使用的 Interface，但在安全性和隱私性方面卻大打折扣。簡化的系統可能會增加可用性，但卻可能導致 Address 重複使用等問題，破壞隱私。因此，任何可用性的改善都必須小心權衡潛在的安全性與隱私權的取捨。

#### 擴充性與隱私權衡

在 Bitcoin 網路中，可擴充性與隱私權經常會發生衝突。提高可擴展性的增強功能，如更大的 UTXO 或減少加密混淆，通常會降低隱私性。相反地，Monero 的環狀簽章等注重隱私的技術會增強使用者的匿名性，但卻會對可擴展性造成負面影響。此外，有狀合約的引入（如在 Ethereum 中所見）提供了更大的靈活性，但卻以降低安全性和可擴展性為代價。平衡這些權衡是一個複雜的挑戰，需要仔細的考量。

### 隱私權技術

在 Bitcoin 中，不同的隱私權處理方式都有各自的取捨。隱私權模糊化（Privacy by obfuscation）是指增加更多的資訊來模糊相關的資料，可以提高隱私權，但可能會使網路變得複雜。例子包括 Monero 和 Zcash。另一方面，透過省略來隱私，目的是減少 On-Chain 資訊，如 Lightning Network 所見，可以同時改善隱私和擴充性。每種方法都有其優點和缺點，因此必須採用細微的方法來提升隱私。

### 共識的改變與挑戰

由於網路的分散性，改變 Bitcoin 的共識機制是一項罕見且具挑戰性的工作。ChISA (交叉輸入簽章聚合) 和契約等提案旨在引入更複雜的交易規則，但其實施充滿困難。共識變更需要社群內廣泛的同意，如果建議的變更不被接受，所需的協調工作可能會導致嚴重的挫折感和倦怠感。這突顯了在制定協定時需要小心謹慎、通力合作。

### Bitcoin 開發的創新與標準

在 Bitcoin Wallet 開發過程中遵循標準化實踐對於確保易用性和安全性至關重要。目前許多錢包並不遵循既定標準，導致分散和潛在漏洞。標準化可以顯著改善用戶體驗和 Bitcoin 交易的整體安全性。

傳統的 12 個字元備份短語雖然對基本的 Bitcoin 使用有效，但在容納 Lightning Network 等 off-chain 通訊協定方面卻有不足。未來的備份標準需要不斷演進，才能為這些進階功能提供更好的安全性與可用性，確保使用者能在 Bitcoin 生態系統的不同層級安全地管理資產。

透過統一的通訊協定來簡化付款流程，對於提升使用者體驗是非常重要的。BIP70、BIP78 和 Payneem 等現有通訊協定提供了各種解決方案，但仍有進一步創新的空間。更精簡、更易於使用的支付通訊協定可以促進更廣泛的採用和易用性。

開發更好的工具和硬體對於改善 Bitcoin 的可用性和安全性至關重要。硬體錢包（例如 Ledger 和 Trezor）等創新產品提供了強大的安全解決方案，但必須持續發展以因應 Address 新興的威脅。改良後的工具可讓更多人更容易使用 Bitcoin，並提高其安全性。

降低與 Hardware Wallet 發行相關的風險並確保其完整性至關重要。Supply 連鎖攻擊對這些裝置的安全性構成重大威脅。實施嚴格的安全措施並確保生產和分銷過程的透明度，有助於降低這些風險。

簡化使用者與 Bitcoin 和 Lightning Network 的互動，同時維持安全性和效率，是我們的主要目標。更好的使用者經驗抽象可以讓 Bitcoin 更容易被非技術使用者使用，在不影響安全性的情況下，促進更廣泛的採用。

製作教育材料以改善 Bitcoin 的可用性、安全性和隱私權是很有影響力的。教育使用者有關 Bitcoin 的最佳實作與基本原則，可以讓他們做出明智的決定，並提升他們使用網路的整體體驗。

![Image](assets/en/1/3.webp)

**Layer 1 和 Layer 2 變更**

基礎 Layer (Layer 1) 的創新具有挑戰性，但對於 Bitcoin 的長期演進卻至關重要。Layer 2 解決方案（如 Lightning Network）允許更多的實驗性變更，並能更靈活地 Address 可擴展性和隱私權問題。這兩層在 Bitcoin 的持續發展中都扮演著關鍵的角色。

**共識協調**

Bitcoin 協定的變更需要大量的協調與社群共識。Bitcoin 的分散性使得這個過程本身就具有挑戰性。有效的協調和明確的溝通對於處理複雜的通訊協定變更和確保改進的成功採用至關重要。

**可擴充性挑戰**

達成全球共識和管理複雜的次級層 (例如 Lightning Network)，對可擴展性提出了挑戰。這些問題必須加以解決，以確保 Bitcoin 能容納不斷增加的交易量，同時維持其安全性與分散性的核心原則。

總而言之，持續解決這些開放性問題以及在 Bitcoin 生態系統中進行創新，對於其演進至關重要。要在可用性、安全性、隱私性和可擴充性之間取得平衡，必須謹慎考量並共同努力。透過對這些發展的貢獻，參與者可協助塑造 Bitcoin 的未來及其在全球金融版圖中的角色。

# Bitcoin 基礎

<partId>6c0a3691-3ce4-5309-8ad7-e16e4b63c734</partId>

## Bitcoin 的安全思維

<chapterId>0b97af0c-015a-54e3-a7f0-0f62ceb96c07</chapterId>

<professorId>7dfc5865-a0f6-4c3b-9b05-83e0d807ac59</professorId>

:::video id=08101af2-1ded-4f3a-b1db-d4477c6ab63e:::

歡迎來到今天的**安全性與可靠性**講座。我們的目標是探討系統設計與實際應用這兩個基本面向之間的微妙關係。

### 安全思維簡介

安全思維以保護系統免受蓄意攻擊的原則為基礎。它涉及到辨識潛在的威脅，並採取措施來降低威脅。相較之下，可靠性則著重於確保系統在指定條件下正常運作，並考慮可能發生的故障，而非蓄意破壞安全性的企圖。

#### 安全性與可靠性的關係

雖然安全性與可靠性的目標都是維護系統的完整性，但兩者的方法卻有很大的不同。可靠度工程處理的是隨機事件造成系統故障的可能性，通常會運用統計方法來預測並降低這些故障。另一方面，安全性必須考慮到攻擊的蓄意與智慧性，因此需要稱為「深度防禦」的多層防禦策略。

#### 安全性與可靠性

可靠性工程的一個典型例子可以追溯到 18 世紀的橋梁建造。所使用鋼材的品質，包括其成分和製造過程，對橋樑的可靠性有著關鍵性的影響。工程師必須考慮單點故障，並使用概率和統計來評估和確保橋樑的長期可靠性。

![Image](assets/en/2/1.webp)

與可靠度不同，安全性處理的是有意的威脅。舉例來說，256 位元的密碼金鑰提供了數學上的安全性保證，這是因為暴力破壞金鑰是不可行的。安全措施必須考慮不同的威脅模式，從實體篡改到複雜的網路攻擊。

### 實際應用

考慮使用紙質錢包建立和儲存 Bitcoin 金鑰的流程。雖然紙質錢包是安全的，但它們很容易受到實體損壞和竄改。要確保此類錢包的完整性，需要防偽方法和強大的驗證協議。

在另一種情況下，想像一下在機場接機時，司機會使用密碼來驗證乘客的身份。這種簡單卻有效的安全措施可以防止冒名者欺騙雙方。

在危地馬拉，為選舉結果加上時間戳記，對於確保選舉程序的完整性發揮了關鍵作用。透過使用加密方法對 Timestamp 資料進行加密，選舉官員可以提供竄改過的證據，證明選舉結果的真實性，從而阻嚇受到重大經濟誘因驅使的潛在操縱者。

![Image](assets/en/2/2.webp)

### 識別和緩解潛在威脅

威脅建模是識別潛在安全威脅並建立減緩威脅策略的過程。這包括了解系統環境、識別可能的攻擊者，以及根據假設和機率分析開發安全通訊協定。

#### 建立安全通訊協定

例如，為了保障選舉，可以實施公正的監督或跨黨派監測，以確保透明度和完整性。時間戳記和交叉驗證等加密方法有助於維持資料的真實性和防止篡改。

#### 信任驗證

信任驗證可以用 PGP (Pretty Good Privacy) 驗證來說明。透過驗證 PGP 金鑰的指紋和簽章，使用者可以建立數位身分的真實性。類似的做法對於透過 Hash 比對（例如 SHA-256）來驗證軟體完整性也是非常重要的。

#### 建立信任途徑

建立信任並非一蹴可及；它需要連結多種信任途徑並確保冗餘。例如，使用 HTTPS 和 Blockchain 支援的憑證透明度可確保網路來源的真實性，讓攻擊者難以違反信任。

#### 安全獎勵

瞭解獎勵機制的作用對維護安全性至關重要。例如，Bitcoin 的安全模型依賴於礦工的獎勵和網路參與者的驗證，突顯了經濟獎勵在維護數位生態系統中的重要性。

#### 保護 Bitcoin 皮夾

Bitcoin 錢包的安全策略包括多重簽章設定和多樣化儲存。這些方法可確保即使其中一個元件受到攻擊，整體安全性仍然完好無損。

#### 驗證的重要性

最後，使用者驗證是維護安全網路的關鍵。每位使用者在驗證交易及驗證軟硬體元件時所扮演的角色，都有助於維護網路的完整性，並挫败潛在的威脅。

總而言之，理解並整合安全性與可靠性原則對於設計穩健的系統至關重要。透過從歷史範例中學習、應用現實世界的策略，以及持續驗證信任度，我們可以建立既安全又可靠的系統。

## Bitcoin 中的自由與開放源碼軟體 (FLOSS)

<chapterId>2c59d609-f1ef-53f4-9575-df62e4d066e9</chapterId>

<professorId>7dfc5865-a0f6-4c3b-9b05-83e0d807ac59</professorId>

:::video id=4544ef7a-685e-4aaf-98a0-8a10dce06172:::

自由與開放原始碼軟體 (FLOSS) 的使用在 Bitcoin 的生態系統中至關重要。Peter Todd 探討了 FLOSS 對 Bitcoin 的重要性，探索了 FLOSS 的歷史，並檢視了 Github 如何讓我們協同建立像 Bitcoin 這樣的開放原始碼軟體。

### 軟體的性質與重要性

軟體的核心是程式碼與資料的集合，用以指示電腦裝置如何執行特定任務。硬體需要實體材料與製造過程才能複製，而軟體則不同，它可以輕易複製與散佈，幾乎不需成本。這個根本性的差異在軟體的擴散與發展上扮演了關鍵的角色。

軟體與硬體的主要區別之一是開放原始碼的概念。雖然開放原始碼硬體已經存在，但由於複製實體物件的複雜性，開放原始碼硬體並不普遍。相反地，開放原始碼軟體因為容易複製與散佈而蓬勃發展。開放原始碼軟體允許任何人檢視、修改和散佈程式碼，促進加速創新和問題解決的合作環境。

軟體的法律架構主要圍繞著作權法。這些法律賦予軟體創造者使用、修改及散佈其作品的專屬權利。然而，開放原始碼授權條款提供了一個在特定條件下與大眾分享這些權利的機制。這個法律結構對於了解軟體散佈與修改的動態是非常重要的。

總而言之，軟體作為容易複製的代碼與資料，加上開放原始碼授權所提供的法律機制，突顯出軟體在現代數位環境中的重要性。此架構不僅能推動創新，還能確保軟體能被全球社群自由分享與改進。

### 自由軟體運動的歷史

自由軟體運動起源於 1980 年代早期，主要由 Richard Stallman 的軟體自由願景所推動。Stallman 對於專屬軟體的限制性感到沮喪，於是開始創造使用者可以自由使用、修改與分享的軟體。這促使自由軟體基金會 (FSF) 於 1985 年成立。

Stallman 的重大貢獻之一是發展 GNU 計劃，旨在創造一個類似 Unix 的自由作業系統。GNU 是「GNU's Not Unix」的縮寫，提供了完全自由作業系統的許多重要元件。然而，它缺乏核心，即作業系統的核心部分。

Linus Torvalds 在 1991 年創造了 Linux 核心，填補了這個缺口。Torvalds 的核心與 GNU 元件結合，產生了功能完整的自由作業系統 GNU/Linux。Stallman 的 Commitment 軟體自由哲學與 Torvalds 的實際貢獻之間的合作，充分展現了開放原始碼方法的力量。

![Image](assets/en/2/3.webp)

自由軟體運動對軟體產業有著深遠的影響，它提倡的理念是軟體應該免費供所有人使用、修改和分享。它的原則奠定了許多開放原始碼專案與社群今日蓬勃發展的基礎。

### 開放原始碼的經濟與資金

開放原始碼專案的資金來源與持續發展是獨特的挑戰與機會。開放原始碼專案與專屬軟體不同，專屬軟體透過銷售與授權費用產生收入，而開放原始碼專案則通常仰賴其他的資金模式。

Bitcoin Core 就是一個成功的例子，它是 Bitcoin 基礎架構的重要部分。Bitcoin Core 的開發人員通常透過補助金、捐款，以及從專案成功中獲益的組織贊助獲得經費。這種模式可讓開發人員專注於軟體的改進，而不受傳統商業資金的限制。

![Image](assets/en/2/4.webp)

另一個突出的例子是 Linux 作業系統。許多公司，例如 IBM、Red Hat 和 Intel，都對 Linux 的發展有所貢獻，因為他們的產品和服務都有賴於一個強大且安全的作業系統。這些公司提供財務支援、貢獻程式碼，並提供資源以維護和強化 Linux 生態系統。

開放原始碼授權證，例如 MIT、GPL 和 AGPL，在開放原始碼軟體的經濟動態中也扮演著重要的角色。MIT 之類的許可證允許更靈活地使用程式碼，包括商業化。相反地，像 GPL 之類的 copyleft 授權則確保任何衍生作品也必須是開放原始碼，以促進合作環境。

![Image](assets/en/2/5.webp)

總而言之，開放原始碼軟體的經濟是由社群貢獻、企業贊助以及創新的資金模式所驅動。這些機制確保了開放原始碼專案的永續性與持續改善，讓開發者與使用者都能受惠。

## Bitcoin 中的加密技術

<chapterId>71867dd2-912c-55ad-b59c-9dbca8a39469</chapterId>

<professorId>6cfd206c-53b8-47a0-bbf4-44fd84e6ee1d</professorId>

:::video id=b482b0f0-4468-4eaf-bcd6-eb4748bdfa3a:::

歡迎！今天，我們將深入探討每個 Bitcoin 開發人員都應該知道的密碼學的重要方面。我們將著重於基礎概念和實際應用，而不會用過多的理論細節來壓倒您。我們的主要目標是讓您掌握在 Bitcoin 中有效理解、實作和疑難排解加密機制的知識。

### Bitcoin 開發人員的核心密碼概念

在本節中，我們將深入探討 Bitcoin 開發人員必備的主要加密概念，包括 Hash 函數、Merkle 樹、數位簽章和橢圓曲線。

![Image](assets/en/2/6.webp)

**Hash 函式**：Hash 函數接受輸入並產生固定長度的位元組字串。在 Bitcoin 中，Hash 函數是資料完整性和安全性的基礎。加密 Hash 函數必須有效率、generate 看起來是隨機輸出，並產生固定長度的輸出，不論輸入大小。它們用於檔案完整性檢查，確保資料未被惡意篡改。

![Image](assets/en/2/7.webp)

**安全屬性**：加密 Hash 函式必須遵守幾項安全特性。預映像抵抗確保從 Hash 輸出逆向工程原始輸入是不可行的。其次，預映像抵抗意味著很難找到不同的輸入來產生相同的 Hash 輸出。碰撞阻抗可確保找不到兩個不同的輸入會產生相同的 Hash 輸出。

**Merkle Trees**：Merkle Tree 是一種資料結構，能夠有效且安全地驗證大型資料集。資料項成對散列，所得的散列結果反覆組合，形成單一根 Hash。在 Bitcoin 中，Merkle 樹在區塊創建和交易驗證中至關重要，特別是對於簡化支付驗證 (SPV) 客戶端和 Taproot (Mast) 中。

![Image](assets/en/2/8.webp)

**數位簽章 (ECDSA)**：橢圓曲線數位簽章演算法 (ECDSA) 用於確保 Bitcoin 交易的真實性和完整性。它涉及使用私人密碼匙產生簽章，並可使用對應的公開密碼匙進行驗證。主要概念包括瞭解有限域、離散對數和非ces 的重要性。

**Elliptic Curves**：橢圓曲線因其效率和安全性而被用於公開密碼匙加密。橢圓曲線加密法的安全性取決於離散對數問題的難解程度。

![Image](assets/en/2/9.webp)

### Bitcoin 中的實用密碼應用與安全實務

在本節中，我們將探討這些概念在實際 Bitcoin 開發中的應用，以及應遵循的最佳安全實務。

** 加密 = 危險**：加密技術是一把雙刃劍。雖然它可以防止意外的資料損害和惡意行為，但不正確的實作卻可能導致嚴重的漏洞。開發人員必須深入瞭解加密機制，以確保安全實作和排除潛在問題的能力。舉例來說，SHA-2 的 256 位元輸出可確保前影像攻擊大約需要 2^256 次工作，而防碰撞大約需要 2^128 次工作。

![Image](assets/en/2/10.webp)

**Merkle Tree 應用**：瞭解對數證明大小並確保小心設計樹對於避免缺陷是非常重要的，例如交易驗證中的 Hash 重複。Merkle 樹用於區塊建立、交易驗證，以及 Taproot 等增強功能。

**Public Key Cryptography**：離散對數法和有限字段是 Bitcoin 密碼計算的基礎。挑戰回應通訊協定用來驗證私人密碼匙的知識，而不會洩露密碼匙。

![Image](assets/en/2/11.webp)

**安全影響**：歷史案例顯示 Nonce 重複使用造成重大財務損失。了解產生獨特非ces 的重要性至關重要。使用類似 LibSecP256k1 的可信賴程式庫，可確保穩健且安全的加密作業。

**Elliptic Curve Cryptography (ECC)**：簽章方案已從身份通訊協定演進到目前用於 Bitcoin (BIP 340) 的 Schnorr 簽章等方案。橢圓曲線和有限域演算法的知識可確保安全的加密實作。

**給開發人員的一般建議**：加密協定必須經過徹底的同業審查。開發人員必須精確並充分瞭解加密程序的每個步驟。意識到加密實作中常見的陷阱可以避免重大的漏洞。

**加密學中的橢圓曲線**：金鑰調整和安全性是重要的課題，例如在確保安全性的同時，使用額外的私人金鑰來修改公開金鑰。Bitcoin 的特定橢圓曲線 SECP256K1 及其參數 (P 和 N) 是其實作的基礎。

#### 總結

在這個講座中，我們已經探討了基本的加密概念，這些概念是 Bitcoin 的安全性和功能性的基礎。從 Hash 函數、Merkle 樹和數位簽章的關鍵作用，到橢圓曲線加密學的複雜數學，這些 Elements 形成 Bitcoin 分散式網路的骨幹。了解這些概念不僅僅是掌握理論，更重要的是認識到實際世界開發中的實際影響和潛在陷阱。

身為 Bitcoin 開發人員，必須謹慎且精確地進行加密實作。Bitcoin 網路的安全性在很大程度上取決於這些加密原則的正確和安全應用。無論您是驗證交易、設計新功能，或是確保 Blockchain 的完整性，對加密學的深入瞭解都能讓您在 Bitcoin 生態系統中建立更穩健、安全且創新的解決方案。

只要掌握這些概念並遵守最佳實務，您就能為 Bitcoin 的持續發展做出有效貢獻，確保其未來的彈性與安全性。

## Bitcoin 的治理模式

<chapterId>a30ec3e7-b290-5145-a9a9-042224ab20d2</chapterId>

<professorId>7dfc5865-a0f6-4c3b-9b05-83e0d807ac59</professorId>

:::video id=91a38c17-5801-4a5c-baf2-c9e4cc24fd84:::

### Bitcoin 的性質

Bitcoin 是一種數位貨幣，以共識通訊協定運作，這是一套由網路參與者同意的規則，以確保統一性和功能性。Bitcoin 的核心是被稱為 Blockchain 的分散式 Ledger，交易由網路節點記錄和驗證。完整節點儲存 Bitcoin Blockchain 的全部歷史，在維護此 Ledger 的完整性上扮演著重要的角色。其他類型的節點，例如存檔節點、修剪節點和 SPV（簡化支付驗證）節點，也以各種方式對網路做出貢獻。共識協定可確保所有這些節點都同意 Blockchain 的狀態，使 Bitcoin 穩健地抵擋審查和欺詐。

#### 預防變更

Bitcoin 的管理對於防止任意或惡意變更通訊協定至關重要。這是透過共識機制達成的，需要社群間的廣泛同意。具備程式設計知識的開發人員在提出變更時扮演重要角色，但這些變更必須獲得更廣泛的社群接受才能執行。

Bitcoin 核心與替代實作都有監督軟體開發與維護的維護人員。這些維護人員負責合併程式碼變更，確保這些變更符合共識規則，並且不會引入弱點。

#### Soft 前叉 vs Hard 前叉

Soft 分叉是收緊 Bitcoin 通訊協定現有規則的變更，使某些先前有效的交易失效。它們是向後相容的，這表示未升級的節點仍能識別新規則。Soft Fork 的一個例子是 2010 年對溢出錯誤的修復，它防止了憑空創造金錢。

Hard 分叉是鬆動現有規則的變更，允許新類型的交易。這些並非向後相容，意即未升級的節點無法辨識新規則。Hard Fork 的範例可能需要用來解決 2106 年的問題，以確保 Bitcoin 在此日期之後仍能繼續運作。

![Image](assets/en/2/12.webp)

![Image](assets/en/2/13.webp)

### 治理範例

幾個真實案例說明了 Bitcoin 在行動上的治理。2010 年的溢出錯誤修復是一個 Soft Fork 來解決關鍵缺陷。2106 年的問題可能需要 Hard Fork 來 Address 其影響。從最長工作鏈到最多工作鏈的過渡反映了一個影響如何達成共識的重大治理決策。

Bitcoin 的治理也針對協定使用上的實際變化。例如，引入序號和銘文說明了協定變更如何無法審查交易。同樣地，Full RBF (Replace-by-fee) 的實施改變了交易替換程序，卻沒有改變共識規則。

#### 改變與共識的動機

Bitcoin 的變更可能受到各種動機的驅使，例如修復關鍵錯誤、引進新功能，或因經濟或政治原因而限制變更。這些動機通常會在社群內引起爭論，討論何謂錯誤與功能，以及對網路的整體影響。

Bitcoin 的共識機制使其具有固有的政治性，需要廣泛的同意才能接受變更。這種政治性對於維持網路的分散性以及確保任何修改都符合社群的最佳利益至關重要。

運行中的節點可以驗證 Bitcoin 規則並參與網路，即使使用不同的通訊協定，例如 Blockstream Satellite。這強調了 Bitcoin 的共識機制與網路使用的資料通訊方式之間的分離。節點的經濟意義，尤其是那些由大型實體（如 Binance）經營的節點，會影響變更的採用。這些實體在網路中擁有大量的經濟利益，可以透過營運有影響力的節點來左右決策。

### 區塊大小之爭

區塊大小的爭議是一個重要的治理問題，圍繞著是否增加 Bitcoin 的區塊大小。這個爭議隨著 SegWit 的實施而解決，Soft Fork 增加了有效區塊大小，並啟用了 Lightning Network。

![Image](assets/en/2/14.webp)

### 強制變更與多數規則

曾有人試圖透過法律迫使 Bitcoin 開發者為了個人利益而改變 Blockchain 規則，例如 Craig Wright 提出的訴訟。這些嘗試突顯了 Bitcoin 治理所涉及的挑戰和道德考量。

在 Bitcoin 中，多數規則扮演著重要的角色。如果 60% 的礦工採用新規則，他們的區塊就會被運行原始 Bitcoin 核心的礦工拒絕，導致分裂。因缺乏社區支持而失敗的 Hard Fork 的例子是 Bitcoin Satoshi 的願景 (BSV)。

讓我們簡單回顧一些重要的概念。

**Forced Soft Fork**：執行限制性規則來變更 Bitcoin 的概念可能會導致更多分裂和管理問題。此方法說明 Bitcoin 社群內的複雜性和潛在衝突。

**51% 攻擊**：51% 攻擊描述了一種情況，大多數雜湊能力可以透過 Mining 空區塊攻擊 Bitcoin。除非社群針對 Address 的攻擊採用新的共識規則，否則這可能會有效扼殺網路。

**Check-Lock-Time-Verify (CLTV)**：Check-Lock-Time-Verify (CLTV) 是以 Soft Fork 實施治理變更的範例。CLTV 可確保交易僅在特定時間之後有效，這對付款通道和備份金鑰非常有用。這項變更使用之前什麼都不做的 opcode 收緊了規則。

總而言之，Bitcoin 的未來與變更是由使用者的集體意志所決定。重大的變更需要廣泛的共識，這反映了 Bitcoin 治理的分散性和政治性。

# Layer 一個概念

<partId>5300855f-e5e4-5bca-9afe-2397f7c76260</partId>

## Bitcoin 中的節點元件

<chapterId>75ea1d88-ee6f-5f98-af90-e4758c55e606</chapterId>

<professorId>6cfd206c-53b8-47a0-bbf4-44fd84e6ee1d</professorId>

:::video id=6fae79f6-da81-4870-927b-923bd1672176:::

Adam Gibson 分解了 Bitcoin 節點的各種元件。本章的重點在於每個元件在維護網路功能和完整性上所扮演的角色。他特別著重於我們為什麼要執行 Bitcoin 節點、Bitcoin 節點要做什麼，以及 Bitcoin 節點的不同元件如何運作。

### Bitcoin 節點簡介

瞭解 Bitcoin 節點的角色對任何參與 Bitcoin 網路的人來說都是至關重要的。運行 Bitcoin 節點可讓使用者驗證交易、參與共識，並維持對其隱私的控制。本講座將探討為何執行 Bitcoin 節點是有益的，以及它如何對 Bitcoin 網路的整體安全性和分散性做出貢獻。

### 為什麼要執行 Bitcoin 節點？

基於幾個原因，執行 Bitcoin 節點是必要的：

1. **驗證**：透過執行節點，您可以自行驗證交易，確保您收到的 Bitcoin 是有效的，而無需依賴第三方。

2. ** 參與共識**：節點在決定 Bitcoin 網路的規則上扮演重要角色，因此參與共識有助於維護 Blockchain 的完整性與安全性。

3. **隱私和控制**：運行您自己的節點，可確保您不必依賴外部節點，因為外部節點可能會追蹤您的交易和 Wallet 結餘，從而危及您的隱私。

### Bitcoin 節點有什麼功能？


- 保留對等**清單：節點必須找到網路中的其他節點並連線，才能獲得 Exchange 資訊。
- 接收並傳送有效的交易和區塊**：Bitcoin 節點負責在網路上傳播有效的交易和區塊。
- 保存區塊和最重鏈的歷史**：節點儲存自己的 Blockchain 副本，可讓他們驗證交易和區塊的真實性。
- 保留有效候選清單；Mempool**：節點必須在 Mempool 中保留可能的交易候選人清單，以納入區塊中。

![nodes network](assets/en/3/18.webp)

**NOTE**：Mempool 是已驗證但尚未包含在區塊中的交易的暫存區。

### 節點元件

#### Bitcoin 核心模組

![Bitcoin core modules](assets/en/3/19.webp)


- 對等發現**：對等發現是節點找到其他節點進行連線的過程。
- 驗證引擎**：驗證引擎負責根據網路規則檢查交易和區塊的有效性。
- RPC (遠端程序呼叫)**：Bitcoin 核心包含一個 RPC Interface，允許外部應用程式 (例如錢包) 與節點互動。
- 儲存區塊與 Chain 狀態**：Bitcoin Core 可以儲存整個 Blockchain，也可以不儲存整個 Blockchain，無論是存檔或修剪的節點。它也會在磁碟上儲存網路的目前狀態 (The UTXO set)。

#### 我們可以移除什麼？


- Miner**：由於需要較高的計算能力，大多數 Bitcoin 節點不參與 Mining。
- RPC (伺服器)**：Bitcoin Core 實作 JSON-RPC Interface，可使用命令列輔助程式 bitcoin-cli 存取。
- Wallet (disablewallet)**：如果您偏好使用外部 Wallet，可以停用 Bitcoin Core 中的 Wallet 功能。這可讓您單獨管理私人金鑰。
- Mempool (blocksonly)**：對於希望將頻寬使用量降至最低的使用者，執行「blocksonly」節點是一個解決方案，節點只處理區塊，忽略交易。

### 連鎖國家

#### 硬幣在哪裡？

硬幣並不是儲存在位址中；而是儲存在 UTXOs 中，代表所有尚未花費的交易輸出。您可以使用指令檢索這些資訊：

```Bash
bitcoin-cli gettxoutsetinfo
```

![utxoset info command](assets/en/3/20.webp)

我們可以稽核 Bitcoins 的數量是否正確。

#### 對於每個 UTXO，chainstate 都有：


- txid.
- 輸出索引。
- UTXO 在哪個區塊。
- 無論是 Coinbase UTXO.

**重要**：交易與 UTXO 不同。

![Txs and UTXOs](assets/en/3/21.webp)

#### Mempool

這是每個節點中未確認交易的清單，稱為候選交易。儲存在 RAM 中，以便快速存取，而且它不是共識的一部分。

#### Bitcoin 節點的安全考量

執行 Bitcoin 節點時，安全性是最重要的。以下是一些需要注意的重要事項：

#### 避免集中化

依賴單一來源取得 Blockchain 資料，例如從中央伺服器下載所有區塊，會造成重大風險。為了維持 Bitcoin 的分散性質，節點應連結至多個對等體，並驗證所接收的資料。

#### 防止隔離攻擊

隔離攻擊發生於節點被誘騙連線至有限的對等集，讓攻擊者提供錯誤的資料。透過連線到不同的對等集，並驗證收到的資料，節點可以保護自己免受這些攻擊。

#### 管理同儕連線

節點必須仔細管理其對等連線，以確保不會連線到惡意行為者。這包括維護顯示可疑行為的被禁止對等體清單，並定期更新對等體清單，以避免依賴一小群節點。

#### UTXO 套裝的重要性

UTXO 集代表 Bitcoin 的當前狀態，列出所有未使用的交易輸出。它對於驗證交易和確保硬幣不會被花費超過一次非常重要。保持這個集數小且容易存取，對維持網路的效率非常重要。

#### 總結

運行 Bitcoin 節點是參與 Bitcoin 網路的強大方式，提供您驗證交易、維護隱私的能力，並有助於 Blockchain 的安全性和分散性。無論您選擇執行 Full node 或透過修剪 Blockchain 或停用某些元件來自訂您的設定，瞭解 Bitcoin 節點的核心功能和安全考量，將使您有能力做出明智的決定，並為 Bitcoin 的持續演進做出貢獻。

## Bitcoin 的資料結構

<chapterId>5ed314b1-8293-567d-bf03-730e8c9c774b</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

:::video id=1790e5fb-33f5-4e0e-982e-41589cd02965:::

本講座的主要目的是引導您通過在 Rust 中編寫解析器來解析 Bitcoin 區塊。這包括了解 Bitcoin 區塊和交易的結構，並實作必要的邏輯來擷取和詮釋這些資料。

### 在 Rust 中解析 Bitcoin 區塊和交易

#### 要解析的元件

若要解析 Bitcoin 區塊，您需要專注於下列元件：

1. ** 區塊標題**

2. ** 區塊內交易**

3. **交易輸入和輸出**

#### 區塊標頭結構

區塊標頭是 Bitcoin 區塊的基石，包含下列欄位：


- 版本**：表示區塊的版本。
- 上一區塊**：參考 Blockchain 中的前一個區塊。
- Merkle Root**：Hash 代表區塊中所有交易的合併 Hash。
- Timestamp**：區塊被挖出的時間。
- 位元**：有效區塊 Hash 的目標臨界值。
- Nonce**：礦工為使 Hash 低於目標臨界值而調整的值。
- 交易次數**：區塊中的交易次數。

**Note**：在 Mining 過程中，只有前 80 位元組 (包含區塊標頭) 會被散列。

![Block header structure](assets/en/3/1.webp)

#### 簡化

為了讓我們的範例易於管理：


- 我們將專注於解析 SegWit 之前（傳統）的區塊，避免增加 Segregated Witness 的複雜性。
- 我們將跳過 Bitcoin 腳本語言中的某些操作碼，專注於我們需要解析完整區塊的幾個操作碼。

#### 交易架構

Bitcoin 區塊中的每個交易包含以下內容：


- 版本**：交易的版本。
- 輸入數量**：交易輸入的計數。
- 輸入**：輸入的清單。
  - 上一個輸出（outpoint）**：上一個輸出參考值。
    - Hash**：參考交易的 Hash。
    - 索引**：交易中特定輸出的索引，稱為「vout」。
  - 腳本長度**：簽章腳本的長度。
  - 簽名腳本**：用於確認交易授權的腳本。
  - Sequence**：由寄件者定義的交易版本。
- 輸出數量**：交易輸出的計數。
- 輸出**：包含 Value 和 ScriptPubKey。
  - 價值**：交易值。
  - PubKey 腳本長度**：PubKey script 的長度。
  - PubKey 腳本**：包含公開金鑰，作為要求輸出的設定。
- 鎖定時間**：表示此交易可包含在區塊中的區塊高度或 Timestamp。

![Transaction structure](assets/en/3/2.webp)

![TxIn structure](assets/en/3/3.webp)

![Outpoint structure](assets/en/3/4.webp)

![TxOut structure](assets/en/3/5.webp)

#### 解析技術

在 Rust 中，我們可以使用各種技術來解析這些結構：


- 利用 `from_le_bytes` 讀取 Little Endian 資料。
- 實作自訂的 `parse` trait 來處理不同結構的解析邏輯。

```Rust
trait Parse: Sized {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error>;
}
```


- 針對清單和特定類型 (例如 `VarInt`、`U32`、`U64` 等) 實作一般解析。

```Rust
impl Parse for i32 {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let val = i32::from_le_bytes(bytes[0..4].try_into()?);
Ok((val, &bytes[4..]))
}
}
```

### 除錯與測試

為了確保我們的解析器能正常運作：


- 將解析的資料與已知區塊詳細資料 (例如來自 Mempool.space)進行比較。
- 驗證解析的交易計數和區塊詳細資料是否符合預期值。

### 處理特殊情況和腳本解析

#### 執行「解析」功能

我們將實作 `parse` 函式來處理完整的區塊，包括區塊標頭和交易。這包括讀取區塊資料並擷取相關欄位。

```Rust
impl Parse for Block {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let (header, bytes) = Parse::parse(bytes)?;
let (transactions, bytes) = Parse::parse(bytes)?;
let block = Block {
header, transactions
};
Ok((block, bytes))
}
}
```

#### 區塊標頭修改

我們需要調整解析邏輯，將交易計數從區塊標頭結構中移除，將其視為獨立的實體。

```Rust
impl Parse for BlockHeader {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let (version, bytes) = Parse::parse(bytes)?;
let (prev_block, bytes) = Parse::parse(bytes)?;
let (merkle_root, bytes) = Parse::parse(bytes)?;
let (timestamp, bytes) = Parse::parse(bytes)?;
let (bits, bytes) = Parse::parse(bytes)?;
let (nonce, bytes) = Parse::parse(bytes)?;
let header = BlockHeader {
version, prev_block, merkle_root, timestamp, bits, nonce,
};
Ok((header, bytes))
}
}
```

#### 結構定義

定義一個新的結構`Block`，它包含區塊標頭和交易清單。

```Rust
struct Block {
header: BlockHeader,
transactions: Vec<Transaction>,
}
```

#### Rust 語法 Elements

引入 Rust 語法 Elements，例如問號 (`?`)，用於錯誤處理。這將簡化我們的程式碼，使其更具可讀性。

#### 認證

新增 assertions 以驗證在處理完整區塊後，沒有遺留未解析的位元組。這可確保解析程序的完整性。

#### Coinbase 交易等特殊情況

Coinbase 交易是用於認領 Block reward 的區塊中的第一筆交易，具有獨特的特性。我們需要適當處理這些特殊情況。

```Rust
struct OutPoint {
txid: [u8; 32],
vout: u32,
}
impl OutPoint {
fn is_coinbase(&self) -> bool {
self.txid == [0; 32] && self.vout == 0xFFFFFFFF
}
}
```

#### 腳本解析策略

為了解析事務中的腳本，我們將著重於常見的操作碼，例如 `OP_CHECKSIG`、`OP_HASH160` 和 `OP_PUSH`。解析這些腳本對驗證交易和處理錯誤至關重要。

```Rust
enum OpCode {
False,
Return,
Dup,
Equal,
CheckSig,
Hash160,
EqualVerify,
Push(Vec<u8>),
}
impl Parse for OpCode {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
match bytes[0] {
v @ 1..=75 => {
let data = bytes[1..(v as usize + 1)].iter().cloned().collect();
Ok((OpCode::Push(data), &bytes[(v as usize + 1)..]))
},
76 => {
let len = bytes[1] as usize;
let data = bytes[2..(len + 2)].iter().cloned().collect();
Ok((OpCode::Push(data), &bytes[(len + 2)..]))
},
0 => Ok((OpCode::False, &bytes[1..])),
106 => Ok((OpCode::Return, &bytes[1..])),
118 => Ok((OpCode::Dup, &bytes[1..])),
135 => Ok((OpCode::Equal, &bytes[1..])),
136 => Ok((OpCode::EqualVerify, &bytes[1..])),
169 => Ok((OpCode::Hash160, &bytes[1..])),
172 => Ok((OpCode::CheckSig, &bytes[1..])),
_ => todo!()
}
}
}
```

![op_checksig](assets/en/3/6.webp)

![op_hash160](assets/en/3/7.webp)

![op_push](assets/en/3/8.webp)

#### 腳本解析的挑戰

腳本解析可能會帶來挑戰，尤其是 coinbase 交易。重要的是要考慮到邊緣情況並正確處理，以確保準確的解析。

```Rust
impl Parse for Script {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let (len, bytes) = VarInt::parse(bytes)?;
let mut script_bytes = &bytes[..len.0 as usize];
let mut opcodes = Vec::new();
while !script_bytes.is_empty() {
let (opcode, bytes) = OpCode::parse(script_bytes)?;
script_bytes = bytes;
opcodes.push(opcode);
}
Ok((Script(opcodes), &bytes[len.0 as usize..]))
}
}
```

#### 緊湊型磚塊

目前使用精簡區塊是為了提高節點間資料傳輸的效率。這可減少頻寬使用量，並透過傳送 Mempool 中遺漏的交易，以節點在區塊中已有的交易來填補，然後再進行驗證，從而加快同步速度。

#### 現有圖書館的使用

對於共識關鍵應用程式，建議使用現有的函式庫，以避免 bug 並確保安全性，例如 [Rust-Bitcoin](https://docs.rs/Bitcoin/latest/Bitcoin/) 或 [Bitcoin-dev-kit](https://docs.rs/BDK/latest/BDK/)。實作您自己的解析器可能很有教育意義，但在生產環境中也有風險。

![libraries](assets/en/3/9.webp)

### Bitcoin Mining 的效率與安全性

#### Mining 的效率

Mining 空區塊對礦工來說可以更有效率：


- 礦工開始 Mining 空區塊以節省時間。
- 空區塊可以在前一個區塊確認後，快速開採，然後再切換到完整區塊。

#### Mining 空塊的原因

空區塊有時會因為時間問題而被挖出。礦工在開始 Mining 下一個區塊時，可能尚未收到完整的交易清單，因此他們會選擇挖一個空區塊。

![empty block](assets/en/3/10.webp)

#### 空區塊的惡意 Mining

雖然有可能出現惡意的 Mining 空區塊，但尚未觀察到。造成空區塊的主要原因是時序限制，而非惡意意圖。

#### 空塊的影響

出現空區塊是 Mining 程序的正常現象，主要是由於時序問題。雖然它們不包含交易，但仍會延展 Blockchain 並有助於網路安全。

#### 安全的重要性

Bitcoin Mining 的安全性是最重要的。透過遵守最佳實務和使用經過嚴格審核的函式庫，礦工和開發人員可以確保 Blockchain 的完整性，並防止潛在的漏洞。

總而言之，在 Rust 中解析 Bitcoin 區塊和交易涉及到理解複雜的結構和實施高效的解析技術。處理特殊情況和腳本解析需要仔細考慮，而專注於效率和安全性可確保 Bitcoin 網路的穩健性。

## Bitcoin 軟體概觀與節點實作

<chapterId>96d64781-fc27-5209-88d8-2acf00d05ea8</chapterId>

<professorId>0b05838c-24af-43ff-93be-896c907e0bc1</professorId>

:::video id=1d148008-9197-446f-afb5-628d4c3a5015:::

Daniela Brozzoni 全面概述了 Bitcoin Layer 1 軟體堆疊，解釋了構成 Bitcoin 通訊協定基礎的各個層次（即 Bitcoin 節點和 Bitcoin 錢包），以及如何透過介紹 Bitcoin 函式庫和深入瞭解 Bitcoin 開發套件 (BDK) 來建立 Bitcoin 軟體。

### Bitcoin 軟體概觀

Bitcoin 的軟體堆疊是其運作的基礎，由各種 Elements 組成，包括節點和錢包。這個生態系統的關鍵部分是 Bitcoin 開發套件 (BDK)，我們稍後會詳細探討。首先，讓我們集中討論節點在 Bitcoin 網路中的角色。

#### Bitcoin 節點

Bitcoin 節點是 Bitcoin 網路的骨幹。它們彼此連接，進行 Exchange 交易和區塊，並驗證傳入的資料。有不同類型的節點，每種節點都有其獨特的用途：


- 完整節點**：這些節點儲存整個 Blockchain，並驗證所有交易和區塊。這些節點提供高度的安全性，對於網路的分散性是不可或缺的。
  - 存檔節點**：存檔節點是完整節點的子集，保留所有 Blockchain 資料，對於歷史分析和除錯很有價值。

![archival node](assets/en/3/11.webp)


  - 修剪節點**：剪枝節點只保留 Blockchain 的一部分，剔除驗證時不再需要的舊資料，節省磁碟空間。

![pruned node](assets/en/3/12.webp)

#### Bitcoin 核心

Bitcoin Core 是使用最廣泛的 Full node 實作。它同時執行 Full node 和 Wallet 的雙重功能。Bitcoin Core 的主要功能包括


- 可用性**：可透過命令列 Interface (CLI) 和圖形使用者 Interface (GUI) 使用。
- 開放原始碼性質**：程式碼是開放原始碼，讓開發人員貢獻並審查其運作。
- 語言**：以 C++ 寫成，並使用 Python 測試，可確保穩健的效能與可靠性。

![cli-gui](assets/en/3/13.webp)

##### 探索 Bitcoin 核心

要獲得 Bitcoin Core 的實作經驗，可以使用 Git 來編譯和執行測試。這個過程包括


- 編譯程式碼以建立可執行版本。[Bitcoin github](https://github.com/Bitcoin/Bitcoin) 存取 doc/build-\*.md 以取得說明。

```Bash
./autogen.sh
./configure
make # use "-j N" for N parallel jobs
make install # optional
```


- 執行測試以確保一切運作正常。可在 [此處](https://github.com/Bitcoin/Bitcoin/blob/master/test/README.md) 找到說明

```Bash
make check
#individual tests can be run directly calling the test script e.g:
test/functional/feature_rbf.py
#run all possible tests
test/functional/test_runner.py
```


- 在 Python 中建立並執行測試，以驗證特定功能。檔案 [example.py](https://github.com/Bitcoin/Bitcoin/blob/master/test/functional/example_test.py)是一個使用 RPC 和 P2P 介面的測試案例的大量註解範例。

#### 替代節點實作

除了 Bitcoin Core 之外，還有幾種替代的節點實作：


- Bitcoin 結**：它提供比 Bitcoin 核心更先進的功能，佔用更多空間和記憶體。
- LibBitcoin**：靈活且模組化的實作。
- btcd**：以 Go 撰寫，提供不同的設計哲學。

實施這些替代方案有其本身的風險，尤其是在共識規則方面。偏離既定的驗證規則可能會導致分叉或不一致。Bitcoin 核心專案希望透過集中共識程式碼來降低這些風險，以確保各種實作的一致性。

![implementation](assets/en/3/14.webp)

### Bitcoin 皮夾與安全

Bitcoin 錢包對於安全管理您的 Bitcoin 持有量至關重要。它們有各種不同的形式，每種形式都有獨特的功能和安全考慮。

#### Bitcoin 皮夾的種類

1. **保管人與非保管人**：


   - 保管人錢包**：由第三方管理，提供便利，但需要信任保管人。
   - 非保管人錢包**：由使用者控制，提供更高的安全性與隱私權。

2. **Desktop vs. Mobile**：


   - 桌面錢包**：通常功能更豐富、更安全。
   - 行動錢包**：提供便利性與可攜性。

3. **On-Chain 對 Lightning**：


   - On-Chain 皮夾**：直接與 Bitcoin Blockchain 互動。
   - 閃電錢夾**：促進更快速、更便宜的交易 off-chain。

4. **Cold 皮夾 vs. Hot 皮夾**：


   - Cold 皮夾**：不連線至網際網路，提供絕佳的安全防護。
   - Hot 皮夾**：與網際網路連線，提供更多存取便利性，但安全性較低。

#### Cold Wallet 安全性

Cold 電子錢包因其安全性而備受推崇。由於保持離線狀態，它們在本質上可以抵禦線上黑客的攻擊。然而，確保透過 Cold 電子錢包進行的交易安全且準確，以防止不慎將 Bitcoin 傳送給惡意行為者，是非常重要的。

#### 腕錶專用錢包

僅可觀看的錢包僅包含公開金鑰，允許使用者接收 Bitcoin 並監控其餘額，但無法消費。此功能可為需要密切監控所持資金的人增加額外的 Layer 安全性。

#### Bitcoin Wallet 的基本功能

無論是哪一種類型，每一台 Bitcoin Wallet 都會執行三個基本功能：

1. **接收 Bitcoin**：generate 位址，並監視傳入的交易。

2. **Send Bitcoin**：建立並廣播交易到網路。

3. **顯示餘額**：顯示 Wallet 目前的餘額。

#### Bitcoin 皮夾的作用


- Bitcoin 電子錢包就像鑰匙鏈一樣，保存並生成加密鑰匙。

![keychain](assets/en/3/15.webp)


- 它們會監控 Blockchain 是否有交易傳入。

![monitor](assets/en/3/16.webp)


- 透過選擇未使用的交易輸出 (UTXO)、設定輸入和輸出，以及最佳化隱私和費用來建立交易。

![tx_builder](assets/en/3/17.webp)

#### Wallet 邏輯的重複使用性

鑑於所有 Bitcoin 錢包都有類似的功能，重複重寫 Wallet 邏輯的效率很低。這就是 Bitcoin 開發套件 (BDK) 發揮作用的地方。

### Bitcoin 開發套件 (BDK) 與技術概念

Bitcoin 開發套件 (BDK) 是專為簡化 Bitcoin 錢包的建立與管理而設計的函式庫。

#### BDK 概觀

BDK 透過提供建構在 Rust Bitcoin 之上的更高層級功能，簡化了 Wallet 的建立。它透過綁定支援多種程式語言，包括 Kotlin、Swift 和 Python。

#### 其他 Bitcoin 圖書館

無數的 Bitcoin 函式庫迎合不同的程式語言，例如 Python、JavaScript、Java、Go 和 C。

#### 關鍵技術概念

1. **描述符**：描述符描述如何從金鑰衍生出 Bitcoin 指令碼和位址，讓 Wallet 功能更靈活、更強大。

2. **PSBT（部分簽署的 Bitcoin 交易）**：PSBT 是一種需要多重簽章的交易格式，可促進協同交易並加強安全性。

3. **Rust 語法**：Rust 中的關鍵概念，例如用於 null 安全性的 `Option ` 以及用於錯誤處理的 `Result ` 類型，對於理解和有效使用 BDK 是不可或缺的。

#### 建立和管理交易

BDK 可簡化建立、簽署和廣播交易的流程：

1. **建立交易**：指定收件人、金額和費用。

2. **簽署交易**：使用 PSBT 收集簽名。

3. **Broadcast Transactions**：將完成的交易傳送至網路。

#### BDK 中的工作流程範例


- 設定 Wallet**：使用描述符初始化 Wallet。

```Rust
use bdk::{Wallet, SyncOptions};
use bdk::database::MemoryDatabase;
use bdk::blockchain::ElectrumBlockchain;
use bdk::electrum_client::Client;
use bdk::bitcoin;
fn main() -> Result<(), bdk::Error> {
let wallet = Wallet::new(
"tr(tprv8ZgxMBicQKsPf6WJ1Rr8Zmdsr6MaACS5K3tHw3QDQmFbkEsdnG3zAZzhjEgEtetL1jwZ5VAL85UaaFzUpAZPrS7aGkQ3GdM75xPu4sUxSiF/*)",
None,
bitcoin::Network::Testnet,
MemoryDatabase::default(),
)?;
Ok(())
}
```


- generate 位址**：建立新的位址，從 Testnet Faucet 接收 Bitcoin。

```Rust
//import AddressIndex outside the main function
use bdk::wallet::AddressIndex;
//Function to add isnide main function
let address = wallet.get_address(AddressIndex::New)?;
```


- 檢查餘額**：監控 Wallet 的餘額，首先連接到電子琴，同步 Wallet 並從 Wallet 取得餘額。

```Rust
//connect to Electrum server and save the blockchain
let client = Client::new("ssl://electrum.blockstream.info:60002")?;
let blockchain = ElectrumBlockchain::from(client);
//sync wallet to the blockchain received
wallet.sync(&blockchain, SyncOptions::default())?;
//get the balance from your wallet
let balance = wallet.get_balance()?;
println!("This is your wallet balance: {}", balance);
```


- 建立、簽署及廣播交易**：建立並完成交易，然後將其廣播至網路。

```Rust
//Add to the imports
use bdk::bitcoin::Address;
use bdk::{SignOptions};
use std::str::FromStr;
use bdk::blockchain::Blockchain;
//build a transaction psbt
let mut builder = wallet.build_tx();
let recipient_address = Address::from_str("tb1qlj64u6fqutr0xue85kl55fx0gt4m4urun25p7q").unwrap();
builder
.drain_wallet()
.drain_to(recipient_address.script_pubkey())
.fee_rate(FeeRate::from_sat_per_vb(2.0))
.enable_rbf();
let (mut psbt, tx_details) = builder.finish()?;
println!("This is our psbt: {}", psbt);
println!("These are the details of the tx: {:?}", tx_details);
//Sign the PSBT
let finalized = wallet.sign(&mut psbt, SignOptions::default())?;
println!("Is my PSBT Signed? {}", finalized);
println!("This is my PSBT finalized: {}", psbt);
let tx = psbt.extract_tx();
let tx_id = tx.txid();
println!("this is my Bitcoin tx: {}", bitcoin::consensus::encode::serialize_hex(&tx));
println!("this is mny tx id: {}", tx_id);
//Broadcast the transaction
blockchain.broadcast(&tx)?;
```

#### 列印 txid 和廣播交易

指定並列印 transaction ID (txid) 可在 Mempool.space 等平台上進行監控。廣播交易可以使用 `Blockchain.broadcast` 方法完成，驗證交易的詳細資訊和狀態是確保成功傳播的關鍵。

#### BDK 效用與隱私權注意事項

BDK 對於簡化 Bitcoin Wallet 開發而言非常寶貴。若要增強隱私性，建議使用 Electrum、Explora 等工具和個人 Bitcoin 核心節點。

#### 程式語言

開發 Bitcoin 專案時，由於 Rust 的安全性和效率，通常會是首選。但是，語言的選擇可能會根據具體的專案需求和開發人員的專業知識而有所不同。

#### BDK 相依性

BDK 依賴數個關鍵依賴項目，包括 Rust-Bitcoin 和 Rust-Miniscipt。資料庫管理和密碼學可能會使用其他函式庫。

透過瞭解這些元件，從 Bitcoin 節點和錢包到 Bitcoin 開發套件 (BDK)，您可以更有信心和能力地瀏覽 Bitcoin 生態系統。這些知識讓您有能力開發穩健且安全的 Bitcoin 應用程式，為這項革命性技術的持續演進做出貢獻。

# Lightning Network

<partId>d7ac2ad7-a4b3-564f-8a8d-cfec5297b3a5</partId>

## 付款管道的歷史

<chapterId>a0b11c6e-c0ff-5e65-b809-b2ab9a2fc37b</chapterId>

<professorId>880c7fa7-8d4c-4c9b-81b4-bc61ed256516</professorId>

:::video id=b90f19a3-a95e-4cd1-8c55-41016f3339cb:::

### 付款管道的歷史

歡迎來到我們關於 Blockchain 技術中的現代支付解決方案的講座。今天，我們將探討多跳鎖 (MHL) 和 Lightning Network 的歷史背景和主要發展。

#### 概述與歷史背景

多跳鎖 (MHL) 和 Lightning Network 是 Blockchain 技術中的先進概念，有助於整個網路進行高效且安全的微支付。從歷史角度來看，這些創新的需求來自於在 Blockchain 技術（尤其是 Bitcoin）最初部署時所觀察到的低效率和限制。隨著我們的深入探討，您將會了解以主題為基礎的結構和分層方法如何為 Blockchain 交易帶來革命性的改變。

### 主題式結構

MHL 和 Lightning Network 的推出標誌著從傳統、線性 Blockchain 交易到更複雜、多層系統的範式轉變。透過將交易分割為特定主題或區塊，這些創新技術可提供更具擴充性與安全性的支付基礎架構，解決早期 Blockchain 實作中的許多固有問題。

### Bitcoin 的問題

Bitcoin 是 Blockchain 技術的先驅，它引進了一種分散式系統，交易會在整個網路中廣播。雖然具有革命性，但這種方法本身效率不高。網路中的每個節點都必須驗證每筆交易，導致嚴重的延遲和瓶頸，尤其是在交易量大的時候。

Bitcoin 的分散式驗證程序需要大量的計算資源。每筆交易都必須由多個節點進行驗證和記錄，因此需要消耗大量的能源和處理能力。這不僅增加了營運成本，也對網路的頻寬造成壓力，導致交易費用增加和處理時間變慢。

雖然 Bitcoin 的分散性是其核心優勢之一，但也帶來了重大的挑戰。Blockchain 的公開性質意味著所有人都能看到所有的交易，這引起了隱私權的疑慮。此外，由於 Mining 的權力集中在少數大型實體手中，因此需要在眾多節點之間達成共識，這可能會導致集中化的壓力。

### 付款管道作為解決方案

![Gold coin](assets/en/4/1.webp)_Gold Standard Metaphor_

針對 Address 的低效率和 Bitcoin 的隱私權問題，有人提出付款通道作為可行的解決方案。微支付通道允許交易發生 off-chain，減少了整個網路不斷分享資料的需求。這可大幅減輕 Blockchain 的負擔，讓交易更快速、更便宜。

支付通道背後的基本原則是採取交易 off-chain 的概念。與其向整個網路廣播每筆交易，當事人可以開啟一個付款通道，在他們之間進行許多交易。只有通道的開啟和關閉才會被記錄在 Blockchain 上，大大提高了效率和隱私性。

儘管支付通道具有 off-chain 的性質，但仍可選擇強制執行交易 On-Chain。如果發生爭議或有一方試圖作弊，就可以將通道的最新狀態廣播給 Blockchain，確保商定的交易得以兌現，並正確分配資金。

支付通道代表了 Blockchain 技術的重大躍進，提供了一種可擴展且安全的交易方法，同時解決了與 Bitcoin 相關的許多基本問題。隨著我們在這些基礎上持續創新和發展，Blockchain 的未來看起來越來越有希望。

總括而言，瞭解 Bitcoin 的歷史背景與挑戰，以及透過 MHL、Lightning Network 與付款管道所提出的創新解決方案，可全面掌握 Blockchain 技術的現況與未來潛力。

## 原子路由的歷史

<chapterId>28be7b31-e6b2-5eea-a5ed-62ce0a154b6e</chapterId>

<professorId>880c7fa7-8d4c-4c9b-81b4-bc61ed256516</professorId>

:::video id=059a714b-4fe9-4266-acb0-6fe5af491662:::

在之前的討論中，我們涵蓋了基本付款管道的基本原理。這些管道允許兩個參與者，例如 Alice 和 Bob，直接進行無縫交易。然而，這個模式有一個明顯的限制：Alice 只能與 Bob 進行交易，而無法與 Charlie 等其他參與者進行交易，除非她與每個參與者都建立獨立的通道。這種多通道的必要性導致了低效率和可擴展性的問題，因為 Alice 要與她需要交易的每個人開啟直接通道是不切實際的。

### 集中式啤酒花

為了 Address 這些限制，Manny Rosenfeld 在 2012 年提出了集中式跳轉的概念。此模式引入了集中式支付處理器（如 TrustPay）來路由使用者之間的支付。雖然這種方法可以減少對多個直接通道的需求，但也引入了顯著的缺點。集中式跳轉存在安全問題、信任顧慮、隱私侵犯、詐騙可能性、審查和可靠性問題。使用者必須信任這些集中式實體才能促成交易，這與分散式的精神背道而馳。

### 哈希時間鎖 Contract (HTLC) 與實作

集中式跳躍的限制和缺點要求更安全和分散的解決方案。在此需求下，Joseph Poon 和 Thaddeus Dreijer 於 2015 年提出哈希時間鎖 Contract（HTLC），作為 Lightning Network 的一部分。HTLC 結合了時間鎖和 Hash 鎖的原理，以確保交易的原子性和不可信性。這表示交易要麼完全完成，要麼根本不會發生，從而降低與不完全支付相關的風險。

HTLC 的工作流程包含多個步驟，可確保透過多個中介進行安全路由。假設 Alice 想要透過中間人 Bob、Carol 和 Diana 支付 Eric。流程中的每個步驟都涉及建立時間鎖和金額遞減的 Commitment 交易。如有必要，最後一個步驟可以廣播到 Bitcoin 網路，以完成交易。

在 HTLC 中，Alice 以秘密「R」的 Hash 鎖定付款。鮑勃、卡蘿和黛安娜各自與後續的中介人建立類似的契約，確保他們只有在提出正確的秘密「R」時，才能領回自己的資金。此機制可確保原子性；付款完全完成或失敗，以防止部分資金損失。

![Hash lock](assets/en/4/2.webp)_Hash lock function_

### 實務考量與網路動態

在實際情況中，Alice 的付款流程涉及透過多個中間人 (例如 Bob、Carol 和 Diana) 向 Eric 付款。此鏈中的每位參與者都負責從前一位參與者抽取資金。

#### 頻道狀態更新

頻道根據參與者之間的相互協議和簽名更新其狀態。例如，Alice 和 Bob 不一定要使用秘密「R」，只要他們同意交易條款，就可以更新他們的通道狀態。

#### 確保原子性

HTLC 機制透過使用時間鎖及簽章來確保原子性。此保障措施可確保支付通訊協定保證完全成功或完全失敗，防止部分資金損失。

![Time lock and signatures](assets/en/4/3.webp)_Combine restrictions_

#### 獎勵與責任

像 Diana 和 Carol 這樣的中介人會受到激勵，在網路中採取正確的行為。如果他們沒有這樣做，後果通常只會影響中介本身，從而促進負責任的行為。

### 實務考量

但是，支付路由中更多的跳數會增加延遲、費用和潛在的不可靠。開放多個通道有助於減少路由所需的跳數，提高整體效率。

#### 通路圖與流動性

網路中的節點既可以是公開宣布的通道圖的一部分，也可以保持不被宣布。這些通道的流動性對有效路由起著關鍵作用，因為節點需要有足夠的餘額才能成功轉發付款。

#### 來源路由與隱私權

Alice 必須知道網路的拓樸結構，才能決定付款路徑。儘管付款路由經過多個中間人的複雜性，但仍採用來源路由來保護隱私。

![Source Routing](assets/en/4/4.webp)_Source Routing Path_

#### 總結

總而言之，適當的節點運作可確保原子式支付，而 Lightning Network 旨在 Address Ripple 等傳統支付系統所面臨的許多問題。透過利用 HTLC 和策略路由，Lightning Network 為分散式支付提供了更具擴充性、更有效率且更安全的解決方案。

## Bolt 評論

<chapterId>ba4b09ae-81de-53f2-8c15-316f037aaea9</chapterId>

:::video id=f0d17fe4-d793-4b90-924e-b551db501fbb:::

Bitcoin 網路以 Trustless 價值 Exchange 系統運作，主要作為結算 Layer，交易記錄在公共 Ledger 上。這可確保安全性和不變性，但也有其限制，尤其是在交易速度和費用方面。因此，Bitcoin 對於日常的小額交易可能效率不高。

進入 Lightning Network，它的功能是在 Bitcoin Blockchain 之上的第二個 Layer。此支付網路旨在促進快速且低成本的交易。只要在雙方之間開通付款通道，就可以進行 off-chain 交易，只需在 Bitcoin Blockchain 上記錄初始和最終結餘。這可大幅降低主網路的負載，增強可擴充性，並使微交易變得可行。

為了更好地掌握這個概念，請考慮酒吧帳單的比喻。當您在酒吧開帳時，您可以持續點飲料，但每次點飲料後都不需付款。最後，您會在晚上結束時結清總金額。同樣地，一個 Lightning 通道允許多次交易 off-chain，只有在通道關閉時才結算 On-Chain。另一個類比是機場，透過多個節點進行支付，就像搭乘轉機才能到達目的地。每個節點 (或「航班」) 都會幫助您將付款引導到它需要去的地方，確保有效率的路由。

![airport analogy](assets/en/4/5.webp)_The airport analogy of LN_

就本質而言，Lightning Network 可補足 Bitcoin 網路的不足，將其從純粹的結算 Layer 轉變為能有效處理日常交易的多功能系統。

### **Lightning Network 規格**

Lightning Network 通訊協定透過 10 個 BOLT（閃電技術基礎）進行仔細定義。這些 BOLTs 是在米蘭的一次會議上商定的，並作為各種 Lightning Network 實作的基礎。

![bolt](assets/en/4/6.webp)_BOLT Diagram _

#### Bolt 1 (基本通訊協定)

Bolt 1 使用類型-長度-值 (TLV) 結構概括了訊息格式，可確保不同的實作能夠一致地理解訊息。通訊通常透過特定的 TCP 連接埠進行，訊息可分為以下幾類


- 通訊訊息**：這些訊息包括 `Init`、`Error`、`Warning`、`Ping` 及 `Pong` 訊息，用來建立連線、處理錯誤、探查連線狀態及混淆通訊。
- 通道設定訊息**：這些訊息在通道建立階段非常重要。
- 通道狀態訊息**：這些訊息會處理活動頻道內的更新，確保雙方同步。
- Gossip 訊息**：這些訊息用於網路拓樸發現和更新。
- 實驗訊息**：這些訊息允許在不中斷網路的情況下測試新功能。

#### Bolt 2（通道生命週期）

Bolt 2 深入探討通道的生命週期，從建立到正常運作，最後到結算。主要流程包括


- 通道建立**：在此階段中，各方開啟通道、Exchange 簽名，並建立資金交易。
- 正常操作**：在此，頻道狀態會使用 Hash Time-Locked Contracts (HTLC) 持續更新。Commitment 和撤銷訊息可確保雙方同意目前的狀態。
- 結算**：這包括關閉通路，通常是透過雙方同意和費用協商，以完成交易，而不會進入無限期的關閉循環。

#### 更新機制

HTLC 在網路的付款路由中扮演舉足輕重的角色，讓安全交易無須信任。Commitment 和撤銷訊息可確保雙方就通道的狀態達成協議，並防止欺詐。

#### 特別訊息

更新費用」等特定訊息會調整 Commitment 交易的 Miner 費用，而「通道重新建立」訊息則會確保雙方對等機構在斷線後保持同步。

#### 關閉通道

若發現作弊行為，可透過雙方協議、單方面行動或懲罰來關閉通道。適當的關閉可安全地完成交易。

#### 流動性管理掉期

掉期可在不關閉通道的情況下實現 On-Chain 提款和高效的流動性管理。目前正在開發未來的解決方案，如拼接，以加強這個過程。

#### 安全措施

Commitment 交易結合了 nLockTime、OPCheckSequenceVerify 和撤銷金鑰等機制，以確保資金安全並防止盜竊。

### 路由與洋蔥路由

![onion routing](assets/en/4/7.webp)_Onion Routing diagram _

付款使用洋蔥路由，也就是建立透過多個節點傳送的加密封包。HTLC 可確保交易安全，確保隱私性與安全性。

### Invoice 結構

Lightning Network 發票 (Bolt 11) 以 Bech32 編碼，包含付款 Hash、說明和到期日等詳細資訊。每個 Invoice 必須使用一次，以防止重複使用的問題。

![Invoice structure](assets/en/4/8.webp)_BOLT11 Invoice_

#### 加密與驗證

握手程序和加密 (Chacha20) 與認證 (Poly1305) 可確保 Lightning 交易中訊息的完整性和隱私性。

#### 替代方案

其他付款請求方法如 LNURL、KeySend 和 Bolt 12 提供不同的功能和採用程度，為網路提供彈性。

#### 網路發現

Lightning Network 中的網路發現已從最初使用的 IRC（網路中繼通訊）演進到 Bolt 7 定義的更複雜的通訊協定。 此通訊協定使用特定的 Lightning 訊息（通常稱為 gossip 訊息）來發現和維護網路拓樸。

#### Bolt7 訊息

主要的 Bolt 7 訊息包括


- 節點公告**：此訊息廣播節點的存在。
- 頻道公告**：此訊息會通知網路關於新頻道的建立。
- 公告簽章**：這可確保廣播訊息的真實性。
- 頻道更新**：此訊息傳達有關頻道的更新，例如費用結構和 HTLC 的最高金額。

#### 頻道公告流程

此過程會從本地對等體交換身分和頻道詳細資料開始。在驗證簽章和提供交易資金之後，他們會向網路對等體公佈通道，確保整個網路保持最新的拓樸變化。

#### DNS Bootstrap

DNS 和 Bitcoin DNS seed 查詢提供 IP 和節點資訊，有助於發現 Lightning 對等點。這種初始發現機制有助於節點快速連接到網路。

#### 專題公告

節點可以廣播其支援的功能，確保向下相容性，同時允許可選的增強功能。這種靈活性可確保所有節點都能順利互動，即使通訊協定在演進。

#### 處理 Bolt11 發票

網路可確保 Bolt 11 發票的唯一性，避免同一 Invoice 的多次付款。如果重複使用 Invoice，網路節點會截取並防止重複付款，以維持交易完整性。

#### 語音資料傳輸

儘管如此，透過 Lightning Network 傳輸語音資料會嚴重壓縮，並受到訊息大小的限制。Sphinx 是一個應用範例，它探討如何創新使用 Lightning 來傳輸資料。

#### 使用案例與爭論

Lightning Network 的用途是一個持續爭論的話題。雖然 Lightning Network 主要是為支付而設計，但也在探討其他使用情況，例如資料傳輸，儘管並未被普遍接受。社群持續討論潛在的網路應用和通訊協定強化。

#### 社區討論

Lightning Network 社群充滿活力，不斷就使用個案、協定應用和潛在改進進行辯論和討論。這種協同合作的環境可促進創新，同時確保網路的發展能滿足使用者的需求。

總而言之，了解第二代 Layer 重要性、Lightning Network 規格以及網路發現機制，對於想要深入研究 Lightning Network 複雜性的人而言至關重要。這是一個複雜但高回報的領域，有望改變數位交易的未來。

## 主要 LN 客戶

<chapterId>a2ad8db4-aea2-5231-927c-616c53db31bf</chapterId>

:::video id=90240cb6-a942-4015-b0c2-b721c48309ec:::

Lightning Network (LN) 代表著 Bitcoin 在可擴展性和交易速度方面的重大突破。LN 客戶端（通常稱為 Lightning wallets）是專門的軟體或應用程式，可讓使用者透過 Lightning Network 進行交易。這些錢包是使用者與 LN 之間的重要 Interface，利用 off-chain 路徑促進即時結算、低費用的交易。

Lightning wallets 的設計讓交易過程更人性化，即使只有極少技術知識的人也能從先進的 Bitcoin 功能中獲益。透過實現快速且具成本效益的微交易，這些錢包將大大促進 Bitcoin 在日常交易中的廣泛應用。

![LN Clients](assets/en/4/9.webp)_Lightning Wallets_

### Bitcoin 皮夾 vs. Lightning 皮夾

Bitcoin 錢包和 Lightning 錢包在架構和使用案例上有根本的不同，儘管它們有私密金鑰管理的共同特徵：

#### Bitcoin 皮夾：


- 私密金鑰關注**：Bitcoin 電子錢包的主要焦點是誰持有私密金鑰。這決定了使用者資金的安全性和控制權。
- 交易複雜性**：Bitcoin 錢包會處理各種交易腳本，例如 Segregated Witness (SegWit) 和 Taproot，可優化交易規模並加強隱私和安全性。

#### 閃電錢夾：


- 私鑰管理**：與 Bitcoin 錢包類似，私密金鑰的控制仍然至關重要。
- 流動資金管理**：Lightning 電子錢包的一個顯著特點是需要管理流動資金，這涉及到本地（出境）和遠程（入境）流動資金的平衡，以確保交易路由順暢。這需要用戶了解並優化其渠道，以促進有效的支付轉發。

#### 閃電錢包的流動性管理

有效的流動資金管理是 Lightning Network 成功營運的基石。它涉及兩種主要流動資金的策略平衡：

#### 本地（出境）流動資金：


- 這代表使用者可從其 Lightning 頻道寄出的 Bitcoin 數量。它對於啟動付款和確保交易能傳送至收款人至關重要。

#### 遠端（入境）流動資金：


- 這代表使用者可透過其管道接收的 Bitcoin 數量。它同樣重要，因為它確保其他人可以向用戶發送付款。

#### 流動資金管理範例：

![Example of Liquidity](assets/en/4/10.webp)_Lightning Liquidity_

考慮一個涉及 Alice、Bob、Charlie 和 Dan 的情境 - 典型的 LN 使用者透過各種通道互連：


- Alice 想要支付 Dan，但她與 Bob 的通道中缺乏足夠的本地流動性。
- 如果 Bob 有足夠的餘額，並且與 Charlie 有通道，而 Charlie 與 Dan 有通道，Alice 的付款就可以經由 Bob 和 Charlie 到達 Dan。

![Example of Liquidity](assets/en/4/11.webp)_Lightning Liquidity_

但是，如果其中任何一個通道面臨枯竭或連線問題，交易可能會失敗。這說明了在整個網路中維持均衡流動性的重要性。

#### Lightning Network 的挑戰：


- 渠道枯竭**：隨著時間的推移，渠道可能會變得不平衡，資金集中在一邊，限制了交易能力。
- 連線問題**：高效率的交易路由需要強大的網路連線，而維護網路連線可能是一項挑戰。

為了克服這些挑戰，流動資金服務供應商 (LSP) 提供協助管理流動資金的服務，通常是收費的，以確保使用者維持最佳的渠道餘額，使交易順利進行。

### 不同錢包及其功能

有多種 Lightning wallets 可供選擇，每種都能滿足不同用戶的需求和喜好。以下是一些範例：

#### Satoshi 的 Wallet：


- 功能**：完全託管、使用者友善，但封閉源碼有潛在的隱私疑慮。

#### 阿爾比


- 功能**：瀏覽器延伸功能，開放原始碼，同時支援託管與非託管模式，增強通用性。

#### 微風：


- 特色**：手機上的輕量級節點，開放原始碼，結合自我保管與管理流動性，提供控制與便利的平衡。

#### 鳳凰城


- 功能**：與 Breeze 相似，利用 LSP 模型來管理流動資金，開放原始碼，著重於使用者的簡單性及有效的流動資金管理。

#### 開啟 Bitcoin Wallet (OBW)：


- 功能**：整合 On-Chain 和 Lightning 錢包，支援託管式頻道，開放原始碼並具備進階功能，適合功能強大的使用者。

### 託管與流動性管理矩陣

錢包可以根據誰持有私鑰和誰管理流動性進行分類。此矩阵可帮助用户选择符合其安全性和便利性偏好的钱包：


- 保管式錢包**：第三方持有私人金鑰，通常提供自動流動性管理。例如 Satoshi 的 Wallet。
- 非保管式錢包**：使用者持有私人金鑰，可能需要手動流動性管理。例如 Breeze 和 OBW。

![Liquidity Lightning](assets/en/4/12.webp)_2x2 Matrix of LN Clients_

### 批評與改進領域

儘管閃電錢包有許多好處，但也面臨一些批評和需要改進的地方：


- 隱私**：封閉式錢包和某些託管模式會引起隱私問題。
- 易用性**：如何在先進功能與易用性之間取得平衡仍是一項挑戰。
- 開放原始碼開發**：不同程度的開放原始碼貢獻會影響使用者信任度與創新速度。

### 其他洞察與使用案例

#### 演算法挑戰：

目前在 Lightning Network 內尋找最佳路徑的演算法通常都是次優的，涉及到試驗和錯誤。需要改進以提高路由效率。

#### 多部分付款：

將較大額的付款拆分成較小的交易，可以減輕流動性和路徑搜尋的問題，確保交易更順暢。

#### 來自路由的收益：

透過路由費賺取的收益通常微乎其微，這使得個人使用者為了獲利而運行路由節點的吸引力大打折扣。

#### 各種 Wallet 範例：


- Blink Wallet**：位於薩爾瓦多、保管、需要電話號碼、功能穩定的 Sats，但缺乏進階的 Lightning Network 功能。
- Blitz Wallet**：開放原始碼、自行保管、需要使用者管理的流動性，為強大使用者提供廣泛的資訊。
- SwissBitcoinPay**：專為商家設計，託管時間長達 24 小時，對於高交易量的用戶收費最低。

#### Wallet 使用個案：

不同的錢包有不同的用途，從初學者的易用性到高級使用者的進階功能。沒有單一「最佳」的 Wallet；選擇取決於個人需求和喜好。

#### 開放原始碼貢獻：

使用者對於開放原始碼專案的回饋與貢獻，對於開發與個人技能的成長是非常寶貴的，也促進了合作與創新的環境。

總之，瞭解 Lightning Network 客戶端各方面的情況、與傳統 Bitcoin 錢包的差異，以及有效管理流動性的重要性，對於充分發揮 Lightning Network 的潛力至關重要。透過選擇正確的 Wallet 並積極參與生態系統，使用者可以大幅提升 Bitcoin 的交易體驗。

# LN 的挑戰

<partId>ca58c9d7-ba7e-5392-8488-6a21a9850e6a</partId>

## LN 的實際挑戰

<chapterId>014c7c40-aef7-58ac-b51f-33784463f482</chapterId>

**（視訊即將推出）**

在本節中，Asi0 將探討使用 Lightning Network (LN) 時所面臨的實際挑戰。儘管 Lightning Network 採用革命性的方式來擴充 Bitcoin 交易，但它仍提出了使用者和開發人員必須克服的幾項實際挑戰。我們將特別探討四大挑戰： ***流動資金管理**、**Layer 1/Layer 2 抽象**、**接收離線付款**以及**備份管理**。

每項挑戰都從兩個角度來看：**使用者**和**開發人員**，因為您在生態系統中扮演的角色不同，挑戰和解決方案也不同。

---
### 挑戰 1：流動資金管理

#### **從使用者的角度來看：**

在 Lightning Network 中，**流動資金**是指支付或收款所需的支付通道中的可用資金。使用者需要確保有足夠的入站和出站流動資金，才能成功進行交易。例如，如果您想接收付款，您必須有可用的入站流動資金，這表示另一個節點必須分配其部分餘額給您的通道。同樣地，如果您想發送付款，您的通道中就需要出站流動資金。


- 實際問題**：使用者經常發現很難平衡他們的通路並維持足夠的流動性。此外，頻道重新平衡也會產生成本。
- 可能的解決方案**：一些 Lightning 錢包已開始整合自動通道再平衡功能，但此功能仍在開發中。用戶也依賴**閃電服務供應商（LSP）**來協助進行流動性管理。

#### **從開發人員的角度來看：**

開發人員面臨在應用程式中實施無縫流動性管理的挑戰。他們需要創建工具，自動進行再平衡，減少使用者的摩擦，同時優化費用，避免流動性瓶頸。


- 實際問題**：在流動性可變的網路中實作有效的付款路由演算法，可能相當複雜且需要大量計算。
- 可能的解決方案**：開發人員正在探索**流動資金路由**的先進演算法，並利用**雙資金管道**，以確保交易兩端都有流動資金可用。

> **定義**：
>

> - **流動性**：在「閃電」通路中可用於付款或收款的資金。
> - **LSP (Lightning Service Provider)**：可協助使用者在 Lightning Network 上管理流動資金和頻道的服務。
---
### 挑戰 2：L1/L2 抽象

#### **從使用者的角度來看：**

對使用者而言，**Layer 1 (L1)** (Bitcoin 的基礎 Layer)與**Layer 2 (L2)** (Lightning Network)之間的互動通常無法完全抽象化。例如，開啟和關閉通道需要 On-Chain Bitcoin 交易 (L1)，使用者必須為這些動作支付 On-Chain 費用。當 Bitcoin 網路擁擠時，這會帶來額外的複雜性和潛在的延遲。


- 實際問題**：用戶在與Bitcoin base Layer互動時，往往難以理解與Lightning Layer互動時的複雜性。這可能導致費用、交易時間和安全性方面的困惑。
- 可能的解決方案**：改進的 Wallet 設計可抽象 L1/L2 互動，並在後台管理通道開啟/關閉。有些錢包已經允許用戶根據情況在 On-Chain 和 Lightning 交易之間無縫切換。

#### **從開發人員的角度來看：**

開發人員的任務是為用戶抽象出 L1 和 L2 的複雜性，創建流暢直觀的介面，高效處理交易。我們面臨的挑戰是在保持 Lightning 協定完整性和安全性的同時，優化用戶體驗。


- 實際問題**：確保使用者免於管理通路和 On-Chain 交易的複雜技術問題，同時在需要時保持透明度。
- 可能的解決方案**：開發人員正在開發一些功能，例如 **拼接**（允許在不關閉頻道的情況下從頻道中新增或移除資金）和自動頻道管理工具。

> **定義**：
>

> - **L1 (Layer 1)**：Bitcoin 的主 Blockchain Layer。
> - **L2 (Layer 2)**：Lightning Network，在 Bitcoin 的基礎上運作，使交易速度更快、成本更低。
> - **分割**：一種可修改 Lightning 通道平衡的技術，無需關閉通道。
---
### 挑戰 3：接收離線付款

#### **從使用者的角度來看：**

Lightning Network 的挑戰之一是**在使用者離線時接收付款。與 Bitcoin 的基礎 Layer 可以隨時接收交易不同，Lightning 需要付款人和收款人都在線上才能完成交易。這對於許多希望在日常情況下使用 Lightning 付款的使用者而言，是一大限制。


- 實際問題**：除非用戶的節點在線並連接至網路，否則用戶無法接收付款，這對於想要使用 Lightning 作為日常付款方式的用戶來說很不方便。
- 可能的解決方案**：一些變通方案包括使用託管式錢包，或在收款節點上線前，仰賴第三方服務作為付款中介。

#### **從開發人員的角度來看：**

開發人員正在探索如何讓用戶在節點離線時也能收到 Lightning 付款。這需要創造性的解決方案，以保持 Lightning 的分散性，同時解決經常連線的實際問題。


- 實際問題**：開發一個協定或系統，讓使用者可以在不影響安全性或分散性的情況下離線接收付款，是一項重大的技術挑戰。
- 可能的解決方案**：目前正在研究**離線付款憑證**，此憑證可讓收款人在重新連線至網路後申請付款。

> **定義**：
>

> - ** 離線付款**：一方未連線至 Lightning Network 時發送或接收的付款。
> - ** 監護錢包**：由第三方控制私人金鑰並代表使用者管理交易的錢包。
---
### 挑戰 4：備份管理

#### **從使用者的角度來看：**

備份 Lightning 通道對於用戶在節點宕機或資料丟失時恢復資金是非常重要的。然而，Lightning 通道的備份過程比 Bitcoin 更為複雜，因為通道是有狀態的，這意味著它們會隨著每次交易而改變。


- 實際問題**：使用者需要確保他們的頻道備份是最新的，因為使用過期的備份可能會導致資金損失或受到網路懲罰。
- 可能的解決方案**：Phoenix 等錢包已實現自動通道備份，但這些功能尚未普及到所有 Lightning 錢包。

#### **從開發人員的角度來看：**

開發人員需要實施備份解決方案，讓用戶即使在災難性故障後也能安全可靠地恢復資金。我們面臨的挑戰是如何確保這些解決方案既安全又易用，同時還能保持 Lightning 協定的完整性。


- 實際問題**：設計安全、分散且使用者友善的備份系統是一大挑戰，因為備份必須隨著通道的每次狀態變更而保持更新。
- 可能的解決方案**： **已開發靜態通道備份 (SCB)** 以簡化復原，但需要更先進的解決方案以進行完全自動化的安全備份。

> **定義**：
>

> - **靜態通道備份（SCB）**：一種備份類型，可讓使用者在 Lightning 通道發生故障時，透過還原通道的最新狀態來復原其資金。
---
#### 總結

Lightning Network 在 Bitcoin 交易的速度和成本效益方面提供了巨大的優勢，但也提出了幾項實際挑戰。這些挑戰-***流動性管理***、***L1/L2 抽象***、***接收離線付款***以及***備份管理***-都需要使用者和開發人員提供創新的解決方案。隨著網路持續演進，克服這些障礙將是達成廣泛採用及改善整體使用者體驗的關鍵。

透過解決這些挑戰，Lightning Network 將會持續成熟，成為更穩健可靠的解決方案，以擴充 Bitcoin。

## LN 未來演進

<chapterId>c06763dd-bb26-5fec-8ac4-3e446e9517cd</chapterId>

<professorId>880c7fa7-8d4c-4c9b-81b4-bc61ed256516</professorId>

:::video id=ab5f65f1-0b0d-4ca9-8ff7-d42764c1e915:::

### Bitcoin 的彈性與進化

**Bitcoin 吉祥物：蜜獾**

Bitcoin 經常以蜜獾作為化身，蜜獾以其堅韌和不屈而聞名。這個象徵正好代表 Bitcoin 堅強不屈的天性。就像蜜獾能經受毒咬而繼續茁壯成長一樣，Bitcoin 也在各種逆境中展現了非凡的韌性，包括監管挑戰、市場波動和技術攻擊。

**Bitcoin 的本質：不斷進化**

與一成不變的概念相反，Bitcoin 正處於永續演進的狀態。它的通訊協定和生態系統由全球的開發人員和研究人員社群不斷改進和完善。這個演進過程是由增強安全性、擴充性和功能性的需求所驅動，以確保 Bitcoin 在加密貨幣領域中保持領先地位。

### Lightning Network 的創新

**Lightning Network：快速開發**

Lightning Network 是 Bitcoin 的第二個-Layer 解決方案，用於擴大交易規模和加快交易速度，目前正在快速開發中。此 Layer 可透過 off-chain 支付通道實現快速、低成本的交易。目前正在整合重要的創新技術，以提高其效率和可用性。

**雙資助管道**

傳統上，Lightning 通道由一方提供資金。但是，雙方出資的通道允許雙方（例如 Alice 和 Bob）為通道的流動性出資。這種增強功能有助於提高發送和接收容量的靈活性，但需要進行前期溝通，並制定新協議來管理聯合資金。

**拼接**

拼接（Spliting）是一項允許用戶在不關閉Lightning通道的情況下修改其大小的功能。此功能可從現有通道中增加或移除資金，提供管理通道流動性的無縫方式。拼接功能促進了 On-Chain 交易和 Lightning 通道之間的互操作性，提高了整體網路效率。

**L2 機制**

L2 機制引進了一種新方法來使舊通道狀態失效，而不需依賴懲罰機制。此更新依賴 SIGHASH_ANYPREVOUT，此功能需要 Bitcoin Soft Fork。L2 機制有望簡化通道管理並提高安全性。

**Bolt 12**

Bolt 12 可解決 Lightning Network 目前使用的 Bolt 11 發票的限制。它引入了可重複使用的發票，並將流程自動化，僅在 Lightning Network 內運作，無需 HTTP 和 Web 伺服器。這項創新可簡化交易並提升使用者體驗。

### 提升 Bitcoin 交易的隱私與效率

**Taproot、MuSig 和 Schnorr 簽名**

Taproot 是一項重大升級，可整合交易複雜性並加強隱私性。Taproot 與 MuSig（多簽署交易協定）和 Schnorr Signatures 相結合，可提高交易效率。這些進步讓 Lightning 交易類似於一般的 Bitcoin 交易，簡化了流程並加強了隱私保護。

**PTLC 路由**

點時間鎖定合約 (PTLC) 是現有 Hash 時間鎖定合約 (HTLC) 的改進。PTLC 使用 Schnorr 簽署，並透過以公開金鑰取代共用機密來改善隱私權，從而降低付款關聯性和濫用的可能性。

**通道工廠**

頻道工廠可建立多方頻道 (例如 4 對 4 Multisig)，進而產生新的 2 對 2 付款頻道 off-chain。此系統允許快速、免費地建立和關閉通道，儘管它需要所有參與者的合作。通道工廠可增加 Lightning Network 的整體擴充性與彈性。

**Watchtowers**

Watchtowers 是監控 Blockchain 舊通道狀態的第三方實體。如果偵測到違規行為，它們會公佈懲罰交易，以確保網路安全。雖然 Watchtowers 可以阻止不當行為，從而提高安全性，但它們也會引入有關監控交易的隱私問題。

**blinded 路徑**

blinded 路徑的設計是為了加強 Lightning Network 中接收者的隱私。它們會遮蔽最終接收者的 Address，確保只有寄件者知道中間節點，而每個節點只知道其相鄰節點。此方法可保護接收者的身分並增強整體隱私。

**閃電服務供應商 (LSP)**

Lightning Service Providers (LSP) 由 Breeze Wallet 提出概念，旨在透過即時接收功能改善使用者體驗。LSPs為用戶打開通道，類似於互聯網服務供應商提供連接服務的方式。這項創新簡化了用戶上線流程，並確保在 Lightning Network 上進行無縫互動。

**保持更新的資源**

要掌握 Bitcoin 和 Lightning Network 的最新技術創新，必須善用寶貴的資源。Bitcoin OpTec 電子報、lightning dev 郵件清單，以及來自業界專家（如 Jason Lopp）的資料，可提供有關這個快速發展領域的持續進步和研究的深入見解和最新資訊。

藉由瞭解和欣賞這些發展，我們可以認知到 Bitcoin 和 Lightning Network 對未來數位交易所帶來的多方面進展和潛力。

## LN 上的通訊協定

<chapterId>f4d147bb-f146-5b36-a994-b9b70da83744</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

:::video id=ffee9682-1bfa-4717-9f22-9bc1baff0722:::

### 擴展和整合 Lightning Payments

#### 瞭解 Lightning Payments

在深入探討 Lightning 付款的擴充與整合之前，了解 Lightning 付款的基本操作是非常重要的。傳統的 Lightning 付款涉及幾個關鍵部分：**付款人**、**收款人**和**Lightning Network**本身。付款人透過產生一個**Invoice**，向收款人啟動付款，該**Invoice**包含一些關鍵資訊，例如要支付的金額和目的地（收款人的節點）。

此過程依賴 **Hash 時間鎖定合約 (HTLC)**，可確保付款只能由合法收款人在指定時間內領取。此機制中兩個重要的 Elements 是 ** 洋蔥路由** 和 **HTLC 鏈**：


- 洋蔥路由**：透過分層封裝交易資料來提供隱私，確保每個中介只知道其前後的節點，而不知道整個路由。
- HTLC Chain**：一系列鎖定資金的合約，直到付款完成或還原為止。

**Keysend**是增強 Lightning Network 功能的最新通訊協定。傳統的 generate 和 Invoice 需要寄件者和收件者事先溝通，Keysend 則不同，它可讓**寄件者主動付款**，簡化流程並改善使用者體驗。

不過，傳統發票也有其限制。例如：


- 單次使用**：發票通常只用於一次交易，可能會造成不便。
- 尺寸限制**：大型發票很難以 QR 代碼的形式處理，因此對某些應用程式來說並不可行。

> **定義**：
>

> - **Invoice**：Lightning Network 中的付款請求，通常包含金額和收款人詳細資訊。
> - **HTLC（Hash 時限鎖定 Contract）**：Smart contract 的一種，用於確保在時間限制內有條件付款。
> - ** 洋蔥路由**：一種隱私技術，交易資料像洋蔥一樣分層，以保護寄件者和收件者的身分。
### 通訊協定與使用案例

商業模式與先進通訊協定

儘管有傳統發票的限制，但仍出現了幾種協定來擴展和加強 Lightning 付款。


- LNURL**：一種簡化 Invoice 生成的通訊協定，允許動態建立發票、支援法幣面額，並可使用 **Lightning 位址**。此方法可提供更靈活的付款方式，並與不同的使用個案整合，大幅提升使用者體驗。
- Bolt 12 提供**：此協定與 LNURL 相似，但利用**洋蔥訊息**來增強隱私性。Bolt 12 可讓使用者自動取得發票，無須手動介入，提高隱私性與可用性。

其中一個值得注意的 Lightning 付款整合是在 **Nostr**，一個分散的社交媒體平台。Nostr 整合了 Lightning 付款，以實現小費和微交易，展示了 Lightning 如何嵌入到各種應用程式中。

另一個協定 **RGB**，可透過 Lightning Network 進行 ** 資產轉移，進一步擴展 Lightning 的功能。RGB 允許透過 Lightning 通道轉移包括代幣在內的各種資產，擴大了可交易的範圍。

**Lightning Liquidity Service Providers (LSP) **也在擴展Lightning付款中扮演重要角色。LSP 為接收付款提供流動資金，協助開啟**雙資金通道**，並透過即時攔截付款和開啟通道，確保交易無縫進行。

> **定義**：
>

> - **LNURL**：可建立動態 Invoice 的通訊協定，讓付款更輕鬆、更靈活。
> - **Bolt 12**：Lightning 的延伸，可利用洋蔥訊息來保護隱私，同時自動化 Invoice 抓取。
> - **Nostr**：整合 LP 協定與使用個案的分散式平台
> 微交易付款。
> - **RGB協定**：可透過 Lightning Network 傳輸資產（如代幣）的協定。
> - **LSP (Lightning Service Provider)**：為 Lightning 交易提供流動資金和開放渠道的實體，讓使用者更容易使用網路。
### 商業模式與先進通訊協定

Lightning 支付技術的進步為新的商業模式鋪平了道路，特別是對**Lightning 服務提供商 (LSP)** 而言。LSP 只會在偵測到付款時才開啟通道，從而減少預先設定的複雜性，從而提升用戶體驗。

Lightning促進的商業模式的一個例子是**拍賣模式**。在這種模式下，伺服器會保留最高出價，並拒絕較低出價，在拍賣結束前保持付款待定。這避免了退款的需要，並簡化了拍賣流程。

另一個實例是在**撲克遊戲**中，伺服器透過保留投注直到遊戲結束來管理付款，確保投注過程順利。

Lightning 支付也被整合到**Nostr**等平台和播客服務中，展示了這些協定的多功能性。此外，付款的**前影像**可用作**存取鑰匙**，以解鎖內容或服務，進一步增加 Lightning Network 的實用性。

先進的通訊協定，如 ** 點時間鎖定合約 (PTLC) **，透過啟用更複雜的加密操作，讓 Lightning 更進一步。PTLCs 改善了路由和付款分割，提高了安全性和效率。

**LNURL**和**Bolt 12**等通訊協定可減少手動互動，從而簡化付款程序，確保 Lightning Network 更為人性化，並獲得廣泛採用。

> **定義**：
>

> - **PTLC (Point Time-Locked Contract)**：一種在 HTLC 的基礎上加以改良的加密原始碼，可實現更靈活、更安全的支付。
> - **預設影像**：用於解鎖 HTLC 的值，也可以作為服務的存取金鑰。
> - ** 拍賣模式**：一種付款模式，在拍賣過程中，付款會暫停，只有在接受最高出價時才會發放。
### 總結

Lightning 支付通過各種協定和用例進行擴展和整合，展示了 Lightning Network 的動態演進。從改善支付的基本功能到引進先進的商業模式和加密協定，Lightning 的未來在創新和廣泛採用方面大有可為。

# 獎金

<partId>4c5c74d7-40a9-5292-9b82-e3f3d79875e1</partId>

## Bitcoin Mining 精華版

<chapterId>a4eacfc3-7b37-5fa3-abd1-b1fc48b645f0</chapterId>

<professorId>e320ccda-be59-492b-a81b-243d9acb592f</professorId>

:::video id=161d074d-4a81-48da-b2c9-9bde041a0da5:::

#### 簡介

Ajelex 著重於 Bitcoin Mining 的商業層面，研究在競爭激烈的市場中維持獲利能力的策略。討論內容包括營運成本分析、效率措施以及推動 Mining 產業的經濟因素。

### 1.Mining 複雜性與獲利因素

#### 技術與策略因素

Mining 複雜性在 Bitcoin 的範圍內主要涉及決定 Mining 營運利潤的技術性和策略性 Elements。最關鍵的是要了解 Mining 並非純粹的機率遊戲，而是一個需要仔細規劃和持續最佳化的複雜過程。

#### 主要獲利因素

![energy cost](assets/en/bonus/mining/1.webp)

1. **電力成本**：電力成本是影響 Mining 獲利能力的最重要因素之一。在法國等地區，相較於薩爾瓦多等國家，電力可能相對昂貴，而在薩爾瓦多等國家，較低的成本可為礦業者提供競爭優勢。

2. **硬體效率**：Mining 硬體的效率，以 Hash 的速率和耗電量來衡量，起著舉足輕重的作用。S19J Pro 等先進 ASIC 礦機的效率遠高於 Antminer S9 等舊型號。

3. **時期**：Bitcoin Mining 鼓勵長期規劃。

4. **BTC 價格**：BTC 價格是決定 Mining 盈利能力的關鍵。

5. **網路難度**：網路難度代表在 10 分鐘內挖掘一個區塊所需的平均 Hashrate 數量。

6. **策略工具**：[braiins.com](https://insights.braiins.com) 之類的工具對於計算獲利能力和幫助礦工做出以數據為導向的決策非常寶貴。

#### 實際應用

根據我的個人經驗，我甚至使用 Mining 為我在法國的公寓供暖，在 Mining Bitcoin 的同時創造性地抵銷了電費。這個例子強調了將 Mining 運作融入日常生活以獲得更多好處的實用性。

#### Mining 的瓶頸

礦工面臨三大主要瓶頸：硬體供應、能源存取，以及維持營運所需的資金。由於需求量大而造成 ASIC 的稀缺，往往導致等待時間過長和價格膨脹，使 Mining 的情況更加複雜。


- **能源瓶頸**的範例。

2021 年，中國政府禁止在其境內使用 Mining，導致中國的 Mining 公司無法獲得能源。這導致 Hashrate 在兩週內下跌了**50%**。

![hashrate drop](assets/en/bonus/mining/4.webp)

---
### 2.Mining 硬體的演進與效率

#### 歷史演進

Mining 硬體的發展歷程是不朽的，從簡單的 CPU Mining 到我們今天使用的高度專業化的 ASIC 礦機。

![evolution hardware](assets/en/bonus/mining/3.webp)

1. **CPU Mining**：早期，Mining 是使用一般電腦處理器 (CPU) 執行。隨著網路的成長，這種方法很快就被超越。

2. **GPU Mining**：圖形處理單元 (GPU) 大幅提升了 Mining 的效率，使 CPU 在 Mining 用途上變得過時。

3. **FPGA Mining**：現場可程式閘陣列 (FPGA) 提供比 GPU 更佳的效能與能源效率。

4. **ASIC Mining**：特定應用程式整合電路 (ASIC) 代表 Mining 硬體效率的頂峰，專為 Mining 作業而設計，具有無與倫比的效能。

#### 詳細比較：S19J Pro vs. Antminer S9


- S19J Pro**：S19J Pro 以高效率和高可靠性著稱，提供優異的 Hash 速率與較低的耗電量，是大型作業的理想選擇。
- Antminer S9**：雖然 Antminer S9 較舊且效率較低，但由於其經濟實惠且效能不俗，仍深受小型裝置和業餘愛好者的歡迎。

![s19j pro vs antminer s9](assets/en/bonus/mining/2.webp)

#### Mining 效率與學習

Mining 不僅提供財務獎勵，還提供寶貴的實踐經驗。透過 Mining 獲取免 KYC 的比特幣，對於那些關心隱私權的人來說是一個很有吸引力的建議。

#### 進階工具與技術

售後軟體可提升 Mining 硬體的效率與功能。提供最佳化與自動調整功能的工具可確保每顆晶片都能以最高效率運作，有效平衡 Hash 的速率與耗電量。

---
### 3.Mining 業務的法規與市場動態

#### 法規影響

法規對 Mining 格局的形成起著重要作用。例如，中國的 Mining 禁令對全球 Mining 業務產生了深遠的影響，使網絡 Hash 率大幅下降，並導致 Mining 的力量在不同地區重新分配。

#### 市場動態

1. ** 硬體供應與成本**：ASIC 礦機的價格和可用性受 Bitcoin 的市場價格影響。牛市期間的高需求會造成稀缺性和價格膨脹。

2. **Hash 價值與 Hash 價格**：了解 Hash 價值 (每天每太拉希賺取的薩托希) 與 Hash 價格 (Hash 價格的貨幣價值) 之間的區別是非常重要的。兩者都會受到網路難度和 Bitcoin 市價的影響。

#### Mining 儲存庫與獎勵機制

1. **Mining資源池**：透過整合資源，Mining 遊戲池能提供更穩定的獎勵，降低單人 Mining 遊戲的差異與風險。

2. **Reward Schemes**：不同的獎勵機制，如按份付酬 (PPS) 和按比例獎勵，為礦工提供了各種風險和獎勵狀況。


   - 按份付費**：按份付費 (Pay-Per-Share) 會對礦工提交的每份有效份數進行獎勵，而不論資料池是否找到區塊。 **Shares** 是證明礦工已完成所需工作的單位，而算力池會驗證這些股份。

![pps](assets/en/bonus/mining/6.webp)


   - 比例**：它取決於 Mining 區塊的 Miner 對區塊總 Hashrate 的貢獻來平均分配獎勵。

![prop](assets/en/bonus/mining/5.webp)

#### Mining 的未來

隨著區塊獎勵的減少，礦工將越來越依賴交易費用。這種轉變令人擔心，單靠交易費是否足以激勵礦工繼續保護網路安全。

#### 主機 Mining

託管式 Mining 服務可提供較低的作業成本，但也有風險，例如缺乏控制和可能發生詐欺。為了降低這些風險，適當的盡職調查是必要的。

#### 安全與效率

先進的安全通訊協定和可再生能源的使用，不僅提升了獲利能力，也有助於 Mining 生態系統的永續成長。

總而言之，Bitcoin Mining 的世界是一個複雜、多元的領域，需要對技術、策略、法規和市場動態有深入的瞭解。感謝您的關注，我期待您的提問和討論。

## 瞭解 Joinmarket

<chapterId>f109f64f-9b73-5fbf-8870-5d34d5b69df8</chapterId>

<professorId>6cfd206c-53b8-47a0-bbf4-44fd84e6ee1d</professorId>

:::video id=b89f2064-f2e1-49c3-97d0-580891eee1dd:::

Adam Gibson 深入介紹 Joinmarket，詳細說明這個 CoinJoin 實作如何增強 Bitcoin 的隱私和可替代性。他討論 Joinmarket 如何在 Bitcoin 生態系統裡促進協作、Trustless 及匿名交易。然後，在第二部分，他展示如何在 Signet 執行 Joinmarket。

## Cubo+ 第一年黑客研討會

<chapterId>3faf7daa-ea42-5b68-bcaf-04b70b2e02dd</chapterId>

### Groupe 1 Hackathon - Satoshi 傳承

:::video id=d78b199e-39cd-4d3c-b478-1502ba9c952a:::

Satoshi Legacy 的小組介紹他們使用 Shopify、React JS 和 Hydrogen 以及 IBEX 付款閘道建立 Lightning 電子商務的工作。

### Groupe 2 Hackathon - Honey Badger

:::video id=2159b401-e195-4bc8-9046-67a05c6ab7ea:::

Honey Badger 的小組介紹了她的解決方案，利用 LnBits 和 Next.js、Node.js 和 Hydrogen，在部落格中內建 Lightning Powered Micropayments。

### Groupe 3 Hackathon

:::video id=eb1e3c20-03ea-4ff8-b018-d197377a85cf:::

第三組透過客製化 API、LND、vue.js、node.js、Bootstrap 來呈現 Lightning Network Node Dashboard。

### Groupe 4 Hackathon - Satoshi 獎學金

:::video id=de1f6032-a0fa-49b0-82eb-18ba0e631756:::

Satoshi 的 Fellowship's 小組展示使用 LnBits 和 MongoDB、Poetry、Node.js 的 LN 遊戲應用程式。

### Groupe 5 Hackathon - Lighting Walker

:::video id=1328bada-4fd1-494a-83c6-f147a4880448:::

Lightning Walker 小組展示了他們使用 MySQL、JavaScript 和 ZDB 的 API 來提供匯款服務的解決方案。

# 總結

<partId>a633fb0c-839c-4405-8b77-2377cce79dd7</partId>

## 評論與評分

<chapterId>7f4f46e2-de71-5387-8609-9785fb9e5946</chapterId>

<isCourseReview>true</isCourseReview>
## 總結

<chapterId>33cb95cf-91d1-555b-a33b-0e3bd6745c33</chapterId>

<isCourseConclusion>true</isCourseConclusion>