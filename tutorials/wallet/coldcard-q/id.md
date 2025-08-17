---
name: COLDCARD Q
description: Menyiapkan dan menggunakan COLDCARD Q
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang dirancang khusus untuk mengelola dan mengamankan private key dompet Bitcoin. Tidak seperti dompet perangkat lunak (hot wallet) yang dipasang di perangkat umum dan hampir selalu terhubung ke Internet, dompet perangkat keras menjaga private key tetap terisolasi secara fisik, sehingga mengurangi risiko peretasan maupun pencurian.

Tujuan utama dompet perangkat keras adalah mengurangi fungsionalitas perangkat seminimal mungkin untuk memperkecil attack surface. Attack surface yang lebih kecil berarti lebih sedikit vektor serangan potensial, yaitu semakin sedikit titik lemah dalam sistem yang bisa dieksploitasi oleh penyerang untuk mendapatkan akses ke Bitcoin.

Menggunakan dompet perangkat keras sangat disarankan untuk mengamankan Bitcoin kamu, terutama kalau kamu menyimpannya dalam jumlah besar, baik dari segi nilai absolut maupun proporsinya terhadap total aset yang kamu punya.

Dompet perangkat keras dipakai bersama perangkat lunak manajemen dompet di komputer atau smartphone. Perangkat lunak tersebut membuat dan mengelola transaksi, tapi tanda tangan kriptografi yang diperlukan supaya transaksi valid hanya dilakukan di dalam dompet perangkat keras. Dengan begitu, private key kamu nggak akan pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras memberi perlindungan ganda buat kamu: di satu sisi, dompet ini melindungi Bitcoin kamu dari serangan jarak jauh dengan menjaga private key tetap offline, dan di sisi lain, perangkat ini punya ketahanan fisik yang lebih tinggi terhadap upaya ekstraksi kunci. Berdasarkan dua kriteria keamanan ini, kita bisa menilai dan mengklasifikasikan berbagai model yang ada di pasaran.

Dalam tutorial ini, aku ingin memperkenalkan kepada kamu, salah satu solusi tersebut: **COLDCARD Q**.

---
Karena COLDCARD Q menawarkan banyak sekali fungsi, aku usulkan untuk membagi penggunaannya ke dalam dua tutorial. Dalam tutorial pertama ini, kita akan membahas konfigurasi awal dan fungsi dasar perangkat. Lalu, dalam tutorial kedua, kita akan melihat bagaimana cara memanfaatkan semua opsi lanjutan COLDCARD kamu.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## Memperkenalkan COLDCARD Q

COLDCARD Q adalah dompet perangkat keras khusus Bitcoin yang dikembangkan oleh perusahaan asal Kanada, Coinkite, yang sebelumnya dikenal lewat seri MK. Q merupakan produk mereka yang paling canggih sejauh ini, dan diposisikan sebagai dompet perangkat keras Bitcoin terbaik.

Dari sisi hardware, COLDCARD Q hadir dengan semua fitur yang dibutuhkan untuk memberikan pengalaman pengguna yang optimal:

- Layar LCD yang besar menyederhanakan navigasi dan pengoperasian;
- Keyboard QWERTY lengkap;
- Kamera terintegrasi untuk memindai kode QR;
- Dua slot kartu microSD ;
- Opsi daya yang sepenuhnya terisolasi melalui tiga baterai AAA (tidak termasuk), atau melalui kabel USB-C ;
- Dua Secure Element dari dua produsen berbeda untuk memberikan lapisan keamanan tambahan;
- Kemampuan untuk berkomunikasi melalui NFC.

