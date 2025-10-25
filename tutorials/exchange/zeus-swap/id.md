---
name: Zeus Swap
description: Layanan Exchange non-kustodian antara bitcoin On-Chain dan Lightning Network
---

![cover](assets/cover.webp)



Ekosistem Bitcoin menghadirkan dualitas: jaringan utama (On-Chain) menawarkan keamanan maksimum, sementara Lightning Network memungkinkan transaksi instan. Arsitektur dua Layer ini menciptakan tantangan praktis: bagaimana dana dapat ditransfer secara efisien di antara dua lapisan ini tanpa perantara terpusat?



Masalahnya konkret: Anda menerima pembayaran Lightning tetapi ingin menyimpannya di penyimpanan Cold, atau sebaliknya, Anda memiliki bitcoin On-Chain tetapi membutuhkan likuiditas Lightning. Solusi tradisional melibatkan pembukaan/penutupan saluran Lightning secara manual (mahal dan teknis) atau platform terpusat yang membutuhkan KYC.



Zeus Swap memecahkan masalah ini dengan layanan Exchange otomatis tanpa penitipan. Dikembangkan oleh Zeus LSP, layanan ini memungkinkan Anda untuk mengonversi bitcoin On-Chain menjadi satoshi Lightning secara dua arah, tanpa mempercayakan dana Anda ke perantara. Prosesnya menggunakan kontrak atom (HTLC) yang menjamin bahwa Exchange akan selesai atau dibatalkan.



Inovasi ini terletak pada kesederhanaannya: hanya dengan beberapa klik untuk mendapatkan Exchange yang menjaga kedaulatan finansial Anda, tanpa perlu registrasi atau KYC.



## Apa itu Zeus Swap?



Zeus Swap adalah layanan likuiditas Exchange yang dikembangkan oleh Zeus LSP yang memungkinkan pertukaran atomik antara jaringan Bitcoin utama dan Lightning Network. Ini adalah infrastruktur teknis yang menggunakan submarine swap dan reverse swap untuk memfasilitasi konversi dua arah antara On-Chain BTC dan Lightning satoshi, sambil mempertahankan sifat non-kustodian dari operasi.



### Arsitektur teknis



Zeus Swap menggunakan teknologi pertukaran atom Bitcoin/Lightning dari Boltz yang merupakan sumber terbuka. Protokol ini menggunakan Hash Time Locked Contracts (HTLC): kontrak yang mengunci dana dengan dua kondisi pelepasan (pengungkapan rahasia kriptografi atau berakhirnya waktu).



Untuk pertukaran kapal selam (On-Chain → Lightning), pengguna mengirimkan bitcoin ke Address yang menggabungkan Hash dari Invoice Lightning. Zeus LSP membuka dana ini hanya dengan membayar Invoice yang sesuai, mengungkapkan pra-gambar yang secara otomatis membuka bitcoin. Mekanisme ini menjamin keasliannya.



Untuk pertukaran terbalik (Lightning → On-Chain), pengguna membayar Lightning Invoice dari Zeus LSP, mengungkapkan pra-gambar yang memungkinkan pelepasan transaksi Bitcoin yang telah disiapkan ke Address tujuan.



Untuk detail lebih lanjut mengenai cara kerja Lightning Network, bacalah kursus khusus kami:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Model bisnis



Zeus LSP bertindak sebagai pembuat pasar, menjaga likuiditas On-Chain dan Lightning untuk menghormati swap. Untuk swap, Zeus menerapkan biaya variabel (biasanya 0,1% hingga 0,5% tergantung pada arah dan kondisi) ditambah biaya Mining Bitcoin, yang ditampilkan secara transparan sebelum validasi.



Sebagai Penyedia Layanan Lightning, Zeus mengoptimalkan biaya berkat keahliannya dalam pembukaan saluran berdasarkan permintaan, perutean yang efisien, dan solusi likuiditas yang disesuaikan.



### Integrasi



Zeus Wallet secara native mengintegrasikan layanan ini, memungkinkan pertukaran tanpa meninggalkan Interface Bitcoin/Lightning. Hal ini menghilangkan gesekan menyalin dan menempel di antara aplikasi.



