---
name: Arch Linux
description: Distribusi minimalis dan berkinerja tinggi yang dirancang sesuai dengan filosofi KISS.
---

![cover](assets/cover.webp)



Arch Linux adalah distribusi yang terkenal dengan ketangguhan, kinerja, dan kemampuan beradaptasi, terutama untuk tujuan pengembangan. Linux menawarkan stabilitas yang sangat baik dan lingkungan yang kondusif untuk kustomisasi, didukung oleh manajer paket yang sangat cepat dan andal. Filosofinya didasarkan pada prinsip **KISS** (*Keep It Simple, Stupid*): menawarkan distribusi yang ringan, sederhana, cepat, dan tidak berantakan, sambil memberikan banyak kebebasan kepada pengguna.



## Mengapa memilih Arch Linux?





- Gratis dan sumber terbuka**: Seperti kebanyakan distribusi Linux, Arch Linux benar-benar gratis. Tidak ada biaya lisensi, menjadikannya pilihan yang sangat baik untuk pelajar, pekerja lepas, atau penggemar.
- Filosofi KISS**: Arch dirancang agar sederhana, ringan dan efisien. Ini hanya menyediakan hal-hal yang penting, memungkinkan Anda untuk membangun lingkungan Anda à la carte.
- Manajer paket Pacman**: Pacman adalah pengelola paket yang cepat, andal, dan dirancang dengan baik. Ini memungkinkan instalasi dan pembaruan perangkat lunak yang efisien, dan mengelola ketergantungan dengan presisi.
- Dokumentasi yang komprehensif dan komunitas yang aktif**: [Arch Wiki](https://wiki.archlinux.org) mungkin merupakan salah satu dokumentasi teknis terbaik di dunia Linux. Ini adalah tambang emas untuk memahami apa yang Anda lakukan. Komunitas yang sebagian besar terdiri dari profil-profil yang berpengalaman ini sangat aktif dan dapat membantu Anda jika Anda mengalami kebuntuan, asalkan Anda telah melakukan sedikit riset sebelumnya.



## Instalasi dan konfigurasi



### Prasyarat



Bahan yang dibutuhkan:





- Kunci USB minimal sebesar **8 GB**
- rAM minimum 2 GB** minimum
- Komputer dengan ruang disk kosong minimal 20 GB



### Unduh



![0_1](assets/fr/01.webp)



Sejak 2017, Arch Linux tidak lagi mendukung arsitektur 32-bit. Hanya versi 64-bit yang tersedia.





- Kunjungi [situs web resmi] (https://mir.archlinux.fr/iso/latest/) untuk mengunduh versi resmi terbaru dari citra ISO.



### Membuat kunci yang dapat di-boot



Untuk membuat flash drive USB yang dapat di-boot, Anda dapat menggunakan alat bantu seperti **Balena Etcher**:





- Unduh Balena Etcher dari [situs web resmi](https://etcher.balena.io).
- Luncurkan perangkat lunak, pilih citra ISO Arch Linux.
- Pilih kunci USB Anda sebagai perangkat target.
- Klik **Flash** untuk mulai membuat kunci yang dapat di-boot.



![0_2](assets/fr/02.webp)



## Menginstal Arch Linux



## Mem-boot dengan kunci USB





- Matikan komputer Anda sepenuhnya
- Colokkan kunci USB yang dapat di-boot
- Hidupkan ulang dan masuk ke BIOS/UEFI dengan menekan **F1**, **Escape**, **F9**, dst. (tergantung model Anda)
- Pada menu boot, pilih kunci USB sebagai perangkat boot. Jika semuanya telah diatur dengan benar, Anda akan dibawa ke layar boot Arch Linux Interface.



## Meluncurkan penginstalan



Pada layar boot, pilih opsi pertama untuk meluncurkan instalasi. Perhatikan bahwa Arch Linux tidak menawarkan pemasang grafis. Setelah diluncurkan, Anda akan dibawa ke terminal dalam mode root.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Konfigurasi keyboard



Anda dapat menampilkan tata letak yang tersedia dengan:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Kemudian muat tata letak dengan:



```shell
loadkeys nom-disposition
```



Secara default, papan ketik menggunakan bahasa Inggris (qwerty), tetapi Anda dapat beralih ke `azerty` dengan `loadkeys fr`.



### Mengatur tanggal dan waktu



Arch Linux menggunakan alat `timedatectl` untuk mengelola jam sistem.



![0_7](assets/fr/07.webp)





- Atur zona waktu Anda dengan:


```shell
timedatectl set-timezone Europe/Paris
```





- Periksa apakah sinkronisasi otomatis diaktifkan dengan:


```shell
timedatectl status
```





- Aktifkan jika perlu:


```shell
timedatectl set-ntp true
```




Ini akan mengaktifkan NTP, protokol untuk sinkronisasi otomatis dengan server waktu. Langkah ini penting untuk menghindari kesalahan tanggal saat menginstal paket atau mengonfigurasi sertifikat SSL di kemudian hari.



### Partisi disk





- Periksa apakah sistem Anda melakukan booting di **UEFI** atau **BIOS** dengan file:



```shell
ls /sys/firmware/efi
```



Jika file tersebut ada, berarti Anda menggunakan **UEFI**. Jika tidak, Anda berada di **BIOS (Legacy)**.




- Buat daftar disk yang tersedia:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Mulai Manajer Partisi:



```shell
cfdisk /dev/nom-du-disque
```



Pilih **GPT** jika Anda menggunakan UEFI, **DOS** jika Anda menggunakan BIOS.



![0_9](assets/fr/09.webp)



#### Skor yang akan dibuat




- Dalam mode UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- Di BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Pilih **Tulis**, ketik **yes**, lalu **Berhenti**.



### Memformat partisi





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



### Instalasi sistem dasar



Pasang partisi **root**:





- Pada BIOS:


```shell
mount /dev/sda2 /mnt
```




- di UEFI:


```shell
mount /dev/sda3 /mnt
```



Kemudian instal paket-paket penting:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate file **fstab**, yang memungkinkan sistem operasi untuk secara otomatis mengelola pemasangan partisi pada setiap boot, tanpa intervensi manual:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Masuk ke lingkungan **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Konfigurasi sistem





- Instal editor teks untuk mengedit:



```shell
pacman -S vim
```





- Mengatur bahasa:


Edit `/etc/locale.gen` lalu hapus baris `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Mengatur nama mesin:



```shell
echo nom_machine > /etc/hostname
```





- Atur kata sandi root:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Menginstal GRUB



Instal file:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Setelah diunduh, Anda perlu menginstalnya sesuai dengan format partisi disk.




- Untuk **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Untuk **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Finalisasi





- Keluar dari lingkungan akar:


```shell
exit
```





- Lepaskan partisi:


```shell
umount -R /mnt
```





- Mulai ulang:


```shell
reboot
```



Saat memulai, masuk dengan login dan kata sandi **root** Anda.



![0_18](assets/fr/18.webp)


## Koneksi jaringan setelah reboot



Mungkin saja tidak ada koneksi jaringan yang aktif saat reboot. Anda dapat membuat daftar antarmuka dengan:



```shell
ip link
```



Kemudian konfigurasikan jaringan Interface dengan memasukkan teks berikut di terminal



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Grafis Interface (GNOME)



Secara default, **Arch Linux** tidak memiliki Interface grafis. Untuk menambahkannya:



Perbarui sistem:



```shell
pacman -Syu
```



Instal **Xorg** dengan perintah berikut dan tekan enter setiap kali untuk mempertahankan pilihan default:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Instal **GNOME** dengan perintah berikut dan masukkan setiap kali untuk mempertahankan pilihan default:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktifkan **pengelola sesi**:



```shell
systemctl enable gdm
systemctl start gdm
```



Sistem akan melakukan boot ulang secara otomatis dan Anda akan mendapatkan login grafis Interface. Masuk dengan nama pengguna dan kata sandi root.



![0_21](assets/fr/21.webp)



## Membuat pengguna



Setelah berada di **Interface GNOME**, Anda perlu membuat pengguna baru untuk keamanan yang lebih baik dan penggunaan yang lebih aman dan bebas risiko. Masuk ke aplikasi dan pilih opsi "konsol" untuk meluncurkan terminal.





- Menambahkan pengguna:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Instal **sudo**:


```shell
pacman -S sudo
```





- Aktifkan hak **sudo**:



```shell
EDITOR=nano visudo
```





- Kemudian hapus baris tersebut:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Mulai ulang sistem dan masuk dengan nama pengguna Anda.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Menginstal perangkat lunak



Karena Arch Linux bersifat minimalis, banyak perangkat lunak yang tidak terinstal secara default. Untuk menambahkan apa yang Anda butuhkan, ketik perintah berikut:



```shell
pacman -S nom_du_paquet_a_installe
```



Contohnya, untuk menginstal editor teks **nano**, Anda bisa mengetikkan:



```shell
pacman -S nano
```



Untuk menginstal peramban web yang ringan seperti `firefox`, gunakan:



```shell
pacman -S firefox
```



Terakhir, jika Anda ingin menambahkan alat jaringan yang penting seperti `net-tools`, perintahnya adalah:



```shell
pacman -S net-tools
```



Jangan lupa bahwa Anda bisa menginstal beberapa paket dalam satu perintah dengan mendaftarkannya secara terpisah:



```shell
pacman -S vim firefox net-tools
```



Arch Linux menonjol karena stabilitasnya yang luar biasa, filosofi minimalis, dan ketangguhannya, sehingga menjadikannya pilihan ideal untuk lingkungan pengembangan. Dengan hanya menyediakan hal-hal yang penting, ia menawarkan fondasi yang ringan dan berkinerja tinggi yang mudah disesuaikan dengan kebutuhan spesifik Anda. Pendekatan minimalis ini juga mendukung kontrol yang lebih besar atas sistem, memperkuat keamanan dengan membatasi permukaan serangan. Berkat komunitasnya yang aktif dan dokumentasi yang lengkap, Arch Linux dapat membantu Anda menciptakan lingkungan yang aman dan fleksibel yang dioptimalkan untuk pengembangan profesional.



Jika Anda senang memulai dengan Arch Linux, Anda akan menyukai tutorial kami tentang **Fedora OS**, sebuah sistem operasi yang modular, aman, dan tangguh yang dapat beradaptasi dengan kebutuhan dan penggunaan Anda.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1