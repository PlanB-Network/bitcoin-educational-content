---
term: BIP0330
---

Sebuah proposal yang dikenal sebagai "*Erlay*", yang bertujuan untuk mengoptimalkan penyebaran transaksi yang belum dikonfirmasi dalam jaringan Bitcoin. Saat ini, transaksi disiarkan ke semua rekan-rekan dari sebuah node, yang mengakibatkan redundansi dan penggunaan bandwidth yang berlebihan. BIP330 mengusulkan untuk membatasi siaran ini ke 8 peer secara default, kemudian menggunakan mekanisme rekonsiliasi untuk berbagi transaksi yang hilang secara efisien. Erlay mengurangi konsumsi bandwidth sekitar 40%. Hal ini juga menghindari peningkatan linear dalam konsumsi bandwidth dengan jumlah peer yang terhubung ke node.