---
name: RoninDojo v2
description: 在树莓派上安装您的RoninDojo v2比特币节点
---
![cover RoninDojo v2](assets/cover.webp)

***警告：** 继Samourai Wallet创始人于4月24日被捕，其服务器被查封之后，RoninDojo的某些功能，如Whirlpool，已不再可用。然而，这些工具有可能在未来几周内重新启用或以不同方式重新推出。此外，由于RoninDojo的代码托管在同样被查封的Samourai的GitLab上，目前无法远程下载代码。RoninDojo团队很可能正在努力重新发布代码。*

_我们正在密切关注此案件的发展以及与之相关工具的发展情况。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守其管辖区的法律。_

---

> "*使用比特币时保护隐私。*"

在[之前的教程](https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0)中，我们已经解释了安装和使用RoninDojo v1的过程。然而，在过去的一年里，RoninDojo团队推出了他们的第二版实现，这标志着软件架构的重大转折点。事实上，他们放弃了Linux Manjaro发行版，转而采用Debian。因此，他们不再提供预配置的镜像以便在树莓派上自动安装。但仍有一种手动安装的方法。这就是我用于我自己的节点的方法，自那以后，RoninDojo v2在我的树莓派4上运行得非常好。因此，我提供了一个新的教程，关于如何在树莓派上手动安装RoninDojo v2。

## 目录：
- 什么是RoninDojo？
- 选择哪些硬件来安装RoninDojo v2？
- 如何组装树莓派4？
- 如何在树莓派4上安装RoninDojo v2？
- 如何使用您的RoninDojo v2节点？

## 什么是RoninDojo？
Dojo最初是一个基于比特币核心的完整比特币节点实现，由Samourai Wallet团队开发。这个解决方案可以安装在任何设备上。与其他核心实现不同，Dojo已经特别优化以与Samourai Wallet的Android应用环境集成。至于RoninDojo，它是一个旨在简化Dojo及各种其他补充工具的安装和管理的实用工具。简而言之，RoninDojo通过整合大量额外的工具，丰富了Dojo的基本实现，同时简化了其安装和管理。

