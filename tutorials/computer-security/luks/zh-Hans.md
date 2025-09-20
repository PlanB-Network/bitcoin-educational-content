---
name: LUKS
description: 使用 LUKS 和 cryptsetup 为 USB 闪存盘加密
---
![cover](assets/cover.webp)



___



*本教程基于 Mickael Dorigny 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。*



___



## I.介绍



为 U 盘加密是保护敏感数据的好方法。 **在本教程中，我们将介绍如何使用 LUKS（*Linux 统一密钥设置*）和 cryptsetup 在 Linux 系统上为 U 盘加密**。



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) （*Linux 统一密钥设置*）是一种磁盘加密标准，主要用于 Linux 系统。它采用强大的算法对磁盘分区进行加密，从而确保数据安全。它在 Linux 系统上的支持方便了加密密钥和密码的管理，提供了标准化的 Interface 和与各种管理工具的兼容性。



要学习本教程，您需要 ：





- uSB 键；
- 安装了 "**cryptsetup**"的 Linux 系统（通常默认情况下可用，否则我们将了解如何获取）。



## II.安装 cryptsetup



首先，我们需要确保系统中有 "**cryptsetup**"命令：



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



如果该命令无响应，则需要安装 "**cryptsetup**"：



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



现在，我们已经拥有了通过 LUKS 创建加密 USB 密钥所需的一切。



实际上，加密工作是由 "**dm-crypt**"实用程序完成的。"**cryptsetup**"是一个命令行 Interface，用于管理**dm-crypt**的功能和操作。



## III.创建 LUKS 分区和文件系统



### A.识别 USB 密钥



现在，我们要在 U 盘上创建一个加密的 LUKS 分区。如果你还没有将它连接到系统上，现在就是时候了。



在本教程中，我要加密的是整个 U 盘，而不仅仅是一个分区。同样重要的是，在此过程中，**密钥中的所有现有数据都将被清除**。



第一步是在 "**/dev/**"目录下找到与 U 盘相对应的设备文件。插入 U 盘并识别其设备名称。可以使用以下命令列出存储设备：



```
$ lsblk
```



找到你的 USB 密钥，例如 "**/dev/sdb**"。你也可以使用 "**fdisk -l**"命令来显示 USB 密钥的型号名称（最好不要弄错），并使用设备的存储大小作为指示器：



![Image](assets/fr/019.webp)



用 "**lsblk**"和 "**fdisk**"识别要加密的 USB 密钥。



在我的例子中，我的 USB 密钥位于 "**/dev/sdb**"。如果你看到 "**/dev/sdb1**"、"**/dev/sdb2**"等字样，这些就是当前硬盘上的分区。这些是当前存在于密钥中的分区。它们将被我们删除。



### B.删除现有数据



现在，我们要删除 U 盘上的所有数据。该操作是用 0 填满 U 盘的磁盘空间。



**确保您的目标设备文件是正确的！**



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



这就确保了我们的密钥上不会有持久的明文数据。



### C.用 LUKS 加密 USB 密钥



现在我们要初始化 USB 密钥上的 LUKS 分区。这包括创建 LUKS 分区：



```
# Formattage d'une partition LUKS sur la clé USB
$ sudo cryptsetup luksFormat /dev/sdb

WARNING!
========
This will overwrite data on /dev/sdb irrevocably.

Are you sure? (Type 'yes' in capital letters): YES
Enter passphrase for /dev/sdb:
Verify passphrase:
```



在这里，"`luksFormat`"子命令将初始化和格式化设备以使用 LUKS 加密。系统会提示你输入大写字母 "YES "确认此操作，然后定义*passphrase*。**选择一个强大的*passphrase*，以确保在丢失的情况下，攻击者无法通过暴力攻击发现它。**



之后，"**/dev/sdb**"磁盘将被格式化为 LUKS，并可用作加密卷。



### D.格式化加密卷



我们就快成功了，现在我们需要在 LUKS 分区内创建一个有效分区。这样，一旦解锁，我们就可以像使用其他文件系统一样使用它。为此，我们需要打开加密分区：



```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Lister les disques
$ sudo fdisk -l
[...]

Disk /dev/sdb: 7.72 GiB, 8294236160 bytes, 16199680 sectors
Disk model: Flash Disk
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/usbkey1: 7.71 GiB, 8277458944 bytes, 16166912 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```



