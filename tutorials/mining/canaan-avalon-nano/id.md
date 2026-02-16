---
name: Canaan Avalon Nano 3S
description: Mengkonfigurasi ASIC Avalon untuk solo mining atau penyatuan Miner
---

![cover](assets/cover.webp)



Dalam tutorial ini, kita akan melihat cara menyiapkan Canaan Avalon Nano 3S, untuk penggunaan Miner yang mudah di rumah.



Hingga saat ini, mesin ASIC (*Sirkuit Terpadu Khusus Aplikasi*) yang secara khusus dirancang untuk melakukan tugas tertentu, dalam hal ini perhitungan hash (SHA-256) untuk Miner Bitcoin, pada dasarnya memang tidak cocok untuk penggunaan di rumah. Kebisingan yang mengganggu, panas yang dihasilkan, dan kebutuhan untuk menyesuaikan instalasi listrik kamu agar mampu mendukung konsumsi daya perangkat ini yang sangat besar membuat sebagian besar dari kita tidak bisa ikut ambil bagian.


Saat ini, Canaan, salah satu produsen mesin ASIC terkemuka, telah memutuskan untuk menangani pasar perorangan yang menginginkan Miner di rumah, dengan menawarkan berbagai produk yang relatif tidak berisik dan sangat mudah dipasang (plug & play).



Perangkat ini dipasarkan sebagai pemanas tambahan dalam kasus **Avalon Nano 3S (140W)**, atau sebagai radiator mini dengan output **800W** dalam kasus **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Harap dicatat bahwa perbedaan harga dibandingkan pemanas tradisional dengan daya yang setara, dalam sebagian besar kasus, tidak memungkinkan kamu mendapatkan keuntungan finansial. Satoshi yang dihasilkan dari aktivitas mining tidak akan pernah menutupi selisih harga ini, kecuali jika kamu memiliki akses ke listrik gratis (surplus) atau listrik yang sangat murah.

Menurut pendapatku, perangkat ini sebaiknya dilihat sebagai cara sederhana untuk mining di rumah bagi mereka yang ingin melakukannya karena alasan pribadi: *mendapatkan sats non-KYC / memainkan “lotre” secara solo / berpartisipasi dalam desentralisasi hashrate dll.,* sambil memperoleh keuntungan **sebagai bonus** dari panas yang dihasilkan untuk menghangatkan ruangan di musim dingin. Namun, perangkat ini bukan solusi untuk menghemat uang, setidaknya dalam banyak kasus (negara-negara Barat).



## Buka Kotak dan Fitur



Pertama, mari kita lihat apa yang ada di dalam kotak Avalon Nano 3S.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Setelah kamu membuka kotaknya, kamu akan menemukan selongsong karton yang berisi penerima WiFi yang, seperti yang akan kita lihat nanti, harus dicolokkan ke port USB perangkat agar bisa tersambung ke jaringan lokal kamu. Selain itu, juga disertakan buku petunjuk serta pin logam untuk mengatur ulang perangkat ke pengaturan pabrik jika diperlukan.


