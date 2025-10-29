---
name: Elementary OS
description: Pengganti ideal untuk Windows dan MacOS
---

![cover](assets/cover.webp)

Elementary OS adalah sistem operasi berbasis Ubuntu, yang dirancang agar sederhana, cepat, dan stabil untuk banyak penggunaan sehari-hari. OS ini merepresentasikan alternatif Linux yang seimbang untuk MacOS dan Windows. Interface grafisnya yang lancar, intuitif, dan tidak berantakan membuatnya mudah dipelajari, bahkan untuk pemula. Sistem ini juga berfokus pada ergonomi, keamanan, dan kinerja.

https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Mengapa memilih Elementary OS

- **Kesederhanaan dan kemudahan penggunaan**: Interface grafis Elementary OS berada di antara MacOS dan Windows. kesamaan ini membuatnya mudah diadopsi, bahkan untuk pengguna yang tidak berpengalaman.

- **Keamanan**: Seperti kebanyakan distribusi Linux, Elementary OS mendapat manfaat dari tingkat keamanan yang tinggi. Pembaruan rutin, manajemen hak, dan tidak adanya virus umum menjadikannya sistem yang andal.

- **Kecepatan**: Elementary OS adalah distribusi yang ringan. Yang membutuhkan sedikit sumber daya, menjadikannya cepat dan cocok untuk komputer dengan konfigurasi sederhana.

- **Gratis**: Sistem ini sepenuhnya gratis. Namun, saat Anda mengunduhnya, Anda dapat memberikan donasi untuk mendukung para pengembang.

- **Komunitas aktif**: Komunitas tentang Elementary OS beragam dan responsif. Jika Anda menghadapi kesulitan, Anda dapat dengan mudah menemukan bantuan di forum atau media sosial.

## Instalasi dan konfigurasi

### Prasyarat perangkat keras

Sebelum memulai pemasangan, pastikan Anda memiliki peralatan berikut ini:

- **Flash Drive USB** minimal 12 GB
- **Memori RAM** minimal 4 GB
- **Hard Disk sebesar 20 GB** atau lebih untuk penggunaan yang nyaman

## Unduh image ISO

