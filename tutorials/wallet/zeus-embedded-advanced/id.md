---
name: Zeus Tertanam - Lanjutan
description: Kustodian mandiri multi-simpul Wallet
---

![Zeus](assets/cover.webp)


## Pengantar ZEUS Wallet


ZEUS adalah aplikasi seluler Bitcoin Wallet dan manajemen node dengan fungsionalitas penuh dari Bitcoin lightning Wallet yang membuat pembayaran Bitcoin menjadi sederhana, memberikan pengguna kontrol penuh atas keuangan mereka, dan memungkinkan pengguna yang lebih mahir untuk mengelola node Lightning mereka dari telapak tangan mereka.


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
- Multi node / akun didukung (Anda dapat mengelola node rumah Anda sendiri, menjalankan node LND yang tertanam, terhubung ke beberapa akun LNDhub)
- Menu aktivitas yang mudah digunakan
- Enkripsi PIN atau passphrase, mode Privasi - sembunyikan data sensitif Anda
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

Untuk dapat menggunakan Zeus dan mengelola saluran Lightning, likuiditas, biaya, dan lain-lain, lebih baik Anda membaca terlebih dahulu beberapa panduan penting tentang Lightning Network.


#### Panduan:


- [LND - Dokumentasi Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Dokumentasi Petir Inti] (https://lightning.readthedocs.io/index.html)
- [Panduan Petir Pemula] (https://bitcoiner.guide/lightning/) - oleh Bitcoin Tanya Jawab
- [Manajemen Simpul Petir](https://www.lightningnode.info/) - oleh openoms
- [Lightning Network dan analogi bandara](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Mengelola Likuiditas Simpul Petir](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Pemeliharaan Simpul Petir](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Video tutorial oleh Sesi BTC


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Panduan panduan bagaimana cara mulai menggunakan node tertanam Zeus LN pada perangkat seluler Anda


![Image](assets/en/01.webp)


Saya mendedikasikan panduan ini untuk semua pengguna Lightning Network (LN) baru yang ingin memulai perjalanan berdaulat baru dengan menggunakan node tahanan mandiri Wallet pada perangkat seluler mereka.


Anggap saja Anda sudah melewati semua dompet LN kustodian, tetapi Anda belum siap untuk mulai menjalankan node LN perutean PUBLIC, Anda hanya ingin menumpuk lebih banyak Sats di atas LN dengan cara yang lebih self-custodial dan melakukan pembayaran reguler melalui LN.


Ini dia Zeus, dimulai dengan [versi v0.8.0 yang diumumkan di blog mereka] (https://blog.zeusln.com/new-release-zeus-v0-8-0/), sekarang menawarkan node LND yang disematkan ke dalam aplikasi. Sampai saat ini Zeus adalah aplikasi manajemen node jarak jauh + akun LNDhub. Tetapi sekarang... node ada di dalam ponsel!


![Image](assets/en/02.webp)


### Rekap cepat fitur-fitur utama untuk Zeus Node:



- Node LND privat** - Itu berarti node ini TIDAK akan melakukan perutean publik untuk pembayaran orang lain melalui node Anda. Node dan salurannya tidak diumumkan (privat, tidak terlihat pada grafik LN publik). Untuk menerima dan melakukan pembayaran akan dilakukan melalui rekan-rekan LSP Anda yang terhubung. INGAT: Zeus Embedded Node TIDAK akan melakukan perutean publik!
- Layanan LND yang persisten** - pengguna dapat mengaktifkan fitur ini dan menjaga layanan LND tetap aktif secara terus menerus seperti halnya node LN biasa. Aplikasi tidak harus dibuka, layanan persisten akan menjaga semua komunikasi tetap online.
- Filter blok Neutrino** - sinkronisasi blok dilakukan dengan menggunakan [filter blok dan protokol Neutrino] (https://bitcoinops.org/en/topics/compact-block-filters/) (tidak ada informasi tentang dana On-Chain pengguna kami). Pengingat: untuk koneksi internet dengan latensi tinggi/lambat, sinkronisasi blok berdasarkan neutrino ini terkadang bisa gagal. Mencoba beralih ke server yang dekat dengan neutrino dapat membantu memulihkan sinkronisasi. Tanpa sinkronisasi ini, node LND Anda tidak akan dapat dimulai!
- Saluran Taproot Sederhana** - Ketika menutup saluran ini, pengguna dikenakan biaya yang lebih rendah dan diberikan privasi yang lebih besar karena mereka terlihat seperti pengeluaran Taproot lainnya ketika memeriksa jejak On-Chain mereka.
- LSP terintegrasi** - Olympus adalah node LSP baru untuk Zeus. Pengguna dapat menerima kembali Sats melalui LN secara langsung, tanpa harus mengatur saluran LN sebelumnya. Cukup dengan membuat LN Invoice dan membayar dari LN Wallet lainnya, dengan layanan saluran Zeus 0-conf. Baca lebih lanjut tentang Zeus LSP di sini. LSP juga memberikan privasi tambahan kepada pengguna kami dengan menyediakan faktur yang dibungkus yang menyembunyikan kunci publik node mereka dari pembayar.
- Buku Kontak** - Anda dapat menyimpan kontak secara manual atau mengimpor dari NOSTR, untuk memudahkan pengiriman pembayaran ke tujuan reguler Anda.
- Dukungan penuh untuk LNURL, pengiriman dan penerimaan LN Address** - sekarang Anda dapat mengatur kustodian mandiri LN Address Anda sendiri dengan @zeuspay.com. Pengingat: Anda juga dapat menggunakan Zeus untuk autentikasi LN di situs-situs yang memungkinkan Anda masuk dengan autentikasi LN. Sangat praktis.
- Point of Sale** - Sekarang pengguna pedagang dapat mengatur item produk mereka sendiri dan menjual langsung dari Zeus, dengan PoS yang terintegrasi. Untuk saat ini berisi kebutuhan dasar tetapi di masa depan akan berisi fitur-fitur yang diperluas.
- Log LND** - pengguna dapat membaca secara real time log layanan LND dan menggunakannya untuk men-debug masalah yang mungkin terjadi (terutama untuk koneksi yang buruk)
- Pencadangan Otomatis** - saluran node LN secara otomatis dicadangkan di server Olympus. Pencadangan otomatis ini dienkripsi dengan node Wallet seed Anda (tanpa seed sama sekali tidak berguna). Pengguna juga dapat mengekspor secara manual SCB (cadangan saluran statis) untuk pemulihan bencana.


### Cara bergabung dengan Zeus LN Node (LND tertanam)


Dalam panduan ini saya hanya akan membahas tentang node LND yang tertanam, dan bukan tentang cara lain untuk menggunakan aplikasi yang luar biasa ini (manajemen node jarak jauh dan akun LNDhub). Untuk jenis koneksi lainnya, silakan merujuk ke [halaman Zeus Docs] (https://docs.zeusln.app/category/getting-started), yang dijelaskan dengan sangat baik dan tidak perlu menulis panduan khusus.


#### LANGKAH 1 - PENGATURAN AWAL


Karena Zeus adalah node LND penuh, saya akan memberikan beberapa rekomendasi awal:



- Jangan gunakan perangkat lama, karena dapat mempengaruhi penggunaan aplikasi canggih ini. Terutama pada periode sinkronisasi, aplikasi ini dapat menggunakan CPU dan RAM secara intensif. Kurangnya hal ini bahkan bisa membuat aplikasi Zeus tidak bisa digunakan.
- Gunakan setidaknya Android 11 sebagai OS seluler dan perbarui sebanyak mungkin. Untuk iOS juga demikian, cobalah untuk menggunakan versi OS yang lebih tinggi.
- Anda akan membutuhkan setidaknya 1GB ruang disk untuk penyimpanan data. Seiring berjalannya waktu dapat bertambah lebih banyak, tetapi ada fungsi untuk memadatkan basis data ke tingkat MB.
- TIDAK perlu menggunakan Zeus dengan layanan Tor atau Orbot. Tolong jangan memperumit masalah lebih dari yang diperlukan. Tor dalam hal ini tidak akan menawarkan Anda lebih banyak privasi tetapi hanya memperburuk keadaan untuk sinkronisasi awal. Juga berhati-hatilah dengan VPN apa yang Anda gunakan dan periksa latensi koneksi menuju server neutrino. Perlu diingat, filter blokir Neutrino tidak membocorkan atau melacak identitas perangkat Anda, hanya melayani blokir. Lalu lintas LN juga berada di belakang LSP dengan kanal privat sehingga sangat sedikit informasi yang keluar, tidak ada alasan untuk panik tentang privasi.
- Bersabarlah untuk sinkronisasi awal, bisa memakan waktu beberapa menit. Usahakan untuk terhubung ke koneksi internet broadband dengan latensi yang baik. Jika Anda menjalankan node Bitcoin Anda sendiri, [Anda dapat mengaktifkan layanan neutrino] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) dan menghubungkan Zeus Anda ke node Anda sendiri, bahkan menggunakan LAN internal, sehingga Anda akan mendapatkan kecepatan maksimum.


Setelah Anda mengatur jenis koneksi "Node tertanam", aplikasi akan mulai menyinkronkan untuk sementara waktu. Tunggu dengan sabar untuk menyelesaikan bagian tersebut, lalu masuk ke halaman Pengaturan utama.


![Image](assets/en/03.webp)


Secara singkat, mari kita selami masing-masing bagian Pengaturan dan memahami beberapa fitur utama, sebelum Anda mulai menggunakan Zeus:


**A - PENGATURAN**


Ini adalah bagian dengan pengaturan umum untuk seluruh aplikasi


**1 - Penyedia Layanan Petir (LSP) **


Di sini disajikan dua layanan LSP:



- saluran _Just in time_ - ketika Anda tidak memiliki saluran terbuka atau likuiditas masuk yang tersedia, jika layanan ini diaktifkan, layanan ini akan membuka saluran dengan cepat untuk Anda. Opsi ini dapat dinonaktifkan jika Anda tidak ingin membuka lebih banyak saluran jenis ini.
- meminta saluran terlebih dahulu_ - Anda dapat membeli saluran masuk dari LSP Olympus secara langsung di aplikasi dengan berbagai opsi dan jumlah (untuk masuk dan keluar).


LSP membantu menghubungkan pengguna ke Lightning Network dengan membuka saluran pembayaran ke node mereka. [Baca lebih lanjut tentang LSP di sini] (https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS memiliki LSP baru yang terintegrasi ke dalamnya yang disebut [OLYMPUS by ZEUS] (https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), yang tersedia untuk semua pengguna yang menggunakan node tertanam yang baru.


Pada bagian ini, secara default adalah LSP Olympus (https://0conf.lnolymp.us), tetapi Anda juga dapat mengatur LSP 0conf lain yang mendukung protokol ini.


perlu diingat:_

ketika Anda membuka saluran dengan Olympus LSP menggunakan faktur LN yang dibungkus, Anda juga akan mendapatkan likuiditas masuk sebesar 100 ribu! Ini adalah opsi yang sangat bagus jika Anda perlu menerima lebih banyak Sats._

contoh: Anda menyetor 400k Sats untuk membuka saluran LSP, maka LSP akan membuka saluran berkapasitas 500k Sats ke node Zeus Anda dan mendorong 400k Sats yang Anda setorkan ke sisi Anda

"Likuiditas masuk" = lebih banyak "ruang" di saluran Anda untuk menerima


Di masa depan, kami berharap kami dapat memiliki banyak LSP lain yang dapat diintegrasikan ke dalam Zeus dan menggunakan masing-masing LSP sebagai alternatif. Hanya masalah waktu sampai LSP baru akan mengadopsi standar terbuka untuk saluran 0conf semacam ini.


Jika Anda tidak ingin membuka saluran baru "dengan cepat", Anda dapat menonaktifkan opsi ini.


Pada bagian yang sama, Anda juga memiliki opsi untuk memilih "request Simple Taproot Channels" ketika LSP akan membuka saluran menuju node Zeus Anda. Saluran Taproot Sederhana ini menawarkan privasi On-Chain yang lebih baik dan biaya yang lebih rendah pada penutupan saluran. Hanya ada dua alasan mengapa Anda tidak ingin menggunakannya:



- Mereka masih baru, dan mungkin masih ada bug di LND saat menggunakannya.
- Rekanan Anda tidak mendukungnya. Bahkan node LND harus secara eksplisit memilihnya, untuk saat ini.


**2 - Pengaturan pembayaran**


Fitur ini akan menawarkan Anda cara untuk mengatur biaya yang Anda inginkan untuk pembayaran, melalui LN atau onchain. Juga menyediakan opsi untuk menambah atau mengurangi batas waktu untuk faktur Anda.


Jika beberapa pembayaran LN Anda gagal, Anda dapat meningkatkan biaya untuk menemukan rute yang lebih baik. Juga jika Anda melakukan onchain txs, Anda dapat mengatur biaya tertentu sehingga tx Anda tidak akan terjebak di Mempool untuk waktu yang lama, jika terjadi periode biaya yang tinggi.


**3 - Pengaturan faktur**


Pada bagian ini terdapat beberapa opsi untuk faktur generate:



- Mengatur memo standar yang akan ditampilkan di Invoice Anda generate
- Waktu kedaluwarsa dalam hitungan detik, jika Anda menginginkan waktu tertentu, lebih lama atau lebih singkat untuk pembayaran Invoice Anda
- Sertakan petunjuk rute - berikan informasi untuk menemukan saluran yang tidak diiklankan, atau saluran pribadi. Hal ini memungkinkan perutean pembayaran ke node yang tidak terlihat secara publik di jaringan. Petunjuk perutean menyediakan rute parsial antara node privat penerima dan node publik. Petunjuk perutean ini kemudian disertakan dalam Invoice yang dihasilkan oleh penerima dan diberikan kepada pembayar. Saya menyarankan untuk mengaktifkannya secara default, jika tidak, pembayaran yang masuk bisa gagal (tidak ada rute yang ditemukan).
- AMP Invoice - Pembayaran Multi Jalur Atomik adalah jenis pembayaran Lightning baru yang diimplementasikan oleh LND yang memungkinkan untuk menerima Sats tanpa Invoice tertentu, menggunakan [keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Praktis merupakan kode pembayaran statis. [Baca lebih lanjut di sini] (https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Tampilkan bidang gambar awal khusus - gunakan opsi ini hanya dalam kasus yang sangat spesifik ketika Anda benar-benar ingin menggunakan bidang khusus dalam gambar awal. [Baca selengkapnya di sini](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Pilihan lain di bagian ini adalah bagaimana mengatur jenis onchain Address yang ingin Anda gunakan: SegWit bersarang, SegWit, Taproot.


![Image](assets/en/04.webp)


Klik pada tombol roda atas dan layar popup akan muncul untuk memilih tipe Address yang diinginkan. Setelah Anda mengaturnya, pada saat Anda menekan tombol terima untuk onchain, itu akan menjadi generate tipe Address yang dipilih. Anda dapat mengubahnya kapan saja.


**4 - Pengaturan saluran**


Di bagian ini Anda dapat mengatur beberapa fitur saluran pembuka, seperti:



- jumlah konfirmasi
- Umumkan saluran (secara default tidak aktif), artinya saluran tersebut akan menjadi saluran yang tidak diumumkan
- Saluran Taproot Sederhana
- Tampilkan tombol pembelian saluran


**5 - Pengaturan privasi**


Di sini Anda akan menemukan beberapa pengaturan dasar untuk menambahkan lebih banyak privasi menggunakan aplikasi Zeus:



- Block explorer untuk membuka rincian tx (Mempool.space, blockstream.info atau yang bersifat pribadi)
- Baca papan klip - sakelar aktif/nonaktif jika Anda ingin Zeus membaca papan klip perangkat Anda
- Mode Lurker - sakelar aktif/nonaktif jika Anda ingin menyembunyikan info sensitif tertentu dari aplikasi Zeus Anda. Pilihan yang bagus ketika Anda membuat demo atau tangkapan layar.
- Saran biaya Mempool - aktifkan opsi ini jika Anda ingin menggunakan tingkat biaya yang disarankan dari [Mempool.space](https://Mempool.space/)


**6 - Keamanan**


Bagian ini hanya memiliki dua opsi untuk mengamankan aplikasi saat dibuka: atur kata sandi atau PIN.


Setelah Anda mengatur PIN untuk membuka aplikasi, Anda juga dapat mengatur "PIN darurat". PIN tambahan rahasia ini HANYA akan digunakan dalam situasi paksaan, jika Anda terancam. Jika Anda memasukkan PIN ini, semua konfigurasi akan terhapus. Jadi, sebaiknya Anda terus memperbarui cadangan Anda. Pencadangan otomatis diaktifkan secara default, tetapi ada baiknya Anda juga memiliki cadangan sendiri, di luar perangkat.


**7 - Mata Uang**


Mengaktifkan atau menonaktifkan opsi untuk menampilkan konversi mata uang fiat dalam penggunaan aplikasi Zeus. Saat ini mendukung lebih dari 30 mata uang fiat di seluruh dunia.


**8 - Bahasa**


Anda dapat beralih di antara beberapa bahasa terjemahan, yang ditinjau oleh komunitas Zeus dengan penutur asli.


**9 - Tampilan**


Pada bagian ini Anda dapat mempersonalisasi tampilan Zeus Anda, memilih berbagai tema warna, layar default (keypad atau balance), menampilkan alias node Anda, mengaktifkan tombol keypad yang besar, menampilkan lebih banyak angka desimal.


**10 - Tempat Penjualan**


Ini adalah fitur khusus untuk mengaktifkan/menonaktifkan sistem PoS yang terintegrasi ke dalam Zeus. Anda dapat menjalankan PoS mandiri atau terhubung ke sistem PoS Square. Saat ini mendukung fungsi dasar sebagai PoS, tetapi cukup untuk awal yang baik dan dapat membantu para pedagang kecil (bar/restoran, toko kelontong) untuk mulai menerima BTC dengan cara asli.


Di dalam pengaturan ini, Anda akan menemukan berbagai opsi untuk mengatur PoS Anda:



- Jenis pembayaran konfirmasi: Hanya LN, 0-konf, 1-konf
- Mengaktifkan/menonaktifkan tips untuk karyawan yang mengoperasikan PoS
- Tampilkan / sembunyikan keypad
- Persentase pajak yang berlaku pada tiket
- Membuat produk dan kategori produk
- Daftar sederhana dari semua penjualan


Berikut ini adalah video demo langsung cara menggunakan Zeus PoS:


*b - Cadangan Wallet** *B - Cadangan Wallet


Node yang tertanam di ZEUS didasarkan pada LND dan menggunakan [format aezeed seed] (https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Ini berbeda dengan [format BIP39] (https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) yang biasa Anda lihat pada kebanyakan dompet Bitcoin, walaupun mungkin terlihat mirip. Aezeed menyertakan beberapa data tambahan termasuk tanggal lahir Wallet yang akan membantu pemindaian ulang selama pemulihan menjadi lebih efisien.


Format kunci aezeed harus kompatibel dengan dompet seluler berikut ini: Blixt, BlueWallet dan Breez. Harap diperhatikan bahwa seed saja tidak akan cukup untuk memulihkan semua saldo Anda jika Anda memiliki saluran yang terbuka atau tertunda untuk ditutup!


Pelajari lebih lanjut tentang proses pencadangan dan pemulihan di [halaman Dokumen Zeus](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


SARAN DAYA: Ketika Anda menyimpan seed Anda, harap simpan juga node pubkey! Kadang-kadang ada baiknya untuk memilikinya, bersama dengan seed dan SCB (Cadangan Saluran Statis) Anda untuk berjaga-jaga jika Anda perlu memverifikasi pemulihan.


SCB hanya diperlukan jika Anda memiliki saluran LN yang terbuka. Jika Anda hanya memiliki dana onchain, tidak diperlukan.


Jika Anda melihat bahwa setelah sekian lama masih belum menampilkan txs riwayat lama, buka Embedded node - Peers dan nonaktifkan opsi untuk menggunakan daftar peer yang dipilih (secara default adalah btcd.lnolymp.us). Ini akan memicu restart dan akan terhubung ke node neutrino pertama yang tersedia dengan respons waktu yang lebih baik. Atau gunakan peers neutrino terkenal lainnya yang disebutkan di bawah ini.


Jika Anda ingin melihat lebih banyak opsi pemulihan untuk node LND, [silakan baca panduan saya sebelumnya] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), di mana Anda dapat menemukan langkah-langkah cara mengimpor aezeed seed ke dalam Sparrow Wallet atau metode lainnya.


**C - Node Tertanam**


Pada bagian ini kita akan menemukan beberapa alat dasar untuk mengelola node terintegrasi:



- pemulihan Bencana_ - Pencadangan otomatis dan manual untuk saluran LN. Silakan baca lebih lanjut cara menggunakan fitur ini di halaman Dokumen Zeus.
- _Express Graph Sync_ - Aplikasi Zeus akan mengunduh grafik data gosip LN dari server khusus, untuk sinkronisasi yang lebih cepat dan lebih baik, menawarkan jalur pembayaran terbaik. Anda juga dapat memilih untuk menghapus data grafik sebelumnya pada saat pengaktifan.
- _Peers_ - bagian untuk mengelola neutrino peers dan 0-conf peers. Jika Anda mengalami masalah dengan sinkronisasi awal, saluran tidak online, itu karena perangkat Anda memiliki latensi tinggi dengan peer neutrino yang dikonfigurasi. Coba ganti daftar peer yang disukai atau tambahkan peer spesifik Anda yang Anda tahu memiliki latensi yang lebih baik untuk sinkronisasi. Server neutrino yang terkenal adalah:



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



- log _LND_ - alat yang sangat berguna untuk men-debug masalah node LN Anda dan mengontrol secara mendalam apa yang terjadi dengan tingkat yang lebih teknis.
- pengaturan lanjutan_ - lebih banyak alat untuk mengontrol penggunaan node LND Anda:



 - mode _Pathfinding_ - bimodal atau apriori, cara untuk menemukan rute yang lebih baik untuk pembayaran LN Anda dan juga mengatur ulang informasi rute sebelumnya. Silakan baca panduan yang sangat bagus ini tentang pencarian jalur: [Pathfinding] (https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - oleh Docs Lightning Engineering dan [LN Payment Pathfinding] (https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - oleh Voltage
 - _Persistent LND_ - aktifkan mode ini jika Anda ingin layanan LND berjalan terus menerus di latar belakang dan menjaga node Anda tetap online 24/7. Ini sangat berguna jika Anda menggunakan Zeus sebagai PoS di toko kecil atau Anda menerima banyak tip LN melalui LN Address.
 - _Rescan wallet_ - opsi ini akan memicu pemindaian penuh pada saat restart dari semua txs onchain Wallet Anda. Aktifkan hanya jika Anda kehilangan beberapa txs di Wallet Anda. Proses pemindaian ulang akan memakan waktu, beberapa menit, jadi bersabarlah dan selalu periksa log untuk melihat detail lebih lanjut mengenai perkembangannya.
 - _Compact Database_ - opsi ini sangat berguna jika aplikasi Zeus Anda menggunakan banyak ruang perangkat (lihat detail aplikasi di pengaturan perangkat Anda). Jika Anda memiliki banyak aktivitas menggunakan Zeus, saya sarankan untuk melakukan pemadatan ini lebih sering. Setelah Anda melihat bahwa Anda memiliki lebih dari 1-1,5GB data untuk aplikasi Zeus, lakukan pemadatan. Proses ini akan dimulai ulang dan memakan waktu, jadi bersabarlah.
 - _Delete Neutrino files_ - opsi ini untuk menghapus file neutrino (dengan restart) akan mengurangi banyak penggunaan penyimpanan data. Mengurangi penggunaan data juga berdampak besar pada penggunaan baterai, mengurangi penggunaan baterai, terutama jika Anda menggunakan Zeus dalam mode persisten.


**D - Info Simpul**


Di bagian ini, Anda akan menemukan detail lebih lanjut tentang status node Zeus Anda sebagai:



- Alias - ID simpul pendek
- Public Key - kunci publik lengkap untuk node Anda yang diperlukan oleh node lain untuk menemukan jalur menuju node Anda. Ingatlah bahwa pubkey ini TIDAK terlihat pada LN Explorer biasa (Mempool, Amboss, 1ML, dll). Pubkey ini HANYA dapat dijangkau melalui rekan-rekan dan saluran LN Anda yang terhubung.
- Versi implementasi LN
- Versi aplikasi Zeus
- Status Synced to chain dan Synced to graph - status yang sangat penting, yang menunjukkan status node Anda yang benar. Jika keduanya tidak menampilkan "true", itu berarti node Anda masih melakukan sinkronisasi atau mengalami beberapa masalah dalam sinkronisasi. Jadi disarankan untuk melihat ke dalam log LND Anda atau tunggu sebentar.
- Tinggi blok dan Hash - menunjukkan blok terakhir dan Hash yang dilihat dan disinkronkan oleh node Anda.


**E - Info Jaringan**


Bagian ini menampilkan rincian lebih lanjut tentang status umum untuk Lightning Network, yang diekstrak dari data sinkronisasi grafik Anda: jumlah saluran publik yang tersedia, jumlah node, jumlah saluran zombie (offline atau mati), diameter grafik, rata-rata dan derajat maksimal untuk grafik.


Data informasi ini dapat berguna untuk melakukan debug atau hanya digunakan untuk statistik.


*f - Petir Address** *F - Petir Address


Pada bagian ini pengguna dapat mengatur sendiri penitipan uangnya LN Address @zeuspay.com.


ZEUS PAY memanfaatkan hash preimage yang dibuat oleh pengguna, faktur HODL, dan skema pengesahan Zaplocker Nostr untuk memungkinkan pengguna yang mungkin tidak online 24/7 untuk menerima pembayaran ke Address petir statis. Pengguna hanya perlu masuk ke dompet ZEUS mereka dalam waktu 24 jam untuk mengklaim pembayaran, jika tidak, pembayaran akan dikembalikan ke pengirim.


Jika Anda mengaktifkan "mode persisten", semua pembayaran ke LN Address Anda akan langsung diterima.


Pelajari tentang cara kerja pembayaran [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) dan lebih lanjut tentang [Biaya ZeusPay di sini](https://docs.zeusln.app/lightning-Address/fees).


**G - Alamat Onchain**


Di bagian ini Anda dapat melihat alamat onchain yang Anda hasilkan untuk kontrol koin yang lebih baik


**H - Kontak**


Buku kontak baru diperkenalkan di Zeus v 0.8.0 yang dapat Anda gunakan untuk mengirim pembayaran dengan cepat ke teman dan keluarga Anda, juga dengan kemampuan untuk mengimpor kontak Anda dari Nostr.


Cukup masukkan npub Nostr Anda atau NIP-05 Address yang dapat dibaca manusia, dan ZEUS akan menanyakan Nostr untuk semua kontak Anda. Dari sana Anda dapat mengirimkan pembayaran cepat ke kontak, atau mengimpor semua atau beberapa kontak ke buku kontak lokal Anda./<


Berikut ini adalah video singkat tentang cara mengonfigurasi dan menggunakan kontak Zeus Anda:


**I - Alat**


Di sini kami memiliki berbagai sub-bagian dengan lebih banyak alat:



- akun_ - di sini Anda dapat mengimpor akun/dompet eksternal, dompet Cold, dompet Hot, untuk mengontrol atau digunakan sebagai sumber pendanaan eksternal untuk saluran node Zeus Anda. Fitur ini masih dalam tahap percobaan.
- mempercepat transaksi_ - Fitur ini dapat membantu ketika Anda memiliki tx yang macet ke dalam Mempool dan ingin menaikkan biaya. Anda harus memberikan output tx dari detail tx dan memilih biaya baru yang ingin Anda gunakan. Harus lebih tinggi dari yang sebelumnya dan mengharuskan Anda memiliki lebih banyak dana yang tersedia di onchain Wallet Anda.


![Image](assets/en/05.webp)


Anda harus pergi ke tx yang tertunda dan menyalin titik keluar txid. Kemudian masuk ke bagian ini dan tempelkan, lalu pilih biaya baru yang ingin Anda gunakan untuk menabraknya. Ini akan memunculkan layar baru dengan biaya yang direkomendasikan pada saat itu, atau Anda dapat mengatur biaya khusus. Ingat HARUS lebih tinggi dari yang sebelumnya.


Selalu lebih baik untuk menyimpan UTXO dengan maksimum 100k Sats di Zeus onchain Wallet Anda, agar dapat menggunakannya untuk menambah biaya ketika diperlukan.



- tanda tangani atau verifikasi_ - Dengan fitur ini Anda dapat menandatangani pesan tertentu dengan kunci Wallet Anda. Juga dapat digunakan untuk memverifikasi pesan untuk membuktikan bahwa pesan tersebut berasal dari kunci Wallet tertentu.
- konverter mata uang - alat sederhana untuk menghitung konversi kurs antara BTC dan mata uang fiat lainnya.


**J - Merchandise dan Dukungan**


Di sini Anda akan menemukan info dan tautan lebih lanjut tentang Zeus, toko online, sponsor, media sosial.


**K - Bantuan**


Pada bagian terakhir ini Anda akan menemukan tautan ke halaman dokumentasi Zeus, masalah Github (jika Anda ingin mengirim bug atau permintaan langsung ke pengembang aplikasi), dukungan email.



### LANGKAH 2 - MULAI MENGGUNAKAN ZEUS NODE



Ingat, Zeus terutama digunakan sebagai LN Wallet, untuk pembayaran yang mudah dan cepat melalui LN. Tentu saja, ini juga berisi onchain Wallet, tetapi yang satu itu harus digunakan secara eksklusif untuk membuka / menutup saluran LN dan bukan untuk pembayaran kopi biasa.


Silakan baca panduan saya yang lain tentang [bagaimana menjadi bank Anda sendiri menggunakan 3 level Stash] (https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


Pada saat ini pengguna memiliki 2 cara untuk mulai menggunakan Zeus:



- Langsung melalui LN, menggunakan saluran 0-conf dari Olympus LSP
- Deposit pertama di onchain Wallet dan kemudian membuka saluran LN normal dengan peer yang Anda inginkan.


#### Metode A - Menggunakan LSP Olympus


Ini adalah cara yang sangat mudah dan sederhana untuk memasukkan pengguna baru LN ke Zeus. Ini bisa berupa pengguna Bitcoin yang benar-benar baru dan belum memiliki Sats sama sekali, yang di-'onboarding' oleh teman, atau pedagang baru yang memulai pembayaran LN pertamanya.


Secara default, Zeus akan menggunakan LSP-nya sendiri, Olympus. Tetapi nantinya Anda juga dapat beralih ke LSP lain yang mendukung protokol 0-conf untuk membuka saluran.


Hanya dengan membuat Invoice di Zeus Anda (masukkan jumlah dan klik tombol "minta"), Anda akan dapat langsung menerima Sats tersebut.


Invoice yang Anda miliki akan dibungkus (https://docs.zeusln.app/lsp/wrapped-invoices) dan Anda akan mendapatkan informasi mengenai biaya yang terkait dengan layanan ini jika sudah dibayar. Invoice yang dibungkus ini berisi petunjuk rute menuju node Zeus Anda, sehingga LSP dapat menemukan node baru Anda dan membuka saluran dengan dana baru yang Anda setorkan.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Untuk mendapatkan saluran LN dari LSP dengan dana yang ingin Anda terima pertama kali, Invoice ini harus dibayar dari LN Wallet lainnya dan tunggu beberapa saat hingga LSP membuka saluran ke arah node Zeus Anda, kurangi biayanya dan dorong sisa pembayaran ke sisi saluran Anda.


Yang harus Anda lakukan adalah membayar Invoice yang dihasilkan untuk Anda di ZEUS dengan lightning Wallet, dan saluran Anda akan langsung terbuka. [Silakan baca biaya LSP Zeus] (https://docs.zeusln.app/lsp/fees).


Manfaat lain dari pembayaran untuk saluran adalah perutean tanpa biaya. Hal ini berarti ketika melakukan pembayaran routing, hop pertama melalui OLYMPUS by ZEUS tidak dikenakan biaya routing. Harap diperhatikan, bahwa hop di luar OLYMPUS by ZEUS akan tetap dikenakan biaya.


Setelah saluran siap, klik tombol kanan di bagian bawah layar yang menampilkan saluran Zeus.


![Image](assets/en/08.webp)


Dan Anda akan melihat saluran seperti ini, yang menunjukkan sisi keseimbangan saluran Anda:


![Image](assets/en/09.webp)


Semakin banyak yang akan Anda belanjakan dari saluran ini, semakin banyak likuiditas masuk yang akan Anda miliki. Semakin banyak Sats yang akan Anda terima di saluran ini, semakin sedikit ruang likuiditas masuk yang Anda miliki.


Berikut ini adalah demonstrasi visual sederhana yang bagus (oleh Rene Pickhardt) tentang cara kerja saluran LN:


Pada saat ini, dengan mempertimbangkan layar demo untuk saluran, klik pada nama saluran dan Anda akan melihat detail lebih lanjut tentang saluran tersebut.


Anda memiliki satu saluran dengan Olympus, dengan kapasitas total 490.000 Sats, dengan keseimbangan 378.000 Sats di sisi Anda dan 88.000 Sats di sisi Olympus. Itu berarti Anda dapat menerima maksimum 88k Sats lebih banyak di saluran yang sama.


Jika Anda perlu menerima lebih dari 88k Sats (likuiditas masuk yang tersedia dalam kasus ini), katakanlah 500k Sats lagi, dengan hanya membuat LN Invoice baru dengan jumlah tersebut, akan memicu permintaan saluran baru ke LSP Olympus. Jadi, Anda akan mendapatkan saluran kedua.


Oleh karena itu, untuk menghindari membayar lebih banyak biaya untuk membuka banyak channel, disarankan untuk membuka channel yang lebih besar terlebih dahulu, misalnya 1-2M Sats. Setelah terbuka, Anda dapat menukar sebagian dari Sats tersebut ke onchain, katakanlah 50%, menggunakan layanan swap eksternal apa pun yang dijelaskan dalam panduan ini.


Setelah Anda menukar dari channel tersebut, katakanlah 50% dan mengembalikan Sats ke dalam onchain Zeus Anda sendiri Wallet, Anda siap untuk beralih ke metode selanjutnya untuk membuka channel baru - dari saldo onchain.


#### Metode B - Menggunakan saldo onchain Anda


Dengan metode ini Anda dapat membuka saluran ke node LN lainnya, termasuk LSP Olympus yang sama. Tetapi jika Anda sudah memiliki saluran dengan Olympus disarankan untuk memiliki juga dengan node lain, untuk keandalan yang lebih baik dan juga dapat menggunakan MPP (pembayaran multi-bagian).


![Image](assets/en/10.webp)


Di atas adalah contoh pembayaran LN Invoice menggunakan MPP. Seperti yang dapat Anda lihat di bagian bawah layar terdapat "pengaturan" dan membuka halaman drop-down dengan detail lebih lanjut untuk pembayaran yang akan Anda lakukan. Pada layar tersebut, jika Anda mempunyai setidaknya 2 saluran yang terbuka, fitur MPP akan diaktifkan secara default. Anda juga dapat mengaktifkan AMP (atomic multi-path) dan mengatur bagian tertentu yang Anda inginkan. Ini adalah fitur yang sangat berguna!


Untuk private node seperti Zeus, saya akan merekomendasikan untuk memiliki 2-3 saluran yang bagus (maksimal 4-5), dengan LSP yang bagus dan likuiditas yang baik untuk memenuhi semua kebutuhan Anda untuk membayar atau menerima Sats melalui LN. [Lihat lebih banyak saran likuiditas node LN dalam panduan ini] (/nodes/managing-lightning-node-liquidity-en.html). Juga di sini [panduan umum tentang likuiditas LN] (https://Bitcoin.design/guide/how-it-works/liquidity/) dari tim Desain Bitcoin.


Memilih peer yang tepat, saya tahu, bukanlah tugas yang mudah, bahkan untuk pengguna yang berpengalaman. [Jadi saya akan memberi Anda beberapa opsi untuk memulai] (https://github.com/ZeusLN/zeus/discussions/2265), ini adalah node peer yang saya uji sendiri menggunakan Zeus (saya mencoba menghubungkan hanya ke node LND untuk menghindari masalah ketidakcocokan)


Berikut ini juga daftar rekan-rekan node yang dijamin untuk Zeus. Jika Anda mengetahui yang bagus, Anda dapat menambahkannya ke daftar tersebut.


Anda dapat membuka saluran di Zeus dengan membuka tampilan Saluran dengan mengklik ikon saluran di sudut kanan bawah tampilan utama, lalu menekan ikon + di sudut kanan atas.


![Image](assets/en/11.webp)


Jika Anda ingin membuka saluran dengan node tertentu, klik (A) sudut atas untuk memindai QR nodeID node (pada Mempool, Amboss, 1ML Anda dapat memperoleh QR tersebut) dan semua detail peer akan terisi.


PENGINGAT:


- Node tertanam Zeus tidak menggunakan layanan Tor! Jadi, tolong jangan mencoba untuk membuka saluran dengan node yang berada di bawah Tor! Anda melakukan lebih banyak kerusakan pada diri anda sendiri daripada menambahkan lebih banyak privasi. Tor untuk LN tidak menawarkan lebih banyak privasi tetapi menambahkan lebih banyak masalah.
- pilihlah dengan bijak rekan-rekan Anda, lebih baik LSP yang baik, node perutean yang baik, bukan node kampungan acak yang dapat menutup saluran Anda dan tidak dapat menawarkan likuiditas yang baik. [Di sini saya menulis panduan khusus] (https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) tentang likuiditas dan contoh node.


Jika Anda langsung mengklik tombol "Buka Saluran ke Olympus", Anda akan mengisi kolom yang diperlukan untuk membuka saluran ke [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Tidak seperti saluran LSP berbayar, saluran Anda akan memerlukan konfirmasi On-Chain, menggunakan dana onchain Anda (Anda dapat memilih dari UTXO Anda di tampilan saluran terbuka); saluran tersebut tidak akan terbuka secara instan. Silakan lihat terlebih dahulu biaya Mempool yang sebenarnya dan sesuaikan dengan kebutuhan Anda, tergantung pada seberapa cepat Anda ingin membuka saluran tersebut.


Sebelum menekan tombol untuk membuka saluran, geser ke bawah opsi lanjutan:


![Image](assets/en/12.webp)


Anda juga harus memastikan bahwa saluran tersebut tidak diumumkan (privat). Secara default, opsi ini tidak aktif untuk saluran yang diumumkan. Opsi ini tidak disarankan untuk diaktifkan untuk node tertanam Zeus, hanya berguna ketika Anda menggunakan Zeus dengan node jarak jauh Anda, sebagai node perutean publik.


Tidak seperti saluran LSP berbayar, Anda tidak akan mendapatkan keuntungan dari perutean tanpa biaya dengan membuka saluran dengan metode ini.


Dan selesai, cukup klik pada tombol "Buka Saluran", tunggu tx dikonfirmasi oleh penambang. Setelah saluran terbuka, Anda dapat bertransaksi sesuai keinginan dengan Sats dari saluran Anda.


Ingatlah bahwa saluran ini akan memiliki semua saldo di pihak ANDA, jadi Anda tidak akan memiliki likuiditas masuk. Seperti yang saya katakan sebelumnya, tukar atau habiskan beberapa Sats untuk membeli barang di atas LN untuk "memberi lebih banyak ruang" untuk menerima.


Bayangkan saluran LN Anda sebagai segelas air. Anda menuangkan air (Sats) ke dalam gelas kosong (saluran Anda) hingga terisi penuh. Anda tidak dapat menuangkan lebih banyak air sampai Anda meminumnya (menghabiskan/menukar). Ketika gelas hampir kosong, tuangkan lebih banyak air (Sats) ke dalamnya dengan menggunakan swap in. [Baca lebih lanjut tentang layanan swap eksternal di sini](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Ada juga layanan LSP lain yang menjual saluran inbound kepada Anda: LNBig atau Bitrefill. Saya pikir ada lebih banyak layanan seperti ini tetapi tidak dapat mengingatnya sekarang.


Jadi jika Anda membutuhkan saluran LN yang kosong (saldo 100% di sisi peer sejak awal), untuk menerima lebih banyak pembayaran daripada yang dapat Anda tangani pada saluran yang sudah terisi, ini bisa menjadi pilihan yang sangat bagus. Anda akan membayar biaya tertentu untuk membuka saluran ini dan Anda mendapatkan banyak ruang masuk.



## TIPS DAN TRIK


### Batas cadangan masuk


Saat ini, karena beberapa keterbatasan kode LN, tidak mungkin untuk menerima jumlah yang ditampilkan di "Inbound". Selalu ingat bahwa Anda harus membuat faktur dengan jumlah yang lebih sedikit, yaitu jumlah "Cadangan Lokal Saluran".


![Image](assets/en/13.webp)


Seperti yang dapat Anda lihat pada gambar di atas, "inbound" menampilkan bahwa saya masih dapat menerima 5101 Sats, tetapi pada kenyataannya pada saat ini tidak mungkin untuk menerima lebih banyak. Dan Anda dapat mengamati bahwa itu adalah jumlah yang sama dengan "Cadangan lokal".


Jadi perlu diingat, ketika Anda membuat faktur untuk diterima, perhatikan juga likuiditas saluran Anda dan kurangi cadangan lokal dari jumlah tersebut, jika Anda ingin mendorong hingga batas jumlah piutang.


### Saran singkat untuk pengguna baru yang memulai dengan node Zeus:



- Manfaatkan saluran baru Anda dengan benar.


Sebagai contoh, jika Anda tahu bahwa Anda akan menerima dalam seminggu, katakanlah 1M Sats, buka saluran 2M Sats dan tukar ke dalam onchain Wallet atau ke dalam akun kustodian LN (sementara) 50-60% dari likuiditas keluar Anda. Selalu siap dengan lebih banyak likuiditas. Ketika Anda membutuhkan lebih banyak likuiditas kembali ke saluran Zeus Anda, Anda dapat memindahkannya kembali dari akun kustodian.


Jika Anda tahu bahwa Anda akan mengirim, katakanlah, 500 ribu Sats/minggu, maka bukalah saluran 1 juta Sats. Dengan cara ini Anda akan tetap memiliki cadangan sampai Anda mengisinya lagi.



- Jika Anda seorang pedagang dan Anda akan selalu menerima lebih banyak daripada yang Anda keluarkan secara teratur, belilah saluran masuk khusus. Ini adalah cara termurah. Anda membayar biaya minimal dan mendapatkan saluran "kosong".



- Jangan membuka saluran kecil yang tidak berarti sebesar 50-100-300-500k Sats. Anda akan mengisinya dalam hitungan hari, bahkan jika Anda menggunakannya hanya untuk zaps. Buka saluran yang lebih besar dan berbeda, BUKAN hanya satu saluran.


Setelah Anda membuka channel yang lebih besar, Anda selalu dapat menggunakan submarine swap eksternal untuk memindahkan Sats ke dalam dompet onchain Anda (termasuk kembali ke onchain Zeus). Menjaga keseimbangan antara likuiditas masuk dan keluar adalah hal yang baik dan Anda juga dapat "menggunakan kembali" Sats tersebut untuk membuka lebih banyak channel jika Anda mau.


### Invoice yang dibungkus


Jika Anda ingin menambahkan lebih banyak privasi saat menerima, Anda dapat menggunakan metode "wrapped Invoice". Pengingat: untuk dapat melakukan ini, Anda memerlukan saluran dengan Olympus LSP. Faktur yang dibungkus akan "menyembunyikan" tujuan akhir (node Zeus Anda) dan menampilkan node LSP Anda sebagai tujuan kepada pembayar.


Untuk mendapatkan Invoice yang sudah dibungkus, buka layar keypad utama, masukkan jumlah dan tekan request. Akan muncul kode QR normal untuk Invoice Anda. Sekarang, klik tombol "X" di kanan atas dan Anda akan diarahkan ke lebih banyak opsi untuk Invoice.


![Image](assets/en/14.webp)


Sekarang Anda harus mengaktifkan opsi di atas "Aktifkan LSP" dan tekan tombol "Buat Invoice". Opsi itu akan membuat Invoice yang dibungkus dan ingat, akan mengenakan sedikit biaya.


### Faktur dengan petunjuk rute


Ini adalah fitur yang sangat berguna jika Anda ingin mengelola likuiditas beberapa saluran masuk. Secara praktis, Anda dapat menunjukkan saluran masuk mana yang Anda inginkan untuk menerima Sats dari Invoice.


Fitur ini juga dapat digunakan untuk rebalanacing melingkar, ketika Anda ingin memindahkan likuiditas dari satu saluran yang terisi ke saluran lain yang kosong.


Bagaimana cara membuat Invoice dengan petunjuk rute?



- Pada layar utama, geser ke kanan laci LN dan klik "Terima"
- Dalam pengaturan Invoice, masuk ke bagian bawah dan aktifkan tombol "Sisipkan petunjuk rute", kemudian pilih tab "Custom". Ini akan membuka layar dengan semua saluran yang tersedia. Pilih salah satu yang ingin Anda terima.
- Isi semua detail Invoice lainnya, jumlah, memo, dan lain-lain dan klik "buat Invoice".
- Membayar Invoice tersebut akan membawa Sats ke saluran yang ditunjukkan.


Jika Anda ingin membayar Invoice (penyeimbangan melingkar), ketika Anda membayarnya dari node Zeus yang sama, di layar pembayaran, pilih saluran keluar (yang memiliki lebih banyak likuiditas) yang ingin Anda gunakan sebagai pengirim pembayaran.


### Bayar dengan Keysend


Keysend adalah fitur LN yang sangat diremehkan dan pengguna harus lebih sering menggunakannya.


[Keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) memungkinkan pengguna di Lightning Network untuk mengirim pembayaran kepada orang lain, langsung ke kunci publik mereka, selama node mereka memiliki saluran publik dan mengaktifkan keysend. Keysend tidak mengharuskan penerima pembayaran untuk mengeluarkan Invoice.


Jadi, bagaimana Anda dapat melakukannya dengan Zeus?


Cukup pindai atau salin nodeID tujuan (atau gunakan kontak Zeus untuk menyimpan node tujuan reguler Anda sebagai kontak) dan kemudian dari layar utama Zeus, klik tombol "Kirim". Pada layar tersebut kemudian tempelkan nodeID atau pilih dari kontak Anda.


Masukkan jumlah Sats, pesan jika diperlukan (ya, Anda juga dapat menggunakannya sebagai obrolan rahasia melalui LN) dan klik tombol "Kirim". Selesai!


![Image](assets/en/15.webp)


Jika Anda memiliki saluran langsung dengan rekan yang dituju, TIDAK ADA biaya yang dikenakan.


Jika Anda tidak memiliki saluran langsung dengan peer tujuan, maka pembayaran keysend akan membayar biaya sebagai pembayaran LN Invoice normal, yang dirutekan pada jalur reguler seperti pembayaran lainnya. Hanya saja, ingat, itu tidak akan meninggalkan jejak apa pun sebagai LN Invoice.


## Kesimpulan


Saya sarankan untuk membaca panduan tindak lanjut [Penggunaan lanjutan Zeus] (https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) dengan lebih banyak instruksi dan kasus penggunaan.


Dan... selesai! Mulai sekarang Anda cukup menggunakan Zeus Node sebagai BTC/LN Wallet biasa di ponsel Anda. UI-nya cukup sederhana dan mudah digunakan, intuitif untuk semua jenis pengguna, saya rasa saya tidak perlu menjelaskan lebih lanjut tentang cara melakukan dan menerima pembayaran.


Sebagai kesimpulan, berikut ini adalah bagan privasi perbandingan :


![Image](assets/en/16.webp)