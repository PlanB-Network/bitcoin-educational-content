---
name: Tapsigner
description: Mengatur dan menggunakan Tapsigner dengan Nunchuk
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang didedikasikan untuk pengelolaan dan keamanan kunci privat dari dompet Bitcoin. Berbeda dengan dompet perangkat lunak (atau dompet panas) yang dipasang pada mesin umum yang sering terhubung ke Internet, dompet perangkat keras memungkinkan isolasi fisik dari kunci privat, mengurangi risiko peretasan dan pencurian.

Tujuan utama dari dompet perangkat keras adalah untuk meminimalkan fungsionalitas perangkat untuk mengurangi permukaan serangan. Permukaan serangan yang lebih kecil juga berarti lebih sedikit vektor serangan potensial, yaitu, lebih sedikit titik lemah dalam sistem yang dapat dieksploitasi oleh penyerang untuk mengakses bitcoin.

Disarankan untuk menggunakan dompet perangkat keras untuk mengamankan bitcoin Anda, terutama jika Anda memiliki jumlah yang signifikan, baik dalam nilai absolut maupun sebagai proporsi dari total aset Anda.

Dompet perangkat keras digunakan bersama dengan perangkat lunak manajemen dompet pada komputer atau smartphone. Perangkat lunak ini mengelola pembuatan transaksi, tetapi tanda tangan kriptografis yang diperlukan untuk memvalidasi transaksi ini dilakukan sepenuhnya di dalam dompet perangkat keras. Ini berarti bahwa kunci privat tidak pernah terpapar ke lingkungan yang berpotensi rentan.

Dompet perangkat keras menawarkan perlindungan ganda bagi pengguna: di satu sisi, mereka mengamankan bitcoin Anda dari serangan jarak jauh dengan menjaga kunci privat offline, dan di sisi lain, mereka umumnya menawarkan resistensi fisik yang lebih baik terhadap upaya untuk mengekstrak kunci. Dan tepat pada 2 kriteria keamanan ini, seseorang dapat menilai dan meranking berbagai model yang tersedia di pasar.

Dalam tutorial ini, saya mengusulkan untuk menemukan salah satu solusi ini: Tapsigner oleh Coinkite.

## Pengenalan ke Tapsigner

Tapsigner adalah dompet perangkat keras yang dirancang dalam bentuk kartu NFC oleh perusahaan Coinkite, yang juga dikenal karena memproduksi Coldcards.

![TAPSIGNER NUNCHUK](assets/notext/01.webp)

Tapsigner memungkinkan penyimpanan pasangan yang terdiri dari kunci privat induk dan kode rantai sesuai dengan BIP32, untuk menurunkan pohon kunci kriptografis. Kunci-kunci ini dapat digunakan untuk menandatangani transaksi dengan meletakkan Tapsigner di dekat telepon atau pembaca kartu NFC.
Kartu NFC ini dijual seharga $19.99, yang sangat terjangkau dibandingkan dengan dompet perangkat keras lain yang tersedia di pasar. Namun, karena formatnya, Tapsigner tidak menawarkan sebanyak opsi seperti perangkat lain. Jelas tidak ada baterai, tidak ada kamera, juga tidak ada pembaca kartu micro SD, karena ini adalah kartu. Menurut saya, kekurangan terbesar adalah tidak adanya layar pada dompet perangkat keras, yang membuatnya lebih rentan terhadap beberapa jenis serangan jarak jauh. Memang, ini memaksa pengguna untuk menandatangani secara buta dan mempercayai apa yang mereka lihat di layar komputer mereka.

Meskipun memiliki keterbatasan, Tapsigner bisa menarik karena harganya yang murah. Dompet ini dapat digunakan khususnya untuk meningkatkan keamanan dompet pengeluaran selain dompet tabungan yang dilindungi oleh dompet perangkat keras yang dilengkapi dengan layar. Ini juga mewakili solusi yang baik bagi mereka yang memiliki jumlah bitcoin yang kecil dan tidak ingin menginvestasikan seratus euro dalam perangkat yang lebih canggih. Selain itu, penggunaan Tapsigner dalam konfigurasi multisig, atau potensial dalam sistem dompet dengan timelock di masa depan, dapat menawarkan manfaat yang menarik.

## Bagaimana cara membeli Tapsigner?

