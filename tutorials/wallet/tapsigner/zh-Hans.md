---
name: Tapsigner
description: 使用Nunchuk设置和使用Tapsigner
---
![封面](assets/cover.webp)

硬件钱包是一种专门用于管理和保护比特币钱包私钥的电子设备。与常安装在经常连接互联网的通用设备上的软件钱包（或热钱包）不同，硬件钱包允许物理隔离私钥，减少了被黑客攻击和盗窃的风险。

硬件钱包的主要目标是最小化设备的功能以减少其攻击面。较小的攻击面也意味着较少的潜在攻击向量，即系统中较少的弱点，攻击者可能利用这些弱点访问比特币。

特别是如果您持有大量比特币，无论是绝对价值还是占您总资产的比例，都推荐使用硬件钱包来保护您的比特币。

硬件钱包与计算机或智能手机上的钱包管理软件结合使用。这个软件管理交易的创建，但验证这些交易所必需的加密签名仅在硬件钱包内完成。这意味着私钥永远不会暴露于可能脆弱的环境中。

硬件钱包为用户提供双重保护：一方面，通过保持私钥离线，它们可以保护您的比特币免受远程攻击；另一方面，它们通常提供更好的物理抵抗力，防止尝试提取密钥。正是基于这2个安全标准，可以评判和排名市场上可用的不同模型。

在本教程中，我提议发现这些解决方案之一：Coinkite的Tapsigner。

## 介绍Tapsigner

Tapsigner是Coinkite公司设计的一种硬件钱包，形式为NFC卡，该公司也以生产Coldcards而闻名。

![TAPSIGNER NUNCHUK](assets/notext/01.webp)

Tapsigner允许存储一对由主私钥和链码组成的对，符合BIP32，以派生出一系列加密密钥。这些密钥可以用来通过将Tapsigner靠近手机或NFC卡读取器来签署交易。
这种NFC卡的售价为19.99美元，与市场上其他硬件钱包相比非常实惠。然而，由于其格式，Tapsigner没有提供像其他设备那样多的选项。显然，由于它是一张卡，所以没有电池、没有相机，也没有微SD卡读取器。在我看来，它最大的缺点是硬件钱包上缺少屏幕，这使它更容易受到某些类型远程攻击的威胁。实际上，这迫使用户盲目签名，并信任他们在计算机屏幕上看到的内容。

尽管有其局限性，但由于价格低廉，Tapsigner可能很有趣。这个钱包可以特别用来增强支出钱包的安全性，除了使用带屏幕的硬件钱包保护的储蓄钱包。对于那些持有少量比特币且不希望在更复杂的设备上投资数百欧元的人来说，它也代表了一个好的解决方案。此外，将Tapsigner用于多签配置，或者将来可能用于带有时间锁的钱包系统，可以提供有趣的好处。

## 如何购买Tapsigner？

Tapsigner可以在[官方Coinkite网站](https://store.coinkite.com/store/category/tapsigner)上购买。要在实体店购买，您也可以在该网站上找到[认证经销商的列表](https://coinkite.com/resellers)。
您还需要一部与NFC通信兼容的手机，或者一个USB设备来以标准频率13.56 MHz读取NFC卡。
## 如何初始化带有Nunchuk的Tapsigner？

收到您的Tapsigner后，第一步是检查包装确保它未被打开。如果包装受损，可能表明卡已被泄露，可能不是正品。CoinKite会用一个阻挡无线电波的盒子交付您的Tapsigner。确保它在您的包裹中。

![TAPSIGNER NUNCHUK](assets/notext/02.webp)

为了管理钱包，我们将使用**Nunchuk Wallet**移动应用程序。确保您的智能手机兼容NFC，然后从[Google Play商店](https://play.google.com/store/apps/details?id=io.nunchuk.android)、[App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073)或直接通过其[`.apk`文件](https://github.com/nunchuk-io/nunchuk-android/releases)下载Nunchuk。

![TAPSIGNER NUNCHUK](assets/notext/03.webp)
如果您是第一次使用Nunchuk，应用程序将提示您创建一个账户。出于本教程的目的，不需要创建一个。所以，选择“*继续作为访客*”以无账户方式继续。
![TAPSIGNER NUNCHUK](assets/notext/04.webp)

然后点击“*非辅助钱包*”。

![TAPSIGNER NUNCHUK](assets/notext/05.webp)

接下来，点击“*我将自己探索*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/06.webp)

进入Nunchuk后，点击“*钥匙*”标签旁的“*+*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/07.webp)

选择“*添加NFC钥匙*”。

![TAPSIGNER NUNCHUK](assets/notext/08.webp)

然后点击“*添加TAPSIGNER*”。

![TAPSIGNER NUNCHUK](assets/notext/09.webp)

