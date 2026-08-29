---
name: COLDCARD Q - 专家
description: 使用 COLDCARD Q 的高级功能
---

> **⚠️ 紧急安全公告（2026年7月）— Coldcard 钱包正在被持续盗取。** Coldcard 设备种子生成过程中的一个固件漏洞，使攻击者无需你进行任何操作即可找出你的种子短语。**所有 Coldcard 型号均受影响：Mk3、Mk4、Mk5 和 Q。** 2026年7月30日，约 500 个钱包中被盗走大约 594 BTC，且攻击仍在持续。只有使用掷骰子方法生成的钱包才被认为是安全的，并且前提是你至少掷了 50 次骰子。如果你不知道、不记得或不确定你的种子是如何生成的，请将其视为已泄露，并**立即将资金转移**到种子并非在 Coldcard 上生成的钱包。请关注 Coinkite 的官方公告。请参阅我们的专门迁移教程：

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

![cover](assets/cover.webp)

在之前的教程中，我们介绍了 COLDCARD Q 的初始配置及其基本功能，适合初学者。如果您刚刚收到 COLDCARD Q 并且尚未进行设置，我建议您先阅读之前的教程，然后再继续阅读本教程：

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

本教程将专门介绍 COLDCARD Q 的高级选项，专为高级用户和注重安全的用户设计。事实上，COLDCARD 与其他硬件钱包的区别就在于其众多高级安全功能。当然，您无需使用所有这些选项。只需选择符合您安全策略的选项即可。

**警告**：错误使用某些高级选项可能会导致您的比特币丢失或硬件钱包损坏。因此，我强烈建议您仔细阅读每个选项的建议和说明。

开始之前，请确保您有 12 个 或 24 个单词的助记词的纸质备份，并通过以下菜单检查其有效性： `Advanced/Tools > Danger Zone > Seed Functions > View Seed Words`。

![CCQ](assets/fr/01.webp)

## BIP39 Passphrase（密语）

如果您不了解 BIP39 密语是什么，或者不太清楚它的工作原理，我强烈建议您事先阅读这篇教程，其中涵盖了理解使用密码短语相关风险所需的理论基础：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

请记住，一旦您在钱包中设置了密语，仅凭助记词不足以重新访问您的比特币。您需要同时使用助记词和密语。此外，每次解锁您的 COLDCARD Q 时，您都需要输入密语。这增强了安全性，因为即使您实际接触到 COLDCARD，并且知道 PIN 码，如果没有密语，也无法访问您的比特币。

在 COLDCARD 上，您有两种方式管理您的密语：

1. **传统输入方式：** 每次使用硬件钱包时，您都需要手动输入密语，就像使用其他硬件钱包一样。COLDCARD Q 配备全键盘，简化了这一操作。

2. **您可以选择加密密码短语并将其存储在 microSD 卡上。在这种情况下，每次使用 COLDCARD Q 时，您都需要将 microSD 卡插入其中。请注意，此 microSD 卡仅适用于您的 COLDCARD Q，并非备份。因此，您务必将密码短语的副本保存在纸质或金属等物理介质上。**

为了设置 BIP39 密语，请访问 "*Passphrase*" 选单。

![CCQ](assets/fr/02.webp)

使用键盘输入密语。请务必选择一个强大的密码（长且随机），并进行物理备份。

![CCQ](assets/fr/03.webp)

设置密码后，COLDCARD Q 将显示与该密码相关联的新钱包的主密钥指纹。请务必保存该指纹。将来当您使用设备时再次输入密码，就可以检查显示的指纹是否与您保存的指纹一致。这种检查可以确保您在输入密码时没有出错。

![CCQ](assets/fr/04.webp)

现在您可以按 “*ENTER*” 键将此密语应用到您的助记词中，并激活新钱包。如果您想将此密码短语保存到microSD 卡上，请将卡插入相应的插槽并按 “*1*” 键。

![CCQ](assets/fr/05.webp)

您的密语已生效。密钥印记会显示在主屏幕顶部。

![CCQ](assets/fr/06.webp)

