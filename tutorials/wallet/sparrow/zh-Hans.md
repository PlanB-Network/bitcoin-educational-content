---
name: 麻雀 Wallet
description: 安装、配置和使用 Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet 是 Craig Raw 开发的一款自我保管 Bitcoin 投资组合管理软件。这款开源软件因其众多功能和直观的 Interface 而受到比特币用户的青睐。

使用麻雀有两种方法：


- 如 Hot Wallet，您的私人密钥存储在个人电脑中。
- 作为 Cold Wallet 管理器，私钥保存在 Hardware Wallet 上。在这种模式下，Sparrow 只操作公开的 Wallet 信息、跟踪资金、生成地址和建立交易，但需要 Hardware Wallet 签名才能使这些交易生效。因此，它可以取代 Ledger Live 或 Trezor Suite 等应用程序。

Sparrow 支持单签名和多签名钱包，可以流畅地管理多个钱包。例如，您可以同时控制一个连接到 Ledger 的 Wallet，另一个连接到 Trezor，还有一个 Hot Wallet。

该软件还提供先进的硬币控制功能，让您可以精确选择在交易中使用哪些UTXO，从而优化保密性。

在连接方面，麻雀让您可以通过 Electrum 服务器或 Bitcoin Core 远程连接到自己的 Bitcoin 节点。如果你还没有自己的节点，也可以使用公共节点。远程连接通过 Tor 进行。

## 安装麻雀 Wallet

