---
name: Joinstr
description: CoinJoins terdesentralisasi melalui jaringan Nostr untuk kerahasiaan Bitcoin yang berdaulat
---

![cover](assets/cover.webp)


Transparansi blockchain Bitcoin memungkinkan siapa pun melacak riwayat transaksi. CoinJoins memutus keterkaitan ini dengan mencampurkan beberapa transaksi yang terjadi secara simultan, sehingga mengembalikan tingkat kerahasiaan yang setara dengan uang tunai.

Namun, solusi tradisional biasanya bergantung pada koordinator terpusat sebagai satu titik kegagalan. Wasabi dan Samourai berhenti beroperasi pada tahun 2024 akibat tekanan regulasi.

**Joinstr** menghapus kelemahan tersebut dengan memanfaatkan jaringan Nostr yang terdesentralisasi untuk kebutuhan koordinasi. Aplikasi sumber terbuka ini memungkinkan CoinJoins yang benar-benar berdaulat, di mana tidak ada otoritas pusat yang dapat menyensor, memantau, atau mengganggu layanan.


## Apa itu Joinstr?



Joinstr adalah alat sumber terbuka yang merevolusi pendekatan CoinJoins dengan memanfaatkan protokol Nostr sebagai infrastruktur koordinasi. Berbeda dengan solusi terpusat yang membutuhkan server khusus, Joinstr bergantung pada jaringan relay Nostr yang terdistribusi untuk memungkinkan para peserta berkoordinasi secara langsung antar rekan.

Arsitektur terdesentralisasi: Jaringan Nostr menggantikan peran koordinator pusat. Peserta membuat atau bergabung dengan "kumpulan" dengan memposting pengumuman terenkripsi melalui relay Nostr. Informasi ini, seperti jumlah, peserta, dan alamat, tetap tidak dapat dipahami oleh relay, sehingga tidak ada entitas pusat yang dapat memantau, menyensor, atau memfilter CoinJoins.

**SIGHASH_ALL|ANYONECANPAY:** Joinstr memanfaatkan flag tanda tangan Bitcoin ini, yang memungkinkan setiap peserta hanya menandatangani input miliknya sendiri sambil tetap memvalidasi seluruh output. Setiap pengguna membuat PSBT secara lokal, menandatanganinya, lalu mendistribusikannya melalui Nostr. Bitcoin kamu tetap berada di bawah kendali eksklusifmu hingga penandatanganan terakhir.

**Filosofi:** Joinstr mengikuti etos cypherpunk Bitcoin, dengan tiga tujuan utama, yaitu **ketahanan terhadap penyensoran** (tidak ada otoritas yang dapat menghentikan layanan), **non-kustodian sepenuhnya** (kamu memegang sendiri private key-mu), dan **perlakuan yang setara** (tidak ada UTXO yang dapat didiskriminasi).



### Fitur utama



**Kumpulan yang fleksibel**: Tidak seperti denominasi tetap, setiap pengguna dapat membuat pool dengan jumlah yang diinginkan dan target jumlah pengguna, mengoptimalkan penggunaan UTXO tanpa pemisahan buatan.



**Biaya transparan**: Tidak ada biaya koordinasi. Hanya biaya transaksi Bitcoin yang dibagi rata di antara para peserta (beberapa ribu satoshi per orang).



**Ephemerality**: Tidak ada data pengguna yang disimpan. Informasi dikirimkan melalui pesan Nostr yang dienkripsi dan segera dihapus setelah transaksi.



### Platform yang tersedia



Tutorial ini berfokus pada **aplikasi Android**, satu-satunya solusi yang saat ini stabil dan direkomendasikan. Plugin Electrum sudah tersedia tetapi memiliki masalah kompatibilitas yang membuatnya tidak stabil. Antarmuka web sedang dalam pengembangan.



## Konfigurasi Inti Bitcoin



Joinstr Android memerlukan koneksi ke node Bitcoin melalui RPC. Kamu perlu mengonfigurasi Bitcoin Core di komputer kamu terlebih dahulu agar dapat menerima koneksi dari ponsel kamu.



