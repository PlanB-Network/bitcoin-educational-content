---
name: RGB CLI
description: 如何在 RGB 上创建和交换智能合约？
---
![cover](assets/cover.webp)

在本教程中，我们将使用 LNP/BP 协会创建的命令行工具 "rgb"，按部就班地编写合同。目的是展示如何安装和操作 CLI、编译模式、导入接口和接口实现，然后发布 RGB 资产。我们还将了解底层逻辑，包括编译和状态验证。本教程结束时，您应该能够重现流程并创建自己的 RGB 合同。

## RGB 协议提醒

RGB 是一个运行于比特币之上的协议，可模拟智能合约功能和数字资产管理，而不会对其所基于的区块链造成过载。与传统的链上智能合约（如以太坊上）不同，RGB 依赖于 "*客户端验证*"系统：大部分数据和状态历史记录都由参与方独自交换和存储，而比特币区块链只承载小规模的加密承诺（通过*Tapret*或*Opret*等机制）。因此，在 RGB 协议中，比特币区块链只充当时间戳服务器和双重消费保护系统。

RGB 合约的结构类似于一个进化状态机。它以 "创世纪 "开始，"创世纪 "根据严格类型化和编译的 "模式 "定义初始状态（例如，描述供应、行情或其他元数据）。然后进行状态转换，必要时进行状态扩展，以修改或扩展该状态。无论是转移可替代资产（RGB20）还是创建独一无二的资产（RGB21），每一项操作都涉及*一次性封印*。这些封印将比特币UTXO与链外状态连接起来，防止重复消费，同时确保保密性和可扩展性。

要了解有关 RGB 协议工作原理的更多信息，我建议您参加这个综合培训课程：

https://planb.network/courses/csv402
RGB 的内部逻辑基于 Rust 库，作为开发人员，您可以将 Rust 库导入到您的项目中，以管理*客户端验证*部分。此外，LNP/BP 团队正在开发其他语言的绑定，但尚未最终确定。此外，比特币交易所（Bitfinex）等其他实体也在开发自己的集成栈，但我们将在另一篇教程中讨论这些问题。目前，"rgb "CLI 是官方参考，尽管它还相对不够完善。

## 安装和演示 rgb CLI 工具

主命令名为 `rgb`。它的设计让人联想到 `git`，有一系列子命令用于操作合约、调用合约、发行资产等。比特币钱包目前尚未集成，但将在即将推出的版本（0.11）中集成。下一个版本将使用户能够直接从`rgb`创建和管理他们的钱包（通过描述符），包括生成 PSBT、兼容外部硬件（如硬件钱包）进行签名，以及与 Sparrow 等软件的互操作性。这将简化整个资产发行和转移过程。

### 通过货运安装

我们在 Rust 中用 .NET Framework 安装该工具：

```bash
cargo install rgb-contracts --all-features
```

(注意：该板块名为 "rgb-contracts"，安装的命令名为 "rgb"。如果已存在名为 `rgb` 的板块，则可能会发生碰撞，因此命名为 `rgb`)

安装过程中会编译大量依赖项（如命令解析、Electrum 集成、零知识证明管理等）。

安装完成后，.NET Framework 将自动运行：

```bash
rgb
```

运行 `rgb`（不带参数）会显示可用的子命令列表，如 `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer` 等。你可以更改本地存储目录（存放所有日志、示意图和实现的储藏室）、选择网络（testnet、mainnet）或配置你的 Electrum 服务器。

![RGB-CLI](assets/fr/01.webp)

### 控制措施概览

运行以下命令时，你会看到默认情况下已经集成了一个 `RGB20` 界面：

```bash
rgb interfaces
```

如果未集成该接口，请克隆.NET Framework 4.0：

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

编译：

```bash
cargo run
```

然后导入您选择的界面：

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

然而，我们被告知还没有将模式导入软件。储藏库中也没有合同。要查看它，请运行命令 ：

```bash
rgb schemata
```

然后，您可以克隆该资源库，以检索某些原理图：

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

该资源库的 `src/` 目录中包含多个 Rust 文件（例如 `nia.rs`），这些文件定义了模式（NIA 表示 "*Non Inflatable Asset*"，UDA 表示 "*Unique Digital Asset*"等）。编译时，您可以运行 ：

```bash
cd rgb-schemata
cargo run
```

这会生成多个与编译示意图相对应的 `.rgb` 和 `.rgba` 文件。例如，您可以找到 `NonInflatableAsset.rgb`。

### 导入模式和接口实现

现在您可以将原理图导入 `rgb` ：

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

这将把它添加到本地存储库中。如果我们运行以下命令，就会看到模式已经出现：

```bash
rgb schemata
```

## 合同创建（签发）

创建新资产有两种方法：


- 我们可以使用 Rust 中的脚本或代码，通过填充模式字段（全局状态、自有状态等）来构建合约，并生成`.rgb`或`.rgba`文件；
- 或者直接使用 `issue` 子命令，用 YAML（或 TOML）文件描述令牌的属性。

您可以在 Rust 的`examples`文件夹中找到示例，其中说明了如何构建`ContractBuilder`、填写`global state`（资产名称、股票代码、供应量、日期等）、定义 Owned State（分配给哪个 UTXO），然后将所有这些编译成您可以导出、验证并导入储藏库的*合同委托。

另一种方法是手动编辑 YAML 文件，以自定义 "ticker"、"name "和 "supply "等。假设文件名为 `RGB20-demo.yaml`。您可以指定 ：


