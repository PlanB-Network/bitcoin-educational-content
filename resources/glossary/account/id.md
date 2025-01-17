---
term: REKENING

---
Dalam dompet HD (Hierarchical Deterministic), sebuah akun merepresentasikan sebuah lapisan derivasi pada kedalaman 3 menurut BIP32. Setiap akun diberi nomor secara berurutan mulai dari `/0'/` (derivasi yang diperkeras, sehingga pada kenyataannya `/2^31/` atau `/2 147 483 648/`). Pada kedalaman derivasi inilah `xpubs` yang terkenal berada. Saat ini, biasanya hanya satu akun yang digunakan dalam sebuah dompet HD. Akan tetapi, pada awalnya, dompet ini dibuat untuk memisahkan berbagai kategori penggunaan di dalam dompet yang sama. Sebagai contoh, jika kita mengambil jalur derivasi standar untuk alamat penerimaan Taproot (P2TR) eksternal: `m/86'/0'/0'/0/0`, indeks akunnya adalah `/0'/` yang kedua.

![](../../dictionnaire/assets/17.webp)