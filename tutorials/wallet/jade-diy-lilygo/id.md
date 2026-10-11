---
name: Jade DIY
description: Mengubah papan pengembangan seharga $15 menjadi perangkat keras Bitcoin yang berfungsi penuh wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Membangun untuk Pemula


**Penonton:** Pembangun yang penasaran dengan sedikit atau tanpa pengalaman embedded.


**Durasi:** 2 jam (fleksibel)


**Hasil yang diharapkan:** Pada akhirnya, siswa akan:



- Mengenal model keamanan hardware wallet DIY dibandingkan perangkat komersial.
- Merakit perangkat penandatanganan berbasis mikrokontroler.
- Mem-flash firmware open-source dan memverifikasi checksum build.
- Menandatangani dan menyiarkan transaksi mainnet menggunakan perangkat baru mereka.


---

## Abstrak


Lokakarya 2 jam ini mengajarkan pemula untuk membuat hardware wallet Bitcoin yang fungsional dengan mem-flash firmware Jade open-source ke papan T-Display LilyGO seharga $15. Siswa mengubah perangkat keras pengembangan umum menjadi perangkat penandatanganan yang sebanding dengan hardware wallet komersial seharga $150, sambil mempelajari dasar-dasar keamanan lewat pengalaman langsung, bukan hanya teori.


### Filosofi


Membangun perangkat penandatanganan sendiri bukan cuma soal menghemat uang, tapi juga tentang memahami teknologi yang melindungi Bitcoin kamu. Lokakarya ini mengusung "keamanan melalui pemahaman" dibandingkan sekadar percaya pada kotak hitam. Dengan mencari sendiri sumber komponen, mem-flash firmware open-source, dan menghasilkan entropi sendiri, siswa mengurangi risiko rantai pasokan sekaligus belajar mengevaluasi klaim keamanan secara kritis. Tujuannya adalah otonomi yang terinformasi: siswa harus memahami kekuatan dan keterbatasan perangkat DIY mereka dibandingkan alternatif komersial yang sudah jadi.



---

## Konsep Dasar (15 menit)


### Apa Itu Self-Custody dan Mengapa Itu Penting?


Bitcoin diciptakan untuk menghilangkan kebutuhan akan pihak ketiga tepercaya, seperti bank dan perusahaan, dari sistem uang kita. Alih-alih mengandalkan kepercayaan, Bitcoin menggunakan matematika, fisika, dan kriptografi untuk memberi kekuatan kepada siapa pun agar bisa memiliki dan mengendalikan uang mereka tanpa memerlukan izin dari siapa pun.


Cara kerjanya adalah bitcoin tercatat di buku besar digital global yang disebut blockchain, atau bitcoin timechain, yaitu buku besar publik dan transparan yang dijalankan oleh jaringan komputer, bukan buku besar terpusat seperti rekening bank.


Hal penting yang perlu dipahami adalah bahwa untuk memindahkan bitcoin dari satu tempat ke tempat lain, kamu harus menandatangani transaksi menggunakan private key. Anggap saja seperti membuka brankas dengan kata sandi, lalu memindahkan bitcoin ke brankas milik orang lain. Bitcoin memberi kamu kekuatan untuk memegang kunci brankas itu sendiri, alih-alih bergantung pada bank untuk memindahkan uangmu.


Dengan kekuatan besar datang tanggung jawab besar. Jika kunci hilang, danamu juga hilang selamanya. Dalam konteks ini, kamu bisa menganggap kunci brankas tersebut sebagai uang itu sendiri. Walaupun kunci tidak sama dengan bitcoin, kunci adalah mekanisme untuk memindahkan dana kamu dan karena itu harus benar-benar dilindungi. Inilah alasan munculnya ungkapan "not your keys, not your coins".


