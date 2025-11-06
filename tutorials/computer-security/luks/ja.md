---
name: LUKS
description: LUKSとcryptsetupによるUSBフラッシュドライブの暗号化
---
![cover](assets/cover.webp)



___



*このチュートリアルは、[IT-Connect](https://www.it-connect.fr/)に掲載されたMickael Dorignyのオリジナルコンテンツに基づいています。ライセンス[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文に変更が加えられている可能性があります。*



___



## I.プレゼンテーション



USBメモリを暗号化することは、機密データを保護する良い方法です。 **このチュートリアルでは、LUKS (*Linux Unified Key Setup*) と cryptsetup を使って、Linux システム上で USB メモリを暗号化する方法を紹介します。**



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*)は、主にLinuxシステムで使用されるディスク暗号化規格です。強固なアルゴリズムでディスクパーティションを暗号化することで、データを保護します。Linuxシステムでのサポートにより、暗号化キーとパスワードの管理が容易になり、標準化されたInterfaceと様々な管理ツールとの互換性が提供される。



このチュートリアルに従うには、：





- uSBキー；
- **cryptsetup**がインストールされたLinuxシステム（多くの場合、デフォルトで利用可能。）



## II.cryptsetupのインストール



まず、システム上に "**cryptsetup**"コマンドがあることを確認する必要がある：



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



このコマンドに応答がない場合は、"**cryptsetup**"をインストールする必要がある：



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



これで、LUKSを使って暗号化されたUSBキーを作成するのに必要なものはすべて揃った。



実際には、暗号化作業を行うのは "**dm-crypt**"ユーティリティである。「**cryptsetup**」は、**dm-crypt**の機能と動作を管理するコマンドラインInterfaceです。



## III.LUKS パーティションとファイルシステムの作成



### A.USBキーを特定する



これからUSBメモリに暗号化されたLUKSパーティションを作成します。もしまだシステムに接続していないなら、今がその時です。



このチュートリアルでは、1つのパーティションだけでなく、USBメモリ全体を暗号化します。また、この手順の間、**すべての既存データがキーから消去される**ということを知っておくことも重要です。



最初のステップは、"**/dev/**"ディレクトリにあるUSBスティックに対応するデバイスファイルを見つけることです。USBメモリーを挿入し、デバイス名を確認してください。以下のコマンドでストレージ・デバイスをリストアップできます：



```
$ lsblk
```



例えば "**/dev/sdb**"のように、USBキーを探す。コマンド "**fdisk -l**"を使ってUSBキーのモデル名を表示し（間違えないのが一番）、デバイスのストレージサイズを指標にすることもできます：



![Image](assets/fr/019.webp)



暗号化するUSBキーを "**lsblk**"と "**fdisk**"で特定する。



私の例では、USBキーは "**/dev/sdb**"にあります。もし "**/dev/sdb1**"、"**/dev/sdb2**"などと表示されたら、これらは現在ドライブにあるパーティションです。これらは、あなたのキーに現在存在するパーティションである。これらは我々の操作によって削除される。



### B.既存データの削除



これからUSBメモリ上のデータをすべて削除する。この操作は、USBメモリーのディスク領域を0で埋めるというものだ。



**正しいデバイスファイルをターゲットにしてください！**



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



これにより、我々の鍵に永続的な平文データが存在しないことが保証される。



### C.LUKSでUSBキーを暗号化する。



これからUSBキーのLUKSパーティションを初期化します。これにはLUKSパーティションの作成が必要です：



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



ここで、"`luksFormat`"サブコマンドはデバイスを初期化し、LUKS暗号化を使用するようにフォーマットする。大文字で`YES`と入力してこの操作を確認するようプロンプトが表示されるので、次に*passphrase*を定義する。**passphrase**は、紛失した場合に攻撃者がブルートフォース攻撃で発見できないように、堅牢なものを選択してください。



この後、"**/dev/sdb**"ディスクはLUKSでフォーマットされ、暗号化ボリュームとして使用できるようになる。



### D.暗号化ボリュームをフォーマットする



あと少しで、LUKSパーティション内に有効なパーティションを作る必要がある。こうしてロックを解除すれば、他のファイルシステムと同じように使えるようになります。そのためには、暗号化されたパーティションを開く必要があります：



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



ここで、"**usbkey1**"は私のコンテキストでパーティションマウントにつける名前です。好きな方を選んでください。LUKSパーティションに含まれるこのパーティションをフォーマットする必要があります：



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



**ここで、ターゲットロケーション**が "**/dev/mappe/usbkey1**"と指定されていますが、なぜですか？



"**/dev/mapper/usbkey1**"は、USBキーへの "ショートカット "です（"**/dev/mapper**"は、マッピング用のLinuxの一般的なものです）。そのため、暗号化解除されたパーティションにアクセスできる。このようになります：



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



## IV.暗号化されたUSBキーの使用



### A.LUKSボリュームを開いて編集する



**Interface**グラフィックより



Debianでは、デフォルトで "**dm-crypt**"が存在する。そのため、ほとんどの場合、インストールはUSBキーが差し込まれたときに直接行われます。その後、このようなポップアップ・ウィンドウでpassphraseの入力を求められます：



![Image](assets/fr/018.webp)



LUKSパーティションの復号化passphraseの入力を要求する。



passphraseが入力されると、システムはキー上のファイルシステムを読み込み、このファイルシステムをマウントできるようになり、マウントされたパーティションが表示される：



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



**コマンドライン**



しかし、コマンドラインでの操作方法を知っておく価値はあります。まず、"**crypsetup**"と "**luksOpen**"サブコマンドを使って暗号化されたパーティションを復号化することから始めましょう：



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



さて、復号化されたUSBフラッシュ・ドライブのボリュームは、ファイル・システムとOSが使用できるボリュームを示すので、その内容を任意のフォルダ、たとえば私の場合は「**/home/mickael/mnt**」にマウントする：



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



つまり、USBメモリ上のデータに自由かつ透過的にアクセスできるのだ。



### B.LUKSボリュームを閉じて削除する



操作が完了したら、ボリュームを破損しないように、すべてを適切に閉じることを忘れないでください。最初のステップは、.NET Frameworkをアンマウントすることだ：



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



その後、暗号化されたパーティション自体を閉じます：



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



これで、私たちのUSBキーを使う人は、暗号化されたデータ以外、その中身を何も見ることができなくなった。



## V.結論



グラフィカル・ユーザー・インターフェースはこの操作を透過的にしますが、暗号化されたLUKSパーティションをコマンドラインからフォーマット、作成、オープン、クローズする方法を知っておくと便利です。いったんフォーマットしてしまえば、LUKS パーティションを開いたり閉じたりするのに必要な操作は、セキュリティー上の利点に比べればごくわずかです。