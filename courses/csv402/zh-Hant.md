---
name: RGB 協定，從理論到實踐
goal: 獲得瞭解和使用 RGB 所需的技能
objectives: 

  - 瞭解 RGB 通訊協定的基本概念
  - 掌握 Client-side Validation 和 Bitcoin 承諾的原則
  - 學習如何建立、管理和轉移 RGB 合約
  - 如何操作與 RGB 相容的 Lightning 節點

---
# 發現 RGB 通訊協定

潛入 RGB 的世界，RGB 協定是基於 Bitcoin Blockchain 的共識規則和運作而設計，以契約和資產的形式實現和強制執行數位權利。本綜合訓練課程將引導您了解 RGB 的技術與實務基礎，從「Client-side Validation」與「單次使用封印」的概念，到進階智慧型契約的實作。

透過結構化、循序漸進的程式，您將發現 Client-side Validation 的機制、Bitcoin 上的確定承諾以及使用者之間的互動模式。學習如何在 Bitcoin 或 Lightning Network 上建立、管理和轉移 RGB 代幣。

無論您是開發人員、Bitcoin 愛好者，或只是好奇想進一步瞭解這項技術，本訓練課程都將為您提供掌握 RGB 和在 Bitcoin 上建立創新解決方案所需的工具和知識。

本課程以 Fulgur'Ventures 舉辦的現場研討會為基礎，由三位知名老師和 RGB 專家教授。

+++
# 簡介

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## 課程介紹

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

大家好，歡迎來到這個專門針對 RGB 的訓練課程，RGB 是在 Bitcoin 和 Lightning Network 上執行的客戶端驗證 Smart contract 系統。本課程的結構設計是為了能夠深入探索這個複雜的主題。以下是本課程的組織方式：

**第 1 節：理論

第一部分專門講解理解 Client-side Validation 和 RGB 基礎所需的理論概念。正如您在本課程中所發現的，RGB 引進了許多在 Bitcoin 中並不常見的技術概念。在本節中，您還可以找到詞彙表，提供 RGB 協定特有的所有詞彙定義。

**第二節：練習

第二節將著重於第一節中所看到的理論概念的應用。我們將學習如何建立和操作 RGB 契約。我們也會看到如何使用這些工具來編程。前兩節由 Maxim Orlovsky 主講。

**第 3 節：應用

最後一節由其他講者帶領，介紹以 RGB 為基礎的具體應用，強調現實生活中的使用案例。