Ronin还提供了一个名为“*Tanto*”的节点盒解决方案，[一个由他们的团队组装的系统上已经安装了RoninDojo的设备](https://ronindojo.io/en/products)。Tanto是一个付费选项，对于那些希望避免技术复杂性的人来说可能很有趣。但由于RoninDojo的源代码是开放的，也可以在您自己的硬件上部署它。这种替代方案更经济，但仍然需要一些额外的操作，我们将在本教程中介绍。
RoninDojo 是一个道场，因此它允许轻松集成 Whirlpool CLI 到您的比特币节点中，以提供最佳的 coinjoin 体验。有了 Whirlpool CLI，就可以实现 24 小时全天候不间断地混合您的比特币，而无需让您的个人电脑保持开机状态。

除了 Whirlpool CLI，RoninDojo 还包括多种工具来增强您的道场功能。其中，Boltzmann 计算器分析您的交易隐私级别，Electrum 服务器允许将您的比特币钱包连接到您的节点，而 Mempool 服务器则使您能够在本地查看您的交易，而不泄露信息。

与 Umbrel 等其他节点解决方案相比，RoninDojo 明确专注于链上解决方案和隐私工具。与 Umbrel 不同，RoninDojo 不支持设置 Lightning 节点，也不支持集成更通用的服务器应用程序。尽管 RoninDojo 提供的多功能工具比 Umbrel 少，但它具备管理链上活动所需的所有基本功能。

如果您不需要 Umbrel 提供的通用功能或与 Lightning Network 相关的功能，并且您正在寻找一个简单、稳定的节点，配备诸如 Whirlpool 或 Mempool 等基本工具，那么 RoninDojo 可能是理想的解决方案。虽然 Umbrel 倾向于成为一个面向 Lightning Network 和多功能性的迷你多任务服务器，但 RoninDojo 依照 Samourai Wallet 的理念，专注于用户隐私的基本工具。

现在我们已经概述了 RoninDojo，让我们一起看看如何设置这个节点。

## 为安装 RoninDojo v2 选择什么硬件？
RoninDojo 提供了一个用于在 [RockPro64](https://ronindojo.io/en/download) 上自动安装其软件的镜像。然而，我们的教程重点介绍在 Raspberry Pi 4 上的手动安装程序。尽管最近推出了 Raspberry Pi 5，而且这个教程理论上应该与这个新型号兼容，但我还没有机会亲自测试它，也没有从社区得到任何反馈。一旦我获得 Pi 5 和兼容的组件，我将更新这个教程以保持您的信息更新。与此同时，我建议优先选择 Pi 4，因为它完美地适用于我的节点。
就我个人而言，我在配备 8 GB RAM 的 Raspberry Pi 上运行 RoninDojo。尽管一些社区成员已经成功地在只有 4 GB RAM 的设备上运行它，但我自己没有测试过这种配置。考虑到价格差异不大，选择 8 GB RAM 版本似乎是明智的。如果您计划将来将您的 Raspberry Pi 用于其他用途，这也可能证明是有用的。
需要注意的是，RoninDojo 团队报告了与机箱和 SSD 适配器相关的频繁问题。我自己也遇到了这些问题。**因此，强烈建议避免为您的节点的 SSD 使用配备 USB 线的机箱。**相反，应该选择专为您的 Raspberry Pi 设计的存储扩展卡：

![存储扩展卡 RPI4](assets/notext/1.webp)
为了存储比特币区块链，您需要一个与您选择的存储扩展卡兼容的SSD。目前（2024年2月），我们正处于过渡阶段。预计在几个月内，1 TB的硬盘将不再足以容纳不断增长的区块链大小，尤其是考虑到您计划集成到节点中的各种应用。因此，有些人建议投资2 TB的SSD，以便长期内心安宁。然而，随着SSD价格年复一年的下降趋势，其他人建议选择1 TB的硬盘，这应该足够使用一到两年，并认为到它变得过时时，2 TB型号的成本可能已经降低。因此，选择取决于您的个人偏好。如果您计划长期保留您的RoninDojo，并希望在未来几年避免任何技术操作，选择2 TB的SSD似乎是最谨慎的，因为它为您提供了未来的舒适余地。
此外，您还需要各种小组件：
- 一个带风扇的外壳，用于容纳您的Raspberry Pi和您的存储扩展卡。包括SSD扩展卡和兼容外壳的套件可在线购买；
- 一个给您的Raspberry Pi的电源线；
- 至少16 GB的micro SD卡（尽管技术上8 GB就足够了，但8 GB和16 GB卡之间的价格差异通常可以忽略不计）；
- 一个RJ45以太网线缆，用于网络连接。

![节点材料](assets/notext/2.webp)

## 如何组装Raspberry Pi 4？
您的节点的组装将根据所选硬件而有所不同，特别是外壳的类型。然而，遵循的步骤的总体概要在组装中通常是相似的。
首先，安装您的SSD到存储扩展卡上，注意在后面固定两个锁定螺丝。

![组装1](assets/notext/3.webp)

然后，将您的Raspberry Pi附加到扩展卡上。

![组装2](assets/notext/4.webp)

同时，将风扇附加到Raspberry Pi上。

![组装3](assets/notext/5.webp)

连接各种组件，注意使用正确的引脚，参考您的外壳手册。外壳制造商通常提供视频教程来帮助您进行组装。在我的情况下，我有一个带有开/关按钮的额外扩展卡。这对于制作比特币节点并不是必需的。我主要使用它是为了有一个电源按钮。

如果，像我一样，您有一个带有开/关按钮的扩展卡，不要忘记安装小型的“自动开机”跳线。这将允许您的节点一旦通电就自动启动。这个功能在停电事件中特别有用，因为它允许您的节点自己重新启动，无需您的手动干预。

![组装4](assets/notext/6.webp)

在将所有硬件插入外壳之前，重要的是通过通电来检查您的Raspberry Pi、存储扩展卡和风扇的正常工作。

![组装5](assets/notext/7.webp)
最后，将您的树莓派安装在其外壳中。请注意，稍后的步骤将需要将micro SD卡插入树莓派上的适当端口。如果您的外壳配有一个开口，允许您在不打开外壳的情况下插入SD卡（就像照片中展示的我的那样），您现在可以继续关闭外壳。然而，如果您的外壳没有直接访问micro SD端口的通道，您将需要等到准备好micro SD卡后再插入它，然后完成组装。

![assembly6](assets/notext/8.webp)

## 如何在树莓派4上安装RoninDojo v2？

### 步骤1：准备可启动的micro SD
组装好硬件后，下一步是安装RoninDojo。为此，我们将从您的电脑准备一个可启动的micro SD卡，通过将适当的磁盘映像烧录到它上面。
您需要使用 _**Raspberry Pi Imager**_ 软件，该软件旨在方便下载、配置和写入操作系统到用于树莓派的micro SD卡上。首先在您的个人电脑上安装这款软件：
- 对于Ubuntu/Debian：https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- 对于Windows：https://downloads.raspberrypi.org/imager/imager_latest.exe
- 对于Mac：https://downloads.raspberrypi.org/imager/imager_latest.dmg

软件安装完成后，打开它，并将您的micro SD卡插入您的个人电脑。从Raspberry Pi Imager界面，选择 `CHOOSE OS`：

![choose OS](assets/notext/9.webp)

接下来，进入 `Raspberry Pi OS (other)` 菜单：

![choose OS others](assets/notext/10.webp)

选择名为 `Raspberry Pi OS (Legacy, 64-bit) Lite` 的操作系统，大小为 `0.3 GB`：

![choose OS Legacy Lite](assets/notext/11.webp)

选择操作系统后，您将被重定向到Raspberry Pi Imager的主菜单。点击 `CHOOSE STORAGE`：

![choose storage](assets/notext/12.webp)

选择您的micro SD卡：

![choose micro sd](assets/notext/13.webp)

选择了操作系统和micro SD卡后，点击 `NEXT`：

![choose next](assets/notext/14.webp)

一个新窗口将出现。选择 `EDIT CONFIGURATION`：

![edit settings](assets/notext/15.webp)

在这个窗口中，转到 `GENERAL` 标签页并进行以下设置（这些设置对其工作非常重要）：
- 启用选项并将 `RoninDojo` 指定为主机名；
- 启用 `Set username and password`，输入 `pi` 作为用户名，选择一个密码，并记下这些信息，因为稍后将需要它们。这些凭证是临时的，之后会被删除；
- 禁用 `Configure Wi-Fi`；
- 启用 `Set locale settings` 并选择您的时区以及与您的电脑相对应的键盘类型；

![general settings](assets/notext/16.webp)

在 SERVICES 标签页中，点击 `Enable SSH` 框并选择 `Use a password for authentication`：

![services settings](assets/notext/17.webp)

同时，确保在 `OPTIONS` 标签页中，遥测被禁用：

![options settings](assets/notext/18.webp)

点击 `SAVE`：
点击`YES`以确认，开始创建可启动的micro SD卡：
![settings save](assets/notext/19.webp)
![settings yes](assets/notext/20.webp)

将会有消息通知您，micro SD卡上的所有数据将被擦除。点击`YES`以确认，开始此过程：

![overwrite micro SD](assets/notext/21.webp)

等待软件完成准备您的micro SD卡：

![writing micro SD](assets/notext/22.webp)

当显示结束过程的消息时，您可以从计算机中取出micro SD卡：

![writing micro SD completed](assets/notext/23.webp)

### 第2步：完成节点组装
现在，您可以将micro SD卡插入树莓派的适当端口。

![micro SD](assets/notext/24.webp)

然后使用以太网线将您的树莓派连接到路由器。最后，通过连接电源线并按下电源按钮（如果您的设置包括一个）来开启您的节点。

### 第3步：与节点建立SSH连接
首先，需要找到节点的IP地址。您可以选择使用如_[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ 或_[Angry IP Scanner](https://angryip.org/)_等工具，或检查您的路由器的管理界面。IP地址应该是`192.168.1.??`的形式。**对于以下所有命令，将`[IP]`替换为节点的实际IP地址**，（去掉括号）。

启动终端。

为了移除可能已与节点的IP地址关联的密钥，执行命令：
`ssh-keygen -R [IP]`。

此命令后出现的错误不严重；它仅意味着在您已知的主机列表中不存在该密钥（这相当可能）。例如，如果您的节点的IP是`192.168.1.40`，命令变为：`ssh-keygen -R 192.168.1.40`。

接下来，通过执行命令与您的节点建立SSH连接：
`ssh pi@[IP]`。
将出现有关主机真实性的消息：`The authenticity of host '[IP]' can't be established.` 这表明由于缺乏已知的公钥，无法验证您尝试连接的设备的真实性。当首次通过SSH连接到新主机时，总会出现此消息。您必须回答`yes`以将其公钥添加到您的本地目录，这将防止在将来的SSH连接到此节点时出现此警告消息。因此，键入`yes`并按`enter`以验证。
然后，系统会要求您输入密码，即之前在第1步中设置的临时密码。用`enter`确认。这样，您就通过SSH连接到了您的节点。

总结，以下是要执行的命令：
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- 输入临时密码并确认。

### 第4步：更新和准备
现在，您通过SSH会话连接到了您的节点。在终端上，命令提示应该是：`pi@RoninDojo:~ $`。首先，使用以下命令更新可用包的列表并为现有包安装更新：
`sudo apt update && sudo apt upgrade -y`
更新完成后，使用以下命令安装 *Git* 和 *Dialog*：`sudo apt install git dialog -y`

接下来，通过执行以下命令克隆 _RoninOS_ Git仓库的 `master` 分支：
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

使用以下命令运行脚本 `customize-image.sh`：
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**重要的是要让脚本无中断地运行，并耐心等待其过程结束**，这大约需要10分钟。当出现 `Setup is complete` 消息时，您可以进行下一步。

### 步骤5：启动RoninOS
使用以下命令启动RoninOS：
`sudo systemctl start ronin-setup`

使用以下命令显示日志文件的行：
`tail -f /home/ronindojo/.logs/setup.logs`

在这个阶段，**重要的是要让RoninOS启动并等待**它完成运行。这大约需要40分钟。当出现 `All RoninDojo feature installations complete!` 时，您可以进行步骤6。

### 步骤6：访问RoninUI并更改凭据
完成安装后，要通过浏览器连接到您的节点，请确保您的个人电脑与您的节点连接到同一局域网。如果您的机器上使用了VPN，请暂时禁用它。要在浏览器中访问节点界面，请在URL栏中输入：
- 直接输入您节点的IP地址，例如，`192.168.1.??`；
- 或者，输入 `ronindojo.local`。

一旦进入RoninUI首页，系统将提示您开始设置。要做到这一点，请点击 `Let's start` 按钮。

![lets start](assets/notext/25.webp)

在这个阶段，RoninUI会向您展示您的 `root` 密码。保管好它是至关重要的。您可以选择物理备份，比如纸质备份，或者保存在[密码管理器](https://planb.network/courses/secu101/4/2)中。

![root password](assets/notext/26.webp)

保存 `root` 密码后，勾选 `I have backed up Root user credentials` 并点击 `Continue` 继续。

![confirm root password](assets/notext/27.webp)

下一步涉及创建用户密码，该密码将用于访问RoninUI网页界面以及与您的节点建立SSH会话。选择一个强密码并确保安全保存。您需要在点击 `Finish` 以验证之前输入这个密码两次。至于用户名，建议保持默认选择，`ronindojo`。如果您决定更改它，请记得相应调整后续步骤中的命令。

![user credentials](assets/notext/28.webp)

完成这些操作后，等待您的节点初始化。然后您将访问RoninUI网页界面。您几乎到达了流程的尾声，只剩下一些小步骤了！
![Ronin UI](assets/notext/29.webp)

### 步骤7：移除临时凭据
在您的个人电脑上打开一个新的终端，并使用以下命令与您的节点建立SSH连接：
`SSH ronindojo@[IP]`
例如，如果您节点的IP地址是`192.168.1.40`，那么相应的命令将是：`SSH ronindojo@192.168.1.40`

如果您在上一步中更改了用户名，将默认用户名（`ronindojo`）替换为另一个，请确保在命令中使用这个新名称。例如，如果您选择的用户名是`planb`，IP地址是`192.168.1.40`，那么要输入的命令将是：
`SSH planb@192.168.1.40`
系统会要求您输入用户密码。输入密码后，按`enter`键确认。然后您将进入RoninCLI界面。使用键盘上的箭头键导航到`Exit RoninDojo`选项，并按`enter`键选择它。
![RoninCLI](assets/notext/30.webp)

此时，您将处于节点的终端上，命令提示符类似于：`ronindojo@RoninDojo:~ $`。要删除在配置可启动的微型SD卡期间创建的临时用户，请输入以下命令并按`enter`键：
`sudo deluser --remove-home pi`

系统会提示您确认用户密码。输入密码并按`enter`键确认。等待操作完成，然后使用`exit`命令离开终端。

恭喜您！您的RoninDojo v2节点现在已配置完毕并准备使用。它将开始进行IBD（*初始区块下载*），继续从创世区块下载并验证比特币区块链。这一步涉及检索自2009年1月3日以来进行的所有比特币交易，并需要一些时间。一旦区块链完全下载，索引器将继续压缩数据库。IBD的持续时间可能会有很大差异。一旦这个过程完成，您的RoninDojo节点将完全可操作。

**如果您正在从旧的RoninDojo v1节点**迁移到这个新版本，并且保持使用相同的SSD，那么您的节点应该会自动检测并重用磁盘上现有的数据，免去了再次执行IBD的必要。在这种情况下，您只需等待节点与最新的区块重新同步。

### 第8步："veth* 修复"
如果您在Raspberry Pi上遇到RoninDojo v2的一个bug，即在无故障安装后，您的节点突然通过SSH变得无法访问，但在简单重启后恢复，那么您需要执行第8步。这个常见的bug可以通过社区开发的解决方案轻松修复：即"_veth修复_"。这个小修正可以永久解决突然断线的问题。以下是如何应用它。

在您的个人电脑上打开一个新的终端，并使用以下命令与您的节点建立SSH连接：
`SSH ronindojo@[IP]`

例如，如果您节点的IP地址是`192.168.1.40`，那么相应的命令将是：
`SSH ronindojo@192.168.1.40`

系统会提示您输入用户密码。输入密码并按`enter`键确认。然后您将进入RoninCLI界面。使用键盘的箭头键导航到`Exit RoninDojo`选项，并按`enter`键选择它。
此时，您正处于节点的终端上，命令提示符类似于：`ronindojo@RoninDojo:~ $`。要应用veth*修复，请输入以下命令并按`enter`键：`sudo nano /etc/dhcpcd.conf`

再次确认您的密码并按`enter`键。

您将进入`dhcpcd.conf`文件。您需要复制以下文本，确保包括星号，并将其添加到文件底部：
`denyinterfaces veth*`

要做到这一点，请使用键盘上的向下箭头移动到文件底部，然后使用鼠标右键点击将文本粘贴到独立行上。

添加文本后，按`ctrl X`开始退出，接着按`ctrl Y`确认保存更改，并按`enter`键最终完成并返回命令提示符。为确保修改正确应用，请使用适当的命令重新打开`dhcpcd.conf`文件。

要完成修复的应用，请执行以下操作重启您的节点：
`sudo reboot now`

此时，您可以关闭终端。允许RoninDojo重启所需的时间，之后您应该能够通过浏览器的图形界面重新连接。这个过程应该会修复遇到的bug。

## 如何使用您的RoninDojo v2节点？

### 将您的钱包软件连接到Electrs
您刚安装并同步的节点的首次使用将是向比特币网络广播您的交易。您可能会想将各种钱包连接到您的节点，以便保密地广播您的交易。您可以通过Electrum Rust Server（electrs）来做到这一点。这个应用通常预装在您的RoninDojo节点上。如果没有，您可以通过RoninCLI界面手动安装它，在`Applications > Manage Applications > Install Electrum Server`。

要获取您的Electrum Server的Tor地址，从RoninUI网页界面，转到：
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
然后，您需要在您的钱包软件中输入以`.onion`结尾的`Hostname`地址，附带端口`50001`。![hostname](assets/notext/33.webp)
例如，在Sparrow Wallet中，只需转到标签页：
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### 将您的钱包软件连接到Samourai Dojo
作为使用Electrs的替代方案，Dojo允许您将兼容的软件钱包直接连接到您的RoninDojo节点。像Samourai Wallet和Sentinel这样的钱包提供了这项功能。

要建立连接，您只需扫描您的Dojo的QR码。通过RoninUI访问此QR码，导航至：
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
要将您的Samourai Wallet链接到您的Dojo，只需在应用安装期间扫描此QR码：

![Samourai Wallet connection](assets/notext/36.webp)
如果您在设置Ronin Dojo之前已经拥有了Samourai Wallet，那么在恢复您的钱包之前，有必要备份您的钱包，卸载然后重新安装Samourai Wallet应用。重新安装应用后，您将有选项连接到新的Dojo。**请小心，如果操作不正确，这个过程有丢失比特币的风险！**确保您已经将Samourai钱包的备份保存在您的文件中，并通过`设置 > 故障排除 > 密码短语`验证您的密码短语的有效性。同时，拥有恢复短语和密码短语的可读备份也很重要。为了这个操作更精确，建议跟随这个详细教程：[https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai)。

### 使用您自己的Mempool.space区块浏览器
区块浏览器将比特币区块链的原始信息转换成结构化且易于阅读的格式。使用像*Mempool.space*这样的工具，可以分析交易，搜索特定地址，甚至实时查询网络的mempool的平均费率。

然而，使用在线区块浏览器对您的隐私构成风险，并且涉及到对第三方提供的数据的信任。实际上，通过不通过您自己的节点使用这些服务，您可能无意中泄露了有关您的交易的信息，并且必须依赖网站所有者呈现的信息的准确性。
为了降低这些风险，建议通过Tor网络在您的节点上直接托管，使用您自己的*Mempool.space*实例。这个解决方案确保了您的隐私保护和数据的自主性。
首先，从RoninUI安装*Mempool Space Visualizer*。在网页界面，转到`Dashboard`标签并点击`Mempool Space`下的`Manage`：
`Dashboard > Mempool Space > Manage`
![管理mempool](assets/notext/37.webp)
然后点击`Install Mempool visualizer`按钮：
![安装mempool](assets/notext/38.webp)
确认您的用户密码：
![密码mempool](assets/notext/39.webp)
等待安装完成，然后再次点击`Manage`按钮：
![管理Mempool](assets/notext/40.webp)
您将获得一个`.onion`链接，通过Tor网络访问您自己的*Mempool.space*实例。
![Mempool链接](assets/notext/41.webp)
我建议您将这个链接保存在Tor浏览器的收藏夹中，或者将其添加到您智能手机上的Tor Browser应用中，以便从任何地方轻松且安全地访问。如果您还没有Tor浏览器，可以在这里下载：[https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### 使用Whirlpool混合您的比特币
您的RoninDojo节点还集成了_WhirlpoolCLI_，一个命令行界面，用于自动化Whirlpool coinjoins，以及_WhirlpoolGUI_，一个设计用来与_WhirlpoolCLI_交互的图形界面。
通过Whirlpool执行coinjoin需要使用的应用程序保持活跃以进行重混。对于那些希望达到高匿名集的人来说，这个条件可能是限制性的。实际上，集成了Whirlpool的应用程序的托管设备必须持续开机。这意味着要参与全天候的重混，你的电脑或智能手机必须持续开启，并且持续运行Samourai或Sparrow。解决这一限制的方法是在一台始终开机的机器上使用_WhirlpoolCLI_，例如比特币节点，允许你的硬币无间断地重混，而无需保持另一台设备开机。
一份详细的教程正在准备中，将一步步指导你通过Samourai Wallet和RoninDojo v2进行coinjoin的过程，从A到Z。

为了更深入地理解coinjoin及其在比特币上的使用，我还邀请你查阅这篇其他文章：[理解并使用比特币上的coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2)，在这里我详细介绍了你需要知道的关于这项技术的一切。
### 使用Whirlpool Stat Tool (WST)

在使用Whirlpool进行coinjoins之后，准确评估你的混合UTXOs所达到的隐私级别是有用的。为此，你可以使用Python工具*Whirlpool Stat Tool*。这个工具允许你测量你的UTXOs的前瞻性和回顾性分数，同时分析它们在池中的扩散率。

为了深入理解这些匿名集的计算机制，我推荐阅读文章：[REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)，它详细介绍了这些指标的功能。

要访问WST工具，请转到RoninCLI。为此，在你的个人电脑上打开一个终端，并使用以下命令与你的节点建立SSH连接：
`SSH ronindojo@[IP]`

例如，如果你节点的IP地址是`192.168.1.40`，合适的命令将是：
`SSH ronindojo@192.168.1.40`

如果你在第6步更改了用户名，将默认用户名（`ronindojo`）替换为另一个，请确保在命令中使用这个新名称。例如，如果你选择的用户名是`planb`，并且IP地址是`192.168.1.40`，则要输入的命令将是：
`SSH planb@192.168.1.40`

系统将要求你输入用户密码。输入它并按`enter`键验证。然后你将访问RoninCLI界面。使用键盘上的箭头键导航到`Samourai Toolkit`菜单并按`enter`键选择它：

![Samourai Toolkit](assets/notext/43.webp)

然后选择`Whirlpool Stat Tool`：

![WST](assets/notext/44.webp)

初始化WST后，工具将进行自动安装。等待此步骤。使用说明将滚动显示。安装完成后，按任意键访问WST终端：

![WST commands](assets/notext/45.webp)

将显示以下命令提示符：
`wst#/tmp>`

如果你希望退出此界面并返回到RoninCLI菜单，只需输入：
`quit`

首先，需要配置代理以使用Tor，以确保在从OXT提取数据时的保密性。输入命令：
`socks5 127.0.0.1:9050`
接下来，下载包含您交易信息的矿池数据：
`download 0001`
将`0001`替换为您感兴趣的矿池的面额代码。WST上的面额代码如下：
- 0.5比特币的矿池：`05`
- 0.05比特币的矿池：`005`
- 0.01比特币的矿池：`001`
- 0.001比特币的矿池：`0001`

下载后，通过在此命令中替换`0001`为您矿池的代码来加载数据：`load 0001`

![WST加载](assets/notext/46.webp)

等待加载完成，这可能需要几分钟时间。一旦数据加载完毕，要知道您的币的匿名集分数，请执行命令`score`，后跟您的TXID（不包括括号）：
`score [TXID]`

![WST分数](assets/notext/47.webp)

WST随后将显示回顾性分数（_向后看的指标_），接着是前瞻性分数（_向前看的指标_）。除了匿名集分数外，WST还将指示您的交易在矿池中的扩散率，相对于其匿名集。

**重要的是要注意，您的币的前瞻性分数应该根据您最初混币的TXID来计算，而不是根据您最近的混币。相反，UTXO的回顾性分数是根据最后一个周期的TXID来计算的。**

### 使用Boltzmann计算器
Boltzmann计算器是一个用于分析比特币交易的工具，提供了测量其熵级别等高级指标的能力。这些数据提供了对交易隐私的量化评估，并帮助识别潜在缺陷。这个工具已经集成到您的RoninDojo节点中，使其易于访问和使用。

在详细说明如何使用Boltzmann计算器之前，了解这些指标的含义、计算方法及其用途是重要的。尽管适用于任何比特币交易，这些指标对于评估coinjoin交易的质量特别有用。

**软件计算的第一个指标**是可能组合的总数，工具中以`nb combinations`表示。根据涉及的UTXOs的值，这个指标量化了输入可以与输出关联的方式数量。换句话说，它确定了交易可以生成的合理解释数量。例如，根据Whirlpool 5x5模型构建的coinjoin呈现`1496`个可能的组合：
![组合](assets/notext/50.webp)
信用：KYCP

**计算的第二个指标**是交易的熵，由`Entropy`指示。当交易有大量可能的组合时，通常更有意义地参考其熵。这被定义为可能组合数量的二进制对数。这里是使用的公式：
- $E$：交易的熵；
- $C$：交易的可能组合数量。
$$E = \log_2(C)$$
在数学中，二进制对数（底数为2的对数）对应于将2提升到某个幂的逆运算。换句话说，$x$的二进制对数是必须将2提升到的指数，以获得$x$。因此，这个指标用比特来表示。以根据Whirlpool 5x5模型构建的coinjoin交易的熵计算为例，如前所述，它提供了`1496`种可能的组合：$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ 比特}$$

因此，这个coinjoin交易显示的熵为10.5469比特，这被认为是非常令人满意的。这个值越高，交易允许的不同解释就越多，从而增强了其隐私级别。

我们再来看一个更常规交易的例子，它有一个输入和两个输出：[1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
在这个交易的情况下，唯一可能的解释是：`(inp 0) > (Outp 0 ; Outp 1)`。因此，其熵被确定为`0`：
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ 比特}$$
**第三个指标**由Boltzmann Calculator提供，名为`Wallet Efficiency`（钱包效率）。这个指标通过将交易与在相同设置中可想象的最优交易进行比较来评估交易的效率。这引导我们讨论最大熵的概念，它对应于特定交易结构理论上可以达到的最高熵。因此，对于Whirlpool 5x5 coinjoin结构，最大熵被设定为`10.5469`。然后通过将这个最大熵与分析交易的实际熵进行对比来计算交易的效率。使用的公式如下：
- $ER$：交易的实际熵，以比特表示；
- $EM$：给定交易结构可能的最大熵，也以比特表示；
- $Ef$：交易的效率，以比特表示。
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ 比特}$$

这个指标也以百分比表示，其公式则为：
- $CR$：实际可能的组合数量；
- $CM$：具有相同结构的最大可能组合数量；
- $Ef$：效率以百分比表示。
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

因此，`100%`的效率表明，基于其结构，交易最大化了其隐私潜力。
**第四个指标**，熵密度或`Entropy Density`，提供了一个关于交易中每个输入或输出相对熵的视角。这个指标对于评估和比较不同大小交易的效率非常有用。计算它，只需将交易的总熵除以涉及的输入和输出的总数。以Whirlpool 5x5 coinjoin为例：
- $ED$：以比特表示的熵密度；
- $E$：以比特表示的交易熵；
- $T$：交易中输入和输出的总数。
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ 比特}$$
**第五个信息**由Boltzmann Calculator提供的是输入和输出之间匹配概率的表格。这个表格通过`Boltzmann score`指出，一个特定输入与给定输出连接的概率。以Whirlpool coinjoin为例，概率表将突出显示每个输入和输出之间链接的机会，为交易中的模糊性或关联的可预测性提供量化度量：

| %       | 输出 0 | 输出 1 | 输出 2 | 输出 3 | 输出 4 |
|---------|--------|--------|--------|--------|--------|
| 输入 0 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 1 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 2 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 3 | 34%    | 34%    | 34%    | 34%    | 34%    |
| 输入 4 | 34%    | 34%    | 34%    | 34%    | 34%    |

这里，很明显每个输入与任何输出关联的机会都是相等的，这增强了交易的模糊性和保密性。然而，在单一输入和两个输出的简单交易情况下，情况有所不同：

| %       | 输出 0 | 输出 1 |
|---------|--------|--------|
| 输入 0 | 100%   | 100%   |

这里，我们看到每个输出来自输入 0 的概率是 100%。较低的概率因此转化为更大的保密性，通过稀释输入和输出之间的直接链接。

**第六个信息**提供的是确定性链接的数量，以及这些链接的比率。这个指标揭示了在分析的交易中输入和输出之间有多少连接是无可争议的，概率为100%。比率反过来提供了这些确定性链接在交易总链接中的权重视角。

例如，一个Whirlpool类型的coinjoin交易没有确定性链接，因此显示的指标和比率为0%。另一方面，在我们检查的第二个交易中（一个输入和两个输出），指标设置为2，比率达到100%。因此，一个空指标表示由于输入和输出之间没有直接和无可争议的链接，因此具有优秀的保密性。
**如何在RoninDojo上访问玻尔兹曼计算器？**要访问*玻尔兹曼计算器*工具，请转到RoninCLI。为此，请在个人电脑上打开一个终端，并使用以下命令与您的节点建立SSH连接：`SSH ronindojo@[IP]`

例如，如果您节点的IP地址是`192.168.1.40`，则相应的命令将是：
`SSH ronindojo@192.168.1.40`

如果您在第6步更改了用户名，将默认用户名（`ronindojo`）替换为另一个，请确保在命令中使用这个新名称。例如，如果您选择的用户名是`planb`且IP地址是`192.168.1.40`，则要输入的命令将是：
`SSH planb@192.168.1.40`

系统会要求您输入用户密码。输入密码后，按`enter`键确认。然后您将进入RoninCLI界面。使用键盘上的箭头导航到`Samourai Toolkit`菜单，并按`enter`键选择它：

![Samourai Toolkit](assets/notext/43.webp)

然后选择`Boltzmann Calculator`：

![boltzmann](assets/notext/49.webp)

您将进入软件的主页：

![boltzmann home](assets/notext/51.webp)

输入您希望研究的交易的TXID，然后按`enter`键：

![boltzmann txid](assets/notext/52.webp)

然后计算器将提供我们之前讨论过的所有指标：

![boltzmann result](assets/notext/53.webp)

### 您的RoninDojo v2的其他功能
您的RoninDojo节点集成了各种其他功能。特别是，您有能力扫描特定信息以考虑到它。例如，有时您的Samourai钱包，连接到RoninDojo，可能不显示您实际持有的比特币。如果余额显示为0，而您确信这个钱包中有比特币，几个原因可以解释这种情况，如派生路径中的错误。但其中一个原因也可能是您的节点没有正确监控您的地址。为了解决这个问题，您可以确保您的节点确实在跟踪您的`xpub`，使用_xpub工具_。要通过RoninUI访问此工具，请按照以下路径操作：
`Maintenance > XPUB Tool`

输入导致问题的`xpub`，然后点击`Check`按钮以验证此信息：
![xpub tool](assets/notext/54.webp)
确保正确列出了所有交易。还重要的是要验证使用的派生类型是否与您的钱包匹配。如果不是这样，请点击`Retype`，然后根据您的需要从`BIP44`、`BIP49`或`BIP84`中选择。
除了这个工具之外，RoninUI的`Maintenance`标签页还充满了其他有用的功能：
- *Transaction Tool*：允许检查给定交易的详细信息；
- *Address Tool*：允许确认您的Dojo是否跟踪了给定地址；
- *Rescan Blocks*：强制您的节点对指定的区块范围执行新的扫描。

`Push Tx`标签页是RoninUI的另一个有趣功能，它使得可以在比特币网络上广播已签名的交易。交易必须以十六进制形式输入。
关于您的RoninUI仪表板上可用的其他标签页：
- `Apps`：托管Whirlpool应用程序，并将肯定用于未来集成新应用；
- `Logs`：提供对软件事件日志的实时访问；
- `System Info`：提供有关您的节点的一般信息，如CPU温度、存储空间使用情况或RAM数据。您还会找到`Reboot`和`Shut down`选项，用于重启或关闭您的节点；
- `Settings`：允许您更改用户密码。

就是这样了！感谢您跟随本教程到最后。如果您喜欢它，我鼓励您在社交媒体上分享它。此外，如果您有机会，请考虑支持那些为我们的社区提供这些免费和开源软件的开发者捐款：[https://donate.ronindojo.io/](https://donate.ronindojo.io/)。为了深入了解RoninDojo并发现更多资源，我强烈推荐查阅下面提到的外部资源链接。

**外部资源：**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/介绍boltzmann-85930984a159](https://medium.com/@laurentmt/介绍boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)