Web Interface yang independen tetap dapat diakses oleh semua dompet, menjamin fleksibilitas penggunaan yang maksimal.



## Fitur utama



### Pertukaran dua arah



Zeus Swap menawarkan dua tipe Exchange:



**Swap kapal selam (On-Chain → Lightning)**: menyuntikkan likuiditas Lightning dari cadangan Bitcoin Anda, berguna untuk memberi makan node Wallet atau Lightning yang bergerak tanpa membuka saluran secara manual.



**Reverse swap (Lightning → On-Chain)**: mengonversi satoshi Lightning menjadi bitcoin On-Chain untuk penyimpanan jangka panjang, menghindari penutupan saluran yang mahal.



### Antarmuka pengguna



*web *Interface** (swaps.zeuslsp.com): pengalaman yang disederhanakan tanpa registrasi, proses yang dipandu dengan tampilan biaya dan status secara real-time.



*integrasi *Zeus Wallet**: pertukaran langsung dari aplikasi, manajemen otomatis faktur dan alamat, menghilangkan kesalahan penanganan.



### Keselamatan dan pemulihan



Setiap pertukaran menghasilkan Contract yang unik dengan parameter yang tidak dapat diubah: Hash Petir, batas waktu, pengembalian dana Address. Jika terjadi kegagalan, pemulihan otomatis melalui Address disediakan, terlepas dari Zeus LSP.



**Zeus Swaps Rescue Key**: selama pertukaran On-Chain → Lightning, Zeus secara otomatis menghasilkan kunci pemulihan universal yang menggantikan file pengembalian dana individu yang lama. Kunci unik ini berfungsi pada perangkat apa pun dan untuk semua swap yang dibuat dengannya. Sangat penting untuk mengunduh dan menyimpan kunci ini di lokasi yang aman agar dapat memulihkan dana Anda jika terjadi kegagalan swap.



### Optimalisasi jaringan



Zeus Swap secara otomatis menyesuaikan waktu kedaluwarsa dan biaya Mining sesuai dengan kondisi jaringan. Pengguna Zeus mendapatkan keuntungan dari opsi lanjutan: pilihan LSP, penundaan yang disesuaikan, kompatibilitas dengan layanan lain (Boltz).



## Pemasangan dan penggunaan



### Metode akses



*web *Interface** (swaps.zeuslsp.com): solusi universal yang kompatibel dengan semua dompet, tidak perlu instalasi, ideal untuk penggunaan sesekali.



**Aplikasi Zeus** (iOS/Android): pengalaman terpadu yang memadukan Wallet dan swap, cocok untuk pengguna biasa.



Lihat tutorial Zeus kami untuk mempelajari lebih lanjut tentang Wallet yang lengkap ini:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Konfigurasi web



**On-Chain → Petir**: Prosesnya dimulai dengan mengonfigurasi swap pada web Zeus Swap Interface. Pengguna dapat menggunakan tanda panah di antara bidang On-Chain dan Lightning untuk membalikkan arah swap.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: pemilihan jumlah (Sats 50.000 → Sats 49.648 setelah biaya) dengan tampilan transparan biaya jaringan (Sats 302) dan layanan Zeus (Sats 50).*



Selama proses tersebut, Zeus menawarkan Anda untuk mengunduh kunci pemulihan universal :



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Dialog unduhan untuk Kunci Penyelamatan Zeus Swaps - kunci universal yang menggantikan file penggantian individu yang lama*



Jika Anda sudah memiliki kunci, Zeus memungkinkan Anda untuk memeriksanya:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface untuk memeriksa validitas Kunci Penyelamatan Zeus Swaps yang sudah ada*



Setelah dikonfigurasi, Zeus menghasilkan depot Bitcoin Address dan menampilkan instruksi :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Halaman penyelesaian swap: Kode QR dan Bitcoin Address untuk mengirim 50.000 Satss, dengan pengingat tanggal kedaluwarsa 24 jam*



Swap kemudian menunggu konfirmasi Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transaksi dalam Mempool - menunggu konfirmasi Bitcoin untuk menyelesaikan swap*"



Setelah dikonfirmasi, pertukaran selesai secara otomatis:



