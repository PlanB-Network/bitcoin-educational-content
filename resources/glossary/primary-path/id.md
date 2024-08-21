---
term: PRIMARY PATH
---

Dalam perangkat lunak dompet yang menggunakan Miniscript, seperti Liana misalnya, primary path merujuk pada rangkaian kunci yang memungkinkan pengeluaran dana secara langsung, tanpa ada kondisi berbasis waktu. Jalur ini selalu dapat diakses dan digunakan untuk pengelolaan harian bitcoin, tanpa memerlukan penantian (timelock) berbeda dengan recovery paths. Ambil contoh sebuah skrip yang menggabungkan 2 kunci berbeda: kunci A, yang mengizinkan pengeluaran bitcoin secara langsung, dan kunci B, yang memungkinkan pengeluarannya setelah jeda yang ditentukan oleh timelock sebanyak 52.560 blok. Dalam contoh ini, kunci A berasal dari primary path, sementara kunci B berasal dari recovery path.