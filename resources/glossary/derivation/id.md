---
term: DERIVATION
---

Merujuk pada proses menghasilkan pasangan kunci anak dari pasangan kunci induk (kunci privat dan kunci publik) dan kode rantai dalam dompet deterministik dan hierarkis (HD). Proses ini memungkinkan segmentasi cabang dan organisasi dompet ke dalam berbagai tingkatan dengan banyak pasangan kunci anak, yang semuanya dapat dipulihkan dengan hanya mengetahui informasi pemulihan dasar (frasa mnemonik dan setiap kata sandi potensial). Untuk menurunkan kunci anak, fungsi `HMAC-SHA512` digunakan dengan kode rantai induk dan penggabungan kunci induk dan indeks 32-bit. Ada dua jenis turunan:
* Turunan normal, yang menggunakan kunci publik induk sebagai dasar fungsi `HMAC-SHA512`;
* Turunan diperkuat, yang menggunakan kunci privat induk sebagai dasar fungsi `HMAC-SHA512`;

Hasil dari HMAC-SHA512 dibagi menjadi dua: 256 bit pertama menjadi kunci anak (privat atau publik setelah diproses melalui ECDSA), dan 256 bit sisanya menjadi kode rantai anak.