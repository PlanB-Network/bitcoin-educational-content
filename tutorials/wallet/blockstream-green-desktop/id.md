---
name: Blockstream Green - Desktop
description: Menggunakan Green Wallet di komputer Anda
---
![cover](assets/cover.webp)

Dalam tutorial ini, kita akan membahas gimana cara pakai perangkat lunak Blockstream Green di komputer kamu buat ngelola dompet yang aman lewat dompet perangkat keras. Waktu kamu pakai dompet perangkat keras, penting banget buat pake perangkat lunak di komputer kamu untuk ngelola dompet. Perangkat lunak manajemen ini nggak punya akses ke kunci pribadi; fungsinya cuma buat lihat saldo dompet kamu, bikin alamat penerima, sama bikin dan nyebarin transaksi yang nanti bakal ditandatangani sama dompet perangkat keras. Green hanyalah salah satu dari banyak solusi yang tersedia buat ngelola dompet perangkat keras Bitcoin kamu.

Pada tahun 2024, Blockstream Green hanya kompatibel dengan perangkat Ledger Nano S (versi lama), Ledger Nano X, Trezor One, Trezor T, dan Blockstream Jade.

## Memperkenalkan Blockstream Green

Blockstream Green adalah aplikasi perangkat lunak yang tersedia di ponsel dan desktop. Sebelumnya dikenal sebagai Green Address, portofolio ini menjadi proyek Blockstream setelah diakuisisi pada tahun 2016.

Green adalah aplikasi yang sangat mudah digunakan, membuatnya sangat cocok untuk pemula. Aplikasi ini menawarkan berbagai fungsi, seperti pengelolaan hot wallet, dompet perangkat keras, serta dompet pada sidechain Liquid. Kamu juga dapat menggunakannya untuk mengatur dompet khusus jam tangan.

![GREEN-DESKTOP](assets/fr/01.webp)

Dalam tutorial ini, kita hanya akan berkonsentrasi pada penggunaan perangkat lunak pada komputer. Untuk menjelajahi penggunaan Green lainnya, silakan baca tutorial khusus kami yang lain:

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Menginstal dan mengonfigurasi perangkat lunak Blockstream Green

