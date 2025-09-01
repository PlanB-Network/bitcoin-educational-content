---
name: Whonix
description: Menjaga privasi dan kerahasiaan Anda.
---

![cover](assets/cover.webp)



**Whonix** adalah distribusi Linux yang berbasiskan **Debian**, yang dirancang untuk menyediakan lingkungan yang menggabungkan **keamanan**, **anonimitas**, dan **privasi**. Mudah dipelajari, dan kompatibel dengan berbagai antarmuka (mesin virtual, Qubes OS, mode Live), distribusi ini mencakup perutean lalu lintas jaringan secara default melalui **Tor**, **double firewall** (satu firewall di Gateway dan satu lagi di Workstation), **perlindungan penuh terhadap kebocoran IP/DNS**, serta alat bantu yang secara efektif menyembunyikan aktivitas Anda dari para pengamat jaringan, termasuk ISP. Lebih dari sekadar sistem anonim, **Whonix** adalah lingkungan pengembangan yang aman dan lengkap.



## Mengapa memilih Whonix?





- Gratis**: Seperti kebanyakan distribusi Linux, Whonix merupakan sistem sumber terbuka yang dilisensikan secara gratis. Sistem ini dikembangkan secara open source, dengan komunitas yang aktif dan transparan.
- Privasi, keamanan, dan anonimitas**: Tujuan utama Whonix adalah menawarkan lingkungan yang sangat aman, di mana semua data Anda terlindungi dan komunikasi Anda dienkripsi melalui jaringan Tor.
- Mudah digunakan**: Whonix menawarkan Interface grafis yang intuitif dan telah dikonfigurasi sebelumnya, cocok bahkan untuk pengguna pemula. Tidak perlu menjadi seorang ahli untuk mendapatkan manfaat dari perlindungan tingkat lanjut.
- Lingkungan yang ideal untuk pengembangan yang aman**: Whonix memungkinkan Anda mengembangkan, menguji, mengaudit, atau menjalankan program tanpa harus mengungkap IP Address asli Anda atau mengekspos kebiasaan browsing atau komunikasi jaringan Anda.
- Sesi sekali pakai dan mode Live**: Whonix dapat diluncurkan dalam mode Live atau melalui mesin sekali pakai (misalnya melalui **Qubes OS**), memungkinkan tugas-tugas penting dilakukan tanpa meninggalkan jejak yang terus-menerus setelah sesi berakhir.
- Instalasi yang relatif sederhana**: Gambar siap pakai disediakan untuk instalasi cepat di mesin virtual (VirtualBox, KVM, Qubes). Sistem ini didokumentasikan dan diperbarui secara berkala.



## Instalasi dan konfigurasi



Sebelum beralih ke instalasi Whonix, penting untuk dicatat bahwa distribusi ini **belum tersedia secara resmi** sebagai sistem utama yang dapat diinstal secara langsung pada disk Hard (dalam mode bare metal). Dengan kata lain, Anda **belum dapat menginstal Whonix sebagai sistem operasi hos klasik**, seperti Ubuntu atau Debian standar.



Namun, beberapa edisi tersedia, memungkinkan Whonix untuk digunakan secara **volatile** (mode Live, sesi sementara) atau **persisten** (melalui mesin virtual atau integrasi dalam Qubes OS).



Untuk penggunaan jangka panjang dan stabil, **virtualisasi saat ini merupakan satu-satunya metode yang direkomendasikan secara resmi**. Anda bisa menjalankan Whonix menggunakan **VirtualBox** (Whonix-Gateway dan Whonix-Workstation) atau mengintegrasikannya ke dalam sistem seperti **Qubes OS**. Dalam tutorial ini, kita akan fokus pada instalasi VirtualBox.



### Prasyarat



Sebelum Anda dapat menginstal Whonix dalam mode virtual, pastikan mesin Anda memenuhi persyaratan teknis minimum. Virtualisasi membutuhkan sumber daya tertentu yang tidak dapat ditawarkan oleh semua komputer. Oleh karena itu, prosesor Anda harus mendukung teknologi virtualisasi (Intel VT-x atau AMD-V), dan opsi ini diaktifkan di BIOS/UEFI.



Berikut ini adalah spesifikasi yang direkomendasikan untuk pengalaman yang lancar dan stabil dengan Whonix:





- Memori Akses Acak (RAM)**: minimal **8 GB** sangat disarankan. Semakin banyak RAM yang Anda miliki, semakin banyak sumber daya yang dapat Anda alokasikan ke mesin virtual (Gateway dan Workstation), sehingga meningkatkan kinerja.
- Ruang disk yang tersedia**: sediakan setidaknya 30 GB ruang disk kosong**. Ini termasuk ruang yang diperlukan untuk dua mesin virtual, file sistem, dan data atau snapshot.
- Prosesor**: prosesor dengan setidaknya **4 inti fisik** (8 thread logis) direkomendasikan, terutama jika Anda ingin menjalankan layanan atau alat lain secara paralel.



### Unduh Whonix