每次解锁 COLDCARD Q 时，您都需要访问 “*Passphrase*” 选单，并按照上述方式输入您的密语，以便将其应用到设备中存储的助记词，并访问正确的比特币钱包。

![CCQ](assets/fr/07.webp)

如果您已将密码短语保存在 microSD 卡上，每次使用时，请将其插入 COLDCARD 并访问 “*Passphrase*” 选单。COLDCARD 将直接从 microSD 卡加载密语，因此您无需手动输入。点击 “*Restore Saved*”。
![CCQ](assets/fr/08.webp)

请检查加载的密语的长度和首字母是否正确。

![CCQ](assets/fr/09.webp)

确认显示的指纹与您的钱包指纹匹配，然后点击 "*Restore*"。

![CCQ](assets/fr/10.webp)

请注意，使用密语意味着您需要将由助记词和密语组合生成的新密钥导入到您的钱包管理软件（例如 Sparrow Wallet）中。为此，请按照此教程中的 “*在 Sparrow 上配置新钱包*” 步骤操作：

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## 解锁选项

COLDCARD 设备解锁过程也提供了多种选项。让我们来详细了解一下这些高级选项。

### Trick PIN

Trick PIN 是与初始设备配置时定义的密码不同的辅助密码。一旦在 COLDCARD 开机时输入该密码，就会触发预先配置的特定操作。您可以配置多个 Trick PIN 码，每个密码对应不同的操作。这些功能使您可以根据个人安全策略定制 COLDCARD。在遭遇人身威胁（例如抢劫，比特币社区通常称之为 “5 美元扳手袭击”）时，这些功能尤其有用。

为了启用 Trick PIN 码并将其与操作关联，请前往 `Settings > Login Settings > Trick PINs` 选单。

![CCQ](assets/fr/11.webp)

选择 "*Add New Trick*"。

![CCQ](assets/fr/12.webp)

设置与操作相关的 PIN 码，并记得保存。

![CCQ](assets/fr/13.webp)

然后选择每次输入此 Trick PIN 时自动执行的操作。以下是密码可执行的操作列表：


- "*Brick Self*：如果您输入 Trick PIN，此操作将销毁两个 COLDCARD Q 芯片，使设备完全无法使用。届时，您将无法转售、重复使用，甚至无法将其退还给 Coinkite。该设备将彻底报废。此功能可在遭遇抢劫时使用，使劫匪相信他永远无法访问您的比特币。**请注意**：如果没有助记词和密码的物理备份，您的比特币将永久丢失。

![CCQ](assets/fr/14.webp)


- "*Wipe Seed*"：此选单提供了多种删除种子的操作，即重置 COLDCARD 而不破坏它。与 “*Brick Self*” 选项不同，可以使用助记词的备份来重新配置设备。但是，如果没有此备份，您的比特币将会丢失。以下是可用的选项：
- "*Wipe & Reboot*"：删除种子并重新启动 COLDCARD，而不在屏幕上显示任何信息。
 - "*Silent Wipe*"：静默擦除种子，并解锁随机假钱包上的 COLDCARD，就好像什么也没发生一样。
 - "*Wipe -> Wallet*"：谨慎地删除种子并解锁预配置的辅助钱包上的 COLDCARD，该钱包被设计为诱饵。该钱包可能包含您的比特币储蓄的一小部分，以满足攻击者的需要。
 - "*Say Wiped, Stop*"：删除种子并在屏幕上显示消息 `Seed is wiped, Stop`。

![CCQ](assets/fr/15.webp)


- "*Duress Wallet*"：通过此操作，Trick PIN 可以使用 BIP85 解锁从种子派生的钱包。这个二级钱包可以用作满足攻击者的诱饵。COLDCARD 的行为就像真正的钱包一样，但如果没有主 PIN（与 Trick PIN 不同），攻击者将永远无法访问真正的钱包。这一策略旨在让人们相信与 Trick PIN 相关联的钱包是唯一存在的。

![CCQ](assets/fr/16.webp)


