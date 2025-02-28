---
name: Mengatur BitAxe
Description: Bagaimana cara mengatur BitAxe?
---

### Pendahuluan

BitAxe adalah proyek open-source yang dibuat oleh Skot dan [tersedia di GitHub](https://github.com/skot/bitaxe) yang memungkinkan eksperimen penambangan dengan biaya efektif.

Proyek ini telah merekayasa ulang cara kerja dari Antminer S19 yang terkenal oleh Bitmain, pemimpin pasar dalam ASIC, mesin khusus untuk penambangan bitcoin. Sekarang, chip kuat ini dapat digunakan dalam proyek open-source baru. Berbeda dengan Nerdminer, BitAxe memiliki kekuatan komputasi yang cukup untuk terhubung ke kolam penambangan, yang akan memungkinkan Anda untuk secara rutin mendapatkan beberapa satoshi. Di sisi lain, Nerdminer hanya dapat terhubung ke apa yang disebut solopool, yang berfungsi seperti tiket lotre: Anda memiliki peluang kecil untuk memenangkan hadiah blok penuh.

Ada beberapa versi BitAxe, dengan chip dan performa yang berbeda:

| Seri Model Bitaxe        | Chip ASIC | Digunakan Pada              | Hash Rate yang Diharapkan   | Ideal Untuk                                                                                                |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Seri 100)    | 1 x BM1397| Seri Antminer 17            | 400 GH/s (hingga 450 GH/s)  | Pemula penambangan Bitcoin, menawarkan hash rate solid dengan konsumsi daya moderat.                       |
| Bitaxe Ultra (Seri 200)  | 1 x BM1366| Antminer S19 XP dan S19k Pro| 500 GH/s (hingga 550 GH/s)  | Penambang serius yang bertujuan menyeimbangkan efisiensi dan hash rate yang lebih tinggi.                  |
| Bitaxe Hex (Seri 300)    | 6 x BM1366| Antminer S19k Pro dan S19 XP| 3.0 TH/s (hingga 3.3 TH/s)  | Penambang yang mencari skalabilitas dan performa tinggi tanpa mengorbankan efisiensi.                      |
| Bitaxe Supra (Seri 400)  | 1 x BM1368| Antminer S21                | 600 GH/s (hingga 700 GH/s)  | Penggemar serius yang mencari hash rate dan efisiensi tertinggi.                                           |

Dalam tutorial ini, kita akan menggunakan BitAxe Ultra 204 yang dilengkapi dengan chip BM1366, digunakan untuk Antminer S19XP. Ini sudah dirakit dan diflash oleh penjual.

### [Daftar penjual tersedia di halaman ini](https://bitaxe.org/legit.html)

![signup](assets/2.webp)

Umumnya, catu daya dijual bersamanya. Jika tidak, Anda akan perlu membeli catu daya dengan kabel jack 5V dan setidaknya 4A.

![signup](assets/1.webp)

### Konfigurasi
Ketika Anda pertama kali menyambungkan BitAxe Anda, itu akan mencoba terhubung ke jaringan Wi-Fi secara default. Setelah lima percobaan, itu akan menampilkan nama jaringan Wi-Fi sendiri sehingga Anda dapat terhubung ke sana dan mengonfigurasinya.
Untuk melakukan ini, Anda dapat menggunakan komputer atau smartphone apa saja. Pergi ke pengaturan Wi-Fi Anda, cari jaringan baru, dan Anda akan melihat Wi-Fi yang bernama Bitaxe_XXXX. Di sini, adalah `Bitaxe_A859`. Sambungkan ke jaringan Wi-Fi ini, dan sebuah jendela akan secara otomatis terbuka.

![signup](assets/3.webp)

Di jendela ini, klik pada tiga baris horizontal kecil di kiri atas, kemudian pada `Settings`.

![signup](assets/4.webp)

