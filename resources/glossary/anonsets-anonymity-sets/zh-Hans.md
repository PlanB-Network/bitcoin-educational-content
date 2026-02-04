---
term: 匿名集 (Anonsets)

definition: 通过计算集合中不可区分的UTXO数量来衡量UTXO隐私程度的指标，通常在coinjoin之后。
---
Anonset 用作评估特定 UTXO 隐私程度的指标。更具体而言，它们衡量包含所研究币的集合中不可区分的 UTXO 数量。由于需要一组相同的 UTXO，anonset 通常在 coinjoin 周期内计算。在必要时，它们可以用于评估 coinjoin 的质量。较大的 anonset 意味着更高水平的匿名性，因为在集合中区分某个特定 UTXO 变得更加困难。

Anonset 分为两种类型：forward anonset（forward-looking metrics）；以及 backward anonset（backward-looking metrics）。术语 "*score*" 有时也用于指代 anonset。

第一个指标表示在已知输入 UTXO 的情况下，被研究的输出 UTXO 所隐藏的集合规模。该指标可用于衡量该币种在从过去到现在的分析（从输入到输出）下的隐私抗性。第二个指标表示在已知输出 UTXO 的情况下，某一币种可能的来源数量。该指标可用于衡量该币种在从现在到过去的分析（从输出到输入）下的隐私抗性。











