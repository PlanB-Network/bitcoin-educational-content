---
term: UTREEXO
---

由 Tadge Dryja 設計的通訊協定，使用基於 Merkle 樹的累加器壓縮 Bitcoin 節點的 UTXO 集。與需要大量儲存空間的經典 UTXO 集不同，Utreexo 只儲存 Merkle Tree 根，大幅減少了所需的記憶體。這可讓節點驗證交易輸入中使用的 UTXO 是否存在，而無需保留完整的 UTXO 集。透過使用 Utreexo，每個節點只保留稱為 Merkle Root 的加密指紋。當進行交易時，使用者會提供 UTXOs 的 Ownership 證明和相對應的 Merkle 路徑。因此，節點可以驗證交易，而無需儲存整個 UTXO 集。讓我們以圖表來舉例了解這個機制：


![](../../dictionnaire/assets/15.webp)


在這個範例中，為了方便理解，我故意將 UTXO 設定縮小為 4 個 UTXO。實際上，要想像一下，在寫這些線條的時候，Bitcoin 上有將近 1.4 億個 UTXO。在這個圖中，Utreexo 節點只需要在 RAM 中保留 Merkle Root。如果它收到花費 UTXO 3 號（黑色）的交易，證明將由下列 Elements 組成：


- UTXO 3；
- Hash 4；
- Hash 1-2.


Utreexo 節點利用交易傳送者傳送的這些資訊，執行下列驗證：


- 它會計算 UTXO 3 的印記，從而得到 Hash 3；
- 它將 Hash 3 與 Hash 4 連結起來；
- 它會計算他們的印記，從而得到 Hash 3-4；
- 它將 Hash 3-4 與 Hash 1-2 連結起來；
- 它會計算他們的印記，從而得到 Merkle Root。


如果它透過程序取得的 Merkle Root 與儲存在 RAM 中的 Merkle Root 相同，那麼它就會相信 UTXO No.

此方法可降低 Full node 操作員對 RAM 的需求。然而，Utreexo 也有其限制，包括因額外證明而增加區塊大小，以及 Utreexo 節點可能依賴 Bridge 節點來取得遺失的證明。橋接節點是傳統的完整節點，提供必要的證明給 Utreexo 節點，從而允許完整的驗證。這種方法提供了效率與分散性之間的折衷，讓資源有限的使用者更容易進行交易驗證。