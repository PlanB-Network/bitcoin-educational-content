---
term: ANONSETS (匿名集)
---

匿名集用作评估特定UTXO隐私级别的指标。更具体地说，它们衡量在包括所研究硬币的集合中不可区分的UTXO的数量。由于需要一组相同的UTXO，匿名集通常在一系列coinjoin中计算。在适当的情况下，它们允许判断coinjoin的质量。较大的匿名集意味着更高的匿名级别，因为在集合中区分特定的UTXO变得困难。有两种类型的匿名集：
* 预期匿名集；
* 回顾性匿名集。

第一种指的是在已知输入UTXO的情况下，被隐藏的研究UTXO所在的群体的大小。这个指标允许衡量硬币隐私对从过去到现在（输入到输出）的分析的抵抗力。在英语中，这个指标的名称是“*forward anonset*,” 或 “*forward-looking metrics*。”

![](../../dictionnaire/assets/39.png)

第二种指的是在已知输出UTXO的情况下，给定硬币的可能来源数量。这个指标允许衡量硬币隐私对从现在到过去（输出到输入）的分析的抵抗力。在英语中，这个指标的名称是“*backward anonset*,” 或 “*backward-looking metrics*。”

![](../../dictionnaire/assets/40.png)

> ► *在法语中，通常接受使用术语“anonset”。然而，它可以被翻译为“ensemble d'anonymat”或“potentiel d'anonymat”。在英语和法语中，术语“score”有时也用来指代匿名集（预期得分和回顾得分）*。