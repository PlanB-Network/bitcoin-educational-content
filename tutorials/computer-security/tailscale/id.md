---
name: Tailscale
description: Tutorial Tailscale tingkat lanjut
---
![cover](assets/cover.webp)

## 1. Pendahuluan

Tailscale adalah VPN generasi terbaru yang membuat jaringan mesh terenkripsi antar perangkat Anda. Ini memungkinkan Anda menghubungkan perangkat jarak jauh seolah-olah berada di jaringan lokal yang sama, tanpa konfigurasi rumit atau pembukaan port.

Untuk self-hosting, Tailscale menetapkan setiap perangkat IP pribadi tetap dalam jaringan virtual, menawarkan akses stabil ke layanan Anda bahkan ketika IP publik Anda berubah. Ini berarti Anda dapat mengelola server Anda dari jarak jauh, tanpa mengekspos layanan Anda langsung ke internet.

**Aplikasi utama:**

- Mengelola server pribadi dari luar
- Mengelola node Umbrel/Lightning lebih cepat daripada Tor
- Akses aman ke Raspberry Pi atau NAS
- Terhubung ke layanan Anda melalui SSH atau HTTP tanpa konfigurasi jaringan yang rumit

Tailscale adalah VPN generasi berikutnya yang menciptakan jaringan mesh terenkripsi di antara perangkat-perangkat Anda. VPN ini memungkinkan Anda menyambungkan mesin-mesin jarak jauh seolah-olah mereka berada di jaringan lokal yang sama, tanpa konfigurasi yang rumit atau pembukaan port.



Untuk hosting mandiri, Tailscale memberikan setiap perangkat IP pribadi tetap dalam jaringan virtual, menawarkan akses stabil ke layanan Anda bahkan ketika IP publik Anda berubah. Ini berarti Anda bisa mengelola server Anda dari jarak jauh, tanpa mengekspos layanan Anda secara langsung ke Internet.



**Aplikasi utama:**




- Mengelola server pribadi dari luar
- Mengelola node Umbrel/Lightning lebih cepat daripada Tor
- Akses aman ke Raspberry Pi atau NAS
- Terhubung ke layanan Anda melalui SSH atau HTTP tanpa konfigurasi jaringan yang rumit



Pendekatan yang berfokus pada kesederhanaan ini memungkinkan para penyelenggara sendiri untuk mengakses layanan mereka dengan aman, menghindari jebakan-jebakan VPN tradisional.



## 2. Bagaimana Tailscale bekerja



Tidak seperti VPN tradisional, yang merutekan semua lalu lintas melalui server pusat, Tailscale menciptakan jaringan mesh di mana perangkat berkomunikasi secara langsung satu sama lain. Server pusat hanya menangani autentikasi dan distribusi kunci, tanpa melihat data pengguna.


## 2. Bagaimana Tailscale bekerja

Tidak seperti VPN tradisional yang mengarahkan semua lalu lintas melalui server pusat, Tailscale menciptakan jaringan mesh di mana perangkat berkomunikasi langsung satu sama lain. Server pusat hanya menangani autentikasi dan distribusi kunci, tanpa melihat data pengguna.
![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)

*Gambar 1: VPN tradisional dengan arsitektur hub-and-spoke di mana semua lalu lintas melewati server pusat*

*Gambar 1: VPN tradisional dengan arsitektur hub-and-spoke di mana semua lalu lintas melewati server pusat*



Berdasarkan WireGuard, setiap perangkat menghasilkan kunci kriptografinya sendiri. Server koordinasi mendistribusikan kunci publik ke node, yang kemudian membuat terowongan terenkripsi ujung ke ujung secara langsung di antara mereka sendiri. Untuk melewati firewall, Tailscale menggunakan NAT traversal dan, sebagai upaya terakhir, relay DERP yang mempertahankan enkripsi.



![VPN maillé (mesh)](assets/fr/02.webp)

*Gambar 2: Jaringan mesh Tailscale memungkinkan perangkat-perangkat berkomunikasi secara langsung satu sama lain.*

