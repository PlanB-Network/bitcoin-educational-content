---
name: Bitcoin Core节点（Linux）
description: 使用Bitcoin Core运行您自己的节点
---

![封面](assets/cover.webp)

# 使用Bitcoin Core运行您自己的节点

介绍比特币和节点的概念，补充了在Linux上安装的全面指南。

比特币最令人兴奋的提议之一是能够自己运行程序，从而在网络和公共交易账本的验证中以细粒度参与。

比特币是一个开源项目，自2009年以来一直免费公开分发。在其诞生近15年后，比特币现已成为一个强大且不可阻挡的数字货币网络，受益于强大的有机网络效应。对于他们的努力和远见，中本聪值得我们的感激。顺便说一下，我们在Agora 256上托管了比特币白皮书（注：也在大学上）。

## 成为您自己的银行

对于坚持比特币公理的人来说，运行自己的节点已变得至关重要。无需请求任何人的许可，就可以从一开始下载区块链，从而根据比特币协议验证从A到Z的所有交易。

该程序还包括自己的钱包。因此，我们可以控制我们发送到网络其余部分的交易，无需任何中介或第三方。你就是你自己的银行。

因此，本文的其余部分是一个安装指南，专门介绍在Debian兼容的Linux发行版上安装Bitcoin Core——最广泛使用的比特币软件版本，例如Ubuntu和Pop!/\_OS。遵循本指南，向您的个人主权迈进一步。

## Debian/Ubuntu上的Bitcoin Core安装指南

> 先决条件
>
> - 最小6GB的数据存储（修剪节点）— 1TB的数据存储（完整节点）
> - 允许至少24小时完成初始区块下载（IBD）。即使对于修剪节点，这个操作也是必须的。
> - 即使对于修剪节点，也允许~600GB的带宽用于IBD。

> 💡 以下命令是为Bitcoin Core版本24.1预定义的。

## 下载和验证文件

1. 下载bitcoin-24.1-x86_64-linux-gnu.tar.gz，以及SHA256SUMS和SHA256SUMS.asc文件。（https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz）

2. 在下载文件所在的目录中打开一个终端。例如，cd ~/Downloads/。
3. 使用命令sha256sum --ignore-missing --check SHA256SUMS验证版本文件的校验和是否列在校验和文件中。
4. 此命令的输出应包括下载的版本文件的名称，后跟“OK”。示例：bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK。

5. 使用命令sudo install git安装git。然后，使用命令git clone https://github.com/bitcoin-core/guix.sigs克隆包含Bitcoin Core签名者PGP密钥的存储库。
6. 使用命令gpg --import guix.sigs/builder-keys/\*导入所有签名者的PGP密钥。
7. 使用命令gpg --verify SHA256SUMS.asc验证校验和文件是否已使用签名者的PGP密钥签名。
每个签名都会返回一行以：“gpg: Good signature”开头，另一行以“Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320”（Pieter Wuille的PGP密钥指纹示例）结尾。
> 💡 并非所有签名者的密钥都需要返回“OK”。实际上，可能只需要一个。由用户确定他们自己对PGP验证的验证阈值。
>
> 可以忽略警告消息：WARNING: This key is not certified with a trusted signature!

> 没有迹象表明该签名属于所有者。

## 安装比特币核心图形界面

1. 在终端中，仍在位于比特币核心版本文件的目录中，使用命令 tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz 来提取存档中包含的文件。

2. 使用命令 sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\* 安装之前提取的文件。

3. 使用命令 sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev 安装必要的依赖项。

4. 使用命令 bitcoin-qt 启动 bitcoin-qt（比特币核心图形界面）。

5. 要选择一个裁剪节点，请勾选限制区块链存储并配置要存储的数据限制：

![welcome](assets/1.webp)

## 第一部分结论：安装指南

一旦安装了比特币核心，建议尽可能保持运行，以通过验证交易和向其他节点传输新区块来为比特币网络做出贡献。

然而，即使只是为了验证收到和发送的交易，间歇性地运行和同步你的节点仍然是一个好习惯。

