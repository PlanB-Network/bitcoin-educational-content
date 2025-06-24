---
name: 特雷玛
description: 安全的匿名即时消息
---
![cover](assets/cover.webp)



Threema 于 2012 年在瑞士成立，是一款旨在保证隐私和安全的即时通讯应用程序。与 WhatsApp、Telegram 或 Signal 不同，Threema 无需电话号码或电子邮件 Address 即可创建账户。每个用户都有一个唯一的标识符，实现完全匿名注册。



在技术方面，通过 Threema 进行的通信是端到端加密的。移动应用程序代码自 2020 年起开放源代码，但服务器基础设施仍然是专有和集中式的。服务器完全托管在瑞士（瑞士因其数据保护法律框架而闻名）。



![Image](assets/fr/01.webp)



Threema 有安卓和 iOS 的基本客户端。此外，还有网络应用程序以及适用于 Windows、Linux 和 macOS 的软件。不过，要使用这些软件，您必须先在移动设备上注册。



Threema 应用程序不是免费的。它采用一次性购买模式：5.99 欧元可终身使用该应用程序（如果直接购买，则为 4.99 欧元）。要真正匿名使用 Threema，支付也需要匿名。因此，您可以在 "*Threema 商店*"上用比特币或现金购买激活密钥，以激活安卓版本。而在 iOS 上，由于苹果公司对应用程序货币化的限制，必须通过 App Store 购买。



此外，还有一个名为 "*Threema Work*"的专用商业版本。在本教程中，我们将重点介绍家庭版。



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



## 安装 Threema 应用程序



Threema 适用于所有平台。您可以直接从手机应用商店下载该应用程序：




- [Google Play]（https://play.google.com/store/apps/details?id=ch.threema.app）；
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/)；
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829)；
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



