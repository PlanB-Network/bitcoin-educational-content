---
name: Ginger Wallet
description: Perangkat lunak Bitcoin wallet yang bersumber terbuka dan mandiri, fork dari Wasabi Wallet, yang mengintegrasikan Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet adalah portofolio Bitcoin sumber terbuka, non-kustodian yang berfokus pada kerahasiaan dan privasi. Ini memulai kehidupan sebagai fork dari Wasabi Wallet (setelah versi 2.0.7.2 - lisensi MIT).



Ginger Wallet mempertahankan arsitektur teknis Wasabi sambil menambahkan beberapa fitur khusus. Menurut [dokumentasi Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi menekankan pada **otonomi dan kontrol**, sementara Ginger berfokus pada **kemudahan penggunaan, keamanan, dan pengalaman yang disederhanakan**, sehingga dapat diakses oleh mereka yang tidak terlalu paham dengan aspek teknis.



Ginger Wallet adalah perangkat lunak wallet untuk komputer saja (tidak ada aplikasi seluler).



## Apa itu Coinjoin?



**coinjoin** adalah struktur transaksi Bitcoin khusus yang menyatukan beberapa peserta dalam satu transaksi kolaboratif. Mekanisme ini menggabungkan input dari beberapa pengguna berbeda ke dalam satu transaksi yang sama, sehingga sangat sulit, bahkan nyaris mustahil jika dilakukan dengan benar, untuk melacak aliran dananya. Hasilnya, hampir tidak mungkin bagi pengamat luar untuk mengidentifikasi secara pasti asal dan tujuan bitcoin yang terlibat, tidak seperti pada transaksi Bitcoin konvensional.

Buat kamu sebagai pengguna, coinjoin membantu menjaga privasi. Misalnya, kalau kamu menerima donasi sebesar 10.000 sats di sebuah alamat Bitcoin, pengirim bisa melacak dana tersebut dan, dalam beberapa kasus, menyimpulkan bahwa kamu punya jumlah bitcoin yang lebih besar atau mengamati aktivitasmu. Dengan melakukan coinjoin setelah menerima 10.000 sats ini, kamu memutus kemampuan pelacakan tersebut: pengirim tidak lagi bisa memperoleh informasi apa pun tentang kamu dari pembayaran ini.

Coinjoin Chaumian menawarkan tingkat keamanan yang tinggi, karena dana tetap berada di bawah kendali eksklusif pengguna setiap saat. Bahkan operator server koordinasi pun tidak bisa mengalihkan bitcoin peserta dalam keadaan apa pun. Baik pengguna maupun koordinator tidak perlu saling percaya: masing-masing tetap memegang kendali atas private key mereka, dan hanya punya wewenang untuk memvalidasi transaksi. Jadi, tidak ada pihak ketiga yang bisa mengambil bitcoin kamu selama coinjoin, atau membuat hubungan langsung antara input dan output milikmu.



Untuk mempelajari lebih lanjut tentang coinjoin, lihat kursus BTC 204 dari Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Pasang Ginger Wallet



Untuk menginstal Ginger Wallet, kunjungi situs web [Ginger Wallet](https://gingerwallet.io).



Tekan **Unduh** untuk mengunduh versi yang tepat untuk komputer kamu (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Pilihan lainnya adalah dengan membuka [GitHub] proyek ini (https://github.com/GingerPrivacy/GingerWallet/releases) untuk mengunduhnya.



![screen](assets/fr/04.webp)



Kemudian jalankan program instalasi.



![screen](assets/fr/05.webp)




## Pengaturan parameter



### Konfigurasi awal



Buka Ginger Wallet, pilih bahasa yang kamu inginkan.



![screen](assets/fr/06.webp)



Sejak awal, Ginger mengingatkan kamu tentang biaya yang terlibat dalam proses coinjoin.



![screen](assets/fr/07.webp)



Kemudian tekan **Mulai**, lalu **Baru** untuk membuat portofolio baru.



![screen](assets/fr/08.webp)



Selanjutnya, simpan dan konfirmasikan seedphrase kamu.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Untuk keamanan tambahan, Ginger Wallet memberi kamu opsi untuk menambahkan passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase ini, setelah ditambahkan, akan diminta setiap kali kamu mencoba mengakses portofolio kamu.



![screen](assets/fr/12.webp)



Ginger secara otomatis mengaktifkan **Coinjoin** secara default saat kamu membuat portofolio. Kamu akan diberi tahu tentang hal ini dan kemudian bisa menyesuaikan pengaturannya sesuai kebutuhanmu.



![screen](assets/fr/13.webp)




### Pengaturan umum



Setelah kamu membuat portofolio pertama, kamu akan dibawa ke antarmuka Ginger Wallet.



![screen](assets/fr/14.webp)



Aktifkan **Mode rahasia**, jika kamu ingin menyembunyikan saldo di dompet.



![screen](assets/fr/15.webp)



Kamu dapat membuat beberapa portofolio pada Ginger Wallet. Cukup klik **Tambahkan portofolio**.



![screen](assets/fr/16.webp)



Ginger mendukung penggunaan portofolio perangkat keras melalui antarmuka Bitcoin Core standar, meskipun integrasi langsung dari atau ke portofolio perangkat keras belum tersedia.



Portofolio perangkat keras yang kompatibel termasuk (tetapi tidak terbatas pada):




- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- dll.



Sekarang klik **Pengaturan**.



![screen](assets/fr/17.webp)



Pengaturan ini adalah pengaturan aplikasi secara umum, dan konfigurasi yang kamu buat di sana akan berlaku untuk semua portofolio.



Dalam **Pengaturan**, kamu memiliki tab :





- Umum**



![screen](assets/fr/18.webp)





- Penampilan



Di tab ini, kamu dapat mengubah bahasa, mata uang, dan unit tampilan biaya (BTC/Satoshi), di antaranya.



![screen](assets/fr/19.webp)





- Bitcoin**



Tab ini memungkinkan kamu mengaktifkan Bitcoin Knots agar berjalan saat aplikasi dijalankan, memilih jaringan yang kamu gunakan (Main/RegTest), serta penyedia fee rate (Mempool Space/Blockstream info/Full Node), dan lain-lain.



![screen](assets/fr/20.webp)





- Fitur keselamatan**



Di tab Keamanan, kamu bisa mengaktifkan autentikasi dua faktor, mengaktifkan atau menonaktifkan Tor, dan bahkan mengaturnya agar dinonaktifkan setelah aplikasi Ginger ditutup.



![screen](assets/fr/21.webp)



**NB** :




- Untuk autentikasi dua faktor, pastikan aplikasi autentikasi kamu mendukung protokol SHA256 dan kode 8 digit. Ginger Wallet memerlukan kode 2FA 8 digit untuk meningkatkan keamanan. Format yang lebih panjang ini membuat kode lebih sulit ditebak atau dikompromikan, sehingga memberi perlindungan lebih besar terhadap akses yang tidak sah.
- Secara default, semua lalu lintas jaringan Ginger melewati Tor, jadi tidak perlu konfigurasi manual. Jika Tor sudah aktif di sistem kamu, Ginger akan otomatis memprioritaskannya.

Tetapi setelah kamu menonaktifkan Tor di pengaturan, privasimu secara umum tetap terjaga, kecuali dalam dua situasi:

- selama Coinjoin, koordinator bisa menghubungkan input dan output kamu ke alamat IP kamu;
- saat menyiarkan transaksi, node berbahaya yang terhubung denganmu bisa mengaitkan transaksi kamu dengan IP kamu.

Jangan lupa tekan **Done** (di sudut kanan bawah) setiap kali untuk menyimpan pengaturan kamu. Beberapa pengaturan mengharuskan Ginger Wallet dihidupkan ulang agar bisa diterapkan.

Selain itu, bilah pencarian di bagian atas portofolio memungkinkan kamu mencari dan mengakses parameter apa pun, dan lain-lain...




![screen](assets/fr/22.webp)




### Konfigurasi portofolio



Beberapa portofolio dapat dibuat dalam aplikasi, sehingga setiap portofolio dapat dikonfigurasikan sesuai dengan kebutuhan kamu. Untuk melakukannya, klik **tiga titik** di depan nama portofolio, lalu **Pengaturan portofolio**.



![screen](assets/fr/23.webp)



Seperti yang bisa kamu lihat, selain parameter wallet, kamu juga bisa melihat UTXO (daftar koin yang kamu miliki), statistik, dan informasi wallet (misalnya extended public key).



Untuk kembali ke konfigurasi portofolio, setelah kamu mengklik parameter portofolio, kamu akan dibawa ke tab berikut:




- Umum** (di mana Anda dapat mengubah nama portofolio);



![screen](assets/fr/24.webp)





- Coinjoin** (di mana kamu dapat menyesuaikan pengaturan coinjoin untuk wallet ini);



![screen](assets/fr/25.webp)





- Tools** (di mana kamu dapat memeriksa seedphrase, menyinkronkan portofolio Anda lagi, atau menghapusnya).



![screen](assets/fr/26.webp)




## Menerima bitcoin



![video](https://youtu.be/cqv35wBDWMQ)



Untuk menerima bitcoin di wallet kamu di Ginger Wallet:




- tekan **Terima** ;



![screen](assets/fr/27.webp)





- Masukkan nama sumber yang ingin kamu kaitkan dengan alamat tersebut. Ini adalah label untuk melacak pembayaran kamu. Ini tidak punya implikasi on-chain; ini hanya informasi penelusuran yang disimpan secara lokal di aplikasi kamu;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klik tanda panah kecil di sebelah kiri **Generate** untuk memilih format alamat kamu (**SegWit** / **Taproot**), lalu klik **Generate**, untuk generate alamat dan kode QR.



![screen](assets/fr/29.webp)



Alamat atau kode QR ini akan digunakan oleh pengirim untuk mengirimkan bitcoin kepada kamu.



![screen](assets/fr/30.webp)




## Kirim bitcoin




![video](https://youtu.be/2nf5aAimfhg)



Untuk melakukan ini :




- Tekan tombol **Kirim**;
- masukkan alamat penerima, jumlah yang akan dikirim dan label;
- periksa ikhtisar transaksi dan konfirmasi untuk mengirim.



![screen](assets/fr/31.webp)




## Membelanjakan bitcoin



Sangat mudah untuk membeli dan menjual Bitcoin dengan Ginger Wallet. Hanya dalam beberapa langkah, kamu bisa membelanjakan bitcoin.



### Beli bitcoin



![video](https://youtu.be/lEqTBzm5MEA)



Pengguna Ginger Wallet dapat membeli bitcoin.





- Tekan tombol **Beli**. Tombol ini tetap terlihat meskipun wallet kosong.



![screen](assets/fr/32.webp)





- Pilih negaramu, atau bahkan negara bagianmu (di beberapa wilayah, seperti Kanada), sebelum melanjutkan pembelian bitcoin. Bahkan, saat kamu mengklik fungsi **Buy** untuk pertama kali, kamu juga harus menentukan wilayahmu.



![screen](assets/fr/33.webp)



Tekan **Lanjutkan** untuk melanjutkan proses pembelian.





- Kemudian masukkan jumlah bitcoin yang ingin kamu beli di kolom khusus. Kamu juga bisa memilih mata uang transaksi.



![screen](assets/fr/34.webp)


Setiap mata uang memiliki batas pembelian minimum dan maksimum. Misalnya, dalam USD, batas maksimumnya adalah $30.000.

Jika kamu sudah melakukan pembelian, kamu bisa melihat riwayat transaksi dengan mengklik tombol **Pesanan sebelumnya**. Daftar transaksi sebelumnya beserta statusnya akan ditampilkan.

- Pilih penawaran yang paling sesuai untuk kamu.

Pada tahap ini, kamu akan melihat daftar semua penawaran yang tersedia. Untuk setiap penawaran, kamu akan melihat:

 - nama pemasok (1);
 - jumlah bitcoin yang setara dengan nominal yang kamu masukkan sebelumnya, metode pembayaran, serta biaya pembelian (2);
 - tombol **Terima** (3).

Setiap mata uang memiliki batas pembelian minimum dan maksimum. Misalnya, dalam USD, batas maksimumnya adalah $30.000.



Jika Anda telah melakukan pembelian, Anda dapat melihat riwayat transaksi Anda dengan mengklik tombol **Pesanan sebelumnya**. Daftar transaksi sebelumnya dan statusnya akan ditampilkan.


- Pilih penawaran yang tepat untuk Anda.



Pada titik ini, kamu akan melihat daftar semua penawaran yang tersedia. Untuk setiap penawaran, kamu memiliki :




 - nama pemasok (1) ;
 - jumlah bitcoin yang setara dengan jumlah yang dimasukkan sebelumnya, metode pembayaran dan biaya pembelian (2);
 - tombol **Terima** (3).



![screen](assets/fr/35.webp)



Biaya yang tertera dalam penawaran bukan biaya tambahan. Biaya tersebut sudah termasuk dalam jumlah total penawaran.

Sudut kanan atas layar, berlabel **Semua**, memungkinkan kamu memfilter penawaran berdasarkan metode pembayaran. Metode pembayaran yang kamu pilih akan ditetapkan secara default, tetapi bisa diubah kapan saja.



![screen](assets/fr/36.webp)



Jika kamu menemukan penawaran yang sesuai, klik tombol **Terima** untuk melanjutkan pembelian. Kamu akan diarahkan ke halaman penjual, tempat kamu bisa menyelesaikan transaksi.

### Menjual bitcoin

Pengguna Ginger Wallet bisa menjual Bitcoin. Tombol **Jual** hanya akan terlihat jika ada dana yang tersedia di portofolio.





- Klik **Jual**.



![screen](assets/fr/37.webp)





- Sama seperti opsi **Beli**, saat kamu menggunakan fungsi **Jual** untuk pertama kalinya, kamu harus memilih negaramu sebelum melanjutkan penjualan bitcoin.

- Selanjutnya, kamu perlu memasukkan jumlah Bitcoin yang ingin kamu jual. Kamu bisa memasukkan jumlah ini dalam BTC atau mata uang fiat seperti dolar AS (USD).

- Setelah selesai, kamu akan melihat daftar penawaran yang tersedia. Pilih penawaran penjualan yang sesuai untuk kamu, lalu klik **Terima** untuk melanjutkan.

- Sekarang kamu perlu menyelesaikan transaksi:
 - Setelah menerima penawaran, kamu akan diarahkan ke halaman pemasok;
 - Ikuti petunjuk di halaman pemasok;
 - Pada tahap tertentu, kamu akan menerima alamat penerima dan jumlah yang harus dikirim;
 - Lalu kembali ke Ginger Wallet untuk melanjutkan proses;
 - Setelah kembali ke Ginger Wallet, kotak dialog akan muncul, memungkinkan kamu melanjutkan dengan mengeklik **Kirim**.

Ini akan membuka layar **Kirim** dengan alamat penerima dan jumlah yang sudah terisi otomatis. Kamu juga bisa menggunakan tombol **Kirim** di layar beranda. Meskipun kamu bisa mengirim transaksi secara manual, kami menyarankan untuk menyelesaikannya melalui kotak dialog agar prosesnya lebih optimal.

## Membuat coinjoin pada Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Lindungi privasi bitcoin kamu dengan **Coinjoin**, yang terintegrasi langsung ke dalam Ginger Wallet. Wallet ini menggunakan **WabiSabi**, protokol coinjoin Chaumian yang dirancang untuk memfasilitasi coinjoin yang lebih mudah diakses dan efisien.

Kamu bebas memilih strategi coinjoin (otomatis atau manual) yang paling sesuai untukmu.

Ginger Coinjoin siap digunakan segera setelah kamu mengunduhnya, tanpa langkah tambahan. Secara otomatis, Ginger Coinjoin berjalan di latar belakang untuk melindungi privasimu pada setiap transaksi. Dalam praktiknya, pemutar Coinjoin akan muncul setiap kali kamu memiliki saldo yang bisa dianonimkan.

Untuk memulai coinjoin secara manual, prosesnya hanya satu klik. Mulai putaran dan tunggu hingga transaksi coinjoin dibuat dan dikonfirmasi. Kamu akan melihat skor anonimisasi di antarmuka.

Beberapa campuran bisa dilakukan hingga tingkat anonimitas yang kamu inginkan tercapai. Kamu juga bisa mengecualikan bagian tertentu dari campuran.

Secara default, Ginger menggunakan koordinatornya sendiri dengan semua parameter yang sudah dikonfigurasi sebelumnya dan biaya yang dijamin. Coinjoin dengan nilai lebih dari 0,03 BTC dikenakan biaya koordinator sebesar 0,3% selain biaya mining. Input sebesar 0,03 BTC atau kurang, serta remix, dibebaskan dari biaya koordinator, bahkan setelah satu transaksi. Karena itu, pembayaran yang dilakukan dengan dana Coinjoin memungkinkan pengirim dan penerima mencampur koin mereka tanpa dikenakan biaya koordinator.

Ginger lebih mengutamakan coinjoin dengan lebih banyak peserta dibanding putaran yang lebih kecil dan cepat. Coinjoin yang lebih besar menawarkan anonimitas lebih tinggi, biaya lebih rendah, dan efisiensi ruang blok yang lebih baik.

## Keselamatan dan praktik terbaik

Keinginan untuk desentralisasi dan menjaga privasi menuntut penerapan beberapa praktik terbaik:

- Selalu simpan seedphrase kamu di tempat yang aman dan offline;
- Jika kamu kehilangan komputer atau mencurigai ada akses tidak sah, segera buat wallet baru. Pindahkan dana kamu ke wallet baru tersebut dan hapus wallet lama;
- Gunakan alamat berbeda untuk setiap penerimaan agar tidak terjadi address reuse;
- Selalu unduh aplikasi wallet kamu hanya dari akun GitHub resmi atau situs web resmi.

Sekarang kamu sudah terbiasa menggunakan aplikasi Ginger Wallet untuk mengirim, menerima, dan membelanjakan bitcoin kamu.

Kalau kamu merasa tutorial ini bermanfaat, silakan tinggalkan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini melalui platform media sosial kamu. Terima kasih banyak!

Aku juga menyarankan kamu untuk melihat tutorial tentang cara menggunakan aplikasi desktop Liana untuk mengirim dan menerima bitcoin, serta mengimplementasikan rencana waris otomatis.




https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