---
本訓練課程最初源自於 [Fulgur'Ventures](https://fulgur.ventures/) 在托斯卡尼 Viareggio 舉辦的為期兩週的進階開發開發營。第一週的課程著重於 Rust 和 SDK，您可以在其他課程中找到：

https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58
在本課程中，我們將專注於 RGB 訓練營的第二週。

**Week 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**第 2 週 - 目前的訓練 CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

非常感謝這些現場課程的主辦單位以及參與的三位老師：


- Maxim Orlovsky： *Ex Tenebrae sententia sapiens dominabitur astris.Cypher、人工智能、機器人、超人類主義。RGB、Prime、Radiant 和 lnp_bp、mycitadel_io & cyphernet_io* 的創造者；
- 亨特-特魯吉洛 *開發人員、Rust、Bitcoin、閃電、RGB* ；
- 費德里科-滕加 *我正在為將世界變成 Cypherpunk 烏托邦盡一己之力。目前正在 Bitfinex* 研究 RGB。

本訓練課程的書面版本是使用 2 個主要資源起草的：


- Maxim Orlovsky、Hunter Trujilo 和 Frederico Tenga 在 Lightning Bootcamp 的研討會影片 ；
- RGB 文件，由 [Bitfinex](https://www.bitfinex.com/) 贊助製作。

# 理論上的 RGB

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## 分散式運算概念簡介

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::

RGB 是基於 Bitcoin Blockchain 的共識規則與運作，以可擴充與保密的方式應用與強制執行數位權利 (合約與資產的形式) 的通訊協定。第一章的目的是介紹 RGB 協定的基本概念和術語，特別強調其與 Client-side Validation 和單次使用封印等基本分散式運算概念的密切關聯。

在本章中，我們將探討**分散式共識系統**的基本原理，並瞭解 RGB 如何融入這個技術系列。我們也將介紹一些主要原則，這些原則有助於我們瞭解 RGB 為何以可擴充和獨立於 Bitcoin 本身的共識機制為目標，同時在必要時依賴它。

### 簡介

分散式運算是電腦科學的一個特定分支，研究用於在節點網路中流通和處理資訊的通訊協定。這些節點和通訊協定規則共同構成了所謂的分散式系統。這種系統的基本特性包括 ：


- 每個節點對特定資料進行獨立驗證及確認的**能力；
- 節點建構完整或部分資訊視圖的可能性（取決於協定）。這些視圖就是分散式系統的**狀態；
- 操作的**時序**，使資料有可靠的時間戳記，並對事件的順序（狀態順序）達成共識。

特別是，分散式系統中的**共識**概念涵蓋兩方面：


- 確認狀態變更的有效性**（根據協議規則）；
- 這些狀態變更的**協定順序，使後續無法重寫或逆向驗證的作業（這在 Bitcoin 中也稱為「雙重花費保護」）。

Satoshi Nakamoto 以 Bitcoin 引入了第一個功能性、無權限的分散式共識機制實現，這要歸功於 Blockchain 資料結構和 Proof-of-Work (PoW) 演算法的結合使用。在這個系統中，區塊歷史的可信度取決於節點（礦工）對其投入的計算能力。因此，Bitcoin 是分佈式共識系統的主要歷史性案例，對所有人開放（*無權限*）。

在 Blockchain 和分散式運算的世界裡，我們可以區分出兩種基本範例： *傳統意義上的 Blockchain****，以及***狀態通道*****，其中最佳的生產範例就是 Lightning Network。Blockchain 被定義為一個按時間順序排列的事件登錄器，在一個開放、無權限的網絡中以共識方式複製。另一方面，狀態通道是對等通道，可讓兩個（或更多）參與者維持更新的狀態 off-chain，僅在開啟和關閉這些通道時使用 Blockchain。

在 Bitcoin 的背景下，您無疑已經熟悉了 Mining 的原則、Blockchain 上交易的去中心化和終局性，以及支付通道的工作方式。有了 RGB，我們將引進一個新的範例，稱為 **Client-side Validation**，與 Blockchain 或 Lightning 不同，它包含本機（客戶端）儲存和驗證 Smart contract 的狀態轉換。這也有別於其他「DeFi」技術 (_rollups_、_plasma_、_ARK_ 等)，因為 Client-side Validation 依賴 Blockchain 來防止 Double-spending 並擁有時間戳記系統，同時只與相關參與者保留 off-chain 狀態和轉換的登錄器。

![RGB-Bitcoin](assets/fr/003.webp)

稍後，我們還會介紹一個重要的名詞：「**Stash**」的概念，它是指保存 Contract 狀態所需的客戶端資料集，因為這些資料不會在網路上進行全局複製。最後，我們將探討 RGB 背後的原理，這是一個利用 Client-side Validation 的通訊協定，以及為什麼它可以補充現有的方法 (Blockchain 和狀態通道)。

### 分散式運算的三難問題

要瞭解 Client-side Validation 和 RGB Address 如何解決 Blockchain 和 Lightning 未解決的問題，讓我們來發現分散式運算中的 3 大「三難題」：


- 可擴充、分散、隱私** ；
- CAP** 理論 (一致性、可用性、分割容忍度) ；
- CIA** 三難點 (機密性、完整性、可用性)。

#### 1.可擴充性、分散性和機密性


- Blockchain (Bitcoin)**

Blockchain 高度分散，但擴充性不高。更重要的是，由於所有東西都在全球公開的登記冊中，因此保密性有限。我們可以嘗試使用零知識技術 (Confidential Transactions、mimblewimble 方案等) 來提高機密性，但公有鏈無法隱藏交易圖形。


- 閃電/國家頻道**

與 Blockchain 相比，狀態通道 (如 Lightning Network)更具擴充性，也更隱密，因為交易是在 off-chain 進行的。然而，公開宣佈某些 Elements (資金交易、網路拓樸) 的義務以及網路流量的監控會部分損害機密性。分散性也會受到影響：路由是現金密集型的，主要節點可能成為集中點。這正是我們在 Lightning 上開始看到的現象。


- Client-side Validation (RGB)**

這種新的範例更具擴展性，也更機密，因為我們不僅可以整合零揭露的知識證明技術，而且沒有全局的交易圖表，因為沒有人持有整個登記冊。另一方面，這也意味著在去中心化上的某種妥協：Smart contract 的發行者可以扮演中心角色（就像 Ethereum 中的「Contract 部署者」）。然而，與 Blockchain 不同的是，使用 Client-side Validation，您只需儲存和驗證您感興趣的合約，這樣就避免了下載和驗證所有現有狀態的需要，從而提高了可擴展性。

![RGB-Bitcoin](assets/fr/004.webp)

#### 2.CAP 理論 (一致性、可用性、分割容錯)

CAP 理論強調，分散式系統不可能同時滿足一致性 (*一致性*)、可用性 (* 可用性*) 和分割容忍度 (* 分割容忍度*)。


- Blockchain**

Blockchain 偏重於一致性和可用性，但在網路分割方面做得不好：如果看不到區塊，就無法行動，也無法擁有與整個網路相同的視圖。


- 閃電** (法文)

狀態通道系統具有可用性和分割容錯性 (因為即使網路被分割，兩個節點仍能彼此保持連線)，但整體一致性則取決於 Blockchain 上通道的開啟和關閉。


- Client-side Validation (RGB)**

像 RGB 這樣的系統可提供一致性（每個參與者都在本地驗證其資料，不會含糊不清）和分割容錯性（您可自主保存資料），但無法保證全球可用性（每個人都必須確認自己擁有相關的歷史片段，有些參與者可能不會發佈任何內容或停止分享某些資訊）。

![RGB-Bitcoin](assets/fr/005.webp)

#### 3.CIA 三難點 (機密性、完整性、可用性)

這個三難題提醒我們，機密性、完整性和可用性無法同時獲得最佳化。Blockchain、Lightning 和 Client-side Validation 以不同的方式達到此平衡。我們的想法是，沒有任何單一系統可以提供所有功能；必須結合幾種方法 (Blockchain 的時間戳記、Lightning 的同步方法，以及 RGB 的本地驗證)，才能獲得一個連貫的套件，在每個層面上提供良好的保證。

![RGB-Bitcoin](assets/fr/006.webp)

### Blockchain 的作用和分片概念

Blockchain (在此為 Bitcoin)主要是作為_時間戳記_機制和防止雙重花費的保護機制。與其插入 Smart contract 或分散式系統的完整資料，我們只需將**加密承諾**（_commitments_）納入交易（在 Client-side Validation 的意義上，我們稱之為「狀態轉換」）。因此 ：


- 我們將 Blockchain 從大量的資料和邏輯中釋放出來；
- 每個使用者只儲存 Contract 中他自己的部分 (他的 "*Shard*")所需的歷史記錄，而不是複製 Global State。

Sharding 是一個起源於分散式資料庫的概念 (例如 MySQL 用於 Facebook 或 Twitter 等社交網路)。為了解決資料量和同步延遲的問題，資料庫被分割成_shards_（美國、歐洲、亞洲等）。每個區段都是本機一致的，並且只與其他區段部分同步。

對於 RGB 類型的智慧型契約，我們 Shard 依契約本身而定。每個 Contract 都是獨立的 _shard_。舉例來說，如果您只持有 USDT 代幣，您就不需要儲存或驗證另一種代幣（如 USDC）的整個歷史。在 Bitcoin 上，Blockchain 不做 _sharding_：您有一組全局的 UTXO。使用 Client-side Validation，每個參與者只保留其持有或使用的 Contract 資料。

因此，我們可以想像這個生態系統如下：


- Blockchain (Bitcoin)** 作為確保完整複製最小暫存器的基礎，並作為時間戳記 Layer；
- Lightning Network** 為快速、Confidential Transactions，仍基於 Bitcoin Blockchain 的安全性與最終結算；
- RGB 與 Client-side Validation** 可加入更複雜的 Smart contract 邏輯，而不會使 Blockchain 變得雜亂或失去保密性。

![RGB-Bitcoin](assets/fr/007.webp)

這三個 Elements 形成一個三角形的整體，而不是「Layer 2」、「Layer 3」等的線性堆疊。Lightning 可以直接連接到 Bitcoin，或與結合 RGB 資料的 Bitcoin 交易相關聯。同樣地，「BiFi」用途（Bitcoin 上的財務）可根據保密性、擴充性或 Contract 邏輯的需求，與 Blockchain、Lightning 及 RGB 組成。

![RGB-Bitcoin](assets/fr/008.webp)

### 狀態轉換的概念

在任何分散式系統中，驗證機制的目的是能夠**確定狀態變更的有效性和時間順序。其目的在於驗證通訊協定規則是否受到尊重，並證明這些狀態變更是以確定且不可篡改的順序相繼發生。

為了了解這種驗證在**Bitcoin**的情況下是如何運作的，更廣泛來說，為了掌握 Client-side Validation 背後的哲學，讓我們先回顧一下 Bitcoin Blockchain 的機制，然後再看看 Client-side Validation 與它們有什麼不同，以及它做了哪些優化。

![RGB-Bitcoin](assets/fr/009.webp)

就 Bitcoin Blockchain 而言，交易驗證是基於一個簡單的規則：


- 所有網路節點都會下載每個區塊和交易；
- 他們驗證這些交易，以驗證 UTXO 集 (所有未使用的輸出) 的正確演變；
- 它們會儲存這些資料 (以區塊的形式)，以便在必要時重播歷史。

![RGB-Bitcoin](assets/fr/010.webp)

然而，這種模式有兩大缺點：


- 可擴充性**：由於每個節點都必須處理、驗證和存檔每個人的交易，因此交易容量有明顯的限制，尤其是與最大區塊大小有關（Bitcoin 平均 10 分鐘 1 MB，不包括 cookies）；
- 隱私**：所有東西都是公開廣播和儲存的（金額、目的地址等），這限制了交換的機密性。

![RGB-Bitcoin](assets/fr/012.webp)

實際上，這個模式對於作為基礎 Layer (Layer 1) 的 Bitcoin 來說是可行的，但對於同時需要高交易吞吐量和一定保密性的更複雜用途來說，可能就不夠用了。

Client-side Validation 是基於相反的想法：與其要求整個網路驗證並儲存所有交易，不如讓每個參與者 (客戶端) 只驗證與自己有關的歷史部分：


- 當某人收到資產（或任何其他數位財產）時，他只需要知道並驗證導致該資產的作業鏈（狀態轉換），並證明其合法性；
- 這一系列的作業，從 ***Genesis***（初始發行）到最近的交易，形成一個無環有向圖 (DAG) 或 Shard，也就是整體歷史的一部分。

![RGB-Bitcoin](assets/fr/013.webp)

與此同時，為了讓網路的其他部分（或更精確地說，底層的 Layer，例如 Bitcoin）能夠鎖定最終狀態，而不會看到這些資料的細節，Client-side Validation 依賴於 ***Commitment*** 的概念。

*Commitment* 是加密 Commitment，通常是插入到 Bitcoin 交易中的 _hash_ (例如 SHA-256)，可證明已包含私人資料，但不會洩露這些資料。

感謝這些_承諾_，我們可以證明：


- 資訊的存在（因為資訊已存放於 Hash 中） ；
- 此資訊的前置性（因為它已在 Blockchain 中錨定並加上時間戳記，具有日期和區塊順序）。

不過，確切的內容不會透露，因此可維護其機密性。

具體來說，以下是 RGB State Transition 的工作原理：


- 您準備一個新的 State Transition（例如轉移一個 RGB 令牌）；
- 您 generate 加密 Commitment 到此轉換，並將其插入 Bitcoin 交易 (這些承諾在 RGB 通訊協定中稱為 「*錨*」)；
- 交易對手（接收方）擷取與此資產相關的客戶端歷史記錄，並驗證端對端的一致性，從 Smart contract 的 Genesis 到您傳送給它的轉換。

![RGB-Bitcoin](assets/fr/014.webp)

Client-side Validation 有兩大優點：


- 可擴充性：**

Blockchain 所包含的承諾 (*commitments*) 都很小 (約數十位元組)。這可確保區塊空間不會飽和，因為只需要包含 Hash。這也使得 off-chain 通訊協定得以演進，因為每個使用者只需儲存他或她的歷史片段 (他或她的 _stash_)。


- 隱私權 :**

交易本身（即其詳細內容）不會公佈為 On-Chain。只有它們的指紋 (*Hash*) 才會公開。因此，金額、位址和 Contract 邏輯仍然是隱私的，接收方可以在本機檢查所有先前的轉換，以驗證其 Shard 的有效性。除非發生爭議或需要證明，否則接收方沒有理由公開這些資料。

在 RGB 之類的系統中，來自不同合約（或不同資產）的多個狀態轉換可以透過單一_commitment_彙集到單一 Bitcoin 交易中。此機制可在 On-Chain 交易與 off-chain 資料 (客戶端驗證的轉換) 之間建立確定且有時間戳記的連結，並可讓多個分片同時記錄在單一 Anchor 點中，進一步降低 On-Chain 的成本與佔用空間。

實際上，當這個 Bitcoin 交易被驗證時，就永久「鎖定」了基礎契約的狀態，因為已經刻在 Blockchain 中的 Hash 就不可能再修改了。

![RGB-Bitcoin](assets/fr/015.webp)

### Stash 概念

**Stash**是參與者為了維護RGB Smart contract的完整性和歷史而必須絕對保留的一組客戶端資料。不像 Lightning 頻道，某些狀態可以在本機從共用資訊中重建，RGB Contract 的 Stash 不會複製到其他地方：如果您遺失了它，沒有人能夠還原給您，因為您要對自己的那份歷史負責。這就是您需要在 RGB 中採用具有可靠備份程序的系統的原因。

![RGB-Bitcoin](assets/fr/016.webp)

### Single-Use Seal：起源與運作

在接受貨幣等資產時，有兩項保證是必要的：


- 收到物品的真實性；
- 收到物品的唯一性，避免雙重支出。

對於實體資產，例如鈔票，實體的存在足以證明其未曾被複製。然而，在數位世界中，資產純粹是資訊性的，這種驗證方式就比較複雜，因為資訊很容易倍增和被複製。

正如我們前面所看到的，寄件者揭露狀態轉換的歷史，使我們能夠確保 RGB 令牌的真實性。透過存取 Genesis 交易之後的所有交易，我們可以確認代幣的真實性。這個原理類似於 Bitcoin，在 Bitcoin 中，硬幣的歷史可以追溯到原始的 Coinbase Transaction，以驗證其有效性。然而，與 Bitcoin 不同的是，RGB 的這種狀態轉換歷史是私有的，並保存在客戶端。

為了防止 RGB 令牌的 Double-spending，我們使用稱為「**Single-Use Seal**」的機制。此系統可確保每個代用幣使用一次後，無法以欺詐方式再次使用第二次。

一次性封印是由 Peter Todd 於 2016 年提出的加密基元，類似於實體封印的概念：一旦在容器上貼上 Seal，若不不可逆轉地破壞 Seal，就無法打開或修改容器。

![RGB-Bitcoin](assets/fr/018.webp)

將這種方法轉換到數位世界，就能證明一連串的事件確實發生過，而且不能再在事後更改。因此，單次使用封印超越了「Hash + Timestamp」的簡單邏輯，增加了一個 Seal 的概念，這個 Seal 只能關閉 ** 一次**。

![RGB-Bitcoin](assets/fr/017.webp)

為了讓單次使用封條發揮作用，您需要一個能夠證明出版物存在或不存在的出版物證明媒介，而且一旦資訊散布出去，就很難 (如果不是不可能) 偽造。例如，**Blockchain**（如 Bitcoin）可充當此角色，而一份公開發行的紙張報紙也可。構想如下：


- 我們想要證明某個關於訊息 `h(m)` 的 Commitment 已經發佈給觀眾，而沒有揭露訊息 `m` 的內容；
- 我們要證明沒有其他競爭性的 `h(m')` 訊息 Commitment 被發表來取代`h(m)`；
- 我們也希望能夠檢查訊息 `m` 是否在某個日期之前存在。

Blockchain 非常適合扮演這個角色：只要交易被包含在區塊中，整個網路就能對其存在與內容提供相同的不可偽造證明（至少部分而言，因為 _commitment_ 可以隱藏細節，同時證明訊息的真實性）。

因此，Single-Use Seal 可被視為一種正式的承諾，即只發布一次訊息 (在現階段仍是未知的)，且發布的方式可由所有相關方驗證。

不同於簡單的 _commitments_ (Hash) 或時間戳記 (可證明存在日期)，Single-Use Seal 提供了額外的保證，**沒有替代的 Commitment** 可以共存：您不能關閉相同的 Seal 兩次，或嘗試取代封存的訊息。

以下的比較有助於了解這個原則：


- 加密 Commitment (Hash)**：使用 Hash 函式，您可以透過公佈其 Hash 來承諾一段資料（一個數字）。在您揭露預先映像之前，該資料仍然是保密的，但您可以證明您事先知道該資料；
- Timestamp (Blockchain)**：透過在 Blockchain 中插入此 Hash，我們也證明我們在一個精確的時刻（即包含在區塊中）知道它；
- Single-Use Seal**：有了單次使用的封條，我們更進一步讓 Commitment 成為唯一。使用單一 Hash，您可以同時創造多個相互矛盾的承諾 (醫生向家人宣布「*是男孩*」，卻在個人日記中寫下「*是女孩*」的問題)。Single-Use Seal 透過將 Commitment 連結到一個公開證明媒介 (例如 Bitcoin Blockchain) 來消除這種可能性，因此花費 UTXO 就能確實封鎖 Commitment。一旦花費 UTXO，就無法再花費相同的 UTXO 來取代 Commitment。

| | 簡單的 Commitment (digest/Hash) | 時間戳 | 單次使用的封條 | | 簡單的 Commitment (digest/Hash) | 時間戳 | 單次使用的封條

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

| 發佈 Commitment 不會顯示訊息 | 是 | 是 | 是 | 是 | 是

| 證明 Commitment 日期/某日期前的訊息存在 | 不可能 | 有可能 | 有可能

| 證明不可能存在替代的 Commitment | 不可能 | 不可能 | 有可能 | 有可能 | 有可能

一次性使用密封件主要分三個階段運作：

**Seal Definition :**


- Alice 事先定義發佈 Seal 的規則 (何時、何地及如何發佈訊息)；
- Bob 接受或承認這些條件。

![RGB-Bitcoin](assets/fr/021.webp)

**Seal 關閉 :**


- 在執行時，Alice 會透過發佈實際訊息 (通常是 _commitment_ 的形式，例如 Hash)，來關閉 Seal；
- 它還能提供**見證**（加密證明），證明 Seal 是封閉且不可撤銷的。

![RGB-Bitcoin](assets/fr/019.webp)

**Seal 驗證 :**


- 一旦 Seal 關閉，Bob 就無法再打開：他只能檢查是否已經關閉；
- 鮑勃收集 Seal、**見證**和訊息（或他的 Commitment），以確保一切相符，且沒有競爭的封條或不同的版本。

此流程可概述如下：

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

然而，Client-side Validation 更進了一步：如果 Seal 本身的定義仍在 Blockchain 之外，那麼（理論上）有人就有可能挑戰相關 Seal 的存在性或合法性。為了克服這個問題，使用了一連串互鎖的單次使用封條：


- 每個封閉的 Seal 包含以下 Seal 的定義；
- 我們在 Blockchain (Bitcoin 交易中) 註冊這些關閉 (及其 _commitments_) ；
- 因此，任何修改先前 Seal 的嘗試都會與 Bitcoin 中蕴含的歷史相矛盾。

這正是 RGB 系統的功能：


- 已發佈的訊息是對用戶端已驗證資料的 _commitments_ (承諾)；
- Seal Definition 與 Bitcoin UTXO 相關聯；
- 當這個 UTXO 用完或有新的輸出記入同一個 Commitment 時，Seal 關閉；
- 花費這些 UTXO 的交易鏈對應於出版證明：RGB 上的每個轉換或狀態變更因此錨定在 Bitcoin。

總結一下：


- _密封定義_是您打算 UTXO Seal 未來的 Commitment；
- 當您花費這筆 UTXO 時，就會發生_seal closing_，產生包含 Commitment 的交易；
- _見證_是交易本身，它證明您已經用此內容結束 Seal；
- 您無法證明 Seal 未被關閉（您無法絕對確定 UTXO 未被花費或不會被花費在您尚未見過的區塊中），但您可以證明它確實已被關閉。

這種唯一性對 Client-side Validation 非常重要：當您驗證 State Transition 時，您要檢查它是否對應唯一的 UTXO，而不是之前在競爭的 Commitment 中使用過的。這就保證了 off-chain 智慧合約中沒有雙重花費。

### 多重承諾與根基

一個 RGB Smart contract 可能需要同時使用數個單次使用封條（數個 UTXO）。更重要的是，單一 Bitcoin 交易可能會引用數個不同的合約，每個合約都會封印自己的 State Transition。這需要一個 ** 多重 Commitment** 機制，以確定且唯一地證明沒有任何承諾是重複存在的。這就是 **Anchor** 的概念在 RGB 中發揮作用的地方：一個特殊的結構連結 Bitcoin 交易和一個或多個客戶端承諾 (狀態轉換)，每個都可能屬於不同的 Contract。我們會在下一章仔細研究這個概念。

![RGB-Bitcoin](assets/fr/023.webp)

該專案的兩個主要 GitHub 套件庫 (位於 LNPBP 組織之下) 將第一章所研究的這些概念的基本實作集中在一起：


- client_side_validation** ：包含用於本地驗證的 Rust 基元；
- single_use_seals**：執行邏輯來定義並安全地關閉這些封條。

![RGB-Bitcoin](assets/fr/020.webp)

請注意，這些軟體磚塊與 Bitcoin 無關；理論上，它們可應用於任何其他出版證明媒體 (其他註冊表、期刊等)。實際上，RGB 依賴 Bitcoin 的穩健性和廣泛共識。

![RGB-Bitcoin](assets/fr/021.webp)

### 來自公眾的問題

#### 邁向更廣泛使用一次性密封件

Peter Todd 也創造了_Open Timestamps_協定，而 Single-Use Seal 概念則是這些想法的自然延伸。除了 RGB 之外，我們還可預見其他的使用情況，例如在不使用 _merge mining_ 的情況下建構 _sidechains_ 或與 drivechain 相關的提案，例如 BIP300。任何需要單個 Commitment 的系統原則上都可以利用此加密原始碼。今天，RGB 是第一個主要的全面實作。

#### 資料可用性問題

由於在 Client-side Validation 中，每個使用者都會儲存自己的部分歷史記錄，因此無法在全球範圍內保證資料的可用性。如果 Contract 發行者隱藏或撤銷某些資訊，您可能不知道發售的實際演變情況。在某些情況下（如穩定幣），發行者應維護公開資料以證明流通量，但技術上沒有此義務。因此，有可能設計出故意不透明的合約，並擁有無限的 Supply，這就產生了信任的問題。

#### 分片與 Contract 隔離

每個 Contract 代表一個獨立的_shard_：例如，USDT 和 USDC 無需分享它們的歷史。原子交換仍是可能的，但這並不涉及合併它們的暫存器。所有的事情都由加密的 Commitment 來完成，而不會向每個參與者透露整個歷史圖形。

### 總結

我們已經看到 Client-side Validation 的概念與 Blockchain 和 _state channels_ 的契合點、它如何回應分散式運算的三難問題，以及它如何獨特地利用 Bitcoin Blockchain 來避免 Double-spending 和進行 * 時間戳記*。這個想法是基於**Single-Use Seal**的概念，讓您可以建立無法隨意再花費的獨特承諾。如此一來，每位參與者只上傳絕對必要的歷史記錄，增加智慧契約的擴充性與機密性，同時保留 Bitcoin 作為背景的安全性。

接下來，我們將詳細解釋如何在 Bitcoin 中應用此 Single-Use Seal 機制 (透過 UTXOs)、如何建立並驗證錨點，然後在 RGB 中建立完整的智慧型契約。我們會特別研究多重承諾的問題，也就是證明 Bitcoin 交易同時封鎖不同契約中的多個狀態轉換，而不會引入漏洞或雙重承諾的技術挑戰。

在深入瞭解第二章更多的技術細節之前，請隨時重讀關鍵定義 (Client-side Validation、Single-Use Seal、錨等)，並牢牢記住整體邏輯：我們希望調和 Bitcoin Blockchain 的優點 (安全性、分散性、時間戳記) 與 off-chain 解決方案的優點 (速度、保密性、可擴展性)，而這正是 RGB 與 Client-side Validation 所要達成的目標。

## Commitment Layer

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::

在本章中，我們將探討 Bitcoin Blockchain 內 Client-side Validation 和單次使用封裝的實作。我們將介紹 RGB 的 **Commitment Layer** （Layer 1）的主要原則，特別是**TxO2**方案，RGB 使用此方案來定義和關閉 Bitcoin 交易中的 Seal。接下來，我們將討論兩個尚未詳述的重要觀點：


- _deterministic Bitcoin 承諾_；
- 多協議承諾。

正是這些概念的結合，讓我們能夠在單一 UTXO 上疊加數個系統或合約，因此也能在單一 Blockchain 上疊加數個系統或合約。

應該記住的是，所描述的加密操作絕對可以應用於其他區塊鏈或出版媒體，但 Bitcoin 的特性（在去中心化、抵制審查和對所有人開放方面）使其成為開發進階可編程性（如 **RGB**所要求的）的理想基礎。

### Bitcoin 中的 Commitment 方案及其被 RGB 使用的情況

正如我們在課程第一章所看到的，單次使用封印是一個一般的概念：我們許諾在交易的特定位置包含一個 Commitment (_commitment_)，這個位置就像我們在訊息上關閉的 Seal。然而，在 Bitcoin Blockchain 上，有幾個選項可以選擇放置這個 _commitment_ 的位置。

為了了解這個邏輯，讓我們回想一下基本原則：為了關閉_單次使用的封印_，我們在指定的訊息上插入_commitment_來花費封印區域。在 Bitcoin 中，有多種方式可以做到這一點：


- 使用公開金鑰或 Address**

我們可以決定特定的公開金鑰或 Address 是_單次使用的封印_。只要這個金鑰或 Address 在交易中出現 On-Chain，就表示 Seal 以某個訊息結束。


- 使用 Bitcoin** 交易輸出

這表示一個 _ 單次使用的封印被定義為一個精確的 _outpoint_ （一個 txid + 輸出號碼對）。只要這個 _outpoint_ 用完，Seal 就會關閉。

在研發 RGB 時，我們發現至少有 4 種不同的方式可以在 Bitcoin 上實現這些封條：


- 透過公開金鑰定義 Seal，並在 _output_ ；
- 使用 _outpoint_ 定義 Seal 並使用 _output_ 關閉；
- 透過公開金鑰的值定義 Seal，並在 _input_ ；
- 透過_outpoint_定義 Seal，並在_input_中關閉。

| Schema 名稱 | Seal Definition | Seal 結束 | 額外要求 | 主要申請 | 可能的 Commitment 方案

| ----------- | ------------------------- | ------------------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------- |

| PkO | 公開金鑰值 | 交易輸出 | P2(W)PKH | 目前無 | Keytweak, taptweak, opret | P2(W)PKH | 目前無

| TxO2 | 交易輸出 | 交易輸出 | 需要 Bitcoin 上的確定承諾 | RGBv1 (通用) | Keytweak, tapret, opret | RGBv1 (通用)

| PkI | 公開金鑰值 | 交易輸入 | 僅限 Taproot 且與傳統錢包不相容 | 基於 Bitcoin 的身分 | Sigtweak、witweak | Taproot 與 Bitcoin 不相容。

| TxO1 | 交易輸出 | 交易輸入 | 僅限 Taproot 且與傳統錢包不相容 | 目前沒有 | Sigtweak, witweak | TxO1 | 交易輸出 | 交易輸入 | 僅限 Taproot 且與傳統錢包不相容 | 目前沒有

我們不會詳細說明每一種配置，因為在 RGB 中，我們選擇使用 ** 個 _outpoint_ 作為 Seal** 的定義，並將 _commitment_ 放在花費這個 _outpoint_ 的交易輸出中。因此，我們可以為後續引入以下概念：


- "Seal Definition"** ：一個指定的 _outpoint_ (以 txid + 輸出號碼來識別) ；
- 「Seal 結束 」**：花費此 _outpoint_ 的交易，其中一個 _commitment_ 被加入到訊息中。

選擇此方案是為了與 RGB 架構相容，但其他配置也可能適用於不同用途。

TxO2 「中的 」O2 "提醒我們，定義和結束都是基於交易輸出的支出（或建立）。

### TxO2 圖示範例

提醒一下，定義_單次使用的印章_不一定需要發佈 On-Chain 交易。舉例來說，Alice 已經有一個未使用的 UTXO 就夠了。她可以決定「這個 _outpoint_ (已經存在的) 現在是我的 Seal」。她在本地（_客戶端）記下這一點，直到這個 UTXO 用完，Seal 才會被視為開放。

![RGB-Bitcoin](assets/fr/024.webp)

在它想要關閉 Seal 的那一天（為了發出一個事件信號，或是為了 Anchor 一個特定的訊息），它會在一個新的交易中花費這個 UTXO（這個交易通常被稱為 "_witness transaction_"（與 _segwit_ 無關，只是我們給它的術語）。這個新的事務將包含對訊息的_commitment_。

![RGB-Bitcoin](assets/fr/025.webp)

請注意，在本範例中 ：


- 除了 Bob (或 Alice 選擇透露完整證明的對象) 之外，沒有人會知道這次交易中隱藏了某個訊息；
- 每個人都可以看到 _outpoint_ 已經被花費，但只有 Bob 持有證明，證明訊息實際上是錨定在交易中。

為了說明這個 TxO2 方案，我們可以使用_單次使用封印_作為撤銷 PGP 金鑰的機制。Alice 不需要在伺服器上公佈廢止憑證，而是可以說："This Bitcoin output, if spent, means that my PGP key is revoked"。

因此 Alice 擁有特定的 UTXO，特定的狀態或資料 (只有她自己知道) 在本機 (用戶端) 上與其相關聯。

Alice 通知 Bob 如果花掉這筆 UTXO，就會被視為發生了特定事件。從外面看，我們只看到 Bitcoin 的交易；但鮑勃知道這筆支出有隱藏的意義。

![RGB-Bitcoin](assets/fr/026.webp)

當 Alice 使用這個 UTXO 時，她會關閉訊息上的 Seal，表示她的新金鑰，或只是舊金鑰的廢止。如此一來，任何監控 On-Chain 的人都會看到 UTXO 已經用完，但只有擁有完整證明的人才會知道這正是 PGP 金鑰的撤銷。

![RGB-Bitcoin](assets/fr/027.webp)

為了讓 Bob 或其他相關人員檢查隱藏的訊息，Alice 必須提供他 off-chain 資訊。

![RGB-Bitcoin](assets/fr/028.webp)

因此 Alice 必須提供 Bob ：


- 訊息本身（例如，新的 PGP 金鑰） ；
- 該訊息涉及交易的加密證明 (稱為 _extra transaction proof_ 或 _anchor_)。

![RGB-Bitcoin](assets/fr/029.webp)

第三方沒有這些資訊。他們只會看到 UTXO 已經使用。因此保密性得到了保證。

為了釐清架構，讓我們將過程歸納為兩個交易：


- 交易 1**：這包含_seal 定義_，也就是將作為 Seal 的_outpoint_。

![RGB-Bitcoin](assets/fr/031.webp)


- 交易 2**：花費這個_outpoint_。這會關閉 Seal，並在同一個事務中，插入訊息上的 _commitment_ 。

![RGB-Bitcoin](assets/fr/033.webp)

因此，我們稱第二筆交易為「_見證交易」。

從另一個角度來說明，我們可以代表兩個層次：


- 頂端 Layer (Blockchain，公開)**：每個人都會看到交易，並知道已花費一個 _outpoint_ ；
- 較低的 Layer（客戶端，隱私）**：只有 Alice（或相關人員）透過加密證明和她在本機保留的訊息，知道這項支出對應於這樣那樣的訊息。

![RGB-Bitcoin](assets/fr/034.webp)

但在關閉 Seal 時，會產生一個問題，就是 _commitment_ 應該插入哪裡？

在上一節中，我們簡單提到 Client-side Validation 模型如何應用在 RGB 及其他系統。在這裡，我們要處理關於 ** 決定性 Bitcoin 承諾** 的部分，以及如何將它們整合到交易中。我們的想法是要了解為什麼我們要在_見證交易_中插入單一的 Commitment，最重要的是如何確保不會有其他未公開的競爭承諾。

### 交易中的 Commitment 位置

當你向某人證明某個訊息被嵌入到一個交易中時，你需要能夠保證在同一個交易中沒有另一種形式的 Commitment (第二個隱藏的訊息)，而這個訊息還沒有被揭露給你。為了讓 Client-side Validation 保持穩健，您需要一個 ** 決定性的 *** 機制，將單一的_commitment_放在關閉_單次使用封印_的交易中。

_witness transaction_ 花費了著名的 UTXO（或稱 _seal definition_），這項花費對應於 Seal 的關閉。從技術上來說，我們知道每個 outpoint 只能花費一次。這正是 Bitcoin 抵制雙重支出的基礎。但是花費交易可能有幾個_輸入_、幾個_輸出_，或是以複雜的方式組成（coinjoins、Lightning channels 等）。因此，我們需要清楚地定義在這個結構中插入 _commitment_ 的位置，而且要毫不含糊、統一。

無論使用何種方法 (PkO、TxO2 等)，都可以插入 _commitment_ ：


- 在輸入**中透過.NET 輸入：
    - Sigtweak** (修改 ECDSA 簽署的 `r` 元件，類似於「Sign-to-Contract」原則) ；
    - Witweak** (交易的 _segregated witness_ 資料被修改)。
- 在輸出**中透過 ：
    - Keytweak** (收件者的公開金鑰與訊息一起被「調整」) ；
    - Opret** (訊息會放置在非消耗性輸出 `OP_RETURN` 中) ；
    - Tapret** (或 _Taptweak_)，它依賴 Taproot 將 Commitment 插入 Taproot 金鑰的腳本部分，因此可以確定地修改公開金鑰。

![RGB-Bitcoin](assets/fr/035.webp)

以下是每種方法的詳細資訊：

![RGB-Bitcoin](assets/fr/038.webp)

*** 簽名調整 (簽名至 Contract) :***

早期的方案是利用簽章（ECDSA 或 Schnorr）的隨機部分來嵌入 _commitment：這就是所謂的「**Sign-to-Contract**」技術。您可以使用包含資料的 Hash 來取代隨機產生的 Nonce。如此一來，簽章就隱含揭示了您的 Commitment，而不需要在交易中增加任何額外的空間。這種方式有許多優點：


- 沒有 On-Chain 過載（您使用的地方與基本 Nonce 相同）；
- 理論上，這可以是相當離散的，因為 Nonce 最初是隨機基準。

不過，也出現了 2 個主要的缺點：


- Multisig 之前的 Taproot：當您有多位簽名者時，您需要決定由哪位簽名者來承擔 _commitment_。簽名可以有不同的順序，如果簽名者拒絕，您就會失去對 _commitment_ 結果的控制；
- MuSig 與共用 Nonce：使用 Schnorr Multisig (*MuSig*)，Nonce 的產生是一種多方演算法，要個別調整 Nonce 變得幾乎不可能。

實際上，**sig tweak** 與現有的硬體（硬體錢包）和格式（Lightning 等）也不太相容。因此，這個偉大的想法是 Hard 來實踐的。

***關鍵調整 (付費至 Contract) :***

** key tweak** 採用了_pay-to-contract_的歷史概念。我們使用公開金鑰 `X` 並加入值 `H(message)` 來調整它。具體來說，如果 `X = x * G` 和 `h = H(訊息)`，那麼新的金鑰就是 `X' = X + h * G`。這個經過調整的金鑰會隱藏 Commitment 到`訊息`。原始私密金鑰的持有者可以藉由在他的私密金鑰 `x` 中加入 `h` 來證明他有花費輸出的金鑰。理論上，這是很優雅的，因為：


- 輸入 _commitment_ 時，不需要新增任何欄位；
- 您不會儲存任何額外的 On-Chain 資料。

但實際上，我們會遇到以下困難：


- 由於標準公開金鑰已經過「調整」，錢包無法再辨識它，因此錢包無法輕鬆地將 UTXO 與您常用的金鑰聯繫起來；
- 硬體錢包並不是為了使用非源自其標準衍生的金鑰來簽章而設計的；
- 您需要調整您的腳本、描述符等。

在 RGB 的背景下，這條路線的構想一直到 2021 年為止，但事實證明這條路線太複雜，無法在目前的標準和基礎設施下運作。

*** 見證調整 :***

另一個想法，某些通訊協定，例如 _inscriptions Ordinals_ 已經付諸實行，就是直接將資料放在事務的「見證」部分 (因此有「見證調整」的說法)。然而，這種方法 ：


- 讓參與立即可見（您可以從字面上將原始資料貼到見證器中）；
- 可能會受到審查 (如果太大或任何其他任意特性，礦工或節點可能會拒絕中繼)；
- 佔用磚塊空間，有違 RGB 自由輕盈的宗旨。

此外，見證的設計在某些情況下是可剪枝的，這會讓穩健的證明變得更複雜。

*** 開啟-返回 (opret) :***

操作非常簡單，一個 `OP_RETURN`允許您在交易的特殊欄位中儲存一個 Hash 或訊息。但它會立即被偵測到：每個人都看見在交易中有一個_commitment_，而且它可以被刪除或丟棄，以及增加額外的輸出。由於這會增加透明度和大小，從 Client-side Validation 解決方案的觀點來看，它被認為是不太令人滿意的。

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

最後一個選項是使用 **Taproot**（BIP341 引進）與 *Tapret* 方案。 *Tapret* 是確定性 Commitment 的更複雜形式，在 Blockchain 的佔用空間和 Contract 作業的保密性方面帶來改善。主要的構想是將 Commitment 隱藏在 [Taproot 交易] (https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) 的「腳本路徑支出」部分。

![RGB-Bitcoin](assets/fr/036.webp)

在描述如何將 Commitment 插入 Taproot 交易之前，我們先來看看 Commitment 的**確切形式，它必須**臨時**對應於一個 64 位元組的字串 [建構](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196)，如下所示：

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- 29 個位元組 `OP_RESERVED`, 接著是 `OP_RETURN`, 然後是 `OP_PUSHBYTE_33`, 形成 31 個位元組 _prefix_ 部份；
- 接下來是 32 位元組的 _commitment_ (通常是來自 **MPC** 的 Merkle Root)，我們再加上 1 位元組的 **Nonce**（第二部分總共 33 位元組）。

因此，64 位元組的 `Tapret` 方法看起來像是一個 `Opret`，我們在其中加入了 29 位元組的 `OP_RESERVED` 前綴，並多加了一個位元組作為 Nonce。

為了在實作、機密性和擴充性方面保持彈性，Tapret 方案會根據需求考慮各種使用情況：


- 在沒有預先存在的 Script Path 結構下，將 Tapret Commitment 獨特地併入 Taproot 交易；
- 將 Tapret Commitment 整合到已配備 Script Path 的 Taproot 交易中。

讓我們仔細看看這兩種情況。

#### 無現有 Script 路徑的 Tapret 整合

在第一種情況下，我們從 Taproot 輸出金鑰 (*Taproot Output Key*) `Q` 開始，它只包含內部公開金鑰 `P` *(內部金鑰*)，沒有相關的腳本路徑 (*Script Path*) ：

![RGB-Bitcoin](assets/fr/047.webp)


- `P`：_Key Path Spend_ 的內部公開金鑰。
- `G`：橢圓曲線 [secp256k1](https://en.Bitcoin.it/wiki/Secp256k1) 的生成點。
- t = tH_TWEAK(P)` 是根據 [BIP86](https://github.com/Bitcoin/bips/blob/master/bip-0086.mediawiki#Address-derivation)，透過_標記切細值_ (例如 `SHA-256(SHA-256(TapTweak)||P)`)計算的切細因子。這證明沒有隱藏的腳本。

若要包含**Tapret** Commitment，請新增**腳本路徑花費**，並使用**獨特的腳本**，如下所示：

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)`之後會變成新的調整因子，包括 **Script_root**。
- `Script_root=tH_BRANCH(64-byte_Tapret_Commitment)`代表此 **script**的根，它只是一個類型為`SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`的 Hash。

Taproot 樹狀結構中的包含性和唯一性證明可歸結為單一的內部公開金鑰 `P`。

#### Tapret 整合至預先存在的 Script Path

第二種情況是關於更複雜的 `Q` Taproot** 輸出，其中已包含數個腳本。例如，我們有一棵由 3 個腳本組成的樹：

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` 指定葉腳本的歸一化標籤 Hash 函數。
- a, B, C ` 代表已包含在 Taproot 結構中的腳本。

若要新增 Tapret Commitment，我們需要在樹狀結構的第一層插入一個 * 不可消耗的腳本*，將現有的腳本下移一層。從視覺上來看，樹會變成 .NET：

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC ` 代表頂層群組 `A, B, C` 的標記 Hash。
- tHT` 代表與 64 位元組 `Tapret` 對應的腳本 Hash。

根據 Taproot 規則，每個分支/葉必須依照 Hash 的詞彙順序來組合。有兩種可能的情況：


- `tHT` > `tHABC`: Tapret Commitment 移到樹的右邊。唯一性證明只需要 `tHABC` 和 `P` ；
- tHT` < `tHABC`**: Tapret Commitment 放在左邊。為了證明右邊沒有其他的 Tapret Commitment，必須揭示 `tHAB` 和 `tHC` 以證明沒有其他這樣的文字。

第一種情況 (`tHABC < tHT`) 的視覺範例：

![RGB-Bitcoin](assets/fr/051.webp)

第二種情況的範例 (`tHABC>tHT`)：

![RGB-Bitcoin](assets/fr/052.webp)

#### 使用 Nonce 進行最佳化

為了提高機密性，我們可以「挖掘」（更準確的說法是「暴力破解」）`<Nonce>`（64 位元組 `Tapret` 的最後一個位元組）的值，嘗試取得 Hash `tHT`，使得 `tHABC < tHT`。在這種情況下，Commitment 會被放在右邊，使用者就不必洩露現有腳本的全部內容來證明 Tapret 的唯一性。

總而言之，「Tapret」提供了一種離散和確定的方式，將 Commitment 納入 Taproot 交易，同時尊重 RGB 的 Client-side Validation 和 Single-Use Seal 邏輯所必須的唯一性和明確性要求。

#### 有效出口

對於 RGB Commitment 交易，有效 Bitcoin Commitment 方案的主要要求如下：交易 (*Witness Transaction*) 必須可證明包含單一 Commitment。這項要求使得在同一個交易中，無法為用戶端已驗證的資料建構另一個歷史。這表示_單次使用封條_關閉的訊息是唯一的。

為了滿足這個原則，不論交易中有多少個輸出，我們都要求**只有一個輸出**可以包含 Commitment (*Commitment*)。對於每個使用的方案 (*Opret* 或 *Tapret*)，唯一可以包含 RGB _commitment_ 的有效輸出是 ：


- *Opret* 方案的第一個輸出 `OP_RETURN`（如果存在）；
- *Tapret* 方案的第一個 Taproot 輸出（如果存在）。

請注意，一個交易很有可能在兩個不同的輸出中包含單一的「Opret」 Commitment 和單一的「Tapret」 Commitment。由於 Seal Definition 的確定性質，這兩個承諾對應於客戶端驗證的兩個不同的資料。

### RGB 的分析與實際選擇

當我們開始 RGB 時，我們檢閱了所有這些方法，以確定在何處以及如何以確定的方式在交易中放置 _commitment_。我們定義了一些標準：


- 相容於不同的使用情境 (例如 Multisig、Lightning、硬體錢包等)；
- 對 On-Chain 空間的影響 ；
- 實施和維護的難度 ；
- 保密和抵制審查。

| 方法 | On-Chain 追蹤與大小 | 客戶端大小 | Wallet 整合 | 硬體相容性 | Lightning 相容性 | Taproot 相容性

| -------------------------------------------------- | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |

| Keytweak (deterministic P2C) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 Bolt, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig |

| Sigtweak (deterministic S2C) | 🟢 | 🟢 | 🟠 | 🔴 | 🔴 Bolt, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig | 🟠 | 🟠 Taproot, 🔴 MuSig | 🟠

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 Bolt， 🟠 Bifrost | - |

| Tapret 演算法：左上方節點 | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 Bolt、🟢 Bifrost | 🟢 Taproot、🟢 MuSig |

| Tapret 演算法 #4：任何節點 + 證明 | 🟢 | 🟠 | 🟠 | 🟢 | 🔴 Bolt、🟢 Bifrost | 🟢 Taproot、🟢 MuSig |

確定性 Commitment 方案 | 標準 | On-Chain 成本 | 客戶端的證書大小 | On-Chain 成本 | 客戶端的證書大小 | On-Chain 成本 | 客戶端的證書大小 | Commitment 方案

| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |

| 密鑰調整 (Deterministic P2C) | LNPBP-1, 2 | 0 位元組 | 33 位元組 (未調整的密鑰) | | LNPBP-1, 2 | 0 位元組 (未調整的密鑰)

| Sigtweak (Deterministic S2C) | WIP (LNPBP-39) | 0 位元組 | 0 位元組 | 0 位元組

| Opret (OP_RETURN) | - | 36 (v)bytes (additional TxOut) | 0 bytes |

| Tapret 演算法：左上方節點 | LNPBP-6 | 任何 n-of-m Multisig 的見證中有 32 位元組 (8 vbytes) 並透過腳本路徑支出 | 無腳本的腳本上有 0 位元組 Taproot ~270 位元組在單一腳本的情況下， ~128 位元組在多腳本的情況下 | Tapret 演算法：左上方節點 | LNPBP-6 | 見證中有 32 位元組 (8 vbytes) 並透過腳本路徑支出

| Tapret 演算法 #4：任何節點 + 唯一性證明 | LNPBP-6 | 32 位元組的見證位元組 (8 vbytes) 適用於單一腳本的情況，其他大多數情況的見證位元組為 0 位元組 | 0 位元組適用於無腳本的腳本 Taproot，65 位元組直到 Taptree 包含一打腳本為止 | | Tapret 演算法 #5：任意節點 + 唯一性證明

| Layer | On-Chain 成本 (位元組/位元組) | On-Chain 成本 (位元組/位元組) | On-Chain 成本 (位元組/位元組) | On-Chain 成本 (位元組/位元組) | 客戶端成本 (位元組) | 客戶端成本 (位元組) | 客戶端成本 (位元組) | 客戶端成本 (位元組) | 客戶端成本 (位元組) | 客戶端成本 (位元組)

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Type** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret**

| Single-sig | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | 0?                       | 0 |

| MuSig (n-of-n) | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | ?> 0 | 0 |

| multi-sig 2-of-3 | 32/8 | 32/8 或 0 | 0 | n/a | 32 | ~270 | 65 | 32 | n/a | 0 |

| multi-sig 3-of-5 | 32/8 | 32/8 or 0 | 0 | n/a | 32 | ~340 | 65 | 32 | n/a | 0 |

| multi-sig 2-of-3，超時 | 32/8 | 0 | 0 | n/a | 32 | 64 | 65 | 32 | n/a | 0 |

| Layer | On-Chain 成本 (vbytes) | On-Chain 成本 (vbytes) | On-Chain 成本 (vbytes) | 客戶端成本 (位元組) | 客戶端成本 (位元組) | 客戶端成本 (位元組)

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **類型** | **基礎** | **塔佩特 #2** | **塔佩特 #4** | **塔佩特 #2** | **塔佩特 #4** | **塔佩特 #2** | **塔佩特 #4**

| MuSig (n-of-n) | 16.5 | 0 | 0 | 0 | 0 | 0 |

| FROST (n-of-m) | ?                      | 0 | 0 | 0 | 0 |

| Multi_a (n-of-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 |

| 分支 MuSig / Multi_a (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| 有逾時 (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| 方法 | 隱私性和可擴展性 | 互操作性 | 兼容性 | 可攜性 | 複雜性 | 複雜性

| ----------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |

Keytweak (Deterministic P2C) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡

| Sigtweak (Deterministic S2C)

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 | 🟢

| Algo Tapret：左上方節點

| Algo Tapret #4：任何節點 + 證明 | | 🟢 | 🟢 | 🟠 | 🔴 | 🔴

在研究過程中，我們發現沒有一個 Commitment 方案與目前的 Lightning 標準完全相容（Lightning 標準沒有採用 Taproot、_muSig2_ 或額外的 _commitment_ 支援）。我們正在努力修改 Lightning 的通道結構 (*BiFrost*)，以允許插入 RGB 承諾。這是我們需要重新檢視交易結構、金鑰以及通道更新簽署方式的另一個領域。

分析結果顯示，事實上，其他方法（key tweak、sig tweak、witness tweak 等）也呈現其他形式的複雜性：


- 要麼我們的 On-Chain 體積很大；
- 要麼就是與現有的 Wallet 程式碼完全不相容；
- 在非合作的 Multisig 中，要麼解決方案不可行。

對於 RGB，有兩種方法特別突出： ***Opret***和***Tapret***，兩者都歸類為 「交易輸出」，並與通訊協定使用的 TxO2 模式相容。

### 多重通訊協定承諾 - MPC

在本節中，我們將探討 **RGB**如何透過確定性方案（根據「Opret」或「Tapret」），在單一 Bitcoin 交易中記錄的 Commitment (*Commitment*) 內處理多個合約（或更精確地說，它們的_transition bundles_）的聚合。為了達到這個目的，各種契約的 Merkelization 排序是在稱為 **MPC Tree** (_Multi Protocol Commitment Tree_) 的結構中進行。在本節中，我們將探討此 MPC Tree 的結構、如何取得其根，以及多個契約如何可以保密且毫不含糊地分享相同的交易。

Multi Protocol Commitment (MPC) 旨在滿足兩種需求：


- 構建 `mpc::Commitment` Hash：這將根據 `Opret` 或 `Tapret` 方案包含在 Bitcoin Blockchain 中，並且必須反映所有要驗證的狀態變更；
- 在單一 _commitment_ 中同時儲存多個合約，可在單一 Bitcoin 交易中管理多個資產或 RGB 合約的獨立更新。

具體來說，每一個_transition bundle_屬於一個特定的 Contract。所有這些資訊都會被插入一棵 **MPC Tree**，其根 (`mPC::Root`)再經過哈希處理，得到`mPC::Commitment`。根據所選擇的確定方法，正是這最後的 Hash 被放置在 Bitcoin 交易（_見證交易_）中。

![RGB-Bitcoin](assets/fr/042.webp)

#### MPC Root Hash

實際寫入 On-Chain 的值（在 `Opret` 或 `Tapret` 中）稱為 `mPC::Commitment`。其計算方式為 [BIP-341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki)，公式為 ：

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

其中 ：


- `mpc_tag` 是一個標籤：`urn:ubideco:mpc:Commitment#2024-01-31`，根據 [RGB 標籤慣例] (https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments.md) 選擇；
- `depth` (1 位元組) 表示 *MPC Tree* 的深度；
- cofactor`（16 位元，以 Little Endian 表示）是一個參數，用來提升分配給樹狀結構中每個 Contract 的位置的唯一性；
- `mpc::Root` 是 *MPC Tree* 的根，根據下一節所述的程序計算。

![RGB-Bitcoin](assets/fr/044.webp)

#### MPC 樹木建設

要建立此 MPC Tree，我們需要確保每個 Contract 對應到唯一的葉子位置。假設我們有 ：


- c` 個要包含的合約，在 `i = {0,1,...,C-1}` 中以 `i` 為索引；
- 對於每個 Contract `c_i`，我們都有一個識別碼 `ContractId(i) = c_i`。

然後，我們建構一棵寬度為 `w` 且深度為 `d` 的樹，使得 `2^d = w`，且 `w > C`，如此一來，每個 Contract 都可以被放置在單獨的 _leaf_ 中。每個 Contract 在樹中的位置 `pos(c_i)` 由 ：

```txt
pos(c_i) = c_i mod (w - cofactor)
```

其中 `cofactor`為一整數，可增加每個 Contract 獲得不同位置的機率。實際上，建構過程會依循反覆的過程：


- 我們從最小深度 (`d=3`，以隱藏確切的合約數) 開始；
- 我們嘗試不同的 `cofactors`（最多 `w/2`，或基於效能考量最多 500）；
- 如果我們無法在沒有碰撞的情況下定位所有契約，我們會遞增 `d` 並重新開始。

目的是避開太高的樹，同時將碰撞風險降到最低。請注意，碰撞現象遵循隨機分布邏輯，與 [Anniversary Paradox](https://en.wikipedia.org/wiki/Birthday_problem) 相關聯。

#### 有人居住的樹葉

一旦為契約 `i = {0,1,...,C-1}`取得 `C` 個不同的位置 `pos(c_i)` 後，每張工作表就會填入一個 Hash 函數 (* 標記為 Hash*)：

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

其中 ：


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`，總是根據 RGB 的 Merkle 慣例來選擇；
- `0x10` 識別 _contract leaf_ ；
- `c_i` 是 32 位元組的 Contract 識別碼 (源自 Genesis Hash)；
- bundleId(c_i)` 是一個 32 位元組的 Hash，描述與 `c_i` 相對應的「狀態轉換」集 (集合成 *Transition Bundle*)。

#### 無人居住的樹葉

其餘未指派給 Contract 的葉子 (即 `w - C` 葉子) 會填入「假」值 (_entropy leaf_) ：

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

其中 ：


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`，總是根據 RGB 的 Merkle 慣例來選擇；
- `0x11` 表示_熵葉_ ；
- `entropy` 是一個 64 位元組的隨機值，由建立樹的人選取；
- `j` 是這片樹葉在樹中的位置 (32 位元 Little Endian)。

#### MPC 節點

在產生 `w` 葉子 (無論是否有人居住) 之後，我們開始進行 merkelization。任何內部節點的散列方式如下：

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

其中 ：


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`，總是根據 RGB 的 Merkle 慣例來選擇；
- b` 是_分支因子_ (8 位元)。最常見的情況是 `b=0x02` 因為樹是二進位且完整的；
- d` 是節點在樹中的深度；
- `w` 是樹寬度 (256 位元 Little Endian 二進位)；
- tH1` 和 `tH2` 是子節點 (或葉) 的哈希值，已如上所示計算出來。

依此類推，我們得到根 `mPC::Root`。然後，我們可以計算 `mpc::Commitment` (如上文解釋)，並插入 On-Chain。

為了說明這一點，讓我們想像一個 `C=3` (三個合約) 的例子。它們的位置假設為：`pos(c_0)=7`、`pos(c_1)=4`、`pos(c_2)=2`。其他的葉子 (位置 0, 1, 3, 5, 6) 是_熵葉_。下圖顯示以 ：


- 表示 `BundleId(c_i)` 的 `BUNDLE_i` ；
- `tH_MPC_LEAF(A)`等等，代表葉子（有些代表契約，有些代表熵） ；
- 每個分支 `tH_MPC_BRANCH(...)` 結合了兩個子分支的哈希值。

最後的結果是 **mPC::Root**，然後是 `mPC::Commitment`。

![RGB-Bitcoin](assets/fr/053.webp)

#### MPC 軸檢查

當驗證者想要確保 `c_i` Contract (和它的 `BundleId`) 包含在最後的 `mpc::Commitment` 中時，他只需要收到一個 Merkle 證明。這個證明指出追蹤葉子 (在這個例子中，是 `c_i` 的 _contract leaf_)回到根所需的節點。不需要公開整個 *MPC Tree*：這樣可以保護其他契約的機密性。

在範例中，`c_2`驗證器只需要一個中間 Hash (`tH_MPC_LEAF(D)`)、兩個`tH_MPC_BRANCH(...)`、`pos(c_2)`位置證明和`cofactor`值。然後，它可以在本機重建根，再重新計算 `mpc::Commitment` 並與寫入 Bitcoin 交易 (在 `Opret` 或 `Tapret` 內) 的 `mpc::Commitment` 比較。

![RGB-Bitcoin](assets/fr/054.webp)

此機制可確保 ：


- 相對於 `c_2` 的狀態確實包含在彙總資訊區塊中（用戶端）；
- 由於 On-Chain _commitment 指向單一 MPC 根，因此沒有人能以相同的交易建立另一個歷史。

#### MPC 結構概要

Multi Protocol Commitment* (MPC) 是使 RGB 將多個合約彙集到單一 Bitcoin 交易中的原則，同時保持承諾的唯一性和對其他參與者的保密性。由於樹狀結構的確定性，每個 Contract 都被分配到一個唯一的位置，而「假」葉 (*Entropy Leaves*) 的存在部分掩蓋了參與交易的合約總數。

整個 Merkle Tree 永遠不會儲存在客戶端。我們只需為每個相關的 Contract 設定一個 _Merkle path_ generate，並傳送給接收者（接收者可隨後驗證 Commitment）。在某些情況下，您可能有數個資產已通過相同的 UTXO。您可以將幾個 _Merkle paths_ 合併為一個所謂的 _multi-protocol Commitment block_，以避免重複太多資料。

因此，每個 _Merkle proof_ 都是輕量級的，尤其是在 RGB 中，樹的深度不會超過 32。還有一個「Merkle 區塊」的概念，它保留了更多的資訊 (截面、熵等)，對於結合或分離幾個分支很有用。

這就是為什麼花了這麼長的時間才敲定 RGB。我們從 2019 年開始就有了整體願景：將所有東西都放在用戶端，流通代幣 off-chain。但對於細節，如多個合約的分片、Merkle Tree 的結構、如何處理碰撞和合併證明......這些都需要反覆斟酌。

### 錨點：全球集合

繼承承諾 (「Opret」或「Tapret」) 和 MPC (*Multi Protocol Commitment*) 的建構，我們需要在 RGB 協定中 Address **Anchor** 的概念。Anchor 是客戶端驗證的結構，它匯集了驗證 Bitcoin Commitment 實際包含特定合約資訊所需的 Elements 。換句話說，Anchor 總結了驗證上述_承諾_所需的所有資料。

Anchor 包含三個有序欄位：


- txid
- MPC 證明
- 額外交易證明 - ETP

這些欄位中的每一個都在驗證過程中扮演一定的角色，無論是重建底層的 Bitcoin 交易，或是證明隱藏的 Commitment 的存在 (尤其是在 `Tapret` 的情況下)。

#### txid

txid」欄位對應於包含「Opret」或「Tapret」Commitment 的 Bitcoin 交易的 32 位元組識別碼。

理論上，可以依循單次使用封裝的邏輯，追蹤指向每個 Witness Transaction 的狀態轉換鏈來找到這個 `txid`。然而，為了方便並加速驗證，這個 `txid` 會被簡單地包含在 Anchor 中，因此驗證者不必回溯整個 off-chain 歷史。

#### MPC 證明

第二個欄位 `MPC Proof` 是指這個特定 Contract (例如 `c_i`)包含在 _Multi Protocol Commitment_ 中的證明。它是 ：


- pos_i"，此 Contract 在 MPC 樹中的位置；
- cofactor`, 定義用於解決位置碰撞的值；
- Merkle Proof「，即用於重建 MPC 根並驗證 Contract 識別碼及其 」Transition Bundle "已承諾到根的節點和哈希值集。

此機制已在上一節關於建立 *MPC Tree* 的內容中說明，其中每個 Contract 都會因 .NET Framework 而獲得一個唯一的樹葉：

```txt
pos(c_i) = c_i mod (w - cofactor)
```

然後，使用一個確定性的 merkelization 方案來聚合所有的葉子 (契約 + 熵)。最後，「MPC Proof」允許在本地重建根，並與包含 On-Chain 的「mPC::Commitment」進行比較。

#### 額外交易證明 - ETP

第三個欄位，即 **ETP** 取決於所使用的 Commitment 類型。如果 Commitment 的類型是 `Opret`，就不需要額外的證明。驗證器會檢查交易的第一個 `OP_RETURN` 輸出，並直接在那裡找到 `mPC::Commitment`。

**如果 Commitment 屬於「Tapret」類型**，則必須提供稱為 *Extra Transaction Proof - ETP* 的額外證明。它包含 ：


- 嵌入 *Commitment* 的 Taproot 輸出的內部公開金鑰 (`P`)；
- 腳本路徑花費」的夥伴節點 (當 Tapret *Commitment* 插入腳本時)，以證明此腳本在 Taproot 樹中的確切位置：
 - 如果 `Tapret` *Commitment* 在右側分支上，我們會揭示左側節點 (例如 `tHABC`)、
 - 如果 `Tapret` *Commitment* 在左側，您需要公開 2 個節點 (例如 `tHAB` 和 `tHC`)，以證明右側沒有其他 *Commitment* 存在。
- `Nonce` 可用來「挖掘」最佳配置，讓 *Commitment* 置於樹的右側 (證明最佳化)。

這個額外的證明是必要的，因為與`Opret`不同，`Tapret` Commitment是整合在Taproot腳本的結構中，這需要揭露Taproot樹的一部分，才能正確地驗證*Commitment*的位置。

![RGB-Bitcoin](assets/fr/045.webp)

因此，**錨**封裝了在 RGB 的情況下驗證 Bitcoin Commitment 所需的所有資訊。它們同時指出相關的交易 (`txid`)，以及 Contract 定位的證明 (`MPC證明`)，同時在`Tapret`的情況下管理額外的證明 (`ETP`)。如此一來，Anchor 可保護 off-chain 狀態的完整性和唯一性，確保相同的交易無法被重新詮釋為其他契約資料。

### 總結

在本章中，我們將介紹 ：


- 如何在 Bitcoin 中應用單次使用 Seals 概念 (特別是透過_outpoint_)；
- 將 _commitment_ 確定插入交易的各種方法 (Sig tweak、Key tweak、witness tweak、OP_RETURN、Taproot/Tapret) ；
- RGB 專注於 Tapret 承諾的原因 ；
- 透過 _multi-protocol commitments_ 進行多重 Contract 管理，如果您不想在想要證明特定觀點時揭露整個狀態或其他契約，此功能是不可或缺的；
- 我們也看到 _Anchors_ 的作用，它將所有東西 (交易 txid、Merkle Tree 證明和 Taproot 證明) 整合在單一套件中。

實際上，技術實作分為幾個專用的 Rust _crates_（在 _client_side_validation_、_commit-verify_、_bp_core_ 等）。基本概念是存在的：

![RGB-Bitcoin](assets/fr/046.webp)

在下一章，我們將探討 RGB 純粹的 off-chain 元件，也就是 Contract 邏輯。我們會看到 RGB 契約如何以部分複製_無限狀態機_的方式組織，達到比 Bitcoin scripts 更高的表達能力，同時又能保持資料的機密性。

## 智慧型契約及其狀態簡介

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::

在本章與下一章中，我們將探討 RGB 環境中的 ***Smart contract** 概念，並探討這些契約定義與演進其 *state* 的不同方式。我們會了解為什麼 RGB 架構使用單次使用 Seals 的有序順序，能以可擴充的方式執行各種類型的 ***Contract 作業***，而且不需要經過集中式的註冊中心。我們也將探討***Business Logic***在構成 Contract State 演進過程中的基本角色。

### 智慧契約與數位不記名權利

RGB 的目的是提供在 Bitcoin 上執行智慧合約的基礎架構。我們所說的「Smart contract」是指數位當事人之間的協議，此協議可自動以計算方式執行，不需要人為介入來強制執行條款。換句話說，Contract 的法律是由軟體執行，而非由可信賴的第三方執行。

這種自動化提出了分散化的問題：我們如何才能擺脫集中化的登記處 (例如中央平台或資料庫) 來管理 Ownership 和 Contract 的效能？RGB 所接手的原始想法，是回到 Ownership 所謂的「不記名證券」模式。歷史上，某些證券 (債券、股票等) 是以不記名形式發行，讓任何實際持有該文件的人都能強制執行其權利。

![RGB-Bitcoin](assets/fr/055.webp)

RGB 將這個概念應用於數位世界：權利 (和義務) 被封裝在可操作的 off-chain 資料中，而這些資料的狀態則由參與者自己驗證。相較於其他以公開登記冊為基礎的方法，此舉先驗地允許更大程度的保密性與獨立性。

### Smart contract RGB 狀態簡介

RGB 中的 Smart contract 可視為狀態機，由 ：


- 一個 **狀態**，即反映 Contract 目前組態的資訊集；
- 一個 **Business Logic**（一組規則），說明在什麼條件下以及由誰修改狀態。

![RGB-Bitcoin](assets/fr/056.webp)

重要的是要了解這些合約不只限於代幣的簡單轉讓。它們可以體現各式各樣的應用：從傳統資產（代幣、股票、債券）到更複雜的機制（使用權、商業條款等）。與其他區塊鏈不同的是，Contract 的程式碼是所有人都可以存取和執行的，RGB 的方法將 Contract 的存取和知識區分給參與者 (「***Contract 參與者***」)。有幾種角色：


- Contract 的發行者**或建立者，他定義了 Contract 的 Genesis 及其初始變數；
- 有權** (*Ownership*) 或其他執行能力的當事人 ；
- 觀察員**，可能只限於看到某些資訊，但不能觸發修改。

這種角色分離確保只有授權人員才能與契約狀態互動，有助於抵抗審查。這也讓 RGB 具備橫向擴充的能力：大部分的驗證都在 Blockchain 外部進行，只有加密錨點 (*承諾*) 會刻在 Bitcoin 上。

### 狀態和 RGB 中的 Business Logic

從實際角度來看，Contract 的 **Business Logic** 採用規則和腳本的形式，定義在 RGB 所謂的 **Schema** 中。Schema 對 .NET 編碼：


- 國家結構（哪些欄位是公用的？哪些欄位屬於哪些方？
- 有效性條件（在授權進行狀態更新之前必須檢查什麼？
- 授權（誰可以啟動 *State Transition*？ 誰只能觀察？）

同時，**Contract State** 通常會分解成兩個元件：


- A **Global State**：公共部分，所有人都有可能觀察到（取決於組態）；
- Owned States**：私人部分，透過 Contract 邏輯中參考的 UTXOs 專門分配給擁有者。

正如我們在接下來的章節所看到的，任何狀態更新 (*Contract Operation*) 都必須對接 Bitcoin _commitment_ (透過 `Opret` 或 `Tapret`) 並遵守 *Business Logic* 腳本，才能被視為有效。

### Contract 作業：國家的建立與演變

在 RGB 範圍內，***Contract Operation*** 是將 Contract 從 ** 舊狀態** 變更為 ** 新狀態** 的任何事件。這些作業遵循下列邏輯：


- 我們注意到 Contract 的現況；
- 我們套用規則或操作（一個 ***State Transition***、一個 ***Genesis***，如果是最開始的狀態，或是一個 ***State Extension***，如果有一個公開的 *Valency* 要重新觸發）；
- 我們透過 Blockchain 上的新_commitment_來進行 Anchor 的修改，關閉一個_單用封印_並建立另一個 ；
- 相關權利人在本機 (* 客戶端*) 驗證轉換符合 *Schema*，且相關的 Bitcoin 交易已註冊 On-Chain。

![RGB-Bitcoin](assets/fr/057.webp)

最終的結果是更新的 Contract，現在有了不同的狀態。這個轉換不需要整個 Bitcoin 網路關心細節，因為 Blockchain 中只記錄了一個小小的加密指紋 (_commitment_)。單次使用 Seals 的順序可防止任何 Double-spending 或雙重使用狀態。

### 營運鏈：從 Genesis 到終端狀態

為了說明這一點，一個 RGB Smart contract 以 **Genesis** 開始，也就是第一個狀態。此後，各種 Contract 作業相繼出現，形成一個 DAG (*Directed Acyclic Graph*) 作業：


- 每個轉換都是基於先前的一個狀態（或幾個，在收斂轉換的情況下）；
- 由於 Bitcoin Anchor 的共識，每個轉換都有時間戳記，且不可更改，因此保證了時間順序；
- 當沒有更多的作業正在進行時，就會達到**終點狀態**：Contract 最近的完整狀態。

![RGB-Bitcoin](assets/fr/012.webp)

這種 DAG 拓樸結構 (而非簡單的線性鏈) 反映出 Contract 的不同部分只要不互相矛盾，就有可能並行演進。RGB 接著會透過 * 客戶端 * 驗證所涉及的每個參與者，來注意避免任何不一致的情況。

### 摘要

RGB 中的智慧契約引進了數位不記名票據的模式，雖然是分散式的，但錨定在 Bitcoin 中，用於時間戳記和保證交易順序。這些合約的自動執行是基於.NET技術：


- A **Contract State*，表示 Contract 目前的組態（權限、餘額、變數等）；
- A **Business Logic** (*Schema*)，定義哪些轉換是允許的，以及必須如何驗證；
- Contract 作業**，透過錨定在 Bitcoin 交易中的承諾，逐步更新此狀態。

在下一章中，我們將詳細介紹這些***狀態***和***狀態轉換***在 off-chain 層級的具體表示，以及它們與嵌入在 Bitcoin 中的 UTXOs 和 Single-use Seals 的關係。這將是一個機會，讓我們看看 RGB 以 Client-side Validation 為基礎的內部機制，如何在維護資料機密性的同時，維持智慧型契約的一致性。

## RGB Contract 作業

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::

在本章中，我們將再次在 RGB 協定中瞭解智慧契約中的操作和狀態轉換是如何運作的。目的也是要了解多位參與者如何合作轉移資產的 Ownership。

### 狀態轉換及其機制

一般原則仍與 Client-side Validation 相同，狀態資料由所有者持有，並由接收者驗證。然而，RGB 在此的特殊性在於 Bob 身為接收者，會要求 Alice 將某些資訊納入 Contract 資料中，以便透過隱藏參照他的一個 UTXO 來真正控制所接收的資產。

為了說明 *State Transition*（這是 RGB 中基本的 ***Contract 操作***之一）的過程，讓我們以 Alice 和 Bob 之間的資產轉移為例，逐步說明：

**最初情況：**

Alice 有一個 ***Stash RGB*** 本地端驗證的資料 (* 客戶端*)。這個 Stash 指的是她在 Bitcoin 上的一個 UTXO。這表示此資料中的_seal definition_會指向屬於 Alice 的 UTXO。這個想法是要讓她能夠將與資產 (例如 RGB 代幣) 相關聯的某些數位權利轉移給 Bob。

![RGB-Bitcoin](assets/fr/058.webp)

**Bob 也有 UTXOs :**

另一方面，Bob 至少有一個自己的 UTXO，與 Alice 的 UTXO 沒有直接連結。在 Bob 沒有 UTXO 的情況下，仍然可以使用 *Witness Transaction* 本身來向他進行轉移：這個交易的輸出就會包含 Commitment (_commitment_)，並隱含地將新 Contract 的 Ownership 與 Bob 相關聯。

![RGB-Bitcoin](assets/fr/059.webp)

**建造新物業 (*新國家*) :**

鮑勃傳送給愛麗絲以 ***Invoice*** 形式編碼的資訊（我們會在後面的章節詳細說明 Invoice 的建構），要求她建立一個符合 Contract 規則的新狀態。這個狀態會包含一個新的 *Seal Definition* 指向鮑勃的其中一個 UTXO。如此一來，鮑勃就會得到這個新狀態所定義資產的 Ownership，例如一定數量的 RGB 代幣。

![RGB-Bitcoin](assets/fr/060.webp)

**準備交易樣本：**

Alice 然後建立一個 Bitcoin 交易，花費先前 Seal 所引用的 UTXO（使她合法化為持有人的那個）。在這個交易的輸出中，一個 *Commitment*（透過 `Opret` 或 `Tapret`）被插入到 Anchor 新的 RGB 狀態。`Opret` 或 `Tapret` 承諾來自 *MPC tree*（如前幾章所見），它可以彙集來自不同合約的數個轉換。

**傳送*Consignment*給Bob:**

在廣播交易之前，Alice 會傳送一個 ***Consignment*** 給 Bob，其中包含所有必要的 *client-side* 資料 (他的 *Stash*)，以及對 Bob 有利的新狀態資訊。此時，Bob 應用 RGB 共識規則：


- 它會驗證 *Consignment* 中包含的所有 RGB 資料，包括賦予它資產 Ownership 的新狀態；
- 依據*Consignment*中包含的*Anchors*，它會驗證見證交易的時序（從 Genesis 到最近的轉換），並驗證 Blockchain 中的相應承諾。

**過渡完成：**

如果 Bob 感到滿意，他可以給予批准 (例如，簽署 *Consignment*)。接著 Alice 就可以廣播準備好的樣本交易。一旦確認後，這就會關閉先前由 Alice 持有的 Seal，並由 Bob 正式確認 Ownership。反 Double-spending 安全性則基於與 Bitcoin 相同的機制：UTXO 已經用完，證明 Alice 無法再重複使用。

![RGB-Bitcoin](assets/fr/061.webp)

新的狀態現在會參考 Bob 的 UTXO，讓 Bob 得到先前由 Alice 持有的 Ownership。錨定 RGB 資料的 Bitcoin 輸出，成為 Ownership 轉移的不可撤銷證明。

由兩個 Contract 作業（一個 **Genesis** 然後一個 ***State Transition*** ）組成的最小 DAG (*Directed Acyclic Graph*) 的範例可以說明 RGB 狀態 (* 客戶端 * Layer，紅色) 如何連接至 Bitcoin Blockchain (*Commitment* Layer，橘色)。

![RGB-Bitcoin](assets/fr/062.webp)

它顯示一個 Genesis 定義了一個 Seal (*Seal Definition*)，然後一個 *State Transition* 關閉這個 Seal，在另一個 UTXO 中建立一個新的 Seal。

在這種情況下，這裡有一些術語的提醒：


- 一台 ***Assignment*** 將 ：
    - 一台 ***Seal Definition*** (指向 UTXO)；
    - Owned States**，即與 Ownership 相關聯的資料 (例如，代幣轉移的數量)。
- 一個 **Global State** 匯集了 Contract 的一般屬性，對所有人可見，並確保演化的全局一致性。

狀態轉換**（State Transitions）在前一章中已描述，是 Contract Operation 的主要形式。它們參考一個或多個先前的狀態（來自 Genesis 或另一個 State Transition），並將它們更新為新的狀態。

![RGB-Bitcoin](assets/fr/063.webp)

此圖顯示在一個 *State Transition Bundle* 中，如何在單一樣本交易中關閉數個封印，同時開啟新的封印。事實上，RGB 通訊協定的一個有趣特點是它的擴充能力：數個過程可以聚合成一個 Transition Bundle，每個聚合都與 *MPC 樹*（一個獨特的捆綁識別符）的一個獨特葉子相關聯。拜 *Deterministic Bitcoin Commitment* (DBC) 機制所賜，整個訊息會插入到 `Tapret` 或 `Opret` 輸出中，同時關閉先前的封印，並可能定義新的封印。Anchor* 是儲存在 Blockchain 中的 Commitment 與 Client-side Validation 結構（*客戶端）之間的直接連結。

在接下來的章節中，我們將探討建立和驗證 State Transition 所涉及的所有元件和流程。這些 Elements 大多數都是 RGB 共識的一部分，在 **RGB Core Library** 中實作。

### Transition Bundle

在 RGB 上，可以捆綁屬於相同 Contract 的不同狀態轉換（即共用相同的 **ContractId**，源自 Genesis **OpId**）。在最簡單的情況下，就像上述範例中的 Alice 與 Bob 之間，一個 **Transition Bundle** 只包含一個轉換。但支援多付費者作業 (例如：coinjoins、Lightning channel openings 等) 表示多位使用者可以將他們的狀態轉換 (State Transition) 結合在單一束中。

收集後，這些轉換會（透過 MPC + DBC 機制）錨定在單一的 Bitcoin 交易中：


- 每個 State Transition 都經過散列，並組成一個 Transition Bundle ；
- Transition Bundle 本身會進行散列，並插入與此 Contract 對應的 MPC 樹葉中（一個 BundleId）；
- 最後透過 Witness Transaction 中的 `Opret` 或 `Tapret` 啟動 MPC 樹狀結構，從而關閉已消耗的封印並定義新的封印。

技術上來說，在 MPC 工作表中插入的 **BundleId** 是從應用於 bundle 的 *InputMap* 欄位的嚴格序列化的標記 Hash 取得的：

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

其中 `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03` 為例。

InputMap* 是一個資料結構，它列出樣本交易的每個輸入 `i`，對應 State Transition 的 *OpId* 的參照。例如

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` 是交易中引用 `OpId` 的條目總數；
- opId(input_j)` 是 bundle 中一個狀態轉換的操作識別碼。

透過每個項目只參考一次且有序的方式，我們可以防止相同的 Seal 在兩個同時進行的狀態轉換中使用兩次。

### 狀態產生與作用中狀態

因此，狀態轉換可用於將資產的 Ownership 從一個人轉移至另一個人。然而，它們並非 RGB 通訊協定中唯一可能的操作。該通訊協定定義了三種 **Contract 作業** ：


- State Transition** ；
- Genesis** ；
- State Extension**.

其中，**Genesis** 和 **State Extension** 有時被稱為「*狀態產生操作*」，因為它們會建立新的狀態，而不會立即關閉任何狀態。這是非常重要的一點： **Genesis** 和 **State Extension** 不涉及關閉 Seal。相反，它們定義了一個新的 Seal，而這個新的 Seal 必須由後續的 **State Transition** 耗費，才能在 Blockchain 歷史中真正生效。

![RGB-Bitcoin](assets/fr/064.webp)

Contract 的 **Active State** 通常定義為從 Genesis 開始，在 Bitcoin Blockchain 的所有錨點之後，由交易歷史（DAG）所產生的最新狀態集合。任何已過時的舊狀態（即附在已用完的 UTXO 上）不再視為活動狀態，但仍是檢查歷史一致性的必要條件。

### Genesis

Genesis 是每個 RGB Contract 的起點。它由 Contract 發行者建立，並根據 **Schema** 定義初始參數。就 RGB 令牌而言，Genesis 可指定，例如 ：


- 最初建立的代幣數量及其擁有者；
- 總可能發行上限 ；
- 任何重新發行的規則，以及哪些參與者符合資格。

作為 Contract 中的第一筆交易，Genesis 不會引用任何先前的狀態，也不會關閉任何 Seal。然而，Genesis 必須被第一筆 State Transition (通常是掃描/自動消費交易給發行商本身，或是初次分發給使用者) **消耗** (關閉) 後，才能出現在歷史記錄中並被驗證。

### State Extension

State Extensions** 為智慧契約提供了獨創的功能。它們讓 Redeem 在 Contract 定義中規定的某些數位權利 (*Valencies*) 成為可能，而不會立即關閉 Seal。最常見的情況是，這涉及到 .NET 和 .NET：


- 分散式代幣問題；
- 資產交換機制 ；
- 有條件重發（可能包括銷毀其他資產等）。

技術上來說，State Extension 會引用 *Redeem*（一種特殊類型的 RGB 輸入），對應於先前定義的 *Valency*（例如，在 Genesis 或其他 State Transition 中）。它定義了一個新的 Seal，可提供給受益的人或條件。要使 Seal 生效，必須由後續的 State Transition 使用。

![RGB-Bitcoin](assets/fr/065.webp)

例如：Genesis 會產生發行權 (*Valency*)。經授權的行動者可行使此權利，並建立 State Extension ：


- 它指的是 Valency (Redeem)；
- 它會建立一個指向 UTXO 的新 *Assignment*（新 *Owned State* 資料）；
- 未來由此新 UTXO 擁有者發行的 State Transition 將實際轉移或分發新發行的代幣。

### Contract Operation 的組件

現在我想詳細看看 RGB 中 **Contract Operation** 的每個組成 Elements。Contract Operation 是修改 Contract 狀態的動作，並由合法收件者以確定的方式在用戶端進行驗證。特別地，我們會看到 Contract Operation 如何一方面考慮到 Contract 的**舊狀態** (*Old State*)，另一方面考慮到**新狀態** (*New State*)的定義。

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

如果我們看上面的圖表，我們可以看到一個 Contract Operation 包含 Elements 指的是**新的狀態**，而其他則指的是更新後的**舊狀態**。

**新國家**的 Elements 是 ：


- 指派**，其中定義了 ：
 - Seal Definition***；
 - **Owned State**。
- **Global State**，可以修改或豐富；
- Valencies**, 可能在 State Transition 或 Genesis 中定義。

**舊國家**是透過 .NET Framework 來引用的：


- 輸入**，指向先前狀態轉換的*Assignments*（Genesis 中並沒有）；
- Redeems**，指先前定義的 Valencies（僅在 State Extensions 中）。

此外，Contract Operation 包含更多針對操作的一般欄位：


- ffv`（*快轉版本*）：表示 Contract 版本的 2 位元整數；
- transitionType` 或 ExtensionType`：根據 Business Logic 指定轉換或擴充類型的 16 位元整數；
- `ContractId`：參考 Contract Genesis 的 *OpId* 的 32 位元組編號。包含在轉換與擴充中，但不包含在 Genesis 中；
- schemaId：僅在 Genesis 中出現，這是 32 位元組的 Hash，代表 Contract 的結構 (*Schema*)；
- Testnet`：布林值，表示您是在 Testnet 或 Mainnet 網路上。僅限 Genesis；
- altlayers1`：變數，用來識別除了 Bitcoin 之外，用於 Anchor 資料的替代 Layer (Sidechain 或其他)。僅存在於 Genesis 中；
- metadata」：可儲存臨時資訊的欄位，有助於驗證複雜的 Contract，但不得記錄在最終狀態歷史中。

最後，所有這些欄位都會透過自訂的雜湊程序進行濃縮，以產生獨一無二的指紋「OpId」。此 `OpId` 隨後會整合到 Transition Bundle 中，使其能夠在通訊協定中進行驗證和驗證。

因此，每個 *Contract Operation* 都由一個名為 `OpId` 的 32 位元組 Hash 來識別。這個 Hash 是由組成操作的所有 Elements 的 SHA256 Hash 計算出來的。換句話說，每個 *Contract Operation* 都有自己的加密 Commitment，其中包含驗證操作真實性和一致性所需的所有資料。

RGB Contract 由 Genesis `OpId`衍生的 `ContractId` 來識別（因為沒有預先的 Genesis 操作）。具體來說，我們使用 Genesis `OpId`，倒轉位元組順序並應用 Base58 編碼。這種編碼使 `ContractId` 更容易處理和辨識。

### 狀態更新方法和規則

**Contract State** 代表 RGB 通訊協定必須追蹤給定 Contract 的資訊集。它由 ：


- 單一 Global State**：這是 Contract 的公共、全局部分，對所有人可見；
- 一個或多個 Owned 狀態**：每個 Owned State 都與唯一的 Seal 相關聯（因此在 Bitcoin 上有一個 UTXO）。.與.之間有區別：
    - 公**擁有的國家、
    - 私人**擁有的國家。

![RGB-Bitcoin](assets/fr/066.webp)

*Global State* 作為單一區塊直接包含在 *Contract Operation* 中。*Owned States* 定義在每個 *Assignment* 中，與 *Seal Definition* 一起。

RGB 的一大特色是修改 Global State 和 Owned States 的方式。一般有兩種行為：


- 可變**：當狀態元素被描述為可變時，每次新的操作都會以新的狀態取代先前的狀態。舊資料會被視為過時；
- 累積**：當狀態元素被定義為累積時，每次新的操作都會在之前的狀態上增加新的資訊，而不會覆蓋之前的狀態。結果就是一種累積的歷史。

如果在 Contract 中，某個狀態元素沒有被定義為可變或可累積，則此元素在後續操作中會保持為空（換言之，此欄位沒有新版本）。是 Contract 的 Schema（即編碼的 Business Logic）決定一個狀態（全局或擁有）是可變更、累積或固定的。一旦定義了 Genesis，只有在 Contract 本身允許的情況下才能修改這些屬性，例如透過特定的 State Extension。

下表說明每種類型的 Contract Operation 如何操控（或不操控）Global State 和 Owned State：

| | Genesis | State Extension | State Transition |

| ---------------------------- | :-----:| :-------------:| :--------------:|

| **新增 Global State** | + | - | + | |

| ** Global State 的突變** | n/a | - | + | |

| **新增 Owned State** | + | - | + | |

| **Owned State的突變** | n/a | No | + | |

| **添加 Valencies** | + | + | + | |

**`+`** : 如果 Contract 的 Schema 允許，則可執行動作。

**`-`**：操作必須由後續的 State Transition 確認（單獨的 State Extension 並不能關閉 Single-Use Seal）。

此外，每種資料的時間範圍和更新權限可在下表中區分：

| | 元數據 | Global State | Owned State

| ------------------------------- | ---------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |

| **範圍** | 為單一 Contract Operation 定義 | 為 Contract 全局定義 | 為每個 Seal (*Assignment*) 定義 | ** 範圍** | 為單一 Contract Operation 定義 | 為 Contract 全局定義 | 為每個 Seal (*Assignment*) 定義

| **誰可以更新它？** | 不可更新（短暫資料） | 由行為人（發行者等）發行的操作 | 取決於擁有 Seal 的合法持有人（可以在隨後的交易中使用它的人） | **誰可以更新它？

| **時間範圍** | 僅適用於目前的作業 | 狀態在作業結束時建立 | 狀態在作業之前已定義（由前一作業的 *Seal Definition* 定義） | | **時間範圍** | 僅適用於目前的作業 | 狀態在作業結束時建立

### Global State

Global State 常被形容為「沒有人擁有，大家都知道」。它包含有關 Contract 的一般資訊，這些資訊是公開可見的。例如，在代幣發行的 Contract 中，它可能包含 ：


- ticker (代號的符號縮寫)：`ticker` ；
- 標記的全名： `name` ；
- 精度（小數點位數）：`precision` ；
- 初始發售 (和/或最大代幣限制)：`issuedSupply` ；
- 發行日期： `created` ；
- 法律資料或其他公開資訊： `data`。

這些 Global State 可以放置在公共資源（網站、IPFS、Nostr、Torrent 等）上，並分發給社群。同時，經濟誘因（需要持有和傳輸這些代幣等）自然會促使 Contract 使用者自行維護和傳播這些資料。

### 作業

*Assignment* 是定義 .NET 的基本結構：


- Seal (*Seal Definition*)，指向特定的 UTXO；
- *Owned State*，即與此 Seal 相關的屬性或資料。

*Assignment* 可視為 Bitcoin 交易輸出的類比，但更具彈性。這就是財產轉移的邏輯： *Assignment*將特定類型的資產或權利 (`AssignmentType`)與 Seal 相關聯。誰擁有與此 Seal 連結的 UTXO 私密金鑰（或誰能花費此 UTXO），誰就被視為此 *Owned State* 的擁有者。

RGB 的一大優勢在於能夠隨意顯示 (*reveal*) 或隱藏 (*conceal*) *Seal Definition* 和 *Owned State* 欄位。這提供了保密性和選擇性的強大組合。舉例來說，您可以在不揭露所有資料的情況下，證明轉換是有效的，方法是將揭露的版本提供給必須驗證的人，而第三方只能看到隱藏的版本 (一個 Hash)。實際上，轉換的 `OpId` 總是從 * 隱藏 * 資料計算出來的。

![RGB-Bitcoin](assets/fr/067.webp)

#### Seal Definition

*Seal Definition* 在其揭示的形式中，有四個基本欄位：txptr"、"vout"、"blinding 「和 」method"：


- txptr**： 這是 Bitcoin 上的 UTXO 參照 ：
    - 如果是 **Genesis Seal**，則會直接指向現有的 UTXO（與 Genesis 相關的 UTXO）；
    - 在**圖 Seal** 的情況下，我們可以有 ：
        - 一個簡單的 `txid`，如果指向特定的 UTXO、
        - 或`WitnessTx`，它指定了一個自我參考：Seal 指向交易本身。這在沒有外部 UTXO 時特別有用，例如在 Lightning 通道開啟交易中，或收件人沒有 UTXO 時。
- vout** : `txptr` 所指示的交易輸出號碼。只出現在標準圖形 Seal (不適用於 `WitnessTx`)；
- billing**：8 位元組的隨機數字，用來加強機密性，並防止對 UTXO 身份的暴力嘗試；
- method** : 表示使用的錨定方法 (`Tapret`或`Opret`)。

Seal Definition 的*隱藏*形式是這 4 個欄位串連的 SHA256 Hash（已標記），並加上 RGB 的特定標記。

![RGB-Bitcoin](assets/fr/068.webp)

#### 擁有國家

*Assignment* 的第二個元件是 Owned State。與 Global State 不同的是，它可以公共或私人形式存在：


- 公開 Owned State**：所有人都知道與 Seal 相關的資料。例如，公開圖片；
- 隱私 Owned State**：資料是隱藏的，只有擁有者（必要時也可能包括驗證者）知道。例如，持有的代幣數量。

RGB 定義了 Owned State 四種可能的狀態類型 (*StateTypes*)：


- 宣告式**：不包含數值資料，只包含宣告式權利 (例如投票權)。隱藏和揭示的形式是相同的；
- Fungible**: 代表可替代的數量 (就像代幣)。在揭示形式中，我們有 `amount` 和 `blinding`。在隱藏形式中，我們有一個 *Pedersen commitment*，它會隱藏數量和盲點；
- Structured**: 儲存結構化資料 (最多 64 kB)。在揭示形式下，它是資料 Blob。在隱藏形式下，它是此 blob 的標記 Hash：

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

例如：

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Attachments**：將檔案 (音訊、影像、二進位檔案等) 連結至 Owned State，儲存檔案 Hash `file_hash`、MIME 類型 `media type` 及加密鹽值 `salt`。檔案本身則存放在其他地方。在隱藏形式下，它是一個以前面三個資料項為標記的 Hash：

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

例如：

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

總括而言，以下是公開和隱藏形式的 4 種可能狀態：

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **元素** | **表述式** | **可變式** | **結構化** | **附件** | **附件**

| ------------------- | -------------- | ------------------------------------ | ----------------------------- | ----------------------------- |

| **資料** | 無 | 有符號或無符號 64 位元整數 | 任何嚴格的資料類型 | 任何檔案 | **資料** | 無 | 有符號或無符號 64 位元整數 | 任何嚴格的資料類型 | 任何檔案

| **資訊類型** | 無 | 有符號或無符號 | 嚴格類型 | MIME 類型

| **隱私權** | 非必要 | Pedersen commitment | Hash 帶有盲點 | 哈希文件識別碼 | ** 隱私權** | 非必要

| **大小限制** | 不適用 | 256 位元組 | 高達 64 KB | 高達 ~500 GB | 不適用

### 輸入

*Contract Operation* 的 Input（輸入）是指在此新操作中使用的 *Assignments（分配）。一個 Input 表示 ：


- prevOpId` : *Assignment*所在的上一個操作的識別碼 (`OpId`)；
- assignmentType`： *Assignment*的類型（例如，"assetOwner "用於令牌）；
- `Index`： *Assignment*在與前一個`OpId`關聯的清單中的索引，在隱藏封條的詞彙排序後決定。

輸入從來沒有出現在 Genesis 中，因為之前沒有 Assignments。它們也不會出現在 State Extensions 中（因為 State Extensions 不會關閉封印，而是根據 Valencies 重新定義新的封印）。

當我們有 Owned 屬於 `Fungible` 類型的狀態時，驗證邏輯 (透過 Schema 中提供的 AluVM 指令碼) 會檢查總和的一致性：進入的代幣 (*Inputs*) 總和必須等於輸出的代幣 (在新的 *Assignments* 中) 總和。

### 元資料

**Metadata** 欄位最多可達 64 KiB，用來包含對驗證有用的臨時資料，但不會整合到 Contract 的永久狀態中。例如，複雜腳本的中間計算變數可以儲存在這裡。此空間不打算儲存在全局歷史中，這也是它不屬於 Owned State 或 Global State 範圍的原因。

### 閥值

Valencies** 是一種原始的 RGB 通訊協定機制。它們可以在 Genesis、State Transition 或 State Extensions 中找到。它們代表可由 State Extension (透過 *Redeems*) 啟動，然後由後續的轉換 (Transition) 終止的數值權利。每個 Valency 都由一個 `ValencyType` (16 位元) 來識別。其語義 (重新發行權、代幣交換、燒錄權等) 定義在 Schema 中。

具體來說，我們可以想像一個 Genesis 定義了一個「再發行權」Valency。如果符合特定條件，State Extension 將消耗它 (*Redeem*)，以引入新數量的代幣。然後，由 Seal 持有者產生的 State Transition 可以轉讓這些新代用幣。

### 贖回

Redeems 相當於 Valency 的 Assignments 輸入。它們只出現在 State Extension 中，因為這是啟動先前定義的 Valency 的地方。Redeem 由兩個欄位組成：


- `PrevOpId` : 指定 Valency 的操作的 `OpId`；
- `ValencyType`：您想要啟動的 Valency 類型 (每個 `ValencyType` 只能被 State Extension 使用一次)。

例如：Redeem 可以對應 CoinSwap 執行，這取決於在 Valency 中編碼的內容。

### RGB 狀態特性

現在我們來看看 RGB 的幾個基本狀態特性。特別是，我們會看看 ：


- **Strict Type System**，強制對資料進行精確的類型化組織；
- 將**驗證**與**Ownership**分開的重要性 ；
- RGB 中的**共識演化**系統，其中包括*快進*和*推回*的概念。

一如往常，請記住所有與 Contract 狀態有關的事情都是根據協定中設定的共識規則在用戶端進行驗證，其最終的加密參考是以 Bitcoin 交易為基礎。

#### 嚴格的類型系統

RGB 使用 *Strict Type System* 和確定的序列化模式 (*Strict Encoding*)。這個組織的設計是為了保證 Contract 資料在定義、處理和驗證時的完美可重複性和精確性。

在許多程式設計環境（JSON、YAML......）中，資料結構可以很靈活，甚至是太過放任。另一方面，在 RGB 中，每個欄位的結構和類型都有明確的限制。例如 ：


- 每個變數都有特定的類型 (例如 8 位元無符號整數 `u8`，或 16 位元有符號整數等)；
- 類型可以組成（嵌套類型）。這表示您可以基於其他類型定義一個類型（例如，一個集合類型包含一個 `u8` 欄位、一個 `bool` 欄位等）；
- 也可以指定集合：清單 (*list*)、集合 (*set*) 或字典 (*map*)，並以確定的順序進行；
- 每個欄位都是有邊界的（*下限* / *上限*）。我們也對集合中的 Elements 數量施加限制（包含）；
- 資料是位元組對齊的，序列化是嚴格定義且毫不含糊的。

多虧了這個嚴格的編碼協定 ：


- 不論使用何種實作或程式語言，欄位的順序總是相同的；
- 因此，以相同資料集計算的哈希值是可重複且相同的（嚴格的確定性*承諾*）；
- 邊界可防止資料大小不受控制地增長（例如欄位太多）；
- 這種編碼形式有助於加密驗證，因為每個參與者都清楚知道如何將資料序列化和 Hash。

實際上，結構 (*Schema*) 和產生的程式碼 (*Interface* 和相關邏輯) 都是經過編譯的。使用描述性語言來定義 Contract（類型、欄位、規則）和 generate 一個嚴格的二進位格式。編譯後的結果是 .NET：


- 每個欄位的*記憶體佈局*；
- 語義識別符（表示變量名稱的變更是否會對邏輯產生影響，即使記憶體結構保持不變）。

嚴格的類型系統也能精確監控變更：結構的任何修改 (即使是欄位名稱的變更) 都能被偵測到，並可能導致整體足跡的改變。

最後，每次編譯都會產生一個指紋，這是一個加密識別碼，可證明程式碼（資料、規則、驗證）的確實版本。例如，形式為 ：

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

這使得管理共識或實施更新成為可能，同時確保網路中使用的版本具有詳細的可追溯性。

為了防止 RGB Contract 的狀態在客戶端驗證時變得過於麻煩，一項共識規則規定驗證計算中涉及的任何資料的最大大小為 `2^16` 位元組 (64 Kio)。這適用於每個變數或結構：不超過 65536 位元組，或等效的數字 (32768 16 位元整數等)。這也適用於集合 (清單、集合、映射)，不得超過 `2^16` Elements。

此限制可保證 ：


- 控制 State Transition 期間要處理的資料最大大小；
- 與用來執行驗證指令碼的虛擬機器 (*AluVM*) 相容。

#### 驗證 != Ownership 典範

RGB 的一大創新是嚴格區分兩個概念：


- 驗證**：檢查 State Transition 是否尊重 Contract 的規則 (Business Logic、歷史等)；
- **Ownership**（Ownership，或稱控制）：擁有 Bitcoin UTXO 的事實，可讓 Single-Use Seal 花費（或關閉），進而發生 State Transition。

驗證**發生在 RGB 軟體堆疊層級 (函式庫、*承諾*協定等)。其作用是確保 Contract 的內部規則（金額、權限等）受到尊重。觀察員或其他參與者也可以驗證資料歷史。

另一方面，Ownership** 完全依賴 Bitcoin 的安全性。擁有 UTXO 的私密金鑰意味著可以控制啟動新轉換（關閉 Single-Use Seal）的能力。因此，即使有人可以看到或驗證資料，但如果他們不擁有相關的 UTXO 就無法改變狀態。

![RGB-Bitcoin](assets/fr/069.webp)

這種方法限制了在更複雜的區塊鏈中遇到的典型漏洞（Smart contract 的所有代碼都是公開的，任何人都可以修改，有時這會導致黑客入侵）。在 RGB 上，攻擊者無法簡單地與 On-Chain 狀態互動，因為對狀態 (*Ownership*) 行動的權利受到 Bitcoin Layer 的保護。

更重要的是，此解耦功能可讓 RGB 與 Lightning Network 自然整合。Lightning通道可以用來接觸和移動RGB的資產，而不需要每次都接觸On-Chain的*承諾*。我們會在本課程的後續章節更仔細地了解 RGB 在 Lightning 上的這種整合。

#### RGB 的共識發展

除了語意程式碼版本化之外，RGB 還包含一個可隨時間演進或更新 Contract 共識規則的系統。演進有兩種主要形式：


- 快進**
- 推回**（法文）

當先前無效的規則變為有效時，就會發生快轉。例如，如果 Contract 演變為允許新的 `AssignmentType` 類型或新的欄位 ：


- 這無法與經典的 Blockchain hardfork 相提並論，因為 RGB 可以在 Client-side Validation 中運作，並且不會影響 Blockchain 的整體相容性；
- 實際上，這類變更是以 Contract Operation 中的 `Ffv`（*快轉版本*）欄位來表示；
- 目前的持有者不會受到傷害：他們的身份仍然有效；
- 另一方面，新受益人（或新使用者）需要更新其軟體（其 Wallet）以識別新規則。

回推意味著之前有效的規則變得無效。因此它是規則的「硬化」，但嚴格來說不是軟叉：


- 現有持有人可能會受到影響（他們可能會發現自己的資產在新版本中變得過時或無效）；
- 我們可以認為，我們事實上是在創造一個新的規約：誰採用新規則，誰就背離舊規約；
- 發行商可能會決定在此新通訊協定中重新發行資產，迫使使用者維護兩個獨立的錢包 (一個用於舊通訊協定，另一個用於新通訊協定)，如果他們想要管理兩個版本的話。

在關於 RGB Contract 作業的本章中，我們探討了此通訊協定的基本原則。您應該已經注意到，RGB 通訊協定本身的複雜性需要使用許多技術詞彙。因此，在下一章中，我將為您提供一份詞彙表，總結這第一個理論部分所涵蓋的所有概念，以及所有與 RGB 相關的技術詞彙定義。接著，在下一節中，我們將從實務角度來探討 RGB 合約的定義與執行。

## RGB 詞彙

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

如果您需要回顧這份簡短的詞彙表，其中包含 RGB 世界中使用的重要技術詞彙 (依字母順序列出)，您會發現它非常有用。如果您已經瞭解我們在第一節中所涵蓋的所有內容，本章並非必要。

#### AluVM

縮寫 AluVM 代表「_算術邏輯單元虛擬機_」，是專為 Smart contract 驗證和分散式運算所設計的寄存器型虛擬機。它用於（但並非專屬保留）RGB 合約的驗證。因此，RGB Contract 中包含的腳本或操作可以在 AluVM 環境中執行。

如需更多資訊：[AluVM 官方網站](https://www.AluVM.org/)

#### Anchor

Anchor 代表一組用戶端資料，用於證明交易中包含唯一的_commitment_。在 RGB 通訊協定中，Anchor 包含下列 Elements：


- **Witness Transaction**的 Bitcoin 交易識別碼 (txid) ；
- **Multi Protocol Commitment (MPC)** ；
- **Deterministic Bitcoin Commitment (DBC)**；
- 如果使用 **Tapret** Commitment 機制，則需要 ** 額外交易證明 (ETP)**（請參閱此機制專用章節）。

因此，Anchor 可在特定的 Bitcoin 交易與經 RGB 通訊協定驗證的私人資料之間建立可驗證的連結。它保證這些資料確實包含在 Blockchain 中，但其確切內容不會公開曝光。

#### Assignment

在 RGB 的邏輯中，Assignment 相當於在 Contract 狀態中修改、更新或建立某些屬性的交易輸出。一個 Assignment 包含兩個 Elements：


- A **Seal Definition**（提及特定的 UTXO） ；
- 一個 **Owned State**（描述與此新業主相關的狀態的資料）。

因此，Assignment 表示狀態的一部分（例如資產）現在分配給特定的持有人，該持有人通過與 UTXO 相連的 Single-Use Seal 識別。

#### Business Logic

Business Logic 組合了 Contract 的所有規則和內部運作，由其 **Schema**（即 Contract 本身的結構）描述。它規定 Contract 的狀態如何演進，以及在何種條件下演進。

#### Client-side Validation

Client-side Validation 是指各方（客戶端）根據協定規則驗證私下交換的資料集的過程。在 RGB 的情況下，這些交換的資料會被組合起來，稱為 **交易**。RGB 與 Bitcoin 規約不同，Bitcoin 規約要求所有的交易都要公佈於 On-Chain，而 RGB 則只允許 _commitments_ (錨定於 Bitcoin)公開儲存，而基本的 Contract 資訊 (轉換、認證、證明) 則保留於 off-chain，僅在相關使用者之間分享。

#### Commitment

Commitment (在密碼學的意義上) 是一個數學物件，表示為 `C`，由結構化資料 `m` (訊息) 和隨機值 `r` 的運算確定地衍生出來。我們寫成 ：

$$
C = \text{commit}(m, r)
$$

此機制包含兩個主要操作：


- Commit**：將加密函數應用於訊息 `m` 和隨機數 `r` 以產生 `C` ；
- 驗證**：我們使用 `C`、`m` 訊息和 `r` 值來檢查這個 Commitment 是否正確。函式會回傳 `True` 或 `False`。

Commitment 必須尊重兩個屬性：


- 綁定**：一定不可能找到兩個不同的訊息產生相同的 `C` ：

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

例如：

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- 隱藏**: 瞭解 `C` 不得洩露 `m` 的內容。

在 RGB 通訊協定中，Commitment 會包含在 Bitcoin 交易中，以證明在特定時間存在某項資訊，但不會透露資訊本身。

#### Consignment

一個**Consignment**將各方之間交換的資料組合起來，受 Client-side Validation 的規範，在 RGB 中。Consignment 有兩大類：


- Contract Consignment**：由 * 發行者* (Contract 發行者) 提供，它包括初始化資訊，例如 Schema、Genesis、Interface 和 Interface Implementation。
- 傳輸 Consignment**：由付款方 (*payer*) 提供。它包含導致 Terminal Consignment 的整個狀態轉換歷史（即付款方收到的最終狀態）。

這些託運貨物不會在 Blockchain 上公開記錄，而是由相關各方透過其選擇的通訊渠道直接交換。

#### Contract

Contract 是一組透過 RGB 通訊協定在多位行動者之間以數位方式執行的權利。它有一個活動狀態和一個由 Schema 定義的 Business Logic，Business Logic 指定哪些操作是授權的（轉接、延長等）。Contract 的狀態及其有效性規則在 Schema 中表達。在任何時候，Contract 只會根據 Schema 和驗證腳本（例如在 AluVM 中執行）所允許的內容發展。

#### Contract Operation

Contract Operation 是根據 Schema 規則執行的 Contract 狀態更新。RGB 中存在以下操作：


- State Transition** ；
- Genesis** ；
- State Extension**.

每個操作都會透過新增或取代某些資料來修改狀態 (Global State、Owned State...) 。

#### Contract Participant

Contract Participant 是指參與 Contract 相關作業的行動者。在 RGB 中，區分為：


- Contract 的簽發者，會產生 Genesis（Contract 的來源）；
- Contract 方，即 Contract 狀態的權利持有者；
- 如果 Contract 提供公眾可存取的 Valencies，則公眾方可建立國家擴展區。

#### Contract Rights

Contract Rights 指參與 RGB Contract 者可行使的各種權利。它們可分為幾類：


- Ownership 權限**，與特定 UTXO 的 Ownership 相關聯（透過_Seal Definition_）；
- 執行權**，即根據 Schema 建立一個或多個轉換（State Transitions）的能力；
- 公共權利**，當 Schema 授權某些公共用途時，例如透過贖回 Valency 建立 State Extension。

#### Contract State

Contract State 對應於特定時刻 Contract 的當前狀態。它可以由公開和私人資料組成，反映 Contract 的狀態。RGB 區分.NET 與.NET：


- **Global State**，其中包括 Contract 的公共屬性（在 Genesis 中設定或透過授權更新新增）；
- Owned States**，屬於特定所有者，由其 UTXOs 識別。

#### Deterministic Bitcoin Commitment - DBC

Deterministic Bitcoin Commitment (DBC) 是一套規則，用來在 Bitcoin 交易中以可證明和唯一的方式註冊_commitment_。在 RGB 通訊協定中，DBC 有兩種主要形式：


- Opret**
- Tapret**

這些機制精確地定義了 _commitment_ 在 Bitcoin 交易的輸出或結構中如何編碼，以確保此 Commitment 是確定地可追蹤與可驗證的。

#### Directed Acyclic Graph - DAG

DAG (或 *Acyclic Guided Graph*) 是一種無週期圖形，可實現拓樸調度。區塊鏈，就像 RGB 合約的_shards_，可以用 DAG 表示。

如需更多資訊：[Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### 雕刻

雕刻是一個可選的資料字串，Contract 的繼任擁有者可將其輸入 Contract 歷史。例如，此功能存在於 **RGB21** Interface 中，可將紀念或描述性資訊加入 Contract 歷史中。

#### 額外交易證明 - ETP

ETP (*Extra Transaction Proof*) 是 Anchor 的一部分，包含驗證 **Tapret** *Commitment*（在 _taproot_ 的情況下）所需的額外資料。其中包括 Taproot script 的內部公開金鑰 (_internal PubKey_) 以及 _Script Path Spend_ 的特定資訊。

#### Genesis

Genesis 指的是由 Schema 管轄的資料集，這些資料在 RGB 中構成任何 Contract 的初始狀態。它可以與 Bitcoin 的 _Genesis Block_ 概念或 Coinbase Transaction 概念相提並論，但這裡是在 _client-side_ 和 RGB 令牌層級。

#### Global State

Global State 是包含在 Contract State 中的公共屬性集。它定義在 Genesis，依據 Contract 規則，可由經授權的轉換更新。與 Owned State 不同，Global State 並不屬於特定實體；它更接近 Contract 內的公共註冊表。

#### Interface

Interface 是一組指令，用來解碼 Schema 或 Contract 運算中編譯的二進位資料及其狀態，以便讓使用者或其 Wallet 可以讀取。它扮演著解譯 Layer 的角色。

#### Interface Implementation

Interface Implementation 是將 **Interface** 連結至 **Schema** 的聲明集。它可讓 Interface 本身進行語意轉譯，以便使用者或相關軟體 (錢包) 能夠理解 Contract 的原始資料。

#### Invoice

Invoice 的形式是一個以 [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58) 編碼的 URL，其中包含了構建 **State Transition**（由付款方）所需的資料。換句話說，它是一個 Invoice，使交易方（*付款方*）能夠建立相應的轉換，以轉移資產或更新 Contract 的狀態。

#### Lightning Network

Lightning Network 是 Bitcoin 上支付通道（或稱 _state 通道_）的分散式網路，由 2/2 個多重簽章錢包組成。它可實現快速、低成本的_離鏈_交易，同時在必要時依賴 Bitcoin 的 Layer 1 進行仲裁（或關閉）。

如需更多關於 Lightning 如何運作的資訊，我建議您修讀此其他課程：

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
#### Multi Protocol Commitment - MPC

Multi Protocol Commitment (MPC) 是指在 RGB 中使用的 Merkle Tree 結構，在單一 Bitcoin 交易中包含來自不同合約的多個 ** 過渡包。其目的是在單一 Anchor 點組合數個承諾 (可能對應不同的合約或不同的資產)，以最佳化區塊空間的佔用。

#### Owned State

Owned State 是 Contract State 的一部分，它被包圍在 Assignment 中，並與特定持有人相關聯（通過指向 UTXO 的 Single-Use Seal）。例如，這代表分配給該人的數位資產或特定合約權利。

#### Ownership

Ownership 是指控制和使用 Seal Definition 所引用的 UTXO 的能力。當 Owned State 與 UTXO 連結時，此 UTXO 的擁有者有權根據 Contract 的規則，潛在地轉移或演變相關的狀態。

#### Partially Signed Bitcoin Transaction - PSBT

PSBT (_Partially Signed Bitcoin Transaction_) 是尚未完全簽署的 Bitcoin 交易。它可以在幾個實體之間共用，每個實體都可以新增或驗證某些 Elements（簽章、腳本...），直到該交易被視為可以進行 On-Chain 發佈為止。

如需更多資訊：[BIP-0174](https://github.com/Bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Pedersen commitment

Pedersen commitment 是加密 Commitment 的一種類型，具有與加法運算**同態**的特性。這表示可以在不透露個別值的情況下驗證兩個承諾的總和。

形式上，如果 ：

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

然後

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

例如，這個屬性對於隱藏所交換的代幣數量非常有用，同時仍能驗證總數。

進一步資訊：[Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Redeem

在 State Extension 中，Redeem 是指收回（或利用）先前聲明的 **Valency**的動作。由於 Valency 是一種公共權利，Redeem 允許授權參與者要求特定的 Contract State Extension。

#### Schema

RGB 中的 Schema 是一組宣告性的程式碼，描述管理 Contract 運作的變數、規則和 Business Logic (*Business Logic*)。Schema 定義了狀態結構、允許的轉換類型以及驗證條件。

#### Seal Definition

Seal Definition 是 Assignment 中將_承諾_與新持有人擁有的 UTXO 相關聯的部分。換句話說，它指出條件的位置（在哪個 UTXO），並建立資產或權利的 Ownership。

#### Shard

Shard 代表 RGB Contract 的狀態轉換歷史 DAG 中的一個分支。換句話說，它是 Contract 整體歷史的連貫子集，例如，對應於自 _Genesis_ 以來證明特定資產有效性所需的轉換順序。

#### Single-Use Seal

Single-Use Seal 是 Commitment 對尚未明確的訊息所做的加密承諾，此訊息在未來只會揭露一次，且必須為特定受眾的所有成員所知。其目的是為了防止對同一個 Seal 產生多個競爭承諾。

#### Stash

Stash 是用戶為一個或多個 RGB 契約儲存的用戶端資料集，用於驗證 (*Client-side Validation*)。這包括過渡歷史、託運、有效性證明等。每個持有人只保留他們需要的歷史部分（*碎片*）。

#### State Extension

State Extension 是 Contract Operation，用來贖回先前宣告的 ** Valencies**，重新觸發狀態更新。State Extension 必須由 State Transition 結束（這會更新 Contract 的最終狀態）才能生效。

#### State Transition

State Transition 是將 RGB Contract 的狀態變更為新狀態的操作。它可以修改 Global State 和/或 Owned State 資料。實際上，每個轉換都經過 Schema 規則的驗證，並透過 _commitment_ 錨定在 Bitcoin Blockchain 中。

#### Taproot

指 Bitcoin 的 SegWit v1 交易格式，由 [BIP341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) 和 [BIP342](https://github.com/Bitcoin/bips/blob/master/bip-0342.mediawiki) 推出。Taproot 改善了腳本的機密性和彈性，特別是讓交易更精簡、更難區分彼此。

#### Terminal Consignment - Consignment Endpoint

Terminal Consignment (或_Consignment Endpoint_)是*轉移 Consignment*，包含 Contract 的最終狀態，包括從接收者的 Invoice (*收款人*) 所建立的 State Transition。因此，它是轉移的終點，具有證明 Ownership 或狀態已被轉移的必要資料。

#### Transition Bundle

一個 Transition Bundle 是一組 RGB 狀態轉換 (屬於相同的 Contract)，這些狀態轉換都參與相同的 ***Witness Transaction*** Bitcoin。這使得將多個更新或傳輸捆綁到單一 On-Chain Anchor 中成為可能。

#### UTXO

Bitcoin UTXO (*Unspent Transaction Output*) 由交易的 Hash 和輸出索引 (*vout*) 定義。有時也稱為 _outpoint_。在 RGB 通訊協定中，參照 UTXO（透過 **Seal Definition**）能夠找到 **Owned State**，也就是在 Blockchain 上持有的屬性。

#### Valency

Valency 是一種不需要國家儲存的公共權利，但可以透過 **State Extension** 贖回。因此，它是一種對所有人（或某些玩家）開放的可能性形式，在 Contract 的邏輯中宣告，以便在稍後的日期執行特定的延伸。

#### Witness Transaction

Witness Transaction 是 Bitcoin 交易，用來關閉包含 Multi Protocol Commitment (MPC) 的訊息周圍的 Single-Use Seal。此交易花費一個 UTXO 或建立一個 UTXO，以便 Seal 與 RGB 協定連結的 Commitment。它的作用是 On-Chain 證明狀態已在特定時間點設定。

# 在 RGB 上編程

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## 執行 RGB 合約

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::

在本章中，我們將進一步了解 RGB Contract 是如何定義和實作的。我們會看到 RGB Contract 的元件是什麼，它們的角色是什麼，以及它們是如何構成的。

### RGB Contract 的組件

到目前為止，我們已經討論過代表 Contract 起點的 **Genesis**，也看過它如何與 *Contract Operation* 的邏輯和通訊協定的狀態配合。然而，RGB Contract 的完整定義並不僅限於 Genesis：它涉及三個互補的元件，共同構成實作的核心。

第一個元件稱為 **Schema**。這是一個描述 Contract 基本結構和 Business Logic (*Business Logic*) 的檔案。它指定了所使用的資料類型、驗證規則、允許的操作 (例如：初始代幣發行、轉移、特殊條件等)，簡而言之，就是規定 Contract 如何運作的一般框架。

第二個元件是**Interface**。它著重於使用者（以及延伸的組合軟體）如何與 Contract 互動。它描述了語義，也就是各種欄位和動作的可讀性表示。因此，Schema 定義了 Contract 如何在技術上運作，而 Interface 則定義了如何呈現和揭露這些功能：方法名稱、資料顯示等。

第三個元件是 **Interface Implementation**，它是 Schema 和 Interface 之間的橋梁，是前兩個元件的補充。換句話說，它將 Interface 所表達的語意與 Schema 所定義的基本規則聯繫起來。例如，在 Wallet 中輸入的參數與協定強制的二進位結構之間的轉換，或以機器語言編譯驗證規則，都是由此實作管理。

這種模組化是 RGB 的一個有趣特色，因為它允許不同的開發人員群組分別進行這些方面的工作 (*Schema*、*Interface*、*實施*)，只要他們遵循協定的共識規則即可。

總而言之，每台 Contract 包含 ：


- Genesis**，這是 Contract 的初始狀態（可比喻為定義資產、權利或任何其他可參數化資料的第一個 Ownership 的特殊交易）；
- Schema**，說明 Contract 的 Business Logic（資料類型、驗證規則等）；
- Interface**，為錢包與人類使用者提供語意 Layer，闡明交易的讀取與執行；
- 實施** Interface，銜接 Business Logic 與呈現方式，以確保 Contract 定義與使用者體驗一致。

![RGB-Bitcoin](assets/fr/070.webp)

值得注意的是，Wallet 若要管理 RGB 資產 (無論是可替代代幣或任何種類的權利)，必須具備所有這些 Elements 編譯： *Schema*、*Interface*、*Interface Implementation* 和 *Genesis*。這是透過 ***Contract Consignment*** 來傳輸的，也就是包含驗證客戶端 Contract 所需的一切資料包。

為了幫助釐清這些概念，以下是一個摘要表，將 RGB Contract 的元件與物件導向程式設計 (OOP) 或 Ethereum 生態系統中已知的概念進行比較：

| RGB Contract Component | Meaning | OOP Equivalent | Ethereum Equivalent | Contract

| ---------------------------- | ------------------------------------- | ------------------------------------------ | --------------------------------- |

| **Genesis** | Contract 的初始狀態 | 類建構器 | Contract 建構器 | **Genesis** | Contract 的初始狀態 | 類建構器 | Contract 建構器

| **Schema** | Contract | 類別 | Contract | 的 Business Logic

| **Interface** | Contract 的語義 | Interface (Java) / Trait (Rust) / Protocol (Swift) | ERC 標準 |

| **Interface Implementation** | 映射語義與邏輯 | Impl (Rust) / Implements (Java) | 應用程式二進位 Interface (ABI) |

左側欄位顯示 Elements 與 RGB 通訊協定的具體內容。中間一欄顯示每個元件的具體功能。然後，在「OOP 對應」欄中，我們找到物件導向程式設計中的對應詞彙：


- **Genesis** 扮演類似 *Class 建構子*的角色：Contract 的狀態就是在這裡初始化的；
- **Schema** 是一個類別的描述，也就是其屬性、方法和基本邏輯的定義；
- **Interface** 對應於 *interfaces* (Java)、*traits* (Rust) 或 *protocols* (Swift)：這些是函式、事件、欄位...的公開定義；
- **Interface Implementation** 對應於 Rust 中的 *Impl* 或 Java 中的 *Implements*，在這裡我們指定程式碼將如何實際執行 Interface 中公佈的方法。

在 Ethereum 的情境中，Genesis 更接近 *Contract 構建器*，Schema 更接近 Contract 定義，Interface 更接近 ERC-20 或 ERC-721 等標準，而 Interface Implementation 更接近 ABI (*Application Binary Interface*)，它指定了與 Contract 互動的格式。

RGB 模組化的優點也在於不同的利害關係人可以撰寫他們自己的 Interface Implementation，只要他們尊重 *Schema* 的邏輯和 *Interface* 的語意即可。因此，發行商可以開發一個新的、更方便使用者的前端 (Interface)，而不需要修改 Contract 的邏輯；反之，也可以擴充 Schema 以增加功能，並提供新版的適應 Interface Implementation，而舊有的實作在基本功能上仍然有效。

當我們編譯一個新的 Contract 時，我們會 generate 一個 Genesis（發行或分發資產的第一步），以及它的組件（Schema、Interface、Interface Implementation）。在這之後，Contract 就可以完全運作，並可以傳播給錢包和使用者。這種方法將 Genesis 與這三個元件結合，保證了高度的客製化（每個 Contract 都可以有自己的邏輯）、去中心化（每個人都可以為指定元件做出貢獻）和安全性（驗證仍由協定嚴格定義，而不像其他區塊鏈上經常出現的情況那樣依賴於任意的 On-Chain 程式碼）。

現在我想仔細看看這些組件：**Schema**、**Interface** 和 **Interface Implementation**。

### Schema

在上一節中，我們看到在 RGB 的生態系統中，一個 Contract 是由幾個 Elements 組成的：建立初始狀態的 Genesis 以及其他幾個互補的元件。Schema 的目的是宣告性地描述 Contract 的所有 Business Logic，也就是資料結構、使用的類型、允許的操作及其條件。因此，它是讓 Contract 在客戶端運作的一個非常重要的元素，因為每個參與者（例如 Wallet）必須檢查它所接收的狀態轉換是否符合 Schema 所定義的邏輯。

Schema 可比喻為物件導向程式設計 (OOP) 中的「類」。一般而言，Schema 是一個定義 Contract 元件的模型，例如 .NET、.NET、.NET 和 .NET：


- 不同類型的所有權狀態和指派 ；
- Valencies，即針對特定操作可觸發（*贖回*）的特殊權利；
- Global State 欄位，描述 Contract 的全局、公用和共用屬性；
- Genesis 結構（最先啟動 Contract 的操作） ；
- State Transition 和 State Extensions 的允許形式，以及這些操作如何修改 .NET Framework；
- 與每個作業相關的元資料，用來儲存臨時或附加資訊；
- 決定 Contract 內部資料如何演變的規則（例如，欄位是否可變或累積）；
- 被視為有效的作業順序：例如，需要遵守的轉換順序或需要滿足的邏輯條件集。

![RGB-Bitcoin](assets/fr/071.webp)

當資產的*發行者*在 RGB 上發佈 Contract 時，會提供與之相關的 Genesis 和 Schema。希望與資產互動的使用者或錢包會擷取 Schema 以瞭解 Contract 背後的邏輯，並在稍後驗證他們將參與的轉換是否合法。

對於收到 RGB 資產資訊（例如代幣轉移）的任何人而言，第一步是根據 Schema 驗證此資訊。這包括使用 Schema 編譯到 .NET Framework：


- 檢查 Owned State、Assignments 及其他 Elements 是否已正確定義，以及它們是否尊重強加的類型（所謂的 *strict type system*）；
- 檢查是否滿足轉移規則（驗證腳本）。這些腳本可透過 AluVM 執行，AluVM 存在於客戶端，負責驗證 Business Logic 的一致性（轉移金額、特殊條件等）。

實際上，Schema 並非可執行程式碼，這可見於儲存 On-Chain 程式碼的區塊鏈（Ethereum 上的 EVM）。相反，RGB 將 Business Logic (宣告性) 與 Blockchain 上的可執行程式碼 (僅限於加密錨點) 分開。因此，Schema 決定規則，但根據 Client-side Validation 原則，這些規則的應用是在 Blockchain 以外，在每個參與者的場所進行。

Schema 在被 RGB 應用程式使用之前，必須先進行編譯。編譯後會產生一個二進位檔案 (例如 `.RGB`)，或是一個加密的二進位檔案 (`.rgba`)。當 Wallet 匯入這個檔案時，它就會知道 .RGB 的內容：


- 透過嚴格的類型系統，每種資料類型 (整數、結構、陣列...) 是什麼樣子；
- Genesis 應該如何結構化 (了解資產初始化)；
- 不同類型的作業 (狀態轉換、狀態延伸) 以及它們如何修改狀態 ；
- AluVM 引擎將應用的腳本規則（在 Schema 中引入），以檢查操作的有效性。

如前幾章所述，*嚴格類型系統*提供我們穩定、確定的編碼格式：所有變數，不論是 Owned State、Global State 或 Valencies，都有精確的描述（大小、必要時的上下限、有符號或無符號類型等）。也可以定義嵌套結構，例如支援複雜的使用個案。

Schema 可選擇引用根 `SchemaId`，這有助於重複使用現有的基本結構（模板）。如此一來，您就可以演進 Contract 或從已經過驗證的範本中建立變體 (例如新類型的代幣)。這種模組化避免了重新建立整個合約的需要，並鼓勵最佳實務的標準化。

另一點很重要的是，狀態演變（轉移、更新等）的邏輯是以腳本、規則和條件的形式在 Schema 中描述的。因此，如果 Contract 設計者希望授權重新發行或強制執行燒毀機制（銷毀代幣），他可以在 Schema 的驗證部分為 AluVM 指定相應的腳本。

#### 與可編程 On-Chain 區塊鏈的差異

不像 Ethereum 之類的系統，Smart contract 程式碼 (可執行) 是寫入 Blockchain 本身，RGB 儲存 Contract (其邏輯) off-chain，是以編譯的宣告性文件的形式。這意味著 ：


- Bitcoin 網路的每個節點都沒有執行圖靈完備的虛擬機器。RGB Contract 的規則不是在 Blockchain 上執行，而是在每個希望驗證狀態的使用者身上執行；
- Contract 資料不會污染 Blockchain：只有加密證據 (*commitments*) 會嵌入 Bitcoin 交易 (透過 `Tapret` 或 `Opret`)；
- Schema 可以更新或拒絕（*快進*、*推回*等），不需要在 Bitcoin Blockchain 上進行 Fork。錢包僅需匯入新的 Schema 並適應共識變更。

#### 發行機構和使用者的使用

當*發行者*創建一項資產（例如，非通脹性的可替代代幣）時，它會準備 ：


- 描述排放、轉移等規則的 Schema ；
- 與此 Schema 相適應的 Genesis（含發行代幣的總數、初始擁有者的身份、重新發行的任何特殊 Valencies 等）。

然後，它會將編譯好的 Schema (一個 `.RGB` 檔案) 提供給使用者，以便任何收到此標記的傳輸的人可以在本機檢查操作的一致性。如果沒有這個 Schema，使用者就無法解釋狀態資料或檢查它是否符合 Contract 規則。

因此，當新的 Wallet 想要支援資產時，只需整合相關的 Schema。此機制可為新的 RGB 資產類型增加相容性，而無需變更 Wallet 的軟體基礎：只需匯入 Schema 的二進位檔並瞭解其結構即可。

Schema 定義了 RGB 中的 Business Logic。它列出 Contract 的演化規則、資料結構（Owned States、Global State、Valencies）和相關的驗證腳本（可由 AluVM 執行）。有了這個宣告性文件，Contract 的定義（編譯檔）與規則的實際執行（客戶端）就清楚地分開了。這種解耦給 RGB 帶來了極大的靈活性，可以實現廣泛的用例（可替代代幣、NFT、更複雜的合約），同時避免了可編程 On-Chain 區塊鏈典型的複雜性和缺陷。

#### Schema 範例

讓我們來看看 Schema 對於 RGB Contract 的一個具體例子。這是 Rust `nia.rs`（"*Non-Inflatable Assets*"的首字母）文件中的一個摘錄，它定義了一個可替代代幣的模型，這些代幣在其初始 Supply （非通膨資產）之外不能再發行。在 RGB 的世界裡，這種代幣可被視為等同於 Ethereum 上的 ERC20，也就是遵守某些基本規則（例如轉讓、Supply 初始化等）的可替代代幣。

在深入瞭解程式碼之前，值得回顧一下 RGB Schema 的一般結構。有一連串的宣告框架 ：


- 可能的 `SchemaId`，表示使用另一個基本 Schema 作為範本；
- **全球國家**和**自有國家**（有其嚴格的類型） ；
- Valencies** （如有）；
- 可以引用這些狀態和值的**操作** (Genesis、狀態轉換、狀態延伸)；
- 用於描述和驗證資料的 **Strict Type System**；
- 驗證腳本** (透過 AluVM 執行)。

![RGB-Bitcoin](assets/fr/072.webp)

下面的程式碼顯示 Rust Schema 的完整定義。我們將根據下面的註釋 (1) 至 (9) 逐部分進行註釋：

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - 函式標頭及子結構描述**

nia_schema()`函數會回傳一個`SubSchema`，表示這個 Schema 可以部分繼承自一個更通用的 Schema。在 RGB 的生態系統中，這種彈性使得重複使用主 Schema 的某些標準 Elements 成為可能，然後再定義特定於 Contract 的規則。在這裡，我們選擇不啟用繼承，因為 `subset_of` 將會是 `None`。


- (2) - 一般屬性：ffv、subset_of、type_system**

`ffv` 屬性對應於 Contract 的 *fast-forward* 版本。此處的 `zero!()` 值表示我們處於版本 0 或此 Schema 的初始版本。如果您之後想要增加新的功能 (新的操作類型等)，您可以遞增這個版本來表示共識的改變。

`subset_of：None ` 屬性確認沒有繼承。`type_system` 欄位指的是 `types` 函式庫中已定義的嚴格類型系統。這一行表示 Contract 使用的所有資料都使用相關函式庫所提供的嚴格序列化實作。


- (3) - 全球國家

在 `global_types` 區塊中，我們宣告四個 Elements。我們使用關鍵字，例如 `GS_NOMINAL` 或 `GS_ISSUED_SUPPLY`，以便稍後引用它們：


- `GS_NOMINAL` 指的是 `DivisibleAssetSpec` 類型，它描述所建立代幣的各種欄位 (全名、股票代號、精確度...)；
- `GS_DATA` 代表一般資料，例如免責聲明、元資料或其他文字；
- `GS_TIMESTAMP` 指的是發行日期；
- `GS_ISSUED_SUPPLY` 設定 Supply 的總數，也就是可以建立的最大代幣數。

關鍵字 `once(...)` 表示每個欄位只能出現一次。


- (4) - 擁有類型

在 `owned_types` 中，我們宣告了 `OS_ASSET`，它描述了一個可替代的狀態。我們使用 `StateSchema::Fungible(FungibleType::Unsigned64Bit)`，表示資產 (代幣) 的數量儲存為 64 位元的無符號整數。因此，任何交易都會傳送一定數量單位的此代用幣，並根據此嚴格類型化的數值結構進行驗證。


- (5) - Valencies**

我們指出 `valency_types: none!()`，這表示此 Schema 中沒有 Valencies，換句話說，沒有特殊或額外的權利 (例如重新發行、有條件燒錄等)。如果 Schema 包含任何 Valencies，則會在此節中宣告。


- (6) - Genesis：第一次操作

在此我們進入宣告 Contract 作業的部分。Genesis 的描述為 ：


- 沒有 `metadata` (欄位 `metadata：Ty::<SemId>::UNIT.id(None)`) ；
- 必須各出現一次的 Global State (`Once`)；
- 一個 Assignments 清單，其中 `OS_ASSET` 必須出現 `OnceOrMore`。這表示 Genesis 至少需要一個 `OS_ASSET` Assignment (初始持有人)；
- 無 Valency : `valencies: none!()`.

這就是我們如何限制初始代幣發行的定義：我們必須宣告所發行的 Supply (`GS_SISSUED_SUPPLY`)，加上至少一個持有者 (類型為 `OS_ASSET` 的 Owned State)。


- (7) - 延伸

外延：無！() "欄位表示在此 Contract 中並未預見任何 State Extension。這表示沒有操作 Redeem 數位權利 (Valency) 或在轉換之前執行 State Extension。一切都透過 Genesis 或 State Transition 來完成。


- (8) - 轉換：TS_TRANSFER

在 `transitions` 中，我們定義了 `TS_TRANSFER` 類型的操作。我們解釋：


- 它沒有元資料；
- 它不會修改 Global State（已在 Genesis 中定義）；
- 它需要一個或多個 `OS_ASSET` 作為輸入。這表示它必須花費現有的 Owned 狀態；
- 它會建立 (`分配`) 至少一個新的 `OS_ASSET`（換句話說，收件者會收到代幣） ；
- 它不會產生新的 Valency。

這模擬了基本轉移的行為，它消耗 UTXO 上的代幣，然後創建新的 Owned 狀態，以利於接收者，因此保留了輸入和輸出之間總量的相等。


- (9) - AluVM script 與入口點** (法文)

最後，我們宣告一個 AluVM script (`Script::AluVM(AluScript { ... })`)。這個腳本包含 ：


- 驗證時要使用的一個或多個外部函式庫 (`libs`)；
- 指向 AluVM 程式碼中函數偏移的入口點，對應於 Genesis 的驗證 (`ValidateGenesis`)，以及每個宣告的轉換 (`ValidateTransition(TS_TRANSFER)`)。

此驗證碼負責應用 Business Logic。例如，它會檢查 ：


- 在 Genesis 期間未超出 `GS_ISSUED_SUPPLY` 的範圍；
- `TS_TRANSFER` 的 `inputs` (tokens spent) 總和等於 `assignments` (tokens received) 總和。

如果不遵守這些規則，過渡將被視為無效。

這個 "*Non Inflatable Fungible Asset*" 的例子Schema 讓我們更了解簡單的 RGB 可替代代幣 Contract 的結構。我們可以清楚地看到資料描述 (Global 和 Owned States)、作業聲明 (Genesis、轉換、延伸) 和驗證執行 (AluVM scripts) 之間的區隔。有了這個模型，代幣的行為就像經典的可替代代幣，但仍在用戶端進行驗證，而且不依賴 On-Chain 基礎架構來執行其程式碼。Bitcoin Blockchain 中僅錨定加密承諾。

### Interface

Interface 是為了使 Contract 可被使用者（人類閱讀）和組合（軟體閱讀）閱讀和操作而設計的 Layer。因此，Interface 所扮演的角色相當於物件導向程式語言（Java、Rust trait 等）中的 Interface，它揭露並說明 Contract 的功能結構，但不一定揭露 Business Logic 的內部細節。

與 Schema 不同，Interface 提供 .NET 所需的讀取鍵，而 Schema 純粹是宣告性的，編譯成二進位檔案後很難原封不動地使用：


- 列出並說明 Contract 所包含的全球國家和擁有國家；
- 存取每個欄位的名稱和值，以便顯示（例如：針對代用幣，找出其股票代號、最大金額等）；
- 透過將資料與可理解的名稱相關聯（例如，透過明確指定「金額」而非二進制識別符來執行轉帳），以解釋和建構 Contract 作業 (Genesis、State Transition 或 State Extension)。

![RGB-Bitcoin](assets/fr/073.webp)

例如，有了 Interface，您就可以在 Wallet 中編寫程式碼，直接操作「代幣數量」、「資產名稱」等標籤，而不是操作欄位。如此一來，管理 Contract 就變得更直覺。如此一來，Contract 的管理變得更直覺。

#### 一般操作

此方法有許多優點：


- 標準化：**

相同類型的 Contract 可由標準 Interface 支援，在數個 Wallet 實作之間共用。這有助於相容性和程式碼重複使用。


- Schema 和 Interface 之間有明顯的分隔：**

在 RGB 設計中，Schema (Business Logic) 與 Interface（呈現與操作）是兩個獨立的實體。編寫 Contract 邏輯的開發人員可以專注於 Schema，而不必擔心人體工學或資料表示，而另一個團隊 (或同一團隊，但在不同的時間線上) 則可以開發 Interface。


- 彈性演進：**

Interface 可在資產發行後修改或新增，而無需變更 Contract 本身。這與某些 On-Chain Smart contract 系統有很大的不同，在某些系統中，Interface（通常與執行代碼混合）會凍結在 Blockchain 中。


- 多重 Interface 功能

相同的 Contract 可透過不同的 Interfaces 暴露於不同的需求：一個簡單的 Interface 供最終使用者使用，另一個較進階的 Interface 則供需要管理複雜組態作業的發行者使用。Wallet 可以依據用途選擇匯入哪一個 Interface。

![RGB-Bitcoin](assets/fr/074.webp)

實際上，當 Wallet 擷取 RGB Contract (透過 `.RGB` 或 `.rgba` 檔案) 時，也會匯入相關的 Interface，而 Interface 也會被編譯。在執行時，Wallet 可以，例如 ：


- 瀏覽國家清單並讀取其名稱，在使用者 Interface 上顯示 Ticker、Initial Amount、Issue Date 等資訊，而不是無法讀取的數字識別碼；
- 使用明確的參數名稱建立操作 (例如轉移)：不用寫成 `assignments { OS_ASSET => 1 }`，它可以在表單中提供使用者「Amount」欄位，並將此資訊轉換成 Contract 所期望的嚴格類型欄位。

#### 與 Ethereum 及其他系統的差異

在以太坊上，Interface（通過 ABI 描述，*Application Binary Interface*）一般來自 On-Chain 儲存的程式碼（Smart contract）。在不觸及 Contract 本身的情況下，修改 Interface 的特定部分可能會很昂貴或複雜。但是，RGB 完全基於 off-chain 邏輯，資料錨定在 Bitcoin 上的 *commitments* 中。這種設計使得修改 Interface（或其實作）而不影響 Contract 的基本安全性成為可能，因為業務規則的驗證仍保留在 Schema 和參考的 AluVM 程式碼中。

#### Interface 編譯

與 Schema 一樣，Interface 以原始碼定義 (通常以 Rust 定義)，並編譯為 `.RGB` 或 `.rgba` 檔案。此二進位檔案包含 Wallet 至 .Schema 所需的所有資訊：


- 以名稱識別欄位 ；
- 將每個欄位（及其值）連結到 Contract 中定義的嚴格系統類型；
- 瞭解允許的不同作業，以及如何建立它們。

一旦匯入 Interface，Wallet 就能正確顯示 Contract，並向使用者提出互動建議。

### LNP/BP 協會標準化的介面

在 RGB 生態系統中，Interface 用來賦予 Contract 的資料和操作可讀和可操作的意義。因此，Interface 是 Schema 的補充，Schema 在內部描述 Business Logic（嚴格類型、驗證腳本等）。在本節中，我們將檢視 LNP/BP 協會針對常見 Contract 類型 (可替代代幣、NFT 等) 所開發的標準介面。

提醒一下，我們的想法是每個 Interface 描述如何在 Wallet 側顯示和操作 Contract，清楚命名欄位 (例如 `spec`、`ticker`、`issuedSupply`...) 並定義可能的操作 (例如 `Transfer`、`Burn`、`Rename`...)。有幾個介面已經開始運作，但未來還會有更多。

#### 一些即時可用的介面

**RGB20** 是可替代資產的 Interface，可與 Ethereum 的 ERC20 標準相提並論。然而，它更進一步，提供更廣泛的功能：


- 例如，資產發行後可以重新命名（變更*標籤*或全名），或調整其精確度（*股票分割*）；
- 它也可以描述二次再發行 (有限或無限) 以及先燒毀再置換的機制，以授權發行者在特定情況下銷毀資產，然後再重新製造資產；

舉例來說，RGB20 Interface 可連結至 **Non-Inflatable Asset (NIA) 方案**，該方案會強加一個不可充氣的初始 Supply，或依需要連結至其他更進階的方案。

**RGB21** 關係到 NFT 類合約，或更廣泛而言，任何獨特的數位內容，例如數位媒體 (影像、音樂等) 的表達。除了描述單一資產的發行和轉讓外，它還包括以下特點：......：


- 整合支援在 Contract 中直接包含檔案（最多 16 MB）（用於用戶端擷取）；
- 物主可在歷史中輸入「*雕刻*」，以證明 NFT 過去的 Ownership。

**RGB25** 是一種混合標準，結合了可替代與不可替代的層面。它專為部分可替代資產所設計，例如不動產代用化，您想要分割財產，同時保留與單一根資產的連結 (換句話說，您有一棟房子的可替代部分，連結到一棟不可替代的房子)。技術上來說，此 Interface 可與 **Collectible Fungible Asset* (CFA)** Schema 相關聯，此 Schema 考慮到分割的概念，同時追溯原始資產。

#### 開發中的介面

為了更專門的用途，還規劃了其他介面，但目前尚未推出：


- RGB22**，專門用於數位身分，以管理 RGB 生態系統中的識別碼和 On-Chain 設定檔；
- RGB23**，用於進階時間戳記，使用 *Opentimestamps* 的某些構想，但具有可追蹤功能；
- RGB24**，其目的是建立一個類似於 *Ethereum Name Service* 的去中心化域名系統 (DNS)；
- RGB26**, 旨在以更複雜的格式 (治理、投票等) 管理 DAOs (*分散式自治組織*)；
- RGB30**，與 RGB20 非常相似，但其特點是考慮到分散的初始發行和使用國家擴展。這將用於由多個實體管理再發行或受更精細條件限制的資產。

當然，視您諮詢本課程的日期而定，這些介面可能已經可以運作和存取。

#### Interface 範例

此 Rust 程式碼片段顯示 [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface (可替代資產)。這段程式碼來自標準 RGB 程式庫中的「rgb20.rs」檔案。讓我們來看看它，以瞭解 Interface 的結構，以及它如何在 Business Logic（在 Schema 中定義）與暴露給錢包和使用者的功能之間提供橋樑。

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

在這個 Interface 中，我們注意到與 Schema 結構的相似之處：我們找到 Global State、Owned States、Contract Operations（Genesis 和 Transitions）的聲明，以及錯誤處理。但 Interface 著重於 Wallet 或任何其他應用程式對這些 Elements 的呈現和操作。

與 Schema 的差異在於類型的性質。Schema 使用嚴格的類型 (例如 `FungibleType::Unsigned64Bit`)，以及更具技術性的識別碼。Interface 使用欄位名稱、巨集 (`fname!()`、`tn!()`)，以及對參數類別的引用 (`ArgSpec`、`OwnedIface::Rights`...)。這裡的目的是方便 Elements 對 Wallet 的功能理解和組織。

此外，Interface 可以為基本的 Schema 引進額外的功能 (例如管理 `burnEpoch` 權限)，只要這與最終驗證的用戶端邏輯保持一致即可。Schema 中的 AluVM 「腳本」部分將確保加密的有效性，而 Interface 則描述使用者 (或 Wallet) 如何與這些狀態和轉換進行互動。

#### Global State 和分配

在 `global_state` 區段中，我們可以找到 `spec`（資產描述）、`data`、`created`、`issuedSupply`、`burnedSupply`、`replacedSupply` 等欄位。這些都是 Wallet 可以讀取並呈現的欄位。舉例來說


- `spec` 將顯示標記設定；
- `issuedSupply` 或 `burnedSupply` 會給我們已發行或已燒毀的代幣總數，等等。

在 `assignments` 區段中，我們定義了各種角色或權限。例如：


- `assetOwner` 對應於代幣的持有（它是可替代的 *Owned State*）；
- `burnRight`對應於燒掉代幣的能力；
- updateRight` 對應於重新命名資產的權利。

public`或`private`關鍵字（例如 `AssignIface::public(...)`）表示這些狀態是可見的（`public`）或保密的（`private`）。至於 `Req::NoneOrMore`、`Req::Optional`，則表示預期出現的情況。

#### Genesis 和過渡

Genesis ` 部分說明如何初始化資產：


- spec`、`data`、`created`、`issuedSupply` 欄位是必須填寫的 (`ArgSpec::required()`)；
- Assignments 例如 `assetOwner` 可以存在於多個副本 (`ArgSpec::many()`)，允許代幣分發給多個初始持有人；
- inflationAllowance」或「burnEpoch」等欄位可能會 (也可能不會) 包含在 Genesis 中。

然後，對於每個轉換 (`Transfer`、`Issue`、`Burn`...)，Interface 定義了該作業期望哪些欄位作為輸入、該作業將產生哪些欄位作為輸出，以及可能發生的任何錯誤。例如

**Transition :**


- 輸入 : `previous` → 必須是一個 `assetOwner` ；
- 指派： `beneficiary` → 將成為新的 `assetOwner` ；
- Error: `NON_EQUAL_AMOUNTS` (Wallet 因此能夠處理輸入總和與輸出總和不一致的情況)。

**Transition `Issue` :**


- 可選 (`optional:true`)，因為額外的排放不一定會啟動；
- 輸入：`used` → `inflationAllowance`, 即增加更多代幣的權限 ；
- 指派：beneficiary`（收到的新代用幣）和`future`（剩餘的`inflationAllowance`） ；
- 可能的錯誤：SUPPLY_MISMATCH`、`ISSUE_EXCEEDS_ALLOWANCE` 等。

**Burn transition :**


- 輸入： `used` → a `burnRight` ；
- Globals : `burnedSupply` required ；
- 指派：`future` → `burnRight` 的可能延續，如果我們還沒燒完所有東西 ；
- 錯誤：`supply_mismatch`、`invalid_proof`、`insufficient_coverage`。

因此，每個操作都會以 Wallet 可讀的方式描述。這使得圖形化的 Interface 可以顯示在使用者可以清楚看到的地方："您有燒錄的權利。您想燒掉某個數量嗎？程式碼知道要填入 `burnedSupply` 欄位，並檢查 `burnRight` 是否有效。

總括來說，重要的是要記住，Interface 無論多麼完整，其本身並不能定義 Contract 的內部邏輯。核心的工作是由 **Schema**完成的，其中包括嚴格的類型、Genesis 結構、轉換等等。Interface 只是將這些 Elements 以更直覺和命名的方式呈現出來，供應用程式使用。

由於 RGB 的模組化特性，Interface 可以進行升級 (例如，增加 `Rename` 轉換、修正欄位顯示等)，而無需重寫整個 Contract。此 Interface 的使用者只要更新`.RGB`或`.rgba`檔，就能立即受惠於這些改進。

但是一旦您宣告了 Interface，您就需要將它連結到對應的 Schema。這是透過 ***Interface Implementation*** 來完成的，它會指定如何將每個命名欄位 (例如 `fname!("assetOwner")`) 對應到 Schema 中定義的嚴格 ID (例如 `OS_ASSET`)。舉例來說，這可確保當 Wallet 操作`burnRight`欄位時，這是 Schema 中描述燒錄代幣能力的狀態。

### Interface Implementation

在 RGB 架構中，我們看到每個元件 (Schema、Interface 等) 都可以獨立開發與編譯。然而，仍有一個不可或缺的元素將這些不同的元件連結在一起：***Interface Implementation***。這就是將 Schema (在 Business Logic 方面) 中定義的識別碼或欄位，明確地對應到 Interface (在呈現與使用者互動方面) 中宣告的名稱。因此，當 Wallet 載入 Contract 時，它可以清楚瞭解哪個欄位對應什麼，以及 Interface 中的操作名稱與 Schema 的邏輯有何關聯。

重要的一點是，Interface Implementation 不一定要揭露所有的 Schema 功能，也不一定要揭露所有的 Interface 欄位：它可以被限制為一個子集。實際上，這使得限制或過濾 Schema 的某些方面成為可能。例如，您可以有一個有四種操作類型的 Schema，但實作 Interface 在給定的上下文中只對應其中兩種。相反地，如果 Interface 提出其他端點，我們可以選擇不在此實作。

這裡有一個 Interface Implementation 的經典範例，我們將一個 *Non-Inflatable Asset* (NIA) Schema 與 RGB20 Interface 相關聯：

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

在此實作中，Interface ：


- 我們透過 `nia_schema()` 明確引用 Schema，透過 `Rgb20::iface()` 明確引用 Interface。調用 `Schema.schema_id()` 和 `iface.iface_id()` 用來在編譯端 Anchor Interface Implementation（這會關聯這兩個元件的加密識別碼）；
- Schema Elements 與 Interface Elements 之間建立了映射。例如，Schema 中的「GS_NOMINAL」欄位會連結到 Interface 側的字串「spec」(「NamedField::with(GS_NOMINAL, fname!("spec") `)。我們對操作也做同樣的處理，例如 `TS_TRANSFER`，我們將它連結到 Interface 中的 `"Transfer"`...；
- 我們可以看到沒有 valencies (`valencies:none!()`)或 extensions (`extensions:none!()`)，反映出這個 NIA Contract 並沒有使用這些功能。

編譯後的結果是一個獨立的「.RGB」或「.rgba」檔案，除了 Schema 和 Interface 外，還要匯入 Wallet。因此，軟體知道如何將這個 NIA Contract（其邏輯由其 Schema 描述）具體連結到「RGB20」Interface（提供人類名稱和可替代代幣的互動模式），應用這個 Interface Implementation 作為兩者之間的閘道。

#### 為什麼要分開 Interface Implementation？

分離可提高彈性。單一的 Schema 可以有多個不同的 Interface 實作，每個實作映射不同的功能。更重要的是，Interface Implementation 本身可以演進或重寫，而不需要改變 Schema 或 Interface。這保留了 RGB 的模組化原則：每個元件 (Schema、Interface、Interface Implementation) 都可以獨立進行版本控制與更新，只要遵守協定所強制的相容性規則 (相同的識別碼、類型的一致性等)。

在具體使用中，當 Wallet 載入 Contract 時，必須 ：


- 載入已編譯的 **Schema**（了解 Business Logic 的結構）；
- 載入已編譯的 **Interface**（了解名稱和使用者端操作） ；
- 載入已編譯的 **Interface Implementation**（將 Schema 邏輯與 Interface 名稱連結，逐一操作，逐一欄位）。

此模組化架構使 .NET 等使用情境成為可能：


- 限制特定使用者的特定操作：例如，提供只提供基本傳輸存取權限的部分實作 Interface，而不提供燒錄或更新功能；
- 變更呈現：設計一個 Interface Implementation，重新命名 Interface 中的欄位或以不同方式映射，但不改變 Contract 的基礎；
- 支援多種方案：只要結構相容，Wallet 可以為相同的 Interface 類型載入多個 Interface 實作，以處理不同的方案 (不同的符記邏輯)。

在下一章中，我們將探討 Contract 轉帳如何運作，以及 RGB 發票如何產生。

## Contract 轉讓

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::

在本章中，我們將分析 RGB 生態系統中的 Contract 轉移過程。為了說明這一點，我們將看一下 Alice 和 Bob，我們通常的主角，他們希望 Exchange 一個 RGB 資產。我們也會展示一些 `RGB`命令列工具的命令摘錄，看看它實際上是如何運作的。

### 瞭解 RGB Contract 轉移

讓我們以 Alice 和 Bob 之間的轉移為例。在這個範例中，我們假設 Bob 剛開始使用 RGB，而 Alice 已經在她的 Wallet 中持有 RGB 資產。我們會看到 Bob 如何設定他的環境、匯入相關的 Contract，然後向 Alice 請求轉移，最後 Alice 如何在 Bitcoin Blockchain 上執行實際交易。

#### 1) 安裝 RGB Wallet

首先，Bob 需要安裝 RGB Wallet，也就是與協定相容的軟體。這一開始並不包含任何合約。鮑勃還需要.NET：


- A Bitcoin Wallet 來管理您的 UTXO；
- 與 Bitcoin 節點 (或 Electrum 伺服器) 連線，以便您可以識別您的 UTXO，並在網路上傳播您的交易。

提醒一下，RGB 中的 **Owned State** 指的是 Bitcoin UTXOs。因此，我們必須始終能夠在包含指向 RGB 資料的加密承諾 (「Tapret」或「Opret」) 的 Bitcoin 交易中管理和花費 UTXO。

#### 2) Contract 資訊取得

Bob 接著需要擷取他感興趣的 Contract 資料。這些資料可以透過任何管道流通：網站、電子郵件、訊息應用程式...等。實際上，這些資料會以 ***Consignment*** 組合起來，也就是包含 ：


- **Genesis**，定義 Contract 的初始狀態；
- **Schema**，說明 Business Logic（嚴格類型、驗證腳本等）；
- **Interface**，定義呈現 Layer（欄位名稱、可存取的操作）；
- **Interface Implementation**，具體連結 Schema 與 Interface。

![RGB-Bitcoin](assets/fr/075.webp)

由於每個元件的重量通常少於 200 位元組，因此總大小通常為幾千位元組。也有可能在 Base58 中透過抗檢查頻道 (例如 Nostr 或透過 Lightning Network) 廣播此 Consignment，或以 QR 碼的形式廣播。

#### 3) Contract 匯入與驗證

鮑勃收到 Consignment 後，會將它匯入他的 RGB Wallet。這將......：


- 檢查 Genesis 和 Schema 是否有效；
- 載入 Interface 和 Interface Implementation ；
- 更新您的用戶端資料 Stash。

鮑勃現在可以在他的 Wallet 中看到資產（即使他還未擁有它），並瞭解哪些欄位可用、哪些操作是可能的...然後，他需要聯絡實際擁有要轉移資產的人。在我們的範例中，這個人就是 Alice。

發現誰持有某項 RGB 資產的過程與尋找 Bitcoin 付款人的過程相似。此連結的細節取決於用途（市集、私人聊天頻道、發票、銷售商品與服務、薪資...）。

#### 4) 發出 Invoice

要啟動 RGB 資產轉移，Bob 必須先簽發 Invoice。此 Invoice 用於 ：


- 告訴 Alice 要執行的作業類型 (例如，從 RGB20 Interface `Transfer`)；
- 向 Alice 提供 Bob 的 *Seal Definition*（即他希望接收資產的 UTXO）；
- 指定所需的活性成分數量（例如 100 個單位）。

Bob 在命令列上使用 `RGB` 工具。假設他想要 100 個單位的代幣，其 `ContractId` 已知，想要依賴 `Tapret`，並指定其 UTXO (`456e3..dfe1:0`) ：

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

在本章的最後，我們將進一步了解 RGB 發票的結構。

#### 5) Invoice 傳輸

生成的 Invoice（例如 URL：`RGB:2WBcas9.../RGB20/100+utxob:...`）包含 Alice 準備傳輸所需的所有資訊。與 Consignment 一樣，它可以精簡地編碼 (Base58 或其他格式)，並透過訊息應用程式、電子郵件、Nostr... 傳送。

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Alice 方面的交易準備

Alice 收到 Bob 的 Invoice。在她的 RGB Wallet 中，有一個 Stash 包含要轉移的資產。要使用包含該資產的 UTXO 時，她必須先 generate 一個 PSBT (*Partially Signed Bitcoin Transaction*)，也就是使用她所擁有的 UTXO 進行不完整的 Bitcoin 交易：

```bash
alice$ wallet construct tx.psbt
```

此基本交易（暫未簽署）將用於與轉帳給鮑勃相關聯的加密 Anchor Commitment。Alice 的 UTXO 將因此花掉，而在輸出中，我們將為 Bob 放置 `Tapret` 或 `Opret` Commitment。

#### 7) 產生轉移 Consignment

接下來，Alice 會透過 ：

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

這個新的 `Consignment.RGB` 檔案包含 ：


- 到目前為止（自 Genesis 以來）驗證資產所需的完整「國家轉移」歷史；
- 根據 Bob 發出的 Invoice 將資產從 Alice 轉移給 Bob 的新 State Transition；
- 不完整的 Bitcoin 交易 (*Witness Transaction*) (`tx.PSBT`)，花費了 Alice 的 Single-Use Seal，修改為包含給 Bob 的加密 Commitment。

在此階段，交易尚未在 Bitcoin 網路上廣播。Consignment 比基本的 Consignment 更大，因為它包含了整個歷史記錄 (*proof chain*)，以證明資產的合法性。

#### 8) Bob 檢查並接受 Consignment

Alice 將此 **Terminal Consignment** 傳送給 Bob。然後，Bob 將 ：


- 檢查 State Transition 的有效性（確保歷史一致、遵守 Contract 規則等）；
- 將其加入您當地的 Stash；
- 可能是 generate Consignment 上的簽名 (`sig:...`)，以證明已審核通過（有時稱為「*薪資單*」）。

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9)選項：Bob 將確認發送回 Alice (* 付費單*)

如果 Bob 希望，他可以將此簽章傳回給 Alice。這表示


- 它承認過渡是有效的；
- 他同意廣播 Bitcoin 交易。

這並非強制性的，但可以為 Alice 提供保證，不會有後續的轉讓爭議。

#### 10) Alice 簽署並發佈交易

然後，Alice 可以 ：


- 檢查 Bob 的簽名 (`RGB check <sig>`) ；
- 簽署 *Witness Transaction* 仍是 PSBT (`Wallet簽署`) ；
- 在 Bitcoin 網路上發佈 Witness Transaction (`-publish`)。

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

一經確認，此交易即標誌著轉讓的結束。Bob 成為資產的新擁有者：他現在有一個 Owned State 指向他控制的 UTXO，交易中 Commitment 的出現證明了這一點。

總括而言，以下是完整的轉移程序：

![RGB-Bitcoin](assets/fr/079.webp)

### RGB 轉移的優勢


- 保密性** ：

只有 Alice 和 Bob 可以存取所有 State Transition 資料。他們在 Blockchain 外部透過託管方式 Exchange 這些資訊。Bitcoin 交易中的加密承諾不會透露資產類型或金額，這保證了遠高於其他 On-Chain 代幣系統的保密性。


- 客戶端驗證** ：

Bob 可以透過比較 *Consignment* 與 Bitcoin Blockchain 中的 *anchors* 來檢查傳輸的一致性。他不需要第三方驗證。Alice 不需要在 Blockchain 上公佈完整的歷史記錄，這可以減少基本通訊協定的負載，並提高保密性。


- 簡化原子性** ：

複雜的交換（例如 BTC 與 RGB 資產之間的原子交換）可以在單一交易中進行，避免使用 HTLC 或 PTLC 腳本。如果協議沒有廣播，每個人都可以其他方式重複使用他們的 UTXO。

### 轉移摘要圖

在詳細瞭解發票之前，這裡有一個 RGB 轉帳整體流程的摘要圖表：


- Bob 安裝 RGB Wallet 並取得初始 Contract Consignment；
- Bob 發出 Invoice，提及接收資產的 UTXO；
- Alice 接收 Invoice、建立 PSBT 並產生 Terminal Consignment；
- 鮑勃接受、檢查、將資料加入他的 Stash，並在必要時簽名（*付款單*）；
- Alice 在 Bitcoin 網路上公佈交易；
- 交易確認後，轉帳才算正式完成。

![RGB-Bitcoin](assets/fr/080.webp)

這項轉移說明了 RGB 通訊協定的所有威力與彈性：在客戶端驗證的私有 Exchange，以最小且隱密的方式錨定在 Bitcoin Blockchain 上，並保留該通訊協定的最佳安全性 (沒有 Double-spending 的風險)。這使得 RGB 成為一個很有前途的價值轉移生態系統，比 On-Chain 可程式化區塊鏈更具機密性和可擴展性。

### 發票 RGB

在本節中，我們將詳細解釋**發票**如何在 RGB 生態系統中運作，以及如何使用 Contract 進行操作（特別是轉帳）。首先，我們將檢視所使用的識別碼，然後檢視它們是如何編碼的，最後檢視以 URL 表示的 Invoice 結構（這種格式在錢包中使用非常方便）。

#### 識別碼和編碼

以下每個 Elements 定義了唯一的識別碼：


- An RGB Contract；
- 其 Schema (Business Logic) ；
- 其 Interface 和 Interface Implementation ；
- 其資產（代幣、NFT 等）、

這種唯一性非常重要，因為系統的每個元件都必須能夠區分。例如，一個 Contract X 不能與另一個 Contract Y 混淆，兩個不同的介面（例如 RGB20 對 RGB21）必須有不同的識別碼。

為了讓這些識別碼既有效率（小尺寸）又可讀，我們使用 .NET 技術：


- Base58 編碼，可避免使用容易混淆的字元（例如 `0` 和字母 `O`），並提供相對較短的字串；
- 表示識別符性質的前綴，通常以 `RGB:` 或類似的 URN 形式表示。

例如，`ContractId` 可以用類似 ：

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

RGB:` 前綴確認這是一個 RGB 識別碼，而不是 HTTP 連結或其他協定。有了這個前綴，錢包能夠正確解釋這個字串。

#### 識別碼分割

RGB 識別碼通常相當長，因為底層 (加密) 安全性可能需要 256 位元或更多的欄位。為了方便人類閱讀與驗證，我們將這些字串分割成幾個區塊，並以連字號 (`-`)隔開。因此，我們不再使用一長串、不間斷的字元，而是將它分割成較短的區塊。這種做法在信用卡或電話號碼中很常見，在此也同樣適用，以方便驗證。因此，舉例來說，可以告訴使用者或合作夥伴「*請檢查第三個區塊是 `9GEgnyMj7`*」，而不必一次比較整個區塊。最後一個區塊通常用作**校驗和**，以便有一個錯誤或錯字偵測系統。

舉例來說，以 base58 編碼和分割的 `ContractId` 可以是 ：

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

每個破折號將字串分成幾個部分。這不會影響程式碼的語意，只會影響其表達方式。

#### 將 URL 用於發票

RGB Invoice 以 URL 的形式顯示。這表示可以點選或掃描（如同 QR 代碼），Wallet 就可以直接解讀它來進行交易。這種簡單的互動方式不同於其他一些系統，在其他系統中，您必須複製和貼上各種資料到軟體中的不同欄位。

可替代標記（例如 RGB20 標記）的 Invoice 可能如下所示：

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

讓我們分析一下這個 URL：


- `RGB:`** (前綴): 表示啟用 RGB 通訊協定的連結 (類似於其他上下文中的 `http:` 或 `Bitcoin:`)；
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**：表示您要操作的令牌的`ContractId`；
- `/RGB20/100`**：表示使用 `RGB20` Interface，並要求 100 單位的資產。語法為`/Interface/amount` ；
- `+utxob:`**:指定加入收件人 UTXO 的資訊 (或更精確地說，Single-Use Seal 的定義)；
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**：這是 *blinded* UTXO（或 Seal Definition）。換句話說，Bob 隱藏了他確切的 UTXO，所以寄件者 (Alice) 不知道確切的 Address 是什麼。她只知道有一個有效的 Seal 指的是由 Bob 控制的 UTXO。

事實上，所有功能都可整合到單一 URL 中，讓使用者的生活更輕鬆：只需在 Wallet 中輕輕一按或掃描，即可執行操作。

我們可以想像使用簡單的剔號 (例如 `USDT`)來取代 `ContractId` 的系統。然而，這將會引起重大的信任與安全問題：剔號並非唯一的參考（好幾個契約都可能聲稱自己稱為 `USDT`）。對於 RGB，我們需要一個唯一、無歧義的加密識別碼。因此，我們採用 256 位元的字串，以 base58 編碼並分割。使用者知道他正在操作的正是 ID 為 `2WBcas9-yjz...` 的 Contract，而不是其他。

#### 額外的 URL 參數

您也可以在 URL 中加入額外的參數，方式與 HTTP 相同，例如 ：

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`：例如，代表與 Invoice 相關的簽章，某些錢包能夠驗證；
- 如果 Wallet 不管理此簽章，則會直接忽略此參數。

讓我們以透過 RGB21 Interface 的 NFT 為例。例如，我們可以有 ：

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

在這裡我們看到：


- `RGB:`**：URL 前綴 ；
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**：Contract ID (NFT) ；
- rGB21**：Interface 適用於不可偽造資產 (NFT) ；
- `DbwzvSu-4BZU81jEp-...`**：對 NFT 唯一部分的明確引用，例如資料 Blob（媒體、元資料...）的 Hash ；
- `+utxob:egXsFnw-...`**：Seal Definition。

想法是一樣的：傳輸一個 Wallet 可以解讀的獨特連結，清楚識別要傳輸的獨特資產。

#### 透過 URL 進行其他操作

RGB URL 不只是用來要求傳輸。它們也可以編碼更先進的操作，例如發行新的代幣 (*issuance*)。舉例來說

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

在這裡我們發現：


- RGB:` : protocol ；
- `2WBcas9-...`：Contract ID ；
- `/RGB20/issue/100000`：表示要調用「*Issue*」轉換來建立額外 100,000 個代幣；
- `+utxob:`：Seal Definition。

例如，Wallet 可能會寫道："I have been asked to carry out an `issue` operation from the `RGB20` Interface, on such and such a Contract, for 100,000 units, for the benefit of such and such a Single-Use Seal.*."

現在我們已經瞭解了 RGB 程式設計的主要 Elements，接下來我將帶您了解如何繪製 RGB Contract 的章節。

## 草擬智慧型契約

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::

在本章中，我們將採用命令列工具 `RGB`，逐步編寫 Contract。目的是展示如何安裝和操作 CLI、編譯 **Schema**、匯入 **Interface**和 **Interface Implementation**，然後發行 (*issue*) 資產。我們還會瞭解底層邏輯，包括編譯和狀態驗證。在本章結束時，您應該可以重現流程並建立自己的 RGB 契約。

提醒您，RGB 的內部邏輯是以 Rust 函式庫為基礎，身為開發人員的您可以將這些函式庫匯入您的專案中，以管理 Client-side Validation 的部分。此外，LNP/BP 協會團隊正在研究其他語言的綁定，但尚未定案。此外，Bitfinex 等其他實體也在開發自己的整合堆疊（我們會在課程的最後 2 章談到這些）。因此，就目前而言，"RGB "CLI 是官方參考，即使它仍然相對未經完善。

### 安裝和展示 RGB 工具

主指令簡稱為「RGB」。它的設計讓人聯想到 `git`，有一組子指令用來操作契約、呼叫契約、發行資產等等。Bitcoin Wallet 目前尚未整合，但會在即將推出的版本 (0.11) 中整合。這個下一個版本將能讓使用者直接從 `RGB`建立和管理他們的錢包 (透過描述符)，包括 PSBT 的產生、與外部硬體 (例如 Hardware Wallet) 的相容性以進行簽章，以及與 Sparrow 等軟體的互通性。這將簡化整個資產發行與轉移的情境。

#### 透過貨運安裝

我們在 Rust 中安裝了 .NET 工具：

```bash
cargo install rgb-contracts --all-features
```

(注意：crate 名為 `RGB-contracts`，安裝的指令將命名為 `RGB`。如果已存在名為 `RGB` 的 crate，可能會發生碰撞，因此才會有這個名稱)

安裝過程中會編譯大量的相依性（例如指令解析、Electrum 整合、零知識證明管理等）。

安裝完成後，.NET 會自動啟動：

```bash
rgb
```

執行 `RGB`（不含參數）會顯示可用的子指令清單，例如 `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer` 等。您可以變更本機儲存目錄 (存放所有記錄、示意圖與實作的 Stash)、選擇網路 (Testnet、Mainnet) 或設定您的 Electrum 伺服器。

![RGB-Bitcoin](assets/fr/081.webp)

#### 控制的第一次概述

執行下列指令時，您會看到預設已整合了一個 `RGB20` Interface：

```bash
rgb interfaces
```

如果未整合此 Interface，請克隆 .NET Framework：

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

編譯它：

```bash
cargo run
```

然後匯入您選擇的 Interface：

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

另一方面，我們被告知尚未有 Schema 匯入軟體中。Stash 中也沒有 Contract。若要查看，請執行命令 ：

```bash
rgb schemata
```

然後，您可以複製儲存庫以擷取某些示意圖：

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

此儲存庫在其 `src/` 目錄中包含數個 Rust 檔案 (例如 `nia.rs`)，這些檔案定義模式 (NIA 代表 "*Non Inflatable Asset*「，UDA 代表 」*Unique Digital Asset*"，等等)。若要編譯，您可以執行 ：

```bash
cd rgb-schemata
cargo run
```

這會產生數個與已編譯示意圖相對應的「.RGB」和「.rgba」檔案。例如，您會找到 `NonInflatableAsset.RGB`。

#### 導入 Schema 和 Interface Implementation

現在您可以將原理圖匯入 `RGB` 中：

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

這會將它加入本機的 Stash。如果我們執行以下指令，就會發現 Schema 現在出現了：

```bash
rgb schemata
```

### 創建 Contract（發行）

有兩種方法可以建立新資產：


- 我們可以使用 Rust 中的腳本或程式碼，透過填入 Schema 欄位 (Global State、自有國家等) 來建立 Contract，並產生`.RGB`或`.rgba`檔；
- 或直接使用 `issue` 子指令，並使用 YAML (或 TOML) 檔描述 token 的屬性。

您可以在 Rust 的 `examples` 資料夾中找到範例，這些範例說明您如何建立一個 `ContractBuilder `、填入 `Global State`（資產名稱、股票代號、Supply、日期等）、定義 Owned State（指派給哪個 UTXO），然後將所有這些編譯成 *Contract Consignment*，您就可以匯出、驗證並匯入 Stash。

另一種方法是手動編輯 YAML 檔案，自訂 `ticker`、`name`、`Supply` 等。假設檔案名稱為 `RGB20-demo.yaml`。您可以指定 ：


- `spec`：股票代號、名稱、精確度 ；
- `條款'：一個用於法律通知的欄位 ；
- `issuedSupply` : 已發行的代幣數量 ；
- `assignments`: 表示 Single-Use Seal (*Seal Definition*) 和已解鎖的數量。

以下是要建立的 YAML 檔案範例：

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

然後只要執行指令 ：

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

在我的案例中，唯一的 Schema 識別碼 (需用單引號括起）是 `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` 而且我沒有輸入任何發行商。所以我的訂單是 ：

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

如果您不知道 Schema ID，請執行命令 ：

```bash
rgb schemata
```

CLI 回覆說新的 Contract 已經發出並加入 Stash。如果我們鍵入以下指令，我們會看到現在有一個額外的 Contract，對應剛剛發出的 Contract：

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

接著，下一個指令會顯示全局狀態 (名稱、股票、Supply...) 和 Owned 狀態清單，也就是分配 (例如，在 UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1` 中定義的 100 萬個 `PBN` 代幣)。

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### 匯出、匯入及驗證

若要與其他使用者分享此 Contract，可從 Stash 匯出至 .NET 檔案：

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

可以將 `myContractPBN.RGB` 檔案傳給其他使用者，他可以使用命令 ：

```bash
rgb import myContractPBN.rgb
```

匯入時，如果是簡單的 *Contract Consignment*，我們會收到「`Importing Consignment RGB`」訊息。如果是較大的 *State Transition Consignment*，指令會有所不同 (`RGB接受`)。

為了確保有效性，您也可以使用本機驗證功能。例如，您可以執行 ：

```bash
rgb validate myContract.rgb
```

#### Stash 的使用、驗證和顯示

提醒一下，Stash 是模式、介面、實作和契約（Genesis + 轉換）的本地庫存。每次執行「匯入」，都會新增一個元素到 Stash。這個 Stash 可以用命令 ：

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

這將 generate 一個資料夾，其中包含整個 Stash 的詳細資訊。

### 轉移和 PSBT

若要執行轉移，您需要操作本機 Bitcoin Wallet 來管理「Tapret」或「Opret」承諾。

#### generate 和 Invoice

在大多數情況下，Contract 的參與者 (例如 Alice 和 Bob) 之間的互動是透過產生 Invoice 來進行的。如果 Alice 想要 Bob 執行某些事情 (代幣轉移、重新發行、DAO 中的動作等)，Alice 會建立一個 Invoice 詳細說明她對 Bob 的指示。因此我們有 ：


- Alice** （Invoice 的發行者） ；
- Bob** (接收並執行 Invoice)。

與其他生態系統不同，RGB Invoice 並不局限於付款的概念。它可以嵌入任何與 Contract 相關聯的請求：撤銷金鑰、投票、在 NFT 上建立雕刻 (*engraving*) 等。相應的操作可以在 Contract Interface 中描述。相應的操作可以在 Contract Interface 中描述。

以下指令會產生 RGB Invoice：

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

與 ：


- `$Contract`：Contract 識別碼 (*ContractId*) ；
- `$Interface`：要使用的 Interface（例如：`RGB20`） ；
- `$ACTION`：Interface 中指定的操作名稱（對於簡單的可替代代幣轉移，可以是「轉移」）。如果 Interface 已經提供預設動作，則無需在此再次輸入；
- `$STATE`：要轉移的狀態資料（例如，如果轉移的是可替代代幣，則是代幣的數量）；
- `$Seal`：受益人（Alice）的 Single-Use Seal，即對 UTXO 的明確引用。Bob 將使用此資訊建立 Witness Transaction，而相對應的輸出就會屬於 Alice (以 *blinded UTXO* 或未加密的形式)。

例如，使用下列指令

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI 將 generate 與 Invoice 相似 ：

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

它可以透過任何管道 (文字、QR code 等) 傳送給 Bob。

#### 進行轉移

要從此 Invoice ：


- 鮑勃（在他的 Stash 中持有代幣）有一個 Bitcoin Wallet。他需要準備一個 Bitcoin 交易（以 PSBT 的形式，例如 `tx.PSBT`），花掉所需的 RGB 代幣所在的 UTXO，再加上一個 UTXO 作為貨幣 (Exchange) ；
- Bob 執行下列指令：

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- 這會產生一個 `Consignment.RGB` 檔案，其中包含 ：
 - 轉換歷史向 Alice 證明代用幣是真的；
 - 將代幣轉移到 Alice 的 Single-Use Seal 的新轉換；
 - A Witness Transaction（未簽名）。
- Bob 將這個`Consignment.RGB`檔傳送給 Alice（透過電子郵件、分享伺服器或 RGB-RPC 通訊協定、Storm 等）；
- Alice 接收 `Consignment.RGB` 並接受它自己的 Stash ：

```bash
alice$ rgb accept consignment.rgb
```


- CLI 會檢查轉換的有效性，並將其加入 Alice 的 Stash。如果無效，指令會失敗，並附有詳細的錯誤訊息。否則，它會成功，並報告樣本交易尚未在 Bitcoin 網路上廣播（Bob 正在等待 Alice 的 Green 亮起）；
- 作為確認的方式，`accept` 指令會傳回一個簽章 (*payslip*)，Alice 可以將這個簽章傳送給 Bob，讓他知道她已經驗證了 *Consignment* ；
- 鮑勃就可以簽署並發佈 (`--publish`)他的 Bitcoin 交易：

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- 此交易一經 On-Chain 確認，資產的 Ownership 即視為轉移給 Alice。Alice 的 Wallet 監控交易的 Mining，看到新的 Owned State 出現在其 Stash 中。

在下一章中，我們將進一步了解如何將 RGB 整合到 Lightning Network 中。

## Lightning Network 上的 RGB

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::

在本章中，我建議檢視如何在 Lightning Network 中使用 RGB，透過 off-chain 付款管道整合並移動 RGB 資產 (代幣、NFT 等)。

基本的想法是，RGB State Transition (*State Transition*) 可以委託給 Bitcoin 交易，而 Bitcoin 交易又可以保持 off-chain，直到 Lightning 通道關閉為止。因此，每次更新通道時，都可以將新的 RGB State Transition 納入新的提交交易，然後使舊的轉換失效。如此一來，Lightning 通道就能用來轉移 RGB 資產，並能以與傳統 Lightning 付款相同的方式進行路由。

### 頻道建立與資金

若要建立載有 RGB 資產的 Lightning 通道，我們需要兩個 Elements：


- Bitcoin 資金，以建立頻道的 2/2 Multisig（頻道的基本 UTXO）；
- RGB 資金，將資產送至相同的 Multisig。

以 Bitcoin 來說，資金交易必須存在，以定義參考 UTXO，即使它只包含少量的 Sats（這只是未來 Commitment 交易中的每個輸出都一樣保持在 Dust 限制之上的問題）。例如，Alice 可能決定提供 10k Sats 和 500 USDT（作為 RGB 資產發行）。在資金交易中，我們會加入一個 Commitment (`Opret`或`Tapret`)，錨定 RGB State Transition。

![RGB-Bitcoin](assets/fr/091.webp)

一旦準備好融資交易（但尚未廣播），就會建立 Commitment 交易，以便任何一方可以隨時單方面關閉通道。這些交易類似 Lightning 的經典 Commitment 交易，只是我們增加了一個額外的輸出，包含與新 State Transition 相連的 RGB Anchor (OP_RETURN 或 Taproot)。

然後 RGB State Transition 將資金的 2/2 Multisig 的資產移至 Commitment Transaction 的輸出。這個過程的優點在於 RGB 狀態的安全性完全符合 Lightning 的懲罰機制：如果 Bob 廣播舊的通道狀態，Alice 可以懲罰他並花費輸出，以收回 Sats 和 RGB 代幣。因此，這種誘因比沒有 RGB 資產的 Lightning 通道還要強烈，因為攻擊者不僅會失去 Sats，也會失去通道的 RGB 資產。

因此，由 Alice 簽署並傳送給 Bob 的 Commitment Transaction 會是這樣：

![RGB-Bitcoin](assets/fr/092.webp)

由 Bob 簽署並發送給 Alice 的 Commitment Transaction 會是這樣：

![RGB-Bitcoin](assets/fr/093.webp)

### 頻道更新

當兩個通道參與者之間發生付款（或他們希望變更資產分配）時，他們會建立一對新的 Commitment 交易。每個輸出的 Sats 中的金額可能保持不變，也可能保持不變，視實作而定，因為其主要作用是允許建立有效的 UTXO。另一方面，OP_RETURN（或 Taproot）輸出必須修改，以包含新的 RGB Anchor，代表通道中資產的新分佈。

例如，如果 Alice 在通道中轉帳 30 USDT 給 Bob，新的 State Transition 將反映 Alice 的餘額為 400 USDT，Bob 的餘額為 100 USDT。OP_RETURN/Taproot Anchor 會加入 (或修改) 提交交易，以包含此轉換。請注意，從 RGB 的觀點來看，轉換的輸入仍然是初始 Multisig（On-Chain 資產實際分配至通道關閉為止）。只有 RGB 的輸出 (分配) 會改變，視決定的重新分配而定。

由 Alice 簽署的 Commitment Transaction，準備由 Bob 分發：

![RGB-Bitcoin](assets/fr/094.webp)

由 Bob 簽署的 Commitment Transaction，準備由 Alice 分發：

![RGB-Bitcoin](assets/fr/095.webp)

### HTLC 管理

實際上，Lightning Network 可讓付款透過多個通道，使用 HTLC (*Hashed Time-Locked Contracts*)。RGB 也是一樣：每筆經由通道的付款，都會有一個 HTLC 輸出加入到承諾交易中，並有一個 RGB 分配連結到這個 HTLC。因此，花費 HTLC 輸出的人 (由於秘密或在時間鎖到期後) 可同時收回 Sats 和相關的 RGB 資產。另一方面，您顯然需要有足夠的 Sats 和 RGB 資產現金。

![RGB-Bitcoin](assets/fr/096.webp)

因此，RGB 在 Lightning 上的操作必須與 Lightning Network 本身的操作同步考慮。如果您想深入瞭解這個主題，我強烈建議您看看這另一個全面的訓練課程：

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
### RGB 代碼地圖

最後，在進入下一節之前，我想先為您介紹一下 RGB 所使用的程式碼。協定是基於一套 Rust 函式庫和開放原始碼規格。以下是主要儲存庫和 crates 的概觀：

![RGB-Bitcoin](assets/fr/097.webp)

#### Client-side Validation


- 儲存庫**：[client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crates** ：[client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

管理 off-chain 驗證和一次性使用封條邏輯。

#### 確定性 Bitcoin 承諾 (DBC)


- 儲存庫**：[bp-core](https://github.com/BP-WG/bp-core)
- 木箱**：[BP-DBC](https://crates.io/crates/bp-dbc)

管理 Bitcoin 交易（Tapret、OP_RETURN 等）中的確定性錨定。

#### Multi Protocol Commitment (MPC)


- 儲存庫**：[client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crate** ：[commit_verify](https://crates.io/crates/commit_verify)

多種接合組合，並與不同的通訊協定整合。

#### 嚴格類型與嚴格編碼


- 規格**：[網站 strict-types.org](https://www.strict-types.org/)
- 儲存庫**：[string-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Crates** ：[strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Client-side Validation 使用嚴格的類型系統和確定序列化。

#### RGB 核心


- 儲存庫**：[RGB-core](https://github.com/RGB-WG/RGB-core)
- 箱子**：[RGB-core](https://crates.io/crates/RGB-core)

協定的核心，包含 RGB 驗證的主要邏輯。

#### RGB 標準函式庫 & Wallet


- 儲存庫**：[RGB-std](https://github.com/RGB-WG/RGB-std)
- 箱子** ：[RGB-std](https://crates.io/crates/RGB-std)

標準實作、Stash 和 Wallet 管理。

#### RGB CLI


- 儲存庫**：[RGB](https://github.com/RGB-WG/RGB)
- 木箱**：[RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)

`RGB` CLI 和 crate Wallet，用於命令列操作契約。

#### RGB Schema


- 儲存庫**：[RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)

包含模式 (NIA、UDA 等) 及其實作的範例。

#### AluVM


- 資訊** ：[AluVM.org](https://www.AluVM.org/)
- 儲存庫**：[AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- 箱子**：[AluVM](https://crates.io/crates/AluVM), [aluasm](https://crates.io/crates/aluasm)

基於註冊表的虛擬機器，用於執行驗證指令碼。

#### Bitcoin 協定 - BP


- 儲存庫** ：[bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)

支援 Bitcoin 通訊協定的附加元件 (交易、旁路等)。

#### 無所不在的確定性運算 - UBIDECO


- 儲存庫**：[UBIDECO](https://github.com/UBIDECO)

與開放原始碼決定性開發相連結的生態系統。

# 以 RGB 為基礎

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA 與 Bitmask 專案

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::

本課程的最後一節以 RGB 開始訓練營中各講者的演講為基礎。其中包括對 RGB 及其生態系統的見證與反思，以及基於協定的工具與專案的簡報。第一章由 Hunter Beast 主持，接下來的兩章由 Frederico Tenga 主持。

### 從 JavaScript 到 Rust，再到 Bitcoin 生態系統

起初，Hunter Beast 主要使用 JavaScript 工作。之後，他發現了 **Rust**，一開始這種語言的語法似乎並不吸引人，而且令人沮喪。然而，他逐漸欣賞到這種語言的威力、對記憶體 (*heap* 和 *stack*) 的控制，以及隨之而來的安全性和效能。他強調 Rust 是深入瞭解電腦運作方式的絕佳訓練場地。

Hunter Beast 複述了他在 *Altcoin* 生態系統中各種專案的背景，例如 Ethereum (使用 Solidity、TypeScript 等)，以及後來的 Filecoin。他解釋說，他最初對其中一些協定印象深刻，但最後卻對其中大多數協定感到失望，尤其是因為它們的代幣化（tokenomics）。他譴責這些計畫中可疑的財務誘因、稀釋投資者的代幣膨脹創造，以及潛在的剝削層面。所以他最後採取了**Bitcoin Maximalist**的立場，這不僅是因為有些人讓他看到了Bitcoin更健全的經濟機制，以及這個系統的穩健性。

### RGB 的吸引力與層次建構

用他的話說，讓他確信 Bitcoin 相關性的是 RGB 的發現和層級的概念。他相信，其他區塊鏈上的現有功能可以在 Bitcoin 以上的更高層複製，而不會改變基本協定。

2022 年 2 月，他加入**DIBA**，專門負責 RGB，尤其是**Bitmask**的 Wallet。當時，Bitmask 仍在 0.01 版，並在 0.4 版執行 RGB，僅用於管理單一代用幣。他指出，當時的邏輯部分是以伺服器為基礎，因此比現在較不以自我保管為導向。自此之後，架構朝向這個模式演進，深受比特幣使用者的喜愛。

### RGB 協定的基礎

**RGB**協定是_彩色硬幣_概念的最新、最先進的體現，在 2012-2013 年左右已經開始探索。當時，有幾個團隊希望將不同的 Bitcoin 值與 UTXO 相關聯，這導致了多種分散的實作。由於缺乏標準化，加上當時需求不高，因此這些解決方案無法長久立足。

時至今日，RGB 以其概念上的穩健性和透過 LNP/BP 關聯的統一規格而脫穎而出。其原理以 Client-side Validation 為基礎。Bitcoin Blockchain 只儲存加密承諾（_commitments_，透過 Taproot 或 OP_RETURN），而大部分資料（Contract 定義、傳輸歷史等）則由相關使用者儲存。如此一來，儲存負載便可分散，並可強化資料交換的機密性，而不會加重 Blockchain 的負擔。此方法可在模組化且可擴充的框架內，建立可替代的資產 (**RGB20** 標準) 或獨特的資產 (**RGB21** 標準)。

### 代幣功能 (RGB20) 和獨特資產 (RGB21)

透過 **RGB20**，我們在 Bitcoin 上定義了一個可替代的代幣。發行者選擇一個_supply_、一個_precision_，並建立一個_contract_，然後可以在其中進行轉帳。每筆轉帳都參考 Bitcoin UTXO，UTXO 就像 *Single-Use Seal*。這個邏輯可以確保使用者無法花費相同的資產兩次，因為只有有能力花費 UTXO 的人實際上擁有更新客戶端 Contract 狀態的鑰匙。

**RGB21** 以獨特的資產 (或「NFT」) 為目標。資產的 Supply 值為 1，可與透過特定欄位描述的元資料 (影像檔案、音訊等) 相關聯。與公開區塊鏈上的 NFT 不同，資料及其 MIME 識別碼可以保持私有，由擁有者自行決定進行點對點分發。

### Bitmask 解決方案：RGB 的 Wallet

為了實際利用 RGB 的功能，**DIBA** 專案設計了一個 Wallet 名為 [Bitmask](https://bitmask.app/)。其構想是提供一個非監控、以 Taproot 為基礎的工具，可作為網頁應用程式或瀏覽器擴充套件存取。Bitmask 可管理 RGB20 和 RGB21 資產，並整合各種安全機制：


- 核心程式碼以 Rust 寫成，然後以 WebAssembly 編譯，在 JavaScript 環境 (React) 中執行；
- 鑰匙在本地產生，然後在本地加密儲存；
- 狀態資料 (Stash) 保存在記憶體中，透過 **Carbonado** 函式庫進行序列化和加密，該函式庫使用 Blake3 執行壓縮、錯誤修正、加密和串流驗證。

拜這個架構所賜，所有資產交易都在客戶端進行。從外部來看，Bitcoin 交易不過是典型的 Taproot 支出交易，沒有人會懷疑它也帶有可替代代幣或 NFT 的轉移。沒有 On-Chain 重載（沒有公開儲存的元資料）保證了一定程度的自由裁量權，也更容易抵制可能的審查企圖。

### 安全性與分散式架構

由於 RGB 協定要求每位參與者保留其交易記錄 (以證明其收到的轉帳的有效性)，因此便產生儲存的問題。Bitmask 建議在本地將 Stash 序列化，然後傳送至數個伺服器或雲端（可選）。資料仍由使用者透過 **Carbonado** 加密，因此伺服器無法讀取。如果發生部分損壞，錯誤修正 Layer 可以重新構成內容。

CRDT (_Conflict-free replicated data type_)的使用可讓不同版本的 Stash 在出現歧異時合併。每個人都可以隨心所欲地託管這些資料，因為沒有任何單一的 Full node 會載有與資產相關的所有資訊。這正好反映了 *Client-side Validation* 的理念，即每位擁有者都有責任儲存其 RGB 資產有效性的證據。

### 邁向更廣闊的生態系統：市場、互通性和新功能

Bitmask 背後的公司並不僅限於簡單的 Wallet 開發。DIBA 打算開發 ：


- 交換代幣的**市場**，尤其是以**RGB21**形式交換；
- 與其他錢包相容（例如 *Iris Wallet*）；
- 轉移批次**技術，即在單一交易中包含數筆連續的 RGB 轉移的可能性。

與此同時，我們正在開發 **WebBTC** 或 **WebLN** (讓網站可以要求 Wallet 簽署 Bitcoin 或 Lightning 交易的標準)，以及「電子燒錄」Ordinals 項目的能力 (如果我們想要將 Ordinals 轉換成更隱密、更靈活的 RGB 格式)。

### 總結

整個過程顯示出 RGB 生態系統如何透過強大的技術解決方案進行部署，並讓終端使用者能夠使用。從 Altcoin 的觀點過渡到更以 Bitcoin 為中心的願景，再加上 *Client-side Validation* 的發現，說明了一個相當合乎邏輯的路徑：我們了解到，只要利用 Taproot 交易或 OP_RETURN 上的加密承諾，就有可能在不分叉 Blockchain 的情況下實現各種功能 (可替代代幣、NFT、智慧合約......)。

**Bitmask** Wallet 就是這種方法的一部分：在 Blockchain 側，您看到的只是普通的 Bitcoin 交易；在使用者側，您操作的是一個網路 Interface，在這裡您可以創建、Exchange 並儲存各種 off-chain 資產。這個模式清楚地將貨幣基礎架構 (Bitcoin) 與發行和轉移邏輯 (RGB) 分隔開來，同時確保高度的機密性和更好的擴充性。

## Bitfinex 在 RGB 上的工作

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::

在本章中，根據 Frederico Tenga 的簡報，我們將探討 Bitfinex 團隊專為 RGB 創建的一系列工具和專案，其目的是促進圍繞此通訊協定的豐富多樣的生態系統的出現。該團隊的初步目標不是發佈特定的商業產品，而是提供軟體建置區塊、貢獻於 RGB 協定本身，並提出具體的實作參考，例如行動 Wallet (*Iris Wallet*) 或相容於 RGB 的 Lightning 節點。

### 背景與目標

自 2022 年左右開始，Bitfinex RGB 團隊一直專注於開發技術堆疊，使 RGB 能夠被有效開發和測試。已經做出了多項貢獻：


- 參與原始碼與通訊協定規範，包括撰寫增強提案、修正錯誤等；
- 供開發人員使用的工具，可簡化 RGB 在應用程式中的整合；
- 設計一個名為 [Iris](https://iriswallet.com/)的行動 Wallet 來實驗和說明使用 RGB 的最佳作法；
- 建立客製化的 Lightning 節點，能夠以 RGB 資產管理通道；
- 支援其他團隊在 RGB 上建立解決方案，以鼓勵多樣性和強大的生態系統。

此方法旨在涵蓋整個需求鏈：從低階函式庫 (*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*)，使 Wallet 得以實作，到生產方面 (Lightning 節點、Android 版 Wallet 等)。

### RGBlib 函式庫：簡化 RGB 應用程式的開發

創建 RGB 電子錢包和應用程式民主化的重要一點是提供一個足夠簡單的抽象，使開發人員無需學習協議內部邏輯的所有知識。這正是以 Rust 寫成的 **RGBlib** 的目的。

RGBlib 充當了我們在前幾章所能研究的 RGB 高度彈性（但有時也很複雜）需求與應用程式開發人員具體需求之間的橋梁。換句話說，希望管理代幣轉移、資產發行、驗證等的 Wallet (或服務) 可以依賴 RGBlib，而無需瞭解每個加密細節或每個可自訂的 RGB 參數。

本書店提供 ：


- 發行 (_issuance_) 資產 (可替代與否) 的統包功能；
- 透過操作簡單的物件（位址、金額、UTXOs 等）來傳輸（傳送/接收）資產的能力；
- 用於儲存和載入 Client-side Validation 所需的狀態資訊（*consignments*）的機制。

因此，RGBlib 依賴 RGB 所特有的複雜概念 (Client-side Validation、Tapret/Opret anchor)，但將其封裝起來，讓最終應用程式不必重新編寫所有程式或做出危險的決定。更重要的是，RGBlib 已與多種語言 (Kotlin 和 Python) 結合，為 Rust 以外的用途打開大門。

### Iris Wallet：Android 上 RGB Wallet 的範例

為了證明 RGBlib 的有效性，Bitfinex 團隊開發了 **Iris Wallet**，現階段僅在 Android 上使用。這是一個行動 Wallet，說明了類似於一般 Bitcoin Wallet 的使用者體驗：您可以發行資產、傳送資產、接收資產、檢視資產歷史，同時保持自我保管模式。

Iris 有許多有趣的功能：

**使用 Electrum 伺服器：**

如同任何 Wallet，Iris 需要瞭解 Blockchain 上的交易確認。Iris 並未嵌入完整的節點，而是預設由 Bitfinex 團隊維護的 Electrum 伺服器。不過，使用者可以配置自己的伺服器或其他第三方服務。如此一來，Bitcoin 交易可以模組化的方式進行驗證和資訊擷取 (索引)。

**RGB 代理伺服器：**

與 Bitcoin 不同的是，RGB 需要在寄件者和收件者之間進行 Exchange 的 off-chain 元資料 (*consignments*)。為了簡化這個過程，Iris 提供了一個透過代理伺服器進行通訊的解決方案。接收方的 Wallet 會產生一個 *Invoice*，其中會提到寄件方應該將 * 客戶端 * 資料寄到哪裡。預設情況下，URL 指向 Bitfinex 團隊託管的代理，但您可以更改此代理（或託管您自己的代理）。我們的想法是回到熟悉的用戶體驗，即收件人顯示 QR 代碼，發件人掃描此代碼進行交易，而無需任何複雜的額外操作。

**連續備份：**

嚴格來說，在 Bitcoin 的情況下，備份您的 seed 通常就已經足夠（雖然現在我們建議備份 seed 和描述符）。對於 RGB，這還不夠：您還需要保留本機歷史記錄 (*consignments*)，證明您確實擁有 RGB 資產。每次收到收據時，裝置都會儲存新的資料，這些資料對於之後的消費非常重要。Iris 會自動管理使用者 Google Drive 中的加密備份。這不需要特別信任 Google，因為備份是經過加密的，而且未來還計劃提供更強大的選項 (例如個人伺服器)，以避免任何第三方業者審查或刪除的風險。

**其他功能：**


- 建立 Faucet，快速測試或分發代用幣，以進行實驗或推廣；
- 一個認證系統 (目前是集中式的)，用以區分合法代幣與抄襲著名股票的偽造代幣。未來，此認證可能會變得更分散 (透過 DNS 或其他機制)。

總而言之，Iris 所提供的使用者體驗接近於經典的 Bitcoin Wallet，由於 RGBlib 和代理伺服器的使用，掩蓋了額外的複雜性 (Stash 管理、*Consignment* 歷史等)。

### 代理伺服器與使用者體驗

上面介紹的代理伺服器值得詳細說明，因為它是順暢使用者體驗的關鍵。RGB 交易是在背景中透過 .NET Framework 進行，而不是由寄件人手動傳送*訂單*給收件人：


- 收件人會產生 *Invoice*（其中包含代理 Address）；
- 寄件者會傳送（透過 HTTP 請求）一個轉換專案（*Consignment*）給代理；
- 接收者擷取此專案，在本機執行 * 客戶端 * 驗證；
- 接著，接收者會透過代理公佈接受 (或可能拒絕) State Transition ；
- 寄件者可以檢視驗證狀態，如果接受，則廣播 Bitcoin 交易，完成傳輸。

如此一來，Wallet 的行為幾乎與一般的 Wallet 無異。使用者並不知道所有的中間步驟。誠然，目前的代理既沒有加密也沒有認證（這留下了保密性和完整性的顧慮），但這些改進在之後的版本中是可能的。代理的概念對於重現「我發送 QR 碼，您掃瞄付款」的體驗仍然非常有用。

### RGB 整合在 Lightning Network 上

Bitfinex 團隊工作的另一個重點是使 Lightning Network 與 RGB 資產相容。其目的是在 USDT（或任何其他代幣）中啟用 Lightning 通道，並從 Lightning 上的 Bitcoin 相同優勢（近乎瞬間的交易、路由等）中受益。具體來說，這涉及到建立一個 Lightning 節點，修改為 .USDT 或其他代幣：


- 打開一個通道，不僅要放置 satoshis，還要在資金 UTXO Multisig 中放置一個或多個 RGB 資產；
- generate Lightning Commitment 交易（Bitcoin 端）伴隨相應的 RGB 狀態轉換。每次更新通道時，RGB 轉換會重新定義 Lightning 輸出中的資產分佈；
- 啟用單邊關閉，在符合 Lightning Network 規則 (HTLC、時間鎖、懲罰等) 的情況下，以專屬 UTXO 擷取資產。

這個被稱為「**RGB Lightning Node**」的解決方案，使用 LDK (*Lightning Dev Kit*) 作為基礎，並加入將 RGB 令牌注入通道所需的機制。Lightning 承諾保留經典結構 (puncturable outputs、timelock...)，此外還有 Anchor 和 RGB State Transition（透過 `Opret` 或 `Tapret`）。對使用者而言，這開啟了在穩定幣或透過 RGB 發出的任何其他資產中使用 Lightning 通道的方式。

### DEX 的潛力和對 Bitcoin 的影響

一旦透過 Lightning 管理數個資產，就有可能在單一 Lightning 路由路徑上想像一個**原子 Exchange** ，使用相同的秘密和時間鎖邏輯。例如，用戶A在一個Lightning通道上持有Bitcoin，用戶B在另一個Lightning通道上持有USDT RGB。他們可以建立一條路徑，連接他們的兩個通道，同時以 Exchange BTC 換取 USDT，而無需信任。這不過是在幾個跳躍中進行的**原子交換**，使外部參與者幾乎忘記他們正在進行交易的事實，而不僅僅是路由。這種方法提供 ：


- 延遲非常低，因為 Lightning 上的一切都保持 off-chain。
- 優越的**隱私性**：沒有人知道這是一筆交易，而不是普通的路由；
- 避免前置運行，這是 On-Chain DEX 經常出現的問題 ；
- 降低成本（您不需支付區塊空間，只需支付 Lightning 路由費）。

我們可以想像一個生態系統，在這個系統中，Lightning 節點提供掉期價格（通過提供流動性）。每個節點，如果願意的話，都可以扮演_市場製造者_的角色，在 Lightning 上買入和賣出各種資產。這種_layer-2_ DEX 的前景強化了一個想法，即不需要 Fork 或使用第三方區塊鏈來獲得分散的資產交換。

對 Bitcoin 的影響可能是正面的：由於這些 * 穩定幣*、衍生幣和其他代幣所產生的交易量，Lightning 的基礎設施（節點、通道和服務）將得到更充分的利用。對 Lightning 上的 USDT 支付感興趣的商家，將機械地發現 Lightning 上的 BTC 支付（由相同的堆疊管理）。Lightning Network 基礎設施的維護和融資也可以從這些非 BTC 流量的倍增中獲益，這將間接惠及 Bitcoin 用戶。

### 結論與資源

致力於 RGB 的 Bitfinex 團隊透過其工作說明了在協定之上可進行的工作的多樣性。一方面，有 RGBlib，一個有助於設計錢包和應用程式的函式庫。另一方面，我們有 Iris Wallet，這是一個在 Android 上實作的 Interface 終端使用者整潔的示範。最後，RGB 與 Lightning 的整合顯示了穩定幣通道的可能性，並為 Lightning 上潛在的分散式 DEX 開啟了道路。

這種方法在很大程度上仍屬實驗性質，並會持續演進：RGBlib 函式庫會不斷精進，Iris Wallet 也會定期接受增強，而專用的 Lightning 節點還未成為主流的 Lightning 用戶端。

對於希望瞭解更多資訊或提供貢獻的人，我們提供了多種資源，包括：


- [GitHub RGB 工具儲存庫](https://github.com/RGB-Tools)；
- [Iris Wallet 專用資訊網站](https://iriswallet.com/) 在 Android 上測試 Wallet。

在下一章中，我們將進一步了解如何啟動 RGB Lightning 節點。

## RLN - RGB Lightning 節點

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::

在最後一章中，Frederico Tenga 會逐步帶您在 Regtest 環境上設定一個 Lightning RGB 節點，並教您如何在節點上建立 RGB 代幣。透過啟動兩個獨立的節點，您還會發現如何在它們與 Exchange RGB 資產之間開啟一個 Lightning 通道。

本視訊為教學，類似於我們在前一章所介紹的內容，但這次特別著重於 Lightning！

本視訊的主要資源是 Github 套件庫 [RGB Lightning Node](https://github.com/RGB-Tools/RGB-lightning-node)，讓您輕鬆在 Regtest 中啟動此組態。

### 部署與 RGB 相容的 Lightning 節點

此過程將前面各章所涵蓋的所有概念都納入其中並加以實踐：


- 在閃電通道的 2/2 Multisig 上封鎖的 **UTXO** 不僅可以接收比特幣，還可以成為 RGB 資產（可替代與否）的 Single-Use Seal 的想法 ；
- 在每個 Lightning engagement 交易中增加一個輸出 (`Tapret`或`Opret`)，專門用於錨定 RGB State Transition；
- 相關基礎架構 (bitcoind/indexer/proxy) 以驗證 Bitcoin 交易和 Exchange * 客戶端*資料。

### RGB-lightning 節點介紹

**`RGB-lightning-node`**專案是一個Rust daemon，以`Rust-lightning` (LDK) Fork為基礎進行修改，以考慮通道中存在的RGB資產。打開通道時，可以指定資產的存在，每次更新通道狀態時，都會創建一個 RGB 轉換，反映資產在 Lightning 輸出中的分佈。這樣就可以實現.NET和ASP.NET：


- 例如，在 USDT 中開啟 Lightning 通道；
- 透過網路路由這些代幣，前提是路由路徑有足夠的流動性；
- 利用 Lightning 的懲罰和定時鎖定邏輯，無需修改：只需在 Commitment Transaction 的額外輸出中 Anchor 轉換 RGB。

程式碼仍處於 alpha 階段：我們建議僅在 **regtest** 或 **Testnet** 上使用。

### 節點安裝

要編譯並安裝「RGB-lightning-node」二進位檔，我們首先要複製套件庫及其子模組，然後執行 .NET Framework：

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- `--recurse-submodules` 選項也會複製必要的子裝置 (包括修改版的 `Rust-lightning`)；
- shallow-submodules」選項限制了 clone 的深度，以加快下載速度，同時仍可存取重要的 commit。

從專案根目錄執行下列指令，以編譯並安裝 .NET Framework 2.0：

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` 可確保嚴格遵守相依性的版本；
- `--debug` 不是必須的，但可以幫助您集中注意力（如果您喜歡，也可以使用 `--release` ）；
- `--path .` 告訴 `cargo install` 從目前的目錄安裝。

此指令結束後，您的 `$CARGO_HOME/bin/` 中會出現一個 `RGB-lightning-node` 可執行檔。請確定這個路徑在您的 `$PATH` 中，這樣您就可以從任何目錄中呼叫這個指令。

### 性能要求

RGB-lightning-node` daemon 需要 .NET Framework 的存在和配置才能運作：


- 一個 `bitcoind`** 節點

每個 RLN 實例都需要與 `bitcoind` 通訊，以廣播和監控其 On-Chain 交易。需要向 daemon 提供驗證 (登入/密碼) 和 URL (主機/連接埠)。


- 索引器** (Electrum 或 Esplora)

daemon 必須能夠列出並探索 On-Chain 交易，特別是找到資產已被錨定的 UTXO。您需要指定您的 Electrum 伺服器或 Esplora 的 URL。


- 一個 RGB** 代理

如前幾章所述，**代理伺服器**是一個元件（可選，但強烈建議使用），用來簡化 Lightning 對等體之間的 Exchange *分配。再一次，必須指定 URL。

ID 和 URL 會在 daemon 透過 API 解鎖時輸入。稍後再詳述。

### 啟動 Regtest

對於簡單的使用，有一個 `regtest.sh` 腳本可以透過 Docker 自動啟動一組服務：bitcoind」、「electrs」（索引器）、「RGB-proxy-server」。

![RGB-Bitcoin](assets/fr/100.webp)

這可讓您啟動一個本機、隔離、預先設定的環境。它會在每次重新啟動時建立和銷毀容器和資料目錄。我們將從啟動 ：

```bash
./regtest.sh start
```

這個腳本將 ：


- 建立一個 `docker/` 目錄來儲存 ；
- 在 regtest 中執行 `bitcoind` 以及索引器 `electrs` 和 `RGB-proxy-server` ；
- 等到一切準備就緒即可使用。

![RGB-Bitcoin](assets/fr/101.webp)

接下來，我們要啟動幾個 RLN 節點。在不同的 shell 中執行，例如 (啟動 3 個 RLN 節點) ：

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- `--network regtest` 參數表示使用 regtest 設定；
- `--daemon-listening-port`表示 Lightning 節點將監聽哪個 REST 連接埠的 API 呼叫 (JSON)；
- `--ldk-peer-listening-port` 指定要監聽的 Lightning P2P 連接埠；
- `dataldk0/`, `dataldk1/` 是儲存目錄的路徑 (每個節點分別儲存其資訊)。

您也可以從瀏覽器在 RLN 節點上執行指令：

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

一個節點要打開一個通道，它必須首先在用以下命令產生的 Address 上有比特幣（以節點 n°1 為例）：

```bash
curl -X POST http://localhost:3001/address
```

答案會為您提供 Address。

![RGB-Bitcoin](assets/fr/103.webp)

在 `bitcoind` Regtest 上，我們要挖一些 bitcoins。運行：

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

將資金傳送至上述產生的節點 Address：

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

然後挖掘一個區塊來確認交易：

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Testnet 啟動 (無 Docker)

如果您想要測試更真實的情況，您可以在 Testnet 上啟動 3 個 RLN 節點，而不是在 Regtest 中，指向公共服務 ：

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

預設情況下，如果找不到任何設定，daemon 會嘗試使用 ：


- `bitcoind_rpc_host`:`electrum.iriswallet.com`。
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`.
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`

使用登入 ：


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

您也可以透過 `init`/`unlock` API 自訂這些 Elements。

### 頒發 RGB 令牌

要發行代用幣，我們會先建立「可著色」的 UTXO：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

當然，您可以調整訂單。為了確認交易，我們會挖出一個 .NET：

```bash
./regtest.sh mine 1
```

現在我們可以建立 RGB 資產。命令將取決於您想要建立的資產類型及其參數。這裡我要建立一個 NIA (*Non Inflatable Asset*) 符記，名稱為 "PBN"，Supply 為 1000 個單位。精確度」允許您定義單位的可分割性。

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

回應包括新建立資產的 ID。請記住這個識別碼。在我的例子中，它是 ：

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

然後您可以將它轉移到 On-Chain 或分配到 Lightning 頻道中。這正是我們下一節要做的。

### 開啟通道並轉移 RGB 資產

您必須先使用 `/connectpeer`指令將您的節點連接到 Lightning Network 上的對等點。在我的例子中，我控制兩個節點。因此，我將使用此命令擷取第二個 Lightning 節點的公開金鑰：

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

指令會返回我的節點 n°2 的公開金鑰：

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

接下來，我們將透過指定相關資產 (`PBN`)來開啟通道。`/openchannel` 指令可讓您以 satoshis 為單位定義通道的大小，並選擇包含 RGB 資產。這取決於您想要建立什麼，但在我的情況下，命令是 ：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

在此瞭解更多資訊：


- `peer_pubkey_and_opt_addr`：我們要連線的對等機構的識別碼 (我們之前找到的公開金鑰)；
- capacity_sat`：以 Satoshis 為單位的頻道總容量 ；
- `push_msat`：通道開啟時，最初轉移給對等方的金額（以毫釐為單位）（在此我立即轉移 10,000 Sats，以便他稍後可以進行 RGB 轉移）；
- `asset_amount`：RGB 資產承諾給通道的金額 ；
- `asset_id` : RGB 資產在頻道中的唯一識別碼；
- `public`：表示通道是否應該公開，以便在網路上進行路由。

![RGB-Bitcoin](assets/fr/111.webp)

為了確認交易，需要挖出 6 個區塊：

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Lightning 通道現在打開，節點 n°1 一邊也包含 500 `PBN` 代幣。如果節點 n°2 希望接收 `PBN` 代幣，它必須 generate 和 Invoice。以下是操作方法：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

與 ：


- `amt_msat`：Invoice 數量，單位為 millisatoshis (最低 3000 Sats) ；
- expiry_sec`：Invoice 失效時間，以秒為單位；
- `asset_id` : 與 Invoice 相關聯的 RGB 資產的識別碼；
- `asset_amount`：與此 Invoice 一起轉移的 RGB 資產金額。

回應時，您會收到 RGB Invoice （如前幾章所述）：

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

現在我們將從第一個節點支付這筆 Invoice，該節點持有必要的現金與 `PBN` 代幣：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

已付款。執行命令 ：

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

以下是如何部署經修改以搭載 RGB 資產的 Lightning 節點。本示範以 .NET Framework 為基礎：


- regtest 環境 (透過 `./regtest.sh`) 或 Testnet ；
- 一個 Lightning 節點 (`RGB-lightning-node`)，基於一個 `bitcoind`、一個索引器和一個 `RGB-proxy-server`；
- 一系列 JSON REST API，用於開啟/關閉通道、發行代幣、透過 Lightning 傳輸資產等。

感謝這個過程：


- 閃電接合交易包括附加輸出 (OP_RETURN 或 Taproot) 與 RGB 轉換的錨定；
- 轉帳方式與傳統的 Lightning 付款方式完全相同，但增加了 RGB 代幣；
- 只要路徑上的比特幣和資產 RGB 都有足夠的流動性，就可以連結多個 RLN 節點，進行跨節點的路由和付款實驗。

本專案仍處於 alpha 階段。因此強烈建議您僅限於測試環境 (regtest, Testnet)。

這種 LN-RGB 兼容性所開啟的機會相當可：閃電上的穩定幣、DEX Layer-2、以極低成本轉移可替代代幣或 NFT...前面的章節概述了概念架構和驗證邏輯。現在，您可以實際瞭解如何啟動和運行這樣的節點，以進行未來的開發或測試。

# 總結

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>

## 評論與評分

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>
## 總結

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>