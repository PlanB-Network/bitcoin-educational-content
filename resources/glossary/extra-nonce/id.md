---
term: EXTRA-Nonce
---

Bidang yang digunakan dalam `scriptSig` dari Coinbase Transaction sebuah blok, yang memungkinkan lebih banyak kemungkinan untuk diuji untuk mendapatkan Hash yang lebih rendah dari target kesulitan, di samping Nonce klasik, yang ditemukan secara langsung di header setiap blok.


Memodifikasi ekstra-Nonce di Coinbase Transaction mengubah pengenal transaksi ini, dan oleh karena itu mengubah Merkle Root dari semua transaksi dalam blok, yang juga mengubah header blok. Hal ini memungkinkan Miner untuk terus mencari hash ketika jangkauan Nonce klasik sudah habis, tanpa mengubah struktur blok kandidatnya.


Dalam pool Mining, ekstra-Nonce sering dibagi menjadi dua bagian: satu dibuat oleh pool untuk mengidentifikasi setiap helikopter, dan satu lagi dimodifikasi oleh helikopter untuk mencari bagian yang valid. Hal ini memungkinkan berbagai helikopter dalam pool untuk bekerja secara bersamaan pada blok kandidat yang sama dengan seluruh rentang nonces, tanpa menduplikasi pekerjaan yang sama di tingkat pool.