---
name: 深入探究 Simplicity
goal: 掌握 Simplicity 的設計哲學、型別系統與完整生命週期
objectives:
  - 理解三種基本組合方法，以及構成完整語言的九個組合子
  - 從 Simplicity 的最小型別系統建構布林邏輯、算術與 SHA-256
  - 掌握 Failure 與 Reader 副作用如何實現真正的區塊鏈互動
  - 了解 Simplicity 程式如何成為 Taproot 位址，並用見證資料贖回
---

# 深入探究 Simplicity

本課程深入探討 Simplicity 語言背後的理論與設計決策，內容基於 Simplicity 在 Blockstream Research 的創造者 [Russell O'Connor 博士](https://r6.ca/)所撰寫、完整五篇的 ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) 文章系列。本課程說明的是 Simplicity *為什麼*被設計成這樣，而不是如何撰寫 Simplicity。

課程沿著 O'Connor 博士的文章，依序介紹組合計算的三種基本方式、最小型別系統與其完備性定理、從第一原理建構實用資料型別與算術、為了區塊鏈互動而謹慎引入的副作用，最後說明程式如何被承諾到位址並在鏈上贖回。

+++

# 引言

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## 課程概覽

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

歡迎來到 SCR403 — 深入探究 Simplicity！

本課程基於 [Blockstream](https://blockstream.com/) 的 Infrastructure Tech Developer、也是 Simplicity 創造者 [Russell O'Connor 博士](https://r6.ca/)所撰寫的 **"Delving Simplicity"** 文章系列。原始文章發表於 [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) 論壇，並構成本課程的主要來源材料。我們感謝他的開創性工作，讓這份教育內容得以成形。

### 你將學到什麼

本課程探索 Simplicity 背後的設計哲學與數學基礎；Simplicity 是於 2025 年 7 月在 [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) 啟用的新一代腳本語言。本課程遵循完整五篇文章系列，並分成兩個主要內容部分：

1. **Simplicity 的基礎** — 為什麼區塊鏈計算需要一種根本不同的語言、組合操作的三種方式（循序、平行、條件），以及形成數學上完整語言的九個核心組合子
2. **從資料型別到程式** — 從第一原理建構布林邏輯、算術與 SHA-256；理解實現區塊鏈互動的 Failure 與 Reader 副作用；並學習程式如何透過 Commitment Merkle Root 被承諾到 Taproot 位址，並用見證資料贖回

### 先備知識

這是一門**專家級**課程（約 10 小時）。你應該熟悉：
- 基本 Bitcoin 腳本概念（交易驗證做什麼）
- 基本程式設計概念（型別、函式、組合）
- 熟悉一些數學記號會有幫助，但不是必要條件。我們會隨著課程逐步介紹一切

### 重要資源

- **原始文章**：Russell O'Connor 博士在 Delving Bitcoin 上撰寫的 ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary)
- **Simplicity 儲存庫**：[BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — 原始碼與 Rocq 形式化證明
- **官方網站**：[simplicity-lang.org](https://simplicity-lang.org/) — 文件與 SimplicityHL 參考
- **Blockstream 部落格**：[GitHub 上的 Simplicity](https://blog.blockstream.com/en-simplicity-github/) — 技術概覽

準備好深入探索 Bitcoin 工程中最優雅的作品之一了嗎？開始吧！

## 什麼是 Simplicity？

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

如果你來到本課程時對 Simplicity 沒有背景知識，本章會先幫你定位，再進入深入內容。

### Simplicity 概述

Simplicity 是一種**Bitcoin 原生智能合約語言**，如今已在 Liquid Network 上線。它最早由 Russell O'Connor 博士約於 2012 年構想，並在他 2017 年的論文 *Simplicity: A New Language for Blockchains* 中詳細闡述；經過多年形式化驗證與開發後，於 2025 年 7 月在 Liquid Network 啟用。

不同於 Ethereum 的 Solidity 這種圖靈完備的高階合約語言，Simplicity 有意保持極簡。它有：
- **三種型別構造子**（單位、和、積）
- **九個組合子**（基本操作與組合規則）
- **沒有迴圈、沒有遞迴、沒有動態記憶體**

僅憑這些原語，你就能建構交易驗證所需的任何計算，從布林邏輯到完整的 SHA-256 雜湊。

### 今天你可以用 Simplicity 做什麼？

Simplicity 已經在 Liquid Network 上支援真實應用。最值得注意的是 [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/)，這是一個無需 oracle 的選擇權市場，使用者以 USDt 作為抵押品交易 L-BTC 的看漲選擇權（底層合約也支援看跌選擇權）。其他已上線的 Simplicity 專案包括 SideSwap 的 [Swaption](https://swaption.io/)（選擇權）以及 Resolvr 的開源 [Deadcat](https://github.com/Resolvr-io/deadcat)（預測市場）。除了 DeFi 之外，Simplicity 還能實現進階花費條件，例如金庫、限制條款 (Covenant)，以及在 Bitcoin Script 中不可能或不安全的複雜 multisig 方案。

### 本課程是什麼 — 以及不是什麼

這**不是**實作式的程式教學。你不會在這裡撰寫 Simplicity 程式。如果你要找的是那類內容，請參考：
- [simplicity-lang.org](https://simplicity-lang.org/) — 官方文件與高階語言 SimplicityHL
- [Simplicity GitHub 儲存庫](https://github.com/BlockstreamResearch/simplicity) — 參考實作、範例與 Rocq 證明
- 關於入門的 [Blockstream 部落格文章](https://blog.blockstream.com/en-simplicity-github/)

本課程**真正**關注的是：Simplicity 設計背後的**哲學與技術選擇**。為什麼要這樣創造這門語言？為什麼只有九個組合子？為什麼沒有遞迴？型別系統連結到 Gentzen 的序列演算，這件事為什麼重要？

你可以把它理解成：不是學習如何開車，而是理解**引擎為什麼被這樣打造**。

### 這門課適合誰？

本課程很適合：
- **協定開發者**，想在寫程式前理解 Simplicity 的基礎
- **Bitcoin 研究者**，對形式化驗證與型別理論方法感興趣
- **電腦科學家**，好奇序列演算與區塊鏈計算之間的連結
- **進階 bitcoiners**，想超越對 Liquid 腳本能力的表層理解

如果「和型別」、「組合子」或「序列演算」這類術語對你而言全然陌生，不用擔心，我們會從零開始解釋一切。但請準備好面對一段密集、數學性強的旅程。

### 從文章到課程

Russell O'Connor 博士原始的 "Delving Simplicity" 系列由五篇技術文章構成。本課程將這些材料重組並加上註解，形成循序漸進的學習路徑，並穿插測驗來檢驗你的理解。想法、定義與證明都來自他，我們則將格式調整為結構化教育內容。

# Simplicity 的基礎

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## 組合計算的基本方式

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

既然 Simplicity 已經在 Liquid Network 上啟用，我想深入探討 Simplicity 語言的哲學與設計。

Bitcoin 的交易驗證與一般程式語言設計是截然不同的應用。區塊空間成本很高，所以程式需要精簡。Bitcoin 交易中的程式只會在單一輸入上執行，而且所有人都在同一個輸入上執行該程式。此外，授權交易的行為者已經事先知道計算的結果：也就是該交易有效。

通常，授權行為者會執行昂貴得多的計算，以推導出證明交易有效性的見證資料；而在區塊鏈上執行的程式只需要檢查見證資料是否有效。檢查有效性通常比證明有效性便宜許多。

我們在設計 Simplicity 時，正是把這類獨特的語言設計挑戰納入考量。例如，Simplicity 要求未執行的分支必須被剪枝，因此不會出現在區塊鏈上。預處理步驟被仔細設計成在 Simplicity 程式大小上呈現（準）線性時間複雜度。使用靜態分析而不是 "gas"；gas 必須以規定方式執行程式碼才可計算，因此會讓執行模型的細節變成共識關鍵。執行期間不做動態記憶體配置。諸如此類。

在深入 Simplicity 的設計細節之前，我想先以一些程式設計哲學開始本系列：如何把基本建構區塊組合起來，創造新的功能。

### 組合

假設有人正在為 Bitcoin 這類區塊鏈設計一種可程式化交易語言。特別是，程式只能存取交易資料與各輸入的 UTXO 資料，而執行只決定交易有效性（這讓執行結果可以被快取）。假設一開始有一組基本操作，可以執行各種任務，例如基本計算、從交易讀取和／或處理資料，以及簽章驗證。每個操作會消耗某種型別的輸入（可能為空），並回傳某種型別的輸出。我們有哪些方式可以把這些基本操作組合成更複雜的操作？

### 循序組合

![循序組合](assets/en/001.webp)

最基本的組合方法是循序組合。如果我們有兩個基本操作，其中一個的輸出資料型別與另一個的輸入資料型別相符，那麼就能把這兩個操作組合成一個新的複合操作。這個新操作會依序執行這兩個基本操作：以第一個操作的輸入作為輸入，將第一個操作的輸出傳入第二個操作的輸入，最終回傳第二個操作的輸出。

當然，我們不需要把自己限制在只能組合基本操作。既然已經有一些複合操作，我們也可以使用函式組合來組合它們。

在數學中，這種循序組合通常就稱為「組合」，因此人們可能會以為這是唯一的組合方式。不過，我們還有其他方式可以組合操作。

### 平行組合

![平行組合](assets/en/002.webp)

假設我們有兩個操作，它們可以是基本操作也可以是複雜操作，而且兩者都接受相同型別的輸入。組合這兩個操作的第二種基本方式，是在同一個輸入上同時執行它們。這稱為平行組合，其輸出型別是原始兩個操作輸出型別的「積」，並包含兩個輸出的配對。

雖然這被稱為「平行」組合，而且原則上兩個操作可以平行執行，但平行執行並不是操作上的要求。我們可以先執行一個操作，再執行第二個操作，以「循序」方式實作平行組合。只要輸出相同，我們並不在意平行組合的實作細節。

### 條件組合

![條件組合](assets/en/003.webp)

條件組合是平行組合的對偶。在這種情況下，我們有兩個會產生相同輸出的操作，並透過選擇其中一個來執行而把它們組合起來。這個複合操作的輸入，是原始操作輸入型別的「和」或「帶標籤聯合」。在此情境中，標籤 "Left" 或 "Right" 是輸入資料中的一個位元，它決定攜帶的是哪一種資料型別，因此也決定兩個操作中的哪一個可以被執行。

即使輸入是兩個相同型別的和，條件組合也以同樣方式運作。和型別仍然包含標籤，而該標籤的值決定要執行兩個操作中的哪一個。

### Bitcoin Script 中的組合

在各種程式語言中，有許多方式可以實現這三類組合。在 Bitcoin Script 中，循序組合（近似地）透過串接兩段例程來實現（這也是為什麼 Bitcoin Script 被稱為串接式程式語言），因為一段例程的輸出會留在堆疊上，供後續例程消耗。平行組合則透過使用 duplicate 與 swap 操作來操作堆疊，使兩段例程能在同一個輸入上執行。事情並不完全直接，因為我們所謂型別的「積」通常是透過使用多個堆疊項目來實現。希望你能看出其中的大致想法。

條件組合當然是由 `OP_IF` 實現，它會根據堆疊上的值進行分支。在這種情況下，堆疊頂端項目扮演標籤的角色，而通常堆疊上的下一個或多個項目會具有取決於該標籤值的不同「型別」。對於每個情況，堆疊項目型別可能只適合由 `OP_IF` 中其中一個分支處理。然而，當我們到達 `OP_ENDIF` 後，堆疊項目必須具有一致的「型別」，使剩餘腳本能夠不依賴先前採用哪個分支而繼續執行。

### Simplicity 中的組合

我們設計 Simplicity 時使用了能直接實作這三種組合形式的組合子。再加上少數幾個支援與積型別、和型別相關的其他基本操作的組合子，核心 Simplicity 語言最後由九個組合子構成，足以表達任何有限計算。我們會在下一章更詳細討論這一點。

### 第四種組合

在結束之前，我們應該提到，在電腦科學中至少還有另一種組合，稱為「遞迴組合」。在遞迴組合中，一個操作會被反覆迭代多次。

請注意，Bitcoin Script 不支援遞迴組合；同樣地，我們也已明確將無界遞迴排除在 Simplicity 的設計之外。我們的論點是，無界迭代計算更適合透過跨多筆交易計算的遞迴限制條款 (Covenant) 來實作。這讓使用者能避開區塊空間與標準性限制，並更好地預測交易成本。

話雖如此，確實有方法濫用 Simplicity 的委託功能來提供某種類似無界遞迴組合的東西，我們可能會在本系列後面討論。

### 結論

我們回顧了三種主要組合形式，用於將基本操作轉換為複雜操作：

- 循序組合
- 平行組合
- 條件組合

我們討論了這些組合形式如何在 Bitcoin Script 中實現，並暗示它們如何影響 Simplicity 語言的設計。我們指出，第四種組合，也就是遞迴組合，在 Simplicity 與 Bitcoin Script 中都被特意排除。

下一章將描述構成 Simplicity 語言核心的九個組合子、它們如何直接實現這三種組合形式，以及這如何形成一種能描述任何有限計算的完整語言。

## Simplicity 的組合子完備性

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

本章介紹核心 Simplicity 語言，並展示該語言是完備的，意思是任何有限計算都能在其中表達。

### Simplicity 型別

Simplicity 支援三種基本型別構造子。積型別 `A × B` 表示平行組合的輸出，而和型別 `A + B`（帶標籤聯合）處理條件組合的輸入。第三種型別是單位型別。

### 單位型別

單位型別記為 `𝟙` 或 `ONE`，只包含一個值：空 tuple `⟨⟩` 或 `()`。這種零位元資料型別不攜帶任何資訊。

### 和型別

和型別 `A + B` 將兩個型別與表示「左」或「右」的標籤結合起來。值寫作 `σᴸ(a)` 或 `inl(a)` 表示帶左標籤的值，寫作 `σᴿ(b)` 或 `inr(b)` 表示帶右標籤的值。即使組合相同型別，標籤仍然保持不同。

#### 布林型別

型別 `𝟙 + 𝟙`，記為 `𝟚` 或 `TWO`，代表具有兩個值的一位元型別。依照慣例，`σᴸ⟨⟩` 代表 false/zero，而 `σᴿ⟨⟩` 代表 true/one。

### 積型別

積型別 `A × B` 包含值的配對，寫作 `⟨a, b⟩` 或 `(a, b)`。型別 `𝟚 × 𝟚` 有四個值，不同於 `𝟚 + 𝟚` 中的四個值。

### 核心 Simplicity 表達式

操作記為 `f : A ⊢ B`，意思是輸入型別為 `A`，輸出型別為 `B`。Simplicity 是「一階」的 — 它沒有函式型別。

### 兩個基本操作

核心語言提供兩個基本操作：

**恆等 (`iden`).** 恆等操作會原封不動傳遞其輸入：

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**單位 (`unit`).** 單位操作會丟棄其輸入並回傳空 tuple：

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

它們形成了每個型別各有一個操作的族。

### 三個組合組合子

循序組合使用 `comp f g`（寫作 `f ⨾ g` 或 `f >>> g`）：

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

平行組合使用 `pair f g`（寫作 `f ▵ g` 或 `f &&& g`）：

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

條件組合使用 `case f g : (A + B) × C ⊢ D`，讓各分支能存取共享環境 `C`：

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

為什麼條件組合採取這種形狀 — 一個和搭配一個共享環境 `C` — 而不是更簡單的 `copair f g : A + B ⊢ C`，僅僅挑選一個分支？因為裸的 `copair` 無法表達**分配**：也就是函式 `dist : (A + B) × C ⊢ A × C + B × C`，它會把共享輸入推入被採用的那個分支。透過把環境 `C` 直接建入 `case`，Simplicity 從單一組合子同時取得條件組合*與*分配 — 這是讓核心語言維持在九個組合子的重要設計決策之一。

### 另外四個組合子

積的消耗使用 `take` 與 `drop`：

**take** 取出左元素：

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** 取出右元素：

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

和的產生使用 `injl` 與 `injr`：

**injl** 以左標籤包裝：

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** 以右標籤包裝：

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### 九個核心組合子

總計來說，Simplicity 恰好有九個核心組合子：

| 組合子 | 用途 |
|---|---|
| `iden` | 傳遞輸入 |
| `unit` | 丟棄輸入 |
| `comp` | 循序組合 |
| `pair` | 平行組合 |
| `case` | 條件組合 |
| `take` | 從積中取出左側 |
| `drop` | 從積中取出右側 |
| `injl` | 注入到和的左側 |
| `injr` | 注入到和的右側 |

### Simplicity 與序列演算

Simplicity 的設計源自 Gentzen 序列演算的合取—析取片段。更精確地說，它是序列演算的*函式詮釋*的一種變體，而這本身類似於自然演繹與 lambda 演算之間的 Curry-Howard 對應。組合子規則呈現「前提中的型別小於結論中的型別」，使 Bit Machine — Simplicity 的抽象堆疊機直譯器 — 能在執行期間最小化資料複製。

### 值不是表達式

Simplicity 表達式表示操作，而不是值。記號 `scribe b : A ⊢ B` 表示一個永遠回傳值 `b` 的唯一表達式，它是記號上的便利，而不是組合子。這類似 Bitcoin Script，其中 `OP_1` 這樣的操作會推入值，而不是直接表達值。

### Simplicity 的完備性定理

有了所有九個組合子後，我們如何知道沒有缺少什麼 — 也就是這九個真的足夠？Simplicity 完備性定理回答了這一點：對於（有限）Simplicity 型別之間的任何函式，都有某個 Simplicity 表達式能表示它。此證明是建構性的 — 它展示如何建構該表達式：

1. **分解輸入**：使用巢狀 `case` 表達式，將任何型別的任何輸入完全分解為其組成位元
2. **建立查找表**：對每個可能輸入，使用 `scribe` 產生對應輸出
3. **組裝**：巢狀 cases 與 scribes 一起形成一個巨大的查找表，用來實作該函式

此定理已在 Rocq 證明輔助器（原 Coq）中形式化驗證。該證明是官方 Simplicity 儲存庫的一部分，並已由機器檢查其正確性。

雖然完備性定理保證 Simplicity 的九個組合子能表達（有限）Simplicity 型別之間的任何函式，但透過查找表建構得到的表達式實際上非常龐大。對 256 位元輸入的函式需要一個含有 2²⁵⁶ 個項目的查找表。這就是為什麼接下來的章節聚焦於建構能利用計算結構的高效率表達式，而不是用查找表暴力窮舉一切。

### 結論

Simplicity 的核心語言包含一套型別系統與組合子，可表達任何有限計算。雖然完備性定理保證了表達能力，但從泛用建構得到的表達式實際上非常龐大。實用的 Simplicity 開發需要利用計算結構來獲得簡潔表達式。接下來的章節將探索資料結構、交易互動，以及額外的組合子。

# 從資料型別到程式

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## 建構資料型別

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

前幾章中，我們展示了 Simplicity 的核心組合子集合足以實作任何有限純計算。本章會展示如何從這些原語建構實用的資料結構與計算 — 就像電腦是由邏輯閘建構而成一樣。

### 布林邏輯

布林型別記為 `𝟚`，等於 `𝟙 + 𝟙`，並有兩個值：`σᴸ⟨⟩`（false）與 `σᴿ⟨⟩`（true）。使用核心組合子即可建構布林邏輯運算子。

#### And 操作

邏輯 `and : 𝟚 × 𝟚 ⊢ 𝟚` 操作接受兩個位元並回傳一個位元。其實作會根據第一個位元分支：如果為 false，回傳 false；否則回傳第二個位元。

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

以 `⟨false, false⟩` 測試：

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

以 `⟨true, true⟩` 測試：

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### 其他邏輯操作

`not` 操作需要一個輔助組合子：

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

初始的 `iden ▵ unit : A ⊢ A × 𝟙` 會為輸入加入一個空「環境」，讓 `case` 組合子能夠套用。兩個分支中使用 `take` 會丟棄這個空環境，以執行 `f` 或 `g`。

其他布林邏輯操作：

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### 位元加法器

「半加器」接受兩個位元並將它們相加，產生兩位元輸出：一個進位位元與一個和位元。

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

「全加器」會將三個位元相加，產生兩位元輸出。輸入使用巢狀 tuple `(𝟚 × 𝟚) × 𝟚`。

對於巢狀 tuple，會使用緊湊記號：

- `O f` 表示 `take f`
- `I f` 表示 `drop f`
- `H` 表示 `iden`

例如，`I O H` 意思是 `drop (take iden) : A × (B × C) ⊢ B`，會取出中間的值。此記號讓人聯想到二進位數字：當把巢狀 tuple 想成二元樹時，該記號表示樹位置的反向二進位數字。這些表達式形成 Simplicity 的 De Bruijn 索引。

**注意：** `I`、`O` 與 `H` 記號只適用於僅由 `take`、`drop` 與 `iden` 組成的子表達式。

全加器會組合兩個半加器，並對進位位元取邏輯 `or`：

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

在第一行中，`take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` 會在前兩個位元上執行半加器，並保存最後一個位元。

在第二行中，`O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` 會保存第一個位元（第一個半加器的輸出進位），並在最後兩個位元上執行半加器。

在最後一行中，`(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` 會對前兩個位元（兩個半加器的輸出進位）取邏輯 OR，並回傳第二個半加器的輸出和位元。

這展示了 Simplicity 程式設計：使用 `I`、`O` 與 `H` 記號來引用資料位元，形成合適的「環境」，以便透過循序組合呼叫其他函式。

使用者不會直接定義低階操作。本系列後面會討論實作常見函式的標準函式庫 jets。終端使用者不被期待直接用 Simplicity 程式設計，這點類似 Bitcoin Script。相反地，像 SimplicityHL 這樣的高階語言會產生 Simplicity 程式碼，管理子表達式「環境」，並把具名變數翻譯成適當的 `take` 與 `drop` 序列。

### 向量

固定長度向量是透過形成型別 `A` 的迭代積來定義：

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

它們也可以寫成 `A^2`、`A^4`、`A^8` 等。

向量只為長度為二的冪次方而定義。其他冪次需要選擇括號結合慣例。

給定表達式 `f : A ⊢ B`，重複配對會把它「映射」到固定長度向量上：

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

給定函式 `f : A × B ⊢ B`，可在固定長度向量上迭代或「摺疊」：

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

存在許多變體。給定 `f : A × B ⊢ C`，可用 `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ` 在配對向量上進行 "zip"。給定 `f : (A × B) × C ⊢ C`，可用 `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C` 在配對向量上摺疊。結合 `map` 與 `fold-right` 會建立累積式組合子：`f : A × C ⊢ C × B` 產生 `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`。還有更多變體是可能的。

#### 多位元字

位元向量會產生多位元整數。例如，`𝟚³²` 是 32 位元字型別。`𝟚²⁵⁶` 是 256 位元字型別，適合雜湊與密碼學操作。

使用全加器，向量操作的一個變體會定義多位元字上的「漣波進位加法器」：

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` 接受兩個 n 位元二進位數字與一個一位元進位輸入，回傳一個一位元進位輸出旗標與一個 n 位元和。

#### SHA-256

透過遞迴定義多位元字上的算術操作 — 減法、乘法、除法 — 以及位元邏輯操作，例如邏輯 AND、OR、XOR，並反覆組合它們，甚至能建構 SHA-256 的區塊壓縮函式：

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256 壓縮使用 Simplicity 在 Rocq 證明輔助器（原 Coq）中形式化定義，並有形式化證明表明 `sha256-hash-block` 實作是正確的。

原始 Simplicity 形式的壓縮執行速度太慢。Jets 會以原生方式執行像 SHA-256 壓縮這樣的常見函式。純 Simplicity 實作則作為 jets 的形式化規格。

### Option 型別

Option 型別來自與單位型別取和：

```
Option A ≔ 𝟙 + A
```

型別 `Option A` 可以寫作 `A?` 或 `𝕊 A`（其中 `𝕊` 表示 "successor"）。函式可映射到 option 型別上：

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

也可以定義 monadic 組合子，例如 bind：

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### 變長緩衝區

「緩衝區」是部分填滿向量的型別：

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

型別 `Xᑉ⁸` 展開為 `(1 + X⁴) × ((1 + X²) × (1 + X))`。把它當作多項式並展開，得到 `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`。將其詮釋為型別時，它代表最多 7 個 X 的所有可能 tuple 的和，包括空 tuple。這正是長度嚴格小於 8 的 list 型別。

如同向量，也可以在緩衝區上定義映射與摺疊操作。堆疊操作包括 `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` 與 `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`。`push-<n` 會把一個項目附加到緩衝區；如果發生溢位，則回傳一個完整向量。`pop-<n` 會移除一個項目，回傳較小的緩衝區與被移除的項目；如果原始緩衝區為空，則可選地回傳 nothing。

`push-<n` 的遞迴定義如下：

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

原始 Simplicity 在超過某些複雜度層級後會變得難以閱讀。終端使用者會使用像 SimplicityHL 這樣的高階語言，由它產生這些慣用表達式。

### 結論

本章展示了如何從位元建構邏輯操作。由此產生了位元層級算術，使我們能對執行進行推理。接著發展了向量型別，展示如何在多位元字上迭代以定義算術。繼續下去，像 SHA-256 與 Schnorr 簽章驗證這樣的密碼學操作，也能只用 Simplicity 組合子定義 — 而這些其實全都已經用 Simplicity 定義。

本章不是所有可在 Simplicity 中建構的資料型別與操作的完整指南，而是說明如何在 Simplicity 的限制內達成實用功能。儘管型別受到有限界定，仍然可以定義有用的向量、緩衝區型別，以及迭代這些結構的操作。

實際標準函式庫操作規格與此處定義略有不同。例如，全加器使用 3-way XOR 與 "majority" 邏輯函式，而不是兩個半加器。

實務上，Simplicity 程式會使用 jets 進行算術與密碼學操作。不過，jets 只會替代表達式。迭代緩衝區與向量的組合子無法被 jets 取代，並會出現在實際 Simplicity 程式中。不過終端使用者並不是直接使用這些，而是使用像 SimplicityHL 這樣的高階語言，由它產生這類表達式。

遞迴定義的組合子看起來會讓表達式大小呈指數成長。這並不是問題。在序列化期間，表達式會被編碼為 DAG（有向無環圖），而不是樹。實際表示只會線性成長。

到目前為止，我們只考慮了純計算。若要與交易資料互動，以執行簽署交易這類任務，就需要某種方式讓程式在簽章無效時失敗。下一章會討論 Simplicity 中的副作用。

## 兩種副作用

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

前幾章中，我們展示了如何使用 Simplicity 的核心組合子集合建構一些資料結構與計算。如前所述，核心組合子足以實作任何有限純計算。這引出一個問題：還能做到什麼？我們可以為表達式加入額外副作用。

表達式可能有各式各樣的副作用：狀態更新、寫入日誌、拋出例外、從環境讀取、呼叫 continuation 等等。Simplicity 中可用的副作用會取決於應用。

對於 Bitcoin 與 Liquid 應用，目前我們有兩種副作用：Failure 效應，也就是例外型別為 `𝟙` 的例外效應；以及 Reader 效應，它允許存取交易環境中的資料。我們的核心組合子是「純」的；它們沒有副作用。不過，jets 可以引入具有副作用的新原語。

### 帶有效應的 Jets

本課程後面會更詳細談到 jets，但這裡先介紹幾個範例 jets 來說明它們的副作用。

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` 是一個 jet，用於某個表達式，該表達式接受一個 x-only 公鑰、一個 256 位元訊息，以及一個 Schnorr 簽章，並且什麼都不回傳！根據其型別，它應該與 `unit` 行為相同。差異在於該 jet 的副作用：如果簽章驗證失敗，整個計算就會透過拋出例外（單位型別）而中止。這就是 Failure 效應。

#### Verify

`verify : 𝟚 ⊢ 𝟙` 是一個用來表達 Failure 效應的極簡 jet。如果 `verify` 的輸入是 `false`，整個計算會透過拋出例外而中止。如果輸入是 `true`，則不回傳任何東西，但計算可以繼續。

#### 交易雜湊

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` 看起來像是一個常數函式，因為只有一個可能的輸入值：空 tuple。然而，這個 jet 會從交易環境讀取，並產生一個交易資料的雜湊，類似於 Bitcoin Script 簽章驗證中使用的 `SIGHASH_ALL` 訊息摘要。這是 Reader 效應的一個範例：回傳值取決於該 jet 執行所在的交易環境。還有其他幾個雜湊 jets 會雜湊交易環境資料的不同子集，以協助為簽章建構自訂訊息摘要。

#### 內省 Jets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` 是一個函式，接受一個輸入索引，並回傳該輸入的交易 sequence number；如果索引超出範圍，則可選地回傳 nothing。同樣地，輸出值不是輸入索引的純函式；相反地，該操作使用 Reader 效應存取交易環境，以判定輸出值。還有其他幾個內省 jets 會回傳交易環境資料的不同片段。

### 分類效應

並非所有副作用都一樣。有些副作用比其他副作用表現得更良好。我們可以根據它們對程式轉換的適應程度來分類效應。

#### 可交換效應

可交換效應是指：如果你交換兩個表達式的輸出，就能安全地交換表達式本身，而不改變表達式的效應。考慮 `swap = I H ▵ O H : A × B ⊢ B × A`。如果對每個帶有副作用的表達式 `f` 與 `g`，都有 `f ▵ g ⨾ swap = g ▵ f`，那麼這些效應就是可交換的。

從環境讀取交易資料是一種可交換效應，因為無論我們以什麼順序執行讀取，從環境讀取的結果都相同。

一般而言，拋出例外不是可交換效應。如果 `f` 拋出某個例外 `e₁`，而 `g` 拋出另一個例外 `e₂`，那麼從 `f` 與 `g` 的配對中拋出哪個例外，取決於它們的執行順序。

不過，在 Failure 效應的特殊情況中，由於只能拋出單位型別的例外，因此該效應是可交換的。無論 `f` 或 `g` 中哪一個拋出例外，結果例外都會相同，因為只有一個可能的例外值。

#### 冪等效應

冪等效應是指：如果你複製一個表達式的輸出，就能安全地複製該表達式本身，而不改變表達式的效應。考慮 `dup = iden ▵ iden : A ⊢ A × A`。如果對每個帶有副作用的 `f`，都有 `f ⨾ dup = dup ⨾ f ▵ f`，那麼這些效應就是冪等的。

從環境讀取交易資料是一種冪等效應。拋出例外也是一種冪等效應。雖然兩個複製出的表達式中只有一個會被執行，但 `dup ⨾ f ▵ f` 拋出的任何例外都會與 `f ⨾ dup` 拋出的例外相同。

不過，寫入日誌可能不是冪等的，因為複製該效應會讓日誌訊息出現兩次。然而，如果日誌由一組訊息的_集合_而不是一串訊息的_列表_構成，則該效應會是冪等的（且可交換），因為集合插入本身就是冪等操作。

#### 單位效應

單位效應是指：如果你丟棄一個表達式的輸出，就能安全地丟棄該表達式本身，而不改變表達式的效應。如果對每個帶有副作用的 `f`，`f ⨾ unit = unit` 永遠成立，那麼你的效應就是單位效應。

從環境讀取資料是少數幾種單位效應之一。如果從交易環境讀取資料的結果被丟棄，那麼執行該讀取的整個表達式也可以被丟棄。

Failure 效應不是單位效應。如果 `f` 拋出例外，那麼 `f ⨾ unit` 也會拋出；執行甚至不會到達 `unit` 組合子就已經中止。另一方面，`unit` 顯然不會拋出任何例外，所以 `f ⨾ unit` 與 `unit` 的效應會不同。

總結來說，上述效應在這三種性質上的表現如下：

| 效應 | 可交換 | 冪等 | 單位 |
| --- | :---: | :---: | :---: |
| Reader（交易環境） | ✓ | ✓ | ✓ |
| Failure（單位型別例外） | ✓ | ✓ | ✗ |
| Writer（作為集合的日誌） | ✓ | ✓ | ✗ |
| 一般例外（任意型別） | ✗ | ✓ | ✗ |

### Simplicity 中允許的效應

某種效應具備的良好性質越多，Simplicity optimizer 對使用這些效應的程式進行轉換的空間就越大。理想上，我們只允許同時具備三種性質的效應：可交換、冪等與單位。這會讓 optimizer 能執行任何它想要的程式轉換。不過，從環境讀取是唯一滿足這三種性質的效應。

因此，我們改為要求 Simplicity 效應必須可交換且冪等。我們在 Simplicity 中使用的兩種效應，也就是 Failure 效應與 Reader 效應，都是可交換且冪等的。這允許對 Simplicity 程式碼執行一大類最佳化。

不過，如果 `f` 可能產生 Failure 效應，則不允許進行上述「丟棄」轉換，也就是嘗試把 `f ⨾ unit` 替換為 `unit`，或任何類似轉換。確實，想像如果 `f` 包含一個 `bip0340-verify` 斷言，嘗試把這項檢查最佳化掉將會是災難性的。

### 為什麼要允許副作用？

Simplicity 為什麼要允許副作用？如果每個程式都把整筆交易當作輸入，並回傳一個判定交易是否有效的布林輸出，豈不是更好嗎？

#### 批次驗證

我們使用 Failure 效應的其中一個原因，是為了支援 Schnorr 簽章的[批次驗證](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification)。在批次驗證中，許多個別 Schnorr 簽章檢查會以某種方式匯集在一起，使得如果任何單一簽章檢查失敗，整個批次就會失敗。

這種批次程序比逐一驗證每個簽章更有效率。缺點是，如果批次驗證失敗，我們不會得知具體是哪一個或哪幾個簽章檢查失敗。

透過使用失敗副作用，`bip0340-verify` 確保如果簽章檢查失敗，整筆交易就會失敗。如果 `bip0340-verify` 反而回傳 `𝟚`，也就是布林型別，來表示成功或失敗，那麼失敗的簽章檢查仍可能導向一個腳本成功的分支。在這種情況下，我們就需要知道該特定簽章是否有效，因此無法利用批次驗證。

#### 預先計算的交易資料

早期 Bitcoin Script 中的一個問題是，用來為簽章建立訊息摘要的雜湊函式，其時間複雜度與交易大小呈線性關係。通常每個輸入至少會為簽章驗證建立一個訊息摘要，因此整體雜湊量會與交易大小呈二次關係。

此問題在 Segwit 以及 Bitcoin Script 後續迭代中被修正，方法是重新定義訊息摘要，使其能在每次簽章檢查中以常數時間計算。這依賴 `PrecomputedTransactionData`，它會先一次性預先計算交易資料的雜湊，然後由每個輸入的 sighash 計算共享。Simplicity 的交易雜湊 jets 依賴同類型的預先計算交易資料，以確保 jets 能在常數時間執行。

假設 `sig-all-hash` 沒有使用 Reader 效應。假設我們設法為交易環境建構了一個 Simplicity 型別。姑且稱它為 `TxEnv`，使得 `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` 成為該 jet 的型別。這樣的定義會要求 `sig-all-hash` jet 能夠計算任何交易的雜湊，而不只是它所涉入的那筆交易。Simplicity 程式可以複製給定的 `TxEnv`，並將修改後的副本傳給 `sig-all-hash`。在這種情況下，`sig-all-hash` 就不能依賴 `PrecomputedTransactionData`，而我們又會回到需要對傳入此版本 `sig-all-hash` 的任何交易資料花費線性時間。

因為 `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` 使用 Reader 效應來存取交易資料，所以它_只能_存取固定的交易環境。因此，該 jet 的實作可以安全地使用 `PrecomputedTransactionData` 並以常數時間運作。

### 跨輸入簽章聚合

雖然目前 Liquid 與 Bitcoin 都不支援[跨輸入簽章聚合](https://hrf.org/latest/cisa-research-paper/)，但我們希望確認 Simplicity 在時機到來時能與其相容。

雖然細節尚未敲定，我們想像半聚合會使用 Writer 效應來實作。也就是說，一個型別如 `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` 的新 jet，會接受一個公鑰、訊息摘要，以及 Schnorr 簽章的 `r`-component（Schnorr 簽章由 `r`-component 與 `s`-component 構成），並在繼續執行前將其寫入交易日誌。然後，在交易中的其他位置或與交易一起，會提供所有半聚合 Schnorr 簽章的聚合 `s`-component。只有在為所有已記錄的 key、message 與 `r`-component 提供這樣的聚合 `s`-component 時，交易才有效。

為了滿足 Simplicity 的要求，這個 Writer 效應需要是冪等且可交換的。這可以透過把 writer 日誌視為 key、message、`r`-component tuple 的集合來確保。這之所以可行，是因為集合操作是冪等且可交換的。把日誌視為值的集合，會與半聚合驗證演算法相容。

### 結論

本章探討了如何為 Simplicity 能做的計算加入副作用。我們依據各種效應相對於各種程式轉換的良好程度，分類了不同類型的效應。我們決定將 Simplicity 的效應限制為可交換且冪等的效應。

我們在 Bitcoin 與 Liquid 應用中使用的兩種效應，是用於存取交易環境的 Reader 效應，以及用於中止並使程式失敗的 Failure 效應。有些 jets 會使用可能發生這些副作用的原語操作。

Failure 效應決定 Simplicity 程式的輸出：程式要麼失敗，使交易無效；要麼成功。Reader 效應為 Simplicity 程式提供一種輸入：包含交易資料的環境。但我們也需要向 Simplicity 程式提供其他輸入，例如數位簽章。

下一章將探討什麼是 Simplicity 程式、它們如何轉換為位址，以及我們如何向 Simplicity 程式加入其他輸入，例如簽章。

## 程式與位址

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

上一章中，我們描述了 Simplicity 使用的兩種副作用：Failure 效應，它決定程式成功或失敗；以及 Reader 效應，它提供對交易環境的存取。現在我們轉向實務問題：Simplicity 程式到底是什麼，又如何成為區塊鏈上的位址？

### Simplicity 程式

Simplicity 程式被定義為型別為 `𝟙 ⊢ 𝟙` 的 Simplicity 表達式。這個型別簽章表示程式不接受有意義的輸入（只有單位值），也不產生有意義的輸出（只有單位值）。Reader 效應捕捉交易環境輸入，而 Failure 效應表示成功或失敗。這些效應處理 I/O，而不是由 Simplicity 型別本身處理。

### Commitment Merkle Root

Bitcoin 不是在鏈上儲存完整程式，而是採用承諾 — 這是一種從 Pay-to-Script-Hash (P2SH) 延伸而來的實務做法。Simplicity 使用 Commitment Merkle Root (CMR)。

每個組合子會收到一個 SHA-256 標籤，該標籤源自以下模式：`Simplicity␟Commitment␟[identifier]`，其中 `␟` 表示 ASCII code 31（unit separator）。

每個標籤都是以下列出的對應 pre-image 字串的 SHA-256 雜湊：

| 組合子 | 標籤 pre-image（ASCII 字串） |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

接著，Simplicity 表達式會被遞迴雜湊為 256 位元 CMR：對每個組合子，連同其參數的 CMR，一起計算帶標籤的 SHA-256 midstate（以 `#ᶜ(e)` 表示表達式 `e` 的 CMR，並以 `∥` 表示位元組串接）：

| 組合子 | CMR 規則 |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

二元組合子（`comp`、`pair`、`case`）會串接兩個子節點的 CMR；一元組合子（`take`、`drop`、`injl`、`injr`）會在 32 位元組的 `0x00` padding 後串接其單一子節點的 CMR；而零元葉節點（`iden`、`unit`）只雜湊其標籤。兩項慣例讓這件事計算起來很便宜：使用 SHA-256 midstates，因此**每個表達式最多只需要一次 SHA-256 壓縮函式呼叫**（假設到常數標籤為止的 midstate 已預先計算），而單引數構造子會以 32 位元組的 `0x00` padding 作為其引數前綴，這允許想要的實作進行一點額外預先計算。

對於 `unit` 組合子 — 一個沒有引數子表達式的零元構造子 — 此規則特化為 `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`，其中 `tag_unit = SHA-256(Simplicity␟Commitment␟unit)`（標籤會被餵入兩次）。平凡 `unit` 程式得到的 CMR 是：

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

關鍵在於，CMR 不承諾 Simplicity 表達式的型別，而是依賴贖回期間的型別推論。

### 位址

位址採用 BIP-0341 的 Taproot 機制，將 CMR 承諾在 TapLeaf version `0xbe` 之下。流程包括：

1. 計算 TapLeaf tagged hash，結合 version byte、CMR length 與 CMR 本身
2. tweak 一個內部公鑰（當不需要 key-spend path 時使用 NUMS point）
3. 轉換為 bech32m 格式
4. 加入適當的 checksum

當不需要 key-spend path 時，內部公鑰會設為 **NUMS**（"Nothing-Up-My-Sleeve"）點：這是一個刻意選擇的曲線點，使得沒有人知道它的離散對數 — 換言之，這個點沒有對應的私鑰。因為沒有人能為它產生簽章，所以 key-spend path 可證明地不可用，而該輸出*只能*透過已承諾的 Simplicity script path 花費。在真實應用中，這個 NUMS point 應依照 BIP-0341 的建議隨機化，使沒有 key-spend path 的輸出無法與一般 Taproot 輸出區分（這是一項隱私好處）。

#### 從 Simplicity 到位址

讓我們走完整個推導過程，使用最簡單的可能程式：`unit : 𝟙 ⊢ 𝟙`，一個永遠成功的 no-op。

**1. 組合子標籤。** 首先計算 `unit` 標籤：

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR。** 將標籤餵入兩次以取得程式的 CMR：

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash。** 在 CMR 前加上 Simplicity 的 TapLeaf version `0xbe` 與 CMR length `0x20`（32 位元組），然後取 Elements TapLeaf tagged hash（tagged hash 是 `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`）：

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

因為只有這一個 leaf，所以沒有 TapBranches，因此這個 hash 已經是 TapTree root。

**4. TapTweak。** 由於我們不想要 key-spend path，因此使用 BIP-0341 NUMS point 作為 internal key，並用 TapTree root 對其進行 tweak：

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. 輸出公鑰。** 在曲線上 tweak internal key，`output_pk = lift_x(internal_pk) ⊕ t·G`（此處摘要說明橢圓曲線算術），得到 x-only output key `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`。

**6. Bech32m 位址。** 編碼 x-only output key，前置一個 `p`（SegWit v1 witness-version 字元），加入 Liquid-testnet human-readable prefix `tex1`，並附加 Bech32m checksum。最終位址是：

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

這是很多工作 — 但其中大部分是 Taproot 本身要求的，而不是 Simplicity 要求的。

### 見證表達式

一種新的組合子型別處理了 Simplicity 程式缺乏輸入的問題：見證表達式。`witness` 組合子允許將簽章資料與其他見證材料整合到程式中。

```
      w : B
-----------------
witness w : A ⊢ B
```

見證表達式的語義很直接：它忽略其輸入，並單純回傳值 `w`（可以是任何 Simplicity 型別），也就是 `⟦witness w⟧(a) = w`。這**沒有增加新的表達能力** — 根據完備性定理，Simplicity 已經能建構任何這樣的常數函式（回想前幾章的 `scribe` 巨集）。`witness` 組合子的重點完全在於其 **CMR**：值 `w` 被**排除**在表達式的 CMR 之外，因此位址可以在 `w` 已知之前計算，而 `w` 則在贖回時提供。

此設計選擇支援剪枝 — 未執行的條件分支不需要在鏈上揭露，包括與其相關聯的見證表達式。當一個分支被剪枝時，驗證者只需要被剪枝子樹的 CMR，而不需要其實際內容。

### 見證值

見證表達式只能持有一個*值*，而不能持有更一般的 Simplicity 表達式，這可能看起來像是限制。但基於 UTXO 的區塊鏈程式只會執行一次。沒有必要把整個子表達式傳入見證節點：使用者可以在鏈下自行執行該子表達式，並把其輸出轉錄成見證值，以取得完全相同的結果。

（本課程稍後會遇到 `disconnect` 組合子，它的行為很像一個*確實*把整個 Simplicity 表達式作為引數的見證表達式。）

另一種設計是把所有見證資料作為頂層 Simplicity 程式的引數餵入。偏好見證表達式有兩個原因。第一，**剪枝**：`case` 表達式的未執行分支永遠不會在鏈上揭露，而那些分支內的任何見證表達式也會隨之被剪枝。第二，**局部性**：見證表達式讓我們能把每個見證值精確放在其被使用的位置，而不是從程式的頂層輸入一路穿線傳下去。

### 型別推論

由於 CMR 不承諾型別，型別系統會在贖回期間被重建。Simplicity 的型別推論演算法會根據組合子結構，判定每個子表達式的最小型別。更精確地說，推論會計算每個子表達式的*主*（最一般）型別；任何仍保持自由的型別變數接著會被實例化為單位型別 `𝟙`，從而為程式產生唯一、最小的型別。

### 結論

本章確立了 Simplicity 程式是型別為 `𝟙 ⊢ 𝟙` 的表達式，說明 Commitment Merkle Root 如何由每個組合子的帶標籤 SHA-256 雜湊建構而成，並展示 CMR 如何透過 BIP-0341 Taproot 轉換為鏈上位址。我們介紹了見證表達式，作為在花費時提供簽章資料與其他輸入的機制，同時不必在位址建立時承諾其值。

# 最後部分

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## 評論與評分

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## 期末考

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## 結論

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
