---
name: Bitaxe
description: Bagaimana cara mengatur BitAxe?
---
![video](https://youtu.be/tvLSK8v0MK8)
## Pendahuluan

BitAxe adalah proyek open-source yang dibuat oleh Skot dan [tersedia di GitHub](https://github.com/skot/bitaxe) yang memungkinkan eksperimen penambangan dengan biaya efektif.

Proyek ini telah merekayasa ulang cara kerja Antminer S19 yang terkenal dari Bitmain, pemimpin pasar dalam ASIC, mesin khusus untuk penambangan Bitcoin. Kini, chip bertenaga ini bisa digunakan dalam proyek open-source baru. Berbeda dengan Nerdminer, BitAxe memiliki daya komputasi yang cukup untuk terhubung ke mining pool, yang memungkinkan kamu secara rutin mendapatkan beberapa satoshi. Di sisi lain, Nerdminer hanya bisa terhubung ke yang disebut solo pool, yang berfungsi seperti tiket lotre: kamu memiliki peluang kecil untuk memenangkan hadiah blok penuh.

Ada beberapa versi BitAxe, dengan chip dan performa yang berbeda:

| Seri Model Bitaxe        | Chip ASIC | Digunakan Pada              | Hash Rate yang Diharapkan   | Ideal Untuk                                                                                                |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Seri 100)    | 1 x BM1397| Seri Antminer 17            | 400 GH/s (hingga 450 GH/s)  | Pemula penambangan Bitcoin, menawarkan hash rate solid dengan konsumsi daya moderat.                       |
| Bitaxe Ultra (Seri 200)  | 1 x BM1366| Antminer S19 XP dan S19k Pro| 500 GH/s (hingga 550 GH/s)  | Penambang serius yang bertujuan menyeimbangkan efisiensi dan hash rate yang lebih tinggi.                  |
| Bitaxe Hex (Seri 300)    | 6 x BM1366| Antminer S19k Pro dan S19 XP| 3.0 TH/s (hingga 3.3 TH/s)  | Penambang yang mencari skalabilitas dan performa tinggi tanpa mengorbankan efisiensi.                      |
| Bitaxe Supra (Seri 400)  | 1 x BM1368| Antminer S21                | 600 GH/s (hingga 700 GH/s)  | Penggemar serius yang mencari hash rate dan efisiensi tertinggi.                                           |

Dalam tutorial ini, kita akan menggunakan BitAxe Ultra 204 yang dilengkapi dengan chip BM1366, digunakan untuk Antminer S19XP. Ini sudah dirakit dan diflash oleh penjual.

[Daftar pengecer tersedia di halaman ini](https://bitaxe.org/legit.html)

![signup](assets/2.webp)

Umumnya, catu daya dijual bersamanya. Jika tidak, kamu perlu membeli catu daya dengan kabel jack 5V dan arus setidaknya 4A.

![signup](assets/1.webp)

## Konfigurasi
Saat pertama kali kamu menyambungkan BitAxe, perangkat ini akan mencoba terhubung ke jaringan Wi-Fi secara default. Setelah lima kali percobaan, BitAxe akan menampilkan nama jaringan Wi-Fi miliknya sendiri agar kamu bisa terhubung dan melakukan konfigurasi.

Untuk melakukannya, kamu bisa menggunakan komputer atau smartphone apa pun. Buka pengaturan Wi-Fi, cari jaringan baru, dan kamu akan melihat jaringan bernama Bitaxe_XXXX. Dalam contoh ini, namanya adalah 'Bitaxe_A859'. Sambungkan ke jaringan Wi-Fi tersebut, dan sebuah jendela akan terbuka secara otomatis.

![signup](assets/3.webp)

Di jendela ini, klik pada tiga baris horizontal kecil di kiri atas, kemudian pada `Settings`.

![signup](assets/4.webp)

Kamu perlu memasukkan informasi jaringan Wi-Fi secara manual, karena tidak ada sistem penemuan otomatis.
![signup](assets/5.webp)
Oleh karena itu, masukkan SSID Wi-Fi kamu, yaitu nama jaringan kamu, kata sandi, serta informasi tentang mining pool yang telah kamu pilih. Hati-hati, di sini URL pool tidak disajikan dengan cara yang sama. Sebagai contoh, untuk Braiins, URL pool yang diberikan adalah: `stratum+tcp://eu.stratum.braiins.com:3333`.

![signup](assets/6.webp)

Seperti yang kamu lihat pada layar, kamu perlu menghapus bagian `stratum+tcp://` dan `:3333`, meninggalkan hanya `eu.stratum.braiins.com`. Kemudian, di kolom `Port`, masukkan 4 digit di akhir URL yang diberikan oleh pool, tetapi tanpa `:`. Di sini, oleh karena itu `3333`.

Dalam tutorial ini, kami menggunakan mining pool Braiins, tetapi kamu bebas memilih yang lain. Kamu dapat menemukan tutorial kami tentang mining pool [di situs web Plan ₿ Academy](https://planb.academy/en/tutorials/mining).

Selanjutnya, di `User`, masukkan identifikasi Anda kemudian `Password`, biasanya, itu adalah `"x"` atau `"Anything123"`.

Pengaturan `Core Voltage` sebaiknya dibiarkan pada `1200` secara default, dan untuk `Frequency`, juga biarkan nilai default awalnya. Akan dimungkinkan untuk menyesuaikan pengaturan ini nanti untuk mendapatkan lebih banyak daya komputasi. Namun, penting untuk memastikan bahwa suhu chip tidak melebihi 65-70°C, karena BitAxe tidak memiliki sistem untuk mengurangi kinerja dalam kasus overheating. Jika suhu melebihi 65°C terlalu banyak, itu bisa merusak BitAxe kamu.

![signup](assets/7.webp)

Setelah kamu memasukkan semua pengaturan dengan benar, klik tombol 'Save' di bagian bawah, lalu restart BitAxe dengan mencabutnya dan memasangnya kembali.
Jika informasinya dimasukkan dengan benar, perangkat akan langsung terhubung ke Wi-Fi kamu, kemudian ke mining pool, dan mulai menampilkan beberapa informasi di layar kecilnya. Mungkin diperlukan beberapa menit sebelum perangkat muncul di dashboard mining pool.

## Dasbor dan layar

Tiga tampilan berbeda akan bergulir. Pada halaman ketiga, kamu akan melihat informasi `IP`, yang merupakan alamat IP yang memungkinkan kamu terhubung ke dashboard. Di sini, alamatnya adalah `192.168.1.19`.

![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)

Untuk mengakses dashboard, cukup masukkan alamat ini ke dalam browser internet kamu.

Di dashboard, kamu akan menemukan semua informasi yang ditampilkan di layar kecil, yang sekarang akan kita lihat secara detail.

![signup](assets/11.webp)

| Layar BitAxe | Dashboard                                   | Deskripsi                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | Daya komputasi saat ini, dinyatakan dalam GigaHash/s                                                                                                                                                                      |
| W/THs         | Efisiensi                                  | Ini adalah efisiensi BitAxe kamu yang dinyatakan dalam W/THs. Ini adalah rasio antara daya listrik yang dikonsumsi dan daya komputasi yang dihasilkan.                                                                          |
| A/R           | Shares                                      | Jumlah `Shares` yang dikirim oleh BitAxe kamu ke pool, mewakili jumlah pekerjaan yang disediakan.                                                                                                                          |
| UT            | Uptime                                      | Waktu sejak BitAxe Anda beroperasi tanpa gangguan (tersedia di menu kiri di bawah `Logs`).                                                                                                                |
| BD            | Kesulitan Terbaik                           | Kesulitan maksimum yang dicapai sejak restart terakhir. Untuk perbandingan, kesulitan jaringan saat ini sekitar 85T.                                                                                                      |
| FAN           | FAN di kotak `Heat`                         | Kecepatan rotasi kipas, dinyatakan dalam rotasi per menit.                                                                                                                                                                 |
| Temp          | Suhu ASIC di kotak `Heat`                   | Suhu chip, yang seharusnya tidak melebihi 65°C.                                                                                                                                                                            |
| Pwr           | Daya                                        | Daya dalam watt yang dikonsumsi. Namun, informasi ini tidak memperhitungkan layar, kipas, atau catu daya. Misalnya, ketika menampilkan 11.7W, konsumsi total sebenarnya adalah 15.8W.                                     |
| mV mA         | Tegangan Masukan Arus Masukan               | Tegangan dan arus yang dikonsumsi oleh mesin. Daya dalam watt sama dengan tegangan dikalikan dengan arus.                                                                                                                  |
| FH            | Memori Heap Bebas (menu kiri -> `Logs`)     | Memori yang tersedia.                                                                                                                                                                                                     |
| vCore         | Tegangan ASIC (di kotak Performa)           | Tegangan yang diukur pada chip ASIC.                                                                                                                                                                                      |
| IP            | NA                                          | Alamat IP.                                                                                                                                                                                                                |
| V2.1.0        | Versi (menu kiri -> `Logs`)                 | Versi firmware.                                                                                                                                                                                                           |
Kamu dapat mengubah pengaturan Wi-Fi atau kolam kapan saja tanpa masalah.  
Tergantung pada ventilasi dan suhu ruangan, Kamu mungkin perlu meningkatkan atau mungkin harus menurunkan performa agar suhu tidak melebihi 65°C. Jika kamu meningkatkan performa, kamu akan mendapatkan lebih banyak satoshi, tetapi BitAxe milikmu juga akan mengonsumsi lebih banyak listrik!
