---
name: Blockstream Green - 2FA
description: Menyiapkan multisig 2/2 di Dompet Green
---
![cover](assets/cover.webp)

___

***Catatan:** Mulai Mei 2025, tidak akan lagi memungkinkan untuk mengaktifkan akun baru yang dilindungi oleh autentikasi dua faktor (2FA). Fitur ini hanya tersedia untuk pengguna yang sebelumnya sudah mengaktifkan jenis akun ini.*

___

Dompet perangkat lunak adalah aplikasi yang dipasang di komputer, smartphone, atau perangkat lain yang terhubung ke Internet, yang memungkinkan kamu mengelola dan mengamankan kunci dompet Bitcoin. Berbeda dengan dompet perangkat keras yang mengisolasi private key, dompet "panas" beroperasi di lingkungan yang berisiko terkena serangan siber, sehingga meningkatkan kemungkinan pembajakan dan pencurian.

Dompet perangkat lunak sebaiknya digunakan untuk mengelola jumlah bitcoin yang wajar, terutama untuk transaksi sehari-hari. Dompet ini juga menarik bagi pengguna dengan aset bitcoin terbatas, di mana investasi pada dompet perangkat keras mungkin terasa tidak proporsional. Namun, karena selalu terhubung ke Internet, dompet perangkat lunak kurang aman untuk menyimpan dana jangka panjang atau jumlah besar. Untuk tujuan itu, pilihan terbaik adalah menggunakan dompet perangkat keras.

Dalam tutorial ini, aku akan menunjukkan bagaimana cara meningkatkan keamanan hot wallet menggunakan opsi "*2FA*" di Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)

## Memperkenalkan Blockstream Green

Blockstream Green adalah dompet perangkat lunak yang tersedia di ponsel dan desktop. Sebelumnya dikenal sebagai *Green Address*, dompet ini menjadi proyek Blockstream setelah diakuisisi pada tahun 2016.

Green merupakan aplikasi yang sangat mudah digunakan, sehingga menarik bagi pemula. Aplikasi ini menawarkan semua fitur penting dari dompet Bitcoin yang baik, termasuk RBF (*Replace-by-Fee*), opsi koneksi Tor, kemampuan untuk menghubungkan node milikmu sendiri, SPV (*Simple Payment Verification*), serta penandaan dan kontrol koin.

Blockstream Green juga mendukung jaringan Liquid, sebuah sidechain Bitcoin yang dikembangkan oleh Blockstream untuk transaksi cepat dan rahasia di luar blockchain utama. Dalam tutorial ini, fokus kita hanya pada Bitcoin, tapi aku juga sudah membuat tutorial lain untuk mempelajari cara menggunakan Liquid di Green:

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## opsi multisig 2/2 (2FA)

Di Green, kamu bisa membuat hot wallet klasik "*singlesig*". Tapi kamu juga memiliki opsi "*2FA multisig*", yang meningkatkan keamanan hot wallet tanpa merepotkan pengelolaan sehari-hari.

Jadi, kamu akan membuat dompet multisig 2/2, artinya setiap transaksi membutuhkan tanda tangan dari dua kunci. Kunci pertama berasal dari frasa mnemonik 12 atau 24 kata kamu dan diamankan secara lokal dengan PIN di ponsel. Kamu memiliki kendali penuh atas kunci ini. Kunci kedua dipegang oleh server Blockstream, dan untuk menandatangani transaksi diperlukan otentikasi melalui kode yang dikirim via email, SMS, panggilan telepon, atau, seperti yang akan kita lihat dalam tutorial ini, melalui aplikasi otentikasi (Authy, Google Authenticator, dll.).

Untuk menjaga otonomi jika terjadi kegagalan Blockstream (misalnya kebangkrutan atau kerusakan server yang menyimpan kunci kedua), ada mekanisme penguncian waktu pada multisig. Mekanisme ini mengubah multisig 2/2 menjadi multisig 1/2 setelah sekitar satu tahun (atau tepatnya 51.840 blok, nilai ini bisa dimodifikasi), sehingga dompet hanya membutuhkan kunci lokal untuk membelanjakan bitcoin. Jadi, jika kamu kehilangan akses ke server Blockstream atau otentikasi 2FA, kamu hanya perlu menunggu maksimal satu tahun untuk bisa menggunakan bitcoin kamu secara bebas tanpa tergantung pada Blockstream.


![GREEN 2FA MULTISIG](assets/fr/02.webp)

