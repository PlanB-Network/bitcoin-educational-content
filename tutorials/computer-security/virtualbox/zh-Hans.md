---
name: VirtualBox
description: 在 Windows 11 上安装 VirtualBox 并创建第一个虚拟机
---
![cover](assets/cover.webp)



___



*本教程基于 Florian Burnel 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。



___




## I.介绍



在本教程中，我们将学习如何在 Windows 11 上安装 VirtualBox 以创建虚拟机，无论是运行 Windows 10、Windows 11、Windows Server 还是 Linux 发行版（Debian、Ubuntu、Kali Linux 等）。



本篇 VirtualBox 入门教程将帮助您开始使用 Oracle 开发的开源虚拟化解决方案，该解决方案完全免费。稍后，我们还将在网上推出其他教程，带你深入了解这一主题。



说到虚拟化工作站，无论是作为项目的一部分进行测试，还是在 IT 学习期间，VirtualBox 显然都是一个不错的解决方案。它也是其他解决方案的替代方案，如集成到 Windows 10 和 Windows 11（以及 Windows Server）中的 Hyper-V，以及 VMware Workstation（收费）/VMware Workstation Player（个人使用免费）。



我的配置： **我将在一台 Windows 11 工作站上安装 VirtualBox**，但你也可以在 Windows 10（或旧版本）和 Linux 上安装 VirtualBox。就虚拟机而言，VirtualBox 支持多种系统，包括 Windows（如 Windows 10、Windows 11、Windows Server 2022 等）、Linux（Debian、Rocky Linux、Ubuntu、Fedora 等）、BSD（PfSense）和 macOS。



## II.下载适用于 Windows 11 的 VirtualBox



