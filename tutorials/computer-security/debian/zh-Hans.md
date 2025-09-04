---
name: Debian
description: 以其稳定性、健壮性和兼容性而闻名的 Linux 发行版。
---

![cover](assets/cover.webp)



Debian 是一款自由的 GNU/Linux 发行版，以其强大和可靠而著称。它的 Linux 内核和所有软件包都经过严格测试，以确保坚如磐石的稳定性和高度的安全性。Debian 既适用于服务器，也适用于工作站，它提供了易于使用的体验和丰富的软件目录。无论您是在为日常使用还是生产环境寻找一个安全的系统，Debian 都是您的正确选择。



## 为什么选择 Debian？





- 自由开放**：Debian 完全开放源代码，保证透明度，不收取许可证费用。
- 稳定性和安全性**：每个版本都经过全面的测试，这使得 Debian 成为市场上最可靠、最安全的发行版之一。
- 活跃的社区**：庞大的社区和丰富的文档可随时为您提供支持。
- 轻量级和可扩展**：您可以在资源有限的机器上安装 Debian，同时保持良好的性能。
- 广泛的软件目录**：可通过软件库获取 50,000 多个官方软件包。



## 选择 Interface 图形



Debian 提供多种桌面环境以满足您的需求：





- GNOME**：现代、直观的 Interface，是初学者的理想选择。它提供了一个流畅、易用的图形菜单来访问应用程序。
- XFCE**：轻便快速，非常适合性能较弱的机器。
- KDE Plasma**：高度可定制，外观类似 Windows。
- Cinnamon**：简洁、优雅的 Interface，灵感来自 Windows。
- LXDE / LXQt**：超轻量级，适用于旧电脑。
- MATE**：简洁、经典，接近旧版 GNOME。



💡 为了获得舒适、易于握持的体验，强烈推荐**GNOME**。



## 安装和配置 Debian


### 硬件要求



在开始安装之前，请确保您拥有以下设备：





- USB 密钥**：至少 8 GB，用于保存可启动 ISO 映像。
- 随机存取内存（RAM）**：4 GB，确保顺利安装和运行。
- 磁盘空间**：至少 15 GB 的可用空间，用于系统和更新。



### 下载



Debian 映像的选择取决于您的处理器架构：





