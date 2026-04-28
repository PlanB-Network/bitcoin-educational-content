---
name: Jade DIY
description: Mengubah papan pengembangan seharga $15 menjadi perangkat keras Bitcoin yang berfungsi penuh wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Membangun Pemula


**Penonton:** Pembangun yang penasaran dengan sedikit atau tanpa pengalaman yang tertanam.


**Durasi:** 2 jam (fleksibel)


**Hasil yang diharapkan:** Pada akhirnya, siswa akan:



- Kenali model keamanan dompet perangkat keras DIY versus perangkat komersial.
- Merakit perangkat penandatanganan berbasis mikrokontroler.
- Flash firmware sumber terbuka dan verifikasi checksum build.
- Menandatangani dan menyiarkan transaksi mainnet menggunakan perangkat baru mereka.


---

## Abstrak


Lokakarya 2 jam ini mengajarkan para pemula untuk membuat perangkat keras Bitcoin wallet yang fungsional dengan mem-flash firmware Jade open-source ke papan T-Display LilyGO seharga $15. Para siswa mengubah perangkat keras pengembangan umum menjadi perangkat penandatanganan yang sebanding dengan dompet komersial seharga $150, mempelajari dasar-dasar keamanan melalui pengalaman langsung dan bukan hanya teori.


### Filosofi


Membangun perangkat penandatanganan Anda sendiri bukan hanya tentang menghemat uang-ini tentang memahami teknologi yang melindungi Bitcoin Anda. Lokakarya ini merangkul "keamanan melalui pemahaman" daripada kepercayaan kotak hitam. Dengan mencari sumber komponen, mem-flash firmware sumber terbuka, dan menghasilkan entropi sendiri, para siswa mengurangi risiko rantai pasokan sambil belajar mengevaluasi klaim keamanan secara kritis. Tujuannya adalah otonomi yang terinformasi: siswa harus memahami kekuatan dan keterbatasan perangkat DIY mereka dibandingkan dengan alternatif komersial yang sudah jadi.


---

## Konsep Dasar (15 menit)


### Apa itu Penitipan Mandiri dan Mengapa Itu Penting?


Bitcoin diciptakan untuk menghilangkan kebutuhan akan pihak ketiga yang terpercaya, seperti bank dan perusahaan dari sistem uang kita. Alih-alih menggunakan kepercayaan, bitcoin menggunakan matematika, fisika, dan kriptografi untuk memberikan kekuatan kepada siapa pun untuk memiliki dan mengendalikan uang mereka tanpa memerlukan izin siapa pun.


Cara kerjanya adalah bitcoin ada di buku besar digital global yang disebut blockchain alias bitcoin timechain, yang merupakan buku besar publik dan transparan yang dijalankan oleh komputer, bukan buku besar terpusat seperti rekening bank.


Hal yang penting untuk dipahami adalah untuk memindahkan bitcoin dari satu tempat ke tempat lain, Anda harus menandatangani transaksi tersebut dengan apa yang disebut sebagai private key. Anggap saja seperti membuka brankas dengan kata sandi, dan memindahkan bitcoin ke brankas orang lain. Bitcoin memberikan Anda kekuatan untuk memegang kunci brankas itu sendiri, alih-alih mengandalkan bank untuk memindahkan uang Anda.


Dengan kekuatan yang besar datanglah tanggung jawab yang besar, kehilangan kunci dan dana Anda hilang selamanya. Dengan cara ini, Anda dapat menganggap kunci brankas sebagai uang itu sendiri. Walaupun kunci tidak sama dengan bitcoin, kunci adalah mekanisme untuk memindahkan dana Anda dan oleh karena itu sangat penting untuk dilindungi. Inilah mengapa kami mengatakan "bukan kunci Anda, bukan koin Anda".


Istilah self-custody mungkin terdengar membingungkan, tetapi yang dimaksud adalah memegang kunci pribadi Anda sendiri, dan mengendalikan bitcoin Anda sendiri. Jika Anda tidak memegang kunci tersebut, Anda mempercayai orang lain untuk memegangnya untuk Anda. Jika bitcoin Anda berada di ETF atau di bursa (Mt. Gox, FTX, Coinbase, Binance, dll.), Anda tidak memiliki bitcoin, Anda hanya memiliki klaim atas bitcoin. Hal ini menimbulkan berbagai macam risiko, seperti bursa yang diretas dan kehilangan bitcoin Anda atau perusahaan yang meminjamkan uang Anda dan hanya memberikan sebagian kecil sebagai cadangan. Selain itu, pihak ketiga yang tidak tepercaya akan memiliki kendali penuh atas uang Anda dan dapat membatasi atau membekukan penarikan.


