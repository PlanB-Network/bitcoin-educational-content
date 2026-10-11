---
name: Satochip
description: Pengaturan dan penggunaan kartu pintar Satochip
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang didedikasikan untuk mengelola dan mengamankan kunci privat dari dompet Bitcoin. Berbeda dengan dompet perangkat lunak (atau dompet panas) yang dipasang pada perangkat umum yang sering terhubung ke Internet, dompet perangkat keras memungkinkan isolasi fisik kunci privat, sehingga mengurangi risiko peretasan dan pencurian.

Tujuan utama dompet perangkat keras adalah meminimalkan fungsionalitas perangkat untuk memperkecil permukaan serangan. Permukaan serangan yang lebih kecil berarti lebih sedikit vektor serangan potensial, yaitu lebih sedikit celah dalam sistem yang bisa dimanfaatkan penyerang untuk mengakses bitcoin.

Disarankan untuk menggunakan dompet perangkat keras untuk mengamankan bitcoin kamu, terutama jika kamu menyimpan jumlah yang signifikan, baik secara nilai absolut maupun sebagai proporsi dari total aset kamu.

Dompet perangkat keras digunakan bersama perangkat lunak manajemen dompet di komputer atau smartphone. Perangkat lunak ini mengelola pembuatan transaksi, tetapi tanda tangan kriptografis yang diperlukan untuk memvalidasi transaksi dilakukan sepenuhnya di dalam dompet perangkat keras. Artinya, kunci privat tidak pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras menawarkan perlindungan ganda bagi pengguna: di satu sisi, perangkat ini mengamankan bitcoin kamu dari serangan jarak jauh dengan menjaga kunci privat tetap offline, dan di sisi lain, umumnya menawarkan ketahanan fisik yang lebih baik terhadap upaya ekstraksi kunci. Dua kriteria keamanan inilah yang bisa digunakan untuk menilai dan membandingkan berbagai model yang tersedia di pasar.

Dalam tutorial ini, aku mengajak kamu untuk mengenal salah satu solusi tersebut: Satochip.

## Pengenalan ke Satochip

Satochip adalah dompet perangkat keras berbentuk kartu dengan chip bersertifikasi *EAL6+*, yang merupakan standar keamanan sangat tinggi (*NXP JCOP*). Perangkat ini diproduksi oleh sebuah perusahaan asal Belgia.

![SATOCHIP](assets/notext/01.webp)

Kartu pintar ini dijual seharga €25, yang tergolong sangat terjangkau dibandingkan dompet perangkat keras lain di pasaran. Chip-nya merupakan *secure element* yang memastikan ketahanan sangat baik terhadap serangan fisik. Selain itu, kodenya bersifat open-source (*AGPLv3*). Namun, karena formatnya, Satochip tidak menawarkan opsi sebanyak perangkat lain. Tidak ada baterai, tidak ada kamera, dan tidak ada pembaca kartu microSD, karena ini memang berbentuk kartu. Kekurangan terbesar menurutku adalah tidak adanya layar pada dompet perangkat keras ini, sehingga lebih rentan terhadap jenis serangan jarak jauh tertentu. Artinya, kamu harus menandatangani secara buta dan mempercayai apa yang tampil di layar komputer kamu.

Meski punya keterbatasan, Satochip tetap menarik karena harganya yang murah. Dompet ini bisa digunakan untuk meningkatkan keamanan dompet pengeluaran, sebagai pelengkap dompet tabungan yang dilindungi oleh dompet perangkat keras dengan layar. Ini juga jadi solusi yang cocok buat kamu yang menyimpan bitcoin dalam jumlah kecil dan tidak ingin mengeluarkan ratusan euro untuk perangkat yang lebih canggih. Selain itu, penggunaan Satochip dalam konfigurasi multisig, atau bahkan dalam sistem dompet dengan timelock di masa depan, bisa menawarkan keuntungan yang menarik.

Perusahaan Satochip juga menawarkan dua produk lain. Ada Satodime, yaitu kartu penyimpan yang dirancang untuk menyimpan bitcoin secara offline, tetapi tidak memungkinkan transaksi. Ini semacam dompet kertas yang jauh lebih aman dan bisa digunakan, misalnya, untuk membuat hadiah. Terakhir, ada Seedkeeper, yaitu pengelola seedphrase. Perangkat ini bisa digunakan untuk menyimpan seed kamu secara aman tanpa harus langsung menuliskannya di selembar kertas.

