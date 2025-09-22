---
name: Trezor Shamir Backup
description: Trezor 上的单股和多股 Mnemonic 短语
---
![cover](assets/cover.webp)



*图片来源：[Trezor.io](https://trezor.io/)*



## Trezor 上的新备份选项



自 2023 年以来，Trezor 一直在提供一种名为 "***单一份额备份***"的新备份格式，逐步取代了大多数投资组合中基于 BIP39 的经典方法。与传统的 12 个字或 24 个字的 Mnemonic 短语不同，这种新格式基于一个 20 个字的短语，该短语源自中本聪实验室开发的标准： **SLIP39**。其目的是提高备份的稳健性和可读性，同时实现向分布式备份模式的顺利迁移。



这种分布式模式被称为**多共享备份**。它基于相同的原理，但不是生成一个单一的 Mnemonic 短语，而是将其分割成多个称为 **shares** 的片段，每个片段本身就是一个 Mnemonic 短语。要恢复组合，其中一定数量的 *shares*（由 *threshold* 定义）必须重新组合。例如，在 "3-of-5 "方案中，5 份中的任何 3 份都能恢复投资组合。请注意，Trezor 的分布式备份系统不同于 Multisig 钱包。要使用比特币，只需使用 Hardware Wallet Trezor。只需要一个签名。分布式仅适用于 Mnemonic 短语级别，即备份。



![Image](assets/fr/01.webp)



该系统解决了 Mnemonic 短语的单点故障问题，却没有管理 Multisig 或 passphrase BIP39 的弊端。恢复过程不再以单一信息为基础，而是以多个信息为基础。



使用*单份备份*创建了投资组合的用户可随时切换到*多份备份*，而无需迁移投资组合。接收地址和账户将保持不变。*多份备份*系统只影响备份，而投资组合的其他部分保持不变。



Trezor Model T、Safe 3 和 Safe 5 提供多共享备份。Trezor Model One 不支持该功能。



**重要提示：** Trezor 的*多重共享*系统采用*沙米尔秘密共享*方案进行分发，因此在加密方面是安全的。我们强烈建议不要手动应用类似的系统，自行分割经典的 Mnemonic 短语。这种做法很糟糕，会大大增加比特币被盗和丢失的风险，所以千万不要这么做。经典 Mnemonic 短语是完整存储的。



## 沙米尔在 SLIP39 中分享秘密



Trezor 上*多共享*备份的加密机制是*沙米尔秘密共享方案*（SSSS）。其原理如下：将秘密信息（此处为投资组合的 seed）转化为数学多项式。然后计算这个多项式的几个点，每个点成为一个份额。通过收集最少的点数（阈值），用多项式插值法重建原始秘密。



从低于阈值的份额数中无法推导出任何秘密信息，从而保证了秘密信息在理论上的完美安全性。换句话说，如果没有达到阈值，即使拥有无限计算能力的攻击者也无法猜出 seed。



SLIP39 采用这种方案来分配 seed 组合。每一份都是一个 20 个单词的句子，由 1024 个单词组成（与 BIP39 的单词列表不同）。



## 在 Trezor 上设置多共享备份



在 Trezor 上创建投资组合时，您有三种不同的选择：




- 使用 12 或 24 个单词的经典 BIP39 Mnemonic 短语；
- 使用单共享 Mnemonic 短语 (SLIP39)；
- 在多共享（SLIP39）中配置多个 Mnemonic 短语。



如果您选择单份额 SLIP39 Mnemonic 词组，以后就可以升级为多份额，而无需重置组合。另一方面，如果您使用的是经典 BIP39 组合（12 或 24 个单词的短语），则无法直接转换为多份额。您必须从头开始创建一个新的多份额投资组合，并通过一次或多次 Bitcoin 交易将资金从旧投资组合转入新组合。这种操作更为复杂，成本也更高。如果您想进行这种迁移，我建议您购买一个新的 Hardware Wallet Trezor，以避免在投资组合软件中输入您的 seed。



在本教程中，我们将首先了解如何在创建投资组合时设置多份额，然后在随后的章节中了解如何在现有投资组合中将单份额转换为多份额。



如果您需要设备初始设置方面的帮助，我们还为每种 Trezor 型号提供了详细的教程：



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### 关于新的投资组合



现在您已经完成了 Trezor 的初始配置，可以创建投资组合了。在 Trezor Suite 中，点击 "*创建新的 Wallet*"按钮。



![Image](assets/fr/02.webp)



选择 "*多共享备份*"选项，然后点击 "*创建 Wallet*"。



![Image](assets/fr/03.webp)



接受 Trezor 上的使用条款并确认创建投资组合。



![Image](assets/fr/04.webp)



在 Trezor Suite 中，点击 "*继续备份*"。



![Image](assets/fr/05.webp)



仔细阅读说明，确认后点击 "*创建 Wallet 备份*"。



![Image](assets/fr/06.webp)



有关保存和管理 Mnemonic 短语的正确方法的更多信息，我强烈推荐您阅读本教程，尤其是初学者：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

在 Trezor 上选择要配置的共享总数。最常见的配置是 2-de-3 和 3-de-5。在本例中，我将创建 2-de-3，因此选择 3 个共享。每个共享将代表一个 20 个字的 Mnemonic 短语。



**对于 Safe 5 用户，虽然屏幕上会显示 "*轻点继续*"，但您实际上需要向上轻扫来确认**



![Image](assets/fr/07.webp)



然后确认阈值，即重新获得 Wallet 及其中的比特币所需的份额数。



![Image](assets/fr/08.webp)



Trezor 将使用随机数生成器创建您的各种共享（Mnemonic 短语）。请确保在操作过程中无人监视。将屏幕上提供的单词写在您选择的物理介质上。重要的是要保持单词的编号和顺序。



我建议您在单独的介质上记下每个共享文件，并仔细管理它们的存储，避免在同一个地方访问多个共享文件。例如，对于像我这样的 "2-of-3 "配置，一种选择是将一份保存在家中，另一份保存在信任的朋友处，最后一份保存在银行保险箱中。存储位置的选择取决于您的个人安全策略。



您可以在屏幕上方看到当前正在查看的共享。



当然，您绝不能像我在本教程中所做的那样，在互联网上分享这些文字。本例 Wallet 将仅用于 Testnet，并将在教程结束时删除。



![Image](assets/fr/09.webp)



要进入下一个单词，请点击屏幕底部。您可以通过向下滑动来倒退。写下所有单词后，手指停留在屏幕上，进入下一份，重复上述操作。



![Image](assets/fr/10.webp)



每次分享录音结束时，系统都会要求您选择 Mnemonic 短语中的单词，以确认您是否正确写下了这些单词。



![Image](assets/fr/11.webp)



这样，您就成功使用多共享选项备份了您的投资组合。现在您可以继续执行其余的配置说明。



### 现有单股投资组合



如果你已经拥有一个带有单共享备份（SLIP39 Mnemonic 短语，而不是经典的 BIP39 短语）的 Trezor Wallet，并希望提高 Wallet 备份的可用性和安全性，你可以建立一个多共享系统，而无需转移你的比特币。



为此，请连接并解锁 Hardware Wallet。在 Trezor Suite 中进入 "设置"。



![Image](assets/fr/12.webp)



转到 "*设备*"选项卡。



![Image](assets/fr/13.webp)



然后点击 "*创建多共享备份*"。



![Image](assets/fr/14.webp)



阅读说明，然后单击 "*创建多共享备份*"。



![Image](assets/fr/15.webp)



然后，您需要在 Trezor 屏幕上输入当前的 Mnemonic 词组（单共享）。选择字数（默认为 20）。



![Image](assets/fr/16.webp)



然后使用 Trezor 的屏幕键盘输入当前 Mnemonic 短语的每个单词。



![Image](assets/fr/17.webp)



然后，您可以按照上一节提供的说明选择多共享备份的配置。



![Image](assets/fr/18.webp)



创建多共享备份后，您需要决定如何处理原始的单共享 Mnemonic 短语。由于 Bitcoin 组合保持不变，因此该单一短语将始终允许对其进行访问。这取决于您的安全策略，但一般来说，建议您销毁这个短语，以消除单点故障，这正是多共享备份的目的所在。如果您决定销毁它，请确保安全销毁，因为**它仍然可以访问您的比特币**。



恭喜您，现在您已经掌握了在 Trezor 硬件钱包上使用单共享和多共享备份的方法。如果你想进一步提高 Wallet 的安全性，请查看本教程中有关 BIP39 密码的内容：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您觉得本教程有用，请在下面留下 Green 大拇指。欢迎在您的社交网络上分享本文。非常感谢



## 其他资源





- [SLIP-0039：沙米尔 Mnemonic 代码的秘密共享](https://github.com/satoshilabs/slips/blob/master/slip-0039.md)；
- [Trezor上的多共享备份](https://trezor.io/learn/a/multi-share-backup-on-trezor)；
- [维基百科：沙米尔的秘密共享](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing)。