Tapsigner tersedia untuk dibeli [di situs resmi Coinkite](https://store.coinkite.com/store/category/tapsigner). Untuk membelinya di toko fisik, Anda juga dapat menemukan [daftar reseller bersertifikat](https://coinkite.com/resellers) di situs tersebut.
Anda juga akan memerlukan telepon yang kompatibel dengan komunikasi NFC, atau perangkat USB untuk membaca kartu NFC pada frekuensi standar 13,56 MHz.
## Bagaimana cara menginisialisasi Tapsigner dengan Nunchuk?

Setelah Anda menerima Tapsigner Anda, langkah pertama adalah memeriksa kemasannya untuk memastikan belum dibuka. Jika paketnya rusak, itu bisa menunjukkan bahwa kartu telah dikompromikan dan mungkin tidak asli. CoinKite akan mengirimkan Tapsigner Anda dengan sebuah kotak yang memblokir gelombang radio. Pastikan itu ada dalam paket Anda.

![TAPSIGNER NUNCHUK](assets/notext/02.webp)

Untuk mengelola dompet, kita akan menggunakan aplikasi seluler **Nunchuk Wallet**. Pastikan smartphone Anda kompatibel dengan NFC, kemudian unduh Nunchuk dari [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) atau langsung melalui file [`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases) nya.

![TAPSIGNER NUNCHUK](assets/notext/03.webp)
Jika Anda menggunakan Nunchuk untuk pertama kalinya, aplikasi akan meminta Anda untuk membuat akun. Untuk tujuan tutorial ini, tidak perlu membuat satu. Jadi, pilih "*Lanjutkan sebagai tamu*" untuk melanjutkan tanpa akun.
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

Anda sekarang perlu memilih bagaimana Anda menghasilkan kode rantai induk Anda.

Tapsigner menggunakan standar BIP32. Ini berarti bahwa derivasi kunci kriptografis Anda yang mengamankan bitcoin Anda tidak bergantung pada frasa mnemonik seperti dompet BIP39, tetapi langsung pada kunci pribadi induk dan kode rantai induk. 2 elemen ini dilewatkan melalui fungsi HMAC untuk secara deterministik dan hierarkis menurunkan sisa dompet Anda.

Kunci pribadi induk dihasilkan langsung oleh TRNG (*True Random Number Generator*) yang terintegrasi ke dalam Tapsigner Anda. Kode rantai induk, di sisi lain, harus disediakan dari luar. Pada langkah ini, Anda memiliki pilihan: biarkan Nunchuk menghasilkannya secara otomatis dengan mengklik pada "*Otomatis*", atau menghasilkannya sendiri dengan memilih "*Lanjutan*" dan memasukkannya ke dalam kolom yang disediakan.

![TAPSIGNER NUNCHUK](assets/notext/12.webp)
Selanjutnya, Anda perlu memilih kode PIN. Di area "*Starting PIN*", masukkan kode PIN yang tertulis di bagian belakang Tapsigner Anda.
![TAPSIGNER NUNCHUK](assets/notext/13.webp)

Pilih kode PIN untuk mengamankan akses fisik ke Tapsigner Anda. Kode PIN ini tidak berperan dalam proses pemulihan dompet. Fungsinya hanya untuk membuka kunci Tapsigner Anda untuk menandatangani transaksi. Pastikan untuk menyimpan kode PIN ini agar tidak lupa. Klik pada "*Continue*" untuk melanjutkan.

![TAPSIGNER NUNCHUK](assets/notext/14.webp)
Letakkan kartu Tapsigner Anda di belakang ponsel Anda sekarang untuk menginisialisasinya.
![TAPSIGNER NUNCHUK](assets/notext/15.webp)

Nunchuk kemudian akan menghasilkan file pemulihan untuk dompet Anda, yang memungkinkan Anda untuk mendapatkan kembali akses ke bitcoin Anda jika Anda kehilangan kartu NFC Anda. File ini dienkripsi dengan kode cadangan yang tertulis di belakang Tapsigner Anda. Untuk memulihkan bitcoin Anda, Anda akan sangat memerlukan file ini serta kode untuk mendekripsinya. Oleh karena itu, penting untuk membuat salinan kode ini di kertas, karena jika Anda kehilangan kartu NFC Anda, akses ke kode ini juga akan hilang, karena saat ini hanya tertulis di kartu. Pastikan juga untuk membuat beberapa cadangan file pemulihan terenkripsi Anda.

![TAPSIGNER NUNCHUK](assets/notext/16.webp)

Pilih nama untuk dompet Anda.

![TAPSIGNER NUNCHUK](assets/notext/17.webp)

Dasar dompet Anda sekarang telah disiapkan. Untuk memverifikasi keaslian Tapsigner Anda, kapan saja, Anda dapat mengklik tombol "*Run health check*".

![TAPSIGNER NUNCHUK](assets/notext/18.webp)

Masukkan PIN Anda.

![TAPSIGNER NUNCHUK](assets/notext/19.webp)

Kemudian letakkan kartu Anda di belakang ponsel Anda.

![TAPSIGNER NUNCHUK](assets/notext/20.webp)

## Bagaimana cara membuat dompet di Tapsigner?

Kembali ke beranda Nunchuk, Anda dapat melihat bahwa Tapsigner Anda terdaftar dalam perangkat penandatangan yang tersedia.

![TAPSIGNER NUNCHUK](assets/notext/21.webp)

Anda sekarang perlu menghasilkan kunci untuk dompet Bitcoin Anda. Untuk melakukan ini, klik pada tombol "*+*" di sebelah kanan tab "*Wallets*".

![TAPSIGNER NUNCHUK](assets/notext/22.webp)

Klik pada "*Create new wallet*".

![TAPSIGNER NUNCHUK](assets/notext/23.webp)

Kemudian pilih opsi "*Create a new wallet using existing keys*".

![TAPSIGNER NUNCHUK](assets/notext/24.webp)

Pilih nama untuk dompet Anda kemudian klik pada "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/25.webp)

Pilih Tapsigner Anda sebagai perangkat penandatangan untuk set kunci baru ini, kemudian klik pada "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/26.webp)

Jika semuanya sesuai dengan keinginan Anda, konfirmasi pembuatan.

![TAPSIGNER NUNCHUK](assets/notext/27.webp)
Anda kemudian dapat menyimpan file konfigurasi dompet Anda. File ini secara eksklusif berisi kunci publik Anda, yang berarti bahkan jika seseorang mengaksesnya, mereka tidak dapat mencuri bitcoin Anda. Namun, mereka dapat mengikuti semua transaksi Anda. Oleh karena itu, file ini hanya menimbulkan risiko terhadap privasi Anda. Dalam beberapa kasus, file ini mungkin sangat penting untuk memulihkan dompet Anda.
![TAPSIGNER NUNCHUK](assets/notext/28.webp)

Dan begitulah, dompet Anda berhasil dibuat!

![TAPSIGNER NUNCHUK](assets/notext/29.webp)

Ketika Anda tidak menggunakan Tapsigner Anda, ingatlah untuk menyimpannya dalam kotak yang disediakan oleh Coinkite, yang memblokir gelombang radio untuk melindungi dari pembacaan yang tidak sah.

## Bagaimana cara menerima bitcoin di Tapsigner?

Untuk menerima bitcoin, klik pada dompet Anda.

![TAPSIGNER NUNCHUK](assets/notext/30.webp)

Kemudian gunakan alamat yang dihasilkan untuk menerima bitcoin. Jika Anda sebelumnya telah menerima bitcoin di dompet ini, Anda perlu mengklik tombol "*Receive*" untuk menghasilkan alamat penerimaan kosong baru.

![TAPSIGNER NUNCHUK](assets/notext/31.webp)

Setelah transaksi pengirim disiarkan, Anda akan melihatnya muncul di dompet Anda.

![TAPSIGNER NUNCHUK](assets/notext/32.webp)

Klik pada "*View coins*".

![TAPSIGNER NUNCHUK](assets/notext/33.webp)

Pilih UTXO baru Anda.

![TAPSIGNER NUNCHUK](assets/notext/34.webp)

Klik pada "*+*" di sebelah "*Tags*" untuk menambahkan label pada UTXO Anda. Ini adalah praktik yang baik, karena membantu Anda mengingat asal usul koin Anda dan mengoptimalkan privasi Anda untuk pengeluaran di masa depan.

![TAPSIGNER NUNCHUK](assets/notext/35.webp)

Pilih tag yang ada atau buat yang baru, kemudian klik pada "*Save*". Anda juga memiliki opsi untuk membuat "*collections*" untuk mengorganisir koin Anda secara lebih terstruktur.

![TAPSIGNER NUNCHUK](assets/notext/36.webp)

## Bagaimana cara mengirim bitcoin dengan Tapsigner?

Sekarang setelah Anda memiliki bitcoin di dompet Anda, Anda juga dapat mengirimkannya. Untuk melakukan ini, klik pada dompet pilihan Anda.

![TAPSIGNER NUNCHUK](assets/notext/37.webp)

Klik pada tombol "*Send*".

![TAPSIGNER NUNCHUK](assets/notext/38.webp)

Pilih jumlah yang akan dikirim, kemudian klik pada "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/39.webp)

Tambahkan "*note*" pada transaksi Anda di masa depan untuk mengingat tujuannya.

![TAPSIGNER NUNCHUK](assets/notext/40.webp)
Selanjutnya, masukkan secara manual alamat penerima di bidang yang ditentukan.
![TAPSIGNER NUNCHUK](assets/notext/41.webp)

Anda juga dapat memindai alamat yang dikodekan QR code dengan mengklik ikon yang terletak di pojok kanan atas layar.

![TAPSIGNER NUNCHUK](assets/notext/42.webp)

Klik pada tombol "*Create Transaction*".

![TAPSIGNER NUNCHUK](assets/notext/43.webp)

Verifikasi detail transaksi Anda, kemudian klik pada tombol "*Sign*" di sebelah Tapsigner Anda.

![TAPSIGNER NUNCHUK](assets/notext/44.webp)

Masukkan PIN Anda untuk membukanya.

![TAPSIGNER NUNCHUK](assets/notext/45.webp)

Kemudian letakkan Tapsigner di belakang smartphone Anda.
![TAPSIGNER NUNCHUK](assets/notext/46.webp)
Transaksi Anda sekarang telah ditandatangani. Periksa sekali lagi bahwa semuanya sudah benar, kemudian klik pada "*Broadcast Transaction*" untuk menyiarkan transaksi tersebut di jaringan Bitcoin.

![TAPSIGNER NUNCHUK](assets/notext/47.webp)

Transaksi Anda sekarang sedang menunggu konfirmasi.

![TAPSIGNER NUNCHUK](assets/notext/48.webp)

## Bagaimana cara memulihkan dompet jika Tapsigner hilang?

Jika Anda kehilangan Tapsigner Anda, Anda dapat memulihkan dompet Anda menggunakan kode yang tercatat di bagian belakang kartu. Oleh karena itu, penting untuk menyimpan kode ini secara terpisah dari Tapsigner, karena jika kartu hilang, akses ke kode ini juga akan hilang. Anda juga akan memerlukan cadangan terenkripsi dari dompet.

Untuk pemulihan, kami akan menggunakan aplikasi Nunchuk, tetapi ingat bahwa ini berarti sementara mengamankan dana Anda dalam dompet panas (hot wallet). Jika Tapsigner Anda mengamankan jumlah yang signifikan, pertimbangkan untuk mengikuti proses pemulihan yang sama dengan Coldcard baru.

Buka aplikasi Nunchuk dan klik pada tombol "*+*" di sebelah tab "*Keys*".

![TAPSIGNER NUNCHUK](assets/notext/49.webp)

Pilih "*Add NFC key*".

![TAPSIGNER NUNCHUK](assets/notext/50.webp)

Pilih opsi "*Recover TAPSIGNER key from backup*".

![TAPSIGNER NUNCHUK](assets/notext/51.webp)

Anda kemudian akan diarahkan ke penjelajah file perangkat Anda. Temukan dan pilih file cadangan terenkripsi dari dompet Anda. Biasanya, nama file ini dimulai dengan `backup...`.

![TAPSIGNER NUNCHUK](assets/notext/52.webp)

Masukkan kata sandi yang mendekripsi file cadangan. Kata sandi ini sesuai dengan yang awalnya dicatat di bagian belakang Tapsigner Anda.

![TAPSIGNER NUNCHUK](assets/notext/53.webp)
Kemudian pilih nama untuk dompet pemulihan Anda.
![TAPSIGNER NUNCHUK](assets/notext/54.webp)

Anda sekarang telah mendapatkan kembali akses ke bitcoin Anda. Dompet Anda sekarang dikelola sebagai dompet panas yang terlihat di tab "*Keys*" aplikasi Nunchuk. Selanjutnya, Anda perlu membuat set kunci kriptografi baru di bagian "*Wallets*" dengan mengasosiasikan kunci ini dengannya. Untuk melakukan ini, Anda dapat mengikuti langkah-langkah lagi di bagian "*How to create a wallet on a Tapsigner?*" dari tutorial ini.

![TAPSIGNER NUNCHUK](assets/notext/55.webp)

Jika Anda kehilangan Tapsigner Anda, saya sangat menyarankan Anda untuk segera mentransfer bitcoin Anda ke dompet lain yang Anda miliki, idealnya dilindungi oleh dompet perangkat keras (hardware wallet). Memang, Tapsigner yang Anda hilangkan berpotensi berada di tangan yang salah. Oleh karena itu, penting untuk mengosongkan dompet yang baru saja Anda pulihkan dan berhenti menggunakannya.

Selamat, Anda sekarang sudah menguasai penggunaan Tapsigner! Jika Anda merasa tutorial ini bermanfaat, saya akan sangat menghargai jika Anda bisa meninggalkan jempol ke atas di bawah ini. Jangan ragu untuk membagikan artikel ini di jaringan sosial Anda. Terima kasih banyak!