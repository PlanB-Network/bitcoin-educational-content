---
term: MINISCRIPT
---

Framework yang dirancang untuk menyediakan kerangka kerja bagi pemrograman skrip secara aman pada Bitcoin. Bahasa asli dari Bitcoin disebut skrip. Penggunaannya cukup kompleks dalam praktik, terutama untuk aplikasi yang canggih dan disesuaikan. Di atas semua itu, sangat sulit untuk memverifikasi batasan sebuah skrip. Miniscript menggunakan subset dari skrip Bitcoin untuk menyederhanakan pembuatan, analisis, dan verifikasi mereka. Setiap miniscript setara 1 untuk 1 dengan skrip asli. Sebuah bahasa kebijakan yang ramah pengguna digunakan, yang kemudian dikompilasi menjadi miniscript, untuk akhirnya sesuai dengan skrip asli.

![](../../dictionnaire/assets/30.png)

Dengan demikian, Miniscript memungkinkan pengembang untuk membangun skrip yang canggih dengan cara yang lebih aman dan lebih dapat diandalkan. Properti esensial dari Miniscript adalah sebagai berikut:
* Memungkinkan analisis statis dari skrip, termasuk kondisi pengeluaran yang diizinkannya dan biayanya dalam hal sumber daya;
* Memungkinkan pembuatan skrip yang mematuhi konsensus;
* Memungkinkan analisis apakah jalur pengeluaran yang berbeda mematuhi aturan standar dari node-node;
* Menetapkan standar umum, yang dapat dipahami dan dikomposisikan, untuk semua perangkat lunak dan perangkat keras dompet.

Proyek Miniscript diluncurkan pada tahun 2018 oleh Peter Wuille, Andrew Poelstra, dan Sanket Kanjalkar, melalui perusahaan Blockstream. Miniscript ditambahkan ke dompet Bitcoin Core dalam mode hanya-baca pada Desember 2022 dengan versi 24.0, dan kemudian sepenuhnya pada Mei 2023 dengan versi 25.0.