![image](assets/fr/01.webp)


Dengan penyimpanan mandiri, Anda menghilangkan kepercayaan dari persamaan. Tidak ada yang bisa membekukan dana Anda atau menolak transaksi, Anda bisa mengirim uang melintasi batas negara, kepada siapa pun, kapan pun, dan Anda tidak memerlukan rekening bank, kartu identitas, atau persetujuan siapa pun. Tidak ada yang dapat menghentikan Anda, menyensor Anda, atau mencuri dari Anda, membuka kekuatan penuh bitcoin sebagai uang kebebasan. Inilah mengapa kami katakan, dengan bitcoin Anda bisa menjadi bank Anda sendiri.


Bitcoin diciptakan untuk memecahkan masalah manipulasi kepercayaan dan uang, sebuah jalan keluar dari sistem kita saat ini, tetapi jalan keluarnya hanya berfungsi jika Anda mengambil kuncinya. Inilah sebabnya mengapa penitipan mandiri sangat penting.


### Apa yang dimaksud dengan Wallet?


Istilah wallet adalah istilah yang sedikit keliru dan oleh karena itu dapat membingungkan. Ya, memang benar bahwa bitcoin wallet, seperti halnya wallet fisik, menyimpan nilai. Namun perbedaan utamanya adalah dompet bitcoin tidak benar-benar menyimpan bitcoin.


Bitcoin hanya ada sebagai entri buku besar di blockchain publik, atau di dalam brankas metaforis di dunia maya. Ingatlah bahwa untuk memindahkan bitcoin, Anda harus menggunakan kunci Anda untuk membuka brankas dan memindahkan koin ke tempat lain, kunci pribadi itulah yang digunakan untuk membelanjakan bitcoin. Ketika Anda melakukan transaksi dengan wallet Anda, Anda benar-benar hanya menggunakan kunci Anda untuk menandatangani transaksi. Dengan cara inilah Anda menunjukkan bukti bahwa Anda memiliki uang tersebut dan memiliki hak untuk membelanjakan koin-koin tersebut.


Dompet Bitcoin sebenarnya hanya menyimpan kunci pribadi Anda, jadi akan lebih tepat jika disebut sebagai gantungan kunci.


### Dompet Hot vs Dompet Cold


wallet panas adalah aplikasi perangkat lunak di ponsel atau komputer Anda. Aplikasi ini terhubung ke internet, sehingga lebih mudah digunakan dan lebih cepat untuk menandatangani transaksi, tetapi ini juga berarti aplikasi ini lebih rentan terhadap peretas, malware, dan phishing. Disebut "panas" karena terhubung ke internet, dicolokkan dan dinyalakan. Contohnya adalah telepon wallet atau browser wallet.


Di sisi lain, wallet dingin, atau wallet perangkat keras, adalah perangkat yang membuat dan menyimpan kunci Anda secara offline. Hal ini menghilangkan kemampuan seseorang untuk meretas dana Anda dan jauh lebih aman untuk tabungan jangka panjang, namun perangkat ini diperlukan untuk menandatangani setiap transaksi dan bisa jadi kurang nyaman.


### Model Ancaman Hardware Wallet


Dompet perangkat keras ada untuk memecahkan masalah mendasar: bagaimana Anda menandatangani transaksi Bitcoin tanpa mengekspos kunci pribadi Anda ke komputer yang terhubung ke internet yang dapat disusupi oleh malware atau penyerang jarak jauh? Model ancaman inti mengasumsikan bahwa laptop atau ponsel yang Anda gunakan sehari-hari berpotensi untuk diserang. Perangkat keras wallet menciptakan sebuah lingkungan yang terisolasi di mana private key tidak pernah meninggalkan perangkat, dan penandatanganan transaksi terjadi di dalam secure element atau mikrokontroler yang hanya mengomunikasikan tanda tangan kembali ke komputer host, bukan kunci itu sendiri. Bahkan jika komputer Anda benar-benar disusupi, penyerang tidak dapat mencuri Bitcoin Anda tanpa akses fisik ke perangkat dan PIN Anda.


