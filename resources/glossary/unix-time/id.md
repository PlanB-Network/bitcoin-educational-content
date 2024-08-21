---
term: UNIX TIME
---

Unix Time atau Unix Timestamp mewakili jumlah detik yang telah berlalu sejak 1 Januari 1970, pada tengah malam UTC (Unix Epoch). Sistem ini digunakan dalam sistem operasi Unix dan turunannya untuk menandai waktu secara universal dan terstandarisasi. Ini memungkinkan sinkronisasi jam dan pengelolaan acara berbasis waktu, terlepas dari zona waktu.

Dalam konteks Bitcoin, ini digunakan untuk jam lokal dari node, dan dengan demikian untuk perhitungan NAT (Network-Adjusted Time). Waktu yang disesuaikan jaringan adalah median dari waktu node yang dihitung secara lokal oleh setiap node, dan referensi ini kemudian digunakan untuk memverifikasi validitas timestamp blok. Memang, agar blok diterima oleh sebuah node, timestamp-nya harus berada di antara MTP (Median Time Past dari 11 blok yang ditambang terakhir) dan NAT ditambah 2 jam:

```text
MTP < Timestamp Valid < (NAT + 2h)
```

Unix Time juga digunakan untuk menetapkan timelock ketika mereka didasarkan pada waktu nyata, daripada pada jumlah blok.