---
name: Mostro
description: Platform pertukaran Bitcoin P2P bebas KYC melalui Lightning dan Nostr
---

![cover](assets/cover.webp)



Bagaimana cara Anda mendapatkan atau menjual bitcoin tanpa mengorbankan kedaulatan finansial Anda? Platform terpusat memberlakukan prosedur KYC invasif yang mengekspos data pribadi Anda, dengan kemungkinan pembekuan akun yang sewenang-wenang atau pengawasan negara.



**Mostro P2P** menawarkan alternatif terdesentralisasi yang menggabungkan Lightning Network, protokol Nostr, dan faktur penahanan. Inovasi utamanya: sistem escrow otomatis di mana bitcoin Anda tetap berada di bawah kendali Anda di seluruh bursa, menghilangkan risiko pencurian, kebangkrutan bursa, atau penyitaan sewenang-wenang.



## Apa yang dimaksud dengan Mostro P2P?



Mostro P2P adalah protokol pertukaran Bitcoin sumber terbuka yang dibuat oleh **grunch**, pengembang bot Telegram populer **lnp2pbot** yang diluncurkan pada tahun 2021. Meskipun lnp2pbot telah mengaktifkan pertukaran P2P bebas KYC melalui Lightning, namun hal ini menimbulkan kerentanan yang besar: **Telegram merupakan titik kegagalan terpusat** yang rentan terhadap penyensoran oleh pemerintah.



Mostro mewakili **evolusi terdesentralisasi** dari konsep ini: dengan mengganti Telegram dengan protokol **Nostr** (jaringan relay terdistribusi yang tidak dapat disensor), Mostro menghilangkan risiko sistemik ini. Protokol ini menggabungkan Lightning Network untuk transaksi instan, Nostr untuk komunikasi yang tahan sensor, dan **penyimpanan faktur** untuk menciptakan escrow otomatis yang benar-benar non-kustodian.



### Arsitektur teknis



Mostro bekerja melalui tiga komponen:




- Daemon Mostrod**: pertukaran koordinat antara pengguna dan Lightning Network
- Node Lightning**: membuat faktur penahanan (eskro kriptografi ~ 24 jam)
- Pelanggan Mostro**: antarmuka pengguna (CLI, Seluler, Web)



Pesanan dipublikasikan di Nostr sebagai peristiwa publik (tipe 38383), sementara perdagangan pribadi ditransmisikan melalui pesan terenkripsi ujung ke ujung (NIP-59, NIP-44). Setiap instance Mostro mendefinisikan biayanya sendiri (umumnya antara 0,3% dan 1%) dan batas transaksi (mulai dari beberapa ribu hingga beberapa ratus ribu sats, tergantung pada instance).



### Keuntungan yang menentukan



**Tahan sensor**: Tidak ada pemerintah yang dapat menutup Mostro selama relai Nostr masih ada di suatu tempat di dunia. Tidak seperti lnp2pbot yang rentan melalui Telegram, Mostro mengizinkan pertukaran yang **tahan sensor**.



**Escrow non-kustodian**: Faktur penahanan kilat mengunci bitcoin Anda tanpa mentransfernya secara permanen. Dana Anda tetap berada di bawah kendali Anda dan secara otomatis dikembalikan kepada Anda jika terjadi masalah (~24 jam).



**Kerahasiaan berdasarkan desain**: Tersedia dua mode yang sesuai dengan kebutuhan Anda. Mode Reputasi** menghubungkan reputasi Anda dengan kunci Nostr Anda untuk membangun kepercayaan yang langgeng. Mode Pribadi Penuh ** mendukung anonimitas absolut dengan kunci sementara sekali pakai.



## Fitur utama



**Komunikasi yang terdesentralisasi**: Semua pesanan dipublikasikan di Nostr melalui peristiwa yang ditandatangani secara kriptografis. Negosiasi pribadi dikirimkan melalui pesan terenkripsi ujung ke ujung, menjamin kerahasiaan mutlak.



