---
name: Satscard
description: Mengatur dan menggunakan Satscard dengan Nunchuk
---
![cover](assets/cover.webp)

Bitcoin adalah sistem uang elektronik yang memungkinkan kita melakukan transaksi peer-to-peer. Namun, untuk memastikan sebuah transaksi tidak bisa diubah, dibutuhkan beberapa konfirmasi, biasanya 6, untuk mencegah kemungkinan pengeluaran ganda oleh pengirim. Waktu tunggu validasi ini kadang terasa kurang praktis, terutama saat kita menginginkan kefinalan instan seperti uang tunai fisik. Berbeda dengan uang tunai, di mana kepemilikan selembar uang berpindah secara langsung, transaksi Bitcoin memerlukan waktu tunggu sebelum benar-benar dianggap tidak dapat dibalik.

Di sinilah Satscard berperan. Solusi ini menawarkan cara untuk mentransfer bitcoin secara fisik dan instan, tanpa perlu melakukan transaksi on-chain. Satscard berfungsi sebagai kartu pembawa yang memungkinkan perpindahan kepemilikan bitcoin secara aman, sehingga menghadirkan pengalaman yang lebih mendekati uang tunai tradisional. Dalam tutorial ini, aku akan memperkenalkan kamu pada solusi ini.

## Apa itu Satscard?

Satscard dari Coinkite adalah penerus dari Opendime. Ini adalah kartu NFC yang memungkinkan transfer fisik bitcoin, mirip seperti uang kertas atau koin. Tidak seperti hardware wallet tradisional, Satscard adalah kartu pembawa, yang berarti kepemilikan fisik kartu sama dengan kepemilikan bitcoin yang diamankan oleh kunci privat yang tersimpan di dalamnya. Harganya berkisar antara $6.99 hingga $17.99 tergantung desain yang kamu pilih.

![SATSCARD](assets/notext/01.webp)

Chip Satscard dilengkapi dengan 10 slot, yang memungkinkannya menyimpan bitcoin hingga 10 kali di 10 alamat berbeda. Setiap slot bekerja secara independen dan secara teori hanya digunakan satu kali untuk mengunci bitcoin di dalamnya. Untuk membelanjakan bitcoin, kamu cukup membuka segel slot menggunakan aplikasi yang kompatibel, seperti Nunchuk, dengan memasukkan kode verifikasi 6 digit yang tercetak di bagian belakang Satscard.

Kartu ini memastikan bahwa kunci privat yang mengamankan bitcoin di blockchain tidak bisa disimpan oleh pemilik sebelumnya setelah mereka secara fisik menyerahkan kartu tersebut. Penerima juga bisa memverifikasi keabsahan slot dan jumlah yang tersimpan di dalamnya saat proses pertukaran.

Sistem ini sangat cocok digunakan untuk membeli barang fisik dengan bitcoin, atau untuk memberikan bitcoin sebagai hadiah.

## Bagaimana cara membeli Satscard?

