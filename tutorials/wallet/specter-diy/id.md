---
name: Specter DIY
description: Panduan penyiapan untuk Specter DIY
---

![cover](assets/cover.webp)


## Spectre-DIY


> Cypherpunks menulis kode. Kita tahu bahwa seseorang harus menulis perangkat lunak untuk mempertahankan privasi, dan karena kita tidak bisa mendapatkan privasi kecuali kita semua melakukannya, kita akan menulisnya.

*Manifesto Cypherpunk - Eric Hughes - 9 Maret 1993*


Ide dari proyek ini adalah membangun perangkat keras wallet dari komponen yang sudah jadi.

Meskipun kami memiliki papan ekstensi yang menempatkan segala sesuatu dalam faktor bentuk yang bagus dan membantu Anda menghindari penyolderan apa pun, kami akan terus mendukung dan mempertahankan kompatibilitas dengan komponen standar.


![image](assets/fr/01.webp)


Kami juga ingin membuat proyek ini tetap fleksibel sehingga dapat bekerja pada rangkaian komponen lain dengan sedikit perubahan. Mungkin Anda ingin membuat perangkat keras wallet dengan arsitektur yang berbeda (RISC-V?), dengan modem audio sebagai saluran komunikasi - Anda seharusnya dapat melakukannya. Seharusnya mudah untuk menambah atau mengubah fungsionalitas Specter dan kami mencoba mengabstraksikan modul logika sebanyak mungkin.


Kode QR adalah cara default bagi Specter untuk berkomunikasi dengan host. Kode QR cukup nyaman dan memungkinkan pengguna untuk mengendalikan transmisi data - setiap kode QR memiliki kapasitas yang sangat terbatas dan komunikasi terjadi secara searah. Dan ini bersifat airgap - Anda tidak perlu menghubungkan wallet ke komputer setiap saat.


Untuk penyimpanan rahasia, kami mendukung mode agnostik (wallet melupakan semua rahasia saat dimatikan), mode sembrono (menyimpan rahasia dalam flash mikrokontroler aplikasi) dan integrasi secure element akan segera hadir.


Fokus utama kami adalah pengaturan multisignature dengan dompet perangkat keras lainnya, tetapi wallet juga dapat berfungsi sebagai penandatangan tunggal. Kami mencoba untuk membuatnya kompatibel dengan Bitcoin Core jika kami bisa - PSBT untuk transaksi yang tidak ditandatangani, deskriptor wallet untuk mengimpor/mengekspor dompet multisig. Untuk berkomunikasi dengan Bitcoin Core dengan lebih mudah, kami juga sedang mengerjakan [aplikasi Specter Desktop] (https://github.com/cryptoadvance/specter-desktop) - sebuah server flask python kecil yang berbicara dengan node Bitcoin Core Anda.


Sebagian besar firmware ditulis dalam MicroPython yang membuat kode mudah untuk diaudit dan diubah. Kami menggunakan pustaka [secp256k1] (https://github.com/bitcoin-core/secp256k1) dari Bitcoin Core untuk perhitungan kurva elips dan pustaka [LittlevGL] (https://lvgl.io/) untuk GUI.


## Penafian


Proyek ini telah matang secara signifikan, hingga tingkat keamanan Specter-DIY sekarang sebanding dengan dompet perangkat keras komersial di pasaran. Kami menerapkan bootloader aman yang memverifikasi peningkatan firmware, sehingga Anda dapat yakin bahwa hanya firmware yang telah ditandatangani yang dapat diunggah ke perangkat setelah penyiapan awal. Namun, tidak seperti perangkat penandatanganan komersial, bootloader harus diinstal secara manual oleh pengguna dan tidak diatur di pabrik vendor perangkat. Oleh karena itu, berikan perhatian ekstra selama instalasi firmware awal dan pastikan Anda memverifikasi tanda tangan PGP dan mem-flash firmware dari komputer yang aman.


Jika ada sesuatu yang tidak berhasil, buka masalah di sini atau ajukan pertanyaan di [grup Telegram] kami (https://t.me/+VEinVSYkW5TUl5Ai).


## Daftar belanja untuk Specter-DIY


Di sini kami menjelaskan apa yang harus dibeli, dan di bagian perakitan berikutnya kami menjelaskan cara menyusunnya dan beberapa catatan tentang papan - jumper daya, port USB, dll.


### Papan penemuan


Bagian utama perangkat ini adalah papan pengembang:



- Papan pengembang STM32F469I-DISCO (yaitu dari [Mouser] (https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) atau [Digikey] (https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Kabel Mini**USB
- Kabel MicroUSB standar untuk berkomunikasi melalui USB


Opsional, tetapi direkomendasikan:


- [Pemindai kode QR Waveshare] (https://www.waveshare.com/barcode-scanner-module.htm) dengan header pin panjang seperti [ini] (https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) atau [ini] (https://www.amazon.com/gp/product/B015KA0RRU/) untuk menghubungkan pemindai ke papan (diperlukan 4 header pin).


Saat ini kami sedang mengerjakan papan ekstensi yang mencakup slot kartu pintar, pemindai kode QR, baterai, dan casing cetak 3d, tetapi tidak termasuk bagian utama - papan penemuan yang perlu Anda pesan secara terpisah. Dengan cara ini, serangan rantai pasokan masih belum menjadi masalah karena komponen-komponen yang sangat penting bagi keamanan dibeli dari toko elektronik secara acak.


Anda dapat mulai menggunakan Specter bahkan tanpa komponen tambahan, tetapi Anda akan dapat berkomunikasi dengannya melalui USB atau slot kartu SD internal. Menggunakan Specter melalui USB berarti tidak memiliki celah udara sehingga Anda kehilangan properti keamanan yang penting.


### Pemindai QR


Untuk pemindai kode QR, Anda memiliki beberapa opsi.


**Opsi 1. Direkomendasikan.** Pemindai yang sangat bagus dari Waveshare (40$)


[Pemindai gelombang (Waveshare scanner) (https://www.waveshare.com/barcode-scanner-module.htm) - Anda perlu menemukan cara untuk memasangnya dengan baik, mungkin menggunakan semacam pelindung Arduino Prototype dan selotip.


Tidak perlu menyolder, tetapi jika Anda memiliki keterampilan menyolder, Anda bisa membuat wallet menjadi lebih bagus;)


**Opsi 2.** Pemindai yang sangat bagus dari Mikroe tetapi cukup mahal (150$):


[Klik Barcode] (https://www.mikroe.com/barcode-click) + [Adaptor] (https://www.mikroe.com/arduino-uno-click-shield)


**Opsi 3.** Pemindai QR lainnya


Anda bisa menemukan beberapa pemindai murah di China. Kualitasnya sering kali tidak terlalu bagus, tetapi Anda bisa mengambil kesempatan. Bahkan mungkin ESPcamera bisa digunakan. Anda hanya perlu menghubungkan daya, UART (pin D0 dan D1), dan pemicu ke D5.


**Opsi 4.** Tidak ada pemindai.


Maka, Anda hanya dapat menggunakan Specter dengan USB / SD Card.


Kecuali jika Anda membuat modul komunikasi Anda sendiri yang menggunakan sesuatu yang lain daripada kode QR - audiomodem, bluetooth, atau apa pun. Segera setelah dapat dipicu dan mengirim data melalui serial, Anda dapat melakukan apa pun yang Anda inginkan.


### Komponen opsional


Jika Anda menambahkan powerbank kecil atau baterai & pengisi daya/booster, wallet Anda akan menjadi benar-benar mandiri;)



## Perakitan Spectre-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Menghubungkan pemindai kode batang Waveshare


Firmware wallet akan mengonfigurasi pemindai untuk Anda pada saat pertama kali dijalankan, jadi tidak diperlukan prakonfigurasi manual.


Berikut ini cara Anda menghubungkan pemindai ke papan tulis:


![image](assets/fr/02.webp)


Untuk kenyamanan, Anda dapat membeli pelindung Arduino Protype dan menyolder & memasang semua yang ada di atasnya (misalnya [yang ini] (https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Manajemen daya


Di sisi atas papan terdapat jumper yang menentukan di mana ia akan mengambil daya. Anda dapat mengubah posisi jumper dan memilih sumber daya menjadi salah satu port USB atau pin VIN dan menghubungkan baterai eksternal di sana (harus 5V).


### Kandang untuk DIY


Lihat folder [lampiran] (https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Jadilah kreatif!


Rakitlah Specter-DIY Anda sendiri dan kirimkan gambar-gambarnya kepada kami (buatlah pull request atau hubungi kami).


Lihatlah [Galeri] (https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) dengan Specters yang dikumpulkan oleh komunitas!




## Menginstal kode yang dikompilasi


Dengan bootloader yang aman, penginstalan awal firmware sedikit berbeda. Peningkatan lebih mudah dan tidak perlu menghubungkan perangkat keras wallet ke komputer.


![video](https://youtu.be/eF4cgK_L6T4)


### Mem-flash firmware awal


**Catatan** Jika Anda tidak ingin menggunakan binari dari rilis, lihat [dokumentasi bootloader](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) yang menjelaskan cara mengkompilasi dan mengkonfigurasinya untuk menggunakan kunci publik Anda, bukan kunci publik kami.



- Jika Anda meng-upgrade dari versi di bawah `1.4.0` atau meng-upload firmware untuk pertama kalinya, gunakan `initial_firmware_<version>.bin` dari halaman [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Verifikasi tanda tangan file `sha256.signed.txt` dengan [kunci PGP Stepan](https://stepansnigirev.com/ss-specter-release.asc)
 - Verifikasi hash dari `initial_firmware_<version>.bin` terhadap hash yang disimpan di `sha256.signed.txt`
- Jika Anda meng-upgrade dari bootloader kosong atau Anda melihat pesan kesalahan bootloader bahwa firmware tidak valid, lihat bagian berikutnya - Mem-flash firmware Specter yang ditandatangani.
- Pastikan jumper daya papan penemuan Anda berada pada posisi STLK
- Sambungkan papan penemuan ke komputer Anda melalui kabel **miniUSB** di bagian atas papan.
    - Papan seharusnya muncul sebagai disk yang dapat dilepas bernama `DIS_F469NI`.
- Salin file `initial_firmware_<version>.bin` ke dalam root dari sistem berkas `DIS_F469NI`.
- Setelah papan selesai mem-flash firmware, papan akan mereset sendiri dan melakukan boot ulang ke bootloader. Bootloader akan memeriksa firmware dan melakukan booting ke firmware utama. Jika melihat pesan kesalahan bahwa tidak ada firmware yang ditemukan - ikuti petunjuk pembaruan dan unggah firmware melalui kartu SD.
- Sekarang Anda dapat mengganti jumper daya di tempat yang Anda sukai dan memberi daya pada papan dari powerbank atau baterai.


Mem-flash firmware awal melalui copy-paste file `.bin` terkadang gagal - sering kali karena kabel, atau jika Anda menyambungkan perangkat melalui hub USB. Dalam hal ini, Anda dapat mencoba beberapa kali lagi (biasanya berhasil dalam 2-3 kali percobaan).


Jika selalu gagal, Anda dapat menggunakan alat sumber terbuka [stlink](https://github.com/stlink-org/stlink/releases/latest). Instal dan ketik di terminal Anda: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Biasanya cara ini bekerja jauh lebih handal.


### Meningkatkan firmware



- Unduh `specter_upgrade_<version>.bin` dari [rilis] (https://github.com/cryptoadvance/specter-diy/releases).
- Salin biner ini ke root kartu SD (berformat FAT, maksimal 32 GB)
 - Pastikan hanya ada satu file `specter_upgrade***.bin` di direktori root
- Masukkan kartu SD ke slot SD pada papan penemuan dan nyalakan papan
- Bootloader akan mem-flash firmware dan akan memberi tahu Anda saat selesai.
- Nyalakan ulang papan - Anda akan melihat antarmuka Specter-DIY sekarang, ini akan menyarankan Anda untuk memilih kode PIN Anda


Setiap kali rilis baru keluar, cukup unduh `specter_upgrade_<version>.bin` dari rilis tersebut, masukkan ke dalam kartu SD dan upgrade perangkat seperti pada langkah sebelumnya. Bootloader akan memastikan hanya firmware yang telah ditandatangani yang dapat dimuat ke board.


### Cara mengetahui versi firmware


Buka menu `Pengaturan perangkat` - menu ini akan menampilkan nomor versi di bawah judul layar.


## Gunakan Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Keamanan dari Specter-DIY


### Perangkat keras


Tampilan dikontrol oleh MCU aplikasi.


Integrasi elemen aman belum ada - saat ini rahasia juga disimpan di MCU utama. Tetapi Anda dapat menggunakan wallet tanpa menyimpan rahasianya - Anda harus memasukkan frasa pemulihan Anda setiap saat. Mengapa harus mengingat passphrase yang panjang jika Anda dapat mengingat seluruh mnemonik?


Perangkat menggunakan flash eksternal untuk menyimpan beberapa file (QSPI), tetapi semua file pengguna ditandatangani oleh wallet dan diperiksa ketika dimuat.


Fungsionalitas pemindaian QR ada pada mikrokontroler terpisah sehingga semua pemrosesan gambar terjadi di luar MCU yang sangat penting bagi keamanan. Saat ini USB dan kartu SD masih dikelola oleh MCU utama, jadi jangan gunakan kartu SD dan USB jika Anda ingin mengurangi permukaan serangan.


### Perlindungan PIN (autentikasi pengguna)


Selama boot pertama, sebuah rahasia unik dihasilkan pada MCU utama. Rahasia ini memungkinkan Anda untuk memverifikasi bahwa perangkat tidak diganti dengan perangkat yang berbahaya - ketika Anda memasukkan kode PIN, Anda akan melihat daftar kata-kata yang akan tetap sama selama rahasianya masih ada.


Kode PIN Anda bersama dengan rahasia unik ini digunakan untuk membuat kunci dekripsi untuk kunci Bitcoin (jika Anda menyimpannya). Jadi, jika penyerang dapat melewati layar PIN, dekripsi akan tetap gagal.


Jika anda telah mengunci firmware (TODO: tambahkan tautan petunjuk di sini) maka secara efektif akan mengunci rahasianya juga, jadi jika penyerang memasukkan firmware yang berbeda ke papan, rahasianya akan terhapus dan anda akan bisa mengenalinya ketika anda mulai memasukkan kode PIN - urutan kata akan berbeda.


### Pembuatan frasa pemulihan


Ini adalah salah satu bagian terpenting dari wallet - untuk generate kuncinya dengan aman. Untuk melakukan hal ini dengan baik, kami menggunakan beberapa sumber entropi:



- TRNG dari mikrokontroler. Hak milik, bersertifikat, dan mungkin bagus tetapi kami tidak mempercayainya
- Layar sentuh. Setiap kali Anda menyentuh layar, kami mengukur posisi dan momen saat sentuhan ini terjadi (dalam detak mikrokontroler pada 180MHz).
- Mikrofon internal - belum. Papan ini memiliki dua mikrofon, sehingga perangkat keras wallet dapat mendengarkan Anda dan mencampurkan data ini ke kumpulan entropi.


Semua entropi ini di-hash dan dikonversi ke frasa pemulihan Anda. Entropi yang dihasilkan selalu lebih baik daripada sumber individu mana pun.


### Logika tingkat tinggi - dompet


Spectre beroperasi sebagai penyimpanan kunci. Ia menyimpan kunci pribadi HD yang dapat digunakan dalam dompet. Dompet ditentukan oleh deskriptornya. Kami juga mendukung miniscript.


Setiap wallet adalah milik jaringan tertentu. Ini berarti bahwa jika Anda mengimpor wallet di `testnet`, wallet tidak akan tersedia di `mainnet` atau `regtest` - Anda harus beralih ke jaringan ini dan mengimpor wallet secara terpisah.


### Verifikasi transaksi


Aturan berikut ini berlaku untuk transaksi yang akan ditandatangani oleh wallet:



- jika ditemukan input campuran dari dompet yang berbeda, pengguna akan diperingatkan ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- output perubahan menunjukkan nama wallet yang dikirim ke mereka
- untuk menggunakan multisig atau miniscript, Anda harus mengimpor wallet terlebih dahulu dengan menambahkan deskriptor wallet (melalui QR, USB, atau kartu SD)


## Dukungan deskriptor


Semua deskriptor Bitcoin yang normal dapat digunakan. Selain itu, kami memiliki beberapa ekstensi:


### Beberapa cabang dalam deskriptor


Untuk menghemat ruang pada kode QR, kami mengizinkan penambahan deskriptor dengan beberapa cabang sekaligus. Jika Anda ingin menggunakan `wpkh(xpub/0/*)` untuk menerima alamat dan `wpkh(xpub/1/*)` untuk mengubah alamat, Anda bisa menggabungkannya dalam satu deskriptor: `wpkh(xpub/{0,1}/*)` - wallet akan memperlakukan indeks pertama dari bagian kumpulan `{}` sebagai cabang untuk menerima alamat dan cabang kedua sebagai mengubah alamat.


Anda juga dapat menentukan lebih dari dua cabang, dan indeks cabang dapat berbeda untuk penanda tangan yang berbeda, sehingga deskriptor ini sangat aneh tetapi benar-benar valid:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Di sini untuk menerima alamat nomor 17, wallet akan menggunakan skrip dari `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Satu-satunya persyaratan adalah jumlah indeks dalam semua set sama (3 dalam kasus di atas).


### Derivasi default


Jika deskriptor berisi kunci publik utama tetapi tidak mengandung turunan wildcard, turunan default `/{0,1}/*` akan ditambahkan ke semua kunci yang diperluas dalam deskriptor. Jika setidaknya salah satu dari xpubs memiliki turunan wildcard, deskriptor tidak akan diubah.


Deskriptor `wpkh(xpub)` akan dikonversi menjadi `wpkh(xpub/{0,1}/*)`.


### Miniscript


Specter mendukung miniscript, tetapi tidak mendukung kompilasi policy-to-miniscript (karena terlalu mahal). Kami melakukan beberapa pemeriksaan pada miniscipt, sehingga hanya skrip `B` yang diperbolehkan pada level teratas dan semua argumen dalam sub-miniscript harus memiliki properti yang sesuai dengan [spec] (http://bitcoin.sipa.be/miniscript/).


Anda dapat menggunakan [bitcoin.sipa.be] (http://bitcoin.sipa.be/miniscript/) untuk generate deskriptor dari kebijakan dan kemudian mengimpornya ke wallet.


Sebagai contoh, kebijakan "Saya dapat membelanjakan sekarang, atau dalam 100 hari istri saya dapat membelanjakan" dapat dikonversi ke dalam wallet seperti itu:


Kebijakan: `or(9@pk(xpubA),and(older(14400),pk(B)))` (kunci saya adalah 9 kali lebih mungkin)


Miniscript: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Karena di sini kita tidak memiliki turunan wildcard, turunan default `/{0,1}/*` akan ditambahkan ke xpubs.



---

Lisensi MIT


Hak Cipta (c) 2019 cryptoadvance


---