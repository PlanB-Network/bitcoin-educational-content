---
name: Arch Linux
description: 根据 KISS 理念设计的简约、高性能配电盘。
---

![cover](assets/cover.webp)



Arch Linux 是一款以其稳健性、性能和适应性而著称的发行版，尤其适用于开发目的。它具有出色的稳定性和有利于定制的环境，并有一个极其快速可靠的软件包管理器提供支持。它的理念基于**KISS**（*Keep It Simple, Stupid*）原则：提供一个轻便、简单、快速和简洁的发行版，同时给用户留出很大的自由空间。



## 为什么选择 Arch Linux？





- **免费开源**：与大多数 Linux 发行版一样，Arch Linux 完全免费。没有许可证费用，是学生、自由职业者或爱好者的绝佳选择。
- **KISS** 理念：Arch 设计简单、轻便、高效。它只提供必要的功能，让您可以按需构建自己的环境。
- **Pacman** 软件包管理器Pacman 是一款快速、可靠、精心设计的软件包管理器。它能高效安装和更新软件，并精确管理依赖关系。
- 全面的文档和活跃的社区：[Arch Wiki](https://wiki.archlinux.org)可能是 Linux 世界中最好的技术文档之一。它是了解你正在做什么的金矿。社区成员大多是经验丰富的程序员，他们非常活跃，如果你遇到困难，只要事先做了一些研究，他们就能提供帮助。



## 安装和配置



### 先决条件



所需材料





- 至少**8 GB**的 USB 密钥
- 最低 **2 GB** 内存
- 至少有 20 GB 可用磁盘空间的电脑



### 下载



![0_1](assets/fr/01.webp)



自 2017 年起，Arch Linux 不再支持 32 位架构。只有 64 位版本可用。





- 请访问 [官方网站](https://mir.archlinux.fr/iso/latest/) 下载最新的官方版 ISO 映像。



### 创建可启动密钥



要创建可启动 USB 闪存盘，可以使用 **Balena Etcher** 等工具：





- 从 [官方网站](https://etcher.balena.io) 下载 Balena Etcher。
- 启动软件，选择 Arch Linux ISO 映像。
- 选择 USB 密钥作为目标设备。
- 点击 **Flash**，开始创建可启动密钥。



![0_2](assets/fr/02.webp)



## 安装 Arch Linux



## 用 USB 密钥启动





- 完全关闭电脑
- 插入可启动 USB 密钥
- 重新启动并按**F1**、**Escape**、**F9**等键（视机型而定）进入 BIOS/UEFI
- 在启动菜单中选择 USB 密钥作为启动设备。如果一切设置正确，你将进入 Arch Linux Interface 启动界面。



## 启动安装



在启动屏幕上，选择第一个选项启动安装。请注意，Arch Linux 不提供图形安装程序。启动后，你将进入一个根模式的终端。



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### 键盘配置



您可以使用 .NET Framework 3.0 显示可用的布局：



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



然后用 .NET Framework 载入布局：



```shell
loadkeys nom-disposition
```



默认情况下，键盘为英文（qwerty），但可以使用 `loadkeys fr` 切换为 `azerty`。



### 设置日期和时间



Arch Linux 使用 `timedatectl` 工具来管理系统时钟。



![0_7](assets/fr/07.webp)





- 用 .NET 设置您的时区


```shell
timedatectl set-timezone Europe/Paris
```





- 检查是否已使用 .NET Framework 启用自动同步功能：


```shell
timedatectl status
```





- 必要时激活它：


```shell
timedatectl set-ntp true
```




这将激活与时间服务器自动同步的协议 NTP。这一步很重要，可避免以后安装软件包或配置 SSL 证书时出现日期错误。



### 磁盘分区





- 检查您的系统是否在 **UEFI** 或 **BIOS** 下启动，并带有 .NET Framework 4.0：



```shell
ls /sys/firmware/efi
```



如果该文件存在，则您处于 **UEFI**。否则，您将处于**BIOS（传统）**。




- 列出可用磁盘：


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- 启动分区管理器 ：



```shell
cfdisk /dev/nom-du-disque
```



如果使用 UEFI，请选择 **GPT**；如果使用 BIOS，请选择 **DOS**。



![0_9](assets/fr/09.webp)



#### 创建分数




- 在 **UEFI** 模式下



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- 在 BIOS 中



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



选择**写入**，键入**是**，然后**退出**。



### 格式化分区





- **UEFI**：



```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```





- **BIOS**：



```shell
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```



![0_11](assets/fr/11.webp)



### 基本系统安装



挂载**根**分区：





- 关于 BIOS ：


```shell
mount /dev/sda2 /mnt
```




- UEFI ：


```shell
mount /dev/sda3 /mnt
```



然后安装必要的软件包：



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate **fstab**文件，它能让操作系统在每次启动时自动管理分区挂载，无需人工干预：



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



进入**根**环境：



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### 系统配置





- 安装文本编辑器来编辑 .NET 文件：



```shell
pacman -S vim
```





- 设置语言 ：


编辑 `/etc/locale.gen`，然后取消对 `en_US.UTF-8 UTF-8` 行的注释



![0_14](assets/fr/14.webp)





- 设置机器名称 ：



```shell
echo nom_machine > /etc/hostname
```





- 设置 root 密码 ：



```shell
passwd
```



![0_15](assets/fr/15.webp)



### 安装 GRUB



安装 ：



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



下载后，需要根据磁盘分区格式进行安装。




- 对于 **BIOS** ：



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- 用于 **UEFI** ：



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### 定稿





- 退出 chroot 环境：


```shell
exit
```





- 移除分区：


```shell
umount -R /mnt
```





- 重新启动 ：


```shell
reboot
```



启动时，使用**根**登录名和密码登录。



![0_18](assets/fr/18.webp)


## 重启后的网络连接



重启时可能会出现网络连接未激活的情况。您可以使用 ：



```shell
ip link
```



然后在终端中输入以下文本配置 Interface 网络



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface 图形（GNOME）



默认情况下，**Arch Linux** 不包含图形 Interface。要添加一个 ：



更新系统：



```shell
pacman -Syu
```



使用以下命令安装 **Xorg**，每次按回车键保留默认选项：



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



使用以下命令安装 **GNOME**，每次都输入以保留默认选项：



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



激活**会话管理器** ：



```shell
systemctl enable gdm
systemctl start gdm
```



系统会自动重启，并显示 Interface 图形登录界面。使用根用户名和密码登录。



![0_21](assets/fr/21.webp)



## 创建用户



进入**Interface GNOME**后，您需要创建一个新用户，以获得更高的安全性和更安全、无风险的使用。进入应用程序，选择 "控制台 "选项启动终端。





- 添加用户 ：



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- 安装 **sudo** ：


```shell
pacman -S sudo
```





- 激活 **sudo** 权限：



```shell
EDITOR=nano visudo
```





- 然后取消对 ：



```shell
%wheel ALL=(ALL:ALL) ALL
```





- 重新启动系统并使用用户名登录。



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## 安装软件



由于 Arch Linux 很简约，很多软件默认情况下都没有安装。要添加所需的软件，请键入以下命令：



```shell
pacman -S nom_du_paquet_a_installe
```



例如，要安装 **nano** 文本编辑器，可以键入 ：



```shell
pacman -S nano
```



要安装轻量级网络浏览器（如 "firefox"），请使用 .NET Framework 3.0：



```shell
pacman -S firefox
```



最后，如果要添加必要的网络工具，如 `net-tools`, 命令应为 ：



```shell
pacman -S net-tools
```



别忘了，你可以在一条命令中安装多个软件包，只需将它们分别列出即可：



```shell
pacman -S vim firefox net-tools
```



Arch Linux 以其卓越的稳定性、简约的理念和强大的功能脱颖而出，成为开发环境的理想选择。Arch Linux 只提供基本功能，为用户提供了一个轻量级、高性能的基础系统，用户可以根据具体需求轻松定制。这种极简主义方法还有利于加强对系统的控制，通过限制攻击面来增强安全性。凭借活跃的社区和详尽的文档，Arch Linux 可以帮助你创建一个安全、灵活的环境，优化专业开发。



如果你喜欢使用 Arch Linux，那么你一定会喜欢我们关于 **Fedora OS** 的教程，这是一个模块化、安全、强大的操作系统，能适应你的需求和用途。



https://planb.academy/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1