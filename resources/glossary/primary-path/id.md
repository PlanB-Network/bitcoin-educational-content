---
term: JALUR UTAMA

---
Dalam perangkat lunak dompet yang menggunakan Miniscript, seperti Liana misalnya, jalur utama mengacu pada sekumpulan kunci yang memungkinkan pengeluaran dana secara langsung, tanpa syarat waktu. Jalur ini selalu dapat diakses dan digunakan untuk manajemen harian bitcoin, tanpa membutuhkan waktu tunggu (timelock) tidak seperti jalur pemulihan. Ambil contoh skrip yang menggabungkan 2 kunci yang berbeda: kunci A, yang mengotorisasi pengeluaran bitcoin secara langsung, dan kunci B, yang mengizinkan pengeluaran setelah penundaan yang ditentukan oleh penguncian waktu sebesar 52.560 blok. Dalam contoh ini, kunci A berasal dari jalur utama, sedangkan kunci B berasal dari jalur pemulihan.