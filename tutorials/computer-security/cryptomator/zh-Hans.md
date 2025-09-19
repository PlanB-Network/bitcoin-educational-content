---
name: Cryptomator
description: 在云中加密你的文件
---
![cover](assets/cover.webp)



___



*本教程基于 Florian BURNEL 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。*



___



## I.介绍



在本教程中，我们将使用 Cryptomator 应用程序加密存储在云中的数据，无论是 Microsoft OneDrive、Google Drive、Dropbox、Box 还是 iCloud 上的数据。



对存储在 Drive 等在线存储解决方案上的数据进行加密是保护文件和隐私的最佳方式。有了加密技术，即使数据存储在美国或世界其他国家的服务器上，也只有您才能解密和读取数据。



在本演示中，将使用装有 OneDrive 的 Windows 11 22H2 机器，但操作步骤在其他版本的 Windows 和其他存储服务上是相同的。您只需安装同步客户端并添加账户。这样，Cryptomator 就能在保险库中存储数据。



![Image](assets/fr/020.webp)



Cryptomator 是其他应用程序的替代品，特别是另一篇文章中介绍的 Picocrypt，它看起来不同，但使用起来同样简单。Cryptomator 也是**开放源码**，符合 RGPD 标准，并将使用 AES-256 位加密算法**加密数据**。相比之下，Picocrypt 依靠的是速度更快的 XChaCha20 算法（也是 256 位）。



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Cryptomator 应用程序适用于**Windows**（exe / msi）、**Linux**、**macOS**以及**Android**和**iOS**。顺便说一下，除了安卓应用程序需要付费（14.99 欧元）外，其他所有应用程序都是免费的。



在您的计算机上，**Cryptomator 将创建一个文件夹，并在其中创建一个保险库**。保险箱可存储在您的 OneDrive、Google Drive 或类似设备上，在保险箱内，您的数据将被加密。因此，如果您将所有数据存储在托管在 Drive 存储空间上的保险箱中，这些数据将受到保护（因为数据已加密）。



**注**：本文以在线存储服务为例，但 Cryptomator 可用来加密本地磁盘、外部磁盘甚至 NAS 上的数据。事实上，没有任何限制。



## II.安装 Cryptomator



要开始使用，您需要**下载**并**安装**Cryptomator**。下载完成后，只需点击几下即可完成安装。与 [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/)一样，Cryptomator 将依靠 WinFsp 在 Windows 机器上**挂载虚拟驱动器。





- [从官方网站下载 Cryptomator](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III.在 Windows 上使用 Cryptomator



### A.创建新保险箱



要创建新保险箱，请单击 "**添加**"按钮并选择 "**新保险箱...**"。该机器上现有的和已知的保险箱将显示在 Interface 的左侧。 **在机器 A 上创建的保险箱可以在机器 B**上打开和修改，前提是机器 B 装有 Cryptomator（加密密钥已知）。



![Image](assets/fr/015.webp)



首先为保险库命名，例如 "**IT-Connect**"。这将在我的 OneDrive 中创建一个名为 "**IT-Connect**"的目录。



![Image](assets/fr/011.webp)



下一步，Cryptomator 可能会**检测您机器上的 "驱动器 "**：Google Drive、OneDrive、Dropbox 等....。以便您直接选择提供商。我在两台不同的 Windows 11 机器上试过，使用了多个驱动器，但都没有检测到。这不是问题，只需定义 "**自定义位置**"并选择存储空间的根目录即可。例如 **C:/Users/<用户名>/OneDrive**。



![Image](assets/fr/018.webp)



接下来，您可以调整专家设置下的一个选项。



![Image](assets/fr/021.webp)



接下来，您需要定义**与加密密钥**相对应的密码。有了这个密码，您就可以**解锁 Cryptomator 保险箱**并访问其数据。 **如果密码丢失，您将无法访问您的数据**。最后，你还可以通过勾选 "**是，安全总比遗憾好**"选项来**创建备份密钥**，这与[BitLocker]恢复密钥（https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/）的精神如出一辙。建议您这样做，但不要将备份密钥存储在 OneDrive 的根目录下！



点击 "**创建保险箱**"。



![Image](assets/fr/019.webp)



复制恢复密钥，并将其保存在您最喜欢的密码管理器中。点击 "**下一步**"。



![Image](assets/fr/013.webp)



这样，您的新树干就创建好了，可以随时使用！



![Image](assets/fr/014.webp)



### B.访问数字



要访问保险箱及其数据，无论是**读取现有数据还是**添加新数据，都需要**解锁**。Cryptomator 会列出已知的保险箱：IT-Connect 保险箱会出现，只需选择它并点击 "**解锁**"即可。



![Image](assets/fr/016.webp)



您必须输入密码才能解锁保险箱。然后点击 "**释放驱动器**"。



![Image](assets/fr/022.webp)



**您的保险箱作为虚拟驱动器挂载在 Windows 机器上**。该驱动器继承了字母 E，可以让您访问数据（由于保险箱已解锁，所以是纯文本）。



![Image](assets/fr/017.webp)



在 OneDrive 端，我们无法直接浏览 Cryptomator 保管库。我们看不到数据（既看不到文件名，也看不到内容）。这意味着您不需要通过常用的 OneDrive 快捷方式向 Cryptomator 保管库添加数据。**您必须使用 Cryptomator 的虚拟驱动器添加数据。**



![Image](assets/fr/012.webp)



### C.干线选项



保险箱的设置可通过 "**加密卷选项**"按钮（锁定时）进行访问，并可在不活动的情况下启用自动锁定，就像密码保险箱一样。顾名思义，"**启动时解锁加密卷**"选项无需任何干预即可解锁驱动器并挂载虚拟驱动器。出于安全考虑，最好避免激活该选项。



通过 "**挂载**"选项卡，你还可以决定挂载只读或指定特定字母。



![Image](assets/fr/024.webp)



此外，在 Cryptomator 设置中，您还可以**启用应用程序自动启动**。



## IV.结论



有了**Cryptomator**，你只需几分钟就能**创建一个加密保险箱**，保护你想存储在 OneDrive 和其他设备上的数据。它与驱动器 "配对 "时非常容易使用：为此，我更倾向于使用 Picocrypt。