在 Android 上，也可以 [通过 APK 安装](https://shop.threema.ch/en/download)。



还有 [电脑版本](https://threema.ch/download) （MacOS、Linux 和 Windows）。本教程将告诉你如何同步它们。



## 购买 Threema 许可证



安装应用程序后，如果您是直接通过应用程序商店安装的，那么您已经支付了许可证费用，应该可以立即使用。如果通过 F-Droid 或 APK 安装，则需要在官方网站上购买许可证。



[前往 "*Threema 商店*"(https://shop.threema.ch/)，点击 "*购买安卓版 Threema*"按钮。



![Image](assets/fr/02.webp)



选择您希望购买的许可证数量（如果只为您购买一个），选择货币，并选择许可证交付方式。您可以选择通过电子邮件或直接在网站上匿名接收许可证。然后点击 "*继续付款*"。



![Image](assets/fr/03.webp)



选择付款方式。在我的情况下，我要用比特币支付，我也建议你这样做，因为它可以让你保持匿名（只要你适当使用 Bitcoin），而且比远程现金支付方便得多。然后点击 "*下一步*"。



![Image](assets/fr/04.webp)



如果不需要 Invoice，请再次点击 "*下一步*"，无需输入任何个人信息。



然后点击 "*确认付款*"确认购买。



![Image](assets/fr/05.webp)



然后，您需要将指定的金额发送到所提供的 Bitcoin Address（不幸的是，目前还不支持 "闪电"）。在 Blockchain 上确认交易后，点击 Invoice 旁边的 "*关闭*"。



然后您就可以获取许可证密钥。请注意：如果您没有输入电子邮件 Address，密钥只会显示在这里。记住保存该页面的 URL，以便日后访问。



![Image](assets/fr/06.webp)



## 在 Threema 上创建账户



有了许可证密钥，你就可以启动应用程序了。首次启动时，如果您没有通过应用程序商店购买 Threema，系统会要求您输入在网站上购买的许可证密钥。



![Image](assets/fr/07.webp)



然后点击 "*立即设置*"按钮。



![Image](assets/fr/08.webp)



在屏幕上移动手指，可获得 generate 个熵源，用于创建您的 "*Threema ID*"。



![Image](assets/fr/09.webp)



然后就会显示您的 "*Threema ID*"。通过它，您可以与其他用户取得联系。点击 "*下一步*"。



![Image](assets/fr/10.webp)



选择密码。如果有必要，它可以让你恢复对账户的访问。密码要尽可能长且随机，并保存一份安全的副本，例如放在密码管理器中。



![Image](assets/fr/11.webp)



然后选择一个用户名，可以是真名，也可以是化名。



![Image](assets/fr/12.webp)



然后，您就可以将您的 Threema ID 与您的电话号码联系起来。这样可以方便您搜索联系人，但如果您使用 Threema，这也是为了保护您的匿名性：所以最好不要链接。点击 "*下一步*"。



![Image](assets/fr/13.webp)



完成此步骤后，点击 "*完成*"。



![Image](assets/fr/14.webp)



现在您已经连接到 Threema，可以开始通信。



![Image](assets/fr/15.webp)



## 设置 Threema



首先，点击右上角的三个小圆点进入设置，然后选择 "*设置*"。



![Image](assets/fr/16.webp)



在 "*隐私*"选项卡中，你可以找到几个选项，根据自己的需要进行调整：




- 同步手机上的联系人 ；
- 接受来自陌生人的信息；
- 数据录入过程中的书写指示符 ；
- 信息接收通知...



![Image](assets/fr/17.webp)



在 "*安全*"选项卡中，我建议激活 "*锁定机制*"选项，以保护对应用程序的访问。此外，还建议激活 passphrase，以确保本地备份的安全。



![Image](assets/fr/18.webp)



您可以自由探索设置的其他部分，根据自己的喜好定制应用程序。



![Image](assets/fr/19.webp)



## 备份您的 Threema 账户



在开始交换信息之前，重要的是要计划好恢复账户的方法，尤其是在手机更换或丢失的情况下。为此，请单击 Interface 右上方的三个点，然后进入 "*备份*"菜单。



![Image](assets/fr/20.webp)



这里有两个备份数据的选项：




- "*特雷玛安全*"；
- "*数据备份*"。



"Threema Safe* 在 Threema 的服务器上保存您所有的账户信息，但您的对话除外。这些数据使用您创建账户时选择的密码进行加密，确保 Threema 无法访问。我们会定期自动备份。



使用 "*Threema Safe*"，您只需输入 "*Threema ID*"和密码即可在新设备上恢复账户。如果缺少这两个信息中的任何一个，就无法恢复账户。



此选项只允许您检索您的 ID、个人资料、联系人、群组和某些设置，但**不能检索您的对话历史记录**。



要激活 "*Threema Safe*"，只需选中 "*备份*"菜单中的选项即可。



![Image](assets/fr/21.webp)



如果还想备份和恢复通话记录，则需要使用 "*数据备份*"选项。这会生成一个完整的账户备份，存储在手机本地。您需要将此备份转移到新设备上，然后使用密码（可能还有 passphrase）恢复整个账户。



由于该备份只是本地备份，因此需要定期复制到外部介质上。否则，一旦设备丢失，将无法恢复。因此，这种方法最适合有计划地从一个设备转移到另一个设备，而不是紧急情况。



请注意："*数据备份*"仅在使用相同操作系统时有效。例如，您无法使用它从三星迁移到 iPhone。



## 定制您的 Threema 个人资料



在 Interface 的左上角，点击您的个人资料图片，然后选择 "*我的个人资料*"。



![Image](assets/fr/22.webp)



在这里，您可以自定义您的个人资料：添加照片、选择查看对象或查看您的 Threema 登录信息。



![Image](assets/fr/23.webp)



## 同步 PC 软件



如果您想在电脑上访问您的对话，可以使用专用软件同步您的 Threema 账户。从官方网站](https://threema.ch/en/download) 下载适用于您操作系统的软件。



![Image](assets/fr/24.webp)



在手机上点击右上角的三个点，然后打开 "*Threema 2.0 for Desktop*"菜单。



![Image](assets/fr/25.webp)



点击 "*添加设备*"，然后用手机扫描电脑上软件显示的二维码。



![Image](assets/fr/26.webp)



要确认同步，请单击软件中显示的表情符号组。



![Image](assets/fr/27.webp)



在电脑上使用密码登录。



![Image](assets/fr/28.webp)



除了移动应用程序，您现在还可以直接从电脑访问您的 Threema 账户。



![Image](assets/fr/29.webp)



## 使用 Threema 发送信息



现在一切设置正确，您可以开始聊天了。点击 "*开始聊天*"按钮。



![Image](assets/fr/30.webp)



选择 "*新联系人*"。



![Image](assets/fr/31.webp)



输入或扫描通讯员的 "*Threema ID*"。



![Image](assets/fr/32.webp)



点击信息图标。



![Image](assets/fr/33.webp)



给通讯员发送第一条信息。



![Image](assets/fr/34.webp)



当你的联系人回复时，连接就会建立，你就可以看到他或她的姓名和个人照片。然后，您就可以发送 Exchange 消息、多媒体文件，甚至拨打电话。



![Image](assets/fr/35.webp)



恭喜您，现在您已经掌握了 Threema 消息传递的使用方法，它是 WathsApp 的绝佳替代品！如果您觉得本教程有用，请在下方留下 Green 大拇指，我将不胜感激。欢迎在您的社交网络上分享本教程。非常感谢



我还向你推荐另一篇教程，其中我向你介绍了质子邮件（Proton Mail），它是 Gmail 的替代品，对隐私更加友好：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2