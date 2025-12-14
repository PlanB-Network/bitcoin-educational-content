---
name: Seedkeeper x SeedSigner
description: Bagaimana cara menggunakan Seedkeeper dengan SeedSigner saya?
---

![cover](assets/cover.webp)



*Terima kasih kepada tim [Satochip](https://satochip.io/) yang telah setuju untuk menggunakan kembali [video mereka](https://www.youtube.com/@satochip/videos) dalam tutorial ini. Terima kasih juga kepada [Crypto Guide](https://www.youtube.com/@CryptoGuide/) untuk fork dari firmware SeedSigner, yang memungkinkan dukungan untuk smartcard



---

SeedSigner adalah perangkat keras wallet yang Anda rakit sendiri dari perangkat keras standar, biasanya menggunakan Raspberry Pi Zero. wallet ini disebut "*stateless*": tidak seperti kebanyakan model lain yang ada di pasaran (Coldcard, Trezor, Ledger, dll.), wallet ini tidak menyimpan data apa pun di memori permanen, dan hanya beroperasi langsung dari RAM. Akibatnya, seed portofolio Anda tidak pernah disimpan di SeedSigner. Setiap kali Anda memulai ulang, Anda harus mengisinya agar perangkat dapat menandatangani transaksi Anda. Metode yang paling umum adalah dengan menyimpan seed Anda sebagai kode QR, yang kemudian Anda pindai setiap kali Anda menggunakannya (*SeedQR*).



Akan tetapi, pendekatan ini memiliki risiko yang signifikan: seed harus tetap dapat diakses dalam bentuk teks yang jelas sehingga dapat dipindai. Jika terjadi pencurian atau penyusupan, penyerang dapat dengan mudah mendapatkannya dan mencuri bitcoin Anda.



Untuk mengatasi kelemahan ini, SeedSigner dapat digabungkan dengan [**Seedkeeper**] (https://satochip.io/product/seedkeeper/), sebuah kartu pintar yang dikembangkan oleh Satochip. Hal ini memungkinkan frase mnemonic (atau rahasia lainnya) untuk disimpan di dalam secure element yang dilindungi oleh kode PIN. Applet Seedkeeper merupakan sumber terbuka, dan secure element-nya memiliki sertifikasi EAL6+. Digunakan bersama dengan SeedSigner, aplikasi ini menawarkan fitur keamanan yang sangat menarik: kunci Anda tetap dikelola sepenuhnya secara offline, Anda menandatangani transaksi Anda pada layar yang terpercaya, dan seed secara fisik terlindungi dengan smartcard yang tahan terhadap serangan fisik.



Yang Anda perlukan untuk menyelesaikan instalasi adalah item berikut ini:




- Peralatan yang biasa dibutuhkan untuk SeedSigner klasik: Raspberry Pi Zero, layar Waveshare 1.3", kamera yang kompatibel dan kartu microSD (Anda akan menemukan detail lebih lanjut dalam tutorial SeedSigner di bawah);
- Kit ekstensi SeedSigner, tersedia [di toko resmi Satochip] (https://satochip.io/product/seedsigner-extension-kit/), yang memungkinkan Anda membaca dan menulis ke smartcard secara langsung dari SeedSigner Anda. Pilihan lainnya adalah dengan menggunakan pembaca smartcard eksternal, yang dapat dihubungkan dengan kabel ke port Micro-USB pada Raspberry Pi. Namun, saya sendiri belum menguji solusi ini;
- Seedkeeper, atau sebagai alternatif, sebuah smartcard kosong untuk menginstal applet Seedkeeper (kit ekstensi yang dijual oleh Satochip sudah termasuk smartcard kosong).



![Image](assets/fr/01.webp)



Tutorial ini mencakup dua skenario:




- Jika Anda sudah memiliki portofolio Bitcoin yang dikelola melalui SeedSigner Anda, cukup instal firmware yang baru. Anda kemudian dapat terus menggunakan wallet yang sudah ada, kali ini menggunakan Seedkeeper untuk keamanan tambahan.
- Jika Anda belum memiliki Bitcoin wallet yang terhubung dengan SeedSigner Anda, Anda harus mengikuti langkah **5** dan **6** pada tutorial di bawah ini. Bagian ini menjelaskan bagaimana cara membuat generate frasa mnemonik dengan SeedSigner, menyimpannya melalui *SeedQR*, dan kemudian menghubungkan wallet ini ke Sparrow Wallet untuk mengelolanya. Saya tidak akan membahas prosedur-prosedur ini di sini dan **Saya mengasumsikan bahwa Anda telah memiliki Bitcoin wallet yang berfungsi, yang dikonfigurasi dengan Sparrow dan SeedSigner Anda**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Instal firmware



Untuk menggunakan SeedSigner Anda dengan Seedkeeper, Anda perlu menginstal firmware alternatif, yang berbeda dari SeedSigner asli, untuk mendukung pembacaan kartu pintar. Untuk hal ini, [saya sarankan untuk menggunakan fork dari "*3rdIteration*"] (https://github.com/3rdIteration/seedsigner). Unduh [versi terbaru dari gambar] (https://github.com/3rdIteration/seedsigner/releases) (`.zip`) yang sesuai dengan model Raspberry Pi yang Anda gunakan.



![Image](assets/fr/02.webp)



Jika Anda belum memilikinya, unduh perangkat lunak [Balena Etcher] (https://etcher.balena.io/), kemudian lanjutkan sebagai berikut:




- Masukkan kartu microSD ke dalam komputer Anda;
- Meluncurkan Pengetsa ;
- Pilih file `.zip` yang baru saja Anda unduh;
- Pilih kartu microSD sebagai target;
- Klik `Flash!`.



![Image](assets/fr/03.webp)



Tunggu hingga proses selesai: microSD Anda sekarang siap digunakan. Sekarang Anda dapat melanjutkan untuk merakit perangkat Anda.



Untuk rincian lebih lanjut tentang instalasi firmware dan verifikasi perangkat lunak (langkah yang sangat saya sarankan untuk Anda lakukan), lihat tutorial berikut ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Merakit pembaca kartu pintar



![video](https://youtu.be/jqE8HDMCImA)



Mulailah dengan memasang kamera pada Raspberry Pi Zero, dengan hati-hati memasukkannya ke pin kamera dan menguncinya dengan tab hitam. Kemudian letakkan Pi di bagian bawah casing, pastikan untuk menyelaraskan port dengan lubang yang sesuai.



![Image](assets/fr/04.webp)



Kemudian pasang pembaca kartu pintar ke pin GPIO Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Geser penutup plastik di atas pembaca kartu pintar hingga posisinya benar.



![Image](assets/fr/06.webp)



Kemudian tambahkan layar ke pin GPIO ekstensi.



![Image](assets/fr/07.webp)



Terakhir, masukkan kartu microSD yang berisi firmware ke dalam port samping pada Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Anda sekarang dapat menghubungkan SeedSigner Anda baik melalui port Micro-USB Raspberry Pi Zero, atau melalui port USB-C ekstensi. Kedua opsi tersebut berfungsi. Tunggu beberapa detik untuk memulai, maka Anda akan melihat layar selamat datang muncul.



![Image](assets/fr/09.webp)



Untuk detail lebih lanjut tentang pengaturan awal SeedSigner Anda, saya sarankan tutorial berikut ini:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Mem-flash kartu pintar dengan applet Seedkeeper (opsional)



![video](https://youtu.be/NF4HemyEcOY)



Jika Anda sudah memiliki Seedkeeper, Anda dapat melewati langkah ini dan langsung ke langkah 4. Pada bagian ini, kita akan melihat cara memasang applet Seedkeeper pada smartcard kosong (metode DIY).



Untuk memulai, buka menu `Tools > Smartcard Tools` pada SeedSigner Anda.



![Image](assets/fr/10.webp)



Kemudian pilih `Tools DIY > Instal Applet`.



![Image](assets/fr/11.webp)



Masukkan kartu pintar Anda ke dalam pembaca SeedSigner, dengan chip menghadap ke bawah, lalu pilih applet `SeedKeeper`.



![Image](assets/fr/12.webp)



Harap bersabar selama instalasi: prosesnya mungkin memerlukan waktu beberapa puluh detik.



![Image](assets/fr/13.webp)



Setelah applet berhasil diinstal, Anda dapat melanjutkan ke langkah 4.



![Image](assets/fr/14.webp)



## 4. Menyimpan SeedQR yang sudah ada di Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Sekarang setelah Seedkeeper Anda beroperasi, Anda bisa menyimpan mnemonik Bitcoin wallet Anda di smartcard. Untuk memulai, nyalakan SeedSigner Anda seperti biasa, lalu pindai *SeedQR* wallet Anda untuk memuatnya ke dalam perangkat. Setelah seed diimpor, cukup pilih `Selesai`.



![Image](assets/fr/15.webp)



Saat seed dimuat, akses menu `Backup Seed`.



![Image](assets/fr/16.webp)



Kemudian masukkan Seedkeeper Anda ke dalam drive SeedSigner, dan pilih opsi `Ke SeedKeeper`.



![Image](assets/fr/17.webp)



SeedSigner kemudian akan meminta Anda memasukkan kode PIN untuk Seedkeeper Anda. Karena ini adalah kartu kosong, tidak ada kode yang belum ditentukan. Masukkan kode apa pun untuk melewati langkah ini, lalu validasi.



![Image](assets/fr/18.webp)



SeedSigner mendeteksi bahwa Seedkeeper belum diinisialisasi (misalnya, tidak ada kata sandi yang ditetapkan). Klik `Saya Mengerti` untuk melanjutkan.



![Image](assets/fr/19.webp)



Sekarang pilih kode PIN baru Seedkeeper Anda, antara 4 sampai 16 karakter. Untuk keamanan tambahan, pilihlah kode yang panjang dan acak: kode ini adalah satu-satunya penghalang yang melindungi akses fisik ke frasa mnemonik Anda.



Ingatlah untuk menyimpan PIN ini segera setelah dibuat, baik di dalam sebuah pengelola kata sandi yang handal, atau di sebuah media fisik yang terpisah, tergantung pada strategi Anda. Pada kasus terakhir, pastikan untuk tidak menyimpan media yang berisi PIN di tempat yang sama dengan Seedkeeper Anda, karena jika tidak, proteksi tidak akan efektif. Penting untuk memiliki salinan cadangan: **Tanpa PIN ini, Anda tidak akan bisa mengakses seed Anda, dan bitcoin Anda akan hilang**.



![Image](assets/fr/20.webp)



Anda kemudian dapat mendefinisikan `Label` yang terkait dengan frasa mnemonik Anda. Label ini berguna jika Anda menyimpan beberapa rahasia di Seedkeeper, sehingga Anda dapat dengan mudah mengidentifikasinya.



![Image](assets/fr/21.webp)



Frasa mnemonik Anda sekarang tersimpan pada kartu pintar.



![Image](assets/fr/22.webp)



Dalam hal strategi keamanan, ada beberapa pendekatan yang bisa dilakukan, tergantung pada kebutuhan dan tingkat eksposur risiko Anda. Secara pribadi, saya menyarankan agar Anda menyimpan setidaknya 2 salinan seed Anda:




- Ini adalah yang pertama untuk kartu pintar, yang dapat Anda akses dengan mudah untuk operasi sehari-hari, seperti memverifikasi alamat atau menandatangani transaksi. Metode ini praktis (seperti yang akan kita lihat di bagian 5) dan tetap aman berkat perlindungan yang ditawarkan oleh kode PIN, sehingga Anda dapat tetap mengaksesnya tanpa risiko besar;
- Salinan kedua dari frasa mnemonik Anda yang tidak terenkripsi, yang berfungsi sebagai cadangan utama portofolio Anda, untuk digunakan hanya jika terjadi kehilangan atau pencurian terhadap Seedkeeper. Karena versi ini tidak terenkripsi, versi ini harus disimpan di lokasi yang terpisah dan lebih aman, untuk mencegah kompromi simultan dari 2 cadangan.



Tergantung pada strategi perlindungan dan profil risiko Anda, Anda juga dapat menduplikasi seed di beberapa Seedkeeper yang berbeda, atau membuat beberapa salinan fisik dari mnemonik. Untuk mempelajari lebih lanjut mengenai praktik-praktik ini, lihat tutorial berikut:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Memuat seed dari Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Anda sekarang dapat menggunakan Seedkeeper Anda untuk memuat frasa mnemonik Anda ke dalam SeedSigner pada saat startup, dan dengan demikian menandatangani transaksi Bitcoin Anda. Untuk memulai, nyalakan SeedSigner Anda dengan mencolokkannya, kemudian buka menu `Seeds`.



![Image](assets/fr/23.webp)



Kemudian pilih opsi `Dari SeedKeeper`.



![Image](assets/fr/24.webp)



Masukkan Seedkeeper Anda ke dalam pembaca kartu pintar, lalu masukkan kode PIN Anda untuk membukanya. Konfirmasikan entri Anda dengan menekan tombol konfirmasi di kanan bawah, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper dapat berisi beberapa rahasia, sehingga SeedSigner akan meminta Anda untuk memilih salah satu yang ingin Anda muat. Label yang ditampilkan sesuai dengan nama yang Anda tentukan di langkah 4. Jika, seperti pada kasus saya, Anda hanya mendaftarkan satu seed, hanya satu pilihan yang tersedia.



![Image](assets/fr/26.webp)



seed Anda sekarang telah dimuat. Periksa apakah ini adalah wallet yang benar dengan membandingkan sidik jari yang ditampilkan pada layar dengan sidik jari yang ditentukan dalam pengaturan Sparrow Wallet Anda. Sidik jari ini juga disediakan ketika wallet pertama kali dibuat.



Jika Anda menggunakan passphrase, Anda bisa menerapkannya pada tahap ini (lihat bagian 6 dari tutorial ini). Jika tidak, cukup klik `Done`.



![Image](assets/fr/27.webp)



Anda kemudian dapat menggunakan wallet Anda seperti biasa: memeriksa alamat pengiriman dan menandatangani transaksi, seperti halnya dengan SeedSigner klasik. Untuk mengetahui lebih lanjut tentang cara menggunakannya, lihat tutorial khusus:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Menggunakan Seedkeeper dengan passphrase BIP39



Apakah Anda menggunakan passphrase untuk melindungi portofolio Bitcoin Anda? Anda juga bisa mendaftarkannya di Seedkeeper Anda, di samping seed Anda. Solusi ini akan memungkinkan Anda untuk memuat wallet Anda dengan cepat ke SeedSigner, tanpa harus memasukkan passphrase secara manual pada keypad kecil setiap kali Anda menggunakannya.



Menurut saya, metode ini sangat menarik, karena memungkinkan Anda mendapatkan keuntungan dari keunggulan keamanan passphrase, sekaligus menghilangkan kendala yang terkait dengan penggunaan sehari-hari. Berikut ini contoh konfigurasi yang saya rekomendasikan:




- Simpanlah seed dan passphrase Anda di Seedkeeper, yang dilindungi oleh kode PIN yang kuat (ini penting). Cadangan ini akan memungkinkan Anda untuk menggunakan wallet Anda dengan mudah setiap hari. Jika Anda mau, Anda bisa menduplikasi informasi ini pada Seedkeeper kedua;
- Simpan juga salinan yang jelas dari mnemonik dan passphrase Anda, di atas kertas atau logam. Ini adalah cadangan terakhir Anda jika Anda kehilangan Seedkeeper atau PIN-nya. Pastikan untuk menyimpan salinan ini di lokasi yang terpisah, sehingga tidak dapat dikompromikan secara bersamaan.



Dalam konfigurasi ini, jika seseorang mendapatkan mnemonic plaintext Anda saja, mereka tidak akan dapat mencuri apa pun tanpa mengetahui passphrase (asalkan, tentu saja, cukup kuat untuk menahan serangan brute force). Sebaliknya, jika seseorang menemukan passphrase Anda dalam bentuk teks biasa, ia tidak akan dapat digunakan tanpa frasa mnemonik yang sesuai.



Terakhir, jika seseorang berhasil mendapatkan akses fisik ke Seedkeeper Anda yang berisi seed dan passphrase, mereka tidak akan dapat mengekstrak apa pun tanpa mengetahui kode PIN. Tidak seperti passphrase, kode ini tidak dapat dipaksakan, karena smartcard secara otomatis mengunci dirinya sendiri setelah 5 kali percobaan yang tidak valid.



Oleh karena itu, keamanan konfigurasi ini didasarkan pada 2 hal penting:




- Sebuah **passphrase yang kuat**: harus panjang, acak dan berisi berbagai macam karakter. Kerumitannya tidak menjadi masalah bagi Anda, karena Anda hanya perlu memasukkannya sekali pada keyboard selama inisialisasi; setelah itu, ia akan dikirimkan oleh Seedkeeper ;
- Kode PIN yang kuat untuk Seedkeeper: juga acak dan terdiri dari 16 karakter.



Untuk menyiapkan pengaturan ini, mulailah dengan memuat passphrase Anda ke dalam SeedSigner seperti biasa. Anda dapat mengikuti prosedur yang dijelaskan dalam tutorial ini:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Setelah portofolio Anda dengan passphrase dimuat dengan benar ke SeedSigner, buka menu `Seeds` dan pilih footprint yang sesuai dengan portofolio ini. Perhatikan bahwa footprint ini berbeda dengan footprint portofolio tanpa passphrase.



![Image](assets/fr/28.webp)



Kemudian klik `Backup Seed`, masukkan Seedkeeper ke dalam drive, dan pilih `Untuk SeedKeeper`.



![Image](assets/fr/29.webp)



Masukkan PIN Anda untuk membuka kunci Seedkeeper, lalu tetapkan label pada rahasia ini. Anda dapat membiarkan sidik jari sebagai label untuk mempertahankan suatu bentuk penyangkalan yang masuk akal, atau secara eksplisit menyatakan `Sandi Wallet`, misalnya.



![Image](assets/fr/30.webp)



Portofolio passphrase Anda sekarang terdaftar di Seedkeeper.



![Image](assets/fr/31.webp)



Lain kali Anda memulai, cukup masukkan Seedkeeper Anda ke dalam drive, lalu arahkan ke `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Masukkan PIN Anda untuk membuka kunci smartcard, lalu pilih wallet yang sesuai dengan passphrase Anda.



![Image](assets/fr/33.webp)



Periksa jejak passphrase dan wallet Anda, lalu konfirmasikan.



![Image](assets/fr/34.webp)



Anda sekarang dapat mengakses portofolio Anda dengan passphrase dan menandatangani transaksi Anda seperti yang biasa Anda lakukan pada SeedSigner.



## 7. Opsi tambahan



Dalam menu `Tools > Smartcard Tools`, Anda akan menemukan beberapa opsi untuk mengelola Seedkeeper Anda:





- Dalam menu `Common Tools`, Anda dapat :
 - Periksa keaslian kartu;
 - Ubah kode PIN ;
 - Mengubah label yang terkait dengan rahasia Anda ;
 - Nonaktifkan fungsi NFC (disarankan jika hanya menggunakan pembaca chip);
 - Lakukan pengaturan ulang pabrik.





- Dalam menu `SeedKeeper Functions`, Anda dapat :
 - Lihat daftar rahasia terdaftar ;
 - Menyimpan rahasia baru ;
 - Menghapus rahasia yang sudah ada ;
 - Simpan atau muat deskriptor Anda (fungsi yang berguna untuk portofolio multi-sig).





- Dalam menu `DIY Tools`, Anda dapat :
 - Mengkompilasi applet Seedkeeper ;
 - Pasang applet pada kartu kosong ;
 - Hapus applet Seedkeeper untuk mengatur ulang dan membuatnya kosong lagi.



Sekarang Anda tahu cara menggunakan Seedkeeper untuk mencadangkan portofolio Anda dengan aman dalam kombinasi dengan SeedSigner.



Jika pengaturan ini meyakinkan Anda, jangan ragu untuk mendukung proyek yang memungkinkannya:




- Dengan membeli peralatan Anda secara langsung [di situs web Satochip] (https://satochip.io/shop/);
- Dengan memberikan [donasi untuk proyek SeedSigner] (https://seedsigner.com/donate/);
- Dengan berlangganan [saluran YouTube Crypto Guide] (https://www.youtube.com/@CryptoGuide/), yang dijalankan oleh orang yang mengelola repositori GitHub yang menghosting firmware yang dimodifikasi.