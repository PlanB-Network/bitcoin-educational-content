---
name: Raspberry Pi Zero
description: 如何使用 Raspberry Pi Zero 和配件套件构建一个最小化、隔离且低成本的计算机。
---
![cover](assets/cover.webp)



如果您已经在 Plan ₿ Network 页面上浏览了一段时间，那么您已经了解到，最受欢迎的安全设置之一，几乎是必须的，**就是通过离线存储私人密钥来管理资金**。



如果您还没有发现它，您可以在本教程中找到开放源码资源的链接，了解更多相关信息。



要离线管理私钥，就需要一台始终与网络断开的设备，无论是[硬件钱包](https://planb.network/resources/glossary/hardware-wallet)还是专用于此特定功能的隔离计算机。



例如，如果您没有能力购买只执行这项任务的硬件，但又不想放弃这一安全步骤，该如何做呢？



## 解决方案


如果我告诉你，你可以制作一个气隙计算机形式的离线设备，其大小和重量与 USB 闪存盘相当，价格仅为 35 欧元，你会怎么想？你会不相信吗？



继续阅读。



我会告诉你更多：请通读全文。建议的解决方案很便宜，但并不是最简单的。首先，你要了解总体思路，然后决定投入一些时间进行个人研究，并尽可能放心地选择是否继续以及如何继续。



## 要求


**1** 一台 [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/)：PI Zero（没有任何后缀）是构建性能最低计算机的基础，但最重要的是它缺少 Wi-Fi 和 Bluetooth 卡，这是本次练习的必要要求。





- 费用：编写本教程时（2025 年 8 月）约为 15.00 美元。
- 持续生产：覆盆子保证生产到 2030 年 1 月。



遗憾的是，不带 Wi-Fi 和蓝牙功能的 PI Zero 几乎已无法购买。您或许可以更容易地找到 PI Zero W 和 PI Zero 2W 的替代品。在这种情况下，您可以通过更改配置文件来禁用连接功能。安装操作系统后，您需要将这些项目添加到配置文件中：



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



本指南的一部分将告诉你如何操作以及在哪里操作。不过，如果你真的想确保万无一失，你可以在网上找到一些教程，教你如何用小刀（适合在电子板上工作的那种）拆卸 Wi-Fi 芯片。



**2** Raspberry PI Zero 的启动器套件：按照 Raspberry 世界的惯例，它是裸机，没有外部外壳。此外，如此小的电路板资源有限，限制了与外界连接的可能性。



当我决定继续使用时，我发现 [这个套件](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) 配件齐全，可以充分利用 PI Zero 的全部潜力。事实上，该套件包含一个 USB A -> micro USB 电源 Supply、一个小型 USB 集线器、一个 mini-HDMI -> HDMI 适配器、一个铜制散热器和一个铝制外壳。套件中还提供了将 PI Zero 装入新外壳所需的螺丝和内六角扳手。





- 费用：19.99 欧元。



**3** 本教程无需在气隙计算机上花费大量预算。但您应该知道，您需要一个 USB 键盘和鼠标（必须是有线的，避免蓝牙）以及一个显示器。根据显示器的输入，您可能需要一个迷你 HDMI 适配器，这是 PI Zero 上唯一可用的输出。最后，请注意 Hard 的事实，即我们都有一个非无线键盘和鼠标在家里的某个地方--是时候 Dust 关闭它们了。



## 额外预算



**4** 您可以从树莓公司购买原装的 Supply 电源，价格约为 15.00 欧元。



**5** 我个人选择使用启动器套件中提供的电源 Supply，但同时使用了一条 USBA → miniUSB 所谓的 "无数据 "电缆，价格为 3.70 欧元。



**6** 一张微型 SD 卡，至少有 32 GB 的大容量存储空间；如果是工业级质量/级别则更好。



**7** 您需要一个系统，一个 USB 转 micro SD 适配器，就像您在图片中看到的那种。事实上，PI Zero 的操作系统和内存可以在该介质上运行。



![img](assets/it/06.webp)



## 安装操作系统


在将 PI Zero 合上机箱之前，我建议您安装操作系统。这样，您就可以立即检查指示运行的 LED 灯。



为了选择和刻录操作系统，我选择了最简单的方法：使用树莓派的 "PI Imager "工具。



![img](assets/it/01.webp)



前往 [Raspberry 的 Github](https://github.com/raspberrypi/rpi-imager/releases) 下载 Imager 的最新版本，选择最适合您操作系统的版本（撰写时为 v. 1.9.6）。您会注意到，在每个文件旁边还有对应文件的哈希值。这将对验证很有帮助。



![img](assets/it/02.webp)



我建议你验证你将在 airgap 计算机上使用的操作系统，以确保你个人的安全。这将使您确信，您使用的是合法（非恶意）版本的相机，因此也是 Raspi 操作系统。



下载后立即进行验证，并将您通常使用的机器连接到互联网上



然后打开 Linux 终端并准备下载，创建一个用于使用它的 `raspios` 目录。



![img](assets/it/19.webp)



用 `wget` 为你的 Linux 发行版下载相机。



![img](assets/it/20.webp)



最后，运行文件 `sha256sum` 命令，将 Hash 与树莓派在 Github 上提供的 Hash 进行比较。



![img](assets/it/21.webp)



或者，如果您使用的是 Windows，请打开 Power Shell 并键入以下命令：



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



您将获得 Hash，它必须与 Raspberry Github 上发布的版本一致。



验证下载后，即可在日常使用的电脑上安装 Imager 并打开它。Imager 是将操作系统刻录到 micro SD（PI Zero 的 "系统盘"）所需的工具。



过程非常简单：首先选择您要使用的树莓设备（因此请注意您的 Raspi Zero 型号），然后选择操作系统版本，最后选择要闪存操作系统的 micro SD 卡的挂载点。



### 第一步



![img](assets/it/03.webp)



### 第二步



![img](assets/it/07.webp)



**注意**：选择 "PI OS 32 位"，这是唯一能与 PI Zero 兼容的操作系统。



### 第三步



![img](assets/it/08.webp)



(请务必选择 "不包括系统驱动器"，以避免被提示在计算机上安装 Raspi 操作系统）。



一切设置完成后，相机会询问您是否要使用自定义设置。选择你想要的设置，或者点击_No_继续使用默认选项。



![img](assets/it/09.webp)



确认要删除 micro SD 的内容



![img](assets/it/10.webp)



相机开始向微型 SD 闪存操作系统，滚动条会显示进度。



![img](assets/it/11.webp)



最后是自动验证，我建议您不要停止。



![img](assets/it/12.webp)



最后，屏幕上会出现一条信息，如果一切顺利，它就会像图片中显示的那样。



![img](assets/it/13.webp)



现在你可以真正地将micro SD从读卡器中取出，并放入PI Zero的插槽中。打开小型Raspberry并观察LED：我们预期它应为绿色并闪烁，表示操作系统正在正常加载，然后会持续亮起。如果有其他提示，例如LED以固定频率闪烁或呈红色，请查阅FAQ或[支持论坛页面](https://forums.raspberrypi.com/)。



## 首次配置


Raspi OS 的首次启动会比平时慢一些，因为它必须执行一些实际的安装任务。但如果一切顺利，你会看到一个欢迎屏幕。



![img](assets/it/14.webp)



单击 _Next_ 设置地理区域，尤其是加载正确的键盘。请特别注意后者。



![img](assets/it/15.webp)



单击_下一步_，系统将要求您创建用户，记下您的凭据并妥善保管。



![img](assets/it/16.webp)



向导会要求你在 Chromium 和 Firefox 之间选择一个默认网络浏览器；如果你使用的是零 W 或 2W PI，它还会询问你有关 Wi-Fi 网络设置的问题。继续点击_Skip_。



系统会提示你升级板载软件和操作系统。选择_Skip_：在本练习中，我们实际上是在构建一台脱机机器，此时必须保持脱机状态。



最后，它可能会要求你启用 "ssh"，但也请拒绝这一步骤，因为这是一个零空隙 IP。



![img](assets/it/17.webp)



没有更多配置了。完成后，重启树莓派，使更改生效。



![img](assets/it/18.webp)



## 新的计算机气隙


重启后，新的气隙计算机就准备就绪了。PI Zero 会向你显示新的桌面，你可以通过图形用户界面或命令行操作。



![img](assets/it/22.webp)



### 零瓦或 2 瓦 PI 初始步骤


如果您使用的是 Raspberry PI Zero W 或 2W 系列，您的电路板上有 Wi-Fi 和蓝牙芯片。在首次设置时，您跳过了连接配置，因此 PI Zero 无法连接到互联网。现在您可以通过软件永久禁用这两个芯片。



事实上，Raspi OS 提供了一个 `config.txt` 文件，您可以根据自己的喜好进行编辑。config "文件位于 "boot "分区的 "firmware "目录下，你可以用 "root "权限编辑和保存它。



从左上角的图标打开终端，它就变成了 "root"(1)。



![img](assets/it/23.webp)



(1) 如果 Raspi OS 在前面的步骤中没有让您创建 "root "密码，我建议您现在使用 "passwd "命令创建。让 `root` 用户独立于个人用户移动，在恢复情况下会非常方便。



在终端上查看 `config.txt` 文件，并准备使用 `nano` 编辑器对其进行编辑。



![img](assets/it/24.webp)



编辑应在整个 "config "的底部，即"[All]"字样之后进行。此时，您将添加本教程开头所示的 `dtoverlay` 命令。



![img](assets/it/25.webp)



保存、关闭并重新启动。接下来，我们将对小树莓进行探索。



## 对该设备有何期待？


查看 Raspberry 网站上的[技术规格](https://www.raspberrypi.com/products/raspberry-pi-zero/)，PI Zero 配备了单核 BCM2835 处理器和 512 MB 内存，因此性能并不强大。



由于终端比较轻便，我们将使用命令行来探索系统配置。



开机后，你会看到一个简短的彩虹色屏幕，然后是树莓的欢迎信息，左下角是与启动相关的内核信息。



当 PI OS 桌面出现时，打开终端并键入



```bash
uname -a
```


该命令将在屏幕上显示当前使用的内核版本以及其他信息。



![img](assets/it/26.webp)



您还可以通过键入查看 CPU 和硬件的信息：



```bash
lscpu
```



![img](assets/it/27.webp)



另请参阅 `proc/mem/info`。



![img](assets/it/28.webp)



查找 Debian 的版本和发布代号：



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## 使用


虽然 PI Zero 的性能似乎有限（从纸面上以及与当今机器的性能相比），但它的性能很好，尤其是作为终端。





- 首先，你可以进入主菜单，然后从 "添加/删除软件 "面板中获得启发，你会发现这里有许多实用程序可供编程和练习。记住，你也可以从终端进行操作，但一定要有 "root "权限。



![img](assets/it/33.webp)





- 您可以 "领养 "这个离线设备，用于存储各种机密文件，在需要时仍可访问，而不会暴露在互联网上。
- 您可以使用此配置安全地 generate GPG 密钥。
- 你甚至可以将这个新的“小玩具”用作隔离签名设备，[按照 Arman The Parman 的建议操作](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0)。



在我熟悉的钱包中，只有 Electrum 提供 32 位版本。那么：我们在本教程中准备的零 IP 可以让你在离线状态下保留私钥，我们在本教程中介绍了 Wallet airgap 的设置：



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## 结论


这种设置可能有一个很大的弱点：micro SD 是一种可能带来问题的介质。它很容易受到重度使用的影响；也许你已经在手机上使用过它，有这方面的经验。在零 airgap IP 上安装好要使用的所有软件后，使用现有的 Raspi 操作系统工具为珍贵的 micro SD 做好备份。



![img](assets/it/34.webp)



随着需求的增长和预算的增加，您可以探索其他树莓派或类似的解决方案。例如，说到内存，PI 5 可以装配 M2 NVME 驱动器，这肯定比 microSD 更坚固耐用。



别忘了做笔记，并记录下即将离线使用的实用软件安装的每一个步骤。 **迟早会有更新的 Raspi 操作系统问世**，您一定要好好利用。到那时，你将不得不删除所有内容，重新来过（也许会用新的 micro SD 😂）。



我们刚才所做的练习，假设也是您的第一次实验，您一定会记忆犹新。我们不可能总是在离线的情况下将硬件用于 "嵌入式 "操作，而忽略了时不时打开和检查一台空气盖的机器。



不过，你还是成功了，祝贺你！你还可以向所有需要降低预算的人推荐这个解决方案。