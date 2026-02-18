---
name: Wallet of Satoshi - Penitipan Mandiri
description: Ketahui cara mengonfigurasi mode penyimpanan mandiri portofolio Wallet of Satoshi
---

![cover](assets/cover.webp)



***Bukan kunci Anda, bukan koin Anda** lebih dari sekadar pepatah, ini adalah prinsip dasar Bitcoin, yang berarti bahwa jika Anda tidak mengontrol **kunci pribadi** yang membuka kunci bitcoin Anda, Anda tidak benar-benar memilikinya.



Banyak pengguna biasanya memulai dengan **custodial wallet**, kemudian bermigrasi ke **self-custodial wallet**, di mana mereka mengontrol kunci pribadi mereka sendiri.


Dalam tutorial ini, kami tidak akan memperkenalkan Anda pada wallet kustodian mandiri yang baru. Sebaliknya, kami akan memperkenalkan Anda pada fitur baru ***Wallet of Satoshi*** wallet: **mode kustodian mandiri**.



Tujuan dari integrasi baru ini adalah untuk memungkinkan pengguna untuk mempertahankan kendali atas private key mereka sambil mendapatkan manfaat dari kesederhanaan dan pengalaman pengguna yang lancar.



Sebelum kita masuk ke inti permasalahan, mari kita luangkan waktu sejenak untuk memeriksa mode pengamanan diri khusus yang ditawarkan oleh Wallet of Satoshi (WoS).



## Fitur khusus dari mode self-dustody



Kesederhanaan dan kelancaran mode penyimpanan mandiri WoS menghilangkan kerumitan dalam membuka saluran Lightning, mengelola node... Tetapi bagaimana ini mungkin?



Mode penyimpanan mandiri Wallet of Satoshi didukung oleh **Spark**. Ini adalah solusi Layer 2 untuk Bitcoin, yang dibuat oleh Lightspark, menggunakan teknologi **statechains**.



Akibatnya, Anda tidak melakukan transaksi secara langsung di Lightning Network. Interaksi antara jaringan **LN** dan **Spark** terjadi melalui **pertukaran atom**.



Sebagai contoh, Bob ingin membayar faktur Lightning menggunakan WoS. Dia mentransfer satoshi-nya, tetapi di latar belakang, ini dialihkan ke **Spark Service Provider (SSP) ** di Spark, yang pada gilirannya mengeksekusi pembayaran di jaringan Lightning.



Sebaliknya, Alice ingin mendapatkan dana secara langsung dari portofolio WoS-nya. Dalam hal ini, **SSP** menerima sats melalui LN dan segera mengkredit portofolio Alice.



Jadi, penting untuk diperhatikan bahwa untuk mendapatkan keuntungan dari kesederhanaan dan kelancaran WoS, Anda harus bergantung pada server Spark. Namun, dalam hal keamanan, jika SSP menjadi berbahaya atau tidak tersedia, Anda memiliki mekanisme **keluar sepihak**, sebuah langkah keamanan yang memungkinkan Anda untuk memulihkan dana Anda di Bitcoin on-chain (meskipun ini bisa jadi lambat dan mahal), menjamin pengalaman kustodian mandiri yang sebanding dengan node Lightning pribadi.



Dengan mempertimbangkan semua parameter ini, Anda kemudian dapat memutuskan berapa banyak sats yang ingin Anda simpan dalam penyimpanan mandiri WoS Anda.



Jika Anda baru mengenal Wallet of Satoshi, Anda tentu saja perlu mengunduh aplikasi seluler wallet. Namun demikian, jika Anda sudah menggunakannya dan ingin mengetahui cara menggunakan **mode self-custody**, silakan langsung ke bagian **Konfigurasi mode self-custody** dalam tutorial ini.



## Memulai dengan Wallet of Satoshi



Buka toko aplikasi Anda dan unduh WoS.



![screen](assets/fr/03.webp)



Buka aplikasi setelah pengunduhan selesai dan tekan **Start**.



![screen](assets/fr/04.webp)



Anda akan diarahkan ke antarmuka utama aplikasi. Bahkan, ketika Anda mengakses WoS untuk pertama kalinya, portofolio sudah berfungsi dan secara sistematis terbuka dalam mode kustodian secara default.



