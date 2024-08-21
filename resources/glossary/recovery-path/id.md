---
term: JALUR PEMULIHAN
---

Dalam perangkat lunak dompet yang menggunakan Miniscript, seperti Liana misalnya, jalur pemulihan merujuk pada kumpulan kunci yang hanya menjadi operasional setelah periode ketidakaktifan yang ditentukan dalam skrip yang mengunci bitcoin (timelock). Jalur pemulihan hanya dapat digunakan setelah timelock berakhir, sehingga menawarkan metode untuk memulihkan dana ketika jalur utama tidak tersedia. Pertimbangkan contoh skrip yang menggabungkan 2 kunci berbeda: kunci A, yang mengizinkan pengeluaran bitcoin secara langsung, dan kunci B, yang memungkinkan pengeluarannya setelah keterlambatan yang ditentukan oleh timelock sebanyak 52.560 blok. Dalam contoh ini, kunci A berasal dari jalur utama, sementara kunci B berasal dari jalur pemulihan.