Mulailah dengan menginstal perangkat lunak Blockstream Green di komputermu. Buka [situs web resmi] (https://blockstream.com/green/) dan klik tombol "*Unduh Sekarang*". Kemudian ikuti proses instalasi sesuai dengan sistem operasi yang kamu pakai.

![GREEN-DESKTOP](assets/fr/02.webp)

Luncurkan aplikasi, lalu centang kotak "Saya menerima ketentuan...*".

![GREEN-DESKTOP](assets/fr/03.webp)

Kalau kamu buka Green pertama kali, layar beranda bakal muncul tanpa portofolio yang dikonfigurasi. Nanti, kalau kamu bikin atau impor portofolio, portofolio itu bakal tampil di antarmuka ini. Sebelum lanjut bikin portofolio, aku saranin kamu buat nyesuain dulu pengaturan aplikasi biar sesuai sama kebutuhan kamu. Klik ikon Pengaturan di pojok kiri bawah.

![GREEN-DESKTOP](assets/fr/04.webp)

Dalam menu "*General*", kamu bisa mengubah bahasa perangkat lunak dan mengaktifkan fungsi eksperimental jika kamu mau.

![GREEN-DESKTOP](assets/fr/05.webp)

Pada menu "*Jaringan*", kamu bisa mengaktifkan koneksi melalui Tor, sebuah jaringan yang mengenkripsi semua koneksimu dan membuat aktivitasmu menjadi sulit dilacak. Meskipun opsi ini mungkin sedikit memperlambat jalannya aplikasi, ini sangat disarankan untuk melindungi privasimu, terutama jika kamu tidak menggunakan node-mu sendiri.

![GREEN-DESKTOP](assets/fr/06.webp)

Untuk pengguna yang memiliki node lengkap mereka sendiri, Green menawarkan opsi untuk menghubungkannya melalui server Electrum, menjamin kontrol penuh atas informasi jaringan Bitcoin dan penyebaran transaksi. Untuk melakukannya, klik menu "*Server khusus dan validasi*", lalu masukkan detail server Electrum yang kamu punya.

![GREEN-DESKTOP](assets/fr/07.webp)

Fitur alternatif lainnya adalah opsi "*Verifikasi SPV*", yang memungkinkan kamu untuk memverifikasi data blockchain tertentu secara langsung dan dengan demikian mengurangi kebutuhan untuk mempercayai node default Blockstream, meskipun metode ini tidak memberikan semua jaminan dari sebuah node yang lengkap. Opsi ini juga dapat ditemukan di menu "*Server khusus dan validasi*".

![GREEN-DESKTOP](assets/fr/08.webp)

Setelah kamu menyesuaikan parameter ini dengan kebutuhanmu, kamu dapat keluar dari halaman ini.

## Impor dompet Bitcoin di Blockstream Green

Anda sekarang siap untuk mengimpor dompet Bitcoin-mu. Klik tombol "**Mulai**".

![GREEN-DESKTOP](assets/fr/09.webp)

Kamu dapat memilih antara membuat dompet perangkat lunak lokal atau mengelola cold wallet melalui dompet perangkat keras. Untuk tutorial ini, kita akan berkonsentrasi untuk mengelola dompet perangkat keras, jadi kamu harus memilih opsi "*On Hardware Wallet*".

Opsi "*Watch-only*" memungkinkan kamu untuk mengimpor kunci publik yang diperluas (`xpub`) untuk melihat transaksi portofolio tanpa dapat menggunakan dana yang terkait.

![GREEN-DESKTOP](assets/fr/10.webp)

Jika kamu menggunakan Jade, klik tombol yang sesuai. Jika tidak, pilih "*Hubungkan Perangkat Keras yang berbeda*". Dalam skenario ini, aku menggunakan Ledger Nano S. Untuk pengguna Ledger, pastikan kamu menginstal aplikasi "*Bitcoin Legacy*" di dompet perangkat keras, karena Green hanya mendukung versi ini.

![GREEN-DESKTOP](assets/fr/11.webp)

Hubungkan dompet perangkat keras milikmu ke komputer dan pilih Green.

![GREEN-DESKTOP](assets/fr/12.webp)

Tunggu hingga Green mengimpor informasi portofoliomu, setelah itu kamu bisa mengaksesnya.

![GREEN-DESKTOP](assets/fr/13.webp)

Pada titik ini, ada dua skenario yang mungkin terjadi. Jika kamu sudah pernah menggunakan dompet perangkat keras sebelumnya, kamu akan melihat akunmu muncul di perangkat lunak. Namun, jika kamu baru saja menginisialisasi dompet perangkat keras dengan membuat frasa mnemonik tanpa pernah menggunakannya, kamu perlu membuat akun. Klik "*Buat Akun*".

![GREEN-DESKTOP](assets/fr/14.webp)

Pilih "*Standard*" jika kamu ingin menggunakan dompet klasik.

![GREEN-DESKTOP](assets/fr/15.webp)

Sekarang kamu sudah memiliki akses ke akun milikmu.

![GREEN-DESKTOP](assets/fr/16.webp)

## Menggunakan wallet perangkat keras dengan Blockstream Green

Setelah wallet Bitcoin siap, kamu siap untuk menerima satoshi pertamamu! Cukup klik tombol "*Terima*".

![GREEN-DESKTOP](assets/fr/17.webp)

Klik tombol "*Salin alamat*" untuk menyalin alamat, atau pindai kode QR-nya.

![GREEN-DESKTOP](assets/fr/18.webp)

Setelah transaksi disiarkan di jaringan, transaksi tersebut akan muncul di walletmu. Tunggu hingga kamu menerima konfirmasi yang cukup untuk menganggap transaksi tersebut tidak dapat diubah.

![GREEN-DESKTOP](assets/fr/19.webp)

Dengan bitcoin di wallet-mu, Kamu sekarang siap untuk mengirimnya. Klik tombol "*Kirim*".

![GREEN-DESKTOP](assets/fr/20.webp)

Pada halaman berikutnya, masukkan alamat penerima. kamu bisa memasukkannya secara manual atau memindai kode QR dengan webcammu.

![GREEN-DESKTOP](assets/fr/21.webp)

Pilih jumlah pembayaran.

![GREEN-DESKTOP](assets/fr/22.webp)

Di bagian bawah layar, kamu dapat memilih tarif biaya untuk transaksi ini. Kamu dapat memilih untuk mengikuti rekomendasi aplikasi atau menyesuaikan biaya. Semakin tinggi biaya dalam kaitannya dengan transaksi tertunda lainnya, semakin cepat transaksi akan diproses. Untuk informasi pasar biaya, silakan kunjungi [Mempool.space] (https://mempool.space/) di bagian "*Biaya Transaksi*".

![GREEN-DESKTOP](assets/fr/23.webp)

Jika kamu ingin memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, klik tombol "*Pemilihan koin secara manual*".

![GREEN-DESKTOP](assets/fr/24.webp)

Periksa parameter transaksi dan, jika semuanya sesuai dengan yang kamu harapkan, klik "*Next*".

![GREEN-DESKTOP](assets/fr/25.webp)

Periksa kembali apakah alamat, jumlah, dan biaya sudah benar, lalu klik "*Konfirmasi transaksi*".

![GREEN-DESKTOP](assets/fr/26.webp)

Pastikan semua parameter transaksi sudah benar di layar wallet perangkat keras kamu, lalu tanda tangani transaksi dengan menggunakan wallet tersebut.

![GREEN-DESKTOP](assets/fr/27.webp)

Setelah transaksi ditandatangani dari wallet perangkat keras, Green secara otomatis menyiarkannya ke jaringan Bitcoin. Kemudian transaksi kamu akan muncul di dasbor wallet Bitcoin milikmu, menunggu konfirmasi.

![GREEN-DESKTOP](assets/fr/28.webp)

Sekarang kamu sudah mengetahui bagaimana cara mengkonfigurasi Blockstream Green dengan mudah untuk mengelola wallet Bitcoin yang kamu punya pada wallet perangkat keras.

Jika kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosial. Terima kasih banyak!

Saya juga menyarankan kamu untuk melihat tutorial komprehensif lainnya di aplikasi seluler Blockstream Green untuk menyiapkan hot wallet:

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143


