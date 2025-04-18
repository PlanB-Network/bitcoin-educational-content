---
name: 阿尔比枢纽
description: 如何轻松启动自己的闪电节点？
---
![cover](assets/cover.webp)

Alby Hub 是 Alby 最新的开源软件，这家公司也是受欢迎的 Lightning 网络扩展的开发者。Alby Hub 是一个自托管钱包，拥有最易于使用的 Lightning 节点，可从任何地方访问并集成到数十个应用中。Alby Hub 是一个用于管理 Lightning 节点的易用界面。

在本教程中，我们将探讨使用 Alby Hub 的不同方法，以及如何将其连接到 Alby Go（Alby 的移动应用程序）或 Alby 浏览器扩展。这将使您能够在移动中使用您的 sats，同时在节点管理中保持自主性。


![ALBY HUB](assets/fr/01.webp)

## 什么是艾尔比枢纽？

Alby Hub 被设定为 Alby 生态系统中的新旗舰工具。该软件使用户能够轻松管理其具有集成 Lightning 节点的自托管钱包，同时保留对其密钥的所有权（自我托管）。

Alby Hub 是一款适应性很强的工具。它既能满足初学者的需求，也能满足高级用户的需求。新手可以用它来轻松操作一个真正的 Lightning 节点，而无需处理底层的复杂问题。对于更有经验的用户，Alby Hub 可用作现有 Lightning 节点高级管理的完整界面。

根据您的需求，Alby Hub 有 4 种配置可供选择：


- 阿尔比中枢云：**

对于新手来说，第一个选项是 Alby 云选项。它允许您直接在 Alby 管理的服务器上部署 Hub，并通过您的 Alby Hub 界面进行访问。尽管 Alby 管理服务器，但您仍然对您的资金拥有主权，因为您的密钥是使用只有您知道的密码加密的。然而，为了使节点正常运行，您的密钥必须保持在 RAM 中解密状态，这意味着如果有人物理访问服务器，它们在理论上可能面临风险。对于初学者来说，这是一个有趣的折中方案，但重要的是要了解其中的风险。

这种方案的主要优势在于，您可以获得一个全天候运行的Lightning节点，而无需自己管理托管。此外，与需要自己管理通道备份的自托管方案相比，Lightning节点的备份更加简单和自动化。

