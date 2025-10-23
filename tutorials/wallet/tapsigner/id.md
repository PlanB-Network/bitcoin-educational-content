---
name: Tapsigner
description: Mengatur dan menggunakan Tapsigner dengan Nunchuk
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang dirancang khusus untuk mengelola dan melindungi kunci privat dari dompet Bitcoin. Berbeda dengan dompet perangkat lunak (atau dompet panas) yang dipasang di perangkat umum dan sering terhubung ke Internet, dompet perangkat keras memungkinkan isolasi fisik kunci privat, sehingga mengurangi risiko peretasan dan pencurian.

Tujuan utama dompet perangkat keras adalah meminimalkan fungsionalitas perangkat agar permukaan serangannya sekecil mungkin. Permukaan serangan yang lebih kecil berarti lebih sedikit vektor serangan potensial, yaitu lebih sedikit titik lemah dalam sistem yang bisa dimanfaatkan penyerang untuk mengakses bitcoin.

Sangat disarankan untuk menggunakan dompet perangkat keras agar bitcoin kamu tetap aman, terutama jika jumlahnya cukup besar, baik dari segi nilai maupun proporsi terhadap total aset kamu.

Dompet perangkat keras digunakan bersama perangkat lunak pengelola dompet di komputer atau smartphone. Perangkat lunak ini membuat transaksi, tapi tanda tangan kriptografis yang diperlukan untuk memvalidasi transaksi dilakukan sepenuhnya di dalam dompet perangkat keras. Ini berarti kunci privat tidak pernah terpapar ke lingkungan yang berpotensi rentan.

Dompet perangkat keras memberikan perlindungan ganda bagi pengguna. Di satu sisi, mereka menjaga bitcoin kamu tetap aman dari serangan jarak jauh dengan menyimpan kunci privat secara offline. Di sisi lain, mereka umumnya memiliki ketahanan fisik yang lebih baik terhadap upaya ekstraksi kunci. Berdasarkan dua kriteria keamanan inilah, berbagai model dompet perangkat keras bisa dievaluasi dan dibandingkan.

Dalam tutorial ini, aku akan mengajak kamu mengenal salah satu solusi tersebut: Tapsigner dari Coinkite.

## Pengenalan ke Tapsigner

Tapsigner adalah dompet perangkat keras berbentuk kartu NFC yang dibuat oleh Coinkite, perusahaan yang juga dikenal sebagai pembuat Coldcard.

![TAPSIGNER NUNCHUK](assets/notext/01.webp)

Tapsigner memungkinkan penyimpanan pasangan kunci yang terdiri dari kunci privat induk dan kode rantai sesuai dengan BIP32, yang digunakan untuk menurunkan pohon kunci kriptografis. Kunci-kunci ini bisa digunakan untuk menandatangani transaksi hanya dengan menempelkan Tapsigner ke ponsel atau pembaca kartu NFC.

Kartu NFC ini dijual seharga $19,99, harga yang sangat terjangkau dibandingkan dengan dompet perangkat keras lain di pasaran. Namun karena bentuknya, Tapsigner tidak menawarkan banyak fitur seperti perangkat lain. Tidak ada baterai, tidak ada kamera, dan tidak ada pembaca kartu microSD—karena memang ini hanyalah kartu. Kekurangan paling besar menurutku adalah tidak adanya layar pada dompet perangkat keras ini, yang membuatnya lebih rentan terhadap beberapa jenis serangan jarak jauh. Hal ini memaksa pengguna untuk menandatangani transaksi secara buta dan mempercayai apa yang ditampilkan di layar komputer mereka.

Meski punya keterbatasan, Tapsigner tetap menarik karena harganya yang murah. Dompet ini bisa digunakan untuk meningkatkan keamanan dompet pengeluaran, di samping dompet tabungan yang dilindungi oleh dompet perangkat keras dengan layar. Tapsigner juga bisa jadi pilihan bagus bagi kamu yang hanya menyimpan sedikit bitcoin dan tidak ingin mengeluarkan ratusan euro untuk perangkat yang lebih canggih. Selain itu, penggunaan Tapsigner dalam konfigurasi multisig, atau mungkin dalam sistem dompet dengan timelock di masa depan, dapat memberikan manfaat tambahan yang menarik.

## Bagaimana cara membeli Tapsigner?