点击“*继续*”，然后将您的Tapsigner NFC卡靠近您的智能手机。

![TAPSIGNER NUNCHUK](assets/notext/10.webp)

如果您的Tapsigner是新的，Nunchuk将提议初始化它。点击“*是*”。

![TAPSIGNER NUNCHUK](assets/notext/11.webp)

现在您需要选择如何生成您的主链代码。

Tapsigner使用BIP32标准。这意味着，保护您比特币的加密密钥的派生不依赖于像BIP39钱包那样的助记词短语，而是直接依赖于主私钥和主链代码。这两个元素通过HMAC函数传递，以确定性和层次性地派生出您钱包的其余部分。

主私钥由集成到您的Tapsigner中的TRNG（*真随机数生成器*）直接生成。另一方面，主链代码必须从外部提供。在这一步，您有一个选择：通过点击“*自动*”让Nunchuk自动生成它，或通过选择“*高级*”并在提供的字段中输入它来自己生成。
接下来，您需要选择一个PIN码。在“*初始PIN码*”区域，输入您的Tapsigner背面写着的PIN码。
![TAPSIGNER NUNCHUK](assets/notext/13.webp)

选择一个PIN码来保护您的Tapsigner的物理访问权限。这个PIN码在钱包恢复过程中不起作用。它的唯一功能是解锁您的Tapsigner以签署交易。确保保存这个PIN码以避免忘记它。点击“*继续*”以进行下一步。

![TAPSIGNER NUNCHUK](assets/notext/14.webp)
现在将您的Tapsigner卡放在手机背面以初始化它。
![TAPSIGNER NUNCHUK](assets/notext/15.webp)

Nunchuk接下来将为您的钱包生成恢复文件，这允许您在丢失NFC卡的情况下重新获得访问您的比特币的权限。这个文件用您的Tapsigner背面写着的备份码加密。要恢复您的比特币，您绝对需要这个文件以及解密它的代码。因此，重要的是要制作这个代码的纸质副本，因为如果您丢失了NFC卡，对这个代码的访问也将丢失，因为目前它只写在卡上。确保还创建您的加密恢复文件的多个备份。

![TAPSIGNER NUNCHUK](assets/notext/16.webp)

为您的钱包选择一个名称。

![TAPSIGNER NUNCHUK](assets/notext/17.webp)

您的钱包的基础现在已经设置好了。要随时验证您的Tapsigner的真实性，您可以点击“*运行健康检查*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/18.webp)

输入您的PIN码。

![TAPSIGNER NUNCHUK](assets/notext/19.webp)

然后将您的卡放在手机背面。

![TAPSIGNER NUNCHUK](assets/notext/20.webp)

## 如何在Tapsigner上创建一个钱包？

回到Nunchuk首页，您可以看到您的Tapsigner已在可用的签名设备中注册。

![TAPSIGNER NUNCHUK](assets/notext/21.webp)

您现在需要为您的比特币钱包生成密钥。为此，点击“*钱包*”标签右侧的“*+*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/22.webp)

点击“*创建新钱包*”。

![TAPSIGNER NUNCHUK](assets/notext/23.webp)

然后选择“*使用现有密钥创建新钱包*”选项。

![TAPSIGNER NUNCHUK](assets/notext/24.webp)

为您的钱包选择一个名称，然后点击“*继续*”。

![TAPSIGNER NUNCHUK](assets/notext/25.webp)

选择您的Tapsigner作为这组新密钥的签名设备，然后点击“*继续*”。

![TAPSIGNER NUNCHUK](assets/notext/26.webp)

如果一切都符合您的满意，确认创建。

![TAPSIGNER NUNCHUK](assets/notext/27.webp)
您可以保存您的钱包配置文件。这个文件仅包含您的公钥，这意味着即使有人访问到它，他们也无法窃取您的比特币。然而，他们可以追踪您的所有交易。因此，这个文件只对您的隐私构成风险。在某些情况下，它对于恢复您的钱包可能是必不可少的。![TAPSIGNER NUNCHUK](assets/notext/28.webp)

就这样，您的钱包成功创建了！

![TAPSIGNER NUNCHUK](assets/notext/29.webp)

当您不使用Tapsigner时，记得将其存放在Coinkite提供的盒子里，该盒子可以阻挡无线电波，以防止未经授权的读取。

## 如何在Tapsigner上接收比特币？

要接收比特币，请点击您的钱包。

![TAPSIGNER NUNCHUK](assets/notext/30.webp)

然后使用生成的地址来接收比特币。如果您之前在这个钱包上接收过比特币，您需要点击“*接收*”按钮来生成一个新的空白接收地址。

![TAPSIGNER NUNCHUK](assets/notext/31.webp)

