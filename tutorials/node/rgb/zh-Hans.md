---
name: RGB
description: RGB简介及资产创建
---

![RGB vs Ethereum](assets/0.webp)

## 引言

2009年1月3日，中本聪启动了第一个比特币节点，从那一刻起，新的节点加入，比特币开始表现得仿佛它是一种新的生命形式，一种从未停止进化的生命形式，它逐渐成为了世界上最安全的网络，这得益于其独特的设计，这个设计由中本聪非常周到地构思，因为通过经济激励，它吸引了通常被称为矿工的用户投资于能源和计算能力，这有助于网络安全。

随着比特币继续增长和采用，它面临着可扩展性问题，比特币网络允许每10分钟挖出一个包含交易的新区块，假设我们每天有144个区块，每个区块最多2700笔交易，比特币的处理速度仅为每秒4.5笔交易，中本聪意识到了这一限制，我们可以在2011年3月发送给Mike Hearn的一封电子邮件1中看到，他解释了我们今天所知道的支付通道是如何工作的。通过支付通道，可以快速安全地进行小额支付，而无需等待确认。这就是链下协议的用武之地。

根据Christian Decker2的说法，链下协议通常是用户使用区块链的数据并在最后一刻之前不触及区块链本身的系统。基于这一概念，闪电网络诞生了，这是一个使用链下协议的网络，允许几乎瞬时完成比特币支付，由于并非所有这些操作都写在区块链上，它允许每秒处理成千上万笔交易并扩展比特币。

在比特币上的链下协议领域的研究和开发打开了潘多拉盒子，今天我们知道，我们可以实现的不仅仅是以去中心化方式进行价值转移，非营利组织LNP/BP标准协会专注于比特币和闪电网络上的第2层和第3层协议的开发，其中RGB项目脱颖而出。

## 什么是RGB？

RGB源于Peter Todd3在2016-2019年对一次性密封和客户端验证的研究，由Giacomo Zucco和社区将其发展成为比特币和闪电网络上更好的资产协议。这些想法的进一步发展导致RGB成为一个完整的智能合约系统，自2019年以来，在Maxim Orlovsky的领导下，社区参与其实施。

我们可以将RGB定义为一套开源协议，它允许我们以可扩展和保密的方式执行复杂的智能合约。它不是一个特定的网络（如比特币或闪电网络）；每个智能合约只是一组合约参与者，他们可以使用不同的通信渠道（默认为闪电网络）进行交互。RGB使用比特币区块链作为状态承诺的层，并在链下维护智能合约的代码和数据，这使其可扩展，利用比特币交易（和脚本）作为智能合约的所有权控制系统；而智能合约的演化由链下方案定义，最终重要的是，一切都在客户端进行验证。

简单来说，RGB是一个系统，允许用户在任何时候审计、执行和验证智能合约，而无需额外成本，因为它不使用“传统”系统所做的区块链，复杂的智能合约系统最早由以太坊开创，但由于它要求用户为每个操作支付大量的gas，它们从未实现它们所承诺的可扩展性，因此它从未成为将当前金融系统之外的用户纳入银行体系的选项。
当前，区块链行业提倡智能合约的代码和数据都必须存储在区块链中，并由网络的每个节点执行，不管这是否会导致大小的过度增加或计算资源的误用。RGB提出的方案更加智能和高效，因为它打破了区块链范式，将智能合约和数据与区块链分离，从而避免了在其他平台中看到的网络饱和，同时它不强制每个节点执行每个合约，而是由涉及的各方执行，这为保密性增添了前所未有的层次。
![RGB vs Ethereum](assets/1.webp)

## RGB中的智能合约

在RGB智能合约中，开发者定义了一个方案，指定合约随时间演变的规则。该方案是RGB智能合约构建的标准，无论是发行方在定义发行合约时，还是钱包或交易所都必须遵循特定的方案来验证合约。只有当验证正确时，各方才能接受请求并与资产进行交互。

RGB中的智能合约是状态变化的有向无环图（DAG），其中只有图的一部分是已知的，而且无法访问其余部分。RGB方案是这个图演变的一组核心规则，智能合约就是从这些规则开始的。每个合约参与者都可以添加这些规则（如果方案允许），由这些规则的迭代应用构建的图形。

## 可替代资产

RGB中的可替代资产遵循LNPBP RGB-20规范，当定义了RGB-20时，称为“初始数据”的资产数据通过闪电网络分发，其中包含使用资产所需的信息。最基本的资产形式不允许二次发行、代币销毁、重新命名或替换。

