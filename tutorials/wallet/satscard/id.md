---
name: Satscard
description: Cara Mengatur dan menggunakan Satscard dengan Nunchuk
---
![cover](assets/cover.webp)

Bitcoin adalah sistem uang elektronik yang memungkinkan kita melakukan transaksi peer-to-peer. Namun, supaya sebuah transaksi benar-benar nggak bisa diubah, dibutuhkan beberapa konfirmasi (biasanya 6) untuk mencegah kemungkinan pengeluaran ganda oleh pengirim. Keterlambatan validasi ini kadang bisa bikin nggak nyaman, terutama kalau kefinalan instan kayak uang tunai fisik yang diinginkan. Beda sama uang tunai, di mana kepemilikan selembar uang kertas langsung berpindah, transaksi Bitcoin butuh waktu tunggu sebelum dianggap benar-benar nggak bisa dibalik.

Di sinilah Satscard berperan. Kartu ini nawarin cara untuk ngirim bitcoin secara fisik dan instan, tanpa harus bikin transaksi on-chain. Satscard berfungsi sebagai kartu pemegang yang bisa mindahin kepemilikan bitcoin dengan aman, jadi pengalamannya lebih mirip sama uang tunai tradisional. Dalam tutorial ini, aku bakal ngenalin kamu sama solusi ini.

## Apa itu Satscard?

Satscard dari Coinkite adalah penerus Opendime. Ini adalah kartu NFC yang bisa ngirim bitcoin secara fisik, mirip kayak uang kertas atau koin. Beda dari dompet hardware tradisional, Satscard adalah kartu pemegang, yang artinya kepemilikan fisik kartu sama dengan kepemilikan bitcoin yang diamankan dengan kunci di dalamnya. Harganya ada di kisaran $6,99 sampai $17,99 tergantung desain yang kamu pilih.

![SATSCARD](assets/notext/01.webp)

Chip Satscard dilengkapi dengan 10 slot, yang bikin kamu bisa nyimpen bitcoin sampai 10 kali di 10 alamat berbeda. Setiap slot jalan secara independen dan secara teori harus dipakai sekali aja buat ngunci bitcoin di dalamnya. Buat ngabisin bitcoin, kamu cukup buka segel slot pakai aplikasi yang kompatibel, misalnya Nunchuk, dengan masukin kode verifikasi 6 digit yang tercetak di bagian belakang Satscard.

Kartu ini ngejamin kalau kunci privat yang ngamanin bitcoin di blockchain nggak bisa lagi dipegang pemilik sebelumnya setelah kartu itu berpindah tangan secara fisik. Penerima juga bisa langsung ngecek validitas slot dan jumlah yang tersimpan di dalamnya waktu pertukaran berlangsung.

Sistem ini sangat berguna buat belanja barang fisik pakai bitcoin, atau buat ngasih bitcoin sebagai hadiah.

## Bagaimana cara membeli Satscard?

