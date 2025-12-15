---
name: 编程 Bitcoin
goal: 从零开始构建完整的 Bitcoin 库，了解 Bitcoin 的加密基础
objectives: 

 - 用 Python 实现有限域运算和椭圆曲线操作
 - 以编程方式构建和解析 Bitcoin 事务
 - 创建 Testnet 地址并在网络上广播交易
 - 掌握 Bitcoin 安全模型的数学基础

---
# Bitcoin 脚本和程序之旅


本强化课程为期两天，由 Jimmy Song 讲授，通过从头开始构建一个完整的 Bitcoin 库，让您深入了解 Bitcoin 的技术基础。从有限域和椭圆曲线的基本数学开始，您将逐步学习事务解析、脚本执行和网络通信。通过在 Jupyter 笔记本中进行实际编码练习，您将创建自己的 Testnet Address、手动构建事务并将其直接广播到网络，同时深刻理解使 Bitcoin 和 Trustless 安全的加密原理。


享受您的发现！


+++

# 介绍

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## 课程概览

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

欢迎来到课程 PRO 202 _**Programming Bitcoin**_，这是一段深入的旅程，将带你从有限域算术一路学习到在比特币测试网中构建并广播真实交易。

在本课程中，您将逐步使用 Python 构建一个比特币库，同时掌握理解比特币安全性和内部运作所需的加密学、协议和软件基础。PRO 202 的方法完全以实践为主：每个概念都会立即在 Jupyter 笔记本中实现，确保理论与代码相互促进。

### 比特币的基本数学概念

本节首先建立不可或缺的数学基础。您将实现有限域算术和椭圆曲线运算（群运算定律、加法、倍点、标量乘法……）——这是 ECDSA 的前提。目标有二：理解使加密签名成为可能的代数结构，并构建可靠的 Python 工具来操作它们。

接下来，您将正式化 ECDSA 的各个组成部分：密钥生成、点格式化、哈希、签名创建和验证。本节将理论与实践直接联系起来，强调实现细节以及底层安全模型的稳健性。

### 比特币交易的内部运作机制

在第二部分中，您将剖析比特币交易的结构：UTXO、输入/输出、序列、脚本、编码等。您将编写代码来构建、签名和验证交易，从而精确理解哈希所承诺的内容及其原因。

接下来，您将实现一个最小化的 _Script_ 执行器，审查关键操作码，并验证支出路径。目标是让您能够审计交易行为、诊断验证失败，并分析支出策略的安全性。

### 比特币网络的内部运作机制

在第三部分中，您将把交易放入更广泛的系统中：区块结构、区块头、难度以及工作量证明（Proof-of-Work）机制。您将处理协议消息、区块头和默克尔树。

最后，您将研究点对点节点通信、消息优化以及SegWit的引入。

与 Plan ₿ Academy 的每门课程一样，最后一部分包含一个旨在巩固您理解的评估。准备好揭示比特币的内部运作机制，并编写驱动它的代码了吗？让我们开始吧！

# Bitcoin 的基本数学概念

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## 实施 Bitcoin 的数学

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## 椭圆曲线密码学

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin 交易内部结构

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin 事务解析和 ECDSA 签名

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin 脚本和事务验证

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## 交易构建和按脚本付费 Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin 网络内部结构

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin 块和 Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## 网络通信与梅克尔树

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## 高级节点通信和隔离见证

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# 最后部分


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## 评论与评级


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## 结论


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
