---
name: Skala ekor
description: Tutorial Tailscale tingkat lanjut
---
![cover](assets/cover.webp)



## 1. Pendahuluan



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



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Gambar 1: VPN tradisional dengan arsitektur hub-and-spoke di mana semua lalu lintas melewati server pusat*



Berdasarkan WireGuard, setiap perangkat menghasilkan kunci kriptografinya sendiri. Server koordinasi mendistribusikan kunci publik ke node, yang kemudian membuat terowongan terenkripsi ujung ke ujung secara langsung di antara mereka sendiri. Untuk melewati firewall, Tailscale menggunakan NAT traversal dan, sebagai upaya terakhir, relay DERP yang mempertahankan enkripsi.



![VPN maillé (mesh)](assets/fr/02.webp)


*Gambar 2: Jaringan mesh skala ekor di mana perangkat berkomunikasi secara langsung satu sama lain*



Semua komunikasi dienkripsi dengan WireGuard. Tailscale hanya melihat metadata (koneksi) tetapi tidak pernah melihat konten pertukaran. Untuk kedaulatan yang lebih besar, Headscale memungkinkan server koordinasi untuk dihosting sendiri.



**Keamanan dan kerahasiaan:** Berkat WireGuard, semua komunikasi di Tailscale dienkripsi dari ujung ke ujung. Tailscale tidak dapat membaca lalu lintas Anda - hanya perangkat Anda yang memiliki kunci pribadi yang diperlukan. Layanan ini hanya melihat metadata: Alamat IP, nama perangkat, stempel waktu koneksi, dan log koneksi peer-to-peer (tanpa konten).



Namun, arsitektur ini bergantung pada Tailscale Inc. untuk koordinasi jaringan. Untuk menghilangkan ketergantungan ini, Headscale menawarkan alternatif sumber terbuka yang memungkinkan Anda untuk menghosting sendiri server kontrol saat menggunakan klien Tailscale resmi, sehingga menjamin kedaulatan penuh atas infrastruktur jaringan Anda, dengan biaya konfigurasi yang lebih teknis.



