---
term: BIP0330
---

Sebuah proposal yang dikenal sebagai "*Erlay*", yang bertujuan untuk mengoptimalkan estafet transaksi yang belum dikonfirmasi dalam jaringan Bitcoin. Saat ini, transaksi disampaikan ke semua _peer_ dari sebuah node, yang mengakibatkan redundansi dan penggunaan _bandwidth_ yang berlebihan. BIP330 mengusulkan untuk membatasi siaran ini ke 8 _peer_ secara bawaan, kemudian menggunakan mekanisme rekonsiliasi untuk berbagi transaksi yang hilang secara efisien. Erlay mengurangi konsumsi bandwidth sekitar 40%. Hal ini juga mencegah peningkatan dalam konsumsi _bandwidth_ dengan jumlah _peer_ yang terhubung ke node.
