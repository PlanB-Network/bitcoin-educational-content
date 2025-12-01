---
name: COLDCARD - 联合签名
description: 了解联合签名功能并在 COLDCARD 上使用该功能
---

![cover](assets/cover.webp)


*注意：本教程针对已经对多重签名钱包、Coinkite 设备以及 Sparrow wallet 或 Nunchuk.* 等软件有一定经验的用户。



![video](https://youtu.be/MjMPDUWWegw)




**为什么冷卡要联合签名？



该功能可让您以硬件安全模块（HSM）的方式在 ColdCard（Q 或 Mk4）设备上添加**支出条件**，以保护您的资金，同时保留相当大的灵活性和控制权。



例如，支出条件可以是





- 幅度限制**：对单次交易中可花费的比特币金额设置上限。
- 速度限制：** 决定在单位时间内（每小时、每天、每周等）可以进行多少笔交易，要求交易之间至少有多少个区块。
- 预先批准的地址：** 只允许向预先批准的地址发送比特币。
- 双因素身份验证：** 需要第三方 2FA 移动应用程序（TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)）在可上网的 NFC 智能手机/平板电脑上进行确认。



**工作原理



在 ColdCard Mk4 或 Q 设备上添加第二个 seed，称为 "消费策略密钥"，在本教程中我们称之为 "C 密钥"。


除了这个额外的 seed 密钥外，您还需要至少一个额外的 Supply 密钥 (XPUB)，我们称之为 "备份密钥"，以便创建一个 Wallet Multisig 2 对 N 密钥。



总之，我们将创建一个 Wallet Multisig，您的 ColdCard 设备将包含 2 个花费资金所需的私人密钥，即设备的 seed 主密钥和 "花费策略密钥"。



每次 "C Key "被要求签名时，指定的消费条件都将适用，ColdCard 只有在交易符合这些条件时才会签名。



如果您希望免除这些消费条件，也可以这样做：




- 使用其中一个备份键和 seed 手柄签名，或根据 Multisig 的大小使用 2 个备份键签名。
- 在 "联合签名 "菜单中输入 "消费政策密钥 "或 "C 密钥"。 **后者不能直接在设备上查询，否则任何人都可以取消已配置的消费条件。




## 配置冷卡联合签名



