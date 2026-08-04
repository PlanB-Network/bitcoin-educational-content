---
name: Slipstream
description: 使用 Slipstream 将已签名交易直接发送给矿工，而不广播到 Bitcoin 网络
---

![封面](assets/cover.webp)

通常，当你签署一笔交易时，它会自动广播到网络上的每个 Bitcoin 节点。然后，它会等待被挖出。

不过，只要它还没有进入区块，获得你私钥的攻击者就可能替换它并盗走资金。如果你使用的是 ColdCard 硬件钱包，这通常就是这种情况。

矿业公司 MARA 的 Slipstream 工具可以让你绕过向网络广播交易这一步：交易会被直接（并且只）发送给一名矿工，该矿工会将其保密，避免它在网络上暴露。这笔交易可能需要更长时间才会被挖出，但它会受到保护，免受替换攻击。

下面，我们提供一个教程，让 [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) 用户，以及 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) 钱包用户，可以通过 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 页面使用矿工 MARA 的 Slipstream 工具。

⚠️ **警告**：此工具只适用于某些用户类型，主要是 Liana 钱包、miniscript 钱包和某些类型的多签。Wizardsardine **明确不建议**将其用于资金已经处于严重被盗风险的钱包，例如恢复短语是在受随机数生成器漏洞影响的 ColdCard 设备上生成的钱包。在这种情况下，与攻击者的竞速以秒为单位，而发送给单个矿工的交易确认时间远长于正常广播的交易。如果这与你有关，请先阅读我们的专门教程：

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## 对于 Liana 用户

Liana 由 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 页面的发布方 Wizardsardine 维护，因此路径很直接：你只需导出已签名的 PSBT 文件，而不是广播它。

*前提条件：你的 Liana 钱包中有资金。*

### 步骤 1：用 Liana 创建你的交易

像往常一样，通过添加目标地址、描述和金额（这里是钱包中的最大可用金额）来构建你的交易。

设置手续费率：