- "*Login Countdown*"：此选单将操作与执行前的倒计时进行分组。**警告**，其中一些可能会损坏您的设备或导致您的比特币丢失。以下是可用的子操作：
- "*Wipe & Countdown*"：从 COLDCARD 内存中清除种子，然后开始一小时倒计时。如果不保存您的助记词或密码，您的比特币将会丢失。此选项旨在欺骗攻击者，让他们认为设备将在倒计时结束时解锁，而实际上它将重置为出厂设置。
 - "*Countdown & Brick*"：开始一小时倒计时，最后 COLDCARD 会破坏其两个安全芯片，使其永久无法使用。如果没有备份，您的比特币将会丢失。此操作旨在欺骗攻击者，攻击者认为自己正在等待解锁，而实际上设备会自毁。
 - "*Just Countdown*" ：触发一个简单的一小时倒计时，之后 COLDCARD 重新启动，无需任何进一步操作。种子不会被删除，设备保持完好。请小心不要将此操作与 “*Login Countdown*” 选项混淆，将在以下部分中讨论，该选项会在允许访问真实钱包的同时向主 PIN 添加倒计时。

![CCQ](assets/fr/17.webp)


- "*Look Blank*"：此操作使 COLDCARD 显示为空，给人以种子已被删除的印象。事实上，什么也没有发生，种子完好无损。这模拟未使用或重置的 COLDCARD。

![CCQ](assets/fr/18.webp)


- "*Just Reboot*"：使用 Trick PIN 时，COLDCARD 只需重新启动即可。不执行其他操作。

![CCQ](assets/fr/19.webp)


- "*Delta Mode*"：这种复杂的操作是为有经验的用户保留的，旨在对抗高度复杂的胁迫攻击，无论是来自国家还是拥有特权信息的亲戚。当激活 Delta Mode 时，COLDCARD 提供对真实钱包的访问，使攻击者能够导航并验证它是否是正确的钱包。然而，交易签名被阻止，从而阻止任何比特币转移。此外，对助记词的访问被禁用，任何检索助记词的尝试都将导致其被删除。为了增强可信度，与 Delta Mode一起使用的 Trick PIN 必须与真实 PIN 共享相同的前缀（以显示相同的反网络钓鱼字样），但后缀必须不同。

![CCQ](assets/fr/20.webp)

选择操作后，请确认您的选择。

![CCQ](assets/fr/21.webp)

然后，您可以在专用选单中查看所有配置的 Trick PIN。

![CCQ](assets/fr/22.webp)

通过选择现有的 Trick PIN，您可以检查关联的操作。您还可以使用 “*Hide Trick*” 隐藏它，使其在 Trick PIN 选单中不可见。您可以通过单击 "*Delete Trick*" 将其删除，或者更改 PIN 码，同时保留 “*Change PIN*” 的相关操作。

![CCQ](assets/fr/23.webp)

通过 "*Trick PIN*" 选单中的 "*Add If Wrong*" 选项，您可以配置特定操作，在尝试输入主 PIN 码一定次数错误后自动触发。允许的尝试次数可在配置过程中设置。

### Scramble Keys

输入 PIN 码时，"Scramble Keys" 选项可以扰乱键盘按钮上显示的数字。即使在有人或摄像头监视的情况下，该功能也能保护 PIN 码的机密性。

要激活该选项，请访问菜单 "设置 > 登录设置 > 乱码键"。

![CCQ](assets/fr/24.webp)

选择 "*Scramble Keys*" 选项。

![CCQ](assets/fr/25.webp)

从现在起，当您解锁 COLDCARD Q 时，每次使用键盘上的按键时都会随机分配新的数字。

![CCQ](assets/fr/26.webp)

### Login Countdown

此选项使您可以在每次尝试解锁 COLDCARD 时强制执行系统倒计时。它可以集成到您的安全策略中，方法是在发生盗窃时延迟对设备的访问，或者在签署交易之前施加延迟，例如在发生抢劫时保护自己。但是，此倒计时适用于您的所有使用，包括当您合法使用 COLDCARD 时，这也要求您保持耐心。请注意不要将此选项与 “*Just Countdown*” 操作混淆，该操作仅在使用特定 Trick PIN 时才会激活。

