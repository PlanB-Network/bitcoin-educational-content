---
name: Public Pool
description: Pengenalan Public Pool
---

![signup](assets/cover.webp)

**Public Pool** bukan pool biasa; ini juga dikenal sebagai **Solo Pool.** Jika penambang kamu berhasil menambang sebuah blok, kamu akan mengumpulkan seluruh hadiah blok tersebut, tanpa dibagi dengan peserta lain di kolam atau dengan kolam itu sendiri.

**Public Pool** hanya menyediakan **template blok** untuk penambang kamu, sehingga penambang dapat menjalankan tugasnya tanpa kamu perlu memiliki node Bitcoin dan perangkat lunak yang berkomunikasi dengan penambang kamu. Karena kamu tidak menggabungkan kekuatan komputasi dengan peserta lain, peluang kamu untuk berhasil menambang sebuah blok jelas sangat rendah, mirip dengan sistem lotere, di mana sesekali seseorang yang beruntung memenangkan jackpot.

![signup](assets/1.webp)

Di **Dashboard** dari **Public Pool**, kamu masih memiliki beberapa statistik seperti **Total Hashrate** poll serta distribusi dari berbagai jenis penambang yang terhubung ke pool.

![signup](assets/2.webp)

Dalam beberapa baris pertama, kita dapat melihat **Bitaxe** dengan 1323 **Bitaxe** terhubung untuk total 649TH/s. **Bitaxe** adalah proyek **Sumber Terbuka** yang memungkinkan penggunaan kembali chip dari **ASIC** seperti **Antminer S19** pada papan elektronik **sumber terbuka** untuk membuat penambang kecil 0.5TH/s dengan 15W. Ini adalah penambang yang akan kita gunakan sebagai contoh untuk tutorial ini.

## Menambahkan **Pekerja** 👷‍♂️

![signup](assets/cover.webp)

Di bagian atas halaman, Anda dapat menyalin alamat pool **stratum+tcp://public-pool.io:21496**.

Selanjutnya, untuk bidang **pengguna**, masukkan alamat **Bitcoin** yang kamu miliki.

Jika kamu memiliki beberapa penambang, kamu dapat memasukkan alamat yang sama untuk semuanya sehingga **hashrate** mereka digabungkan dan muncul sebagai satu penambang. Kamu juga dapat membedakannya dengan menambahkan nama yang berbeda untuk masing-masing. Untuk melakukan ini, cukup tambahkan **.namapekerja** setelah alamat **Bitcoin**.

Akhirnya, untuk bidang **kata sandi**, gunakan **‘x’**.

Contoh: Jika alamat **Bitcoin** kamu adalah **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** dan kamu ingin menamai penambang kamu **« Brrrr »**, maka kamu akan memasukkan informasi berikut di antarmuka penambang kamu:

- **URL**: stratum+tcp://public-pool.io:21496
- **PENGGUNA**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Kata Sandi**: **‘x’**
Jika penambang kamu adalah **Bitaxe**, bidangnya sedikit berbeda, tetapi informasinya tetap sama:
- **URL**: public-pool.io (di sini, kamu perlu menghapus bagian di awal **‘stratum+tcp://’** dan bagian di akhir **‘:21496’** yang akan dilaporkan di bidang port)
- **Port**: 21496
- **Pengguna**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Kata Sandi**: **‘x’**

![signup](assets/3.webp)
Beberapa menit setelah kamu mulai menambang, kamu akan dapat melihat data Anda di situs web **Public Pool** dengan mencari alamat kamu.

## Dashboard

![signup](assets/4.webp)

Setelah kamu terhubung ke **Public Pool**, kamu dapat mengakses **Dashboard** kamu dengan mencari menggunakan alamat **Bitcoin** yang kamu masukkan di bidang **User**. Dalam kasus kita di sini, itu adalah **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

Di **Dashboard**, berbagai informasi ditampilkan baik tentang data kamu maupun tentang jaringan.

![signup](assets/5.webp)

Kamu memiliki **Network Hash Rate** yang sesuai dengan total kekuatan kerja dari jaringan **Bitcoin**.

**Network Difficulty** menunjukkan kesulitan yang harus dicapai untuk memvalidasi sebuah blok.

Dan **Your Best Difficulty** adalah kesulitan tertinggi yang telah kamu capai. Jika, dengan keberuntungan 🍀, kamu mencapai kesulitan jaringan, maka kamu memenangkan seluruh hadiah blok... setelah 100 blok. Kamu harus menunggu 100 blok sebelum dapat menghabiskannya.

Kamu juga memiliki **Block Height** yang merupakan nomor dari blok terakhir yang ditambang serta bobotnya yang dinyatakan dalam WU, maksimumnya adalah 4,000,000.

Di bawah ini, kamu dapat melihat semua statistik dari masing-masing perangkat kamu secara individu jika kamu telah memberi mereka nama yang berbeda dengan menambahkan **.name** di belakang alamat **Bitcoin** Anda di bidang **User**.