Istilah self-custody mungkin terdengar membingungkan, tetapi artinya sederhana: memegang private key sendiri dan mengendalikan bitcoin kamu sendiri. Jika kamu tidak memegang kunci tersebut, berarti kamu mempercayai pihak lain untuk memegangnya. Jika bitcoin kamu berada di ETF atau di bursa (Mt. Gox, FTX, Coinbase, Binance, dll.), kamu sebenarnya tidak memiliki bitcoin, kamu hanya memiliki klaim atas bitcoin tersebut. Ini menimbulkan berbagai risiko, seperti bursa diretas dan kehilangan bitcoin pengguna, atau perusahaan meminjamkan dana pengguna dan hanya menyimpan sebagian kecil sebagai cadangan. Selain itu, pihak ketiga memiliki kendali penuh atas uangmu dan dapat membatasi atau bahkan membekukan penarikan.



![image](assets/fr/01.webp)


Dengan self-custody, kamu menghilangkan unsur kepercayaan dari persamaan. Tidak ada yang bisa membekukan dana kamu atau menolak transaksi, kamu bisa mengirim uang melintasi batas negara, kepada siapa pun, kapan pun, tanpa memerlukan rekening bank, kartu identitas, atau persetujuan dari siapa pun. Tidak ada yang bisa menghentikan, menyensor, atau mencuri dari kamu, sehingga membuka kekuatan penuh bitcoin sebagai uang kebebasan. Inilah alasan kenapa kita mengatakan bahwa dengan bitcoin kamu bisa menjadi bank bagi diri sendiri.


Bitcoin diciptakan untuk memecahkan masalah manipulasi kepercayaan dan uang, sebuah jalan keluar dari sistem keuangan saat ini. Namun, jalan keluar itu hanya bekerja jika kamu memegang sendiri kuncinya. Karena itulah self-custody menjadi sangat penting.


### Apa yang dimaksud dengan Wallet?

Istilah wallet sebenarnya agak menyesatkan dan karena itu bisa membingungkan. Memang benar bahwa bitcoin wallet, seperti wallet fisik, menyimpan nilai. Namun perbedaan utamanya adalah wallet Bitcoin tidak benar-benar menyimpan bitcoin.


Bitcoin hanya ada sebagai entri pada buku besar di blockchain publik, atau sebagai brankas metaforis di dunia maya. Ingat, untuk memindahkan bitcoin kamu harus menggunakan kunci untuk membuka brankas tersebut dan memindahkan koin ke tempat lain. Private key itulah yang digunakan untuk membelanjakan bitcoin. Saat kamu melakukan transaksi dengan wallet, sebenarnya kamu hanya menggunakan kunci tersebut untuk menandatangani transaksi. Dengan cara inilah kamu membuktikan bahwa kamu memiliki dana dan berhak membelanjakan koin-koin itu.


Wallet Bitcoin pada dasarnya hanya menyimpan private key kamu, jadi secara teknis lebih tepat kalau disebut sebagai gantungan kunci.


### Hot Wallet vs Cold Wallet


Hot allet adalah aplikasi software di ponsel atau komputer kamu. Aplikasi ini terhubung ke internet, sehingga lebih mudah digunakan dan lebih cepat untuk menandatangani transaksi, tetapi itu juga berarti lebih rentan terhadap peretas, malware, dan phishing. Disebut "panas" karena selalu terhubung ke internet, aktif, dan menyala. Contohnya adalah mobile wallet atau browser wallet.


Di sisi lain, cold wallet, atau hardware wallet, adalah perangkat yang membuat dan menyimpan kunci kamu secara offline. Ini menghilangkan peluang seseorang meretas dana kamu dan jauh lebih aman untuk penyimpanan jangka panjang. Namun, perangkat ini perlu digunakan setiap kali menandatangani transaksi sehingga bisa terasa kurang praktis.


### Model Ancaman Hardware Wallet


Hardware wallet ada untuk memecahkan masalah mendasar: bagaimana kamu menandatangani transaksi Bitcoin tanpa mengekspos private key ke komputer yang terhubung ke internet yang bisa disusupi malware atau penyerang jarak jauh? Model ancaman utamanya mengasumsikan bahwa laptop atau ponsel yang kamu gunakan sehari-hari berpotensi diserang. Hardware wallet menciptakan lingkungan terisolasi di mana private key tidak pernah meninggalkan perangkat, dan proses penandatanganan transaksi terjadi di dalam secure element atau mikrokontroler yang hanya mengirimkan tanda tangan kembali ke komputer host, bukan kuncinya. Bahkan jika komputer kamu sepenuhnya disusupi, penyerang tetap tidak bisa mencuri bitcoin tanpa akses fisik ke perangkat dan PIN kamu.


