---
name: Whonix
description: Menjaga privasi dan kerahasiaan Anda.
---

![cover](assets/cover.webp)

**Whonix** adalah distribusi Linux berbasis **Debian**, yang dirancang untuk menyediakan lingkungan yang menggabungkan **keamanan**, **anonimitas**, dan **privasi**. Mudah dipelajari, dan kompatibel dengan berbagai interface (virtual machines, Qubes OS, Live mode), secara default aplikasi ini mencakup perutean lalu lintas jaringan via **Tor**, **double firewall** (satu firewall pada Gateway dan satu lagi pada Workstation), **perlindungan penuh terhadap kebocoran IP/DNS**, serta aplikasi untuk secara efektif menutupi aktivitas Anda dari pengamat jaringan, termasuk ISP Anda. Lebih dari sekadar sistem anonim, Whonix adalah lingkungan pengembangan yang aman dan lengkap.

## Mengapa memilih Whonix?

- **Gratis**: Seperti kebanyakan distribusi Linux, Whonix adalah sistem open source yang dilisensikan sepenuhnya gratis. Ini dikembangkan secara open source, dengan komunitas yang aktif dan transparan.
- **Privasi, Keamanan, dan Anonimitas**: Tujuan utama Whonix adalah menawarkan lingkungan yang sangat aman, di mana semua data Anda dilindungi dan komunikasi Anda dienkripsi melalui jaringan Tor.
- **Mudah Digunakan**: Whonix menawarkan Interface grafis yang intuitif dan telah dikonfigurasi sebelumnya, cocok bahkan untuk pengguna pemula. Tidak perlu menjadi ahli untuk mendapatkan manfaat dari perlindungan tingkat lanjut.
- **Lingkungan Ideal untuk Pengembangan yang Aman**: Whonix memungkinkan Anda mengembangkan, menguji, mengaudit, atau menjalankan program tanpa pernah mengungkapkan alamat IP Anda yang sebenarnya atau mengekspos kebiasaan penjelajahan atau komunikasi jaringan Anda.
- **Sesi Sekali Pakai dan Live Mode**: Whonix dapat diluncurkan dalam Live mode atau melalui komputer sekali pakai (misalnya via **Qubes OS**), memungkinkan tugas-tugas penting dilakukan tanpa meninggalkan jejak persisten setelah sesi berakhir.
- **Instalasi Relatif Sederhana**: Image yang siap pakai disediakan untuk instalasi cepat di virtual machines (VirtualBox, KVM, Qubes). Sistem ini terdokumentasi dan diperbarui secara berkala.

## Instalasi dan konfigurasi

Sebelum melanjutkan ke instalasi Whonix, penting untuk dicatat bahwa distribusi ini belum tersedia secara resmi sebagai sistem utama yang dapat dipasang langsung pada hard disk (dalam mode bare metal). Dengan kata lain, **Anda belum dapat memasang Whonix sebagai host operating system klasik**, seperti Ubuntu atau Debian standar.

Namun, beberapa edisi tersedia, memungkinkan Whonix digunakan secara **volatile** (Live mode, sesi sementara) atau **persisten** (via virtual machines atau integrasi dalam Qubes OS).

Untuk penggunaan jangka panjang yang stabil, **virtualisasi saat ini adalah satu-satunya metode yang direkomendasikan secara resmi**. Anda dapat menjalankan Whonix menggunakan **VirtualBox** (Whonix-Gateway dan Whonix-Workstation) atau mengintegrasikannya ke dalam sistem seperti **Qubes OS**. Dalam tutorial ini, kami akan berfokus pada instalasi VirtualBox.

### Prasyarat

Sebelum Anda dapat memasang Whonix dalam mode virtual, pastikan komputer Anda memenuhi persyaratan teknis minimum. Virtualisasi membutuhkan sumber daya tertentu yang tidak dapat ditawarkan oleh semua komputer. Oleh karena itu, penting bahwa prosesor Anda mendukung teknologi Virtualisasi (Intel VT-x atau AMD-V), dan opsi ini diaktifkan di BIOS/UEFI.

Berikut adalah spesifikasi yang direkomendasikan untuk pengalaman yang lancar dan stabil dengan Whonix:

- **Random Access Memory (RAM)**: minimum **8 GB** sangat direkomendasikan. Semakin banyak RAM yang Anda miliki, semakin banyak sumber daya yang dapat Anda alokasikan ke virtual machines (Gateway dan Workstation), meningkatkan kinerja.
- **Ruang Disk Tersedia**: harap sediakan **setidaknya 30 GB** ruang disk kosong. Ini termasuk ruang yang dibutuhkan untuk dua virtual machines, file sistem, dan data atau snapshot apa pun.
- **Prosesor**: prosesor dengan setidaknya **4 core fisik (8 logical threads)** direkomendasikan, terutama jika Anda ingin menjalankan layanan atau aplikasi lain secara paralel.