**Catatan**: Untuk detail lebih lanjut mengenai konfigurasi lengkap Bitcoin Core, lihat tutorial khusus kami:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Persyaratan jaringan



#### Temukan alamat IP lokal Anda



Ponsel Android kamu harus dapat menjangkau node Bitcoin di jaringan lokal. Temukan alamat IP komputer kamu:



**Di macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Alternatif sederhana:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Di Linux** :



```bash
hostname -I | awk '{print $1}'
```



**Pada Windows** :



```cmd
ipconfig
```



Temukan alamat IPv4 (format `192.168.x.x` atau `10.0.x.x`)



### Konfigurasi RPC



#### Edit bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Cari file `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Perpustakaan/Dukungan Aplikasi/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Buka file dengan editor teks favorit kamu dan tambahkan konfigurasi ini untuk mengaktifkan server RPC.



**Konfigurasi yang direkomendasikan untuk memulai (penanda)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



*konfigurasi *mainnet** (untuk penggunaan produksi):



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Penting** :




- Signet sangat direkomendasikan** untuk pengujian pertama kamu: aplikasi ini masih dalam pengembangan (beta), dan bug mungkin masih ada. Signet memungkinkan kamu melakukan pengujian secara gratis, tanpa mempertaruhkan dana sungguhan
- Ganti `192.168.1.0/24` dengan subnet jaringan kamu (misalnya, jika IP kamu adalah `192.168.68.57`, gunakan `192.168.68.0/24`)



**Keamanan**: Menghasilkan kata sandi yang kuat:



```bash
openssl rand -base64 32
```



### Inisialisasi



#### Mulai ulang dan periksa



1. Matikan Bitcoin Core sepenuhnya


2. Mulai ulang untuk menerapkan konfigurasi




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Saat Bitcoin Core dijalankan untuk pertama kalinya, Bitcoin Core akan mengunduh dan menyinkronkan blockchain Signet. Proses ini jauh lebih cepat dibandingkan mainnet dan biasanya hanya memerlukan beberapa menit. Tunggu hingga sinkronisasi selesai sebelum melanjutkan.


![CRÉATION DE WALLET](assets/fr/04.webp)



Setelah disinkronkan, buat portofolio baru dengan mengklik "Buat wallet baru". Berikan nama eksplisit seperti `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



wallet kamu sekarang telah dibuat dan siap menerima bitcoin yang telah ditandai untuk pengujian.



#### Dapatkan bitcoin yang telah ditandai (tes)



Untuk menguji Joinstr di bookmark, kamu memerlukan bitcoin uji coba gratis:



![SIGNET FAUCET](assets/fr/06.webp)



Gunakan penanda publik seperti :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Di Bitcoin Core, generate alamat penerimaan baru (tab "Terima"), salin dan tempelkan ke dalam formulir faucet. Pecahkan captcha jika perlu. Kamu akan menerima bitcoin yang ditandai secara gratis dalam hitungan detik.



## Aplikasi Android



### Instalasi



![APPLICATION ANDROID](assets/fr/07.webp)



Buka [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) untuk mengunduh versi APK terbaru. Pada browser Android, unduh file, lalu buka untuk memulai penginstalan. Kamu harus mengizinkan penginstalan dari sumber yang tidak dikenal dalam pengaturan keamanan ponsel kamu jika perlu.



### Konfigurasi aplikasi



![PERMISSIONS VPN](assets/fr/08.webp)



Saat pertama kali diluncurkan, aplikasi Joinstr akan meminta izin untuk mengontrol VPN bawaan. Terima kedua permintaan izin tersebut, yaitu kontrol OpenVPN dan koneksi VPN. Izin ini diperlukan untuk integrasi VPN, yang berfungsi melindungi privasi jaringan kamu.


![INTERFACE APPLICATION](assets/fr/09.webp)



Aplikasi Joinstr diatur ke dalam tiga tab utama:




- Beranda**: Layar beranda
- Kolam**: Membuat dan mengelola pool CoinJoin
- Pengaturan**: Konfigurasi aplikasi



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Konfigurasikan pengaturan di tab "Pengaturan":



**1. Relai Nostr **: Alamat relai Nostr untuk koordinasi kolam renang




- Contoh: `wss://relay.damus.io`
- Relay lain yang direkomendasikan: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Penting**: Semua peserta harus menggunakan relay Nostr yang sama untuk melihat dan bergabung dengan pool yang sama. Jika kamu menggunakan relay yang berbeda, kamu tidak akan melihat pool yang dibuat pada relay lain



