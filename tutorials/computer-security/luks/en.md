---
name: LUKS
description: Encrypting a USB flash drive with LUKS and cryptsetup
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Mickael Dorigny published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


Encrypting a USB stick is a good way of protecting your sensitive data. **In this tutorial, we'll take a look at how to use LUKS (*Linux Unified Key Setup*) with cryptsetup to encrypt a USB stick on a Linux system.** This method will enable you to secure your data, particularly in the event of loss or theft of your USB stick.


[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) is a disk encryption standard used mainly on Linux systems. It secures data by encrypting disk partitions with robust algorithms. Its support on Linux systems facilitates the management of encryption keys and passwords, offering standardized Interface and compatibility with various management tools.


To follow this tutorial, you will need:



- uSB key;
- a Linux system with "**cryptsetup**" installed (often available by default, otherwise we'll see how to get it).


## II. Installing cryptsetup


First, we need to make sure that we have the "**cryptsetup**" command on our system:


```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```


If you get no response to this command, you need to install "**cryptsetup**":


```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```


We now have everything we need to create our encrypted USB key via LUKS.


In reality, it's the "**dm-crypt**" utility that will do the encryption work. "**cryptsetup**" is a command-line Interface that manages the features and actions of **dm-crypt**.


## III. Creating the LUKS partition and file system


### A. Identify the USB key


We're now going to create an encrypted LUKS partition on our USB stick. If you haven't already connected it to your system, now's the time to do so.


For the purposes of this tutorial, I'm encrypting my entire USB stick, not just one partition. It's also important to know that during this procedure, **all existing data will be erased from the key**.


The first step is to locate the device file corresponding to your USB stick in the "**/dev/**" directory. Insert your USB stick and identify its device name. You can use the following command to list storage devices:


```
$ lsblk
```


Locate your USB key, for example "**/dev/sdb**". You can also use the command "**fdisk -l**" to display the name of the USB key model (it's best not to make a mistake), and use the device's storage size as an indicator:


![Image](assets/fr/019.webp)


Identify the USB key to be encrypted with "**lsblk**" and "**fdisk**".


In my example, my USB key is located in "**/dev/sdb**". If you see "**/dev/sdb1**", "**/dev/sdb2**", etc., these are the partitions currently present on your drive. These are the partitions currently present on your key. They will be deleted by our manipulation.


### B. Delete existing data


We're now going to delete all the data on our USB stick. The operation consists in filling the disk space on our USB stick with 0s.


**Make sure you target the right device file!


```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```


This ensures that there will be no persistent plaintext data on our key.


### C. Encrypt the USB key with LUKS


We're now going to initialize the LUKS partition on our USB key. This involves creating the LUKS partition:


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


Here, the "`luksFormat`" subcommand initializes and formats the device to use LUKS encryption. You'll be prompted to confirm this operation by typing `YES` in uppercase, then define a *passphrase*. **Choose a robust *passphrase* to ensure that, in the event of loss, the attacker cannot discover it via brute-force attacks.


After this, the "**/dev/sdb**" disk will be formatted with LUKS and ready to be used as an encrypted volume.


### D. Format encrypted volume


We're almost there, and now we need to create a valid partition within our LUKS partition. This way, once unlocked, we can use it like any other file system. To do this, we need to open the encrypted partition:


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


Here, "**usbkey1**" is the name I give to the partition mount in my context. You can choose whichever you like. We then need to format this partition contained in the LUKS partition, for example, here as **ext4**:


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


**Here, the target location** is specified as "**/dev/mappe/usbkey1**"**, why?


"**/dev/mapper/usbkey1**" is the "shortcut" we've given to our USB key ("**/dev/mapper**" is generic to Linux for mapping). It therefore provides access to our decrypted partition. Here's what you're supposed to see now:


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


## IV. Using the encrypted USB key


### A. Open and edit LUKS volume


**Via Interface graphic** **:**


Under Debian, "**dm-crypt**" is present by default. So, in most cases, installation takes place directly when the USB key is plugged in. You will then be asked to enter your passphrase in a pop-up window such as this one:


![Image](assets/fr/018.webp)


Request to enter the decryption passphrase for the LUKS partition.


Once the passphrase has been entered, your system will be able to read the file system on the key and then mount this file system, which will show our mounted partition:


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


**On the command line:**


However, it's worth knowing how to perform the operation on the command line. Let's start by decrypting the encrypted partition using "**crypsetup**" and the "**luksOpen**" sub-command:


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


Now, the decrypted volume of our USB flash drive presents a volume that our file system and OS can use, so we will mount its contents in any folder, for example "**/home/mickael/mnt**" in my case:


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


This means we can access the data on our USB stick freely and transparently.


### B. Close and remove LUKS volume


Once our operation is complete, don't forget to close everything properly to make sure we don't corrupt our volume. The first step is to unmount the:


```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```


Then close the encrypted partition itself:


```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```


Now, anyone using our USB key will see nothing of its contents except encrypted data.


## V. Conclusion


Graphical user interfaces make this operation transparent, but it is still useful to know how to format, create, open and close an encrypted LUKS partition from the command line. Once formatted, the manipulations required to open and close a LUKS partition are minimal compared with the security gains.