Metode ini secara signifikan meningkatkan keamanan hot wallet kamu, sekaligus memberi kendali penuh atas bitcoin dan memudahkan penggunaan sehari-hari. Namun, metode ini membutuhkan penyegaran timelock secara berkala untuk menjaga keamanan 2FA. Hitung mundur 360 hari dimulai sejak bitcoin diterima, di mana dana tetap dilindungi oleh 2FA. Jika setelah 360 hari kamu belum menggunakan dana tersebut untuk transaksi, bitcoin hanya akan dilindungi oleh kunci lokal, tanpa 2FA.

Kendala ini membuat opsi 2FA lebih cocok untuk portofolio pengeluaran, karena transaksi reguler secara otomatis memperbarui timelock. Untuk portofolio tabungan jangka panjang, hal ini bisa menjadi masalah, karena kamu harus melakukan transaksi sapuan setiap tahun sebelum timelock berakhir.

Kerugian lain dari metode ini adalah penggunaan skrip minoritas. Dari sudut pandang privasi, ini lebih rumit: sangat sedikit orang yang memakai skrip yang sama, sehingga pengamat luar lebih mudah mengidentifikasi sidik jari dompet kamu. Selain itu, skrip ini menimbulkan biaya transaksi lebih tinggi karena ukurannya lebih besar.

Jika kamu memilih untuk tidak menggunakan opsi 2FA dan hanya ingin membuat dompet "*singlesig*" di Green, aku mengundangmu untuk membaca tutorial lainnya:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Menginstal dan mengonfigurasi perangkat lunak Blockstream Green

Langkah pertama tentu saja mengunduh aplikasi Green. Buka toko aplikasi kamu:

- [Untuk Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Untuk Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN 2FA MULTISIG](assets/fr/03.webp)

