---
name: Zorin OS
description: Panduan lengkap untuk menginstal dan menggunakan Zorin OS sebagai alternatif modern untuk Windows
---

![cover](assets/cover.webp)



## Pendahuluan



Sistem operasi (OS) adalah perangkat lunak dasar yang memungkinkan komputer berfungsi: mengelola perangkat keras, perangkat lunak, keamanan, dan antarmuka pengguna.


Zorin OS adalah distribusi Linux yang dirancang khusus untuk memudahkan transisi dari Windows, sekaligus menawarkan manfaat perangkat lunak sumber terbuka: keamanan, stabilitas, privasi, dan kinerja.



Berdasarkan Ubuntu LTS, Zorin OS menggabungkan kompatibilitas perangkat lunak yang tinggi dengan antarmuka yang akrab dan dapat disesuaikan, menjadikannya alternatif yang kredibel dan dapat diakses untuk Windows.



## Mengapa Zorin OS?





- Interface sudah tidak asing lagi**: Penampilan seperti Windows (menu mulai, bilah tugas)
- Transisi yang mudah**: dirancang untuk pengguna yang berasal dari Windows
- Keamanan yang ditingkatkan**: Arsitektur Linux, lebih sedikit terkena virus
- Menghormati privasi**: tidak ada pengumpulan data yang mengganggu
- Performa yang dioptimalkan**: bekerja dengan baik pada mesin yang sederhana
- Basis Ubuntu LTS**: stabilitas, pembaruan rutin, dan kompatibilitas yang luas
- Personalisasi tingkat lanjut**: melalui alat bantu Zorin Appearance.



## Instalasi dan konfigurasi



### 1. Prasyarat



**Peralatan yang dibutuhkan:**





- Kunci USB minimal **8 GB** (disarankan 12 GB);
- Komputer dengan setidaknya **25 GB ruang disk kosong**
- Koneksi internet (disarankan).



### 2. Unduh Zorin OS





- Kunjungi situs web resminya: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Pilih **Zorin OS Core** (disarankan versi gratis)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Unduh gambar ISO



Zorin OS juga menawarkan file :





- Zorin OS Lite** (komputer lama)
- Zorin OS Pro** (berbasis biaya, dengan fitur dan dukungan canggih)



## Membuat kunci USB yang dapat di-booting



Anda dapat menggunakan beberapa alat bantu, seperti Balena Etcher :