Satscard tersedia untuk dibeli [di situs resmi Coinkite](https://store.coinkite.com/store/category/satscard). Untuk membelinya di toko fisik, kamu juga dapat menemukan [daftar reseller bersertifikat](https://coinkite.com/resellers) di situs tersebut.
Kamu juga akan memerlukan telepon yang kompatibel dengan komunikasi NFC, atau perangkat USB untuk membaca kartu NFC pada frekuensi standar 13.56 MHz.
## Bagaimana cara memuat slot di Satscard?

Setelah kamu menerima Satscard kamu, langkah pertama adalah memeriksa kemasannya untuk memastikan tidak ada yang terbuka. Jika kemasan rusak, itu bisa menunjukkan bahwa kartu telah dikompromikan dan mungkin tidak asli.

Untuk mengelola Satscard, kita akan menggunakan aplikasi seluler **Nunchuk Wallet**. Pastikan smartphone kamu kompatibel dengan NFC, kemudian unduh Nunchuk dari [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073), atau langsung melalui file [`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases) nya.
Secara teori, kamu bisa langsung mengirim bitcoin ke alamat yang tercantum di bagian belakang Satscard tanpa menggunakan Nunchuk. Namun, aku menyarankan untuk tidak melakukannya, karena kita perlu memastikan terlebih dahulu bahwa alamat slot pertama memang berasal dari kunci privat yang tersimpan di Satscard dan bukan alamat palsu.

Jika kamu baru pertama kali menggunakan Nunchuk, aplikasi akan menawarkan opsi untuk membuat akun. Untuk kebutuhan tutorial ini, kamu tidak perlu membuat akun. Jadi, pilih "*Lanjutkan sebagai tamu*" untuk melanjutkan tanpa akun.

Kemudian klik pada "*Dompet tanpa bantuan*".

Selanjutnya, klik tombol "*Saya akan menjelajah sendiri*".

Setelah berada di layar utama Nunchuk, klik logo "*NFC*" di bagian atas layar.

Dekatkan Satscard ke bagian belakang ponsel untuk memindainya.

Nunchuk akan menampilkan alamat penerima yang sesuai dengan slot pertama Satscard kamu. Biasanya, alamat ini harus sama persis dengan yang tertulis di bagian belakang kartu. Salin alamat tersebut dan gunakan untuk mentransfer bitcoin yang ingin kamu kunci pada slot ini.

## Bagaimana cara memeriksa bitcoin pada slot?

Setelah transaksi terkonfirmasi, kamu bisa memeriksa saldo yang terkait dengan slot Satscard dengan memindainya menggunakan Nunchuk. Dengan begitu, saat transaksi berlangsung, penerima bitcoin dapat langsung memverifikasi melalui aplikasi Nunchuk mereka bahwa kartu tersebut memang berisi bitcoin sesuai jumlah yang disepakati.

Jika pihak lain tidak memiliki aplikasi Nunchuk, mereka tetap bisa memverifikasi keabsahan Satscard. Cukup aktifkan NFC di smartphone mereka lalu tempelkan Satscard ke bagian belakang perangkat. Tindakan ini akan otomatis membuka situs web Satscard di browser, sehingga siapa pun bisa memeriksa keaslian kartu sekaligus jumlah bitcoin yang terkait dengannya.


## Bagaimana cara menarik bitcoin dari slot?

Sekarang setelah slot pertama Satscard terisi sejumlah bitcoin, kamu bisa menyerahkan kartu tersebut kepada penerima pembayaran.

Kalau kamu adalah penerimanya, kamu perlu menginstal Nunchuk. Setelah masuk ke aplikasi, klik logo "*NFC*" di bagian atas layar.

Tempelkan Satscard ke bagian belakang ponsel.

Nunchuk akan menampilkan jumlah bitcoin yang diamankan di alamat tersebut.

Untuk membuka kunci privat dan memindahkan bitcoin ke alamat milikmu, klik tombol "*Buka kunci dan sapu saldo*".

Opsi "*Sapu ke dompet*" memungkinkan kamu langsung mengirim bitcoin ke dompet yang sudah ada di aplikasi Nunchuk. Untuk mentransfer dana ke alamat penerima lain, pilih "*Tarik ke alamat*". Masukkan alamat tujuan tempat kamu ingin mengirim bitcoin yang diamankan oleh Satscard. Pastikan alamat yang dimasukkan sudah benar, karena ini adalah satu-satunya kesempatan untuk memverifikasinya, lalu klik tombol "*Create transaction*".

Masukkan kode PIN Satscard kamu. Kode 6 digit ini tercetak di bagian belakang kartu fisik.

Tetap tempelkan Satscard di belakang smartphone saat menandatangani transaksi menggunakan kunci privat yang tersimpan di kartu NFC.

Transaksimu sekarang sudah ditandatangani dan disiarkan ke jaringan Bitcoin, yang berarti slot yang digunakan di Satscard kini kosong.

## Bagaimana cara menggunakan kembali Satscard?

Berbeda dengan solusi sekali pakai seperti Opendime, Satscard dilengkapi chip dengan 10 slot independen, sehingga memungkinkan hingga 10 kali penggunaan dalam satu kartu. Slot pertama, yang sudah dikonfigurasi di pabrik oleh Coinkite, sesuai dengan alamat penerima yang tertulis di bagian belakang Satscard kamu.

Untuk mengaktifkan 9 slot lainnya, kamu perlu menghasilkan pasangan kunci dan alamat melalui aplikasi Nunchuk. Di halaman utama aplikasi, klik logo "*NFC*" di bagian atas layar.

Tempelkan Satscard ke bagian belakang ponsel.

Nunchuk akan menampilkan bahwa tidak ada slot aktif di kartu, yang wajar karena slot pertama sudah digunakan dan slot kedua belum dibuat. Untuk melihat slot yang sebelumnya digunakan, klik "*View unsealed slots*". Sangat disarankan untuk tidak menggunakan kembali slot tersebut, karena ini akan menyebabkan address reuse yang merugikan privasi on-chain kamu. Karena itu, kita akan menyiapkan slot baru dengan mengklik tombol "*Yes*".

Sekarang kamu perlu memilih bagaimana cara menghasilkan master chain code.

Slot di Satscard mengikuti standar BIP32, artinya derivasi kunci kriptografis yang mengamankan bitcoin tidak bergantung pada seedphrase seperti pada wallet BIP39, melainkan langsung pada master private key dan master chain code. Kedua elemen ini digunakan sebagai input dalam fungsi HMAC-SHA512 untuk menghasilkan pasangan child key. Setiap slot memiliki master key dan master chain code masing-masing. Hanya ada satu tingkat derivasi untuk setiap slot.

Pasangan kunci untuk slot pertama sudah dihasilkan sebelumnya oleh Coinkite. Karena itu, kamu bisa langsung mengaksesnya melalui Nunchuk, dan alamat penerimanya tercetak di bagian belakang kartu NFC. Untuk slot lainnya, kamu sendiri yang bertanggung jawab menghasilkan kuncinya.

Master private key untuk setiap slot dihasilkan langsung oleh Satscard, sedangkan master chain code harus disediakan dari luar. Untuk chain code slot baru, kamu punya dua opsi: biarkan Nunchuk membuatnya secara otomatis dengan memilih "*Automatic*", atau buat sendiri dengan memilih "*Advanced*" lalu memasukkannya di kolom yang tersedia. Agar efektif, chain code harus dibuat seacak mungkin.

Masukkan PIN 6 digit yang tertera di bagian belakang Satscard.

![SATSCARD](assets/notext/26.webp)

Letakkan Satscard Anda di bagian belakang ponsel Anda.

![SATSCARD](assets/notext/27.webp)

Slot baru berhasil dikonfigurasi. Kamu sekarang bisa melihat alamat penerima untuk menyetorkan bitcoin. Untuk melanjutkan proses pengisian, ikuti instruksi pada bagian "*Cara mengisi slot pada Satscard?*" di tutorial ini. Kamu bisa mengulangi proses ini hingga 10 kali pada setiap Satscard.

Selamat, kamu sekarang sudah menguasai cara menggunakan Satscard! Jika kamu merasa tutorial ini bermanfaat, aku akan sangat menghargai jika kamu meninggalkan jempol ke atas di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosial kamu. Terima kasih banyak!