Anda perlu memasukkan informasi jaringan Wi-Fi Anda secara manual, karena tidak ada sistem penemuan otomatis.
![signup](assets/5.webp)
Oleh karena itu, masukkan SSID Wi-Fi Anda, yaitu nama jaringan Anda, kata sandi, serta informasi tentang mining pool yang telah Anda pilih. Hati-hati, di sini URL pool tidak disajikan dengan cara yang sama. Sebagai contoh, untuk Braiins, URL pool yang diberikan adalah: `stratum+tcp://eu.stratum.braiins.com:3333`.

![signup](assets/6.webp)

Seperti yang Anda lihat pada layar, Anda perlu menghapus bagian `stratum+tcp://` dan `:3333`, meninggalkan hanya `eu.stratum.braiins.com`. Kemudian, di kolom `Port`, masukkan 4 digit di akhir URL yang diberikan oleh pool, tetapi tanpa `:`. Di sini, oleh karena itu `3333`.

Dalam tutorial ini, kami menggunakan mining pool Braiins, tetapi Anda bebas memilih yang lain. Anda dapat menemukan tutorial kami tentang mining pool [di situs web PlanB Network](https://planb.network/en/tutorials/mining).

Selanjutnya, di `User`, masukkan identifikasi Anda kemudian `Password`, biasanya, itu adalah `"x"` atau `"Anything123"`.

Pengaturan `Core Voltage` sebaiknya dibiarkan pada `1200` secara default, dan untuk `Frequency`, juga biarkan nilai default awalnya. Akan dimungkinkan untuk menyesuaikan pengaturan ini nanti untuk mendapatkan lebih banyak daya komputasi. Namun, penting untuk memastikan bahwa suhu chip tidak melebihi 65-70°C, karena BitAxe tidak memiliki sistem untuk mengurangi kinerja dalam kasus overheating. Jika suhu melebihi 65°C terlalu banyak, itu bisa merusak BitAxe Anda.

![signup](assets/7.webp)

Setelah Anda dengan benar memasukkan semua pengaturan, klik tombol `Save` di bagian bawah, kemudian restart BitAxe Anda hanya dengan mencabutnya dan memasangnya kembali.
Jika Anda memasukkan informasi Anda dengan benar, perangkat harus segera terhubung ke Wi-Fi Anda, kemudian ke mining pool, dan mulai menampilkan beberapa informasi di layar kecilnya. Mungkin akan membutuhkan beberapa menit agar muncul di dashboard mining pool.
### Dashboard dan Layar

Tiga tampilan berbeda akan bergulir. Pada halaman ketiga, Anda akan melihat informasi `IP`, yang merupakan alamat IP yang memungkinkan Anda terhubung ke dashboard. Di sini, alamatnya adalah `192.168.1.19`.

![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)

Untuk mengakses dashboard, cukup masukkan alamat ini ke dalam browser internet Anda.

Di dashboard, Anda akan menemukan semua informasi yang ditampilkan di layar kecil, yang sekarang akan kita lihat secara detail.

![signup](assets/11.webp)

| Layar BitAxe | Dashboard                                   | Deskripsi                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | Daya komputasi saat ini, dinyatakan dalam GigaHash/s                                                                                                                                                                      |
| W/THs         | Efisiensi                                  | Ini adalah efisiensi BitAxe Anda yang dinyatakan dalam W/THs. Ini adalah rasio antara daya listrik yang dikonsumsi dan daya komputasi yang dihasilkan.                                                                          |
| A/R           | Shares                                      | Jumlah `Shares` yang dikirim oleh BitAxe Anda ke pool, mewakili jumlah pekerjaan yang disediakan.                                                                                                                          |
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
Anda dapat mengubah pengaturan Wi-Fi atau kolam kapan saja tanpa masalah.  
Tergantung pada ventilasi dan suhu ruangan Anda, Anda mungkin perlu meningkatkan atau mungkin harus menurunkan performa agar suhu tidak melebihi 65°C. Jika Anda meningkatkan performa, Anda akan mendapatkan lebih banyak satoshi, tetapi BitAxe Anda juga akan mengonsumsi lebih banyak listrik!