**Sistem reputasi**: peringkat bintang 5 dengan perhitungan berulang yang disimpan secara permanen di Nostr. Memungkinkan Anda membangun reputasi sebagai trader andal secara bertahap.



**Arbitrase terdesentralisasi**: Jika terjadi sengketa, arbiter yang tidak memihak akan memeriksa bukti dan membuat keputusan berdasarkan kriteria yang transparan. Setiap sengketa menghasilkan token yang unik untuk penelusuran.



**Fleksibilitas pembayaran**: Dukungan untuk banyak mata uang fiat melalui layanan nilai tukar yadio.io. Menerima transfer SEPA, PayPal, Revolut, uang tunai, dan metode apa pun yang disetujui oleh kedua belah pihak.



## Tersedia pelanggan Mostro



Mostro menawarkan dua klien operasional utama untuk bursa P2P Anda.



### Mostro CLI - Klien Baris Perintah



**Mostro CLI** adalah klien yang paling matang dan fungsional. Ditulis dalam Rust, ia menawarkan berbagai fitur Mostro melalui antarmuka baris perintah. Kompatibel dengan macOS, Linux dan Windows.



**Kontrol utama** :




- 'daftar pesanan': Menampilkan semua pesanan yang tersedia
- `pemesan baru`: Membuat pesanan beli atau jual baru
- `takesell` / `takebuy`: Mengambil pesanan beli atau jual
- `fiatsent`: Konfirmasi pengiriman pembayaran fiat
- `release`: Lepaskan escrow dan selesaikan pertukaran
- `getdm`: Melihat pesan langsung
- `rate`: Mengevaluasi mitra pengimbang Anda setelah pertukaran



Ideal untuk pengguna teknis, otomatisasi, dan lingkungan yang membutuhkan keamanan maksimum.



### Mostro Mobile - Aplikasi ponsel cerdas



Aplikasi seluler **mobile app** dalam versi alfa memungkinkan perdagangan P2P langsung dari ponsel cerdas Anda. Grafis intuitif Interface dengan navigasi tab, tampilan order, filter canggih, dan obrolan terintegrasi untuk berkomunikasi dengan rekanan Anda.



Tersedia untuk **Android** (melalui APK di GitHub), ini adalah pilihan optimal bagi pengguna yang menyukai kesederhanaan dan sesekali melakukan trading seluler.



### Mostro-web - Web Interface (dalam pengembangan)



Interface aplikasi web JavaScript tingkat lanjut yang sedang dalam pengembangan aktif. Dirancang untuk menawarkan pengalaman pengguna yang lengkap dengan fungsi perdagangan dan manajemen portofolio yang luas. Akses melalui browser tanpa perlu instalasi.



## Instalasi dan konfigurasi



Tutorial ini akan memandu Anda melalui instalasi dan penggunaan dua klien utama Mostro: CLI dan aplikasi seluler.



### Prasyarat penting



Sebelum memulai, Anda akan memerlukan :