**Untuk penjelasan rinci tentang cara kerja Tailscale, termasuk manajemen bidang kontrol, penjelajahan NAT, dan relay DERP, kami merekomendasikan artikel yang sangat bagus [How Tailscale Works] (https://tailscale.com/blog/how-tailscale-works) di blog resminya. Artikel ini menjelaskan secara mendalam konsep teknis yang membuat Tailscale begitu kuat.



## 3. Memasang Timbangan Ekor



Tailscale berjalan pada sistem operasi **paling umum** (Windows, macOS, Linux, iOS, Android). Pemasangannya dikatakan "cepat dan mudah" pada semua platform. Mari kita mulai dengan melihat Interface dan cara membuat akun, kemudian beralih ke prosedur instalasi untuk lingkungan yang berbeda.



### 3.1 Pembuatan akun skala ekor



Buka [https://tailscale.com/](https://tailscale.com/) dan klik tombol "Mulai" di bagian kanan atas halaman.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Halaman beranda Tailscale menjelaskan konsepnya dan menawarkan permulaan gratis*



Untuk menggunakan Tailscale, pertama-tama Anda perlu membuat akun melalui penyedia identitas:



![Page de connexion Tailscale](assets/fr/04.webp)


*Pilihan penyedia identitas untuk terhubung ke Tailscale (Google, Microsoft, GitHub, Apple, dll.)*



Setelah masuk, Tailscale akan menanyakan beberapa informasi tentang tujuan penggunaan Anda:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Formulir untuk lebih memahami kasus penggunaan Anda (pribadi atau profesional)*



Setelah Anda membuat akun, Anda bisa memasang Tailscale pada perangkat Anda:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale memungkinkan Anda menginstal aplikasi pada sistem yang berbeda*



### 3.2 Pemasangan pada platform yang berbeda





- Pada Windows dan macOS:** Cukup unduh aplikasi grafis dari situs web resmi Tailscale dan instal (file .msi di Windows, file .dmg di Mac). Setelah terinstal, aplikasi ini akan meluncurkan Interface grafis yang memungkinkan Anda terhubung (melalui peramban) ke akun Tailscale Anda untuk mengautentikasi mesin.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Sambungkan MacBook ke tailnet*



![Connexion réussie](assets/fr/09.webp)


*Konfirmasi bahwa perangkat terhubung ke jaringan Tailscale*





- Di Linux (Debian, Ubuntu, dll.):** Anda memiliki beberapa opsi. Metode yang paling sederhana adalah menjalankan skrip instalasi resmi: misalnya, pada Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Skrip ini akan menambahkan repositori resmi Tailscale dan menginstal paket. Anda juga dapat [secara manual menambahkan repositori APT] (https://pkgs.tailscale.com) atau menggunakan paket Snap atau apt biasa. Setelah terinstal, daemon `tailscale` akan berjalan di latar belakang. Anda kemudian perlu melakukan autentikasi simpul (lihat Interface CLI vs web di bawah ini). Pada distribusi lain (Fedora, Arch...), paket ini juga tersedia melalui repositori standar atau skrip instalasi universal. Untuk server tanpa kepala, gunakan CLI: misalnya `sudo tailscale up --auth-key <key>` jika menggunakan kunci autentikasi yang telah dibuat sebelumnya, atau cukup `tailscale up` untuk login interaktif (yang akan memberikan URL untuk dikunjungi untuk mengautentikasi perangkat).





- Pada sistem berbasis ARM (Raspberry Pi, dll.):** Kami umumnya menggunakan Linux, jadi pendekatan yang sama seperti di atas (skrip atau paket). Perhatikan bahwa Tailscale mendukung arsitektur ARM32/ARM64 tanpa masalah. Banyak pengguna menginstal Tailscale pada Raspberry Pi OS melalui apt atau pada distribusi ringan (DietPi, dll) untuk mengakses Pi mereka di mana saja.





- Di iOS dan Android:** Tailscale menyediakan aplikasi seluler **resmi**. Cukup instal *Tailscale* dari [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) atau [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Langkah-langkah untuk memasang Tailscale di iPhone: selamat datang, privasi, pemberitahuan, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Sambungkan ke tailnet, pilih akun dan validasi di iPhone*



Setelah aplikasi terinstal, saat pertama kali diluncurkan, aplikasi ini akan meminta Anda untuk mengautentikasi melalui penyedia yang dipilih (Google, Apple ID, Microsoft, dll., tergantung pada apa yang Anda gunakan untuk Tailscale) - prosedurnya sama dengan platform lain, biasanya pengalihan ke halaman web OAuth. Setelah itu, aplikasi seluler membuat VPN (pada iOS Anda harus menerima pengaya konfigurasi VPN). Aplikasi ini kemudian bisa berjalan di latar belakang, memberikan Anda akses ke tailnet Anda dari mana saja. *Harap diperhatikan:* Pada perangkat seluler, Anda hanya dapat memiliki **satu VPN aktif dalam satu waktu** - jadi pastikan Anda tidak memiliki VPN lain yang terhubung pada waktu yang sama, atau Tailscale tidak akan bisa membuat VPN-nya sendiri. Di Android, Anda bisa menyiapkan profil kerja terpisah jika Anda ingin mengisolasi penggunaan tertentu (misalnya, profil dengan Tailscale aktif untuk aplikasi tertentu).



### 3.3 Menambahkan beberapa perangkat dan validasi



Setelah perangkat pertama Anda terhubung, Tailscale akan meminta Anda untuk menambahkan perangkat lain ke jaringan Anda:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface menunjukkan perangkat pertama yang terhubung dan menunggu perangkat lain*



Setelah Anda menambahkan beberapa perangkat, Anda dapat memeriksa apakah perangkat tersebut dapat berkomunikasi satu sama lain:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Konfirmasi bahwa perangkat dapat berkomunikasi satu sama lain melalui ping*



Tailscale kemudian menyarankan konfigurasi tambahan untuk meningkatkan pengalaman Anda:



![Suggestions de configuration](assets/fr/14.webp)


*Saran untuk menyiapkan DNS, berbagi perangkat, dan mengelola akses*



### 3.4 Dasbor Administrasi



Konsol administrasi web memungkinkan Anda melihat dan mengelola semua perangkat yang terhubung:



![Tableau de bord des machines](assets/fr/15.webp)


*Daftar perangkat yang tersambung dengan karakteristik dan statusnya*



**Interface Web vs Interface CLI:** Tailscale menawarkan dua cara yang saling melengkapi untuk berinteraksi dengan jaringan: **administrasi web Interface** dan **klien baris perintah (CLI)**.





- Interface Web (Konsol Admin)**: dapat diakses di [https://login.tailscale.com](https://login.tailscale.com), konsol web ini merupakan dasbor pusat untuk jaringan Tailscale Anda. Ini mencantumkan semua perangkat (*Mesin*), status online / offline mereka, alamat IP Tailscale mereka, dan banyak lagi. Di sini Anda dapat **mengelola perangkat** (mengganti nama, kedaluwarsa kunci, mengesahkan rute, menonaktifkan simpul), **mengelola pengguna** (dalam konteks organisasi), dan mendefinisikan aturan keamanan (ACL). Di sinilah Anda mengonfigurasi opsi global seperti MagicDNS, tag, atau auth key (auth key sebelum generate untuk penambahan perangkat secara otomatis). Web Interface sangat berguna untuk mendapatkan gambaran umum dan menerapkan perubahan yang akan disebarkan melalui server koordinasi ke semua node. *Contoh:* Mengaktifkan **rute subnet** atau **node keluar** dilakukan dengan satu klik di konsol, setelah node yang bersangkutan mengumumkannya.





- Baris perintah Interface (CLI):** Perintah `tailscale` tersedia di CLI pada setiap perangkat di mana Tailscale diinstal. CLI ini memungkinkan Anda untuk melakukan segalanya secara lokal: menghubungkan (`tailscale up`), memeriksa status (`tailscale status` untuk melihat peer mana yang terhubung), debug (`tailscale ping <ip>`), dan sebagainya. Beberapa fitur bahkan **eksklusif untuk CLI** atau lebih canggih, misalnya:





  - `tailscale up --advertise-routes = 192.168.0.0/24` untuk mengiklankan rute subnet,
  - `tailscale up --advertise-exit-node` untuk mengusulkan mesin Anda sebagai simpul keluar,
  - `tailscale set --accept-routes=true` (atau `--exit-node=<IP>`) untuk mengkonsumsi rute atau menggunakan simpul keluar,
  - `tailscale ip -4` untuk menampilkan IP Tailscale perangkat,
  - `kunci/tidak terkunci` (jika menggunakan *tailnet-lock*, fitur keamanan tingkat lanjut),
  - atau `tailscale file send <node>` untuk menggunakan **Taildrop** (transfer file antar perangkat).


CLI sangat berguna pada server tanpa grafis Interface, dan untuk membuat skrip tindakan tertentu. **Perbedaan dalam penggunaan:** Sebagian besar konfigurasi dasar dapat dilakukan melalui Web atau melalui CLI. Sebagai contoh, menambahkan perangkat dilakukan dengan meminta melalui konsol, atau dengan menjalankan `tailscale up` pada perangkat dan memvalidasi melalui web. Demikian pula, mengganti nama perangkat dapat dilakukan melalui konsol atau dengan `tailscale set --hostname`. **Singkatnya, konsol web sangat ideal untuk administrasi jaringan global (terutama dengan banyak mesin/pengguna), sedangkan CLI berguna untuk kontrol halus atas mesin tertentu, skrip otomatisasi, atau penggunaan pada sistem tanpa GUI.



## 4. Menggunakan Skala Ekor pada Payung



Umbrel adalah platform hosting mandiri yang populer (terutama digunakan untuk node Bitcoin/Lightning dan layanan hosting mandiri lainnya, melalui App Store). Untuk menginstal dan mengonfigurasi Umbrel, kami sarankan Anda mengikuti tutorial khusus kami:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Menggunakan Umbrel dan Tailscale bersama-sama adalah kasus penggunaan yang sangat menarik, karena Umbrel secara native mengintegrasikan modul Tailscale yang mudah digunakan. Berikut ini adalah bagaimana Tailscale terintegrasi dengan Umbrel dan apa yang dibawanya:



### 4.1 Pemasangan dan konfigurasi payung





- Menginstal Tailscale di Umbrel:** Umbrel memiliki aplikasi Tailscale resmi di App Store. Pemasangannya tidak bisa lebih sederhana lagi:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Halaman aplikasi Tailscale di Umbrel App Store*



Dari Interface Web Umbrel, buka App Store, cari **Tailscale** dan klik *Install*. Beberapa detik kemudian, aplikasi terinstal pada Umbrel. Ketika Anda membukanya, Umbrel menampilkan halaman yang memungkinkan Anda menautkan node Anda ke Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Layar koneksi skala ekor di Interface Umbrel*



Cukup **klik "Masuk "**, yang akan mengarahkan Anda ke halaman autentikasi Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Terhubung ke Tailscale melalui penyedia identitas*



Anda dapat mengautentikasi melalui akun Tailscale Anda (Google/GitHub/dll) atau memasukkan email Anda. Biasanya, di Umbrel, Interface meminta Anda untuk mengunjungi [https://login.tailscale.com](https://login.tailscale.com) dan masuk - ini mengotentikasi aplikasi Umbrel Tailscale.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Konfirmasi bahwa perangkat Umbrel terhubung ke jaringan Tailscale*



Setelah selesai, Umbrel Anda sudah "berada di dalam" jaringan Tailscale Anda dan muncul di konsol Anda dengan sebuah nama (mis. *umbrel*). Anda kemudian dapat mengeklik IP Address perangkat Anda untuk menyalinnya, mengambil IPv6 Address atau MagicDNS yang terkait dengan perangkat Anda.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Konsol administrasi tailscale menunjukkan beberapa perangkat yang terhubung, termasuk Umbrel*




### 4.2 Akses jarak jauh ke layanan Umbrel



Setelah Umbrel terhubung ke Tailscale, **Anda dapat mengakses Interface Umbrel dan aplikasi yang berjalan di dalamnya, dari mana saja, seolah-olah Anda berada di jaringan lokal**. Ini adalah salah satu keunggulan utama dibandingkan Tor.



Aksesnya sangat sederhana: alih-alih menggunakan `umbrel.local` (yang hanya bekerja pada jaringan lokal Anda), Anda menggunakan Tailscale IP Address Umbrel (`http://100.x.y.z`) langsung dari perangkat apa pun yang tersambung ke tailnet Anda. Ini berfungsi di mana pun Anda berada atau koneksi internet apa pun yang Anda gunakan (4G, Wi-Fi publik, jaringan perusahaan).



**Contoh aplikasi yang dihosting Umbrel yang dapat diakses melalui Tailscale:**





- Payung utama Interface**: Akses dasbor Umbrel Anda cukup dengan mengetik `http://100.x.y.z` di browser Anda
- Node Bitcoin**: Kelola node Bitcoin Anda tanpa latensi, lihat sinkronisasi dan statistik
- Simpul Petir**: Gunakan ThunderHub, RTL, atau antarmuka manajemen Lightning lainnya dengan respons yang cepat
- Mempool**: Lihat transaksi Bitcoin dan Mempool tanpa penundaan Tor
- noStrudel**: Akses layanan Nostr Anda yang dihosting di Umbrel



**Hubungkan dompet eksternal ke Bitcoin atau node petir Anda melalui Tailscale :**



Tailscale juga memungkinkan dompet Bitcoin dan Lightning Anda yang terpasang di perangkat lain untuk terhubung langsung ke node Umbrel Anda:





- Sparrow wallet (Bitcoin)**: Wallet Bitcoin eksternal ini dapat terhubung langsung ke server Electrum Umbrel Anda menggunakan Tailscale IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Mengkonfigurasi server Electrum pribadi di Sparrow wallet menggunakan IP Tailscale Umbrel Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Daftar alias server Electrum di Sparrow dengan IP Umbrel Tailscale Address*



Baca panduan lengkap kami untuk mengonfigurasi Sparrow wallet dengan node Bitcoin Anda:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Petir)**: Lightning seluler Wallet ini dapat terhubung ke node Lightning Anda di Umbrel. Alih-alih mengonfigurasi titik akhir sebagai `.onion', cukup atur IP Tailscale dari Umbrel Anda dan port API Lightning. Sambungan akan instan dibandingkan dengan Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Mengkonfigurasi Zeus untuk terhubung ke node Lightning melalui Tailscale* IP Address



Untuk mengonfigurasi Zeus dengan simpul Lightning Anda, lihat tutorial terperinci kami:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Untuk mengetahui lebih lanjut mengenai Lightning Network dan cara kerjanya pada Umbrel, kunjungi :



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Keunggulan dibandingkan Tor



Umbrel secara asli menawarkan akses jarak jauh melalui Tor (dengan menyediakan alamat `.onion` untuk layanan webnya). Meskipun Tor memiliki keunggulan kerahasiaan (anonimitas) dan tidak memerlukan registrasi, banyak pengguna merasa **Tor lambat dan tidak stabil** untuk penggunaan sehari-hari (halaman dimuat dengan lambat, waktu habis, dll.) - *"Umbrel via Tor sangat lambat "* beberapa mengeluh.



Tailscale menawarkan koneksi **lebih cepat, latensi rendah**, karena lalu lintas lewat secara langsung (atau melalui relai cepat), bukannya memantul melalui 3 simpul Tor. Terlebih lagi, Tailscale menyediakan pengalaman "jaringan lokal": IP privat digunakan, dan aplikasi bisa dipetakan secara langsung (misalnya drive jaringan SMB di \100.x.y.z).



Meskipun demikian, Tor memiliki keuntungan karena terdesentralisasi dan "out of the box" pada Umbrel, sedangkan Tailscale melibatkan kepercayaan pada pihak ketiga (atau hosting headscale). Tor juga berguna untuk akses tanpa klien (dari peramban Tor mana pun, Anda bisa melihat UI Umbrel, sedangkan Tailscale membutuhkan klien yang terinstal pada perangkat pengakses).



**Kesimpulannya, untuk penggunaan interaktif (dompet Lightning, antarmuka web yang sering digunakan), Tailscale menawarkan kenyamanan dan kecepatan yang cukup baik dibandingkan dengan Tor, dengan harga sedikit ketergantungan eksternal. Banyak orang memilih untuk menggunakan *keduanya*: Tailscale sehari-hari, dan Tor sebagai cadangan atau untuk berbagi akses dengan seseorang tanpa mengundang mereka ke dalam VPN mereka.



### 4.4 Keamanan



Dengan menggunakan Tailscale dengan Umbrel, Anda menghindari mengekspos Umbrel ke Internet. Node Umbrel hanya dapat diakses oleh perangkat terotentikasi Anda yang lain di tailnet, sehingga sangat mengurangi permukaan serangan (tidak ada port yang terbuka untuk orang asing, tidak ada risiko serangan pada layanan web melalui Internet).



Komunikasi dienkripsi (WireGuard) sebagai tambahan dari enkripsi apa pun yang sudah dilakukan oleh layanan Anda (misalnya, bahkan HTTP internal di dalam terowongan). Anda masih bisa menerapkan ACL Tailscale untuk, misalnya, mencegah perangkat tailnet tertentu mengakses Umbrel jika Anda ingin mempartisi jaringan. Umbrel sendiri tidak melihat perbedaannya - dia berpikir bahwa dia melayani lokal.



---

Sebagai penutup bagian ini, mengintegrasikan Tailscale pada Umbrel hanya membutuhkan beberapa klik dan **sangat meningkatkan aksesibilitas** node yang Anda hosting sendiri. Anda akan dapat mengelola Umbrel dan layanannya dari mana saja, dengan aman dan efisien, seolah-olah Anda sedang berada di rumah. Ini adalah solusi yang sangat berguna untuk aplikasi real-time (Lightning) yang mengalami latensi Tor, atau secara lebih umum untuk self-host yang mencari koneksi privat yang sederhana. Semua tanpa membuka satu port** pada kotak Anda, dan tanpa konfigurasi jaringan yang rumit.



## 5. Manajemen tingkat lanjut dan kasus penggunaan



### 5.1 Fitur canggih skala ekor



**Manajemen jaringan:** Konsol administrasi (login.tailscale.com) memungkinkan Anda mengelola perangkat, melihat koneksi, dan mengonfigurasi aturan akses.



**MagicDNS:** Secara otomatis menyelesaikan nama perangkat (mis. `raspberrypi.tailnet.ts.net`) untuk menghindari mengingat alamat IP.



**ACL dan kontrol akses:** Tentukan dengan tepat siapa yang dapat mengakses apa di jaringan Anda melalui aturan JSON, ideal untuk mengisolasi perangkat tertentu atau membatasi akses ke layanan tertentu.



**Berbagi Perangkat memungkinkan Anda mengundang seseorang untuk mengakses mesin tertentu tanpa memberi mereka akses ke seluruh jaringan Anda.



**Router Subnet:** Mesin Tailscale dapat bertindak sebagai pintu gerbang untuk seluruh subnet, memungkinkan akses ke perangkat non-Tailscale (IoT, printer, dll.) melalui satu mesin yang dikonfigurasi.



**Node Keluar:** Gunakan mesin sebagai gateway Internet untuk keluar dengan IP-nya. Berguna untuk Wi-Fi publik atau untuk menerobos pembatasan geografis.



**Taildrop:** Alternatif yang aman untuk AirDrop, memungkinkan Anda untuk mentransfer file di antara perangkat Tailscale Anda, apa pun platform atau lokasinya. Tidak seperti AirDrop, yang terbatas pada ekosistem Apple dan kedekatan fisik, Taildrop bekerja di antara semua perangkat Anda (Windows, Mac, Linux, Android, iOS), meskipun perangkat-perangkat tersebut berada di negara yang berbeda. File ditransfer secara langsung antar perangkat dengan enkripsi ujung ke ujung, tanpa melewati server pusat. Gunakan baris perintah `taildrop file cp` atau aplikasi grafis Interface, tergantung pada sistem Anda.



### 5.2 Perbandingan dengan solusi lain



**Vs OpenVPN:** Tailscale jauh lebih sederhana untuk dikonfigurasi (tidak ada port yang harus dibuka, tidak ada manajemen sertifikat) tetapi melibatkan ketergantungan pada layanan pihak ketiga. OpenVPN sepenuhnya dapat dikontrol, tetapi membutuhkan lebih banyak keahlian.



**Sebagai pesaing langsung, ZeroTier beroperasi pada Layer 2 (Ethernet), memungkinkan siaran/multicast, sedangkan Tailscale beroperasi pada Layer 3 (IP). ZeroTier menawarkan fleksibilitas jaringan yang lebih besar, sedangkan Tailscale lebih mengutamakan kesederhanaan penggunaan.



**Vs Tor:** Tor menawarkan anonimitas yang tidak dimiliki oleh Tailscale, tetapi jauh lebih lambat. Tor terdesentralisasi dan tidak memerlukan akun, sedangkan Tailscale lebih cepat dan menawarkan pengalaman seperti LAN.



**Vs WireGuard manual:** Tailscale mengotomatiskan semua manajemen kunci dan koneksi yang harus ditangani secara manual oleh WireGuard. Pada dasarnya ini adalah WireGuard + manajemen yang disederhanakan Layer.



Kesimpulannya, Tailscale memposisikan dirinya sebagai solusi modern yang berorientasi pada kesederhanaan, ideal untuk penggunaan pribadi dan tim kecil. Bagi para pencinta kontrol penuh, Headscale menawarkan alternatif hosting mandiri.



## 6. Kesimpulan



**Manfaat Tailscale:** Tailscale menawarkan beberapa keuntungan untuk hosting mandiri:





- Kesederhanaan dan kinerja** - Instalasi cepat di semua platform tanpa konfigurasi jaringan yang rumit. Lalu lintas mengikuti jalur paling langsung di antara mesin Anda (P2P mesh), dengan kinerja protokol WireGuard dan tidak ada server pusat yang membatasi throughput.
- Keamanan dan fleksibilitas** - Enkripsi ujung ke ujung, mengurangi permukaan serangan, dan fitur-fitur canggih (ACL, otentikasi SSO/MFA). Bekerja bahkan di belakang NAT atau saat bepergian, dengan router subnet dan simpul keluar untuk menyesuaikan jaringan dengan kebutuhan Anda.



**Batasan:** Juga perlu diingat:





- Ketergantungan eksternal** - Dalam versi standarnya, layanan ini bergantung pada infrastruktur Tailscale Inc. Ketergantungan ini dapat dilewati melalui Headscale (alternatif hosting mandiri).
- Kendala lainnya** - Kode sumber yang sebagian tertutup, keterbatasan versi gratis untuk penggunaan tingkat lanjut tertentu, tidak ada dukungan untuk Layer 2 (siaran/multicast), dan kebutuhan akses Internet untuk membuat koneksi.



**Tailscale sangat ideal untuk self-host individu dan tim kecil, pengembang yang membutuhkan akses ke sumber daya yang tersebar, pemula VPN, dan pengguna seluler. Untuk perusahaan yang membutuhkan kontrol penuh, solusi lain seperti Headscale atau WireGuard secara langsung mungkin lebih baik.



**Jelajahi Headscale untuk hosting mandiri penuh, integrasi API dan DevOps (Terraform), atau alternatif seperti Innernet (serupa tetapi sepenuhnya hosting mandiri) dan Netmaker.



Tailscale adalah alat yang penting untuk hosting mandiri, berkat kesederhanaan dan efisiensinya, membuat infrastruktur pribadi Anda dapat diakses seolah-olah berada di awan, sambil tetap memegang kendali di rumah.



## 7. Sumber daya yang berguna



### Dokumentasi resmi





- Pusat Dokumentasi Tailscale**: [docs.tailscale.com](https://docs.tailscale.com) - Dokumentasi lengkap dalam bahasa Inggris, panduan instalasi, tutorial, dan referensi teknis.
- Bagaimana Tailscale bekerja**: [Cara Kerja Tailscale] (https://tailscale.com/blog/how-tailscale-works) - Artikel terperinci yang menjelaskan cara kerja Tailscale.
- Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Melacak pembaruan dan fitur baru.



### Panduan praktis





- Tutorial Homelab**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Panduan khusus untuk hosting mandiri.
- Mengkonfigurasi Simpul Keluar** : [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Panduan terperinci untuk mengkonfigurasi Exit Node.
- Gunakan Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Mentransfer file antar perangkat Tailscale.



### Perbandingan





- Tailscale vs solusi lainnya**: [tailscale.com/compare](https://tailscale.com/compare) - Perbandingan mendetail dengan solusi VPN dan jaringan lainnya (ZeroTier, OpenVPN, dll.).



### Komunitas





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Diskusi, pertanyaan, dan umpan balik.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Kode sumber pelanggan, tempat melacak pengembangan dan melaporkan masalah.
- Perselisihan**: [discord.gg/tailscale](https://discord.gg/tailscale) - Komunitas pengguna dan pengembang.



Tailscale secara teratur menyediakan konten dan fitur baru. Kunjungi [blog resmi] (https://tailscale.com/blog/) mereka untuk berita dan studi kasus terbaru.