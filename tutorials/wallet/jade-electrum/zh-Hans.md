---
name: Jade - Electrum
description: 如何使用带有 Electrum 的 Jade 或 Jade Plus（桌面）
---

![cover](assets/cover.webp)



_本指南摘自[Bitcoin Workshops 课程](https://officinebitcoin.it/lezioni/jadeele/index.html)_

本教程以 Jade Classic 为例，但操作步骤同样适用于 Jade Plus 用户。

初始化 Jade 后，即可开始使用，并选择一个钱包显示界面。

Jade 是一款可以与多种钱包或配套应用程序配合使用的设备，具体请参阅 Blockstream 网站上的相关说明。

本教程将介绍如何通过 USB 数据线连接使用 Electrum 钱包。

## 公钥传输

取出并打开已初始化的 Jade。开机后界面如下：

![img](assets/en/32.webp)



如果选择 _Unlock Jade_，就会出现一个选单，让您选择如何将设备连接到配套应用程序。

使用 Electrum 时，Jade 只能通过 USB 连接，因此请选择此方法。

启动 Electrum，默认情况下会提示您打开上次使用的钱包。

如果您是第一次将 Jade 连接到 Electrum，请选择 _Create New Wallet_，然后选择 _Finish_。

![img](assets/en/34.webp)

为钱包命名。

![img](assets/en/35.webp)

选择 "Standard Wallet"。

![img](assets/en/36.webp)

选择密钥存储时，必须选择 _Use a hardware device_。

![img](assets/en/37.webp)

Electrum 将开始扫描硬件设备。

![img](assets/en/38.webp)

将 USB 线连接到电脑（USB-C 端已连接到 Jade），钱包硬件将显示为锁定状态。输入设置过程中设置的六位 PIN 码即可解锁 Jade。

![img](assets/en/39.webp)

硬件设备已解锁，Electrum 检测到 Jade。点击 _Next_ 以继续。

![img](assets/en/40.webp)

此时，Electrum 会提示您设置策略脚本：选择 _Native Segwit_。

![img](assets/en/41.webp)

从 Jade 钱包向 Electrum 显示器传输公钥的阶段开始。

公钥导出完成后，该过程结束。

仅供查看模式已准备就绪，Electrum 会显示以下屏幕提示完成。

![img](assets/en/42.webp)

钱包已创建完成，您可以开始探索：您可以查看地址、钱包信息，最重要的是，您可以在右下角看到这是 Blockstream 设备的标识。Blockstream 徽标旁边的绿点表示设备已开启并已正确连接到本地网络。

![img](assets/en/43.webp)

## 接收和支出交易

在 Electrum 的 “Receive” 选单中，生成一个 `scriptPubKey`（地址）来接收资金。始终从小额资金开始，并进行收付款测试。

![img](assets/en/44.webp)

收到聪（比特币）后，您可以在 “History” 选单中查看到账情况。

![img](assets/en/45.webp)

![img](assets/en/46.webp)

交易确认后，即可使用此 UTXO 以完成测试。

费用包含使用 Jade 进行签名。

前往 Electrum 的 “Send” 选单，粘贴scriptPubKey并仔细检查。

![img](assets/en/47.webp)

完成后，点击 _Pay_。

交易窗口打开，请务必在此设置正确的交易费用。完成所有设置后，点击右下角的 “Preview”。

![img](assets/en/48.webp)

交易窗口显示一些重要信息，首先是状态：`Unsigned`（未签名）

在此阶段，您还可以看到 _Sign_（签名）命令，您必须点击该命令才能在 Jade 上签名。

![img](assets/en/49.webp)

现在开始所显示的钱包和硬件设备之间的通信阶段，Electrum 会提醒您按照硬件设备上的指示进行操作，硬件设备已打开并准备好签名。

![img](assets/en/50.webp)

**然而，首先您最好确认一下您要签名的内容：您刚刚设置的交易的所有参数也会显示在 Jade 上，** 您可以逐一进行验证。

![img](assets/en/51.webp)

要继续操作，请确保始终将光标放在指向下一步的 `→` 箭头上，切勿放在 `X` 上，除非您想在未完成操作的情况下终止操作。

验证部分以手续费显示结束。此时，确认操作就相当于签名。

![img](assets/en/52.webp)

Jade 会短暂处理该操作，完成后会返回主选单。

![img](assets/en/53.webp)

在 Electrum 钱包中，您可以查看交易状态，该状态已从 `Unsigned`(未签名) 变为 `Signed`（已签名）。现在，您可以点击 “_Broadcast_” 按钮来广播该交易。

![img](assets/en/54.webp)

经测试，此钱包可用于接收用于安全存储的 UTXO。

![img](assets/en/55.webp)

本指南以一个示例为例，说明如何将通过 USB 连接的 Jade 连接到仅观察（watch-only）的钱包。Electrum 是一个经典示例，但您可能更喜欢其他钱包。