![video](https://youtu.be/MjMPDUWWegw)



### 1- 激活功能



首先，确保您的设备至少有最新的固件版本：




- Mk4: v5.4.2
- 问：V1.3.2Q




在 Mk4 或 ColdCardQ 上，转到 *Advanced Tools（高级工具）> ColdCard Co-Signing（冷卡联合签名）*。



![Co-Sign](assets/fr/01.webp)



*在下面的教程中，为方便起见，将使用 ColdCardQ 进行截图，但 Mk4 和 Q* 的操作步骤和菜单完全相同。



显示功能摘要。


在我们即将创建的 2 对 3 多重签名 Wallet 中，我们将再次使用指定密钥的术语：



键 A = 冷卡主设备 seed


键 B = 备份键


键 C = 开支政策键



点击 **"ENTER "**。



![Co-Sign](assets/fr/02.webp)



下一步是决定哪个私人密钥作为 "支出政策密钥 "或 "密钥 C"。



我们可以看到，我们有几种选择：





- 或按**"ENTER "**键，generate 会出现一个新的 12 个单词的 seed 句子。





- 点击**"(1) "**导入现有的 12 个字的 seed，或选择**"(2) "**导入现有的 24 个字的 seed。





- 或按 **"(6) "**，从设备的保险库中导入 seed。



在本教程中，我们决定按**"(1) "**键导入一个现有的 12 个字的 seed。这可以是您已经拥有的任何 seed BIP39，而且您显然有备份。



使用键盘输入 seed 的 12 个单词。在本例中，我们选择 seed 有效词组 beef x 12。然后按 **"ENTER "**。


*注意：如果您没有备份本 seed，您将无法修改设备上的 "联合签名 "设置，以更改您的消费条件*。



现在设备上的 "联合签名 "功能已激活。接下来，我们需要选择消费条件，然后完成多重签名 Wallet 的创建。



![Co-Sign](assets/fr/03.webp)



### 2- 选择支出条件或 "*支出政策*"



在这里，我们指定了**"C Key "**或**"Spending Policy Key**"签署交易时必须满足的支出条件。



在**"共同签署 "**菜单中，点击**"支出政策**"。



然后，您可以选择最大值，即单笔交易可花费的最大卫星数。



在本例中，我们将选择最大幅值为 **21212** 卫星。点击**"ENTER "**确认。




![Co-Sign](assets/fr/04.webp)



然后，我们选择设置最大速度，即设备在单位时间内能够签署的交易数量。在本教程中，我们将选择无限速度，即不限制交易数量。




![Co-Sign](assets/fr/05.webp)



### 3- 创建 Wallet Multisig 2-on-N



除了设备的**主 seed** （密钥 A）和**"支出策略密钥 "** （密钥 C）外，我们还需要为 Wallet Multisig 选择第三个密钥，即**"备份密钥 "** （密钥 B）。



我们的 "B Key "必须通过 SD 卡或 ColdCardQ 的 QR 码导入。


为此，我们需要第二个 ColdCard Mk4 或 Q 设备，在该设备上使用我们的 "键 B"。



在装有 **"备份密钥 "**（例如 ColdCard Mk4）的第二个设备上，从主菜单转到 **"设置 "**，然后转到 **"Multisig Wallet"** ，最后转到 **"导出 Xpub "**。


(如果您的第二台设备是 ColdCardQ，您当然可以选择通过 QR 码导出 Xpub）。





![Co-Sign](assets/fr/06.webp)





在下一个屏幕中，插入 SD 卡并点击右下角的 **"验证 "** 按钮。然后点击 **"(1) "**，将文件保存到 SD 卡中。



文件名中将包含公钥指纹 (*fingerprint*)，格式为 `ccxp-0F056943.json`。




![Co-Sign](assets/fr/07.webp)



然后将 SD 卡插入 "初始 "ColdCardQ，导入我们的 "备份密钥"（密钥 B）。


在 "ColdCard Co-Signing（冷卡联合签名）"菜单中选择 "Build 2-of-N"，然后在下一个屏幕中点击**"ENTER "**，再点击**"ENTER "**，从 SD 卡中导入 "备份密钥"。



![Co-Sign](assets/fr/08.webp)



在下一个屏幕上，将 "账号 "留空（除非你很清楚自己在做什么），然后再次点击 **"回车 "**。



![Co-Sign](assets/fr/09.webp)



我们终于可以使用新的 Wallet Multisig 2-sur-3，其组成如下：



键 A= 冷卡 Q 主控 seed


密钥 B=备份密钥（刚从第二个冷卡设备导入）


密钥 C=支出政策密钥（如果用于签名，则施加预定义的支出条件）



## 与 Sparrow wallet 联合签名



如有必要，请参阅下面的教程以熟悉 Sparrow wallet 软件：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- 出口 Wallet Multisig 2-sur-3 至 Sparrow wallet



现在，我们需要将 Wallet Multisig 导出到 Sparrow，以便在那里放置第一颗卫星。



在 ColdCardQ 的主菜单中选择 **"设置 "**，然后选择 **"Multisig钱包 "**。


现在将显示 ColdCard 已知的 Multisig 钱包集，这里涉及的密钥数量为 "2/3"（2-sur3）。选择我们刚刚创建的 Multisig **"ColdCard联合签名 "**，然后点击**"ColdCard导出 "**。



![Co-Sign](assets/fr/10.webp)




最后，选择将 Wallet 导出到 Sparrow 的方法。在本例中，我们选择 SD 卡，将 SD 卡插入设备的插槽 A 后，点击 **"(1) "**。



![Co-Sign](assets/fr/11.webp)



然后在 Sparrow wallet 中选择 "导入 Wallet"。



![Co-Sign](assets/fr/12.webp)



然后点击 **"导入文件 "**。然后选择 SD 卡上的文件 ** "export-Coldcard_Co-sign.txt" **。



![Co-Sign](assets/fr/13.webp)



为您的 Wallet 取一个在 Sparrow 中显示的名称，并选择一个密码来加密您的 Wallet（或不加密）。



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



我们现在已经准备好接收第一颗卫星，并测试我们应用于 Wallet 的支出条件。



![Co-Sign](assets/fr/16.webp)



### 2- 测试预定义的支出政策



需要提醒的是，我们已经为 Wallet Multisig 确定了 21212 沙托希的最大值。这意味着，每次消费政策密钥（密钥 C）签署交易时，只有当消费金额小于或等于 21212 萨托希时，后者才有效。



让我们来测试一下。


首先，让我们点击 Sparrow 中的 "接收 "选项卡，在 Wallet 中放入几个 Satss，我们将在本教程中一直使用它。



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



然后，让我们通过模拟 50,000 Sats 的交易，尝试花费超过 21212 允许的卫星数。



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



使用 ColdCardQ 扫描代表*未签名*交易的二维码以导入交易后，屏幕上显示的内容是这样的。一条警告信息告诉我们，消费条件尚未满足。如果我们还是签署了交易，那么 2 个密钥（设备上的 seed 主密钥，而不是 "密钥 C"）中只有一个会签署。




![Co-Sign](assets/fr/23.webp)



在这里，将交易导入 Sparrow 后，我们可以看到只有一个签名应用到了交易中。



![Co-Sign](assets/fr/24.webp)




现在，让我们重复这个实验，但交易量为 21 000 个卫星，即小于我们为这个 Wallet 设定的最大量级（21212 Sats）。




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



让我们试着用 ColdCardQ 签署这笔交易。



这次没有问题，没有出现任何警告信息，而且当我们将已签名的交易导入 Sparrow wallet 时，这次已经应用了 2 个签名，使交易有效并可以分发。




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## 与双节棍共同签名



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- 网络 2FA 和白名单地址



在本段中，我们将使用双节棍与 Wallet Multisig 联署，并借此机会应用新的消费条件，看看效果如何。



转到 *Avanced Tools（高级工具） > ColdCard Co-Signing（冷卡联合签名）*。


我们需要输入 "消费政策密钥"，以便进入菜单更改消费条件。在本例中，我们输入 12 x "牛肉"。



出于与本教程相关的实际原因，我们决定保留 21212 Sats 的量级和最大 "限制速度"。另一方面，我们将使用**"白名单地址 "**菜单来限制可使用资金的地址。




![Co-Sign](assets/fr/31.webp)




扫描您希望添加到白名单的地址（我们选择 2 个）的相关二维码，然后点击 **"ENTER "**。连续按**"ENTER "**键验证地址后，我们可以看到已对Magnitude和受益人地址进行了限制。



![Co-Sign](assets/fr/32.webp)



最后，为了全面了解 "Co-Sign "提供的可能性，让我们激活 "Web 2FA "选项。


此功能可让您使用符合 TOTP RFC-6238 标准的应用程序，如 Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / 或 Aegis Authenticator，以增加额外的 Layer 安全性。



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

具体来说，在签署交易之前，您需要将您的 NFC 上网设备靠近您的 Coldcard。这将自动带您进入一个coldcard.com网页，要求您输入您申请的6位数代码。如果您输入了正确的代码，网页上会显示一个 QR 代码，您可以扫描以获取 ColdCardQ，或者在您的 Mk4 上输入一个 8 位数代码，授权您的设备签名。





![Co-Sign](assets/fr/33.webp)



扫描双重认证应用程序中显示的 QR 代码并添加 ColdCard Co-Sign (CCC) 账户后，系统会要求您输入 2FA 代码以验证一切正常。



在 NFC 设备背面输入您的 ColdCard。



![Co-Sign](assets/fr/34.webp)



在打开的网页上，输入您最喜欢的应用程序的 2FA 代码。然后扫描 ColdCardQ 显示的 QR 码（或输入 Mk4 显示的 8 位数代码）。



![Co-Sign](assets/fr/35.webp)




目前，我们已对规模（21212 Sats）、目标地址和双重验证施加了限制。



![Co-Sign](assets/fr/36.webp)



### 2- 输出 Wallet Multisig 2 对 3 至双节棍



这次让我们把 Wallet Multisig 2 对 3 输出到 Nunchuk 中，就像之前输出 Sparrow 一样。


转到 *设置 > Multisig 钱包 > 2/3: ColdCard Co-sign（冷卡联合签名） > ColdCard Export（冷卡导出）*。



![Co-Sign](assets/fr/10.webp)



这一次，点击同名的 ColdcardQ 按钮 **"NFC "**，选择 NFC 导出选项。



![Co-Sign](assets/fr/37.webp)



在 Nunchuk 中，如果您是第一次打开应用程序，请点击 **"恢复现有的 Wallet"**。



![Co-Sign](assets/fr/38.webp)



如果应用程序中已有 Wallet，请点击右上角的**"+"**，然后点击**"恢复现有 Wallet"**。



![Co-Sign](assets/fr/39.webp)




然后选择 **"从 COLDCARD 恢复 Wallet"**，再选择 **"Multisig Wallet"**。



![Co-Sign](assets/fr/40.webp)



最后，将智能手机背面轻触 ColdCardQ 的屏幕，即可通过 NFC 导入 Wallet。



![Co-Sign](assets/fr/41.webp)



我们的账户和之前通过 Sparrow wallet 存入的卫星币又回来了。



![Co-Sign](assets/fr/42.webp)



### 3- 测试预定义的支出政策



现在，让我们尝试进行一笔违反我们设定的 2 个消费条件的交易。 **我们尝试向一个尚未批准的 Address 发送超过 21212 Sats 的金额。



![Co-Sign](assets/fr/43.webp)



创建交易后，点击右上角的 3 个小圆点，将其导出到您的 ColdCard 中。



![Co-Sign](assets/fr/44.webp)



然后选择 **"通过 BBQR 导出 "**，并扫描 ColdCardQ 显示的二维码。



![Co-Sign](assets/fr/45.webp)



然后，ColdcardQ 会显示一个警告，当你滚动到屏幕底部时，就会发现这笔交易违反了消费条件。



**请注意，为了防止潜在的攻击者试图规避限制，该装置并没有告诉我们涉及哪些消费条件。




![Co-Sign](assets/fr/46.webp)



如果您仍然按**"ENTER "**键进行验证，则会出现代表已签名交易的二维码。如果在 Nunchuk 上导入，可以看到只应用了一个签名。



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






让我们执行完全相同的操作，但这次交易要遵守量级限制（21212 Sats），并将 Satoshis 发送到我们预先配置的 2 个地址之一。



我们将 Nunchuk 12121 Sats 发送到我们的 2 个地址之一。然后，我们按照之前的方法将交易导出到 ColdCard。



![Co-Sign](assets/fr/49.webp)




将未签名交易导入 ColdCardQ 后，让我们看看这次会显示什么。



屏幕上总是会出现警告，但这次滚动到屏幕底部，我们会看到需要通过 2FA 验证交易。设备要求我们将 ColdcardQ 靠近联网的 NFC 终端（智能手机或平板电脑），我们照做了。



![Co-Sign](assets/fr/50.webp)



智能手机上会打开一个网页，要求我们输入 2FA 验证码，多亏了 Proton Authenticator，我们输入了验证码。



![Co-Sign](assets/fr/51.webp)





然后扫描网页上出现的 QR 码，授权 ColdCard 签署交易。


现在，交易已由两个密钥签名，因此有效。



如果 ColdCardQ 启用了 "Push Tx "功能，您只需在智能手机背面轻轻一点，就可以直接向网络广播交易。



![Co-Sign](assets/fr/52.webp)




如果您没有激活 "Push tx"，请按下 ColdCardQ 上的 "QR "按钮，将已签署的交易显示为 QR 码，然后将其导入 Nunchuk，方法与上例相同。



![Co-Sign](assets/fr/53.webp)



这次我们注意到有 2 个签名已经应用，因此交易已准备好在 Bitcoin 网络上广播。



![Co-Sign](assets/fr/54.webp)




本教程到此结束，您将了解到 Coinkite 的 ColdCardQ 和 Mk4 设备中集成的 Co-Sign 功能所提供的各种可能性，以及通过 Sparrow 和 Nunchuk 等钱包使用该功能的情况。