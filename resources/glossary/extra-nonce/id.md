---
term: EXTRA-NONCE
---

Bidang yang digunakan dalam `scriptSig` dari _Coinbase Transaction_ sebuah blok, yang memungkinkan lebih banyak kemungkinan untuk diuji untuk mendapatkan _Hash_ yang lebih rendah dari target kesulitan, di samping nilai _Nonce_ klasik, yang ditemukan secara langsung di _header_ setiap blok.


Memodifikasi _extra-Nonce_ di _Coinbase Transaction_ akan mengubah ID transaksi ini, dan itu akan mengubah _Merkle Root_ dari semua transaksi dalam blok, yang juga mengubah _header_ blok. Hal ini memungkinkan Miner untuk terus mencari _hash_ ketika jangkauan _Nonce_ klasik sudah habis, tanpa mengubah struktur blok kandidatnya.


Dalam _mining pool_, _Extra-Nonce_ sering dibagi menjadi dua bagian: satu dibuat oleh _pool_ untuk mengidentifikasi setiap _chopper_, dan satu lagi dimodifikasi oleh _chopper_ untuk mencari bagian yang valid. Hal ini memungkinkan berbagai _chopper_ dalam _pool_ untuk bekerja secara bersamaan pada blok kandidat yang sama dengan seluruh rentang _nonce_, tanpa menduplikasi pekerjaan yang sama di tingkat _pool_.
