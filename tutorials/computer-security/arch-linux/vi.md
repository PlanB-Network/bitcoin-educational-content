---
name: Arch Linux
description: Thiết kế hệ thống phân phối tối giản, hiệu suất cao theo triết lý KISS.
---

![cover](assets/cover.webp)



Arch Linux là một bản phân phối nổi tiếng với tính mạnh mẽ, hiệu suất và khả năng thích ứng, đặc biệt là cho mục đích phát triển. Nó mang lại sự ổn định tuyệt vời và một môi trường thuận lợi cho việc tùy chỉnh, được hỗ trợ bởi trình quản lý gói cực kỳ nhanh chóng và đáng tin cậy. Triết lý của nó dựa trên nguyên tắc **KISS** (Giữ mọi thứ đơn giản, đừng làm rối tung lên*): cung cấp một bản phân phối nhẹ nhàng, đơn giản, nhanh chóng và gọn gàng, đồng thời mang lại sự tự do tối đa cho người dùng.



## Tại sao nên chọn Arch Linux?





- Miễn phí và mã nguồn mở**: Giống như hầu hết các bản phân phối Linux, Arch Linux hoàn toàn miễn phí. Không có phí cấp phép, khiến nó trở thành lựa chọn tuyệt vời cho sinh viên, người làm việc tự do hoặc những người đam mê.
- Triết lý KISS**: Arch được thiết kế đơn giản, nhẹ nhàng và hiệu quả. Nó chỉ cung cấp những yếu tố thiết yếu, cho phép bạn tự do xây dựng môi trường sống theo ý muốn.
- Trình quản lý gói Pacman**: Pacman là trình quản lý gói nhanh, đáng tin cậy và được thiết kế tốt. Nó cho phép cài đặt và cập nhật phần mềm hiệu quả, đồng thời quản lý các gói phụ thuộc một cách chính xác.
- Tài liệu toàn diện và cộng đồng năng động**: [Arch Wiki](https://wiki.archlinux.org) có lẽ là một trong những tài liệu kỹ thuật tốt nhất trong thế giới Linux. Đây là một mỏ vàng để hiểu rõ những gì bạn đang làm. Cộng đồng, chủ yếu bao gồm những người có kinh nghiệm, rất năng động và có thể giúp bạn nếu bạn gặp khó khăn, miễn là bạn đã tìm hiểu trước.



## Cài đặt và cấu hình



### Điều kiện tiên quyết



Vật liệu cần thiết:





- Một ổ USB có dung lượng tối thiểu **8 GB**
- Tối thiểu 2 GB** RAM
- Một máy tính có ít nhất 20 GB dung lượng đĩa trống



### Tải xuống



![0_1](assets/fr/01.webp)



Từ năm 2017, Arch Linux không còn hỗ trợ kiến trúc 32 bit nữa. Chỉ còn phiên bản 64 bit.





- Truy cập [trang web chính thức](https://mir.archlinux.fr/iso/latest/) để tải xuống phiên bản chính thức mới nhất của ảnh ISO.



### Tạo khóa khởi động



Để tạo ổ đĩa flash USB có thể khởi động, bạn có thể sử dụng một công cụ như **Balena Etcher**:





- Tải Balena Etcher từ [trang web chính thức](https://etcher.balena.io).
- Khởi chạy phần mềm, chọn ảnh ISO Arch Linux.
- Chọn khóa USB của bạn làm thiết bị mục tiêu.
- Nhấp vào **Flash** để bắt đầu tạo khóa khởi động.



![0_2](assets/fr/02.webp)



## Cài đặt Arch Linux



## Khởi động bằng khóa USB





- Tắt máy tính của bạn hoàn toàn
- Cắm ổ USB có thể khởi động
- Khởi động lại và vào BIOS/UEFI bằng cách nhấn **F1**, **Escape**, **F9**, v.v. (tùy thuộc vào kiểu máy của bạn)
- Trong menu khởi động, hãy chọn ổ USB làm thiết bị khởi động. Nếu mọi thứ được thiết lập chính xác, bạn sẽ được đưa đến màn hình khởi động Arch Linux Interface.



## Khởi chạy cài đặt



Trên màn hình khởi động, hãy chọn tùy chọn đầu tiên để khởi chạy cài đặt. Lưu ý rằng Arch Linux không cung cấp trình cài đặt đồ họa. Sau khi khởi chạy, bạn sẽ được chuyển đến terminal ở chế độ root.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Cấu hình bàn phím



Bạn có thể hiển thị các bố cục có sẵn bằng:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Sau đó tải một bố cục với:



```shell
loadkeys nom-disposition
```



Theo mặc định, bàn phím là tiếng Anh (qwerty), nhưng bạn có thể chuyển sang `azerty` bằng `loadkeys fr`.



### Cài đặt ngày và giờ



Arch Linux sử dụng công cụ `timedatectl` để quản lý đồng hồ hệ thống.



![0_7](assets/fr/07.webp)





- Đặt múi giờ của bạn bằng:


```shell
timedatectl set-timezone Europe/Paris
```





- Kiểm tra xem đồng bộ hóa tự động có được bật không bằng:


```shell
timedatectl status
```





- Kích hoạt nếu cần thiết:


```shell
timedatectl set-ntp true
```




Thao tác này sẽ kích hoạt NTP, giao thức đồng bộ hóa tự động với máy chủ thời gian. Bước này rất quan trọng để tránh lỗi ngày tháng khi cài đặt gói hoặc cấu hình chứng chỉ SSL sau này.



### Phân vùng đĩa





- Kiểm tra xem hệ thống của bạn khởi động ở **UEFI** hay **BIOS** bằng:



```shell
ls /sys/firmware/efi
```



Nếu tệp tồn tại, bạn đang ở chế độ **UEFI**. Nếu không, bạn đang ở chế độ **BIOS (Legacy)**.




- Liệt kê các đĩa có sẵn:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Khởi động Trình quản lý phân vùng:



```shell
cfdisk /dev/nom-du-disque
```



Chọn **GPT** nếu bạn đang ở UEFI, **DOS** nếu bạn đang ở BIOS.



![0_9](assets/fr/09.webp)



#### Điểm số để tạo




- Ở chế độ UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- Trong BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Chọn **Ghi**, nhập **có**, sau đó nhập **Thoát**.



### Định dạng phân vùng





- UEFI**:



```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```





- BIOS**:



```shell
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```



![0_11](assets/fr/11.webp)



### Cài đặt hệ thống cơ bản



Gắn phân vùng **root**:





- Trên BIOS:


```shell
mount /dev/sda2 /mnt
```




- trên UEFI:


```shell
mount /dev/sda3 /mnt
```



Sau đó cài đặt các gói cần thiết:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate là tệp **fstab**, cho phép hệ điều hành tự động quản lý việc gắn phân vùng ở mỗi lần khởi động mà không cần can thiệp thủ công:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Vào môi trường **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Cấu hình hệ thống





- Cài đặt trình soạn thảo văn bản để chỉnh sửa:



```shell
pacman -S vim
```





- Cài đặt ngôn ngữ:


Chỉnh sửa `/etc/locale.gen` sau đó bỏ chú thích dòng `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Đặt tên máy:



```shell
echo nom_machine > /etc/hostname
```





- Đặt mật khẩu root:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Cài đặt GRUB



Cài đặt:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Sau khi tải xuống, bạn cần cài đặt theo định dạng phân vùng đĩa.




- Đối với **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Đối với **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Hoàn thiện





- Thoát khỏi môi trường chroot:


```shell
exit
```





- Xóa các phân vùng:


```shell
umount -R /mnt
```





- Khởi động lại:


```shell
reboot
```



Khi khởi động, hãy đăng nhập bằng tên đăng nhập **root** và mật khẩu của bạn.



![0_18](assets/fr/18.webp)


## Kết nối mạng sau khi khởi động lại



Có thể xảy ra trường hợp không có kết nối mạng nào hoạt động khi khởi động lại. Bạn có thể liệt kê các giao diện bằng:



```shell
ip link
```



Sau đó cấu hình mạng Interface bằng cách nhập văn bản sau vào thiết bị đầu cuối



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Đồ họa Interface (GNOME)



Theo mặc định, **Arch Linux** không chứa Interface đồ họa. Để thêm một:



Cập nhật hệ thống:



```shell
pacman -Syu
```



Cài đặt **Xorg** bằng lệnh sau và nhấn enter mỗi lần để giữ nguyên các lựa chọn mặc định:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Cài đặt **GNOME** bằng lệnh sau và nhập mỗi lần để giữ nguyên các lựa chọn mặc định:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Kích hoạt **trình quản lý phiên**:



```shell
systemctl enable gdm
systemctl start gdm
```



Hệ thống sẽ tự động khởi động lại và bạn sẽ thấy giao diện đăng nhập đồ họa Interface. Đăng nhập bằng tên người dùng và mật khẩu root.



![0_21](assets/fr/21.webp)



## Tạo người dùng



Khi vào **Interface GNOME**, bạn cần tạo một người dùng mới để bảo mật hơn và sử dụng an toàn, không rủi ro. Vào ứng dụng và chọn tùy chọn "console" để khởi chạy terminal.





- Thêm người dùng:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Cài đặt **sudo**:


```shell
pacman -S sudo
```





- Kích hoạt quyền **sudo**:



```shell
EDITOR=nano visudo
```





- Sau đó bỏ chú thích ở dòng:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Khởi động lại hệ thống và đăng nhập bằng tên người dùng của bạn.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Cài đặt phần mềm



Vì Arch Linux là hệ điều hành tối giản, nhiều phần mềm không được cài đặt theo mặc định. Để thêm những gì bạn cần, hãy nhập lệnh sau:



```shell
pacman -S nom_du_paquet_a_installe
```



Ví dụ, để cài đặt trình soạn thảo văn bản **nano**, bạn có thể nhập:



```shell
pacman -S nano
```



Để cài đặt trình duyệt web nhẹ như `firefox`, hãy sử dụng:



```shell
pacman -S firefox
```



Cuối cùng, nếu bạn muốn thêm các công cụ mạng thiết yếu như `net-tools`, lệnh sẽ là:



```shell
pacman -S net-tools
```



Đừng quên rằng bạn có thể cài đặt nhiều gói trong một lệnh bằng cách liệt kê chúng riêng biệt:



```shell
pacman -S vim firefox net-tools
```



Arch Linux nổi bật với tính ổn định vượt trội, triết lý tối giản và độ bền bỉ, khiến nó trở thành lựa chọn lý tưởng cho các môi trường phát triển. Bằng cách chỉ cung cấp những tính năng thiết yếu, Arch Linux mang đến một nền tảng nhẹ, hiệu suất cao, dễ dàng tùy chỉnh theo nhu cầu cụ thể của bạn. Cách tiếp cận tối giản này cũng ưu tiên khả năng kiểm soát hệ thống tốt hơn, tăng cường bảo mật bằng cách hạn chế bề mặt tấn công. Nhờ cộng đồng năng động và tài liệu hướng dẫn đầy đủ, Arch Linux có thể giúp bạn tạo ra một môi trường an toàn, linh hoạt, được tối ưu hóa cho phát triển chuyên nghiệp.



Nếu bạn thích bắt đầu với Arch Linux, bạn sẽ thích hướng dẫn của chúng tôi về **Fedora OS**, một hệ điều hành dạng mô-đun, an toàn và mạnh mẽ, có thể thích ứng với nhu cầu và mục đích sử dụng của bạn.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1