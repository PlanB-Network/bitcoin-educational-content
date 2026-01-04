---
name: White Noise
description: 基于 Nostr 和 MLS 协议的私有去中心化信息传输应用程序
---

![cover](assets/cover.webp)




## 导言



"困难之中蕴藏着机遇"。阿尔伯特-爱因斯坦的这句话提醒我们，问题并不是一成不变的，其中蕴含着创新解决方案的种子。



我们在本教程中介绍的解决方案的推出动机就很好地说明了这一点。它是**White Noise**，因需要而生。



根据*Bitcoin杂志*的报道，创始人马克斯-希勒布兰德（Max Hillebrand）这样说道："他解释说："现有的加密应用程序在大规模使用时效率很低：增加 100 人的群组对话速度会减慢。他解释说："现有的加密应用程序在大规模使用时效率低下：在一个群组对话中加入 100 个人会大大降低加密速度。同时，去中心化平台不提供私人信息。最后，Nostr 的开放中继网络允许每个人传播想法，但对直接信息的保护仍然严重不足。我们意识到：为了保护自由，我们必须合并这些系统。



## 什么是 White Noise？



White Noise 是一个由非营利团队开发的开源消息应用程序。该应用程序倡导安全、隐私和去中心化。与传统应用程序不同，它既不需要电话号码，也不需要电子邮件地址。


White Noise 的特点是整合了两个基本协议--Nostr 和 MLS，这两个协议构成了 White Noise 的技术基础。



Nostr（由中继器传输的笔记和其他东西）是一个分散的开源协议，旨在抵制审查。  该协议使用中继器、密钥对和客户端。



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

有了白噪声，您甚至可以选择自己的中继设置，最大限度地保护隐私。



另一方面，MLS（Messaging Layer Security）是一种能对信息进行端到端加密的安全协议。换句话说，只有端点（即信息的发送方和接收方）才能访问信息。这意味着参与信息路由的中继站无法访问信息内容。



下面是 White Noise 与一些最著名的信息应用程序的快速比较。



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## 开始使用 White Noise



### White Noise 安装