Namun, hardware wallet juga menghadirkan ancaman tersendiri. Kamu harus percaya bahwa produsennya tidak menanamkan backdoor, rantai pasokan tidak dirusak, dan proses pembuatan angka acak benar-benar acak. Penyerang fisik bisa mengekstrak kunci melalui serangan side-channel atau manipulasi chip, dan seseorang yang memiliki akses sementara dapat memodifikasi perangkat kamu. Membangun hardware wallet sendiri membantu kamu memahami kompromi ini. Kamu akan membuat keputusan soal secure element versus mikrokontroler tujuan umum, cara memverifikasi transaksi di layar, serta cara melindungi dari ancaman jarak jauh dan fisik. Tujuannya bukan keamanan yang sempurna, tetapi memahami ancaman ma


### Konsep Utama



- **Entropi dan seedphrase:** wallet kamu hanya seaman tingkat keacakan yang membentuknya. Kita akan menggabungkan generator angka acak perangkat dengan metode sederhana yang bisa dilakukan manusia, seperti lemparan dadu, lalu mengubah entropi tersebut menjadi 12 atau 24 kata [seedphrase BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), dan meninggalkan sesi ini dengan cadangan tertulis atau logam yang benar-benar kamu percayai.
- **Kebersihan seedphrase:** Perlakukan seedphrase seperti kunci utama tabungan kamu. Jangan pernah mengetikkan kata-katanya di ponsel atau komputer, karena keylogger, tangkapan layar, atau cadangan cloud bisa membocorkannya selamanya. Simpan seedphrase secara offline, taruh di tempat yang hanya bisa kamu akses, dan biasakan membacanya dengan lantang sebelum kamu pergi.
- **Secure element + mikrokontroler:** Bayangkan secure element sebagai brankas dan mikrokontroler sebagai otaknya. Secure element menjaga private key dengan ketahanan terhadap manipulasi, sementara mikrokontroler menangani layar, tombol, dan logika firmware. Perlu diingat bahwa hardware wallet yang kita buat di sini tidak memiliki secure element. Ini bukan berarti tidak aman, tetapi tingkat perlindungannya lebih rendah.
- **Memercayai firmware:** Firmware adalah sistem operasi tersembunyi dari wallet. Selalu unduh dari rilis yang sudah ditandai, periksa hash yang dipublikasikan, dan pahami bahwa reproducible build memungkinkan banyak orang mengompilasi kode yang sama dan menghasilkan biner yang identik. Jika checksum tidak cocok, jangan lanjut menandatangani.


---

## Apa yang Kita Bangun?


Kami menggunakan perangkat keras generik, LilyGo T-Display, dan menginstal firmware Jade SDK di atasnya. [Jade Plus](https://blockstream.com/jade/jade-plus/) adalah wallet sumber terbuka, yang biasanya berharga $150:


![image](assets/fr/02.webp)


Hari ini, kami akan mem-flash firmware mereka ke perangkat keras seharga $15.


### Apa yang Harus Dibeli


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB dengan cangkang, model K164)** - [Pesan langsung dari LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) dengan harga sekitar $15. Papan ESP32 ini menyediakan layar, tombol, dan antarmuka USB yang mirip dengan Jade Plus dari Blockstream. ESP32 onboard juga menyertakan radio Wi-Fi dan Bluetooth. Kita akan mem-flash firmware yang menonaktifkan keduanya, tetapi fitur tersebut tetap menjadi bagian dari model ancaman karena kode berbahaya bisa saja mengaktifkannya kembali.
- **Kabel USB-C** - Bawalah kabel yang mendukung transfer data agar kamu bisa mem-flash firmware dan menyalakan papan langsung dari laptop (aman untuk penggunaan di kelas).


### Mengapa Membangun Hardware Wallet Anda Sendiri?



