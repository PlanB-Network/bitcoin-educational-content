---
name: 深入 Simplicity
goal: 掌握 Simplicity 的设计哲学、类型系统和完整生命周期
objectives:
  - 理解三种基本组合方法以及构成完整语言的九个组合子
  - 从 Simplicity 的最小类型系统构建布尔逻辑、算术和 SHA-256
  - 掌握 Failure 和 Reader 副作用如何实现真正的区块链交互
  - 了解 Simplicity 程序如何变成 Taproot 地址，并通过见证数据赎回
---

# 深入 Simplicity

本课程基于 Simplicity 在 Blockstream Research 的创造者 [Dr. Russell O'Connor](https://r6.ca/) 撰写的完整五篇 ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) 文章系列，深入探讨 Simplicity 语言背后的理论和设计决策。本课程解释的是 Simplicity *为什么* 被设计成这样，而不是如何编写 Simplicity。

本课程沿着 O'Connor 博士的文章展开，依次讲解组合计算的三种基本方式、最小类型系统及其完备性定理、从第一原则构建实用数据类型和算术、为区块链交互谨慎引入副作用，最后说明程序如何被承诺到地址并在链上赎回。

+++

# 引言

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## 课程概览

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

欢迎来到 SCR403 — 深入 Simplicity！

本课程基于 [Blockstream](https://blockstream.com/) 基础设施技术开发者、Simplicity 创造者 [Dr. Russell O'Connor](https://r6.ca/) 撰写的 **"Delving Simplicity"** 文章系列。原文发布在 [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) 论坛上，并构成本课程的主要来源材料。我们感谢他的开创性工作，是它使这份教育内容成为可能。

### 你将学到什么

本课程探讨 Simplicity 背后的设计哲学和数学基础。Simplicity 是下一代脚本语言，已于 2025 年 7 月在 [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) 上激活。本课程遵循完整的五篇文章系列，并组织为两个主要内容部分：

1. **Simplicity 基础** — 为什么区块链计算需要一种根本不同的语言，组合操作的三种方式（顺序、并行、条件），以及构成数学上完备语言的九个核心组合子
2. **从数据类型到程序** — 从第一原则构建布尔逻辑、算术和 SHA-256；理解实现区块链交互的 Failure 和 Reader 副作用；并学习程序如何通过承诺 Merkle 根被承诺到 Taproot 地址，并用见证数据赎回

### 先修知识

这是一门**专家级**课程（约 10 小时）。你应当熟悉：
- 基本的 Bitcoin 脚本概念（交易验证做什么）
- 基本的编程概念（类型、函数、组合）
- 熟悉一些数学记号会有帮助，但并非必需。我们会在过程中逐步介绍一切

### 关键资源

- **原始文章**：Dr. Russell O'Connor 在 Delving Bitcoin 上撰写的 ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary)
- **Simplicity 代码库**：[BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — 源代码和 Rocq 形式化证明
- **官方网站**：[simplicity-lang.org](https://simplicity-lang.org/) — 文档和 SimplicityHL 参考
- **Blockstream 博客**：[Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — 技术概览

准备好深入探索 Bitcoin 工程中最优雅的作品之一了吗？开始吧！

## 什么是 Simplicity？

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

如果你在没有 Simplicity 背景的情况下学习本课程，本章会在我们深入难点之前帮助你建立方向感。

### 简而言之，Simplicity 是什么

Simplicity 是一种 **Bitcoin 原生智能合约语言**，如今已在 Liquid Network 上运行。它最早由 Dr. Russell O'Connor 大约在 2012 年构想，并在其 2017 年论文 *Simplicity: A New Language for Blockchains* 中详细阐述；经过多年形式化验证和开发后，于 2025 年 7 月在 Liquid Network 上激活。

不同于 Ethereum 的 Solidity（图灵完备的高级合约语言），Simplicity 有意保持最小化。它拥有：
- **三种类型构造子**（单位、和、积）
- **九个组合子**（基本操作和组合规则）
- **没有循环、没有递归、没有动态内存**

仅凭这些原语，你就可以构建交易验证所需的任何计算，从布尔逻辑到完整的 SHA-256 哈希。

### 今天你可以用 Simplicity 做什么？

Simplicity 已经在 Liquid Network 上为真实应用提供支持。其中最值得注意的是 [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/)，这是一个无需预言机的期权市场，用户使用 USDt 作为抵押品交易 L-BTC 看涨期权（底层合约也支持看跌期权）。其他已上线的 Simplicity 项目包括 SideSwap 的 [Swaption](https://swaption.io/)（期权）以及 Resolvr 的开源项目 [Deadcat](https://github.com/Resolvr-io/deadcat)（预测市场）。在 DeFi 之外，Simplicity 还能实现高级花费条件，例如保险库、限制条款和复杂的多签方案；这些条件在 Bitcoin Script 中要么不可能，要么不安全。

### 本课程是什么 — 以及不是什么

这**不是**一门动手编码教程。你不会在这里编写 Simplicity 程序。如果你想学习这部分，请查看：
- [simplicity-lang.org](https://simplicity-lang.org/) — 官方文档和 SimplicityHL 高级语言
- [Simplicity GitHub 代码库](https://github.com/BlockstreamResearch/simplicity) — 参考实现、示例和 Rocq 证明
- [Blockstream 博客文章](https://blog.blockstream.com/en-simplicity-github/) 关于如何入门

本课程**关注的是**：Simplicity 设计背后的**哲学和技术选择**。为什么要以这种方式创建这门语言？为什么只有九个组合子？为什么没有递归？为什么类型系统与 Gentzen 的相继式演算相连这件事很重要？

可以把它理解为：学习**为什么发动机被这样构建**，而不是学习如何驾驶汽车。

### 本课程适合谁？

本课程非常适合：
- 想在编写代码之前理解 Simplicity 基础的**协议开发者**
- 对形式化验证和类型论方法感兴趣的 **Bitcoin 研究者**
- 对相继式演算与区块链计算之间联系感到好奇的**计算机科学家**
- 想超越表层理解、深入掌握 Liquid 脚本能力的**高级 bitcoiner**

如果“和类型”、“组合子”或“相继式演算”等术语对你来说完全陌生，不必担心，我们会从零开始解释一切。但也请准备好踏上一段密集的数学旅程。

### 从文章到课程

Dr. O'Connor 的原始 "Delving Simplicity" 系列由五篇技术文章组成。本课程将这些材料重新组织并加以注释，形成一条循序渐进的学习路径，并在过程中通过测验检验你的理解。这些思想、定义和证明都属于他，我们只是将格式改编为结构化教育内容。

# Simplicity 基础

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## 组合计算的基本方式

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

既然 Simplicity 已经在 Liquid Network 上激活，我想深入探讨一下 Simplicity 语言的哲学和设计。

Bitcoin 的交易验证与常规编程语言设计是显著不同的应用场景。区块空间成本很高，因此程序需要紧凑。Bitcoin 交易中的程序只会在单个输入上执行，并且每个人都在同一个输入上执行该程序。此外，授权交易的主体已经提前知道计算结果：即交易是有效的。

通常，授权主体会运行成本高得多的计算来推导见证数据，以证明交易有效；而在区块链上运行的程序只需要检查见证数据是否有效。检查有效性往往比证明有效性便宜得多。

我们在设计 Simplicity 时就考虑到了这些独特的语言设计挑战。例如，Simplicity 要求未执行分支被剪枝，因此它们不会出现在区块链上。预处理步骤被精心设计为在 Simplicity 程序大小上表现出（准）线性时间复杂度。使用静态分析而不是“gas”，因为 gas 无法在不以规定方式执行代码的情况下计算；这样，执行模型的细节就不会变成共识关键。执行期间不进行动态内存分配。等等。

在深入 Simplicity 的设计细节之前，我想先以一些编程哲学开启这个系列，讨论将基本构建块组合成新功能的一般方式。

### 组合

假设有人正在为像 Bitcoin 这样的区块链设计一种可编程交易语言。尤其是，程序只能访问交易数据和输入的 UTXO 数据，并且执行只决定交易有效性（这使得执行结果可以被缓存）。假设我们从一组基本操作开始，这些操作可以执行各种任务，例如基本计算、读取和/或处理交易中的数据，以及签名验证。每个操作消耗某种类型的输入（可能为空）并返回某种类型的输出。我们可以用哪些方式将这些基本操作组合成更复杂的操作？

### 顺序组合

![顺序组合](assets/en/001.webp)

最基本的组合方法是顺序组合。如果我们有两个基本操作，其中一个操作的输出数据类型与另一个操作的输入数据类型匹配，那么我们就可以将这两个操作组合成一个新的复合操作。这个新操作按顺序运行这两个基本操作：以第一个操作的输入作为输入，将第一个操作的输出传递给第二个操作的输入，并最终返回第二个操作的输出。

当然，我们不需要将自己限制在只组合基本操作上。既然我们已经有了一些复合操作，也可以用函数组合继续组合它们。

在数学中，这种顺序组合通常就被称为“组合”，人们可能会以为这是组合事物的唯一方式。然而，我们还有其他组合操作的方式。

### 并行组合

![并行组合](assets/en/002.webp)

假设我们有两个操作，它们可以是基本操作，也可以是复杂操作，并且它们都接受同一类型的输入。组合这两个操作的第二种基本方式，是在同一个输入上同时执行它们。这称为并行组合，输出类型是原始两个操作输出类型的“积”，并包含这两个输出组成的对。

虽然这被称为“并行”组合，而且这两个操作原则上可以并行执行，但并行执行并不是操作上的要求。我们可以通过先执行一个操作再执行第二个操作，以“顺序”的方式实现并行组合。只要输出相同，我们并不关心并行组合是如何实现的。

### 条件组合

![条件组合](assets/en/003.webp)

条件组合是并行组合的对偶。在这种情况下，我们有两个产生相同输出的操作，并通过选择其中一个来执行而将它们组合起来。这个复合操作的输入是原始操作输入类型的“和”或“带标签联合”。在这个例子中，标签“Left”或“Right”是输入数据中的单个位，它决定所携带的是哪种类型的数据，从而决定两个操作中哪一个可以被执行。

即使输入是两个相同类型的和，条件组合也以同样方式运行。和类型仍然包含一个标签，而该标签的值决定两个操作中哪一个将被执行。

### Bitcoin Script 中的组合

在各种编程语言中，有许多方式可以实现这三种组合。在 Bitcoin Script 中，顺序组合（近似地）通过连接两个例程来实现（这就是为什么 Bitcoin Script 被称为连接式编程语言），因为一个例程的输出留在栈上，供后续例程消费。并行组合通过使用复制和交换操作操纵栈来实现，使得两个例程可以在同一个输入上运行。事情并不完全直接，因为我们称为类型“积”的东西通常是通过使用多个栈项来实现的。希望你能看出总体思路。

条件组合当然是通过 `OP_IF` 实现的，它根据栈上的值进行分支。在这种情况下，栈顶项扮演标签的角色，而栈上的下一个或多个项通常属于不同的“类型”，这些类型取决于标签的值。对于每种情况，栈项类型可能只适合由 `OP_IF` 中的某个分支处理。然而，当我们到达 `OP_ENDIF` 之后，栈项必须具有一致的“类型”，使得剩余脚本能够独立于先前选择的分支继续执行。

### Simplicity 中的组合

我们设计 Simplicity 时使用了直接实现这三种组合形式的组合子。再加上一些用于支持与积类型和和类型相关的其他基本操作的组合子，Simplicity 核心语言最终由九个组合子组成，足以表达任何有限计算。我们将在下一章更详细地讨论这一点。

### 第四种组合

在结束之前，我们应该提到，计算机科学中至少还有另一种组合，称为“递归组合”。在递归组合中，一个操作会被迭代多次。

请注意，Bitcoin Script 不支持递归组合；类似地，我们也明确将无界递归排除在 Simplicity 的设计之外。我们的论点是，无界迭代计算更适合使用递归限制条款实现，使其在多笔交易上进行计算。这允许用户避开区块空间和标准性约束，并更好地预测交易成本。

话虽如此，也有办法滥用 Simplicity 的委托功能来提供某种类似无界递归组合的东西，我们或许会在本系列后面讨论。

### 结论

我们回顾了三种主要的组合形式，它们用于将基本操作转化为复杂操作：

- 顺序组合
- 并行组合
- 条件组合

我们讨论了这些组合形式如何在 Bitcoin Script 中实现，并提示了它们如何影响 Simplicity 语言的设计。我们注意到，第四种组合，即递归组合，被 Simplicity 和 Bitcoin Script 特意排除。

在下一章中，我们将描述构成 Simplicity 语言核心的九个组合子，说明它们如何直接实现这三种组合形式，以及这如何形成一门用于描述任何有限计算的完整语言。

## Simplicity 的组合子完备性

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

在本章中，我们介绍 Simplicity 核心语言，并说明这门语言是完备的，也就是说，任何有限计算都可以在其中表达。

### Simplicity 类型

Simplicity 支持三种基本类型构造子。积类型 `A × B` 表示并行组合的输出，而和类型 `A + B`（带标签联合）处理条件组合的输入。第三种类型是单位类型。

### 单位类型

单位类型，记作 `𝟙` 或 `ONE`，只包含一个值：空元组 `⟨⟩` 或 `()`。这种零位数据类型不携带任何信息。

### 和类型

和类型 `A + B` 将两种类型与表示“左”或“右”的标签组合起来。值写作 `σᴸ(a)` 或 `inl(a)` 表示左标签值，写作 `σᴿ(b)` 或 `inr(b)` 表示右标签值。即使组合相同类型，标签仍然保持不同。

#### 布尔类型

类型 `𝟙 + 𝟙`，记作 `𝟚` 或 `TWO`，表示一个具有两个值的一位类型。按照约定，`σᴸ⟨⟩` 表示 false/zero，而 `σᴿ⟨⟩` 表示 true/one。

### 积类型

积类型 `A × B` 包含值对，写作 `⟨a, b⟩` 或 `(a, b)`。类型 `𝟚 × 𝟚` 有四个值，这不同于 `𝟚 + 𝟚` 中的四个值。

### 核心 Simplicity 表达式

操作记作 `f : A ⊢ B`，意思是输入类型为 `A`，输出类型为 `B`。Simplicity 是“一阶”的 — 它没有函数类型。

### 两个基本操作

核心语言提供两个基本操作：

**恒等 (`iden`)。** 恒等操作将其输入原样传递：

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**单位 (`unit`)。** 单位操作丢弃其输入并返回空元组：

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

它们形成族，每种类型都有一个操作。

### 三个组合组合子

顺序组合使用 `comp f g`（写作 `f ⨾ g` 或 `f >>> g`）：

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

并行组合使用 `pair f g`（写作 `f ▵ g` 或 `f &&& g`）：

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

条件组合使用 `case f g : (A + B) × C ⊢ D`，让分支能够访问共享环境 `C`：

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

为什么条件组合采用这种形状 — 一个和类型与共享环境 `C` 配对 — 而不是更简单的 `copair f g : A + B ⊢ C`，仅仅选择一个分支？因为裸露的 `copair` 无法表达**分配**：函数 `dist : (A + B) × C ⊢ A × C + B × C` 会把一个共享输入推入被选择的分支。通过把环境 `C` 直接构建进 `case`，Simplicity 用单个组合子同时获得条件组合*和*分配 — 这是将核心语言压缩到九个组合子的关键设计决策之一。

### 另外四个组合子

积的消费使用 `take` 和 `drop`：

**take** 提取左元素：

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** 提取右元素：

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

和的生成使用 `injl` 和 `injr`：

**injl** 用左标签包装：

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** 用右标签包装：

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### 九个核心组合子

总而言之，Simplicity 正好有九个核心组合子：

| 组合子 | 用途 |
|---|---|
| `iden` | 将输入原样传递 |
| `unit` | 丢弃输入 |
| `comp` | 顺序组合 |
| `pair` | 并行组合 |
| `case` | 条件组合 |
| `take` | 从积中提取左侧 |
| `drop` | 从积中提取右侧 |
| `injl` | 注入到和的左侧 |
| `injr` | 注入到和的右侧 |

### Simplicity 与相继式演算

Simplicity 的设计源自 Gentzen 相继式演算的合取-析取片段。更准确地说，它是相继式演算的*函数式解释*的一种变体，而后者本身类似于自然演绎与 lambda 演算之间的 Curry-Howard 对应。组合子规则表现出“前提中的类型小于结论中的类型”，使 Bit Machine — Simplicity 的抽象栈机解释器 — 能够在执行期间最小化数据复制。

### 值不是表达式

Simplicity 表达式表示操作，而不是值。记号 `scribe b : A ⊢ B` 表示一个总是返回值 `b` 的唯一表达式，它只是记号上的便利，而不是组合子。这与 Bitcoin Script 类似，其中像 `OP_1` 这样的操作会推入值，而不是直接表达值。

### Simplicity 的完备性定理

有了全部九个组合子之后，我们如何知道自己没有遗漏什么 — 这九个组合子确实足够？Simplicity 完备性定理回答了这个问题：对于（有限）Simplicity 类型之间的任何函数，都存在某个 Simplicity 表达式来表示它。证明是构造性的 — 它展示了如何构建该表达式：

1. **分解输入**：使用嵌套的 `case` 表达式，将任何类型的任何输入完全分解为其组成位
2. **构建查找表**：对每个可能的输入，使用 `scribe` 生成相应输出
3. **组装**：嵌套的 case 和 scribe 一起形成一个巨大的查找表，用来实现该函数

该定理在 Rocq 证明助手（以前称为 Coq）中经过形式化验证。证明是官方 Simplicity 代码库的一部分，并已通过机器检查确认正确。

虽然完备性定理保证 Simplicity 的九个组合子可以表达（有限）Simplicity 类型之间的任何函数，但由查找表构造产生的表达式会大到不切实际。一个作用于 256 位输入的函数需要包含 2²⁵⁶ 个条目的查找表。这就是为什么接下来的章节会聚焦于构建利用计算结构的高效表达式，而不是通过查找表暴力穷举一切。

### 结论

Simplicity 的核心语言包含一个类型系统和一组组合子，能够表达任何有限计算。虽然完备性定理保证了表达能力，但通用构造产生的表达式大到不切实际。实际的 Simplicity 开发需要利用计算结构来获得简洁表达式。接下来的章节将探索数据结构、交易交互以及额外的组合子。

# 从数据类型到程序

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## 构建数据类型

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

在前几章中，我们展示了 Simplicity 的核心组合子集合如何足以实现任何有限的纯计算。本章展示如何从这些原语构建实用的数据结构和计算 — 就像计算机由逻辑门构建而成一样。

### 布尔逻辑

布尔类型，记作 `𝟚`，等于 `𝟙 + 𝟙`，并有两个值：`σᴸ⟨⟩`（false）和 `σᴿ⟨⟩`（true）。使用核心组合子，可以构造布尔逻辑运算符。

#### And 操作

逻辑 `and : 𝟚 × 𝟚 ⊢ 𝟚` 操作接受两个位并返回一个位。实现方式是在第一个位上分支：如果为 false，则返回 false；否则返回第二个位。

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

使用 `⟨false, false⟩` 测试：

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

使用 `⟨true, true⟩` 测试：

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### 其他逻辑操作

`not` 操作需要一个辅助组合子：

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

初始的 `iden ▵ unit : A ⊢ A × 𝟙` 会向输入添加一个空“环境”，使 `case` 组合子能够应用。两个分支中使用 `take` 会丢弃这个空环境，以执行 `f` 或 `g`。

其他布尔逻辑操作：

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### 位加法器

“半加器”接受两个位并将它们相加，产生两位输出：一个进位位和一个和位。

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

“全加器”将三个位相加，产生两位输出。输入使用嵌套元组 `(𝟚 × 𝟚) × 𝟚`。

对于嵌套元组，使用紧凑记号：

- `O f` 表示 `take f`
- `I f` 表示 `drop f`
- `H` 表示 `iden`

例如，`I O H` 表示 `drop (take iden) : A × (B × C) ⊢ B`，用于提取中间值。这个记号让人联想到二进制数字：当把嵌套元组看作二叉树时，该记号表示树位置的反向二进制数字。这些表达式构成 Simplicity 的 De Bruijn 索引。

**注意：** `I`、`O` 和 `H` 记号只适用于完全由 `take`、`drop` 和 `iden` 组成的子表达式。

全加器组合两个半加器，并对进位位取逻辑 `or`：

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

在第一行中，`take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` 在前两个位上运行半加器，同时保存最后一个位。

在第二行中，`O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` 保存第一个位（第一个半加器的进位输出），并在最后两个位上运行半加器。

在最后一行中，`(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` 对前两个位（两个半加器的进位输出）取逻辑 OR，并返回第二个半加器的和输出位。

这展示了 Simplicity 编程：使用 `I`、`O` 和 `H` 记号引用数据位，形成适合通过顺序组合调用其他函数的“环境”。

用户不会直接定义低层操作。本系列后面会讨论实现常用函数的标准库 jets。终端用户并不需要直接用 Simplicity 编程，这类似于 Bitcoin Script。相反，像 SimplicityHL 这样的高级语言会生成 Simplicity 代码，管理子表达式“环境”，并将命名变量翻译成适当的 `take` 和 `drop` 序列。

### 向量

固定长度向量通过形成类型 `A` 的迭代积来定义：

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

这些也可写作 `A^2`、`A^4`、`A^8` 等。

向量只为长度为二的幂时定义。其他幂需要选择括号约定。

给定表达式 `f : A ⊢ B`，重复配对会把它“映射”到固定长度向量上：

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

给定函数 `f : A × B ⊢ B`，可在固定长度向量上进行迭代或“折叠”：

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

存在许多变体。给定 `f : A × B ⊢ C`，可以用 `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ` 在配对向量上执行“zip”。给定 `f : (A × B) × C ⊢ C`，可以用 `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C` 在配对向量上折叠。组合 `map` 和 `fold-right` 可以创建累加组合子：`f : A × C ⊢ C × B` 给出 `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`。还可以有更多变体。

#### 多位字

位向量产生多位整数。例如，`𝟚³²` 是 32 位字类型。`𝟚²⁵⁶` 是 256 位字类型，适合哈希和密码学操作。

使用全加器，一种向量操作的变体可以定义多位字上的“串行进位加法器”：

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` 接受两个 n 位二进制数和一个一位进位输入，返回一个一位进位输出标志和一个 n 位和。

#### SHA-256

通过递归定义多位字上的算术操作 — 减法、乘法、除法 — 以及逐位逻辑操作，如逻辑 AND、OR、XOR，并反复组合这些操作，甚至可以构建 SHA-256 的区块压缩函数：

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256 压缩在 Rocq 证明助手（以前称为 Coq）中使用 Simplicity 进行了形式化定义，并附带形式化证明，证明 `sha256-hash-block` 实现是正确的。

作为原始 Simplicity，压缩运行得太慢。Jets 会以原生方式执行 SHA-256 压缩等常用函数。纯 Simplicity 实现则作为 jets 的形式化规范。

### Option 类型

Option 类型由与单位类型取和得到：

```
Option A ≔ 𝟙 + A
```

类型 `Option A` 可写作 `A?` 或 `𝕊 A`（其中 `𝕊` 表示“后继”）。函数会映射到 option 类型上：

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

可以定义 bind 等单子组合子：

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### 可变长度缓冲区

“缓冲区”是部分填充向量的类型：

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

类型 `Xᑉ⁸` 展开为 `(1 + X⁴) × ((1 + X²) × (1 + X))`。把它当作多项式并展开，会得到 `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`。作为类型解释时，它表示长度最多为 7 的所有可能 X 元组之和，包括空元组。这正是长度严格小于 8 的列表类型。

与向量类似，可以在缓冲区上定义映射和折叠操作。栈操作包括 `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` 和 `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`。`push-<n` 会向缓冲区追加一个项，如果发生溢出则返回完整向量。`pop-<n` 会移除一个项，返回较小的缓冲区和被移除的项；如果原缓冲区为空，则可选地返回 nothing。

`push-<n` 的递归定义如下：

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

当复杂度超过某个水平时，原始 Simplicity 会变得难以理解。终端用户会使用像 SimplicityHL 这样的高级语言来生成这些惯用表达式。

### 结论

本章展示了如何从位构建逻辑操作。由此产生了位级算术，使我们能够推理执行。我们还发展了向量类型，展示了如何在多位字上迭代以定义算术。进一步地，像 SHA-256 和 Schnorr 签名验证这样的密码学操作也可以仅使用 Simplicity 组合子来定义 — 而且它们实际上都已经使用 Simplicity 定义。

本章并不是关于 Simplicity 中所有可构建数据类型和操作的全面指南，而是说明如何在 Simplicity 的约束内实现实用功能。尽管类型是有限有界的，有用的向量、缓冲区类型以及在这些结构上迭代的操作都可以被定义。

实际标准库操作规范与这里的定义略有不同。例如，全加器使用三路 XOR 和“多数”逻辑函数，而不是两个半加器。

在实践中，Simplicity 程序使用 jets 处理算术和密码学操作。然而，jets 只能替代表达式。遍历缓冲区和向量的组合子无法被 jets 替代，并且会出现在实际的 Simplicity 程序中。不过，终端用户并不是直接使用这些组合子，而是使用像 SimplicityHL 这样的高级语言生成此类表达式。

递归定义的组合子看起来会在表达式大小上指数增长。这并不成问题。序列化期间，表达式会被编码为 DAG（有向无环图），而不是树。实际表示只会线性增长。

到目前为止，我们只考虑了纯计算。与交易数据交互以执行签署交易等任务，需要某种方式让程序在签名无效时失败。下一章讨论 Simplicity 中的副作用。

## 两种副作用

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

在前几章中，我们展示了如何使用 Simplicity 的核心组合子集合构建一些数据结构和计算。如前所述，核心组合子足以实现任何有限纯计算。这引出了一个问题：还能实现什么？我们可以为表达式添加额外的副作用。

表达式可能存在各种类型的副作用：状态更新、写入日志、抛出异常、从环境读取、调用 continuation 等。Simplicity 中可用的副作用取决于应用。

对于 Bitcoin 和 Liquid 应用，我们目前有两种副作用：Failure 效应，它是一种异常效应，其中异常类型为 `𝟙`；以及 Reader 效应，它允许访问来自交易环境的数据。我们的核心组合子是“纯”的；它们没有副作用。然而，jets 可以引入具有副作用的新原语。

### 带有效应的 Jets

我们将在本课程后面更多讨论 jets，但这里先介绍几个示例 jets，以说明它们的副作用。

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` 是一个表达式的 jet，它接受一个 x-only 公钥、一个 256 位消息和一个 Schnorr 签名，并且不返回任何东西！按照其类型，它应当表现得和 `unit` 一样。差别在于该 jet 的副作用：如果签名验证失败，整个计算会通过抛出一个（单位类型的）异常而中止。这就是 Failure 效应。

#### Verify

`verify : 𝟚 ⊢ 𝟙` 是一个用于表达 Failure 效应的极简 jet。如果 `verify` 的输入为 `false`，整个计算会通过抛出异常而中止。如果输入为 `true`，则不返回任何东西，但计算可以继续。

#### 交易哈希

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` 看起来像一个常量函数，因为只有一个可能的输入值：空元组。然而，这个 jet 会从交易环境中读取，并产生一个交易数据哈希，类似于 Bitcoin Script 签名验证中使用的 `SIGHASH_ALL` 消息摘要。这是 Reader 效应的一个例子：返回值取决于该 jet 执行时所在的交易环境。还有几个其他哈希 jets 会对交易环境数据的不同子集进行哈希，以帮助为签名构建自定义消息摘要。

#### 内省 Jets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` 是一个函数，它接受一个输入索引，并返回该输入的交易序列号；如果索引越界，则可选地返回 nothing。同样，输出值并不是输入索引的纯函数；相反，该操作使用 Reader 效应访问交易环境，以确定输出值。还有几个其他内省 jets 会返回交易环境数据的不同片段。

### 对效应进行分类

并非所有副作用都是一样的。有些副作用比其他副作用表现得更好。我们可以根据它们对程序变换的适应程度来分类效应。

#### 可交换效应

可交换效应指的是：如果你交换两个表达式的输出，就可以安全地交换表达式本身，而不会改变表达式的效应。考虑 `swap = I H ▵ O H : A × B ⊢ B × A`。如果对于每个具有副作用的表达式 `f` 和 `g`，都有 `f ▵ g ⨾ swap = g ▵ f`，那么这些效应就是可交换的。

从环境读取交易数据是一种可交换效应，因为无论我们以什么顺序执行读取，从环境读取的结果都是相同的。

一般来说，抛出异常不是一种可交换效应。如果 `f` 抛出某个异常 `e₁`，而 `g` 抛出另一个异常 `e₂`，那么从 `f` 和 `g` 组成的对中抛出哪个异常取决于它们的执行顺序。

然而，在 Failure 效应的特殊情况下，只能抛出单位类型的异常，因此该效应是可交换的。无论 `f` 还是 `g` 抛出异常，最终异常都会相同，因为只有一个可能的异常值。

#### 幂等效应

幂等效应指的是：如果你复制一个表达式的输出，就可以安全地复制表达式本身，而不会改变表达式的效应。考虑 `dup = iden ▵ iden : A ⊢ A × A`。如果对于每个具有副作用的 `f`，都有 `f ⨾ dup = dup ⨾ f ▵ f`，那么这些效应就是幂等的。

从环境读取交易数据是一种幂等效应。抛出异常也是一种幂等效应。尽管两个被复制的表达式中只有一个会被执行，`dup ⨾ f ▵ f` 抛出的任何异常也会与 `f ⨾ dup` 抛出的异常相同。

不过，写入日志可能不是幂等的，因为复制该效应会导致日志消息出现两次。然而，如果日志由消息的_集合_而不是消息的_列表_组成，那么该效应就是幂等的（并且是可交换的），因为集合插入本身就是幂等操作。

#### 单位效应

单位效应指的是：如果你丢弃一个表达式的输出，就可以安全地丢弃表达式本身，而不会改变表达式的效应。如果对于每个具有副作用的 `f`，总是有 `f ⨾ unit = unit`，那么你的效应就是单位的。

从环境读取数据是少数几类单位效应之一。如果从环境读取交易数据的结果被丢弃，那么执行该读取的整个表达式也可以被丢弃。

Failure 效应不是单位的。如果 `f` 抛出异常，那么 `f ⨾ unit` 也会抛出；执行甚至还没到达 `unit` 组合子，计算就已经中止。另一方面，`unit` 显然不会抛出任何异常，因此 `f ⨾ unit` 和 `unit` 的效应是不同的。

总结一下，上面讨论的效应在这三种性质上的表现如下：

| 效应 | 可交换 | 幂等 | 单位 |
| --- | :---: | :---: | :---: |
| Reader（交易环境） | ✓ | ✓ | ✓ |
| Failure（单位类型异常） | ✓ | ✓ | ✗ |
| Writer（作为集合的日志） | ✓ | ✓ | ✗ |
| 一般异常（任意类型） | ✗ | ✓ | ✗ |

### Simplicity 中允许的效应

一种效应拥有的良好性质越多，Simplicity 优化器在变换使用这些效应的程序时就拥有越大的空间。理想情况下，我们只允许同时具有三种性质的效应：可交换、幂等和单位。这将允许优化器执行它想要的任何程序变换。然而，从环境读取是唯一满足全部三种性质的效应。

相反，我们要求 Simplicity 效应必须是可交换且幂等的。我们在 Simplicity 中使用的两种效应，即 Failure 效应和 Reader 效应，都是可交换且幂等的。这允许对 Simplicity 代码执行一大类优化。

然而，上述“丢弃”变换，即试图用 `unit` 替换 `f ⨾ unit`，或任何类似变换，如果 `f` 可能产生 Failure 效应，就不被允许。事实上，想象一下，如果 `f` 包含一个 `bip0340-verify` 断言，试图把那个检查优化掉将是灾难性的。

### 为什么要允许副作用？

为什么 Simplicity 甚至要允许副作用？如果每个程序都把整个交易作为输入，并返回一个决定交易是否有效的布尔输出，不是更好吗？

#### 批量验证

我们拥有 Failure 效应的一个原因，是为了支持 Schnorr 签名的[批量验证](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification)。在批量验证中，许多单独的 Schnorr 签名检查会以某种方式汇聚在一起，使得只要任一签名检查失败，整个批次就失败。

这种批处理过程相较于逐个验证每个签名提高了效率。缺点是，如果批量验证失败，我们无法知道具体哪个或哪些签名检查失败。

通过使用失败副作用，`bip0340-verify` 确保如果签名检查失败，整笔交易就失败。如果 `bip0340-verify` 反而返回 `𝟚`（布尔类型）来表示成功或失败，那么失败的签名检查仍然可能导向脚本成功的分支。在这种情况下，我们需要知道特定签名是否有效，因此就无法利用批量验证。

#### 预计算交易数据

早期 Bitcoin Script 的一个问题是，用于为签名创建消息摘要的哈希函数在交易大小上是线性的。通常每个输入至少会创建一个用于签名验证的消息摘要，因此总体哈希量在交易大小上是二次的。

这个问题在 SegWit 以及 Bitcoin Script 的后续迭代中得到修复，方式是重新定义消息摘要，使其可以在每次签名检查中以常数时间计算。这依赖于 `PrecomputedTransactionData`，它会预先计算一次交易数据的哈希，然后由每个输入的 sighash 计算共享。Simplicity 的交易哈希 jets 依赖同样类型的预计算交易数据，以确保 jets 以常数时间运行。

假设 `sig-all-hash` 没有使用 Reader 效应。假设我们以某种方式设法为交易环境构建了一个 Simplicity 类型。我们称它为 `TxEnv`，于是 `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` 就是该 jet 的类型。这样的定义要求 `sig-all-hash` jet 能够计算任何交易的哈希，而不仅仅是它所参与的那笔交易。Simplicity 程序可以复制给定的 `TxEnv`，并把它的修改副本传给 `sig-all-hash`。在这种情况下，`sig-all-hash` 无法依赖 `PrecomputedTransactionData`，我们就会重新回到需要对传入这个版本 `sig-all-hash` 的任何交易数据执行线性时间计算。

因为 `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` 使用 Reader 效应访问交易数据，它_只_能访问固定的交易环境。因此，该 jet 的实现可以安全地使用 `PrecomputedTransactionData` 并以常数时间运行。

### 跨输入签名聚合

虽然 Liquid 和 Bitcoin 目前都不支持[跨输入签名聚合](https://hrf.org/latest/cisa-research-paper/)，但我们希望检查 Simplicity 能否在时机到来时与其兼容。

尽管细节尚未确定，我们设想用 Writer 效应实现半聚合。也就是说，一个类型例如为 `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` 的新 jet 会接受一个公钥、消息摘要和 Schnorr 签名的 `r` 组件（Schnorr 签名由一个 `r` 组件和一个 `s` 组件组成），并在继续执行前将其写入交易日志。然后，在交易的其他位置或随交易一起，为所有半聚合的 Schnorr 签名提供一个聚合 `s` 组件。只有当为所有记录的密钥、消息和 `r` 组件提供了这样的聚合 `s` 组件时，交易才有效。

为满足 Simplicity 的要求，这个 Writer 效应需要是幂等且可交换的。可以通过将 writer 日志视为由密钥、消息、`r` 组件元组组成的集合来保证这一点。这可行是因为集合操作是幂等且可交换的。将日志视为值的集合将与半聚合验证算法兼容。

### 结论

在本章中，我们考察了向 Simplicity 可以执行的计算添加副作用。我们按照各种效应相对于各种程序变换表现得有多好，对它们进行了分类。我们决定将 Simplicity 的效应限制为可交换且幂等的效应。

我们用于 Bitcoin 和 Liquid 应用的两个效应是 Reader 效应（用于访问交易环境）和 Failure 效应（用于中止并使程序失败）。一些 jets 会使用可能发生这些副作用的原始操作。

Failure 效应决定 Simplicity 程序的输出：程序要么失败，使交易无效；要么成功。Reader 效应为 Simplicity 程序提供一种输入：包含交易数据的环境。但我们还需要向 Simplicity 程序提供其他输入，例如数字签名。

在下一章中，我们将看看什么是 Simplicity 程序，它们如何被转换成地址，以及我们如何向 Simplicity 程序添加其他输入，例如签名。

## 程序与地址

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

在上一章中，我们描述了 Simplicity 使用的两种副作用：Failure 效应，它决定程序成功或失败；以及 Reader 效应，它提供对交易环境的访问。现在我们转向一个实践问题：Simplicity 程序究竟是什么，它又如何成为区块链上的地址？

### Simplicity 程序

Simplicity 程序被定义为类型为 `𝟙 ⊢ 𝟙` 的 Simplicity 表达式。这个类型签名意味着程序不接受有意义的输入（只有单位值），也不产生有意义的输出（只有单位值）。Reader 效应捕获交易环境输入，而 Failure 效应表示成功或失败。这些效应处理的是 I/O，而不是 Simplicity 类型本身。

### 承诺 Merkle 根

Bitcoin 不是在链上存储完整程序，而是采用承诺 — 这一做法从 Pay-to-Script-Hash（P2SH）延伸而来。Simplicity 使用承诺 Merkle 根（CMR）。

每个组合子都会收到一个 SHA-256 标签，该标签从如下模式派生：`Simplicity␟Commitment␟[identifier]`，其中 `␟` 表示 ASCII 码 31（单位分隔符）。

每个标签都是下列对应原像字符串的 SHA-256 哈希：

| 组合子 | 标签原像（ASCII 字符串） |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

然后，通过为每个组合子连同其参数的 CMR 计算一个带标签的 SHA-256 中间状态，Simplicity 表达式会被递归哈希成一个 256 位 CMR（用 `#ᶜ(e)` 表示表达式 `e` 的 CMR，用 `∥` 表示字节拼接）：

| 组合子 | CMR 规则 |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

二元组合子（`comp`、`pair`、`case`）会拼接两个子节点的 CMR；一元组合子（`take`、`drop`、`injl`、`injr`）会在 32 字节 `0x00` 填充之后拼接其单个子节点的 CMR；而零元叶子（`iden`、`unit`）只对其标签进行哈希。有两个约定使计算保持低成本：使用 SHA-256 中间状态，因此**每个表达式至多需要调用一次 SHA-256 压缩函数**（假设直到常量标签为止的中间状态已预计算），并且单参数构造子在其参数前加上 32 字节 `0x00` 填充，这让希望如此的实现可以做一点额外预计算。

对于 `unit` 组合子 — 一个没有参数子表达式的零元构造子 — 该规则特化为 `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`，其中 `tag_unit = SHA-256(Simplicity␟Commitment␟unit)`（标签被输入两次）。平凡 `unit` 程序得到的 CMR 是：

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

关键是，CMR 不承诺 Simplicity 表达式的类型，而是在赎回期间依赖类型推断。

### 地址

地址使用 BIP-0341 的 Taproot 机制，并把 CMR 承诺在 TapLeaf 版本 `0xbe` 下。该过程包括：

1. 计算一个 TapLeaf 标签哈希，将版本字节、CMR 长度和 CMR 本身组合起来
2. 对一个内部公钥进行 tweak（当不希望有密钥花费路径时，使用一个 NUMS 点）
3. 转换为 bech32m 格式
4. 添加适当的校验和

当不希望有密钥花费路径时，内部公钥被设置为一个 **NUMS**（\"Nothing-Up-My-Sleeve\"）点：这是一个特意选择的曲线点，使得没有人知道它的离散对数 — 换言之，它没有对应的私钥。因为没有人能为它生成签名，密钥花费路径就可证明不可用，输出也就*只能*通过被承诺的 Simplicity 脚本路径花费。在真实应用中，应按照 BIP-0341 建议对这个 NUMS 点进行随机化，使没有密钥花费路径的输出与普通 Taproot 输出不可区分（这是隐私收益）。

#### 从 Simplicity 到地址

让我们走完整个推导过程，使用可能最简单的程序：`unit : 𝟙 ⊢ 𝟙`，一个始终成功的无操作程序。

**1. 组合子标签。** 首先计算 `unit` 标签：

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR。** 将标签输入两次，得到程序的 CMR：

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf 哈希。** 将 Simplicity 的 TapLeaf 版本 `0xbe` 和 CMR 长度 `0x20`（32 字节）前缀到 CMR 前，然后取 Elements TapLeaf 标签哈希（标签哈希为 `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`）：

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

因为只有这一个叶子，没有 TapBranches，所以这个哈希已经就是 TapTree 根。

**4. TapTweak。** 由于我们不想要密钥花费路径，我们使用 BIP-0341 NUMS 点作为内部密钥，并用 TapTree 根对其进行 tweak：

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. 输出密钥。** 在曲线上调整内部密钥，`output_pk = lift_x(internal_pk) ⊕ t·G`（这里概括了椭圆曲线运算），得到 x-only 输出密钥 `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`。

**6. Bech32m 地址。** 编码 x-only 输出密钥，前缀一个 `p`（SegWit v1 见证版本字符），添加 Liquid-testnet 人类可读前缀 `tex1`，并附加 Bech32m 校验和。最终地址是：

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

这确实做了很多工作 — 但其中很大一部分是 Taproot 本身要求的，而不是 Simplicity 要求的。

### 见证表达式

一种新的组合子类型解决了 Simplicity 程序没有输入的问题：见证表达式。`witness` 组合子允许把签名数据和其他见证材料集成到程序中。

```
      w : B
-----------------
witness w : A ⊢ B
```

见证表达式的语义很直接：它忽略输入，并简单返回值 `w`（它可以是任何 Simplicity 类型），即 `⟦witness w⟧(a) = w`。这**没有增加新的表达能力** — 根据完备性定理，Simplicity 已经可以构建任何这样的常量函数（回想前几章中的 `scribe` 宏）。`witness` 组合子的意义完全在于它的 **CMR**：值 `w` 被**排除**在表达式的 CMR 之外，因此地址可以在 `w` 已知之前计算，而 `w` 在赎回时提供。

这一设计选择支持剪枝 — 未执行的条件分支无需在链上揭示，包括其中关联的见证表达式。当一个分支被剪枝时，验证者只需要被剪枝子树的 CMR，而不需要它的实际内容。

### 见证值

见证表达式只能持有一个*值*，而不能持有更一般的 Simplicity 表达式，这可能看起来像是一种限制。但基于 UTXO 的区块链上的程序只会执行一次。没有必要把整个子表达式传入 witness 节点：用户可以直接在链下自行运行该子表达式，并将其输出转录为见证值，从而获得完全相同的结果。

（在本课程后面，我们会遇到 `disconnect` 组合子，它的行为很像一个*确实*以完整 Simplicity 表达式作为参数的见证表达式。）

另一种设计是把所有见证数据作为参数输入到顶层 Simplicity 程序。见证表达式因两个原因更受偏好。第一，**剪枝**：`case` 表达式中未执行的分支永远不会在链上揭示，而这些分支内部的任何见证表达式也会随之一同被剪枝。第二，**局部性**：见证表达式让我们可以把每个见证值精确放置在它被使用的位置，而不是从程序的顶层输入一路传递下去。

### 类型推断

由于 CMR 不承诺类型，类型系统会在赎回期间被重建。Simplicity 的类型推断算法会根据组合子结构确定每个子表达式的最小类型。更准确地说，推断会计算每个子表达式的*主*（最一般）类型；随后，任何仍然自由的类型变量都会被实例化为单位类型 `𝟙`，从而为程序产生一个唯一的最小类型。

### 结论

在本章中，我们确定了 Simplicity 程序是类型为 `𝟙 ⊢ 𝟙` 的表达式，解释了如何从每个组合子的带标签 SHA-256 哈希构造承诺 Merkle 根，并展示了如何通过 BIP-0341 Taproot 将 CMR 转换为链上地址。我们介绍了见证表达式，它是一种在花费时提供签名数据和其他输入、同时不在地址创建时承诺其值的机制。

# 最后一节

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## 评价与评分

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## 期末考试

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## 结论

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
