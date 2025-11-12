---
name: 蛋糕 Wallet
description: 关于蛋糕 Wallet 和静默支付的教程
---

![cover](assets/cover.webp)


本指南探讨[**Cake Wallet**](https://cakewallet.com/)：一个开源、非托管、注重隐私的多货币 wallet，可用于 Android、iOS、macOS、Linux 和 Windows。我们将深入探讨其 Bitcoin 特有的隐私功能，通过 **无声支付**（改进的 on-chain 隐私协议）发送/接收 Bitcoin，并了解异步交易 PayJoin v2 的实现。


## 🎉 主要功能



- [**无声支付（BIP-352）**](https://bips.dev/352/) 改进了以前的[BIP 47 支付密码](https://silentpayments.xyz/docs/comparing-proposals/bip47/) 也称为 "PayNyms"，具有可重复使用的隐身地址。当发件人使用您的 "无声支付 "地址时，他们的 wallet 将使用不同的密钥生成唯一的一次性地址，这些密钥将合并成唯一的一次性 Taproot 地址。区块链记录显示的是不相关的交易，因此无法将收到的付款联系起来。静默支付具有一系列优点，包括
    - 可重复使用的地址：每次交易无需 generate 新地址，可提供更好的用户体验并提高隐私性
    - 零成本增加：静默支付不会增加交易规模或成本。
    - 增强匿名性：外部观察者无法将交易与静默支付地址联系起来。
    - 发送方与接收方无需互动：双方无需进行任何交流即可进行交易。
    - 每笔付款都有唯一的地址：消除意外重复使用地址的风险。
    - 无需服务器：无需专用服务器即可进行静默支付。
- PayJoin v2** 通过将发送方和接收方的输入合并到单个事务中，减轻了事务图分析的难度。蛋糕 Wallet 实现了两个关键的进步：
    - 异步交易**：发送方和接收方无需同时在线即可完成私人交易。
    - 无服务器通信**：任何一方都无需运行 Payjoin 服务器，从而消除了一大技术障碍。
- Coin 控制**可在交易过程中手动选择 UTXO。这可以防止在使用多个不同来源的 UTXO 时意外连接地址。
- 支持 TOR**，允许用户通过 Tor 网络传输网络流量
- RBF**（Replace-By.Fee）可让您在发送交易后调整费用。


## 1️⃣设置您的 Wallet


Cake Wallet 提供广泛的平台支持。您可以选择 "Android"、"iOS / macOS"、"Linux "和 "Windows"。  要开始使用，请访问 https://docs.cakewallet.com/get-started/ 并选择您的操作系统。


![image](assets/en/01.webp)


安装后，设置一个 `PIN` （4 或 6 位数字）。然后您将看到


1.创建新的 Wallet（针对新用户）

2.还原 Wallet（适用于现有钱包）


![image](assets/en/02.webp)


在下一个屏幕中，您可以选择多种加密货币。选择 "Bitcoin "并点击 "下一步"，然后提供一个 "Wallet 名称 "来识别 wallet。点击 "高级设置"，会出现一系列 "隐私设置"。进行这些更改：



- Fiat API:** 选择 "仅限 Tor"（通过 Tor 发送价格请求）
- 交换：** 选择 "仅限托尔"（匿名交换流量）


默认生成 BIP-39 seed 类型，可选择更改为 Electrum seed 类型。衍生路径如下：



- Electrum：`m/0'`
- BIP-39：`m/84'/0'/0`


如果您想增加一个额外的安全层，可以设置 "passphrase"。  passphrase 的主要目的是提供额外保护，防止物理攻击。即使攻击者找到了 seed 短语，如果没有正确的 passphrase，他们也无法访问您的 wallet。换句话说，seed 短语单独代表一个 wallet，而 seed 短语加上 passphrase 会创建一个完全不同的 wallet，与原来的 wallet 没有任何联系。这一功能还可以实现受 passphrase 保护的 "秘密钱包"，并为您提供似是而非的推诿。在胁迫情况下，您可以透露 seed 短语，同时将较大的资产安全地保存在受 passphrase 保护的 wallet 中。


如果您已经在运行自己的节点，请切换 "添加新自定义节点 "并提供您的 "节点 Address"，以便在您自己的基础设施中验证事务和区块。完成后，点击 "继续 "和 "下一步 "创建 wallet。


![image](assets/en/03.webp)


在下一个屏幕上，你会看到一个免责声明：


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


要了解保存记忆短语的最佳方法，请参考本教程：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

点击 "我明白了。给我看我的 seed`，并将这些文字保存在安全的地方！然后点击 `验证 seed`，验证后点击 `打开 Wallet`。


## 2️⃣设置


在深入了解之前，让我们先看看 "主屏幕 "和 "设置"。


在主屏幕上，我们可以看到显示的不同项目：



- 汉堡包菜单 "带我们进入 "设置
- 可用余额
- 静默支付卡开始扫描发送到您的静默支付地址的交易
- 将 Payjoin 卡 "启用 "为保护隐私和节省费用的功能
- 底部是 "Wallet 概述"、"接收"、Bitcoin 和其他货币之间的 "交换"、"发送 "和 "购买 "的快捷方式。


![image](assets/en/11.webp)


点击 "汉堡菜单 "图标可打开设置菜单。让我们回顾一下选项。


![image](assets/en/05.webp)


### A - 连接与同步 🔗


在这里，我们可以重新连接 wallet、管理节点和连接到自己的节点（推荐）。静默支付扫描 "允许我们通过指定 "从块高度扫描 "或 "从日期扫描 "来自定义扫描。


![image](assets/en/06.webp)


作为一项 "Alpha "功能，还可以选择 "启用内置 Tor"，通过 Tor 网络传输流量。


### B - 无声支付设置 🔈


我们可以在主屏幕上切换 "静默支付 "卡来显示该功能。启用 "始终扫描 "后，wallet 就可以持续监控区块链，查看是否有静默支付输入。如上所述，我们可以指定扫描参数，根据需要定制扫描过程。


![image](assets/en/07.webp)


### C - 安全与备份 🗝️


为了确保 wallet 的安全，我们可以根据应用程序内的提示创建备份。这将确保我们有一份安全的私人密钥副本，以便在 wallet 丢失或被盗时找回。此外，我们还可以查看 seed 短语和私人密钥、更改 PIN 码、启用生物识别验证、签名/验证和设置 2FA，以提供额外的保护。


![image](assets/en/08.webp)


**注意**：自 2025 年 9 月起，安卓设备上的指纹生物识别身份验证必须至少使用 2 级生物识别技术，详情请参见 [此处](https://source.android.com/docs/security/features/biometric/measure#biometric-classes)。不过，这一要求将来可能会改变。


### D - 隐私设置 🔒


我们还可以使用 Tor 加密网络连接，在访问外部资源时保护我们的隐私，从而增强 wallet 的安全性。此外，我们还可以防止截图，以保护 wallet 信息的机密性；启用自动生成地址，为每次交易创建新地址；禁用买入/卖出操作，以防止未经授权的交易。此外，我们还可以 "启用 PayJoin"，这是我们稍后将讨论的另一项隐私功能。


![image](assets/en/09.webp)


### E - 其他设置 🔧


其他设置允许我们管理费用优先级，并为我们的交易设置默认费用水平。这使我们能够在考虑到当前网络利用率的情况下，控制与我们的静默支付相关的交易费用。


![image](assets/en/10.webp)


## 3️⃣使用静默支付接收₿比特币


接收 Bitcoin 有多种选项和地址类型。Segwit (P2WPKH)` *（以 bc1q.... 开始）* 是默认选项。  让我们在本例中选择 `Silent Payments`。


要接收静默支付，首先点击蛋糕 Wallet 中的 "接收 "图标。然后，输入您希望收到的金额。要指定地址类型，请再次点击屏幕上方的 "接收"，然后从选项中选择 "无声付款"。


主屏幕上将显示可重复使用的静默支付二维码和地址。不出所料，地址相当长：


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


现在，使用兼容 BIP-352 的 wallet（如 Blue Wallet）扫描该二维码并发送付款。您会看到 wallet 从您的无声地址中生成了一个唯一的目的地地址。


![image](assets/en/13.webp)


## 4️⃣使用静默支付发送₿比特币


由于 Blue Wallet 只能 "发送 "静默支付，我们将使用另一个 BIP 352 兼容型 wallet 作为接收方。此过程与普通 Bitcoin 交易相同。



- 点击主屏幕上的 "发送
- 您可以粘贴我们可重复使用的 "sp1qq... "地址，或直接在应用程序中扫描二维码。
- 选择您希望从可用余额中支出的金额
- 点击屏幕下方的 "发送 "确认交易


一旦我们输入了`sp1qq...`地址，wallet 就会在后台自动生成一个相应的`bc1p...`Taproot 地址 (P2TR)，该地址将用于静默支付。


我们可以选择使用 "Coin 控制 "功能为每笔交易编写内部说明、调整费用设置或为交易选择某些 UTXO。


![image](assets/en/14.webp)


向右轻扫以确认交易。


发送交易后，系统会询问您是否要将该联系人添加到通讯录中。


![image](assets/en/15.webp)


## 5️⃣ PayJoin


让我们回顾一下 PayJoin [关于](https://docs.cakewallet.com/cryptos/bitcoin/#payjoin)：


支付连接 v2 是 Bitcoin 中的一项保护隐私和节省费用的功能，它允许交易的发送方和接收方共同创建单笔交易。该交易的输入来自发送方和接收方**，从而打破了针对 Bitcoin 最常见的监控技术，并在某些情况下实现了更好的扩展和费用节省。


要了解有关 PayJoin 的更多信息，您还可以访问以下教程。


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

要使用 PayJoin，双方都需要一个与 PayJoin 兼容的 wallet，接收方的 wallet 中至少要有一枚硬币或输出。请按照以下步骤开始操作：


1.点击 "汉堡菜单"，然后点击 "隐私 "按钮

2.切换 "使用 Payjoin "选项

3.  点击主屏幕上的 "接收"，您将看到一个 PayJoin QR 码和复制按钮（当选择 Segwit 时）


![image](assets/en/16.webp)


## 6️⃣其他功能


还有其他一些功能，如多币种 "交换"、与不同供应商连接的 "买卖 "选项以及 "蛋糕支付 "等蛋糕特定程序，可让您购买预付卡或礼品卡。


![image](assets/en/17.webp)


## 🎯 结论


这是我们对 Cake Wallet 的评测，它具有实用的 Bitcoin 隐私功能，如静音支付（BIP-352）和 Payjoin v2。


无声支付用可重复使用的隐身地址取代一次性地址，以防止传入交易的 on-chain 链接。虽然以前版本的同步问题有了明显改善，但扫描和检测静默支付所需的计算要求有所提高，需要更多的资源和带宽。


Payjoin v2 将发送方和接收方的输入合并为单笔交易，无需额外费用或中央协调，从而打破了链式分析。这打破了常见的输入所有权启发式，这是一个重大优势，因为它意味着你不能假定所有输入都属于发送方。


对于优先考虑财务匿名性的用户来说，Cake Wallet 是一个可行的选择。它将隐私协议直接纳入其核心功能，使其无需任何复杂的技术即可访问。随着对公共区块链的监控越来越多，像这样的工具有助于在最重要的地方维护交易隐私。在 wallet 范围内更广泛地实施这些标准将是一个值得欢迎的发展。


## 资源


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/