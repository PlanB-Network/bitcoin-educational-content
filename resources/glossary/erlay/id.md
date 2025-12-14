---
term: ERLAY
---

Protokol jaringan yang diusulkan untuk meningkatkan efisiensi transmisi transaksi yang belum dikonfirmasi antara node Bitcoin.


Saat ini, setiap transaksi disebarkan melalui sistem di mana setiap node melakukan transmisi transaksi yang diketahuinya ke semua rekan-rekannya. Masalahnya adalah hal ini menyebabkan banyak redundansi dan penggunaan _bandwidth_ untuk duplikasi. Banyak transmisi transaksi yang tidak diperlukan, karena penerima sudah mengetahui tentang transaksi ini, dan setiap node hanya perlu mengetahui tentang setiap transaksi satu kali. Erlay mengusulkan untuk membatasi secara bawaan hingga 8 jumlah _peer_ yang secara langsung dikirimi transaksi oleh sebuah node, dan kemudian menggunakan proses rekonsiliasi berdasarkan pustaka _minisketch_ untuk membagi transaksi yang hilang dengan lebih efisien.


Erlay dapat mengurangi konsumsi _bandwidth_ sekitar 40%, membuat operasi node penuh lebih mudah diakses oleh pengguna dengan koneksi Internet yang terbatas, dan dengan demikian memingkatkan desentralisasi jaringan dengan lebih baik. Protokol ini juga akan mempertahankan konsumsi _bandwidth_ yang hampir konstan ketika jumlah koneksi meningkat. Ini berarti bahwa akan jauh lebih mudah bagi operator node untuk menerima koneksi dalam jumlah yang sangat besar dari rekan-rekan mereka, yang akan meningkatkan keamanan jaringan Bitcoin dengan mengurangi risiko partisi, baik yang disengaja maupun tidak. Selain itu, Erlay akan membuat lebih sulit untuk menentukan node asal dari sebuah transaksi, sehingga meningkatkan kerahasiaan bagi pengguna node yang tidak beroperasi di bawah Tor.

Erlay diusulkan dalam BIP330.
