---
name: 使用 Elements 和 Liquid Network 建構
goal: 學習使用 Elements 開放原始碼 Blockchain 平台及其主要功能進行開發
objectives: 

  - 瞭解 Elements Blockchain 平台和 Liquid 側鏈的基礎概念。
  - 學習設定和執行獨立和 Sidechain 組態的 Elements 節點。
  - 獲得聯合 block signing 和 Federated 2-Way Peg 的實際經驗。
  - 針對實際使用個案，建立並管理安全、有效率的 Blockchain 環境。

---
# 以 Liquid 和 Elements 為基礎

探索 Liquid 與 Elements 的進階特色與功能，並學習如何有效利用這些工具來強化您的開發專案。本訓練提供完整的理論與實務基礎，讓您能夠掌握 Confidential Transactions、Issued Assets 和 Federated block signing 等功能。

Liquid 以 Elements 架構為基礎，旨在改善金融和技術解決方案的隱私性、可擴展性和功能性。在本課程中，您將獲得資產發行與管理、Federated 2-Way Peg，以及 elementsd 與 elements-cli 等工具使用的實務經驗，讓您有能力創造出符合您需求的創新解決方案。

本課程專為各種經驗等級的開發人員量身打造。初級和中級使用者可以找到容易理解的說明和實用範例，而高級使用者則可以深入瞭解 Liquid 和 Elements 的技術細節和較少人知道的功能。

加入我們，提升您的技能、發揮 Liquid 和 Elements 的全部潛力，並為 Liquid 創新的未來創造具有影響力的工具。

+++
# 簡介

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## 課程簡介

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::

Elements 學院的目的是介紹並解釋 Elements 的主要概念，Elements 是 Liquid 所建立的開放原始碼平台。課程結束時，您應該對 Elements 的主要功能（如 Confidential Transactions 和 Issued Assets）以及執行 Elements Core 的流程有相當的了解。

每一部分都有附有說明文字的課程和視訊，視訊結束時會進行小測驗。問題的數量與前一個主題的大小有關。第 10 節將總結課程內容，並以一個較大的測驗結束。

若有任何問題、需要額外資訊或對測驗答案有疑問，請直接與您的老師 James Dorfman 聯絡。

## Elements 概觀

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::

Elements 是一個開放原始碼、具備 Sidechain 功能的 Blockchain 平台，可存取社群成員開發的強大功能，例如 Confidential Transactions 和 Issued Assets。

Elements 的核心是一個協定，它能夠圍繞交易歷史和規則形成共識，這些交易歷史和規則管理著分佈式 Blockchain Ledger 中儲存的資產的轉移和創建。

