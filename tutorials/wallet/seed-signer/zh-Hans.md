---
name: Seed Signer

description: 设置您的Seed Signer
---

![cover](assets/cover.webp)

## 材料：

1. 树莓派 Zero (版本 1.3)

树莓派 Zero

为了实现完全隔离的解决方案，请确保使用没有WiFi或蓝牙功能的1.3版本，但任何树莓派2/3/4或Zero型号都可以工作。

注意：树莓派通常不带引脚；需要焊接引脚，或者可以使用名为“GPIO Hammer”的工具。
GPIO Hammer

如果您的焊接技术不够好，或者您还没有焊接铁，那么您可以使用“GPIO Hammer”作为焊接的替代品。

2. Chapeau LCD WaveShare 1.3英寸，分辨率为240×240像素的屏幕

WaveShare LCD Hat

Waveshare 1.3″ 240×240 pxl LCD

注意：仔细选择Waveshare屏幕；确保购买分辨率为240×240像素的型号。
更多信息

3. 兼容Pi Zero的摄像头模块

树莓派摄像头

Aokin / AuviPal 5MP 1080p带OV5647传感器的视频摄像头模块；其他带有OV5647传感器模块的品牌也应该可以工作，但可能不兼容Orange Pill外壳。

注意：您需要有一条专门与树莓派Zero兼容的摄像头带线。

4. 至少4GB容量的MicroSD卡

详细资源：https://seedsigner.com/explainers/

## 软件：

软件安装

1. 下载最新的“seedsigner_x_x_x.img.zip”文件
   最新发布

2. 解压“seedsigner_x_x_x.img.zip”文件

3. 使用Balena Etcher或类似工具将解压后的.img镜像文件写入microsd卡
   BALENA ETCHER

4. 在SeedSigner中安装microsd卡。
   SeedSigner GPG公钥
   seedsigner_pubkey.gpg

## 视频教程

_指南取自Southerbitcoiner，由Cole创建_

### 一系列视频指南，涵盖SeedSigner：一个开源的、DIY硬件钱包/签名设备

![image](assets/1.webp)

SeedSigner是一个您可以从头开始构建的比特币签名设备。听起来可能很难，但这个四部分系列应该会帮到您 :) 我建议您先看第1部分和第2部分，然后决定是使用桌面（观看第3部分）还是移动设备（观看第4部分）。

您需要知道的一切都在下面。其他有用的链接包括SeedSigner的网站、他们的Github、他们的Keybase、最新发布和硬件要求。

### 第1部分：如何构建SeedSigner：

在这个视频中，我将向您展示如何下载和验证SeedSigner软件，需要哪些部件，以及如何组装您的SeedSigner。

![video](https://youtu.be/mGmNKYOXtxY)

### 第2部分：测试您的SeedSigner
在我使用我的SeedSigner之前，我做了一些测试以确保它没有执行任何恶意操作。我想分享这一步骤。以下是如何验证您的SeedSigner导出正确的钱包（xpub）、如何验证SeedSigner骰子投掷的数学计算，以及如何验证SeedSigner的bip-85子种子的方法。
![视频](https://youtu.be/34W1IyTyXZE)

### 第3部分：如何将SeedSigner与Sparrow Wallet（桌面版）一起使用

SeedSigner能够生成种子并对比特币交易进行签名。但它本身无法构建交易。您需要使用一个钱包“协调器”与您的SeedSigner一起使用。以下是如何将Sparrow Wallet与您的SeedSigner一起使用：

![视频](https://youtu.be/IQb8dh-VTOg)

第4部分：如何将SeedSigner与Blue Wallet（移动版）一起使用

SeedSigner能够生成种子并对比特币交易进行签名。但它本身无法创建交易。您需要使用一个钱包“协调器”与您的SeedSigner一起使用。以下是如何将Blue Wallet与您的SeedSigner一起使用：

![视频](https://youtu.be/x0Ee35Ct0r4)

目前为止，这些都是SeedSigner的指南！如果您认为我遗漏了什么，请告诉我。这些是我潜在视频的列表：

> SeedSigner的整体评价。它作为一个签名设备是一个好选择吗？优点/缺点？

> 如何将Bip-85与SeedSigner一起使用
> 如何成为SeedSigner的Jim叔叔

觉得这些有价值？考虑发送小费以帮助资助未来的视频：
https://www.southernbitcoiner.com/donate/