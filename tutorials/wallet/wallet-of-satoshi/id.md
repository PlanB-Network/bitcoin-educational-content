---
name: Wallet dari Satoshi
description: Kustodian Wallet paling sederhana untuk memulai
---
![cover](assets/cover.webp)

tutorial ini ditulis oleh_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Mengunduh, Menyiapkan, dan Menggunakan Wallet dari Satoshi

Wallet dari Satoshi adalah Lightning Network Wallet, kustodian, dan sangat mudah digunakan.

Untuk keperluan kursus [BTC105 - Menemukan Sekarang] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), voucher ini digunakan untuk Redeem Lightning Network.

**Selalu ingat**: _bukan kuncimu, bukan koinmu_

Dompet kustodian nggak ngasih kamu kendali penuh atas dana kamu. Dompet kayak gini biasanya nggak direkomendasikan, kecuali buat pemula. WoS sebaiknya dipakai sebagai dompet transisi atau tempat nyimpen uang saku, bukan buat akumulasi dana jangka panjang.

---

Wallet of Satoshi (WoS) adalah dompet kustodian, tapi punya reputasi yang cukup baik. Kita bisa pakai alat seperti WoS, misalnya, buat ningkatin kemampuan kita dalam menerima likuiditas. Sementara waktu, kita bisa ngasih ke WoS tugas “pekerjaan kotor” dalam ngatur likuiditas channel buat kita. Setelah jumlah tertentu tercapai, kita bisa mindahin saldo dari WoS ke wallet non-kustodian kita lewat On-Chain.

**WARNING⚠️: Dianjurkan untuk membaca tutorial secara keseluruhan sebelum melanjutkan**

### Mengunduh Wallet dari Satoshi

Buka Play Store dan unduh WoS

![image](assets/it/01.webp)

**Catatan:** WoS hanya dapat diunduh dari toko resmi. Jika sistem operasi perangkat diprogram, sebelum membuka WoS, ada bagian verifikasi oleh OS itu sendiri. Setelah tahap verifikasi, pilih _Open_.

![image](assets/it/02.webp)

Wallet dari Satoshi terbuka dengan layar berikut ini, dan kamu perlu mengklik _Start_

![image](assets/it/03.webp)

### Mendaftarkan Akun untuk WoS

Pada tahap ini, wallet kamu udah berfungsi, tapi demi keamanan yang lebih baik, lanjutkan buat nyiapin login. Ini penting buat bisa memulihkan dana kalau suatu saat perangkat kamu rusak atau hilang. Jadi, pilih menu di bagian kiri atas.

![image](assets/it/04.webp)

Seluruh jendela menu akan terbuka, dan di situ kamu cuma perlu ngatur mata uang (secara default, Wallet of Satoshi nunjukin dolar AS sebagai mata uang utama) dan warna tema (terang atau gelap), sesuai selera kamu. Jangan pakai menu lain dulu.

Karena WoS adalah dompet kustodian, kita nggak bisa nyadangkan wallet pakai seedphrase. Tapi kita bisa ngaktifin fitur pemulihan dana lewat WoS kalau perangkat kita hilang atau nggak dipakai lagi, dengan ngeklik **Login/Daftar.**

Setelah itu bakal muncul jendela yang minta kamu masukin alamat email. Email ini bisa pakai Proton (disarankan), tapi yang penting aktif dan bisa diakses, karena nanti email itu dipakai buat memulihkan dana kalau ponsel kamu hilang, dicuri, atau rusak.

![image](assets/it/08.webp)

Wallet dari Satoshi telah mengirim pesan ke kotak masuk email yang ditunjukkan.

![image](assets/it/09.webp)

Di kotak surat, kita akan menemukan dua kata, yang harus kita masukkan, menulis ulang, di tempat yang disediakan oleh aplikasi.

- jangan aktifkan penerjemah: kata-kata harus tetap dalam bahasa Inggris**
- tulis ulang kedua kata tersebut dengan memperhatikan huruf besar/huruf kecil**

![image](assets/it/10.webp)

Setelah menyalin kedua kata tersebut, klik _OK_.

![image](assets/it/11.webp)

Hasilnya akan berupa gambar yang muncul di bagian atas, dengan simbol tanda centang untuk verifikasi.

![image](assets/it/12.webp)

sementara di bagian pengaturan, bilah _Login/Register_ berwarna merah sekarang menampilkan email pengguna Address.

![image](assets/it/13.webp)

