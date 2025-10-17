---
name: Bitcoin 和 BTC 支付服务器
goal: 为您的企业安装 BTC Pay 服务器
objectives: 

  - 了解什么是 btcpayserver。
  - 自行托管和配置 BTC Pay 服务器。
  - 在日常业务中使用 btcpayserver。

---

# Bitcoin 和 BTCPay 服务器


这是关于 BTCPay 服务器操作员的入门课程，由 Alekos 和 Bas 编写，并由 melontwist 和 asi0 根据 Plan ₿ 课程格式进行了改编。


后话


"这是谎言，我对你的信任破灭了，我要让你过时"。


由 BTCPay 服务器基金会制作


+++

# 导言


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## 课程概览


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


欢迎来到 BTCPay 服务器上的 POS 305 课程！


本培训的目的是教您如何在企业或组织内安装、配置和使用 BTCPay 服务器。BTCPay Server 是一个开源解决方案，可让您自主、安全、经济高效地处理 Bitcoin 支付。本课程主要面向希望掌握 BTCPay Server 自主托管并将其完全集成到日常运营中的高级用户。


**第 1 部分：BTCPay 服务器简介**

我们将从 BTCPay Server 的一般介绍开始，包括登录屏幕、用户账户管理和创建新商店。该介绍将帮助您了解 BTCPay Server Interface 并掌握开始使用该工具所需的基本功能。


**第 2 部分：Bitcoin 密钥安全简介**

Bitcoin 资金的安全非常重要。在本节中，我们将探讨加密密钥的生成、使用硬件钱包保护这些密钥，以及如何通过 BTCPay 服务器与您的密钥进行交互。您还将学习如何配置 BTCPay Server Lightning Wallet，以优化您的交易。


**第 3 部分：BTCPay 服务器 Interface**

本部分将指导您了解 BTCPay 服务器的用户 Interface。您将学习如何浏览仪表板、配置商店和服务器设置、管理支付以及利用集成插件。我们的目标是为您提供必要的工具，以便根据您的具体需求定制安装。


**第 4 部分：配置 BTCPay 服务器**

最后，我们将重点介绍如何在各种环境中实际安装 BTCPay 服务器。无论您使用的是 LunaNode、Voltage 还是 Umbrel 节点，您都将学到部署和配置 BTCPay 服务器的基本步骤，同时考虑到每个环境的具体情况。


准备好掌握 BTCPay 服务器并发展您的业务了吗？开始吧


## 作者的 Bitcoin 和 BTCPay 服务器广受好评


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


让我们从了解 BTCPay 服务器及其起源开始。我们重视透明度和特定标准，以便在 Bitcoin 领域形成信任。

该领域的一个项目破坏了这些价值观。BTCPay 服务器的首席开发者尼古拉斯-多里埃尔（Nicolas Dorier）对此耿耿于怀，并承诺废除这些价值观。多年后的今天，我们每天都在努力实现这个完全开源的未来。


> 这是谎言，我对你的信任破灭了，我会让你过时的。
> 尼古拉-多里耶

尼古拉斯说完这些话后，我们就开始建设了。我们在 BTCPay 服务器上做了大量工作。更多的人希望为这项工作做出贡献。其中最著名的有 r0ckstardev、MrKukks、Pavlenex 和第一个使用该软件的商家 astupidmoose。


什么是开放源代码？


FOSS 是自由与开源软件的缩写。前者是指允许任何人复制、修改甚至分发软件版本（甚至以盈利为目的）。后者是指公开共享源代码，鼓励公众贡献和改进软件。

这吸引了经验丰富的用户，他们热衷于为自己已经在使用并从中获得价值的软件做出贡献，最终被证明比专有软件更容易被采用。它符合 Bitcoin 的精神，即 "信息渴望自由"。它将充满热情的人们聚集在一起，形成一个社区，而且更有趣。与 Bitcoin 一样，自由和开放源码软件是不可避免的。


### 在我们开始之前


本课程由多个部分组成。许多部分将由您的任课老师负责，您可以访问的演示环境、您自己的托管服务器以及可能的域名。如果您独立完成本课程，请注意您将无法使用标有 DEMO 的环境。

注意。如果您在教室中学习本课程，服务器名称可能因教室设置而异。因此，服务器名称中的变量可能会有所不同。


### 课程结构


每一章都有目标和知识评估。在本课程中，我们将逐一介绍这些内容，并在每个课块（即章节）的结尾提供关键特征总结。插图的特点是提供视觉反馈，并从视觉方面强化关键概念。每个课块的开头都设定了教学目标。这些目标不仅仅是一份清单。它们为你提供了一套新技能的指南。随着 BTCPay 服务器设置的完成，知识评估将逐步增加难度。


### 学生可以获得哪些课程？


通过 BTCPay 服务器课程，学生可以了解 Bitcoin 的基本原理、技术和非技术。通过 BTCPay 服务器使用 Bitcoin 的广泛培训，学员可以操作自己的 Bitcoin 基础设施。


### 重要网址或联系机会


允许 Alekos 和 Bas 编写本课程的 BTCPay 服务器基金会位于日本东京。可通过所列网站联系 BTCPay 服务器基金会。



- https://foundation.btcpayserver.org
- 加入官方聊天频道： https://chat.btcpayserver.org


## Bitcoin 简介


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### 通过课堂练习了解 Bitcoin


这是一项课堂练习，因此，如果您自己参加了这门课程，您就不能进行这项练习，但您仍然可以完成这项练习。要完成这项任务，至少需要 9 到 11 人。


在观看了 BBC 制作的 "Bitcoin 和 Blockchain 如何工作 "介绍后，练习开始。


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


本练习至少需要九名参与者。本练习旨在让大家实际了解 Bitcoin 的工作原理。通过扮演网络中的每个角色，您将以互动和游戏的方式进行学习。本练习不涉及 Lightning Network。


### 举例说明：需要 9 / 11 人


这些角色是



- 1 名客户
- 1 商人
- 7 至 9 个 Bitcoin 节点


**设置如下：**


顾客在 Bitcoin 商店购买产品。


**情景 1 - 传统银行系统**



- 设置：
  - 请参阅所附 Figjam - [活动示意图](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) 中的图表/说明。
  - 请三名学生志愿者分别扮演顾客 (Alice)、商人 (Bob) 和银行。
- 表演事件发生的顺序：
  - 顾客--在网上浏览商店，发现一件价值 25 美元的商品，并告知商家他们想要购买。
  - 商人 - 要求付款。
  - 客户向商家发送银行卡信息
  - 商户 - 将信息转发给银行（同时确认商户本人和商户的身份/信息），要求支付
  - 银行收集客户和商户信息（Alice 和 Bob），并检查客户余额是否充足。
  - 从 Alice 的账户中扣除 （25）美元，在 Bob 的账户中增加 （24）美元，收取 （1）美元的服务费
  - 商家收到银行的 "大拇指 "后，就会将商品寄给客户。
- 评论：
  - Bob 和 Alice 必须与银行有关系。
  - 银行收集了 Bob 和 Alice 的身份信息。
  - 班克被砍了一刀
  - 必须信任银行，随时保管每位参与者的资金。


**情景 2 - Bitcoin 系统**



- 设置：
  - 请参阅所附 Figjam - [活动示意图](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) 中的图表/说明。
  - 用九名学生取代银行，他们将在网络中扮演计算机（Bitcoin 节点/用户）的角色，以取代银行。
- 9 台计算机中的每一台都有过去所有交易的完整历史记录（因此，余额准确无误，不会造假），还有一套规则：
  - 验证交易已正确签名 (thekeyfitsthelock)
  - 向网络中的同行发送并接收有效交易，丢弃无效交易（包括任何试图花费相同资金两次的交易）
- 如果 "随机 "计算机发送的新交易内容全部有效，则定期更新/添加记录（注意：为简单起见，我们暂时忽略 Proof of Work 部分），否则拒绝接受这些记录，并继续执行之前的操作，直至下一台 "随机 "计算机发送更新信息
  - 如果内容有效，就会得到适当的奖励。
- 表演事件发生的顺序：
  - 顾客--在网上浏览商店，发现一件价值 25 美元的商品，并告知商家他们想要购买。
  - 商家--要求客户从其 Wallet 发送 Invoice/Address 付款。
  - 客户构建交易（向商家提供的 Address 发送价值 25 美元的 BTC）并将其发送到 Bitcoin 网络。
- 计算机--接收交易并验证：
  - Address 中至少有 25 美元的 BTC 来自
  - 交易签名正确（客户 "解锁"）。
  - 如果不是，则交易不会在网络中传播；如果是，则会传播并处于等待状态。
  - 商户可查看交易是否处于待处理和等待状态。
- 一台计算机被 "随机 "选中，提议通过广播包含交易的 "区块 "来最终完成提议的交易；如果交易成功，他们将获得 BTC 奖励。
  - 可选/增强功能--不随机选择计算机，而是通过让计算机掷骰子来模拟 Mining，直到出现某种预定结果（例如，第一个掷出双六的计算机被选中）
  - 它还可以演算出如果两台计算机大约同时获胜会发生什么情况，从而导致连锁分裂。
  - 计算机检查有效性，如果符合规则，则更新/添加记录到分类账，并向同行广播交易块。
  - 随机选择的计算机会因为提出一个有效区块而获得奖励。
  - 商户支票交易已完成；因此，资金已收到，物品已发送给客户。
- 评论：
  - 请注意，不需要预先存在银行关系。
  - 无需第三方提供便利；由代码/激励措施取代。
  - 直接 Exchange 以外的任何人不得收集数据，参与者之间必须只交换必要的数量（如运输 Address）。
  - 人与人之间不需要信任（发送物品的商家除外），在很多方面与现金购买类似。
  - 资金直接归个人所有。
  - 为简单起见，Bitcoin Ledger 用美元表示，但实际上是 BTC。
  - 我们模拟的是单笔交易的广播，但实际上，网络中会有多笔交易待处理，区块中会同时包含数千笔交易。节点还会验证是否有重复支出的交易待处理（在这种情况下，除了一个交易外，我会放弃所有交易）。
- 作弊情景：
  - 如果客户没有 25 美元的 BTC 呢？
    - 他们无法创建交易，因为 "解锁 "和 "Ownership "是一回事，计算机会检查交易是否正确签名，否则就会拒绝交易。
  - 如果随机选择的计算机试图 "改变 Ledger"，该怎么办？
    - 该拦截将被拒绝，因为其他每台计算机都有完整的历史记录，会注意到这一变化，从而违反它们的规则之一。
    - 随机计算机不会获得奖励，其区块中的交易也不会最终完成。


## 知识评估


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA 课堂讨论


讨论第二种情况下课堂练习中的一些过度简化，并更详细地描述 Bitcoin 系统的实际作用。


### KA 词汇复习


定义上一节介绍的以下关键术语：



- 节点
- Mempool
- 难度目标
- 街区


**集体讨论一些补充术语的含义：**


Blockchain、交易、双重支出、拜占庭将军问题、Mining、Proof of Work (PoW)、Hash 函数、Block reward、Blockchain、最长链、51% 攻击、输出、输出锁、更改、Satoshis、公钥/私钥、Address、公钥密码学、数字签名、Wallet


# BTCPay 服务器介绍


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## 了解 BTCPay 服务器登录屏幕


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### 使用 BTCPay 服务器


本课程块的目标是获得对 BTCPay Server 软件的一般了解。在共享环境中，建议您跟随教师的演示，并参考 BTCPay Server 课程手册，与教师一起学习。您将学习如何通过多种方法创建 Wallet。示例包括 Hot Wallet 设置和通过 BTCPay Server Vault 连接的硬件钱包。这些目标将在演示环境中实现，由课程教师展示并提供访问权限。


如果您自己学习本课程，您可以在 https://directory.btcpayserver.org/filter/hosts 找到用于演示的第三方主机列表。我们强烈建议不要将这些第三方选项用作生产环境；不过，这些选项可用于介绍 Bitcoin 和 BTCPay 服务器的使用。


作为 BTCPay Server 摇滚明星学员，您可能以前有过设置 Bitcoin 节点的经验。本课程专为 BTCPay 服务器软件栈量身定制。


BTCPay 服务器中的许多选项都以某种形式存在于其他 Bitcoin Wallet 相关软件中。


### BTCPay 服务器登录屏幕


欢迎您进入演示环境，系统会要求您 "登录 "或 "创建账户"。出于安全原因，服务器管理员可能会禁用创建新账户的功能。BTCPay服务器的标识和按钮颜色可以更改，因为BTCPay服务器是开源软件。第三方主机可以对软件进行白标，并改变整个外观。


![image](assets/en/001.webp)


### 创建账户窗口


在 BTCPay 服务器上创建账户需要有效的电子邮件 Address 字符串；example@email.com 是电子邮件的有效字符串。


密码长度至少为 8 个字符，包括字母、数字和字符。设置一次密码后，您必须验证密码是否与在第一个密码字段中输入的密码相同。


正确填写电子邮件和密码后，点击 "创建账户 "按钮。这将在教师的 BTCPay 服务器实例中保存电子邮件和密码。


![image](assets/en/002.webp)


**注意！**


如果您独立学习本课程，很可能要在第三方主机上创建此账户；因此，我们再次强调，这些账户不应被用作生产环境，而只能用于培训目的。


### 由 BTCPay 服务器管理员创建账户


BTCPay服务器实例的管理员也可以为BTCPay服务器创建账户。BTCPay 服务器实例的管理员可以点击 "服务器设置"(1)，点击 "用户 "选项卡(2)，然后点击用户选项卡右上方的 "+ 添加用户 "按钮(3)。在目标（4.3）中，您将了解更多关于管理员控制账户的信息。


![image](assets/en/003.webp)


作为管理员，您需要用户的电子邮件 Address 并设置标准密码。出于安全考虑，建议管理员通知用户在使用账户前更改密码。如果管理员没有设置密码，而服务器上又配置了 SMTP，用户将收到一封电子邮件，其中包含一个邀请链接，让用户自己创建账户和设置密码。


### 示例


与教师一起学习课程时，请按照教师提供的链接在演示环境中创建自己的账户。确保安全保存您的电子邮件 Address 和密码；在本课程的其余演示目标中，您将需要这些登录凭证。


在本次练习之前，您的指导老师可能已经提前收集了电子邮件 Address，并发送了邀请链接。如有指示，请查看您的电子邮件。


在没有教师指导的情况下学习课程时，请使用 BTCPay Server 演示环境创建账户；请访问


https://Mainnet.demo.btcpayserver.org/login。


该账户只能用于演示/培训目的，不得用于商业用途。


### 技能概要


在本节中，您将学到以下内容：



- 如何通过 Interface 在托管服务器上创建账户。
- 服务器管理员如何在服务器设置中手动添加用户。


### 知识评估


#### KA 概念审查


说明将演示服务器用于生产目的不是好主意的原因。


## 管理用户账户


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### BTCPay 服务器上的账户管理


店主创建账户后，可在 BTCPay 服务器用户界面的左下方进行管理。账户按钮下方有多个高级设置。



- 暗/亮模式
- 隐藏敏感信息切换。
- 管理账户。


![image](assets/en/004.webp)


### 深色和浅色模式


BTCPay 服务器的用户可以选择浅色或深色模式版本的用户界面。面向客户的页面不会改变。它们使用客户首选的暗模式或亮模式设置。


### 隐藏敏感信息切换


