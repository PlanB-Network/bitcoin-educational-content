---
name: Coin Wallet
description: 关于 Coin Wallet 和加强隐私与安全的方法的教程
---

![cover](assets/cover.webp)


本教程介绍[Coin Wallet](https://coin.space/)--一种用于移动设备的自加密 wallet，以及如何在使用移动 wallet 应用程序时提高安全性和隐私性。



## 关于 Coin Wallet


**Coin Wallet**是由Bitcoin爱好者团队于2015年创建的一款自托管/非托管、开源wallet。它最初是一个网络应用程序，2017 年推出 iOS 应用程序，2020 年推出 Android 应用程序--可在 Google Play、三星 Galaxy Store 和华为 AppGallery 上下载。


主要优势


- 非监护建筑
- 完全[开放源代码](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- 设计简洁明了
- 专注于核心目的--安全存储加密货币，无多余功能
- 跨平台支持：手机（iOS 和 Android）、台式机、网页
- 支持 RBF（收费替换）--随时加速卡住的交易
- 使用 [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/)/FIDO2 密钥的硬件 2FA
- 内置 Tor 支持 - 通过 Tor 网络传输所有流量，最大限度地保护隐私



## 1️⃣ 安装 Coin Wallet

Coin Wallet 可在所有主要平台上使用。



- [iOS应用商店](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [安卓（银河商店）](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [安卓（华为应用图库）](https://appgallery.huawei.com/app/C112183767)



- [安卓（Uptodown）](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [所有发布链接](https://github.com/CoinSpace/CoinSpace/releases)


还可用于桌面（Windows、Linux、macOS）、网络应用程序和 Tor。


![image](assets/en/01.webp)


## 2️⃣创建 Wallet 和设置 PIN 码


wallet 是使用 passphrase 创建的，passphrase 是从[2048 个单词的列表](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts) 中生成的一个由 12 个空格分隔的单词组成的随机序列。

Coin Wallet 支持从其他钱包导入 12、15、18、21 或 24 个字符的口令。


passphrase 是主私人密钥的人可读形式。必须安全保存。passphrase 是访问或恢复 wallet 所需的全部信息。如果 passphrase 丢失，wallet 和所有资金将永久丢失。绝不能共享 passphrase。Coin Wallet 不会在任何服务器或数据库中存储密钥。


**12个字的passphrase是否安全？

由于每个位置有 2048 个可能的字，因此有 2048¹² ≈ 10³𠞙 种组合--提供 ~128 位的安全性，相当于 Bitcoin 私钥。人们普遍认为这个级别已经足够。


![image](assets/en/02.webp)


写下 passphrase 并确认后，应用程序会要求设置一个**4 位数的 PIN**，以便日常访问。为了更加方便，您可以启用生物识别身份验证（指纹或人脸识别）来代替使用 PIN 码。


![image](assets/en/03.webp)



没有账户，没有密钥恢复，没有 passphrase 重置，也没有交易逆转。安全性完全由用户负责。


有关保存记忆短语的详细最佳实践：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣密码+PIN。使用时间和方式


**什么时候需要 passphrase？

只有在这种罕见的情况下：


- 在新设备上设置 wallet
- 重新安装 Coin Wallet 应用程序
- 清除应用程序/浏览器数据（本地存储）
- 从账户中删除硬件匙
- 输入三次错误的 PIN 码（应用程序会锁定以确保安全）


在日常使用中，4 位密码足以解锁 wallet。


**密码+PIN：如何使用**

passphrase 是真正的主私钥，可在任何设备上使用。

Coin Wallet 使用 4 位数字的 PIN 码，每次输入 12-24 个单词都很不方便，因此可以在当前设备上实现快速、日常访问。

仅凭简单的 PIN 码不足以直接保护主密钥，因此永远不会用于加密。取而代之的是



- PIN 码被发送到服务器，并与长加密 token 进行交换。
- 该 token 可解密仅存储在设备上的加密主密钥。


如果密码输入错误三次，服务器将永久删除 token。本地存储的密钥将无法使用，恢复 wallet 的唯一方法是输入原始 passphrase。

这种设计既方便又能提供强大的后备保护。



## 4️⃣接收₿itcoin - Address 类型和隐私


Coin Wallet 支持所有三种 Bitcoin 地址格式：



- 本地 SegWit (Bech32)** - 以 **bc1q** 开头 - 费用最低，推荐使用
- 嵌套的 SegWit (P2SH)** - 以**3**开头
- 传统（P2PKH）** - 以**1**开头


![image](assets/en/04.webp)


**为什么每次存款后地址都会改变？

这是有意为之，目的是保护隐私。每次收到硬币时，Coin Wallet 都会自动生成一个新的未使用地址。如果重复使用同一个地址（例如，月薪地址），任何人都可以在区块链浏览器上轻松汇总所有收到的交易，并知道总收入。


旧地址永远有效--你仍然可以向它们收件--但建议每次都使用一个新地址，这是隐私保护的最佳做法。


**如何领取Bitcoin：**

1.打开硬币

2.轻按**接收**

3.选择所需的地址类型（最好是 **bc1q** - `本地 SegWit`）。

4.显示二维码或复制地址并发送给付款人


**可选 - Mecto（用于当面支付）：**

在同一个接收屏幕上有一个 "Mecto "按钮。

打开时


- 您将被要求输入一个**昵称**（gravatar）。
- 您的当前位置和接收地址将暂时与其他同样启用了 Mecto 的 Coin Wallet 用户共享
- 他们可以在小地图上发现你，无需输入或扫描即可发送硬币


数据只对其他 Mecto 用户可见，并在 1 小时后自动删除（或在关闭时立即删除）。

Mecto 完全是可选项，如果您希望最大限度地保护隐私，请不要使用。


![image](assets/en/05.webp)


## 5️⃣发送₿比特币


发送 Bitcoin：


1.打开硬币 → 点击**发送**

2.粘贴地址或扫描 QR 码

3.输入金额（或点击 **Max**）

4.选择交易速度：


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5.使用 4 位数密码确认 → 交易已广播


### 如何加速待处理的比特币交易 (RBF)


如果您选择了慢速收费，交易就会被卡住：


1.转到 "**历史**"选项卡

2.点击待处理交易

3.点选 **加速**（付费更换）

4.确认 → 交易将以更高的费用重新广播


目前支持 RBF 加速：

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


有关 Replace-by-fee (RBF) 的更多信息： https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣导出私钥


**什么时候需要私人密钥？

(99 % 的用户从不这样做--12 个字的 passphrase 就足够了）


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### 如何在 Coin Wallet 中导出私钥


1.开放 **Bitcoin (BTC)**

2.滚动到页面底部 - 点击 **导出私钥**

3.该应用程序会以 **WIF** 格式（以 5、K 或 L 开头）显示每个地址的余额及其私人密钥和二维码。


只显示非空地址。


**WIF 密钥示例**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**下一步该做什么（建议）**


- 打开 Electrum、Sparrow、BlueWallet 或任何硬件 wallet
- 导入/扫描私人密钥
- 所有资金立即转移到您当前 seed 下的新安全地址


切勿以纯文本方式存储私人密钥。扫描后，可以安全删除。


有关私钥和派生路径的完整指南：[《如何使用私钥：终极指南》](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣技术细节 - BIP39、BIP32 和衍生路径


Coin Wallet 严格遵循官方的 Bitcoin 标准，几乎所有正规钱包都采用该标准。


BIP39` - passphrase 如何成为主私钥


- 默认字数：12
- 可选 passphrase/密码：无 ("")
- 初始熵：128 位（12 个字符）→256 位（24 个字符）
- 开源实施：https://github.com/paulmillr/scure-bip39
- 单词表：包含 2048 个单词的标准英语单词表
- 支持从任何其他 BIP39 wallet 导入 12、15、18、21 和 24 个单词的短语


BIP32 + BIP44/BIP49/BIP84` - 确定性生成所有地址

通过一把万能钥匙，wallet 可以按照严格规定的顺序 generate 数以亿计的地址。这就是为什么在 Electrum、Sparrow、Trezor、Ledger、BlueWallet 等系统中输入相同的 12 个单词，会显示出完全相同的地址和余额。


**Coin Wallet 用于 Bitcoin 的分叉路径**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

每条路径的内部


- `/0` - 外部链（您显示的收款地址）
- `/1` - 内部链（更改 wallet 本身使用的地址）


由于 Coin Wallet 遵循这些公共标准，未作任何更改，因此，即使在 10-20-30 年后，您的资金仍可在任何其他兼容的 wallet 中收回。


## 8️⃣利用 Tor 增强匿名性


**为什么在 Coin Wallet 中使用 Tor**

Tor 向 Bitcoin 节点、交易所和观察者隐藏了你的真实 IP 地址。

所有流量（余额、交易、交换）都通过 Tor 网络进行，没有直接连接，也没有 IP 泄露。

这将直接在应用程序的源代码中实现（请参阅[.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)）。


Coin Wallet 有一个隐藏的 .onion 地址，自 6.6.3 版（2024 年 12 月）起，**直接在移动应用程序中内置 Tor 支持**。


### 如何在安卓和 iOS 上启用 Tor


1. **安装 Orbot** - Tor 项目官方应用程序（免费）


   - 安卓 → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **打开 Orbot → 点击开始**

从列表中选择 **Coin Wallet**，以便只有 wallet 使用 Tor（可选，但建议使用）

等待直至显示**"已连接 "**（10-30 秒）。


3. **打开 Coin Wallet → 设置 → 网络**

打开**使用 Tor**


4. **检查状态**

顶栏出现**个紫色 Tor 洋葱图标** → 所有流量现在都通过 Tor 转接


![image](assets/en/06.webp)


就这样，您的手机 Coin Wallet 就完全匿名了。


享受私人加密货币管理！


## 📝 结论


[Coin Wallet]（https://coin.space/）--真正的 Bitcoin wallet 先驱之一，拥有 10 年的开发历史。

它刻意保持简单，并始终专注于其核心任务：安全地存储您的加密货币。

没有广告、没有新闻源、没有订阅、没有社交功能、没有任何干扰--只有一个干净、快速、自我约束的 wallet，它能准确地完成它应该做的事情。

Coin Wallet 始终将简便性和安全性放在首位。


## 📖 资源


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39