Untuk pengguna Android, kamu juga dapat menginstal aplikasi melalui file `.apk` [tersedia di GitHub Blockstream](https://github.com/Blockstream/green_android/releases).

![GREEN 2FA MULTISIG](assets/fr/04.webp)

Luncurkan aplikasi, lalu centang kotak "Saya menerima ketentuan...".

![GREEN 2FA MULTISIG](assets/fr/05.webp)

Saat kamu membuka Green untuk pertama kali, layar beranda akan tampil tanpa portofolio yang dikonfigurasi. Nantinya, setelah kamu membuat atau mengimpor portofolio, portofolio tersebut akan muncul di antarmuka ini. Sebelum melanjutkan ke pembuatan portofolio, aku menyarankan kamu menyesuaikan pengaturan aplikasi agar sesuai dengan kebutuhan. Klik pada "Pengaturan aplikasi".

![GREEN 2FA MULTISIG](assets/fr/06.webp)

Opsi "*Privasi yang Ditingkatkan*", yang hanya tersedia di Android, meningkatkan privasi dengan menonaktifkan tangkapan layar dan menyembunyikan pratinjau aplikasi. Opsi ini juga otomatis mengunci akses aplikasi segera setelah ponsel kamu terkunci, sehingga data menjadi lebih sulit untuk terekspos.


![GREEN 2FA MULTISIG](assets/fr/07.webp)

Bagi kamu yang ingin meningkatkan privasi, aplikasi ini menawarkan opsi untuk merutekan lalu lintas melalui Tor, sebuah jaringan yang mengenkripsi semua koneksi dan membuat aktivitas lebih sulit dilacak. Meskipun opsi ini bisa sedikit memperlambat kinerja aplikasi, fitur ini sangat disarankan untuk melindungi privasi, terutama jika kamu tidak menggunakan node Bitcoin lengkap milikmu sendiri.


![GREEN 2FA MULTISIG](assets/fr/08.webp)

Untuk kamu yang memiliki node Bitcoin lengkap sendiri, Green Wallet menyediakan opsi untuk menghubungkannya melalui server Electrum, sehingga kamu mendapatkan kontrol penuh atas informasi jaringan Bitcoin dan penyiaran transaksi.

![GREEN 2FA MULTISIG](assets/fr/09.webp)

Fitur alternatif lainnya adalah opsi "*Verifikasi SPV*", yang memungkinkan kamu memverifikasi data Blockchain tertentu secara langsung, sehingga mengurangi ketergantungan pada node default Blockstream. Meski begitu, metode ini tetap tidak memberikan jaminan penuh seperti menggunakan node Bitcoin lengkap.

![GREEN 2FA MULTISIG](assets/fr/10.webp)

Setelah kamu menyesuaikan pengaturan ini sesuai dengan kebutuhan, klik tombol "*Save*" dan mulai ulang aplikasi.

![GREEN 2FA MULTISIG](assets/fr/11.webp)

## Buat dompet Bitcoin di Blockstream Green

Anda sekarang siap untuk membuat dompet Bitcoin. Klik tombol "*Mulai*".

![GREEN 2FA MULTISIG](assets/fr/12.webp)

Kamu bisa memilih untuk membuat dompet perangkat lunak lokal atau mengelola dompet dingin menggunakan dompet perangkat keras. Untuk tutorial ini, kita akan fokus membuat hot wallet, jadi kamu perlu memilih opsi "*On This Device*".

![GREEN 2FA MULTISIG](assets/fr/13.webp)

Kamu kemudian bisa memilih untuk memulihkan dompet Bitcoin yang sudah ada atau membuat dompet baru. Untuk keperluan tutorial ini, kita akan membuat dompet baru. Namun, jika kamu perlu memulihkan dompet Bitcoin yang sudah ada dari frasa mnemonik, misalnya karena ponsel lama hilang, kamu harus memilih opsi yang kedua.

![GREEN 2FA MULTISIG](assets/fr/14.webp)

Kemudian kamu dapat memilih antara frasa mnemonik 12 kata atau 24 kata. Frasa ini memungkinkan kamu memulihkan akses ke dompet dari perangkat lunak yang kompatibel jika terjadi masalah pada ponsel. Saat ini, memilih frasa 24 kata tidak memberikan tingkat keamanan yang lebih baik dibandingkan frasa 12 kata. Karena itu, aku menyarankan kamu memilih frasa mnemonik 12 kata.

Kemudian Green akan memberikan frasa mnemonik kamu. Sebelum melanjutkan, pastikan kamu tidak sedang diawasi. Klik "*Tampilkan frasa pemulihan*" untuk menampilkannya di layar.

![GREEN 2FA MULTISIG](assets/fr/15.webp)

**Mnemonic ini memberi kamu akses penuh dan tidak terbatas ke seluruh bitcoin kamu**. Siapa pun yang memiliki frasa ini bisa mencuri dana kamu, bahkan tanpa akses fisik ke ponsel, tergantung pada status timelock yang kedaluwarsa atau 2FA dalam kasus dompet 2/2 di Green.

Frasa ini memungkinkan kamu memulihkan akses ke kunci lokal jika ponsel hilang, dicuri, atau rusak. Karena itu, sangat penting untuk mencadangkannya dengan sangat hati-hati **di media fisik, bukan digital**, dan menyimpannya di tempat yang aman. Kamu bisa menuliskannya di atas kertas, atau untuk tingkat keamanan tambahan, terutama jika dompet berisi jumlah besar, aku menyarankan mengukirnya pada media baja tahan karat agar terlindung dari risiko kebakaran, banjir, atau kerusakan. Untuk hot wallet yang hanya menyimpan jumlah kecil, cadangan kertas sederhana biasanya sudah cukup.

*Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet seperti yang dilakukan dalam tutorial ini. Portofolio contoh ini hanya digunakan di Testnet dan akan dihapus di akhir tutorial.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)

Setelah kamu mencatat frasa mnemonik dengan benar di media fisik, klik "*Lanjutkan*". Green Wallet kemudian akan meminta kamu mengonfirmasi beberapa kata dalam frasa mnemonik untuk memastikan semuanya sudah dicatat dengan benar. Isi bagian yang kosong dengan kata-kata yang hilang.

![GREEN 2FA MULTISIG](assets/fr/17.webp)

Pilih kode PIN perangkat kamu yang akan digunakan untuk membuka Green Wallet. Ini menjadi perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam proses derivasi kunci kriptografi dompet. Artinya, meskipun tanpa PIN, selama kamu memiliki frasa mnemonik 12 atau 24 kata, kamu tetap bisa mendapatkan kembali akses ke kunci lokal.

Kami menyarankan memilih kode PIN 6 digit yang dibuat seacak mungkin. Pastikan kamu mengingat atau menyimpannya dengan aman, karena jika lupa, kamu harus memulihkan dompet dari frasa mnemonik. Kamu juga bisa menambahkan opsi pembukaan kunci biometrik untuk menghindari memasukkan PIN setiap kali digunakan. Namun secara umum, biometrik jauh lebih tidak aman dibandingkan PIN itu sendiri. Karena itu, secara default, aku menyarankan kamu tidak mengaktifkan opsi pembukaan kunci ini.