访问 [Sparrow Wallet 官方下载页面](https://sparrowwallet.com/download/)，选择与您的操作系统相对应的软件版本。

![Image](assets/fr/01.webp)

在安装软件之前，检查软件的完整性和真实性非常重要。如果您不知道如何操作，请点击此处查看完整教程：

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow 安装完成后，您可以跳过初始说明屏幕，直接进入连接管理屏幕。

![Image](assets/fr/02.webp)

## 连接到 Bitcoin 网络

要与 Bitcoin 网络互动并广播您的交易，Sparrow 必须连接到 Bitcoin 节点。建立这种连接有三种主要方式：


- 🟡 使用公共节点，即连接到允许此类连接的第三方节点。如果您没有自己的 Bitcoin 节点，此选项可让您快速开始使用 Sparrow。不过，您连接的节点会看到您的所有交易，这可能会危及您的机密性。控制自己的密钥至关重要，但拥有自己的节点更好。因此，只有当你刚刚开始使用 Sparrow 时才会使用这个选项，同时也要注意隐私泄露的风险。
- 🟢 连接到 Bitcoin Core 节点。如果您有自己的 Bitcoin Core 节点，您可以将其连接到 Sparrow Wallet，如果 Bitcoin Core 安装在同一台机器上，可以在本地连接，也可以远程连接。
- 通过 Electrum 服务器连接。如果您的 Bitcoin 节点配备了 Electrs（如 Umbrel 或 Start9 等节点一体机解决方案），您可以从 Sparrow 远程连接到它。

**最好在自己的节点上通过 Electrs 或 Bitcoin Core 进行连接，以减少对第三方的信任并优化保密性**。

### 连接到公共节点 🟡

连接到公共节点非常简单。点击 "*公共服务器*"选项卡。

![Image](assets/fr/03.webp)

从下拉列表中选择一个节点。

![Image](assets/fr/04.webp)

然后点击 "*测试连接*"。

![Image](assets/fr/05.webp)

连接完成后，麻雀 Wallet 将在 Interface 的右下角显示一个黄色的"√"，表示您已连接到公共节点。

![Image](assets/fr/06.webp)

### 连接到 Bitcoin 核心 🟢

连接 Bitcoin 节点的第二种方法是将 Sparrow 与 Bitcoin Core 相连。如果 Bitcoin Core 安装在同一台机器上，则通过 cookie 文件进行身份验证。如果 Bitcoin Core 安装在远程机器上，则需要使用 `Bitcoin.conf` 文件中定义的密码。

请注意，如果使用被剪切的 Bitcoin 核心节点，就无法还原包含本地存储区块之前的事务的 Wallet。不过，对于在 Sparrow 上创建的新 Wallet 来说，这不是问题：即使节点被修剪，新事务也是可见的。

要配置 Bitcoin Core 节点，可根据操作系统参考以下教程之一：

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

在 Sparrow 上，转到 "*Bitcoin 核心*"选项卡。

![Image](assets/fr/07.webp)

**具有 Bitcoin 核心局部：**

如果计算机上安装了 Bitcoin Core，请在软件文件中找到`Bitcoin.conf`文件。如果该文件不存在，您可以创建它。用文本编辑器打开该文件并插入以下一行：

```ini
server=1
```

然后保存更改。

您也可以通过 Bitcoin-QT 的 Interface 图形进行此操作，方法是导航至 "*设置*" > "*选项...*"并激活 "*启用 RPC 服务器*"选项。>"*选项...*"并激活 "*启用 RPC 服务器*"选项。

做完这些更改后，不要忘记重新启动软件。

![Image](assets/fr/08.webp)

然后返回 Sparrow Wallet，输入 cookie 文件的路径，通常与 `Bitcoin.conf`位于同一文件夹，具体取决于操作系统：

| **macOS** | ~/Library/Application Support/Bitcoin | **macOS** | ~/Library/Application Support/Bitcoin

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin | %APPDATA%\Bitcoin | %APPDATA%\Bitcoin

| **Linux** | ~/.Bitcoin | **Bitcoin

![Image](assets/fr/09.webp)

其他参数保持默认，URL `127.0.0.1` 和端口 `8332`，然后点击 "*测试连接*"。

![Image](assets/fr/10.webp)

连接已建立。右下角会出现一个 Green 标记，表示您已连接到 Bitcoin 核心节点。

![Image](assets/fr/11.webp)

**配备 Bitcoin 核心远程：**

如果 Bitcoin Core 安装在连接到同一网络的另一台机器上，请首先在软件文件中找到 "Bitcoin.conf" 文件。如果该文件不存在，您可以创建它。用文本编辑器打开该文件并添加以下一行：

```ini
server=1
```

编辑文件后，确保将其保存在操作系统的相应文件夹中：

| **macOS** | ~/Library/Application Support/Bitcoin | **macOS** | ~/Library/Application Support/Bitcoin

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin | %APPDATA%\Bitcoin | %APPDATA%\Bitcoin

| **Linux** | ~/.Bitcoin | **Linux** | ~/.Bitcoin

也可通过 Bitcoin-QT Interface 图形化 Interface 执行此操作。进入 "*设置*"菜单，然后是 "*选项...*"，勾选相应复选框激活 "*启用 RPC 服务器*"选项。如果 "Bitcoin.conf "文件不存在，您可以点击 "*Open Configuration File*（*打开配置文件*）"，直接从 Interface 创建该文件。

![Image](assets/fr/12.webp)

查找本地网络中托管 Bitcoin Core 的机器的 IP Address。为此，您可以使用 [Angry IP Scanner](https://angryip.org/) 等工具。为方便起见，我们假设您的节点的 IP Address 为 `192.168.1.18`。

在 `Bitcoin.conf` 文件中添加以下几行，设置 `rpcbind=192.168.1.18` 以匹配节点的 IP Address。

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

在 `Bitcoin.conf` 文件中，为远程连接添加用户名和密码。确保将 `loic` 替换为用户名，将 `my_password` 替换为高强度密码：

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

修改并保存文件后，重新启动 Bitcoin-QT 软件。

现在您可以返回麻雀 Wallet。转到 "*用户/密码*"选项卡。输入您在 `Bitcoin.conf` 文件中配置的用户名和密码。其他参数保持默认，即 URL `127.0.0.1` 和端口 `8332`。然后点击 "*测试连接*"。

![Image](assets/fr/15.webp)

连接已建立。右下角会出现 Green 标记，表示您已连接到 Bitcoin 核心节点。

![Image](assets/fr/16.webp)

### 连接到 Electrum 服务器 🔵

最后一种连接方式是使用远程 Electrum 服务器。这种方法可以让你从其他设备通过 Tor 连接到你的节点，并利用索引器在 Sparrow 上更快地浏览你的投资组合。如果你有像 Umbrel 或 Start9 这样的 "盒装节点 "解决方案，就特别适合使用这种方法。

为此，请获取 Electrum 服务器的 Tor `.onion' Address。以 Umbrel 为例，你可以在 Electrs 应用程序中找到它。

![Image](assets/fr/17.webp)

在 Sparrow Wallet 上，访问 "*私人电子货币*"选项卡。

![Image](assets/fr/18.webp)

在空白处输入您的 Tor Address。其他设置可以保持默认。然后点击 "*测试连接*"。

![Image](assets/fr/19.webp)

连接已确认。如果关闭此窗口，右下角会出现一个蓝色的"√"，表明您已连接到 Electrum 服务器。

![Image](assets/fr/20.webp)

## 创建温暖的投资组合

现在 Sparrow Wallet 已经配置好与 Bitcoin 网络通信，您可以创建第一个 Wallet了。本节将指导您创建 Hot Wallet，即私钥存储在您的计算机上的 Wallet。由于您的电脑是一台与互联网相连的复杂机器，因此它的攻击面非常大。因此，Hot Wallet 只能用于存储有限数量的比特币。如果要存储较大数额的比特币，可选择安全的 Wallet 和 Hardware Wallet。如果这就是你要找的，你可以跳到下一节。

要创建 Hot Wallet，请在 Sparrow Wallet 主页屏幕上点击 "*文件*"选项卡，然后点击 "*新建 Wallet*"。

![Image](assets/fr/21.webp)

输入投资组合的名称，然后点击 "*创建 Wallet*"。

![Image](assets/fr/22.webp)

在 Interface 的顶部，您可以选择创建 "*单签名*"或 "*多签名*"组合。在下方，选择锁定UTXO 的脚本类型。我建议您使用最新的标准："*Taproot (P2TR)*"。

![Image](assets/fr/23.webp)

然后点击 "*新的或导入的 Software Wallet*"。

![Image](assets/fr/24.webp)

选择 BIP39 标准，因为几乎所有 Bitcoin 组合软件都支持该标准。然后，选择恢复短语的长度。目前，12 个字的短语就足够了，因为两者的安全性相似，但 12 个字的短语更容易保存。

![Image](assets/fr/25.webp)

点击 "*generate New*"按钮，generate 您的 Wallet 的 Mnemonic 短语。这个短语可以完全无限制地访问您的所有比特币。任何拥有该短语的人都可以盗取您的资金，即使无法实际访问您的电脑。

这 12 个字的短语可以在电脑丢失、被盗或损坏的情况下恢复对比特币的访问。因此，仔细保存并将其存放在安全的地方非常重要。

您可以将其刻在纸上，或者为了提高安全性，将其刻在不锈钢上，以防火灾、水灾或倒塌。Mnemonic 的介质选择取决于您的安全策略，但如果您使用的是麻雀作为含有适量 Wallet 的温性消费介质，纸张就足够了。

有关保存和管理 Mnemonic 短语的正确方法的更多信息，我强烈推荐您阅读本教程，尤其是初学者：

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**显然，您绝不能像我在本教程中所做的那样，在互联网上分享这些文字。本例 Wallet 将仅用于 Testnet，并将在教程结束时删除。

您也可以点击 "*使用 passphrase*"方框，选择添加 passphrase BIP39。警告：使用 passphrase 可能非常有用，但如果您不了解它的工作原理，就会有很大风险。因此，我强烈建议您阅读这篇相关的理论短文：

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

将 Mnemonic 和任何 passphrase 保存到物理介质后，单击 "*确认备份*"。

![Image](assets/fr/27.webp)

重新输入 12 个单词，确认已正确保存，然后点击 "*创建密钥库*"。

![Image](assets/fr/28.webp)

然后点击 "*Import Keystore*（导入密钥库*）"，从 Mnemonic 短语中导入 generate 组合密钥。

![Image](assets/fr/29.webp)

点击 "*应用*"，完成组合创建。

![Image](assets/fr/30.webp)

设置一个强大的密码，以确保能访问您的 Sparrow 投资组合。最好将密码保存在密码管理器中，以免忘记。请注意，该密码不参与密钥的生成。它只用于通过麻雀 Wallet 访问您的 Wallet。因此，即使没有这个密码，您的 Mnemonic 短语也足以从任何兼容 BIP39 的应用程序访问您的比特币。

![Image](assets/fr/31.webp)

您的 Hot Wallet 已经创建。如果您不打算将 Hardware Wallet 与麻雀一起使用，可以跳到本教程的*接收比特币*部分。

## 管理 Cold 投资组合

使用 Sparrow Wallet 的第二种方法是将其设置为 Hardware Wallet 的投资组合管理器。在这种配置下，Bitcoin Wallet 的私钥只保留在 Hardware Wallet 上，而 Sparrow 只能访问公共信息。这种方法比上面讨论的 Hot 钱包具有更高的安全性，因为私钥保存在专门的设备上，通常带有安全芯片，不与互联网连接，因此攻击面比传统计算机小得多。

将 Hardware Wallet 与 Sparrow 连接有两种主要方式：


- 通过电缆，通常与 Trezor Safe 3 或 Ledger Nano S Plus 等入门级型号一起使用；
- 在 Air-Gap 模式下，即在没有直接有线连接的情况下，通过 MicroSD 卡或 QR 码 Exchange。

Sparrow 支持所有这些通信方式，并与市场上大多数硬件钱包兼容。

在本教程中，我将使用带电缆的 Ledger Nano S，但在气隙模式下操作步骤类似。有关 Hardware Wallet 的具体细节，请参阅 Plan ₿ Network 的专门教程。

开始之前，请确保 Hardware Wallet 上已经配置了 Wallet。如果使用有线连接，请通过电缆将其连接到电脑。

要将所谓的 "*Keystore*"（管理投资组合所需的公共信息）导入 Sparrow Wallet，请点击 "*File*"标签，然后点击 "*New Wallet*"。

![Image](assets/fr/32.webp)

为您的投资组合命名，然后点击 "*创建 Wallet*"。我建议您输入 Hardware Wallet 的名称，以便日后识别。

![Image](assets/fr/33.webp)

在 Interface 顶部，选择 "*单签名*"或 "*多签名*"组合。在我们的示例中，我们将配置单签名组合。

请在下面选择锁定UTXO 的脚本类型。如果您的 Hardware Wallet 支持，我建议您选择 "*Taproot (P2TR)*"。

![Image](assets/fr/34.webp)

接下来，连接方法不同，步骤也不同。如果使用 Air-Gap 方法，请选择 "*Airgapped Hardware Wallet*"。然后按照设备的具体说明进行操作。

![Image](assets/fr/35.webp)

如果像我一样使用电缆连接，请选择 "*连接 Hardware Wallet*"。

![Image](assets/fr/36.webp)

点击 "*扫描*"，让 Sparrow 检测你的设备。确保设备已插入并解锁。对于某些型号的设备，如 Ledger，您需要打开 "*Bitcoin*"应用程序以启用检测。

![Image](assets/fr/37.webp)

选择 "*导入密钥存储*"。

![Image](assets/fr/38.webp)

点击 "*应用*"，完成组合创建。

![Image](assets/fr/39.webp)

设置一个强大的密码，以确保对 Sparrow Wallet 的访问安全。该密码将保护您的公钥、地址和交易历史。我们建议您将其保存在密码管理器中。请注意，该密码不参与密钥的生成。即使没有该密码，您也可以通过任何兼容 BIP39 的软件恢复对 Mnemonic 的访问。

![Image](assets/fr/40.webp)

您的管理组合已在 Sparrow 上配置完毕。

![Image](assets/fr/41.webp)

## 接收比特币

现在您的 Wallet 已经在麻雀上设置好了，您可以接收比特币了。只需进入 "*接收*"菜单即可。

![Image](assets/fr/42.webp)

麻雀将在您的 Wallet 中显示第一个未使用的 Address。您可以为这个 Address 添加一个 "*标签*"，以便将来提醒您这些卫星的来源。

![Image](assets/fr/43.webp)

如果您使用的是 Hot Wallet，则可以通过复制或扫描相关二维码立即使用显示的 Address。

如果您使用的是 Hardware Wallet，请务必在使用前检查设备屏幕上的 Address。对于有线设备，连接并解锁 Hardware Wallet，然后在 Sparrow 中点击 "*显示 Address*"。确保 Hardware Wallet 上显示的 Address 与 Sparrow 上显示的一致。

![Image](assets/fr/44.webp)

对于 Hardware Wallet Air-Gap 用户，Address 验证因设备型号而异。有关精确说明，请参阅专门的 Plan ₿ Network 教程。

一旦付款人广播了交易，您就会看到它出现在 "*交易*"选项卡中。您可以点击查看更多详细信息，如 txid。

![Image](assets/fr/45.webp)

在 "*地址*"选项卡中，你会看到所有收件箱地址的列表。您可以查看这些地址是否已被使用，以及是否已添加标签。 *接收*"地址是 Sparrow 在你点击 "*接收*"时显示的地址，用于接收付款。更改*"地址用于交易中的 Exchange，即收回输入中未使用的 UTXO 部分。

![Image](assets/fr/46.webp)

在 "*UTXOs*"（UTXOs*）选项卡中，您可以看到所有的UTXOs，即您持有的Bitcoin碎片。您可以看到每个 UTXO 的数量和相关标签。

![Image](assets/fr/47.webp)

## 发送比特币

现在您的 Wallet 中已经有了一些卫星币，您也可以选择发送一些。虽然有几种方法可以做到这一点，但我建议您使用 "*UTXOs*"菜单，以便更精确地控制您花费的硬币（*硬币控制*），而不是直接进入 "*发送*"菜单（尽管如果您是初学者，后者可能就足够了）。

![Image](assets/fr/48.webp)

选择您希望作为该交易输入的UTXOs，然后点击 "*发送所选*"。通过这种方法，您可以根据支出情况和收到UTXOs 时的标签，从UTXOs 中选择最合适的来源，以优化付款的保密性。请确保所选 UTXO 的总和大于您希望发送的金额。

![Image](assets/fr/49.webp)

在 "*付款至*"字段中输入收件人的 Address。您也可以点击摄像头图标，用网络摄像头扫描 Address。通过 "*+添加*"按钮，您可以在一次交易中支付多个地址。

![Image](assets/fr/50.webp)

为您的交易添加一个标签，以提醒您交易的目的。该标签也将与您的最终 Exchange 相关联。

![Image](assets/fr/51.webp)

输入要发送到此 Address 的金额。

![Image](assets/fr/52.webp)

根据当前市场条件调整收费率。您可以通过输入绝对收费值或使用滑块调整收费率来做到这一点。

![Image](assets/fr/53.webp)

在 Interface 的底部，您可以选择 "*效率*"和 "*隐私*"。就我而言，"*隐私*"选项不可用，因为我的投资组合中只有一个 UTXO。"*Efficiency*" 相当于传统交易，而 "*Privacy*"则是石墙型交易，这种交易结构通过模拟小型 CoinJoin 来加强保密性，从而使链式分析更加复杂。

![Image](assets/fr/54.webp)

Sparrow 会显示一个摘要图，显示您的输入、输出和交易费用（注意，费用实际上不是输出，这与此图所示相反）。如果您对一切都满意，请点击 "*创建交易*"。

![Image](assets/fr/55.webp)

这将带您进入一个页面，详细介绍交易的 Elements 信息。检查所有信息是否正确，然后点击 "*最终完成交易以供签署*"。

![Image](assets/fr/56.webp)

保持 Sighash 的默认状态非常重要。要了解原因，请参阅本培训课程，我将在课程中为您讲解有关 Sighash 的所有知识：

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

在下一个屏幕中，选项会根据您使用的 Wallet 类型而有所不同：


- 对于 Hardware Wallet Air-Gap，点击 "*Show QR*"显示 PSBT，您可以用设备签署，然后使用 "*Scan QR*"将签署的 PSBT 加载到 Sparrow 中。"*保存交易*"选项的工作方式与此类似，但使用的是 microSD .NET；
- 对于 Hot Wallet，只需点击 "*签名*"并输入 Wallet 密码即可签名；
- 对于有线 Hardware Wallet，也可点击 "*签名*"将未签名的交易发送到您的设备。

![Image](assets/fr/57.webp)

在您的 Hardware Wallet 上检查收件人的 Address、发送金额和费用。如果一切无误，请继续签名。

交易签署完成后，将重新出现在 Sparrow 中，准备在 Bitcoin 网络上广播，以便随后纳入区块。如果一切正常，请点击 "*广播交易*"。

![Image](assets/fr/58.webp)

您的交易正在广播，等待确认。

![Image](assets/fr/59.webp)

## 在 Sparrow 上管理和配置投资组合

在 "*设置*"选项卡中，您可以找到有关投资组合的详细信息，例如 ：


- 投资组合类型（单项密码或 multi-sig 密码） ；
- 使用的脚本类型 ；
- 您为投资组合指定的名称 ；
- 万能钥匙印记；
- 旁路路径 ；
- 账户的扩展公开密钥。

![Image](assets/fr/60.webp)

通过 "*导出*"按钮，您可以导出投资组合信息，以便在其他软件中使用，同时保留在 Sparrow 中设置的信息。

通过 "*添加账户*"按钮，您可以为您的投资组合添加一个额外的账户。一个账户对应一组独立的收件箱地址。例如，如果您希望用一个 Mnemonic 短语将个人账户和企业账户分开，这项功能就非常有用。

通过 "*高级*"按钮可进入高级设置，如自定义 Sparrow 的 Address 搜索和更改投资组合密码。

![Image](assets/fr/61.webp)

关闭 Sparrow Wallet 时，Wallet 会自动锁定。下次打开软件时，窗口会提示您使用密码解锁 Wallet。

![Image](assets/fr/62.webp)

如果该窗口没有打开，或者您希望在 Sparrow 上打开另一个投资组合，请单击 "*文件*"选项卡并选择 "*打开 Wallet*"。

![Image](assets/fr/63.webp)

这将打开文件管理器，进入 Sparrow 存储钱包的文件夹。只需选择要打开的 Wallet，输入密码即可解锁。

![Image](assets/fr/64.webp)

在 "*设置*"下的 "*文件*"菜单中，您可以找到前几节已经介绍过的 Bitcoin 网络连接参数。您还可以调整各种参数，如使用的单位、用于换算的法定货币和信息来源。

![Image](assets/fr/65.webp)

查看*"选项卡提供自定义选项和一些有用的命令，如 "*刷新 Wallet*"，可刷新您投资组合的交易搜索。

![Image](assets/fr/66.webp)

工具*"选项卡汇集了多个高级工具，包括 .NET 和 .NET Framework：


- 通过 "*签名/验证信息*"，您可以证明拥有接收的 Address 或验证签名。
- "发送到多个地址*"提供了一种简化的 Interface 方式，可同时向多个接收地址执行交易，方便批量消费。
- 通过 "*扫私钥*"，你可以找回用简单私钥保护的比特币，并将它们转移到你的麻雀 Wallet 中。这对于那些拥有 2010 年代早期（高清钱包时代之前）比特币的人来说特别有用。
- "验证下载 "可验证下载软件的完整性和真实性，然后再将其安装到设备上。
- "*Restart In*" 允许您切换到 Testnet 或 Signet 网络上的钱包。如果您想使用没有实际价值的硬币访问测试网络，这将非常有用。

![Image](assets/fr/67.webp)

您现在已经了解了 Sparrow Wallet 软件的全部内容，它是日常管理 Bitcoin 投资组合的绝佳工具。

如果您觉得本教程有用，请在下面留下 Green 的大拇指，我将不胜感激。欢迎在您的社交网络上分享。非常感谢！

我还推荐另一篇教程，其中介绍了如何用 Sparrow Wallet 配置 Hardware Wallet COLDCARD Q：

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3