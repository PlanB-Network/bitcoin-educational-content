---
name: COLDCARD Q - Key Teleport
description: 何为 Key Teleport 且如何使用它？
---

> **⚠️ 紧急安全公告（2026年7月）— Coldcard 钱包正在被持续盗取。** Coldcard 设备种子生成过程中的一个固件漏洞，使攻击者无需你进行任何操作即可找出你的种子短语。**所有 Coldcard 型号均受影响：Mk3、Mk4、Mk5 和 Q。** 2026年7月30日，约 500 个钱包中被盗走大约 594 BTC，且攻击仍在持续。只有使用掷骰子方法生成的钱包才被认为是安全的，并且前提是你至少掷了 50 次骰子。如果你不知道、不记得或不确定你的种子是如何生成的，请将其视为已泄露，并**立即将资金转移**到种子并非在 Coldcard 上生成的钱包。请关注 Coinkite 的官方公告。请参阅我们的专门迁移教程：

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Coinkite 在其旗舰产品 ColdCardQ 设备中提供的 **Key Teleport（密钥传送）** 功能是什么？


**Key Teleport** 可让您在两台 ColdCardQ 之间安全地传输机密数据。传输通道甚至不需要加密，而且可以是公开的。



这可用于转账：





- **gW-0 短语**（ColdCard Q 的种子主密主控器或[存储在 ColdCardQ 种子库中的密钥](https://coldcard.com/docs/temporary-seeds/#seed-vault) 中存储的秘密）**。
- **机密笔记和密码**：可任何密钥或 ColdCardQ 上的整个 **Secure Notes & Passwords** 目录 (https://coldcard.com/docs/secure_notes/)。
- **整个 ColdCardQ 的备份**：接收该备份的 ColdCardQ 必须没有主种子才能工作。
- gW-3（**PSBT（部分签名的比特币交易）**），作为多重签名方案的一部分。



这要求您将 [设备固件升级到版本 v1.3.2Q](https://coldcard.com/docs/upgrade/) 或更高版本。



## 如何使用密钥传送？



### 1- 传输任何类型的数据


在此，我们将介绍如何传输种子助记词、笔记、密码，或整个 ColdCardQ 备份。多重签名交易的 PSBT 传输将在稍后讨论。



#### 准备接收密钥的设备



在 ColdCardQ 的 **"Advanced / Tools**" 选单中，选择 **"Key Teleport (start)"**。


在下一个屏幕上，系统会提供一个 8 位数的密码，此处为“20420219”。您需要将此密码告知发送方。例如，您可以使用短信、您常用的安全消息系统，甚至语音通话来发送此密码。


然后点击 ColdCardQ 上的 “**Enter**” 按钮，进入下一步




![CCQ-key-teleport](assets/fr/01.webp)




屏幕上会出现二维码。同样，您需要把这个二维码传送给 ColdCardQ 的 "发送者"。最简单的方法是通过视频通话发送。



**请勿通过发送前一个 8 位密码的相同传输通道发送此二维码**。



![CCQ-key-teleport](assets/fr/02.webp)



*如果您感兴趣，我们不妨来了解一下允许密钥通过不安全通道传输的底层机制*。



*我们在这里实际上是通过 Diffie-Hellman 密钥交换方法发起密钥传输，这部分内容在我下面提供的 BTC204 课程中有详细介绍。*。



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*我们目前已有：*




- 生成了一对临时密钥（公钥/私钥分别为 Ka 和 ka，其中 Ka=G.ka，G 为 ECDH 生成点），以及一个 8 位数的密码。

- 使用此密码通过 AES-256-CTR 加密公钥 (Ka)，然后通过通信信道 A 将此密码传输到 “发送” ColdCardQ。

- 最后，我们使用与第一个通信信道不同的第二个通信信道 B，通过上述二维码将加密数据包传输给发送者。



#### 准备用来发送机密的设备



在发送设备上点击 **"QR"** 按钮，扫描接收设备发送给您的二维码，然后通过单独通道输入上一步中告知您的 8 位数密码。现在我们可以开始从 "发送" 设备发送数据了。



**请勿输入错误的 8 位密码，因为不会显示错误信息，流程将继续。但是，最终数据传输将会失败，您需要重新开始。**。



![CCQ-key-teleport](assets/fr/03.webp)



**对于比较好奇的读者，让我们再来看看我们在密码学和秘密传输方面所做的工作：**




- 我们通过扫描接收设备上的二维码导入了加密数据。
- 然后，我们使用通过辅助通道传输给我们的 8 位密码对其进行解密。
- 因此，我们获得了接收方最初生成的公钥 (Ka)。
- 接下来，我们在发送设备上生成一个新的临时密钥对 (Kb/kb，其中 Kb = G.kb)，并使用该密钥对 Ka 应用 ECDH。因此，我们执行操作 kb.Ka = Ks，其中 Ks 被称为 **Session Key**。




现在，您需要选择要在 2 个 ColdCardQ 之间传输的秘密的性质（机密笔记、密码、完整备份、您保险库中包含的种子、种子设备主控）。



![CCQ-key-teleport](assets/fr/04.webp)



在这里，我们的秘诀是选择 **"Quick Text Message"**，发送一条短信息。输入您的信息（例如“Plan ₿ Academy rocks”），然后按 **"ENTER"**。


然后，设备会生成一个新的随机密码，称为 **"Teleport Password "**，例如 "NE XG BT SK"。



![CCQ-key-teleport](assets/fr/05.webp)



按下 **"ENTER"**，您将看到一个新的二维码。请接收设备扫描该二维码。然后在另一个通信频道上，向接收设备发送 **"Teleport Password"**。



![CCQ-key-teleport](assets/fr/06.webp)



*在此，我们再次向好奇的读者介绍这一阶段的情况：*




- 选择要传送的秘密后，我们将生成一个新的随机密码，名为 **"Teleport Password"**。
- 然后，我们使用上一步生成的 **"Session Key"**，即 "Ks"，通过 AES-256-CTR 对秘密进行加密。
- 在已使用 **"Session Key"** 加密的数据包前加上我们的 Kb 公钥，然后使用 **"Teleport Password"**。再进行一层 AES-256-CTR 加密。最后，将整个数据包编码成二维码。




#### 完成向接收设备的密钥传输


按下 **QR** 按钮，扫描发送设备通过 Visio 通道显示的二维码。系统会提示您输入 **Teleport Password**：NE XG BT SK。



![CCQ-key-teleport](assets/fr/07.webp)





然后对数据进行解密，使接收设备能够理解这些数据。接收到的信息确实是 "Plan ₿ Academy rocks"。仅此而已。



![CCQ-key-teleport](assets/fr/08.webp)



**最后阶段究竟发生了什么？**

- 我们使用 **“Teleport Password”** 解密了发送方发送的数据。
- 因此，我们得到了公钥 Kb 和由 “Session Key” Ks 加密的秘密消息。但是，作为接收方，我们并不知道发送方生成的 Ks，该如何操作呢？
- 我们需要将初始步骤 **"Prepare the device that will receive the data"** 中获得的私钥 ka 应用于公钥 Kb。
- 实际上，通过计算 **ka.Kb = ka.kb.G = kb.ka.G = kb.Ka = Ks**，我们可以得到 **Ks**。最终，Ks 用于解密秘密消息。


### 2- 将 PSBT 转移到多签名钱包（高级）



前提是您的多签名钱包已创建好，并且您的 ColdCardQ 设备已经预设为可以执行多重签名交易。如果不是这种情况，可在 Coinkite 网站 [此处](https://coldcard.com/docs/Multisig/) 上查阅相关解释。



简单提醒一下什么是多签名钱包（Multisig）。


通常情况下，要使用钱包中的资金，只需要一个私钥即可解锁与您的地址关联的UTXO。

如果是多签名钱包，则可能需要多达 15 个私钥，因此也需要 15 个签名才能使用资金。这被称为 “M/N” 钱包，其中 N 介于 1 到 15 之间，M 是资金可供使用所需的签名数量。例如，一个 3/5 多签名钱包至少需要 5 个签名中的 3 个。


接下来的挑战在于如何协调签名者轮流签名“部分签名比特币交易”（PSBT）。在这种情况下，**Key Teleport** 可以用于以简单且保密的方式在共同签名者之间传输 PSBT。共同签名者之间的一次简单视频通话即可实现。



以下是 3/4 多签名钱包的实现方式。



**签名者 1：**



签名者 1 导入并签署 PSBT。最后，他点击 “T” 键，使用 “Key Teleport” 功能将 PSBT 发送给签名者 2。


![CCQ-key-teleport](assets/fr/09.webp)




点击 **"ENTER"** 选择签名者 2 后，将提供一个 "Teleport Password"（此处为 JJ YC AB 6A），该密码必须通过其他通信渠道发送给签名者 2。例如，可以通过短信或语音通话发送，但**不能**使用视频通话。



再次按下 “ENTER” 键，系统将显示一个二维码，该二维码代表由签名者 1 签名并使用 “TELEPORT PASSWORD” 加密的 PSBT。



![CCQ-key-teleport](assets/fr/10.webp)



**签名者 2：**



签名者 2 扫描签名者 1 向其展示的二维码。然后输入通过辅助通信通道传输的 “TELEPORT PASSWORD” 以解密传输的数据。

签名者 2 对交易进行签名，然后点击 “T” 键，通过 "Key Teleport" 将 PSBT 发送给签名者 3。

显然，已经完成了 2 次签名。现在只差签名者 3 的签名，交易才能生效。点击 “ENTER” 键选择签名者 3。



![CCQ-key-teleport](assets/fr/11.webp)



然后生成一个新的 “TELEPORT PASSWORD”，接着生成一个二维码，该二维码编码了由签名者 1 和签名者 2 签名的 PSBT，并使用该新的 “TELEPORT PASSWORD”（GW YQ K3 LL）进行加密。



![CCQ-key-teleport](assets/fr/12.webp)



**签名者 3：**

重复上述步骤


签名者 3 扫描签名者 2 向其展示的二维码。然后输入通过辅助通信通道传输的 “TELEPORT PASSWORD”。



签名者 3 对交易进行签名。此时，由于已完成 4 个签名中的 3 个，交易被标记为已完成，并可通过各种媒介（SD 卡、NFC、二维码等）进行分发。


![CCQ-key-teleport](assets/fr/13.webp)



如果您的 ColdCardQ 的 “Push Tx” 功能已激活，只需将您的 ColdCardQ 贴在任何支持 NFC 的联网设备（智能手机/平板电脑）的背面，即可通过比特币网络广播交易。



![CCQ-key-teleport](assets/fr/14.webp)



*对于从一个签名者到另一个签名者的 PSBT 转移，“Key Teleport” 只需在每个阶段使用 “Teleport Password” 即可，该密码会在 PSBT 从一个签名者传输到另一个签名者时对其进行加密。由于传输的数据不能用于窃取资金，因此无需像发送高度机密信息（种子、密码等）时那样使用 Diffie-Hellman 密钥交换。*



![CCQ-key-teleport](assets/fr/15.webp)



*来源：[ColdCard 官方网站](https://coldcard.com/)*
