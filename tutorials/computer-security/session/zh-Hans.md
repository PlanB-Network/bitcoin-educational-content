---
name: Session
description: 发送加密信息，而非元数据
---
![cover](assets/cover.webp)



会话是一种加密信息应用程序，创建于 2020 年，旨在提供比传统信息更高的保密性。它最初由*奥克森隐私技术基金会*开发，后由*会话技术基金会*开发。



会声会影拥有一些有趣的技术特点：信息端到端加密、分散式网络组织以保证可用性和冗余性，以及受 Tor 启发的洋葱路由。此外，与需要电话号码注册的 WathsApp 或 Signal 不同，Session 不要求提供任何个人信息（没有电话号码，没有电子邮件，只有一对加密密钥）。



会话功能可让您发送信息、文件、语音信息、音频通话以及多达 100 名成员的群组（或更多群组），同时最大限度地减少元数据泄露。



![Image](assets/fr/01.webp)



会话 "首先面向将保密性放在首位的用户。该信息服务是 WhatsApp 的重要替代品，其架构设计可抵御现代监控模式。



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
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = 端到端加密*。



## 安装会话应用程序



会话适用于所有平台。您可以直接从手机应用商店下载该应用程序：




- [Google Play]（https://play.google.com/store/apps/details?id=network.loki.messenger）；
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868)；
- [F-Droid](https://fdroid.getsession.org/).



在 Android 上，也可以 [通过 APK 安装](https://github.com/session-foundation/session-android/releases)。



在本教程中，我们将重点介绍手机版，但请注意，[电脑版也可使用](https://getsession.org/download) （MacOS、Linux 和 Windows）。稍后，我们将介绍如何在多台设备上同步账户。



## 创建会话账户



首次启动时，点击 "*创建账户*"。



![Image](assets/fr/02.webp)



为您的个人资料选择一个显示名称。可以是化名，也可以是真名。



![Image](assets/fr/03.webp)



然后，您需要在两种通知管理模式中进行选择：





- 快速模式（**Firebase Cloud Messaging/Apple Push Notification Service**）：借助谷歌或苹果（取决于您的系统）提供的通知服务，您可以近乎实时地接收消息通知。为此，你的 IP Address 和一个唯一的通知 ID 会被传送到谷歌或苹果，会话账户 ID 也会在 STF 服务器上注册（通过 Tor）。这种模式会暴露元数据（诚然微乎其微），但不会泄露信息内容或联系人，也不会让你的实际活动被追踪到。因此，这种模式的响应速度更快，但依赖于集中式基础设施，保密性稍差。





- 慢速模式（**后台轮询**）：会话应用程序在后台保持激活状态，定期轮询网络以获取新信息。这种方式比第一种方式更能保证保密性，因为数据不会传输到第三方服务器；谷歌、苹果或 STF 服务器都不会收到任何信息。另一方面，这种模式也有两个缺点：通知可能会延迟（长达几分钟），而且由于应用程序在后台活动，能耗通常会更高。



![Image](assets/fr/04.webp)



现在您已连接到会话应用程序，可以开始交换信息。



![Image](assets/fr/05.webp)



## 保存会话帐户



在开始使用会声会影之前，首先要保存账户，以便在设备丢失时恢复。为此，请点击 "*保存恢复密码*"旁边的 "*继续*"按钮。



![Image](assets/fr/06.webp)



然后，会话将显示一个 Mnemonic 短语。请仔细复制并妥善保管。该短语提供了对会话账户的完全访问权限，因此切勿泄露。你需要它才能在其他设备上访问你的账户，尤其是在你当前的手机丢失或更换的情况下。



![Image](assets/fr/07.webp)



该短语的工作方式与 Bitcoin 组合中使用的 Mnemonic 短语类似。因此，我建议您参考另一篇教程，我在其中介绍了保存 Mnemonic 短语的最佳做法：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**请注意**：与 Bitcoin 作品集中使用的 Mnemonic 短语不同，在会话中，**您绝对必须保存每个单词的完整**。前 4 个字母是不够的！



## 设置会话应用程序



要访问应用程序设置，请单击 Interface 左上角的个人照片。您可以在此添加个人照片。



![Image](assets/fr/08.webp)



在 "*隐私*"菜单中，您可以启用或禁用各种功能（注意，有些功能可能会暴露您的 IP Address）。我还建议激活 "*锁定应用程序*"选项，该选项要求通过身份验证才能访问应用程序。



![Image](assets/fr/09.webp)



在 "*通知*"菜单中，你可以选择 "*快速模式*"和 "*慢速模式*"（参见本教程的前几部分）。您还可以根据自己的喜好自定义通知。



![Image](assets/fr/10.webp)



最后，进入 "*外观*"菜单，根据自己的喜好调整 Interface。如果您想重新备份，"*恢复密码*"菜单允许您找回 Mnemonic 短语。



![Image](assets/fr/11.webp)



## 使用会话发送信息



要联系其他人，请点击主页上的 "*+*"按钮。



![Image](assets/fr/12.webp)



有多个选项可供选择。如果您想创建或加入一个群组，请选择 "*创建群组*"或 "*加入社区*"。



![Image](assets/fr/13.webp)



如果您希望别人将您添加为联系人，可以让他们扫描您的会话 ID 作为二维码。



![Image](assets/fr/14.webp)



要远程发送登录信息，请点击 "*邀请朋友*"。然后，您可以复制您的会话 ID，并通过其他通信渠道发送。您也可以在主页上点击您的个人照片来获取此信息。



![Image](assets/fr/15.webp)



如果您有他人的会话 ID 并希望添加，请点击 "*新信息*"。



![Image](assets/fr/16.webp)



然后，您可以将其标识符粘贴到文本中，如果有 QR 码，也可以直接扫描。



![Image](assets/fr/17.webp)



然后向此人发送一条初始信息。



![Image](assets/fr/18.webp)



一旦对方接受了您的请求，您就会看到他们的用户名出现，然后您就可以与他们自由聊天了。



![Image](assets/fr/19.webp)



## 同步桌面软件



要在电脑上同步账户，需要安装软件。[请从官方网站下载](https://getsession.org/download)。我建议您在安装前检查其真实性和完整性。



![Image](assets/fr/20.webp)



首次启动时，点击 "*我有一个账户*"。



![Image](assets/fr/21.webp)



输入 Mnemonic 短语，确保每个单词之间留有空格。



![Image](assets/fr/22.webp)



现在，您可以从电脑访问您的对话。



![Image](assets/fr/23.webp)



恭喜您，现在您已经掌握了会话消息的使用技巧，这是 WathsApp 的绝佳替代品！



我还推荐另一篇教程，其中我介绍了 Threema，这是另一种有趣的信息应用程序替代方案：



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74