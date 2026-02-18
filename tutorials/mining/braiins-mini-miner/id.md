---
name: Braiins Mini Miner
description: Membuat Mining dengan mudah dari rumah.
---
![cover](assets/cover.webp)



## Pendahuluan



Mini Miner Braiins BMM 100 adalah produk yang diciptakan oleh mining pool Braiins. Perangkat ini memiliki desain yang menarik dan sangat senyap. Perangkat ini menghasilkan daya komputasi sebesar 1,1 Th/s dan mengonsumsi daya sekitar 40 watt. Tidak seperti perangkat lain, perangkat ini bukan open source, tetapi sangat mudah dipasang, kamu hanya perlu beberapa klik saja. Mini Miner BMM 100 adalah versi pertama yang dirilis. Saat ini versi 2 sedang diproduksi, yang disebut BMM 101, dan berbeda dari versi pertama karena memiliki layar yang lebih besar serta dukungan Wi-Fi, tetapi prosedur pemasangannya tetap sama.



Kamu juga dapat menemukan informasi yang jauh lebih penting dengan membaca panduan lengkap secara langsung di [situs produsen](https://braiins.com/hardware/mini-Miner-bmm-100).



## Gambaran umum tentang BMM 100



perangkat terlihat seperti paralelepiped dengan layar di bagian depan



![image](assets/en/01.webp)



kipas angin di sisi atas



![image](assets/en/02.webp)



sementara di sisi belakang terdapat: lubang daya, slot kartu SD yang mungkin diperlukan untuk pembaruan apa pun, serta tombol kecil bertuliskan `IP REPORT` yang memungkinkan kamu mengetahui IP address Mini Miner, di mana address ini diperlukan untuk mengakses dasbor perangkat. Setelah tombol ditekan, IP address akan ditampilkan selama sekitar 5 detik, lalu menghilang dan layar yang telah diatur akan muncul kembali. Namun, jika kamu perlu mengubah beberapa pengaturan, cukup tekan tombol tersebut sekali lagi dan IP address akan muncul kembali di layar. Melanjutkan daftar, kita menemukan port Ethernet dan akses untuk melakukan pengaturan ulang perangkat, di mana kamu perlu menggunakan pin dan menahannya selama 10 detik untuk mengatur ulang semua pengaturan Mini Miner. Terakhir, terdapat dua lampu indikator, satu hijau dan satu merah, yang menunjukkan status Miner.



![image](assets/en/03.webp)



## Menghubungkan Mini Miner



Kamu perlu menghubungkan perangkat ke internet melalui Ethernet, tetapi pada versi baru yaitu BMM 101, hal ini sudah tidak diperlukan lagi. Kembali ke Mini Miner ini, setelah kita menemukan lokasi penempatannya, kita perlu menghubungkannya terlebih dahulu ke jalur internet lalu ke daya. Perangkat akan secara otomatis menyala dan menampilkan IP address di layar.


## Konfigurasi



Kita perlu membuka peramban dan memasukkan IP address yang menunjukkan Mini Miner di bilah pencarian. Aku ingatkan kamu bahwa untuk menemukan perangkat di jaringan, kamu harus berada di jaringan lokal, jadi komputer yang kamu gunakan harus terhubung ke jaringan yang sama dengan Mini Miner. Setelah IP address dimasukkan, kita tekan enter dan halaman login ke sistem operasi Mini Miner, yaitu Braiins OS, akan muncul di layar.



![image](assets/en/06.webp)



Untuk masuk, kamu harus memasukkan `root` sebagai nama pengguna, sementara kata sandi dapat kamu kosongkan. Klik login dan dasbor mini Miner milikmu akan muncul.



![image](assets/en/07.webp)



## Pengaturan umum



Mari masuk ke Sistem



![image](assets/en/24.webp)



di dalam pengaturan, kami menemukan beberapa pengaturan umum seperti tema (terang atau gelap), bahasa, zona waktu, dan perubahan kata sandi.



![image](assets/en/25.webp)



Jika kita masuk ke "Mini Miner Screen", kita akan mendapatkan pengaturan Mini Miner, seperti tampilan layar. Kita bisa memilih apakah akan menampilkan waktu, harga Bitcoin, atau layar dengan informasi status mesin seperti hash rate, suhu, daya yang dikonsumsi, dan sebagainya. Di sini terserah kamu untuk memilih apa yang ingin kamu lihat di layar. Kita juga dapat mengubah kecerahan layar, mengatur mode malam, serta menampilkan waktu dalam format 12 jam atau 24 jam.


![image](assets/en/26.webp)



Setelah kamu membuat perubahan, klik `Simpan Perubahan` dan kamu akan melihat perubahan pada layar perangkat milikmu.



![image](assets/en/27.webp)



## Koneksi ke Mining pool



Sekarang kami belum beroperasi, karena kami harus terhubung ke pool untuk memulai Mining, jadi kami harus pergi ke "Konfigurasi"



![image](assets/en/08.webp)



dan entri pertama hanya `Pools`.



![image](assets/en/09.webp)



Di sini kita harus memutuskan mining pool mana yang akan digunakan. Dalam tutorial ini aku akan menunjukkan kepada kamu dua opsi. Opsi pertama adalah menghubungkan kita ke mining pool Braiins yang juga digunakan oleh para penambang profesional, seperti yang dapat kamu lihat di tutorial ini:


https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Pilihan kedua adalah menghubungkan kita ke mining pool yang melakukan solo mining, seperti Public Pool. Ikuti panduan ini untuk melakukannya:


https://planb.academy/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Pool Braiins



Untuk terhubung ke pool ini, kita perlu membuat akun. Pool ini juga melakukan pembayaran menggunakan Lightning Network, sehingga kamu bisa menerima beberapa sats per hari. Untuk melakukannya, kita perlu membuat sebuah Lightning address untuk menerima hadiah. Jika kamu tidak tahu cara membuat akun di Braiins Pool atau cara mengatur Lightning address kamu, kamu bisa mengikuti panduan ini:


https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Setelah selesai, kita akan berada di dasbor Braiins Pool. Yang perlu kita lakukan adalah memberi tahu pool bahwa kita ingin menghubungkan salah satu miner kita. Jadi, di sisi kiri layar kamu akan menemukan beberapa menu. Kita perlu masuk ke bagian "Workers".


![image](assets/en/04.webp)



dan kita perlu mengklik tombol ungu di sebelah kanan yang bertuliskan "Hubungkan pekerja."



![image](assets/en/05.webp)



Ini dia jendela yang berisi informasi yang kita perlukan untuk menghubungkan mini Miner ke kolam renang. Di sini satu-satunya perubahan yang dapat kita lakukan adalah memilih Stratum V2. Untuk mengetahui apa itu Stratum v2, lihat entri ini di [glosarium](https://planb.academy/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Sekarang kita perlu menyalin string yang dimulai dengan stratumv2. Jadi kita klik pada simbol "salin" kecil, lalu kita masuk ke dasbor mini Miner yang telah kita tinggalkan di konfigurasi dan pool. Kita klik pada tambahkan pool baru



![image](assets/en/11.webp)



dan tempelkan string yang telah kita salin ke dalam ruang di bawah URL Pool.



![image](assets/en/12.webp)



Sekarang kita perlu menambahkan nama pengguna dan kata sandi. Mari kita kembali ke dasbor pool. Di bagian bawah, kita juga akan menemukan userID dan kata sandi. UserID adalah nama pengguna akun kita yang dibuat saat pendaftaran, ditambah dengan nama Miner yang ingin kita daftarkan. Kamu bisa memutuskan apakah ingin memberi nama pada perangkat yang kamu hubungkan ke pool atau tidak. Ini bersifat opsional, tetapi sangat disarankan agar jika kamu menghubungkan beberapa perangkat, akan lebih mudah untuk langsung mengidentifikasinya. Jika kamu tidak ingin mengisi apa pun, kamu bisa membiarkan `nama pekerja` kosong.


![image](assets/en/13.webp)



Kita kemudian masuk ke Mini Miner dan memasukkan nama pengguna. Di sini kita akan memasukkan "finalstepbitcoin", yang merupakan userID aku, lalu miniminer. Ini adalah nama yang aku pilih untuk perangkat ini. Jika kamu tidak ingin menamainya, cukup tulis userID.kata. Dalam kasus aku, nama pengguna yang digunakan adalah finalstepbitcoin.workername. Setelah kamu memasukkan nama pengguna, kamu bisa memilih kata sandi dan menuliskannya di kolom yang tersedia. Kamu juga bisa memasukkan anithing123, seperti yang ditampilkan di layar pool, karena ini hanya contoh untuk menunjukkan bahwa kamu bisa memasukkan kata sandi apa pun yang kamu inginkan.


Setelah kamu memasukkan semua data, kamu perlu menekan tombol simpan di sebelah kanan yang berbentuk seperti floppy disk. Dengan begitu, kamu telah mengonfigurasi data pool di Mini Miner.


![image](assets/en/14.webp)



Sekarang Anda harus kembali ke dasbor kolam renang dan klik "Terhubung! Kembali."



![image](assets/en/15.webp)



Kita telah menghubungkan Mini Miner kita ke pool Braiins. Sekarang kamu sudah bisa melihatnya di daftar workers. Jika belum muncul, lakukan penyegaran dan tunggu beberapa saat. Setelah muncul, pastikan statusnya bertuliskan "OK" dengan tanda centang hijau.


![image](assets/en/17.webp)



Jika kamu kembali ke dasbor, kamu akan mulai melihat pergerakan pada grafik dan melihat hashrate pada perangkat kita. Ini berarti pool sudah menerima pekerjaan kita dan, untuk semua maksud dan tujuan, kita sudah mulai menambang.


![image](assets/en/16.webp)



### Kolam Renang Umum



Melalui pool ini, kita bisa mencoba peruntungan dengan melakukan solo mining sambil tetap bersandar pada pool. Dalam skenario ini, kita tidak akan menerima hadiah reguler, tetapi akan mendapatkan hadiah penuh jika berhasil menambang sebuah blok. Selanjutnya, kita akan terhubung ke public pool, yaitu sebuah mining pool khusus yang sepenuhnya open source. Kita buka jendela baru pada browser dan pergi ke [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



muncullah sebuah halaman dengan semua informasi yang kita butuhkan. Kami kemudian menyalin di sana strata Address



![image](assets/en/19.webp)



kemudian kita kembali ke dasbor mini Miner kita, masuk ke konfigurasi dan ke pools, klik add new pool (proses yang sama seperti yang terlihat di atas) dan tempelkan 'stratum Address di bawah url pool.



![image](assets/en/20.webp)



Sekarang mari kita kembali ke halaman pool dan melihat bahwa sebagai nama pengguna kita harus memasukkan Bitcoin Address, yang akan menjadi nama yang akan kita terima hadiahnya jika kita merusak sebuah blok, lalu sebuah titik dan kemudian nama perangkat kita, seperti yang telah kita lakukan sebelumnya dengan Braiins Pool, sedangkan kata sandinya dapat kita pilih sendiri.



![image](assets/en/21.webp)



Kita kembali ke mini Miner dan di bawah nama pengguna kita tempelkan Address Bitcoin diikuti dengan titik dan nama, aku akan menaruh `miniminer`. Pada kata sandi, aku akan memasukkan tes, kamu memasukkan apa pun yang Anda inginkan.



![image](assets/en/22.webp)



Sekarang kita menyimpan pengaturan dan menonaktifkan kolam renang Braiins.



![image](assets/en/23.webp)



Bagus! Kita sekarang berada di Mining di public pool!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)