![GREEN 2FA MULTISIG](assets/fr/18.webp)

Masukkan PIN kamu untuk kedua kalinya untuk mengonfirmasikannya.

![GREEN 2FA MULTISIG](assets/fr/19.webp)

Tunggu hingga portofolio dibuat, lalu klik tombol "*Buat akun*".

![GREEN 2FA MULTISIG](assets/fr/20.webp)

Kemudian kamu dapat memilih antara dompet tanda tangan tunggal standar atau dompet yang dilindungi oleh autentikasi dua faktor (2FA). Dalam tutorial ini, kita akan memilih opsi kedua.

![GREEN 2FA MULTISIG](assets/fr/21.webp)

Dompet multisig Bitcoin kamu sekarang telah dibuat menggunakan aplikasi Green!

![GREEN 2FA MULTISIG](assets/fr/22.webp)

## Menyiapkan 2FA

Klik pada akun Anda.

![GREEN 2FA MULTISIG](assets/fr/23.webp)

Klik tombol hijau "*Tingkatkan keamanan akun Anda dengan menambahkan 2FA*".

![GREEN 2FA MULTISIG](assets/fr/24.webp)

Kamu kemudian bisa memilih metode autentikasi untuk mengakses kunci kedua dari multisig 2/2. Untuk tutorial ini, kita akan menggunakan aplikasi autentikasi. Jika kamu belum terbiasa dengan jenis aplikasi ini, aku sarankan kamu membaca tutorial kami tentang Authy:

https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Pilih "*Aplikasi Autentikator*".

![GREEN 2FA MULTISIG](assets/fr/25.webp)

Green kemudian akan menampilkan kode QR dan kunci pemulihan. Kunci ini memungkinkan kamu memulihkan akses ke 2FA jika aplikasi autentikasi hilang. Sangat disarankan untuk membuat cadangan kunci ini dan menyimpannya dengan aman, meskipun kamu tetap bisa memulihkan akses ke bitcoin setelah periode timelock berakhir, seperti yang dijelaskan sebelumnya.

Di aplikasi autentikasi kamu, tambahkan akun baru lalu pindai kode QR yang ditampilkan oleh Green.


![GREEN 2FA MULTISIG](assets/fr/26.webp)

*Tentu saja, kamu tidak boleh membagikan kunci dan kode QR ini di Internet, seperti yang aku lakukan dalam tutorial ini. Dompet contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.*

Klik tombol "*Lanjutkan*".

![GREEN 2FA MULTISIG](assets/fr/27.webp)

Masukkan kode dinamis 6 digit yang ada pada aplikasi autentikasi.

![GREEN 2FA MULTISIG](assets/fr/28.webp)

autentikasi 2 faktor sekarang diaktifkan.

![GREEN 2FA MULTISIG](assets/fr/29.webp)

Dengan menjelajahi menu ini, kamu juga bisa mengatur durasi timelock. Hitung mundur dimulai segera setelah bitcoin diterima, dan setelah timelock kedaluwarsa, dana hanya bisa dibelanjakan menggunakan kunci lokal, tanpa perlu 2FA. Durasi default ditetapkan 12 bulan, tapi untuk portofolio tabungan mungkin lebih masuk akal memilih 15 bulan agar frekuensi pembaruan timelock lebih jarang. Sebaliknya, untuk portofolio pengeluaran, timelock 6 bulan bisa lebih cocok karena akan sering diperbarui lewat transaksi harian, dan timelock yang lebih pendek juga mengurangi waktu tunggu jika terjadi masalah dengan 2FA. Terserah kamu untuk menentukan durasi timelock yang paling sesuai.

![GREEN 2FA MULTISIG](assets/fr/30.webp)

Sekarang kamu dapat keluar dari menu ini. Portofolio multisig sudah siap!

![GREEN 2FA MULTISIG](assets/fr/31.webp)

## Menyiapkan portofolio kamu di Blockstream Green

Jika kamu ingin mempersonalisasi portofolio, klik pada tiga titik kecil di sudut kanan atas.

![GREEN 2FA MULTISIG](assets/fr/32.webp)

Opsi "*Rename*" memungkinkan Anda menyesuaikan nama portofolio, yang sangat berguna jika kamu mengelola beberapa portofolio pada aplikasi yang sama.

![GREEN 2FA MULTISIG](assets/fr/33.webp)

