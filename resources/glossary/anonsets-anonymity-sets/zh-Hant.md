---
term: 匿名集
---

Anonsets 可作為評估特定 UTXO 隱私級別的指標。更明確地說，它們衡量的是包含所研究硬幣的集合內無法區分的 UTXOs 數量。由於需要一組完全相同的 UTXOs，anonsets 通常是在一個硬幣接合週期中計算出來的。在適當的情況下，它們允許判斷硬幣接合的品質。大的匿名集意味著匿名程度的提高，因為很難在集合中區分出特定的 UTXO。有兩種類型的匿名集：


- 前瞻性匿名集；
- 回溯匿名集。


第一個指標表示所研究的 UTXO 所隱藏的群組大小，知道輸入時的 UTXO。這個指標允許測量硬幣隱私對從過去到現在（輸入到輸出）的分析的抵抗力。在英文中，這個指標的名稱是 "*forward anonset*「，或 」*forward-looking metrics*"。


![](../../dictionnaire/assets/39.webp)


第二個指標顯示特定硬幣的可能來源數量，知道輸出端的 UTXO。這個指標允許測量硬幣隱私對從現在到過去（輸出到輸入）的分析的抵抗力。在英文中，這個指標的名稱是 "*backward anonset*「，或 」*backward-looking metrics*"。


![](../../dictionnaire/assets/40.webp)


> ► *在法語中，一般接受使用 "anonset "一詞。不過，也可翻譯為 "ensemble d「anonymat「 或 」potentiel d」anonymat"。在英文和法文中，"score "一詞有時也被用來指代 anonsets（前瞻性 score 和回溯性 score）*。