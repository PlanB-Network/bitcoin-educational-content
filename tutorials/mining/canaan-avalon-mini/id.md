---
name: Canaan Avalon Mini 3
description: Mengkonfigurasi ASIC Avalon untuk solomining atau penyatuan Miner
---

![cover](assets/cover.webp)



Dalam tutorial ini, kita akan melihat cara menyiapkan Canaan Avalon Mini 3, untuk penggunaan Miner yang mudah di rumah.



Hingga saat ini, mesin ASIC (*Application-Specific Integrated Circuit*) yang secara khusus dirancang untuk melakukan tugas tertentu - dalam hal ini, perhitungan hash (SHA-256) untuk miner Bitcoin - pada dasarnya memang tidak cocok untuk penggunaan rumahan. Gangguan kebisingan, panas yang dihasilkan, serta kebutuhan untuk menyesuaikan instalasi listrik kamu agar mampu menopang daya yang sangat besar dari perangkat ini membuat sebagian besar dari kita tidak bisa ikut ambil bagian.

Saat ini, Canaan, salah satu produsen mesin ASIC terkemuka, memutuskan untuk menyasar pasar perorangan yang ingin menjalankan miner di rumah, dengan menawarkan berbagai produk yang relatif tidak berisik dan sangat mudah dipasang (plug & play).



Perangkat ini dipasarkan sebagai pemanas tambahan dalam kasus **Avalon Nano 3S (140W)**, atau sebagai radiator mini dengan output **800W** dalam kasus **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Perlu dicatat bahwa perbedaan harga dibandingkan pemanas tradisional dengan daya yang setara, dalam sebagian besar kasus, tidak memungkinkan kamu memperoleh keuntungan finansial. Satoshi yang dihasilkan dari aktivitas mining tidak akan pernah menutupi selisih harga ini, kecuali jika kamu memiliki akses ke listrik gratis (surplus) atau listrik yang sangat murah.


Menurut pendapatKU, perangkat ini harus dilihat lebih sebagai cara sederhana untuk Miner di rumah bagi mereka yang ingin melakukannya karena alasan pribadi: *mendapatkan Satss non-KYC / memainkan "lotre" dengan menyendiri / berpartisipasi dalam desentralisasi Hashrate dll.*, sambil mendapatkan keuntungan **sebagai bonus** dari panas yang dihasilkan untuk menghangatkan ruangan di musim dingin. Tetapi bukan sebagai cara untuk menghemat uang setidaknya dalam banyak kasus (negara-negara Barat).



## Buka Kotak dan Fitur



### Avalon Nano 3S



Pertama, mari kita lihat apa yang ada di dalam kotak Avalon Mini 3.



![image](assets/fr/24.webp)



Ketika KAMU membuka kotaknya, petunjuk pengoperasian langsung ada di depanMU, tetapi yang lebih penting, modul penerima WIFI tersembunyi di bawah stiker putih bundar di sebelah kiri petunjuk pengoperasian. Kamu akan membutuhkannya nanti.



![image](assets/fr/25.webp)



Di bawah blok busa adalah perangkat, kemudian setelah dikeluarkan dari kotaknya, unit daya Supply.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Menyalakan dan menyambungkan ke jaringan lokal



Setelah dibongkar, letakkan Avalon Mini 3 milikmu di tempat yang relatif terbuka, jika memungkinkan, agar panas dapat bersirkulasi dengan baik. Kemudian mulailah dengan memasukkan modul penerima WIFI kecil ke dalam port USB di bagian bawah perangkat, tancapkan daya Supply dan pastikan tombol daya pada posisi "1".



![image](assets/fr/28.webp)



Setelah langkah-langkah ini selesai, layar LED perangkat akan menyala dan menunjukkan simbol "Bluetooth", yang menunjukkan bahwa perangkat siap untuk dihubungkan ke jaringan lokalmu melalui aplikasi Avalon Family.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Untuk melakukannya, buka toko aplikasi seluler, cari dan unduh aplikasi **Avalon Family**.



