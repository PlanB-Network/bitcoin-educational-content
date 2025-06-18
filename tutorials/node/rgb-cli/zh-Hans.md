---
name: RGB CLI
description: 如何在RGB上创建和交换智能合约？
---
![cover](assets/cover.webp)

在本教程中，我们将按照步骤逐步编写一份合约，使用由LNP/BP协会创建的命令行工具 rgb。目的在于展示如何安装和操作CLI、编译架构（Schema）、导入接口和接口实现，然后发布RGB资产。我们还将了解底层逻辑，包括编纂和状态验证。完成本教程后，您应该能够重复该过程，并创建自己的RGB合约。

## RGB协议提醒

RGB是一个运行于比特币之上的协议，可模拟智能合约功能和数字资产管理，而不会对其所基于的区块链造成过载。与传统的链上智能合约（如在以太坊上的合约）不同，RGB 依赖于 "*客户端验证（Client-side validation）*"系统：大部分数据和状态历史记录都由参与方独自交换和存储，而比特币区块链只承载小规模的加密承诺（通过*Tapret*或*Opret*等机制）。因此，在RGB协议中，比特币区块链只充当时间戳服务器和双重支付保护系统。

RGB合约的结构类似于一个进化状态机。它以"Genesis"为起点，"Genesis"根据严格类型化和编纂的 "模式 "定义初始状态（例如，描述供应(supply)、行情(ticker)或其他元数据）。然后进行状态转换，必要时进行状态扩展，以修改或扩展该状态。无论是转移可替代资产（RGB20）还是创建独特的资产（RGB21），每一项操作都涉及*一次性封印(Single-use Seals)*。这些封印将比特币UTXO与链外状态连接起来，防止重复消费，同时确保保密性和可扩展性。

如果您想要了解关于RGB协议工作原理的更多信息，我建议您参加这门全面的培训课程：

https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

RGB的内部逻辑基于Rust库（Library），您作为开发人员可以将Rust库导入到您的项目中，以管理*客户端验证（Client-side Validation）*部分。此外，LNP/BP团队正在开发其他语言的绑定，但尚未通过最后确定。此外，比特币交易所（Bitfinex）等其他实体也在开发自己的集成栈，但我们将在另一篇教程中讨论这些问题。目前，"rgb "CLI 是官方参考，尽管它还相对不够完善。


## 安装和演示rgb CLI工具

主命令名为`rgb`。它的名字的设计将让人联想到`git`，有一系列子命令用于更改合约、调用合约、发行资产等。比特币钱包目前尚未整合，但将在即将推出的版本（0.11）中结合。下一个版本将使用户能够直接从`rgb`创建和管理他们的钱包（通过描述符），包括生成PSBT（部分签名的比特币交易）、对外部硬件进行签名（如硬件钱包）的兼容性，以及与Sparrow等软件的互操作性。这将简化整个资产发行和转移过程。

### 通过Cargo的安装

我们将在Rust中使用 .NET Framework 安装该工具：

```bash
cargo install rgb-contracts --all-features
```

(注意：该板块的名称为 "rgb-contracts"，安装的命令名为 "rgb"。如果已存在名为 `rgb` 的板块，则可能会发生碰撞)

安装过程中会收集大量依赖项（如命令解析（command parsing）、Electrum 集成、零知识证明管理等）。

安装完成后，.NET Framework将自动运行：

```bash
rgb
```

运行 `rgb`（不带参数）会显示可用的子命令列表，如 `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer` 等。您可以更改局部存储器目录（存放所有日志、示意图和接口实现的储藏室）、选择网络（testnet、mainnet）或配置您的Electrum服务器。

![RGB-CLI](assets/fr/01.webp)

### 控制措施概览

运行以下命令时，您会看到默认情况下已经集成了一个 `RGB20` 界面：

```bash
rgb interfaces
```

如果该接口未被集成，请克隆.NET Framework 4.0：

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

对其进行编纂：

```bash
cargo run
```

然后导入您选择的界面：

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

然而，我们将被告知未有被导入到软件的模式（schema）。储藏库中也没有合约。如果您想要查看它，请运行以下命令 ：

```bash
rgb schemata
```

然后，您可以克隆该资源库，以检索某些原理图：

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

该资源库的 `src/` 目录中包含多个Rust文件（例如 `nia.rs`），这些文件定义了模式（NIA 表示 "*Non Inflatable Asset*"，UDA 表示 "*Unique Digital Asset*"等）。您可以运行以下命令以进行编纂 ：

```bash
cd rgb-schemata
cargo run
```

这会生成多个与编译示意图相对应的 `.rgb` 和 `.rgba` 文件。例如，您将看到 `NonInflatableAsset.rgb`。

### 导入模式和接口实现

现在您可以将原理图导入`rgb` ：

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

这将把它添加到局部存储库中。如果我们运行以下命令，就会看到模式已经出现：

```bash
rgb schemata
```

## 合约创建（签发）

创建新资产有两种方法：


- 我们可以使用 Rust 中的脚本或代码，通过填充模式字段（全局状态（global state）、拥有状态（Owned States)等）来构建合约，并生成`.rgb`或`.rgba`文件；
- 或者直接使用 `issue` 子命令，用YAML（或TOML）文件描述代币的属性。

您可以在Rust的`examples`文件夹中找到示例，其中说明了如何构建`ContractBuilder`、填写`global state`（资产名称、代号、供应量、日期等）、定义 Owned State（分配给哪个UTXO），然后将所有编纂成您可以导出、验证并导入储藏库的*合约委托（Contract consignment）*。

