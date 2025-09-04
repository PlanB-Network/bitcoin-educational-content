---
name: LUKS
description: Шифрование USB-накопителя с помощью LUKS и cryptsetup
---
![cover](assets/cover.webp)



___



*Этот учебник основан на оригинальном контенте Mickael Dorigny, опубликованном на [IT-Connect](https://www.it-connect.fr/). Лицензия [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). В оригинальный текст могли быть внесены изменения.*



___



## I. Презентация



Шифрование USB-накопителя - хороший способ защиты конфиденциальных данных. **В этом руководстве мы рассмотрим, как использовать LUKS (*Linux Unified Key Setup*) с помощью cryptsetup для шифрования USB-накопителя в системе Linux.** Этот метод позволит вам защитить свои данные, особенно в случае потери или кражи USB-накопителя.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) - стандарт шифрования дисков, используемый в основном в системах Linux. Он обеспечивает защиту данных путем шифрования дисковых разделов с помощью надежных алгоритмов. Его поддержка в системах Linux облегчает управление ключами шифрования и паролями, обеспечивая стандартизацию Interface и совместимость с различными инструментами управления.



Чтобы следовать этому руководству, вам понадобится:





- клавиша uSB;
- система Linux с установленным "**cryptsetup**" (часто доступен по умолчанию, в противном случае мы посмотрим, как его получить).



## II. Установка cryptsetup



Во-первых, нам нужно убедиться, что в нашей системе есть команда "**cryptsetup**":



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Если вы не получили ответа на эту команду, вам необходимо установить "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Теперь у нас есть все необходимое для создания зашифрованного USB-ключа с помощью LUKS.



На самом деле шифрование выполняется утилитой "**dm-crypt**". "**cryptsetup**" - это Interface из командной строки, который управляет функциями и действиями **dm-crypt**.



## III. Создание раздела и файловой системы LUKS



### A. Идентификация USB-носителя



Сейчас мы создадим зашифрованный раздел LUKS на нашем USB-накопителе. Если вы еще не подключили его к системе, сейчас самое время это сделать.



В данном руководстве я шифрую весь USB-накопитель, а не только один раздел. Также важно знать, что во время этой процедуры **все существующие данные будут удалены с ключа**.



Первым делом найдите файл устройства, соответствующий вашему USB-накопителю, в каталоге "**/dev/**". Вставьте USB-накопитель и определите имя его устройства. Для просмотра списка устройств хранения можно использовать следующую команду:



```
$ lsblk
```



Найдите свой USB-носитель, например "**/dev/sdb**". Вы также можете использовать команду "**fdisk -l**", чтобы отобразить имя модели USB-носителя (лучше не ошибиться), а также использовать размер памяти устройства в качестве индикатора:



![Image](assets/fr/019.webp)



Определите USB-носитель для шифрования с помощью "**lsblk**" и "**fdisk**".



В моем примере USB-носитель находится в разделе "**/dev/sdb**". Если вы видите "**/dev/sdb1**", "**/dev/sdb2**" и т. д., это разделы, имеющиеся на вашем накопителе. Это разделы, которые в настоящее время присутствуют на вашем ключе. Они будут удалены в результате наших манипуляций.



### B. Удаление существующих данных



Сейчас мы удалим все данные на нашем USB-накопителе. Операция заключается в заполнении дискового пространства на нашем USB-накопителе символами 0.



**Убедитесь, что вы выбрали правильный файл устройства!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Это гарантирует, что на нашем ключе не будет постоянных данных в открытом виде.



### C. Зашифруйте USB-носитель с помощью LUKS



Теперь мы собираемся инициализировать раздел LUKS на нашем USB-носителе. Для этого нужно создать раздел LUKS:



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



Здесь подкоманда "`luksFormat`" инициализирует и форматирует устройство для использования шифрования LUKS. Вам будет предложено подтвердить эту операцию, набрав `YES` в верхнем регистре, а затем определить *passphrase*. **Выберите надежный *passphrase*, чтобы в случае потери злоумышленник не смог обнаружить его с помощью атаки методом перебора.



После этого диск "**/dev/sdb**" будет отформатирован в LUKS и готов к использованию в качестве зашифрованного тома.



### D. Форматирование зашифрованного тома



Мы почти у цели, и теперь нам нужно создать действительный раздел внутри раздела LUKS. Таким образом, разблокировав его, мы сможем использовать его как любую другую файловую систему. Для этого нам нужно открыть зашифрованный раздел:



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



Здесь "**usbkey1**" - это имя, которое я даю монтируемому разделу в моем контексте. Вы можете выбрать любое другое. Затем нам нужно отформатировать этот раздел, содержащийся в разделе LUKS, например, здесь как **ext4**:



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



**Здесь целевое расположение** указано как "**/dev/mappe/usbkey1**"**, почему?



"**/dev/mapper/usbkey1**" - это "ярлык", который мы назначили нашему USB-ключу ("**/dev/mapper**" является общим для Linux для отображения). Таким образом, он обеспечивает доступ к нашему расшифрованному разделу. Вот что вы должны увидеть теперь:



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



## IV. Использование зашифрованного USB-носителя



### A. Откройте и отредактируйте том LUKS



**График Interface** **:**



В Debian "**dm-crypt**" присутствует по умолчанию. Поэтому в большинстве случаев установка происходит непосредственно при подключении USB-носителя. Затем вам будет предложено ввести свой passphrase во всплывающем окне, подобном этому:



![Image](assets/fr/018.webp)



Запрос на ввод расшифровки passphrase для раздела LUKS.



После ввода passphrase ваша система сможет прочитать файловую систему на ключе, а затем смонтировать эту файловую систему, что покажет наш смонтированный раздел:



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



**В командной строке:**



Однако стоит знать, как выполнить эту операцию в командной строке. Начнем с расшифровки зашифрованного раздела с помощью команды "**crypsetup**" и подкоманды "**luksOpen**":



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



Теперь расшифрованный том нашего USB-накопителя представляет собой том, который может использовать наша файловая система и ОС, поэтому мы смонтируем его содержимое в любую папку, например "**/home/mickael/mnt**" в моем случае:



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



Это означает, что мы можем получить свободный и прозрачный доступ к данным на нашем USB-накопителе.



### B. Закройте и удалите том LUKS



После завершения операции не забудьте закрыть все должным образом, чтобы не повредить наш том. Первым шагом будет размонтирование диска:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Затем закройте сам зашифрованный раздел:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Теперь любой, кто воспользуется нашим USB-ключом, не увидит ничего из его содержимого, кроме зашифрованных данных.



## V. Заключение



Графические пользовательские интерфейсы делают эту операцию прозрачной, но все же полезно знать, как форматировать, создавать, открывать и закрывать зашифрованный раздел LUKS из командной строки. После форматирования манипуляции, необходимые для открытия и закрытия раздела LUKS, минимальны по сравнению с выигрышем в безопасности.