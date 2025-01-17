---
name: 标记UTXO
description: 如何正确标记您的UTXO？
---
![cover](assets/cover.webp)

在本教程中，您将发现有关在比特币钱包中标记UTXO以及关于币控制的所有必要信息。我们从理论部分开始，以完全理解这些概念，然后进入实践部分，探索如何在主要的比特币钱包软件中具体使用标签。

## 什么是UTXO标记？
“标记”是一种技术，涉及将注释或标签与比特币钱包内的特定UTXO关联起来。这些注释由钱包软件本地存储，永远不会通过比特币网络传输。因此，标记是一种个人管理工具。

例如，如果我通过Bisq与Charles进行P2P交易收到一个UTXO，我可以给它分配标签`Bisq P2P Purchase Charles`。

标记允许人们记住UTXO的来源或预期目的地，这简化了资金管理并优化了用户的隐私。当与“币控制”功能结合使用时，标记变得更加相关。币控制是优秀比特币钱包中可用的一个选项，它使用户能够手动选择在创建交易时将作为输入使用的特定UTXO。

使用具有币控制功能的钱包，结合UTXO标记，允许用户精确区分和选择交易的UTXO，从而避免合并来自不同来源的UTXO。这种做法减少了与共同输入所有权启发式（CIOH）相关的风险，该启发式建议交易的输入具有共同所有权，这可能会损害用户的隐私。

让我们回到我的非KYC UTXO的例子，我想避免将其与来自知道我的身份的受监管交易平台的UTXO合并。通过在我的非KYC UTXO和我的KYC UTXO上放置不同的标签，我将能够轻松识别哪个UTXO作为输入来满足支出，使用币控制功能。

## 如何正确标记您的UTXO？
没有适合所有人的UTXO标记的通用方法。由您来定义一个标记系统，以便您可以轻松找到您的钱包。
标记的一个关键标准是UTXO的来源。您应该简单地指明这枚硬币是如何到达您的钱包的。它是来自交易平台吗？客户的账单结算？点对点交换？还是代表购买的找零？因此，您可以指定：
- `Withdrawal Exchange.com`；
- `Payment Client David`；
- `P2P Purchase Charles`；
- `Change from sofa purchase`。
![labelling](assets/en/1.webp)
为了精细化您的UTXO管理并遵循您在钱包内的资金隔离策略，您可以用一个额外的指标丰富您的标签，以反映这些分隔。如果您的钱包包含两类您不想混合的UTXO，您可以在标签中整合一个标记以清晰区分这些组。

这些分隔标记将取决于您自己的标准，例如区分KYC UTXO（知道您的身份）和非KYC（匿名）的，或者区分专业和个人资金。采用前面提到的标签示例，这可以被翻译为：
- `KYC - Withdrawal Exchange.com`；
- `KYC - Payment Client David`；
- `NO KYC - P2P Purchase Charles`；
- `NO KYC - Change from sofa purchase`。
![标注](assets/en/2.webp)无论如何，请记住，好的标注是在您需要时能够理解的标注。如果您的比特币钱包主要用于储蓄，那么这些标签可能几十年后才对您有用。因此，请确保它们清晰、精确且全面。

还建议在交易过程中持续对一个币进行标注。例如，在进行无KYC的UTXO合并时，确保将结果UTXO标记不仅仅为`合并`，而是具体为`无KYC合并`，以保持币源的清晰追踪。

最后，给标签上日期并非强制性的。大多数钱包软件已经显示了交易日期，并且总是可以使用其TXID在区块浏览器上检索到这些信息。

## 教程：在Specter桌面版上进行标注

连接并打开您在Specter桌面版上的钱包，然后选择`地址`标签页。

![标注](assets/notext/3.webp)
在这里，您将看到所有地址的列表，以及锁定在它们上的任何比特币。默认情况下，地址在`标签`列下通过它们的索引来识别。要更改标签，只需点击它，输入所需的标签，然后点击蓝色图标确认。
![标注](assets/notext/4.webp)

您的标签随后将出现在您的地址列表中。

![标注](assets/notext/5.webp)

您也可以提前分配标签，当您与发送者分享您的接收地址时。要做到这一点，通过访问`接收`标签页，在专用字段中记下您的标签。

![标注](assets/notext/6.webp)

## 教程：在Electrum上进行标注

在Electrum钱包中，登录您的钱包后，点击您想要分配标签的交易，在`历史`标签页中。

![标注](assets/notext/7.webp)

一个新窗口打开。点击`描述`框并输入您的标签。

![标注](assets/notext/8.webp)

一旦输入了标签，您可以关闭此窗口。

![标注](assets/notext/9.webp)

您的标签已成功保存。您可以在`描述`标签页下找到它。

![标注](assets/notext/10.webp)

在`币`标签页中，您可以执行币控制，您的标签位于`标签`列中。

![标注](assets/notext/11.webp)

## 教程：在Green Wallet上进行标注

在Green Wallet应用中，访问您的钱包并选择您想要标注的交易。然后，点击小铅笔图标来记下您的标签。

![标注](assets/notext/12.webp)

输入您的标签，然后点击绿色的`保存`按钮。

![标注](assets/notext/13.webp)

您将能够在交易的详情和您钱包的仪表板上找到您的标签。

![标注](assets/notext/14.webp)

## 教程：在Samourai Wallet上进行标注

在Samourai Wallet中，有几种不同的方法允许您为交易分配标签。对于第一种方法，首先打开您的钱包并选择您想要添加标签的交易。然后按`添加`按钮，位于`备注`框旁边。

![标注](assets/notext/15.webp)
在您的标签中输入并通过点击蓝色的`Add`按钮确认。
![labelling](assets/notext/16.webp)

您将在交易的详情中找到您的标签，同时也能在您钱包的仪表盘上看到。

![labelling](assets/notext/17.webp)
对于第二种方法，点击屏幕右上角的三个小点，然后点击`Show Unspent Transaction Outputs`菜单。
![labelling](assets/notext/18.webp)

在这里，您将找到钱包中所有UTXOs的综合列表。显示的列表属于我的存款账户，然而，通过从专用菜单导航，可以为Whirlpool账户复制此操作。

然后点击您希望标记的UTXO，接着点击`Add`按钮。

![labelling](assets/notext/19.webp)

在您的标签中输入并通过点击蓝色的`Add`按钮确认。然后，您将在交易的详情和您钱包的仪表盘上找到您的标签。

![labelling](assets/notext/20.webp)

## 教程：在Sparrow Wallet上进行标记

使用Sparrow Wallet软件，可以通过多种方式分配标签。最简单的方法是在向发送者通报接收地址时预先添加标签。要做到这一点，在`Receive`菜单中，点击`Label`字段并输入您选择的标签。只要在该地址上收到比特币，这将被保留并在软件中随时可访问。

![labelling](assets/notext/21.webp)

如果您在收到地址时忘记了标记，仍然可以稍后通过`Transactions`菜单添加一个。只需在`Label`列中点击您的交易，然后输入所需的标签。

![labelling](assets/notext/22.webp)

您还有从`Addresses`菜单添加或修改标签的选项。

![labelling](assets/notext/23.webp)

最后，您可以在`UTXOs`菜单中查看您的标签。Sparrow Wallet自动在您的标签后面加上括号，里面注明了输出的性质，这有助于区分是由于找零产生的UTXOs还是直接收到的。

![labelling](assets/notext/24.webp)