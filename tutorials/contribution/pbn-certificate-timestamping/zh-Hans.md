---
name: Plan ₿ 网络证书和文凭的时间戳记
description: 了解Plan ₿ 网络如何为您的证书和文凭发放可验证的证明
---

![封面](assets/cover.webp)

如果您正在阅读这篇文章，那么您很有可能已经收到了一个比特币证书或者是您在Plan ₿网络上完成的某个课程的结业文凭，因此恭喜您取得了这一成就！

在本教程中，我们将看到Plan ₿网络如何为您的比特币证书或任何课程完成文凭发放可验证的证明。然后在第二部分，我们将看到如何验证这些证明的真实性。

# Plan ₿网络的证明机制

在Plan ₿ 网络，我们为您提供的证书和文凭是由我们加密签名的，并在时间链上（即比特币区块链）进行时间戳记。为了实现这一点，我们必须采用一个依赖于两种加密操作的证明机制：

1. 对总结您成就的文本文件进行GPG签名
2. 通过[opentimestamps](https://opentimestamps.org/)对这个签名文件进行时间戳记。

基本上，第一个操作允许您验证是谁发放了证书（或文凭），而第二个操作允许您验证证书是何时被发放的。
我们相信，这种简单的证明机制使我们能够发放带有无可否认证明的证书和文凭，任何人都可以自行验证。

![image](./assets/proof-mechanism.webp)

请注意，由于这种证明机制，任何试图改变您的证书或文凭的哪怕是最小的细节都会创建一个完全不同的sha256哈希值的签名文件，这将立即揭示篡改行为，因为签名和时间戳记将不再有效。此外，如果有人试图恶意伪造Plan ₿网络的一些证书或文凭，简单的签名验证就会揭露这种欺诈行为。

## GPG签名是如何工作的？

GPG签名是通过使用一个名为GNU Private Guard的开源软件获得的。这个软件允许任何人轻松创建私钥、签名和验证签名，以及加密和解密文件。对于本教程的范围，了解Plan ₿网络使用GPG来创建其私钥/公钥并签署任何比特币证书或课程完成文凭即可。

另一方面，如果有人想验证一个签名文件的真实性，他们可以使用GPG导入发行者的公钥并进行验证。在教程的第二部分，我们将看到如何使用终端来做到这一点。

对于那些好奇并想了解更多关于这个神奇软件的人，您可以参考["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## 时间戳记是如何工作的？

任何人都可以使用OpenTimestamps对文件进行时间戳记，并获得文件存在的可验证证明。换句话说，它不为您提供文件创建时间的证明，而是提供一个文件存在的证明，不晚于某个特定时刻。
OpenTimestamps能够免费提供这项服务，归功于一种高效的方式，将此类证明存储在比特币区块链中。它使用文件的sha256哈希作为文件的唯一标识符，并与其他用户提交的文件的哈希构建一个默克尔树，只在一个OpReturn交易中锚定默克尔树结构的哈希。
一旦这笔交易被记录在某个区块中，任何拥有初始文件和与之关联的`.ots`文件的人都可以验证时间戳的真实性。在教程的第二部分，我们将看到如何通过终端和OpenTimestamps网站的图形界面验证您的比特币证书或任何课程完成证书。

# 如何验证Plan ₿网络证书或文凭

## 第1步：下载您的证书或文凭

登录到您的个人PBN仪表板。

![image](./assets/login.webp)

通过点击左侧菜单进入证书页面，并选择您的考试场次或课程完成证书。

![image](./assets/credential.webp)

下载zip文件。

![image](./assets/download.webp)

通过右键点击`.zip`文件并选择“提取”来提取内容。您将在里面找到三个不同的文件：

- 签名文本文件（例如，certificate.txt）
- 开放时间戳（OTS）文件（例如，certificate.txt.ots）
- PDF证书（例如，certificate.pdf）

## 第2步：验证文本文件的签名

首先在包含文件的文件夹中打开一个终端（右键点击文件夹窗口并点击“在终端中打开”）。然后按照以下说明操作

1. 使用以下命令导入Plan ₿ Network公共PGP密钥：

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

如果您成功导入了PGP密钥，您应该会看到如下消息：

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

注意：如果您看到处理了1个密钥但导入了0个，很可能是您之前已经导入了相同的密钥，这是正常的。

2. 使用以下命令验证证书或文凭的签名：

```bash
gpg --verify certificate.txt
```

此命令应显示有关签名的详细信息，包括：

- 谁签名的（Plan ₿ Network）
- 何时签名的
- 签名是否有效

这是结果的一个示例：

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

如果您看到像“BAD signature”这样的消息，那意味着文件已被篡改。

## 第3步：验证开放时间戳

### 通过图形界面验证

1. 访问OpenTimestamps网站：https://opentimestamps.org/
2. 点击“Stamp & Verify”标签。
3. 将OTS文件（例如，`certificate.txt.ots`）拖放到指定区域。
4. 将时间戳文件（例如，`certificate.txt`）拖放到指定区域。
5. 网站将自动验证开放时间戳并显示结果。

如果您看到以下消息，则时间戳有效：
![封面](assets/opentimestamp_wegui_verified.webp)

### CLI 方法

注意：此过程**将需要运行本地比特币节点**

1. 从官方仓库安装 OpenTimestamps 客户端：https://github.com/opentimestamps/opentimestamps-client，运行以下命令：

```
pip install opentimestamps-client
```

2. 导航到包含提取的证书文件的目录。

3. 运行以下命令以验证开放时间戳：

```
ots verify certificate.txt.ots
```

此命令将：

- 根据比特币的区块链检查时间戳
- 显示文件确切的时间戳时间
- 确认时间戳的真实性

### 最终结果

请注意，如果显示以下**两条**消息，则验证成功：

1. GPG 签名被报告为**“来自 Plan ₿ Network 的好签名”**
2. OpenTimestamps 验证显示特定的比特币区块时间戳，并报告**“成功！比特币区块 [区块高度] 证明数据自 [时间戳] 起就存在”**

现在您知道了 Plan ₿ Network 如何为任何比特币证书和课程完成证书发行可验证的证明，您可以轻松验证其完整性。

