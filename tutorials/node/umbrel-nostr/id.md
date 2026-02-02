---
name: Umbrel Nostr
description: Mengonfigurasi dan menggunakan aplikasi Nostr di Umbrel
---

![cover](assets/cover.webp)



## Prasyarat: Pemasangan payung


Umbrel adalah platform sumber terbuka yang memungkinkan kamu menghosting aplikasi Bitcoin dan layanan lainnya dengan mudah di server pribadimu. Ini adalah solusi lengkap yang sangat menyederhanakan hosting mandiri untuk node Bitcoin dan aplikasi terdesentralisasi.

Pastikan kamu sudah menginstal Umbrel dengan mengikuti panduan instalasi kami:


https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Pengantar ke Nostr


**Nostr** adalah protokol jaringan terbuka dan terdesentralisasi yang dirancang untuk jejaring sosial. Namanya adalah singkatan dari _"Notes and Other Stuff Transmitted by Relays"._ Ini memungkinkan siapa saja untuk mempublikasikan pesan (catatan) yang dikelola sebagai peristiwa JSON dan menyebarkannya lewat server relay, bukan lewat platform terpusat. Setiap pengguna punya sepasang kunci kriptografi (privat atau publik) yang berfungsi sebagai pengenal. Kunci publik (npub) mengidentifikasi pengguna, dan kunci privat (nsec) memungkinkan pesan ditandatangani. Berkat arsitekturnya yang terdistribusi, **Nostr menawarkan ketahanan terhadap sensor dan fleksibilitas yang luar biasa.** Kamu bisa memakai beberapa klien dan terhubung ke sebanyak mungkin relay yang kamu mau tanpa bergantung pada satu server mana pun.



Singkatnya, Nostr adalah protokol komunikasi terdesentralisasi di mana **klien** (aplikasi pengguna) mengirim dan menerima peristiwa lewat **relay** (server). Protokol ini sangat populer di komunitas Bitcoin sejak 2023 karena nilai-nilai desentralisasi dan kedaulatan datanya.

**Catatan:** Untuk memakai Nostr, **kamu membutuhkan kunci privatmu** (dibuat oleh klien Nostr atau lewat ekstensi khusus). Jangan pernah membagikan kunci privatmu, karena itu akan memungkinkan siapa pun untuk menyamar sebagai kamu. Simpan di tempat yang aman dan gunakan alat manajemen kunci yang aman (lihat Tip di bawah).



## Aplikasi payung untuk Nostr



Umbrel menawarkan ekosistem aplikasi yang terintegrasi untuk memanfaatkan Nostr secara penuh pada node pribadimu. Kami akan merinci penggunaan aplikasi utama yang berhubungan dengan Nostr: **Nostr Relay, noStrudel,** Snort dan **Nostr Wallet Connect.** Masing-masing aplikasi memenuhi kebutuhan spesifik: _Nostr Relay_ adalah **server relay pribadi,** _noStrudel_ dan _Snort_ adalah **klien Nostr** (antarmuka untuk membaca/menerbitkan catatan), sedangkan Nostr Wallet Connect adalah alat untuk menautkan portofolio Lightning ke Nostr.



### Nostr Relay - Relai pribadi Anda di Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** adalah aplikasi resmi Umbrel untuk menjalankan Nostr relay sendiri di node pribadimu. Tujuan utamanya adalah memiliki private relay yang dapat diandalkan untuk mencadangkan semua aktivitas Nostr secara real time. Dengan kata lain, dengan menggunakan relay pribadi ini selain relay publik, kamu memastikan semua catatan, pesan, dan reaksi disalin ke rumah, aman dari penyensoran atau kehilangan data.



**Instalasi:** Dari Umbrel App Store (kategori _Sosial_), instal _Nostr Relay_. Setelah diluncurkan, aplikasi akan berjalan di latar belakang (layanan docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)


Kamu akan melihat web Interface melalui Umbrel: web ini menyediakan informasi dasar dan, terutama, URL relay-mu (kanan atas), yang harus kamu salin untuk penggunaan lebih lanjut. Tombol sinkronisasi (ikon bola dunia) juga tersedia.



**Untuk memanfaatkan estafet Umbrel Anda:**



**Tambahkan relai ke klien Nostr kamu:** Pada aplikasi klienmu (misalnya Damus di iOS, Amethyst di Android, Snort atau noStrudel di Umbrel, dan sebagainya), tambahkan URL relay privat yang sudah kamu salin sebelumnya. Secara default, relay Umbrel mendengarkan di port **4848.** Jika mengaksesnya di jaringan lokal, URL-nya akan seperti: `ws://umbrel.local:4848` (atau gunakan IP lokal Umbrel).



