---
name: LUKS
description: การเข้ารหัสไดรฟ์ USB แฟลชด้วย LUKS และ cryptsetup
---
![cover](assets/cover.webp)



___



*บทแนะนำนี้อ้างอิงจากเนื้อหาต้นฉบับโดย Mickael Dorigny ที่เผยแพร่บน [IT-Connect](https://www.it-connect.fr/). ใบอนุญาต [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). อาจมีการเปลี่ยนแปลงจากข้อความต้นฉบับ.*



___



## I. การนำเสนอ



การเข้ารหัส USB stick เป็นวิธีที่ดีในการปกป้องข้อมูลที่ละเอียดอ่อนของคุณ **ในบทช่วยสอนนี้ เราจะมาดูวิธีการใช้ LUKS (*Linux Unified Key Setup*) ร่วมกับ cryptsetup เพื่อเข้ารหัส USB stick บนระบบ Linux** วิธีนี้จะช่วยให้คุณรักษาความปลอดภัยของข้อมูล โดยเฉพาะในกรณีที่ USB stick ของคุณสูญหายหรือถูกขโมย



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) เป็นมาตรฐานการเข้ารหัสดิสก์ที่ใช้หลักบนระบบ Linux มันรักษาความปลอดภัยข้อมูลโดยการเข้ารหัสพาร์ติชันดิสก์ด้วยอัลกอริธึมที่แข็งแกร่ง การสนับสนุนบนระบบ Linux ช่วยให้การจัดการคีย์และรหัสผ่านการเข้ารหัสเป็นไปอย่างสะดวก โดยมีการเสนอ Interface มาตรฐานและความเข้ากันได้กับเครื่องมือการจัดการต่าง ๆ



ในการทำตามบทแนะนำนี้ คุณจะต้องมี:





- กุญแจ uSB;
- ระบบ Linux ที่ติดตั้ง "**cryptsetup**" (มักจะมีให้โดยค่าเริ่มต้น ถ้าไม่มีก็จะดูวิธีการติดตั้ง)



## II. การติดตั้ง cryptsetup



ก่อนอื่น เราต้องตรวจสอบให้แน่ใจว่าเรามีคำสั่ง "**cryptsetup**" ในระบบของเรา:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



หากคุณไม่ได้รับการตอบสนองต่อคำสั่งนี้ คุณจำเป็นต้องติดตั้ง "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



ตอนนี้เรามีทุกอย่างที่เราต้องการเพื่อสร้างกุญแจ USB ที่เข้ารหัสของเราผ่าน LUKS แล้ว



ในความเป็นจริงแล้ว เป็นเครื่องมือ "**dm-crypt**" ที่จะทำงานเข้ารหัส "**cryptsetup**" เป็นเครื่องมือบรรทัดคำสั่ง Interface ที่จัดการคุณสมบัติและการทำงานของ **dm-crypt**



## III. การสร้างพาร์ติชันและระบบไฟล์ LUKS



### A. ระบุคีย์ USB



เรากำลังจะสร้างพาร์ติชัน LUKS ที่เข้ารหัสบน USB ของเรา หากคุณยังไม่ได้เชื่อมต่อกับระบบของคุณ ตอนนี้เป็นเวลาที่ควรทำเช่นนั้น



สำหรับวัตถุประสงค์ของบทแนะนำนี้ ฉันกำลังเข้ารหัส USB ทั้งหมดของฉัน ไม่ใช่แค่พาร์ติชันเดียว นอกจากนี้ยังสำคัญที่จะต้องทราบว่าในระหว่างขั้นตอนนี้ **ข้อมูลทั้งหมดที่มีอยู่จะถูกลบออกจากคีย์**



ขั้นตอนแรกคือการค้นหาไฟล์อุปกรณ์ที่ตรงกับ USB stick ของคุณในไดเรกทอรี "**/dev/**" เสียบ USB stick ของคุณและระบุชื่ออุปกรณ์ คุณสามารถใช้คำสั่งต่อไปนี้เพื่อแสดงรายการอุปกรณ์จัดเก็บข้อมูล:



```
$ lsblk
```



ค้นหา USB key ของคุณ เช่น "**/dev/sdb**" คุณยังสามารถใช้คำสั่ง "**fdisk -l**" เพื่อแสดงชื่อรุ่นของ USB key (ควรระวังไม่ให้ผิดพลาด) และใช้ขนาดความจุของอุปกรณ์เป็นตัวบ่งชี้:



![Image](assets/fr/019.webp)



ระบุ USB key ที่จะเข้ารหัสด้วย "**lsblk**" และ "**fdisk**".



ในตัวอย่างของฉัน, USB key ของฉันอยู่ที่ "**/dev/sdb**". ถ้าคุณเห็น "**/dev/sdb1**", "**/dev/sdb2**", เป็นต้น, นี่คือพาร์ติชันที่มีอยู่ในไดรฟ์ของคุณในขณะนี้. นี่คือพาร์ติชันที่มีอยู่ใน key ของคุณในขณะนี้. พวกมันจะถูกลบโดยการจัดการของเรา.



### B. ลบข้อมูลที่มีอยู่



ตอนนี้เรากำลังจะลบข้อมูลทั้งหมดใน USB ของเรา การดำเนินการนี้ประกอบด้วยการเติมพื้นที่ดิสก์ใน USB ของเราด้วยเลข 0



**ตรวจสอบให้แน่ใจว่าคุณกำหนดเป้าหมายไฟล์อุปกรณ์ที่ถูกต้อง!**



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



สิ่งนี้ช่วยให้มั่นใจได้ว่าจะไม่มีข้อมูลข้อความธรรมดาที่คงอยู่บนคีย์ของเรา



### C. เข้ารหัสคีย์ USB ด้วย LUKS



เรากำลังจะเริ่มต้นพาร์ติชัน LUKS บน USB key ของเรา ซึ่งเกี่ยวข้องกับการสร้างพาร์ติชัน LUKS:



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



ที่นี่ คำสั่งย่อย "`luksFormat`" จะเริ่มต้นและฟอร์แมตอุปกรณ์เพื่อใช้การเข้ารหัส LUKS คุณจะได้รับการแจ้งให้ยืนยันการดำเนินการนี้โดยพิมพ์ `YES` เป็นตัวพิมพ์ใหญ่ จากนั้นกำหนด *passphrase* **เลือก *passphrase* ที่แข็งแกร่งเพื่อให้แน่ใจว่า ในกรณีที่สูญหาย ผู้โจมตีไม่สามารถค้นพบได้ผ่านการโจมตีแบบ brute-force**



หลังจากนี้ ดิสก์ "**/dev/sdb**" จะถูกฟอร์แมตด้วย LUKS และพร้อมที่จะใช้งานเป็นวอลุ่มที่เข้ารหัสแล้ว



### D. ฟอร์แมตไดรฟ์ที่เข้ารหัส



เราเกือบจะถึงแล้ว และตอนนี้เราจำเป็นต้องสร้างพาร์ติชันที่ถูกต้องภายในพาร์ติชัน LUKS ของเรา ด้วยวิธีนี้ เมื่อปลดล็อกแล้ว เราสามารถใช้งานได้เหมือนระบบไฟล์อื่น ๆ ในการทำเช่นนี้ เราจำเป็นต้องเปิดพาร์ติชันที่เข้ารหัส:



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



ที่นี่ "**usbkey1**" คือชื่อที่ฉันให้กับการเมานต์พาร์ติชันในบริบทของฉัน คุณสามารถเลือกชื่อใดก็ได้ตามที่คุณต้องการ จากนั้นเราจำเป็นต้องฟอร์แมตพาร์ติชันนี้ที่อยู่ในพาร์ติชัน LUKS ตัวอย่างเช่น ที่นี่เป็น **ext4**:



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



**ที่นี่, ตำแหน่งเป้าหมาย** ถูกระบุเป็น "**/dev/mappe/usbkey1**", ทำไม?



"**/dev/mapper/usbkey1**" คือ "ทางลัด" ที่เราได้ตั้งให้กับ USB key ของเรา ("**/dev/mapper**" เป็นคำทั่วไปใน Linux สำหรับการแมป) ดังนั้นมันจึงให้การเข้าถึงพาร์ติชันที่ถอดรหัสของเรา นี่คือสิ่งที่คุณควรเห็นตอนนี้:



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



## IV. การใช้กุญแจ USB ที่เข้ารหัส



### A. เปิดและแก้ไข LUKS volume



**ผ่านกราฟิก Interface** **:**



ภายใต้ Debian, "**dm-crypt**" มีอยู่โดยค่าเริ่มต้น ดังนั้น ในกรณีส่วนใหญ่ การติดตั้งจะเกิดขึ้นโดยตรงเมื่อเสียบกุญแจ USB คุณจะถูกขอให้ป้อน passphrase ของคุณในหน้าต่างป๊อปอัพเช่นนี้:



![Image](assets/fr/018.webp)



คำขอเพื่อเข้าสู่การถอดรหัส passphrase สำหรับพาร์ติชัน LUKS



เมื่อ passphrase ได้ถูกป้อนเข้าไป ระบบของคุณจะสามารถอ่านระบบไฟล์บนคีย์และจากนั้นเมานต์ระบบไฟล์นี้ ซึ่งจะแสดงพาร์ติชันที่เมานต์ของเรา:



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



**บนบรรทัดคำสั่ง:**



อย่างไรก็ตาม มันก็คุ้มค่าที่จะรู้วิธีการดำเนินการบนบรรทัดคำสั่ง มาเริ่มต้นด้วยการถอดรหัสพาร์ติชันที่เข้ารหัสโดยใช้ "**crypsetup**" และคำสั่งย่อย "**luksOpen**":



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



ตอนนี้ ปริมาณที่ถอดรหัสของ USB แฟลชไดรฟ์ของเราจะแสดงปริมาณที่ระบบไฟล์และระบบปฏิบัติการของเราสามารถใช้ได้ ดังนั้นเราจะเมานต์เนื้อหาของมันในโฟลเดอร์ใดๆ เช่น "**/home/mickael/mnt**" ในกรณีของฉัน:



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



ซึ่งหมายความว่าเราสามารถเข้าถึงข้อมูลใน USB ของเราได้อย่างอิสระและโปร่งใส



### B. ปิดและลบไดรฟ์ LUKS



เมื่อการดำเนินการของเราเสร็จสิ้น อย่าลืมปิดทุกอย่างให้เรียบร้อยเพื่อให้แน่ใจว่าเราไม่ทำให้ข้อมูลเสียหาย ขั้นตอนแรกคือการยกเลิกการต่อ:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



จากนั้นปิดพาร์ติชันที่เข้ารหัสเอง:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



ตอนนี้ ใครก็ตามที่ใช้กุญแจ USB ของเราจะไม่เห็นเนื้อหาใด ๆ ยกเว้นข้อมูลที่เข้ารหัสแล้ว



## บทสรุป



อินเทอร์เฟซผู้ใช้แบบกราฟิกทำให้การดำเนินการนี้โปร่งใส แต่ยังคงมีประโยชน์ที่จะรู้วิธีการจัดรูปแบบ สร้าง เปิด และปิดพาร์ติชัน LUKS ที่เข้ารหัสจากบรรทัดคำสั่ง เมื่อจัดรูปแบบแล้ว การจัดการที่จำเป็นในการเปิดและปิดพาร์ติชัน LUKS นั้นน้อยมากเมื่อเทียบกับผลประโยชน์ด้านความปลอดภัย