Menurutku, COLDCARD Q cuma punya dua kekurangan. Pertama, karena fiturnya banyak, ukurannya jadi cukup besar, dengan panjang hampir 13 cm dan lebar 8 cm, kurang lebih seukuran smartphone kecil. Bodinya juga agak tebal karena ada slot baterai. Kalau kamu cari dompet perangkat keras yang lebih kecil dan gampang dibawa, MK4 yang jauh lebih ringkas mungkin bisa jadi pilihan lebih tepat. Kekurangan kedua jelas ada di harga, yaitu **$239.99** di situs resmi, sekitar $72 lebih mahal dibanding MK4. Ini bikin Q bersaing langsung dengan dompet perangkat keras premium seperti Ledger Flex atau Foundation Passport.

![CCQ](assets/fr/001.webp)

Dari sisi perangkat lunak, COLDCARD Q dilengkapi dengan baik seperti perangkat Coinkite lainnya, dengan sejumlah fitur canggih:


- Dice Roll untuk menghasilkan frasa pemulihan Anda sendiri;
- Kode PIN ;
- Hitung mundur ke kunci PIN terakhir;
- Frasa sandi BIP39 ;
- PIN penguncian akhir;
- Hitung mundur koneksi ;
- SeedXOR;
- BIP85

Singkatnya, COLDCARD Q memberi pengalaman pengguna yang lebih baik dibanding MK4, dan bisa dibilang ideal untuk pengguna tingkat menengah sampai mahir yang ingin kemudahan penggunaan lebih maksimal.

