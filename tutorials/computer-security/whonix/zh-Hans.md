---
name: Whonix
description: 保护您的隐私和机密。
---

![cover](assets/cover.webp)



**Whonix**是一个基于**Debian**的Linux发行版，旨在提供一个集**安全**、**匿名**和**隐私**于一体的环境。它简单易学，兼容不同的界面（虚拟机、Qubes OS、实时模式），默认情况下包括通过**Tor**进行的网络流量路由、**双重防火墙**（网关和工作站各有一个防火墙）、**全面的 IP/DNS 防泄漏保护**，以及对网络观察者（包括互联网服务提供商）有效屏蔽你的活动的工具。Whonix 不仅仅是一个匿名系统，还是一个完整的安全开发环境。



## 为什么选择 Whonix？





- 免费**：与大多数 Linux 发行版一样，Whonix 是完全免费授权的开源系统。它采用开放源代码开发，拥有一个活跃而透明的社区。
- 隐私、安全和匿名** ：Whonix 的主要目标是提供一个超级安全的环境，通过 Tor 网络保护您的所有数据并加密您的通信。
- 易于使用**：Whonix 提供直观、预配置的图形化 Interface，甚至适合新手用户。无需成为专家即可享受高级保护。
- 理想的安全开发环境**：Whonix 可让您开发、测试、审核或运行程序，而不会泄露您的真实 IP Address，也不会暴露您的浏览或网络通信习惯。
- 一次性会话和实时模式**：Whonix 可在实时模式下启动，也可通过一次性机器（如通过 **Qubes OS**）启动，从而在执行关键任务时不会在会话结束后留下持久痕迹。
- 安装相对简单**：提供即用型镜像，可在虚拟机（VirtualBox、KVM、Qubes）中快速安装。系统文档齐全并定期更新。



## 安装和配置



在开始安装 Whonix 之前，必须注意的是，该发行版**还未正式**为可直接安装在 Hard 磁盘上（裸机模式）的主系统。换句话说，你**还不能将 Whonix 作为经典的主机操作系统**安装，比如 Ubuntu 或标准 Debian。



不过，Whonix 有多个版本可供选择，可用于**易失性**（实时模式、临时会话）或**持久性**（通过虚拟机或集成到 Qubes 操作系统中）。



对于长期、稳定的使用，**虚拟化是目前官方唯一推荐的方法**。您可以使用**VirtualBox**（Whonix-Gateway 和 Whonix-Workstation）运行 Whonix，也可以将其集成到**Qubes OS** 等系统中。在本教程中，我们将重点介绍 VirtualBox 安装。



### 先决条件



在以虚拟模式安装 Whonix 之前，请确保您的计算机满足最低技术要求。虚拟化需要某些资源，但并非所有计算机都能提供这些资源。因此，您的处理器必须支持虚拟化技术（英特尔 VT-x 或 AMD-V），并且 BIOS/UEFI 中已启用该选项。



以下是使用 Whonix 获得流畅稳定体验的建议规格：





- 随机存取内存（RAM）**：强烈建议至少 **8 GB**。内存越大，分配给虚拟机（网关和工作站）的资源就越多，从而提高性能。
- 可用磁盘空间**：请预留至少 30 GB 的可用磁盘空间**。这包括两个虚拟机、系统文件和任何数据或快照所需的空间。
- 处理器**：建议使用至少**4 个物理内核**（8 个逻辑线程）的处理器，特别是如果您想并行运行其他服务或工具。



### 下载 Whonix



Whonix 有多个版本，具体取决于使用环境的类型。对于大多数用户（Windows、Linux 或 MacOs）来说，VirtualBox 版本最容易设置。你可以直接从[官方网站](https://www.whonix.org/wiki/VirtualBox)下载镜像。



⚠️ Whonix **与使用 Apple Silicon 处理器（ARM 架构）的 MacBook 不兼容。



## 安装 VirtualBox



要运行 Whonix，您需要一个**管理程序，如 VirtualBox、Qubes 或 KVM。



下载文件后，像安装其他软件一样进行安装。接受默认选项，除非你有特殊要求。迷路了吗？查看我们的 VirtualBox 使用指南。



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### 导入 Whonix



安装好 VirtualBox 后，就可以导入之前下载的 Whonix `.ova` 文件（`Whonix-Gateway-Xfce.ova` 和`Whonix-Workstation-Xfce.ova`）。



打开 VirtualBox，然后点击 **文件 → 导入设备**。


选择相应的 `.ova` 文件（从网关开始）。



![0_03](assets/fr/03.webp)



选择存储 Whonix 虚拟机文件的位置。



![0_04](assets/fr/04.webp)



接受使用条款，然后启动导入，等待过程结束。



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix 配置



在启动 Whonix 之前，重要的是要调整一些**系统设置**，以确保更好的性能：



选择**Whonix-Workstation-Xfce**虚拟机，然后点击**配置**。



![0_06](assets/fr/07.webp)



进入**系统**选项卡，默认内存分配为 2048 MB。我们建议你**将其增加到 4096 MB（4 GB）**，以提高流畅性，尤其是当你打算打开多个应用程序或长时间工作时。网关可以保持在 2048 MB，除非您并行使用大量 Tor 连接。



![0_08](assets/fr/08.webp)



### 开始使用 Whonix



要使 Whonix 正常、安全地工作，** 您必须遵循以下启动顺序** ：



首先，启动 **Whonix-Gateway-Xfce** 机器。这台机器负责通过**Tor**网络路由所有流量。没有网关的运行，任何流量都不会通过 Tor，你也就失去了匿名性。



![0_09](assets/fr/09.webp)



网关完全启动后（你会看到 Tor 已连接），就可以启动 **Whonix-Workstation-Xfce**，它会自动通过网关连接。



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### 系统更新



进入终端，输入以下命令更新软件包列表：



```shell
sudo apt update
```



然后运行以下命令安装可用的更新：



```shell
sudo apt full-upgrade
```



## 探索 Whonix



**Whonix**是一个旨在提供**安全、**匿名和**保密计算环境的系统，是上网冲浪而不泄露身份或数据的理想选择。为实现这一目标，它配备了大量实用的日常应用程序，旨在从一开始就加强您的数字安全。


### KeepassXC



**KeePassXC** 是 Whonix 的集成密码管理器。它可让您**安全地创建、存储和管理**密码，而无需手动记住所有密码。密码存储在一个**加密的数据库中，并受主密码保护。



### Tor 浏览器



**Tor 浏览器**是 Whonix 的默认网页浏览器。它依赖于**Tor**网络，该网络通过世界各地的多个中继站对您的流量进行重定向，因此几乎无法识别您的真实 IP Address。



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### 电石 Bitcoin Wallet



**Electrum** 是 Whonix 上预装的一款轻便快速的 Bitcoin Wallet，可让您匿名管理**加密货币交易。它不会下载整个 Blockchain，而是使用远程服务器获取必要的信息，因此比完整的 Wallet 要轻便得多。



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix 不仅仅是一个操作系统：它还是一个真正的**安全环境**，旨在保护您的匿名性、隐私和敏感活动。得益于其基于 Tor 的架构、网关和工作站之间的智能分区以及预装的 Tor 浏览器、KeePassXC 和 Electrum 等工具，它为任何希望**匿名浏览**、**安全工作**或**处理机密数据**的人提供了全套解决方案。



要加强 Unix 系统的安全性，请参阅我们的机器审计教程：检查操作系统中的安全漏洞，确保您的数据不被泄露。



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af