---
name: BIP-39 密钥 SeedSigner
description: 如何将 passphrase 添加到我的 SeedSigner 投资组合中？
---

![cover](assets/cover.webp)



passphrase BIP39 是一个可选密码，它与记忆短语相结合，为确定性和分层式 Bitcoin 钱包提供了额外的安全保护。在本教程中，我们将共同探讨如何在与 SeedSigner 一起使用的 Bitcoin wallet 上设置 passphrase。



![Image](assets/fr/01.webp)



## 添加密码前的先决条件



在开始本教程之前，如果您不熟悉 passphrase 的概念、工作原理及其对 Bitcoin wallet 的影响，我强烈建议您参阅我在另一篇理论文章中的解释（这一点非常重要，因为在不完全了解 passphrase 工作原理的情况下使用 passphrase 会让您的比特币面临风险）：



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

在开始本教程之前，请确保您已经初始化了 SeedSigner 并生成了记忆短语。如果您还没有，而且您的 SeedSigner 是全新的，请按照 Plan ₿ Academy 上的教程进行操作。完成此步骤后，您可以返回本教程：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 如何将 passphrase 添加到 SeedSigner？



将 passphrase 添加到通过 SeedSigner 管理的投资组合中会创建一个全新的投资组合，生成一套完全独立的密钥。因此，如果您已经有一个包含 Satss 的投资组合，您将无法再用 passphrase 访问它，因为它会生成一个完全不同的投资组合。



要在 SeedSigner 上应用 passphrase，请打开设备并像往常一样扫描 SeedQR。然后，SeedSigner 将显示您当前 wallet 的指纹，与**没有 passphrase 的 wallet 相对应。带有 passphrase 的 wallet 将具有不同的指纹。



单击 "BIP-39 密码 "按钮。



![Image](assets/fr/02.webp)



然后使用屏幕键盘在提供的字段中输入您选择的 passphrase。请务必做一个或多个物理备份（纸质或金属）：丢失 passphrase 将导致永久无法访问您的比特币。 **要恢复 wallet，助记符和 passphrase 都是必不可少的。



完成输入后，按下 SeedSigner 右下方的 "KEY3 "按钮进行验证。



![Image](assets/fr/03.webp)



*在这个例子中，我使用的是 passphrase `pba`。但是，在您的情况下，请确保您选择的是稳健的 passphrase。如需了解如何定义最佳 passphrase，请参阅另一篇文章： *



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner 会显示 passphrase wallet 的新指纹。将该指纹复制多份： 这对使用 passphrase 和 wallet 时非常重要，因为它可以让您在每次输入 passphrase 时检查您是否输入错误，以及您是否访问了正确的 wallet。



例如，如果我在启动 SeedSigner 时错误地写下了 passphrase `Pba` 而不是 `pba`，那么从小写字母到大写字母的简单改变就会导致创建一个与我想要访问的完全不同的投资组合。



该指纹不会对您的 wallet 的安全性或保密性造成任何风险。它不会泄露任何有关您的密钥的公共或私人信息。因此，与助记符和 passphrase 不同，您可以将指纹保存在数字介质上。我建议您在多个地方保存一份副本：纸张、密码管理器等。



保存指纹后，点击 "完成"。



![Image](assets/fr/04.webp)



然后，您就可以访问您的投资组合的所有功能，就像在经典的 SeedSigner 上一样。



![Image](assets/fr/05.webp)



现在您可以将密钥存储导入 Sparrow Wallet 并正常使用 wallet。每次重启时，您都需要扫描 SeedQR 并使用键盘重新输入 passphrase，就像我们在这里所做的那样。



在实际使用 wallet 与 passphrase 之前，我强烈建议您进行一次完全的空恢复测试。这将允许您确认记忆短语和 passphrase 的备份是有效的。要了解如何执行此检查，请参阅以下教程：



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895