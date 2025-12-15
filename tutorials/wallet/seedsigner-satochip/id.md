---
name: Satochip x SeedSigner
description: Bagaimana cara menggunakan Satochip dengan SeedSigner Anda?
---

![cover](assets/cover.webp)



*Terima kasih kepada [Crypto Guide] (https://www.youtube.com/@CryptoGuide/) untuk fork dari firmware SeedSigner untuk dukungan smartcard, yang akan kita gunakan dalam tutorial ini



---

Satochip adalah perangkat keras format kartu pintar wallet dengan elemen keamanan bersertifikasi EAL6+, salah satu standar keamanan tertinggi. Perangkat ini dirancang dan diproduksi oleh perusahaan Belgia dengan nama yang sama: Satochip.



Dengan harga sekitar €25, Satochip menonjol dari kompetisi karena nilai uang yang sangat baik. Berkat chipnya yang aman, ia menawarkan ketahanan terhadap serangan fisik. Terlebih lagi, kode sumber appletnya sepenuhnya merupakan sumber terbuka, dilisensikan di bawah *AGPLv3*.



Di sisi lain, formatnya memberikan batasan fungsional tertentu. Kelemahan utama dari Satochip adalah tidak adanya layar terintegrasi: oleh karena itu, pengguna harus menandatangani transaksi secara membabi buta, hanya mengandalkan tampilan komputer mereka.



Untuk mengatasi kelemahan ini, konfigurasi yang sangat menarik adalah menggunakannya bersama dengan SeedSigner. Dalam pengaturan ini, komunikasi tidak lagi terjadi secara langsung antara komputer dan Satochip, tetapi melalui pertukaran kode QR antara komputer dan SeedSigner. SeedSigner kemudian bertindak sebagai layar kepercayaan: menampilkan informasi yang akan ditandatangani, sementara tanda tangan itu sendiri dilakukan oleh Satochip. Tidak seperti penggunaan SeedSigner konvensional (atau bahkan digunakan bersama dengan Seedkeeper), seed tidak pernah dimasukkan ke dalam SeedSigner. Dengan demikian, SeedSigner menjadi layar Satochip, menghilangkan risiko yang terkait dengan penandatanganan buta.



Jika kita melihat masalahnya dari sisi lain, menggunakan SeedSigner dengan Satochip akan mengisi celah utama dalam SeedSigner: kemampuan untuk menyimpan dan menggunakan seed di dalam secure element.



Menurut pendapat saya, konfigurasi ini menawarkan beberapa keuntungan dibandingkan dompet perangkat keras konvensional:




- Satochip berharga sekitar €25, dan karena applet ini bersifat open-source, Anda bisa memasangnya sendiri pada smartcard kosong. Anda kemudian perlu menambahkan biaya komponen SeedSigner dan ekstensi untuk membaca smartcard: tergantung di mana Anda membeli perangkat keras ini, totalnya akan berkisar antara €70 hingga €100.
- Semua perangkat lunak yang terlibat dalam penyiapan adalah sumber terbuka: firmware SeedSigner dan applet Satochip.
- Anda mendapatkan keuntungan dari elemen keamanan bersertifikat.
- Konfigurasi dapat dilakukan sepenuhnya secara DIY, tanpa bantuan perangkat keras yang secara eksplisit ditujukan untuk penggunaan Bitcoin, yang dapat memberikan bentuk penyangkalan yang masuk akal dan resistensi terhadap ancaman eksternal tertentu (termasuk, tergantung pada negaranya, tekanan negara). Ini juga merupakan solusi yang menarik jika akses ke dompet perangkat keras komersial dibatasi atau tidak mungkin di wilayah Anda.




## 1. Bahan yang dibutuhkan



Untuk melaksanakan penyiapan ini, Anda memerlukan item berikut ini:




- Peralatan yang biasa dibutuhkan oleh SeedSigner klasik:
 - raspberry Pi Zero dengan pin GPIO,
 - 1.layar Waveshare 3",
 - kamera yang kompatibel,
 - kartu microSD.



![Image](assets/fr/01.webp)





- Kit ekstensi SeedSigner, tersedia [dari toko resmi Satochip](https://satochip.io/product/seedsigner-extension-kit/), yang memungkinkan Anda membaca dan menulis ke smartcard secara langsung dari SeedSigner Anda. Pilihan lainnya adalah dengan menggunakan [pembaca smartcard eksternal] (https://satochip.io/product/chip-card-reader/), yang dapat dihubungkan dengan kabel ke port Micro-USB pada Raspberry Pi. Namun, saya sendiri belum menguji solusi ini;
- [Satochip](https://satochip.io/product/satochip/), atau sebagai alternatif, [smartcard kosong](https://satochip.io/product/card-for-diy-project/) untuk menginstal applet Satochip (kit ekstensi yang dijual oleh Satochip sudah termasuk smartcard kosong). Kit ekstensi Satochip juga mendukung format [SIM JavaCard] (https://satochip.io/product/blank-sim-javacard-for-diy-project/). Jadi, Anda dapat memilih format ini jika Anda mau.



![Image](assets/fr/02.webp)



Untuk detail lebih lanjut tentang peralatan yang diperlukan untuk merakit SeedSigner, silakan merujuk ke Bagian 1 dari tutorial ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Instal firmware



Untuk menggunakan SeedSigner Anda dengan Satochip, Anda perlu menginstal firmware alternatif, yang berbeda dengan SeedSigner asli, untuk mendukung pembacaan kartu pintar. Untuk hal ini, [saya merekomendasikan penggunaan fork dari "**3rdIteration**"] (https://github.com/3rdIteration/seedsigner). Unduh [versi terbaru dari gambar] (https://github.com/3rdIteration/seedsigner/releases) (`.zip`) yang sesuai dengan model Raspberry Pi yang Anda gunakan.



![Image](assets/fr/03.webp)



Jika Anda belum memilikinya, unduh perangkat lunak [Balena Etcher] (https://etcher.balena.io/), kemudian lanjutkan sebagai berikut:




- Masukkan kartu microSD ke dalam komputer Anda;
- Meluncurkan Pengetsa ;
- Pilih file `.zip` yang baru saja Anda unduh;
- Pilih kartu microSD sebagai target;
- Klik `Flash!`.



![Image](assets/fr/04.webp)



Tunggu hingga proses selesai: microSD Anda sekarang siap digunakan. Sekarang Anda dapat melanjutkan untuk merakit perangkat Anda.



Untuk rincian lebih lanjut tentang instalasi firmware dan verifikasi perangkat lunak (langkah yang sangat saya sarankan untuk Anda lakukan), lihat tutorial berikut ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Merakit pembaca kartu pintar



Mulailah dengan memasang kamera pada Raspberry Pi Zero, dengan hati-hati memasukkannya ke pin kamera dan menguncinya dengan tab hitam. Kemudian letakkan Pi di bagian bawah casing, pastikan untuk menyelaraskan port dengan lubang yang sesuai.



![Image](assets/fr/05.webp)



Kemudian pasang pembaca kartu pintar ke pin GPIO Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Geser penutup plastik di atas pembaca kartu pintar hingga posisinya benar.



![Image](assets/fr/07.webp)



Kemudian tambahkan layar ke pin GPIO ekstensi.



![Image](assets/fr/08.webp)



Terakhir, masukkan kartu microSD yang berisi firmware ke dalam port samping pada Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Anda sekarang dapat menghubungkan SeedSigner Anda baik melalui port Micro-USB Raspberry Pi Zero, atau melalui port USB-C ekstensi. Kedua opsi tersebut berfungsi. Tunggu beberapa detik untuk memulai, maka Anda akan melihat layar selamat datang muncul.



![Image](assets/fr/10.webp)



Untuk detail lebih lanjut tentang pengaturan awal SeedSigner Anda, saya sarankan Anda membaca bagian 4 dari tutorial berikut ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Meng-flash kartu pintar dengan applet Satochip (opsional)



Jika Anda sudah memiliki Satochip, Anda bisa melewatkan langkah ini dan langsung ke langkah 4. Pada bagian ini, kita akan melihat cara memasang applet Satochip pada smartcard kosong (metode DIY). Applet hanyalah sebuah program kecil yang berjalan pada smartcard yang memungkinkan kita untuk mengelola fungsi-fungsi tertentu.



Untuk memulai, buka menu `Tools > Smartcard Tools` pada SeedSigner Anda.



![Image](assets/fr/11.webp)



Kemudian pilih `Tools DIY > Instal Applet`.



![Image](assets/fr/12.webp)



Masukkan kartu pintar Anda ke dalam pembaca SeedSigner, dengan chip menghadap ke bawah, dan pilih applet `Satochip`.



![Image](assets/fr/13.webp)



Harap bersabar selama instalasi: prosesnya mungkin memerlukan waktu beberapa puluh detik.



![Image](assets/fr/14.webp)



Setelah applet berhasil diinstal, Anda dapat melanjutkan ke langkah 4.



![Image](assets/fr/15.webp)




## 5. Membuat dan menyimpan seed



### 5.1. Menghasilkan seed



Sekarang setelah semua perangkat keras dan perangkat lunak Anda berfungsi dengan baik, Anda dapat melanjutkan untuk membuat portofolio Bitcoin Anda. Untuk melakukan ini, colokkan SeedSigner Anda, kemudian generate seed Anda seperti pada SeedSigner konvensional, baik dengan melempar dadu atau dengan mengambil foto:




- Buka menu `Tools > Camera / Dice Rolls`;
- Kemudian ikuti proses pembangkitan entropi menurut metode yang dipilih;
- Terakhir, cadangkan seed pada media fisik dan periksa cadangan dengan cermat.



![Image](assets/fr/16.webp)



Jika Anda ingin melihat rincian prosedur ini, silakan ikuti bagian 5 dari tutorial ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Menyimpan seed di Tempat Penyimpanan Benih



Setelah seed dibuat, ini adalah satu-satunya waktu di mana ia berada dalam RAM SeedSigner. Dalam kasus saya, saya ingin menyimpannya di [Seedkeeper] (https://satochip.io/product/seedkeeper/), sebuah produk Satochip lain yang didesain untuk menyimpan rahasia. Saya akan menggunakan perangkat ini sebagai pilihan terakhir, jika Satochip saya hilang.



Strategi pencadangan yang dipilih di sini tergantung pada preferensi Anda, tetapi sangat penting untuk memiliki setidaknya satu salinan frasa mnemonik Anda, baik di media fisik (kertas atau logam) atau, seperti di sini, di Seedkeeper. Anda juga dapat melipatgandakan jumlah cadangan sesuai kebutuhan. Untuk informasi lebih lanjut mengenai strategi pencadangan portofolio, saya sarankan Anda membaca tutorial ini:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Untuk mencadangkan seed Anda di Seedkeeper, langsung ke menu `Backup Seed`.



![Image](assets/fr/17.webp)



Kemudian masukkan Seedkeeper Anda ke dalam pembaca kartu pintar, dan pilih `Untuk SeedKeeper`.



![Image](assets/fr/18.webp)



Masukkan PIN Anda untuk membukanya.



![Image](assets/fr/19.webp)



Pilihlah `Label` untuk dengan mudah mengidentifikasi berbagai rahasia Anda yang tersimpan di Seedkeeper. Anda dapat, misalnya, menyimpan jejak wallet atau secara eksplisit menunjukkan `Benih`. Pilihannya tergantung pada preferensi dan risiko Anda.



![Image](assets/fr/20.webp)



Jika strategi pencadangan Anda hanya bergantung pada Seedkeeper ini, saya sangat menyarankan agar Anda menjalankan tes pemulihan kosong sekarang, kemudian membandingkan sidik jari untuk memeriksa apakah pencadangan berfungsi.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Kode PIN Seedkeeper harus sepanjang dan seacak mungkin, untuk mencegah upaya paksa jika terjadi gangguan fisik pada kartu. Anda juga harus menyimpan salinan cadangan dari kode PIN ini, yang disimpan di lokasi yang terpisah dari Seedkeeper. Tanpa PIN ini, Anda tidak akan bisa mengakses mnemonic yang tersimpan di Seedkeeper, dan bitcoin Anda akan hilang secara permanen.



### 5.3. Menyimpan seed pada Satochip



Sekarang portofolio Anda telah dibuat, disimpan, dan diverifikasi, kami akan mentransfernya ke Satochip. Untuk melakukan ini, pastikan seed dimuat ke dalam RAM SeedSigner. Kemudian masuk ke `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Masukkan Satochip Anda ke dalam pembaca kartu pintar, lalu pilih `Inisialisasi dengan Seed`.



![Image](assets/fr/22.webp)



Perangkat akan meminta Anda untuk memasukkan kode PIN Satochip; karena kartu masih baru dan belum diinisialisasi, maka belum ada PIN. Masukkan kode apa pun untuk melewati langkah ini (ini bukan langkah pemblokiran).



![Image](assets/fr/23.webp)



SeedSigner mendeteksi bahwa Satochip Anda belum diinisialisasi. Klik `Saya Mengerti` untuk mengonfirmasi.



![Image](assets/fr/24.webp)



Anda kemudian dapat mengatur kode PIN Satochip, dari 4 hingga 16 karakter. Untuk memperkuat keamanan wallet Anda, pilihlah kode acak yang panjang: ini adalah satu-satunya perlindungan terhadap akses fisik ke frasa mnemonik Anda.



Ingatlah untuk menyimpan PIN ini segera setelah dibuat, baik di pengelola kata sandi yang aman atau di media fisik, tergantung strategi pribadi Anda. Dalam kasus terakhir, pastikan untuk tidak menyimpan media yang berisi PIN di tempat yang sama dengan Satochip Anda, karena jika tidak, proteksi tidak akan berguna. Penting untuk memiliki salinan cadangan: **Tanpa PIN ini, Anda tidak akan bisa mengakses seed Anda, dan bitcoin Anda akan hilang selamanya**.



![Image](assets/fr/25.webp)



SeedSigner kemudian menanyakan seed mana yang akan diimpor ke dalam Satochip. Pilih salah satu yang sidik jarinya cocok dengan portofolio yang baru saja Anda buat.



![Image](assets/fr/26.webp)



seed Anda sekarang diimpor ke dalam Satochip.



![Image](assets/fr/27.webp)



Anda sekarang dapat mematikan SeedSigner Anda.



Jika Anda ingin menggunakan passphrase BIP39 untuk meningkatkan keamanan wallet Anda, silakan lihat bagian 6 dari tutorial ini:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Impor wallet ke Sparrow



Setelah portofolio Anda aktif dan berjalan, kami akan mengimpor informasi publiknya ("*keystore*") ke dalam Sparrow Wallet atau perangkat lunak manajemen portofolio lainnya. Perangkat lunak ini akan digunakan untuk membuat, mendistribusikan, dan melacak transaksi Anda. Akan tetapi, perangkat lunak ini tidak akan dapat menandatanganinya, karena hanya Satochip (dan semua cadangannya) yang memiliki private key yang diperlukan untuk operasi ini.



### 6.1 Mempersiapkan SeedSigner dan Satochip



Masukkan kartu microSD yang berisi sistem operasi, kemudian nyalakan SeedSigner Anda. Untuk saat ini, alat ini tidak dapat melakukan apa pun, karena belum mengenal seed Anda. Anda harus mulai dengan memasukkan Satochip ke dalam pembaca kartu pintar, karena kartu inilah yang menyimpan seed Anda.



Dari layar Utama, akses menu `Tools > Smartcard Tools > Satochip Functions (Alat-alat > Fungsi Satochip).



![Image](assets/fr/28.webp)



Kemudian klik `Export Xpub`.



![Image](assets/fr/29.webp)



Pilih jenis portofolio. Dalam kasus kami, ini adalah portofolio tunggal: pilih `Single Sig`.



![Image](assets/fr/30.webp)



Berikutnya adalah pilihan standar skrip. Pilih yang terbaru: `Native SegWit`.



![Image](assets/fr/31.webp)



Terakhir, pilih `Koordinator`, yaitu perangkat lunak manajemen portofolio yang ingin Anda gunakan. Di sini, kita akan menggunakan Sparrow Wallet.



![Image](assets/fr/32.webp)



Sebuah pesan peringatan akan muncul: ini adalah hal yang normal. Kunci publik yang diperluas (`xpub`) memungkinkan Anda untuk melihat semua alamat yang berasal dari seed Anda (pada akun pertama). Akan tetapi, kunci ini tidak memberikan akses ke dana Anda: pengungkapannya akan membahayakan privasi Anda, tetapi tidak membahayakan keamanan bitcoin Anda. Dengan kata lain, ini memungkinkan Anda untuk melihat saldo Anda, tetapi tidak untuk membelanjakannya.



Klik `Saya Mengerti`.



![Image](assets/fr/33.webp)



Kemudian masukkan kode PIN Satochip Anda untuk membukanya. Ini adalah kode yang Anda tentukan dan simpan di langkah 5.



![Image](assets/fr/34.webp)



Terakhir, klik `Export Xpub` jika Anda puas dengan informasi yang ditampilkan.



![Image](assets/fr/35.webp)



SeedSigner kemudian menghasilkan xpub Anda dalam bentuk kode QR dinamis, yang berisi semua data yang Anda perlukan untuk mengelola portofolio Anda di Sparrow Wallet. Anda dapat menyesuaikan kecerahan layar menggunakan joystick untuk mempermudah pemindaian kode QR.



### 6.2 Mengimpor portofolio baru ke dalam Sparrow Wallet



Pastikan perangkat lunak Sparrow Wallet sudah terinstal di komputer Anda. Jika Anda tidak tahu cara mengunduhnya, memeriksa keasliannya dan menginstalnya dengan benar, lihat tutorial lengkap kami tentang masalah ini:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Pada komputer Anda, buka Sparrow Wallet, kemudian pada bilah menu, klik `File → Import Wallet`.



![Image](assets/fr/36.webp)



Gulir ke bawah ke `SeedSigner`, lalu pilih `Scan...`. Webcam Anda akan diaktifkan: pindai kode QR dinamis yang ditampilkan pada layar SeedSigner Anda.



![Image](assets/fr/37.webp)



Tetapkan nama untuk portofolio Anda, lalu klik `Buat Wallet`. Sparrow kemudian akan meminta Anda untuk mengatur kata sandi untuk mengunci akses lokal ke wallet ini. Pilih kata sandi yang kuat: kata sandi ini akan melindungi data Anda di Sparrow (kunci publik, alamat, label, dan riwayat transaksi). Namun, kata sandi ini tidak diperlukan untuk memulihkan wallet di masa depan: hanya frasa mnemonic Anda (dan mungkin passphrase) yang diperlukan.



Saya sarankan Anda menyimpan kata sandi ini dalam pengelola kata sandi, untuk menghindari kehilangannya.



![Image](assets/fr/38.webp)



Keystore Anda telah berhasil diimpor.



![Image](assets/fr/39.webp)



Sekarang periksa apakah `sidik jari master` yang ditampilkan di Sparrow Wallet cocok dengan yang sebelumnya ditemukan di SeedSigner Anda.



SeedSigner kemudian akan meminta Anda untuk memindai alamat penerima secara acak dari Sparrow wallet Anda untuk mengonfirmasi keabsahan impor.



![Image](assets/fr/40.webp)



Satochip Anda (melalui SeedSigner) dan Sparrow Wallet sekarang terhubung dengan aman. Sparrow bertindak sebagai antarmuka manajemen yang lengkap, sementara Satochip tetap menjadi satu-satunya perangkat yang mampu menandatangani transaksi Anda. Anda sekarang siap untuk menerima dan mengirim bitcoin dalam konfigurasi yang benar-benar tanpa celah.



![Image](assets/fr/41.webp)



## 7. Menerima dan mengirim bitcoin



Satochip dan Sparrow Wallet Anda sekarang telah dikonfigurasikan untuk bekerja bersama. Pada bagian ini, kami akan menjelaskan langkah demi langkah cara menerima dan mengirim bitcoin dalam mode ini.



### 7.1 Menerima bitcoin



#### 7.1.1 Membuat alamat penerimaan



Pada komputer Anda, buka Sparrow Wallet dan buka kunci `Satochip-SeedSigner` wallet menggunakan kata sandi Anda. Pastikan perangkat lunak terhubung ke server (indikator di kanan bawah). Kemudian, pada bilah sisi, klik `Terima`.



![Image](assets/fr/42.webp)



Alamat Bitcoin yang baru muncul. Anda akan menemukan :




- Alamat dalam format teks (dimulai dengan `bc1q... ` jika Anda menggunakan P2WPKH, seperti dalam contoh ini) ;
- Kode QR terkait;
- Kolom `Label`, berguna untuk melacak transaksi Anda.



Saya sangat menyarankan agar Anda menambahkan label pada setiap tanda terima bitcoin di wallet Anda. Ini akan membantu Anda dengan mudah mengidentifikasi asal usul setiap UTXO dan mengelola privasi Anda dengan lebih baik. Untuk mengetahui lebih lanjut tentang subjek penting ini, lihat pelatihan khusus di Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Untuk menambahkan label, cukup masukkan nama di bidang `Label`, lalu konfirmasikan.



Sebagai contoh:



```txt
Label : Sale of the Raspberry Pi Zero
```



Alamat Anda sekarang dikaitkan dengan label ini di semua bagian Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 Verifikasi Address pada SeedSigner



Sebelum menyampaikan alamat penerima Anda kepada pembayar, penting untuk memeriksa bahwa alamat tersebut adalah milik seed Anda. Langkah ini memastikan bahwa Satochip Anda akan dapat menandatangani transaksi yang terkait dengan alamat ini. Langkah ini juga mencegah potensi serangan di mana Sparrow akan menampilkan alamat palsu. Ingatlah bahwa Sparrow berjalan pada lingkungan yang tidak aman (komputer Anda), yang permukaan serangannya jauh lebih besar dibandingkan dengan Satochip Anda, yang benar-benar terisolasi. Inilah sebabnya mengapa anda tidak boleh mempercayai alamat yang ditampilkan di Sparrow sebelum memeriksanya pada perangkat keras wallet anda.



Pada Sparrow, klik pada kode QR alamat untuk memperbesarnya: kode tersebut akan ditampilkan dalam layar penuh.



![Image](assets/fr/44.webp)



Pada SeedSigner Anda, masukkan Satochip ke dalam pembaca, lalu dari menu utama, pilih `Pindai`. Pindai kode QR yang ditampilkan di komputer Anda, lalu pilih `Use Satochip card`.



![Image](assets/fr/45.webp)



Kemudian konfirmasikan jenis skrip yang digunakan (dalam hal ini, `Native SegWit`), masukkan kode PIN Satochip untuk membukanya, dan validasi informasi `xpub`.



![Image](assets/fr/46.webp)



Jika alamat yang dipindai cocok dengan alamat yang berasal dari seed Anda, SeedSigner akan menampilkan pesan: `Address Terverifikasi`.



![Image](assets/fr/47.webp)



Dengan demikian, Anda bisa yakin bahwa alamat tersebut termasuk dalam portofolio Anda.



#### 7.1.3 Penerimaan dana



Anda sekarang dapat mengirimkan alamat ini dalam bentuk teks atau melalui kode QR kepada orang atau departemen yang perlu mengirimi Anda satss. Setelah transaksi disiarkan di jaringan, transaksi tersebut akan muncul di tab `Transactions` pada Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Kirim bitcoin



Mengirim bitcoin dengan konfigurasi Satochip-SeedSigner melibatkan 3 langkah:




- Pembuatan transaksi di Sparrow ;
- Menandatangani transaksi ini pada Satochip, melalui SeedSigner ;
- Terakhir, transaksi disiarkan melalui jaringan dari Sparrow.



Semua pertukaran antara kedua perangkat berlangsung secara eksklusif melalui kode QR.



#### 7.2.1 Membuat transaksi di Sparrow



Pada Sparrow Wallet, Anda dapat membuat transaksi dengan mengeklik tab `Kirim` pada bilah sisi kiri. Namun, saya lebih suka menggunakan tab `UTXOs`, yang memungkinkan Anda mempraktikkan *Coin Control*. Metode ini menawarkan kontrol yang tepat atas UTXO yang dibelanjakan, untuk membatasi informasi yang terungkap selama transaksi Anda.



Pada tab `UTXOs`, pilih koin yang ingin Anda belanjakan, lalu klik `Kirim Terpilih`.



![Image](assets/fr/49.webp)



Kemudian isi kolom transaksi:




- Di `Bayar ke`, tempelkan alamat penerima atau pindai kode QR mereka menggunakan ikon kamera ;
- Di `Label`, tambahkan label untuk melacak pengeluaran ini;
- Dalam `Jumlah`, masukkan jumlah yang akan dikirim;
- Terakhir, pilihlah kecepatan pengisian daya sesuai dengan kondisi jaringan saat ini (estimasi tersedia di [mempool.space](https://mempool.space/)).



Setelah Anda mengisi semua kolom, tinjau kembali informasi tersebut dengan cermat, lalu klik `Buat Transaksi >>`.



![Image](assets/fr/50.webp)



Periksa detail transaksi untuk terakhir kalinya untuk memastikan keakuratannya, lalu klik `Finalize Transaction for Signing`.



![Image](assets/fr/51.webp)



Transaksi sekarang sudah siap, namun belum ditandatangani. Untuk menampilkan [PSBT (*Partially Signed Bitcoin Transaction*)] (https://planb.academy/en/resources/glossary/psbt) sebagai kode QR, klik `Tampilkan QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Menandatangani transaksi dengan Satochip



Nyalakan SeedSigner Anda dan masukkan Satochip seperti biasa. Dari layar beranda, pilih `Pindai`, lalu pindai kode QR yang ditampilkan pada Sparrow.



![Image](assets/fr/53.webp)



Pilih opsi `Use Satochip card (Gunakan kartu Satochip).



![Image](assets/fr/54.webp)



Masukkan kode PIN Anda untuk membuka kunci kartu pintar.



![Image](assets/fr/55.webp)



SeedSigner mendeteksi bahwa ini adalah PSBT dan menampilkan ringkasan transaksi:




   - Jumlah yang dikirim,
   - Alamat tujuan,
   - Biaya transaksi terkait.



Klik `Tinjau Detail` dan periksa semua informasi secara langsung pada layar SeedSigner. Hal yang paling penting untuk diperiksa adalah jumlah yang dikirim, alamat tujuan dan biaya transaksi.



![Image](assets/fr/56.webp)



Jika semua sudah sesuai, pilih `Setujui PSBT` untuk menandatangani transaksi menggunakan Satochip.



![Image](assets/fr/57.webp)



Setelah tanda tangan selesai, SeedSigner menghasilkan kode QR baru yang berisi transaksi yang telah ditandatangani, yang siap untuk dipindai oleh Sparrow.



#### 7.2.3 Menyiarkan transaksi dari Sparrow



Setelah transaksi ditandatangani dan divalidasi, yang tersisa hanyalah menyiarkannya di jaringan Bitcoin sehingga penambang dapat memasukkannya ke dalam blok. Pada Sparrow, klik pada `Scan QR`.



![Image](assets/fr/58.webp)



Tunjukkan kode QR yang ditampilkan pada SeedSigner Anda (yang berisi transaksi yang ditandatangani) ke webcam. Sparrow kemudian akan menampilkan semua detail transaksi. Periksa apakah semua informasi sudah benar, lalu klik "Broadcast Transaction" untuk menyiarkannya di jaringan Bitcoin.



![Image](assets/fr/59.webp)



Transaksi Anda sekarang dikirim ke jaringan. Anda dapat mengikuti konfirmasinya di tab `Transaksi` pada Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Dapatkan kembali wallet Anda



Seperti yang telah kita lihat di bagian sebelumnya, tergantung pada strategi keamanan Anda, ada beberapa cara untuk mencadangkan frasa pemulihan selain Satochip Anda:




- Menggunakan *SeedQR* klasik dengan SeedSigner;
- Dengan merekam frasa mnemonik pada media fisik;
- Atau dengan menyimpannya di Seedkeeper, seperti yang dijelaskan di bagian 5.2.



Bagaimanapun, ada 2 situasi utama di mana Anda perlu melakukan intervensi: kehilangan Satochip atau kehilangan SeedSigner. Mari kita lihat bagaimana cara bereaksi pada masing-masing skenario ini.



### 8.1. Ambil wallet Anda dengan Satochip



Jika Anda masih memiliki Satochip Anda tetapi SeedSigner Anda rusak atau hilang, situasinya cukup mudah untuk dikelola, karena wallet Anda masih ada di dalam Satochip.



Pilihan terbaik adalah merekomendasikan komponen yang diperlukan dan membangun ulang SeedSigner baru dari awal. Karena ini adalah perangkat "tanpa kewarganegaraan", tidak masalah apakah Anda menggunakan SeedSigner yang sama atau yang lain: selama Anda dapat memasukkan Satochip Anda, semuanya akan bekerja secara normal.



Jika Anda tidak ingin membuat ulang, Anda juga dapat menggunakan Satochip Anda dengan cara klasik, yaitu langsung dari komputer, tanpa melalui SeedSigner. Metode ini bekerja dengan sempurna, tetapi sangat mengurangi keamanan Bitcoin wallet Anda: Anda kehilangan isolasi "*air-gapped*" dan sekarang harus menandatangani dalam keadaan buta, karena SeedSigner bertindak sebagai layar yang dipercaya. Akan tetapi, ini dapat menjadi solusi sementara dalam keadaan darurat, atau jika anda tidak dapat membuat ulang SeedSigner.



Untuk melakukan ini, Anda memerlukan kartu pintar USB atau pembaca NFC. Buka wallet yang ingin Anda pulihkan di Sparrow, lalu buka tab `Settings` dan klik `Replace`.



![Image](assets/fr/61.webp)



Masukkan Satochip Anda ke pembaca kartu pintar yang terhubung ke komputer, lalu klik `Import` di samping `Satochip`.



![Image](assets/fr/62.webp)



Terakhir, masukkan PIN smartcard Anda untuk membukanya. Anda kemudian dapat mengakses wallet Anda, membuat transaksi dan menandatanganinya secara langsung menggunakan Satochip yang terhubung.



### 8.2. Ambil portofolio Anda dengan SeedSigner



Skenario lain yang lebih rumit adalah ketika Anda kehilangan akses ke Satochip Anda yang berisi seed: entah karena rusak, hilang, dicuri, atau Anda lupa kode PIN-nya. Jika Satochip Anda dicuri atau hilang, kami sangat menyarankan agar, setelah akses ke dana Anda dipulihkan, Anda segera mentransfer bitcoin Anda ke wallet yang baru, yang dibuat dengan seed yang berbeda. Hal ini memastikan bahwa penyerang potensial tidak akan pernah bisa mendapatkan akses ke satss Anda.



Untuk mendapatkan kembali akses ke portofolio Anda dan memindahkan dana Anda, cukup masukkan seed Anda ke SeedSigner. Bergantung pada media cadangan yang Anda gunakan, Anda memiliki beberapa opsi:





- Masukkan frasa mnemonik Anda secara manual di menu `Seeds > Masukkan 12 kata seed`.



![Image](assets/fr/63.webp)





- Pindai *SeedQR* Anda dengan mengeklik tombol `Pindai` di halaman beranda.



![Image](assets/fr/64.webp)





- Atau muat seed Anda dari Seedkeeper, melalui menu `Seeds > From SeedKeeper` (ini adalah metode yang saya gunakan dalam tutorial ini). Anda hanya perlu memasukkan PIN Seedkeeper dan memilih rahasia yang akan digunakan sebagai seed pada SeedSigner.



![Image](assets/fr/65.webp)



Setelah seed dimuat ke dalam SeedSigner, metode apa pun yang Anda gunakan, Anda akan dapat menandatangani satu atau beberapa transaksi pemindaian untuk memindahkan bitcoin Anda ke wallet yang baru dan tanpa kompromi. Untuk mengetahui bagaimana cara melakukannya, lihat bagian 7.2 dari tutorial berikut ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Sekarang Anda sudah mengetahui cara menggunakan Satochip untuk mengelola portofolio Bitcoin Anda dengan aman dalam kombinasi dengan SeedSigner.



Jika pengaturan ini meyakinkan Anda, jangan ragu untuk mendukung proyek yang memungkinkannya:




- Dengan membeli peralatan Anda secara langsung [di situs web Satochip] (https://satochip.io/shop/);
- Dengan memberikan [donasi untuk proyek SeedSigner] (https://seedsigner.com/donate/);
- Dengan berlangganan [saluran YouTube Crypto Guide] (https://www.youtube.com/@CryptoGuide/), yang dijalankan oleh orang yang mengelola repositori GitHub yang menghosting firmware yang dimodifikasi yang kami gunakan dalam tutorial ini.