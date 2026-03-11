---
name: Trezor Shamir Backup
description: Trezor 上的单共享和多共享助记词
---
![cover](assets/cover.webp)

*图片来源：[Trezor.io](https://trezor.io/)*

## Trezor 上的新备份选项

自 2023 年以来，Trezor 提供了一种名为 “单共享备份”（Single-share Backup）的全新备份格式，逐步取代了大多数钱包中沿用的传统基于 BIP39 的方法。与传统的 12 或 24 个单词的助记词不同，这种新格式基于一个 20 个单词的短语，该短语源自 SatoshiLabs 开发的标准：**SLIP39**。其目的是提高备份的稳健性和可读性，同时实现向分布式备份模型的平滑迁移。

这种分布式模型被称为 “多共享备份”（Multi-share Backup）。它基于相同的原理，但它不是生成一个单一的助记词，而是将其分割成若干个称为 “份额”（shares）的片段，每个份额本身就是一个助记词。要恢复钱包，必须重新组合一定数量的份额（由阈值定义）。例如，在 3/5 方案中，5 个份额中的任意 3 个即可恢复钱包。请注意，Trezor 的分布式备份系统与多重签名钱包不同。为了使用您的比特币，您只需要您的 Trezor 硬件钱包。只需要一个签名。分布式仅应用于助记词层面，即备份层面。

![Image](assets/fr/01.webp)

该系统解决了助记词单点故障的问题，同时避免了管理多签名或 BIP39 Passphrase（密语）的缺点。恢复过程不再基于单一信息，而是基于多条信息，并且由于阈值的存在，还具有更高的容错能力。

使用“单共享备份”创建钱包的用户可随时切换到“多共享备份”，无需迁移钱包。接收地址和账户将保持不变。“多共享备份”系统仅影响备份，钱包的其余部分保持不变。

“多共享备份”功能适用于 Trezor Model T、Safe 3 和 Safe 5。Trezor Model One 不支持此功能。

**重要提示：** Trezor 的“多共享备份”系统采用加密技术，确保安全，因为它使用 *Shamir's Secret Sharing Scheme* (SSSS，即 Shamir 秘密共享方案) 进行分发。我们强烈建议您不要手动分割经典助记词来应用类似的系统。这种做法会显著增加比特币被盗和丢失的风险，因此请勿这样做。经典助记词完整存储。

## SLIP39 中的 Shamir 秘密共享

Trezor 上的 *Multi-share* 备份底层加密机制是 *Shamir‘s Secret Sharing Scheme* (SSSS)。其原理如下：将秘密信息（在本例中为钱包种子）转换为数学多项式。然后计算该多项式的若干个点，每个点构成一个份额。通过多项式插值，收集到最少数量的点（阈值），即可重构原始秘密信息。

低于阈值的份额数量无法推导出任何秘密信息，从而保证了秘密信息的完美理论安全性。换句话说，即使拥有无限计算能力的攻击者，如果未达到阈值，也无法猜出种子。

SLIP39 使用此方案分发种子钱包。每个份额都是一个 20 个单词的列表，由一个包含 1024 个单词的列表构成（与 BIP39 列表不同）。

## 在 Trezor 上设置多共享备份

在 Trezor 上创建钱包时，您有三种不同的选择：

- 使用经典的 BIP39 助记词（12 或 24 个单词）；
- 使用单共享助记词 (SLIP39)；
- 在多共享 (SLIP39) 中配置多个助记词。

如果您选择使用单共享 SLIP39 助记词，以后无需重置钱包即可升级到多共享钱包。另一方面，如果您从经典的 BIP39 钱包（12 或 24 个单词的助记词）开始，则无法直接将其转换为多共享钱包。您必须从头开始创建一个新的多共享钱包，并通过一笔或多笔比特币交易将资金从旧钱包转移到新钱包。这是一个更复杂且成本更高的操作。如果您想进行此迁移，我建议您购买新的 Trezor 硬件钱包，这样就无需在钱包软件中输入助记词。

在本教程中，我们将首先介绍如何在创建钱包时设置多份额钱包，然后在后续章节中，我们将介绍如何在现有钱包中将单份额钱包转换为多份额钱包。

如果您在设备初始设置方面需要帮助，我们还为每款 Trezor 型号提供了详细的教程：

https://planb.academy/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.academy/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### 创建新钱包

您已完成 Trezor 的初始配置，现在可以创建钱包了。在 Trezor Suite 中，点击 "*Create new Wallet*" 按钮。

![Image](assets/fr/02.webp)

选择 "*Multi-share Backup*" 选项，然后点击 "*Create Wallet*"。

![Image](assets/fr/03.webp)

接受 Trezor 的使用条款，并确认创建钱包。

![Image](assets/fr/04.webp)

在 Trezor Suite 中，点击 "*Continue to backup*"。

![Image](assets/fr/05.webp)

仔细阅读说明，确认后点击 "*Create Wallet backup*"。

![Image](assets/fr/06.webp)

如需了解如何正确保存和管理助记词，我强烈建议您参考以下教程，尤其如果您是新手：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

在 Trezor 设备上，选择您要配置的份额总数。最常见的配置是 2-of-3 和 3-of-5。在本例中，我将创建一个 2-of-3 的配置，因此我将选择 3 个份额。每个份额代表一个 20 个单词的助记词。

*对于 Safe 5 用户，虽然屏幕会显示 “Tap to continue”，但您实际上需要向上滑动以确认。*

![Image](assets/fr/07.webp)

然后确认阈值，即恢复对钱包及其比特币访问权限所需的份额数量。

![Image](assets/fr/08.webp)

Trezor 将使用其随机数生成器创建您的各种份额（助记词）。请确保在此操作过程中无人监视。将屏幕上显示的单词写在您选择的实体介质上。务必按顺序编号并排列单词。

我建议您将每个份额记录在不同的介质上，并妥善保管，避免多个份额放在同一位置。例如，对于像我这样的 2/3 配置，一种方法是将一份放在家里，一份交给值得信赖的朋友，最后一份放在银行保险箱中。存储位置的选择取决于您的个人安全策略。

您可以在屏幕顶部看到当前正在查看的共享内容。

当然，您绝不能像我在本教程中那样在互联网上分享这些单词。此示例钱包仅在测试网上使用，并将在教程结束后删除。

![Image](assets/fr/09.webp)

为了查看下一个单词，请点击屏幕底部。您可以通过向下滑动来返回上一个单词。记下所有单词后，按住屏幕即可查看下一个共享内容，并重复此操作。

![Image](assets/fr/10.webp)

在每次记录共享内容后，系统会要求您选择助记词，以确认您已正确记录。

![Image](assets/fr/11.webp)

好了，您已成功使用多共享选项备份了钱包。现在您可以继续执行剩余的配置步骤。

### 在现有的单共享钱包上

如果您已经拥有一个 Trezor 钱包，并且该钱包使用单共享备份（SLIP39 助记词，而非传统的 BIP39 助记词），并且您希望提高钱包备份的可用性和安全性，您可以设置多共享系统，而无需转移您的比特币。

为此，请连接并解锁您的硬件钱包。在 Trezor Suite 中，前往 “Settings”。

![Image](assets/fr/12.webp)

前往 "*Device*" 选项卡。

![Image](assets/fr/13.webp)

然后点击 "*Create Multi-share Backup*"。

![Image](assets/fr/14.webp)

阅读说明，然后点击 "*Create Multi-share Backup*"。

![Image](assets/fr/15.webp)

接下来，您需要在 Trezor 屏幕上输入您当前的助记词（single-share）。选择单词数量（默认为 20）。

![Image](assets/fr/16.webp)

然后，使用 Trezor 的屏幕键盘输入您当前助记词的每个单词。

![Image](assets/fr/17.webp)

然后，您可以按照上一节中的说明选择多共享备份的配置。

![Image](assets/fr/18.webp)

创建多共享备份后，您需要决定如何处理您最初的单共享助记词。由于比特币钱包保持不变，因此该助记词将始终允许您访问该钱包。这取决于您的安全策略，但通常建议销毁此短语以消除单点故障，这正是多共享备份的目的所在。如果您决定销毁它，请务必确保操作安全，因为**它仍然允许您访问您的比特币**。

恭喜，您现在已经掌握了在 Trezor 硬件钱包上使用单共享备份和多共享备份的方法。如果您想进一步提升钱包安全性，请查看这篇关于 BIP39 Passphrase（密语）的教程：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您觉得这篇教程有用，请在下方点个赞。欢迎在社交网络上分享这篇文章。非常感谢！

## 其他资源

- [SLIP-0039：Shamir 的助记词秘密共享](https://github.com/satoshilabs/slips/blob/master/slip-0039.md)；
- [Trezor 上的多共享备份](https://trezor.io/learn/a/multi-share-backup-on-trezor)；
- [维基百科：Shamir 的秘密共享](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing)。