在这里，"**usbkey1**"是我给分区挂载的名称。你可以选择自己喜欢的名称。然后，我们需要格式化包含在 LUKS 分区中的分区，例如，这里的格式化为 **ext4** ：



```
# Formattage de la partition en ext4
$ sudo mkfs.ext4 /dev/mapper/usbkey1

mke2fs 1.47.0 (5-Feb-2023)
Creating filesystem with 2020864 4k blocks and 505920 inodes
Filesystem UUID: cfa607d3-c31f-475d-bcfe-fa951b60a591
Superblock backups stored on blocks:
32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks):
done
Writing superblocks and filesystem accounting information:
done
```



**这里，目标位置**被指定为 "**/dev/mapper/usbkey1**"，为什么？



"**/dev/mapper/usbkey1**"是我们为 USB 密钥指定的 "快捷方式"（"**/dev/mapper**"是 Linux 的通用映射方式）。因此，它可以访问我们的解密分区。下面就是你现在应该看到的 ：



```
# Liste des périphériques et leurs partition
$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda         8:0    0  200G  0 disk
├─sda1      8:1    0  199G  0 part  /
├─sda2      8:2    0    1K  0 part
└─sda5      8:5    0  975M  0 part  [SWAP]
sdb         8:16   1  7.7G  0 disk
└─usbkey1 254:0    0  7.7G  0 crypt
sr0        11:0    1 1024M  0 rom
```



## IV.使用加密的 USB 密钥



### A.打开并编辑 LUKS 卷



**Via Interface graphic** **:**



在 Debian 系统中，"**dm-crypt**"是默认存在的。因此，在大多数情况下，插入 USB 密钥后即可直接进行安装。然后，弹出窗口会要求你输入 passphrase：



![Image](assets/fr/018.webp)



请求输入 LUKS 分区的解密 passphrase。



输入 passphrase 后，系统就能读取密钥上的文件系统，然后挂载该文件系统，并显示我们挂载的分区：



```
$ lsblk
NAME                                        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda                                           8:0    0  200G  0 disk
├─sda1                                        8:1    0  199G  0 part  /
├─sda2                                        8:2    0    1K  0 part
└─sda5                                        8:5    0  975M  0 part  [SWAP]
sdb                                           8:16   1  7.7G  0 disk
└─luks-425f7800-e461-47e9-b8cc-f76d0cefb853 254:0    0  7.7G  0 crypt /media/mickael/cfa607d3-c31f-475d-bcfe-fa95
sr0                                          11:0    1 1024M  0 rom
```



**命令行：**



不过，了解如何在命令行上执行操作还是很有必要的。让我们先使用 "**crypsetup**"和 "**luksOpen**"子命令解密加密分区：



```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Liste des périphériques et leurs partition
$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
[...]
sdb         8:16   1  7.7G  0 disk
└─usbkey1 254:0    0  7.7G  0 crypt
sr0        11:0    1 1024M  0 rom
```



现在，U 盘解密后的卷显示为文件系统和操作系统可以使用的卷，因此我们可以将其内容挂载到任何文件夹中，例如 "**/home/mickael/mnt**"：



```
# Monter le volume déchiffré sur notre système de fichier
$ mkdir /home/mickael/mnt
$ sudo mount /dev/mapper/usbkey1 /home/mickael/mnt

$ ls /home/mickael/mnt -al
total 24
drwxr-xr-x  3 root    root     4096 Jun 11 14:38 .
drwx------ 31 mickael mickael  4096 Jun 11 21:44 ..
drwx------  2 root    root    16384 Jun 11 14:38 lost+found

```



这意味着我们可以自由、透明地访问 U 盘中的数据。



### B.关闭并删除 LUKS 卷



操作完成后，别忘了正确关闭一切，以确保我们的卷不会损坏。第一步是卸载 ：



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



然后关闭加密分区本身：



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



现在，任何人使用我们的 USB 密钥，除了加密数据外，都不会看到任何内容。



## V.结论



图形用户界面使这一操作变得透明，但了解如何通过命令行格式化、创建、打开和关闭加密的 LUKS 分区仍然很有用。格式化后，打开和关闭 LUKS 分区所需的操作与安全收益相比微不足道。