### Menerima Pembayaran

Untuk menerima di WoS, klik _Receive_ dan serangkaian perintah akan muncul.

![image](assets/it/14.webp)

Kamu bisa menerima

- melalui LN-Address **a**
- melalui LN, dengan mengatur Invoice **b**
- on chain (WoS mendukung jaringan Bitcoin tetapi dengan swap kapal selam berbayar) **c**
- dengan memindai kode QR dari LNurl-p **d**

![image](assets/it/15.webp)

### Membuat Invoice

Klik _Receive_ dan pilih perintah dengan simbol Lightning Network.

![image](assets/it/16.webp)

Menu pembuatan Invoice muncul, dan kita klik _Tambahkan Jumlah_ untuk menulis jumlah yang tepat dan menambahkan deskripsi, dalam contoh ini, "Invoice pertama saya".

![image](assets/it/17.webp)

Dengan keyboard, kami menetapkan jumlahnya.

![image](assets/it/18.webp)

untuk kemudian mendapatkan pembayaran Invoice. Pembayaran yang diterima akan muncul seperti ini:

![image](assets/it/19.webp)

### Pengambilan dari POS

Wallet dari Satoshi memiliki fitur default, yang membuatnya sangat cocok untuk pedagang: POS. Mari kita lihat cara mengaktifkannya.

Dari layar utama, pilih menu di kanan atas.

![image](assets/it/20.webp)

Kemudian pilih _Point of Sale_.

![image](assets/it/21.webp)

Dengan rilis terbaru WoS, pastikan untuk memilih _Keypad_.

![image](assets/it/22.webp)

Lalu ketik jumlahnya di keypad, dalam contoh ini sebesar 10 sen atau 118 sats. Tambahkan deskripsi untuk koleksi kamu, misalnya “koleksi keduaku dengan POS”. Setelah itu, tombol hijau besar akan menyala dan tinggal kamu klik.

![image](assets/it/23.webp)

ke generate ke Invoice dan menunjukkannya - misalnya - kepada pelanggan.

![image](assets/it/24.webp)

Pembayaran ini juga ditagih!

![image](assets/it/25.webp)

### Mengirim pembayaran

Kesederhanaan adalah kekuatan layar utama WoS. Untuk membayar Invoice, klik _Kirim_

![image](assets/it/26.webp)

Pada penggunaan pertama kali, WoS meminta izin untuk mengakses kamera

![image](assets/it/27.webp)

Mulai saat ini, kamera akan aktif

![image](assets/it/28.webp)

Dengan membingkai invoice, kita bisa lihat kalau pembayaran sebesar 210 sats sedang diminta. Deskripsinya juga bisa terlihat kalau si penerima menetapkannya. Layar ini berfungsi sebagai ringkasan sekaligus permintaan konfirmasi: WoS “meminta izin” buat ngirim pembayaran, dan kamu bisa nyetujuinya dengan ngeklik tombol hijau *Send.*

![image](assets/it/29.webp)

Ketika pembayaran mencapai tujuannya, WoS akan memberi tahu dengan layar ini

![image](assets/it/30.webp)

Dari layar utama, klik _History_ (tepat di bawah saldo), daftar transaksi akan muncul

![image](assets/it/31.webp)

#### Memulihkan akun WoS

Sekarang kita bakal lihat cara menginstal WoS di perangkat baru. Ini juga berguna kalau ponsel kamu hilang, dicuri, atau udah nggak bisa dipakai lagi. Setelah diinstal ulang, kamu cukup ngulangi proses pendaftaran akun seperti yang tadi dijelasin, dengan satu perbedaan: di bagian akhir, saat diminta masuk pakai email yang udah kamu daftarkan sebelumnya, WoS bakal muncul kayak gini:

![image](assets/it/33.webp)

Sebuah pesan akan muncul ngasih tahu kalau email udah dikirim berisi langkah buat ngaktifin lagi akun kamu. Sekarang buka kotak masuk email kamu.

**PENTING:** buka email itu dari PC atau, kalau nggak bisa, dari perangkat lain yang berbeda dengan perangkat yang mau kamu pakai buat memulihkan akun WoS. Di dalam kotak masuk, kamu bakal nemuin email yang berisi kode QR yang perlu kamu pindai.

![image](assets/it/34.webp)


Setelah kode QR dibingkai, pada halaman utama WoS, akun yang dipulihkan akan muncul, dengan saldo dan riwayat.
