---
term: AKUN
---

Dalam dompet HD (Hierarchical Deterministic), sebuah akun mewakili lapisan derivasi pada kedalaman 3 menurut BIP32. Setiap akun diberi nomor secara berurutan mulai dari `/0'/` (derivasi yang diperkuat, sehingga dalam kenyataannya `/2^31/` atau `/2 147 483 648/`). Pada kedalaman derivasi inilah `xpubs` yang terkenal itu berada. Saat ini, biasanya hanya satu akun yang digunakan dalam sebuah dompet HD. Namun, pada awalnya, mereka dirancang untuk memisahkan berbagai kategori penggunaan dalam dompet yang sama. Sebagai contoh, jika kita mengambil jalur derivasi standar untuk alamat penerimaan Taproot eksternal (P2TR): `m/86'/0'/0'/0/0`, indeks akun adalah `/0'/` kedua.

![](../../dictionnaire/assets/17.png)