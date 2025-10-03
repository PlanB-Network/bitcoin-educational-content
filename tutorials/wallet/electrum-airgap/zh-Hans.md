---
name: Electrum Airgap
description: 通往安全的第一步，使用Electrum的冷钱包
---
![cover](assets/cover.webp)



## Cold Wallet



在本教程中，我将介绍如何在没有专用 Hardware Wallet 的情况下，制作第一个断开互联网连接的气隙签名设备。您只需准备两台电脑即可：




- 旧设备将永远无法连接互联网；
- 您日常使用的电脑。



与传统的 "Hot Wallet "相比，这种配置具有更高的安全性：旧电脑（没有网络连接）保管着你的私人密钥，这些密钥永远不会暴露在互联网上，而是离线存储（"airgap "或 "Cold"）。



取而代之的是在日常使用的电脑上安装一个 Wallet 显示器（"专用手表"），它与网络连接，您可以用它来检查余额和准备收据交易等。



## Wallet 气隙：内容和方法



通过执行本指南中的步骤，我们将在两台不同的电脑上安装两个 Software Wallet Electrum，并最终创建两个具有不同密钥库的钱包：Wallet airgap 将使用 Wallet HD 的整个层次结构，而 Wallet display 将使用主公钥生成。



这两个钱包在各方面都非常不同。我们将看到，它们唯一的共同点就是地址：




- airgap 计算机上的 gW-13 只能签名，但由于断开了网络连接，不知道所使用的余额和地址；
- 在没有私人密钥的情况下，日常计算机上的 Wallet 只能准备和传播交易，而不能处置支出。



## 初步准备工作



要下载 Electrum，我建议您按照本教程的第一个步骤操作：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

下载后，在安装之前一定要验证版本，然后进行 "一台服务器 "配置，您可以在帮助部分的 "从虚拟 Wallet 开始 "中找到这一点。



只有安装在日常计算机上的 Wallet 才需要进行 "一台服务器 "配置操作，因为另一台计算机将始终处于离线状态。



下面的操作涉及在两台不同的电脑（和钱包）上进行练习，因此为了方便和突出重点，我选择将 Wallet airgap 设置为浅色主题，而 Wallet 显示屏则设置为深色主题。



## Wallet 气隙创建



下载并验证下载的 Electrum 后，复制一份可执行文件并将其带到离线电脑上。然后启动并安装 Electrum。



双击启动 Electrum：使用 Wallet 的计算机处于离线状态，请忽略网络设置，直接创建 Wallet，在本指南中，我们称其为 "airgap"。



![image](assets/en/01.webp)



选择_标准钱包_。



![image](assets/en/02.webp)



然后选择 _Create a new seed_（创建新种子），让软件 generate Mnemonic。



![image](assets/en/03.webp)



将来自 Electrum 的 12 个 generate 单词准确地抄写到纸底，然后进行验证步骤，在 Electrum 要求时按顺序重新输入单词。



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Wallet 创建完成后，设置一个复杂的密码（"Strong"）来加密气隙设备上的 Wallet 文件。这一步非常微妙和重要，因为现在选择的密码可以防止访问具有支配权的 Wallet，使其能够花费资金签署交易。



![image](assets/en/06.webp)



点击 "完成"，Wallet 即被定义并显示在屏幕上。当然，网络连接指示器（即右下角的彩点）是红色的，因为计算机已断开连接，不允许 Wallet 显示联机键。



![image](assets/en/07.webp)



## 创建 Wallet 可视化



现在，您的 Wallet 已拥有离线私人密钥，您需要设置一个显示 Wallet，或 "纯手表"，它将允许您查看余额，并准备收据交易，以继续安全地积累 Sats。



从位于离线设备上的 Wallet，选择 _Wallet_ -> _Information_ 菜单



![image](assets/en/08.webp)



包含所有 Wallet 信息的窗口将出现，您可以在其中选中 "衍生路径 "和 "主指纹"，例如将它们标记在 Mnemonic 句子中的单词旁边（强烈建议）。



![image](assets/en/09.webp)



请记住，您是从一台未连接的计算机上获取这些数据的，因此您必须将 `zpub` 复制/粘贴到文本文件中，然后保存到 USB 盘中。



现在，您可以移动到连接到互联网的电脑上，启动 Electrum 并创建一个新的 Wallet。



从 _File_ 菜单中选择 _New/Restore_。



![image](assets/en/10.webp)



新的 Wallet 只供查看，因此本指南将称之为 "只供观看"。



![image](assets/en/12.webp)



在下一个屏幕中选择_标准钱包_，然后点击_下一步_。



![image](assets/en/13.webp)



在选择 "密钥库 "时要注意：要创建显示 Wallet，请选择_使用主密钥_。然后继续_下一步_。



![image](assets/en/14.webp)



在此处粘贴从 Wallet 脱机复制的`zpub`，您已通过 USB 媒体将其带入此计算机。



![image](assets/en/15.webp)



最后，也为这个 Wallet 设置一个强密码，可能不同于为相应的 Cold 选择的密码。



您将看到 Wallet 显示屏出现，并伴有警告。该信息提醒您，这是仅供显示的 Wallet，您不能使用它来花费相关资金。



**注意**：*因此*，您需要始终拥有私人密钥来处理该 Wallet 的 UTXO。有了一个良好的备份系统，您就不难继续完全拥有您的比特币了。



![image](assets/en/16.webp)



每次打开 Wallet 时都会出现该警告。点击 "确定"，进入验证步骤。



## 两个 Wallet 的验证



正如我们在本指南开头所学到的，Wallet 气隙及其显示屏 Wallet 是两个具有不同功能但**共享相同地址**的组合。



