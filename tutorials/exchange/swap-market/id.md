---
name: SwapMarket
description: Pengumpul layanan Bitcoin dan Lightning swap
---

![cover](assets/cover.webp)



Mentransfer dana antara Bitcoin on-chain dan Lightning Network pada umumnya membutuhkan pembukaan saluran Lightning secara manual (teknis dan mahal), atau penggunaan platform swap terpusat dengan KYC. SwapMarket menawarkan alternatif: swap atom tanpa kepercayaan melalui penyedia yang kompetitif, tanpa KYC.



Inovasi: meskipun penyedia adalah perantara, HTLC (*Hash Time Locked Contracts*) secara matematis menjamin bahwa dana Anda tetap berada di bawah kendali Anda. Agregasi dari beberapa penyedia (Boltz, ZEUS Swaps, Eldamar, Middle Way) menciptakan persaingan harga. Interface web open-source yang dapat dihosting sendiri.



## Apa itu SwapMarket?



Agregator sumber terbuka yang diluncurkan pada tahun 2024, SwapMarket berfungsi sebagai pembanding penyedia swap Bitcoin/Lightning. Pengguna dapat langsung membandingkan kondisi (biaya, likuiditas, limit) dan memilih penyedia yang optimal.



### Arsitektur teknis



**Menghadapi sisi klien**: 100% aplikasi sisi klien (Aplikasi Web fork Boltz) dihosting di Halaman GitHub. Kode berjalan di browser tanpa server backend. Riwayat disimpan secara lokal (cookie/cache). Kode sumber publik dan dapat diaudit.



**Penemuan penyedia** : Daftar yang dikodekan dalam `src/configs/mainnet.ts`. Penyedia baru ditambahkan melalui Pull Request atau email.



**Backend independen**: Setiap penyedia mengoperasikan backend Boltz sendiri. Antarmuka meminta API secara real time untuk membandingkan harga secara instan.



**HTLC Swap Atom**: Hash Kontrak Terkunci Waktu menjamin keatomisan: baik swap dieksekusi, atau masing-masing pihak mendapatkan kembali dananya. Risiko pihak lawan dieliminasi secara matematis.



### Filosofi



SwapMarket mengurangi sentralisasi dengan menciptakan persaingan antar penyedia untuk biaya dan likuiditas. Tanpa KYC, kode sumber terbuka yang dapat dihosting sendiri, penggandaan operator independen untuk menghindari satu titik kegagalan.



## Fitur utama



### Pasar Penyedia



Antarmuka menampilkan semua penyedia yang aktif: nama penyedia, biaya yang diterapkan (persentase dan/atau tetap), jumlah minimum/maksimum yang tersedia, dan jenis swap yang didukung. Aplikasi ini secara langsung menanyakan API dari setiap penyedia yang dirujuk dalam file konfigurasi untuk mendapatkan kuotasi secara real time. Persaingan antar penyedia menjamin harga yang optimal, umumnya sekitar 0,5% untuk swap standar.



### Pertukaran dua arah



**Swap-in (on-chain → Lightning)**: Mengonversi on-chain BTC menjadi satoshi Lightning. Kasus penggunaan: memberi daya pada wallet Lightning seluler, mendapatkan kapasitas masuk pada node, atau memiliki likuiditas instan.



**Tukar tambah (Lightning → on-chain)**: Mengonversi satoshi Lightning ke on-chain BTC. Kasus penggunaan: mengosongkan wallet Lightning ke penyimpanan dingin atau menyeimbangkan kembali likuiditas antar lapisan.



### Keselamatan dan pemulihan



*pertukaran atomik *Trustless**: HTLC menjamin bahwa pertukaran diselesaikan secara penuh, atau masing-masing pihak mendapatkan kembali sahamnya. Risiko mitra pengimbang dieliminasi secara matematis.



**Mekanisme pembayaran kembali**: Setiap swap memiliki penguncian waktu. Jika swap gagal, dana secara otomatis dapat dikembalikan setelah masa berlaku habis. Pengguna selalu memiliki opsi untuk mendapatkan kembali bitcoinnya.



**Kunci pemulihan**: SwapMarket memungkinkan Anda mengekspor kunci pemulihan untuk swap yang sedang berlangsung. Jika terjadi masalah, kunci-kunci ini dapat digunakan untuk menyelesaikan atau membatalkan swap dari perangkat apa pun.



## Instalasi dan akses



### Web Interface