有时，发行者将来需要发行更多代币，例如USDT这样的稳定币，其每个代币的价值与像美元这样的通货膨胀货币的价值挂钩。为了实现这一点，存在更复杂的RGB-20方案，除了初始数据外，它们还要求发行者产生托运单，这些托运单也将在闪电网络中流通；有了这些信息，我们可以知道资产的总流通供应量。对于销毁资产或更改其名称也是如此。

与资产相关的信息可以是公开的或私密的：如果发行者需要保密，他/她可以选择不分享有关代币的信息，并在绝对隐私中进行操作，但我们也有相反的情况，即发行者和持有者需要整个过程是透明的。这是通过分享代币数据来实现的。

## RGB-20程序

销毁程序会使代币失效，销毁的代币不能再被使用。

替换程序发生在代币被销毁并且相同代币的新数量被创建时。这有助于减少资产历史数据的大小，这对于维持资产速度是重要的。

为了支持在不需要替换的情况下销毁资产的用例，使用了只允许销毁资产的RGB-20子方案。

## 非可替代资产
在RGB中的非同质化资产遵循LNPBP RGB-21规范5，当我们处理NFT时，我们也有一个主方案和一个子方案。这些方案有一个雕刻程序，允许我们附加代币所有者的自定义数据，我们今天在NFT中看到的最常见的例子是与代币链接的数字艺术。代币发行者可以使用RGB-21子方案禁止这种数据雕刻。与其他NFT区块链系统不同，RGB允许以完全去中心化和抗审查的方式分发大型媒体代币数据，利用称为Bifrost的闪电网络P2P扩展，该扩展也用于构建许多其他形式的RGB特定智能合约功能。
除了可替代资产和NFT外，RGB和Bifrost还可以用来生产其他形式的智能合约，包括DEXes、流动性池、算法稳定币等，我们将在未来的文章中介绍。

## RGB的NFT与其他平台的NFT对比

- 无需昂贵的区块链存储
- 不需要IPFS，而是使用一个闪电网络扩展（称为Bifrost）（并且它是完全端到端加密的）
- 不需要特殊的数据管理解决方案 - 再次强调，Bifrost扮演了这个角色
- 无需信任网站来维护NFT代币或关于发行资产/合约ABIs的数据
- 内置DRM加密和所有权管理
- 使用闪电网络（Bifrost）进行备份的基础设施
- 内容变现的方式（不仅仅是出售NFT本身，还包括多次访问内容的权限）

## 结论

自比特币推出近13年来，该领域进行了大量研究和实验，无论是成功还是错误，都让我们更多地了解去中心化系统在实践中的表现，什么使它们真正去中心化，以及哪些行动倾向于使它们中心化，所有这些都让我们得出结论，真正的去中心化是一个罕见且难以实现的现象，真正的去中心化只有比特币实现了，这就是我们专注于在其基础上构建的原因。

RGB在比特币的深渊中有其自己的深渊，当我深入其中时，我将发布我所学到的，在下一篇文章中，我们将介绍LNP和RGB节点以及如何使用它们。

- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md

# RGB节点教程

## 介绍

在本教程中，我们将解释如何使用RGB节点创建一个可替代代币以及如何转移它，本文档基于RGB节点演示，并且不同之处在于本教程使用真实的测试网数据，为此，我们必须构建我们自己的部分签名比特币交易，即psbt。

## 要求

推荐使用Linux发行版，本教程使用的是基于Ubuntu的Pop!OS，您将需要：

- cargo
- Bitcoin core
- git
注意：本教程展示了在Linux终端执行命令的过程，为了区分用户输入的内容和终端中的响应，我们使用$符号表示bash提示符。
您需要安装一些依赖项：

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

构建与运行

RGB-node是正在进行的工作（WIP），这就是为什么我们必须定位到一个特定的提交（3f3c520c19d84c66d430e76f0fc68c5a66d79c84）以便能够正确编译和使用它，为此我们执行以下命令。

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

现在我们开始编译它，不要忘记使用--locked标志，因为clap的一个版本引入了一个重大变更。

