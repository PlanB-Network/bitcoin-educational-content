---
name: LN VPN

description: 设置您的VPN
---

![image](assets/cover.webp)

LN VPN 是一个可定制的VPN服务，仅接受闪电网络支付。今天，我将向您展示如何使用它，并在浏览互联网时留下更少的痕迹。

市面上有许多优质的VPN服务提供商，我们在本文中进行了全面的评测（超链接）。然而，LN VPN脱颖而出，我们不想错过向您介绍它的机会。

大多数VPN服务提供商，如ProtonVPN和Mullvad，提供使用比特币支付的选项，但需要创建账户并购买长期或短期的计划，这可能不适合每个人的预算。

LN VPN 使得按需使用VPN成为可能，短至一小时，这得益于其通过闪电网络实现的比特币支付。即时且匿名的闪电支付为微支付开辟了一个全新的世界。

> 💡 本指南描述了如何从Linux Ubuntu 22.04 LTS系统使用LN VPN。

## 先决条件：Wireguard

简单来说，Wireguard用于创建您的计算机和远程服务器之间的安全隧道，您将通过该隧道浏览互联网。在您按照本指南签订租约的期间，这个服务器的IP地址将作为您的IP地址出现。

官方Wireguard安装指南：https://www.wireguard.com/install/

```
Wireguard安装
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## 先决条件：闪电比特币钱包

如果您还没有闪电比特币钱包，不用担心，我们在这里为您准备了一个非常简单的指南。（LN教程部分可以帮助您）

## 第1步：签订租约

从https://lnvpn.com，您需要选择VPN隧道出口IP的国家和持续时间。设置这些参数后，点击“通过闪电支付”。

![image](assets/1.webp)

将显示一个闪电发票，您只需用您的闪电钱包扫描它。

支付发票后，您需要等待几秒钟到两分钟以生成您的Wireguard配置设置。如果花费的时间稍长，请不要惊慌，我们已经进行了数十次这样的程序，有时它只是需要稍微长一点时间。
接下来的屏幕将出现，您只需点击“下载为文件”以接收您的配置文件，该文件的名称看起来像lnvpn-xx-xx.conf，其中“xx”将对应当前日期。
![image](assets/2.webp)

## 第2步：激活隧道

首先，您需要重命名上一步获得的配置文件，以便Wireguard能自动识别。

转到您的下载文件夹，无论是在终端窗口还是使用文件资源管理器，并将lnvpn-xx-xx.conf文件重命名为wg0.conf，如下所示：

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

就这样！隧道已激活！

## 第3步：验证

使用像whatismyip这样的在线服务来验证您的公共IP地址现在是否是您刚刚激活的VPN的IP地址。

## 第4步：禁用
当您的租约到期时，您需要禁用连接以重新获得互联网访问权限。然后，您可以随时重复步骤1到3，以与LN VPN建立租约。
禁用隧道：

```
    $ sudo ip link delete dev wg0
```

就这样！您现在知道如何使用LN VPN，一个独特的VPN服务了！