![image](assets/fr/11.webp)


Setelah terinstal, buka aplikasi ini dengan mengeklik "Lewati" di sudut kanan atas, kemudian pada tombol "Tambah" dan terakhir pada "Cari". Pastikan kamu mengaktifkan Bluetooth pada smartphomemu, sehingga pendeteksian perangkat berjalan lancar.



![image](assets/fr/12.webp)


Setelah perangkat terdeteksi oleh aplikasi, klik perangkat tersebut dan pilih "Hubungkan". Kemudian kamu akan dibawa ke layar di mana kamu dapat memasukkan detail koneksi WIFI.


![image](assets/fr/13.webp)


Setelah terhubung ke jaringan lokal kamu, Mini 3 milikmu akan menampilkan informasi seperti IP Address, waktu, Hashrate dan daya listrik.



Di bawah ini adalah tabel ringkasan spesifikasi teknis umum Mini 3:




| Fitur                                      | Nilai                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Konsumsi Daya                              | 800 W                                                     |
| Kebisingan                                                | 35-55 dB                                                  |
| Temperatur Udara Keluaran                       | 60-70°C (pada suhu lingkungan 25°C)                  |
| Persyaratan Suhu Ambien untuk Penggunaan | -5° C - 40°C                                              |
| Rentang Tegangan Input Perangkat                         | 110V-240V AC 50/60Hz                                      |
| Ukuran Mesin                                 | Panjang: 760 mm / Kedalaman: 104 mm / Tinggi: 214.5 mm |
| Berat Mesin                                  |  8.35 kg                                                  |

## Menghubungkan ke Mining pool



**Bagian ini umum pada perangkat Nano 3s dan Mini 3, karena prosesnya sama persis **



Entah kita ingin melakukan mining secara "menyendiri" atau "pool" miner, kita tetap harus terhubung ke mining pool. Kenyataannya, perangkat kita tidak lebih dari pembuat hash yang tidak memiliki kesadaran terhadap jaringan Bitcoin. Menghubungkannya ke sebuah pool akan memberinya akses ke jaringan Bitcoin, serta memungkinkannya menerima templat blok untuk dikerjakan.



### Menggunakan aplikasi untuk menyambungkan ke Mining pool



Pada aplikasi Avalon Family, pilih perangkat seperti yang ditunjukkan di bawah ini. Kamu kemudian akan secara otomatis diminta untuk mengubah kata sandi administrator mesin. Klik "OK" jika kamu ingin melakukannya, atau batalkan untuk membiarkan kata sandi akses default "admin".


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





- nama "pekerja" yang terdiri dari *Bitcoin Address* dan *pseudo* yang kamu pilih untuk perangkat kamu, keduanya dipisahkan dengan *titik*, misalnya:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- kata sandi, yang biasanya selalu "**x**"



Setelah informasi kolam renang dimasukkan, klik "Simpan".



![image](assets/fr/18.webp)


