---
name: 幽灵 DIY
description: Specter DIY 安装指南
---

![cover](assets/cover.webp)


## 幽灵-DIY


> 赛弗尔朋克写代码。我们知道，必须有人编写软件来保护隐私，而除非我们都这样做，否则就无法获得隐私，所以我们要编写软件。

*Cypherpunk 的宣言 - 埃里克-休斯 - 1993 年 3 月 9 日*。


该项目的构想是利用现成的组件构建硬件 wallet。

尽管我们有一块扩展板，可以将所有部件整合在一个漂亮的外形中，并帮助您避免焊接，但我们仍将继续支持并保持与标准部件的兼容性。


![image](assets/fr/01.webp)


我们还希望保持项目的灵活性，使其只需最小的改动就能在任何其他组件上运行。也许你想在不同的架构（RISC-V？）上制作硬件 wallet，用音频调制解调器作为通信通道--你应该可以做到。添加或更改 Specter 的功能应该很容易，我们会尽可能抽象出逻辑模块。


二维码是 Specter 与主机通信的默认方式。二维码非常方便，用户可以控制数据传输--每个二维码的容量都非常有限，而且通信是单向的。而且，它是空中传输的，任何时候都不需要将 wallet 连接到电脑上。


在秘密存储方面，我们支持不可知模式（wallet 在关闭时会忘记所有秘密）、鲁莽模式（将秘密存储在应用微控制器的闪存中），secure element 集成即将推出。


