---
name: Silentium
description: Web progresif wallet dengan dukungan Pembayaran Senyap (BIP-352)
---

![cover](assets/cover.webp)



Penggunaan kembali alamat Bitcoin adalah salah satu ancaman paling langsung terhadap kerahasiaan pengguna. Ketika seorang penerima berbagi satu alamat untuk menerima banyak pembayaran, setiap pengamat dapat melacak semua transaksi yang terkait dan merekonstruksi riwayat keuangan mereka. Masalah ini terutama mempengaruhi pembuat konten, badan amal atau aktivis yang ingin menampilkan alamat donasi secara publik tanpa mengorbankan privasi mereka.



Silentium menjawab masalah ini dengan solusi elegan yang dapat diakses langsung dari browser Anda. Aplikasi web progresif sumber terbuka (PWA) ini, diluncurkan pada Mei 2024 oleh Louis Singer, mengimplementasikan Silent Payments (BIP-352): alamat statis yang dapat digunakan kembali di mana setiap pembayaran berakhir di alamat blockchain yang terpisah, tanpa interaksi sebelumnya atau tautan yang dapat diamati antara transaksi.



**Peringatan penting**: Silentium adalah sebuah proyek eksperimental yang berfungsi sebagai *bukti konsep* untuk dompet ringan Silent Payments. Ini tidak boleh digunakan sebagai wallet harian atau untuk menyimpan jumlah yang signifikan. Para pengembang secara eksplisit menyatakan:



> Gunakan dengan risiko Anda sendiri.

Perhatikan bahwa wallet ini dapat digunakan sebagai testnet atau regtest.



## Apa itu Silentium?



### Filosofi dan tujuan



Silentium berfungsi sebagai demonstrasi teknis untuk mengimplementasikan Pembayaran Senyap dalam peramban wallet yang ringan. Meskipun juga mendukung alamat Bitcoin konvensional, penekanannya adalah pada Pembayaran Senyap untuk memungkinkan pengguna bereksperimen dengan teknologi privasi ini dengan cara yang mudah.



### Bagaimana cara kerja Pembayaran Diam?



Pembayaran Senyap (BIP-352) menggunakan Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Penerima menghasilkan alamat statis (`sp1...` pada mainnet, `tsp1...` pada testnet) yang terdiri dari dua kunci publik: kunci pemindaian untuk mendeteksi pembayaran, dan kunci pembelanjaan untuk menggunakannya.



Pengirim menggabungkan kunci masukan pribadinya dengan kunci pemindaian penerima untuk menghitung rahasia bersama yang menghasilkan "tweak" kriptografi. Tweak ini, yang ditambahkan ke kunci pengeluaran, menciptakan alamat Taproot yang unik untuk setiap transaksi. Penerima mereproduksi perhitungan ini dengan kunci pemindaian pribadinya untuk mendeteksi dan membelanjakan dana tanpa interaksi sebelumnya.



Keuntungan: kerahasiaan yang ditingkatkan untuk pengirim dan penerima, tidak memerlukan server pihak ketiga, transaksi tidak dapat dibedakan dari pembayaran Taproot konvensional. Kerugian utama: pemindaian blockchain yang intensif untuk mendeteksi pembayaran.



Untuk mengetahui lebih lanjut tentang cara kerja teoretis dari Pembayaran Diam, lihat bagian terakhir dari kursus BTC.204 tentang Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Platform yang didukung



Silentium adalah Aplikasi Web Progresif (PWA) yang dapat diakses dari peramban modern apa pun (seluler atau desktop). Gunakan secara langsung di `app.silentium.dev`, instal sebagai aplikasi asli melalui browser Anda, atau gunakan secara lokal. Instalasi dilakukan langsung dari peramban, tanpa melalui toko resmi.



## Menggunakan Aplikasi Web



### Akses dan pemasangan



