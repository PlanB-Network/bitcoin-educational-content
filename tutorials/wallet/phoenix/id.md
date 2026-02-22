---
name: Phoenix
description: Menginstal dan menggunakan Phoenix Wallet
---
![cover](assets/cover.webp)

Phoenix adalah dompet dan node Lightning kustodian mandiri yang dikembangkan oleh ACINQ, sebuah perusahaan Prancis yang fokus pada solusi perangkat lunak berbasis Lightning. Tidak seperti dompet Lightning kustodian seperti Wallet of Satoshi, di mana bitcoin dipegang oleh pihak ketiga, Phoenix memungkinkan kamu untuk memegang kendali penuh atas kunci pribadi.

Phoenix berfungsi sebagai node Lightning yang sebenarnya yang tertanam di ponsel kamu, secara otomatis membuka saluran dengan node Lightning ACINQ. Aplikasi ini dibangun menggunakan Lightning-KMP, sebuah implementasi lintas platform Lightning Network dalam Kotlin yang dioptimalkan untuk dompet seluler. Tidak seperti solusi node Lightning lainnya, Phoenix sangat menyederhanakan pengelolaan. Kamu tidak perlu menangani pembukaan dan penutupan saluran, menjalankan node Bitcoin, atau mengelola likuiditas di jaringan Lightning. Phoenix menangani semua operasi teknis ini di latar belakang.

Aplikasi ini menggabungkan kemudahan penggunaan dan kenyamanan dompet Lightning seluler dengan keamanan dan kedaulatan node Lightning pribadi yang asli. Phoenix memungkinkan kamu menggunakan Lightning Network dengan aman, efisien, dan mandiri, sambil tetap menikmati pengalaman pengguna yang lancar dan intuitif.

Sebagai imbalannya, dikenakan biaya tertentu:

- Mengirim melalui Lightning dikenakan biaya 0,4% dari jumlah tersebut ditambah 4 sats ;
- Jika uang tunai diperlukan untuk menerima melalui Lightning, maka akan dikenakan biaya sebesar 1% dari jumlah tersebut;
- Setiap saluran membutuhkan biaya 1000 sats untuk dibuka.

Menurut pendapatku, Phoenix merupakan solusi perantara yang sangat baik antara portofolio Lightning kustodian dan manajemen manual dari node Lightning. Aplikasi ini cocok untuk pemula maupun pengguna tingkat lanjut yang memilih untuk tidak berurusan dengan detail pengelolaan LND atau Core Lightning mereka sendiri. Mari kita cari tahu cara menggunakannya!


![Image](assets/fr/01.webp)

## Instal aplikasi

Buka toko aplikasi Anda dan instal Phoenix :


