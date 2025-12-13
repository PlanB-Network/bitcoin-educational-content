---
name: Ashigaru Terminal
description: 在桌面上使用 Ashigaru 进行硬币接合
---

![cover](assets/cover.webp)



Ashigaru Terminal 是 Ashigaru 团队对 Sparrow 服务器的改编，它实现了 Whirlpool 硬连接协议。该软件是 Samourai Wallet 开始的工作的延续，特别是 Whirlpool 图形用户界面，它采用的基本原则是：自我保管和保密。



该软件是 Sparrow 服务器的 fork，经过修改和优化，可与 Samourai 团队最初开发的 ZeroLink 硬币连接协议 Whirlpool 生态系统完全集成。



Ashigaru Terminal 采用简约的 TUI 界面，可部署在个人电脑或专用服务器上。它可让您直接与 Whirlpool 互动，启动 "*Tx0*"，管理 "*Deposit*"、"*Premix*"、"*Postmix*"和 "*Badbank*"账户，并执行自动混音以加强部件的保密性。



简而言之，如果您想使用 Whirlpool 创建联接，Ashigaru Terminal 将特别有用。



在第一个教程中，我将带您了解 Ashigaru Terminal 的安装和操作。然后，第二篇更高级的教程将专门介绍如何实际创建硬币接合。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1.安装芦原终端