Satscard bisa kamu beli [di situs resmi Coinkite](https://store.coinkite.com/store/category/satscard). Untuk belinya di toko fisik, kamu juga bisa nemuin [daftar reseller bersertifikat](https://coinkite.com/resellers) di situs tersebut.
Kamu juga bakal butuh ponsel yang kompatibel dengan komunikasi NFC, atau perangkat USB buat baca kartu NFC di frekuensi standar 13,56 MHz.

## Bagaimana cara memuat slot di Satscard?

Setelah kamu nerima Satscard, langkah pertama adalah ngecek kemasannya buat pastiin nggak ada yang kebuka. Kalau kemasannya rusak, itu bisa jadi tanda kalau kartu udah dikompromikan dan mungkin nggak asli.

Nah, Untuk mengelola Satscard, kita bakal pakai aplikasi seluler **Nunchuk Wallet.** Pastikan smartphone kamu kompatibel dengan NFC, lalu unduh Nunchuk dari [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073), atau bisa langsung melalui file [`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases) nya.
Secara teori, kamu bisa langsung ngirim bitcoin ke alamat yang tertera di bagian belakang Satscard tanpa pake Nunchuk. Tapi aku nyaranin jangan dulu, soalnya kita bakal verifikasi dulu kalau alamat slot pertama beneran berasal dari kunci privat yang disimpen di Satscard dan bukan alamat palsu.

Kalau kamu baru pertama kali pake Nunchuk, aplikasinya bakal nawarin buat bikin akun. Buat keperluan tutorial ini, kamu nggak perlu bikin akun. Jadi, pilih "*Lanjutkan sebagai tamu*" biar bisa lanjut tanpa akun.

Kemudian klik "*Dompet tanpa bantuan*".

Terus, klik tombol "*Saya akan menjelajah sendiri*".

Setelah berada di layar utama Nunchuk, klik pada logo "*NFC*" di bagian atas layar.

Tempelin Satscard ke bagian belakang ponsel kamu buat dipindai.

Nunchuk bakal nampilin alamat penerima yang sesuai sama slot pertama Satscard kamu. Biasanya, alamat ini harus sama persis dengan yang ditulis manual di bagian belakang kartu. Salin alamat itu lalu pakai buat transfer bitcoin yang mau kamu kunci di slot ini.

## Bagaimana cara memeriksa bitcoin pada slot?

Setelah transaksi terkonfirmasi, kamu bisa ngecek saldo yang terhubung ke slot Satscard dengan memindainya pakai Nunchuk. Dengan begitu, waktu transaksi berlangsung, penerima bitcoin bisa langsung verifikasi lewat aplikasi Nunchuk mereka kalau kartu itu beneran nyimpen bitcoin yang jadi hak mereka.

Kalau pihak lain nggak punya aplikasi Nunchuk, mereka tetap bisa verifikasi keaslian Satscard. Cukup aktifin NFC di smartphone mereka lalu tempelin Satscard ke bagian belakang perangkat. Browser bakal otomatis kebuka ke situs Satscard, di mana mereka bisa ngecek keaslian kartu sekaligus jumlah bitcoin yang terkait.

## Bagaimana cara menarik Bitcoin dari slot?

Sekarang setelah slot pertama Satscard terisi dengan sejumlah bitcoin, kamu bisa langsung kasih kartu itu ke penerima pembayaran.

Kalau kamu jadi penerima, kamu perlu instal Nunchuk. Setelah masuk ke aplikasi, klik logo "*NFC*" di bagian atas layar.

Tempelin Satscard ke bagian belakang ponsel kamu.

Nunchuk bakal nampilin jumlah yang diamankan di alamat itu.

Buat buka kunci privat dan mindahin bitcoin ke alamat yang kamu punya, klik tombol "*Buka kunci dan sapu saldo*".

Opsi "*Sapu ke dompet*" bikin kamu bisa langsung ngirim bitcoin ke dompet yang udah ada di aplikasi Nunchuk. Kalau mau transfer dana ke alamat penerima lain, pilih "*Tarik ke alamat*".
Masukin alamat penerima tempat kamu mau ngirim bitcoin yang diamankan Satscard. Pastikan alamat yang kamu masukin udah bener (ini satu-satunya waktu kamu bisa verifikasi), lalu klik tombol "*Create transaction*".

Masukin kode PIN dari Satscard kamu. Kode 6 digit ini tercetak di bagian belakang kartu fisik.

Tempelin Satscard di belakang smartphone kamu waktu menandatangani transaksi dengan kunci privat yang tersimpen di kartu NFC.

Sekarang transaksi kamu udah ditandatangani dan disiarkan ke jaringan Bitcoin, yang berarti slot yang tadi dipakai di Satscard kamu sekarang kosong.

## Bagaimana cara menggunakan kembali Satscard?

Beda dengan solusi sekali pakai kayak Opendime, Satscard dilengkapi chip dengan 10 slot independen, jadi bisa dipakai sampai 10 kali dalam satu kartu. Slot pertama, yang udah dikonfigurasi pabrik oleh Coinkite, sesuai sama alamat penerima yang tertulis di bagian belakang Satscard kamu.

Buat ngaktifin 9 slot lainnya, kamu perlu bikin pasangan kunci dan alamat lewat aplikasi Nunchuk. Dari halaman utama aplikasi, klik logo "*NFC*" di bagian atas layar.

Tempelin Satscard di belakang ponsel kamu.

Nunchuk bakal nampilin kalau belum ada slot aktif di kartu, ini wajar karena slot pertama udah dipakai dan slot kedua belum dibuat. Buat lihat slot yang sebelumnya udah dipakai, klik "*View unsealed slots*". Sangat disarankan untuk nggak pake ulang slot itu, soalnya bisa bikin alamat kepake dua kali dan merugikan privasi on-chain kamu. Jadi, kita bakal siapin slot baru dengan klik tombol "*Yes*".

Sekarang kamu perlu pilih gimana cara bikin kode rantai induk kamu.

Slot di Satscard ngikutin standar BIP32, artinya turunan kunci kriptografis yang ngamanin bitcoin nggak bergantung pada frasa mnemonik kayak di dompet BIP39, tapi langsung pada kunci privat induk dan kode rantai induk. Dua elemen ini dipake sebagai input dalam fungsi HMAC-SHA512 buat bikin pasangan kunci anak. Setiap slot punya kunci induk dan kode rantai induknya masing-masing. Cuma ada satu tingkat derivasi buat tiap slot.

Pasangan kunci untuk slot pertama udah dibuat sebelumnya sama Coinkite. Itu kenapa kamu bisa langsung akses lewat Nunchuk, dan kenapa alamat penerimanya tercetak di bagian belakang kartu NFC. Tapi untuk slot-slot lainnya, kamu yang bertanggung jawab buat bikin kuncinya.

Kunci privat induk untuk setiap slot dibikin langsung sama Satscard, sedangkan kode rantai induknya harus kamu sediakan dari luar. Buat kode rantai slot baru, kamu punya dua pilihan: biarin Nunchuk bikin otomatis dengan pilih "*Automatic*", atau bikin sendiri dengan pilih "*Advanced*" lalu masukin di kolom yang disediakan. Supaya kode rantai ini efektif, harus seacak mungkin.

Terakhir, masukin PIN 6 digit yang tercetak di bagian belakang Satscard kamu.

![SATSCARD](assets/notext/26.webp)

Tempelin Satscard di bagian belakang ponsel kamu.

![SATSCARD](assets/notext/27.webp)

Sebuah slot baru berhasil dikonfigurasi. Sekarang kamu bisa lihat alamat penerima buat nyetor bitcoin. Buat lanjut ngisi, ikuti instruksi di bagian "*Cara mengisi slot pada Satscard?*" dari tutorial ini.
Kamu bisa ngulang proses ini sampai 10 kali di tiap Satscard.

Selamat, sekarang kamu udah menguasai cara pake Satscard! Kalau kamu ngerasa tutorial ini bermanfaat, aku bakal sangat senang kalau kamu mau kasih jempol ke atas di bawah ini. Jangan ragu juga buat bagiin artikel ini ke jaringan sosial kamu. Makasih banyak!