![Swap réussi](assets/fr/06.webp)



*Konfirmasi keberhasilan: 49.648 Sats diterima di Lightning setelah dikurangi biaya jaringan dan layanan*



### Menggunakan Aplikasi Zeus



** Lightning → On-Chain**: Aplikasi Zeus menawarkan pengalaman terintegrasi untuk pertukaran terbalik (Lightning ke Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Layar utama Zeus menunjukkan saldo Lightning (69.851 Sats) dan On-Chain (38.018 Sats), akses untuk melakukan swap melalui menu samping*



![Configuration du swap reverse](assets/fr/08.webp)



*Penciptaan reverse swap Interface: 50.000 Sats Lightning → 49.220 Sats On-Chain, dengan biaya jaringan (530 Sats) dan layanan (250 Sats) yang ditampilkan dengan jelas. Pengguna dapat secara manual memasukkan Bitcoin yang menerima Address, atau generate secara otomatis dari Wallet Zeus melalui tombol "generate On-Chain Address"*



![Finalisation du swap mobile](assets/fr/09.webp)



*Layar finalisasi: Layar pembayaran Lightning Invoice dengan "BAYARKAN Invoice INI", konfirmasi pembayaran Lightning yang berhasil dalam 9,96 detik, dan laporan saldo dengan 49.162 Sats yang sedang menunggu konfirmasi*



### Pengawasan dan keamanan



Setiap swap memiliki pengenal unik dengan pelacakan waktu nyata. Tampilan progres penuh, peringatan otomatis untuk tanggal kedaluwarsa. Rekomendasi pengisian daya otomatis sesuai dengan kondisi jaringan.



## Keuntungan dan keterbatasan



### Manfaat





- Kesederhanaan**: Tukar dalam beberapa klik vs. manipulasi saluran manual
- Non-kustodian**: tidak ada KYC, tidak ada akun, dana tidak pernah dipercayakan kepada pihak ketiga
- Transparansi**: biaya ditampilkan secara eksplisit sebelum validasi (0,1% hingga 0,5% + minage tergantung pada pengujian pengguna - periksa biaya saat ini di setiap swap)
- Integrasi seluler**: pengalaman asli di Zeus Wallet



### Keterbatasan





- Waktu kedaluwarsa **: maksimum 24-48 jam, gagal jika Bitcoin tidak dikonfirmasi tepat waktu
- Batas jumlah**: minimum 25.000 Sats, variabel likuiditas Zeus LSP sesuai dengan kondisi
- Melacak On-Chain**: Skrip HTLC yang berpotensi dapat diidentifikasi oleh analisis Blockchain
- Diperlukan konfirmasi**: minimal 10 menit untuk validasi Bitcoin



## Praktik terbaik



### Waktu dan biaya





- Perhatikan Mempool.space untuk saat-saat kepadatan rendah
- Lebih memilih akhir pekan dan jam-jam di luar jam sibuk untuk mengurangi biaya Mining
- Hitung profitabilitas: jumlah kecil vs pembukaan saluran langsung



### Keamanan





- Periksa alamat Bitcoin dengan hati-hati (disarankan untuk menyalin-tempel)
- Cadangkan Kunci Penyelamatan Zeus Swaps**: unduh dan simpan kunci pemulihan di tempat yang aman
- Dokumen: ID Contract, pengembalian dana Address, tanggal kedaluwarsa
- Gunakan biaya Mining yang sesuai untuk konfirmasi tepat waktu



### Strategi penggunaan





- Menyeimbangkan likuiditas On-Chain/Lightning agar sesuai dengan kebutuhan Anda
- Zeus Swap untuk penyesuaian satu kali, saluran langsung untuk kebutuhan permanen



## Perbandingan dengan layanan swap lainnya



### Zeus Swap vs Boltz Exchange



Zeus Swap menggunakan teknologi backend Boltz, tetapi membuat beberapa perbaikan penting:



*manfaat *Zeus Swap**:




- Interface unified **: integrasi asli dalam teknik web Zeus Wallet vs Interface Boltz
- WebSocket API**: pembaruan waktu nyata vs. jajak pendapat manual
- Manajemen otomatis**: penagihan otomatis dan manajemen Address
- Dukungan seluler**: hanya untuk pengoptimalan ponsel cerdas vs desktop
- Dokumentasi Swagger**: API REST lengkap untuk pengembang



**Boltz tetap menguntungkan** untuk kemandirian total dan digunakan dengan pengaturan Bitcoin/Lightning.



Zeus Swap mengubah teknologi Boltz yang telah terbukti menjadi pengalaman pengguna yang umum, sebanding dengan perbedaan antara protokol mentah dan aplikasi yang mudah digunakan.



### Zeus Swap vs Phoenix/Breez (swap terintegrasi)



Phoenix dan Breez mengintegrasikan fungsi swap transparan yang menyembunyikan kerumitan teknis dari pengguna akhir. Phoenix menggunakan sistem swap-in/swap-out otomatis di mana pengguna tidak secara eksplisit membedakan antara lapisan Bitcoin: dia "mengirim ke Bitcoin Address" dan aplikasi menangani swap di latar belakang.



Pendekatan yang sangat sederhana ini sangat cocok untuk pemula, tetapi membatasi pemahaman dan kontrol operasi. Zeus Swap mengadopsi filosofi yang lebih mendidik: pengguna memahami bahwa mereka menukar antara dua lapisan yang berbeda, secara bertahap mengembangkan pemahaman mereka tentang ekosistem dua Layer Bitcoin.



## Perbandingan biaya dan batasan terperinci (2024)



⚠️ **Peringatan**: Biaya dapat berubah sewaktu-waktu tergantung pada kondisi pasar dan pembaruan layanan. Selalu periksa biaya yang ditampilkan di Interface sebelum memvalidasi swap.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap menawarkan keseimbangan antara kemudahan penggunaan dan kontrol teknis: lebih mudah diakses daripada Boltz, lebih fleksibel daripada Phoenix/Breez, dengan pendekatan non-kustodian yang ketat.



## Kesimpulan



Zeus Swap mewakili inovasi yang signifikan dalam ekosistem Bitcoin, yang secara elegan menyelesaikan tantangan interoperabilitas antara jaringan utama dan Lightning Network. Dengan menggabungkan ketahanan kriptografi atomic swap dengan pengalaman pengguna yang dapat diakses, layanan ini mendemokratisasi manajemen Bitcoin dual-Layer tanpa mengorbankan prinsip-prinsip kedaulatan keuangan.



Arsitektur non-kustodian Zeus Swap, yang diwarisi dari teknologi Boltz yang telah terbukti, memastikan bahwa dana Anda tetap berada di bawah kendali eksklusif Anda selama proses swap. Pendekatan ini menghormati semangat Bitcoin sambil menawarkan kenyamanan pengguna yang diperlukan untuk adopsi arus utama. Transparansi harga dan tidak adanya proses KYC memperkuat proposisi nilai yang unik ini.



Bagi pengguna Bitcoin modern, Zeus Swap adalah alat strategis untuk mengoptimalkan distribusi likuiditas sesuai dengan kebutuhan: Penyimpanan aman On-Chain untuk simpanan jangka panjang, ketersediaan kilat untuk pembelanjaan harian dan transaksi mikro. Fleksibilitas ini mengubah manajemen Bitcoin dari kendala teknis menjadi keunggulan kompetitif.



Evolusi masa depan Zeus Swap, yang didukung oleh tim Zeus LSP yang berpengalaman dan komunitas open-source Boltz, menjanjikan peningkatan yang berkelanjutan dalam hal biaya, waktu pemrosesan, dan pengalaman pengguna. Layanan ini merupakan bagian dari tren yang lebih luas menuju pematangan infrastruktur Bitcoin, di mana kecanggihan teknis menjadi transparan bagi pengguna akhir.



## Sumber daya



### Dokumentasi resmi




- [Zeus Swap - Portal Web](https://swaps.zeuslsp.com)
- [Zeus Wallet - Aplikasi seluler](https://zeusln.app)
- [Blog Zeus - Pengumuman dan tutorial](https://blog.zeusln.com)
- [Dokumentasi teknis Zeus](https://docs.zeusln.app)



### Komunitas dan dukungan




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)