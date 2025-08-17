---
name: Blockstream Green - 2FA
description: Menyiapkan multisig 2/2 di Dompet Green
---
![cover](assets/cover.webp)

___

***Catatan:** Mulai Mei 2025, tidak akan lagi memungkinkan untuk mengaktifkan akun baru yang dilindungi oleh autentikasi dua faktor (2FA). Fitur ini hanya tersedia untuk pengguna yang sebelumnya sudah mengaktifkan jenis akun ini.*

___

Dompet perangkat lunak itu aplikasi yang dipasang di komputer, smartphone, atau perangkat lain yang terhubung ke internet. Dengan dompet ini, kamu bisa ngatur sekaligus mengamankan kunci Bitcoin-mu. Beda sama dompet perangkat keras yang nyimpen kunci pribadi secara terisolasi, dompet “panas” (hot wallet) berjalan di lingkungan yang lebih rentan terhadap serangan siber, jadi risikonya dibajak atau dicuri juga lebih besar.

Dompet perangkat lunak paling pas dipakai buat ngatur jumlah Bitcoin yang wajar, terutama kalau buat transaksi sehari-hari. Buat kamu yang punya aset Bitcoin terbatas, dompet ini juga bisa jadi pilihan menarik, karena beli dompet perangkat keras kadang terasa kurang sebanding. Tapi, karena dompet perangkat lunak selalu terhubung ke internet, keamanannya lebih rendah buat nyimpen tabungan jangka panjang atau dana besar. Kalau buat kebutuhan itu, pilihan terbaik tetap dompet perangkat keras.

Dalam tutorial ini, aku akan tunjukkan kepada Anda bagaimana cara meningkatkan keamanan hot wallet menggunakan opsi "*2FA*" di Blockstream Green.

![GREEN 2FA MULTISIG](assets/fr/01.webp)

## Memperkenalkan Blockstream Green

Blockstream Green adalah dompet perangkat lunak yang tersedia di ponsel dan desktop. Sebelumnya dikenal sebagai *Green Address*, dompet ini menjadi proyek Blockstream setelah diakuisisi pada tahun 2016.

Green merupakan aplikasi yang sangat mudah digunakan, yang bikin pemula tertarik. Aplikasi ini menawarkan semua fitur penting dari dompet Bitcoin yang bagus, termasuk RBF (*Replace-by-Fee*), opsi koneksi Tor, kemampuan untuk menghubungkan nodemu sendiri, SPV (*Simple Payment Verification*), penandaan dan kontrol koin.

Blockstream Green juga mendukung jaringan Liquid, yaitu sidechain Bitcoin yang dikembangkan oleh Blockstream buat transaksi cepat dan lebih privat di luar blockchain utama. Di tutorial ini kita bakal fokus ke Bitcoin aja, tapi aku juga udah bikin tutorial terpisah kalau kamu mau belajar cara pakai Liquid di Green:

https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## opsi multisig 2/2 (2FA)

Pada Green, kamu bisa membuat hot wallet klasik "*singlesig*". Namun, kamu juga memiliki opsi "*2FA multisig*", yang meningkatkan keamanan hot wallet tanpa harus merepotkan pengelolaan sehari-hari.

Jadi, kamu bakal bikin dompet multisig 2/2, artinya setiap transaksi butuh tanda tangan dari dua kunci. Kunci pertama berasal dari frasa mnemonik 12 atau 24 kata yang diamankan secara lokal pakai PIN di ponselmu. Kunci ini sepenuhnya ada di bawah kendali kamu. Sementara itu, kunci kedua dipegang sama server Blockstream, dan supaya bisa dipakai buat tanda tangan perlu otentikasi. Proses otentikasinya bisa lewat kode yang dikirim via email, SMS, panggilan telepon, atau—seperti yang bakal kita lihat di tutorial ini—lewat aplikasi autentikator (Authy, Google Authenticator, dll.).

Biar kamu tetap punya kendali penuh kalau suatu saat Blockstream gagal (misalnya perusahaan bangkrut atau server yang nyimpen kunci kedua hancur), ada mekanisme time-lock yang dipasang di multisig kamu. Mekanisme ini bakal otomatis ubah multisig 2/2 jadi 1/2 setelah sekitar satu tahun (tepatnya 51.840 blok, tapi angka ini bisa diubah). Setelah itu, dompetmu cuma butuh kunci lokal aja buat ngeluarin Bitcoin. Jadi, kalau kamu kehilangan akses ke server Blockstream atau otentikasi 2FA, cukup tunggu maksimal setahun dan kamu tetap bisa bebas pakai Bitcoin-mu langsung dari aplikasi, tanpa harus bergantung lagi sama Blockstream.

