---
name: LUKS
description: Криптиране на USB флаш устройство с LUKS и cryptsetup
---
![cover](assets/cover.webp)



___



*Този урок се основава на оригинално съдържание от Mickael Dorigny, публикувано в [IT-Connect](https://www.it-connect.fr/). Лиценз [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Възможно е да са направени промени в оригиналния текст.*



___



## I. Презентация



Криптирането на USB флаш памет е добър начин за защита на поверителните ви данни. **В този урок ще разгледаме как да използваме LUKS (*Linux Unified Key Setup*) с cryptsetup, за да криптираме USB стик в система Linux.** Този метод ще ви позволи да защитите данните си, особено в случай на загуба или кражба на USB стика.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) е стандарт за дисково криптиране, използван главно в системите Linux. Той защитава данните чрез криптиране на дискови дялове с надеждни алгоритми. Поддръжката му в системите Linux улеснява управлението на ключовете и паролите за криптиране, като предлага стандартизирани Interface и съвместимост с различни инструменти за управление.



За да следвате този урок, ще ви е необходимо:





- ключ uSB;
- система Linux с инсталирана програма "**cryptsetup**" (често е налична по подразбиране, в противен случай ще видим как да я получим).



## II. Инсталиране на cryptsetup



Първо, трябва да се уверим, че в системата ни е инсталирана командата "**cryptsetup**":



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Ако не получите отговор на тази команда, трябва да инсталирате "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Вече разполагаме с всичко необходимо, за да създадем криптиран USB ключ чрез LUKS.



Всъщност работата по криптирането се извършва от помощната програма "**dm-crypt**". "**cryptsetup**" е Interface за команден ред, който управлява функциите и действията на **dm-crypt**.



## III. Създаване на дял и файлова система LUKS



### A. Идентифициране на USB ключа



Сега ще създадем криптиран дял LUKS на нашата USB памет. Ако все още не сте я свързали към системата, сега е моментът да го направите.



За целите на този урок криптирам цялата си USB памет, а не само един дял. Също така е важно да знаете, че по време на тази процедура **всички съществуващи данни ще бъдат изтрити от ключа**.



Първата стъпка е да откриете файла на устройството, съответстващ на вашата USB памет, в директорията "**/dev/**". Поставете USB паметта и идентифицирайте името на устройството. Можете да използвате следната команда, за да изведете списък на устройствата за съхранение:



```
$ lsblk
```



Намерете своя USB ключ, например "**/dev/sdb**". Можете също така да използвате командата "**fdisk -l**", за да покажете името на модела на USB ключа (най-добре е да не сбъркате) и да използвате размера на паметта на устройството като индикатор:



![Image](assets/fr/019.webp)



Идентифицирайте USB ключа, който трябва да бъде криптиран, с "**lsblk**" и "**fdisk**".



В моя пример моят USB ключ се намира в "**/dev/sdb**". Ако видите "**/dev/sdb1**", "**/dev/sdb2**" и т.н., това са дяловете, които се намират в момента на вашето устройство. Това са дяловете, които в момента се намират на вашия ключ. Те ще бъдат изтрити чрез нашата манипулация.



### B. Изтриване на съществуващи данни



Сега ще изтрием всички данни от нашата USB памет. Операцията се състои в запълване на дисковото пространство на нашата USB памет с 0.



**Уверете се, че сте избрали правилния файл на устройството!**



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Това гарантира, че върху нашия ключ няма да има постоянни данни в обикновен текст.



### C. Криптиране на USB ключа с LUKS



Сега ще инициализираме дяла LUKS на нашия USB ключ. Това включва създаването на дял LUKS:



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



Тук подкомандата "`luksFormat`" инициализира и форматира устройството, за да използва криптиране LUKS. Ще бъдете подканени да потвърдите тази операция, като въведете `YES` с главни букви, след което дефинирайте *passphrase*. **Изберете надежден *passphrase*, за да сте сигурни, че в случай на загуба, нападателят няма да може да го открие чрез атаки с груба сила**



След това дискът "**/dev/sdb**" ще бъде форматиран с LUKS и ще бъде готов за използване като криптиран том.



### D. Форматиране на криптиран том



Почти сме готови и сега трябва да създадем валиден дял в рамките на нашия дял LUKS. По този начин, след като го отключим, ще можем да го използваме като всяка друга файлова система. За да направим това, трябва да отворим криптирания дял:



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



Тук "**usbkey1**" е името, което давам на монтирания дял в моя контекст. Можете да изберете каквото ви харесва. След това трябва да форматираме този дял, съдържащ се в дяла LUKS, например тук като **ext4**:



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



**Тук целевото местоположение** е посочено като "**/dev/mappe/usbkey1**", защо?



"**/dev/mapper/usbkey1**" е "прекият път", който сме задали на нашия USB ключ ("**/dev/mapper**" е общо за Linux за картографиране). Следователно той осигурява достъп до нашия декриптиран дял. Ето какво трябва да видите сега:



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



## IV. Използване на криптирания USB ключ



### A. Отваряне и редактиране на том LUKS



**Графика Interface** **:**



Под Debian "**dm-crypt**" присъства по подразбиране. Така че в повечето случаи инсталацията се извършва директно при включване на USB ключа. След това ще бъдете помолени да въведете вашия passphrase в изскачащ прозорец като този:



![Image](assets/fr/018.webp)



Искане за въвеждане на passphrase за декриптиране на дял LUKS.



След като въведете passphrase, вашата система ще може да прочете файловата система на ключа и след това да монтира тази файлова система, което ще покаже нашия монтиран дял:



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



**На командния ред:**



Въпреки това си струва да знаете как да извършите операцията в командния ред. Нека започнем с декриптиране на криптирания дял с помощта на "**crypsetup**" и подкомандата "**luksOpen**":



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



Сега декриптираният обем на нашата USB флаш памет представлява обем, който файловата система и операционната система могат да използват, така че ще монтираме съдържанието му в някоя папка, например "**/home/mickael/mnt**" в моя случай:



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



Това означава, че можем да имаме свободен и прозрачен достъп до данните в USB паметта.



### B. Затворете и извадете обема LUKS



След като операцията приключи, не забравяйте да затворите всичко правилно, за да сте сигурни, че няма да повредим обема си. Първата стъпка е да демонтирате:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



След това затворете самия криптиран дял:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Сега всеки, който използва нашия USB ключ, няма да види нищо от съдържанието му, освен криптираните данни.



## V. Заключение



Графичните потребителски интерфейси правят тази операция прозрачна, но все пак е полезно да знаете как да форматирате, създавате, отваряте и затваряте криптиран дял LUKS от командния ред. Веднъж форматирани, манипулациите, необходими за отваряне и затваряне на дял LUKS, са минимални в сравнение с ползите за сигурността.