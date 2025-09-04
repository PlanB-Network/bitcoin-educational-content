---
name: Debian
description: Distribusi Linux yang terkenal dengan stabilitas, ketahanan, dan kompatibilitasnya.
---

![cover](assets/cover.webp)



Debian adalah distribusi GNU/Linux gratis, yang terkenal dengan ketangguhan dan keandalannya. Kernel Linux dan semua paketnya telah diuji secara ketat untuk memastikan stabilitas yang kokoh dan tingkat keamanan yang tinggi. Cocok untuk server dan workstation, Debian menawarkan pengalaman yang mudah digunakan dan katalog perangkat lunak yang luas. Baik Anda mencari sistem yang aman untuk penggunaan sehari-hari atau lingkungan produksi, Debian adalah pilihan yang tepat.



## Mengapa memilih Debian?





- Gratis dan terbuka**: Debian sepenuhnya open source, menjamin transparansi dan tidak ada biaya lisensi.
- Stabilitas dan keamanan**: setiap rilis telah melalui proses pengujian yang menyeluruh, membuat Debian menjadi salah satu distribusi yang paling dapat diandalkan dan aman di pasaran.
- Komunitas aktif**: komunitas yang luas dan dokumentasi yang ekstensif tersedia untuk mendukung Anda kapan pun Anda membutuhkannya.
- Ringan dan terukur**: Anda dapat menginstal Debian pada mesin dengan sumber daya yang tidak terlalu besar dengan tetap mempertahankan kinerja yang baik.
- Katalog perangkat lunak yang luas**: lebih dari 50.000 paket resmi tersedia melalui repositori.



## Memilih grafik Interface



Debian menawarkan beberapa lingkungan desktop yang sesuai dengan kebutuhan Anda:





- GNOME**: Interface yang modern dan intuitif, ideal untuk pemula. Menawarkan menu grafis yang lancar dan mudah digunakan untuk mengakses aplikasi.
- XFCE**: ringan dan cepat, cocok untuk mesin yang tidak terlalu bertenaga.
- KDE Plasma**: sangat dapat disesuaikan, dengan tampilan seperti Windows.
- Cinnamon**: Interface yang sederhana dan elegan, terinspirasi oleh Windows.
- LXDE / LXQt**: sangat ringan, cocok untuk komputer lama.
- MATE**: sederhana dan klasik, mirip dengan GNOME lama.



💡 Untuk pengalaman yang nyaman dan mudah digunakan, **GNOME sangat direkomendasikan**.



## Menginstalasi dan mengkonfigurasi Debian


### Persyaratan perangkat keras



Sebelum memulai pemasangan, pastikan Anda memiliki peralatan berikut ini:





- Kunci USB**: minimum 8 GB untuk menyimpan citra ISO yang dapat di-booting.
- Memori Akses Acak (Random Access Memory (RAM))**: 4 GB untuk instalasi dan pengoperasian yang lancar.
- Ruang disk**: setidaknya 15 GB ruang kosong untuk sistem dan pembaruan.



### Unduh



Pilihan image Debian tergantung pada arsitektur prosesor Anda:





- AMD64**: unduh edisi "live hybrid" dari daftar [unduh] (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: dapatkan image DVD dari situs web resmi [Debian] (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Arsitektur lain**: temukan ISO yang sesuai dengan arsitektur Anda [di sini](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Membuat kunci USB yang dapat di-booting



Setelah Anda mengunduh citra ISO yang sesuai, lanjutkan dengan membuat media instalasi:




- Unduh Balena Etcher** dari [situs web resmi] (https://etcher.balena.io/), kemudian dapatkan biner untuk sistem Anda dan instal.



![etcher](assets/fr/02.webp)





- Luncurkan Etcher**: buka perangkat lunak dan pilih citra ISO Debian yang telah diunduh sebelumnya.
- Pilih kunci USB**: tentukan kunci Anda (8 GB+) sebagai target.
- Mulai flash**: klik **Flash!** dan tunggu sampai prosesnya selesai.



![flash](assets/fr/03.webp)



Kunci USB Anda sekarang siap untuk mulai menginstal Debian.



## Menginstal Debian pada sistem Anda



### Mem-boot dari kunci USB



Untuk meluncurkan penginstalan dari kunci USB Anda:




- Matikan** komputer sepenuhnya.
- Reboot** lalu akses BIOS/UEFI dengan segera menekan `ESC`, `F2`, `F11` (atau tombol khusus, tergantung merek Anda).
- Pada menu boot, **pilih kunci USB Anda** sebagai perangkat boot.
- Konfirmasikan** dengan tombol Enter untuk memulai image Debian: ini akan membawa Anda ke layar selamat datang pemasang.



### Meluncurkan penginstalan



Layar mulai:



![starting](assets/fr/04.webp)



Saat mem-boot dari stik USB, layar selamat datang Debian menawarkan beberapa opsi:




- Live System**: meluncurkan Debian tanpa menginstalnya, ideal untuk menguji lingkungan.
- Start Installer**: memulai penginstalan secara langsung pada disk Hard.
- Opsi Pemasangan Lanjutan**: memberi Anda akses ke mode pemasangan yang disesuaikan.



Untuk menjelajahi Debian dalam mode live, pilih **Live System** dan konfirmasikan dengan **Enter**. Anda kemudian dapat meluncurkan instalasi dengan mengeklik **Install Debian** di lingkungan live.



![system](assets/fr/05.webp)





- Pilihan bahasa** (opsional)



Pilih bahasa utama sistem Debian Anda dari daftar, lalu klik OK.



![language](assets/fr/06.webp)





- Zona waktu** (GMT)



Pilih zona geografis Anda untuk mengatur tanggal dan waktu secara otomatis.



![timezone](assets/fr/07.webp)





- Tata letak papan ketik



Pilih bahasa dan tata letak keyboard Anda. Gunakan bidang uji bawaan untuk memeriksa apakah setiap tombol menghasilkan karakter yang diharapkan.



![keyboard](assets/fr/08.webp)



### Partisi disk





- Hapus disk**: jika Anda memiliki partisi khusus, opsi ini akan menghapus semua isinya.
- Pemartisian manual**: pilih opsi ini untuk membuat, mengubah ukuran, atau menghapus partisi sesuai kebutuhan.



![disk](assets/fr/09.webp)





- Membuat akun pengguna



Masukkan nama lengkap, nama akun, dan kata sandi yang kuat untuk memastikan sesi Anda aman.



![user](assets/fr/10.webp)





- Ringkasan parameter ** Rangkuman parameter



Ringkasan pilihan Anda akan ditampilkan: centang setiap item dan kembali untuk memodifikasi jika perlu.



![settings](assets/fr/11.webp)





- Meluncurkan penginstalan



Klik **Instalasi** untuk mulai menyalin file dan mengkonfigurasi sistem, lalu tunggu hingga prosesnya selesai.



![install](assets/fr/12.webp)





- Mulai ulang**



Setelah instalasi selesai, boot ulang komputer untuk menerapkan semua konfigurasi dan mengakses sistem Debian baru Anda.



![restart](assets/fr/13.webp)



Saat pengaktifan, masukkan nama pengguna dan kata sandi untuk mengakses sistem.



![login](assets/fr/14.webp)



## Pembaruan sistem



Sebelum Anda mulai menggunakan sistem Anda, sangat penting untuk memperbaruinya. Hal ini memungkinkan Anda untuk mendapatkan manfaat dari tambalan perangkat lunak terbaru, repositori terbaru, dan dalam beberapa kasus, tambalan keamanan untuk sistem operasi itu sendiri.



### Opsi 1: Memperbarui melalui grafis Interface (GNOME)



Jika Anda telah menginstal Debian dengan lingkungan desktop GNOME, Anda dapat melakukan pembaruan secara grafis. Untuk melakukannya, buka aplikasi **Software**, lalu buka tab **Updates**. Kemudian klik **Restart and update** untuk memulai proses.



### Opsi 2: Memperbarui melalui terminal (disarankan)



Metode ini menawarkan kontrol yang lebih lengkap. Metode ini memungkinkan Anda memperbarui repositori, paket perangkat lunak, dan, jika perlu, kernel.




- Buka terminal dengan menggunakan pintasan `Ctrl + Alt + T`.
- Perbarui daftar paket yang tersedia dengan perintah berikut:



```shell
sudo apt update
```



Masukkan kata sandi Anda saat diminta (perhatikan bahwa tidak ada karakter yang akan ditampilkan saat Anda mengetik - ini normal).





- Untuk menginstal pembaruan yang tersedia:



```shell
sudo apt full-upgrade
```



## Temukan tugas-tugas dasar



### Menjelajahi Internet



Peramban web default pada Debian adalah **Firefox**. Jika Anda lebih suka peramban lain, Anda dapat menginstal peramban lain, asalkan tersedia di repositori Debian (seperti Chromium, Brave...).



### Pengolah kata



Paket **LibreOffice** terinstal secara default pada Debian.





- Untuk menulis dokumen, gunakan **LibreOffice Writer**, yang setara dengan Microsoft Word.
- Untuk spreadsheet, **LibreOffice Calc** bertindak sebagai alternatif untuk Excel.
- Terakhir, **LibreOffice Impress** memungkinkan Anda membuat presentasi, seperti halnya PowerPoint.



## Menginstal aplikasi



Ada dua cara untuk menginstal aplikasi pada Debian:



### Metode grafis:



Anda dapat menggunakan **software manager** (dapat diakses melalui Interface grafis) untuk mencari dan menginstal aplikasi dengan mudah.



### Metode baris perintah:



Jika aplikasi yang Anda cari tidak muncul di Interface grafis, atau jika Anda lebih suka terminal, gunakan perintah berikut:



```shell
sudo apt install <name>
```



Ganti `<nama>` dengan nama paket. Misalnya, untuk menginstal `curl`:



```shell
sudo apt install curl
```



### Menginstal paket yang diunduh secara manual:



Jika Anda telah mengunduh file `.deb` (paket Debian), Anda dapat menginstalnya dengan perintah berikut:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Sistem Debian Anda sekarang telah terinstal dan siap digunakan untuk tugas sehari-hari.


Berkat lingkungan desktop **GNOME**, Anda dapat mengakses berbagai macam aplikasi melalui Interface grafis yang mudah digunakan, ideal untuk pemula dan pengguna tingkat lanjut.



Anda juga dapat mengubah lingkungan desktop Anda (misalnya ke XFCE, KDE, dll.) tanpa harus menginstal ulang Debian. Untuk melakukannya, cukup gunakan terminal dan instal lingkungan baru pilihan Anda.



Untuk mempelajari lebih lanjut tentang Debian, dan secara umum tentang distribusi GNU/Linux, saya sarankan Anda untuk membaca kursus ini:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1