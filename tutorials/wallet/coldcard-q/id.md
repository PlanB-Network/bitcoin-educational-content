---
name: KARTU KOLEKSI Q
description: Menyiapkan dan menggunakan COLDCARD Q
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah sebuah perangkat elektronik yang didedikasikan untuk mengelola dan mengamankan kunci pribadi dompet Bitcoin. Tidak seperti dompet perangkat lunak (atau hot wallet) yang dipasang pada mesin-mesin umum yang sering kali terhubung ke Internet, dompet perangkat keras memungkinkan kunci pribadi diisolasi secara fisik, sehingga mengurangi risiko pembajakan dan pencurian.

Tujuan utama dari dompet perangkat keras adalah untuk mengurangi fungsionalitas perangkat sebanyak mungkin untuk meminimalisir permukaan serangan. Lebih sedikit permukaan serangan juga berarti lebih sedikit vektor serangan potensial, yaitu lebih sedikit titik lemah dalam sistem yang dapat dieksploitasi oleh penyerang untuk mendapatkan akses ke bitcoin.

Disarankan untuk menggunakan dompet perangkat keras untuk mengamankan bitcoin Anda, terutama jika Anda menyimpan dalam jumlah besar, baik dalam nilai absolut maupun proporsi dari total aset Anda.

Dompet perangkat keras digunakan bersama dengan perangkat lunak manajemen dompet pada komputer atau smartphone. Perangkat lunak yang terakhir mengelola pembuatan transaksi, tetapi tanda tangan kriptografi yang diperlukan untuk membuat transaksi ini valid hanya dilakukan di dalam dompet perangkat keras. Ini berarti bahwa private key tidak pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras menawarkan perlindungan ganda bagi pengguna: di satu sisi, dompet ini mengamankan bitcoin Anda dari serangan jarak jauh dengan menjaga kunci pribadi tetap offline, dan di sisi lain, dompet ini secara umum menawarkan ketahanan fisik yang lebih besar terhadap upaya untuk mengekstrak kunci. Dan berdasarkan 2 kriteria keamanan inilah kita dapat menilai dan mengklasifikasikan model-model yang berbeda di pasaran.

Dalam tutorial ini, saya ingin memperkenalkan kepada Anda, salah satu solusi tersebut: **COLDCARD Q**.

---
Karena COLDCARD Q menawarkan banyak sekali fungsi, saya mengusulkan untuk membagi penggunaannya ke dalam 2 tutorial. Dalam tutorial pertama ini, kita akan melihat konfigurasi awal dan fungsi dasar perangkat. Kemudian, dalam tutorial kedua, kita akan melihat cara memanfaatkan semua opsi lanjutan COLDCARD Anda.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
## Memperkenalkan COLDCARD Q

COLDCARD Q adalah dompet perangkat keras khusus Bitcoin yang dikembangkan oleh perusahaan Kanada, Coinkite, yang dikenal dengan model MK sebelumnya. Q merupakan produk mereka yang paling canggih hingga saat ini, dan diposisikan sebagai dompet perangkat keras Bitcoin terbaik.

Dari segi perangkat keras, COLDCARD Q dilengkapi dengan semua fitur yang diperlukan untuk pengalaman pengguna yang optimal:


- Layar LCD yang besar menyederhanakan navigasi dan pengoperasian;
- Keyboard QWERTY lengkap;
- Kamera terintegrasi untuk memindai kode QR;
- Dua slot kartu microSD ;
- Opsi daya yang sepenuhnya terisolasi melalui tiga baterai AAA (tidak termasuk), atau melalui kabel USB-C ;
- Dua Elemen Aman dari dua produsen berbeda untuk keamanan tambahan;
- Kemampuan untuk berkomunikasi melalui NFC.

