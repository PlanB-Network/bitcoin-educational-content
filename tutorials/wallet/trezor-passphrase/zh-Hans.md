---
name: Trezor 上的 BIP-39 Passphrase（密语）
description: 如何为我的 Trezor 钱包添加密语？
---
![cover](assets/cover.webp)

BIP39 Passphrase（密语）是一个可选密码，它与助记词结合使用，可为确定性分层比特币钱包提供额外的安全保障。在本教程中，我们将一起学习如何在 Trezor（Safe 3、Safe 5 和 Model One）上的安全比特币钱包中设置密语。

![Image](assets/fr/01.webp)

在开始本教程之前，如果您还不熟悉密语的概念、工作原理及其对比特币钱包的影响，我强烈建议您先阅读这篇理论文章，其中详细解释了所有相关内容（这一点非常重要，因为在不完全了解其工作原理的情况下使用密语可能会使您的比特币面临风险）：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您在配置过程中选择了 BIP39 标准（如果您不需要*多共享备份*，我推荐您选择此标准），Trezor 的密语处理方式与传统方式相同。Trezor 的特殊之处在于，您可以直接在硬件钱包上输入密语，也可以使用 Trezor Suite 软件通过电脑键盘输入。第二种方法安全性要低得多，因为计算机的攻击面比硬件钱包大得多。然而，在传统键盘上输入复杂的密语可能比在硬件钱包上输入更快，这可能会鼓励用户使用强密语。因此，即使需要手动输入，使用密语也总比完全不使用要好。但是，必须意识到这会增加遭受数字攻击的风险。

并非所有兼容 Trezor 的钱包管理软件都提供这些选项。例如，对于 Model One，可以通过 Sparrow Wallet 上的键盘输入密语。对于 Model T、Safe 3 和 Safe 5 型号，您必须使用 Trezor Suite 或直接在硬件钱包上输入密语，因为 HWI 几年前已禁用通过 Sparrow 输入密语的选项。

![Image](assets/fr/02.webp)

在 Trezor Suite 中，您可以通过两种不同的方式管理密语的需求。您可以在 “*Device*” 选项卡中启用 “*passphrase*” 选项。启用后，Trezor Suite 和所有其他钱包管理软件每次启动时都会自动要求您输入密语。如果您希望使用更隐蔽的密语方式，可以将设置保留为 “*Standard*”。在这种情况下，您需要在每次启动硬件钱包时手动访问左上角的选单，然后点击“*+ passphrase*” 按钮。

在开始本教程之前，请确保您已初始化 Trezor 并生成助记词。如果您尚未初始化 Trezor 并生成助记词，请按照 Plan ₿ Academy 上提供的针对您 Trezor 型号的教程进行操作。完成此步骤后，您可以返回本教程。

https://planb.academy/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.academy/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## 为 Safe 3 或 Safe 5 添加密语

创建钱包、保存助记词并设置 PIN 码后，您将进入 Trezor Suite 的主选单。在左上角，应该会出现一个窗口，提示您激活 BIP39 密语。

![Image](assets/fr/03.webp)

如果此窗口未出现，您需要在 “Device” 设置选项卡中手动激活 “passphrase” 选项。

![Image](assets/fr/04.webp)

此窗口会要求您输入密语。请选择一个强密语，并立即将其备份到纸张或金属等介质上。在本例中，我选择的密语为：`fH3&kL@9mP#2sD5qR!82`。这只是一个示例；不过，我建议您选择一个稍长一些的密语。30 到 40 个字符比较理想（就像一个强密码一样）。

当然，您绝不应该像我在本教程中那样在互联网上分享您的密语。这个示例钱包仅用于测试网，并将在本教程结束后删除。

关于选择密语的更具体建议，我再次邀请您参考这篇文章：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您想通过电脑键盘输入您的密语，请在提供的字段中输入，然后点击 "*Access passphrase Wallet*"。

![Image](assets/fr/05.webp)

您的硬件钱包随后将显示您的密语。请确保它与您的物理备份（纸质或金属）一致，然后再点击屏幕继续。

![Image](assets/fr/06.webp)

这样您就可以访问受密语保护的钱包了。

![Image](assets/fr/07.webp)

如果您希望仅在 Trezor 设备上输入密语以增强安全性，请在提示时点击 “*Enter passphrase on Trezor*”。

![Image](assets/fr/08.webp)

您的 Trezor 设备上将出现一个 T9 键盘，您可以在其中输入密语。输入完成后，点击绿色对勾即可将密语应用到您的钱包。

![Image](assets/fr/09.webp)

然后，您就可以访问您的密语安全钱包了。

![Image](assets/fr/10.webp)

使用 Sparrow Wallet 的步骤类似，但对于 T 型、Safe 3 型和 Safe 5 型 Trezor 设备，必须在硬件钱包上输入密语，而不能通过电脑键盘输入。

每当 Sparrow Wallet 需要访问您的 Trezor 设备，且自上次启动以来尚未设置密码时，您需要使用 T9 键盘输入密码。

![Image](assets/fr/11.webp)

## 为 Model One 添加密码

在 Model One 设备上，使用 BIP39 密语几乎是必不可少的。由于该设备没有内置安全元件，因此敏感信息相对容易被窃取。因此，它无法抵御物理攻击。但是，由于密语在设备关机后不会保留，因此使用强密语（无法被暴力破解）可以保护您免受该型号设备遭受的大多数已知物理攻击。

在 Model One 上，无法直接在硬件钱包上输入密语。您需要通过电脑键盘输入。

创建钱包、保存助记词并设置 PIN 码后，您将进入 Trezor Suite 的主页。在左上角，应该会弹出一个窗口，提示您激活 BIP39 密语。

![Image](assets/fr/12.webp)

如果此窗口未出现，您需要在设置的 “Device” 选项卡中启用 “passphrase” 选项。

![Image](assets/fr/13.webp)

此窗口会要求您输入密语。请选择一个强密语，并立即将其备份到纸张或金属等介质上。在这个例子中，我选择的密语为：`fH3&kL@9mP#2sD5qR!82`。这只是一个示例；不过，我建议您选择一个稍长的密语。30 到 40 个字符比较理想（就像一个强密码一样）。

如需更具体的密语选择建议，我再次邀请您参考这篇文章：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

在提供的字段中输入您的密语，然后点击 “*Access passphrase Wallet*” 按钮。

![Image](assets/fr/14.webp)

您的硬件钱包将显示您的密语。请确保它与您的实体备份（纸质或金属）一致，然后点击右侧按钮以继续。

![Image](assets/fr/15.webp)

这将带您进入带有密语的钱包。

![Image](assets/fr/16.webp)

然后，使用 Sparrow Wallet 的步骤完全相同。每次 Sparrow 需要访问您的硬件钱包，且自上次设备启动以来未输入过密语时，您都需要重新输入密语。

![Image](assets/fr/17.webp)

恭喜，您现在已经掌握了如何在 Trezor 硬件钱包上使用 BIP39 Passphrase（密语）。如果您想进一步提升钱包安全性，不妨看看这篇关于 Trezor *Multi-share* 备份系统（*Shamir's Secret Sharing Scheme*）的教程：

https://planb.academy/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

如果您觉得这篇教程有用，请在下方点个赞。欢迎在社交网络上分享这篇文章。非常感谢！
