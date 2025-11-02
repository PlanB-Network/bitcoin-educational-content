---
name: SwapMarket
description: Pengumpul layanan Bitcoin dan Lightning swap
---

![cover](assets/cover.webp)



Mentransfer dana antara Bitcoin On-Chain dan Lightning Network pada umumnya membutuhkan pembukaan saluran Lightning secara manual (teknis dan mahal), atau penggunaan platform swap terpusat dengan KYC. SwapMarket menawarkan sebuah alternatif: Swap atom Trustless melalui penyedia yang kompetitif, tanpa KYC.



Inovasi: meskipun penyedia adalah perantara, HTLC (*Hash Time Locked Contracts*) secara matematis menjamin bahwa dana Anda tetap berada di bawah kendali Anda. Agregasi dari beberapa penyedia (Boltz, ZEUS Swaps, Eldamar, Middle Way) menciptakan persaingan harga. Interface web open-source yang dapat dihosting sendiri.



## Apa itu SwapMarket?



Agregator sumber terbuka yang diluncurkan pada tahun 2024, SwapMarket berfungsi sebagai pembanding penyedia swap Bitcoin/Lightning. Pengguna dapat langsung membandingkan kondisi (biaya, likuiditas, limit) dan memilih penyedia yang optimal.



### Arsitektur teknis



**Menghadapi sisi klien**: 100% aplikasi sisi klien (Fork Boltz Web App) yang dihosting di Halaman GitHub. Kode berjalan di browser tanpa server backend. Riwayat disimpan secara lokal (cookie/cache). Kode sumber publik dan dapat diaudit.



**Penemuan penyedia** : Daftar kode Hard di `src/configs/Mainnet.ts`. Penyedia baru ditambahkan melalui Pull Request atau email.



**Backend independen**: Setiap penyedia mengoperasikan backend Boltz-nya sendiri. Interface menanyakan API secara real time untuk membandingkan harga secara instan.



**HTLC Swap Atom**: Hash Kontrak Terkunci Waktu menjamin keatomisan: baik swap dieksekusi, atau masing-masing pihak mendapatkan kembali dananya. Risiko pihak lawan dieliminasi secara matematis.



### Filosofi



SwapMarket mengurangi sentralisasi dengan menciptakan kompetisi antara penyedia untuk biaya dan likuiditas. Tanpa KYC, kode sumber terbuka yang dapat dihosting sendiri, penggandaan operator independen untuk menghindari satu titik kegagalan.



## Fitur utama



### Pasar Penyedia



Interface menampilkan semua penyedia yang aktif: nama penyedia, biaya yang diterapkan (persentase dan/atau tetap), jumlah minimum/maksimum yang tersedia, dan jenis swap yang didukung. Aplikasi ini secara langsung menanyakan API dari setiap penyedia yang dirujuk dalam file konfigurasi untuk mendapatkan kuotasi secara real time. Persaingan antar penyedia menjamin harga yang optimal, umumnya sekitar 0,5% untuk swap standar.



### Pertukaran dua arah



**Swap-in (On-Chain → Lightning)**: Mengonversi On-Chain BTC menjadi satoshi Lightning. Kasus penggunaan: memberi daya pada Wallet Lightning seluler, mendapatkan kapasitas masuk pada node, atau memiliki likuiditas instan.



**Penukaran (Lightning → On-Chain)**: Mengubah satoshi Lightning menjadi On-Chain BTC. Kasus penggunaan: membuang Lightning Wallet ke penyimpanan Cold atau menyeimbangkan kembali likuiditas antar lapisan.



### Keselamatan dan pemulihan



**Trustless Pertukaran Atom: HTLC menjamin bahwa Exchange diselesaikan secara penuh, atau masing-masing pihak mendapatkan kembali sahamnya. Risiko pihak lawan dihilangkan secara matematis.



**Mekanisme penukaran**: Setiap swap memiliki tanggal kedaluwarsa (TIMELOCK). Jika swap gagal, dana secara otomatis dapat dikembalikan setelah kedaluwarsa. Pengguna selalu memiliki opsi untuk mendapatkan kembali bitcoinnya.



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



Aplikasi ini dapat diakses di `http://localhost:3000`. Self-hosting menjamin kontrol penuh atas Interface, menghilangkan risiko penyensoran domain resmi, dan memungkinkan kode sumber untuk diaudit sebelum dieksekusi.



### Konfigurasi awal



**Wallet Lightning**: Pastikan Anda memiliki Wallet Lightning yang beroperasi (Phoenix, Zeus, BlueWallet, dll.). Untuk swap-in, Anda akan menukar generate dengan Lightning Invoice. Untuk swap-out, Anda akan membayar Lightning Invoice.



