---
name: 編程 Bitcoin
goal: 從零開始建立完整的 Bitcoin 函式庫，瞭解 Bitcoin 的加密基礎
objectives: 

 - 在 Python 中實作有限欄位運算和橢圓曲線運算
 - 以程式化方式建構和解析 Bitcoin 交易
 - 建立測試網路位址並透過網路廣播交易
 - 掌握 Bitcoin 安全模型的數學基礎

---
# Bitcoin 的腳本與程式之旅


本密集課程為期兩天，由 Jimmy Song 授課，從基礎開始建立完整的 Bitcoin 函式庫，讓您深入了解 Bitcoin 的技術基礎。從有限字段和橢圓曲線的基本數學開始，您將進一步了解交易解析、腳本執行和網路通訊。透過 Jupyter 記事本中的實作編碼練習，您將建立自己的 testnet 位址、手動建構交易，並直接將交易傳送至網路，同時深刻瞭解使 Bitcoin 變得安全無虞的密碼原則。


享受旅程！


+++

# 簡介


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## 課程總覽


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


歡迎來到課程 PRO 202 _**Programming Bitcoin**_，這是一個密集的旅程，帶您從有限場運算一直到在 Bitcoin 的 Testnet 上建立和廣播真正的交易。


在本課程中，您將逐步在 Python 中建立 Bitcoin 函式庫，同時掌握精確推理 Bitcoin 安全性和內部運作所需的密碼、協定和軟體基礎。PRO 202 採用徹底的實作方法：每個概念都會立即在 Jupyter 筆記本中實作，確保理論與程式碼互相強化。


### Bitcoin 的基本數學概念


第一節將建立不可或缺的數學基礎。您將實作有限場運算和橢圓曲線運算 (群法、加法、倍增、標量乘法...) - ECDSA 的先決條件。我們的目標有二：瞭解使加密簽章成為可能的代數結構，並建立可靠的 Python 工具來操作它們。


接下來，您將正規化 ECDSA 的組成部分：金鑰產生、點格式化、雜湊、簽章建立和驗證。本節直接將理論與實務相連結，強調實作細節和底層安全模型的穩健性。


### Bitcoin 交易內部運作


在第二部分，您將剖析 Bitcoin 交易的結構：UTXO、輸入/輸出、序列、腳本、編碼等。您將撰寫程式碼來建構、簽署和驗證交易，精確了解散列所承諾的內容和原因。


接下來，您將實作一個最小的 _Script_ 執行器、檢閱關鍵操作碼，並驗證支出路徑。目標是讓您能夠審核交易行為、診斷驗證失敗，並推理支出政策的安全性。


### Bitcoin 網路內部運作


在第三部分中，您將把交易放在更廣泛的系統中，包括區塊結構、標頭、難度和 Proof-of-Work 機制。您將會處理協定訊息、區塊標頭和 Merkle 樹。


最後，您將學習對等節點通訊、訊息最佳化以及 SegWit 的介紹。


如同 Plan ₿ Academy 的所有課程一樣，最後部分包含一個評估，旨在鞏固您的理解。準備好揭開 Bitcoin 的內部運作，並寫出為其提供動力的程式碼嗎？讓我們開始吧！










# Bitcoin 的基本數學概念

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## 實施 Bitcoin 的數學

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin 程式設計基礎：核心數學結構


