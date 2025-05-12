---
name: Trezor U2F 和 FIDO2
description: 使用 Trezor 加强在线安全
---
![cover](assets/cover.webp)



Trezor 设备是一种硬件钱包，最初设计用于保护 Bitcoin Wallet 的安全，但它们也具有在网络上进行强身份验证的高级选项。由于与**U2F**和**FIDO2**协议兼容，它们使您无需完全依赖密码即可安全访问在线账户。



U2F（*通用第二因素*）协议由谷歌和 Yubico 于 2014 年推出，随后被 FIDO 联盟标准化。它可以在登录时添加第二个物理验证因素（2FA）。一旦激活，除了传统的密码外，用户还必须通过按下 Trezor 上的一个按钮来批准每次连接其账户的尝试。在这种情况下，Trezor 的工作方式与 Yubikey 类似。



这种方法基于非对称加密技术：不传输秘密数据，使网络钓鱼或拦截攻击无效。目前，许多在线服务都支持 U2F。



除了能实现双因素身份验证的 U2F 外，Trezors 还支持 FIDO2（*快速身份在线 2.0*），它是 U2F 的进化版。这是 2018 年推出的标准化身份验证协议，它扩展了 U2F 的逻辑，旨在完全取代密码。它基于两个组件： *WebAuthn*（浏览器端）和*CTAP2*（物理密钥端）。FIDO2 实现了 "无密码 "身份验证：用户只需通过 Trezor 设备识别自己的身份，该设备是唯一的加密令牌，无需额外的密码。该协议现在与许多在线服务兼容，特别是那些面向企业的服务。



除了 "无密码*"功能外，FIDO2 还能以类似 U2F 的方式实现双因素身份验证。



FIDO2 还引入了常驻凭证的概念，即直接存储在 Trezor 中的标识符，其中包括实现连接的私钥和用户的身份信息。这种机制实现了真正的免密码身份验证：只需插入 Trezor 并确认访问，无需输入身份信息或密码。相反，非驻留凭证则更为传统，只在设备中存储私钥；用户 ID 仍存储在服务器端，因此每次连接时都必须输入。稍后我们将讨论如何用 Trezor 保存这些凭证。



在本教程中，我们将了解如何激活 U2F 或 FIDO2 进行双因素身份验证，然后如何配置 FIDO2，以便无需密码直接使用 Trezor 访问账户。



**注：** U2F 兼容所有 Trezor 型号，但 FIDO2 仅支持 Safe 3、Safe 5 和 Model T，不支持 Model One。



## 在 Trezor 上使用 U2F/FIDO2 实现 2FA



开始之前，请确保已在 Trezor 上设置好 Bitcoin Wallet。正确保存 Mnemonic 非常重要，因为双因素身份验证中用于 U2F 和 FIDO2 的密钥都来自这个 Mnemonic。如果你的 Trezor 丢失或损坏，你可以通过在另一部 Trezor 设备上输入 Mnemonic 短语来恢复对密钥的访问（注意，对于 "*无密码*"模式下的 FIDO2 凭据，仅 seed 是不够的，我们将在接下来的章节中看到）。



将 Trezor 连接到电脑并解锁。



![Image](assets/fr/01.webp)



使用双因素身份验证访问您要保护的账户。例如，我要使用 Bitwarden 账户。你通常可以在服务设置中的 "*身份验证*"、"*安全*"、"*登录*"或 "*密码*"选项卡下找到 2FA 选项。



![Image](assets/fr/02.webp)



在 "双因素身份验证 "部分，选择 "*密码匙*"选项（术语可能因网站而异）。



![Image](assets/fr/03.webp)



通常会要求您确认当前密码。



![Image](assets/fr/04.webp)



给你的安全密钥起个名字，方便识别，然后点击 "*Read Key*"（读取密钥）。



![Image](assets/fr/05.webp)



您的账户详细信息将显示在 Trezor 屏幕上。轻触屏幕或按键确认。您还会被要求确认 PIN 码。



![Image](assets/fr/06.webp)



注册此安全密钥。



![Image](assets/fr/07.webp)



从现在起，当你想连接到你的账户时，除了常规的密码外，你还会被要求连接你的 Trezor。



![Image](assets/fr/08.webp)



然后按 Trezor 屏幕确认身份验证。



![Image](assets/fr/09.webp)



使用 Hardware Wallet Trezor 进行双因素身份验证的优势在于，通过 Mnemonic 短语，您可以轻松找回密钥。除了这种基本备份外，您还可以使用已激活 2FA 的各项服务提供的紧急代码。如果丢失了安全密钥，紧急代码可以让您连接到自己的账户。因此，在必要时，它可以取代 2FA 进行连接。



例如，在 Bitwarden 上，您可以点击 "*查看恢复代码*"来获取该代码。



![Image](assets/fr/10.webp)



我建议你把这个密码和你的主密码放在不同的地方，以防止它们一起被盗。例如，如果您的密码保存在密码管理器中，那么请将 2FA 紧急代码单独保存在纸上。



这种方法为您在丢失用于 2FA 身份验证的 Trezor 时提供两级备份：第一级备份使用 Mnemonic 短语，适用于所有账户；第二级备份使用紧急代码，适用于每个账户。不过，重要的是**不要混淆 Mnemonic 和紧急代码的作用**：