- spec`：代码、名称、精度 ；
- "条款"：用于法律通告的字段；
- `issuedSupply` ：已发行的代币数量；
- `assignments`: 表示一次性使用密封件（*密封件定义*）和已解锁的数量。

下面是一个要创建的 YAML 文件示例：

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

然后只需运行命令 ：

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

在我的情况中，唯一模式标识符（用单引号括起来）是 `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k`，我没有输入任何发行人。因此，我的订单是 ：

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

如果不知道模式 ID，请运行命令 ：

```bash
rgb schemata
```

CLI 会回复说，已签发了一份新合同，并将其添加到了储量中。如果我们键入下面的命令，就会看到现在又多了一份合同，与刚刚签发的合同相对应：

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

然后，下一条命令会显示全局状态（名称、代号、供应量......）和自有状态列表，即分配情况（例如，UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1` 中定义的 100 万个 `PBN` 代币）。

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## 导出、导入和验证

要与其他用户共享这份合同，可以将其从储藏库导出到 .NET 文件：

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

可将 `myContractPBN.rgb` 文件传给其他用户，后者可使用命令 ：

```bash
rgb import myContractPBN.rgb
```

导入时，如果是简单的*合同委托*，我们会收到"`导入委托 rgb`"信息。如果是较大的*状态转换委托*，命令会有所不同（`rgb accept`）。

为确保有效性，您还可以使用本地验证功能。例如，您可以运行 ：

```bash
rgb validate myContract.rgb
```

### 储藏库的使用、验证和显示

需要提醒的是，储藏库是模式、接口、实现和合约（创世纪 + 过渡）的本地库存。每运行一次 "导入"，就会向储藏库添加一个元素。可以使用命令 ：

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

这将生成一个文件夹，其中包含整个藏品的详细信息。

## 转账和 PSBT

要进行转账，您需要操作一个本地比特币钱包来管理 "Tapret "或 "Opret "承诺。

### 生成发票

在大多数情况下，合约参与者（如 Alice 和 Bob）之间的互动是通过生成发票来实现的。如果爱丽丝希望鲍勃执行某些操作（代币转移、重新发行、DAO 中的操作等），爱丽丝就会创建一张发票，详细说明她对鲍勃的指示。因此，我们有 ：


- Alice** （发票开具人） ；
- 鲍勃**（接收和执行发票者）。

与其他生态系统不同，RGB 发票并不局限于付款的概念。它可以嵌入与合约相关的任何请求：撤销密钥、投票、在 NFT 上创建雕刻（*engraving*）等。相应的操作可在合约接口中描述。相应的操作可以在合约界面中描述。

以下命令生成一张 RGB 发票：

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

与 ：


- $CONTRACT`：合同标识符 (*ContractId*) ；
- `$INTERFACE`：要使用的接口（如 `RGB20`） ；
- `$ACTION`：接口中指定的操作名称（对于简单的可替换令牌传输，可以是 "Transfer"（传输））。如果接口已经提供了默认操作，则无需在此再次输入；
- $STATE`：要传输的状态数据（例如，如果传输的是可替换令牌，则是令牌的数量）；
- $SEAL`：受益人（Alice）的一次性印章，即对UTXO的明确引用。鲍勃将使用此信息建立见证交易，相应的输出将属于爱丽丝（以*屏蔽的UTXO*或未加密的形式）。

例如，使用以下命令

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI 将生成类似于 .NET 的发票：

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

它可以通过任何渠道（文本、QR 码等）传送给 Bob。

### 进行转账

要从本发票转账 ：


- 鲍勃（在他的储藏中持有代币）有一个比特币钱包。他需要准备一个比特币交易（以 PSBT 的形式，例如 `tx.psbt`），花费所需 RGB 代币所在的 UTXO，外加一个用于货币（兑换）的 UTXO；
- 鲍勃执行以下命令

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- 这将生成一个 `consignment.rgb` 文件，其中包含 ：
 - 过渡历史向 Alice 证明了代币的真实性；
 - 将代币转移到 Alice 的一次性印章的新过渡；
 - 见证交易（无符号）。
- Bob 将此 `consignment.rgb` 文件发送给 Alice（通过电子邮件、共享服务器或 RGB-RPC 协议、Storm 等）；
- Alice 接收到 `consignment.rgb` 并将其存入自己的存储库：

```bash
alice$ rgb accept consignment.rgb
```


- CLI 会检查过渡的有效性，并将其添加到 Alice 的存储库中。如果无效，命令会失败，并带有详细的错误信息。否则，命令成功，并报告样本交易尚未在比特币网络上广播（Bob 正在等待 Alice 的绿灯）；
- 作为确认，"接受 "命令会返回一个签名（*付款单*），爱丽丝可以将该签名发送给鲍勃，向他表明她已经验证了*委托*；
- 然后，鲍勃就可以签署并发布（"--发布"）他的比特币交易：

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- 一旦这笔交易在链上得到确认，该资产的所有权就被视为转移给了 Alice。爱丽丝的钱包在监控交易的挖矿过程中，会看到新的 "拥有状态 "出现在它的钱包中。

现在您已经知道如何签发和转移 RGB 合同了。如果您觉得本教程有用，请在下面竖起大拇指，我将不胜感激。欢迎在您的社交网络上分享本文。非常感谢！

我还推荐另一篇教程，其中我介绍了如何启动兼容 RGB 的闪电节点，以几乎即时的方式交换代币：

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea