---
name: LUKS
description: Mã hóa ổ đĩa flash USB bằng LUKS và cryptsetup
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Mickael Dorigny được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã có một số thay đổi.*



___



## I. Trình bày



Mã hóa ổ USB là một cách tốt để bảo vệ dữ liệu nhạy cảm của bạn. **Trong hướng dẫn này, chúng ta sẽ xem xét cách sử dụng LUKS (*Linux Unified Key Setup*) với cryptsetup để mã hóa ổ USB trên hệ thống Linux.** Phương pháp này sẽ cho phép bạn bảo mật dữ liệu, đặc biệt là trong trường hợp ổ USB bị mất hoặc bị đánh cắp.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) là một tiêu chuẩn mã hóa ổ đĩa được sử dụng chủ yếu trên các hệ thống Linux. Tiêu chuẩn này bảo mật dữ liệu bằng cách mã hóa các phân vùng ổ đĩa bằng các thuật toán mạnh mẽ. Việc hỗ trợ tiêu chuẩn này trên các hệ thống Linux giúp việc quản lý khóa mã hóa và mật khẩu trở nên dễ dàng hơn, cung cấp Interface được chuẩn hóa và tương thích với nhiều công cụ quản lý khác nhau.



Để làm theo hướng dẫn này, bạn sẽ cần:





- chìa khóa USB;
- hệ thống Linux có cài đặt "**cryptsetup**" (thường có sẵn theo mặc định, nếu không, chúng ta sẽ xem cách tải xuống).



## II. Cài đặt cryptsetup



Trước tiên, chúng ta cần đảm bảo rằng hệ thống của chúng ta có lệnh "**cryptsetup**":



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Nếu bạn không nhận được phản hồi cho lệnh này, bạn cần cài đặt "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Bây giờ chúng ta đã có mọi thứ cần thiết để tạo khóa USB được mã hóa thông qua LUKS.



Trên thực tế, tiện ích "**dm-crypt**" sẽ thực hiện công việc mã hóa. "**cryptsetup**" là một Interface dòng lệnh quản lý các tính năng và hành động của **dm-crypt**.



## III. Tạo phân vùng LUKS và hệ thống tập tin



### A. Xác định khóa USB



Bây giờ chúng ta sẽ tạo một phân vùng LUKS được mã hóa trên USB. Nếu bạn chưa kết nối nó với hệ thống, hãy thực hiện ngay bây giờ.



Trong hướng dẫn này, tôi sẽ mã hóa toàn bộ ổ USB chứ không chỉ một phân vùng. Điều quan trọng cần lưu ý là trong quá trình này, **tất cả dữ liệu hiện có sẽ bị xóa khỏi khóa**.



Bước đầu tiên là tìm tệp thiết bị tương ứng với ổ USB của bạn trong thư mục "**/dev/**". Cắm ổ USB vào và xác định tên thiết bị. Bạn có thể sử dụng lệnh sau để liệt kê các thiết bị lưu trữ:



```
$ lsblk
```



Xác định vị trí ổ USB của bạn, ví dụ: "**/dev/sdb**". Bạn cũng có thể sử dụng lệnh "**fdisk -l**" để hiển thị tên model ổ USB (tốt nhất là không nên nhập sai) và sử dụng dung lượng lưu trữ của thiết bị làm chỉ báo:



![Image](assets/fr/019.webp)



Xác định khóa USB cần mã hóa bằng "**lsblk**" và "**fdisk**".



Trong ví dụ của tôi, ổ USB của tôi nằm trong "**/dev/sdb**". Nếu bạn thấy "**/dev/sdb1**", "**/dev/sdb2**", v.v., đây là các phân vùng hiện có trên ổ đĩa của bạn. Đây là các phân vùng hiện có trên ổ đĩa của bạn. Chúng sẽ bị xóa sau thao tác của chúng ta.



### B. Xóa dữ liệu hiện có



Bây giờ chúng ta sẽ xóa toàn bộ dữ liệu trên ổ USB. Thao tác này bao gồm việc điền đầy dung lượng ổ đĩa trên ổ USB bằng các số 0.



**Hãy đảm bảo bạn nhắm đúng tệp thiết bị!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Điều này đảm bảo rằng sẽ không có dữ liệu văn bản thuần túy nào tồn tại trên khóa của chúng ta.



### C. Mã hóa khóa USB bằng LUKS



Bây giờ chúng ta sẽ khởi tạo phân vùng LUKS trên USB. Việc này bao gồm việc tạo phân vùng LUKS:



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



Tại đây, lệnh phụ "`luksFormat`" sẽ khởi tạo và định dạng thiết bị để sử dụng mã hóa LUKS. Bạn sẽ được nhắc xác nhận thao tác này bằng cách nhập `YES` bằng chữ in hoa, sau đó định nghĩa *passphrase*. **Hãy chọn *passphrase* mạnh mẽ để đảm bảo rằng, trong trường hợp mất dữ liệu, kẻ tấn công không thể phát hiện ra nó bằng các cuộc tấn công brute-force.



Sau đó, đĩa "**/dev/sdb**" sẽ được định dạng bằng LUKS và sẵn sàng để sử dụng như một ổ đĩa được mã hóa.



### D. Định dạng ổ đĩa được mã hóa



Chúng ta sắp hoàn tất rồi, và bây giờ chúng ta cần tạo một phân vùng hợp lệ trong phân vùng LUKS. Bằng cách này, sau khi mở khóa, chúng ta có thể sử dụng nó như bất kỳ hệ thống tệp nào khác. Để làm điều này, chúng ta cần mở phân vùng đã mã hóa:



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



Ở đây, "**usbkey1**" là tên tôi đặt cho phân vùng mount trong ngữ cảnh của tôi. Bạn có thể chọn bất kỳ tên nào bạn thích. Sau đó, chúng ta cần định dạng phân vùng này nằm trong phân vùng LUKS, ví dụ, ở đây là **ext4**:



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



**Ở đây, vị trí mục tiêu** được chỉ định là "**/dev/mappe/usbkey1**"**, tại sao?



"**/dev/mapper/usbkey1**" là "lối tắt" chúng ta đã gán cho ổ USB ("**/dev/mapper**" là lối tắt chung cho Linux để ánh xạ). Do đó, nó cung cấp quyền truy cập vào phân vùng đã giải mã. Sau đây là những gì bạn sẽ thấy:



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



## IV. Sử dụng khóa USB được mã hóa



### A. Mở và chỉnh sửa ổ đĩa LUKS



**Qua đồ họa Interface** **:**



Trên Debian, "**dm-crypt**" được mặc định sẵn. Vì vậy, trong hầu hết các trường hợp, quá trình cài đặt diễn ra ngay khi ổ USB được cắm vào. Sau đó, bạn sẽ được yêu cầu nhập passphrase trong một cửa sổ bật lên như sau:



![Image](assets/fr/018.webp)



Yêu cầu nhập mã giải mã passphrase cho phân vùng LUKS.



Sau khi nhập passphrase, hệ thống của bạn sẽ có thể đọc hệ thống tệp trên khóa và sau đó gắn kết hệ thống tệp này, điều này sẽ hiển thị phân vùng đã gắn kết của chúng ta:



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



**Trên dòng lệnh:**



Tuy nhiên, bạn nên biết cách thực hiện thao tác này trên dòng lệnh. Hãy bắt đầu bằng cách giải mã phân vùng đã mã hóa bằng lệnh "**crypsetup**" và lệnh phụ "**luksOpen**":



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



Bây giờ, ổ đĩa flash USB đã giải mã của chúng ta sẽ hiển thị một ổ đĩa mà hệ thống tệp và hệ điều hành của chúng ta có thể sử dụng, do đó chúng ta sẽ gắn nội dung của nó vào bất kỳ thư mục nào, ví dụ như trong trường hợp của tôi là "**/home/mickael/mnt**":



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



Điều này có nghĩa là chúng ta có thể truy cập dữ liệu trên ổ USB một cách tự do và minh bạch.



### B. Đóng và xóa ổ đĩa LUKS



Sau khi hoàn tất thao tác, đừng quên đóng mọi thứ cẩn thận để đảm bảo ổ đĩa không bị hỏng. Bước đầu tiên là ngắt kết nối:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Sau đó đóng phân vùng đã mã hóa:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Bây giờ, bất kỳ ai sử dụng khóa USB của chúng tôi sẽ không thấy bất kỳ nội dung nào trong đó ngoại trừ dữ liệu được mã hóa.



## V. Kết luận



Giao diện người dùng đồ họa làm cho thao tác này trở nên minh bạch, nhưng việc biết cách định dạng, tạo, mở và đóng phân vùng LUKS được mã hóa từ dòng lệnh vẫn rất hữu ích. Sau khi được định dạng, các thao tác cần thiết để mở và đóng phân vùng LUKS là tối thiểu so với những lợi ích về bảo mật.