---
term: NVERSION
---

Field `nVersion` dalam transaksi Bitcoin digunakan untuk menunjukkan versi dari format transaksi yang digunakan. Ini memungkinkan jaringan untuk membedakan antara evolusi format transaksi yang berbeda dari waktu ke waktu dan untuk menerapkan aturan yang sesuai. Field ini tidak memiliki dampak pada aturan konsensus. Ini berarti bahwa nilai apa pun yang diberikan kepada field ini tidak mengakibatkan transaksi menjadi tidak valid. Namun, field `nVersion` memiliki aturan standarisasi yang saat ini hanya menerima nilai `1` dan `2`. Untuk saat ini, field ini hanya berguna untuk aktivasi field `nSequence`.