**Wallet On-Chain**: Untuk swap-in, Anda memerlukan Wallet Bitcoin On-Chain untuk mengirim dana. Untuk swap-out, siapkan Bitcoin yang menerima Address.



**Konfigurasi opsional**: SwapMarket menyimpan riwayat dan preferensi swap dalam cookie browser. Tidak diperlukan pembuatan akun.



## Akses ke pengaturan dan Tombol Penyelamatan



Sebelum melakukan swap pertama Anda, kami sangat menyarankan agar Anda mengunduh **Kunci Penyelamatan**. Kunci darurat ini memungkinkan Anda untuk memulihkan dana Anda jika terjadi masalah teknis atau kehilangan akses ke perangkat Anda.



### Parameter akses



Dari halaman utama SwapMarket, klik ikon roda gigi (⚙️) di kanan atas Interface, di sebelah formulir swap.



![Accès aux paramètres](assets/fr/01.webp)



### Pengaturan Halaman



Halaman Pengaturan terbuka, menampilkan beberapa opsi konfigurasi:





- Denominasi**: Pilihan antara BTC atau Sats
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



Contoh pertama ini menunjukkan cara mengonversi satoshi Lightning menjadi bitcoin On-Chain.



**Langkah 1: Konfigurasi pertukaran



Dari halaman utama, pilih formulir pertukaran :




- PETIR** (kolom atas): Masukkan jumlah yang ingin Anda kirimkan dalam Sats Lightning (contoh: 30.000 Sats)
- Bitcoin** (kolom bawah): Jumlah yang akan Anda terima secara otomatis ditampilkan setelah biaya dipotong (contoh: Sats 29.320)



Di kolom bawah, tempelkan **penerimaan Bitcoin Address** di tempat Anda ingin menerima dana. Periksa Address ini dengan cermat.



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



**Harap diperhatikan**: Pemilihan penyedia Interface tidak menampilkan **jumlah minimum** untuk setiap penyedia. Informasi ini hanya muncul dalam pembuatan swap Interface, setelah penyedia dipilih. Jumlah minimum dan maksimum dapat bervariasi dari satu penyedia ke penyedia lainnya, dan dapat berubah dari waktu ke waktu. **Selalu periksa batasan ini pada saat Anda melakukan swap**: jika jumlah yang ingin Anda swap berada di luar batasan penyedia, Anda dapat memilih penyedia lain yang lebih sesuai untuk transaksi Anda.



![Sélection du provider](assets/fr/04.webp)



**Langkah 3: Pembuatan swap dan pembayaran Lightning**



Klik pada tombol **"CREATE ATOMIC SWAP "** berwarna kuning. SwapMarket akan menukarkan generate dengan **Lightning Invoice** (BOLT11) untuk Anda bayarkan dari Lightning Wallet Anda.



Halaman menampilkan :




- ID Swap**: Pengidentifikasi swap unik (contoh: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap dibuat, menunggu pembayaran)
- Kode QR**: Pindai dengan Wallet Lightning Anda
- Invoice Petir**: String karakter yang dimulai dengan "lnbc" (contoh: lnbc300u1p50whiv... gn5dk2szgqkvfkzc)



Bayar Invoice ini dari Wallet Lightning Anda (Phoenix, Zeus, BlueWallet, dll.). Jumlah pasti yang harus dibayarkan akan ditampilkan (contoh: 30.000 Sats).



![Paiement Lightning](assets/fr/05.webp)



**Langkah 4: Konfirmasi dan penerimaan**



Setelah pembayaran Lightning dikonfirmasi, SwapMarket langsung menerima pembayaran Anda dan penyedia menyiarkan transaksi Bitcoin ke Address Anda.



Status berubah menjadi **"Invoice.settled "** (Invoice dibayar), dan pesan konfirmasi muncul.



Bitcoin On-Chain Anda akan tersedia segera setelah transaksi dikonfirmasi (biasanya dalam beberapa menit hingga beberapa jam, tergantung pada biaya Mining yang dipilih oleh penyedia).



![Confirmation swap-out](assets/fr/06.webp)



Anda dapat mengklik **"OPEN CLAIM TRANSACTION "** untuk melihat transaksi Bitcoin pada Blockchain explorer.



### Swap-in: Bitcoin → Petir



Contoh kedua ini menunjukkan bagaimana cara mengonversi bitcoin On-Chain menjadi satoshi Lightning.



**Langkah 1: Konfigurasi pertukaran



Dari halaman utama, pilih formulir pertukaran :




- Bitcoin** (kolom atas): Masukkan jumlah yang ingin Anda kirimkan dalam Sats Bitcoin (contoh: 63.400 Sats)
- PETIR** (kolom paling bawah): Jumlah yang akan Anda terima secara otomatis ditampilkan setelah dikurangi biaya (contoh: 62.884 Sats)



