---
name: 姜 Wallet
description: 开源、自我保管的 Bitcoin Wallet 软件，来自 Wasabi Wallet 的 Fork，整合 Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet 是一个开放源代码、非托管 Bitcoin 组合，侧重于保密和隐私。它的前身是来自 Wasabi Wallet 的 Fork（2.0.7.2 版之后 - MIT 许可）。



Ginger Wallet 保留了 Wasabi 的技术架构，同时增加了一些特定功能。根据 [Ginger Wallet 文档](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet)，Wasabi 强调**自主性和控制**，而 Ginger 则注重**易用性、安全性和简化体验**，使那些对技术方面不太熟悉的人也能使用。



Ginger Wallet 是仅供电脑使用的 Wallet 软件（无移动应用程序）。



## 什么是 CoinJoin？



CoinJoin** 是一种特殊的 Bitcoin 交易结构，它将多个参与者集中在一个单一的合作交易中。这种机制将不同用户的条目混合到一个共同的交易中，使得追踪资金变得极其困难--如果操作得当，甚至往往是不可能的。因此，与传统的 Bitcoin 交易不同，外部观察者几乎不可能确定所涉比特币的来源和去向。



对用户而言，CoinJoin 有助于为您保密。例如，如果您在 Bitcoin Address 上收到 10,000 Sats 的捐款，发件人可以追踪这些资金，并在某些情况下推断出您持有更多比特币，或观察您的活动。如果您在捐赠 10,000 Sats 之后再进行一次 CoinJoin，您就打破了这种可追溯性：发件人将无法再从这次付款中获得任何关于您的信息。



Chaumian CoinJoin 提供高度的安全性，因为资金始终由用户独家控制。即使是协调服务器的操作员也无法在任何情况下转移参与者的比特币。用户和协调者都不需要相互信任：每个人都保留对自己私钥的控制权，并且只有权验证交易。因此，任何第三方都无法在 CoinJoin 期间侵占你的比特币，也无法在你的输入和输出之间建立直接联系。



要了解有关 CoinJoin 的更多信息，请查看 Plan ₿ Academy 的 BTC 204 课程 ：



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 安装 Ginger Wallet



