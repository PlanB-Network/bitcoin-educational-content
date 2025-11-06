---
name: 梨
description: 如何在 Pears 上安装和使用应用程序？
---

![cover](assets/cover.webp)



在本教程中，我们将学习如何在**Pears**上运行应用程序，这是一种由**Holepunch**开发、**Tether**支持的点对点（P2P）技术。其目的很简单：使网络应用程序的发布和使用不依赖任何集中式基础设施（无服务器、无主机、无中介）成为可能。换句话说，即使云提供商倒闭或某个国家封锁了某个域名，应用程序也能在网络对等方中继续运行。



## 1.梨是什么？



Pears 是点对点应用程序的运行环境、开发工具和部署平台。这一开源工具使用户之间直接构建、共享和运行软件成为可能，而无需服务器或基础设施。具体而言，这意味着每个用户都成为一个网络节点，与其他对等用户共享部分应用程序和数据，而不是将应用程序托管在中央服务器上。整个系统形成一个分布式网络，每个实例相互合作，以保持服务的可访问性。



![Image](assets/fr/01.webp)



这种方法基于 Holepunch 开发的一套模块化软件砖：




- 超核**：分布式日志，无需中央数据库即可保证数据的一致性和安全性。
- Hyperbee**：Hypercore 上的索引器，用于高效的数据组织和浏览。
- Hyperdrive**：一种分布式文件系统，用于在对等机之间存储和同步应用程序文件。
- Hyperswarm**和**HyperDHT**：无需中央服务器，即可在全球范围内发现和连接对等体的网络层。
- Secretstream**：E2E 加密协议，用于确保两个对等方之间的交换安全。



通过结合这些组件，Pears 可以创建自主、加密和分布式应用程序，让每个用户都积极参与到网络中来。这种分散式架构消除了基础设施成本、审查风险和 SPOF（*单点故障*）。



## 2.项目的起源和理念



Pears 由 Holepunch 开发，该公司由 Mathias Buus 和 Paolo Ardoino（Tether 首席执行官和 Bitfinex 首席技术官）创立，其使命是将点对点逻辑扩展到 Bitcoin 之外。他们的目标是建立一个 "点对点互联网"，在这个互联网上，每个应用程序都可以在没有授权、没有服务器、没有中介的情况下运行。Holepunch 已经是**Keet**的幕后推手，这是一个完全 P2P 的视频会议和信息应用程序。



*本 Pears 安装教程根据操作系统的不同分为几个部分。请直接转到与你的环境相对应的部分，按照相应的说明进行操作： *




- Linux（Debian）** → 第**部分3**
- 视窗** → 第**4部分**
- macOS** → 第 **5** 部分



## 3.如何在 Linux（Debian）上安装 Pears



在 Debian 系统上安装 Pears 相对简单，但需要一些先决条件，我们将在本节详细介绍。



### 3.1. 更新系统



首先，最重要的是确保您的系统是最新的。



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. 安装依赖项



Pears 依赖于某些系统库，特别是 Bare JavaScript 运行时使用的`libatomic1`。使用以下命令安装：



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. 通过 NVM 安装 Node.js 和 npm



Pears通过*Node.js*软件包管理器*npm*发布。虽然 Pears 的运行并不直接依赖于 *Node.js*，但安装时必须使用 *Node.js*。在Linux上安装*Node.js*的推荐方法是*NVM*（*Node版本管理器*），它允许你并行管理多个版本的Node。



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



然后重新加载终端，激活 *NVM* ：



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



检查 *NVM* 是否已安装：



```bash
nvm --version
```



![Image](assets/fr/06.webp)



然后安装稳定版本的 *Node.js*（例如当前的 LTS）：



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



检查 *Node.js* 和 *npm* 安装情况：



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 使用 npm 安装梨



一旦 *npm* 可用，就可以在系统中全局安装 Pears CLI。这样，你就可以在任何目录下运行 `pear` 命令。



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5.初始化梨



安装完成后，只需在终端运行以下命令即可：



```bash
pear
```



首次启动时，Pears 会连接到对等网络，下载必要的组件。这一过程不需要中央服务器：文件直接从其他对等网络获取。



![Image](assets/fr/10.webp)



下载完成后，再次运行命令检查是否一切正常：



```bash
pear
```



![Image](assets/fr/11.webp)



如果一切安装正确，Pears Help 将显示可用命令列表。



### 3.6.用 Keet 测试梨



要检查 Pears 是否完全正常运行，可以启动网络上已有的 P2P 应用程序，如 Holepunch 的开源信息和视频会议软件 Keet。



```bash
pear run pear://keet
```



该命令直接从 Pears 网络加载 Keet 应用程序，无需通过中央服务器。如果 Keet 能正确启动，说明你的 Pears 安装已完全正常。



![Image](assets/fr/12.webp)



现在，您的 Linux 系统已准备就绪，可以使用 Pears 运行和托管点对点应用程序。



## 4.如何在 Windows 上安装 Pears



在 Windows 上安装 Pears 与在 Linux 上一样简单，但需要一些特殊工具。



*如果您使用的是 Linux，则可跳至步骤 6.*。



### 4.1. 以管理员模式打开 PowerShell



首先，以管理员权限运行 PowerShell：




- 点击开始菜单；
- 键入 PowerShell ；
- 右键单击 "*Windows PowerShell*"；
- 选择 "*以管理员身份运行*"。



![Image](assets/fr/15.webp)