Di bidang bawah, tempelkan Lightning** Invoice (BOLT11) yang dihasilkan dari Lightning Wallet Anda, atau gunakan LNURL Address jika Wallet Anda mendukungnya.



![Configuration swap-in](assets/fr/07.webp)



**Langkah 2: Pemeriksaan Kunci Penyelamatan**



Setelah mengklik **"CREATE ATOMIC SWAP "**, sebuah jendela modal akan muncul, meminta Anda untuk memverifikasi Kunci Penyelamatan Anda.



![Modal Rescue Key](assets/fr/08.webp)



**Kunci Penyelamatan Boltz**: Karena Anda telah mengunggah kunci pemulihan selama konfigurasi awal (lihat bagian sebelumnya), klik tombol **"VERIFIKASI KUNCI YANG ADA "** untuk mengimpor kunci yang telah Anda simpan.



Pilih file Kunci Penyelamatan yang telah diunduh sebelumnya. Setelah verifikasi berhasil, Interface secara otomatis beralih ke langkah berikutnya.



**Langkah 3: Bitcoin** setor Address



SwapMarket kini menghasilkan **Bitcoin Address yang unik** yang berisi HTLC Contract yang terhubung ke Lightning Invoice Anda.



Halaman menampilkan :




- ID Penukaran**: Pengenal unik (contoh: 1kGmB6JyGqU4)
- Status** : "Invoice.set" (Invoice set, menunggu pembayaran Bitcoin)
- Kode QR**: Depot Bitcoin Address
- Bitcoin** Address: Biasanya dimulai dengan "bc1p..." (contoh: bc1p5mvtwxapjkds... 9d4n9f)
- Peringatan berwarna kuning**: "Pastikan transaksi Anda terkonfirmasi dalam waktu ~24 jam setelah pembuatan swap ini!"



Periode ~24 jam ini adalah **waktu habis** dari HTLC Contract. Jika transaksi Bitcoin Anda tidak dikonfirmasi dalam jangka waktu ini, swap akan gagal dan Anda harus menggunakan Kunci Penyelamatan untuk memulihkan dana Anda.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Anda dapat menyalin Address dengan mengklik tombol **"Address"**, atau memindai kode QR langsung dari Wallet On-Chain Anda.



**Langkah 4: Mengirim bitcoin**



Dari Wallet Bitcoin On-Chain Anda, kirimkan **jumlah yang ditunjukkan (mis. 63.400 Sats) ke Address yang dihasilkan.



**Penting**: Gunakan biaya Mining yang sesuai untuk menjamin konfirmasi yang cepat. Jika biaya terlalu rendah dan transaksi tetap berada di Mempool setelah batas waktu (~24 jam), swap akan gagal.



Setelah transaksi dikirim, SwapMarket mendeteksi bahwa transaksi tersebut ada di Mempool dan menampilkan :




- Status** : "transaksi.Mempool"
- Pesan**: "Transaksi dalam Mempool - Menunggu konfirmasi untuk menyelesaikan swap"



![Transaction en mempool](assets/fr/10.webp)



**Langkah 5: Konfirmasi dan Penerimaan Kilat**



Segera setelah transaksi Bitcoin menerima konfirmasi pertama, penyedia layanan secara otomatis membayar Lightning Invoice Anda. Anda langsung menerima satoshi pada Lightning Wallet Anda.



Status berubah menjadi **"transaction.claim.pending "**, kemudian pesan konfirmasi ditampilkan:



![Confirmation swap-in](assets/fr/11.webp)



Satoshi Lightning Anda segera tersedia di Wallet Anda.



## Keuntungan dan keterbatasan



### Manfaat



**Persaingan tarif**: Agregasi penyedia layanan menciptakan persaingan alami yang menurunkan biaya (0,49% hingga 0,5%).



**Kerahasiaan**: Tanpa KYC, Interface 100% sisi klien (tidak ada transmisi data pribadi), kompatibel dengan Tor Browser.



**Non-kustodian**: HTLC secara matematis menjamin kontrol eksklusif atas dana Anda. Baik swap berhasil, atau Anda mendapatkan bitcoin Anda kembali.



**Sumber terbuka yang dapat dihosting sendiri**: kode publik yang dapat diaudit, dapat digunakan secara lokal untuk ketahanan maksimum terhadap sensor.



### Keterbatasan



**Likuiditas terbatas**: Jumlah penyedia aktif terbatas (Boltz, Eldamar, MiddleWay tergantung periode). Jumlah maksimum mungkin terbatas.



**Waktu kedaluwarsa**: Batas waktu dari 24 jam hingga 48 jam. Jika transaksi On-Chain tidak dikonfirmasi sebelum kedaluwarsa, diperlukan pemulihan manual.



