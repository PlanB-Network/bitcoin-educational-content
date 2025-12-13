---
name: Pop!_OS
description: Linux 发行版 Pop!_OS 安装指南
---

![cover](assets/cover.webp)



## 导言



Pop！OS 是一个基于 Linux 的操作系统，由 **System76**开发，该公司是一家专门为开发人员、设计师和高级用户提供机器的美国制造商。



Pop！OS旨在提供一个现代、稳定、高性能的环境，其特色在于简单的体验、强大的工具和对生产力的高度关注。



### 谁是 System76？



System76 是一家成立于 2005 年的美国公司，总部设在丹佛，专门生产专为 Linux 设计的笔记本电脑、台式机和服务器。



与传统制造商不同，System76 开发的机器具有开放性、可维修性和软件自由性。



System76 不仅仅制造电脑。



该公司还开发了.NET技术：




- Pop!OS**，它自己的基于 Linux 的操作系统；
- COSMIC**是Pop!OS .NET使用的现代高性能桌面环境；
- 开放固件**，这是一款基于 Coreboot .NET 的开源固件；
- 开发人员和设计人员的工具。



其目标是提供高质量的硬件和软件集成，可与苹果生态系统相媲美，但完全开放，并以 Linux 为中心。



## 一个现代化、稳定和可访问的系统



Pop!OS 建立在 Ubuntu 的基础上，具有出色的稳定性、广泛的硬件兼容性和庞大的软件生态系统。


它提供了一个优雅的界面，即 COSMIC 桌面，其设计流畅、直观、可定制，即使是新用户也可以使用。



## 开发人员、设计人员和高要求用户的理想选择



Pop!





- 开发人员（预装工具、高级平铺管理）、
- 使用 Nvidia 或 AMD 显卡的用户、
- 寻找可靠系统的学生和专业人员、
- 希望进行简单过渡的 windows 用户。



它包括自动平铺、清晰的软件中心和集成的生产力工具，使日常使用更加轻松。



## 流行操作系统》亮点





- 性能优化**得益于定期更新。
- 提供两个 ISO 版本**：标准版和 Nvidia 优化版。
- 增强安全性**（安装时提供 LUKS 加密功能）。
- Interface COSMIC**符合人体工程学，现代感十足。
- 与 Ubuntu 和 Flatpak 软件高度兼容**。



## 安全下载 POP!



### 1.先决条件



在下载和安装 POP!OS 之前，你需要做几件事来正确准备安装环境。



### 所需设备





- 兼容电脑**：英特尔或 AMD 处理器，英特尔/AMD/Nvidia GPU。
- 至少 4GB 内存**（建议使用 8GB 内存，以保证使用舒适）。
- 至少 20 GB 可用空间**（建议 40 GB 或以上）。
- 至少 4 GB 的 USB 密钥**，用于创建安装介质。



### 互联网连接



稳定的连接对于 ：





- 下载 ISO 映像、
- 安装后再安装更新。



Pop！OS 可以在没有网络连接的情况下运行，但在互联网上安装要顺利得多。



### 数据备份



如果 Pop!OS 要取代另一个系统（Windows、Ubuntu 等）或与之共存，建议在开始之前备份重要文件。



### 检查是否存在 Nvidia GPU（如适用）



对于配备 Nvidia 显卡的电脑，您需要下载包含 Nvidia 驱动程序的特殊 ISO 映像。


这项检查非常简单：





- 请参考个人电脑规格、
- 或在系统设置中查找显卡型号。



### 从官方网站下载