Menu "*Unit*" memungkinkanmu untuk mengubah satuan dasar dompet. Sebagai contoh, kamu bisa memilih untuk menampilkannya dalam satoshi daripada bitcoin.

![GREEN 2FA MULTISIG](assets/fr/34.webp)

Menu "*Pengaturan*" menyediakan akses ke berbagai opsi dompet Bitcoin Anda.

![GREEN 2FA MULTISIG](assets/fr/35.webp)

Di sini, sebagai contoh, kamu akan menemukan kunci publik yang diperluas dan *descriptor*-nya, yang berguna jika kamu berencana untuk membuat dompet dalam mode watch-only dari dompet ini.

![GREEN 2FA MULTISIG](assets/fr/36.webp)

Kamu juga dapat mengubah PIN dompet dan mengaktifkan koneksi biometrik.

![GREEN 2FA MULTISIG](assets/fr/37.webp)

## Menggunakan Blockstream Green

Setelah dompet Bitcoin siap, kamu siap untuk menerima satoshi pertama kamu! Cukup klik tombol "*Terima*".

![GREEN 2FA MULTISIG](assets/fr/38.webp)

Green kemudian akan menampilkan address penerimaan pertama yang masih kosong di dompet kamu. Kamu bisa memindai kode QR yang terkait atau menyalin address tersebut secara langsung untuk menerima bitcoin. Jenis address ini tidak menentukan jumlah yang akan dikirim oleh pengirim. Namun, kamu juga bisa membuat address dengan permintaan jumlah tertentu dengan mengetuk tiga titik di pojok kanan atas, lalu memilih "*Request amount*", dan memasukkan jumlah yang diinginkan.

![GREEN 2FA MULTISIG](assets/fr/39.webp)

Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di dompet.

![GREEN 2FA MULTISIG](assets/fr/40.webp)

Tunggu hingga kamu menerima konfirmasi yang cukup untuk menganggap transaksi sudah pasti.

![GREEN 2FA MULTISIG](assets/fr/41.webp)

Dengan bitcoin di dompet, kamu sekarang juga dapat mengirim bitcoin. Klik "*Kirim*".

![GREEN 2FA MULTISIG](assets/fr/42.webp)

Pada halaman berikutnya, masukkan alamat penerima. Kamu dapat memasukkannya secara manual atau memindai kode QR.

![GREEN 2FA MULTISIG](assets/fr/43.webp)

Pilih jumlah pembayaran.

![GREEN 2FA MULTISIG](assets/fr/44.webp)

Di bagian bawah layar, kamu bisa memilih tarif biaya untuk transaksi ini. Kamu dapat mengikuti rekomendasi aplikasi atau menyesuaikan biaya sendiri. Semakin tinggi biaya dibandingkan transaksi tertunda lainnya, semakin cepat transaksi kamu akan diproses.
 Untuk informasi pasar biaya, silakan kunjungi [Mempool.space](https://mempool.space/) di bagian "*Biaya Transaksi*".

![GREEN 2FA MULTISIG](assets/fr/45.webp)

Klik "*Selanjutnya*" untuk mengakses layar ringkasan transaksi. Periksa apakah alamat, jumlah, dan biaya sudah benar.

![GREEN 2FA MULTISIG](assets/fr/46.webp)

Jika semua berjalan lancar, geser tombol hijau di bagian bawah layar ke kanan untuk menandatangani dan menyiarkan transaksi di jaringan Bitcoin.

![GREEN 2FA MULTISIG](assets/fr/47.webp)

Ini adalah saat kamu perlu memasukkan kode autentikasi untuk membuka kunci multisig kedua yang dipegang oleh Blockstream. Masukkan kode 6 digit yang ditampilkan pada aplikasi autentikasi kamu.

![GREEN 2FA MULTISIG](assets/fr/48.webp)

Transaksi sekarang akan muncul di dasbor dompet Bitcoin kamu, menunggu konfirmasi.

![GREEN 2FA MULTISIG](assets/fr/49.webp)

Sekarang kamu sudah tahu cara mengatur dompet multisig 2/2 dengan mudah menggunakan opsi 2FA di Blockstream Green.

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat menghargai jika kamu memberi jempol hijau di bawah. Jangan ragu juga untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih banyak.

Aku juga menyarankan kamu melihat tutorial komprehensif lainnya tentang aplikasi seluler Blockstream Green untuk menyiapkan dompet Liquid:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a
