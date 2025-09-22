---
name: Canaan Avalon Nano 3S
description: Mengkonfigurasi ASIC Avalon Anda untuk solomining atau penyatuan Miner
---

![cover](assets/cover.webp)



Dalam tutorial ini, kita akan melihat cara menyiapkan Canaan Avalon Nano 3S, untuk penggunaan Miner yang mudah di rumah.



Hingga saat ini, mesin ASIC (*Sirkuit Terpadu Khusus Aplikasi*) yang secara khusus dirancang untuk melakukan tugas tertentu - dalam hal ini, perhitungan Hash (SHA-256) untuk Miner dari Bitcoin - secara khusus tidak cocok untuk penggunaan rumah tangga. Gangguan kebisingan, panas yang dihasilkan dan kebutuhan untuk menyesuaikan instalasi listrik Anda untuk mendukung daya yang sangat besar dari perangkat ini membuat sebagian besar dari kita tidak dapat mengambil bagian.



Saat ini, Canaan, salah satu produsen mesin ASIC terkemuka, telah memutuskan untuk menangani pasar perorangan yang menginginkan Miner di rumah, dengan menawarkan berbagai produk yang relatif tidak berisik dan sangat mudah dipasang (plug & play).



Perangkat ini dipasarkan sebagai pemanas tambahan dalam kasus **Avalon Nano 3S (140W)**, atau sebagai radiator mini dengan output **800W** dalam kasus **Avalon Mini 3**.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Harap dicatat bahwa perbedaan harga dengan pemanas tradisional dengan daya yang setara, dalam sebagian besar kasus, tidak memungkinkan Anda untuk mendapatkan keuntungan finansial. Satoshi yang dihasilkan oleh aktivitas Mining tidak akan pernah mengimbangi perbedaan harga ini, kecuali jika Anda memiliki akses ke listrik gratis (surplus) atau listrik yang sangat murah.



Menurut pendapat saya, perangkat ini harus dilihat lebih sebagai cara sederhana untuk Miner di rumah bagi mereka yang ingin melakukannya karena alasan pribadi: *mendapatkan Satss non-KYC / memainkan "lotre" dengan menyendiri / berpartisipasi dalam desentralisasi Hashrate dll.*, sambil mendapatkan keuntungan **sebagai bonus** dari panas yang dihasilkan untuk menghangatkan ruangan di musim dingin. Tetapi bukan sebagai cara untuk menghemat uang setidaknya dalam banyak kasus (negara-negara Barat).



## Buka Kotak dan Fitur



Pertama, mari kita lihat apa yang ada di dalam kotak Avalon Nano 3S.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Setelah Anda membuka kotaknya, Anda akan menemukan selongsong karton yang berisi penerima WIFI yang, seperti yang akan kita lihat nanti, harus dicolokkan ke port USB perangkat agar dapat tersambung ke jaringan lokal Anda. Juga disertakan buku petunjuk, dan pin logam untuk mengatur ulang perangkat ke pengaturan pabrik jika perlu.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Setelah semuanya keluar dari kotak, inilah yang ada di tangan: mesin itu sendiri tentu saja, buku petunjuk, penerima WIFI, ujung logam yang disebutkan di atas, dan daya perangkat Supply. Kartu kredit yang disediakan tidak layak disebutkan menurut kami.



![image](assets/fr/05.webp)



Di bawah ini adalah tabel yang merangkum spesifikasi teknis umum Nano 3S :



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Menyalakan dan menyambungkan ke jaringan lokal



Setelah dibongkar, letakkan Avalon Nano 3 S Anda jika memungkinkan di tempat yang relatif terbuka agar panas dapat bersirkulasi. Kemudian mulailah dengan memasukkan modul penerima WIFI kecil seperti yang ditunjukkan di bawah ini:



![image](assets/fr/06.webp)


Kemudian, colokkan colokan USB-C daya Supply ke port USB-C perangkat untuk menyalakannya.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Perangkat akan melakukan booting dan logo Avalon Nano akan muncul di layar, diikuti dengan logo "ponsel" dengan tulisan "Silakan Konfigurasi Jaringan Dengan Aplikasi Avalon Family".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Untuk melakukannya, buka toko aplikasi seluler Anda, cari dan unduh aplikasi **Avalon Family**.



![image](assets/fr/11.webp)


Setelah terinstal, buka aplikasi ini dengan mengeklik "Lewati" di sudut kanan atas, kemudian pada tombol "Tambah" dan terakhir pada "Cari". Pastikan Anda mengaktifkan Bluetooth pada ponsel cerdas Anda, sehingga pendeteksian perangkat berjalan lancar.



![image](assets/fr/12.webp)


Setelah perangkat terdeteksi oleh aplikasi, klik perangkat tersebut dan pilih "Hubungkan". Anda kemudian akan dibawa ke layar di mana Anda dapat memasukkan detail koneksi WIFI Anda.


![image](assets/fr/13.webp)


Setelah perangkat terhubung ke jaringan lokal Anda, layar akan terlihat seperti ini:



![image](assets/fr/14.webp)



Ini menunjukkan Hashrate "fiktif", karena belum ada pool yang dikonfigurasi, dan waktu, tanggal, daya, dan IP perangkat Address - sangat berguna jika Anda ingin mengakses Interface perangkat melalui PC dan browser (lebih lanjut tentang ini nanti).



![image](assets/fr/15.webp)




## Menghubungkan ke Mining pool



**Bagian ini umum pada Nano 3s dan Mini 3, karena prosesnya sama persis**.



Apakah kita ingin "menyendiri" atau "pool" Miner, kita harus terhubung ke Mining pool. Pada kenyataannya, perangkat kita tidak lebih dari sebuah pembuat Hash tanpa mengetahui jaringan Bitcoin. Menghubungkannya ke sebuah pool akan memberinya akses ke jaringan Bitcoin, dan memungkinkannya untuk menerima templat blok untuk dikerjakan.



