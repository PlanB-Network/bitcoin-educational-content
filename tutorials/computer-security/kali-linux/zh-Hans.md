---
name: Kali
description: 逐步在 VirtualBox 上安装 Kali Linux、将其作为可启动 U 盘或双启动。
---

![cover-kali](assets/cover.webp)



## 导言



### 为什么选择 Kali Linux？



**Kali Linux** 是一个专门用于 IT 安全的 Linux 发行版。


这就是我们使用 Kali Linux 的原因：





- 它预先配置了多种五项测试工具（系统和网络安全测试）。
- 它是**开源和免费的**，因此您可以自由使用和修改。
- 它**可靠、**安全，是学习网络安全知识的理想选择。
- 它让你学会如何在可测试的环境中使用 Linux。
- 它可以通过不同方式安装： ***VirtualBox**、**可启动 USB 密钥**或**双启动**。



## 安装和配置



### 1.先决条件



**所需设备：**





- 64 位处理器**（英特尔或 AMD）。
- 最低 8 GB 内存**（对于轻型安装或虚拟机，4 GB 内存可能足够）。
- 50 GB 可用磁盘空间** 用于安装 Kali Linux。
- 互联网连接**，以下载 ISO 映像和更新。
- 至少 8 GB 的 USB 密钥**，用于创建可启动媒体（如果要在 PC 上安装 Kali 或在 Live USB 上测试）。



在现有 PC 上安装之前，备份数据非常重要。



### 2.下载





