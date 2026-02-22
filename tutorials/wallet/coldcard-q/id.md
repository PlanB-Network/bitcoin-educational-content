---
name: COLDCARD Q
description: Menyiapkan dan menggunakan COLDCARD Q
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang didedikasikan untuk mengelola dan mengamankan private key dompet Bitcoin. Berbeda dengan dompet perangkat lunak atau hot wallet yang dipasang pada mesin umum dan sering terhubung ke Internet, dompet perangkat keras memungkinkan private key diisolasi secara fisik, sehingga mengurangi risiko pembajakan dan pencurian.

Tujuan utama dari dompet perangkat keras adalah mengurangi fungsionalitas perangkat semaksimal mungkin untuk meminimalkan permukaan serangan. Semakin sedikit permukaan serangan berarti semakin sedikit pula vektor serangan potensial, yaitu titik lemah dalam sistem yang bisa dieksploitasi penyerang untuk mendapatkan akses ke bitcoin.

Sangat disarankan untuk menggunakan dompet perangkat keras guna mengamankan bitcoin kamu, terutama jika kamu menyimpan dalam jumlah besar, baik secara nilai absolut maupun sebagai proporsi dari total aset kamu.

Dompet perangkat keras digunakan bersama dengan perangkat lunak manajemen dompet di komputer atau smartphone. Perangkat lunak tersebut menangani pembuatan transaksi, tetapi tanda tangan kriptografi yang diperlukan agar transaksi valid hanya dilakukan di dalam dompet perangkat keras. Ini berarti private key tidak pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras menawarkan perlindungan ganda bagi pengguna. Di satu sisi, dompet ini melindungi bitcoin kamu dari serangan jarak jauh dengan menjaga private key tetap offline. Di sisi lain, dompet ini umumnya menawarkan ketahanan fisik yang lebih tinggi terhadap upaya ekstraksi kunci. Berdasarkan dua kriteria keamanan inilah kita dapat menilai dan mengklasifikasikan berbagai model yang tersedia di pasaran.

Dalam tutorial ini, kita akan membahas salah satu solusi tersebut, yaitu **COLDCARD Q**.

---
Karena COLDCARD Q menawarkan begitu banyak fungsi, kita akan membagi penggunaannya ke dalam dua tutorial. Dalam tutorial pertama ini, kita akan membahas konfigurasi awal dan fungsi dasar perangkat. Kemudian, pada tutorial kedua, kita akan melihat cara memanfaatkan seluruh opsi lanjutan di COLDCARD kamu.

https://planb.academy/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## Memperkenalkan COLDCARD Q

COLDCARD Q adalah dompet perangkat keras khusus Bitcoin yang dikembangkan oleh perusahaan asal Kanada, Coinkite, yang juga dikenal lewat model MK sebelumnya. Q adalah produk mereka yang paling canggih hingga saat ini, dan diposisikan sebagai dompet perangkat keras Bitcoin terbaik.

Dari sisi perangkat keras, COLDCARD Q dilengkapi dengan semua fitur yang dibutuhkan untuk pengalaman pengguna yang optimal:

- Layar LCD besar yang memudahkan navigasi dan pengoperasian;
- Keyboard QWERTY lengkap;
- Kamera terintegrasi untuk memindai kode QR;
- Dua slot kartu microSD;
- Opsi daya yang sepenuhnya terisolasi melalui tiga baterai AAA (tidak termasuk), atau melalui kabel USB-C;
- Dua Secure Element dari dua produsen berbeda untuk keamanan tambahan;
- Kemampuan berkomunikasi melalui NFC.

Menurut pendapat kita, COLDCARD Q hanya memiliki dua kekurangan. Pertama, karena fiturnya yang sangat lengkap, ukurannya cukup besar, dengan panjang hampir 13 cm dan lebar 8 cm, kurang lebih seukuran smartphone kecil. Perangkat ini juga terasa cukup tebal karena adanya kompartemen baterai. Jika kamu mencari dompet perangkat keras yang lebih kecil dan mudah dibawa, MK4 yang jauh lebih ringkas bisa menjadi pilihan yang lebih cocok. Kekurangan kedua adalah harga perangkatnya, yang dibanderol **$239.99** di situs resmi, atau sekitar $72 lebih mahal dibandingkan MK4. Hal ini menempatkan COLDCARD Q dalam persaingan langsung dengan dompet perangkat keras premium lain seperti Ledger Flex atau Foundation Passport.