**Pemusatan Interface**: Meskipun dapat dihosting sendiri, Interface resmi dihosting di Halaman GitHub. Jika GitHub menyensor repo, akses melalui swapmarket.github.io akan diblokir (solusi: hosting mandiri).



**Jejak-jejak On-Chain**: Skrip HTLC berpotensi dapat diidentifikasi dengan analisis Blockchain tingkat lanjut.



## Praktik terbaik



### Konfigurasi yang aman



**Unduh Kunci Penyelamatan Anda**: Sebelum melakukan swap pertama Anda, unduh Kunci Penyelamatan Anda dari Pengaturan (lihat bagian khusus di atas). Kunci unik ini akan berfungsi untuk semua swap Anda di masa mendatang, sehingga Anda dapat memulihkan dana jika terjadi masalah.



**Gunakan Tor Browser**: Untuk kerahasiaan maksimum, akses SwapMarket melalui Tor Browser untuk menyembunyikan IP Address Anda.



**Pertimbangkan untuk melakukan hosting sendiri**: Untuk pengguna teknis, menjalankan instans SwapMarket Anda sendiri akan menghilangkan ketergantungan pada domain Halaman GitHub resmi.



### Pengoptimalan pertukaran



**Perhatikan Mempool**: Periksa Mempool.space sebelum melakukan swap-in. Pilih waktu dengan aktivitas rendah untuk meminimalkan biaya Mining.



**Periksa alamat**: Untuk penukaran, periksa dengan cermat Address yang Anda terima. Gunakan salin dan tempel dan periksa 5 karakter pertama dan 5 karakter terakhir.



**Uji dengan jumlah kecil**: Mulailah dengan jumlah minimum yang diizinkan (25.000 hingga 50.000 Sats). Tingkatkan secara bertahap setelah Anda menguasai prosesnya.



**Dokumentasikan swap Anda**: Catat ID setiap swap, penukaran Address, dan tanggal kedaluwarsa. Informasi ini memudahkan pelacakan dan pemulihan jika terjadi masalah teknis.



### Strategi penggunaan



**Menyeimbangkan arus kas Anda**: Gunakan SwapMarket untuk menyesuaikan alokasi Anda antara On-Chain (tabungan, keamanan jangka panjang) dan Lightning (pengeluaran harian, pembayaran instan) sesuai dengan kebutuhan Anda yang sebenarnya.



**Hitung profitabilitas**: Untuk kebutuhan likuiditas Lightning permanen, bandingkan biaya kumulatif swap berulang versus membuka saluran Lightning secara langsung. SwapMarket unggul untuk penyesuaian satu kali, tidak harus untuk aliran reguler yang besar.



## SwapMarket vs Boltz: Apa perbedaannya?



### Boltz: Teknologi vs Layanan



**Boltz adalah teknologi sumber terbuka** (`boltz-backend` di GitHub) yang mengimplementasikan pertukaran atom melalui HTLC antara Bitcoin, Lightning, dan Liquid.



**Poin penting**: Semua penyedia SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) menggunakan contoh backend Boltz mereka sendiri. Oleh karena itu, teknologi yang mendasarinya identik. Kerentanan pada backend Boltz berpotensi mempengaruhi semua penyedia, tetapi sifat sumber terbuka dari sistem ini memungkinkan audit komunitas.



**Boltz Exchange** adalah layanan tunggal yang dioperasikan oleh tim Boltz, sementara **SwapMarket** menyatukan beberapa penyedia yang semuanya menggunakan teknologi Boltz, menciptakan lingkungan harga yang kompetitif.



Lihat tutorial Boltz dan Zeus Swap kami untuk lebih jelasnya:



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

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



SwapMarket memfasilitasi pertukaran Bitcoin/Lightning dengan menggabungkan beberapa penyedia ke dalam satu Interface. Arsitektur HTLC menjamin sifat non-kustodian dari pertukaran, ketiadaan KYC menjaga kerahasiaan, dan kode sumber terbuka yang dapat dihosting sendiri memperkuat ketahanan terhadap sensor.



Persaingan antar penyedia layanan meningkatkan harga dan melipatgandakan sumber likuiditas. Untuk mengoptimalkan manajemen dua Layer (penghematan On-Chain, biaya Lightning), SwapMarket adalah alat praktis yang menjaga kedaulatan dan kerahasiaan keuangan.



## Sumber daya



### Dokumentasi resmi




- [SwapMarket - Aplikasi web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Dokumentasi teknis](https://docs.boltz.Exchange/)
- [Panduan hosting mandiri](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Proyek-proyek terkait




- [Boltz Exchange] (https://boltz.Exchange) - Layanan pertukaran atom asli
- [ZEUS Swaps] (https://zeusln.com) - Penyedia Lightning swap