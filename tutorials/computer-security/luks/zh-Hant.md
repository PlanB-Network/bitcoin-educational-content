---
name: LUKS
description: 使用 LUKS 和 cryptsetup 加密 USB 隨身碟
---
![cover](assets/cover.webp)



___



*本教學依據 Mickael Dorigny 於 [IT-Connect](https://www.it-connect.fr/) 發表的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___



## I.簡報



為 USB 隨身碟加密是保護敏感資料的好方法。 **在本教程中，我們將介紹如何使用 LUKS (*Linux Unified Key Setup*) 和 cryptsetup 在 Linux 系統上為 USB 隨身碟加密。** 此方法可讓您保護資料安全，尤其是在 USB 隨身碟遺失或遭竊的情況下。



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) 是主要用於 Linux 系統的磁碟加密標準。它使用強大的演算法加密磁碟分割，以確保資料安全。它在 Linux 系統上的支援有助於管理加密金鑰和密碼，提供標準化的 Interface 並與各種管理工具相容。



若要遵循本教學，您將需要 ：





- uSB 鑰匙；
- 已安裝「**cryptsetup**」的 Linux 系統 (通常預設為可用，否則我們會看到如何取得)。



## II.安裝 cryptsetup



首先，我們需要確認系統上有 "**cryptsetup**" 指令：



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



如果此指令沒有回應，您需要安裝「**cryptsetup**」：



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



現在我們已經擁有透過 LUKS 建立加密 USB 密鑰所需的一切。



實際上，是由 "**dm-crypt**" 工具來執行加密工作。"**cryptsetup**" 是一個命令列 Interface，用來管理 **dm-crypt** 的功能和動作。



## III.建立 LUKS 磁碟分割和檔案系統



### A.識別 USB 密鑰



我們現在要在 USB 隨身碟上建立加密的 LUKS 磁碟分割。如果您尚未將 USB 隨身碟連接至您的系統，現在正是時候。



在本教程中，我將加密整個 USB 隨身碟，而不僅僅是一個磁碟分割。同樣重要的是，在此過程中，**鍵上的所有現有資料將被刪除**。



第一步是在 "**/dev/**" 目錄中找到 USB 隨身碟對應的裝置檔案。插入您的 USB 隨身碟，並確認它的裝置名稱。您可以使用以下指令列出儲存裝置：



```
$ lsblk
```



找到您的 USB 密鑰，例如「**/dev/sdb**」。您也可以使用「**fdisk -l**」指令來顯示 USB key 型號的名稱 (最好不要弄錯)，並使用裝置的儲存空間大小作為指標：



![Image](assets/fr/019.webp)



使用「**lsblk**」和「**fdisk**」識別要加密的 USB 密鑰。



在我的範例中，我的 USB key 位於 "**/dev/sdb**"。如果您看到 "**/dev/sdb1**"、"**/dev/sdb2**"等，這些就是您磁碟機上目前存在的磁碟分割。這些是目前存在於您的鑰匙上的磁碟分割。它們會被我們的操作刪除。



### B.刪除現有資料



現在我們要刪除 USB 隨身碟上的所有資料。此操作包括將 USB 隨身碟上的磁碟空間填滿 0。



**確定您的目標是正確的裝置檔案！



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



這可確保我們的金鑰上不會有持續存在的明文資料。



### C.使用 LUKS 加密 USB 密鑰



現在我們要初始化 USB 密鑰上的 LUKS 磁碟分割。這包括建立 LUKS 磁碟分割：



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



在此，「`luksFormat`」子指令會初始化並格式化裝置，以使用 LUKS 加密。系統會提示您以大寫鍵入 `YES` 確認此操作，然後定義 *passphrase*。 **選擇穩健的 *passphrase*，以確保在遺失時，攻擊者無法透過暴力攻擊發現。



之後，"**/dev/sdb**"磁碟將格式化為 LUKS，並可用作加密磁碟區。



### D.格式化加密磁碟區



我們就快成功了，現在我們需要在 LUKS 磁碟分割內建立一個有效的磁碟分割。這樣，一旦解鎖，我們就可以像使用其他檔案系統一樣使用它。要做到這一點，我們需要打開加密的磁碟分割：



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



在此，「**usbkey1**」是我在上下文中為磁碟分割掛載取的名稱。您可以隨意選擇。然後，我們需要格式化包含在 LUKS 磁碟分割中的這個磁碟分割，例如，這裡的格式化為 **ext4** ：



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



**在這裡，目標位置**指定為「**/dev/mappe/usbkey1**」**，為什麼？



「**/dev/mapper/usbkey1**」是我們給予 USB key 的「捷徑」（「**/dev/mapper**」是 Linux 通用的映射）。因此，它可以存取我們已解密的磁碟分割。以下是您現在應該看到的內容 ：



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



## IV.使用加密的 USB 密鑰



### A.開啟並編輯 LUKS 磁碟區



**Via Interface 圖形** **:**



在 Debian 下，「**dm-crypt**」是預設存在的。因此，在大多數情況下，安裝會在插入 USB key 時直接進行。然後，您會被要求在彈出視窗中輸入您的 passphrase，例如這個視窗：



![Image](assets/fr/018.webp)



請求輸入 LUKS 磁碟分割的解密 passphrase。



輸入 passphrase 之後，您的系統就可以讀取金鑰上的檔案系統，然後掛載此檔案系統，這時會顯示我們已掛載的磁碟分割：



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



**在命令列上：**



但是，值得瞭解的是如何在命令列上執行操作。讓我們先使用「**crypsetup**」和「**luksOpen**」子指令來解密加密的磁碟分割：



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



現在，USB 隨身碟的解密磁碟區會呈現我們的檔案系統和作業系統可以使用的磁碟區，因此我們會將其內容掛載到任何資料夾，例如「**/home/mickael/mnt**」：



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



這表示我們可以自由且透明地存取 USB 隨身碟上的資料。



### B.關閉並移除 LUKS 磁碟區



一旦我們的作業完成，別忘了妥善關閉一切，以確保不會損壞我們的磁碟區。第一步是卸載 ：



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



然後關閉加密的磁碟分割本身：



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



現在，任何人使用我們的 USB 密鑰時，除了加密的資料外，將看不到任何內容。



## V.結論



圖形化使用者介面使此操作透明化，但知道如何從命令列格式化、建立、開啟和關閉加密的 LUKS 磁碟分割仍是有用的。格式化之後，開啟和關閉 LUKS 磁碟分割所需的操作與安全性收益相比，就微不足道了。