SwapMarket tidak memerlukan instalasi. Akses melalui peramban dengan mengunjungi https://swapmarket.github.io. Untuk kerahasiaan maksimum, gunakan Brave, Firefox dengan ekstensi anti-pelacakan, atau LibreWolf. Tor Browser direkomendasikan untuk anonimitas jaringan.



Tidak perlu registrasi, email, atau verifikasi identitas.



### Hosting mandiri (opsional)



Untuk pengguna teknis yang ingin menghilangkan ketergantungan pada domain Halaman GitHub resmi, SwapMarket dapat dijalankan secara lokal:



**Melalui npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Melalui Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Aplikasi ini dapat diakses di `http://localhost:3000`. Self-hosting menjamin kontrol penuh atas antarmuka, menghilangkan risiko penyensoran domain resmi, dan memungkinkan kode sumber untuk diaudit sebelum dieksekusi.



### Konfigurasi awal



**Wallet Lightning**: Pastikan Anda memiliki wallet Lightning yang operasional (Phoenix, Zeus, BlueWallet, dll.). Untuk swap-in, Anda akan mendapatkan faktur Lightning generate. Untuk swap-out, Anda akan membayar faktur Lightning.



**Wallet on-chain**: Untuk swap-in, Anda memerlukan wallet Bitcoin on-chain untuk mengirim dana. Untuk swap-out, siapkan alamat penerima Bitcoin.



**Konfigurasi opsional**: SwapMarket menyimpan riwayat dan preferensi swap dalam cookie browser. Tidak diperlukan pembuatan akun.



## Akses ke pengaturan dan Tombol Penyelamatan



Sebelum melakukan swap pertama Anda, kami sangat menyarankan agar Anda mengunduh **Kunci Penyelamatan**. Kunci darurat ini memungkinkan Anda untuk memulihkan dana Anda jika terjadi masalah teknis atau kehilangan akses ke perangkat Anda.



### Parameter akses



Dari halaman utama SwapMarket, klik ikon roda gigi (⚙️) di bagian kanan atas antarmuka, di sebelah formulir swap.



![Accès aux paramètres](assets/fr/01.webp)



### Pengaturan Halaman



Halaman Pengaturan terbuka, menampilkan beberapa opsi konfigurasi:





- Denominasi**: Pilihan BTC atau sats
- Pemisah Desimal**: Pemisah desimal (, atau .)
- Pemberitahuan Audio/Peramban**: Pemberitahuan audio dan browser
- Kunci Penyelamatan** : Unduh kunci pemulihan
- Log**: Melihat, mengunduh, atau menghapus log



![Page Settings](assets/fr/02.webp)



### Unduh Kunci Penyelamatan



Klik tombol **Unduh** di sebelah "Kunci Penyelamatan".



**Poin penting**:




- Kunci Penyelamatan adalah **kunci darurat satu atap** yang berfungsi untuk semua pertukaran Anda di masa mendatang
- Simpan kunci ini di tempat yang **aman dan permanen** (pengelola kata sandi, brankas digital)
- Jika terjadi masalah swap (waktu habis, kegagalan teknis), kunci ini memungkinkan Anda untuk memulihkan dana Anda



## Membuat swap langkah demi langkah



### Tukar keluar: Petir → Bitcoin



Contoh pertama ini menunjukkan cara mengonversi satoshi Lightning menjadi bitcoin on-chain.



**Langkah 1: Konfigurasi pertukaran



Dari halaman utama, pilih formulir pertukaran :




- PETIR** (kolom atas): Masukkan jumlah yang ingin Anda kirimkan dalam sats Lightning (contoh: 30.000 sats)
- BITCOIN** (kolom bawah): Jumlah yang akan Anda terima secara otomatis ditampilkan setelah biaya dipotong (contoh: 29.320 sats)



Di kolom bawah, tempelkan **alamat penerima Bitcoin** di mana Anda ingin menerima dana. Periksa alamat ini dengan cermat.



Penyedia default biasanya Boltz Exchange. Biaya jaringan dan biaya penyedia ditampilkan dengan jelas.



![Configuration swap-out](assets/fr/03.webp)



**Langkah 2: Pemilihan penyedia layanan**



Klik pada menu drop-down penyedia (default: "Boltz Exchange") untuk menampilkan semua penyedia likuiditas yang tersedia.



Jendela modal terbuka, menampilkan tabel perbandingan:




