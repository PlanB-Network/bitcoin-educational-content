---
name: Elementary OS
description: Windows 和 MacOS 的理想替代品
---

![cover](assets/cover.webp)



Elementary OS 是一个基于 Ubuntu 的操作系统，设计简单、快速、稳定，适合日常使用。它是 MacOS 和 Windows 的 Linux 平衡替代品。其流畅、直观、简洁的图形化 Interface 使其易于学习，即使是初学者也能轻松上手。它还注重人体工程学、安全性和性能。



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## 为什么选择初级操作系统





- **简单易用**：Elementary OS 的图形 Interface 介于 MacOs 和 Windows 之间。这种熟悉感使其易于使用，即使是没有经验的用户也能轻松上手。





- **安全性**：与大多数 Linux 发行版一样，Elementary OS 也具有很高的安全性。定期更新、权限管理和不存在常见病毒使其成为一个可靠的系统。





- **速度**：Elementary OS 是一款轻量级发行版。它需要的资源很少，因此速度很快，适合配置不高的电脑使用。





- **免费**：该系统完全免费。不过，在下载时，您可以捐款支持开发人员。





- **活跃的社区**：围绕 Elementary OS 的社区种类繁多、反应迅速。如果您遇到困难，可以很容易地在论坛或社交网络上找到帮助。



## 安装和配置


### 硬件先决条件



在开始安装之前，请确保您拥有以下设备：





- 至少 12 GB 的**USB 密钥**
- **内存** 至少 4 GB
- 20 GB** 或更大的 **Hard 硬盘，使用更舒适



## 下载 ISO 映像



访问操作系统官方网站 [elementary](https://elementary.io/)，选择支持该项目的金额。此步骤为可选步骤。


如果您希望免费下载 ISO 映像，请在 **"其他 "** 字段中输入 0，然后开始下载系统 ISO 映像。



![0_01](assets/fr/01.webp)



## 创建可启动 USB 密钥



下载 ISO 映像后，您需要将其安装到 USB 密钥上，以便继续安装。



下载 [Balena Etcher](https://etcher.balena.io/) 等软件或类似工具，然后启动软件。


选择先前下载的 **Elementary OS** ISO 映像，并将 USB 密钥设置为目标。



点击 **flash** 按钮启动程序，等待程序完成后再取出 USB 密钥。



![0_02](assets/fr/02.webp)



## 按键启动和 BIOS 访问



关闭要安装 Elementary OS 的计算机，然后插入 USB 密钥。


电脑启动后，进入 BIOS（"ESC"、"F9 "或 "F11"，视品牌而定），选择 USB 密钥作为启动设备，然后按 "Enter "键启动程序。



## 安装初级操作系统



如果 USB 密钥配置正确，安装将自动启动。



### 语言选择



选择要安装系统的语言。您还可以选择地区版本。



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### 键盘布局



选择与您的键盘相对应的布局。系统提供了一个字段来检查按键是否能产生正确的字符。



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### 测试模式



初级操作系统可让你在安装前测试系统。该模式可让您探索 Interface，而无需修改 Hard 磁盘上的任何内容。



### 启动安装





- 点击 **"擦除磁盘并安装 "**，直接在整个磁盘上安装。
- 如果希望手动管理分区，请单击**"自定义安装 "**。



![0_07](assets/fr/07.webp)



### 光盘选择



选择要安装 Elementary OS 的磁盘，然后单击 "继续 "按钮。



![0_08](assets/fr/08.webp)



### 磁盘加密



有一个选项允许您对磁盘进行加密，以**保护**您的数据安全。你需要设置一个强大的密码来激活这种保护。不过，这是可选项。



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### 启动安装



在启动安装之前，您可以根据机器的兼容性授权自动安装其他硬件驱动程序。





- 点击 "擦除并安装 "开始安装。
- 等待该过程完成。



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### 重新启动



完成后，点击**enter**按钮重新启动，然后在适当的时候移除 USB 密钥，以避免重新启动安装。



![0_13](assets/fr/13.webp)



## 安装后的配置



重新启动后，还需要几个步骤。



![0_14](assets/fr/14.webp)



### 语言选择



登录时确认或更改系统语言。



![0_15](assets/fr/15.webp)



### 键盘布局



确保键盘布局是您想要的布局。



![0_16](assets/fr/05.webp)



### 创建用户账户



通过定义用户名将用户账户与操作系统关联起来，然后使用至少包含 20 个字符和符号的字母数字密码确保数据访问安全。



![0_17](assets/fr/17.webp)



### 第一次连接



首次登录时，Elementary OS 会通过一些基本设置来个性化你的环境。



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## 系统更新



在长期使用之前，必须用最新补丁更新系统。


### 方案 1：通过 Interface 图形更新



进入**应用中心**，点击右上角的更新图标。等待更新列出，然后点击**"全部更新 "**开始安装。



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### 选项 2：通过终端更新



您也可以通过终端在命令行中执行更新：这是一个值得推荐的选项，因为它非常准确。



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



首次更新时，操作系统需要用户密码和确认才能更新软件包，甚至是 Elementary 内核中的软件包。



## 工作环境配置



初级操作系统只包含基本工具。为了使您的环境适应您的需要，尤其是如果您是开发人员，我们建议您安装其他工具。





- 您可以使用以下命令添加有用的依赖项（可根据需要调整）：



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



此命令将安装 **Git**、**Python 3**、**pip**、**编译器工具**、**wget**、**curl**、**zsh**、**make**、**snapd** 和 **vscode**，以准备一个基本的开发环境。



Elementary OS 已经在你的电脑上运行了。其简洁、轻巧和优雅的理念使其成为个人和专业使用的绝佳选择。你将获得一个稳定、流畅、简洁的系统，并可根据自己的喜好进行定制。无论是开发、办公还是日常浏览，它都能为你打造一个高效、直观、愉悦的工作环境。还可以查看我们关于 Fedora 的教程，这是一款同样简单、强大和模块化的 Linux 发行版。



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0