### 4.下载 NVS



Pears是通过*npm*（*Node.js*软件包管理器）安装的。在 Windows 系统上，Holepunch 推荐使用 *NVS*（*Node Version Switcher*），它比 *NVM* 更稳定。



在 PowerShell 中运行以下命令安装最新版本的 *NVS* ：



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. 安装 Node.js



安装完成后，重启 PowerShell 并输入以下命令：



```powershell
nvs
```



您将看到可用的 *Node.js* 版本列表。按键盘上的 `a` 键，选择第一个版本。



![Image](assets/fr/17.webp)



*已安装 Node.js*。



![Image](assets/fr/18.webp)



### 4.4.检查安装情况



确保 *Node.js* 和 *npm* 可访问：



```powershell
node -v
npm -v
```



这两条命令都必须返回版本号。



![Image](assets/fr/19.webp)



### 4.5.使用 npm 安装 Pears



一旦 *Node.js* 和 *npm* 可用，请在系统上全局安装 **Pears CLI**：



```powershell
npm install -g pear
```



这将在全局 *npm* 目录中安装 `pear` 二进制文件。



![Image](assets/fr/20.webp)



### 4.6.检查并初始化 Pears



安装完成后，运行 ：



```powershell
pear
```



首次启动时，Pears 会自动从点对点网络下载必要的组件。这一过程可能需要片刻时间。



![Image](assets/fr/21.webp)



如果一切顺利，您将看到 CLI Pears 帮助屏幕，上面列出了可用的子命令（运行、seed、信息......）。



### 4.7.用 Keet 测试梨



要检查 Pears 是否完全正常运行，可以启动网络上已有的 P2P 应用程序，如 Holepunch 的开源信息和视频会议软件 Keet。



```bash
pear run pear://keet
```



该命令直接从 Pears 网络加载 Keet 应用程序，无需通过中央服务器。如果 Keet 能正确启动，说明你的 Pears 安装已完全正常。



![Image](assets/fr/22.webp)



现在，您的 Windows 系统已准备就绪，可以使用 Pears 运行和托管点对点应用程序。



## 5.如何在 macOS 上安装 Pears？



在 macOS 上安装 Pears 与在 Linux 上安装类似，但需要针对苹果环境做一些调整。让我们一起来探索这些步骤。



*如果您使用的是 Linux 或 Windows 系统，并且已经安装了 Pears，则可以直接进入**步骤 6**。



### 5.1.检查系统要求



安装之前，请确保您的系统中已安装 *Xcode Command Line Tools*。此软件包为 _Node.js_ 及其依赖项提供了必要的编译工具。



为此，请使用键盘快捷键 "Cmd + 空格键 "打开终端，然后键入 "终端 "并按下 "Enter "键。然后在终端中输入此命令即可启动安装：



```bash
xcode-select --install
```



如果系统中已经安装了这些工具，macOS 会通知你。



### 5.2. 安装 NVM



Pears通过*Node.js*软件包管理器*npm*发布。虽然Pears的运行并不直接依赖于*Node.js*，但它是安装所必需的。在 macOS 上安装 *Node.js* 的推荐方法是 *NVM* （*Node 版本管理器*），它允许你并行管理多个 Node 版本。



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



然后重新加载终端，激活 *NVM* ：



```bash
source ~/.zshrc
```



如果使用 *bash* 而不是 *zsh*，请运行 ：



```bash
source ~/.bashrc
```



然后检查 *NVM* 是否已安装：



```bash
nvm --version
```



终端应返回系统中安装的 *NVM* 版本。



### 5.3. 安装 Node.js 和 npm



然后安装稳定版本的 *Node.js*（例如当前的 LTS）：



```bash
nvm install --lts
```



安装完成后，检查已安装的版本：



```bash
node -v
npm -v
```



这两条命令都必须返回版本号。



### 5.4 使用 npm 安装梨



一旦 *npm* 可用，就可以在系统中全局安装 Pears CLI。这样就可以在任何目录下运行 `pear` 命令。



```bash
npm install -g pear
```



### 5.5.初始化梨



安装完成后，只需在终端运行以下命令即可：



```bash
pear
```



首次启动时，Pears 会连接到对等网络，下载必要的组件。这一过程不需要中央服务器：文件直接从其他对等网络获取。



下载完成后，再次运行命令检查是否一切正常：



```bash
pear
```



如果一切安装正确，Pears Help 将显示可用命令列表。



### 5.6.用 Keet 测试梨



要检查 Pears 是否完全正常运行，可以启动网络上已有的 P2P 应用程序，如 Holepunch 的开源信息和视频会议软件 Keet。



```bash
pear run pear://keet
```



该命令直接从 Pears 网络加载 Keet 应用程序，无需通过中央服务器。如果 Keet 能正确启动，说明你的 Pears 安装已完全正常。



现在，你的 macOS 系统已准备就绪，可以使用 Pears 运行和托管点对点应用程序。



## 6.如何在梨树上使用应用程序？



Pears 启动并运行后，你可以使用以下命令直接运行你选择的应用程序：



```bash
pear run pear://[KEY]
```



只需将"[KEY]"替换为您希望使用的应用程序密钥即可。



![Image](assets/fr/13.webp)



要了解如何在 Pears 上运行我们的 Plan ₿ Academy 平台，请查看本综合教程 ：



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

要了解如何使用您刚刚在 Pears 上启动的 Keet 消息应用程序，请查看本教程：



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b