- Unduh dan instal [Balena Etcher](https://etcher.balena.io/).
- Buka Balena Etcher, kemudian pilih gambar ISO Zorin.
- Pilih kunci USB sebagai media tujuan.
- Klik Flash dan tunggu sampai prosesnya selesai.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Booting kunci dan akses BIOS



Matikan komputer tempat Anda ingin menginstal Zorin OS, lalu colokkan kunci USB.


Saat komputer Anda dinyalakan, akses BIOS (`ESC`, `F9`, atau `F11`, tergantung pada mereknya) dan pilih kunci USB sebagai perangkat boot, lalu tekan `Enter` untuk memulai proses boot.





- Pada saat pengaktifan, pilih **Coba atau Instal Zorin OS**.



![capture](assets/fr/08.webp)





- Jika Anda memiliki kartu grafis NVIDIA, pilih **Coba atau Instal Zorin OS (driver NVIDIA modern)**.
- Harap tunggu sementara file diperiksa.



![capture](assets/fr/09.webp)





- Pada penginstal Zorin OS, pilih bahasa **Prancis** lalu klik Install **Zorin OS**.



![capture](assets/fr/10.webp)





- Pilih tata letak keyboard.



![capture](assets/fr/11.webp)





- Centang kotak **Unduh pembaruan selama instalasi Zorin OS** dan **Instal perangkat lunak pihak ketiga untuk perangkat keras grafis dan Wi-Fi serta format media tambahan**.



![capture](assets/fr/12.webp)





- Untuk menginstal Zorin OS pada seluruh disk: pilih **Hapus disk dan instal Zorin OS**.



![capture](assets/fr/14.webp)



Untuk menginstal Zorin OS di samping Windows (dual-boot) :





- Pilih **Instal Zorin OS di samping Windows Boot Manager**.



![capture](assets/fr/15.webp)





- Jika Anda belum mempartisi disk Anda, pilih ruang disk yang ingin Anda alokasikan untuk Zorin OS, lalu klik **Instal sekarang**.



![capture](assets/fr/16.webp)





- Konfirmasikan perubahan pada disk dua kali.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Pilih area geografis **Paris**.



![capture](assets/fr/18.webp)





- Buat akun pengguna dan beri nama komputer Anda.



![capture](assets/fr/19.webp)





- Harap tunggu sementara Zorin OS diinstal.



![capture](assets/fr/20.webp)





- Setelah instalasi selesai, klik **Restart Now**.



![capture](assets/fr/21.webp)





- Lepaskan kunci instalasi USB dan tekan Enter.



![capture](assets/fr/22.webp)



## Menemukan dan menggunakan Zorin OS



### Start-up pertama



Ketika Anda menyalakan komputer, Anda akan dibawa ke GRUB - manajer boot Linux. Secara default, **Zorin OS** dipilih; setelah 30 detik, sistem akan mulai secara otomatis.



![capture](assets/fr/23.webp)



Jika Anda telah menginstal Zorin OS sebagai dual-boot dengan Windows, Anda dapat melakukan booting ke Windows dengan memilih **Windows Boot Manager**.



Masuk dengan akun pengguna Anda :



![capture](assets/fr/24.webp)



Pada saat pertama kali dinyalakan, aplikasi **Selamat Datang di Zorin OS** diluncurkan untuk membantu Anda menemukan sistem operasi baru Anda.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Memperbarui sistem



Manajer Pembaruan akan segera terbuka untuk memberi tahu Anda bahwa pembaruan telah tersedia. Instal dengan mengeklik tombol **Instal sekarang**.



![capture](assets/fr/33.webp)



Anda dapat memeriksa pembaruan secara manual di **Software** > Aplikasi Pembaruan:



![capture](assets/fr/34.webp)



### Personalisasi



Hal pertama yang harus dilakukan di Zorin OS adalah memilih **tata letak desktop** yang paling nyaman bagi Anda. Anda akan menemukan tata letak yang mirip dengan yang ditemukan di Windows (dan bahkan lebih dari itu dengan versi Pro).



Untuk melakukannya, buka **Zorin Appareance** > **Ketik** :



![capture](assets/fr/35.webp)



Kemudian buka **Pengaturan** untuk menyesuaikan sistem Anda:


**Suara - Pengaturan - Zorin OS



![capture](assets/fr/36.webp)



**Akun online - Pengaturan - Zorin OS



![capture](assets/fr/37.webp)



### Aplikasi



Ada beberapa cara untuk menginstal aplikasi:





- Software**, toko aplikasi Zorin OS. Aplikasi berasal dari beberapa sumber: apt, Flatpak dan Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (baris perintah) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Untuk informasi lebih lanjut tentang cara menginstal aplikasi di Zorin OS, lihat halaman ini: [Instal Aplikasi (zorin.com)](https://zorin.com/help/install-apps/).



### Aplikasi Windows



Untuk menginstal aplikasi Windows, mulailah dengan menginstal paket **zorin-windows-app-support** melalui Terminal :



```bash
sudo apt install zorin-windows-app-support
```



Untuk daftar aplikasi Windows yang kompatibel dan tingkat kompatibilitasnya, lihat halaman [Database Aplikasi Wine] (https://appdb.winehq.org/). Di sana Anda akan menemukan lencana berikut ini, yang sesuai dengan tingkat kompatibilitas (dari yang terbaik hingga yang terburuk): Platinum, Emas, Perak, Perunggu, dan Sampah.



Untuk menginstal aplikasi Windows .exe atau .msi, Anda memiliki dua pilihan:





- Buka **PlayOnLinux** dan klik tombol **Instal** untuk menelusuri aplikasi dan game yang kompatibel.



![capture](assets/fr/41.webp)





- Klik dua kali pada file **.exe atau .msi** aplikasi dan biarkan program instalasi memandu Anda.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Kesimpulan dan sumber daya tambahan



Zorin OS adalah alternatif yang solid dan terjangkau untuk Windows, yang menggabungkan kesederhanaan, keamanan, dan privasi.



Hal ini memungkinkan transisi yang mulus ke Linux, tanpa mengorbankan kenyamanan atau produktivitas.



Untuk lebih melindungi kehidupan digital Anda, kami sarankan untuk menggunakan layanan yang ramah privasi, terutama untuk komunikasi terenkripsi:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2