隐藏敏感信息按钮提供了一个快速、简单的安全Layer。当您需要操作 BTCPay 服务器，但在公共场所可能有人从您的肩上潜伏过去时，打开 "隐藏敏感信息 "按钮，BTCPay 服务器中的所有数值都将被隐藏。别人或许可以从您的肩膀上看到，但却无法再看到您正在处理的数值。


### 管理账户


创建用户账户后，就可以在这里管理密码、2FA 或 API 密钥。


### 管理账户 - 账户


可选择使用不同的电子邮件 Address 更新您的账户。为确保您的电子邮件 Address 正确无误，BTCPay 服务器允许您发送验证电子邮件。如果用户设置了新的电子邮件 Address，并确认验证成功，请单击保存。用户名仍与之前的电子邮件相同。


用户可以决定删除自己的整个账户。点击 "账户 "选项卡上的 "删除 "按钮即可。


![image](assets/en/005.webp)


**注意！**


更改电子邮件后，账户的用户名不会改变。之前给定的电子邮件 Address 将保留为登录名。


### 管理帐户 - 密码


学生可能想更改密码。他可以进入 "密码 "选项卡进行更改。在这里，他需要输入旧密码，并可将其更改为新密码。


![image](assets/en/006.webp)


### 双因素身份验证 (2fa)


为了限制密码被盗造成的后果，可以使用双因素身份验证 (2FA)，这是一种相对较新的安全方法。您可以通过 "管理帐户 "和 "双因素身份验证 "选项卡激活双因素身份验证。使用用户名和密码登录后，您必须完成第二个步骤。


BTCPay 服务器支持两种启用 2FA 的方法：基于应用程序的 2FA（Authy、Google、Microsoft Authenticators）或通过安全设备（FIDO2 或 LNURL Auth）。


### 双因素身份验证 - 基于应用程序


根据手机操作系统（安卓或 iOS），用户可以选择以下应用程序；


1.下载双因素验证器。


   - Authy for [Android](https://play.google.com/store/apps/details?id=com.authy.authy) 或 [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator for [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) 或 [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - 用于 [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) 或 [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605) 的 Google Authenticator

2.下载并安装 Authenticator 应用程序后。


   - 扫描 BTCPay 服务器提供的二维码
   - 或将 BTCPay 服务器生成的密钥手动输入 Authenticator 应用程序。

3.Authenticator 应用程序将为您提供一个唯一代码。在 BTCPay 服务器中输入唯一代码以验证设置，然后点击验证完成整个过程。


![image](assets/en/007.webp)


### 技能概要


在本节中，您将学到以下内容：



- 账户管理选项以及在 BTCPay 服务器实例上管理账户的各种方法。
- 如何设置基于应用程序的 2FA。


### 知识评估


#### KA 概念审查


说明基于应用程序的 2FA 如何帮助确保账户安全。


## 创建新商店


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### 创建商店向导


新用户登录 BTCPay 服务器时，环境是空的，需要创建第一个商店。BTCPay 服务器的介绍向导会让用户选择 "创建您的商店"(1)。商店可视为满足 Bitcoin 需求的 "家"。一个新的 BTCPay 服务器节点将从同步 Bitcoin Blockchain 开始 (2)。根据您运行 BTCPay 服务器的基础设施，这可能需要几个小时到几天的时间。实例的当前版本显示在 BTCPay Server UI 的右下角。这在排除故障时非常有用。


![image](assets/en/008.webp)


### 创建商店向导


本课程开始时的屏幕将与上一页略有不同。由于教师已经准备好演示环境，Bitcoin Blockchain 已经同步，因此您将看不到节点的同步状态。


用户可以决定删除自己的整个账户。点击 "账户 "选项卡上的 "删除 "按钮即可。


![image](assets/en/009.webp)


**注意！**


BTCPay 服务器账户可以创建无限数量的商店。每个商店都是一个 Wallet 或 "家"。


### 示例


首先点击 "创建您的商店"。


![image](assets/en/010.webp)


这将创建您使用 BTCPay 服务器的第一个主页和仪表板。


(1) 点击 "创建您的商店 "后，BTCPay 服务器会要求您为商店命名；可以是任何对您有用的名称。


![image](assets/en/011.webp)


(2) 接下来必须设置默认存储货币，可以是法定货币，也可以是以 Bitcoin 或 Sats 计价的货币。在演示环境中，我们将设置为美元。


![image](assets/en/012.webp)


(3) 作为商店设置的最后一个参数，BTCPay 服务器要求您设置 "首选价格来源"，以便将 Bitcoin 的价格与当前法币价格进行比较，这样您的商店就能在 Bitcoin 和商店设置的法币之间显示正确的 Exchange 汇率。我们将在演示示例中使用默认设置，将其设置为 Kraken Exchange。BTCPay 服务器使用 Kraken API 检查 Exchange 汇率。


![image](assets/en/013.webp)


(4) 设置好店铺参数后，点击 "创建 "按钮，BTCPay 服务器将为您创建第一个店铺的仪表板，并继续向导操作。


![image](assets/en/014.webp)


恭喜您，您已经创建了第一个商店，本练习到此结束。


![image](assets/en/015.webp)


### 技能概要


在本节中，您将学到



- 创建商店和配置默认货币，并结合价格来源偏好。
- 每个 "商店 "都是一个新家，与 BTCPay 服务器上的其他商店分开。


# Bitcoin 密钥安全简介


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## 了解 Bitcoin 密钥的生成


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### 生成 Bitcoin 密钥涉及哪些方面？


Bitcoin 钱包在创建时会产生所谓的 "seed"。在上一个目标中，您创建了一个 "seed"，之前生成的一系列单词也被称为 Mnemonic 短语。seed 用于生成单个 Bitcoin 密钥，并用于发送或接收 Bitcoin。seed 短语不得与第三方或不信任的同行共享。


seed 的生成是根据被称为 "分层确定性"（HD）框架的行业标准进行的。


![image](assets/en/016.webp)


### 地址


BTCPay 服务器是根据 generate 新的 Address 构建的。这缓解了公钥或 Address 重复使用的问题。使用相同的公钥可以轻松跟踪您的整个支付历史。将密钥视为一次性使用凭证将大大提高您的隐私保护。我们还使用 Bitcoin 地址，请不要将其与公钥混淆。


Address 通过 "散列算法 "从公钥中提取。不过，大多数钱包和交易都会显示地址，而不是公开密钥。一般来说，地址比公钥短，通常以 "1"、"3 "或 "bc1 "开头，而公钥则以 "02"、"03 "或 "04 "开头。



- 以 `1.....` 开头的地址仍然是非常常见的地址。正如 "创建新商店 "一章中提到的，这些都是传统地址。这种 Address 类型适用于 P2PKH 交易。P2Pkh 使用 Base58 编码，因此 Address 区分大小写。其结构以公钥为基础，另加一个数字作为标识符。



- 以 "bc1...... "开头的地址正逐渐成为常用地址。这些地址被称为（本地）SegWit 地址。与上述其他地址相比，这些地址提供了更好的收费结构。本地 SegWit 地址使用 Bech32 编码，只允许使用小写字母。



- 以 `3...` 开头的地址通常仍被交易所用作存款地址。在 "创建新存储 "一章中提到了这些地址，它们是封装或嵌套的 SegWit 地址。不过，它们也可以用作 "Multisig Address"。作为 SegWit Address 使用时，可以节省一些交易费用，但比本地 SegWit 要少。P2SH 地址使用 Base58 编码。这使得它与传统的 Address 一样对大小写敏感。



- 以 "2... "开头的地址是 Testnet 地址。它们用于接收 Testnet Bitcoin (tBTC)。千万不要混淆，向这些地址发送 Bitcoin。出于开发目的，您可以 generate 发送 Testnet Wallet。网上有多个获取 Testnet Bitcoin 的渠道。切勿购买 Testnet Bitcoin。Testnet Bitcoin 已被开采。这可能是开发人员使用 Regtest 的原因。对于开发人员来说，这是一个游乐场环境，缺少某些网络组件。不过，Bitcoin 对开发目的非常有用。


### 公用钥匙


目前，公钥在实践中使用较少。随着时间的推移，Bitcoin 用户已经用地址代替了公钥。但它们仍然存在，偶尔也会被使用。一般来说，公钥是比地址更长的字符串。就像地址一样，它们以一个特定的标识符开头。



- 首先，"02... "和 "03... "是以 SEC 格式编码的非常标准的公钥标识符。它们可以被处理并转化为接收地址，用于创建 multi-sig 地址或验证签名。早期的 Bitcoin 交易使用公共密钥作为 P2PK 交易的一部分。



- 然而，HD 钱包使用不同的结构。xpub..."、"ypub... "或 "zpub... "被称为扩展公钥或 xpub。作为 HD Wallet 的一部分，这些密钥用于衍生许多公钥。由于您的 xpub 保存着您的全部历史记录，即过去和未来的交易记录，因此切勿与不受信任的各方共享这些记录。


### 技能概要


在本节中，您将学到以下内容：



- 地址和公开密钥数据类型的区别，以及使用地址比使用公开密钥的好处。


### 知识评估


说明与 Address 重复使用或公用密钥方法相比，每次交易使用新地址的好处。


## 使用 Hardware Wallet 保护钥匙


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### 存储 Bitcoin 密钥


生成 seed 短语后，本书中生成的 12 - 24 个单词列表需要适当备份和安全保护，因为这些单词是恢复访问 Wallet 的唯一方法。高清钱包的结构及其使用单个 seed 确定性地生成地址的方式意味着，您创建的所有地址都将使用代表您的 seed 或恢复短语的 Mnemonic 单词列表进行备份。


确保您的恢复短语安全。如果被人访问，特别是怀有恶意的人，他们可以转移你的资金。保管好 seed 的安全，同时也要记住它们之间是相互的。存储 Bitcoin 私钥有几种方法，在安全性、隐私性、便利性和物理存储方面各有利弊。由于私人密钥的重要性，Bitcoin 用户倾向于以 "自我保管 "的方式存储和安全保管这些密钥，而不是使用银行等 "保管 "服务。根据用户的不同情况，他们必须使用 Cold 存储解决方案或 Hot Wallet。


### Hot 和 Cold 存放 Bitcoin 钥匙


通常，Bitcoin 钱包以 Hot Wallet 或 Cold Wallet 计价。大多数权衡在于便利性、易用性和安全风险。在托管解决方案中也可以看到上述每种方法。不过，这里的权衡主要基于安全和隐私，超出了本课程的范围。


### Hot Wallet


Hot 钱包是通过手机、网络或桌面软件与 Bitcoin 互动的最便捷方式。Wallet 始终与互联网连接，使用户能够发送或接收 Bitcoin。然而，这也是它的弱点；Wallet 由于始终在线，现在更容易受到黑客或设备上恶意软件的攻击。在 BTCPay 服务器中，Hot 钱包将私钥存储在实例中。如果有人恶意访问您的 BTCPay Server 商店，就有可能从 Address 中窃取资金。当BTCPay服务器在托管环境中运行时，您应始终在安全配置文件中考虑到这一点，最好不要在这种情况下使用Hot Wallet。当BTCPay服务器安装在由您拥有和保护的硬件上时，风险状况会大大降低，但绝不会完全消失。


### Cold Wallet


个人将其 Bitcoin 移入 Cold Wallet 中，因为它可以将私钥与互联网隔离，从而保护其免受潜在的在线威胁。将互联网连接从等式中移除可降低恶意软件、间谍软件和 SIM 卡交换的风险。Cold 存储器被认为在安全性和自主性方面优于 Hot 存储器，前提是采取足够的预防措施防止丢失 Bitcoin 私钥。Cold 存储器最适合大量的 Bitcoin，由于 Wallet 设置的复杂性，Bitcoin 不适合经常使用。


在 Cold 存储器中存储 Bitcoin 密钥有多种方法，从纸质钱包到脑钱包、硬件钱包，或者从一开始就是 Wallet 文件。大多数钱包使用 BIP 39 来 generate seed 短语。然而，在 Bitcoin core 软件内部，尚未就其使用达成共识。Bitcoin core 软件仍将 generate Wallet.dat 文件，您需要将其存储在安全的离线位置。


### 技能概要


在本节中，您将学到



- Hot 和 Cold 钱包在功能上的差异及其权衡。


### 知识评估 概念审查



- 什么是 Wallet？



- Hot 和 Cold 钱包有什么区别？



- 说明什么是 "生成 Wallet"？


## 使用 Bitcoin 按键


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay 服务器 Wallet


BTCPay 服务器包含以下标准 Wallet 功能：



- 交易
- 发送
- 接收
- 重新扫描
- 拉动支付
- 付款
- PSBT
- 常规设置


### 交易


管理员可在交易视图中查看与该特定存储连接的 On-Chain Wallet 的收发交易。每笔交易都有收到和发出金额的区别。收到的交易金额为 Green，发出的交易金额为红色。在 BTCPay 服务器交易视图中，管理员还将看到一组标准标签。


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### 如何发送


BTCPay 服务器的发送功能从您的 BTCPay 服务器 On-Chain Wallet 发送交易。BTCPay 服务器允许以多种方式签署交易以花费资金。您可以通过以下方式签署交易



- Hardware Wallet
- 支持 PSBT 的钱包
- 高清私钥或恢复种子。
- Hot Wallet


#### Hardware Wallet


BTCPay 服务器内置 Hardware Wallet 支持，让您可以将 Hardware Wallet 与 BTCPay Vault 结合使用，而不会将信息泄露给第三方应用程序或服务器。BTCPay 服务器中的 Hardware Wallet 集成使您能够导入 Hardware Wallet，并在设备上进行简单确认后即可使用收到的资金。您的私钥不会离开设备，所有资金都会根据您的 Full node 进行验证，确保不会泄露数据。


#### 与支持 PSBT 的 Wallet 签署


PSBT（部分签名 Bitcoin 交易）是仍需完全签名的 Bitcoin 交易的交换格式。BTCPay 服务器支持 PSBT，可通过兼容的硬件和软件钱包进行签名。


构建完全签署的 Bitcoin 交易需要经过以下步骤：



- 构建的 PSBT 有特定的输入和输出，但没有签名
- 导出的 PSBT 可由支持该格式的 Wallet 导入
- 可使用 Wallet 检查并签署交易数据
- 从 Wallet 导出签名的 PSBT 文件并导入 BTCPay 服务器
- BTCPay 服务器生成最终 Bitcoin 交易
- 验证结果并向网络广播


#### 使用高清私人密钥或 Mnemonic seed 签名


如果您在使用 BTCPay 服务器之前已经创建了 Wallet，那么您只需在适当的字段中输入您的私人密钥即可使用资金。请在 Wallet> Settings（设置）中设置适当的 "AccountKeyPath"，否则无法使用。


#### 使用 Hot Wallet 签署


如果您在设置商店时创建了一个新的 Wallet 并将其启用为 Hot Wallet，它将自动使用存储在服务器上的 seed 进行签名。


### RBF (Replace-by-fee)


Replace-by-fee（RBF）是Bitcoin协议的一项功能，允许您替换之前广播的交易（仍未确认）。这样就可以随机化 Wallet 的交易指纹，或用更高的费率来替换它，以提高交易在确认队列（Mining）中的优先级。这将有效取代原来的交易，因为更高的费率将被优先考虑，一旦确认，它将使原来的交易失效（不会重复消费）。


按 "高级设置 "按钮查看 RBF 选项。


![image](assets/en/017.webp)



- 随机化可提高私密性，允许自动替换交易以实现交易指纹的随机化。
- 是，标记为 RBF 的交易，并明确替换（默认不替换，仅通过输入替换）
- 不，不允许替换交易。


### Coin 选型


Coin 选择是一种先进的隐私增强功能，允许您在制作交易时选择要使用的硬币。例如，使用刚从连体混合中获得的硬币付款。


Coin 选择与 Wallet 标签功能配合使用。这样，您就可以对收到的资金贴上标签，以便更顺利地进行 UTXO 管理和支出。


BTCPay 服务器支持 BIP-329 标签管理。如果您从支持 BIP-329 的 Wallet 转来并设置了标签，BTCPay 服务器将自动识别并导入这些标签。迁移服务器时，也可将这些信息导出并导入新环境。


### 如何接收


当点击 BTCPay 服务器中的接收按钮时，会生成一个未使用的 Address，可用于接收付款。管理员也可通过创建新的 "Invoice "来生成新的 Address。


BTCPay 服务器将始终提示您 generate 下一个可用的 Address，以防止 Address 重复使用。点击 "generate 下一个可用的 BTC Address "后，BTCPay 服务器会生成一个新的 Address 和 QR。您还可以直接为 Address 设置标签，以便更好地管理地址。


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### 重新扫描


重新扫描功能依靠 Bitcoin core 0.17.0 的 "Scantxoutset "来扫描 Blockchain（称为 UTXO Set）的当前状态，以查找属于已配置派生方案的硬币。Wallet 重新扫描解决了 BTCPay 服务器用户经常遇到的两个常见问题。


1.间隙限制问题 - 大多数第三方钱包都是轻型钱包，许多用户共享一个节点。轻钱包和依赖 Full node 的钱包会限制在 Blockchain 上跟踪的无余额地址的数量（通常为 20 个），以防止出现性能问题。BTCPay 服务器会为每个 Invoice 生成一个新的 Address。考虑到上述情况，在 BTCPay 服务器连续生成 20 张未支付发票后，外部 Wallet 将停止获取交易，假设没有新的交易发生。一旦发票在 21 日、22 日等日期支付，您的外部 Wallet 就不会显示这些交易。另一方面，在内部，BTCPay 服务器 Wallet 会跟踪其生成的任何 Address，并显著提高间隙限制。它不依赖第三方，可以始终显示正确的余额。

2.间隙限制解决方案 - 如果您的 [外部/现有 Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet)允许间隙限制配置，那么简单的办法就是增加间隙限制。但是，大多数钱包都不允许这样做。据我们所知，目前支持间隙限制配置的钱包只有 Electrum、Wasabi 和 Sparrow wallet。不幸的是，您可能会在使用其他钱包时遇到问题。为了获得最佳的用户体验和隐私保护，请考虑使用 BTCPay 服务器内部的 Wallet 而不是外部钱包。


#### BTCPay 服务器使用 "mempoolfullrbf=1"


BTCPay 服务器使用 "mempoolfullrbf=1"；我们已将其作为默认设置添加到您的 BTCPay 服务器设置中。不过，您也可以自行禁用该功能。如果没有 "mempoolfullrbf=1"，如果客户在未发出RBF信号的交易中重复消费，商户只能在确认后才能知道。


管理员可能希望退出此设置。通过以下字符串，您可以更改默认设置。


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### BTCPay 服务器 Wallet 设置


BTCPay 服务器中的 Wallet 设置提供了 Wallet 一般设置的简明概览。如果 Wallet 是使用 BTCPay Server 创建的，则所有这些设置都会预先填入。


![image](assets/en/020.webp)


BTCPay 服务器中的 Wallet 设置提供了 Wallet 一般设置的简明概览。如果Wallet是通过BTCPay服务器创建的，所有这些设置都会预先填入。BTCPay Server的Wallet设置从Wallet状态开始。是纯观察型Wallet还是Hot型Wallet？根据Wallet类型的不同，操作也会不同，包括重新扫描Wallet以查找丢失的交易、从历史记录中删除旧交易、为支付链接注册Wallet，或替换和删除连接到商店的当前Wallet。在 BTCPay 服务器的 Wallet 设置中，管理员可为 Wallet 设置标签，以便更好地管理 Wallet。在这里，管理员还能看到衍生方案、账户密钥（xpub）、指纹和密钥路径。Wallet 设置中的付款只有两个主要设置。如果交易未能在 Invoice 到期后（设定分钟数）内确认，则付款无效。当支付交易确认次数达到 X 时，Invoice 将被视为已确认。管理员还可以在支付屏幕上设置切换显示推荐费用，或在区块数中设置手动确认目标。


![image](assets/en/021.webp)


**注意！**


如果您独立学习本课程，创建此账户可能需要在第三方主机上进行。因此，我们再次建议不要将其用作生产环境，而只能用于培训目的。


### 示例


#### 在 BTCPay 服务器中设置 Bitcoin Wallet


BTCPay 服务器提供两种设置 Wallet 的方法。一种方法是导入现有的 Bitcoin Wallet。导入可以通过连接Hardware Wallet、导入Wallet文件、输入扩展公钥、扫描Wallet的二维码，或者手动输入之前创建的Wallet恢复seed。在 BTCPay 服务器中，也可以创建新的 Wallet。在生成新的 Wallet 时，有两种可能的 BTCPay 服务器配置方式。


BTCPay 服务器中的 Hot Wallet 选项可启用 "PayJoin "或 "Liquid "等功能。但也有一个缺点：为该 Wallet 生成的恢复 seed 将存储在服务器上，任何拥有管理员控制权的人都可以获取它。由于您的私钥来自于您的恢复 seed，恶意行为者可能会获取您当前和未来的资金！


为了降低 BTCPay 服务器中的这一风险，管理员可以将服务器设置 > 策略 > "允许非管理员为其商店创建 Hot 钱包 "中的值设置为 "否"，因为这是默认值。为加强 Hot 钱包的安全性，服务器管理员应在允许拥有 Hot 钱包的账户上启用 2FA 身份验证。在公共服务器上存储私钥是一种危险的做法，会带来重大风险。其中一些风险与 Lightning Network 风险类似（有关 Lightning Network 风险，请参阅下一章）。


BTCPay 服务器提供的生成新 Wallet 的第二种方法是创建 Watch-only wallet。BTCPay 服务器将为您的私人密钥生成一次 generate。在用户确认写下其 seed 短语后，BTCPay 服务器将从服务器上清除私钥。这样，您的商店就有了一个 Watch-only wallet 连接。要使用Watch-only wallet上收到的资金，请参阅 "如何发送 "一章，您可以使用BTCPay服务器Vault、PSBT (Partially Signed Bitcoin Transaction)，或者手动提供您的seed短语。


您在上一部分创建了一个新的 "商店"。安装向导会继续询问 "设置 Wallet "或 "设置 Lightning 节点"。在本示例中，您将按照 "设置 Wallet "向导流程进行操作 (1)。


![image](assets/en/022.webp)


点击 "设置Wallet "后，向导将继续询问您如何继续；BTCPay服务器现在提供将现有Bitcoin Wallet连接到您的新商店的选项。如果您没有Wallet，BTCPay服务器建议您创建一个新的Wallet。本示例将按照 "创建一个新的 Wallet"（2）的步骤进行。按照步骤学习如何 "连接现有的 Wallet (1)"。


![image](assets/en/023.webp)


**注意！**


如果您在课堂上学习本课程，请注意我们生成的当前示例和 seed 仅用于教学目的。在这些地址的整个练习过程中，不应该有任何超出要求的大量内容。


(1) 点击 "创建新 Wallet "按钮，继续 "新建 Wallet "向导。


![image](assets/en/024.webp)


(2) 单击 "创建新的 Wallet "后，向导的下一个窗口将提供 "Hot Wallet "和 "Watch-only wallet "选项。如果您跟随教师，您的环境是共享 Demo，您只能创建 Watch-only wallet。请注意下面两个图之间的区别。在演示环境中，您可以跟随教师创建一个 "Watch-only wallet"，然后继续执行 "新建 Wallet "向导。


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) 继续新建 Wallet 向导，现在您已进入创建 BTC Watch-only wallet 部分。在这里，我们要设置 Wallet 的 "Address 类型"。BTCPay 服务器允许您选择自己喜欢的 Address 类型；在编写本课程时，仍建议使用 bech32 地址。关于地址的更多详情，请参阅本部分第一章。



