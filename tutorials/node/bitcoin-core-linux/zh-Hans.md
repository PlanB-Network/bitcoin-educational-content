---
name: Bitcoin Core (Linux)
description: 在 Linux 上使用 Bitcoin core 运行自己的节点
---

![cover](assets/cover.webp)


## 使用 Bitcoin core 运行自己的节点


介绍 Bitcoin 和节点的概念，辅以全面的 Linux 安装指南。


Bitcoin 最令人兴奋的一点是，我们可以自己运行程序，从而在更细的层面上参与网络和公共交易 Ledger 的验证。


Bitcoin 作为一个开源项目，自 2009 年以来一直免费提供并公开发布。成立近 17 年后，Bitcoin 已成为一个强大且不可阻挡的数字货币网络，并受益于强大的有机网络效应。Satoshi 中本聪的努力和远见值得我们感谢。顺便说一句，我们在 Agora 256 上发布了 Bitcoin 白皮书（注：也在大学里发布）。


### 成为自己的银行


对于 Bitcoin 精神的拥护者来说，运行自己的节点已经变得至关重要。无需征得任何人的同意，就可以从一开始就下载 Blockchain，从而根据 Bitcoin 协议验证从 A 到 Z 的所有交易。


该程序还包括自己的 Wallet。因此，我们可以控制发送到网络其他部分的交易，而无需任何中介或第三方。您就是自己的银行。


因此，本文的其余部分将专门介绍如何在兼容 Debian 的 Linux 发行版（如 Ubuntu 和 Pop！OS）上安装 Bitcoin core（使用最广泛的 Bitcoin 软件版本）。根据本指南，您将离个人主权更近一步。


## Bitcoin core Debian/Ubuntu 安装指南


**前提条件**


- 至少 6GB 数据存储空间（pruned 节点）- 1TB 数据存储空间（Full node）
- 预计 *初始块下载* (IBD) 至少需要 24 小时。即使是 pruned 节点也必须执行此操作。
- 即使是 pruned 节点，也要为 IBD 预留 ~600GB 的带宽。


**注：💡** 下列命令为 Bitcoin core 版本 24.1 的预定义命令。


### 下载和验证文件



