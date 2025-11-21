---
term: NSEQUENCE
---

Bitcoin 交易項目中的 `nSequence` 欄位用來表示此項目的時間鎖定方式。最初，它的目的是允許在 mempool 中動態更換交易，以啟用類似 Lightning 的支付系統覆蓋。但是，隨著 BIP68 中相對時間鎖定的引入，它的用途也發生了變化。現在，「nSequence」欄位可指定交易納入區塊前的相對延遲時間。這個延遲可以區塊的數量來定義，也可以是 512 秒的倍數 (也就是實時)。需要注意的是，只有當 `nVersion` 欄位大於或等於 `2`時，這種對 `nSequence` 欄位的新詮釋才有效。對 `nSequence` 欄位的這個解釋是在 Bitcoin 的共識規則層級。此外，在標準化規則的層級上，這個欄位也用於信令 RBF (Replace-by-fee)。如果一個交易包含一個低於 `0xfffffffe` 的 `nSequence` ，那麼它可以在遵循此政策的節點上透過 RBF 被取代。