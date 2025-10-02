---
name: pfSense
description: Menginstal Pfsense
---
![cover](assets/cover.webp)

___

*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan besar telah dilakukan pada teks asli penulis untuk memperbarui tutorial ini.*

___

![Image](assets/fr/027.webp)

## I. Presentasi



pfSense adalah sistem operasi open source gratis yang mengubah komputer, server khusus, atau perangkat keras apa pun menjadi router dan firewall berkinerja tinggi dan sangat mudah dikonfigurasi. Berbasis FreeBSD dan terkenal dengan arsitektur jaringannya yang stabil dan tangguh, pfSense telah menetapkan standar untuk firewall sumber terbuka untuk bisnis, otoritas lokal, dan pengguna rumahan yang menuntut lebih dari lima belas tahun.

pfSense adalah sistem operasi open source dan gratis yang mengubah komputer, dedicated server, atau perangkat keras apa pun menjadi router dan firewall yang berperforma tinggi dan sangat dapat dikonfigurasi. Berbasis FreeBSD dan terkenal karena arsitektur jaringannya yang stabil dan tangguh, pfSense telah menjadi standar untuk firewall sumber terbuka bagi bisnis, otoritas lokal, dan pengguna rumahan yang menuntut selama lebih dari lima belas tahun.

Fungsi utamanya telah berkembang pesat selama bertahun-tahun, dan telah disempurnakan dengan setiap versi baru. Hingga saat ini, pfSense menawarkan:

- Administrasi terpusat yang lengkap melalui Interface web yang modern, intuitif, dan aman.
- Firewall stateful berperforma tinggi dengan dukungan NAT tingkat lanjut (termasuk NAT-T) dan manajemen aturan yang granular.
- Dukungan multi-WAN asli, memungkinkan agregasi atau redundansi koneksi Internet.
- Server dan relay DHCP terintegrasi.
- Ketersediaan tinggi berkat protokol CARP untuk failover dan kemungkinan mengonfigurasi klaster pfSense.
- Load balancing antara beberapa koneksi atau server.
- Dukungan VPN penuh: IPsec, OpenVPN, dan WireGuard (menggantikan L2TP, yang sekarang sudah usang).
- Captive portal yang dapat dikonfigurasi untuk kontrol akses tamu, terutama di lingkungan publik atau hotel.

pfSense juga dilengkapi dengan sistem paket yang dapat diperluas yang mempermudah penambahan fitur-fitur canggih seperti proxy transparan (Squid), pemfilteran URL, atau IDS/IPS (Snort atau Suricata) langsung dari Interface web.

pfSense didistribusikan hanya untuk platform 64-bit, sejalan dengan rekomendasi FreeBSD saat ini. pfSense dapat dipasang pada perangkat keras standar (PC, rack server) atau pada platform embedded berdaya rendah seperti perangkat Netgate atau kotak x86 berprofil rendah tertentu, yang jauh lebih kuat daripada kotak Alix yang lebih lama.

Terakhir, perlu diingat bahwa pfSense memerlukan setidaknya dua interface jaringan fisik: satu didedikasikan untuk zona eksternal (WAN) dan satu didedikasikan untuk jaringan internal (LAN). Tergantung pada kompleksitas infrastruktur Anda (DMZ, VLAN, multi-WAN), beberapa interface tambahan mungkin diperlukan untuk memanfaatkan sepenuhnya kemampuannya.

## II. Unduh image file

Versi stable pfSense terbaru, saat tutorial ini ditulis, adalah 2.8 (dirilis pada Juni 2025). Anda dapat mengunduh image ISO atau file instalasi yang disesuaikan dengan lingkungan perangkat keras Anda langsung dari situs web resminya.