- 通过 12 或 24 个字的 Mnemonic 短语，您不仅可以访问所有账户上用于 2FA 的密钥，还可以访问用 Trezor 加密的比特币；
- 紧急代码只允许您在相关账户上暂时绕过 2FA 请求（在本例中，只允许在 Bitwarden 上绕过）。



## 在 Trezor 上使用 FIDO2



除了双因素身份验证外，FIDO2 还支持 "无密码 "身份验证，即登录网站时无需输入密码。只需将 Trezor 与电脑连接，就能以这种方式访问安全账户。下面介绍如何配置该功能。



开始之前，请确保已在 Trezor 上设置好 Bitcoin Wallet。保存 Mnemonic 十分重要，因为 FIDO2"*无密码*"标识符是用 seed 加密的（我们将在下一节了解如何正确保存这些标识符）。



将 Trezor 与电脑连接并解锁。



![Image](assets/fr/01.webp)



以 "*无密码*"模式访问您要保护的账户。我将以 Bitwarden 账户为例。该选项通常位于服务设置中，通常在 "*验证*"、"*安全*"或 "*密码*"选项卡下。



例如，在 Bitwarden 上，该选项位于 "*主密码*"选项卡下。点击 "*打开*"激活 FIDO2 身份验证。



![Image](assets/fr/11.webp)



通常会要求您确认密码。



![Image](assets/fr/12.webp)



您的账户详细信息将显示在 Trezor 屏幕上。轻触屏幕或按键确认。您还需要确认 PIN 码。



![Image](assets/fr/13.webp)



在网站上，添加一个名字来记住你的安全密钥，然后点击 "*打开*"。



![Image](assets/fr/14.webp)



然后会要求您表明身份，以检查钥匙是否正常工作。



![Image](assets/fr/15.webp)



从现在起，登录账户时不再需要输入电子邮件 Address 或登录名。只需点击按钮，即可在登录表单上使用物理密钥进行身份验证。



![Image](assets/fr/16.webp)



输入 Hardware Wallet PIN 码，确认与 Trezor 的连接。



![Image](assets/fr/17.webp)



您无需输入密码即可连接到自己的账户。



![Image](assets/fr/18.webp)



**请注意，即使您通过 Trezor 上的 FIDO2 激活了 "*无密码*"身份验证，您在线账户的主密码仍然有效**。



## 保存您的 FIDO2 凭据（凭据居民）



如果您使用 FIDO2 或 U2F 进行双因素身份验证，即通过 Trezor 登录除 2FA 验证外还需要密码的账户，那么仅凭 Mnemonic 短语就可以获取密钥。但是，如果您在上一节所述的 "*无密码*"模式下使用 FIDO2，则除了备份加密凭证的 Mnemonic 短语外，还需要复制一份 FIDO 凭证。



为此，你需要一台安装了 Python 的电脑。打开终端，运行以下命令安装必要的 Trezor 软件：



```shell
pip3 install --upgrade trezor
```



通过 USB 将 Trezor 与电脑连接，然后使用 PIN 码解锁。



![Image](assets/fr/01.webp)



要获取存储在 Trezor 上的 FIDO2 识别码列表，请运行以下命令：



```shell
trezorctl fido credentials list
```



在 Trezor 上确认导出。



![Image](assets/fr/19.webp)



您的 FIDO2 登录信息将显示在您的终端上。例如，对于我的 Bitwarden 账户，我得到了以下信息：



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



将所有信息复制并保存到文本文件中。除了显示您正在使用这些带有 FIDO2 的服务外，该备份不会带来任何重大风险。*Credential ID*" 使用 Wallet 的 seed 加密，这意味着攻击者获取此备份后将无法连接到您的账户，只能注意到您正在使用这些账户。要解密这些 ID，您需要 Wallet 中的 seed。



因此，您可以创建该文本文件的多个副本，并将其存储在不同的地方，例如本地电脑、文件托管服务和 U 盘等外部介质上。但请注意，该备份不会自动更新，因此每次与 Trezor 建立新的 "*无密码*"连接时，都需要更新该备份。



现在假设你的 Trezor 坏了。要找回 FIDO2 凭证，首先需要在新的兼容 FIDO2 的 Trezor 设备上使用 Mnemonic 短语恢复 Wallet。



恢复完成后，要在新设备上导入 FIDO2 标识符，请在终端中运行以下命令：



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



只需将 `<CREDENTIAL_ID>` 替换为您的一个标识符即可。例如，在我的例子中，这样就可以得到 ：



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor 将提示您导入 FIDO2 识别码。请在屏幕上按键确认。



![Image](assets/fr/20.webp)



现在，您的 FIDO2 登录已在 Trezor 上运行。对每个标识符重复此步骤。



恭喜你，现在你已经可以用 U2F 和 FIDO2 快速使用 Trezor 了！如果您觉得本教程有用，请在下面留下 Green 的大拇指。欢迎在您的社交网络上分享本教程。非常感谢



我还想推荐另一篇教程，其中我们介绍了 U2F 和 FIDO2 身份验证的另一种解决方案：



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e