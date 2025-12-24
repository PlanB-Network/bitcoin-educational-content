---
name: BIP47 - PayNym
description: Gunakan kode pembayaran yang dapat digunakan kembali di Ashigaru
---
![cover](assets/cover.webp)



Kesalahan privasi terburuk yang bisa kamu lakukan di Bitcoin adalah memakai ulang address. Setiap kali address yang sama menerima beberapa pembayaran, transaksi-transaksi itu bakal terhubung, ngasih peta transaksi kamu ke seluruh dunia. Karena itu, sangat disarankan kamu selalu bikin address unik untuk setiap penerimaan. Tapi buat beberapa aplikasi Bitcoin, hal ini nggak selalu mudah.



BIP47, yang diusulkan oleh Justus Ranvier pada tahun 2015, memberi jawaban yang elegan buat masalah ini. BIP ini mengenalkan konsep **kode pembayaran yang bisa dipakai ulang:** sebuah pengenal unik yang memungkinkan pembayaran bitcoin onchain dalam jumlah hampir nggak terbatas untuk diterima tanpa harus memakai ulang sebuah address. Berkat mekanisme kriptografi yang didasarkan pada pertukaran ECDH (*Diffie-Hellman pada kurva elips*), setiap pembayaran ke kode yang sama bakal menghasilkan address baru yang kosong, khusus untuk hubungan antara pengirim dan penerima.


![Image](assets/fr/01.webp)



Prinsip BIP47 ini diimplementasikan secara khusus oleh **PayNym**, sistem yang awalnya dikembangkan oleh Samourai Wallet dan sekarang diambil alih oleh Ashigaru. Dalam tutorial ini, kita bakal lihat cara ngaktifin PayNym kamu, nuker kode pembayaran dengan koresponden, dan ngelakuin transaksi tanpa pakai address.

Aku nggak bakal nmembahas pengoperasian BIP47 secara mendetail di sini. Kalau kamu mau pelajari lebih dalam soal ini, silakan lihat bab 6.6 dari kursus pelatihan BTC 204.


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Prasyarat



Untuk mengikuti tutorial ini, yang kamu perlukan cuma wallet di aplikasi Ashigaru. Kalau kamu belum tahu cara unduh, verifikasi, install aplikasi, atau bikin wallet, aku saranin kamu baca tutorial ini dulu:


https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Minta PayNym



Langkah pertama adalah ngeklaim PayNym kamu. Operasi ini cuma perlu dilakukan satu kali per wallet. Proses ini ngehubungin kode pembayaran BIP47 kamu yang berasal dari seed ('PM...') dengan pengenal unik yang spesifik buat implementasi PayNym. Pengidentifikasi yang lebih pendek dan lebih gampang dibaca ini nantinya bisa kamu kirim ke koresponden buat memudahkan pertukaran, tanpa harus bagi-bagi kode BIP47 yang panjang dan lengkap.

Untuk ngelakuinnya, klik gambar PayNym kamu di kiri atas antarmuka, lalu tekan kode pembayaran 'PM....'



![Image](assets/fr/02.webp)



Kemudian klik pada tiga titik kecil di sudut kanan atas, dan pilih `Klaim PayNym`.



![Image](assets/fr/03.webp)



Konfirmasikan dengan mengklik tombol `KLAIM PAYNYM ANDA`.



![Image](assets/fr/04.webp)



Segarkan halaman: ID PayNym kamu sekarang bakal tampil di bawah gambar kamu, tepat di atas kode pembayaran BIP47 kamu.


![Image](assets/fr/05.webp)



PayNym sekarang sudah aktif dan siap digunakan untuk transaksi BIP47 pertama kamu.



## Terhubung dengan kontak

Ada dua jenis koneksi antara PayNym: **follow** dan **connect.** Operasi 'follow' sepenuhnya gratis. Operasi ini bikin hubungan antara dua PayNym lewat Soroban, protokol komunikasi terenkripsi berbasis Tor yang dikembangin tim Samourai dan diadopsi Ashigaru. Tautan ini memungkinkan dua pengguna yang saling follow buat bertukar informasi secara privat, khususnya buat ngelakuin koordinasi transaksi kolaboratif seperti Stowaway atau StonewallX2, yang bakal kita bahas di tutorial lain. Langkah ini khusus untuk PayNym dan bukan bagian dari protokol BIP47.



![Image](assets/fr/06.webp)


