---
term: PATHFINDING
---

Proses yang digunakan oleh node untuk menentukan jalur optimal untuk merutekan pembayaran melalui jaringan saluran Lightning. Pencarian jalur dilakukan oleh node pembayar, yang harus memilih node perantara yang paling sesuai untuk mencapai penerima. Pilihan ini didasarkan pada sejumlah kriteria, seperti biaya, kapasitas saluran, dan batas waktu.


Algoritma pencarian jalur membuat grafik topologi jaringan dari data _Gossip_ dan mengevaluasi berbagai kemungkinan rute antara node pembayar dan penerima. Rute-rute ini diurutkan dari yang terbaik hingga yang terburuk berdasarkan berbagai kriteria. Node kemudian menguji rute-rute ini sampai berhasil melakukan pembayaran pada salah satu rute tersebut.
