---
name: Plan ₿ Academy - Pears App
description: 如何在 Pears 上安装和使用 Plan ₿ Academy 应用程序？
---

![cover](assets/cover.webp)


您可能已经知道 Plan ₿ Academy 是最大的 Bitcoin 教育数据库，它汇集了课程、教程和成千上万的开源资源。最初，Plan ₿ Academy 是一个网站。但是，如果您无法再正常访问它，例如在审查的情况下，会发生什么呢？


在本教程中，我们将学习如何使用**Pears**（一种由**Holepunch**开发、**Tether**支持的点对点（P2P）技术），以真正抗审查的方式运行**Plan ₿ Academy**平台。


Pears 是一款允许我们在不依赖中央网站的情况下运行 Plan ₿ Academy 平台的软件。在本教程中，我们将在您的计算机上安装 Pears，以便通过 Pears 访问 Plan ₿ Academy。


Pears 的目标很简单：无需依赖任何集中式基础设施（无服务器、无主机、无中介），即可分发和使用网络应用程序。换句话说，即使云服务提供商关闭或某个国家封锁了某个域名，应用程序也能继续在网络的同行中运行。通过这种方法，我们的教育平台 Plan ₿ Academy 可以在全球范围内访问，不会出现单点故障。


---

**TL;DR:**



- 安装梨；



- 运行以下命令启动 Plan ₿ Academy 应用程序：


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1.梨是什么？


Pears 同时是一个运行环境、一个开发工具和一个点对点应用程序的部署平台。这款开源工具允许你在没有服务器或基础设施的情况下，直接在用户之间构建、共享和运行软件。在实践中，这意味着每个用户都成为网络中的一个节点：他们与其他对等用户共享部分应用程序和数据，而不是将应用程序托管在中央服务器上。整个系统形成一个分布式网络，每个实例相互合作，以保持服务的可访问性。


![Image](assets/fr/01.webp)


这种方法基于 Holepunch 开发的一套模块化软件组件：



- 超核**：分布式日志，无需中央数据库即可确保数据的一致性和安全性。
- Hyperbee**：建立在 Hypercore 基础上的索引，可以高效地组织和查询数据。
- Hyperdrive**：一种分布式文件系统，用于在同行之间存储和同步应用程序文件。
- Hyperswarm**和**HyperDHT**：网络层，无需中央服务器即可在全球范围内实现对等物发现和连接。
- Secretstream**：一种端到端加密协议，可确保对等方之间的通信安全。


通过结合这些组件，Pears 可以创建自主、加密和分布式应用程序，让每个用户都积极参与到网络中来。这种分散式架构消除了基础设施成本、审查风险和 SPOF（*单点故障*）。


Pears 由 Holepunch 开发，该公司由马蒂亚斯-布斯（Mathias Buus）和保罗-阿多诺（Paolo Ardoino，Tether 首席执行官和 Bitfinex 首席技术官）创立，其使命是将点对点逻辑扩展到 Bitcoin 之外。他们的目标是建立一个 "点对点互联网"，在这个互联网上，每个应用程序都可以在没有许可、没有服务器、没有中介的情况下运行。Holepunch已经在**Keet**背后，这是一个完全P2P的视频会议和信息应用程序。


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*本 Pears 安装教程根据操作系统的不同分为多个部分。请直接转到与你的环境相对应的部分，按照相应的说明进行操作： *



- Linux（Debian）** → 第**2节**
- 视窗** → 第**3节**
- macOS** → 第 **4 节**


## 2.如何在 Linux（Debian）上安装 Pears？


在 Debian 上安装 Pears 相对简单，但需要一些先决条件，我们将在本节详细介绍。


### 2.1.更新系统


在做其他任何事情之前，确保您的系统是最新的很重要。


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2.安装依赖项


Pears 依赖于一些系统库，包括 Bare JavaScript 运行时引擎使用的 `libatomic1`。使用以下命令安装：


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3.通过 NVM 安装 Node.js 和 npm


Pears通过*npm*（*Node.js*软件包管理器）发布。虽然Pears并不直接依赖*Node.js*运行，但安装时需要使用*Node.js*。在Linux上安装*Node.js*的推荐方法是通过*NVM*（*Node版本管理器*），它允许你同时管理多个版本的Node。


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


然后，重新加载终端以激活 *NVM*：


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


检查 *NVM* 是否正确安装：


```bash
nvm --version
```


![Image](assets/fr/06.webp)


接下来，安装稳定版本的 *Node.js*（例如当前的 LTS 版本）：


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


确认 *Node.js* 和 *npm* 已正确安装：


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4.使用 npm 安装梨


一旦 *npm* 可用，就可以在系统中全局安装 Pears CLI。这样就可以在任何目录下运行 `pear` 命令。


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5.初始化梨


安装完成后，只需在终端运行以下命令即可：


```bash
pear
```


首次启动时，Pears 会连接到对等网络，下载必要的组件。这一过程不依赖于任何中央服务器，而是直接从其他对等网络获取文件。


![Image](assets/fr/10.webp)


下载完成后，再次运行命令确认一切正常：


```bash
pear
```


![Image](assets/fr/11.webp)


如果一切安装正确，Pears 帮助菜单将显示可用命令列表。


### 2.6.用 Keet 测试梨


要验证 Pears 是否完全正常运行，可以启动网络上现有的 P2P 应用程序，如 Holepunch 开发的开源信息和视频会议软件 Keet。


```bash
pear run pear://keet
```


该命令不使用中央服务器，直接从 Pears 网络加载 Keet 应用程序。如果 Keet 能正确启动，说明你的 Pears 安装已完全正常。


![Image](assets/fr/12.webp)


现在，您的 Linux 系统已准备就绪，可以使用 Pears 运行和托管点对点应用程序。


## 3.如何在 Windows 上安装 Pears


在 Windows 上安装 Pears 与在 Linux 上一样简单，但需要一些特定工具。


*如果您使用的是 Linux 系统，并且已经安装了 Pears，则可直接跳至**步骤 5**。


### 3.1.以管理员身份打开 PowerShell


首先，以管理员权限启动 PowerShell：



- 点击开始菜单；
- 键入 "PowerShell"；
- 右键单击 "*Windows PowerShell*"；
- 选择 "*以管理员身份运行*"。


![Image](assets/fr/15.webp)


### 3.2.下载 NVS


Pears是通过*npm*（*Node.js*软件包管理器）安装的。在 Windows 系统上，Holepunch 推荐使用 *NVS*（*Node Version Switcher*），它比 *NVM* 更稳定。


在 PowerShell 中运行以下命令安装最新版本的 *NVS*：


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3.安装 Node.js


安装完成后，重启 PowerShell，然后输入以下命令：


```powershell
nvs
```


您将看到可用的 *Node.js* 版本列表。按键盘上的 `a` 键，选择第一个版本。


![Image](assets/fr/17.webp)


*Node.js* 已安装。


![Image](assets/fr/18.webp)


### 3.4.核实安装


确保 *Node.js* 和 *npm* 可访问：


```powershell
node -v
npm -v
```


这两条命令都应返回版本号。


![Image](assets/fr/19.webp)


### 3.5.使用 npm 安装梨


一旦 *Node.js* 和 *npm* 可用，请在系统中全局安装 **Pears CLI**：


```powershell
npm install -g pear
```


这将在你的全局 *npm* 目录中安装 `pear` 二进制文件。


![Image](assets/fr/20.webp)


### 3.6.验证和初始化梨形图


安装完成后运行：


```powershell
pear
```


首次启动时，Pears 会自动从点对点网络下载所需的组件。这一过程可能需要片刻时间。


![Image](assets/fr/21.webp)


如果一切顺利，您将看到 Pears CLI 帮助菜单，其中包含可用子命令列表（运行、seed、信息......）。


### 3.7.用 Keet 测试梨


要验证 Pears 是否完全正常运行，可以启动网络上现有的 P2P 应用程序，如 Holepunch 开发的开源信息和视频会议软件 Keet。


```bash
pear run pear://keet
```


该命令不使用任何中央服务器，直接从 Pears 网络加载 Keet 应用程序。如果 Keet 成功启动，就意味着你的 Pears 安装已完全正常。


![Image](assets/fr/22.webp)


现在，您的 Windows 系统已准备就绪，可以使用 Pears 运行和托管点对点应用程序。


## 4.如何在 macOS 上安装梨


在 macOS 上安装 Pears 与 Linux 相似，但需要针对苹果环境做一些调整。让我们一起来完成这些步骤。


*如果您使用的是 Linux 或 Windows 系统，并且已经安装了 Pears，则可以直接跳到**步骤 5***.


### 4.1.检查系统先决条件


安装之前，请确保您的系统已安装 *Xcode Command Line Tools*。此软件包为 *Node.js* 及其依赖项提供了必要的构建工具。


为此，请使用快捷键 "Cmd + 空格键 "打开终端，输入 "终端"，然后按 "Enter "键。然后，在终端中运行以下命令进行安装：


```bash
xcode-select --install
```


如果系统中已安装这些工具，macOS 会发出通知。


### 4.2.安装 NVM


Pears通过*Node.js*软件包管理器*npm*发布。虽然Pears并不直接依赖*Node.js*运行，但安装时需要*Node.js*。在macOS上安装*Node.js*的推荐方法是*NVM*（*Node版本管理器*），它允许你同时管理多个Node版本。


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


然后重新加载终端，激活 *NVM*：


```bash
source ~/.zshrc
```


如果使用 *bash* 而不是 *zsh*，请运行


```bash
source ~/.bashrc
```


接下来，检查 *NVM* 是否安装正确：


```bash
nvm --version
```


终端应显示已安装的 *NVM* 版本。


### 4.3.安装 Node.js 和 npm


接下来，安装稳定版本的 *Node.js*（例如当前的 LTS 版本）：


```bash
nvm install --lts
```


安装完成后，请验证已安装的版本：


```bash
node -v
npm -v
```


这两条命令都应返回版本号。


### 4.4.使用 npm 安装梨


一旦 *npm* 可用，就可以在系统中全局安装 Pears CLI。这将允许你在任何目录下执行 `pear` 命令。


```bash
npm install -g pear
```


### 4.5.初始化梨


安装完成后，只需在终端运行以下命令即可：


```bash
pear
```


首次启动时，Pears 会连接到对等网络，下载必要的组件。这一过程不需要任何中央服务器，而是直接从其他对等网络获取文件。


下载完成后，重新运行命令验证一切正常：


```bash
pear
```


如果一切安装正确，Pears 帮助菜单将显示可用命令列表。


### 4.6.用 Keet 测试梨


要验证 Pears 是否完全正常运行，可以启动网络上已有的 P2P 应用程序，如 Holepunch 的开源信息和视频会议软件 Keet。


```bash
pear run pear://keet
```


该命令不使用中央服务器，直接从 Pears 网络加载 Keet 应用程序。如果 Keet 启动成功，说明你的 Pears 安装已完全正常。


现在，你的 macOS 系统已准备就绪，可以使用 Pears 运行和托管点对点应用程序。


## 5.如何在梨上使用₿计划学院


安装并运行 Pears 后，即可通过 P2P 网络直接启动 **Plan ₿ Academy** 平台。只需在终端运行以下命令即可（相同命令可在 Linux、Windows 和 macOS 上运行）：


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


加载完成后，Plan ₿ Academy 将在 Pears 环境中打开，就像原始网站一样随时可用，但无需依赖中央服务器。


![Image](assets/fr/14.webp)


## 6.如何制定播种计划 ₿ 梨学院


在 Pears 网络中，*seed* 应用程序意味着从您自己的计算机将其重新分配给其他同行。实际上，当你使用 seed Plan ₿ Academy 时，你的计算机就成了一个数据源，其他用户无需依赖中央服务器即可下载应用程序。


这种机制增强了我们的应用程序在梨网络上的弹性和抗审查能力。应用程序的 seed 对等体越多，其可用性和去中心化程度就越高，即使一些原始节点离线也不例外。


要帮助分发 Plan ₿ Academy，只需运行以下命令即可：


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


只要该命令处于激活状态，设备就会参与分发应用程序的文件。如果关闭终端，共享进程就会停止。


要在重启后继续播种，可以在后台运行命令或创建系统服务，例如 Linux 上的 systemd 服务、macOS 上的 LaunchAgent 或 Windows 上的计划任务。这些方法可确保 Plan ₿ Academy 应用程序在系统启动时自动恢复播种。


感谢您为梨子上的《Plan ₿学院》的分散式传播做出贡献，并帮助 Bitcoin 教育真正抵制审查！