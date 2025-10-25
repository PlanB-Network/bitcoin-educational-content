---
name: COLDCARD Q - Key Teleport
description: 什么是密钥传送，如何使用？
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Coinkite 旗舰产品 ColdCardQ 设备的**键远程传输**功能是什么？



**Key Teleport** 可让您在两台 ColdCardQ 之间安全地传输机密数据。传输通道甚至不需要加密，而且可以是公开的。



这可用于转账：





- gW-0 短语**（ColdCard Q 的 seed 主控器或 ColdCardQ 的 [seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault) 中存储的秘密）**。
- 机密笔记和密码：可以是任何秘密，也可以是 ColdCardQ 上的整个 **Secure Notes & Passwords** 目录 (https://coldcard.com/docs/secure_notes/)。
- 备份整个 **ColdCardQ**：接收该备份的 ColdCardQ 必须没有 seed Master 才能工作。
- gW-3（**部分签名的 Bitcoin 交易**），作为多重签名方案的一部分。



这要求您将 [设备固件升级到版本 v1.3.2Q](https://coldcard.com/docs/upgrade/) 或更高版本。



## 如何使用钥匙传送？



### 1- 传输任何类型的数据



在此，我们将讨论 seed 句子、笔记、密码或 ColdCardQ 备份的整体传输。多签名交易的 PSBT 传输情况将在后面讨论。



#### 准备接收机密的设备



在 ColdCardQ 的**"高级/工具**"菜单中，选择**"按键传送（开始）"**。


在下一个屏幕上，会提示一个 8 位数的密码，这里是 "20420219"。您需要将此密码告知发件人。例如，使用短信发送该密码，或使用您最喜欢的安全邮件系统，甚至是语音电话。



然后点击 ColdCardQ 上的**"Enter**"按钮进入下一步。




![CCQ-key-teleport](assets/fr/01.webp)




屏幕上会生成一个 QR 码。同样，您需要把这个 QR 码传送给 ColdCardQ 的 "发送者"。最简单的方法是通过视频通话。



**请勿通过发送前一个 8 位密码的相同传输通道发送此 QR 码**。



![CCQ-key-teleport](assets/fr/02.webp)



*有兴趣的朋友，让我们试着了解一下允许秘密通过不安全渠道传输的基本机制*。



*实际上，我们在这里做的是通过 Diffie-Hellman 方法启动秘密传输，我在下面附上的 BTC204 课程中已经介绍了这一方法*。



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*我们目前有：*




- 生成了一对短暂密钥（公/私密钥分别为 Ka 和 ka，Ka=G.ka，G 为 ECDH 生成点）和一个 8 位数密码。
- 使用该密码通过 AES-256-CTR 加密公钥 (Ka)，然后通过通信通道 A 将该密码传输给 **发送** ColdCardQ。
- 最后，我们通过上面的二维码，使用不同于第一个通信信道 B 的第二个通信信道，将加密后的数据包传送给发送者。



#### 准备发送机密的设备



在发送设备上点击 **"QR "**按钮，扫描接收设备发送给您的 QR 码，然后通过单独通道输入上一步中告知您的 8 位数密码。现在我们可以开始从 "发送 "设备发送数据了。



**请不要输入错误的 8 位数密码，因为不会显示错误信息，程序将继续进行。但是，最后的数据传输将失败，您必须重新开始**。



![CCQ-key-teleport](assets/fr/03.webp)



**对于好奇心较强的人来说，让我们再来看看我们在密码学和秘密传输方面的研究成果：**




- 我们通过扫描接收设备上的 QR 码导入加密数据。
- 然后，我们使用通过二级渠道*传送给我们的 8 位数密码对其进行解密。
- 因此，我们掌握了接收者最初生成的公钥（Ka）。
- 然后，我们在发送设备上 generate 一个新的短暂密钥对（Kb/kb，Kb=G.kb），用来对 Ka 应用 ECDH。因此，我们执行 kb.Ka=Ks 操作，其中 Ks 称为 **"会话密钥 "**。




现在请您选择要在两个 ColdCardQ 之间传输的机密的性质（机密笔记、密码、完整备份、存储库中的种子、seed 设备主控）。



![CCQ-key-teleport](assets/fr/04.webp)



在这里，我们的秘诀是选择 **"快速短信 "**，发送一条短信息。输入您的信息（对我们来说是 "PlanB Network rocks"），然后按**"回车键 "**。


然后，设备会生成一个新的随机密码，称为**"Teleport Password "**，例如 "NE XG BT SK"。



![CCQ-key-teleport](assets/fr/05.webp)



按下 **"ENTER "**，您将看到一个新的 QR 码。请接收设备扫描该二维码。然后在另一个通信频道上，向接收设备发送**"传送密码 "**。



![CCQ-key-teleport](assets/fr/06.webp)



*在此，我们再次向好奇者介绍这一阶段的情况：*




- 在选择要传送的秘密后，我们 generate 一个新的随机密码，名为 **"传送密码"**。
- 然后，我们使用上一步生成的**"会话密钥 "**，即 "Ks"，通过 AES-256-CTR 对秘密进行加密。
- 我们用 Kb 公钥对已用**"会话密钥 "**加密的数据包进行前缀，然后再用**"远程口令 "**对数据包进行 Layer AES-256-CTR 加密。然后，整个过程被编码为 QR 码




#### 完成向接收设备的机密传输



按下 **"QR "**按钮，扫描发送设备通过 visio 频道显示的 QR 码。系统会要求您输入 "NE XG BT SK "的**"远程口令 "**。



![CCQ-key-teleport](assets/fr/07.webp)





然后对数据进行解密，使接收设备能够理解这些数据。接收到的信息确实是 "PlanB Network rocks"。仅此而已。



![CCQ-key-teleport](assets/fr/08.webp)



**最后阶段究竟发生了什么？**




- 我们已经使用**"远程传送密码 "**解密了发送者传输的数据。
- 因此，我们就有了公开密钥 Kb 和由**"会话密钥 "**"Ks "加密的密文。但是，作为接收方，我们不知道发送方创建的 Ks，又该如何做到这一点呢？
- 我们需要将初始步骤**"准备接收数据的设备"**中的私钥"ka"应用到公钥**Kb**中。
- 事实上，通过计算 ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks 我们就能找到 Ks。最后用它来破译密文。



### 2- 将 PSBT 移至 Multisig（高级）



前提是您的 Wallet Multisig 已经创建，并且您的 ColdCardQ 设备已经预设为可以执行多重签名交易。如果不是这种情况，可在 Coinkite 网站 [此处](https://coldcard.com/docs/Multisig/) 上查阅相关解释。



简单提醒一下什么是多重签名 Wallet（Multisig）。



通常，要使用 Wallet 资金，只需要一个私人密钥就能解锁与地址相关的 UTXO。


在 Wallet Multisig 的情况下，可能需要多达 15 个私人密钥和 15 个签名才能使用资金。这就是所谓的 "M out of N "组合，其中 N 介于 1 到 15 之间，而 M 则是可使用资金所需的签名数。例如，Wallet Multisig 3 出 5 将需要 5 个签名中至少 3 个签名。



然后，挑战在于协调签署者之间的关系，依次为 "Partially Signed Bitcoin Transaction "签署 "PSBT"。在这种情况下，可以使用 "**密钥远程传输**"在共同签署人之间以简单、保密的方式传输 PSBT。共同签署人之间只需进行简单的视频通话即可。



下面是 Multisig 3 of 4 的操作方法。



**签署人 1：**



签字人 1 导入并签署 PSBT。最后，他点击**"T "**，使用**"密钥传送 "**将 PSBT 发送给签名人 2。



![CCQ-key-teleport](assets/fr/09.webp)




点击**"ENTER"**选择签字人 2 后，将提供一个 "电话端口口令"（此处为 JJ YC AB 6A），该口令必须通过其他通信渠道传送给签字人 2。例如，短信或语音电话，但**不是视频电话**。



再次按下 **"ENTER "**，出现一个代表 PSBT 的 QR 码，该 QR 码由 1 签名，然后由 "TELEPORT PASSWORD "加密。



![CCQ-key-teleport](assets/fr/10.webp)



**签署人 2：**



签字人 2 扫描签字人 1 向其出示的二维码。然后输入通过二级通信信道传输的 "TELEPORT 密码"，对传输的数据进行解密。



签字人 2 签署交易，然后点击 **"T "**，通过 "密钥远程传输 "将 PSBT 传输给签字人 3。


显然，已经有 2 个签名了。现在只差第 3 个签名人的签名，交易就可以生效了。点击 **"ENTER "**，选择签名人 3。



![CCQ-key-teleport](assets/fr/11.webp)



然后创建一个新的 "TELEPORT 密码"，接着再创建一个 QR 码，对 1 和 2 签名的 PSBT 进行编码，然后用这个新的 "TELEPORT 密码"（GW YQ K3 LL）进行加密。



![CCQ-key-teleport](assets/fr/12.webp)



**签署人3：**



重复上述步骤。


签字人 3 扫描签字人 2 向其出示的二维码。然后输入通过二级通信通道传输的 "电话端口口令"。



签名人 3 签署交易，此时，由于 4 个签名中的 3 个已经完成，交易被视为最终完成，可以通过各种媒介（SD 卡、NFC、QR 等）进行分发。



![CCQ-key-teleport](assets/fr/13.webp)



如果激活了 ColdCardQ 的 "Push Tx "功能，只需将 ColdCardQ 贴在任何 NFC 互联网连接设备（智能手机/平板电脑）的背面，即可通过 Bitcoin 网络广播交易。



![CCQ-key-teleport](assets/fr/14.webp)



*对于 PSBT 从一个签名者到另一个签名者的传输，只需在每个阶段通过 "远程口令 "使用 "密钥远程传输"，即可在 PSBT 从一个签名者传输到另一个签名者时对其进行加密。由于传输的数据不会被用于窃取资金，因此不需要像发送高度机密（seed、密码等......）时那样使用 Diffie-Hellman* 。



![CCQ-key-teleport](assets/fr/15.webp)



*来源：[ColdCard 官方网站]()[冷卡官方网站](https://coldcard.com/)*