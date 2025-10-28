---
name: Zeus Embedded - Tingkat Lanjutan
description: Kustodian mandiri multi-node Wallet
---

![Zeus](assets/cover.webp)


## Pengantar ZEUS Wallet


ZEUS adalah aplikasi seluler Bitcoin wallet dan pengelola node dengan fungsionalitas penuh dari Bitcoin Lightning wallet yang membuat pembayaran Bitcoin jadi simpel, memberi kamu kendali penuh atas keuanganmu, dan memungkinkan pengguna berpengalaman mengelola node Lightning langsung dari genggaman tangan.


### Untuk siapa ZEUS?

Saat ini ZEUS diperuntukkan bagi orang-orang yang menjalankan [Lightning Network Daemon (LND)] (https://lightning.engineering/) atau [Core Lightning (CLN)] (https://blockstream.com/lightning/) node rumah/bisnis mereka sendiri dan mengelolanya melalui Zeus, dari jarak jauh.

Pedagang yang menggunakan [BTCPay] (https://btcpayserver.org/) atau [LNBits] (https://lnbits.com/) atau [Alby] (https://getalby.com/) (atau akun LNDhub lainnya) juga dapat terhubung ke, menggunakan, dan mengelola node/akun mereka dari ZEUS.

[Mulai dari v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS akan mulai melayani pengguna biasa yang hanya menginginkan cara sederhana untuk melakukan pembayaran Bitcoin yang cepat dan murah dari perangkat seluler mereka dengan memiliki [built-in mobile Lightning node](https://docs.zeusln.app/category/embedded-node) dengan [Lightning Service Provider (LSP)](https://docs.zeusln.app/lsp/intro) yang terintegrasi.

### Sumber daya Zeus yang penting:


- Halaman web resmi Zeus - [https://zeusln.app/](https://zeusln.app/)
- Dokumentasi Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Repositori Github Zeus](https://github.com/ZeusLN/zeus)
- [Grup dukungan Telegram Zeus](https://t.me/ZeusLN)
- [Zeus di NOSTR](https://iris.to/zeus@zeusln.app)
- [Pengumuman Blog Zeus](https://blog.zeusln.com)


### Fitur Zeus

#### Fitur umum:


- Penitipan mandiri, Bitcoin dan Lightning hanya Wallet
- Tanpa biaya pemrosesan, Tanpa KYC
- Sumber terbuka sepenuhnya (APGLv3)
- Multi-node / akun didukung (Kamu dapat mengelola node rumah sendiri, menjalankan node LND yang tertanam, terhubung ke beberapa akun LNDhub)
- Menu aktivitas yang mudah digunakan
- Enkripsi PIN atau passphrase, mode Privasi - sembunyikan data sensitif milikmu
- Buku kontak, multi tema, multi bahasa

#### Fitur teknis

- Terhubung melalui Tor
- Dukungan LNURL penuh (Bayar, tarik, autentikasi, saluran), Kirim ke alamat Lightning
- Manajemen saluran Pencahayaan yang terperinci, dukungan MPP/AMP, Keysend, manajemen biaya perutean
- Dukungan Replace-by-fee (RBF) dan Anak membayar untuk orang tua (CPFP)
- Pembayaran dan permintaan NFC, Tanda tangani & verifikasi pesan
- Dukungan SegWit dan Taproot
- Saluran Taproot Sederhana
- Alamat kilat kustodian mandiri (@zeuspay.com)
- Point of Sale by Square (segera buka PoS)

### Panduan dan Video Tutorial

Untuk dapat menggunakan Zeus dan mengelola saluran Lightning, likuiditas, biaya, dan lain-lain, lebih baik kamu membaca terlebih dahulu beberapa panduan penting tentang Lightning Network.

#### Panduan:


- [LND - Dokumentasi Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Dokumentasi Lightning Core] (https://lightning.readthedocs.io/index.html)
- [Panduan Lightning Pemula] (https://bitcoiner.guide/lightning/) - oleh Bitcoin Tanya Jawab
- [Manajemen Lightning Node](https://www.lightningnode.info/) - oleh openoms
- [Lightning Network dan analogi bandara](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Mengelola Likuiditas Lightning Node](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Pemeliharaan Lightning Node](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Video tutorial oleh Sesi BTC

![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)

## Panduan panduan bagaimana cara mulai menggunakan node tertanam Zeus LN pada perangkat seluler kamu


![Image](assets/en/01.webp)

Aku mendedikasikan panduan ini untuk semua pengguna baru Lightning Network (LN) yang ingin memulai perjalanan kedaulatan finansial dengan menggunakan wallet node self-custodial di perangkat seluler mereka.

Anggap saja kamu sudah melewati tahap memakai dompet LN kustodian, tapi belum siap menjalankan node LN routing publik. Kamu cuma ingin menumpuk lebih banyak sats di LN dengan cara yang lebih self-custodial dan tetap bisa melakukan pembayaran rutin lewat LN.

Ini dia Zeus, dimulai dengan [versi v0.8.0 yang diumumkan di blog mereka] (https://blog.zeusln.com/new-release-zeus-v0-8-0/), sekarang menawarkan node LND yang disematkan ke dalam aplikasi. Sampai saat ini Zeus adalah aplikasi manajemen node jarak jauh + akun LNDhub. Tetapi sekarang... node ada di dalam ponsel!


![Image](assets/en/02.webp)


### Rekap cepat fitur-fitur utama untuk Zeus Node:


- Node LND privat** - Artinya, node ini tidak akan melakukan routing publik untuk pembayaran orang lain lewat node kamu. Node dan salurannya bersifat privat (tidak terlihat di grafik publik LN). Untuk menerima dan mengirim pembayaran, semuanya dilakukan lewat koneksi dengan rekan LSP kamu. Ingat: Zeus Embedded Node tidak melakukan routing publik!
- Layanan LND yang persisten** - Pengguna bisa mengaktifkan fitur ini dan membuat layanan LND tetap berjalan terus-menerus layaknya node LN biasa. Aplikasi tidak perlu dibuka, karena layanan persisten akan menjaga semua komunikasi tetap online.
- Filter blok Neutrino** - sinkronisasi blok dilakukan dengan menggunakan [filter blok dan protokol Neutrino] (https://bitcoinops.org/en/topics/compact-block-filters/) (tidak ada informasi tentang dana On-Chain pengguna kami). Pengingat: Untuk koneksi internet dengan latensi tinggi atau lambat, sinkronisasi blok berbasis Neutrino kadang bisa gagal. Coba ganti ke server Neutrino yang lokasinya lebih dekat supaya sinkronisasi bisa pulih. Tanpa sinkronisasi ini, node LND kamu tidak akan bisa dijalankan!
- Saluran Taproot Sederhana** - Ketika menutup saluran ini, pengguna dikenakan biaya yang lebih rendah dan diberikan privasi yang lebih besar karena mereka terlihat seperti pengeluaran Taproot lainnya ketika memeriksa jejak On-Chain mereka.
- LSP terintegrasi** - Olympus adalah node LSP baru untuk Zeus. Pengguna dapat menerima kembali Sats melalui LN secara langsung, tanpa harus mengatur saluran LN sebelumnya. Cukup dengan membuat LN Invoice dan membayar dari LN Wallet lainnya, dengan layanan saluran Zeus 0-conf. Baca lebih lanjut tentang Zeus LSP di sini. LSP juga memberikan privasi tambahan kepada pengguna kami dengan menyediakan faktur yang dibungkus yang menyembunyikan kunci publik node mereka dari pembayar.
- Buku Kontak** - Kamu bisa menyimpan kontak secara manual atau mengimpor dari NOSTR, untuk memudahkan pengiriman pembayaran ke tujuan reguler kamu.
- Dukungan penuh untuk LNURL, pengiriman dan penerimaan LN Address** - sekarang kamu dapat mengatur kustodian mandiri LN Address kamu sendiri dengan @zeuspay.com. Pengingat: kamu juga dapat menggunakan Zeus untuk autentikasi LN di situs-situs yang memungkinkanmu masuk dengan autentikasi LN. Sangat praktis.
- Point of Sale** - Sekarang pengguna pedagang dapat mengatur item produk mereka sendiri dan menjual langsung dari Zeus, dengan PoS yang terintegrasi. Untuk saat ini berisi kebutuhan dasar tetapi di masa depan akan berisi fitur-fitur yang diperluas.
- Log LND** - pengguna dapat membaca secara real time log layanan LND dan menggunakannya untuk men-debug masalah yang mungkin terjadi (terutama untuk koneksi yang buruk)
- Pencadangan Otomatis** - saluran node LN secara otomatis dicadangkan di server Olympus. Pencadangan otomatis ini dienkripsi dengan node Wallet seed kamu (tanpa seed sama sekali tidak berguna). Pengguna juga dapat mengekspor secara manual SCB (cadangan saluran statis) untuk pemulihan bencana.


### Cara bergabung dengan Zeus LN Node (LND tertanam)

Dalam panduan ini aku hanya akan membahas tentang node LND yang tertanam, dan bukan tentang cara lain untuk menggunakan aplikasi yang luar biasa ini (manajemen node jarak jauh dan akun LNDhub). Untuk jenis koneksi lainnya, silakan merujuk ke [halaman Zeus Docs] (https://docs.zeusln.app/category/getting-started), yang dijelaskan dengan sangat baik dan tidak perlu menulis panduan khusus.

#### LANGKAH 1 - PENGATURAN AWAL


Karena Zeus adalah node LND penuh, aku akan memberikan beberapa rekomendasi awal:

- Jangan pakai perangkat lama, karena bisa memengaruhi performa aplikasi canggih ini. Terutama saat proses sinkronisasi, aplikasi bisa menggunakan CPU dan RAM cukup intensif. Kalau perangkatmu kurang kuat, Zeus bisa saja tidak berfungsi dengan baik.
- Gunakan minimal Android 11 sebagai sistem operasi dan pastikan selalu diperbarui. Untuk iOS juga sama, usahakan pakai versi OS terbaru.
- Kamu butuh setidaknya 1 GB ruang penyimpanan untuk data. Seiring waktu ukuran ini bisa bertambah, tapi ada fitur untuk memadatkan basis data hingga ke level MB.
- Tidak perlu menggunakan Zeus dengan Tor atau Orbot. Jangan bikin rumit hal yang sebenarnya sederhana. Tor tidak akan menambah privasi di sini, malah bisa memperlambat sinkronisasi awal. Hati-hati juga dengan VPN yang kamu pakai, dan pastikan latensi koneksi ke server Neutrino tetap rendah. Ingat, filter blok Neutrino tidak melacak atau membocorkan identitas perangkatmu—hanya menyaring blok. Lalu lintas LN juga berjalan di belakang LSP dengan kanal privat, jadi informasi yang keluar sangat minim. Tidak ada alasan buat panik soal privasi.
- Bersabarlah untuk sinkronisasi awal, bisa memakan waktu beberapa menit. Usahakan untuk terhubung ke koneksi internet broadband dengan latensi yang baik. Jika kamu menjalankan node Bitcoin kamu sendiri, [Kamu dapat mengaktifkan layanan neutrino] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) dan menghubungkan Zeus kamu ke node kamu sendiri, bahkan menggunakan LAN internal, sehingga kamu akan mendapatkan kecepatan maksimum.


Setelah kamu mengatur jenis koneksi "Node tertanam", aplikasi akan mulai menyinkronkan untuk sementara waktu. Tunggu dengan sabar untuk menyelesaikan bagian tersebut, lalu masuk ke halaman Pengaturan utama.

![Image](assets/en/03.webp)

Secara singkat, mari kita selami masing-masing bagian Pengaturan dan memahami beberapa fitur utama, sebelum kamu mulai menggunakan Zeus:


**A - PENGATURAN**

Ini adalah bagian dengan pengaturan umum untuk seluruh aplikasi


**1 - Penyedia Layanan Lightning (LSP) **

Di sini disajikan dua layanan LSP:

- saluran _Just in time_ - ketika kamu tidak memiliki saluran terbuka atau likuiditas masuk yang tersedia, jika layanan ini diaktifkan, layanan ini akan membuka saluran dengan cepat untukmu. Opsi ini dapat dinonaktifkan jika kamu tidak ingin membuka lebih banyak saluran jenis ini.
- meminta saluran terlebih dahulu_ - kamu dapat membeli saluran masuk dari LSP Olympus secara langsung di aplikasi dengan berbagai opsi dan jumlah (untuk masuk dan keluar).

LSP membantu menghubungkan pengguna ke Lightning Network dengan membuka saluran pembayaran ke node mereka. [Baca lebih lanjut tentang LSP di sini] (https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS memiliki LSP baru yang terintegrasi ke dalamnya yang disebut [OLYMPUS by ZEUS] (https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), yang tersedia untuk semua pengguna yang menggunakan node tertanam yang baru.

Pada bagian ini, secara default adalah LSP Olympus (https://0conf.lnolymp.us), tetapi kamu juga dapat mengatur LSP 0conf lain yang mendukung protokol ini.

perlu diingat:_

ChatGPT said:

Ketika kamu membuka saluran dengan Olympus LSP menggunakan invoice LN yang dibungkus, kamu juga akan mendapatkan likuiditas masuk sebesar 100 ribu sats! Ini opsi yang sangat bagus kalau kamu ingin bisa menerima lebih banyak sats.

Contohnya: kamu menyetor 400k sats untuk membuka saluran LSP, maka LSP akan membuka saluran berkapasitas 500k sats ke node Zeus kamu dan mendorong 400k sats yang kamu setorkan ke sisi kamu.

Likuiditas masuk berarti ada lebih banyak “ruang” di saluran kamu untuk menerima pembayaran.

Ke depannya, diharapkan akan ada lebih banyak LSP yang bisa diintegrasikan ke dalam Zeus, dan masing-masing bisa digunakan sebagai alternatif. Hanya soal waktu sampai LSP baru mengadopsi standar terbuka untuk saluran 0-conf seperti ini.

Kalau kamu tidak ingin membuka saluran baru secara instan, kamu bisa menonaktifkan opsi ini.

Di bagian yang sama, kamu juga bisa memilih opsi “request Simple Taproot Channels” saat LSP akan membuka saluran ke node Zeus kamu. Saluran Taproot sederhana ini memberikan privasi on-chain yang lebih baik dan biaya penutupan saluran yang lebih rendah. Hanya ada dua alasan kenapa kamu mungkin tidak ingin menggunakannya:

- Fitur ini masih baru, jadi mungkin masih ada bug di LND saat digunakan.
- Rekan kamu belum mendukungnya. Bahkan node LND pun saat ini harus mengaktifkannya secara eksplisit.

**2 - Pengaturan pembayaran**

Fitur ini memberi kamu cara untuk mengatur biaya sesuai keinginan, baik untuk pembayaran lewat LN maupun on-chain. Kamu juga bisa menambah atau mengurangi batas waktu untuk invoice kamu.

Kalau beberapa pembayaran LN gagal, kamu bisa menaikkan biaya supaya rute yang lebih baik bisa ditemukan. Begitu juga untuk transaksi on-chain, kamu bisa menetapkan biaya tertentu agar transaksi kamu tidak tersangkut di mempool terlalu lama saat periode biaya sedang tinggi.


**3 - Pengaturan faktur**

Pada bagian ini terdapat beberapa opsi untuk faktur generate:

- Atur memo standar yang akan muncul di invoice yang kamu buat.
- Tentukan waktu kedaluwarsa dalam hitungan detik, kalau kamu ingin durasi pembayaran invoice dibuat lebih lama atau lebih singkat.
- Aktifkan route hints — ini memberi informasi untuk menemukan saluran yang tidak diiklankan atau bersifat privat. Fitur ini memungkinkan pembayaran bisa diarahkan ke node yang tidak terlihat publik di jaringan. Route hints menyediakan rute parsial antara node privat penerima dan node publik. Informasi ini disertakan di invoice yang dibuat penerima dan diberikan ke pengirim. Disarankan untuk mengaktifkan fitur ini secara default, karena kalau tidak, pembayaran masuk bisa gagal akibat tidak ditemukan rute yang sesuai.
- AMP Invoice - Pembayaran Multi Jalur Atomik adalah jenis pembayaran Lightning baru yang diimplementasikan oleh LND yang memungkinkan untuk menerima Sats tanpa Invoice tertentu, menggunakan [keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Praktis merupakan kode pembayaran statis. [Baca lebih lanjut di sini] (https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Tampilkan bidang gambar awal khusus - gunakan opsi ini hanya dalam kasus yang sangat spesifik ketika kamu benar-benar ingin menggunakan bidang khusus dalam gambar awal. [Baca selengkapnya di sini](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).

Pilihan lain di bagian ini adalah bagaimana mengatur jenis onchain Address yang ingin kamu gunakan: SegWit bersarang, SegWit, Taproot.

![Image](assets/en/04.webp)

Klik ikon roda di bagian atas, lalu akan muncul popup untuk memilih tipe address yang kamu inginkan. Setelah kamu mengaturnya, setiap kali menekan tombol Terima untuk transaksi on-chain, address yang dihasilkan akan sesuai dengan tipe yang kamu pilih. Kamu bisa mengubahnya kapan pun.

**4 - Pengaturan saluran**

Di bagian ini kamu dapat mengatur beberapa fitur saluran pembuka, seperti:

- jumlah konfirmasi
- Umumkan saluran (secara default tidak aktif), artinya saluran tersebut akan menjadi saluran yang tidak diumumkan
- Saluran Taproot Sederhana
- Tampilkan tombol pembelian saluran

**5 - Pengaturan privasi**

Di sini kamu akan menemukan beberapa pengaturan dasar untuk menambahkan lebih banyak privasi menggunakan aplikasi Zeus:

- Block explorer untuk membuka rincian tx (Mempool.space, blockstream.info atau yang bersifat pribadi)
- Baca papan klip - sakelar aktif/nonaktif jika kamu ingin Zeus membaca papan klip perangkat
- Mode Lurker - sakelar aktif/nonaktif jika kamu ingin menyembunyikan info sensitif tertentu dari aplikasi Zeus. Pilihan yang bagus ketika kamu membuat demo atau tangkapan layar.
- Saran biaya Mempool - aktifkan opsi ini jika kamu ingin menggunakan tingkat biaya yang disarankan dari [Mempool.space](https://Mempool.space/)


**6 - Keamanan**

Bagian ini hanya punya dua opsi untuk mengamankan aplikasi saat dibuka: atur kata sandi atau PIN.

Setelah kamu mengatur PIN untuk membuka aplikasi, kamu juga bisa membuat PIN darurat. PIN rahasia tambahan ini hanya digunakan saat kamu berada dalam situasi terpaksa atau terancam. Jika PIN ini dimasukkan, semua konfigurasi di aplikasi akan langsung terhapus. Karena itu, pastikan kamu selalu memperbarui cadanganmu. Pencadangan otomatis memang aktif secara default, tapi sebaiknya kamu juga punya salinan cadangan sendiri di luar perangkat.


**7 - Mata Uang**

Mengaktifkan atau menonaktifkan opsi untuk menampilkan konversi mata uang fiat dalam penggunaan aplikasi Zeus. Saat ini mendukung lebih dari 30 mata uang fiat di seluruh dunia.


**8 - Bahasa**

Kamu dapat beralih di antara beberapa bahasa terjemahan, yang ditinjau oleh komunitas Zeus dengan penutur asli.

**9 - Tampilan**

Di bagian ini, kamu bisa mempersonalisasi tampilan Zeus sesuai selera, memilih berbagai tema warna, menentukan layar default (keypad atau balance), menampilkan alias node kamu, mengaktifkan tombol keypad besar, dan menampilkan lebih banyak angka desimal.
**10 - Tempat Penjualan**

Ini adalah fitur khusus untuk mengaktifkan atau menonaktifkan sistem PoS yang terintegrasi di Zeus. Kamu bisa menjalankan PoS mandiri atau menghubungkannya ke sistem PoS Square. Saat ini fungsinya masih dasar, tapi sudah cukup bagus untuk langkah awal dan bisa membantu pedagang kecil seperti bar, restoran, atau toko kelontong mulai menerima BTC secara langsung.

Di dalam pengaturan ini, kamu akan menemukan berbagai opsi untuk mengatur PoS:

- Jenis pembayaran konfirmasi: Hanya LN, 0-konf, 1-konf
- Mengaktifkan/menonaktifkan tips untuk karyawan yang mengoperasikan PoS
- Tampilkan / sembunyikan keypad
- Persentase pajak yang berlaku pada tiket
- Membuat produk dan kategori produk
- Daftar sederhana dari semua penjualan

Berikut ini adalah video demo langsung cara menggunakan Zeus PoS:

*b - Cadangan Wallet** *B - Cadangan Wallet


Node yang tertanam di ZEUS didasarkan pada LND dan menggunakan [format aezeed seed] (https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Ini berbeda dengan [format BIP39] (https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) yang biasa kamu lihat pada kebanyakan dompet Bitcoin, walaupun mungkin terlihat mirip. Aezeed menyertakan beberapa data tambahan termasuk tanggal lahir Wallet yang akan membantu pemindaian ulang selama pemulihan menjadi lebih efisien.

Format kunci Aezeed harus kompatibel dengan dompet seluler berikut ini: Blixt, BlueWallet dan Breez. Harap diperhatikan bahwa seed saja tidak akan cukup untuk memulihkan semua saldo kamu jika kamu memiliki saluran yang terbuka atau tertunda untuk ditutup!

Pelajari lebih lanjut tentang proses pencadangan dan pemulihan di [halaman Dokumen Zeus](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).

SARAN DAYA: Ketika kamumenyimpan seed milikmu, harap simpan juga node pubkey! Kadang-kadang ada baiknya untuk memilikinya, bersama dengan seed dan SCB (Cadangan Saluran Statis) kamu untuk berjaga-jaga jika kamu perlu memverifikasi pemulihan.

SCB hanya diperlukan kalau kamu sudah punya saluran LN yang terbuka. Kalau kamu cuma punya dana on-chain, fitur ini tidak dibutuhkan.

Kalau setelah beberapa waktu riwayat transaksi lama masih belum muncul, buka Embedded Node → Peers lalu nonaktifkan opsi untuk menggunakan daftar peer yang dipilih (secara default: btcd.lnolymp.us). Tindakan ini akan memicu restart dan membuat node terhubung ke server Neutrino pertama yang tersedia dengan waktu respons yang lebih cepat. Kamu juga bisa memakai peer Neutrino lain yang sudah dikenal dan disebutkan di bawah ini.

Kalau kamu ingin melihat lebih banyak opsi pemulihan untuk node LND, [silakan baca panduan saya sebelumnya] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), di mana kamu dapat menemukan langkah-langkah cara mengimpor Aezeed seed ke dalam Sparrow Wallet atau metode lainnya.

**C - Embedded Node**

Pada bagian ini kita akan menemukan beberapa alat dasar untuk mengelola node terintegrasi:

- pemulihan Bencana_ - Pencadangan otomatis dan manual untuk saluran LN. Silakan baca lebih lanjut cara menggunakan fitur ini di halaman Dokumen Zeus.
- _Express Graph Sync_ - Aplikasi Zeus akan mengunduh grafik data gosip LN dari server khusus, untuk sinkronisasi yang lebih cepat dan lebih baik, menawarkan jalur pembayaran terbaik. kamu juga dapat memilih untuk menghapus data grafik sebelumnya pada saat pengaktifan.
- _Peers_ - bagian untuk mengelola neutrino peers dan 0-conf peers. Jika kamu mengalami masalah dengan sinkronisasi awal, saluran tidak online, itu karena perangkat kamu memiliki latensi tinggi dengan peer neutrino yang dikonfigurasi. Coba ganti daftar peer yang disukai atau tambahkan peer spesifik yang kamu tahu memiliki latensi yang lebih baik untuk sinkronisasi. Server neutrino yang terkenal adalah:

 - btcd1.lnolymp.us | btcd2.lnolymp.us - untuk wilayah AS
 - sg.lnolymp.us - untuk wilayah Asia
 - btcd-Mainnet.lightning.computer - untuk wilayah AS
 - uswest.blixtwallet.com (Seattle) - untuk wilayah AS
 - europe.blixtwallet.com (Jerman) - untuk wilayah Uni Eropa
 - asia.blixtwallet.com - untuk wilayah Asia
 - node.eldamar.icu - untuk wilayah AS
 - noad.sathoarder.com - untuk wilayah AS
 - bb1.breez.technology | bb2.breez.technology - untuk wilayah AS
 - neutrino.shock.network - wilayah AS

- log _LND_ - Alat yang sangat berguna untuk men-debug masalah pada node LN kamu dan memantau apa yang terjadi secara lebih mendalam di level teknis.
- pengaturan lanjutan_ - lebih banyak alat untuk mengontrol penggunaan node LND:



 - mode _Pathfinding_ - Bimodal atau apriori, cara untuk menemukan rute yang lebih baik untuk pembayaran LN kamu dan juga mengatur ulang informasi rute sebelumnya. Silakan baca panduan yang sangat bagus ini tentang pencarian rute: [Pathfinding] (https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - oleh Docs Lightning Engineering dan [LN Payment Pathfinding] (https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - oleh Voltage
 - _Persistent LND_ - aktifkan mode ini jika kamu ingin layanan LND berjalan terus menerus di latar belakang dan menjaga node tetap online 24/7. Ini sangat berguna kalau kamu menggunakan Zeus sebagai PoS di toko kecil atau menerima banyak tip LN melalui LN Address.
 - _Rescan wallet_ - opsi ini akan memicu pemindaian penuh pada saat restart dari semua txs onchain Wallet. Aktifkan hanya jika kamu kehilangan beberapa txs di Wallet. Proses pemindaian ulang akan memakan waktu, beberapa menit, jadi bersabarlah dan selalu periksa log untuk melihat detail lebih lanjut mengenai perkembangannya.
 - _Compact Database_ - opsi ini sangat berguna jika aplikasi Zeus menggunakan banyak ruang perangkat (lihat detail aplikasi di pengaturan perangkat kamu). Jika kamu memiliki banyak aktivitas menggunakan Zeus, saya sarankan untuk melakukan pemadatan ini lebih sering. Setelah melihat bahwa kamu memiliki lebih dari 1-1,5GB data untuk aplikasi Zeus, lakukan pemadatan. Proses ini akan dimulai ulang dan memakan waktu, jadi bersabarlah.
 - _Delete Neutrino files_ - opsi ini untuk menghapus file neutrino (dengan restart) akan mengurangi banyak penggunaan penyimpanan data. Mengurangi penggunaan data juga berdampak besar pada penggunaan baterai, mengurangi penggunaan baterai, terutama jika kamu menggunakan Zeus dalam mode persisten.

**D - Info Node**

Di bagian ini, kamu akan menemukan detail lebih lanjut tentang status node Zeus milikmu sebagai:

- Alias - ID node pendek
- Public Key - kunci publik lengkap untuk node kamu yang diperlukan oleh node lain untuk menemukan jalur menuju node milikmu. Ingatlah bahwa pubkey ini TIDAK terlihat pada LN Explorer biasa (Mempool, Amboss, 1ML, dll). Pubkey ini HANYA dapat dijangkau melalui rekan-rekan dan saluran LN kamu yang terhubung.
- Versi implementasi LN
- Versi aplikasi Zeus
- Status Synced to chain dan Synced to graph - status yang sangat penting, yang menunjukkan status node yang benar. Jika keduanya tidak menampilkan "true", itu berarti node kamu masih melakukan sinkronisasi atau mengalami beberapa masalah dalam sinkronisasi. Jadi disarankan untuk melihat ke dalam log LND kamu atau tunggu sebentar.
- Tinggi blok dan Hash - menunjukkan blok terakhir dan Hash yang dilihat dan disinkronkan oleh node milikmu.

**E - Info Jaringan**

Bagian ini menampilkan detail lebih lanjut tentang status umum Lightning Network, yang diambil dari data sinkronisasi grafik kamu: jumlah saluran publik yang tersedia, jumlah node, jumlah saluran zombie (offline atau tidak aktif), diameter grafik, serta nilai rata-rata dan derajat maksimum dari grafik tersebut.

Data informasi ini dapat berguna untuk melakukan debug atau hanya digunakan untuk statistik.

*f - Lightning Address** 

Di bagian ini, kamu bisa mengatur sendiri alamat LN kamu di @zeuspay.com.

ZEUS PAY memanfaatkan hash preimage yang dibuat pengguna, invoice HODL, dan skema otorisasi Zaplocker Nostr untuk memungkinkan kamu menerima pembayaran ke alamat Lightning statis, bahkan saat tidak online 24/7. Kamu hanya perlu membuka wallet ZEUS dalam waktu 24 jam untuk mengklaim pembayaran. Jika tidak, dana akan otomatis dikembalikan ke pengirim.

Kalau kamu mengaktifkan mode persisten, semua pembayaran ke LN Address kamu akan langsung diterima.


Pelajari tentang cara kerja pembayaran [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) dan lebih lanjut tentang [Biaya ZeusPay di sini](https://docs.zeusln.app/lightning-Address/fees).

**G - Alamat Onchain**

Di bagian ini kamu bisa melihat alamat onchain yang dihasilkan untuk kontrol koin yang lebih baik

**H - Kontak**

Buku kontak baru diperkenalkan di Zeus v0.8.0, yang bisa kamu gunakan untuk mengirim pembayaran dengan cepat ke teman dan keluarga, serta mengimpor kontak langsung dari Nostr.

Cukup masukkan npub Nostr kamu atau alamat NIP-05 yang bisa dibaca manusia, dan ZEUS akan mengambil daftar kontakmu dari Nostr. Dari situ, kamu bisa langsung mengirim pembayaran ke kontak tertentu, atau mengimpor semua maupun sebagian kontak ke buku kontak lokal di Zeus.

Berikut video singkat tentang cara mengatur dan menggunakan fitur kontak di Zeus:

**I - Alat**

Di sini kami memiliki berbagai sub-bagian dengan lebih banyak alat:


- akun_ - di sini kamu dapat mengimpor akun/dompet eksternal, dompet Cold, dompet Hot, untuk mengontrol atau digunakan sebagai sumber pendanaan eksternal untuk saluran node Zeus kamu. Fitur ini masih dalam tahap percobaan.
- mempercepat transaksi_ - Fitur ini dapat membantu ketika kamu memiliki tx yang macet ke dalam Mempool dan ingin menaikkan biaya. Kamu harus memberikan output tx dari detail tx dan memilih biaya baru yang ingin kamu gunakan. Harus lebih tinggi dari yang sebelumnya dan mengharuskan kamu memiliki lebih banyak dana yang tersedia di onchain Wallet kamu.


![Image](assets/en/05.webp)


Kamu harus membuka transaksi yang masih tertunda dan menyalin output txid-nya. Setelah itu, masuk ke bagian ini dan tempelkan txid tersebut, lalu pilih biaya baru yang ingin kamu gunakan untuk menabraknya. Akan muncul layar baru dengan rekomendasi biaya saat itu, atau kamu bisa menetapkan biaya khusus sendiri — ingat, biaya baru harus lebih tinggi dari sebelumnya.

Selalu disarankan untuk menyimpan UTXO maksimal sekitar 100k sats di wallet on-chain Zeus kamu, supaya bisa digunakan untuk menambah biaya jika diperlukan.

-Tanda tangani atau verifikasi. Dengan fitur ini, kamu bisa menandatangani pesan tertentu menggunakan kunci wallet kamu. Juga bisa dipakai untuk memverifikasi pesan dan membuktikan bahwa pesan tersebut memang berasal dari kunci wallet tertentu.

-Konverter mata uang. Alat sederhana untuk menghitung konversi nilai antara BTC dan mata uang fiat lainnya.

**J - Merchandise dan Dukungan**

Di sini Kamu akan menemukan info dan tautan lebih lanjut tentang Zeus, toko online, sponsor, media sosial.

**K - Bantuan**

Pada bagian terakhir ini Kamu akan menemukan tautan ke halaman dokumentasi Zeus, masalah Github (Kalau kamu ingin mengirim bug atau permintaan langsung ke pengembang aplikasi), dukungan email.

### LANGKAH 2 - MULAI MENGGUNAKAN ZEUS NODE

Ingat, Zeus terutama digunakan sebagai LN wallet, untuk pembayaran yang cepat dan mudah lewat Lightning Network. Memang ada wallet on-chain di dalamnya, tapi wallet itu sebaiknya dipakai hanya untuk membuka atau menutup saluran LN, bukan untuk transaksi harian seperti beli kopi.

Silakan baca panduan yang lain tentang [bagaimana menjadi bank milikmu sendiri menggunakan 3 level Stash] (https://darth-coin.github.io/beginner/be-your-own-bank-en.html).

Pada saat ini pengguna memiliki 2 cara untuk mulai menggunakan Zeus:

- Langsung melalui LN, menggunakan saluran 0-conf dari Olympus LSP
- Deposit pertama di onchain Wallet dan kemudian membuka saluran LN normal dengan peer yang kamu inginkan.

#### Metode A - Menggunakan LSP Olympus

Ini adalah cara yang sangat mudah dan sederhana untuk memperkenalkan pengguna baru ke LN lewat Zeus. Penggunanya bisa saja orang yang benar-benar baru di Bitcoin dan belum punya sats sama sekali, yang sedang di-onboard oleh teman, atau pedagang baru yang ingin menerima pembayaran LN pertamanya.

Secara default, Zeus akan menggunakan LSP bawaannya, Olympus. Tapi nantinya kamu bisa beralih ke LSP lain yang mendukung protokol 0-conf untuk pembukaan saluran.

Cukup dengan membuat invoice di Zeus (masukkan jumlah dan tekan tombol “Minta”), kamu bisa langsung menerima sats.

Invoice yang kamu buat akan dibungkus (https://docs.zeusln.app/lsp/wrapped-invoices) dan akan menampilkan informasi tentang biaya layanan setelah pembayaran dilakukan. Wrapped invoice ini berisi petunjuk rute menuju node Zeus kamu, sehingga LSP bisa menemukan node baru tersebut dan membuka saluran dengan dana yang kamu setorkan.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)

Untuk mendapatkan saluran LN dari LSP dengan dana yang ingin kamu terima pertama kali, invoice ini harus dibayar dari wallet LN lain. Setelah itu, tunggu sebentar sampai LSP membuka saluran ke node Zeus kamu, memotong biaya layanan, lalu mendorong sisa pembayaran ke sisi saluran milikmu.

Yang harus kamu lakukan adalah membayar Invoice yang dihasilkan untukmu di Zeus dengan lightning Wallet, dan saluran kamu akan langsung terbuka. [Silakan baca biaya LSP Zeus] (https://docs.zeusln.app/lsp/fees).

Manfaat lain dari pembayaran untuk saluran adalah routing tanpa biaya. Artinya, saat kamu melakukan pembayaran, hop pertama yang melewati OLYMPUS by ZEUS tidak akan dikenakan biaya routing. Namun, perlu diingat bahwa hop di luar OLYMPUS by ZEUS tetap akan dikenakan biaya.

Setelah saluran siap, klik tombol di kanan bawah layar yang menampilkan saluran Zeus kamu.

![Image](assets/en/08.webp)


Dan kamu akan melihat saluran seperti ini, yang menunjukkan sisi keseimbangan saluran:


![Image](assets/en/09.webp)


Semakin banyak yang kamu belanjakan dari saluran ini, semakin besar likuiditas masuk yang kamu miliki. Sebaliknya, semakin banyak sats yang kamu terima di saluran ini, semakin sedikit ruang likuiditas masuk yang tersisa.

Berikut ini adalah demonstrasi visual sederhana yang bagus (oleh Rene Pickhardt) tentang cara kerja saluran LN:

Kamu punya satu saluran dengan Olympus, berkapasitas total 490.000 sats, dengan saldo 378.000 sats di sisi kamu dan 88.000 sats di sisi Olympus. Artinya, kamu masih bisa menerima maksimal 88k sats lagi melalui saluran yang sama.

Kalau kamu perlu menerima lebih dari 88k sats (yakni melebihi likuiditas masuk yang tersedia), misalnya 500k sats lagi, cukup buat LN invoice baru dengan jumlah tersebut, ini akan memicu permintaan pembukaan saluran baru ke LSP Olympus, sehingga kamu akan mendapatkan saluran kedua.

Untuk menghindari biaya tambahan akibat membuka terlalu banyak channel, disarankan membuka saluran yang lebih besar di awal, misalnya 1–2M sats. Setelah terbuka, kamu bisa menukar sebagian sats itu ke on-chain, misalnya 50%, menggunakan layanan swap eksternal yang dijelaskan dalam panduan ini.

Setelah kamu menukar sekitar 50% dan mengembalikan sats tersebut ke wallet on-chain Zeus kamu sendiri, kamu sudah siap lanjut ke metode berikutnya untuk membuka channel baru, yaitu dari saldo on-chain.


#### Metode B - Menggunakan saldo onchain Kamu


Dengan metode ini, kamu bisa membuka saluran ke node LN lain, termasuk ke LSP Olympus yang sama. Namun, jika kamu sudah punya saluran dengan Olympus, disarankan juga membuka saluran dengan node lain untuk meningkatkan keandalan dan memungkinkan penggunaan MPP (multi-part payment).

![Image](assets/en/10.webp)

Di atas adalah contoh pembayaran LN invoice menggunakan MPP. Seperti yang bisa kamu lihat di bagian bawah layar, terdapat menu “pengaturan” yang membuka halaman drop-down berisi detail tambahan untuk pembayaran yang akan kamu lakukan. Pada layar tersebut, jika kamu memiliki minimal dua saluran yang terbuka, fitur MPP akan aktif secara default. Kamu juga bisa mengaktifkan AMP (atomic multi-path) dan mengatur bagian tertentu sesuai kebutuhanmu. Ini fitur yang sangat berguna!

Untuk private node seperti Zeus, aku akan merekomendasikan untuk memiliki 2-3 saluran yang bagus (maksimal 4-5), dengan LSP yang bagus dan likuiditas yang baik untuk memenuhi semua kebutuhanmu untuk membayar atau menerima Sats melalui LN. [Lihat lebih banyak saran likuiditas node LN dalam panduan ini] (/nodes/managing-lightning-node-liquidity-en.html). Juga di sini [panduan umum tentang likuiditas LN] (https://Bitcoin.design/guide/how-it-works/liquidity/) dari tim Desain Bitcoin.

Memilih peer yang tepat, aku tahu, bukanlah tugas yang mudah, bahkan untuk pengguna yang berpengalaman. [Jadi aku akan memberimu beberapa opsi untuk memulai] (https://github.com/ZeusLN/zeus/discussions/2265), ini adalah daftar node peer yang sudah aku uji sendiri menggunakan Zeus (aku hanya mencoba terhubung ke node LND untuk menghindari masalah ketidakcocokan).

Berikut ini juga daftar peer node yang direkomendasikan untuk Zeus. Kalau kamu tahu node bagus lainnya, kamu bisa menambahkannya ke daftar ini.

Kamu bisa membuka saluran di Zeus dengan masuk ke tampilan Saluran, lalu klik ikon saluran di pojok kanan bawah layar utama, dan tekan ikon + di pojok kanan atas.

![Image](assets/en/11.webp)

Jika kamu ingin membuka saluran dengan node tertentu, klik (A) sudut atas untuk memindai QR nodeID node (pada Mempool, Amboss, 1ML milikmu dapat memperoleh QR tersebut) dan semua detail peer akan terisi.

PENGINGAT:

- Node embedded Zeus tidak menggunakan layanan Tor! Jadi, jangan coba membuka saluran dengan node yang berjalan di bawah Tor. Kamu justru akan merugikan diri sendiri alih-alih menambah privasi. Tor pada LN tidak memberikan privasi lebih, malah menimbulkan lebih banyak masalah.
- pilihlah dengan bijak rekan-rekan kamu, lebih baik LSP yang baik, node perutean yang baik, bukan node kampungan acak yang dapat menutup saluran kamu dan tidak dapat menawarkan likuiditas yang baik. [Di sini saya menulis panduan khusus] (https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) tentang likuiditas dan contoh node.

Jika kamu langsung mengklik tombol "Buka Saluran ke Olympus", kamu akan mengisi kolom yang diperlukan untuk membuka saluran ke [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).

Berbeda dengan saluran LSP berbayar, saluran yang kamu buka sendiri akan memerlukan konfirmasi on-chain dan menggunakan dana on-chain milikmu (kamu bisa memilih UTXO langsung dari tampilan saluran terbuka). Saluran ini tidak akan terbuka secara instan. Pastikan kamu memeriksa terlebih dahulu biaya mempool terkini dan sesuaikan dengan kebutuhan, tergantung seberapa cepat kamu ingin saluran tersebut terbuka.

Sebelum menekan tombol untuk membuka saluran, geser ke bawah untuk menampilkan opsi lanjutan.


![Image](assets/en/12.webp)


Kamu juga harus memastikan bahwa saluran yang akan dibuka tidak diumumkan (private channel). Secara default, opsi ini tidak aktif untuk saluran publik. Disarankan untuk tidak mengaktifkan opsi ini jika kamu menggunakan node tertanam Zeus, karena fitur ini hanya berguna ketika Zeus terhubung ke node jarak jauh yang berfungsi sebagai node perutean publik.

Berbeda dengan saluran LSP berbayar, membuka saluran dengan metode ini tidak memberikan keuntungan perutean tanpa biaya.

Jika semuanya sudah siap, cukup tekan tombol "Buka Saluran", lalu tunggu hingga transaksi dikonfirmasi oleh penambang. Setelah saluran terbuka, kamu bisa mulai bertransaksi menggunakan Sats di saluranmu.

Perlu diingat, saluran baru ini akan memiliki seluruh saldo di sisi kamu, artinya kamu belum memiliki likuiditas masuk. Seperti dijelaskan sebelumnya, kamu perlu menukar atau membelanjakan sebagian Sats untuk “memberi ruang” agar bisa menerima pembayaran masuk.

Bayangkan saluran Lightning Network kamu seperti segelas air:
kamu menuangkan air (Sats) ke dalam gelas kosong (saluran) hingga penuh. Kamu tidak bisa menuangkan air lagi sampai kamu meminumnya (menghabiskan atau menukar). Ketika gelas mulai kosong, kamu bisa menuangkan air lagi (menambah likuiditas masuk) menggunakan swap-in. [Baca lebih lanjut tentang layanan swap eksternal di sini](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).

Ada juga beberapa LSP (Lightning Service Provider) lain yang menawarkan saluran inbound berbayar, seperti LNBig dan Bitrefill. Kemungkinan masih ada penyedia lainnya, namun dua ini termasuk yang paling dikenal dan tepercaya.

Jika kamu membutuhkan saluran LN yang kosong sepenuhnya (dengan saldo 100% di sisi peer sejak awal), layanan seperti ini bisa menjadi solusi ideal. Dengan saluran inbound seperti ini, kamu bisa menerima lebih banyak pembayaran daripada kapasitas yang tersedia di saluran yang sudah aktif dan terisi.

Tentu, kamu perlu membayar sejumlah biaya pembukaan saluran, tetapi sebagai imbalannya kamu mendapatkan likuiditas masuk yang besar dan siap digunakan, yang sangat berguna terutama jika kamu ingin menerima pembayaran LN secara rutin tanpa menunggu likuiditas terbentuk dari aktivitas keluar.

## TIPS DAN TRIK


### Batas cadangan masuk

Saat ini, karena adanya keterbatasan teknis pada protokol Lightning Network (LN), kamu tidak dapat menerima jumlah penuh yang ditampilkan di bagian “Inbound Capacity”. Selalu ingat: ketika membuat Invoice LN, pastikan jumlah yang kamu minta lebih kecil dari “Cadangan Lokal Saluran” (Local Channel Reserve).

![Image](assets/en/13.webp)


Seperti yang bisa kamu lihat di gambar di atas, "inbound" menunjukkan kalau aku masih bisa menerima 5101 Sats, tapi sebenarnya saat ini sudah nggak mungkin menerima lebih banyak lagi. Kamu juga bisa perhatiin kalau jumlah itu sama persis dengan "cadangan lokal".

Jadi, perlu diingat, waktu kamu bikin invoice untuk menerima pembayaran, perhatikan juga likuiditas channel kamu dan kurangi cadangan lokal dari jumlah itu kalau kamu mau menerima hingga batas maksimal jumlah yang bisa masuk.


### Saran singkat untuk pengguna baru yang memulai dengan node Zeus:

-Manfaatkan saluran barumu dengan benar.

Sebagai contoh, kalau kamu tahu bakal menerima sekitar 1M Sats dalam seminggu, bukalah saluran sebesar 2M Sats dan tukarkan 50–60% dari likuiditas keluar itu ke wallet onchain atau akun kustodian LN (sementara). Selalu siap dengan lebih banyak likuiditas. Saat kamu butuh likuiditas tambahan di saluran Zeus, kamu bisa memindahkannya kembali dari akun kustodian. Kalau kamu tahu bakal mengirim sekitar 500 ribu Sats per minggu, bukalah saluran 1 juta Sats. Dengan begitu kamu masih punya cadangan sampai waktunya isi ulang lagi.

-Kalau kamu seorang pedagang dan akan selalu lebih banyak menerima daripada mengirim secara rutin, belilah saluran masuk khusus. Ini cara paling murah. Kamu cuma bayar biaya minimal dan langsung dapat saluran “kosong”.

-Jangan buka saluran kecil yang nggak berarti seperti 50–100–300–500k Sats. Itu bakal penuh dalam hitungan hari, bahkan kalau cuma dipakai buat zaps. Bukalah saluran yang lebih besar dan beragam, bukan cuma satu saluran saja. Setelah kamu buka channel yang lebih besar, kamu bisa pakai submarine swap eksternal untuk memindahkan Sats ke wallet onchain kamu (termasuk kembali ke onchain Zeus). Menjaga keseimbangan antara likuiditas masuk dan keluar itu penting, dan kamu juga bisa “menggunakan ulang” Sats tersebut buat buka lebih banyak channel kalau mau.


### Invoice yang dibungkus


Kalau kamu ingin menambah privasi saat menerima pembayaran, kamu bisa pakai metode “wrapped invoice”. Pengingat: untuk melakukan ini, kamu perlu punya saluran dengan Olympus LSP. Invoice yang dibungkus akan “menyembunyikan” tujuan akhir (node Zeus kamu) dan menampilkan node LSP kamu sebagai tujuan bagi pengirim.

Untuk mendapatkan invoice yang sudah dibungkus, buka layar keypad utama, masukkan jumlah yang mau kamu terima, lalu tekan request. Akan muncul kode QR biasa untuk invoice kamu. Sekarang, klik tombol “X” di kanan atas, dan kamu akan diarahkan ke opsi tambahan untuk invoice tersebut.

![Image](assets/en/14.webp)

Sekarang kamu perlu mengaktifkan opsi di atas tulisan “Aktifkan LSP”, lalu tekan tombol “Buat Invoice”. Opsi ini akan membuat invoice yang sudah dibungkus, dan ingat, fitur ini akan mengenakan sedikit biaya.

### Faktur dengan petunjuk rute

Ini adalah fitur yang sangat berguna kalau kamu ingin mengelola likuiditas dari beberapa saluran masuk. Secara praktis, kamu bisa menentukan saluran masuk mana yang ingin kamu gunakan untuk menerima Sats dari invoice.

Fitur ini juga bisa dipakai untuk circular rebalancing, yaitu saat kamu ingin memindahkan likuiditas dari satu saluran yang sudah penuh ke saluran lain yang masih kosong.

Lalu, bagaimana cara membuat invoice dengan petunjuk rute?



- Pada layar utama, geser ke kanan laci LN dan klik "Terima"
- Dalam pengaturan Invoice, masuk ke bagian bawah dan aktifkan tombol "Sisipkan petunjuk rute", kemudian pilih tab "Custom". Ini akan membuka layar dengan semua saluran yang tersedia. Pilih salah satu yang ingin kamu terima.
- Isi semua detail Invoice lainnya, jumlah, memo, dan lain-lain dan klik "buat Invoice".
- Membayar Invoice tersebut akan membawa Sats ke saluran yang ditunjukkan.


Jika kamu ingin membayar Invoice (penyeimbangan melingkar), ketika kamu membayarnya dari node Zeus yang sama, di layar pembayaran, pilih saluran keluar (yang memiliki lebih banyak likuiditas) yang ingin kamu gunakan sebagai pengirim pembayaran.


### Bayar dengan Keysend


Keysend adalah fitur LN yang sangat diremehkan dan pengguna harus lebih sering menggunakannya.

[Keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) memungkinkan pengguna di Lightning Network untuk mengirim pembayaran kepada orang lain, langsung ke kunci publik mereka, selama node mereka memiliki saluran publik dan mengaktifkan keysend. Keysend tidak mengharuskan penerima pembayaran untuk mengeluarkan Invoice.

Jadi, bagaimana kamu melakukannya dengan Zeus?

Cukup pindai atau salin nodeID tujuan (atau gunakan kontak Zeus untuk menyimpan node tujuan reguler kamu sebagai kontak) dan kemudian dari layar utama Zeus, klik tombol "Kirim". Pada layar tersebut kemudian tempelkan nodeID atau pilih dari kontak kamu.

Masukkan jumlah Sats, pesan jika diperlukan (ya, kamu juga dapat menggunakannya sebagai obrolan rahasia melalui LN) dan klik tombol "Kirim". Selesai!


![Image](assets/en/15.webp)

Kalau kamu punya saluran langsung dengan rekan tujuan, maka TIDAK akan ada biaya yang dikenakan.

Tapi kalau kamu nggak punya saluran langsung dengan peer tujuan, pembayaran keysend akan tetap membayar biaya seperti pembayaran LN invoice biasa, yang dirutekan lewat jalur reguler seperti transaksi lainnya. Hanya saja, ingat, pembayaran ini nggak akan meninggalkan jejak apa pun sebagai LN invoice.

## Kesimpulan


Aku sarankan untuk membaca panduan tindak lanjut [Penggunaan lanjutan Zeus] (https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) dengan lebih banyak instruksi dan kasus penggunaan.


Dan… selesai! Mulai sekarang kamu bisa langsung pakai Zeus Node sebagai wallet BTC/LN biasa di ponselmu. Tampilan antarmukanya sederhana, mudah digunakan, dan cukup intuitif untuk semua jenis pengguna, jadi aku rasa nggak perlu lagi dijelaskan panjang lebar soal cara mengirim atau menerima pembayaran.

Sebagai penutup, berikut ini bagan perbandingan privasi:


![Image](assets/en/16.webp)
