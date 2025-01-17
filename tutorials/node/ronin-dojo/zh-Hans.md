---
name: RoninDojo

description: 安装和使用您的RoninDojo比特币节点。
---
***警告：** 继Samourai Wallet创始人于4月24日被捕，其服务器被查封后，RoninDojo的某些功能，如Whirlpool，已不再运行。然而，这些工具有可能在未来几周内被重新启用或以不同方式重新推出。此外，由于RoninDojo的代码托管在同样被查封的Samourai的GitLab上，目前无法远程下载代码。RoninDojo团队很可能正在努力重新发布代码。*

_我们正在密切关注此案件的发展以及与之相关工具的发展情况。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守其管辖区的法律。_

_本教程专用于安装RoninDojo v1。为了利用最新的改进和功能，我强烈推荐参考我们专门为在您的树莓派上直接安装RoninDojo v2准备的教程：_ https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

运行并使用您自己的节点是真正参与比特币网络的关键。虽然运行一个比特币节点不会为用户带来任何财务利益，但它允许他们保护自己的隐私，独立行动，并对网络的信任有控制权。

在本文中，我们将详细查看RoninDojo，这是运行您自己的比特币节点的绝佳解决方案。

### 目录：

- 什么是RoninDojo？
- 应该选择什么硬件？
- 如何安装RoninDojo？
- 如何使用RoninDojo？
- 结论

如果您不熟悉比特币节点的工作原理及其角色，我建议首先阅读此文章：比特币节点 - 第1/2部分：技术概念。

![Samourai](assets/1.webp)

## 什么是RoninDojo？

Dojo是由Samourai Wallet团队开发的一个完整比特币节点服务器。您可以自由地将其安装在任何机器上。

RoninDojo是Dojo及各种其他工具的安装助手和管理工具。RoninDojo采用Dojo的原始实现，并向其添加了许多其他工具，同时也使安装和管理变得更加容易。

他们还提供了一个“即插即用”的硬件，RoninDojo Tanto，由他们的团队组装的机器上预装了RoninDojo。Tanto是一个付费解决方案，适合那些不想自己动手的人。

RoninDojo的代码是开源的，因此也可以在您自己的硬件上安装这个解决方案。这个选项成本效益高，但需要更多的操作，这就是我们在本文中要做的。

RoninDojo是一个Dojo，因此它允许将Whirlpool CLI轻松集成到您的比特币节点中，以获得最佳的CoinJoin体验。通过Whirlpool CLI，您不仅可以让您的比特币24/7重新混合，而不需要保持您的个人电脑开机，而且还可以大大提高您的隐私。
RoninDojo整合了许多依赖于您的Dojo的其他工具，例如Boltzmann计算器，它确定交易的隐私级别，Electrum服务器用于将您不同的比特币钱包连接到您的节点，或是Mempool服务器以私密方式观察您的交易。与我在本文中向您介绍的另一种节点解决方案Umbrel相比，RoninDojo深度专注于“链上”解决方案和优化用户隐私的工具。因此，RoninDojo不允许与闪电网络进行交互。

与Umbrel相比，RoninDojo提供的工具较少，但Ronin上存在的为比特币用户准备的少数几个基本功能非常稳定。

因此，如果您不需要Umbrel服务器的所有功能，只想要一个带有少数几个基本工具如Whirlpool或Mempool的简单且稳定的节点，那么RoninDojo可能是一个不错的解决方案。

在我看来，Umbrel的开发重点大量放在了闪电网络和多功能工具上。它仍然是一个比特币节点，但目标是使其成为一个多任务的迷你服务器。相比之下，RoninDojo的开发重点更符合Samourai Wallet团队的方向，专注于比特币用户的基本工具，允许完全独立并在比特币上优化隐私管理。

请注意，设置RoninDojo节点比设置Umbrel节点稍微复杂一些。