## Bagaimana cara membeli Satochip?
Satochip sudah tersedia untuk dijual [di situs resmi](https://satochip.io/product/satochip/). Untuk membelinya di toko fisik, kamu juga bisa menemukan [daftar reseller resmi](https://satochip.io/resellers/) di situs web Satochip.
Untuk berinteraksi dengan perangkat lunak manajemen dompet kamu, Satochip menawarkan dua opsi: melalui komunikasi NFC atau melalui pembaca kartu pintar. Untuk opsi NFC, pastikan perangkat kamu kompatibel dengan teknologi ini atau gunakan pembaca NFC eksternal. Satochip beroperasi pada frekuensi standar 13.56 MHz. Jika tidak, kamu juga bisa menggunakan pembaca kartu pintar. Perangkat ini bisa kamu temukan di situs web Satochip atau di toko lainnya.


![SATOCHIP](assets/notext/02.webp)

## Bagaimana cara mengatur Satochip dengan Sparrow?

Setelah kamu menerima Satochip kamu, langkah pertama adalah memeriksa kemasannya untuk memastikan tidak ada yang terbuka. Kemasan Satochip harus dilengkapi dengan stiker segel. Jika stiker ini hilang atau rusak, itu bisa menjadi indikasi bahwa kartu pintar telah dikompromikan dan mungkin tidak asli.

![SATOCHIP](assets/notext/03.webp)
Kamu akan menemukan Satochip di dalamnya.

![SATOCHIP](assets/notext/04.webp)

Untuk mengelola dompet, dalam tutorial ini, aku menyarankan menggunakan Sparrow. Jika kamu belum memiliki perangkat lunaknya, [kunjungi situs resmi untuk mengunduhnya](https://sparrowwallet.com/download/). Kamu juga bisa melihat tutorial kami tentang Sparrow Wallet (segera hadir).

![SATOCHIP](assets/notext/05.webp)

Masukkan Satochip kamu ke dalam pembaca kartu pintar atau letakkan di atas pembaca NFC, dan sambungkan pembaca ke komputer kamu yang telah membuka Sparrow.

![SATOCHIP](assets/notext/06.webp)

Buka Sparrow Wallet dan pastikan kamu terhubung dengan benar ke node Bitcoin. Untuk melakukan ini, periksa tanda centang di kanan bawah: seharusnya kuning jika kamu terhubung ke node publik, hijau untuk koneksi ke Bitcoin Core, atau biru untuk Electrum.

![SATOCHIP](assets/notext/07.webp)

Di Sparrow Wallet, klik pada tab "*File*".

![SATOCHIP](assets/notext/08.webp)

Kemudian pada menu "*New Wallet*".

![SATOCHIP](assets/notext/09.webp)

Pilih nama untuk dompet kamu kemudian klik pada "*Create Wallet*".

![SATOCHIP](assets/notext/10.webp)

Klik pada tombol "*Connected Hardware Wallet*".

![SATOCHIP](assets/notext/11.webp)

Klik pada tombol "*Scan...*".

![SATOCHIP](assets/notext/12.webp)

Satochip kamu seharusnya muncul. Klik pada "*Import Keystore*".

![SATOCHIP](assets/notext/13.webp)

Selanjutnya, kamu perlu mengatur kode PIN untuk membuka kunci Satochip kamu. Pilih kata sandi yang kuat, antara 4 hingga 16 karakter. Pastikan kamu membuat cadangan kata sandi ini.

Perlu diingat, kata sandi ini bukan passphrase. Artinya, meskipun tanpa kata sandi ini, seedphrase kamu tetap memungkinkan untuk mengimpor ulang dompet ke dalam perangkat lunak jika diperlukan. Kata sandi ini hanya digunakan untuk mengamankan akses ke Satochip itu sendiri. Fungsinya setara dengan kode PIN pada dompet perangkat keras lainnya.

Setelah kata sandi dimasukkan, klik lagi tombol "*Import Keystore*".

![SATOCHIP](assets/notext/14.webp)

Catat lagi kata sandi tersebut, kemudian klik pada tombol "*Initialize*".
![SATOCHIP](assets/notext/15.webp)
Kamu kemudian sampai pada jendela untuk menghasilkan frasa mnemonik Anda. Klik tombol "*Generate New*".

![SATOCHIP](assets/notext/16.webp)
Buat satu atau lebih salinan fisik dari seedphrase kamu dengan menuliskannya di atas kertas atau media logam. Perlu kamu sadari, frasa ini memberikan akses penuh ke bitcoin kamu tanpa perlindungan tambahan. Artinya, jika seseorang menemukannya, mereka bisa langsung mencuri bitcoin kamu, bahkan tanpa akses ke Satochip atau kode PIN-nya. Karena itu, sangat penting untuk mengamankan cadangan ini dengan baik.  

Selain itu, seedphrase ini memungkinkan kamu memulihkan akses ke bitcoin jika Satochip hilang, rusak, atau jika kamu lupa kode PIN.

![SATOCHIP](assets/notext/17.webp)

Dompet Bitcoin kamu telah berhasil dibuat.

![SATOCHIP](assets/notext/18.webp)

Klik lagi pada tombol "*Import Keystore*".

![SATOCHIP](assets/notext/19.webp)

Dompet kamu sekarang telah dibuat. Kunci privat Anda sekarang disimpan pada smartcard Satochip kamu. Klik pada tombol "*Apply*" untuk melanjutkan.

![SATOCHIP](assets/notext/20.webp)

Disarankan untuk menetapkan kata sandi tambahan guna mengamankan data publik yang dikelola oleh Sparrow Wallet, selain kode PIN Satochip kamu. Kata sandi ini akan melindungi akses ke Sparrow Wallet, sehingga membantu menjaga kunci publik, alamat, dan riwayat transaksi kamu dari akses yang tidak sah.

![SATOCHIP](assets/notext/21.webp)

Masukkan kata sandi kamu di dua kolom, lalu klik pada tombol "*Set Password*".

![SATOCHIP](assets/notext/22.webp)

Dan begitulah, Satochip kamu sekarang telah dikonfigurasi di Sparrow Wallet.

![SATOCHIP](assets/notext/23.webp)

Sekarang dompet telah dibuat, kamu dapat mencabut Satochip milikmu. Simpan di tempat yang aman!

## Bagaimana cara menerima bitcoin dengan Satochip?

Setelah berada di dompet kamu, klik pada tab "*Receive*".

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet akan menghasilkan alamat untuk dompet kamu. Biasanya, pada dompet perangkat keras lain, kamu disarankan untuk mengklik "*Display Address*" guna memverifikasi alamat langsung di layar perangkat. Sayangnya, opsi ini tidak tersedia pada Satochip, tetapi pastikan kamu tetap menggunakannya saat memakai dompet perangkat keras lain.

![SATOCHIP](assets/notext/25.webp)

Kamu dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan alamat ini. Ini adalah praktik yang baik yang membantu Anda mengelola UTXO kamu dengan lebih baik.

![SATOCHIP](assets/notext/26.webp)

Untuk informasi lebih lanjut tentang pelabelan, aku juga merekomendasikan untuk memeriksa tutorial lain ini:

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Aku kemudian dapat menggunakan alamat ini untuk menerima bitcoin.

![SATOCHIP](assets/notext/27.webp)
## Bagaimana cara Mengirim Bitcoin dengan Satochip?
Sekarang setelah kamu menerima sats pertama di dompet yang diamankan dengan Satochip, kamu juga bisa mulai membelanjakannya! Hubungkan Satochip ke komputer kamu, buka Sparrow Wallet, lalu masuk ke tab "*Send*" untuk membuat transaksi baru.

![SATOCHIP](assets/notext/28.webp)
Jika kamu ingin melakukan coin control, yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin kamu gunakan, lalu klik "*Kirim Terpilih*". Kamu akan diarahkan ke layar yang sama seperti tab "*Send*", tetapi dengan UTXO yang sudah dipilih untuk transaksi.

![SATOCHIP](assets/notext/29.webp)

Masukkan alamat tujuan. Kamu juga dapat memasukkan beberapa alamat dengan mengklik tombol "*+ Tambah*".

![SATOCHIP](assets/notext/30.webp)

Catat sebuah "*Label*" untuk mengingat tujuan dari pengeluaran ini.

![SATOCHIP](assets/notext/31.webp)

Pilih jumlah yang akan dikirim ke alamat ini.

![SATOCHIP](assets/notext/32.webp)

Sesuaikan tarif biaya transaksi kamu sesuai dengan pasar saat ini.

![SATOCHIP](assets/notext/33.webp)

Pastikan semua parameter transaksi kamu sudah benar, kemudian klik pada "*Buat Transaksi*".

![SATOCHIP](assets/notext/34.webp)

Jika semuanya sesuai dengan keinginan kamu, klik pada "*Finalisasi Transaksi untuk Ditandatangani*".

![SATOCHIP](assets/notext/35.webp)

Klik pada "*Tanda Tangan*".

![SATOCHIP](assets/notext/36.webp)

Klik pada "*Tanda Tangan*" lagi di sebelah Satochip kamu.

![SATOCHIP](assets/notext/37.webp)

Masukkan kode PIN Satochip kamu, kemudian klik pada "*Tanda Tangan*" lagi untuk menandatangani transaksi.

![SATOCHIP](assets/notext/38.webp)

Transaksi kamu sekarang sudah ditandatangani. Klik pada "*Siarkan Transaksi*" untuk menyiarkannya ke jaringan Bitcoin.

![SATOCHIP](assets/notext/39.webp)

Kamu dapat menemukannya di tab "*Transaksi*" dari Sparrow Wallet.

![SATOCHIP](assets/notext/40.webp)

Selamat, sekarang kamu sudah mengerti cara menggunakan Satochip! Kalau tutorial ini terasa bermanfaat, aku akan sangat menghargai jempol ke atas di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosial kamu. Terima kasih banyak!
