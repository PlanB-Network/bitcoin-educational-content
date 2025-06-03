---
name: Keet
description: 点对点聊天
---
![cover](assets/cover.webp)



Keet 是一款无需服务器即可运行的即时通讯应用程序。该应用由 Holepunch（一家由 Tether 和 Bitfinex 投资的公司）于 2022 年推出，完全基于点对点网络，采用彻底去中心化的方式：用户之间直接交换信息、通话和文件，没有中间商。



Keet 对所有通信进行端到端加密，不要求提供任何个人数据。注册是匿名的，不需要电话号码或电子邮件。除交换文本信息外，Keet 还提供高质量的视频通话和无限制的文件共享。因此，该应用程序可以混合使用，既可用于个人，也可用于专业用途。



![Image](assets/fr/01.webp)



目前（2025 年 4 月），Keet 尚未完全开源。部分源代码可以在[Holepunch 的 GitHub 代码库](https://github.com/holepunchto)上找到，尤其是加密和网络组件，但客户端 Interface 还没有。不过，Holepunch 已宣布打算最终将整个应用程序开源。根据你发现本教程的时间，这可能已经完成了。




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
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| **Keet**             | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = 端到端加密*。



## 安装 Keet



Keet 适用于所有平台。您可以直接从手机应用商店下载应用程序：




- [Google Play]（https://play.google.com/store/apps/details?id=io.keet.app&pli=1）；
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549)；



在 Android 上，也可以 [通过 APK 安装](https://github.com/holepunchto/keet-mobile-releases/releases)。



在本教程中，我们将重点介绍手机版，但请注意，[电脑版也可用](https://keet.io/) （MacOS、Linux 和 Windows）。还可以在多个设备上同步账户。



## 在 Keet 上创建账户



首次启动时，您可以忽略演示屏幕。



![Image](assets/fr/02.webp)



点击 "*我是新用户*"按钮。



![Image](assets/fr/03.webp)



接受使用条款，然后点击 "*快速设置*"。



![Image](assets/fr/04.webp)



选择名称或昵称，然后点击 "*完成设置*"。



![Image](assets/fr/05.webp)



您的个人资料现已创建。再次单击 "*完成设置*"完成设置。



![Image](assets/fr/06.webp)



您可以随时从 "*个人资料*"选项卡中自定义个人资料。



## 保存您的 Keet 账户



使用新 Keet 帐户的第一件事就是保存恢复短语。这是一串由 24 个单词组成的短语，可以让你在丢失或更换设备时恢复对账户的访问。知道这个短语的任何人都可以完全访问您的账户，因此必须做一个可靠的备份，千万不要泄露。



为此，请单击 Interface 右下方的 "*配置文件*"选项卡。



![Image](assets/fr/07.webp)



然后进入 "*设置*"菜单。



![Image](assets/fr/08.webp)



选择 "*隐私和安全*"。



![Image](assets/fr/09.webp)



然后点击 "*恢复短语*"。



![Image](assets/fr/10.webp)



按 "*查看短语*"按钮显示恢复短语。仔细复制并妥善保管。



![Image](assets/fr/11.webp)



## 用 Keet 发送信息



要在 Keet 上通信，您需要创建 "*房间*"。为此，请单击 Interface 右上方的铅笔图标。



![Image](assets/fr/12.webp)



选择 "*新建群聊*"。



![Image](assets/fr/13.webp)



为 "*房间*"选择一个名称和描述，然后点击 "*创建群聊*"。



![Image](assets/fr/14.webp)



您的 "*Room*"现已创建。点击右上角的 "*+*"图标邀请与会者。



![Image](assets/fr/15.webp)



定义通过邀请链接授予新会员的权限，以及链接的有效期。然后点击 "*generate invite*"（*generate 邀请*）。



![Image](assets/fr/16.webp)



Keet 将通过 generate 链接加入您的 "*Room*"。您可以复制并分享它，也可以让您想邀请的人扫描它的 QR 码。



![Image](assets/fr/17.webp)



现在就可以开始交换信息和多媒体文件了。要开始通话，请单击右上角的电话图标。



![Image](assets/fr/18.webp)



您还可以从该组向特定成员发送私人信息。点击群组的个人照片，然后在 "*成员*"部分选择所需的成员。



![Image](assets/fr/19.webp)



点击 "*发送 DM 申请*"按钮并输入您的信息。



![Image](assets/fr/20.webp)



一旦接受了 DM 请求，您就可以在主页上找到这位联系人，在那里您可以与他私下交谈。



![Image](assets/fr/21.webp)



## 在多台设备上同步您的账户



现在您已经知道如何使用 Keet 并拥有一个账户，还可以在电脑等其他设备上同步。为此，请在手机上打开应用程序，然后点击 "*个人档案*"，进入 "*设置*"。



![Image](assets/fr/22.webp)



然后进入 "*我的设备*"菜单。



![Image](assets/fr/23.webp)



点击 "*添加设备*"。Keet 将 generate 同步新设备的链接。复制此链接。



![Image](assets/fr/24.webp)



在第二台设备上安装 Keet。在主屏幕上选择 "*我是当前用户*"选项。



![Image](assets/fr/25.webp)



然后点击 "*链接设备*"。



![Image](assets/fr/26.webp)



粘贴第一台设备提供的链接，然后点击 "*开始同步*"。



![Image](assets/fr/27.webp)



在第一个设备上，点击 "*确认链接设备*"以授权连接。



![Image](assets/fr/28.webp)



在第二个设备上，点击 "*链接设备*"完成整个过程。



![Image](assets/fr/29.webp)



现在，您可以通过这个新设备访问您的所有 "*房间*"和对话。



![Image](assets/fr/30.webp)



恭喜您，现在您已经掌握了使用 Keet 消息的速度，它是 WathsApp 的绝佳替代品！如果您觉得本教程有用，请在下面留下 Green 大拇指，我将不胜感激。欢迎在您的社交网络上分享本教程。非常感谢



我还向你推荐另一篇教程，其中我向你介绍了质子邮件（Proton Mail），它是 Gmail 的替代品，对隐私更加友好：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2