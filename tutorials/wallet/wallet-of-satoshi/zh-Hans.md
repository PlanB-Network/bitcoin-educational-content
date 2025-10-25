---
name: Wallet of Satoshi
description: 最简单的托管 Wallet 开始使用
---
![cover](assets/cover.webp)

_本教程由_ [Bitcoin 校园](https://linktr.ee/bitcoincampus_) 编写


## 下载、设置和使用 Satoshi 的 Wallet


Satoshi 的 Wallet 是 Lightning Network 的 Wallet，具有监护功能，使用非常简单。

就课程[BTC105 - Finding Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5)而言，它用于 Redeem Lightning Network 凭证。


**永远记住**：不是你的钥匙，也不是你的硬币_


托管钱包不允许用户完全控制自己的资金。除初学者外，通常不建议使用托管钱包。WoS 应作为过渡性 Wallet 或用于存放零用钱，而不是用于长期资金积累。


---

Wallet of Satoshi（WoS）是一种托管产品，但它有一定的声誉。例如，我们可以合理地求助于 WoS 这样的工具来提高我们接收流动性的能力。我们暂时把代为管理渠道流动性的 "脏活 "交给 WoS。一旦达到一定数量，我们将清空 WoS On-Chain 到我们的非托管 Wallet。


**警告⚠️：建议在继续**之前阅读本教程的全部内容


### 下载 Satoshi 的 Wallet


前往 Play Store 下载 WoS


![image](assets/it/01.webp)


**注意：** WoS 只能从官方商店下载。如果设备的操作系统已编程，则在打开 WoS 前，操作系统本身会进行验证。验证阶段结束后，请选择_Open_（打开）。


![image](assets/it/02.webp)


在打开 Satoshi 的 Wallet 时，会出现以下界面，需要点击_Start_（开始）。


![image](assets/it/03.webp)


### 注册 WoS 账户


此时，Wallet 已经开始运行，但为了更安全起见，我们还需要设置一个登录名：在设备出现故障或丢失的情况下，需要用它来恢复资金。因此，请选择左上角的菜单。


![image](assets/it/04.webp)


整个菜单窗口将打开，您必须在其中根据喜好设置货币（Satoshi 的 Wallet 默认将美元作为参考货币）和主题颜色（浅色/深色）。请勿使用其他命令。


由于 WoS 是一种保管工具，我们无法用 Mnemonic 短语备份 Wallet，但我们可以通过点击_登录/注册_，在移动设备丢失或无法使用的情况下，使 WoS 能够收回我们的资金。

出现一个窗口，要求我们输入电子邮件 Address。该电子邮件可以是**Proton 邮件**（推荐），但必须能正常使用，因为一旦手机丢失/被盗或损坏，我们可以通过它找回 Wallet 中的资金。


![image](assets/it/08.webp)


Satoshi 的 Wallet 已向指定的电子邮件收件箱发送信息。


![image](assets/it/09.webp)


在邮箱中，我们会发现两个单词，我们需要在应用程序提供的空白处输入并改写这两个单词。


- 请勿启动翻译器：这些词语仍然是英语
- 重写这两个词，注意大写/小写


![image](assets/it/10.webp)


转录完这两个单词后，点击 _OK_。


![image](assets/it/11.webp)


结果应该是图像出现在顶部，并带有用于验证的复选标记。


![image](assets/it/12.webp)


在设置部分，红色的_登录/注册_栏现在会显示用户的电子邮件 Address。


![image](assets/it/13.webp)


### 接收付款


要在 WoS 上接收信息，请单击_Receive_（接收），然后会出现一系列命令。


![image](assets/it/14.webp)


您可以收到


- 经由 LN-Address **a**
- 通过 LN，设置 Invoice **b**
- on chain（WoS 支持 Bitcoin 网络，但需付费进行海底交换） **c**
- 通过扫描 LNurl-p **二维码**


![image](assets/it/15.webp)


### 创建 Invoice


单击 _Receive_（接收），然后选择带有 Lightning Network 符号的命令。


![image](assets/it/16.webp)


Invoice 创建菜单出现，我们点击 _Add Amount_（添加金额），写入准确金额并添加说明，在本例中为 "我的第一个 Invoice"。


![image](assets/it/17.webp)


通过键盘，我们可以设置金额。


![image](assets/it/18.webp)


然后获得 Invoice 的付款。收到的付款是这样的


![image](assets/it/19.webp)


### 从 POS 收款


Satoshi 的 Wallet 有一个默认功能，特别适合商家使用：POS。让我们看看如何激活它。


从主屏幕选择右上角的菜单。


![image](assets/it/20.webp)


然后选择_销售点_。


![image](assets/it/21.webp)


在最新版本的 WoS 中，请务必选择_Keypad_。


![image](assets/it/22.webp)

然后在键盘上键入金额，在下面的示例中等于 10 美分/118 Sats。为收款添加说明，本例中为 "我第二次使用 POS 机"。一个大的 Green 按钮亮起，点击它

![image](assets/it/23.webp)


例如，可以将 generate 和 Invoice 展示给客户。


![image](assets/it/24.webp)


这笔款项也是收取的！


![image](assets/it/25.webp)


### 发送付款


简单是 WoS 主屏幕的优势。要支付 Invoice，请单击_发送_。


![image](assets/it/26.webp)


首次使用时，WoS 会请求允许访问摄像机


![image](assets/it/27.webp)


从这一刻起，摄像机启动


![image](assets/it/28.webp)


通过框选 Invoice，我们可以看到已申请支付 210 Sats。如果申请者设置了说明，也会读取说明。该界面是摘要，也是确认请求：WoS "请求授权 "发送付款，点击 Green _Send_ 按钮即可获得授权。


![image](assets/it/29.webp)


付款到达目的地后，WoS 会通过以下屏幕发出通知


![image](assets/it/30.webp)


在主屏幕上点击_历史记录_（就在余额下方），交易列表就会出现


![image](assets/it/31.webp)


#### 恢复 WoS 账户


现在，我们来看看如何在新设备上安装 WoS；这在手机被盗、丢失或无法操作之前安装 Wallet 的手机时也很有用。重新安装后，您必须重新执行刚才介绍的账户注册程序，但有一个不同之处：在要求使用之前设置的电子邮件登录时，WoS 会显示如下内容：


![image](assets/it/33.webp)


有一条信息警告我们已发送一封电子邮件，内含重新激活账户的程序。您必须打开收件箱。


**重要**：从电脑上打开邮件，或者在任何情况下，从不同于要恢复 WoS 账户的设备上打开邮件。在收件箱中，我们会发现一封邮件，邮件中显示了一个二维码，我们可以通过该二维码框选


![image](assets/it/34.webp)


输入二维码后，在 WoS 的主页上就会显示恢复的账户以及余额和历史记录。