![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Setelah semuanya dikeluarkan dari kotak, inilah yang kamu dapatkan: tentu saja mesin itu sendiri, buku petunjuk, penerima WiFi, ujung logam yang disebutkan sebelumnya, serta power supply perangkat. Kartu kredit yang disertakan menurut kami tidak terlalu layak untuk dibahas.


![image](assets/fr/05.webp)



Di bawah ini adalah tabel yang merangkum spesifikasi teknis umum Nano 3S :




| Fitur                                      | Nilai                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Tingkat Hash                                      | 6 Th/s +- 5%                                            |
| Konsumsi Daya                               | 140 W                                                   |
| Kebisingan                                                | 30 - 40 dB                                              |
| Rentang Suhu Udara Keluaran                 | 60-70°C (pada suhu lingkungan 25°C)                |
| Persyaratan Suhu Ambien untuk Penggunaan | -5 hingga 30°C                                            |
| Rentang Tegangan Input Perangkat                         | 28V 5A berkelanjutan                                          |
| Rentang Tegangan Input Adapter                       | 110-240V AC 50/60Hz                                     |
| Ukuran Perangkat                                 | Panjang: 205 mm / Lebar: 115 mm / Tinggi: 58.5 mm |
| Berat Perangkat                                  | 0.86 kg                                                 |

## Menyalakan dan menyambungkan ke jaringan lokal



Setelah dibongkar, letakkan Avalon Nano 3 S kamu jika memungkinkan di tempat yang relatif terbuka agar panas dapat bersirkulasi. Kemudian mulailah dengan memasukkan modul penerima WIFI kecil seperti yang ditunjukkan di bawah ini:



![image](assets/fr/06.webp)


Kemudian, colokkan colokan USB-C daya Supply ke port USB-C perangkat untuk menyalakannya.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Perangkat akan melakukan booting dan logo Avalon Nano akan muncul di layar, diikuti dengan logo "ponsel" dengan tulisan "Silakan Konfigurasi Jaringan Dengan Aplikasi Avalon Family".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Untuk melakukannya, buka toko aplikasi seluler kamu, cari dan unduh aplikasi **Avalon Family**.



![image](assets/fr/11.webp)


Setelah terinstal, buka aplikasi ini dengan mengeklik "Lewati" di sudut kanan atas, kemudian pada tombol "Tambah" dan terakhir pada "Cari". Pastikan Anda mengaktifkan Bluetooth pada ponsel cerdas kamu, sehingga pendeteksian perangkat berjalan lancar.



![image](assets/fr/12.webp)


Setelah perangkat terdeteksi oleh aplikasi, klik perangkat tersebut lalu pilih "Hubungkan". Kamu kemudian akan dibawa ke layar tempat kamu bisa memasukkan detail koneksi WiFi kamu.

![image](assets/fr/13.webp)


Setelah perangkat terhubung ke jaringan lokal kamu, layar akan terlihat seperti ini:



![image](assets/fr/14.webp)



Ini menampilkan hashrate yang bersifat “fiktif” karena belum ada pool yang dikonfigurasi, serta informasi waktu, tanggal, daya, dan alamat IP perangkat, yang sangat berguna jika kamu ingin mengakses interface perangkat melalui PC dan browser (akan dibahas lebih lanjut nanti).


![image](assets/fr/15.webp)




## Menghubungkan ke Mining pool



**Bagian ini umum pada Nano 3s dan Mini 3, karena prosesnya sama persis**.



Apakah kita ingin melakukan mining secara "solo" atau melalui "pool", kita tetap harus terhubung ke mining pool. Pada kenyataannya, perangkat kita tidak lebih dari sekadar pembuat hash yang tidak mengetahui jaringan Bitcoin. Dengan menghubungkannya ke sebuah pool, perangkat akan mendapatkan akses ke jaringan Bitcoin dan memungkinkan dirinya menerima template blok untuk dikerjakan.


### Menggunakan aplikasi untuk menyambungkan ke Mining pool



Pada aplikasi Avalon Family, pilih perangkat seperti yang ditunjukkan di bawah ini. Kamu kemudian akan secara otomatis diminta untuk mengubah kata sandi administrator mesin. Klik "OK" jika kamu ingin melakukannya, atau batalkan untuk tetap menggunakan kata sandi akses default "admin".


![image](assets/fr/16.webp)


Kemudian pilih "Pengaturan", lalu "Konfigurasi Kolam" dan masukkan parameter untuk 3 kolam yang diminta.


Pool #2 dan #3 akan bertindak sebagai cadangan jika salah satu dari mereka gagal, sehingga Miner kamu tidak akan sia-sia. Secara default, Hashrate akan diarahkan ke pool #1



Dalam kasus kami, kami memilih:




- 1 - Kolam Renang Umum,
- 2 - CkPool,
- 3 - Lautan.



![image](assets/fr/17.webp)



Untuk detail lebih lanjut mengenai cara menghubungkan ke Mining pool, silakan baca tutorial ini:



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Singkatnya, kita membutuhkan





- pool Address, biasanya **stratum+tcp://xxxxxxxx:port**.





- nama "pekerja" yang terdiri dari *Bitcoin Address Anda* dan *pseudo* yang Anda pilih untuk perangkat Anda, keduanya dipisahkan dengan *titik*, misalnya:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- kata sandi, yang biasanya selalu "**x**"



Setelah informasi kolam renang dimasukkan, klik "Simpan".



![image](assets/fr/18.webp)


Nyalakan kembali perangkat sesuai petunjuk, dan tunggu beberapa menit hingga Hashrate Anda mengarah ke kolam pilihan kamu (#1).



### Menggunakan browser untuk menyambung ke Mining pool



Kamu juga bisa terhubung ke mining pool dan, secara umum, mengakses sistem manajemen interface perangkat kamu melalui browser favoritmu.

Untuk melakukannya, ketik alamat IP perangkat yang ditampilkan pada layar di bawah ini, dalam contoh kami 192.168.144.6, ke bilah alamat browser.


![image](assets/fr/15.webp)



Halaman berikut akan muncul, meminta Anda untuk membuka aplikasi Avalon Family dan memindai kode QR yang ditampilkan dengan aplikasi tersebut.



![image](assets/fr/20.webp)



Buka aplikasi, dan klik 3 garis di kanan atas, lalu pindai. Pindai kode QR peramban, lalu masukkan kata sandi administrator aplikasi dan klik OK.



![image](assets/fr/21.webp)



Di sini kamu berada di halaman web yang memungkinkan kamu berinteraksi dengan Avalon kamu. Halaman ini lebih berfungsi sebagai dasbor untuk menampilkan metrik mesin, daripada sebagai sarana untuk mengonfigurasinya.


Tetapi pengaturan kolam renang masih dapat diakses dengan cara ini, dengan mengklik **"Pool Config "** di pojok kanan bawah.



![image](assets/fr/22.webp)



Dengan cara yang sama seperti di aplikasi seluler, kamu bisa memasukkan parameter pool kamu di sini.


![image](assets/fr/23.webp)



## Kontrol perangkat kamu melalui aplikasi Avalon Family



Sekarang kita sudah menghubungkan Miner di rumah ke jaringan lokal dan mengarahkan hashrate kita ke pool mining. Selanjutnya, mari kita lihat fitur-fitur penting dari mesin ini melalui aplikasi Avalon Family.

Di aplikasi Avalon Family, klik ikon yang sesuai dengan Avalon Nano 3S.

Kamu kemudian akan disuguhkan 3 menu: "Work Mode", "Light control", dan "Settings". Pertama, klik "Work Mode". Setelah itu, kamu akan ditawari 3 mode daya untuk mesin kamu.


**Rendah**: memberi kamu sekitar 3 Th/s Hashrate untuk konsumsi daya 70W


**Sedang**: memberi kamu sekitar 4,5 Th/s dari Hashrate untuk konsumsi daya 100W


**Tinggi**: akan memberi kamu sekitar 6 Th/s Hashrate pada konsumsi maksimum 140W



![image](assets/fr/31.webp)


Mari kita mundur selangkah dan menjelajahi menu "Light Control". Menu ini bersifat murni kosmetik. Tersedia banyak opsi untuk berbagai warna, intensitas, suhu warna, mematikan LED perangkat di malam hari, dan lain-lain. Kamu bisa mengeksplorasinya sendiri dengan sangat mudah.


![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Terakhir, menu terakhir yang tersedia untuk kita adalah menu "Settings" yang sebelumnya sudah kita lihat saat menghubungkan ke mining pool. Di sini kamu bisa mengelola pool kamu, mengubah kata sandi administrator perangkat, serta memantau berbagai metrik seperti tanggal kedaluwarsa garansi, kebersihan filter, atau cara menghubungi dukungan jika terjadi kegagalan.


![image](assets/fr/35.webp)


Untuk perawatan dan menjaga filter tetap sebersih mungkin, kami menyarankan untuk menggunakan penyedot debu dan secara rutin menyedot udara masuk dan keluar guna mencegah terjadinya penyumbatan.

Kita telah sampai di akhir tutorial ini, yang mengajarkan kita cara menghubungkan Avalon Nano 3S ke jaringan lokal kita, cara mengarahkan hashrate ke mining pool, serta cara menavigasi berbagai opsi dan pengaturan menggunakan aplikasi Avalon Family.

Untuk mengetahui lebih lanjut, lihat tutorial kami tentang versi Avalon yang lebih tinggi: Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7