为了配置此选项，请访问 `Settings > Login Settings > Login Countdown` 选单。

![CCQ](assets/fr/27.webp)

选择倒计时时间。例如，如果您选择 1 小时，则每次尝试解锁 COLDCARD Q 都必须等待 1 小时。

![CCQ](assets/fr/28.webp)

每次解锁时，系统都会提示您输入 PIN 码。

![CCQ](assets/fr/29.webp)

然后等待倒计时设定的时间。

![CCQ](assets/fr/30.webp)

倒计时结束时，您需要再次输入 PIN 码才能访问设备。

![CCQ](assets/fr/31.webp)

### Calculator Login

此选项允许您在解锁时将 COLDCARD 伪装成计算器。要激活此功能，请访问选单 `Settings > Login Settings > Calculator Login`.

![CCQ](assets/fr/32.webp)

选择该选项，将其激活。

![CCQ](assets/fr/33.webp)

从现在起，每次打开设备时，都会显示一个包含基本命令的计算器。

![CCQ](assets/fr/34.webp)

例如，您可以计算 "*Plan ₿ Academy*" 的 SHA256 哈希值。

![CCQ](assets/fr/35.webp)

为了从计算器模式解锁 COLDCARD，请首先输入您的 PIN 码前缀，后跟破折号（-）。例如，如果您的 PIN 码是 `00-00`（此代码较弱，仅作为示例，因此请选择强 PIN 码），请输入 `00-`。然后，COLDCARD 将显示您的两个反网络钓鱼词。

![CCQ](assets/fr/36.webp)

然后输入完整的 PIN 码，中间用空格或破折号隔开，例如：`00 00`。

![CCQ](assets/fr/37.webp)

然后 COLDCARD 将退出计算器模式并正常解锁。

## 彻底销毁您的 COLDCARD

如果您打算处置 COLDCARD Q，例如因为您现在正在使用另一个硬件钱包，则正确销毁该设备非常重要。这可确保第三方无法恢复与您的钱包相关的信息。

信息销毁分为三个级别，具体取决于您的需求。在开始之前，请确保您的钱包已导入另一个硬件钱包，您可以访问您的所有资金，最重要的是，您拥有助记词和任何密码，两者都有效。如果没有钱包备份，您的 COLDCARD 被破坏将导致您的比特币丢失。

第一级破坏包括仅删除种子。此选项将从 COLDCARD 内存中删除您的助记词，同时保持设备正常运行。如果您想稍后再次使用 COLDCARD Q，这是理想的选择。要从内存中删除种子，请访问 `Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed` 选单。

![CCQ](assets/fr/38.webp)

第二级破坏包括通过软件永久禁用 COLDCARD 的两个安全芯片。此操作会使设备完全无法使用。您将无法转售、重复使用或将其退还给 Coinkite：它将被永久销毁。要继续，请按照上一节中介绍的相关 “*Brick Me*” PIN 码的步骤进行操作，然后在解锁 COLDCARD 时有意输入该 PIN 码。

第三级涉及对 COLDCARD Q 安全组件的物理破坏。和以前一样，这将使设备不可挽回地无法使用。为此，请使用钻头在设备右上角（翻转后）的两个芯片上靠近 “*SHOOT HERE*” 铭文的位置打一个孔。

**重要预防措施**：


- 为避免触电风险，请在操作前从设备中取出电池并拔下电源插头。
- 关闭设备后等待几分钟，然后再开始钻孔。
- 佩戴绝缘手套和护目镜以确保您的安全。

![CCQ](assets/fr/39.webp)

一旦芯片被打孔，请勿尝试重新连接 COLDCARD Q。

恭喜，您现在已经掌握了 COLDCARD Q 的高级选项！

如果您发现本教程有用，如果您能在下面留下一个园艺拇指，我将非常感激。请随意在您的社交网络上分享本教程。非常感谢！

我还推荐另一个教程，其中我们讨论了 CCQ 的直接竞争对手 Ledger Flex 的使用：

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a
