---
term: HASH256
---

Fungsi kriptografi yang digunakan untuk berbagai aplikasi pada Bitcoin. Ini melibatkan penerapan fungsi SHA256 dua kali pada data masukan. Pesan dijalankan melalui SHA256 sekali, dan hasil dari operasi ini digunakan sebagai masukan untuk satu kali lagi melalui SHA256. Keluaran dari fungsi ini oleh karena itu adalah 256 bit.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$