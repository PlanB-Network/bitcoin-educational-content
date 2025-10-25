---
name: Manjaro
description: 让更多人了解 Arch Linux 的强大功能
---
![cover](assets/cover.webp)



Arch Linux 凭借其强大的功能和稳定性，在许多领域都很受欢迎。不过，对于新手用户来说，它可能很难上手。正是为了解决这个问题，**Manjaro**应运而生：基于直观、易学的Interface，提供Arch Linux的强大功能，但同时提供更简单、更易用的体验。



## 开始使用 Manjaro



Manjaro 最大的优势之一就是其**简单高效的更新系统**。无需手动管理：Manjaro会帮你搞定！当有更新可用时，通知区域的图标（位置因版本而异）会提醒你。你所要做的就是按照提示操作，整个过程快速而轻松。



Manjaro 还提供了**丰富的应用程序目录**。由于 Manjaro 基于 Arch Linux，因此可以直接访问其官方软件库，其中包含丰富的各种软件，包括专有应用程序。为了进行更多测试，Manjaro 会稍稍延迟一些 Arch Linux 更新；这样做的代价是稍稍延迟新版本的发布，以提高稳定性。如果你觉得这样的选择还不够，还可以访问**AUR（*Arch User Repository*）**，这是一个由社区管理的庞大库。如果一个程序不存在于官方软件库中，那么它很有可能就在 AUR 中。



与 Windows 或 macOS 等系统相比，Manjaro 的另一个优势是对资源的需求**低**。它对内存和计算能力的消耗更少，是老式电脑或性能较弱的电脑的理想选择：你的机器将变得更加流畅和快速，重新焕发第二春。



除此之外，Manjaro 是**完全免费的**。与 Windows 或 macOS 不同的是，你无需支付任何费用即可安装并充分发挥它的作用。最后，由于定期快速更新，Manjaro 提供了**增强的安全性，从而限制了漏洞的暴露**。其活跃的社区还能确保任何问题都能迅速得到纠正，并提出有效的解决方案。



## 探索 Manjaro OS



在开始安装 Manjaro 之前，必须了解该发行版有多个版本。每个版本都提供独特的桌面环境，对工作流程和系统资源消耗都有影响。Manjaro 有三个主要官方版本。



![0_01](assets/fr/01.webp)





- **KDE Plasma版**是可定制程度最高的版本。如果你正在寻找一个视觉效果优雅、性能卓越的系统，KDE Plasma 是一个绝佳的选择。这种稳定的桌面环境非常适合希望获得全面控制和定制体验的用户。





- 对于资源较为有限的计算机，**Xfce** 版是理想的解决方案。它的 Interface 既轻便又直观，即使在旧电脑上也能保证流畅运行。此外，它的布局让人联想到 Windows，让新用户更容易过渡到 Linux。





- 最后，**GNOME** 版提供了一种完全不同的方法。其精简的设计强调通过虚拟工作空间提高生产力和组织能力。这种以活动为中心的工作流程对已经熟悉 Linux 并正在寻找简约、高效环境的用户特别有吸引力。



### 其他 Manjaro 版本



![0_02](assets/fr/02.webp)



除了官方版本，Manjaro 社区还提供其他版本。这些替代版本旨在满足特定需求，并提供各种桌面环境。



如果你刚刚开始使用电脑，并且正在寻找一款熟悉的 Interface 系统，**肉桂**版将是你的最佳选择。它的设计易于使用，同时保留了传统办公环境的经典习惯。



对于更高级的用户，还有诸如**i3 窗口管理器**或**Sway**等版本。这些版本更轻、更快，但需要熟练掌握命令行才能进行全面配置和使用。这些环境非常适合那些希望完全控制自己的系统，并将效率放在首位的用户。



## 技术要求



为使 Manjaro 达到最佳运行状态，您的电脑必须满足一些最低要求。我们建议您至少安装 .NET Framework 3.0 或更高版本：





- **64 位 (x86_64)** 处理器
- 建议使用 4 GB 内存（最低 2 GB）**（见下文）**
- 30 GB 磁盘空间（如果创建专用的"/home"分区，空间会更大）



## 安装 Manjaro



