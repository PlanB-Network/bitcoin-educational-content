---
name: لوکس
description: رمزگذاری یک درایو فلش USB با LUKS و cryptsetup
---
![cover](assets/cover.webp)



___



*این آموزش بر اساس محتوای اصلی نوشته شده توسط Mickael Dorigny منتشر شده در [IT-Connect](https://www.it-connect.fr/) است. مجوز [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). ممکن است تغییراتی در متن اصلی ایجاد شده باشد.*



___



## I. ارائه



رمزگذاری یک USB استیک راه خوبی برای محافظت از داده‌های حساس شماست. **در این آموزش، نگاهی خواهیم داشت به چگونگی استفاده از LUKS (*Linux Unified Key Setup*) با cryptsetup برای رمزگذاری یک USB استیک در سیستم لینوکس.** این روش به شما امکان می‌دهد تا داده‌های خود را به ویژه در صورت گم شدن یا سرقت USB استیک خود، ایمن کنید.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) یک استاندارد رمزگذاری دیسک است که عمدتاً در سیستم‌های لینوکس استفاده می‌شود. این استاندارد با رمزگذاری پارتیشن‌های دیسک با الگوریتم‌های قوی، داده‌ها را ایمن می‌کند. پشتیبانی آن در سیستم‌های لینوکس مدیریت کلیدها و رمزهای عبور رمزگذاری را تسهیل می‌کند و Interface استاندارد شده و سازگاری با ابزارهای مدیریتی مختلف را ارائه می‌دهد.



برای دنبال کردن این آموزش، شما نیاز خواهید داشت به:





- کلید uSB؛
- یک سیستم لینوکس با "**cryptsetup**" نصب‌شده (اغلب به‌صورت پیش‌فرض موجود است، در غیر این صورت خواهیم دید که چگونه آن را دریافت کنیم).



## II. نصب cryptsetup



اول، باید مطمئن شویم که دستور "**cryptsetup**" را روی سیستم خود داریم:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



اگر پاسخی به این دستور دریافت نمی‌کنید، باید "**cryptsetup**" را نصب کنید:



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



اکنون همه چیزهایی که برای ایجاد کلید USB رمزگذاری شده خود از طریق LUKS نیاز داریم را داریم.



در واقع، این ابزار "**dm-crypt**" است که کار رمزگذاری را انجام می‌دهد. "**cryptsetup**" یک ابزار خط فرمان Interface است که ویژگی‌ها و عملکردهای **dm-crypt** را مدیریت می‌کند.



## III. ایجاد پارتیشن LUKS و سیستم فایل



### A. شناسایی کلید USB



اکنون قصد داریم یک پارتیشن رمزگذاری شده LUKS بر روی فلش USB خود ایجاد کنیم. اگر هنوز آن را به سیستم خود متصل نکرده‌اید، اکنون زمان آن است که این کار را انجام دهید.



برای اهداف این آموزش، من کل حافظه USB خود را رمزگذاری می‌کنم، نه فقط یک پارتیشن. همچنین مهم است بدانید که در طول این فرآیند، **تمام داده‌های موجود از کلید پاک خواهند شد**.



اولین گام این است که فایل دستگاه مربوط به USB خود را در دایرکتوری "**/dev/**" پیدا کنید. USB خود را وارد کرده و نام دستگاه آن را شناسایی کنید. می‌توانید از فرمان زیر برای لیست کردن دستگاه‌های ذخیره‌سازی استفاده کنید:



```
$ lsblk
```



کلید USB خود را پیدا کنید، به عنوان مثال "**/dev/sdb**". همچنین می‌توانید از دستور "**fdisk -l**" برای نمایش نام مدل کلید USB استفاده کنید (بهتر است اشتباه نکنید)، و از اندازه ذخیره‌سازی دستگاه به عنوان یک شاخص استفاده کنید:



![Image](assets/fr/019.webp)



شناسایی کلید USB برای رمزگذاری با "**lsblk**" و "**fdisk**".



در مثال من، کلید USB من در "**/dev/sdb**" قرار دارد. اگر "**/dev/sdb1**"، "**/dev/sdb2**"، و غیره را مشاهده کردید، این‌ها پارتیشن‌هایی هستند که در حال حاضر روی درایو شما وجود دارند. این‌ها پارتیشن‌هایی هستند که در حال حاضر روی کلید شما وجود دارند. آن‌ها با دستکاری ما حذف خواهند شد.



### B. حذف داده‌های موجود



اکنون قصد داریم تمام داده‌های موجود در فلش USB خود را حذف کنیم. این عملیات شامل پر کردن فضای دیسک فلش USB ما با 0 می‌باشد.



**مطمئن شوید که فایل دستگاه صحیح را هدف قرار می‌دهید!**



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



این اطمینان می‌دهد که هیچ داده متنی ساده ماندگاری روی کلید ما وجود نخواهد داشت.



### ج. کلید USB را با LUKS رمزگذاری کنید



اکنون قصد داریم پارتیشن LUKS را بر روی کلید USB خود راه‌اندازی کنیم. این شامل ایجاد پارتیشن LUKS می‌شود:



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



در اینجا، زیر فرمان "`luksFormat`" دستگاه را برای استفاده از رمزگذاری LUKS مقداردهی اولیه و فرمت می‌کند. از شما خواسته می‌شود تا با تایپ `YES` به حروف بزرگ این عملیات را تأیید کنید، سپس یک *passphrase* تعریف کنید. **یک *passphrase* قوی انتخاب کنید تا در صورت از دست دادن، مهاجم نتواند آن را از طریق حملات جستجوی فراگیر کشف کند.**



پس از این، دیسک "**/dev/sdb**" با LUKS فرمت شده و آماده استفاده به عنوان یک حجم رمزگذاری شده خواهد بود.



### D. فرمت کردن حجم رمزگذاری‌شده



ما تقریباً به مقصد رسیده‌ایم و اکنون باید یک پارتیشن معتبر درون پارتیشن LUKS خود ایجاد کنیم. به این ترتیب، پس از باز کردن قفل، می‌توانیم از آن مانند هر سیستم فایل دیگری استفاده کنیم. برای انجام این کار، باید پارتیشن رمزگذاری شده را باز کنیم:



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



در اینجا، "**usbkey1**" نامی است که من به پارتیشن مونت در زمینه خود می‌دهم. شما می‌توانید هر نامی که دوست دارید انتخاب کنید. سپس باید این پارتیشن که در پارتیشن LUKS قرار دارد را فرمت کنیم، به عنوان مثال، اینجا به صورت **ext4** :



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



**در اینجا، مکان هدف** به صورت "**/dev/mappe/usbkey1**"** مشخص شده است، چرا؟**



"**/dev/mapper/usbkey1**" به عنوان "میانبر" برای کلید USB ما داده شده است ("**/dev/mapper**" به طور عمومی در لینوکس برای نگاشت استفاده می‌شود). بنابراین، دسترسی به پارتیشن رمزگشایی شده ما را فراهم می‌کند. در اینجا چیزی است که اکنون باید ببینید:



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



## IV. استفاده از کلید USB رمزگذاری شده



### A. باز کردن و ویرایش حجم LUKS



**از طریق Interface گرافیک** **:**



در دبیان، "**dm-crypt**" به‌صورت پیش‌فرض موجود است. بنابراین، در اکثر موارد، نصب به‌طور مستقیم زمانی که کلید USB وصل می‌شود، انجام می‌گیرد. سپس از شما خواسته می‌شود که passphrase خود را در یک پنجره پاپ‌آپ مانند این وارد کنید:



![Image](assets/fr/018.webp)



درخواست برای وارد کردن رمزگشایی passphrase برای پارتیشن LUKS.



هنگامی که passphrase وارد شد، سیستم شما قادر خواهد بود سیستم فایل روی کلید را بخواند و سپس این سیستم فایل را مونت کند، که پارتیشن مونت شده ما را نشان خواهد داد:



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



**در خط فرمان:**



با این حال، ارزش دارد که بدانید چگونه عملیات را در خط فرمان انجام دهید. بیایید با رمزگشایی پارتیشن رمزگذاری شده با استفاده از "**crypsetup**" و زیر فرمان "**luksOpen**" شروع کنیم:



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



اکنون، حجم رمزگشایی‌شده‌ی فلش درایو USB ما حجمی را ارائه می‌دهد که سیستم فایل و سیستم‌عامل ما می‌توانند از آن استفاده کنند، بنابراین محتوای آن را در هر پوشه‌ای، به عنوان مثال "**/home/mickael/mnt**" در مورد من، مونت خواهیم کرد:



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



این بدان معناست که ما می‌توانیم به داده‌های موجود در حافظه USB خود به صورت آزادانه و شفاف دسترسی داشته باشیم.



### B. بستن و حذف حجم LUKS



پس از اتمام عملیات ما، فراموش نکنید که همه چیز را به درستی ببندید تا مطمئن شویم حجم ما خراب نمی‌شود. اولین قدم این است که : را از حالت نصب خارج کنید.



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



سپس خود پارتیشن رمزگذاری شده را ببندید:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



اکنون، هر کسی که از کلید USB ما استفاده کند، هیچ‌چیزی از محتوای آن را نخواهد دید به‌جز داده‌های رمزگذاری‌شده.



## V. نتیجه‌گیری



رابط‌های کاربری گرافیکی این عملیات را شفاف می‌سازند، اما همچنان مفید است که بدانید چگونه یک پارتیشن رمزگذاری‌شده LUKS را از طریق خط فرمان فرمت، ایجاد، باز و بسته کنید. پس از فرمت شدن، دستکاری‌های لازم برای باز و بسته کردن یک پارتیشن LUKS در مقایسه با مزایای امنیتی آن حداقل است.