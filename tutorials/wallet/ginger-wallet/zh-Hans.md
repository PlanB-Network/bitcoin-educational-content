---
name: Ginger Wallet
description: 开源、自托管的比特币钱包软件，来自 Wasabi Wallet 的分叉，整合了混币交易功能
---
![cover](assets/cover.webp)


Ginger Wallet 是一款开源的非托管比特币钱包，专注于保密性和隐私性。它起源于 Wasabi Wallet（版本 2.0.7.2 之后 - MIT 许可证）。

Ginger Wallet 保留了 Wasabi 的技术架构，并添加了一些特定功能。根据 [Ginger Wallet 文档](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet)，Wasabi 强调**自主性和控制权**，而 Ginger 则侧重于**易用性、安全性和简化的用户体验**，使其更易于技术用户使用。

Ginger Wallet 仅适用于电脑（没有移动应用程序）。

## 何为混币交易？（Coinjoin）

**Coinjoin** 是一种特殊的比特币交易结构，它将多个参与者聚集到一起进行单笔协作交易。这种机制将不同用户的输入混合到同一笔交易中，使得资金追踪变得极其困难——如果操作得当，甚至几乎不可能。因此，与传统的比特币交易不同，外部观察者几乎不可能确定所涉及的比特币的来源和目的地。

对于您这位用户而言，CoinJoin 有助于保护您的隐私。例如，如果您收到一笔 10,000 聪的比特币捐赠，捐赠者可以追踪这笔资金，并在某些情况下推断您持有更多比特币，或者监视您的活动。在收到这笔 10,000 聪的捐赠后进行一次 CoinJoin，即可打破追踪机制：捐赠者将无法再从这笔付款中获取任何关于您的信息。

Chaumian CoinJoin 提供高度安全性，因为资金始终由用户完全控制。即使是协调服务器的运营商，在任何情况下也无法转移参与者的比特币。用户和协调者之间无需相互信任：双方各自保留对其私钥的控制权，并拥有验证交易的唯一授权。因此，在 CoinJoin 过程中，任何第三方都无法窃取您的比特币，也无法在您的输入和输出之间建立直接关联。

为了了解更多关于 CoinJoin 的信息，请查看 Plan ₿ Academy 的 BTC 204 课程：

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 安装 Ginger Wallet

为了安装 Ginger Wallet，请访问网站 [Ginger Wallet](https://gingerwallet.io)。

按**下载**，请下载适合您电脑的版本（Windows/MacOs/Linux）。

![screen](assets/fr/03.webp)

另一种方法是访问项目的 [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) 下载。

![screen](assets/fr/04.webp)

然后运行安装程序。

![screen](assets/fr/05.webp)

## 参数设置

### 初始配置

打开 Ginger 钱包，选择您偏好的语言。

![screen](assets/fr/06.webp)


Ginger 会从一开始就提醒您 Coinjoin 过程中涉及的费用。

![screen](assets/fr/07.webp)

然后按 **Start**，再按 **New** 以创建一个新的钱包。

![screen](assets/fr/08.webp)

接下来，保存并确认您的助记词。

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)

为了增强安全性，Ginger Wallet 允许您添加 Passphrase（密语）。