- [Unduh pfSense](https://www.pfsense.org/download/)

Portal unduhan memungkinkan Anda untuk memilih:

- Arsitektur (umumnya **AMD64** untuk semua perangkat keras modern).
- Tipe Image ISO (**Installer USB Memstick** untuk instalasi melalui flash drive USB, ISO Installer untuk burning or virtual editing).
- _Download mirror_ terdekat, untuk mengoptimalkan kecepatan transfer.

Bagi mereka yang ingin menggunakan pfSense di lingkungan virtual (Proxmox, VMware ESXi, VirtualBox...), image **OVA** juga tersedia. VM yang siap pakai ini sangat menyederhanakan instalasi dan konfigurasi awal. Pastikan saja Anda menyesuaikan sumber daya yang dialokasikan (CPU, RAM, interface jaringan) sesuai dengan beban yang diharapkan dan topologi jaringan Anda.

Sebelum instalasi, kami menyarankan untuk memeriksa integritas file yang diunduh dengan memverifikasi **SHA256** yang disediakan di halaman unduhan resmi. Ini untuk memastikan image ISO tersebut tidak diubah atau rusak.

## III. Instalasi

Dalam contoh ini, penginstalan dilakukan pada VM yang menjalankan VirtualBox. Prosedurnya tetap sama persis pada komputer fisik atau hypervisor lainnya, kecuali untuk manajemen perangkat virtual.

### 1. Persyaratan perangkat keras minimum

Untuk penggunaan standar, kita merekomendasikan :

- **RAM minimum 1 GB** (2 GB atau lebih disarankan untuk mengaktifkan paket tambahan atau dukungan ZFS).
- **Ruang disk 8 GB** (20 GB atau lebih disarankan untuk konfigurasi yang lebih canggih, terutama jika Anda memasang proxy cache, IDS/IPS, atau log yang terperinci).
- **Setidaknya dua virtual network interface** (satu untuk WAN, satu untuk LAN). Di VirtualBox, tambahkan di pengaturan VM sebelum startup.

### 2. Memulai Installer

Pasang image ISO yang diunduh sebagai virtual optical drive di VirtualBox, atau masukkan flash drive USB jika Anda memasang di komputer fisik. Saat startup, menu boot akan muncul.

Jika Anda tidak memilih opsi apa pun, pfSense akan secara otomatis memulai dengan opsi default setelah beberapa detik. Tekan tombol "**Enter**" untuk memulai startup normal.

![Image](assets/fr/027.webp)

Ketika menu utama muncul, tekan tombol "**I**" dengan cepat untuk memulai instalasi.

![Image](assets/fr/001.webp)

### 3. Pengaturan penginstalasi awal



Layar pertama memungkinkan Anda menetapkan beberapa parameter regional, seperti font tampilan dan pengkodean karakter. Pengaturan ini berguna dalam kasus tertentu (keyboard non-standar, layar serial, bahasa oriental). Untuk sebagian besar instalasi, pertahankan nilai default dan pilih "**Terima Pengaturan ini**".

Layar pertama memungkinkan Anda untuk mengatur beberapa parameter regional, seperti font tampilan dan pengkodean karakter. Pengaturan ini berguna dalam kasus-kasus tertentu (keyboard non-standar, layar serial, bahasa oriental). Untuk sebagian besar instalasi, pertahankan nilai default dan pilih "**Accept these Settings**".

![Image](assets/fr/002.webp)

### 4. Pilihan mode instalasi

Pilih "Quick/Easy Install" untuk menjalankan instalasi otomatis dengan opsi yang direkomendasikan. Metode ini akan menghapus disk yang dipilih dan mengonfigurasi pfSense dengan partisi default.

![Image](assets/fr/003.webp)

Sebuah peringatan akan muncul, mengindikasikan bahwa semua data pada disk akan dihapus. Konfirmasi dengan "**OK**".

Installer kemudian akan menyalin file-file yang diperlukan ke disk. Tergantung pada pada perangkat keras Anda, ini bisa memakan waktu dari beberapa detik hingga beberapa menit.

### 5. Pemilihan Kernel

Ketika installer meminta Anda untuk memilih tipe kernel, biarkan "**Standard Kernel**" tetap terpilih. Kernel generik ini sangat cocok untuk penerapan standar, baik pada PC, server, atau VM.

### 6. Akhiri penginstalan dan mulai ulang

Setelah instalasi selesai, pilih "**Reboot**" untuk me-reboot mesin Anda pada instansi pfSense baru Anda.

**Catatan penting**: keluarkan image ISO atau lepaskan flash drive USB instalasi sebelum reboot, untuk menghindari restart program instalasi saat boot berikutnya.

## IV. Memulai pfSense untuk pertama kalinya

Pada startup pertama, pfSense harus dikonfigurasi untuk mengenali dan menetapkan interface jaringannya dengan benar (WAN, LAN, DMZ, VLAN, dll.). Identifikasi kartu jaringan Anda yang cermat sangat penting untuk menghindari kesalahan konfigurasi yang dapat membuat Anda kehilangan akses ke Interface web atau membuat firewall Anda tidak beroperasi.

Saat diluncurkan, pfSense secara otomatis mendeteksi dan mendaftar semua interface jaringan yang tersedia, menunjukkan alamat MAC untuk masing-masingnya. Ini membuatnya mudah untuk membedakan di antara mereka.

### 1. VLAN

Pertanyaan pertama berkaitan dengan konfigurasi VLAN. Pada tahap ini, untuk konfigurasi dasar, kita tidak akan mengaktifkan VLAN apa pun. Jadi, tekan tombol "**N**" untuk melewati langkah ini.

![Image](assets/fr/004.webp)

### 2. WAN dan LAN Interface Assignment

pfSense kemudian meminta Anda untuk menentukan Interface mana yang akan digunakan untuk WAN (akses Internet). Anda dapat memilih antara :

- Masukkan nama Interface secara manual (disarankan untuk lingkungan virtual).
- Gunakan deteksi otomatis dengan menekan "**A**". Opsi ini berguna pada host fisik, asalkan kabel jaringan Anda tersambung dan tautannya aktif.

![Image](assets/fr/005.webp)

Dalam contoh ini, kita secara manual mengonfigurasi WAN. Masukkan nama Interface yang tepat. Untuk papan Intel, namanya akan sering menjadi "**em0**" di bawah FreeBSD, tetapi dapat bervariasi tergantung pada perangkat kerasnya. Misalnya, kartu Realtek akan sering ditampilkan sebagai "**re0**".

![Image](assets/fr/006.webp)

Ulangi operasi yang sama untuk mendefinisikan Interface LAN . Di sini, kami menggunakan "**em1**".

pfSense mengonfirmasi bahwa Interface LAN mengaktifkan baik firewall maupun NAT untuk melindungi jaringan internal Anda dan mengelola terjemahan alamat.

Jika Anda memiliki interface fisik lainnya, Anda dapat mengonfigurasi interface tambahan (DMZ, Wi-Fi, VLAN tertentu) pada tahap ini. Setiap Interface logis membutuhkan kartu jaringan atau Interface virtual yang sesuai. Untuk konfigurasi awal, kita akan membatasi diri pada WAN dan LAN.

Setelah penugasan selesai, pfSense menampilkan ringkasan yang jelas tentang korespondensi antara interface fisik dan peran yang ditugaskan. Konfirmasi dengan "**Y**".

### 3. Konsol PfSense

Ketika langkah ini selesai, menu utama konsol pfSense akan muncul. Ini menawarkan beberapa opsi yang berguna untuk administrasi langsung, seperti mengatur ulang kata sandi web, me-reboot, memuat ulang konfigurasi, atau menetapkan ulang interface.

![Image](assets/fr/007.webp)

Anda juga akan melihat ringkasan pengaturan jaringan saat ini, termasuk alamat IP default Interface LAN, biasanya **192.168.1.1**. Ini adalah alamat yang perlu Anda masukkan di browser Anda untuk mengakses Interface administrasi web.

**Catatan**: Jika jaringan internal Anda menggunakan rentang alamat yang berbeda, pilih "**2)** Set Interface(s) IP Address" di menu untuk menetapkan alamat IP yang sesuai dengan lingkungan Anda.

Secara default, jika Interface WAN Anda terhubung ke perangkat atau modem yang dikonfigurasi DHCP, pfSense akan secara otomatis mengambil alamat IP publik. Oleh karena itu, Anda harus mendapatkan akses Internet langsung dengan menghubungkan klien ke Interface LAN pfSense.

## V. Akses pertama ke web Interface

Setelah startup awal selesai dan interface jaringan dikonfigurasi, Anda dapat mengakses Interface web pfSense untuk menyelesaikan dan menyempurnakan konfigurasi Anda.



### 1. Koneksi awal

Hubungkan komputer ke port LAN (atau Interface LAN virtual di hypervisor Anda) dan tetapkan alamat IP dalam rentang yang sama jika diperlukan (secara default, pfSense secara otomatis mendistribusikan alamat melalui DHCP di LAN).

Di browser Anda, buka alamat yang ditunjukkan oleh konsol (secara default `https://192.168.1.1`). Perlu diketahui bahwa pfSense memerlukan HTTPS bahkan untuk koneksi pertama, jadi Anda akan mendapatakan peringatan sertifikat yang ditandatangani sendiri (self-signed certificate), yang dapat Anda abaikan dengan menambahkan pengecualian.

Layar login muncul. Kredensial default adalah:

- **Nama pengguna:** `admin`
- **Kata sandi:** `pfsense`

Pengidentifikasi ini akan dimodifikasi selama wizard konfigurasi awal.

## VI. Wizard Pengaturan

Pada koneksi pertama, pfSense meminta Anda untuk mengikuti **Wizard Pengaturan**. Kami sangat menyarankan agar Anda menggunakannya untuk memastikan bahwa semua parameter penting didefinisikan dengan benar.

### 1. Parameter umum

Anda bisa :

- Tentukan nama host dan domain lokal (contoh: `pfsense` dan `lan.local`).
- Tentukan server DNS dan pilih apakah pfSense akan menggunakan DNS ISP Anda atau layanan eksternal (Cloudflare, OpenDNS, Quad9...).

### 2. Zona waktu

Tentukan zona waktu situs Anda agar log dan jadwal konsisten (misalnya `Eropa/Paris`).

### 3. Konfigurasi WAN

Konfigurasikan koneksi WAN :

- Default ke **DHCP** (cukup jika Anda berada di virtualbox).
- Jika Anda memiliki IP tetap, masukkan parameter (IP statis, mask, gateway, DNS) secara manual.
- Jika perlu, tentukan autentikasi VLAN atau PPPoE (umum pada beberapa ISP).

### 4. Konfigurasi LAN

Wizard menyarankan untuk mengubah subnet LAN default. Jika Anda memiliki rencana pengalamatan tertentu, sekarang saatnya untuk menyesuaikannya.

### 5. Mengubah kata sandi administrator

Amankan pfSense Anda dengan segera menetapkan kata sandi yang kuat untuk pengguna `admin`.

## VII. Verifikasi dan pembaruan

Sebelum menerapkan firewall Anda, pastikan Anda memiliki versi terbaru :

- Buka **System > Update**.
- Pilih saluran pembaruan (biasanya **Stable**).
- Periksa pembaruan dan terapkan pembaruan tersebut.

Sebaiknya aktifkan pemberitahuan pembaruan agar Anda selalu mendapat informasi tentang patch keamanan.

## VIII. Menyimpan konfigurasi

Sebelum melakukan perubahan besar, terapkan kebijakan cadangan:

- Buka **Diagnostics > Backup & Restore**.
- Unduh salinan konfigurasi saat ini (`config.xml`).
- Simpan di tempat yang aman (media eksternal terenkripsi).

Untuk lingkungan yang sangat penting, pertimbangkan pencadangan konfigurasi otomatis pada server eksternal atau melalui skrip yang diprogram.

## IX. Pengalaman terbaik setelah pemasangan

Untuk mengakhiri konfigurasi Anda dengan benar:

- **Modifikasi aturan firewall**: Secara default, pfSense mengizinkan semua lalu lintas keluar di LAN dan memblokir lalu lintas masuk di WAN. Sesuaikan aturan ini sesuai kebutuhan.
- **Konfigurasi akses jarak jauh yang aman**: Jika diperlukan, aktifkan akses ke Interface web dari WAN hanya melalui VPN atau dengan batasan IP.
- **Aktifkan notifikasi**: Konfigurasi server SMTP untuk menerima peringatan (kegagalan, pembaruan, kesalahan).
- **Pasang ekstensi yang berguna**: Misalnya, IDS/IPS (Snort, Suricata), proxy (Squid), pemfilteran DNS (pfBlockerNG).

Firewall pfSense Anda sekarang sudah aktif dan berjalan, siap melindungi jaringan Anda. Berkat fleksibilitas dan komunitas aktifnya, Anda memiliki aplikasi yang kuat dan dapat ditingkatkan (scalable) yang dapat beradaptasi dengan kebutuhan Anda di masa mendatang (multi-WAN, VLAN, VPN site-to-site, captive portal, dll.).

Bacalah dokumentasi resmi ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) secara rutin untuk menemukan fitur-fitur baru dan memastikan konfigurasi Anda selalu up-to-date dan aman.
