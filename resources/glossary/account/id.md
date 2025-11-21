---
term: AKUN

---
Sesuai BIP32, dalam dompet HD (*Hierarchical Deterministic*), sebuah akun berada pada tingkat kedalaman ketiga dalam hierarki turunan. Setiap akun diberi nomor secara berurutan mulai dari `/0'/` (turunan yang diperkuat, dari `/0'/` hingga `/2^31/` atau `/2 147 483 648/`). Pada kedalaman derivasi inilah `xpubs` berada. Saat ini, biasanya hanya ada satu akun yang digunakan dalam sebuah dompet HD. Akan tetapi, pada awalnya, dompet ini dibuat untuk memisahkan berbagai kategori penggunaan di dalam dompet yang sama. Sebagai contoh, jika kita mengambil jalur derivasi standar untuk alamat penerimaan Taproot (P2TR) eksternal: `m/86'/0'/0'/0/0`, indeks yang merujuk pada akunnya adalah angka `/0'/` kedua.

![](../../dictionnaire/assets/17.webp)