```
$ cargo install --path . --all-features --locked

....
....
    完成 [优化] 目标的构建 in 2m 14s
  正在安装至 /home/user/.cargo/bin/fungibled
  正在安装至 /home/user/.cargo/bin/rgb-cli
  正在安装至 /home/user/.cargo/bin/rgbd
  正在安装至 /home/user/.cargo/bin/stashd
   已安装包 `rgb_node v0.4.2 (/home/user/dev/rgb-node)`（可执行文件 `fungibled`、`rgb-cli`、`rgbd`、`stashd`）

```

正如rust编译器告诉我们的，二进制文件被复制到了$HOME/.cargo/bin目录，如果您的编译器将它们复制到了不同的位置，您必须确保该目录被包含在$PATH中。

在已安装的二进制文件中，我们可以看到三个守护进程或服务（以d结尾的文件）和一个cli（命令行界面），cli允许我们与主rgbd守护进程进行交互。在本教程中，我们将运行两个节点，我们还将需要两个客户端，每个客户端必须连接到其自己的节点，为此我们创建两个别名。

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

我们可以直接运行这些别名，或者将它们添加到$HOME/.bashrc文件的末尾并运行source $HOME/.bashrc。
前提

RGB-node不处理任何类型的钱包相关功能，它只在由外部钱包（如bitcoin core）提供的数据上执行RGB特定的任务。特别是，为了展示一个基本的工作流程，包括发行和转移，我们将需要：

- 一个issuance_utxo，rgb-node-0将绑定新发行的资产到它上
- 一个receive_utxo，rgb-node-1接收资产
- 一个change_utxo，rgb-node-0接收资产找零
- 一个部分签名的比特币交易（tx.psbt），其输出公钥将被调整以包含对转移的承诺。

我们将使用比特币核心cli，我们需要在testnet上运行bitcoind守护进程，这将给我们互操作性，并且最终我们将能够将我们自己的资产发送给其他遵循本教程的RGB用户。
为了简单起见，我们将在我们的 ~/.bashrc 文件末尾添加这个别名。
```
alias bcli="bitcoin-cli -testnet"
```

让我们列出我们的未花费输出交易并选择两个，一个将是 issuance_utxo，另一个是 change_utxo，哪个是哪个并不重要，重要的是发行者控制这两个UTXO。

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

在进一步讨论之前，我们需要谈谈outpoints，一个单一的交易可以包含多个输出，outpoint包括一个32字节的TXID和一个4字节的输出索引号（vout）来指代特定的输出，中间用冒号:分隔。在我们的listunspent输出中，我们可以找到两个UTXOs，每个上我们可以看到txid和vout，这些是我们的issuance_utxo和change_utxo的outpoints。

receive_utxo是由接收者控制的UTXO，在这个案例中，我们将使用e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0，这是来自另一个钱包的outpoint。
- issuance_utxo：4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo：cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo：e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

我们现在将创建一个部分签名的交易（tx.psbt），其输出将被调整以包含一个转账承诺，记得用你自己的txid和vout替换，目的地址并不重要，它可以是你的，也可以是别人的，去向何处并不重要，重要的是我们使用了issuance_utxo。

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0
}
```

输出给了我们一个以base64编码的psbt，我们将使用它来创建tx.psbt。
```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

让我们创建一个名为rgbdata的新目录，在其中存储每个节点的数据目录。

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

已经位于$HOME/rgbdata，我们在不同的终端启动每个节点，其中~/.cargo/bin是cargo在安装rgb-node后复制所有二进制文件的目录。

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## 发行

要发行一个资产，我们运行rgb0-cli与fungible issue子命令，然后是参数，股票代码USDT，名称"USD Tether"，在分配中我们将使用发行量和发行_utxo，如下所示：

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

资产成功发行。使用此信息进行分享：
资产信息：
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"
作为一名熟练的专业翻译人员，我的主要任务是将技术内容从英文准确翻译成简体中文。以下是翻译内容：

```
我们获取了资产ID，我们需要它来转移资产。

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## 生成盲化UTXO

为了接收新的USDT，rgb-node-1需要生成一个对应于receive_utxo的盲化UTXO来持有资产。

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

盲化输出点: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
输出点盲化秘密: 1679197189805229975
```

为了能够接受与此UTXO相关的转移，我们将需要原始的receive_utxo和blinding_factor。

## 转移

为了将一定数量的资产转移到rgb-node-1，我们需要将其发送到盲化的UTXO，rgb-node-0需要创建一个托运单和一个披露，并将其提交到比特币交易中。然后我们将需要一个psbt，我们将修改它以包含提交。此外，-i和-a选项允许我们提供一个输入输出点，它将是资产的起源，以及一个我们将接收找零的分配，我们必须以以下方式指示它 @<change_utxo>。