- SegWit (bech32)
  - 本地 SegWit 地址以 `bc1q` 开头。
  - 示例： `bc1qXXXXXXXXXXXXXXXXXXX
- 传统
  - 传统地址是以数字 "1 "开头的地址。
  - 例如：`15e15hXXXXXXXXXXXXXXXXXX
- Taproot （面向高级用户）
  - Taproot 地址以 `bc1p` 开头。
  - 例如：`bc1pXXXXXXXXXXXXXXXXXXXXXX
- SegWit 包装
  - SegWit 封装地址以 `3` 开头。
  - 例如：`37BBXXXXXXXXXXXXX


选择 SegWit（推荐）作为首选的 Wallet Address 类型。


![image](assets/en/027.webp)


(4) 在设置 Wallet 的参数时，BTCPay 服务器允许用户通过 BIP39 设置可选的 passphrase；请务必确认密码。


![image](assets/en/028.webp)


(5) 设置Wallet的Address类型并可能设置一些高级选项后，点击创建，BTCPay服务器将generate您的新Wallet。请注意，这是生成 seed 短语前的最后一步。请确保只在有人可能无法通过查看您的屏幕窃取 seed 短语的环境中进行此操作。


![image](assets/en/029.webp)


(6) 在向导的下一界面，BTCPay 服务器将为您显示新生成的 Wallet 的恢复 seed 短语；这些短语是恢复您的 Wallet 和签署交易的关键。BTCPay 服务器会生成一个包含 12 个单词的 seed 短语。这些单词将在此设置界面后从服务器中删除。该Wallet是专门的Watch-only wallet。建议不要以数字或图片形式存储此 seed 短语。用户只有主动承认写下了 seed 短语，才能继续向导操作。


![image](assets/en/030.webp)


(7) 点击 "完成 "并确保新生成的Bitcoin seed短语安全后，BTCPay服务器将使用所附的新Wallet更新您的商店，并准备好接收付款。在用户 Interface 的左侧导航菜单中，请注意 Bitcoin 现在是如何突出显示并在 Wallet 下激活的。


![image](assets/en/031.webp)


### 举例说明：写下 seed 短语


此时使用 Bitcoin 特别安全。如前所述，只有您才能访问或了解您的 seed 短语。在您跟随教师和课堂学习时，生成的 seed 只应在本课程中使用。太多的因素，包括同学的窥探、不安全的系统等，使得这些密钥只具有教育意义，不可信。不过，生成的密钥仍应保存，供课程示例使用。


在这种情况下，我们将使用的第一种方法，也是最不安全的方法，就是按照正确的顺序写下 seed 短语。seed 短语卡包含在提供给学生的课程材料中，也可以在 BTCPay 服务器 GitHub 上找到。我们将用这张卡片写下上一步生成的单词。请确保按照正确的顺序书写。写下这些单词后，请与软件给出的单词进行核对，确保写下的顺序正确无误。写完后，点击复选框，说明您已正确写下 seed 短语。


### 示例：在 Hardware Wallet 上存储 seed 短语


在本课程中，我们将讨论如何在 Hardware Wallet 上存储 seed 短语。与教师一起学习本课程时，有时可能会用到这种设备。在本课程中，指导材料汇编了一份适合此练习的硬件钱包列表。


在本例中，我们将使用 BTCPay 服务器保险库和 Blockstream Jade Hardware Wallet。


您还可以观看连接 Hardware Wallet 的视频指南。

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


下载 BTCPay 服务器保险库：https://github.com/btcpayserver/BTCPayServer.Vault/releases