**2. URL simpul**: Alamat IP node Bitcoin kamu (tanpa port)




- Format: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. Nama Pengguna RPC** : Nama pengguna yang dikonfigurasikan dalam `rpcuser=` pada bitcoin.conf 




- Contoh: `satoshi



**4. Kata Sandi RPC ** : Kata sandi yang ditetapkan dalam `rpcpassword=` pada bitcoin.conf



**5. Port RPC**: Port RPC tergantung pada jaringan




- Mainnet ** : `8332`
- Penanda**: `38332`



**6. Wallet **: Pilih portofolio Bitcoin Core yang berisi UTXO yang akan dicampur




- Contoh: `tuto_joinstr_signet`



**7. Gerbang VPN**: Pilih server VPN Riseup




- Contoh: `(Paris) vpn07-par.riseup.net`
- Lainnya tersedia: Amsterdam, Seattle, dll.
- ⚠️ **Penting**: Semua peserta dalam pool yang sama harus menggunakan **Gateway VPN yang sama** untuk berpartisipasi dalam CoinJoin. Selama proses pencampuran, semua peserta harus muncul dengan alamat IP keluar yang sama untuk mencegah analisis jaringan mengkorelasikan pengguna



Aplikasi Joinstr **terintegrasi secara native** dengan Riseup VPN, menyederhanakan koordinasi antar pengguna.



**Penting** :




- Pastikan ponsel dan komputer kamu berada di jaringan WiFi lokal yang sama
- Koneksi VPN akan diaktifkan secara otomatis saat berpartisipasi dalam sebuah pool
- Klik **"Simpan "** setelah kamu menetapkan semua parameter



## Penggunaan praktis



### Membuat atau bergabung dengan grup



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Kamu memiliki dua opsi untuk berpartisipasi dalam CoinJoin:



**Opsi 1: Membuat kolam baru**



Klik "Buat Kumpulan Baru" di tab "Kumpulan". Tentukan denominasi dalam BTC, misalnya 0,002 BTC, dan jumlah peserta yang diinginkan, minimal 2 dan disarankan 3 sampai 5 untuk anonimitas yang lebih baik. Aplikasi kemudian akan menunggu pengguna lain untuk bergabung ke pool kamu. Setelah jumlah peserta yang dibutuhkan tercapai, proses pendaftaran output akan dimulai secara otomatis, dan kamu perlu memilih UTXO yang ingin dicampur lalu klik "Daftar".



**⏱️ Penting**: Pool akan kedaluwarsa setelah **10 menit** tidak ada aktivitas. Jika jumlah pengguna yang dibutuhkan tidak tercapai, pool akan ditutup secara otomatis.



**Opsi 2: Bergabung dengan grup yang sudah ada**



Pada tab "Lihat Pool Lainnya", telusuri pool yang tersedia yang dibuat oleh pengguna lain. Pilih pool yang sesuai dengan jumlah Anda dan bergabunglah. Pastikan kamu sudah mengonfigurasi relai Nostr dan VPN Gateway yang sama dengan peserta lainnya (lihat bagian Konfigurasi).



*aturan pemilihan *UTXO**: UTXO kamu harus sedikit lebih tinggi dari denominasi pool (antara +500 dan +5000 surplus sats).



**Contoh**: Untuk pool 0,002 BTC (200.000 sats), gunakan UTXO antara 200.500 dan 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Prosesnya kemudian **sepenuhnya otomatis:** setelah input kamu didaftarkan, aplikasi akan menunggu semua peserta mendaftarkan input mereka. Setelah seluruh input terdaftar, PSBT dibuat, lalu secara otomatis ditandatangani menggunakan kunci kamu dan digabungkan dengan tanda tangan peserta lainnya. Terakhir, transaksi yang sudah lengkap akan disiarkan ke jaringan Bitcoin. Kamu akan menerima TXID, atau pengenal transaksi, setelah siaran selesai. Tidak diperlukan manipulasi manual pada PSBT di Android.



### Verifikasi on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Setelah transaksi disiarkan, kamu akan menerima TXID (pengenal transaksi). Lihatlah di [mempool.space](https://mempool.space) atau peramban favorit kamu. Untuk menguji pada penanda, gunakan [mempool.space/signet](https://mempool.space/signet).



Anda dapat mengamati :





- N entri**: Satu per peserta (dalam contoh kami, 2 entri)
- N output identik**: jumlah persis dari denominasi (di sini, 2 output masing-masing 0,00199800 BTC)
- Diagram alir**: mempool.space secara visual menampilkan campuran input dan output
- Fitur**: Transaksi dapat diidentifikasi sebagai SegWit, Taproot, RBF, dll.



Karena semua output utama memiliki jumlah yang sama, maka **tidak mungkin untuk menentukan yang mana milik siapa**. Ini adalah prinsip dasar CoinJoin: output yang tidak dapat dibedakan.



**Contoh tanda tangan transaksi**: [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Harap diperhatikan**: Jika UTXO kamu lebih besar daripada denominasi kumpulan, kamu akan menghasilkan change output atau kembalian. UTXO kembalian ini tetap dapat dilacak dan harus dikelola secara terpisah dari output anonim kamu. Jangan pernah menggabungkannya dengan output hasil pencampuran kamu.



## Paket kualitas dan anonimitas CoinJoin



Efisiensi CoinJoin diukur dengan **anonset**: jumlah output dengan nilai yang sama yang dihasilkan oleh transaksi. Semakin tinggi angka ini, semakin sulit untuk menentukan input mana yang sesuai dengan output yang mana.



Joinstr saat ini menghasilkan rata-rata **2 hingga 5 peserta**. Angka-angka ini lebih rendah daripada koordinator terpusat tradisional seperti Wasabi (50-100 peserta) atau Whirlpool (5-10 peserta), tetapi itulah harga dari desentralisasi.



💡 **Untuk memahami set anonimitas dan perhitungannya secara mendetail**, lihat kursus lengkap kami: [Set anonimitas](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs CoinJoins lainnya




| Aspek | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Peserta per pool** | 50-100 | 5-10 | Variabel (P2P) | **2-5** |
| **Koordinator** | Tersentralisasi (ditutup 2024) | Tersentralisasi (aktif) | P2P maker/taker | **Tidak ada (Nostr)** |
| **Ketahanan sensor** | Lemah | Sedang | Sangat tinggi | **Sangat tinggi** |
| **Biaya koordinasi** | Persentase | Biaya masuk | Dibayar kepada pembuat | **Tidak ada** |
| **Diskriminasi UTXO** | Ya (daftar hitam) | Tidak | Tidak | **Tidak** |

💡 **Solusi CoinJoin aktif lainnya**:




- Ashigaru**: Implementasi sumber terbuka dari protokol Whirlpool dengan koordinator terpusat tetapi dapat digunakan dengan cara yang terdesentralisasi. Terus beroperasi setelah penyitaan Samourai Wallet pada tahun 2024.
- JoinMarket**: Solusi P2P terdesentralisasi tanpa koordinator pusat, berdasarkan model bisnis pembuat/pengambil di mana "pembuat" menyediakan likuiditas dan dibayar oleh "pengambil".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Pengorbanan yang mendasar:** Joinstr dan JoinMarket adalah dua solusi tanpa koordinator pusat. JoinMarket menggunakan model bisnis P2P dengan insentif finansial, sementara Joinstr memanfaatkan Nostr untuk koordinasi tanpa biaya. Joinstr mengorbankan anonimitas skala besar yang instan demi kesederhanaan, seperti tidak adanya manajemen maker dan taker, serta ketiadaan biaya koordinasi..



**Rekomendasi praktis**: Untuk mengimbangi pool yang lebih kecil, jalankan beberapa putaran CoinJoin secara berurutan dengan pengguna yang berbeda. Atur jarak antar ronde dan ubah relay Nostr di antara setiap ronde untuk memaksimalkan kerahasiaanmu.



Silakan baca kursus lengkap kami tentang privasi bitcoin untuk informasi lebih lanjut tentang topik ini:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Keuntungan dan keterbatasan



### Sorotan



**Privasi yang ditingkatkan**: Kombinasi enkripsi komunikasi Nostr, VPN bersama di antara para pengguna, dan penggunaan Tor yang direkomendasikan menciptakan proteksi berlapis-lapis yang sulit dilewati.



**Transparan, biaya minimal**: Tidak ada biaya koordinasi, hanya biaya mining yang dibagi secara adil di antara para pengguna. Tidak ada persentase yang dipungut oleh operator mana pun.



### Kendala yang perlu dipertimbangkan





- Likuiditas variabel**: Kumpulan yang lebih kecil, dapat menunggu peserta berkumpul
- Proyek sedang berlangsung**: Aplikasi dalam versi beta, mungkin ada bug. Uji terlebih dahulu dengan jumlah kecil pada penanda
- Serangan Sybil**: Kemungkinan satu lawan mengendalikan beberapa peserta pool



## Praktik terbaik



** Isolasi UTXO**: Jangan pernah menggabungkan UTXO campuran dengan yang tidak dicampur. Gunakan portofolio terpisah untuk output anonim Anda.



**Penting untuk melakukan beberapa putaran**: Lakukan minimal 3 putaran berturut-turut dengan peserta yang berbeda. Variasikan jumlah dan pengaturan waktu untuk menghindari pola. Beri jarak waktu beberapa jam.



**Perlindungan jaringan**: Gunakan Tor secara sistematis sebagai tambahan dari VPN bawaan. Hasilkan kunci Nostr yang bersifat sementara untuk setiap sesi penting.



**Kemajuan hati-hati**: Mulailah menandai dengan jumlah yang kecil.



## Kesimpulan



Joinstr mewakili solusi privasi Bitcoin yang benar-benar terdesentralisasi. Dengan memanfaatkan Nostr untuk koordinasi, alat ini menghilangkan ketergantungan pada koordinator pusat sambil tetap menjaga kedaulatan pengguna.

**Untuk pengguna yang menghargai ketahanan terhadap penyensoran dan siap melakukan beberapa putaran CoinJoin untuk mengimbangi ukuran pool yang lebih kecil.

Dengan latar belakang pengawasan keuangan yang terus meningkat, alat terdesentralisasi untuk melindungi privasi menjadi semakin penting.


## Sumber daya



### Dokumentasi resmi




- [Situs web resmi Joinstr](https://joinstr.xyz)
- [Dokumentasi pengguna](https://docs.joinstr.xyz/users/using-joinstr)
- [Dokumentasi teknis](https://docs.joinstr.xyz/overview/how-does-it-work)
- [Kode sumber GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [Aplikasi Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Tutorial




- [Tutorial plugin Electrum](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Panduan lengkap oleh Uncensored Tech



### Komunitas dan dukungan




- [Telegram Joinstr Group](https://t.me/joinstr) - Dukungan komunitas dan pojok penanda
- [Diskusi teknis tentang DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Alat tambahan




- [Bookmark Faucet](https://signetfaucet.com) - Uji coba Bitcoin gratis
- [Alt Signet Faucet](https://alt.signetfaucet.com) - alternatif Faucet
- [Mempool.space](https://mempool.space) - Block explorer dengan analisis privasi