Jika kamu menggunakan Tailscale (lihat di bawah), kamu bahkan bisa memakai alias DNS MagicDNS (biasanya `umbrel` atau nama yang dibuat otomatis) untuk mengaksesnya dari mana saja, tetap di port 4848.

Jika lebih suka Tor, dapatkan .onion Address Umbrel-mu dan gunakan dengan port 4848 melalui browser atau klien yang kompatibel Tor (lihat bagian Tor).

Setelah URL ditambahkan ke konfigurasi Relay klien Nostr, sambungkan ke relay ini. Kamu akan melihat di klien bahwa relay Umbrel sudah tersambung (biasanya ditandai dengan titik hijau atau indikator serupa).



**Sinkronisasi riwayat (opsional)**: Pada web Interface _Nostr Relay_ di Umbrel, klik ikon **globe** 🌐 (di bagian atas halaman). Tindakan ini akan memaksa relay Umbrel kamu untuk terhubung ke relay lainnya (yang dikonfigurasi di klien kamu) untuk **mengimpor aktivitas publik lama kamu**. Ini berarti bahwa catatan masa lalu yang telah kamu terbitkan atau baca melalui relai publik juga akan diunduh dan disimpan di relai pribadi Anda. Mohon tunggu hingga sinkronisasi berlangsung.



**Gunakan Nostr seperti biasa:** Mulai sekarang, setiap aktivitas baru (catatan yang dipublikasikan, reaksi, pesan pribadi terenkripsi, dan sebagainya) yang kamu lakukan di Nostr akan diteruskan seperti biasa ke relay publik dan **secara paralel ke relay Umbrel-mu.** Jika klien Nostr dikonfigurasi dengan benar, klien akan mengirim setiap peristiwa ke semua relay (termasuk relay pribadimu). Relay pribadi ini akan berfungsi sebagai cadangan real-time. Bahkan jika terjadi pemutusan sementara, klienmu tetap bisa menyinkronkan ulang data yang hilang nanti berkat relay ini. Ini memberi kamu kendali penuh atas data Nostr-mu.


Sebagai latar belakang, _Nostr Relay_ dari Umbrel didasarkan pada proyek open-source **nostr-rs-relay** (implementasi protokol Rust). Ini mendukung seluruh protokol Nostr dan berbagai NIP standar (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, dll.), menjamin kompatibilitas maksimum dengan pelanggan.



### noStrudel - Klien Nostr untuk penjelajah



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** adalah klien web Nostr yang berorientasi pada pengguna, ideal untuk memahami dan menjelajahi jaringan Nostr secara mendalam. Ini semacam kotak pasir untuk memeriksa peristiwa dan relay, serta bereksperimen dengan fitur-fitur canggih protokol. Interface menggunakan bahasa Inggris dan relatif teknis, sehingga cocok untuk pengguna berpengalaman yang ingin tahu cara kerja Nostr.



**Instalasi:** Instal _noStrudel_ dari Umbrel App Store (kategori _Social_). Setelah diluncurkan, aplikasi ini dapat diakses melalui browser di Address Umbrel kamu (mis. `http://umbrel.local` atau melalui .onion/Tailscale, lihat bagian akses eksternal).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Mengkonfigurasi relai:** Ketika kamu membuka noStrudel, kamu akan melihat tombol "Setup Relai" di sudut kanan atas. Klik tombol tersebut untuk mengonfigurasi relai Anda.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Di halaman ini, tempelkan URL relay Umbrel yang sudah kamu salin sebelumnya. Kamu juga bisa menambahkan relay lain yang disarankan secara default oleh aplikasi. Setelah relay dikonfigurasi, klik "Masuk" di kiri bawah untuk melanjutkan.


![Options de connexion dans noStrudel](assets/fr/06.webp)



**Koneksi:** noStrudel menawarkan beberapa opsi koneksi. Dalam kasus kami, kami akan memilih "Kunci Pribadi" dan menempelkan kunci pribadi Nostr yang telah dibuat sebelumnya. Jika Anda belum memiliki kunci, Anda dapat memasang ekstensi [Nostr Connect](https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) untuk membuat dan/atau menyimpan kunci Nostr Anda dan dengan demikian dapat berkomunikasi dengan lebih aman dengan berbagai aplikasi Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Setelah terhubung, kamu dapat menggunakan noStrudel untuk berbagi catatan melalui Nostr. Interface memberimu akses ke :





