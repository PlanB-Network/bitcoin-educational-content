---
name: DietPi
description: 为性能不佳的机器优化的轻量级操作系统。倾向于自托管
---

![cover](assets/cover.webp)



在非技术领域，"Odroid"、"Raspberry Pi"、"Orange Pi "或 "Radxa "等品牌鲜为人知。但只要放眼科技圈，我们就会发现，**SBC**计算机--基于单个主板制造，体积通常比常用计算机微小--已成为任何个人项目不可或缺的支持。



这些计算机型号繁多。它们最好装载 Linux 发行版，这些发行版通常经过调整，以便在这些功率不足的机器上顺利运行。



**DietPi 也不例外**：它是一个基于 Debian 的操作系统，经过优化后尽可能轻便，即使是性能最差的 SBC 也能运行得非常快。就在编写本教程时，DietPi 从 Debian12 Bookworm 升级到了 Debian13 Trixie，现在它还支持开源的基于 `RISC-V` 处理器的 SBC。DietPi 是一个值得进一步研究的惊喜发现。



## 优势



这不是用于小型树莓板的 Debian 的 "通常复制品"。DietPi 才是：




- 针对速度和轻便性进行了优化**：[与其他适用于 SBC 的 Debian 发行版的比较](https://dietpi.com/blog/?p=888)，DietPi 在所有方面都更轻便。DietPi ISO 映像的重量不到 1 GB，是目前专用于旧型号 Raspberry 或 Orange PI（例如）的版本中最小的。DietPi 对内存和 CPU 资源的需求非常低，因此它总能从电路板（即使是较旧的电路板）中获得最佳性能。
- 内置自动化和安装程序**：一套专用命令可帮助用户监控系统资源，并自动执行安装和启动程序、更新版本、备份和检查所有日志的任务。
- 一个强大的、以实验为导向的社区**：来自 DietPi 社区的[教程](https://dietpi.com/forum/c/community-tutorials/8)和项目，是您从软件中获得灵感的理想选择，有了 DietPi，您只需点击一下即可安装软件。



**从 SBC 榨取每一滴水从未如此简单**。



## 自托管自动化


想尝试使用自己的服务器来运行高级网络解决方案，或开发 Bitcoin 专业工具？DietPi 可能就是你一直在寻找的解决方案。虽然很多人都知道如何管理自己的基础设施，并运行经过完美配置和保护的服务器，但 DietPi 对那些想从零开始的人来说是一个合适的步骤。



DietPi 允许你使用 "向导 "和自己的命令行来构建这些任务，而不是手动执行这些任务所需的所有复杂任务。在这里，你可以尝试自己的个人云、智能家居设备管理、自动备份和 crontab，以及更高级的解决方案。



![img](assets/en/01.webp)



## 安装



### 下载



DietPi 提供了大量 ISO 映像，可将操作系统刻录到许多不同的设备上。其中一些仅受支持：例如，用于 Raspberry PI5 的 ISO 仍在测试中，但你一定能找到适合自己板子的 ISO。



在本指南中，我选择将其安装在瘦客户机上，因此选择了_PC/VM_，然后又选择了_Native PC_。这些设备有两种 ISO 映像，它们在生成引导加载程序方面有所不同。教程中使用的机器相当老旧，因此选择了 _BIOS/CSM_ 版本。如果你的机器较新，正确的版本可能是 `UEFI`。



![img](assets/en/02.webp)



您将进入包含 "安装程序图像"、"sha256 "和 "签名 "的页面。



![img](assets/en/03.webp)



在日常使用的计算机的 "home "中准备一个目录，以便使用 "wget "下载必要的文件。



![img](assets/en/04.webp)



开发人员的公开密钥需要进行最低限度的研究，但您可以在以下链接中找到：https://github.com/MichaIng.gpg。



![img](assets/en/05.webp)



使用 `ls -la` 检查该目录的内容，并使用 `gpg --import` 将 MichaIng 密钥导入密钥环。



### 验证和闪光



最后，也是我最推荐的部分：确定您下载并准备安装到 SBC 上的操作系统的真实性。



![img](assets/en/06.webp)



如果使用 sha256sum 命令也得到了 "良好签名 "结果和相同的 Hash 控制，则可以继续将 ISO 闪存到 U 盘。使用 Whale Etcher 等应用程序来完成此操作。



![img](assets/en/07.webp)



## DietPi 安装



![img](assets/en/09.webp)



将闪存盘转移到将托管 DietPi 的设备上，并开始安装莱姆 Green 操作系统。在本练习中，我们使用的瘦客户机有 16 GB 内存、128 GB SSD 操作系统和第二个 1 TB 数据磁盘。安装耗时不到 30 分钟，但如果使用树莓派等设备，资源可能会更少，耗时也会更长。安装过程中会显示进度。



![img](assets/en/08.webp)



DietPi 是专为 Raspberries 等设备设计的，其本质是所谓的 "无头 "安装，没有图形环境，只有本地 "shsh "访问。在本指南中，你将看到一个图形环境，准确地说，是 LXDE。



在此步骤中，您还需要在 Chromium 和 Firefox 之间选择默认使用的网络浏览器。这两种浏览器都能很好地运行；除了个人偏好之外，没有特别的禁忌。



最后，安装程序可能会询问你是否要安装任何程序，但在此**我建议你不要预装任何程序**。你应该知道，在这一步之后，出于安全考虑，你会被要求更改两个用户的默认密码。最重要的是，你需要**设置 "全局软件密码（GSP）"**，这将确保以受控方式访问各种软件。 **如果你在安装操作系统时下载了任何软件，但没有设置 "GSP"，那么这些软件实际上将无法访问**。在设置 "全局软件密码 "后，您将不得不卸载并重新安装这些软件：因此，**不要放入任何东西，以免重复工作**。(可能会带来不便，但并非 100% 确定）。



安装结束时会要求激活 DietPi-Survey，这是一项用于支持操作系统开发的自动数据收集服务。根据网站提供的信息，当你从 DietPi 提供的自动化软件中下载任何软件时，或者当你升级到下一个版本时，数据收集就会被激活。每个人都可以选择加入（_Opt IN_）或退出（_Opt OUT_）。



![img](assets/en/23.webp)



安装完成并重启后，DietPi 就会显示在屏幕上。在教程中，如前所述，我选择了 "LXDE "图形环境。在桌面上，我找到了启动 `htop` 和打开终端的快捷方式。



![img](assets/en/10.webp)



### "操作系统中的 "工具



忘掉你在 Linux 发行版上使用的大多数程序吧--DietPi 已经进行了优化，你已经遗漏了不少程序。基本上，你必须手动安装很多命令，但如果你只是尝试一下，不妨抵制诱惑，试着测试一下 DietPi 的自动化功能。



该终端无疑是开始使用新操作系统的第一个有用工具，每次打开时都会自动打开。



![img](assets/en/11.webp)



在终端屏幕上，你会看到一系列以 `dietpi-` 开头的命令，它们代表了该操作系统的 [工具](https://dietpi.com/docs/dietpi_tools/)：




- dietpi-launcher"：用于访问操作系统、文件管理器等。
- dietpi-Software"：这是一种工具，通过它可以安装套件中已有的所有软件。
- `dietpi-config`: 访问系统配置，甚至是最先进的配置。



![img](assets/en/14.webp)



### 备份



备份服务器是系统管理员在首次启动服务器时就应预料到的例行工作。



DietPi 有一个 "dietpi-Backup "命令，我建议你使用它来找到理想的解决方案：它允许你设置定期备份，增量或不增量取决于所使用的应用程序，以及自定义例程的所有选项。



![img](assets/en/22.webp)



通过启动 `dietpi-Drive_Manager` 来加载目标驱动器并将其用于此功能，从而选择备份的目标，例如另一个磁盘。



## 配置



自助托管对每个人来说都是一种可取的体验，无论是好奇者还是热心者。然而，启动和配置服务器涉及到一些不小的技术挑战。DietPi 的**简易性就体现在这里，只需几个简单的步骤，您就可以根据自己的需要配置一个系统。



![img](assets/en/24.webp)



基本设置和高级设置，只需一个 Interface 命令就能触手可及：



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```