COLDCARD Q tersedia untuk dijual [di situs web resmi Coinkite] (https://store.coinkite.com/store/coldcard). Bisa juga dibeli dari pengecer.

## Mempersiapkan tutorial

Setelah kamu menerima COLDCARD, langkah pertama adalah memeriksa kemasannya untuk memastikan segelnya belum dibuka. Kalau kemasannya rusak, itu bisa jadi tanda kalau dompet perangkat keras sudah disusupi dan mungkin tidak asli.

![CCQ](assets/fr/002.webp)

Apabila kamu membuka kotak, kamu akan menemukan item berikut ini:


- COLDCARD Q dalam kantong tertutup;
- Kartu untuk merekam frasa mnemonik Anda.

![CCQ](assets/fr/003.webp)

Pastikan tas masih tersegel dan tidak rusak. Periksa juga apakah nomor pada tas sesuai dengan nomor yang tertera di kertas di dalamnya. Simpan nomor ini untuk referensi di kemudian hari.
![CCQ](assets/fr/004.webp)

Kalau kamu lebih suka memberi daya pada COLDCARD tanpa menghubungkannya ke komputer (air-gap), masukkan tiga baterai AAA ke bagian belakang perangkat. Atau, kamu juga bisa menyambungkannya ke komputer lewat kabel USB-C.

![CCQ](assets/fr/005.webp)

Untuk tutorial ini, kamu juga membutuhkan Sparrow Wallet untuk mengelola dompet Bitcoin di komputermu. Download [Sparrow Wallet] (https://sparrowwallet.com/download/) dari situs web resminya. Aku sangat menyarankanmu untuk memeriksa keasliannya (dengan GnuPG) dan integritasnya (melalui hash) sebelum melanjutkan instalasi. Kalau tidak tahu bagaimana cara melakukannya, ikuti tutorial ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Pemilihan kode PIN

Sekarang kamu dapat mengaktifkan COLDCARD dengan menekan tombol di sudut kiri atas.

![CCQ](assets/fr/006.webp)

Tekan tombol "*ENTER*" untuk menerima persyaratan penggunaan.

![CCQ](assets/fr/007.webp)

COLDCARD Q kemudian akan menampilkan nomor di bagian atas layar. Pastikan nomor ini sama dengan nomor yang tertera di kantong tersegel dan pada potongan plastik di dalamnya. Ini untuk memastikan paket kamu tidak dibuka sejak dikemas oleh Coinkite sampai kamu menerimanya. Tekan "*ENTER*" untuk melanjutkan.

![CCQ](assets/fr/008.webp)

Masuk ke menu "*Pilih Kode PIN*" dan konfirmasikan dengan tombol "*ENTER*".

![CCQ](assets/fr/009.webp)

Kode PIN ini dipakai untuk membuka kunci COLDCARD kamu. Jadi, PIN berfungsi sebagai perlindungan dari akses fisik yang tidak sah. PIN ini tidak terlibat dalam derivasi kunci kriptografi dompet kamu. Artinya, meskipun tanpa PIN, selama kamu punya frasa mnemonik, kamu tetap bisa memulihkan akses ke Bitcoin.

PIN COLDCARD dibagi menjadi dua bagian: awalan dan akhiran, masing-masing bisa terdiri dari 2 sampai 6 digit, dengan total 4 hingga 12 digit. Saat membuka kunci COLDCARD, pertama kamu masukkan awalan, lalu perangkat akan menampilkan 2 kata. Setelah itu baru masukkan akhiran. Dua kata ini diberikan ke kamu saat proses konfigurasi, dan harus disimpan baik-baik karena akan selalu dibutuhkan setiap kali membuka kunci COLDCARD. Kalau dua kata yang muncul sesuai dengan yang kamu simpan saat konfigurasi, itu berarti perangkat kamu belum pernah disusupi sejak terakhir dipakai.

Klik sekali lagi pada "*Pilih PIN*"

![CCQ](assets/fr/010.webp)

Konfirmasikan bahwa kamu telah membaca peringatan tersebut.

![CCQ](assets/fr/011.webp)

Sekarang kamu akan memilih kode PIN kamu. Disarankan untuk membuat PIN yang panjang dan acak. Pastikan kamu menyimpan PIN ini di tempat yang berbeda dari tempat menyimpan COLDCARD. Kamu bisa menggunakan kartu yang sudah disertakan dalam paket untuk mencatat PIN ini.

Masukkan awalan yang kamu pilih, lalu tekan tombol "*ENTER*" untuk mengonfirmasi bagian pertama kode PIN.

![CCQ](assets/fr/012.webp)

Dua kata anti-phishing kemudian akan muncul di layar kamu. Simpan baik-baik untuk referensi di masa mendatang. Kamu bisa menggunakan kartu yang disertakan dalam paket untuk menuliskannya.

![CCQ](assets/fr/013.webp)

Kemudian masukkan bagian kedua dari kode PIN dan tekan "*ENTER*".

![CCQ](assets/fr/014.webp)

Konfirmasikan PIN dengan memasukkannya untuk kedua kalinya, periksa apakah dua kata anti-phishing sesuai dengan yang kamu simpan sebelumnya.

![CCQ](assets/fr/015.webp)

Mulai sekarang, setiap kali kamu membuka kunci COLDCARD, ingatlah untuk memeriksa validitas dua kata anti-phishing yang muncul di layar setelah Anda memasukkan awalan kode PIN.

## Pembaruan firmware

Ketika menggunakan perangkat kamu untuk pertama kalinya, penting untuk memeriksa dan memperbarui firmware. Untuk melakukannya, akses menu "*Tingkat Lanjut/Alat*".

![CCQ](assets/fr/016.webp)

**Penting:** Jika kamu berencana untuk meng-upgrade firmware dan ini bukan pertama kalinya kamu menggunakan COLDCARD (misalnya, kamu sudah memiliki dompet yang dibuat di COLDCARD), pastikan sudah memiliki frasa mnemonik dan frasa tersebut berfungsi dengan baik (begitu juga dengan frasa sandi opsional, jika ada). Hal ini penting untuk menghindari kehilangan bitcoin Anda jika terjadi masalah selama pembaruan perangkat.

Pilih "*Upgrade Firmware*".

![CCQ](assets/fr/017.webp)

Pilih "*Tampilkan Versi*".

![CCQ](assets/fr/018.webp)

Kamu bisa memeriksa versi firmware COLDCARD milikmu saat ini. Sebagai contoh, dalam kasusku, versinya adalah "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Periksa [di situs web resmi COLDCARD] (https://coldcard.com/downloads) untuk mengetahui apakah versi yang lebih baru tersedia. Klik "*Unduh*" untuk mengunduh firmware baru.

![CCQ](assets/fr/020.webp)

Pada titik ini, kami sangat menyarankan untuk memeriksa integritas dan keaslian firmware yang diunduh. Untuk melakukan ini, unduh [dokumen yang berisi hash dari semua versi, yang ditandatangani oleh pengembang] (https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifikasi tanda tangan dengan [kunci publik pengembang] (https://keybase.io/dochex), dan pastikan bahwa hash yang ditunjukkan dalam dokumen yang ditandatangani sesuai dengan yang ada pada firmware yang diunduh dari situs. Jika semuanya sudah benar, kamu dapat melanjutkan pembaruan.

Kalau kamu tidak terbiasa dengan proses verifikasi ini, aku sarankan kamu untuk mengikuti tutorial ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Ambil kartu microSD dan transfer file firmware (dokumen dalam format `.dfu`) ke kartu tersebut. Masukkan kartu microSD ke salah satu port COLDCARD milikmu.

![CCQ](assets/fr/021.webp)

Kemudian, di menu pembaruan firmware, pilih "*Dari MicroSD*".

![CCQ](assets/fr/022.webp)

Pilih file yang sesuai dengan firmware.

![CCQ](assets/fr/023.webp)

Konfirmasikan pilihanmu dengan menekan tombol "*ENTER*".

![CCQ](assets/fr/024.webp)

Harap tunggu sementara firmware diperbarui.

![CCQ](assets/fr/025.webp)

Setelah pembaruan selesai, masukkan kode PIN untuk membuka kunci perangkat.

![CCQ](assets/fr/026.webp)

Firmware sekarang sudah diperbarui.

## Parameter COLDCARD Q

Kalau mau, kamu dapat menjelajahi pengaturan COLDCARD milikmu dengan mengakses menu "*Pengaturan*".

![CCQ](assets/fr/027.webp)

Dalam menu ini, kamu akan menemukan berbagai opsi penyesuaian, misalnya, mengatur kecerahan layar atau memilih satuan pengukuran default.

![CCQ](assets/fr/028.webp)

Kita akan mencermati pengaturan lanjutan lainnya dalam tutorial berikutnya:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## Membuat dompet Bitcoin

Sekarang saatnya membuat dompet Bitcoin baru! Untuk itu, kamu perlu membuat frasa mnemonik. Di COLDCARD, ada tiga cara yang bisa kamu pilih untuk membuat frasa ini:


- Gunakan generator angka acak internal (TRNG) saja;
- Gabungkan TRNG dengan lemparan dadu untuk menambah entropi;
- Gunakan lemparan dadu saja.

**Untuk pengguna pemula dan menengah, kami sarankan untuk hanya menggunakan generator nomor acak internal COLDCARD**

Aku tidak merekomendasikan opsi dadu saja, karena kalau eksekusinya buruk bisa menghasilkan entropi yang kurang, sehingga membahayakan keamanan dompet kamu.

Pilihan terbaik jelas yang kedua, yaitu menggabungkan TRNG dengan sumber entropi eksternal berupa lemparan dadu. Metode ini menjamin entropi minimum tetap sama dengan TRNG saja, sekaligus menambahkan lapisan keamanan ekstra kalau sampai generator internal gagal (baik disengaja maupun tidak). Dengan memilih opsi ini, kamu dapat keuntungan berupa kontrol lebih besar atas proses pembuatan seed, tanpa menambah risiko meskipun eksekusi dari sisi kamu kurang sempurna.

Klik "*New Seed Phrase*".

![CCQ](assets/fr/029.webp)

Kamu bisa memilih panjang frasa mnemonik kamu. Aku sarankan pilih 12 kata, karena tidak terlalu rumit untuk dikelola dan tetap menawarkan tingkat keamanan yang setara dengan frasa 24 kata.

![CCQ](assets/fr/030.webp)

COLDCARD kemudian akan menampilkan frasa pemulihan yang dihasilkan oleh TRNG kamu. Kalau kamu ingin menambahkan entropi eksternal tambahan, tekan tombol "*4*".

![CCQ](assets/fr/031.webp)

Ini akan membawa kamu ke halaman untuk menambahkan entropi lewat lemparan dadu. Lemparlah sebanyak mungkin (disarankan minimal 50 kali, meskipun kurang dari itu tetap aman karena kamu sudah mendapat entropi dari TRNG), lalu masukkan hasilnya dengan tombol "*1*" sampai "*6*". Setelah selesai, tekan "*ENTER*" untuk mengonfirmasi.

![CCQ](assets/fr/032.webp)

Frasa mnemonik baru akan ditampilkan, berdasarkan entropi yang baru saja Anda berikan dan TRNG.

**Peringatan: Mnemonik ini memberikan akses penuh dan tidak terbatas ke semua bitcoin milikmu**. Siapa pun yang punya frasa ini bisa mencuri dana kamu, bahkan tanpa akses fisik ke COLDCARD. Frasa 12 kata ini akan mengembalikan akses ke Bitcoin kamu kalau terjadi kehilangan, pencurian, atau kerusakan pada COLDCARD. Karena itu, sangat penting untuk menyimpannya dengan hati-hati di tempat yang aman.

Kamu bisa menuliskannya di kartu yang disertakan bersama COLDCARD, atau untuk keamanan ekstra, sebaiknya ukir di media baja tahan karat supaya tahan risiko kebakaran, banjir, atau keruntuhan. Bagaimanapun juga, jangan pernah menyimpannya di media digital, karena itu bisa bikin kamu kehilangan Bitcoin.

Tuliskan kata-kata yang muncul di layar ke media fisik pilihan kamu. Sesuai strategi keamanan kamu, boleh juga membuat beberapa salinan fisik lengkap dari frasa tersebut (yang penting jangan dipisah-pisahkan). Pastikan setiap kata diberi nomor dan tetap berurutan.

Tentu saja, **kamu tidak boleh membagikan kata-kata ini** di Internet, tidak seperti dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.

Setelah menuliskan kata-kata, tekan "*ENTER*".

![CCQ](assets/fr/033.webp)

Untuk memastikan kamu sudah menyimpan frasa dengan benar, sistem akan meminta kamu mengonfirmasi beberapa kata tertentu. Pilih nomor yang sesuai dengan setiap kata lewat papan tombol.

![CCQ](assets/fr/034.webp)

Dompet kamu sekarang sudah berhasil dibuat! Di sudut kanan atas layar, kamu bisa melihat fingerprint dari master private key kamu. Tekan "*ENTER*".

![CCQ](assets/fr/035.webp)

Sekarang kamu bisa mengakses menu utama COLDCARD milikmi.

![CCQ](assets/fr/036.webp)

## Menyiapkan portofolio baru di Sparrow

Ada beberapa opsi untuk membangun komunikasi antara perangkat lunak Sparrow Wallet dan COLDCARD milikmu. Yang paling mudah adalah menggunakan kabel USB-C. Namun, secara default, COLDCARD telah menonaktifkan komunikasi kabel dan NFC. Untuk mengaktifkannya kembali, buka "*Pengaturan*", lalu "*Hardware On/Off*", dan aktifkan opsi komunikasi yang diinginkan.

![CCQ](assets/fr/037.webp)

Kalau kamu lebih suka menjaga COLDCARD tetap benar-benar terisolasi dari komputer, kamu bisa memilih komunikasi air-gap tidak langsung, lewat kode QR atau kartu microSD. Metode inilah yang akan kita pakai di tutorial ini.

Buka "*Tingkat Lanjut/Alat*".

![CCQ](assets/fr/038.webp)

Pilih "*Dompet Ekspor*".

![CCQ](assets/fr/039.webp)

Kemudian pilih "*Dompet Sparrow*".

![CCQ](assets/fr/040.webp)

Tekan "*ENTER*" untuk menghasilkan file konfigurasi.

![CCQ](assets/fr/041.webp)

Kemudian, pilih cara mengirim file ini ke Sparrow. Dalam contoh ini, aku telah memasukkan microSD ke dalam slot "*A*", jadi aku akan memilih tombol "*1*". Kamu juga dapat menampilkan informasi sebagai kode QR pada layar COLDCARD dengan menekan tombol "*QR*", dan memindai kode QR ini dengan webcam komputer milikmu.

![CCQ](assets/fr/042.webp)

Luncurkan Sparrow Wallet dan lewati halaman perkenalan untuk mencapai layar utama. Pastikan kamu terhubung dengan benar ke sebuah node dengan memeriksa sakelar di kanan bawah layar.

![CCQ](assets/fr/043.webp)

Sebaiknya kamu pakai node Bitcoin milikmu sendiri. Di tutorial ini aku pakai node publik (kuning) karena masih di testnet, tapi kalau untuk penggunaan nyata/produksi, paling aman pakai Bitcoin Core lokal (hijau) atau server Electrum di node jarak jauh (biru).

Akses menu "*File*" dan pilih "*Dompet Baru*".

![CCQ](assets/fr/044.webp)

Beri nama dompetmu dan klik "*Buat Dompet*".

![CCQ](assets/fr/045.webp)

Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan mengamankan bitcoinmu.

![CCQ](assets/fr/046.webp)

Klik "*Dompet Perangkat Keras yang Terisi Penuh*".

![CCQ](assets/fr/047.webp)

Di bawah tab "*Coldcard*", klik "*Scan...*" jika Anda berencana untuk memindai kode QR yang ditampilkan di COLDCARD milikmu, atau "*Import File...*" untuk mengimpor file dari microSD (ini adalah file `.json`).

![CCQ](assets/fr/048.webp)

Setelah mengimpor, periksa apakah "*Sidik jari master*" yang ditampilkan di Sparrow cocok dengan yang ditampilkan di COLDCARD-mu. Konfirmasikan pembuatan dengan mengklik "*Terapkan*".

![CCQ](assets/fr/049.webp)

Siapkan kata sandi yang kuat untuk mengamankan akses ke Dompet Sparrow kamu. Kata sandi ini bakal melindungi kunci publik, alamat, tag, dan riwayat transaksi kamu dari akses yang nggak sah.

Sebaiknya simpan kata sandi ini biar nggak lupa (misalnya di pengelola kata sandi).

![CCQ](assets/fr/050.webp)

Dompet kamu sekarang sudah diatur di Sparrow Wallet.

![CCQ](assets/fr/051.webp)

Sebelum kamu menerima bitcoin pertama di dompet, **sangat disarankan untuk melakukan tes pemulihan kosong.** Catat beberapa informasi referensi, seperti xpub kamu, lalu reset COLDCARD Q saat dompet masih kosong. Setelah itu, coba pulihkan dompet ke COLDCARD menggunakan cadangan kertas kamu. Periksa apakah xpub yang dihasilkan setelah pemulihan sama dengan yang kamu catat sebelumnya. Kalau sama, berarti cadangan kertas kamu bisa diandalkan.

Untuk belajar lebih lanjut soal cara melakukan tes pemulihan, kamu bisa baca tutorial lain ini:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Menerima bitcoin

Untuk menerima bitcoin pertama, mulailah dengan mengaktifkan dan membuka kunci COLDCARD Anda.

![CCQ](assets/fr/052.webp)

Pada Sparrow Wallet, klik tab "*Receive*".

![CCQ](assets/fr/053.webp)

Sebelum kamu menggunakan alamat yang ditampilkan oleh Sparrow Wallet, pastikan untuk mengeceknya di layar COLDCARD. Langkah ini memastikan bahwa alamat di Sparrow tidak dimanipulasi, dan bahwa dompet hardware benar-benar menyimpan kunci pribadi yang dibutuhkan untuk membelanjakan bitcoin dari alamat tersebut. Dengan begitu, kamu bisa terhindar dari jenis serangan tertentu.

Untuk melakukan pemeriksaan ini, klik menu "*Address Explorer*" pada COLDCARD.

![CCQ](assets/fr/054.webp)

Pilih jenis skrip yang kamu gunakan pada Sparrow. Dalam skenarioku, ini adalah Segwit P2WPKH. aku klik di atasnya.

![CCQ](assets/fr/055.webp)

Setelah itu, kamu bisa melihat berbagai alamat turunanmu secara berurutan.

![CCQ](assets/fr/056.webp)

Periksa dengan Sparrow apakah alamatnya cocok. Dalam skenarioku, alamat dengan jalur turunan `m/84'/1'/0'/0/0` memang `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` pada Sparrow dan COLDCARD.

![CCQ](assets/fr/057.webp)

Cara lain untuk memverifikasi kepemilikan alamat ini adalah dengan memindai kode QR-nya langsung ke Sparrow dari COLDCARD-mu. Dari layar beranda COLDCARD-mu, pilih "*Pindai Kode QR Apa Saja*". Kamu juga dapat menggunakan tombol "*QR*" pada keyboard.

![CCQ](assets/fr/058.webp)

Pindai kode QR dari alamat yang ditampilkan di Sparrow Wallet.

![CCQ](assets/fr/059.webp)

Pastikan alamat yang ditampilkan di COLDCARD-mu sesuai dengan yang ditampilkan di Sparrow. Kemudian tekan tombol "*1*".

![CCQ](assets/fr/060.webp)

Dengan demikian, alamat tersebut berhasil dikonfirmasi.

![CCQ](assets/fr/061.webp)

Sekarang kamu bisa menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan alamat ini. Ini adalah praktik yang baik karena memudahkanmu dalam mengelola UTXO.

![CCQ](assets/fr/062.webp)

Untuk informasi lebih lanjut mengenai pelabelan, aku juga merekomendasikan tutorial lainnya ini:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kemudian kamu dapat menggunakan alamat ini untuk menerima bitcoin.

![CCQ](assets/fr/063.webp)

## Kirim bitcoin

Setelah kamu menerima sat pertama di dompet aman COLDCARD, kamu juga dapat membelanjakannya!

Seperti biasa, mulailah dengan mengaktifkan dan membuka kunci COLDCARD Q, lalu buka Sparrow Wallet dan buka tab "*Kirim*" untuk menyiapkan transaksi baru.

![CCQ](assets/fr/064.webp)

Jika kamu ingin melakukan "kontrol koin", yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin kamu belanjakan, lalu klik "*Kirim Terpilih*". Kamu akan diarahkan ke layar yang sama pada tab "*Kirim*", tetapi dengan UTXO yang sudah dipilih untuk transaksi.

![CCQ](assets/fr/065.webp)

Masukkan alamat tujuan. Kamu juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".

![CCQ](assets/fr/066.webp)

Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.

![CCQ](assets/fr/067.webp)

Pilih jumlah yang akan dikirim ke alamat ini.

![CCQ](assets/fr/068.webp)

Sesuaikan tarif biaya transaksimu sesuai dengan pasar saat ini.

![CCQ](assets/fr/069.webp)

Pastikan semua parameter transaksimu sudah benar, lalu klik "*Buat Transaksi*".

![CCQ](assets/fr/070.webp)

Jika semuanya sudah sesuai dengan keinginan kamu, klik "*Finalisasi Transaksi untuk Penandatanganan*".

![CCQ](assets/fr/071.webp)

Setelah kamu membuat transaksi di Sparrow, saatnya untuk menandatanganinya di COLDCARD Anda. Untuk mengirimkan PSBT (transaksi yang belum ditandatangani) ke perangkat, kamu memiliki beberapa opsi. Jika transmisi data kabel diaktifkan, kamu bisa mengirimkan transaksi secara langsung melalui koneksi USB-C, seperti yang kamu lakukan dengan dompet perangkat keras lainnya. Dalam hal ini, pada Sparrow, kamu harus mengklik tombol "*Sign*" di pojok kanan bawah. Dalam contoh skenarioku, tombol ini diblokir karena COLDCARD tidak terhubung dengan kabel.

![CCQ](assets/fr/072.webp)

Jika kamu lebih suka mempertahankan koneksi "celah udara" tanpa kontak langsung antara dompet perangkat keras dan komputermu, kamu memiliki 2 opsi. Yang pertama, dan yang lebih kompleks, adalah menggunakan kartu microSD. Masukkan kartu microSD ke dalam komputer, rekam transaksi melalui tombol "*Save Transaction*" pada Sparrow, kemudian transfer kartu ini ke port pada COLDCARD milikmu.

![CCQ](assets/fr/073.webp)

Kemudian akses menu "*Siap Menandatangani*".

![CCQ](assets/fr/074.webp)

Tinjau detail transaksi pada COLDCARD, termasuk alamat penerima, jumlah yang dikirim, dan biaya transaksi.

![CCQ](assets/fr/075.webp)

Jika semuanya sudah benar, tekan tombol "*ENTER*" untuk menandatangani transaksi.

![CCQ](assets/fr/076.webp)

Kemudian letakkan microSD kembali ke komputer kamu dan pada Sparrow, klik "*Muat Transaksi*" untuk memuat transaksi yang telah ditandatangani dari microSD. Kamu kemudian dapat melakukan pemeriksaan akhir sebelum mengunggahnya ke jaringan Bitcoin.

![CCQ](assets/fr/077.webp)

Metode kedua untuk menandatangani dengan COLDCARD di Air-Gap, yang jauh lebih sederhana daripada metode microSD, adalah dengan memindai PSBT secara langsung melalui kamera perangkat. Pada Sparrow, pilih "*Show QR*".

![CCQ](assets/fr/078.webp)

Pada COLDCARD, pilih "*Pindai Kode QR Apa Saja*". Kamu juga dapat menggunakan tombol "*QR*" pada keyboard.

![CCQ](assets/fr/079.webp)

Gunakan kamera COLDCARD untuk memindai kode QR yang ditampilkan pada Sparrow.

![CCQ](assets/fr/080.webp)

Rincian transaksi akan muncul lagi untuk verifikasi. Tekan "*ENTER*" untuk menandatangani jika semuanya sesuai dengan keinginanmu.

![CCQ](assets/fr/081.webp)

COLDCARD kamu kemudian akan menampilkan transaksi yang telah ditandatangani sebagai kode QR. Gunakan webcam komputermu untuk memindai kode QR ini dengan memilih "*Pindai QR*" pada Sparrow.

![CCQ](assets/fr/082.webp)

Transaksi yang Anda tandatangani sekarang sudah dapat dilihat di Sparrow. Periksa sekali lagi apakah semuanya sudah benar, lalu klik "*Broadcast Transaction*" untuk menyiarkannya ke jaringan Bitcoin.

![CCQ](assets/fr/083.webp)

Kamu bisa melacak transaksimu di tab "*Transaksi*" di Sparrow Wallet.

![CCQ](assets/fr/084.webp)

Selamat, kamu sekarang sudah menguasai penggunaan dasar COLDCARD Q dengan Sparrow Wallet!

Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu bersedia memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan tutorial ini di media sosial. Terima kasih banyak!

Aku juga menyarankanmu untuk membaca tutorial lainnya yang membahas opsi lanjutan COLDCARD Q :

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