- Hemat sekitar $135 dibandingkan dengan membeli perangkat komersial.
- Bangun kenyamanan dengan flashing firmware, elemen yang aman, dan higienis wallet.
- Putar perangkat penandatanganan tambahan untuk menyebarkan tabungan ke beberapa dompet.
- Kurangi risiko rantai pasokan dengan mencari dan merakit sendiri setiap komponen.
- Ingatlah mantra Lopp: kedaulatan dan kenyamanan selalu bertentangan.


## Pengaturan Fisik


### Persiapkan Casing Kamu


Kamu punya dua pilihan untuk menempatkan papan T-Display LilyGO: casing hasil cetak 3D atau penutup resmi dari LilyGO. Casing cetak bisa ditemukan dan dicetak dari [model ini](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Casing ini memberikan pelindung yang ringan dan bisa disesuaikan untuk perangkat kamu.



![image](assets/fr/04.webp)


Sebagai alternatif, kamu bisa menggunakan casing resmi LilyGO, yang memberikan tingkat presisi dan hasil akhir yang sedikit berbeda, dengan perlindungan yang lebih kuat dan tampilan yang lebih rapi.


![image](assets/fr/05.webp)


Perlu diperhatikan bahwa casing cetak dan casing resmi memiliki perbedaan kecil dalam desain dan cara perakitan. Apa pun pilihan kamu, pastikan papan terpasang dengan benar di dalam casing agar tidak terjadi koneksi longgar atau kerusakan.


### Memeriksa Papan


Sebelum lanjut, periksa dengan cermat papan T-Display LilyGO kamu untuk memastikan tidak ada cacat atau serpihan yang terlihat. Pastikan layar, tombol, dan port USB-C bersih serta bebas dari debu atau sisa solder. Tangani papan dengan hati-hati, dan perhatikan keamanan pelepasan muatan listrik statis (ESD) dengan mengardekan diri atau menggunakan tali ESD untuk mencegah kerusakan pada komponen sensitif.


### Hubungkan ke Laptop Kamu


Gunakan kabel USB-C yang mendukung transfer data untuk menyambungkan papan LilyGO ke laptop kamu. Koneksi ini akan memberi daya sekaligus memungkinkan kamu mem-flash firmware.


Saat boot, kamu akan melihat layar berikut:



![image](assets/fr/06.webp)



Ketika dinyalakan, LilyGO akan menampilkan layar uji warna yang berputar melalui warna-warna solid. Hal ini mengonfirmasi bahwa layar dan papan berfungsi dengan benar sebelum mem-flash firmware.


Setelah tes warna selesai, layar akan kembali ke kondisi default, yang mengindikasikan bahwa papan siap untuk langkah selanjutnya dalam proses pembuatan.


![image](assets/fr/07.webp)


## Cara Mudah atau Cara Sulit


Ada dua pendekatan utama untuk mem-flash firmware hardware wallet kamu: cara mudah dan cara sulit. Cara mudah menggunakan alat yang sudah dikonfigurasi sebelumnya atau flasher berbasis web yang secara otomatis memuat firmware ke perangkat dengan input minimal. Metode ini ideal untuk pemula yang ingin hasil cepat atau lebih suka menghindari kerumitan debugging dan penggunaan command line. Prosesnya lebih sederhana dan membuat perangkat lebih cepat siap digunakan, sehingga cocok untuk siapa pun yang baru mengenal pengembangan embedded atau hardware wallet.


Di sisi lain, cara sulit menggunakan tools command line secara manual untuk mem-flash firmware. Pendekatan ini mengharuskan kamu memverifikasi tanda tangan dan checksum firmware untuk memastikan keaslian dan integritasnya, sehingga memberi pemahaman yang lebih dalam tentang proses flashing dan bagaimana firmware berinteraksi dengan perangkat keras. Walaupun membutuhkan usaha lebih dan keterbiasaan dengan perintah terminal, metode ini memberi kontrol, transparansi, dan tingkat kepercayaan yang lebih tinggi terhadap keamanan perangkat kamu.


Setiap metode punya kelebihan dan kekurangan. Cara mudah mengorbankan sebagian tingkat verifikasi dan pemahaman demi kecepatan serta kenyamanan, sedangkan cara sulit memerlukan lebih banyak waktu dan keterampilan teknis tetapi memberi fleksibilitas dan pemahaman yang lebih kuat terhadap teknologi dasarnya. Instruktur sebaiknya mendorong siswa memilih cara yang paling sesuai dengan tingkat kenyamanan dan rasa ingin tahu mereka, sehingga kepercayaan diri dan semangat eksplorasi tetap berkembang.



## Cara Mudah


Cara termudah untuk mem-flash ESP32



- Buka Github resmi Blockstream: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Kamu dapat mengunduh file sumber dan menjalankan situs web secara lokal, tetapi GitHub telah menghostingnya di [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub menyajikan HTML, CSS, JavaScript, dll. secara langsung ke peramban kamu sehingga Anda bisa mem-flash perangkat tanpa menginstal alat pengembang.


![image](assets/fr/09.webp)



- Buka menu dropdown (kemungkinan besar default-nya adalah `M5Stack Core2`) dan pilih papan pengembangan kamu - untuk kelas ini, pilih `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Saat kamu mengklik flash, jendela ini akan muncul. Untuk mengetahui perangkat mana yang merupakan LILYGO, cabut dulu LilyGO lalu pasang kembali. Port COM yang digunakan LilyGO akan muncul dan menghilang. Pilih port COM yang terhubung ke Jade.


![image](assets/fr/11.webp)



- Itu saja, bilah kemajuan akan muncul dan ketika selesai, Anda siap untuk mengaturnya


## Menyiapkan Jade Wallet


Setelah firmware berhasil di-flash, LilyGO T-Display kamu sekarang sudah menjadi hardware wallet Jade yang berfungsi penuh. Bagian ini akan memandu kamu melalui proses penyiapan awal, mulai dari membuat seedphrase hingga menghubungkan perangkat dengan software wallet seperti Sparrow atau aplikasi mobile Blockstream Green.


### Boot Awal dan Pengaturan Perangkat


- **Nyalakan perangkat:** Dengan LilyGO masih terhubung ke laptop kamu melalui USB-C, firmware Jade akan otomatis melakukan boot. Kamu akan melihat logo Jade muncul di layar.



- **Masuk ke mode penyiapan:** Perangkat akan menampilkan menu awal. Gunakan dua tombol fisik pada papan untuk navigasi:
 - **Tombol kiri:** Pindah ke atas/kembali
 - **Tombol kanan:** Bergerak ke bawah/maju
 - **Kedua tombol bersamaan:** Pilih/konfirmasi



- **Pilih "Setup":** Arahkan ke opsi Setup lalu tekan kedua tombol untuk konfirmasi. Perangkat akan memandu kamu melalui proses konfigurasi awal.


### Membuat Wallet Kamu



- **Pilih "Mulai Penyiapan":** Perangkat akan meminta kamu memulai proses pembuatan wallet. Konfirmasikan pilihan tersebut.



- **Pilih "Buat Wallet Baru":** Kamu akan melihat dua opsi:
 - **Buat Wallet Baru:** Menghasilkan seedphrase baru (pilih ini untuk lokakarya)
 - **Pulihkan Wallet:** Memulihkan wallet yang sudah ada dari seedphrase (untuk pengguna tingkat lanjut)
- Pilih "Buat Wallet Baru" dan konfirmasi.



- **Menghasilkan entropi:** Perangkat akan menggunakan generator angka acak untuk membuat entropi kriptografis. Proses ini membutuhkan beberapa detik karena perangkat mengumpulkan keacakan dari berbagai sumber.


### Mencatat Seedphrase Kamu



- **Tuliskan seedphrase kamu:** Perangkat sekarang akan menampilkan seedphrase BIP39 berisi 12 kata, satu per satu. Ini adalah langkah paling penting dalam seluruh proses.



**Praktik keamanan yang penting:**


- Tuliskan setiap kata dengan jelas di atas kertas (gunakan kartu seedphrase yang disediakan jika tersedia)
- Periksa kembali setiap kata saat kamu menulisnya
- Jangan pernah memotret seedphrase dengan ponsel
- Jangan pernah mengetikkan kata-katanya ke komputer atau ponsel apa pun
- Jaga seedphrase tetap rahasia, jangan bagikan layar atau menunjukkannya kepada orang lain



- **Verifikasi seedphrase kamu:** Setelah menuliskan 12 kata, perangkat akan meminta kamu mengonfirmasi beberapa kata dari seedphrase tersebut untuk memastikan semuanya tercatat dengan benar. Gunakan tombol untuk memilih kata yang tepat pada setiap prompt.


**Kiat pro:** Sebelum lanjut, biasakan membaca kembali seedphrase kamu dengan suara pelan (tanpa terdengar orang lain). Ini membantu menemukan kesalahan penulisan atau ambiguitas sejak awal.

### Metode Koneksi



- **Pilih jenis koneksi:** Firmware Jade mendukung dua metode koneksi:
 - **USB:** Koneksi kabel melalui USB-C (direkomendasikan untuk lokakarya ini)
 - **Bluetooth:** Koneksi nirkabel ke perangkat mobile



- Pilih **USB** untuk sekarang, karena ini adalah opsi paling mudah untuk software wallet desktop dan tidak menambahkan vektor serangan nirkabel.



- **Penamaan perangkat:** Jade akan menampilkan pengenal unik seperti "Connect Jade A7D924". Pengenal ini membantu kamu membedakan beberapa hardware wallet jika nanti membuat lebih dari satu. Catat pengenal ini jika perlu.


### Menghubungkan ke Software Wallet


Sekarang kamu punya dua opsi utama untuk berinteraksi dengan hardware wallet yang baru kamu buat: aplikasi mobile Blockstream Green (untuk penggunaan saat bepergian) atau Sparrow Wallet (untuk penggunaan desktop dengan fitur yang lebih advanced). Untuk lokakarya ini, kita akan fokus pada Sparrow Wallet karena memberikan visibilitas yang lebih jelas terhadap detail teknis transaksi Bitcoin.



#### Opsi 1: Aplikasi Mobile Blockstream Green (Mulai Cepat)


Jika kamu ingin menguji perangkat secara cepat menggunakan perangkat mobile:



- Unduh aplikasi **Blockstream Green** dari App Store (iOS) atau Google Play (Android)
- Buka aplikasi lalu pilih "Hubungkan Hardware Wallet"
- Pilih "Jade" dari daftar perangkat yang didukung
- Hubungkan Jade ke ponsel menggunakan kabel USB-C ke USB-C (atau adaptor USB-C ke Lightning untuk iPhone 15+)
- Ikuti petunjuk di layar untuk menghubungkan dan membuat wallet pertama kamu


**Catatan tentang Liquid:** Aplikasi Blockstream Green mendukung Bitcoin dan Liquid (sidechain Bitcoin). Jika kamu menggunakan fitur Liquid, kamu mungkin akan diminta untuk "Export master blinding key". Ini memungkinkan aplikasi melihat jumlah transaksi di jaringan Liquid yang secara default bersifat rahasia. Untuk pelatihan ini, kamu bisa melewati fitur Liquid dan fokus pada transaksi Bitcoin standar.


#### Opsi 2: Sparrow Wallet (Direkomendasikan untuk Lokakarya)


Sparrow Wallet adalah aplikasi desktop yang kuat yang memberi kamu kontrol granular atas transaksi Bitcoin dan terhubung dengan mulus ke hardware wallet Jade kamu.


**Instalasi:**



- Unduh Sparrow Wallet dari situs web resmi: [sparrowwallet.com](https://sparrowwallet.com)
- Verifikasi tanda tangan unduhan (lihat dokumentasi Sparrow untuk detailnya)
- Instal lalu jalankan aplikasinya



**Menghubungkan Jade kamu ke Sparrow:**



- Di Sparrow, buka **File → New Wallet**
- Beri nama wallet kamu (misalnya, "My Jade Wallet")
- Klik **Connect Hardware Wallet**
- Sparrow akan otomatis mendeteksi perangkat Jade yang terhubung
- Jika diminta, konfirmasikan koneksi di layar Jade dengan menekan kedua tombol
- Pilih jenis script yang kamu inginkan:
 - **Native Segwit (P2WPKH):** Direkomendasikan untuk pemula, biaya lebih rendah dan kompatibilitas luas dengan wallet modern
 - **Nested Segwit (P2SH-P2WPKH):** Untuk kompatibilitas dengan layanan yang lebih lama
 - **Taproot (P2TR):** Paling advanced, menawarkan privasi lebih baik dan biaya lebih rendah, tetapi membutuhkan dukungan wallet yang lebih baru
- Klik **Import Keystore** untuk menyelesaikan koneksi


**Mengonfigurasi Koneksi Server Sparrow:**


Sebelum kamu bisa melihat saldo atau menyiarkan transaksi, Sparrow harus terhubung ke node Bitcoin untuk mengambil data blockchain. Kamu punya beberapa opsi, masing-masing dengan kompromi berbeda antara kenyamanan, privasi, dan tingkat kepercayaan:



- **Electrum Server Publik (Paling mudah, paling tidak privat):** Terhubung ke server publik yang dijalankan pihak ketiga. Cepat disiapkan, tetapi server bisa melihat alamat wallet kamu dan berpotensi menautkannya ke alamat IP kamu. Cocok untuk pengujian di testnet.
 - Di Sparrow, buka **Tools → Preferences → Server**
 - Pilih **Public Server** lalu pilih server dari daftar
 - Klik **Test Connection** untuk memverifikasi




- **Bitcoin Core atau Knots Node (Paling privat, paling banyak usaha):** Menjalankan node Bitcoin sendiri secara penuh. Ini adalah standar emas untuk privasi dan verifikasi, karena kamu memvalidasi setiap transaksi sendiri dan tidak perlu mempercayai server pihak lain. Namun, metode ini membutuhkan pengunduhan seluruh blockchain (~600GB) dan menjaga node tetap tersinkronisasi.
 - Instal dan sinkronkan Bitcoin Core atau Knots
 - Di Sparrow, buka **Tools → Preferences → Server**
 - Pilih **Bitcoin Core atau Knots** lalu masukkan detail koneksi node kamu



- **Electrum Server Pribadi (Keseimbangan yang baik):** Jalankan server Electrum sendiri (seperti Fulcrum atau Electrs) yang terhubung ke node Bitcoin Core atau Knots kamu. Opsi ini menawarkan privasi penuh tanpa harus menjalankan Sparrow di mesin yang sama dengan node.
 - Siapkan server Electrum yang terhubung ke node Bitcoin Core atau Knots kamu
 - Di Sparrow, buka **Tools → Preferences → Server**
 - Pilih **Private Electrum** lalu masukkan URL server kamu


Untuk lokakarya ini, menggunakan **Public Electrum Server** sudah cukup untuk transaksi testnet. Namun untuk penggunaan produksi dengan dana sungguhan, sebaiknya pertimbangkan menjalankan node sendiri atau memakai server pribadi tepercaya agar privasi tetap maksimal.


#### Opsi 3: Aplikasi Desktop Blockstream Green (Mulai Cepat)


Blockstream Green adalah perangkat lunak untuk menyelesaikan pengaturan JadeDIY dan harus dengan versi desktop



- Dapatkan aplikasi resmi Blockstream - ini adalah tautan ke sana dari situs web mereka. Setelah kamu berada di sana, klik [Unduh sekarang](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Tergantung di mana kamu mengunduh, kemungkinan besar file tersebut ada di folder Unduhan. Periksa di sana dan klik dua kali file yang dapat dieksekusi untuk menginstal perangkat lunak.


![image](assets/fr/13.webp)



- Kamu mungkin perlu memberikan izin admin untuk menjalankan installer. Setelah itu, jendela seperti pada gambar berikut akan muncul, klik **Next**.


![image](assets/fr/14.webp)



- Pilih lokasi tempat kamu ingin menginstal aplikasi (bisa di folder program seperti biasa atau di lokasi yang mudah ditemukan), lalu klik **Next**.


![image](assets/fr/15.webp)



- Penginstal akan menanyakan nama pintasan. Masukkan salah satu atau biarkan default, lalu klik **Next**.


![image](assets/fr/16.webp)



- Jika kamu menginginkan pintasan desktop, centang kotak; jika tidak, klik **Next**.


![image](assets/fr/17.webp)



- Terakhir, klik **Instal** dan tunggu beberapa menit sampai proses instalasi selesai.


![image](assets/fr/18.webp)



- Bilah kemajuan harus terisi sampai akhir.


![image](assets/fr/19.webp)



- Setelah selesai, halaman baru akan muncul - klik **Selesai**.


![image](assets/fr/20.webp)



- Temukan aplikasi Blockstream yang baru saja diinstal (contoh yang ditampilkan di menu Start Windows 11).


![image](assets/fr/21.webp)



- Setelah kamu menemukannya, klik untuk meluncurkan - layar pembuka akan muncul.


### Memverifikasi Pengaturan Kamu


Setelah terhubung ke Sparrow (atau aplikasi wallet lainnya):



- **Periksa alamat kamu:** Sparrow akan menampilkan alamat penerima yang berasal dari seedphrase kamu. Kamu bisa memverifikasi alamat tersebut di perangkat Jade dengan membuka tab "Receive" di Sparrow lalu klik "Show Address". Alamat akan muncul di layar komputer dan juga di layar Jade.




- **Buat alamat penerima:** Klik tab **Receive** di Sparrow lalu salin alamat penerima Bitcoin pertama kamu.



- **Siap untuk transaksi:** Hardware wallet kamu sekarang sudah sepenuhnya terkonfigurasi dan siap menerima serta menandatangani transaksi Bitcoin. Lanjutkan ke bagian berikutnya untuk berlatih menandatangani transaksi testnet.



---

### Daftar Periksa Penyiapan Cepat



- Firmware Jade berhasil melakukan boot
- Wallet baru dibuat dengan seedphrase 12 kata
- Seedphrase ditulis dengan jelas dan sudah diverifikasi
- Mode koneksi USB sudah dipilih
- Software wallet (Sparrow) sudah diinstal dan terhubung
- Koneksi server sudah dikonfigurasi (Public Electrum untuk mainnet)
- Alamat penerima pertama sudah dibuat dan diverifikasi di perangkat



---

**Lisensi MIT**


**Hak Cipta (c) 2025 The Bitcoin Network NYC**


Dengan ini diberikan izin, secara cuma-cuma, kepada setiap orang yang mendapatkan salinan perangkat lunak ini dan file dokumentasi terkait ("Perangkat Lunak"), untuk bertransaksi dengan Perangkat Lunak tanpa batasan, termasuk tanpa batasan hak untuk menggunakan, menyalin, memodifikasi, menggabungkan, mempublikasikan, mendistribusikan, mensublisensikan, dan/atau menjual salinan Perangkat Lunak, dan untuk mengizinkan orang-orang yang menerima Perangkat Lunak tersebut untuk melakukan hal tersebut, dengan tunduk pada persyaratan berikut ini:


Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus disertakan dalam semua salinan atau bagian penting dari Perangkat Lunak.


PERANGKAT LUNAK INI DISEDIAKAN "SEBAGAIMANA ADANYA", TANPA JAMINAN DALAM BENTUK APA PUN, BAIK TERSURAT MAUPUN TERSIRAT, TERMASUK NAMUN TIDAK TERBATAS PADA JAMINAN UNTUK DAPAT DIPERJUALBELIKAN, KESESUAIAN UNTUK TUJUAN TERTENTU, DAN TANPA PELANGGARAN. DALAM HAL APAPUN, PENULIS ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB ATAS KLAIM, KERUSAKAN, ATAU TANGGUNG JAWAB LAINNYA, BAIK DALAM TINDAKAN KONTRAK, PERBUATAN MELAWAN HUKUM, ATAU LAINNYA, YANG TIMBUL DARI, AKIBAT, ATAU SEHUBUNGAN DENGAN PERANGKAT LUNAK ATAU PENGGUNAAN ATAU TRANSAKSI LAIN DALAM PERANGKAT LUNAK.


---
