---
name: Public Pool
description: Pengenalan Public Pool
---

![signup](assets/cover.webp)

**Public Pool** bukan sembarang kolam; ini yang juga dikenal sebagai **Solo Pool**. Jika penambang Anda berhasil menambang sebuah blok, maka Anda akan menerima seluruh hadiah blok tersebut, yang tidak dibagi dengan peserta lain dari kolam atau dengan kolam itu sendiri.

**Public Pool** hanya menyediakan **template blok** untuk penambang Anda agar dapat melakukan pekerjaannya, tanpa Anda perlu memiliki **node Bitcoin** dan perangkat lunak yang berkomunikasi dengan penambang Anda. Karena Anda tidak menggabungkan kekuatan komputasi Anda dengan peserta lain, peluang Anda untuk berhasil menambang sebuah blok jelas sangat rendah, menjadikannya semacam sistem lotere, di mana kadang-kadang seorang individu beruntung memenangkan jackpot.

![signup](assets/1.webp)

Di **Dashboard** dari **Public Pool**, Anda masih memiliki beberapa statistik seperti **Total Hashrate** dari kolam serta distribusi dari berbagai jenis penambang yang terhubung ke kolam.

![signup](assets/2.webp)

Dalam baris pertama, kita dapat melihat **Bitaxe** dengan 1323 **Bitaxe** terhubung untuk total 649TH/s. **Bitaxe** adalah proyek **Open source** yang memungkinkan penggunaan kembali chip dari **ASIC** seperti **Antminer S19** pada papan elektronik **opensource** untuk membuat penambang yang sangat kecil sebesar 0.5TH/s untuk 15W. Ini adalah penambang yang akan kita gunakan sebagai contoh untuk tutorial ini.

## Tambahkan **Worker** 👷‍♂️

![signup](assets/cover.webp)

Di bagian atas halaman, Anda dapat menyalin alamat kolam **stratum+tcp://public-pool.io:21496**.

Selanjutnya, untuk kolom **user**, masukkan alamat **Bitcoin** yang Anda miliki.

Jika Anda memiliki beberapa penambang, Anda dapat memasukkan alamat yang sama untuk semuanya sehingga **hashrate** mereka digabungkan dan muncul sebagai satu penambang. Anda juga dapat membedakannya dengan menambahkan nama yang berbeda untuk masing-masing. Untuk melakukan ini, cukup tambahkan **.workername** setelah alamat **Bitcoin**.

Akhirnya, untuk kolom **password**, gunakan **‘x’**.

Contoh: Jika alamat **Bitcoin** Anda adalah **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** dan Anda ingin menamai penambang Anda **« Brrrr »**, maka Anda harus memasukkan informasi berikut di antarmuka penambang Anda:

- **URL** : stratum+tcp://public-pool.io:21496
- **USER** : **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Password** : **‘x’**
Jika penambang Anda adalah **Bitaxe**, kolomnya sedikit berbeda, tetapi informasinya tetap sama:
- **URL**: public-pool.io (di sini, Anda perlu menghapus bagian di awal **‘stratum+tcp://’** dan bagian di akhir **‘:21496’** yang akan dilaporkan di kolom port)
- **Port**: 21496
- **User**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Password**: **‘x’**
![signup](assets/3.webp)
Beberapa menit setelah Anda mulai menambang, Anda akan dapat melihat data Anda di situs web **Public Pool** dengan mencari alamat Anda.

## Dashboard

![signup](assets/4.webp)

Setelah Anda terhubung ke **Public Pool**, Anda dapat mengakses **Dashboard** Anda dengan mencari menggunakan alamat **Bitcoin** yang Anda masukkan di bidang **User**. Dalam kasus kita di sini, itu adalah **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

Di **Dashboard**, berbagai informasi ditampilkan baik tentang data Anda maupun tentang jaringan.

![signup](assets/5.webp)

Anda memiliki **Network Hash Rate** yang sesuai dengan total kekuatan kerja dari jaringan **Bitcoin**.

**Network Difficulty** menunjukkan kesulitan yang harus dicapai untuk memvalidasi sebuah blok.

Dan **Your Best Difficulty** adalah kesulitan tertinggi yang telah Anda capai. Jika, dengan keberuntungan 🍀, Anda mencapai kesulitan jaringan, maka Anda memenangkan seluruh hadiah blok... setelah 100 blok. Anda harus menunggu 100 blok sebelum dapat menghabiskannya.

Anda juga memiliki **Block Height** yang merupakan nomor dari blok terakhir yang ditambang serta bobotnya yang dinyatakan dalam WU, maksimumnya adalah 4,000,000.

Di bawah ini, Anda dapat melihat semua statistik dari setiap perangkat Anda secara individu jika Anda telah memberi mereka nama yang berbeda dengan menambahkan **.name** di belakang alamat **Bitcoin** Anda di bidang **User**.