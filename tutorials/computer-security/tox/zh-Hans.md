---
name: 毒素
description: 在去中心化的 Tox 协议上，无需中介即可开启对话
---
![cover](assets/cover.webp)



端到端加密是 WhatsApp 和 Telegram 等许多信息应用程序提供的一项服务。这里所说的加密是指，在发送方发送信息之前，先用一把只有接收方才有钥匙的密码锁将信息加密。今天，我们将去探索一款完全去中心化的端到端加密信息应用程序，它基于类似于 Blockchain 的原理，提供安全的端到端加密通信，无需中介：Tox Chat。



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = 端到端加密*。



## Tox 是什么？



Tox 是一种免费（开源）、去中心化的通信协议，它使用*网络和密码学库*（NaCl）技术以及加密算法组合来确保用户的安全和保密。Tox 可让您与朋友安全、分散、无中介地发送 Exchange 文本消息、拨打音频和视频电话、共享文件和分享屏幕。



Tox 协议使用的技术与区块链等点对点网络类似，有利于协议基础设施的去中心化。与社交网络和端到端加密信息应用不同，Tox Chat 应用建立在去中心化协议的基础上，没有中央服务器。所有用户都在一个无中介、抗审查的点对点网络中交流。要进行通信，每个用户都要通过一个唯一的 ID（ToxID）来识别，该 ID 源自用户的公钥，并存储在分布式 Hash 表中。



## 加入毒素



您可以通过从 [Tox Chat 网站](https://tox.chat) 下载的即时通讯客户端使用 Tox 协议。



![download](assets/fr/01.webp)



根据操作系统的不同，您可以下载并安装与 .NET Framework 4.0 兼容的 Tox 客户端：





- aTox[aTox](https://github.com/evilcorpltd/aTox)，一款用 Kotlin 编写的 Tox 客户端，仅在安卓平台上提供



![aTox](assets/fr/02.webp)





- qTox：来自 [open source](https://github.com/TokTok/qTox) 的 Tox 客户端，基于 Qt Framework (C++)，可在 Windows、Linux 和 MacOs 上使用。



![qTox](assets/fr/03.webp)





- Toxic：[Toxic](https://github.com/JFreegman/toxic) 是一个用 C 语言编写的 Tox 客户端，可在带有命令行界面的系统上运行。



![Toxic](assets/fr/04.webp)



在本教程中，我们将使用 Windows 上的 qTox 客户端和 aTox 进行通信。



## 开始使用 qTox



下载后，安装 Tox 客户端并创建个人资料。



![qTox-acount](assets/fr/05.webp)



恭喜您，您刚刚加入了 Tox 协议。在 qTox 软件上，点击用户名即可找到您的个人资料信息。



![profil](assets/fr/06.webp)



特别是，您可以找到您的 Tox ID，您可以将其保存为二维码，与希望与您取得联系的人分享。



导出 Tox 配置文件，这样您就有了一份配置文件和联系人信息的备份，可以用来恢复。点击**导出**按钮，然后选择备份文件的路径。



![export](assets/fr/07.webp)



从**更多**菜单，添加好友、导入联系人并管理收到的好友请求。



![friends](assets/fr/08.webp)



例如，您可以通过这个 Tox ID 联系我：EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



发送好友请求后，收件人必须接受或拒绝您的请求，您才能联系他们。



![request](assets/fr/09.webp)



您的 Tox 客户端包含即时消息应用程序提供的所有选项：





- 视频通话





- 语音通话





- 文件共享





- 表情符号



![chat](assets/fr/10.webp)



### 同行小组



您的 Tox 客户端还可以让您以完全分散的方式与一群人进行交流：这就是所谓的会议。在 "**群组**"菜单中，创建一个新会议，或查看您收到的会议邀请列表。



![conferences](assets/fr/11.webp)



创建会议后，您可以在 Tox 客户端上邀请朋友加入会议。在好友列表中，右键单击您想邀请的好友的用户名。点击**邀请参加会议**选项，然后选择您创建的会议名称。您也可以通过**创建新会议**选项隐式创建会议来邀请朋友。



⚠️ Tox 客户端仍在开发中，因此您在与软件交互时可能会遇到错误。Tox Android 客户端 (aTox) 尚未提供会议和视频通话功能。



![invite](assets/fr/12.webp)



### 文件传输



在**文件传输**菜单中，您可以查看从联系人处发送和接收文件的历史记录。



![files](assets/fr/13.webp)



您还可以为每次讨论定制文件共享配置。右键单击收件人的用户名，选择 "显示更多详细信息"。



![details](assets/fr/14.webp)



从 Interface 详情中，您可以管理授予收件人的 .NET 和 .NET 授权：





- 自动接受会议邀请。





- 自动接受文件。





- 讨论文件的备份路径



![permissions](assets/fr/15.webp)



### 更多参数



在**设置**菜单中，您可以自定义 Tox 客户端的设置。





- 在**常规**部分，更改 Tox 客户端的基本语言，定义文件备份路径和自动接受的最大文件大小。



![general](assets/fr/16.webp)





- 在**Interface 用户**部分，修改信息的字体和大小。您还可以更改 Tox 客户端的主题。



![ui](assets/fr/17.webp)





- 在 "**隐私**"选项卡中，您可以通过取消选中 "保留聊天记录 "复选框来定义短暂信息。当您发现自己被好友请求发送垃圾邮件时，也可以点击 "generate 随机垃圾邮件代码 "按钮更改您的垃圾邮件代码。



![privacy](assets/fr/18.webp)



### 如何保证 Tox 的保密性？



Tox 协议使用分布式 Hash 表创建分散节点网络。每个 Tox 客户端都是 DHT 网络的一部分，并存储有关其他节点的信息。就 Tox 而言，DHT 将 IP 地址存储为与 Tox 公钥（Tox ID）相关联的值。这样，无需查询中央服务器，就能轻松搜索到 Tox 客户端设备。



想象一下，向我们的用户 `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` 写信，我们将其命名为**用户 B**。Tox 客户端将在 Hash 分布表中找到该标识符，并检索相关的 IP Address。一旦找到 IP Address，Tox 客户端就会与**用户 B** 的机器建立直接的加密通信通道，或使用其他节点作为中继站与**用户 B** 通信。加密算法可确保无论通过哪种通信渠道，只有**用户 B** 才能读取您的信息内容。



如果您喜欢发现 Tox，并能理解它对加强隐私保护的作用，请随时为本教程竖起大拇指。我们还向您推荐我们的《简单登录》教程，这是一款可以让您匿名接收和发送电子邮件的工具。



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41