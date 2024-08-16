---
name: Tails

description: 在USB密钥上安装Tails
---

![image](assets/cover.webp)

一种便携式且具有遗忘性的操作系统，保护您免受监视和审查。

## 为什么要在USB密钥上安装Tails？

Tails (https://tails.boum.org/) 是随时拥有一台安全计算机的最简单方式，使用它不会在您使用的计算机上留下任何痕迹。

要使用Tails，关闭您可以访问的计算机（在您父母家、朋友家、网吧...）并用您的Tails USB密钥启动它，而不是Windows、macOS或Linux。

之后，您将拥有一个独立于常规操作系统的工作空间和通信环境，并且从不使用硬盘。

Tails从不写入硬盘，只使用计算机的RAM来运行。当Tails关闭时，这个内存会被完全擦除，从而移除所有可能的痕迹。

## 一些具体的使用案例

为了给您提供一直携带Tails USB密钥的好处的具体想法，这里是Agora256团队编制的一个小而非详尽的列表：

- 以未受审查和匿名的方式连接到互联网和Tor，浏览网站而不留下痕迹；
- 打开来自可疑网站的PDF；
- 使用Electrum钱包测试您的比特币私钥备份；
- 使用办公套件（LibreOffice）并在不属于您的计算机上工作；
- 在Linux环境中迈出您的第一步，学习如何离开微软和苹果的世界。

## 如何信任Tails？

使用软件总是涉及信任元素，但不必是盲目的。像Tails这样的工具必须努力为其用户提供值得信赖的手段。对于Tails，这意味着：

- 公开源代码：https://gitlab.tails.boum.org/；
- 基于声誉良好的项目：Tor和Debian；
- 可验证和可重现的下载；
- 不同个人和组织的推荐。

## 安装和使用指南

本安装指南的目的是引导您完成安装的每个步骤。我们不会描述比官方指南更多的操作步骤，但我们会在给您提示和技巧的同时指引您正确的方向。

出于实践经验的原因，这些提示将集中在macOS和Linux平台上。
🛠️
在开始此程序之前，请确保您有一个USB密钥，最小读取速度为150 MB/s，容量至少为8 GB，理想情况下为USB 3.0。

先决条件：

- 1个USB密钥，仅用于Tails，容量至少为8 GB
- 一台连接到互联网的计算机，配备Linux、macOS（或Windows）
- 根据您的互联网连接速度，大约需要一小时的空闲时间，包括½小时用于安装（需要下载1.3 GB的文件）

## 第1步：从您的计算机下载Tails

![image](assets/1.webp)

> 🔗 官方Tails部分：https://tails.boum.org/install/linux/index.fr.html#download

下载带有.img扩展名的安装文件可能需要一些时间，这取决于您的互联网下载速度，因此请提前计划。如果连接现代且高效，将不到5分钟。

将文件保存在已知文件夹中，例如Downloads，因为这将是下一步所必需的。

## 第2步：验证您的下载

![image](assets/2.webp)
🔗 官方 Tails 部分：https://tails.boum.org/install/linux/index.fr.html#verify
验证下载确保它是由 Tails 开发者发布的，并且在下载过程中没有被损坏或拦截。

使用 PGP 手动验证您刚下载的文件是否是预期的文件是可能的，但如果没有高级知识，这种验证提供的安全级别与下载页面上的 JavaScript 验证相同，而且更加复杂且容易出错。

要验证文件，请使用官方部分提供的“选择您的下载...”按钮！

## 第 3 步：在您的 USB 键上安装 Tails

![image](assets/3.webp)

> 🔗 官方 Tails 部分：
>
> - Linux: https://tails.boum.org/install/linux/index.fr.html#install
> - macOS: https://tails.boum.org/install/mac/index.fr.html#etcher 和 https://tails.boum.org/install/mac/index.fr.html#install

在整个指南中，将 Tails 安装到您的 USB 键上是最困难的步骤，尤其是如果您以前从未这样做过。最重要的一点是为您的操作系统选择官方部分中的正确程序：Linux 或 macOS。

一旦按照推荐安装并准备好工具，就可以将带有 .img 扩展名的文件复制到您的键上（擦除所有现有数据），使其独立地“可启动”。

祝您好运！我们在第 4 步见。

## 第 4 步：在您的 Tails USB 键上重新启动

![image](assets/4.webp)

> 🔗 官方 Tails 部分：https://tails.boum.org/install/linux/index.en.html#restart
> 现在是时候使用您的新 USB 闪存盘启动您的一台计算机了。将其插入其一个 USB 端口并重启！

> 💡 大多数计算机不会自动从 Tails USB 闪存盘启动，但您可以按下启动菜单键以显示可能从中启动的设备列表。

为了确定您应该按哪个键以确保您有允许您选择 USB 闪存盘而不是您通常的硬盘的启动菜单，这里是按制造商列出的非详尽列表：

| 制造商       | 键              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| 其他...      | F12, Esc         |

一旦选择了 USB 闪存盘，您应该会看到这个新的启动屏幕，这是一个非常好的迹象，所以让计算机继续启动...

![image](assets/5.webp)

## 第 5 步：欢迎来到 Tails！

![image](assets/6.webp)

> 🔗 官方 Tails 部分：https://tails.boum.org/install/linux/index.en.html#tails

在引导加载器和加载屏幕之后一两分钟，欢迎屏幕出现。

![image](assets/7.webp)

在欢迎屏幕中，在“语言和地区”部分选择您的语言和键盘布局。点击开始 Tails。

![image](assets/8.webp)
如果您的计算机没有通过线缆连接到您的网络，请参考官方Tails指南，以帮助您在没有Wi-Fi的情况下连接到您的网络（请参阅“测试您的Wi-Fi”部分）。
一旦连接到本地网络，Tor连接向导会出现，帮助您连接到Tor网络。

![image](assets/9.webp)

您可以开始匿名浏览，探索Tails中包含的选项和软件。尽情享受吧，您有足够的空间犯错误，因为USB闪存盘上的内容不会被修改……您的下一次重启将会忘记您所有的体验！

## 在未来的指南中...

一旦您对自己的Tails USB闪存盘有了更多的实验，我们将在另一篇文章中探讨其他更高级的主题，例如：

> 使用Tails的最新版本更新密钥；配置和使用持久存储；安装额外的软件。
> 届时，一如既往，如果您有任何问题，随时与Agora256社区分享。我们一起学习，为的是明天比今天更出色！