![GREEN 2FA MULTISIG](assets/fr/02.webp)

Metode ini bikin hot wallet kamu jauh lebih aman, sambil tetap kasih kamu kendali penuh atas Bitcoin dan memudahkan pemakaian sehari-hari. Tapi, ada satu hal penting: timelock harus diperbarui secara berkala supaya 2FA tetap aktif. Hitungan mundur 360 hari—di mana dana kamu dilindungi oleh 2FA—langsung mulai sejak kamu menerima Bitcoin. Kalau setelah 360 hari itu kamu belum melakukan transaksi dengan dana tersebut, Bitcoin-mu cuma bakal dilindungi sama kunci lokal aja, tanpa 2FA.

Keterbatasan ini bikin opsi 2FA lebih cocok dipakai buat portofolio pengeluaran, karena transaksi rutin otomatis memperbarui timelock. Tapi kalau tujuannya buat tabungan jangka panjang, agak ribet, karena kamu harus ingat untuk melakukan transaksi sweep setidaknya setahun sekali sebelum timelock habis.

Ada juga kekurangan lain dari metode keamanan ini, yaitu kamu harus pakai skrip minoritas. Dari sisi privasi, ini bikin keadaan lebih rumit: karena cuma sedikit orang yang pakai jenis skrip kayak gini, jadi lebih gampang bagi pengamat luar buat mengenali pola dompetmu. Selain itu, ukuran skrip yang lebih besar juga bikin biaya transaksinya jadi lebih tinggi.

Jika kamu memilih untuk tidak menggunakan opsi 2FA dan hanya ingin membuat dompet "*singlesig*" di Green, aku mengundangmu untuk membaca tutorial lainnya:

https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Menginstal dan mengonfigurasi perangkat lunak Blockstream Green

Langkah pertama tentu saja mengunduh aplikasi Green. Buka toko aplikasi kamu:

- [Untuk Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Untuk Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN 2FA MULTISIG](assets/fr/03.webp)

