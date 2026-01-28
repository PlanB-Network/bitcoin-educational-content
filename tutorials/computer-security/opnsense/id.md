---
name: OPNsense
description: Bagaimana cara menginstal dan mengonfigurasi firewall OPNsense?
---
![cover](assets/cover.webp)

___

*Tutorial ini didasarkan pada konten asli oleh Florian BURNEL yang dipublikasikan di [IT-Connect](https://www.it-connect.fr/). Lisensi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Perubahan mungkin telah dilakukan pada teks asli.*

___

## I. Presentasi

Dalam tutorial ini, kita akan melihat firewall open source OPNsense. Kita akan melihat fitur-fitur utamanya, prasyarat, dan cara memasang solusi berbasis FreeBSD ini.

Sebelum memulai, Anda harus tahu bahwa **OPNsense dan pfSense merupakan firewall open source** yang berbasis pada FreeBSD. Kita dapat mengatakan bahwa pfSense adalah semacam saudara tua OPNsense, karena yang terakhir adalah sebuah Fork yang dibuat pada tahun 2015. Terakhir, penting untuk menunjukkan bahwa sejak 2017, OPNsense telah beralih ke HardenedBSD sebagai ganti FreeBSD. HardenedBSD adalah versi FreeBSD yang ditingkatkan, dengan fitur-fitur keamanan tingkat lanjut.

OPNsense menonjol berkat Interface pengguna yang lebih modern dan ritme pembaruan yang lebih sering. Faktanya, jadwal pembaruan OPNsense mencakup dua rilis utama per tahun, yang diperbarui setiap dua minggu sekali (menghasilkan rilis minor). Tindak lanjut ini sangat menarik dibandingkan dengan pfSense, jika kita melihat versi komunitas dari solusi-solusi ini.

![Image](assets/fr/050.webp)

## II. Fitur OPNsense

OPNsense adalah sistem operasi yang dirancang untuk berfungsi sebagai firewall dan router, meskipun fitur-fiturnya banyak dan dapat diperluas dengan memasang paket-paket tambahan. Cocok untuk penggunaan produksi, terutama digunakan untuk keamanan jaringan dan manajemen aliran data.

### A. Fitur utama

Berikut ini adalah beberapa fitur utama OPNsense:

- **Firewall dan NAT**: OPNsense menyediakan fungsionalitas firewall stateful tingkat lanjut dengan pemfilteran stateful, serta kemampuan NAT (_Network Address Translation_).
- **DNS/DHCP**: OPNsense dapat dikonfigurasi untuk mengelola layanan DNS dan DHCP pada jaringan. Ia dapat bertindak sebagai server DHCP, tetapi juga dapat digunakan sebagai resolver DNS untuk perangkat-perangkat di jaringan lokal. Dnsmasq juga terintegrasi secara default.
- **VPN**: OPNsense mendukung beberapa protokol VPN, termasuk IPsec, OpenVPN, dan WireGuard, yang memungkinkan koneksi yang aman untuk akses jarak jauh ke workstation seluler atau interkoneksi situs.
- **Web proxy**: OPNsense menyertakan web proxy untuk mengontrol dan memfilter akses Internet. Ia juga dapat digunakan untuk memfilter konten dan mengelola akses jaringan.
- **Manajemen Bandwidth (QoS)**: OPNsense menawarkan fitur manajemen QoS (_Quality of Service_) untuk memprioritaskan lalu lintas jaringan dan mengelola bandwidth jaringan dengan lebih baik.
- **Captive portal**: Fitur ini memungkinkan Anda mengelola akses pengguna ke jaringan melalui halaman otentikasi (basis lokal, voucher, dll.). Ini adalah fitur yang umumnya diterapkan untuk jaringan Wi-Fi publik.
- **IDS/IPS**: OPNsense mengintegrasikan Suricata untuk menawarkan fungsi IDS (_Intrusion Detection System_) dan IPS (_Intrusion Prevention System_) untuk melindungi jaringan dari serangan.
- **Ketersediaan tinggi (High availability) (CARP)**: OPNsense mendukung CARP (**Common Address Redundancy Protocol**) untuk ketersediaan tinggi antara beberapa firewall OPNsense, memastikan bahwa layanan tetap aktif bahkan jika terjadi kegagalan perangkat keras.
- **Pelaporan dan Pemantauan**: OPNsense menyediakan Aplikasi pelaporan dan pemantauan real time untuk melacak kinerja jaringan (dengan NetFlow) dan mendeteksi masalah potensial, berkat pembuatan log. Ini termasuk grafik. Aplikasi Monit terintegrasi ke dalam OPNsense dan memungkinkan pengawasan terhadap firewall itu sendiri.

### B. Paket tambahan

Ini hanyalah gambaran umum dari fitur-fitur yang ditawarkan oleh OPNsense. Selain itu, **katalog paket** yang dapat diakses dari Interface administrasi OPNsense memungkinkan Anda untuk **memperkaya firewall dengan fungsionalitas tambahan**. Ini termasuk klien ACME, agen Wazuh, layanan NTP Chrony, dan Caddy sebagai reverse proxy.

![Image](assets/fr/051.webp)

## III. Prasyarat OPNsense

Pertama-tama, Anda perlu memutuskan di mana Anda akan memasang OPNsense. Ada beberapa solusi yang memungkinkan, termasuk instalasi pada:

- Sebuah hypervisor sebagai virtual machine, baik itu Hyper-V, Proxmox, VMware ESXi, dan lain-lain.
- Sebuah mesin sebagai sistem bare-metal. Ini bisa berupa mini PC yang berfungsi sebagai firewall.

Anda juga dapat membeli **perangkat OPNsense yang bisa dipasang di rak** melalui toko online kami.

Anda perlu mempertimbangkan sumber daya perangkat keras yang dibutuhkan untuk menjalankan OPNsense. Hal ini dirinci pada [halaman dokumentasi ini](https://docs.opnsense.org/manual/hardware.html).

**Sumber daya minimum dan yang direkomendasikan untuk produksi:**


| Fitur | Minimum | Rekomendasi |
| --- | --- | --- |
| Prosesor | 1 GHz - 2 inti | 1.5 GHz - Multi-inti |
| RAM | 2 GB | 8 GB |
| Ruang penyimpanan untuk sistem | Hard drive, SSD atau kartu SD (4 GB) | 120 GB di SSD |

Terakhir, **kebutuhan sumber daya Anda bergantung di atas segalanya pada jumlah koneksi yang akan dikelola**, dan karenanya pada **kebutuhan bandwidth Anda**. Selain itu, **ingatlah layanan yang akan diaktifkan dan digunakan** (proxy, deteksi intrusi, dll.) karena dapat menguras CPU dan/atau RAM.

Anda juga akan memerlukan image ISO instalasi OPNsense, yang dapat Anda unduh dari [situs web resmi](https://opnsense.org/download/). Untuk instalasi pada VM, pilih "**dvd**" sebagai tipe image untuk mendapatkan image ISO (file) (dan lakukan apa pun yang Anda suka dengannya...). Untuk instalasi melalui flash drive USB yang dapat di-boot, pilih opsi "**vga**" untuk mendapatkan file "**.img**".

![Image](assets/fr/048.webp)

Anda juga memerlukan komputer untuk administrasi dan pengujian OPNsense.

## IV. Konfigurasi target

Tujuan kita adalah :

- **Membuat jaringan virtual internal (192.168.10.0/24 - LAN)**, yang dapat mengakses Internet melalui firewall OPNsense. Untuk penggunaan produksi, ini bisa menjadi jaringan lokal, kabel, dan/atau Wi-Fi Anda.
- **Mengaktifkan dan mengonfigurasi NAT** agar VM dalam jaringan virtual internal dapat mengakses Internet.
- **Mengaktifkan dan mengonfigurasi server DHCP pada OPNsense** untuk mendistribusikan konfigurasi IP ke perangkat-perangkat yang terhubung ke jaringan virtual internal di masa mendatang.
- **Mengonfigurasi firewall** untuk hanya mengizinkan aliran keluar dari LAN ke WAN dalam HTTP (80) dan HTTPS (443).
- **Mengonfigurasi firewall** untuk mengizinkan LAN virtual menggunakan OPNsense sebagai resolver DNS (53).

Jika Anda menggunakan platform Hyper-V, ini akan memberi Anda representasi sebagai berikut:

![Image](assets/fr/033.webp)

## V. Menginstal firewall OPNsense

### A. Mempersiapkan flash drive USB yang dapat di-booting

Langkah pertama adalah menyiapkan media instalasi: **flash drive USB yang dapat di-booting dengan OPNsense**. Ini tentu saja opsional jika Anda bekerja di lingkungan virtual, tetapi bagaimanapun juga, Anda perlu mengunduh image ISO instalasi OPNsense.

Setelah mengunduh, Anda akan mendapatkan **arsip yang berisi image dalam format ".img"**. Anda dapat **membuat flash drive USB yang dapat di-boot** dengan berbagai aplikasi, termasuk **balenaEtcher**: sangat mudah digunakan. Terlebih lagi, aplikasi ini akan mengenali file image dalam arsip, sehingga Anda tidak perlu mendekompresnya terlebih dahulu.

- [Unduh balenaEtcher](https://etcher.balena.io/)

Setelah aplikasi terinstal, pilih gambar Anda, flash drive USB Anda, lalu klik tombol "Flash!" Tunggu sebentar.

![Image](assets/fr/049.webp)

Sekarang Anda siap untuk menginstal.

### B. Menginstal Sistem OPNsense

Mulai jalankan VM yang menghosting OPNsense. Anda akan melihat halaman selamat datang yang mirip dengan yang di bawah ini. Selama beberapa detik, layar yang ditampilkan akan terlihat di window. Biarkan prosesnya berjalan dengan sendirinya...

![Image](assets/fr/019.webp)

File Image OPNsense dimuat ke dalam VM, sehingga sistem dapat diakses dalam mode "**live**", yaitu disimpan sementara dalam memori.

![Image](assets/fr/025.webp)

Kemudian Anda akan sampai pada Interface yang mirip dengan yang di bawah ini. Masuk dengan login "**installer**" dan kata sandi "**opnsense**". Harap diperhatikan bahwa keyboard yang digunakan saat ini adalah **QWERTY**. Pada titik ini, kita akan **memulai proses instalasi OPNsense**.

![Image](assets/fr/026.webp)

Wizard baru muncul di layar. Langkah pertama adalah memilih tata letak keyboard yang sesuai dengan konfigurasi Anda. Untuk keyboard AZERTY, pilih opsi "**Prancis (tombol aksen)**" dari daftar, lalu klik dua kali**.

![Image](assets/fr/027.webp)

Langkah kedua adalah memilih tugas yang akan dilakukan. Di sini, kita akan melakukan instalasi menggunakan sistem file **ZFS**. Posisikan diri Anda pada baris "**Install (ZFS)**" dan konfirmasikan dengan **Enter**.

![Image](assets/fr/028.webp)

Pada langkah ketiga, pilih "**stripe**" karena mesin kami dilengkapi dengan **hanya satu disk**: tidak ada redundansi yang memungkinkan untuk mengamankan penyimpanan firewall dan datanya. Hal ini sangat relevan ketika menginstal pada mesin fisik untuk melindungi dari kegagalan perangkat keras disk, melalui prinsip RAID.

![Image](assets/fr/029.webp)

Pada langkah keempat, cukup tekan **Enter** untuk mengonfirmasi.

![Image](assets/fr/030.webp)

Terakhir, konfirmasikan dengan memilih "**YES**" lalu tekan tombol **Enter**.

![Image](assets/fr/031.webp)

Sekarang Anda harus menunggu sementara OPNsense diinstal... Proses ini membutuhkan waktu sekitar 5 menit.

![Image](assets/fr/032.webp)

Setelah instalasi selesai, kita dapat mengubah kata sandi "**root**" sebelum melakukan boot ulang. Pilih "**Root Password**", tekan **Enter** dan masukkan kata sandi "**root**" dua kali.

![Image](assets/fr/020.webp)

Terakhir, pilih "**Complete Install**" dan tekan **Enter**. Gunakan kesempatan ini untuk **eject the disk from the VM's DVD drive**. Dalam pengaturan VM, Anda juga dapat mengatur boot pertama ke disk.

![Image](assets/fr/021.webp)

VM akan melakukan boot ulang dan memuat sistem OPNsense dari disk, karena kita baru saja menginstalnya. Masuk dengan akun "root" di konsol, dan kata sandi baru Anda (jika tidak, kata sandi default adalah "**opnsense**").

### D. Menghubungkan interface jaringan

Layar yang ditunjukkan di bawah ini akan muncul. Pilih "**1**" dan tekan **Enter** untuk mengaitkan kartu jaringan VM dengan interface OPNsense.

![Image](assets/fr/022.webp)

Pertama, wizard meminta Anda untuk mengonfigurasi link aggregation dan VLAN. Tentukan "**n**" untuk menolak, dan setiap kali, validasi jawaban Anda dengan **Enter**. Selanjutnya, Anda perlu menetapkan dua interface "**hn0**" dan "**hn1**" ke WAN dan LAN. Pada prinsipnya, "**hn0**" sesuai dengan WAN dan interface lainnya dengan LAN.

Begini cara kerjanya:

![Image](assets/fr/023.webp)

Kita sekarang memiliki :

- Interface **LAN** terkait dengan kartu jaringan "**hn1**" dan dengan alamat IP default OPNsense, yaitu **192.168.1.1/24**.
- Interface **WAN** terkait dengan kartu jaringan "**hn0**" dan dengan alamat IP yang diambil melalui **DHCP** pada jaringan lokal (berkat virtual switch eksternal kita).

Secara default, Interface administrasi OPNsense hanya dapat diakses dari LAN Interface, untuk alasan keamanan yang jelas. Oleh karena itu, Anda harus tersambung ke LAN Interface firewall untuk melakukan administrasi. Jika hal ini tidak memungkinkan, Anda dapat mengelola OPNsense untuk sementara waktu dari WAN. Hal ini melibatkan penonaktifan fungsi firewall.

Secara default, interface administrasi OPNsense hanya dapat diakses dari Interface LAN, untuk alasan keamanan yang jelas. Oleh karena itu, Anda harus terhubung ke Interface LAN firewall untuk melakukan administrasi. Jika ini tidak memungkinkan, Anda dapat sementara waktu mengelola OPNsense dari WAN. Ini melibatkan penonaktifan fungsi firewall.

Untuk melakukannya, beralihlah ke mode shell melalui opsi "**8**" dan jalankan perintah berikut:

```
pfctl -d
```

![Image](assets/fr/024.webp)

### E. Akses ke sistem manajemen OPNsense Interface

Interface Administrasi OPNsense dapat diakses melalui HTTPS, menggunakan alamat IP dari Interface LAN (atau WAN). Browser Anda akan membawa Anda ke halaman login. Masuklah dengan akun "root" dan kata sandi yang Anda pilih sebelumnya.

![Image](assets/fr/034.webp)

Tunggu beberapa detik... Anda akan diminta untuk mengikuti wizard untuk melakukan konfigurasi dasar. Klik "**Next**" untuk melanjutkan.

![Image](assets/fr/036.webp)

Langkah pertama adalah mendefinisikan hostname, nama domain, memilih bahasa, dan mendefinisikan server DNS yang akan digunakan untuk resolusi nama. Mempertahankan opsi "**Enable Resolver**" akan memungkinkan firewall digunakan sebagai resolver DNS, yang akan berguna untuk mesin-mesin di LAN virtual kita.

![Image](assets/fr/037.webp)

Lanjutkan ke langkah berikutnya. Wizard memberi Anda opsi untuk **mendefinisikan server NTP untuk sinkronisasi tanggal dan waktu**, meskipun sudah ada server yang dikonfigurasi secara default. Selain itu, penting untuk memilih zona waktu yang sesuai dengan lokasi geografis Anda (kecuali jika Anda memiliki kebutuhan khusus).

![Image](assets/fr/038.webp)

Kemudian tibalah langkah penting: **mengonfigurasi Interface WAN**. Saat ini, WAN dikonfigurasi dalam DHCP dan akan tetap dalam mode konfigurasi ini, kecuali jika Anda ingin menetapkan alamat IP statis.

![Image](assets/fr/039.webp)

Masih di halaman konfigurasi Interface WAN, Anda perlu menghapus centang pada opsi "**Block access to private networks via WAN**" jika jaringan di sisi WAN menggunakan pengalamatan privat. Ini kemungkinan akan terjadi jika Anda menjalankan Lab, dan dapat mencegah Anda mengakses Internet.

![Image](assets/fr/040.webp)

Selanjutnya, Anda dapat **menentukan kata sandi "root"**, tetapi ini opsional karena kita sudah melakukannya.

![Image](assets/fr/041.webp)

Lanjutkan sampai akhir untuk memulai reload konfigurasi. Jika Anda perlu terus mengambil kendali melalui WAN, jalankan ulang perintah di atas setelah proses ini selesai.

![Image](assets/fr/042.webp)

Hanya itu saja yang bisa dilakukan!

![Image](assets/fr/035.webp)

### E. Konfigurasi DHCP

Tujuan kita adalah menggunakan server DHCP OPNsense untuk mendistribusikan alamat IP pada LAN virtual. Untuk melakukan ini, kita perlu mengakses lokasi menu ini:

```
Services > ISC DHCPv4 > [LAN]
```

**Seperti yang Anda lihat, DHCP sudah diaktifkan secara default pada LAN**. Jika Anda tidak tertarik dengan layanan ini, Anda harus menonaktifkannya. Meskipun sudah diaktifkan dan kita ingin menggunakannya, penting untuk meninjau konfigurasinya.

Jika diperlukan, Anda dapat mengubah rentang alamat IP yang akan didistribusikan: **192.168.10.10** hingga **192.168.10.245**, tergantung pada pengaturan saat ini.

![Image](assets/fr/046.webp)

Kita juga dapat melihat bahwa kolom **"DNS servers", "Gateway", "Domain name"**, dll., kosong secara default. Faktanya, ada pewarisan otomatis dari opsi-opsi tertentu dan nilai default untuk berbagai kolom ini. Misalnya, untuk server DNS, alamat IP dari Interface LAN akan didistribusikan, memungkinkan firewall OPNsense digunakan sebagai resolver DNS.

Simpan konfigurasi setelah melakukan perubahan, jika perlu.

![Image](assets/fr/047.webp)

Untuk menguji server DHCP, Anda perlu menyambungkan VM ke jaringan LAN firewall Anda.

VM ini harus mendapatkan alamat IP dari server DHCP OPNsense, dan VM kita harus memiliki akses ke jaringan. Akses Internet harus berfungsi. Perlu diketahui bahwa jika Anda telah menonaktifkan fungsi firewall untuk mengakses OPNsense dari WAN, ini akan menonaktifkan NAT, mencegah Anda mengakses Web.

**Catatan**: lease DHCP yang saat ini dikeluarkan dapat dilihat dari Interface administrasi OPNsense. Untuk melakukannya, buka lokasi berikut: **Services > ISC DHCPv4 > Leases**.

![Image](assets/fr/045.webp)

### F. Mengkonfigurasi aturan NAT dan firewall

Kabar baiknya, sekarang kita bisa mengakses Interface administrasi OPNsense dari LAN.

```
https://192.168.1.10
```

Setelah masuk ke OPNsense, mari kita temukan konfigurasi NAT. Pergi ke lokasi ini: **Firewall > NAT > Outbound**. Di sini Anda dapat memilih antara pembuatan aturan NAT keluar secara otomatis (default) dan manual.

Pilih mode otomatis melalui opsi "**Automatic generation of outgoing NAT rules**" dan klik "**Save**" (pada prinsipnya, konfigurasi ini sudah menjadi yang aktif). Dalam mode otomatis, OPNsense itu sendiri membuat aturan NAT untuk setiap jaringan Anda.

![Image](assets/fr/043.webp)

Untuk saat ini, semua komputer yang terhubung ke LAN virtual "**192.168.10.0/24**" dapat mengakses Internet tanpa batasan. Namun, tujuan kita adalah membatasi akses ke WAN hanya pada protokol HTTP dan HTTPS, serta DNS pada Interface LAN firewall.

Jadi, kita perlu membuat aturan firewall... Jelajahi menu sebagai berikut: **Firewall > Rules > LAN**.

**Secara default, ada dua aturan untuk mengizinkan semua lalu lintas LAN keluar, dalam IPv4 dan IPv6**. Nonaktifkan kedua aturan ini dengan mengklik panah hijau di paling kiri, di awal setiap baris.

Kemudian, buat tiga aturan baru untuk mengotorisasi **jaringan LAN** (yaitu "**LAN net**") untuk:

- Mengakses semua tujuan menggunakan **HTTP**.
- Mengakses semua tujuan dengan **HTTPS**.
- Meminta **OPNsense** pada **Interface LAN-nya** (yaitu "**LAN address**"), melalui **protokol DNS** (ini berarti menggunakan firewall sebagai resolver DNS), jika tidak, otorisasi resolver DNS Anda melalui alamat IP-nya.

Ini memberikan hasil sebagai berikut:

![Image](assets/fr/044.webp)

Yang perlu dilakukan hanyalah mengklik "**Apply changes**" untuk menerapkan aturan firewall baru ke produksi. Perlu diketahui bahwa semua aliran yang tidak diizinkan secara eksplisit akan diblokir secara default.

VM LAN dapat mengakses Internet, menggunakan HTTP dan HTTPS. Semua protokol lain akan diblokir.

![Image](assets/fr/018.webp)

## IV. Kesimpulan

Dengan mengikuti panduan ini, Anda akan dapat memasang OPNsense dan segera memulainya. OPNsense menawarkan berbagai fitur untuk mengamankan dan mengelola lalu lintas jaringan Anda secara efisien, dan cocok untuk digunakan di lingkungan profesional.

Instalasi ini hanyalah permulaan: jangan ragu untuk menjelajahi menu dan mengonfigurasi fitur lain untuk menyesuaikan OPNsense dengan kebutuhan Anda.
