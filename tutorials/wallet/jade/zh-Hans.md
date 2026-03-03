---
name: Jade
description: 如何设置您的 Jade 设备
---

![image](assets/cover.webp)

## 教学视频

![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - 移动比特币硬件钱包完整教程，由 BTCsession 创作

## 完整的写作指南

![image](assets/cover2.webp)

### 前提条件

1. 下载 Blockstream Green 的最新版本。

2. 安装此驱动程序，确保您的计算机能识别 Jade。

### 桌面设置

![full guide](https://youtu.be/0fPVzsyL360)

打开 Blockstream Green，然后点击 “Devices” 下的 Blockstream 图标。

![image](assets/1.webp)

使用随附的 USB 数据线将 Jade 连接到您的电脑。

> **注意：**如果您的电脑无法识别 Jade，请确保已安装必要的驱动程序，并检查是否是 USB 权限问题。

Jade 在 Green 界面上显示后，点击“检查更新”并选择最新固件版本进行更新。使用 Jade 上的滚轮或开关确认并继续更新。请确保 Jade 仍然显示 “Initialize” 按钮，否则您需要在设置 Jade 后才能进行升级。如有必要，请使用返回按钮返回此屏幕。

![image](assets/2.webp)

更新 Jade 固件后，请在您想要使用的网络和安全策略中选择 “Setup Jade”。

> **提示：**安全策略列在下方登录屏幕的 “Type” 下方。如果您不确定选择 “Singlesig” 还是 “Multisig”，请参阅我们的指南，点击[此处](https://help.blockstream.com/hc/en-us/articles/4403642609433)。

![image](assets/3.webp)

接下来，选择创建新钱包，并选择 12 个单词来生成您的助记词。点击 “Advanced” 按钮，您可以选择 12 个单词或 24 个单词的助记词。

![image](assets/4.webp)

将助记词离线记录在纸上（或使用专用助记词备份设备以确保安全）。然后，使用 Jade 顶部的旋钮或开关来验证您的助记词。此步骤可确保您已正确记录。

![image](assets/5.webp)

设置并确认您的六位数 PIN 码。这用于每次您登录钱包时解锁 Blockstream Jade。

![image](assets/6.webp)

现在，只需在Green桌面应用上选择前往钱包，您将看到您的钱包在Blockstream Green上打开。Blockstream Jade也会显示它已准备就绪！您现在可以使用Jade发送和接收比特币交易了。

![image](assets/7.webp)

使用完钱包后，请断开 Blockstream Jade 与设备的连接。下次想在 Blockstream Jade 上使用钱包时，只需重新连接设备并按照提示操作即可。

来源：https://help.blockstream.com/hc/en-us/articles/17478506300825

### 附录 A - 验证 Green Wallet 下载文件

验证下载文件是指检查您下载的文件自开发者发布以来是否已被修改。

我们通过检查签名（由开发者私钥生成）、下载的文件以及开发者的公钥，并使用 gpg --verify 函数进行验证，确保结果为 TRUE。接下来我将向您展示具体操作方法。

首先，我们需要获取签名密钥：

对于 Linux 系统，打开终端并运行以下命令（只需复制粘贴文本，并包含引号）：

```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

对于 Mac 系统，操作步骤相同，但需要先下载并安装 GPG Suite。

对于 Windows 系统，操作步骤相同，但需要先下载并安装 GPG4Win。

您将看到一条输出信息，提示公钥已导入。

![image](assets/9.webp)

这张图片的 alt 属性为空；它的文件名是 image-3-1024x162.webp

接下来，我们需要获取包含软件哈希值的文件。它存储在 Blockstream 的 GitHub 页面上。首先访问他们的信息页面（链接在此），然后点击 “desktop” 链接。这将带你到 GitHub 上的最新版本页面，在那里你会看到一个指向 SHA256SUMS.asc 文件的链接，这是一个文本文件，其中包含 Blockstream 发布的我们下载的程序的哈希值。

![image](assets/10.webp)

GitHub:

![image](assets/11.webp)

虽然不是必须的，但我在保存到磁盘后将 “SHA256SUMS.asc” 重命名为 “SHA256.txt”，以便在 Mac 上使用文本编辑器更轻松地打开该文件。文件内容如下：

![image](assets/12.webp)

我们关注的文本位于顶部。根据我们下载的文件，有一个相应的哈希输出，我们稍后将进行比较。

文档的底部包含了对上述消息的签名——它是一个二合一的文件。

顺序并不重要，但在检查哈希之前，我们将验证哈希消息是真实的（即没有被篡改）。

打开终端。你需要处于 SHA256SUMS.asc 文件下载的正确目录。假设你将其下载到了 “Downloads” 目录，对于 Linux 和 Mac，像这样更改目录（区分大小写）：

```bash
cd Downloads
```

当然，你必须在这些命令后按<enter>键。对于Windows，打开CMD（命令提示符），并输入同样的命令（尽管它不区分大小写）。

对于Windows和Mac，你需要已经按照前面的指示下载了GPG4Win和GPG Suite。对于Linux，gpg随操作系统提供。从终端（或Windows的CMD），输入此命令：

```bash
gpg --verify SHA256SUMS.asc
```

文件名的确切拼写（用红色标出）可能在你获取文件的当天有所不同，所以确保命令与下载的文件名匹配。你应该得到这个输出，并忽略有关受信任签名的警告——这只意味着你还没有手动告诉计算机你信任我们之前导入的公钥。

![image](assets/13.webp)

这张图片的 alt 属性为空；其文件名是 image-4-1024x165.webp。

此输出确认签名有效，我们确信“info@greenaddress.it”的私钥已对数据（哈希报告）进行了签名。

现在我们应该对下载的 zip 文件进行哈希运算，并将输出结果与已发布的版本进行比较。请注意，SHA256SUMS.asc 文件中有一段文字写着 “Hash: SHA512”，这让我感到困惑，因为该文件中明明包含 SHA256 的输出，所以我将忽略它。

对于 Mac 和 Linux 系统，请打开终端，前往到 zip 文件的下载位置（可能需要再次输入“cd Downloads”，除非您之后没有关闭终端）。顺便说一下，您可以随时通过输入 PWD（“打印当前工作目录”）来查看当前所在的目录。如果您对这些都不熟悉，可以搜索 “如何浏览 Linux/Mac/Windows 文件系统” 观看一个简短的 YouTube 视频。

为了获取该文件，请输入以下命令：

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

您应该检查一下您的文件确切名称，并根据需要修改上面蓝色字体部分的文本。

您将得到类似这样的输出（如果您的文件与我的不同，您的输出也会有所不同）：

![image](assets/14.webp)

接下来，将哈希输出与 SHA256SUMS.asc 文件中的内容进行比较。如果它们匹配，则表示成功！恭喜！

来源：https://armantheparman.com/jade/

### 在 Sparrow 上使用

如果您已经知道如何使用 Sparrow，那么操作与以往相同：

> 注意：例如，使用 Specter 的过程也相同

使用此处的链接下载 Sparrow。

![image](assets/14.5.webp)

点击 “Next” 按照设置指南了解不同的连接选项。

![image](assets/15.webp)

选择你想要的服务器，然后选择创建新钱包。

![image](assets/16.webp)

输入您的钱包名称，然后点击 “Create Wallet”。

![image](assets/17.webp)

选择您所需的策略和脚本类型，然后选择 “Connected Hardware Wallet”。

> 注意：如果您之前曾将 Blockstream Jade 作为 Blockstream Green 的单签名钱包使用，并且想要在 Sparrow 中查看您的交易记录，请确保脚本类型与您在 Blockstream Green 中包含资金的账户类型相匹配。您还需要确保派生路径也匹配。

![image](assets/18.webp)

插入您的 Blockstream Jade 并点击扫描。然后，系统会提示你在 Jade 上输入 PIN 码。

> 提示：在连接 Jade 之前，请确保 Blockstream Green 应用未打开。如果 Green 处于开启状态，可能会导致 Sparrow 无法识别您的 Jade 钱包。

![image](assets/19.webp)

选择 “Import Keystore” 导入默认账户的公钥，或点击箭头手动选择您想要使用的密钥派生路径。

![image](assets/20.webp)

导入所需的密钥后，点击 “Apply”。

![image](assets/21.webp)

您已成功设置钱包，现在可以开始使用 Sparrow 和 Blockstream Jade 接收、存储和使用您的比特币。

> 注意：如果您之前使用 Jade 搭配 Blockstream Green 作为多签名防护钱包，则不应期望新的 Sparrow Walelt 显示相同的余额——它们是不同的钱包。要再次访问您的多签名防护钱包，只需将您的 Jade 重新连接到 Blockstream Green 即可。

![image](assets/22.webp)

来源：https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-

### Blockstream Green 应用程序
如果您更倾向于使用移动设备，可以将其与 Blockstream Green 一起使用
- 如何将 Blockstream Jade 与 Green 一起设置 | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- 如何接收比特币到 Jade 钱包 | Blockstream Jade - https://youtu.be/CVtcDdiPqLA
