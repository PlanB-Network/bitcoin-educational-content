---
term: 匿名集 (Anonsets)
definition: 通過計算集合中不可區分的UTXO數量來衡量UTXO隱私程度的指標，通常在coinjoin之後。
---
Anonset 用作評估特定 UTXO 隱私程度的指標。更具體而言，它們衡量包含所研究幣的集合中不可區分的 UTXO 數量。由於需要一組相同的 UTXO，anonset 通常在 coinjoin 週期內計算。在必要時，它們可用於評估 coinjoin 的品質。較大的 anonset 意味著更高程度的匿名性，因為在集合中辨識特定的 UTXO 變得更加困難。

Anonset 分為兩種類型：forward anonset（forward-looking metrics）；以及 backward anonset（backward-looking metrics）。有時也會使用「*score*」一詞來指稱 anonset。

第一個指標表示在已知輸入 UTXO 的情況下，被研究的輸出 UTXO 所隱藏的集合規模。該指標可用於衡量該幣種在從過去到現在的分析（從輸入到輸出）下的隱私抗性。第二個指標表示在已知輸出 UTXO 的情況下，某一幣種可能的來源數量。該指標可用於衡量該幣種在從現在到過去的分析（從輸出到輸入）下的隱私抗性。
