访问 [White Noise 网站](https://www.whitenoise.chat/)，然后点击 **下载**。



![screen](assets/fr/03.webp)



White Noise 目前只能在移动设备上使用。


在出现的新界面上，按 ：





- 如果您想在 Android 上下载，请点击 **Zapstore** 或 **Android APK** 按钮；
- 如果您使用的是 iPhone，请点击 **iOS TestFlight** 按钮。



![screen](assets/fr/04.webp)



在本教程中，我们将进行 Android 下载。


如果您选择通过**Zapstore**下载，则会跳转到 Zapstore。进入 Zapstore 后，在搜索栏中输入 **White Noise**。然后点击**安装**进行下载。



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



如果你选择下载 APK 文件，你会被重定向到 White Noise GitHub 存储库，为你的智能手机选择合适的版本。



可用的 APK 文件有 ：





- whitenoise-0.2.1-arm64-v8a.apk** (57.7 MB)，适用于配备 64 位处理器的新款手机；
- whitenoise-0.2.1-armeabi-v7a.apk**（47.5 MB）适合使用 32 位处理器的旧版手机。



您还可以使用**.sha256**文件，这些文件只是校验和，用于验证下载的完整性。



![screen](assets/fr/07.webp)



下载完成后，安装并打开应用程序。



![screen](assets/fr/08.webp)



### 初始用户账户设置



首次连接 White Noise，请按**注册**按钮。



![screen](assets/fr/09.webp)



然后，选择个人照片、姓名并添加简短的自我介绍，配置您的个人资料。您不必填写真实身份（姓名和照片）。


请注意，White Noise 会自动为您选择一个名字（假名），您可以保留或更改。最后，按下**结束**按钮。



![screen](assets/fr/10.webp)



您将被重定向到 White Noise 的**主屏幕**，您的对话将在此列出。您的账户现已设置完毕，可以随时使用。您可以共享个人资料或搜索好友开始聊天。



![screen](assets/fr/11.webp)




### 发现 White Noise 接口



在主界面的屏幕顶部，你会看到 ：



在左上角，个人资料图标是个人资料照片的缩略图，或者是个人资料名称的第一个字母。点击它可进入账户设置。



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



在右上角，你可以找到开始新对话的图标。



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## 用户账户设置



按左上角的配置文件图标进入设置。



![screen](assets/fr/16.webp)



在**设置**界面的顶部，你会看到你的照片和个人资料名称，然后是你的公钥，你可以使用旁边的二维码共享公钥。



![screen](assets/fr/17.webp)



下面是**更改账户**按钮，可让您连接到应用程序中的另一个配置文件。



![screen](assets/fr/18.webp)



第一部分有四（4）个子菜单，例如 ：





- 修改个人资料**



在该子菜单中，您可以修改配置文件名称、Nostr 地址 (NIP-05)...不要忘记点击**保存**来保存更改。



![screen](assets/fr/19.webp)





- 配置文件键**



在这里，您可以访问您的公钥和私钥（秘钥）。正如 White Noise 提醒您的那样，您的私人密钥在任何情况下都不得泄露。



![screen](assets/fr/20.webp)





- 电源继电器



在该子菜单中，您可以添加或删除**通用继电器**（定义用于所有 Nostr 应用程序的继电器）、**盒式继电器**和**钥匙包继电器**。



为此，请点击中继站前面的**垃圾**图标删除中继站，或点击**+**（加号）图标添加新的中继站。



![screen](assets/fr/21.webp)





- 断开**



点击该子菜单可断开账户与应用程序的连接。但请确保离线保存了私钥，否则以后将无法再次登录。



![screen](assets/fr/22.webp)




第二部分提供子菜单：





- 应用程序设置



在这里，您可以定义应用程序的外观（主题和显示语言），甚至在您认为数据已被泄露或您自己感到有风险时删除数据。



![screen](assets/fr/23.webp)





- 向 White Noise 捐赠



您可以通过 White Noise 背后的团队（非营利组织）的闪电地址或 Bitcoin 默默支付地址捐款支持他们。



![screen](assets/fr/24.webp)



最后，最下方是**开发人员设置**。



![screen](assets/fr/25.webp)




## 开始对话



现在让我们来看看如何开始对话。在撰写本文时，White Noise 提供了三种交流方式。我们将依次探讨**私人对话**（**1:1**聊天），即只有您和一个人之间的对话、**群组对话**和**发送多媒体文件**。




### 猫 1:1



要在主界面添加新通讯员，请单击开始新对话的图标。


然后扫描公开密钥的 QR 码 (1) 或将新联系人的公开密钥 (2) 粘贴到搜索栏，即可找到他或她。



![screen](assets/fr/26.webp)



然后点击**开始对话**按钮，开始与通讯员对话。您还可以按**添加到群组**按钮来**关注**您的联系人或邀请他/她加入群组对话。



![screen](assets/fr/27.webp)



您给新通讯员的第一条信息类似于邀请请求。在您与他/她交流之前，您的联系人必须接受这一请求。如果对方拒绝，那就无法进行对话了。



![screen](assets/fr/28.webp)



更重要的是，只要他们不接受你的邀请，他们就无法阅读你最初发送的信息内容。



一旦他接受了你的邀请，他就可以回复你，你们就可以进行无缝、安全的交流。



![screen](assets/fr/29.webp)



此外，在讨论中，您还可以使用其他功能。



您可以长按特定信息来显示选项，例如 ：




- 用表情符号 (1) 回应消息；
- 按**回复** (2)，直接引用**回复信息；
- 按**复制** (3)复制信息。



![screen](assets/fr/30.webp)





- 只有当信息来自您本人时，才可使用**删除**按钮删除信息。



![screen](assets/fr/31.webp)



您可以在对话中进行搜索。



点击屏幕上方的联系人头像进入 "对话信息"，然后点击**在对话中搜索**按钮。



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



在出现的搜索栏中，输入要搜索的单词并启动搜索。然后，您会看到搜索词以**粗体**突出显示。



![screen](assets/fr/34.webp)




### 小组对话



可在 White Noise 上创建对话组。



为此，请轻触新对话启动界面中的图标，然后点击**新群组对话**。然后，在搜索栏中输入要添加到群组的第一个成员的公开密钥。



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



最后，如果该选项不起作用，可在**开始新对话**界面的搜索栏中输入你想添加到群组的第一个成员的公开密钥。你也可以扫描与其公钥相关的二维码。



这一次，不要点击**开始对话**按钮，而是点击**添加到群组**按钮。



![screen](assets/fr/37.webp)



在弹出的菜单中，点击**新建群组对话**。



![screen](assets/fr/38.webp)



然后按**继续**（无需再次输入公钥）。



![screen](assets/fr/39.webp)



作为组的创建者，您将自动成为其管理员。填写组的详细信息，如**组名称和描述**，然后点击**创建组**按钮。



![screen](assets/fr/40.webp)



您添加为第一个成员的用户以及随后添加的其他用户都会收到邀请他们加入群组的通知。他们必须点击**接受**才能加入群组。



![screen](assets/fr/41.webp)



您也可以将正在聊天的新成员添加到现有群组中。要这样做，点击屏幕上方对方的头像进入 "对话信息"，然后点击**添加到群组**按钮。



![screen](assets/fr/42.webp)



在出现的新界面上，**选中**您想将它添加到的群组，然后点击**添加到群组**。剩下要做的就是等待它同意加入群组了。



![screen](assets/fr/43.webp)



请注意，只有群组管理员才能修改群组信息，添加或开除成员。此外，密钥轮换可以防止被禁止的成员解密未来的信息。



要删除成员，请在群组主界面点击顶部的群组图标进入群组信息界面。



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



然后点击成员姓名，**从群组中删除**。在此界面，您还可以给他发送信息、关注他或将他添加到另一个群组。



![screen](assets/fr/46.webp)



### 发送多媒体文件



目前，White Noise 上的用户之间只能共享照片。无论您是在私人对话还是群聊中，都需要 ：





- 按文本信息输入框左侧的**加 (+)** 符号。



![screen](assets/fr/47.webp)





- 然后点击底部标有**照片**的方框，进入您的相册。



![screen](assets/fr/48.webp)





- 选择要发送的照片。



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## 应牢记的要点



White Noise 具有良好的保密性和卓越的安全性。另一方面，White Noise 的应用刚刚起步，还不是很广泛，仍处于起步阶段。因此，现在下结论还为时过早。在使用过程中可能会遇到一些故障。



目前，与流行的信息应用程序相比，它缺乏某些功能（不能进行音频或视频通话，不能发送音频或视频多媒体文件）。



尽管如此，White Noise 仍然是保密性要求极高的对话（例如与家人、好友或共同事业的积极分子）的一个有趣选择，尽管它确实需要花费一点精力来安装（通过其他应用程序商店或 APK 文件）和学习（掌握一点 Nostr 协议的密钥对、客户端和中继的概念）。



现在您知道如何使用 White Noise 与亲朋好友安全通信了吧。如果您觉得本教程有用，请为我们竖起大拇指。



我们向您推荐关于 Tox Chat 的教程，这是一款可以让您通过去中心化的 Tox 协议进行无中介聊天的应用程序。



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3