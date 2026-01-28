---
name: Windows 11
description: 通过配置文件自动安装 Microsoft Windows 11
---
![cover](assets/cover.webp)


在本教程中，我们将学习如何使用标准 Windows 安装程序以外的方法自动安装 Windows 11。


## 下载！


首先你需要一个安装文件。最安全可靠的地方是直接从微软的官方网站下载。


只需访问下面提供的链接，并按照说明下载 [Windows 11 ISO 文件](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


进入下载页面后，向下滚动到下载 ISO 文件的部分。


![Image](assets/en/01.webp)


选择合适的版本。


![Image](assets/en/03.webp)


选择 Windows 11 后，单击确认按钮。


在此步骤中，可能需要几秒钟来处理请求，然后您将看到以下页面：


![Image](assets/en/04.webp)


确认请求后，您需要选择自己喜欢的语言。


![Image](assets/en/05.webp)


选择语言并单击 "确认 "按钮后，请求将被处理。这一步骤可能需要几秒钟。


请求成功处理后，您将看到一个带有 .iso 文件下载链接的页面。单击 64 位下载按钮开始下载。


文件大小约为 5.5 GB，生成的链接有效期为 24 小时。


## 自动化！


在此阶段，我们需要对标准 Windows 安装进行更改。在这一阶段，使用无人值守安装，我们将决定安装哪些项目，而无需用户事后输入。事实上，在这种方法中，我们使用 XML 文件来配置 Windows 中安装的步骤和服务。换句话说，使用 Unattended.xml 文件可在安装过程中创建一个自动化流程，无需选择多个选项，并避免了安装过程中通常需要的繁琐步骤。这种方法是微软推出的一种不同寻常的标准方法。更多信息，请访问 [微软官方网站](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11)。


互联网上有各种生成无人值守文件的工具。其中一些是在线工具，另一些则是离线工具。本网站](https://schneegans.de/windows/unattend-generator) 就是创建该文件的在线工具之一。打开后，我们将看到以下页面：


![Image](assets/en/06.webp)


如页面顶部所述，此方法可用于安装 Windows 10 和 11。第一步，我们选择 Windows 语言。如果我们需要在 Windows 显示和键盘语言列表中添加第二种甚至第三种语言，可以使用下面的方框：


![Image](assets/en/07.webp)


下一步，我们选择所需的位置。


![Image](assets/en/08.webp)


在此阶段，我们还可以指定计算机的处理器架构。在这一步中，我们可以

1.决定是否忽略 Windows 安全功能，如 TPM 和安全启动。安全启动功能可确保在启动过程中，如果任何核心 Windows 文件被篡改，都会被检测到并阻止其执行。该功能还有助于保护系统，防止在 Windows 上安装恶意更新。在某些电脑上，尤其是旧型号的电脑上，启用绕过这些功能的选项有时是不可避免的。不过，一般建议保持启用安全启动等功能。

2.忽略需要互联网连接才能完成安装的要求。这在无法使用有线局域网连接的情况下非常有用，因为在大多数情况下，Windows 安装过程中尚未识别无线网卡，因此需要通过电缆连接互联网。激活此选项可解决与此步骤相关的问题。


下一步，我们可以为计算机选择一个名称。


![Image](assets/en/09.webp)


我们还可以让 Windows 为系统选择一个名称。在此步骤中，我们可以选择 Windows 的类型，是压缩还是非压缩，或者让 Windows 根据计算机的规格确定合适的版本。在此阶段还可以设置时区。


下一步涉及分区设置：


![Image](assets/en/10.webp)


在此阶段，我们可以指定安装 Windows 的分区类型，以及安装 Windows 恢复环境所需的设置。选择第一个选项后，分区选择和分区将推迟到安装 Windows 时进行，在安装过程中，将像正常安装方法一样询问这些问题。


在此步骤中，我们选择要安装的 Windows 版本：


![Image](assets/en/11.webp)


如果有产品密钥，也可以在此阶段输入。


下一步是配置 Windows 登录账户：


![Image](assets/en/12.webp)


## 账户会议


在这个阶段


1.我们可以为管理员账户定义名称和密码。还可以创建多个用户或管理员账户。

2.在这里，我们指定了 Windows 安装后首次登录的账户。本部分的不同选项如图所示。

3.如果不想创建任何账户，请清除所有账户并选择此选项。在这种情况下，安装 Windows 后，您将自动登录到 Windows 管理员账户。


下一步是配置密码和主机文件设置：


![Image](assets/en/13.webp)


在这一阶段，我们要确定密码是否应有过期时间。此外，这部分还包括与登录尝试失败相关的安全设置，可根据需要启用或禁用。


在这一部分的底部，有文件显示的设置。这些选项在标准 Windows 安装过程中均不可用，必须在安装后进行配置。相比之下，使用无人值守安装方法，这些设置很容易访问。


下一步是配置 Windows 安全设置：


![Image](assets/en/14.webp)


## 安全设置


在这个阶段


1.Windows Defender 可以启用或禁用。该功能类似于 Windows 中的安全软件，有助于防止恶意文件的执行和某些网络攻击等。

2.可以禁用 Windows 自动更新。这是 Windows 用户面临的常见难题之一！

3.该部分允许启用或禁用 UAC（用户账户控制）。该功能可防止可疑应用程序使用较高的读写权限运行。

4.Windows 使用此功能来检测潜在的有害软件。

5.在 PowerShell 等 Windows 应用程序中启用或禁用对长路径的支持。

6.启用或禁用远程桌面，以便远程访问系统。


根据所使用的 Windows 版本，可能支持也可能不支持其中某些功能。


下一步是配置图标：


![Image](assets/en/15.webp)


在本节中


1.桌面图标已列出，可根据需要添加或删除。

2.开始菜单图标已列出，也可根据需要添加或删除。

3.本节允许配置是否安装虚拟化相关工具。此选项仅适用于 Windows 11，不适用于 Windows 10。


下一步是配置 Wi-Fi 设置：


![Image](assets/en/16.webp)


在本节中，可以配置 Wi-Fi 网络设置。如前所述，在大多数情况下，Windows 安装过程中无法识别 Wi-Fi 网卡，因此在设置过程中通常无法连接。不过，通过配置本部分，如果检测到无线网卡，系统就可以连接到互联网。


下一步涉及一个重要的设置：


![Image](assets/en/17.webp)


在本节中，我们将指定是否向 Microsoft 发送系统问题信息。


下一步是配置默认应用程序：


![Image](assets/en/18.webp)


## 默认软件启用/禁用


在这部分中，我们可以选择任何不想默认安装的应用程序。例如，我们可以选择不安装 Cortana 或 Copilot。


下一步涉及与应用程序执行相关的安全设置：


![Image](assets/en/19.webp)


通过应用 WDAC 设置，可以阻止某些应用程序的执行。


最后，在应用所需的设置后，就可以下载生成的 XML 文件了：


![Image](assets/en/20.webp)


点击下载 XML 文件，就会下载 autounattend.xml 文件。要使用该文件，只需将下载的 ISO 安装到 USB 驱动器上，将 autounattend.xml 文件放入根目录，然后继续安装 Windows。


Rufus 是用于创建可启动 USB 驱动器的工具之一。Rufus 可以用给定的 Windows 安装 ISO 文件制作可启动的 Windows 安装闪存盘。它既快捷又简单，你可以 [在此](https://rufus.ie/en/#download) 下载。


![Image](assets/en/21.webp)


在该软件中，选择所需的 USB 驱动器和相应的 ISO 文件后，我们点击 "开始"。


![Image](assets/en/22.webp)


在此阶段，我们禁用所有选项，因为启用这些选项会导致在使用生成的 Unattend 文件时发生冲突。文件复制到 U 盘后，我们将 autounattend.xml 文件放到根目录下：


![Image](assets/en/23.webp)


此时，USB 驱动器已准备就绪，可用于自动安装 Windows，并可使用该驱动器开始安装。


## ISO 编辑


如果需要在虚拟机上安装 Windows，可以使用软件来创建和编辑 ISO 文件。AnyBurn 就是这样一款软件。提取从微软网站下载的 ISO 文件内容后，将 autounattend.xml 文件放到根目录下。然后，使用 AnyBurn 创建一个包含更新内容的新 ISO。


AnyBurn 是一款处理 ISO 文件的多功能软件。它提供多种处理 ISO 文件的功能，其中之一是创建可启动 ISO 映像；[此处](https://www.anyburn.com/download.php) 是其原始网站。


在软件主页上，选择 "从文件/文件夹创建图像"：


![Image](assets/en/24.webp)


在下一页，选择从 ISO 提取的所有文件以及 autounattend.xml 文件。


![Image](assets/en/25.webp)


在这一步中，我们要对设置进行配置，以使 ISO 文件可启动：


![Image](assets/en/26.webp)


在此阶段，必须设置 bootfix.bin 文件的路径，以使 ISO 可以启动。该文件位于 ISO 根目录下的启动文件夹内。此外，建议在 "属性 "部分启用 ISO9660 和 UDF 选项。


![Image](assets/en/27.webp)


完成此步骤后，单击 "下一步 "将创建 ISO 文件。该文件可用于虚拟化软件，如 Oracle VirtualBox：


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65