Nyalakan kembali perangkat sesuai petunjuk, dan tunggu beberapa menit hingga Hashrate kamu mengarah ke kolam pilihan Anda (#1).



### Menggunakan browser untuk menyambung ke Mining pool



Kamu juga dapat terhubung ke Mining pool dan, secara umum, mengakses sistem manajemen Interface perangkat kamu melalui browser favorit Anda.



Untuk melakukannya, ketik IP Address dari perangkat yang ditunjukkan pada layar di bawah ini, dalam contoh kami **192.168.144.6** pada bilah pencarian browser



![image](assets/fr/15.webp)



Halaman berikut akan muncul, memintamu untuk membuka aplikasi Avalon Family dan memindai kode QR yang ditampilkan dengan aplikasi tersebut.



![image](assets/fr/20.webp)



Buka aplikasi, dan klik 3 garis di kanan atas, lalu pindai. Pindai kode QR peramban, lalu masukkan kata sandi administrator aplikasi dan klik OK.



![image](assets/fr/21.webp)



Di sini kamu berada di halaman web yang memungkinkanmu berinteraksi dengan Avalon. Ini lebih merupakan dasbor untuk menampilkan metrik mesin, daripada sarana untuk mengonfigurasinya.



Tetapi pengaturan kolam renang masih dapat diakses dengan cara ini, dengan mengklik **"Pool Config "** di pojok kanan bawah.



![image](assets/fr/22.webp)



Dengan cara yang sama seperti pada aplikasi seluler, kamu dapat memasukkan parameter pool di sini.



![image](assets/fr/23.webp)



## Kontrol perangkat melalui aplikasi Avalon Family



Kami sekarang telah menghubungkan Miner di rumah kami ke jaringan lokal, dan mengarahkan Hashrate kami ke kolam-kolam tambang. Sekarang mari kita temukan fitur-fitur penting dari alat berat kita melalui aplikasi Avalon Family.



Pada menu utama aplikasi keluarga Avalon, klik ikon yang sesuai dengan Avalon Mini 3. Kamu akan dibawa langsung ke menu untuk mengelola mode pengoperasian.



tersedia 3 opsi: mode "Heater", mode "Mining" atau mode "Night".





- Dalam mode "Heater" kamu memiliki 2 tingkat daya "Eco" atau "Super".


Tingkat "Eco" sesuai dengan daya pemanasan 500W untuk Hashrate sekitar 25 Th/s dan 40 dB untuk tingkat suara.


Tingkat "Super" sesuai dengan daya output 650 W pada sekitar 30Th/s dan 45 dB. Mode ini memungkinkanmu untuk menetapkan suhu lingkungan maksimum di atas suhu di mana unit akan berhenti bekerja.



![image](assets/fr/36.webp)




- Dalam mode "Mining", unit beroperasi pada kecepatan maksimum, tanpa opsi untuk menetapkan suhu target (tentu saja, selain dari batas overheating bawaan). Tujuannya adalah untuk memaksimalkan performa Miner. Di sini, daya output mendekati 800 W pada sekitar 37,5 Th/s dan tingkat kebisingan 50-55 dB.



![image](assets/fr/37.webp)


Terakhir, dalam mode "Night", Mini 3 Anda beroperasi pada kecepatan serendah mungkin dengan kebisingan minimum. 400 W, 20 Th/s dan sekitar 33 dB.



Di sini, kamu juga bisa menetapkan suhu target. Saat suhu melewati batas tersebut, unit akan masuk ke mode tidak aktif dan menghentikan miner. Jika suhu turun, unit akan menyala kembali dan melanjutkan fungsi pemanasan serta miner. Dalam mode ini, LED layar dimatikan secara default, tetapi kamu bisa memilih untuk menyalakannya jika diperlukan untuk menerangi ruangan saat gelap, misalnya sebagai lampu malam (lihat foto di bawah).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Terakhir, kamu bisa bermain-main dengan LED Avalon kamu melalui menu "Tampilan". Kamu dapat memilih untuk menggulir informasi pengoperasian yang relevan, menampilkan waktu, atau bahkan menampilkan gambar khusus (pixelated).



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Seperti halnya Avalon Nano 3S, menu "Pengaturan" memungkinkanmu mengubah kata sandi administrator, pengaturan pool, memeriksa halangan filter (terletak di bagian bawah perangkat), menghubungi dukungan, atau melihat log perangkat.



![image](assets/fr/42.webp)



Sekali lagi, filter di bagian bawah unit dapat dibersihkan dengan penyedot debu, semakin sering dibersihkan, semakin baik.



Kita telah sampai pada akhir tutorial ini, yang telah mengajarkan kita cara menghubungkan Avalon Mini 3 ke jaringan lokal kita, cara mengarahkan Hashrate ke pool Mining, dan cara menavigasi opsi dan pengaturan menggunakan aplikasi Avalon Family.



Untuk mengetahui lebih lanjut, lihat tutorial kami mengenai versi yang lebih kecil dari Avalon: Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6