另一种方法是手动编辑YAML文件，以自定义 "ticker"、"name "和 "supply "等。假设文件名为 `RGB20-demo.yaml`。您可以设定为：


- `spec`：代号、名称、精度 ；
- `terms`：用于法律通告的字段；
- `issuedSupply` ：已发行的代币数量；
- `assignments`: 表示一次性使用密封件（*密封件定义（seal definition）*）和已解锁的数量。

下面是一个要创建的YAML文件示例：

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

然后只需运行以下命令 ：

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

在我的示范，唯一模式标识符（用单引号括起来）是 `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k`，我没有输入任何发行人。因此，我的命令如下 ：

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

如果不知道模式ID，请运行以下命令 ：

```bash
rgb schemata
```

CLI会回复说，已签发了一份新合约，并将其添加到了储量中。如果我们键入下面的命令，就会看到现在又多了一份合约，对应于刚刚签发的合约：

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

然后，下一条命令会显示全局状态（名称、代号、供应量......）和自有状态列表，即分配情况（例如，UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1` 中定义的100万个`PBN`代币）。

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## 导出、导入和验证

如果您想要与其他用户共享这份合约，您可以将其从储藏库导出到 .NET 文件中：

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

此 `myContractPBN.rgb` 文件可被传给其他用户，后者可使用以下命令 ：

```bash
rgb import myContractPBN.rgb
```

导入时，如果是简单的*合约委托（Contract consignment）*，我们会收到"`Importing consignment rgb`"信息。如果是较大的*状态转换委托（State transition consignment）*，命令会有所不同（`rgb accept`）。

为确保有效性，您还可以使用本地验证功能。例如，您可以运行以下命令 ：

```bash
rgb validate myContract.rgb
```

### 储藏库的使用、验证和显示

作为提醒，储藏库是模式、接口、实现和合约（Genesis + 转换）的本地库存。每运行一次 "导入"，就会向储藏库添加一个元素。您可以运行以下命令以查看储藏库：

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

这将生成一个文件夹，其中包含整个储藏库的详细信息。

## 转账和PSBT（部分签名的比特币交易）

如果您想要进行转账，您需要改造一个本地比特币钱包来管理 "Tapret "或 "Opret "承诺（commitment）。

### 生成发票

在大多数情况下，合约参与者（如Alice和Bob）之间的互动是通过生成发票来实现的。如果Alice想要Bob执行某些操作（代币转移、重新发行、DAO中的操作等），Alice就会创建一张发票，详细说明她对Bob的指示。因此，Alice和Bob的角色如下：


- Alice（发票发行人） ；
- Bob（接收和执行发票者）。

与其他系统不同，RGB发票并不局限于付款的概念。它可以嵌入与合约相关的任何请求：撤销密钥、投票、在NFT上创建雕刻（*engraving*）等。相应的操作可在合约接口中描述。

以下命令将生成一张RGB发票：

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

解析：


- $CONTRACT`：合同标识符 (*ContractId*) ；
- `$INTERFACE`：将被使用的接口（如 `RGB20`） ；
- `$ACTION`：接口中指定的操作名称（对于简单的可替换代币传输，可以是 "Transfer"（传输））。如果接口已提供默认操作，则无需在此再次输入；
- $STATE`：要传输的状态数据（例如，如果传输的是可替换令牌，则是令牌的数量）；
- $SEAL`：受益人（Alice）的一次性印章，即对UTXO的明确参考。Bob将使用此信息构建见证交易，相应的输出将属于Alice（以*屏蔽的UTXO（blinded UTXO）*或未加密的形式）。

例如，使用以下命令：

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI将生成类似于 .NET 的发票：

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

它可以通过任何渠道（文本、二维码等）传送给 Bob。

### 进行转账

如果您想要从本发票转账 ：


- Bob（在他的储藏中持有代币）有一个比特币钱包。他需要准备一个比特币交易（以 PSBT 的形式，例如 `tx.psbt`），花费所需 RGB 代币所在的 UTXO，外加一个用于货币（兑换）的 UTXO；
- Bob执行以下命令：

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- 这将生成一个 `consignment.rgb` 文件，其中包含 ：
 - 转换历史，其向Alice证明了代币的真实性；
 - 将代币转移到 Alice的一次性印章的新转换；
 - 见证交易（无签署）。
- Bob将此 `consignment.rgb` 文件发送给 Alice（通过电子邮件、共享服务器或 RGB-RPC 协议、Storm 等平台）；
- Alice 接收到 `consignment.rgb` 并将其存入自己的存储库：

```bash
alice$ rgb accept consignment.rgb
```


- CLI 会检查转换的有效性，并将其添加到 Alice 的存储库中。如果转换无效，命令会失败，并带有详细的错误信息。否则，如果命令成功，并报告样本交易尚未在比特币网络上广播（Bob 正在等待 Alice 的批准）；
- 通过确认，"接受 （accept）"命令会返回一个签名（*付款单（payslip）*），Alice可以将该签名发送给Bob，向他表明她已经验证了此*委托（consignment）*；
- 然后，Bob就可以签署并发布（"--publish"）他的比特币交易：

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- 一旦这笔交易在链上得到确认，该资产的所有权就被视为被转移给Alice了。Alice的钱包在监控交易的挖矿过程中，会看到新的 "拥有状态（Owned State）"出现在它的钱包中。

现在您已经了解如何签发和转移 RGB 合约了。如果您觉得本教程有用，请在下面竖起大拇指，我将不胜感激。欢迎在您的社交网络上分享本文。非常感谢！

我还推荐另一篇教程，其中我介绍了如何启动兼容RGB的闪电节点，以几乎即时的方式交换代币：


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea
