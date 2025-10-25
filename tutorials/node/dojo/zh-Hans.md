---
name: 道场
description: 实现隐私和自主的开源 Bitcoin 节点
---

![cover](assets/cover.webp)



*本教程基于[Ashigaru 官方文档](https://ashigaru.rs/docs/)，我接管并扩充了该文档。我重新编写了所有章节，以提高清晰度，增加了更详细的解释，并为初学者提供了插图，使安装和使用更容易理解。



---

Dojo 是一个开放源代码程序，旨在为某些以 Bitcoin core 节点为基础、面向隐私的 Bitcoin 钱包充当后台服务器。从历史上看，它是为与 Samourai Wallet 一起工作而开发的，Samourai Wallet 是一种移动 Wallet，提供先进的隐私功能，如 Whirlpool (CoinJoin)、Ricochet、Stonewall、PayNym...Samourai Wallet 的开发人员被捕后，Samourai Wallet 现已关闭，但其社区继承者**Ashigaru Wallet** 已经接手，并继续依靠 Dojo 为希望在使用 Bitcoin 时控制其数据的用户提供完整的体验。



![Image](assets/fr/01.webp)



实际上，Dojo 是 Wallet 和 Bitcoin 网络之间的网关。如果没有 Dojo，轻量级移动 Wallet 将不得不查询第三方服务器，以获取您的 UTXO 状态和历史记录，或广播您的交易。这意味着对第三方服务器的依赖性和敏感数据的泄露（使用的地址、金额、支付频率等）。有了 Dojo，您可以自己托管该服务器，并直接连接到自己的 Bitcoin 节点。这样，您的所有投资组合请求都将通过由您控制的基础设施进行，没有中间商，从而加强了您的保密性和主权。



## 建立道场的要求



建立 Dojo 服务器并不需要超强的机器。只要有一台入门级电脑、一个稳定的互联网连接，并能让它持续（24/7）开机，任何人都可以建立一个正常工作的 Dojo。



### 选择机器类型



您可以使用 ：




- 一台笔记本电脑
- 台式电脑
- 微型电脑（如 Intel NUC、联想 Thincentre Tiny......）。



每种方案都各有利弊：




- 价格：翻新的迷你电脑或台式机通常比新笔记本电脑便宜。
- 占用空间：迷你电脑占用空间更少。
- 电源 Supply：笔记本电脑的优势在于有电池，这意味着它不会像微型电脑那样在断电时关闭。
- 可升级性："钩刺 "一般可以增加内存或轻松更换 Hard 磁盘。



有关选择设备的更多信息，我建议您学习这门课程：



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### 推荐设备



无需购买新机器。具有以下规格的翻新计算机将比单板电子设备（如 Raspberry Pi）性能更好。



**最低规格：**




- X86-64 架构（64 位处理器）。
- 2 GHz 或更快的双核处理器。
- 最低 8 GB 内存。
- 2 TB 或更大容量的 NVMe SSD（用于存储 Bitcoin 的 Blockchain，以及必要的索引）。



**建议使用的操作系统 **




- 基于 Debian 的发行版，如 Ubuntu 24.04 LTS。



**推荐设备：**




- HP EliteDesk / EliteBook
- 戴尔 OptiPlex
- 联想 ThinkCentre / ThinkPad
- 英特尔 NUC
- 等等



在其他硬件配置上运行 Dojo 服务器也是完全可能的。不过，为了获得最佳性能并减少问题，我们建议您遵循上述建议。



在本教程中，我将使用一台旧的 ThinkCentre Tiny，它配备了英特尔奔腾双核 G4400T 处理器、8 GB 内存和 2 TB 固态硬盘。



## 1 - 安装 Ubuntu



*如果您想在已经配置好的设备上安装 Dojo，可以跳过此步骤，直接进入步骤 2.*。



准备好所选硬件后，就该安装操作系统了。您几乎可以使用任何 Debian 发行版，但我建议您选择 LTS 版本的 Ubuntu，因为它完全符合我们的目的。以下是安装步骤：



### 1.1. 创建可启动 USB 密钥



在一台已经正常工作的电脑（你的常用机器）上，[从官方网站](https://ubuntu.com/download/desktop) 下载 Ubuntu LTS ISO 映像（本文撰写时为 "24.04"，如果有其他版本，请使用最新版本）。



![Image](assets/fr/02.webp)



将至少 8 GB 的 USB 密钥插入电脑，然后使用 [Balena Etcher](https://etcher.balena.io/) 等软件创建可启动密钥。选择刚刚下载的 Ubuntu ISO 映像，选择 USB 密钥作为目标设备，然后开始创建过程（请耐心等待，可能需要几分钟）。



![Image](assets/fr/03.webp)



将可启动 USB 密钥插入已关机的计算机（即您要运行 Dojo 的计算机）。启动计算机，并立即按键盘上的**F12**或**F10**（视机型而定）进入启动菜单。然后在计算机启动顺序中选择 USB 密钥作为优先设备。



![Image](assets/fr/04.webp)



### 1.2. 安装操作系统



出现 Ubuntu 主屏幕。选择 "试用或安装 Ubuntu*"。



![Image](assets/fr/05.webp)



然后按照经典的 Ubuntu 安装程序进行安装：




- 选择语言。
- 选择键盘类型。
- 如果通过 RJ45 电缆连接，则无需配置 Wi-Fi。
- 点击 "*安装 Ubuntu*"，勾选安装第三方软件（Wi-Fi 驱动程序、多媒体编解码器等）选项。
- 当向导询问安装类型时，选择 "*擦除磁盘并安装 Ubuntu*"。 **警告**：此操作将完全删除磁盘内容。请仔细检查所选磁盘是否与用于 Dojo 的 NVMe SSD 相符。
- 创建一个简单的用户名（如 "*loic*"）。
- 为机器命名（如 "*dojo-node*"）。
- 设置强大的密码并妥善保管。
- 启用 "*请求我的密码登录*"选项，以加强安全性。
- 指明您所在的时区，然后点击 "*安装*"。
- 等待安装完成。完成后，系统将自动重新启动。
- 重新启动计算机时取出 USB 安装密钥。



有关 Ubuntu 安装过程的更多详情，请参阅我们的专门教程 ：



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. 系统更新



首次启动后，使用组合键 ***Ctrl + Alt + T*** 打开终端，运行以下命令更新系统：



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2.室外建筑安装



要让 Dojo 正常工作，系统上必须有某些软件砖。这些软件砖用于管理软件库、通信、存档解压缩以及在 Docker 容器内执行 Dojo。所有这些操作都在终端中执行。



### 2.1.准备工作



以下命令将返回个人文件夹。在运行一系列安装之前，这是一个很好的做法。



```bash
cd ~/
```



在安装任何软件之前，请确保机器上可用软件的数据库是最新的。这样可以避免安装过时的版本。



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. 安装实用程序



该系统需要添加若干工具：




- apt-transport-https"：允许您通过 HTTPS 安全下载数据包
- ca-certificates：管理加密连接所需的证书
- curl"：从互联网检索文件
- gnupg-agent"：用于 GPG 密钥管理
- software-properties-common`: 提供用于操作 APT 软件源的实用程序
- unzip：解压 ZIP 格式文件



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



在安装过程中，系统可能会要求您确认。按 "*y*"键，然后按 "*Enter*"键。



![Image](assets/fr/08.webp)



### 2.3. 安装 Torsocks



Torsocks 使某些命令可以通过 Tor 网络执行，从而提高了通信的保密性。



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. 安装 Docker 和 Docker Compose



Dojo 在 Docker 容器内运行。这意味着每个服务都被隔离在一个独立的环境中，从而简化了维护和安全性。为此，您需要安装 Docker 和 Docker Compose 工具，它能让您同时管理多个容器。



#### 添加 Docker 签名密钥



Docker 提供自己的数字签名密钥。添加该密钥可验证下载软件包的真实性。



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### 添加了官方 Docker 存储库



接下来，你需要告诉系统在哪里可以找到 Docker 官方软件包。这条命令会在软件包管理器配置中添加一个新的软件仓库。



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### 安装 Docker 和 Docker Compose



现在可以安装主要的 Docker 组件了。



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### 用户授权



默认情况下，只有以管理员权限执行的命令才能启动 Docker。为了更加方便，我建议将当前用户添加到 "*docker*"组。这样，你就可以使用 Docker，而不必每次都输入 "sudo"。



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3.创建单个用户（可选）



如果您想提高系统的安全性，我建议您创建一个单独的用户，专门用于运行 Dojo。这种分离限制了风险：如果 Dojo 出现安全问题，它不会直接危及您的主账户。



### 3.1. 创建用户账户



下面的命令将创建一个名为 "*dojo*"的新用户。该用户将拥有一个主目录 `/home/dojo`，并可访问 bash 终端。它还将被添加到 sudo 组，以便执行管理命令。



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2.设置密码



为这个账户指定一个强大的密码非常重要。理想情况下，应使用 Bitwarden 等密码管理器为 generate 设置一个较长、Hard 难以猜测的密码组合。



```bash
sudo passwd dojo
```



系统会要求您输入所选密码，然后再次确认。



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3.授权用户使用 Docker



要使用户 "*dojo*"能够启动运行 Dojo 所需的容器，必须将其添加到 Docker 组。这样就不必在每条命令前加上 `sudo`。



```bash
sudo usermod -aG docker dojo
```



### 3.4.系统重启



为了使组更改生效，必须重新启动机器。



```bash
sudo reboot
```



### 3.5.用新用户登录



系统重新启动后，使用***dojo***登录名和之前定义的密码登录。随后的所有步骤都必须使用该专用账户执行。



## 4.下载并检查 Dojo



在安装 Dojo 之前，必须确保文件来自官方开发人员，且未被修改。这一步需要使用 PGP 和哈希值来验证文件的真实性和完整性。



### 4.1. 导入开发者的 PGP 密钥



通过 Tor 下载开发者的公钥，并将其导入本地钥匙串。该密钥将用于验证与 Dojo 文件相关的签名。



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.下载最新版本的 Dojo



读取包含 Dojo 源代码的压缩包。在本例中，最新版本是 `1.27.0`：请根据 [官方 GitHub 代码库中的最新版本](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) 修改命令。



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3.下载指纹和签名



开发人员发布了一个文件，其中列出了存档的数字指纹，以及一个由他们的 PGP 密钥签名的文件。下载它们以便在本地比较您的文件。



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4.检查 PGP 签名



检查指纹文件是否已由导入的密钥签名。



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



正确的结果显示一个有效的签名，密钥为`E53AD419B242822F19E23C6D3033D463D6E544F6`，相关的 Address 为`dojocoder@pm.me`。可能会出现警告，说明密钥未经认证：您可以忽略它。



反之，如果签名无效，则应立即停止安装过程并从头开始。



![Image](assets/fr/17.webp)



### 4.5.检查存档完整性



计算下载文件的 SHA256 指纹，然后打开指纹文件比较两个值。



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



如果两个指纹相同，则可以确定存档未被修改。如果两者不同，就不要再继续了，删除文件。



![Image](assets/fr/18.webp)



### 4.6.提取和整理文件



验证成功后，您就可以解压压缩包，并准备一个专门用于安装 Dojo 的文件夹。



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7.清理不必要的文件



删除不再需要的临时文件和存档，保持环境清洁。



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5.道场配置



Dojo 是一个后端服务器，汇集了多项服务，可与您的投资组合互动并管理您的 Bitcoin 节点。其配置可能比较复杂，但该项目提供了一种简化方法，可自动安装和配置以下组件：




- Dojo（主应用程序接口）
- Bitcoin core（完整的 Bitcoin 节点）
- BTC-RPC 浏览器（网络版 Block explorer）
- Fulcrum 索引器（区块和交易的快速索引）
- 可在 Tor 网络上使用的 Fulcrum 电子货币服务器
- 本地网络上可用的 Fulcrum Electrum 服务器
- 行政管理证书



### 5.1. 管理证书



为了确保对各种服务的访问，您需要 generate 几个唯一标识符：




- bitcoind_rpc_user
- bitcoind_rpc_password
- mysql_root_password
- mYSQL_USER
- mysql_password
- nODE_API_KEY`
- 节点管理员密钥
- node_jwt_secret



这些标识符**必须是唯一的**（这一点非常重要：您不能在多个服务中使用相同的密码），完全由数字、大写字母和小写字母（字母数字）组成，长度约为 40 个字符，以确保高度安全。我再次强烈建议使用密码管理器。



### 5.2.访问配置文件



Dojo 配置文件位于 `conf/` 文件夹中。请移至该目录：



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3.Bitcoin core 配置



用 nano 文本编辑器打开 Bitcoin core 配置文件：



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



在该文件中，输入生成的标识符：



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ *** 将 `your-ID-here` 和 `your-password-here` 替换为您自己的登录名（密码要强）。***



您还可以调整 Bitcoin core 使用的缓存内存大小，以提高性能（如果可用内存较多，甚至可以使用更大的缓存内存）：



```
BITCOIND_DB_CACHE=2048
```



保存更改并关闭编辑器 ：




- 按 `Ctrl + X
- type `y`
- 然后按 "*Enter*"键



### 5.4.MySQL 配置



然后打开 MySQL 数据库配置：



```bash
nano docker-mysql.conf.tpl
```



请输入您的登录信息：



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ *** 将 `your-ID-here` 和 `your-password-here` 替换为您自己的登录名（使用强大、唯一的密码）。***



用同样的方法保存（`Ctrl + X`，`y`，"*Enter*"）。



![Image](assets/fr/23.webp)



### 5.5.支点分度器配置



打开以下文件



```bash
nano docker-indexer.conf.tpl
```



添加参数以激活 Fulcrum 并将其正确集成到 Dojo 中：



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



接下来，根据您的配置，有两种可能。如果 Dojo 安装在一台独立于日常电脑的机器上（专用机、服务器......），请输入本地网络中的 IP Address，例如 ：



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



要找出机器的本地 IP Address，请打开另一个终端并输入以下命令：



```bash
hostname -I
```



第二种可能：如果 Dojo 直接在您的日常个人电脑上运行，请保留配置文件中的默认值：



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



保存并退出编辑器（`Ctrl + X`，`y`，"*Enter*"）。



### 5.6.节点服务配置



最后，打开主 Dojo 服务的配置：



```bash
nano docker-node.conf.tpl
```



请输入您的登录信息：



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ *** 用您自己的凭据（使用强大、唯一的密码）替换`your-password-here`。***



![Image](assets/fr/26.webp)



然后激活本地索引器：



```
NODE_ACTIVE_INDEXER=local_indexer
```



保存并退出编辑器（`Ctrl + X`，`y`，"*Enter*"）。



### 5.7.登录管理



配置完成后，无需保存生成的所有标识符。唯一必须保存的是.NET：



```
NODE_ADMIN_KEY
```



此登录信息将使您稍后能够登录 Dojo 维护工具。所有其他登录名都可以从密码管理器或手写笔记中删除。如果将来需要检索，仍可从 Dojo 配置文件中访问它们。



## 6.道场安装



在此阶段，Dojo 将在您的计算机上安装并启动。该操作将启动多个服务（Bitcoin core、Fulcrum 索引器、Dojo 后台等），并启动 Blockchain Bitcoin 的完全同步。这可能需要几天时间，具体取决于您的硬件和互联网连接。



### 6.1.检查 Docker 是否正常运行



在开始安装之前，请确保 Docker 处于运行状态。运行以下命令



```bash
docker run hello-world
```



该命令会下载并启动一个小型测试容器。如果一切正常，你应该会看到类似于 ：



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



如果未显示此信息，请使用 .NET Framework 3.0 重新启动计算机：



```bash
sudo reboot
```



然后重新登录**dojo**账户，再次运行测试命令。如果错误仍然存在，说明 Docker 安装不正确。在这种情况下，请返回 "2.4. "安装 Docker 的步骤，仔细检查每一条命令。



### 6.2.进入 Dojo 安装目录



安装所需的脚本位于 `my-dojo` 文件夹中。移至该目录：



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



使用 `ls` 命令检查是否存在 `dojo.sh` 文件。这是自动安装 Dojo 和启动其所有服务的主要脚本。



![Image](assets/fr/29.webp)



### 6.3.开始安装



运行 .NET Framework 4.0，开始安装：



```bash
./dojo.sh install
```



按 "y "确认安装，然后按 "*Enter*"。



![Image](assets/fr/30.webp)



该脚本将 ：




- 下载并启动必要的 Docker 容器、
- 初始化 Bitcoin core，并开始同步 Blockchain、
- 启动 Fulcrum 索引器，跟踪交易和地址、
- 激活 Dojo 后端及其 API。



您会看到日志源源不断地滚动，其中包含丰富多彩的参考信息，如 `bitcoind`、`soroban`、`nodejs` 或 `fulcrum`。这种滚动表示 Dojo 已开始运行，并开始执行各种服务。



![Image](assets/fr/31.webp)



### 6.4.退出日志显示



日志会实时显示在终端中。要在 Dojo 后台运行时返回命令提示符，请键入 ：



```
Ctrl + C
```



别担心：停止日志显示并不会停止服务。Docker 会继续在后台运行 Dojo（如果你想让 IBD 继续运行，显然不需要停止计算机）。



### 6.5.了解 *初始区块下载* (IBD)



启动时，Bitcoin core 必须下载并验证 2009 年以来的整个 Blockchain。这一步称为 *** 初始区块下载* (IBD)**。这一步至关重要，因为它能让 Dojo 节点独立验证每个 Bitcoin 区块和交易。



这种同步的持续时间取决于多个因素：




- 处理器的性能和可用的 RAM 内存量、
- 磁盘的速度、
- 节点连接的对等节点的数量和质量、
- 互联网连接的速度。



在实际操作中，这一过程一般需要 2 到 7 天**。在此期间，您可以让机器持续运行。机器运行时间越长，同步完成的速度就越快。我建议您通过查看 Bitcoin core 日志或使用安装后的 Dojo 维护工具（见下一节）定期检查同步状态。



为了加深您对 IBD 的了解，更广泛地说，是对 Bitcoin 节点的运行和作用的了解，我建议您学习本课程：



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7.同步监控



首次安装 Dojo 时，您需要等待两个主要操作完全完成：Blockchain Bitcoin (*IBD*) 的完整下载和 Fulcrum 对该 Blockchain 的索引。根据您的连接和机器功率，这可能需要几天时间。在此期间，您可以监控进程的进展，以确保一切运行顺利。



有两种方法可以监控同步状态：




- 使用 Dojo 维护工具（或 DMT），它很简单，但在 IBD 期间提供的细节很少；
- 直接查看机器上的 Dojo 日志，技术性更强，但更精确。



### 7.1.通过 Dojo 维护工具 (DMT) 进行检查



Dojo 维护工具是一个安全、基于网络的 Interface，可让您监控工厂状态并执行某些操作。它是监控 IBD 进展的最简单、最方便的方法。在初始同步阶段，显示的信息可能有限。例如，DMT 不会显示 Fulcrum 索引的详细进度。另一方面，一旦同步完成，DMT 将清楚地显示 ：




- Green 上的所有灯光；
- 每个服务（节点、索引器、Dojo DB）的最后验证块。



要访问它，你需要知道你的 DMT 的 URL，并[通过 Tor 浏览器](https://www.torproject.org/download/)连接到它。为此，请打开终端，进入 `/my-dojo`目录：



```bash
cd ~/dojo-app/docker/my-dojo
```



然后运行以下命令：



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



然后，您就可以访问通过 Tor 连接到您的 Dojo 的所有相关信息。我们感兴趣的是以下 URL：



```
Dojo API and Maintenance Tool =
```



要从任何网络上的任何机器（甚至远程）访问 DMT，请打开 Tor 浏览器并输入此 URL，然后输入 `/admin`。例如，如果您的 URL 是 `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, 您需要在 [Tor 浏览器](https://www.torproject.org/download/) 栏中输入：



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **请对本 Address 严格保密



然后，您将被重定向到一个身份验证页面。DMT 使用您之前生成的 `NODE_ADMIN_KEY` 密码登录。



![Image](assets/fr/33.webp)



登录后，您可以访问 "*Dojo 维护工具*"！在 IBD 期间，您可以在 "*Full node*"菜单中查看 "*最新区块*"信息，了解 Bitcoin 节点的当前状态。



![Image](assets/fr/34.webp)



记得在 Tor 浏览器中将此 Address 加入书签，以便日后检索。



一旦您的 Dojo 完全同步，您就可以在 DMT 主页的所有指示器上看到 Green 检查 ✅。



### 7.2.通过 Dojo 日志进行验证



跟踪 IBD 进展的第二种方法是直接查阅机器日志。这种方法提供了更为精确的实时监控。你可以看到 Bitcoin core 在下载区块方面的进展，以及 Fulcrum 是如何索引这些区块的。



连接到托管 Dojo 的机器并打开终端。所有命令都应在 `my-dojo` 目录下执行。将自己定位在该文件夹中：



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core 日志



查看 Bitcoin core 日志，跟踪 IBD 进展：



```bash
./dojo.sh logs bitcoind
```



开始时，您将看到区块头的预同步阶段：



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



当这一数字达到 100% 时，Bitcoin core 将开始完整下载 Blockchain。你会看到 IBD 的进度。要了解当前块的高度，请查看 `height=` 所指示的值。你也可以关注关键字 `progress=`，它表示 IBD 进度的百分比。



![Image](assets/fr/36.webp)



要关闭日志并返回命令提示符，请一如既往地使用 "Ctrl + C "组合键。



#### 支点日志



一旦 Bitcoin core 完成报头预同步，Fulcrum 就会开始为 Blockchain 编制索引。使用 .NET 查看其日志：



```bash
./dojo.sh logs fulcrum
```



然后，你将看到最后一个索引块的高度（在 "height: "后显示）以及索引进度百分比。



![Image](assets/fr/37.webp)



### 7.3.Fulcrum 数据库损坏



Fulcrum 是一款功能特别强大的索引器，但它的安装可能比较复杂，尤其是因为它的数据库管理非常精细。如果在初始同步过程中断电或突然关机，索引器的数据库可能会损坏。例如，如果有以下日志，就可以看到这种情况：



```bash
fulcrum | The database has been corrupted etc...
```



**注：** 此类错误应在即将发布的 Fulcrum 2.0 中得到纠正。



如果这种情况发生在您身上，对 bitcoind（您的 Bitcoin 节点）没有任何影响：它的 IBD 将继续独立于 Fulcrum 进行。不过，在您删除其损坏的数据并从头开始重新同步之前，您将无法使用 Fulcrum。具体操作如下



停止道场



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



只删除 Fulcrum 容器和卷：



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



通常情况下，名称为 "my-dojo_data-fulcrum"，如果不是这种情况，请调整上一条命令返回的名称。



然后重新启动 Dojo，从头开始重建 Fulcrum：



```bash
./dojo.sh upgrade
```



然后，你就可以通过查看日志来检查 Fulcrum 是否正常工作了：



```bash
docker logs -f fulcrum
```




## 8.使用道场维护工具



一旦您的 Bitcoin 结与最多的 Proof of Work 结同步到经纱头上，并且 Blockchain 结已 100% 经由 Fulcrum 定位，您就可以开始使用您的道场了。



您的 Dojo 提供了广泛的功能，每个新版本都会定期增强这些功能。在我看来，最重要的 2 项功能是 ：




- 可以连接 Ashigaru Wallet，使用自己的节点查阅 Blockchain 数据并广播您的交易、
- 和 Block explorer，让您可以访问 Blockchain Bitcoin 的信息，而不会将您的数据暴露给您无法控制的外部实例。



让我们来看看如何使用它们。


### 8.1.将 Ashigaru 连接到您的道场



将 Ashigaru Wallet 与道场连接起来非常简单：在 DMT 上打开 "*配对*"菜单。这时会出现一个二维码，您可以直接用 Ashigaru 应用程序扫描。



![Image](assets/fr/38.webp)



在 Ashigaru 应用程序中，创建或恢复 Wallet 后首次启动该程序时，会跳转到 "*配置您的 Dojo 服务器*"页面。按 "*扫描 QR*"，然后扫描 DMT 上显示的 QR 码。



![Image](assets/fr/39.webp)



然后点击 "*继续*"按钮。



![Image](assets/fr/40.webp)



您现在已连接到您的道场。



![Image](assets/fr/41.webp)



### 8.2.使用 Block explorer



Dojo 会自动安装一个 Block explorer，[BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer)，它直接从您自己的 Bitcoin 节点获取数据。资源管理器可让您通过简单易懂的 Interface 网络访问来自 Blockchain 和 Mempool 的原始信息。因此，您可以轻松检查待处理交易的状态、查看 Address 的余额或检查区块的组成。



要访问它，只需从浏览器中获取 Tor Address。为此，请运行与获取 DMT Address 相同的命令：



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



您可以通过 Tor 访问所有 Dojo 连接信息。我们感兴趣的是以下 URL：



```
Block Explorer =
```



如果您已经连接了 DMT，也可以在连接 JSON 内的 "*配对*"菜单中找到此 Address：



![Image](assets/fr/43.webp)



要从任何网络上的任何机器（甚至是远程）访问你的浏览器，请打开 [Tor 浏览器](https://www.torproject.org/download/)，然后输入你刚刚获取的 URL。



⚠️ **请对本 Address 严格保密



这样，您就可以使用自己的 Block explorer。



![Image](assets/fr/44.webp)



*图片来源：https://ashigaru.rs/.*



要跟踪交易，只需在右上角的搜索栏中输入 txid。



![Image](assets/fr/45.webp)



*图片来源：https://ashigaru.rs/.*



要检查与 Address 相关的机芯，请在搜索栏中输入 Address，按同样的方法操作。



![Image](assets/fr/46.webp)



*图片来源：https://ashigaru.rs/.*



您还可以在搜索栏中输入区块的 Hash 或高度，以显示详细信息。



![Image](assets/fr/47.webp)



*图片来源：https://ashigaru.rs/.*



## 9.道场维护



### 9.1 停止你的道场



切勿突然切断 Dojo 的电源，因为这可能会损坏某些数据库，尤其是 Fulcrum 索引器。如果必须关闭，请始终执行 Dojo 的清洁关机操作，然后在完成所有程序后关闭机器：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 更新您的道场



Dojo 会定期更新，并发布新版本以修复错误、提高稳定性和增加功能。因此，[定期检查更新](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) 和更新您的 Dojo 非常重要。更新过程与初始安装类似，但需要将某些文件替换为最新版本，同时保持配置不变。以下是干净、安全更新的详细步骤：



要了解 Dojo 的当前版本，请运行命令 ：



```bash
./dojo.sh version
```



虽然这一步是可选的，但我建议您首先更新操作系统。这样可以降低不兼容的风险，并确保 Dojo 使用的依赖关系是最新的：



```bash
sudo apt-get update
sudo apt-get upgrade
```



转到 Dojo 目录，停止当前服务：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



然后重新启动系统，以获得一个全新的系统：



```bash
sudo reboot
```



Dojo 附带数字签名文件。这些 PGP 签名可确保文件来自开发者，且未被以任何方式更改。重要的是，每次更新 Dojo 时都要检查它们，就像第一次安装时一样。首先通过 Tor 下载开发者的公钥，然后将其导入 .NET Framework：



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



返回个人目录：



```bash
cd ~/
```



通过 Tor 从 GitHub 下载最新版本的 Dojo。在本例中，版本为 `1.28.0`（在撰写本文时，该版本尚不存在：这只是举例说明）。请记住将文件和链接[替换为您希望安装的版本](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases)：



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



同时下载包含 PGP 指纹和签名的文件（再次记住在命令中调整版本）：



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



检查下载的指纹文件是否已由开发者的密钥签名：



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



正确的结果应显示 ：



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



可能会出现密钥未经认证的警告，但这并不重要。另一方面，如果签名无效或对应的是另一个密钥，就不要再继续了，重新开始检查链接。



然后计算存档的 SHA256 指纹，并与官方指纹文件进行比较：



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



如果两个指纹完全吻合，则存档是真实完整的。如果不一致，请立即删除文件，不要继续。



解压缩主目录中的压缩包：



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



然后将内容复制到 Dojo 目录，覆盖旧的 .NET 文件：



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



此操作会保留位于 `~/dojoapp/docker/my-dojo/conf` 中的配置文件，但会用更新版本替换所有其他文件。



要保持环境清洁，请删除不必要的文件：



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



返回 Dojo 脚本目录并运行更新命令：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



该命令指示 Docker 用新文件重建镜像，然后自动重启所有服务。过程结束时，请检查日志，确保 Bitcoin core、Fulcrum 和 Dojo 都能正常工作：



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



如果服务启动时没有出错，并且日志显示正在处理数据块，则说明您的 Dojo 已经更新并开始运行。