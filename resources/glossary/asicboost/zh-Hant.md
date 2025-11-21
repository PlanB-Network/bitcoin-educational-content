---
term: ASICBOOST
---

ASICBOOST 是 2016 年發明的演算法最佳化方法，旨在透過減少每次嘗試標頭的 Hash 所需的計算量，將 Bitcoin Mining 的效率提高約 20%。此技術利用了 Mining 使用的 SHA256 Hash 函式的一項功能，即在處理資料之前將資料分割成區塊。ASICBOOST 在多次散列嘗試中保留其中一個區塊不變，允許 Miner 在多次嘗試中只做這個區塊的部分工作。這種資料共用方式可以重複使用先前的計算結果，從而減少找到有效 Hash 所需的總計算次數。


ASICBOOST 可以兩種形式使用：Overt ASICBOOST 和 Covert ASICBOOST。Overt ASICBOOST 形式對每個人都是可見的，因為它涉及使用區塊的 `nVersion` 欄位作為 Nonce，而不改變真正的 `Nonce`。Covert 形式則是利用 Merkle 樹來隱藏這些修改。然而，由於第二個 Merkle Tree，增加了使用第二個方法所需的計算次數，自從 SegWit 推出後，這第二個方法就變得不那麼有效了。


總而言之，ASICBOOST 可讓礦工不必為所有散列嘗試執行真正完整的 SHA256，因為部分結果保持不變，這可加快礦工的工作速度。