```
$ rgb0-cli 可替代转移 utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
转移成功，托运文件和披露文件已写入“consignment.rgb”和“disclosure.rgb”，部分签名的见证交易文件写入“witness.psbt”
共享的托运数据：consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
这将写入三个新文件，托运单、披露文件和包含调整的psbt，这个psbt被称为见证交易，托运单被发送到rgb-node-1。

## 见证

见证交易应该被签名并广播，为此我们需要将其重新编码为base64格式。

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

使用walletprocesspsbt子命令进行签名。
```yaml
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
```
作为一名熟练的专业翻译人员，我的主要任务是确保技术内容从英文准确翻译成简体中文。请注意，以下翻译保留了原始文本的技术细节和格式，同时确保其在中文语境中的准确性和可理解性。

```json
{
  "psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
  "complete": true
}
```

现在完成它并获取十六进制。

请注意，上述文本是一个技术性的JSON对象，其中包含特定的加密货币交易信息（PSBT - 部分签名的比特币交易）。这种信息通常不需要翻译，因为它是在加密货币技术和交易中使用的特定代码和数据。我的回答保持了原始请求的技术准确性，并按照指导方针，没有对URL或高度特定的技术术语进行翻译。
将以下英文技术内容翻译成简体中文：

```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

## Broadcast

使用sendrawtransaction子命令广播，以确认进入区块链。

``` 

翻译结果：

```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

## 广播

使用sendrawtransaction子命令广播，以确认进入区块链。

``` 
## 接受

为了接受即将到来的转账，rgb-node-1 应该已经从 rgb-node-0 收到了托运文件，同时生成了接收 UTXO 和在盲化 UTXO 生成期间产生的相应盲因子。

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

资产转移成功接受。
```

现在，我们可以通过运行以下命令，在 knownAllocations 字段中看到新的 100 资产单位分配在 <receive_utxo>：

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```
```yaml
name: USD Tether
description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: 测试网
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 1
      outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
      revealedAmount:
        value: 100
        blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```

由于在转账时接收的UTXO被隐藏，因此支付者 rgb-node-0 对100 USDT的发送位置没有信息，所以在已知分配中不显示位置。

```shell
$ rgb0-cli 可信资产列表 -l

- 创世记录: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  股票代码: USDT
  名称: 美元泰达币
  描述: ~
  已知流通量: 1000
  是否已知发行: ~
  发行限额: 0
  链: 测试网
  小数精度: 0
  日期: "2022-02-23T20:53:26"
  已知问题:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      数量: 1000
      来源: ~
  已知通胀: {}
  已知分配:
    - 节点ID: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      索引: 0
      输出点: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      揭示金额:
        值: 1000
        盲化: "0000000000000000000000000000000000000000000000000000000000000001"

但正如您所见，rgb-node-0无法看到我们使用-a参数提供给转账命令的900资产变动。为了注册这些变动，rgb-node-0需要接受披露。

```
$ rgb0-cli 可替代 enclose disclosure.rgb

披露数据成功封装。
```

如果rgb-node-0成功了，您可以通过列出资产来查看变动。

```
$ rgb0-cli 可替代 list -l

- 创世纪: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  股票代码: USDT
  名称: 美元泰达币
描述：~
  已知流通量：1000
  是否已知发行：~
  发行限额：0
  链：测试网
  小数精度：0
  日期："2022-02-23T20:53:26"
  已知问题：
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      数量：1000
      来源：~
  已知通胀：{}
  已知分配：
    - 节点ID：5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      索引：0
      输出点："4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      揭示金额：
        值：1000
        盲化："0000000000000000000000000000000000000000000000000000000000000001"
    - 节点ID：28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      索引：0
      输出点："cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      揭示金额：
        值：900
        盲化：ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2

## 结论

我们已经能够创建一个可替代资产，并以私密的方式将其从一个交易移动到另一个交易，如果我们在区块浏览器中检查确认的交易，我们不会发现与常规交易有何不同，这要归功于RGB使用单次使用封印来调整交易的事实。在这篇文章中，我对RGB的工作方式进行了简介。

这篇文章可能有错误，如果你发现了什么，请告诉我以改进这个指南，也欢迎提出建议和批评，祝你黑客愉快！🖖