要安装 Ginger Wallet，请访问网站 [Ginger Wallet](https://gingerwallet.io)。



按**下载**，下载适合您电脑的版本（Windows/MacOs/Linux）。



![screen](assets/fr/03.webp)



另一种方法是到项目的 [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) 下载。



![screen](assets/fr/04.webp)



然后运行安装程序。



![screen](assets/fr/05.webp)




## 参数设置



### 初步配置



打开 Ginger Wallet，选择您喜欢的语言。



![screen](assets/fr/06.webp)



从一开始，Ginger 就会提醒你 CoinJoin 过程中涉及的成本。



![screen](assets/fr/07.webp)



然后按**开始**，再按**新**创建一个新的投资组合。



![screen](assets/fr/08.webp)



然后，保存并确认您的 seedphrase。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



为了提高安全性，Ginger Wallet 还提供了加装 passphrase 的选项。



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

该 passphrase 添加后，您每次尝试访问您的投资组合时都会被请求。



![screen](assets/fr/12.webp)



创建投资组合时，Ginger 会自动激活默认的 **CoinJoin**。您会被告知这一点，然后可以根据自己的需要自定义设置。



![screen](assets/fr/13.webp)




### 常规设置



创建第一个作品集后，您将进入 Ginger 的 Interface Wallet。



![screen](assets/fr/14.webp)



如果想隐藏钱包中的余额，请激活**保密模式**。



![screen](assets/fr/15.webp)



您可以在 Ginger Wallet 上创建多个作品集。只需点击**添加作品集**即可。



![screen](assets/fr/16.webp)



Ginger 支持通过 Bitcoin core 标准 Interface 使用硬件组合，但目前还不能从硬件组合直接集成或集成到硬件组合。



兼容的硬件组合包括（但不限于）：




- BLOCKSTREAM 翡翠
- 冷卡 MK4
- 冷卡 Q
- Ledger 纳米 S Plus
- Ledger 纳米 X
- Trezor T 型
- Trezor Safe 3
- 等等



现在点击**设置**。



![screen](assets/fr/17.webp)



这些设置是一般应用程序的设置，您在这里进行的配置将适用于所有投资组合。



在**设置**中，有以下选项卡 ：





- 一般**



![screen](assets/fr/18.webp)





- 外观



在该选项卡中，您可以更改语言、货币和费用显示单位（BTC/Satoshi）等。



![screen](assets/fr/19.webp)





- Bitcoin**



通过该选项卡，您可以启用 Bitcoin Knots，使其在应用程序启动时运行，选择网络（Main/RegTest）和费率提供商（Mempool Space/BLOCKSTREAM info/Full node）等。



![screen](assets/fr/20.webp)





- 安全功能**



在 "安全 "选项卡中，你可以启用双因素身份验证，激活或停用 Tor，甚至在关闭 Ginger 应用程序后禁用 Tor。



![screen](assets/fr/21.webp)



**NB** ：




- 对于双因素身份验证，请确保您的身份验证应用程序支持 SHA256 协议和 8 位代码。Ginger Wallet 要求使用 8 位数的 2FA 代码来增强安全性。这种较长的格式使代码更难被猜测或破解，从而为防止未经授权的访问提供了更大的保护。
- 默认情况下，所有 Ginger 网络流量都会通过 Tor 传输，无需手动配置。如果 Tor 已在系统中激活，Ginger 会自动给予其优先权。



但是，一旦在设置中停用 Tor，除了两种情况外，你的隐私一般都会得到保护：




- 在使用 CoinJoin 时，协调器可将您的输入和输出连接到 IP Address；
- 在广播交易时，您所连接的恶意节点可能会将您的交易与您的 IP 关联起来。



不要忘记每次都按**完成**（在 Coin 的右下方）来保存设置。有些设置需要重新启动 Ginger Wallet 才能生效。



此外，通过投资组合顶部的搜索栏，您还可以搜索和访问任何参数等。



![screen](assets/fr/22.webp)




### 投资组合配置



应用程序中可以创建多个作品集，因此每个作品集都可以根据您的需要进行配置。为此，请点击组合名称前的**三点**，然后点击**组合设置**。



![screen](assets/fr/23.webp)



如您所见，除了 Wallet 参数外，您还可以看到您的 UTXOs（您拥有的代币列表）、统计数据和 Wallet 信息（例如扩展公钥）。



点击 "投资组合参数 "后，将返回投资组合配置，进入以下选项卡：




- 常规** （可在此更改投资组合名称） ；



![screen](assets/fr/24.webp)





- CoinJoin**（您可在此自定义此投资组合的 CoinJoin 设置） ；



![screen](assets/fr/25.webp)





- 工具**（在这里您可以检查您的 seedphrase、再次同步您的投资组合或删除它）。



![screen](assets/fr/26.webp)




## 接收比特币



在 Ginger Wallet 上接收比特币：




- 按**接收** ；



![screen](assets/fr/27.webp)





- 输入您希望关联 Address 的来源名称。这是用于跟踪付款的标签。这对 On-Chain 没有任何影响；它只是存储在您应用程序本地的可追溯性信息；



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- 点击**generate**左侧的小箭头，选择您的 Address 格式（**SegWit** /**Taproot**），然后点击**generate**，转到 generate 和 Address 以及二维码。



![screen](assets/fr/29.webp)



发件人将使用这个 Address 或 QR 码向您发送比特币。



![screen](assets/fr/30.webp)




## 发送比特币



如何通过 Ginger Wallet 发送信息的视频教程。



![Vidéo](https://youtu.be/2nf5aAimfhg)



为此：




- 按**发送**按钮；
- 输入收件人的 Address、要发送的金额和标签；
- 查看交易概览并确认发送。



![screen](assets/fr/31.webp)




## 消费比特币



用 Ginger Wallet 买卖 Bitcoin 非常简单。只需几步，您就可以花掉您的比特币。



### 购买比特币



Ginger Wallet 用户可以购买比特币。





- 按下**购买**按钮。即使 Wallet 是空的，该按钮仍可见。



![screen](assets/fr/32.webp)





- 在购买 Bitcoin 之前，请选择您所在的国家，甚至您所在的州（在某些地区，如加拿大）。事实上，当您第一次点击**购买**功能时，您还需要指定您所在的地区。



![screen](assets/fr/33.webp)



按**继续**进入购买流程。





- 然后在专用字段中输入您要购买的比特币数量。您还可以选择交易货币。



![screen](assets/fr/34.webp)



每种货币都有最低和最高购买限额。例如，美元的最高限额为 30,000 美元。



如果您已经进行了购物，您可以点击**以前的订单**按钮查看您的交易历史。将显示过去的交易列表及其状态。





- 选择适合您的优惠。



此时，您将看到所有可用优惠的列表。对于每项优惠，您都可以.....：




 - 供应商名称 (1) ；
 - 与之前输入的金额相当的比特币数量、支付方式和购买费用 (2) ；
 - 接受**按钮 (3)。



![screen](assets/fr/35.webp)



报价中注明的费用不构成额外费用。这些费用已包含在报价总额中。



屏幕右上方 Coin 的**All**标签允许您按付款方式过滤报价。您选择的付款方式将被默认设置，但可以随时更改。



![screen](assets/fr/36.webp)



如果找到合适的报价，请点击**接受**按钮继续购买。然后，您将被转到卖方页面，在那里您可以完成交易。



### 出售比特币



Ginger Wallet 用户可以出售 Bitcoin。只有在投资组合中有可用资金时，才能看到**出售**按钮。





- 点击**出售**。



![screen](assets/fr/37.webp)





- 与**购买**选项一样，首次使用销售功能时，必须先选择国家，然后才能进行 Bitcoin 销售。





- 接下来，您需要输入您希望出售的比特币数量。您可以输入 BTC 或美元等法定货币。





- 完成此操作后，您将看到可用优惠列表。选择适合您的销售优惠，然后点击**接受**继续。





- 现在，您需要完成交易：
 - 接受报价后，您将跳转到供应商页面；
 - 请按照供应商页面上的说明操作；
 - 届时，您将收到收件人 Address 和准确的汇款金额；
 - 然后返回 Ginger Wallet 继续这一过程；
 - 回到 Ginger Wallet 后，会出现一个对话框，您可以点击**发送**继续。



这将打开**发送**屏幕，并预填收件人的 Address 和金额。您也可以使用主屏幕上的**发送**按钮。虽然您可以手动发送交易，但我们建议您通过对话框完成交易，以优化流程。



## 在 Ginger Wallet 上制作 CoinJoin



![Vidéo](https://youtu.be/AJe67RDfB1A)



使用直接集成到 Ginger Wallet 中的**CoinJoin**来保护比特币的机密性。Wallet 使用**WABISABI**，这是一个 Chaumian CoinJoin 协议，旨在促进更方便、更高效的接币。



您可以选择最适合自己的 CoinJoin 策略（自动或手动）。



下载 Ginger CoinJoin 后即可使用（无需其他步骤）。Ginger CoinJoin 会自动在后台运行，以保护您每笔交易的隐私。实际上，只要您有可以匿名的余额，CoinJoin 阅读器就会出现。



至于手动启动 CoinJoin，只需一键操作。启动一轮，等待 CoinJoin 交易建立和确认。您将在 Interface 中看到匿名化分数。



可以进行多次混合，直到达到所需的匿名程度。您还可以从混音中排除某些部分。



默认情况下，Ginger 使用自己的协调器，并预设了所有参数和保证费用。价值超过 0.03 BTC 的代币合并，除 Mining 费用外，还需支付 0.3% 的协调人费用。0.03 BTC 或以下的入币以及混币，即使是单笔交易，也免收协调人费用。因此，使用 CoinJoin 资金付款时，发送方和接收方都可以重新混合他们的币，而无需支付协调人费用。



与规模较小、速度较快的回合相比，Ginger 更喜欢参与者较多的硬币接合。规模更大的硬币接合提供了更多的匿名性、更低的成本和更高的 BLOCK 空间效率。




## 安全和最佳做法



为了实现权力下放和保护隐私，需要采用几种最佳做法：




- 请务必将 seedphrase 存放在离线的安全位置；
- 如果您丢失了电脑或怀疑有人未经授权访问您的电脑，请立即创建一个新的 Wallet。将您的资金转入新的投资组合，并删除旧的投资组合；
- 每次接收都使用不同的 Address，以避免重复使用地址；
- 请务必只从官方 GitHub 账户或官方网站下载作品集应用程序。



现在你已经熟悉使用 Ginger Wallet 应用程序发送、接收和消费比特币了。



如果您觉得本教程有用，请在下方给我留下 Green 大拇指。请随时通过您的社交媒体平台分享本文。非常感谢



我还建议你看看这个教程，了解如何使用 Liana 计算机应用程序发送和接收比特币，以及如何实施自动遗产计划。



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04