Pop！OS ISO 映像应直接从 System76 官方网页下载：[system76.com/pop](https://system76.com/pop/)。



本页面始终提供与您的硬件相匹配的最新版本。



![capture](assets/fr/03.webp)



### 选择版本：标准或 Nvidia，或 Raspberry Pi (ARM64)



Pop！OS 有三个版本：



### 标准版本



建议用于使用 .NET Framework 3.0 的计算机：





- intel 或 AMD 处理器
- 集成英特尔或 AMD GPU；
- AMD Radeon 显卡



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia 版本



建议配备 Nvidia 显卡的电脑使用。


该镜像已包含 Nvidia 驱动程序，使安装更轻松，并减少图形问题。



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi 版本（ARM64）



适用于 Raspberry Pi 4 和 400（ARM 处理器）。


它采用 ARM 架构，是这些微型计算机的专用版本。



![Utilisation de Balena Etcher](assets/fr/06.webp)



## 创建可启动 USB 密钥



您可以使用多种工具，如 Balena Etcher ：





- 下载并安装 [Balena Etcher](https://etcher.balena.io/)。



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- 打开 Balena Etcher，然后选择 Pop!OS ISO 映像。
- 选择 USB 密钥作为目标介质。
- 单击 Flash，等待进程结束。



![Utilisation de Balena Etcher](assets/fr/09.webp)



## 安装和保护 Pop!



### 从 USB 密钥启动





- 关闭电脑。
- 插入 USB 密钥（内含 Pop！OS）。
- 打开电脑。在最新的 PC 上，系统应能自动识别 USB 启动密钥。如果不是这种情况，请按住 BIOS/UEFI 访问键（通常是 F2、F12 或 Delete，视品牌而定）重新启动。
  - 在 BIOS/UEFI 菜单中选择 USB 密钥作为启动设备。
  - 保存并重新启动。



### 启动安装



选择可启动 USB 密钥作为启动设备后，电脑将启动进入 Pop!OS Live 环境。



选择语言。



![Capture](assets/fr/10.webp)



选择地点。



![Capture](assets/fr/11.webp)



选择键盘输入语言。



![Capture](assets/fr/12.webp)



选择键盘布局。



![Capture](assets/fr/13.webp)



选择 "清洁安装 "选项进行标准安装。这是Linux新用户的最佳选择，但要注意它会删除目标驱动器的所有内容。或者，你也可以选择 "Try Demo Mode"（尝试演示模式），继续在实时环境中测试Pop!OS。



![Capture](assets/fr/14.webp)



选择 "自定义（高级）"访问 GParted。通过该工具，您可以配置双启动、创建单独的"/home "分区或将"/tmp "分区放在不同的驱动器上等高级功能。



单击 "擦除并安装"，将 Pop!OS 安装到所选硬盘上。



![Capture](assets/fr/15.webp)



### 用户账户配置



安装程序的下一部分将指导你创建用户账户，以便登录新操作系统。



提供一个全名（可包括您选择的任何文字，大写或小写）以及一个用户名（必须小写）：



![Capture](assets/fr/16.webp)



创建账户后，系统会提示您设置新密码。



![Capture](assets/fr/17.webp)



### 全磁盘加密



系统磁盘加密不是必须的，但它能在有人未经授权对设备进行物理访问时保证用户数据的安全。



通过选中 "加密密码与用户账户密码相同"，可以使用登录密码对硬盘进行加密。您也可以取消选中该复选框，然后选择底部的 "设置密码"。选择 "不加密 "可忽略磁盘加密过程。



![Capture](assets/fr/18.webp)



如果您选择了 "设置密码 "按钮，您将看到一个额外的提示，要求您设置加密密码。



进入安装程序的下一步。现在，Pop!OS 将开始在磁盘上安装。



![Capture](assets/fr/19.webp)



安装完成后，重新启动计算机并登录以完成用户账户配置过程。



如果您已经更改了启动顺序，在启动时优先使用 Live USB 密钥，请完全关闭计算机并移除安装 USB 密钥。如果处于双启动模式，请按相应的键访问配置，并选择包含 Pop!OS 安装的驱动器。



![Capture](assets/fr/20.webp)



### 英伟达™（NVIDIA®）图形处理器



如果您是从英特尔/AMD ISO 安装的，而您的系统有独立的英伟达™（NVIDIA®）显卡，或者您后来添加了显卡，则需要为显卡手动安装驱动程序，以获得最佳性能。在命令终端运行以下命令安装驱动程序：



```bash
sudo apt install system76-driver-nvidia
```



您还可以从 Pop!_Shop 安装英伟达™（NVIDIA®）显卡驱动程序。



![Capture](assets/fr/20.webp)



## 安装必要工具



Pop！OS通过其Pop！Shop提供各种软件，但许多基本工具也可以通过终端安装`apt`或`flatpak`。下面介绍如何安装关键工具，以获得完整的工作环境。



### 终端安装



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### 通过 Pop！商店（图形界面）





- 从主菜单中打开 **Pop!
- 使用搜索栏查找所需的应用程序（例如，"Brave"）。
- 为每个应用程序点击 **安装**。
- Pop！_Shop 可自动管理依赖关系和更新。



## 系统更新



### 方案 1：通过图形用户界面（GUI）



Pop！OS拥有一个简单、直观的图形更新管理器。



1.点击**主菜单**（左下角图标）。


2.打开 **"Pop！_Shop "**。


3.在Pop！_Shop中，点击**"更新 "**选项卡。


4.系统将自动检查可用的更新。


5.点击 **"全部更新 "** 开始安装更新。


6.如果需要，请输入您的密码。


7.等待进程结束，必要时重新启动。



### 方案 2：通过终端



打开终端，输入 ：



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### 用户管理



我们建议使用具有 sudo 权限的标准用户账户进行日常操作。



创建新用户 ：



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



注销，然后用这个新用户重新登录。



### 图形驱动程序管理





- 对于 Nvidia 显卡，请检查是否安装了专有驱动程序：



```bash
sudo apt install system76-driver-nvidia
```





- 对于 AMD/Intel，默认情况下一般会包含驱动程序。



### 激活防火墙 (UFW)



Pop！OS默认不阻止网络流量。激活 UFW 以增强安全性：



```bash
sudo ufw enable && sudo ufw status verbose
```



### 配置自动更新



在无需人工干预的情况下及时更新系统：



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### 自定义外观和行为





- 打开**系统设置** → **外观**，选择浅色或深色主题。
- 通过 COSMIC 管理器配置活动边角、动画和扩展功能。
- 调整桌面布局，优化工作流程。



### 配置自动备份



Pop！OS集成了Deja Dup等备份工具：





- 从菜单中启动**备份**。
- 选择外部驱动器或网络位置。
- 安排定期备份。



### 安装有用的 GNOME/COSMIC 扩展程序



下面推荐几款可增强用户体验的扩展程序：





- Dash to Dock**：应用程序栏始终可见。
- GSConnect**：与安卓系统同步。
- 剪贴板指示器**：高级剪贴板管理。



通过 .NET Framework 安装



```bash
sudo apt install gnome-shell-extensions
```



然后在设置中激活它们。



### 优化内存和交换管理



检查您的交换状态：



```bash
swapon --show
```



如有必要，增加交换大小或配置交换文件 ：



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



将其添加到 `/etc/fstab` 文件，以便自动挂载。



## 软件包和存储库管理



### 了解软件包源



基于 Ubuntu 的 Pop!OS 主要使用 .NET Framework：





- Ubuntu** 官方软件库：用于大多数稳定软件。
- System76** 资源库：用于驱动程序、固件和特定工具。
- Flatpak**：访问各种沙盒应用程序。
- Snap**（可选）：另一种通用软件包格式。



---

### 添加和管理 PPA 资源库



要安装经常更新的软件，可以添加某些 PPA（个人软件包存档）：



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## 结论



Pop!OS 是一款现代、稳定的 Linux 发行版，适合初学者和高级用户使用。



凭借其直观的 COSMIC 界面和集成工具，无论是开发、创作还是日常使用，它都能提供流畅、高效的体验。



本教程涵盖关键阶段：准备、下载、安装、初始设置和基本工具。



欢迎进一步探索 Pop!OS 并自定义环境，使其发挥最大功效。