要下载，请访问 [Manjaro 官方网站](https://manjaro.org/) 并选择最适合你的版本。下载文件后，你需要用 Manjaro ISO 映像创建一个可启动 USB 密钥。



然后访问 [Rufus] 软件网站 (https://rufus.ie/fr/) 并下载。运行程序，插入 USB 密钥，选择 Manjaro ISO 映像并开始闪存。等待过程结束后再拔出密钥。然后就可以重启电脑了。



![0_03](assets/fr/03.webp)



要在电脑上安装 Manjaro，首先要完全关闭电脑。然后插入 USB 密钥，重新开机，按**F2、F10、F12、Escape**或**Delete**（视制造商而定）进入启动菜单或 UEFI/BIOS 固件。



然后选择 USB 密钥作为启动设备，开始操作系统安装过程。



### 启动屏幕



首次从 USB 密钥启动 Manjaro 时，会直接进入安装菜单。在启动安装之前，你可以更改键盘布局或系统语言。



然后选择**使用开源驱动程序启动**选项，开始安装 Manjaro。这些开源驱动程序与大多数硬件兼容，在大多数情况下都能满足需求。如果你使用的是英伟达（NVIDIA）显卡，或者需要更高的图形处理性能，可以选择**使用专有驱动程序**，即使用专有驱动程序。



![0_04](assets/fr/04.webp)



系统将以**默认的实时模式**启动。这允许你在永久安装之前测试 Manjaro 的功能，看看它是否符合你的需求。准备就绪后，点击 ** 安装 Manjaro Linux** 选项。



选择所需的安装语言，然后点击 **下一步**。



![0_06](assets/fr/06.webp)



然后选择您所在的位置，设置正确的时区。在此阶段，您还可以更改语言和日期格式。



![0_07](assets/fr/07.webp)



选择键盘布局。可使用测试字段检查键入的字符是否符合预期。



![0_08](assets/fr/08.webp)



### 磁盘分区


您有两个磁盘分区选项。





- 第一种，也是最简单的一种方法，就是擦除整个磁盘，然后在上面安装 Manjaro。
- 第二种允许**手动分区**。



![0_09](assets/fr/09.webp)



为了安装干净，我们建议至少创建三个分区：





- 第一个分区为 516 MB**（主分区），用于启动**。
- 第二个**2 GB**（逻辑）分区用于**交换**。
- 第三个分区用于**个人数据**。



如果您希望同时安装其他系统，则需要分割最后一个分区，只分配一部分给 Manjaro（至少 **15 GB** 以保证系统正常运行）。


### 创建用户账户



填写所需信息，创建系统用户账户。最后，设置管理员密码（**根**）。该管理员是**超级用户**，拥有系统的全部权限和执行高级命令的能力。



![0_10](assets/fr/10.webp)



### 选择合适的办公套件



Manjaro 可让您在 **FreeOffice** 和 **LibreOffice** 之间进行选择。





- **LibreOffice** 的功能更全面，拥有更多软件和高级功能。
- 而 **FreeOffice** 则更轻便，只包含基本功能：**文本编辑器**、**计划编制器**和**演示文稿**。



![0_11](assets/fr/11.webp)



### 配置摘要



摘要屏幕会显示您设置的所有参数。如有必要，您可以返回进行更改，而不会影响您已经进行的其他设置。



然后点击 **安装**，确认后即可开始实际安装。



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



### 安装结束



过程结束后，选中**立即重启**框，然后点击**完成**。系统将重新启动，**Manjaro 即可使用**。



![0_13](assets/fr/14.webp)



## 使用 Manjaro 的第一步



安装 Manjaro 只是第一步。为了最大限度地利用系统，这里有一些有用的知识。



### 更新系统



Manjaro 大大简化了更新工作。更新软件包



```shell
sudo pacman -Syu
```



该命令下载并安装现有的最新版本。我们建议你定期运行它，以保持系统的**安全和稳定**。



### 配置开发环境



要在 Manjaro 上开发网络应用程序，只需通过一条命令即可安装基本工具：



```shell
sudo pacman -S nodejs npm git yarn
```



该命令安装 Node.js 和 npm 以运行和管理 JavaScript 和 TypeScript 项目，安装 Git 以进行版本管理，安装 Yarn 作为替代软件包管理器。



### 安装 Bitcoin Wallet



要在 Manjaro 上管理比特币，可以安装 **Electrum**，这是一款轻量级、安全的 Wallet .NET 应用程序：



```shell
sudo pacman -S electrum  # Install Electrum
```



Electrum让您**轻松地接收和发送比特币，同时提供多种Wallet管理和passphrase保护等高级功能**。如需完整的 Electrum 使用指南，请查看我们的专门教程，了解如何创建 Wallet、保护您的资金和进行交易。



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## 确保 Manjaro 系统安全



安全是任何 Linux 安装的一个重要方面。保护数据的机密性和完整性对你来说非常重要。



### 防火墙配置



Manjaro 包含 UFW（*Uncomplicated Firewall*），这是一个管理网络过滤防火墙的程序，但你必须手动激活它：



```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```



![verbose](assets/fr/15.webp)



### 管理用户权限



1. **创建一个非特权用户**



```shell
sudo useradd -m username
sudo passwd username
```



2. **Sudoers 文件配置**



```shell
sudo EDITOR=nano visudo
```



现在，你已经准备好在你的机器上使用 Manjaro Linux 了。得益于其**简单的安装**、**方便的更新**和**灵活性**，你将拥有一个功能强大、性能卓越的系统，适用于开发、日常使用以及使用 Electrum 等工具管理比特币。



Manjaro 集**稳定性、速度和安全性**于一身，同时保持**完全免费**，是初学者和高级用户的理想选择。花点时间探索它的各种功能，并根据自己的需求定制环境。如果你想了解更多专业知识并探索 Arch Linux 系统，我们强烈推荐你阅读我们的教程。



https://planb.network/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973