要安装 Ashigaru Terminal，你需要 Tor 浏览器，因为二进制文件只能通过 Tor 网络分发。如果你还没有安装，请[在你的机器上安装](https://www.torproject.org/download/)。



### 1.1. 下载 Ashigaru Terminal



从 Tor 浏览器，转到 [其 Git 仓库的发布页面](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) 为你的操作系统下载最新版本的 Ashigaru Terminal。



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



为您的操作系统下载以下 2 个文件：




- 二进制文件（Debian/Ubuntu 为 `ashigaru_terminal_v1.0.0_amd64.deb`，macOS 为 `.dmg` 或 Windows 为 `.zip`）；
- 签名哈希值文件：`ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2.检查 Ashigaru 终端



在设备上运行软件之前，您需要检查其真实性和完整性。这是非常重要的一步，因为它可以防止您安装可能会危及您的比特币或感染您的机器的欺诈版本。



打开一个新的浏览器标签，进入 [Keybase 验证工具](https://keybase.io/verify)。将刚才下载的 `.txt` 文件内容粘贴到提供的字段中，然后点击 `Verify` 按钮。



![Image](assets/fr/02.webp)



为了使验证来源多样化，您还可以将该信息与 clearnet [ashigaru.rs](https://ashigaru.rs/download/) 网站"/下载 "部分中的信息进行比较。



![Image](assets/fr/03.webp)



如果签名有效，Keybase 将显示一条信息，确认文件已由 Ashigaru 开发人员签名。



![Image](assets/fr/04.webp)



您还可以点击 Keybase 显示的 `ashigarudev` 配置文件，检查其密钥指纹是否完全匹配： `A138 06B1 FA2A 676B`。



![Image](assets/fr/05.webp)



如果在此阶段出现错误，则表示签名无效。在这种情况下，**不要安装下载的软件**。重新从头开始，或在继续之前向社区寻求帮助。



Keybase 已为您提供了应用程序的验证哈希值。现在我们要检查你下载的 `.deb`、`.zip` 或 `.dmg`文件的哈希值是否与 Keybase 上验证的一致。为此，请访问 [HASH FILE ONLINE](https://hash-file.online/)。



点击 "BROWSE... "按钮，选择在步骤 1.1 中下载的".deb"、".zip "或".dmg "文件。然后选择 `SHA-256` 哈希函数，点击 `CALCULATE HASH` 以 generate 文件的哈希值。



![Image](assets/fr/06.webp)



然后，网站将显示软件哈希值。将其与您在 Keybase.io 上验证的哈希值进行比较。如果两者完全匹配，则真实性和完整性检查成功。然后您就可以使用该软件了。



![Image](assets/fr/07.webp)



### 1.3 启动芦原终点站





- Debian / Ubuntu



要安装软件，请运行命令 ：



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



根据下载版本修改顺序。



然后检查安装情况：



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



然后启动软件：



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- 视窗**



右键单击已下载并检查过的".zip "文件，然后选择 "全部解压缩... "以解压缩其内容。



提取完成后，双击 "Ashigaru-terminal.exe "文件启动软件。



![Image](assets/fr/08.webp)



## 2.开始使用 Ashigaru 终端



Ashigaru Terminal 是一个 TUI（*基于文本的用户 Interface*）程序，即直接在终端中运行的简约界面。你可以使用菜单和键盘快捷键与之交互，但不需要任何真正的经典图形环境。



![Image](assets/fr/09.webp)



使用方法很简单：使用键盘上的方向键浏览菜单，按 "Enter "键验证操作或确认选择。



## 3.将您的节点连接到芦原终点站



默认情况下，Ashigaru Terminal 会连接到公共 Electrum 服务器。这显然会带来保密和主权方面的风险。因此，我们要将其配置为直接连接到您自己的 Electrum Server。



为此，请打开 "首选项 > 服务器 "菜单。



![Image](assets/fr/10.webp)



点击"< 编辑 >"按钮。



![Image](assets/fr/11.webp)



选择 "Private Electrum Server"，然后单击"<继续>"。



![Image](assets/fr/12.webp)



输入服务器的 URL 和端口。您可以在`.onion`中指定一个 Tor 地址。然后点击 `< Test >` 验证连接。



![Image](assets/fr/13.webp)



如果连接成功，则会显示 "Success"（成功）信息以及服务器的详细信息。



![Image](assets/fr/14.webp)



如果您还没有 Bitcoin 节点，我建议您学习这门课程：



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*在本教程中，我将断开 Electrs 服务器的连接，因为我要在 testnet 上工作。不过，在 mainnet.* 上的操作完全相同。



## 4.在 Ashigaru Terminal 上创建投资组合



软件配置正确后，我们就可以添加 Bitcoin 产品组合了。



您有两个选择：




- 您可以从头开始创建一个新的 wallet，并将其专用于 Ashigaru Terminal。在这种情况下，每次与 wallet 交互时都需要打开该软件；
- 或者，您也可以将现有的 Ashigaru wallet 直接从手机导入 Ashigaru Terminal。这种方法的缺点是会稍微降低设置的安全性，因为您的 wallet 会暴露在两个而不是一个风险环境中。另一方面，它的优点是可以让 Ashigaru Terminal 持续运行以混合您的金币，同时允许您通过 Ashigaru 移动应用程序远程消费金币。



在本教程中，我们将选择第二种方法。不过，如果你想创建一个全新的作品集，步骤也是一样的：唯一不同的是在创建过程中，你需要保存新的记忆短语和新的 passphrase。



另请注意，Ashigaru Terminal 不允许您直接花费比特币。您可以在 Ashigaru Terminal 和 Ashigaru 应用程序上同步同一个钱包（这正是我将在本教程中演示的），或在 Sparrow Wallet 上进行同步。



如果您还没有关于 Ashigaru 应用程序的 wallet，可以参考专门的教程 ：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

进入 "钱包 "菜单。



![Image](assets/fr/15.webp)



然后选择 "创建/恢复 wallet..."。打开 Wallet...` 选项可让您日后访问 Ashigaru Terminal 中已保存的投资组合。



![Image](assets/fr/16.webp)



给你的投资组合取个名字。



![Image](assets/fr/17.webp)



然后选择投资组合类型 "Hot Wallet"。






![Image](assets/fr/18.webp)



在这一阶段，不同的程序取决于您最初的选择：




- 如果您想从头开始创建一个新组合，请单击"<生成新 Wallet>"，定义一个 passphrase BIP39，然后小心地将您的记忆短语和 passphrase 保存在物理介质上；



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- 如果您希望使用与 Ashigaru 应用程序相同的 wallet，请在相应字段中直接输入记忆短语的 12 个单词和 passphrase BIP39。请用小写字母、全称、按顺序、用空格隔开、不带数字或额外字符书写这些单词。



完成此步骤后，点击 `< 下一步 >`。



*注意*：如果无法点击此按钮，则表示您的记忆短语无效。请仔细检查所有单词是否有误或拼写错误。



![Image](assets/fr/19.webp)



然后您需要设置密码。该密码用于解锁灰原终端 wallet，防止未经授权的物理访问。它不参与密钥的加密推导：换句话说，即使没有这个密码，任何人只要有您的记忆短语和 passphrase 就能恢复您的 wallet 并访问您的比特币。



选择一个长、复杂、随机的密码。在安全的地方保存一份副本：最好保存在物理介质或安全的密码管理器中。



完成后点击 `< OK >`。



![Image](assets/fr/20.webp)



## 5.使用投资组合



然后，您可以选择访问哪个账户。目前，我们还没有启动任何混合，所以我们将访问 "存款 "账户。



![Image](assets/fr/21.webp)



由于 Ashigaru Terminal 是 Sparrow 服务器的 fork，因此操作与 Sparrow 完全相同。您会发现相同的菜单：



![Image](assets/fr/22.webp)





- transactions"（交易）：可以查看与该账户相关联的历史交易记录。在我的情况下，其中一些已经出现，因为我曾在同一个 wallet 上使用 Ashigaru 应用程序进行过一些交易。



![Image](assets/fr/23.webp)





- receive`：生成一个新的空白收据地址，用于将储蓄存入存款账户。



![Image](assets/fr/24.webp)





- addresses`: 显示所有地址的列表，无论它们属于账户的内部链还是外部链。



![Image](assets/fr/25.webp)





- UTXOs`：列出所有可用的 UTXOs。



![Image](assets/fr/26.webp)





- 设置"：可访问您的投资组合*描述符*。您还可以查看您的 seed、调整 *Gap Limit* 或更改投资组合的创建日期。



![Image](assets/fr/27.webp)



您现在已经了解如何安装和使用 Ashigaru Terminal。 在下一个教程中，我们将了解如何使用此软件执行 coinjoin 以及如何在“*Postmix*”中管理资金。
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
