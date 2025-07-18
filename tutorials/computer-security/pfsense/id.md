---
name: pfSense
description: Menginstal Pfsense
---
![cover](assets/cover.webp)



___



*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0] (https://creativecommons.org/licenses/by-nc/4.0/). Perubahan besar telah dilakukan pada teks asli penulis untuk memperbarui tutorial ini.*



___



![Image](assets/fr/027.webp)



## I. Presentasi



pfSense adalah sistem operasi open source gratis yang mengubah komputer, server khusus, atau perangkat keras apa pun menjadi router dan firewall berkinerja tinggi dan sangat mudah dikonfigurasi. Berbasis FreeBSD dan terkenal dengan arsitektur jaringannya yang stabil dan tangguh, pfSense telah menetapkan standar untuk firewall sumber terbuka untuk bisnis, otoritas lokal, dan pengguna rumahan yang menuntut lebih dari lima belas tahun.



Fungsi utamanya telah berkembang pesat selama bertahun-tahun, dan telah disempurnakan dengan setiap versi baru. Hingga saat ini, pfSense menawarkan :





- Administrasi yang lengkap dan terpusat melalui web Interface yang modern, intuitif, dan aman.
- Firewall stateful berkinerja tinggi dengan dukungan NAT tingkat lanjut (termasuk NAT-T) dan manajemen aturan granular.
- Dukungan multi-WAN asli, memungkinkan agregasi atau redundansi koneksi Internet.
- Server dan relai DHCP terintegrasi.
- Ketersediaan tinggi berkat protokol CARP untuk failover dan kemungkinan mengkonfigurasi cluster pfSense.
- Penyeimbangan beban di antara beberapa koneksi atau server.
- Dukungan VPN penuh: IPsec, OpenVPN dan WireGuard (menggantikan L2TP, yang sekarang sudah usang).
- Portal captive yang dapat dikonfigurasi untuk kontrol akses tamu, terutama di lingkungan publik atau hotel.



pfSense juga dilengkapi dengan sistem paket yang dapat diperluas yang memudahkan untuk menambahkan fitur-fitur canggih seperti proxy transparan (Squid), pemfilteran URL atau IDS/IPS (Snort atau Suricata) secara langsung dari web Interface.



pfSense didistribusikan hanya untuk platform 64-bit, sesuai dengan rekomendasi FreeBSD saat ini. Dapat diinstal pada perangkat keras standar (PC, server rak) atau pada platform tertanam berdaya rendah seperti peralatan Netgate atau kotak x86 profil rendah tertentu, yang jauh lebih bertenaga daripada kotak Alix yang lebih tua.



Terakhir, perlu diingat bahwa pfSense membutuhkan setidaknya dua antarmuka jaringan fisik: satu didedikasikan untuk zona eksternal (WAN) dan satu lagi didedikasikan untuk jaringan internal (LAN). Tergantung pada kompleksitas infrastruktur Anda (DMZ, VLAN, beberapa WAN), beberapa antarmuka tambahan mungkin diperlukan untuk memanfaatkan kemampuannya sepenuhnya.



## II. Unduh gambar



Versi stabil terbaru dari pfSense, pada saat tutorial ini ditulis, adalah 2.8 (dirilis pada bulan Juni 2025). Anda bisa mengunduh citra ISO atau berkas instalasi yang disesuaikan dengan lingkungan perangkat keras Anda langsung dari situs web resminya:





- [Unduh pfSense](https://www.pfsense.org/download/)



Portal pengunduhan memungkinkan Anda untuk memilih :





- Arsitektur (umumnya **AMD64** untuk semua perangkat keras modern).
- Jenis gambar (**Installer USB Memstick** untuk pemasangan melalui stik USB, **ISO Installer** untuk pembakaran atau penyuntingan virtual).
- Cermin unduhan terdekat, untuk mengoptimalkan kecepatan transfer.



Bagi mereka yang ingin menggunakan pfSense di lingkungan tervirtualisasi (Proxmox, VMware ESXi, VirtualBox...), image **OVA** juga tersedia. Mesin virtual yang siap pakai ini sangat menyederhanakan instalasi dan konfigurasi awal. Pastikan Anda menyesuaikan sumber daya yang dialokasikan (CPU, RAM, antarmuka jaringan) sesuai dengan beban yang diharapkan dan topologi jaringan Anda.



Sebelum instalasi, kami sarankan untuk memeriksa integritas file yang diunduh dengan memverifikasi **SHA256** yang disediakan pada halaman unduhan resmi. Hal ini untuk memastikan bahwa gambar belum diubah atau rusak.



## III. Instalasi



Dalam contoh ini, penginstalan dilakukan pada mesin virtual yang menjalankan VirtualBox. Prosedurnya tetap sama persis pada mesin fisik atau hypervisor lainnya, kecuali untuk manajemen perangkat virtual.



### 1. Persyaratan perangkat keras minimum



Untuk penerapan standar, kami merekomendasikan :





- rAM minimum 1 GB** (disarankan 2 GB atau lebih untuk mengaktifkan paket tambahan atau dukungan ZFS).
- ruang disk 8 GB** (20 GB atau lebih lebih baik untuk konfigurasi yang lebih canggih, terutama jika Anda menginstal cache proxy, IDS/IPS, atau log terperinci).
- Setidaknya dua antarmuka jaringan virtual** (satu untuk WAN, satu untuk LAN). Di VirtualBox, tambahkan ke pengaturan VM sebelum memulai.



### 2. Penginstalan penginstal



Pasang image ISO yang diunduh sebagai drive optik virtual di VirtualBox, atau masukkan kunci USB jika Anda menginstal pada mesin fisik. Saat pengaktifan, menu boot akan muncul:



Jika Anda tidak memilih opsi apa pun, pfSense akan secara otomatis memulai dengan opsi default setelah beberapa detik. Tekan tombol "**Enter**" untuk memulai pengaktifan normal.



![Image](assets/fr/027.webp)



Ketika menu utama muncul, tekan tombol "**I**" dengan cepat untuk memulai instalasi.



![Image](assets/fr/001.webp)



### 3. Pengaturan penginstalasi awal



Layar pertama memungkinkan Anda menetapkan beberapa parameter regional, seperti font tampilan dan pengkodean karakter. Pengaturan ini berguna dalam kasus tertentu (keyboard non-standar, layar serial, bahasa oriental). Untuk sebagian besar instalasi, pertahankan nilai default dan pilih "**Terima Pengaturan ini**".



![Image](assets/fr/002.webp)



### 4. Pilihan mode instalasi



Pilih "**Penginstalan Cepat/Mudah**" untuk menjalankan penginstalan otomatis dengan opsi yang direkomendasikan. Metode ini akan menghapus disk yang dipilih dan mengonfigurasi pfSense dengan partisi default.



![Image](assets/fr/003.webp)



Peringatan akan muncul, mengindikasikan bahwa semua data pada disk akan dihapus. Konfirmasikan dengan "**OK**".



Penginstal kemudian menyalin file yang diperlukan ke disk. Tergantung pada perangkat keras Anda, proses ini dapat memakan waktu beberapa detik hingga beberapa menit.



### 5. Pemilihan inti



Ketika penginstal meminta Anda untuk memilih jenis kernel, biarkan "**Kernel Standar**" yang dipilih. Kernel generik ini sangat cocok untuk penerapan standar, baik pada PC, server, atau VM.



### 6. Akhiri penginstalan dan mulai ulang



Setelah instalasi selesai, pilih "**Reboot**" untuk mem-boot ulang mesin Anda pada instans pfSense yang baru.



**Catatan penting**: hapus image ISO atau lepaskan kunci USB instalasi sebelum melakukan boot ulang, untuk menghindari pengulangan program instalasi saat Anda melakukan boot.



## IV. Memulai pfSense untuk pertama kalinya



Saat pertama kali dinyalakan, pfSense harus dikonfigurasikan untuk mengenali dan menetapkan antarmuka jaringan dengan benar (WAN, LAN, DMZ, VLAN, dll.). Identifikasi kartu jaringan Anda dengan hati-hati sangat penting untuk menghindari kesalahan konfigurasi yang dapat membuat Anda tidak dapat mengakses web Interface atau membuat firewall Anda tidak berfungsi.



Pada saat peluncuran, pfSense secara otomatis mendeteksi dan membuat daftar semua antarmuka jaringan yang tersedia, yang mengindikasikan MAC Address untuk masing-masing antarmuka. Hal ini memudahkan untuk membedakannya.



### 1. VLAN



Pertanyaan pertama menyangkut konfigurasi VLAN. Pada tahap ini, untuk konfigurasi dasar, kita tidak akan mengaktifkan VLAN apa pun. Jadi, tekan tombol "**N**" untuk melewati langkah ini.



![Image](assets/fr/004.webp)



### 2. WAN dan LAN Interface Assignment



pfSense kemudian meminta Anda untuk menentukan Interface mana yang akan digunakan untuk WAN (akses Internet). Anda dapat memilih antara :





- Masukkan nama Interface secara manual (disarankan untuk lingkungan virtual).
- Gunakan deteksi otomatis dengan menekan "**A**". Opsi ini berguna pada host fisik, asalkan kabel jaringan Anda tersambung dan tautannya aktif.



![Image](assets/fr/005.webp)



Dalam contoh ini, kami mengkonfigurasi WAN secara manual. Masukkan nama yang tepat untuk Interface. Untuk board Intel, nama yang sering digunakan adalah "**em0**" pada FreeBSD, tetapi dapat bervariasi tergantung pada perangkat kerasnya. Sebagai contoh, kartu Realtek akan sering ditampilkan sebagai "**re0**".



![Image](assets/fr/006.webp)



Ulangi operasi yang sama untuk mendefinisikan LAN Interface. Di sini, kami menggunakan "**em1**".



pfSense mengonfirmasi bahwa LAN Interface mengaktifkan firewall dan NAT untuk melindungi jaringan internal Anda dan mengelola terjemahan Address.



Jika Anda memiliki antarmuka fisik lain, Anda dapat mengonfigurasi antarmuka tambahan (DMZ, Wi-Fi, VLAN tertentu) pada tahap ini. Setiap Interface logis memerlukan kartu jaringan yang sesuai atau Interface virtual. Untuk konfigurasi awal, kami akan membatasi diri pada WAN dan LAN.



Setelah penugasan selesai, pfSense menampilkan ringkasan yang jelas tentang korespondensi antara antarmuka fisik dan peran yang ditetapkan. Konfirmasikan dengan "**Y**".



### 3. Konsol PfSense



Setelah langkah ini selesai, menu utama konsol pfSense akan muncul. Menu ini menawarkan beberapa opsi yang berguna untuk administrasi langsung, seperti mengatur ulang kata sandi web, melakukan boot ulang, memuat ulang konfigurasi, atau menetapkan ulang antarmuka.



![Image](assets/fr/007.webp)



Anda juga akan melihat ringkasan pengaturan jaringan saat ini, termasuk IP default LAN Interface Address, biasanya **192.168.1.1**. Ini adalah Address yang harus Anda masukkan di browser Anda untuk mengakses web administrasi Interface.



**Catatan**: Jika jaringan internal Anda menggunakan rentang Address yang berbeda, pilih "**2)** Set Interface(s) IP Address" dalam menu untuk menetapkan IP Address yang sesuai dengan lingkungan Anda.



Secara default, jika WAN Interface Anda terhubung ke kotak atau modem yang dikonfigurasi DHCP, pfSense akan secara otomatis mengambil IP publik Address. Oleh karena itu, Anda akan mendapatkan keuntungan dari akses Internet langsung dengan menghubungkan klien ke LAN pfSense Interface.



## V. Akses pertama ke web Interface



Setelah pengaktifan awal selesai dan antarmuka jaringan dikonfigurasikan, Anda bisa mengakses web Interface pfSense untuk menyelesaikan dan menyempurnakan konfigurasi Anda.



### 1. Koneksi awal



Sambungkan komputer ke port LAN (atau LAN Interface virtual di hypervisor Anda) dan tetapkan IP Address dalam rentang yang sama jika perlu (secara default, pfSense secara otomatis mendistribusikan Address melalui DHCP di LAN).



Pada peramban Anda, buka Address yang ditunjukkan oleh konsol (secara default `https://192.168.1.1`). Perhatikan bahwa pfSense memerlukan HTTPS bahkan untuk koneksi pertama - jadi Anda akan mendapatkan peringatan sertifikat yang ditandatangani sendiri, yang dapat Anda abaikan dengan menambahkan pengecualian.



Layar login muncul. Kredensial default adalah :




- Nama pengguna:** `admin`
- Kata sandi:** `pfsense`



Pengidentifikasi ini akan dimodifikasi selama wizard konfigurasi awal.



## VI. Wizard Pengaturan



Pada koneksi pertama, pfSense meminta Anda untuk mengikuti **Wizard Pengaturan**. Kami sangat menyarankan agar Anda menggunakannya untuk memastikan bahwa semua parameter penting didefinisikan dengan benar.



### 1. Parameter umum



Anda bisa :




- Tentukan nama host dan domain lokal (contoh: `pfsense` dan `lan.local`).
- Tentukan server DNS dan pilih apakah pfSense akan menggunakan DNS ISP Anda atau layanan eksternal (Cloudflare, OpenDNS, Quad9...).



### 2. Zona waktu



Tunjukkan zona waktu situs Anda agar log dan jadwal konsisten (misalnya `Eropa/Paris`).



### 3. Konfigurasi WAN



Konfigurasikan koneksi WAN :




- Default ke **DHCP** (cukup jika Anda berada di belakang kotak).
- Jika Anda memiliki IP tetap, masukkan parameter (IP statis, mask, gateway, DNS) secara manual.
- Jika perlu, tentukan autentikasi VLAN atau PPPoE (umum pada beberapa ISP).



### 4. Konfigurasi LAN



Wizard menyarankan untuk mengubah subnet LAN default. Jika Anda memiliki rencana pengalamatan tertentu, sekarang saatnya untuk menyesuaikannya.



### 5. Mengubah kata sandi administrator



Amankan pfSense Anda dengan segera menetapkan kata sandi yang kuat untuk pengguna `admin`.



## VII. Verifikasi dan pembaruan



Sebelum menerapkan firewall Anda, pastikan Anda memiliki versi terbaru dari :





- Buka **Sistem > Pembaruan**.
- Pilih saluran pembaruan (biasanya **Stable**).
- Periksa pembaruan dan terapkan pembaruan tersebut.



Sebaiknya aktifkan pemberitahuan pembaruan agar Anda selalu mendapat informasi tentang patch keamanan.



## VIII. Menyimpan konfigurasi



Sebelum melakukan perubahan besar, terapkan kebijakan cadangan:





- Buka **Diagnostik > Pencadangan & Pemulihan**.
- Unduh salinan konfigurasi saat ini (`config.xml`).
- Simpan di tempat yang aman (media eksternal terenkripsi).



Untuk lingkungan yang sangat penting, pertimbangkan pencadangan konfigurasi otomatis pada server eksternal atau melalui skrip yang diprogram.



## IX. Praktik terbaik setelah pemasangan



Untuk mengakhiri penyebaran Anda dengan ketenangan pikiran:





- Memodifikasi aturan firewall**: secara default, pfSense mengizinkan semua lalu lintas keluar di LAN dan memblokir lalu lintas masuk di WAN. Sesuaikan aturan ini sesuai kebutuhan.
- Konfigurasikan akses jarak jauh yang aman**: jika diperlukan, aktifkan akses ke web Interface dari WAN hanya melalui VPN atau dengan pembatasan IP.
- Aktifkan notifikasi**: konfigurasikan server SMTP untuk menerima peringatan (kegagalan, pembaruan, kesalahan).
- Instal ekstensi yang berguna**: misalnya, IDS/IPS (Snort, Suricata), proxy (Squid), penyaringan DNS (pfBlockerNG).



Firewall pfSense Anda sekarang sudah aktif dan berjalan, siap melindungi jaringan Anda. Berkat fleksibilitas dan komunitasnya yang aktif, Anda memiliki alat yang kuat dan terukur yang dapat beradaptasi dengan kebutuhan Anda di masa depan (multi-WAN, VLAN, VPN situs-ke-situs, captive portal, dll.).



Bacalah dokumentasi resmi ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) secara teratur untuk menemukan fitur-fitur baru dan memastikan konfigurasi Anda sudah mutakhir dan aman.