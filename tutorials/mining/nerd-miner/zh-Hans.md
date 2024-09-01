---
name: Nerdminer
description: 以接近零的机会开始挖掘比特币
---

![cover](assets/cover.webp)

> 设置您的NerdMiner_v2

在本教程中，我们将指导您完成设置NerdMiner_v2所需的步骤，这是一款专用于比特币挖掘的硬件设备（一个ESP-32 S3）。
显然，这样的设备的计算能力无法与业余或专业矿工的ASICs竞争。尽管如此，NerdMiner是一个完美的教育工具，可以使比特币挖掘变得具体化。而且，谁知道，如果（非常）幸运的话，你可能会找到一个区块和随之而来的奖励。对于好奇的人，我们将在[获胜概率估计](#estimation-de-la-probabilite-de-gain)部分看到。就功耗而言，NerdMiner消耗0.5W；相比之下，一个LED灯平均消耗的功率要多20倍。

在进行不同步骤之前，让我们列出制作它所需的设备：

- 一个[Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- 一个[USB-C电源供应器](https://amzn.eu/d/gIOot90)
- 一个3D外壳：如果您有3D打印机，您可以下载[3D文件](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons)，否则您可以在[Silexperience在线商店](https://silexperience.company.site/NerdMiner_V2-p544379757)购买一个。
- 一台安装了Chrome浏览器的PC
- 一个互联网连接
- 一个比特币地址

您也可以从几个经销商那里购买预组装的NerdMiner套件，例如：

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

首先，我们将看到如何将软件刷新到ESP-32 S3上，然后我们将看到如何重启它以更改wifi网络。这些步骤适用于Windows用户，如果您使用的是Linux操作系统，请执行[Linux用户的初步步骤](#etapes-preliminaires-pour-utilisateurs-linux)以允许您的系统识别ESP-32 S3。

# NerdMiner_v2软件的安装

使用webflasher可以极大简化软件的安装。

## 第1步：准备webflasher

首先，您需要访问[在线NM2 flasher](https://bitmaker-hub.github.io/diyflasher/)。

然后选择与您的ESP-32相对应的固件。大多数情况下它是默认的：T-Display S3。然后点击“Flash”。

> ⚠️ 使用Chrome浏览器非常重要 - 因为它默认允许使用flash并访问您的USB端口。

![](assets/webflasher.webp)

## 第2步：连接ESP-32

一旦启动webflasher，一个弹出窗口将打开，显示浏览器识别的不同USB端口。
然后，您可以连接您的ESP-32，一个新的端口将会显示（在这个例子中，它是ttyACM0端口）。然后您必须选择它并点击“连接”。
![](assets/flasher-port-serial.webp)

软件将在几秒钟内下载到您的ESP32。

![](assets/NM2-sucessfully-installed.webp)

## 第3步：NerdMiner配置

您的NerdMiner配置将通过智能手机或电脑完成。
启用WiFi并连接到本地的NerdMinerAP网络。如果您使用的是智能手机，配置门户将自动打开。否则，在浏览器中输入地址192.168.4.1。
然后选择“配置WiFi”。

现在您可以配置您的NerdMiner。
首先，通过选择您的网络名称并输入关联的密码来连接到您的WiFi网络。

然后，您可以选择您想要参与的挖矿池。实际上，在比特币挖矿行业中，汇集计算力以增加找到区块的机会是常见的，以换取按提供的哈希率比例分享奖励。
对于NerdMiners，您可以选择连接到以下其中一个池：

| 池URL             | 端口  | URL                        | 状态                                     |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | 默认的单独和开源挖矿池                   |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | 由CHMEX维护                              |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | 由djerfy维护                             |

一旦您选择了您的池，您需要输入您的比特币地址，以便在（特殊情况下）找到区块时接收奖励。

同时，选择您的时区，以便NerdMiner可以正确显示时间。
现在您可以点击“保存”。

![](assets/wifi-configuration.webp)

恭喜您，现在您是比特币挖矿网络的一部分了！

## NerdMiner操作

NerdMinerv2软件有3个不同的屏幕，您可以通过点击屏幕右侧顶部的按钮来访问：

- 主屏幕提供访问您的NerdMiner统计信息的入口。
- 第二个屏幕提供访问时间、您的哈希率、比特币价格和区块高度的入口。
- 第三个屏幕提供访问全球比特币挖矿网络统计信息的入口。
  ![](assets/NM2-screens.webp)

如果您想重启您的NerdMiner，例如更改WiFi网络，您需要按顶部按钮5秒钟。

按一次底部按钮将关闭您的NerdMiner。点击两次将旋转屏幕方向。

### Linux用户的初步步骤

以下是Chrome在Linux上检测您的串行端口的步骤。

1. 确定关联的端口：

- 将您的ESP-32连接到您的电脑。
- 打开一个终端。
- 输入以下命令以列出所有端口：
  - `dmesg | grep tty`
  - 或 `ls /dev/tty*`
- 为了确保端口的准确性，您可以通过在ESP-32未连接的情况下重复该命令来进行排除。

2. 更改关联端口的权限：
- 默认情况下，访问串行端口可能需要根权限，因此我们将通过将您的用户添加到`dialout`组来使其可用。- `sudo usermod -a -G dialout YOUR_USERNAME`，将`YOUR_USERNAME`替换为您的用户名。
  - 然后注销并以该用户重新登录，或重启系统以确保组更改生效。

现在您的ESP-32已被您的系统识别，您可以返回到[第一步](#etape-1-preparation-du-webflasher)进行软件安装。

## 结论

就这样！您的NerdMiner_v2现已配置并准备就绪。

祝您挖矿愉快，好运常伴！

### 估算获胜的概率

让我们来估算一下赢得区块奖励的概率吧。这个估算将是粗略的，只旨在获得概率的数量级。
NerdMiner可以连接的矿池只是“独立挖矿池”，这意味着矿池不会共享所有连接矿机的哈希率，而只是充当协调者。
现在，假设我们的NerdMiner的哈希率约为45kH/s。

知道总哈希率约为450 EH/s（或4.5 x 10^20哈希每秒），我们可以认为找到下一个区块的概率是1在100万亿中，这是非常非常非常不可能发生的。所以，除了作为一个教育工具和好奇心对象，NerdMiner还可以在电力成本边际为0.5W的情况下，作为比特币挖矿的彩票——尽管我们刚刚看到获胜的概率极低。然而，为什么不挑战一下你的运气呢？

### 额外信息

如果您想进一步了解该主题，这里有一些链接：

- [NerdMiner_v2项目页面](http://github.com/BitMaker-hub/NerdMiner_v2)
- [NerdMiners的完整文档](https://docs.bitwater.ch/nerd-miner-v2/)