现在我们已经对RoninDojo有了一个大致的了解，让我们看看如何一起设置这个节点。

## 如何选择硬件？

选择托管和运行RoninDojo的机器时，您有几个选项。

如前所述，最简单的选择是订购Tanto，这是一款专为此目的设计的即插即用机器。要订购您的Tanto，请访问此处：[链接](https://shop.ronindojo.io/product-category/nodes/)。

由于RoninDojo团队生产开源代码，也可以在其他机器上实施RoninDojo。您可以在此页面上找到安装向导的最新版本：[链接](https://ronindojo.io/en/downloads.html)，以及此页面上的代码的最新版本：[链接](https://code.samourai.io/ronindojo/RoninDojo)。

我个人将其安装在了一个8GB的Raspberry Pi 4上，一切工作得很完美。

但是，请注意，RoninDojo团队指出，机箱和SSD适配器经常会有问题。因此，不建议使用带有电缆的机箱为您的机器的SSD供电。相反，更推荐使用为您的主板专门设计的存储扩展卡，例如这样一款：Raspberry Pi 4存储扩展卡。

以下是设置您自己的RoninDojo节点的示例：

- 一个Raspberry Pi 4。
- 带风扇的机箱。
- 兼容的存储扩展卡。
- 电源线。
- 16GB或更大的工业级micro SD卡。
- 1TB或更大的SSD。
- RJ45以太网线，推荐使用第8类。

## 如何安装RoninDojo？

### 第1步：准备可启动的micro SD卡。

组装好您的机器后，您可以开始安装RoninDojo。首先，通过将适当的磁盘映像烧录到micro SD卡上来创建一个可启动的micro SD卡。

将您的micro SD卡插入个人电脑，然后前往官方RoninDojo网站下载RoninOS磁盘映像：https://ronindojo.io/en/downloads.html。
下载与您的硬件相对应的磁盘映像。在我的情况下，我下载了"MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ"映像：
![下载RoninOS磁盘映像](assets/2.webp)

下载映像后，使用相应的.SHA256文件验证其完整性。我将在本文中详细描述如何执行此操作：如何在Windows上验证比特币软件的完整性？

验证RoninOS完整性的具体说明也可在此页面找到：https://wiki.ronindojo.io/en/extras/verify。

要将此映像烧录到您的微型SD卡上，您可以使用如Balena Etcher之类的软件，您可以在此处下载：https://www.balena.io/etcher/。

执行此操作，选择Etcher中的映像并将其烧录到微型SD卡上：

![使用Etcher烧录磁盘映像](assets/3.webp)

操作完成后，您可以将可启动的微型SD卡插入树莓派并开启机器。

### 步骤2：配置RoninOS。

RoninOS是您的RoninDojo节点的操作系统。它是Manjaro的一个修改版，Manjaro是一个Linux发行版。启动机器并等待几分钟后，您可以开始其配置。

要远程连接到它，您需要找到RoninDojo机器的IP地址。为此，您可以例如连接到您的互联网盒的管理面板，或者您也可以下载如https://angryip.org/之类的软件来扫描您的本地网络并找到机器的IP。

找到IP后，您可以使用SSH从连接到同一本地网络的另一台计算机控制您的机器。

从运行macOS或Linux的计算机上，只需打开终端。从运行Windows的计算机上，您可以使用专门的工具如Putty或直接使用Windows PowerShell。

打开终端后，输入以下命令：

> ssh root@192.168.?.?

只需将两个问号替换为您之前找到的RoninDojo的IP。
提示：在Shell中，右键点击粘贴项目。

接下来，您将进入Manjaro控制面板。使用箭头更改下拉列表中的目标以选择正确的键盘布局。

![Manjaro键盘配置](assets/4.webp)

为您的会话选择一个用户名和密码。使用一个强密码并进行安全备份。您可以在安装期间选择使用一个弱密码，稍后可以通过将其“复制粘贴”到RoninUI中轻松更改。这将允许您在Manjaro的设置过程中使用一个非常强的密码，而不需要花费太多时间手动输入它。

![Manjaro用户名配置](assets/5.webp)

接下来，您还将被要求选择一个root密码。对于root密码，直接输入一个强密码。您将无法从RoninUI更改它。同样，记得安全备份这个root密码。

然后输入您的位置和时区。

![Manjaro时区配置](assets/6.webp)

![Manjaro位置配置](assets/7.webp)

接下来，选择一个主机名。

![Manjaro主机名配置](assets/8.webp)

最后，验证Manjaro配置信息并确认。

![验证ManjaroOS配置信息](assets/9.webp)

### 步骤3：下载RoninDojo。
RoninOS的初始配置将完成。一旦完成，如上面的截图所示，机器将重启。稍等片刻，然后输入以下命令重新连接到您的RoninDojo机器：
> ssh 用户名@192.168.?.?

只需将“用户名”替换为您之前选择的用户名，并将问号替换为您的RoninDojo的IP地址。

然后输入您的用户密码。

在终端中，它将显示如下：

![SSH连接到RoninOS](assets/10.webp)

您现在已连接到您的机器，该机器目前只安装了RoninOS。现在您需要在其上安装RoninDojo。

通过输入以下命令下载最新版本的RoninDojo：

> git clone https://code.samourai.io/ronindojo/RoninDojo

下载将会很快。在终端中，您将看到这样的内容：

![克隆RoninDojo](assets/11.webp)

等待下载完成，然后使用以下命令安装并访问RoninDojo用户界面：

> ~/RoninDojo/ronin

您将被要求输入您的用户密码：

![比特币节点密码验证](assets/12.webp)

只有在您第一次访问您的RoninDojo时才需要此命令。之后，要通过SSH访问RoninCLI，您只需输入命令[SSH 用户名@192.168.?.?]，将“用户名”替换为您的用户名并输入您节点的IP地址。系统将提示您输入用户密码。

接下来，您将看到这个精彩的动画：

![RoninCLI启动动画](assets/13.webp)

然后您将最终进入RoninDojo CLI用户界面。

### 步骤4：安装RoninDojo。

从主菜单，使用键盘上的箭头键导航到“系统”菜单。按回车键确认您的选择。

![RoninCLI导航菜单到系统](assets/14.webp)

然后进入“系统设置与安装”菜单。

![RoninCLI导航菜单到RoninDojo系统安装](assets/15.webp)

最后，使用空格键选中“系统设置”和“安装RoninDojo”，然后选择“接受”开始安装。

![RoninDojo安装确认](assets/16.webp)

让安装过程静静进行。在我的案例中，它花了大约2小时。在此过程中保持您的终端开启。

偶尔检查您的终端，因为在安装的某些阶段，您将被要求按一个键，例如这里：

![RoninDojo安装进行中](assets/17.webp)

在安装结束时，您将看到不同的容器开始启动：

![节点容器启动](assets/18.webp)

然后您的节点将重启。重新连接到RoninCLI进行下一步。

![比特币节点重启](assets/19.webp)

### 步骤5：下载工作量证明链并访问RoninUI。

安装完成后，您的节点将开始下载比特币工作量证明链。这称为初始区块下载（IBD）。根据您的互联网连接和设备，这通常需要2到14天的时间。

您可以通过访问RoninUI网络界面来跟踪链下载的进度。

要从本地网络访问它，请在浏览器的地址栏中输入以下内容：

- 直接输入您机器的IP地址（192.168.?.?）

- 或输入：ronindojo.local
请记得如果您正在使用VPN，请禁用它。
### 可能的问题

如果您无法通过浏览器连接到RoninUI，请检查应用程序是否通过SSH连接到您的节点的终端正常运行。按照以下步骤连接到主菜单：

- 输入：SSH username@192.168.?.? 替换为您的凭据。

- 输入您的用户密码。

一旦进入主菜单，请前往：

> RoninUI > 重启

如果应用程序正确重启，那么问题出在您的浏览器连接上。检查您是否正在使用VPN，并确保您与节点连接到同一网络。

如果重启产生错误，请尝试更新操作系统，然后重新安装RoninUI。更新操作系统：

> 系统 > 软件更新 > 更新操作系统

更新和重启完成后，通过SSH重新连接到您的节点并重新安装RoninUI：

> RoninUI > 重新安装

重新下载RoninUI后，尝试通过浏览器连接到RoninUI。

> 提示：如果您意外退出RoninCLI并发现自己在Manjaro终端上，只需输入命令"ronin"即可直接返回到RoninCLI的主菜单。

### 网页登录

您也可以从任何网络通过Tor登录到RoninUI的网页界面。要做到这一点，请从RoninCLI检索您的RoninUI的Tor地址：

> 凭据 > Ronin UI

检索以.onion结尾的Tor地址，然后通过在您的Tor浏览器中输入此地址来登录到Ronin UI。小心不要泄露您的各种凭据，因为它们是敏感信息。

![RoninUI网页登录界面](assets/20.webp)

登录后，系统会要求您输入用户密码。这是您通过SSH登录时使用的相同密码。

![RoninUI网页界面管理面板](assets/21.webp)

我们可以在这里看到IBD（初始区块下载）的进度。请耐心等待，您正在检索自2009年1月3日以来在比特币上进行的所有交易。

下载完整的区块链后，索引器将压缩数据库。这个操作大约需要12小时。您也可以在RoninUI的"索引器"下跟踪其进度。

完成这些后，您的RoninDojo节点将完全可用：

![索引器同步至100%功能节点](assets/22.webp)

如果您想将用户密码更改为更强的密码，您现在可以从"设置"标签页进行更改。在RoninDojo上，没有额外的安全层，所以我建议选择一个真正强大的密码并注意备份。

## 如何使用RoninDojo？

一旦链下载并压缩，您就可以开始享受您的新RoninDojo节点提供的服务了。让我们看看如何使用它们。

### 将钱包软件连接到electrs。

您新安装并同步的节点的第一个用途将是将您的交易广播到比特币网络。因此，您可能希望将您的不同钱包管理软件连接到它。

您可以使用Electrum Rust Server（electrs）来做到这一点。该应用程序通常预装在您的RoninDojo节点上。如果没有，您可以从RoninCLI界面手动安装它。

简单地前往：

> 应用程序 > 管理应用程序 > 安装Electrum服务器

要获取您的Electrum服务器的Tor地址，从RoninCLI菜单中前往：

> 凭据 > Electrs
您只需在您的钱包软件中输入.onion链接。例如，在Sparrow Wallet中，前往标签页：
> 文件 > 偏好设置 > 服务器

在服务器类型中，选择“私有Electrum”，然后在相应字段中输入您的Electrum服务器的Tor地址。最后，点击“测试连接”以测试并保存您的连接。

![Sparrow Wallet连接到electrs的界面](assets/23.webp)

### 将钱包软件连接到Samourai Dojo。

除了使用Electrs，您还可以使用Samourai Dojo将您的兼容软件钱包连接到您的RoninDojo节点。例如，Samourai Wallet提供了这个选项。

为此，只需扫描您的Dojo的连接QR码。要从RoninUI访问它，请点击“仪表盘”标签，然后在您的Dojo的框中点击“管理”按钮。然后您将能够看到您的Dojo和BTC-RPC Explorer的连接QR码。要显示它们，请点击“显示值”。

![检索连接到Dojo的QR码](assets/24.webp)

要将您的Samourai Wallet连接到您的Dojo，您需要在应用安装过程中扫描此QR码：

![从Samourai Wallet应用连接到Dojo](assets/25.webp)

### 使用您自己的Mempool Explorer。

对于比特币用户来说，explorer是一个必不可少的工具，它允许您检查比特币链上的各种信息。例如，使用Mempool，您可以实时检查其他用户应用的费用，以便相应地调整您的费用。您还可以检查您的交易的确认状态或查看一个地址的余额。

这些explorer工具可能会暴露您的隐私风险，并要求您信任第三方的数据库。当您不通过自己的节点使用这个在线工具时：

- 您有泄露有关您钱包信息的风险。

- 您信任网站管理员托管的工作量证明链。

为了避免这些风险，您可以通过Tor网络在您的节点上使用您自己的Mempool实例。通过这种解决方案，您不仅在使用服务时保护了您的隐私，而且由于您查询自己的数据库，因此不再需要信任提供商。

为此，首先从RoninCLI安装Mempool Space Visualizer：

> 应用程序 > 管理应用程序 > 安装Mempool Space Visualizer

安装完成后，检索您的Mempool链接。Tor地址将允许您从任何网络访问它。同样，我们通过RoninCLI检索此链接：

> 凭证 > Mempool

![检索Tor Mempool地址](assets/26.webp)

只需在Tor浏览器中输入您的Mempool Tor地址，即可享受基于您自己数据的Mempool实例。我建议将这个Tor地址添加到您的收藏夹中，以便更快地访问。您也可以在桌面上创建一个快捷方式。

![Mempool Space界面](assets/27.webp)

如果您还没有Tor浏览器，您可以在这里下载：https://www.torproject.org/download/

您也可以通过在智能手机上安装Tor浏览器并输入相同的地址来访问它。从任何地方，您都可以使用您自己的节点查看比特币链的状态。

### 使用Whirlpool CLI。

您的RoninDojo节点还包括WhirlpoolCLI，一个用于自动化Whirlpool混合的远程命令行界面。
当您使用Whirlpool实现进行CoinJoin时，您使用的应用程序必须保持开启状态，以执行混币和重混币操作。对于想要获得高匿名集的用户来说，这个过程可能会很繁琐，因为托管Whirlpool应用程序的设备必须始终保持开机状态。实际上，这意味着如果您想让您的UTXOs参与24/7的重混币，您将需要让您的个人电脑或手机不断开启应用程序。

解决这一限制的一个方法是在一台打算始终开机的机器上使用WhirlpoolCLI，例如比特币节点。通过这种方式，我们的UTXOs可以在不需要保持除我们的比特币节点之外的其他机器运行的情况下，实现24/7的重混币。

WhirlpoolCLI与WhirlpoolGUI一起使用，WhirlpoolGUI是一个图形界面，安装在个人电脑上，便于轻松管理Coinjoins。我将在本文中详细解释如何使用您自己的dojo设置Whirlpool CLI：[链接](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez)。

要了解更多关于Coinjoin的信息，我在这篇文章中解释了一切：[链接](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin)。

### 使用Whirlpool Stat工具。

在使用Whirlpool进行CoinJoins之后，您可能想要知道您混合的UTXOs的实际隐私级别。Whirlpool Stat工具允许您轻松做到这一点。使用这个工具，您可以计算您混合的UTXOs的预期分数和回顾分数。要了解更多关于计算这些匿名集以及它们是如何工作的，我推荐阅读这一部分：[链接](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)。

该工具预装在您的RoninDojo上。目前，它仅可通过RoninCLI使用。要从主菜单启动它，请转到：

> Samourai Toolkit > Whirlpool Stat工具

使用说明将会出现。完成后，按任意键访问命令行：

![Whirlpool Stats Tool软件首页](assets/28.webp)

终端将被显示：

> wst#/tmp>

要退出此界面并返回到RoninCLI菜单，只需输入命令：

> quit

首先，我们将在Tor上设置代理，以便在完全隐私的情况下提取OXT数据。输入命令：

> socks5 127.0.0.1:9050

然后从包含您交易的池中下载数据：

> download 0001
>
> 将0001替换为您感兴趣的池面额代码。

WST上的面额代码如下：

- 0.5比特币的池：05

- 0.05比特币的池：005

- 0.01比特币的池：001

- 0.001比特币的池：0001
![从OXT的池0001下载数据](assets/29.webp)
数据下载完成后，使用以下命令加载数据：

> load 0001
>
> 将0001替换为您感兴趣的池编号代码。

![从池0001加载数据](assets/30.webp)
让加载过程进行，这可能需要几分钟。数据加载完成后，输入score命令并跟上您的TXID（交易标识符）以获取其匿名集：

> score TXID
>
> 将TXID替换为您交易的标识符。

![打印给定TXID的前瞻性和回顾性分数](assets/31.webp)

WST随后将显示回顾性分数（基于过去的指标）紧接着是前瞻性分数（基于未来的指标）。除了匿名集的分数外，WST还根据匿名集为您提供池中输出的扩散率。

请注意，您UTXO的前瞻性分数是基于您最初混合的TXID计算的，而不是您最后的混合。相反，UTXO的回顾性分数是基于最后一个周期的TXID计算的。

如果您不理解匿名集这些概念，我建议阅读我关于Coinjoin的文章的这一部分，在这里我通过图表详细解释了一切：[https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### 使用Boltzmann计算器。

Boltzmann计算器是一个工具，允许您轻松计算比特币交易的各种高级指标，包括其熵级别。所有这些数据将帮助您量化交易的隐私级别并检测任何潜在错误。这个工具预装在您的RoninDojo节点上。

要从RoninCLI访问它，请通过SSH连接，然后进入菜单：

> Samourai Toolkit > Boltzmann Calculator

在解释如何在RoninDojo上使用它之前，我将解释这些指标代表什么，它们是如何计算的，以及它们的用途。

这些指标可用于任何比特币交易，但它们对于研究Coinjoin交易的质量特别有趣。

1. 该软件计算的第一个指标是可能的组合数量。在计算器上标记为"nb combinations"。鉴于UTXOs的值，这个指标代表从输入到输出的可能映射的数量。

> 如果您不熟悉"UTXO"这个术语，我建议阅读这篇简短的文章：比特币交易的机制：UTXO、输入和输出。

换句话说，这个指标代表给定交易的可能解释数量。例如，一个Whirlpool 5x5 Coinjoin结构将有1496个可能的组合：

![Coinjoin交易的示意图在kycp.org上](assets/32.webp)

图片来源：KYCP
2. 第二个计算指标是交易的熵。由于交易可能的组合数量可能非常高，因此可以选择使用熵代替。熵表示可能组合数量的二进制对数。其公式如下：
- E：交易的熵。
- C：交易可能的组合数量。

> E = log2(C)

在数学中，二进制对数（底数为2）是2的幂函数的逆函数。换句话说，x的二进制对数是必须将数字2提升到的幂，以获得值x。

因此：

> E = log2(C)
> C = 2^E

此指标以比特为单位表示。例如，这是一个Whirlpool 5x5 Coinjoin交易的熵计算，之前提到的可能组合数量等于1496：

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469比特

因此，这个Coinjoin交易的熵为10.5469比特，这是非常好的。

这个指标越高，交易的不同解释就越多，因此交易就越保密。

让我们再看一个例子。这是一个有一个输入和两个输出的“经典”交易：

![比特币交易示意图在oxt.me](assets/34.webp)

图片来源：OXT

这个交易只有一种可能的解释：

> [(输入 0) > (输出 0 ; 输出 1)]

所以它的熵将等于0：

> C = 1
>
> E = log2(C)
>
> E = 0

3. Boltzmann计算器返回的第三个指标是被称为“钱包效率”的交易效率。这个指标简单地允许将输入交易与同一配置下的最佳可能交易进行比较。

我们现在将介绍最大熵的概念，它代表给定交易结构可达到的最高熵。例如，一个Whirlpool 5x5 Coinjoin结构将具有10.5469的最大熵。效率指标将这个最大熵与输入交易的实际熵进行比较。其公式如下：

- ER：实际熵，以比特表示。
- EM：具有相同结构的最大熵，以比特表示。
- Ef：以比特表示的效率。

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0比特

这个指标也以百分比表示，因此公式变为：

- CR：实际可能组合数量。
- CM：具有相同结构的最大可能组合数量。
- Ef：以百分比表示的效率。

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

效率为100%意味着这个交易相对于其结构具有最高可能的隐私性。

4. 第四个计算指标是熵密度。它允许我们将熵关联到每个输入或输出。这个指标可以用来比较不同大小交易的效率。

其计算非常简单：我们将交易的熵除以交易中存在的输入和输出的总数。例如，对于一个Whirlpool 5x5 Coinjoin，我们将有：

    ED：以比特表示的熵密度。
    E：以比特表示的交易熵。
    T：交易中输入和输出的总数。

T = 5 + 5 = 10
ED = E / TED = 10.5469 / 10
ED = 1.054 比特

Boltzmann 计算器提供的第五项信息是输入与输出之间链接的概率表。这个表格简单地给出了一个给定输入对应给定输出的概率（Boltzmann 分数）。

如果我们以 Whirlpool Coinjoin 为例，概率表将是：

| %       | 输出 0 | 输出 1 | 输出 2 | 输出 3 | 输出 4 |
|---------|--------|--------|--------|--------|--------|
| 输入 0 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 1 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 2 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 3 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 4 | 34%    | 34%    | 34%    | 34%    | 34%    |

在这里我们可以看到，每个输入与每个输出被链接的概率是相等的。

然而，如果我们以一个输入和两个输出的交易为例，它看起来会是这样：

| 输入 | 输出 0 | 输出 1 |
| ---- | ------ | ------ |
| 0    | 100%   | 100%   |

在这个例子中，我们可以看到每个输出来自输入 0 的概率是 100%。

这个概率越低，保密性水平越高。

6. 计算的第六项信息是确定性链接的数量。也会提供确定性链接的比率。这个指标突出显示了给定交易中输入与输出之间有 100% 概率的链接数量，意味着它们是不可否认的。

比率指的是交易中确定性链接的数量与链接总数的比例。

例如，一个 Coinjoin Whirlpool 交易在输入和输出之间没有确定性链接。指标将是零，比率也是 0%。

然而，对于研究的第二笔交易（1个输入和2个输出），指标是 2，比率是 100%。

因此，如果这个指标是零，它表示良好的保密性。

现在我们已经研究了这些指标，让我们看看如何使用这个软件来计算它们。从 RoninCLI，进入菜单：

> Samourai Toolkit > Boltzmann Calculator

![Boltzmann Calculator 软件主页](assets/35.webp)

一旦软件启动，输入你想研究的交易 ID。你可以一次输入多个交易，用逗号分隔，然后按回车：

![在 Boltzmann Calculator 上输入要研究的 TXID](assets/36.webp)

计算器随后将返回我们之前看到的所有指标：

![为此 TXID 打印的 Boltzmann Calculator 数据](assets/37.webp)

输入命令 "Quit" 退出软件并返回到 RoninCLI 菜单。

要了解更多关于 Boltzmann 计算器的信息，我推荐阅读这些文章：

- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
### 连接Bisq
Bisq是一个点对点交易平台，允许您买卖比特币。它使用运行在Tor上的桌面软件，使您能够在不需要提供身份信息的情况下交换比特币。
Bisq通过2/2多签名系统确保点对点交易的安全。您可以将此软件与您自己的RoninDojo节点一起使用，以优化交易的隐私性并信任来自您自己节点区块链的数据。

下载Bisq软件，请访问官方网站：https://bisq.network/

开始使用该软件，我推荐阅读此页面：https://bisq.network/getting-started/

要从您的RoninDojo检索连接链接，您需要通过SSH连接到RoninCLI。然后进入菜单：

> 应用程序 > 管理应用程序

输入您的密码，然后用空格键勾选：

> [ ] 启用Bisq连接

确认您的选择。让您的节点安装，然后从以下位置检索Tor V3地址：

> 凭证 > Bitcoind

复制“比特币守护进程”下的地址。

您也可以通过在“仪表板”上的“比特币核心”框中简单点击“管理”，从RoninUI界面检索您的Bitcoind Tor V3地址：

![在RoninUI上检索TorV3比特币守护进程地址](assets/38.webp)

要从Bisq连接您的节点，请进入菜单：

> 设置 > 网络信息

![从Bisq软件访问节点连接界面](assets/39.webp)

点击“使用自定义比特币核心节点”的气泡。然后在指定框中输入您的比特币TorV3地址，带有“.onion”但不带“http://”。

![在Bisq软件中输入节点的TorV3地址的框](assets/40.webp)

重启Bisq软件。您的节点现在已连接到您的Bisq。

### 其他功能

您的RoninDojo节点还包括其他基本功能。您有能力扫描特定信息以确保其被考虑。

例如，有时可能您连接到RoninDojo的钱包找不到属于您的比特币。即使您确信这个钱包中有比特币，余额也是0。需要考虑的可能原因有很多，包括派生路径中的错误，其中也可能是您的节点没有观察您的地址。

要解决这个问题，您可以检查您的节点是否正在跟踪您的xpub，使用“xpub工具”。从RoninUI访问它，请进入菜单：

> 维护 > XPUB工具

输入有问题的xpub并点击“检查”以验证此信息。

![来自RoninUI的XPUB工具](assets/41.webp)

如果您的xpub被节点跟踪，您将看到这样的显示：

![显示成功分析的XPUB工具结果](assets/42.webp)

检查所有交易是否正确显示。同时，验证派生类型是否与您的钱包匹配。这里我们可以看到，节点将此xpub解释为BIP44派生。如果这种派生类型与您的钱包不匹配，请点击“重新输入”按钮，然后根据您的选择选择BIP44/BIP49/BIP84：

![从RoninUI更改所研究xpub的派生类型](assets/43.webp)

如果您的xpub未被您的节点跟踪，您将看到此屏幕邀请您导入它：
![使用RoninUI上的XPUB工具导入xpub](assets/44.webp)
您还可以使用其他维护工具：

- 交易工具：允许您查看特定交易的详细信息。
- 地址工具：允许您验证特定地址是否被您的Dojo跟踪。
- 重新扫描区块：强制您的节点重新扫描选定范围的区块。

您还会在RoninUI上找到“Push Tx”工具。它允许您将签名的交易广播到比特币网络。必须以十六进制格式输入：

![从RoninUI广播签名交易的工具](assets/45.webp)

## 结论。

我们已经看到了如何安装并开始使用这个奇妙的工具，即RoninDojo。它是运行自己的比特币节点的绝佳选择。它是一个稳定的解决方案，集成并保持所有比特币用户所需的基本工具的最新状态。

如果使用终端不让您感到害怕，并且如果您不需要与闪电网络相关的工具，那么RoninDojo可能会吸引您。

如果可以，请考虑向自由生产这些开源软件的开发者捐赠：https://donate.ronindojo.io/

要了解更多关于RoninDojo的信息，我推荐查看下面我的外部资源中的链接。

### 进一步阅读：

- 理解并使用比特币上的CoinJoin。
- 哈希函数 - 摘自电子书《Bitcoin Démocratisé 1》。
- 关于比特币密码短语需要知道的一切。

### 外部资源：

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/介绍boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/
