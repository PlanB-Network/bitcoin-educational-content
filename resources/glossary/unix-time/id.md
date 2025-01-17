---
term: WAKTU UNIX

---
Waktu Unix atau Stempel Waktu Unix menunjukkan jumlah detik yang telah berlalu sejak 1 Januari 1970, pada tengah malam UTC (Zaman Unix). Sistem ini digunakan dalam sistem operasi Unix dan turunannya untuk menandai waktu dengan cara yang universal dan terstandardisasi. Sistem ini memungkinkan sinkronisasi jam dan pengelolaan acara berbasis waktu, tanpa memandang zona waktu.

Dalam konteks Bitcoin, ini digunakan untuk jam lokal node, dan dengan demikian untuk perhitungan NAT (Network-Adjusted Time). Waktu yang disesuaikan dengan jaringan adalah median dari waktu node yang dihitung secara lokal oleh setiap node, dan referensi ini kemudian digunakan untuk memverifikasi validitas stempel waktu blok. Memang, agar sebuah blok dapat diterima oleh sebuah node, cap waktunya harus berada di antara MTP (Median Time Past dari 11 blok terakhir yang ditambang) dan NAT ditambah 2 jam:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Time juga digunakan untuk menetapkan batas waktu ketika didasarkan pada waktu nyata, bukan pada sejumlah blok.