![Creation wallet](assets/2.webp)

# 为比特币核心节点配置Tor

> 💡 本指南适用于Ubuntu/Debian兼容的Linux发行版上的比特币核心24.0.1。

## 为比特币核心安装和配置Tor

首先，我们需要安装Tor服务（The Onion Router），一个用于匿名通信的网络，它将允许我们匿名化我们与比特币网络的互动。关于在线隐私保护工具的介绍，包括Tor，请参考我们关于此主题的文章。

要安装Tor，打开终端并输入 sudo apt -y install tor。安装完成后，服务通常会自动在后台启动。使用命令 sudo systemctl status tor 检查它是否正确运行。响应应显示 Active: active (exited)。按Ctrl+C退出此功能。

> 无论如何，你可以在终端使用以下命令来启动、停止或重启Tor：

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

接下来，让我们用命令 bitcoin-qt 启动比特币核心图形界面。然后，启用软件的自动功能，通过Tor代理路由我们的连接：Settings > Network，从那里我们可以勾选 Connect through SOCKS5 proxy (default proxy) 以及 Use a separate SOCKS5 proxy to reach peers via Tor onion services。

![option](assets/3.webp)

比特币核心会自动检测是否安装了Tor，如果是，将默认创建到其他也使用Tor的节点的出站连接，除了到使用IPv4/IPv6网络（明网）的节点的连接。
💡 要将显示语言更改为法语，请转到设置中的显示选项卡。
## 高级Tor配置（可选）

可以配置比特币核心（Bitcoin Core），使其仅通过Tor网络与节点连接，从而通过我们的节点优化我们的匿名性。由于图形界面中没有此功能的内置功能，我们需要手动创建一个配置文件。转到设置，然后选择选项。

![option 2](assets/4.webp)

在这里，点击打开配置文件。一旦进入bitcoin.conf文本文件，简单地添加一行onlynet=onion并保存文件。你需要重启比特币核心使此命令生效。
然后，我们将配置Tor服务，以便比特币核心可以通过代理接收传入连接，允许网络上的其他节点使用我们的节点下载区块链数据，而不会危及我们机器的安全。

在终端中，输入sudo nano /etc/tor/torrc以访问Tor服务配置文件。在此文件中，查找行#ControlPort 9051并删除#以启用它。现在在文件中添加两行新内容：HiddenServiceDir /var/lib/tor/bitcoin-service/ 和 HiddenServicePort 8333 127.0.0.1:8334。要在保存文件的同时退出文件，请按Ctrl+X > Y > Enter。回到终端，通过输入命令sudo systemctl restart tor重启Tor。

通过这种配置，比特币核心将能够仅通过Tor网络（Onion）与网络上的其他节点建立传入和传出连接。要确认这一点，请点击窗口选项卡，然后选择节点。

![Nodes Window](assets/5.webp)

## 额外资源

最终，仅使用Tor网络（onlynet=onion）可能会使您容易受到Sybil攻击。这就是为什么一些人推荐维持多网络配置以减轻这种类型风险的原因。此外，一旦配置了Tor代理，所有IPv4/IPv6连接都将通过Tor代理路由，如前所述。

另外，为了仅停留在Tor网络上并减轻Sybil攻击的风险，您可以通过添加行addnode=trusted_address.onion到您的bitcoin.conf文件中，添加另一个受信任节点的地址。如果您想连接到多个受信任的节点，可以多次添加此行。

要查看与Tor交互的您的比特币节点的特定日志，请在您的bitcoin.conf文件中添加debug=tor。现在，您将在调试日志中拥有相关的Tor信息，您可以在信息窗口中使用调试文件按钮查看这些日志。也可以直接在终端中使用命令bitcoind -debug=tor查看这些日志。

> 💡 一些有趣的链接：
>
> - 解释Tor及其与比特币关系的Wiki页面
> - 由Jameson Lopp提供的比特币核心配置文件生成器
> - 由Jon Atack提供的Tor配置指南

一如既往，如果您有任何问题，随时在Agora256社区分享。我们一起学习，为的是明天比今天更好！