- Di [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet);
- Di [App Store](https://apps.apple.com/fr/app/phoenix-wallet/id1544097028?l=en-GB).

![Image](assets/fr/02.webp)

Kamu juga dapat menginstal aplikasi [dengan file apk di repositori GitHub mereka](https://github.com/ACINQ/phoenix/releases).

![Image](assets/fr/03.webp)

## Pembuatan portofolio

Setelah aplikasi dimulai, klik tombol "*Next*" untuk melewatkan presentasi, kemudian "*Start*".

![Image](assets/fr/04.webp)

Pilih "*Buat dompet baru*".

![Image](assets/fr/05.webp)

Dan itu saja, dompet dan node Lightning kamu sekarang sudah dibuat.

![Image](assets/fr/06.webp)

## Menyimpan frasa mnemonik

Sebelum memulai, kita perlu menyimpan seedphrase 12 kata. Seedphrase ini memberikan akses penuh dan tidak terbatas ke semua bitcoin kamu. Siapa pun yang memiliki seedphrase ini bisa mencuri dana kamu, bahkan tanpa akses fisik ke ponsel kamu.

Seedphrase 12 kata ini akan mengembalikan akses ke bitcoin kamu jika terjadi kehilangan, pencurian, atau kerusakan pada ponsel. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menaruhnya di tempat yang aman.

Kamu bisa menuliskannya di atas kertas atau, untuk keamanan tambahan, mengukirnya di atas baja tahan karat untuk melindunginya dari kebakaran, banjir, atau keruntuhan. Pilihan media untuk seedphrase kamu akan bergantung pada strategi keamanan kamu, tetapi jika kamu menggunakan Phoenix sebagai portofolio pengeluaran yang berisi jumlah yang tidak terlalu banyak, kertas sudah cukup.

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola seedphrase kamu, aku sangat merekomendasikan mengikuti tutorial lainnya, khususnya jika kamu seorang pemula:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Klik pada pesan yang ditampilkan di bagian atas antarmuka "*Save your wallet...*".

![Image](assets/fr/07.webp)

Kemudian klik "*Save my wallet*".

![Image](assets/fr/08.webp)

Kemudian klik "*Lihat kunci saya*" dan simpan frasa mnemonik kamu pada media fisik.

![Image](assets/fr/09.webp)

Centang dua kotak di bagian bawah antarmuka untuk mengonfirmasi bahwa pencadangan telah berhasil diselesaikan.

![Image](assets/fr/10.webp)

## Penyiapan aplikasi

Sebelum melakukan transaksi pertama, kamu bisa menyesuaikan pengaturan dengan mengeklik ikon roda gigi di bagian kiri bawah antarmuka.

![Image](assets/fr/11.webp)

Pada menu "*Display*", Anda bisa memilih tema aplikasi, denominasi yang digunakan untuk bitcoin, dan mata uang fiat lokal kamu.

![Image](assets/fr/12.webp)

Dalam "*Pilihan pembayaran*", kamu akan menemukan berbagai pengaturan lanjutan untuk pembayaran Lightning. Kamu dapat mempertahankan pengaturan default.

![Image](assets/fr/13.webp)

Di "*Manajemen saluran*", tetapkan biaya maksimum yang siap kamu bayarkan saat membuka saluran Lightning.

![Image](assets/fr/14.webp)

Dalam menu "*Access control*", aku sangat menyarankan agar kamu mengaktifkan sistem otentikasi untuk mengamankan akses ke aplikasi di ponsel kamu. Hal ini akan mencegah siapa pun yang memiliki akses ke ponsel kamu yang tidak terkunci untuk mengakses Phoenix dan mencuri bitcoin kamu.

![Image](assets/fr/15.webp)

Pada menu "*Electrum server*", jika Anda memiliki server Electrs, kamu bisa menghubungkannya untuk menyiarkan transaksi kamu.

![Image](assets/fr/16.webp)

Untuk meningkatkan kerahasiaan koneksi kamu, aktifkan koneksi melalui Tor di menu "*Tor*". Meskipun menggunakan Tor mungkin sedikit memperlambat pembayaran kamu, dan mengharuskan aplikasi Phoenix terbuka di latar depan saat menerima, hal ini secara signifikan meningkatkan privasi kamu.

![Image](assets/fr/17.webp)

## Menerima bitcoin secara on-chain

Saat pertama kali digunakan, kamu memiliki opsi untuk mengisi dompet Phoenix kamu dengan dana on-chain. Kamu juga dapat melakukan deposit pertama ini langsung dari Lightning (lihat bagian selanjutnya), tetapi dalam kedua kasus tersebut, biaya tambahan akan dikenakan untuk membuka saluran pertama kamu.

Klik pada tombol "*Terima*".

![Image](assets/fr/18.webp)

Geser kode QR ke kiri untuk menampilkan alamat penerimaan Bitcoin. Kirim jumlah yang ingin kamu depositkan ke Phoenix ke alamat tersebut.

![Image](assets/fr/19.webp)

Jumlah yang diterima secara on-chain akan muncul pertama kali sebagai tertunda di bawah saldo portofolio kamu. Diperlukan 3 kali konfirmasi sebelum dana dapat digunakan.

![Image](assets/fr/20.webp)

Setelah dana diterima, Phoenix secara otomatis membuka saluran Lightning untuk kamu. Sekarang kamu bisa mengirim dan menerima bitcoin melalui Lightning Network.

![Image](assets/fr/21.webp)

## Menerima bitcoin melalui Lightning

Untuk menerima satelit melalui Lightning Network, klik tombol "*Receive*".

![Image](assets/fr/22.webp)

Phoenix menghasilkan faktur Lightning. Kamu dapat memindainya atau mengirimkannya kepada orang yang ingin mentransfer tagihan kepada kamu.

![Image](assets/fr/23.webp)

Dengan mengklik tombol "*Edit*", kamu dapat menambahkan deskripsi yang akan terlihat oleh pembayar pada faktur, dan menentukan jumlah tertentu yang harus dikirim oleh pembayar.

![Image](assets/fr/24.webp)

Faktur klasik yang disebutkan di atas hanya dapat digunakan satu kali. Untuk opsi pembayaran yang dapat digunakan kembali, kamu dapat menggunakan kode QR yang dapat digunakan kembali, yang merupakan penawaran BOLT12.

![Image](assets/fr/25.webp)

Setelah faktur atau penawaran BOLT12 dilunasi, transaksi akan muncul di dompet Lightning kamu.

![Image](assets/fr/26.webp)

## Kirim bitcoin melalui Lightning

Sekarang setelah kamu memiliki satelit di Phoenix, kamu siap untuk melakukan pembayaran melalui Lightning Network. Mulailah dengan mengklik tombol "*Kirim*".

![Image](assets/fr/27.webp)

Beberapa opsi tersedia untuk kamu. Dengan mengklik "*Pindai kode QR*", kamu dapat memindai faktur Lightning, penawaran BOLT12, atau bahkan alamat penerima untuk pembayaran on-chain.

![Image](assets/fr/28.webp)

Kamu juga dapat memasukkan informasi ini secara manual melalui keyboard pada bidang di bagian atas antarmuka, atau memasukkan alamat Lightning (BOLT12 atau LNURL). Kamu juga dapat menempelkan informasi secara langsung menggunakan tombol "*Paste*".

![Image](assets/fr/29.webp)

Dalam contoh ini, aku telah memindai faktur untuk 10.000 sat. Untuk melakukan pembayaran, cukup klik "*Bayar*".

![Image](assets/fr/30.webp)

Transaksi selesai.

![Image](assets/fr/31.webp)

Selamat, kamu sekarang tahu cara mengkonfigurasi dan menggunakan Phoenix. Jika kamu merasa tutorial ini bermanfaat, aku akan berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih telah berbagi!

Untuk melangkah lebih jauh, lihat tutorial tentang Alby Hub ini, solusi inovatif dan mudah digunakan lainnya untuk meluncurkan node Lightning kamu sendiri:

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Dan untuk mengetahui lebih lanjut tentang pengoperasian teknis Lightning Network, kamu dapat menemukan pelatihan gratis yang luar biasa dari Fanis Michalakis di Plan ₿ Academy :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
