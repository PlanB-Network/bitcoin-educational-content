---
name: 玉石 - Electrum
description: 如何使用带有 Electrum 的 Jade 或 Jade Plus（台式机）
---

![cover](assets/cover.webp)



_本指南摘自[Bitcoin 讲习班课程](https://officinebitcoin.it/lezioni/jadeele/index.html)_



本教程使用 Jade Classic 制作，但其操作同样适用于使用 Jade Plus 的用户。



初始化 Jade 后，您就可以开始使用它，并选择一个 wallet 显示器。



Jade 是一款可与多个 wallet 或 Blockstream 网站上指定的配套应用程序一起使用的设备。



在本教程中，您将看到通过 USB 电缆连接使用 Electrum Wallet 的步骤。



## 公钥转让



打开已初始化的 Jade。一打开它，就会出现下面这个样子：




![img](assets/en/32.webp)



如果选择 _Unlock Jade_（解锁 Jade），就会出现一个菜单，让你选择如何将设备连接到配套应用程序。



Electrum 只能通过 USB 连接 Jade，因此请选择这种方法。



启动 Electrum，它将作为默认选项打开上次使用的 wallet。



如果您是第一次将 Jade 连接到 Electrum，请选择_创建新钱包_，然后选择_完成_。



![img](assets/en/34.webp)



名称 wallet。



![img](assets/en/35.webp)



选择标准 Wallet。



![img](assets/en/36.webp)



选择密钥存储时，必须选择_使用硬件设备_。



![img](assets/en/37.webp)



Electrum 开始扫描硬件设备。



![img](assets/en/38.webp)



通过 USB 与电脑连接（USB C 端已与 Jade 连接），wallet 硬件就会显示为锁定模式。输入设置时设置的六位数密码，Jade 即可解锁。




![img](assets/en/39.webp)



解锁硬件设备，Electrum 检测到 Jade。点击 "下一步 "继续。



![img](assets/en/40.webp)



此时，Electrum 会要求您设置策略脚本：选择 _Native Segwit_。



![img](assets/en/41.webp)



wallet 从 Jade 向 Electrum 传输公钥的阶段开始。



公钥导出完成后，程序也就结束了。



只读手表已准备就绪，Electrum 将通过以下屏幕发出完成提示。



![img](assets/en/42.webp)



wallet 实际上已经创建，您可以开始探索它：您可以看到_地址_、_钱包信息_，最重要的是，您可以在右下角看到它是 Blockstream 设备的提示。Blockstream 徽标旁边的绿点表示设备已打开并已正确连接到本地网络。



![img](assets/en/43.webp)



## 接收和支出交易



从 Electrum 的 _Receive_ 菜单，generate 获取一个 `scriptPubKey`（地址）来接收资金。始终从小额开始，并进行接收+支出测试。



![img](assets/en/44.webp)



收到卫星后，您可以在_History_（历史）菜单中查看卫星的到达情况。



![img](assets/en/45.webp)



![img](assets/en/46.webp)



交易确认后，您就可以使用这笔 UTXO 并完成测试。



这笔费用涉及使用 Jade 签名。



转到 Electrum 的 _Send_ 菜单，粘贴一个 scriptPubKey 并检查无误。



![img](assets/en/47.webp)



完成后，按_Pay_。



交易窗口打开，在此必须设置正确的交易费用。完成所有设置后，点击右下角的_Preview_（预览）。



![img](assets/en/48.webp)



交易窗口会显示一些重要细节，首先是状态：未签名



在此阶段，您还可以看到_Sign_（签名）命令，您必须点击该命令才能在 Jade 上签名。



![img](assets/en/49.webp)



现在开始显示屏 wallet 和硬件设备之间的通信阶段，Electrum 会提醒您按照硬件设备上的指示进行操作，硬件设备已打开并准备好签名。



![img](assets/en/50.webp)



**不过，您最好先验证一下您要签署的内容：您刚刚设置的交易的所有参数也会出现在 Jade** 上，您可以对它们进行验证。



![img](assets/en/51.webp)



要继续操作，请确保始终将光标放在通往下一步的箭头"→"上，而不要放在 "X "上，除非您想在未完成操作的情况下结束操作。



验证部分以显示费用结束。此时的确认相当于签名。



![img](assets/en/52.webp)



Jade 会短暂处理该操作，完成后会返回主菜单。



![img](assets/en/53.webp)



在 Electrum 上，您可以看到事务的状态已从 "未署名 "变为 "已署名"，现在您可以点击_Broadcast_来传播该事务。



![img](assets/en/54.webp)



经测试，wallet 可用于接收 UTXO，以便安全储存。



![img](assets/en/55.webp)



本指南举例说明如何通过 USB 将您的 Jade 与 wallet 手表连接。Electrum 是一个典型的例子，但你可能更喜欢其他 wallet 软件。Jade 可以将公钥导出到许多其他钱包：在本教程中，您可以找到类似的功能，指导您如何使用您最喜欢的 companio 应用程序。