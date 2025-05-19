---
name: 奥尔维德
description: 为每个人提供私人信息
---
![cover](assets/cover.webp)



Olvid 是一款法国即时通讯应用程序，于 2019 年推出，旨在提供高度安全性，同时不影响隐私。与 WhatsApp 或 Signal 不同，Olvid 在注册时不要求提供任何个人数据：没有电话号码，没有电子邮件，什么都没有。用户之间的身份识别基于密钥 Exchange，没有目录服务器或共享 Address 本。



所有信息都使用独创的加密协议进行端到端加密，旨在保护元数据：没有人知道你在和谁通话，也没有人知道什么时候在和谁通话。客户端代码是开源的，但用于路由加密信息的中央服务器仍是专有的，托管在 AWS 上。



Olvid 提供免费版本和每月 4.99 欧元的订阅版本。免费版功能齐全，但不能拨打音频和视频电话（不过可以接听），也不能在多台设备上同步账户。因此，如果你只打算使用智能手机，不需要拨打电话，Olvid 是一个很好的解决方案。



Olvid 已通过 ANSSI（法国网络安全机构）认证。该应用程序是传统信息服务（WhatsApp、Facebook Messenger、微信......）的绝佳替代品，既能保护隐私，又能保持简单易用。



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
| **Olvid**                | **✅**              | **✅**              | **✅**                   | **✅**                          | **❌**                           | **❌**                    | **2019**              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = 端到端加密*。



## 安装 Olvid 应用程序



Olvid 适用于所有平台。您可以直接从手机应用商店下载该应用程序：




- [Google Play]（https://play.google.com/store/apps/details?id=io.olvid.messenger）；
- [App Store](https://apps.apple.com/app/olvid/id1414865219)；



在 Android 上，也可以 [通过 APK 安装](https://www.olvid.io/download/)。



在本教程中，我们将重点介绍手机版，但请注意，[电脑版也可用](https://www.olvid.io/download/) （MacOS、Linux 和 Windows）。如果你选择付费版本，就可以在多个设备上同步你的账户。



![Image](assets/fr/01.webp)



## 在 Olvid 上创建账户



首次启动应用程序时，请点击 "*我是新用户*"按钮。



![Image](assets/fr/02.webp)



选择昵称或输入您的名字和姓氏。



![Image](assets/fr/03.webp)



添加个人照片



![Image](assets/fr/04.webp)



您的账户现已创建。



![Image](assets/fr/05.webp)



为防止您的 Olvid 账户访问权限丢失，我们建议您设置自动备份。为此，请单击 Interface 右上方的三个点打开设置，然后选择 "*设置*"。



![Image](assets/fr/06.webp)



进入 "*保存按键和联系人*"菜单。



![Image](assets/fr/07.webp)



然后点击 "*generate 备份密钥*"。该密钥将对备份进行加密。如果您需要在其他设备上恢复账户，但又无法再访问该账户，则需要备份和此密钥才能解密。



![Image](assets/fr/08.webp)



将这把钥匙放在安全的地方。您也可以制作一份纸质副本。



![Image](assets/fr/09.webp)



然后，您可以选择创建本地备份或在云服务上创建自动备份。强烈建议使用第二种方法，以确保在任何情况下都能访问您的 Olvid 账户，即使手机丢失也是如此。



![Image](assets/fr/10.webp)



确保选中 "*启用自动备份*"选项。



![Image](assets/fr/11.webp)



您还可以探索其他可用设置，根据自己的需要定制应用程序。



![Image](assets/fr/12.webp)



## 使用 Olvid 发送信息



要发送信息，必须先添加联系人。在主页上点击蓝色的 "*+*"按钮。



![Image](assets/fr/13.webp)



Olvid 会显示你的用户 ID。然后，您就可以把它转发给您希望与之交流的人，让他们把您添加为联系人。



要添加一个人，请用相机扫描其身份证，或点击右上角的三个小圆点手动粘贴。



![Image](assets/fr/14.webp)



扫描 ID 后，您可以让联系人扫描显示的二维码，或者点击 "*远程联系人*"向他们发送远程连接请求。



![Image](assets/fr/15.webp)



连接现已建立。



![Image](assets/fr/16.webp)



现在您可以开始与您的联系人交换信息和其他内容！



![Image](assets/fr/17.webp)



在主页上，您可以找到所有对话。



![Image](assets/fr/18.webp)



第二个选项卡包含所有联系人。



![Image](assets/fr/19.webp)



您还可以创建小组讨论。



![Image](assets/fr/20.webp)



恭喜您，现在您已经掌握了 Olvid 消息传递的使用方法，它是 WathsApp 的绝佳替代品！如果您觉得本教程有用，请在下方留下 Green 大拇指，我将不胜感激。请随时在您的社交网络上分享本教程。非常感谢



我还向你推荐另一篇教程，其中我向你介绍了质子邮件（Proton Mail），它是 Gmail 的替代品，对隐私更加友好：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2