- 访问 [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- 为您的应用程序选择 ISO 映像：
  - 安装映像**：用于 PC 安装。
  - 虚拟映像**：在 VirtualBox 或 VMware 上安装 Kali。
- 下载 ISO 映像。



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3.创建可启动 USB 密钥



您可以使用多种工具，如 Balena Etcher ：





- 下载并安装 [Balena Etcher](https://etcher.balena.io/)。



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- 打开 Balena Etcher，然后选择 Kali ISO 映像。
- 选择 USB 密钥作为目标介质。
- 点击 "Flash"，等待程序完成。



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4.安装和保护 Kali Linux



#### 4.1 通过 USB 密钥启动





- 关闭电脑。
- 插入 USB 密钥（内含 Kali Linux）。
- 打开电脑。在最新的 PC 上，系统应能自动识别 USB 启动密钥。如果不是这种情况，请按住 BIOS/UEFI 访问键（通常为 F2、F12 或 Delete，视品牌而定）重新启动。
  - 在 BIOS/UEFI 菜单中选择 USB 密钥作为启动设备。
  - 保存并重新启动。



#### 4.2 启动安装



##### 启动屏幕



从 U 盘启动时，应出现 Kali Linux 启动屏幕。在**图形安装**和**文本安装**之间进行选择。在本例中，我们选择了图形安装。



![capture](assets/fr/06.webp)



如果使用**Live**镜像，你会看到另一种模式，即**Live**，这也是默认启动选项。



![Mode Live](assets/fr/07.webp)



##### 语言选择



选择您喜欢的安装和系统语言。



![Sélection de la langue](assets/fr/08.webp)



请注明您的地理位置。



![Options d'accessibilité](assets/fr/09.webp)



##### 键盘配置



选择键盘布局。可使用测试栏检查按键是否与您的配置相符。



![Configuration du clavier](assets/fr/10.webp)



##### 网络连接



现在，安装程序会扫描你的网络接口，搜索 DHCP 服务，然后提示你输入系统的主机名。在下面的示例中，我们输入了 **"kali "** 作为主机名。



![Configuration réseau](assets/fr/11.webp)



您可以选择提供本系统将使用的默认域名（可从 DHCP 或现有操作系统中获取值）。



![Choix du type d'installation](assets/fr/12.webp)



##### 用户账户



然后，创建系统的用户账户（全名、用户名和强密码）。



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### 时区



选择您所在的地理区域以设置系统时间。



![Sélection du fuseau horaire](assets/fr/16.webp)



##### 分区类型



然后，安装程序会扫描磁盘，并根据配置显示多个选项。



在本指南中，我们从**空白磁盘**开始，这样就有**四种可能的选择**。


我们将选择 "**指导--使用整个磁盘**"，因为在这里我们要一次性安装 Kali Linux（单次启动）。这意味着不会保留其他操作系统，而且可以擦除整个磁盘。



如果磁盘已包含数据，可能会显示附加选项 **指导--使用最大的连续可用空间**。



这个替代方案允许你在不删除现有数据的情况下安装 Kali Linux，因此非常适合与其他系统双启动。



在我们的案例中，磁盘是空的，所以没有出现该选项。



![Choix du partitionnement](assets/fr/17.webp)



选择要分区的磁盘。



![capture](assets/fr/18.webp)



根据需要，你可以选择将所有文件保存在一个分区中（默认行为），或者为一个或多个顶级目录设置单独的分区。



如果不确定自己想要什么，请选择**单一分区中的所有文件**选项。



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



在安装程序进行任何不可逆转的更改之前，您还有最后一次机会检查磁盘配置。点击_Continue（继续）后，安装程序将启动，安装工作基本完成。



![capture](assets/fr/21.webp)



##### 加密 LVM



如果在上一步中启用了该选项，Kali Linux 现在会在询问您 LVM 密码之前执行安全硬盘擦除。



请使用强密码，否则将显示弱 passphrase 警告。



##### 代理信息



Kali Linux 使用软件源分发应用程序。如果您的环境使用代理，则需要输入必要的代理信息。



如果您**不确定**是否使用代理，请**留空**。输入虚假信息将阻止与版本库的连接。



![capture](assets/fr/22.webp)



##### Metapets



如果尚未配置网络访问，则需要在出现提示时**进一步配置**。



如果使用的是**实时**图像，则不会显示下一步。



然后，你可以选择要安装的 [元软件包](https://www.kali.org/docs/general-use/metapackages/)。默认选项将安装一个标准的 Kali Linux 系统，所以你不需要修改任何东西。



![capture](assets/fr/23.webp)



#### 启动信息



然后确认安装 GRUB 引导加载器。



![capture](assets/fr/24.webp)



##### 重新启动



最后，单击 "继续 "重新启动新的 Kali Linux 安装。



![capture](assets/fr/25.webp)



#### 4.3 安装后更新和配置 Kali Linux



更新系统是新安装后的重要步骤。您有两种选择：



##### 方案 1：通过图形用户界面（GUI）



Kali 和 Debian/Ubuntu 一样，提供集成的图形更新管理器。



1.点击**主菜单**（左上角或底部，具体取决于您的桌面）。


2.打开 **"软件更新程序 "**。


3.该工具将 ：




    - 检查要更新的软件包。
    - 您将看到一个列表（包含尺寸和版本）。
    - 只需单击一下，即可启动更新。


4.根据提示输入管理员密码 (`sudo`)。


5.让它安装，必要时重新启动。



##### 方案 2：通过终端



打开终端，运行 ：



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



建议不要使用**root**账户进行日常工作，而应创建一个非root用户。



在终端中键入这些命令：



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



注销并用新用户重新登录。



让我们用表格来总结一下 Kali Linux 的一些基本任务。



### Kali Linux 下的基本任务




| **类别** | **基础任务** | **描述 / 目标** | **主要方法** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **系统导航** | 打开终端 | 访问 Kali 的主命令行 | 点击终端图标或使用 `Ctrl + Alt + T` |
| | 浏览文件夹 | 在系统目录树中移动 | `cd /路径/到/文件夹`，使用 `ls` 列出文件 |
| | 创建 / 删除文件夹 | 组织文件 | `mkdir 文件夹名`，`rm -r 文件夹名` |
| **文件管理** | 复制 / 移动文件 | 在终端中操作文件 | `cp 文件 目的地`，`mv 文件 目的地` |
| | 删除文件 | 释放磁盘空间 | `rm 文件名` |
| | 显示文本文件内容 | 快速读取文件 | `cat 文件.txt`，`less 文件.txt` |
| **系统管理** | 更新 Kali Linux | 安装最新版本和安全补丁 | `sudo apt update && sudo apt full-upgrade -y` |
| | 安装软件 | 添加新工具或实用程序 | `sudo apt install 软件包名` |
| | 删除软件 | 清理系统 | `sudo apt remove 软件包名` |
| | 清理不需要的依赖 | 节省磁盘空间 | `sudo apt autoremove` |
| **网络和互联网** | 检查网络连接 | 测试互联网访问 | `ping google.com` |
| | 识别 IP 地址 | 了解您的网络配置 | `ip a` 或 `ifconfig` |
| | 更改 Wi-Fi 网络 | 连接到另一个接入点 | 网络图标 → 选择所需的 Wi-Fi |
| **账户和权限** | 执行管理员命令 | 临时获取 root 权限 | `sudo 命令` |
| | 创建新用户 | 添加本地账户 | `sudo adduser 用户名` |
| | 修改密码 | 保护账户安全 | `passwd` |
| **外观和舒适度** | 更改壁纸 | 个性化桌面 | 右键点击桌面 → **桌面设置** |
| | 修改主题 / 图标 | 提高可读性和美观性 | 设置 → 外观 / 主题 |
| **Kali 工具** | 打开工具菜单 | 探索测试和安全工具 | **应用程序 → Kali Linux** 菜单 |
| | 启动工具（如：nmap, wireshark） | 实际探索安全实用程序 | `sudo nmap`、`wireshark` 等 |
| **帮助和文档** | 获取命令帮助 | 在使用前了解命令 | `man 命令` 或 `命令 --help` |

## 结论



安装 Kali Linux 只是探索这个专用于网络安全的强大环境的第一步。通过掌握基本任务和系统管理，每个人都可以开始探索内置工具并了解 Linux 系统的内部运作。Kali 提供了一个绝佳的学习平台，既能强化技术技能，又能培养真正的 IT 安全文化。