一旦发送者的交易被广播，您将在您的钱包上看到它出现。

![TAPSIGNER NUNCHUK](assets/notext/32.webp)

点击“*查看币*”。

![TAPSIGNER NUNCHUK](assets/notext/33.webp)

选择您的新UTXO。

![TAPSIGNER NUNCHUK](assets/notext/34.webp)

点击“*标签*”旁边的“*+*”来给您的UTXO添加一个标签。这是一个好习惯，因为它帮助您记住您的币的来源，并为未来的支出优化您的隐私。

![TAPSIGNER NUNCHUK](assets/notext/35.webp)

选择一个现有的标签或创建一个新的，然后点击“*保存*”。您还可以创建“*集合*”来以更有结构的方式组织您的币。

![TAPSIGNER NUNCHUK](assets/notext/36.webp)

## 如何使用Tapsigner发送比特币？

现在您的钱包中有了比特币，您也可以发送它们。要做到这一点，请点击您选择的钱包。

![TAPSIGNER NUNCHUK](assets/notext/37.webp)

点击“*发送*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/38.webp)

选择要发送的金额，然后点击“*继续*”。

![TAPSIGNER NUNCHUK](assets/notext/39.webp)

添加一个“*备注*”到您未来的交易中，以记住其目的。

![TAPSIGNER NUNCHUK](assets/notext/40.webp)
接下来，手动在指定的字段中输入接收者的地址。
![TAPSIGNER NUNCHUK](assets/notext/41.webp)

您也可以通过点击屏幕右上角的图标来扫描编码的QR码地址。

![TAPSIGNER NUNCHUK](assets/notext/42.webp)

点击“*创建交易*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/43.webp)

验证您的交易详情，然后点击您的Tapsigner旁边的“*签名*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/44.webp)

输入您的PIN码以解锁它。

![TAPSIGNER NUNCHUK](assets/notext/45.webp)

然后将Tapsigner放在您的智能手机背面。
![TAPSIGNER NUNCHUK](assets/notext/46.webp)
您的交易现已签名。请最后再次检查一切是否正确，然后点击“*广播交易*”将其广播到比特币网络上。

![TAPSIGNER NUNCHUK](assets/notext/47.webp)

您的交易现在正在等待确认。

![TAPSIGNER NUNCHUK](assets/notext/48.webp)

## 如何在丢失Tapsigner的情况下恢复钱包？

如果您丢失了Tapsigner，您可以使用卡片背面记下的代码恢复您的钱包。因此，将此代码与Tapsigner分开保存很重要，因为如果卡片丢失，访问此代码的能力也将丢失。您还需要钱包的加密备份。

为了恢复，我们将使用Nunchuk应用程序，但请记住，这意味着暂时将您的资金保护在一个热钱包中。如果您的Tapsigner保护了大量资金，考虑使用新的Coldcard遵循相同的恢复过程。

打开Nunchuk应用程序，然后点击“*Keys*”标签旁的“*+*”按钮。

![TAPSIGNER NUNCHUK](assets/notext/49.webp)

选择“*添加NFC密钥*”。

![TAPSIGNER NUNCHUK](assets/notext/50.webp)

选择“*从备份恢复TAPSIGNER密钥*”选项。

![TAPSIGNER NUNCHUK](assets/notext/51.webp)

然后，您将被重定向到您设备的文件资源管理器。定位并选择您钱包的加密备份文件。通常，此文件的名称以`backup...`开头。

![TAPSIGNER NUNCHUK](assets/notext/52.webp)

输入解密备份文件的密码。此密码对应于最初记在您的Tapsigner背面的密码。

![TAPSIGNER NUNCHUK](assets/notext/53.webp)
然后为您的恢复钱包选择一个名称。
![TAPSIGNER NUNCHUK](assets/notext/54.webp)

您现在已重新获得对您比特币的访问权限。您的钱包现在作为热钱包在Nunchuk应用的“*Keys*”标签中管理。接下来，您需要在“*Wallets*”部分创建一组新的加密密钥，并将此密钥与之关联。为此，您可以在本教程的“*如何在Tapsigner上创建钱包？*”部分再次遵循步骤。

![TAPSIGNER NUNCHUK](assets/notext/55.webp)

如果您丢失了Tapsigner，我强烈建议您立即将您的比特币转移到您拥有的另一个钱包，理想情况下是由硬件钱包保护的钱包。实际上，您丢失的Tapsigner可能落入了错误的手中。因此，重要的是要清空您刚刚恢复的钱包，并停止使用它。

恭喜您，现在您已经掌握了使用Tapsigner的方法！如果您觉得本教程有帮助，我将非常感激您能在下方留下点赞。欢迎在您的社交网络上分享本文。非常感谢！