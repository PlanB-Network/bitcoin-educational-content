---
name: COLDCARD - Co-Sign
description: Temukan fitur Co-Sign dan gunakan di COLDCARD Anda
---

![cover](assets/cover.webp)


*NB: Tutorial ini ditujukan untuk orang-orang yang telah memiliki pengalaman dengan dompet multisignature, perangkat Coinkite, dan perangkat lunak seperti Sparrow wallet atau Nunchuk*



![video](https://youtu.be/MjMPDUWWegw)




**Mengapa Tanda Tangan Bersama ColdCard?



Fitur ini memungkinkan Anda menambahkan **ketentuan pengeluaran** ke perangkat ColdCard (Q atau Mk4) dengan cara Modul Keamanan Perangkat Keras (HSM), untuk melindungi dana Anda sekaligus mempertahankan fleksibilitas dan kontrol yang cukup besar terhadapnya.



Kondisi pengeluaran dapat berupa, misalnya:





- Batasan jumlah**: membatasi jumlah bitcoin yang dapat Anda belanjakan dalam satu transaksi.
- Batas kecepatan:** tentukan berapa banyak transaksi yang dapat Anda lakukan per unit waktu (per jam, hari, minggu, dll.), yang membutuhkan jumlah minimum blok di antaranya.
- Alamat yang telah disetujui sebelumnya:** Hanya mengizinkan pengiriman bitcoin ke alamat yang telah disetujui sebelumnya.
- Autentikasi dua faktor:** Memerlukan konfirmasi dari aplikasi seluler 2FA pihak ketiga (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) pada ponsel cerdas/tablet berkemampuan NFC dengan akses internet.



**Bagaimana cara kerjanya



Dengan menambahkan seed kedua ke perangkat ColdCard Mk4 atau Q Anda, yang disebut "Spending Policy Key", yang akan kita sebut di sepanjang tutorial ini sebagai "C Key".


Selain seed tambahan ini, Anda akan diminta untuk Supply setidaknya satu kunci tambahan (XPUB), yang akan kami sebut "Kunci Cadangan", untuk membuat Wallet Multisig 2-on-N.



Singkatnya, kita akan membuat Wallet Multisig, dan perangkat ColdCard Anda akan berisi 2 kunci privat yang diperlukan untuk membelanjakan dana, master seed perangkat dan "Kunci Kebijakan Pembelanjaan".



Setiap kali "C Key" diminta untuk menandatangani, ketentuan pembelanjaan yang telah ditentukan akan berlaku, dan ColdCard hanya akan menandatangani jika transaksi sesuai dengan ketentuan tersebut.



Jika Anda ingin mengabaikan ketentuan pengeluaran ini, Anda dapat melakukannya:




- dengan menandatangani dengan salah satu kunci cadangan dan tangan seed, atau 2 kunci cadangan tergantung pada ukuran Multisig Anda.
- dengan memasukkan "Kunci Kebijakan Pengeluaran" atau "Kunci C" di menu "Tanda Tangan Bersama". **Kunci ini tidak dapat dikonsultasikan secara langsung pada perangkat, jika tidak, siapa pun dapat membatalkan kondisi pengeluaran yang dikonfigurasi.**




## Mengkonfigurasi Tanda Tangan Bersama ColdCard



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktifkan fungsionalitas



Pertama-tama, pastikan perangkat Anda memiliki setidaknya versi firmware terbaru:




- Mk4: v5.4.2
- T: v1.3.2Q




Pada Mk4 atau ColdCardQ Anda, buka *Alat Bantu Lanjutan > Penandatanganan Bersama ColdCard*.



![Co-Sign](assets/fr/01.webp)



*Dalam tutorial berikut ini, tangkapan layar akan diambil pada ColdCardQ untuk kenyamanan, tetapi langkah-langkah dan menu identik antara Mk4 dan Q.*



Rangkuman fungsionalitas ditampilkan.


Terminologi yang digunakan untuk menunjukkan kunci, yang akan kita gunakan lagi dalam Wallet multi-tanda tangan 2-on-3 yang akan kita buat, adalah:



Kunci A = Master kartu dingin seed


Kunci B = Kunci Cadangan


Kunci C = Kunci Kebijakan Pengeluaran



Klik **"MEMASUKKAN "**.



![Co-Sign](assets/fr/02.webp)



Langkah selanjutnya adalah memutuskan kunci pribadi mana yang akan bertindak sebagai "Kunci Kebijakan Pengeluaran" atau "Kunci C".



Kita dapat melihat bahwa kita memiliki beberapa opsi yang terbuka bagi kita:





- Atau tekan **"MASUK "** ke generate untuk membuat kalimat seed baru yang terdiri dari 12 kata.





- Klik **"(1) "** untuk mengimpor seed 12 kata yang sudah ada, atau pilih **"(2) "** untuk mengimpor seed 24 kata yang sudah ada.





- Atau tekan **"(6) "** untuk mengimpor seed dari brankas perangkat Anda.



Untuk keperluan tutorial ini, kami memutuskan untuk mengimpor seed 12 kata yang sudah ada dengan menekan **"(1) "**. Ini bisa berupa seed BIP39 yang sudah Anda miliki, dan tentunya Anda memiliki cadangannya.



Gunakan papan ketik Anda untuk memasukkan 12 kata dari seed Anda. Untuk contoh ini, kita akan memilih frasa valid seed daging sapi x 12. Kemudian tekan **"MEMASUKKAN "**.


*NB: jika Anda tidak memiliki cadangan seed ini, Anda tidak dapat lagi mengubah pengaturan "Co-Sign" pada perangkat Anda, untuk mengubah kondisi pengeluaran Anda*



Fitur "Co-Sign" sekarang sudah diaktifkan pada perangkat. Selanjutnya kita harus memilih kondisi pembelanjaan kita, kemudian menyelesaikan pembuatan Wallet multi-tanda tangan.



![Co-Sign](assets/fr/03.webp)



### 2- Pilih ketentuan pengeluaran atau "*kebijakan pengeluaran*"



Di sini kami menentukan kondisi pengeluaran yang harus dipenuhi ketika **"Kunci C "** atau **"Kunci Kebijakan Pengeluaran**" menandatangani transaksi.



Pada menu **"Penandatanganan Bersama "**, klik **"Kebijakan Pembelanjaan**".



Anda kemudian dapat memilih nilai maksimum, yaitu jumlah maksimum satoshi yang dapat dibelanjakan dalam satu transaksi.



Untuk contoh ini, kita akan memilih besaran maksimum **21212** satoshi. Klik **"ENTER "** untuk mengonfirmasi.




![Co-Sign](assets/fr/04.webp)



Kita kemudian memilih untuk mengatur kecepatan maksimum, yaitu jumlah transaksi yang dapat ditandatangani oleh perangkat per unit waktu. Untuk tutorial ini, kita akan memilih kecepatan tak terbatas, yaitu tidak ada batasan jumlah transaksi.




![Co-Sign](assets/fr/05.webp)



### 3- Buat Wallet Multisig 2-on-N



Kita masih harus memilih kunci ketiga untuk Wallet Multisig kita, yaitu **"Kunci Cadangan "** (Kunci B), di samping **master seed** (Kunci A) dan **"Kunci Kebijakan Pengeluaran "** (Kunci C).



"B Key" kami harus diimpor melalui kartu SD, atau melalui kode QR untuk ColdCardQ.


Untuk melakukan ini, kita memerlukan perangkat ColdCard Mk4 atau Q kedua, di mana "Key B" kita digunakan.



Pada perangkat kedua yang berisi **"Backup Key "**, katakanlah ColdCard Mk4 dalam contoh ini, masuklah dari menu utama ke **"Settings "**, kemudian, **"Multisig Wallet"**, dan terakhir **"Export Xpub "**.


(Jika perangkat kedua Anda adalah ColdCardQ, Anda akan memiliki opsi untuk mengekspor Xpub Anda melalui kode QR, tentu saja).





![Co-Sign](assets/fr/06.webp)





Pada layar berikutnya, masukkan kartu SD dan klik tombol **"validasi "** di kanan bawah. Kemudian klik **"(1) "** untuk menyimpan file pada kartu SD.



File ini akan berisi sidik jari kunci publik (*fingerprint*) dalam namanya, dan akan berbentuk `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Kemudian masukkan kartu SD ke dalam ColdCardQ "awal" untuk mengimpor "Kunci Cadangan" (kunci B).


Pada menu "ColdCard Co-Signing", pilih "Build 2-of-N", lalu pada layar berikutnya klik **"ENTER "**, lalu sekali lagi **"ENTER "** untuk mengimpor "Backup Key" dari kartu SD.



![Co-Sign](assets/fr/08.webp)



Pada layar berikutnya, biarkan "Nomor Rekening" kosong (kecuali jika Anda tahu persis apa yang Anda lakukan) dan klik **"MASUK "** sekali lagi.



![Co-Sign](assets/fr/09.webp)



Akhirnya, kami siap menggunakan Wallet Multisig 2-sur-3 yang baru, yang disusun sebagai berikut:



Kunci A = Coldcard Q master seed


Kunci B = Kunci Cadangan (baru saja diimpor dari perangkat Coldcard kedua)


Kunci C= Kunci Kebijakan Pengeluaran (jika digunakan untuk menandatangani, memberlakukan ketentuan pengeluaran yang telah ditetapkan)



## Tanda Tangan Bersama dengan Sparrow wallet



Jika perlu, bacalah tutorial di bawah ini untuk membiasakan diri Anda dengan perangkat lunak Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Ekspor Wallet Multisig 2-sur-3 ke Sparrow wallet



Kami sekarang perlu mengekspor Wallet Multisig ke Sparrow agar kami dapat menempatkan satoshi pertama kami di sana.



Dari menu utama ColdCardQ Anda, pilih **"Pengaturan "**, lalu **"Dompet Multisig"**.


Kumpulan dompet Multisig yang dikenal dengan ColdCard Anda sekarang ditampilkan, dengan jumlah kunci yang terlibat di sini "2/3" (2-sur3). Pilih Multisig **"ColdCard Co-Sign "** yang baru saja kita buat, lalu klik **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Terakhir, pilih metode yang memungkinkan Anda mengekspor Wallet ke Sparrow. Dalam kasus kami, kami akan memilih kartu SD, lalu klik **"(1) "** setelah memasukkan kartu SD ke dalam slot A pada perangkat.



![Co-Sign](assets/fr/11.webp)



Kemudian di Sparrow wallet, pilih "Impor Wallet".



![Co-Sign](assets/fr/12.webp)



Kemudian klik **"Impor File "**. Kemudian pilih file **"export-Coldcard_Co-sign.txt "** pada kartu SD Anda.



![Co-Sign](assets/fr/13.webp)



Berikan nama pada Wallet Anda seperti yang akan muncul pada Sparrow, dan pilih kata sandi untuk mengenkripsi Wallet Anda (atau tidak).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Kami sekarang siap untuk menerima satoshi pertama kami dan menguji kondisi pengeluaran yang telah kami terapkan pada Wallet kami.



![Co-Sign](assets/fr/16.webp)



### 2- Menguji kebijakan pengeluaran yang telah ditetapkan sebelumnya



Sebagai pengingat, kami telah memutuskan besaran maksimum 21212 satoshi untuk Wallet Multisig kami. Ini berarti bahwa setiap kali Kunci Kebijakan Pembelanjaan (Kunci C) menandatangani transaksi, transaksi tersebut hanya akan valid jika jumlah yang dibelanjakan kurang dari atau sama dengan 21212 satoshi.



Mari kita coba mengujinya.


Pertama, mari kita klik pada tab "Receive" di Sparrow dan jatuhkan beberapa Satss ke Wallet, yang akan kita gunakan di sepanjang tutorial ini.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Kemudian mari kita coba membelanjakan lebih dari 21212 satoshi yang diizinkan dengan mensimulasikan transaksi 50.000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Setelah memindai kode QR yang mewakili transaksi *unsigned* dengan ColdCardQ untuk mengimpor transaksi, berikut ini adalah apa yang akan ditampilkan di layar. Sebuah pesan peringatan akan memberitahu kita bahwa syarat pembelanjaan belum terpenuhi. Jika kita tetap menandatangani transaksi tersebut, maka hanya salah satu dari 2 kunci (master seed di perangkat, tapi bukan "Kunci C") yang akan ditandatangani.




![Co-Sign](assets/fr/23.webp)



Di sini, setelah mengimpor transaksi kita ke Sparrow, kita dapat melihat bahwa hanya satu tanda tangan yang telah diterapkan pada transaksi.



![Co-Sign](assets/fr/24.webp)




Sekarang mari kita ulangi percobaan ini, tetapi untuk transaksi 21.000 satoshi, yaitu kurang dari magnitudo maksimum (21212 Sats) yang kita tetapkan untuk Wallet ini.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Mari kita coba menandatangani transaksi ini dengan ColdCardQ.



Tidak ada masalah kali ini, tidak ada pesan peringatan yang muncul, dan ketika kami mengimpor transaksi yang telah ditandatangani ke Sparrow wallet, kali ini 2 tanda tangan telah diterapkan, sehingga transaksi tersebut valid dan siap untuk didistribusikan.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Tanda Tangan Bersama dengan Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Alamat Web 2FA & Daftar Putih



Dalam paragraf ini, kami akan menggunakan Wallet Multisig Co-Sign dengan Nunchuk, dan mengambil kesempatan untuk menerapkan ketentuan pembelanjaan baru untuk melihat bagaimana hasilnya.



Buka *Alat Bantu Lanjutan > Penandatanganan Bersama ColdCard*.


Kita diminta untuk memasukkan "Kunci Kebijakan Pembelanjaan", untuk mengakses menu yang memungkinkan kita untuk mengubah kondisi pembelanjaan. Dalam kasus kami, kami memasukkan 12 x "daging sapi".



Kami telah memutuskan untuk mempertahankan magnitudo 21212 Sats, dan "Limit Velocity" maksimum untuk alasan praktis yang berkaitan dengan tutorial ini. Di sisi lain, kita akan menggunakan menu **"Alamat Daftar Putih "** untuk menetapkan alamat-alamat di mana dana kita dapat dibelanjakan.




![Co-Sign](assets/fr/31.webp)




Pindai kode QR yang terkait dengan alamat (kami akan memilih 2) yang ingin Anda tambahkan ke daftar putih, lalu klik **"MASUK "**. Setelah memvalidasi alamat Anda dengan menekan **"MASUK "** secara berurutan, kami melihat bahwa batasan Magnitude dan alamat penerima telah diterapkan.



![Co-Sign](assets/fr/32.webp)



Terakhir, untuk mendapatkan gambaran lengkap tentang kemungkinan yang ditawarkan oleh "Co-Sign", mari aktifkan opsi "Web 2FA".


Fitur ini memungkinkan Anda menggunakan aplikasi yang sesuai dengan TOTP RFC-6238 seperti Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / atau Aegis Authenticator, untuk menambahkan keamanan Layer ekstra.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Secara konkretnya, sebelum menandatangani transaksi, Anda harus mendekatkan perangkat yang terhubung dengan NFC dan terhubung dengan internet ke Coldcard. Secara otomatis, Anda akan diarahkan ke halaman web coldcard.com, di mana Anda akan diminta untuk memasukkan kode 6 digit untuk aplikasi Anda. Jika Anda memasukkan kode yang benar, halaman web akan menampilkan kode QR untuk memindai ColdCardQ, atau kode 8 digit untuk dimasukkan ke Mk4 Anda, untuk mengotorisasi perangkat Anda agar dapat ditandatangani.





![Co-Sign](assets/fr/33.webp)



Setelah memindai kode QR yang ditampilkan di aplikasi autentikasi ganda Anda, dan menambahkan akun ColdCard Co-Sign (CCC) Anda, Anda akan diminta untuk memverifikasi bahwa semuanya sudah sesuai dengan memasukkan kode 2FA Anda.



Ketik ColdCard Anda ke bagian belakang perangkat NFC.



![Co-Sign](assets/fr/34.webp)



Pada halaman web yang terbuka, masukkan kode 2FA aplikasi favorit Anda. Kemudian pindai kode QR yang ditampilkan dengan ColdCardQ Anda (atau masukkan kode 8 digit yang ditampilkan di Mk4 Anda).



![Co-Sign](assets/fr/35.webp)




Kami sekarang telah memberlakukan batas pada magnitudo (21212 Sats), alamat tujuan, dan otentikasi ganda.



![Co-Sign](assets/fr/36.webp)



### 2- Ekspor Wallet Multisig 2-on-3 ke Nunchuk



Kali ini, mari kita mengekspor Wallet Multisig 2-on-3 ke dalam Nunchuk, seperti yang kita lakukan pada Sparrow sebelumnya.


Buka *Pengaturan > Dompet Multisig > 2/3: Tanda Tangan Bersama ColdCard > Ekspor ColdCard*.



![Co-Sign](assets/fr/10.webp)



Kali ini, pilih opsi NFC untuk ekspor dengan mengeklik tombol ColdcardQ dengan nama yang sama **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Di Nunchuk, jika Anda membuka aplikasi untuk pertama kalinya, klik **"Pulihkan Wallet yang sudah ada "**.



![Co-Sign](assets/fr/38.webp)



Jika Anda sudah memiliki Wallet dalam aplikasi, klik **"+"** di kanan atas, lalu **"Pulihkan Wallet yang ada "**.



![Co-Sign](assets/fr/39.webp)




Kemudian pilih **"Pulihkan Wallet dari COLDCARD "** lalu **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Terakhir, ketuk bagian belakang ponsel cerdas Anda ke layar ColdCardQ untuk mengimpor Wallet melalui NFC.



![Co-Sign](assets/fr/41.webp)



Akun kami dan satoshi yang sebelumnya disimpan melalui Sparrow wallet telah kembali.



![Co-Sign](assets/fr/42.webp)



### 3- Menguji kebijakan pengeluaran yang telah ditetapkan sebelumnya



Sekarang mari kita coba melakukan transaksi yang melanggar 2 kondisi pembelanjaan yang telah kita tetapkan. **Kita akan mencoba membelanjakan lebih dari 21.212 Sats ke Address yang belum disetujui.** Mari kita coba mengirim 22.222 Sats ke Address secara acak.



![Co-Sign](assets/fr/43.webp)



Setelah transaksi dibuat, klik pada 3 titik kecil di sudut kanan atas untuk mengekspornya ke ColdCard Anda.



![Co-Sign](assets/fr/44.webp)



Kemudian pilih **"Ekspor melalui BBQR "**, dan pindai kode QR yang ditampilkan dengan ColdCardQ Anda.



![Co-Sign](assets/fr/45.webp)



ColdcardQ Anda kemudian menampilkan peringatan yang, saat Anda menggulir ke bagian bawah layar, menjelaskan bahwa transaksi tersebut melanggar ketentuan pembelanjaan, seperti yang diharapkan.



**Perhatikan bahwa perangkat tidak memberi tahu kami kondisi pengeluaran apa saja yang terlibat, untuk mencegah penyerang potensial mencoba menghindari pembatasan.**




![Co-Sign](assets/fr/46.webp)



Jika Anda masih memvalidasi dengan menekan **"ENTER "**, kode QR yang mewakili transaksi yang ditandatangani akan muncul. Jika Anda mengimpornya di Nunchuk, Anda dapat melihat bahwa hanya satu tanda tangan yang telah diterapkan.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Mari kita lakukan operasi yang persis sama, tetapi kali ini dengan transaksi yang menghormati batas besaran (21212 Sats), dan membelanjakan satoshi ke salah satu dari 2 alamat yang telah kita konfigurasikan sebelumnya.



Kami mengirim Nunchuk 12121 Sats ke salah satu dari 2 alamat kami. Kemudian kami mengekspor transaksi ke ColdCard kami seperti yang telah dilakukan sebelumnya.



![Co-Sign](assets/fr/49.webp)




Setelah mengimpor transaksi yang belum ditandatangani ke dalam ColdCardQ, mari kita lihat apa yang akan kita lihat kali ini.



Peringatan selalu ada, tetapi kali ini, dengan menggulir ke bagian bawah layar, kami melihat bahwa ini adalah masalah memvalidasi transaksi melalui 2FA. Perangkat meminta kami mendekatkan ColdcardQ ke terminal NFC yang terhubung ke Internet (smartphone atau tablet), dan kami melakukannya.



![Co-Sign](assets/fr/50.webp)



Sebuah halaman web terbuka di ponsel cerdas kami, meminta kami untuk memasukkan kode 2FA kami, yang kami lakukan berkat Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Kemudian pindai kode QR yang muncul di halaman web, untuk mengesahkan ColdCard Anda untuk menandatangani transaksi.


Transaksi sekarang ditandatangani oleh 2 kunci dan oleh karena itu valid.



Jika "Push Tx" diaktifkan pada ColdCardQ Anda, Anda dapat menyiarkan transaksi secara langsung ke jaringan dengan mengetuk bagian belakang ponsel cerdas Anda.



![Co-Sign](assets/fr/52.webp)




Jika Anda tidak mengaktifkan "Push tx", tekan tombol "QR" pada ColdCardQ Anda untuk menampilkan transaksi yang telah ditandatangani sebagai kode QR, dan mengimpornya ke Nunchuk, dengan cara yang sama seperti pada contoh sebelumnya.



![Co-Sign](assets/fr/53.webp)



Kali ini kami melihat bahwa 2 tanda tangan telah diterapkan, sehingga transaksi siap untuk disiarkan di jaringan Bitcoin.



![Co-Sign](assets/fr/54.webp)




Kita telah sampai pada akhir tutorial ini, yang akan memberi Anda gambaran umum tentang kemungkinan yang ditawarkan oleh fungsionalitas Co-Sign yang diintegrasikan ke dalam perangkat ColdCardQ dan Mk4 Coinkite, serta penggunaannya melalui dompet seperti Sparrow dan Nunchuk.