- [下载](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`，以及 `SHA256SUMS` 和 `SHA256SUMS.asc` 文件（显然您需要下载最新版本的软件）。



- 在下载文件所在的目录下打开终端。例如：`cd ~/Downloads/`。



- 使用 "sha256sum --ignore-missing --check SHA256SUMS "命令验证版本文件的校验和是否列在校验和文件中。



- 该命令的输出应包括下载的版本文件名，后面跟`OK`。Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz:OK`。



- 使用 `sudo apt install git` 命令安装 git。然后，使用 `git clone https://github.com/Bitcoin-core/guix.sigs` 命令克隆包含 Bitcoin core 签名者 PGP 密钥的仓库。



- 使用`gpg --import guix.sigs/builder-keys/*` 命令导入所有签名者的 PGP 密钥



- 使用 "gpg --verify SHA256SUMS.asc "命令验证校验和文件是否已用签名者的 PGP 密钥签名。



每个有效签名都会显示一行以gpg：良好签名 "开头的一行和以 "主密钥指纹："结尾的一行：主密钥指纹：133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320`（Pieter Wuille 的 PGP 密钥指纹示例）。


**注意💡：** 并非所有签名密钥都必须返回 "OK"。事实上，可能只需要一个。用户可自行决定 PGP 验证的验证阈值。


你可以忽略这些警告：



- 此密钥未经可信签名认证！``



- 没有迹象表明签名属于所有人。


### 安装 Bitcoin core 图形化 Interface



- 在终端中，仍在 Bitcoin core 版本文件所在的目录下，使用 "tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz" 命令解压压缩包中的文件。



- 使用命令 `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*` 安装之前提取的文件



- 使用 "sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev "命令安装必要的依赖项。



- 使用 `Bitcoin-qt` 命令启动 _bitcoin-qt_ (Bitcoin core 图形化 Interface)。



- 要选择 pruned 节点，请选中 _Limit Blockchain storage_ 并配置要存储的数据限制：


![welcome](assets/fr/02.webp)


### 第 1 部分结论：安装指南


安装 Bitcoin core 后，建议尽可能保持其运行，通过验证交易和向其他对等方传输新区块，为 Bitcoin 网络做出贡献。


不过，间歇性地运行和同步节点，哪怕只是为了验证接收和发送的事务，仍不失为一种好的做法。


![Creation wallet](assets/fr/03.webp)


## 为 Bitcoin core 节点配置 Tor


**注意💡：** 本指南适用于兼容 Ubuntu/Debian 的 Linux 发行版上的 Bitcoin core 24.0.1。


### 为 Bitcoin core 安装和配置 Tor


首先，我们需要安装 Tor 服务（洋葱路由器），这是一个用于匿名通信的网络，可以让我们匿名处理与 Bitcoin 网络的交互。如需了解包括 Tor 在内的在线隐私保护工具，请参阅我们的相关文章。


要安装 Tor，请打开终端并输入 `sudo apt -y install tor`。安装完成后，服务通常会在后台自动启动。使用命令 `sudo systemctl status tor` 检查服务是否正常运行。响应应显示 `Active: active (exited)`。按 `Ctrl+C` 键退出此功能。


**提示：** 在任何情况下，你都可以在终端中使用以下命令来启动、停止或重启 Tor：


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


接下来，让我们使用 "Bitcoin-qt "命令启动 Bitcoin core 图形化 Interface。然后，启用软件的自动功能，通过 Tor 代理路由我们的连接：设置 > 网络_，然后勾选_通过 SOCKS5 代理（默认代理）连接_和_使用单独的 SOCKS5 代理通过 Tor 洋葱服务连接对等网络_。


![option](assets/fr/04.webp)


Bitcoin core 会自动检测是否安装了 Tor，如果安装了 Tor，除了与使用 IPv4/IPv6 网络（clearnet）的节点建立连接外，默认情况下还会与同样使用 Tor 的其他节点建立出站连接。


**注💡：** 要将显示语言更改为法语，请转到 "设置 "中的 "显示 "选项卡。


### Tor 高级配置（可选）


我们可以对 Bitcoin core 进行配置，使其只使用 Tor 网络与对等网络连接，从而优化节点的匿名性。由于 Interface 图形界面没有内置功能，我们需要手动创建一个配置文件。转到 "设置"，然后是 "选项"。


![option 2](assets/fr/05.webp)


在这里，点击_Open configuration file_（打开配置文件）。进入 `Bitcoin.conf` 文本文件后，只需添加一行 `onlynet=onion` 并保存文件。您需要重启 Bitcoin core 才能使该命令生效。


然后，我们将配置 Tor 服务，使 Bitcoin core 可以通过代理接收传入连接，让网络上的其他节点可以使用我们的节点下载 Blockchain 数据，而不会影响我们机器的安全性。


在终端中输入 `sudo nano /etc/tor/torrc` 访问 Tor 服务配置文件。在该文件中，查找 "#ControlPort 9051 "行，删除 "#"以启用它。现在在文件中添加两行新内容：


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


要在保存文件的同时退出文件，请按 `Ctrl+X > Y > Enter` 键。返回终端，输入命令 `sudo systemctl restart tor` 重启 Tor。


使用此配置后，Bitcoin core 将只能通过 Tor 网络（洋葱）与网络上的其他节点建立进出连接。要确认这一点，请点击_Window_（窗口）选项卡，然后点击_Peers_（同行）。


![Nodes Window](assets/fr/06.webp)


### 其他资源


归根结底，只使用 Tor 网络（`onlynet=onion`）可能会让你容易受到 Sybil Attack 的攻击。这就是为什么有人建议保持多网络配置以降低此类风险。此外，如前所述，一旦配置了 Tor 代理，所有 IPv4/IPv6 连接都将通过 Tor 代理路由。


或者，为了只留在 Tor 网络上并降低 Sybil Attack 的风险，你可以在`Bitcoin.conf`文件中添加`addnode=trusted_address.onion`行，将另一个受信任节点的 Address 添加到文件中。如果要连接多个受信任节点，可以多次添加此行。


要查看 Bitcoin 节点与 Tor 交互相关的日志，请在 `Bitcoin.conf` 文件中添加 `debug=tor`。现在，您的调试日志中就会有相关的 Tor 信息，您可以在_信息_窗口中使用_调试文件_按钮查看这些信息。也可以直接在终端中使用`bitcoind -debug=tor`命令查看这些日志。


**提示💡：** 这里有一些有趣的链接：


- [维基页面解释 Tor 及其与 Bitcoin 的关系](https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core 配置文件生成器，Jameson Lopp 提供](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Jon Atack 的 Tor 配置指南](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


如果您有任何问题，请随时与 Agora256 社区分享。我们一起学习，明天会比今天更好！