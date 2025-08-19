---
name: Fedora
description: 为你提供免费、完整和安全工作空间的 Linux 发行版。
---


![cover](assets/cover.webp)





Fedora 是 2003 年推出的基于 Linux 的免费开源操作系统，由**Fedora 项目**社区开发，并得到**Red Hat Linux** 的支持。该系统以其稳定性、良好的性能和易用性而闻名，是初学者和高级用户的绝佳选择。该系统可在大多数现代处理器架构上运行，因此几乎可以在任何计算机上安装。Fedora 还提供多个预配置版本，称为 "Fedora Spins "或 "Fedora Editions"，专为特定需求（视频游戏、天文学、开发......）而设计。



## Fedora Linux 架构



如前所述，Fedora 是基于 Linux 内核的免费操作系统。Linux 内核是操作系统中与计算机硬件通信并管理内存和处理能力等系统资源的部分。



Fedora Linux 包含在 Linux 内核上运行操作系统所需的各种软件工具和应用程序。Fedora 的模块化架构意味着它主要由一系列独立组件组成，这些组件可以根据需要轻松添加、移除或替换。这样，您就可以只使用所需的资源来构建操作系统。



Fedora 还包含一个桌面环境，即用户执行任务和访问应用程序的 Interface。Fedora 的默认桌面环境是 GNOME，这是一个用户友好、易于使用且高度可定制的桌面环境。



## 为什么选择 Fedora？



在众多的 Linux 发行版中，Fedora 因 .NET Framework 而脱颖而出：





- 模块化**：与不同的处理器架构兼容，Fedora 可以安装在大多数电脑上，甚至是低功耗电脑，完全满足您的需求。





- 简单直观的 Interface**：Fedora 将现代图形 Interface 与强大的命令行 Interface 相结合，使所有配置文件都能轻松使用。





- 内核稳定性**：Fedora 以 Red Hat 为基础，以其更新的可靠性而闻名，尤其是内核更新。





- 快速、简便的安装**：图像大小仅为 3 GB，即使在资源有限的机器上也能快速、简便地安装。



## Fedora 版本



根据您的配置文件和使用情况，Fedora 提供适合您需求的版本。您主要可以找到 .NET 和 .NET 版本：





- Fedora 工作站**：该版本是个人和/或专业电脑使用的理想选择，安装有通用实用程序，如浏览器、办公套件（文本编辑器）和媒体播放软件。





- Fedora 服务器**：该版本专门用于服务器管理。Fedora Server 包含多种工具，可帮助您根据自己的规模部署和管理服务器。





- Fedora CoreOS**：想要轻松运行和部署云应用程序？Fedora CoreOS 版为您提供了使用 Docker 和 Kubernets 等工具创建和管理镜像的工具。



在本教程中，我们将使用 Fedora 工作站版本。不过，下面详细介绍的过程与其他版本类似。



## 安装和配置 Fedora 工作站



安装 Fedora 工作站需要以下硬件配置：




- 至少 **8 GB** 的 USB 密钥，用于启动操作系统。
- 计算机 Hard 磁盘上至少有 **40 GB 可用空间**。
- 4GB 内存**，带来流畅体验。



### 下载 Fedora 工作站