- Status**: Indikator Green jika penyedia aktif
- Alias**: Nama penyedia (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Biaya**: Biaya yang dikenakan oleh penyedia layanan (umumnya antara 0,49% dan 0,5%)
- Max Swap**: Jumlah maksimum yang diterima untuk swap



Bandingkan biaya dan jumlah maksimum, lalu pilih penyedia pilihan Anda.



**Harap diperhatikan**: Antarmuka pemilihan penyedia tidak menampilkan **jumlah minimum** untuk setiap penyedia. Informasi ini hanya muncul di antarmuka pembuatan swap, setelah penyedia dipilih. Jumlah minimum dan maksimum dapat bervariasi dari satu penyedia ke penyedia lainnya, dan dapat berubah dari waktu ke waktu. **Selalu periksa batasan ini pada saat Anda melakukan swap**: jika jumlah yang ingin Anda swap berada di luar batasan penyedia, Anda dapat memilih penyedia lain yang lebih sesuai untuk transaksi Anda.



![Sélection du provider](assets/fr/04.webp)



**Langkah 3: Pembuatan swap dan pembayaran Lightning**



Klik pada tombol **"CREATE ATOMIC SWAP "** berwarna kuning. SwapMarket akan membuatkan faktur **Lightning** (BOLT11) untuk Anda bayarkan dari wallet Lightning Anda.



Halaman menampilkan :




- ID Swap**: Pengidentifikasi swap unik (contoh: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap dibuat, menunggu pembayaran)
- Kode QR**: Pindai dengan wallet Lightning Anda
- Invoice Petir**: String karakter yang dimulai dengan "lnbc" (contoh: lnbc300u1p50whiv... gn5dk2szgqkvfkzc)



Bayar tagihan ini dari wallet Lightning Anda (Phoenix, Zeus, BlueWallet, dll.). Jumlah pasti yang harus dibayar akan ditampilkan (contoh: 30.000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Langkah 4: Konfirmasi dan penerimaan**



Setelah pembayaran Lightning dikonfirmasi, SwapMarket langsung menerima pembayaran Anda dan penyedia menyiarkan transaksi Bitcoin ke alamat Anda.



Status berubah menjadi **"invoice.settled "** (faktur telah dibayar), dan pesan konfirmasi ditampilkan.



Bitcoin on-chain Anda akan tersedia segera setelah transaksi dikonfirmasi (biasanya beberapa menit hingga beberapa jam, tergantung pada biaya mining yang dipilih oleh penyedia).



![Confirmation swap-out](assets/fr/06.webp)



Anda dapat mengklik **"OPEN CLAIM TRANSACTION "** untuk melihat transaksi Bitcoin pada browser blockchain.



### Swap-in: Bitcoin → Petir



Contoh kedua ini menunjukkan cara mengonversi bitcoin on-chain menjadi satoshi Lightning.



**Langkah 1: Konfigurasi pertukaran



Dari halaman utama, pilih formulir pertukaran :




- BITCOIN** (kolom atas): Masukkan jumlah yang ingin Anda kirimkan dalam sats Bitcoin (contoh: 63.400 sats)
- PETIR** (kolom paling bawah): Jumlah yang akan Anda terima secara otomatis ditampilkan setelah dikurangi biaya (contoh: 62.884 sats)



Di kolom bawah, tempelkan faktur Lightning** (BOLT11) yang dihasilkan dari wallet Lightning Anda, atau gunakan alamat LNURL jika wallet Anda mendukungnya.



![Configuration swap-in](assets/fr/07.webp)



**Langkah 2: Pemeriksaan Kunci Penyelamatan**



Setelah mengklik **"CREATE ATOMIC SWAP "**, sebuah jendela modal akan muncul, meminta Anda untuk memverifikasi Kunci Penyelamatan Anda.



![Modal Rescue Key](assets/fr/08.webp)



**Kunci Penyelamatan Boltz**: Karena Anda telah mengunggah kunci pemulihan selama konfigurasi awal (lihat bagian sebelumnya), klik tombol **"VERIFIKASI KUNCI YANG ADA "** untuk mengimpor kunci yang telah Anda simpan.



Pilih file Kunci Penyelamatan yang telah diunduh sebelumnya. Setelah verifikasi berhasil, antarmuka secara otomatis beralih ke langkah berikutnya.



**Langkah 3: Alamat setoran Bitcoin**



SwapMarket sekarang menghasilkan **alamat Bitcoin unik** yang berisi kontrak HTLC yang ditautkan ke faktur Lightning Anda.



Halaman menampilkan :




- ID Penukaran**: Pengenal unik (contoh: 1kGmB6JyGqU4)
- Status**: "invoice.set" (set faktur, menunggu pembayaran Bitcoin)
- Kode QR**: Alamat depot Bitcoin
- Alamat Bitcoin**: Biasanya dimulai dengan "bc1p..." (contoh: bc1p5mvtwxapjkds... 9d4n9f)
- Peringatan berwarna kuning**: "Pastikan transaksi Anda terkonfirmasi dalam waktu ~24 jam setelah pembuatan swap ini!"



Periode ~24 jam ini adalah **waktu habis** kontrak HTLC. Jika transaksi Bitcoin Anda tidak dikonfirmasi dalam jangka waktu ini, swap akan gagal dan Anda harus menggunakan Kunci Penyelamatan untuk memulihkan dana Anda.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Anda dapat menyalin alamat dengan mengklik tombol **"ALAMAT "**, atau memindai kode QR langsung dari wallet on-chain Anda.



**Langkah 4: Mengirim bitcoin**



Dari wallet Bitcoin on-chain Anda, kirimkan **jumlah yang tertera (mis. 63.400 sats) ke alamat yang dihasilkan.



**Penting**: Gunakan biaya mining yang sesuai untuk menjamin konfirmasi yang cepat. Jika biaya terlalu rendah dan transaksi tetap berada di mempool setelah batas waktu (~24 jam), swap akan gagal.



Setelah transaksi dikirim, SwapMarket mendeteksi bahwa transaksi tersebut ada di mempool dan menampilkan :




- Status** : "transaksi.mempool
- Pesan**: "Transaksi ada di mempool - Menunggu konfirmasi untuk menyelesaikan swap"



![Transaction en mempool](assets/fr/10.webp)



**Langkah 5: Konfirmasi dan Penerimaan Kilat**



Segera setelah transaksi Bitcoin menerima konfirmasi pertama, penyedia layanan secara otomatis membayar faktur Lightning Anda. Anda langsung menerima satoshi pada wallet Lightning Anda.



Status berubah menjadi **"transaction.claim.pending "**, kemudian pesan konfirmasi ditampilkan:



![Confirmation swap-in](assets/fr/11.webp)



Satoshi Lightning Anda segera tersedia di wallet Anda.



## Keuntungan dan keterbatasan



### Manfaat



**Persaingan tarif**: Agregasi penyedia layanan menciptakan persaingan alami yang menurunkan biaya (0,49% hingga 0,5%).



**Kerahasiaan**: Tanpa KYC, 100% antarmuka sisi klien (tidak ada transmisi data pribadi), kompatibel dengan Tor Browser.



**Non-kustodian**: HTLC secara matematis menjamin kontrol eksklusif atas dana Anda. Baik swap berhasil, atau Anda mendapatkan bitcoin Anda kembali.



**Sumber terbuka yang dapat dihosting sendiri**: kode publik yang dapat diaudit, dapat digunakan secara lokal untuk ketahanan maksimum terhadap sensor.



### Keterbatasan



**Likuiditas terbatas**: Jumlah penyedia aktif terbatas (Boltz, Eldamar, MiddleWay tergantung periode). Jumlah maksimum mungkin terbatas.



**Waktu kedaluwarsa**: Batas waktu dari 24 jam hingga 48 jam. Jika transaksi on-chain tidak dikonfirmasi sebelum masa berlaku habis, diperlukan pemulihan secara manual.



**Sentralisasi Interface**: Meskipun dapat dihosting sendiri, antarmuka resminya dihosting di Halaman GitHub. Jika GitHub menyensor repo, akses melalui swapmarket.github.io akan diblokir (solusi: hosting mandiri).



**Jejak on-chain**: Skrip HTLC berpotensi dapat diidentifikasi dengan analisis blockchain tingkat lanjut.



## Praktik terbaik



### Konfigurasi yang aman



**Unduh Kunci Penyelamatan Anda**: Sebelum melakukan swap pertama Anda, unduh Kunci Penyelamatan Anda dari Pengaturan (lihat bagian khusus di atas). Kunci unik ini akan berfungsi untuk semua swap Anda di masa mendatang, sehingga Anda dapat memulihkan dana jika terjadi masalah.



**Gunakan Tor Browser**: Untuk kerahasiaan maksimum, akses SwapMarket melalui Tor Browser untuk menyembunyikan alamat IP Anda.



**Pertimbangkan untuk melakukan hosting sendiri**: Untuk pengguna teknis, menjalankan instans SwapMarket Anda sendiri akan menghilangkan ketergantungan pada domain Halaman GitHub resmi.



### Pengoptimalan pertukaran



**Perhatikan mempool**: Periksa mempool.space sebelum melakukan swap-in. Pilih waktu dengan aktivitas rendah untuk meminimalkan biaya mining.



**Periksa alamat**: Untuk pertukaran, periksa dengan cermat alamat penerima Anda. Gunakan salin dan tempel dan periksa 5 karakter pertama dan 5 karakter terakhir.



**Uji dengan jumlah kecil**: Mulailah dengan jumlah minimum yang diizinkan (25.000 hingga 50.000 sats). Tingkatkan secara bertahap setelah Anda menguasai prosesnya.



**Dokumentasikan swap Anda**: Catat ID, alamat penukaran, dan tanggal kedaluwarsa setiap swap. Informasi ini memudahkan pelacakan dan pemulihan jika terjadi masalah teknis.



### Strategi penggunaan



**Menyeimbangkan arus kas Anda**: Gunakan SwapMarket untuk menyesuaikan alokasi Anda antara on-chain (tabungan, keamanan jangka panjang) dan Lightning (pengeluaran harian, pembayaran instan) sesuai dengan kebutuhan Anda yang sebenarnya.



**Hitung profitabilitas**: Untuk kebutuhan likuiditas Lightning permanen, bandingkan biaya kumulatif swap berulang versus membuka saluran Lightning secara langsung. SwapMarket unggul untuk penyesuaian satu kali, tidak harus untuk aliran reguler yang besar.



## SwapMarket vs Boltz: Apa perbedaannya?



### Boltz: Teknologi vs Layanan



**Boltz adalah teknologi sumber terbuka** (`boltz-backend` di GitHub) yang mengimplementasikan pertukaran atom melalui HTLC antara Bitcoin, Lightning, dan Liquid.



**Poin penting**: Semua penyedia SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) menggunakan contoh backend Boltz mereka sendiri. Oleh karena itu, teknologi yang mendasarinya identik. Kerentanan pada backend Boltz berpotensi mempengaruhi semua penyedia, tetapi sifat open-source dari sistem ini memungkinkan audit oleh komunitas.



**Boltz Exchange** adalah layanan tunggal yang dioperasikan oleh tim Boltz, sementara **SwapMarket** menyatukan beberapa penyedia yang semuanya menggunakan teknologi Boltz, menciptakan lingkungan harga yang kompetitif.



Lihat tutorial Boltz dan Zeus Swap kami untuk lebih jelasnya:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Perbedaan utama



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

*manfaat *SwapMarket**: Persaingan harga, diversifikasi instance backend, perbandingan waktu nyata.



**Alternatif teknologi** (tidak kompatibel dengan SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Solusi-solusi ini menggunakan implementasi submarine swap mereka sendiri.



**Rekomendasi**: Gunakan Boltz Exchange untuk kesederhanaan atau SwapMarket untuk mengoptimalkan biaya melalui kompetisi. Keduanya memiliki keamanan yang setara (HTLC non-kustodian).



## Kesimpulan



SwapMarket memfasilitasi pertukaran Bitcoin/Lightning dengan menggabungkan beberapa penyedia ke dalam satu antarmuka. Arsitektur HTLC menjamin sifat non-kustodian dari pertukaran, ketiadaan KYC menjaga kerahasiaan, dan kode sumber terbuka yang dapat dihosting sendiri memperkuat ketahanan terhadap sensor.



Persaingan antar penyedia layanan meningkatkan harga dan melipatgandakan sumber likuiditas. Untuk mengoptimalkan manajemen dua lapis (penghematan on-chain, biaya Lightning), SwapMarket adalah alat praktis yang menjaga kedaulatan dan kerahasiaan keuangan.



## Sumber daya



### Dokumentasi resmi




- [SwapMarket - Aplikasi web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Dokumentasi teknis](https://docs.boltz.exchange/)
- [Panduan hosting mandiri](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Proyek-proyek terkait




- [Boltz Exchange] (https://boltz.exchange) - Layanan pertukaran atom asli
- [ZEUS Swaps] (https://zeusln.com) - Penyedia pertukaran kilat