- Dasbor Nostr lengkap dengan garis waktu catatan, notifikasi, pesan, pencarian profil
- Manajemen relai dan status koneksi
- Alat bantu lanjutan untuk memeriksa peristiwa dan konten JSON-nya
- Opsi konfigurasi untuk filter garis waktu dan PIN



**Tip:** Pada _noStrudel_, kamu dapat mengatur _filter garis waktu_ atau menguji _NIPs (Nostr Implementation Possibilities)_ yang berbeda. Sebagai contoh, periksa dukungan untuk NIP-05 (pengidentifikasi terdesentralisasi) atau fitur yang lebih baru. Hal ini membuat _noStrudel_ menjadi alat yang sangat baik untuk bereksperimen dalam lingkungan yang terkendali.



### Snort - Pelanggan Modern Nostr di Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** adalah klien web Nostr lain yang tersedia di Umbrel, menawarkan **Interface** yang modern, cepat, dan tidak berantakan untuk berinteraksi dengan jaringan sosial yang terdesentralisasi. Tidak seperti noStrudel, yang menargetkan pengguna yang kuat, _Snort_ bertujuan untuk kesederhanaan penggunaan tanpa mengorbankan fungsionalitas. Dibangun dengan React, dan menawarkan UX yang rapi yang mengingatkan kita pada jejaring sosial klasik, sehingga cocok untuk penggunaan sehari-hari.



**Instalasi:** Instal _Snort_ dari Umbrel App Store (kategori _Sosial_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Ketika kamu membuka Snort, Anda akan melihat tombol "Daftar" di sudut kiri bawah.



![Options de connexion dans Snort](assets/fr/10.webp)



Kamu bisa memilih untuk mendaftar atau terhubung ke akun yang sudah ada (yang akan kita lakukan untuk tutorial ini).


![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort menawarkan beberapa metode koneksi. Kamu bisa memakai ekstensi Nostr Connect yang sudah terinstal sebelumnya atau metode lain yang tersedia. Setelah terhubung, kamu bisa menggunakan aplikasi ini sepenuhnya.

Interface dari _Snort_ menawarkan:





- Tampilan **Posts/Conversations/Global** untuk menavigasi di antara catatan kamu, diskusi berulir, atau umpan global
- Tab untuk **Pemberitahuan**, **Pesan** (DM), **Pencarian**, **Profil**, dll.
- Tombol **+** atau _Tulis_ untuk menerbitkan catatan baru
- Manajemen **langganan (berikut)** dan **daftar**
- Menu manajemen relai untuk menambah/menghapus relai dan melacak ketersediaannya



**Konfigurasi relai yang disarankan:** Untuk menambahkan relai Umbrel, buka Pengaturan - Relai. Masukkan URL relay kamu (`ws://umbrel:4848` atau URL lain tergantung pada konfigurasi) pada daftar relai Snort. Dengan cara ini, Snort akan mempublikasikan catatan pada relay pribadi kamu sebagai tambahan pada relay publik.



### Nostr Wallet Connect - Tautkan Lightning Wallet Anda ke Nostr



**Nostr Wallet Connect (NWC) adalah aplikasi yang **menghubungkan node Umbrel (Lightning) kamu ke aplikasi Nostr yang kompatibel untuk melakukan pembayaran Lightning (misalnya, mengirimkan _zaps_, pembayaran mikro untuk "menyukai" konten). Dalam tutorial ini, kita akan melihat cara menghubungkan noStrudel ke node Lightning kamu untuk melakukan pembayaran langsung dari Interface.



**Pemasangan dan konfigurasi:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Instal _Nostr Wallet Connect_ dari toko Alby di Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



Di noStrudel, klik profil di sudut kanan atas, lalu pada tombol "kelola".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klik "Lightning" kemudian "hubungkan Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Di antara opsi koneksi yang tersedia, pilih "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Klik "Connect" untuk secara otomatis dialihkan ke sesi Umbrel Nostr Wallet Connect kamu.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Pada halaman Nostr Wallet Connect, kamu dapat :




   - Tentukan anggaran maksimum kamu
   - Memvalidasi otorisasi
   - Mengatur waktu kedaluwarsa untuk koneksi


Klik "hubungkan" untuk menyelesaikannya.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Anda akan diarahkan ke noStrudel dengan pesan konfirmasi: Anda sekarang bisa melakukan zap ke seluruh dunia dari node Wallet/LND Anda!



Berkat NWC, pembayaran **Lightning** Anda melalui **Nostr** (zaps ke pos hadiah, pembayaran *Value for Value*, dll.) dimulai dari **node Anda sendiri**. Kamu tidak perlu lagi merutekan transaksi melalui layanan eksternal atau memindai QR dari ponsel milikmu setiap saat. Pengalaman pengguna sangat ditingkatkan, namun tetap *non-kustodian* dan ramah privasi.


Jika kamu ingin mengetahui cara menyiapkan node Lightning sendiri di Umbrel, aku sarankan melihat tutorial komprehensif lainnya ini:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Konfigurasi dan keamanan tingkat lanjut



Menggunakan Umbrel dan Nostr secara bersamaan pada tingkat lanjut membutuhkan perhatian khusus pada **keamanan** dan **konektivitas**. Berikut ini beberapa tips tentang cara melindungi konfigurasi Anda dan mengaksesnya secara optimal, di mana pun kamu berada.



### Akses eksternal yang aman: Tor dan Tailscale



Untuk alasan keamanan, Umbrel hanya dapat diakses secara default di jaringan lokal kamu (dan melalui Tor). Untuk berinteraksi dengan Nostr jauh dari rumah, kamu memiliki dua solusi pilihan: **Tor** (akses anonim melalui jaringan bawang) dan **Tailscale** (jaring VPN pribadi).





- Akses melalui Tor: Umbrel secara otomatis mengonfigurasi **layanan Tor (.onion)** untuk web dan aplikasi Interface. Ini berarti kamu dapat mengakses Interface Umbrel (termasuk *noStrudel* atau *Snort*) dari mana saja, menggunakan peramban Tor, tanpa mengekspos IP publik kamu. Tor digunakan untuk mengakses layanan Umbrel kamu dari luar jaringan lokal kamu, tanpa mengekspos perangkat kamu ke Internet ([Siapkan Tor di sistem Anda - Panduan - Komunitas Umbrel](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)). Untuk menggunakan opsi ini, masuk ke pengaturan Umbrel dan ambil URL .onion Umbrel kamu (atau pindai kode QR yang disediakan). Pada peramban Tor, akses .onion Address ini: kamu akan mendapatkan Interface yang sama dengan Interface lokal. 


**Relai Nostr melalui Tor:** Jika kamu ingin relay Nostr-mu bisa dijangkau melalui Tor oleh klienmu (atau teman yang berwenang), hal ini memungkinkan. Umbrel tidak menyediakan relay .onion Address secara langsung, tetapi karena berjalan di port 4848, kamu bisa menggunakan .onion:




    - Gunakan UI Umbrel's .onion Address dan konfigurasikan klien kamu untuk terhubung melalui Interface ini (tidak praktis untuk WebSocket),





- Atau **mengekspos port 4848 sebagai layanan bawang terpisah**. Ini memerlukan pengaturan konfigurasi Tor di Umbrel (disediakan untuk pengguna tingkat lanjut yang sudah terbiasa dengan SSH). Sebagai alternatif, kamu bisa membuat terowongan Tor di server lain yang mengarahkan ke Umbrel; namun, untuk penggunaan pribadi, paling mudah memakai Tailscale.




- Akses melalui **Tailscale:** [Tailscale](https://tailscale.com/) adalah solusi VPN mesh yang menciptakan jaringan privat virtual antara perangkat kamu dan Umbrel. Keuntungannya: bekerja seolah-olah kamu berada di LAN, tetapi melalui Internet, terenkripsi dan tanpa konfigurasi yang rumit. **Tailscale memberikan Umbrel Anda IP tetap dan nama domain pribadi, terlepas dari lokasi jaringannya** ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)). Dalam praktiknya, setelah kamu menginstal Tailscale di Umbrel (dari Umbrel App Store, kategori *Networking*) **dan** pada perangkat kamu (ponsel, PC...), kamu akan dapat menjangkau Umbrel melalui Address seperti `100.x.y.z` (IP Tailscale) atau nama seperti `umbrel.tailnet123.


untuk Nostr_, Tailscale sangat berguna: ponsel kamu, jika memiliki Tailscale aktif, akan dapat terhubung ke `ws://umbrel:4848` (terima kasih kepada MagicDNS) atau langsung ke IP Tailscale dan port 4848 untuk menggunakan relay. Klien seperti Damus atau Amethyst akan melihat Umbrel kamu seolah-olah berada di jaringan lokal yang sama. **Tips:** Aktifkan opsi **MagicDNS** di Tailscale untuk menggunakan nama host `umbrel` alih-alih mengingat IP. Hal ini memastikan koneksi yang lancar ke relay Anda bahkan ketika kamu sedang bepergian ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Terlebih lagi, Tailscale memungkinkan kamu mengakses Interface Umbrel (dan dengan demikian klien web _noStrudel/Snort_) melalui peramban yang sederhana, menggunakan IP pribadi atau nama domain yang ditetapkan. Tidak perlu Tor Browser, dan kecepatan transfer data secara umum lebih baik daripada melalui jaringan Tor.




**Catatan: Tor dan Tailscale tidak saling eksklusif. Kamu bisa tetap mengaktifkan Tor untuk akses anonim atau layanan tertentu, dan menggunakan Tailscale sehari-hari untuk kemudahannya. Dalam kedua kasus tersebut, Anda tidak perlu membuka port pada router kamu, yang memperkuat keamanan.**



### Mengamankan relai Nostr kamu (praktik yang disarankan)


Jika kamu menjadi host relay Nostr di Umbrel, terutama dalam konteks tingkat lanjut, pastikan untuk menerapkan beberapa praktik yang baik:




- **Relai pribadi atau terbatas:** Secara default, relai Umbrel kamu bersifat pribadi (tidak diumumkan kepada publik) dan, jika kamu hanya mengaksesnya melalui Tailscale atau LAN kamu, relay tersebut tidak akan dapat diakses oleh orang asing. **Jaga kerahasiaan tautan** Jangan menyiarkannya di jaringan Nostr publik kecuali jika kamu ingin menjadi tuan rumah bagi pengguna lain secara sukarela, yang merupakan masalah lain (moderasi, bandwidth, dll.). Untuk penggunaan pribadi, kami sarankan untuk membatasi akses ke diri kamu sendiri dan, jika perlu, ke beberapa teman dan keluarga tepercaya.





- Daftar Putih / Auth: Implementasi relai nostr-rs mendukung mekanisme autentikasi **NIP-42** serta *whitelist* kunci publik. Dengan mengaktifkan opsi-opsi ini, kamu dapat membatasi relai kamu sehingga **hanya menerima peristiwa yang ditandatangani oleh kunci tertentu (milik Anda)**, atau bahwa klien harus mengautentikasi untuk mempublikasikan. Pengaturan ini membutuhkan pengeditan file konfigurasi `config.toml` relai di Umbrel (melalui SSH di kontainer Docker). *Ini merupakan manipulasi tingkat lanjut, tetapi sebagai contoh, kamu dapat membuat daftar iklan yang diizinkan* (`pubkey_whitelist`). Dengan cara ini, bahkan jika seseorang menemukan relay kamu, mereka tidak akan dapat memublikasikan apa pun di sana jika tidak ada dalam daftar.





- **Pembaruan dan pemeliharaan:** Selalu perbarui Umbrel dan aplikasi *Nostr Relay* kamu. Pembaruan dapat mencakup peningkatan kinerja (misalnya penanganan spam yang lebih baik) dan perbaikan keamanan. Di Umbrel, periksa App Store secara teratur untuk mengetahui pembaruan *Nostr Relay*, dan terapkan jika diperlukan.





- **Pemantauan dan batasan:** Awasi bagaimana relay kamu digunakan. Jika kamu membukanya untuk orang lain, awasi beban (penyimpanan CPU/RAM) pada Umbrel kamu, karena relai dapat dengan cepat menumpuk banyak data. nostr-rs-relay menawarkan **batas kecepatan dan penyimpanan yang dapat dikonfigurasi** (`batas` dalam konfigurasi, misalnya jumlah kejadian per detik, ukuran kejadian maksimum, pembersihan kejadian lama...). Untuk penggunaan pribadi, kamu mungkin tidak perlu menyentuhnya, tetapi ketahuilah bahwa parameter-parameter ini ada jika kamu membutuhkannya ([nostr-rs-relay/config.toml di master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Mengamankan kunci Nostr: Poin ini sudah disebutkan sebelumnya, tapi sangat penting: jangan pernah memasukkan kunci pribadi Nostr-mu ke interface yang tidak kamu percayai. Sebagai gantinya, gunakan ekstensi browser atau perangkat eksternal (seperti signer Nostr di ponsel terpisah) untuk menandatangani tindakan sensitif. Di Umbrel, klien webmu seperti *Snort* dan *noStrudel* bisa bekerja tanpa mengetahui kunci rahasiamu, lewat NIP-07. Manfaatkan kesempatan ini untuk menggabungkan kenyamanan dan keamanan.




Dengan mengikuti tips berikut, integrasi node Umbrel-mu dengan Nostr akan menjadi kuat dan aman. Kamu akan memiliki lingkungan lengkap: node Bitcoin untuk pembayaran Lightning, relay Nostr pribadi untuk kedaulatan data, dan klien web Nostr berkinerja tinggi untuk menavigasi jaringan sosial terdesentralisasi yang baru ini. Selamat menjelajahi Nostr dengan Umbrel!
