---
term: NVERSION

---
Kolom `nVersion` dalam transaksi Bitcoin digunakan untuk mengindikasikan versi format transaksi yang digunakan. Hal ini memungkinkan jaringan untuk membedakan antara evolusi yang berbeda dari format transaksi dari waktu ke waktu dan menerapkan aturan yang sesuai. Kolom ini tidak berdampak pada aturan konsensus. Ini berarti bahwa nilai apa pun yang diberikan pada bidang ini tidak mengakibatkan transaksi menjadi tidak valid. Namun, field `nVersion` memiliki aturan standarisasi yang saat ini hanya menerima nilai `1` dan `2`. Untuk saat ini, field ini hanya berguna untuk aktivasi field `nSequence`.