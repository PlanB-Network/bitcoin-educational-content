---
term: 匿名集

---
匿名集是评估特定 UTXO 隐私水平的指标。更具体地说，它们衡量的是包括所研究硬币在内的集合中无法区分的UTXO的数量。由于需要一组完全相同的UTXO，因此匿名集通常是在一个硬币连接周期内计算得出的。在适当的情况下，它们可以用来判断硬币拼接的质量。大的匿名集意味着匿名程度的提高，因为很难区分集合中的特定UTXO。匿名集有两种类型：


- 预期匿名集；
- 回溯匿名集。

第一个指标表示所研究的UTXO在知道输入UTXO的情况下，被隐藏在其中的群体的大小。该指标可以测量硬币的隐私对从过去到现在（输入到输出）的分析的阻力。该指标的英文名称为 "*forward anonset*"或 "*forward-looking metrics*"。

![](../../dictionnaire/assets/39.webp)

第二个指标是在了解输出端的 UTXO 后，显示特定硬币的可能来源数量。这个指标可以测量硬币的隐私对从现在到过去（从输出到输入）的分析的阻力。该指标的英文名称为 "*backward anonset*"或 "*backward-looking metrics*"。

![](../../dictionnaire/assets/40.webp)

> ► *在法语中，人们普遍接受使用 "anonset "一词。不过，也可译为 "ensemble d'anonymat "或 "potentiel d'anonymat"。在英语和法语中，"score "一词有时也用来指anonset（前瞻性评分和回顾性评分）*。