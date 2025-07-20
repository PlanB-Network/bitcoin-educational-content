---
name: Umbrel Nostr
description: Mengonfigurasi dan menggunakan aplikasi Nostr di Umbrel
---

![cover](assets/cover.webp)



## Prasyarat: Pemasangan payung



Umbrel adalah platform sumber terbuka yang memungkinkan Anda meng-host aplikasi Bitcoin dan layanan lainnya dengan mudah di server pribadi Anda. Ini adalah solusi lengkap yang sangat menyederhanakan hosting mandiri untuk node Bitcoin dan aplikasi terdesentralisasi.



Pastikan Anda telah menginstal Umbrel dengan mengikuti panduan instalasi kami:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Pengantar ke Nostr



**Nostr** adalah protokol jaringan terbuka dan terdesentralisasi yang dirancang untuk jejaring sosial. Namanya adalah singkatan dari _"Notes and Other Stuff Transmitted by Relays"_. Ini memungkinkan siapa saja untuk mempublikasikan pesan (catatan), yang dikelola sebagai peristiwa JSON, dan menyebarkannya melalui server relay daripada platform terpusat. Setiap pengguna memiliki sepasang kunci kriptografi (privat/publik) yang berfungsi sebagai pengenal: kunci publik (npub) mengidentifikasi pengguna, dan kunci privat (nsec) memungkinkan pesan untuk ditandatangani. Berkat arsitektur terdistribusi ini, **Nostr menawarkan ketahanan terhadap sensor** dan fleksibilitas yang luar biasa: Anda dapat menggunakan beberapa klien dan terhubung ke sebanyak mungkin relai yang Anda inginkan, tanpa bergantung pada satu server.



Singkatnya, Nostr adalah protokol komunikasi terdesentralisasi di mana **klien** (aplikasi pengguna) mengirim dan menerima peristiwa melalui **relayer** (server). Protokol ini sangat populer di kalangan komunitas Bitcoin sejak tahun 2023, karena nilai-nilai desentralisasi dan kedaulatan datanya.



**Catatan:** Untuk menggunakan Nostr, Anda memerlukan kunci pribadi Anda (dibuat oleh klien Nostr atau melalui ekstensi khusus). **Jangan pernah membagikan kunci pribadi Anda**, karena akan memungkinkan siapa pun untuk menyamar sebagai Anda. Simpanlah di tempat yang aman dan gunakan alat manajemen kunci yang aman (lihat Tip di bawah).



## Aplikasi payung untuk Nostr



Umbrel menawarkan ekosistem aplikasi yang terintegrasi untuk memanfaatkan Nostr secara penuh pada node pribadi Anda. Kami akan merinci penggunaan aplikasi utama yang berhubungan dengan Nostr: **Nostr Relay**, **noStrudel**, **Snort** dan **Nostr Wallet Connect**. Masing-masing aplikasi memenuhi kebutuhan spesifik: _Nostr Relay_ adalah **server relay pribadi**, _noStrudel_ dan _Snort_ adalah **klien Nostr** (antarmuka untuk membaca/menerbitkan catatan), sedangkan _Nostr Wallet Connect_ adalah alat untuk menautkan **portofolio Lightning** ke Nostr.



### Nostr Relay - Relai pribadi Anda di Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** adalah aplikasi resmi Umbrel untuk menjalankan **Nostr relay** Anda sendiri pada node Anda. Tujuan utamanya adalah untuk memiliki *private** dan relay yang dapat diandalkan untuk *mencadangkan semua aktivitas Nostr Anda secara real time. Dengan kata lain, dengan menggunakan relai pribadi ini selain relai publik, Anda memastikan bahwa semua catatan, pesan, dan reaksi Anda disalin ke rumah, aman dari penyensoran atau kehilangan data.



**Instalasi:** Dari Umbrel App Store (kategori _Sosial_), instal _Nostr Relay_. Setelah diluncurkan, aplikasi akan berjalan di latar belakang (layanan docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Anda akan melihat web Interface melalui Umbrel: web ini menyediakan informasi dasar dan, terutama, URL relai Anda (kanan atas), yang harus Anda salin untuk penggunaan lebih lanjut. Tombol sinkronisasi (ikon bola dunia) juga tersedia.



**Untuk memanfaatkan estafet Umbrel Anda:



**Tambahkan relai ke klien Nostr Anda:** Pada aplikasi klien Anda (misalnya Damus pada iOS, Amethyst pada Android, Snort atau noStrudel pada Umbrel, dsb.), tambahkan URL relai privat Anda yang telah disalin sebelumnya. Secara default, relai Umbrel mendengarkan pada port **4848**. Jika Anda mengaksesnya di jaringan lokal, ini memberikan URL seperti: `ws://umbrel.local:4848` (atau gunakan IP lokal Umbrel).



Jika Anda menggunakan Tailscale (lihat di bawah), Anda bahkan bisa menggunakan alias DNS MagicDNS (biasanya `umbrel` atau nama yang dibuat secara otomatis) untuk mengaksesnya dari mana saja, selalu pada port 4848.



Jika Anda lebih suka Tor, dapatkan .onion Address Umbrel Anda dan gunakan dengan port 4848 melalui peramban atau klien yang kompatibel dengan Tor (lihat bagian Tor)



Setelah URL ditambahkan ke konfigurasi Relay klien Nostr Anda, sambungkan ke relay ini. Anda akan melihat pada klien Anda bahwa relai Umbrel telah tersambung (biasanya ditunjukkan dengan titik Green atau yang serupa).



**Sinkronisasi riwayat (opsional)**: Pada web Interface _Nostr Relay_ di Umbrel, klik ikon **globe** 🌐 (di bagian atas halaman). Tindakan ini akan memaksa relay Umbrel Anda untuk terhubung ke relay lainnya (yang dikonfigurasi di klien Anda) untuk **mengimpor aktivitas publik lama Anda**. Ini berarti bahwa catatan masa lalu yang telah Anda terbitkan atau baca melalui relai publik juga akan diunduh dan disimpan di relai pribadi Anda. Mohon tunggu hingga sinkronisasi berlangsung.



**Gunakan Nostr seperti biasa:** Mulai sekarang, setiap aktivitas baru (catatan yang dipublikasikan, reaksi, pesan pribadi terenkripsi, dll.) yang Anda lakukan di Nostr akan diteruskan seperti biasa ke relai publik **dan secara paralel ke relai Umbrel Anda**. Jika klien Nostr Anda dikonfigurasi dengan benar, klien akan mengirimkan setiap peristiwa ke semua relai (termasuk relai Anda). Relai pribadi Anda akan bertindak sebagai cadangan waktu nyata. Bahkan jika terjadi pemutusan sementara, pelanggan Anda akan dapat menyinkronkan ulang data yang hilang nanti berkat relai ini. ini memberi Anda kendali penuh atas data Nostr Anda



Sebagai latar belakang, _Nostr Relay_ dari Umbrel didasarkan pada proyek open-source **nostr-rs-relay** (implementasi protokol Rust). Ini mendukung seluruh protokol Nostr dan berbagai NIP standar (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, dll.), menjamin kompatibilitas maksimum dengan pelanggan.



### noStrudel - Klien Nostr untuk penjelajah



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** adalah klien web Nostr yang berorientasi pada pengguna, ideal untuk memahami dan menjelajahi jaringan Nostr secara detail. Ini adalah semacam kotak pasir untuk memeriksa peristiwa dan relay, dan untuk bereksperimen dengan fitur-fitur canggih protokol. Interface menggunakan bahasa Inggris dan relatif teknis, sehingga ideal untuk pengguna berpengalaman yang ingin tahu tentang cara kerja Nostr.



**Instalasi:** Instal _noStrudel_ dari Umbrel App Store (kategori _Social_). Setelah diluncurkan, aplikasi ini dapat diakses melalui browser Anda di Address Umbrel Anda (mis. `http://umbrel.local` atau melalui .onion/Tailscale, lihat bagian akses eksternal).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Mengkonfigurasi relai:** Ketika Anda membuka noStrudel, Anda akan melihat tombol "Setup Relai" di sudut kanan atas. Klik tombol tersebut untuk mengonfigurasi relai Anda.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Pada halaman ini, tempelkan URL relai Umbrel Anda yang telah Anda salin sebelumnya. Anda juga dapat menambahkan relay lain yang diusulkan secara default oleh aplikasi. Setelah Anda mengonfigurasi relai Anda, klik "Masuk" di kiri bawah untuk melanjutkan.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Koneksi:** noStrudel menawarkan beberapa opsi koneksi. Dalam kasus kami, kami akan memilih "Kunci Pribadi" dan menempelkan kunci pribadi Nostr yang telah dibuat sebelumnya. Jika Anda belum memiliki kunci, Anda dapat memasang ekstensi [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) untuk membuat dan/atau menyimpan kunci Nostr Anda dan dengan demikian dapat berkomunikasi dengan lebih aman dengan berbagai aplikasi Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Setelah terhubung, Anda dapat menggunakan noStrudel untuk berbagi catatan Anda melalui Nostr. Interface memberi Anda akses ke :





- Dasbor Nostr lengkap dengan garis waktu catatan, notifikasi, pesan, pencarian profil
- Manajemen relai dan status koneksi
- Alat bantu lanjutan untuk memeriksa peristiwa dan konten JSON-nya
- Opsi konfigurasi untuk filter garis waktu dan PIN



**Tip:** Pada _noStrudel_, Anda dapat mengatur _filter garis waktu_ atau menguji _NIPs (Nostr Implementation Possibilities)_ yang berbeda. Sebagai contoh, periksa dukungan untuk NIP-05 (pengidentifikasi terdesentralisasi) atau fitur yang lebih baru. Hal ini membuat _noStrudel_ menjadi alat yang sangat baik untuk bereksperimen dalam lingkungan yang terkendali.



### Snort - Pelanggan Modern Nostr di Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** adalah klien web Nostr lain yang tersedia di Umbrel, menawarkan **Interface** yang modern, cepat, dan tidak berantakan untuk berinteraksi dengan jaringan sosial yang terdesentralisasi. Tidak seperti noStrudel, yang menargetkan pengguna yang kuat, _Snort_ bertujuan untuk kesederhanaan penggunaan tanpa mengorbankan fungsionalitas. Dibangun dengan React, dan menawarkan UX yang rapi yang mengingatkan kita pada jejaring sosial klasik, sehingga cocok untuk penggunaan sehari-hari.



**Instalasi:** Instal _Snort_ dari Umbrel App Store (kategori _Sosial_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Ketika Anda membuka Snort, Anda akan melihat tombol "Daftar" di sudut kiri bawah.



![Options de connexion dans Snort](assets/fr/10.webp)



Anda bisa memilih untuk mendaftar atau terhubung ke akun yang sudah ada (yang akan kita lakukan untuk tutorial ini).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort menawarkan beberapa metode koneksi. Anda bisa menggunakan ekstensi Nostr Connect yang sudah terinstal sebelumnya atau metode lain yang tersedia. Setelah terhubung, Anda akan dapat menggunakan aplikasi ini sepenuhnya.



Interface dari _Snort_ menawarkan:





- Tampilan **Posts/Conversations/Global** untuk menavigasi di antara catatan Anda, diskusi berulir, atau umpan global
- Tab untuk **Pemberitahuan**, **Pesan** (DM), **Pencarian**, **Profil**, dll.
- Tombol **+** atau _Tulis_ untuk menerbitkan catatan baru
- Manajemen **langganan (berikut)** dan **daftar**
- Menu manajemen relai untuk menambah/menghapus relai dan melacak ketersediaannya



**Konfigurasi relai yang disarankan:** Untuk menambahkan relai Umbrel, buka Pengaturan - Relai. Masukkan URL relai anda (`ws://umbrel:4848` atau URL lain tergantung pada konfigurasi anda) pada daftar relai Snort. Dengan cara ini, Snort akan mempublikasikan catatan anda pada relai pribadi anda sebagai tambahan pada relai publik.



### Nostr Wallet Connect - Tautkan Lightning Wallet Anda ke Nostr



**Nostr Wallet Connect (NWC) adalah aplikasi yang **menghubungkan node Umbrel (Lightning) Anda ke aplikasi Nostr yang kompatibel untuk melakukan pembayaran Lightning (misalnya, mengirimkan _zaps_, pembayaran mikro untuk "menyukai" konten). Dalam tutorial ini, kita akan melihat cara menghubungkan noStrudel ke node Lightning Anda untuk melakukan pembayaran langsung dari Interface.



**Pemasangan dan konfigurasi:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Instal _Nostr Wallet Connect_ dari toko Alby di Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



Di noStrudel, klik profil Anda di sudut kanan atas, lalu pada tombol "kelola".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klik "Lightning" kemudian "hubungkan Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Di antara opsi koneksi yang tersedia, pilih "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Klik "Connect" untuk secara otomatis dialihkan ke sesi Umbrel Nostr Wallet Connect Anda.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Pada halaman Nostr Wallet Connect, Anda dapat :




   - Tentukan anggaran maksimum Anda
   - Memvalidasi otorisasi
   - Mengatur waktu kedaluwarsa untuk koneksi


Klik "hubungkan" untuk menyelesaikannya.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Anda akan diarahkan ke noStrudel dengan pesan konfirmasi: Anda sekarang bisa melakukan zap ke seluruh dunia dari node Wallet/LND Anda!



Berkat NWC, pembayaran **Lightning** Anda melalui Nostr** (zaps ke pos hadiah, pembayaran _Value for Value_, dll.) dimulai dari **node Anda sendiri**. Anda tidak perlu lagi merutekan transaksi Anda melalui layanan eksternal atau memindai QR dari ponsel Anda setiap saat. Pengalaman pengguna sangat ditingkatkan, namun tetap _non-kustodian_ dan ramah privasi.



Jika Anda ingin mengetahui cara menyiapkan node Lightning Anda sendiri di Umbrel, saya sarankan Anda melihat tutorial komprehensif lainnya ini:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Konfigurasi dan keamanan tingkat lanjut



Menggunakan Umbrel dan Nostr secara bersamaan pada tingkat lanjut membutuhkan perhatian khusus pada **keamanan** dan **konektivitas**. Berikut ini beberapa tips tentang cara melindungi konfigurasi Anda dan mengaksesnya secara optimal, di mana pun Anda berada.



### Akses eksternal yang aman: Tor dan Tailscale



Untuk alasan keamanan, Umbrel Anda hanya dapat diakses secara default di jaringan lokal Anda (dan melalui Tor). Untuk berinteraksi dengan Nostr jauh dari rumah, Anda memiliki dua solusi pilihan: **Tor** (akses anonim melalui jaringan bawang) dan **Tailscale** (jaring VPN pribadi).





- Akses melalui Tor:** Umbrel secara otomatis mengonfigurasi **layanan Tor (.onion)** untuk web dan aplikasi Interface. Ini berarti Anda dapat mengakses Interface Umbrel (termasuk _noStrudel_ atau _Snort_) dari mana saja, menggunakan peramban Tor, tanpa mengekspos IP publik Anda. tor digunakan untuk mengakses layanan Umbrel Anda dari luar jaringan lokal Anda, tanpa mengekspos perangkat Anda ke Internet ([Siapkan Tor di sistem Anda - Panduan - Komunitas Umbrel] (https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ Untuk menggunakan opsi ini, masuk ke pengaturan Umbrel dan ambil URL .onion Umbrel Anda (atau pindai kode QR yang disediakan). Pada peramban Tor, akses .onion Address ini: Anda akan mendapatkan Interface yang sama dengan Interface lokal. Anda kemudian dapat menggunakan aplikasi Nostr Anda seperti di rumah.


**Relai Nostr melalui Tor:** Jika Anda ingin relai Nostr Anda dapat dijangkau melalui Tor oleh pelanggan Anda (atau teman yang berwenang), hal ini dimungkinkan. Umbrel tidak menyediakan relai .onion Address secara langsung, tetapi karena berjalan pada port 4848, Anda dapat menggunakan .onion:





    - Gunakan UI Umbrel's .onion Address dan konfigurasikan klien Anda untuk terhubung melalui Interface ini (tidak praktis untuk WebSocket),





    - Atau ** mengekspos port 4848 sebagai layanan bawang terpisah. Ini memerlukan mengutak-atik konfigurasi Tor pada Umbrel (disediakan untuk pengguna tingkat lanjut yang sudah terbiasa dengan SSH). Sebagai alternatif, pertimbangkan sebuah terowongan Tor di server lain yang mengarahkan ke Umbrel: namun, untuk penggunaan pribadi, paling mudah menggunakan Tailscale.





- Akses melalui Tailscale:** [Tailscale](https://tailscale.com/) adalah solusi VPN mesh yang menciptakan jaringan privat virtual antara perangkat Anda dan Umbrel. Keuntungannya: bekerja seolah-olah Anda berada di LAN, tetapi melalui Internet, terenkripsi dan tanpa konfigurasi yang rumit. **Tailscale memberikan Umbrel Anda IP tetap dan nama domain pribadi, terlepas dari lokasi jaringannya ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. Dalam praktiknya, setelah Anda menginstal Tailscale di Umbrel (dari Umbrel App Store, kategori _Networking_) **dan** pada perangkat Anda (ponsel, PC...), Anda akan dapat menjangkau Umbrel melalui Address seperti `100.x.y.z` (IP Tailscale) atau nama seperti `umbrel.tailnet123.ts.net`.


untuk Nostr_, Tailscale sangat berguna: ponsel Anda, jika memiliki Tailscale aktif, akan dapat terhubung ke `ws://umbrel:4848` (terima kasih kepada MagicDNS) atau langsung ke IP Tailscale dan port 4848 untuk menggunakan relay. Klien seperti Damus atau Amethyst akan melihat Umbrel Anda seolah-olah berada di jaringan lokal yang sama. **Tips:** Aktifkan opsi **MagicDNS** di Tailscale untuk menggunakan nama host `umbrel` alih-alih mengingat IP. Hal ini memastikan koneksi yang lancar ke relay Anda bahkan ketika Anda sedang bepergian ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Terlebih lagi, Tailscale memungkinkan Anda mengakses Interface Umbrel (dan dengan demikian klien web _noStrudel/Snort_) melalui peramban yang sederhana, menggunakan IP pribadi atau nama domain yang ditetapkan. Tidak perlu Tor Browser, dan kecepatan transfer data secara umum lebih baik daripada melalui jaringan Tor.




**Catatan: Tor dan Tailscale tidak saling eksklusif. Anda bisa tetap mengaktifkan Tor untuk akses anonim atau layanan tertentu, dan menggunakan Tailscale sehari-hari untuk kemudahannya. Dalam kedua kasus tersebut, Anda tidak perlu membuka port pada router Anda, yang memperkuat keamanan.



### Mengamankan relai Nostr Anda (praktik yang disarankan)



Jika Anda menjadi tuan rumah relai Nostr di Umbrel, terutama dalam konteks tingkat lanjut, pastikan untuk menerapkan beberapa praktik yang baik:





- Relai pribadi atau terbatas:** Secara default, relai Umbrel Anda bersifat pribadi (tidak diumumkan kepada publik) dan, jika Anda hanya mengaksesnya melalui Tailscale atau LAN Anda, relai tersebut tidak akan dapat diakses oleh orang asing. **Jaga kerahasiaan tautan ** Jangan menyiarkannya di jaringan Nostr publik kecuali jika Anda ingin menjadi tuan rumah bagi pengguna lain secara sukarela, yang merupakan masalah lain (moderasi, bandwidth, dll.). Untuk penggunaan pribadi, kami sarankan untuk membatasi akses ke diri Anda sendiri dan, jika perlu, ke beberapa teman dan keluarga tepercaya.





- Daftar Putih / Auth**: Implementasi relai nostr-rs mendukung mekanisme autentikasi **NIP-42** serta _whitelist_ kunci publik. Dengan mengaktifkan opsi-opsi ini, Anda dapat membatasi relai Anda sehingga **hanya menerima peristiwa yang ditandatangani oleh kunci tertentu (milik Anda)**, atau bahwa klien harus mengautentikasi untuk mempublikasikan. pengaturan ini membutuhkan pengeditan file konfigurasi `config.toml` relai di Umbrel (melalui SSH di kontainer Docker)._ Ini merupakan manipulasi tingkat lanjut, tetapi sebagai contoh, Anda dapat membuat daftar iklan yang diizinkan (`pubkey_whitelist`). Dengan cara ini, bahkan jika seseorang menemukan relai Anda, mereka tidak akan dapat memublikasikan apa pun di sana jika tidak ada dalam daftar.





- Pembaruan dan pemeliharaan:** Selalu perbarui Umbrel dan aplikasi _Nostr Relay_ Anda. Pembaruan dapat mencakup peningkatan kinerja (misalnya penanganan spam yang lebih baik) dan perbaikan keamanan. Di Umbrel, periksa App Store secara teratur untuk mengetahui pembaruan _Nostr Relay_, dan terapkan jika diperlukan.





- Pemantauan dan batasan:** Awasi bagaimana relai Anda digunakan. Jika anda membukanya untuk orang lain, awasi beban (penyimpanan CPU/RAM) pada Umbrel anda, karena relai dapat dengan cepat menumpuk banyak data. nostr-rs-relay menawarkan **batas kecepatan dan penyimpanan yang dapat dikonfigurasi** (`batas` dalam konfigurasi, misalnya jumlah kejadian per detik, ukuran kejadian maksimum, pembersihan kejadian lama...). Untuk penggunaan pribadi, Anda mungkin tidak perlu menyentuhnya, tetapi ketahuilah bahwa parameter-parameter ini ada jika Anda membutuhkannya ([nostr-rs-relay/config.toml di master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Mengamankan kunci Nostr:** Poin ini sudah disebutkan sebelumnya, tetapi ini sangat penting: jangan pernah memasukkan kunci pribadi Nostr Anda ke dalam Interface yang tidak Anda percayai. Sebagai gantinya, gunakan ekstensi peramban atau perangkat eksternal (seperti _signer_ Nostr pada ponsel terpisah) untuk menandatangani tindakan sensitif. Pada Umbrel, klien web Anda seperti _Snort_ dan _noStrudel_ dapat bekerja tanpa mengetahui kunci rahasia Anda, melalui NIP-07. Manfaatkan kesempatan ini untuk menggabungkan kenyamanan dan keamanan.




Dengan mengikuti tips berikut ini, integrasi node Umbrel Anda dengan Nostr akan menjadi kuat **dan** aman. Anda akan memiliki lingkungan yang lengkap: node Bitcoin untuk pembayaran Lightning, relai Nostr pribadi untuk kedaulatan data, dan klien web Nostr berkinerja tinggi untuk menavigasi jaringan sosial terdesentralisasi yang baru ini. Selamat menjelajahi Nostr dengan Umbrel!