![screen](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

添加密语后，每次尝试访问您的钱包时都会被请求。

![screen](assets/fr/12.webp)

创建钱包时，Ginger Wallet 会自动激活默认的 **Coinjoin**。应用程序会告知这一点，然后可以根据自己的需要自定义设置。

![screen](assets/fr/13.webp)

### 常规设置

创建第一个钱包后，您将进入 Ginger Wallet 界面。

![screen](assets/fr/14.webp)

如果想隐藏钱包中的余额，请激活 **Discreet Mode**（隐秘模式）。

![screen](assets/fr/15.webp)

您可以在 Ginger Wallet 上创建多个钱包。只需点击 **Add a wallet**。

![screen](assets/fr/16.webp)

Ginger 支持通过 Bitcoin Core 标准接口使用硬件钱包，但目前还不能从硬件钱包直接集成或集成到硬件钱包。

兼容的硬件钱包包括（但不限于）：

- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- 等等。

现在点击 **Settings**。



![screen](assets/fr/17.webp)

这些设置是应用程序的通用设置，您在此处所做的配置将应用于所有钱包。

在 **Settings** 中，您会看到以下选项卡：

- **General**（一般）

![screen](assets/fr/18.webp)

- **Appearance**（外观）

在该选项卡中，您可以更改语言、货币和费用显示单位（BTC/Satoshi）等。

![screen](assets/fr/19.webp)

- **Bitcoin**（比特币设置）

通过该选项卡，您可以启用 Bitcoin Knots 在应用程序启动时运行、选择网络（主网络/RegTest）和收费率提供商（Mempool Space/Blockstream info/Full Node）等。

![screen](assets/fr/20.webp)

- **Safety features**（安全功能）

在 "Security" 选项卡中，您可以启用双因素身份验证，激活或停用 Tor，甚至在关闭 Ginger 应用程序后禁用 Tor。

![screen](assets/fr/21.webp)



**注意*** ：

- 对于双因素身份验证，请确保您的身份验证应用程序支持 SHA256 协议和 8 位验证码。Ginger Wallet 需要 8 位 2FA 验证码来增强安全性。这种更长的格式使验证码更难猜测或破解，从而更好地防止未经授权的访问。

默认情况下，所有 Ginger 网络流量都通过 Tor 网络传输，无需手动配置。如果您的系统已启用 Tor，Ginger 会自动优先使用 Tor。

但是，一旦您在设置中禁用 Tor，您的隐私通常仍会得到保护，但以下两种情况除外：

- 在 Coinjoin 过程中，协调者（Coordinator）可能会将您的输入和输出与您的 IP 地址关联起来；

- 在广播交易时，您连接的恶意节点可能会将您的交易与您的 IP 地址关联起来。

每次更改设置后，请务必点击右下角的 “Done” 按钮以保存设置。某些设置需要重启 Ginger Wallet 才能生效。

此外，钱包顶部的搜索栏可让您搜索和访问任何参数等。
![screen](assets/fr/22.webp)

### 钱包配置

应用程序中可以创建多个钱包，因此每个钱包都可以根据您的需要进行配置。为此，请点击组合名称前的**三点**，然后点击 **Portfolio settings**。

![screen](assets/fr/23.webp)

如您所见，除了钱包参数外，您还可以看到您的 UTXOs（您拥有的比特币列表）、统计数据和钱包信息（例如扩展公钥）。

为了返回钱包配置，点击钱包参数后，将进入以下选项卡：

- **General**（可在此更改钱包名称） ；

![screen](assets/fr/24.webp)

- **Coinjoin** （您可以在此自定义此钱包的混币设置） ；

![screen](assets/fr/25.webp)

- **Tools**（在这里您可以检查您的助记词、再次同步您的钱包或删除它）。

![screen](assets/fr/26.webp)

## 接收比特币

![video](https://youtu.be/cqv35wBDWMQ)

在 Ginger Wallet 上的钱包中接收比特币：

- 点击**Receive** ；

![screen](assets/fr/27.webp)

输入您希望将此地址关联的来源名称。这是为了方便您追踪付款而添加的标签。这不会对链上产生任何影响；它只是存储在您本地应用程序中的可追溯性信息；

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)

- 点击 **Generate** 左侧的小箭头，选择地址格式（**SegWit** /**Taproot**），然后点击 **Generate**，即可生成生成地址和二维码。

![screen](assets/fr/29.webp)

发送者将使用此地址或二维码向您发送比特币。

![screen](assets/fr/30.webp)

## 发送比特币

![video](https://youtu.be/2nf5aAimfhg)

为此：

- 点击 **Send** 按钮；
- 输入接收者地址、发送金额和标签；
- 查看交易概览并确认发送。

![screen](assets/fr/31.webp)

## 消费比特币

使用 Ginger 钱包买卖比特币非常简单。只需几个步骤，即可轻松使用您的比特币。

### 购买比特币

![video](https://youtu.be/lEqTBzm5MEA)

Ginger Wallet 用户可以购买比特币。

- 点击 **Buy** 按钮。即使钱包是空的，该按钮仍然可见。

![screen](assets/fr/32.webp)

- 在购买比特币之前，请选择您所在的国家，甚至您所在的州（在某些地区，如加拿大）。事实上，当您第一次点击 **Buy** 功能时，您还需要指定您的地区。

![screen](assets/fr/33.webp)

点击 **Continue** 进入购买流程。

- 然后在专用字段中输入您要购买的比特币数量。您还可以选择交易货币。

![screen](assets/fr/34.webp)

每种货币都有最低和最高购买限额。例如，美元的最高限额为 30,000 美元。

如果您已经购买了，您可以点击 **Previous orders** 按钮查看您的交易历史。将显示过去的交易列表及其状态。

- 选择适合您的购买方案。

此时，您将看到所有可用方案的列表。对于每项优惠，您都可以：

 - 供应商名称 (1) ；
 - 与之前输入的金额相当的比特币数量、支付方式和购买费用 (2) ；
 - **Accept** 按钮 (3)。

![screen](assets/fr/35.webp)

报价中注明的费用不构成额外费用。这些费用已包含在报价总额中。

在屏幕右上角的 **All** 中，您可以按付款方式筛选购买方案。您选择的付款方式将默认设置，但可以随时更改。

![screen](assets/fr/36.webp)

如果找到合适的方案，请点击 **Accept** 按钮以继续购买。然后，您将被重定向到卖家页面，在那里您可以完成交易。


### 出售比特币

Ginger Wallet 用户可以出售比特币。只有在钱包中有可用资金时，才能看到 **Sell** 按钮。

- 点击 **Sell**。

![screen](assets/fr/37.webp)


- 与 **Buy** 选项一样，当您首次使用卖出功能时，必须先选择您的国家，然后才能出售比特币。

- 接下来，您需要输入您希望出售的比特币数量。您可以输入 BTC 或美元等法定货币。

- 完成此操作后，您将看到可用方案的列表。选择适合您的销售优惠，然后点击 **Accept** 以继续。


- 现在，您需要完成交易：
 - 接受方案后，您将被重定向供应商页面；
 - 请按照供应商页面上的说明操作；
 - 随后，您将收到接收者地址和准确的发送金额；
 - 然后返回 Ginger Wallet 继续这一过程；
 - 回到 Ginger Wallet 后，会出现一个对话框，您可以点击 **Send** 以继续。



这将打开 **Send** 页面，并预填接收者地址和金额。您也可以使用主屏幕上的 **Send** 按钮。虽然您可以手动发送交易，但我们建议您通过对话框完成交易，以该优化流程。

## 在 Ginger Wallet 上进行 Coinjoin 交易

![Vidéo](https://youtu.be/AJe67RDfB1A)



使用直接集成到 Ginger Wallet 中的 **Coinjoin**，保护比特币的隐私。该钱包采用 **WabiSabi**，一种 Chaumian CoinJoin 协议，旨在简化 CoinJoin 交易流程，提高交易效率。

您可以选择最适合自己的 Coinjoin 策略（自动或手动）。

下载 Ginger Coinjoin 后即可使用（无需额外步骤）。Ginger Coinjoin 会自动在后台运行，以保护您每笔交易的隐私。实际上，只要您有可以匿名的余额，Coinjoin 模块就会出现。

至于手动启动 Coinjoin，只需一键操作。启动一轮，然后等待建立并确认 Coinjoin 交易。您将在界面中看到匿名化分数。

您可以进行多次混币交易，直到达到所需的匿名化级别。您还可以从混合中排除某些部分。

默认情况下，Ginger 使用其自身的协调者，所有参数均已预配置，费用也有保障。价值超过 0.03 BTC 的代币 Coinjoin 交易，除挖矿费用外，还将收取 0.3% 的协调者费用。价值 0.03 BTC 或以下的交易以及 Remix 交易，即使是单笔交易，也免收协调者费用。因此，使用 Coinjoin 资金进行的支付允许发送者和接收者重新进行混币交易，而无需支付协调器费用。

Ginger 更倾向于参与者人数较多的 Coinjoin 回合，而不是规模较小、速度较快的回合。规模较大的 Coinjoin 回合能够提高匿名性、还提供更低的成本和更高的区块空间利用率。

## 安全和最佳做法

为了实现去中心化和保护隐私，我们需要遵循以下几项最佳实践：

- 请务必将助记词存放在离线的安全位置；
- 如果您的电脑丢失或怀疑有人未经授权访问，请立即创建新的钱包。将您的资金转入新的钱包，并删除旧的钱包；
- 为每次收款使用不同的地址，避免重复使用地址；
- 请务必只从官方 GitHub 账户或官方网站下载钱包应用程序。

现在您已经熟悉了如何使用 Ginger 钱包应用程序发送、接收和使用您的比特币。

如果您觉得本教程有用，请在下方给我留下绿色拇指。请随时通过您的社交媒体平台分享本文。非常感谢！

我还建议您查看这篇关于如何使用 Liana 电脑应用程序收发比特币以及如何实施自动化遗产规划的教程。

https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