![CCQ](assets/fr/001.webp)

Dari sisi perangkat lunak, COLDCARD Q juga dibekali dengan sangat baik, seperti perangkat Coinkite lainnya, dengan berbagai fitur canggih:

- Dice Roll untuk menghasilkan seedphrase kamu sendiri;
- Kode PIN;
- Hitung mundur ke kunci PIN terakhir;
- Passphrase BIP39;
- PIN penguncian akhir;
- Hitung mundur koneksi;
- SeedXOR;
- BIP85.

Singkatnya, COLDCARD Q menawarkan pengalaman pengguna yang lebih baik dibandingkan MK4, dan kemungkinan sangat ideal bagi pengguna tingkat menengah hingga mahir yang menginginkan kemudahan penggunaan yang lebih tinggi.


COLDCARD Q tersedia untuk dijual [di situs web resmi Coinkite](https://store.coinkite.com/store/coldcard). Bisa juga dibeli dari pengecer.

## Mempersiapkan tutorial

Setelah kamu menerima COLDCARD miikmu, langkah pertama adalah memeriksa kemasannya untuk memastikan bahwa kemasan tersebut belum pernah dibuka. Jika kemasannya rusak, hal ini bisa mengindikasikan bahwa dompet perangkat keras tersebut telah disusupi dan mungkin tidak asli.

![CCQ](assets/fr/002.webp)

Saat kamu membuka kotaknya, kamu akan menemukan item berikut ini:


- COLDCARD Q di dalam kantong tertutup;
- Kartu untuk mencatat seedphrase kamu.

![CCQ](assets/fr/003.webp)

Pastikan kantong tersebut belum dibuka segelnya atau rusak. Periksa juga apakah nomor pada kantong kamu sesuai dengan nomor yang tertera pada kertas di dalam kantong. Simpan nomor ini untuk referensi di kemudian hari.

![CCQ](assets/fr/004.webp)

Jika kamu lebih suka memberi daya pada COLDCARD tanpa menghubungkannya ke komputer (air-gapped), masukkan tiga baterai AAA ke bagian belakang perangkat. Atau, kamu juga dapat menghubungkannya ke komputer melalui kabel USB-C.

![CCQ](assets/fr/005.webp)

Untuk tutorial ini, kamu juga membutuhkan Sparrow Wallet untuk mengelola dompet Bitcoin di komputer. Unduh [Sparrow Wallet](https://sparrowwallet.com/download/) dari situs web resminya. Aku sangat menyarankan kamu untuk memeriksa keasliannya (dengan GnuPG) dan integritasnya (melalui hash) sebelum melanjutkan instalasi. Jika kamu belum tahu cara melakukannya, ikuti tutorial ini:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Pemilihan kode PIN

Sekarang kamu dapat mengaktifkan COLDCARD Anda dengan menekan tombol di sudut kiri atas.

![CCQ](assets/fr/006.webp)

Tekan tombol "*ENTER*" untuk menerima persyaratan penggunaan.

![CCQ](assets/fr/007.webp)

COLDCARD Q kamu kemudian akan menampilkan sebuah nomor di bagian atas layar. Pastikan nomor ini sesuai dengan nomor yang tertera pada kantong tersegel dan pada potongan plastik di dalam kantong. Hal ini memastikan bahwa paket kamu belum dibuka sejak dikemas oleh Coinkite hingga saat kamu membukanya. Tekan "*ENTER*" untuk melanjutkan.

![CCQ](assets/fr/008.webp)

Masuk ke menu "*Pilih Kode PIN*" dan konfirmasikan dengan tombol "*ENTER*".

![CCQ](assets/fr/009.webp)

Kode PIN ini digunakan untuk membuka kunci COLDCARD kamu. Oleh karena itu, kode ini berfungsi sebagai perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam proses derivasi kunci kriptografi dompet kamu. Jadi, bahkan tanpa mengetahui kode PIN ini, selama kamu memiliki seedphrase kamu, kamu tetap dapat memulihkan akses ke bitcoin kamu.

Kode PIN COLDCARD dibagi menjadi dua bagian, yaitu awalan dan akhiran, yang masing-masing dapat terdiri dari 2 hingga 6 digit, dengan total panjang 4 hingga 12 digit. Saat membuka kunci COLDCARD, kamu harus terlebih dahulu memasukkan awalan, lalu perangkat akan menampilkan 2 kata. Setelah itu, masukkan akhiran. Dua kata ini akan diberikan kepadamu selama langkah konfigurasi ini dan harus disimpan dengan sangat hati-hati, karena kamu akan membutuhkannya setiap kali membuka kunci COLDCARD kamu. Jika dua kata yang ditampilkan saat membuka kunci sesuai dengan yang kamu simpan saat konfigurasi, ini menegaskan bahwa perangkat kamu belum pernah disusupi sejak terakhir kali digunakan.

Klik sekali lagi pada "*Pilih PIN*"

![CCQ](assets/fr/010.webp)

Konfirmasikan bahwa kamu telah membaca peringatan tersebut.

![CCQ](assets/fr/011.webp)

Sekarang kamu akan memilih kode PIN kamu. Kita merekomendasikan kode PIN yang panjang dan acak. Pastikan kamu menyimpan kode ini di lokasi yang terpisah dari tempat penyimpanan COLDCARD kamu. Kamu bisa menggunakan kartu yang disertakan dalam paket untuk mencatat kode ini.

Masukkan awalan pilihan kamu, lalu tekan tombol "*ENTER*" untuk mengonfirmasi bagian pertama dari kode PIN.

![CCQ](assets/fr/012.webp)

Dua kata anti-phishing kemudian akan ditampilkan di layar. Simpan dengan hati-hati untuk referensi di masa mendatang. Kamu dapat menggunakan kartu yang disertakan dalam paket untuk menuliskannya.

![CCQ](assets/fr/013.webp)

Kemudian masukkan bagian kedua dari kode PIN dan tekan "*ENTER*".

![CCQ](assets/fr/014.webp)

Konfirmasikan PIN kamu dengan memasukkannya untuk kedua kalinya, periksa apakah dua kata anti-phishing sesuai dengan yang kamu simpan sebelumnya.

![CCQ](assets/fr/015.webp)

Mulai sekarang, setiap kali kamu membuka kunci COLDCARD, ingatlah untuk memeriksa validitas dua kata anti-phishing yang muncul di layar setelah kamu memasukkan awalan kode PIN.

## Pembaruan firmware

Ketika menggunakan perangkat kamu untuk pertama kalinya, penting untuk memeriksa dan memperbarui firmware. Untuk melakukannya, akses menu "*Tingkat Lanjut/Alat*".

![CCQ](assets/fr/016.webp)

**Penting:** Jika kamu berencana untuk meng-upgrade firmware dan ini bukan pertama kalinya kamu menggunakan COLDCARD (misalnya, kamu sudah memiliki dompet yang dibuat di COLDCARD), pastikan kamu memiliki seedphrase kamu dan seedphrase tersebut berfungsi dengan baik, termasuk passphrase opsional jika digunakan. Hal ini sangat penting untuk menghindari kehilangan bitcoin kamu jika terjadi masalah selama proses pembaruan perangkat.

Pilih "*Upgrade Firmware*".

![CCQ](assets/fr/017.webp)

Pilih "*Tampilkan Versi*".

![CCQ](assets/fr/018.webp)

Kamu dapat memeriksa versi firmware COLDCARD saat ini. Sebagai contoh, dalam kasus ini, versinya adalah "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Periksa [di situs web resmi COLDCARD](https://coldcard.com/downloads) untuk mengetahui apakah versi yang lebih baru tersedia. Klik "*Unduh*" untuk mengunduh firmware baru.

![CCQ](assets/fr/020.webp)

Pada titik ini, kami sangat menyarankan untuk memeriksa integritas dan keaslian firmware yang diunduh. Untuk melakukan ini, unduh [dokumen yang berisi hash dari semua versi, yang ditandatangani oleh pengembang](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifikasi tanda tangan dengan [kunci publik pengembang](https://keybase.io/dochex), dan pastikan bahwa hash yang ditunjukkan dalam dokumen yang ditandatangani sesuai dengan yang ada pada firmware yang diunduh dari situs. Jika semuanya sudah benar, kamu dapat melanjutkan pembaruan.

Jika kamu tidak terbiasa dengan proses verifikasi ini, aku sarankan kamu mengikuti tutorial ini:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Ambil kartu microSD dan transfer file firmware (dokumen dalam format `.dfu`) ke kartu tersebut. Masukkan kartu microSD ke salah satu port COLDCARD milikmu.

![CCQ](assets/fr/021.webp)

Kemudian, di menu pembaruan firmware, pilih "*Dari MicroSD*".

![CCQ](assets/fr/022.webp)

Pilih file yang sesuai dengan firmware.

![CCQ](assets/fr/023.webp)

Konfirmasikan pilihan Anda dengan menekan tombol "*ENTER*".

![CCQ](assets/fr/024.webp)

Harap tunggu sementara firmware diperbarui.

![CCQ](assets/fr/025.webp)

Setelah pembaruan selesai, masukkan kode PIN kamu untuk membuka kunci perangkat.

![CCQ](assets/fr/026.webp)

Firmware milikmu sekarang sudah diperbarui.

## Parameter COLDCARD Q

Jika mau, kamu dapat menjelajahi pengaturan COLDCARD dengan mengakses menu "*Pengaturan*".

![CCQ](assets/fr/027.webp)

Dalam menu ini, kamu akan menemukan berbagai opsi penyesuaian, misalnya, mengatur kecerahan layar atau memilih satuan pengukuran default.

![CCQ](assets/fr/028.webp)

Kita akan mencermati pengaturan lanjutan lainnya dalam tutorial berikutnya:

https://planb.academy/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## Membuat dompet Bitcoin

Sekarang saatnya membuat dompet Bitcoin baru. Untuk melakukannya, kamu perlu membuat seedphrase. Di COLDCARD, ada tiga metode untuk menghasilkan seedphrase ini:

- Menggunakan generator angka acak internal saja (TRNG);
- Menggunakan kombinasi TRNG dan pelemparan dadu untuk menambahkan entropi;
- Menggunakan pelemparan dadu saja.

**Untuk pengguna pemula dan menengah, kita menyarankan untuk hanya menggunakan generator angka acak internal COLDCARD.**

Aku tidak merekomendasikan opsi pelemparan dadu saja, karena eksekusi yang kurang tepat dapat menghasilkan entropi yang tidak mencukupi, sehingga membahayakan keamanan dompet kamu.

Namun, pilihan terbaik tentu adalah opsi kedua, yang menggabungkan TRNG dengan sumber entropi eksternal. Metode ini menjamin tingkat entropi minimum yang setara dengan penggunaan TRNG saja, sekaligus menambahkan lapisan keamanan ekstra jika terjadi kegagalan pada generator internal, baik disengaja maupun tidak. Dengan memilih opsi ini, yang menggabungkan TRNG dan pelemparan dadu, kamu mendapatkan kontrol yang lebih besar atas proses pembuatan seedphrase tanpa menambah risiko jika terjadi kesalahan eksekusi di pihak kamu.


Klik "*Kata Benih Baru*".

![CCQ](assets/fr/029.webp)

Kamu bisa memilih panjang seedphrase kamu. Aku menyarankan untuk memilih seedphrase 12 kata, karena lebih mudah dikelola dan tetap menawarkan tingkat keamanan portofolio yang setara dengan seedphrase 24 kata.

![CCQ](assets/fr/030.webp)

COLDCARD kemudian akan menampilkan frasa pemulihan yang dihasilkan TRNG kamu. Jika kamu ingin menambahkan entropi eksternal tambahan, tekan tombol "*4*".

![CCQ](assets/fr/031.webp)

Ini akan membawa kamu ke halaman tempat kamu bisa menambahkan entropi dengan melempar dadu. Lakukan sebanyak mungkin lemparan (disarankan minimal 50 lemparan, tetapi kurang dari itu juga tidak masalah karena kamu sudah mendapat manfaat dari entropi TRNG), lalu catat hasilnya dengan menekan tombol "*1*" hingga "*6*". Setelah selesai, tekan "*ENTER*" untuk mengonfirmasi.

![CCQ](assets/fr/032.webp)

Seedphrase baru akan ditampilkan, berdasarkan entropi yang baru saja kamu berikan dan TRNG.

**Peringatan: Seedphrase ini memberikan akses penuh dan tidak terbatas ke seluruh bitcoin kamu**. Siapa pun yang memiliki seedphrase ini dapat mencuri dana kamu, bahkan tanpa akses fisik ke COLDCARD kamu. Seedphrase 12 kata ini memungkinkan kamu memulihkan akses ke bitcoin jika COLDCARD kamu hilang, dicuri, atau rusak. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di tempat yang aman.

Kamu bisa menuliskannya pada kartu yang disertakan bersama COLDCARD kamu. Untuk keamanan tambahan, aku menyarankan agar kamu mengukirnya pada media baja tahan karat guna melindunginya dari risiko kebakaran, banjir, atau keruntuhan. Apa pun metodenya, jangan pernah menyimpannya dalam bentuk digital, karena hal tersebut dapat menyebabkan kehilangan bitcoin kamu.

Tuliskan kata-kata yang ditampilkan di layar pada media fisik pilihan kamu. Tergantung pada strategi keamanan kamu, kamu bisa mempertimbangkan untuk membuat beberapa salinan fisik lengkap dari seedphrase tersebut, namun yang paling penting adalah jangan memisah-misahkannya. Pastikan setiap kata diberi nomor dan disimpan dalam urutan yang benar.

Tentu saja, **kamu tidak boleh membagikan kata-kata ini** di Internet, tidak seperti yang dilakukan dalam tutorial ini. Dompet contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.

Setelah selesai menuliskan semua kata, tekan "*ENTER*".


![CCQ](assets/fr/033.webp)

Untuk memastikan bahwa kamu telah menyimpan seedphrase dengan benar, sistem akan meminta kamu untuk mengonfirmasi kata-kata tertentu. Pilih nomor yang sesuai dengan setiap kata menggunakan papan tombol.

![CCQ](assets/fr/034.webp)

Dompet kamu sekarang sudah dibuat! Di sudut kanan atas layar, kamu dapat melihat sidik jari kunci pribadi utama Anda. Tekan "*ENTER*".

![CCQ](assets/fr/035.webp)

Sekarang kamu dapat mengakses menu utama COLDCARD kamu.

![CCQ](assets/fr/036.webp)

## Menyiapkan portofolio baru di Sparrow

Ada beberapa opsi untuk membangun komunikasi antara perangkat lunak Sparrow Wallet dan COLDCARD kamu. Cara paling mudah adalah menggunakan kabel USB-C. Namun, secara default, COLDCARD kamu menonaktifkan komunikasi melalui kabel dan NFC. Untuk mengaktifkannya kembali, buka menu "*Settings*", lalu "*Hardware On/Off*", dan aktifkan opsi komunikasi yang kamu inginkan.

![CCQ](assets/fr/037.webp)

Jika kamu lebih memilih untuk menjaga COLDCARD kamu benar-benar terisolasi dari komputer, kamu bisa menggunakan metode komunikasi air-gapped tidak langsung, yaitu melalui kode QR atau kartu microSD. Metode inilah yang akan kita gunakan dalam tutorial ini.

Buka "*Tingkat Lanjut/Alat*".

![CCQ](assets/fr/038.webp)

Pilih "*Dompet Ekspor*".

![CCQ](assets/fr/039.webp)

Kemudian pilih "*Dompet Sparrow*".

![CCQ](assets/fr/040.webp)

Tekan "*ENTER*" untuk menghasilkan file konfigurasi.

![CCQ](assets/fr/041.webp)

Kemudian, pilih cara untuk mengirim file ini ke Sparrow. Dalam contoh ini, aku memasukkan kartu microSD ke dalam slot "*A*", jadi aku akan memilih tombol "*1*". Kamu juga bisa menampilkan informasi tersebut sebagai kode QR di layar COLDCARD dengan menekan tombol "*QR*", lalu memindai kode QR ini menggunakan webcam komputer kamu.

![CCQ](assets/fr/042.webp)

Luncurkan Sparrow Wallet dan lewati halaman perkenalan untuk mencapai layar utama. Pastikan kamu terhubung dengan benar ke sebuah node dengan memeriksa sakelar di kanan bawah layar.

![CCQ](assets/fr/043.webp)

Sangat disarankan agar kamu menggunakan node Bitcoin kamu sendiri. Dalam tutorial ini, aku menggunakan node publik (kuning) karena memakai testnet, tetapi untuk penggunaan produksi, yang terbaik adalah menggunakan Bitcoin Core secara lokal (hijau) atau server Electrum pada node jarak jauh (biru).

Akses menu "*File*" dan pilih "*Dompet Baru*".

![CCQ](assets/fr/044.webp)

Beri nama dompet kamu dan klik "*Buat Dompet*".

![CCQ](assets/fr/045.webp)

Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan mengamankan bitcoin kamu.

![CCQ](assets/fr/046.webp)

Klik "*Dompet Perangkat Keras yang Terisi Penuh*".

![CCQ](assets/fr/047.webp)

Di bawah tab "*Coldcard*", klik "*Scan...*" jika kamu berencana untuk memindai kode QR yang ditampilkan di COLDCARD kamu, atau "*Import File...*" untuk mengimpor file dari microSD (ini adalah file `.json`).

![CCQ](assets/fr/048.webp)

Setelah mengimpor, periksa apakah "*Sidik jari master*" yang ditampilkan di Sparrow cocok dengan yang ditampilkan di COLDCARD kamu. Konfirmasikan pembuatan dengan mengklik "*Terapkan*".

![CCQ](assets/fr/049.webp)

Siapkan kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet kamu. Kata sandi ini akan melindungi kunci publik, alamat, tag, dan riwayat transaksi kamu dari akses yang tidak sah.

Sebaiknya simpan kata sandi ini agar kamu tidak lupa, misalnya menggunakan pengelola kata sandi.

![CCQ](assets/fr/050.webp)

Dompet kamu sekarang sudah diatur di Sparrow Wallet.

![CCQ](assets/fr/051.webp)

Sebelum kamu menerima bitcoin pertama di dompet kamu, **aku sangat menyarankan untuk melakukan tes pemulihan kosong**. Catat beberapa informasi referensi, seperti xpub kamu, lalu reset COLDCARD Q kamu saat dompet masih kosong. Setelah itu, coba pulihkan dompet kamu ke COLDCARD menggunakan cadangan kertas kamu. Periksa apakah xpub yang dihasilkan setelah pemulihan sama dengan yang kamu catat sebelumnya. Jika sesuai, kamu bisa yakin bahwa cadangan kertas kamu dapat diandalkan.

Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, aku menyarankan kamu membaca tutorial lain ini:

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Menerima bitcoin

Untuk menerima bitcoin pertama kamu, mulailah dengan mengaktifkan dan membuka kunci COLDCARD kamu.

![CCQ](assets/fr/052.webp)

Pada Sparrow Wallet, klik tab "*Receive*".

![CCQ](assets/fr/053.webp)

Sebelum menggunakan alamat yang diusulkan oleh Sparrow Wallet, periksa alamat tersebut langsung di layar COLDCARD kamu. Praktik ini memungkinkan kamu memastikan bahwa alamat yang ditampilkan di Sparrow tidak dimanipulasi, dan bahwa dompet perangkat keras memang menyimpan private key yang diperlukan untuk membelanjakan bitcoin yang diamankan oleh alamat tersebut. Hal ini membantu kamu menghindari beberapa jenis serangan.

Untuk melakukan pemeriksaan ini, buka menu "*Address Explorer*" di COLDCARD.

![CCQ](assets/fr/054.webp)

Pilih jenis skrip yang Anda gunakan pada Sparrow. Dalam kasus saya, ini adalah Segwit P2WPKH. Saya klik di atasnya.

![CCQ](assets/fr/055.webp)

Kemudian kamu dapat melihat berbagai alamat turunan kamu secara berurutan.

![CCQ](assets/fr/056.webp)

Periksa dengan Sparrow apakah alamatnya cocok. Dalam kasusku, alamat dengan jalur turunan `m/84'/1'/0'/0/0` memang `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` pada Sparrow dan COLDCARD.

![CCQ](assets/fr/057.webp)

Cara lain untuk memverifikasi kepemilikan alamat ini adalah dengan memindai kode QR-nya langsung ke Sparrow dari COLDCARD kamu. Dari layar beranda COLDCARD kamu, pilih "*Pindai Kode QR Apa Saja*". Kamu juga bisa menggunakan tombol "*QR*" pada keyboard.

![CCQ](assets/fr/058.webp)

Pindai kode QR dari alamat yang ditampilkan di Sparrow Wallet.

![CCQ](assets/fr/059.webp)

Pastikan alamat yang ditampilkan di COLDCARD kamu sesuai dengan yang ditampilkan di Sparrow. Kemudian tekan tombol "*1*".

![CCQ](assets/fr/060.webp)

Dengan demikian, alamat tersebut berhasil dikonfirmasi.

![CCQ](assets/fr/061.webp)

Sekarang kamu bisa menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan oleh alamat ini. Ini adalah praktik yang baik karena membantu kamu mengelola UTXO dengan lebih rapi.

![CCQ](assets/fr/062.webp)

Untuk informasi lebih lanjut mengenai pelabelan, aku juga merekomendasikan tutorial lainnya ini:

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kemudian kamu dapat menggunakan alamat ini untuk menerima bitcoin.

![CCQ](assets/fr/063.webp)

## Kirim bitcoin

Setelah kamu menerima sat pertama di dompet aman COLDCARD kamu, kamu juga sudah bisa membelanjakannya.

Seperti biasa, mulai dengan menyalakan dan membuka kunci COLDCARD Q kamu, lalu buka Sparrow Wallet dan masuk ke tab "*Kirim*" untuk menyiapkan transaksi baru.

![CCQ](assets/fr/064.webp)

Jika kamu ingin melakukan "coin control", yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin kamu belanjakan, lalu klik "*Kirim Terpilih*". Kamu akan diarahkan ke layar yang sama di tab "*Kirim*", tetapi dengan UTXO yang sudah dipilih untuk transaksi tersebut.

![CCQ](assets/fr/065.webp)

Masukkan alamat tujuan. Kamu juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".

![CCQ](assets/fr/066.webp)

Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.

![CCQ](assets/fr/067.webp)

Pilih jumlah yang akan dikirim ke alamat ini.

![CCQ](assets/fr/068.webp)

Sesuaikan tarif biaya transaksi kamu sesuai dengan pasar saat ini.

![CCQ](assets/fr/069.webp)

Pastikan semua parameter transaksi kamu sudah benar, lalu klik "*Buat Transaksi*".

![CCQ](assets/fr/070.webp)

Jika semuanya sudah sesuai dengan keinginan kamu, klik "*Finalisasi Transaksi untuk Penandatanganan*".

![CCQ](assets/fr/071.webp)

Setelah kamu membuat transaksi di Sparrow, saatnya menandatanganinya dengan COLDCARD kamu. Untuk mengirimkan PSBT (transaksi yang belum ditandatangani) ke perangkat kamu, ada beberapa opsi yang bisa digunakan. Jika transmisi data melalui kabel diaktifkan, kamu dapat mengirimkan transaksi secara langsung lewat koneksi USB-C, seperti pada dompet perangkat keras lainnya. Dalam hal ini, di Sparrow kamu perlu mengklik tombol "*Sign*" di pojok kanan bawah. Pada contoh ini, tombol tersebut diblokir karena COLDCARD tidak terhubung melalui kabel.

![CCQ](assets/fr/072.webp)

Jika kamu lebih suka mempertahankan koneksi **air-gapped** tanpa kontak langsung antara dompet perangkat keras dan komputer kamu, ada 2 opsi yang bisa digunakan. Opsi pertama, dan yang lebih kompleks, adalah menggunakan kartu microSD. Masukkan kartu microSD ke komputer kamu, simpan transaksi melalui tombol "*Save Transaction*" di Sparrow, lalu pindahkan kartu tersebut ke port microSD di COLDCARD kamu.

![CCQ](assets/fr/073.webp)

Kemudian akses menu "*Siap Menandatangani*".

![CCQ](assets/fr/074.webp)

Tinjau detail transaksi pada COLDCARD kamu, termasuk alamat penerima, jumlah yang dikirim, dan biaya transaksi.

![CCQ](assets/fr/075.webp)

Jika semuanya sudah benar, tekan tombol "*ENTER*" untuk menandatangani transaksi.

![CCQ](assets/fr/076.webp)

Kemudian letakkan microSD kembali ke komputer kamu dan pada Sparrow, klik "*Muat Transaksi*" untuk memuat transaksi yang telah ditandatangani dari microSD. Kemudian kamu dapat melakukan pemeriksaan akhir sebelum mengunggahnya ke jaringan Bitcoin.

![CCQ](assets/fr/077.webp)

Metode kedua untuk menandatangani transaksi dengan COLDCARD kamu dalam mode **air-gapped**, yang jauh lebih sederhana dibandingkan metode microSD, adalah dengan memindai PSBT secara langsung menggunakan kamera perangkat. Di Sparrow, pilih "*Show QR*".

![CCQ](assets/fr/078.webp)

Pada COLDCARD, pilih "*Pindai Kode QR Apa Saja*". Kamu juga dapat menggunakan tombol "*QR*" pada keyboard.

![CCQ](assets/fr/079.webp)

Gunakan kamera COLDCARD untuk memindai kode QR yang ditampilkan pada Sparrow.

![CCQ](assets/fr/080.webp)

Rincian transaksi akan muncul lagi untuk verifikasi. Tekan "*ENTER*" untuk menandatangani jika semuanya sesuai dengan keinginan kamu.

![CCQ](assets/fr/081.webp)

COLDCARD kamu kemudian akan menampilkan transaksi yang telah ditandatangani sebagai kode QR. Gunakan webcam komputer kamu untuk memindai kode QR ini dengan memilih "*Pindai QR*" pada Sparrow.

![CCQ](assets/fr/082.webp)

Transaksi yang kamu tandatangani sekarang sudah dapat dilihat di Sparrow. Periksa sekali lagi apakah semuanya sudah benar, lalu klik "*Broadcast Transaction*" untuk menyiarkannya ke jaringan Bitcoin.

![CCQ](assets/fr/083.webp)

Kamu dapat melacak transaksi milikmu di tab "*Transaksi*" di Sparrow Wallet.

![CCQ](assets/fr/084.webp)

Selamat, kamu sekarang sudah menguasai penggunaan dasar COLDCARD Q bersama Sparrow Wallet!

Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan tutorial ini di jejaring sosial kamu. Terima kasih banyak!

Aku juga menyarankan kamu untuk membaca tutorial lainnya yang membahas opsi lanjutan COLDCARD Q:

https://planb.academy/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