- AMD64**：从[下载]列表中下载 "实时混合 "版 (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/)。
- ARM64**：从 [Debian] 官方网站 (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/) 获取 DVD 映像。
- 其他架构**：在 [此处](https://debian.obspm.fr/debian-cd/12.11.0/) 查找与您的架构相对应的 ISO。



![download](assets/fr/01.webp)



### 创建可启动 USB 密钥



下载相应的 ISO 映像后，继续创建安装介质：




- 从[官方网站](https://etcher.balena.io/) 下载 Balena Etcher**，然后获取适合自己系统的二进制文件并安装。



![etcher](assets/fr/02.webp)





- 启动 Etcher**：打开软件并选择之前下载的 Debian ISO 映像。
- 选择 USB 密钥**：指定您的密钥（8 GB 以上）为目标。
- 启动闪存**：点击**闪存！**，等待过程完成。



![flash](assets/fr/03.webp)



您的 USB 密钥现在可以开始安装 Debian 了。



## 在系统中安装 Debian



### 从 USB 密钥启动



要从 USB 密钥启动安装程序 ：




- 完全关闭**计算机。
- 重新启动**，然后立即按`ESC`、`F2`、`F11`（或专用键，视品牌而定）访问 BIOS/UEFI。
- 在启动菜单中，**选择 USB 密钥**作为启动设备。
- 按 Enter 键确认**，启动 Debian 映像：这将带您进入安装程序的欢迎界面。



### 启动安装



启动屏幕 ：



![starting](assets/fr/04.webp)



从 U 盘启动时，Debian 欢迎屏幕会提供几个选项：




- 实时系统**：无需安装即可启动 Debian，是测试环境的理想选择。
- 启动安装程序**：直接在 Hard 磁盘上启动安装。
- 高级安装选项**：允许您访问自定义安装模式。



要探索实时模式下的 Debian，请选择**实时系统**，并用**回车**确认。然后，您可以在实时环境中点击**安装 Debian**，启动安装。



![system](assets/fr/05.webp)





- 语言选择**（可选）



从列表中选择 Debian 系统的主要语言，然后点击确定。



![language](assets/fr/06.webp)





- 时区**（格林尼治标准时间）



选择您所在的地理区域，自动设置日期和时间。



![timezone](assets/fr/07.webp)





- 键盘布局



选择键盘语言和布局。使用内置测试栏检查每个键是否能产生预期的字符。



![keyboard](assets/fr/08.webp)



### 磁盘分区





- 擦除磁盘**：如果有专用分区，该选项将删除其所有内容。
- 手动分区**：选择该选项可根据需要创建、调整大小或删除分区。



![disk](assets/fr/09.webp)





- 创建用户账户



输入您的全名、账户名和强大的密码，以确保您的会话安全。



![user](assets/fr/10.webp)





- 参数摘要**



将显示您的选择摘要：检查每个项目，必要时返回修改。



![settings](assets/fr/11.webp)





- 启动安装



点击 "**安装**"开始复制文件和配置系统，然后等待该过程完成。



![install](assets/fr/12.webp)





- 重新启动**



安装完成后，重新启动计算机，应用所有配置并访问新的 Debian 系统。



![restart](assets/fr/13.webp)



启动时，输入用户名和密码以访问系统。



![login](assets/fr/14.webp)



## 系统更新



在开始使用系统之前，更新系统至关重要。这样您就能从最新的软件补丁、最新的软件源中获益，有时还能从操作系统本身的安全补丁中获益。



### 方案 1：通过图形化 Interface (GNOME) 更新



如果您在 GNOME 桌面环境下安装了 Debian，您可以通过图形方式执行更新。为此，请打开**软件**应用程序，然后转到**更新**选项卡。然后点击**重启和更新**开始更新过程。



### 方案 2：通过终端更新（推荐）



这种方法提供了更全面的控制。它允许你更新软件源、软件包，并在必要时更新内核。




- 使用快捷键 "Ctrl + Alt + T "打开终端。
- 使用以下命令更新可用软件包列表：



```shell
sudo apt update
```



根据提示输入密码（注意，输入时不会显示任何字符，这是正常现象）。





- 安装可用的更新 ：



```shell
sudo apt full-upgrade
```



## 了解基本任务



### 浏览互联网



Debian 的默认浏览器是**火狐**。如果您喜欢其他浏览器，只要 Debian 软件仓库中有（如 Chromium、Brave......），您可以安装其他浏览器。



### 文字处理



Debian 默认安装了**LibreOffice**套件。





- 要编写文档，请使用**LibreOffice Writer**，它相当于 Microsoft Word。
- 在电子表格方面，**LibreOffice Calc** 可替代 Excel。
- 最后，**LibreOffice Impress** 可以让你像制作 PowerPoint 一样制作演示文稿。



## 安装应用程序



在 Debian 上安装应用程序有两种方法：



### 图解法 ：



您可以使用**软件管理器**（可通过图形化 Interface）轻松搜索和安装应用程序。



### 命令行方法 ：



如果您要查找的应用程序没有出现在图形 Interface 中，或者您更喜欢使用终端，请使用以下命令：



```shell
sudo apt install <name>
```



将 `<name>` 替换为软件包名称。例如，要安装 `curl` ：



```shell
sudo apt install curl
```



### 安装手动下载的软件包 ：



如果下载的是 `.deb`文件（Debian 软件包），可以使用以下命令进行安装：



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

现在，您的 Debian 系统已经安装完毕，可以随时执行日常任务。


得益于**GNOME**桌面环境，你可以通过用户友好的图形 Interface 访问各种应用程序，无论是初学者还是高级用户都非常适合。



您也可以更改桌面环境（如 XFCE、KDE 等），而无需重新安装 Debian。要做到这一点，只需使用终端并安装您所选择的新环境即可。



要了解有关 Debian 的更多信息，以及更广泛的有关 GNU/Linux 发行版的信息，我建议您参考本课程：



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1