有關 Elements 的更多背景資訊，可隨時瀏覽 Elements 計畫網站 (https://elementsproject.org/)、Liquid 官方部落格 (https://blog.Liquid.net/) 及開發人員入口網站(https://Liquid.net/devs)。

### Elements

Elements 於 2015 年推出，可降低內部開發及研究成本，並運用最新的 Blockchain 技術，開啟許多新的使用實例。基於 Elements 的 Blockchain 可作為獨立的 Blockchain 運作，或與另一個 Blockchain 掛接並作為 Sidechain 運行。將 Elements 作為 Sidechain 執行，可以在不同區塊鏈之間可驗證地轉讓資產。

Elements 建立在 Bitcoin 的程式碼基礎上並加以擴充，讓熟悉 bitcoind API 的開發人員可以快速且符合成本效益地建立可用的區塊鏈，並測試概念驗證專案。Elements 建立在 Bitcoin 的程式碼基礎上，也讓 Elements 成為 Bitcoin 通訊協定本身變更的測試平台。

接下來列出 Elements 的一些主要功能。

#### Confidential Transactions

預設情況下，Elements 中的所有位址都是使用 Confidential Transactions 的 blinded。蒙蔽是指除了參與者和他們選擇向其透露蒙蔽金鑰的人之外，每個人都可以透過加密方式隱藏所轉移資產的金額和類型。

#### Issued Assets

Elements 上的 Issued Assets 允許在網路參與者之間發行和轉讓多種資產。已發行資產也受益於 Confidential Transactions，持有相關 reissuance token 的任何人都可以重新發行或銷毀該資產。

#### Federated 2-Way Peg

Elements 是通用的 Blockchain 平台，也可與現有的 Blockchain（如 Bitcoin）「掛鉤」，以實現資產從一條鏈到另一條鏈的雙向轉移。將 Elements 實作為 Sidechain 可讓您繞過主鏈的某些固有屬性，同時保留主鏈上資產所提供的高度安全性。

#### 簽名區塊

Elements 使用簽署人 Strong Federation，稱為區塊簽署人 (Block Signers)，他們以可靠且及時的方式簽署並建立區塊。這消除了 PoW Mining 流程的交易延遲問題，由於其隨機 poisson 分佈，區塊時間差異很大。聯邦 block signing 流程可實現可靠的區塊創建，而無需引入第三方信任或基於計算「算法」的 Mining。

Elements 在 Bitcoin 核心程式碼基礎上增加了所有這些功能，擴展了 mainchain 通訊協定的能力，在部署為 Sidechain 或獨立的 Blockchain 解決方案時，可實現新的業務用例。

# 元素

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Elements 如何運作

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::

Elements 為 Blockchain 使用者每天面臨的問題提供技術解決方案；交易延遲、缺乏隱私以及可替代性風險。

Elements 透過使用 Federated block signing 和 Confidential Transactions 克服了這些問題。

與 Bitcoin 網路不同的是，Elements 內的 block signing 流程不依賴動態成員多方簽章 (DMMS) 和 Proof of Work (PoW)。取而代之的是，Elements 使用稱為區塊簽章者 (Block Signers) 的 Strong Federation 簽章者，他們可以可靠且及時的方式簽章和建立區塊。這消除了 PoW Mining 流程的交易延遲，因為其隨機 poisson 分佈會造成很大的區塊時間方差。Federated block signing 程序可在不需要引入第三方信任的情況下實現可靠的區塊創建。

Elements 可作為另一個 Blockchain (例如 Bitcoin) 的 Sidechain 執行，或作為獨立的 Blockchain 執行，不依賴其他網路。

當作為 Sidechain 使用時，Strong Federation 也包含能夠在主鏈和 Elements Sidechain 之間安全、受控地轉移資產的成員。受控的資產轉移稱為 Federated 2-Way Peg，執行資產轉移角色的成員稱為 watchmen。

Elements 網路運作的過程以及網路參與者的角色，對於了解 Elements 如何運作非常重要。

無論是以 Sidechain 或獨立的 Blockchain 實作，Elements 都是利用區塊簽章器強聯盟來產生區塊。

### 強大的聯盟

Elements 使用 Blockstream 首次提出的共識模型，稱為強聯盟 (Strong Federations)。Strong Federation 不需要 Proof of Work (PoW)，而是依靠一群互不信任的參與者 (稱為 Functionaries) 的集體行動。

在 Strong Federation 中，功能人員可扮演的角色有：Block Signers 和 watchmen。如果在 Sidechain 或獨立 Blockchain 模式下執行 Elements，則需要 Block Signers，而 watchmen 僅在 Sidechain 設定中需要。

Strong Federation 的成員可執行的動作分為兩種不同的角色，以加強安全性並限制攻擊者可能造成的損害。

當這些參與者的角色結合起來時，Elements 就能同時提供快速的區塊創建（更快且最終的交易確認）和有保證的可轉讓資產（可直接連結到另一個 Blockchain 的掛鉤資產）。

您可以在此閱讀強大聯盟白皮書： https://blockstream.com/strong-federations.pdf

### 區塊簽名

當任何組成區塊簽章者動態群組的人透過展示已消耗的 Proof of Work 來擴展鏈時，Blockchain 就會像 Bitcoin 的 Blockchain 一樣被擴展。這套系統的動態性質引進了此類系統固有的延遲問題。

透過使用固定的簽名者集，聯邦模式以已知集、多重簽名方案取代動態集。減少擴展 Blockchain 所需的參與者數目，可提高系統的速度和可擴展性，同時各方的驗證可確保交易歷史的完整性。

Federated block signing 包含幾個階段：


- 步驟 1 - 區塊簽章者以輪流方式向所有其他參與的區塊簽章者提出候選區塊。
- 步驟 2 - 每位 block signer 預先承諾簽署給定的候選區塊，以表示其意向。
- 步驟 3 - 如果符合給定的預 Commitment 門檻，每個 block signer 會簽署該區塊。
- 步驟 4 - 如果符合簽章閾值 (可能與步驟 3 的簽章閾值不同)，該區塊即被接受並傳送至網路。Strong Federation 已就最新的交易區塊達成共識。
- 步驟 5 - 接著由循環中的下一個 block signer 提出下一個區塊，並重複此程序。

由於 Strong Federation 的區塊生成不是概率性的，而是基於固定的簽名者集，因此它永遠不會受到多區塊重組的影響。這可大幅減少與確認交易相關的等待時間。它也消除了為了獲利而挖礦的誘因（即區塊獎勵），取而代之的是積極參與的誘因，在這個網路中，所有參與者都有相同的共同目標：確保網路繼續以對所有人都有利的方式運作。在不引入單點失效或更高信任要求的情況下，它可以做到這一點。

### Elements 作為 Sidechain - watchmen 和 Federated 2-Way Peg

當作為 Sidechain 運行時，Strong Federation 的某些成員需要履行額外的角色，即 watchmen。watchmen 負責將資產轉入或轉出 Elements Sidechain，這個過程稱為「Peg-In」和「Peg-Out」。

為了讓 Sidechain 以可信賴的方式運作，它必須允許參與者驗證資產的 Supply 是可控制和可驗證的。Elements Sidechain 使用 2-Way Federated Peg 來實現資產進出 Elements Blockchain 的雙向轉移。這滿足了可證明發行和鏈間轉移的要求。

Federated 2-Way Peg 功能允許資產與其他區塊鏈互通，並代表另一個 Blockchain 的原生資產。透過將您的 Blockchain 與其他資產掛鉤，您可以擴展 mainchain 的功能，並克服其某些固有的限制。

從高層次來看，當有人將 mainchain 資產傳送到由多重簽章 watchmen Wallet 控制的 Address 時，就會發生轉入 Sidechain 的情況。這會有效凍結 mainchain 上的資產。然後 watchmen 會驗證交易，並釋放 Sidechain 內相關資產的相同金額。釋放的資產會傳送到 Sidechain Wallet，該 Wallet 可以證明對原始 mainchain 資產的索賠權。此流程有效地將資產從母鏈移至 Sidechain。

為了將資產轉移回 mainchain，使用者在 Sidechain 上進行特殊的掛出交易。此交易由 watchmen 檢查，然後由他們在 mainchain 上控制的多重簽章 Wallet 簽署交易支出。在 mainchain 交易生效之前，聯盟中必須有一定數量的參與者簽署。當 watchmen 將資產傳回 mainchain 時，他們也會銷毀 Sidechain 上的相應金額，有效地在區塊鏈間轉移資產。

## 設定並執行 Elements

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::

由於 Elements 是基於 Bitcoin 的程式碼基礎，因此構成運作中網路的元件非常相似。

Elements 節點軟體本身稱為 `elementsd`，在使用者的機器上以 daemon 的方式執行。daemon (或 Windows 中的服務) 是一個以背景服務方式執行的程式，不需要登入使用者的直接控制。

注意：在本文件中，我們會一直將 elementsd 稱為 daemon 版本，但只要啟用伺服器選項，一切都可以用 Elements-qt 來完成。

Elements daemon 連接到網路中的其他節點，因此它可以 Exchange 交易和區塊資料，驗證和擴展其網路 Blockchain 的本地副本。

Elements 軟體也包含一個名為「elements-cli」的客戶端程式，可讓您從命令列向 elementsd 傳送遠端程序呼叫 (RPC) 指令。例如，這可用於查詢 Wallet 結餘、檢視交易或區塊資料或廣播交易。使用過 Bitcoin 對應 bitcoind 和 bitcoin-cli 的人應該都很熟悉這個設定。

由於 Elements 節點可以在啟動時傳入參數或透過設定檔進行設定，因此可以在同一台機器上運行多個實例。這對於測試和開發非常有用，因為您可以在一台機器上建立自己的區域網路，每個 Elements 節點都有自己的 Blockchain 資料副本，管理自己的未確認有效交易池，並在不同的連接埠聆聽 RPC 請求。

### Elements 程式碼儲存與社群

Elements 是一個開放原始碼專案，其原始碼可在 Elements GitHub 套件庫中找到，網址為 https://github.com/ElementsProject/Elements。該資源庫包含 elementsd 和 elements-cli 程式的原始碼，以及支援的安裝和建置工具、測試套件和一些說明文件。

為了補充程式碼倉庫，還有 https://elementsproject.org 網站，這是一個以社群為中心的資源，包含 Elements 是什麼、如何運作的說明，以及全面的教學部分。教學重點在於依照命令列範例學習 Elements，並教您如何在其上建立簡單的桌面與網頁應用程式。該網站還列有熱門的 Elements 社群討論區，而且本身也託管在 GitHub 上，讓社群能對網站內容做出貢獻。

要在您的電腦上執行 Elements，您首先需要克隆（下載一份）原始程式碼，安裝程式碼的任何相依性，最後再建立 daemon 和用戶端執行檔。之後，Elements 軟體就可以配置和執行了。

## 設定節點與網路

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

可以在啟動時將組態設定傳給 Elements 節點，以改變其執行、驗證資料、連線到其他節點以及初始化其 Blockchain 資料的方式。

設定可從指定的 `Elements.conf` 檔案載入，或透過命令列傳入參數。

有些東西可以使用這些參數來變更：


- 獨立 Blockchain 實作中使用的 default asset 名稱。
- 建立的初始資產編號。
- 支付網路交易費用時使用的資產。
- Blockchain 資料檔案的儲存位置。
- 用於連接 Bitcoin 節點的 RPC 認證。
- 必須符合的 `n of m` 門檻，以及可以簽署區塊的有效公開金鑰。
- 需要滿足的腳本，以便將資產轉入或轉出 Sidechain。
- 是否將 Bitcoin 節點當作 Sidechain 連線。

這些規則有許多是網路共識規則的一部分，因此在啟動時應用於所有節點是很重要的。有些規則可以在鏈初始化之後變更，但有些則需要在用於鏈初始化之後修復。

參數的使用將在課程稍後時間，當與每一節相關時加以說明。

### 使用命令列的基本操作

本課程將展示使用 `elements-cli` 程式對一個或多個 Elements 節點進行 RPC 呼叫的範例。這將在終端會話中完成，為了使命令更簡短，將使用`alias`。根據這個慣例，當您看到類似以下的命令時：

```bash
e1-dae
e1-cli getnewaddress
```

`e1-dae` 和 `e1-CLI` 實際上是利用終端機的 `alias` 功能的排版捷徑。在執行命令時，`e1-dae` 和 `e1-CLI` 實際上會被取代，執行的命令類似於：

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

我們上面看到的是啟動 Elements daemon 的呼叫，以及呼叫位於「$HOME/Elements/src」目錄中的 elements-cli 程式，以及「datadir」參數的值。`datadir` 參數允許我們告訴 daemon 和用戶端實例在哪裡找到它們的設定檔案，對 daemon 而言，則在哪裡儲存它的 Blockchain 副本。由於它們共用一個 config 檔案，用戶端將可以對 daemon 進行 RPC 呼叫。

再次執行上述指令，但使用不同的 `datadir` 值，我們就可以啟動一個以上的 Elements 範例，每個範例都有自己獨立的 Blockchain 副本和組態設定。根據這個慣例，我們會在課程中使用別名 `e2-dae` 和 `e2-CLI` 來指代不同於 e1 的 datadir 目錄。所以上面的範例對於我們的第二個 `e2` 實例將會是：

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

這可讓我們執行各種作業，例如節點間的資產交易、發行資產，以及檢查同一網路中不同節點間 Confidential Transactions 的盲點使用情況。

# 使用元素 實用案例

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Confidential Transactions

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::

在本節中，您將學習如何使用 Elements 的 Confidential Transactions 功能。

Elements 中的所有位址預設都是使用 Confidential Transactions 的 blinded，這可讓只有交易參與者 (以及他們選擇透露致盲金鑰的人) 才能看到轉移的資產數量和類型，同時仍能以加密方式保證所花費的硬幣不會多於可用的硬幣。

### 機密地址和 Confidential Transactions

預設情況下，當您使用 `getnewaddress`指令在 Elements 中建立新的 Address 時，該 Address 會建立為機密 Address。

為了示範 Confidential Transactions，我們會讓 e2 自行傳送一些資金，然後嘗試從 e1 檢視交易。這將展示 Elements 中交易的機密性。

Elements 節點產生的每個新 Address 預設都是保密的。我們可以讓 e2 去 generate 產生一個新的 Address 來證明這一點。

```
e2-cli getnewaddress
```

請注意 Address 以 e1 開頭。這表示它是 Confidential Address。使用 getaddressinfo 指令詳細檢查 Address 會顯示 Address 的更多詳細資訊。

```
e2-cli getaddressinfo <address>
```

您可以看到有一個 confidential_key 屬性告訴我們這是一個機密的 Address。

confidential_key 是公開的致盲金鑰，會加到機密 Address 本身。這就是機密 Address 如此冗長的原因。

它也有一個相關的非機密 Address。如果您希望在 Elements 內使用一般的非機密交易，則資產應該傳送到此 Address，而不是 lq1 前綴的 Address。

現在我們可以讓 e2 傳送一些資金到它所產生的 Address。這將在稍後展示 e1，因為它不是交易方之一，所以無法檢視交易的詳細資訊。

```
e2-cli sendtoaddress <address>
```

注意 transaction ID。確認交易。

```
e2-cli -generate 101
```

從 e2 本身的角度來看 e2 寄送一些資金給自己的交易。

```
e2-cli gettransaction <txid>
```

向上捲動交易詳細資訊，您可以看到 e2 可以檢視傳送和接收的金額以及交易的資產。您也可以看到 amountblinder 和 assetblinder 屬性，它們用來遮蔽未參與交易的其他節點的詳細資訊。

要從 e1 檢查相同交易的詳細資料，我們首先需要取得原始交易詳細資料。

```
e1-cli getrawtransaction <txid>
```

這會傳回原始的交易詳細資訊。如果您查看 vout 部分，可以看到有三個實例。前兩個是收款金額和變更金額，第三個是交易費用。在這三個金額中，費用是唯一可以看到值的，因為費用本身永遠是 unblinded 內的 Elements。

### 閃光鑰匙

前兩個 vout 部分顯示的是價值金額的「blinded 範圍」，以及作為實際交易金額和資產類型證明的 Commitment 資料。

即使我們將 e2 的私人密碼匙匯入 e1 的 Wallet，它仍然無法看到交易的資產金額和種類，因為它仍然不知道 e2 所使用的保密密碼匙。我們會將 e2 的 Wallet 所使用的私人密碼匙匯入 e1 的 Wallet 來證明這一點。首先，我們需要從 e2 匯出金鑰

```
e2-cli dumpprivkey <address>
```

然後將其匯入 e1。

```
e1-cli importprivkey <privkey>
```

現在我們可以證明 e1 仍然看不到數值。

```
e1-cli gettransaction <txid>
```

事實上，它顯示 0 為 tx 數量，而實際上是 1。

為了能夠看到實際的、未縮放的值，我們需要縮放鍵。要做到這一點，我們首先要從 e2 匯出致盲鍵。

```
e2-cli dumpblindingkey <address>
```

然後將其匯入 e1。

```
e1-cli importblindingkey <address> <blinding key>
```

現在，當我們從 e1 取得交易詳細資料時。

```
e1-cli gettransaction <txid>
```

它顯示在匯入盲鍵後，我們現在可以在交易中檢視 1 的實際值。

在本節中，我們已經了解到使用保密鑰匙可以隱藏交易中資產的數量和類型，而通過輸入正確的保密鑰匙，我們可以揭示這些值。在實際使用中，如果需要驗證某一方持有的資產數量和類型，可以將盲鑑金鑰提供給核數師。Elements 的 Confidential Transactions 功能還允許執行「範圍證明」。範圍證明可證明在特定範圍內持有資產的數量，而無需揭露實際數量本身。

我們也看到 Confidential Transactions 是可選的，但在產生新的 Address 時預設為啟用。

這一課到此；祝您在測驗中取得好成績，下一課見！

## Issued Assets

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::

在本節中，您將學習如何使用 Elements 的 Issued Assets 功能。

Issued Assets 可在 Elements 網路參與者之間發行和轉移多種類型的資產。網絡上的任何節點都可以發行自己的資產。發行的資產可代表任何可替代的 Ownership 資產，包括代金券、息票、貨幣、存款、債券、股票等。Issued Assets 為建立 Trustless 交易所、期權和其他涉及自我 Issued Assets 的進階智慧合約打開了大門。

已發行資產也受惠於 Confidential Transactions，任何持有相關代幣的人都可以重新發行這些資產。

第一步，我們需要存取兩個 Elements 節點，我們稱之為 e1 和 e2。這兩個節點的區塊鏈已經被重置，default asset 在它們之間被分割。

這兩個節點位於相同的區域網路，彼此相連，因此在其交易 Mempool 中共享相同的交易，以及相同的區塊鏈。雖然它們運行在同一台機器上，但值得注意的是，它們並不共享相同的實際 Blockchain 檔案。每個節點都管理自己的本地 Blockchain 副本，其中包含相同的交易歷史，因為它們達成共識，彼此遵守相同的協定規則。

讓我們先檢查每個節點對於網路中現有資產發行的看法。

這可以使用 listissuances 指令來完成。

```
e1-cli listissuances
e2-cli listissuances
```

如您所見，兩個節點都顯示相同的發行歷史。它們都顯示一個資產，即初始發行的 2,100 萬個 Bitcoin，這些資產是在 on chain 初始化時建立的。您可以在執行上述指令的結果中看到資產的十六進位 ID，以及指定給資產的標籤，也就是「Bitcoin」。

值得注意的是，default asset 在鏈初始化時總是會被賦予一個標籤。當您發行自己的資產時，您可以自行為它們設定標籤，我們很快就會這麼做。在此之前，我們需要發行自己的資產。

我們要讓 e1 簽發新的資產。這是使用 issueasset 指令完成的。

```
e1-cli issueasset 100 1 false
```

`issueasset` 接受 3 個參數。

要發行的新資產金額，我們使用 100。要創建的代幣數量（代幣用於重新發行資產的數量），我們選擇了 1。最後一個參數告訴 Elements 要以 blinded 或 unblinded 來建立資產發行。我們會使用 unblinded，因為我們想在一會兒從 e2 檢視發行金額，所以我們會輸入 false。

執行指令會返回有關發行的資料。這些資料包括 transaction ID（您可以複製一份以備日後使用）、資產的唯一十六進位值，以及資產的代碼的唯一十六進位值。

generate 確認發行交易的區塊。

```
e1-cli -generate 1
```

再次針對 e1 執行 `listissuances` 指令。

```
e1-cli listissuances
```

這顯示 e1 現在知道 2 項發行，即 Bitcoin 的初始發行和我們新發行的資產，我們可以看到其中的 100 項。請注意新資產的十六進位值，而且與 Bitcoin 發行一樣，沒有相關的資產標籤。

再次檢查 e2 的已知發行清單。

```
e2-cli listissuances
```

這顯示 e2 並不知道 e1 所發行的資產。它只能看到它已經可以看到的 Bitcoin 的初始發行。

這是因為 e2 不知道，也沒有觀看 e1 發出新資產時所傳送至的 Address。

值得注意的是，即使 e2 無法看到發行本身，e1 仍可向 e2 傳送部分資產。新資產就會在 e2 的 Wallet 中顯示為可用餘額，即使它不知道原始發行。

為了讓 e2 能看到實際的簽發（因此也能看到簽發的金額），我們需要將 Address 加入 e2，成為有注視的 Address。

為此，我們需要找出資產傳送至的 Address。為此，我們將使用先前複製的 transaction ID，並讓 e1 擷取該交易的詳細資訊，以便找出正確的 Address，加入 e2 的 Wallet 觀察清單。

```
e1-cli gettransaction <the-issuance-transaction-id>
```

向上捲動交易資料的十六進位，您會看到收到 100 個新資產的 Address，並以其十六進位值識別。

將 Address 複製，以便匯入 e2。

現在讓我們將 Address 匯入 e2。為此，我們使用 importaddress 指令。

```
e2-cli importaddress <the-issued-to-address>
```

如果我們現在檢查 e2 的發行清單。

```
e2-cli listissuances
```

您可以看到我們新發行的資產現在已包含在清單中。e2 節點也能確定已發行資產的金額，以及相關代幣的金額，因為該發行是 unblinded 發行。要在 Elements 中啟用資產 ID 到名稱的對應，首先停止 Elements。

```
e1-cli stop
```

然後使用額外的參數重新啟動，將資產的十六進位映射到所提供的標籤。這可讓節點以更人性化的格式向我們顯示資產的相關資料。如果您願意的話，可以將這個參數加入 Elements.conf 的最後，那麼您就不需要每次啟動 daemon 時都加入這個參數。例如

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

但我們在此會使用論點方法。

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

再次查詢節點的發行清單。

```
e1-cli listissuances
```

這說明資產的十六進位值對應到其標籤是有效的。再次檢查 e2 節點的發行清單。

```
e2-cli listissuances
```

您可以看到 e2 節點無法存取此標籤，因為只有設定標籤的節點才能使用標籤。事實上，我們可以在 e2 上為相同的資產 hex 指定與在 e1 上不同的標籤。首先停止 e2 節點。

```
e2-cli stop
```

以指定給新資產十六進位的不同標籤重新開始。

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

從 e2 上市發行。

```
e2-cli listissuances
```

資產標籤是每個節點的本地標籤，只有資產的六角才會被網路中的其他節點識別。

當進行交易和 Wallet 結餘查詢時，標籤到資產六角的映射很有用，因為它允許一種簡短的方式來參照資產。例如，如果我們想將一些新資產（金額為 10）從 e1 傳送至 e2，而不使用標籤。

首先，我們需要取得一個 Address 來傳送資產。

```
e2-cli getnewaddress
```

然後使用 sendtoaddress 指令。

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

透過產生區塊來確認交易。

```
generate 1
```

檢查資產是否在 e2 上收到。

```
e2-cli getwalletinfo
```

我們可以看到資產確實收到了。

請注意，e2 會映射接收到的資產的十六進位，並使用自己的標籤顯示。要做同樣的事情，更簡單的方法是在傳送時使用 e1 的資產標籤。

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

在幕後，Elements 將本機標籤映射為十六進位值，以幫助簡化 Issued Assets 的使用。

在本節中，我們瞭解了如何發行和標示資產。在下一節中，我們將探討如何重新發行和銷毀已發行資產的數量。

## 再發行資產

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::

在本節中，您將學習如何發行更多已發行資產，以及如何銷毀一定數量的已發行資產。

當資產所代表的東西沒有固定的 Supply 時，就可能需要重新發行（製造更多）資產或銷毀一定數量的資產。例如，這適用於代表存放在金庫中的黃金的資產；當黃金單位進出金庫時，代表金庫 Supply 的資產需要相應地向上或向下調整。

重新發行資產金額需要 Ownership 相關代用幣，該代用幣是在最初發行資產時與資產一起建立的。

在創建更多資產時，只要重新發行資產數量的節點擁有資產的 reissuance token，那麼最初發行資產的節點並不重要。我們將探討如何初始化 reissuance token、如何使用 reissuance token 重新發行資產，以及如何將 reissuance token 轉移給其他節點，使它們也有權限重新發行資產。

我們需要存取兩個 Elements 節點，我們稱之為 e1 和 e2。這兩個節點的區塊鏈已被重置，default asset 在它們之間分割。

我們讓 e1 發行數量為 100 的新資產，並為同一資產建立 1 個 reissuance token。為了簡化範例，我們將以 unblinded 來建立發行。因此，讓我們繼續發行資產及其相關的 reissuance token。

```
e1-cli issueasset 100 1 false
```

請注意資產的 ID 以及（重新發行）代用幣的 ID。

由於我們稍後會從 e2 重新發行更多資產，因此我們需要記下資產發行的 transaction ID，並使用該資產匯入資產傳送的 Address。

確認交易。

```
e1-cli -generate 1
```

現在我們使用 gettransaction 指令檢查交易的詳細資料：

```
e1-cli gettransaction <txid>
```

向上捲動交易資料的十六進位，您會看到在交易中，e1 收到 1 個 reissuance token 和 100 個相關資產。

複製一份 Address，以便我們匯入 e2。

現在將 Address 匯入 e2 的 Wallet。

```
e2-cli importaddress <address>
```

現在我們可以看到 e1 和 e2 都知道資產發行。

```
e1-cli listissuances
e2-cli listissuances
```

目前 e1 持有一定數量的資產和 1 reissuance token，但 e2 沒有。

```
e1-cli getwalletinfo
```

另外請注意，e1 擁有的 default asset 比之前少，因為它支付了一小筆金額來支付交易費用。當所建立的區塊成熟超過 100 個區塊深度時，e1 就會收取這筆款項。

```
e2-cli getwalletinfo
```

由於 e1 持有 reissuance token，它可以重新發行更多的 reissuance token。這可以使用 reissueasset 指令來完成。讓 e1 再發行 100 個資產。

```
e1-cli reissueasset <asset-id> 100
```

檢查重發成功。

```
e1-cli getwalletinfo
```

您可以看到 e1 現在如預期持有 200 的資產。

由於 e2 並未持有一定數量的 reissuance token，如果他們嘗試重新發行資產，將會收到錯誤。

```
e2-cli reissueasset <asset-id> 100
```

請注意錯誤訊息。

我們可以使用 listissuances 指令從 e1 檢視重新簽發的詳細資訊。

```
e1-cli listissuances
```

請注意 `is_reissuance` 標誌。

如果我們現在寄給 e2 一筆 reissuance token 的金額，他們就可以自己重新發行一筆資產。首先，我們需要一個 Address 來發送。值得注意的是，在發送和顯示餘額時，reissuance token 與 Elements 中的任何其他資產一樣，也可以像任何其他資產一樣細分為較小的面額，因此我們不需要向 e2 發送 1 個 reissuance token 才能讓它重新發行資產。任何面額都足夠了。生成一個 Address 供 e2 接收 reissuance token。

```
e2-cli getnewaddress
```

然後從 e1 傳送一部分 RIT 到 e2。

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

確認交易。

```
e1-cli -generate 1
```

現在我們可以看到 e2 持有它被傳送的 0.1。

```
e2-cli getwalletinfo
```

這表示 e2 現在可以重新發行更多與其 Wallet 中持有的 RIT 相關的資產。我們將讓 e2 重新發行 500 份資產。

```
e2-cli reissueasset <asset-id> 500
```

檢查重新簽發的結果。

```
e2-cli getwalletinfo
```

您可以看到，e2 現在在其 Wallet 結餘中持有重新發行的金額，而 RIT 本身並未在資產重新發行的過程中消耗。

銷毀一定數量的資產是任何至少持有被銷毀數量的人都可以做的事，不受 reissuance token 規範。

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

在本節中，我們瞭解了如何發行資產，以及如何使用作為資產發行一部分的 reissuance token。我們也看到轉讓 reissuance token 就像轉讓任何其他資產一樣簡單，而且持有任何數量的 reissuance token 都會賦予持有人發行更多相關資產的權利。因此，在您的網路中控制誰有權存取再發行代幣是非常重要的。我們也看到了如何銷毀一定數量的資產，而且這個過程不受 reissuance token 持有者的控制。

# 元素聯盟

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## block signing

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::

Elements 支援聯合簽署模式，可讓您指定必須簽署建議區塊的 Strong Federation 成員數目以產生有效區塊。

在此之前，為了方便舉例，我們一直使用 `generate` 指令來建立區塊，而 generate 指令不需要滿足多重簽章的要求，這樣建立的區塊才能被網路接受為有效。

我們將設定我們的節點需要 2-of-2 Multisig 區塊建立。這將會使用 signblockscript 參數來設定，這個參數可以加入設定檔或在啟動時傳入節點。為了使用此參數初始化連鎖，我們首先需要建立它所組成的腳本。

我們會使用一些現有的節點來做這個動作，儲存它們輸出的資料，然後將鏈抹除，這樣我們就可以使用 signblockscript 參數重新啟動它。這是必要的，因為腳本會形成網路共識規則的一部分，並且需要設定 on chain 初始化。它不能在稍後添加到已存在的鏈上。

我們需要存取兩個 Elements 節點，我們稱之為 e1 和 e2。這兩個節點的區塊鏈已被重設，default asset 在它們之間分割。

確保 Elements.conf 檔案中的 con_max_block_sig_size 參數設定為高值，否則本節稍後的 block signing 將會失敗。本教學中我們設定 con_max_block_sig_size=2000 。

由於我們將重置 Blockchain 並清除與 e1 和 e2 相關的錢包，因此我們需要將使用的位址、公鑰和私鑰複製到 generate 的 block signing 腳本中，以便稍後使用。

首先，我們需要每個將成為 block signing 節點的 generate 新 Address，您需要複製一份。

```
e1-cli getnewaddress
e2-cli getnewaddress
```

然後，我們需要從地址中抽取公開金鑰，並記錄下來以備日後使用。

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

然後擷取私密金鑰，稍後我們會重新匯入這些金鑰，以便節點可以在我們重新初始化 Blockchain 和 Wallet 資料後簽署區塊。

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

現在我們需要 generate 一個 Redeem 腳本，要求 2 對 2 多重簽章。我們可以使用 createmultisig 指令，並傳入第一個參數為 2，然後提供兩個公開金鑰。稍後建立區塊時，Ownership 需要證明的就是這些金鑰。

e1 或 e2 節點都可以 generate Multisig。

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

這就是我們的 redeemscript，您可以複製以供稍後使用。

現在我們需要抹除現有的 Blockchain 和 Wallet 資料，這樣我們就可以重新開始使用新的 signblockscript 作為鏈共識規則的一部分。這就是我們之前需要複製部分資料的原因，例如將在新鏈中用來簽署區塊的私人金鑰。在繼續之前，您需要這樣做。

刪除現有的 Wallet 和連鎖資料後，我們現在可以啟動節點，讓它們使用 signblockscript 參數初始化新的連鎖。讓我們傳入 -evbparams=dynafed:0::: 來停用 dynafed 啟動，因為本範例不需要這個進階功能。

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

現在我們需要匯入之前儲存的私人金鑰，以便我們的節點可以簽署並協助完成任何建議的區塊。

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

使用 generate 指令現在應該會出錯，因為它不符合我們節點現在強制執行的所需 block signing 規則。

```
e1-cli -generate 1
```

為了提出新區塊，任一節點都可以呼叫 getnewblockhex 指令。這會回傳一個新區塊的十六進位元，在被我們網路中的任何節點接受之前，該區塊需要簽署。

```
e1-cli getnewblockhex
```

請記住，該指令只是建立一個建議區塊，而不是 generate。

為了確認這一點，我們可以看到 Blockchain 目前沒有任何區塊。

```
e1-cli getblockcount
```

如果我們嘗試在沒有先簽署的情況下提交 block hex。

```
e1-cli submitblock <block-hex>
```

我們收到一則訊息，告訴我們區塊證明無效。這是因為它尚未由所需的兩方中的兩方簽署。

所以讓 e1 簽署建議的區塊。

```
e1-cli signblock <block-hex>
```

讓 e2 在六角簽名。

```
e2-cli signblock <block-hex>
```

請注意，e2 並未簽署由 e1 簽署建議區塊所產生的輸出。他們都會獨立於彼此的結果簽署建議的區塊六角。

現在我們需要合併 e1 和 e2 的區塊簽章。任一節點都可以做到這一點，它們所需要的只是來自另一個節點的已簽章區塊十六進位元。

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

您可以看到 combineblocksigs 指令會輸出已簽署區塊的十六進位以及完成狀態，告訴我們區塊的十六進位已準備好提交。

現在任一節點都可以提交完成的區塊 hex。我們讓 e1 來做。

```
e1-cli submitblock <combined-signed-hex>
```

檢查提交是否有效。

```
e1-cli getblockcount
e2-cli getblockcount
```

您可以看到 e1 和 e2 都接受該區塊為有效，並將其加入 Blockchain 本機副本的頂端。

總結一下流程。在本節中，我們有：


- 建議一個區塊。
- 讓每個節點都簽名。
- 合併簽名。
- 檢查簽章是否有效，並符合連鎖的 redeemscript 門檻。
- 提交區塊。

網路中的每個節點都會驗證區塊，並將其加入 Blockchain 的本機副本中。

### block signing

儘管過程最初看起來很複雜，但 Elements 中 block signing 的順序總是相同的，初始設定只需要執行一次：

1.初始設定（執行一次）

2.使用聯邦區塊簽章器的公開金鑰，建立稱為「signblockscript」的多重簽章 Address。

3.由此產生的 Redeem 指令碼會用來啟動新的 Blockchain。

4.區塊生產（進行中）

5.建議的區塊會產生並交換簽署。

一旦有一定數量的簽署人簽署了建議的區塊，它就會被合併並提交給網絡。如果它符合連鎖的「signblockscript」標準，節點就會接受它為有效區塊。

## 元素作為側鏈

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::

Elements 是一個開放原始碼的通用 Blockchain 平台，也可以「掛接」到現有的 Blockchain，例如 Bitcoin。當與另一個 Blockchain 掛鉤時，Elements 被稱為作為「Sidechain」運作。側鏈允許資產從一個鏈向另一個鏈的雙向轉移。將 Elements 實作為 Sidechain 可讓您繞過 mainchain 的一些固有限制，同時保留在 mainchain 上抵押的資產所提供的相當程度的安全性。

雖然 Sidechain 可以感知 mainchain 及其交易歷史，但 mainchain 無法感知 Sidechain，其運作也不需要 mainchain。這可讓側鏈進行創新，而不受 mainchain 協定改進提案的限制或延遲。與其試圖直接改變 mainchain，不如擴展主協定，讓 mainchain 本身保持安全與專門，為 Sidechain 的順暢運作提供基礎。

透過擴充 Bitcoin 的功能並利用其基本安全性，基於 Elements 的 Sidechain 就能提供 mainchain 使用者之前無法使用的新功能。Liquid Network 就是生產中使用的基於 Elements 的 Sidechain 的範例。

為了將 Elements Blockchain 初始化為 Sidechain，我們需要使用 federated peg script 參數。這個參數可以在節點的設定檔中設定，或是在啟動時傳入。

federated peg script 定義 Strong Federation 的哪些成員可以執行掛入和掛出功能。這些功能人員被稱為「watchmen」，因為他們觀察 mainchain 和 Sidechain 是否有有效的掛入和掛出交易，並在有效時採取行動。peg-out 「表示將掛鉤資產從 Sidechain 移出並移入 mainchain，而 」peg-in "表示將掛鉤資產從 mainchain 移入 Sidechain。當我們說「移入 Sidechain」時，我們實際上是指資金被鎖定在 mainchain 上的多重簽章 Address 中，並且在 Elements Sidechain 上創建了相應數量的資產。當我們說 「移出 Sidechain 」時，我們的意思是資產在 Elements Sidechain 上被銷毀，相應金額從 mainchain 上的鎖定資金中釋放。執行掛入和掛出功能的許可需要功能人員證明 Ownership 在 federated peg script 中使用的公開密鑰。這需要使用相應的私人金鑰。

因此，為了建立 federated peg script，我們首先需要讓每個節點都擁有 generate 公開金鑰。我們也需要儲存相關的私密金鑰以供日後使用，因為我們需要抹除任何現有的連鎖資料，並使用 federated peg script 來初始化新的連鎖。這是因為 federated peg script 構成 Sidechain 共識規則的一部分，而且日後無法套用至現有的、未對齊的 Blockchain。

因此，讓我們在每個節點上 generate 一個 Address，儲存相關資料以供稍後使用，並 generate federated peg script，稍後我們將用它來初始化我們的 Sidechain。

首先，我們需要每個節點 (將作為我們網路中的 watchmen) generate 一個新的 Address。

```
e1-cli getnewaddress
e2-cli getnewaddress
```

然後，我們驗證 Address 以取得公開金鑰。

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

然後擷取與每個 Address 相關聯的私密金鑰。

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

儲存私人密碼匙和公開密碼匙以供日後使用。

現在我們需要清除現有的 Blockchain 和 Wallet 資料，因為我們要使用 federated peg script 來初始化新的連鎖。現在就可以進行。別忘了啟動 Bitcoin daemon，我們需要將它掛入。

現在我們可以使用先前儲存的公開金鑰建立的 federated peg script 來初始化新的金鑰鏈。我們輸入並圍繞著公開金鑰的數字會定義並限定所使用的金鑰數量，以及為了掛入或掛出我們的 Sidechain 而必須證明的金鑰 Ownership。

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

現在，我們將匯入之前儲存的私密金鑰，以便我們的節點之後能夠簽署並完成資產在鏈之間的轉移，滿足 federated peg script 的要求。

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

我們現在需要成熟兩個鏈上的一些區塊。區塊成熟是掛鉤過程的必要條件，因為它可以防止 mainchain 上的區塊重組導致 pegged asset Supply 在 Sidechain 中膨脹。

為了讓本節專注於聯邦掛架，我們將不使用上一節介紹的 block signing 模型來產生區塊，而回到使用「generate」指令來建立新區塊。

```
b-cli generate 101
e1-cli generate 1
```

我們現在不一定需要 generate 區塊來做 Elements。但是，我們還是要 generate 一個。這是避免潛在不一致的好做法。

現在我們的鏈已準備好掛入。為了 peg-in，我們需要使用 getpeginaddress 指令來 generate 一種特殊的 Address。請注意，從 getpeginaddress 產生掛入 Address 到 claimpegin 聲稱掛入 Address 之間的時間應該儘量縮短。掛入位址不是長期耐用的，不應該重複使用。

```
e1-cli getpeginaddress
```

您可以看到該指令建立了一個新的 mainchain Address，以及一個新的腳本，需要滿足該腳本才能領取掛入資金。mainchain Address 是「付給腳本 Hash」的 Address，將由在 Elements 網路中扮演 watchmen 角色的功能人員使用。

如同 getnewaddress，getpeginaddress 會在呼叫節點的 Wallet 中加入新的秘密，因此在節點管理流程中，必須將備份 Wallet 檔案列入考量。

我們現在要從 mainchain 傳送一些 Bitcoin 到 Sidechain。我們的 mainchain 回歸測試 Wallet 已經持有一些資金。

```
b-cli getwalletinfo
```

我們可以看到 Wallet 可容納 50 個 Bitcoin。我們要從 mainchain 傳送一個 Bitcoin 到 Sidechain。我們需要將資金傳送至 mainchain 節點先前產生的 Address。

```
b-cli sendtoaddress <e1-pegin-address>
```

我們需要保留此交易的 ID，因為稍後我們需要它作為資金證明。

現在我們可以看到 mainchain Wallet 的餘額減少了我們寄出的金額，再加上一小筆額外的交易費用。

```
b-cli getwalletinfo
```

我們需要再次成熟交易。

```
b-cli generate 101
```

為了讓我們的 Elements 節點領取掛入資金，我們需要取得掛入交易已完成的「證明」。加密證明使用資金 transaction ID 來計算默克爾路徑，並證明交易存在於已確認的區塊中。

```
b-cli gettxoutproof '["<tx-id>"]'
```

我們也需要原始交易資料。

```
b-cli getrawtransaction <tx-id>
```

有了掛入交易的憑證和原始資料，我們的 Elements 節點現在就可以使用原始交易和交易憑證要求掛入。

```
e1-cli claimpegin <raw> <proof>
```

請注意，有一個可選的第三個參數，我們可以提供給 claimpegin。這第三個參數可以用來指定 Sidechain Address 來傳送申領的資金。這在我們的範例中並不需要，因為我們是從 Address 的相同節點呼叫命令，而 Address 擁有申領的資金。

檢查 e1 的餘額。

```
e1-cli getwalletinfo
```

產生區塊以確認索賠。

```
e1-cli generate 1
```

檢查 e1 的餘額。

```
e1-cli getwalletinfo
```

我們可以看到，掛入已成功認領。

掛帳的流程類似。生成 Address，向其發送資金，如果交易有效，則釋放資金。我們不會涵蓋整個peg-out 過程，因為它涉及到 mainchain 的工作，這超出了本課程的範圍。Elements 事件的步驟是在 mainchain 上產生 Address。

```
b-cli getnewaddress
```

資金使用 sendtomainchain 指令從 Elements 節點傳送至 mainchain Address。

```
e1-cli sendtomainchain <new-address> 1
```

產生區塊以確認交易。

```
e1-cli generate 1
```

檢查節點 Wallet 的餘額。

```
e1-cli getwalletinfo
```

並看到餘額減少了。

在本節中，我們瞭解了如何


- generate a federated peg script。
- 初始化一個使用腳本作為網路共識參數規則的新鏈。
- 將資金從 mainchain 傳送至 Sidechain。
- 領取 Elements Sidechain 內的資金。
- 瞭解如何開始傳送資金回 mainchain。

### FederatedPegScript

為了讓 Elements 能以 Sidechain 的方式運作，其 Blockchain 中的 Genesis 區塊必須以 `fedpegscript` 的方式建立。這可在節點啟動時傳入 `fedpegscript` 參數。該腳本隨後將成為 Elements Blockchain 共識規則的一部分，並允許確認並執行 peg-in 和 peg-out 請求。

fedpegscript」是由授權執行掛鈎動作的人所控制的公開金鑰所組成。以下顯示 2 對 2 多重簽章 fedpegscript 的範例格式：

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

注意：公開金鑰外的字元是表示公開金鑰和 `n of m` 要求的分隔符。例如，1-of-1 fedpegscript 的範本為 「5121<公開金鑰 1>51ae」。

### 釘入

在 Elements Sidechain 接受掛入之前，必須在 mainchain 上有足夠的確認。這是避免 Elements Sidechain 上 pegged asset 的 Supply 因 mainchain 重組而造成膨脹所必須的。

Bitcoin Blockchain 的頂端短暫重新組織是 Proof of Work (PoW) 共識機制正常運作的一部分。因此，Elements 只有在 Bitcoin Blockchain 內有足夠深度時，才會接受有效的 Peg-in。這樣做的目的是防止 Elements 多次接受相同的 peg-in。

### Peg-Out

當 Elements 節點呼叫「sendtomainchain」指令時，就會發生掛出交易，該指令會將 mainchain Address (掛出目的地) 以及要「提款」的 pegged asset 金額作為輸入。這會在 Sidechain 上建立掛出交易。一旦作為 watchmen 的功能人員偵測到 Sidechain 上的掛出交易已被確認，他們就會按照我們在課程的前幾節所學，將 mainchain 上的資產實際釋放到掛出目的地。

## Elements 作為獨立的 Blockchain

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::

到目前為止，我們已瞭解如何將 Elements 作為 Sidechain 執行。不過，它也可以作為獨立的 Blockchain 解決方案，並擁有自己的預設原生資產。在此設定中，Elements Blockchain 仍保留 Sidechain 實作的所有功能，例如 Confidential Transactions 和 Issued Assets，但不需要 peg-in 或 peg-out 來增加或移除流通中的 default asset 金額。

在本節中，我們將

初始化新的 Elements Blockchain，default asset 名稱為 `newasset`。

指定要建立 1,000,000 `newasset` 以及 2 個重新發行的代幣。

領取所有 anyone-can-spend `newasset` 硬幣。

領取「newasset」的所有 anyone-can-spend 補發代用幣。

將資產及其 reissuance token 傳送至另一個節點的 Wallet。

從兩個節點重新發行更多 'newasset'。

為了初始化 Elements 網路，使其能以獨立 Blockchain 的方式運作，每個節點都需要以一些基本參數啟動。它們用來告訴節點不要嘗試從其他 Blockchain 驗證 peg-ins、網路的 default asset 名稱，以及要建立的 default asset 和相關 reissuance token 的數量。

我們現在將在兩個連接的 Elements 節點上使用這些參數啟動一個新的鏈。我們將把 default asset 命名為 `newasset` 並發行 100 萬個 `newasset` 和兩個 `newasset` 再發行代幣。

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

請注意，這裡使用的金額是網路可以接受的最小面額，因此兩億個再發行代幣實際上等於兩個整數的代幣。初始免費代用幣的面額也是如此。

檢查我們節點目前的 Wallet 結餘。

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

我們可以看到初始化工作正常。

由於最初發行的資產是以「任何人都可以花費」的方式建立，我們會讓 e1 領回所有資產，這樣就可以移除 e2 的存取權。

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

請注意，我們不需要指定「newasset」為要傳送的資產，因為它已經是 default asset，因此也是用來支付網路費用的 default asset。

在 Elements 中，您可以將多種資產類型傳送至相同的 Address，因此我們可以重新使用剛產生的 Address 來接收 default asset，並將其作為重新發行代幣的目的地 Address。

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

確認交易。

```
e1-cli generate 101
```

我們現在要檢查 e1 是否是資產及其 reissuance token 的唯一持有者。

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

我們可以看到事實確實如此。

現在我們要將一些 'newasset' 傳送給目前持有 0 結餘的 e2。

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

請注意，我們不必指定要傳送的資產類型，因為 `newasset` 已經建立為網路的 default asset

讓我們也送一些 `newasset` 的重新發行代幣給 e2。

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

確認交易。

```
e1-cli generate 101
```

我們可以檢查錢包是否已經相應更新。

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

現在我們從 e1 重新發行一些 default asset。請注意，這個功能是由 initialreissuancetokens 啟動參數啟用的。如果省略或設定為零，將導致 default asset 無法在日後重新發行。

```
e1-cli reissueasset newasset 100
```

我們能夠使用 `newasset` 的標籤，而不必提供十六進位 id 值，因為 Elements 鏈總是標示其 default asset。

檢查 default asset 的重新發行是否成功：

```
e1-cli generate 101
e1-cli getwalletinfo
```

我們現在要證明，因為 e2 持有一些 `newasset` 重新發行代幣，所以它也可以重新發行 default asset。

```
e2-cli reissueasset newasset 100
```

檢查 e2 重新簽發 default asset 是否成功。

```
e2-cli generate 101
e2-cli getwalletinfo
```

在本節中，我們將 Elements 設定為獨立的 Blockchain，並檢查基本功能是否如預期般運作。

我們使用啟動參數來

初始化新的 Elements Blockchain 與命名為 'newasset' 的 default asset。

指定 default asset 創建 on chain 初始化的數量。

為 default asset 建立一些重新發行的代幣，並從兩個節點重新發行更多的 default asset。

在我們獨立的 Blockchain Elements 網路上，所有其他交易作業的操作方式與課程主要章節所涵蓋的範例相同，但會使用「newasset」而非「Bitcoin」作為預設和費用資產。

### 節點啟動和鏈初始化參數

要將 Elements 節點當成獨立的 Blockchain 來操作，必須同時使用幾個參數。我們現在就來看看這些參數的作用。

#### `validatepegin=0`。

由於獨立的 Blockchain 不需要驗證任何 peg-in 或 peg-out 交易，因此我們需要停用這些檢查。有了這個設定，您就不需要執行 Bitcoin 用戶端軟體，也不需要儲存 Bitcoin Blockchain 的複本，因為 Elements 網路會獨立運作。

#### 預設分割資產名稱

這可讓您指定 Blockchain 初始化時建立的 default asset 名稱。

#### 初始免費硬幣

要建立的 default asset 的數量 (相當於 Bitcoin 的 Satoshi 單位)。

#### 初始發行代幣

為 default asset 製造的再發行代幣數量（等同於 Bitcoin 的 Satoshi 單位）。如果沒有這個，就無法創造更多的 default asset。如果您不想創建更多的 default asset，可以將此設定為零或省略。

使用這些參數，啟動節點的常式會如下所示：

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### 基本操作

`defaultpeggedassetname` 參數會為 default asset 套用標籤。如果沒有此設定，default asset 會自動命名為 `Bitcoin`。在之前的章節中，當我們傳送自己發行的資產到另一個節點時，我們必須指定資產十六進位或本機套用的資產標籤，才能告訴 Elements 我們要傳送的資產。由於 `defaultpeggedassetname` 適用於所有節點，因此我們在傳送時不需要為它命名，即使它的名稱不是 `Bitcoin`。之前預設會傳送 `Bitcoin` 的每個函式，現在都會傳送您選擇標示 default asset 為何物。

因此，將 10 台新的 default asset 傳送至 Address 非常簡單：

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

如果您也為節點提供了 `initialreissuancetokens` 大於 0 的值，那麼您也將能夠重新發行更多的 default asset，如果您將 Elements 當作 Sidechain 執行，就無法做到這一點。

要做到這一點，任何持有與 default asset 相關聯的代用幣數量的節點只需發佈形式為命令的指令即可：

```
e1-cli reissueasset <default asset name> <amount>
```

透過使用上述參數，您可以將 Elements 作為獨立的 Blockchain 運作，並擁有自己的 default asset，與 Bitcoin 和其他區塊鏈解耦。

## 總結

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::

在本課程中，我們學習到 Elements 是一個開放原始碼的網路通訊協定，可作為 Sidechain 實作到另一個 Blockchain，或作為獨立的 Blockchain 解決方案。

我們已經看到 Elements (https://github.com/ElementsProject/Elements) 的原始碼和網站都寄存在 GitHub 上，而且還有一些社群討論區，例如 Build On L2(https://community.Liquid.net/c/developers/)，或是 Liquid 開發者 Telegram (https://t.me/liquid_devel)，可以用來學習更多關於在 Elements 和 Liquid 上部署和開發應用程式的資訊。Confidential Transactions 和 Issued Assets 等關鍵功能，以及 Strong Federation 的成員如何啟用聯盟 block signing 和 2-Way Peg 機制。

下一步是挑戰自己，進行涵蓋之前所有部分的累積測驗，然後開始您的 Elements 之旅...祝您好運！

# 總結

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## 評論與評分

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>
## 總結

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

恭喜您完成此課程！

我們很高興您已成功達到學習旅程中的這個里程碑。透過您的付出和參與，您獲得了寶貴的知識和技能，這些知識和技能將為您的職業發展提供良好的幫助。