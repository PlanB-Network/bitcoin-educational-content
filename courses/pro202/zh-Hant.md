---
name: 編程 Bitcoin
goal: 從零開始建立完整的 Bitcoin 函式庫，瞭解 Bitcoin 的加密基礎
objectives: 

 - 在 Python 中實作有限欄位運算和橢圓曲線運算
 - 以程式化方式建構和解析 Bitcoin 交易
 - 建立 Testnet 位址並在網路上廣播交易
 - 掌握 Bitcoin 安全模型的數學基礎

---
# Bitcoin 的腳本與程式之旅


本密集課程為期兩天，由 Jimmy Song 授課，從基礎開始建立完整的 Bitcoin 函式庫，讓您深入了解 Bitcoin 的技術基礎。從有限字段和橢圓曲線的基本數學開始，您將進一步學習交易解析、腳本執行和網路通訊。透過在 Jupyter 記事本中的實作編碼練習，您將建立自己的 Testnet Address、手動建構交易，並直接將交易傳送至網路，同時深刻瞭解使 Bitcoin 和 Trustless 安全的加密原理。


享受您的發現！


+++

# 介紹

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## 課程概覽

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

歡迎來到課程 PRO 202 _**Programming Bitcoin**_，這是一段深入的旅程，將帶你從有限域算術一路學習到在比特幣測試網中建立並廣播真實交易。

在本課程中，您將逐步使用 Python 構建一個比特幣函式庫，同時掌握理解比特幣安全性與內部運作所需的密碼學、協議與軟體基礎。PRO 202 的方法完全以實踐為主：每個概念都會立即在 Jupyter 筆記本中實作，確保理論與程式碼相互強化。

### 比特幣的基本數學概念

本節首先建立不可或缺的數學基礎。您將實作有限域算術和橢圓曲線運算（群規律、加法、倍點、純量乘法……）——這些是 ECDSA 的先決條件。目標有二：理解使加密簽章成為可能的代數結構，並構建可靠的 Python 工具以便操作它們。

接下來，您將正式化 ECDSA 的各個組成部分：金鑰生成、點格式化、雜湊、簽章建立與驗證。本節將理論與實踐直接連結，強調實作細節及底層安全模型的穩健性。

### 比特幣交易的內部運作機制

在第二部分中，您將剖析比特幣交易的結構：UTXO、輸入/輸出、序列、腳本、編碼等。您將撰寫程式碼來構建、簽署和驗證交易，從而準確理解雜湊所承諾的內容及其原因。

接下來，您將實作一個最小化的 _Script_ 執行器，檢視關鍵操作碼，並驗證支出路徑。目標是使您能夠稽核交易行為、診斷驗證失敗，並推理支出政策的安全性。

### 比特幣網路的內部運作機制

在第三部分中，您將把交易置於更廣泛的系統中：區塊結構、區塊標頭、難度以及工作量證明（Proof-of-Work）機制。您將處理協議訊息、區塊標頭和默克爾樹。

最後，您將研究點對點節點通訊、訊息最佳化以及SegWit 的引入。

與 Plan ₿ Academy 的每門課程一樣，最後一部分包含一個旨在鞏固您理解的評估。準備好揭示比特幣的內部運作機制，並編寫驅動它的程式碼了嗎？讓我們開始吧！

# Bitcoin 的基本數學概念

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## 實施 Bitcoin 的數學

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## 橢圓曲線密碼學

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin 交易內部工作

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin 交易解析與 ECDSA 簽署

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin 腳本與交易驗證

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## 交易建置與付款到腳本 Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin 網路內部結構

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin 區塊和 Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## 網路通訊與 Merkle Trees

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## 進階節點通訊與分離見證

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# 最後部分


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## 評論與評分


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## 總結


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