Semua komunikasi dienkripsi dengan WireGuard. Tailscale hanya melihat metadata (koneksi) tetapi tidak pernah melihat konten pertukaran. Untuk kedaulatan yang lebih besar, Headscale memungkinkan server koordinasi untuk dihosting sendiri.

**Keamanan dan kerahasiaan:** 

Berkat WireGuard, semua komunikasi di Tailscale terenkripsi secara end-to-end. Tailscale tidak dapat membaca lalu lintas data Anda—hanya perangkat Anda yang memiliki kunci pribadi yang diperlukan. Layanan ini hanya melihat metadata: alamat IP, nama perangkat, timestamp koneksi, dan log koneksi peer-to-peer (tanpa konten).

Namun, arsitektur ini bergantung pada Tailscale Inc. untuk koordinasi jaringan. Untuk menghilangkan ketergantungan ini, Headscale menawarkan alternatif open sorce yang memungkinkan Anda melakukan self-host server kontrol sambil tetap menggunakan aplikasi Tailscale resmi. Dengan begitu, Anda memiliki kedaulatan penuh atas infrastruktur jaringan Anda, meskipun dengan biaya konfigurasi yang lebih teknis.

**Untuk penjelasan lebih rinci tentang cara kerja Tailscale**, termasuk manajemen bidang kontrol, NAT traversal, dan relai DERP, kami merekomendasikan artikel luar biasa [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) di blog resmi mereka. Artikel ini menjelaskan secara mendalam konsep teknis yang menjadikan Tailscale begitu kuat.

## 3. Memasang Tailscale

Tailscale berjalan pada sistem operasi **paling umum** (Windows, macOS, Linux, iOS, Android). Pemasangannya dikatakan "cepat dan mudah" pada semua platform. Mari kita mulai dengan melihat Interface dan cara membuat akun, kemudian beralih ke prosedur instalasi untuk lingkungan yang berbeda.

### 3.1 Pembuatan akun Tailscale