Akan tetapi, dompet perangkat keras memperkenalkan ancaman mereka sendiri. Anda harus percaya bahwa produsennya tidak memperkenalkan pintu belakang, rantai suplai tidak dirusak, dan pembuatan nomor acak benar-benar acak. Penyerang fisik dapat mengekstrak kunci melalui serangan saluran samping atau manipulasi chip, dan seseorang yang memiliki akses sementara dapat memodifikasi perangkat Anda. Membangun perangkat keras Anda sendiri wallet membantu Anda memahami pengorbanan ini - Anda akan membuat keputusan tentang elemen yang aman versus mikrokontroler tujuan umum, cara memverifikasi transaksi pada layar, dan cara melindungi dari ancaman jarak jauh dan fisik. Tujuannya bukanlah keamanan yang sempurna, tetapi memahami ancaman mana yang Anda lindungi dan mana yang masih ada.


### Konsep Utama



- Entropi dan frasa seed:** wallet Anda hanya seaman keacakan yang melahirkannya. Kami akan mencampur generator angka acak perangkat dengan trik yang mudah digunakan manusia seperti lemparan dadu, mengubah entropi tersebut menjadi 12 atau 24 kata [frasa BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), dan meninggalkan ruangan dengan cadangan tertulis atau logam yang Anda percayai.
- Kebersihan frasa kata sandi:** Perlakukan seed seperti kunci utama tabungan Anda. Jangan pernah mengetikkan kata-katanya di ponsel atau komputer-keylogger, tangkapan layar, dan cadangan awan dapat membocorkannya selamanya. Simpanlah frasa tersebut secara offline, simpan di suatu tempat yang hanya bisa diakses oleh Anda, dan latihlah untuk membacanya dengan lantang sebelum Anda pergi.
- Elemen aman + mikrokontroler:** Bayangkan secure element sebagai lemari besi dan mikrokontroler sebagai otaknya. secure element menjaga kunci pribadi dengan ketahanan terhadap gangguan, sedangkan mikrokontroler menangani layar, tombol, dan logika firmware. Perhatikan bahwa dompet perangkat keras yang kami buat saat ini tidak memiliki secure element. Ini bukan berarti tidak aman, hanya saja tingkat proteksinya lebih rendah.
- Memercayai firmware:** Firmware adalah sistem operasi yang tidak terlihat dari wallet. Selalu unduh dari rilis yang ditandai, periksa hash yang dipublikasikan, dan pahami bahwa build yang dapat direproduksi memungkinkan beberapa orang mengkompilasi kode yang sama dan menghasilkan biner yang sama persis. Jika checksum tidak cocok, Anda tidak perlu menandatangani.


---

## Apa yang Kita Bangun?


Kami menggunakan perangkat keras generik, LilyGo T-Display, dan menginstal firmware Jade SDK di atasnya. Jade Plus] (https://blockstream.com/jade/jade-plus/) adalah wallet sumber terbuka, yang biasanya berharga $150:


![image](assets/fr/02.webp)


Hari ini, kami akan mem-flash firmware mereka ke perangkat keras seharga $15.


### Apa yang Harus Dibeli


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB dengan cangkang, model K164)** - [Pesan langsung dari LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) dengan harga sekitar $15. Papan ESP32 ini menyediakan tampilan, tombol, dan antarmuka USB yang mirip dengan Jade Plus dari Blockstream. ESP32 onboard juga menyertakan radio Wi-Fi dan Bluetooth; kami akan mengirimkan firmware yang membuat mereka dinonaktifkan, tetapi mereka membentuk model ancaman Anda karena kode berbahaya dapat menghidupkannya kembali.
- Kabel USB-C** - Bawalah kabel berkemampuan data sehingga Anda dapat melakukan flash firmware dan menyalakan papan langsung dari laptop Anda (tidak masalah untuk penggunaan di kelas).


### Mengapa Membangun Hardware Wallet Anda Sendiri?