Untuk pengguna Android, kamu juga dapat menginstal aplikasi melalui file `.apk` [tersedia di GitHub Blockstream](https://github.com/Blockstream/green_android/releases).

![GREEN 2FA MULTISIG](assets/fr/04.webp)

Luncurkan aplikasi, lalu centang kotak "Saya menerima ketentuan...*".

![GREEN 2FA MULTISIG](assets/fr/05.webp)

Kalau kamu buka Green pertama kali, layar beranda bakal tampil tanpa ada portofolio yang dikonfigurasi. Nanti, setelah kamu bikin atau impor portofolio, baru deh portofolio itu muncul di antarmuka ini. Sebelum lanjut bikin portofolio, sebaiknya kamu atur dulu pengaturan aplikasi biar sesuai sama kebutuhanmu. Klik aja “Pengaturan aplikasi”.

![GREEN 2FA MULTISIG](assets/fr/06.webp)

Opsi "*Privasi yang Ditingkatkan*", yang hanya tersedia di Android, meningkatkan privasi dengan menonaktifkan tangkapan layar dan menyembunyikan pratinjau aplikasi. Opsi ini juga secara otomatis mengunci akses aplikasi segera setelah ponsel kamu terkunci, sehingga data lebih sulit untuk diekspos.

![GREEN 2FA MULTISIG](assets/fr/07.webp)

Buat kamu yang pengin ningkatin privasi, aplikasi ini punya opsi buat ngeroute semua lalu lintas lewat Tor, jaringan yang mengenkripsi koneksi kamu dan bikin aktivitasmu susah dilacak. Walaupun opsi ini bisa bikin aplikasi jadi agak lebih lambat, fitur ini tetap sangat disarankan buat jaga privasi—apalagi kalau kamu belum pakai full node sendiri.

![GREEN 2FA MULTISIG](assets/fr/08.webp)

Untuk pengguna yang memiliki node lengkap mereka sendiri, Green Wallet menawarkan kemungkinan untuk menghubungkannya melalui server Electrum, menjamin kontrol penuh atas informasi jaringan Bitcoin dan distribusi transaksi.

![GREEN 2FA MULTISIG](assets/fr/09.webp)

Fitur alternatif lainnya adalah opsi "*Verifikasi SPV*", yang memungkinkan Anda untuk memverifikasi data blockchain tertentu secara langsung dan dengan demikian mengurangi kebutuhan untuk mempercayai node default Blockstream, meskipun metode ini tidak memberikan semua jaminan dari sebuah node yang lengkap.

![GREEN 2FA MULTISIG](assets/fr/10.webp)

Setelah Anda menyesuaikan pengaturan ini dengan kebutuhanmu, klik tombol "*Save*" dan mulai ulang aplikasi.

![GREEN 2FA MULTISIG](assets/fr/11.webp)

## Buat dompet Bitcoin di Blockstream Green

Kamu sekarang siap untuk membuat dompet Bitcoin. Klik tombol "*Mulai*".

![GREEN 2FA MULTISIG](assets/fr/12.webp)

Kamu dapat memilih antara membuat dompet perangkat lunak lokal atau mengelola dompet dingin melalui dompet perangkat keras. Untuk tutorial ini, kita akan berkonsentrasi untuk membuat hot wallet, jadi Anda harus memilih opsi "*On This Device*".

![GREEN 2FA MULTISIG](assets/fr/13.webp)

Kamu bisa pilih buat bikin dompet Bitcoin baru atau memulihkan dompet yang sudah ada. Di tutorial ini kita bakal bikin dompet baru. Tapi kalau kamu perlu ngebuat ulang dompet Bitcoin dari frasa mnemonik—misalnya karena HP lamamu hilang—kamu tinggal pilih opsi yang kedua.

![GREEN 2FA MULTISIG](assets/fr/14.webp)

Setelah itu, kamu bisa pilih antara frasa mnemonik 12 kata atau 24 kata. Frasa ini berfungsi buat ngembaliin akses ke dompet kamu dari software yang kompatibel kalau ada masalah sama HP-mu. Saat ini, pakai frasa 24 kata nggak kasih keamanan lebih dibanding frasa 12 kata. Jadi, aku saranin kamu pilih frasa mnemonik 12 kata aja.

Green kemudian akan memberikan frasa mnemonik kamu. Sebelum melanjutkan, pastikan kamu tidak sedang diawasi. Klik "*Tampilkan frasa pemulihan*" untuk menampilkannya di layar.

![GREEN 2FA MULTISIG](assets/fr/15.webp)

**Mnemonik ini memberikanmu akses penuh dan tidak terbatas ke semua bitcoinmu**. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke ponsel (tergantung pada penguncian waktu yang kedaluwarsa atau 2FA dalam kasus dompet 2/2 di Green).

Hal ini memungkinkan kamu untuk memulihkan akses ke kunci lokal jika terjadi kehilangan, pencurian, atau kerusakan pada ponsel kamu. Jadi, sangat penting untuk mencadangkannya dengan hati-hati **pada media fisik (bukan digital)** dan menyimpannya di tempat yang aman. Kamu bisa menuliskannya di selembar kertas, atau untuk keamanan tambahan, jika dompet kamu berukuran besar, aku sarankan untuk mengukirnya di atas penyangga baja tahan karat untuk melindunginya dari risiko kebakaran, banjir, atau kehancuran (untuk hot wallet yang dirancang untuk mengamankan bitcoin dalam jumlah kecil, cadangan kertas sederhana mungkin sudah cukup).

*Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.*

![GREEN 2FA MULTISIG](assets/fr/16.webp)

Setelah Anda merekam frasa mnemonik kamu dengan benar pada media fisik, klik "*Lanjutkan*". Green Wallet kemudian akan memintamu untuk mengonfirmasi beberapa kata dalam frasa mnemonik kamu untuk memastikan telah merekamnya dengan benar. Isi bagian yang kosong dengan kata-kata yang hilang.

![GREEN 2FA MULTISIG](assets/fr/17.webp)

Pilih kode PIN untuk perangkatmu, yang bakal dipakai buat buka Green Wallet. PIN ini berfungsi sebagai perlindungan dari akses fisik yang nggak sah. PIN ini nggak ada hubungannya sama turunan kunci kriptografi dompetmu. Jadi, walaupun tanpa PIN, siapa pun yang punya frasa mnemonik 12 atau 24 kata tetap bisa ngembaliin akses ke kunci lokalmu.

Disarankan pakai PIN 6 digit yang acak. Jangan lupa simpan baik-baik, soalnya kalau sampai lupa, kamu terpaksa harus pulihin dompet dari frasa mnemonik. Kamu juga bisa nambahin opsi buka kunci pakai biometrik biar nggak perlu masukin PIN tiap kali dipakai. Tapi secara umum, biometrik jauh lebih nggak aman dibanding PIN itu sendiri. Jadi, secara default, aku saranin jangan aktifin opsi ini.

![GREEN 2FA MULTISIG](assets/fr/18.webp)

Masukkan PIN untuk kedua kalinya untuk mengonfirmasikannya.

![GREEN 2FA MULTISIG](assets/fr/19.webp)

Tunggu hingga portofolio dibuat, lalu klik tombol "*Buat akun*".

![GREEN 2FA MULTISIG](assets/fr/20.webp)

Kemudian dapat memilih antara dompet tanda tangan tunggal standar atau dompet yang dilindungi oleh autentikasi dua faktor (2FA). Dalam tutorial ini, kita akan memilih opsi kedua.

![GREEN 2FA MULTISIG](assets/fr/21.webp)

Dompet multisig Bitcoin-mu sekarang telah dibuat menggunakan aplikasi Green!

![GREEN 2FA MULTISIG](assets/fr/22.webp)

## Menyiapkan 2FA

Klik pada akun.

![GREEN 2FA MULTISIG](assets/fr/23.webp)

Klik tombol hijau "*Tingkatkan keamanan akun dengan menambahkan 2FA*".

![GREEN 2FA MULTISIG](assets/fr/24.webp)

Setelah itu, kamu bisa pilih metode autentikasi buat ngakses kunci kedua dari multisig 2/2-mu. Di tutorial ini, kita bakal pakai aplikasi autentikasi. Kalau kamu belum familiar sama jenis aplikasi ini, aku saranin baca dulu tutorial kami tentang Authy:

https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Pilih "*Aplikasi Autentikator*".

![GREEN 2FA MULTISIG](assets/fr/25.webp)

Green lalu bakal nampilin kode QR dan kunci pemulihan. Kunci ini dipakai buat ngembaliin akses 2FA kalau aplikasi Authy kamu hilang. Disarankan banget buat nyimpen cadangan kunci ini dengan aman, meskipun sebenarnya kamu tetap bisa balik akses ke Bitcoin-mu setelah time-lock berakhir, seperti yang udah dijelasin sebelumnya.

Di aplikasi autentikasi, tambahkan kode baru, lalu pindai kode QR yang disediakan oleh Green.

![GREEN 2FA MULTISIG](assets/fr/26.webp)

*Tentu saja, Anda tidak boleh membagikan kunci dan kode QR ini di Internet, seperti yang saya lakukan dalam tutorial ini. Dompet contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.*

Klik tombol "*Lanjutkan*".

![GREEN 2FA MULTISIG](assets/fr/27.webp)

Masukkan kode dinamis 6 digit yang ada pada aplikasi autentikasi.

![GREEN 2FA MULTISIG](assets/fr/28.webp)

autentikasi 2 faktor sekarang diaktifkan.

![GREEN 2FA MULTISIG](assets/fr/29.webp)

Di menu ini, kamu juga bisa ngatur durasi time-lock. Hitungan mundurnya mulai begitu Bitcoin masuk, dan setelah time-lock habis, dana kamu cuma bisa dipakai pakai kunci lokal aja tanpa 2FA. Secara default, durasinya diset 12 bulan. Tapi kalau buat tabungan, masuk akal juga kalau kamu pilih 15 bulan biar nggak terlalu sering perpanjang time-lock. Sebaliknya, buat portofolio pengeluaran, time-lock 6 bulan bisa lebih cocok, soalnya bakal sering otomatis diperbarui lewat transaksi harian, plus durasi yang lebih pendek bikin waktu tunggu lebih singkat kalau ada masalah sama 2FA. Intinya, kamu yang tentuin durasi time-lock yang paling pas buat kebutuhanmu.

![GREEN 2FA MULTISIG](assets/fr/30.webp)

Kamu sekarang dapat keluar dari menu ini. Portofolio multisig sudah siap!

![GREEN 2FA MULTISIG](assets/fr/31.webp)

## Menyiapkan portofolio di Blockstream Green

Jika kamu ingin mempersonalisasi portofolio, klik pada tiga titik kecil di sudut kanan atas.

![GREEN 2FA MULTISIG](assets/fr/32.webp)

Opsi "*Rename*" memungkinkan kamu menyesuaikan nama portofolio, yang sangat berguna jika kamu mengelola beberapa portofolio pada aplikasi yang sama.

![GREEN 2FA MULTISIG](assets/fr/33.webp)

Menu "*Unit*" memungkinkan kamu untuk mengubah satuan dasar dompet. Sebagai contoh, kamu bisa memilih untuk menampilkannya dalam satoshi daripada bitcoin.

![GREEN 2FA MULTISIG](assets/fr/34.webp)

Menu "*Pengaturan*" menyediakan akses ke berbagai opsi dompet Bitcoin-mu.

![GREEN 2FA MULTISIG](assets/fr/35.webp)

Di sini, sebagai contoh, kamu akan menemukan kunci publik yang diperluas dan *descriptor*-nya, yang berguna jika kamu berencana untuk membuat dompet dalam mode watch-only dari dompet ini.

![GREEN 2FA MULTISIG](assets/fr/36.webp)

Kamu juga dapat mengubah PIN dompet dan mengaktifkan koneksi biometrik.

![GREEN 2FA MULTISIG](assets/fr/37.webp)

## Menggunakan Blockstream Green

Setelah dompet Bitcoin siap, kamu siap untuk menerima satoshi pertamamu! Cukup klik tombol "*Terima*".

![GREEN 2FA MULTISIG](assets/fr/38.webp)

Green kemudian akan menampilkan alamat penerima pertama yang kosong di dompetmu. Kamu bisa memindai kode QR yang terkait, atau menyalin alamat tersebut secara langsung untuk mengirim bitcoin. Jenis alamat ini tidak menentukan jumlah yang akan dikirim oleh pembayar. Namun, kamu bisa membuat alamat yang meminta jumlah tertentu, dengan mengeklik tiga titik kecil di pojok kanan atas, lalu "*Request amount*", dan memasukkan jumlah yang diinginkan.

![GREEN 2FA MULTISIG](assets/fr/39.webp)

Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di dompetmu.

![GREEN 2FA MULTISIG](assets/fr/40.webp)

Tunggu hingga kamu menerima konfirmasi yang cukup untuk menganggap transaksi sudah pasti.

![GREEN 2FA MULTISIG](assets/fr/41.webp)

Dengan bitcoin di dompet, kamu sekarang juga dapat mengirim bitcoin. Klik "*Kirim*".

![GREEN 2FA MULTISIG](assets/fr/42.webp)

Pada halaman berikutnya, masukkan alamat penerima. Kamu dapat memasukkannya secara manual atau memindai kode QR.

![GREEN 2FA MULTISIG](assets/fr/43.webp)

Pilih jumlah pembayaran.

![GREEN 2FA MULTISIG](assets/fr/44.webp)

Di bagian bawah layar, kamu dapat memilih tarif biaya untuk transaksi ini. kamu dapat memilih untuk mengikuti rekomendasi aplikasi atau menyesuaikan biaya. Semakin tinggi biaya dalam kaitannya dengan transaksi tertunda lainnya, semakin cepat transaksi kamu akan diproses. Untuk informasi pasar biaya, silakan kunjungi [Mempool.space] (https://mempool.space/) di bagian "*Biaya Transaksi*".

![GREEN 2FA MULTISIG](assets/fr/45.webp)

Klik "*Selanjutnya*" untuk mengakses layar ringkasan transaksi. Periksa apakah alamat, jumlah, dan biaya sudah benar.

![GREEN 2FA MULTISIG](assets/fr/46.webp)

Jika semua berjalan lancar, geser tombol hijau di bagian bawah layar ke kanan untuk menandatangani dan menyiarkan transaksi di jaringan Bitcoin.

![GREEN 2FA MULTISIG](assets/fr/47.webp)

Ini adalah saat kamu perlu memasukkan kode autentikasi Anda untuk membuka kunci multisig kedua yang dipegang oleh Blockstream. Masukkan kode 6 digit yang ditampilkan pada aplikasi autentikasi.

![GREEN 2FA MULTISIG](assets/fr/48.webp)

Transaksi sekarang akan muncul di dasbor dompet Bitcoin milikmu, menunggu konfirmasi.

![GREEN 2FA MULTISIG](assets/fr/49.webp)

Jadi sekarang kamu sudah tahu bagaimana cara mengatur dompet multisig 2/2 dengan mudah menggunakan opsi 2FA Blockstream Green!

Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosial. Terima kasih banyak!

Aku juga menyarankanmu untuk melihat tutorial komprehensif lainnya di aplikasi seluler Blockstream Green untuk menyiapkan dompet Liquid:

https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