Buka [https://tailscale.com/](https://tailscale.com/) dan klik tombol "Get Started / Mulai" di bagian kanan atas halaman.

![Page d'accueil Tailscale](assets/fr/03.webp)

*Halaman beranda Tailscale menjelaskan konsepnya dan menawarkan pemakaian gratis*

Untuk menggunakan Tailscale, pertama-tama Anda perlu membuat akun melalui penyedia identitas:

![Page de connexion Tailscale](assets/fr/04.webp)

*Pilihan penyedia identitas untuk terhubung ke Tailscale (Google, Microsoft, GitHub, Apple, dll.)*

Setelah masuk, Tailscale akan menanyakan beberapa informasi tentang tujuan penggunaan Anda:

![Questionnaire d'utilisation](assets/fr/05.webp)

*Formulir untuk lebih memahami tujuan penggunaan Anda (pribadi atau profesional)*

Setelah Anda membuat akun, Anda bisa memasang Tailscale pada perangkat Anda:

![Ajout du premier appareil](assets/fr/07.webp)

*Tailscale memungkinkan Anda menginstal aplikasi pada OS yang berbeda*

### 3.2 Pemasangan pada platform yang berbeda

- **Pada Windows dan macOS:** Cukup unduh aplikasi dengan tampilan grafis dari situs web resmi Tailscale dan instal (file ".msi" di Windows, file ".dmg" di Mac). Setelah terinstal, aplikasi akan meluncurkan tampilan Grafis yang memungkinkan Anda terhubung (melalui browser) ke akun Tailscale Anda untuk mengautentikasi perangkat.

![Connexion d'un appareil macOS](assets/fr/08.webp)

*Sambungkan MacBook ke tailnet*

![Connexion réussie](assets/fr/09.webp)

*Konfirmasi bahwa perangkat terhubung ke jaringan Tailscale*

- **Pada Linux (Debian, Ubuntu, dll.):** Anda memiliki beberapa opsi. Metode yang paling sederhana adalah menjalankan skrip instalasi resmi: misalnya, pada Debian/Ubuntu:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Script ini akan menambahkan repositori resmi Tailscale dan menginstal paketnya. Anda juga bisa [menambahkan repositori APT secara manual](https://pkgs.tailscale.com) atau menggunakan paket Snap atau Apt biasa. Setelah terinstal, daemon `tailscaled` akan berjalan di latar belakang. Kemudian, Anda perlu **mengautentikasi node** (lihat tampilan CLI vs web di bawah). Pada distribusi lain (Fedora, Arch, dll.), paket ini juga tersedia melalui repositori standar atau script instalasi universal. Untuk server headless, gunakan CLI: contohnya `sudo tailscale up --auth-key <key>` jika menggunakan kunci autentikasi yang sudah dibuat sebelumnya, atau cukup `tailscale up` untuk login interaktif (yang akan memberikan URL untuk dikunjungi guna mengautentikasi perangkat).

- **Pada sistem berbasis ARM (Raspberry Pi, dll.):** Kami menggunakan Linux pada umumnya, jadi pendekatannya sama seperti di atas (menggunakan script atau paket). Perlu dicatat bahwa Tailscale mendukung arsitektur ARM32/ARM64 tanpa masalah. Banyak pengguna menginstal Tailscale di Raspberry Pi OS melalui apt atau pada distribusi ringan (DietPi, dll) untuk mengakses Raspberry Pi mereka di mana saja.

- **Pada iOS dan Android:** Tailscale menyediakan aplikasi seluler **resmi**. Cukup instal *Tailscale* dari [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) atau [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).

![Installation sur iPhone](assets/fr/11.webp)

*Langkah-langkah untuk memasang Tailscale di iPhone: selamat datang, privasi, pemberitahuan, VPN*

![Connexion sur iPhone](assets/fr/12.webp)

*Sambungkan ke tailnet, pilih akun dan validasi di iPhone*

Setelah aplikasi terinstal, saat pertama kali diluncurkan, aplikasi ini akan meminta Anda untuk mengautentikasi melalui penyedia yang dipilih (Google, Apple ID, Microsoft, dll., tergantung pada apa yang Anda gunakan untuk Tailscale) - Ini adalah prosedur yang sama seperti pada platform lain, biasanya pengalihan ke halaman web OAuth. Setelah itu, aplikasi seluler akan membuat VPN (di iOS Anda perlu menerima add-on konfigurasi VPN). Aplikasi ini kemudian dapat berjalan di latar belakang, memberi Anda akses ke tailnet Anda dari mana saja.

***Harap diperhatikan:*** Pada perangkat seluler, Anda hanya dapat memiliki **satu VPN aktif dalam satu waktu** - jadi pastikan Anda tidak memiliki VPN lain yang terhubung pada saat yang sama, atau Tailscale tidak akan dapat membuat koneksinya sendiri. Di Android, Anda dapat mengatur profil kerja terpisah jika Anda ingin mengisolasi penggunaan tertentu (misalnya, profil dengan Tailscale aktif untuk aplikasi tertentu).

### 3.3 Menambahkan beberapa perangkat dan validasi

Setelah perangkat pertama Anda terhubung, Tailscale akan meminta Anda untuk menambahkan perangkat lain ke jaringan Anda:

![Ajout d'appareils supplémentaires](assets/fr/10.webp)

*Interface menunjukkan perangkat pertama yang terhubung dan menunggu perangkat lain*

Setelah Anda menambahkan beberapa perangkat, Anda dapat memeriksa apakah perangkat tersebut dapat berkomunikasi satu sama lain:

![Test de connectivité entre appareils](assets/fr/13.webp)

*Konfirmasi bahwa perangkat dapat berkomunikasi satu sama lain melalui ping*

Tailscale kemudian menyarankan konfigurasi tambahan untuk meningkatkan pengalaman Anda:

![Suggestions de configuration](assets/fr/14.webp)

*Saran untuk pengaturan DNS, berbagi perangkat, dan mengelola akses*

### 3.4 Dasbor Administrasi

Web administrasi Konsol memungkinkan Anda melihat dan mengelola semua perangkat yang terhubung:

![Tableau de bord des machines](assets/fr/15.webp)

*Daftar perangkat yang tersambung dengan karakteristik dan statusnya*

**Interface Web vs Interface CLI:** Tailscale menawarkan dua cara yang saling melengkapi untuk berinteraksi dengan jaringan: **Interface web administration** dan **command-line client (CLI)**

- **Interface Web (Konsol Admin)**: dapat diakses melalui [https://login.tailscale.com](https://login.tailscale.com), adalah dashboard utama untuk jaringan Tailscale Anda. Konsol ini menampilkan daftar semua perangkat (Mesin), status online/offline perangkat tersebut, alamat IP Tailscale-nya, dan informasi lainnya. Melalui konsol ini, Anda dapat **mengelola perangkat** (mengganti nama, membatasi masa berlaku kunci, mengotorisasi rute, menonaktifkan node), **mengelola pengguna** (dalam konteks organisasi), serta mendefinisikan aturan keamanan (ACL). Di sinilah Anda juga dapat mengonfigurasi opsi global seperti MagicDNS, tag, atau kunci autentikasi (kunci autentikasi yang dibuat sebelumnya untuk penambahan perangkat secara otomatis). Antarmuka web ini sangat berguna untuk mendapatkan gambaran umum dan menerapkan perubahan yang akan disebarkan melalui server koordinasi ke semua node. Contoh: Mengaktifkan **rute subnet** atau **exit node** dapat dilakukan dengan sekali klik di konsol, setelah node yang bersangkutan mengumumkan dirinya siap.
- **Command Line Interface (CLI):** Perintah `tailscale` tersedia pada antarmuka command line (CLI) di setiap perangkat yang telah terinstal Tailscale. CLI ini memungkinkan Anda untuk melakukan berbagai tindakan secara lokal: menghubungkan (`tailscale up`), memeriksa status (`tailscale status` untuk melihat peer yang terhubung), melakukan debug (`tailscale ping <ip>`), dan sebagainya. Beberapa fitur bahkan **eksklusif untuk CLI** atau lebih canggih, misalnya:
  - `tailscale up --advertise-routes = 192.168.0.0/24` untuk menyiarkan rute subnet,
  - `tailscale up --advertise-exit-node` untuk mengusulkan perangkat Anda sebagai exit node,
  - `tailscale set --accept-routes=true` (atau `--exit-node=<IP>`) untuk menggunakan rute atau exit node.
  - `tailscale ip -4` untuk menampilkan IP Tailscale perangkat,
  - `tailscale lock/unlock` (jika menggunakan *tailnet-lock*, fitur keamanan tingkat lanjut),
  - atau `tailscale file send <node>` untuk menggunakan **Taildrop** (transfer file antar perangkat).

CLI sangat bermanfaat pada server tanpa tampilan grafis dan untuk penulisan script tindakan tertentu.

**Perbedaan Penggunaan:** Sebagian besar konfigurasi dasar dapat dilakukan baik melalui tampilan web maupun CLI. Contohnya, penambahan perangkat dapat dilakukan dengan prompt melalui konsol, atau dengan menjalankan `tailscale up` pada perangkat dan memvalidasinya melalui web. Demikian pula, penggantian nama perangkat dapat dilakukan melalui konsol atau dengan perintah `tailscale set --hostname`.

**Singkatnya**, konsol web ideal untuk administrasi jaringan global (terutama dengan banyak perangkat/pengguna), sedangkan CLI berguna untuk kontrol terperinci atas perangkat tertentu, script otomatisasi, atau penggunaan pada sistem tanpa GUI.


## 4. Menggunakan Tailscale pada Umbrel

Umbrel adalah platform self-hosting yang populer (terutama digunakan untuk node Bitcoin/Lightning dan layanan self-host lainnya, melalui App Store-nya). Untuk menginstal dan mengkonfigurasi Umbrel, kami merekomendasikan Anda mengikuti tutorial khusus kami:

https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Menggunakan Umbrel dan Tailscale secara bersamaan merupakan kasus penggunaan yang sangat menarik, mengingat Umbrel secara native mengintegrasikan modul Tailscale yang mudah diterapkan. Berikut adalah bagaimana Tailscale berintegrasi dengan Umbrel dan manfaat yang diberikannya:

### 4.1 Pemasangan dan konfigurasi Umbrel

- **Menginstal Tailscale di Umbrel:** Umbrel memiliki aplikasi Tailscale resmi di App Store-nya. Proses instalasinya sangatlah mudah:
  
![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)

*Halaman aplikasi Tailscale di Umbrel App Store*


Dari tampilan Web Umbrel, buka App Store, cari **Tailscale**, lalu klik *Installl*. Beberapa detik kemudian, aplikasi akan terinstal di Umbrel Anda. Saat Anda membukanya, Umbrel akan menampilkan halaman yang memungkinkan Anda menautkan node Anda ke Tailscale.

![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Layar koneksi Tailscale di Interface Umbrel*

Cukup **klik "Login / Masuk "**, yang akan mengarahkan Anda ke halaman autentikasi Tailscale:

![Page d'authentification Tailscale](assets/fr/18.webp)

*Terhubung ke Tailscale melalui penyedia identitas*

Anda dapat mengautentikasi melalui akun Tailscale Anda (Google/GitHub/dll.) atau memasukkan email Anda. Biasanya, di Umbrel, Interface akan meminta Anda untuk mengunjungi [https://login.tailscale.com](https://login.tailscale.com) — ini akan mengautentikasi aplikasi Tailscale Umbrel Anda.

![Confirmation de connexion réussie](assets/fr/19.webp)

*Konfirmasi bahwa perangkat Umbrel terhubung ke jaringan Tailscale*

Setelah selesai, Umbrel Anda kini "masuk" ke jaringan Tailscale Anda dan akan muncul di konsol Anda dengan sebuah nama (misalnya, *umbrel*). Anda kemudian bisa mengeklik alamat IP perangkat Anda untuk menyalinnya, mendapatkan alamat IPv6, atau melihat MagicDNS yang terkait dengan perangkat Anda.

![Console Tailscale avec appareils connectés](assets/fr/20.webp)

*Konsol administrasi tailscale menunjukkan beberapa perangkat yang terhubung, termasuk Umbrel*

### 4.2 Akses jarak jauh ke layanan Umbrel

Setelah Umbrel terhubung ke Tailscale, **Anda bisa mengakses Interface Umbrel dan semua aplikasi yang berjalan di atasnya, dari mana saja, seolah-olah Anda berada di jaringan lokal**. Ini adalah salah satu keunggulan utama dibandingkan Tor.

Aksesnya sangat sederhana: daripada menggunakan `umbrel.local` (yang hanya berfungsi di jaringan lokal Anda), Anda cukup menggunakan alamat IP Tailscale Umbrel Anda (`http://100.x.y.z`) langsung dari perangkat mana pun yang terhubung ke tailnet Anda. Ini berfungsi di mana pun Anda berada atau jenis koneksi internet apa pun yang Anda gunakan (4G, Wi-Fi publik, jaringan perusahaan).

**Contoh aplikasi yang dihosting Umbrel yang dapat diakses melalui Tailscale:**
- **Interface main Umbrel**: Akses dasbor Umbrel Anda cukup dengan mengetik `http://100.x.y.z` di browser Anda
- **Bitcoin node**: Kelola node Bitcoin Anda tanpa latensi, melihat sinkronisasi dan statistik
- **Lightning Node**: Gunakan ThunderHub, RTL, atau interface manajemen Lightning lainnya dengan respons yang cepat
- **Mempool**: Lihat transaksi Bitcoin dan Mempool tanpa penundaan Tor
- **noStrudel**: Akses layanan Nostr Anda yang dihosting di Umbrel

**Hubungkan dompet eksternal ke Bitcoin atau Lightning Node Anda melalui Tailscale:**

Tailscale juga memungkinkan dompet Bitcoin dan Lightning Anda yang terpasang di perangkat lain untuk terhubung langsung ke node Umbrel Anda:
- **Sparrow wallet (Bitcoin)**: Wallet Bitcoin eksternal ini dapat terhubung langsung ke server Electrum Umbrel Anda menggunakan Tailscale IP Address:

![Configuration Electrum dans Sparrow](assets/fr/21.webp)

*Mengkonfigurasi server Electrum pribadi di Sparrow wallet menggunakan alamat IP Tailscale Umbrel*

![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)

*Daftar alias server Electrum di Sparrow dengan alamat IP Umbrel Tailscale*

Baca panduan lengkap kami untuk mengonfigurasi Sparrow wallet dengan node Bitcoin Anda:

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

- **Zeus (Lightning)**: Dompet seluler Lightning ini dapat terhubung ke node Lightning Anda di Umbrel. Daripada mengonfigurasi endpoint sebagai `.onion', cukup atur IP Tailscale Umbrel Anda dan port API Lightning. Koneksi akan instan dibandingkan dengan Tor.

![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)

*Mengkonfigurasi Zeus untuk terhubung ke node Lightning melalui alamat ID Tailscale*

Untuk mengonfigurasi Zeus dengan node Lightning Anda, lihat tutorial terperinci kami:

https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Untuk mengetahui lebih lanjut mengenai Lightning Network dan cara kerjanya pada Umbrel, kunjungi:

https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

### 4.3 Keunggulan dibandingkan Tor

Umbrel secara native menawarkan akses jarak jauh melalui Tor (dengan menyediakan alamat `.onion` untuk layanan web-nya). Meskipun Tor memiliki keunggulan kerahasiaan (anonimitas) dan tidak memerlukan pendaftaran, banyak pengguna menganggap **Tor lambat dan tidak stabil** untuk penggunaan sehari-hari (halaman lambat diimemuat, waktu habis, dll.) — "_Umbrel via Tor sangat lambat,_" keluh sebagian orang.

Tailscale menawarkan koneksi yang l**ebih cepat dan berlatensi rendah**, karena lalu lintas data langsung (atau melalui relai cepat) daripada memantul melalui 3 node Tor. Terlebih lagi, Tailscale menyediakan pengalaman "jaringan lokal": IP pribadi digunakan, dan aplikasi dapat dipetakan secara langsung (misalnya, drive jaringan SMB di \\100.x.y.z).

Meskipun demikian, Tor memiliki keunggulan karena desentralisasi dan "berbeda" di Umbrel, sedangkan Tailscale melibatkan kepercayaan pada pihak ketiga (atau hosting Headscale). Tor juga berguna untuk akses tanpa aplikasi (dari browser Tor mana pun, Anda dapat melihat UI Umbrel, sedangkan Tailscale memerlukan aplikasi yang terinstal pada perangkat yang mengakses).

**Kesimpulannya**, untuk penggunaan interaktif (dompet Lightning, antarmuka web yang dinamis), Tailscale menawarkan kenyamanan dan kecepatan yang patut diperhitungkan dibandingkan dengan Tor, yang dibayar dengan sedikit ketergantungan eksternal. Banyak orang memilih untuk menggunakan keduanya: Tailscale untuk penggunaan sehari-hari, dan Tor sebagai cadangan atau untuk berbagi akses dengan seseorang tanpa mengundang mereka ke VPN mereka.

### 4.4 Keamanan

Dengan menggunakan Tailscale bersama Umbrel, Anda menghindari mengekspos Umbrel ke Internet. Node Umbrel hanya dapat diakses oleh perangkat terautentikasi Anda yang lain di dalam tailnet, yang secara signifikan mengurangi "*attack surface*" - serangan pada layer front end (tidak ada port yang terbuka untuk pihak asing, tidak ada risiko serangan pada layanan web melalui Internet).

Komunikasi dienkripsi (WireGuard) di samping enkripsi apa pun yang sudah dilakukan oleh layanan Anda (misalnya, bahkan HTTP internal berada di dalam sambungan). Anda tetap bisa menerapkan ACL Tailscale, contohnya, untuk mencegah perangkat tailnet tertentu mengakses Umbrel jika Anda ingin mempartisi jaringan. Umbrel sendiri tidak melihat perbedaannya — dan mengira sedang melayani secara lokal.

---

Sebagai kesimpulan dari bagian ini, integrasi Tailscale pada Umbrel hanya memerlukan beberapa klik dan **secara signifikan meningkatkan aksesibilitas** node yang Anda hosting sendiri. Anda akan dapat mengelola Umbrel beserta layanannya dari mana saja, secara aman dan efisien, seolah-olah Anda berada di jaringan lokal. Ini merupakan solusi yang sangat berguna untuk aplikasi real-time (misalnya Lightning) yang terpengaruh oleh latensi Tor, atau secara umum bagi setiap self-hoster yang mencari koneksi pribadi yang sederhana. Semuannya **tanpa mengekspos satu port pun** pada perangkat Anda, dan tanpa konfigurasi jaringan yang rumit.

## 5. Manajemen tingkat lanjut dan kasus penggunaan

### 5.1 Fitur canggih Tailscale

- **Manajemen jaringan:** Konsol administrasi (`login.tailscale.com`) memungkinkan Anda mengelola perangkat, melihat koneksi, dan mengonfigurasi aturan akses.
- **MagicDNS:** Secara otomatis memetakan nama perangkat (mis. `raspberrypi.tailnet.ts.net`) untuk menghindari mengingat alamat IP.
- **ACL dan kontrol akses:** Menentukan secara tepat siapa yang dapat mengakses sesuatu dalam jaringan Anda melalui aturan JSON, ideal untuk mengisolasi perangkat tertentu atau membatasi akses ke layanan tertentu.
- **Berbagi Perangkat:** memungkinkan Anda mengundang seseorang untuk mengakses perangkat tertentu tanpa memberi mereka akses ke seluruh jaringan Anda.
- **Router Subnet:** Perangkat Tailscale dapat bertindak sebagai pintu gerbang untuk seluruh subnet, memungkinkan akses ke perangkat non-Tailscale (IoT, printer, dll.) melalui satu perangkat yang dikonfigurasi.
- **Exit Node:** Mengggunakan perangkat sebagai gateway Internet untuk keluar dengan IP-nya. Berguna untuk Wi-Fi publik atau untuk menerobos pembatasan geografis.
- **Taildrop:** Sebuah alternatif aman untuk AirDrop, memungkinkan Anda mentransfer file antar perangkat Tailscale Anda, apa pun platform atau lokasinya. Tidak seperti AirDrop yang terbatas pada ekosistem Apple dan kedekatan fisik, Taildrop berfungsi di antara semua perangkat Anda (Windows, Mac, Linux, Android, iOS), bahkan jika mereka berada di negara yang berbeda. File ditransfer langsung antar perangkat dengan enkripsi end-to-end, tanpa melalui server pusat. Gunakan perintah `taildrop file cp` di command line atau aplikasi antarmuka grafis tergantung pada sistem Anda.

### 5.2 Perbandingan dengan solusi lain

1. **Vs. OpenVPN:** Tailscale jauh lebih sederhana untuk dikonfigurasi (tidak perlu membuka port, tidak ada manajemen sertifikat), tetapi melibatkan ketergantungan pada layanan pihak ketiga. OpenVPN sepenuhnya dapat dikontrol, namun membutuhkan lebih banyak keahlian.
2. **ZeroTier (Pesaing langsung):** beroperasi pada Layer 2 (Ethernet), memungkinkan broadcast/multicast, sementara Tailscale beroperasi pada Layer 3 (IP). ZeroTier menawarkan fleksibilitas jaringan yang lebih besar, sedangkan Tailscale mengutamakan kesederhanaan penggunaan.
3. **Vs Tor:** Tor menawarkan anonimitas yang tidak dimiliki Tailscale, namun jauh lebih lambat. Tor bersifat terdesentralisasi dan tidak memerlukan akun, sementara Tailscale lebih cepat dan menawarkan pengalaman seperti LAN.
4. **Vs WireGuard manual:** Tailscale mengotomatiskan semua manajemen kunci dan koneksi yang secara manual harus Anda tangani di WireGuard. Tailscale pada dasarnya adalah WireGuard + lapisan manajemen yang disederhanakan.

**Kesimpulannya,** Tailscale memposisikan dirinya sebagai solusi modern yang berorientasi pada kesederhanaan, ideal untuk penggunaan pribadi dan tim kecil. Bagi mereka yang mengutamakan kontrol total, Headscale menawarkan alternatif hosting mandiri (self-hosting).

## 6. Kesimpulan

**Manfaat Tailscale:** Tailscale menawarkan beberapa keuntungan untuk hosting mandiri (self-hosting):
- **Kesederhanaan dan kinerja** - Instalasi cepat di semua platform tanpa konfigurasi jaringan yang rumit. Lalu lintas mengikuti jalur paling efisien antar perangkat Anda (P2P mesh), dengan performa protokol WireGuard dan tanpa server pusat yang membatasi _throughput_(banyak data yang berhasil di transfer).
- **Keamanan dan fleksibilitas** - Enkripsi end-to-end, _attack surface_ yang berkurang, dan fitur-fitur canggih (ACL, autentikasi SSO/MFA). Berfungsi bahkan di balik NAT atau saat beroperasi, dengan subnet router dan exit node untuk menyesuaikan jaringan dengan kebutuhan Anda.

**Batasan:** perlu juga diingat:
- **Ketergantungan Eksternal:** Dalam versi standarnya, layanan ini bergantung pada infrastruktur Tailscale Inc. Ketergantungan ini bisa dihindari melalui Headscale (alternatif self-hosting).
- **Kendala lainnya** - Source code sebagian tertutup, ada batasan pada versi gratis untuk beberapa penggunaan lanjutan, tidak ada dukungan untuk Layer 2 (broadcast/multicast), dan membutuhkan akses internet untuk membangun koneksi.
  
**Tailscale** sangat cocok untuk individu self-host dan tim kecil, pengembang yang membutuhkan akses ke sumber daya yang tersebar, pemakai pemula VPN, dan pengguna seluler. Namun, untuk perusahaan yang memerlukan kendali penuh, solusi lain seperti Headscale atau WireGuard secara langsung mungkin lebih disukai.

**Jelajahi Headscale** untuk self-hosting lengkap, integrasi API dan DevOps (Terraform), atau alternatif seperti Innernet (mirip tetapi sepenuhnya self-hosted) dan Netmaker.

Tailscale adalah sarana penting untuk self-hosting, berkat kesederhanaan dan efisiensinya. Tailscale membuat infrastruktur pribadi Anda dapat diakses seolah-olah berada di cloud, namun tetap mempertahankan kendali di rumah Anda.

## 7. Sumber daya yang berguna

### Dokumentasi resmi

- **Pusat Dokumentasi Tailscale**: [docs.tailscale.com](https://docs.tailscale.com) - Dokumentasi lengkap dalam bahasa Inggris, panduan instalasi, tutorial, dan referensi teknis.
- **Bagaimana Tailscale bekerja**: [Bagaimana Tailscale bekerja](https://tailscale.com/blog/how-tailscale-works) - Artikel terperinci yang menjelaskan cara kerja Tailscale.
- **Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Melacak pembaruan dan fitur baru.

### Panduan praktis

- **Tutorial Homelab**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Panduan khusus untuk self-hosting.
- **Mengkonfigurasi Exit Node**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Panduan terperinci untuk mengkonfigurasi Exit Node.
- **Penggunaan Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Mentransfer file antar perangkat Tailscale.

### Perbandingan

- **Tailscale vs solusi lainnya**: [tailscale.com/compare](https://tailscale.com/compare) - Perbandingan mendetail dengan solusi VPN dan jaringan lainnya (ZeroTier, OpenVPN, dll.).

### Komunitas

- **Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Diskusi, pertanyaan, dan masukkan.
- **GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Source code pelanggan, tempat melacak pengembangan dan melaporkan masalah.
- **Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Komunitas pengguna dan pengembang.

Tailscale secara teratur menyediakan konten dan fitur baru. Kunjungi [blog resmi](https://tailscale.com/blog/) mereka untuk berita dan studi kasus terbaru.