[Buka `https://app.silentium.dev/` dari browser Anda] (https://app.silentium.dev/). Aplikasi dimuat secara instan dan menampilkan layar beranda.



Untuk menginstalnya sebagai aplikasi bawaan di iOS, tekan tombol bagikan (kotak dengan panah ke atas) lalu pilih "Di layar beranda". Di Android, peramban biasanya menawarkan notifikasi "Tambahkan ke layar beranda" secara langsung. Setelah terinstal, Silentium akan muncul dengan ikon khusus dan berfungsi sebagai aplikasi bawaan, tetapi membutuhkan koneksi internet untuk menyinkronkan transaksi.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Pembuatan portofolio



Pada peluncuran pertama, pilih "Buat Wallet" untuk membuat portofolio baru generate, atau "Pulihkan Wallet" untuk memulihkan dari frasa pemulihan yang sudah ada.



Pilih "Buat Wallet". Aplikasi ini menghasilkan frasa 12 kata yang harus Anda tulis dengan hati-hati. Frasa ini adalah satu-satunya cara untuk memulihkan dana Anda. Bahkan di testnet, terapkan praktik pencadangan yang baik. Tekan "Lanjutkan" setelah menyimpan frasa Anda.



Aplikasi kemudian meminta Anda untuk menetapkan kata sandi untuk mengamankan akses ke wallet. Pilih kata sandi yang kuat dan konfirmasikan.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Setelah frasa dikonfirmasi dan kata sandi ditetapkan, Anda akan dibawa ke antarmuka utama.



### Interface utama dan parameter



Antarmuka utama menampilkan saldo Anda dalam satoshi (awalnya 0 sats), dengan tiga tombol di bagian bawah:




- Sinkronisasi **: menyinkronkan wallet dengan blockchain
- Terima**: untuk menerima dana
- Kirim**: untuk mengirim bitcoin



Akses Pengaturan melalui ikon di kanan atas (tiga bilah horizontal). Menu Pengaturan menawarkan beberapa opsi:





- Tentang**: informasi aplikasi
- Cadangan**: cadangan frasa pemulihan
- Penjelajah**: pilih penjelajah blockchain (Mempool secara default) dan server Silentiumd
- Jaringan**: pemilihan jaringan (mainnet/testnet)
- Kata sandi**: ubah kata sandi
- Reload**: memuat ulang wallet
- Atur ulang **: atur ulang lengkap
- Tema**: ubah tema



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Bagian **Explorer** sangat penting: bagian ini memungkinkan Anda untuk memilih penjelajah blockchain yang digunakan (Mempool secara default) dan juga menampilkan URL server Silentiumd (`https://bitcoin.silentium.dev/v1` untuk mainnet). Jika Anda meng-host server Silentiumd Anda sendiri atau ingin menggunakan testnet, di sinilah Anda mengonfigurasi parameter-parameter ini.



### Menerima dana



Dari antarmuka utama, tekan tombol "Terima". Secara default, Silentium menampilkan alamat Pembayaran Senyap dengan kode QR-nya. Alamat tersebut dimulai dengan `sp1...` pada mainnet atau `tsp1...` pada testnet.



Anda dapat beralih antara Pembayaran Senyap dan alamat Bitcoin klasik menggunakan tombol "Beralih ke alamat klasik" / "Beralih ke alamat senyap" di bagian bawah layar.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Setelah transaksi disiarkan, harap tunggu beberapa menit. Untuk Pembayaran Senyap, Silentium secara otomatis memindai blockchain untuk transaksi yang ditujukan untuk Anda. Transaksi akan muncul dengan status "Belum dikonfirmasi" sebelum akhirnya dikonfirmasi secara bertahap.



### Kirim pembayaran



Dari antarmuka utama, tekan tombol "Kirim". Layar kirim akan menanyakan kepada Anda :



1. **Address**: tempelkan alamat Pembayaran Senyap (`sp1... ` atau `tsp1... `) atau alamat Bitcoin klasik. Anda dapat menggunakan ikon pemindaian QR untuk memindai alamat.


2. **Jumlah**: masukkan jumlah dalam satoshi yang akan dikirim. Papan tombol numerik ditampilkan untuk memudahkan entri. Saldo yang tersedia ditampilkan di bagian atas untuk referensi.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Setelah Anda memasukkan alamat dan jumlah, tekan "Lanjutkan" untuk melanjutkan. Aplikasi akan meminta Anda untuk memilih tingkat biaya yang diinginkan sebelum mengonfirmasi transaksi.



## wallet hosting mandiri



### Mengapa menjadi tuan rumah sendiri?



Hosting lokal Silentium menawarkan kedaulatan penuh, verifikasi kode, lingkungan pengembangan, dan ketahanan dalam menghadapi kegagalan situs resmi.



### Prasyarat



Node.js (versi 14+), npm atau yarn, Git, dan ruang disk sekitar 500 MB.



### Instalasi lokal



Kloning repositori dan instal file :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Meluncurkan dan menggunakan



Mulai aplikasi dalam mode pengembangan:



```bash
yarn start
```



Buka `http://localhost:3000` di browser Anda. Untuk versi produksi yang dioptimalkan:



```bash
yarn build
```



File yang dihasilkan di `build/` dapat dilayani dengan nginx, Apache, atau server web apa pun. Secara default, Silentium terhubung ke server publik `bitcoin.silentium.dev`. Ubah pengaturan ini dalam parameter untuk menggunakan testnet atau server Anda sendiri.



## Server Silentiumd



### Peran dan operasi



Silentium menggunakan server pengindeksan **Silentiumd** untuk mengoptimalkan deteksi pembayaran. Memindai semua transaksi Taproot akan terlalu rumit untuk browser atau ponsel.



Silentiumd melakukan pra-kalkulasi data perantara (tweak) untuk setiap transaksi Taproot. wallet Anda mengunduh tweak ini (beberapa byte per transaksi) dan melakukan perhitungan akhir secara lokal, memverifikasi kepemilikan pembayaran. Server tidak pernah mengetahui kunci Anda atau dapat mengidentifikasi transaksi Anda, tidak seperti server Electrum konvensional.



Filter BIP158 yang ringkas memungkinkan wallet Anda menentukan blok mana yang akan dipindai tanpa mengungkapkan alamat Anda, sehingga menjaga kerahasiaan Anda.



### Server publik



Server publik `bitcoin.silentium.dev` (mainnet), yang disponsori oleh Vulpem Ventures, menawarkan pengalaman yang sederhana dan langsung. Meskipun kerahasiaan terjaga, pendekatan ini menyiratkan kepercayaan relatif pada infrastruktur pihak ketiga.



### Hosting server Silentiumd Anda sendiri



Untuk kedaulatan penuh, host server Silentiumd Anda sendiri. Prasyarat: Bitcoin Core non-elagged node dengan `txindex=1` dan `blockfilterindex=1`, Go 1.21+, ruang disk 10-20 GB, keterampilan administrasi sistem.



**Instalasi:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfigurasikan melalui variabel lingkungan (lihat `config.md` repositori untuk detailnya). Server mengindeks blockchain dan mengekspos API yang dapat ditanyakan oleh wallet Anda.



Saat ini tidak ada solusi paket untuk Umbrel atau Start9, sehingga membatasi aksesibilitas bagi pengguna non-teknis.



## Keuntungan dan keterbatasan



### Sorotan





- Aksesibilitas maksimum**: gunakan dari browser apa pun, tidak perlu instalasi yang berat
- Multi-platform**: berfungsi di ponsel (Android/iOS) dan desktop berkat teknologi PWA
- Hosting mandiri sederhana**: instalasi lokal dapat dilakukan dengan beberapa perintah
- Sumber terbuka**: kode yang dapat diaudit sepenuhnya di GitHub
- Berfokus pada privasi**: tidak ada pelacakan, tidak ada analisis, perhitungan kriptografi lokal
- Arsitektur terpisah**: pemisahan yang jelas antara wallet (klien) dan server pengindeksan
- Tanpa akun**: tidak perlu registrasi atau data pribadi



### Kendala yang perlu dipertimbangkan





- Proyek eksperimental**: bukti konsep saja, tidak dimaksudkan untuk penggunaan sehari-hari atau produksi
- Tidak ada jaminan**: risiko bug, kerentanan, kemungkinan kehilangan dana
- Dukungan terbatas**: sedikit dokumentasi pengguna, komunitas kecil, tidak ada dukungan resmi
- Ketergantungan server**: membutuhkan server Silentiumd yang berfungsi (publik atau host sendiri)
- Pemindaian intensif**: Deteksi Pembayaran Senyap menghabiskan bandwidth
- Fungsionalitas yang berkurang**: tidak ada kontrol koin, tidak ada Lightning, tidak ada multi-tanda tangan



## Praktik terbaik



### Keamanan seed



Bahkan di testnet, perlakukan frasa pemulihan Anda dengan serius. Tuliskan dan simpan di tempat yang aman. Simpan dompet terpisah untuk testnet dan mainnet: jangan pernah menggunakan test seed pada wallet yang ditujukan untuk dana sungguhan.



### Verifikasi kode sumber



Salah satu keuntungan dari hosting mandiri adalah kemampuan untuk memeriksa kode sumber sebelum menjalankannya. Jika Anda berencana untuk menggunakan Silentium dengan dana sungguhan, luangkan waktu untuk mengaudit kode atau meminta pengembang tepercaya untuk melakukannya. Juga bandingkan hash kode yang digunakan pada `app.silentium.dev` dengan yang ada di repositori GitHub untuk memastikan keasliannya.



### Pencadangan dan pemulihan



Pemulihan dana Silent Payments membutuhkan wallet yang kompatibel dengan protokol BIP-352. wallet standar tidak dapat memindai blockchain untuk mengambil Silent Payments UTXO Anda. Tetap pasang Silentium atau pastikan Anda memiliki akses ke wallet lain yang kompatibel (seperti Cake Wallet atau implementasi lain di masa mendatang) untuk memulihkan dana Anda jika perlu.



## Kesimpulan



Silentium menyediakan tempat pengujian yang dapat diakses untuk memahami Pembayaran Senyap tanpa gesekan teknis. Sebagai bukti konsep, ini menunjukkan bagaimana teknologi privasi ini dapat diintegrasikan ke dalam peramban wallet sambil menjaga keamanannya. Bereksperimenlah di testnet untuk menemukan terobosan yang menjanjikan untuk privasi on-chain ini.



## Sumber daya



### Dokumentasi resmi




- Repositori Silentium GitHub (wallet): https://github.com/louisinger/silentium
- Repositori Silentiumd GitHub (server): https://github.com/louisinger/silentiumd
- Aplikasi web: https://app.silentium.dev/
- Situs komunitas Silent Payments: https://silentpayments.xyz
- Spesifikasi BIP-352: https://bips.dev/352



### Artikel dan sumber daya




- Pengumuman resmi (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Pembayaran Senyap: https://bitcoinops.org/en/topics/silent-payments/



### Alat Testnet




- Keran Testnet: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet