---
name: Braiins Mini Miner
description: Membuat Mining dengan mudah dari rumah.
---
![cover](assets/cover.webp)



## Pendahuluan



Mini Miner braiins BMM 100 adalah produk yang diciptakan oleh Mining pool Braiins. Perangkat ini memiliki desain yang menarik dan sangat senyap. Perangkat ini menghasilkan daya komputasi sebesar 1,1 Th/s dan mengkonsumsi daya sekitar 40 watt. Tidak seperti perangkat lain, perangkat ini bukan open source, tetapi sangat mudah dipasang, hanya perlu beberapa klik saja! Mini Miner BMM 100 adalah versi pertama yang dirilis. Sekarang versi 2 sedang diproduksi, yang disebut BMM 101, yang berbeda dari yang pertama karena memiliki layar yang lebih besar dan adanya Wi-Fi, tetapi prosedur pemasangannya sama.



Anda juga dapat menemukan informasi yang jauh lebih penting dengan membaca panduan lengkap secara langsung di [situs produsen](https://braiins.com/hardware/mini-Miner-bmm-100).



## Gambaran umum tentang BMM 100



perangkat terlihat seperti paralelepiped dengan layar di bagian depan



![image](assets/en/01.webp)



kipas angin di sisi atas



![image](assets/en/02.webp)



sementara di sisi belakang terdapat: lubang untuk daya, ruang untuk kartu SD (yang mungkin diperlukan untuk pembaruan apa pun), tombol kecil bertuliskan `IP REPORT` yang memungkinkan Anda mengetahui IP Address mini Miner, yang mana Address diperlukan untuk mengakses dasbor perangkat. Setelah tombol ditekan, IP Address akan ditampilkan selama sekitar 5 detik, kemudian menghilang dan layar yang telah diatur muncul kembali. Namun, jika Anda perlu mengubah beberapa pengaturan, cukup tekan tombol yang dimaksud sekali lagi dan IP Address akan muncul kembali di layar. Melanjutkan daftar, kami menemukan port Ethernet dan akses untuk melakukan pengaturan ulang perangkat, di mana Anda perlu mengambil pin dan menahannya selama 10 detik untuk mengatur ulang semua pengaturan mini Miner. Akhirnya kami menemukan dua lampu indikator, satu Green dan satu merah, yang menunjukkan kepada kami status Miner.



![image](assets/en/03.webp)



## Menghubungkan Mini Miner



Anda perlu menghubungkan perangkat ke internet melalui ethernet, namun dengan versi baru (BMM 101) hal ini tidak diperlukan lagi. Kembali ke mini Miner ini, setelah kita menemukan lokasi, kita perlu menghubungkannya terlebih dahulu ke jalur internet dan kemudian ke daya: perangkat akan secara otomatis menyala dan menampilkan IP Address di layar.



## Konfigurasi



Kita perlu membuka peramban dan memasukkan IP Address yang menunjukkan mini Miner di bilah pencarian. Saya ingatkan Anda bahwa untuk menemukan perangkat di jaringan, Anda harus berada di jaringan lokal, jadi komputer yang Anda gunakan harus terhubung ke jaringan yang sama dengan mini Miner. Setelah kita memasukkan IP Address, kita tekan enter dan halaman login ke sistem operasi mini Miner, yaitu Braiins OS, akan muncul di layar.



![image](assets/en/06.webp)



Untuk masuk, Anda harus memasukkan `root` sebagai nama pengguna Anda, sementara kata sandi dapat Anda kosongkan. Klik login dan dasbor mini Miner Anda akan muncul.



![image](assets/en/07.webp)



## Pengaturan umum



Mari masuk ke Sistem



![image](assets/en/24.webp)



di dalam pengaturan, kami menemukan beberapa pengaturan umum seperti tema (terang atau gelap), bahasa, zona waktu, dan perubahan kata sandi.



![image](assets/en/25.webp)



Jika kita masuk ke "Mini Miner Screen", kita akan mendapatkan pengaturan mini Miner, seperti tampilan layar. Kita bisa memilih apakah akan menampilkan waktu, atau harga Bitcoin, atau layar dengan informasi status mesin seperti produk Hash, suhu, watt yang dikonsumsi, dan sebagainya. Di sini terserah Anda untuk memilih apa yang ingin Anda lihat di layar; kita juga dapat mengubah kecerahan layar, mengatur mode malam, dan menampilkan waktu dengan format 12 jam atau 24 jam.



![image](assets/en/26.webp)



Setelah Anda membuat perubahan, klik `Simpan Perubahan` dan Anda akan melihat perubahan pada layar perangkat Anda



![image](assets/en/27.webp)



## Koneksi ke Mining pool



Sekarang kami belum beroperasi, karena kami harus terhubung ke pool untuk memulai Mining, jadi kami harus pergi ke "Konfigurasi"



![image](assets/en/08.webp)



dan entri pertama hanya `Pools`.



![image](assets/en/09.webp)



Di sini kita harus memutuskan kolam mana yang akan digunakan. Dalam tutorial ini saya akan menunjukkan kepada Anda dua opsi. Yang pertama adalah menghubungkan kita ke Mining pool Braiins yang juga digunakan oleh para penambang profesional, seperti yang dapat Anda lihat di tutorial ini:



https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Pilihan kedua adalah menghubungkan kita ke Mining pool yang mina di solo, seperti Kolam Renang Umum, ikuti panduan ini untuk melakukannya:



https://planb.academy/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Kolam renang Braiins



Untuk terhubung ke pool ini kita perlu membuat akun. pool ini juga melakukan pembayaran menggunakan Lightning Network, sehingga kita akan dapat menerima beberapa Sats per hari. Untuk melakukan ini, kita perlu membuat sebuah Address untuk menerima hadiah. Jika Anda tidak tahu cara membuat akun di braiins pool atau cara mengatur petir Address Anda, Anda dapat mengikuti panduan ini:



https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Setelah selesai, kita berada di dasbor pool Braiins. Yang harus kita lakukan adalah memberi tahu pool bahwa kita ingin terhubung dengan salah satu Penambang kita, jadi di sisi kiri layar Anda akan menemukan sejumlah entri. Kita harus pergi ke "pekerja."



![image](assets/en/04.webp)



dan kita perlu mengklik tombol ungu di sebelah kanan yang bertuliskan "Hubungkan pekerja."



![image](assets/en/05.webp)



Ini dia jendela yang berisi informasi yang kita perlukan untuk menghubungkan mini Miner ke kolam renang. Di sini satu-satunya perubahan yang dapat kita lakukan adalah memilih Stratum V2. Untuk mengetahui apa itu Stratum v2, lihat entri ini di [glosarium] (https://planb.academy/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Sekarang kita perlu menyalin string yang dimulai dengan stratumv2. Jadi kita klik pada simbol "salin" kecil, lalu kita masuk ke dasbor mini Miner yang telah kita tinggalkan di konfigurasi dan pool. Kita klik pada tambahkan pool baru



![image](assets/en/11.webp)



dan tempelkan string yang telah kita salin ke dalam ruang di bawah URL Pool.



![image](assets/en/12.webp)



Sekarang kita perlu menambahkan nama pengguna dan kata sandi. Mari kita kembali ke dasbor kolam renang. Di bawahnya kita juga memiliki userID dan kata sandi. UserID dan nama pengguna kita, yang kita berikan saat membuat akun, ditambah nama Miner yang ingin kita masukkan. Anda dapat memutuskan apakah akan memberikan nama pada perangkat yang Anda sambungkan ke pool atau tidak, ini opsional, tetapi disarankan untuk memasukkannya, jadi jika Anda menghubungkan beberapa perangkat, akan lebih mudah untuk mengidentifikasinya dengan segera. Jika Anda tidak ingin memasukkan apa pun, Anda dapat membiarkan `nama pekerja`.



![image](assets/en/13.webp)



Kita kemudian masuk ke mini Miner dan memasukkan nama pengguna. Di sini kita akan memasukkan "finalstepbitcoin" yang merupakan userID saya, miniminer dot. Ini adalah nama yang saya putuskan untuk diberikan pada perangkat. Jika Anda tidak ingin menamainya, tulis saja userid dot nama pengguna. Dalam kasus saya, nama pengguna saya adalah finalstepbitcoin.workername. Setelah Anda memasukkan nama pengguna, Anda bisa memilih kata sandi dan menuliskannya di kolom kosong. Anda juga bisa memasukkan anithing123, yang juga ditampilkan di layar pool, tetapi ini hanya untuk menunjukkan bahwa Anda bisa memasukkan kata sandi apa pun yang Anda inginkan.



Setelah Anda memasukkan semua data, Anda harus menekan tombol simpan di sebelah kanan (yang berbentuk seperti floppy disk) dan dengan cara ini Anda telah mengonfigurasi data pool dalam mini Miner.



![image](assets/en/14.webp)



Sekarang Anda harus kembali ke dasbor kolam renang dan klik "Terhubung! Kembali."



![image](assets/en/15.webp)



Kami telah menghubungkan mini Miner kami ke kolam renang braiins! Anda sekarang dapat melihatnya di daftar pekerja. Jika tidak muncul, lakukan penyegaran dan tunggu beberapa saat. Setelah muncul, pastikan statusnya "OK" dengan tanda centang Green.



![image](assets/en/17.webp)



jika Anda kembali ke dasbor, Anda akan mulai melihat pergerakan pada grafik dan melihat Hashrate pada perangkat kami. Ini berarti bahwa kolam menerima pekerjaan kita dan oleh karena itu kita untuk semua maksud dan tujuan merusak.



![image](assets/en/16.webp)



### Kolam Renang Umum



Melalui kolam ini kita bisa mencoba keberuntungan dan menambang sendirian, bersandar pada kolam. Dalam hal ini kita tidak akan menerima hadiah, tetapi kita akan menerima hadiah penuh jika berhasil menambang sebuah blok. Kemudian kita akan terhubung ke pool publik, sebuah pool khusus Mining yang sepenuhnya open source. Kita buka jendela baru pada browser dan pergi ke [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



muncullah sebuah halaman dengan semua informasi yang kita butuhkan. Kami kemudian menyalin di sana strata Address



![image](assets/en/19.webp)



kemudian kita kembali ke dasbor mini Miner kita, masuk ke konfigurasi dan ke pools, klik add new pool (proses yang sama seperti yang terlihat di atas) dan tempelkan 'stratum Address di bawah url pool.



![image](assets/en/20.webp)



Sekarang mari kita kembali ke halaman pool dan melihat bahwa sebagai nama pengguna kita harus memasukkan Bitcoin Address, yang akan menjadi nama yang akan kita terima hadiahnya jika kita merusak sebuah blok, lalu sebuah titik dan kemudian nama perangkat kita, seperti yang telah kita lakukan sebelumnya dengan Braiins Pool, sedangkan kata sandinya dapat kita pilih sendiri.



![image](assets/en/21.webp)



Kita kembali ke mini Miner dan di bawah nama pengguna kita tempelkan Address Bitcoin diikuti dengan titik dan nama, saya akan menaruh `miniminer`. Pada kata sandi, saya akan memasukkan tes, Anda memasukkan apa pun yang Anda inginkan.



![image](assets/en/22.webp)



Sekarang kita menyimpan pengaturan dan menonaktifkan kolam renang Braiins.



![image](assets/en/23.webp)



Bagus! Kita sekarang berada di Mining di kolam renang umum!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)