### Unduh Whonix

Whonix tersedia dalam beberapa edisi, tergantung pada jenis lingkungan yang ingin Anda gunakan. Untuk sebagian besar pengguna (Windows, Linux, atau MacOs), edisi VirtualBox adalah yang paling mudah diatur. Anda dapat mengunduh image langsung dari [situs web resmi](https://www.whonix.org/wiki/VirtualBox).

⚠️ Whonix **tidak kompatibel** dengan MacBook yang menggunakan prosesor Apple Silicon (arsitektur ARM).

## Menginstal VirtualBox

Untuk menjalankan Whonix, Anda memerlukan **hypervisor** seperti VirtualBox, Qubes, atau KVM.

Setelah Anda mengunduh file, instal seperti yang Anda lakukan pada perangkat lunak lainnya. Terima opsi default kecuali Anda memiliki persyaratan khusus. Apakah Anda tersesat? Lihat panduan kami untuk menggunakan VirtualBox.

https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65

### Mengimpor Whonix

Setelah VirtualBox terinstal, Anda dapat mengimpor file Whonix `.ova` yang telah Anda unduh sebelumnya (`Whonix-Gateway-Xfce.ova` dan `Whonix-Workstation-Xfce.ova`).

Buka VirtualBox, lalu klik **File → Import appliance**.

Pilih file `.ova` yang sesuai (mulai dengan Gateway).

![0_03](assets/fr/03.webp)

Pilih lokasi di mana file VM Whonix akan disimpan.

![0_04](assets/fr/04.webp)

Terima persyaratan penggunaan, lalu luncurkan impor dan tunggu hingga prosesnya selesai.

![0_05](assets/fr/05.webp)

![0_06](assets/fr/06.webp)

### Konfigurasi Whonix

Sebelum memulai Whonix, penting untuk menyesuaikan beberapa **pengaturan sistem** untuk memastikan kinerja yang lebih baik:

Pilih VM **Whonix-Workstation-Xfce**, lalu klik **Configuration**.

![0_06](assets/fr/07.webp)

Buka tab **System**, di mana alokasi RAM default adalah 2048 MB. Kami menyarankan Anda untuk meningkatkannya menjadi 4096 MB (4 GB) untuk kelancaran yang lebih baik, terutama jika Anda bermaksud membuka beberapa aplikasi atau bekerja dalam sesi yang panjang. Gateway dapat tetap menggunakan 2048 MB, kecuali jika Anda menggunakan banyak koneksi Tor secara paralel.

![0_08](assets/fr/08.webp)

### Memulai Whonix

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

**Whonix** adalah sistem yang dirancang untuk menyediakan lingkungan komputasi yang **aman**, **anonim**, dan **rahasia**, ideal untuk menjelajah Internet tanpa mengorbankan identitas atau data Anda. Untuk mencapai hal ini, Whonix dilengkapi dengan sejumlah aplikasi harian berguna yang dirancang untuk memperkuat keamanan digital Anda sejak awal.

### KeepassXC

**KeePassXC** adalah password manager terintegrasi Whonix. Aplikasi ini memungkinkan Anda **membuat, menyimpan, dan mengelola** kata sandi Anda dengan aman, tanpa harus mengingat semuanya secara manual. Kata sandi disimpan dalam database terenkripsi, yang dilindungi oleh master password.

### Browser Tor

**Tor Browser** adalah browser web default Whonix. browser ini mengandalkan jaringan **Tor**, yang mengarahkan lalu lintas Anda melalui beberapa relay di seluruh dunia, sehingga hampir tidak mungkin untuk mengidentifikasi IP Address Anda yang sebenarnya.

https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet

**Electrum** adalah wallet Bitcoin yang ringan dan cepat, telah terinstal sebelumnya di Whonix untuk memungkinkan Anda mengelola **transaksi cryptocurrency** secara anonim. Aplikasi ini tidak mengunduh seluruh Blockchain tetapi menggunakan server jarak jauh untuk mendapatkan informasi yang diperlukan, membuatnya jauh lebih ringan daripada Wallet penuh.

https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix lebih dari sekadar sistem operasi: ini adalah **lingkungan aman sejati** yang dirancang untuk melindungi anonimitas, privasi, dan aktivitas sensitif Anda. Berkat arsitektur berbasis Tor, pemartisian cerdas antara Gateway dan Workstation, serta aplikasi yang telah terpasang sebelumnya seperti Tor Browser, KeePassXC, dan Electrum, aplikasi ini menawarkan solusi siap pakai bagi siapa saja yang ingin **menjelajah secara anonim, bekerja dengan aman, atau menangani data rahasia**.

Untuk memperkuat keamanan Anda pada sistem Unix Anda, lihatlah tutorial kami tentang mengaudit komputer Anda: periksa adanya celah keamanan di sistem operasi Anda dan pastikan data Anda tidak diretas.

https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af