Tapsigner tersedia untuk dibeli [di situs resmi Coinkite](https://store.coinkite.com/store/category/tapsigner). Untuk membelinya di toko fisik, kamu juga bisa menemukan [daftar reseller bersertifikat](https://coinkite.com/resellers) di situs tersebut.
Kamu juga akan memerlukan telepon yang kompatibel dengan komunikasi NFC, atau perangkat USB untuk membaca kartu NFC pada frekuensi standar 13,56 MHz.
## Bagaimana cara menginisialisasi Tapsigner dengan Nunchuk?

Setelah kamu menerima Tapsigner, langkah pertama adalah memeriksa kemasannya untuk memastikan belum pernah dibuka. Jika paketnya rusak, itu bisa jadi tanda bahwa kartu sudah dikompromikan atau tidak asli. Coinkite mengirimkan Tapsigner dalam kotak khusus yang berfungsi memblokir gelombang radio. Pastikan kotak itu ada di dalam paketmu.

![TAPSIGNER NUNCHUK](assets/notext/02.webp)

Untuk mengelola dompet, kita akan menggunakan aplikasi seluler **Nunchuk Wallet**. Pastikan smartphone kamu kompatibel dengan NFC, kemudian unduh Nunchuk dari [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) atau langsung melalui file [`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases) nya.

![TAPSIGNER NUNCHUK](assets/notext/03.webp)
Kalau kamu menggunakan Nunchuk untuk pertama kalinya, aplikasi akan meminta kamu untuk membuat akun. Untuk tujuan tutorial ini, tidak perlu membuat satu. Jadi, pilih "*Lanjutkan sebagai tamu*" untuk melanjutkan tanpa akun.
![TAPSIGNER NUNCHUK](assets/notext/04.webp)

Kemudian klik pada "*Dompet tanpa bantuan*".

![TAPSIGNER NUNCHUK](assets/notext/05.webp)

Selanjutnya, klik pada tombol "*Saya akan menjelajah sendiri*".

![TAPSIGNER NUNCHUK](assets/notext/06.webp)

Setelah berada di Nunchuk, klik pada tombol "*+*" di sebelah tab "*Kunci*".

![TAPSIGNER NUNCHUK](assets/notext/07.webp)

Pilih "*Tambahkan kunci NFC*".

![TAPSIGNER NUNCHUK](assets/notext/08.webp)

Kemudian klik pada "*Tambahkan TAPSIGNER*".

![TAPSIGNER NUNCHUK](assets/notext/09.webp)

Klik pada "*Lanjutkan*" dan kemudian tempatkan kartu NFC Tapsigner Anda ke smartphone Anda.

![TAPSIGNER NUNCHUK](assets/notext/10.webp)

Jika Tapsigner Anda baru, Nunchuk akan menawarkan untuk menginisialisasinya. Klik pada "*Ya*".

![TAPSIGNER NUNCHUK](assets/notext/11.webp)

Sekarang kamu perlu memilih bagaimana cara membuat kode rantai indukmu.

Tapsigner menggunakan standar BIP32. Artinya, proses turunan kunci kriptografis yang melindungi bitcoin kamu tidak bergantung pada seedphrase seperti pada dompet BIP39, melainkan langsung pada kunci privat induk dan kode rantai induk. Dua elemen ini diproses melalui fungsi HMAC untuk menurunkan seluruh struktur dompet kamu secara deterministik dan hierarkis.

Kunci privat induk dihasilkan langsung oleh TRNG (*True Random Number Generator*) yang terintegrasi di dalam Tapsigner. Sementara itu, kode rantai induk harus disediakan dari luar. Pada tahap ini, kamu punya dua pilihan: biarkan Nunchuk membuatnya secara otomatis dengan menekan "Otomatis", atau buat sendiri dengan memilih "Lanjutan" lalu memasukkannya ke kolom yang tersedia.

![TAPSIGNER NUNCHUK](assets/notext/12.webp)
Selanjutnya, kamu perlu memilih kode PIN. Di area "*Starting PIN*", masukkan kode PIN yang tertulis di bagian belakang Tapsigner Anda.
![TAPSIGNER NUNCHUK](assets/notext/13.webp)

Pilih kode PIN untuk mengamankan akses fisik ke Tapsigner milikmu. Kode PIN ini tidak berperan dalam proses pemulihan dompet. Fungsinya hanya untuk membuka kunci Tapsigner milikmu untuk menandatangani transaksi. Pastikan untuk menyimpan kode PIN ini agar tidak lupa. Klik pada "*Continue*" untuk melanjutkan.

![TAPSIGNER NUNCHUK](assets/notext/14.webp)
Letakkan kartu Tapsigner Anda di belakang ponsel Anda sekarang untuk menginisialisasinya.
![TAPSIGNER NUNCHUK](assets/notext/15.webp)

Nunchuk kemudian akan membuat file pemulihan untuk dompet kamu, yang memungkinkan kamu memulihkan akses ke bitcoin jika kartu NFC-mu hilang. File ini dienkripsi menggunakan kode cadangan yang tertera di bagian belakang Tapsigner. Untuk memulihkan bitcoin, kamu membutuhkan file tersebut dan kode untuk mendekripsinya. Karena itu, sangat penting untuk menyalin kode ini ke kertas, sebab jika kamu kehilangan kartu NFC, kamu juga akan kehilangan akses ke kode tersebut, karena saat ini hanya tertulis di kartu. Pastikan juga kamu membuat beberapa salinan cadangan dari file pemulihan terenkripsi itu.

![TAPSIGNER NUNCHUK](assets/notext/16.webp)

Pilih nama untuk dompetmu.

![TAPSIGNER NUNCHUK](assets/notext/17.webp)

Dasar dompet kamu sekarang telah disiapkan. Untuk memverifikasi keaslian Tapsignermu, kapan saja, kamu bisa mengklik tombol "*Run health check*".

![TAPSIGNER NUNCHUK](assets/notext/18.webp)

Masukkan PIN milikmu.

![TAPSIGNER NUNCHUK](assets/notext/19.webp)

Kemudian letakkan kartu di belakang ponselmu.

![TAPSIGNER NUNCHUK](assets/notext/20.webp)

## Bagaimana cara membuat dompet di Tapsigner?

Kembali ke beranda Nunchuk, kamu dapat melihat bahwa Tapsigner kamu terdaftar dalam perangkat penandatangan yang tersedia.

![TAPSIGNER NUNCHUK](assets/notext/21.webp)

Kamu sekarang perlu menghasilkan kunci untuk dompet Bitcoin milikmi. Untuk melakukan ini, klik pada tombol "*+*" di sebelah kanan tab "*Wallets*".

![TAPSIGNER NUNCHUK](assets/notext/22.webp)

Klik pada "*Create new wallet*".

![TAPSIGNER NUNCHUK](assets/notext/23.webp)

Kemudian pilih opsi "*Create a new wallet using existing keys*".

![TAPSIGNER NUNCHUK](assets/notext/24.webp)

Pilih nama untuk dompet milikmu kemudian klik pada "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/25.webp)

Pilih Tapsigner milikmu sebagai perangkat penandatangan untuk set kunci baru ini, kemudian klik pada "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/26.webp)

Jika semuanya sesuai dengan keinginan Anda, konfirmasi pembuatan.

![TAPSIGNER NUNCHUK](assets/notext/27.webp)
Kamu kemudian bisa menyimpan file konfigurasi dompetmu. File ini hanya berisi kunci publik, jadi meskipun seseorang mendapatkannya, mereka tidak akan bisa mencuri bitcoin kamu. Namun, mereka bisa melacak semua transaksi kamu. Karena itu, file ini hanya berisiko terhadap privasi, bukan keamanan. Dalam beberapa kasus, file ini bisa sangat penting untuk memulihkan dompet kamu.
![TAPSIGNER NUNCHUK](assets/notext/28.webp)

Dan begitulah, dompet milikmu berhasil dibuat!

![TAPSIGNER NUNCHUK](assets/notext/29.webp)

Saat kamu tidak menggunakan Tapsigner, ingat untuk menyimpannya di dalam kotak bawaan dari Coinkite, yang berfungsi memblokir gelombang radio agar terlindung dari pembacaan tanpa izin.

## Bagaimana cara menerima bitcoin di Tapsigner?

Untuk menerima bitcoin, klik pada dompetmu.

![TAPSIGNER NUNCHUK](assets/notext/30.webp)

Kemudian gunakan alamat yang dihasilkan untuk menerima bitcoin. Jika jamu sebelumnya telah menerima bitcoin di dompet ini, kamu perlu mengklik tombol "*Receive*" untuk menghasilkan alamat penerimaan kosong baru.

![TAPSIGNER NUNCHUK](assets/notext/31.webp)

Setelah transaksi pengirim disiarkan, kamu akan melihatnya muncul di dompetmu.

![TAPSIGNER NUNCHUK](assets/notext/32.webp)

Klik pada "*View coins*".

![TAPSIGNER NUNCHUK](assets/notext/33.webp)

Pilih UTXO barumu.

![TAPSIGNER NUNCHUK](assets/notext/34.webp)

Klik pada "*+*" di sebelah "*Tags*" untuk menambahkan label pada UTXO milikmu. Ini adalah praktik yang baik, karena membantumu mengingat asal usul koin milikmu dan mengoptimalkan privasi untuk pengeluaran di masa depan.

![TAPSIGNER NUNCHUK](assets/notext/35.webp)

Pilih tag yang ada atau buat yang baru, kemudian klik pada "*Save*". Kamu juga memiliki opsi untuk membuat "*collections*" untuk mengorganisir koin milikmu secara lebih terstruktur.

![TAPSIGNER NUNCHUK](assets/notext/36.webp)

## Bagaimana cara mengirim bitcoin dengan Tapsigner?

Sekarang setelah milikmu memiliki bitcoin di dompetmu, Kamu juga dapat mengirimkannya. Untuk melakukan ini, klik pada dompet pilihanmu.

![TAPSIGNER NUNCHUK](assets/notext/37.webp)

Klik pada tombol "*Send*".

![TAPSIGNER NUNCHUK](assets/notext/38.webp)

Pilih jumlah yang akan dikirim, kemudian klik pada "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/39.webp)

Tambahkan "*note*" pada transaksimu di masa depan untuk mengingat tujuannya.

![TAPSIGNER NUNCHUK](assets/notext/40.webp)
Selanjutnya, masukkan secara manual alamat penerima di bidang yang ditentukan.
![TAPSIGNER NUNCHUK](assets/notext/41.webp)

Kamu juga dapat memindai alamat yang dikodekan QR code dengan mengklik ikon yang terletak di pojok kanan atas layar.

![TAPSIGNER NUNCHUK](assets/notext/42.webp)

Klik pada tombol "*Create Transaction*".

![TAPSIGNER NUNCHUK](assets/notext/43.webp)

Verifikasi detail transaksimu, kemudian klik pada tombol "*Sign*" di sebelah Tapsignermu.

![TAPSIGNER NUNCHUK](assets/notext/44.webp)

Masukkan PIN untuk membukanya.

![TAPSIGNER NUNCHUK](assets/notext/45.webp)

Kemudian letakkan Tapsigner di belakang smartphonemu.
![TAPSIGNER NUNCHUK](assets/notext/46.webp)
Transaksi Anda sekarang telah ditandatangani. Periksa sekali lagi bahwa semuanya sudah benar, kemudian klik pada "*Broadcast Transaction*" untuk menyiarkan transaksi tersebut di jaringan Bitcoin.

![TAPSIGNER NUNCHUK](assets/notext/47.webp)

Sekarang transaksimu sedang menunggu konfirmasi.

![TAPSIGNER NUNCHUK](assets/notext/48.webp)

## Bagaimana cara memulihkan dompet jika Tapsigner hilang?

Jika kamu kehilangan Tapsigner, kamu bisa memulihkan dompetmu menggunakan kode yang tercetak di bagian belakang kartu. Karena itu, penting untuk menyimpan kode ini terpisah dari Tapsigner, sebab jika kartunya hilang, kamu juga akan kehilangan akses ke kode tersebut. Kamu juga memerlukan cadangan terenkripsi dari dompetmu.

Untuk proses pemulihan, kita akan menggunakan aplikasi Nunchuk. Namun, ingat bahwa ini berarti dana kamu akan sementara disimpan di dompet panas (hot wallet). Jika Tapsigner kamu menyimpan jumlah yang cukup besar, sebaiknya lakukan proses pemulihan yang sama menggunakan Coldcard baru.

Buka aplikasi Nunchuk dan klik pada tombol "*+*" di sebelah tab "*Keys*".

![TAPSIGNER NUNCHUK](assets/notext/49.webp)

Pilih "*Add NFC key*".

![TAPSIGNER NUNCHUK](assets/notext/50.webp)

Pilih opsi "*Recover TAPSIGNER key from backup*".

![TAPSIGNER NUNCHUK](assets/notext/51.webp)

Kamu kemudian akan diarahkan ke penjelajah file perangkatmu. Temukan dan pilih file cadangan terenkripsi dari dompetmu. Biasanya, nama file ini dimulai dengan `backup...`.

![TAPSIGNER NUNCHUK](assets/notext/52.webp)

Masukkan kata sandi yang mendekripsi file cadangan. Kata sandi ini sesuai dengan yang awalnya dicatat di bagian belakang Tapsigner Anda.

![TAPSIGNER NUNCHUK](assets/notext/53.webp)
Kemudian pilih nama untuk dompet pemulihan Anda.
![TAPSIGNER NUNCHUK](assets/notext/54.webp)

Sekarang kamu telah mendapatkan kembali akses ke bitcoin milikmu. Dompet kamu sekarang dikelola sebagai dompet panas yang terlihat di tab "*Keys*" aplikasi Nunchuk. Selanjutnya, kamu perlu membuat set kunci kriptografi baru di bagian "*Wallets*" dengan mengasosiasikan kunci ini dengannya. Untuk melakukan ini, kamu dapat mengikuti langkah-langkah lagi di bagian "*How to create a wallet on a Tapsigner?*" dari tutorial ini.

![TAPSIGNER NUNCHUK](assets/notext/55.webp)

Jika kamu kehilangan Tapsigner, sangat disarankan untuk segera memindahkan bitcoin kamu ke dompet lain yang kamu miliki, idealnya yang dilindungi oleh dompet perangkat keras. Tapsigner yang hilang bisa saja jatuh ke tangan yang salah. Karena itu, penting untuk segera mengosongkan dompet yang baru kamu pulihkan dan berhenti menggunakannya.

Selamat, sekarang kamu sudah menguasai cara menggunakan Tapsigner! Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu mau memberikan jempol ke atas di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih banyak!