您可以从 Fedora 项目官方网站下载 [Fedora Workstation] 版本 (https://fedoraproject.org/fr/workstation/download)。然后选择与您的处理器架构（32 位 - 64 位）相对应的版本，点击**下载**图标。



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### 创建可启动 USB 密钥



要安装 Fedora，您需要使用 [Balena Etcher](https://etcher.balena.io/) 等软件创建可启动 USB 密钥。



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



完成 Balena Etcher 安装后，打开应用程序并选择下载的 Fedora Workspace ISO 映像。选择 USB 密钥作为目标媒体，然后点击**Flash**按钮开始创建可启动密钥。



![boot](assets/fr/05.webp)


### 安装 Fedora



完成 USB 密钥启动后，关闭计算机。


打开计算机，然后在启动过程中按`F2`、`F12`或`ESC`键（视计算机而定）访问 BIOS。



在启动选项中，选择 USB 密钥作为主启动设备。确认此选择后，计算机将重新启动并自动启动 USB 密钥中的 Fedora 安装程序**。



计算机从 USB 盘启动后，会出现**GRUB 屏幕**。



在此阶段，您有以下选择：




- 测试介质**：此选项允许您检查 U 盘的完整性，并确保存在正确安装所需的所有依赖项。这是一个可选步骤，但如果对 U 盘有任何疑问，建议使用此步骤。



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- 启动 Fedora**：这将以 "实时 "模式启动 Fedora，无需安装。



在 Fedora 桌面（实时模式）上，点击 **安装 Fedora**（或安装在 Hard 磁盘上）开始安装过程。您可以选择稍后安装，无需安装即可测试 Fedora。



![install-live](assets/fr/08.webp)



第一步是选择 Fedora 的**安装语言**和**键盘布局**



![language](assets/fr/10.webp)





- 选择安装磁盘 ：



选择要安装 Fedora 的 Hard 磁盘。



如果磁盘是空的，Fedora 会自动使用所有可用空间。否则，您可以自定义分区（手动或自动）。



![disk](assets/fr/11.webp)





- 加密 ：



在此阶段，Fedora 建议加密您的磁盘，以增加额外的 Layer 安全性。这将确保只有您的 Fedora 系统才能读取数据。



![chiffrement](assets/fr/12.webp)



在启动安装之前，Fedora 会显示您的选择摘要。确认后点击安装按钮开始 Fedora 安装。



![resume](assets/fr/13.webp)



在安装过程中，Fedora 会复制文件并配置系统。完成后，计算机会自动重启。



![installation](assets/fr/14.webp)



### 基本配置


首次使用时，您需要确定一些设置：




- 必要时更改系统语言。



![language](assets/fr/15.webp)





- 选择适合您偏好的键盘布局。



![keyboard](assets/fr/16.webp)





- 在搜索栏中输入城市名称，选择您所在的时区，然后点击相应的建议。



![timezone](assets/fr/17.webp)





 - 为有需要的应用程序启用或禁用对位置的访问，以及自动发送错误报告。



![location](assets/fr/18.webp)





- 决定是否启用第三方软件库。



![logs](assets/fr/19.webp)





- 输入您的全名并为您的账户定义用户名。



![name](assets/fr/20.webp)





- 为您的会话创建一个安全密码：尽可能长（至少 20 个字符）、尽可能随机、包含多种字符（小写、大写、数字和符号）。记住保存密码。



![mdp](assets/fr/21.webp)



完成所有这些步骤后，启动 Fedora 并立即开始使用，无需重启。



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



安装完成后，您可以使用预装的一些实用程序咨询 Interface 主页。



![install-now](assets/fr/09.webp)



## 了解基本任务



### 浏览互联网


Fedora 的默认浏览器是**Firefox**。它易于使用，适合大多数需求。


如果您喜欢其他浏览器，可以从**软件管理器**或通过**终端**安装。


### 文字处理


Fedora 默认包含**LibreOffice**办公套件，该套件提供多种实用工具：




- Writer** 用于文字处理。
- Calc** 用于电子表格。
- Impress** 制作演示文稿。


## 安装应用程序


要安装新的应用程序，您可以使用 Fedora 的**软件管理器**（称为_Software_），它使安装变得简单而直观。  不过，使用**终端**通常更快、更准确。



在安装任何软件之前，请务必记住更新**存储库**，以确保您能访问可用的最新版本。



然后使用以下命令启动所需应用程序的安装：


sudo dnf install software_name`


## 更新操作系统


安装后，更新 Fedora 以利用最新的安全补丁和软件更新非常重要。


### 方案 1：通过 Interface 图形




- 打开 Fedora **设置**，然后转到**系统**部分。
- 点击 **软件更新**。
- 开始下载更新，等待更新完成。



安装更新后，可能需要重新启动**。


### 方案 2：通过终端




- 打开终端，首先更新**存储库**，确保有最新版本的 .NET Framework：



```shell
sudo dnf check-update
```





- 接下来，使用以下命令更新所有已安装的软件：



```shell
sudo dnf upgrade
```



现在，您的 Fedora 系统已是最新版本，可随时用于执行所有日常任务。了解我们关于另一个 Linux 发行版 Linux Mint 的教程，以及如何为你的 Bitcoin 交易建立一个健康安全的环境。



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5