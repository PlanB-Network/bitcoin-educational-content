---
name: Ginger Wallet
description: Perangkat lunak Bitcoin wallet yang bersumber terbuka dan mandiri, fork dari Wasabi Wallet, yang mengintegrasikan Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet adalah portofolio Bitcoin sumber terbuka, non-kustodian yang berfokus pada kerahasiaan dan privasi. Ini memulai kehidupan sebagai fork dari Wasabi Wallet (setelah versi 2.0.7.2 - lisensi MIT).



Ginger Wallet mempertahankan arsitektur teknis Wasabi sambil menambahkan beberapa fitur khusus. Menurut [dokumentasi Ginger Wallet] (https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi menekankan pada **otonomi dan kontrol**, sementara Ginger berfokus pada **kemudahan penggunaan, keamanan, dan pengalaman yang disederhanakan**, sehingga dapat diakses oleh mereka yang tidak terlalu paham dengan aspek teknis.



Ginger Wallet adalah perangkat lunak wallet untuk komputer saja (tidak ada aplikasi seluler).



## Apa itu Coinjoin?



**coinjoin** adalah struktur transaksi Bitcoin khusus yang menyatukan beberapa peserta dalam satu transaksi kolaboratif. Mekanisme ini menggabungkan entri dari beberapa pengguna yang berbeda ke dalam sebuah transaksi yang sama, sehingga sangat sulit - bahkan tidak mungkin, jika dilakukan dengan benar - untuk melacak dana. Sebagai hasilnya, hampir tidak mungkin bagi pengamat luar untuk mengidentifikasi secara pasti asal dan tujuan bitcoin yang terlibat, tidak seperti pada transaksi Bitcoin konvensional.



Bagi Anda, sebagai pengguna, coinjoin membantu menjaga kerahasiaan Anda. Sebagai contoh, jika Anda menerima donasi sebesar 10.000 sats pada alamat Bitcoin, pengirim dapat melacak dana ini dan, dalam beberapa kasus, menyimpulkan bahwa Anda memiliki jumlah bitcoin yang lebih besar, atau mengamati aktivitas Anda. Dengan melakukan coinjoin setelah donasi 10.000 sats ini, Anda mematahkan kemampuan pelacakan: pengirim tidak lagi dapat memperoleh informasi apa pun tentang Anda dari pembayaran ini.



Coinjoin Chaumian menawarkan tingkat keamanan yang tinggi, karena dana tetap berada di bawah kendali eksklusif pengguna setiap saat. Bahkan operator dari server koordinasi tidak dapat mengalihkan bitcoin peserta dalam keadaan apa pun. Baik pengguna maupun koordinator tidak perlu saling mempercayai: masing-masing tetap memegang kendali atas kunci pribadinya, dan hanya memiliki wewenang untuk memvalidasi transaksi. Oleh karena itu, tidak ada pihak ketiga yang dapat mengambil bitcoin Anda selama coinjoin, atau membuat hubungan langsung antara input dan output Anda.



Untuk mempelajari lebih lanjut tentang coinjoin, lihat kursus BTC 204 dari Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Pasang Ginger Wallet



Untuk menginstal Ginger Wallet, kunjungi situs web [Ginger Wallet] (https://gingerwallet.io).



Tekan **Unduh** untuk mengunduh versi yang tepat untuk komputer Anda (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Pilihan lainnya adalah dengan membuka [GitHub] proyek ini (https://github.com/GingerPrivacy/GingerWallet/releases) untuk mengunduhnya.



![screen](assets/fr/04.webp)



Kemudian jalankan program instalasi.



![screen](assets/fr/05.webp)




## Pengaturan parameter



### Konfigurasi awal



Buka Ginger Wallet, pilih bahasa yang Anda inginkan.



![screen](assets/fr/06.webp)



Sejak awal, Ginger mengingatkan Anda tentang biaya yang terlibat dalam proses coinjoin.



![screen](assets/fr/07.webp)



Kemudian tekan **Mulai**, lalu **Baru** untuk membuat portofolio baru.



![screen](assets/fr/08.webp)



Selanjutnya, simpan dan konfirmasikan seedphrase Anda.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Untuk keamanan tambahan, Ginger Wallet memberi Anda opsi untuk menambahkan passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase ini, setelah ditambahkan, akan diminta setiap kali Anda mencoba mengakses portofolio Anda.



![screen](assets/fr/12.webp)



Ginger secara otomatis mengaktifkan **Coinjoin** default ketika Anda membuat portofolio. Anda akan diberitahu tentang hal ini dan kemudian dapat menyesuaikan pengaturan agar sesuai dengan kebutuhan Anda.



![screen](assets/fr/13.webp)




### Pengaturan umum



Setelah Anda membuat portofolio pertama Anda, Anda akan dibawa ke antarmuka Ginger Wallet.



![screen](assets/fr/14.webp)



Aktifkan **Mode rahasia**, jika Anda ingin menyembunyikan saldo di dompet Anda.



![screen](assets/fr/15.webp)



Anda dapat membuat beberapa portofolio pada Ginger Wallet. Cukup klik **Tambahkan portofolio**.



![screen](assets/fr/16.webp)



Ginger mendukung penggunaan portofolio perangkat keras melalui antarmuka Bitcoin Core standar, meskipun integrasi langsung dari atau ke portofolio perangkat keras belum tersedia.



Portofolio perangkat keras yang kompatibel termasuk (tetapi tidak terbatas pada):




- Blockstream Jade
- Kartu dingin MK4
- Kartu dingin Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- dll.



Sekarang klik **Pengaturan**.



![screen](assets/fr/17.webp)



Pengaturan ini adalah pengaturan aplikasi secara umum, dan konfigurasi yang Anda buat di sana akan berlaku untuk semua portofolio.



Dalam **Pengaturan**, Anda memiliki tab :





- Umum**



![screen](assets/fr/18.webp)





- Penampilan



Di tab ini, Anda dapat mengubah bahasa, mata uang, dan unit tampilan biaya (BTC/Satoshi), di antaranya.



![screen](assets/fr/19.webp)





- Bitcoin**



Tab ini memungkinkan Anda mengaktifkan Bitcoin Knots untuk berjalan pada saat aplikasi dijalankan, memilih jaringan Anda (Main/RegTest), dan penyedia tarif pengisian daya Anda (Mempool Space/Blockstream info/Full Node), dll.



![screen](assets/fr/20.webp)





- Fitur keselamatan**



Pada tab Keamanan, Anda bisa mengaktifkan autentikasi dua faktor, mengaktifkan atau menonaktifkan Tor, dan bahkan menonaktifkannya setelah aplikasi Ginger ditutup.



![screen](assets/fr/21.webp)



**NB** :




- Untuk autentikasi dua faktor, pastikan aplikasi autentikasi Anda mendukung protokol SHA256 dan kode 8 digit. Ginger Wallet memerlukan kode 2FA 8 digit untuk meningkatkan keamanan. Format yang lebih panjang ini membuat kode lebih sulit ditebak atau dikompromikan, sehingga memberikan perlindungan yang lebih besar terhadap akses yang tidak sah.
- Secara default, semua lalu lintas jaringan Ginger melewati Tor, sehingga tidak memerlukan konfigurasi manual. Jika Tor sudah aktif di sistem Anda, Ginger akan secara otomatis memberikan prioritas.



Tetapi setelah Anda menonaktifkan Tor dalam pengaturan, privasi Anda secara umum tetap terjaga, kecuali dalam dua situasi:




- selama Coinjoin, koordinator dapat menghubungkan input dan output Anda ke alamat IP Anda;
- ketika menyiarkan transaksi, simpul berbahaya yang terhubung dengan Anda dapat mengaitkan transaksi Anda dengan IP Anda.



Jangan lupa untuk menekan **Done** (di sudut kanan bawah) setiap kali, untuk menyimpan pengaturan Anda. Beberapa pengaturan mengharuskan Ginger Wallet dihidupkan ulang agar dapat diterapkan.



Selain itu, bilah pencarian di bagian atas portofolio memungkinkan Anda mencari dan mengakses parameter apa pun, dll...



![screen](assets/fr/22.webp)




### Konfigurasi portofolio



Beberapa portofolio dapat dibuat dalam aplikasi, sehingga setiap portofolio dapat dikonfigurasikan sesuai dengan kebutuhan Anda. Untuk melakukannya, klik **tiga titik** di depan nama portofolio, lalu **Pengaturan portofolio**.



![screen](assets/fr/23.webp)



Seperti yang dapat Anda lihat, selain parameter wallet, Anda juga dapat melihat UTXO (daftar token yang Anda miliki), statistik, dan informasi wallet (kunci publik yang diperluas, misalnya).



Untuk kembali ke konfigurasi portofolio, setelah Anda mengklik parameter portofolio, Anda akan dibawa ke tab berikut:




- Umum** (di mana Anda dapat mengubah nama portofolio);



![screen](assets/fr/24.webp)





- Coinjoin** (di mana Anda dapat menyesuaikan pengaturan coinjoin untuk wallet ini);



![screen](assets/fr/25.webp)





- Tools** (di mana Anda dapat memeriksa seedphrase Anda, menyinkronkan portofolio Anda lagi, atau menghapusnya).



![screen](assets/fr/26.webp)




## Menerima bitcoin



![video](https://youtu.be/cqv35wBDWMQ)



Untuk menerima bitcoin di wallet Anda di Ginger Wallet:




- tekan **Terima** ;



![screen](assets/fr/27.webp)





- Masukkan nama sumber yang ingin Anda kaitkan dengan alamat tersebut. Ini adalah pelabelan untuk melacak pembayaran Anda. Ini tidak memiliki implikasi on-chain; ini hanyalah informasi penelusuran yang disimpan secara lokal dalam aplikasi Anda;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klik tanda panah kecil di sebelah kiri **Generate** untuk memilih format alamat Anda (**SegWit** / **Taproot**), lalu klik **Generate**, untuk generate alamat dan kode QR.



![screen](assets/fr/29.webp)



Alamat atau kode QR ini akan digunakan oleh pengirim untuk mengirimkan bitcoin kepada Anda.



![screen](assets/fr/30.webp)




## Kirim bitcoin




![video](https://youtu.be/2nf5aAimfhg)



Untuk melakukan ini :




- Tekan tombol **Kirim**;
- masukkan alamat penerima, jumlah yang akan dikirim dan label;
- periksa ikhtisar transaksi dan konfirmasi untuk mengirim.



![screen](assets/fr/31.webp)




## Membelanjakan bitcoin



Sangat mudah untuk membeli dan menjual Bitcoin dengan Ginger Wallet. Hanya dalam beberapa langkah, Anda bisa membelanjakan bitcoin Anda.



### Beli bitcoin



![video](https://youtu.be/lEqTBzm5MEA)



Pengguna Ginger Wallet dapat membeli bitcoin.





- Tekan tombol **Beli**. Tombol ini tetap terlihat meskipun wallet kosong.



![screen](assets/fr/32.webp)





- Pilih negara Anda, atau bahkan negara bagian Anda (di beberapa wilayah, seperti Kanada), sebelum melanjutkan pembelian bitcoin. Bahkan, ketika Anda mengklik fungsi **Buy** untuk pertama kalinya, Anda juga harus menentukan wilayah Anda.



![screen](assets/fr/33.webp)



Tekan **Lanjutkan** untuk melanjutkan proses pembelian.





- Kemudian masukkan jumlah bitcoin yang ingin Anda beli di kolom khusus. Anda juga bisa memilih mata uang transaksi.



![screen](assets/fr/34.webp)



Setiap mata uang memiliki batas pembelian minimum dan maksimum. Misalnya, dalam USD, batas maksimumnya adalah $30.000.



Jika Anda telah melakukan pembelian, Anda dapat melihat riwayat transaksi Anda dengan mengklik tombol **Pesanan sebelumnya**. Daftar transaksi sebelumnya dan statusnya akan ditampilkan.





- Pilih penawaran yang tepat untuk Anda.



Pada titik ini, Anda akan melihat daftar semua penawaran yang tersedia. Untuk setiap penawaran, Anda memiliki :




 - nama pemasok (1) ;
 - jumlah bitcoin yang setara dengan jumlah yang dimasukkan sebelumnya, metode pembayaran dan biaya pembelian (2);
 - tombol **Terima** (3).



![screen](assets/fr/35.webp)



Biaya yang tertera dalam penawaran bukan merupakan biaya tambahan. Biaya-biaya tersebut sudah termasuk dalam jumlah total penawaran.



Sudut kanan atas layar, berlabel **Semua**, memungkinkan Anda memfilter penawaran berdasarkan metode pembayaran. Metode pembayaran yang Anda pilih akan ditetapkan secara default, tetapi dapat diubah kapan saja.



![screen](assets/fr/36.webp)



Jika Anda menemukan penawaran yang sesuai, klik tombol **Terima** untuk melanjutkan pembelian. Anda akan diarahkan ke halaman penjual, di mana Anda dapat menyelesaikan transaksi.



### Menjual bitcoin



Pengguna Ginger Wallet dapat menjual Bitcoin. Tombol **Jual** hanya akan terlihat jika ada dana yang tersedia dalam portofolio.





- Klik **Jual**.



![screen](assets/fr/37.webp)





- Seperti halnya opsi **Beli**, ketika Anda menggunakan fungsi Jual untuk pertama kalinya, Anda harus memilih negara Anda sebelum melanjutkan penjualan bitcoin.





- Selanjutnya, Anda perlu memasukkan jumlah Bitcoin yang ingin Anda jual. Anda bisa memasukkan jumlah ini dalam BTC atau mata uang fiat seperti dolar AS (USD).





- Setelah Anda selesai melakukannya, Anda akan melihat daftar penawaran yang tersedia. Pilih penawaran penjualan yang sesuai untuk Anda, lalu klik **Terima** untuk melanjutkan.





- Sekarang Anda perlu menyelesaikan transaksi:
 - Setelah Anda menerima penawaran, Anda akan diarahkan ke halaman pemasok;
 - Ikuti petunjuk pada halaman pemasok ;
 - Pada titik tertentu, Anda akan menerima alamat penerima dan jumlah yang harus dikirim;
 - Kemudian kembali ke Ginger Wallet untuk melanjutkan proses;
 - Setelah kembali ke Ginger Wallet, kotak dialog akan muncul, memungkinkan Anda untuk melanjutkan dengan mengeklik **Kirim**.



Ini akan membuka layar **Kirim** dengan alamat penerima dan jumlah yang telah diisi sebelumnya. Anda juga dapat menggunakan tombol **Kirim** pada layar beranda. Meskipun Anda dapat mengirim transaksi secara manual, kami sarankan Anda menyelesaikannya melalui kotak dialog untuk proses yang lebih optimal.



## Membuat coinjoin pada Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Lindungi kerahasiaan bitcoin Anda dengan **Coinjoin**, yang terintegrasi langsung ke dalam Ginger Wallet. wallet menggunakan **WabiSabi**, protokol coinjoin Chaumian yang dirancang untuk memfasilitasi coinjoin yang lebih mudah diakses dan efisien.



Terserah Anda untuk memilih strategi coinjoin (otomatis atau manual) yang paling sesuai untuk Anda.



Ginger Coinjoin siap digunakan segera setelah Anda mengunduhnya (tidak ada langkah tambahan yang diperlukan). Secara otomatis, Ginger Coinjoin berjalan di latar belakang untuk melindungi privasi Anda dengan setiap transaksi. Dalam praktiknya, pemutar Coinjoin akan muncul setiap kali Anda memiliki saldo yang dapat dianonimkan.



Sedangkan untuk memulai coinjoin secara manual, ini adalah operasi satu klik. Mulai putaran dan tunggu hingga transaksi coinjoin dibuat dan dikonfirmasi. Anda akan melihat skor anonimisasi di antarmuka.



Beberapa campuran dapat dilakukan sampai tingkat anonimitas yang diinginkan tercapai. Anda juga dapat mengecualikan bagian tertentu dari campuran.



Secara default, Ginger menggunakan koordinatornya sendiri dengan semua parameter yang telah dikonfigurasi sebelumnya dan biaya yang dijamin. Coinjoin token yang bernilai lebih dari 0,03 BTC dikenakan biaya koordinator 0,3% sebagai tambahan dari biaya mining. Entri 0,03 BTC atau kurang, serta remix, dibebaskan dari biaya koordinator, bahkan setelah satu transaksi. Oleh karena itu, pembayaran yang dilakukan dengan dana Coinjoin memungkinkan pengirim dan penerima untuk mencampur koin mereka tanpa dikenakan biaya koordinator.



Ginger lebih memilih coinjoin dengan lebih banyak peserta daripada putaran yang lebih kecil dan lebih cepat. Coinjoin yang lebih besar menawarkan lebih banyak anonimitas, biaya yang lebih rendah, dan efisiensi ruang blok yang lebih besar.




## Keselamatan dan praktik terbaik



Keinginan untuk desentralisasi dan pelestarian privasi memerlukan adopsi beberapa praktik terbaik:




- Selalu simpan seedphrase Anda di tempat yang aman di luar jaringan;
- Jika Anda kehilangan komputer atau mencurigai adanya akses yang tidak sah, segera buat wallet yang baru. Transfer dana Anda ke portofolio baru ini dan hapus portofolio lama;
- Gunakan alamat yang berbeda untuk setiap resepsi untuk menghindari penggunaan ulang alamat;
- Selalu unduh aplikasi portofolio Anda secara eksklusif dari akun GitHub resmi atau situs web resmi.



Sekarang Anda sudah terbiasa menggunakan aplikasi Ginger Wallet untuk mengirim, menerima, dan membelanjakan bitcoin Anda.



Jika Anda merasa tutorial ini bermanfaat, silakan tinggalkan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini melalui platform media sosial Anda. Terima kasih banyak!



Saya juga menyarankan Anda untuk melihat tutorial ini tentang cara menggunakan aplikasi komputer Liana untuk mengirim dan menerima bitcoin, serta mengimplementasikan rencana real estat otomatis.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04