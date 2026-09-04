---
name: Zeus Embedded - Lanjutan
description: Dompet Lightning multi-node dengan kustodi sendiri
---

![Zeus](assets/cover.webp)


## Pengantar ZEUS Wallet


ZEUS adalah aplikasi seluler Bitcoin wallet sekaligus alat manajemen node dengan fungsionalitas penuh sebagai Lightning wallet, yang membuat pembayaran Bitcoin jadi sederhana, memberi kamu kontrol penuh atas dana, dan memungkinkan pengguna yang lebih mahir mengelola node Lightning langsung dari genggaman tangan.

### Untuk siapa ZEUS?

Saat ini ZEUS ditujukan untuk orang yang menjalankan node rumah / bisnis mereka sendiri dengan [Lightning Network Daemon (LND)](https://lightning.engineering/) atau [Core Lightning (CLN)](https://blockstream.com/lightning/) dan mengelolanya dari jarak jauh melalui Zeus.


Pedagang yang menggunakan [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) atau [Alby](https://getalby.com/) (atau akun LNDhub lainnya) juga dapat menghubungkan, menggunakan, dan mengelola node / akun mereka dari ZEUS.


[Mulai dari v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS akan mulai melayani pengguna biasa yang hanya ingin cara sederhana untuk melakukan pembayaran bitcoin yang cepat dan murah dari perangkat seluler mereka dengan memiliki [node Lightning seluler bawaan](https://docs.zeusln.app/category/embedded-node) dengan [Penyedia Layanan Lightning (LSP)](https://docs.zeusln.app/lsp/intro) terintegrasi.


### Sumber daya Zeus yang penting:


- Halaman web resmi Zeus - [https://zeusln.app/](https://zeusln.app/)
- Dokumentasi Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Repositori Github Zeus](https://github.com/ZeusLN/zeus)
- [Grup dukungan Zeus di Telegram](https://t.me/ZeusLN)
- [Zeus di NOSTR](https://iris.to/zeus@zeusln.app)
- [Pengumuman Blog Zeus](https://blog.zeusln.com)


### Fitur Zeus

#### Fitur umum:


- Self-custody, hanya Bitcoin dan Lightning wallet  
- Tanpa biaya pemrosesan, tanpa KYC  
- Sepenuhnya open source (AGPLv3)  
- Dukungan multi node atau akun, kamu bisa mengelola node rumah sendiri, menjalankan node LND tertanam, atau terhubung ke beberapa akun LNDhub  
- Menu aktivitas yang mudah digunakan  
- Enkripsi PIN atau passphrase, mode Privasi untuk menyembunyikan data sensitif kamu  
- Buku kontak, multi tema, multi bahasa  


#### Fitur teknis


- Terhubung melalui Tor  
- Dukungan LNURL penuh, Pay, Withdraw, Auth, Channel, serta kirim ke Lightning address  
- Manajemen channel Lightning yang terperinci, dukungan MPP atau AMP, Keysend, serta pengaturan biaya routing  
- Dukungan Replace-by-Fee, RBF, dan Child Pays For Parent, CPFP  
- Pembayaran dan permintaan via NFC, tanda tangani dan verifikasi pesan  
- Dukungan SegWit dan Taproot  
- Simple Taproot Channels  
- Lightning address self-custodial (@zeuspay.com)  
- Point of Sale by Square, fitur PoS segera hadir  


### Panduan dan Video Tutorial


Untuk bisa menggunakan Zeus dan mengelola channel Lightning, likuiditas, biaya, dan lainnya, sebaiknya kamu membaca terlebih dahulu beberapa panduan penting tentang Lightning Network.


#### Panduan:


- [LND - Dokumentasi Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Dokumentasi Core Lightning](https://lightning.readthedocs.io/index.html)
- [Panduan Lightning untuk Pemula](https://bitcoiner.guide/lightning/) – oleh Bitcoin Q&A
- [Manajemen Node Lightning](https://www.lightningnode.info/) – oleh openoms
- [Jaringan Lightning dan analogi bandara](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Mengelola Likuiditas Node Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Pemeliharaan Node Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Video tutorial oleh Sesi BTC


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Panduan panduan bagaimana cara mulai menggunakan node tertanam Zeus LN pada perangkat seluler kamu


![Image](assets/en/01.webp)


Aku mendedikasikan panduan ini untuk semua pengguna baru Lightning Network, LN, yang ingin memulai perjalanan berdaulat mereka dengan menggunakan node self-custodial di perangkat seluler.


Anggap saja kamu sudah melewati semua wallet LN kustodial, tetapi belum siap menjalankan node routing LN PUBLIC. Kamu hanya ingin menumpuk lebih banyak sats di atas LN dengan cara yang lebih self-custodial dan melakukan pembayaran rutin melalui LN.

Inilah Zeus, dimulai dengan [versi v0.8.0 yang diumumkan di blog mereka](https://blog.zeusln.com/new-release-zeus-v0-8-0/), kini menawarkan node LND tertanam di dalam aplikasi. Hingga kini Zeus adalah aplikasi manajemen node jarak jauh + akun LNDhub. Tetapi sekarang… node ada di dalam ponsel!


![Image](assets/en/02.webp)


### Rekap cepat fitur-fitur utama untuk Zeus Node:



- Node LND **privat** - Artinya node ini TIDAK akan melakukan routing publik untuk pembayaran orang lain melalui node kamu. Node dan channel-nya tidak diumumkan (privat, tidak terlihat di grafik publik Lightning Network). Untuk menerima dan mengirim pembayaran akan dilakukan melalui rekan LSP yang terhubung. INGAT: Zeus Embedded Node TIDAK melakukan routing publik!
- **Layanan LND yang persisten** - Kamu bisa mengaktifkan fitur ini untuk menjaga layanan LND tetap berjalan terus seperti node Lightning biasa. Aplikasi tidak harus selalu dibuka, karena layanan persisten akan menjaga semua komunikasi tetap online.
-   **Filter blok Neutrino** - sinkronisasi blok dilakukan menggunakan [filter blok dan protokol Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (tanpa memberikan informasi tentang dana on-chain pengguna kami). Pengingat: untuk koneksi internet berlatensi tinggi / lambat, sinkronisasi blok berbasis Neutrino ini kadang dapat gagal. Mencoba beralih ke server Neutrino terdekat dapat membantu memulihkan sinkronisasi. Tanpa sinkronisasi ini, node LND kamu tidak dapat dimulai!
- **Simple Taproot Channel** - Saat menutup channel ini, kamu dikenakan biaya lebih rendah dan mendapatkan privasi lebih besar karena transaksi terlihat seperti pengeluaran Taproot lain saat dilihat di rantai on-chain.
- **LSP terintegrasi** - Olympus adalah node LSP baru untuk Zeus. Kamu bisa menerima sats kembali melalui LN secara langsung tanpa harus menyiapkan channel terlebih dahulu. Cukup buat Lightning invoice dan bayar dari wallet LN lain, dengan layanan channel Zeus 0-conf. Kamu juga mendapatkan privasi tambahan karena LSP menyediakan invoice terbungkus yang menyembunyikan public key node kamu dari pihak pembayar.
- **Buku Kontak** - Kamu bisa menyimpan kontak secara manual atau mengimpor dari Nostr, untuk memudahkan pembayaran ke tujuan yang sering kamu gunakan.
- Dukungan penuh LNURL, serta pengiriman dan penerimaan Lightning address - sekarang kamu bisa mengatur Lightning address self-custodial kamu sendiri di @zeuspay.com. Sebagai pengingat, kamu juga bisa memakai Zeus untuk autentikasi LN di situs yang mendukung login dengan Lightning authentication. Praktis.
- **Point of Sale** - Sekarang pengguna pedagang bisa mengatur daftar produk sendiri dan menjual langsung lewat Zeus melalui fitur PoS terintegrasi. Untuk saat ini masih mendukung fungsi dasar, tetapi ke depan akan diperluas fiturnya.
- **Log LND** - Kamu bisa membaca log layanan LND secara real time dan menggunakannya untuk melakukan debugging jika ada masalah, terutama saat koneksi kurang stabil.
- **Pencadangan Otomatis** - Channel node LN otomatis dicadangkan di server Olympus. Backup otomatis ini dienkripsi dengan seed wallet kamu, jadi tanpa seed sama sekali tidak bisa dipakai. Kamu juga bisa mengekspor secara manual SCB, Static Channel Backup, untuk pemulihan saat terjadi bencana.


### Cara bergabung dengan Zeus LN Node (LND tertanam)


Dalam panduan ini aku hanya akan membahas node LND tertanam, dan bukan tentang cara lain untuk menggunakan aplikasi luar biasa ini (manajemen node jarak jauh dan akun LNDhub). Untuk jenis koneksi lainnya, silakan lihat [halaman dokumentasi Zeus](https://docs.zeusln.app/category/getting-started), yang sudah dijelaskan dengan sangat baik dan tidak memerlukan panduan khusus.


#### LANGKAH 1 - PENGATURAN AWAL


Karena Zeus adalah node LND penuh, aku akan memberikan beberapa rekomendasi awal:



- Jangan gunakan perangkat lama, karena bisa mempengaruhi performa aplikasi canggih ini. Terutama saat proses sinkronisasi, aplikasi bisa menggunakan CPU dan RAM secara intensif. Jika spesifikasinya rendah, Zeus bahkan bisa tidak berjalan dengan baik.
- Gunakan minimal Android 11 dan pastikan sistem operasi selalu diperbarui. Untuk iOS juga begitu, usahakan memakai versi OS terbaru atau yang lebih tinggi.
- Kamu membutuhkan setidaknya 1 GB ruang penyimpanan untuk data. Seiring waktu bisa bertambah, tetapi ada fitur untuk memadatkan database hingga ukuran yang lebih kecil dalam satuan MB.
- TIDAK perlu menggunakan Zeus dengan Tor atau Orbot. Jangan membuatnya lebih rumit dari yang diperlukan. Dalam konteks ini, Tor tidak selalu memberi privasi tambahan, dan justru bisa memperlambat sinkronisasi awal. Hati-hati juga dengan VPN yang kamu pakai dan periksa latensi koneksi ke server Neutrino. Perlu diingat, filter blokir Neutrino tidak membocorkan atau melacak identitas perangkat, hanya memproses blok. Lalu lintas LN juga berada di belakang LSP dengan channel privat, jadi informasi yang keluar sangat terbatas. Tidak perlu panik soal privasi.
- Bersabarlah saat sinkronisasi awal, karena bisa memakan waktu beberapa menit. Usahakan terhubung ke internet broadband dengan latensi yang stabil. Jika kamu menjalankan node Bitcoin sendiri, [Anda dapat mengaktifkan layanan neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) dan menghubungkan Zeus Anda ke node Anda sendiri, bahkan menggunakan LAN internal, sehingga Anda akan mendapatkan kecepatan maksimum.


Setelah kamu mengatur jenis koneksi "Node tertanam", aplikasi akan mulai menyinkronkan untuk sementara waktu. Tunggu dengan sabar untuk menyelesaikan bagian tersebut, lalu masuk ke halaman Pengaturan utama.


![Image](assets/en/03.webp)


Secara singkat, mari kita selami masing-masing bagian Pengaturan dan memahami beberapa fitur utama, sebelum kamu mulai menggunakan Zeus:


**A - PENGATURAN**


Ini adalah bagian dengan pengaturan umum untuk seluruh aplikasi


**1 - Lightning Service Provider (LSP)**


Di sini disajikan dua layanan LSP:



- Channel _Just in Time_ - Jika kamu tidak memiliki channel terbuka atau tidak memiliki inbound liquidity yang tersedia, dan fitur ini diaktifkan, sistem akan membuka channel dengan cepat untuk kamu. Opsi ini bisa dinonaktifkan jika kamu tidak ingin membuka channel jenis ini lagi.
- Memesan channel terlebih dahulu - Kamu bisa membeli inbound channel dari LSP Olympus langsung dari dalam aplikasi, dengan berbagai pilihan dan nominal (untuk inbound dan outbound liquidity).


LSP membantu menghubungkan pengguna ke jaringan Lightning dengan membuka saluran pembayaran ke node mereka. [Baca lebih lanjut tentang LSP di sini](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS memiliki LSP baru yang terintegrasi bernama [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), yang tersedia untuk semua pengguna yang menggunakan node tersemat baru.

Secara default, yang digunakan adalah LSP Olympus (https://0conf.lnolymp.us), tetapi kamu juga bisa mengatur LSP 0conf lain yang mendukung protokol ini.


Perlu diingat:

Saat kamu membuka channel dengan Olympus LSP menggunakan wrapped LN invoice, kamu juga akan mendapatkan inbound liquidity sebesar 100 ribu sats. Ini opsi yang sangat bagus jika kamu perlu menerima lebih banyak sats.

Contoh: Jika kamu menyetor 400k sats untuk membuka channel LSP, maka LSP akan membuka channel dengan kapasitas 500k sats ke node Zeus kamu dan mendorong 400k sats yang kamu setorkan ke sisi kamu.

"Likuiditas masuk" artinya lebih banyak ruang di channel kamu untuk menerima pembayaran.


Ke depan, kita berharap akan ada lebih banyak LSP yang bisa diintegrasikan ke Zeus dan masing-masing bisa menjadi alternatif. Tinggal menunggu sampai LSP baru mengadopsi standar terbuka untuk channel 0conf seperti ini.


Jika kamu tidak ingin membuka channel baru dengan cepat, kamu bisa menonaktifkan opsi tersebut.


Di bagian yang sama, kamu juga bisa memilih opsi "request Simple Taproot Channels" saat LSP membuka channel ke node Zeus kamu. Channel Taproot sederhana ini menawarkan privasi on-chain yang lebih baik dan biaya penutupan yang lebih rendah. Ada dua alasan kamu mungkin tidak ingin menggunakannya:


- Teknologinya masih baru, sehingga mungkin masih ada bug di LND saat memakainya.  
- Rekanannya belum mendukung fitur ini. Bahkan node LND pun harus secara eksplisit memilihnya untuk saat ini.


**2 - Pengaturan pembayaran**


Fitur ini memungkinkan kamu mengatur biaya yang ingin kamu gunakan untuk pembayaran, baik melalui LN maupun on-chain. Ada juga opsi untuk mengatur batas waktu invoice, baik untuk memperpanjang maupun memperpendeknya.


Jika beberapa pembayaran LN gagal, kamu bisa menaikkan biaya untuk menemukan rute yang lebih baik. Jika kamu melakukan transaksi on-chain, kamu juga bisa mengatur fee tertentu agar transaksi tidak lama tertahan di mempool saat biaya jaringan sedang tinggi.


**3 - Pengaturan faktur**


Pada bagian ini terdapat beberapa opsi untuk faktur generate:



- Mengatur memo default yang akan ditampilkan di invoice yang kamu buat.
- Mengatur waktu kedaluwarsa dalam hitungan detik, jika kamu ingin menentukan durasi yang lebih lama atau lebih singkat untuk invoice pembayaran kamu.
- Sertakan routing hints - memberikan informasi untuk menemukan channel yang tidak diiklankan atau channel privat. Fitur ini memungkinkan pembayaran diarahkan ke node yang tidak terlihat secara publik di jaringan. Routing hints menyediakan sebagian rute antara node privat penerima dan node publik. Petunjuk ini kemudian dimasukkan ke dalam invoice yang dibuat oleh penerima dan diberikan ke pihak pembayar. Aku sarankan mengaktifkannya secara default, karena jika tidak, pembayaran yang masuk bisa gagal akibat tidak ditemukan rute.
- AMP Invoice - Pembayaran Multi Jalur Atomik adalah jenis pembayaran Lightning baru yang diimplementasikan oleh LND yang memungkinkan untuk menerima Sats tanpa Invoice tertentu, menggunakan [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Praktis merupakan kode pembayaran statis. [Baca lebih lanjut di sini](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Tampilkan bidang gambar awal khusus - gunakan opsi ini hanya dalam kasus yang sangat spesifik ketika kamu benar-benar ingin menggunakan bidang khusus dalam gambar awal. [Baca selengkapnya di sini](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Pilihan lain di bagian ini adalah bagaimana mengatur jenis onchain Address yang ingin kamu gunakan: Nested SegWit, SegWit, Taproot.


![Image](assets/en/04.webp)


Klik tombol roda gigi di bagian atas, lalu akan muncul popup untuk memilih tipe address yang kamu inginkan. Setelah kamu mengaturnya, saat kamu menekan tombol terima untuk on-chain, sistem akan langsung membuat address sesuai tipe yang kamu pilih. Kamu bisa mengubahnya kapan saja.

**4 - Pengaturan saluran**


Di bagian ini kamu bisa mengatur beberapa fitur untuk pembukaan channel, seperti:


- Jumlah konfirmasi  
- Umumkan channel (secara default tidak aktif), artinya channel tersebut akan menjadi channel privat  
- Simple Taproot Channel  
- Tampilkan tombol pembelian channel  


**5 - Pengaturan privasi**


Di sini kamu akan menemukan beberapa pengaturan dasar untuk menambah privasi saat menggunakan aplikasi Zeus:


- Block explorer untuk melihat detail transaksi (Mempool.space, Blockstream.info, atau explorer yang lebih privat)  
- Baca clipboard - opsi aktif atau nonaktif jika kamu ingin Zeus membaca papan klip perangkat  
- Mode Lurker - opsi aktif atau nonaktif jika kamu ingin menyembunyikan informasi sensitif tertentu di aplikasi Zeus. Ini pilihan yang bagus saat kamu membuat demo atau mengambil screenshot.
- Saran biaya Mempool - aktifkan opsi ini jika ingin menggunakan tingkat biaya yang disarankan dari [Mempool.space](https://Mempool.space/)


**6 - Keamanan**


Bagian ini hanya memiliki dua opsi untuk mengamankan aplikasi saat dibuka: atur password atau PIN.


Setelah kamu mengatur PIN untuk membuka aplikasi, kamu juga bisa membuat "PIN darurat". PIN tambahan ini bersifat rahasia dan HANYA digunakan dalam situasi terpaksa, misalnya jika kamu berada dalam tekanan. Jika kamu memasukkan PIN darurat, semua konfigurasi akan terhapus. Jadi pastikan kamu selalu memperbarui backup kamu. Pencadangan otomatis aktif secara default, tetapi tetap disarankan untuk memiliki backup sendiri di luar perangkat.


**7 - Mata Uang**


Kamu bisa mengaktifkan atau menonaktifkan opsi untuk menampilkan konversi mata uang fiat di aplikasi Zeus. Saat ini mendukung lebih dari 30 mata uang fiat di seluruh dunia.


**8 - Bahasa**


Kamu bisa beralih di antara beberapa bahasa yang diterjemahkan dan ditinjau oleh komunitas Zeus bersama penutur asli.


**9 - Tampilan**


Di bagian ini kamu bisa mempersonalisasi tampilan Zeus, memilih berbagai tema warna, menentukan layar utama default (keypad atau balance), menampilkan alias node kamu, mengaktifkan tombol keypad yang lebih besar, serta menampilkan lebih banyak angka desimal.


**10 - Tempat Penjualan**


Ini adalah fitur untuk mengaktifkan atau menonaktifkan sistem PoS yang terintegrasi di Zeus. Kamu bisa menjalankan PoS mandiri atau terhubung ke sistem PoS Square. Saat ini fitur ini mendukung fungsi dasar sebagai PoS, cukup untuk memulai dan membantu pedagang kecil seperti bar, restoran, atau toko kelontong menerima BTC secara native.


Di dalam pengaturan ini, kamu akan menemukan berbagai opsi untuk mengatur PoS kamu:


- Jenis konfirmasi pembayaran: hanya LN, 0-conf, atau 1-conf  
- Aktifkan atau nonaktifkan tips untuk karyawan yang mengoperasikan PoS  
- Tampilkan atau sembunyikan keypad  
- Atur persentase pajak yang berlaku pada struk  
- Buat produk dan kategori produk  
- Lihat daftar sederhana semua transaksi penjualan

Berikut ini adalah video demo langsung cara menggunakan Zeus PoS:


**B - Cadangan Wallet** *B - Cadangan Wallet*


Node yang tertanam di ZEUS didasarkan pada LND dan menggunakan [format aezeed seed](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Ini berbeda dengan [format BIP39](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) yang biasa Anda lihat pada kebanyakan dompet Bitcoin, walaupun mungkin terlihat mirip. Aezeed menyertakan beberapa data tambahan termasuk tanggal lahir Wallet yang akan membantu pemindaian ulang selama pemulihan menjadi lebih efisien.


Format kunci aezeed harus kompatibel dengan wallet seluler berikut: Blixt, BlueWallet, dan Breez. Perlu diingat bahwa seed saja tidak cukup untuk memulihkan seluruh saldo kamu jika kamu memiliki channel yang masih terbuka atau dalam proses penutupan!

Pelajari lebih lanjut tentang proses pencadangan dan pemulihan di [halaman Dokumen Zeus](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


SARAN PENTING: Saat kamu menyimpan seed, pastikan juga menyimpan node pubkey. Kadang lebih baik menyimpannya bersama seed dan SCB, Static Channel Backup, untuk berjaga-jaga jika kamu perlu memverifikasi proses pemulihan.


SCB hanya diperlukan jika kamu memiliki channel LN yang masih terbuka. Jika kamu hanya menyimpan dana on-chain, file ini tidak dibutuhkan.


Jika setelah waktu lama riwayat transaksi lama masih belum muncul, buka menu Embedded node - Peers dan nonaktifkan opsi penggunaan daftar peer yang dipilih (secara default menggunakan btcd.lnolymp.us). Ini akan memicu restart dan sistem akan terhubung ke peer Neutrino pertama yang tersedia dengan waktu respons paling baik. Kamu juga bisa memilih peer Neutrino terkenal lainnya yang tercantum di bawah.


Jika Anda ingin melihat lebih banyak opsi pemulihan untuk node LND, [silakan baca panduan saya sebelumnya](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), di mana kamu dapat menemukan langkah-langkah cara mengimpor aezeed seed ke dalam Sparrow Wallet atau metode lainnya.


**C - Node Tertanam**

Di bagian ini kamu akan menemukan beberapa alat dasar untuk mengelola node terintegrasi:


- Pemulihan bencana - Backup otomatis dan manual untuk channel LN. Silakan baca dokumentasi Zeus untuk mengetahui cara menggunakan fitur ini dengan lebih detail.

- Express Graph Sync - Aplikasi Zeus akan mengunduh data graph gosip LN dari server khusus, untuk sinkronisasi yang lebih cepat dan lebih optimal, sehingga kamu bisa mendapatkan jalur pembayaran terbaik. Kamu juga bisa memilih untuk menghapus data graph sebelumnya saat mengaktifkannya.

- Peers - Bagian untuk mengelola Neutrino peers dan 0-conf peers. Jika kamu mengalami masalah saat sinkronisasi awal atau channel tidak online, biasanya karena latensi tinggi ke peer Neutrino yang digunakan. Coba ganti daftar peer yang diprioritaskan atau tambahkan peer yang kamu tahu memiliki latensi lebih baik untuk sinkronisasi. Berikut beberapa server Neutrino yang terkenal:


  - btcd1.lnolymp.us | btcd2.lnolymp.us - wilayah AS  
  - sg.lnolymp.us - wilayah Asia  
  - btcd-Mainnet.lightning.computer - wilayah AS  
  - uswest.blixtwallet.com (Seattle) - wilayah AS  
  - europe.blixtwallet.com (Jerman) - wilayah Uni Eropa  
  - asia.blixtwallet.com - wilayah Asia  
  - node.eldamar.icu - wilayah AS  
  - noad.sathoarder.com - wilayah AS  
  - bb1.breez.technology | bb2.breez.technology - wilayah AS  
  - neutrino.shock.network - wilayah AS  


- Log LND - Alat yang sangat berguna untuk melakukan debugging masalah pada node LN kamu dan melihat secara teknis apa yang terjadi di sistem.

- Pengaturan lanjutan - Lebih banyak alat untuk mengontrol dan mengelola penggunaan node LND kamu:



 - mode _Pathfinding_ - bimodal atau apriori, cara untuk menemukan rute yang lebih baik untuk pembayaran LN kamu dan juga mengatur ulang informasi rute sebelumnya. Silakan baca panduan yang sangat bagus ini tentang pencarian jalur: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - oleh Docs Lightning Engineering dan [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - oleh Voltage
- _Persistent LND_ - Aktifkan mode ini jika kamu ingin layanan LND berjalan terus di latar belakang dan menjaga node tetap online 24/7. Ini sangat berguna jika kamu menggunakan Zeus sebagai PoS di toko kecil atau menerima banyak tip melalui Lightning address.

- _Rescan wallet_ - Opsi ini akan memicu pemindaian ulang penuh saat restart untuk semua transaksi on-chain di wallet kamu. Aktifkan hanya jika kamu merasa ada transaksi yang hilang. Proses pemindaian ulang bisa memakan waktu beberapa menit, jadi bersabarlah dan selalu periksa log untuk melihat detail progresnya.

- _Compact Database_ - Opsi ini berguna jika aplikasi Zeus menggunakan banyak ruang penyimpanan di perangkat (cek detail aplikasi di pengaturan perangkat kamu). Jika aktivitas kamu cukup tinggi, lakukan pemadatan secara berkala. Jika ukuran data sudah lebih dari sekitar 1 sampai 1,5 GB, lakukan proses compact. Sistem akan restart dan butuh waktu, jadi tunggu sampai selesai.

- _Delete Neutrino files_ - Opsi untuk menghapus file Neutrino (dengan restart). Ini bisa mengurangi penggunaan penyimpanan secara signifikan dan juga berdampak pada konsumsi baterai, terutama jika kamu memakai Zeus dalam mode persisten.


**D - Info Node**


Di bagian ini kamu bisa melihat detail status node Zeus kamu, seperti:


- Alias - ID singkat node  
- Public Key - kunci publik lengkap node kamu yang dipakai node lain untuk menemukan jalur menuju node kamu. Perlu diingat, pubkey ini TIDAK muncul di Lightning explorer biasa seperti Mempool, Amboss, atau 1ML. Pubkey ini hanya bisa diakses melalui peer dan channel Lightning yang terhubung.

- Versi implementasi Lightning  
- Versi aplikasi Zeus  
- Status Synced to chain dan Synced to graph - indikator penting yang menunjukkan status sinkronisasi node. Jika salah satu tidak menunjukkan "true", berarti node masih sinkronisasi atau ada masalah. Sebaiknya cek log LND atau tunggu proses selesai.

- Tinggi blok dan hash - menunjukkan blok terakhir dan hash yang sudah dilihat dan disinkronkan oleh node kamu.


**E - Info Jaringan**


Bagian ini menampilkan detail status umum Lightning Network yang diambil dari data sinkronisasi graph, seperti jumlah channel publik, jumlah node, jumlah channel zombie (offline atau tidak aktif), diameter graph, serta rata-rata dan derajat maksimum graph.


Data ini berguna untuk debugging atau sekadar melihat statistik jaringan.


**F - Lightning Address**


Di bagian ini kamu bisa mengatur self-custodial Lightning address kamu di @zeuspay.com.


ZEUS PAY memanfaatkan hash preimage yang dibuat pengguna, HODL invoice, dan skema otentikasi Zaplocker Nostr untuk memungkinkan pengguna yang tidak online 24/7 tetap bisa menerima pembayaran ke Lightning address statis. Kamu hanya perlu masuk ke wallet ZEUS dalam waktu 24 jam untuk mengklaim pembayaran, jika tidak, dana akan dikembalikan ke pengirim.


Jika kamu mengaktifkan mode persisten, semua pembayaran ke Lightning address kamu akan langsung diterima.


Pelajari tentang cara kerja pembayaran [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) dan lebih lanjut tentang [Biaya ZeusPay di sini](https://docs.zeusln.app/lightning-Address/fees).


**G - Alamat On-Chain**


Di bagian ini kamu bisa melihat alamat on-chain yang kamu hasilkan untuk kontrol koin yang lebih baik.


**H - Kontak**


Buku kontak baru diperkenalkan di Zeus v0.8.0. Kamu bisa menggunakannya untuk mengirim pembayaran dengan cepat ke teman dan keluarga, serta mengimpor kontak dari Nostr.


Cukup masukkan npub Nostr kamu atau NIP-05 address yang bisa dibaca manusia, dan ZEUS akan mengambil data kontak dari Nostr. Dari sana kamu bisa langsung mengirim pembayaran ke kontak tersebut, atau mengimpor semua maupun sebagian kontak ke buku kontak lokal.


Berikut video singkat tentang cara mengonfigurasi dan menggunakan kontak di Zeus:


**I - Alat**


Di sini kamu akan menemukan beberapa subbagian dengan lebih banyak alat:


- akun - Di sini kamu bisa mengimpor akun atau wallet eksternal, baik wallet cold maupun hot, untuk mengontrol atau menjadikannya sumber dana eksternal bagi channel node Zeus. Fitur ini masih dalam tahap percobaan.

- mempercepat transaksi - Fitur ini membantu jika transaksi kamu tertahan di mempool dan kamu ingin menaikkan fee. Kamu perlu memasukkan output tx dari detail transaksi dan memilih fee baru yang ingin digunakan. Fee harus lebih tinggi dari sebelumnya dan kamu harus memiliki dana yang cukup di wallet on-chain kamu.


![Image](assets/en/05.webp)


Kamu harus masuk ke transaksi yang tertunda dan menyalin output txid-nya. Setelah itu buka fitur ini, tempel txid tersebut, lalu pilih fee baru yang ingin kamu gunakan untuk mempercepatnya. Akan muncul layar dengan rekomendasi fee saat itu, atau kamu bisa menentukan fee khusus. Ingat, fee yang baru HARUS lebih tinggi dari sebelumnya.


Sebaiknya simpan UTXO dengan nilai maksimal sekitar 100k sats di wallet on-chain Zeus, supaya bisa digunakan untuk menambah biaya (fee bump) jika diperlukan.


- Tanda tangani atau verifikasi - Dengan fitur ini kamu bisa menandatangani pesan menggunakan kunci wallet kamu. Fitur ini juga bisa dipakai untuk memverifikasi pesan dan membuktikan bahwa pesan tersebut benar berasal dari kunci wallet yang sama.

- Konverter mata uang - Alat sederhana untuk menghitung konversi antara BTC dan mata uang fiat lainnya.


**J - Merchandise dan Dukungan**


Di sini kamu akan menemukan info dan tautan lebih lanjut tentang Zeus, toko online, sponsor, dan media sosial.


**K - Bantuan**


Di bagian terakhir ini kamu bisa menemukan tautan ke dokumentasi Zeus, halaman issue GitHub jika ingin melaporkan bug atau mengajukan permintaan fitur, serta alamat dukungan email.


### LANGKAH 2 - MULAI MENGGUNAKAN ZEUS NODE


Ingat, Zeus terutama dipakai sebagai Lightning wallet untuk pembayaran yang cepat dan mudah melalui LN. Memang ada on-chain wallet di dalamnya, tetapi sebaiknya digunakan khusus untuk membuka atau menutup channel LN, bukan untuk pembayaran sehari-hari seperti beli kopi.

Silakan baca panduan saya yang lain tentang [bagaimana menjadi bank kamu sendiri menggunakan 3 level Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


Saat ini kamu punya dua cara untuk mulai menggunakan Zeus:


- Langsung melalui LN menggunakan channel 0-conf dari Olympus LSP  
- Deposit pertama ke wallet on-chain lalu membuka channel LN secara normal dengan peer yang kamu pilih


#### Metode A - Menggunakan LSP Olympus


Ini adalah cara yang paling mudah dan sederhana untuk onboarding pengguna baru ke Zeus. Bisa digunakan oleh pengguna Bitcoin yang benar-benar baru dan belum punya sats sama sekali, atau oleh teman yang membantu onboarding, maupun pedagang yang baru mulai menerima pembayaran LN.


Secara default, Zeus akan memakai LSP miliknya sendiri, Olympus. Namun ke depan kamu juga bisa beralih ke LSP lain yang mendukung protokol 0-conf untuk membuka channel.


Cukup buat invoice di Zeus (masukkan jumlah lalu tekan tombol "Minta"), dan kamu sudah bisa langsung menerima sats tersebut.


Invoice yang dibuat akan dibungkus (wrapped invoice) sesuai dokumentasi di (https://docs.zeusln.app/lsp/wrapped-invoices) dan kamu akan melihat informasi terkait biaya layanan jika sudah dibayar. Wrapped invoice ini berisi routing hint ke node Zeus kamu, sehingga LSP bisa menemukan node baru kamu dan membuka channel dengan dana yang kamu setorkan.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Untuk mendapatkan channel LN dari LSP menggunakan dana yang ingin kamu terima pertama kali, invoice tersebut harus dibayar dari wallet LN lain. Setelah dibayar, tunggu beberapa saat sampai LSP membuka channel ke node Zeus kamu, memotong biaya layanannya, lalu mendorong sisa dana ke sisi channel kamu.


Yang harus kamu lakukan adalah membayar Invoice yang dihasilkan di ZEUS dengan lightning Wallet, dan saluran kamu akan langsung terbuka. [Silakan baca biaya LSP Zeus](https://docs.zeusln.app/lsp/fees).


Manfaat lain dari membuka channel lewat pembayaran ini adalah routing tanpa biaya. Artinya, saat melakukan pembayaran routing, hop pertama melalui OLYMPUS by ZEUS tidak dikenakan biaya routing. Perlu diingat, hop di luar OLYMPUS by ZEUS tetap akan dikenakan biaya.


Setelah channel siap, tekan tombol di kanan bawah layar yang menampilkan daftar channel Zeus.

![Image](assets/en/08.webp)


Dan kamu akan melihat saluran seperti ini, yang menunjukkan sisi keseimbangan saluran:


![Image](assets/en/09.webp)


Semakin banyak yang kamu belanjakan dari channel ini, semakin besar inbound liquidity yang kamu miliki. Semakin banyak sats yang kamu terima di channel ini, semakin kecil ruang inbound liquidity yang tersisa.


Berikut ini demonstrasi visual sederhana yang bagus (oleh Rene Pickhardt) tentang cara kerja channel Lightning:


Saat ini, dengan melihat layar demo channel, klik nama channel untuk melihat detail lebih lanjut.


Kamu memiliki satu channel dengan Olympus, dengan kapasitas total 490.000 sats, dengan saldo 378.000 sats di sisi kamu dan 88.000 sats di sisi Olympus. Artinya, kamu masih bisa menerima maksimal 88k sats lagi di channel yang sama.


Jika kamu perlu menerima lebih dari 88k sats (melebihi inbound liquidity yang tersedia), misalnya 500k sats lagi, cukup buat invoice baru dengan jumlah tersebut. Itu akan memicu permintaan pembukaan channel baru ke LSP Olympus, sehingga kamu akan mendapatkan channel kedua.


Untuk menghindari membayar biaya lebih sering karena membuka banyak channel kecil, lebih baik membuka channel yang lebih besar terlebih dahulu, misalnya 1–2M sats. Setelah channel terbuka, kamu bisa menukar sebagian sats, misalnya 50%, ke on-chain menggunakan layanan swap eksternal apa pun yang dijelaskan dalam panduan ini.


Setelah kamu menukar sekitar 50% dan memindahkannya kembali ke wallet on-chain Zeus, kamu siap beralih ke metode berikutnya untuk membuka channel baru dari saldo on-chain.


#### Metode B - Menggunakan saldo on-chain kamu


Dengan metode ini kamu bisa membuka channel ke node LN lain, termasuk LSP Olympus yang sama. Namun jika kamu sudah punya channel dengan Olympus, sebaiknya kamu juga membuka channel dengan node lain untuk keandalan yang lebih baik dan agar bisa memanfaatkan MPP (Multi-Part Payments).


![Image](assets/en/10.webp)


Di atas adalah contoh pembayaran Lightning invoice menggunakan MPP. Seperti yang kamu lihat, di bagian bawah layar ada menu "pengaturan" yang membuka halaman drop-down berisi detail lebih lanjut tentang pembayaran yang akan kamu lakukan. Jika kamu memiliki setidaknya 2 channel yang terbuka, fitur MPP akan aktif secara otomatis. Kamu juga bisa mengaktifkan AMP (Atomic Multi-Path) dan mengatur porsi pembayaran sesuai kebutuhan. Ini fitur yang sangat berguna!


Untuk private node seperti Zeus, aku akan merekomendasikan untuk memiliki 2-3 saluran yang bagus (maksimal 4-5), dengan LSP yang bagus dan likuiditas yang baik untuk memenuhi semua kebutuhanmu untuk membayar atau menerima Sats melalui LN. [Lihat lebih banyak saran likuiditas node LN dalam panduan ini](/nodes/managing-lightning-node-liquidity-en.html). Juga di sini [panduan umum tentang likuiditas LN](https://Bitcoin.design/guide/how-it-works/liquidity/) dari tim Desain Bitcoin.


Memilih peer yang tepat, saya tahu, bukanlah tugas yang mudah, bahkan untuk pengguna yang berpengalaman. [Jadi aku akan memberimu beberapa opsi untuk memulai](https://github.com/ZeusLN/zeus/discussions/2265), ini adalah node peer yang aku uji sendiri menggunakan Zeus (aku mencoba menghubungkan hanya ke node LND untuk menghindari masalah ketidakcocokan)


Berikut juga daftar peer node yang direkomendasikan untuk Zeus. Jika kamu tahu node yang bagus, kamu bisa menambahkannya ke daftar tersebut.


Untuk membuka channel di Zeus, masuk ke tampilan Channel dengan menekan ikon channel di sudut kanan bawah layar utama, lalu tekan ikon "+" di sudut kanan atas.


![Image](assets/en/11.webp)


Jika kamu ingin membuka channel dengan node tertentu, tekan (A) di sudut atas untuk memindai QR nodeID dari node tersebut (di Mempool, Amboss, atau 1ML kamu bisa mendapatkan QR-nya). Setelah dipindai, semua detail peer akan terisi otomatis.


PENGINGAT:


- Node embedded Zeus tidak menggunakan layanan Tor. Jadi jangan mencoba membuka channel dengan node yang hanya bisa diakses melalui Tor. Itu lebih banyak merugikan kamu sendiri daripada menambah privasi. Tor untuk LN tidak selalu memberi keuntungan privasi, dan justru sering menambah kompleksitas dan masalah.

- Pilih peer dengan bijak. Lebih baik memilih LSP yang baik atau node routing yang sehat dengan likuiditas bagus, bukan node sembarangan yang bisa menutup channel kamu secara tiba-tiba atau tidak memberikan likuiditas yang memadai. [Di sini aku menulis panduan khusus](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) tentang likuiditas dan contoh node.


Jika aku langsung mengklik tombol "Buka Saluran ke Olympus", aku akan mengisi kolom yang diperlukan untuk membuka saluran ke [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Berbeda dengan channel LSP berbayar, channel yang kamu buka sendiri akan memerlukan konfirmasi on-chain dan menggunakan dana on-chain kamu (kamu bisa memilih UTXO yang ingin dipakai di tampilan pembukaan channel). Channel tidak akan langsung terbuka secara instan. Sebelum menekan tombol untuk membuka channel, sebaiknya cek dulu fee mempool yang sedang berlaku dan sesuaikan dengan kebutuhan kamu, tergantung seberapa cepat kamu ingin channel tersebut dikonfirmasi.


Geser ke bawah untuk melihat opsi lanjutan sebelum membuka channel:


![Image](assets/en/12.webp)


Pastikan juga channel tersebut tidak diumumkan (privat). Secara default, opsi ini tidak aktif untuk channel yang diumumkan. Opsi ini tidak disarankan untuk diaktifkan jika kamu menggunakan node embedded Zeus, dan biasanya hanya berguna jika kamu menghubungkan Zeus ke node jarak jauh sebagai node routing publik.


Berbeda dengan channel LSP berbayar, kamu tidak mendapatkan keuntungan routing tanpa biaya jika membuka channel dengan metode ini.


Jika sudah siap, cukup tekan tombol "Buka Channel" dan tunggu transaksi dikonfirmasi oleh miner. Setelah channel terbuka, kamu bisa langsung bertransaksi menggunakan sats di channel tersebut.


Perlu diingat, channel ini akan menempatkan seluruh saldo di sisi kamu, sehingga kamu tidak memiliki inbound liquidity. Seperti yang sudah dijelaskan sebelumnya, tukar atau gunakan sebagian sats untuk membeli sesuatu di atas LN agar kamu punya ruang untuk menerima lagi.


Bayangkan channel Lightning seperti gelas air. Kamu menuangkan air (sats) ke dalam gelas kosong (channel) sampai penuh. Kamu tidak bisa menuang lebih banyak sampai kamu meminumnya (menghabiskan atau menukar). Saat gelas mulai kosong, kamu bisa mengisinya lagi melalui swap in. [Baca lebih lanjut tentang layanan swap eksternal di sini](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Ada juga layanan LSP lain yang menjual inbound channel kepada kamu, seperti LNBig atau Bitrefill. Mungkin masih ada layanan lain, tetapi aku tidak ingat semuanya sekarang.


Jadi jika kamu membutuhkan channel LN yang kosong (saldo 100% di sisi peer sejak awal) untuk bisa menerima lebih banyak pembayaran dibanding channel yang sudah penuh, ini bisa jadi pilihan yang bagus. Kamu membayar biaya tertentu untuk membuka channel tersebut dan mendapatkan ruang inbound yang besar.


## TIPS DAN TRIK


### Batas inbound yang bisa digunakan


Saat ini, karena keterbatasan implementasi kode LN, kamu tidak bisa langsung menerima jumlah penuh yang terlihat di bagian "Inbound". Selalu ingat untuk membuat invoice dengan jumlah yang lebih kecil, yaitu sebesar nilai "Cadangan Lokal Channel".

![Image](assets/en/13.webp)


Seperti yang kamu lihat di gambar, "Inbound" masih menunjukkan bahwa kamu bisa menerima 5101 sats, tetapi pada praktiknya saat ini tidak memungkinkan untuk menerima lebih dari itu. Jumlah tersebut sama dengan nilai "Cadangan Lokal Channel".


Jadi ingat, saat membuat invoice untuk menerima pembayaran, perhatikan juga likuiditas channel kamu dan kurangi cadangan lokal dari jumlah yang ingin kamu terima jika kamu ingin memaksimalkan batas penerimaan.


### Saran singkat untuk pengguna baru yang mulai memakai node Zeus:


- Gunakan channel baru kamu dengan optimal.


Misalnya, jika kamu tahu akan menerima sekitar 1M sats dalam seminggu, buka channel sebesar 2M sats lalu tukar atau pindahkan sekitar 50 sampai 60 persen likuiditas keluar kamu ke on-chain atau ke akun LN kustodial sementara. Selalu siapkan lebih banyak likuiditas. Ketika kamu butuh likuiditas kembali ke channel Zeus, kamu bisa memindahkannya lagi dari akun tersebut.


Jika kamu tahu akan mengirim sekitar 500 ribu sats per minggu, buka channel sekitar 1 juta sats. Dengan begitu kamu masih punya ruang cadangan sebelum perlu mengisinya kembali.


- Jika kamu seorang pedagang dan biasanya menerima lebih banyak daripada yang kamu keluarkan, lebih baik beli channel inbound khusus. Ini biasanya paling hemat biaya. Kamu membayar biaya minimal dan mendapatkan channel "kosong" dengan ruang penerimaan besar.


- Jangan membuka channel kecil yang tidak berarti seperti 50k, 100k, 300k, atau 500k sats. Channel kecil akan cepat penuh, bahkan hanya untuk transaksi kecil seperti zaps. Lebih baik buka channel yang lebih besar dan berbeda, bukan hanya satu channel saja.


Setelah kamu membuka channel besar, kamu bisa menggunakan submarine swap eksternal untuk memindahkan sats ke wallet on-chain kamu, termasuk kembali ke on-chain Zeus. Menjaga keseimbangan antara inbound dan outbound liquidity itu penting, dan kamu juga bisa menggunakan kembali sats tersebut untuk membuka channel baru jika diperlukan.


### Wrapped Invoice


Jika kamu ingin menambah privasi saat menerima, kamu bisa menggunakan metode "wrapped invoice". Ingat, untuk bisa memakai ini, kamu harus punya channel dengan Olympus LSP. Wrapped invoice akan menyembunyikan tujuan akhir (node Zeus kamu) dan menampilkan node LSP sebagai tujuan kepada pembayar.


Untuk mendapatkan wrapped invoice, buka layar keypad utama, masukkan jumlah, lalu tekan request. Akan muncul QR invoice biasa. Setelah itu, tekan tombol "X" di kanan atas untuk membuka opsi lanjutan invoice.

![Image](assets/en/14.webp)


Sekarang kamu perlu mengaktifkan opsi di atas yang bertuliskan "Aktifkan LSP" lalu tekan tombol "Buat Invoice". Opsi ini akan membuat wrapped invoice dan ingat, ada sedikit biaya yang dikenakan.


### Invoice dengan routing hint


Ini fitur yang sangat berguna jika kamu ingin mengelola likuiditas di beberapa channel inbound. Secara praktis, kamu bisa menentukan channel inbound mana yang ingin kamu pakai untuk menerima sats dari invoice tersebut.


Fitur ini juga bisa dipakai untuk rebalancing melingkar, yaitu saat kamu ingin memindahkan likuiditas dari channel yang sudah penuh ke channel lain yang masih kosong.


Bagaimana cara membuat invoice dengan routing hint?


- Di layar utama, geser ke kanan drawer LN lalu klik "Terima".  
- Di pengaturan invoice, scroll ke bawah dan aktifkan opsi "Sisipkan routing hint", lalu pilih tab "Custom". Akan muncul daftar channel yang tersedia. Pilih channel yang ingin kamu gunakan untuk menerima.  
- Isi detail invoice lainnya seperti jumlah, memo, dan lain-lain, lalu tekan "Buat Invoice".  
- Saat invoice dibayar, sats akan masuk ke channel yang sudah kamu tentukan.


Jika kamu ingin membayar invoice untuk keperluan rebalancing (melingkar), dan kamu membayarnya dari node Zeus yang sama, di layar pembayaran pilih channel keluar (yang memiliki likuiditas lebih besar) sebagai sumber pembayaran.


### Bayar dengan Keysend


Keysend adalah fitur Lightning yang sering diremehkan, padahal sangat berguna dan sebaiknya lebih sering dipakai.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) memungkinkan pengguna di Lightning Network untuk mengirim pembayaran kepada orang lain, langsung ke kunci publik mereka, selama node mereka memiliki saluran publik dan mengaktifkan keysend. Keysend tidak mengharuskan penerima pembayaran untuk mengeluarkan Invoice.


Jadi, bagaimana kamu melakukannya di Zeus?


Cukup pindai atau salin nodeID tujuan (atau gunakan buku kontak Zeus untuk menyimpan node tujuan yang sering kamu pakai), lalu dari layar utama Zeus tekan tombol "Kirim". Di layar itu, tempel nodeID atau pilih langsung dari kontak kamu.


Masukkan jumlah sats, tambahkan pesan jika perlu (ya, kamu juga bisa menggunakannya sebagai chat rahasia lewat LN), lalu tekan tombol "Kirim". Selesai!


![Image](assets/en/15.webp)


Jika kamu memiliki channel langsung dengan peer tujuan, TIDAK ada biaya tambahan yang dikenakan.


Jika kamu tidak memiliki channel langsung dengan peer tujuan, maka pembayaran keysend akan dikenakan biaya seperti pembayaran Lightning invoice biasa, karena dirutekan melalui jalur normal seperti transaksi lainnya. Namun ingat, keysend tidak meninggalkan jejak sebagai Lightning invoice.


## Kesimpulan


Aku sarankan untuk membaca panduan tindak lanjut [Penggunaan lanjutan Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) dengan lebih banyak instruksi dan kasus penggunaan.


Dan... selesai! Mulai sekarang kamu cukup memakai Zeus Node sebagai BTC/LN wallet biasa di ponsel kamu. UI-nya cukup sederhana, mudah digunakan, dan intuitif untuk semua jenis pengguna. Aku rasa tidak perlu lagi menjelaskan lebih lanjut tentang cara mengirim dan menerima pembayaran.

Sebagai kesimpulan, berikut ini adalah bagan privasi perbandingan :


![Image](assets/en/16.webp)
