---
term: DERIVASI

---
Mengacu pada proses pembuatan pasangan kunci anak dari pasangan kunci induk (kunci pribadi dan kunci publik) dan sebuah kode rantai dalam sebuah deterministik dan hirarkis (HD) wallet. Proses ini memungkinkan untuk segmentasi cabang dan pengorganisasian sebuah dompet ke dalam level yang berbeda dengan banyak pasangan kunci anak, yang mana semuanya dapat dipulihkan hanya dengan mengetahui informasi pemulihan dasar (frasa mnemonik dan kata sandi potensial). Untuk mendapatkan kunci anak, fungsi `HMAC-SHA512` digunakan dengan kode rantai induk dan penggabungan kunci induk dan indeks 32-bit. Ada dua jenis turunan:


- Derivasi normal, yang menggunakan kunci publik induk sebagai dasar dari fungsi `HMAC-SHA512`;
- Derivasi yang diperkeras, yang menggunakan kunci privat induk sebagai dasar dari fungsi `HMAC-SHA512`;

Hasil dari HMAC-SHA512 dibagi menjadi dua: 256 bit pertama menjadi kunci anak (privat atau publik setelah diproses melalui ECDSA), dan 256 bit sisanya menjadi kode rantai anak.