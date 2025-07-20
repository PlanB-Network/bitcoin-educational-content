---
name: passphrase BIP39 Trezor
description: 如何将 passphrase 添加到 Trezor 产品组合中？
---
![cover](assets/cover.webp)



passphrase BIP39 是一个可选密码，与 Mnemonic 短语相结合，为确定性和分层 Bitcoin 组合提供额外的 Layer 安全性。在本教程中，我们将共同探讨如何在 Trezor（Safe 3、Safe 5 和 Model One）上的安全 Bitcoin Wallet 上设置 passphrase。



![Image](assets/fr/01.webp)



在开始本教程之前，如果您不熟悉 passphrase 的概念、工作原理及其对 Bitcoin Wallet 的影响，我强烈建议您参阅我在另一篇理论文章中的解释（这一点非常重要，因为在不完全了解 passphrase 工作原理的情况下使用 passphrase 会给您的比特币带来风险）：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果在配置过程中选择了 BIP39 标准，Trezor 上的 passphrase 将以传统方式处理（如果不需要*多共享备份*，我建议使用这种方式）。Trezor 的特别之处在于，你既可以直接在 Hardware Wallet 上输入 passphrase，也可以使用 Trezor Suite 软件通过电脑键盘输入。第二种方法的安全性要低得多，因为电脑的攻击面比 Hardware Wallet 大得多。不过，在传统键盘上输入复杂的 passphrase 可能比在 Hardware Wallet 上更快，这可能会鼓励使用强密码。因此，即使必须输入 passphrase，使用 passphrase 总比不使用要好。不过，重要的是要始终意识到这意味着数字攻击风险的增加。



并非所有与 Trezor 兼容的投资组合管理软件都提供这些选项。例如，对于 Model One，可通过 Sparrow Wallet 上的键盘输入 passphrase。对于 T 型、Safe 3 和 Safe 5 型，您必须使用 Trezor Suite 或直接在 Hardware Wallet 上输入 passphrase，因为通过 Sparrow 输入的选项几年前已被 HWI 禁用。



![Image](assets/fr/02.webp)



在 Trezor Suite 中，有两种管理 passphrase 需求的不同方法。您可以激活 "*设备*"选项卡中的 "*passphrase*"选项。如果启用该选项，Trezor Suite 和所有其他投资组合管理软件都会在每次启动时系统地要求您输入 passphrase。如果您喜欢更谨慎地使用 passphrase，可以将设置保留为 "*标准*"。在这种情况下，您需要手动访问 Hardware Wallet 左上角的菜单，并在每次启动时点击 "*+ passphrase*"按钮。



在开始本教程之前，请确保您已经初始化了 Trezor 并生成了 Mnemonic 短语。如果尚未初始化，并且您的 Trezor 是新产品，请按照 Plan ₿ Network 上的特定型号教程进行操作。完成这一步骤后，即可返回本教程。



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## 为保险柜 3 或保险柜 5 添加 passphrase



创建 Wallet、保存 Mnemonic 和设置 PIN 码后，就会进入 Trezor Suite 的主菜单。左上角会出现一个窗口，邀请您激活 passphrase BIP39。



![Image](assets/fr/03.webp)



如果该窗口没有出现，则需要在 "*设备*"设置选项卡中手动激活 "*passphrase*"选项。



![Image](assets/fr/04.webp)



该窗口要求您输入 passphrase。选择一个强大的 passphrase，并立即在纸张或金属等介质上进行物理备份。在本例中，我选择的是 passphrase：`fH3&kL@9mP#2sD5qR!82`.这只是一个例子，但我建议您选择稍长一点的 passphrase。30 到 40 个字符是最理想的（就像一个好的密码）。



当然，您千万不要像我在本教程中所做的那样，在互联网上分享您的 passphrase。本例中的 Wallet 只能在 Testnet 上使用，并将在教程结束时删除。



有关选择 passphrase 的更多具体建议，请再次参阅另一篇文章：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您想通过电脑键盘输入您的 passphrase，请在提供的字段中输入，然后点击 "*访问 passphrase Wallet*"。



![Image](assets/fr/05.webp)



然后，Hardware Wallet 将显示您的 passphrase。在点击屏幕继续之前，请确保它与您的物理备份（纸质或金属）相匹配。



![Image](assets/fr/06.webp)



这样您就可以访问受 passphrase 保护的投资组合。



![Image](assets/fr/07.webp)



如果您希望只在 Trezor 上输入 passphrase，以提高安全性，请在出现提示时点击 "*在 Trezor 上输入 passphrase*"。



![Image](assets/fr/08.webp)



Trezor 上会出现一个 T9 键盘，让您输入 passphrase。完成输入后，点击 Green 标记，将 passphrase 应用到 Wallet 上。



![Image](assets/fr/09.webp)



然后，您就可以访问您的 passphrase 安全 Wallet。



![Image](assets/fr/10.webp)



使用麻雀 Wallet 的步骤类似，但对于 T、Safe 3 和 Safe 5 型号，必须在 Hardware Wallet 上输入 passphrase，而不是通过计算机键盘。



如果麻雀 Wallet 需要访问 Trezor，而上次启动后尚未应用 passphrase，则需要使用 T9 键盘输入。



![Image](assets/fr/11.webp)



## 为一号模型添加 passphrase



在 Model One 上，使用 passphrase BIP39 几乎是必不可少的。由于该设备没有安全元件，因此相对容易提取敏感信息。因此，它无法抵御物理攻击。不过，由于 passphrase 在关机后不会保留在设备上，因此使用强力（不可篡改）的 passphrase 可以保护您免受该型号设备上大多数已知的物理攻击。



在 Model One 上，无法直接在 Hardware Wallet 上输入 passphrase。您需要通过电脑键盘输入。



创建 Wallet、保存 Mnemonic 和设置 PIN 码后，就会进入 Trezor Suite 的主菜单。左上角会出现一个窗口，邀请你激活 passphrase BIP39。



![Image](assets/fr/12.webp)



如果该窗口未出现，则需要在设置的 "*设备*"选项卡中激活 "*passphrase*"选项。



![Image](assets/fr/13.webp)



该窗口要求您输入 passphrase。选择一个强大的 passphrase，并立即在纸张或金属等介质上进行物理备份。在这个例子中，我选择了 passphrase：`fH3&kL@9mP#2sD5qR!82`。这只是一个例子，但我建议您选择稍长一点的 passphrase。30 到 40 个字符是最理想的（就像一个好的密码）。



关于选择 passphrase 的更多具体建议，我再次邀请您参阅另一篇文章：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

在提供的字段中输入您的 passphrase，然后点击 "*访问 passphrase Wallet*"按钮。



![Image](assets/fr/14.webp)



您的 Hardware Wallet 将显示您的 passphrase。确保它与您的物理备份（纸质或金属）相匹配，然后点击右侧按钮继续。



![Image](assets/fr/15.webp)



这将带您进入受 passphrase 保护的投资组合。



![Image](assets/fr/16.webp)



此后使用麻雀 Wallet 的程序保持不变。每次麻雀需要访问您的 Hardware Wallet，且设备上次启动后尚未输入 passphrase，您都需要输入。



![Image](assets/fr/17.webp)



恭喜您，现在您已经掌握了在 Trezor 硬件钱包上使用 passphrase BIP39 的方法。如果你想进一步提高 Wallet 的安全性，请查看本教程，了解 Trezor 的*多共享*备份系统（*Shamir 的秘密共享计划*）：



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

如果您觉得本教程有用，请在下方留下 Green 大拇指，我将不胜感激。欢迎在您的社交网络上分享本文。非常感谢