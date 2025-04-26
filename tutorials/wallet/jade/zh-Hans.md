---
name: Jade

description: 如何设置您的JADE设备
---

![image](assets/cover.webp)

## 教学视频

![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - 移动比特币硬件钱包完整教程，由BTCsession提供

## 完整的写作指南

![image](assets/cover2.webp)

### 先决条件

1. 下载Blockstream Green的最新版本。

2. 安装此驱动程序，确保您的计算机能识别Jade。

### 桌面设置

![full guide](https://youtu.be/0fPVzsyL360)

打开Blockstream Green，然后点击设备下的Blockstream标志。

![image](assets/1.webp)

使用随附的USB线将Jade连接到您的桌面。

> 注意：如果您的计算机未能识别Jade，请确保下载本指南中提到的驱动程序。

一旦您的Jade在Green中显示，通过点击检查更新并选择最新的固件版本来更新Jade。使用Jade上的滚轮或切换按钮来确认并继续更新。确保您的Jade仍然显示“初始化”按钮，否则您将必须等到设置Jade之后再升级它。如有必要，使用返回按钮回到此屏幕。

![image](assets/2.webp)

更新Jade的固件后，选择在您想要使用的网络和安全策略上设置Jade。

> 提示：登录屏幕下方显示的安全策略列在类型下。如果您不确定是选择单签名还是多签名盾，请查看我们的指南。(https://help.blockstream.com/hc/en-us/articles/4403642609433)

![image](assets/3.webp)

接下来，选择创建一个新钱包并选择12个单词来生成您的恢复短语。点击高级将提供给您12个和24个单词恢复短语的选项。

![image](assets/4.webp)

在纸上（或使用专用的恢复短语备份设备以增加安全性）离线记录恢复短语。然后，使用Jade顶部的滚轮或切换按钮来验证您的恢复短语。此步骤确保您已正确记录下来。

![image](assets/5.webp)

设置并确认您的六位数PIN码。这用于每次您登录钱包时解锁Blockstream Jade。

![image](assets/6.webp)

现在，只需在Green桌面应用上选择前往钱包，您将看到您的钱包在Blockstream Green上打开。Blockstream Jade也会显示它已准备就绪！您现在可以使用Jade发送和接收比特币交易了。

![image](assets/7.webp)

使用钱包后，断开您的Blockstream Jade与设备的连接。下次您想在Blockstream Jade上使用钱包时，只需重新连接您的设备并按照提示操作。

来源：https://help.blockstream.com/hc/en-us/articles/17478506300825

### 附录A - 验证Green钱包下载文件

验证下载意味着检查您下载的文件自开发者发布以来未被修改。

我们通过检查签名（由开发者的私钥产生）与下载的文件以及开发者的公钥一起，通过gpg –verify函数返回TRUE结果来完成这一操作。接下来我会向您展示如何做到这一点。如果您想了解这方面的背景知识，我有这个指南和那个指南。

首先，我们获取签名密钥：
对于Linux用户，打开终端，并运行以下命令（你应该直接复制并粘贴文本，并包括引号）：
```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

对于Mac用户，你需要做同样的事情，但首先你需要下载并安装GPG Suite。

对于Windows用户，你需要做同样的事情，但首先你需要下载并安装GPG4Win。

你将会收到一个输出，表示公钥已被导入。

![image](assets/9.webp)

此图片的alt属性为空；其文件名为image-3-1024x162.webp

接下来，我们需要获取包含软件哈希值的文件。它存储在Blockstream的GitHub页面上。首先访问他们的信息页面，然后点击“desktop”链接。它会将你带到GitHub上的最新发布页面，在那里你会看到一个指向SHA256SUMS.asc文件的链接，这是一个包含我们下载的程序的Blockstream发布的哈希值的文本文档。

![image](assets/10.webp)

GitHub:

![image](assets/11.webp)

虽然不是必须的，但在保存到磁盘后，我将“SHA256SUMS.asc”重命名为“SHA256.txt”，以便在Mac上使用文本编辑器更容易打开文件。这是文件的内容：

![image](assets/12.webp)

我们关注的文本位于顶部。根据我们下载的文件，有一个相应的哈希输出，我们稍后将进行比较。

文档的底部包含了对上述消息的签名——它是一个二合一的文件。

顺序并不重要，但在检查哈希之前，我们将验证哈希消息是真实的（即没有被篡改）。

打开终端。你需要处于SHA256SUMS.asc文件下载的正确目录。假设你将其下载到了“Downloads”目录，对于Linux和Mac，像这样更改目录（区分大小写）：

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

此图片的alt属性为空；其文件名为image-4-1024x165.webp

这个输出确认签名是好的，我们确信“info@greenaddress.it”的私钥签署了数据（哈希报告）。
现在我们应该对下载的zip文件进行哈希处理，并将输出结果与已发布的结果进行比较。请注意，在SHA256SUMS.asc文件中，有一段文字说“Hash: SHA512”，这让我感到困惑，因为文件明显包含了SHA256的输出，所以我打算忽略这一点。

对于Mac和Linux，打开终端，导航到zip文件下载的位置（可能你需要再次输入“cd Downloads”，除非你自那以后没有关闭终端）。顺便说一下，你可以通过输入PWD（“print working directory”），随时检查你所在的目录，如果这一切对你来说很陌生，观看一个快速的YouTube视频，搜索“如何导航Linux/Mac/Windows文件系统”会很有帮助。

要对文件进行哈希处理，请输入以下内容：

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

你应该检查你的文件确切叫什么，并在需要时修改上面蓝色的文本。

你会得到像这样的输出（如果文件与我的不同，你的输出也会不同）：

![image](assets/14.webp)

接下来，将哈希输出与SHA256SUMS.asc文件中的内容进行视觉比较。如果它们匹配，那么--> 成功！恭喜。

来源：https://armantheparman.com/jade/

### 在Sparrow上使用

如果你已经知道如何使用Sparrow，那么一如既往：

> 注意：这个过程与Specter一样

使用这里提供的链接下载Sparrow。

![image](assets/14.5.webp)

点击下一步，跟随设置向导了解不同的连接选项。

![image](assets/15.webp)

选择你想要的服务器，然后选择创建新钱包。

![image](assets/16.webp)

为你的钱包输入一个名称，然后点击创建钱包。

![image](assets/17.webp)

选择你想要的策略和脚本类型，然后选择连接的硬件钱包。

> 注意：如果你之前使用Blockstream Jade作为单签名钱包与Blockstream Green一起使用，并希望在Sparrow中查看你的交易，请确保脚本类型与Green中包含你资金的账户类型匹配。你还需要匹配派生路径。

![image](assets/18.webp)

插入你的Blockstream Jade并点击扫描。然后，系统会提示你在Jade上输入PIN码。

> 提示：在连接你的Jade之前，请确保Blockstream Green应用没有打开。如果Green打开了，这可能会导致你的Jade在Sparrow中无法被检测到。

![image](assets/19.webp)

选择导入密钥库以导入默认账户的公钥，或选择箭头手动选择你想要使用的派生路径。

![image](assets/20.webp)

在你想要的密钥被导入后，点击应用。

![image](assets/21.webp)

你现在已经成功设置了你的钱包，你可以开始使用Sparrow和Blockstream Jade接收、存储和花费你的比特币了。

> 注意：如果你之前使用Jade与Blockstream Green作为多签名盾牌钱包使用，你不应该期望你的新Sparrow钱包显示相同的余额 - 这些是不同的钱包。要再次访问你的多签名盾牌钱包，只需将你的Jade重新连接到Blockstream Green即可。

![image](assets/22.webp)

来源：https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-

### green app
如果您更倾向于使用移动设备，可以将其与Blockstream Green一起使用
- 如何将Blockstream Jade与Green一起设置 | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- 如何接收比特币到Jade钱包 | Blockstream Jade - https://youtu.be/CVtcDdiPqLA