---
name: Bacca
description: 无需 Ledger Live 软件即可设置 Ledger
---
![cover](assets/cover.webp)

如果您使用 Ledger，您可能会发现，您必须通过 Ledger Live 软件，至少在初始设备配置时，要检查其真实性并在其上安装比特币应用程序。不过，在配置之后，许多比特币用户更愿意使用专门的比特币钱包管理软件，如 Sparrow 或 Liana，而不是 Ledger Live。虽然 Ledger 生产的硬件钱包非常出色，能快速包含最新的比特币功能，但他们的软件并不一定适合比特币用户的特定需求。事实上，Ledger Live 包含许多专为山赛币设计的功能，而专门用于比特币钱包管理的选项却很有限。但 Sparrow 和 Liana（目前）的问题在于，它们不允许您在 Ledger 上安装比特币应用程序。

在初始配置 Ledger 时，如果不需要使用 Ledger Live，可以使用 Bacca 工具（或 "Ledger 安装程序"）。通过该软件，您可以安装和更新比特币应用程序，验证 Ledger 的真实性，甚至随后更新设备的固件。Bacca 由 Chaincode Labs 的 Bitcoin Core 开发者、[Revault and Liana](https://wizardsardine.com/) 的联合创始人和 Pythcoiner Antoine Poinsot (Darosior)创建。

在本教程中，我将教您如何使用该工具，这样您就可以永远不用 Ledger Live 软件，仍然可以享受 Ledger 设备带来的乐趣。它适用于所有设备：Nano S Classic、Nano S Plus、Nano X、Flex 和 Stax。

---
*请注意，该工具是一个相当新的工具，其开发者明确指出，它仍处于**测试阶段**。他们建议仅将其用于测试目的，而不是用于托管真实比特币钱包的设备，尽管这样的做法是可能的。在这方面，我建议您遵循该工具开发者的建议，这些建议[在其 GitHub 存储库的 README 中](https://github.com/darosior/ledger_installer)。*

---
## 先决条件

在您的电脑上，您需要两个工具来使用 Bacca：

- Git ；
- Rust。

如果您已安装，您可以跳过这一步。

**Linux：**

在 Linux 发行版中，Git 一般都已预装。如果您想要检查系统中是否安装了 Git，可以在终端中键入以下命令 ：

```bash
git --version
```

如果系统上没有安装 Git，下面是在 Debian .NET 系统上安装 Git 的命令：

```bash
sudo apt install git
```

最后，要安装 Rust 开发环境，请使用以下命令：

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows：**

为了安装 Git，请访问 [项目官方网站](https://git-scm.com/)。下载软件并按照安装说明进行操作。

![BACCA](assets/fr/01.webp)

以同样的方式从 [官方网站](https://www.rust-lang.org/tools/install) 安装 Rust。

![BACCA](assets/fr/02.webp)

**MacOS:**

如果系统中尚未安装 Git，请打开终端并运行以下命令进行安装：

```bash
git --version
```

如果系统中未安装 Git，则会打开一个窗口，提示您安装包含 Git 的 Xcode。只需按照屏幕上的说明进行安装即可。

为了安装 Rust，请运行以下命令：

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Bacca 安装

打开终端，进入要保存软件的文件夹，然后运行以下命令：

```bash
git clone https://github.com/darosior/ledger_installer.git
```

前往软件目录：

```bash
cd ledger_installer
```

然后使用 Cargo 编译项目并运行 Bacca GUI：

```bash
cargo run -p ledger_manager_gui
```

现在您可以进入软件界面。

![BACCA](assets/fr/03.webp)

## 配置您的 Ledger

开始之前，如果您的 Ledger 是新的，请确保您已经设置了 PIN 码并保存了恢助记词。这些初始步骤不需要 Ledger Live。只需通过 USB 电缆连接 Ledger，为其供电即可。如果您不确定如何进行这两个步骤，可以参考针对您的型号的教程开头部分：



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## 使用 Bacca

将 Ledger 与电脑连接，使用设置的 PIN 码解锁。Bacca 会自动检测到您的 Ledger。

![BACCA](assets/fr/04.webp)

为了确认 Ledger 的真实性，请点击 "*Check*" 按钮。您需要在 Ledger 设备上授权连接才能继续。

![BACCA](assets/fr/05.webp)

然后，Bacca 会告诉您 Ledger 是否是真的。如果不是，则表明该设备已被破解，或者是假冒的。在这种情况下，请立即停止使用。

![BACCA](assets/fr/06.webp)

在 "*Apps*" 选单中，您可以查看已在 Ledger 上安装的应用程序列表。

![BACCA](assets/fr/07.webp)

如果您想要安装比特币应用程序，请点击 "*Install*"，然后授权在 Ledger 上安装。

![BACCA](assets/fr/08.webp)

应用程序安装已完毕。

![BACCA](assets/fr/09.webp)

如果您没有安装最新版本的比特币应用程序，Bacca 将显示 "*Update*" 按钮，而不是 "*Latest*" 指示。只需点击该按钮即可更新应用程序。

![BACCA](assets/fr/10.webp)

现在，您的 Ledger 已经正确配置了最新版本的比特币应用程序，您已经准备好在 Sparrow 或 Liana 等管理软件上导入和使用您的钱包，而无需通过 Ledger Live！

如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。非常感谢。

我还建议您看看 GnuPG 的这篇教程，其中介绍了如何在安装软件前检查其完整性和真实性。这是一种重要的做法，尤其是在安装 Liana 或 Sparrow 等钱包管理软件时：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