Whonix tersedia dalam beberapa edisi, tergantung pada jenis lingkungan yang ingin Anda gunakan. Untuk sebagian besar pengguna (Windows, Linux atau MacOs), edisi VirtualBox adalah yang paling mudah diatur. Anda bisa mengunduh gambar langsung dari [situs web resmi](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **tidak kompatibel** dengan MacBook yang menggunakan prosesor Apple Silicon (arsitektur ARM).



## Menginstal VirtualBox



Untuk menjalankan Whonix, Anda memerlukan **hypervisor** seperti VirtualBox, Qubes, atau KVM.



Setelah Anda mengunduh file, instal seperti yang Anda lakukan pada perangkat lunak lainnya. Terima opsi default kecuali Anda memiliki persyaratan khusus. Apakah Anda tersesat? Lihat panduan kami untuk menggunakan VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Mengimpor Whonix



Setelah VirtualBox terinstal, Anda dapat mengimpor file Whonix `.ova` yang telah Anda unduh sebelumnya (`Whonix-Gateway-Xfce.ova` dan `Whonix-Workstation-Xfce.ova`).



Buka VirtualBox, lalu klik **File → Impor alat**.


Pilih file `.ova` yang sesuai (mulai dengan Gateway).



![0_03](assets/fr/03.webp)



Pilih lokasi di mana file mesin virtual Whonix akan disimpan.



![0_04](assets/fr/04.webp)



Terima persyaratan penggunaan, lalu luncurkan impor dan tunggu hingga prosesnya selesai.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Konfigurasi Whonix



Sebelum memulai Whonix, penting untuk menyesuaikan beberapa **pengaturan sistem** untuk memastikan kinerja yang lebih baik:



Pilih mesin virtual **Whonix-Workstation-Xfce**, lalu klik **Konfigurasi**.



![0_06](assets/fr/07.webp)



Buka tab **System**, di mana alokasi RAM default adalah 2048 MB. Kami menyarankan Anda untuk meningkatkannya menjadi 4096 MB (4 GB) untuk kelancaran yang lebih baik, terutama jika Anda bermaksud membuka beberapa aplikasi atau bekerja dalam sesi yang panjang. Gateway dapat tetap menggunakan 2048 MB, kecuali jika Anda menggunakan banyak koneksi Tor secara paralel.



![0_08](assets/fr/08.webp)



### Memulai dengan Whonix



Agar Whonix dapat bekerja dengan baik dan aman, **Anda harus mengikuti urutan penginstalan ini**:



Pertama, jalankan mesin **Whonix-Gateway-Xfce**. Mesin ini bertanggung jawab untuk merutekan semua lalu lintas melalui jaringan **Tor**. Tanpa gateway yang berjalan, tidak ada lalu lintas yang akan dirutekan melalui Tor dan Anda akan kehilangan anonimitas.



![0_09](assets/fr/09.webp)



Setelah Gateway diluncurkan sepenuhnya (Anda akan melihat Tor terhubung), Anda dapat memulai **Whonix-Workstation-Xfce**, yang secara otomatis akan terhubung melalui Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Pembaruan sistem



Masuk ke terminal, masukkan perintah berikut untuk memperbarui daftar paket:



```shell
sudo apt update
```



Kemudian jalankan perintah berikut untuk menginstal pembaruan yang tersedia:



```shell
sudo apt full-upgrade
```



## Temukan Whonix



**Whonix** adalah sistem yang dirancang untuk menyediakan lingkungan komputasi yang **aman**, **anonim**, dan **rahasia**, yang ideal untuk menjelajahi Internet tanpa mengorbankan identitas atau data Anda. Untuk mencapai hal ini, sistem ini dilengkapi dengan sejumlah aplikasi sehari-hari yang berguna yang dirancang untuk memperkuat keamanan digital Anda sejak awal.


### KeepassXC



**KeePassXC** adalah pengelola kata sandi terintegrasi dari Whonix. Ini memungkinkan Anda untuk **membuat, menyimpan, dan mengelola** kata sandi Anda dengan aman, tanpa harus mengingat semuanya secara manual. Kata sandi disimpan dalam basis data terenkripsi, dilindungi oleh kata sandi utama.



### Peramban Tor



**Tor Browser** adalah peramban web default Whonix. Peramban ini mengandalkan jaringan **Tor**, yang mengarahkan lalu lintas Anda melalui beberapa relay di seluruh dunia, sehingga hampir tidak mungkin untuk mengidentifikasi IP Address Anda yang sebenarnya.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** adalah Bitcoin Wallet yang ringan dan cepat, sudah terinstal di Whonix untuk memungkinkan Anda mengelola **transaksi mata uang kripto** secara anonim. Ia tidak mengunduh seluruh Blockchain tetapi menggunakan server jarak jauh untuk mendapatkan informasi yang diperlukan, membuatnya jauh lebih ringan daripada Wallet penuh.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix lebih dari sekadar sistem operasi: Whonix adalah **lingkungan aman** asli yang dirancang untuk melindungi anonimitas, privasi, dan aktivitas sensitif Anda. Berkat arsitektur berbasis Tor, partisi cerdas antara Gateway dan Workstation, dan alat yang sudah terinstal seperti Tor Browser, KeePassXC, dan Electrum, sistem operasi ini menawarkan solusi siap pakai bagi siapa pun yang ingin **menjelajah secara anonim**, **bekerja dengan aman**, atau **mengelola data rahasia**.



Untuk memperkuat keamanan pada sistem Unix Anda, lihatlah tutorial kami tentang mengaudit mesin Anda: periksa celah keamanan pada sistem operasi Anda dan pastikan data Anda tidak terganggu.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af