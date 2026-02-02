---
name: Ashigaru - Stowaway
description: 如何在 Ashigaru 上进行 Payjoin 交易？
---
![cover](assets/cover.webp)



> *迫使区块链间谍重新思考他们自以为知道的一切*。

Payjoin 是一种 Bitcoin 交易结构，旨在通过与收款人的直接合作来提高用户的保密性。目前有几种实现方法可促进其实施并使流程自动化。其中最著名的无疑是 Stowaway，它最初由 Samurai Wallet 团队开发，现已集成到其 fork Ashigaru 中。



## Stowaway 是如何工作的？



如前所述，Ashigaru 集成了名为 "Stowaway "的 PayJoin 工具。该工具可在安卓系统的 Ashigaru 应用程序中使用。要进行 Payjoin，收款人（同时也是合作者）必须使用与 Stowaway 兼容的软件，即目前只能使用 Ashigaru。



Stowaway 基于 Samurai 称为 "Cahoots "的一类交易。Cahoot 是几个用户之间的合作交易，涉及 Bitcoin 区块链之外的信息交换。Ashigaru 目前提供两种 Cahoots 工具：Stowaway（Payjoins）和 StonewallX2。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots 交易要求用户之间交换部分已签名的交易。这个过程可能既漫长又繁琐，尤其是在远程操作的情况下。不过，如果合作者在同一地点，还是可以手动完成。具体来说，就是连续扫描两个参与者之间交换的五个 QR 码。



如果距离较远，这种方法就会变得过于复杂。为了解决这个问题，萨莫拉公司开发了一种基于 Tor 的加密通信协议，名为 "*Soroban*"。有了 Soroban，Payjoin 所需的交换就可以在后台自动进行。



这些加密通信需要 Cahoot 参与者之间的连接和验证。这就是 Soroban 依赖用户 Paynyms 的原因。如果您还不了解 Paynyms 的工作原理，请参阅本专门教程了解更多信息：



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

简而言之，Paynym 是与您的 wallet 相关联的唯一标识符，使您能够激活各种功能，包括加密交换。它的形式是一个标识符，并附有插图。例如，我在 Testnet 上使用的就是这种形式：



![Image](assets/fr/01.webp)



**总结：**





- payjoin" = 特定的协作交易结构；





- `Stowaway` = 在 Ashigaru 上实现 Payjoin；





- `Cahoots` = Samourai 对其所有合作交易类型的称呼，特别是 Payjoin "Stowaway"，今天在 Ashigaru 上被接管；





- soroban = 在 Tor 上建立的加密通信协议，允许在 "Cahoots "交易中与其他用户协作；





- paynym"=唯一的 wallet 标识符，用于与 "Soroban "上的另一个用户建立通信，以进行 "Chahoots "交易。



要想更深入地了解 Payjoins 的工作原理及其在链上隐私保护中的作用，我推荐另一篇教程：



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## 如何在 Paynyms 之间建立连接？



要开始使用，您当然需要安装 Ashigaru 并创建 .NET Framework 3.0：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

要通过 Ashigaru 进行远程 Cahoots 交易，包括 PayJoin（*Stowaway*），您必须首先使用 Paynym "关注 "您希望合作的用户。在偷渡的情况下，这意味着要关注您希望向其发送比特币的人。如果你还不知道如何关注另一个 Paynym，你可以在本教程中找到详细步骤：



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## 如何在 Ashigaru 上进行 Payjoin？



要进行 Stowaway 交易，请单击屏幕左上角的 Paynym 图像，然后打开 "协作 "菜单。与您一起参与交易的人也必须这样做，除非您亲自交换 QR 码。



![Image](assets/fr/02.webp)



您有两个选项：如果您是付款人，请选择 "发起"；如果您是收款人，请选择 "参与"。



![Image](assets/fr/03.webp)



如果您是收件人，操作步骤非常简单。要通过 Soroban 网络进行远程协作，请单击 "参与"，选择要使用的账户，然后按 "等待 CAHOOTS 请求"，等待付款人发送请求。



![Image](assets/fr/04.webp)



另一方面，如果要通过二维码扫描进行面对面合作，请进入 wallet 主页，按屏幕上方的二维码图标，然后扫描发起交易的付款人提供的二维码。



![Image](assets/fr/05.webp)



如果您是付款人角色，即发起交易的人，请转到 "协作 "菜单，然后选择 "发起"。



![Image](assets/fr/06.webp)



对于交易类型，由于我们希望进行 Payjoin 偷渡，因此请选择该选项。



![Image](assets/fr/07.webp)



然后，您可以选择在线协作（*Cahoots*，通过*Soroban*）或面对面协作（交换二维码）。



![Image](assets/fr/08.webp)



### 在线 Cahoots



如果您选择了 "在线 "选项，则从您关注的 Paynyms 中选择收件人。



![Image](assets/fr/09.webp)



点击 "设置交易"，然后选择要支出的账户。



![Image](assets/fr/10.webp)



在下一页，输入交易详情：发送给收件人的金额和收费率。无需输入收款地址，因为收款人会在 PSBT 交换时自行发送地址。



然后点击 "查看交易设置"。



![Image](assets/fr/11.webp)



仔细核对信息，确保您的合作者正在监听*Cahoots*请求，然后点击绿色的 "开始交易 "按钮，通过索罗班启动 PSBT 交换。



![Image](assets/fr/12.webp)



等到两个参与者都签署了交易，然后在 Bitcoin 网络上广播。



![Image](assets/fr/13.webp)



### 面对面讨论



如果您希望亲自进行兑换，请选择 "STONEWALL X2 "交易类型，然后选择 "亲自/手动 "选项。



![Image](assets/fr/14.webp)



点击 "设置交易"，然后选择要支出的账户。



![Image](assets/fr/15.webp)



在下一页，输入交易详情：发送给收件人的金额和收费率。无需输入收款地址，因为收款人会在 PSBT 交换时自行发送地址。



然后点击 "查看交易设置"。



![Image](assets/fr/16.webp)



检查详细信息，然后按绿色的 "开始交易 "按钮，开始通过 QR 码扫描交换 PSBT。



![Image](assets/fr/17.webp)



交换是通过与合作者交替扫描完成的：点击 "SHOW QR CODE "向合作者显示您的 QR 代码，合作者将对其进行扫描。然后，他将点击 "SHOW QR CODE "显示他的二维码，你再用 "LAUNCH QR Scanner "扫描。重复这一过程，直到完成所有五个交换步骤。



![Image](assets/fr/18.webp)



完成所有交换后，检查交易详情，然后拖动屏幕底部的绿色箭头释放交易。



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96).其结构如下



![Image](assets/fr/20.webp)



*信用：[mempool.space](https://mempool.space/)*



如果我们对这笔交易进行分析，我们会看到输入端有我的 UTXO `164,211 sats`，以及属于实际收款人的 UTXO `190,002 sats`。在输出端，我收到的交换 UTXO 为 `63,995 sats`，而收款人收到的 UTXO 为 `290,002 sats`。比较投入和产出，我们可以看到，收款人确实赚取了 `100 000 sats`，这相当于我的实际付款额，而我则损失了 `100 000 sats`，我在其中加入了 mining 成本。



显然，我能描述这种结构，是因为我自己构建了这个事务。但对于外部观察者来说，无论是输入还是输出，一般都无法确定哪个 UTXO 属于哪个参与者。



要加深对 Bitcoin 上链隐私管理的了解，我建议您参加 Plan ₿ Academy 上的 BTC 204 培训：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c