如果我们把这两个钱包并排起来看，就会发现在 Wallet 气隙中有一个 "seed "符号，而在纯手表中则没有。即使是这个细节也能帮助您记住，Wallet 显示屏 Wallet 没有私钥。



![image](assets/en/17.webp)



不过，要进行准确的首次检查，请在两个钱包中都选择 "地址 "菜单：由于它们共享相同的地址，因此两个钱包的地址列表应完全相同。



![image](assets/en/18.webp)



⚠️ **注意**： **不能有中间地带；地址必须相同。如果地址不同，则必须删除所有已完成的工作并重新开始**。



现在你可以进行两种不同的检查。首先，尝试删除两个钱包，然后在相应的电脑上从头开始恢复。如果要进行此验证，显示 Wallet 的程序与上述程序相同。



但是，对于 Wallet 气隙，您必须在 "键库 "屏幕上选择_我已经有一个种子_，然后从纸质备份中复制单词输入。



在 "免充值 "试用结束后，您可以尝试进行小额交易，并立即消费。



## 收支交易



要开始使用您的电子货币气垫，您可以先用小额资金进行收据交易，然后将其用于购买自己的 Address。然后，您就可以熟悉程序，验证自己是否完全控制了资金。



**注意**：我不建议您在确信可以顺利进行所有操作之前在 Wallet 上存入大量资金。



下面介绍的步骤乍一看可能很复杂。不要因此而沮丧：当你第一次尝试时，你会发现完成这些步骤只需要几分钟。



要接收资金，您必须使用连接到互联网的计算机上的显示屏 Wallet。在 "接收 "菜单中点击 "创建请求"，让 Electrum generate 显示第一个可用的 Address，并用它向我们发送几个 Satss。



![image](assets/en/19.webp)



![image](assets/en/20.webp)



一旦交易被传播，您就可以看到--很自然地--它只在 Wallet 显示屏上可见，而不是在 Wallet 气隙上。



![image](assets/en/21.webp)



在您的交易得到确认后，您可以准备费用，从而尝试从 Wallet 网络外签署程序。然后在专用监视器上准备交易，并按_Preview_键进行检查



![image](assets/en/22.webp)



你可以在高级交易窗口中看到这一点：




- 交易未签名（`Status: Unsigned）；
- 标志 "和 "广播 "命令被禁止。



您唯一能做的就是原样导出交易，将其带到 Wallet 气隙并签署。



将 USB 闪存盘插入电脑，然后从左下角的菜单中选择 _Share_（共享）。



![image](assets/en/23.webp)



然后选择_保存到文件_。



![image](assets/en/24.webp)



将交易保存到 USB 盘。



您会注意到，Electrum 给文件起了个名字，第一个数字是 transaction ID，文件扩展名为`.PSBT`，意思是`Partially Signed Bitcoin Transaction`。



提取带有`.PSBT`文件的媒体，并将其离线连接到计算机。



现在从 Wallet 气隙中选择 _Tools_ 菜单，然后选择 _Load transaction_ 和 From file_。



![image](assets/en/25.webp)



使用文件管理器，从其位置选择 `.PSBT`。



![image](assets/en/29.webp)



离网计算机软件将自动打开高级交易窗口，与您在 Wallet 显示屏上看到的完全相同。状态是 "未签署"，但不同的是，这里的 "签署 "命令是激活的。这正是您需要执行的命令。



![image](assets/en/26.webp)



![image](assets/en/27.webp)



现在交易已经签署，请记住您的 Wallet 是在离线机器上。因此，即使您看到 "广播 "命令处于活动状态，您的 Wallet 也无法将事务传播到 Bitcoin 网络。



现在您需要做的是重复将已签名的事务导出到 USB 记忆棒的操作，以便将其导入到连接到互联网的计算机中并进行传播。



从左下角菜单再次选择_共享_，然后选择_保存到文件_。



![image](assets/en/28.webp)



现在文件的扩展名不同了： **现在交易的扩展名不是 `.PSBT`，而是 `.txn`。从现在起，Electrum 将让你识别已签名交易和未签名交易**。



![image](assets/en/30.webp)



为了最终传播交易，请将 USB 棒从离线计算机中取出，插入连接到互联网的计算机中。



从 "只看不买 "中重复导入步骤，即从_工具_菜单中选择_载入交易_，最后选择_从文件_。



![image](assets/en/31.webp)



Electrum 会为你打开交易窗口，与之前在 Wallet 上显示的窗口有明显不同，现在已经签名（"Status: Signed"），并且可以使用 "Broadcast "命令。



您需要做的最后一项操作就是这样：



![image](assets/en/32.webp)



## 结论



现在您的测试已经完成。如果您按照指南操作并得到了相同的结果，那么您已经在两台不同的电脑上用 Electrum 创建了一个 Wallet Cold，您可以用它来存储比特币。



您需要密切注意的只有两点：


1) **切勿使用 Wallet 气隙连接到 generate 接收地址**。因为它是离线的，所以它总是会向您提供第一个 Address，这与您刚刚用来进行测试交易的 Address 不谋而合；



![image](assets/en/33.webp)



从上图可以看出，离线的 Wallet 不知道自己的 Address 历史。在这方面，它是完全盲目的。 **它能为您做的唯一工作就是存储您的离线密钥和签署您的交易**_。



2) 使用专用 U 盘，**不要使用经常使用的介质**。日常使用的工具更容易受到网络攻击，甚至可能在无意中攻击你断开网络连接的电脑。你只用于此目的的 U 盘与你的电脑在线接触的机会很少，特别是如果你是一个不需要花钱的 "宅男"，这样就减少了接收和传播病毒、恶意软件等的可能性。