Alby Cloud 是一项付费服务 [查看他们的定价](https://albyhub.com/#pricing) 了解更多详情。费用通过 Alby 发布的 Lightning 发票从您的钱包中自动扣除。这是通过 NWC 连接完成的，该连接配置您的节点以自动支付与您的订阅相关的 Alby 发票。


- 使用现有节点的 Alby Hub :**

如果您已经在 Umbrel 或 Start9 上托管了一个节点，Alby Hub 可用作高级管理界面，与 ThunderHub 或 RTL 的使用方式相同。


- 阿尔比枢纽当地：**

也可以将 Alby Hub 直接安装在您的电脑上，尽管这种选择不太实用，因为您的电脑必须始终保持开启状态才能远程访问 Lightning 节点。然而，这一替代方案可能适合您的特定需求。


- 个人服务器上的 Alby Hub：**

对于高级用户，Alby Hub 可以通过一个简单的命令部署到个人服务器上。本教程不涉及这一选项，但你可以在 [Alby 的 GitHub](https://github.com/getAlby/hub?tab=readme-ov-file#docker) 上找到专门的说明。

本教程主要介绍界面，无论选择哪种方案，界面都是一样的。我们还将介绍如何使用付费云选项部署 Alby Hub，以及如何使用盒装节点选项（Umbrel 或 Start9）部署 Alby Hub。

![ALBY HUB](assets/fr/02.webp)

要在 PC 上进行本地安装，请 [根据操作系统下载并安装软件](https://github.com/getAlby/hub/releases)，然后按照界面上的相同说明进行操作。

![ALBY HUB](assets/fr/03.webp)

## 创建 Alby 账户

第一步是创建一个 Alby 账户。虽然这不是使用 Alby Hub 的必要条件，但可以让您充分利用可用的选项，包括获取闪电地址的可能性。

访问 [艾尔比官方网站](https://getalby.com/) 并点击 "*创建账户*"按钮。

![ALBY HUB](assets/fr/04.webp)

输入昵称和电子邮件地址，然后点击 "*注册*"。该电子邮件地址将用于稍后登录您的账户。

![ALBY HUB](assets/fr/05.webp)

输入您通过电子邮件收到的验证码。

![ALBY HUB](assets/fr/06.webp)

登录在线账户后，点击 "*继续*"按钮。

![ALBY HUB](assets/fr/07.webp)

再次点击 "*继续*"。

![ALBY HUB](assets/fr/08.webp)

## 云托管选项

然后，您需要在自托管选项（将 Alby Hub 安装在您自己的设备上）和高级选项之间进行选择。我将首先解释如何使用 Pro Cloud 选项（请注意，这是一个付费选项，详细信息请参阅上一节）。

点击 "*升级*"。

![ALBY HUB](assets/fr/09.webp)

点击 "*立即订阅*"确认。

![ALBY HUB](assets/fr/10.webp)

点击 "*启动 Alby Hub*"。

![ALBY HUB](assets/fr/11.webp)

在节点创建过程中稍等片刻。

![ALBY HUB](assets/fr/12.webp)

就是这样，您的 Alby Hub 现在已配置完成。在下一部分中，我将向您展示如何在现有节点上安装 Alby Hub。如果您还没有 Lightning 节点，您可以直接跳到下一部分，在 Alby Cloud 上配置 Alby Hub。


![ALBY HUB](assets/fr/13.webp)

## 自托管选项

如果您希望将 Alby Hub 用作现有 Lightning 节点的接口，您有几种选择：将其安装在服务器上、本地安装在计算机上或通过节点盒（Umbrel 或 Start9）安装。在这些配置中使用 Alby Hub 是免费的。我们将重点讨论盒中节点选项，因为我发现服务器选项在没有物理访问权限的情况下会带来与云版本类似的风险，而在电脑上本地安装通常并不合适。

要在 Umbrel 上进行设置（Start9 的步骤相同），必须首先配置一个 LND 节点。

登录 Umbrel 界面，进入应用程序商店。

![ALBY HUB](assets/fr/14.webp)

查找 "*Alby Hub*"应用程序。

![ALBY HUB](assets/fr/15.webp)

将其安装到节点上。

![ALBY HUB](assets/fr/16.webp)

你的 Alby Hub 界面现在已经准备就绪。您可以像使用云界面一样学习本教程的其余部分，但没有付费版本的选项。此外，与云版本不同，您的密钥存储在您的节点上，而不是 Alby 的服务器上。

![ALBY HUB](assets/fr/17.webp)

## 启动阿尔比枢纽

点击 "*开始*"按钮。

![ALBY HUB](assets/fr/18.webp)

然后，Alby Hub 会提示您选择一个密码。这个密码非常重要，因为它将用于加密你的钱包。在付费云版本中，您的密钥存储在 Alby 服务器上，用只有您知道的密码进行加密，然后解密并存储在 RAM 中，以便在必要时签署交易。

因此，选择一个强密码是至关重要的。任何拥有此密码的人都可能潜在地访问您的节点。请确保还在纸张上或更好的情况下，在一块金属上制作一个或多个物理备份，以增强安全性。

仔细选择并保存密码后，点击 "*创建密码*"。

![ALBY HUB](assets/fr/19.webp)

现在您可以访问您的 "闪电 "节点了。

![ALBY HUB](assets/fr/20.webp)

首先要做的是保存您的恢复短语，您的密钥就是从中派生的。为此，请点击“设置”。如果您启用了自动备份，此短语将允许您恢复对您的钱包的访问。

![ALBY HUB](assets/fr/21.webp)

然后转到 "*备份*"选项卡。输入密码即可访问。

![ALBY HUB](assets/fr/22.webp)

然后，您就可以使用 12 个字的恢复短语了。用纸或金属制作一个或多个该短语的物理备份，并将其存放在安全的地方。

![ALBY HUB](assets/fr/23.webp)

保存短语后，选中复选框确认已保存，然后点击 "*继续*"。

![ALBY HUB](assets/fr/24.webp)

## 如何恢复对比特币的访问？

在将资金发送到您的 Alby Hub 之前，了解如何在出现问题时恢复它们以及恢复所需的信息非常重要。恢复过程会根据要恢复的资金性质和节点的托管方式而有所不同。

对于付费云用户，完整恢复您的比特币需要三个关键要素：

- 您的恢复短语；
- 访问您的 Alby 帐户，以检索自动备份。

如果缺少这两条信息中的任何一条，都将无法完全恢复您的比特币。

对于那些在自己设备上运行 Alby Hub 的人，恢复过程记录在 [此处](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account)。

如果您在现有节点上安装了 Alby Hub，您需要遵循该节点操作系统的恢复流程。例如：Umbrel 提供了一种 [选项](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md)，可以加密您的 Lightning 通道的最新状态，并通过 Tor 动态和匿名地保存。请注意，只有 Alby 的自动备份可以让您在不关闭任何通道的情况下完全恢复您的 Hub。


## 购买第一个 Lightning 频道

现在您可以按照 Alby Hub 提供的说明进行操作。点击按钮，打开您的第一个收款渠道。

![ALBY HUB](assets/fr/25.webp)

选择 "*开放频道*"。如果您不打算成为路由节点，也没有特别的需要，我建议您选择私人频道。

![ALBY HUB](assets/fr/26.webp)

Alby Hub 会生成一张发票供您付款。这笔费用包括开通通道所需的交易费，以及为您的节点开通通道的 LSP（*闪电服务提供商*）的服务费，使您可以立即收到付款。

![ALBY HUB](assets/fr/27.webp)

一旦发票付款并确认交易，您的第一个闪电通道就建立了。

![ALBY HUB](assets/fr/28.webp)

在 "*节点*"选项卡中，您可以看到您现在有现金收入，可以通过 Lightning 接收付款。

![ALBY HUB](assets/fr/29.webp)

要接收付款，请点击 "*钱包*"标签，然后点击 "*接收*"。

![ALBY HUB](assets/fr/30.webp)

输入金额，必要时添加说明，然后点击 "*创建发票*"。

![ALBY HUB](assets/fr/31.webp)

我收到了第一笔 120,000 萨特的付款。

![ALBY HUB](assets/fr/32.webp)

返回 "*钱包*"标签，即可查看钱包余额。请注意，Alby Hub 会在您首次付款时自动预留 354 个席位。此后，您每开通一个 "闪电 "通道，Alby Hub 就会自动预留相当于通道容量 1%的储备金。该储备金是一项安全措施，一旦你的同伴试图欺诈，你的节点就能收回通道资金。这就是为什么虽然我发送了 120,000 sats，但我的余额上只显示了 119,646 sats。

![ALBY HUB](assets/fr/33.webp)

## 在链上存入比特币

如果你想用外链现金进行支付，也可以自己开通一个通道。为此，您需要在钱包中存有链上比特币。

在 "*节点*"选项卡上点击 "*存款*"。

![ALBY HUB](assets/fr/34.webp)

向显示的地址发送比特币。该地址来自您之前保存的恢复短语。

![ALBY HUB](assets/fr/35.webp)

我发送了 72,000 sats。它们现在可以在 "*储蓄余额*"中看到，其中包括我在链上拥有的所有资金，而不是闪电上的资金。

![ALBY HUB](assets/fr/36.webp)

## 打开 "闪电 "通道

现在您有了链上资金，就可以开通一个新的闪电通道。建议您开设多个通道，并提供足够的金额，以确保您可以随时无限制地进行支付。大多数LSP（*闪电服务提供商*）要求至少有150,000个Sats才能为您开通通道。

在 "*节点*"选项卡中，点击 "*打开通道*"。

![ALBY HUB](assets/fr/37.webp)

选择通道大小。考虑到这是一个 "闪电 "节点，存放密钥的机器并不能提供与硬件钱包相同的安全级别，我建议您不要打开太小的通道。因此，请谨慎选择阻止的金额。

![ALBY HUB](assets/fr/38.webp)

在 "*高级选项*"菜单中，您可以选择用哪个 LSP 打开通道，或者手动输入另一个闪电节点。

![ALBY HUB](assets/fr/39.webp)

然后点击 "*打开频道*"。

![ALBY HUB](assets/fr/40.webp)

等待您的频道在链上确认。

![ALBY HUB](assets/fr/41.webp)

现在，您的新频道将出现在 "*节点*"选项卡中。

![ALBY HUB](assets/fr/42.webp)

## 节点管理

管理您的 Lightning 通道比您想象的要简单。Alby Hub 允许您在您的支出余额和链上余额之间转移 sats。这样您就可以增加发送或接收的容量。

![ALBY HUB](assets/fr/66.webp)


## 连接支出应用程序

现在，您已经有了一个可以正常工作的闪电节点，您可以每天用它来接收和消费 Sats。虽然 Alby Hub 的网页界面可以方便地管理节点，但它并不适合在移动中进行快速交易。为此，我们将使用安装在智能手机上的闪电钱包应用程序。

在本教程中，我建议您选择 Alby Go，它非常易于使用，但您也可以使用 Zeus 等其他兼容的应用程序。

![ALBY HUB](assets/fr/43.webp)

要安装 Alby Go，请进入设备的应用程序商店：


- [Android版](https://play.google.com/store/apps/details?id=com.getalby.mobile)；
- [苹果公司](https://apps.apple.com/us/app/alby-go/id6471335774)。

![ALBY HUB](assets/fr/44.webp)

安卓用户也可以通过`.apk`文件[可在 Alby 的 GitHub 上获取](https://github.com/getAlby/go/releases)安装该应用程序。

![ALBY HUB](assets/fr/45.webp)

启动应用程序后，点击 "*连接钱包*"。

![ALBY HUB](assets/fr/46.webp)

在您的 Alby Hub 中，在应用商店 (App Store) 下找到 “Alby Go” 并点击 “Connect”  
![ALBY HUB](assets/fr/47.webp)  
点击 “Connect with One-Tab Connections”。这将允许您通过 Alby Go 一键将您的 Alby Hub 链接到其他应用程序。  

![ALBY HUB](assets/fr/48.webp)  

Alby Hub 将生成一个密钥，以建立与 Alby Go 的连接。


![ALBY HUB](assets/fr/49.webp)

返回 Alby Go 应用程序，扫描二维码或粘贴秘密。

![ALBY HUB](assets/fr/50.webp)

点击 "完成*"。

![ALBY HUB](assets/fr/51.webp)

您现在可以通过智能手机远程访问由 Alby Hub 提供支持的 Lightning 节点，使您能够每天随时随地轻松发送和接收 sats。


![ALBY HUB](assets/fr/52.webp)

如有必要，您可以直接在 Alby Hub 上点击该连接，管理其权限。

![ALBY HUB](assets/fr/53.webp)

要接收卫星信号，只需点击 "*接收*"。

![ALBY HUB](assets/fr/54.webp)

点击 "*发票*"修改发票金额和说明。

![ALBY HUB](assets/fr/55.webp)

从发票中扣款，以接收 Sats。

![ALBY HUB](assets/fr/56.webp)

要发送统计信息，请点击 "*发送*"。

![ALBY HUB](assets/fr/57.webp)

扫描您要支付的发票。

![ALBY HUB](assets/fr/58.webp)

然后点击 "*支付*"。

![ALBY HUB](assets/fr/59.webp)

您的交易已确认。

![ALBY HUB](assets/fr/60.webp)

点击小箭头，您就可以访问您的交易历史记录。

![ALBY HUB](assets/fr/61.webp)

这些交易也可以在 Alby Hub 上看到。

![ALBY HUB](assets/fr/62.webp)

## 定制您的闪电地址

Alby 为您提供闪电地址选项。这样，您就可以在节点上接收付款，而无需每次都手动生成发票。默认情况下，Alby 会为你分配一个闪电地址，但你也可以自定义。登录您的 Alby 在线账户，点击右上角您的姓名，然后选择 "*设置*"。

![ALBY HUB](assets/fr/63.webp)

导航至 "*闪电地址*"菜单。

![ALBY HUB](assets/fr/64.webp)

修改地址，然后点击 "*更新您的闪电地址*"进行确认。

![ALBY HUB](assets/fr/65.webp)

请注意，您的地址一旦更改，就不再属于您。因此，请确保不再向该地址发送邮件。

就这样，你现在知道如何使用 Alby Hub 工具在自己的节点上使用 Lightning 了。如果你觉得本教程有用，请在下面点个 "赞"。请随时在您的社交网络上分享本文。非常感谢

要详细了解我们在本教程中使用的所有 "闪电 "机制，我强烈建议您了解我们关于该主题的免费培训：

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
