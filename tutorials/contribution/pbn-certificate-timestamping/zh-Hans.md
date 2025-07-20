---
name: Plan ₿ Network 文凭时间戳
description: 了解Plan ₿ Network如何为您的证书和文凭发放可验证的证明
---

![封面](assets/cover.webp)

如果您正在阅读这篇文章，那么您很有可能已经收到了一个₿-CERT证书，或者您已经在Plan ₿ Network上完成了某个课程并获得了结业文凭。恭喜您取得了这一成就！

在本教程中，我们将了解Plan ₿ Network如何为您的₿-CERT证书或任何课程完成文凭发放可验证的证明。然后在第二部分，我们将理解如何验证这些证明的真实性。

# Plan ₿ Network的证明机制

在Plan ₿ Network上，我们为您提供的证书和文凭是由我们的密码术签署的，并且这些证书和文凭会通过时间戳而被记录在时间链上（即比特币区块链）。为了实现这一点，我们必须采用一个依赖于两种加密操作的证明机制：

1. 对生成您成就的文本文件进行GPG签名
2. 通过[opentimestamps](https://opentimestamps.org/)对这个签名文件进行时间戳记。

简而言之，第一个操作允许您验证证书（或文凭）的颁发者，而第二个操作允许您验证证书是何时被发放的。
我们相信，这种简单的证明机制使我们能够发放带有无可否认证明的证书和文凭，任何人都可以自行验证。

![image](./assets/proof-mechanism.webp)

请注意，由于这种证明机制，任何试图改变您的证书或文凭的人，即使只更改微小细节，都会创建一个完全不同的sha256哈希值的签名文件，这将立即揭示篡改行为，因为签名和时间戳记将不再有效。此外，如果有人试图恶意伪造Plan ₿ Network的一些证书或文凭，简单的签名验证就会揭露这种欺诈行为。

## GPG签名是如何运作的？

GPG签名是通过使用一个名为GNU Private Guard的开源软件获得的。这个软件允许任何人可轻松创建私钥、签名和验证签名，以及加密和解密文件。请注意，在教程的范围内，Plan ₿ Network使用GPG来创建其私钥/公钥并签署任何₿-CERT证书或课程完成文凭。

另一方面，如果有人想验证一个签名文件的真实性，他们可以使用GPG导入颁发者的公钥并进行验证。在教程的第二部分，我们将了解如何使用终端来做到这一点。

对于那些感兴趣并想要深入了解这一出色的软件的人，您可以查看["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## 时间戳记是如何运作的？

任何人都可以使用OpenTimestamps对文件进行时间戳记，并获得文件存在的可验证证明。换句话说，它不为您提供文件创建时间的证明，而是提供一个文件存在的证明，其不晚于某个特定时间。
OpenTimestamps能够免费提供这项服务，得益于一种高效的方式，将此类证明存储在比特币区块链中。它使用文件的sha256哈希作为文件的唯一标识符，并与其他用户提交的文件的哈希构建一个默克尔树（Merkle Tree），其只将该默克尔树的哈希记录在一个OpReturn交易中。
一旦这笔交易被记录在某个区块中，任何拥有初始文件和与之关联的`.ots`文件的人都可以验证时间戳的真实性。在教程的第二部分，我们将学习如何通过终端和OpenTimestamps网站的图形界面验证您的₿-CERT证书或任何课程完成证书。

# 如何验证Plan ₿ Network证书或文凭

## 第1步：下载您的证书或文凭

登录到您的个人Plan ₿ Network仪表板。

![image](./assets/login.webp)

通过点击左侧选单进入证件页面，并选择您的考试场次或课程完成证书。

![image](./assets/credential.webp)

下载zip文件。

![image](./assets/download.webp)

通过右键点击`.zip`文件并选择“提取”来提取内容。您将在里面找到三个不同的文件：

- 已签名的文本文件（例如，certificate.txt）
- 开放时间戳（Open timestamp，OTS）文件（例如，certificate.txt.ots）
- PDF证书（例如，certificate.pdf）

## 第2步：验证文本文件的签名

首先，您需要在包含文件的文件夹中打开一个终端（右键点击文件夹窗口并点击“在终端中打开”）。然后按照以下说明操作

1. 使用以下命令导入Plan ₿ Network公共PGP密钥：

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

如果您成功导入了PGP密钥，您应该会看到以下消息：

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

注意：如果您看到1个已处理的密钥，而没有已导入的密钥，这最可能意味着您之前已经导入了相同的密钥，而这是正常的。

2. 使用以下命令验证证书或文凭的签名：

```bash
gpg --verify certificate.txt
```

此命令应显示有关签名的详细信息，包括：

- 签名者（Plan ₿ Network）
- 签名时间
- 签名的有效性

这是验证结果的一个例子：

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
4. 将已有时间戳记文件（例如，`certificate.txt`）拖放到指定区域。
5. 网站将自动验证开放时间戳并显示结果。

如果您看到以下消息，则时间戳有效：
![封面](assets/opentimestamp_wegui_verified.webp)

### Command Line Interface（CLI，命令行界面）方法

注意：这个过程**需要正在运行的本地比特币节点**

1. 从官方仓库安装 OpenTimestamps 客户端：https://github.com/opentimestamps/opentimestamps-client，运行以下命令：

```
pip install opentimestamps-client
```

2. 进入到包含提取的证书文件的目录。

3. 运行以下命令以验证开放时间戳：

```
ots verify certificate.txt.ots
```

此命令将：

- 根据比特币的区块链记录检查时间戳
- 显示文件的时间戳时间
- 确认时间戳的真实性

### 最终结果

请注意，如果系统显示以下**两条**消息，则验证成功：

1. GPG 签名被报告为**“来自Plan ₿ Network的签名有效”（Good signature from Plan ₿ Network）**
2. OpenTimestamps 验证显示特定的比特币区块时间戳，并报告**“成功！比特币区块 [区块高度] 证明数据自 [时间戳] 起就存在”（Success! Bitcoin block [区块高度] attests data existed as of [时间戳]）**

现在您知道了Plan ₿ Network如何为任何₿-CERT证书和课程完成证书颁发可验证的证明，并且您可以轻松验证其真实性。