Kunjungi situs web sistem operasi resmi [elementary](https://elementary.io/) dan pilih jumlah yang akan didonasikan untuk mendukung proyek ini. Langkah ini bersifat opsional.

Jika Anda ingin mengunduh image ISO secara gratis, masukkan 0 pada kolom **"Other"** dan mulai mengunduh image ISO sistem.

![0_01](assets/fr/01.webp)

## Membuat Flash Drive USB yang dapat di-booting

Setelah Anda mengunduh image ISO, Anda harus membuatnya dapat di-boot pada Flash Drive USB untuk melanjutkan instalasi.

Unduh perangkat lunak, seperti [Balena Etcher](https://etcher.balena.io/) atau aplikasi yang serupa, kemudian jalankan perangkat lunak tersebut.

Pilih image ISO **Elementary OS** yang telah diunduh sebelumnya, lalu tetapkan flash drive USB Anda sebagai target.

Klik tombol **flash** untuk memulai proses, dan tunggu sampai proses selesai sebelum melepas Flash Drive USB.

![0_02](assets/fr/02.webp)

## Booting flash drive dan akses BIOS

Matikan komputer yang ingin Anda instal Elementary OS, lalu colokkan flash drive USB.

Saat komputer Anda dinyalakan, akses BIOS (`ESC`, `F9`, atau `F11`, tergantung pada mereknya) dan pilih flash drive USB sebagai perangkat boot, lalu tekan `Enter` untuk memulai proses boot.

## Menginstal Elementary OS

Instalasi dimulai secara otomatis jika Flash Drive USB dikonfigurasi dengan benar.

### Pemilihan bahasa

Pilih bahasa yang ingin Anda gunakan untuk menginstal sistem. Anda juga dapat memilih varian regional.

![0_03](assets/fr/03.webp)

![0_04](assets/fr/04.webp)

### Tata letak keyboard

Pilih tata letak yang sesuai dengan keyboard Anda. Sebuah tampilan disediakan untuk memeriksa apakah tuts menghasilkan karakter yang benar.

![0_05](assets/fr/05.webp)

![0_06](assets/fr/06.webp)

### Mode uji

Elementary OS memungkinkan Anda menguji sistem sebelum menginstalnya. Mode ini memungkinkan Anda menjelajahi Interface tanpa memodifikasi apa pun pada hard disk.

### Menjalankan penginstalan

- Klik **"Erase disk and install"** untuk menginstal secara langsung pada seluruh disk.
- Klik **"Custom install"** jika Anda ingin mengelola partisi secara manual.

![0_07](assets/fr/07.webp)

### Pemilihan disk

Pilih disk tempat Elementary OS akan diinstal, lalu klik tombol Lanjutkan.

![0_08](assets/fr/08.webp)

### Enkripsi disk

Sebuah opsi memungkinkan Anda untuk mengenkripsi disk untuk **mengamankan data Anda**. Anda harus menetapkan kata sandi yang kuat untuk mengaktifkan perlindungan ini. Namun, ini bersifat opsional.

![0_09](assets/fr/09.webp)

![0_10](assets/fr/10.webp)

### Menjalankan penginstalan

Sebelum meluncurkan penginstalan, Anda dapat mengizinkan penginstalan otomatis driver perangkat keras tambahan, tergantung pada kompatibilitas komputer Anda.

- Klik "**Erase and install**" untuk memulai pemasangan.
- Tunggu hingga proses selesai.

![0_11](assets/fr/11.webp)

![0_12](assets/fr/12.webp)

### Mulai ulang

Setelah selesai, klik tombol **enter** untuk memulai ulang, kemudian lepaskan Flash Drive USB pada saat yang tepat untuk menghindari pengulangan instalasi.

![0_13](assets/fr/13.webp)

## Konfigurasi setelah pemasangan

Setelah reboot, diperlukan beberapa langkah tambahan.

![0_14](assets/fr/14.webp)

### Pemilihan bahasa

Konfirmasikan atau ubah bahasa sistem saat masuk.

![0_15](assets/fr/15.webp)

### Tata letak keyboard

Pastikan tata letak keyboard sesuai dengan yang Anda inginkan.

![0_16](assets/fr/05.webp)

### Membuat akun pengguna

Kaitkan akun pengguna dengan sistem operasi Anda dengan menentukan nama pengguna dan kemudian mengamankan akses ke data Anda dengan kata sandi alfanumerik yang terdiri dari setidaknya 20 karakter dan simbol.

![0_17](assets/fr/17.webp)

### Koneksi pertama

Ketika Anda masuk untuk pertama kalinya, Elementary OS memungkinkan Anda mempersonalisasi lingkungan Anda dengan beberapa pengaturan dasar.

![0_18](assets/fr/18.webp)

![0_19](assets/fr/19.webp)

## Pembaruan sistem

Sebelum digunakan dalam jangka waktu lama, penting untuk memperbarui sistem dengan patch terbaru.


### Opsi 1: Memperbarui melalui grafik Interface

Masuk ke **AppCenter** dan klik ikon pembaruan di sudut kanan atas. Tunggu hingga pembaruan terdaftar, lalu klik **"Update All"** untuk memulai penginstalan.

![0_20](assets/fr/20.webp)

![0_21](assets/fr/21.webp)

### Opsi 2: Memperbarui melalui terminal

Anda juga dapat melakukan pembaruan dari baris perintah melalui terminal Anda: opsi yang direkomendasikan untuk keakuratannya.

```shell
sudo apt update
```

```shell
sudo apt full-upgrade
```
Untuk pembaruan pertama Anda, sistem operasi memerlukan kata sandi pengguna dan konfirmasi untuk memperbarui paket perangkat lunak, bahkan di kernel Elementary.

## Konfigurasi lingkungan kerja

Elementary OS hanya menyertakan aplikasi yang penting. Untuk menyesuaikan lingkungan Anda dengan kebutuhan Anda, terutama jika Anda adalah seorang pengembang, kami sarankan untuk menginstal aplikasi tambahan.

- Anda dapat menambahkan dependensi yang berguna dengan perintah berikut (disesuaikan dengan kebutuhan Anda):

```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```

Perintah ini menginstal **Git**, **Python 3**, **pip**, **tool kompiler**, **wget**, **curl**, **zsh**, **make**, **snapd**, dan **vscode** untuk menyiapkan lingkungan pengembangan dasar.

Elementary OS sekarang sudah terpasang dan berjalan di komputer Anda. Filosofinya yang mengutamakan kesederhanaan, keringanan, dan keanggunan menjadikannya pilihan yang sangat baik untuk penggunaan pribadi maupun profesional. Anda mendapatkan sistem yang stabil, lancar, dan tidak berantakan, siap untuk disesuaikan sesuai dengan preferensi Anda. Baik untuk pengembangan, pekerjaan kantor, atau penjelajahan sehari-hari, semuanya sudah tersedia untuk membangun lingkungan kerja yang efisien, intuitif, dan menyenangkan. Anda juga bisa melihat tutorial kami tentang Fedora, sebuah distribusi Linux yang sama sederhananya, tangguh, dan modular.

https://planb.academy/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0
