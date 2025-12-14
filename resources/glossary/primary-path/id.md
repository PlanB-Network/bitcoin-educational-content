---
term: PRIMARY PATH

---
Dalam perangkat lunak dompet yang menggunakan _Miniscript_, seperti Liana misalnya, jalur utama mengacu pada sekumpulan kunci yang memungkinkan pengeluaran dana secara langsung, tanpa syarat waktu. Jalur ini selalu dapat diakses dan digunakan untuk manajemen harian bitcoin, tanpa membutuhkan waktu tunggu (_timelock_) tidak seperti jalur pemulihan. Sebagai contoh, skrip yang menggabungkan 2 kunci yang berbeda: kunci A, yang mengizinkan pengeluaran bitcoin secara langsung, dan kunci B, yang mengizinkan pengeluaran setelah penundaan yang ditentukan oleh penguncian waktu sebesar 52.560 blok. Dalam contoh ini, kunci A berasal dari jalur utama, sedangkan kunci B berasal dari jalur pemulihan.