- 点击左下角 “Coins selection” 下的小方框，选择你想要花费的币；
- 然后输入手续费率。请记得将手续费设置为远高于建议费率，如本页面所述：[outofband.wizardsardine.com](https://outofband.wizardsardine.com/)。

最后，点击 “Next”。

![在 Liana 中构建交易](assets/fr/01.webp)

### 步骤 2：检查你的交易详情

点击 “Sign” 之前，检查你的交易详情；尤其是：

- 发送金额；
- 分配给交易手续费的 satoshi 数量；
- 但最重要的是，你要把资金发送到的地址（请记得检查地址的前 5/6 个字符、后 5/6 个字符，以及地址中间的 5/6 个字符，以避免“地址投毒”攻击）。

![检查交易详情](assets/fr/02.webp)

### 步骤 3：选择签名钱包

接下来，选择你需要用来签署交易的软件钱包和/或硬件钱包。快速提醒：对于 2-of-2 多签钱包，你需要 2 个签名中的 2 个。

### 步骤 4：导出交易的 PSBT 文件

Bitcoin 交易现在已经由相应的密钥签名。不要点击 “Broadcast”，否则它会被分享给整个网络；如果你使用 ColdCard 硬件钱包，你的交易将被公开暴露，你的资金将面临风险。

现在你可以点击 “Export”，然后把 PSBT 文件保存在你的电脑本地。

![从 Liana 导出 PSBT 文件](assets/fr/03.webp)

### 步骤 5：通过 outofband.wizardsardine.com 将交易发送给矿工

现在进入最后几个步骤。要把交易发送给矿工，你只需拿起 PSBT 文件，并把它拖放到指定区域。

![把 PSBT 文件拖放到 outofband.wizardsardine.com](assets/fr/04.webp)

随后，交易会如下所示显示出来。

![队列中的交易](assets/fr/05.webp)

### 步骤 6：通过 Slipstream 发送交易

最后，你只需点击 “Send”，交易就会通过 Slipstream 发送给 MARA。

![通过 Slipstream 发送交易](assets/fr/06.webp)

几秒钟内，交易随后会从 “Sending” 变为 “Accepted”：

![Slipstream 接受的交易](assets/fr/07.webp)

剩下要做的就是复制交易标识符（TXID），然后将其粘贴到 [mempool.space](https://mempool.space/) 中，以便观察它被挖出：

![在 mempool.space 上查找 TXID](assets/fr/08.webp)

请注意：交易会显示为 “Transaction not found”，直到矿工 MARA 挖出一个区块并将你的交易包含其中。这可能需要几十分钟，甚至数小时，因为 MARA 只持有 Bitcoin 网络约 4.5% 的哈希率。截至 2026 年 8 月 4 日，这大约对应每 3 小时 45 分钟挖出一个区块。

## 对于其他钱包的用户

如果你不使用 [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04)，但仍想使用该工具，这里有一个使用 2-of-2 多签钱包的教程。为此，我们将使用 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) 软件钱包。

*前提条件：你的 Sparrow 钱包中有资金。*

### 步骤 1：创建你的交易

使用 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)，在你的多签钱包上创建交易。请记得将手续费设置为远高于建议费率，如本页面所述：[outofband.wizardsardine.com](https://outofband.wizardsardine.com/)。

创建后，点击 “Create Transaction”。

![在 Sparrow 中创建交易](assets/fr/09.webp)

### 步骤 2：完成你的交易

为了完成你的交易，你现在需要签署它。为此，点击 “Finalize Transaction for Signing”。

![完成交易以供签名](assets/fr/10.webp)

### 步骤 3：用你的不同密钥签署交易

现在到了签署交易的时候。为此，只需用你使用的软件钱包或硬件钱包签署它。

![用多签密钥签署交易](assets/fr/11.webp)

### 步骤 4：下载已签名交易，并且不要将其广播到网络

Bitcoin 交易现在已经由我们 2-of-2 多签的两个密钥签名。不要点击 “Broadcast Transaction”，否则它会被分享给整个网络；如果你使用 ColdCard 硬件钱包，你的交易将被公开暴露，你的资金将面临风险。

![已签名交易，已准备好但未广播](assets/fr/12.webp)

### 步骤 5：显示已签名交易脚本，或下载 PSBT 文件

要显示已签名的 Bitcoin 交易，现在点击 “View Final Transaction”。然后你可以复制已签名的 Bitcoin 交易脚本：

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![显示已签名交易脚本](assets/fr/13.webp)

如果你想下载交易文件，你可以：

- 点击 “File”，然后点击 “Save transaction…”；
- 或点击右下角的网络连接按钮（黄色按钮），然后点击 “Save Final Transaction”。

随后，交易会保存在你的电脑本地。

![在本地保存最终交易](assets/fr/14.webp)

### 步骤 6：通过 outofband.wizardsardine.com 将交易发送给矿工

现在进入最后几个步骤。要把交易发送给矿工，你只需：

- 前往 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)；
- 粘贴上一步复制的已签名交易脚本，然后点击下方的 “ADD TO QUEUE”；

![将交易脚本粘贴到工具中](assets/fr/15.webp)

- 或拿起文件，并把它拖放到指定区域。

![把交易文件拖放到工具中](assets/fr/16.webp)

随后，交易会如下所示显示出来。

![队列中的交易](assets/fr/17.webp)

如果有消息告诉你，交易中输入的 satoshi 总金额未知（因此无法计算手续费的 satoshi 数量），你只需手动输入 satoshi 输入总金额。要找到它，只需在 Sparrow 中点击你的交易显示，也就是图表中间的位置：

![Sparrow 中显示的输入总金额](assets/fr/18.webp)

然后将该金额（在我们的示例中为 15,904 sats）输入 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 工具：

![手动输入总输入金额](assets/fr/19.webp)

最后，检查手续费率是否正确。

### 步骤 7：通过 Slipstream 发送交易

最后，你只需点击 “Send”，交易就会通过 Slipstream 发送给 MARA。

![通过 Slipstream 发送交易](assets/fr/20.webp)

几秒钟内，交易随后会从 “Sending” 变为 “Accepted”：

![Slipstream 接受的交易](assets/fr/21.webp)

剩下要做的就是复制交易标识符（TXID），然后将其粘贴到 [mempool.space](https://mempool.space/) 中，以便观察它被挖出：

![在 mempool.space 上查找 TXID](assets/fr/22.webp)

请注意：交易会显示为 “Transaction not found”，直到矿工 MARA 挖出一个区块并将你的交易包含其中。这可能需要几十分钟，甚至数小时，因为 MARA 只持有 Bitcoin 网络约 4.5% 的哈希率。截至 2026 年 8 月 4 日，这大约对应每 3 小时 45 分钟挖出一个区块。