要下载 VirtualBox 安装到 Windows 机器上，只有一个好的 Address：[VirtualBox 官方网站](https://www.virtualbox.org/wiki/Downloads) 的 "**下载**"部分。只需点击 "Windows hosts "即可开始下载这个大小刚刚超过 100 MB 的可执行文件。



![Image](assets/fr/025.webp)



## III.在 Windows 11 上安装 VirtualBox



### A.安装 VirtualBox



安装 VirtualBox** 非常简单，所有 Windows 版本的安装过程都一样。首先启动刚刚下载的 VirtualBox 可执行文件，然后点击 "**下一步**"。



![Image](assets/fr/026.webp)



此安装可自定义，但我建议您安装所有功能：默认选择即是如此。在下图中，你可以看到各种 Elements，包括 .NET 和 .NET：





- VirtualBox USB 支持**，使 VirtualBox 支持 USB 设备
- VirtualBox 桥接网络**以 "桥接 "模式集成网络支持（虚拟机可直接连接到本地网络）
- VirtualBox 仅限主机网络** 在 "仅限主机 "模式下集成网络支持（在此模式下，虚拟机只能与 Windows 11 物理主机和其他虚拟机通信）。



点击 "**下一步**"继续。



![Image](assets/fr/001.webp)



点击 "**是**"，请注意**网络将在 Windows 11 机器上中断片刻**，同时 VirtualBox 将进行网络修改以支持不同的网络类型，包括桥接模式。



![Image](assets/fr/002.webp)



确认后，安装将开始...然后会出现 "**您是否要安装此设备软件？选中 "**始终信任甲骨文公司的软件**"选项，然后点击 "**安装**"。VirtualBox 实际上需要在计算机上安装几个驱动程序。



![Image](assets/fr/003.webp)



安装现已完成！勾选 "**安装后启动 Oracle VM VirtualBox 6.1.34**"选项，然后点击 "**点击**"启动软件。



![Image](assets/fr/004.webp)



### B.添加扩展包



仍可在 VirtualBox 官方网站（见前一个链接）上下载官方扩展包，点击 "**所有支持的平台**"链接，即可在 "**VirtualBox 6.1.34 Oracle VM VirtualBox 扩展包**"部分访问该扩展包。该扩展包可为 VirtualBox 添加其他功能：虽然不是必须添加，但可能很有用！例如，它包括在虚拟机中支持 USB 3.0、支持网络摄像头和磁盘加密。



打开 VirtualBox，点击菜单中的 "**文件**"，然后点击 "**设置**"。



![Image](assets/fr/005.webp)



点击左侧的 "**扩展程序**"（1），然后点击右侧的 "**+**"按钮（2），**加载刚刚下载的 VirtualBox**扩展包（3）。



![Image](assets/fr/006.webp)



点击 "**安装**"按钮进行确认。



![Image](assets/fr/007.webp)



点击 "**OK**"：官方扩展包已安装到 VirtualBox 实例中！



![Image](assets/fr/008.webp)



让我们继续创建第一个虚拟机。



## IV.创建第一个 VirtualBox 虚拟机



要在 VirtualBox 上创建新的虚拟机，只需单击 "**新**"按钮即可启动虚拟机创建向导。由于这是你第一次启动 VirtualBox，我想向你详细介绍一下 Interface 和其他按钮。





- 设置**：常规 VirtualBox 配置（默认虚拟机文件夹、更新管理、语言、NAT 网络、扩展等）。
- 导入**：以 OVF 格式导入虚拟设备
- 导出**：以 OVF 格式导出现有虚拟机以创建虚拟设备
- 添加**：以标准 VirtualBox 格式（.vbox）或 XML 格式将现有虚拟机添加到 VirtualBox 清单中



左侧的 "**工具**"部分提供了**高级功能，主要用于管理虚拟网络，也可用于管理虚拟机存储**。在 "**工具**"条目下，稍后将添加虚拟机。



![Image](assets/fr/009.webp)



### A.虚拟机创建过程



**请注意，VirtualBox 支持多种操作系统，包括 Windows、Linux 和 BSD。在本例中，我将为 Windows 11 创建一个虚拟机。需要填写几个字段：





- Name**：虚拟机名称（这是将在 VirtualBox 中显示的名称）
- 机器文件夹**：存储虚拟机的位置，因为将在此位置创建一个带有虚拟机名称的子文件夹
- 类型**：操作系统类型，取决于您要安装的操作系统
- Version**：您希望安装的系统版本，在本例中为 Windows 11，因此为 "**Windows11_64**"。



点击 "**下一步**"继续。



![Image](assets/fr/010.webp)



根据您在上一步中选择的操作系统，**VirtualBox 会推荐分配给虚拟机的资源**。在这里，我们讨论的是希望分配给虚拟机的内存。让我们假设为 4 GB，因为 Windows 11 确实推荐使用 4 GB，但如果资源不足，请指定使用 2 GB。 **继续



**注意**：分配给虚拟机的资源可以稍后修改。



![Image](assets/fr/011.webp)



就虚拟 Hard 磁盘而言，我们要从头开始，因此需要选择 "**立即创建虚拟 Hard 磁盘**"，以便虚拟机有存储空间来安装操作系统和存储数据。点击 "**创建**"。



![Image](assets/fr/012.webp)



VirtualBox 支持三种不同格式的虚拟 Hard 磁盘，这是与 VMware 和 Hyper-V 等其他解决方案的主要区别。有三种格式可供选择：





- VDI**，VirtualBox 官方格式
- VHD**，这是 Hyper-V 的官方格式，不过现在更多使用的是新的 VHDX 格式
- VMDX** 是 VMware 的官方格式，适用于 VMware Workstation 和 VMware ESXi。



要创建仅用于此 VirtualBox 实例的虚拟机，请选择 "**VDI**"。另一方面，如果以后要将虚拟 Hard 磁盘连接到 Hyper-V 主机，则最好从 VHD 格式开始，以避免转换。单击 "**下一步**"。



![Image](assets/fr/013.webp)



**虚拟磁盘的大小可以是动态的，也可以是固定的**。动态时，代表**虚拟磁盘的文件（此处为 .vdi 文件）会随着数据写入磁盘而增长**，直至达到最大大小，但删除数据时不会缩小。相反，如果是固定大小，**的总存储空间会立即分配（因此会保留）**，这样性能会稍高一些，但在首次创建虚拟磁盘时需要较长的时间。



就个人而言，对于使用 VirtualBox 测试虚拟机，我认为 "**动态分配**"模式就足够了。



![Image](assets/fr/014.webp)



**下一步是指定虚拟磁盘的大小**，注意默认情况下磁盘将存储在虚拟机目录中（在此阶段可以更改）。为了符合 Windows 11 的要求，我指定了 64 GB 的大小，但也可以指定更小的大小。点击 "**创建**"创建虚拟机！



![Image](assets/fr/015.webp)



此时，虚拟机已在我们的清单中，它已配置好，但操作系统尚未安装。在启动虚拟机之前，我们需要最终完成虚拟机的配置。



### B.将 ISO 映像分配给 VirtualBox 虚拟机



要安装 Windows 11 或其他任何系统，我们都需要安装源。大多数情况下，我们使用 ISO 格式的磁盘镜像来安装操作系统。 **有必要将 Windows 11 ISO 映像加载到虚拟机的虚拟 DVD 驱动器中



点击 VirtualBox 清单中的虚拟机 (1)，然后点击 "**配置**"按钮 (2)，即可进入该虚拟机的常规配置。该菜单用于管理资源（如增加内存、配置 CPU 等）。点击左侧的 "**存储**"按钮（3），在 DVD 驱动器上点击 "**空**"按钮（4），然后点击 DVD 形图标（5）和 "**选择磁盘文件**"。



![Image](assets/fr/016.webp)



选择要安装的操作系统的 ISO 映像，然后单击 "确定"。这就是我得到的结果：



![Image](assets/fr/017.webp)



请留在虚拟机的 "**配置**"部分，我还有一些事情要解释。



### C.虚拟机网络连接



转到左侧的 "**网络**"部分。通过该部分，您可以管理虚拟机的网络：虚拟网络接口数量（每个虚拟机最多 4 个）、MAC Address 和网络访问模式（NAT、网桥访问、内部网络等）。 **如果您想让虚拟机访问互联网，请选择 "NAT "或 "桥接访问 "**，但第二种模式要求网络上的 DHCP 服务器处于活动状态，否则您必须手动配置 IP Address。



注：我将在专门的文章中再详细介绍网络部分。



![Image](assets/fr/018.webp)



### D.虚拟处理器的数量



与物理计算机一样，虚拟机也需要内存、Hard 磁盘和处理器才能运行。当我们创建虚拟机时，您可能已经注意到向导没有包含处理器配置。不过，您可以随时通过 "**系统**"选项卡，然后通过 "**处理器**"进行配置，在这里您可以选择虚拟处理器的数量。



注意：嵌套虚拟化需要 "**启用 VT-x/AMD-v 嵌套**"选项。



在我的情况下，虚拟机有 2 个虚拟处理器：



![Image](assets/fr/019.webp)



**请随时查看配置菜单的其他部分。



### E.首次启动和操作系统安装



要启动虚拟机，只需在清单中选择该虚拟机，然后单击 "**启动**"按钮。第二个窗口将打开，提供虚拟机的可视化概览。



![Image](assets/fr/020.webp)



哎呀，我遇到了一个令人讨厌的错误，我的虚拟机无法启动！错误信息是 "虚拟机登录失败......"，详情如下：



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



事实上，这是正常现象，因为我的计算机**未启用虚拟化功能！要纠正这个问题，您需要重新启动计算机，访问 BIOS 并启用虚拟化。



![Image](assets/fr/021.webp)



无需等待，我重新启动计算机，按下 "SUPPR "键进入华硕主板的 BIOS**（按键可能因机器而异，例如可能是 F2）。要激活虚拟化，必须启用 "SVM 模式"。同样，不同主板、不同制造商的名称也会有所变化。请查找**AMD-V**（AMD CPU）或**Intel VT-x**（Intel CPU）功能。



![Image](assets/fr/022.webp)



完成后，保存修改并重新启动物理机...这次，**VirtualBox 可以启动虚拟机**并加载 Windows ISO 映像来安装操作系统！ 🙂



![Image](assets/fr/023.webp)



在安装了 VirtualBox 的 Windows 11 物理主机上，我们可以看到 Windows 11 虚拟机文件夹中包含各种文件。





- 与虚拟机配置（内存、CPU 等）相对应的 VBOX** 文件（XML 格式）
- VBOX-PREV** 文件是先前配置的备份
- VDI** 文件对应动态模式下的虚拟 Hard 磁盘，因此目前只有 13 GB，而其最大容量为 64 GB。
- NVRAM** 文件包含虚拟机的 BIOS 状态，相当于物理机的非易失性内存



![Image](assets/fr/024.webp)



## V.结论



**现在，VirtualBox 已在 Windows 11 物理机上启动并运行！剩下的就是利用它来创建虚拟机了！** 我将在另一篇文章中介绍如何在 VirtualBox 虚拟机中安装 Windows 11。对于 Windows 10、Windows Server 或 Linux 发行版（Ubuntu、Debian 等），请让我们来指导您！