---
name: 信号
description: 自由表达
---
![cover](assets/cover.webp)



Signal 是一款端到端加密信息应用程序，默认情况下具有良好的保密性。每条信息、通话和文件都受到 Signal 协议的保护，该协议是公认的最强大的信息传输协议之一。它被许多其他应用程序重复使用，包括用于 RCS 通信的 WathsApp、Facebook Messenger、Skype 和 Google Messages。



Signal 由 Moxie Marlinspike（化名）于 2014 年推出，自 2018 年起由 Signal 基金会开发，该基金会是在布莱恩-阿克顿（WhatsApp 联合创始人）支持下创建的非营利组织。



![Image](assets/fr/01.webp)



与 WhatsApp 相比，Signal 的突出之处在于它的透明度：应用程序的代码，包括客户端和服务器端，都是完全开源的。这使得任何人都可以对其进行审计，尤其是检查加密是否如宣传的那样应用。



不过，Signal 依赖于电话号码的使用，与其他解决方案相比，这是它在匿名性方面的主要弱点。尽管如此，在我看来，该应用程序在安全性和保密性方面是最可靠的，这要归功于它完全开放的架构和广泛采用的加密协议，因此，与其他更边缘化的应用程序不同，它是经过测试和审核的。



| 应用程序             | E2EE 1:1       | E2EE 群组      | 匿名注册            | 开源客户端许可证             | 开源服务器许可证             | 去中心化服务器       | 创建年份          |
| -------------------- | -------------- | -------------- | ------------------- | ---------------------------- | ---------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                            | ❌                            | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (可选)      | ❌                   | ❌                            | ❌                            | ❌                    | 2011              |
| Telegram             | 🟡 (可选)      | ❌              | 🟡                  | ✅                            | ❌                            | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                            | ✅                            | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                            | ❌                            | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (联邦式)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                            | N/A                          | 🟡 (通过邮件)        | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (联邦式)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                            | ❌                            | 🟡(无目录)          | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                            | N/A                          | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                    | 2013              |

*E2EE = 端到端加密*。




## 安装 Signal 应用程序



Signal 适用于所有平台。您可以直接从手机的应用程序商店下载该应用程序：




- [Google Play]（https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms）；
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669)；



在 Android 上，也可以 [通过 APK 安装](https://github.com/signalapp/Signal-Android/releases)。



在本教程中，我们将重点介绍手机版，但请注意，[桌面版也可用](https://signal.org/fr/download/) （MacOS、Linux 和 Windows）。不过，在将账户与桌面版同步之前，您需要先设置移动应用程序。



## 在 Signal 上创建账户



首次启动应用程序时，请单击 "*继续*"按钮。



![Image](assets/fr/02.webp)



输入电话号码，然后点击 "*下一步*"。



![Image](assets/fr/03.webp)



系统将通过短信向您发送验证码。请在 Signal 应用程序中输入此验证码。



![Image](assets/fr/04.webp)



选择一个 PIN 码来保护你的 Signal 账户。该密码会对你的数据进行加密，如果你的设备丢失，可以用它来恢复对你账户的访问。因此，选择一个尽可能长且随机的 PIN 码并保存可靠的记录非常重要。



![Image](assets/fr/05.webp)



再次确认 PIN 码。



![Image](assets/fr/06.webp)



您现在可以个性化您的用户配置文件。选择一张照片，输入你的名字或昵称。在这个阶段，你还可以定义谁可以通过你的号码在 Signal 上找到你。如果你想让别人看到你，请选择 "*Everyone*"；如果你想让别人无法通过电话号码找到你，请选择 "*Nobody*"（这样就只能用 "*用户名*"来添加你）。选择完毕后，点击 "*下一步*"。



![Image](assets/fr/07.webp)



现在您已连接到 Signal，并准备好发送 Exchange 消息。



![Image](assets/fr/08.webp)



## 设置您的 Signal 账户



点击左上角的个人照片，进入应用程序设置。



![Image](assets/fr/09.webp)



通过 "*账户*"菜单，您可以管理个人资料设置。我建议您保留默认设置。您还可以激活 "*注册锁定*"选项，该选项可以保护您的账户免受某些类型的攻击。该菜单还包含将账户转移到新设备所需的选项。



![Image](assets/fr/10.webp)



再次点击设置中的个人资料图片，您就可以进入个性化个人资料选项。我建议您设置一个 "*用户名*"：这样您就可以在不暴露电话号码的情况下与其他人取得联系。



![Image](assets/fr/11.webp)



通过选择 "*QR 代码或链接*"，您将获得与想要添加您到 Signal 的人分享所需的信息。



![Image](assets/fr/12.webp)



隐私*"菜单尤为重要。在这里，您可以找到控制号码可见性、管理与联系人的信息以及在应用程序上授予各种授权的选项。



![Image](assets/fr/13.webp)



您还可以自由探索 "*外观*"、"*聊天*"和 "*通知*"菜单，根据个人需要调整 Interface 和应用程序的操作。



## 连接桌面应用程序



要连接桌面应用程序，首先要在电脑上安装软件（参见本教程的第一部分）。然后，在手机上进入 "设置"，打开 "*已连接设备*"部分。



![Image](assets/fr/14.webp)



点击 "*链接新设备*"按钮。



![Image](assets/fr/15.webp)



在电脑上启动软件，然后用手机扫描屏幕上显示的二维码。如果要导入通话记录，请选择 "*传输信息历史记录*"选项。



![Image](assets/fr/16.webp)



现在，您的设备已完全同步。



![Image](assets/fr/17.webp)



## 使用 Signal 发送信息



要在 Signal 上与某人通信，首先需要将其添加为联系人。有几种选择：你可以通过电话号码添加（如果对方激活了通过这种方式查找的选项），或者使用对方的 Signal ID。



点击 Interface 右下角的铅笔图标。



![Image](assets/fr/18.webp)



就我而言，我想按用户名添加人。因此，我点击了 "*按用户名查找*"。



![Image](assets/fr/19.webp)



然后，您可以粘贴登录信息或扫描二维码。



![Image](assets/fr/20.webp)



给他发信息建立联系。



![Image](assets/fr/21.webp)



对话将显示在主页上。如果对方接受了你的联系请求，你将看到对方的姓名和个人照片。



![Image](assets/fr/22.webp)



恭喜你，现在你已经掌握了 Signal 消息的使用方法，它是 WathsApp 的绝佳替代品！如果你觉得本教程有用，请在下方留下 Green 大拇指，我将不胜感激。欢迎在你的社交网络上分享本教程。非常感谢



我还向你推荐另一篇教程，其中我向你介绍了质子邮件（Proton Mail），它是 Gmail 的替代品，对隐私更加友好：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2