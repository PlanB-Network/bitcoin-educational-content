---
name: RaspiBlitz
description: 设置您的RaspiBlitz的指南
---

![image](assets/0.webp)

RaspiBlitz是一个自助式的闪电网络节点（LND 和/或 Core Lightning），与比特币全节点一起运行在树莓派（1TB SSD）上，并配有一个漂亮的显示屏，便于设置和监控。

RaspiBlitz主要面向那些想要学习如何在家中去中心化运行自己的节点的人——因为：不是你的节点，就不是你的规则。通过成为其完整部分，发现并发展闪电网络日益增长的生态系统。将其作为工作坊的一部分或作为周末项目自己构建。

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - 如何运行一个闪电和比特币全节点，由BTC session提供

# Parman的Raspiblitz设置指南

Raspiblitz是一个出色的系统，用于运行比特币节点和相关应用。我向大多数用户推荐它和MyNode节点（理想情况下应有两个节点以实现冗余）。一个主要优势是Raspiblitz节点是“Free Open Source Software”，而MyNode或Umbrel则不是。[为什么这很重要？Vlad Costa 解释道。](https://bitcoin-takeover.com/why-bitcoin-free-open-source-software-matters/amp/?__twitter_impression=true) 你还可以通过WiFi连接而不是以太网运行Raspiblitz – 这里有一个[补充指南](https://armantheparman.com/headless-wifi/)供参考。（我还没有找到在MyNode上实现这一点的方法）。

你可以购买一个带有小屏幕的现成节点，或者你可以自己构建一个（你不需要屏幕）。

[GitHub页面上的指南](https://github.com/rootzoll/raspiblitz)非常出色，但可能对有中等经验的用户来说过于详细。我的说明将更简洁，希望更容易遵循。

基本上，该过程与使用Raspberry Pi 4设置[MyNode节点](https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/)的过程非常相似。Raspiblitz指南建议您购买显示器，但实际上您并不需要，而且我也不推荐这样做。您甚至不需要额外的键盘或鼠标。只需通过同一家庭网络上的计算机访问设备的终端菜单，并在终端中使用ssh命令即可。这在Linux/Mac（简单）上可行，而在Windows上则稍微困难一些。

## 第1步：购买设备。

你需要的设备与运行MyNode节点完全相同。你可以尝试其中之一，唯一的区别是微SD卡上的数据。

- 树莓派4，4Gb内存或8Gb（4Gb已经足够）
- 官方树莓派电源（非常重要！不要买通用的，认真的）
- Pi的外壳。（FLIRC外壳很棒。整个外壳是散热器，你不需要风扇，风扇可能会很吵）
- 32 Gb微SD卡（你需要一个，但有几个会方便。）
- 内存卡读卡器（大多数计算机没有微SD卡的插槽）。
- 外置SSD 1Tb硬盘。
- 以太网线（连接到你家的路由器）。

你不需要显示器（或键盘或鼠标）

注意：这是错误的硬盘：这是一个便携式外置硬盘。它不是SSD。SSD至关重要。这就是为什么它便宜（价格以澳元计）

![image](assets/1.webp)

这是正确的类型：

![image](assets/2.webp)

这个更快，但不必要地昂贵：

![image](assets/3.webp)

## 第2步：下载Raspiblitz镜像
导航到 [Raspiblitz GitHub 网站](https://github.com/rootzoll/raspiblitz)，然后找到“download image”链接：
![image](assets/4.webp)

下载文件的 sha-256 哈希值在网站上提供。它会随着每次更新而改变。如果你不明白这是关于什么的，你应该明白，所以我写了一份[你可以在这里阅读的指南。](https://armantheparman.com/gpg/)

![image](assets/5.webp)

## 步骤3：验证镜像

在继续之前，如果你不熟悉命令行下的文件系统操作，这很容易学，你应该去了解一下。

这是一个[对 Linux 有用的视频，但也适用于 Mac](https://youtu.be/id3DGvljhT4?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK)。

对于 Windows，这里有一个[简单的教程](https://www.youtube.com/watch?v=MBBWVgE0ewk&t=1s)。
_更新：pgp/gpg 验证现已可用。您需要 Openoms 的公钥。[在这里](http://parman.org/downloadable/openoms.txt)（链接可能需要无痕模式才能工作 – http，不是 https）_
Mac/Linux

等待文件下载完成（很重要！），然后打开终端，导航到你下载文件的位置，并输入以下命令...

```bash
shasum -a 256 xxxxxxxxxxxxxx
```

其中xxxxxxxxxxxxxx是你刚刚下载的文件的名称。如果你不在该文件所在的目录中，你必须输入完整路径。

计算机会思考大约20秒。检查输出的哈希文件是否与上一步从网站下载的文件匹配。如果它们完全相同，你就可以继续了。
Windows

打开命令提示符并导航到文件下载的位置，然后输入此命令：

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

其中xxxxxxxxxxxxxx是你刚刚下载的文件的名称。如果你不在该文件所在的目录，你必须输入完整路径。

计算机会思考大约20秒。检查输出的哈希文件是否与上一步从网站下载的文件匹配。如果它们完全相同，你就可以继续了。

## 步骤4：刷写SD卡

您可以使用 Balena Etcher 来完成此操作。[在此下载](https://www.balena.io/etcher/)。

Etcher的使用非常直观。插入你的micro SD卡并将Raspiblitz软件（.img文件）刷写到SD卡上。

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

完成后，驱动器将不再可读。你可能会从操作系统收到一个错误，驱动器应该会从桌面上消失。拔出卡片。

## 步骤5：设置树莓派并插入SD卡

部件（未显示外壳）：

![image](assets/10.webp)

![image](assets/11.webp)

连接以太网线和硬盘USB连接器（暂时不要连接电源）。避免连接中间的蓝色USB端口。它们是USB 3。即使驱动器可能支持USB 3，也请使用USB 2端口（更可靠）。

![image](assets/12.webp)

micro SD卡放在这里：

![image](assets/13.webp)

最后，连接电源：

![image](assets/14.webp)

## 步骤6：找到树莓派的IP地址

使用Raspiblitz，你永远不需要一个显示器。然而，你确实需要在家庭网络上使用另一台计算机。如果你的树莓派没有通过以太网连接，并且你想依赖WiFi，找到IP需要一些计算机技能。对不起，无法帮助你。你需要一个以太网连接。（问题来自于需要访问显示器和操作系统来连接WiFi并输入密码。）

检查你的路由器，获取所有已连接设备的IP列表。
我在浏览器中输入了192.168.0.1（路由器随附的说明），登录后，我能看到我的设备IP地址为192.168.0.191。注意，这些IP地址在互联网上不是公开可见的（它们首先通过路由器），它们仅是您家庭网络上设备的标识符。
找到IP地址是至关重要的。

> 更新：您可以在Mac或Linux机器上使用终端，通过命令“arp -a”找到家庭网络上所有以太网连接设备的IP地址。输出的格式可能不如路由器显示的那么美观，但所有您需要的信息都在那里。如果不明显哪个是树莓派，进行试错。

## 步骤7：SSH进入树莓派

记得在开机前将SD卡插入树莓派。等待几分钟，然后在另一台Linux/Mac上，打开终端。

对于Mac/Linux，在终端中输入：

```bash
ssh admin@您的树莓派IP地址
```

在 Windows 上，你需要安装 [putty](http://putty.org/) 才能通过 ssh 连接到 Pi。输入与上面相同的命令。

您第一次这样做，或者当您通过更换SD卡更改树莓派的操作系统时，您可能会也可能不会遇到这个错误...

![image](assets/15.webp)

解决的方法是导航到“known_hosts”文件所在的位置（错误消息中会告诉您），并删除它。命令是"rm known_hosts"

然后，重复ssh命令以登录。这将会发生...

![image](assets/16.webp)

输入yes（完整单词）以继续。

如果成功，您将被要求输入密码。这不是您电脑的密码，而是raspiblitz的密码。通用密码是“raspiblitz”，您稍后会更改它。终端窗口将变成蓝色，您将有类似旧DOS菜单的菜单选项。使用箭头键或鼠标导航。

![image](assets/17.webp)

按照提示设置您的密码，然后它将检测您的硬盘驱动器，并给您一个格式化的选项（如果需要）。

然后，您将被问及是否想从另一个来源复制区块链数据或重新下载。复制它是一个学习过程，指令相当好，值得保留...

![image](assets/18.webp)

简单但较慢的方式是从头开始下载整个链...

![image](assets/19.webp)

许多文本将在终端屏幕上快速闪过。您可能会误以为这是区块链下载的过程，但在我看来，它似乎是在生成通信的私钥。

然后出现闪电网络选项。

![image](assets/20.webp)

创建一个新密码来锁定您的闪电钱包，然后将创建一个新钱包，并给您24个单词来记录下来...

![image](assets/21.webp)

确保您记录下来并保持安全。我听说过一个人因为他没有计划使用闪电网络，所以没有记录下来，但一年后决定使用它，并开启了通道。然后意识到他的单词没有备份，而且我记得从设备中再次提取单词是不可能的，他不得不关闭所有的通道并重新开始。他摆脱了困境，但其他人可能就没有那么幸运了。

接下来，几分钟的文本会在终端窗口滚动。然后...

![image](assets/22.webp)
您将会从ssh会话中登出。请使用您的新密码，密码A重新登录。一旦登录，系统会要求您输入密码C以解锁您的闪电钱包。
现在我们等待。两周后见。您可以关闭终端，这对Pi没有任何影响，它只是一个通信窗口。

![image](assets/23.webp)

如果由于某种原因，您想在区块链下载完成之前关闭Pi，只要您正确操作，这也是可以的。一旦您重新连接，区块链将从中断的地方继续下载。

按CTRL+c退出蓝屏。您将访问Pi的Linux终端。在这里，您可以输入“menu”，这将加载以下屏幕，从那里您可以关闭Pi电源。

![image](assets/24.webp)

指南结束

从现在开始，您的节点已经准备就绪。如果您还需要帮助浏览更多选项，请参考github上的更多教程和指南 https://github.com/raspiblitz/raspiblitz#feature-documentation