![screen](assets/fr/05.webp)



Meskipun Anda tidak ingin menggunakan WoS dalam mode kustodian, kami sarankan Anda mengonfigurasinya terlebih dahulu. Untuk melakukannya, baca tutorial ini.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Mari kita lanjutkan ke konfigurasi WoS kita dalam penyimpanan mandiri.



## Konfigurasi mode penitipan mandiri



Klik pada menu hamburger (ikon 3 batang) di sudut kanan atas antarmuka utama.



![screen](assets/fr/06.webp)



Kemudian, pada menu yang muncul, klik pada submenu **Open Self Custody Wallet**.



![screen](assets/fr/07.webp)



WoS segera memberi tahu Anda bahwa *mode penjagaan diri dilengkapi dengan frasa pemulihan. Selain itu, Anda bertanggung jawab penuh atas keamanan dana Anda*.



![screen](assets/fr/08.webp)



Centang tombol "**Saya Mengerti**" (1), lalu tekan tombol **Buka Kustodi Sendiri Wallet** (2), yang muncul dalam warna kuning cerah.



![screen](assets/fr/09.webp)



### Membuat portofolio kustodian mandiri



Setelah mengklik tombol **Buka Penitipan Mandiri Wallet**, klik tombol **Buat Wallet Baru**.



![screen](assets/fr/10.webp)



WoS kemudian akan membuat portofolio kustodian mandiri untuk Anda, sekali lagi dalam aplikasi yang sama. Anda akan dapat beralih antara mode **kustodian** (tersedia di wilayah tertentu) dan mode **kustodian mandiri** sesuai keinginan Anda dan kapan saja.



![screen](assets/fr/11.webp)



Setelah dibuat, Anda akan diarahkan ke antarmuka utama penyimpanan mandiri WoS. Anda akan melihat bahwa tidak ada perbedaan antara ikhtisar umum dan antarmuka portofolio penyimpanan WoS dan portofolio penyimpanan mandiri WoS.



### Menyimpan frasa mnemonik Anda



Ketuk ikon **Keychain + Backup Wallet** yang terletak di bagian atas layar di antara nama Wallet of Satoshi dan menu hamburger.



![screen](assets/fr/12.webp)



WoS menawarkan dua cara berbeda untuk menyimpan 12 kata (frasa mnemonik) Anda: **pencadangan melalui Google Drive** dan **pencadangan manual**.



Meskipun kami menyarankan pencadangan manual, yang merupakan yang paling aman, kami juga akan menunjukkan kepada Anda cara mencadangkan melalui Google Drive.



#### Pencadangan melalui Google Drive



Klik tombol **Cadangan Drive Google**.



![screen](assets/fr/13.webp)



Jika Anda memilih untuk mencadangkan dengan Google Drive, ada risiko tinggi bahwa akun Google Anda akan disusupi. Seseorang yang jahat akan memiliki akses ke file yang berisi 12 kata Anda, dan dengan demikian dapat memperoleh akses ke wallet Anda.



Menambahkan kata sandi untuk mengenkripsi file yang berisi 12 kata Anda tentu saja merupakan cara yang baik untuk menambahkan lapisan keamanan ekstra.



Jadi, aktifkan tombol **Enkripsi dengan kata sandi** di opsi lanjutan.



![screen](assets/fr/14.webp)



Pada antarmuka baru yang muncul, tetapkan kata sandi yang kuat, kemudian konfirmasikan lagi.



![screen](assets/fr/15.webp)



Penting untuk diingat bahwa setelah Anda memilih kata sandi, Anda tidak boleh lupa atau kehilangan media tempat Anda menulis kata sandi. Jika Anda lupa atau kehilangannya, Anda tidak akan pernah bisa mengakses 12 kata sandi Anda, dan juga dana Anda.



Setelah memilih kata sandi, pilih akun Google untuk pencadangan, lalu berikan akses yang diperlukan oleh WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Tunggu beberapa detik. Bingo! Pencadangan Anda telah berhasil diselesaikan.



![screen](assets/fr/18.webp)



Anda selalu memiliki opsi untuk membuat cadangan tambahan dengan memilih metode cadangan kedua: cadangan manual.


#### Pencadangan manual



Jika Anda memilih pencadangan manual, kami sangat menyarankan Anda untuk membaca tutorial ini, yang membahas praktik terbaik untuk mencadangkan frasa mnemonik Anda dengan aman, sehingga Anda tidak kehilangan akses ke bitcoin Anda.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tekan tombol **Pencadangan Manual**.



![screen](assets/fr/19.webp)



Pada antarmuka berikut ini, WoS mengingatkan Anda tentang beberapa tindakan pencegahan keamanan yang harus diperhatikan sebelum melanjutkan dengan pencadangan manual.



Aktifkan tombol **Saya mengerti** dan tekan tombol **Selanjutnya**.



![screen](assets/fr/20.webp)



Anda kemudian akan disajikan dengan 12 kata Anda. Simpanlah, lalu klik tombol **Next**.



![screen](assets/fr/21.webp)



Pada antarmuka baru ini, tekan kata-kata dalam urutan yang benar.



![screen](assets/fr/22.webp)



Terakhir, klik tombol **Next**. Selamat! Pencadangan Anda sekarang sudah selesai.



![screen](assets/fr/23.webp)



## Pemulihan portofolio penitipan mandiri



Ketika Anda ingin memulihkan atau mengembalikan penyimpanan mandiri WoS wallet Anda setelah mengganti ponsel atau karena alasan lain, berikut adalah langkah-langkah yang harus diikuti.



Untuk membuka portofolio WoS, klik pada menu hamburger di sudut kanan atas antarmuka utama.


Pada menu yang muncul, klik pada submenu **Open Self Custody Wallet**.


Pada antarmuka baru yang muncul, tekan tombol **Restore Existing Wallet**.



![screen](assets/fr/24.webp)



Pilih metode pemulihan dan lanjutkan ke langkah berikutnya.



![screen](assets/fr/25.webp)



### Pulihkan melalui Google Drive



1. Tekan tombol **Kembalikan Dari Google Drive**.


2. Pilih akun Google dan biarkan WoS mengambil data pemulihan yang tersimpan di Google Drive Anda.


3. Kemudian masukkan kata sandi enkripsi Anda (jika Anda telah menentukannya sebelumnya, tentu saja) dari file yang berisi 12 kata.


4. Tunggu beberapa saat hingga pemulihan diterapkan, dan Anda akan dapat mengakses portofolio Anda lagi.



### Pemulihan manual



1. Tekan tombol **Restore Secara Manual**.


2. Kemudian masukkan 12 kata dari frasa mnemonik Anda, tulis setiap kata di depan angka awalnya.


3. Tunggu beberapa saat hingga pemulihan diterapkan, dan Anda akan dapat mengakses portofolio Anda lagi.




### Mentransfer bitcoin antara penyimpanan WoS dan penyimpanan mandiri WoS



Ketika Anda memiliki bitcoin (sats) di penyimpanan WoS wallet dan membuat penyimpanan mandiri WoS wallet, Anda tidak akan kehilangan dana Anda. Lebih baik lagi, Anda bisa mentransfernya ke portofolio penyimpanan mandiri Anda dan sebaliknya.



Untuk melakukannya:


Anda bisa menyalin alamat penyimpanan mandiri Lightning WoS atau faktur yang Anda buat.



![screen](assets/fr/26.webp)



Sekarang buka tahanan wallet Anda dan tekan tombol **Envoyer**.



Kemudian tempelkan alamat atau faktur. Tekan **Envoyer** untuk kedua kalinya.



Kembali ke portofolio penyimpanan mandiri Anda dan Anda akan melihat bahwa Anda memang telah menerima dana.



![screen](assets/fr/27.webp)



## Mengirim dan menerima bitcoin



Sedangkan untuk mengirim dan menerima bitcoin dalam mode penyimpanan mandiri, sama seperti gambaran umum dan antarmuka, mereka tidak berbeda dengan mengirim dan menerima bitcoin melalui penyimpanan WoS wallet.



Silakan lihat tutorial dasar untuk menggunakan Wallet of Satoshi pada Jaringan Plan₿.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Sekarang Anda dapat mengonfigurasi dan mengoperasikan Wallet of Satoshi sendiri dalam mode self-custody.



Jika Anda merasa tutorial ini bermanfaat, silakan tinggalkan jempol hijau di bawah ini. Terima kasih banyak!