### Menggunakan aplikasi untuk menyambungkan ke Mining pool



Pada aplikasi Avalon Family, pilih perangkat seperti yang ditunjukkan di bawah ini. Anda kemudian akan secara otomatis diminta untuk mengubah kata sandi administrator mesin. Klik "OK" jika Anda ingin melakukannya, atau batalkan untuk membiarkan kata sandi akses default "admin".


![image](assets/fr/16.webp)


Kemudian pilih "Pengaturan", lalu "Konfigurasi Kolam" dan masukkan parameter untuk 3 kolam yang diminta.


Pool #2 dan #3 akan bertindak sebagai cadangan jika salah satu dari mereka gagal, sehingga Miner Anda tidak akan sia-sia. Secara default, Hashrate akan diarahkan ke pool #1



Dalam kasus kami, kami memilih:




- 1 - Kolam Renang Umum,
- 2 - CkPool,
- 3 - Lautan.



![image](assets/fr/17.webp)



Untuk detail lebih lanjut mengenai cara menghubungkan ke Mining pool, silakan baca tutorial ini:



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Singkatnya, kita membutuhkan





- pool Address, biasanya **stratum+tcp://xxxxxxxx:port**.





- nama "pekerja" yang terdiri dari *Bitcoin Address Anda* dan *pseudo* yang Anda pilih untuk perangkat Anda, keduanya dipisahkan dengan *titik*, misalnya:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- kata sandi, yang biasanya selalu "**x**"



Setelah informasi kolam renang dimasukkan, klik "Simpan".



![image](assets/fr/18.webp)


Nyalakan kembali perangkat sesuai petunjuk, dan tunggu beberapa menit hingga Hashrate Anda mengarah ke kolam pilihan Anda (#1).



### Menggunakan browser untuk menyambung ke Mining pool



Anda juga dapat terhubung ke Mining pool dan, secara umum, mengakses sistem manajemen Interface perangkat Anda melalui browser favorit Anda.



Untuk melakukannya, ketik IP Address dari perangkat yang ditunjukkan pada layar di bawah ini, dalam contoh kami **192.168.144.6** pada bilah pencarian browser



![image](assets/fr/15.webp)



Halaman berikut akan muncul, meminta Anda untuk membuka aplikasi Avalon Family dan memindai kode QR yang ditampilkan dengan aplikasi tersebut.



![image](assets/fr/20.webp)



Buka aplikasi, dan klik 3 garis di kanan atas, lalu pindai. Pindai kode QR peramban, lalu masukkan kata sandi administrator aplikasi dan klik OK.



![image](assets/fr/21.webp)



Di sini Anda berada di halaman web yang memungkinkan Anda berinteraksi dengan Avalon Anda. Ini lebih merupakan dasbor untuk menampilkan metrik mesin, daripada sarana untuk mengonfigurasinya.



Tetapi pengaturan kolam renang masih dapat diakses dengan cara ini, dengan mengklik **"Pool Config "** di pojok kanan bawah.



![image](assets/fr/22.webp)



Dengan cara yang sama seperti pada aplikasi seluler, Anda dapat memasukkan parameter kolam Anda di sini.



![image](assets/fr/23.webp)



## Kontrol perangkat Anda melalui aplikasi Avalon Family



Kami sekarang telah menghubungkan Miner di rumah kami ke jaringan lokal, dan mengarahkan Hashrate kami ke kolam-kolam tambang. Sekarang mari kita temukan fitur-fitur penting dari alat berat kami melalui aplikasi Avalon Family.



Dalam aplikasi keluarga Avalon, klik ikon yang sesuai dengan Avalon Nano 3S.


anda kemudian disajikan dengan 3 menu: "Work Mode", "Light control", dan "Settings". Pertama, klik pada "Work Mode". Anda kemudian akan ditawari 3 mode daya untuk mesin Anda.



**Rendah**: memberi Anda sekitar 3 Th/s Hashrate untuk konsumsi daya 70W


**Sedang**: memberi Anda sekitar 4,5 Th/s dari Hashrate untuk konsumsi daya 100W


**Tinggi**: akan memberi Anda sekitar 6 Th/s Hashrate pada konsumsi maksimum 140W



![image](assets/fr/31.webp)


Mari kita mundur selangkah dan menjelajahi menu "Light Control". Ini murni kosmetik. Tersedia sejumlah besar opsi untuk berbagai warna, intensitas, panas, mematikan LED perangkat di malam hari, dll... Anda bisa mengetahuinya sendiri dengan mudah.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Terakhir, menu terakhir yang tersedia untuk kita adalah menu "Pengaturan" yang telah kita lihat untuk menghubungkan ke kolam Mining kami. Di sini Anda dapat mengelola kolam Anda, mengubah kata sandi administrator perangkat, dan mengamati berbagai metrik seperti tanggal kedaluwarsa garansi, kebersihan filter, atau cara menghubungi dukungan jika terjadi kegagalan.



![image](assets/fr/35.webp)


Untuk perawatan dan menjaga filter sebersih mungkin, kami sarankan untuk menggunakan penyedot debu dan secara teratur menyedot udara masuk dan keluar untuk mencegah penyumbatan.



Kita telah sampai pada akhir tutorial ini, yang telah mengajarkan kita cara menghubungkan Avalon Nano 3 S ke jaringan lokal kita, cara mengarahkan Hashrate ke pool Mining, dan cara menavigasi opsi dan pengaturan menggunakan aplikasi Avalon Family.



Untuk mengetahui lebih lanjut, lihat tutorial kami tentang versi superior Avalon: Mini 3.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7