- Hemat sekitar $135 dibandingkan dengan membeli perangkat komersial.
- Bangun kenyamanan dengan flashing firmware, elemen yang aman, dan higienis wallet.
- Putar perangkat penandatanganan tambahan untuk menyebarkan tabungan ke beberapa dompet.
- Kurangi risiko rantai pasokan dengan mencari dan merakit sendiri setiap komponen.
- Ingatlah mantra Lopp: kedaulatan dan kenyamanan selalu bertentangan.


## Pengaturan Fisik


### Persiapkan Kasus Anda


Anda memiliki dua pilihan untuk menempatkan papan T-Display LilyGO Anda: casing cetak 3D atau penutup resmi LilyGO. Casing cetak dapat ditemukan dan dicetak dari [model ini](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Casing ini menawarkan cangkang yang ringan dan dapat disesuaikan untuk perangkat Anda.


![image](assets/fr/04.webp)


Sebagai alternatif, Anda dapat menggunakan casing LilyGO resmi, yang memberikan kesesuaian dan hasil akhir yang sedikit berbeda, menawarkan perlindungan yang lebih kuat dan tampilan yang dipoles.


![image](assets/fr/05.webp)


Perhatikan bahwa casing yang dicetak dan casing resmi sedikit berbeda dalam hal desain dan perakitan. Opsi apa pun yang Anda pilih, pastikan papan terpasang dengan benar di dalam casing untuk menghindari koneksi yang longgar atau kerusakan.


### Memeriksa Papan


Sebelum melanjutkan, periksa dengan cermat papan T-Display LilyGO Anda untuk mengetahui adanya cacat atau serpihan yang terlihat. Pastikan layar, tombol, dan port USB-C bersih dan bebas dari debu atau percikan solder. Tangani papan dengan hati-hati, dan perhatikan keamanan pelepasan muatan listrik statis (ESD) dengan mengardekan diri Anda sendiri atau menggunakan tali pengikat ESD untuk mencegah kerusakan pada komponen sensitif.


### Hubungkan ke Laptop Anda


Dengan menggunakan kabel USB-C berkemampuan data, sambungkan papan LilyGO ke laptop Anda. Koneksi ini akan memberikan daya dan memungkinkan Anda untuk mem-flash firmware.


Saat boot, Anda akan disambut dengan layar berikut ini:


![image](assets/fr/06.webp)



Ketika dinyalakan, LilyGO akan menampilkan layar uji warna yang berputar melalui warna-warna solid. Hal ini mengonfirmasi bahwa layar dan papan berfungsi dengan benar sebelum mem-flash firmware.


Setelah tes warna selesai, layar akan kembali ke kondisi default, yang mengindikasikan bahwa papan siap untuk langkah selanjutnya dalam proses pembuatan.


![image](assets/fr/07.webp)


## Cara Mudah atau Cara Hard


Ada dua pendekatan utama untuk mem-flash firmware wallet perangkat keras Anda: cara yang mudah dan cara yang sulit. Cara mudah menggunakan alat yang sudah dikonfigurasi sebelumnya atau flasher berbasis web yang secara otomatis memuat firmware ke perangkat Anda dengan input minimal. Metode ini sangat ideal untuk pemula yang ingin menang cepat atau lebih suka menghindari kerumitan debugging dan interaksi baris perintah. Metode ini menyederhanakan proses dan membuat Anda lebih cepat aktif dan berjalan, sehingga dapat diakses oleh mereka yang baru mengenal pengembangan tertanam atau dompet perangkat keras.


Di sisi lain, cara yang sulit adalah dengan menggunakan alat bantu baris perintah secara manual untuk mem-flash firmware. Pendekatan ini memerlukan verifikasi tanda tangan dan checksum firmware untuk memastikan keaslian dan integritasnya, sehingga memberi Anda pemahaman yang lebih dalam tentang proses flashing dan bagaimana firmware berinteraksi dengan perangkat keras. Meskipun membutuhkan lebih banyak usaha dan keakraban dengan perintah terminal, pendekatan ini menawarkan kontrol yang lebih besar, transparansi, dan kepercayaan diri dalam keamanan perangkat Anda.


Setiap metode memiliki kekurangan dan kelebihan: cara yang mudah mengorbankan tingkat kepercayaan dan pemahaman demi kecepatan dan kenyamanan, sedangkan cara yang sulit membutuhkan lebih banyak waktu dan keterampilan teknis, namun memberi Anda fleksibilitas dan pemahaman yang lebih kuat tentang teknologi yang mendasarinya. Instruktur harus mendorong siswa untuk memilih cara yang paling sesuai dengan tingkat kenyamanan dan keingintahuan mereka, sehingga dapat memupuk rasa percaya diri dan eksplorasi.


## Cara Mudah


Cara termudah untuk mem-flash ESP32



- Buka Github resmi Blockstream: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Anda dapat mengunduh file sumber dan menjalankan situs web secara lokal, tetapi GitHub telah menghostingnya di [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub menyajikan HTML, CSS, JavaScript, dll. secara langsung ke peramban Anda sehingga Anda bisa mem-flash perangkat tanpa menginstal alat pengembang.


![image](assets/fr/09.webp)



- Buka menu dropdown (kemungkinan besar default-nya adalah `M5Stack Core2`) dan pilih papan pengembangan Anda - untuk kelas ini, pilih `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Ketika Anda mengklik flash, ini akan muncul. Untuk mengetahui perangkat mana yang merupakan LILYGO, cabut lilygo dan pasang kembali. Port com yang digunakan Lilygo akan muncul dan menghilang. Klik port COM yang dicolokkan ke Jade


![image](assets/fr/11.webp)



- Itu saja, bilah kemajuan akan muncul dan ketika selesai, Anda siap untuk mengaturnya


## Menyiapkan Jade Wallet


Setelah firmware berhasil di-flash, LilyGO T-Display Anda sekarang menjadi perangkat keras Jade wallet yang berfungsi penuh. Bagian ini akan memandu Anda melalui proses penyiapan awal, mulai dari membuat frasa seed hingga menghubungkan perangkat dengan perangkat lunak wallet seperti Sparrow atau aplikasi seluler Blockstream Green.


### Boot Awal dan Pengaturan Perangkat



- Nyalakan perangkat:** Dengan LilyGO yang masih terhubung ke laptop Anda melalui USB-C, firmware Jade akan melakukan booting secara otomatis. Anda akan melihat logo Jade muncul di layar.



- Masuk ke mode penyiapan:** Perangkat akan menampilkan menu awal. Gunakan dua tombol fisik pada papan untuk menavigasi:
 - Tombol kiri:** Pindah ke atas/belakang
 - Tombol kanan:** Bergerak ke bawah/maju
 - Kedua tombol secara bersamaan:** Pilih/konfirmasi



- Pilih "Setup":** Navigasikan ke pilihan Setup dan tekan kedua tombol untuk mengonfirmasi. Perangkat akan memandu Anda melalui proses konfigurasi awal.


### Menciptakan Wallet Anda



- Pilih "Mulai Penyiapan":** Perangkat akan meminta Anda untuk memulai proses pembuatan wallet. Konfirmasikan pilihan Anda.



- Pilih "Buat Wallet Baru":** Anda akan disajikan dengan dua pilihan:
 - Buat Wallet Baru:** Menghasilkan frasa seed baru (pilih ini untuk lokakarya)
 - Pulihkan Wallet:** Memulihkan wallet yang ada dari frasa seed (untuk pengguna tingkat lanjut)



- Pilih "Buat Wallet Baru" dan konfirmasi.



- Menghasilkan entropi:** Perangkat akan menggunakan generator angka acak untuk membuat entropi kriptografi. Proses ini memerlukan waktu beberapa detik karena perangkat mengumpulkan keacakan dari berbagai sumber.


### Merekam Frasa Benih Anda



- Tuliskan frasa seed Anda:** Perangkat sekarang akan menampilkan frasa BIP39 seed 12 kata, satu kata per satu. Ini adalah langkah yang paling penting dalam keseluruhan proses.


**Praktik keamanan yang penting:**


- Tuliskan setiap kata dengan jelas di atas kertas (gunakan kartu frasa seed yang disediakan jika tersedia)
- Periksa kembali setiap kata saat Anda menulisnya
- Jangan sekali-kali memotret frasa seed dengan ponsel Anda
- Jangan pernah mengetikkan kata-kata tersebut ke dalam komputer atau ponsel apa pun
- Jaga kerahasiaan frasa seed Anda-jangan bagikan layar atau tunjukkan kepada orang lain



- Verifikasi frasa seed Anda:** Setelah menuliskan ke-12 kata, perangkat akan meminta Anda untuk mengonfirmasi beberapa kata dari frasa tersebut untuk memastikan bahwa Anda merekamnya dengan benar. Gunakan tombol untuk memilih kata yang benar untuk setiap prompt.


**Kiat pro:** Sebelum melanjutkan, berlatihlah membaca frasa seed Anda kembali ke diri Anda sendiri dengan suara keras (tanpa suara, sehingga orang lain tidak dapat mendengarnya). Hal ini membantu menangkap kesalahan tulisan tangan atau ambiguitas.


### Metode Koneksi



- Pilih jenis koneksi:** Firmware Jade mendukung dua metode koneksi:
 - USB:** Sambungan kabel melalui kabel USB-C (direkomendasikan untuk bengkel ini)
 - Bluetooth:** Koneksi nirkabel ke perangkat seluler



- Pilih **USB** untuk saat ini, karena ini adalah opsi yang paling mudah untuk perangkat lunak wallet desktop dan tidak memperkenalkan vektor serangan nirkabel.



- Penamaan perangkat:** Jade akan menampilkan pengenal unik seperti "Connect Jade A7D924". Pengidentifikasi ini membantu Anda membedakan antara beberapa dompet perangkat keras jika Anda akhirnya membuat lebih dari satu. Catatlah pengenal ini jika diinginkan.


### Menghubungkan ke Perangkat Lunak Wallet


Anda sekarang memiliki dua opsi utama untuk berinteraksi dengan perangkat keras wallet yang baru Anda buat: aplikasi seluler Blockstream Green (untuk penggunaan di mana saja) atau Sparrow Wallet (untuk penggunaan desktop dengan fitur-fitur yang lebih canggih). Untuk lokakarya ini, kita akan fokus pada Sparrow Wallet, karena menawarkan visibilitas yang lebih baik ke dalam detail teknis transaksi Bitcoin.


#### Opsi 1: Aplikasi Seluler Blockstream Green (Mulai Cepat)


Jika Anda ingin menguji perangkat Anda secara cepat dengan perangkat seluler:



- Unduh aplikasi **Blockstream Green** dari App Store (iOS) atau Google Play (Android)
- Buka aplikasi dan pilih "Hubungkan Hardware Wallet"
- Pilih "Jade" dari daftar perangkat yang didukung
- Colokkan Jade Anda ke ponsel Anda menggunakan kabel USB-C ke USB-C (atau adaptor USB-C ke Lightning untuk iPhone 15+)
- Ikuti petunjuk di layar untuk menghubungkan dan membuat wallet pertama Anda


**Catatan tentang Liquid:** Aplikasi Blockstream Green mendukung Bitcoin dan Liquid (sidechain Bitcoin). Jika Anda menggunakan fitur Liquid, Anda mungkin akan diminta untuk "Export master blinding key" - ini memungkinkan aplikasi untuk melihat jumlah transaksi di jaringan Liquid, yang seharusnya bersifat rahasia. Untuk pelatihan ini, Anda dapat melewatkan fitur Liquid dan fokus pada transaksi Bitcoin standar.


#### Opsi 2: Sparrow Wallet (Direkomendasikan untuk Bengkel)


Sparrow Wallet adalah aplikasi desktop yang kuat yang memberi Anda kontrol granular atas transaksi Bitcoin Anda dan terhubung dengan mulus dengan perangkat keras Jade wallet Anda.


**Instalasi:**



- Unduh Sparrow Wallet dari situs web resmi: [sparrowwallet.com](https://sparrowwallet.com)
- Verifikasi tanda tangan unduhan (lihat dokumentasi Sparrow untuk detailnya)
- Menginstal dan meluncurkan aplikasi


**Menghubungkan Giok Anda ke Sparrow:**



- Di Sparrow, buka **File → New Wallet**
- Berikan nama pada wallet Anda (misalnya, "My Jade Wallet")
- Klik **Terhubung Hardware Wallet**
- Sparrow akan secara otomatis mendeteksi perangkat Jade Anda yang dicolokkan
- Jika diminta, konfirmasikan koneksi pada layar Jade dengan menekan kedua tombol
- Pilih jenis naskah yang Anda inginkan:
 - Native Segwit (P2WPKH):** Direkomendasikan untuk pemula-biaya terendah, kompatibilitas terluas dengan dompet modern
 - Nested Segwit (P2SH-P2WPKH):** Untuk kompatibilitas dengan layanan yang lebih lama
 - Taproot (P2TR):** Paling canggih, menawarkan privasi terbaik dan biaya terendah, tetapi membutuhkan dukungan wallet yang mutakhir
- Klik **Import Keystore** untuk menyelesaikan koneksi


**Mengkonfigurasi Koneksi Server Sparrow:**


Sebelum Anda dapat melihat saldo atau menyiarkan transaksi, Sparrow harus terhubung ke node Bitcoin untuk mengambil data blockchain. Anda memiliki beberapa opsi, masing-masing dengan pengorbanan yang berbeda antara kenyamanan, privasi, dan kepercayaan:



- Electrum Server Publik (Paling mudah, paling tidak privat):** Menghubungkan ke server publik yang dioperasikan oleh pihak ketiga. Cepat untuk disiapkan, tetapi server dapat melihat alamat wallet Anda dan berpotensi menautkannya ke alamat IP Anda. Baik untuk pengujian di testnet.
 - Di Sparrow, buka **Tools → Preferensi → Server**
 - Pilih **Public Server** dan pilih server dari daftar
 - Klik **Uji Koneksi** untuk memverifikasi



- Bitcoin Core atau Knot Node (Paling privat, paling banyak bekerja):** Jalankan node Bitcoin Anda sendiri secara penuh. Ini adalah standar emas untuk privasi dan verifikasi, karena Anda memvalidasi setiap transaksi sendiri dan tidak mempercayai server orang lain. Namun, ini membutuhkan pengunduhan seluruh blockchain (~600GB) dan menjaga node Anda tetap tersinkronisasi.
 - Memasang dan menyinkronkan Bitcoin Core atau Knot
 - Di Sparrow, buka **Tools → Preferensi → Server**
 - Pilih **Bitcoin Core atau Knot** dan masukkan detail koneksi node Anda



- Electrum Server Pribadi (Keseimbangan yang baik):** Hos server Electrum Anda sendiri (seperti Fulcrum atau Electrs) yang terhubung ke node Bitcoin Core atau Knot Anda. Menawarkan privasi penuh tanpa perlu menjalankan Sparrow pada mesin yang sama dengan node Anda.
 - Siapkan server Electrum yang mengarah ke node Bitcoin Core atau Knot Anda
 - Di Sparrow, buka **Tools → Preferensi → Server**
 - Pilih **Private Electrum** dan masukkan URL server Anda


Untuk lokakarya ini, menggunakan **Public Electrum Server** tidak masalah untuk transaksi testnet. Dalam lingkungan produksi dengan dana sungguhan, Anda sebaiknya mempertimbangkan untuk menjalankan node Anda sendiri atau menggunakan server pribadi yang tepercaya untuk privasi maksimum.


#### Opsi 3: Aplikasi Desktop Blockstream Green (Mulai Cepat)


Blockstream Green adalah perangkat lunak untuk menyelesaikan pengaturan JadeDIY dan harus dengan versi desktop



- Dapatkan aplikasi resmi Blockstream - ini adalah tautan ke sana dari situs web mereka. Setelah Anda berada di sana, klik [Unduh sekarang](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Tergantung di mana Anda mengunduh, kemungkinan besar file tersebut ada di folder Unduhan. Periksa di sana dan klik dua kali file yang dapat dieksekusi untuk menginstal perangkat lunak.


![image](assets/fr/13.webp)



- Anda mungkin harus memberikan hak admin untuk menjalankan penginstal. Setelah Anda melakukannya, sebuah jendela akan muncul yang akan terlihat seperti gambar berikut - klik **Next**.


![image](assets/fr/14.webp)



- Pilih di mana Anda ingin menempatkan aplikasi yang terinstal (lokasi yang sama dengan program Anda yang lain atau di suatu tempat yang mudah ditemukan), lalu klik **Next**.


![image](assets/fr/15.webp)



- Penginstal akan menanyakan nama pintasan. Masukkan salah satu atau biarkan default, lalu klik **Next**.


![image](assets/fr/16.webp)



- Jika Anda menginginkan pintasan desktop, centang kotak; jika tidak, klik **Next**.


![image](assets/fr/17.webp)



- Terakhir, klik **Instal** dan tunggu beberapa menit sampai proses instalasi selesai.


![image](assets/fr/18.webp)



- Bilah kemajuan harus terisi sampai akhir.


![image](assets/fr/19.webp)



- Setelah selesai, halaman baru akan muncul - klik **Selesai**.


![image](assets/fr/20.webp)



- Temukan aplikasi Blockstream yang baru saja diinstal (contoh yang ditampilkan di menu Start Windows 11).


![image](assets/fr/21.webp)



- Setelah Anda menemukannya, klik untuk meluncurkan - layar pembuka akan muncul.


### Memverifikasi Pengaturan Anda


Setelah terhubung ke Sparrow (atau aplikasi wallet lainnya):



- Periksa alamat Anda:** Sparrow akan menampilkan alamat penerima yang berasal dari frasa seed Anda. Anda dapat memverifikasi alamat pada perangkat Jade Anda dengan membuka tab "Terima" di Sparrow dan mengklik "Tampilkan Address" -alamat tersebut akan muncul di layar komputer dan layar Jade.



- Buat alamat penerima:** Klik tab **Terima** pada Sparrow dan salin alamat penerima Bitcoin Anda yang pertama.



- Siap untuk transaksi:** Perangkat keras wallet Anda sekarang sudah terkonfigurasi sepenuhnya dan siap untuk menerima dan menandatangani transaksi Bitcoin. Lanjutkan ke bagian berikutnya untuk berlatih menandatangani transaksi testnet.



---

### Daftar Periksa Penyiapan Cepat



- Firmware Jade berhasil melakukan booting
- wallet baru dibuat dengan frasa seed 12 kata
- Frasa benih ditulis dengan jelas dan diverifikasi
- Mode koneksi USB yang dipilih
- Perangkat lunak Wallet (Sparrow) diinstal dan terhubung
- Koneksi server dikonfigurasikan (Electrum publik untuk mainnet)
- Alamat penerima pertama yang dibuat dan diverifikasi pada perangkat



---

**Lisensi MIT**


**Hak Cipta (c) 2025 The Bitcoin Network NYC**


Dengan ini diberikan izin, secara cuma-cuma, kepada setiap orang yang mendapatkan salinan perangkat lunak ini dan file dokumentasi terkait ("Perangkat Lunak"), untuk bertransaksi dengan Perangkat Lunak tanpa batasan, termasuk tanpa batasan hak untuk menggunakan, menyalin, memodifikasi, menggabungkan, mempublikasikan, mendistribusikan, mensublisensikan, dan/atau menjual salinan Perangkat Lunak, dan untuk mengizinkan orang-orang yang menerima Perangkat Lunak tersebut untuk melakukan hal tersebut, dengan tunduk pada persyaratan berikut ini:


Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus disertakan dalam semua salinan atau bagian penting dari Perangkat Lunak.


PERANGKAT LUNAK INI DISEDIAKAN "SEBAGAIMANA ADANYA", TANPA JAMINAN DALAM BENTUK APA PUN, BAIK TERSURAT MAUPUN TERSIRAT, TERMASUK NAMUN TIDAK TERBATAS PADA JAMINAN UNTUK DAPAT DIPERJUALBELIKAN, KESESUAIAN UNTUK TUJUAN TERTENTU, DAN TANPA PELANGGARAN. DALAM HAL APAPUN, PENULIS ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB ATAS KLAIM, KERUSAKAN, ATAU TANGGUNG JAWAB LAINNYA, BAIK DALAM TINDAKAN KONTRAK, PERBUATAN MELAWAN HUKUM, ATAU LAINNYA, YANG TIMBUL DARI, AKIBAT, ATAU SEHUBUNGAN DENGAN PERANGKAT LUNAK ATAU PENGGUNAAN ATAU TRANSAKSI LAIN DALAM PERANGKAT LUNAK.


---