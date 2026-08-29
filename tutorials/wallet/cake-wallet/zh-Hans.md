---
name: Cake Wallet
description: 关于 Cake Wallet 和静默支付的教程
---

![cover](assets/cover.webp)


本指南将深入探讨 Cake Wallet（https://cakewallet.com/）：一款开源、非托管、注重隐私的多币种钱包，支持 Android、iOS、macOS、Linux 和 Windows 系统。我们将详细介绍其针对比特币的隐私功能，演示如何通过“静默支付”（一种改进的链上隐私协议）发送/接收比特币，并了解 PayJoin v2 在异步交易中的实现。


## 🎉 主要功能



- [**静默支付（BIP-352）**](https://bips.dev/352/) 改进了以前的[BIP 47 支付代码](https://silentpayments.xyz/docs/comparing-proposals/bip47/) 也称为 "PayNyms"，具有可重用的隐身地址（stealth address）。当发送者使用您的 "静默支付" 地址时，他们的钱包将使用不同的密钥生成独特的一次性地址，这些密钥将合并成独特的一次性 Taproot 地址。区块链记录显示的是不相关的交易，因此无法将收到的付款联系起来。静默支付具有一系列优点，包括：
    - 可重用的地址：每次交易无需生成新地址，可提供更好的用户体验并提高隐私性
    - 零额外成本：静默支付不会增加交易规模或成本。
    - 增强匿名性：外部观察者无法将交易与静默支付地址联系起来。
    - 发送者与接收者无需互动：双方无需进行任何交流即可进行交易。
    - 每笔付款都有独特的地址：消除意外重用地址的风险。
    - 无需服务器：无需专用服务器即可进行静默支付。
- **PayJoin v2** 通过将发送方和接收方的输入合并到单个交易中，减轻了交易图分析的难度。Cake Wallet 实现了两个关键的进步：
    - **异步交易**：发送者和接收者无需同时在线即可完成私人交易。
    - **无服务器通信**：任何一方都无需运行 Payjoin 服务器，从而消除了一大技术障碍。
- **币控制**允许用户在交易过程中手动选择 UTXO。这可以防止在使用多个不同来源的 UTXO 时意外连接地址。
- **支持 TOR**，允许用户通过 Tor 网络传输网络流量
- **RBF**（手续费替换）可让您在发送交易后调整费用。


## 1️⃣ 设置您的钱包


Cake Wallet 提供广泛的平台支持。您可以选择 `Android`, `iOS / macOS` , `Linux` 或 `Windows`。 开始使用时，请访问 https://docs.cakewallet.com/get-started/ 并选择您的操作系统。


![image](assets/en/01.webp)


安装后，设置一个 `PIN` （4 或 6 位数字）。然后您将看到：


1.`Create a New Wallet`（针对新用户）

2.`Restore Wallet`（适用于现有钱包）


![image](assets/en/02.webp)


在下一个屏幕中，您可以选择多种加密货币。选择 `Bitcoin` 并点击 `Next`，然后提供一个 `Wallet name` 来识别出钱包。点击 `Advanced Settings`，会出现一系列 `Privacy Stettings`。进行这些更改：



- **Fiat API:** 选择 `Tor Only`（通过 Tor 发送价格请求）
- **Swap:** 选择 `Tor Only`（匿名交换流量）


默认生成 BIP-39 种子类型，可选择更改为 Electrum 种子类型。派生路径如下：



- Electrum：`m/0'`
- BIP-39：`m/84'/0'/0`


如果您想增加一个额外的安全层，可以设置 `passphrase`（密语）。密语的主要目的是提供额外保护，防止物理攻击。即使攻击者找到了助记词，如果没有正确的密语，他们也无法访问您的钱包。换句话说，单独的助记词代表一个钱包，而助记词加上密语则创建了一个与原始钱包完全不同的新钱包。此功能还支持使用密语保护的 “秘密钱包”，并赋予您一定的否认能力。在受到胁迫的情况下，您可以透露助记词，同时将更多资产安全地保存在受密语保护的钱包中。


如果您已经在运行自己的节点，请切换 `Add New Custom Node` 并输入您的 `Node Address`，以便在您自己的基础设施中验证事务和区块。完成后，点击 `Continue` 和 `Next` 以创建您的钱包。


![image](assets/en/03.webp)


在下一个屏幕上，您会看到一个免责声明：


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```

翻译：
下一页您将看到一串单词。这是您独一无二的私人助记词，也是钱包丢失或出现故障时恢复钱包的唯一方法。您有责任将其记录下来，并妥善保管在 Cake Wallet 应用之外的安全地方。


![image](assets/en/04.webp)


如果您想要了解保存助记词的最佳方法，请参考本教程：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

点击 `I understand. Show me my seed`，并将这些助记词写下和保存在安全的地方！然后点击 `Verify seed`，验证后点击 `Open Wallet`。


## 2️⃣ 设置


在深入了解之前，让我们先看看 `Home Screen` 和 `Settings`。


在主屏幕上，我们可以看到系统显示的不同项目：



- “汉堡包选单”（Hamburger Menu）将带我们进入 "设置“ Settings）
- 可用余额（Available Balance）
- 静默支付卡（Silent Payments Card），以扫描发送到您的静默支付地址的交易
- 将 Payjoin 卡（Payjoin card）设为 "启用"，为保护隐私和节省费用的功能
- 底部是 "钱包概述"（Wallet Overview）、"接收"（Receive）、比特币和其他货币之间的 "交换"（Swap）、"发送"（Send）和 "购买"（Buy）的快捷方式。


![image](assets/en/11.webp)


点击 "汉堡包选单" 图标可打开设置选单。让我们回顾一下选项。


![image](assets/en/05.webp)


### A - 连接与同步 🔗


在此处，我们可以重新连接钱包、管理节点和连接到自己的节点（推荐）。`Silent Payments Scanning`（静默支付扫描）允许我们通过指定 `Scan from block height`（聪特定的区块高度扫描）或 `Scan from date`（聪特定的日期扫描）来自定义扫描时间范围。


![image](assets/en/06.webp)


作为一项 `Alpha` 功能，还有 `Enable built-in Tor` 选项，通过 Tor 网络传输流量。


### B - 静默支付设置 🔈（Silent Payments settings）


我们可以在主屏幕上切换 "静默支付" 卡来显示该功能。启用 `Always scanning` 后，钱包就可以持续监控区块链，查看是否有静默支付输入。如上所述，我们可以指定扫描参数，根据需要定制扫描过程。


![image](assets/en/07.webp)


### C - 安全与备份（Security & backup） 🗝️


为了确保钱包的安全，我们可以根据应用程序内的提示创建备份。这将确保我们有一份安全的私人密钥副本，以便在钱包丢失或被盗时找回。此外，我们还可以查看助记词和私钥、更改 PIN 码、启用生物识别验证、签名/验证和设置 2FA，以提供额外的保护。


![image](assets/en/08.webp)


**注意**：自 2025 年 9 月起，安卓设备上的指纹生物识别身份验证必须至少使用 2 级生物识别技术，详情请参见[此网址](https://source.android.com/docs/security/features/biometric/measure#biometric-classes)。不过，这一要求将来可能会改变。


### D - 隐私设置（Privacy Settings）🔒


我们还可以使用 Tor 加密互联网连接，从而增强钱包的安全性，并在访问外部资源时保护隐私。此外，我们可以阻止屏幕截图以保护钱包信息的机密性，启用自动生成地址功能，为每笔交易创建新地址，并禁用买卖操作以防止未经授权的交易。此外，我们还可以启用 PayJoin 功能，这是我们稍后将介绍的另一项隐私功能。

![image](assets/en/09.webp)


### E - 其他设置（Other Settings）🔧


其他设置允许我们管理费用优先级，并为我们的交易设置默认费用水平。这使我们能够在考虑到当前网络利用率的情况下，控制与我们的静默支付相关的交易费用。


![image](assets/en/10.webp)


## 3️⃣ 使用静默支付接收比特币


接收比特币有多种选项和地址类型。`Segwit (P2WPKH)` *（以 bc1q.... 为开头）* 是默认选项。让我们在本例中选择 `Silent Payments`。


要接收静默支付，首先点击 Cake Wallet 中的 “接收” 图标。然后，输入您希望收到的金额。为了指定地址类型，请再次点击屏幕上方的 `Receive`，然后从选项中选择 `Silent Payments`。


主屏幕上将显示可重用的静默支付二维码和地址。不出所料，地址相当长：


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


现在，使用兼容 BIP-352 的钱包（如 Blue Wallet）扫描该二维码并发送付款。您会看到钱包从您的静默地址中生成了一个独特的目的地地址。


![image](assets/en/13.webp)


## 4️⃣ 使用静默支付发送比特币


由于 Blue Wallet 只能发送静默支付，我们将使用另一个 BIP 352 兼容型钱包作为接收者。此过程与普通比特币交易相同。



- 点击主屏幕上的 `Send`
- 您可以粘贴我们可重用的 `sp1qq...` 地址，或直接在应用程序中扫描二维码。
- 选择您希望从可用余额中支出的金额
- 点击屏幕下方的 `Send` 按钮以确认交易


一旦我们输入了 `sp1qq...` 地址，钱包就会在后台自动生成一个相应的 `bc1p...` Taproot 地址 (P2TR)，该地址将用于静默支付。


我们可以选择使用 `Coin Control`（币控制）功能为每笔交易编写内部说明、调整费用设置或为交易选择某些 UTXO。


![image](assets/en/14.webp)


向右滑动以确认交易。


发送交易后，系统会询问您是否要将该联系人添加到通讯录中。


![image](assets/en/15.webp)


## 5️⃣ PayJoin


让我们回顾一下 PayJoin [的定义](https://docs.cakewallet.com/cryptos/bitcoin/#payjoin)：


Payjoin v2 是比特币中一项保护隐私并节省手续费的功能，它允许交易的发送者和接收者共同协作，创建一笔单一的交易。这笔交易包含了发送方和接收方的输入，从而突破了针对比特币最常见的监控手段，并在某些情况下实现了更好的可扩展性和更低的手续费。

如果您想要了解关于 PayJoin 的更多信息，您还可以访问以下教程：


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

要使用 PayJoin，交易双方都需要拥有支持 PayJoin 的钱包，并且接收者的钱包中至少需要有一种币种或输出。请按照以下步骤操作：

1. 点击汉堡选单，然后点击 `Privacy` 按钮

2. 切换 `Use Payjoin` 选项

3.  击主屏幕上的 `Receive`，您将看到一个 PayJoin 二维码和复制按钮（如果您选择了 Segwit）


![image](assets/en/16.webp)


## 6️⃣ 其他功能


还有其他一些功能，例如多币种 “交换”、与不同供应商连接的 “买卖” 选项，以及 Cake 特有的程序，例如 “Cake Pay”，它允许您购买预付卡或礼品卡。

![image](assets/en/17.webp)


## 🎯 结论


这是我们对 Cake Wallet 的评测，它具有实用的比特币隐私功能，如静默支付（BIP-352）和 Payjoin v2。


静默支付用可重用的隐身地址取代一次性地址，以防止传入交易的链上链接。虽然以前版本的同步问题有了明显改善，但扫描和检测静默支付所需的计算要求有所提高，需要更多的资源和带宽。


Payjoin v2 将发送者和接收者的输入合并为单笔交易，无需额外费用或中央协调，从而打破了区块链分析。这打破了共同输入所有权启发式，这是一个重大优势，因为它意味着您不能假定所有输入都属于发送者。


对于优先考虑财务匿名性的用户来说，Cake Wallet 是一个可行的选择。它将隐私协议直接纳入其核心功能，使其无需任何复杂的技术即可访问。随着对公共区块链的监控日益加强，像这样的工具有助于在最关键的领域维护交易隐私。如果这些标准能在钱包领域得到更广泛的应用，那将是一个令人欣喜的发展趋势。


## 资源


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/