我们主要关注与其他硬件钱包的多签名设置，但 wallet 也可以作为单签名器使用。我们尽可能使其与 Bitcoin Core 兼容--PSBT 用于无签名交易，wallet 描述符用于导入/导出多签名钱包。为了更方便地与 Bitcoin Core 通信，我们还在开发 [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - 一个与 Bitcoin Core 节点通信的小型 python flask 服务器。


大部分固件都是用 MicroPython 编写的，这使得代码易于审核和更改。我们使用 Bitcoin Core 的 [secp256k1](https://github.com/bitcoin-core/secp256k1) 库进行椭圆曲线计算，并使用 [LittlevGL](https://lvgl.io/) 库进行图形用户界面。


## 免责声明


该项目已经非常成熟，Specter-DIY 的安全级别已经可以与市场上的商业硬件钱包相媲美。我们实施了一个安全引导加载器，可以验证固件升级，因此可以确保只有经过签名的固件才能在初始设置后上传到设备上。不过，与商业签名设备不同的是，引导加载器必须由用户手动安装，而不是在设备供应商的工厂中设置。因此，在初始固件安装时要格外注意，确保验证了 PGP 签名，并在安全的电脑上闪存固件。


如果有问题，请在这里提出，或在我们的 [Telegram 群组](https://t.me/+VEinVSYkW5TUl5Ai) 中提问。


## Specter-DIY 购物清单


在这里，我们将介绍需要购买的产品，在下一部分的组装中，我们将介绍如何组装它，以及有关电路板的一些注意事项--电源跳线、USB 端口等。


### 探索板


设备的主要部分是开发板：



- STM32F469I-DISCO 开发板（例如，可从 [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) 或 [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811) 购买）
- 迷你**USB 电缆
- 通过 USB 进行通信的标准 MicroUSB 电缆


可选但建议使用：


- [Waveshare二维码扫描仪](https://www.waveshare.com/barcode-scanner-module.htm) 带有[这些](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) 或[这些](https://www.amazon.com/gp/product/B015KA0RRU/) 这样的长针头，用于连接扫描仪和电路板（需要 4 个针头）。


我们目前正在开发一种扩展板，其中包括一个智能卡插槽、二维码扫描器、电池和一个 3d 打印外壳，但不包括主要部件--发现板，您需要单独订购。这样一来，供应链攻击仍然不是问题，因为安全关键部件是从电子商店随意购买的。


即使没有任何额外组件，您也可以开始使用 Specter，但只能通过 USB 或内置 SD 卡插槽与它通信。通过 USB 使用 Specter 意味着它无法与空气连接，因此你将失去一项重要的安全性能。


### QR 扫描仪


对于 QR 码扫描器，您有多种选择。


**选项 1.推荐。** Waveshare 提供的扫描仪非常不错（40 美元）


[Waveshare扫描仪](https://www.waveshare.com/barcode-scanner-module.htm) - 你需要想办法把它安装好，也许可以使用某种 Arduino 原型屏蔽和一些鸭嘴胶带。


无需焊接，但如果您具备焊接技能，就能让 wallet 变得更漂亮；)


**方案 2.** Mikroe 公司生产的扫描仪非常不错，但价格相当昂贵（150 美元）：


[条码点击](https://www.mikroe.com/barcode-click) + [适配器](https://www.mikroe.com/arduino-uno-click-shield)


**选项 3.** 任何其他 QR 扫描仪


你可以在中国找到一些便宜的扫描仪。它们的质量通常不是很好，但你可以冒险一试。也许 ESPcamera 也能胜任这项工作。您只需将电源、UART（D0 和 D1 引脚）和触发器连接到 D5。


**选项 4.** 无扫描仪。


这样，您就只能通过 USB 或 SD 卡使用 Specter。


除非你建立自己的通信模块，使用其他东西来代替 QR 码--音频调制解调器、蓝牙或其他任何东西。只要它能被触发并通过串口发送数据，你就可以做任何你想做的事。


### 可选组件


如果再加上一个小巧的电源箱或电池和电源充电器/增压器，您的 wallet 就可以完全自给自足了；)



## 组装 Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### 连接 Waveshare 条形码扫描器


wallet 固件会在第一次运行时为您配置扫描仪，因此无需手动预配置。


下面是将扫描仪连接到电路板的方法：


![image](assets/fr/02.webp)


为了方便起见，您可以购买一个 Arduino Protype 屏蔽板，然后将所有部件焊接并安装在上面（例如 [这个](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347)）。


### 电源管理


在电路板的顶端有一个跳线，用于定义电源的位置。您可以改变跳线的位置，将电源选择为其中一个 USB 端口或 VIN 引脚，并在此处连接外部电池（电压应为 5V）。


### 供 DIY 使用的外壳


查看 [附文](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures) 文件夹。


### 要有创意！


组装自己的 Specter-DIY，并将图片发送给我们（提出拉取请求或联系我们）。


查看 [图库](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md)，其中有社区收集的幽灵！




## 安装已编译的代码


有了安全引导加载器，固件的初始安装略有不同。升级更简单，无需将硬件 wallet 连接到计算机。


![video](https://youtu.be/eF4cgK_L6T4)


### 刷新初始固件


*注意*** 如果你不想使用发行版中的二进制文件，请查看 [bootloader 文档](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md)，其中解释了如何编译和配置它以使用你的公钥而不是我们的公钥。



- 如果您是从 "1.4.0 "以下版本升级或首次上传固件，请使用 [releases](https://github.com/cryptoadvance/specter-diy/releases) 页面上的 "initial_firmware_<version>.bin"。
 - 根据[斯捷潘的 PGP 密钥]验证`sha256.signed.txt`文件的签名(https://stepansnigirev.com/ss-specter-release.asc)
 - 将 `initial_firmware_<version>.bin` 的哈希值与存储在 `sha256.signed.txt` 中的哈希值进行校验
- 如果您是从空引导加载器升级，或看到引导加载器错误信息提示固件无效，请查看下一节--刷新已签名的 Specter 固件。
- 确保发现板的电源跳线位于 STLK 位置
- 通过板顶部的**微型 USB**电缆将探索板连接到电脑。
    - 电路板应显示为名为 "DIS_F469NI "的可移动磁盘。
- 将 `initial_firmware_<version>.bin` 文件复制到 `DIS_F469NI` 文件系统的根目录。
- 闪存固件完成后，电路板将重置并重启至引导加载程序。引导加载程序将检查固件并启动进入主固件。如果看到未找到固件的错误信息，请按照更新说明通过 SD 卡上传固件。
- 现在，您可以随心所欲地切换电源跳线，用电源箱或电池为电路板供电。


通过复制粘贴 ".bin "文件来刷新初始固件有时会失败，通常是因为电缆的原因，或者是通过 USB 集线器连接设备。在这种情况下，您可以多试几次（通常 2-3 次即可成功）。


如果总是失败，可以使用 [stlink](https://github.com/stlink-org/stlink/releases/latest) 开源工具。安装并在终端中键入`st-flash write <path/to/initial_firmare.bin> 0x8000000`。这样通常会更可靠。


### 升级固件



- 从 [releases](https://github.com/cryptoadvance/specter-diy/releases) 下载 `specter_upgrade_<version>.bin`。
- 将此二进制文件复制到 SD 卡根目录（FAT 格式，最大 32 GB）
 - 确保根目录中只有一个 `specter_upgrade***.bin` 文件
- 将 SD 卡插入探索板的 SD 插槽，然后打开探索板电源
- Bootloader 会闪存固件，并在完成后通知您。
- 重新启动电路板 - 此时你将看到 Specter-DIY 界面，它会建议你选择 PIN 码


每当有新版本发布时，只需从版本中下载 `specter_upgrade_<version>.bin`，将其放入 SD 卡，然后像上一步一样升级设备。Bootloader 将确保只有经过签名的固件才能加载到电路板上。


### 如何查找固件版本


进入 "设备设置 "菜单 - 屏幕标题下方会显示版本号。


## 使用 Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Specter-DIY 的安全性


### 硬件


显示屏由应用 MCU 控制。


安全元件集成尚未完成--目前秘密也存储在主 MCU 上。但是，您可以在不存储秘密的情况下使用 wallet，每次都需要输入恢复短语。如果能记住整个口诀，为什么还要记住长长的 passphrase？


设备使用外部闪存存储某些文件（QSPI），但所有用户文件都由 wallet 签名，并在加载时进行检查。


QR 扫描功能由独立的微控制器实现，因此所有图像处理都在安全关键的 MCU 之外进行。目前，USB 和 SD 卡仍由主 MCU 管理，因此如果想减少攻击面，就不要使用 SD 卡和 USB。


### 密码保护（用户身份验证）


首次启动时，主 MCU 会生成一个唯一的密文。输入 PIN 码时，您会看到一系列单词，这些单词在密码存在期间保持不变。


您的 PIN 码和这一独一无二的秘密将用于 generate 密钥的解密（如果您存储了 Bitcoin 密钥）。因此，如果攻击者能绕过 PIN 屏幕，解密仍然会失败。


如果您锁定了固件（TODO：在此添加说明链接），则也将有效锁定秘密，因此如果攻击者向电路板闪入不同的固件，秘密就会被清除，而您在开始输入 PIN 码时就能识别它--单词序列将不同。


### 生成恢复词组


这是 wallet 最重要的部分之一，也是 generate 的关键所在。为了做好这一点，我们使用了多种熵源：



- 微控制器的 TRNG。它是专有的，经过认证，可能很好，但我们不信任它
- 触摸屏。每次触摸屏幕时，我们都会测量触摸发生的位置和时间（以微控制器 180MHz 的嘀嗒频率）。
- 内置麦克风 - 还没有。电路板有两个麦克风，因此硬件 wallet 可以监听您的声音，并将这些数据混入熵池。


所有这些熵都会散列在一起，并转换成您的恢复词组。由此产生的熵总是比任何一个单独的来源都要好。


### 高级逻辑 - 钱包


Specter 是一种密钥存储设备。它保存着可用于钱包的 HD 私钥。钱包由其描述符定义。我们也支持迷你脚本。


每个 wallet 都属于一个特定的网络。这意味着，如果您在 `testnet` 上导入了 wallet，它将无法在 `mainnet` 或 `regtest` 上使用 - 您需要切换到该网络并单独导入 wallet。


### 交易验证


以下规则适用于 wallet 将签署的交易：



- 如果发现来自不同钱包的混合输入，用户会受到警告 ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- 更改输出显示发送到的 wallet 名称
- 要使用多标识符或迷你脚本，首先需要通过添加 wallet 描述符（通过 QR、USB 或 SD 卡）导入 wallet


## 描述符支持


所有正常的 Bitcoin 描述符都能正常工作。除此之外，我们还有一些扩展功能：


### 描述符中的多个分支


为了节省 QR 代码的空间，我们允许一次性添加多个分支的描述符。如果您想将 `wpkh(xpub/0/*)` 用于接收地址，将 `wpkh(xpub/1/*)` 用于更改地址，您可以将它们合并为一个描述符： `wpkh(xpub/{0,1}/*)` - wallet 将把 `{}` 集合部分的第一个索引作为接收地址分支，第二个索引作为更改地址分支。


您还可以指定两个以上的分支，而且不同的联署人可以指定不同的分支索引，因此这种描述符非常奇怪，但完全有效：


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


在此，wallet 将使用 `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))` 中的脚本接收地址 17。


唯一的要求是所有集合中的索引数量相同（上述情况中为 3 个）。


### 默认派生


如果描述符包含主公钥，但不包含通配符派生，则会在描述符中的所有扩展密钥中添加默认派生 `/{0,1}/*`。如果至少有一个 xpub 具有通配符派生，描述符将不会更改。


描述符 `wpkh(xpub)` 将转换为 `wpkh(xpub/{0,1}/*)`。


### 迷你脚本


Specter 支持迷你脚本，但不支持策略到迷你脚本的编译（因为编译成本太高）。我们会对迷你脚本进行一些检查，因此顶层只允许使用 "B "脚本，子迷你脚本中的所有参数都必须具有[spec](http://bitcoin.sipa.be/miniscript/)规定的属性。


您可以使用 [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) 从策略中 generate 一个描述符，然后将其导入 wallet。


例如，"我现在可以消费，或者 100 天后我妻子可以消费 "的政策可以这样转换成 wallet：


政策：或（9@pk(xpubA),and(older(14400),pk(B))）`（我的密钥的可能性高 9 倍）


迷你脚本：`or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor：`wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),alier(14400))))`)


由于这里没有任何通配符派生词，默认派生词 `/{0,1}/*` 将被附加到 xpubs 中。



---

MIT 许可


版权所有 (c) 2019 cryptoadvance


---