请确保为您的特定系统下载正确的文件。Windows用户应下载[BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe)软件包，Mac用户应下载[BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg)，Linux用户应下载[BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


安装BTCPay Server Vault后，点击桌面上的图标启动软件。当 BTCPay Server Vault 安装完成并首次启动时，它会询问是否允许与网络应用程序一起使用。它将要求授予访问您所使用的特定BTCPay服务器的权限。接受这些条件。BTCPay Server Vault现在将搜索硬件设备。一旦找到设备，BTCPay服务器将识别Vault正在运行，并已获取您的设备。


**注意！**


使用 Hot Wallet 时，不要将 SSH 密钥或服务器管理帐户交给管理员以外的任何人。任何可以访问这些账户的人都可以访问 Hot Wallet 中的资金。


### 技能概要


在本节中，您将学到以下内容：



- Bitcoin Wallet 的交易视图及其各种分类。
- 从 Bitcoin Wallet 发送信息时，有多种选择，从硬件到 Hot 钱包都有。
- 使用大多数钱包时面临的间隙限制问题，以及如何纠正这一问题。
- 如何在 BTCPay 服务器中 generate 新 Bitcoin Wallet，包括在 Hardware Wallet 中存储密钥和备份恢复短语。


在本目标中，您已学会如何在 BTCPay 服务器中 generate Bitcoin Wallet 新 GW。我们尚未讨论如何保护或使用这些密钥。在对这一目标的简要概述中，您已经学会了如何建立第一个商店。您已学会如何 generate 一个 Bitcoin 恢复 seed 短语。


### 知识评估 实际审查


说明生成密钥的方法和确保密钥安全的方案，以及安全方案的权衡/风险。


## BTCPay 服务器闪电 Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


服务器管理员在配置新的 BTCPay 服务器实例时，可以设置 Lightning Network 实现，如 LND、Core Lightning 或 Eclair；更多详细安装说明，请参阅 "配置 BTCPay 服务器 "部分。


如果通过课堂教学，将闪电节点连接到BTCPay服务器是通过自定义节点实现的。默认情况下，非BTCPay服务器管理员的用户将无法使用内部闪电节点。这是为了保护服务器所有者的资金不受损失。服务器管理员可以安装一个插件，通过LNBank授予访问其Lightning节点的权限；这不在本书的讨论范围之内。有关LNBank的更多信息，请参阅官方插件页面。


### 连接内部节点（服务器管理员）


服务器管理员可以使用BTCPay服务器的内部Lightning节点。无论采用哪种Lightning实现方式，连接内部Lightning节点的方法都是一样的。


进入之前的设置商店，点击左侧菜单中的 "闪电 "Wallet。BTCPay 服务器提供两种设置方式：使用内部节点（默认情况下仅适用于服务器管理员）或自定义节点（外部连接）。服务器管理员可点击 "使用内部节点 "选项。无需进行更多配置。点击 "保存 "按钮并注意 "BTC Lightning 节点已更新 "的通知。商店现已成功获得 Lightning Network 功能。


### 连接外部节点（服务器用户/存储所有者）


默认情况下，店主不得使用服务器管理员的闪电节点。需要连接到外部节点，可以是店主在设置 BTCPay 服务器之前拥有的节点，也可以是服务器管理员提供的 LNBank 插件，还可以是 Alby 等托管解决方案。


进入之前设置好的商店，点击左侧菜单中钱包下方的 "闪电"。由于默认情况下不允许店主使用内部节点，因此该选项为灰色。使用自定义节点是商店所有者默认情况下唯一可用的选项。


BTCPay服务器需要连接信息；预制（或托管解决方案）将提供专门为Lightning实施定制的连接信息。在BTCPay服务器中，店主可以使用以下连接；



- 通过 TCP 或 Unix 域ocket 连接的 C-lightning。
- 通过 HTTPS 进行闪电充电
- 通过 HTTPS 的 Eclair
- 通过 REST 代理访问 LND
- 通过 REST API 访问 LNDhub


![image](assets/en/032.webp)


点击 "测试连接"，确保您正确输入了连接详情。确认连接正常后，点击 "保存"，BTCPay 服务器就会显示商店已更新为闪电节点。


### 管理内部 Lightning 节点 LND（服务器管理员）


连接内部 Lightning 节点后，服务器管理员会发现仪表板上出现了专门用于显示 Lightning 信息的新磁贴。



- 闪电平衡
- 渠道中的 BTC
  - BTC 开放渠道
  - BTC 本地余额
  - BTC 远程余额
  - BTC 关闭渠道
- BTC On-Chain
  - BTC 已确认
  - BTC 未经证实
  - 保留 BTC
- 闪电服务
  - 驾驭闪电（RTL）。


通过点击 "Lightning 服务 "磁贴中的 "Ride the Lightning Logo "或左侧菜单中钱包下方的 "Lightning"，服务器管理员可以进入 RTL 进行 Lightning 节点管理。


**注意！**


连接内部 Lightning 节点失败 - 如果内部连接失败，请确认：


1.Bitcoin On-Chain 节点完全同步

2.内部闪电节点已在 "闪电">"设置">"BTC 闪电设置 "下 "启用"。


如果您无法连接到您的闪电节点，您可以尝试重启您的服务器，或阅读BTCPay服务器官方文档中的更多详情；https://docs.btcpayserver.org/Troubleshooting/。在您的闪电节点显示 "在线 "之前，您无法在商店中接受闪电付款。请点击 "公共节点信息 "链接测试您的闪电连接。


### 闪电 Wallet


在左侧菜单栏的 Lightning Wallet 选项中，服务器管理员可以轻松访问 RTL、其公共节点信息以及针对其 BTCPay 服务器商店的 Lightning 设置。


#### 内部节点信息


服务器管理员可以点击内部节点信息，查看服务器状态（在线/离线）以及 Clearnet 或 Tor 的连接字符串。


![image](assets/en/033.webp)


#### 更改连接


要更改外部 Lightning 节点，请进入 "Lightning 设置 "并点击 "更改连接"（位于 "公共节点信息 "旁边）。这将重置现有设置。输入新节点的详细信息，点击 "保存"，商店就会相应更新。


![image](assets/en/034.webp)


#### 服务


如果服务器管理员决定为 "闪电 "实施安装多个服务，则会在此处列出这些服务。通过标准的 LND 实施，管理员将把 Ride The Lightning (RTL) 作为节点管理的标准工具。


#### BTC Lightning Wallet 设置


在上一步中为商店添加闪电节点后，店主仍可通过闪电设置顶部的切换按钮选择停用闪电节点。


![image](assets/en/035.webp)


#### 闪电支付选项


店主可以设置以下参数，以增强客户的 "闪电 "体验。



- 以 Satoshis 为单位显示闪电付款金额。
- 在 Lightning Invoice 中添加专用信道的跳频提示。
- 在结账时统一 On-Chain 和 Lightning 支付 URL/QR 代码。
- 为闪电发票设置描述模板。


#### LNURL


店主可以选择使用或不使用LNURL。Lightning Network URL或LNURL是为闪电付款人和收款人之间的互动而提出的标准。简而言之，LNURL 是以 LNURL 为前缀的 bech32 编码 URL。Lightning Wallet会对URL进行解码，与URL联系，并等待一个包含进一步指令的JSON对象，其中最重要的是一个定义LNURL行为的标签。



- 启用 LNURL
- LNURL 经典模式
  - 为了与 Wallet 兼容，Bech32 编码（经典）与明文 URL（即将推出）
- 允许收款人发表评论。


### 示例 1


#### 通过内部节点连接 Lightning（管理员）


只有当您是该实例的管理员，或管理员已更改默认设置使用户可以使用内部闪电节点时，该选项才可用。


作为管理员，点击左侧菜单栏中的Lightning Wallet。BTCPay 服务器将要求您选择连接闪电节点的两个选项之一：内部节点或自定义外部节点。点击 "使用内部节点"，然后点击 "保存"。


#### 管理您的闪电节点 (RTL)


连接到内部闪电节点后，BTCPay服务器将更新并显示 "BTC闪电节点已更新 "的通知，确认您已将闪电连接到您的商店。


管理闪电节点是服务器管理员的一项任务。这包括以下内容：


- 管理交易
- 管理流动资金
  - 入境流动性
  - 出境流动性
- 管理同行和渠道
  - 有联系的同行
  - 渠道费
  - 通道状态
- 经常备份通道状态。
- 检查路由报告
- 或者使用 Loop 等服务。


所有闪电节点的管理均以RTL为标准（假设您在LND上运行）。管理员可以点击 BTCPay 服务器中的闪电 Wallet，找到打开 RTL 的按钮。BTCPay 服务器的主控制面板现已更新为 Lightning Network 磁贴，包括快速访问 RTL。


### 示例 2


#### 与艾尔比连接到闪电


在与 Alby 这样的托管人连接时，店主应首先创建一个账户，然后访问 https://getalby.com/


![image](assets/en/036.webp)


创建 Alby 账户后，前往 BTCPay 服务器商店。


步骤 1：点击仪表板上的 "设置闪电节点 "或钱包下方的 "闪电"。


![image](assets/en/037.webp)


第 2 步：插入 Alby 提供的 Wallet 连接凭证。在 Alby 控制面板上，点击 Wallet。在这里您可以找到 "Wallet 连接凭证"。复制这些凭证。将 Alby 提供的凭证粘贴到 BTCPay 服务器的连接配置字段中。


![image](assets/en/038.webp)


第3步：向BTCPay服务器提供连接详情后，点击 "测试连接 "按钮，确保连接正常。注意屏幕上方的 "连接到闪电节点成功 "信息。这就确认一切正常。


![image](assets/en/039.webp)


第 4 步：点击 "保存"，您的商店现在已连接到 Alby 的 "闪电 "节点。


![image](assets/en/040.webp)


**注意！**


永远不要相信托管闪电解决方案的价值超过你愿意失去的价值。


### 技能概要


在本节中，您将学到



- 如何连接内部或外部 Lightning 节点
- 仪表板中与 "闪电 "有关的各种磁贴的内容和功能
- 如何使用电压浪涌或 Alby 配置 Lightning Wallet


### 知识评估 实际审查


描述将 Lightning Wallet 连接到商店的各种选择。


# BTCPay 服务器 Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## 仪表板概览


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay 服务器是一个模块化软件包。但是，每个 BTCPay 服务器都必须遵守一些标准，这些标准将规范管理员与用户之间的交互。从仪表板开始。每个 BTCPay 服务器登录后的主要入口。控制面板提供商店业绩、Wallet 当前余额和过去 7 天交易的概览。由于这是一个模块化视图，插件可以利用该视图为自己服务，并在仪表盘上创建自己的磁贴。在本课程中，我们将只讨论 BTCPay 服务器中的标准插件和应用程序，以及它们各自的视图。


### 仪表板瓷砖


在 BTCPay 服务器仪表盘的主视图中，有几个标准磁贴可用。这些磁贴专为商店所有者或管理员设计，以便在概览中快速管理商店。



- Wallet 平衡
- 交易活动
- 闪电余额（如果商店已启用闪电功能）
- 闪电服务（如果商店已启用闪电服务）
- 最近的交易
- 近期发票
- 当前活跃的众筹
- 店铺业绩/最畅销商品。


### Wallet 平衡


Wallet 余额磁贴可快速显示 Wallet 的资金和业绩概况。它可以用 BTC 或法币以每周、每月或每年图表的形式查看。


![image](assets/en/041.webp)


### 交易活动


在 Wallet 余额磁贴旁边，BTCPay 服务器会显示待处理付款、过去 7 天内的交易次数以及您的商店是否已发出退款的快速概览。点击 "管理 "按钮，您将进入待处理付款的管理页面（在 BTCPay Server - 支付章节了解更多关于付款的信息）。


![image](assets/en/042.webp)


### 闪电平衡


只有在激活 "闪电 "时才能看到。


当管理员允许Lightning Network访问时，BTCPay服务器仪表盘现在有一个新的磁贴，显示您的闪电节点信息。渠道中有多少 BTC，本地或远程如何平衡（入站或出站流动性），渠道是否正在关闭或打开，以及闪电节点上的 On-Chain 持有多少 Bitcoin。


![image](assets/en/043.webp)


### 闪电服务


这只有在闪电活动时才能看到。


除了在BTCPay服务器仪表板上看到您的闪电余额外，管理员还将看到 "闪电服务 "磁贴。在这里，管理员可以找到用于管理闪电节点的工具的快速按钮；例如，Ride the Lightning 是 BTCPay Server 用于管理闪电节点的标准工具之一。


![image](assets/en/044.webp)


### 近期交易


最近交易 "磁贴显示您店铺最近的交易。只需单击一下，BTCPay 服务器实例的管理员就能看到最近的交易，并了解是否需要关注该交易。


![image](assets/en/045.webp)


### 近期发票


最近发票 "磁贴显示 BTCPay 服务器生成的 6 张最新发票，包括状态和 Invoice 金额。该磁贴还包含一个 "查看全部 "按钮，可轻松访问 Invoice 的完整概览。


![image](assets/en/046.webp)


### 销售点和众筹


由于BTCPay服务器提供一套标准插件或应用程序，销售点和众筹是BTCPay服务器的两个主要插件。每个商店和 Wallet BTCPay 服务器的用户都可以根据自己的需要 generate 销售点或众筹。每个插件都将创建一个新的仪表板瓦片，显示插件的性能。


![image](assets/en/047.webp)


请注意 "销售点 "磁贴和 "众筹 "磁贴之间的细微差别。管理员在 "销售点 "磁贴中看到的是销量最高的项目。在众筹磁贴中，这变成了 "顶级特权"。这两个磁贴都有快速按钮，用于管理各自的应用程序和查看最近由顶级项目或顶级津贴创建的发票。


![image](assets/en/048.webp)


**注意！**


余额图表和最近交易仅适用于 On-Chain 支付方式。有关 Lightning Network 余额和交易的信息已列入待办事项列表。自 BTCPay 服务器版本 1.6.0 起，Lightning Network 基本余额可用。


### 技能概要


在本节中，您将学到以下内容：



- 主登陆页面上磁贴的核心布局称为 "控制面板"。
- 基本了解每块瓷砖的内容。


### 知识评估审查


从仪表板中尽可能多地列出内存中的磁贴。


## BTCPay 服务器 - 商店设置


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


在BTCPay服务器软件中，我们知道有两种类型的设置。BTCPay服务器商店特定设置，即仪表盘下方左侧菜单栏中的设置按钮，以及BTCPay服务器设置，位于菜单栏底部账户上方。BTCPay 服务器的服务器特定设置只能由服务器管理员查看。


商店设置由许多选项卡组成，可对每套设置进行分类。



- 一般情况
- 费率
- 结账外观
- 访问令牌
- 用户
- 角色
- 网络钩子
- 付款处理器
- 电子邮件
- 表格


### 一般情况


在 "常规设置 "选项卡中，店主可以设置自己的品牌和付款默认值。在初始设置商店时，会给出一个商店名称；这将反映在 "商店名称 "下的 "常规设置 "中。在这里，店主还可以设置与品牌相匹配的网站，以及供管理员在数据库中识别的商店 ID。


#### 打造品牌


由于 BTCPay 服务器是自由和开放源码软件，因此店主可以根据自己的店铺定制品牌。设置品牌颜色、存储品牌徽标，并为公共/面向客户的页面（发票、付款申请、拉动付款）添加自定义 CSS。


#### 付款方式


在支付设置中，店主可以设置商店的默认货币（Bitcoin 或任何法定货币）。


#### 允许任何人创建发票


此设置适用于 BTCPay Server 的开发者或构建者。为您的商店启用此设置后，外部世界就可以在您的 BTCPay 服务器实例上创建发票。


#### 在发票上添加额外费用（网络费


BTCPay 中的一项功能，当商户需要一次性转移大量 Bitcoin 时，可保护商户免受 Dust 攻击或客户日后产生的高额费用。例如，客户创建了一个 20 美元的 Invoice 并进行了部分支付，支付了 20 次 1 美元，直到 Invoice 全部支付。商户现在有一笔较大的交易，如果商户以后决定转移这些资金，Mining 的费用就会增加。默认情况下，当 Invoice 分多次交易支付时，BTCPay 会在 Invoice 总金额上增加额外的网络费用，以支付商户的这笔费用。BTCPay 提供多个选项来定制此保护功能。您可以收取网络费用：



- 只有在客户为 Invoice 支付了一次以上的情况下（在上面的例子中，如果客户为 20\$ 创建了一个 Invoice，并支付了 1\$ ，那么现在应付的 Invoice 总金额就是 19\$ + 网络费。网络费在第一次付款后收取）
- 每笔付款（包括第一笔付款，在我们的例子中，即使是第一笔付款，总额也将立即达到 20\$ + 网络费）
- 从不添加网络费（完全禁用网络费）


虽然它可以防止 Dust 交易，但如果沟通不当，也会给企业带来负面影响。客户可能会有额外的问题，并认为你多收了他们的钱。


#### Invoice 在什么情况下失效？


Invoice 定时器默认设置为 15 分钟。该计时器根据 Bitcoin 与固定 Exchange 的费率锁定 Bitcoin 的金额，作为防止波动的保护机制。如果客户未在规定时间内支付 Invoice，则 Invoice 将被视为过期。一旦交易在 Blockchain 上显示（确认次数为零），Invoice 即被视为 "已支付"；当交易达到商家规定的确认次数（通常为 1-6）时，Invoice 即被视为 "已完成"。计时器可按分钟自定义。


#### 即使支付的金额比预期少 X%，是否也视为已支付 Invoice？


当客户使用 Exchange Wallet 直接支付 Invoice 时，Exchange 会收取少量费用。这意味着该 Invoice 未被视为完全完成。Invoice 会被标记为 "部分支付"。如果商家希望接受未足额支付的发票，可以在此设置百分比率。


### 费率


在 BTCPay 服务器中，当生成 Invoice 时，它总是需要最新、最准确的 Bitcoin 至飞特价格。在 BTCPay Server 中创建新商店时，管理员会被要求设置首选价格来源。商店建立后，店主可随时在此选项卡中更改价格来源。


#### 高级费率规则脚本


主要供高级用户使用。如果开启，店主就可以围绕价格行为和如何向客户收费创建脚本。


#### 测试


您首选货币对的快速测试场所。该功能还包括通过 REST 查询检查默认货币对的功能。


### 结账外观


结账外观 "选项卡从 Invoice 的特定设置和默认付款方式开始，并在满足设定要求后启用特定付款方式。


#### Invoice 设置


默认付款方式。BTCPay 服务器的标准配置提供三个选项。



- BTC (On-Chain)
- BTC (LNURL-pay)
- 英联邦运输委员会（off-chain 和闪电）


我们可以为商店设置参数，只有当价格小于 X 时，顾客才会与 "闪电 "进行互动，反之亦然，对于 On-Chain 交易，当 X 大于 Y 时，始终显示 On-Chain 支付选项。


![image](assets/en/049.webp)


#### 结账


自 BTCPay 服务器 1.7 版起，引入了新的结账 Interface，即结账 V2。由于 1.9 版已标准化，管理员和店主仍可将结账设置为之前的版本。通过使用切换 "使用经典结账"，店主可以将商店恢复到以前的结账体验。BTCPay 服务器还为在线商务或店内体验提供了一套精选预设。


![image](assets/en/050.webp)


当客户与商店互动并生成 Invoice 时，Invoice 会有一个过期时间。BTCPay 服务器默认设置为 5 分钟，管理员可根据自己的喜好进行调整。结账页面可通过选中以下参数进一步自定义：



- 通过展示彩纸庆祝付款
- 显示商店标题（名称和徽标）
- 显示 "用 Wallet 支付 "按钮
- 统一 On-Chain 和 off-chain 支付 URL/QR
- 以里数显示闪电付款金额
- 结账时自动检测语言


![image](assets/en/051.webp)


未设置自动检测语言时，BTCPay 服务器默认显示英语。店主可将默认语言更改为自己喜欢的语言。


![image](assets/en/052.webp)


点击下拉菜单，店主可以设置在结账页面上显示的自定义 HTML 标题。


![image](assets/en/053.webp)


为确保客户了解自己的付款方式，店主可明确设置结账时始终要求用户选择自己喜欢的付款方式。支付 Invoice 后，BTCPay 服务器将允许客户返回网店。店主可将此重定向设置为在客户付款后自动应用。


![image](assets/en/054.webp)


#### 公共收据


在公共收据设置中，店主可以将收据页面设置为公共页面，在收据页面上显示付款清单和二维码，方便顾客访问。


![image](assets/en/055.webp)


### 访问令牌


访问令牌用于与某些电子商务集成或定制集成配对。


![image](assets/en/056.webp)


### 用户


商店用户是店主管理其员工、员工账户和商店访问权限的地方。员工创建账户后，店主可将特定用户添加为商店的访客用户或所有者。要进一步定义员工的角色，请参阅下一节 "BTCPay 服务器商店设置 - 角色"。


![image](assets/en/057.webp)


### 角色


店主可能觉得用户的标准角色不够重要。在自定义角色设置中，店主可以定义业务中对每个角色的确切需求。


(1) 要创建新角色，请单击 "+ 添加角色 "按钮。


![image](assets/en/058.webp)


(2) 输入角色名称，例如 "出纳员"。


![image](assets/en/059.webp)


(3) 配置角色的个人权限。



- 修改您的商店。
- 管理与店铺关联的 Exchange 账户。
  - 查看与您的商店关联的 Exchange 账户。
- 管理您的拉动付款。
- 创建拉动式付款。
  - 创建未经批准的拉动付款。
- 修改发票。
  - 查看发票。
  - 创建 Invoice。
  - 从与店铺相关的闪电节点创建发票。
- 查看您的商店。
  - 查看发票。
  - 查看您的付款申请。
  - 修改商店的网络钩子。
- 修改付款申请。
  - 查看您的付款申请。
- 使用与店铺相关的闪电节点。
  - 查看与店铺相关的闪电发票。
  - 从与店铺相关的闪电节点创建发票。
- 将资金存入与您的店铺相连的 Exchange 账户。
- 从 Exchange 账户向您的商店提取资金。
- 在店铺的 Exchange 账户上进行资金交易。


创建角色时，名称是固定的，在编辑模式下无法更改。


![image](assets/en/060.webp)


### 网络钩子


在 BTCPay 服务器中，创建新的 "网络钩子 "相当容易。在 BTCPay Server 商店设置 - Webhooks 选项卡中，店主可以通过点击 "+ 创建 Webhook "轻松创建新的 Webhook。网络钩子允许 BTCPay 服务器向其他服务器或电子商务集成发送与您的商店相关的 HTTP 事件。


![image](assets/en/061.webp)


现在您已进入创建 Webhook 的视图。确保您知道有效载荷 URL，并将其粘贴到 BTCPay 服务器中。当您粘贴有效载荷 URL 时，下方会显示网络钩子密文。复制网络钩子密文并将其提供给端点。一切设置完成后，您就可以在 BTCPay 服务器中切换到 "自动重新交付"。BTCPay 服务器会在 10 秒后或 1 分钟后尝试重新发送任何失败的发送，10 分钟后最多可重新发送 6 次。您可以在每个事件之间切换，也可以根据需要指定事件。确保启用网络钩子，并点击 "添加网络钩子 "按钮保存。


![image](assets/en/062.webp)


Webhooks 与 Bitpay API 并不兼容。BTCPay 服务器中有两个独立的 IPN（BitPay 术语："即时支付通知"）。



- Webhookp
- 通知


只有在通过 Bitpay API 创建发票时才使用通知 URL。


### 付款处理器


支付处理器与 BTCPay 服务器中的支付概念协同工作。支付聚合器可批量处理多笔交易并一次性发送。有了赔付处理器，店主就可以自动进行批量赔付。BTCPay Server 提供两种自动付款方法：On-Chain 和 off-chain (LN)。


店主可以分别点击和配置两个支付处理器。店主可能只想每 X 小时运行一次 On-Chain 处理器，而 off-chain 处理器可能每几分钟运行一次。对于 On-Chain，您还可以设置应包含哪个区块的目标。默认设置为 1（或下一个可用区块）。请注意，设置 off-chain 支付处理器只有间隔计时器，没有区块目标。Lightning Network 支付是即时支付。


![image](assets/en/063.webp)

![image](assets/en/064.webp)


店主只有在 Hot Wallet 连接到其商店时才能配置 On-Chain 处理器。


![image](assets/en/065.webp)


设置支付处理程序后，您可以返回 BTCPay 服务器商店设置中的支付处理程序选项卡，快速删除或修改该处理程序。


**注**


支付处理器 On-Chain - On-Chain 支付处理器只能在连接了 Hot Wallet 的商店中运行。如果没有连接 Hot Wallet，BTCPay 服务器将无法持有 Wallet 密钥，也就无法自动处理支付。


### 电子邮件


BTCPay 服务器可使用电子邮件发送通知，或在设置正确的情况下恢复在实例上创建的账户。作为标准配置，BTCPay 服务器不会在密码丢失等情况下发送电子邮件。


![image](assets/en/066.webp)


在店主设置电子邮件规则以触发其店铺中的特定事件之前，他们必须首先设置一些基本的电子邮件设置。BTCPay 服务器需要这些设置才能为与店铺相关的事件或密码重置发送电子邮件。


BTCPay 服务器通过使用 "快速填写 "选项使填写这些信息变得更容易：



- Gmail.com
- 雅虎网站
- 邮件枪
- 办公室365
- 发送网格


通过使用快速填写选项，BTCPay 服务器将预先填充 SMTP 服务器和端口字段。现在，店主只需填写他们的凭证，包括电子邮件 Address、登录（通常等于您的电子邮件 Address）和密码。BTCPay 服务器电子邮件设置中的高级选项是禁用 TLS 证书安全检查；默认情况下已启用。


![image](assets/en/067.webp)


通过电子邮件规则，店主可以设置特定事件，触发向特定电子邮件地址发送电子邮件。



- 创建了 Invoice
- Invoice 收到付款
- Invoice 处理
- Invoice 已过期
- Invoice 已解决
- Invoice 无效
- Invoice 已付款


如果客户提供了电子邮件 Address，这些触发器也可以将信息发送给客户。店主可以预先填写主题行，以明确电子邮件发生的原因和触发原因。


![image](assets/en/068.webp)


### 表格


由于 BTCPay Server 不收集任何数据，店主可能希望在结账体验中添加自定义表单；这样，店主就可以从客户那里收集更多信息。BTCPay Server 表单生成器由两部分组成：表单的可视化视图和更高级的代码视图。


创建新表单时，BTCPay 服务器会打开一个新窗口，要求您提供新表单的基本信息。首先，店主需要为新表单起一个明确的名称；该名称设置后不可更改。


![image](assets/en/069.webp)


店主为表单命名后，还可以将 "允许表单公开使用 "的开关拨到ON，这样表单就会变成 Green。这样就能确保在每个面向客户的位置都使用该表单。例如，如果店主不通过销售点创建单独的 Invoice，他们可能仍想收集客户信息。此切换允许收集这些信息。


![image](assets/en/070.webp)


每个表单至少有一个新表单字段。店主可以选择字段的类型。



- 文本
- 数量
- 密码
- 电子邮件
- 网址
- 电话号码
- 日期
- 隐藏字段
- 字段集
- 用于公开评论的文本区域。
- 选项选择器


每种类型都有其需要填写的参数。店主可以根据自己的喜好进行设置。在第一个创建的字段下面，店主可以向该表单添加新字段。


![image](assets/en/071.webp)


#### 高级自定义表单


BTCPay Server 还允许您用代码构建表单。特别是 JSON。店主可以点击编辑器旁边的 CODE 按钮，进入表单代码，而无需查看编辑器。在字段定义中，只能设置以下字段；字段值存储在 Invoice 的元数据中：


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

字段名称表示在 Invoice 元数据中存储用户提供值的 JSON 属性名称。一些众所周知的名称可以通过解释和修改来调整 Invoice 的设置。


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

您可以在表单的 URL 中添加查询字符串，如"?your_field=value"，从而自动预填 Invoice 的字段。


以下是该功能的一些使用案例：



- 协助用户输入：用已知的客户信息预填字段，让他们更容易完成表单。例如，如果您已经知道客户的电子邮件 Address，就可以预先填写电子邮件字段，以节省客户的时间。
- 个性化：根据客户偏好或细分定制表单。例如，如果您有不同的客户层级，您可以在表单中预先填写相关数据，如客户的会员级别或特定优惠。
- 跟踪：使用隐藏字段和预填值跟踪客户访问来源。例如，您可以为每个营销渠道（如 Twitter、Facebook 和电子邮件）创建带有预填 utm_media 值的链接。这有助于您分析营销工作的效果。
- A/B 测试：预先在字段中填入不同的值，以测试不同的表单版本，从而优化用户体验和转换率。


### 技能概要


在本节中，您将学到以下内容：



- 商店设置 "选项卡的布局和功能
- 多种选项可用于微调 Exchange 基本费率、部分支付、轻微少付等情况的处理。
- 自定义结账外观，包括发票上与价格相关的主链与 Lightning 启用。
- 管理不同角色的商店访问级别和权限。
- 配置自动电子邮件及其触发器
- 创建自定义表单，以便在结账时收集更多客户信息。


### 知识评估


#### KA 回顾


商店设置 "和 "服务器设置 "有什么区别？


#### KA 假设


说明在结账外观 > Invoice 设置中可能选择的一些选项及其原因。


## BTCPay 服务器 - 服务器设置


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay 服务器由两个不同的设置视图组成。一个是商店设置视图，另一个是服务器设置视图。后者仅供服务器管理员使用，商店所有者不可使用。服务器管理员可以添加用户、创建自定义角色、配置电子邮件服务器、设置策略、运行维护任务、检查连接到 BTCPay 服务器的所有服务、上传文件到服务器或检查日志。


### 用户


如前所述，服务器管理员可以通过将用户添加到 "用户 "选项卡来邀请用户使用服务器。


### 全服务器自定义角色


BTCPay 服务器有两种类型的自定义角色：BTCPay 服务器设置中的特定商店自定义角色和全服务器自定义角色。二者拥有相似的权限；然而，如果通过 BTCpay 服务器设置 - 角色选项卡进行设置，应用的角色将是全服务器的，并适用于多个商店。请注意，服务器设置中的自定义角色有一个 "全服务器 "标签。


![image](assets/en/072.webp)


### 全服务器自定义角色


服务器范围内的自定义角色权限设置；



- 修改您的商店。
- 管理与店铺关联的 Exchange 账户。
  - 查看与您的商店链接的 Exchange 账户。
- 管理您的拉动付款。
- 创建拉动式付款。
  - 创建未经批准的拉动付款。
- 修改发票。
  - 查看发票。
  - 创建 Invoice。
  - 从与店铺相关的闪电节点创建发票。
- 查看您的商店。
  - 查看发票。
  - 查看您的付款申请。
  - 修改商店的网络钩子。
- 修改付款申请。
  - 查看您的付款申请。
- 使用与店铺相关的闪电节点。
  - 查看与店铺相关的闪电发票。
  - 从与店铺相关的闪电节点创建发票。
- 将资金存入与您的商店相连的 Exchange 账户。
- 从 Exchange 账户向您的商店提取资金。
- 在店铺的 Exchange 账户上进行资金交易。


**注意！**


创建角色时，名称是固定的，在编辑模式下无法更改。


### 电子邮件


服务器范围的电子邮件设置与特定于商店的电子邮件设置类似。不过，此设置不仅处理商店或管理员日志的触发，还处理其他事件的触发。此电子邮件设置还可在 BTCPay 服务器登录时进行密码恢复。其工作原理与商店特定设置类似；管理员可以快速填写电子邮件参数并输入电子邮件凭据，从而允许服务器发送电子邮件。


![image](assets/en/073.webp)


### 政策


BTCPay 服务器策略管理员可以对现有用户设置、新用户设置、通知设置和维护设置等主题进行各种设置。这些设置用于将新用户注册为管理员或普通用户，或通过在服务器标题中添加 BTCPay 服务器，使其不被搜索引擎发现。


![image](assets/en/074.webp)


#### 现有用户设置


这里提供的选项与自定义角色不同。这些附加权限可能会使商店或其所有者容易受到攻击。可添加到现有用户的策略：



- 允许非管理员在其商店中使用内部 Lightning 节点。
  - 这将允许店主使用服务器管理员的 "闪电 "节点，从而使用他的资金！请注意，这不是允许访问 "闪电 "的解决方案。
- 允许非管理员为其商店创建 Hot 钱包。
  - 这将允许任何在您的 BTCPay 服务器实例上拥有账户的人创建 Hot 钱包，并将其恢复的 seed 存储在管理员的服务器上。这可能会使管理员承担持有第三方资金的责任！
- 允许非管理员为其商店导入 Hot 钱包。
  - 与之前创建 Hot 钱包的主题类似，该策略也允许导入 Hot Wallet，但同样存在创建 Hot 钱包部分提到的危险。


![image](assets/en/075.webp)


#### 新用户设置


我们可以设置一些重要的设置来管理服务器上的新用户。我们可以为新注册用户设置确认电子邮件、禁止通过登录屏幕创建新用户，以及限制非管理员通过应用程序接口创建用户。



- 要求提供注册确认电子邮件。
  - 服务器管理员必须已设置电子邮件服务器。
- 禁用服务器上的新用户注册
- 禁止非管理员访问用户创建 API 端点。


默认情况下，BTCPay 服务器会切换 "禁用服务器上的新用户注册"，并关闭非管理员对用户创建 API 端点的访问。这是出于安全考虑，这样，偶然发现您的 BTCPay 登录信息的人就无法创建账户。


![image](assets/en/076.webp)


#### 通知设置


![image](assets/en/077.webp)


#### 维护设置


BTCPay Server是GitHub上的一个开源项目。每当BTCPay服务器发布新版本软件时，管理员都会收到新版本可用的通知。管理员可能还希望避免搜索引擎（如谷歌、雅虎和 DuckDuckGo）索引 BTCPay Server 域名。由于BTCPay Server是自由和开放源码软件（FOSS），世界各地的开发人员可能希望创建新功能。BTCPay Server有一项实验功能，开启后，管理员可以使用不用于生产而是用于测试的功能。



- 查看 GitHub 上的发布版本，并在 BTCPay Server 推出新版本时发出通知。
- 阻止搜索引擎索引本网站
- 启用实验功能。


![image](assets/en/078.webp)


#### 插件


BTCPay 服务器可添加插件并扩展其功能集。默认情况下，插件从 BTCPay Server 插件生成器资源库中加载。不过，管理员可以选择查看处于预发布状态的插件，如果插件开发者允许，服务器管理员现在可以安装测试版插件。


![image](assets/en/079.webp)


##### 自定义设置


标准的 BTCPay 服务器部署可通过安装时设置的域进行访问。不过，服务器管理员可以重新映射根域，并显示从特定商店创建的应用程序之一。服务器管理员还可将特定域映射到特定应用程序。



- 在网站根目录下显示应用程序
  - 显示根域上可能显示的应用程序列表。


![image](assets/en/080.webp)



- 将特定域映射到特定应用程序。
  - 点击为特定应用程序设置特定域时，管理员可根据需要设置指向特定应用程序的任意多个域。


![image](assets/en/081.webp)


#### 街区探险家


BTCPay 服务器标配 Mempool.space 作为交易的 Block explorer。当 BTCPay 服务器生成新的 Invoice 并绑定交易时，店主可点击打开交易。默认情况下，BTCPay 服务器将指向 Mempool.space 作为 Block explorer；但是，服务器管理员可以将其更改为自己喜欢的选项。


![image](assets/en/082.webp)


### 服务


BTCPay 服务器设置：服务 "选项卡概述了 BTCPay 服务器使用的组件。BTCPay 服务器提供的服务可能因部署方式而异。


BTCPay 服务器管理员可点击每项服务后面的 "查看信息"，打开服务并设置具体设置。


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay 公开 LND 的 GRPC 服务供外部使用；您可在此特定设置菜单中找到连接信息；兼容钱包在此列出。BTCPay 服务器还提供用于连接的二维码，扫描后可应用于手机 Wallet。


服务器管理员可以打开更多详细信息查看。



- 主机详细信息
- 使用 SSL
- 马卡龙
- 管理员马卡龙
- 发票马卡龙
- 只读马卡龙
- GRPC SSL 密码套件 (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay 公开了 LND 的 REST 服务供外界使用；您可在此处找到连接信息；兼容钱包在此处列出。兼容的钱包包括 Joule、Alby 和 ZeusLN。BTCPay 服务器为连接提供二维码，扫描后可应用于兼容的 Wallet。



- REST URI
- 马卡龙
- 管理员马卡龙
- 发票马卡龙
- 只读马卡龙


#### LND seed 备份


如果服务器损坏，LND seed 备份可用于恢复 LND Wallet 的资金。由于 "闪电 "节点是 Hot-Wallet，您可以在本页找到 seed 的机密信息。


LND 记录了恢复过程。有关文档，请参见 https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md。


#### 乘风破浪


Ride the Lightning 是一款以开源软件形式构建的闪电节点管理工具。BTCPay服务器使用RTL作为其堆栈中的闪电节点管理组件。BTCPay服务器管理员可通过服务器设置--服务选项卡或点击闪电Wallet进入RTL。


#### Full node P2P


服务器管理员可能希望将 Bitcoin 节点连接到移动 Wallet。本页提供了如何通过 P2P 协议远程连接 Full node 的信息。在编写本课程时，BTCPay 服务器将 Blockstream Green 和 Wasabi 钱包列为兼容钱包。BTCPay 服务器提供了一个用于连接的二维码，扫描后可应用于兼容的 Wallet。


#### Full node RPC


本页面提供通过 RPC 协议远程连接 Full node 的信息。


#### SSH


SSH 用于维护目的。BTCPay 服务器会显示到达服务器的初始连接命令，以及授权连接服务器的 SSH 公钥。服务器管理员可能希望通过 BTCPay 服务器用户界面禁用 SSH 更改。


#### 动态 DNS


动态 DNS 允许您有一个稳定的 DNS 名称指向您的服务器，即使您的 IP Address 经常变化。如果您在家中托管 BTCPay 服务器，并希望有一个明确的域名来访问您的服务器，建议使用动态 DNS。


请注意，您需要正确配置您的 NAT 和 BTCPay 服务器安装，以获取 HTTPS 证书。


### 主题


BTCPay 服务器标配两种主题：浅色和深色模式。点击左下角的 "账户"，在 "深色主题 "和 "浅色主题 "之间切换。BTCPay 服务器管理员可通过提供自定义 CSS 主题来添加自己的主题。


管理员可以通过添加自定义 CSS 或将自定义主题设置为完全自定义主题来扩展亮/暗主题。


![image](assets/en/084.webp)


#### 服务器品牌


服务器管理员可以通过在服务器范围内设置贵公司的品牌来更改 BTCPay 服务器的品牌。由于 BTCPay 服务器是自由和开放源码软件，服务器管理员可以为软件贴上白标签，并定制适合其业务的外观。


![image](assets/en/085.webp)


### 维护


作为服务器管理员，您的用户希望您能妥善管理服务器。在 BTCPay 服务器的 "维护 "选项卡中，管理员可以进行一些必要的维护。为BTCPay服务器实例设置域名，重启或清理服务器。最重要的可能是运行更新。


BTCPay服务器是一个开源项目，更新频繁。每个新版本都会通过您的 BTCPay 服务器通知或 BTCPay 服务器的官方渠道发布。


![image](assets/en/086.webp)


#### 域名


在 BTCPay 服务器设置完成后，管理员可能希望更改原来的域。在 "维护 "选项卡中，管理员可以更改域。点击确认并在网域上设置适当的DNS记录后，BTCPay服务器将更新并重新启动，返回新的网域。


![image](assets/en/087.webp)


#### 重新启动


重启 BTCPay 服务器和相关服务。


![image](assets/en/088.webp)


#### 清洁


BTCPay 服务器使用 Docker 组件运行；随着更新，可能会有残留的 Docker 镜像、临时文件等。服务器管理员可通过运行清理脚本释放空间。


![image](assets/en/089.webp)


#### 更新


这是维护选项卡中最重要的选项。BTCPay Server由社区构建，因此其更新周期比大多数软件产品更频繁。当BTCPay Server发布新版本时，管理员会在通知中心收到通知。点击更新按钮，BTCPay 服务器将检查 GitHub 上的最新版本，更新服务器并重新启动。在更新之前，建议服务器管理员阅读通过 BTCPay Server 官方渠道发布的版本说明。


![image](assets/en/090.webp)


### 日志


面对问题从来都不是一件有趣的事。本文件概述了最常见的工作流程和步骤，以便独立或在社区协助下有效地识别和解决问题。


找出问题所在至关重要。


#### 复制问题


首先要确定问题发生的时间。尝试复制问题。尝试更新并重启服务器，以验证是否能重现问题。如果能更好地描述您的问题，请截图。


##### 更新服务器


检查您的 BTCPay 服务器版本是否比 BTCPay 服务器的 [最新版本](https://github.com/btcpayserver/btcpayserver/releases) 旧得多。更新服务器可能会解决问题。


##### 重启服务器


重启服务器是解决许多最常见的BTCPay服务器问题的简单方法。您可能需要通过SSH连接到您的服务器，以便重启服务器。


##### 重启服务


您可能只需要重启 BTCPay 服务器部署中的特定服务来解决某些问题，例如重启 letsencrypt 容器来更新 SSL 证书。


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


使用 docker ps 查找你想重启的其他服务的名称。


#### 翻阅日志


日志可提供重要信息。在以下段落中，我们将介绍如何获取 BTCPay 各部分的日志信息。


##### BTCPay 日志


自v1.0.3.8版本起，您可以从前端轻松访问BTCPay服务器日志。如果您是服务器管理员，请进入 "服务器设置">"日志"，打开日志文件。如果您不知道日志中的特定错误意味着什么，请在排除故障时提及。


如果您需要更详细的日志，并正在使用 Docker 部署，您可以使用命令行查看特定 Docker 容器的日志。请参阅以下[ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) 进入在 VPS 上运行的 BTCPay 实例的说明。


下一页是 BTCPay 服务器使用的容器名称总览。


运行以下命令可按容器名称打印日志。替换容器名称可查看其他容器日志。


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


使用 Docker 时，有几种方法可以访问 LND 日志。首先，以根用户身份登录：


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


另外，您也可以使用容器 ID 快速打印日志（只需要第一个唯一 ID 字符，如最左边的两个字符）：


```bash
docker logs 'add your container ID'
```


如果出于任何原因，您需要更多的日志


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


您将看到如下内容


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


要访问这些日志的未压缩日志，请执行 `cat LND.log`，如果需要另一个日志，请使用 `cat LND.log.15`。


要访问`.gzip`中的压缩日志，请使用`gzip -d LND.log.16.gz`（在本例中，我们访问的是`LND.log.16.gz`）。这将生成一个新文件，您可以在其中执行 `cat LND.log.16`。如果上面的方法不起作用，你可能需要先用 `sudo apt-get install gzip` 安装 gzip。


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


或者，使用这个：


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


您还可以使用 c-lightning CLI 命令获取日志信息。


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin 节点日志


除了查看 bitcoind 容器的 [日志](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs)，您还可以使用任何 [bitcoin-cli 命令](https://developer.Bitcoin.org/reference/RPC/index.html)


[（打开新窗口）](https://developer.Bitcoin.org/reference/RPC/index.html) 从您的 Bitcoin 节点获取信息。BTCPay 包含一个脚本，可让您与 Bitcoin 节点轻松通信。


在 btcpayserver-docker 文件夹中，使用你的节点获取 Blockchain 信息：


```bash
bitcoin-cli.sh getblockchaininfo
```


### 文件


BTCPay 服务器具有本地文件系统，可直接将商店（产品）资产、徽标和品牌上传到服务器。只有服务器管理员才能访问服务器的文件系统；商店所有者可在商店一级上传其徽标或品牌。


当服务器管理员位于 "文件存储 "选项卡时，可以直接上传到服务器，或将文件存储提供程序更改为本地文件系统或 Azure Blob Storage。


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### 技能概要


在本节中，您将学到以下内容：



- 存储设置和服务器设置的区别，尤其是与用户、角色和电子邮件相关的设置
- 为 Lightning 或 Bitcoin Hot Wallet 的使用和创建、新用户注册和电子邮件通知设置全服务器策略。
- 如何添加自定义主题（而不是提供简单的明暗选项）以及创建自定义徽标
- 通过提供的图形用户界面执行简单的服务器维护任务
- 排除故障，包括获取任何 Docker 容器或节点的详细信息
- 管理文件存储


### 知识评估


#### KA 概念审查


通过服务器和存储设置分配的角色有什么区别？


#### KA 实用评论


描述 "策略 "选项卡中启用的一些可能用例。


#### KA 实用评论


描述管理员在 "维护 "选项卡中可能进行的一些常规操作。


## BTCPay 服务器 - 支付


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice 是卖方向买方发出的收款文件。


在 BTCPay 服务器中，Invoice 代表必须在规定时间内以固定 Exchange 汇率支付的文件。发票有过期日期，因为它们将 Exchange 费率锁定在规定的时间范围内，从而保护收款人免受价格波动的影响。


BTCPay 服务器的核心是作为 Bitcoin Invoice 管理系统的能力。Invoice 是跟踪和管理已收付款的重要工具。


除非使用内置 [Wallet](https://docs.btcpayserver.org/Wallet/) 手动接收付款，否则商店内的所有付款都将显示在发票页面。该页面按日期对付款进行累计排序，是 Invoice 管理和付款故障排除的中心资源。


![image](assets/en/093.webp)


### 一般情况


#### Invoice 状态


下表列出并描述了 BTCPay 中的标准 Invoice 状态，以及建议采取的常见措施。操作只是建议。用户可根据自己的使用情况和业务确定最佳行动方案。


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Invoice 详情


Invoice 详情页面包含与 Invoice 有关的所有信息。


根据 Invoice 状态、Exchange 比率等自动创建 Invoice 信息。如果 Invoice 是与产品信息（如在销售点应用程序中）一起创建的，则会自动创建产品信息。


#### Invoice 过滤器


可以通过搜索按钮旁边的快速筛选器或高级筛选器过滤发票，点击顶部的（帮助）链接可以切换高级筛选器。用户可以按商店、订单 ID、项目 ID、状态或日期过滤发票。


#### Invoice 出口


BTCPay 服务器发票可以 CSV 或 JSON 格式导出。有关 Invoice 导出和会计的更多信息。


#### 退还 Invoice


如果出于任何原因想退款，您可以从 Invoice 视图轻松创建退款。


#### 发票存档


由于BTCPay服务器没有Address重复使用功能，因此在您商店的Invoice页面上经常会看到许多过期发票。要从您的视图中隐藏它们，请在列表中选择它们并标记为存档。标记为存档的发票不会被删除。您的 BTCPay 服务器仍会检测到对已存档 Invoice 的付款（paidLate 状态）。您可以从搜索过滤器下拉菜单中选择存档发票，随时查看商店的存档发票。


#### 默认货币


商店默认货币，在商店创建向导中设置。


#### 允许任何人创建 Invoice


如果您想让外界在您的商店中创建发票，则应启用此选项。该选项只有在您使用支付按钮或通过 API 或第三方 HTML 网站开具发票时才有用。PoS 应用程序已预先授权，随机访客打开 POS 商店并创建 Invoice 时不需要启用此设置。


#### 为 Invoice 增加额外费用（网络费



- 仅当客户为 Invoice 付款超过一次时
- 每次付款
- 绝不增加网络费用


#### 如果在...分钟后仍未全额付款，Invoice 将失效。


Invoice 的计时器默认设置为 15 分钟。定时器是一种防止波动的保护机制，因为它根据加密货币对非加密货币的汇率锁定加密货币金额。如果客户没有在规定时间内支付 Invoice，Invoice 将被视为过期。一旦交易在 Blockchain 上可见（确认次数为零），Invoice 即被视为 "已支付"；当交易达到商家定义的确认次数（通常为 1-6）时，Invoice 即被视为 "已完成"。计时器是可定制的。


#### 即使支付的金额比预期的少 .%，也视为已支付 Invoice。


在客户使用 Exchange Wallet 直接支付 Invoice 的情况下，Exchange 会收取少量费用。这意味着这样的 Invoice 不被视为完全完成。Invoice 会被标记为 "部分支付"。如果商家希望接受未足额支付的发票，可以在此处设置百分比率


### 要求


付款申请是一项允许 BTCPay 店主创建长期发票的功能。根据支付请求，使用支付时有效的 Exchange 费率支付资金。这样，用户就可以在方便的时候付款，而无需在付款时与店主协商或验证 Exchange 费率。


用户可以分期付款。付款申请将一直有效，直到全额支付或店主要求的到期时间。地址不会重复使用。每次用户点击付款时，都会生成一个新的 Address，为付款申请创建一个 Invoice。


店主可打印付款申请（或导出 Invoice 数据），用于保存记录和记账。BTCPay 会在店铺的 Invoice 列表中自动将发票标记为付款申请。


#### 自定义付款请求



- Invoice 金额 - 设置要求的付款金额
- 面额 - 以法定货币或加密货币显示申请金额
- 付款数量 - 只允许一次付款或部分付款
- 过期时间 - 允许付款至某一日期或无过期时间
- 说明 - 文本编辑器、数据表、嵌入照片和视频
- 外观 - CSS 主题的颜色和样式


![image](assets/en/094.webp)


#### 创建付款申请


在左侧菜单中，转到付款申请，然后单击 "创建付款申请"。


![image](assets/en/095.webp)


提供申请名称、金额、显示面额、相关商店、有效时间和描述（可选）


如果要允许部分付款，请选择 "允许收款人按其面额创建发票 "选项。


单击 "保存并查看 "查看您的付款申请。


BTCPay 为付款请求创建一个 URL。分享该 URL 以查看您的付款请求。需要多个相同请求？您可以使用主菜单中的克隆选项复制付款请求。


![image](assets/en/096.webp)


**警告**


支付请求与商店有关，这意味着每个支付请求在创建时都与商店相关联。请务必将 Wallet 连接到付款申请所属的商店。


#### 付费申请


收款人和请求人可在付款发送后查看付款请求的状态。如果已全额收到付款，状态将显示为已结算。如果只支付了部分款项，"应付金额 "将显示余额。


![image](assets/en/097.webp)


#### 自定义付款请求


可以使用付款申请的文本编辑器编辑描述内容。如果您想使用其他颜色主题或自定义 CSS 样式，这两个选项都可用。


非技术用户可以使用 [bootstrap 主题](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes)。如下所示，通过提供额外的 CSS 代码，可以进一步定制。


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### 拉动付款


传统上，接收方共享其 Bitcoin Address 以进行 Bitcoin 支付，发送方随后向该 Address 发送资金。这种系统被称为 "推送支付"，因为发送方在接收方可能无法使用的情况下发起支付，并将支付推送给接收方。


然而，角色颠倒又如何呢？


如果发送方不推送付款，而是允许接收方在接收方认为合适的时间拉动付款，会怎么样呢？这就是拉动式支付的概念。这样就有了几种新的应用，例如



- 订阅服务（订阅者允许该服务每隔 X 时间提取资金）
- 退款（商家允许客户在其认为合适时将退款转入其 Wallet 中）
- 自由职业者按时间计费（雇佣者允许自由职业者在报告时间后将钱转入其 Wallet 账户）
- 赞助（赞助人允许受助人每月提取资金，以继续支持他们的工作）
- 自动销售（Exchange 的客户允许 Exchange 每月自动从其 Wallet 中提取资金进行销售）
- 余额提款系统（大容量服务允许用户请求从其余额中提款，然后该服务可以轻松地按固定时间间隔向许多用户批量支付所有款项）


### 付款


支付功能与[Pull Payments](https://docs.btcpayserver.org/PullPayments/)功能相关联。该功能允许您在 BTCPay 中创建付款。该功能允许您处理拉动支付（退款、工资支付或提现）。


#### 例 1：退款


让我们以退款为例。顾客在你的商店购买了一件商品，但不幸的是，他们必须退货。他们想要退款。在 BTCPay 中，您可以创建一个 [退款](https://docs.btcpayserver.org/Refund/)，并向客户提供申请退款的链接。一旦客户提供了他们的 Address 并要求退款，退款就会显示在 "付款 "部分。


它的第一个状态是等待审批。店员可以查看是否有多个正在等待，做出选择后，您可以使用 "操作 "按钮。


操作按钮上的选项



- 批准选定的付款
- 批准和发送选定的付款
- 取消选定的付款


下一步是批准和发送选定的付款，因为我们要向客户退款。检查客户的 Address，其中显示了金额以及我们是否希望从退款中扣除费用。完成检查后，剩下的步骤就是签署交易。


客户现在会在申请页面上得到更新。他可以通过 Block explorer 和他的交易链接跟踪交易。一旦交易得到确认，其状态就会变为 "已完成"。


#### 例 2：工资


现在我们来谈谈薪金支付，因为它是由商店内部驱动的，而不是根据客户的要求。其基本概念是一样的，都是利用拉动支付。但我们要做的不是退款，而是[拉动支付](https://docs.btcpayserver.org/PullPayments/)。


进入 BTCPay 服务器的 "拉动支付 "选项卡。在右上角，点击 "创建拉动支付 "按钮。


现在我们开始创建付款，给它起个名字，并以所选货币设定所需的金额。填写 "说明"，以便员工知道它的用途。下一部分与退款类似。员工填写目的地 Address 和他想从这笔付款中申请的金额。他可能会决定分两次申请，向不同的地址申请，甚至在闪电中申请一部分。


如果有多个等待的付款，可以批量签署并发送。一旦签署，付款就会移动到 "进行中 "选项卡，并显示 "交易"。网络接受后，赔付会移动到 "已完成 "选项卡。已完成选项卡纯粹是为了历史目的。它保存已处理的付款和属于它的交易。


### 拉动付款


#### 概念


发件人配置拉式付款时，可以配置一系列属性：



- 拉取请求名称
- 限额
- 单位（如 BTC、SAT、USD）
- 付款方式
  - BTC On-Chain
  - BTC off-chain
- 说明
- 自定义 CSS
- 结束日期（Lightning Network BOLT11 为可选项）


之后，发送方可以通过链接与接收方分享拉动付款，让接收方创建付款。收款人将选择他们的付款方式：



- 使用哪种付款方式
- 向何处汇款


一旦创建了付款，该付款将计入当期的拉动付款限额。然后，发送方将通过设置发送付款的费率来批准付款，并继续付款。


对于发件人，我们提供了一种简单易用的方法，可从 [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/)批量支付多笔款项。


#### 绿地应用程序接口


BTCPay服务器为发送方和接收方提供完整的API，该API在您的实例的"/docs "页面有详细说明。(或文档网站 https://docs.btcpayserver.org）


由于我们的应用程序接口提供了拉动支付的全部功能，发送方可以根据自己的需要自动进行支付。


### 技能概要


在本节中，您将学到以下内容：



- 深入了解 BTCPay 服务器的 Invoice 状态以及可对其执行的操作
- 定制和管理被称为 "请求 "的延长使用寿命的 Invoice 机制。
- BTCPay 服务器独特的拉动支付功能提供了更多灵活的支付可能性，特别是在处理退款和工资支付方面。


### 知识评估


#### KA 概念审查


发票和付款申请之间有哪些区别，使用后者的理由是什么？


#### KA 概念审查


拉动式支付如何扩展 On-Chain 的典型功能？描述一些它们可以实现的使用案例。


## BTCPay 服务器默认插件


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### 默认插件和应用程序


BTCPay 服务器配有一套标准插件（应用程序），可将 BTCPay 服务器转变为电子商务支付网关。通过添加销售点、众筹平台和简易支付按钮，BTCPay 服务器将成为一个易于部署的解决方案。


### 销售点


销售点（PoS）是 BTCPay 服务器的标准插件之一。使用 PoS 插件，店主可直接从 BTCPay 服务器创建网店；店主无需第三方电子商务解决方案即可运营网店。基于网络的 PoS 应用程序使拥有实体店的用户能够轻松接受 Bitcoin，无需费用或第三方，直接输入 Wallet。PoS 可以在平板电脑或其他支持网络浏览的设备上轻松显示。用户可以轻松创建主屏幕快捷方式，快速访问网络应用程序。


#### 如何创建新的销售点


BTCPay Server 使店主能够快速创建多种布局的销售点。BTCPay Server 认识到并非每家商店都是电子商务商店，也并非每家商店都是酒吧或餐馆，因此为您的 PoS 提供了多种标准设置。


当店主点击左侧菜单栏中的 "Point of Sale（销售点）"时，BTCPay 服务器会要求输入名称；该名称将在左侧菜单栏中显示。点击 "创建 "即可创建 PoS。


![image](assets/en/098.webp)


#### 更新新创建的销售点


创建新的 PoS 后，您可以通过以下屏幕更新销售点并为商店添加商品。


##### 应用程序名称


您的销售点名称将在 BTCPay 服务器的主菜单中显示。


##### 显示标题


公众访问时会看到您店铺的标题或名称。BTCPay 服务器默认将您的店铺命名为 "茶叶店"。请将其替换为您的店铺名称。


![image](assets/en/099.webp)


#### 选择销售点风格


BTCPay 服务器能够以多种方式显示其销售点。



- 产品列表
  - 顾客一次只能购买一种产品的商店视图。
- 带购物车的产品列表。
  - 商店视图，顾客可以一次购买多个商品，并在屏幕右侧看到购物车概览。
- 仅键盘
  - 没有产品清单，只有一个直接开票的键盘。
- 打印展示（带 QR 的可打印产品列表）
  - 如果您不能总是以数字方式显示您的产品列表，您需要一个 "离线 "产品解决方案；BTCPay 服务器具有打印显示功能，可作为离线商店使用。


![image](assets/en/100.webp)


#### 销售点风格 - 产品列表


![image](assets/en/101.webp)


#### 销售点风格 - 产品清单 + 购物车


![image](assets/en/102.webp)


#### 销售点样式 - 仅键盘


![image](assets/en/103.webp)


#### 销售点风格 - 印刷展示


![image](assets/en/104.webp)


#### 货币


商店所有者可为其销售点设置与总体默认设置货币不同的货币。商店的默认货币将自动填充此字段。


#### 说明


向全世界介绍你的商店；你卖什么，卖多少钱？在这里，您可以介绍您的商店。


![image](assets/en/105.webp)


#### 产品


创建销售点时，标准 BTCPay 服务器会在商店中添加一些项目供参考。点击任何标准项目上的 "编辑 "按钮，可以更好地了解项目的每个可能选项。


在商店中创建新产品包括以下字段；



- 标题
- 价格（固定价格、最低价格或自定义价格）
- 图片 URL
- 说明
- 库存
- 身份证
- 购买按钮文本。
- 启用/禁用


店主填写完所有新产品字段后，点击保存，你会发现销售点的产品部分现在已经填好了。请务必在屏幕右上角保存，以防店主在添加产品时丢失进度。


店主还可以使用 "原始编辑器 "来配置产品。原始编辑器要求对 JSON 结构有基本的了解。


![image](assets/en/106.webp)


#### 结账


BTCPay 服务器允许对小型 PoS 特定结账进行定制。店主可以设置 "购买 x "文本，或通过添加到表单中来要求特定的客户数据。


#### 小贴士


只有部分商店需要销售提示选项。店主可以根据自己的店铺情况打开或关闭该选项。如果店铺使用的是已打开的小费，店主可在字段中设置自己喜欢的小费文本。BTCPay 服务器的小费按百分比计算。店主可以添加多个百分比，以逗号分隔。


#### 折扣


作为店主，您可能希望在结账时给顾客提供自定义折扣；在您的商店结账时，"折扣 "切换按钮将变得可用。不过，强烈建议不要使用自助结账系统。


#### 自定义付款


打开 "自定义付款 "选项后，客户可以输入一个等于或高于商店生成的原始 Invoice 的设定价格。


#### 附加选项


在为销售点设置好一切之后，还剩下一些额外的选项。店主可以通过 Iframe 轻松嵌入 PoS，或嵌入一个链接到特定商店项目的付款按钮。为了使刚刚创建的 PoS 商店风格化，店主可以在附加选项的底部添加自定义 CSS。


#### 删除此应用程序


如果店主希望从其 BTCPay 服务器中完全删除销售点，在更新 PoS 的底部，店主可点击 "删除此应用程序 "按钮，完全销毁其 PoS 应用程序。点击 "删除此应用程序 "时，BTCPay 服务器会要求输入 "DELETE "并点击 "删除 "按钮确认。删除后，店主将返回 BTCPay 服务器控制面板。


### BTCPay 服务器 - 众筹


除了销售点插件，BTCPay 服务器还提供创建众筹的选项。就像其他众筹平台一样，店主可以设定目标，为捐款创建福利，并根据自己的需要进行定制。


#### 如何设立新的众筹基金


在BTCPay服务器左侧主菜单的插件部分下方点击众筹插件。BTCPay 服务器现在会要求为众筹基金命名；该名称也将显示在左侧菜单栏中。


![image](assets/en/107.webp)


#### 更新新创建的销售点


给应用程序命名后，下一个界面将是更新应用程序的上下文。


#### 应用程序名称


在 BTCPay 服务器的主菜单中将显示您的众筹基金名称。


#### 显示标题


标题是面向公众的众筹。


#### 标语


用一句话概括众筹的目的。


![image](assets/en/108.webp)


#### 特色图片 URL


每个众筹都有自己的主图片，即您能直接识别的横幅。如果您有管理权限，该图片可以存储在您的服务器上。管理员可在 BTCPay 服务器设置 - 文件下上传。如果您是商店所有者，则必须通过第三方主机（例如 Imgur）将图片上传到网络。


#### 公开众筹


该切换使您的众筹公开，从而对外界可见。出于测试目的或查看您的主题是否应用正确，请在建立众筹期间将其设置为 "关闭"。


#### 说明


向世界介绍您的众筹。您筹集资金的目的是什么？在此介绍您的众筹项目。


![image](assets/en/109.webp)


#### 众筹目标


为筹款人应该为项目赚取的收入设定一个目标，并确定目标的货币单位。如果您的目标是在不同日期之间设定的，请确保在众筹目标下方包含这些目标和结束日期。


![image](assets/en/110.webp)


#### 福利


福利可以大大加强您的众筹活动。这是因为福利为人们提供了参与活动的途径。它们既能激发人们自私的动机，也能激发人们善意的动机。它们还能让你了解支持者的消费情况，而不仅仅是他们的慈善钱包--你可以猜猜哪个更重要。


创建新津贴包括以下字段。



- 标题
- 价格（固定价格、最低价格或自定义价格）
- 图片 URL
- 说明
- 库存
- 身份证
- 购买按钮文本。
- 启用/禁用


店主填写完新津贴的所有字段后，点击保存，您会发现 "众筹 "中的 "津贴 "部分已被填写。


![image](assets/en/111.webp)


### BTCPay 服务器 - 销售点


#### 会费


店主可以选择如何显示津贴、如何对津贴进行排序，甚至将津贴与其他津贴进行排名。不过，一旦达到众筹目标，店主可能希望停止向该筹款活动捐款。因此，他可以切换 "达到目标后不允许额外捐款"。这将阻止众筹接受捐款。


##### 众筹行为


Crowdfund 的标准只将使用 Crowdfund 创建的发票计入目标。但是，在某些情况下，商店所有者可能希望将该商店开具的所有发票都计入众筹资金。


#### 其他定制选项


BTCpay 服务器提供了一些额外的自定义功能。您可以在众筹中添加声音、动画甚至讨论主题。店主还可以通过输入自己的自定义 CSS 来修改众筹的外观和感觉。


#### 删除此应用程序


如果店主希望从其BTCPay服务器中完全删除众筹，可在更新众筹的底部点击 "删除此应用程序 "按钮，以完全删除其众筹应用程序。点击 "删除此应用程序 "时，BTCPay服务器会要求输入 "DELETE "并点击 "删除 "按钮确认。删除后，店主将返回 BTCPay 服务器控制面板。


### BTCPay 服务器 - 支付按钮


可轻松嵌入的HTML和高度自定义的支付按钮允许店主接收小费和捐款。在 BTCPay 服务器左侧菜单栏的插件部分下方，店主可以点击 "支付按钮"，然后点击 "启用 "来创建支付按钮。


#### 常规设置


在支付按钮的常规设置中，店主可以设置



- 标准价格
- 默认货币
- 默认付款方式
  - 使用存储默认值
  - BTC On-Chain
  - BTC off-chain（闪电）
  - BTC off-chain (LNURL-pay)
- 结账说明
- 订单编号


#### 显示选项


BTCPay 服务器的支付按钮可根据不同风格进行配置。按钮可以有固定金额或自定义金额，通过滑块或加减拨动来显示。


#### 使用模态


在创建付款按钮时，店主可以选择顾客点击按钮时的行为，并将其显示在模态或新页面中。


**注意！**


警告：付款按钮只能用于支付小费和捐款


不建议在电子商务集成中使用付款按钮，因为用户可以修改订单相关信息。对于电子商务，您应使用我们的 Greenfield API。如果该商店处理商业交易，我们建议在使用支付按钮前创建一个单独的商店。


#### 自定义支付按钮文本


默认情况下，BTCPay 服务器的付款按钮显示 "Pay With BTCPay"（使用 BTCPay 付款）。店主可根据自己的需要设置该文本，并将 BTCPay Server 徽标更改为自己的徽标。使用 "支付按钮文本 "设置文本，并在 "支付按钮图片URL "下粘贴图片URL。


##### 图像大小


按钮中图像的大小只能设置为三种默认值。



- 146x40px
- 168x46px
- 209x57px


#### 按钮类型


BTCPay 服务器知道支付按钮有三种状态。



- 固定金额
  - 之前设定的价格在按钮的常规设置中。
- 自定义金额
  - BTCPay 服务器的 "支付 "按钮上有 + 和 - 拨动按钮，用于设置自定义价格。
  - 使用自定义金额时，BTCPay 服务器将要求提供最小值、最大值以及逐渐增加的幅度。
  - 可将按钮设置为 "使用简单输入样式"。
  - 在按钮和切换按钮显示为内嵌式时，将按钮调整为内嵌式。
- 滑块
  - 与自定义金额类似，但视觉效果不同，因为它是一个滑块，而不是 +/- 拨动式。
  - 使用滑块时，BTCPay 服务器会要求设置最小值、最大值以及逐渐增加的幅度。


**注意！**


可以删除警告说明顶部的付款按钮。


#### 付款通知


服务器 IPN（即时付款通知）专为网络钩子设计，可通过 URL 配置购买后数据。


#### 电子邮件通知


无论何时付款，BTCPay 服务器都会通知店主。


#### 浏览器重定向


当顾客完成购买时，如果店主设置了该链接，他将被重定向到该链接。


#### 高级付款按钮选项


指定 Invoice 创建后应附加到结账页面的其他查询字符串参数。例如，"lang=da-DK "将默认以丹麦语加载结账页面。


#### 将应用程序用作端点


您可以将付款按钮直接链接到以前使用过的 PoS 或众筹应用程序中的某个项目。


店主可以点击下拉菜单，选择所需的应用程序；选择应用程序后，店主就可以添加需要链接的项目。


#### 生成代码


由于 BTCPay 服务器的付款按钮是一种易于嵌入的 HTML，因此 BTCPay 服务器在配置付款按钮后，会在底部显示生成的代码，以便复制到网站中。


店主可将生成的代码复制到自己的网站上，BTCPay 服务器的支付按钮就会直接在网站上激活。


#### 付款通知


服务器 IPN（即时付款通知）专为网络钩子设计，可配置 URL 以发布购买数据。


#### 电子邮件通知


无论何时付款，BTCPay 服务器都会通知店主。


#### 浏览器重定向


当顾客完成购买时，如果店主设置了该链接，他将被重定向到该链接。


#### 高级付款按钮选项


指定 Invoice 创建后应附加到结账页面的其他查询字符串参数。例如，"lang=da-DK "将默认以丹麦语加载结账页面。


#### 将应用程序用作端点


您可以将付款按钮直接链接到以前使用过的 PoS 或众筹应用程序中的某个项目。店主可以点击下拉菜单，选择所需的应用程序。选择应用程序后，店主就可以添加需要链接的项目。


#### 生成代码


由于 BTCPay Server 的付款按钮是一种易于嵌入的 HTML，因此 BTCPay Server 在配置付款按钮后，会在底部显示生成的代码，以便复制到网站中。店主可将生成的代码复制到自己的网站，这样 BTCPay Server 的支付按钮就会直接在其网站上激活。


### 技能概要


在本节中，您将学到



- 如何使用 BTCPay Server 的集成 PoS 插件轻松创建自定义商店
- 如何使用 BTCPay Server 集成的众筹插件轻松创建自定义众筹应用程序
- 使用支付按钮插件为自定义支付按钮生成代码


### 知识评估


#### KA 回顾


BTCPay 服务器标配的三个内置插件是什么？请用几句话描述每个插件的使用方法。


# 配置 BTCPay 服务器


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## 基本了解如何在 LunaNode 环境中安装 BTCPay 服务器


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### 在托管环境（LunaNode）上安装 BTCPay 服务器


这些步骤将提供开始在 LunaNode 上使用 BTCPay 服务器的所有必要信息。部署软件有多种选择。

您可以在 https://docs.btcpayserver.org 找到 BTCPay 服务器的所有详细信息。


#### 我们从哪里开始？


在本部分中，您将熟悉作为托管服务提供商的 LunaNode，了解使用 BTCPay 服务器的第一步，并学习如何使用 Lightning Network。完成所有步骤后，您就可以运行接受 Bitcoin 的网店或众筹平台了！


这是部署 BTCPay 服务器的多种方法之一。详情请阅读我们的文档。


https://docs.btcpayserver.org。


### BTCPay 服务器 - LunaNode 部署


#### LunaNode 部署


首先，访问 LunaNode.com 网站，在此创建一个新账户。点击右上角的 "注册 "或使用主页上的 "开始向导"。


![image](assets/en/112.webp)


创建新账户后，LunaNode 会发送一封验证电子邮件。一旦您验证了账户，与 Voltage 相比，您将立即看到充值账户余额的选项。该余额是支付服务器空间和托管费用所必需的。


![image](assets/en/113.webp)


#### 为您的 LunaNode 账户添加信用额度


点击 "存入信用额度 "后，您可以设置账户充值金额和支付方式。LunaNode 和 BTCPay 服务器每月的费用在 10 美元到 20 美元之间。

与 Voltage.cloud 相比，您可以完全访问您的虚拟专用服务器 (VPS)，从而对您的服务器拥有更多控制权。创建新账户后，LunaNode 会发送一封验证电子邮件。

与 Voltage 相比，验证账户后，您将立即看到充值账户余额的选项。该余额是支付服务器空间和托管费用所必需的。


#### 如何部署新服务器？


在本指南中，我们将指导您创建一组 API 密钥，并使用 LunaNode 开发的 BTCPay 服务器启动器，完成整个设置过程。


在 LunaNode 仪表板中，单击右上角的 API。这会打开一个新页面。我们只需为 API 密钥设置一个名称。其余部分将由 LunaNode 处理，本指南不再涉及。单击 "创建 API 凭证 "按钮。

创建 API 证书后，您会得到一长串字母和字符。这就是您的 API 密钥。


![image](assets/en/114.webp)


#### 如何部署新服务器？


这些凭证分为两部分，API key 和 API ID；我们需要这两个部分。在进入下一步之前，让我们在浏览器中打开第二个标签页，然后访问 https://launchbtcpay.lunanode.com/


这里会要求您提供 API 密钥和 API ID。这是为了让你知道是你提供了这个新服务器。API 密钥应仍在上一个标签页中打开；如果在下表中向下滚动，就能找到 API ID。


您可以返回启动器页面，填写 API 密钥和 ID，然后点击继续。


![image](assets/en/115.webp)


下一步，您可以提供一个域名。如果您已经拥有一个域名，并希望将其用于 BTCPay 服务器，请确保您也添加了域名的 DNS 记录（称为 `A` 记录）。如果您没有域名，请使用 LunaNode 提供的域名（您可以稍后在 BTCPay 服务器设置中进行更改），然后点击继续。


了解更多有关为 BTCPay 服务器设置或更改 DNS 记录的信息；https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### 在 LunaNode 上启动 BTCPay 服务器


完成之前的步骤后，我们就可以为新服务器设置所有选项了。在此，我们将选择 Bitcoin (BTC) 作为支持货币。我们还可以设置接收加密证书更新通知的电子邮件，这是可选项。


本指南旨在设置 Mainnet 环境（现实世界中为 Bitcoin）；不过，LunaNode 也允许您出于开发目的将其设置为 Testnet 或 Regtest。本指南将保留 Mainnet 选项。


您可以选择自己的 Lightning 实现。LunaNode 提供两种不同的实现方式：LND 和 Core Lightning。在本指南中，我们将使用 LND。这两种实现方式的差异虽小，但都是真实存在的；如欲了解更多信息，建议阅读大量文档：https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln。


![image](assets/en/116.webp)


LunaNode 提供多种虚拟机 (VM) 计划。这些计划的价格范围和服务器规格各不相同。在本指南中，使用 m2 计划就足够了；但是，如果您选择的货币不只是 Bitcoin，请考虑至少使用 m4 计划。


加速初始 Blockchain 同步；这是可选的，取决于你的需求。还有一些高级选项，如设置闪电别名、指向特定的 GitHub 版本或设置 SSH 密钥；本指南将不涉及这些内容。


填写完表格后，您只需点击启动虚拟机，Lunanode 就会开始创建您的新虚拟机，包括安装在上面的 BTCPay 服务器。这个过程需要几分钟；服务器准备就绪后，LunaNode 会向您提供新 BTCPay 服务器的链接。


创建过程结束后，点击 BTCPay 服务器链接；在此，您将被要求创建一个管理员账户。


![image](assets/en/117.webp)


### 技能概要


在本节中，您将学到



- 创建 LunaNode 账户并为其提供资金
- 使用 BTCPay 服务器启动器创建自己的服务器


### 知识评估


#### KA 概念审查


说明在 VPS 上运行 BTCPay 服务器实例与在托管实例上创建账户之间的一些区别。


## 在电压环境中安装 BTCPay 服务器


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


您将熟悉托管服务提供商 Voltage.cloud，了解使用 BTCPay 服务器的第一步，并学习如何使用 Lightning Network。完成所有步骤后，您就可以运行接受 Bitcoin 的网店或众筹平台了！


这是部署 BTCPay 服务器的多种方法之一。详情请阅读我们的文档。

https://docs.btcpayserver.org。


### BTCPay 服务器 - Voltage.cloud 部署


首先，访问网站 Voltage.cloud，注册一个新账户。创建账户时，您可以注册 7 天免费试用。点击右上角的 "注册 "或使用主页上的 "免费试用 7 天"。


![image](assets/en/118.webp)


注册账户后，点击仪表板上的 "节点 "按钮。选择 "节点 "并创建新节点后，我们将看到 Voltage 提供的可能节点。由于本指南还将介绍 Lightning Network，因此在创建 BTCPay 服务器之前，我们首先需要选择我们的 Lightning 实现。点击 LightningNode。


![image](assets/en/119.webp)


在这里，您需要选择所需的闪电节点类型。Voltage 有多种照明设置选项。这与部署 LunaNode 时的情况不同。在本指南中，使用 Lite 节点就足够了。请阅读 Voltage.cloud 中有关差异的更多信息。


![image](assets/en/120.webp)


为节点命名、设置密码并确保密码安全。如果密码丢失，您将无法访问备份，Voltage 也无法恢复密码。创建节点，Voltage 会向你显示创建进度。Voltage 已创建了你的 "闪电节点"。现在我们可以创建 BTCPay 服务器实例，并直接访问 Lightning Network。


点击仪表盘左上角的节点。在这里，您可以设置 BTCPay 服务器实例的下一部分。进入节点概览后，点击 "创建新节点"。您将看到与之前类似的界面。现在，我们选择 BTCPay Server，而不是 Lightning Node。


Voltage 向您显示 BTCPay 服务器的地理位置，该服务器托管在美国西部地区。在这里，您还可以看到托管服务器的费用。点击创建，为 BTCPay 服务器命名。启用 "闪电"，Voltage 会显示上一步创建的 "闪电 "节点。点击创建，Voltage 将创建一个 BTCPay 服务器实例。


![image](assets/en/121.webp)


点击创建后，Voltage 会显示默认用户名和密码。这与您之前在 Voltage 设置的密码类似。点击 "登录账户 "按钮，您将被重定向到您的 BTCPay 服务器。


欢迎使用您的新 BTCPay 服务器实例。由于我们在创建过程中已经设置了闪电功能，因此会显示闪电功能已经启用！


### 技能概要


在本章中，您将学到



- 在 Voltage.cloud 上创建账户
- 让 BTCPay 服务器与账户上的 Lightning 节点一起运行的步骤


### 知识评估


#### KA 概念审查


Voltage 和 LunaNode 设置之间有哪些主要区别？


## 在 Umbrel 节点上安装 BTCPay 服务器


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


完成这些步骤后，您就可以在本地网络上接受闪电支付到您的 BTCPay 商店。如果您在餐厅或企业中运行 umbrel 节点，此过程同样适用。如果您想将该商店连接到公共网站，请按照高级练习向公众展示您的伞状节点。


https://umbrel.com/


![image](assets/en/122.webp)


### BTCPay 服务器 - Umbrel 部署


在您的 Umbrel 节点与 Bitcoin Blockchain 完全同步后，进入 Umbrel 应用程序商店，在应用程序下方搜索 BTCPay 服务器。


![image](assets/en/123.webp)


点击 BTCPay Server 查看应用程序详细信息。打开 BTCPay Server 的详细信息后，右下角会显示应用程序正常运行的要求。它显示需要Bitcoin和Lightning节点。如果您尚未在 Umbrel 上安装闪电节点，请点击安装。这个过程可能需要几分钟。


![image](assets/en/124.webp)


安装闪电节点后


1.单击应用程序详细信息中的打开或 Umbrels 面板中的应用程序。

2.单击 "设置新节点"，系统将显示 24 个用于恢复闪电节点的单词。

3.把这些写下来。


![image](assets/en/125.webp)


Umbrel 会要求验证刚才写下的文字。设置好闪电节点后，返回 Umbrel 应用商店，找到 BTCPay 服务器。点击安装按钮，Umbrel 会显示所需组件是否已安装，以及 BTCPay Server 是否需要访问这些组件。安装完成后，点击应用程序详情右上方的 "打开"，或通过 Umbrels 面板打开 BTCPay Server。


Umbrel 会要求核实刚才写下的文字。


![image](assets/en/126.webp)


**注意！**


确保将这些物品存放在安全的地方，就像之前在存放钥匙时学到的那样。


Lightning 节点设置完成后，返回 Umbrel 应用商店，找到 BTCPay Server。点击安装按钮，Umbrel 将显示所需组件是否已安装，以及 BTCPay Server 是否需要访问这些组件。


![image](assets/en/127.webp)


安装完成后，点击应用程序详情右上方的 "打开"，或通过 Umbrels 面板打开 BTCPay Server。


![image](assets/en/128.webp)


### 技能概要


在本节中，您将学到



- 在 Umbrel 节点上安装具有 Lightning 功能的 BTCPay 服务器的步骤


### 知识评估


#### KA 概念审查


Umbrel 上的设置与前两个托管选项有何不同？


# 最后部分


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## 评论与评级

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## 课程总结


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>