本課程將 Bitcoin 密碼系統背後的基本數學知識濃縮在高度實用的工作流程中。本課程會先解釋概念，以範例進行示範，然後在 Jupyter Notebook 中實作。課程的指導思想很簡單：只有編寫了密碼，才能真正理解密碼的基本原理。在為期兩天的課程中，學生會學習 generate 測試網路位址、建立並廣播[交易](https://planb.academy/resources/glossary/transaction-tx)，最後在沒有區塊探索器的情況下與網路互動。所有這些都需要在有限域和橢圓曲線方面打下堅實的基礎。


### 有限域：密碼學的算術引擎


有限域 F(p) 是由素數 p 定義的算術系統，包含 0 到 p-1 的元素。素數域確保每個非零元素都有一個逆數，而且所有的運算都維持在該域內。算術運算使用 modulo p 來進行加法、減法和乘法。Python 的 `pow(base, exp, mod)` 實現了高效率的模乘，這對於實際加密運算中使用的大指數是非常重要的。


#### 乘法行為

將任何非零元素 k 與素數字段的所有元素相乘，會產生該字段的變換。此特性可保證一致性並防止結構上的弱點，使得素數字段成為安全金鑰產生和[數位簽章](https://planb.academy/resources/glossary/digital-signature)的理想選擇。


#### 除法和費馬小定理

除法是透過乘法反演來實現的。費馬小定理指出

n^(p-1) ≡ 1 (mod p)、

所以倒數是 n^(p-2)。Python 用 `pow(n,-1,p)`直接支援這一點。這些操作經常出現在 [ECDSA](https://planb.academy/resources/glossary/ecdsa) 和 Bitcoin 的底層加密例程中。


### 橢圓曲線：公鑰安全的非線性結構


Bitcoin 使用 secp256k1，定義為有限域上的 y² = x³ + 7。橢圓曲線上的點在點相加下形成一個數學群。通過兩個點 P 和 Q 所畫的線與曲線相交於第三個點 R；將 R 反射過 x 軸會得到 P + Q。


倍增點使用的是切線而非割線，斜率來自於曲線的導數。雖然這些公式涉及實數上的微積分，但是當曲線定義在有限域上時，這些公式就變得完全離散且精確了 - 這就是 Bitcoin 所使用的情境。


### 從數學到 Bitcoin 密碼學


有限字段提供了確定性、可反轉的算術；橢圓曲線則提供了非線性結構，在此結構中，計算 k-P 非常容易，但反轉則在計算上並不可行。結合兩者，就能為 Bitcoin 的公鑰/私鑰、ECDSA 簽署和交易安全奠定基礎。了解這些基礎後，學生就可以直接實作金鑰、交易和簽章，而無需抽象或外部工具。


## 橢圓曲線密碼學

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


本章將介紹定義在有限域上的橢圓曲線，並解釋為什麼橢圓曲線是 Bitcoin [密碼學](https://planb.academy/resources/glossary/cryptography)的數學骨幹。實數上的橢圓曲線看起來平滑且連續，但在有限域上運用相同的方程式卻會產生離散、分散的點集。儘管在視覺上有差異，但所有點的加法公式、斜率和代數規則的表現完全相同，只是運算方式改成模組運算。Bitcoin 使用曲線 y² = x³ + 7 (secp256k1)，它保留了對密碼安全性非常重要的對稱性和非線性行為。


### 驗證點與有限場實作


驗證 F₁₃₇ 上的點如 (73,128)，需要檢查 y² mod p 是否等於 x³ + 7 mod p。運算符號的重載可確保所有的算術運算 - 加法、乘法、幂次運算、除法 - 都會自動以 modulo p 執行。一旦有了這些抽象概念，更進階的加密運算就可以直接編寫和推理。


#### 群組屬性與點數相加

橢圓曲線的點在加法下形成一個數學群。這個群體滿足封閉性、關聯性、同一性 (無窮遠處的點) 以及反演 (橫跨 x 軸的反射)。幾何結構確認了這些屬性，使得標量乘法 (P 重複加到本身) 定義良好。這些群組規則使橢圓曲線加密技術得以實現，並確保在重複的點運算下有一致、可預測的行為。


### 循環群與離散對數問題


在曲線上選擇一個產生點 G 可以讓我們 generate 一個循環群：G, 2G, 3G, ...，nG = 0。這些點看起來是非線性和不可預測的，即使是依序產生。這種不可預測性為離散對數問題奠定了基礎：計算 P = sG 很容易，但從 P 決定 s 對於大型群組而言，在計算上並不可行。這個單向函數就是公開密碼匙加密法的安全性所在。標（私人密碼鑰）以小楷書寫；點（公開密碼鑰）則以大楷書寫。


#### 高效的標量乘法

為了有效率地計算 sG，實作使用了雙加演算法：掃描標量的二進制表示，每一步將點加倍，只有當位元為 1 時才加上 G。這將計算從 O(n) 加法減少到 O(log n)，即使是 256 位元的標量也能進行實際的加密操作。


#### Bitcoin 中的 secp256k1 曲線


Bitcoin 使用曲線 secp256k1，定義為 y² = x³ + 7 在素數域上，其中 p = 2²⁵⁶ - 2³² - 977。產生點 G 有固定的座標，使用確定的 NUMS (「我袖中無物」) 程序選擇。群階 n 是接近 2²⁵⁶ 的大素數，確保每個非零點都會產生相同的群。2²⁵⁶ (~10⁷⁷) 的大小是一個天文數字，使得強制[私密金鑰](https://planb.academy/resources/glossary/private-key)在物理上是不可能的。即使有上萬億台超級電腦運行上萬億年，也無法有效地縮小金鑰空間。


### 公用鑰匙、私人鑰匙和 SEC 序列化


私密金鑰是隨機標量 s；[公開金鑰](https://planb.academy/resources/glossary/public-key)是 P = sG。由於求解離散對數問題並不可行，所以 P 可以在不透露 s 的情況下共用。公開金鑰必須使用 SEC 格式進行序列化傳輸。未壓縮的 SEC 格式使用 65 個位元組：前綴 0x04 + x 坐標 + y 坐標。壓縮格式只使用 33 個位元組：前綴 0x02 或 0x03（取決於 y 的奇偶校驗）+ x 坐標。Bitcoin 原本使用未壓縮的金鑰，但為了提高效率，現在改用壓縮金鑰。


#### Bitcoin Address 創建


Bitcoin 位址是公開金鑰的哈希值，而非原始金鑰本身。若要 generate 位址，請以 SEC 格式序列化公開金鑰，計算 hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256) 然後是 RIPEMD-160)，預先加上網路前綴 (mainnet 為 0x00，testnet 為 0x6F)，使用雙 SHA-256 計算校驗和，附加前四個校驗和位元組，並使用 Base58 對結果進行編碼。此編碼會移除含糊不清的字元，並包含校驗和，以防止轉錄錯誤。這個多步驟的管道隱藏了公開金鑰，直到花費發生，增加了網路識別，並確保地址是人類可讀的、防錯的。


# Bitcoin 交易內部運作

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin 交易解析和 ECDSA 簽署

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### 瞭解 ECDSA：Bitcoin 的數位簽章基礎


Bitcoin 依賴 ECDSA，這是一種以橢圓曲線為基礎的簽章方案，提供遠比 RSA 更小的金鑰大小，卻有很強的安全性。它的安全性來自橢圓曲線離散對數問題：給定 P = eG，計算 P 很容易，但從 P 推導出 e 在計算上並不可行。這種非對稱性使公開金鑰加密得以實現，同時保持私人金鑰的安全。


#### ECDSA 簽署的 DER 編碼


Bitcoin 使用 DER 格式編碼 ECDSA 簽章：


- 0x30 (序列標記)
- 長度
- 0x02 + 長度 + R 位元組
- 0x02 + 長度 + S 位元組


這會增加開銷，將 64 位元組的簽章擴大到 ~71-72 位元組。[Taproot](https://planb.academy/resources/glossary/taproot) 採用固定大小的 [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) 簽章，消除了這種低效率的情況。


### 簽署承諾與簽署程序


ECDSA 簽署依賴於承諾方程式：UG + VP = KG。簽章者選擇非零的 U 和 V 值，以及隨機的 [nonce](https://planb.academy/resources/glossary/nonce) K，證明知道私密金鑰，但不會洩露私密金鑰。訊息散列到 Z 中，隨機 K 產生，R 是 KG 的 x 坐標，S = (Z + RE)/K。簽章是一組 (R、S)。安全性主要取決於使用獨一無二、不可預測的 K - 如果 K 被重複使用或洩漏，私密金鑰就會被破解。現代的實作使用確定的 K 產生 (RFC 6979) 來避免 RNG 失敗。


#### 簽名驗證

給定 Z、(R, S) 和公開金鑰 P，驗證者會計算 U = Z/S 和 V = R/S，然後檢查 UG + VP 的 x 坐標是否等於 R。偽造簽名需要解決離散對數問題或破解散列函數。


#### Schnorr 簽名與歷史背景


Schnorr 簽署在數學上較為簡潔，並支援聚合功能，但在 Bitcoin 推出時已取得專利。ECDSA 提供了免費的替代方案，但複雜度較高，簽章也較大。隨著專利到期，Bitcoin 透過 Taproot 新增 Schnorr 簽署，提供固定的 64 位元組簽章，並改善隱私性。為了與舊版相容，ECDSA 仍然受到支援。



### 交易結構和輸入/輸出


Bitcoin 交易包括：


- 版本（4 位元組，little-endian）
- 輸入清單
- 輸出清單
- 鎖定時間 (4 位元組)


輸入透過交易切細值和輸出索引參考先前的 [UTXO](https://planb.academy/resources/glossary/utxo)，並包括解鎖[指令碼](https://planb.academy/resources/glossary/script) (scriptSig) 和用於時間鎖定或 RBF 的序列號。輸出指定金額 (8 位元組) 和鎖定腳本 (scriptPubKey)，定義支出條件。Bitcoin 位址是這些腳本的代表。


#### UTXO 機型

Bitcoin 追蹤的是未動用的產出，而不是帳戶餘額。UTXOs 必須完全花費 - 部分花費是不可能的。要從 100 BTC UTXO 中花費 1 BTC，交易必須包含變更輸出。若忘記變更輸出，剩餘部分就會變成礦工費。


#### 事務序列化與解析


交易使用精簡的二進位格式。在版本欄位之後，一個 varint 編碼輸入的數量。輸入包括


- 上一個傳送雜湊 (32 位元組)
- 輸出索引 (4 位元組)
- scriptSig (varstr)
- 序列 (4 位元組)


輸出包括 8 位元組的金額和 scriptPubKey (varstr)。鎖定時間控制交易何時生效。序列化對大多數的整數使用 little-endian 排序。解析器依序消耗位元組，並將輸入、輸出及腳本委託給專門的類別。


### 費用、變更和可塑性


費用是隱含的：

費用 = sum(輸入值) - sum(輸出值)。

任何未指定的值都會變成費用，因此正確的變更輸出結構是非常重要的。在 [SegWit](https://planb.academy/resources/glossary/segwit) 之前，簽章允許延展性，將 S 修改為 N-S，會產生一個具有不同 ID 的新有效交易。Bitcoin 現在強制執行低 S 規則，而 SegWit 則將簽章與 txid 計算隔離，使 ID 變得穩定，並支援 [Lightning](https://planb.academy/resources/glossary/lightning-network) 等第二層協議。


## Bitcoin 腳本與交易驗證

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script 是一種小型、以堆疊為基礎的智慧契約語言，它定義了如何使用硬幣。每個輸出都帶有一個 scriptPubKey（鎖定腳本），每個輸入都帶有一個 scriptSig（解鎖腳本）。這兩個腳本共同組成了一個程式，必須評估為 "true"，花費才有效。腳本故意不是圖靈完備的，因此所有的執行路徑都是可預測的，並容易在整個網路中驗證。


### 腳本作業與執行模式


腳本是一連串的資料元素和操作碼。資料推送 (簽章、公鑰、雜湊) 會放置在堆疊上，而以 `OP_` 開頭的操作碼會轉換堆疊。執行後，堆疊頂端的元素必須非零才算成功。範例：`OP_DUP` 複製頂端元素，`OP_HASH160` 應用 SHA256 然後再 RIPEMD160，`OP_CHECKSIG` 針對交易的 sighash 和公開金鑰驗證簽章，推 1 為有效，推 0 為無效。解析規則會區分原始資料 (長度前綴) 與操作碼 (依位元組值查詢)，並由小型虛擬機器在每個[節點](https://planb.academy/resources/glossary/node)上確定地執行這些規則。


### P2PK 和 P2PKH：核心付款模式


最早的模式，Pay-to-Public-Key (P2PK)，直接將硬幣鎖定在完整的公開金鑰上：scriptPubKey 是 `<pubkey> OP_CHECKSIG`，而 scriptSig 只是一個簽章。它簡單但不佔空間，而且在花錢之前就暴露了公開金鑰。


#### P2PKH 和地址

Pay-to-Public-Key-Hash (P2PKH) 透過鎖定到 20 位元組公開金鑰的雜湊值，改善了這一點。scriptPubKey 是 `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`，scriptSig 提供 `<signature> <pubkey>`。執行時會檢查所提供的公開金鑰是否已切細到已承諾的值，然後驗證簽章。這會隱藏公開金鑰直到花費時間，減少大小，並符合熟悉的 "1..." 地址格式。mainnet 位址格式。


### 交易驗證與簽章切分


驗證交易的節點必須確保：

1) 每項輸入都會參考現有的未使用輸出。

2) 輸入總值 ≥ 輸出總值（差額即為費用）。

3) 每個 scriptSig 都能正確解鎖其參考的 scriptPubKey。


簽名驗證需要建構已簽名的確切訊息，稱為 scriptSig。對於傳統 ECDSA，驗證會清空所有 scriptSig，將目前輸入的 scriptSig 替換成對應的 scriptPubKey，附加一個 4 位元組的散列類型 (通常是 `SIGHASH_ALL`)，然後將結果進行雙散列。這個 256 位元的值就是 `OP_CHECKSIG` 所使用的。其他的散列類型 (例如 `SINGLE`、`NONE`、有或沒有 `ANYONECANPAY`)，會改變交易的哪些部分會被承認，因此可以用於協同集資或部分指定交易等特殊用例，但實際上很少使用。


#### 四元雜湊和 SegWit

由於傳統交易中的每個輸入都需要在包含所有輸入的結構上進行自己的 sighash 運算，因此驗證時間可能會隨著輸入的數量呈二次方成長。大型多輸入交易曾經造成明顯的驗證延遲。SegWit 重新設計了 sighash 計算，以快取共用部分，並將複雜度降低為線性時間，從而改善了可擴展性，並使拒絕服務攻擊更加困難。


### 腳本謎題和安全課程


腳本所能表達的遠遠不止「一個簽名就能解開這些硬幣」這麼簡單。Script 謎題透過編碼任意條件來證明這一點 - 數學問題、哈希預映像挑戰，甚至是碰撞賞金 - 只要提供正確的資料，任何人都可以使用這些硬幣。然而，僅依賴公開資料（無簽名）的輸出很容易受到[礦工](https://planb.academy/resources/glossary/miner)前置運行的影響：一旦一個有效的解決方案出現在 [mempool](https://planb.academy/resources/glossary/mempool) 中，任何礦工都可以複製它並將報酬重定向到自己身上。


實際的經驗是，真實世界的合約幾乎總是包含簽名檢查，即使合約包含更複雜的邏輯，例如多重簽名、時間鎖或哈希鎖。簽名可將解決方案與特定的一方綁定，以維護獎勵機制，並防止其他人竊取報酬。了解 Script 的堆疊模型、標準模式和微妙的陷阱，對於設計安全的 Bitcoin 智慧型契約，以及推理交易在網路上實際如何驗證，都是非常重要的。


## 交易建置與付款到腳本 Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### 建立 Bitcoin 交易和 P2SH


Bitcoin 交易建構將理論上的通訊協定知識與實際執行結合起來。交易選擇要花費的 UTXO，使用鎖定腳本建立輸出，為每個輸入建立簽章，並將所有內容序列化為節點所期望的格式。這個過程需要瞭解 sighash 產生、腳本行為，以及正確的費用和變更處理。


### 基本交易架構


每個交易輸入都會透過 txid 和索引引用先前的輸出。輸出指定以 Satoshis 和鎖定腳本為單位的金額。總輸入與總輸出的差額就是費用。要簽署一個輸入，交易的修改版本會被序列化，它的 sighash 會被計算出來，而私密金鑰會簽署它。結果簽章和公開金鑰會形成 ScriptSig。一旦每個輸入被簽署，原始交易就可以廣播到網路。


### 多重簽名交易


Bare multisig 使用 `OP_CHECKMULTISIG` 來要求 m-of-n 簽名。由於早期的 off-by-one bug，OP_CHECKMULTISIG 消耗了一個額外的堆疊元素，在 ScriptSig 中需要一個初始的 `OP_0`。裸 multiisig 功能強大但效率低：所有公開金鑰都會出現 on-chain，使得 scriptPubKeys 變得龐大、昂貴，而且難以編碼為位址。這些限制促成了 pay-to-script-hash 的引入。


#### P2SH 架構

P2SH 將複雜的腳本隱藏在 20 位元組的 HASH160 之後。scriptPubKey 是固定的：`OP_HASH160 <20 byte hash> OP_EQUAL`。底層的贖回指令碼 (包含多重身分、時間鎖或其他條件) 只有在支出時才會顯示和執行。寄件者只看到雜湊值，而收件者則私下管理兌換腳本。這種設計減少了 on-chain 的大小，提高了隱私性，並且在不加重寄件者負擔的情況下實現了複雜的合約。


### P2SH 支出與實施


要使用 P2SH 輸出，ScriptSig 必須包含必要的解鎖資料 * 以及贖回指令碼本身。驗證分兩步進行：

1) HASH160(redeem_script) 必須與 scriptPubKey 切細值相符。

2) 驗證完成後，使用提供的資料執行贖回指令碼。


為 P2SH 輸入產生簽章時，sighash 程序會使用 redeem script 來取代 scriptPubKey。每個簽章者都必須具備完整的 redeem script 才能產生 generate 的有效簽章。P2SH 位址在 mainnet 上使用版本位元組 0x05（"3... 「位址），在 testnet 上使用 0xC4（」2... "位址）。


#### 實用的安全考量


丟失兌換腳本意味著丟失資金：花費需要私人密碼匙和兌換腳本本身。Multisig 參與者在接受存款前，必須確認其公開金鑰已正確包含在內。P2SH 支援多重簽名、時間鎖和哈希鎖等先進結構，但腳本邏輯中的錯誤可能會永久鎖定資金，因此在 testnet 上進行測試非常重要。


P2SH 改善了隱私性，在第一次花費前隱藏了花費條件，但一旦兌換腳本出現 on-chain，它就會永久可見。儘管如此，P2SH 在縮小體積、向後相容和彈性合約支援等方面的優點，使得 P2SH 成為一個重要的里程碑，影響了後來的升級版本，例如 SegWit 和 Taproot。


# Bitcoin 網路內部運作

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin 區塊和 Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin [區塊](https://planb.academy/resources/glossary/block)使用 [proof of work](https://planb.academy/resources/glossary/proof-of-work) 組合交易並保護交易。每個區塊包含一個 80 位元組的[標頭](https://planb.academy/resources/glossary/block-header)和交易清單。儘管製造一個有效區塊的能源成本很高，但驗證一個區塊的成本卻很低：儲存所有 ~900k 標頭只需要 ~72 MB，即使是小型裝置也能有效地驗證鏈上的 proof of work。


### Coinbase 交易和區塊獎勵


每個區塊都以一筆 [Coinbase 交易](https://planb.academy/resources/glossary/coinbase-transaction)開始 - 這是新比特幣進入流通的唯一方式。它有一個歸零的 prev-tx 散列值和一個 0xffffffffff 的索引，唯一地識別它。補貼從 50 BTC 開始，每 210,000 個區塊（50, 25, 12.5, 6.25, 3.125, ...）減半。礦工也包括交易費用。由於 4 字節 nonce 對於現代 ASIC 而言太小，因此礦工會修改 Coinbase 交易中的資料，以變更 [Merkle](https://planb.academy/resources/glossary/merkle-tree) 根並創造額外的搜尋空間。BIP34 要求在 Coinbase scriptSig 中嵌入區塊高度，以確保每個 Coinbase txid 都是唯一的。


### 區塊標頭欄位和 Soft Fork 訊號


80 字節的標頭包含


- 版本 (4 位元組)
- 上一區塊切細值 (32 位元組)
- Merkle 根 (32 位元組)
- 時間戳記 (4 位元組)
- 位元 (困[難度](https://planb.academy/resources/glossary/difficulty)目標，4 位元組)
- nonce (4 位元組)


版本號透過 [BIP9](https://planb.academy/resources/glossary/bip) 演變成位元信號系統，允許礦工協調 [soft-fork](https://planb.academy/resources/glossary/soft-fork) 的準備狀態。時間戳是 32 位元的 Unix 時間值，需要在 2106 年左右更新。


#### 位元領域與目標

位元欄位以精簡的形式編碼目標：目標 = 系數 × 256^(指數-3)。有效的區塊雜湊必須低於此目標值。由於雜湊會被詮釋為 little-endian 整數，因此當以十六進位顯示時，有效的雜湊通常會出現許多尾零。


### 難度、驗證與調整


Difficulty 定義為 lowest_target / current_target，表示 mining 目前的難度比最容易的難度高多少。驗證只需要比較標頭的哈希值與目標值，相對於 mining 來說非常便宜。


每個 2016 區塊，Bitcoin 都會調整難度，以 ~10 分鐘的區塊間隔為目標。該調整將前一個 2016 區塊的實際時間與預期的兩週時間進行比較。限制將調整限制在 4 倍之內。當雜湊率急劇下降、難度下調以補償時，重大的真實事件 - 例如中國的 mining 禁運 - 展示了此機制的彈性。


### 整體補貼與總計 Supply


高度 h 的補貼計算為：補貼 = 5_000_000_000 >> (h // 210_000)。這會產生減半時間表，收斂到總供應量 ~2100 萬 BTC。總和的幾何數列 (50 + 25 + 12.5 + ...) × 210,000 說明了上限。礦工可以要求少於允許的補貼，但絕不能超過，否則該區塊將變為無效。隨著補貼在連續的半價中縮減，交易費成為礦工收入和長期網路安全越來越重要的組成部分。


## 網路通訊與 Merkle Trees

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin 網路架構


Bitcoin 的[點對點](https://planb.academy/resources/glossary/peertopeer-p2p)網路以分散式八卦系統的方式運作，節點在不互相信任的情況下傳遞交易和區塊。新節點透過聯絡由核心開發人員維護的硬碼 DNS 種子來啟動。這些 DNS 種子會傳回活躍對等體的 IP，讓節點能夠發現網路，然後透過 getaddr 要求其他對等體。由於網路並不是[共識](https://planb.academy/resources/glossary/consensus)的關鍵，因此只要共識規則不變，實作方式可能會有所不同。


### 訊息結構與握手


所有 Bitcoin P2P 訊息都使用固定的封套：4 位元組 Magic Value (F9BEB4D9 for mainnet)、12 位元組 ASCII 指令、4 位元組 little-endian payload length、4 位元組 checksum (hash256 的前 4 位元組) 以及 payload。常見的指令包括 version、verack、inv、getdata、tx、block、getheaders、headers、ping 及 pong。


當連線節點傳送版本訊息時，握手就開始了。接收方回復 verack 和它自己的版本。一旦雙方交換了這兩個訊息，連線就啟動了，節點就可以開始轉送庫存和資料。


### Merkle 樹和 Merkle 根


Bitcoin 在每個區塊標頭中儲存一個 32 位元組的 Merkle 根，作為對區塊中所有交易的承諾。交易會進行[散列](https://planb.academy/resources/glossary/hash-function) (hash256)、配對、串聯，並重複散列，直到剩下一個散列為止。當一層有奇數時，最後一個哈希值會被重複。在內部，哈希值是 big-endian，而序列化的區塊資料則使用 little-endian，因此需要在樹狀結構建立前後顛倒。


#### 梅克尔证明和 SPV

Merkle 證明允許在不下載整個區塊的情況下驗證交易是否包含在區塊中。該證明由沿著通往根目錄的路徑的兄弟哈希值組成。輕量級 SPV 用戶端僅儲存區塊標頭，並向[完整節點](https://planb.academy/resources/glossary/full-node)請求這些證明。由於 Merkle 樹會以對數成長，因此證明包含數千筆交易的區塊只需要幾百個位元組。


Taproot 擴展了這個概念，將支出條件提交到 Merklized script tree (MAST)，只揭露執行的分支以及 Merkle 證明。這同時提高了效率和隱私性。


### 網路作業與區塊同步


節點使用 getdata 來請求交易或區塊，指定一個類型 ID (1=tx, 2=block, 3=filtered block, 4=compact block) 加上一個 32 位元組識別碼。對於連鎖同步，節點會傳送包含起始區塊切細值的 getheaders，最多會收到 2000 個標頭回應。每個回傳的標頭為 80 位元組，接著是一個 0 的假交易計數。


完全驗證已接收的區塊需要進行兩項檢查：

1.區塊切細值必須低於位元欄位編碼的目標值。

2.從所有交易計算出來的 Merkle 根（使用適當的 endianness 處理）必須與標頭的根相符。


只有當這兩個條件都成功時，節點才會接受該區塊，這反映了 Bitcoin 的「不要相信，要驗證」原則。


## 進階節點通訊與分離見證

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


本課程將先進的 P2P 網路與 Segregated Witness 統一，展示現代 Bitcoin 軟體如何直接與節點互動，同時使用 SegWit 感知的交易結構。開發人員可學習擷取區塊、掃描相關的交易，以及僅使用原始網路通訊來建構交易 - 不需要區塊探索器。


### 基於區塊的交易擷取與隱私權


[錢包](https://planb.academy/resources/glossary/wallet)必須藉由掃描區塊，找出符合其 scriptPubKey 的輸出，來偵測收到的付款。檢索整個區塊比請求個別交易更能保護隱私，因為個別交易會洩露使用者活動的強烈訊號。即使是區塊請求也可能會洩漏低流量鏈上的資訊，因此精簡區塊篩選器 (BIP158) 對於保護隱私的輕型用戶端而言是不可或缺的。篩選器可能會產生誤判，但絕不會產生誤判，讓用戶端只下載可能相關的區塊，而不會洩露特定位址。


### Trustless 網路互動


`get_block` 工作流程展示了正確的網路使用方式：傳送 getdata、接收區塊、然後獨立驗證其 Merkle root 和 proof of work。只有當接收到的標頭切細值與要求的切細值相符，且計算出的 Merkle 根與標頭相符時，才會接受區塊。這體現了「不要相信，要驗證」，確保即使是惡意的對等方也無法欺騙節點接受篡改的資料。


#### 從區塊擷取交易

可以使用簡單的迭代掃描區塊的交易，尋找匹配的 scriptPubKeys。生產型錢包會在新區塊到達時持續執行這項工作，嚴格透過加密驗證來證明輸出的所有權，而非依賴第三方 API。


### SegWit 目標與設計


Segregated Witness (SegWit) 透過從 txid 計算中移除簽名資料來修正交易的可篡改性。這使得可靠的預簽交易鏈得以實現，並使 Lightning Network 變得實用。SegWit 也使用「區塊權重」增加區塊容量：舊節點仍可看到 ≤1 MB 的區塊，而升級後的節點則可驗證包括見證資料在內高達 4 MB 的區塊。版本化的見證程式 (v0-v1 到目前為止) 為未來的腳本類型建立了結構化的升級路徑。


#### P2WPKH (原生 SegWit)


P2WPKH 以 22 位元組的腳本取代傳統的 P2PKH 結構：OP_0 + push20 + hash160(pubkey)。花費將簽章和 pubkey 移到單獨的見證欄位。


- Pre-SegWit 節點：請參閱「任何人都可以花費」，將其視為有效。
- 後 SegWit 節點：識別 OP_0 + 20 位元組切細值，並使用見證資料進行驗證。


這種分離方式可修復延展性並降低費用。見證使用 varint 計數，接著是簽章和公開金鑰。


#### P2SH-P2WPKH (向後相容 SegWit)


為了允許舊錢包傳送至 SegWit 位址，P2WPKH 腳本可以用 P2SH 包裝。


- scriptPubKey: 標準 P2SH hash160(redeemScript)
- scriptSig: redeemScript (P2WPKH 程式)
- 見證：簽名 + 公鑰


驗證層：

1.Pre-BIP16 節點接受 redeemScript 為有效。

2.後 BIP16 節點會評估它，在堆疊上留下 OP_0 + hash。

3.SegWit 節點執行完整的見證驗證。


#### 適用於複雜腳本的 P2WSH


P2WSH 透過提交 SHA256(script)，而非 hash160，將 SegWit 延伸至多位元和進階腳本。典型的 2 對 3 多重認證證書堆疊：


- 空元素 (CHECKMULTISIG bug)
- sig1
- sig2
- 見證腳本


SegWit 節點驗證 SHA256(witnessScript) 與 scriptPubKey 切細值相符，然後執行它。使用 SHA256 和 32 位元組的切細值可以區別 P2WSH 和 P2WPKH，並加強安全性。


#### P2SH-P2WSH (最大相容性)


複雜的 SegWit 指令碼也可以用 P2SH 包裝：


- scriptSig: redeemScript (OP_0 + 32 位元組雜湊值)
- 見證：簽名 + 見證Script


與 P2SH-P2WPKH 完全一樣，驗證會經過三代規則。這個封裝程式對於早期 Lightning 部署所需的多重認證（multisig）而無延展性（malleability）是不可或缺的。雖然原生的 P2WSH 是當今的首選，但包裝形式確保了舊版 wallet 系統的相容性。


### SegWit 的影響


提供了 SegWit：


- 穩定的交易 ID
- 透過折扣證人資料降低費用
- 透過區塊權重提高區塊吞吐量
- 舊節點相容性
- Taproot 和未來擴充的簡易升級路徑


這些工具與無信任的網路互動一起，構成了現代 Bitcoin 開發的骨幹。



# 最後部分


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## 評論與評分


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## 期末考試


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## 總結



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>