Menurut pendapat saya, COLDCARD Q hanya memiliki dua kekurangan. Pertama, karena fiturnya yang banyak, ukurannya cukup besar, dengan panjang hampir 13 cm dan lebar 8 cm, hampir seukuran smartphone kecil. Kamera ini juga agak tebal karena ada tempat baterai. Jika Anda mencari dompet perangkat keras yang lebih kecil dan lebih mudah dibawa-bawa, MK4 yang jauh lebih ringkas mungkin merupakan pilihan yang lebih baik. Kekurangan kedua jelas adalah harga perangkat, yang dibanderol dengan harga **$239.99** di situs web resminya, yaitu $72 lebih mahal daripada MK4, yang menempatkan Q dalam persaingan langsung dengan dompet perangkat keras premium seperti Ledger Flex atau Foundation's Passport.

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

Singkatnya, COLDCARD Q menawarkan pengalaman pengguna yang lebih baik daripada MK4, dan mungkin ideal bagi pengguna tingkat menengah hingga mahir yang mencari kemudahan penggunaan yang lebih baik.

COLDCARD Q tersedia untuk dijual [di situs web resmi Coinkite] (https://store.coinkite.com/store/coldcard). Bisa juga dibeli dari pengecer.

## Mempersiapkan tutorial

Setelah Anda menerima COLDCARD Anda, langkah pertama adalah memeriksa kemasannya untuk memastikan bahwa kemasannya belum dibuka. Jika kemasannya rusak, ini bisa mengindikasikan bahwa dompet perangkat kerasnya telah disusupi dan mungkin tidak asli.

![CCQ](assets/fr/002.webp)

Apabila Anda membuka kotak, Anda akan menemukan item berikut ini:


- COLDCARD Q dalam kantong tertutup;
- Kartu untuk merekam frasa mnemonik Anda.

![CCQ](assets/fr/003.webp)

Pastikan tas belum dibuka segelnya atau rusak. Periksa juga apakah nomor pada tas Anda sesuai dengan nomor yang tertera pada kertas di dalam tas. Simpan nomor ini untuk referensi di masa mendatang.

![CCQ](assets/fr/004.webp)

Jika Anda lebih suka memberi daya pada COLDCARD tanpa menghubungkannya ke komputer (air-gap), masukkan tiga baterai AAA ke bagian belakang perangkat. Atau, Anda dapat menghubungkannya ke komputer melalui kabel USB-C.

![CCQ](assets/fr/005.webp)

Untuk tutorial ini, Anda juga membutuhkan Sparrow Wallet untuk mengelola dompet Bitcoin di komputer Anda. Unduh [Sparrow Wallet] (https://sparrowwallet.com/download/) dari situs web resminya. Saya sangat menyarankan Anda untuk memeriksa keasliannya (dengan GnuPG) dan integritasnya (melalui hash) sebelum melanjutkan instalasi. Jika Anda tidak tahu bagaimana cara melakukannya, ikuti tutorial ini:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
## Pemilihan kode PIN

Sekarang Anda dapat mengaktifkan COLDCARD Anda dengan menekan tombol di sudut kiri atas.

![CCQ](assets/fr/006.webp)

Tekan tombol "*ENTER*" untuk menerima persyaratan penggunaan.

![CCQ](assets/fr/007.webp)

COLDCARD Q Anda kemudian akan menampilkan nomor di bagian atas layar. Pastikan nomor ini sesuai dengan nomor yang tertera pada kantong yang disegel dan pada potongan plastik di dalam kantong. Hal ini memastikan bahwa paket Anda belum dibuka antara waktu pengemasan oleh Coinkite dan waktu Anda membukanya. Tekan "*ENTER*" untuk melanjutkan.

![CCQ](assets/fr/008.webp)

Masuk ke menu "*Pilih Kode PIN*" dan konfirmasikan dengan tombol "*ENTER*".

![CCQ](assets/fr/009.webp)

Kode PIN ini digunakan untuk membuka kunci COLDCARD Anda. Oleh karena itu, kode ini merupakan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam derivasi kunci kriptografi dompet Anda. Jadi, bahkan tanpa akses ke kode PIN ini, dengan memiliki frasa mnemonik Anda, Anda dapat memperoleh kembali akses ke bitcoin Anda.

Kode PIN COLDCARD dibagi menjadi dua bagian: awalan dan akhiran, yang masing-masing dapat terdiri dari 2 hingga 6 digit, dengan total 4 hingga 12 digit. Saat Anda membuka kunci COLDCARD, pertama-tama Anda harus memasukkan awalan, setelah itu perangkat akan menampilkan 2 kata. Kemudian masukkan akhiran. Dua kata ini akan diberikan kepada Anda selama langkah konfigurasi ini, dan harus disimpan dengan hati-hati, karena Anda akan membutuhkannya setiap kali Anda membuka kunci COLDCARD Anda. Jika dua kata yang ditampilkan saat membuka kunci sesuai dengan yang Anda simpan selama konfigurasi, ini akan mengonfirmasi bahwa perangkat Anda belum pernah disusupi sejak terakhir kali digunakan.

Klik sekali lagi pada "*Pilih PIN*"

![CCQ](assets/fr/010.webp)

Konfirmasikan bahwa Anda telah membaca peringatan tersebut.

![CCQ](assets/fr/011.webp)

Sekarang Anda akan memilih kode PIN Anda. Kami merekomendasikan kode PIN yang panjang dan acak. Pastikan Anda menyimpan kode ini di tempat yang berbeda dengan tempat penyimpanan COLDCARD Anda. Anda dapat menggunakan kartu yang disertakan dalam paket untuk mencatat kode ini.

Masukkan awalan pilihan Anda, lalu tekan tombol "*ENTER*" untuk mengonfirmasi bagian pertama kode PIN.

![CCQ](assets/fr/012.webp)

Dua kata anti-phishing kemudian akan ditampilkan di layar Anda. Simpan dengan hati-hati untuk referensi di masa mendatang. Anda dapat menggunakan kartu yang disertakan dalam paket untuk menuliskannya.

![CCQ](assets/fr/013.webp)

Kemudian masukkan bagian kedua dari kode PIN Anda dan tekan "*ENTER*".

![CCQ](assets/fr/014.webp)

Konfirmasikan PIN Anda dengan memasukkannya untuk kedua kalinya, periksa apakah dua kata anti-phishing sesuai dengan yang Anda simpan sebelumnya.

![CCQ](assets/fr/015.webp)

Mulai sekarang, setiap kali Anda membuka kunci COLDCARD, ingatlah untuk memeriksa validitas dua kata anti-phishing yang muncul di layar setelah Anda memasukkan awalan kode PIN.

## Pembaruan firmware

Ketika menggunakan perangkat Anda untuk pertama kalinya, penting untuk memeriksa dan memperbarui firmware. Untuk melakukannya, akses menu "*Tingkat Lanjut/Alat*".

![CCQ](assets/fr/016.webp)

**Penting:** Jika Anda berencana untuk meng-upgrade firmware Anda dan ini bukan pertama kalinya Anda menggunakan COLDCARD (misalnya, Anda sudah memiliki dompet yang dibuat di COLDCARD), pastikan Anda memiliki frasa mnemonik Anda dan frasa tersebut berfungsi dengan baik (begitu juga dengan frasa sandi opsional, jika ada). Hal ini penting untuk menghindari kehilangan bitcoin Anda jika terjadi masalah selama pembaruan perangkat.

Pilih "*Upgrade Firmware*".

![CCQ](assets/fr/017.webp)

Pilih "*Tampilkan Versi*".

![CCQ](assets/fr/018.webp)

Anda dapat memeriksa versi firmware COLDCARD Anda saat ini. Sebagai contoh, dalam kasus saya, versinya adalah "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Periksa [di situs web resmi COLDCARD] (https://coldcard.com/downloads) untuk mengetahui apakah versi yang lebih baru tersedia. Klik "*Unduh*" untuk mengunduh firmware baru.

![CCQ](assets/fr/020.webp)

Pada titik ini, kami sangat menyarankan untuk memeriksa integritas dan keaslian firmware yang diunduh. Untuk melakukan ini, unduh [dokumen yang berisi hash dari semua versi, yang ditandatangani oleh pengembang] (https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifikasi tanda tangan dengan [kunci publik pengembang] (https://keybase.io/dochex), dan pastikan bahwa hash yang ditunjukkan dalam dokumen yang ditandatangani sesuai dengan yang ada pada firmware yang diunduh dari situs. Jika semuanya sudah benar, Anda dapat melanjutkan pembaruan.

Jika Anda tidak terbiasa dengan proses verifikasi ini, saya sarankan Anda mengikuti tutorial ini:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Ambil kartu microSD dan transfer file firmware (dokumen dalam format `.dfu`) ke kartu tersebut. Masukkan kartu microSD ke salah satu port COLDCARD Anda.

![CCQ](assets/fr/021.webp)

Kemudian, di menu pembaruan firmware, pilih "*Dari MicroSD*".

![CCQ](assets/fr/022.webp)

Pilih file yang sesuai dengan firmware.

![CCQ](assets/fr/023.webp)

Konfirmasikan pilihan Anda dengan menekan tombol "*ENTER*".

![CCQ](assets/fr/024.webp)

Harap tunggu sementara firmware diperbarui.

![CCQ](assets/fr/025.webp)

Setelah pembaruan selesai, masukkan kode PIN Anda untuk membuka kunci perangkat.

![CCQ](assets/fr/026.webp)

Firmware Anda sekarang sudah diperbarui.

## Parameter COLDCARD Q

Jika mau, Anda dapat menjelajahi pengaturan COLDCARD Anda dengan mengakses menu "*Pengaturan*".

![CCQ](assets/fr/027.webp)

Dalam menu ini, Anda akan menemukan berbagai opsi penyesuaian, misalnya, mengatur kecerahan layar atau memilih satuan pengukuran default.

![CCQ](assets/fr/028.webp)

Kita akan mencermati pengaturan lanjutan lainnya dalam tutorial berikutnya:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
## Membuat dompet Bitcoin

Sekarang saatnya membuat dompet Bitcoin baru! Untuk melakukannya, Anda perlu membuat frasa mnemonik. Di Coldcard, Anda memiliki tiga metode untuk membuat frasa ini:


- Gunakan hanya generator nomor acak internal (TRNG);
- Gunakan kombinasi TRNG dan pelemparan dadu untuk menambahkan entropi;
- Gunakan dadu gulung saja.

**Untuk pengguna pemula dan menengah, kami sarankan untuk hanya menggunakan generator nomor acak internal COLDCARD**

Saya tidak merekomendasikan opsi dadu saja, karena eksekusi yang buruk dapat menyebabkan hukuman dengan entropi yang tidak mencukupi, sehingga membahayakan keamanan dompet Anda.

Namun, pilihan terbaik tentunya adalah yang kedua, yang menggabungkan penggunaan TRNG dengan sumber entropi eksternal. Metode ini menjamin entropi minimum yang setara dengan TRNG saja, dan menambahkan tingkat keamanan ekstra jika terjadi kegagalan generator internal (sukarela atau tidak). Dengan memilih opsi ini, yang menggabungkan TRNG dan pelemparan dadu, anda mendapatkan keuntungan dari kontrol yang lebih besar terhadap pembuatan hukuman, tanpa meningkatkan resiko jika terjadi eksekusi yang buruk di pihak anda.

Klik "*Kata Benih Baru*".

![CCQ](assets/fr/029.webp)

Anda bisa memilih panjang kalimat Anda. Saya sarankan Anda memilih kalimat 12 kata, karena tidak terlalu rumit untuk dikelola dan menawarkan keamanan portofolio yang tidak kalah dengan kalimat 24 kata.

![CCQ](assets/fr/030.webp)

COLDCARD kemudian akan menampilkan frasa pemulihan yang dihasilkan TRNG Anda. Jika Anda ingin menambahkan entropi eksternal tambahan, tekan tombol "*4*".

![CCQ](assets/fr/031.webp)

Ini akan membawa Anda ke halaman di mana Anda dapat menambahkan entropi dengan melempar dadu. Lakukan lemparan sebanyak mungkin (disarankan minimal 50 lemparan, tetapi kurang dari itu tidak masalah karena Anda sudah mendapatkan keuntungan dari entropi TRNG), dan catat hasilnya dengan tombol "*1*" hingga "*6*". Setelah selesai, tekan "*ENTER*" untuk mengonfirmasi.

![CCQ](assets/fr/032.webp)

Frasa mnemonik baru akan ditampilkan, berdasarkan entropi yang baru saja Anda berikan dan TRNG.

**Peringatan: Mnemonik ini memberikan akses penuh dan tidak terbatas ke semua bitcoin Anda**. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke COLDCARD Anda. Frasa 12 kata ini akan mengembalikan akses ke bitcoin Anda jika terjadi kehilangan, pencurian, atau kerusakan pada COLDCARD Anda. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di tempat yang aman.

Anda bisa menuliskannya di atas karton yang disertakan dengan COLDCARD Anda, atau untuk keamanan tambahan, saya sarankan Anda mengukirnya di atas penyangga baja tahan karat untuk melindunginya dari risiko kebakaran, banjir, atau keruntuhan. Bagaimanapun juga, jangan pernah menyimpannya di media digital, jika tidak, Anda bisa kehilangan bitcoin Anda.

Tuliskan kata-kata yang tersedia di layar pada media fisik pilihan Anda. Tergantung pada strategi keamanan Anda, Anda bisa mempertimbangkan untuk membuat beberapa salinan fisik lengkap dari kalimat tersebut (namun yang terpenting, jangan dipisah-pisahkan). Penting untuk menjaga agar kata-kata tersebut diberi nomor dan dalam urutan yang berurutan.

Tentu saja, **Anda tidak boleh membagikan kata-kata ini** di Internet, tidak seperti dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.

Setelah menuliskan kata-kata, tekan "*ENTER*".

![CCQ](assets/fr/033.webp)

Untuk memastikan bahwa Anda telah menyimpan frasa dengan benar, sistem akan meminta Anda untuk mengonfirmasi kata-kata tertentu. Pilih nomor yang sesuai dengan setiap kata pada papan tombol.

![CCQ](assets/fr/034.webp)

Dompet Anda sekarang sudah dibuat! Di sudut kanan atas layar, Anda dapat melihat sidik jari kunci pribadi utama Anda. Tekan "*ENTER*".

![CCQ](assets/fr/035.webp)

Sekarang Anda dapat mengakses menu utama COLDCARD Anda.

![CCQ](assets/fr/036.webp)

## Menyiapkan portofolio baru di Sparrow

Ada beberapa opsi untuk membangun komunikasi antara perangkat lunak Sparrow Wallet dan COLDCARD Anda. Yang paling mudah adalah menggunakan kabel USB-C. Namun, secara default, COLDCARD Anda telah menonaktifkan komunikasi kabel dan NFC. Untuk mengaktifkannya kembali, buka "*Pengaturan*", lalu "*Hardware On/Off*", dan aktifkan opsi komunikasi yang diinginkan.

![CCQ](assets/fr/037.webp)

Jika Anda lebih suka menjaga COLDCARD Anda benar-benar terisolasi dari komputer Anda, Anda dapat memilih komunikasi "celah udara" tidak langsung, menggunakan kode QR atau kartu microSD. Ini adalah metode yang akan kita gunakan dalam tutorial ini.

Buka "*Tingkat Lanjut/Alat*".

![CCQ](assets/fr/038.webp)

Pilih "*Dompet Ekspor*".

![CCQ](assets/fr/039.webp)

Kemudian pilih "*Dompet Sparrow*".

![CCQ](assets/fr/040.webp)

Tekan "*ENTER*" untuk menghasilkan file konfigurasi.

![CCQ](assets/fr/041.webp)

Kemudian, pilih cara mengirim file ini ke Sparrow. Dalam contoh ini, saya telah memasukkan microSD ke dalam slot "*A*", jadi saya akan memilih tombol "*1*". Anda juga dapat menampilkan informasi sebagai kode QR pada layar COLDCARD dengan menekan tombol "*QR*", dan memindai kode QR ini dengan webcam komputer Anda.

![CCQ](assets/fr/042.webp)

Luncurkan Sparrow Wallet dan lewati halaman perkenalan untuk mencapai layar utama. Pastikan Anda terhubung dengan benar ke sebuah node dengan memeriksa sakelar di kanan bawah layar.

![CCQ](assets/fr/043.webp)

Sangat disarankan agar Anda menggunakan node Bitcoin Anda sendiri. Untuk tutorial ini, saya menggunakan node publik (kuning), karena saya menggunakan testnet, tetapi untuk penggunaan produksi, yang terbaik adalah menggunakan Bitcoin Core secara lokal (hijau) atau server Electrum pada node jarak jauh (biru).

Akses menu "*File*" dan pilih "*Dompet Baru*".

![CCQ](assets/fr/044.webp)

Beri nama dompet Anda dan klik "*Buat Dompet*".

![CCQ](assets/fr/045.webp)

Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan mengamankan bitcoin Anda.

![CCQ](assets/fr/046.webp)

Klik "*Dompet Perangkat Keras yang Terisi Penuh*".

![CCQ](assets/fr/047.webp)

Di bawah tab "*Coldcard*", klik "*Scan...*" jika Anda berencana untuk memindai kode QR yang ditampilkan di COLDCARD Anda, atau "*Import File...*" untuk mengimpor file dari microSD (ini adalah file `.json`).

![CCQ](assets/fr/048.webp)

Setelah mengimpor, periksa apakah "*Sidik jari master*" yang ditampilkan di Sparrow cocok dengan yang ditampilkan di COLDCARD Anda. Konfirmasikan pembuatan dengan mengklik "*Terapkan*".

![CCQ](assets/fr/049.webp)

Siapkan kata sandi yang kuat untuk mengamankan akses ke Dompet Sparrow Anda. Kata sandi ini akan melindungi kunci publik, alamat, tag, dan riwayat transaksi Anda dari akses yang tidak sah.

Sebaiknya simpan kata sandi ini agar Anda tidak lupa (misalnya di pengelola kata sandi).

![CCQ](assets/fr/050.webp)

Dompet Anda sekarang sudah diatur di Sparrow Wallet.

![CCQ](assets/fr/051.webp)

Sebelum Anda menerima bitcoin pertama Anda di dompet, **Saya sangat menyarankan Anda untuk melakukan tes pemulihan kosong**. Tuliskan beberapa informasi referensi, seperti xpub Anda, kemudian setel ulang COLDCARD Q Anda ketika dompet masih kosong. Kemudian coba pulihkan dompet Anda ke COLDCARD menggunakan cadangan kertas Anda. Periksa apakah xpub yang dihasilkan setelah pemulihan sesuai dengan yang Anda tulis sebelumnya. Jika sesuai, Anda bisa yakin bahwa cadangan kertas Anda dapat diandalkan.

Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, saya sarankan Anda membaca tutorial lain ini:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Menerima bitcoin

Untuk menerima bitcoin pertama Anda, mulailah dengan mengaktifkan dan membuka kunci COLDCARD Anda.

![CCQ](assets/fr/052.webp)

Pada Sparrow Wallet, klik tab "*Receive*".

![CCQ](assets/fr/053.webp)

Sebelum menggunakan alamat yang diusulkan oleh Sparrow Wallet, periksa di layar COLDCARD Anda. Praktik ini memungkinkan Anda untuk mengonfirmasi bahwa alamat yang ditampilkan di Sparrow tidak curang, dan bahwa dompet perangkat keras memang menyimpan kunci pribadi yang diperlukan untuk membelanjakan bitcoin yang diamankan dengan alamat ini. Hal ini membantu Anda untuk menghindari beberapa jenis serangan.

Untuk melakukan pemeriksaan ini, klik menu "*Address Explorer*" pada COLDCARD.

![CCQ](assets/fr/054.webp)

Pilih jenis skrip yang Anda gunakan pada Sparrow. Dalam kasus saya, ini adalah Segwit P2WPKH. Saya klik di atasnya.

![CCQ](assets/fr/055.webp)

Anda kemudian dapat melihat berbagai alamat turunan Anda secara berurutan.

![CCQ](assets/fr/056.webp)

Periksa dengan Sparrow apakah alamatnya cocok. Dalam kasus saya, alamat dengan jalur turunan `m/84'/1'/0'/0/0` memang `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` pada Sparrow dan COLDCARD.

![CCQ](assets/fr/057.webp)

Cara lain untuk memverifikasi kepemilikan alamat ini adalah dengan memindai kode QR-nya langsung ke Sparrow dari COLDCARD Anda. Dari layar beranda COLDCARD Anda, pilih "*Pindai Kode QR Apa Saja*". Anda juga dapat menggunakan tombol "*QR*" pada keyboard.

![CCQ](assets/fr/058.webp)

Pindai kode QR dari alamat yang ditampilkan di Sparrow Wallet.

![CCQ](assets/fr/059.webp)

Pastikan alamat yang ditampilkan di COLDCARD Anda sesuai dengan yang ditampilkan di Sparrow. Kemudian tekan tombol "*1*".

![CCQ](assets/fr/060.webp)

Dengan demikian, alamat tersebut berhasil dikonfirmasi.

![CCQ](assets/fr/061.webp)

Sekarang Anda dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan alamat ini. Ini merupakan praktik yang baik yang memungkinkan Anda untuk mengelola UTXO dengan lebih baik.

![CCQ](assets/fr/062.webp)

Untuk informasi lebih lanjut mengenai pelabelan, saya juga merekomendasikan tutorial lainnya ini:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
Anda kemudian dapat menggunakan alamat ini untuk menerima bitcoin.

![CCQ](assets/fr/063.webp)

## Kirim bitcoin

Setelah Anda menerima sat pertama Anda di dompet aman COLDCARD, Anda juga dapat membelanjakannya!

Seperti biasa, mulailah dengan mengaktifkan dan membuka kunci COLDCARD Q Anda, lalu buka Sparrow Wallet dan buka tab "*Kirim*" untuk menyiapkan transaksi baru.

![CCQ](assets/fr/064.webp)

Jika Anda ingin melakukan "kontrol koin", yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin Anda belanjakan, lalu klik "*Kirim Terpilih*". Anda akan diarahkan ke layar yang sama pada tab "*Kirim*", tetapi dengan UTXO yang sudah dipilih untuk transaksi.

![CCQ](assets/fr/065.webp)

Masukkan alamat tujuan. Anda juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".

![CCQ](assets/fr/066.webp)

Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.

![CCQ](assets/fr/067.webp)

Pilih jumlah yang akan dikirim ke alamat ini.

![CCQ](assets/fr/068.webp)

Sesuaikan tarif biaya transaksi Anda sesuai dengan pasar saat ini.

![CCQ](assets/fr/069.webp)

Pastikan semua parameter transaksi Anda sudah benar, lalu klik "*Buat Transaksi*".

![CCQ](assets/fr/070.webp)

Jika semuanya sudah sesuai dengan keinginan Anda, klik "*Finalisasi Transaksi untuk Penandatanganan*".

![CCQ](assets/fr/071.webp)

Setelah Anda membuat transaksi di Sparrow, saatnya untuk menandatanganinya dengan COLDCARD Anda. Untuk mengirimkan PSBT (transaksi yang belum ditandatangani) ke perangkat Anda, Anda memiliki beberapa opsi. Jika transmisi data kabel diaktifkan, Anda bisa mengirimkan transaksi secara langsung melalui koneksi USB-C, seperti yang Anda lakukan dengan dompet perangkat keras lainnya. Dalam hal ini, pada Sparrow, Anda harus mengklik tombol "*Sign*" di pojok kanan bawah. Dalam contoh saya, tombol ini diblokir karena COLDCARD tidak terhubung dengan kabel.

![CCQ](assets/fr/072.webp)

Jika Anda lebih suka mempertahankan koneksi "celah udara" tanpa kontak langsung antara dompet perangkat keras dan komputer Anda, Anda memiliki 2 opsi. Yang pertama, dan yang lebih kompleks, adalah menggunakan kartu microSD. Masukkan kartu microSD ke dalam komputer Anda, rekam transaksi melalui tombol "*Save Transaction*" pada Sparrow, kemudian transfer kartu ini ke port pada COLDCARD Anda.

![CCQ](assets/fr/073.webp)

Kemudian akses menu "*Siap Menandatangani*".

![CCQ](assets/fr/074.webp)

Tinjau detail transaksi pada COLDCARD Anda, termasuk alamat penerima, jumlah yang dikirim, dan biaya transaksi.

![CCQ](assets/fr/075.webp)

Jika semuanya sudah benar, tekan tombol "*ENTER*" untuk menandatangani transaksi.

![CCQ](assets/fr/076.webp)

Kemudian letakkan microSD kembali ke komputer Anda dan pada Sparrow, klik "*Muat Transaksi*" untuk memuat transaksi yang telah ditandatangani dari microSD. Anda kemudian dapat melakukan pemeriksaan akhir sebelum mengunggahnya ke jaringan Bitcoin.

![CCQ](assets/fr/077.webp)

Metode kedua untuk menandatangani dengan COLDCARD Anda di Air-Gap, yang jauh lebih sederhana daripada metode microSD, adalah dengan memindai PSBT secara langsung melalui kamera perangkat. Pada Sparrow, pilih "*Show QR*".

![CCQ](assets/fr/078.webp)

Pada COLDCARD, pilih "*Pindai Kode QR Apa Saja*". Anda juga dapat menggunakan tombol "*QR*" pada keyboard.

![CCQ](assets/fr/079.webp)

Gunakan kamera COLDCARD untuk memindai kode QR yang ditampilkan pada Sparrow.

![CCQ](assets/fr/080.webp)

Rincian transaksi akan muncul lagi untuk verifikasi. Tekan "*ENTER*" untuk menandatangani jika semuanya sesuai dengan keinginan Anda.

![CCQ](assets/fr/081.webp)

COLDCARD Anda kemudian akan menampilkan transaksi yang telah ditandatangani sebagai kode QR. Gunakan webcam komputer Anda untuk memindai kode QR ini dengan memilih "*Pindai QR*" pada Sparrow.

![CCQ](assets/fr/082.webp)

Transaksi yang Anda tandatangani sekarang sudah dapat dilihat di Sparrow. Periksa sekali lagi apakah semuanya sudah benar, lalu klik "*Broadcast Transaction*" untuk menyiarkannya ke jaringan Bitcoin.

![CCQ](assets/fr/083.webp)

Anda dapat melacak transaksi Anda di tab "*Transaksi*" di Sparrow Wallet.

![CCQ](assets/fr/084.webp)

Selamat, Anda sekarang sudah menguasai penggunaan dasar COLDCARD Q dengan Sparrow Wallet!

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial Anda. Terima kasih banyak!

Saya juga menyarankan Anda untuk membaca tutorial lainnya yang membahas opsi lanjutan COLDCARD Q :

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0