- Lightning Network** wallet yang berfungsi dengan likuiditas yang cukup (atau kompatibel dengan Lightning)
 - Direkomendasikan: Phoenix, Breez, Wallet dari Satoshi...
 - Minimum 1000 satoshi likuiditas untuk diuji



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Kunci pribadi Nostr** (format `nsec1...`)
 - Buat kunci perdagangan khusus di [nostrkeygen.com](https://nostrkeygen.com/)
 - Penting**: Jangan pernah menggunakan tombol Nostr pribadi utama Anda
 - Simpan kunci pribadi Anda di tempat yang aman (pengelola kata sandi)





- Opsional, tetapi direkomendasikan**: Koneksi VPN atau Tor untuk menyamarkan alamat IP Anda



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Instalasi Mostro CLI



#### Di macOS



**Langkah 1: Pemeriksaan Rust**



Periksa apakah Rust sudah terinstal (diperlukan versi 1.64+):



```bash
rustc --version
```



Jika Rust tidak dipasang:



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Langkah 2: Mengkloning repositori**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Langkah 3: Konfigurasi**



Salin dan edit file :



```bash
cp .env-sample .env
```



Buka `.env` dan konfigurasikan pengaturan Anda:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Penting untuk sinkronisasi CLI/Mobile**: Untuk mengakses pesanan yang sama pada CLI dan aplikasi seluler, Anda harus menggunakan **Mostro Pubkey** dan **relay Nostr** yang sama pada kedua klien. Periksa pengaturan ini di Pengaturan pada aplikasi seluler.



![Configuration .env](assets/fr/02.webp)



**Langkah 4: Instalasi**



Kompilasi dan instal CLI :



```bash
cargo install --path .
```



Kompilasi membutuhkan waktu 1-2 menit. Eksekusi `mostro-cli` akan terinstal di `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Langkah 5: Periksa**



Periksa apakah semuanya berfungsi:



```bash
mostro-cli --help
```



Anda akan melihat daftar pesanan yang lengkap.



![Vérification avec --help](assets/fr/04.webp)



#### Di Linux (Ubuntu/Debian)



Instalasi identik dengan macOS, dengan tambahan file :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Kemudian ikuti langkah 3 dan 4 di bagian macOS.



#### Pada Windows



Pertama-tama instal Rust melalui [rustup.rs] (https://rustup.rs/), kemudian gunakan PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Konfigurasi yang sama: salin `.env-sample` ke `.env` dan isi parameter Anda.



### Menginstal Mostro Mobile



#### Di Android



**Langkah 1**: Buka [halaman rilis GitHub] (https://github.com/MostroP2P/mobile/releases) dan unduh file **app-release.apk** (sekitar 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Langkah 2: Setelah diunduh, buka file APK dari unduhan Anda. Android akan meminta Anda untuk mengesahkan penginstalan dari sumber ini.



![Téléchargement et installation APK](assets/fr/11.webp)



**Langkah 3**: Ikuti layar orientasi, yang menampilkan fungsi-fungsi:




- Perdagangkan Bitcoin dengan bebas - tanpa KYC **: Berdagang tanpa verifikasi identitas berkat Nostr
- Privasi secara default**: Pilih antara mode Reputasi dan mode Privasi penuh
- Keamanan di setiap langkah**: Perlindungan dengan faktur tanpa penahanan kustodian



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Langkah 4**: Lanjutkan orientasi untuk menemukan :




- Obrolan yang sepenuhnya terenkripsi**: Komunikasi terenkripsi ujung ke ujung
- Ambil penawaran**: Jelajahi buku pesanan dan pilih penawaran
- Tidak dapat menemukan apa yang Anda butuhkan? Buat pesanan khusus Anda sendiri



![Suite onboarding](assets/fr/13.webp)



**Langkah 5: Setelah proses penyiapan selesai, aplikasi akan secara otomatis menghasilkan sepasang tombol Nostr. Masuk ke menu (☰) lalu **Akun** untuk menyimpan **Kata Rahasia** (frasa pemulihan) Anda. Di layar ini juga Anda memiliki opsi untuk mengubah mode privasi yang telah disebutkan sebelumnya.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Penting**: Tuliskan frasa pemulihan Anda di tempat yang aman (pengelola kata sandi, brankas kertas).



### Konfigurasi keamanan awal



Apa pun platform yang Anda gunakan:





- Kunci khusus**: Gunakan identitas Nostr yang terpisah untuk trading
- Jumlah kecil**: Mulai dengan kurang dari sats 10.000 untuk memulai
- Beberapa relai**: Konfigurasikan 3-5 relai yang beragam secara geografis
- Perlindungan jaringan**: Aktifkan VPN atau Tor untuk menyembunyikan alamat IP Anda
- Wallet aman **: Aktifkan penguncian otomatis wallet Lightning Anda



## Gunakan dengan CLI



Bagian ini mendemonstrasikan pembelian bitcoin melalui Mostro CLI dengan mengikuti contoh kasus penggunaan di dunia nyata.



### Langkah 1: Buat daftar pesanan yang tersedia



Perintah `listorders` menampilkan semua pesanan yang aktif:



```bash
mostro-cli listorders
```



Anda akan melihat tabel dengan rincian setiap pesanan: ID, jenis (beli/jual), jumlah, mata uang, metode pembayaran.



![Liste des ordres disponibles](assets/fr/05.webp)



Dalam contoh ini, order untuk menjual 5 EUR melalui Revolut terlihat (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Langkah 2: Mengambil pesanan



Untuk membeli bitcoin ini, lakukan pemesanan dengan `takesell`:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro akan meminta Anda untuk memberikan **Faktur Lightning** untuk menerima BTC. Jumlah pasti dalam satoshi ditunjukkan (di sini: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Langkah 3: Berikan faktur Lightning Anda



Buat faktur Lightning dari wallet (Phoenix, Breez, dll.) Anda dengan jumlah yang tepat, lalu kirimkan:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Sistem akan mengonfirmasi pengiriman dan meminta Anda untuk menunggu penjual membayar faktur penangguhan sebelum mengaktifkan eskro.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Langkah 4: Hubungi penjual



Setelah eskro diaktifkan, gunakan `dmtouser` untuk meminta detail pembayaran dari penjual:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Langkah 5: Ambil jawabannya



Periksa pesan langsung untuk melihat respons penjual:



```bash
mostro-cli getdm
```



Penjual memberi Anda ID pembayarannya (di sini Revtag-nya: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Langkah 6: Melakukan pembayaran fiat



Kirimkan pembayaran melalui metode yang telah disepakati (Revolut dalam contoh ini) ke detail kontak yang diberikan. **Simpan semua dokumen pendukung** (tangkapan layar, referensi transaksi).



### Langkah 7: Konfirmasi pengiriman pembayaran



Setelah pembayaran dilakukan, beri tahu Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Langkah 8: Penerimaan bitcoin



Segera setelah penjual mengonfirmasi penerimaan fiat dan melepaskan escrow dengan perintah `release`, Anda akan langsung menerima bitcoin pada faktur Lightning yang Anda berikan.



### Langkah 9: Evaluasi



Beri nilai penjual untuk berkontribusi pada reputasi yang terdesentralisasi:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Perintah yang berguna



**Membatalkan pesanan** (sebelum pesanan diambil):


```bash
mostro-cli cancel -o <order-id>
```



**Buat pesanan penjualan baru**:


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Buka sengketa** :


```bash
mostro-cli dispute -o <order-id>
```



## Gunakan dengan aplikasi seluler



Bagian ini mendemonstrasikan penjualan bitcoin melalui Mostro Mobile dengan mengikuti contoh kasus penggunaan di dunia nyata.



### Interface utama



Aplikasi ini memiliki 3 tab utama:





- Buku Pesanan**: Jelajahi pesanan beli (BELI BTC) dan jual (JUAL BTC) yang tersedia
- Perdagangan Saya**: Melihat order aktif dan historis Anda
- Mengobrol**: Berkomunikasi dengan rekanan Anda menggunakan angka



![Interface principale](assets/fr/14.webp)



### Konfigurasi yang disarankan



Sebelum melakukan trading, konfigurasikan beberapa pengaturan melalui menu (☰) > **Pengaturan** :





- Lightning Address** (opsional): Untuk menerima pembayaran secara langsung
- Relai**: Tambahkan beberapa relai Nostr untuk ketahanan (mis. `wss: //nos.lol`, `wss: //relay.damus.io`)
- Mostro Pubkey**: Periksa kunci publik dari instans Mostro yang Anda gunakan



![Paramètres de l'application](assets/fr/16.webp)



**Penting untuk sinkronisasi CLI/Sinkronisasi seluler**: Jika Anda menggunakan CLI dan aplikasi seluler, konfigurasikan **relay Nostr dan Mostro Pubkey yang sama persis di kedua klien. Tanpa konfigurasi yang identik ini, Anda tidak akan melihat pesanan yang sama tersedia di kedua antarmuka. Relai dan Mostro Pubkey yang terlihat di Pengaturan (gambar di atas) harus sama dengan yang ada di file `.env' CLI Anda.



### Langkah 1: Buat order jual



Tekan tombol **"+"** berwarna hijau di kanan bawah, lalu pilih **JUAL** (tombol merah).



![Boutons de création d'ordre](assets/fr/17.webp)



Isi formulir pembuatan :



1. **Mata Uang**: Pilih mata uang yang ingin Anda terima (EUR, USD, dll.)


2. **Jumlah** : Masukkan jumlah dalam fiat (mis. 1 hingga 3 EUR)


3. **Metode pembayaran** : Pilih metode (mis. "Revolut")


4. **Jenis harga**: Pilih "Harga Pasar"


5. **Premium**: Sesuaikan premi (penggeser dari -10% hingga +10%, disarankan: 0% untuk menjual dengan cepat)



Tekan **Kirim** untuk mempublikasikan pesanan Anda.



### Langkah 2: Konfirmasi publikasi



Pesanan Anda sekarang sudah diterbitkan! Pesanan akan tersedia selama 24 jam. Anda dapat membatalkannya kapan saja sebelum pembeli mengambilnya dengan menjalankan perintah `batal`.



![Ordre publié](assets/fr/18.webp)



Order muncul di tab **Trade Saya** dengan status "Tertunda" dan lencana "Dibuat oleh Anda".



### Langkah 3: Pembeli mengambil pesanan Anda



Ketika pembeli mengambil pesanan Anda, Anda akan menerima notifikasi. Lihat detailnya di **Perdagangan Saya**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Instruksi penting**: Anda sekarang harus **membayar faktur penahanan** yang ditampilkan untuk mengunci bitcoin Anda (di sini 4674 sats untuk 1-5 EUR) di escrow. Anda memiliki waktu **15 menit maksimum** jika tidak, pertukaran akan dibatalkan.



Salin faktur penahanan dan bayarlah dari wallet Lightning (Phoenix, Breez, dll.) Anda.



### Langkah 4: Berkomunikasi dengan pembeli



Setelah eskro diaktifkan, tekan **KONTAK** untuk membuka obrolan terenkripsi dengan pembeli.



Pembeli (di sini "anonymous-gloriaZhao") akan menghubungi Anda untuk meminta detail pembayaran Anda. Mohon balas dengan detail Anda (Revtag, IBAN, dll.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Langkah 5: Tanda terima pembayaran fiat



Tunggu hingga Anda menerima pembayaran fiat di akun Revolut Anda (atau metode lain yang disepakati). **Periksa dengan cermat**:




- Jumlah yang tepat
- Pengirim
- Referensi jika diminta



Pembeli akan memberi tahu Anda melalui obrolan bahwa ia telah mengirim pembayaran. Mostro juga akan menampilkan pesan yang mengonfirmasi bahwa fiat telah dikirim kepada Anda.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Langkah 6: Lepaskan escrow



Setelah Anda mendapatkan **konfirmasi tanda terima** pembayaran fiat di akun Anda, tekan tombol hijau **LEPAS** dan konfirmasikan untuk mengirim satss ke pembeli.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoin langsung ditransfer ke pembeli melalui faktur Lightning-nya.



### Langkah 7: Mengevaluasi pertimbangan



Setelah rilis, tekan **RATE** untuk memberi nilai pada pembeli. Pilih dari 1 hingga 5 bintang (di sini 5/5) dan tekan **Kirimkan Peringkat**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Pertukaran sudah berakhir!



### Beli bitcoin dengan aplikasi seluler



Proses untuk **membeli** bitcoin serupa tetapi terbalik:



1. Jelajahi tab **Buku Pesanan** > **BELI BTC** untuk melihat pesanan jual


2. Klik pada pesanan yang menarik untuk melihat detailnya


3. Tekan **Terima Pesanan**


4. Berikan faktur Lightning Anda (yang dihasilkan dari wallet Anda)


5. Tunggu sampai penjual mengaktifkan eskro


6. Hubungi penjual melalui **KONTAK** untuk detail pembayaran


7. Kirim pembayaran fiat (simpan bukti)


8. Penjual melepaskan escrow setelah verifikasi


9. Terima bitcoin secara instan di faktur Lightning Anda


10. Beri nilai penjual (1-5 bintang)



### Manajemen masalah



**Membatalkan order**: Di **Trading Saya**, tekan order Anda lalu tombol **BATAL** (hanya tersedia sebelum order diambil).



**Buka sengketa**: Jika terjadi perselisihan, tekan **BUKA SENGKETA** pada detail pesanan. Lampirkan semua bukti (tangkapan layar obrolan, referensi transaksi bank).



## Keuntungan dan keterbatasan



### Manfaat



**Kedaulatan finansial**: Bitcoin Anda tidak akan pernah lepas dari kendali langsung Anda berkat mekanisme penahanan faktur, sehingga menghilangkan risiko kebangkrutan bursa atau pembajakan.



**Tahan sensor**: Tidak ada otoritas yang dapat mematikan jaringan atau menyensor pesanan Anda. Sistem ini bekerja selama relay Nostr beroperasi.



**Anonimitas default**: Hanya kunci Nostr samaran yang mengidentifikasi Anda, tanpa KYC atau data pribadi. Komunikasi terenkripsi ujung ke ujung.



**Fleksibilitas pembayaran**: Semua metode pembayaran yang diterima bersama dapat dilakukan (transfer, aplikasi seluler, uang tunai, barter).



### Keterbatasan



**Pengembangan awal**: Antarmuka yang belum sempurna dan kurva pembelajaran teknis yang diperlukan.



**Likuiditas terbatas**: Jumlah pesanan terbatas, terutama untuk jumlah besar atau mata uang langka.



**Persyaratan teknis**: Diperlukan pemahaman dasar tentang Lightning dan Nostr.



**Tanggung jawab individu**: Tidak ada dukungan terpusat jika terjadi masalah, diperlukan kehati-hatian.



## Kesimpulan



Mostro P2P merupakan alternatif yang menjanjikan untuk bursa terpusat, menggabungkan Lightning Network, Nostr, dan escrow otomatis untuk perdagangan yang benar-benar terdesentralisasi. Meskipun masih dalam tahap awal pengembangan dan likuiditas yang terbatas, platform ini telah menawarkan kedaulatan keuangan, ketahanan terhadap sensor, dan anonimitas default.



Bagi para pengguna bitcoin yang lebih memilih otonomi dan kerahasiaan, Mostro merupakan pilihan yang layak untuk dieksplorasi secara progresif. Arsitekturnya yang terdesentralisasi menjamin evolusi komunitas daripada komersial, membuka jalan bagi masa depan bursa Bitcoin yang benar-benar gratis.



## Sumber daya



### Dokumentasi resmi




- [Situs web resmi Mostro](https://mostro.network)
- [Dokumentasi teknis](https://mostro.network/docs-english/index.html)
- [Mostro Foundation](https://mostro.foundation)



### Kode sumber dan pengembangan




- [Repositori GitHub utama](https://github.com/MostroP2P/mostro)
- [Klien web](https://github.com/MostroP2P/mostro-web)
- [Pelanggan CLI] (https://github.com/MostroP2P/mostro-cli)



### Komunitas




- [Protokol Nostr](https://nostr.com)
- [Panduan Lightning Network](https://lightning.network)