Operasi koneksi ('connect'), di sisi lain, butuh transaksi onchain. Transaksi ini berupa transaksi notifikasi seperti yang didefinisikan di BIP47. Transaksi Bitcoin ini punya metadata di output 'OP_RETURN', yang membentuk saluran komunikasi terenkripsi antara pembayar dan penerima. Dari saluran ini, pembayar bisa generate address penerima yang unik untuk setiap pembayaran, dan penerima bakal dapet notifikasi tentang pembayaran itu, lalu bisa generate private key yang terkait dengan address tersebut buat nanti membelanjakan dana.

Transaksi notifikasi ini punya biaya: biaya mining dan 546 sats yang dikirim ke address notifikasi penerima buat menandai koneksi. Setelah koneksi dibuat, pembayaran dalam jumlah hampir tak terbatas bisa dilakukan lewat BIP47.

Singkatnya:



- follow": gratis, membangun komunikasi terenkripsi melalui Soroban, berguna untuk alat kolaboratif Ashigaru;
- `Hubungkan`: dikenakan biaya, melakukan transaksi notifikasi BIP47 untuk mengaktifkan saluran antara pembayar dan penerima.



Untuk berinteraksi dengan PayNym, kamu harus follow dulu. Ini adalah langkah pertama sebelum bikin koneksi BIP47. Misalnya kamu mau ngirim pembayaran berulang ke PayNym '+instinctiveoffer10'.

Buka halaman PayNym kamu di Ashigaru, lalu klik tombol '+' di bagian kanan bawah antarmuka.



![Image](assets/fr/07.webp)



Kemudian kamu dapat menempelkan kode pembayaran lengkap penerima, atau memindai kode QR mereka.



![Image](assets/fr/08.webp)



Jika Anda hanya memiliki ID PayNym-nya, buka [Paynym.rs](https://paynym.rs/) untuk menemukan kode QR yang terkait dengan kode pembayarannya.



![Image](assets/fr/09.webp)



Setelah kamu memindai kode QR, klik tombol `FOLLOW` untuk mengikuti PayNym.



![Image](assets/fr/10.webp)



Tindakan `FOLLOW` sudah cukup untuk transaksi kolaboratif (*kongkalikong). Namun, untuk mengirim pembayaran BIP47, kamu harus membuat koneksi: klik `HUBUNGKAN` untuk melakukan transaksi notifikasi.



![Image](assets/fr/11.webp)



Notifikasi transaksi kemudian disiarkan di jaringan. Tunggu hingga setidaknya ada satu konfirmasi sebelum melakukan pembayaran pertama.



![Image](assets/fr/12.webp)



## Melakukan pembayaran BIP47



Kamu sekarang udah terhubung dengan penerima dan bisa kirim pembayaran ke address unik yang otomatis dibuat pakai protokol BIP47, tanpa perlu ada pertukaran apa pun dengan penerima.

Dari halaman utama PayNym kamu, klik kontak yang mau kamu kirimi pembayaran.

![Image](assets/fr/13.webp)



Di bagian kanan atas antarmuka, klik ikon panah.



![Image](assets/fr/14.webp)



Masukkan jumlah yang mau dikirim. Kamu nggak perlu masukin address penerima, karena address itu bakal otomatis diturunin pakai protokol BIP47.



![Image](assets/fr/15.webp)



Periksa detail transaksi dengan cermat, termasuk biaya, lalu seret panah hijau di bagian bawah layar untuk menandatangani dan menyiarkan transaksi.



![Image](assets/fr/16.webp)



Transaksi telah terkirim.



![Image](assets/fr/17.webp)



Dalam contoh ini, pembayaran dilakukan ke wallet PayNym aku yang lain. Jadi aku bisa lihat kalau dana itu udah masuk ke Ashigaru wallet aku yang satunya, tanpa ada address yang ditukar secara manual. Cuma pengenal PayNym yang dipakai.


![Image](assets/fr/18.webp)



Kamu sekarang tahu cara menggunakan kode pembayaran yang dapat digunakan kembali BIP47 berkat implementasi PayNym pada aplikasi Ashigaru. Sekarang kamu dapat membagikan kode pembayaran ini kepada siapa saja yang ingin mengirimkan pembayaran kepada kamu (terutama pembayaran berulang). Kamu juga dapat mempublikasikan ID PayNym kamu di situs web atau jejaring sosial kamu untuk menerima donasi.

Untuk memperdalam pengetahuan kamu tentang protokol ini, memahami secara detail cara kerjanya dan implikasinya terhadap kerahasiaan, aku sangat menyarankan kamu mengambil kursus BTC 204-ku:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
