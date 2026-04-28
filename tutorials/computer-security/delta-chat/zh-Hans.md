---
name: 三角洲聊天室
description: 去中心化信息传递工具实用指南
---

![image](assets/cover.webp)




## 简介 - 聊天控制和隐私



近年来，关于 "聊天控制"（Chat Control）的讨论越来越多，这是一项旨在对主要通信平台上的私人信息进行自动扫描的监管提案。其既定目标是打击非法内容，问题是这一机制实际上涉及大规模监控，会破坏端到端加密，从而破坏所有用户（而不仅仅是违法者）的隐私。



真正的风险在于，聊天变成了受控环境，每条信息、图片或附件在到达收件人之前都会被仔细检查。而这正是一种可能的解决方案：从集中式平台转向去中心化的信息传输系统，因为去中心化的信息传输系统不依赖于单一的提供商，不容易受到这种审查。



本教程将介绍其中一种解决方案：Delta Chat。这是一款成熟且已投入使用的工具。




## 为什么要使用德尔塔聊天工具及其工作原理



Delta Chat 已经是一款非常适合日常使用的信息解决方案：对于与朋友、家人和其他人聊天非常有用，就像真正的 WhatsApp。



它是一个完全基于电子邮件的去中心化信息传递系统。它基本上利用了传统电子邮件的基础架构，但在此基础上构建了现代即时通讯工具界面和体验。乍一看，这似乎有点即兴，但实际上它运行得非常好，而且强大得出人意料。你可以使用名为 ChatMail 的专用邮件服务器，但它也可以与普通邮件服务器无缝连接。这意味着您可以使用现有账户登录，而无需创建任何新账户。



另一个亮点是对 WebXDC 的支持，WebXDC 是一种小型网络应用程序，可以直接在聊天中使用，类似于 Telegram 中的迷你应用程序。重要的区别在于，这些应用程序不能访问互联网，因此无法跟踪用户或向外部发送数据。



从安全角度来看，Delta Chat 使用经过验证的端到端加密技术，该技术以 PGP 为基础，但进行了现代扩展，使其保护级别可与 Signal 相媲美。目前唯一缺乏的是完美前向保密，但这是一个不断发展的方面。



Delta Chat 完全以电子邮件为基础，完全避免了电子邮件：




- 必填电话号码
- 集中 ID
- 与单一服务相关联的注册



这也是该工具能够抵御聊天控制等侵入性规定的原因。




## 安装



在 [Delta Chat](https://delta.chat/download) 的官方网站上，您可以进入 "下载 "部分。在 Linux 下，可通过 Flathub 方便地下载，但也有 Arch、NixOS、Snap 和独立版本的软件包。



![image](assets/it/01.webp)



它还可用于




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [视窗](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- 和其他商店...



如果您正在寻找 F-Droid 安装指南，本教程可能会对您有所帮助：



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

非常重要的一点是：桌面版不需要手机。与 WhatsApp 或 SimpleX Chat 不同，您不需要先从手机注册。您可以直接在电脑上创建个人档案，也可以从其他设备上传输。




## 创建简介



打开应用程序后，Delta Chat 会询问您是要创建新的个人档案还是使用现有的个人档案。



![image](assets/it/02.webp)



通过创建新的个人资料，您可以输入




- 一个名字
- 图片（可选）



默认情况下是建议使用 ChatMail 服务器，但这是可能的：




- 选择另一个 ChatMail 服务器
- 使用经典电子邮件帐户
- 手动配置 IMAP 和 SMTP
- 使用其他用户的邀请码注册



几秒钟后，配置文件就准备就绪，您就可以开始使用该应用程序了。



![image](assets/it/03.webp)




## Interface 和聊天



界面非常简洁明了：




- 设备信息，即本地通信
- 保存的信息，类似于 Telegram 中的信息，并可在设备间同步



![image](assets/it/04.webp)



要添加联系人，只需




- 显示您的二维码
- 扫描对方的
- 通过链接发出邀请（共享邀请链接）。



![image](assets/it/05.webp)



连接建立后，会自动配置端到端加密。聊天用户界面与 WhatsApp 非常相似：




- 文本和语音信息
- 照片、视频和文件
- 对信息的回复
- 反应
- 弹出消息
- 自定义通知



![image](assets/it/06.webp)



## WebXDC：聊天中的应用程序：



Delta Chat 允许使用 WebXDC，即嵌入到对话中的小型应用程序。以下是已确认的最有用应用程序的简短列表：




- 调查
- 绘图板
- 临时私人聊天
- 共享聊天分数的游戏



还可以启动更复杂的游戏，这体现了该工具的灵活性。



![image](assets/it/07.webp)



## 组、频道和高级功能



您可以创建群组、使用贴纸（尤其是在桌面上），如果激活实验选项，甚至还可以创建与 Telegram 类似的频道。



在高级设置中，您可以打开




- 语音通话（仍在试验阶段）
- 高级电子邮件档案管理
- 完整备份。



![image](assets/it/08.webp)



## 多设备和备份



Delta Chat 完全支持多设备：




- 您可以通过 QR 码添加第二个设备
- 您可以通过备份执行完全传输。



无需依赖中央服务器，只需几秒钟，您就能重新找到您的聊天记录、群组和完整的历史记录。



![image](assets/it/09.webp)




## 结论



在人们越来越多地谈论控制私人通信的时候，Delta Chat 代表了一个具体的答案：去中心化的加密信息，真正每天都能使用。



在我尝试过的所有解决方案中，这是最让我信服的简单、隐私和自由的解决方案。如果您愿意，也可以通过以下 [邀请链接](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats) 在 Delta Chat 上与我联系



如果您喜欢本指南，可以通过捐款和竖起大拇指来支持我。请记住：只有通过在手机和桌面上使用和探索 Delta Chat，您才能真正发现它的全部功能。



下次再见